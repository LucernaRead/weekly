import runpy, sys, os, json
out = os.path.abspath(sys.argv[1])
os.chdir(sys.argv[2])
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
json.dump(bslib4.REG, open(out, "w"), ensure_ascii=False, indent=1)
print("dumped", len(bslib4.REG), "to", out)
