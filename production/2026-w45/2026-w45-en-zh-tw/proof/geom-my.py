# -*- coding: utf-8 -*-
"""Independent geometry re-measurement for W45 EN x ZH-TW (proofreader's own code).
Methods (per tasking): advance-width boxes from PIL getlength on the SVG's own
font/size/weight/anchor; true-ink boxes from PIL getbbox(anchor='ls'); card-pixel
verification on the shipped 1950x2700 cards (1:1 with SVG coordinates).
"""
import re, os, html, sys
from collections import defaultdict
from PIL import ImageFont, Image

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
FONTMAP = {
    ("serif", False): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc", 3),
    ("serif", True): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc", 3),
    ("sans", False): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 3),
    ("sans", True): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 3),
    ("bl", False): ("/home/hatch/.local/share/fonts/UnifrakturMaguntia.ttf", None),
}
_cache = {}
def font(kind, bold, size):
    k = (kind, bold, int(round(size)))
    if k not in _cache:
        p, idx = FONTMAP[(kind, bold)]
        _cache[k] = ImageFont.truetype(p, int(round(size))) if idx is None else ImageFont.truetype(p, int(round(size)), index=idx)
    return _cache[k]

TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"([^>]*)>(.*?)</text>')
RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*/>')

def parse(path):
    s = open(path, encoding="utf-8").read()
    toks = []
    # document order: find all text and rect tags with positions
    events = []
    for m in TEXT_RE.finditer(s):
        events.append((m.start(), "text", m))
    for m in RECT_RE.finditer(s):
        events.append((m.start(), "rect", m))
    for _, kind, m in sorted(events):
        if kind == "text":
            x, y, fam, size, rest, txt = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), m.group(5), html.unescape(re.sub(r"<[^>]+>", "", m.group(6)))
            bold = 'font-weight="700"' in rest
            am = re.search(r'text-anchor="(\w+)"', rest)
            anchor = am.group(1) if am else "start"
            fkind = "serif" if "Serif" in fam else ("bl" if "Unifraktur" in fam else "sans")
            toks.append(("text", x, y, fkind, bold, size, anchor, txt))
        else:
            toks.append(("rect", float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4))))
    return toks

def adv_box(t):
    _, x, y, kind, bold, size, anchor, txt = t
    f = font(kind, bold, size)
    w = f.getlength(txt)
    x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
    asc, desc = f.getmetrics()
    return (x0, y - asc, x0 + w, y + desc)

def ink_box_ls(t):
    _, x, y, kind, bold, size, anchor, txt = t
    f = font(kind, bold, size)
    bb = f.getbbox(txt, anchor="ls")
    w = f.getlength(txt)
    ox = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
    return (ox + bb[0], y + bb[1], ox + bb[2], y + bb[3])

def scan_dir(d):
    collisions, edges, frames = [], [], []
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".svg"): continue
        toks = parse(os.path.join(d, fn))
        texts = [t for t in toks if t[0] == "text"]
        rows = defaultdict(list)
        for t in texts: rows[round(t[2], 1)].append(t)
        for y, ts in rows.items():
            boxes = sorted((adv_box(t), t) for t in ts)
            for (b1, t1), (b2, t2) in zip(boxes, boxes[1:]):
                if b2[0] < b1[2] - 0.5:
                    collisions.append((fn, y, t1[7], b1, t2[7], b2))
        for t in texts:
            b = adv_box(t)
            if b[2] > 1885.5 or b[0] < 64.5:
                edges.append((fn, t[7], b, t[2]))
            if b[2] > 1913.5 or b[0] < 36.5:
                frames.append((fn, t[7], b, t[2]))
    return collisions, edges, frames

for label, d in [("EDITION", f"{BASE}/weekly-report-w45-en-zh-tw/svg"),
                 ("CORE", f"{BASE}/weekly-report-w45-en-core/svg")]:
    c, e, f = scan_dir(d)
    print(f"===== {label} =====")
    print(f"collisions: {len(c)}")
    for fn, y, t1, b1, t2, b2 in c:
        print(f"  COLL {fn} y={y}: {t1[:45]!r} [{b1[0]:.1f},{b1[2]:.1f}] vs {t2[:45]!r} [{b2[0]:.1f},{b2[2]:.1f}]")
    print(f"right-edge advance flags (>1885.5 or <64.5): {len(e)}")
    for fn, t, b, y in e:
        print(f"  EDGE {fn}: {t[:55]!r} adv [{b[0]:.1f},{b[2]:.1f}] baseline y={y}")
    print(f"frame-press flags (>1913.5 or <36.5): {len(f)}")
    for fn, t, b, y in f:
        print(f"  FRAME {fn}: {t[:55]!r} adv [{b[0]:.1f},{b[2]:.1f}]")

# P6 chart-label ink coverage (anchor ls, later rects only), edition + core
for label, d in [("EDITION", f"{BASE}/weekly-report-w45-en-zh-tw/svg"),
                 ("CORE", f"{BASE}/weekly-report-w45-en-core/svg")]:
    toks = parse(os.path.join(d, "p6-politique.svg"))
    texts = [(i, t) for i, t in enumerate(toks) if t[0] == "text"]
    rects = [(i, t) for i, t in enumerate(toks) if t[0] == "rect"]
    worst, worst_t = 0.0, None
    for i, t in texts:
        ib = ink_box_ls(t)
        area = max(0.0, (ib[2] - ib[0]) * (ib[3] - ib[1]))
        if area <= 0: continue
        mx = 0.0
        for j, r in rects:
            if j <= i: continue
            _, rx, ry, rw, rh = r
            ix = max(0.0, min(ib[2], rx + rw) - max(ib[0], rx))
            iy = max(0.0, min(ib[3], ry + rh) - max(ib[1], ry))
            mx = max(mx, (ix * iy) / area)
        if mx > worst: worst, worst_t = mx, (t[7], ib)
    print(f"P6 {label} worst label ink coverage by later rects: {worst*100:.1f}%  label={worst_t} (gate <30%)")
