#!/usr/bin/env python3
"""Round 2 independent re-derivation for 2026-w46-zh-cn-es. No edition files touched."""
import re, os, json, html, collections
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/zh-cn-proofread-gates-round2")
ES = os.path.join(BASE, "weekly-report-w46-zh-cn-es", "svg")
CORE = os.path.join(BASE, "weekly-report-w46-zh-cn-core", "svg")
PAGES = ["p1-touiban.svg","p2-shenghuo.svg","p3-wenhua.svg","p4-tiyu.svg",
         "p5-qingnian.svg","p6-shendu.svg","p7-ciyu.svg","p8-ceyan.svg"]
TEXT_RE = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)
def nodes(d, p):
    s = open(os.path.join(d, p), encoding="utf-8").read()
    out = []
    for m in TEXT_RE.finditer(s):
        attrs = m.group(1)
        txt = html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        x = re.search(r'x="([0-9.\-]+)"', attrs); y = re.search(r'y="([0-9.\-]+)"', attrs)
        fill = re.search(r'fill="([^"]+)"', attrs)
        out.append({"page": p, "x": float(x.group(1)) if x else None,
                    "y": float(y.group(1)) if y else None, "text": txt,
                    "fill": fill.group(1) if fill else None, "attrs": attrs})
    return out, s
def allnodes(d):
    res = {}
    for p in PAGES:
        res[p], _ = nodes(d, p)
    return res

es = allnodes(ES); core = allnodes(CORE)
flat = [n for p in PAGES for n in es[p]]

# --- 1. Orphan discriminated scan ---
digitdot = [n for n in flat if re.fullmatch(r"\d+\.", n["text"].strip())]
singledigit = [n for n in flat if re.fullmatch(r"\d\.", n["text"].strip())]
colstarts = {65.0, 527.0, 989.0, 1451.0}
orphan_candidates = [n for n in singledigit if n["x"] in colstarts]
ex_x = {137.0, 599.0, 1061.0, 1523.0}
outside_ex = [n for n in digitdot if n["x"] not in ex_x]
# ranges like "25–28."
ranges = [n for n in flat if re.fullmatch(r"\d+[–\-]\d+\.", n["text"].strip())]
secC = [n for n in flat if "Responde con fechas" in n["text"]]
old = [n for n in flat if "de la página 3." in n["text"] or "de la página 5." in n["text"]]
shortfrag = [n for n in flat if n["x"] in colstarts and len(n["text"].strip()) <= 3]
def find_num(dnodes, num):
    return [n for p in PAGES for n in dnodes[p] if n["text"].strip() == f"{num}."]
orphan = {"digitdot_nodes": [(n["page"], n["x"], n["y"], n["text"]) for n in digitdot],
          "singledigit_nodes": [(n["page"], n["x"], n["y"], n["text"]) for n in singledigit],
          "orphan_candidates_colstart": [(n["page"], n["x"], n["y"], n["text"]) for n in orphan_candidates],
          "digitdot_outside_exercise_x": [(n["page"], n["x"], n["y"], n["text"]) for n in outside_ex],
          "range_nodes": [(n["page"], n["x"], n["y"], n["text"]) for n in ranges],
          "sectionC_nodes": [(n["page"], n["x"], n["y"], n["text"]) for n in secC],
          "old_wording_nodes": [(n["page"], n["x"], n["y"], n["text"]) for n in old],
          "short_fragments_colstart": [(n["page"], n["x"], n["y"], n["text"]) for n in shortfrag],
          "ex39_es": [(n["page"], n["x"], n["y"]) for n in find_num(es, 39)],
          "ex39_core": [(n["page"], n["x"], n["y"]) for n in find_num(core, 39)],
          "ex75_es": [(n["page"], n["x"], n["y"]) for n in find_num(es, 75)],
          "ex75_core": [(n["page"], n["x"], n["y"]) for n in find_num(core, 75)]}

# --- 2. Counts: chips (bare + ranges expanded) and level tags ---
def counts(dnodes):
    perpage, levels = {}, collections.Counter()
    for p in PAGES:
        nums = set()
        for n in dnodes[p]:
            t = n["text"].strip()
            if t in ("A2", "B1", "B2"):
                levels[t] += 1
            m = re.fullmatch(r"(\d+)\.", t)
            if m: nums.add(int(m.group(1)))
            m2 = re.fullmatch(r"(\d+)[–\-](\d+)\.", t)
            if m2:
                for k in range(int(m2.group(1)), int(m2.group(2)) + 1): nums.add(k)
        perpage[p] = sorted(nums)
    allnums = sorted(set().union(*perpage.values()))
    return {"levels": dict(levels), "per_page_counts": {p: len(v) for p, v in perpage.items()},
            "per_page_numbers": perpage, "total_unique": len(allnums),
            "missing": [n for n in range(1, 151) if n not in allnums],
            "extra": [n for n in allnums if n < 1 or n > 150],
            "dupes_bare": [k for k, v in collections.Counter(
                int(re.fullmatch(r"(\d+)\.", n["text"].strip()).group(1))
                for p in PAGES for n in dnodes[p] if re.fullmatch(r"\d+\.", n["text"].strip())).items() if v > 1]}

# --- 3. P7 phrases: joined + per-page, contiguity ---
PHRASES = ["双11的正日子","先看结算页，再决定买不买","提高自防自救能力","三支队进了八强",
           "输了就回家","老电影，新画面","快递的高峰分三波","着火了不坐电梯"]
def phrase_check(dnodes):
    out = {}
    for ph in PHRASES:
        per = {}
        for p in PAGES:
            joined = "".join(n["text"] for n in dnodes[p])
            per[p] = joined.count(ph)
        out[ph] = {"total": sum(per.values()), "per_page": per}
    return out

# --- 4. P6 chart ---
def chart():
    s = open(os.path.join(ES, "p6-shendu.svg"), encoding="utf-8").read()
    rects = []
    for r in re.findall(r"<rect[^>]*>", s):
        def g(k):
            m = re.search(k + r'="([\d.]+)"', r); return float(m.group(1)) if m else None
        f = re.search(r'fill="([^"]+)"', r)
        rects.append({"x": g("x"), "y": g("y"), "w": g("width"), "h": g("height"),
                      "fill": f.group(1) if f else None})
    bars = [r for r in rects if r["h"] == 30.0 and r["x"] == 325.0]
    return {"all_rects_h30_x325": bars, "n_rects_total": len(rects)}

# --- 5. Kinsoku ---
NO_START = set("，。、；：？！）］｝》」』】ぁぃぅぇぉゃゅょゎっァィゥェォャュョヮッ")
NO_END = set("（［｛《「『【")
kinsoku = []
for p in PAGES:
    for n in es[p]:
        t = n["text"]
        if t and t[0] in NO_START: kinsoku.append([p, "START", t[:70]])
        if t and t[-1] in NO_END: kinsoku.append([p, "END", t[:70]])

# --- 6. Badge / footer / masthead / images / credits ---
badge = [n for n in es["p1-touiban.svg"] if n["y"] == 434.0]
footers = {p: [n["text"] for n in es[p] if n["y"] == 2624.0] for p in PAGES}
mast = [n for n in es["p1-touiban.svg"] if n["text"].strip() == "Lucerna"]
images = {}
for p in PAGES:
    s = open(os.path.join(ES, p), encoding="utf-8").read()
    images[p] = len(re.findall(r"<image\b", s))
credit_nodes = [ (n["page"], n["text"][:160]) for n in flat
                 if re.search(r"Credit|Wikimedia|Commons|©|Public domain|CC0", n["text"]) ]
# embedded payload identity vs core
import hashlib
def img_md5(d):
    out = {}
    for p in PAGES:
        s = open(os.path.join(d, p), encoding="utf-8").read()
        out[p] = [hashlib.md5(m.group(1).encode()).hexdigest()
                  for m in re.finditer(r'xlink:href="data:image/[^;]+;base64,([^"]+)"', s)]
    return out

# --- 7. Script / politics / reader-facing / trad ---
def script_scan(dnodes):
    res = {}
    for p in PAGES:
        j = "".join(n["text"] for n in dnodes[p])
        res[p] = {"hangul": sum(1 for c in j if "\uAC00" <= c <= "\uD7A4"),
                  "cyrillic": sum(1 for c in j if "\u0400" <= c <= "\u04FF"),
                  "hiragana": sum(1 for c in j if "\u3040" <= c <= "\u309F"),
                  "katakana": sum(1 for c in j if "\u30A0" <= c <= "\u30FF"),
                  "hanzi": sum(1 for c in j if "\u4E00" <= c <= "\u9FFF")}
    return res
POLITICS = ["战争","地缘","外交","政治","选举","民调","政党","政府","领导人","主席","总理","人大","政协","台独","六四"]
politics = {}
for p in PAGES:
    j = "".join(n["text"] for n in es[p])
    for w in POLITICS:
        if w in j: politics.setdefault(p, []).append([w, j.count(w)])
READER = ["W46","w46","zh-cn","2026-w46","SOP","proofread","occlusion","audit","GitHub","github","insert.py","freeze","lint"]
reader = {}
for n in flat:
    for w in READER:
        if w in n["text"]: reader.setdefault(n["page"], []).append([w, n["text"][:140]])
TRAD_ONLY = set(list("麼魚體學讀週雙讓還過為與來東長門問間開關後發對說話語國時現見親觀歡難灣臺認議論權機歲處張帳場陽陰雲電靈龍龜點麵乾亂爭從倉側偵傳傷億儀儘僅廣廠廢彈歸當徹徑復徵德忍志忘忙忠快怎怒怕思急恆悅悉惠惡惱想愁愈愉意愛感慈態慣慘慮慶憂憑憲憶懶懷懸戀"))
trad = {}
for p in PAGES:
    j = "".join(n["text"] for n in es[p])
    c = collections.Counter(ch for ch in j if ch in TRAD_ONLY)
    if c: trad[p] = dict(c)

# --- 8. Added strings (edition minus core multiset) = explanation layer ---
added = {}
for p in PAGES:
    c = collections.Counter(n["text"] for n in core[p])
    e = collections.Counter(n["text"] for n in es[p])
    added[p] = sorted((e - c).elements())
added_all = [t for p in PAGES for t in added[p]]
# untranslated-English residue in added strings: flag added strings with ASCII words
# excluding adjudicated keeps (level kickers, loanwords, frozen English glosses/credits)
ascii_words = collections.Counter()
for t in added_all:
    for w in re.findall(r"[A-Za-z]{3,}", t):
        ascii_words[w] += 1

result = {"orphan_scan": orphan, "counts_es": counts(es), "counts_core": counts(core),
          "phrases_es": phrase_check(es), "chart": chart(), "kinsoku": kinsoku,
          "badge": [(n["x"], n["y"], n["text"], n["fill"]) for n in badge],
          "badge_fill_all": sorted(set(n["fill"] for n in badge)),
          "footers": footers, "masthead_Lucerna": [(n["x"], n["y"], n["text"]) for n in mast],
          "images_per_page": images, "credit_nodes": credit_nodes,
          "image_md5_es": img_md5(ES), "image_md5_core": img_md5(CORE),
          "script_scan_es": script_scan(es), "politics": politics,
          "reader_facing": reader, "trad_hits": trad,
          "added_string_count_per_page": {p: len(added[p]) for p in PAGES},
          "added_strings": added, "ascii_words_in_added": dict(ascii_words)}
with open(os.path.join(OUT, "counts-phrases-chart.json"), "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=1)
print("orphan candidates:", orphan["orphan_candidates_colstart"])
print("digitdot outside ex-x:", orphan["digitdot_outside_exercise_x"])
print("sectionC:", orphan["sectionC_nodes"])
print("ex39 es/core:", orphan["ex39_es"], orphan["ex39_core"])
print("ex75 es/core:", orphan["ex75_es"], orphan["ex75_core"])
print("counts:", result["counts_es"]["levels"], result["counts_es"]["per_page_counts"],
      "total", result["counts_es"]["total_unique"], "missing", result["counts_es"]["missing"])
print("phrases:", {k: v["total"] for k, v in result["phrases_es"].items()})
print("chart:", result["chart"])
print("kinsoku:", kinsoku)
print("badge:", result["badge"])
print("footers:", footers)
print("images:", images, "credits:", len(credit_nodes))
print("scripts:", result["script_scan_es"])
print("politics:", politics, "reader:", reader, "trad:", trad)
print("added counts:", result["added_string_count_per_page"])
