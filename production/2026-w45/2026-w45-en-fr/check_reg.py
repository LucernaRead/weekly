# -*- coding: utf-8 -*-
"""One-process registry check: imports the FR content modules in order
(never standalone) and reports per-page / per-level counts + essay words.
Run with tools/venv/bin/python from the build dir."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bslib4
import content12, content34, content56, content7, content8
from collections import Counter
reg = bslib4.REG
print("total:", len(reg))
print("per page:", dict(sorted(Counter(e["page"] for e in reg).items())))
print("per level:", dict(sorted(Counter(e["level"] for e in reg).items())))
nums = [e["n"] for e in reg]
print("numbering continuous 1..150:", nums == list(range(1, 151)))
# essay: model text is frozen; count from content8 source string
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "content8.py"), encoding="utf-8").read()
import re
m = re.search(r'p\.para\(mx2 \+ 22, wy \+ 74, "(.*?)", 21,', src, re.S)
model = m.group(1)
words = model.replace("«", "").replace("»", "").replace(":", "").split()
print("essay words:", len(words))
print("essay:", model)
# P7 golden-sentence items: phrases list lives in content7 source
src7 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "content7.py"), encoding="utf-8").read()
phrases = re.findall(r'\(\"« (.*?) » \(page \d\)\"', src7)
print("golden sentences:", len(phrases))
for p in phrases: print("  -", p)
