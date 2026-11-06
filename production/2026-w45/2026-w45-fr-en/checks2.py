# Gate battery v2: reuses the canonical audit's ink_box (getmetrics
# baseline-anchored true ink) -- the v1 helper used a wrong face index
# and a wrong vertical origin and is discarded.
import sys, os, re, glob
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
from occlusion_audit import ink_box
import xml.etree.ElementTree as ET
from collections import defaultdict

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = f"{BASE}/files/weekly-report-w45-fr-en"
def texts(path):
    out = []
    for el in ET.parse(path).getroot().iter():
        if el.tag.endswith("text"):
            out.append({"x": float(el.get("x") or 0), "y": float(el.get("y") or 0),
                        "size": float(el.get("font-size") or 20),
                        "bold": (el.get("font-weight") or "") in ("bold", "700"),
                        "anchor": el.get("text-anchor") or "start",
                        "fam": el.get("font-family") or "",
                        "s": "".join(el.itertext())})
    return out
def ib(n):
    return ink_box(n["s"], n["fam"], n["size"], n["bold"], n["x"], n["y"], n["anchor"])

print("== 1. same-baseline rowcheck (P1 top band y=92, band rows y=116/142, footers y=2624) ==")
bad = 0
for p in range(1, 9):
    f = sorted(glob.glob(ED + "/svg/*.svg"))[p - 1]
    rows = defaultdict(list)
    for n in texts(f):
        if n["y"] < 200 or abs(n["y"] - 2624) < 1:
            rows[round(n["y"])].append(n)
    for y, group in rows.items():
        boxes = sorted((ib(n), n["s"][:45]) for n in group)
        boxes = [(b, s) for b, s in boxes if b]
        for (b1, s1), (b2, s2) in zip(boxes, boxes[1:]):
            gap = b2[0] - b1[2]
            print(f"  p{p} y={y} gap={gap:.1f}px :: {s1!r} | {s2!r}")
            if gap < -1: bad += 1
print("  rowcheck overlaps (<-1px):", bad)

print("== 2. right-edge scan (ink right vs 1885 content edge; frame inner 1910) ==")
over = 0
for f in sorted(glob.glob(ED + "/svg/*.svg")):
    for n in texts(f):
        b = ib(n)
        if b and b[2] > 1885.5:
            print(f"  {os.path.basename(f)} y={n['y']:.0f} right={b[2]:.1f} :: {n['s'][:60]!r}")
            over += 1
print("  right-edge overflows:", over)

print("== 3. frame-line scan (ink vs outer frame 28/1922, 28/2672) ==")
cross = 0
for f in sorted(glob.glob(ED + "/svg/*.svg")):
    for n in texts(f):
        b = ib(n)
        if b and (b[0] < 28 or b[2] > 1922 or b[1] < 28 or b[3] > 2672):
            print(f"  {os.path.basename(f)} y={n['y']:.0f} box={tuple(round(v) for v in b)} :: {n['s'][:50]!r}")
            cross += 1
print("  frame crossings:", cross)

print("== 4. P6 chart-label baseline-anchored coverage (getmetrics ink_box) ==")
# Paint-order elements on P6: text ink vs rects drawn AFTER each text.
# Coverage = overlapped ink area / ink area for chart texts (y 1330-1800,
# x < 965); containers excluded; require <30%.
raw = open(f"{ED}/svg/p6-politique.svg", encoding="utf-8").read()
import re as _re
els = []
for m in _re.finditer(r'<(text|rect)\b([^>]*)>(.*?)</(?:text|rect)>|<(rect)\b([^>]*?)/>', raw, _re.S):
    pass
# simpler: ET in document order
root = ET.parse(f"{ED}/svg/p6-politique.svg").getroot()
order = []
for el in root.iter():
    if el.tag.endswith("text"):
        order.append(("text", el))
    elif el.tag.endswith("rect"):
        try: order.append(("rect", (float(el.get("x")), float(el.get("y")), float(el.get("width")), float(el.get("height")))))
        except (TypeError, ValueError): pass
worst = 0.0
for i, (kind, el) in enumerate(order):
    if kind != "text": continue
    y = float(el.get("y") or 0); x = float(el.get("x") or 0)
    if not (1330 <= y <= 1800 and x < 965): continue
    s = "".join(el.itertext())
    b = ink_box(s, el.get("font-family") or "", float(el.get("font-size") or 20),
                (el.get("font-weight") or "") in ("bold", "700"), x, y, el.get("text-anchor") or "start")
    if not b: continue
    area = max(0.0, (b[2] - b[0]) * (b[3] - b[1]))
    ov = 0.0
    for kind2, r in order[i + 1:]:
        if kind2 != "rect": continue
        rx, ry, rw, rh = r
        # container rects (chart box, page frames) excluded
        if rx <= b[0] and ry <= b[1] and rx + rw >= b[2] and ry + rh >= b[3]:
            continue
        ix = max(0.0, min(b[2], rx + rw) - max(b[0], rx))
        iy = max(0.0, min(b[3], ry + rh) - max(b[1], ry))
        ov += ix * iy
    frac = (ov / area * 100) if area else 0.0
    worst = max(worst, frac)
    print(f"  y={y:.0f} coverage={frac:.1f}% :: {s[:55]!r}")
print(f"  worst chart-label coverage: {worst:.1f}% (gate <30%)")
