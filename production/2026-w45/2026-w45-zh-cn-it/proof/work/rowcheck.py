# -*- coding: utf-8 -*-
"""Same-baseline ink-collision scan (canonical audit's TEXTX covers only
DIFFERENT lines) + P6 chart-label element check (text ink vs later rects).
Uses PIL with the real TTC faces (SC index 2), 4x supersampling like the audit.
Flags: same-y text pairs whose ink intervals overlap; earlier-drawn text ink
intersected by a later-drawn rect on P6."""
import re, sys, html, glob, os
from PIL import ImageFont
FD = "/usr/share/fonts/opentype/noto"
def font(fam, size, bold):
    base = "NotoSansCJK" if "Sans" in fam else "NotoSerifCJK"
    path = os.path.join(FD, f"{base}-{'Bold' if bold else 'Regular'}.ttc")
    return ImageFont.truetype(path, int(round(size * 4)), index=2)
def ink_interval(x, y, size, fam, bold, anchor, s):
    f = font(fam, size, bold)
    # getbbox at 4x, then scale down; bbox is (l, t, r, b) relative to anchor point origin
    bb = f.getbbox(s)
    l, r = bb[0] / 4.0, bb[2] / 4.0
    adv = f.getlength(s) / 4.0
    if anchor == "middle":
        x0 = x - adv / 2.0
    elif anchor == "end":
        x0 = x - adv
    else:
        x0 = x
    return (x0 + l, x0 + r, y)  # ink x-interval + baseline y
TEXTRE = re.compile(r'<text x="([0-9.]+)" y="([0-9.]+)" font-family="([^"]+)" font-size="([0-9.]+)"(?: font-weight="([0-9]+)")?[^>]*?(?: text-anchor="([^"]+)")?>(.*?)</text>')
RECTRE = re.compile(r'<rect x="([0-9.]+)" y="([0-9.]+)" width="([0-9.]+)" height="([0-9.]+)"')
flags = []
for path in sorted(glob.glob("../files/weekly-report-w45-zh-cn-it/svg/*.svg")):
    page = os.path.basename(path)
    raw = open(path, encoding="utf-8").read()
    # walk elements in document order
    events = []
    for m in re.finditer(r'<(text|rect)[^>]*?(?:/>|>(.*?)</text>)', raw):
        if m.group(1) == "text":
            tm = TEXTRE.match(m.group(0))
            if not tm: continue
            x, y, fam, size = float(tm.group(1)), float(tm.group(2)), tm.group(3), float(tm.group(4))
            bold = tm.group(5) == "700"
            anchor = tm.group(6) or "start"
            s = html.unescape(tm.group(7))
            if not s.strip(): continue
            try: iv = ink_interval(x, y, size, fam, bold, anchor, s)
            except Exception as e: print("  measure fail", page, s[:30], e); continue
            events.append(("text", iv, s))
        else:
            rm = RECTRE.match(m.group(0))
            if not rm: continue
            rx, ry, rw, rh = (float(v) for v in rm.groups())
            events.append(("rect", (rx, ry, rx + rw, ry + rh), None))
    # same-baseline pairs
    by_y = {}
    for kind, iv, s in events:
        if kind == "text":
            by_y.setdefault(round(iv[2], 1), []).append((iv, s))
    for y, items in by_y.items():
        items.sort()
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                (a0, a1, _), sa = items[i]
                (b0, b1, _), sb = items[j]
                if b0 < a1 - 0.5:  # overlap beyond 0.5px tolerance
                    flags.append(f"{page} y={y} OVERLAP {a1-b0:.1f}px :: {sa[:60]!r} VS {sb[:60]!r}")
    # P6 chart: earlier text ink vs later rect
    if "p6-" in page:
        texts_so_far = []
        for kind, iv, s in events:
            if kind == "text":
                # ink vertical band: baseline -0.88em .. +0.30em approx via size
                texts_so_far.append((iv, s))
            else:
                rx0, ry0, rx1, ry1 = iv
                for (tx0, tx1, ty), s in texts_so_far:
                    # text vertical extent unknown here; use baseline proximity: rect y-range vs baseline
                    if ry0 - 40 <= ty <= ry1 + 10 and tx1 > rx0 and tx0 < rx1:
                        flags.append(f"{page} CHART-GRAZE rect x[{rx0},{rx1}] y[{ry0},{ry1}] vs earlier text {s[:60]!r} ink x[{tx0:.1f},{tx1:.1f}] baseline {ty}")
print(f"same-baseline + chart flags: {len(flags)}")
for f in flags: print(" ", f)
