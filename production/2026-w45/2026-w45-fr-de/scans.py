# -*- coding: utf-8 -*-
"""Supplementary scans for FR x DE (venv PIL, read-only over shipped SVGs).
1. ADVANCE right-edge: every text node, advance width (svglib text_w,
   same Noto CJK SC faces as the builder) vs page right edge 1885.
   Anchor handling: start -> [x, x+w]; middle -> [x-w/2, x+w/2];
   end -> [x-w, x].
2. Frame-line scan: text ink (advance box, conservative) vs the two
   page frame rects (28/28/1894/2644 sw 3.4; 40/40/1870/2620 sw 1.2).
3. Same-baseline rowcheck (FR x RU lesson): on furniture bands
   (P1 top y=92, P1 band rows, every page footer y=2624, P1 badge
   y=574), group nodes by baseline y and flag horizontal overlaps.
4. P6 chart-label baseline-anchored coverage (getmetrics, NOT getbbox):
   for P6 chart-area texts, ink box = baseline - ascent .. baseline +
   descent (PIL font.getmetrics at node size/face), vs any rect drawn
   AFTER the text in paint order; report max coverage %.
5. Line-start kinsoku: text nodes starting with closer punctuation
   ) ] } . , ; : ! ? % " ' (French dialogue em-dash lines and «
   openers are legitimate and excluded; P8 key lines start with
   digits by construction).
"""
import os, re, sys, glob
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import text_w, _font

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-de/svg")
NS = "{http://www.w3.org/2000/svg}"


def kind_of(el):
    fam = el.get("font-family") or ""
    bold = el.get("font-weight") == "700"
    kind = "serif" if "Serif" in fam else "sans"
    return kind, bold


def intervals(path):
    """Return list of (baseline_y, x0, x1, size, text, kind, bold, anchor)."""
    out = []
    for el in ET.parse(path).getroot().iter():
        if not el.tag.endswith("text"):
            continue
        t = (el.text or "")
        if not t.strip():
            continue
        size = float(el.get("font-size") or 20)
        kind, bold = kind_of(el)
        w = text_w(t, kind, bold, size)
        x = float(el.get("x") or 0)
        anch = el.get("text-anchor") or "start"
        if anch == "middle":
            x0, x1 = x - w / 2, x + w / 2
        elif anch == "end":
            x0, x1 = x - w, x
        else:
            x0, x1 = x, x + w
        out.append((float(el.get("y") or 0), x0, x1, size, t.strip(), kind, bold, anch))
    return out


print("== 1. right-edge (limit 1885) ==")
worst = 0
for p in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    for y, x0, x1, size, t, k, b, a in intervals(p):
        if x1 > 1885:
            print("  OVER:", os.path.basename(p), f"y={y} x1={x1:.1f}", repr(t[:60]))
        worst = max(worst, x1)
print("  max x1 over all pages:", round(worst, 1))

print("== 2. frame-line scan (frames at x=28/40, right 1922/1910, y=28/40, bottom 2672/2660) ==")
for p in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    for y, x0, x1, size, t, k, b, a in intervals(p):
        # ink vertical band approx baseline-size .. baseline+0.3*size
        top, bot = y - size, y + size * 0.3
        hits = []
        if x0 < 42 and (28 - 2 <= top <= 2672 or 28 - 2 <= bot <= 2672):
            pass  # left frames are at x<=42; text starts at >=65, no hit possible
        if x1 > 1908 and (top <= 2672 and bot >= 28):
            hits.append("right-frame")
        if hits:
            print("  HIT:", os.path.basename(p), hits, repr(t[:60]))
print("  frame scan done (no output above = no hits)")

print("== 3. same-baseline rowcheck (bands y=92, 574, 2624 + band rows) ==")
for p in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    iv = intervals(p)
    for band_y in (92, 574, 2624):
        row = sorted([(x0, x1, t) for y, x0, x1, s, t, k, b, a in iv if abs(y - band_y) < 1.5])
        for (x0a, x1a, ta), (x0b, x1b, tb) in zip(row, row[1:]):
            if x0b < x1a - 1:
                print(f"  OVERLAP {os.path.basename(p)} y={band_y}: {ta[:40]!r} vs {tb[:40]!r} gap={x0b-x1a:.1f}")
print("  rowcheck done")

print("== 4. P6 chart-label baseline-anchored coverage (getmetrics) ==")
p6 = os.path.join(ED, "p6-politique.svg")
root = ET.parse(p6).getroot()
elems = list(root.iter())
maxcov = 0.0
worst_desc = ""
for i, el in enumerate(elems):
    if not el.tag.endswith("text"):
        continue
    t = (el.text or "")
    if not t.strip():
        continue
    y = float(el.get("y") or 0)
    if not (1330 <= y <= 1800):
        continue  # chart box region only
    size = float(el.get("font-size") or 20)
    kind, bold = kind_of(el)
    f = _font(kind, bold, int(size))
    asc, desc = f.getmetrics()
    x = float(el.get("x") or 0)
    w = text_w(t, kind, bold, size)
    anch = el.get("text-anchor") or "start"
    x0 = x if anch == "start" else (x - w / 2 if anch == "middle" else x - w)
    box = (x0, y - asc, x0 + w, y + desc)
    for el2 in elems[i + 1:]:
        if not el2.tag.endswith("rect"):
            continue
        rx, ry = float(el2.get("x") or 0), float(el2.get("y") or 0)
        rw, rh = float(el2.get("width") or 0), float(el2.get("height") or 0)
        if rw <= 0 or rh <= 0:
            continue
        ox = max(0, min(box[2], rx + rw) - max(box[0], rx))
        oy = max(0, min(box[3], ry + rh) - max(box[1], ry))
        area = (box[2] - box[0]) * (box[3] - box[1])
        cov = ox * oy / area if area else 0
        if cov > maxcov:
            maxcov, worst_desc = cov, f"{t[:40]!r} by rect ({rx},{ry},{rw}x{rh})"
print(f"  max chart-label coverage: {maxcov*100:.1f}% ({worst_desc})  gate <30%")

print("== 5. line-start kinsoku ==")
closers = set(")]}.,;:!?%\"'")
for p in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    for y, x0, x1, size, t, k, b, a in intervals(p):
        if t and t[0] in closers:
            print(f"  START {os.path.basename(p)} y={y}: {t[:70]!r}")
print("  kinsoku scan done")
