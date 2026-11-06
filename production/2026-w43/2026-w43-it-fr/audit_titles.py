# -*- coding: utf-8 -*-
"""Box-fit audit for ES x FR: any text whose ink starts inside an earlier-drawn
box rect (vertically within it) must not cross that rect's right border.
Catches the DE x FR P5 class: a box title striking past its own box border,
which coverage/line audits cannot see. Also reports title-zone margins.
Usage: python audit_titles.py <svg_dir>
"""
import re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import text_w

def attrs(s): return dict(re.findall(r'([\w-]+)="([^"]*)"', s))
def num(a, k, d=0.0):
    try: return float(a.get(k, d))
    except ValueError: return d
def unesc(s): return s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")

TOKEN = re.compile(r'<text\b[^>]*>.*?</text>|<(?:rect|line|image|circle|path)\b[^>]*?/?>', re.S)

def audit(path):
    svg = open(path, encoding="utf-8").read()
    rects = []   # (x0, y0, x1, y1)
    flags, titles = [], []
    for m in TOKEN.finditer(svg):
        tok = m.group(0)
        if tok.startswith("<rect"):
            a = attrs(tok)
            if a.get("fill", "") == "none":
                continue
            x, y, w, h = num(a, "x"), num(a, "y"), num(a, "width"), num(a, "height")
            rects.append((x, y, x + w, y + h))
            continue
        if not tok.startswith("<text"):
            continue
        a = attrs(tok[:tok.index(">") + 1])
        s = unesc(tok[tok.index(">") + 1:-len("</text>")])
        size = num(a, "font-size", 28)
        kind = "serif" if "Serif" in a.get("font-family", "") else "sans"
        bold = a.get("font-weight") == "700"
        w = text_w(s, kind, bold, size)
        sp = a.get("letter-spacing")
        if sp: w += float(sp) * max(0, len(s) - 1)
        x, y = num(a, "x"), num(a, "y")
        an = a.get("text-anchor", "start")
        if an == "end": x0, x1 = x - w, x
        elif an == "middle": x0, x1 = x - w / 2, x + w / 2
        else: x0, x1 = x, x + w
        # innermost earlier rect containing the text's start point and baseline
        cand = None
        for r in rects:
            if r[0] - 1 <= x0 and r[1] - 1 <= y - size * 0.5 and y <= r[3] + 1 and x0 < r[2]:
                if cand is None or (r[2] - r[0]) * (r[3] - r[1]) < (cand[2] - cand[0]) * (cand[3] - cand[1]):
                    cand = r
        if cand is None:
            continue
        if cand[2] - cand[0] >= 1900:  # page frame, not a box
            continue
        over = x1 - cand[2]
        if over > 0:
            flags.append((s, y, over, cand))
        elif y - cand[1] <= size * 2.2:  # title zone of the box
            titles.append((cand[2] - x1, s, y))
    return flags, titles

if __name__ == "__main__":
    d = sys.argv[1]
    worst = []
    total = 0
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".svg"): continue
        fl, ti = audit(os.path.join(d, fn))
        total += len(fl)
        print(f"== {fn}: {len(fl)} box-crossings")
        for s, y, over, r in fl:
            print(f"   CROSS by {over:.1f}px @y={y:.0f} rect={r}: {s[:60]!r}")
        for margin, s, y in sorted(ti)[:3]:
            worst.append((margin, fn, s))
    print("tightest title margins (ink to box border):")
    for margin, fn, s in sorted(worst)[:10]:
        print(f"   {margin:6.1f}px  {fn}  {s[:52]!r}")
    print("TOTAL BOX CROSSINGS:", total)
