# -*- coding: utf-8 -*-
"""Geometric occlusion audit (SOP addendum + thin-line supplement) for zh-TW x FR.
Paint-order scan of the final SVGs. Ink band = baseline -0.88em .. +0.30em,
widths from the production font metrics (svglib). Checks:
 (a) later opaque shape covering >=30% of a text ink band (COVER)
 (b) text ink intruding into the footer band (ink bottom > 2580) (FOOTER)
 (c) text ink past a page edge (EDGE)
 (d) any later-drawn line (line element or thin rect, box EXPANDED by half the
     stroke width) crossing a text ink band (LINEX)
 (e) text ink band crossing the border of an earlier filled rect (STRADDLE)
Run with --selftest first: synthetic positive controls must all fire.
Usage: python audit_zh_tw_fr.py [--selftest] <svg_dir>
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
    elems = []
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
            sw = num(a, "stroke-width", 1.0)
            if tag == "rect":
                x, y, w, h = num(a, "x"), num(a, "y"), num(a, "width"), num(a, "height")
                thin = h <= 3.4 or w <= 3.4
                if thin:  # a rule: expand by half stroke width
                    e = sw / 2
                    box = (x - e, y - e, x + w + e, y + h + e)
                else:
                    box = (x, y, x + w, y + h)
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
                e = sw / 2  # CRITICAL: expand the zero-height box by half the stroke width
                box = (min(x1, x2) - e, min(y1, y2) - e, max(x1, x2) + e, max(y1, y2) + e)
                elems.append(("shape", box, f"line y={y1:g} sw={sw:g}", True, 0, 0))
            elif tag == "path":
                if a.get("fill", "none") == "none":
                    continue
                bb = path_bbox(a.get("d", ""))
                if bb:
                    elems.append(("shape", bb, "path", False, 0, 0))
    return elems

def audit(svg):
    elems = parse(svg)
    flags = []
    texts = [(i, e) for i, e in enumerate(elems) if e[0] == "text"]
    for i, (_, box, label, _t, base, size) in texts:
        x0, y0, x1, y1 = box
        area = max(1.0, (x1 - x0) * (y1 - y0))
        if y1 > FOOTER_RULE and base != 2624:
            flags.append(("FOOTER", label, f"ink bottom {y1:.1f} > {FOOTER_RULE}"))
        if x0 < 0 or x1 > PW or y0 < 0 or y1 > PH:
            flags.append(("EDGE", label, f"box {box}"))
        for kind2, box2, label2, thin, _b, _s in elems[:i]:
            if kind2 != "shape" or thin:
                continue
            bx0, by0, bx1, by1 = box2
            if (bx1 - bx0) >= PW - 1 and (by1 - by0) >= PH - 1:
                continue
            ox = min(x1, bx1) - max(x0, bx0)
            oy = min(y1, by1) - max(y0, by0)
            if ox <= 0 or oy <= 0:
                continue
            crosses_h = (y0 < by0 < y1) or (y0 < by1 < y1)
            crosses_v = (x0 < bx0 < x1) or (x0 < bx1 < x1)
            if (crosses_h and ox > 0.3 * (x1 - x0)) or (crosses_v and oy > 0.3 * (y1 - y0)):
                if not (bx0 <= x0 and x1 <= bx1 and by0 <= y0 and y1 <= by1):
                    flags.append(("STRADDLE", label, f"crosses {label2}"))
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

def selftest():
    hdr = '<svg xmlns="http://www.w3.org/2000/svg" width="1950" height="2700">'
    t = '<text x="100" y="500" font-family="Noto Sans CJK" font-size="25" fill="#222">HELLO WORLD TEST</text>'
    cases = {
        "COVER": hdr + t + '<rect x="90" y="470" width="500" height="60" fill="#000"/></svg>',
        "LINEX": hdr + t + '<line x1="50" y1="495" x2="900" y2="495" stroke="#a00" stroke-width="2"/></svg>',
        "FOOTER": hdr + '<text x="100" y="2620" font-family="Noto Sans CJK" font-size="25" fill="#222">LOW TEXT</text></svg>',
        "STRADDLE": hdr + '<rect x="90" y="440" width="300" height="90" fill="#eee" stroke="#999"/>'
                    '<text x="80" y="500" font-family="Noto Sans CJK" font-size="25" font-weight="700" fill="#222">TITLE SPILLS OUT</text></svg>',
        "EDGE": hdr + '<text x="1900" y="500" font-family="Noto Sans CJK" font-size="25" fill="#222">EDGE TEXT HERE NOW</text></svg>',
    }
    ok = True
    for want, svg in cases.items():
        kinds = {k for k, _, _ in audit(svg)}
        hit = want in kinds
        ok &= hit
        print(f"selftest {want}: {'FIRED' if hit else 'MISSED'} (all flags: {sorted(kinds)})")
    print("SELFTEST", "PASS" if ok else "FAIL")
    return ok

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--selftest" in sys.argv and not selftest():
        sys.exit(2)
    d = args[0]
    total = 0
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".svg"):
            continue
        fl = audit(open(os.path.join(d, fn), encoding="utf-8").read())
        total += len(fl)
        print(f"== {fn}: {len(fl)} flags")
        for kind, label, why in fl:
            print(f"   [{kind}] {label} -- {why}")
    print(f"TOTAL FLAGS: {total}")
