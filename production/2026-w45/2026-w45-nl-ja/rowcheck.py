# -*- coding: utf-8 -*-
"""Same-baseline text-ink collision scan (README #10) + P6 chart-label
coverage with the BASELINE-ANCHORED method (PIL getmetrics ascent/descent,
anchor ls) — NOT getbbox, whose ascender-relative box inflates readings."""
import re, os, sys
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
from PIL import ImageFont

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-ja/svg")
FONTS = OA.FONTS

def parse_texts(path):
    raw = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'<text\b([^>]*)>([^<]*)</text>', raw):
        attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        out.append({"x": float(attrs.get("x", 0)), "y": float(attrs.get("y", 0)),
                    "size": float(attrs.get("font-size", 20)),
                    "fam": attrs.get("font-family", ""),
                    "bold": attrs.get("font-weight", "") in ("700", "bold"),
                    "anchor": attrs.get("text-anchor", "start"),
                    "text": m.group(2)})
    return out

print("== SAME-BASELINE INK SCAN (overlap = gap < 0) ==")
total_over = 0
for f in sorted(os.listdir(ED)):
    els = parse_texts(os.path.join(ED, f))
    by_y = {}
    for e in els:
        by_y.setdefault(round(e["y"], 1), []).append(e)
    for y, group in sorted(by_y.items()):
        if len(group) < 2:
            continue
        boxes = []
        for e in group:
            b = OA.ink_box(e["text"], e["fam"], e["size"], e["bold"], e["x"], e["y"], e["anchor"])
            if b:
                boxes.append((b[0], b[2], e["text"][:40]))
        boxes.sort()
        for (l1, r1, t1), (l2, r2, t2) in zip(boxes, boxes[1:]):
            gap = l2 - r1
            if gap < 0:
                total_over += 1
                print(f"  OVERLAP {f} y={y} gap={gap:.1f} :: {t1!r} vs {t2!r}")
print(f"  same-baseline overlaps: {total_over}")

print("== P6 CHART-LABEL COVERAGE (getmetrics baseline-anchored boxes) ==")
p6 = os.path.join(ED, "p6-verdieping.svg")
raw = open(p6, encoding="utf-8").read()
texts = parse_texts(p6)
rects = []
for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="(#[0-9a-f]+)"', raw):
    x, y, w, h, fill = float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4)), m.group(5)
    if fill == "#3e4c2a" and h == 18:  # olive bars only
        rects.append((x, y, w, h))
print(f"  bars found: {rects}")
# chart labels: serif bold 19.5 texts in col3 (x>=1451) with y in chart area
def ls_box(e):
    path, index = OA.resolve_font(e["fam"], e["size"], e["bold"])
    font = ImageFont.truetype(path, int(round(e["size"])), index=index)
    asc, desc = font.getmetrics()
    adv = font.getlength(e["text"])
    if e["anchor"] == "end":
        left, right = e["x"] - adv, e["x"]
    elif e["anchor"] == "middle":
        left, right = e["x"] - adv / 2, e["x"] + adv / 2
    else:
        left, right = e["x"], e["x"] + adv
    return (left, e["y"] - asc, right, e["y"] + desc)
for e in texts:
    if e["fam"] == "Noto Serif CJK JP" and e["bold"] and e["size"] == 19.5 and e["x"] >= 1451:
        box = ls_box(e)
        area = (box[2] - box[0]) * (box[3] - box[1])
        cov = 0.0
        for (rx, ry, rw, rh) in rects:
            ix = max(0, min(box[2], rx + rw) - max(box[0], rx))
            iy = max(0, min(box[3], ry + rh) - max(box[1], ry))
            cov += ix * iy
        pct = 100 * cov / area if area else 0
        print(f"  label {e['text']!r} baseline y={e['y']} box={[round(v,1) for v in box]} coverage={pct:.1f}%")
