#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Proofread part 2: phrases, kinsoku/orphan, letters-box, P6 table, PDFs,
abstracts, reader-facing sweep, counts incl. matching ranges, gloss spot checks."""
import re, os, glob, json, subprocess, hashlib
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
GATES = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ko-proofread-gates")
EDITIONS = {
 "2026-w46-ko-zh-cn": os.path.join(BASE, "weekly-report-w46-ko-core"),
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
def els(edir, pg):
    s = open(os.path.join(edir, "svg", pg), encoding="utf-8").read()
    return re.findall(r'<text x="([^"]+)" y="([^"]+)"([^>]*)>([^<]*)</text>', s), s
def page_texts(edir, pg):
    return [t for _, _, _, t in els(edir, pg)[0]]

# ---- counts incl. matching ranges ----
counts2 = {}
for slug, edir in EDITIONS.items():
    total = 0; levels = {"A2":0,"B1":0,"B2":0}; per = {}
    for pg in PAGES:
        seq = [t.strip() for _, _, _, t in els(edir, pg)[0]]
        n = 0; lv = {"A2":0,"B1":0,"B2":0}
        for i in range(len(seq)-1):
            if seq[i] in ("A2","B1","B2") and re.fullmatch(r"\d+\.", seq[i+1] or ""):
                n += 1; lv[seq[i]] += 1
            m = re.fullmatch(r"(\d+)–(\d+)\.", seq[i+1] or "") if i+1 < len(seq) else None
            if seq[i] in ("A2","B1","B2") and m:
                a, b = int(m.group(1)), int(m.group(2))
                n += (b-a+1); lv[seq[i]] += (b-a+1)
        per[pg] = {"count": n, "levels": lv}
        total += n
        for k in lv: levels[k] += lv[k]
    counts2[slug] = {"per_page": per, "levels": levels, "total": total}
json.dump(counts2, open(os.path.join(GATES, "exercise-counts-v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("COUNTS-V2:", json.dumps({k: (v["total"], v["levels"]) for k, v in counts2.items()}, ensure_ascii=False))

# ---- P7 phrases: extract Korean phrases from P7 + check contiguous in P1-P6 article text ----
# Phrase block: P7 texts after '이번 주의 문장' header; Korean phrase lines are the
# Serif lines carrying page tags like (1면). We instead verify the KIT-listed 8 phrases
# (from core KIT) against each edition's P1-P6 joined text, whitespace-insensitive,
# and verify the same 8 Korean strings appear on P7 of every edition.
PHRASES = ["배추 값은 내렸는데 새우젓 값은 올랐어요",
 "11월 11일은 이름이 세 개인 날이에요",
 "김장이 한창이에요",
 "수능까지 7일 남았어요. 오늘이 D-7예요",
 "예보 날짜와 실제 관측 날짜는 달라요",
 "결과는 KBO 홈페이지에서 확인하세요",
 "수능까지 딱 일주일이 남아요",
 "날짜와 기준과 결과를 나누면"]
def norm(s): return re.sub(r"\s+", "", s)
ph = {}
for slug, edir in EDITIONS.items():
    art = ""
    for pg in PAGES[:6]:
        art += "".join(page_texts(edir, pg))
    art_n = norm(art)
    p7 = "".join(page_texts(edir, "p7-mal.svg"))
    p7_n = norm(p7)
    ph[slug] = {p: {"in_articles": norm(p) in art_n, "on_p7": norm(p) in p7_n} for p in PHRASES}
json.dump(ph, open(os.path.join(GATES, "p7-phrases.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for slug, d in ph.items():
    print("PHRASES", slug, {p[:12]: v for p, v in d.items()})

# ---- kinsoku: Korean lines starting with closing punct / orphan punct ----
CLOSE_START = set(").,;:!?…»」』》’”")
kin = {}
for slug, edir in EDITIONS.items():
    hits = []
    for pg in PAGES:
        for x, y, a, t in els(edir, pg)[0]:
            tt = t.strip()
            if tt and tt[0] in CLOSE_START:
                hits.append((pg, float(y), tt[:50]))
    kin[slug] = hits
json.dump(kin, open(os.path.join(GATES, "kinsoku.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("KINSOKU:", {k: len(v) for k, v in kin.items()})
for k, v in kin.items():
    for h in v: print("  KIN", k, h)

# ---- reader-facing sweep: internal-production terms in rendered text ----
TERMS = ["W46", "2026-w46", "VOL.3", "proofread", "SOP", "occlusion", "audit", "freeze",
 "weekly-git", "github", "lint", "index.json", "W45", "VOL.4", "core", "fan-out",
 "2026-W46", "ko-de", "ko-en", "language code", "kicker", "cover", "insert.py",
 "run.py", "text.md", "ABSTRACT", "WEEKLY-KIT", "Discord", "repository"]
# VOL.3/VOL.4 are legitimate on-page furniture (masthead/footer/teaser); report separately.
sweep = {}
for slug, edir in EDITIONS.items():
    hits = []
    for pg in PAGES:
        for t in page_texts(edir, pg):
            for term in TERMS:
                if term in t and term not in ("VOL.3", "VOL.4"):
                    hits.append((pg, term, t[:90]))
    sweep[slug] = hits
json.dump(sweep, open(os.path.join(GATES, "reader-facing-sweep.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("SWEEP:", {k: len(v) for k, v in sweep.items()})
for k, v in sweep.items():
    for h in v: print("  SWEEP", k, h)

# ---- P6 comparison table cell values (core + each edition: table is Korean; check identical Korean cells) ----
def p6_table(edir):
    ts = page_texts(edir, "p6-gipi.svg")
    return [t for t in ts if t.strip() in ("구분","이번 주 (11월 9~15일)","시험 날 (11월 19일)","날짜 세기","D-10 ~ D-4","D-데이","분위기","카운트다운","시험 당일","특별 조치","없어요 (평상시)","있어요 (10시 출근 등)")]
t6 = {slug: p6_table(edir) for slug, edir in EDITIONS.items()}
json.dump(t6, open(os.path.join(GATES, "p6-table.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for slug, v in t6.items(): print("P6TABLE", slug, len(v), v)

# ---- P1 numbers box: find standalone number texts on P1 ----
for slug, edir in EDITIONS.items():
    ts = page_texts(edir, "p1-pyoji.svg")
    nums = [t for t in ts if re.fullmatch(r"[0-9][0-9,]*", t.strip() or "")]
    print("P1NUMBERS", slug, nums)

# ---- letters-box measurement on P7: find bordered rect containing disclosure; measure last text baseline vs rect bottom ----
def letters_box(edir):
    _, raw = els(edir, "p7-mal.svg")
    # rects with stroke + fill in P7 lower half
    rects = re.findall(r'<rect x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"[^>]*>', raw)
    texts = els(edir, "p7-mal.svg")[0]
    # disclosure candidates: lines containing VOL.4 promise / disclosure keywords per language is hard;
    # use geometry: letters box is the rect in x 989..1423 (right rail col 3?) — instead report ALL rects y>1500
    # and texts y>1500, letting the analyst compute. Save structured dump.
    return {"rects": [(float(x), float(y), float(w), float(h)) for x, y, w, h in rects],
            "texts_y1500": [(float(x), float(y), t) for x, y, a, t in texts if float(y) > 1500]}
lb = {slug: letters_box(edir) for slug, edir in EDITIONS.items()}
json.dump(lb, open(os.path.join(GATES, "letters-box-dump.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("LETTERSBOX dumped")
