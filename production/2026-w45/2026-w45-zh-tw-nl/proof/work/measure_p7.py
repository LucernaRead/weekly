# -*- coding: utf-8 -*-
"""Own direct measurement of the P7 letter box on the delivered SVG and the
P7 card crop geometry, using the audit tool's own ink parser. Read-only."""
import re, os, html, importlib.util
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
spec = importlib.util.spec_from_file_location("oa", os.path.join(BASE, "tools/occlusion_audit.py"))
oa = importlib.util.module_from_spec(spec); spec.loader.exec_module(oa)
TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)"([^>]*)>([^<]*)</text>')
RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"([^>]*)>')

def measure(path, label):
    s = open(path, encoding="utf-8").read()
    print(f"== {label} ==")
    rects = []
    for m in RECT_RE.finditer(s):
        x, y, w, h = map(float, m.groups()[:4])
        if abs(x - 1451) < 1:
            rects.append((x, y, w, h))
            print(f"  RECT x={x} y={y} w={w} h={h} bottom={y+h:.2f} expanded={y+h+0.7:.2f}")
    els = []
    for m in TEXT_RE.finditer(s):
        t = html.unescape(m.group(4))
        x, y, attrs = float(m.group(1)), float(m.group(2)), m.group(3)
        fm = re.search(r'font-family="([^"]+)"', attrs); sm = re.search(r'font-size="([\d.]+)"', attrs)
        bold = 'font-weight="700"' in attrs or 'font-weight="bold"' in attrs
        anchor = "middle" if 'text-anchor="middle"' in attrs else ("end" if 'text-anchor="end"' in attrs else "start")
        box = oa.ink_box(t, fm.group(1) if fm else "", float(sm.group(1)) if sm else 20.0, bold, x, y, anchor, 0.0)
        els.append((t, x, y, box))
    disc = [e for e in els if "Voorbeeldbrief" in e[0] or "Stuur je brief" in e[0] or "Deferral notice" in e[0] or "invitation stays open" in e[0]]
    for t, x, y, box in disc:
        print(f"  DISC node y={y} ink={[round(v,2) for v in box]} text={t[:110]!r}")
    last = disc[-1]
    # letter box = the col3 rect whose y range contains the disclosure start and whose bottom is just below
    # identify: rect with y=1155.86 per first proof / fixer
    lb = [r for r in rects if abs(r[1] - 1155.86) < 1]
    print(f"  letter-box candidates y~1155.86: {lb}")
    if lb:
        x, y, w, h = lb[0]
        print(f"  LAST line ink bottom={last[3][3]:.2f} ink center={(last[3][1]+last[3][3])/2:.2f}")
        print(f"  CLEARANCE raw={y+h-last[3][3]:.2f} vs expanded={y+h+0.7-last[3][3]:.2f}")
        print(f"  ink center inside expanded border by: {y+h+0.7-(last[3][1]+last[3][3])/2:.2f}")
    # phrases strip / teaser / footer geometry
    for t, x, y, box in els:
        if "Zinnen van de week" in t or "Volgende week" in t or "Pagina 7 van 8" in t:
            print(f"  GEO y={y} ink_bottom={box[3]:.2f} text={t[:80]!r}")
    # all rects in col3 region for gold-rule check: lines
    LINE_RE = re.compile(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"[^>]*>')
    for m in LINE_RE.finditer(s):
        x1, y1, x2, y2 = map(float, m.groups())
        if x1 >= 1400 and abs(y1 - y2) < 0.01:
            print(f"  LINE y={y1} x1={x1} x2={x2}")
    # P7 heads
    for t, x, y, box in els:
        if t.startswith(("A2 ·", "B1 ·", "B2 ·")) and y < 400:
            print(f"  HEAD ink right={box[2]:.1f} text={t[:60]!r}")
    return disc, rects, els

measure(os.path.join(BASE, "files/weekly-report-w45-zh-tw-nl/svg/p7-lang.svg"), "edition P7")
measure(os.path.join(BASE, "files/weekly-report-w45-zhtw-core/svg/p7-lang.svg"), "core P7")
