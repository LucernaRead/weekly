#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract per-page SVG <text> strings (one node per line, in document order)
for pre/post multiset diffing. Read-only."""
import glob, os, sys
from xml.etree import ElementTree as ET

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
NS = "{http://www.w3.org/2000/svg}"
EDITIONS = {"zh-cn": "weekly-report-w46-ko-core", "de": "weekly-report-w46-ko-de",
            "en": "weekly-report-w46-ko-en", "es": "weekly-report-w46-ko-es",
            "fr": "weekly-report-w46-ko-fr", "it": "weekly-report-w46-ko-it",
            "ja": "weekly-report-w46-ko-ja", "nl": "weekly-report-w46-ko-nl",
            "pt": "weekly-report-w46-ko-pt", "ru": "weekly-report-w46-ko-ru",
            "zh-tw": "weekly-report-w46-ko-zh-tw"}

def main(outdir):
    for code, edir in EDITIONS.items():
        d = os.path.join(outdir, code)
        os.makedirs(d, exist_ok=True)
        for path in sorted(glob.glob(os.path.join(GOAL, "files", edir, "svg", "*.svg"))):
            root = ET.parse(path).getroot()
            lines = ["".join(t.itertext()) for t in root.iter(NS + "text")]
            name = os.path.splitext(os.path.basename(path))[0] + ".txt"
            with open(os.path.join(d, name), "w", encoding="utf-8") as fh:
                fh.write("\n".join(lines) + "\n")
            print(code, name, len(lines))

if __name__ == "__main__":
    main(sys.argv[1])
