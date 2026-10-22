# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright==1.58.0"]
# ///
"""Isolated read-only web-artifact tests; never attaches to a user browser.

Run against a served _site directory: uv run --script scripts/check_browser.py
"""
from pathlib import Path
import json, os
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
OUT=Path('/tmp/many-body-web-qa');OUT.mkdir(exist_ok=True)
BASE=os.environ.get('BOOK_BASE_URL','http://127.0.0.1:4242').rstrip('/')
results=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path='/usr/bin/google-chrome',headless=True,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1440,'height':1080},device_scale_factor=1)
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    for name in ['index','01-state-information','14-ghd','25-measurement-transitions','research-map','computational-laboratory']:
        resp=page.goto(f'{BASE}/{name}.html',wait_until='networkidle')
        page.wait_for_timeout(800)
        if name!='index':page.wait_for_selector('mjx-container',timeout=30000)
        data=page.evaluate('''() => ({title:document.title, math:document.querySelectorAll('mjx-container').length,
          mathErrors:[...document.querySelectorAll('mjx-merror')].map(e=>e.textContent),
          missingImages:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src),
          mainOverflow:document.querySelector('main').scrollWidth>document.querySelector('main').clientWidth+3,
          headings:[...document.querySelectorAll('main h1,main h2')].map(e=>e.textContent)})''')
        data.update(page=name,status=resp.status)
        assert resp.status==200,(name,resp.status)
        assert not data['mathErrors'],(name,data['mathErrors'])
        assert not data['missingImages'],(name,data['missingImages'])
        assert not data['mainOverflow'],(name,'main column overflows')
        page.screenshot(path=str(OUT/f'{name}.png'),full_page=False)
        results.append(data)
    # Check actual interactive outputs rather than merely canvas existence.
    out=page.locator('[data-lab="entanglement"] output')
    before=out.inner_text()
    page.locator('[data-lab="entanglement"] input').fill('1.57')
    page.locator('[data-lab="entanglement"] input').dispatch_event('input')
    assert out.inner_text()!=before
    page.locator('[data-lab="circuit"] [name=p]').fill('1')
    page.get_by_role('button',name='Run trajectories').click()
    page.wait_for_function("document.querySelector('[data-lab=circuit] output').textContent.includes('p=1.00')")
    assert 'final mean cut S₂=0.000' in page.locator('[data-lab="circuit"] output').inner_text()
    page.locator('[data-lab="circuit"] [name=p]').fill('0')
    page.get_by_role('button',name='Run trajectories').click()
    page.wait_for_function("document.querySelector('[data-lab=circuit] output').textContent.includes('p=0.00')")
    assert 'empirical average full state=0.000' in page.locator('[data-lab="circuit"] output').inner_text()
    # Check light/dark and a narrow screen without persistent user settings.
    page.goto(f'{BASE}/01-state-information.html',wait_until='networkidle')
    page.locator('.quarto-color-scheme-toggle').click()
    page.wait_for_function("document.body.classList.contains('quarto-dark')")
    page.wait_for_timeout(400)
    page.screenshot(path=str(OUT/'states-dark.png'))
    page.set_viewport_size({'width':390,'height':844})
    page.reload(wait_until='networkidle')
    page.wait_for_timeout(800)
    page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(OUT/'states-mobile.png'))
    assert page.evaluate('document.documentElement.scrollWidth<=window.innerWidth+3'),'mobile page overflow'
    assert not errors,errors
    browser.close()
record={'base_url':BASE,'pages':results,'interactive_limits':'p=0 and p=1 passed; slider output changed',
        'page_errors':errors,'screenshots':str(OUT),'browser':'isolated headless Google Chrome'}
(ROOT/'research/browser-check.json').write_text(json.dumps(record,indent=2)+'\n')
print('Six served pages, MathJax, image loading, interactive limits, dark/mobile screenshots passed.')
