import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content12, content34, content56, content7, content8
from bslib4 import REG
from collections import Counter
out = {"total": len(REG), "levels": dict(Counter(r["level"] for r in REG)),
       "per_page": dict(Counter(r["page"] for r in REG)),
       "types": dict(Counter(r["type"] for r in REG))}
print("REG-DUMP " + json.dumps(out, ensure_ascii=False))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "reg.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False)
