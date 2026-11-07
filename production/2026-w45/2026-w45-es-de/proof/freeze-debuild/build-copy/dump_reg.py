import runpy, sys, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd())
for f in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
out = sys.argv[1]
json.dump(bslib4.REG, open(out,"w"), ensure_ascii=False, indent=1)
print("REG total", len(bslib4.REG))
from collections import Counter
print("level", dict(Counter(e["level"] for e in bslib4.REG)))
print("page", dict(sorted(Counter(e["page"] for e in bslib4.REG).items())))
print("type", dict(Counter(e["type"] for e in bslib4.REG)))
print("sample", json.dumps(bslib4.REG[0], ensure_ascii=False))
print("sample150", json.dumps(bslib4.REG[149], ensure_ascii=False))
