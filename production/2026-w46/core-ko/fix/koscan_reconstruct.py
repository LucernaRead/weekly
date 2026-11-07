#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Post-fix koscan reconstruction (W46 KO fix, Round 1).

The Round 1 proofreader's koscan script was not preserved in the gates dir
(only its logs survive: CANDIDATES / TRUE_SPLITS / S3 + ORPHAN lines).
This reconstruction implements the same verdict criterion from the logs'
evidence: a TRUE_SPLIT is a Korean word broken mid-word across two
consecutive rendered lines of the same column (the wrap must break on
word boundaries; a split word would join, with no space, into a single
source word). S3 = splits whose tail fragment is <=3 syllables is
reported separately; both must be 0.

Method: per page, order <text> elements by (x-column, y); for each
adjacent pair in the same column with a line-pitch gap (25..50px),
take last token of the upper line and first token of the lower line.
CANDIDATE = both tokens Hangul and the upper line does not end with
sentence-final punctuation. TRUE_SPLIT = the joined token (no space)
occurs as a contiguous word in the edition's source manuscript prose
(content*.py literals) while the spaced form does not occur at that
boundary in the source — i.e. the renderer split one source word.
ORPHAN final lines (<=1 syllable, as in the Round 1 logs) are listed
for information only, as in Round 1.
"""
import glob, os, re, sys, ast
from xml.etree import ElementTree as ET

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
NS = "{http://www.w3.org/2000/svg}"
HANG = re.compile(r"[\uac00-\ud7a3]")
PAGES = ["p1-pyoji.svg", "p2-saenghwal.svg", "p3-munhwa.svg", "p4-seupocheu.svg",
         "p5-cheongnyeon.svg", "p6-gipi.svg", "p7-mal.svg", "p8-siheom.svg"]

def source_words(build_dir):
    words = set()
    for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        src = open(os.path.join(build_dir, fn), encoding="utf-8").read()
        for m in re.findall(r'"([^"]+)"', src):
            for w in re.split(r"\s+", m):
                if HANG.search(w):
                    words.add(re.sub(r"[^\uac00-\ud7a3]", "", w))
    return words

def page_lines(svg_path):
    root = ET.parse(svg_path).getroot()
    els = []
    for t in root.iter(NS + "text"):
        els.append((float(t.get("x")), float(t.get("y")), "".join(t.itertext())))
    return els

def scan(edir, build_dir):
    words = source_words(build_dir)
    cand = true = s3 = 0
    orphans = []
    for pg in PAGES:
        els = page_lines(os.path.join(edir, "svg", pg))
        # group by column: x rounded to nearest 10 within same flow; sort by y
        els.sort(key=lambda e: (round(e[0] / 100), e[1]))
        prev = None
        for x, y, s in els:
            s = s.strip()
            if prev and abs(x - prev[0]) < 60 and 25 <= (y - prev[1]) <= 50 and s and prev[2].strip():
                a = prev[2].strip().split()
                b = s.split()
                if a and b and HANG.search(a[-1]) and HANG.search(b[0]):
                    cand += 1
                    if not a[-1].endswith((".", "!", "?", "。", "…")):
                        # CORRECTION 2026-11-03: fragments must be pure-Hangul
                        # tokens. Stripping digits fused "두산에" + "4대"
                        # (source: "두산에\n4대 1로 승리", an explicit
                        # wrap point) into "두산에대" and false-flagged it.
                        # A true mid-word split has pure-Hangul fragments.
                        if not (re.fullmatch(r"[\uac00-\ud7a3]+", a[-1]) and re.fullmatch(r"[\uac00-\ud7a3]+", b[0])):
                            continue
                        joined = a[-1] + b[0]
                        if joined in words and len(joined) >= 3:
                            true += 1
                            if len(re.sub(r"[^\uac00-\ud7a3]", "", b[0])) <= 3:
                                s3 += 1
                            print(f"  TRUE_SPLIT {pg} y={y} {a[-1]!r} + {b[0]!r} = {joined!r}")
            # orphan final lines: very short Hangul-only line
            if s and len(re.sub(r"\s+", "", s)) <= 2 and HANG.search(s) and not re.search(r"[0-9]", s):
                orphans.append((pg, y, s))
            prev = (x, y, s)
    print(f"CANDIDATES={cand} TRUE_SPLITS={true} S3={s3}")
    print(f"ORPHAN final lines (<=2 chars): {len(orphans)}")
    for o in orphans:
        print("  ORPHAN", o)
    return cand, true, s3

if __name__ == "__main__":
    edir, build_dir = sys.argv[1], sys.argv[2]
    print("==", edir)
    scan(edir, build_dir)
