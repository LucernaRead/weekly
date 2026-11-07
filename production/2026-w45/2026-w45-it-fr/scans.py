# -*- coding: utf-8 -*-
"""Supplementary scans for W45 IT x FR (final SVGs):
(a) same-baseline text-node spacing on furniture bands (FR x RU lesson:
    audit TEXTX only compares DIFFERENT lines);
(b) right-edge ADVANCE scan: advance right edge vs RIGHT=1885 and page
    edge 1950, all 8 pages;
(c) P6 chart-label coverage, baseline-anchored ink method (PIL getbbox
    with anchor='ls' on the baseline point), threshold <30% vs
    later-drawn rects.
Fonts mirror the build (NotoSerifCJK-Regular/Bold, NotoSansCJK-Regular/
Bold split TTCs via tables.json paths).
"""
import json, re, sys, xml.etree.ElementTree as ET
from PIL import ImageFont

ED = '/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-it-fr/svg'
PAGES = ['p1-prima', 'p2-vita', 'p3-cultura', 'p4-sport', 'p5-giovani',
         'p6-approfondimento', 'p7-lingua', 'p8-valutazione']
NS = {'s': 'http://www.w3.org/2000/svg'}
FD = '/usr/share/fonts/opentype/noto/'
FACES = {('serif', False): 'NotoSerifCJK-Regular.ttc',
         ('serif', True): 'NotoSerifCJK-Bold.ttc',
         ('sans', False): 'NotoSansCJK-Regular.ttc',
         ('sans', True): 'NotoSansCJK-Bold.ttc'}

def font_of(el):
    fam = el.get('font-family', '')
    kind = 'serif' if 'Serif' in fam else 'sans'
    bold = el.get('font-weight') in ('700', 'bold')
    size = float(el.get('font-size', 20))
    # split TTC: index 2 = SC for both families on this VM
    return ImageFont.truetype(FD + FACES[(kind, bold)], int(round(size)), index=2), size

def texts_and_rects(path):
    root = ET.parse(path).getroot()
    items = []  # (kind, x, y, w, h, text) in paint order
    for el in root.iter():
        tag = el.tag.split('}')[-1]
        if tag == 'text' and (el.text or '').strip():
            f, size = font_of(el)
            t = el.text
            adv = f.getlength(t)
            anchor = el.get('text-anchor', 'start')
            x = float(el.get('x', 0))
            if anchor == 'end':
                x0 = x - adv
            elif anchor == 'middle':
                x0 = x - adv / 2
            else:
                x0 = x
            y = float(el.get('y', 0))
            # baseline-anchored ink box: getbbox with anchor 'ls'
            l, t_, r, b = f.getbbox(t, anchor='ls')
            items.append(('text', x0, y, adv, t, (x0 + l, y + t_, x0 + r, y + b)))
        elif tag == 'rect':
            try:
                items.append(('rect', float(el.get('x', 0)), float(el.get('y', 0)),
                              float(el.get('width', 0)), float(el.get('height', 0)),
                              el.get('fill', '')))
            except ValueError:
                pass
        elif tag == 'line':
            try:
                items.append(('line', float(el.get('x1', 0)), float(el.get('y1', 0)),
                              float(el.get('x2', 0)), float(el.get('y2', 0)), ''))
            except ValueError:
                pass
    return items

def overlap(a0, a1, b0, b1):
    return max(0.0, min(a1, b1) - max(a0, b0))

row_flags, edge_flags = [], []
for pg in PAGES:
    items = texts_and_rects(f'{ED}/{pg}.svg')
    txts = [it for it in items if it[0] == 'text']
    # (a) same-baseline spacing: group by exact y, only furniture bands
    by_y = {}
    for it in txts:
        if it[2] < 600 or it[2] > 2550:  # top band + footer band
            by_y.setdefault(round(it[2], 1), []).append(it)
    for y, group in by_y.items():
        group.sort(key=lambda it: it[1])
        for a, b in zip(group, group[1:]):
            gap = b[1] - (a[1] + a[3])
            if gap < 2:
                row_flags.append((pg, y, round(gap, 1), a[4][:40], b[4][:40]))
    # (b) right-edge ADVANCE scan
    for it in txts:
        right = it[1] + it[3]
        if right > 1885:
            edge_flags.append((pg, round(it[2], 1), round(right, 1), it[4][:60]))
print('ROWCHECK same-baseline flags (<2px gap, furniture bands):', len(row_flags))
for f in row_flags:
    print('  ', f)
print('ADVANCE right-edge flags (>1885):', len(edge_flags))
for f in edge_flags:
    print('  ', f)

# (c) P6 chart-label coverage, baseline-anchored ink
items = texts_and_rects(f'{ED}/p6-approfondimento.svg')
worst = []
for i, it in enumerate(items):
    if it[0] != 'text':
        continue
    x0, yt, xb, yb = it[5]
    area = max(0.0, (xb - x0) * (yb - yt))
    if area <= 0:
        continue
    for later in items[i + 1:]:
        if later[0] != 'rect':
            continue
        rx, ry, rw, rh = later[1], later[2], later[3], later[4]
        if later[5] in ('none', ''):
            continue
        ox = overlap(x0, xb, rx, rx + rw)
        oy = overlap(yt, yb, ry, ry + rh)
        cov = ox * oy / area if area else 0
        if cov > 0:
            worst.append((round(cov * 100, 1), it[4][:50], round(x0, 1), round(yt, 1)))
worst.sort(reverse=True)
print('P6 chart-label coverage: max =', worst[0][0] if worst else 0, '% (gate <30%)')
for w in worst[:10]:
    print('  ', w)
