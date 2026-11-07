#!/usr/bin/env python3
"""Round 3 independent proofreader checks (verify3). Read-only.
Parses shipped SVGs directly; measures with each build's own svglib.
"""
import re, sys, html
from pathlib import Path
from collections import Counter
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-build')
from svglib import text_w, _font
BASE = Path.home()/'workspace/goals/lucernaread-social-media-operations/files'
GATE = Path.home()/'workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-proofread-gates-round3'
TEXT_RE = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)
ATTR_RE = re.compile(r'(\w[\w-]*?)="([^"]*)"')
def texts_of(p):
    raw = Path(p).read_text(encoding='utf-8', errors='replace')
    out=[]
    for i,m in enumerate(TEXT_RE.finditer(raw)):
        attrs=dict(ATTR_RE.findall(m.group(1)))
        inner=re.sub(r'<[^>]+>','',m.group(2))
        inner=html.unescape(inner)
        out.append({'i':i,'x':attrs.get('x'),'y':attrs.get('y'),'size':attrs.get('font-size'),
                    'weight':attrs.get('font-weight'),'anchor':attrs.get('text-anchor'),
                    'fam':attrs.get('font-family'),'text':inner})
    return out

print('===== FIX R-B6: zh-tw P2 bridge =====')
svg = BASE/'weekly-report-w46-en-zh-tw/svg/p2-life.svg'
ts = texts_of(svg)
bridge=[t for t in ts if '動詞原形' in t['text']]
for t in bridge: print(t)
print('lone-punct elements on P2 (text stripped in punctuation-only set):')
punct=set('。）。，、；：？！」』）》】·—-')
for t in ts:
    st=t['text'].strip()
    if st and all(c in punct for c in st): print('  LONE', t)
print('elements at y 2067.225 (old line-2 baseline):', [t for t in ts if t['y']=='2067.225'])
print('ex16 elements y~2098:', [(t['x'],t['y'],t['text']) for t in ts if t['y'] in ('2098.225','2099.225')][:8])

print()
print('===== FIX R-M4: es/fr P3 titles =====')
for ed, exp in [('es',"SCROOGE'S NIGHT · La noche"),('fr',"SCROOGE'S NIGHT · La nuit")]:
    svg=BASE/f'weekly-report-w46-en-{ed}/svg/p3-culture.svg'
    raw=svg.read_text(encoding='utf-8')
    ts=texts_of(svg)
    titles=[t for t in ts if t['x']=='1469' and t['y']=='873']
    print(ed, 'title elements at 1469/873:', titles)
    print(ed, 'expected present as single element:', any(t['text']==exp for t in titles))
    print(ed, 'old title present:', any('LA NOCHE DE SCROOGE' in t['text'] or 'LA NUIT DE SCROOGE' in t['text'] for t in ts))
    # slot geometry
    boxes=[]
    for rm in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*>', raw):
        x,y,w,h=map(float,rm.groups())
        if x==1451.0 and w==434.0 and y<873<y+h: boxes.append((x,y,w,h))
    print(ed, 'box:', boxes, 'SLOT=', 1885.0-1469.0 if boxes else None)
    # width measurement sans bold 23pt (build svglib, SC font per shipped element)
    adv=text_w(exp,"sans",True,23)
    f=_font("sans",True,23); l,t_,r,b=f.getbbox(exp); ink=r-l
    print(ed, f'measured advance={adv:.1f}px ink={ink:.1f}px slot=416.0 fits={adv<=416.0} spare={416.0-adv:.1f}')
    # other P3 titles at same slot in other editions for pattern check
print('P3 title pattern, all 11 (x=1469 y=873):')
for ed in ['core','de','es','fr','it','ja','ko','nl','pt','ru','zh-tw']:
    d='weekly-report-w46-en-core' if ed=='core' else f'weekly-report-w46-en-{ed}'
    ts=texts_of(BASE/d/'svg/p3-culture.svg')
    tt=[t['text'] for t in ts if t['x']=='1469' and t['y']=='873']
    print(' ', ed, tt)

print()
print('===== LONE-PUNCT SCAN: all 8 pages x 3 editions =====')
for ed in ['es','fr','zh-tw']:
    d=f'weekly-report-w46-en-{ed}'
    for svg in sorted((BASE/d/'svg').glob('*.svg')):
        for t in texts_of(svg):
            st=t['text'].strip()
            if st and all(c in punct for c in st):
                print(' ', ed, svg.stem, t)

print()
print('===== BRIDGE WRAP SIMULATION (zh-tw build svglib, sans 20.5pt, width 434) =====')
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-zh-tw-build')
import importlib
import svglib as svgtw
def cw(ch): return svgtw.text_w(ch,"sans",False,20.5)
def greedy(s, width=434.0):
    lines=[]; cur=''; curw=0.0
    for ch in s:
        w=cw(ch)
        if cur and curw+w>width: lines.append(cur); cur=ch; curw=w
        else: cur+=ch; curw+=w
    if cur: lines.append(cur)
    return lines
for label,s in [('old R2 text','用 will + 動詞原形來改寫（承諾與將要發生的事）。'),
                ('new R3 text','用 will + 動詞原形改寫，承諾與將要發生的事。'),
                ('core bridge (simplified control)','用 will + 动词改写（承诺与将要发生的事）。')]:
    lines=greedy(s)
    print(label, len(lines), 'line(s)')
    for l in lines: print(f'   w={sum(cw(c) for c in l):.1f} {l!r}')

print()
print('===== R2->R3 MULTISET DIFF (vs Round 2 texts dir, my own loader) =====')
def load(p):
    c=Counter()
    for line in open(p, encoding='utf-8'):
        m=re.match(r'^\[(\S+)#\d+ [^\]]*\] (.*)$', line.rstrip('\n'))
        if m: c[(m.group(1),m.group(2))]+=1
        else: c[('?',line)]+=1
    return c
R2=Path.home()/'workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-proofread-gates-round2/texts'
for ed in ['es','fr','zh-tw']:
    out=[]
    d=f'weekly-report-w46-en-{ed}'
    for svg in sorted((BASE/d/'svg').glob('*.svg')):
        for i,t in enumerate(texts_of(svg)):
            out.append(f"[{svg.stem}#{i} x={t['x']} y={t['y']} {t['size']}pt w={t['weight']} a={t['anchor']}] {t['text']}")
    (GATE/f'verify3-texts-{ed}.txt').write_text('\n'.join(out)+'\n', encoding='utf-8')
    print(ed, 'extracted', len(out), 'elements -> verify3-texts-%s.txt'%ed)
    # load my own extraction in same (page,text) form
    b=Counter()
    for line in out:
        m=re.match(r'^\[(\S+)#\d+ [^\]]*\] (.*)$', line)
        b[(m.group(1),m.group(2))]+=1
    a=load(R2/f'texts-{ed}.txt')
    d1,d2=a-b,b-a
    print(f'== {ed}: only-Round2 {sum(d1.values())}, only-Round3 {sum(d2.values())}')
    for k,v in sorted(d1.items()): print('  R2-only', v, k)
    for k,v in sorted(d2.items()): print('  R3-only', v, k)
print('DONE verify3-checks')
