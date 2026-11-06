# Registry dump driver: runs content modules in ONE process (like run.py)
# inside a scratch copy only, then dumps bslib4.REG to reg.json in cwd.
# Never run in a shipped build dir.
import runpy, sys, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.getcwd())
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
with open("reg.json", "w", encoding="utf-8") as fh:
    json.dump(bslib4.REG, fh, ensure_ascii=False, indent=1)
print("DUMPED", len(bslib4.REG))
