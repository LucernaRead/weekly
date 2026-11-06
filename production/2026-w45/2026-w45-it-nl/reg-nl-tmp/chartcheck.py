# -*- coding: utf-8 -*-
"""P6 chart-label coverage, baseline-anchored ink method (task prescription):
PIL ImageFont.getmetrics + getbbox(anchor='ls') so the ink box is anchored
on the text baseline; coverage = overlapped ink area / ink area for each
text node vs every rect drawn LATER in paint order on P6. Gate: <30%.
Any overlap >0 is printed for triage; >=30% is a failure.
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import _font

path = sys.argv[1]
src = open(path, encoding='utf-8').read()
elems = []
for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)" fill="([^"]*)"', src):
    elems.append((m.start(), 'rect', float(m.group(1)), float(m.group(2)),
                  float(m.group(1)) + float(m.group(3)), float(m.group(2)) + float(m.group(4)), m.group(5)))
for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"( font-weight="700")?[^>]*?(?: text-anchor="(start|middle|end)")?[^>]*>([^<]*)</text>', src):
    x, y, fam, size, bold, anchor, t = (float(m.group(1)), float(m.group(2)), m.group(3),
                                        float(m.group(4)), bool(m.group(5)), m.group(6) or 'start', m.group(7))
    if not t.strip():
        continue
    kind = 'serif' if 'Serif' in fam else 'sans'
    f = _font(kind, bold, int(round(size)))
    asc, desc = f.getmetrics()
    bb = f.getbbox(t, anchor='ls')  # (left, top, right, bottom) vs baseline-left origin
    adv = f.getlength(t)
    if anchor == 'start':
        ox = x
    elif anchor == 'end':
        ox = x - adv
    else:
        ox = x - adv / 2
    elems.append((m.start(), 'text', ox + bb[0], y + bb[1], ox + bb[2], y + bb[3], t))
elems.sort()
worst = 0.0
for j, (st, k, ax, ay, bx, by, t) in enumerate(elems):
    if k != 'text':
        continue
    area = max(0.0, (bx - ax) * (by - ay))
    if area == 0:
        continue
    for (st2, k2, ax2, ay2, bx2, by2, fill) in elems[j + 1:]:
        if k2 != 'rect':
            continue
        ox = max(0.0, min(bx, bx2) - max(ax, ax2))
        oy = max(0.0, min(by, by2) - max(ay, ay2))
        cov = ox * oy / area
        if cov > 0:
            print(f'overlap {cov*100:5.1f}% text {t[:40]!r} ink=({ax:.0f},{ay:.0f},{bx:.0f},{by:.0f}) vs later rect fill={fill} ({ax2:.0f},{ay2:.0f},{bx2:.0f},{by2:.0f})')
            worst = max(worst, cov)
print(f'worst chart-label coverage: {worst*100:.1f}% (gate <30%)')
sys.exit(1 if worst >= 0.30 else 0)
