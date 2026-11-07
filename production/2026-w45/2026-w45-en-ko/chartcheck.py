# -*- coding: utf-8 -*-
"""P6 chart-label coverage check (README #12 lesson): the four chart label
lines are plain text; measure each label's true ink box (PIL getbbox at 4x,
baseline-anchored) and its overlap with every LATER-drawn opaque rect.
Report any overlap; gate is <30% (and any >0% is adjudicated by eye)."""
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib

LABELS = ["No lines : 38%", "Work on Tuesday : 29%", "Travel plans : 21%", "Habit : 12%"]


def main(svg_path):
    src = open(svg_path, encoding="utf-8").read()
    # paint-order elements: text and rect in document order
    tokens = re.findall(r"<(text|rect)[^>]*?(?:/>|>([^<]*)</text>)", src)
    # richer parse: walk all tags in order
    events = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"( font-weight="700")?[^>]*>([^<]*)</text>|<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]*)"', src):
        if m.group(1) is not None:
            x, y, fam, size, bold, t = (float(m.group(1)), float(m.group(2)), m.group(3),
                                        float(m.group(4)), bool(m.group(5)), html.unescape(m.group(6)))
            kind = "serif" if "Serif" in fam else "sans"
            f = svglib._font(kind, bold, int(round(size * 4)))
            bb = f.getbbox(t)
            # getbbox is relative to the origin at baseline start; ink box:
            left, top, right, bottom = bb[0] / 4.0, bb[1] / 4.0, bb[2] / 4.0, bb[3] / 4.0
            events.append(("text", (x + left, y + top, x + right, y + bottom), t))
        else:
            x, y, w, h, fill = (float(m.group(7)), float(m.group(8)), float(m.group(9)),
                                float(m.group(10)), m.group(11))
            if fill and fill != "none":
                events.append(("rect", (x, y, x + w, y + h), fill))
    worst = 0.0
    for i, (kind, box, t) in enumerate(events):
        if kind != "text" or t not in LABELS:
            continue
        x0, y0, x1, y1 = box
        area = max(0.0, (x1 - x0) * (y1 - y0))
        for kind2, box2, _ in events[i + 1:]:
            if kind2 != "rect":
                continue
            ox = max(0.0, min(x1, box2[2]) - max(x0, box2[0]))
            oy = max(0.0, min(y1, box2[3]) - max(y0, box2[1]))
            cov = (ox * oy / area * 100) if area else 0.0
            if cov > 0:
                print(f"{t!r} covered {cov:.1f}% by later rect {box2}")
                worst = max(worst, cov)
        print(f"{t!r} ink box {tuple(round(v, 1) for v in box)}")
    print(f"max chart-label coverage: {worst:.1f}% (gate <30%)")
    return worst


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1]) >= 30 else 0)
