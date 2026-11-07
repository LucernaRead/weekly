# -*- coding: utf-8 -*-
"""Supplementary checks for the zh-cn x es edition (not replacements for tools):
1. same-baseline text-ink collision scan (all pages, all text nodes)
2. P6 chart-label element check (bar rects vs row/value labels)
3. gloss item counts: split each gloss() source string on the char itself
Usage: python checks.py <edition_dir> <core_build_dir> <my_build_dir>
"""
import sys, os, re, glob, html
from xml.etree import ElementTree as ET
from PIL import ImageFont

ED, CORE_BUILD, MY_BUILD = sys.argv[1], sys.argv[2], sys.argv[3]
FD = "/usr/share/fonts/opentype/noto"
FONTS = {}
def font(kind, bold, size):
    key = (kind, bold, size)
    if key not in FONTS:
        name = ("NotoSerifCJK-" if kind == "serif" else "NotoSansCJK-") + ("Bold" if bold else "Regular") + ".ttc"
        FONTS[key] = ImageFont.truetype(os.path.join(FD, name), size, index=2)
    return FONTS[key]

def ink_box(el):
    s = html.unescape("".join(el.itertext()))
    size = float(el.get("font-size"))
    fam = el.get("font-family", "")
    kind = "serif" if "Serif" in fam else "sans"
    bold = el.get("font-weight") == "700"
    f = font(kind, bold, int(round(size)))
    # PIL getbbox at anchor "la" equivalent: measure raw box, then shift by anchor
    x = float(el.get("x")); y = float(el.get("y"))
    anchor = el.get("text-anchor", "start")
    # getbbox returns (left, top, right, bottom) relative to anchor point at (0,0) with ascender up
    bb = f.getbbox(s)
    w = bb[2] - bb[0]
    if anchor == "middle":
        x0 = x - w / 2 - bb[0]
    elif anchor == "end":
        x0 = x - w - bb[0]
    else:
        x0 = x - bb[0]
    return (x0, x0 + w, s, float(el.get("y")))

print("== 1. same-baseline ink collisions ==")
total_flags = 0
for path in sorted(glob.glob(os.path.join(ED, "svg", "*.svg"))):
    t = ET.parse(path)
    by_y = {}
    for el in t.iter():
        if el.tag.endswith("text"):
            x0, x1, s, y = ink_box(el)
            by_y.setdefault(round(y, 1), []).append((x0, x1, s))
    for y, items in sorted(by_y.items()):
        items.sort()
        for (a0, a1, sa), (b0, b1, sb) in zip(items, items[1:]):
            gap = b0 - a1
            if gap < 2:
                total_flags += 1
                print(f"  {os.path.basename(path)} y={y} gap={gap:.1f}: {sa[:50]!r} || {sb[:50]!r}")
print(f"  same-baseline flags: {total_flags}")

print("== 2. P6 chart-label check ==")
t = ET.parse(os.path.join(ED, "svg", "p6-shendu.svg"))
rects = []
texts = []
for el in t.iter():
    if el.tag.endswith("rect"):
        try:
            rects.append((float(el.get("x")), float(el.get("y")), float(el.get("width")), float(el.get("height")), el.get("fill")))
        except TypeError:
            pass
    if el.tag.endswith("text"):
        texts.append(el)
# chart bars: y around 1276..1450, x=325, fills OLIVE #3e4c2a / GOLD #b3a06a
bars = sorted([r for r in rects if r[0] == 325.0 and r[2] > 100], key=lambda r: r[1])
print(f"  bars: {[(r[2], r[1]) for r in bars]} (expect widths 810/537/480)")
for el in texts:
    s = "".join(el.itertext())
    if s.strip().endswith("元") and float(el.get("y")) > 1200 and float(el.get("y")) < 1500:
        x = float(el.get("x"))
        # find bar on a nearby row (value baseline ~ bar y+34)
        print(f"  value label {s!r} at x={x}")
    if s.startswith(("A:", "B:", "C:")) and float(el.get("y")) > 1200 and float(el.get("y")) < 1500:
        x0, x1, _, _ = ink_box(el)
        print(f"  row label {s!r} ink ends x={x1:.0f} (bar starts 325)")

print("== 3. gloss item counts (split gloss() string on the char) ==")
def gloss_counts(build):
    out = {}
    for f in ["content12.py", "content34.py", "content56.py"]:
        txt = open(os.path.join(build, f), encoding="utf-8").read()
        # gloss calls: .gloss("...") possibly spanning lines? In this build they are single-line.
        for m in re.finditer(r"\.gloss\(\"([^\"]*)\"\)", txt):
            s = m.group(1)
            out.setdefault(f, []).append(len(s.split("·")))
    return out
core_g = gloss_counts(CORE_BUILD)
my_g = gloss_counts(MY_BUILD)
print("  core :", core_g, "total", sum(sum(v) for v in core_g.values()))
print("  ed   :", my_g, "total", sum(sum(v) for v in my_g.values()))
assert core_g == my_g, "GLOSS COUNT MISMATCH"
print("  gloss counts EQUAL item by item")
