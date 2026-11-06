import sys, os, json, runpy
sys.path.insert(0, os.path.abspath("."))
os.chdir(os.path.abspath("."))
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
json.dump(bslib4.REG, open("/tmp/zhtw-fr-reg.json", "w"), ensure_ascii=False, indent=1)
print("dumped", len(bslib4.REG))
