# -*- coding: utf-8 -*-
"""Supplementary audit: box titles vs their own box borders.
For each text, find the nearest PRECEDING rect whose top edge is within 60px
above the text baseline and whose left edge is <= text ink left + 30 (i.e. the
box the text is a title/first line of); flag if the ink box spills past that
rect's right edge (or left edge). Usage: python audit_titles.py <svg_dir>"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import text_w

def attrs(s):
    return dict(re.findall(r'([\w-]+)="([^"]*)"', s))

def num(a, k, default=0.0):
    try:
        return float(a.get(k, default))
    except ValueError:
        return default

def unesc(s):
    return s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")

def audit(path):
    svg = open(path, encoding="utf-8").read()
    token_re = re.compile(r'<text\b[^>]*>.*?</text>|<(?:rect|image)\b[^>]*?/?>', re.S)
    rects = []   # (x0,y0,x1,y1)
    flags = []
    for m in token_re.finditer(svg):
        tok = m.group(0)
        if tok.startswith("<rect"):
            a = attrs(tok)
            if a.get("fill", "") == "none":
                continue
            x, y, w, h = num(a, "x"), num(a, "y"), num(a, "width"), num(a, "height")
            if w > 60 and h > 40:
                rects.append((x, y, x + w, y + h))
            continue
        if not tok.startswith("<text"):
            continue
        a = attrs(tok[:tok.index(">") + 1])
        s = unesc(tok[tok.index(">") + 1:-len("</text>")])
        if not s.strip():
            continue
        size = num(a, "font-size", 28)
        kind = "serif" if "Serif" in a.get("font-family", "") else "sans"
        bold = a.get("font-weight") == "700"
        w = text_w(s, kind, bold, size)
        x, y = num(a, "x"), num(a, "y")
        anchor = a.get("text-anchor", "start")
        if anchor == "end":
            x0, x1 = x - w, x
        elif anchor == "middle":
            x0, x1 = x - w / 2, x + w / 2
        else:
            x0, x1 = x, x + w
        # candidate box: rect painted before, top within [y-70, y], left edge <= x0+2,
        # and text vertically inside the rect
        for (rx0, ry0, rx1, ry1) in reversed(rects):
            if ry0 <= y <= ry1 and abs(rx0 - min(x0, x)) <= 30 and y - ry0 <= 75:
                if x1 > rx1 - 2 or x0 < rx0 - 2:
                    flags.append((s[:50], f"ink [{x0:.0f},{x1:.0f}] vs box [{rx0:.0f},{rx1:.0f}] top {ry0:.0f} base {y:.0f}"))
                break
    return flags

if __name__ == "__main__":
    total = 0
    for fn in sorted(os.listdir(sys.argv[1])):
        if fn.endswith(".svg"):
            fl = audit(os.path.join(sys.argv[1], fn))
            total += len(fl)
            print(f"== {fn}: {len(fl)} title flags")
            for s, why in fl:
                print(f"   [TITLE] {s!r} -- {why}")
    print(f"TOTAL TITLE FLAGS: {total}")
