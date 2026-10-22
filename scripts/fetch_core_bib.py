"""Refresh arXiv records and apply reviewed published-paper metadata.

The arXiv BibTeX export can retain preprint years/titles after publication.
references/core.overrides.json preserves verified publisher corrections.
Never run this network refresh during rendering.
"""
import concurrent.futures, json, pathlib, re, time, urllib.request
ROOT = pathlib.Path(__file__).resolve().parents[1]
ids = json.loads((ROOT / 'references/core.ids.json').read_text())
override_path = ROOT / 'references/core.overrides.json'
overrides = json.loads(override_path.read_text()).get('records', {}) if override_path.exists() else {}

def set_field(raw, field, value):
    """Replace one braced/quoted/simple BibTeX value, preserving other fields."""
    match = re.search(r'(?im)^\s*' + re.escape(field) + r'\s*=\s*', raw)
    replacement = '      ' + field + '={' + str(value) + '}'
    if match is None:
        end = raw.rfind('}')
        prefix = raw[:end].rstrip()
        if not prefix.endswith(','):
            prefix += ','
        return prefix + '\n' + replacement + ',\n' + raw[end:]
    start = match.end()
    if raw[start] == '{':
        depth, end = 1, start + 1
        while depth:
            if raw[end] == '{' and raw[end-1] != '\\':
                depth += 1
            elif raw[end] == '}' and raw[end-1] != '\\':
                depth -= 1
            end += 1
    elif raw[start] == '"':
        end = start + 1
        while raw[end] != '"' or raw[end-1] == '\\':
            end += 1
        end += 1
    else:
        end = raw.find(',', start)
        if end < 0:
            end = raw.rfind('}')
    return raw[:match.start()] + replacement + raw[end:]

def apply_publication_override(key, raw):
    override = overrides.get(key)
    if not override:
        return raw
    entry_type = override.get('entry_type', 'article')
    raw = re.sub(r'^\s*@\w+\{', '@' + entry_type + '{', raw, count=1)
    for field, value in override.get('fields', {}).items():
        raw = set_field(raw, field, value)
    return raw
def fetch(item):
    key, ident = item
    url = 'https://arxiv.org/bibtex/' + ident
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'ResearchTextbook/1.0'})
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode()
            if not re.match(r'@\w+\{', raw.strip()):
                raise ValueError('Not BibTeX: ' + raw[:80])
            raw = re.sub(r'(@\w+\{)[^,]+', lambda m: m[1] + key, raw, count=1)
            raw = raw.replace('doi={https://doi.org/', 'doi={')
            return key, apply_publication_override(key, raw)
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 + attempt)
def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        rows = list(pool.map(fetch, ids.items()))
    (ROOT / 'references/core.bib').write_text('\n\n'.join(raw for _, raw in rows) + '\n')
    print('Fetched', len(rows), 'arXiv records; applied',
          sum(key in overrides for key, _ in rows), 'reviewed publication overrides.')

if __name__ == '__main__':
    main()
