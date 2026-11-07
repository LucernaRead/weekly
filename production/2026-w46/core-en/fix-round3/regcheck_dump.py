import runpy, sys, os, json
from collections import Counter
os.chdir(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-fix-round3/regcheck-build"))
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
out = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-fix-round3/registry-recheck.json")
json.dump(bslib4.REG, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("registry:", len(bslib4.REG))
ns = [e["n"] for e in bslib4.REG]
print("unique:", len(set(ns)), "complete 1..150:", sorted(ns)==list(range(1,151)), "all keyed:", all(e.get("key") for e in bslib4.REG))
print("by page:", dict(sorted(Counter(e["page"] for e in bslib4.REG).items())))
print("by level:", dict(Counter(e["level"] for e in bslib4.REG)))
