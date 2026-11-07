# -*- coding: utf-8 -*-
"""Independent proofreader checks for W45 zh-cn x es. Read-only on delivery/core/W43.
Usage: python myproof.py <base> <proofworkdir>
Writes myproof-report.txt in proofworkdir and prints summary.
"""
import os, re, sys, glob, html, hashlib, base64
from xml.etree import ElementTree as ET
from PIL import ImageFont

B = sys.argv[1]
W = sys.argv[2]
ED = f"{B}/files/weekly-report-w45-zh-cn-es"
CORE = f"{B}/files/weekly-report-w45-zhcn-core"
W43 = f"{B}/files/weekly-report-zh-cn-es"
EDB = f"{B}/hidden_files/weekly-report-w45-zh-cn-es-build"
COB = f"{B}/hidden_files/weekly-report-w45-zhcn-build"
FD = "/usr/share/fonts/opentype/noto"
FONTS = {}
def font(kind, bold, size):
    k = (kind, bold, size)
    if k not in FONTS:
        name = ("NotoSerifCJK-" if kind == "serif" else "NotoSansCJK-") + ("Bold" if bold else "Regular") + ".ttc"
        FONTS[k] = ImageFont.truetype(os.path.join(FD, name), int(round(size)), index=2)
    return FONTS[k]

def all_texts(path):
    """document-order list of (y,x,fs,anchor,family,bold,text, element-index)"""
    t = ET.parse(path); out = []
    for i, el in enumerate(t.iter()):
        if el.tag.endswith("text"):
            out.append(dict(y=float(el.get("y")), x=float(el.get("x")), fs=float(el.get("font-size")),
                            anchor=el.get("text-anchor", "start"), fam=el.get("font-family", ""),
                            bold=(el.get("font-weight") == "700"), s="".join(el.itertext()), idx=i))
    return out

def ink(t):
    """true-ink x-range + y-range (baseline y; PIL bbox top/bottom relative to baseline)."""
    kind = "serif" if "Serif" in t["fam"] else "sans"
    f = font(kind, t["bold"], t["fs"])
    bb = f.getbbox(t["s"])
    w = bb[2] - bb[0]
    if t["anchor"] == "middle": x0 = t["x"] - w / 2 - bb[0]
    elif t["anchor"] == "end": x0 = t["x"] - w - bb[0]
    else: x0 = t["x"] - bb[0]
    # PIL getbbox: top is negative (above baseline), bottom positive below
    return (x0, x0 + w, t["y"] + bb[1], t["y"] + bb[3])

out_lines = []
def log(s=""):
    out_lines.append(s); print(s)

PAGES = ["p1-touiban", "p2-shenghuo", "p3-wenhua", "p4-tiyu", "p5-qingnian", "p6-shendu", "p7-ciyu", "p8-ceyan"]

# ---- 1. same-baseline ink collisions, all pages ----
log("== 1. same-baseline ink collisions (gap<2 flagged; gap<0 = overlap) ==")
tot = 0
for pg in PAGES:
    ts = all_texts(f"{ED}/svg/{pg}.svg")
    by_y = {}
    for t in ts:
        x0, x1, _, _ = ink(t)
        by_y.setdefault(round(t["y"], 1), []).append((x0, x1, t["s"]))
    for y, items in sorted(by_y.items()):
        items.sort()
        for (a0, a1, sa), (b0, b1, sb) in zip(items, items[1:]):
            gap = b0 - a1
            if gap < 2:
                tot += 1
                log(f"  FLAG {pg} y={y} gap={gap:.1f}: {sa[:60]!r} || {sb[:60]!r}")
log(f"  same-baseline flags: {tot}")

# ---- 2. P6 chart-label element coverage vs later-drawn rects ----
log("== 2. P6 chart-label coverage vs later rects (any ink overlap reported) ==")
t = ET.parse(f"{ED}/svg/p6-shendu.svg")
els = list(t.iter())
# collect paint-order elements: rects and texts
seq = []
for el in els:
    if el.tag.endswith("rect"):
        try: seq.append(("rect", float(el.get("x")), float(el.get("y")), float(el.get("width")), float(el.get("height")), el.get("fill")))
        except (TypeError, ValueError): pass
    elif el.tag.endswith("text"):
        d = dict(y=float(el.get("y")), x=float(el.get("x")), fs=float(el.get("font-size")),
                 anchor=el.get("text-anchor", "start"), fam=el.get("font-family", ""),
                 bold=(el.get("font-weight") == "700"), s="".join(el.itertext()))
        x0, x1, y0, y1 = ink(d)
        seq.append(("text", x0, y0, x1, y1, d["s"]))
bars = [s for s in seq if s[0] == "rect" and s[1] == 325.0 and s[3] > 100]
log(f"  bars (x=325,w>100): {[(s[3], s[2]) for s in bars]} expect widths 810/537/480 at y 1282/1340/1398")
# for each text, coverage by any LATER rect
worst = []
for i, s in enumerate(seq):
    if s[0] != "text": continue
    _, x0, y0, x1, y1, txt = s
    area = max(0.0, (x1 - x0) * (y1 - y0))
    if area == 0: continue
    for r in seq[i+1:]:
        if r[0] != "rect": continue
        _, rx, ry, rw, rh, _fill = r
        ox = max(0.0, min(x1, rx + rw) - max(x0, rx)); oy = max(0.0, min(y1, ry + rh) - max(y0, ry))
        if ox > 0 and oy > 0:
            cov = ox * oy / area
            worst.append((cov, txt, (rx, ry, rw, rh)))
worst.sort(reverse=True)
log(f"  texts with ANY later-rect ink overlap: {len(worst)}")
for cov, txt, r in worst[:10]:
    log(f"    cov={cov:.3f} {txt[:70]!r} rect={r}")
# row/value label positions
for s in seq:
    if s[0] == "text" and s[5].strip().endswith("元") and 1200 < s[1] < 1500:
        log(f"  value label {s[5]!r} at x={s[1]:.0f} (bar-end+16 expected 1151/878/821)")

# ---- 3. P8 top rule + flow ends; P7 teaser tail ----
log("== 3. P8 top rule / flow ends; P7 teaser tail ==")
for label, d in [("ED", ED), ("CORE", CORE)]:
    p8 = all_texts(f"{d}/svg/p8-ceyan.svg")
    test = [t for t in p8 if t["y"] < 1264 and t["fs"] in (13.8,)]
    keys = [t for t in p8 if t["y"] >= 1320 and t["fs"] == 13.3]
    # last test-flow node = max y below rule among test-area nodes (exclude headers y<300)
    testflow = [t for t in p8 if 300 < t["y"] < 1264]
    log(f"  {label} P8: max test-flow baseline y={max(t['y'] for t in testflow):.1f} (rule y=1264, builder claim flow ends 1262); "
        f"max keys baseline y={max(t['y'] for t in keys):.2f}; keys nodes={len(keys)}")
    # rule lines
    tt = ET.parse(f"{d}/svg/p8-ceyan.svg")
    for el in tt.iter():
        if el.tag.endswith("line"):
            y1 = el.get("y1"); y2 = el.get("y2")
            if y1 == "1264" or y2 == "1264":
                log(f"  {label} P8 rule line y1={y1} y2={y2} x1={el.get('x1')} x2={el.get('x2')}")
    p7 = all_texts(f"{d}/svg/p7-ciyu.svg")
    content = [t for t in p7 if t["y"] < 2580]
    log(f"  {label} P7: max content baseline y={max(t['y'] for t in content):.1f}; last 3 content nodes:")
    for t in sorted(content, key=lambda z: z["y"])[-3:]:
        log(f"    y={t['y']:.1f} x={t['x']:.0f} {t['s'][:90]!r}")

# ---- 4. gloss counts: source gloss() strings + rendered reconstruction ----
log("== 4. gloss counts (split on '·' itself) ==")
def source_gloss(builddir):
    res = {}
    for f in ["content12.py", "content34.py", "content56.py"]:
        src = open(f"{builddir}/{f}", encoding="utf-8").read()
        strs = re.findall(r'\.gloss\("((?:[^"\\]|\\.)*)"\)', src)
        # gloss() may be called with single-quoted? check also
        res[f] = [len(s.split("·")) for s in strs]
        res[f + "|items"] = [s.split("·") for s in strs]
    return res
cg = source_gloss(COB); eg = source_gloss(EDB)
for f in ["content12.py", "content34.py", "content56.py"]:
    log(f"  {f}: core {cg[f]} edition {eg[f]} equal={cg[f]==eg[f]}")
log(f"  totals core={sum(sum(cg[f]) for f in cg if not f.endswith('|items'))} "
    f"edition={sum(sum(eg[f]) for f in eg if not f.endswith('|items'))}")
# rendered reconstruction: boxes starting with Nota/Notes, fs 20.5, same x, step ~29.7
def rendered_gloss(d, prefix):
    counts = {}
    for pg in PAGES:
        ts = all_texts(f"{d}/svg/{pg}.svg")
        # document order preserved in all_texts
        i = 0; boxes = []
        while i < len(ts):
            t = ts[i]
            if t["s"].startswith(prefix) and t["fs"] == 20.5:
                parts = [t["s"][len(prefix):]]
                x = t["x"]; y = t["y"]; j = i + 1
                while j < len(ts):
                    u = ts[j]
                    if u["fs"] == 20.5 and abs(u["x"] - x) < 1 and abs(u["y"] - (y + 29.725)) < 2:
                        parts.append(u["s"]); y = u["y"]; j += 1
                    else: break
                joined = " ".join(parts)
                boxes.append(len(joined.split("·")))
                i = j
            else: i += 1
        if boxes: counts[pg] = boxes
    return counts
rg_ed = rendered_gloss(ED, "Nota — "); rg_co = rendered_gloss(CORE, "Notes｜")
log(f"  rendered ED: {rg_ed}")
log(f"  rendered CORE: {rg_co}")
log(f"  rendered equal per page: {rg_ed == rg_co}")

# ---- 5. P7 golden sentences ----
log("== 5. P7 golden sentences ==")
phrases = [("不用等11月11日", 1), ("下单就能发货", 2), ("先看结算页，再付款", 2), ("水开始结冰", 3),
           ("三场都输了", 4), ("小局一场没赢", 4), ("故事够不够好", 5), ("别以后，就现在", 5)]
all_ed = {}
for pg in PAGES:
    raw = open(f"{ED}/svg/{pg}.svg", encoding="utf-8").read()
    all_ed[pg] = raw
for ph, pgnum in phrases:
    # count occurrences in raw SVG text (entities: full-width punctuation is literal)
    tot_c = 0; per = {}
    for pg, raw in all_ed.items():
        c = raw.count(ph); per[pg] = c; tot_c += c
    # P7 nodes containing phrase + page tag on same/nearby line
    p7 = all_texts(f"{ED}/svg/p7-ciyu.svg")
    p7hits = [(t["y"], t["s"]) for t in p7 if ph in t["s"]]
    log(f"  「{ph}」 claimed p.{pgnum}: total raw occurrences={tot_c} per-page={per} P7 nodes={p7hits}")

# ---- 6. images ----
log("== 6. images ==")
for label, d in [("ED", ED), ("CORE", CORE)]:
    tot_im = 0
    for pg in PAGES:
        raw = open(f"{d}/svg/{pg}.svg", encoding="utf-8").read()
        imgs = re.findall(r'<image[^>]*>', raw)
        hrefs = re.findall(r'xlink:href="data:image/[^;]+;base64,([^"]+)"', raw)
        h = [hashlib.md5(base64.b64decode(x)).hexdigest()[:12] for x in hrefs]
        tot_im += len(imgs)
        log(f"  {label} {pg}: image elements={len(imgs)} data payloads={len(hrefs)} md5[:12]={h}")
    log(f"  {label} TOTAL images={tot_im}")
# payload identity ED vs CORE per page
for pg in PAGES:
    def payloads(d):
        raw = open(f"{d}/svg/{pg}.svg", encoding="utf-8").read()
        return [hashlib.md5(base64.b64decode(x)).hexdigest() for x in re.findall(r'xlink:href="data:image/[^;]+;base64,([^"]+)"', raw)]
    log(f"  {pg} payloads identical ED==CORE: {payloads(ED)==payloads(CORE)}")
# credit lines
for label, d in [("ED", ED), ("CORE", CORE)]:
    log(f"  {label} credit nodes:")
    for pg in PAGES:
        for t in all_texts(f"{d}/svg/{pg}.svg"):
            if t["s"].startswith("Foto:") or t["s"].startswith("Photo:"):
                log(f"    {pg}: {t['s']!r}")
# CREDITS.md comparison
for label, p in [("ED build", f"{EDB}/assets/CREDITS.md"), ("CORE build", f"{COB}/assets/CREDITS.md")]:
    try:
        txt = open(p, encoding="utf-8").read()
        log(f"  {label} CREDITS.md sha256={hashlib.sha256(txt.encode()).hexdigest()[:16]} len={len(txt)}")
    except Exception as e: log(f"  {label} CREDITS.md ERROR {e}")
# asset payloads vs embedded
log("  asset files vs embedded (ED build assets):")
import glob as _g
for af in sorted(_g.glob(f"{EDB}/assets/*.jpg")) + sorted(_g.glob(f"{EDB}/assets/*.png")):
    data = open(af, "rb").read()
    log(f"    {os.path.basename(af)} bytes={len(data)} md5={hashlib.md5(data).hexdigest()[:12]}")

# ---- 7. readers corner ----
log("== 7. readers corner P7 ==")
for label, d in [("ED", ED), ("CORE", CORE)]:
    p7 = all_texts(f"{d}/svg/p7-ciyu.svg")
    full = " ".join(t["s"] for t in p7)
    log(f"  {label} P7 contains invitation '¡Envíanos tu carta en chino!': {'¡Envíanos tu carta en chino!' in full}")
    log(f"  {label} P7 contains 'Ejemplo de la redacción, no una carta real': {'Ejemplo de la redacción' in full}")
    log(f"  {label} P7 contains 'Aplazado, no cancelado': {'Aplazado, no cancelado' in full}")
    # print corner-region nodes: search for 读者 / corner markers
    for t in p7:
        if "Envíanos" in t["s"] or "Ejemplo de la redacción" in t["s"] or "Aplazado" in t["s"] or "读者园地" in t["s"] or "Readers" in t["s"]:
            log(f"    y={t['y']:.1f} {t['s'][:200]!r}")
# letter identity: nodes in corner region - compare ED vs CORE Chinese letter lines
# heuristic: P7 nodes that are pure/long Chinese and identical in both
ed7 = [t["s"] for t in all_texts(f"{ED}/svg/p7-ciyu.svg")]
co7 = [t["s"] for t in all_texts(f"{CORE}/svg/p7-ciyu.svg")]
log(f"  P7 node multiset: ED {len(ed7)} CORE {len(co7)}; Chinese-letter nodes shared: "
    f"{sum(1 for s in co7 if s in ed7 and any(ch.isalpha() for ch in s))} (of {len(co7)})")

# ---- 8. furniture three-way (all pages footer/page-line) ----
log("== 8. furniture three-way ==")
for label, d in [("ED", ED), ("CORE", CORE), ("W43", W43)]:
    for pg in ["p1-touiban", "p8-ceyan"]:
        ts = all_texts(f"{d}/svg/{pg}.svg")
        foot = [t["s"] for t in ts if abs(t["y"] - 2624) < 1 and t["x"] == 65.0]
        pl = [t["s"] for t in ts if abs(t["y"] - 2624) < 1 and t["anchor"] == "end"]
        log(f"  {label} {pg} footer={foot} pageline={pl}")
    # P1 strap/strapline/top strip: nodes y<434 excluding masthead
    p1 = all_texts(f"{d}/svg/p1-touiban.svg")
    for t in p1:
        if t["y"] < 440 and t["fs"] in (19.5, 20.0, 21.0, 22.0):
            pass
    # print all P1 nodes with y in 300..440
    log(f"  {label} P1 nodes y 300-440:")
    for t in p1:
        if 300 <= t["y"] <= 440:
            log(f"    y={t['y']:.0f} x={t['x']:.0f} fs={t['fs']} anchor={t['anchor']} {t['s'][:130]!r}")
    # gloss prefixes
    prefs = set()
    for pg in PAGES:
        for t in all_texts(f"{d}/svg/{pg}.svg"):
            if t["s"].startswith("Nota") or t["s"].startswith("Notes"):
                prefs.add(t["s"][:8])
    log(f"  {label} gloss prefixes seen: {sorted(prefs)}")

# ---- builder claims spot checks ----
log("== builder-claim spot checks ==")
# P7 B1 glossline
for label, d, needle in [("ED", ED, "el sábado por la tarde, 7 de noviembre"), ("CORE", CORE, "Saturday evening, Nov 7")]:
    hits = []
    for pg in PAGES:
        for t in all_texts(f"{d}/svg/{pg}.svg"):
            if needle in t["s"]: hits.append((pg, t["y"], t["s"][:200]))
    log(f"  {label} glossline needle {needle!r}: {hits}")
    # Chinese result string
    res = [t["s"] for t in all_texts(f"{d}/svg/p7-ciyu.svg") if "11月7日星期六晚上" in t["s"]]
    log(f"  {label} Chinese result nodes: {res}")
# key 150 registry + printed
for label, bd in [("ED", EDB), ("CORE", COB)]:
    src = open(f"{bd}/content8.py", encoding="utf-8").read()
    m = re.findall(r".{0,80}150.{0,120}", src)
    log(f"  {label} content8 lines mentioning 150 (first 5):")
    for x in m[:5]: log(f"    {x!r}")
p8ed = all_texts(f"{ED}/svg/p8-ceyan.svg")
log(f"  ED P8 printed key-150 nodes: {[t['s'] for t in p8ed if t['s'].startswith('150.')]}")
log(f"  ED P8 contains apparatus-as-key '(pregunta abierta': {any('(pregunta abierta' in t['s'] and t['s'].startswith('150.') for t in p8ed)}")
# pinyin notes
log(f"  ED P8 lìdōng notes: {[t['s'] for t in p8ed if 'lìdōng' in t['s']]}")
# English residue: rendered text nodes with ASCII words (excluding proper names/codes)
import re as _re
allowed = set("Lucerna VOL S16 JD Taobao Tmall WeChat Maoyan Sina BO3 AI NBA LPL HLE TES BLG GEN DK KC G2 TL AL TSW MKOI T1 LYON IG CFO LOS TLAW CC0 Wikimedia Commons Foto".split())
for pg in PAGES:
    hits = set()
    for t in all_texts(f"{ED}/svg/{pg}.svg"):
        for w in _re.findall(r"[A-Za-z]+", t["s"]):
            if w not in allowed and len(w) >= 3: hits.add(w)
    log(f"  ED {pg} English-residue words (len>=3, allowlist applied): {sorted(hits) if hits else 'none'}")
# warnings scan in build logs already; also check SVGs for stray quotes / PÁGINA caps
for pg in PAGES:
    raw = open(f"{ED}/svg/{pg}.svg", encoding="utf-8").read()
    if "PÁGINA" in raw: log(f"  ED {pg} contains all-caps PÁGINA (unexpected)")
log("  ED all-caps PÁGINA scan done (no lines above = none)")

with open(f"{W}/myproof-report.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(out_lines) + "\n")
log("WROTE myproof-report.txt")
