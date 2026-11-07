# -*- coding: utf-8 -*-
"""Geometric occlusion audit (SOP gate) for ES x PT.
Paint-order scan of the final SVGs. Ink band = baseline -0.88em .. +0.30em,
widths from the production font metrics (svglib.text_w — same as the build).
Line boxes expanded by half stroke width (+0.1).
Checks:
 (a) COVER  later opaque shape covering >=30% of a text ink band
 (b) FOOTER text ink intruding into the footer band (bottom > 2580; footer texts excluded)
 (c) EDGE   text ink past a page edge (1950x2700)
 (d) LINEX  later thin line / thin rect crossing a text ink band
 (e) TTEXT  two text ink bands overlapping (area > 0)
 (f) XBORD  text ink crossing the border stroke zone of any rect (any paint order),
            excluding full-page background/frame rects
Usage: python audit_es_pt.py <svg_dir>
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

def parse(path):
    svg = open(path, encoding="utf-8").read()
    elems = []  # (kind, box, label, thin, base, size, rectinfo)
    token_re = re.compile(r'<text\b[^>]*>.*?</text>|<(?:rect|line|image|circle|path)\b[^>]*?/?>', re.S)
    for m in token_re.finditer(svg):
        tok = m.group(0)
        if tok.startswith("<text"):
            a = attrs(tok[:tok.index(">") + 1])
            s = unesc(tok[tok.index(">") + 1:-len("</text>")])
            box, size, base = text_box(a, s)
            elems.append(("text", box, f"text@{base:.0f} size {size:g}: {s[:44]!r}", False, base, size, None))
        else:
            tag = re.match(r'<(\w+)', tok).group(1)
            a = attrs(tok)
            if tag == "rect":
                x, y, w, h = num(a, "x"), num(a, "y"), num(a, "width"), num(a, "height")
                box = (x, y, x + w, y + h)
                thin = h <= 3 or w <= 3
                if a.get("fill", "") == "none" and not thin:
                    elems.append(("frame", box, f"rect {box}", thin, 0, 0, (box, num(a, "stroke-width", 1))))
                    continue
                elems.append(("shape", box, f"rect {box}", thin, 0, 0, (box, num(a, "stroke-width", 1))))
            elif tag == "image":
                x, y, w, h = num(a, "x"), num(a, "y"), num(a, "width"), num(a, "height")
                elems.append(("shape", (x, y, x + w, y + h), "image", False, 0, 0, None))
            elif tag == "circle":
                cx, cy, r = num(a, "cx"), num(a, "cy"), num(a, "r")
                if a.get("fill", "") == "none":
                    continue
                elems.append(("shape", (cx - r, cy - r, cx + r, cy + r), "circle", False, 0, 0, None))
            elif tag == "line":
                x1, y1, x2, y2 = num(a, "x1"), num(a, "y1"), num(a, "x2"), num(a, "y2")
                pad = num(a, "stroke-width", 1) / 2 + 0.1
                box = (min(x1, x2) - pad, min(y1, y2) - pad, max(x1, x2) + pad, max(y1, y2) + pad)
                elems.append(("shape", box, f"line y={y1:g}", True, 0, 0, None))
            elif tag == "path":
                if a.get("fill", "none") == "none":
                    continue
                bb = path_bbox(a.get("d", ""))
                if bb:
                    elems.append(("shape", bb, "path", False, 0, 0, None))
    return elems

def inter(b1, b2):
    ix0, iy0 = max(b1[0], b2[0]), max(b1[1], b2[1])
    ix1, iy1 = min(b1[2], b2[2]), min(b1[3], b2[3])
    if ix1 <= ix0 or iy1 <= iy0:
        return 0.0
    return (ix1 - ix0) * (iy1 - iy0)

def audit(path):
    elems = parse(path)
    flags = []
    texts = [(i, e) for i, e in enumerate(elems) if e[0] == "text"]
    rects = [e for e in elems if e[6] is not None]
    for i, e in texts:
        _k0, box, label, _t, base, size, _r0 = e
        x0, y0, x1, y1 = box
        area = max(1.0, (x1 - x0) * (y1 - y0))
        if y1 > FOOTER_RULE and base != 2624:
            flags.append(("FOOTER", label, f"ink bottom {y1:.1f} > {FOOTER_RULE}"))
        if x0 < 0 or x1 > PW or y0 < 0 or y1 > PH:
            flags.append(("EDGE", label, f"box {tuple(round(v,1) for v in box)}"))
        for kind2, box2, label2, thin, _b, _s, _r in elems[i + 1:]:
            if kind2 != "shape":
                continue
            ia = inter(box, box2)
            if ia <= 0:
                continue
            if thin:
                flags.append(("LINEX", label, f"crossed by later {label2}"))
            elif ia / area >= 0.30:
                flags.append(("COVER", label, f"{ia/area:.0%} covered by later {label2}"))
        # (f) text ink crossing a rect border stroke zone
        for _k, _b2, _l2, _th, _bb, _ss, (rb, sw) in [(e[0], e[1], e[2], e[3], e[4], e[5], e[6]) for e in rects]:
            rx0, ry0, rx1, ry1 = rb
            if rx1 - rx0 >= PW - 4 and ry1 - ry0 >= PH - 4:
                continue  # full-page background
            pad = sw / 2 + 0.6
            # border zones: top/bottom horizontal strips + left/right vertical strips
            zones = [(rx0, ry0 - pad, rx1, ry0 + pad), (rx0, ry1 - pad, rx1, ry1 + pad),
                     (rx0 - pad, ry0, rx0 + pad, ry1), (rx1 - pad, ry0, rx1 + pad, ry1)]
            for zi, z in enumerate(zones):
                if inter(box, z) > 0:
                    # text fully inside the rect is fine unless it crosses the zone band itself;
                    # crossing = ink on BOTH sides of the border centre line
                    if zi in (0, 1):
                        c = ry0 if zi == 0 else ry1
                        if y0 < c - 0.5 and y1 > c + 0.5:
                            flags.append(("XBORD", label, f"crosses horizontal border y={c:g} of rect {rb}"))
                    else:
                        c = rx0 if zi == 2 else rx1
                        if x0 < c - 0.5 and x1 > c + 0.5:
                            flags.append(("XBORD", label, f"crosses vertical border x={c:g} of rect {rb}"))
    # (e) text vs text
    tl = [e for _i, e in texts]
    for i in range(len(tl)):
        for j in range(i + 1, len(tl)):
            ia = inter(tl[i][1], tl[j][1])
            if ia > 0:
                a1 = max(1.0, (tl[i][1][2] - tl[i][1][0]) * (tl[i][1][3] - tl[i][1][1]))
                a2 = max(1.0, (tl[j][1][2] - tl[j][1][0]) * (tl[j][1][3] - tl[j][1][1]))
                flags.append(("TTEXT", f"{tl[i][2]}  <>  {tl[j][2]}", f"overlap {ia:.0f}px2 = {ia/min(a1,a2):.0%} of smaller"))
    return flags

if __name__ == "__main__":
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
