# -*- coding: utf-8 -*-
"""Independent proof analysis for W45 zh-tw x de. Reads shipped SVGs only."""
import re, json, collections, glob, os

BASE = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files"
ED = os.path.join(BASE, "weekly-report-w45-zh-tw-de", "svg")
CORE = os.path.join(BASE, "weekly-report-w45-zhtw-core", "svg")
W43 = os.path.join(BASE, "weekly-report-zh-tw-de", "svg")

def texts(p):
    s = open(p, encoding="utf-8").read()
    raw = re.findall(r"<text[^>]*>([^<]*)</text>", s)
    return [t.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">") for t in raw]

def all_texts(d):
    out = {}
    for p in sorted(glob.glob(os.path.join(d, "*.svg"))):
        out[os.path.basename(p)] = texts(p)
    return out

def cjk_set(text_list):
    s = set()
    for t in text_list:
        for ch in t:
            o = ord(ch)
            if (0x2E80 <= o <= 0x9FFF) or (0xF900 <= o <= 0xFAFF) or (0x20000 <= o <= 0x2FA1F):
                s.add(ch)
    return s

def cjk_runs(text_list):
    runs = collections.Counter()
    pat = re.compile(r"[\u2e80-\u9fff\uf900-\ufaff]+")
    for t in text_list:
        for r in pat.findall(t):
            runs[r] += 1
    return runs

ed = all_texts(ED); core = all_texts(CORE); w43 = all_texts(W43)
ed_all = [t for v in ed.values() for t in v]
core_all = [t for v in core.values() for t in v]
w43_all = [t for v in w43.values() for t in v]

res = {}
# Gate 2: CJK union
union = cjk_set(core_all) | cjk_set(w43_all)
ed_set = cjk_set(ed_all)
res["cjk_union_size"] = len(union)
res["edition_cjk_size"] = len(ed_set)
res["outside_union"] = sorted(ed_set - union)
# Simplified-only spot lists
spot = list("邮说国龙马发观欢对让认识语学读书报纸电话车门问间见风云气头")
res["simplified_spot_hits_in_edition_set"] = [c for c in spot if c in ed_set]
res["simplified_spot_hits_in_edition_text"] = [c for c in spot if any(c in t for t in ed_all)]
# Gate 3: CJK run multiset per page + total
res["cjk_run_multiset_diff"] = {}
for pg in sorted(ed):
    d = cjk_runs(ed[pg]) - cjk_runs(core[pg])
    d2 = cjk_runs(core[pg]) - cjk_runs(ed[pg])
    res["cjk_run_multiset_diff"][pg] = {"edition_only": dict(d), "core_only": dict(d2)}
tot_ed, tot_core = cjk_runs(ed_all), cjk_runs(core_all)
res["cjk_run_total_diff"] = {"edition_only": dict(tot_ed - tot_core), "core_only": dict(tot_core - tot_ed)}
# Gate 14: Latin tokens
tok = collections.Counter()
for t in ed_all:
    for w in re.findall(r"[A-Za-zÄÖÜäöüß]+", t):
        tok[w] += 1
res["latin_token_total"] = sum(tok.values())
res["latin_tokens_distinct"] = dict(sorted(tok.items()))
# English apparatus strings
apparatus = ["Explanations in English", "This week", "Word of the week", "Quick quiz",
             "Did you get it", "Fill in", "Over to you", "Work it out", "Practice example",
             "All notes in English", "Model answer", "Open task", "Notes", "Answer keys",
             "Language focus", "Deep read", "Test & keys", "Readers' corner",
             "Phrases of the week", "Next week", "the edition for English-speaking readers"]
joined = "\n".join(ed_all)
res["apparatus_hits"] = {a: joined.count(a) for a in apparatus if joined.count(a)}
# Gloss rendered counts
res["hinweis_rendered"] = sum(t.count("Hinweis · ") for t in ed_all)
res["notes_rendered_edition"] = sum(t.count("Notes") for t in ed_all)
res["notes_rendered_core"] = sum(t.count("Notes") for t in core_all)
# Images per page + credits
res["images"] = {}
for pg in sorted(ed):
    s = open(os.path.join(ED, pg), encoding="utf-8").read()
    sc = open(os.path.join(CORE, pg), encoding="utf-8").read()
    im_ed = re.findall(r"<image[^>]*>", s)
    im_co = re.findall(r"<image[^>]*>", sc)
    res["images"][pg] = {"edition": im_ed, "core": im_co, "identical": im_ed == im_co}
credits = ["Wilfredor", "CorraleH", "Bain News Service", "Benjamin Balazs"]
res["credits_present"] = {c: (c in joined) for c in credits}
# Readers corner
p7 = "\n".join(ed["p7-lang.svg"])
res["readers_de_disclosure_invitation"] = "Schicken Sie uns Ihren Brief!" in p7
res["readers_frozen_disclosure"] = "你的來信，下一期見。" in p7
res["readers_frozen_prefix"] = "延期披露" in p7
# P7 phrases: the 8 Chinese phrases from core P7, count issue-wide in edition + core
phrases = ["用手機轉帳、掃碼付款、網上買保險，都是金融科技", "123個國家及城市、1,600個攤位",
           "需要才買，不要為了折扣買一堆用不到的東西", "在高雄，鋼鐵也能變成舞台",
           "福隆的夏天，在10月26日畫下句點", "6比0完封兄弟，龍隊拋下紅色彩帶",
           "250家店家一起討糖", "旅展首日中午12點才開門"]
res["phrases"] = {}
for ph in phrases:
    res["phrases"][ph] = {"edition_issuewide": joined.count(ph),
                          "core_issuewide": "\n".join(core_all).count(ph),
                          "edition_p7": "\n".join(ed["p7-lang.svg"]).count(ph)}
# P7 tags
res["p7_tags"] = dict(collections.Counter(re.findall(r"\(S\. \d\)", "\n".join(ed["p7-lang.svg"]))))
# P8 dash style + footer + badge
p8j = "\n".join(ed["p8-test.svg"])
res["p8_separator_sample"] = re.findall(r"— Seite \d —", p8j)[:3]
p1j = "\n".join(ed["p1-front.svg"])
res["p1_footer_present"] = "CHINESISCHE WOCHENZEITUNG VOL.2" in p1j
res["p1_badge_present"] = "CHINESISCHER TEXT (TRADITIONELL) · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER" in p1j
# Abstract topics cross-check against core text
core_joined = "\n".join(core_all)
res["abstract_topics_in_core"] = {
    "FinTech Week (金融科技週)": "金融科技週" in core_joined,
    "Taipei travel fair (台北旅展/旅展)": "旅展" in core_joined,
    "Wei Chuan Dragons (味全龍)": "味全龍" in core_joined,
    "Lidong (立冬)": "立冬" in core_joined,
    "Kaohsiung steel sculpture (鋼雕)": "鋼雕" in core_joined,
    "Tianmu Halloween (天母萬聖節/天母搞什麼鬼)": ("天母" in core_joined),
}
# fw-adjacency rewordings: clinic note + key 109
res["key109_de"] = [t for t in ed["p8-test.svg"] if "打卡" in t and "Foto" in t]
res["key109_core"] = [t for t in core["p8-test.svg"] if "打卡" in t]
res["clinic_notes_de"] = [t for t in ed["p7-lang.svg"] if "完勝" in t or "完封" in t]
res["clinic_notes_core"] = [t for t in core["p7-lang.svg"] if "完勝" in t or "完封" in t]

with open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-tw-de-proof/work/analyze.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
print("union", res["cjk_union_size"], "edition", res["edition_cjk_size"], "outside", res["outside_union"])
print("simplified hits set", res["simplified_spot_hits_in_edition_set"], "text", res["simplified_spot_hits_in_edition_text"])
print("cjk run total diff", res["cjk_run_total_diff"])
for pg, d in res["cjk_run_multiset_diff"].items():
    print(pg, "ed_only", d["edition_only"], "core_only", d["core_only"])
print("latin total", res["latin_token_total"], "distinct", len(res["latin_tokens_distinct"]))
print("apparatus hits", res["apparatus_hits"])
print("hinweis", res["hinweis_rendered"], "notes_ed", res["notes_rendered_edition"], "notes_core", res["notes_rendered_core"])
print("images", {k: (len(v["edition"]), len(v["core"]), v["identical"]) for k, v in res["images"].items()})
print("credits", res["credits_present"])
print("readers", res["readers_de_disclosure_invitation"], res["readers_frozen_disclosure"], res["readers_frozen_prefix"])
print("phrases", res["phrases"])
print("p7 tags", res["p7_tags"])
print("abstract topics", res["abstract_topics_in_core"])
print("key109 de", res["key109_de"]); print("key109 core", res["key109_core"])
print("clinic de", res["clinic_notes_de"]); print("clinic core", res["clinic_notes_core"])
