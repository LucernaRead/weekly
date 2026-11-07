# -*- coding: utf-8 -*-
"""W46 shared checks: same-baseline row collisions (all pages) + P6 chart
later-rect graze. Usage: checks.py <edition-build-dir> <svg-dir>
Imports svglib from the edition build dir (correct CJK face per edition)."""
import re, sys, glob, os
sys.path.insert(0, sys.argv[1])
import svglib

def measure(t, kind, bold, size):
    f = svglib._font(kind, bold, int(round(size * 4)))
    bb = f.getbbox(t)
    return bb[0] / 4.0, bb[2] / 4.0, f.getlength(t) / 4.0

TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"( font-weight="700")?[^>]*?(?: text-anchor="(start|middle|end)")?[^>]*>([^<]*)</text>')

def texts(src):
    out = []
    for m in TEXT_RE.finditer(src):
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
        out.append((m.start(), a, y - size, b, y + size * 0.25, t, y))
    return out

def rowcheck(d):
    bad = 0
    for path in sorted(glob.glob(os.path.join(d, "*.svg"))):
        src = open(path, encoding="utf-8").read()
        rows = {}
        for _, a, _, b, _, t, y in texts(src):
            rows.setdefault(round(y, 1), []).append((a, b, t))
        for y, spans in rows.items():
            spans.sort()
            for (a1, b1, t1), (a2, b2, t2) in zip(spans, spans[1:]):
                if a2 - b1 < 6:
                    print(f"{os.path.basename(path)} y={y} gap={a2-b1:.1f}: {t1[:40]!r} <> {t2[:40]!r}")
                    bad += 1
    print("rowcheck collisions:", bad)
    return bad

def chartcheck(path):
    src = open(path, encoding="utf-8").read()
    pos = []
    for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)" fill="([^"]*)"', src):
        pos.append((m.start(), "rect", float(m.group(1)), float(m.group(2)),
                    float(m.group(1)) + float(m.group(3)), float(m.group(2)) + float(m.group(4)), m.group(5)))
    for st, a, ay, b, by, t, _ in texts(src):
        pos.append((st, "text", a, ay, b, by, t))
    pos.sort()
    bad = 0
    for j, (st, k, ax, ay, bx, by, t) in enumerate(pos):
        if k != "text":
            continue
        for (st2, k2, ax2, ay2, bx2, by2, fill) in pos[j + 1:]:
            if k2 != "rect":
                continue
            if ax < bx2 and ax2 < bx and ay < by2 and ay2 < by:
                print(f"OVERLAP text {t[:44]!r} ink=({ax:.0f},{ay:.0f},{bx:.0f},{by:.0f}) vs later rect fill={fill} ({ax2:.0f},{ay2:.0f},{bx2:.0f},{by2:.0f})")
                bad += 1
    print("chart later-rect overlaps:", bad)
    return bad

if __name__ == "__main__":
    b = rowcheck(sys.argv[2])
    c = chartcheck(os.path.join(sys.argv[2], "p6-afondo.svg"))
    print("CHECKS:", "PASS" if b == 0 and c == 0 else "FLAGS PRESENT (adjudicate)")
