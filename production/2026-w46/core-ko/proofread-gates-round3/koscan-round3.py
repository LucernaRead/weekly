#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round 2 OWN koscan/orphan scan (independent implementation, per tools/README
extensions): window 10-45px; same-column pairs (x within 30px, same page);
pure-Hangul fragments; TRUE_SPLIT iff joined fragments form a word attested
in the edition's own source literals (build .py files read as TEXT, never
imported/executed) and the fragments are not separated by a word boundary
in that source. S3 = TRUE_SPLITs whose tail fragment is >=3 syllables
(README: >=3-syllable tails are in scope) AND tail<=3 reported separately
as S3small for comparability with Round 1 logs. Also: orphan final lines
(every final-line element incl. parenthesised fragments), line-start
orphan punctuation, and >=3-syllable tail fragments at line starts.
Source-word set built from string literals in content*.py (ast literal
extraction, no execution)."""
import ast, glob, os, re, sys, json
from xml.etree import ElementTree as ET
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
NS = "{http://www.w3.org/2000/svg}"
HANG = re.compile(r"[\uac00-\ud7a3]")
PURE = re.compile(r"^[\uac00-\ud7a3]+$")
PAGES = ["p1-pyoji.svg","p2-saenghwal.svg","p3-munhwa.svg","p4-seupocheu.svg",
         "p5-cheongnyeon.svg","p6-gipi.svg","p7-mal.svg","p8-siheom.svg"]
BUILDS = {
 "zh-cn": "weekly-report-w46-ko-build", "de": "weekly-report-w46-ko-de-build",
 "en": "weekly-report-w46-ko-en-build", "es": "weekly-report-w46-ko-es-build",
 "fr": "weekly-report-w46-ko-fr-build", "it": "weekly-report-w46-ko-it-build",
 "ja": "weekly-report-w46-ko-ja-build", "nl": "weekly-report-w46-ko-nl-build",
 "pt": "weekly-report-w46-ko-pt-build", "ru": "weekly-report-w46-ko-ru-build",
 "zh-tw": "weekly-report-w46-ko-zh-tw-build",
}
EDITIONS = {k: v.replace("-build", "") for k, v in BUILDS.items()}
EDITIONS["zh-cn"] = "weekly-report-w46-ko-core"

def source_words(build_dir):
    words = set(); spaced = set()
    for fn in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
        src = open(os.path.join(build_dir, fn), encoding="utf-8").read()
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                lit = node.value
                for w in re.split(r"\s+", lit):
                    clean = re.sub(r"[^\uac00-\ud7a3]", "", w)
                    if clean: words.add(clean)
                spaced.add(re.sub(r"\s+", " ", lit).strip())
    return words, spaced

def page_els(path):
    root = ET.parse(path).getroot()
    els = []
    for t in root.iter(NS+"text"):
        els.append((float(t.get("x")), float(t.get("y")), "".join(t.itertext())))
    return els

def scan(code):
    build = os.path.join(GOAL, "hidden_files", BUILDS[code])
    edir = os.path.join(GOAL, "files", EDITIONS[code])
    words, _ = source_words(build)
    cand = true = s3big = s3small = 0
    trues = []; orphans = []; linestart = []
    CLOSE_START = set(").,;:!?…»」』》’”")
    for pg in PAGES:
        els = page_els(os.path.join(edir, "svg", pg))
        # group into columns by x clustering (tolerance 30), sort each by y
        cols = []
        for e in sorted(els, key=lambda e: (e[0], e[1])):
            placed = False
            for c in cols:
                if abs(e[0] - c[0][0]) <= 30:
                    c.append(e); placed = True; break
            if not placed: cols.append([e])
        for col in cols:
            col.sort(key=lambda e: e[1])
            prev = None
            for x, y, s in col:
                st = s.strip()
                # line-start orphan punctuation (any element starting with a closer)
                if st and st[0] in CLOSE_START:
                    linestart.append((pg, y, st[:40]))
                if prev:
                    px, py, ps = prev
                    gap = y - py
                    if 10 <= gap <= 45 and abs(x - px) <= 30 and ps.strip() and st:
                        a = ps.strip().split(); b = st.split()
                        if a and b and HANG.search(a[-1]) and HANG.search(b[0]):
                            cand += 1
                            a1 = re.sub(r"[^\uac00-\ud7a3]", "", a[-1])
                            b1 = re.sub(r"[^\uac00-\ud7a3]", "", b[0])
                            if PURE.match(a[-1]) and PURE.match(b[0]):
                                joined = a[-1] + b[0]
                                if joined in words and len(joined) >= 3:
                                    true += 1
                                    tail = len(b[0])
                                    if tail >= 3: s3big += 1
                                    if tail <= 3: s3small += 1
                                    trues.append((pg, py, y, a[-1], b[0], joined))
                # orphan final-line candidates: short Hangul-only lines (<=2 chars)
                # plus parenthesised fragments, recorded for adjudication
                if st and HANG.search(st):
                    bare = re.sub(r"\s+", "", st)
                    if len(bare) <= 2 and not re.search(r"[0-9]", st):
                        orphans.append((pg, y, st))
                prev = (x, y, s)
    return {"candidates": cand, "true_splits": true, "s3_tail_ge3": s3big,
            "s3_tail_le3": s3small, "true_list": trues,
            "orphan_short": orphans, "line_start_punct": linestart}

if __name__ == "__main__":
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)
    res = {}
    for code in BUILDS:
        r = scan(code); res[code] = r
        print(code, f"CANDIDATES={r['candidates']} TRUE_SPLITS={r['true_splits']} "
              f"S3>=3={r['s3_tail_ge3']} S3<=3={r['s3_tail_le3']} "
              f"ORPHANshort={len(r['orphan_short'])} LINESTART={len(r['line_start_punct'])}")
        for t in r["true_list"]: print("  TRUE", t)
        for o in r["orphan_short"]: print("  ORPHAN", o)
        for o in r["line_start_punct"]: print("  LINESTART", o)
    json.dump(res, open(os.path.join(outdir, "koscan-round3.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
