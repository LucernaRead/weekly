# -*- coding: utf-8 -*-
"""Independent ENxFR W45 proof checks (proof-side script, NOT builder code).
Reads only; writes only into this proof dir. Uses tools/occlusion_audit.py
font resolution (canonical) for ink/advance measurement.
"""
import os, re, sys, json, html
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
from PIL import ImageFont

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-en-fr/svg")
CO = os.path.join(BASE, "files/weekly-report-w45-en-core/svg")
W43 = os.path.join(BASE, "files/weekly-report-en-fr/svg")
OUT = os.path.dirname(os.path.abspath(__file__))
CJK = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]")

def texts(path):
    src = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"([^>]*)>(.*?)</text>', src, re.S):
        x, y, fam, size, attrs, raw = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), m.group(5), m.group(6)
        am = re.search(r'text-anchor="(start|middle|end)"', attrs)
        out.append({"x": x, "y": y, "fam": fam, "size": size, "bold": 'font-weight="700"' in attrs or 'font-weight="bold"' in attrs,
                    "anchor": am.group(1) if am else "start", "text": html.unescape(re.sub(r"<[^>]+>", "", raw)), "raw": raw})
    return out

def ink_span(t):
    path, idx = OA.resolve_font(t["fam"], t["size"], t["bold"])
    f = ImageFont.truetype(path, int(round(t["size"] * 4)), index=idx)
    bb = f.getbbox(t["text"]); adv = f.getlength(t["text"]) / 4.0
    l, r = bb[0] / 4.0, bb[2] / 4.0
    if t["anchor"] == "start": return t["x"] + l, t["x"] + r
    if t["anchor"] == "end": return t["x"] - adv + l, t["x"] - adv + r
    return t["x"] - adv / 2 + l, t["x"] - adv / 2 + r

def adv_right(t):
    path, idx = OA.resolve_font(t["fam"], t["size"], t["bold"])
    f = ImageFont.truetype(path, int(round(t["size"] * 4)), index=idx)
    adv = f.getlength(t["text"]) / 4.0
    if t["anchor"] == "start": return t["x"] + adv
    if t["anchor"] == "end": return t["x"]
    return t["x"] + adv / 2

def ink_vspan(t):
    path, idx = OA.resolve_font(t["fam"], t["size"], t["bold"])
    f = ImageFont.truetype(path, int(round(t["size"] * 4)), index=idx)
    bb = f.getbbox(t["text"]); asc, desc = f.getmetrics()
    # getmetrics at 4x scale; baseline-anchored ink top/bottom in svg units
    return t["y"] - asc / 4.0 + bb[1] / 4.0, t["y"] - asc / 4.0 + bb[3] / 4.0

log = open(os.path.join(OUT, "proof_checks.log"), "w", encoding="utf-8")
def p(*a):
    s = " ".join(str(x) for x in a); print(s); log.write(s + "\n")

# ---- 1. freeze removed non-CJK classification (from my own freeze-diff.json) ----
fd = json.load(open(os.path.join(OUT, "freeze-diff.json"), encoding="utf-8"))
p("== 1. freeze diff removed strings WITHOUT any CJK char ==")
for pg in sorted(fd["pages"], key=int):
    rem = fd["pages"][pg]["removed_strings"]
    pure = [r for r in rem if not CJK.search(r["text"])]
    p(f"p{pg}: removed total {sum(r['count'] for r in rem)}, pure-non-CJK {sum(r['count'] for r in pure)}")
    for r in pure: p(f"   - x{r['count']} {r['text']!r}")
    p(f"   added CJK={fd['pages'][pg]['cjk_added']}, edition CJK total={fd['pages'][pg]['cjk_edition_total']}")

# ---- 2. rendered gloss boxes per page (SVG texts starting 'Note | ') ----
p("\n== 2. rendered gloss boxes: texts containing 'Note | ', items split on '·' ==")
for d, name in [(ED, "FR"), (CO, "CORE")]:
    tot = 0
    for fn in sorted(os.listdir(d)):
        ts = [t for t in texts(os.path.join(d, fn)) if "Note | " in t["text"] or t["text"].startswith("Note |")]
        # core uses Chinese prefix; count separately below
        items = []
        for t in ts:
            s = t["text"].split("Note | ", 1)[-1] if "Note | " in t["text"] else t["text"]
            items += [x.strip() for x in s.split("·") if x.strip()]
        tot += len(items)
        if name == "FR": p(f"  {name} {fn}: gloss-box texts={len(ts)} items={len(items)}")
    p(f"  {name} total rendered Note|-box items: {tot}")
# core gloss boxes use Chinese prefix char: find texts with that prefix
p("  CORE gloss-prefix texts (contain Chinese gloss marker):")
for fn in sorted(os.listdir(CO)):
    ts = [t for t in texts(os.path.join(CO, fn)) if "译注" in t["text"] or "讲解" in t["text"]]
    for t in ts: p(f"    {fn} y={t['y']} {t['text'][:120]!r}")

# ---- 3. P7 golden + definitions ----
p("\n== 3. P7 verbatim checks ==")
gold = ["Tuesday, November 3, is Election Day in the United States.", "The hour from 1 to 2 happened twice.",
        "Which film would you choose ?", "Two games, two continents, one league — that is the modern NFL.",
        "The results will still be there in the morning.", "Patience is part of the system, not a failure of it.",
        "Not every place changes.", "One Sunday is not enough — good thing the week has seven days."]
defs = ["The clocks fell back.", "She is going to vote on Tuesday.", "The Bernabéu is bigger than most stadiums.",
        "Nobody knows whether the race is called yet."]
for label, sents in [("golden", gold), ("definition", defs)]:
    for s in sents:
        cc = sum(1 for t in texts(os.path.join(CO, "p7-langue.svg")) if s in t["text"])
        fc = sum(1 for t in texts(os.path.join(ED, "p7-langue.svg")) if s in t["text"])
        p(f"  {label} core_occ={cc} fr_occ={fc} :: {s!r}")
p("  P7 headings FR:")
for t in texts(os.path.join(ED, "p7-langue.svg")):
    if t["size"] >= 30 and t["y"] < 600 or "LEVEL" in t["text"] or "TOOLBOX" in t["text"] or "PHRASES" in t["text"] or "CLINIC" in t["text"] or "READERS" in t["text"] or "NEXT WEEK" in t["text"] or "LANGUAGE IN HAND" in t["text"]:
        p(f"    y={t['y']} size={t['size']} {t['text'][:100]!r}")
p("  P7 headings W43 (same strings expected):")
for t in texts(os.path.join(W43, "p7-langue.svg")):
    if "LEVEL" in t["text"] or "TOOLBOX" in t["text"] or "PHRASES" in t["text"] or "CLINIC" in t["text"] or "READERS" in t["text"] or "NEXT WEEK" in t["text"] or "LANGUAGE IN HAND" in t["text"]:
        p(f"    y={t['y']} size={t['size']} {t['text'][:100]!r}")

# ---- 4. readers corner ----
p("\n== 4. readers corner ==")
for d, name in [(CO, "CORE"), (ED, "FR")]:
    p(f"  --- {name} P7 texts mentioning reader/Chicago/M. L./Envoyez/lettres ---")
    for t in texts(os.path.join(d, "p7-langue.svg")):
        if any(k in t["text"] for k in ["M. L.", "Chicago", "slept one hour", "Envoyez", "lettres", "paraîtront", "arriv", "exemple", "example", "VOL.3", "meilleur"]):
            p(f"    y={t['y']} {t['text']!r}")

# ---- 5. P8 keys via p8 extract jsons (produced separately) + note scan ----
p("\n== 5. P8 extracts ==")
for name in ["p8-core", "p8-ed"]:
    j = json.load(open(os.path.join(OUT, f"{name}.json"), encoding="utf-8"))
    p(f"  {name}: keys={list(j.keys())[:5]}... (full json in file)")
    # p8.py extract json format inspected at runtime; print top-level keys
    p(f"    top keys: {list(j.keys())}")
frp8 = open(os.path.join(ED, "p8-exercices.svg"), encoding="utf-8").read()
p(f"  FR P8 contains '(ID)' substring: {'(ID)' in frp8}; contains 'pièce d'identité': {'pièce d’identité' in html.unescape(frp8) or chr(39) in frp8}")
for t in texts(os.path.join(ED, "p8-exercices.svg")):
    if "identité" in t["text"] or "ID" in t["text"] and "145" in t["text"]: p(f"    FR P8 identity line y={t['y']} {t['text']!r}")
p("  FR P8 font sizes in ANSWERS region (y>1600):")
from collections import Counter
c = Counter(t["size"] for t in texts(os.path.join(ED, "p8-exercices.svg")) if t["y"] > 1600)
p(f"    {dict(c)}")
p("  FR P8 key-flow max baseline (texts with size 13.5):")
ts135 = [t for t in texts(os.path.join(ED, "p8-exercices.svg")) if t["size"] == 13.5]
p(f"    count={len(ts135)} max y={max(t['y'] for t in ts135)} (KIT claims flow bottom 2530)")
p("  W43 P8 key-flow max baseline (size 13.5):")
ts135w = [t for t in texts(os.path.join(W43, "p8-exercices.svg")) if t["size"] == 13.5]
p(f"    count={len(ts135w)} max y={max(t['y'] for t in ts135w) if ts135w else None}")

# ---- 6. translation premise: core P8 exercise prompts 137-140 ----
p("\n== 6. core P8 translation prompts (rendered SVG text search) ==")
for s in ["Patience is part of the system, not a failure of it.", "Tuesday, November 3, is Election Day in the United States.",
          "Not every place changes."]:
    for d, name in [(CO, "CORE-P8"), (ED, "FR-P8")]:
        hits = [(t["y"], t["text"]) for t in texts(os.path.join(d, "p8-exercices.svg")) if s in t["text"]]
        p(f"  {name} {s[:40]!r}: {hits}")
p("  CORE P8 texts containing 'Translate' or Chinese translate word:")
for t in texts(os.path.join(CO, "p8-exercices.svg")):
    if "Translate" in t["text"] or "翻译" in t["text"]: p(f"    y={t['y']} {t['text']!r}")
p("  FR P8 texts containing 'Translate':")
for t in texts(os.path.join(ED, "p8-exercices.svg")):
    if "Translate" in t["text"]: p(f"    y={t['y']} {t['text']!r}")
p("  CORE P8 NFL-Madrid sentence search (139 prompt candidate):")
for t in texts(os.path.join(CO, "p8-exercices.svg")):
    if "Madrid" in t["text"]: p(f"    y={t['y']} {t['text']!r}")
p("  FR P8 NFL-Madrid sentence search:")
for t in texts(os.path.join(ED, "p8-exercices.svg")):
    if "Madrid" in t["text"]: p(f"    y={t['y']} {t['text']!r}")

# ---- 7. images + credits ----
p("\n== 7. image payload per page (href,x,y,w,h) core vs FR ==")
def images(path):
    src = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"<image[^>]*>", src):
        tag = m.group(0)
        def attr(a):
            mm = re.search(rf'{a}="([^"]*)"', tag); return mm.group(1) if mm else ""
        out.append((attr("xlink:href") or attr("href"), attr("x"), attr("y"), attr("width"), attr("height")))
    return out
for fn in sorted(os.listdir(ED)):
    ci, fi = images(os.path.join(CO, fn)), images(os.path.join(ED, fn))
    p(f"  {fn}: core {len(ci)} FR {len(fi)} equal={ci == fi}")
    if ci != fi:
        p(f"    core={ci}"); p(f"    fr={fi}")
p("  credit-ish lines FR (©/Source/Crédit/Wikimedia/Commons):")
for fn in sorted(os.listdir(ED)):
    for t in texts(os.path.join(ED, fn)):
        if any(k in t["text"] for k in ["©", "Source", "Crédit", "Wikimedia", "Commons", "Manet", "Library"]):
            p(f"    {fn} y={t['y']} {t['text'][:150]!r}")

# ---- 8. geometry: same-baseline furniture ink gaps, right-edge ADVANCE, P6 chart ----
p("\n== 8a. same-baseline furniture bands, INK spans (occlusion font resolution) ==")
for fn in sorted(os.listdir(ED)):
    ts = texts(os.path.join(ED, fn))
    by_y = {}
    for t in ts: by_y.setdefault(round(t["y"]), []).append(t)
    for y, els in sorted(by_y.items()):
        if y not in (92, 116, 142, 478, 522, 2624) or len(els) < 2: continue
        spans = sorted((ink_span(t) + (t["text"][:40],)) for t in els)
        for (l1, r1, t1), (l2, r2, t2) in zip(spans, spans[1:]):
            gap = l2 - r1
            if gap < 40: p(f"  {fn} y={y} ink_gap={gap:.1f} :: {t1!r} || {t2!r}")
p("  (only ink gaps < 40px listed)")
p("\n== 8b. right-edge ADVANCE scan FR ==")
for fn in sorted(os.listdir(ED)):
    for t in texts(os.path.join(ED, fn)):
        r = adv_right(t)
        if r > 1885: p(f"  {fn} y={t['y']} adv_right={r:.1f} {'OVER-1910!' if r > 1910 else ''} :: {t['text'][:60]!r}")
p("  core counterparts of FR >1885 lines:")
for fn in sorted(os.listdir(ED)):
    fr_over = [(t["y"], t["text"]) for t in texts(os.path.join(ED, fn)) if adv_right(t) > 1885]
    for y, tx in fr_over:
        for t in texts(os.path.join(CO, fn)):
            if t["text"] == tx: p(f"    {fn} FR y={y} core y={t['y']} x core={t['x']} :: {tx[:60]!r}")
p("\n== 8c. P6 chart labels baseline-anchored ink vs later rects ==")
import xml.etree.ElementTree as ET
NS = "{http://www.w3.org/2000/svg}"
tree = ET.parse(os.path.join(ED, "p6-politique.svg")); root = tree.getroot(); elems = list(root.iter())
labels = ["No lines : 38%", "Work on Tuesday : 29%", "Travel plans : 21%", "Habit : 12%"]
for i, el in enumerate(elems):
    if el.tag == NS + "text" and "".join(el.itertext()).strip() in labels:
        lab = "".join(el.itertext()).strip(); y = float(el.get("y")); x = float(el.get("x")); size = float(el.get("font-size", 22))
        path, idx = OA.resolve_font(el.get("font-family", ""), size, el.get("font-weight") in ("700", "bold"))
        f = ImageFont.truetype(path, int(round(size * 4)), index=idx)
        asc, desc = f.getmetrics(); bb = f.getbbox(lab)
        top, bot = y - asc / 4.0 + bb[1] / 4.0, y - asc / 4.0 + bb[3] / 4.0
        w = f.getlength(lab) / 4.0; cover = 0.0
        for el2 in elems[i + 1:]:
            if el2.tag == NS + "rect" and el2.get("fill") not in (None, "none"):
                rx, ry, rw, rh = float(el2.get("x", 0)), float(el2.get("y", 0)), float(el2.get("width", 0)), float(el2.get("height", 0))
                ox = max(0, min(x + w, rx + rw) - max(x, rx)); oy = max(0, min(bot, ry + rh) - max(top, ry))
                cover = max(cover, ox * oy / max(1, w * (bot - top)))
        p(f"  {lab!r} baseline={y} ink=({top:.1f},{bot:.1f}) coverage={cover*100:.1f}% {'PASS <30%' if cover < 0.30 else 'FAIL'}")
p("\n== 8d. tight points: P8 Levels line + writing rule; P1/P2 section ends ==")
for t in texts(os.path.join(ED, "p8-exercices.svg")):
    if "Levels" in t["text"] or "Niveaux" in t["text"]: p(f"  FR P8 levels-line y={t['y']} {t['text']!r}")
src8 = open(os.path.join(ED, "p8-exercices.svg"), encoding="utf-8").read()
for m in re.finditer(r'<line[^>]*y1="([\d.]+)"[^>]*>', src8):
    if abs(float(m.group(1)) - 1486) < 3: p(f"  FR P8 line at y1={m.group(1)}: {m.group(0)[:200]}")
# P1 headline / P2 ex: report max baseline among texts in upper/mid regions as proxies + footer-exempt max
for fn, note in [("p1-front.svg", "P1"), ("p2-life.svg", "P2")]:
    ts = [t for t in texts(os.path.join(ED, fn)) if t["y"] < 2580]
    p(f"  {note} max non-footer baseline={max(t['y'] for t in ts)}; texts near max: {[(t['y'], t['text'][:40]) for t in ts if t['y'] > max(t2['y'] for t2 in ts) - 60][:6]}")
log.close()
print("DONE")
