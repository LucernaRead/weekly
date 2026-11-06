#!/usr/bin/env python3
# Independent proof2 analysis for JA×DE W45. Reads delivery + core + W43 only.
import sys, os, re, json, hashlib, base64
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/tools")
import p8 as P8
import occlusion_audit as OA

B = "/home/hatch/workspace/goals/lucernaread-social-media-operations"
ED = B + "/files/weekly-report-w45-ja-de/svg"
CORE = B + "/files/weekly-report-w45-ja-core/svg"
W43 = B + "/files/weekly-report-ja-de/svg"
OUT = B + "/hidden_files/w45/ja-de-proof2"
PAGES = ["p1-hyoushi.svg","p2-kurashi.svg","p3-bunka.svg","p4-supotsu.svg",
         "p5-wakamono.svg","p6-fukayomi.svg","p7-kotoba.svg","p8-tesuto.svg"]

def texts_of(path):
    return P8.load_texts(path)
def els_of(path):
    # parse via OA tag regex for attrs
    s = open(path, encoding="utf-8").read()
    out = []
    for m in OA.TAG_RE.finditer(s):
        if m.group("tattrs") is not None:
            a = OA.parse_attrs(m.group("tattrs"))
            out.append(("text", a, re.sub(r"<[^>]+>", "", m.group("tcontent"))))
        else:
            out.append((m.group("tag"), OA.parse_attrs(m.group("attrs") or ""), ""))
    return out

CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uff00-\uffef]")
res = {}

# ---- 1. P8 segments identical count + keydiff table ----
core_p8, _ = P8.extract(CORE + "/p8-tesuto.svg", 150)
ed_p8, _ = P8.extract(ED + "/p8-tesuto.svg", 150)
ident = [n for n in range(1, 151) if P8.norm(core_p8[n]["seg"]) == P8.norm(ed_p8[n]["seg"])]
res["p8_identical_segments"] = ident
res["p8_how"] = {"core": core_p8["_how"], "ed": ed_p8["_how"]}
# true printed key: for dash lines, part before first " — "; for paren lines, part before last paren group at end
def true_key(seg):
    seg = seg.strip()
    if seg.startswith("✓"): return "✓"
    if " — " in seg:
        k = seg.split(" — ", 1)[0].strip()
        # dash key itself must not contain a trailing paren note start confusion: if k ends with paren group, strip it
        return k
    g = P8.last_paren_group(seg)
    if g: return seg[:g[0]].strip()
    return seg
kd = []
for n in P8.compare(CORE + "/p8-tesuto.svg", ED + "/p8-tesuto.svg", 150)[0]["keydiff"]:
    kd.append({"n": n, "core_seg": core_p8[n]["seg"], "ed_seg": ed_p8[n]["seg"],
               "core_extracted_key": core_p8[n]["key"], "ed_extracted_key": ed_p8[n]["key"],
               "core_true_key": true_key(core_p8[n]["seg"]), "ed_true_key": true_key(ed_p8[n]["seg"]),
               "core_method": core_p8[n]["method"], "ed_method": ed_p8[n]["method"],
               "core_has_note": core_p8[n]["has_note"], "ed_has_note": ed_p8[n]["has_note"]})
res["p8_keydiff_table"] = kd
# P8 note language: every ed segment's note part (after first ' — ' or paren) contains CJK? classify: note contains simplified-Chinese-only chars?
# Instead: check each ed seg for presence of the core Chinese note verbatim, and list ed segs whose note part contains CJK chars that are NOT in core Japanese text
core_all_cjk = set()
for p in PAGES:
    for t in texts_of(CORE + "/" + p): core_all_cjk |= set(CJK.findall(t))
p8_note_cjk = {}
for n in range(1, 151):
    seg = ed_p8[n]["seg"]
    note = seg.split(" — ", 1)[1] if " — " in seg else seg
    p8_note_cjk[n] = sorted(set(CJK.findall(note)))
res["p8_ed_note_cjk_chars"] = {str(k): v for k, v in p8_note_cjk.items() if v}
# P8 dash count
def dash_count(path):
    ts = texts_of(path)
    return sum(1 for t in ts if " — " in t and re.match(r"^\d+\.\s", t.strip()))
res["p8_dash_lines"] = {"ed": dash_count(ED + "/p8-tesuto.svg"), "core": dash_count(CORE + "/p8-tesuto.svg")}

# ---- 2. Freeze diff adjudication ----
fd = json.load(open(OUT + "/freeze-diff.json"))
res["freeze_pages"] = {}
for pg in "12345678":
    d = fd["pages"][pg]
    res["freeze_pages"][pg] = {"added_distinct": len(d["added_strings"]),
        "removed_distinct": len(d["removed_strings"]),
        "added_total": sum(s["count"] for s in d["added_strings"]),
        "removed_total": sum(s["count"] for s in d["removed_strings"]),
        "cjk_core": d["cjk_core_total"], "cjk_ed": d["cjk_edition_total"],
        "cjk_added": d.get("cjk_added", {})}
# removed-string adjudication: kana-bearing removed strings whose kana runs survive in edition page
KANA = re.compile(r"[\u3040-\u30ff]+")
for pg, fname in zip("12345678", PAGES):
    ed_text = "\n".join(texts_of(ED + "/" + fname))
    ed_joined = re.sub(r"\s+", "", ed_text)
    cats = {"pure_no_kana": 0, "kana_runs_survive": 0, "kana_runs_not_survive": [], "p8_note": 0}
    for s in fd["pages"][pg]["removed_strings"]:
        t = s["text"]
        if pg == "8":
            cats["p8_note"] += 1; continue
        kana_runs = KANA.findall(t)
        if not kana_runs: cats["pure_no_kana"] += 1
        elif all(re.sub(r"\s+", "", r) in ed_joined for r in kana_runs): cats["kana_runs_survive"] += 1
        else: cats["kana_runs_not_survive"].append(t)
    res["freeze_pages"][pg]["removed_adjudication"] = cats
# added CJK chars subset of core CJK set, per page
for pg, fname in zip("12345678", PAGES):
    added_cjk = set()
    for s in fd["pages"][pg]["added_strings"]: added_cjk |= set(CJK.findall(s["text"]))
    res["freeze_pages"][pg]["added_cjk_distinct"] = sorted(added_cjk)
    res["freeze_pages"][pg]["added_cjk_not_in_core"] = sorted(added_cjk - core_all_cjk)

# ---- 3. Bare string + apparatus + forbidden ----
APP = ["练习","答案","对照第","范文","本期目录","头条","即学即练","本周单词","数字看本周",
 "闪电问答","快讯","译注","第1版","共8版","练习与答案","中文简析","按版面分页","下期预告",
 "本周金句","本周句式","易错诊所","三个级别","练习数据","读图表","把词和释义配对","填空",
 "造句","判断","翻译","写作","一锅菜","蒸笼","集市","工艺","陶瓷","染色","罚款","变装",
 "雕像","节日","周末","话题","预算","满足","观测","说说你自己","本周","读者园地","参考答案","详见第"]
res["apparatus"] = {}
for fname in PAGES:
    s = open(ED + "/" + fname, encoding="utf-8").read()
    hits = {w: s.count(w) for w in APP if w in s}
    res["apparatus"][fname] = hits
res["bare_string_counts"] = {f: open(ED + "/" + f, encoding="utf-8").read().count("工艺展到11月8日") for f in PAGES}
res["forbidden"] = {}
for label, path in [("svg_ed", ED), ("kit", B + "/files/weekly-report-w45-ja-de/WEEKLY-KIT.md"),
                    ("abstract", B + "/files/weekly-report-w45-ja-de/ABSTRACT.txt")]:
    if os.path.isdir(path):
        tot = {w: 0 for w in ["桥接", "橋接"]}
        for f in PAGES:
            s = open(path + "/" + f, encoding="utf-8").read()
            for w in tot: tot[w] += s.count(w)
        res["forbidden"][label] = tot
    else:
        s = open(path, encoding="utf-8").read()
        res["forbidden"][label] = {w: s.count(w) for w in ["桥接", "橋接"]}
res["svglib_md5"] = {}
for label, path in [("ed_build", B + "/hidden_files/weekly-report-w45-ja-de-build/svglib.py"),
                    ("core_build", B + "/hidden_files/weekly-report-w45-ja-build/svglib.py")]:
    res["svglib_md5"][label] = hashlib.md5(open(path, "rb").read()).hexdigest()

# ---- 4. Kinsoku + P1 top band ----
NO_START = set("。、，．！？：；）」』】ー…‥・") | set("ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮ")
EXT = NO_START | set(")]}.,!?%:;\"'") | set("ヵヶ")
res["kinsoku"] = {}
for fname in PAGES:
    els = els_of(ED + "/" + fname)
    per_text = [t for _, a, t in els if t and t[0] in NO_START]
    per_text_ext = [t for _, a, t in els if t and t[0] in EXT]
    # per-line: group by exact y, sort by x, concat
    lines = {}
    for _, a, t in els:
        if t: lines.setdefault(a.get("y"), []).append((float(a.get("x", 0)), t))
    line_first = []
    for y, items in lines.items():
        s = "".join(t for _, t in sorted(items))
        s2 = s.lstrip()
        if s2 and s2[0] in NO_START: line_first.append((y, s2[:40]))
    line_first_ext = []
    for y, items in lines.items():
        s = "".join(t for _, t in sorted(items)).lstrip()
        if s and s[0] in EXT: line_first_ext.append((y, s[:40]))
    res["kinsoku"][fname] = {"per_text": per_text, "per_text_ext": per_text_ext,
                             "per_line": line_first, "per_line_ext": line_first_ext}
# P1 top band y=92
def topband(path):
    out = []
    for kind, a, t in els_of(path):
        if kind == "text" and a.get("y") == "92":
            fam = a.get("font-family", ""); size = float(a.get("font-size", 20))
            bold = a.get("font-weight", "") in ("700", "bold")
            box = OA.ink_box(t, fam, size, bold, float(a["x"]), 92.0, a.get("text-anchor", "start"))
            out.append({"text": t, "x": a["x"], "anchor": a.get("text-anchor", "start"), "box": box})
    return out
res["p1_topband"] = {"ed": topband(ED + "/p1-hyoushi.svg"), "core": topband(CORE + "/p1-hyoushi.svg")}

# ---- 5. English residue ----
LATIN = re.compile(r"[A-Za-zÄÖÜäöüß]+(?:['\-][A-Za-zÄÖÜäöüß]+)*")
tokens = {}
for fname in PAGES:
    for t in texts_of(ED + "/" + fname):
        for tok in LATIN.findall(t):
            tokens.setdefault(tok, 0)
            tokens[tok] += 1
res["latin_tokens"] = dict(sorted(tokens.items()))
res["sunday_count"] = sum(open(ED + "/" + f, encoding="utf-8").read().count("(Sunday)") for f in PAGES)
sonntag = []
for fname in PAGES:
    for t in texts_of(ED + "/" + fname):
        if "(Sonntag)" in t: sonntag.append((fname, t))
res["sonntag_contexts"] = sonntag
EN_DAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
EN_MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]
res["en_day_month_hits"] = {w: sum(open(ED + "/" + f, encoding="utf-8").read().count(w) for f in PAGES) for w in EN_DAYS + EN_MONTHS}

# ---- 6. P7 ----
ed7 = texts_of(ED + "/p7-kotoba.svg"); core7 = texts_of(CORE + "/p7-kotoba.svg")
res["p7_common_definition_check"] = {}
# definition frame: texts containing ゆるく整える or clinic markers
for needle in ["ゆるく整える", "昨日", "診所", "Fehlerklinik"]:
    res["p7_common_definition_check"][needle] = {"in_core": sum(1 for t in core7 if needle in t),
                                                 "in_ed": sum(1 for t in ed7 if needle in t)}
# page tags sequence: order of (第N面) in core vs (S.N) in ed within full P7 text order
res["p7_tags"] = {"core": re.findall(r"第\d面", " ".join(core7)), "ed": re.findall(r"S\.\d", " ".join(ed7))}
# golden sentences: derive from core P7 Sätze section? Use the 8 known from core text: find sentences that appear in core P7 list area.
# Instead: count the 8 sentences (taken from core full text, verified present in core P7) in whitespace-stripped full texts
GOLD = ["文化の日は、11月3日（火よう日）です。","ゆっくり、ゆるく整える日本の11月です。",
        "『ゆる』は、無理をしない、ゆっくり、という意味です。","鍋の材料が1か月早く並び始めました。",
        "伝統工芸と紅葉と光を、いっしょに楽しむことができます。","ソフトバンクが2連勝でスタートしました。",
        "ルールを守って、楽しいハロウィンにしましょう。","紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。"]
def full_stripped(d):
    all_t = []
    for f in PAGES: all_t.extend(texts_of(d + "/" + f))
    return re.sub(r"\s+", "", " ".join(all_t))
fc, fe = full_stripped(CORE), full_stripped(ED)
res["golden"] = {g: {"core": fc.count(re.sub(r"\s+", "", g)), "ed": fe.count(re.sub(r"\s+", "", g))} for g in GOLD}
res["golden_in_core_p7"] = {g: sum(1 for t in core7 if g in t) for g in GOLD}
# P7 teaser rect
for label, d in [("ed", ED), ("core", CORE)]:
    rects = [(a.get("x"), a.get("y"), a.get("width"), a.get("height")) for kind, a, t in els_of(d + "/p7-kotoba.svg") if kind == "rect"]
    res.setdefault("p7_rects", {})[label] = [r for r in rects if r[0] == "65" and float(r[1]) > 2300]
# P7 definition sentences verbatim: all core P7 texts that are definition-ish (contain 『ゆる) present in ed?
res["p7_def_lines_core_in_ed"] = [t for t in core7 if "ゆるく整える" in t and t in ed7]
res["p7_def_lines_core_total"] = [t for t in core7 if "ゆるく整える" in t]
# P7 explanation-localization count proxy: clinic explanation lines in ed that are German (contain German words) vs core Chinese ones - list ed P7 texts containing 'Mit 「'
res["p7_mit_lines"] = [t for t in ed7 if "Mit 「" in t or "Zerlegung" in t]

# ---- 7. Geometry extras ----
# ADVANCE scan per page
def advance_scan(path):
    worst = 0.0; worst_t = ""; viol = []
    for kind, a, t in els_of(path):
        if kind != "text" or not t.strip(): continue
        fam = a.get("font-family", ""); size = float(a.get("font-size", 20))
        bold = a.get("font-weight", "") in ("700", "bold")
        f = OA.get_font(fam, size, bold)
        adv = f.getlength(t) / OA.SCALE
        x = float(a["x"]); anch = a.get("text-anchor", "start")
        right = x + adv if anch == "start" else (x + adv / 2 if anch == "middle" else x)
        if right > worst: worst, worst_t = right, t
        if right > 1885.5: viol.append((t, right))
    return {"max_adv_right": round(worst, 2), "max_text": worst_t, "violations_over_1885_5": viol}
res["advance"] = {f: advance_scan(ED + "/" + f) for f in PAGES}
# P8 non-footer ink bottom: texts with baseline y < 2580, excluding footer band texts (baseline 2624)
def ink_bottom(path, ymax_baseline=2580):
    mx = 0.0; mt = ""
    for kind, a, t in els_of(path):
        if kind != "text" or not t.strip(): continue
        y = float(a["y"])
        if y >= ymax_baseline: continue
        box = OA.ink_box(t, a.get("font-family", ""), float(a.get("font-size", 20)),
                         a.get("font-weight", "") in ("700", "bold"), float(a["x"]), y, a.get("text-anchor", "start"))
        if box and box[3] > mx: mx, mt = box[3], t
    return {"max_ink_bottom": round(mx, 2), "text": mt}
res["p8_ink_bottom"] = ink_bottom(ED + "/p8-tesuto.svg")
res["p7_teaser_ink"] = ink_bottom(ED + "/p7-kotoba.svg")
# P6 chart coverage baseline-anchored
els6 = els_of(ED + "/p6-fukayomi.svg")
labels = [(a, t) for kind, a, t in els6 if kind == "text" and (t.strip() in ("近場の満足","温泉","紅葉","グルメ","38%","27%","21%","14%") or "近場" in t or t.strip() in ("38%","27%","21%","14%"))]
# simpler: all texts on P6 containing those substrings
lab = []
for kind, a, t in els6:
    if kind == "text" and any(s in t for s in ["近場の満足","温泉","紅葉","グルメ"]) or (kind == "text" and t.strip() in ("38%","27%","21%","14%")):
        lab.append((a, t))
rects6 = [(i, a) for i, (kind, a, t) in enumerate(els6) if kind == "rect"]
def ink_box_ls(a, t):
    fam = a.get("font-family", ""); size = float(a.get("font-size", 20))
    bold = a.get("font-weight", "") in ("700", "bold")
    f = OA.get_font(fam, size, bold)
    asc, desc = f.getmetrics()[0] / OA.SCALE, f.getmetrics()[1] / OA.SCALE
    adv = f.getlength(t) / OA.SCALE
    l, tt, r, b = [v / OA.SCALE for v in f.getbbox(t)]
    x = float(a["x"]); y = float(a["y"]); anch = a.get("text-anchor", "start")
    left = x + l if anch == "start" else (x - adv / 2 + l if anch == "middle" else x - adv + l)
    right = x + r if anch == "start" else (x - adv / 2 + r if anch == "middle" else x - adv + r)
    return (left, y - asc + tt, right, y - asc + b)
cov = []
for a, t in lab:
    ib = ink_box_ls(a, t)
    area = max(0.0, ib[2] - ib[0]) * max(0.0, ib[3] - ib[1])
    # later-drawn opaque rects (fill not none) overlapping
    idx = [i for i, (kind, aa, tt) in enumerate(els6) if kind == "text" and aa is a]
    # find position of this text in els6
    pos = next(i for i, (kind, aa, tt) in enumerate(els6) if kind == "text" and tt == t and aa.get("x") == a.get("x") and aa.get("y") == a.get("y"))
    ov = 0.0
    for kind, aa, tt in els6[pos+1:]:
        if kind != "rect": continue
        fill = aa.get("fill", "")
        if fill in ("none", ""): continue
        rx, ry, rw, rh = float(aa.get("x", 0)), float(aa.get("y", 0)), float(aa.get("width", 0)), float(aa.get("height", 0))
        ix = max(0.0, min(ib[2], rx + rw) - max(ib[0], rx)); iy = max(0.0, min(ib[3], ry + rh) - max(ib[1], ry))
        ov += ix * iy
    cov.append({"text": t, "ink_box": [round(v, 1) for v in ib], "coverage_pct": round(100 * ov / area, 2) if area else 0})
res["p6_chart_coverage"] = cov

# ---- 8. Images ----
def images(d):
    out = {}
    for f in PAGES:
        s = open(d + "/" + f, encoding="utf-8").read()
        imgs = re.findall(r"<image[^>]*>", s)
        det = []
        for im in imgs:
            attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', im))
            href = attrs.get("href", attrs.get("xlink:href", ""))
            payload = href.split(",", 1)[1] if "," in href else href
            det.append({"x": attrs.get("x"), "y": attrs.get("y"), "width": attrs.get("width"),
                        "height": attrs.get("height"), "sha16": hashlib.sha256(base64.b64decode(payload)).hexdigest()[:16] if payload else None})
        out[f] = det
    return out
res["images"] = {"ed": images(ED), "core": images(CORE)}

# ---- 9. Readers corner ----
ed7els = els_of(ED + "/p7-kotoba.svg"); core7els = els_of(CORE + "/p7-kotoba.svg")
res["readers_letter_ed"] = [t for _, a, t in ed7els if "こんにちは" in t or "読者の手紙の例" in t or "図書館で本を" in t]
res["readers_letter_core"] = [t for _, a, t in core7els if "こんにちは" in t or "読者の手紙の例" in t or "図書館で本を" in t]
res["readers_disclosure_ed"] = [t for _, a, t in ed7els if "Beispielbrief" in t or "Redaktionsschluss" in t or "Schickt uns" in t]
res["readers_disclosure_core_jp"] = [t for _, a, t in core7els if "編集部の例" in t or "届きませんでした" in t]
res["readers_teaser_ed"] = [t for _, a, t in ed7els if "第8版の作文" in t]

# ---- 10. Furniture / W43 ----
def masthead(d):
    els = els_of(d + "/p1-hyoushi.svg")
    out = {}
    for kind, a, t in els:
        if kind != "text": continue
        if t.strip() == "Lucerna" and float(a.get("font-size", 0)) > 50: out["wordmark_y"] = a.get("y")
        if "VOL." in t and "Lucerna" in t: out["edition_line"] = (a.get("y"), t)
        if "JAPANISCHER TEXT" in t or "日语周报" in t or "JAPANESE WEEKLY" in t: out["badge_or_edline"] = (a.get("y"), t, a.get("fill"))
    # rects / lines
    for kind, a, t in els:
        if kind == "rect" and a.get("x") == "52": out.setdefault("dark_band", (a.get("y"), a.get("height")))
    return out
res["masthead"] = {"ed": masthead(ED), "core": masthead(CORE), "w43": masthead(W43)}
def footers(d):
    out = {}
    for f in PAGES:
        ts = texts_of(d + "/" + f)
        out[f] = [t for t in ts if ("von 8" in t or "共 8 版" in t or "WOCHENZEITUNG" in t or "日语周报" in t)]
    return out
res["footers"] = {"ed": footers(ED), "w43": footers(W43)}
def badge_count(d):
    return sum(open(d + "/" + f, encoding="utf-8").read().count("#a4553a") for f in [PAGES[0]])
res["badge_a4553a_p1"] = {"ed": badge_count(ED), "w43": badge_count(W43), "core": badge_count(CORE)}
res["uebungen"] = {}
for f in PAGES[1:6]:
    res["uebungen"][f] = [t for t in texts_of(ED + "/" + f) if "Übungen Seite" in t]
res["gloss_prefix"] = {}
for label, d in [("ed", ED), ("w43", W43)]:
    anm = hin = 0
    for f in PAGES:
        for t in texts_of(d + "/" + f):
            if t.startswith("Anm. — ") or "Anm. — " in t[:12]: anm += 1
            if "HINWEIS" in t: hin += 1
    res["gloss_prefix"][label] = {"Anm": anm, "HINWEIS": hin}
# W43 P8 style: dash lines count + paren style sample
res["w43_p8_dash"] = dash_count(W43 + "/p8-tesuto.svg")
res["w43_p8_sample"] = [t for t in texts_of(W43 + "/p8-tesuto.svg") if re.match(r"^\d+\.\s", t.strip())][:3]

# ---- 11. ABSTRACT / KIT / PDF ----
ab = open(B + "/files/weekly-report-w45-ja-de/ABSTRACT.txt", encoding="utf-8").read()
res["abstract"] = {"chars": len(ab.rstrip("\n")), "lines": ab.count("\n"), "has_ascii_quote": '"' in ab,
                   "text": ab.strip()}
kit = open(B + "/files/weekly-report-w45-ja-de/WEEKLY-KIT.md", encoding="utf-8").read()
res["kit_checks"] = {
  "has_fresh_proof_note": "fresh, complete proofread" in kit,
  "has_fix_complete_only": "Fix-complete only" in kit or "fix-complete only" in kit,
  "print_bytes_claim": "28,802,945" in kit, "web_bytes_claim": "3,100,274" in kit,
  "print_sha_claim": "a15cf7cf31c8d42b858b9ce622c10afbeabbb80c2d6bf9699cf57dbbe52e72b6" in kit,
  "web_sha_claim": "1639dd388fd9631f3ac53e0e282028ce7140b72b69c26ff796b6f55824219209" in kit,
  "keydiff_correction": "artifacts 17" in kit or "wrongly said" in kit,
  "round2_overstatement_note": "149 German + 1 Chinese" in kit or "149 German" in kit,
}
try:
    from pypdf import PdfReader
    for label, path in [("print", B + "/files/weekly-report-w45-ja-de/Lucerna-VOL2-DE.pdf"),
                        ("web", B + "/files/weekly-report-w45-ja-de/Lucerna-VOL2-DE-web.pdf")]:
        r = PdfReader(path)
        res.setdefault("pdf", {})[label] = {"pages": len(r.pages), "bytes": os.path.getsize(path)}
except Exception as e:
    res["pdf_error"] = str(e)
# model recount from printed P8 H section: lines starting with 例：? find model lines in ed P8 after '私の11月の週末' heading
p8texts = texts_of(ED + "/p8-tesuto.svg")
# model: texts after the one containing '私の11月の週末』について' - collect following texts until footer? Print candidates
res["model_candidates"] = [t for t in p8texts if "私の11月の週末は" in t or "文化と紅葉の週末" in t]

json.dump(res, open(OUT + "/analysis.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("p8 identical:", ident)
print("keydiff n:", [k["n"] for k in kd])
print("freeze:", {k: (v["added_distinct"], v["removed_distinct"], v["cjk_core"], v["cjk_ed"]) for k, v in res["freeze_pages"].items()})
print("bare:", res["bare_string_counts"])
print("forbidden:", res["forbidden"])
print("svglib:", res["svglib_md5"])
print("kinsoku nonzero:", {k: v for k, v in res["kinsoku"].items() if v["per_text"] or v["per_line"] or v["per_text_ext"] or v["per_line_ext"]})
print("p1 topband ed:", res["p1_topband"]["ed"])
print("sunday:", res["sunday_count"], "sonntag:", res["sonntag_contexts"])
print("en_day_month nonzero:", {k: v for k, v in res["en_day_month_hits"].items() if v})
print("golden:", res["golden"])
print("tags:", res["p7_tags"])
print("advance:", {k: v["max_adv_right"] for k, v in res["advance"].items()})
print("p8 ink bottom:", res["p8_ink_bottom"])
print("p6 coverage:", res["p6_chart_coverage"])
print("images ed:", res["images"]["ed"])
print("images core:", res["images"]["core"])
print("footers ed p1:", res["footers"]["ed"][PAGES[0]])
print("masthead:", res["masthead"])
print("gloss:", res["gloss_prefix"], "uebungen:", res["uebungen"])
print("abstract:", res["abstract"])
print("kit:", res["kit_checks"])
print("pdf:", res.get("pdf"))
print("apparatus nonzero:", {k: v for k, v in res["apparatus"].items() if v})
print("removed adjudication:", {k: v["removed_adjudication"] for k, v in res["freeze_pages"].items()})
print("added_cjk_not_in_core:", {k: v["added_cjk_not_in_core"] for k, v in res["freeze_pages"].items()})
print("p8 dash:", res["p8_dash_lines"], "w43 dash:", res["w43_p8_dash"])
print("disclosure ed:", res["readers_disclosure_ed"])
print("letter ed:", res["readers_letter_ed"])
print("letter core:", res["readers_letter_core"])
print("teaser ed:", res["readers_teaser_ed"])
print("p7 rects ed:", res["p7_rects"]["ed"])
print("model candidates:", res["model_candidates"])
print("latin token count:", len(res["latin_tokens"]))
