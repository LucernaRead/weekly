# -*- coding: utf-8 -*-
"""Round-3 supplementary geometric scans for PT x FR W45 (not covered by
occlusion_audit.py's classes):
  1. rowcheck: same-baseline text-ink collisions (FR x RU lesson) — texts
     sharing one baseline must not overlap in ink. Uses the audit's own
     true-ink boxes (html-unescaped text, so &amp; hits are measured
     decoded, not as raw '&amp;' glyphs).
  2. P6 chart-label coverage by the BASELINE-ANCHORED ink method (PIL
     getmetrics ascent/descent, anchor ls): anchored box =
     (x_start, baseline - ascent, x_start + advance, baseline + descent);
     coverage = overlap with LATER-drawn opaque rects / anchored area.
     <30% passes; the getbbox method's inflated readings do not count.
  3. frame scan: every text/image ink box vs the page frame strips
     (outer rect 28/3.4, inner rect 40/1.2 — drawn first, so LINEX never
     fires on them and BOXTITLE excludes whole-page boxes) + ink-right
     vs the inner frame line (1910).
Run: <tools/venv>/python extra_scans.py <edition-svg-dir>
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "tools"))
import occlusion_audit as OA


def anchored_box(el):
    """Baseline-anchored em box for a text El (getmetrics/getlength)."""
    a = el.attrs
    size = OA.fnum(a, "font-size", 20.0)
    bold = a.get("font-weight", "") in ("700", "bold")
    f = OA.get_font(a.get("font-family", ""), size, bold)
    adv = f.getlength(el.text) / OA.SCALE
    asc, desc = f.getmetrics()[0] / OA.SCALE, f.getmetrics()[1] / OA.SCALE
    x = OA.fnum(a, "x")
    anchor = a.get("text-anchor", "start")
    if anchor == "middle":
        left = x - adv / 2
    elif anchor == "end":
        left = x - adv
    else:
        left = x
    return (left, el.baseline - asc, left + adv, el.baseline + desc)


def overlap_area(a, b):
    w = min(a[2], b[2]) - max(a[0], b[0])
    h = min(a[3], b[3]) - max(a[1], b[1])
    return w * h if w > 0 and h > 0 else 0.0


def main():
    svgdir = sys.argv[1]
    pages = ["p1-capa", "p2-vida", "p3-cultura", "p4-esporte",
             "p5-jovens", "p6-aprofundamento", "p7-lingua", "p8-avaliacao"]
    # ---- 1. rowcheck ----
    print("=== 1. same-baseline rowcheck (true ink, decoded text) ===")
    total_hits = 0
    for pg in pages:
        els, _, _ = OA.parse_svg(open(os.path.join(svgdir, pg + ".svg"),
                                      encoding="utf-8").read())
        by_base = {}
        for el in els:
            if el.kind == "text" and el.box:
                by_base.setdefault(el.baseline, []).append(el)
        hits = []
        for y, group in by_base.items():
            if len(group) < 2:
                continue
            group = sorted(group, key=lambda e: e.box[0])
            for a, b in zip(group, group[1:]):
                ov = a.box[2] - b.box[0]
                if ov > 0.5:
                    hits.append((y, a.text[:40], b.text[:40], round(ov, 1)))
        total_hits += len(hits)
        print(f"  {pg}: {len(hits)} same-baseline collisions")
        for h in hits:
            print(f"    y={h[0]} overlap={h[3]}px :: {h[1]!r} vs {h[2]!r}")
    print(f"  TOTAL rowcheck collisions: {total_hits}")
    # ---- 2. P6 anchored chart coverage ----
    print("=== 2. P6 chart-label coverage (baseline-anchored method) ===")
    els, _, _ = OA.parse_svg(open(os.path.join(svgdir, "p6-aprofundamento.svg"),
                                  encoding="utf-8").read())
    worst = []
    for i, el in enumerate(els):
        if el.kind != "text" or not el.text.strip():
            continue
        ab = anchored_box(el)
        area = (ab[2] - ab[0]) * (ab[3] - ab[1])
        if area <= 0:
            continue
        cov = 0.0
        for later in els[i + 1:]:
            if later.kind == "rect" and OA.is_opaque(later) and later.box:
                cov += overlap_area(ab, later.box)
        frac = cov / area
        if frac > 0.005:
            worst.append((round(frac * 100, 1), el.text[:50], el.baseline))
    worst.sort(reverse=True)
    print(f"  P6 texts with >0.5% later-rect coverage: {len(worst)}")
    for f, t, y in worst[:12]:
        print(f"    {f}% :: y={y} :: {t!r}")
    print(f"  P6 MAX anchored coverage: {worst[0][0] if worst else 0.0}% (gate <30%)")
    # ---- 3. frame scan ----
    print("=== 3. frame scan (ink vs frame strips; inner frame right=1910) ===")
    vstrips = [(26.3, 29.7, "outer-left"), (39.4, 40.6, "inner-left"),
               (1909.4, 1910.6, "inner-right"), (1920.3, 1923.7, "outer-right")]
    hstrips = [(26.3, 29.7, "outer-top"), (39.4, 40.6, "inner-top"),
               (2659.4, 2660.6, "inner-bottom"), (2670.3, 2673.7, "outer-bottom")]
    for pg in pages:
        els, _, _ = OA.parse_svg(open(os.path.join(svgdir, pg + ".svg"),
                                      encoding="utf-8").read())
        maxr, minl, maxb = 0.0, 9999.0, 0.0
        flags = []
        for el in els:
            if el.kind not in ("text", "image") or not el.box:
                continue
            l, t, r, b = el.box
            maxr, minl = max(maxr, r), min(minl, l)
            if el.kind == "text":
                maxb = max(maxb, b)
            for x0, x1, name in vstrips:
                if l < x1 and r > x0:
                    flags.append((name, (el.text or "image")[:40]))
            for y0, y1, name in hstrips:
                if t < y1 and b > y0:
                    flags.append((name, (el.text or "image")[:40]))
        over = [f for f in flags if "inner" in f[0] or "outer" in f[0]]
        print(f"  {pg}: max ink-right={maxr:.1f} min ink-left={minl:.1f} "
              f"max text-ink-bottom={maxb:.1f} frame-strip hits={len(over)}")
        for f in over[:6]:
            print(f"    STRIP {f[0]} :: {f[1]!r}")
    # P7 quote clearance vs preview band top 2404
    els, _, _ = OA.parse_svg(open(os.path.join(svgdir, "p7-lingua.svg"),
                                  encoding="utf-8").read())
    q = [el for el in els if el.kind == "text" and el.baseline and 1900 < el.baseline < 2404]
    if q:
        print(f"  P7 last quote-region ink bottom: {max(el.box[3] for el in q):.1f} "
              f"(preview band top 2404, clearance "
              f"{2404 - max(el.box[3] for el in q):.1f}px)")


if __name__ == "__main__":
    main()
