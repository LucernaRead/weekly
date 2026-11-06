# -*- coding: utf-8 -*-
"""Same-baseline ink-spacing scan (tools README #10 lesson):
for every page, group text nodes by exact baseline y; within a group,
flag pairs whose PIL ink intervals overlap horizontally."""
import re, glob, sys, os
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-pt-build")
from svglib import _font

ED = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-core/svg"
flags = 0
for s in sorted(glob.glob(ED + "/*.svg")):
    raw = open(s, encoding="utf-8").read()
    nodes = re.findall(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"([^>]*)>(.*?)</text>', raw)
    by_y = {}
    for x, y, fam, size, rest, txt in nodes:
        size = float(size); x = float(x); y = float(y)
        bold = "700" in rest
        anchor = "middle" if "middle" in rest else ("end" if "end" in rest else "start")
        kind = "serif" if "Serif" in fam else "sans"
        f = _font(kind, bold, int(size) if size == int(size) else size)
        # ink box: use getbbox on the string at anchor
        try:
            l, t, r, b = f.getbbox(txt)
        except Exception:
            continue
        # getbbox is relative to anchor point (0, baseline); adjust for anchor
        if anchor == "middle":
            x0, x1 = x + l - f.getlength(txt) / 2, x + r - f.getlength(txt) / 2
        elif anchor == "end":
            x0, x1 = x + l - f.getlength(txt), x + r - f.getlength(txt)
        else:
            x0, x1 = x + l, x + r
        by_y.setdefault(y, []).append((x0, x1, txt))
    for y, items in by_y.items():
        items.sort()
        for (a0, a1, at), (b0, b1, bt) in zip(items, items[1:]):
            if b0 < a1 - 1:  # overlap beyond 1px tolerance
                print(f"{os.path.basename(s)} y={y}: OVERLAP '{at[:30]}' [{a0:.0f},{a1:.0f}] vs '{bt[:30]}' [{b0:.0f},{b1:.0f}]")
                flags += 1
print("same-baseline flags:", flags)
