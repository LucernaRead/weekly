# Round-3 audit (one-off, kept in build dir for the record):
# (1) ADVANCE-method full-page right-edge scan: every <text> element's
# advance box (PIL getlength, correct face/bold/size, anchor-adjusted)
# must end inside the page and inside any bordered rect that contains
# its start point.
# (2) Full-page frame-line scan: every bordered-rect border segment and
# every <line> must not intersect any text's TRUE INK box (PIL getbbox).
# The canonical audit's COVER class misses transparent-fill rect borders
# crossing text (nl-pt B1 lesson); this scan closes that gap.
import glob
import os
import re
import sys

from PIL import ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from svglib import _SERIF, _SERIF_B, _SANS, _SANS_B, _IDX, _IDX_TC

ED = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "files/weekly-report-w45-ja-zh-tw/svg")


def font_for(fam, size, bold):
    serif = "Serif" in fam
    tc = fam.endswith("TC")
    if serif:
        path = _SERIF_B if bold else _SERIF
    else:
        path = _SANS_B if bold else _SANS
    idx = _IDX_TC[path] if tc else _IDX[path]
    return ImageFont.truetype(path, int(round(size)), index=idx)


def parse(svg):
    texts = []
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', svg):
        attrs, s = m.group(1), m.group(2)
        def g(name, default=None):
            mm = re.search(name + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else default
        x = float(g('x', 0)); y = float(g('y', 0))
        size = float(g('font-size', 28))
        fam = g('font-family', 'Noto Serif CJK JP')
        bold = g('font-weight', '') == '700'
        anchor = g('text-anchor', 'start')
        f = font_for(fam, size, bold)
        adv = f.getlength(s)
        bb = f.getbbox(s)  # (l, t, r, b) relative to anchor point baseline
        if anchor == 'middle':
            x0 = x - adv / 2
        elif anchor == 'end':
            x0 = x - adv
        else:
            x0 = x
        # ink box: baseline y, ink top = y + bb[1], bottom = y + bb[3]
        texts.append(dict(s=s, x0=x0, x1=x0 + adv, y=y,
                          ink=(x0 + bb[0], y + bb[1], x0 + bb[2], y + bb[3]),
                          anchor=anchor))
    rects = []
    for m in re.finditer(r'<rect([^>]*)/>', svg):
        attrs = m.group(1)
        def g(name, default=None):
            mm = re.search(name + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else default
        if g('stroke', 'none') == 'none':
            continue
        try:
            rects.append((float(g('x', 0)), float(g('y', 0)),
                          float(g('width', 0)), float(g('height', 0)),
                          float(g('stroke-width', 1))))
        except (TypeError, ValueError):
            continue
    lines = []
    for m in re.finditer(r'<line([^>]*)/>', svg):
        attrs = m.group(1)
        def g(name, default=None):
            mm = re.search(name + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else default
        try:
            lines.append((float(g('x1')), float(g('y1')),
                          float(g('x2')), float(g('y2')),
                          float(g('stroke-width', 1))))
        except (TypeError, ValueError):
            continue
    return texts, rects, lines


def seg_intersects_box(x1, y1, x2, y2, box):
    # segment vs axis-aligned box (inclusive); sampling-free exact test
    bx0, by0, bx1, by1 = box
    if max(x1, x2) < bx0 or min(x1, x2) > bx1:
        return False
    if max(y1, y2) < by0 or min(y1, y2) > by1:
        return False
    if x1 == x2:  # vertical
        return by0 <= max(y1, y2) and by1 >= min(y1, y2) and bx0 <= x1 <= bx1
    if y1 == y2:  # horizontal
        return bx0 <= max(x1, x2) and bx1 >= min(x1, x2) and by0 <= y1 <= by1
    # diagonal: check intersection with each box edge
    def orient(ax, ay, bx, by, cx, cy):
        return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    def on_seg(ax, ay, bx, by, cx, cy):
        return min(ax, cx) <= bx <= max(ax, cx) and min(ay, cy) <= by <= max(ay, cy)
    for (ex1, ey1, ex2, ey2) in [(bx0, by0, bx1, by0), (bx1, by0, bx1, by1),
                                  (bx1, by1, bx0, by1), (bx0, by1, bx0, by0)]:
        d1 = orient(x1, y1, x2, y2, ex1, ey1)
        d2 = orient(x1, y1, x2, y2, ex2, ey2)
        d3 = orient(ex1, ey1, ex2, ey2, x1, y1)
        d4 = orient(ex1, ey1, ex2, ey2, x2, y2)
        if ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0)):
            return True
        if d1 == 0 and on_seg(x1, y1, ex1, ey1, x2, y2):
            return True
    return False


def main():
    total_edge = 0
    total_frame = 0
    for path in sorted(glob.glob(os.path.join(ED, "*.svg"))):
        svg = open(path, encoding="utf-8").read()
        w = re.search(r'width="([\d.]+)"', svg)
        page_w = float(w.group(1)) if w else 1240
        texts, rects, lines = parse(svg)
        for t in texts:
            # (a) page right edge (advance method, 0 tolerance)
            if t['x1'] > page_w + 0.5:
                print(f"EDGE {os.path.basename(path)}: advance-right "
                      f"{t['x1']:.1f} > page {page_w}: {t['s'][:60]!r}")
                total_edge += 1
            # (b) containing bordered rect: text start inside rect and
            # vertical center within rect -> advance must clear rect right
            for (rx, ry, rw, rh, rsw) in rects:
                if rx <= t['x0'] <= rx + rw and ry <= t['y'] <= ry + rh:
                    if t['x1'] > rx + rw - 8:
                        print(f"BOXEDGE {os.path.basename(path)}: advance-right "
                              f"{t['x1']:.1f} > rect right {rx + rw:.1f} "
                              f"(rect x={rx} y={ry} w={rw} h={rh}): "
                              f"{t['s'][:60]!r}")
                        total_edge += 1
        # frame-line scan: rect borders + lines vs ink boxes
        segs = []
        for (rx, ry, rw, rh, rsw) in rects:
            h = rsw / 2
            segs.append((rx, ry, rx + rw, ry, h, 'rect-top'))
            segs.append((rx, ry + rh, rx + rw, ry + rh, h, 'rect-bottom'))
            segs.append((rx, ry, rx, ry + rh, h, 'rect-left'))
            segs.append((rx + rw, ry, rx + rw, ry + rh, h, 'rect-right'))
        for (x1, y1, x2, y2, sw) in lines:
            segs.append((x1, y1, x2, y2, sw / 2, 'line'))
        for (x1, y1, x2, y2, half, kind) in segs:
            # expand segment box by half stroke for the intersection test
            for t in texts:
                ix0, iy0, ix1, iy1 = t['ink']
                # quick reject: ink box vs segment bbox expanded
                if ix1 < min(x1, x2) - half or ix0 > max(x1, x2) + half:
                    continue
                if iy1 < min(y1, y2) - half or iy0 > max(y1, y2) + half:
                    continue
                # exact: does the (thick) segment cross the ink box?
                # approximate thickness by testing the center line against
                # the ink box expanded by half stroke
                exp = (ix0 - half, iy0 - half, ix1 + half, iy1 + half)
                if seg_intersects_box(x1, y1, x2, y2, exp):
                    print(f"FRAME {os.path.basename(path)}: {kind} "
                          f"({x1:.0f},{y1:.0f})-({x2:.0f},{y2:.0f}) crosses "
                          f"ink of {t['s'][:60]!r} ink={tuple(round(v, 1) for v in t['ink'])}")
                    total_frame += 1
    print(f"EDGE violations: {total_edge}; FRAME violations: {total_frame}")


if __name__ == "__main__":
    main()
