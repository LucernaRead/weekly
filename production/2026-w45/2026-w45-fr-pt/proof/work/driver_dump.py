# Proofreader-owned single-process driver: runs content modules in order,
# then dumps bslib4.REG (shared module) to reg.json in cwd.
import runpy, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    print("=" * 24, f)
    runpy.run_path(f, run_name="__main__")
import bslib4
json.dump(bslib4.REG, open("reg.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("REG dumped:", len(bslib4.REG))
