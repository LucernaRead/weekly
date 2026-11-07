# -*- coding: utf-8 -*-
"""xKO orphan scan v2, window 10-45 (tools/README #16).

Lines = rendered SVG <text> nodes containing Hangul (the Korean
explanation layer; frozen Traditional lines follow CJK wrap norms and
are out of scope). Blocks: group by (x, font-size), sort by y, split
on y-gap > 45 (the window's upper bound; in-block pitches are 14-35)
and, on P8, before every key-item start line (^N. / ^a. ).
Flags per block:
  S1   final line is a single Hangul syllable;
  SHORT final line <= 2 Hangul syllables that is NOT a complete word
       (listed for adjudication; complete predicates like "있어요."
       are adjudicated non-defects, not counted as defects);
  BRACKET final line ends with a dangling ')' fragment (<= 12 chars);
  HEADP any line starting with orphan punctuation [.!?…)] etc.;
  TAIL3 final line whose first token is >= 3 syllables AND whose
       previous line ends mid-word: approximated by prev line NOT
       ending in sentence-final punctuation (. ? ! …) — every such
       candidate is printed for human adjudication, because per-syllable
       wrap makes word-boundary breaks normal in full-width columns;
       only a final-line fragment that is visibly a word tail (prev
       line's last word continuing onto the final line) counts.
"""
import re, sys, glob, os
from collections import defaultdict
HANGUL = re.compile(r'[\uac00-\ud7a3]')
HEADP = set('.!?…)]}\u3002\u3001')
ITEM_START = re.compile(r'^(\d+\.|[a-d]\.)\s')

def main(d):
    cands = []
    for path in sorted(glob.glob(os.path.join(d, "*.svg"))):
        src = open(path, encoding="utf-8").read()
        nodes = []
        for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"[^>]*>([^<]*)</text>', src):
            x, y, size, t = float(m.group(1)), float(m.group(2)), float(m.group(4)), m.group(5)
            if t.strip() and HANGUL.search(t):
                nodes.append((x, y, size, t.strip()))
        groups = defaultdict(list)
        for x, y, size, t in nodes:
            groups[(round(x), size)].append((y, t))
        for (x, size), lines in groups.items():
            lines.sort()
            blocks, cur, prev_y = [], [], None
            for y, t in lines:
                if prev_y is not None and (y - prev_y > 45 or (os.path.basename(path) == "p8-test.svg" and ITEM_START.match(t))):
                    blocks.append(cur); cur = []
                cur.append((y, t)); prev_y = y
            if cur:
                blocks.append(cur)
            for b in blocks:
                if not b:
                    continue
                for (y, t) in b:
                    if t and t[0] in HEADP:
                        cands.append((os.path.basename(path), "HEADP", y, t[:50]))
                fy, ft = b[-1]
                syl = len(HANGUL.findall(ft))
                if syl <= 1:
                    cands.append((os.path.basename(path), "S1", fy, ft))
                elif syl <= 2:
                    cands.append((os.path.basename(path), "SHORT2", fy, ft))
                if re.search(r'[)\]]\s*$', ft) and len(ft) <= 12:
                    cands.append((os.path.basename(path), "BRACKET", fy, ft))
                if len(b) >= 2:
                    py, pt = b[-2]
                    first = ft.split()[0] if ft.split() else ""
                    if len(HANGUL.findall(first)) >= 3 and not pt.endswith(('.', '?', '!', '…', '。')):
                        cands.append((os.path.basename(path), "TAIL3?", fy, f"prev={pt[-16:]!r} final={ft[:30]!r}"))
    for c in cands:
        print(c)
    print("candidates:", len(cands))

if __name__ == "__main__":
    main(sys.argv[1])
