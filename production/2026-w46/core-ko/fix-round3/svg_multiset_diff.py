#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SVG-text multiset diff pre-fix vs post-fix (Round 3 change isolation).
Reads the pre-fix extraction (extract_svg_text.py) and re-extracts the
current SVGs; reports added/removed strings per edition/page as multisets.
Expected: only P3 gloss wrap lines, P4 item-54 stem line, P7 item-103 stem
line change (wrap reflow may split the gloss/stem across different node
boundaries — report verbatim)."""
import glob, os, sys
from collections import Counter
from xml.etree import ElementTree as ET

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
W = os.path.join(GOAL, "hidden_files", "w46", "ko-fix-round3")
NS = "{http://www.w3.org/2000/svg}"
EDITIONS = {"zh-cn": "weekly-report-w46-ko-core", "de": "weekly-report-w46-ko-de",
            "en": "weekly-report-w46-ko-en", "es": "weekly-report-w46-ko-es",
            "fr": "weekly-report-w46-ko-fr", "it": "weekly-report-w46-ko-it",
            "ja": "weekly-report-w46-ko-ja", "nl": "weekly-report-w46-ko-nl",
            "pt": "weekly-report-w46-ko-pt", "ru": "weekly-report-w46-ko-ru",
            "zh-tw": "weekly-report-w46-ko-zh-tw"}

def load_dir(d):
    out = {}
    for f in sorted(glob.glob(os.path.join(d, "*.txt"))):
        lines = open(f, encoding="utf-8").read().split("\n")
        if lines and lines[-1] == "":
            lines.pop()
        out[os.path.basename(f)] = Counter(lines)
    return out

def current(code):
    edir = os.path.join(GOAL, "files", EDITIONS[code])
    out = {}
    for path in sorted(glob.glob(os.path.join(edir, "svg", "*.svg"))):
        root = ET.parse(path).getroot()
        lines = ["".join(t.itertext()) for t in root.iter(NS + "text")]
        out[os.path.splitext(os.path.basename(path))[0] + ".txt"] = Counter(lines)
    return out

def main():
    total_added = total_removed = 0
    for code in EDITIONS:
        pre = load_dir(os.path.join(W, "pre-fix", "svg-text", code))
        post = current(code)
        print(f"== {code} ==")
        for page in sorted(set(pre) | set(post)):
            a, b = pre.get(page, Counter()), post.get(page, Counter())
            added, removed = b - a, a - b
            if added or removed:
                print(f"  {page}: +{sum(added.values())} -{sum(removed.values())}")
                for s, n in removed.items():
                    print(f"    REMOVED x{n}: {s!r}")
                for s, n in added.items():
                    print(f"    ADDED   x{n}: {s!r}")
                total_added += sum(added.values())
                total_removed += sum(removed.values())
            else:
                print(f"  {page}: identical ({sum(a.values())} nodes)")
    print(f"TOTAL: +{total_added} -{total_removed}")

if __name__ == "__main__":
    main()
