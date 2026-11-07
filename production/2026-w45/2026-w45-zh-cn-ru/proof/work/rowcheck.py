# -*- coding: utf-8 -*-
"""Same-baseline ink-collision scan (the class the canonical occlusion
audit does not cover: two text runs on ONE baseline colliding).
Parses shipped SVGs, measures true ink with PIL/FreeType (SC face 2),
groups text nodes by baseline y, and flags pairs whose ink intervals
overlap (gap < 0) or touch (gap < 2). Run over the edition dir."""
import glob, html, os, re, sys
from PIL import ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
ED = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-ru/svg"
FONTS = {
    ("sans", False): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 2),
    ("sans", True): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 2),
    ("serif", False): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc", 2),
    ("serif", True): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc", 2),
    ("blackletter", False): ("/home/hatch/.local/share/fonts/UnifrakturMaguntia.ttf", 0),
}
_cache = {}

def font(fam, bold, size):
    key = (fam, bold, size)
    if key not in _cache:
        path, idx = FONTS.get((fam, bold), FONTS[("sans", False)])
        try:
            _cache[key] = ImageFont.truetype(path, size, index=idx)
        except Exception:
            _cache[key] = ImageFont.truetype(path, size)
    return _cache[key]

def fam_of(attrs):
    ff = attrs.get("font-family", "")
    if "Unifraktur" in ff:
        return "blackletter"
    if "Serif" in ff:
        return "serif"
    return "sans"

TEXT_RE = re.compile(r'<text([^>]*)>(.*?)</text>', re.S)
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')

flags = 0
for path in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    s = open(path, encoding="utf-8").read()
    nodes = []
    for m in TEXT_RE.finditer(s):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        if "x" not in attrs or "y" not in attrs:
            continue
        txt = html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        if not txt.strip():
            continue
        try:
            x, y = float(attrs["x"]), float(attrs["y"])
            size = float(attrs.get("font-size", "20"))
        except ValueError:
            continue
        bold = attrs.get("font-weight", "") in ("700", "bold")
        anchor = attrs.get("text-anchor", "start")
        f = font(fam_of(attrs), bold, int(round(size)))
        try:
            l, t, r, b = f.getbbox(txt)
            adv = f.getlength(txt)
        except Exception:
            continue
        if anchor == "middle":
            x0, x1 = x - adv / 2 + l, x - adv / 2 + r
        elif anchor == "end":
            x0, x1 = x - adv + l, x - adv + r
        else:
            x0, x1 = x + l, x + r
        nodes.append((y, x0, x1, txt))
    # group by baseline (tolerance 1.0)
    groups = {}
    for y, x0, x1, txt in nodes:
        for gy in list(groups):
            if abs(gy - y) <= 1.0:
                groups[gy].append((x0, x1, txt))
                break
        else:
            groups[y] = [(x0, x1, txt)]
    pg = os.path.basename(path)
    for gy, items in sorted(groups.items()):
        if len(items) < 2:
            continue
        items.sort()
        for (a0, a1, at), (b0, b1, bt) in zip(items, items[1:]):
            gap = b0 - a1
            if gap < 2:
                flags += 1
                print(f"FLAG {pg} y={gy:.1f} gap={gap:.1f} :: {at[:50]!r} VS {bt[:50]!r}")
print(f"rowcheck: {flags} same-baseline flags")
sys.exit(1 if flags else 0)
