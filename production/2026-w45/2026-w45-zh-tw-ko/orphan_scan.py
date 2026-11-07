# -*- coding: utf-8 -*-
"""xKO orphan scan, window 10-45 (tools/README #16, RUxKO-extended).

Groups rendered SVG <text> nodes into lines by (x, font-size) column
and y order, then flags, per paragraph group:
  (a) final line that is a single Hangul syllable / single word;
  (b) final line ending in a dangling ')' or a parenthesised fragment;
  (c) a mid-word split whose tail is >=3 Hangul syllables
      (first-segment <=1-syllable criterion is RETIRED per ESxKO);
  (d) a continuation line STARTING with orphan punctuation
      [.!?…)]\]»」』】％];
  (e) any standalone single-syllable line.
A complete standalone key item (e.g. a full predicate "있어요." that
closes its own sentence at a word boundary) is NOT an orphan and is
adjudicated, not flagged as a defect.
"""
import re, sys, glob, os
from collections import defaultdict

HANGUL = re.compile(r'[\uac00-\ud7a3]')
FRAG_START = set('.!?…)]\]»」』】％')

def syllables(s):
    return len(HANGUL.findall(s))

def main(d):
    cand = []
    for path in sorted(glob.glob(os.path.join(d, "*.svg"))):
        src = open(path, encoding="utf-8").read()
        nodes = []
        for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"[^>]*>([^<]*)</text>', src):
            x, y, fam, size, t = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), m.group(5)
            if t.strip():
                nodes.append((x, y, size, t))
        # group by (x rounded, size): a column's wrapped lines share x+size
        groups = defaultdict(list)
        for x, y, size, t in nodes:
            groups[(round(x), size)].append((y, t))
        for (x, size), lines in groups.items():
            lines.sort()
            for i, (y, t) in enumerate(lines):
                st = t.strip()
                if i == len(lines) - 1:
                    # final line of its group
                    if syllables(st) <= 1 and HANGUL.search(st):
                        cand.append((os.path.basename(path), x, y, "S1", st))
                    if re.search(r'[)\]]\s*$', st) and len(st) <= 12:
                        cand.append((os.path.basename(path), x, y, "BRACKET-TAIL", st))
                if i > 0:
                    prev = lines[i - 1][1].strip()
                    if st and st[0] in FRAG_START:
                        cand.append((os.path.basename(path), x, y, "LINE-HEAD-PUNCT", st))
                    # mid-word split: prev line ends mid-word (no space/punct
                    # end) and this line's first token is >=3 syllables, and
                    # the two join into a longer word (heuristic: prev ends
                    # with Hangul, this starts with Hangul)
                    if prev and HANGUL.search(prev[-1]) and HANGUL.search(st[0]):
                        first = st.split()[0] if st.split() else ""
                        if syllables(first) >= 3 and not prev.endswith(('요', '다', '요.', '다.', '요?', '요!')):
                            cand.append((os.path.basename(path), x, y, "SPLIT>=3", f"prev={prev[-12:]!r} next={st[:20]!r}"))
    for c in cand:
        print(c)
    print("candidates:", len(cand))

if __name__ == "__main__":
    main(sys.argv[1])
