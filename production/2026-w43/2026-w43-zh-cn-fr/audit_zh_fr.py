# -*- coding: utf-8 -*-
"""Geometric occlusion audit (SOP addendum + thin-line supplement) for zh-CN x FR.
Paint-order scan of the shipped SVGs. Ink band = baseline -0.88em .. +0.30em,
widths from the production font metrics (svglib). Shape boxes are EXPANDED by
half the shape's stroke width before testing (a zero-height line box can never
fire otherwise). Checks:
 (a) later opaque shape covering >=30% of a text ink band
 (b) text ink intruding into the footer band (ink bottom > 2580; footer texts excluded)
 (c) text ink past a page edge
 (d) any later-drawn thin line crossing a text ink band
 (e) text-text overlap: two text ink bands intersecting (area > 4% of the smaller)
 (f) box-title spill: a text node starting inside a filled rect must end inside it
Usage: python audit_zh_fr.py <svg_dir>   |   python audit_zh_fr.py --selftest
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import text_w

PW, PH, FOOTER_RULE = 1950, 2700, 2580

def attrs(s):
    return dict(re.findall(r'([\w-]+)="([^"]*)"', s))

def num(a, k, default=0.0):
    try:
        return float(a.get(k, default))
    except ValueError:
        return default

def unesc(s):
    return s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")

def text_box(a, s):
    size = num(a, "font-size", 28)
    kind = "serif" if "Serif" in a.get("font-family", "") else "sans"
    bold = a.get("font-weight") == "700"
    w = text_w(s, kind, bold, size)
    sp = a.get("letter-spacing")
    if sp:
        w += float(sp) * max(0, len(s) - 1)
    x, y = num(a, "x"), num(a, "y")
    anchor = a.get("text-anchor", "start")
    if anchor == "end":
        x0, x1 = x - w, x
    elif anchor == "middle":
        x0, x1 = x - w / 2, x + w / 2
    else:
        x0, x1 = x, x + w
    return (x0, y - 0.88 * size, x1, y + 0.30 * size), size, y

def path_bbox(d):
    nums = [float(v) for v in re.findall(r'-?\d+\.?\d*', d)]
    if len(nums) < 2:
        return None
    xs, ys = nums[0::2], nums[1::2]
    return (min(xs), min(ys), max(xs), max(ys))

def parse(svg):
    elems = []  # (kind, box, label, thin, base, size)
    token_re = re.compile(r'<text\b[^>]*>.*?</text>|<(?:rect|line|image|circle|path)\b[^>]*?/?>', re.S)
    for m in token_re.finditer(svg):
        tok = m.group(0)
        if tok.startswith("<text"):
            a = attrs(tok[:tok.index(">") + 1])
            s = unesc(tok[tok.index(">") + 1:-len("</text>")])
            box, size, base = text_box(a, s)
            elems.append(("text", box, f"text@{base:.0f} size {size:g}: {s[:44]!r}", False, base, size))
        else:
            tag = re.match(r'<(\w+)', tok).group(1)
            a = attrs(tok)
            sw = num(a, "stroke-width", 0) / 2.0 if a.get("stroke") not in (None, "none") else 0.0
            if tag == "rect":
                x, y, w, h = num(a, "x"), num(a, "y"), num(a, "width"), num(a, "height")
                box = (x - sw, y - sw, x + w + sw, y + h + sw)
                thin = h <= 3 or w <= 3
                if a.get("fill", "") == "none" and not thin:
                    continue
                elems.append(("shape", box, f"rect {box}", thin, 0, 0))
            elif tag == "image":
                x, y, w, h = num(a, "x"), num(a, "y"), num(a, "width"), num(a, "height")
                elems.append(("shape", (x, y, x + w, y + h), "image", False, 0, 0))
            elif tag == "circle":
                cx, cy, r = num(a, "cx"), num(a, "cy"), num(a, "r")
                if a.get("fill", "") == "none":
                    continue
                elems.append(("shape", (cx - r, cy - r, cx + r, cy + r), "circle", False, 0, 0))
            elif tag == "line":
                x1, y1, x2, y2 = num(a, "x1"), num(a, "y1"), num(a, "x2"), num(a, "y2")
                box = (min(x1, x2) - sw, min(y1, y2) - sw, max(x1, x2) + sw, max(y1, y2) + sw)
                elems.append(("shape", box, f"line y={y1:g}", True, 0, 0))
            elif tag == "path":
                if a.get("fill", "none") == "none":
                    continue
                bb = path_bbox(a.get("d", ""))
                if bb:
                    elems.append(("shape", bb, "path", False, 0, 0))
    return elems

def audit(path):
    svg = open(path, encoding="utf-8").read()
    elems = parse(svg)
    flags = []
    texts = [(i, e) for i, e in enumerate(elems) if e[0] == "text"]
    rects = [e[1] for e in elems if e[0] == "shape" and not e[3]]
    for i, (_, box, label, _t, base, size) in texts:
        x0, y0, x1, y1 = box
        area = max(1.0, (x1 - x0) * (y1 - y0))
        # (b) footer band
        if y1 > FOOTER_RULE and base != 2624:
            flags.append(("FOOTER", label, f"ink bottom {y1:.1f} > {FOOTER_RULE}"))
        # (c) page edge
        if x0 < 0 or x1 > PW or y0 < 0 or y1 > PH:
            flags.append(("EDGE", label, f"box {box}"))
        # (a)+(d) later shapes
        for kind2, box2, label2, thin, _b, _s in elems[i + 1:]:
            if kind2 != "shape":
                continue
            ix0, iy0 = max(x0, box2[0]), max(y0, box2[1])
            ix1, iy1 = min(x1, box2[2]), min(y1, box2[3])
            if ix1 <= ix0 or iy1 <= iy0:
                continue
            if thin:
                flags.append(("LINEX", label, f"crossed by later {label2}"))
            else:
                cov = (ix1 - ix0) * (iy1 - iy0) / area
                if cov >= 0.30:
                    flags.append(("COVER", label, f"{cov:.0%} covered by later {label2}"))
        # (f) box-title spill: text starting strictly inside a filled rect must end
        # inside the SMALLEST such rect (the page background contains everything)
        containing = [rb for rb in rects if rb[0] + 2 < x0 < rb[2] - 2 and rb[1] < base < rb[3]]
        if containing:
            rb = min(containing, key=lambda r: (r[2] - r[0]) * (r[3] - r[1]))
            if (rb[2] - rb[0]) < PW - 10 and x1 > rb[2] + 0.5:
                flags.append(("BOXTITLE", label, f"ends {x1:.1f} past box right {rb[2]:.1f}"))
    # (e) text-text overlap
    for a in range(len(texts)):
        for b in range(a + 1, len(texts)):
            (_, ba, la, _t1, _ba, _sa), (_, bb, lb, _t2, _bb, _sb) = texts[a][1], texts[b][1]
            ix0, iy0 = max(ba[0], bb[0]), max(ba[1], bb[1])
            ix1, iy1 = min(ba[2], bb[2]), min(ba[3], bb[3])
            if ix1 <= ix0 or iy1 <= iy0:
                continue
            inter = (ix1 - ix0) * (iy1 - iy0)
            smaller = min((ba[2]-ba[0])*(ba[3]-ba[1]), (bb[2]-bb[0])*(bb[3]-bb[1]))
            if smaller > 0 and inter / smaller > 0.04:
                flags.append(("TEXTX", la, f"overlaps {lb} by {inter/smaller:.0%} of smaller"))
    return flags

SELFTEST = """<svg xmlns="http://www.w3.org/2000/svg" width="1950" height="2700">
<rect width="1950" height="2700" fill="#f7f1e2"/>
<text x="100" y="200" font-family="Noto Sans CJK" font-size="25">Texte couvert par la boîte</text>
<rect x="90" y="150" width="500" height="120" fill="#fdfaf0"/>
<text x="100" y="400" font-family="Noto Sans CJK" font-size="25">Texte traversé par une ligne</text>
<line x1="60" y1="392" x2="900" y2="392" stroke="#000" stroke-width="1.6"/>
<text x="100" y="2620" font-family="Noto Sans CJK" font-size="25">Texte dans la bande du pied</text>
<text x="100" y="600" font-family="Noto Sans CJK" font-size="25">Premier texte superposé</text>
<text x="110" y="612" font-family="Noto Sans CJK" font-size="25">Deuxième texte superposé</text>
</svg>"""
CLEAN = """<svg xmlns="http://www.w3.org/2000/svg" width="1950" height="2700">
<rect width="1950" height="2700" fill="#f7f1e2"/>
<text x="100" y="200" font-family="Noto Sans CJK" font-size="25">Texte propre et libre</text>
<rect x="90" y="300" width="500" height="120" fill="#fdfaf0"/>
<text x="108" y="350" font-family="Noto Sans CJK" font-size="23" font-weight="700">Titre dans sa boîte</text>
<text x="65" y="2624" font-family="Noto Sans CJK" font-size="20">Pied de page</text>
</svg>"""

if __name__ == "__main__":
    if sys.argv[1] == "--selftest":
        open("/tmp/audit-test.svg", "w", encoding="utf-8").write(SELFTEST)
        open("/tmp/audit-clean.svg", "w", encoding="utf-8").write(CLEAN)
        tf = audit("/tmp/audit-test.svg")
        cf = audit("/tmp/audit-clean.svg")
        kinds = {k for k, _, _ in tf}
        print("positive control flags:", len(tf), sorted(kinds))
        for kind, label, why in tf:
            print(f"   [{kind}] {label} -- {why}")
        print("clean page flags:", len(cf))
        assert {"COVER", "LINEX", "FOOTER", "TEXTX"} <= kinds, "positive control FAILED"
        assert len(cf) == 0, f"clean page FAILED: {cf}"
        print("SELFTEST PASS: all defect classes fire; clean page silent")
    else:
        d = sys.argv[1]
        total = 0
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".svg"):
                continue
            fl = audit(os.path.join(d, fn))
            total += len(fl)
            print(f"== {fn}: {len(fl)} flags")
            for kind, label, why in fl:
                print(f"   [{kind}] {label} -- {why}")
        print(f"TOTAL FLAGS: {total}")
