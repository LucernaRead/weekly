#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independent proofread gates for W46 KO family — Round 1.
Reads ONLY edition SVGs/PDFs/text.md/ABSTRACT (never build sources for verdicts,
except koscan source-string adjudication). Writes JSON + logs to gates dir.
"""
import re, os, glob, json, subprocess, hashlib, sys
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
GATES = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ko-proofread-gates")
CORE = os.path.join(BASE, "weekly-report-w46-ko-core")
EDITIONS = {
 "2026-w46-ko-zh-cn": CORE,
 "2026-w46-ko-de": os.path.join(BASE, "weekly-report-w46-ko-de"),
 "2026-w46-ko-en": os.path.join(BASE, "weekly-report-w46-ko-en"),
 "2026-w46-ko-es": os.path.join(BASE, "weekly-report-w46-ko-es"),
 "2026-w46-ko-fr": os.path.join(BASE, "weekly-report-w46-ko-fr"),
 "2026-w46-ko-it": os.path.join(BASE, "weekly-report-w46-ko-it"),
 "2026-w46-ko-ja": os.path.join(BASE, "weekly-report-w46-ko-ja"),
 "2026-w46-ko-nl": os.path.join(BASE, "weekly-report-w46-ko-nl"),
 "2026-w46-ko-pt": os.path.join(BASE, "weekly-report-w46-ko-pt"),
 "2026-w46-ko-ru": os.path.join(BASE, "weekly-report-w46-ko-ru"),
 "2026-w46-ko-zh-tw": os.path.join(BASE, "weekly-report-w46-ko-zh-tw"),
}
PAGES = ["p1-pyoji.svg","p2-saenghwal.svg","p3-munhwa.svg","p4-seupocheu.svg","p5-cheongnyeon.svg","p6-gipi.svg","p7-mal.svg","p8-siheom.svg"]
HANG = re.compile(r'[\uac00-\ud7a3]')
CJK = re.compile(r'[\u4e00-\u9fff]')
KANA = re.compile(r'[\u3040-\u30ff]')
CYR = re.compile(r'[\u0400-\u04ff]')
HANJA_ONLY = set("土")  # adjudicated paragraph char; checked separately

def texts_of(path):
    s = open(path, encoding="utf-8").read()
    els = re.findall(r'<text x="([^"]+)" y="([^"]+)"([^>]*)>([^<]*)</text>', s)
    return [(float(x), float(y), attrs, t) for x, y, attrs, t in els], s

def all_texts(edir):
    out = {}
    for p in PAGES:
        els, _ = texts_of(os.path.join(edir, "svg", p))
        out[p] = [t for _, _, _, t in els]
    return out

# ---------- 1. inventories ----------
inv = {}
for slug, edir in EDITIONS.items():
    d = all_texts(edir)
    joined = "\n".join("\n".join(v) for v in d.values())
    inv[slug] = {
      "hangul_chars": len(HANG.findall(joined)),
      "hangul_distinct": sorted(set(HANG.findall(joined))),
      "cjk_chars": len(CJK.findall(joined)),
      "cjk_distinct_count": len(set(CJK.findall(joined))),
      "kana_chars": len(KANA.findall(joined)),
      "cyrillic_chars": len(CYR.findall(joined)),
      "per_page_hangul": {p: len(HANG.findall("\n".join(v))) for p, v in d.items()},
      "per_page_cjk": {p: len(CJK.findall("\n".join(v))) for p, v in d.items()},
    }
json.dump(inv, open(os.path.join(GATES, "inventories.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# freeze-style multiset diffs (independent re-derivation, char-level for Hangul/CJK)
freeze = {}
core_texts = all_texts(CORE)
for slug, edir in EDITIONS.items():
    if slug == "2026-w46-ko-zh-cn":
        freeze[slug] = {"note": "core itself"}
        continue
    ed = all_texts(edir)
    per = {}
    for p in PAGES:
        from collections import Counter
        cc, ee = Counter(core_texts[p]), Counter(ed[p])
        added = dict((ee - cc)); removed = dict((cc - ee))
        added_str = "\n".join(added)
        per[p] = {
          "added_strings": len(added), "removed_strings": len(removed),
          "added_hangul_chars": len(HANG.findall(added_str)),
          "added_hangul_distinct": sorted(set(HANG.findall(added_str))),
          "added_cjk_chars": len(CJK.findall(added_str)),
          "added_kana_chars": len(KANA.findall(added_str)),
          "added_cyrillic_chars": len(CYR.findall(added_str)),
          "added": sorted(added.keys())[:400],
          "removed": sorted(removed.keys())[:400],
        }
    freeze[slug] = per
json.dump(freeze, open(os.path.join(GATES, "freeze-rederive.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------- 2. exercise counts: badge+number+stem triples ----------
def count_exercises(edir):
    per_page = {}; levels = {"A2":0,"B1":0,"B2":0}; p8_nums = []
    for p in PAGES:
        els, _ = texts_of(os.path.join(edir, "svg", p))
        seq = [t.strip() for _, _, _, t in els]
        n = 0; lv = {"A2":0,"B1":0,"B2":0}
        for i in range(len(seq)-2):
            if seq[i] in ("A2","B1","B2") and re.fullmatch(r"\d+\.", seq[i+1] or ""):
                n += 1; lv[seq[i]] += 1
                if p == "p8-siheom.svg": p8_nums.append(int(seq[i+1][:-1]))
        per_page[p] = {"count": n, "levels": lv}
        for k in lv: levels[k] += lv[k]
    return per_page, levels, sorted(p8_nums)

counts = {}
for slug, edir in EDITIONS.items():
    pp, lv, p8n = count_exercises(edir)
    counts[slug] = {"per_page": pp, "levels": lv, "total": sum(v["count"] for v in pp.values()),
                    "p8_numbers": p8n, "p8_min": min(p8n) if p8n else None, "p8_max": max(p8n) if p8n else None,
                    "p8_missing": [x for x in range(113,151) if x not in p8n],
                    "p8_dupes": [x for x in set(p8n) if p8n.count(x) > 1]}
json.dump(counts, open(os.path.join(GATES, "exercise-counts.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: (v["total"], v["levels"], {p: c["count"] for p,c in v["per_page"].items()}) for k,v in counts.items()}, ensure_ascii=False, indent=1))

# ---------- 3. badge + footer + masthead ----------
def badge_footer(edir):
    els1, raw1 = texts_of(os.path.join(edir, "svg", "p1-pyoji.svg"))
    # masthead: UnifrakturMaguntia Lucerna + nearby texts y<430
    mast = [(x,y,attrs,t) for x,y,attrs,t in els1 if "UnifrakturMaguntia" in attrs or y < 430]
    # badge candidates: texts at y 385-400 (majority) or subtitle-slot y~372
    # footer: texts y>2580 on each page
    footers = {}
    for p in PAGES:
        els, _ = texts_of(os.path.join(edir, "svg", p))
        footers[p] = [(x,y,attrs,t) for x,y,attrs,t in els if y > 2580]
    # fill colours of badge-line texts: find text containing reader-native marker words
    return {"masthead_zone": [(x,y,attrs,t) for x,y,attrs,t in mast],
            "footers": {p: [(x,y,attrs,t) for x,y,attrs,t in v] for p,v in footers.items()}}
bf = {slug: badge_footer(edir) for slug, edir in EDITIONS.items()}
json.dump(bf, open(os.path.join(GATES, "badge-footer.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for slug in EDITIONS:
    print("== BADGE/FOOTER", slug)
    for x,y,a,t in bf[slug]["masthead_zone"]:
        print(f"  y={y} {a} {t!r}")
    print("  P1 footer:", [t for _,_,_,t in bf[slug]["footers"]["p1-pyoji.svg"]])
    print("  P8 footer:", [t for _,_,_,t in bf[slug]["footers"]["p8-siheom.svg"]])
