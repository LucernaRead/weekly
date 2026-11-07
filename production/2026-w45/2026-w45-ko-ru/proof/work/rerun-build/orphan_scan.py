# -*- coding: utf-8 -*-
"""KO x RU orphan scan (tools README #16 extended, brief standard):
 S1 line-start orphan punctuation (Korean lines only; gloss-continuation
    lines starting with · reported as G, family format, not defects).
 S2 fragment line: stripped text holds 1-2 Hangul syllables and ends with
    sentence-final punctuation or a lone closing paren.
 S3 mid-word split: consecutive same-x lines, baseline gap in [10, 45],
    corpus-verified (prev last space-token + next first space-token
    contiguous in a Korean source string) with a >=3-syllable TAIL
    (next line's first token). The retired "first segment <= 1" criterion
    is NOT used; S3b lists corpus-verified splits with tail < 3 for
    transparency (adjudicated, not counted under the stated standard).
 S5 line-end orphan OPENING punctuation (「 『 " ' ( 〈 《 stranded last).
 S4 tight-leading (gap <= 20) continuation line with <= 2 Hangul syllables
    (reported; adjudicated against the core's own pattern).
Corpus = this build's content files (Korean source strings, frozen).
Usage: tools/venv/bin/python orphan_scan.py <svg-dir>
"""
import re, sys, glob, os

START_PUNCT = set(".!?…)]»」")
END_OPEN = set("「『“‘（〈《")
HANGUL = re.compile(r"[\uac00-\ud7a3]")

BUILD = os.path.dirname(os.path.abspath(__file__))
CORPUS = ""
for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    CORPUS += open(os.path.join(BUILD, fn), encoding="utf-8").read() + "\n"


def hc(s):
    return len(HANGUL.findall(s))


def main(d):
    n = {"S1": 0, "S2": 0, "S3": 0, "S3b": 0, "S4": 0, "S5": 0, "G": 0}
    for path in sorted(glob.glob(os.path.join(d, "*.svg"))):
        src = open(path, encoding="utf-8").read()
        els = []
        for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>([^<]*)</text>', src):
            els.append((float(m.group(1)), float(m.group(2)), m.group(3)))
        for x, y, t in els:
            s = t.strip()
            if not s:
                continue
            if s.startswith("·"):
                n["G"] += 1
                print(f"G  {os.path.basename(path)} y={y} :: {s[:60]!r}")
                continue
            if s[0] in START_PUNCT and hc(s) >= 1:
                n["S1"] += 1
                print(f"S1 {os.path.basename(path)} y={y} :: {s[:60]!r}")
            if 1 <= hc(s) <= 2 and s[-1] in ".!?…)":
                n["S2"] += 1
                print(f"S2 {os.path.basename(path)} y={y} x={x} :: {s!r}")
            if s and s[-1] in END_OPEN:
                n["S5"] += 1
                print(f"S5 {os.path.basename(path)} y={y} :: {s[:60]!r}")
        by_x = {}
        for x, y, t in els:
            by_x.setdefault(x, []).append((y, t.strip()))
        for x, lines in by_x.items():
            lines.sort()
            for (y1, s1), (y2, s2) in zip(lines, lines[1:]):
                if not s1 or not s2:
                    continue
                gap = y2 - y1
                if 10 <= gap <= 45:
                    last, first = s1.split(" ")[-1], s2.split(" ")[0]
                    first_tok = first.split("(")[0]
                    if (hc(last) >= 1 and (last + first_tok) in CORPUS
                            and last + first_tok != last):
                        # genuine mid-word split only if source has no space
                        # between the two fragments (substring check above
                        # already requires contiguity; a word-boundary wrap
                        # would appear as "last first" with a space, not
                        # as the concatenation)
                        if hc(first_tok) >= 3:
                            n["S3"] += 1
                            print(f"S3 {os.path.basename(path)} x={x} y={y1}->{y2} :: {s1[-20:]!r} | {s2[:30]!r}")
                        else:
                            n["S3b"] += 1
                            print(f"S3b {os.path.basename(path)} x={x} y={y1}->{y2} :: {s1[-20:]!r} | {s2[:30]!r}")
                if gap <= 20 and 1 <= hc(s2) <= 2:
                    n["S4"] += 1
                    print(f"S4 {os.path.basename(path)} x={x} y={y2} :: {s2!r} (after {s1[-30:]!r})")
    print("TOTALS:", n)


if __name__ == "__main__":
    main(sys.argv[1])
