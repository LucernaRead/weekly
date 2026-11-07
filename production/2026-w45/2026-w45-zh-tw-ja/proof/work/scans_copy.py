# -*- coding: utf-8 -*-
"""Same-baseline ink spacing (README #10) + chart-label graze + border-strike
scan for the W45 zh-tw x ja edition vs core. Uses tools occlusion_audit ink_box."""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools")))
from occlusion_audit import ink_box, parse_svg
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
def scan(d):
    same, graze, strike = [], [], []
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".svg"): continue
        els, _, _ = parse_svg(open(os.path.join(d, fn), encoding="utf-8").read())
        shapes = [e for e in els if e.kind != "text" and e.box]
        texts = [e for e in els if e.kind == "text"]
        # same-baseline: group by baseline y (rounded), sort by x, check ink gaps
        by_y = {}
        for e in texts:
            by_y.setdefault(round(e.baseline or 0), []).append(e)
        for y, grp in by_y.items():
            grp = sorted(grp, key=lambda e: e.box[0])
            for a, b in zip(grp, grp[1:]):
                if b.box[0] < a.box[2] - 0.5 and a.box[1] < b.box[3] and b.box[1] < a.box[3]:
                    same.append((fn, y, a.text[:30], b.text[:30]))
        # chart graze: text ink vs later-drawn rects (bars) on p4/p6
        if fn in ("p4-sport.svg", "p6-deep.svg"):
            rects = [s for s in shapes if s.kind == "rect" and s.attrs.get("fill") in ("#a4553a", "#3e4c2a")]
            for e in texts:
                for r in rects:
                    if r.idx < e.idx: continue
                    rl, rt, rr, rb = r.box
                    if not (e.box[2] < rl or e.box[0] > rr or e.box[3] < rt or e.box[1] > rb):
                        graze.append((fn, e.text[:30], f"rect@{r.idx}"))
        # border-strike: any text ink crossing a bordered rect's top/bottom edge band
        rects = [s for s in shapes if s.kind == "rect" and s.attrs.get("stroke") not in (None, "none")]
        for e in texts:
            for r in rects:
                rl, rt, rr, rb = r.box
                if not (rl <= e.box[0] <= rr or rl <= e.box[2] <= rr): continue
                if rt - 2 <= e.box[1] <= rt + 2 or rt - 2 <= e.box[3] <= rt + 2 or rb - 2 <= e.box[1] <= rb + 2 or rb - 2 <= e.box[3] <= rb + 2:
                    # ink touches the border line itself (not just inside the box)
                    if e.box[1] < rt < e.box[3] or e.box[1] < rb < e.box[3]:
                        strike.append((fn, e.text[:30], f"rect y={rt:.0f}..{rb:.0f} ink={e.box[1]:.1f}..{e.box[3]:.1f}"))
    return same, graze, strike
for label, d in [("EDITION", os.path.join(GOAL, "files/weekly-report-w45-zh-tw-ja/svg")),
                 ("CORE", os.path.join(GOAL, "files/weekly-report-w45-zhtw-core/svg"))]:
    s, g, t = scan(d)
    print(f"{label} same-baseline={len(s)} {s[:5]}")
    print(f"{label} chart-graze={len(g)} {g[:5]}")
    print(f"{label} border-strike={len(t)} {t[:10]}")
