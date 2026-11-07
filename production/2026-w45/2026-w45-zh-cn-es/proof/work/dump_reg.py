import os, sys, runpy, json
d = sys.argv[1]; out = sys.argv[2]
os.chdir(d); sys.path.insert(0, d)
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(os.path.join(d, f), run_name="__main__")
import bslib4
reg = []
for e in bslib4.REG:
    reg.append({k: e.get(k) for k in ("n", "level", "page", "type", "key", "note") if k in e} if isinstance(e, dict) else str(e))
with open(out, "w", encoding="utf-8") as fh:
    json.dump(reg, fh, ensure_ascii=False, indent=1)
print("REG dumped:", len(reg))
from collections import Counter
print("levels:", dict(Counter(str(e.get('level')) for e in reg if isinstance(e, dict))))
print("pages:", dict(sorted(Counter(str(e.get('page')) for e in reg if isinstance(e, dict)).items())))
print("keys sample #1, #150:", reg[0] if reg else None, reg[149] if len(reg) > 149 else None)
