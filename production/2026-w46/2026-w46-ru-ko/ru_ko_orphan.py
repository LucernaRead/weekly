# -*- coding: utf-8 -*-
"""KO orphan scan for the W46 RU×KO edition: line-start orphans (closing
punctuation, lone particles) and short-tail wrapped paragraphs.
Paragraph = consecutive <text> elements sharing x + font-size with a steady
y pitch (26-34). Flags are printed for human adjudication; a flag is a
defect only if the rendered card confirms a bad break."""
import sys, os, re, glob
from xml.etree import ElementTree as ET

ED = sys.argv[1]
NS = "{http://www.w3.org/2000/svg}"
HANGUL = re.compile(r"[\uac00-\ud7a3]")
CLOSES = set("。，、；：？！）】」』”’.,?!")
PARTICLES = {"은", "는", "이", "가", "을", "를", "의", "에", "에서", "과", "와",
             "로", "으로", "도", "만", "까지", "부터", "에게", "한테", "보다",
             "처럼", "하고", "이며", "거나", "지만", "는데", "니까", "서", "면",
             "자", "고", "며", "은데", "는데도", "이라", "라는", "이다", "입니다"}

def page_texts(svg):
    t = ET.parse(svg)
    out = []
    for el in t.getroot().iter(NS + "text"):
        s = "".join(el.itertext())
        out.append((float(el.get("x")), float(el.get("y")),
                    float(el.get("font-size") or 0), s))
    return out

flags = []
for svg in sorted(glob.glob(os.path.join(ED, "svg", "*.svg"))):
    name = os.path.basename(svg)
    items = [it for it in page_texts(svg) if HANGUL.search(it[3])]
    # line-start orphans
    for x, y, size, s in items:
        st = s.strip()
        if not st:
            continue
        if st[0] in CLOSES:
            flags.append((name, round(y), "CLOSE-START", st[:40]))
        first = st.split()[0] if st.split() else ""
        if first in PARTICLES and len(st) < 45:
            flags.append((name, round(y), "PARTICLE-START", st[:40]))
    # paragraph grouping: same x + size, y pitch 26..34, in file order
    paras, cur = [], []
    for it in items:
        if cur and (abs(it[0] - cur[-1][0]) > 2 or abs(it[2] - cur[-1][2]) > 0.6
                    or not (26 <= it[1] - cur[-1][1] <= 34)):
            paras.append(cur)
            cur = []
        cur.append(it)
    if cur:
        paras.append(cur)
    for p in paras:
        if len(p) < 2:
            continue
        total = "".join(s for _, _, _, s in p)
        if 10 <= len(total) <= 45:
            continue  # short block by design (window 10-45 exempts whole short blocks)
        tail = p[-1][3].strip()
        nsyl = len(HANGUL.findall(tail))
        if 0 < nsyl < 3:
            flags.append((name, round(p[-1][1]), f"SHORT-TAIL({nsyl} syl)", tail[:40]))

for f in flags:
    print(f)
print("KO orphan flags:", len(flags))
