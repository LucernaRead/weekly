# -*- coding: utf-8 -*-
"""Same-baseline ink-collision scan + P6 chart-label element check.
Approximation (stated in report): PIL ink boxes from the tables.json
font files at SC face index 2; text-anchor middle/start honoured.
This supplements, not replaces, tools/occlusion_audit.py."""
import re, glob, os
from xml.etree import ElementTree as ET
from PIL import ImageFont

B = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = f"{B}/files/weekly-report-w45-zh-cn-pt/svg"
FONTS = {
    ("Noto Sans CJK SC", "700"): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 2),
    ("Noto Sans CJK SC", None): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 2),
    ("Noto Serif CJK SC", "700"): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc", 2),
    ("Noto Serif CJK SC", None): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc", 2),
    ("UnifrakturMaguntia", None): ("/home/hatch/.local/share/fonts/UnifrakturMaguntia.ttf", 0),
}
_cache = {}
def font(fam, wt, size):
    key = (fam, wt, size)
    if key in _cache: return _cache[key]
    path, idx = FONTS.get((fam, wt), FONTS.get((fam, None), ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 2)))
    try: f = ImageFont.truetype(path, int(round(size)), index=idx)
    except TypeError: f = ImageFont.truetype(path, int(round(size)))
    _cache[key] = f; return f

NS = "{http://www.w3.org/2000/svg}"
total_coll = 0
for path in sorted(glob.glob(ED + "/*.svg")):
    tree = ET.parse(path); root = tree.getroot()
    # document order elements
    elems = list(root.iter())
    texts = []  # (idx, x0, x1, y, txt)
    rects = []  # (idx, x, y, w, h)
    for i, el in enumerate(elems):
        tag = el.tag.replace(NS, "")
        if tag == "rect":
            try: rects.append((i, float(el.get("x", 0)), float(el.get("y", 0)), float(el.get("width", 0)), float(el.get("height", 0))))
            except (TypeError, ValueError): pass
        elif tag == "text":
            try:
                x = float(el.get("x")); y = float(el.get("y")); size = float(el.get("font-size"))
            except (TypeError, ValueError): continue
            txt = "".join(el.itertext())
            if not txt.strip(): continue
            f = font(el.get("font-family"), el.get("font-weight"), size)
            length = f.getlength(txt)
            anchor = el.get("text-anchor")
            x0 = x - length / 2 if anchor == "middle" else (x - length if anchor == "end" else x)
            texts.append((i, x0, x0 + length, y, txt))
    # same-baseline: group by exact y
    by_y = {}
    for t in texts: by_y.setdefault(t[3], []).append(t)
    coll = []
    for y, group in by_y.items():
        group = sorted(group, key=lambda t: t[1])
        for a, b in zip(group, group[1:]):
            overlap = a[2] - b[1]
            if overlap > 0.5: coll.append((y, a[4][:40], b[4][:40], round(overlap, 2)))
    print(os.path.basename(path), "same-baseline collisions:", len(coll))
    for c in coll: print("   ", c)
    total_coll += len(coll)
    if "p6-shendu" in path:
        # chart-label check: text ink vs later rects
        hits = []
        for (ti, x0, x1, y, txt) in texts:
            # ink vertical band approx baseline-0.88em..+0.30em, em=size from font
            for (ri, rx, ry, rw, rh) in rects:
                if ri <= ti: continue
                if x0 < rx + rw and x1 > rx and (y - 30) < ry + rh and (y + 10) > ry:
                    # only flag if rect is a bar/background (not tiny badge): report all, adjudicate by print
                    hits.append((txt[:40], round(x0, 1), round(y, 1), (rx, ry, rw, rh)))
        print("   P6 text-vs-later-rect overlaps (raw, incl. badges):", len(hits))
        for h in hits: print("     ", h)
print("TOTAL same-baseline collisions:", total_coll)
