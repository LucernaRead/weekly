# -*- coding: utf-8 -*-
"""Right-edge scan, ADVANCE method (task prescription): for every <text>
node, the right edge is the advance edge (start: x+adv; middle: x+adv/2;
end: x). Flag any text whose advance edge passes the content right edge
(1885) or the page frame lines (1910/1922). Also flag any stroked box
rect whose right edge passes 1885 (box pressing the frame zone).
"""
import re, sys, glob, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import _font

bad = 0
for path in sorted(glob.glob(os.path.join(sys.argv[1], '*.svg'))):
    src = open(path, encoding='utf-8').read()
    for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*stroke="([^"]+)"', src):
        x, y, w = float(m.group(1)), float(m.group(2)), float(m.group(3))
        if x in (28.0, 40.0) and y in (28.0, 40.0):
            continue  # the page frame rects themselves
        if x + w > 1885:
            print(f'{os.path.basename(path)} BOX right={x+w:.0f} > 1885 (x={x:.0f} w={w:.0f})')
            bad += 1
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', src):
        attrs, t = m.group(1), m.group(2)
        if not t.strip():
            continue
        xm = re.search(r'x="([\d.]+)"', attrs)
        fam = re.search(r'font-family="([^"]+)"', attrs)
        size = re.search(r'font-size="([\d.]+)"', attrs)
        am = re.search(r'text-anchor="(start|middle|end)"', attrs)
        if not (xm and fam and size):
            continue
        x = float(xm.group(1))
        anchor = am.group(1) if am else 'start'
        kind = 'serif' if 'Serif' in fam.group(1) else 'sans'
        bold = 'font-weight="700"' in attrs
        adv = _font(kind, bold, int(round(float(size.group(1))))).getlength(t)
        edge = x + adv if anchor == 'start' else (x if anchor == 'end' else x + adv / 2)
        y = re.search(r'y="([\d.]+)"', attrs)
        yy = float(y.group(1)) if y else 0
        if edge > 1910:
            print(f'{os.path.basename(path)} y={yy:.0f} advance-right={edge:.1f} > 1910 FRAME :: {t[:70]!r}')
            bad += 1
        elif edge > 1885:
            print(f'{os.path.basename(path)} y={yy:.0f} advance-right={edge:.1f} in (1885,1910] margin zone :: {t[:70]!r}')
print('frame violations (>1910):', bad)
sys.exit(1 if bad else 0)
