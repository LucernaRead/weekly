# -*- coding: utf-8 -*-
"""W45 EN x KO Korean-line scan (README #16 extended + task window 10-45).

Pairs lines by (page, exact x, y-sorted). Definitions:
 S1 line-start orphan punctuation (Korean lines only).
 S2 Korean fragment line: <=2 Hangul syllables + final punct/paren.
 S3 mid-word split, corpus-verified (prev-last + next-first contiguous in
     a build source string) with a >=3-syllable TAIL (next line's first
     token); the retired 'head <= 1 syllable' criterion is NOT used.
 S4 tight-leading (10 <= gap <= 20) continuation line with <=2 syllables.
 G  gloss continuation starting with · (family format, not a defect).
 L  short standalone instr labels (by design, not defects).
Window for pair checks: 10 <= gap <= 45 (P8 answer lines sit at 14.69).
Usage: ko_scan.py <svg-dir> <corpus-dir>
"""
import glob
import os
import re
import sys

START_PUNCT = set(".!?…)]}»」")
HANGUL = re.compile(r"[\uac00-\ud7a3]")
CORPUS = ""
for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:
    p = os.path.join(sys.argv[2], fn)
    if os.path.exists(p):
        CORPUS += open(p, encoding="utf-8").read() + "\n"


def hc(s):
    return len(HANGUL.findall(s))


def hangul_tail(s):
    """Last Hangul run of a token (a fragment token may end with ')'
    or ','; the run, not the raw token end, is the fragment)."""
    runs = re.findall(r"[\uac00-\ud7a3]+", s)
    return runs[-1] if runs else ""


def hangul_head(s):
    """Leading Hangul run of a token (strips leading '(' etc. and
    trailing ')' etc.). Fix for the round-3 gap: the old code used
    first.split('(')[0] and excluded '(' -starting continuations, so a
    split whose two sides carry parens produced a parenthesised
    concatenation absent from the corpus and was missed (README #16
    paren-fragment case)."""
    m = re.search(r"[\uac00-\ud7a3]+", s)
    return m.group(0) if m else ""


def main():
    n = {"S1": 0, "S2": 0, "S3": 0, "S4": 0}
    for path in sorted(glob.glob(os.path.join(sys.argv[1], "*.svg"))):
        src = open(path, encoding="utf-8").read()
        els = []
        for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>([^<]*)</text>', src):
            els.append((float(m.group(1)), float(m.group(2)), m.group(3)))
        for x, y, t in els:
            s = t.strip()
            if not s:
                continue
            if s.startswith("·"):
                print(f"G  {os.path.basename(path)} y={y} :: {s[:60]!r}")
                continue
            if s[0] in START_PUNCT and hc(s) >= 1:
                print(f"S1 {os.path.basename(path)} y={y} :: {s[:60]!r}")
                n["S1"] += 1
            if hc(s) >= 1 and hc(s) <= 2 and s[-1] in ".!?…)":
                if s not in ("번역", "쓰기", "빈칸 채우기"):
                    print(f"S2 {os.path.basename(path)} y={y} x={x} :: {s!r}")
                    n["S2"] += 1
            if s in ("번역", "쓰기"):
                print(f"L  {os.path.basename(path)} y={y} :: {s!r}")
        by_x = {}
        for x, y, t in els:
            by_x.setdefault(x, []).append((y, t.strip()))
        for x, lines in by_x.items():
            lines.sort()
            for (y1, s1), (y2, s2) in zip(lines, lines[1:]):
                if not s1 or not s2:
                    continue
                gap = y2 - y1
                if gap < 10 or gap > 45:
                    continue
                last, first = s1.split(" ")[-1], s2.split(" ")[0]
                last_h, first_h = hangul_tail(last), hangul_head(first)
                if (last_h and first_h and hc(first_h) >= 3
                        and (last_h + first_h) in CORPUS):
                    print(f"S3 {os.path.basename(path)} x={x} y={y1}->{y2} :: {s1[-20:]!r} | {s2[:30]!r} split={last_h}|{first_h} tail={hc(first_h)}")
                    n["S3"] += 1
                if 10 <= gap <= 20 and 1 <= hc(s2) <= 2:
                    print(f"S4 {os.path.basename(path)} x={x} y={y2} :: {s2!r} (after {s1[-30:]!r})")
                    n["S4"] += 1
    print("counts:", n)


if __name__ == "__main__":
    main()
