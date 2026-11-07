#!/usr/bin/env python3
# Independent proof round 2 for W45 JA x EN. Read-only vs files/ trees; writes only to proof2 dir.
import re, json, hashlib, os, sys, difflib
from pathlib import Path
from collections import Counter
B = Path(os.environ["HOME"]) / "workspace/goals/lucernaread-social-media-operations"
CORE = B / "files/weekly-report-w45-ja-core/svg"
ED = B / "files/weekly-report-w45-ja-en/svg"
W43 = B / "files/weekly-report-ja-en/svg"
PROOF = B / "hidden_files/w45/ja-en-proof2"
BUILD = B / "hidden_files/weekly-report-w45-ja-en-build"
FILES = {"p1": "p1-hyoushi.svg", "p2": "p2-kurashi.svg", "p3": "p3-bunka.svg", "p4": "p4-supotsu.svg",
         "p5": "p5-wakamono.svg", "p6": "p6-fukayomi.svg", "p7": "p7-kotoba.svg", "p8": "p8-tesuto.svg"}

def texts_of(p):
    t = p.read_text(); out = []
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', t):
        a = m.group(1); s = m.group(2)
        def g(k):
            mm = re.search(k + r'="([^"]*)"', a); return mm.group(1) if mm else ""
        out.append({"x": float(g("x") or 0), "y": float(g("y") or 0), "size": g("font-size"),
                    "bold": "700" in a, "anchor": g("text-anchor"), "fill": g("fill"),
                    "fam": g("font-family"), "text": s})
    return out

def raw(p): return p.read_text()
def is_cjk(ch): return '\u2e80' <= ch <= '\u9fff' or '\u3040' <= ch <= '\u30ff'
def cjk_runs(s): return re.findall(r'[\u2e80-\u9fff\u3040-\u30ff]+', s)
def has_kana(s): return bool(re.search(r'[\u3040-\u30ff]', s))

out = {}

# ---------- 0. scope vs pre-fix baseline (hash-only lines ONLY) ----------
pref = (BUILD / "sha256-fix5-prefix.txt").read_text()
pre = {}
for line in pref.splitlines():
    m = re.match(r'^([0-9a-f]{64})\s+(\S+)$', line.strip())
    if m: pre[Path(m.group(2)).name] = m.group(1)
cur = {}
for sub, names in [("svg", list(FILES.values())), ("cards", None)]:
    pass
for fn in FILES.values():
    cur[fn] = hashlib.sha256((ED / fn).read_bytes()).hexdigest()
for fn in sorted((B / "files/weekly-report-w45-ja-en/cards").glob("*.png")):
    cur[fn.name] = hashlib.sha256(fn.read_bytes()).hexdigest()
for pdf in ["Lucerna-VOL2-EN.pdf", "Lucerna-VOL2-EN-web.pdf"]:
    cur[pdf] = hashlib.sha256((B / "files/weekly-report-w45-ja-en" / pdf).read_bytes()).hexdigest()
scope = {"changed": [], "unchanged": [], "missing_in_prefix": []}
for name, h in sorted(cur.items()):
    if name not in pre: scope["missing_in_prefix"].append(name)
    elif pre[name] != h: scope["changed"].append((name, pre[name][:12], h[:12]))
    else: scope["unchanged"].append(name)
# build-tree files vs prefix
bt = {}
for fn in ["transform.py", "run.py", "render.py", "content12.py", "content34.py", "content56.py",
           "content7.py", "content8.py", "bslib4.py", "svglib.py"]:
    h = hashlib.sha256((BUILD / fn).read_bytes()).hexdigest()
    bt[fn] = {"pre": pre.get(fn, "")[:12], "cur": h[:12], "changed": pre.get(fn) != h}
out["scope"] = scope; out["buildtree"] = bt
out["svglib_md5"] = hashlib.md5((BUILD / "svglib.py").read_bytes()).hexdigest()

# ---------- 1. forbidden words ----------
for name, path in [("svg-ed", ED), ("kit", B / "files/weekly-report-w45-ja-en/WEEKLY-KIT.md"),
                   ("abstract", B / "files/weekly-report-w45-ja-en/ABSTRACT.txt")]:
    if path.is_dir():
        cnt = sum(p.read_text().count("桥接") + p.read_text().count("橋接") for p in path.glob("*.svg"))
    else:
        cnt = path.read_text().count("桥接") + path.read_text().count("橋接")
    out[f"forbidden_{name}"] = cnt

# ---------- 2. kinsoku: standard set vs wide set (incl 〜) ----------
STD = set("、。．，」』）】〕")
WIDE = STD | set("ー゛゜ァィゥェォッャュョヮぁぃぅぇぉっゃゅょゎ・：；？！〜…")
kin = {}
for pg, fn in FILES.items():
    for label, d in [("core", CORE), ("ed", ED)]:
        ts = texts_of(d / fn)
        kin[f"{label}_{pg}_std"] = [t["text"] for t in ts if t["text"] and t["text"][0] in STD]
        kin[f"{label}_{pg}_wide"] = [t["text"] for t in ts if t["text"] and t["text"][0] in WIDE]
out["kinsoku"] = {k: (len(v), v) for k, v in kin.items()}

# ---------- 3. freeze diff analysis ----------
fd = json.load(open(PROOF / "freeze-diff-proof2.json"))
PGK = {"p1":"1","p2":"2","p3":"3","p4":"4","p5":"5","p6":"6","p7":"7","p8":"8"}
out["freeze_pages"] = {pg: {"added_n": len(fd["pages"][PGK[pg]]["added_strings"]), "removed_n": len(fd["pages"][PGK[pg]]["removed_strings"]),
    "cjk_core": fd["pages"][PGK[pg]]["cjk_core_total"], "cjk_ed": fd["pages"][PGK[pg]]["cjk_edition_total"], "cjk_added": fd["pages"][PGK[pg]]["cjk_added"]}
    for pg in FILES}
out["removed_with_kana"] = {pg: [s["text"] for s in fd["pages"][PGK[pg]]["removed_strings"] if has_kana(s["text"])]
                            for pg in FILES}
out["added_with_cjk"] = {pg: [s["text"] for s in fd["pages"][PGK[pg]]["added_strings"] if cjk_runs(s["text"])]
                         for pg in FILES}
# frozen sentence check: core strings ending with 。 missing from edition multiset
fmiss = {}
for pg, fn in FILES.items():
    cc = Counter(t["text"] for t in texts_of(CORE / fn)); ec = Counter(t["text"] for t in texts_of(ED / fn))
    fmiss[pg] = [(s, c, ec.get(s, 0)) for s, c in cc.items() if s.endswith("。") and ec.get(s, 0) < c]
out["final_maru_missing"] = fmiss
# freeze string-scope vs pre-fix proof1 json and vs fix5 json
pre_fd = json.load(open(B / "hidden_files/w45/ja-en-proof/freeze-diff-proof.json"))
fix5_fd = json.load(open(BUILD / "freeze-diff-fix5.json"))
def sm(fdobj, pg, key):
    return Counter(s["text"] for s in fdobj["pages"][pg][key])
scope_str = {}
for pg in FILES:
    for key in ["added_strings", "removed_strings"]:
        a, b = sm(fd, PGK[pg], key), sm(pre_fd, PGK[pg], key)
        scope_str[f"{pg}_{key}_vs_preproof"] = {"only_new": sorted((a - b).elements()),
                                                "only_pre": sorted((b - a).elements())}
        a2, b2 = sm(fd, PGK[pg], key), sm(fix5_fd, PGK[pg], key)
        scope_str[f"{pg}_{key}_vs_fix5"] = {"only_new": sorted((a2 - b2).elements()),
                                            "only_fix5": sorted((b2 - a2).elements())}
out["freeze_string_scope"] = scope_str

# ---------- 4. corrosion pairing (removed<->added difflib >0.5), P1/P4/P5/P6/P8 ----------
corr = {}
for pg in ["p1", "p4", "p5", "p6", "p8"]:
    v = fd["pages"][PGK[pg]]
    rem = [s["text"] for s in v["removed_strings"]]; add = [s["text"] for s in v["added_strings"]]
    pairs = []
    for r in rem:
        best, br = None, 0.0
        for a in add:
            ratio = difflib.SequenceMatcher(None, r, a).ratio()
            if ratio > br: best, br = a, ratio
        if br > 0.5: pairs.append((round(br, 3), r, best))
    corr[pg] = pairs
out["corrosion_pairs"] = corr
out["corrosion_jp_jp"] = {pg: [p for p in pairs if has_kana(p[1]) and has_kana(p[2])]
                          for pg, pairs in corr.items()}

# ---------- 5. P1 trend widths ----------
sys.path.insert(0, str(BUILD))
import svglib
trend = {}
for t in texts_of(ED / "p1-hyoushi.svg"):
    if t["text"] in ("Dates in articles; not exact statistics", "These four topics shape this issue."):
        kind = "serif" if "Serif" in t["fam"] else "sans"
        w = svglib.text_w(t["text"], kind, t["bold"], float(t["size"]))
        trend[t["text"]] = {"x": t["x"], "y": t["y"], "size": t["size"], "anchor": t["anchor"],
                            "width_px": round(w, 1)}
out["p1_trend_widths"] = trend

# ---------- 6. counts: bold chip -> next number/range label ----------
counts = {}
for pg, fn in FILES.items():
    ts = texts_of(ED / fn)
    mapping = {}
    for i, t in enumerate(ts):
        if t["text"] in ("A2", "B1", "B2") and t["bold"] and i + 1 < len(ts):
            nxt = ts[i + 1]["text"]
            m1 = re.fullmatch(r"(\d+)\.", nxt)
            m2 = re.fullmatch(r"(\d+)–(\d+)\.", nxt)
            if m1: mapping[int(m1.group(1))] = t["text"]
            elif m2:
                for n in range(int(m2.group(1)), int(m2.group(2)) + 1): mapping[n] = t["text"]
    counts[pg] = {"numbers": sorted(mapping), "levels": dict(Counter(mapping.values())),
                  "n": len(mapping)}
out["counts"] = counts
tot_levels = Counter()
for pg, c in counts.items(): tot_levels.update(c["levels"])
out["counts_total"] = {"n": sum(c["n"] for c in counts.values()), "levels": dict(tot_levels)}

# ---------- 7. P8 printed answer lines (answer section only, continuation-joined) ----------
def p8_lines(d):
    ts = texts_of(d / "p8-tesuto.svg")
    hi = [i for i, t in enumerate(ts) if t["y"] == 1302.0 and "答え" in t["text"]][0]
    lines = {}; cur = None
    for t in ts[hi + 1:]:
        s = t["text"]
        m = re.match(r"^(\d+)\.\s+(.*)$", s)
        if m:
            cur = int(m.group(1)); lines[cur] = {"x": t["x"], "y": t["y"], "parts": [m.group(2)]}
        elif cur is not None and t["x"] == lines[cur]["x"] and not s.startswith("— ") \
                and "Lucerna ·" not in s and not s.startswith("Page "):
            # continuation fragment of the same printed line (wrap)
            lines[cur]["parts"].append(s)
    joined = {}
    for n, v in lines.items():
        # join: CJK-start fragments attach directly, others with a space
        s = v["parts"][0]
        for frag in v["parts"][1:]:
            s += frag if (frag and is_cjk(frag[0])) or frag.startswith("）") else " " + frag
        joined[n] = {"line": f"{n}. {s}", "x": v["x"], "y": v["y"], "parts": v["parts"]}
    return joined
ce = p8_lines(ED); cc = p8_lines(CORE)
out["p8_counts"] = {"core": len(cc), "ed": len(ce)}
out["p8_identical_lines"] = sorted(n for n in ce if n in cc and ce[n]["line"] == cc[n]["line"])
def split_key(line):
    body = re.sub(r"^\d+\.\s+", "", line)
    if " — " in body: return body.split(" — ", 1)[0]
    return body
keydiff_detail = {}
for n in sorted(set(cc) | set(ce)):
    c, e = cc.get(n, {}).get("line", ""), ce.get(n, {}).get("line", "")
    if c != e:
        keydiff_detail[n] = {"core": c, "ed": e, "core_key": split_key(c), "ed_key": split_key(e),
                             "key_same": split_key(c) == split_key(e)}
out["p8_printed_diff"] = keydiff_detail
# P8 note language: note part after ' — '; list notes containing CJK
def note_part(line):
    body = re.sub(r"^\d+\.\s+", "", line)
    return body.split(" — ", 1)[1] if " — " in body else ""
note_cjk = {}
for n, v in ce.items():
    np_ = note_part(v["line"])
    if cjk_runs(np_): note_cjk[n] = {"line": v["line"], "note": np_, "cjk_runs": cjk_runs(np_)}
out["p8_ed_note_cjk"] = note_cjk
# P8 weekday suffixes in edition notes (Japanese weekday words) + P8 notes with kana
out["p8_ed_notes_with_kana"] = {n: v["line"] for n, v in ce.items() if has_kana(note_part(v["line"]))}

# ---------- 8. P7: phrases, tags, definitions, vocab ----------
def full_blank(d):
    s = ""
    for pg, fn in FILES.items(): s += "".join(t["text"] for t in texts_of(d / fn))
    return re.sub(r"\s+", "", s)
ed_blank, co_blank = full_blank(ED), full_blank(CORE)
p7ed = texts_of(ED / "p7-kotoba.svg"); p7co = texts_of(CORE / "p7-kotoba.svg")
def phrases(ts):
    idx = [i for i, t in enumerate(ts) if "今週のフレーズ" in t["text"]][0]
    entries = []
    i = idx + 1
    while i < len(ts):
        t = ts[i]
        if t["text"].startswith("来週") or t["text"].startswith("Lucerna"): break
        if t["text"].startswith("「"):
            quote = t["text"].strip("「」")
            trans = ts[i + 1]["text"] if i + 1 < len(ts) else ""
            entries.append({"quote": quote, "trans": trans})
            i += 2
        else: i += 1
    return entries
ed_ph, co_ph = phrases(p7ed), phrases(p7co)
ph = []
for a, b in zip(ed_ph, co_ph):
    q = a["quote"]
    ph.append({"quote": q, "quote_same_as_core": q == b["quote"],
               "ed_trans": a["trans"], "core_trans": b["trans"],
               "ed_count": ed_blank.count(re.sub(r"\s+", "", q)),
               "co_count": co_blank.count(re.sub(r"\s+", "", q))})
out["p7_phrases"] = ph
out["p7_tags_ed"] = [re.search(r"\((p\.\d+)\)", e["trans"]).group(1) if re.search(r"\((p\.\d+)\)", e["trans"]) else None for e in ed_ph]
out["p7_tags_co"] = [re.search(r"\((第\d+面)\)", e["trans"]).group(1) if re.search(r"\((第\d+面)\)", e["trans"]) else None for e in co_ph]
# P7 definition sentences: core P7 texts ending 。 that are Japanese sentences; check presence in edition
p7_def_missing = []
ed_texts = Counter(t["text"] for t in p7ed)
for t in p7co:
    s = t["text"]
    if s.endswith("。") and has_kana(s) and ed_texts.get(s, 0) < 1:
        p7_def_missing.append(s)
out["p7_def_missing"] = p7_def_missing
# P7 vocab dot lines size 20.5
def dotlines(ts): return [(t["x"], t["y"], t["text"]) for t in ts if "·" in t["text"] and t["size"] == "20.5"]
out["p7_dot_lines"] = {"ed": dotlines(p7ed), "co": dotlines(p7co)}
out["p7_vocab_headwords"] = {
    "ed": [t[2].split("·")[0].strip() for t in dotlines(p7ed)],
    "co": [t[2].split("·")[0].strip() for t in dotlines(p7co)]}

# ---------- 9. gloss P1-P6 ----------
def gloss_blocks(ts, prefix):
    blocks = []; cur = None
    for t in ts:
        if t["text"].startswith(prefix):
            if cur: blocks.append(cur)
            cur = [t]
        elif cur is not None and t["x"] == cur[0]["x"] and t["size"] == cur[0]["size"] and not t["bold"]:
            if t["fill"] == cur[0]["fill"]: cur.append(t)
            else: blocks.append(cur); cur = None
        else:
            if cur: blocks.append(cur); cur = None
    if cur: blocks.append(cur)
    return [" ".join(x["text"] for x in b) for b in blocks]
gloss = {}
for pg in ["p1", "p2", "p3", "p4", "p5", "p6"]:
    co = gloss_blocks(texts_of(CORE / FILES[pg]), "译注｜")
    ed = gloss_blocks(texts_of(ED / FILES[pg]), "Note — ")
    def items(blocks):
        res = []
        for b in blocks:
            body = b.split("｜", 1)[-1].split("—", 1)[-1] if ("｜" in b or "—" in b) else b
            res.append([p.strip() for p in body.split("·")])
        return res
    ci, ei = items(co), items(ed)
    flat_co = [x for grp in ci for x in grp]; flat_ed = [x for grp in ei for x in grp]
    def hw(it):
        # headword = leading token up to first space, except items starting with a digit run
        return it.split(" ")[0] if it else ""
    gloss[pg] = {"core_items": ci, "ed_items": ei,
                 "headwords_core": [hw(x) for x in flat_co],
                 "headwords_ed": [hw(x) for x in flat_ed],
                 "headwords_same": [hw(x) for x in flat_co] == [hw(x) for x in flat_ed],
                 "n_items": (len(flat_co), len(flat_ed))}
out["gloss"] = gloss

# ---------- 10. readers corner ----------
def sample_letter(ts):
    # sample letter: texts between Readers corner header and disclosure
    outl = []
    started = False
    for t in ts:
        if "Readers' corner" in t["text"] or "読者の手紙" in t["text"]: started = True; continue
        if started: outl.append(t["text"])
    return outl
out["readers_ed_texts"] = sample_letter(p7ed)
out["readers_co_texts"] = sample_letter(p7co)
# disclosure strings: core Chinese + Japanese disclosure fragments present in edition?
for frag in ["编辑部示例信", "非真实来信", "※この手紙は編集部の例です", "優秀作は届きませんでした"]:
    out[f"disclosure_frag_{frag[:4]}"] = {"core_p7": frag in "".join(t["text"] for t in p7co),
                                          "ed_p7": frag in "".join(t["text"] for t in p7ed)}
out["ed_disclosure_texts"] = [t["text"] for t in p7ed if "Editor's sample" in t["text"] or "No real letters" in t["text"] or "Send us your letter" in t["text"]]

# ---------- 11. essay ----------
def essay(d):
    ts = texts_of(d / "p8-tesuto.svg")
    ei = [i for i, t in enumerate(ts) if t["text"].startswith("例：")]
    seg = []
    if ei:
        for t in ts[ei[0]: ei[0] + 10]:
            if "答え ·" in t["text"]: break
            seg.append(t["text"])
    joined = "".join(seg).replace("例： ", "", 1)
    return {"segments": seg, "joined": joined,
            "len_all": len(joined),
            "len_no_space": len(re.sub(r"\s+", "", joined)),
            "len_cjk_kana": len([c for c in joined if is_cjk(c)]),
            "len_cjk_kana_digits": len([c for c in joined if is_cjk(c) or c.isdigit()])}
out["essay"] = {"core": essay(CORE), "ed": essay(ED)}

# ---------- 12. abstract ----------
ab = (B / "files/weekly-report-w45-ja-en/ABSTRACT.txt").read_text()
out["abstract"] = {"raw": ab, "newlines": ab.count("\n"), "has_ascii_quote": '"' in ab,
                   "len": len(ab), "single_line_body": len(ab.strip().splitlines()) == 1}

# ---------- 13. images + credits ----------
def img_hashes(d):
    res = {}
    for pg, fn in FILES.items():
        t = raw(d / fn); hs = []
        for m in re.finditer(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', t):
            hs.append(hashlib.sha256(m.group(1).encode()).hexdigest()[:12])
        res[pg] = hs
    return res
out["images"] = {"core": img_hashes(CORE), "ed": img_hashes(ED)}
def credits(d):
    res = {}
    for pg, fn in FILES.items():
        res[pg] = [t["text"] for t in texts_of(d / fn) if "出典" in t["text"] or "Poliphilo" in t["text"]
                   or "Syced" in t["text"] or "Kratochvil" in t["text"] or "広重" in t["text"]
                   or "Commons" in t["text"]]
    return res
out["credits"] = {"core": credits(CORE), "ed": credits(ED)}

# ---------- 14. furniture three-way ----------
def mast(d):
    ts = texts_of(d / "p1-hyoushi.svg"); m = {}
    for t in ts:
        if t["text"] == "Lucerna" and t["size"] == "168": m["wordmark_y"] = t["y"]
        if "EXPLANATIONS IN ENGLISH" in t["text"]: m["badge"] = (t["x"], t["y"], t["size"], t["text"])
        if "中文讲解" in t["text"]: m["badge_cn"] = (t["x"], t["y"], t["size"], t["text"])
    m["texts_300_400"] = [(t["y"], t["size"], t["text"]) for t in ts if 300 <= t["y"] <= 400]
    t_raw = raw(d / "p1-hyoushi.svg")
    m["lines"] = [mm.group(0)[:150] for mm in re.finditer(r'<line[^>]*>', t_raw)][:20]
    m["band_rects"] = [mm.group(0)[:150] for mm in re.finditer(r'<rect[^>]*>', t_raw)
                       if 'y="424"' in mm.group(0) or 'y="424.0"' in mm.group(0)]
    return m
out["mast"] = {k: mast(d) for k, d in [("w43", W43), ("core", CORE), ("ed", ED)]}
def footers(d):
    res = {}
    for pg, fn in FILES.items():
        res[pg] = [t["text"] for t in texts_of(d / fn) if "Lucerna ·" in t["text"] or t["text"].startswith("Page ")]
    return res
out["footers"] = {k: footers(d) for k, d in [("w43", W43), ("core", CORE), ("ed", ED)]}
def p8furn(d):
    ts = texts_of(d / "p8-tesuto.svg")
    return [t["text"] for t in ts if (t["text"].startswith("— ") and t["text"].endswith(" —"))
            or "Test and answers" in t["text"] or "Answers —" in t["text"] or "A short English note" in t["text"]]
out["p8_furn"] = {k: p8furn(d) for k, d in [("w43", W43), ("core", CORE), ("ed", ED)]}
def instr(d):
    s = set()
    for pg, fn in FILES.items():
        for t in texts_of(d / fn):
            if t["text"] in ("Fill in", "Build a sentence", "True or false?", "Match words to meanings",
                             "Match events to places and dates", "Translate", "Writing", "Match words",
                             "填空", "造句", "判断正误", "连线配对", "翻译", "写作"):
                s.add(t["text"])
    return sorted(s)
out["instr"] = {k: instr(d) for k, d in [("w43", W43), ("core", CORE), ("ed", ED)]}
def bands(d):
    res = {}
    for pg, fn in FILES.items():
        res[pg] = [t["text"] for t in texts_of(d / fn) if t["text"].startswith("レベル")][:2]
    return res
out["bands"] = {k: bands(d) for k, d in [("w43", W43), ("core", CORE), ("ed", ED)]}
# Note prefix presence
out["note_prefix"] = {"ed": sum(1 for pg, fn in FILES.items() for t in texts_of(ED / fn) if t["text"].startswith("Note — ")),
                      "w43": sum(1 for pg, fn in FILES.items() for t in texts_of(W43 / fn) if t["text"].startswith("Note — "))}

# ---------- 15. P7 teaser band + max text y ----------
for label, d in [("ed", ED), ("core", CORE)]:
    t_raw = raw(d / "p7-kotoba.svg"); rects = []
    for m in re.finditer(r'<rect[^>]*>', t_raw):
        mm = re.search(r'y="([\d.]+)"', m.group(0)); hh = re.search(r'height="([\d.]+)"', m.group(0))
        if mm and hh and float(mm.group(1)) > 2000:
            rects.append((float(mm.group(1)), float(hh.group(1)), float(mm.group(1)) + float(hh.group(1))))
    out[f"p7_bottom_rects_{label}"] = rects
    ts = texts_of(d / "p7-kotoba.svg")
    out[f"p7_max_text_y_{label}"] = max(t["y"] for t in ts if "Page 7" not in t["text"] and "Lucerna ·" not in t["text"])

# ---------- 16. geometry supplements: ADVANCE right-edge, same-baseline ink overlap, P6 chart ----------
from PIL import ImageFont
def font_for(t):
    kind = "serif" if "Serif" in t["fam"] else "sans"
    return svglib._font(kind, t["bold"], float(t["size"]))
adv_viol = {}
for pg, fn in FILES.items():
    viol = []
    for t in texts_of(ED / fn):
        f = font_for(t); adv = f.getlength(t["text"])
        if t["anchor"] == "start": right = t["x"] + adv
        elif t["anchor"] == "end": right = t["x"]
        elif t["anchor"] == "middle": right = t["x"] + adv / 2
        else: right = t["x"] + adv
        if right > 1885.5: viol.append((t["x"], t["y"], t["text"], round(right, 1)))
    adv_viol[pg] = viol
out["advance_violations"] = adv_viol
# same-baseline ink overlap (texts sharing exact y, ink boxes via getbbox anchor ls)
def ink_box(t):
    f = font_for(t)
    try: bb = f.getbbox(t["text"], anchor="ls")
    except TypeError: bb = f.getbbox(t["text"])
    if t["anchor"] == "start": ox = t["x"]
    elif t["anchor"] == "end": ox = t["x"] - (bb[2] - bb[0])
    elif t["anchor"] == "middle": ox = t["x"] - (bb[2] - bb[0]) / 2
    else: ox = t["x"]
    return (ox + bb[0], t["y"] + bb[1], ox + bb[2], t["y"] + bb[3])
samebase = {}
for pg, fn in FILES.items():
    ts = texts_of(ED / fn); by_y = {}
    for t in ts: by_y.setdefault(t["y"], []).append(t)
    coll = []
    for y, grp in by_y.items():
        if len(grp) < 2: continue
        boxes = [(t, ink_box(t)) for t in grp]
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a, b = boxes[i][1], boxes[j][1]
                if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
                    coll.append((y, boxes[i][0]["text"], boxes[j][0]["text"]))
    samebase[pg] = coll
out["same_baseline_ink_collisions"] = samebase
# P6 chart coverage (getbbox, anchor ls; bars = later rects fill #3e4c2a h=34)
p6raw = raw(ED / "p6-fukayomi.svg")
bars = []
for m in re.finditer(r'<rect[^>]*>', p6raw):
    s = m.group(0)
    if '#3e4c2a' in s and 'height="34"' in s:
        gx = re.search(r'x="([\d.]+)"', s); gy = re.search(r'y="([\d.]+)"', s)
        gw = re.search(r'width="([\d.]+)"', s)
        bars.append((float(gx.group(1)), float(gy.group(1)), float(gx.group(1)) + float(gw.group(1)), float(gy.group(1)) + 34))
chart = []
for t in texts_of(ED / "p6-fukayomi.svg"):
    if re.fullmatch(r"\d+%", t["text"]):
        ib = ink_box(t); ia = max(0, (ib[2] - ib[0]) * (ib[3] - ib[1])); mx = 0.0
        for b in bars:
            ix = max(0, min(ib[2], b[2]) - max(ib[0], b[0])); iy = max(0, min(ib[3], b[3]) - max(ib[1], b[1]))
            if ia: mx = max(mx, ix * iy / ia)
        chart.append((t["text"], t["x"], t["y"], [round(v, 4) for v in ib], round(mx, 4)))
out["p6_chart_coverage"] = {"bars": bars, "labels": chart}

# ---------- 17. extra: simplified scan, P8 note weekdays, letter join, frame fragments, vocab boxes, mast rules ----------
SIMP_ONLY = set("为说话语对发让见读这个们还电车马门问现实义头龙汉认识观点发际动劳务肃胁胆脑肠肤脚脸阴阳艺")
simp = {}
for pg, fn in FILES.items():
    co_chars = set(ch for t in texts_of(CORE / fn) for ch in t["text"])
    ed_chars = set(ch for t in texts_of(ED / fn) for ch in t["text"])
    simp[pg] = {"yi_ed_count": sum(t["text"].count("艺") for t in texts_of(ED / fn)),
                "yi_core_count": sum(t["text"].count("艺") for t in texts_of(CORE / fn)),
                "simp_only_edition_only": sorted((ed_chars & SIMP_ONLY) - co_chars),
                "simp_only_ed": sorted(ed_chars & SIMP_ONLY)}
out["simplified_scan"] = simp
JP_WEEKDAY = ["月よう日", "火よう日", "水よう日", "木よう日", "金よう日", "土よう日", "日よう日", "（周", "周日", "周六"]
out["p8_ed_note_weekday_jp"] = {n: v["line"] for n, v in ce.items()
                                if any(w in note_part(v["line"]) for w in JP_WEEKDAY)}
out["p8_ed_key_weekday_jp"] = {n: v["line"] for n, v in ce.items()
                               if any(w in split_key(v["line"]) for w in JP_WEEKDAY)}
def letter_join(d):
    ts = texts_of(d / "p7-kotoba.svg")
    hi = [i for i, t in enumerate(ts) if "Readers' corner" in t["text"] or ("読者の手紙" in t["text"] and "corner" in t["text"])]
    if not hi:
        hi = [i for i, t in enumerate(ts) if t["text"].startswith("読者の手紙")]
    i = hi[0] + 1; parts = []
    while i < len(ts) and ts[i]["text"].startswith("「") or (i < len(ts) and parts and "です。」" not in "".join(parts)):
        parts.append(ts[i]["text"]); i += 1
        if parts and "です。」" in "".join(parts): break
    return "".join(parts)
out["letter_joined"] = {"core": letter_join(CORE), "ed": letter_join(ED)}
def frame_join(d):
    ts = texts_of(d / "p7-kotoba.svg")
    hi = [i for i, t in enumerate(ts) if "今週のフレーム" in t["text"]][0]
    return "".join(t["text"] for t in ts[hi + 1: hi + 5])
out["frame_joined"] = {"core": frame_join(CORE), "ed": frame_join(ED)}
def vocab_boxes(d):
    ts = texts_of(d / "p7-kotoba.svg")
    sel = [t for t in ts if t["size"] == "20.5" and 400 <= t["y"] <= 700 and t["x"] in (65.0, 527.0, 989.0) and "·" in t["text"]]
    cont = [t for t in ts if t["size"] == "20.5" and 600 <= t["y"] <= 660 and t["x"] == 989.0 and "·" not in t["text"]]
    return {"box_lines": [(t["x"], round(t["y"], 2), t["text"]) for t in sel],
            "continuations": [t["text"] for t in cont]}
out["p7_vocab_boxes"] = {"core": vocab_boxes(CORE), "ed": vocab_boxes(ED)}
def mast_rules(d):
    t_raw = raw(d / "p1-hyoushi.svg")
    ys = []
    for m in re.finditer(r'<line[^>]*>', t_raw):
        mm = re.search(r'y1="([\d.]+)"', m.group(0))
        if mm: ys.append(float(mm.group(1)))
    return ys
out["mast_rules_y"] = {k: mast_rules(d) for k, d in [("w43", W43), ("core", CORE), ("ed", ED)]}
def p7band(d):
    return [t["text"] for t in texts_of(d / "p7-kotoba.svg") if t["text"].startswith("言語フォーカス")]
out["p7_band"] = {k: p7band(d) for k, d in [("w43", W43), ("core", CORE), ("ed", ED)]}
def match_events_loc(d):
    return [(pg, t["text"]) for pg, fn in FILES.items() for t in texts_of(d / fn)
            if t["text"] == "Match events to places and dates"]
out["match_events_loc"] = match_events_loc(ED)
def match_events_core(d):
    # core counterpart: find exercise whose instruction region matches - dump P8 matching section headers in core
    return [(pg, t["text"]) for pg, fn in FILES.items() for t in texts_of(d / fn)
            if t["text"] in ("连线配对", "配对")]
out["match_events_core_counterparts"] = match_events_core(CORE)

json.dump(out, open(PROOF / "proof2.json", "w"), ensure_ascii=False, indent=1)
print("scope changed:", scope["changed"])
print("scope unchanged n:", len(scope["unchanged"]), "missing:", scope["missing_in_prefix"])
print("buildtree changed:", [k for k, v in bt.items() if v["changed"]])
print("svglib md5:", out["svglib_md5"])
print("forbidden:", out["forbidden_svg-ed"], out["forbidden_kit"], out["forbidden_abstract"])
print("kinsoku std:", {k: v[0] for k, v in out["kinsoku"].items() if k.endswith("_std")})
print("kinsoku wide:", {k: v[0] for k, v in out["kinsoku"].items() if k.endswith("_wide")})
print("freeze:", out["freeze_pages"])
print("counts:", out["counts"], "total:", out["counts_total"])
print("p8 counts:", out["p8_counts"], "identical:", out["p8_identical_lines"])
print("p8 printed diff keys:", sorted(keydiff_detail.keys()))
print("p8 note cjk:", note_cjk)
print("trend:", trend)
print("advance viol:", {k: len(v) for k, v in adv_viol.items()})
print("samebase coll:", {k: len(v) for k, v in samebase.items()})
print("p6 chart:", chart)
print("p7 phrases:", [(p["quote"][:12], p["ed_count"], p["co_count"]) for p in ph])
print("p7 tags ed:", out["p7_tags_ed"], "co:", out["p7_tags_co"])
print("p7 def missing:", p7_def_missing)
print("p7 vocab ed:", out["p7_vocab_headwords"]["ed"], "co:", out["p7_vocab_headwords"]["co"])
print("gloss:", {k: v["n_items"] for k, v in gloss.items()}, "headwords_same:", {k: v["headwords_same"] for k, v in gloss.items()})
print("essay core==ed segments:", essay(CORE)["segments"] == essay(ED)["segments"], essay(ED))
print("essay counts ed:", {k: essay(ED)[k] for k in ["len_all","len_no_space","len_cjk_kana","len_cjk_kana_digits"]})
print("abstract:", out["abstract"])
print("images equal:", out["images"]["core"] == out["images"]["ed"])
print("credits equal:", out["credits"]["core"] == out["credits"]["ed"])
print("p7 teaser ed:", out["p7_bottom_rects_ed"], "max y:", out["p7_max_text_y_ed"])
print("corrosion jp-jp:", out["corrosion_jp_jp"])
print("gloss headwords_same:", {k: v["headwords_same"] for k, v in gloss.items()})
print("gloss headwords core vs ed:")
for k, v in gloss.items(): print(" ", k, v["headwords_core"], "||", v["headwords_ed"])
print("simplified:", simp)
print("p8 note weekday jp:", out["p8_ed_note_weekday_jp"])
print("p8 key weekday jp:", out["p8_ed_key_weekday_jp"])
print("letter joined equal:", out["letter_joined"]["core"] == out["letter_joined"]["ed"], out["letter_joined"])
print("frame joined equal:", out["frame_joined"]["core"] == out["frame_joined"]["ed"], out["frame_joined"])
print("vocab boxes ed:", out["p7_vocab_boxes"]["ed"], "core:", out["p7_vocab_boxes"]["core"])
print("mast rules:", out["mast_rules_y"])
print("p7 band:", out["p7_band"])
print("match events loc:", out["match_events_loc"], "core counterparts:", out["match_events_core_counterparts"])
print("final maru missing:", {k: len(v) for k, v in fmiss.items()})
print("freeze scope vs preproof (nonempty only):")
for k, v in scope_str.items():
    extras = {kk: vv for kk, vv in v.items() if vv}
    if extras: print(" ", k, extras)
