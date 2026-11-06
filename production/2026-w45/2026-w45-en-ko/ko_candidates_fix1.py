# -*- coding: utf-8 -*-
"""Fix-round-1 independent candidate lister (paren-aware, README #16).

Lists EVERY same-x pair (gap 10-45) whose trailing-Hangul + leading-Hangul
concatenation occurs in the build-source corpus, with the tail syllable
count — not only tail>=3. Also lists cross-x pairs (same page, different
x, gap 10-45) as a separate section, to rule out indent-continuation
misses. Usage: ko_candidates.py <svg-dir> <corpus-dir>
"""
import glob, os, re, sys
HANGUL = re.compile(r"[\uac00-\ud7a3]")
CORPUS = ""
for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:
    p = os.path.join(sys.argv[2], fn)
    if os.path.exists(p):
        CORPUS += open(p, encoding="utf-8").read() + "\n"

def hc(s): return len(HANGUL.findall(s))
def tail(s):
    runs = re.findall(r"[\uac00-\ud7a3]+", s); return runs[-1] if runs else ""
def head(s):
    m = re.search(r"[\uac00-\ud7a3]+", s); return m.group(0) if m else ""

same, cross = [], []
for path in sorted(glob.glob(os.path.join(sys.argv[1], "*.svg"))):
    src = open(path, encoding="utf-8").read()
    els = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>([^<]*)</text>', src):
        els.append((float(m.group(1)), float(m.group(2)), m.group(3).strip()))
    els = [e for e in els if e[2]]
    by_x = {}
    for x, y, t in els: by_x.setdefault(x, []).append((y, t))
    for x, lines in by_x.items():
        lines.sort()
        for (y1, s1), (y2, s2) in zip(lines, lines[1:]):
            gap = y2 - y1
            if gap < 10 or gap > 45: continue
            lh, fh = tail(s1.split(" ")[-1]), head(s2.split(" ")[0])
            if lh and fh and (lh + fh) in CORPUS:
                same.append((os.path.basename(path), x, y1, y2, lh, fh, hc(fh), s1[-30:], s2[:30]))
    # cross-x: consecutive in y order across different x on same page
    els_y = sorted(els, key=lambda e: e[1])
    for (x1, y1, s1), (x2, y2, s2) in zip(els_y, els_y[1:]):
        if x1 == x2: continue
        gap = y2 - y1
        if gap < 10 or gap > 45: continue
        lh, fh = tail(s1.split(" ")[-1]), head(s2.split(" ")[0])
        if lh and fh and (lh + fh) in CORPUS:
            cross.append((os.path.basename(path), x1, x2, y1, y2, lh, fh, hc(fh)))
print("== SAME-X candidates (all tails) ==")
for r in same: print(f"{r[0]} x={r[1]} y={r[2]}->{r[3]} tail={r[6]} split={r[4]}|{r[5]} :: {r[7]!r} | {r[8]!r}")
print(f"same-x total={len(same)} tail>=3={sum(1 for r in same if r[6]>=3)}")
print("== CROSS-X candidates ==")
for r in cross: print(r)
print(f"cross-x total={len(cross)}")
