"""Source and rendered-book integrity checks, using only Python standard libraries."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import collections, json, re, sys
ROOT=Path(__file__).resolve().parents[1];errors=[]
qmds=list(ROOT.glob('*.qmd'))
bib=(ROOT/'references/all.bib').read_text()
keys=set(re.findall(r'@\w+\{\s*([^,]+)',bib))
labels=collections.defaultdict(list);words=0;equations=0;citations=set()
for p in qmds:
    text=p.read_text();words+=len(text.split());equations+=len(re.findall(r'\{#eq-',text))
    prose=re.sub(r'```.*?```', '', text, flags=re.S)
    for label in re.findall(r'\{#([\w-]+)',text):labels[label].append(p.name)
    for key in re.findall(r'(?<![\w/])@([A-Za-z0-9][\w:.-]*)',prose):
        key=key.rstrip('.:')
        if key.startswith(('eq-','fig-','tbl-','sec-','lst-','thm-','lem-','prp-','cor-','def-','exm-','exr-','cnj-')):continue
        citations.add(key)
        if key not in keys:errors.append(f'{p.name}: missing citation {key}')
    if text.count('$$')%2:errors.append(f'{p.name}: unbalanced display math delimiters')
for label,files in labels.items():
    if len(files)>1:errors.append(f'duplicate label {label}: {files}')
alltext='\n'.join(p.read_text() for p in qmds)
for key in re.findall(r'@((?:eq|fig|tbl|sec)-[\w-]+)',alltext):
    if key not in labels:errors.append('undefined cross-reference '+key)
for p in qmds:
    prose=re.sub(r'```.*?```', '', p.read_text(), flags=re.S)
    prose=re.sub(r'\$\$.*?\$\$|\$[^$]*\$', '', prose, flags=re.S)
    for target in re.findall(r'\]\(([^)\s]+)',prose):
        if target.startswith(('http:','https:','mailto:','#','<')):continue
        path=unquote(target.split('#')[0])
        if path and not (p.parent/path).exists():errors.append(f'{p.name}: missing linked source/asset {path}')
class Page(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.ids=set();self.links=[];self.math=0;self.matherrors=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id'in a:self.ids.add(a['id'])
        if tag in ('a','img','script','iframe','link'):
            u=a.get('href') if tag in ('a','link') else a.get('src')
            if u:self.links.append((tag,u))
        if 'math'in a.get('class','').split():self.math+=1
        if tag=='mjx-merror':self.matherrors.append(a)
if '--rendered'in sys.argv:
    site=ROOT/'_site';pages={}
    for p in site.rglob('*.html'):
        parsed=Page();parsed.feed(p.read_text());pages[p.resolve()]=parsed
        if parsed.matherrors:errors.append(f'{p}: MathJax error')
        if re.search(r'quarto-unresolved-ref|\?\?@|\[\?\?\?\]',p.read_text()):errors.append(f'{p}: unresolved reference marker')
    for p,parsed in pages.items():
        for tag,url in parsed.links:
            u=urlsplit(url)
            if u.scheme or u.netloc or url.startswith(('data:','javascript:')):continue
            if not u.path:target=p
            elif u.path.startswith('/'):
                # GitHub project-site absolute path.
                rel=u.path.removeprefix('/quantum-many-body-dynamics/')
                target=(site/rel.lstrip('/')).resolve()
            else:target=(p.parent/unquote(u.path)).resolve()
            if target.is_dir():target=target/'index.html'
            if not target.exists():errors.append(f'{p.relative_to(site)}: missing {tag} {url}');continue
            if u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
                # Browser text fragments are not ID targets.
                if not u.fragment.startswith(':~:'):errors.append(f'{p.relative_to(site)}: missing anchor {url}')
    pdf=site/'quantum-many-body-dynamics.pdf'
    if not pdf.exists():errors.append('Combined PDF missing')
    expected=len(qmds)
    print(f'Rendered: {len(pages)} HTML pages, {sum(x.math for x in pages.values())} math spans; PDF exists={pdf.exists()}.')
print(f'Sources: {len(qmds)} root QMD files, {words:,} whitespace words including equations/code, {equations} labeled equations, {len(keys)} selected sources, {len(citations)} directly cited keys.')
if errors:
    print('\n'.join(sorted(set(errors))));sys.exit(1)
print('Citation, label, asset, and requested navigation checks passed.')
