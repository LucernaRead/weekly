# -*- coding: utf-8 -*-
"""Geometric occlusion audit (SOP addendum + thin-line supplement) for NL x ES.
Paint-order scan of the shipped SVGs. Ink band = baseline -0.88em .. +0.30em,
widths from the production font metrics (svglib). Checks:
 (a) later opaque shape (rect/image/circle/path, fill not none) covering >=30% of a text ink band
 (b) text ink intruding into the footer band (ink bottom > 2580; the two footer texts excluded)
 (c) text ink past a page edge (1950x2700)
 (d) later-drawn thin line (line element or rect <=3px) crossing a text ink band
Usage: python audit_nl_es.py <svg_dir>
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import text_w

PW, PH, FOOTER_RULE = 1950, 2700, 2580
TAG_RE = re.compile(r'<(text|rect|line|image|circle|path)\b([^>]*?)(/?)>', re.S)
TEXT_RE = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)

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

def audit(path):
    svg = open(path, encoding="utf-8").read()
    # element stream in paint order; text elements consumed whole
    elems = []  # (kind, box, label, is_line)
    pos = 0
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
            if tag == "rect":
                x, y, w, h = num(a, "x"), num(a, "y"), num(a, "width"), num(a, "height")
                box = (x, y, x + w, y + h)
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
                # a <line> bbox is zero-height; expand by half the stroke width
                # (plus a hair) so a horizontal rule inside a text ink band
                # registers as an intersection (zero-height-box blind spot fix)
                pad = num(a, "stroke-width", 1) / 2 + 0.1
                box = (min(x1, x2) - pad, min(y1, y2) - pad,
                       max(x1, x2) + pad, max(y1, y2) + pad)
                elems.append(("shape", box, f"line y={y1:g}", True, 0, 0))
            elif tag == "path":
                if a.get("fill", "none") == "none":
                    continue
                bb = path_bbox(a.get("d", ""))
                if bb:
                    elems.append(("shape", bb, "path", False, 0, 0))
    flags = []
    texts = [(i, e) for i, e in enumerate(elems) if e[0] == "text"]
    for i, (_, box, label, _t, base, size) in texts:
        x0, y0, x1, y1 = box
        area = max(1.0, (x1 - x0) * (y1 - y0))
        # (b) footer band (footer texts themselves sit at baseline 2624 by design)
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
