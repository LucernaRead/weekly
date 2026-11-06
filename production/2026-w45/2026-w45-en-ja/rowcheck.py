# -*- coding: utf-8 -*-
"""Same-row horizontal collision check (README #10): for every pair of
<text> nodes on the same baseline (same y), compute true-ink spans with
PIL via the build's own svglib fonts and report overlaps or gaps < 6.
Attribute parsing is explicit (no lazy-quantifier anchor swallowing)."""
import glob
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib

TEXT_RE = re.compile(r"<text\s([^>]*)>([^<]*)</text>")
ATTR_RE = re.compile(r"([\w-]+)=\"([^\"]*)\"")


def parse_texts(src):
    out = []
    for m in TEXT_RE.finditer(src):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        if "x" not in attrs or "y" not in attrs:
            continue
        out.append((float(attrs["x"]), float(attrs["y"]), attrs.get("font-family", ""),
                    float(attrs.get("font-size", "20")), attrs.get("font-weight") == "700",
                    attrs.get("text-anchor", "start"), html.unescape(m.group(2))))
    return out


def measure(t, kind, bold, size):
    f = svglib._font(kind, bold, int(round(size * 4)))
    bb = f.getbbox(t)
    return bb[0] / 4.0, bb[2] / 4.0, f.getlength(t) / 4.0


def main(d):
    bad = 0
    for path in sorted(glob.glob(os.path.join(d, "*.svg"))):
        src = open(path, encoding="utf-8").read()
        rows = {}
        for x, y, fam, size, bold, anchor, t in parse_texts(src):
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
