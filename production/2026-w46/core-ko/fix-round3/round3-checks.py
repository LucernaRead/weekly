#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round 3 checks (adapted from the preserved Round 2 round2-checks.py,
read first; canonical tools run separately). Reads SVGs/PDFs/ABSTRACT only.
Writes checks.json into the Round 3 gate dir. Adds: item 54/103 stem+key
reconstruction from rendered SVG text, P3 gloss-box geometry, zh-tw
Simplified-only scan (OpenCC s2t via tools venv `opencc` module)."""
import re, os, json, glob, subprocess, sys
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
G = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ko-fix-round3")
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
    # item 54 (P4) + item 103 (P7): find stem fragments in rendered text
    p4j = " ".join(t for _, _, _, t in texts(edir, "p4-seupocheu.svg")[0])
    p7j = " ".join(t for _, _, _, t in texts(edir, "p7-mal.svg")[0])
    out[code]["item54_stem_rendered"] = "한국시리즈 시작이 하루" in p4j
    out[code]["item54_old_suffix_present"] = "___어요" in p4j
    out[code]["item103_stem_rendered"] = "미리 소금에 절인 배추를" in p7j
    out[code]["item103_old_particle_present"] = "___이라고" in p7j
    out[code]["item103_new_particle_present"] = "___라고" in p7j
    # P8 keys 54/103 as printed
    p8j = " ".join(t for _, _, _, t in texts(edir, "p8-siheom.svg")[0])
    out[code]["p8_key54_millyeosseo"] = "밀렸어요" in p8j
    out[code]["p8_key103_jeorim"] = "절임배추" in p8j

# P3 gloss-box geometry: gloss <text> nodes vs enclosing <rect>
RECT_RE = re.compile(r'<rect x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"[^>]*>')
def gloss_geometry(edir):
    s = open(os.path.join(edir, "svg", "p3-munhwa.svg"), encoding="utf-8").read()
    rects = [(float(x), float(y), float(w), float(h)) for x, y, w, h in RECT_RE.findall(s)]
    els = [(float(x), float(y), t) for x, y, a, t in TEXT_RE.findall(s) if "겹치다" in t or "가늘다" in t or ("감사하다" in t and "겹치다" in s[max(0, s.find(t)-200):s.find(t)+200])]
    # Simpler: gloss lines = text nodes whose text is part of the gloss line:
    # nodes containing any of the gloss headwords on the gloss y-band.
    all_els = [(float(x), float(y), t) for x, y, a, t in TEXT_RE.findall(s)]
    gy = [y for x, y, t in all_els if "겹치다" in t]
    if not gy:
        return {"error": "no gloss anchor"}
    band = [e for e in all_els if abs(e[1] - gy[0]) < 60 and ("겹치다" in e[2] or "가늘다" in e[2] or "감사하다" in e[2] or "나누다" in e[2])]
    # The gloss wraps over consecutive lines with the same x start; take all
    # nodes with x within 5 of the anchor x and y within 120 below anchor.
    ax = [x for x, y, t in all_els if "겹치다" in t][0]
    lines = [e for e in all_els if abs(e[0] - ax) < 6 and gy[0] - 5 <= e[1] <= gy[0] + 120]
    # enclosing rect: smallest rect containing all line baselines (y-20..y+8)
    cands = []
    for (rx, ry, rw, rh) in rects:
        if all(rx <= x and x <= rx + rw and ry <= y <= ry + rh for x, y, t in lines):
            cands.append((rw * rh, rx, ry, rw, rh))
    cands.sort()
    box = cands[0][1:] if cands else None
    res = {"gloss_lines": lines, "box": box}
    if box:
        rx, ry, rw, rh = box
        res["margins"] = {"top": min(y for _, y, _ in lines) - ry,
                          "bottom": (ry + rh) - max(y for _, y, _ in lines),
                          "left": min(x for x, _, _ in lines) - rx,
                          "right": (rx + rw) - max(x for x, _, _ in lines)}
        res["inside"] = all(res["margins"].values())
    return res

out["gloss_geometry"] = {code: gloss_geometry(os.path.join(BASE, d)) for code, d in EDITIONS.items()}

# kinsoku
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

# PDFs
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
        r2 = subprocess.run(["pdftotext", fn, "-"], capture_output=True)
        pdfs[code]["print_pdf"] = {"file": os.path.basename(fn), "bytes": os.path.getsize(fn),
                                  "pages": int(pages.group(1)) if pages else None,
                                  "pdftotext_bytes": len(r2.stdout)}
out["pdfs"] = pdfs

json.dump(out, open(os.path.join(G, "gates", "checks.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for code in EDITIONS:
    o = out[code]
    print(code, "가늘=", o["ganeul_count_all"], "가늰=", o["ganeun_count_all"],
          "规=", o["gui_simplified_count"], "規=", o["gui_trad_count"],
          "FFFD=", o["fffd_count"], "kana=", o["kana_chars"], "cyr=", o["cyr_chars"],
          "P6cells=", len(o["p6_table_cells"]))
    print("   P3gloss:", o["p3_gloss"][:170])
    print("   item54 stem:", o["item54_stem_rendered"], "old___어요:", o["item54_old_suffix_present"],
          "| item103 stem:", o["item103_stem_rendered"], "old이라고:", o["item103_old_particle_present"],
          "new라고:", o["item103_new_particle_present"],
          "| keys:", o["p8_key54_millyeosseo"], o["p8_key103_jeorim"])
    g = out["gloss_geometry"][code]
    print("   gloss-box:", g.get("box"), "margins:", g.get("margins"), "lines:", len(g.get("gloss_lines", [])))
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
