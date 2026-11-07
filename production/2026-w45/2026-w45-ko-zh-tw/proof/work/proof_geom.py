# -*- coding: utf-8 -*-
"""Independent geometry supplement for W45 KO x ZH-TW (own ink code).
Methods: (LS) PIL getbbox anchor='ls' native size; (LS4) same at 4x scaled /4;
(DEF) PIL getbbox default anchor (ascender origin) native size -- the
suspected 04:47 phantom method. Writes proof_geom.json + summary."""
import re, os, json, html
from collections import defaultdict
from PIL import ImageFont

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(GOAL, "files/weekly-report-w45-ko-zh-tw/svg")
CORE = os.path.join(GOAL, "files/weekly-report-w45-ko-core/svg")
PAGES = ["p1-pyoji", "p2-saenghwal", "p3-munhwa", "p4-seupocheu",
         "p5-cheongnyeon", "p6-gipi", "p7-mal", "p8-siheom"]
SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SANSB = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SERIFB = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
BLACK = "/home/hatch/.local/share/fonts/UnifrakturMaguntia.ttf"
_cache = {}
def font(fam, size, bold, scale=1):
    if "Unifraktur" in fam:
        key = (BLACK, 0, int(round(size * scale)))
        if key not in _cache: _cache[key] = ImageFont.truetype(BLACK, key[2])
        return _cache[key]
    serif = "Serif" in fam
    path = (SERIFB if bold else SERIF) if serif else (SANSB if bold else SANS)
    # family suffix -> face index; TC=3, KR=1, SC=2
    suf = fam.strip().split()[-1] if fam.strip().split() else "TC"
    idx = {"TC": 3, "KR": 1, "SC": 2, "JP": 0, "HK": 4}.get(suf, 3)
    key = (path, idx, int(round(size * scale)))
    if key not in _cache: _cache[key] = ImageFont.truetype(path, key[2], index=idx)
    return _cache[key]

def parse(path):
    s = open(path, encoding="utf-8").read()
    texts, rects, lines, images = [], [], [], []
    for m in re.finditer(r"<text\s([^>]*)>(.*?)</text>", s, re.S):
        attrs, body = m.group(1), re.sub(r"<[^>]+>", "", m.group(2))
        body = html.unescape(body)
        def g(k):
            mm = re.search(k + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else ""
        texts.append(dict(x=float(g("x") or 0), y=float(g("y") or 0),
                          size=float(g("font-size") or 0), fam=g("font-family"),
                          bold="700" in attrs, anchor=g("text-anchor") or "start",
                          fill=g("fill"), t=body))
    for m in re.finditer(r"<rect\s([^>]*)/>", s):
        attrs = m.group(1)
        def g(k):
            mm = re.search(k + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else ""
        try:
            rects.append(dict(x=float(g("x") or 0), y=float(g("y") or 0),
                              w=float(g("width") or 0), h=float(g("height") or 0),
                              fill=g("fill"), stroke=g("stroke")))
        except ValueError:
            pass
    for m in re.finditer(r"<line\s([^>]*)/>", s):
        attrs = m.group(1)
        def g(k):
            mm = re.search(k + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else ""
        try:
            lines.append(dict(x1=float(g("x1")), y1=float(g("y1")),
                              x2=float(g("x2")), y2=float(g("y2")),
                              sw=float(g("stroke-width") or 1)))
        except ValueError:
            pass
    for m in re.finditer(r"<image\s([^>]*)/>", s):
        attrs = m.group(1)
        def g(k):
            mm = re.search(k + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else ""
        try:
            images.append(dict(x=float(g("x") or 0), y=float(g("y") or 0),
                               w=float(g("width") or 0), h=float(g("height") or 0)))
        except ValueError:
            pass
    return texts, rects, lines, images

def ink(t, method):
    """Return (x0, ytop, x1, ybottom, advance) or None."""
    if not t["t"].strip(): return None
    scale = 4 if method == "LS4" else 1
    f = font(t["fam"], t["size"], t["bold"], scale)
    try:
        if method == "DEF":
            bb = f.getbbox(t["t"])
        else:
            bb = f.getbbox(t["t"], anchor="ls")
        adv = f.getlength(t["t"]) / scale
    except Exception:
        return None
    if t["anchor"] == "middle": x0 = t["x"] - adv / 2
    elif t["anchor"] == "end": x0 = t["x"] - adv
    else: x0 = t["x"]
    return (x0 + bb[0] / scale, t["y"] + bb[1] / scale, x0 + bb[2] / scale, t["y"] + bb[3] / scale, adv)

R = {}
# ADVANCE scan + same-baseline overlap + footer intrusion (LS ink)
adv, overlap, footer = {}, {}, {}
for pg in PAGES:
    texts, _, _, _ = parse(os.path.join(ED, pg + ".svg"))
    worst = 0.0; worst_t = None; n_over_1885 = 0
    for t in texts:
        ib = ink(t, "LS")
        if ib is None: continue
        adv_end = t["x"] + ib[4] if t["anchor"] == "start" else (t["x"] + ib[4] / 2 if t["anchor"] == "middle" else t["x"])
        if adv_end > worst: worst, worst_t = adv_end, t["t"]
        if adv_end > 1885.0: n_over_1885 += 1
    adv[pg] = dict(worst_advance_end=round(worst, 2), worst_text=worst_t, over_1885=n_over_1885)
    # same-baseline groups
    groups = defaultdict(list)
    for t in texts:
        ib = ink(t, "LS")
        if ib: groups[round(t["y"], 2)].append((ib, t["t"]))
    pairs = []
    for y, lst in groups.items():
        lst.sort(key=lambda z: z[0][0])
        for a, b in zip(lst, lst[1:]):
            gap = b[0][0] - a[0][2]
            if gap < 2:
                pairs.append(dict(y=y, a=a[1], b=b[1], gap=round(gap, 2)))
    overlap[pg] = pairs
    foot = []
    for t in texts:
        if t["y"] == 2624.0: continue
        ib = ink(t, "LS")
        if ib and ib[3] > 2580: foot.append(dict(text=t["t"], bottom=round(ib[3], 2)))
    footer[pg] = foot
R["advance"] = adv; R["same_baseline_pairs_gap_lt_2"] = overlap; R["footer_intrusion"] = footer

# P6 label coverage (LS and DEF): labels = all P6 texts; later rects/images in draw order
for method in ("LS", "DEF"):
    texts, rects, lines, images = parse(os.path.join(ED, "p6-gipi.svg"))
    # draw order: need interleaved order -- re-parse raw in document order
    s = open(os.path.join(ED, "p6-gipi.svg"), encoding="utf-8").read()
    items = []  # ('text', t) or ('shape', box)
    for m in re.finditer(r"<text\s([^>]*)>(.*?)</text>|<rect\s([^>]*)/>|<image\s([^>]*)/>", s, re.S):
        if m.group(2) is not None:
            attrs, body = m.group(1), re.sub(r"<[^>]+>", "", m.group(2))
            body = html.unescape(body)
            def g(k, a=attrs):
                mm = re.search(k + r'="([^"]*)"', a); return mm.group(1) if mm else ""
            items.append(("text", dict(x=float(g("x") or 0), y=float(g("y") or 0),
                          size=float(g("font-size") or 0), fam=g("font-family"),
                          bold="700" in attrs, anchor=g("text-anchor") or "start", t=body)))
        else:
            attrs = m.group(3) or m.group(4) or ""
            def g(k, a=attrs):
                mm = re.search(k + r'="([^"]*)"', a); return mm.group(1) if mm else ""
            try:
                items.append(("shape", dict(x=float(g("x") or 0), y=float(g("y") or 0),
                              w=float(g("width") or 0), h=float(g("height") or 0))))
            except ValueError:
                pass
    worst = (0.0, None)
    for i, (kind, t) in enumerate(items):
        if kind != "text": continue
        ib = ink(t, method)
        if ib is None: continue
        area = max(0.0, ib[2] - ib[0]) * max(0.0, ib[3] - ib[1])
        if area <= 0: continue
        covered = 0.0
        for kind2, sh in items[i + 1:]:
            if kind2 != "shape": continue
            ox = max(0.0, min(ib[2], sh["x"] + sh["w"]) - max(ib[0], sh["x"]))
            oy = max(0.0, min(ib[3], sh["y"] + sh["h"]) - max(ib[1], sh["y"]))
            covered += ox * oy
        frac = covered / area
        if frac > worst[0]: worst = (frac, t["t"])
    R.setdefault("p6_coverage", {})[method] = dict(worst_pct=round(worst[0] * 100, 2), worst_text=worst[1], n_labels=len([1 for k, _ in items if k == "text"]))

# P7 readers box / teaser / phrases rule
texts, rects, lines, images = parse(os.path.join(ED, "p7-mal.svg"))
# readers box: rect containing disclosure lines; candidate rects with y near 1230
cands = [r for r in rects if abs(r["y"] - 1230.44) < 2]
R["p7_readers_rects"] = cands
box = cands[0] if cands else None
if box:
    inside = [t for t in texts if box["x"] <= t["x"] < box["x"] + box["w"] and box["y"] <= t["y"] < box["y"] + box["h"]]
    for method in ("LS", "DEF"):
        mx = None; mt = None
        for t in inside:
            ib = ink(t, method)
            if ib and (mx is None or ib[3] > mx): mx, mt = ib[3], t["t"]
        R.setdefault("p7_readers", {})[method] = dict(box_bottom=round(box["y"] + box["h"], 2),
            last_ink=round(mx, 2) if mx else None, last_text=mt,
            air=round(box["y"] + box["h"] - mx, 2) if mx else None)
    # phrases rule: horizontal lines on P7 with y between box bottom and teaser
    R["p7_lines"] = [l for l in lines if 1800 < l["y1"] < 1950]
    R["p7_inside_last_baseline"] = max(t["y"] for t in inside) if inside else None
# teaser band: rects on P7 with bottom near 2461.94, and max rect bottom below 2500
R["p7_rect_bottoms"] = sorted(round(r["y"] + r["h"], 2) for r in rects if r["y"] + r["h"] > 2000)
teaser_texts = [t for t in texts if t["y"] > 2300 and t["y"] < 2540]
R["p7_teaser_texts"] = [(round(t["y"], 2), t["t"]) for t in teaser_texts]

# P8 calibers
texts, rects, lines, images = parse(os.path.join(ED, "p8-siheom.svg"))
keys = [t for t in texts if 1328 <= t["y"] < 2580]
max_base = max(t["y"] for t in keys)
max_base_text = [t["t"] for t in keys if t["y"] == max_base]
# columns by x clusters
xs = sorted(set(round(t["x"], 1) for t in keys))
R["p8_keys_x_clusters"] = xs
last_col_x = max(xs)
last_col = [t for t in keys if round(t["x"], 1) == last_col_x]
last_base = max(t["y"] for t in last_col)
last_base_text = [t["t"] for t in last_col if t["y"] == last_base]
p8 = dict(max_baseline=round(max_base, 2), max_baseline_text=max_base_text,
          last_col_x=last_col_x, last_col_last_baseline=round(last_base, 2), last_col_last_text=last_base_text)
for method in ("LS", "LS4", "DEF"):
    mx = None; mt = None
    for t in keys:
        ib = ink(t, method)
        if ib and (mx is None or ib[3] > mx): mx, mt = ib[3], t["t"]
    p8[f"max_ink_{method}"] = round(mx, 2); p8[f"max_ink_{method}_text"] = mt
    lx = None; lt = None
    for t in last_col:
        ib = ink(t, method)
        if ib and (lx is None or ib[3] > lx): lx, lt = ib[3], t["t"]
    p8[f"last_col_ink_{method}"] = round(lx, 2); p8[f"last_col_ink_{method}_text"] = lt
R["p8"] = p8

# P3 caption geometry: credit lines
for pg in ("p3-munhwa", "p2-saenghwal"):
    texts, rects, lines, images = parse(os.path.join(ED, pg + ".svg"))
    R.setdefault("captions", {})[pg] = [(round(t["x"], 1), round(t["y"], 2), t["size"], t["t"]) for t in texts
        if t["t"].startswith("사진") or t["t"].startswith("그림") or t["t"] == "사진" or "사진이" in t["t"] or "자료 사진" in t["t"]]

outdir = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(outdir, "proof_geom.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(R, ensure_ascii=False, indent=1))
