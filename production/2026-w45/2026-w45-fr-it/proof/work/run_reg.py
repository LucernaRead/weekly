# Run content files in ONE process from a scratch build copy, dump REG + flow ends.
import sys, os, json, runpy
d = sys.argv[1]; outjson = sys.argv[2]
sys.path.insert(0, d)
os.chdir(d)
import bslib4
for f in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
    runpy.run_path(os.path.join(d, f), run_name="__main__")
json.dump(bslib4.REG, open(outjson, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("REG total", len(bslib4.REG))
