#!/usr/bin/env python3
"""Independent PTxES W45 proof checks. READ-ONLY on delivery/core/W43 dirs.
Writes only to this proof dir (stdout redirected by caller)."""
import re, os, sys, json, hashlib
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA

B = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = f"{B}/files/weekly-report-w45-pt-es"
CO = f"{B}/files/weekly-report-w45-pt-core"
W43 = f"{B}/files/weekly-report-pt-es"
EDB = f"{B}/hidden_files/weekly-report-w45-pt-es-build"
COB = f"{B}/hidden_files/weekly-report-w45-pt-build"
PAGES = ["p1-capa","p2-vida","p3-cultura","p4-esporte","p5-jovens","p6-aprofundamento","p7-lingua","p8-avaliacao"]
CJK = re.compile(r"[\u3400-\u9fff\uf900-\ufaff\u3040-\u30ff\uac00-\ud7af]")

def texts(d, p):
    s = open(f"{d}/svg/{p}.svg", encoding="utf-8").read()
    els, _, _ = OA.parse_svg(s)
    out = []
    for el in els:
        if el.kind == "text":
            a = el.attrs
            out.append(dict(x=float(a.get("x", 0)), y=float(a.get("y", 0)),
                            size=float(a.get("font-size", 20)), fam=a.get("font-family",""),
                            bold=a.get("font-weight","") in ("700","bold"),
                            anchor=a.get("text-anchor","start"), t=el.text or "",
                            box=el.box))
    return out, els

def adv_right(t):
    f = OA.get_font(t["fam"], t["size"], t["bold"])
    adv = f.getlength(t["t"]) / OA.SCALE
    if t["anchor"] == "middle": return t["x"] + adv/2
    if t["anchor"] == "end": return t["x"]
    return t["x"] + adv

print("== A. CJK residue + bridge term per edition page ==")
for p in PAGES:
    ts, _ = texts(ED, p)
    all_t = "".join(x["t"] for x in ts)
    print(f"{p}: CJK={len(CJK.findall(all_t))} bridge={'桥接' in all_t}")

print("\n== B. Furniture presence per page (edition) ==")
for p in PAGES:
    ts, _ = texts(ED, p)
    all_t = "\n".join(x["t"] for x in ts)
    foot = "A Lucerna · SEMANARIO PORTUGUÉS VOL.2 · TEXTO EN PORTUGUÉS · EXPLICACIONES EN ESPAÑOL" in all_t
    pg = f"Página {PAGES.index(p)+1} de 8" in all_t
    print(f"{p}: footer={foot} pageline={pg}")

print("\n== C. Expansion: chips -> numbers per page ==")
tot = {}
for p in PAGES:
    ts, _ = texts(ED, p)
    chips = [x for x in ts if x["anchor"] == "middle" and x["t"] in ("A2","B1","B2")]
    nums = []
    for c in chips:
        cand = [x for x in ts if re.fullmatch(r"\d+\.", x["t"].strip()) and abs(x["y"]-c["y"]) < 4 and 0 < x["x"]-c["x"] < 70]
        if cand:
            n = int(cand[0]["t"].strip().rstrip("."))
            nums.append((n, c["t"]))
    nums.sort()
    tot[p] = nums
    print(f"{p}: n={len(nums)} levels A2={sum(1 for _,l in nums if l=='A2')} B1={sum(1 for _,l in nums if l=='B1')} B2={sum(1 for _,l in nums if l=='B2')} range={nums[0][0] if nums else None}-{nums[-1][0] if nums else None}")
alln = [(n, l) for v in tot.values() for n, l in v]
print(f"TOTAL n={len(alln)} union1..150={sorted(n for n,_ in alln)==list(range(1,151))} levels A2={sum(1 for _,l in alln if l=='A2')} B1={sum(1 for _,l in alln if l=='B1')} B2={sum(1 for _,l in alln if l=='B2')}")

print("\n== D. P8 answer-start counts by exercise page-range (from expansion ranges) ==")
ts8, _ = texts(ED, "p8-avaliacao")
starts = {}
for x in ts8:
    m = re.match(r"(\d+)\.\s", x["t"].strip())
    if m: starts[int(m.group(1))] = x["t"]
ranges = [(1,10),(11,28),(29,46),(47,64),(65,82),(83,100),(101,112),(113,150)]
for i,(a,b) in enumerate(ranges):
    print(f"page {i+1} ({a}-{b}): {sum(1 for n in starts if a<=n<=b)}")
print(f"P8 answer starts total={len(starts)} union={sorted(starts)==list(range(1,151))}")

print("\n== E. P8 keydiff items: printed full lines (joined wrap continuations by column x) ==")
def p8_lines(d):
    ts, _ = texts(d, "p8-avaliacao")
    # group nodes by (column x, y-cluster): answer lines start at x in {65,527,989,1451}
    nodes = sorted(ts, key=lambda z:(z["y"], z["x"]))
    return nodes
for d, label in [(CO,"CORE"), (ED,"ED")]:
    nodes = p8_lines(d)
    print(f"-- {label}")
    for want in (2,4,101,137,138,146,139,140):
        # find start node
        st = [x for x in nodes if re.match(rf"{want}\.\s", x["t"].strip())]
        if not st: print(f"  {want}: NOT FOUND"); continue
        s0 = st[0]
        # continuation: same column x, next y within ~30 and not a new numbered item
        cont = [x for x in nodes if x["x"]==s0["x"] and 0 < x["y"]-s0["y"] < 30 and not re.match(r"\d+\.\s", x["t"].strip()) and "PÁGINA" not in x["t"]]
        line = s0["t"] + (" " + " ".join(c["t"] for c in sorted(cont, key=lambda z:z["y"])) if cont else "")
        key = re.match(r"\d+\.\s*(.*?)\s+—\s", line)
        print(f"  {want}: key={key.group(1)!r} full={line!r}")

print("\n== F. P8 last baseline / footer rule ==")
ts8, _t8 = texts(ED, "p8-avaliacao")
nonfoot = [x for x in ts8 if x["y"] < 2600]
print(f"max non-footer baseline={max(x['y'] for x in nonfoot)} (flow bottom 2552, footer rule 2580)")
els8, _, _ = OA.parse_svg(open(f"{ED}/svg/p8-avaliacao.svg", encoding="utf-8").read())
rules = [(e.attrs.get('y1'), e.attrs.get('x1'), e.attrs.get('x2')) for e in els8 if e.kind=="line" and e.attrs.get('y1')=='2580']
print(f"footer rule lines at y=2580: {rules}")

print("\n== G. P1 edition-line + badge widths (Serif/Sans Bold, SC face) ==")
from PIL import ImageFont
def width(text, serif, size, bold):
    path, idx = OA.resolve_font("Noto Serif CJK SC" if serif else "Noto Sans CJK SC", size, bold)
    f = ImageFont.truetype(path, size, index=idx)
    return f.getlength(text)
edline = "SEMANARIO EN PORTUGUÉS · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE"
badge = "TEXTOS EN PORTUGUÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES"
print(f"edition line 38pt serif-bold = {width(edline, True, 38, True):.1f} px; 40pt = {width(edline, True, 40, True):.1f} px; limit 1820")
print(f"badge 19pt sans-bold = {width(badge, False, 19, True):.1f} px")
# verify strings actually on P1
ts1, _ = texts(ED, "p1-capa")
joined1 = " ".join(x["t"] for x in ts1)
print(f"P1 edition line present={edline in joined1}; badge present={badge in joined1}")
for x in ts1:
    if x["t"].startswith("SEMANARIO EN PORTUGUÉS"): print(f"  edition line node: size={x['size']} bold={x['bold']} y={x['y']}")
    if x["t"].startswith("TEXTOS EN PORTUGUÉS"): print(f"  badge node: size={x['size']} bold={x['bold']} y={x['y']} fill? (see svg)")

print("\n== H. Same-baseline ink collisions (decoded ink, all pages) ==")
for p in PAGES:
    ts, _ = texts(ED, p)
    by_y = {}
    for x in ts:
        by_y.setdefault(round(x["y"],3), []).append(x)
    flags = []
    for y, group in by_y.items():
        if len(group) < 2: continue
        group = sorted(group, key=lambda z: (z["box"][0] if z["box"] else z["x"]))
        for a, b in zip(group, group[1:]):
            if a["box"] and b["box"] and b["box"][0] < a["box"][2] - 0.01:
                flags.append((y, a["t"][:40], b["t"][:40], round(b["box"][0]-a["box"][2],2)))
    print(f"{p}: same-baseline flags={len(flags)} {flags[:5]}")

print("\n== I. Right-edge ADVANCE + ink margins per page ==")
for p in PAGES:
    ts, _ = texts(ED, p)
    advmax = max(adv_right(x) for x in ts)
    ink = [x["box"] for x in ts if x["box"]]
    print(f"{p}: max advance-right={advmax:.1f} (>1910: {sum(1 for x in ts if adv_right(x)>1910)}; >1922: {sum(1 for x in ts if adv_right(x)>1922)}) "
          f"ink L={min(b[0] for b in ink):.1f} R={max(b[2] for b in ink):.1f} T={min(b[1] for b in ink):.1f} B={max(b[3] for b in ink if True):.1f}")

print("\n== J. P6 chart-label baseline-anchored ink vs later rects ==")
els6, _, _ = OA.parse_svg(open(f"{ED}/svg/p6-aprofundamento.svg", encoding="utf-8").read())
labels = ["prova","portões abertos","60 min","espera","30 min","330 min"]
for el in els6:
    if el.kind=="text" and el.text and el.text.strip() in labels:
        # later-drawn opaque rects
        later = [e for e in els6[el.idx+1:] if e.kind=="rect" and OA.is_opaque(e)]
        covs = []
        for r in later:
            rb = OA.shape_box(r)
            if rb:
                ov = OA.overlap(el.box, rb)
                if ov[0]: covs.append((round(ov[0],1), r.attrs))
        print(f"label {el.text!r} y={el.baseline} ink={tuple(round(v,1) for v in el.box)} later-rect overlaps={covs}")

print("\n== K. P7 word-box geometry ==")
ts7, _ = texts(ED, "p7-lingua"); els7, _, _ = OA.parse_svg(open(f"{ED}/svg/p7-lingua.svg", encoding="utf-8").read())
for e in els7:
    if e.kind=="rect":
        x, y, w, h = OA.fnum(e.attrs,"x"), OA.fnum(e.attrs,"y"), OA.fnum(e.attrs,"width"), OA.fnum(e.attrs,"height")
        if x > 1400 and 1050 < y < 1350 and w > 300:
            print(f"rect x={x} y={y} w={w} h={h} bottom={y+h}")
gloss = [x for x in ts7 if x["t"].strip()=="feriadão = el puente festivo."]
print(f"gloss node: {[(x['y'], tuple(round(v,1) for v in x['box'])) for x in gloss]}")
prev = [e for e in els7 if e.kind=="rect" and OA.fnum(e.attrs,"y") in (2404.0,) or (e.kind=="rect" and 2395 < OA.fnum(e.attrs,"y") < 2415)]
print(f"preview-band rects near y=2404: {[(OA.fnum(e.attrs,'x'), OA.fnum(e.attrs,'y'), OA.fnum(e.attrs,'width'), OA.fnum(e.attrs,'height')) for e in prev]}")
qt = [x for x in ts7 if x["y"]>2300 and x["y"]<2440]
print(f"last quote-translation baselines: {sorted(set(round(x['y'],1) for x in qt))}")

print("\n== L. Gloss source split-on-· counts (edition build vs core build) ==")
def gloss_counts(builddir):
    import glob
    res = {}
    for fn in ["content12.py","content34.py","content56.py"]:
        src = open(f"{builddir}/{fn}", encoding="utf-8").read()
        for m in re.finditer(r'\.gloss\("([^"]+)"\)', src):
            items = [s for s in m.group(1).split("·")]
            res.setdefault(fn, []).append(len(items))
    return res
print("edition:", gloss_counts(EDB), "total", sum(sum(v) for v in gloss_counts(EDB).values()))
print("core:   ", gloss_counts(COB), "total", sum(sum(v) for v in gloss_counts(COB).values()))
# render survival: each edition gloss item's head + gloss fragment in page text
print("-- render survival per item --")
page_of = {"content12.py": ["p2-vida"], "content34.py": ["p3-cultura","p4-esporte"], "content56.py": ["p5-jovens","p6-aprofundamento"]}
srcmap = {"content12.py": "p2-vida", "content34.py": None, "content56.py": None}
for fn in ["content12.py","content34.py","content56.py"]:
    src = open(f"{EDB}/{fn}", encoding="utf-8").read()
    calls = re.findall(r'\.gloss\("([^"]+)"\)', src)
    # page assignment by order within file: content34: 1st->p3, 2nd->p4; content56: 1st->p5, 2nd->p6
    pages = {"content12.py":["p2-vida"], "content34.py":["p3-cultura","p4-esporte"], "content56.py":["p5-jovens","p6-aprofundamento"]}[fn]
    for ci, call in enumerate(calls):
        pg = pages[ci]
        ts, _ = texts(ED, pg)
        joined = " ".join(x["t"] for x in ts)
        joined_ns = joined.replace(" ", "")
        for item in call.split("·"):
            item = item.strip().rstrip(".")
            if " = " in item:
                left, right = item.split(" = ", 1)
            else:
                left, right = item, ""
            ok = (left.strip() in joined) and (right.strip().split(",")[0].strip() in joined if right.strip() else True)
            print(f"{pg} item {item[:60]!r} survives={ok}")

print("\n== M. P7 quotes: occurrence counts across all edition pages + source page ==")
ts7, _ = texts(ED, "p7-lingua")
quotes = []
for x in ts7:
    t = x["t"].strip()
    if t.startswith("«") and len(t) > 8 and x["y"] > 1950 and x["y"] < 2400:
        quotes.append(t.strip("«»"))
print(f"quote-box PT quotes found: {len(quotes)}")
allpages = {}
for p in PAGES:
    ts, _ = texts(ED, p)
    allpages[p] = " ".join(x["t"] for x in ts)
for q in quotes:
    occ_pages = [p for p in PAGES if q in allpages[p]]
    total = sum(allpages[p].count(q) for p in PAGES)
    print(f"quote {q[:55]!r} total_occ={total} pages={occ_pages}")
print("-- quote translation tags on P7 --")
for x in ts7:
    if x["y"] > 1950 and "(Página" in x["t"]:
        print(f"  {x['t']}")

print("\n== N. Word-box definition verbatim ==")
joined7 = " ".join(x["t"] for x in ts7)
print("definition joined present:", "« feriadão »: sábado, domingo e segunda — três dias de descanso." in joined7)
print("gloss present:", "feriadão = el puente festivo." in joined7)
# core comparison: same definition in core P7?
ts7c, _ = texts(CO, "p7-lingua")
joined7c = " ".join(x["t"] for x in ts7c)
print("definition in core P7:", "« feriadão »: sábado, domingo e segunda — três dias de descanso." in joined7c)

print("\n== O. Readers corner verbatim (edition vs core) ==")
for d, label in [(CO,"CORE"), (ED,"ED")]:
    ts, _ = texts(d, "p7-lingua")
    seg = [x["t"] for x in ts if 1350 <= x["y"] <= 1900 and x["x"] > 1400]
    print(f"-- {label}: {' | '.join(seg)}")

print("\n== P. Model text words from render (P8 section H) ==")
ts8, _ = texts(ED, "p8-avaliacao")
# model text starts at node 'Texto modelo: ...' ; continuations same column until next heading/section
start = [x for x in ts8 if x["t"].startswith("Texto modelo:")]
print(f"start nodes: {[(x['y'], x['x'], x['t'][:60]) for x in start]}")
if start:
    s0 = start[0]
    cont = [x for x in ts8 if x["x"]==s0["x"] and s0["y"] < x["y"] < s0["y"]+400 and not re.match(r"\d+\.\s", x["t"].strip())]
    full = s0["t"] + " " + " ".join(c["t"] for c in sorted(cont, key=lambda z: z["y"]))
    body = full.split("Texto modelo:",1)[1].strip()
    print(f"model full (first 400 chars): {full[:400]!r}")
    print(f"words excl label={len(body.split())} incl label tokens={len(full.split())}")
    print(f"continuation lines: {len(cont)}")

print("\n== Q. Image payload P1 (edition vs core) ==")
def img_hash(d):
    s = open(f"{d}/svg/p1-capa.svg", encoding="utf-8").read()
    m = re.search(r'<image[^>]*href="data:image/[^;]+;base64,([^"]+)"', s)
    if not m: return None, None
    raw = m.group(1)
    import base64
    return hashlib.sha256(base64.b64decode(raw)).hexdigest(), len(raw)
print("edition:", img_hash(ED)); print("core:   ", img_hash(CO))
for d, label in [(ED,"ED"), (CO,"CORE")]:
    s = open(f"{d}/svg/p1-capa.svg", encoding="utf-8").read()
    print(label, "credit-ish strings:", [t for t in re.findall(r'<text[^>]*>([^<]{0,120})</text>', s) if 'Wikimedia' in t or 'Commons' in t or 'Domínio' in t or 'Crédit' in t][:5])

print("\n== R. Furniture vs W43 PTxES (verbatim strings) ==")
def find_str(d, p, needle):
    ts, _ = texts(d, p)
    return [x for x in ts if needle in x["t"]]
checks = [
    ("p1-capa", "TODA SEMANA EM PORTUGUÊS · CADA SEMANA · EL PORTUGUÉS QUE LEE BRASIL"),
    ("p1-capa", "TEXTOS EN PORTUGUÉS · EXPLICACIONES EN ESPAÑOL"),
    ("p2-vida", "Nota — "),
    ("p7-lingua", "BREVE"), ("p7-lingua", "QUIZ RÁPIDO"), ("p7-lingua", "CUÉNTANOS"),
]
for p, needle in checks:
    e = [x["t"] for x in find_str(ED, p, needle)]
    w = [x["t"] for x in find_str(W43, p, needle)]
    print(f"{p} {needle[:40]!r}: ED={e[:2]} W43={w[:2]}")
for p in PAGES:
    te, _ = texts(ED, p); tw, _ = texts(W43, p)
    fe = [x["t"] for x in te if x["y"]==2624.0]
    fw = [x["t"] for x in tw if x["y"]==2624.0]
    print(f"{p} footer ED={fe} W43={fw}")
print("-- W43 P1 edition line + badge nodes --")
for x in texts(W43, "p1-capa")[0]:
    if x["y"] in (330.0, 372.0) or x["t"].startswith("SEMANARIO") or x["t"].startswith("TEXT"):
        print(f"  W43 y={x['y']} size={x['size']} bold={x['bold']} {x['t'][:110]}")
print("-- ED P8 style vs W43 P8 style samples --")
for d, label in [(ED,"ED"), (W43,"W43"), (f"{B}/files/weekly-report-w45-pt-en","PTxEN")]:
    ts, _ = texts(d, "p8-avaliacao")
    s2 = [x["t"] for x in ts if x["t"].strip().startswith("2. ")]
    print(f"  {label} item2: {s2[:1]}")
print("-- pairing-note format samples (P2 gloss box first line) --")
for d, label in [(ED,"ED"), (W43,"W43")]:
    ts, _ = texts(d, "p2-vida")
    gl = [x["t"] for x in ts if x["t"].startswith("Nota —")]
    print(f"  {label}: {gl[:2]}")
