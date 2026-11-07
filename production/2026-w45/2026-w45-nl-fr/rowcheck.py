# -*- coding: utf-8 -*-
"""Supplementary scans for the NL x FR W45 build (README #10/#12):
(a) same-baseline text-ink collisions on every page (the canonical audit's
    TEXTX only compares different lines);
(b) P6 chart-label ink vs later-drawn bar rects, coverage % (COVER fires
    only at >=30%; sub-threshold clipping must still be caught);
(c) P1 word-gloss lines vs the full-width rule at y=1853 (W43 NL-FR case:
    the rule may pass only through an inter-line gap, never through ink).
True ink boxes from PIL/FreeType at the production fonts (svglib faces).
"""
import re, sys, os
from PIL import ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-fr/svg")
CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-core/svg")

FD = "/usr/share/fonts/opentype/noto"
FACES = {("serif", False): (os.path.join(FD, "NotoSerifCJK-Regular.ttc"), 2),
         ("serif", True): (os.path.join(FD, "NotoSerifCJK-Bold.ttc"), 2),
         ("sans", False): (os.path.join(FD, "NotoSansCJK-Regular.ttc"), 2),
         ("sans", True): (os.path.join(FD, "NotoSansCJK-Bold.ttc"), 2)}

def font(kind, bold, size):
    path, idx = FACES[(kind, bold)]
    try:
        return ImageFont.truetype(path, int(round(size)), index=idx)
    except Exception:
        return ImageFont.truetype(path, int(round(size)))

def ink(x, y, s, kind, bold, size):
    """Ink box from PIL getbbox (ascender-relative: top = y - ascent)."""
    f = font(kind, bold, size)
    asc, desc = f.getmetrics()
    bbox = f.getbbox(s)
    if bbox is None:
        return None
    # getbbox: (left, top, right, bottom) relative to anchor point at baseline
    # with anchor default 'la' (left-ascender): x0 is left bearing offset.
    left = x + bbox[0]
    top = y - asc + bbox[1]
    right = x + bbox[2]
    bottom = y - asc + bbox[3]
    return (left, top, right, bottom)

TEXT_RE = re.compile(r'<text([^>]*)>(.*?)</text>', re.S)
RECT_RE = re.compile(r'<rect([^>]*)/?>')

def parse_texts(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in TEXT_RE.finditer(s):
        attrs, t = m.group(1), re.sub(r'<[^>]+>', '', m.group(2))
        def g(name, default=None):
            mm = re.search(rf'{name}="([^"]+)"', attrs)
            return mm.group(1) if mm else default
        x = float(g("x", 0)); y = float(g("y", 0))
        size = float(g("font-size", 20))
        fam = g("font-family", "")
        kind = "serif" if "Serif" in fam else "sans"
        bold = g("font-weight") == "700"
        anchor = g("text-anchor", "start")
        # anchor adjustment: middle/end shift the ink box
        f = font(kind, bold, size)
        w = f.getlength(t)
        if anchor == "middle":
            x = x - w / 2
        elif anchor == "end":
            x = x - w
        box = ink(x, y, t, kind, bold, size)
        out.append({"x": x, "y": y, "size": size, "kind": kind, "bold": bold,
                    "text": t, "box": box, "anchor": anchor})
    return out, s

def parse_rects(s):
    out = []
    for m in RECT_RE.finditer(s):
        attrs = m.group(1)
        def g(name, default=0.0):
            mm = re.search(rf'{name}="([^"]+)"', attrs)
            return float(mm.group(1)) if mm else default
        out.append((g("x"), g("y"), g("width"), g("height")))
    return out

def overlap(a, b):
    x0 = max(a[0], b[0]); y0 = max(a[1], b[1])
    x1 = min(a[2], b[2]); y1 = min(a[3], b[3])
    return max(0.0, x1 - x0) * max(0.0, y1 - y0)

print("=== (a) same-baseline collisions ===")
issues = 0
for fn in sorted(os.listdir(ED)):
    if not fn.endswith(".svg"):
        continue
    texts, _ = parse_texts(os.path.join(ED, fn))
    by_base = {}
    for t in texts:
        by_base.setdefault(round(t["y"], 1), []).append(t)
    for base, group in by_base.items():
        group = sorted(group, key=lambda t: t["box"][0])
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                a, b = group[i], group[j]
                if a["box"][2] <= b["box"][0]:
                    continue
                # same baseline + horizontal ink overlap = collision
                # (ignore the giant wordmark: it has no same-baseline neighbour
                #  except furniture at different sizes; report anyway if hit)
                print(f"  COLLIDE {fn} y={base}: {a['text'][:50]!r} vs {b['text'][:50]!r} "
                      f"overlap_x={a['box'][2]-b['box'][0]:.1f}")
                issues += 1
print(f"  same-baseline collisions: {issues}")

print("=== (b) P6 chart labels vs bars ===")
texts, raw = parse_texts(os.path.join(ED, "p6-verdieping.svg"))
# chart bars: olive rects drawn after the labels; identify by paint order:
# collect all rects with fill OLIVE (#3e4c2a) in the chart area (x~1473, y 200-720)
rects = []
for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]+)"', raw):
    x, y, w, h, fill = float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4)), m.group(5)
    if fill == "#3e4c2a" and 1400 < x < 1900 and 200 < y < 750:
        rects.append((x, y, x + w, y + h))
print(f"  chart bars found: {len(rects)}")
labels = [t for t in texts if t["text"] in ("Ik blijf thuis", "Ik kijk eerst naar de tekst",
                                            "Ik ga toch naar buiten", "Ik weet het niet",
                                            "45", "25", "20", "10") and t["x"] > 1400]
for t in labels:
    cov = 0.0
    area = (t["box"][2] - t["box"][0]) * (t["box"][3] - t["box"][1])
    for r in rects:
        cov += overlap(t["box"], r)
    pct = 100.0 * cov / area if area else 0.0
    print(f"  label {t['text']!r}: coverage {pct:.1f}%")
    if pct >= 30:
        print("  !! COVER >= 30%")

print("=== (c) P1 word gloss vs rule y=1853 ===")
texts, _ = parse_texts(os.path.join(ED, "p1-voorpagina.svg"))
for t in texts:
    if t["x"] > 1400 and ("Le climat" in t["text"] or "Semaine du climat, c'est" in t["text"]):
        print(f"  gloss line y={t['y']} ink=({t['box'][1]:.1f}..{t['box'][3]:.1f}) :: {t['text'][:70]}")
        if t["box"][1] < 1853 < t["box"][3]:
            print("  !! RULE CROSSES INK")
print("  (rule at 1853 must fall between the two gloss lines, touching neither)")
