# -*- coding: utf-8 -*-
"""W46 KO core self-checks: gloss occurrence, P7 phrases verbatim, orphan scan
(10-45 window, >=3-syllable tail, parenthesised fragments, line-start orphan
punctuation), date arithmetic. Reads SVGs + build sources only; never writes
into edition dirs."""
import os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xml.etree import ElementTree as ET

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(GOAL, "files/weekly-report-w46-ko-core")
BUILD = os.path.dirname(os.path.abspath(__file__))

def page_texts(svg):
    root = ET.parse(svg).getroot()
    ns = "{http://www.w3.org/2000/svg}"
    out = []
    for t in root.iter(ns + "text"):
        s = "".join(t.itertext())
        out.append((float(t.get("x")), float(t.get("y")), s))
    return out

# ---- 1. gloss occurrence: every glossed Korean headword must occur in
# prose on the same page (gloss lines themselves excluded) ----
# Gloss headwords are extracted from gloss() calls in sources by hand list:
# (page, headword forms as they appear in prose)
GLOSS = {
 1: ["입동", "절정", "김장", "상륙", "온대저기압"],
 2: ["집계", "좌우", "장바구니", "대상", "노고", "소화기", "막히", "절임배추", "버무리", "아끼", "아삭하", "약하", "김"],
 3: ["기관", "기준", "관측", "구간별", "전망", "나누", "통제", "순환버스", "겹치", "감사", "이용", "막히", "예의", "겹쳐 입", "미끄러지", "돌"],
 4: ["연승", "만루홈런", "미뤄지", "마감", "흔들", "하나가 되", "예상"],
 5: ["정리", "끈끈하", "합격", "관리본부", "신고", "챙기", "건네", "날씬해지", "하얗", "피곤하", "졸리", "평소"],
 6: ["재", "규모", "섞", "정직하", "채우", "속이", "예정", "확정", "믿"],
 7: ["본격", "남", "짐작", "기준", "관측"],
}
print("== gloss occurrence ==")
fails = 0
for pg, words in GLOSS.items():
    fn = sorted(glob.glob(os.path.join(ED, "svg", "*.svg")))[pg - 1]
    texts = [s for _, _, s in page_texts(fn)]
    joined = "\n".join(texts)
    for w in words:
        # count occurrences outside gloss lines (lines starting with 译注｜)
        prose = "\n".join(s for s in texts if not s.startswith("译注"))
        if w not in prose:
            print(f"  P{pg} MISS: {w}")
            fails += 1
print("  gloss fails:", fails)

# ---- 2. P7 phrases verbatim (whitespace-insensitive) against tagged pages ----
print("== P7 phrases ==")
phrases = [
 ("11월 7일은 입동이에요", 0),  # placeholder replaced below
]
# real phrases extracted from content7.py quotes list
import ast
src7 = open(os.path.join(BUILD, "content7.py"), encoding="utf-8").read()
m = re.search(r"quotes = \[(.*?)\n\]", src7, re.S)
pairs = re.findall(r'\("「(.*?)」", "(.*?)", "(.*?)"\)', m.group(1))
ok = True
for q, cn, pg in pairs:
    pnum = int(pg[0])
    fn = sorted(glob.glob(os.path.join(ED, "svg", "*.svg")))[pnum - 1]
    page = "".join(s for _, _, s in page_texts(fn))
    norm = lambda s: re.sub(r"\s+", "", s)
    if norm(q) not in norm(page):
        print(f"  NOT VERBATIM on p{pnum}: {q}")
        ok = False
    else:
        print(f"  ok p{pnum}: {q}")
print("  phrases all verbatim:", ok)

# ---- 3. orphan scan: 10-45 window ----
print("== orphan scan (window 10-45, >=3-syllable tail) ==")
from svglib import wrap, text_w
# Reconstruct wrapped lines per text element is not possible from SVG alone
# (SVG holds already-wrapped lines). Scan rendered lines: group by (page, x, size)
# using y-gaps: consecutive text elements with same x and y-step 10..45 that
# form a paragraph are approximated by same-x runs. Report: final line of a
# run that is a parenthesised fragment or a short tail, and runs starting
# with orphan punctuation.
ORPHAN_START = set(")]}〉》.,!?%:;」』】")
hangul = lambda ch: 0xAC00 <= ord(ch) <= 0xD7A3
def syllables(s):
    return sum(1 for ch in s if hangul(ch))
issues = []
for pi, fn in enumerate(sorted(glob.glob(os.path.join(ED, "svg", "*.svg"))), 1):
    texts = page_texts(fn)
    texts.sort(key=lambda t: (t[1], t[0]))
    # group into runs by x (rounded) and y-step
    runs = []
    for x, y, s in texts:
        if runs and abs(x - runs[-1][-1][0]) < 3 and 10 <= y - runs[-1][-1][1] <= 45 and len(runs[-1]) < 30:
            runs[-1].append((x, y, s))
        else:
            runs.append([(x, y, s)])
    for run in runs:
        if len(run) < 2:
            continue
        last = run[-1][2].strip()
        # parenthesised fragment: last line ends with ) or is "(...)" alone
        tail = last
        if tail.endswith(")") or tail.endswith("」") or tail.startswith("("):
            # count syllables after last space in the fragment's final segment
            seg = tail.split()[-1] if tail.split() else tail
            if syllables(seg) >= 3 or tail in ("(6면)",):
                issues.append((pi, "PAREN-FRAG", run[-1][1], last))
        # line-start orphan punctuation (excluding opening quotes handled by wrap)
        first = run[1][2].strip() if len(run) > 1 else ""
        if first and first[0] in ORPHAN_START:
            issues.append((pi, "START-PUNCT", run[1][1], first))
        # >=3-syllable tail: last line short relative to previous, tail segment
        # after last space in last line has >=3 syllables AND last line is
        # much shorter than the line above (single-word/short tail)
        prev = run[-2][2].strip()
        if len(last) <= 6 and syllables(last) >= 3 and len(prev) >= 14:
            # only flag if last line looks like a stranded verb ending / fragment
            if last.endswith(("요.", "요", "예요.", "예요", "어요.", "어요")) or ")" in last:
                issues.append((pi, "SHORT-TAIL", run[-1][1], last))
for it in issues:
    print(" ", it)
print("  orphan issues:", len(issues))

# ---- 4. date arithmetic ----
print("== dates ==")
from datetime import date
csat = date(2026, 11, 19)
for d, label in [(date(2026,11,9),"D-10"),(date(2026,11,12),"D-7"),(date(2026,11,15),"D-4"),(date(2026,11,18),"D-1")]:
    print(f"  {d} {d.strftime('%a')} -> {(csat-d).days} days = {label}: {(csat-d).days==int(label.split('-')[1]) if '-' in label else True}")
print("  Nov 11 weekday:", date(2026,11,11).strftime("%A"), "| Nov 9:", date(2026,11,9).strftime("%A"), "| Nov 28:", date(2026,11,28).strftime("%A"))
