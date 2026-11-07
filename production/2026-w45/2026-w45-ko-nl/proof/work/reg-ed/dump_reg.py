import os, sys, runpy, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
json.dump(bslib4.REG, open("reg.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("dumped", len(bslib4.REG))
