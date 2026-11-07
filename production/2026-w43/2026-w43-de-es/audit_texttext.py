# -*- coding: utf-8 -*-
"""Supplementary text-text overlap scan for DE x FR (companion to audit_de_fr.py).
Uses the same ink-band model (baseline -0.88em .. +0.30em, production text_w).
Known model artifacts to crop-adjudicate: display-size masthead wordmark
(248pt band overestimates ink) and full-width headline lines whose text_w
width overestimates the true ink end next to a right-anchored gloss.
Usage: python audit_texttext.py <svg_dir>
"""
import re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import text_w

def attrs(s): return dict(re.findall(r'([\w-]+)="([^"]*)"', s))
def num(a, k, d=0.0):
    try: return float(a.get(k, d))
    except ValueError: return d
def unesc(s): return s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")

d = sys.argv[1]
total = 0
for fn in sorted(os.listdir(d)):
    if not fn.endswith('.svg'): continue
    svg = open(os.path.join(d, fn), encoding='utf-8').read()
    boxes = []
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', svg, re.S):
        a = attrs(m.group(1)); s = unesc(m.group(2))
        size = num(a, 'font-size', 28)
        kind = 'serif' if 'Serif' in a.get('font-family', '') else 'sans'
        bold = a.get('font-weight') == '700'
        w = text_w(s, kind, bold, size)
        sp = a.get('letter-spacing')
        if sp: w += float(sp) * max(0, len(s) - 1)
        x, y = num(a, 'x'), num(a, 'y')
        an = a.get('text-anchor', 'start')
        if an == 'end': x0, x1 = x - w, x
        elif an == 'middle': x0, x1 = x - w/2, x + w/2
        else: x0, x1 = x, x + w
        boxes.append((x0, y - 0.88*size, x1, y + 0.30*size, s[:34], y))
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            a, b = boxes[i], boxes[j]
            ix = min(a[2], b[2]) - max(a[0], b[0])
            iy = min(a[3], b[3]) - max(a[1], b[1])
            if ix > 2 and iy > 2:
                print(f'  [{fn}] overlap {ix:.0f}x{iy:.0f}: {a[4]!r} @{a[5]:.0f} vs {b[4]!r} @{b[5]:.0f}')
                total += 1
print('TOTAL text-text overlaps:', total)
