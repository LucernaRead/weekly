import sys, os, json, runpy
# usage: dump_reg.py <build_dir> <out_json>
d = sys.argv[1]
sys.path.insert(0, d)
os.chdir(d)
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(os.path.join(d, f), run_name="__main__")
import bslib4
out = [{"n": e["n"], "page": e["page"], "level": e["level"], "type": e["type"],
        "key": e.get("key"), "note": e.get("note")} for e in bslib4.REG]
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("dumped", len(out))
