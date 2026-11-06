# Same-baseline ink-collision scan (README note #10 class: the canonical
# occlusion audit's TEXTX only compares DIFFERENT lines). For every SVG in
# the edition dir: group text nodes by baseline y; within a group, compute
# true ink x-intervals with PIL + the shipped fonts (same resolution as
# tools/occlusion_audit.py: split TTCs, SC face index 2) and flag any pair
# whose ink intervals overlap. Furniture bands (P1 top strip) included.
# Usage: python rowcheck.py <edition-svg-dir>
import re, sys, os, glob, json
from PIL import ImageFont

TABLES = json.load(open(os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/tools/tables.json"),
    encoding="utf-8"))
FONTS = TABLES["fonts"]
FACE_INDEX = FONTS["face_index"]
_cache = {}

def resolve_font(family, size, bold):
    suffix = "SC"
    if family.endswith("SC"):
        suffix = "SC"
    if "Serif" in family:
        path = FONTS["serif_bold"] if bold else FONTS["serif_regular"]
    elif "Unifraktur" in family:
        return (FONTS["blackletter"], 0)
    else:
        path = FONTS["sans_bold"] if bold else FONTS["sans_regular"]
    return (path, FACE_INDEX.get(suffix, FACE_INDEX["SC"]))

def font_for(family, size, bold):
    path, index = resolve_font(family, size, bold)
    key = (path, index, int(size))
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, int(size), index=index)
    return _cache[key]

def ink_interval(x, size, bold, family, anchor, text):
    f = font_for(family, size, bold)
    bbox = f.getbbox(text)
    if bbox is None:
        return None
    adv = f.getlength(text)
    if anchor == "middle":
        x0 = x - adv / 2
    elif anchor == "end":
        x0 = x - adv
    else:
        x0 = x
    return (x0 + bbox[0], x0 + bbox[2])

def main(d):
    flags = 0
    for path in sorted(glob.glob(os.path.join(d, "*.svg"))):
        t = open(path, encoding="utf-8").read()
        nodes = []
        for m in re.finditer(
                r'<text x="([0-9.]+)" y="([0-9.]+)" font-family="([^"]+)" '
                r'font-size="([0-9.]+)"( font-weight="700")?[^>]*'
                r'text-anchor="([^"]+)"[^>]*>(.*?)</text>', t):
            x, y, fam, size, bold, anchor, txt = m.groups()
            txt = txt.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
            try:
                iv = ink_interval(float(x), float(size), bool(bold), fam, anchor, txt)
            except Exception as e:
                print(f"SKIP {os.path.basename(path)} y={y}: {e}")
                continue
            if iv:
                nodes.append((float(y), iv, txt))
        by_y = {}
        for y, iv, txt in nodes:
            by_y.setdefault(y, []).append((iv, txt))
        for y, items in sorted(by_y.items()):
            items.sort(key=lambda z: z[0][0])
            for (iv1, t1), (iv2, t2) in zip(items, items[1:]):
                if iv2[0] < iv1[1]:
                    print(f"FLAG {os.path.basename(path)} y={y}: overlap "
                          f"{iv1[1]-iv2[0]:.1f}px between {t1[:40]!r} and {t2[:40]!r}")
                    flags += 1
    print("same-baseline flags:", flags)
    sys.exit(1 if flags else 0)

if __name__ == "__main__":
    main(sys.argv[1])
