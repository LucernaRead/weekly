# -*- coding: utf-8 -*-
"""Builder self-checks for W45 zh-tw x FR (not part of the build):
same-baseline ink collisions, chart-label vs later-rect element check,
gloss-call counts, P7 phrase 2x + page tags, image payload identity,
readers'-corner frozen disclosure, Traditional-independence cross-check,
residual-Latin inventory."""
import os, re, sys, json, hashlib, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import text_w

HERE = os.path.dirname(os.path.abspath(__file__))
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-fr/svg")
CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhtw-core/svg")
W43 = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-fr/svg")
PAGES = ["p1-front", "p2-life", "p3-culture", "p4-sport", "p5-youth", "p6-deep", "p7-lang", "p8-test"]

def texts(path):
    src = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"[^>]*?(?: font-weight="700")?[^>]*>([^<]*)</text>', src):
        out.append({"x": float(m.group(1)), "y": float(m.group(2)), "fam": m.group(3),
                    "size": float(m.group(4)), "bold": "700" in m.group(0), "t": m.group(5),
                    "anchor": "middle" if "middle" in m.group(0) else ("end" if "end" in m.group(0) else "start")})
    return src, out

def ink(t):
    # width via svglib text_w with family mapping: TC serif/sans approx by kind
    kind = "serif" if "Serif" in t["fam"] else "sans"
    w = text_w(t["t"], kind, t["bold"], t["size"])
    if t["anchor"] == "middle":
        return (t["x"] - w / 2, t["x"] + w / 2)
    if t["anchor"] == "end":
        return (t["x"] - w, t["x"])
    return (t["x"], t["x"] + w)

print("== 1. same-baseline ink collisions (gap < 2px on same y, same page) ==")
flags = 0
for pg in PAGES:
    _, ts = texts(os.path.join(ED, pg + ".svg"))
    by_y = {}
    for t in ts:
        by_y.setdefault(round(t["y"], 1), []).append(t)
    for y, group in by_y.items():
        group = sorted(group, key=lambda t: ink(t)[0])
        for a, b in zip(group, group[1:]):
            gap = ink(b)[0] - ink(a)[1]
            if gap < 2:
                print(f"  {pg} y={y} gap={gap:.1f} {a['t'][:40]!r} vs {b['t'][:40]!r}")
                flags += 1
print("  flags:", flags)

print("== 2. chart-label element check (P4/P6: label ink vs later-drawn rects) ==")
for pg in ["p4-sport", "p6-deep"]:
    src, ts = texts(os.path.join(ED, pg + ".svg"))
    rects = [(float(a), float(b), float(c), float(d)) for a, b, c, d in
             re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)" fill="#(?:a4553a|3e4c2a)"', src)]
    # order: rects appear in source order; a label is "later-drawn rect covers label" only if rect comes after text in source
    # simpler robust check: any bar rect overlapping any text ink box (x-range + y-range with size band)
    hits = 0
    for t in ts:
        x0, x1 = ink(t)
        y0, y1 = t["y"] - t["size"] * 0.88, t["y"] + t["size"] * 0.30
        for rx, ry, rw, rh in rects:
            if not (x1 < rx or x0 > rx + rw or y1 < ry or y0 > ry + rh):
                # bar labels sit left of bars (x < BX); overlap only counts if text is not the bar's own value label
                if x0 >= rx:
                    print(f"  {pg} OVERLAP {t['t'][:40]!r} with bar at {rx},{ry}")
                    hits += 1
    print(f"  {pg}: bar rects {len(rects)}, overlaps {hits}")

print("== 3. gloss-call counts core vs edition (source grep) ==")
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    c = open(os.path.join(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zhtw-build"), f), encoding="utf-8").read()
    e = open(os.path.join(HERE, f), encoding="utf-8").read()
    for pat in [".gloss(", ".glossline("]:
        print(f"  {f} {pat} core={c.count(pat)} edition={e.count(pat)}")
    # gloss strings containing '·' separators (README #21 split check)
    for src, lab in [(c, "core"), (e, "ed")]:
        for m in re.finditer(r'\.gloss\("([^"]*)"\)', src):
            s = m.group(1)
            if "·" in s:
                print(f"    {lab} gloss with ·: {s[:80]!r} items={len(s.split('·'))}")

print("== 4. P7 phrases: verbatim, exactly 2x, correct page tags ==")
_, p7 = texts(os.path.join(ED, "p7-lang.svg"))
alltext = {}
for pg in PAGES:
    _, ts = texts(os.path.join(ED, pg + ".svg"))
    alltext[pg] = "".join(t["t"] for t in ts)
full = "".join(alltext[p] for p in PAGES)
quotes = [
    ("「用手機轉帳、掃碼付款、網上買保險，都是金融科技」", "p. 1", "p1-front"),
    ("「123個國家及城市、1,600個攤位」", "p. 1", "p1-front"),
    ("「需要才買，不要為了折扣買一堆用不到的東西」", "p. 2", "p2-life"),
    ("「在高雄，鋼鐵也能變成舞台」", "p. 3", "p3-culture"),
    ("「福隆的夏天，在10月26日畫下句點」", "p. 3", "p3-culture"),
    ("「6比0完封兄弟，龍隊拋下紅色彩帶」", "p. 4", "p4-sport"),
    ("「250家店家一起討糖」", "p. 5", "p5-youth"),
    ("「旅展首日中午12點才開門」", "p. 6", "p6-deep"),
]
for q, tag, pg in quotes:
    n = full.count(q)
    onpage = q in alltext[pg]
    print(f"  {q[:22]}... count={n} on-tagged-page={onpage} tag={tag}")

print("== 5. image payloads byte-identical core vs edition ==")
for pg in PAGES:
    cs, es = open(os.path.join(CORE, pg + ".svg"), encoding="utf-8").read(), open(os.path.join(ED, pg + ".svg"), encoding="utf-8").read()
    cp = sorted(re.findall(r'data:image/\w+;base64,([A-Za-z0-9+/=]+)', cs))
    ep = sorted(re.findall(r'data:image/\w+;base64,([A-Za-z0-9+/=]+)', es))
    ch = [hashlib.sha256(base64.b64decode(p)).hexdigest()[:16] for p in cp]
    eh = [hashlib.sha256(base64.b64decode(p)).hexdigest()[:16] for p in ep]
    print(f"  {pg}: core {len(cp)} edition {len(ep)} identical={ch == eh} {ch}")

print("== 6. readers'-corner frozen disclosure intact ==")
_, p7t = texts(os.path.join(ED, "p7-lang.svg"))
joined = "".join(t["t"] for t in p7t)
frozen = "延期披露：VOL.1曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。"
print("  frozen Traditional disclosure present:", frozen in joined)
fr_disc = "Lettre d'exemple"
print("  French disclosure present:", fr_disc in joined, "| invitation 'écrivez-nous' present:", "écrivez-nous" in joined)

print("== 7. Traditional-independence cross-check ==")
def charset(d):
    s = set()
    for pg in PAGES:
        _, ts = texts(os.path.join(d, pg + ".svg"))
        for t in ts:
            for ch in t["t"]:
                if "\u4e00" <= ch <= "\u9fff" or "\u3400" <= ch <= "\u4dbf":
                    s.add(ch)
    return s
ed_cs, core_cs, w43_cs = charset(ED), charset(CORE), charset(W43)
union = core_cs | w43_cs
outside = ed_cs - union
print(f"  edition CJK chars: {len(ed_cs)}, core: {len(core_cs)}, W43: {len(w43_cs)}, outside union: {len(outside)}")
for ch in sorted(outside):
    print(f"    outside: {ch} U+{ord(ch):04X}")
# Simplified-only check: chars in edition not in core multiset that are simplified-only forms
# (approximated: outside-union list above is the gate; also report any Simplified-only char from a small known set)
print("  outside-union count:", len(outside))

print("== 8. residual Latin inventory (edition SVGs, unique strings with A-Z/a-z) ==")
lat = set()
for pg in PAGES:
    _, ts = texts(os.path.join(ED, pg + ".svg"))
    for t in ts:
        if re.search(r"[A-Za-z]", t["t"]):
            lat.add(t["t"])
for s in sorted(lat):
    print(f"  {s[:120]!r}")
print("  unique Latin strings:", len(lat))
