import re, glob, sys
import yaml
ROOT = '/home/hatch/workspace/weekly-git'
LANGS = ['de','fr','es','en','it','pt','nl','ru','ja','ko','zh-cn','zh-tw']
def load_md(path):
    txt = open(path, encoding='utf-8').read()
    m = re.search(r'^---\n(.*?)\n---', txt, re.S)
    fm = yaml.safe_load(m.group(1)) if m else {}
    body = txt[m.end():] if m else txt
    body = re.sub(r'data:[^"\s]*', 'DATAURI', body)
    return fm, body
print("== print covers ==")
for r in LANGS:
    p = f'{ROOT}/covers/2026-w43/2026-w43-cover-{r}/2026-w43-cover-{r}.md'
    fm, body = load_md(p)
    hl = {}
    if isinstance(fm.get('headlines'), list):
        for h in fm['headlines']:
            hl[h['lang']] = h['headline']
    print(f'{r}: fm_keys={sorted(fm.keys())} headlines={len(hl)}')
    if r == 'en':
        print('  EN headlines:', hl)
    # date-like lines in body (first 600 chars, URIs stripped)
    snippet = re.sub(r'\s+', ' ', body)[:600]
    print(f'  body[:600]: {snippet}')
print("== editions ==")
eds = {}
for p in glob.glob(f'{ROOT}/issues/2026-w43/*/2026-w43-*.md'):
    if p.endswith('.text.md'):
        continue
    fm, _ = load_md(p)
    if fm.get('kind') == 'cover':
        continue
    eds[(fm.get('target'), fm.get('native'))] = (bool(fm.get('abstract')), bool(fm.get('excerpt')))
print('edition count:', len(eds))
tg = sorted({t for t,_ in eds}); nv = sorted({n for _,n in eds})
print('targets:', tg); print('natives:', nv)
missing_abs = [k for k,v in eds.items() if not v[0]]
missing_exc = [k for k,v in eds.items() if not v[1]]
print('missing abstract:', missing_abs[:10], 'missing excerpt:', missing_exc[:10])
