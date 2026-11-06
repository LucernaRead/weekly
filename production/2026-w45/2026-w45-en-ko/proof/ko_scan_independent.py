#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independent Korean mid-word split scan for W45 ENxKO proof2.
Written from scratch for this proof round (not a copy of build ko_scan.py).
Method:
 - Parse <text x y> nodes from the DELIVERY SVGs (read-only).
 - Same-x pairs: sort by y per (page, x); consecutive pairs with 10<=gap<=45.
 - Cross-x pairs: sort all lines per page by y; consecutive pairs with
   10<=gap<=45 and x differing (indented continuation check).
 - For each pair: prev_last = trailing Hangul run of prev line's last
   whitespace token; next_first = leading Hangul run of next line's first
   whitespace token (regex first Hangul run, so leading '(' / punctuation
   is stripped, and a '(' -starting continuation is NOT excluded).
 - Candidate iff both runs non-empty AND (prev_last + next_first) occurs
   as a contiguous substring in the build-source corpus (content*.py +
   bslib4.py, read-only). This distinguishes a mid-word split (the
   unwrapped word exists in source) from a word-boundary break (two
   separate words concatenated do not occur in source).
 - Tail = syllable count of next_first. Blocking iff tail >= 3 (SOP #16).
 - S1: line starting with punctuation and containing Hangul.
 - S2: line with 1-2 Hangul syllables ending in .!?...) (labels excluded).
Usage: ko_scan_independent.py <svg-dir> <build-dir>
"""
import glob, html, os, re, sys
HANGUL = re.compile(r"[\uac00-\ud7a3]")
RUN = re.compile(r"[\uac00-\ud7a3]+")
START_PUNCT = set(".!?…)]}»」")
TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>([^<]*)</text>')

svg_dir, build_dir = sys.argv[1], sys.argv[2]
corpus = ""
for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:
    p = os.path.join(build_dir, fn)
    if os.path.exists(p):
        corpus += open(p, encoding="utf-8").read() + "\n"

def tail_run(tok):
    runs = RUN.findall(tok)
    return runs[-1] if runs else ""
def head_run(tok):
    m = RUN.search(tok)
    return m.group(0) if m else ""

same, cross, s1, s2 = [], [], [], []
for path in sorted(glob.glob(os.path.join(svg_dir, "*.svg"))):
    src = open(path, encoding="utf-8").read()
    els = []
    for m in TEXT_RE.finditer(src):
        t = html.unescape(m.group(3)).strip()
        if t:
            els.append((float(m.group(1)), float(m.group(2)), t))
    pg = os.path.basename(path)
    for x, y, t in els:
        if t.startswith("·"):
            continue
        if t[0] in START_PUNCT and HANGUL.search(t):
            s1.append((pg, x, y, t))
            print(f"S1 {pg} x={x} y={y} :: {t!r}")
        hc = len(HANGUL.findall(t))
        if 1 <= hc <= 2 and t[-1] in ".!?…)":
            if t not in ("번역", "쓰기", "빈칸 채우기"):
                s2.append((pg, x, y, t))
                print(f"S2 {pg} x={x} y={y} :: {t!r}")
    by_x = {}
    for x, y, t in els:
        by_x.setdefault(x, []).append((y, t))
    for x, lines in by_x.items():
        lines.sort()
        for (y1, s1t), (y2, s2t) in zip(lines, lines[1:]):
            gap = y2 - y1
            if gap < 10 or gap > 45:
                continue
            last = tail_run(s1t.split(" ")[-1])
            first = head_run(s2t.split(" ")[0])
            if last and first and (last + first) in corpus:
                same.append((pg, x, y1, y2, last, first, len(first)))
                print(f"CAND {pg} x={x} y={y1}->{y2} gap={gap:.1f} tail={len(first)} split={last}|{first} :: {s1t[-30:]!r} | {s2t[:30]!r}")
    # cross-x: page y-order, consecutive regardless of x
    ordered = sorted(els, key=lambda e: e[1])
    for (x1, y1, s1t), (x2, y2, s2t) in zip(ordered, ordered[1:]):
        if x1 == x2:
            continue
        gap = y2 - y1
        if gap < 10 or gap > 45:
            continue
        last = tail_run(s1t.split(" ")[-1])
        first = head_run(s2t.split(" ")[0])
        if last and first and (last + first) in corpus:
            cross.append((pg, x1, x2, y1, y2, last, first, len(first)))
            print(f"CROSS {pg} x={x1}->{x2} y={y1}->{y2} tail={len(first)} split={last}|{first} :: {s1t[-30:]!r} | {s2t[:30]!r}")
print(f"SUMMARY same-x={len(same)} tail>=3={sum(1 for c in same if c[6]>=3)} cross-x={len(cross)} S1={len(s1)} S2={len(s2)}")
