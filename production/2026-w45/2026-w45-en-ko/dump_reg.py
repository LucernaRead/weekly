import os, sys, json
d = sys.argv[1]
sys.path.insert(0, d)
import content12, content34, content56, content7, content8
from bslib4 import REG
out = [{"n": e["n"], "page": e["page"], "level": e["level"], "type": e["type"], "key": e["key"], "note": e["note"]} for e in REG]
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("dumped", len(out))
