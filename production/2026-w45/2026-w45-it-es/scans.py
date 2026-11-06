# -*- coding: utf-8 -*-
"""R2 scans for IT x ES: right-edge (ADVANCE method), same-baseline
furniture-band collisions, P6 chart-label coverage (baseline-anchored
ink method, PIL getmetrics, anchor ls, threshold <30%).
Outputs printed; exit 0 iff all three scans are clean.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xml.etree.ElementTree as ET
from svglib import text_w
from svglib import _font as _getfont
from PIL import ImageFont
NS = '{http://www.w3.org/2000/svg}'
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-it-es/svg")
pages = ["p1-prima", "p2-vita", "p3-cultura", "p4-sport", "p5-giovani",
         "p6-approfondimento", "p7-lingua", "p8-valutazione"]
fails = []

# ---- 1. right edge: every text node's advance end must be <= 1910 (frame band [40,1910]); footer left/right gap reported
for p in pages:
    root = ET.parse(os.path.join(ED, p + ".svg")).getroot()
    for t in root.iter(NS + 'text'):
        txt = ''.join(t.itertext())
        try:
            x = float(t.get('x')); y = float(t.get('y'))
            size = float(t.get('font-size'))
            bold = (t.get('font-weight') in ('700', 'bold'))
            fam = t.get('font-family', '')
            kind = 'serif' if 'Serif' in fam else 'sans'
            anchor = t.get('text-anchor')
        except (TypeError, ValueError):
            continue
        w = text_w(txt, kind, bold, size)
        if anchor == 'middle':
            lo, hi = x - w / 2, x + w / 2
        elif anchor == 'end':
            lo, hi = x - w, x
        else:
            lo, hi = x, x + w
        if lo < 28 or hi > 1910:
            fails.append(f"RIGHTEDGE {p} y={y} [{lo:.1f},{hi:.1f}] {txt[:60]}")
    # footer gap
    fts = [(float(t.get('x')), ''.join(t.itertext()), float(t.get('font-size')),
            t.get('font-family', ''), t.get('font-weight')) for t in root.iter(NS + 'text')
           if t.get('y') == '2624']
    if len(fts) >= 2:
        left = [f for f in fts if f[0] < 900][0]
        right = [f for f in fts if f[0] > 900][0]
        lw = text_w(left[1], 'serif' if 'Serif' in left[3] else 'sans',
                    left[4] in ('700', 'bold'), left[2])
        rw = text_w(right[1], 'serif' if 'Serif' in right[3] else 'sans',
                    right[4] in ('700', 'bold'), right[2])
        print(f"{p} footer: left ends {left[0]+lw:.1f}, right starts {right[0]-rw:.1f}, gap {right[0]-rw-(left[0]+lw):.1f}")
print("RIGHTEDGE flags:", [f for f in fails if f.startswith('RIGHTEDGE')] or "0")

# ---- 2. same-baseline collisions on furniture bands (P1 top y=92, footers y=2624, P1 band y=478/522)
for p in pages:
    root = ET.parse(os.path.join(ED, p + ".svg")).getroot()
    by_y = {}
    for t in root.iter(NS + 'text'):
        try:
            y = float(t.get('y'))
        except (TypeError, ValueError):
            continue
        if y in (92.0, 2624.0, 478.0, 522.0):
            txt = ''.join(t.itertext())
            size = float(t.get('font-size'))
            bold = (t.get('font-weight') in ('700', 'bold'))
            fam = t.get('font-family', '')
            kind = 'serif' if 'Serif' in fam else 'sans'
            x = float(t.get('x')); anchor = t.get('text-anchor')
            w = text_w(txt, kind, bold, size)
            lo, hi = (x - w / 2, x + w / 2) if anchor == 'middle' else ((x - w, x) if anchor == 'end' else (x, x + w))
            by_y.setdefault(y, []).append((lo, hi, txt[:50]))
    for y, spans in by_y.items():
        spans.sort()
        for (l1, h1, t1), (l2, h2, t2) in zip(spans, spans[1:]):
            if h1 > l2:
                fails.append(f"ROW {p} y={y} overlap {t1!r} vs {t2!r}")
print("ROW flags:", [f for f in fails if f.startswith('ROW')] or "0")

# ---- 3. P6 chart labels vs later-drawn bars (baseline-anchored ink)
root = ET.parse(os.path.join(ED, "p6-approfondimento.svg")).getroot()
# collect rects (bars) in paint order and texts
elems = []
for el in root.iter():
    if el.tag == NS + 'rect' and el.get('fill') == '#3e4c2a':
        elems.append(('rect', float(el.get('x')), float(el.get('y')),
                      float(el.get('width')), float(el.get('height'))))
    elif el.tag == NS + 'text':
        elems.append(('text', el))
maxcov = 0.0
for i, el in enumerate(elems):
    if el[0] != 'text':
        continue
    t = el[1]
    txt = ''.join(t.itertext())
    if txt.strip() not in ("Torino", "Milano", "Bologna", "Roma", "Napoli",
                           "3°", "4°", "5°", "9°", "12°"):
        continue
    try:
        x = float(t.get('x')); y = float(t.get('y')); size = float(t.get('font-size'))
        bold = (t.get('font-weight') in ('700', 'bold'))
    except (TypeError, ValueError):
        continue
    fam = t.get('font-family', '')
    kind = 'serif' if 'Serif' in fam else 'sans'
    font = _getfont(kind, bold, int(size))
    if font is None:
        continue
    asc, desc = font.getmetrics()
    # anchor ls: baseline at y; ink box approx x..x+advance, y-asc..y+desc
    ink = (x, y - asc, x + text_w(txt, kind, bold, size), y + desc)
    ink_area = max(0, ink[2] - ink[0]) * max(0, ink[3] - ink[1])
    for el2 in elems[i + 1:]:
        if el2[0] != 'rect':
            continue
        _, rx, ry, rw, rh = el2
        ox = max(0, min(ink[2], rx + rw) - max(ink[0], rx))
        oy = max(0, min(ink[3], ry + rh) - max(ink[1], ry))
        if ink_area and ox * oy > 0:
            cov = ox * oy / ink_area
            maxcov = max(maxcov, cov)
            if cov >= 0.30:
                fails.append(f"CHART label {txt!r} covered {cov:.0%}")
print(f"CHART max label coverage: {maxcov:.1%} (threshold <30%)")
print("ALL SCANS:", "CLEAN" if not fails else fails)
sys.exit(0 if not fails else 1)
