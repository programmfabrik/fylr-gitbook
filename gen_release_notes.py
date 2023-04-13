#!/usr/bin/env python3

import sys, os, datetime, json, re, http.client, urllib.parse, tempfile, subprocess

class Github:
    def __init__(self, token):
        self.token = token

    def get_releases(self):
        con = http.client.HTTPSConnection('api.github.com')
        con.request('GET', '/repos/programmfabrik/fylr/releases', headers = {
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
           continue

    name = rel['name']
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

        if not fs.has_file(a_name):
            with tempfile.NamedTemporaryFile() as tmpfile:
                print('* fetch file {}'.format(a_url))
                gh.get_file(a_url, tmpfile)
                fs.put_file(a_name, tmpfile.name, asset['content_type'])

        md.add_raw('* [{}]({})\n'.format(asset['name'], fs.get_url(a_name)))
    md.add_raw('\n')

    md.add_raw(rel['body'])
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
