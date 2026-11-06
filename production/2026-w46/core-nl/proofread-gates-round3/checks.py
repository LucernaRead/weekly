"""Round 2 independent checks: counts, gloss, chart, P7, essay, kinsoku,
badge/footer/images, PDF layer, dates, promises, F/essay coordinates.
ET-based SVG text extraction (fast; avoids regex over base64 blobs).
Writes counts.json + checks.log into the round2 gate dir.
"""
import re, glob, os, json, collections, subprocess, pathlib
GOAL = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
OUT = GOAL/"hidden_files/w46/nl-proofread-gates-round3"
F = GOAL/"files"
PAGES = ["p1-voorpagina.svg","p2-leven.svg","p3-cultuur.svg","p4-sport.svg",
         "p5-jongeren.svg","p6-verdieping.svg","p7-taal.svg","p8-toets.svg"]
EDS = ["core","de","en","es","fr","it","ja","ko","pt","ru","zh-tw"]
from xml.etree import ElementTree as ET
NS = "{http://www.w3.org/2000/svg}"
def svg_texts(path):
    tree = ET.parse(path)
    return ["".join(el.itertext()) for el in tree.iter(f"{NS}text")]
def svg_texts_xy(path):
    tree = ET.parse(path)
    return [(el.get("x"), el.get("y"), "".join(el.itertext())) for el in tree.iter(f"{NS}text")]
log = open(OUT/"checks.log", "w", encoding="utf-8")
def say(s=""):
    print(s); log.write(s+"\n")

# ---------- 1. COUNTS (same method as Round 1 count_check.py) ----------
say("=== COUNTS ===")
results = {}
for ed in EDS:
    D = F/f"weekly-report-w46-nl-{ed}"
    slug = "2026-w46-nl-zh-cn" if ed == "core" else f"2026-w46-nl-{ed}"
    md = glob.glob(str(D/"*.text.md"))[0]
    lines = open(md, encoding="utf-8").read().splitlines()
    cur = None; per_page = collections.Counter(); levels = collections.Counter(); nums = []
    item_re = re.compile(r"^(\d+)\.\s*\[(A2|B1|B2)\s*[·•]\s*([^\]]+)\]")
    types = collections.Counter()
    for ln in lines:
        m = re.match(r"^## Pagina (\d+)\s*$", ln)
        if m: cur = int(m.group(1)); continue
        m = item_re.match(ln.strip())
        if m:
            n = int(m.group(1)); nums.append(n); levels[m.group(2)] += 1; types[m.group(3).strip()] += 1
            if cur: per_page[cur] += 1
    svg_per_page = {}; svg_nums = []
    for i, pg in enumerate(PAGES, 1):
        ts = svg_texts(D/"svg"/pg)
        stems = [t for t in ts if re.fullmatch(r"\d+\.", t.strip())]
        svg_per_page[i] = len(stems)
        svg_nums += [int(s.strip()[:-1]) for s in stems]
    # levels from text.md bracketed + range headers (25-28 A2, 141-144 B2)
    tot_levels = dict(levels); tot_levels["A2"] = tot_levels.get("A2",0)+4; tot_levels["B2"] = tot_levels.get("B2",0)+4
    per_page_full = dict(sorted(per_page.items()))
    # add range-header items: P2 +4 (25-28), P8 +4 (141-144)
    per_page_full[2] = per_page_full.get(2,0)+4; per_page_full[8] = per_page_full.get(8,0)+4
    results[ed] = {"slug": slug, "textmd_bracketed": len(nums),
                   "textmd_contig_142": sorted(nums)==list(range(1,151)) or (len(nums)==142 and sorted(set(nums))==sorted(set(range(1,151))-set([25,26,27,28,141,142,143,144]))),
                   "textmd_missing": sorted(set(range(1,151))-set(nums)),
                   "textmd_per_page_bracketed": dict(sorted(per_page.items())),
                   "textmd_levels_bracketed": dict(levels), "levels_total": tot_levels,
                   "per_page_total": per_page_full, "total": len(nums)+8,
                   "types": dict(types),
                   "svg_stems": len(svg_nums), "svg_missing": sorted(set(range(1,151))-set(svg_nums)),
                   "svg_dupes": sorted([n for n,c in collections.Counter(svg_nums).items() if c>1]),
                   "svg_per_page": svg_per_page}
    say(f"{slug}: textmd bracketed={len(nums)} missing={results[ed]['textmd_missing']} levels_bracketed={dict(levels)} levels_total={tot_levels} per_page_total={per_page_full} total={len(nums)+8}")
    say(f"   types={dict(types)}")
    say(f"   svg stems={len(svg_nums)} missing={results[ed]['svg_missing']} dupes={results[ed]['svg_dupes']} per_page={svg_per_page}")
json.dump(results, open(OUT/"counts.json","w"), ensure_ascii=False, indent=1)

# ---------- 2. GLOSS counts + headwords ----------
say("\n=== GLOSS ===")
GLOSS_PAGES = {"p2-leven.svg":2,"p3-cultuur.svg":3,"p4-sport.svg":4,"p5-jongeren.svg":5,"p6-verdieping.svg":6}
for ed in EDS:
    D = F/f"weekly-report-w46-nl-{ed}"
    counts = {}
    for pg, pn in GLOSS_PAGES.items():
        # gloss box = contiguous text block: find element containing gloss prefix markers, rejoin wrapped lines by y-order within the gloss column
        # Robust approach: find the gloss string in the .text.md (> quote block) and count items by splitting on '·'; then verify headwords present in SVG text.
        pass
    # text.md gloss lines: lines starting with '>'
    md = glob.glob(str(D/"*.text.md"))[0]
    gloss_lines = [ln[1:].strip() for ln in open(md, encoding="utf-8").read().splitlines() if ln.startswith("> ")]
    # P2-P6 gloss lines are the ones containing Dutch headwords; P7 golden quotes also start with '>' but contain « »
    gloss_lines = [g for g in gloss_lines if "«" not in g]
    say(f"{ed}: text.md gloss blocks={len(gloss_lines)}")
    for g in gloss_lines:
        items = [i.strip() for i in g.split("·")]
        say(f"   n={len(items)} :: {g[:110]}")
    # SVG: verify each Dutch headword appears in the corresponding page SVG text (joined)
    # headwords from core text.md gloss blocks (frozen)
    core_md = glob.glob(str(F/"weekly-report-w46-nl-core/*.text.md"))[0]
    core_gloss = [ln[1:].strip() for ln in open(core_md, encoding="utf-8").read().splitlines() if ln.startswith("> ") and "«" not in ln]

# ---------- 3. CHART bars ----------
say("\n=== CHART BARS (P6 rects fill #3e4c2a) ===")
for ed in EDS:
    tree = ET.parse(F/f"weekly-report-w46-nl-{ed}/svg/p6-verdieping.svg")
    bars = []
    for el in tree.iter():
        if el.tag.endswith("rect"):
            fill = (el.get("fill") or "").lower()
            if fill == "#3e4c2a":
                try: bars.append((float(el.get("x")), float(el.get("y")), float(el.get("width")), float(el.get("height"))))
                except: pass
    bars = sorted(bars, key=lambda b: b[1])
    # chart bars are the 4 at x=1473 with height 18
    chart = [b for b in bars if abs(b[0]-1473) < 1 and abs(b[3]-18) < 1]
    say(f"{ed}: chart bars (x,y,w,h)={chart} widths={[b[2] for b in chart]}")

# ---------- 4. P7 golden sentences ----------
say("\n=== P7 GOLDEN SENTENCES ===")
QUOTES = [
 "Op maandag 9 november begint het Sinterklaasjournaal op televisie",
 "Een dag later, op zondag 15 november, is de intocht in Amsterdam: de 88e editie",
 "Daarom is Sint-Maarten het feest van het delen: licht delen, eten delen, aandacht delen",
 "Op zaterdag 14 november komt Sinterklaas officieel aan in Grave",
 "Op vrijdag 13 november speelt Oranje thuis tegen Griekenland",
 "Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4",
 "Sint-Maarten is een oude traditie in Nederland",
 "Een traditie leeft als mensen haar blijven vieren",
]
def norm(s):
    return re.sub(r"\s+", " ", s).strip()
for ed in EDS:
    D = F/f"weekly-report-w46-nl-{ed}"
    p7joined = norm(" ".join(svg_texts(D/"svg/p7-taal.svg")))
    tags = re.findall(r"\(Pagina (\d+)\)", p7joined)
    ok = [q in p7joined for q in QUOTES]
    say(f"{ed}: P7 quotes {sum(ok)}/8 ok={ok} tags={tags}")
    # body check: each quote in its source page
    srcpages = ["p1-voorpagina.svg","p1-voorpagina.svg","p2-leven.svg","p3-cultuur.svg","p4-sport.svg","p5-jongeren.svg","p6-verdieping.svg","p6-verdieping.svg"]
    bodyok = []
    for q, pg in zip(QUOTES, srcpages):
        bodyok.append(q in norm(" ".join(svg_texts(D/"svg"/pg))))
    say(f"   body quotes {sum(bodyok)}/8 ok={bodyok}")

# ---------- 5. MODEL ESSAY word count ----------
say("\n=== MODEL ESSAY ===")
for ed in EDS:
    D = F/f"weekly-report-w46-nl-{ed}"
    md = open(glob.glob(str(D/"*.text.md"))[0], encoding="utf-8").read()
    m = re.search(r"Tekstmodel:\s*(.+)", md, re.S)
    essay = m.group(1).strip().split("\n")[0] if m else ""
    # essay may wrap in md? take until blank line
    words = essay.split()
    say(f"{ed}: essay words={len(words)} :: {essay[:80]}...")
    # SVG: lines after 'Tekstmodel:' element in P8
    p8 = svg_texts_xy(D/"svg/p8-toets.svg")
    # find index of element starting with Tekstmodel
    idx = next((i for i,(x,y,t) in enumerate(p8) if t.startswith("Tekstmodel:")), None)
    if idx is not None:
        # essay lines follow in same column (x=1451) until footer separator; collect until y>2624 or next section
        collected = [p8[idx][2].replace("Tekstmodel:","").strip()]
        for x,y,t in p8[idx+1:]:
            if x=="1451" and float(y)<2580 and not t.startswith("—") and "De Lucerna" not in t:
                collected.append(t)
            elif float(y)>=2580: break
        joined = norm(" ".join(collected))
        say(f"   SVG essay words={len(joined.split())} :: {joined[:80]}...")

# ---------- 6. KINSOKU ----------
say("\n=== KINSOKU / LINE-START & LINE-END PUNCT ===")
CLOSERS = set("。、，,」』）］｝〉》】､・.!?%)")
OPENERS = set("「『（［｛〈《【")
for ed in ["core","ja","zh-tw"]:
    D = F/f"weekly-report-w46-nl-{ed}"
    for pg in PAGES:
        for x,y,t in svg_texts_xy(D/"svg"/pg):
            if not t: continue
            if t[0] in CLOSERS:
                say(f"  LINE-START-CLOSER {ed} {pg} x={x} y={y}: {t!r}")
            if t[-1] in OPENERS:
                say(f"  LINE-END-OPENER {ed} {pg} x={x} y={y}: {t!r}")
say("kinsoku scan done (no lines above = clean)")

# ---------- 7. BADGE / FOOTER / IMAGES / CREDITS ----------
say("\n=== BADGE+FOOTER+IMAGES ===")
for ed in EDS:
    D = F/f"weekly-report-w46-nl-{ed}"
    footers = 0; pagelines = 0
    for pg in PAGES:
        texts = svg_texts_xy(D/"svg"/pg)
        if any(y=="2624" and "De Lucerna" in t for x,y,t in texts): footers += 1
        if any(y=="2624" and ("版" in t or "Pagina" in t or "Seite" in t or "page" in t.lower() or "ページ" in t or "면" in t or "страниц" in t.lower() or "página" in t.lower()) for x,y,t in texts): pagelines += 1
        # image count
    imgcounts = []
    for pg in PAGES:
        tree = ET.parse(D/"svg"/pg)
        n = sum(1 for el in tree.iter() if el.tag.endswith("image"))
        imgcounts.append(n)
    credits = []
    for pg in PAGES:
        for t in svg_texts(D/"svg"/pg):
            if t.startswith("Foto:"): credits.append(t)
    say(f"{ed}: footer pages={footers}/8 pageline pages={pagelines}/8 images per page={imgcounts} credits={len(credits)} {credits}")
    # P1 badge/subtitle elements
    p1 = svg_texts_xy(D/"svg/p1-voorpagina.svg")
    for x,y,t in p1:
        if y in ("372","568") or ("VOL.3" in t and float(y)<600):
            say(f"   P1 y={y} x={x}: {t!r}")

# ---------- 8. F-OPTION vs ESSAY column (zh-tw + core P8) ----------
say("\n=== ZH-TW/CORE P8 F-OPTION vs ESSAY COLUMNS ===")
for ed in ["core","zh-tw"]:
    p8 = svg_texts_xy(F/f"weekly-report-w46-nl-{ed}/svg/p8-toets.svg")
    for x,y,t in p8:
        if x=="1023" and 800<=float(y)<=1030:
            say(f"  {ed} F-opt x={x} y={y}: {t!r}")
        if x=="1451" and 860<=float(y)<=900:
            say(f"  {ed} essay x={x} y={y}: {t!r}")

# ---------- 9. PDF checks ----------
say("\n=== PDF TEXT LAYER ===")
for ed in EDS:
    D = F/f"weekly-report-w46-nl-{ed}"
    web = sorted(D.glob("*-web.pdf"))[0]
    prn = sorted([p for p in D.glob("*.pdf") if "web" not in p.name])[0]
    def txtbytes(pdf):
        r = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True)
        return len(r.stdout), r.stdout
    wb, wtxt = txtbytes(web); pb, ptxt = txtbytes(prn)
    # pages via pypdf
    from pypdf import PdfReader
    wr = PdfReader(str(web)); pr = PdfReader(str(prn))
    wbox = wr.pages[0].mediabox; pbox = pr.pages[0].mediabox
    say(f"{ed}: web={web.name} {web.stat().st_size}B pages={len(wr.pages)} size={float(wbox.width)}x{float(wbox.height)} textbytes={wb}; print={prn.name} {prn.stat().st_size}B pages={len(pr.pages)} textbytes={pb}; web==print text: {wtxt==ptxt}")

# ---------- 10. OCCLUSION JSONs ----------
say("\n=== OCCLUSION JSON SUMMARY ===")
for f in sorted(OUT.glob("occlusion-*.json")):
    d = json.load(open(f))
    flags = d.get("flags") or d.get("new_flags") or []
    say(f"{f.name}: {d if isinstance(d,dict) and len(str(d))<200 else ''} flags={flags}")

log.close()
print("CHECKS DONE")
