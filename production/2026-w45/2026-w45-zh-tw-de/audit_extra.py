# -*- coding: utf-8 -*-
"""Extra gates for zh-tw x DE (W45): (a) same-baseline ink-collision scan
(FR x RU lesson: the canonical audit's TEXTX only compares different lines);
(b) chart-label element check (DE x RU lesson: sub-30% bar grazing is invisible
to COVER): any text ink intersecting a LATER-drawn rect on chart pages.
Usage: python3 audit_extra.py <edition_svg_dir> [core_svg_dir]
Fonts: same TTC files + TC face as svglib (NotoSerif/SansCJK, TC index).
Masthead wordmark (UnifrakturMaguntia) skipped: it never shares a baseline.
"""
import sys, os, re
from PIL import ImageFont

FONTS_DIR = "/usr/share/fonts/opentype/noto"


def tc_index(path):
    for i in range(12):
        try:
            f = ImageFont.truetype(path, 40, index=i)
            if f.getname()[0].endswith("TC"):
                return i
        except Exception:
            break
    return 0


_cache = {}


def font(family, bold, size):
    base = {"Noto Serif CJK TC": "NotoSerifCJK-Bold.ttc" if bold else "NotoSerifCJK-Regular.ttc",
            "Noto Sans CJK TC": "NotoSansCJK-Bold.ttc" if bold else "NotoSansCJK-Regular.ttc"}[family]
    key = (base, size)
    if key not in _cache:
        path = os.path.join(FONTS_DIR, base)
        _cache[key] = ImageFont.truetype(path, size, index=tc_index(path))
    return _cache[key]


def parse(path):
    s = open(path, encoding="utf-8").read()
    els = []  # (kind, order, data)
    order = 0
    # tokenise in document order: text, rect, line
    pat = re.compile(r"<text\s+([^>]*)>([^<]*)</text>|<rect\s+([^>]*)/>|<line\s+([^>]*)/>")
    for m in pat.finditer(s):
        if m.group(1) is not None:
            attrs, txt = m.group(1), m.group(2)
            def at(nm, default=None):
                mm = re.search(rf'{nm}="([^"]*)"', attrs)
                return mm.group(1) if mm else default
            els.append(("text", order, {
                "x": float(at("x")), "y": float(at("y")),
                "size": float(at("font-size")), "family": at("font-family"),
                "bold": at("font-weight") == "700",
                "anchor": at("text-anchor", "start"),
                "txt": txt.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")}))
        elif m.group(3) is not None:
            attrs = m.group(3)
            def at(nm, default=None):
                mm = re.search(rf'{nm}="([^"]*)"', attrs)
                return mm.group(1) if mm else default
            try:
                els.append(("rect", order, {
                    "x": float(at("x")), "y": float(at("y")),
                    "w": float(at("width")), "h": float(at("height")),
                    "fill": at("fill", "")}))
            except (TypeError, ValueError):
                pass
        order += 1
    return els


def ink_box(t):
    """True-ink box (left, top, right, bottom) in page coords, or None."""
    if t["family"] not in ("Noto Serif CJK TC", "Noto Sans CJK TC"):
        return None
    f = font(t["family"], t["bold"], t["size"])
    txt = t["txt"]
    try:
        adv = f.getlength(txt)
        bb = f.getbbox(txt)  # PIL default anchor "la": y origin is the ascender top,
        asc, _desc = f.getmetrics()  # so subtract ascent to get baseline-relative ink
    except Exception:
        return None
    if t["anchor"] == "middle":
        left_edge = t["x"] - adv / 2
    elif t["anchor"] == "end":
        left_edge = t["x"] - adv
    else:
        left_edge = t["x"]
    return (left_edge + bb[0], t["y"] + bb[1] - asc, left_edge + bb[2], t["y"] + bb[3] - asc)


def scan(d):
    row_flags, chart_flags = [], []
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".svg"):
            continue
        els = parse(os.path.join(d, fn))
        texts = [(o, t, ink_box(t)) for (k, o, t) in els if k == "text"]
        # (a) same-baseline collisions
        by_y = {}
        for o, t, ib in texts:
            if ib is None:
                continue
            by_y.setdefault(t["y"], []).append((ib, t["txt"]))
        for y, items in by_y.items():
            items.sort(key=lambda z: z[0][0])
            for (ib1, s1), (ib2, s2) in zip(items, items[1:]):
                if ib2[0] < ib1[2] - 0.5:
                    row_flags.append(f"{fn} y={y} overlap {ib1[2]-ib2[0]:.1f}px: {s1[:40]!r} vs {s2[:40]!r}")
        # (b) chart-label: text ink vs any LATER rect (bars etc.), chart pages only
        if fn in ("p4-sport.svg", "p6-deep.svg"):
            rects = [(o, r) for (k, o, r) in els if k == "rect"]
            for o, t, ib in texts:
                if ib is None:
                    continue
                for ro, r in rects:
                    if ro <= o or r["fill"] in ("none", ""):
                        continue
                    if r["w"] <= 0 or r["h"] <= 0:
                        continue
                    ix = min(ib[2], r["x"] + r["w"]) - max(ib[0], r["x"])
                    iy = min(ib[3], r["y"] + r["h"]) - max(ib[1], r["y"])
                    if ix > 0 and iy > 0:
                        chart_flags.append(f"{fn} text {t['txt'][:40]!r} ink intersects later rect "
                                           f"({r['x']:.0f},{r['y']:.0f} {r['w']:.0f}x{r['h']:.0f} fill={r['fill']}) by {ix:.1f}x{iy:.1f}px")
    return row_flags, chart_flags


if __name__ == "__main__":
    for label, d in [("edition", sys.argv[1])] + ([("core", sys.argv[2])] if len(sys.argv) > 2 else []):
        rf, cf = scan(d)
        print(f"{label}: same-baseline flags={len(rf)} chart-label flags={len(cf)}")
        for f in rf + cf:
            print("  FLAG", f)
