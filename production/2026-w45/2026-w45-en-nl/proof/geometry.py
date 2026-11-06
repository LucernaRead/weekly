#!/usr/bin/env python3
import html, os, re, json
from PIL import ImageFont
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-en-nl/svg")
CO = os.path.join(BASE, "files/weekly-report-w45-en-core/svg")
OUT = os.path.join(BASE, "hidden_files/w45/en-nl-proof")
FD = "/usr/share/fonts/opentype/noto"
def sc_index(path):
    for i in range(12):
        try:
            f = ImageFont.truetype(path, 40, index=i)
            if f.getname()[0].endswith("SC"): return i
        except Exception: break
    return 0
SERIF = os.path.join(FD, "NotoSerifCJK-Regular.ttc"); SERIF_B = os.path.join(FD, "NotoSerifCJK-Bold.ttc")
SANS = os.path.join(FD, "NotoSansCJK-Regular.ttc"); SANS_B = os.path.join(FD, "NotoSansCJK-Bold.ttc")
IDX = {p: sc_index(p) for p in (SERIF, SERIF_B, SANS, SANS_B)}
_cache = {}
def font(kind, bold, size, scale=1):
    path = {"serif": SERIF_B if bold else SERIF, "sans": SANS_B if bold else SANS}.get(kind, SANS_B if bold else SANS)
    px = max(1, int(round(size * scale)))
    key = (path, px)
    if key not in _cache: _cache[key] = ImageFont.truetype(path, px, index=IDX[path])
    return _cache[key]
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
def parse(path):
    s = open(path, encoding="utf-8").read()
    texts, rects = [], []
    for m in re.finditer(r"<text([^>]*)>(.*?)</text>", s, re.S):
        a = dict(ATTR_RE.findall(m.group(1)))
        texts.append({"x": float(a.get("x", 0)), "y": float(a.get("y", 0)),
                      "size": float(a.get("font-size", 0)), "fam": a.get("font-family", ""),
                      "bold": a.get("font-weight") == "700", "anchor": a.get("text-anchor", "start"),
                      "text": html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))})
    for m in re.finditer(r"<rect([^>]*)/>", s):
        a = dict(ATTR_RE.findall(m.group(1)))
        try:
            rects.append({"x": float(a.get("x", 0)), "y": float(a.get("y", 0)),
                          "w": float(a.get("width", 0)), "h": float(a.get("height", 0)),
                          "fill": a.get("fill", ""), "stroke": a.get("stroke", "")})
        except ValueError: pass
    return texts, rects
def kind_of(fam): return "serif" if "Serif" in fam else "sans"
def adv(t):
    f = font(kind_of(t["fam"]), t["bold"], t["size"])
    return f.getlength(t["text"])
def adv_span(t):
    a = adv(t)
    if t["anchor"] == "middle": return (t["x"] - a/2, t["x"] + a/2)
    if t["anchor"] == "end": return (t["x"] - a, t["x"])
    return (t["x"], t["x"] + a)
def ink_box(t, scale=4):
    f = font(kind_of(t["fam"]), t["bold"], t["size"], scale=scale)
    advv = f.getlength(t["text"]) / scale
    l, tp, r, b = [v / scale for v in f.getbbox(t["text"])]
    asc = f.getmetrics()[0] / scale
    if t["anchor"] == "middle": left, right = t["x"] - advv/2 + l, t["x"] - advv/2 + r
    elif t["anchor"] == "end": left, right = t["x"] - advv + l, t["x"] - advv + r
    else: left, right = t["x"] + l, t["x"] + r
    return (left, t["y"] - asc + tp, right, t["y"] - asc + b)
PAGES = ["p1-front", "p2-life", "p3-culture", "p4-sport", "p5-jeunesse", "p6-politique", "p7-langue", "p8-exercices"]
print("== Right-edge ADVANCE scan (inner frame right = 1910) ==")
for p in PAGES:
    texts, _ = parse(os.path.join(ED, p + ".svg"))
    bad = [(t["text"][:60], adv_span(t)) for t in texts if adv_span(t)[1] > 1910]
    print(f"{p}: over1910={len(bad)} max_adv_right={max(adv_span(t)[1] for t in texts):.1f}")
    for b in bad: print("   ", b)
print("\n== Frame ink scan (outer frame 28..1922 x 28..2672) ==")
for p in PAGES:
    texts, _ = parse(os.path.join(ED, p + ".svg"))
    bad = []
    for t in texts:
        if not t["text"].strip(): continue
        l, tp, r, b = ink_box(t)
        if l < 28 or r > 1922 or tp < 28 or b > 2672: bad.append((t["text"][:60], (round(l,1), round(tp,1), round(r,1), round(b,1))))
    print(f"{p}: outside={len(bad)}")
    for b in bad: print("   ", b)
print("\n== Same-baseline ink collision scan (same y, overlap >0.5px) ==")
for p in PAGES:
    texts, _ = parse(os.path.join(ED, p + ".svg"))
    by_y = {}
    for t in texts:
        if t["text"].strip(): by_y.setdefault(round(t["y"], 2), []).append(t)
    flags = []
    for y, ts in by_y.items():
        boxes = sorted([(ink_box(t), t) for t in ts], key=lambda x: x[0][0])
        for (b1, t1), (b2, t2) in zip(boxes, boxes[1:]):
            if b2[0] < b1[2] - 0.5: flags.append((y, t1["text"][:50], t2["text"][:50], round(b1[2]-b2[0], 1)))
    print(f"{p}: collisions={len(flags)}")
    for f in flags: print("   ", f)
print("\n== P1 dark-band pair y=478 ==")
texts, _ = parse(os.path.join(ED, "p1-front.svg"))
L = [t for t in texts if t["text"] == "AMERICA VOTES ON TUESDAY — AND THE CLOCKS FELL BACK !"]
R = [t for t in texts if t["text"] == "DINSDAG VERKIEZINGSDAG · KLOK TERUG"]
for l in L:
    for r in R:
        ls, rs = adv_span(l), adv_span(r); li, ri = ink_box(l), ink_box(r)
        print(f"  L adv={ls} ink={tuple(round(v,2) for v in li)}")
        print(f"  R adv={rs} ink={tuple(round(v,2) for v in ri)}")
        print(f"  ADV_GAP={rs[0]-ls[1]:.2f} INK_GAP={ri[0]-li[2]:.2f} (negative=overlap/touch)")
print("\n== R2->R3 final-state checks ==")
texts1, _ = parse(os.path.join(ED, "p1-front.svg"))
for needle in ["Deze week gezocht · Google Trends VS", "Midden van een termijn: tussentijdse verkiezing."]:
    hits=[t for t in texts1 if t["text"]==needle]
    for t in hits: print(f"  P1 {needle!r} ink={tuple(round(v,1) for v in ink_box(t))} adv={tuple(round(v,1) for v in adv_span(t))}")
texts8, _ = parse(os.path.join(ED, "p8-exercices.svg"))
for t in texts8:
    if t["text"].startswith("Levels :"): print(f"  P8 {t['text']!r} y={t['y']} ink={tuple(round(v,1) for v in ink_box(t))}")
print("\n== Shortened box titles (NL) ==")
TITLES = [
    ("p1-front", "THE WEEK IN NUMBERS · Cijfers"),
    ("p4-sport", "SUNDAY, NOVEMBER 8 · Zondag"),
    ("p5-jeunesse", "TOO CLOSE TO CALL · Onbeslist"),
    ("p5-jeunesse", "FIVE SENTENCES · Vijf zinnen"),
    ("p6-politique", "A PRACTICE BALLOT · Stembiljet"),
    ("p6-politique", "READ THE CHART · Grafiek"),
    ("p8-exercices", "D · SENTENCES · Zinnen vormen"),
]
for p, title in TITLES:
    texts, rects = parse(os.path.join(ED, p + ".svg"))
    hits = [t for t in texts if t["text"] == title]
    if not hits: print(f"{p} {title!r}: NOT FOUND"); continue
    for t in hits:
        box = ink_box(t)
        cont = [r for r in rects if r["stroke"] and r["x"] <= box[0] and box[2] <= r["x"]+r["w"] and r["y"] <= box[1] and box[3] <= r["y"]+r["h"]]
        print(f"{p} {title!r}: advance={adv(t):.1f} ink={tuple(round(v,1) for v in box)} containing_bordered={len(cont)}")
print("\n== P6 chart coverage (baseline-anchored ink vs later opaque rects) ==")
for p in PAGES:
    s = open(os.path.join(ED, p + ".svg"), encoding="utf-8").read()
    els = []
    for m in re.finditer(r"<text([^>]*)>(.*?)</text>|<rect([^>]*)/>", s, re.S):
        if m.group(1) is not None:
            a = dict(ATTR_RE.findall(m.group(1)))
            els.append(("text", {"x": float(a.get("x", 0)), "y": float(a.get("y", 0)),
                                 "size": float(a.get("font-size", 0)), "fam": a.get("font-family", ""),
                                 "bold": a.get("font-weight") == "700", "anchor": a.get("text-anchor", "start"),
                                 "text": html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))}))
        else:
            a = dict(ATTR_RE.findall(m.group(3)))
            try: els.append(("rect", {"x": float(a.get("x", 0)), "y": float(a.get("y", 0)),
                                      "w": float(a.get("width", 0)), "h": float(a.get("height", 0)),
                                      "fill": a.get("fill", "")}))
            except ValueError: pass
    maxcov = 0.0; worst = None
    for i, (k, t) in enumerate(els):
        if k != "text" or not t["text"].strip(): continue
        l, tp, r, b = ink_box(t); area = max(0.0, (r-l) * (b-tp))
        if area <= 0: continue
        for k2, rc in els[i+1:]:
            if k2 != "rect" or not rc["fill"] or rc["fill"] == "none": continue
            ix = max(0.0, min(r, rc["x"]+rc["w"]) - max(l, rc["x"])); iy = max(0.0, min(b, rc["y"]+rc["h"]) - max(tp, rc["y"]))
            cov = (ix*iy)/area
            if cov > maxcov: maxcov, worst = cov, (t["text"][:50], rc)
    print(f"{p}: max_coverage={maxcov*100:.1f}% worst={worst}")
print("DONE")
