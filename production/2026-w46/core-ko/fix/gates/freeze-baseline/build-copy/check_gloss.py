# -*- coding: utf-8 -*-
"""Gloss verification from SOURCE: parse f.gloss()/glossline() strings per
page, check each Korean headword occurs in that page's prose (excluding the
gloss lines themselves). Dictionary form accepted if stem (minus final 다)
occurs in an inflected form."""
import os, re, glob
from xml.etree import ElementTree as ET

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(GOAL, "files/weekly-report-w46-ko-core")
BUILD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-ko-build")
NS = "{http://www.w3.org/2000/svg}"

def page_texts(pnum):
    fn = sorted(glob.glob(os.path.join(ED, "svg", "*.svg")))[pnum - 1]
    root = ET.parse(fn).getroot()
    return ["".join(t.itertext()) for t in root.iter(NS + "text")]

# page -> list of gloss strings, from sources in file order
FILE_PAGES = {"content12.py": [1, 2], "content34.py": [3, 4], "content56.py": [5, 6], "content7.py": [7]}
# crude: gloss() calls appear in the same order as pages are built within a
# file; assign by tracking CURPAGE lines.
fails = 0
for fname, pages in FILE_PAGES.items():
    src = open(os.path.join(BUILD, fname), encoding="utf-8").read().split("\n")
    cur = None
    for ln in src:
        m = re.search(r"CURPAGE\[0\] = (\d)", ln)
        if m:
            cur = int(m.group(1))
        gm = re.search(r'\.(?:gloss|glossline)\("([^"]+)"', ln)
        if gm and cur:
            gstr = gm.group(1)
            if gstr.startswith("译注"):
                gstr = gstr[3:]
            # glossline() in P7 and ex glosslines are instructions, not
            # word glosses: skip lines that are full Chinese sentences
            if re.match(r"^[\u4e00-\u9fff]", gstr):
                continue
            items = [it.strip() for it in gstr.rstrip("。").split("·")]
            texts = page_texts(cur)
            prose = "\n".join(s for s in texts if not s.startswith("译注"))
            for it in items:
                # headword: leading Hangul (+ spaces/particles) before Chinese
                hm = re.match(r"^[가-힣\s〜\-]+", it)
                if not hm:
                    continue
                head = hm.group(0).strip()
                head = re.sub(r"\s+", " ", head)
                stem = head[:-1] if head.endswith("다") else head
                if head in prose or stem in prose or head.replace(" ", "") in prose.replace(" ", ""):
                    pass
                else:
                    print(f"  P{cur} GLOSS-MISS: {head!r}  (from {it!r})")
                    fails += 1
print("gloss fails:", fails)
