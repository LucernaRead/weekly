# -*- coding: utf-8 -*-
"""Supplementary geometry scans for KO x RU (beyond canonical occlusion_audit):
 A. Same-baseline ink collisions (README #10): pairs of text elements with
    baselines within 3 units whose ink boxes overlap or gap < 2.
 B. Border-cut scan (nl-pt B1 lesson): text ink crossing the border of a
    later-drawn border-only rect (fill none) while starting inside it;
    page-frame rects excluded.
 C. P6 table-label coverage (baseline-anchored ink method, NOT getbbox
    ascender): for every text element on p6, max overlap fraction vs any
    later-drawn rect/image; report the max (gate < 30%).
 D. Right-edge advance scan: advance right edge (anchor-aware, PIL
    getlength) past the 1885 content edge, or advance left before 65.
Uses tools/occlusion_audit.py parsing + font resolution (read-only).
Usage: tools/venv/bin/python geom_extra.py <svg-dir>
"""
import sys, os

sys.path.insert(0, os.path.expanduser(
    "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ko-ru-proof/work/scratch"))
import occlusion_audit as oa

SVGDIR = sys.argv[1]


def adv_right(el):
    a = el.attrs
    f = oa.get_font(a.get("font-family", ""), oa.fnum(a, "font-size", 20.0),
                    a.get("font-weight", "") in ("700", "bold"))
    adv = f.getlength(el.text) / oa.SCALE
    anchor = a.get("text-anchor", "start")
    x = oa.fnum(a, "x")
    if anchor == "middle":
        return x - adv / 2, x + adv / 2
    if anchor == "end":
        return x - adv, x
    return x, x + adv


for fn in sorted(os.listdir(SVGDIR)):
    if not fn.endswith(".svg"):
        continue
    els, W, H = oa.parse_svg(open(os.path.join(SVGDIR, fn), encoding="utf-8").read())
    texts = [el for el in els if el.kind == "text" and el.text and el.text.strip() and el.box]
    # A. same-baseline
    bad_a = 0
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            a, b = texts[i], texts[j]
            if abs(a.baseline - b.baseline) > 3:
                continue
            if a.box[1] >= b.box[3] or b.box[1] >= a.box[3]:
                continue
            gap = max(b.box[0] - a.box[2], a.box[0] - b.box[2])
            if gap < 2:
                bad_a += 1
                print(f"A {fn} y={a.baseline}: GAP {gap:.1f} {a.text[:36]!r} <-> {b.text[:36]!r}")
    # B. border-cut: later border-only rects
    bad_b = 0
    rects = []
    for idx, el in enumerate(els):
        if el.kind == "rect" and el.box:
            fill = (el.attrs.get("fill") or "").lower()
            if fill in ("none", "") and el.attrs.get("stroke"):
                # exclude page frames (full-page rects)
                if el.box[0] <= 40 and el.box[2] >= 1900:
                    continue
                rects.append((idx, el))
    for idx, el in enumerate(texts):
        for ridx, r in rects:
            if ridx <= els.index(el):
                continue
            rx0, ry0, rx1, ry1 = r.box
            # text starts inside the rect horizontally and overlaps vertically
            if not (el.box[0] >= rx0 - 1 and el.box[0] < rx1):
                continue
            if el.box[3] < ry0 or el.box[1] > ry1:
                continue
            if el.box[2] > rx1 + 0.5 or el.box[0] < rx0 - 0.5:
                bad_b += 1
                print(f"B {fn} text {el.text[:40]!r} ink {el.box} crosses rect {r.box}")
    # C. P6 only: max later-rect/image coverage of text ink
    if fn.startswith("p6"):
        worst = (0.0, None)
        for idx, el in enumerate(texts):
            tx0, ty0, tx1, ty1 = el.box
            tarea = max(0.0, (tx1 - tx0) * (ty1 - ty0))
            if tarea == 0:
                continue
            for later in els[els.index(el) + 1:]:
                if later.kind not in ("rect", "image") or not later.box:
                    continue
                if later.kind == "rect" and (later.attrs.get("fill") or "").lower() in ("none", ""):
                    continue
                ix0, iy0 = max(tx0, later.box[0]), max(ty0, later.box[1])
                ix1, iy1 = min(tx1, later.box[2]), min(ty1, later.box[3])
                if ix1 > ix0 and iy1 > iy0:
                    frac = (ix1 - ix0) * (iy1 - iy0) / tarea
                    if frac > worst[0]:
                        worst = (frac, (el.text[:40], later.kind, later.box))
        print(f"C {fn} max later-cover fraction: {worst[0]*100:.1f}% {worst[1]}")
    # D. advance edges
    bad_d = 0
    for el in texts:
        l, r = adv_right(el)
        if r > 1885.5 or l < 64.5:
            # footer right text ends exactly at 1885 by design; allow <= 1885.5
            if r > 1885.5 or l < 64.5:
                bad_d += 1
                print(f"D {fn} advance [{l:.1f}, {r:.1f}] {el.text[:40]!r}")
    print(f"{fn}: A={bad_a} B={bad_b} D={bad_d}")
