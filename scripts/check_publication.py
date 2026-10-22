"""Check the deployed book's pages and representative downloadable artifacts."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import json, os, subprocess, urllib.request
ROOT=Path(__file__).resolve().parents[1]
BASE=os.environ.get('BOOK_BASE_URL','https://xing-phys.github.io/quantum-many-body-dynamics').rstrip('/')
paths=sorted(p.stem+'.html' for p in ROOT.glob('*.qmd'))
paths+=['quantum-many-body-dynamics.pdf','demos/labs.js','data/ising-quench.csv',
        'figs/quasiparticle-pairs.png','references/all.bib']
def check(path):
    url=BASE+'/'+path
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'ManyBodyTextbookQA/1.0'})
        with urllib.request.urlopen(req,timeout=30) as response:
            body=response.read();status=response.status;content_type=response.headers.get('Content-Type','')
        if path.endswith('.html') and b'<html' not in body.lower():raise ValueError('HTML document missing')
        if path.endswith('.pdf'):
            if not body.startswith(b'%PDF'):raise ValueError('PDF magic missing')
            Path('/tmp/many-body-published.pdf').write_bytes(body)
        if path.endswith('.png') and not body.startswith(b'\x89PNG'):raise ValueError('PNG magic missing')
        return {'path':path,'status':status,'bytes':len(body),'content_type':content_type}
    except Exception as error:return {'path':path,'error':str(error)}
with ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(check,paths))
errors=[r for r in results if r.get('status')!=200 or 'error'in r]
report={'base_url':BASE,'checked_at_utc':datetime.now(timezone.utc).isoformat(),
        'source_checkout_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'workflow_run_id':os.environ.get('BOOK_RUN_ID',''),'results':results,'errors':errors}
(ROOT/'research/publication-check.json').write_text(json.dumps(report,indent=2)+'\n')
if errors:print(json.dumps(errors,indent=2));raise SystemExit(1)
print(f'Public HTTP checks passed: {len(results)} endpoints, including all {len(paths)-5} pages and the PDF.')
