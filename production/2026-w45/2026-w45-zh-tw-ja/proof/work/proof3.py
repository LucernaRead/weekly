# -*- coding: utf-8 -*-
"""P7 letter-box + teaser direct measurement (SVG ink + card pixels)."""
import os, re, sys
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
from occlusion_audit import parse_svg
from PIL import Image

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED_SVG = os.path.join(GOAL, "files/weekly-report-w45-zh-tw-ja/svg")
CORE_SVG = os.path.join(GOAL, "files/weekly-report-w45-zhtw-core/svg")

def measure(path, label):
    els, _, _ = parse_svg(open(path, encoding="utf-8").read())
    rects = [e for e in els if e.kind == "rect" and e.attrs.get("stroke") not in (None, "none")]
    texts = [e for e in els if e.kind == "text"]
    print(f"== {label} ==")
    # readers'-corner box: stroked rect with left edge ~1451 (col3) and top > 1000
    cands = [r for r in rects if abs(r.box[0] - 1451) < 5 and r.box[1] > 1000]
    for r in cands:
        print(f"  col3 stroked rect: box={tuple(round(x, 2) for x in r.box)} fill={r.attrs.get('fill')}")
    # the readers box is the lowest col3 stroked rect whose interior holds the disclosure
    # disclosure last line: node starting with '待ちしています' (ed) / 'press time' (core)
    for t in texts:
        if t.text.startswith("待ちしています") or t.text.startswith("press time"):
            print(f"  disclosure last-line node: {t.text[:50]!r} ink={tuple(round(x, 2) for x in t.box)} baseline={t.baseline}")
    # all text nodes with x-range inside col3 box (1451..1885) and y > 1000: max ink bottom
    # identify readers box as the col3 rect with largest top
    if cands:
        box = max(cands, key=lambda r: r.box[1])
        bx0, by0, bx1, by1 = box.box
        inside = [t for t in texts if t.box[0] >= bx0 - 1 and t.box[2] <= bx1 + 1 and t.box[1] >= by0 and t.box[3] <= by1 + 60]
        inside_sorted = sorted(inside, key=lambda t: t.box[3])
        print(f"  readers box: top={by0:.2f} bottom={by1:.2f} height={by1-by0:.2f}")
        for t in inside_sorted[-4:]:
            print(f"    inside last: {t.text[:50]!r} ink_bottom={t.box[3]:.2f}")
        if inside_sorted:
            last = inside_sorted[-1]
            print(f"  CLEARANCE: box_bottom - last_ink_bottom = {by1 - last.box[3]:.2f}px; inside={last.box[3] <= by1}")
    # teaser: rect with height ~118 near bottom, fill dark (not 'none')
    teas = [r for r in els if r.kind == "rect" and abs((r.box[3] - r.box[1]) - 118) < 2 and r.box[1] > 2000]
    for r in teas:
        print(f"  teaser rect: box={tuple(round(x, 2) for x in r.box)} fill={r.attrs.get('fill')}")
        tx0, ty0, tx1, ty1 = r.box
        inside = [t for t in texts if t.box[0] >= tx0 and t.box[2] <= tx1 and t.box[1] >= ty0 and t.box[3] <= ty1 + 5]
        for t in sorted(inside, key=lambda t: t.box[3])[-3:]:
            print(f"    teaser inside last: {t.text[:50]!r} ink_bottom={t.box[3]:.2f}")
        if inside:
            print(f"  TEASER: rect_bottom={ty1:.2f} clear_of_2580={2580 - ty1:.2f}px; last_ink={max(t.box[3] for t in inside):.2f}")

measure(os.path.join(ED_SVG, "p7-lang.svg"), "EDITION P7")
measure(os.path.join(CORE_SVG, "p7-lang.svg"), "CORE P7 (context)")

print("== CARD PIXEL MEASUREMENT, edition P7 ==")
im = Image.open(os.path.join(GOAL, "files/weekly-report-w45-zh-tw-ja/cards/p7-lang.png")).convert("L")
W, H = im.size
print(f"  card size: {W}x{H}")
px = im.load()
def dark(x, y):
    return px[x, y] < 100
# readers box x-range 1451..1885; scan rows for dark-pixel counts in that range
# find border rows: rows with >80% dark across box width
bx0, bx1 = 1451, 1885
for y in range(0, H):
    cnt = sum(1 for x in range(bx0, bx1 + 1) if dark(x, y))
    if cnt > 350:  # >80% of 435
        pass
# collect candidate border rows in col3 region y 1000..1800
borders = []
for y in range(1000, 1850):
    cnt = sum(1 for x in range(bx0, bx1 + 1) if dark(x, y))
    if cnt > 350:
        borders.append((y, cnt))
# group consecutive rows
groups = []
for y, c in borders:
    if groups and y - groups[-1][-1][0] <= 2:
        groups[-1].append((y, c))
    else:
        groups.append([(y, c)])
print(f"  border-row groups in col3 (y 1000..1850): {[(g[0][0], g[-1][0]) for g in groups]}")
if len(groups) >= 2:
    box_top = groups[0][0][0]
    # readers box is the LAST box group pair in this range; find last two groups
    box_bottom = groups[-1][-1][0]
    print(f"  last box bottom border row: {box_bottom}")
    # last ink row strictly inside box (between top border and bottom border), excluding border rows
    top = groups[-2][0][0] if len(groups) >= 2 else None
    # determine readers box: it is the box whose bottom is groups[-1]; its top is the group just above it
    # scan text ink rows inside: rows with >=3 dark pixels in box x-range, not border rows
    border_rows = set(y for g in groups for y, _ in g)
    last_ink = None
    for y in range(groups[-2][0][0] + 1, groups[-1][0][0]):
        cnt = sum(1 for x in range(bx0, bx1 + 1) if dark(x, y))
        if cnt >= 3:
            last_ink = y
    print(f"  readers box top border: {groups[-2][0][0]}, bottom border: {groups[-1][0][0]}, last text ink row: {last_ink}, clearance: {groups[-1][0][0] - last_ink if last_ink else None}px")
# teaser card check: dark rect near bottom spanning x 65..1885; find its bottom row
for y in range(2700 - 1, 2300, -1):
    cnt = sum(1 for x in range(65, 1886) if dark(x, y))
    if cnt > 1500:
        print(f"  teaser dark-rect bottom row (card): {y} (dark count {cnt})")
        break
