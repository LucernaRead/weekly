# -*- coding: utf-8 -*-
"""Same-baseline ink-spacing scan (README #10 supplement to occlusion_audit).
Uses svglib text_w (advance widths, >= true ink) with anchor handling, so a
>=0 advance gap implies a >=0 ink gap. Flags gaps < 5 px on shared baselines."""
import re, glob, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import text_w
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-ru/svg")
CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-core/svg")
def elems(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', s):
        a, t = m.group(1), m.group(2)
        def attr(name, default=None):
            mm = re.search(rf'{name}="([^"]*)"', a)
            return mm.group(1) if mm else default
        x = float(attr("x", 0)); y = float(attr("y", 0))
        size = float(attr("font-size", 20))
        fam = attr("font-family", "")
        kind = "sans" if "Sans" in fam else "serif"
        bold = attr("font-weight") in ("700", "bold")
        anchor = attr("text-anchor", "start")
        w = text_w(t, kind, bold, size)
        left = x - w if anchor == "end" else (x - w / 2 if anchor == "middle" else x)
        out.append((y, left, left + w, t))
    return out
for label, d in [("edition", ED), ("core", CORE)]:
    flags = 0
    for f in sorted(glob.glob(d + "/*.svg")):
        by = {}
        for y, l, r, t in elems(f):
            by.setdefault(round(y, 1), []).append((l, r, t))
        for y, items in by.items():
            items.sort()
            for (l1, r1, t1), (l2, r2, t2) in zip(items, items[1:]):
                gap = l2 - r1
                if gap < 5:
                    print(f"{label} {os.path.basename(f)} y={y} gap={gap:.1f} :: {t1[:40]!r} | {t2[:40]!r}")
                    flags += 1
    print(label, "same-baseline flags (<5px):", flags)
