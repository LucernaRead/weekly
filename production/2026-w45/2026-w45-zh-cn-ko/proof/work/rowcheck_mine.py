# -*- coding: utf-8 -*-
"""Proofreader's own same-baseline ink-collision scan (README #10 pattern).
For every pair of <text> nodes sharing a baseline (rounded y), compute true-ink
spans with PIL via the copied svglib fonts; report overlaps or gaps < 6 units.
Usage: rowcheck_mine.py <svg-dir>
"""
import re, sys, glob, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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
    return bad

if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1]) else 0)
