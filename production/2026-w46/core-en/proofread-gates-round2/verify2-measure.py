#!/usr/bin/env python3
"""Round 2 completion — independent title measurement + wrap simulation.
(1) SLOT derived from SVG geometry (box rect + title x) for P6 and P3, all editions.
(2) Title widths via svglib font metrics (advance + ink), incl. es/fr short candidates
    and no-article variants, to test whether any fuller correct form fits.
(3) Greedy char wrap simulation (sans 20.5pt, width 434) for the zh-tw P2 bridge,
    validated against the three KNOWN wraps (core 1-line, zh-tw current, B4 toolbox).
Read-only. Output to stdout (verify2-measure.log).
"""
import re, sys
from pathlib import Path
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-build')
from svglib import text_w, _font

BASE = Path.home()/'workspace/goals/lucernaread-social-media-operations/files'
EDDIR = {'core':'weekly-report-w46-en-core'}
for e in ['de','es','fr','it','ja','ko','nl','pt','ru','zh-tw']:
    EDDIR[e]=f'weekly-report-w46-en-{e}'

print('===== 1. SLOT FROM SVG GEOMETRY =====')
for pagefile, label in [('p6-politique.svg','P6'),('p3-culture.svg','P3')]:
    for ed in ['core','de','es','fr','it','ja','ko','nl','pt','ru','zh-tw']:
        svg=(BASE/EDDIR[ed]/'svg'/pagefile).read_text(encoding='utf-8')
        # title element: the 23pt bold HOW LONG (P6) / SCROOGE-family (P3) title at x=1469
        tm=None
        for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" font-size="23" font-weight="700"[^>]*>([^<]*)</text>', svg):
            if float(m.group(1))==1469.0 and ('HOW LONG' in m.group(4) or 'SCROOGE' in m.group(4) or 'NOCHE' in m.group(4) or 'NUIT' in m.group(4)):
                tm=m; break
        if tm is None:
            print(f'{label} {ed}: TITLE NOT FOUND'); continue
        # box rect containing the title: rect with x=1451 width=434 whose y-range covers title y
        boxes=[]
        for rm in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*>', svg):
            x,y,w,h=map(float,rm.groups())
            if x==1451.0 and w==434.0 and y < float(tm.group(2)) < y+h:
                boxes.append((x,y,w,h))
        tx,ty,fam,title=float(tm.group(1)),float(tm.group(2)),tm.group(3),tm.group(4)
        bx,by,bw,bh=boxes[0]
        print(f'{label} {ed}: box x={bx} w={bw} right={bx+bw} | title x={tx} font={fam} | SLOT={bx+bw-tx:.1f} | title={title!r}')
print()
print('===== 2. TITLE WIDTHS (svglib sans bold 23pt) =====')
f=_font("sans", True, 23)
def meas(s):
    adv=text_w(s,"sans",True,23)
    l,t,r,b=f.getbbox(s); ink=r-l
    return adv, ink
cases=[
 ("B1 shipped es","HOW LONG ? · ¿Cuánto dura?"),
 ("B1 shipped pt","HOW LONG ? · Quanto dura?"),
 ("B1 shipped ru","HOW LONG ? · Каков срок?"),
 ("B1 full es","HOW LONG ? · ¿Cuánto dura el mandato?"),
 ("B1 full pt","HOW LONG ? · Quanto dura o mandato?"),
 ("B1 full ru","HOW LONG ? · Каков срок полномочий?"),
 ("B1 full ru no-?","HOW LONG ? · Каков срок полномочий"),
 ("B1 alt es cargo","HOW LONG ? · ¿Cuánto dura el cargo?"),
 ("B1 alt es mandato-short","HOW LONG ? · ¿Cuánto dura el mandato"),
 ("B1 alt ru srok-only-q","HOW LONG ? · Каков срок полномочий?"),
 ("M4 shipped nl","SCROOGE'S NIGHT · Scrooge-nacht"),
 ("M4 shipped pt","SCROOGE'S NIGHT · A noite"),
 ("M4 full nl","SCROOGE'S NIGHT · De nacht van Scrooge"),
 ("M4 no-article nl","SCROOGE'S NIGHT · Nacht van Scrooge"),
 ("M4 full pt","SCROOGE'S NIGHT · A noite de Scrooge"),
 ("M4 no-article pt","SCROOGE'S NIGHT · Noite de Scrooge"),
 ("M4 full-caps nl","SCROOGE'S NIGHT · DE NACHT VAN SCROOGE"),
 ("M4 full-caps pt","SCROOGE'S NIGHT · A NOITE DE SCROOGE"),
 ("ES/FR shipped es","LA NOCHE DE SCROOGE"),
 ("ES/FR shipped fr","LA NUIT DE SCROOGE"),
 ("ES/FR short-mixed es","SCROOGE'S NIGHT · La noche"),
 ("ES/FR short-mixed fr","SCROOGE'S NIGHT · La nuit"),
 ("ES/FR full-mixed es","SCROOGE'S NIGHT · La noche de Scrooge"),
 ("ES/FR full-mixed fr","SCROOGE'S NIGHT · La nuit de Scrooge"),
 ("ES/FR no-article es","SCROOGE'S NIGHT · Noche de Scrooge"),
 ("ES/FR no-article fr","SCROOGE'S NIGHT · Nuit de Scrooge"),
 ("ES/FR bare es","SCROOGE'S NIGHT · Noche"),
 ("ES/FR bare fr","SCROOGE'S NIGHT · Nuit"),
 ("ES/FR full-caps es","SCROOGE'S NIGHT · LA NOCHE DE SCROOGE"),
 ("ES/FR full-caps fr","SCROOGE'S NIGHT · LA NUIT DE SCROOGE"),
]
SLOT=416.0
for name,s in cases:
    adv,ink=meas(s)
    print(f'{adv:7.1f}px advance ink {ink:7.1f}px {"OVERFLOW +%.1f"%(adv-SLOT) if adv>SLOT else "fits spare %.1f"%(SLOT-adv)}  {name}: {s!r}')
print()
print('===== 3. GREEDY WRAP SIMULATION (sans 20.5pt, width 434) =====')
def cw(ch):
    return text_w(ch,"sans",False,20.5)
def greedy(s, width=434.0):
    lines=[]; cur=''; curw=0.0
    for ch in s:
        w=cw(ch)
        if cur and curw+w>width:
            lines.append(cur); cur=ch; curw=w
        else:
            cur+=ch; curw+=w
    if cur: lines.append(cur)
    return lines
def check(label, s, expect):
    lines=greedy(s)
    print(f'{label}: {len(lines)} line(s) expect={expect} {"MATCH" if len(lines)==expect[0] and lines==expect[1] else "CHECK"}')
    for i,l in enumerate(lines): print(f'   L{i+1} w={sum(cw(c) for c in l):.1f} {l!r}')
# validation: core bridge single line; zh-tw current 2 lines tail ）。; B4 toolbox at 22.5 serif width 434
check('core bridge', '用 will + 动词改写（承诺与将要发生的事）。', (1,['用 will + 动词改写（承诺与将要发生的事）。']))
check('zh-tw current bridge', '用 will + 動詞原形來改寫（承諾與將要發生的事）。', (2,['用 will + 動詞原形來改寫（承諾與將要發生的事','）。']))
# B4 toolbox uses serif 22.5pt: separate greedy with serif metrics
def cw_serif(ch):
    return text_w(ch,"serif",False,22.5)
def greedy_serif(s, width=434.0):
    lines=[]; cur=''; curw=0.0
    for ch in s:
        w=cw_serif(ch)
        if cur and curw+w>width:
            lines.append(cur); cur=ch; curw=w
        else:
            cur+=ch; curw+=w
    if cur: lines.append(cur)
    return lines
b4=greedy_serif('B1 — « Dickens wrote the story in 1843.»')
print('B4 fixed toolbox (serif 22.5):', b4, [round(sum(cw_serif(c) for c in l),1) for l in b4])
b4old=greedy_serif('B1 — « Dickens wrote the story in 1843. »')
print('B4 old toolbox (serif 22.5):', b4old, [round(sum(cw_serif(c) for c in l),1) for l in b4old])
print()
print('--- zh-tw bridge candidates (must end with content-bearing final line) ---')
cands=[
 ('drop 來 (pre-fix wording)', '用 will + 動詞原形改寫（承諾與將要發生的事）。'),
 ('drop 原形, keep 來', '用 will + 動詞來改寫（承諾與將要發生的事）。'),
 ('shorten tail: 承諾與未來', '用 will + 動詞原形來改寫（承諾與未來）。'),
 ('reword: 表達承諾', '用 will + 動詞原形改寫，表達承諾與將要發生的事。'),
 ('drop 。 (no final stop)', '用 will + 動詞原形來改寫（承諾與將要發生的事）'),
 ('drop parens', '用 will + 動詞原形來改寫，承諾與將要發生的事。'),
]
for label,s in cands:
    lines=greedy(s)
    print(f'{label}: {len(lines)} line(s)')
    for i,l in enumerate(lines): print(f'   L{i+1} w={sum(cw(c) for c in l):.1f} {l!r}')
print('DONE verify2-measure')
