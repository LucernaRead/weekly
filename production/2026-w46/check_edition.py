# -*- coding: utf-8 -*-
"""Generic edition checks for W46 fan-outs: P7 Korean phrases verbatim
(whitespace-insensitive), xKO orphan scan (window 10-45, >=3-syllable tail,
parenthesised fragments, line-start orphan punctuation), line-start
kinsoku. Usage: python check_edition.py <svg-dir>"""
import glob, os, re, sys
from xml.etree import ElementTree as ET

NS = "{http://www.w3.org/2000/svg}"
CORE_BUILD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-ko-build")

def page_texts(svg):
    root = ET.parse(svg).getroot()
    return [(float(t.get("x")), float(t.get("y")), "".join(t.itertext()))
            for t in root.iter(NS + "text")]

def main():
    svgdir = sys.argv[1]
    svgs = sorted(glob.glob(os.path.join(svgdir, "*.svg")))
    assert len(svgs) == 8, svgs
    # phrases from core content7 quotes list
    src7 = open(os.path.join(CORE_BUILD, "content7.py"), encoding="utf-8").read()
    m = re.search(r"quotes = \[(.*?)\n\]", src7, re.S)
    pairs = re.findall(r'\("「(.*?)」", "(.*?)", "(.*?)"\)', m.group(1))
    norm = lambda s: re.sub(r"\s+", "", s)
    ok = True
    for q, cn, pg in pairs:
        pnum = int(pg[0])
        page = "".join(s for _, _, s in page_texts(svgs[pnum - 1]))
        if norm(q) not in norm(page):
            print(f"  PHRASE MISS p{pnum}: {q}")
            ok = False
    print("phrases:", "8/8 OK" if ok else "FAIL")
    # orphan scan
    ORPHAN_START = set(")]}〉》.,!?%:;」』】")
    hangul = lambda ch: 0xAC00 <= ord(ch) <= 0xD7A3
    def syllables(s):
        return sum(1 for ch in s if hangul(ch))
    issues = []
    for pi, fn in enumerate(svgs, 1):
        texts = sorted(page_texts(fn), key=lambda t: (t[1], t[0]))
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
            if last.endswith(")") or last.endswith("」") or last.startswith("("):
                seg = last.split()[-1] if last.split() else last
                if syllables(seg) >= 3:
                    issues.append((pi, "PAREN-FRAG", round(run[-1][1], 1), last))
            first = run[1][2].strip() if len(run) > 1 else ""
            if first and first[0] in ORPHAN_START:
                issues.append((pi, "START-PUNCT", round(run[1][1], 1), first))
            prev = run[-2][2].strip()
            if len(last) <= 6 and syllables(last) >= 3 and len(prev) >= 14:
                if last.endswith(("요.", "요", "예요.", "예요", "어요.", "어요")) or ")" in last:
                    issues.append((pi, "SHORT-TAIL", round(run[-1][1], 1), last))
    for it in issues:
        print("  ORPHAN:", it)
    print("orphan issues:", len(issues))
    # kinsoku: any text line starting with closing punctuation (any page)
    kin = 0
    for pi, fn in enumerate(svgs, 1):
        for x, y, s in page_texts(fn):
            st = s.strip()
            if st and st[0] in ")]}〉》.,!?%:;」』】":
                print(f"  KINSOKU p{pi} y={round(y,1)}: {st[:40]!r}")
                kin += 1
    print("kinsoku line-starts:", kin)

if __name__ == "__main__":
    main()
