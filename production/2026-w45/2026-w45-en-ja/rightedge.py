# -*- coding: utf-8 -*-
"""Right-edge scan (ADVANCE method): for every <text> node, compute the
advance right edge from its anchor and flag advance past the text right
margin (RIGHT = 1885) or past the page edge (1950). End-anchored texts
end at x by construction and are exempt from the margin rule (their
leftward extent is a separate concern, covered by the ink audit)."""
import glob
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib

TEXT_RE = re.compile(r"<text\s([^>]*)>([^<]*)</text>")
ATTR_RE = re.compile(r"([\w-]+)=\"([^\"]*)\"")
RIGHT = 1885.0
PAGE = 1950.0


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


def main(d):
    bad = 0
    for path in sorted(glob.glob(os.path.join(d, "*.svg"))):
        src = open(path, encoding="utf-8").read()
        for x, y, fam, size, bold, anchor, t in parse_texts(src):
            if not t.strip():
                continue
            kind = "serif" if "Serif" in fam else "sans"
            f = svglib._font(kind, bold, int(round(size * 4)))
            adv = f.getlength(t) / 4.0
            if anchor == "start":
                edge = x + adv
            elif anchor == "end":
                edge = x
            else:
                edge = x + adv / 2
            if edge > PAGE or (edge > RIGHT and anchor == "start"):
                print(f"{os.path.basename(path)} y={y} edge={edge:.1f} anchor={anchor}: {t[:60]!r}")
                bad += 1
    print("right-edge violations:", bad)
    return bad


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1]) else 0)
