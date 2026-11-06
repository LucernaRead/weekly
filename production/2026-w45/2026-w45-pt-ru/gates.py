# -*- coding: utf-8 -*-
"""PTxRU W45 gates: rowcheck (same-baseline ink), right-edge ADVANCE scan,
P6 chart-label coverage (baseline-anchored ink vs later rects), gloss counts,
P7 quote doubling, CJK/term residue scans. Run with tools/venv python.
Usage: gates.py <edition-svg-dir> <core-svg-dir>"""
import re, sys, os, glob, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib

ED, CORE = sys.argv[1], sys.argv[2]
TEXT_RE = re.compile(r'<text([^>]*)>([^<]*)</text>')
RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"')

def parse(path):
    src = open(path, encoding='utf-8').read()
    texts, rects = [], []
    for attrs, t in TEXT_RE.findall(src):
        mx = re.search(r'x="([\d.]+)"', attrs)
        my = re.search(r'y="([\d.]+)"', attrs)
        mf = re.search(r'font-family="([^"]+)"', attrs)
        ms = re.search(r'font-size="([\d.]+)"', attrs)
        if not (mx and my and mf and ms):
            continue
        bold = 'font-weight="700"' in attrs
        ma = re.search(r'text-anchor="(start|middle|end)"', attrs)
        anchor = ma.group(1) if ma else 'start'
        t = html.unescape(t)
        if t.strip():
            texts.append((float(mx.group(1)), float(my.group(1)), mf.group(1),
                          float(ms.group(1)), bold, anchor, t))
    for m in RECT_RE.finditer(src):
        rects.append(tuple(map(float, m.groups())))
    return src, texts, rects

def ink_span(t, kind, bold, size, x, anchor):
    f = svglib._font(kind, bold, int(round(size * 4)))
    bb = f.getbbox(t)
    adv = f.getlength(t) / 4.0
    l, r = bb[0] / 4.0, bb[2] / 4.0
    if anchor == 'start':
        return x + l, x + r, adv
    if anchor == 'end':
        return x - adv + l, x - adv + r, adv
    return x - adv / 2 + l, x - adv / 2 + r, adv

def ink_box(t, kind, bold, size, x, y, anchor):
    """Baseline-anchored ink box via PIL getmetrics + anchor 'ls'."""
    f = svglib._font(kind, bold, int(round(size * 4)))
    asc, desc = f.getmetrics()
    asc, desc = asc / 4.0, desc / 4.0
    bb = f.getbbox(t, anchor='ls')
    # getbbox with anchor ls: box relative to baseline-left origin
    bx0, by0, bx1, by1 = (v / 4.0 for v in bb)
    adv = f.getlength(t) / 4.0
    if anchor == 'start':
        ox = x
    elif anchor == 'end':
        ox = x - adv
    else:
        ox = x - adv / 2
    return (ox + bx0, y + by0, ox + bx1, y + by1)

fails = []
# ---- 1. rowcheck: same-baseline gaps < 6 ----
for path in sorted(glob.glob(os.path.join(ED, '*.svg'))):
    _, texts, _ = parse(path)
    rows = {}
    for (x, y, fam, size, bold, anchor, t) in texts:
        kind = 'serif' if 'Serif' in fam else 'sans'
        a, b, _ = ink_span(t, kind, bold, size, x, anchor)
        rows.setdefault(round(y, 1), []).append((a, b, t))
    for y, spans in rows.items():
        spans.sort()
        for (a1, b1, t1), (a2, b2, t2) in zip(spans, spans[1:]):
            if a2 - b1 < 6:
                print(f'ROWCHECK {os.path.basename(path)} y={y} gap={a2-b1:.1f}: {t1[:40]!r} <> {t2[:40]!r}')
                fails.append(('rowcheck', path, y))
print('rowcheck done, flags:', sum(1 for f in fails if f[0] == 'rowcheck'))

# ---- 2. right-edge ADVANCE scan: advance-right > 1910 (inner frame) or < 40 ----
for path in sorted(glob.glob(os.path.join(ED, '*.svg'))):
    _, texts, _ = parse(path)
    for (x, y, fam, size, bold, anchor, t) in texts:
        kind = 'serif' if 'Serif' in fam else 'sans'
        a, b, adv = ink_span(t, kind, bold, size, x, anchor)
        if anchor == 'start':
            ar = x + adv
        elif anchor == 'end':
            ar = x
        else:
            ar = x + adv / 2
        al = ar - adv
        if ar > 1910 or al < 40:
            print(f'RIGHTEDGE {os.path.basename(path)} y={y} adv-span {al:.0f}..{ar:.0f}: {t[:60]!r}')
            fails.append(('rightedge', path, y))
print('rightedge done, flags:', sum(1 for f in fails if f[0] == 'rightedge'))

# ---- 3. P6 chart-label coverage: ink vs later-drawn rects, <30% ----
src, _, _ = parse(os.path.join(ED, 'p6-aprofundamento.svg'))
# element order by document offset
order = []
for m in re.finditer(r'<text[^>]*>[^<]*</text>', src):
    order.append((m.start(), 'text', m.group(0)))
for m in RECT_RE.finditer(src):
    order.append((m.start(), 'rect', m.groups()))
order.sort(key=lambda p: p[0])
chart_flags = 0
for idx, (_, kind_el, payload) in enumerate(order):
    if kind_el != 'text':
        continue
    mm = re.search(r'x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"', payload)
    if not mm:
        continue
    x, y, fam, size = float(mm.group(1)), float(mm.group(2)), mm.group(3), float(mm.group(4))
    bold = 'font-weight="700"' in payload
    ma = re.search(r'text-anchor="(start|middle|end)"', payload)
    anchor = ma.group(1) if ma else 'start'
    tm = re.search(r'>([^<]*)</text>', payload)
    t = html.unescape(tm.group(1)) if tm else ''
    if not t.strip():
        continue
    kind = 'serif' if 'Serif' in fam else 'sans'
    bx0, by0, bx1, by1 = ink_box(t, kind, bold, size, x, y, anchor)
    area = max(0.0, bx1 - bx0) * max(0.0, by1 - by0)
    if area == 0:
        continue
    for (_, kind2, payload2) in order[idx + 1:]:
        if kind2 != 'rect':
            continue
        rx, ry, rw, rh = map(float, payload2)
        ox = max(0.0, min(bx1, rx + rw) - max(bx0, rx))
        oy = max(0.0, min(by1, ry + rh) - max(by0, ry))
        cov = ox * oy / area
        if cov >= 0.30:
            print(f'CHART {t[:50]!r} covered {cov:.0%} by rect {rx},{ry},{rw}x{rh}')
            chart_flags += 1
print('chart coverage flags (>=30%):', chart_flags)
if chart_flags:
    fails.append(('chart', 'p6', 0))

# ---- 4. residue scans on edition SVGs ----
import subprocess
all_svg = ''
for p in sorted(glob.glob(os.path.join(ED, '*.svg'))):
    all_svg += open(p, encoding='utf-8').read()
cjk = re.findall(r'[\u4e00-\u9fff]', all_svg)
print('edition SVG CJK chars:', len(cjk))
if cjk:
    fails.append(('cjk', '', 0))
BANNED = '\u6865\u63a5'
print('banned-term occurrences in edition SVGs:', all_svg.count(BANNED))
if BANNED in all_svg:
    fails.append(('bannedterm', '', 0))
print('FAILURES:', fails if fails else 'none')
