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
