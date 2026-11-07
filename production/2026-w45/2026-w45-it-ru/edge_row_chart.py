# -*- coding: utf-8 -*-
"""RU edition supplementary scans (sibling-method, tools/README lessons):
1. Right-edge ADVANCE scan: per text node, advance width by anchor vs
   frame band [40, 1910] (outer frame at 28/40); footer left/right gap.
2. Same-baseline collision scan on furniture bands (P1 top band y=92,
   every footer y=2624, P1 band rows 478/522): ink intervals on one
   baseline must not overlap (FRxRU lesson 10).
3. Frame-line scan: every page must carry the two frame rects
   (28/40) and footer rule at 2580.
4. P6 chart-label coverage, baseline-anchored ink method (PIL
   getmetrics, anchor 'ls'): label ink vs later-drawn rects, <30%.
"""
import re, sys
from xml.etree import ElementTree as ET
from PIL import ImageFont
import glob, os

ED = 'files/weekly-report-w45-it-ru/svg'
CORE = 'files/weekly-report-w45-it-core/svg'
SANS = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
SANSB = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
SERIF = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc'
SERIFB = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'
def font(fam, size, bold):
    base = {'Noto Sans CJK SC': SANSB if bold else SANS,
            'Noto Serif CJK SC': SERIFB if bold else SERIF}.get(fam, SANS)
    return ImageFont.truetype(base, int(round(size)), index=2)

def nodes(f):
    t = ET.parse(f); out = []
    for e in t.iter():
        if e.tag.endswith('text') and e.text:
            out.append(e)
    return out

# ---- 1. right edge ----
print('== right-edge ADVANCE scan (band [40,1910]) ==')
bad = 0
for f in sorted(glob.glob(ED + '/*.svg')):
    for e in nodes(f):
        x = float(e.get('x')); anc = e.get('text-anchor', 'start')
        size = float(e.get('font-size')); fam = e.get('font-family', 'Noto Sans CJK SC')
        bold = e.get('font-weight') == '700'
        w = font(fam, size, bold).getlength(e.text)
        left = x if anc == 'start' else (x - w if anc == 'end' else x - w / 2)
        right = left + w
        if left < 40 - 0.5 or right > 1910 + 0.5:
            # masthead wordmark (La Lucerna, UnifrakturMaguntia) is exempt: different font metrics
            if e.get('font-family') == 'UnifrakturMaguntia':
                continue
            print(f'  FLAG {os.path.basename(f)} y={e.get("y")} [{left:.1f},{right:.1f}] {e.text[:60]!r}')
            bad += 1
print('right-edge flags:', bad)

# ---- 2. same-baseline collisions ----
print('== same-baseline scan ==')
def ink_interval(e):
    x = float(e.get('x')); anc = e.get('text-anchor', 'start')
    size = float(e.get('font-size')); fam = e.get('font-family', 'Noto Sans CJK SC')
    bold = e.get('font-weight') == '700'
    if fam == 'UnifrakturMaguntia':
        return None
    w = font(fam, size, bold).getlength(e.text)
    left = x if anc == 'start' else (x - w if anc == 'end' else x - w / 2)
    return (left, left + w)
bad2 = 0
for f in sorted(glob.glob(ED + '/*.svg')):
    by_y = {}
    for e in nodes(f):
        iv = ink_interval(e)
        if iv is None: continue
        by_y.setdefault(float(e.get('y')), []).append((iv, e.text))
    for y, lst in by_y.items():
        lst.sort()
        for (a1, t1), (a2, t2) in zip(lst, lst[1:]):
            if a2[0] < a1[1] - 0.5:
                print(f'  OVERLAP {os.path.basename(f)} y={y}: {t1[:40]!r} {a1} vs {t2[:40]!r} {a2}')
                bad2 += 1
print('same-baseline overlaps:', bad2)

# ---- 3. frames ----
print('== frame scan ==')
for f in sorted(glob.glob(ED + '/*.svg')):
    s = open(f, encoding='utf-8').read()
    ok28 = 'x="28" y="28"' in s; ok40 = 'x="40" y="40"' in s
    okfoot = 'y1="2580"' in s or '2580' in s
    print(f'  {os.path.basename(f)} frame28={ok28} frame40={ok40} footer2580={okfoot}')

# ---- 4. P6 chart labels ----
print('== P6 chart-label coverage (baseline-anchored ink, anchor ls) ==')
f = ED + '/p6-approfondimento.svg'
t = ET.parse(f)
elems = []
for e in t.iter():
    tag = e.tag.split('}')[-1]
    if tag == 'text' and e.text:
        elems.append(('text', e))
    elif tag == 'rect':
        elems.append(('rect', e))
maxcov = 0.0; worst = None
for i, (k, e) in enumerate(elems):
    if k != 'text': continue
    txt = e.text
    if not any(c in txt for c in ['Torino', 'Milano', 'Bologna', 'Roma', 'Napoli']) and not re.fullmatch(r'[0-9]+°?', txt.strip()):
        continue
    x = float(e.get('x')); y = float(e.get('y'))
    size = float(e.get('font-size')); fam = e.get('font-family', 'Noto Sans CJK SC')
    bold = e.get('font-weight') == '700'
    fn = font(fam, size, bold)
    asc, desc = fn.getmetrics()
    w = fn.getlength(txt)
    anc = e.get('text-anchor', 'start')
    left = x if anc == 'start' else (x - w if anc == 'end' else x - w / 2)
    ink = (left, y - asc, left + w, y + desc)
    for k2, r in elems[i+1:]:
        if k2 != 'rect': continue
        rx, ry = float(r.get('x')), float(r.get('y'))
        rw, rh = float(r.get('width')), float(r.get('height'))
        fill = r.get('fill', 'none')
        if fill in ('none', 'transparent'): continue
        ix = max(0, min(ink[2], rx + rw) - max(ink[0], rx))
        iy = max(0, min(ink[3], ry + rh) - max(ink[1], ry))
        area = (ink[2]-ink[0]) * (ink[3]-ink[1])
        cov = (ix * iy / area) if area else 0
        if cov > maxcov:
            maxcov = cov; worst = (txt, cov, (rx, ry, rw, rh))
    print(f'  label {txt[:30]!r} at ({x},{y}) checked')
print(f'max chart-label coverage: {maxcov*100:.1f}% (threshold <30%) worst={worst}')
