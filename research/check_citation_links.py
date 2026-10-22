#!/usr/bin/env python3
"""Read-only bibliography link/identity audit; no claim that inaccessible links are broken."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from difflib import SequenceMatcher
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
FILES = ['core.bib', 'thermal.bib', 'transport.bib', 'information.bib']

def balanced(s, pos):
    start = pos
    depth = 0
    for i in range(pos, len(s)):
        if i and s[i-1] == '\\':
            continue
        if s[i] == '{':
            depth += 1
        elif s[i] == '}':
            depth -= 1
            if depth == 0:
                return s[start+1:i], i+1
    raise ValueError('Unbalanced bibliography braces')

def entries(path):
    s = path.read_text()
    out = []
    for m in re.finditer(r'@(\w+)\s*\{([^,\s]+),', s):
        body, end = balanced(s, s.index('{', m.start()))
        body = body.split(',', 1)[1]
        item = {'file': path.name, 'key': m.group(2), 'type': m.group(1)}
        pos = 0
        while True:
            f = re.search(r'([A-Za-z][\w-]*)\s*=\s*', body[pos:])
            if not f:
                break
            field = f.group(1).lower()
            pos += f.end()
            if pos >= len(body):
                break
            if body[pos] == '{':
                value, pos = balanced(body, pos)
            elif body[pos] == '"':
                finish = body.index('"', pos+1)
                value = body[pos+1:finish]
                pos = finish+1
            else:
                finish = body.find(',', pos)
                if finish < 0:
                    finish = len(body)
                value = body[pos:finish].strip()
                pos = finish
            item[field] = value
        out.append(item)
    return out

class Meta(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {}
        self.in_title = False
        self.title = ''
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta':
            key = a.get('name', a.get('property', '')).lower()
            self.meta.setdefault(key, []).append(a.get('content', ''))
        if tag == 'title':
            self.in_title = True
    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
    def handle_data(self, data):
        if self.in_title:
            self.title += data

def check(url):
    result = {'url': url}
    started = time.monotonic()
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'QuantumDynamicsTextbookCitationAudit/1.0',
            'Accept': 'text/html,application/xhtml+xml,application/pdf;q=0.8,*/*;q=0.5',
        })
        with urllib.request.urlopen(req, timeout=16) as r:
            result.update(status=r.status, final_url=r.url,
                          content_type=r.headers.get('Content-Type', ''))
            raw = r.read(750000)
        if 'html' in result['content_type']:
            page = raw.decode('utf8', 'replace')
            parser = Meta(); parser.feed(page)
            result['page_title'] = parser.title.strip()
            result['metadata'] = {k: v for k, v in parser.meta.items()
                                  if k.startswith(('citation_', 'dc.', 'dc:', 'prism.'))
                                  and k not in ['citation_reference', 'citation_author_institution']}
            if 'arxiv.org/abs/' in url:
                doi = re.search(r'Related DOI.*?href="(https://doi.org/[^\"]+)', page, re.S)
                journal = re.search(r'Journal(?:\s|&nbsp;|&#160;)+reference:\s*</td>\s*<td[^>]*>(.*?)</td>', page, re.S)
                if doi:
                    result['related_doi'] = html.unescape(doi.group(1))
                if journal:
                    result['journal_reference'] = re.sub('<[^>]+>', '', journal.group(1)).strip()
        result['classification'] = 'accessible'
    except urllib.error.HTTPError as e:
        result.update(status=e.code, final_url=e.url, error=str(e))
        if e.code in [404, 410]:
            result['classification'] = 'http_not_found_requires_manual_confirmation'
        elif e.code in [401, 403, 429]:
            result['classification'] = 'restricted_or_rate_limited_not_proven_broken'
        else:
            result['classification'] = 'server_error_not_proven_broken'
    except Exception as e:
        result.update(error=type(e).__name__+': '+str(e),
                      classification='transport_error_not_proven_broken')
    result['seconds'] = round(time.monotonic()-started, 2)
    return result

def normalized(title):
    return re.sub(r'[^a-z0-9]+', ' ', html.unescape(title).lower()).strip()

def main():
    records = [e for name in FILES for e in entries(ROOT/'references'/name)]
    urls = sorted(set(u for e in records for u in
                      [e.get('url'), 'https://doi.org/'+e['doi'] if e.get('doi') else None] if u))
    checked = {}
    with ThreadPoolExecutor(max_workers=7) as pool:
        tasks = {pool.submit(check,u):u for u in urls}
        for done in as_completed(tasks):
            checked[tasks[done]] = done.result()
    for e in records:
        u = e.get('url')
        meta = checked.get(u, {}).get('metadata', {})
        title = meta.get('citation_title', [''])[0]
        if title:
            e['remote_title'] = title
            e['title_similarity'] = round(SequenceMatcher(None,normalized(e.get('title','')),
                                                         normalized(title)).ratio(), 3)
        if meta.get('citation_date'):
            e['arxiv_initial_date'] = meta['citation_date']
        if checked.get(u,{}).get('related_doi'):
            e['arxiv_related_doi'] = checked[u]['related_doi']
        if checked.get(u,{}).get('journal_reference'):
            e['arxiv_journal_reference'] = checked[u]['journal_reference']
    output = {'checked_on':'2026-10-22', 'method':'HTTP GET, redirects, primary-page metadata; inaccessible is not broken',
              'records':records, 'url_results':checked}
    path = ROOT/'research'/'citation-link-results.json'
    path.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    counts = {}
    for r in checked.values():
        counts[r['classification']] = counts.get(r['classification'],0)+1
    print(json.dumps({'entries':len(records),'unique_urls':len(urls),'classifications':counts,
                      'output':str(path)},indent=2))
    for e in records:
        if e.get('title_similarity',1) < .8:
            print('TITLE_REVIEW',e['key'],repr(e['title']),repr(e['remote_title']))
    for u,r in checked.items():
        if r.get('status') in [404,410]:
            print('NOT_FOUND_REVIEW',u,r.get('final_url'))

if __name__ == '__main__':
    main()
