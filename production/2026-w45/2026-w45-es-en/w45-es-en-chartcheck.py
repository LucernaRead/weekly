# -*- coding: utf-8 -*-
"""P6 chart GRAZE check (tools/README #12): every text ink box vs every rect
drawn LATER in paint order on the edition P6 SVG. Box fills drawn before
their text are not flagged (they precede); only later-drawn rects that
intersect earlier text ink are reported, with fill colour for triage."""
import sys, re
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-en-build')
import svglib

path = sys.argv[1]
src = open(path, encoding='utf-8').read()
pos = []
for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)" fill="([^"]*)"', src):
    pos.append((m.start(), 'rect', float(m.group(1)), float(m.group(2)),
                float(m.group(1)) + float(m.group(3)), float(m.group(2)) + float(m.group(4)), m.group(5)))
for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"( font-weight="700")?[^>]*?(?: text-anchor="(start|middle|end)")?[^>]*>([^<]*)</text>', src):
    x, y, fam, size, bold, anchor, t = (float(m.group(1)), float(m.group(2)), m.group(3),
                                         float(m.group(4)), bool(m.group(5)), m.group(6) or 'start', m.group(7))
    if not t.strip():
        continue
    kind = 'serif' if 'Serif' in fam else 'sans'
    f = svglib._font(kind, bold, int(round(size * 4)))
    bb = f.getbbox(t)
    adv = f.getlength(t) / 4.0
    l, r = bb[0] / 4.0, bb[2] / 4.0
    if anchor == 'start':
        a, b = x + l, x + r
    elif anchor == 'end':
        a, b = x - adv + l, x - adv + r
    else:
        a, b = x - adv / 2 + l, x - adv / 2 + r
    pos.append((m.start(), 'text', a, y - size, b, y + size * 0.25, t))
pos.sort()
bad = 0
for j, (st, k, ax, ay, bx, by, t) in enumerate(pos):
    if k != 'text':
        continue
    for (st2, k2, ax2, ay2, bx2, by2, fill) in pos[j + 1:]:
        if k2 != 'rect':
            continue
        if ax < bx2 and ax2 < bx and ay < by2 and ay2 < by:
            print(f'OVERLAP text {t[:44]!r} ink=({ax:.0f},{ay:.0f},{bx:.0f},{by:.0f}) vs later rect fill={fill} ({ax2:.0f},{ay2:.0f},{bx2:.0f},{by2:.0f})')
            bad += 1
print('later-rect overlaps:', bad)
