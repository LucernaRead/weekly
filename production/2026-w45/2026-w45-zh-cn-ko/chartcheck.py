# -*- coding: utf-8 -*-
"""Chart-label element check (README #12): on chart pages, compare every
text node's true-ink box against every LATER-drawn rect; report ink
covered by a later rect. Same-baseline/own-chip overlaps are reported
separately so design-internal chip text can be adjudicated."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib


def measure(t, kind, bold, size):
    f = svglib._font(kind, bold, int(round(size * 4)))
    bb = f.getbbox(t)
    return bb[0] / 4.0, bb[2] / 4.0, bb[1] / 4.0, bb[3] / 4.0, f.getlength(t) / 4.0


def check(path):
    src = open(path, encoding="utf-8").read()
    # ordered elements: texts and rects with document order
    elems = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"( font-weight="700")?[^>]*?(?: text-anchor="(start|middle|end)")?[^>]*>([^<]*)</text>|<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*>', src):
        if m.group(7) is not None or m.group(8) is not None:
            pass
        elems.append(m)
    # simpler: tokenise in order
    toks = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"( font-weight="700")?[^>]*?(?: text-anchor="(start|middle|end)")?[^>]*>([^<]*)</text>', src):
        toks.append(("text", m.start(), m))
    for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]*)"', src):
        toks.append(("rect", m.start(), m))
    toks.sort(key=lambda x: x[1])
    texts = []
    bad = 0
    for kind, _, m in toks:
        if kind == "text":
            x, y, fam, size = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4))
            bold, anchor, t = bool(m.group(5)), m.group(6) or "start", m.group(7)
            if not t.strip():
                continue
            fkind = "serif" if "Serif" in fam else "sans"
            l, r, top, bot, adv = measure(t, fkind, bold, size)
            if anchor == "start":
                a, b = x + l, x + r
            elif anchor == "end":
                a, b = x - adv + l, x - adv + r
            else:
                a, b = x - adv / 2 + l, x - adv / 2 + r
            texts.append((a, b, y + top, y + bot, t))
        else:
            rx, ry, rw, rh = float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4))
            fill = m.group(5)
            if fill in ("none", ""):
                continue
            for (a, b, top, bot, t) in texts:
                ix = max(0, min(b, rx + rw) - max(a, rx))
                iy = max(0, min(bot, ry + rh) - max(top, ry))
                if ix > 0 and iy > 0:
                    area = ix * iy
                    ink = (b - a) * (bot - top)
                    cov = area / ink if ink else 0
                    if cov > 0.001:
                        print(f"{os.path.basename(path)} later-rect covers {cov:.1%} of {t[:40]!r} rect=({rx},{ry},{rw}x{rh})")
                        bad += 1
    print(f"{os.path.basename(path)} chart-label flags: {bad}")
    return bad


if __name__ == "__main__":
    total = 0
    for p in sys.argv[1:]:
        total += check(p)
    print("TOTAL:", total)
    sys.exit(1 if total else 0)
