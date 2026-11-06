# -*- coding: utf-8 -*-
"""Same-row horizontal collision check (FRxRU rowcheck.py method, README #10):
for every pair of <text> nodes on the same baseline, compute true-ink spans
with PIL (via the NL build's svglib fonts) and report overlaps or gaps < 6.
"""
import re, sys, glob, os
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-nl-build')
import svglib

def measure(t, kind, bold, size):
    f = svglib._font(kind, bold, int(round(size * 4)))
    bb = f.getbbox(t)
    return bb[0] / 4.0, bb[2] / 4.0, f.getlength(t) / 4.0

def main(d):
    bad = 0
    for path in sorted(glob.glob(os.path.join(d, "*.svg"))):
        src = open(path, encoding="utf-8").read()
        rows = {}
        for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"( font-weight="700")?[^>]*?(?: text-anchor="(start|middle|end)")?[^>]*>([^<]*)</text>', src):
            x, y, fam, size, bold, anchor, t = (float(m.group(1)), float(m.group(2)), m.group(3),
                                                float(m.group(4)), bool(m.group(5)), m.group(6) or "start", m.group(7))
            if not t.strip():
                continue
            kind = "serif" if "Serif" in fam else "sans"
            l, r, adv = measure(t, kind, bold, size)
            if anchor == "start":
                a, b = x + l, x + r
            elif anchor == "end":
                a, b = x - adv + l, x - adv + r
            else:
                a, b = x - adv / 2 + l, x - adv / 2 + r
            rows.setdefault(round(y, 1), []).append((a, b, t))
        for y, spans in rows.items():
            spans.sort()
            for (a1, b1, t1), (a2, b2, t2) in zip(spans, spans[1:]):
                if a2 - b1 < 6:
                    print(f"{os.path.basename(path)} y={y} gap={a2-b1:.1f}: {t1[:40]!r} <> {t2[:40]!r}")
                    bad += 1
    print("collisions:", bad)

if __name__ == "__main__":
    main(sys.argv[1])
