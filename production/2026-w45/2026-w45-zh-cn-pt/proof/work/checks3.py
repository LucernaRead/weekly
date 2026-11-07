# -*- coding: utf-8 -*-
"""Removed-CJK classification + leftover-English scan on delivered edition SVGs."""
import json, re, glob, os
from collections import Counter

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
d = json.load(open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-pt-proof/work/diff.json")))
CJK = re.compile(r'[\u4e00-\u9fff]+')

def page_text(path):
    s = open(path, encoding="utf-8").read()
    return " ".join(re.findall(r'<text[^>]*>([^<]*)</text>', s))

ed_files = {1: 'p1-touiban', 2: 'p2-shenghuo', 3: 'p3-wenhua', 4: 'p4-tiyu', 5: 'p5-qingnian', 6: 'p6-shendu', 7: 'p7-ciyu', 8: 'p8-ceyan'}
print("=== REMOVED-CJK runs NOT present in edition page ===")
for pg, pdata in sorted(d['pages'].items(), key=lambda kv: int(kv[0])):
    ed = page_text(f"{BASE}/weekly-report-w45-zh-cn-pt/svg/{ed_files[int(pg)]}.svg")
    for item in pdata['removed_strings']:
        t = item['text']
        for run in CJK.findall(t):
            if run not in ed:
                print(f" p{pg} run {run!r} in removed string: {t[:130]!r}")
print("(end of removed-CJK list)")

print()
print("=== LEFTOVER-ENGLISH scan (edition SVGs) ===")
allt = ""
for f in sorted(glob.glob(f"{BASE}/weekly-report-w45-zh-cn-pt/svg/*.svg")):
    allt += " " + page_text(f)
words = re.findall(r"[A-Za-zÀ-ÿ]+(?:['-][A-Za-zÀ-ÿ]+)*", allt)
cnt = Counter(w for w in words if re.search(r'[A-Za-z]', w))
# allowlist: PT words contain accents mostly; ASCII-only tokens need review
for w, c in sorted(cnt.items()):
    if re.fullmatch(r"[A-Za-z'-]+", w):
        print(f"  {w}: {c}")
