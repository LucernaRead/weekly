# -*- coding: utf-8 -*-
"""Independent linestart coordinate comparison: edition vs core."""
import glob, html, os, re, sys

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
FORB = set("、。．，！？：；）」』】ー…‥・")
FORB |= set("ゃゅょぁぃぅぇぉっゎ")
FORB |= set(")]}.,!?%:;\"")


def hits(d):
    out = []
    for path in sorted(glob.glob(d + "/*.svg")):
        src = open(path, encoding="utf-8").read()
        for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>([^<]*)</text>', src):
            t = html.unescape(m.group(3))
            if t and t[0] in FORB:
                out.append((os.path.basename(path), float(m.group(1)), float(m.group(2)), t))
    return out


co = hits(BASE + "/files/weekly-report-w45-en-core/svg")
ed = hits(BASE + "/files/weekly-report-w45-en-ja/svg")
print("CORE", len(co))
for h in co:
    print(" ", h[0], h[1], h[2], repr(h[3][:60]))
print("EDITION", len(ed))
for h in ed:
    print(" ", h[0], h[1], h[2], repr(h[3][:60]))
coset = {(p, y) for p, x, y, t in co}
print("--- edition vs core same (page,y):")
for p, x, y, t in ed:
    same = [c for c in co if c[0] == p and c[2] == y]
    print(p, y, repr(t[:45]), "MATCH" if same else "NO-MATCH",
          "core@same-y:", [repr(c[3][:45]) for c in same])
# Japanese-line check: any edition violating line whose first char is kana/kanji
# or whose line contains kana/kanji as its main content (i.e. a Japanese line)?
jp = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff]")
print("--- edition violating lines containing Japanese script:")
for p, x, y, t in ed:
    print(p, y, "HAS-JP" if jp.search(t) else "no-JP", repr(t[:60]))
