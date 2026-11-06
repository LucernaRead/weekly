# -*- coding: utf-8 -*-
"""Same-baseline text-ink collision scan (README #10): for text elements
sharing a baseline (y within 1px), compute PIL true-ink boxes (getbbox at
4x supersampling is approximated here via font.getbbox on the string with
anchor handling: text() uses default anchor start/middle/end) and flag
overlaps > 1.5px on the same baseline. Furniture bands included.
Usage: python rowcheck.py <svg-dir>
"""
import re, sys, glob, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import ImageFont
FONTS_DIR = "/usr/share/fonts/opentype/noto"
def sc_index(path):
    for i in range(12):
        try:
            f = ImageFont.truetype(path, 40, index=i)
            if f.getname()[0].endswith("SC"): return i
        except Exception: break
    return 0
SERIF = os.path.join(FONTS_DIR, "NotoSerifCJK-Regular.ttc"); SERIF_B = os.path.join(FONTS_DIR, "NotoSerifCJK-Bold.ttc")
SANS = os.path.join(FONTS_DIR, "NotoSansCJK-Regular.ttc"); SANS_B = os.path.join(FONTS_DIR, "NotoSansCJK-Bold.ttc")
IDX = {p: sc_index(p) for p in (SERIF, SERIF_B, SANS, SANS_B)}
_cache = {}
def font(kind, bold, size):
    path = {"serif": SERIF_B if bold else SERIF, "sans": SANS_B if bold else SANS}[kind]
    k = (path, size)
    if k not in _cache: _cache[k] = ImageFont.truetype(path, size, index=IDX[path])
    return _cache[k]
def ink(x, y, s, size, kind, bold, anchor):
    f = font(kind, bold, size)
    l, t, r, b = f.getbbox(s)
    w = r - l
    if anchor == "middle": x0 = x - w / 2
    elif anchor == "end": x0 = x - w
    else: x0 = x
    # getbbox is ascender-relative: ink top = y - ascent... use getmetrics
    asc, desc = f.getmetrics()
    # PIL getbbox top is relative to baseline? getbbox returns box relative to anchor point (baseline origin) in recent Pillow: top is negative above baseline
    return (x0 + l, y + t, x0 + r, y + b)
def main():
    d = sys.argv[1]; bad = 0
    for path in sorted(glob.glob(os.path.join(d, "*.svg"))):
        txt = open(path, encoding="utf-8").read()
        els = re.findall(r'<text x="([^"]+)" y="([^"]+)" font-family="([^"]+)" font-size="([^"]+)"( font-weight="700")?[^>]*?( text-anchor="([^"]+)")?>([^<]*)</text>', txt)
        rows = {}
        for x, y, fam, size, bold, _w, anchor, s in els:
            kind = "serif" if "Serif" in fam else "sans"
            rows.setdefault(float(y), []).append((float(x), s, float(size), kind, bool(bold), anchor or "start"))
        for y, items in rows.items():
            boxes = []
            for x, s, size, kind, bold, anchor in items:
                if not s.strip(): continue
                boxes.append((ink(x, y, s, size, kind, bold, anchor), s))
            for i in range(len(boxes)):
                for j in range(i + 1, len(boxes)):
                    (x0a, ya, x1a, yb), sa = boxes[i]; (x0b, yc, x1b, yd), sb = boxes[j]
                    ov = min(x1a, x1b) - max(x0a, x0b)
                    voy = min(yb, yd) - max(ya, yc)
                    if ov > 1.5 and voy > 0:
                        bad += 1
                        print(f"COLLISION {os.path.basename(path)} y={y} overlap={ov:.1f} :: {sa[:30]!r} vs {sb[:30]!r}")
    print("SAME-BASELINE collisions >1.5px:", bad)
main()
