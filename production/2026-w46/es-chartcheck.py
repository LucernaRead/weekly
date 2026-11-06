# -*- coding: utf-8 -*-
"""Element check: text ink vs later-drawn filled rects (chart graze class, README #12)
+ same-baseline ink spacing on furniture bands (README #10). Uses build svglib fonts."""
import re, sys, os, glob
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-es-build")
import svglib
from PIL import ImageFont

def measure(t, kind, bold, size):
    f = svglib._font(kind, bold, int(round(size * 4)))
    bb = f.getbbox(t)
    return bb[0]/4.0, bb[2]/4.0, bb[1]/4.0, bb[3]/4.0, f.getlength(t)/4.0

SVGDIR = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-core/svg"
graze = 0
for path in sorted(glob.glob(os.path.join(SVGDIR, "*.svg"))):
    src = open(path, encoding="utf-8").read()
    # document-order elements: text and rect/line
    elems = []
    for m in re.finditer(r'<(text|rect|line)\b([^>]*)>([^<]*)</\1>|<(rect|line)\b([^>]*)/>', src):
        tag = m.group(1) or m.group(4)
        attrs = m.group(2) or m.group(5) or ""
        inner = m.group(3) or ""
        elems.append((tag, attrs, inner))
    texts = []
    for i, (tag, attrs, inner) in enumerate(elems):
        if tag == "text":
            xm = re.search(r'x="([\d.]+)"', attrs); ym = re.search(r'y="([\d.]+)"', attrs)
            fm = re.search(r'font-family="([^"]+)"', attrs); sm = re.search(r'font-size="([\d.]+)"', attrs)
            bold = 'font-weight="700"' in attrs
            anchor = re.search(r'text-anchor="(\w+)"', attrs)
            anchor = anchor.group(1) if anchor else "start"
            x, y, size = float(xm.group(1)), float(ym.group(1)), float(sm.group(1))
            kind = "serif" if "Serif" in fm.group(1) else "sans"
            l, r, t, b, adv = measure(inner, kind, bold, size)
            if anchor == "start": a, bb = x + l, x + r
            elif anchor == "end": a, bb = x - adv + l, x - adv + r
            else: a, bb = x - adv/2 + l, x - adv/2 + r
            texts.append((i, inner, a, y + t, bb, y + b))
    for (i, inner, a, top, bb, bot) in texts:
        for (tag, attrs, _) in elems[i+1:]:
            if tag != "rect": continue
            if 'fill="none"' in attrs: continue
            xm = re.search(r'x="([\d.]+)"', attrs); ym = re.search(r'y="([\d.]+)"', attrs)
            wm = re.search(r'width="([\d.]+)"', attrs); hm = re.search(r'height="([\d.]+)"', attrs)
            if not (xm and ym and wm and hm): continue
            rx, ry, rw, rh = float(xm.group(1)), float(ym.group(1)), float(wm.group(1)), float(hm.group(1))
            ox = min(bb, rx+rw) - max(a, rx); oy = min(bot, ry+rh) - max(top, ry)
            if ox > 0 and oy > 0:
                print(f"GRAZE {os.path.basename(path)} '{inner[:40]}' ink[{a:.1f},{top:.1f},{bb:.1f},{bot:.1f}] vs rect[{rx},{ry},{rx+rw},{ry+rh}] overlap {ox:.1f}x{oy:.1f}")
                graze += 1
print("graze total:", graze)
# same-baseline scan
bad = 0
for path in sorted(glob.glob(os.path.join(SVGDIR, "*.svg"))):
    src = open(path, encoding="utf-8").read()
    rows = {}
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"( font-weight="700")?[^>]*?(?: text-anchor="(start|middle|end)")?[^>]*>([^<]*)</text>', src):
        x, y, fam, size, bold, anchor, t = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), bool(m.group(5)), m.group(6) or "start", m.group(7)
        if not t.strip(): continue
        kind = "serif" if "Serif" in fam else "sans"
        l, r, tt, b, adv = measure(t, kind, bold, size)
        if anchor == "start": a, bb = x + l, x + r
        elif anchor == "end": a, bb = x - adv + l, x - adv + r
        else: a, bb = x - adv/2 + l, x - adv/2 + r
        rows.setdefault(y, []).append((a, bb, t))
    for y, spans in rows.items():
        spans.sort()
        for (a1, b1, t1), (a2, b2, t2) in zip(spans, spans[1:]):
            gap = a2 - b1
            if gap < 6:
                print(f"ROW {os.path.basename(path)} y={y} gap={gap:.1f} '{t1[:30]}' | '{t2[:30]}'")
                bad += 1
print("same-baseline reports:", bad)
