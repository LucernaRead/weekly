# -*- coding: utf-8 -*-
"""Extra gates for zh-tw x RU (README #10 same-baseline, #12 chart labels).

Same-baseline scan: text nodes sharing a baseline (y within 0.5px) whose
ink boxes are < 4px apart horizontally are flagged (a centred strapline
overprinting a right-hand date would show up here).
Chart-label element check: on P4/P6, any text ink box overlapped by a
later-drawn filled rect is flagged, regardless of coverage percentage.
Ink boxes: PIL FreeType with the TC face (index 3), anchor 'la' corrected
by subtracting the ascent (DE lesson: raw getbbox with 'la' mis-measures
vertical ink).
"""
import os
import re
import sys
from PIL import ImageFont

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-ru")
CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhtw-core")
FONTS = "/usr/share/fonts/opentype/noto"
_cache = {}


def font(kind, bold, size):
    key = (kind, bold, size)
    if key not in _cache:
        path = os.path.join(FONTS, ("NotoSerifCJK-Bold.ttc" if bold else "NotoSerifCJK-Regular.ttc")
                             if kind == "serif" else
                             ("NotoSansCJK-Bold.ttc" if bold else "NotoSansCJK-Regular.ttc"))
        _cache[key] = ImageFont.truetype(path, int(size), index=3)
    return _cache[key]


def parse(path):
    txt = open(path, encoding="utf-8").read()
    texts = []  # (order, x, y, size, kind, bold, text, inkbox)
    rects = []  # (order, x, y, w, h, fill)
    order = 0
    # tokenise top-level elements in paint order: text and rect/image only
    for m in re.finditer(r'<(text|rect|image)\b([^>]*?)(/>|>([^<]*)</text>)', txt):
        tag, attrs = m.group(1), m.group(2)
        order += 1
        if tag == "text":
            def _a(name, default=None):
                mm = re.search(r'\b' + name + r'="([^"]*)"', attrs)
                return mm.group(1) if mm else default
            s = (m.group(4) or "").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
            if not s.strip():
                continue
            x, y = float(_a("x", 0)), float(_a("y", 0))
            size = float(_a("font-size", 20))
            fam = _a("font-family", "")
            kind = "serif" if "Serif" in fam else "sans"
            bold = _a("font-weight") == "700"
            f = font(kind, bold, size)
            # anchor handling: default start; middle/end shift x
            anchor = _a("text-anchor", "start")
            w = f.getlength(s)
            if anchor == "middle":
                x = x - w / 2
            elif anchor == "end":
                x = x - w
            bbox = f.getbbox(s)  # (left, top, right, bottom) with anchor 'la'
            asc, _desc = f.getmetrics()
            ink = (x + bbox[0], y - asc + bbox[1], x + bbox[2], y - asc + bbox[3])
            texts.append((order, x, y, size, kind, bold, s, ink))
        elif tag == "rect":
            def _a(name, default=None):
                mm = re.search(r'\b' + name + r'="([^"]*)"', attrs)
                return mm.group(1) if mm else default
            fill = _a("fill", "none")
            if fill in ("none", None):
                continue
            try:
                rects.append((order, float(_a("x", 0)), float(_a("y", 0)),
                              float(_a("width", 0)), float(_a("height", 0)), fill))
            except (TypeError, ValueError):
                continue
    return texts, rects


def same_baseline(texts):
    flags = []
    by_y = {}
    for t in texts:
        by_y.setdefault(round(t[2] * 2) / 2, []).append(t)
    for y, group in by_y.items():
        group = sorted(group, key=lambda t: t[7][0])
        for a, b in zip(group, group[1:]):
            gap = b[7][0] - a[7][2]
            if gap < 4 and b[7][1] < a[7][3] and a[7][1] < b[7][3]:
                flags.append((y, a[6][:40], b[6][:40], round(gap, 1)))
    return flags


def chart_labels(texts, rects):
    flags = []
    for (o, x, y, size, kind, bold, s, ink) in texts:
        for (ro, rx, ry, rw, rh, fill) in rects:
            if ro <= o:
                continue
            if ink[0] < rx + rw and ink[2] > rx and ink[1] < ry + rh and ink[3] > ry:
                flags.append((s[:40], (rx, ry, rw, rh)))
                break
    return flags


def run(d):
    out = {}
    for name in ["p1-front", "p2-life", "p3-culture", "p4-sport", "p5-youth", "p6-deep", "p7-lang", "p8-test"]:
        texts, rects = parse(os.path.join(d, "svg", name + ".svg"))
        out[name] = (same_baseline(texts), chart_labels(texts, rects) if name in ("p4-sport", "p6-deep") else [])
    return out


if __name__ == "__main__":
    for label, d in [("EDITION", BASE), ("CORE", CORE)]:
        res = run(d)
        tot_sb = sum(len(v[0]) for v in res.values())
        tot_ch = sum(len(v[1]) for v in res.values())
        print(f"{label}: same-baseline flags={tot_sb}, chart-label flags={tot_ch}")
        for k, (sb, ch) in res.items():
            for f in sb:
                print(f"  SB {k}: {f}")
            for f in ch:
                print(f"  CHART {k}: {f}")
