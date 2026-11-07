# -*- coding: utf-8 -*-
"""One-process REG dump for a build copy whose OUT is already repointed
to a scratch dir. Usage: dump_reg.py <build-dir> <out-json>"""
import runpy, sys, os, json
d = sys.argv[1]
os.chdir(d)
sys.path.insert(0, d)
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(os.path.join(d, f), run_name="__main__")
import bslib4
json.dump(bslib4.REG, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("dumped", len(bslib4.REG))
