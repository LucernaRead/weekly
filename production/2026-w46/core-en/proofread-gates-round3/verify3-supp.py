#!/usr/bin/env python3
"""Round 3 supplementary checks (verify3-supp). Read-only."""
import re, html, json
from pathlib import Path
BASE = Path.home()/'workspace/goals/lucernaread-social-media-operations/files'
HF = Path.home()/'workspace/goals/lucernaread-social-media-operations/hidden_files/w46'

print('===== S1. LOWERCASE MATCHING LETTERS (20 keys) raw-SVG parse =====')
reg=json.loads((HF/'en-core/registry.json').read_text(encoding='utf-8'))
regk={str(e['n']): e['key'] for e in reg}
match_nums=[str(n) for n in list(range(24,28))+list(range(38,42))+list(range(56,60))+list(range(74,78))+list(range(141,145))]
print('matching keys (registry):', {n: regk[n] for n in match_nums})
pat=re.compile(r"(?<!\d)(\d{1,3})\. ([a-d])(?=[\s·\(\),;。：、！？（]|$)")
bad=0
for name in ['core','es','fr','zh-tw']:
    d=BASE/('weekly-report-w46-en-core' if name=='core' else f'weekly-report-w46-en-{name}')
    s=(d/'svg/p8-exercices.svg').read_text(encoding='utf-8')
    els=re.findall(r'<text x="([^"]+)" y="([^"]+)"[^>]*>([^<]*)</text>', s)
    els=[(float(x),float(y),html.unescape(t)) for x,y,t in els if float(y)>1850]
    cols={}
    for x,y,t in els: cols.setdefault(round(x),[]).append((y,t))
    txt=' '.join(' '.join(t for _,t in sorted(cols[x])) for x in sorted(cols))
    got={m.group(1): m.group(2) for m in pat.finditer(txt)}
    found=sum(1 for n in match_nums if n in got)
    for n in match_nums:
        if got.get(n)!=regk[n]:
            bad+=1; print(f'  MISMATCH {name} #{n}: registry {regk[n]!r} printed {got.get(n)!r}')
    print(name, 'matching letters found:', found, '/20')
print('matching-letter checks: 80, mismatches:', bad)

print()
print('===== S2. P1 SUBTITLE LINE SIZE (the 42pt FR line) =====')
for name in ['core','es','fr','zh-tw','de','it']:
    d=BASE/('weekly-report-w46-en-core' if name=='core' else f'weekly-report-w46-en-{name}')
    s=(d/'svg/p1-front.svg').read_text(encoding='utf-8')
    for m in re.finditer(r'<text x="975" y="(3[0-9][0-9])"[^>]*font-size="(\d+)"[^>]*>([^<]*)</text>', s):
        print(name, 'y=', m.group(1), 'size:', m.group(2), repr(html.unescape(m.group(3))[:70]))

print()
print('===== S3. DISTINCTIVE SIMPLIFIED-ONLY CHARS IN zh-tw (must be absent) =====')
alltxt=''
for svg in sorted((BASE/'weekly-report-w46-en-zh-tw/svg').glob('*.svg')):
    alltxt+=svg.read_text(encoding='utf-8')
distinct='说读为国学语讲译来发过时见长门问题话将这个对与从会发'
hits={c: alltxt.count(c) for c in distinct if c in alltxt}
print('distinctive simplified hits:', hits)
print('Traditional counterparts present:', {c: alltxt.count(c) for c in '說讀為國學語講譯來發過時見長門問題話將這個對與從會' if c in alltxt})

print()
print('===== S4. P6 RECT COUNT (all) + CHART TEXT ROWS =====')
for name in ['core','es','fr','zh-tw']:
    d=BASE/('weekly-report-w46-en-core' if name=='core' else f'weekly-report-w46-en-{name}')
    s=(d/'svg/p6-politique.svg').read_text(encoding='utf-8')
    print(name, 'all <rect:', s.count('<rect'), '| chart-ish lines:')
    for m in re.finditer(r'<text[^>]*>([^<]*)</text>', s):
        t=html.unescape(m.group(1))
        if re.search(r'days after|Senate|House|2022|certif', t): print('   ', repr(t))

print()
print('===== S5. CLOZE 112 OPTION C CONTINUATION =====')
s=(BASE/'weekly-report-w46-en-core/svg/p8-exercices.svg').read_text(encoding='utf-8')
texts=re.findall(r'<text[^>]*>([^<]*)</text>', s)
for i,t in enumerate(texts):
    if t.startswith('112.'): print('112 el:', repr(html.unescape(t)), '| next:', repr(html.unescape(texts[i+1])) if i+1<len(texts) else None)
print('DONE verify3-supp')
