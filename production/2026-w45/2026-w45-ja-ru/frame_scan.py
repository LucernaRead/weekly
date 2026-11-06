# -*- coding: utf-8 -*-
"""Full-page frame-line scan (canonical occlusion audit does NOT catch
text ink pressed against / crossing a box border or rule line).
For every page: PIL mask ink box per text node (4x supersampling, JP face)
vs every rect border edge and every line segment in paint order.
Flag = ink box straddles an edge by >0.5px on both sides (touching only
is not a flag). Masthead blackletter skipped (frozen, core-identical).
"""
import html
import os
import re
import sys

from PIL import ImageFont as IF

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ja-ru/svg")
SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
PAGES = ["p1-hyoushi", "p2-kurashi", "p3-bunka", "p4-supotsu",
         "p5-wakamono", "p6-fukayomi", "p7-kotoba", "p8-tesuto"]


def mask_box(txt, size, bold, serif):
    path = SERIF if serif else SANS
    if bold:
        path = path.replace("Regular", "Bold")
    f = IF.truetype(path, int(size * 4), index=0)
    ascent, _ = f.getmetrics()
    mask = f.getmask(txt)
    bb = mask.getbbox()
    if not bb:
        return None
    return (bb[0] / 4, -ascent / 4 + bb[1] / 4, bb[2] / 4, -ascent / 4 + bb[3] / 4)


def main():
    total = 0
    for pg in PAGES:
        s = open(os.path.join(BASE, pg + ".svg"), encoding="utf-8").read()
        edges = []  # (kind, fixed-coord, lo, hi)
        for m in re.finditer(r'<rect([^>]*)/>', s):
            ad = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
            # ONLY stroked boxes count as frames: filled chips (number pills),
            # dark bands and chart bars are backgrounds, and text starting
            # exactly at a chip's right edge is adjacency, not a defect.
            if "stroke" not in ad:
                continue
            x, y = float(ad.get("x", 0)), float(ad.get("y", 0))
            w, h = float(ad.get("width", 0)), float(ad.get("height", 0))
            if w <= 0 or h <= 0:
                continue
            edges.append(("v", x, y, y + h))
            edges.append(("v", x + w, y, y + h))
            edges.append(("h", y, x, x + w))
            edges.append(("h", y + h, x, x + w))
        for m in re.finditer(r'<line([^>]*)/>', s):
            ad = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
            x1, y1 = float(ad.get("x1", 0)), float(ad.get("y1", 0))
            x2, y2 = float(ad.get("x2", 0)), float(ad.get("y2", 0))
            if y1 == y2:
                edges.append(("h", y1, min(x1, x2), max(x1, x2)))
            elif x1 == x2:
                edges.append(("v", x1, min(y1, y2), max(y1, y2)))
        flags = []
        for m in re.finditer(r'<text([^>]*)>(.*?)</text>', s):
            ad = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
            fam = ad.get("font-family", "")
            if "Unifraktur" in fam or "Lucerna" in fam:
                continue
            txt = html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
            if not txt.strip():
                continue
            serif = "Serif" in fam
            bold = ad.get("font-weight") == "bold"
            size = float(ad["font-size"])
            x, y = float(ad["x"]), float(ad["y"])
            anchor = ad.get("text-anchor", "start")
            ib = mask_box(txt, size, bold, serif)
            if not ib:
                continue
            if anchor == "middle":
                x0 = x + ib[0] - (0)  # mask is left-anchored; middle anchor shifts:
                # getmask anchor "la" starts at x; for middle-anchored SVG text
                # the renderer centers the advance width, not the ink box.
                # Approximate: shift by (ink_center - advance_center) unknown;
                # use advance width from mask size as fallback:
                w_adv = IF.truetype((SERIF if serif else SANS).replace("Regular", "Bold") if bold else (SERIF if serif else SANS), int(size * 4), index=0).getlength(txt) / 4
                x0 = x - w_adv / 2 + ib[0]
                x1 = x - w_adv / 2 + ib[2]
            elif anchor == "end":
                w_adv = IF.truetype((SERIF if serif else SANS).replace("Regular", "Bold") if bold else (SERIF if serif else SANS), int(size * 4), index=0).getlength(txt) / 4
                x0 = x - w_adv + ib[0]
                x1 = x - w_adv + ib[2]
            else:
                x0, x1 = x + ib[0], x + ib[2]
            y0, y1 = y + ib[1], y + ib[3]
            for kind, c, lo, hi in edges:
                if kind == "v":
                    if x0 < c - 0.5 and x1 > c + 0.5 and lo < y1 and hi > y0:
                        # ignore the outer page frame (texts never legitimately
                        # cross it, so any hit there is real; keep it)
                        flags.append((round(y, 1), txt[:50], f"v-edge x={c}"))
                else:
                    if y0 < c - 0.5 and y1 > c + 0.5 and lo < x1 and hi > x0:
                        flags.append((round(y, 1), txt[:50], f"h-edge y={c}"))
        print(f"{pg}: {len(flags)} frame flags")
        for f in flags[:20]:
            print("   ", f)
        total += len(flags)
    print("TOTAL frame flags:", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
