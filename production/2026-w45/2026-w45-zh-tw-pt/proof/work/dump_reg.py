# -*- coding: utf-8 -*-
import runpy, sys, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
out = sys.argv[1]
json.dump(bslib4.REG, open(out, "w"), ensure_ascii=False, indent=1)
print("dumped", len(bslib4.REG), "to", out)
