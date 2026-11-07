# -*- coding: utf-8 -*-
"""Dump the exercise registry from a build COPY (never the real build dir).
Usage: dump_driver.py <copy-dir> <svg-out-dir> <json-out>
Repoints OUT lines in the copy first, then runs content modules in ONE
process (same order as run.py), then dumps bslib4.REG."""
import json, os, runpy, sys

copy_dir, svg_out, json_out = sys.argv[1], sys.argv[2], sys.argv[3]
for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    p = os.path.join(copy_dir, fn)
    lines = open(p, encoding="utf-8").read().split("\n")
    done = 0
    for i, ln in enumerate(lines):
        if ln.startswith("OUT = os.path.expanduser("):
            lines[i] = f'OUT = os.path.expanduser("{svg_out}")'
            done += 1
    assert done == 1, f"{fn}: OUT lines {done}"
    open(p, "w", encoding="utf-8").write("\n".join(lines))
os.chdir(copy_dir)
sys.path.insert(0, copy_dir)
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(os.path.join(copy_dir, f), run_name="__main__")
import bslib4
reg = [{"n": e["n"], "level": e["level"], "page": e["page"], "type": e["type"],
        "key": e["key"], "note": e["note"]} for e in bslib4.REG]
json.dump(reg, open(json_out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"dumped {len(reg)}")
