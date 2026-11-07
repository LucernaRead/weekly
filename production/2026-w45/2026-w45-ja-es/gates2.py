# -*- coding: utf-8 -*-
"""Round-1 supplementary gates: anchor-aware right-edge scan + P6 chart
label ink coverage vs later-drawn bar rects (occlusion_audit ink boxes)."""
import sys, os, re
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
from occlusion_audit import ink_box, parse_attrs, TAG_RE
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-ja-es/svg")
def esc(s):
    return s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
print("== 7b. right-edge scan, anchor-aware (hard: ink right > 1950) ==")
hard = 0; over = 0
for f in sorted(os.listdir(ED)):
    t = open(os.path.join(ED, f), encoding="utf-8").read()
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', t):
        a = parse_attrs(m.group(1)); s = esc(m.group(2))
        if not s.strip(): continue
        x = float(a.get("x", 0)); anchor = a.get("text-anchor", "start")
        fam = a.get("font-family", ""); size = float(a.get("font-size", 20))
        bold = a.get("font-weight", "") == "700"
        ib = ink_box(s, fam, size, bold, x, float(a.get("y", 0)), anchor)
        if ib is None: continue
        r = ib[2]
        if r > 1950: print(f"  HARD {f} y={a.get('y')} ink_right={r:.1f} :: {s[:60]!r}"); hard += 1
        elif r > 1885: print(f"  over-margin {f} y={a.get('y')} ink_right={r:.1f} :: {s[:60]!r}"); over += 1
print(f"  hard={hard} over-margin={over}")
print("== 8b. P6 chart: label ink vs later bar rects ==")
t = open(os.path.join(ED, "p6-fukayomi.svg"), encoding="utf-8").read()
els = []  # (kind, attrs, text)
for m in TAG_RE.finditer(t):
    if m.group("tattrs") is not None:
        els.append(("text", parse_attrs(m.group("tattrs")), m.group("tcontent")))
    else:
        els.append((m.group("tag"), parse_attrs(m.group("attrs")), ""))
# chart bars: rects with a solid fill other than page/box backgrounds, in chart region.
# Print all rects with fill + geometry to identify bars, then compute coverage for texts above them.
for i, (k, a, s) in enumerate(els):
    if k == "rect":
        print(f"  rect[{i}] x={a.get('x')} y={a.get('y')} w={a.get('width')} h={a.get('height')} fill={a.get('fill')}")
