#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""zh-tw Simplified-only scan (Round 1 method): OpenCC s2t over every CJK
char in zh-tw SVG <text> elements. A char whose s2t form differs is a
Simplified-only candidate; each distinct candidate is listed with counts
and example contexts for adjudication. Reads SVGs only."""
import glob, os, re, sys
from collections import Counter
from xml.etree import ElementTree as ET

sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools/venv/lib/python3.12/site-packages"))
try:
    from opencc import OpenCC
except ImportError:
    from opencc import OpenCC  # noqa
NS = "{http://www.w3.org/2000/svg}"
EDIR = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ko-zh-tw")

def main():
    cc = OpenCC("s2t")
    counts = Counter()
    contexts = {}
    for path in sorted(glob.glob(os.path.join(EDIR, "svg", "*.svg"))):
        root = ET.parse(path).getroot()
        for t in root.iter(NS + "text"):
            s = "".join(t.itertext())
            for ch in s:
                if "\u4e00" <= ch <= "\u9fff":
                    conv = cc.convert(ch)
                    if conv != ch:
                        counts[ch] += 1
                        contexts.setdefault(ch, (os.path.basename(path), s[:60]))
    print("distinct Simplified-only candidates:", len(counts))
    for ch, n in counts.most_common():
        print(f"  {ch} U+{ord(ch):04X} x{n}  e.g. {contexts[ch][0]}: {contexts[ch][1]!r}")

if __name__ == "__main__":
    main()
