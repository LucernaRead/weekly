# -*- coding: utf-8 -*-
"""P6 chart label ink coverage by later-drawn bar rects (baseline-anchored
true ink boxes from occlusion_audit)."""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
from occlusion_audit import ink_box, parse_attrs, TAG_RE
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
t = open(os.path.join(BASE, "files/weekly-report-w45-ja-es/svg/p6-fukayomi.svg"), encoding="utf-8").read()
els = []
for m in TAG_RE.finditer(t):
    if m.group("tattrs") is not None:
        els.append(("text", parse_attrs(m.group("tattrs")), m.group("tcontent")))
    else:
        els.append((m.group("tag"), parse_attrs(m.group("attrs")), ""))
bars = [(i, a) for i, (k, a, s) in enumerate(els) if k == "rect" and a.get("fill") == "#3e4c2a" and float(a.get("width", 0)) > 100]
print("bars:", [(i, a.get("x"), a.get("y"), a.get("width"), a.get("height")) for i, a in bars])
def area(b): return max(0.0, b[2]-b[0]) * max(0.0, b[3]-b[1])
def inter(a, b):
    x0, y0 = max(a[0], b[0]), max(a[1], b[1]); x1, y1 = min(a[2], b[2]), min(a[3], b[3])
    return max(0.0, x1-x0) * max(0.0, y1-y0)
for i, (k, a, s) in enumerate(els):
    if k != "text": continue
    y = float(a.get("y", 0))
    if not (1550 <= y <= 1830): continue
    s2 = s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    ib = ink_box(s2, a.get("font-family", ""), float(a.get("font-size", 20)), a.get("font-weight", "") == "700", float(a.get("x", 0)), y, a.get("text-anchor", "start"))
    if ib is None: continue
    cov = 0.0; hit = None
    for bi, ba in bars:
        if bi <= i: continue
        r = (float(ba["x"]), float(ba["y"]), float(ba["x"]) + float(ba["width"]), float(ba["y"]) + float(ba["height"]))
        c = inter(ib, r) / area(ib) if area(ib) else 0
        if c > cov: cov, hit = c, bi
    print(f"  text[{i}] y={y} ink=({ib[0]:.1f},{ib[1]:.1f},{ib[2]:.1f},{ib[3]:.1f}) maxcov={cov*100:.1f}% bar={hit} :: {s2[:60]!r}")
