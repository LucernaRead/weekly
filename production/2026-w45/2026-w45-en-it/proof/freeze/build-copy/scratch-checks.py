# -*- coding: utf-8 -*-
"""Supplementary geometric scans for W45 EN x IT (round 3), beyond the
canonical occlusion_audit.py (which already reads 0/0/0):
1. right-edge scan, ADVANCE method (PIL getlength, not ink): every text
   node's advance-right vs the 1885 content edge.
2. frame-line pressure scan: any rect border drawn AFTER a text node
   whose stroke line intersects that text's ink box (anchor 'ls' ink).
3. P6 chart-label coverage, baseline-anchored ink (PIL textbbox anchor
   'ls'): overlap of each chart label's ink with any later-drawn rect,
   gate < 30%.
4. same-baseline furniture spacing: P1 top band (y=92), P1 dark band
   (y=478/522), every page footer (y=2624): pairwise ink gaps.
Run with tools/venv/bin/python. Fonts: Noto CJK SC face (index 2),
UnifrakturMaguntia for the masthead.
"""
import re, sys, os
from PIL import ImageFont, ImageDraw, Image

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
SB = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
SR = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SERB = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
SERR = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
BL = os.path.expanduser("~/.local/share/fonts/UnifrakturMaguntia.ttf")
DRAW = ImageDraw.Draw(Image.new("RGB", (10, 10)))


def font_for(family, size, weight):
    if "Unifraktur" in family or size >= 100:
        return ImageFont.truetype(BL, int(round(size)))
    bold = str(weight) == "700"
    if "Sans" in family:
        return ImageFont.truetype(SB if bold else SR, int(round(size)), index=2)
    return ImageFont.truetype(SERB if bold else SERR, int(round(size)), index=2)


def parse(svg_path):
    s = open(svg_path, encoding="utf-8").read()
    elems = []
    for m in re.finditer(r"<(rect|text)\b([^>]*?)(/>|>([^<]*)</text>)", s):
        tag, attrs, _, inner = m.group(1), m.group(2), m.group(3), m.group(4)

        def get(a):
            mm = re.search(a + r'="([^"]+)"', attrs)
            return mm.group(1) if mm else ""

        if tag == "rect":
            try:
                elems.append(("rect", float(get("x") or 0), float(get("y") or 0),
                              float(get("width") or 0), float(get("height") or 0),
                              float(get("stroke-width") or 0), get("fill")))
            except ValueError:
                pass
        else:
            elems.append(("text", float(get("x") or 0), float(get("y") or 0),
                          get("font-family"), float(get("font-size") or 0),
                          get("font-weight"), get("text-anchor") or "start",
                          (inner or "").replace("&amp;", "&")))
    return elems


def ink_box(t):
    _, x, y, fam, size, wt, anchor, txt = t
    f = font_for(fam, size, wt)
    a = {"start": "ls", "middle": "ms", "end": "rs"}[anchor]
    return DRAW.textbbox((x, y), txt, font=f, anchor=a)


def adv_right(t):
    _, x, y, fam, size, wt, anchor, txt = t
    f = font_for(fam, size, wt)
    adv = f.getlength(txt)
    if anchor == "start":
        return x + adv
    if anchor == "end":
        return x
    return x + adv / 2


def overlap_area(a, b):
    x0, y0 = max(a[0], b[0]), max(a[1], b[1])
    x1, y1 = min(a[2], b[2]), min(a[3], b[3])
    return max(0, x1 - x0) * max(0, y1 - y0)


def area(b):
    return max(0, b[2] - b[0]) * max(0, b[3] - b[1])


def seg_hits_box(x0, y0, x1, y1, b, tol):
    # axis-aligned segment vs box, expanded by tol
    if y0 == y1:
        return b[1] - tol <= y0 <= b[3] + tol and not (x1 < b[0] - tol or x0 > b[2] + tol)
    return b[0] - tol <= x0 <= b[2] + tol and not (y1 < b[1] - tol or y0 > b[3] + tol)


def run(edition_dir):
    print("### 1. right-edge ADVANCE scan (flag: advance-right > 1886)")
    worst = []
    for name in sorted(os.listdir(edition_dir)):
        if not name.endswith(".svg"):
            continue
        for t in parse(os.path.join(edition_dir, name)):
            if t[0] != "text":
                continue
            r = adv_right(t)
            worst.append((r, name, t[7][:60]))
    worst.sort(reverse=True)
    for r, name, txt in worst[:6]:
        print(f"  max {name}: advance-right {r:.1f} {txt!r}")
    print("  flags:", sum(1 for r, _, _ in worst if r > 1886))

    print("### 2. frame-line pressure scan (later rect border x earlier text ink)")
    n = 0
    for name in sorted(os.listdir(edition_dir)):
        if not name.endswith(".svg"):
            continue
        elems = parse(os.path.join(edition_dir, name))
        texts = []
        for e in elems:
            if e[0] == "text":
                texts.append((ink_box(e), e[7][:50]))
            else:
                _, x, y, w, h, sw, _fill = e
                tol = sw / 2.0
                borders = [(x, y, x + w, y), (x, y + h, x + w, y + h),
                           (x, y, x, y + h), (x + w, y, x + w, y + h)]
                for box, txt in texts:
                    for (x0, y0, x1, y1) in borders:
                        if seg_hits_box(x0, y0, x1, y1, box, tol):
                            print(f"  {name}: border {x0},{y0}-{x1},{y1} hits {txt!r} box {box}")
                            n += 1
                            break
    print("  pressure flags:", n)

    print("### 3. P6 chart-label coverage (anchor 'ls' ink vs later rects, gate <30%)")
    p6 = parse(os.path.join(edition_dir, "p6-politique.svg"))
    labels = [e for e in p6 if e[0] == "text" and re.match(r"^(No lines|Work on Tuesday|Travel plans|Habit) :", e[7])]
    print("  labels found:", len(labels))
    for lab in labels:
        box = ink_box(lab)
        idx = p6.index(lab)
        worst_cov = 0.0
        for e in p6[idx + 1:]:
            if e[0] == "rect":
                _, x, y, w, h, _sw, _f = e
                cov = overlap_area(box, (x, y, x + w, y + h)) / max(1, area(box))
                worst_cov = max(worst_cov, cov)
        print(f"  {lab[7]!r} ink {tuple(round(v, 1) for v in box)} max coverage {worst_cov:.1%} {'PASS' if worst_cov < 0.30 else 'FAIL'}")

    print("### 4. same-baseline furniture spacing (gap < 0 = overlap)")
    for name in sorted(os.listdir(edition_dir)):
        if not name.endswith(".svg"):
            continue
        elems = [e for e in parse(os.path.join(edition_dir, name)) if e[0] == "text"]
        for y in (92, 478, 522, 2624):
            row = [e for e in elems if abs(e[2] - y) < 1.0]
            if len(row) < 2:
                continue
            boxes = sorted((ink_box(e), e[7][:40]) for e in row)
            gaps = [round(boxes[i + 1][0][0] - boxes[i][0][2], 1) for i in range(len(boxes) - 1)]
            flag = "OVERLAP" if min(gaps) < 0 else "ok"
            print(f"  {name} y={y}: gaps {gaps} {flag}")


if __name__ == "__main__":
    run(os.path.join(BASE, sys.argv[1] if len(sys.argv) > 1 else "weekly-report-w45-en-it", "svg"))
