# -*- coding: utf-8 -*-
"""Run the FR x DE weekly build files in ONE process so the exercise registry
(REG in bslib4) accumulates across pages: content12 -> 34 -> 56 -> 7 -> 8.
Single-process re-render rule (tools/README #7): never run a content module
standalone, never import one inside the core build dir."""
import runpy, sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
files = sys.argv[1:] or ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]
for f in files:
    print("=" * 24, f)
    runpy.run_path(f, run_name="__main__")
print("ALL DONE")
