import runpy, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ".")
import bslib4
for f in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
    runpy.run_path(f, run_name="__main__")
from collections import Counter
print("TOTAL", len(bslib4.REG))
print("levels", dict(Counter(e["lv"] for e in bslib4.REG)))
print("per-page", dict(sorted(Counter(e["page"] for e in bslib4.REG).items())))
print("numbers continuous 1-150:", sorted(e["n"] for e in bslib4.REG)==list(range(1,151)))
print("types", dict(Counter(e["type"] for e in bslib4.REG)))
