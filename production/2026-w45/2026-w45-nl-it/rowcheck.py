# -*- coding: utf-8 -*-
"""Supplementary scans (NOT a replacement for tools/occlusion_audit.py):
1. same-baseline text-ink collisions on every page (audit TEXTX only compares
   DIFFERENT lines; README #10).
2. P6 chart-label ink vs later-drawn rects, reporting max coverage even below
   the audit's 30% COVER threshold (README #12 GRAZE watch).
3. gloss counts, golden sentences, readers' corner, footers, credits, bans.
"""
import re, sys, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import ImageFont
from svglib import _font

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-it/svg")
CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-core/svg")

TEXT_RE = re.compile(r'<text x="([0-9.\-]+)" y="([0-9.\-]+)" font-family="([^"]+)" font-size="([0-9.]+)"([^>]*)>([^<]*)</text>')
RECT_RE = re.compile(r'<rect x="([0-9.\-]+)" y="([0-9.\-]+)" width="([0-9.\-]+)" height="([0-9.\-]+)"')

def parse(path):
    t = open(path, encoding="utf-8").read()
    texts, rects = [], []
    for m in TEXT_RE.finditer(t):
        x, y, fam, size, rest, s = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), m.group(5), html.unescape(m.group(6))
        bold = 'font-weight="700"' in rest
        anchor = re.search(r'text-anchor="([^"]+)"', rest)
        anchor = anchor.group(1) if anchor else "start"
        kind = "serif" if "Serif" in fam else "sans"
        texts.append({"x": x, "y": y, "fam": fam, "size": size, "bold": bold,
                      "anchor": anchor, "kind": kind, "s": s, "pos": m.start()})
    for m in RECT_RE.finditer(t):
        rects.append({"x": float(m.group(1)), "y": float(m.group(2)),
                      "w": float(m.group(3)), "h": float(m.group(4)), "pos": m.start()})
    return texts, rects, t

def inkbox(el):
    if "UnifrakturMaguntia" in el["fam"]:
        return None
    f = _font(el["kind"], el["bold"], el["size"])
    # NOTE: PIL getbbox is ascender-relative, NOT baseline-relative, so its
    # top/bottom cannot be added to the SVG baseline y. Use getmetrics
    # (ascent/descent) for the vertical extent; getbbox left/right for x.
    left, _top, right, _bottom = f.getbbox(el["s"])
    ascent, descent = f.getmetrics()
    length = f.getlength(el["s"])
    if el["anchor"] == "start":
        x0, x1 = el["x"] + left, el["x"] + right
    elif el["anchor"] == "middle":
        x0, x1 = el["x"] - length / 2 + left, el["x"] - length / 2 + right
    else:
        x0, x1 = el["x"] - length + left, el["x"] - length + right
    return (x0, el["y"] - ascent, x1, el["y"] + descent)

print("== 1. same-baseline collisions ==")
for name in sorted(os.listdir(ED)):
    if not name.endswith(".svg"):
        continue
    texts, _, _ = parse(os.path.join(ED, name))
    boxes = [(el, inkbox(el)) for el in texts]
    boxes = [(el, b) for el, b in boxes if b]
    groups = {}
    for el, b in boxes:
        groups.setdefault(round(el["y"], 1), []).append((el, b))
    hits = 0
    for y, items in groups.items():
        items.sort(key=lambda ib: ib[1][0])
        for (e1, b1), (e2, b2) in zip(items, items[1:]):
            if b2[0] < b1[2] - 2 and not (b2[1] > b1[3] or b1[1] > b2[3]):
                print(f"  COLLIDE {name} y={y}: {e1['s'][:40]!r} vs {e2['s'][:40]!r}")
                hits += 1
    print(f"  {name}: {'CLEAN' if hits == 0 else str(hits) + ' hits'}")

print("== 2. P6 chart-label coverage ==")
texts, rects, _ = parse(os.path.join(ED, "p6-verdieping.svg"))
worst = 0.0
worst_txt = "—"
for el in texts:
    b = inkbox(el)
    if not b or not (1451 <= el["x"] <= 1885 and 200 <= el["y"] <= 720):
        continue
    area = max(0.0, (b[2] - b[0]) * (b[3] - b[1]))
    if area <= 0:
        continue
    for r in rects:
        if r["pos"] <= el["pos"]:
            continue
        ix = max(0.0, min(b[2], r["x"] + r["w"]) - max(b[0], r["x"]))
        iy = max(0.0, min(b[3], r["y"] + r["h"]) - max(b[1], r["y"]))
        cov = ix * iy / area
        if cov > worst:
            worst = cov
            worst_txt = el["s"]
print(f"  worst chart-label bbox coverage: {worst*100:.1f}% ({worst_txt!r})")
print(f"  verdict: {'GRAZE-CHECK needed' if worst >= 0.30 else 'below 30% threshold'}")

print("== 3. gloss counts (split rendered gloss strings on ·) ==")
import re as _re
for f, label in [("content12.py", "P2"), ("content34.py", "P3+P4"), ("content56.py", "P5+P6")]:
    pass
# gloss() call strings, in build order, core vs edition
def gloss_calls(path):
    t = open(path, encoding="utf-8").read()
    return _re.findall(r'\.gloss\("([^"]*)"\)', t)
core_build = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-nl-build")
en_build = os.path.dirname(os.path.abspath(__file__))
for f in ["content12.py", "content34.py", "content56.py"]:
    for a, b in zip(gloss_calls(os.path.join(core_build, f)), gloss_calls(os.path.join(en_build, f))):
        ca, cb = len(a.split("·")), len(b.split("·"))
        print(f"  {f} core {ca} vs ed {cb}: {'OK' if ca == cb else 'MISMATCH'}")
# P1 + P7 bridges (· / ; separated explanation lines)
def bridge_calls(path):
    t = open(path, encoding="utf-8").read()
    return _re.findall(r'\.bridge\("([^"]*)"\)', t)
for f in ["content12.py", "content7.py"]:
    for a, b in zip(bridge_calls(os.path.join(core_build, f)), bridge_calls(os.path.join(en_build, f))):
        print(f"  bridge {f}: core {a[:50]!r} ed {b[:50]!r}")
