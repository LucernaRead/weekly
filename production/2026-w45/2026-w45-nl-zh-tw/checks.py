# -*- coding: utf-8 -*-
"""Builder self-checks for NL x ZH-TW W45 (run from the tools dir or anywhere;
occlusion_audit is imported by path). Two checks the canonical audit cannot see:
  1. same-baseline ink collisions (README #10): text runs on one baseline
     whose true ink boxes overlap (furniture bands especially).
  2. P6 chart-label coverage by the baseline-anchored ink method (README #12
     blind spot): for every chart label text element, measure the fraction
     of its ink box covered by later-drawn rects (bars), using PIL
     getmetrics ascent/descent with anchor='ls' -- NOT getbbox (which
     inflates the box and over-reports coverage).
"""
import glob
import os
import sys

sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
from PIL import ImageFont

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-zh-tw/svg")


def rowcheck():
    print("== same-baseline rowcheck ==")
    total = 0
    for path in sorted(glob.glob(os.path.join(ED, "*.svg"))):
        els, W, H = OA.parse_svg(open(path, encoding="utf-8").read())
        texts = [e for e in els if e.kind == "text" and e.box]
        by_base = {}
        for e in texts:
            by_base.setdefault(round(e.baseline), []).append(e)
        for base, group in sorted(by_base.items()):
            group.sort(key=lambda e: e.box[0])
            for a, b in zip(group, group[1:]):
                if b.box[0] < a.box[2] - 0.01:  # ink overlap on one baseline
                    print(f"  COLLISION {os.path.basename(path)} y={base}: "
                          f"{a.text[:40]!r} [{a.box[0]:.1f},{a.box[2]:.1f}] vs "
                          f"{b.text[:40]!r} [{b.box[0]:.1f},{b.box[2]:.1f}]")
                    total += 1
    print(f"  same-baseline collisions: {total}")
    return total


def chartcheck():
    print("== P6 chart-label coverage (baseline-anchored ink) ==")
    path = os.path.join(ED, "p6-verdieping.svg")
    els, W, H = OA.parse_svg(open(path, encoding="utf-8").read())
    # Chart labels = text elements inside the col-3 chart box
    # (x 1451..1885, y 200..691 in content56). Baseline-anchored ink box:
    # PIL getmetrics ascent/descent with anchor 'ls', measured on the
    # audit's 4x-supersampled font and divided back by 4 -- NOT getbbox
    # (getbbox inflates the box and over-reports coverage).
    # Coverage = fraction of the label ink box intersected by any rect
    # drawn AFTER the label in paint order (i.e. bars overprinting labels).
    worst = 0.0
    for i, e in enumerate(els):
        if e.kind != "text":
            continue
        x = OA.fnum(e.attrs, "x")
        if not (1451 <= x <= 1885 and 200 <= e.baseline <= 691):
            continue
        size = OA.fnum(e.attrs, "font-size", 20.0)
        bold = e.attrs.get("font-weight", "") in ("700", "bold")
        font = OA.get_font(e.attrs.get("font-family", ""), size, bold)
        asc, desc = font.getmetrics()
        asc, desc = asc / 4.0, desc / 4.0
        w = font.getlength(e.text) / 4.0
        anchor = e.attrs.get("text-anchor", "start")
        if anchor == "middle":
            x0 = x - w / 2
        elif anchor == "end":
            x0 = x - w
        else:
            x0 = x
        box = (x0, e.baseline - asc, x0 + w, e.baseline + desc)
        area = (box[2] - box[0]) * (box[3] - box[1])
        if area <= 0:
            continue
        for later in els[i + 1:]:
            if later.kind != "rect" or not later.box:
                continue
            ix = max(0, min(box[2], later.box[2]) - max(box[0], later.box[0]))
            iy = max(0, min(box[3], later.box[3]) - max(box[1], later.box[1]))
            cov = ix * iy / area
            if cov > 0.001:
                print(f"  {e.text[:44]!r} covered {cov*100:.1f}% by rect {later.box}")
            worst = max(worst, cov)
    print(f"  worst chart-label coverage: {worst*100:.1f}% (gate <30%)")
    return worst


if __name__ == "__main__":
    c = rowcheck()
    w = chartcheck()
    print(f"RESULT rowcheck={c} chartworst={w*100:.1f}%")
    sys.exit(0 if c == 0 and w < 0.30 else 1)
