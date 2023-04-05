#!/usr/bin/env python3

import sys, os, datetime, json, re, http.client

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

class MDPage:
    def __init__(self):
        self._text = ''

    def add_header(self, header, level = 1):
        self._text += '\n' + '#' * level + ' ' + header + '\n'

    def _fix_md(self, text):
        return re.sub('^# ', '## ', text).replace('\r\n', '\n')\

    def add_raw(self, text):
        self._text += self._fix_md(text)

    def write(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok = True)
        with open(filename, 'w') as f:
            f.write(self._text)

gh = Github(sys.argv[1])
rels_per_year = {}

# per-release pages
for rel in gh.get_releases():
    if rel.get('prerelease') or rel.get('draft'):
           continue

    name = rel['name']
    tag = rel['tag_name']
    year = datetime.datetime.fromisoformat(rel['published_at']).year

    if year not in rels_per_year:
        rels_per_year[year] = []
    rels_per_year[year].append((tag, name))

    fn = 'releases/{}/{}.md'.format(year, tag)

    md = MDPage()
    md.add_header(name)
    md.add_raw('\nPublished {}\n\n'.format(rel['published_at'].replace('T', ' ')))
    md.add_raw(rel['body'])
    md.write(fn)

# releases summaries
for year, rels in rels_per_year.items():
    md = MDPage()
    md.add_header(str(year))
    for tup in rels:
        md.add_raw('* [{}]({}/{}.md)\n'.format(tup[1], year, tup[0]))
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
                    lines.append('    * [{}](releases/{}/{}.md)\n'.format(tup[1], year, tup[0]))
        i += 1

with open('SUMMARY.md', 'w') as f:
    for line in lines:
        f.write(line)
