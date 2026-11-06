import runpy, sys, os, json
from collections import Counter
os.chdir(sys.argv[1])
sys.path.insert(0, sys.argv[1])
for f in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
    runpy.run_path(os.path.join(sys.argv[1], f), run_name="__main__")
import bslib4
json.dump(bslib4.REG, open(sys.argv[2],"w",encoding="utf-8"), ensure_ascii=False, indent=1)
print("TOTAL", len(bslib4.REG))
print("by level", dict(Counter(e["level"] for e in bslib4.REG)))
print("by page", dict(sorted(Counter(e["page"] for e in bslib4.REG).items())))
print("by type", dict(Counter(e["type"] for e in bslib4.REG)))
