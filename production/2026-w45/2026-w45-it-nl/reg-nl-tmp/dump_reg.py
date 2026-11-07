# -*- coding: utf-8 -*-
"""Dump the exercise registry (REG) as JSON after running a build copy's
content modules in ONE process. Usage: dump_reg.py <build-dir> <out.json>.
The build copy's OUT paths must already point at a scratch dir (never run
this inside a shipped build dir)."""
import runpy, sys, os, json
d = sys.argv[1]
absdir = os.path.abspath(d)
os.chdir(d)
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(os.path.join(absdir, f), run_name="__main__")
sys.path.insert(0, absdir)
import bslib4
json.dump(bslib4.REG, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('dumped', len(bslib4.REG))
