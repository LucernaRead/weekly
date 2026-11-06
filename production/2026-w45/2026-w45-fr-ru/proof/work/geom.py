# -*- coding: utf-8 -*-
"""Independent geometry scans for W45 FRxRU proofread (own implementation).
Uses PIL true-ink boxes via the build's svglib font loader (from my repro copy).
Scans: (1) same-baseline collisions gap<6; (2) right-edge ink>1885.5;
(3) P6 chart-label coverage, baseline-anchored (later rect covering a text baseline);
(4) P8 three calibers: flow cursor (driver log), max text baseline, max ink bottom;
(5) P7 readers-corner + preview ink bottoms vs box bottoms; (6) footer rule line y.
"""
import re, sys, glob, os, html
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "fr-ru-proof", "work", "repro"))
# svglib lives in repro copy; adjust: this file is in work/, repro is work/repro
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "repro"))
import svglib

TRE = re.compile(r'<text\b([^>]*)>([^<]*)</text>')
RRE = re.compile(r'<rect\b([^>]*)/?>')
LRE = re.compile(r'<line\b([^>]*)/?>')

def attr(a, k):
    m = re.search(k + r'="([^"]*)"', a)
    return m.group(1) if m else None

def measure(t, kind, bold, size):
    f = svglib._font(kind, bold, int(round(size * 4)))
    bb = f.getbbox(t)
    return bb[0] / 4.0, bb[2] / 4.0, bb[3] / 4.0, f.getlength(t) / 4.0

def parse_texts(path):
    src = open(path, encoding="utf-8").read()
    out = []
    for m in TRE.finditer(src):
        a, t = m.group(1), html.unescape(m.group(2))
        if not t.strip():
            continue
        x, y = float(attr(a, "x")), float(attr(a, "y"))
        fam, size = attr(a, "font-family"), float(attr(a, "font-size"))
        bold = attr(a, "font-weight") == "700"
        anchor = attr(a, "text-anchor") or "start"
        kind = "serif" if "Serif" in (fam or "") else "sans"
        l, r, bot, adv = measure(t, kind, bold, size)
        if anchor == "start":
            left, right = x + l, x + r
        elif anchor == "end":
            left, right = x - adv + l, x - adv + r
        else:
            left, right = x - adv / 2 + l, x - adv / 2 + r
        out.append({"x": x, "y": y, "t": t, "left": left, "right": right,
                    "ink_bottom": y + bot, "size": size, "anchor": anchor})
    return out

def parse_rects(path):
    src = open(path, encoding="utf-8").read()
    out = []
    for m in RRE.finditer(src):
        a = m.group(1)
        if attr(a, "fill") in (None, "none"):
            continue
        out.append({"x": float(attr(a, "x") or 0), "y": float(attr(a, "y") or 0),
                    "w": float(attr(a, "width") or 0), "h": float(attr(a, "height") or 0),
                    "pos": m.start()})
    return out

def parse_items(path):
    # document-order items (rects + texts) for coverage scan
    src = open(path, encoding="utf-8").read()
    items = []
    for m in RRE.finditer(src):
        a = m.group(1)
        if attr(a, "fill") in (None, "none"):
            continue
        items.append(("rect", float(attr(a, "x") or 0), float(attr(a, "y") or 0),
                      float(attr(a, "width") or 0), float(attr(a, "height") or 0), m.start()))
    for m in TRE.finditer(src):
        a, t = m.group(1), html.unescape(m.group(2))
        if not t.strip():
            continue
        x, y = float(attr(a, "x")), float(attr(a, "y"))
        fam, size = attr(a, "font-family"), float(attr(a, "font-size"))
        bold = attr(a, "font-weight") == "700"
        anchor = attr(a, "text-anchor") or "start"
        kind = "serif" if "Serif" in (fam or "") else "sans"
        l, r, bot, adv = measure(t, kind, bold, size)
        if anchor == "start":
            left, right = x + l, x + r
        elif anchor == "end":
            left, right = x - adv + l, x - adv + r
        else:
            left, right = x - adv / 2 + l, x - adv / 2 + r
        items.append(("text", left, y, right, t, m.start()))
    items.sort(key=lambda it: it[-1])
    return items

def scan_dir(d, label):
    print(f"===== {label} : {d}")
    tot_coll = 0
    for path in sorted(glob.glob(os.path.join(d, "*.svg"))):
        ts = parse_texts(path)
        rows = {}
        for t in ts:
            rows.setdefault(round(t["y"], 1), []).append(t)
        for y, spans in rows.items():
            spans.sort(key=lambda s: s["left"])
            for a, b in zip(spans, spans[1:]):
                if b["left"] - a["right"] < 6:
                    print(f"  COLL {os.path.basename(path)} y={y} gap={b['left']-a['right']:.1f}: {a['t'][:40]!r} <> {b['t'][:40]!r}")
                    tot_coll += 1
        for t in ts:
            if t["right"] > 1885.5:
                print(f"  EDGE {os.path.basename(path)} ink_right={t['right']:.1f} y={t['y']} :: {t['t'][:70]!r}")
    print(f"  same-baseline collisions: {tot_coll}")

def p6_coverage(path):
    items = parse_items(path)
    tot = cov = 0
    hits = []
    for i, it in enumerate(items):
        if it[0] != "text":
            continue
        _, ax, by, bx, t, _ = it
        tot += 1
        for j in range(i + 1, len(items)):
            r = items[j]
            if r[0] != "rect":
                continue
            _, rx, ry, rw, rh, _ = r
            if ry <= by <= ry + rh and min(bx, rx + rw) > max(ax, rx):
                cov += 1
                hits.append((t[:50], round(by, 1)))
                break
    print(f"P6 coverage {path}: {cov}/{tot} = {100*cov/tot:.2f}%  hits={hits[:10]}")

def p8_calibers(path, label):
    ts = parse_texts(path)
    maxbase = max(t["y"] for t in ts)
    maxink = max(t["ink_bottom"] for t in ts)
    deep = sorted(ts, key=lambda t: t["ink_bottom"], reverse=True)[:5]
    print(f"P8 {label}: max baseline={maxbase} max ink bottom={maxink:.1f}")
    for t in deep:
        print(f"    ink_bottom={t['ink_bottom']:.1f} y={t['y']} :: {t['t'][:60]!r}")
    return maxbase, maxink

def p7_boxes(path, label):
    ts = parse_texts(path)
    rects = parse_rects(path)
    print(f"P7 {label}: rects with bottom in [2200,2300]:")
    for r in rects:
        if 2200 <= r["y"] + r["h"] <= 2300:
            print(f"    rect x={r['x']} y={r['y']} w={r['w']} h={r['h']} bottom={r['y']+r['h']}")
    print(f"P7 {label}: disclosure lines (Примечание редакции: настоящих):")
    for t in ts:
        if "настоящих писем" in t or "настоящие работы" in t:
            print(f"    y={t['y']} ink_bottom={t['ink_bottom']:.1f} :: {t['t'][:90]!r}")
    print(f"P7 {label}: preview lines (LA SEMAINE PROCHAINE / СЛЕДУЮЩАЯ НЕДЕЛЯ / 11 ноября etc):")
    for t in ts:
        if "SEMAINE PROCHAINE" in t or "СЛЕДУЮЩ" in t or "Диеп" in t or "Сенат" in t:
            print(f"    y={t['y']} ink_bottom={t['ink_bottom']:.1f} :: {t['t'][:90]!r}")
    print(f"P7 {label}: max ink bottom overall={max(t['ink_bottom'] for t in ts):.1f}, max baseline={max(t['y'] for t in ts)}")

def footer_lines(path, label):
    src = open(path, encoding="utf-8").read()
    ys = set()
    for m in LRE.finditer(src):
        a = m.group(1)
        y1, y2 = attr(a, "y1"), attr(a, "y2")
        if y1 and y1 == y2:
            ys.add(float(y1))
    print(f"{label} horizontal line ys near footer: {sorted(y for y in ys if y > 2500)}")

if __name__ == "__main__":
    G = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
    scan_dir(f"{G}/files/weekly-report-w45-fr-ru/svg", "EDITION")
    scan_dir(f"{G}/files/weekly-report-w45-fr-core/svg", "CORE")
    p6_coverage(f"{G}/files/weekly-report-w45-fr-ru/svg/p6-politique.svg")
    p6_coverage(f"{G}/files/weekly-report-w45-fr-core/svg/p6-politique.svg")
    p8_calibers(f"{G}/files/weekly-report-w45-fr-ru/svg/p8-exercices.svg", "EDITION")
    p8_calibers(f"{G}/files/weekly-report-w45-fr-core/svg/p8-exercices.svg", "CORE")
    p7_boxes(f"{G}/files/weekly-report-w45-fr-ru/svg/p7-langue.svg", "EDITION")
    p7_boxes(f"{G}/files/weekly-report-w45-fr-core/svg/p7-langue.svg", "CORE")
    footer_lines(f"{G}/files/weekly-report-w45-fr-ru/svg/p8-exercices.svg", "P8 ED")
    footer_lines(f"{G}/files/weekly-report-w45-fr-ru/svg/p6-politique.svg", "P6 ED")
    footer_lines(f"{G}/files/weekly-report-w45-fr-ru/svg/p1-une.svg", "P1 ED")
