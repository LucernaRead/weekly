# -*- coding: utf-8 -*-
"""Supplemental geometry scans for the W45 EN x ES edition:
1. rowcheck: same-baseline text ink spans, gap < 6 flagged (FR x RU method).
2. chartcheck: P6 chart-label coverage by later opaque rects, baseline-
   anchored boxes (PIL getmetrics, anchor 'ls': top = baseline - ascent,
   bottom = baseline + descent, width = advance). Gate: coverage < 30%.
   True-ink coverage (getbbox) reported alongside.
3. edgescan: right-edge scan by ADVANCE width (flag advance-right > 1885)
   + text-ink vs page-frame bands (outer 28/3.4, inner 40/1.2).
"""
import re, sys, glob, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib

ED = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/en-es-proof/reg-ed/svg")

TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
ANCHOR_RE = re.compile(r'text-anchor="(start|middle|end)"')
RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]+)"')

def font(kind, bold, size):
    return svglib._font(kind, bold, int(round(size * 4)))

def ink_span(t, kind, bold, size, x, anchor):
    f = font(kind, bold, size)
    bb = f.getbbox(t)
    adv = f.getlength(t) / 4.0
    l, r = bb[0] / 4.0, bb[2] / 4.0
    if anchor == "start":
        return x + l, x + r, adv
    if anchor == "end":
        return x - adv + l, x - adv + r, adv
    return x - adv / 2 + l, x - adv / 2 + r, adv

def parse(path):
    src = open(path, encoding="utf-8").read()
    elems = []
    for m in re.finditer(r'<(text|rect)[^>]*?(?:>([^<]*)</text>|/>)', src):
        pass
    texts, rects = [], []
    for m in TEXT_RE.finditer(src):
        x, y, fam, size, attrs, t = (float(m.group(1)), float(m.group(2)), m.group(3),
                                     float(m.group(4)), m.group(5), m.group(6))
        am = ANCHOR_RE.search(attrs)
        anchor = am.group(1) if am else "start"
        bold = "font-weight=\"700\"" in attrs
        t = html.unescape(t)
        if t.strip():
            texts.append({"x": x, "y": y, "fam": fam, "size": size, "bold": bold,
                          "anchor": anchor, "t": t, "pos": m.start()})
    for m in RECT_RE.finditer(src):
        rects.append({"x": float(m.group(1)), "y": float(m.group(2)), "w": float(m.group(3)),
                      "h": float(m.group(4)), "fill": m.group(5), "pos": m.start()})
    return texts, rects

def kind_of(fam):
    return "serif" if "Serif" in fam else "sans"

def rowcheck():
    bad = 0
    print("== rowcheck (same-baseline gaps < 6) ==")
    for path in sorted(glob.glob(os.path.join(ED, "*.svg"))):
        texts, _ = parse(path)
        rows = {}
        for e in texts:
            a, b, _ = ink_span(e["t"], kind_of(e["fam"]), e["bold"], e["size"], e["x"], e["anchor"])
            rows.setdefault(round(e["y"], 1), []).append((a, b, e["t"]))
        for y, spans in rows.items():
            spans.sort()
            for (a1, b1, t1), (a2, b2, t2) in zip(spans, spans[1:]):
                if a2 - b1 < 6:
                    print(f"{os.path.basename(path)} y={y} gap={a2-b1:.1f}: {t1[:45]!r} <> {t2[:45]!r}")
                    bad += 1
    print("rowcheck collisions:", bad)
    return bad

def chartcheck():
    print("== chartcheck P6 (baseline-anchored boxes, gate < 30%) ==")
    path = os.path.join(ED, "p6-politique.svg")
    texts, rects = parse(path)
    labels = [e for e in texts if re.match(r"^(No lines|Work on Tuesday|Travel plans|Habit) : \d+%$", e["t"])]
    intro = [e for e in texts if ("practice survey" in e["t"] or "teaching data" in e["t"])]
    print(f"chart label lines: {len(labels)}, intro lines: {len(intro)}")
    worst = 0.0
    for e in labels + intro:
        f = font(kind_of(e["fam"]), e["bold"], e["size"])
        asc, desc = f.getmetrics()
        asc, desc = asc / 4.0, desc / 4.0
        adv = f.getlength(e["t"]) / 4.0
        # anchor 'ls': x = left edge, y = baseline
        bx0, bx1 = e["x"], e["x"] + adv
        by0, by1 = e["y"] - asc, e["y"] + desc
        area = (bx1 - bx0) * (by1 - by0)
        cov = 0.0
        for r in rects:
            if r["pos"] < e["pos"] or r["fill"] == "none":
                continue
            # only later-drawn rects: rects appear in doc order; compare positions
            ix = max(0.0, min(bx1, r["x"] + r["w"]) - max(bx0, r["x"]))
            iy = max(0.0, min(by1, r["y"] + r["h"]) - max(by0, r["y"]))
            cov = max(cov, ix * iy / area)
        # true-ink coverage for reference
        a, b, _ = ink_span(e["t"], kind_of(e["fam"]), e["bold"], e["size"], e["x"], e["anchor"])
        print(f"  {e['t'][:60]!r} baseline-box coverage={cov*100:.1f}%")
        worst = max(worst, cov)
    print(f"chartcheck worst baseline-box coverage: {worst*100:.1f}% (gate < 30%)")
    return worst

CORE = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/en-es-proof/reg-ed/svg")

def edgescan():
    print("== edgescan (flags: advance-right > 1910 inner frame; ink-right > 1910; ink vs frame bands) ==")
    print("== margin-crossers (advance-right > 1885) are informational; edition set must be a subset of core's or adjudicated ==")
    bad = 0
    for path in sorted(glob.glob(os.path.join(ED, "*.svg"))):
        texts, _ = parse(path)
        mx = 0.0
        for e in texts:
            f = font(kind_of(e["fam"]), e["bold"], e["size"])
            adv = f.getlength(e["t"]) / 4.0
            if e["anchor"] == "start":
                ar = e["x"] + adv
            elif e["anchor"] == "end":
                ar = e["x"]
            else:
                ar = e["x"] + adv / 2
            mx = max(mx, ar)
            if ar > 1910:
                print(f"{os.path.basename(path)} ADVANCE-FRAME {ar:.1f}: {e['t'][:60]!r}")
                bad += 1
            # ink box vertical extent via getbbox at 4x
            bb = f.getbbox(e["t"])
            top = e["y"] + bb[1] / 4.0
            bot = e["y"] + bb[3] / 4.0
            a, b, _ = ink_span(e["t"], kind_of(e["fam"]), e["bold"], e["size"], e["x"], e["anchor"])
            if b > 1910:
                print(f"{os.path.basename(path)} INK-FRAME {b:.1f}: {e['t'][:60]!r}")
                bad += 1
            if ar > 1885:
                print(f"{os.path.basename(path)} MARGIN-CROSS advance-right {ar:.1f}: {e['t'][:60]!r}")
            # frame press: ink box intersecting the frame rectangles' stroke bands
            # outer frame: x 28 (w 3.4) / 1922, y 28 / 2672 ; inner: 40 (1.2) / 1910, 40 / 2660
            for (fx0, fx1, fy0, fy1) in [(26.3, 29.7, 26.3, 2673.7), (1920.3, 1923.7, 26.3, 2673.7),
                                         (26.3, 1923.7, 26.3, 29.7), (26.3, 1923.7, 2668.3, 2671.7),
                                         (39.4, 40.6, 39.4, 2660.6), (1909.4, 1910.6, 39.4, 2660.6),
                                         (39.4, 1910.6, 39.4, 40.6), (39.4, 1910.6, 2659.4, 2660.6)]:
                if a < fx1 and b > fx0 and top < fy1 and bot > fy0:
                    print(f"{os.path.basename(path)} FRAME-PRESS: {e['t'][:60]!r}")
                    bad += 1
        print(f"{os.path.basename(path)} max advance-right: {mx:.1f}")
    print("edgescan flags:", bad)
    return bad

if __name__ == "__main__":
    r = rowcheck()
    c = chartcheck()
    e = edgescan()
    print(f"SUMMARY rowcheck={r} chartcheck_worst={c*100:.1f}% edgescan={e}")
