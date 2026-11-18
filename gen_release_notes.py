#!/usr/bin/env python3

import sys, os, datetime, json, re, glob, http.client, urllib.parse, tempfile, subprocess, tarfile, textwrap

# number of most recent releases fetched from github. releases older than that
# are kept in the index pages as they are, they are never regenerated.
RELEASES_PER_PAGE = 10

# assets of a release which are no downloads.
# the complete release notes: github cuts the text of a release at 125000
# characters, the page of the release takes them from this asset.
NOTES_ASSET = 'fylr_release-notes.md'
# the release records: one file per tag with the digests of its docker images,
# published in _assets/releases/, where the maintain script reads them.
RECORDS_ASSET = 'fylr_release-records.tar.gz'
RECORDS_DIR = '_assets/releases'

class Github:
    def __init__(self, token):
        self.token = token

    def get_releases(self):
        con = http.client.HTTPSConnection('api.github.com')
        con.request('GET', '/repos/programmfabrik/fylr/releases?per_page={}'.format(RELEASES_PER_PAGE), headers = {
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


ENTRY_RE = re.compile(r'^\* \[(?P<name>.*) \((?P<date>\d{4}-\d{2}-\d{2})\)\]\((?P<year>\d{4})/(?P<tag>.*)\.md\)$')

def read_existing_rels():
    """collect the releases already listed in releases/<year>.md, so that
    releases which are not fetched from github anymore are not dropped."""
    rels_per_year = {}
    for fn in glob.glob('releases/[0-9][0-9][0-9][0-9].md'):
        year = int(os.path.basename(fn)[:-3])
        rels = []
        with open(fn, 'r') as f:
            for line in f:
                m = ENTRY_RE.match(line.rstrip('\n'))
                if m is not None:
                    rels.append((m.group('tag'), m.group('name'), m.group('date')))
        rels_per_year[year] = rels
    return rels_per_year

def merge_rel(rels, tup):
    """add/update a release in a list ordered by descending date"""
    for i, old in enumerate(rels):
        if old[0] == tup[0]:
            rels[i] = tup   # known release, keep its position
            return
    for i, old in enumerate(rels):
        if old[2] <= tup[2]:
            rels.insert(i, tup)
            return
    rels.append(tup)

# the docker images and the checksums of the downloads: the release has them
# above its notes, the page at its end, as sections of their own.
DIGESTS_RE = re.compile(r'\A(?:### (?:Docker images|Downloads \(SHA-256\))\n\n```\n.*?\n```\n+)+', flags = re.S)

def digests_last(body):
    body = body.replace('\r\n', '\n')
    m = DIGESTS_RE.match(body)
    if m is None:
        return body
    digests = re.sub('^### ', '## ', m.group(0), flags = re.M)
    return body[m.end():].rstrip('\n') + '\n\n' + digests.rstrip('\n') + '\n'

IMAGE_RE = re.compile(r'docker\.fylr\.io/(?P<repo>fylr/[a-z-]+)@(?P<digest>sha256:[0-9a-f]{64})')
record_warnings = []
record_errors = []

def record_serial(text):
    m = re.search(r'^serial (\d+)$', text, flags = re.M)
    return int(m.group(1)) if m else 0

def record_version(text):
    m = re.search(r'^version (\S+)$', text, flags = re.M)
    return m.group(1) if m else ''

def registry_digest(repo, tag):
    """the digest docker.fylr.io serves a tag as, None if it has no such tag"""
    con = http.client.HTTPSConnection('docker.fylr.io')
    con.request('HEAD', '/v2/{}/manifests/{}'.format(repo, tag), headers = {
        'Accept': ', '.join([
            'application/vnd.docker.distribution.manifest.v2+json',
            'application/vnd.oci.image.manifest.v1+json',
            'application/vnd.docker.distribution.manifest.list.v2+json',
            'application/vnd.oci.image.index.v1+json' ]) })
    res = con.getresponse()
    return res.getheader('Docker-Content-Digest') if res.status == 200 else None

def put_records(tarname):
    """unpack the release records of a release into _assets/releases/. a
    record only replaces an older record of its tag: each final release has
    one for latest, and the releases come newest first."""
    with tarfile.open(tarname) as tar:
        for member in tar.getmembers():
            if not member.isfile():
                continue
            tag = os.path.basename(member.name)
            text = tar.extractfile(member).read().decode('utf-8', 'replace')
            images = [IMAGE_RE.fullmatch(line[6:]) for line in text.splitlines() if line.startswith('image ')]
            if not re.fullmatch(r'[A-Za-z0-9._-]+', tag) \
                    or not text.startswith('fylr-release 1\ntag {}\n'.format(tag)) \
                    or not images or None in images:
                raise Exception('not a release record: {}'.format(member.name))

            fn = os.path.join(RECORDS_DIR, tag)
            if os.path.exists(fn):
                with open(fn, 'r') as f:
                    if record_serial(f.read()) >= record_serial(text):
                        continue

            # the record is what the release pushed. tell when the registry
            # serves the tag as something else. the tag of the version itself
            # is pushed once: served as another image, its record is not taken.
            differs = []
            moved = False
            for image in images:
                served = registry_digest(image.group('repo'), tag)
                if served != image.group('digest'):
                    differs.append('{}:{} is {} in the registry, its release record says {}'.format(
                        image.group('repo'), tag, served, image.group('digest')))
                    moved = moved or (served is not None and tag == record_version(text))
            if moved:
                record_errors.extend(differs)
                continue
            record_warnings.extend(differs)

            os.makedirs(RECORDS_DIR, exist_ok = True)
            with open(fn, 'w') as f:
                f.write(text)
            print('* release record {}'.format(fn))

# the third-party software of the newest release which carries it (6.36 and
# later): its LEGAL.md and its lists of the libraries and of the programs become
# the pages of third-party-software/, whose first page links the SBOMs of that
# release. an asset of a release is named fylr_<tag>_<suffix>.
THIRD_PARTY_DIR = 'third-party-software'
THIRD_PARTY_PAGES = [
    # suffix of the asset, page, title in the table of contents, the title
    # the page gets above the text (None: the text has its own), description
    ('LEGAL.md', 'legal-notices.md', 'Legal notices', 'Legal notices',
        'The license of fylr and the license texts of the third-party software it ships, as fylr shows them under About.'),
    ('libraries.md', 'libraries.md', 'Libraries', None,
        'The third-party components fylr is built from, with the license each one is distributed under.'),
    ('programs.md', 'programs.md', 'Programs', None,
        'The external programs a fylr installation runs, what each one is used for, and the license it is distributed under.'),
]
THIRD_PARTY_SBOMS = [
    ('sbom_image.cdx.json', 'the container image: fylr, the programs it runs and the packages of its operating system'),
    ('sbom_binary.cdx.json', 'the downloads: what the fylr binary links, and the web frontend inside it'),
]
THIRD_PARTY_LINKS = {
    'LEGAL.md': 'the license of fylr and the license text of every library, as fylr shows them under *About*. A release ships them as `LEGAL.md`, next to `LICENSE`.',
    'libraries.md': 'the libraries and their licenses at a glance.',
    'programs.md': 'the programs fylr runs, what for, and their licenses.',
}

def third_party_assets(rel):
    """the assets of a release by their suffix, when it has the third-party
    pages: a release without LEGAL.md has none."""
    prefix = 'fylr_{}_'.format(rel['tag_name'])
    found = { asset['name'][len(prefix):]: asset for asset in rel['assets'] if asset['name'].startswith(prefix) }
    return found if 'LEGAL.md' in found else {}

def version_key(tag):
    return tuple(int(n) for n in re.findall(r'\d+', tag.split('-')[0]))

FENCE_RE = re.compile(r'^ {0,3}(`{3,}|~{3,})')

def demote(text):
    """every heading one level down, for a text below the title of a page. a
    heading underlined with = becomes one with ##. a code block stays as it
    is."""
    out = []
    fence = None
    for line in text.split('\n'):
        m = FENCE_RE.match(line)
        if fence is not None:
            closing = line.strip()
            if closing and set(closing) == {fence[0]} and len(closing) >= len(fence):
                fence = None
        elif m:
            fence = m.group(1)
        elif re.fullmatch(r'=+\s*', line) and out and out[-1].strip() and not out[-1].startswith('#'):
            out[-1] = '## ' + out[-1].strip()
            continue
        elif re.match(r'#{1,5} ', line):
            line = '#' + line
        out.append(line)
    return '\n'.join(out)

def front_matter(description):
    return '---\ndescription: >-\n{}\n---\n\n'.format('\n'.join('  ' + l for l in textwrap.wrap(description, 76)))

def compiled_for(tag, published):
    """the note at the head of a page of the third-party software: the release
    it is compiled from. published is the day of the release, YYYY-MM-DD, or
    empty for a build which is not published."""
    day = ', published {}'.format(published) if published else ''
    return ('{{% hint style="info" %}}\nCompiled from fylr **{}**{}, the newest release. '
        'Each release replaces these pages with its own.\n{{% endhint %}}\n\n').format(tag, day)

def below_title(text, note):
    """the note below the title of a page, the first heading # of its text."""
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('# '):
            return '\n'.join(lines[:i + 1]) + '\n\n' + note + '\n'.join(lines[i + 1:]).lstrip('\n')
    return note + text

def put_third_party(tag, published, texts, downloads):
    """write the pages of the third-party software of a release, published on
    the day YYYY-MM-DD. texts are the page assets by their suffix, downloads
    the (name, url, what) of its SBOMs."""
    os.makedirs(THIRD_PARTY_DIR, exist_ok = True)
    note = compiled_for(tag, published)
    md = front_matter('What fylr is made of: the third-party software it ships, the license of each, and the SBOMs of a release.')
    md += '# Third-party software\n\n' + note
    md += 'fylr is built from third-party software: libraries compiled into the fylr binary and into the web frontend, and programs a fylr installation runs.\n\n'
    for suffix, page, toc, title, description in THIRD_PARTY_PAGES:
        if suffix not in texts:
            continue
        text = texts[suffix].replace('\r\n', '\n').strip('\n') + '\n'
        if title is not None:
            text = '# {}\n\n{}'.format(title, demote(text))
        with open(os.path.join(THIRD_PARTY_DIR, page), 'w') as f:
            f.write(front_matter(description) + below_title(text, note))
        print('* third-party page {}/{}'.format(THIRD_PARTY_DIR, page))
        md += '* [{}]({}): {}\n'.format(toc, page, THIRD_PARTY_LINKS[suffix])
    if downloads:
        md += '\n## SBOM\n\n'
        md += 'A release lists what it is made of as a Software Bill of Materials, in CycloneDX 1.6 (JSON). The ones of {}:\n\n'.format(tag)
        for name, url, what in downloads:
            md += '* [{}]({}): {}.\n'.format(name, url, what)
        md += '\nThe page of every release under [Releases](../releases/README.md) links its own.\n'
    with open(os.path.join(THIRD_PARTY_DIR, 'README.md'), 'w') as f:
        f.write(md)
    print('* third-party page {}/README.md'.format(THIRD_PARTY_DIR))

gh = Github(sys.argv[1])
rels_per_year = read_existing_rels()

fs = Filestore()

# the newest release with the third-party pages: (tag, day published, assets)
third_party = None

# per-release pages
for rel in gh.get_releases():
    if rel.get('draft'):
        print("skip %s: draft" % (rel['name']))
        continue

    special = { asset['name']: asset for asset in rel['assets'] if asset['name'] in (NOTES_ASSET, RECORDS_ASSET) }

    # a pre-release has release records too, but no page
    if RECORDS_ASSET in special:
        with tempfile.NamedTemporaryFile() as tmpfile:
            a_url = special[RECORDS_ASSET]['url']
            gh.get_file(a_url, tmpfile)
            put_records(tmpfile.name)

    if rel.get('prerelease'):
        print("skip %s: prerelease" % (rel['name']))
        continue

    print("release %s..." % (rel['name']))

    name = rel['name'].strip()
    tag = rel['tag_name']
    year = datetime.datetime.fromisoformat(rel['published_at'][:10]).year

    assets = third_party_assets(rel)
    if assets and (third_party is None or version_key(tag) > version_key(third_party[0])):
        third_party = (tag, rel['published_at'][:10], assets)

    if year not in rels_per_year:
        rels_per_year[year] = []
    merge_rel(rels_per_year[year], (tag, name, rel['published_at'][:10]))

    fn = 'releases/{}/{}.md'.format(year, tag)

    md = MDPage()
    md.add_header(name)
    md.add_raw('\nPublished {}\n\n'.format(rel['published_at'].replace('T', ' ')))

    for asset in rel["assets"]:
        if asset['name'] in special:
            continue
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

    body = rel['body']
    if NOTES_ASSET in special:
        with tempfile.NamedTemporaryFile() as tmpfile:
            a_url = special[NOTES_ASSET]['url']
            gh.get_file(a_url, tmpfile)
            with open(tmpfile.name, 'r', encoding = 'utf-8') as f:
                body = f.read()

    md.add_raw(digests_last(body))
    md.write(fn)

# the pages of the third-party software. the loop above has put the SBOMs into
# the filestore, like every download.
if third_party is not None:
    tag, published, assets = third_party
    texts = {}
    for suffix, page, toc, title, description in THIRD_PARTY_PAGES:
        if suffix in assets:
            with tempfile.NamedTemporaryFile() as tmpfile:
                gh.get_file(assets[suffix]['url'], tmpfile)
                with open(tmpfile.name, 'r', encoding = 'utf-8') as f:
                    texts[suffix] = f.read()
    downloads = [ (assets[suffix]['name'], fs.get_url(tag + '/' + assets[suffix]['name']), what)
        for suffix, what in THIRD_PARTY_SBOMS if suffix in assets ]
    put_third_party(tag, published, texts, downloads)

# releases summaries, newest year first
years = sorted(rels_per_year.keys(), reverse = True)

for year in years:
    rels = rels_per_year[year]
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
            for year in years:
                lines.append('  * [{}](releases/{}.md)\n'.format(year, year))
                for tup in rels_per_year[year]:
                    lines.append('    * [{} ({})](releases/{}/{}.md)\n'.format(tup[1], tup[2], year, tup[0]))
        i += 1

with open('SUMMARY.md', 'w') as f:
    for line in lines:
        f.write(line)

if record_warnings:
    print('\nWARNING: the registry does not serve what a release record says. Either a newer')
    print('release is pushed but not published yet, or the tag was changed in the registry:')
    for warning in record_warnings:
        print('* ' + warning)

if record_errors:
    print('\nERROR: the registry serves the tag of a version as another image than its release')
    print('pushed. Such a tag is pushed once. These release records were NOT taken:')
    for error in record_errors:
        print('* ' + error)
    sys.exit(1)
