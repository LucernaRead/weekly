# -*- coding: utf-8 -*-
"""P6 chart-label coverage, baseline-anchored ink method:
PIL font.getbbox(s, anchor='ls'/'rs') gives ink box relative to the
baseline origin (the bug in the first version was using plain getbbox,
which is ascender-relative and inflated coverage to 78%).
Labels: row labels (anchor start) + values (anchor end); rects = chart
bars drawn AFTER the label in the same chart box. Coverage <30% passes.
Usage: python chartcheck.py <p6.svg>
"""
import re, sys, os
from PIL import ImageFont
FONTS_DIR = "/usr/share/fonts/opentype/noto"
def sc_index(path):
    for i in range(12):
        try:
            f = ImageFont.truetype(path, 40, index=i)
            if f.getname()[0].endswith("SC"): return i
        except Exception: break
    return 0
SERIF = os.path.join(FONTS_DIR, "NotoSerifCJK-Regular.ttc"); SERIF_B = os.path.join(FONTS_DIR, "NotoSerifCJK-Bold.ttc")
SANS = os.path.join(FONTS_DIR, "NotoSansCJK-Regular.ttc"); SANS_B = os.path.join(FONTS_DIR, "NotoSansCJK-Bold.ttc")
IDX = {p: sc_index(p) for p in (SERIF, SERIF_B, SANS, SANS_B)}
def font(kind, bold, size):
    path = {"serif": SERIF_B if bold else SERIF, "sans": SANS_B if bold else SANS}[kind]
    return ImageFont.truetype(path, int(size), index=IDX[path])
def main():
    txt = open(sys.argv[1], encoding="utf-8").read()
    # ordered events with contents
    events = []
    for m in re.finditer(r'<(text|rect)\b([^>]*)>([^<]*)?</', txt):
        kind, attrs = m.group(1), m.group(2)
        if kind == "rect":
            xm = re.search(r'x="([^"]+)"', attrs); ym = re.search(r'y="([^"]+)"', attrs)
            wm = re.search(r'width="([^"]+)"', attrs); hm = re.search(r'height="([^"]+)"', attrs)
            fl = re.search(r'fill="([^"]+)"', attrs)
            if xm and ym and wm and hm:
                events.append(("rect", (float(xm.group(1)), float(ym.group(1)), float(wm.group(1)), float(hm.group(1)), fl.group(1) if fl else "")))
        else:
            xm = re.search(r'x="([^"]+)"', attrs); ym = re.search(r'y="([^"]+)"', attrs)
            fm = re.search(r'font-family="([^"]+)"', attrs); sm = re.search(r'font-size="([^"]+)"', attrs)
            bold = 'font-weight="700"' in attrs
            am = re.search(r'text-anchor="([^"]+)"', attrs)
            events.append(("text", (float(xm.group(1)), float(ym.group(1)), "serif" if "Serif" in fm.group(1) else "sans", float(sm.group(1)), bold, am.group(1) if am else "start", m.group(3) or "")))
    worst = 0.0
    for idx, (k, v) in enumerate(events):
        if k != "text": continue
        x, y, kind, size, bold, anchor, s = v
        if s not in ("Ik blijf thuis", "Ik kijk eerst naar de tekst", "Ik ga toch naar buiten", "Ik weet het niet", "45", "25", "20", "10"):
            continue
        f = font(kind, bold, size)
        anch = "ls" if anchor == "start" else ("rs" if anchor == "end" else "ms")
        l, t, r, b = f.getbbox(s, anchor=anch)
        inkbox = (x + l, y + t, x + r, y + b)
        area = max(0.0, (r - l) * (b - t))
        cov = 0.0
        for k2, rv in events[idx+1:]:
            if k2 != "rect": continue
            rx, ry, rw, rh, _fl = rv
            ix = max(0.0, min(inkbox[2], rx+rw) - max(inkbox[0], rx))
            iy = max(0.0, min(inkbox[3], ry+rh) - max(inkbox[1], ry))
            if area: cov = max(cov, ix*iy/area)
        print(f"label {s!r} ink={[round(v,1) for v in inkbox]} max-coverage={cov*100:.1f}%")
        worst = max(worst, cov)
    print(f"P6 chart-label worst coverage: {worst*100:.1f}% (pass <30%)")
main()
