#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round 2 independent checks (own implementation; canonical tools run separately).
Writes checks.json + prints a summary. Reads SVGs/PDFs/ABSTRACT only."""
import re, os, json, glob, subprocess, sys
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
G = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ko-proofread-gates-round3")
EDITIONS = {
 "zh-cn": "weekly-report-w46-ko-core", "de": "weekly-report-w46-ko-de",
 "en": "weekly-report-w46-ko-en", "es": "weekly-report-w46-ko-es",
 "fr": "weekly-report-w46-ko-fr", "it": "weekly-report-w46-ko-it",
 "ja": "weekly-report-w46-ko-ja", "nl": "weekly-report-w46-ko-nl",
 "pt": "weekly-report-w46-ko-pt", "ru": "weekly-report-w46-ko-ru",
 "zh-tw": "weekly-report-w46-ko-zh-tw",
}
PAGES = ["p1-pyoji.svg","p2-saenghwal.svg","p3-munhwa.svg","p4-seupocheu.svg",
         "p5-cheongnyeon.svg","p6-gipi.svg","p7-mal.svg","p8-siheom.svg"]
TEXT_RE = re.compile(r'<text x="([^"]+)" y="([^"]+)"([^>]*)>([^<]*)</text>')
HANG = re.compile(r"[\uac00-\ud7a3]")
HAN = re.compile(r"[\u4e00-\u9fff]")
KANA = re.compile(r"[\u3040-\u30ff]")
CYR = re.compile(r"[\u0400-\u04ff]")
def texts(edir, pg):
    s = open(os.path.join(edir, "svg", pg), encoding="utf-8").read()
    return [(float(x), float(y), a, t) for x, y, a, t in TEXT_RE.findall(s)], s
def joined(edir):
    return "\n".join(t for pg in PAGES for _, _, _, t in texts(edir, pg)[0])

out = {}
for code, d in EDITIONS.items():
    edir = os.path.join(BASE, d)
    j = joined(edir)
    # --- D2/D1 ---
    p3 = texts(edir, "p3-munhwa.svg")[0]
    gloss3 = " ".join(t for _, _, _, t in p3 if "겹치다" in t)
    p6 = texts(edir, "p6-gipi.svg")[0]
    gloss6 = " ".join(t for _, _, _, t in p6 if "재다" in t and "규모" in t)
    out[code] = {
      "ganeul_count_all": j.count("가늘"),
      "ganeun_count_all": j.count("가늰"),
      "p3_gloss": gloss3,
      "p3_gloss_has_ganeulda": "가늘다" in gloss3,
      "p6_gloss": gloss6,
      "gui_simplified_count": j.count("规"),
      "gui_trad_count": j.count("規"),
      "fffd_count": j.count("\ufffd"),
      "han_distinct": sorted(set(HAN.findall(j))),
      "kana_chars": len(KANA.findall(j)),
      "cyr_chars": len(CYR.findall(j)),
      "p6_table_cells": [t for _, _, _, t in p6 if t.strip() in ("구분","이번 주 (11월 9~15일)","시험 날 (11월 19일)","날짜 세기","D-10 ~ D-4","D-데이","분위기","카운트다운","시험 당일","특별 조치","없어요 (평상시)","있어요 (10시 출근 등)")],
    }
    # P5 gloss lines (does any gloss define thin?)
    p5 = texts(edir, "p5-cheongnyeon.svg")[0]
    out[code]["p5_glosses"] = [" ".join(t for _, _, _, t in p5 if ("날씬" in t or "가늘" in t or "가늰" in t))]
    out[code]["p5_gloss_all"] = [t for _, _, _, t in p5 if "HINWEIS" in t or "译注" in t or "譯注" in t or "Note" in t or "Nota" in t or "解説" in t or "Пояснение" in t or "HINWEIS" in t]

# counts from extraction JSON (expand ranges)
ex = json.load(open(os.path.join(G, "exercises-all.json"), encoding="utf-8"))
counts = {}
for code, ed in ex.items():
    per, lv = {}, {"A2":0,"B1":0,"B2":0}
    for it in ed["items"]:
        m = re.match(r"(\d+)–(\d+)\.", it["num"])
        n = (int(m.group(2))-int(m.group(1))+1) if m else 1
        per[it["page"]] = per.get(it["page"], 0) + n
        lv[it["level"]] += n
    counts[code] = {"per_page": per, "levels": lv, "total": sum(per.values())}
out["counts"] = counts

# kinsoku: lines starting with closing punctuation
CLOSE = set(").,;:!?…»」』》’”")
kin = {}
for code, d in EDITIONS.items():
    edir = os.path.join(BASE, d); hits = []
    for pg in PAGES:
        for x, y, a, t in texts(edir, pg)[0]:
            tt = t.strip()
            if tt and tt[0] in CLOSE: hits.append((pg, y, tt[:40]))
    kin[code] = hits
out["kinsoku"] = kin

# P7 phrases
PHRASES = ["배추 값은 내렸는데 새우젓 값은 올랐어요","11월 11일은 이름이 세 개인 날이에요","김장이 한창이에요","수능까지 7일 남았어요. 오늘이 D-7예요","예보 날짜와 실제 관측 날짜는 달라요","결과는 KBO 홈페이지에서 확인하세요","수능까지 딱 일주일이 남아요","날짜와 기준과 결과를 나누면"]
def norm(s): return re.sub(r"\s+","",s)
ph = {}
for code, d in EDITIONS.items():
    edir = os.path.join(BASE, d)
    art = "".join(t for pg in PAGES[:6] for _, _, _, t in texts(edir, pg)[0])
    p7 = "".join(t for _, _, _, t in texts(edir, "p7-mal.svg")[0])
    ph[code] = {p: {"in_articles": norm(p) in norm(art), "on_p7": norm(p) in norm(p7)} for p in PHRASES}
out["p7_phrases"] = ph

# reader-facing sweep
TERMS = ["W46","2026-w46","proofread","SOP","occlusion","audit","freeze","weekly-git","github","index.json","language code","kicker","insert.py","run.py","text.md","ABSTRACT","WEEKLY-KIT","Discord","repository","core","fan-out"]
sweep = {}
for code, d in EDITIONS.items():
    edir = os.path.join(BASE, d); hits = []
    for pg in PAGES:
        for _, _, _, t in texts(edir, pg)[0]:
            for term in TERMS:
                if term in t: hits.append((pg, term, t[:80]))
    sweep[code] = hits
out["reader_sweep"] = sweep

# abstracts
absr = {}
for code, d in EDITIONS.items():
    p = os.path.join(BASE, d, "ABSTRACT.txt")
    s = open(p, encoding="utf-8").read()
    absr[code] = {"lines": s.count("\n"), "has_ascii_dquote": '"' in s, "len": len(s), "text": s.strip()}
out["abstracts"] = absr

# badge/footer
bf = {}
for code, d in EDITIONS.items():
    edir = os.path.join(BASE, d)
    els1 = texts(edir, "p1-pyoji.svg")[0]
    mast = [(x, y, t) for x, y, a, t in els1 if y < 430]
    foot = {}
    for pg in PAGES:
        foot[pg] = [(x, y, t) for x, y, a, t in texts(edir, pg)[0] if y > 2580]
    bf[code] = {"masthead_zone": mast, "footers": foot}
out["badge_footer"] = bf

# web PDFs: pages + size + pdftotext bytes (web only; print via pdfinfo pages)
pdfs = {}
for code, d in EDITIONS.items():
    edir = os.path.join(BASE, d)
    for fn in sorted(glob.glob(edir + "/*-web.pdf")):
        r = subprocess.run(["pdftotext", fn, "-"], capture_output=True)
        pi = subprocess.run(["pdfinfo", fn], capture_output=True, text=True)
        pages = re.search(r"Pages:\s+(\d+)", pi.stdout)
        pdfs[code] = {"web_pdf": os.path.basename(fn), "bytes": os.path.getsize(fn),
                      "pages": int(pages.group(1)) if pages else None, "pdftotext_bytes": len(r.stdout)}
    for fn in sorted(glob.glob(edir + "/*.pdf")):
        if "-web.pdf" in fn: continue
        pi = subprocess.run(["pdfinfo", fn], capture_output=True, text=True)
        pages = re.search(r"Pages:\s+(\d+)", pi.stdout)
        pdfs[code]["print_pdf"] = {"file": os.path.basename(fn), "bytes": os.path.getsize(fn),
                                  "pages": int(pages.group(1)) if pages else None}
out["pdfs"] = pdfs

# writing model char count (core P8 H example lines, x>=1451, y 408..503)
els8 = texts(os.path.join(BASE, EDITIONS["zh-cn"]), "p8-siheom.svg")[0]
model = "".join(t for x, y, a, t in els8 if x >= 1451 and 400 <= y <= 510)
out["writing_model"] = {"joined": model, "chars_no_space": len(re.sub(r"\s+","",model)),
                        "chars_with_space": len(model), "hangul": len(HANG.findall(model))}

json.dump(out, open(os.path.join(G, "checks.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for code in EDITIONS:
    o = out[code]
    print(code, "가늘=", o["ganeul_count_all"], "가늰=", o["ganeun_count_all"],
          "规=", o["gui_simplified_count"], "規=", o["gui_trad_count"],
          "FFFD=", o["fffd_count"], "kana=", o["kana_chars"], "cyr=", o["cyr_chars"])
    print("   P3gloss:", o["p3_gloss"][:160])
    print("   P6gloss:", o["p6_gloss"][:120])
    print("   HAN distinct:", "".join(o["han_distinct"]))
    print("   P6table cells:", len(o["p6_table_cells"]))
print("COUNTS:", json.dumps(counts, ensure_ascii=False))
print("KINSOKU:", {k: len(v) for k, v in kin.items()})
for k, v in kin.items():
    for h in v: print("  KIN", k, h)
print("P7PHRASES all-true:", all(all(vv.values()) for d in ph.values() for vv in d.values()))
for k, d in ph.items():
    bad = [p[:10] for p, vv in d.items() if not all(vv.values())]
    if bad: print("  PHRASE FAIL", k, bad)
print("SWEEP:", {k: len(v) for k, v in sweep.items()})
for k, v in sweep.items():
    for h in v: print("  SWEEP", k, h)
print("ABSTRACTS:")
for k, v in absr.items(): print("  ", k, "lines=", v["lines"], "dquote=", v["has_ascii_dquote"], "len=", v["len"], v["text"][:110])
print("PDFS:", json.dumps(pdfs, ensure_ascii=False, indent=1))
print("WRITING MODEL:", out["writing_model"])
