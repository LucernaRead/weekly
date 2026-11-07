import runpy, sys, os, json
from collections import Counter
d = sys.argv[1]; out = sys.argv[2]
os.chdir(d)
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(os.path.join(d, f), run_name="__main__")
import bslib4
reg = [{"n": i+1, "page": e["page"], "level": e["level"], "type": e["type"], "key": e["key"], "note": e.get("note","")} for i, e in enumerate(bslib4.REG)]
json.dump(reg, open(out, "w"), ensure_ascii=False, indent=0)
print("TOTAL", len(reg), "by level", dict(Counter(e["level"] for e in reg)), "by page", dict(sorted(Counter(e["page"] for e in reg).items())))
