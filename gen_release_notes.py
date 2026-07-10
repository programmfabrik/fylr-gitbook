#!/usr/bin/env python3

import sys, os, datetime, json, re, http.client, urllib.parse, tempfile, subprocess

# Category and area emoji used to give the generated release notes a light
# "chip" design: an at-a-glance count row plus emoji-tagged headers.
CATEGORY_EMOJI = {'Important': '⚠️', 'New': '✨', 'Improved': '⬆️', 'Fixed': '🔧'}
AREA_EMOJI = {'Server': '🖥️', 'Plugins': '🔌', 'Frontend': '🎨'}

def decorate_release_body(body):
    """Count the top-level items per category and prefix the category (### New,
    …) and area (## Server, …) headers with an emoji. Returns (counts, body)."""
    counts = {c: 0 for c in CATEGORY_EMOJI}
    cat = None
    for line in body.splitlines():
        m = re.match(r'^### (Important|New|Improved|Fixed)\s*$', line)
        if m:
            cat = m.group(1)
            continue
        if line.startswith('### '):
            cat = None
            continue
        if cat and re.match(r'^\* \*\*', line):
            counts[cat] += 1
    body = re.sub(r'^### (Important|New|Improved|Fixed)\s*$',
                  lambda m: '### {} {}'.format(CATEGORY_EMOJI[m.group(1)], m.group(1)),
                  body, flags=re.M)
    for area, emoji in AREA_EMOJI.items():
        body = re.sub(r'^## {}\s*$'.format(re.escape(area)),
                      '## {} {}'.format(emoji, area), body, flags=re.M)
    return counts, body

def chip_row(counts):
    """Render the '**At a glance:** `⚠️ N Important` · …' pill row, dropping
    categories with no items. Empty string when nothing was counted."""
    chips = ['`{} {} {}`'.format(CATEGORY_EMOJI[c], counts[c], c)
             for c in ('Important', 'New', 'Improved', 'Fixed') if counts[c]]
    return '**At a glance:** ' + ' · '.join(chips) if chips else ''

class Github:
    def __init__(self, token):
        self.token = token

    def get_releases(self):
        con = http.client.HTTPSConnection('api.github.com')
        con.request('GET', '/repos/programmfabrik/fylr/releases?per_page=100', headers = {
            'User-Agent': 'PF Release Notes Update/1.0',
            'Authorization': 'Bearer ' + self.token })
        res = con.getresponse()
        if res.status != 200:
            raise Exception('failed to get releases: HTTP {}: {}'.format(res.status, res.read()))
        return json.loads(res.read())

    def get_file(self, url, tmpfile):
        parsed = urllib.parse.urlparse(url)
        con = http.client.HTTPSConnection(parsed.netloc)
        con.request('GET', parsed.path, headers = {
            'User-Agent': 'PF Release Notes Update/1.0',
            'Accept': 'application/octet-stream',
            'Authorization': 'Bearer ' + self.token })
        res = con.getresponse()

        # expect redirect to actual location
        if res.status != 302:
            raise Exception('getting asset redirect failed ({} - {})'.format(a_url, res.status))

        loc = res.getheader('location')
        if loc is None:
            raise Exception('getting asset location failed ({})'.format(a_url))

        parsed = urllib.parse.urlparse(loc)
        con = http.client.HTTPSConnection(parsed.netloc)
        con.request('GET', parsed.path + '?' + parsed.query)
        res = con.getresponse()

        if res.status != 200:
            raise Exception('getting asset failed ({} - {})'.format(loc, res.status))

        tmpfile.write(res.read())
        tmpfile.flush()

class MDPage:
    def __init__(self):
        self._text = ''

    def add_header(self, header, level = 1):
        self._text += '\n' + '#' * level + ' ' + header + '\n'

    def _fix_md(self, text):
        return re.sub('^# ', '## ', text, flags = re.M).replace('\r\n', '\n')\

    def add_raw(self, text):
        self._text += self._fix_md(text)

    def write(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok = True)
        with open(filename, 'w') as f:
            f.write(self._text)

class Filestore:
    def get_url(self, filename):
        return 'https://s3.eu-central-1.wasabisys.com/fylr-releases/' + urllib.parse.quote(filename)

    def has_file(self, filename):
        con = http.client.HTTPSConnection('s3.eu-central-1.wasabisys.com')
        con.request('HEAD', '/fylr-releases/' + urllib.parse.quote(filename))
        res = con.getresponse()
        return res.status == 200

    def put_file(self, filename, tmpfile, content_type):
        run = subprocess.run([
            'aws', 's3api', 'put-object',
            '--endpoint=https://s3.eu-central-1.wasabisys.com',
            '--bucket=fylr-releases',
            '--acl=public-read',
            '--content-type={}'.format(content_type),
            '--key={}'.format(filename),
            '--body={}'.format(tmpfile),
            ], capture_output=True)
        if run.returncode != 0:
            raise Exception('s3 upload failed:\n**stdout:\n{}\n**stderr:\n{}'.format(
                run.stdout.decode('utf-8'), run.stderr.decode('utf-8')))


gh = Github(sys.argv[1])
rels_per_year = {}

fs = Filestore()

# per-release pages
for rel in gh.get_releases():
    if rel.get('prerelease') or rel.get('draft'):
        print("skip %s: prerelease=%s, draft=%s" % (rel['name'], rel.get('prerelease'), rel.get('draft')))
        continue

    print("release %s..." % (rel['name']))

    name = rel['name'].strip()
    tag = rel['tag_name']
    year = datetime.datetime.fromisoformat(rel['published_at'][:10]).year

    if year not in rels_per_year:
        rels_per_year[year] = []
    rels_per_year[year].append((tag, name, rel['published_at'][:10]))

    fn = 'releases/{}/{}.md'.format(year, tag)

    md = MDPage()
    md.add_header(name)
    md.add_raw('\nPublished {}\n\n'.format(rel['published_at'].replace('T', ' ')))

    for asset in rel["assets"]:
        a_name = tag + "/" + asset['name']
        a_url = asset['url']
        print('* checking file {}'.format(a_url))
        if not fs.has_file(a_name):
            with tempfile.NamedTemporaryFile() as tmpfile:
                print('* copy file {}'.format(a_url))
                gh.get_file(a_url, tmpfile)
                fs.put_file(a_name, tmpfile.name, asset['content_type'])
        else:
            print('* found {}'.format(a_url))

        md.add_raw('* [{}]({})\n'.format(asset['name'], fs.get_url(a_name)))
    md.add_raw('\n')

    counts, body = decorate_release_body(rel['body'])
    chips = chip_row(counts)
    if chips:
        md.add_raw(chips + '\n\n')
    md.add_raw(body)
    md.write(fn)

# releases summaries
for year, rels in rels_per_year.items():
    md = MDPage()
    md.add_header(str(year))
    for tup in rels:
        md.add_raw('* [{} ({})]({}/{}.md)\n'.format(tup[1], tup[2], year, tup[0]))
    md.write('releases/{}.md'.format(year))

# patch summary page
lines = []
with open('SUMMARY.md', 'r') as f:
    inlines = f.readlines()
    i = 0
    while i < len(inlines):
        line = inlines[i]
        lines.append(line)
        if line.startswith('* [Releases]'):
            while (i + 1) < len(inlines) and inlines[i + 1].startswith(' '):
                i += 1
            for year, rels in rels_per_year.items():
                lines.append('  * [{}](releases/{}.md)\n'.format(year, year))
                for tup in rels:
                    lines.append('    * [{} ({})](releases/{}/{}.md)\n'.format(tup[1], tup[2], year, tup[0]))
        i += 1

with open('SUMMARY.md', 'w') as f:
    for line in lines:
        f.write(line)
