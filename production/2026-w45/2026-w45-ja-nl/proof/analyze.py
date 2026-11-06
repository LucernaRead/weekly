#!/usr/bin/env python3
# Independent JA x NL W45 proof checks. Reads only; writes JSON/TXT into proof dir.
import base64, glob, hashlib, html, json, os, re, sys
from collections import Counter

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = BASE + "/files/weekly-report-w45-ja-nl"
CO = BASE + "/files/weekly-report-w45-ja-core"
W43A = BASE + "/files/weekly-report-ja-nl"  # VOL.1 ja-nl shipped
W43B = os.path.expanduser("~/workspace/weekly-git/issues/2026-w43/2026-w43-ja-nl")
BUILD = BASE + "/hidden_files/weekly-report-w45-ja-nl-build"
COREBUILD = BASE + "/hidden_files/weekly-report-w45-ja-build"
PROOF = BASE + "/hidden_files/w45/ja-nl-proof"
OUT = {}

TEXT_RE = re.compile(r"<text\s+([^>]*)>(.*?)</text>", re.S)
def parse(path):
    s = open(path, encoding="utf-8").read()
    texts = []
    for attrs, inner in TEXT_RE.findall(s):
        def a(n, d=None):
            m = re.search(n + r'="([^"]*)"', attrs)
            return m.group(1) if m else d
        texts.append({"x": float(a("x", 0)), "y": float(a("y", 0)),
                      "size": float(a("font-size", 20)), "family": a("font-family", ""),
                      "weight": a("font-weight", ""), "anchor": a("text-anchor", "start"),
                      "fill": a("fill", ""), "text": html.unescape(re.sub(r"<[^>]+>", "", inner))})
    return s, texts

def texts_of(d, name):
    return parse(os.path.join(d, "svg", name))[1]

EDP = sorted(glob.glob(ED + "/svg/*.svg")); COP = sorted(glob.glob(CO + "/svg/*.svg"))
assert len(EDP) == 8 and len(COP) == 8
ed_texts = {os.path.basename(p): parse(p)[1] for p in EDP}
co_texts = {os.path.basename(p): parse(p)[1] for p in COP}
ed_raw = {os.path.basename(p): open(p, encoding="utf-8").read() for p in EDP}
co_raw = {os.path.basename(p): open(p, encoding="utf-8").read() for p in COP}

def find(texts, pred):
    return [t for t in texts if pred(t)]

# ---- PDF pages/sizes ----
from io import BytesIO
try:
    from pypdf import PdfReader
    for label, path in [("ed-print", ED + "/Lucerna-VOL2-NL.pdf"), ("ed-web", ED + "/Lucerna-VOL2-NL-web.pdf"),
                        ("co-print", CO + "/Lucerna-VOL2.pdf"), ("co-web", CO + "/Lucerna-VOL2-web.pdf")]:
        r = PdfReader(path)
        OUT[label] = {"pages": len(r.pages), "bytes": os.path.getsize(path),
                      "sha": hashlib.sha256(open(path, "rb").read()).hexdigest()}
except Exception as e:
    OUT["pdf_error"] = str(e)

# ---- bridge term scan (exact chars 桥接) ----
term = "\u6865\u63a5"
hits = {}
for label, files in [("svg-ed", EDP), ("svg-co", COP)]:
    for p in files:
        if term in open(p, encoding="utf-8").read():
            hits.setdefault(label, []).append(os.path.basename(p))
for f in ["transform.py", "gen_nl.py", "content12.py", "content34.py", "content56.py",
          "content7.py", "content8.py", "bslib4.py", "render.py", "run.py", "svglib.py",
          "transform-en-reference.py"]:
    p = os.path.join(BUILD, f)
    if os.path.exists(p) and term in open(p, encoding="utf-8").read():
        hits.setdefault("build", []).append(f)
for f in ["WEEKLY-KIT.md", "ABSTRACT.txt"]:
    if term in open(os.path.join(ED, f), encoding="utf-8").read():
        hits.setdefault("kit-abstract", []).append(f)
OUT["bridge_hits"] = hits

# ---- bare #37 string residual across all 8 edition pages + core check ----
bare = "\u5de5\u827a\u5c55\u523011\u67088\u65e5"  # 工艺展到11月8日
OUT["bare37_edition_pages"] = [os.path.basename(p) for p in EDP if bare in open(p, encoding="utf-8").read()]
OUT["bare37_core_pages"] = [os.path.basename(p) for p in COP if bare in open(p, encoding="utf-8").read()]
# Dutch renderings
OUT["nl37_variants"] = {}
for v in ["De tentoonstelling loopt tot 8 november", "De tentoonstelling loopt tot 8 november (zondag)"]:
    OUT["nl37_variants"][v] = [os.path.basename(p) for p in EDP if v in open(p, encoding="utf-8").read()]

# ---- P8 printed lines: #37, #137-140, E instr, P8 last element ----
p8e = ed_texts["p8-tesuto.svg"]; p8c = co_texts["p8-tesuto.svg"]
def line_starting(texts, prefix):
    return [t for t in texts if t["text"].startswith(prefix)]
OUT["p8_ed_37"] = [t["text"] for t in line_starting(p8e, "37.")]
OUT["p8_ed_137_140"] = {n: [t["text"] for t in line_starting(p8e, n + ".")] for n in ["137", "138", "139", "140"]}
OUT["p8_co_137_140"] = {n: [t["text"] for t in line_starting(p8c, n + ".")] for n in ["137", "138", "139", "140"]}
OUT["p8_ed_vertaal"] = [t["text"] for t in p8e if "Vertaal naar" in t["text"]]
OUT["p8_ed_band_right"] = [t["text"] for t in p8e if "Pagina 8" in t["text"] or "第 8 面" in t["text"]]
# P8 answer flow: texts after first separator? Use max y among answer-ish texts excluding footer (y<2580) and band
nonfoot = [t for t in p8e if t["y"] < 2580]
OUT["p8_ed_max_y_text"] = sorted([(t["y"], t["text"][:90]) for t in nonfoot], reverse=True)[:6]
# last numbered answer line: find text starting with 150.
OUT["p8_ed_150"] = [t for t in line_starting(p8e, "150.") ]
OUT["p8_co_150"] = [t for t in line_starting(p8c, "150.")]

# ---- P8 identical distinct lines + classification ----
cs, es = set(t["text"] for t in p8c), set(t["text"] for t in p8e)
ident = sorted(cs & es)
OUT["p8_ident_count"] = len(ident)
OUT["p8_ident_lines"] = ident
OUT["p8_core_lines"] = len(p8c); OUT["p8_ed_lines"] = len(p8e)
# Chinese-explanation penetration test: identical lines containing a Chinese note marker?
# A full answer line carries ' — ' + note or ' (note)'. List identical lines containing ' — '.
OUT["p8_ident_with_dash"] = [t for t in ident if " — " in t]
OUT["p8_ident_with_latin"] = [t for t in ident if re.search(r"[A-Za-z]", t)]

# ---- P8 full-segment comparison via tools/p8 internals ----
sys.path.insert(0, BASE + "/tools")
import p8 as P8M
def segments(path):
    texts = P8M.load_texts(path)
    els = P8M.answers_elements(texts)
    if els is None:
        return None
    # replicate split_joined: use module function if present
    try:
        segs = P8M.split_joined(els, 150)
    except Exception as e:
        segs = ["ERR " + str(e)]
    return segs
seg_c = segments(CO + "/svg/p8-tesuto.svg"); seg_e = segments(ED + "/svg/p8-tesuto.svg")
OUT["p8_segments_core_n"] = len(seg_c) if seg_c else None
OUT["p8_segments_ed_n"] = len(seg_e) if seg_e else None
if seg_c and seg_e:
    OUT["p8_segments_identical"] = [s for s in seg_c if s in seg_e][:20]
    OUT["p8_segments_identical_n"] = len([s for s in seg_c if s in seg_e])
    # per-number key extraction
    def keymap(segs):
        m = {}
        for s in segs:
            mm = re.match(r"\s*(\d+)\.\s*(.*)", s)
            if mm:
                m[int(mm.group(1))] = s
        return m
    kc, ke = keymap(seg_c), keymap(seg_e)
    OUT["p8_seg_keys"] = {n: {"core": kc.get(n, "")[:160], "ed": ke.get(n, "")[:160]}
                          for n in [5, 37, 66, 137, 138, 139, 140]}
    OUT["p8_seg_5_full"] = ke.get(5, "")
    OUT["p8_seg_66_full"] = ke.get(66, "")

# ---- P7: definitions frozen? freeze diff P7 lists + P7 word-box defs from content ----
import json
fz = json.load(open(PROOF + "/freeze-diff-mine.json"))
OUT["freeze_p7_added"] = fz["pages"]["7"]["added_strings"]
OUT["freeze_p7_removed"] = fz["pages"]["7"]["removed_strings"]
OUT["freeze_p7_cjk"] = (fz["pages"]["7"]["cjk_core_total"], fz["pages"]["7"]["cjk_edition_total"])
OUT["freeze_p7_added_n"] = len(fz["pages"]["7"]["added_strings"])
# P7 golden sentences: take core P7 list block sentences from content7 core build
def p7_list_sentences(svg_texts):
    # P7 list items are texts starting with 「 or containing (Pagina N) tags nearby; instead use
    # the 'Zinnen van de week' section: find texts after that header. Simpler: return all texts
    # containing 'Pagina' tags counts + full-page de-whitespace counts computed below.
    return None
all_ed = "".join(t["text"] for texts in ed_texts.values() for t in texts)
all_co = "".join(t["text"] for texts in co_texts.values() for t in texts)
blank_ed = re.sub(r"\s+", "", all_ed); blank_co = re.sub(r"\s+", "", all_co)
# Golden sentences: extract from CORE P7 SVG: sentences in quotes? Use core build content7.py P7 list literals
core7 = open(COREBUILD + "/content7.py", encoding="utf-8").read()
ed7 = open(BUILD + "/content7.py", encoding="utf-8").read()
# P7 phrase list in content7: look for lines with Pagina? Instead extract quoted Japanese sentences
# that appear in the P7 section of content7: search for 'phrase' variable region heuristically:
# fallback: use the 8 sentences from edition P7 SVG list area (texts between 'Zinnen van de week' header
# and next section). Print P7 texts for manual verification in report appendix file.
OUT["p7_ed_texts"] = [(t["y"], t["text"]) for t in ed_texts["p7-kotoba.svg"]]
OUT["p7_co_texts"] = [(t["y"], t["text"]) for t in co_texts["p7-kotoba.svg"]]
OUT["p7_tags_ed"] = {f"(Pagina {n})": all_ed.count(f"(Pagina {n})") for n in range(1, 7)}
OUT["p7_tags_co"] = {f"(Pagina {n})": all_co.count(f"(Pagina {n})") if False else 0 for n in range(1, 7)}
# core tags are Chinese-style? find core P7 tag pattern
OUT["p7_co_page_tags_raw"] = re.findall(r"\(第\d[版面页][^)]*\)", all_co)[:20]
OUT["p7_ed_page_tags_raw"] = re.findall(r"\(Pagina \d\)", all_ed)

# ---- gloss: render split on · ----
def gloss_items(texts):
    items = []
    for t in texts:
        if t["text"].startswith("Uitleg —") or t["text"].startswith("Uitleg"):
            # gloss runs are 'Uitleg — a · b · c' possibly wrapped across elements? Count per element run
            items.append(t["text"])
    return items
OUT["gloss_prefix_runs"] = {}
for fn, texts in ed_texts.items():
    runs = [t["text"] for t in texts if t["text"].startswith("Uitleg")]
    OUT["gloss_prefix_runs"][fn] = runs
# Core gloss prefix is Chinese? find core gloss runs
OUT["gloss_prefix_runs_core"] = {}
for fn, texts in co_texts.items():
    runs = [t["text"] for t in texts if "解説" in t["text"][:6] or t["text"].startswith("解説")]
    OUT["gloss_prefix_runs_core"][fn] = runs
# Count gloss items: split each Uitleg run on ' · ' plus continuation? Rendered gloss items are
# counted by splitting the FULL gloss string (joined across wrapped elements is hard); instead use
# content gloss() call strings split on ' · ' as cross-check, plus SVG: each gloss box's items =
# number of '·' separators +1 summed over runs that belong to gloss boxes (P1-P6 only).
def count_gloss_svg(texts_by_page):
    per = {}
    for fn, texts in texts_by_page.items():
        tot = 0; det = []
        for t in texts:
            if t["text"].startswith("Uitleg —"):
                body = t["text"][len("Uitleg —"):].strip()
                # body may be wrapped: a wrapped gloss continues in following elements without prefix?
                # bslib gloss renders each item? Check: count separators in this element +1
                n = body.count("·") + 1 if body else 0
                det.append((t["y"], body[:80], n))
                tot += n
        per[fn] = {"total": tot, "detail": det}
    return per
OUT["gloss_svg_split"] = count_gloss_svg(ed_texts)

# ---- reader letter ----
OUT["p7_letter_ed"] = [(t["y"], t["text"]) for t in ed_texts["p7-kotoba.svg"] if "Voorbeeldbrief" in t["text"] or "Lezershoek" in t["text"] or "Stuur" in t["text"] or "VOL.3" in t["text"]]
OUT["p7_letter_co"] = [(t["y"], t["text"]) for t in co_texts["p7-kotoba.svg"] if "読者の手紙" in t["text"] or "VOL.3" in t["text"] or "編集部" in t["text"]]
# letter body: P7 texts in letter box region? dump all P7 texts containing Japanese letter sentences
# compare Japanese letter sentences core vs edition: letter sentences are those in content7 letter block
# Use SVG: find texts that are identical between core and ed P7 and contain Japanese letter content
OUT["p7_ident_texts"] = sorted(set(t["text"] for t in co_texts["p7-kotoba.svg"]) & set(t["text"] for t in ed_texts["p7-kotoba.svg"]))

# ---- furniture geometry ----
def txt_at(texts, pred):
    return [t for t in texts if pred(t)]
p1e = ed_texts["p1-hyoushi.svg"]
OUT["furn_p1"] = {
    "wordmark": [(t["y"], t["size"], t["text"]) for t in p1e if t["text"] == "Lucerna"],
    "subtitle": [(t["y"], t["size"], t["text"]) for t in p1e if "日本語版" in t["text"]],
    "badge": [(t["y"], t["size"], t["weight"], t["fill"], t["text"]) for t in p1e if "TEKSTEN IN HET JAPANS" in t["text"]],
    "tagline": [(t["y"], t["size"], t["text"]) for t in p1e if "日本語を学ぶ人のための週刊新聞" in t["text"]],
    "topstrip": [(t["y"], t["text"]) for t in p1e if abs(t["y"] - 92) < 1],
}
# hlines + band rect from raw
def hlines(raw):
    return re.findall(r'<line[^>]*y1="([^"]*)"[^>]*y2="([^"]*)"[^>]*>', raw)
def rects(raw):
    return re.findall(r'<rect[^>]*>', raw)
OUT["furn_p1_lines"] = [m.group(0)[:200] for m in re.finditer(r'<line[^>]*>', ed_raw["p1-hyoushi.svg"])][:12]
OUT["furn_p1_rects_band"] = [m.group(0)[:220] for m in re.finditer(r'<rect[^>]*>', ed_raw["p1-hyoushi.svg"])][:8]
OUT["footers"] = {}
for fn, texts in ed_texts.items():
    OUT["footers"][fn] = [t["text"] for t in texts if t["text"].startswith("Lucerna · JAPANS")]
OUT["pagelines"] = {}
for fn, texts in ed_texts.items():
    OUT["pagelines"][fn] = [t["text"] for t in texts if re.match(r"Pagina \d van 8", t["text"])]
OUT["p8_seps"] = [t["text"] for t in p8e if re.match(r"— Pagina \d —", t["text"])]
OUT["combineer"] = {}
for fn, texts in ed_texts.items():
    OUT["combineer"][fn] = [t["text"] for t in texts if "Combineer" in t["text"] or "Koppel" in t["text"]]
OUT["e_instr_ed"] = [t["text"] for t in p8e if "Vertaal" in t["text"]]

# W43 comparisons
def w43_measure(d):
    if not os.path.exists(d + "/svg"):
        return {"error": "no svg dir"}
    files = sorted(glob.glob(d + "/svg/*.svg"))
    if not files:
        return {"error": "no svg files"}
    p1 = parse(files[0])[1]
    p1raw = open(files[0], encoding="utf-8").read()
    p8f = [f for f in files if "p8" in f]
    p8t = parse(p8f[0])[1] if p8f else []
    return {
        "files": [os.path.basename(f) for f in files],
        "wordmark": [(t["y"], t["size"], t["text"]) for t in p1 if t["text"] == "Lucerna"],
        "subtitle": [(t["y"], t["size"], t["text"]) for t in p1 if "日本語版" in t["text"] or "VOL" in t["text"]],
        "badge": [(t["y"], t["size"], t["weight"], t["text"]) for t in p1 if "TEKSTEN IN HET JAPANS" in t["text"]],
        "tagline": [(t["y"], t["size"], t["text"]) for t in p1 if "週刊新聞" in t["text"] or "日本語を学ぶ" in t["text"]],
        "lines": [m.group(0)[:180] for m in re.finditer(r'<line[^>]*>', p1raw)][:12],
        "p8_band": [t["text"] for t in p8t if "Pagina 8" in t["text"] or "第 8 面" in t["text"]],
        "p8_e_instr": [t["text"] for t in p8t if "Vertaal" in t["text"] or "Translate" in t["text"]],
        "p2_combine": None,
    }
OUT["w43_files_dir"] = w43_measure(W43A)
OUT["w43_weeklygit"] = w43_measure(W43B)
# W43 P2/P8 combine instr
for label, d in [("w43_files", W43A), ("w43_git", W43B)]:
    files = sorted(glob.glob(d + "/svg/*.svg"))
    res = {}
    for f in files:
        ts = parse(f)[1]
        res[os.path.basename(f)] = [t["text"] for t in ts if "Combineer" in t["text"] or "Koppel" in t["text"]]
    OUT[label + "_combine"] = res

# ---- images: parse href + xlink:href ----
def img_hashes(d):
    out = {}
    for p in sorted(glob.glob(d + "/svg/*.svg")):
        raw = open(p, encoding="utf-8").read()
        b64s = re.findall(r'(?:xlink:href|href)="data:image/[^;]+;base64,([^"]+)"', raw)
        out[os.path.basename(p)] = [
            {"b64_sha12": hashlib.sha256(b.encode()).hexdigest()[:12],
             "decoded_sha12": hashlib.sha256(base64.b64decode(b)).hexdigest()[:12],
             "decoded_len": len(base64.b64decode(b))} for b in b64s]
    return out
OUT["images_ed"] = img_hashes(ED)
OUT["images_co"] = img_hashes(CO)
def credits(d):
    out = {}
    for p in sorted(glob.glob(d + "/svg/*.svg")):
        ts = parse(p)[1]
        out[os.path.basename(p)] = [t["text"] for t in ts if any(k in t["text"] for k in ["Poliphilo", "Hiroshige", "Syced", "Kratochvil", "CC0", "パブリック", "出典", "写真", "版画"])]
    return out
OUT["credits_ed"] = credits(ED); OUT["credits_co"] = credits(CO)

# ---- word-level CJK residue ----
core_all = "".join(t["text"] for texts in co_texts.values() for t in texts)
OUT["wordlevel_residue"] = []
for fn, texts in ed_texts.items():
    for t in texts:
        for run in re.findall(r"[\u4e00-\u9fff\u3040-\u30ff]+", t["text"]):
            if len(run) >= 2 and run not in core_all:
                OUT["wordlevel_residue"].append((fn, t["y"], run, t["text"][:90]))

# ---- ABSTRACT ----
ab = open(ED + "/ABSTRACT.txt", encoding="utf-8").read()
OUT["abstract"] = {"raw": ab, "lines": ab.strip().splitlines(), "has_ascii_dquote": '"' in ab,
                   "chars": len(ab.strip())}

# ---- P7 teaser end + P8 end (baseline y + ink bottom via PIL) ----
sys.path.insert(0, BUILD)
try:
    import svglib as SV
    def ink_bottom(t):
        # svglib font loader: try font_for/get_font
        fam = "sans" if "Sans" in t["family"] else ("serif" if "Serif" in t["family"] else "sans")
        bold = t["weight"] in ("700", "bold")
        try:
            f = SV.font_for(fam, bold, t["size"]) if hasattr(SV, "font_for") else SV.get_font(fam, bold, t["size"])
            # PIL getbbox on the string: (left, top, right, bottom) relative to anchor point?
            # For baseline-anchored text, ink bottom ≈ y + descent; use font.getmetrics
            asc, desc = f.getmetrics()
            return {"baseline": t["y"], "ink_bottom_est": t["y"] + desc * 0.0 + (f.getbbox(t["text"])[3] if t["text"] else 0),
                    "ascent": asc, "descent": desc, "bbox": f.getbbox(t["text"]) if t["text"] else None}
        except Exception as e:
            return {"error": str(e)}
    # P7 teaser: last non-footer text on P7 (VOL.3 teaser band?) — find max y <2580
    p7nf = [t for t in ed_texts["p7-kotoba.svg"] if t["y"] < 2580]
    p7last = sorted(p7nf, key=lambda t: t["y"])[-4:]
    OUT["p7_last_texts"] = [(t["y"], t["text"][:100]) for t in p7last]
    OUT["p7_last_ink"] = [(t["text"][:60], ink_bottom(t)) for t in p7last]
    p8last = sorted(nonfoot, key=lambda t: t["y"])[-4:]
    OUT["p8_last_texts"] = [(t["y"], t["text"][:100]) for t in p8last]
    OUT["p8_last_ink"] = [(t["text"][:60], ink_bottom(t)) for t in p8last]
except Exception as e:
    OUT["ink_error"] = str(e)

# ---- build-log overflow scan: check render logs? build dir has no render log; check SVG for overflow markers? ----
# Instead record: search edition SVGs for 'FLOW' markers (none expected in SVG) + check content8 MODELO essay
OUT["essay_check"] = {}
for label, path in [("core", COREBUILD + "/content8.py"), ("ed", BUILD + "/content8.py")]:
    txt = open(path, encoding="utf-8").read()
    m = re.search(r"MODELO\s*=\s*\"([^\"]*)\"", txt, re.S)
    OUT["essay_check"][label] = {"found": bool(m), "len_chars": len(m.group(1)) if m else None,
                                 "text": m.group(1) if m else None}
# essay in SVG: P8 H texts joined
OUT["essay_svg_ed"] = [t["text"] for t in p8e if "私の11月の週末" in t["text"]]

# ---- KIT claim cross-checks: counts ----
OUT["kit_counts"] = {"badge_p1": sum(1 for t in p1e if "TEKSTEN IN HET JAPANS" in t["text"])}

json.dump(OUT, open(PROOF + "/analyze.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("PDF:", OUT.get("ed-print"), OUT.get("ed-web"))
print("bridge:", OUT["bridge_hits"])
print("bare37 ed:", OUT["bare37_edition_pages"], "core:", OUT["bare37_core_pages"])
print("p8_37:", OUT["p8_ed_37"])
print("p8_137-140 ed:", OUT["p8_ed_137_140"])
print("p8_137-140 co:", OUT["p8_co_137_140"])
print("p8 ident:", OUT["p8_ident_count"], "dash-ident:", OUT["p8_ident_with_dash"], "latin-ident:", OUT["p8_ident_with_latin"])
print("p8 seg identical n:", OUT.get("p8_segments_identical_n"))
print("p8 seg keys:", OUT.get("p8_seg_keys"))
print("gloss svg split:", OUT["gloss_svg_split"])
print("gloss prefix runs:", OUT["gloss_prefix_runs"])
print("wordlevel residue:", OUT["wordlevel_residue"])
print("images ed:", OUT["images_ed"])
print("images co:", OUT["images_co"])
print("credits equal:", OUT["credits_ed"] == OUT["credits_co"])
print("abstract:", OUT["abstract"])
print("p7 tags ed:", OUT["p7_tags_ed"])
print("p7 last:", OUT["p7_last_texts"])
print("p8 last:", OUT["p8_last_texts"])
print("essay:", {k: v["len_chars"] for k, v in OUT["essay_check"].items()})
print("furn p1:", OUT["furn_p1"])
print("w43 files:", OUT["w43_files_dir"])
print("w43 git:", OUT["w43_weeklygit"])
print("combineer:", OUT["combineer"])
print("p8 seps:", OUT["p8_seps"], "footers n:", {k: len(v) for k, v in OUT["footers"].items()}, "pagelines:", OUT["pagelines"])
