# -*- coding: utf-8 -*-
"""JA line-start prohibition scan: every <text> element is one laid-out line.
Flag any line whose first character is a closer, a small kana, or an ASCII
closer. Report hits with page + text for adjudication."""
import glob
import html
import os
import re
import sys

FORBIDDEN = set("、。．，！？：；）」』】ー…‥・"
                "ゃゅょぁぃぅぇぉっゎ"
                ")]}.,!?%:;\"")
d = sys.argv[1]
bad = 0
for path in sorted(glob.glob(os.path.join(d, "*.svg"))):
    src = open(path, encoding="utf-8").read()
    for m in re.finditer(r"<text[^>]*>([^<]*)</text>", src):
        t = html.unescape(m.group(1))
        if t and t[0] in FORBIDDEN:
            print(f"{os.path.basename(path)}: {t[:70]!r}")
            bad += 1
print("linestart violations:", bad)
sys.exit(1 if bad else 0)
