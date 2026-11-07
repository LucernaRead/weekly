import runpy, json, sys, os
B = os.path.dirname(os.path.abspath(__file__))
os.chdir(B); sys.path.insert(0, B)
for f in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
json.dump(bslib4.REG, open(os.path.join(B,"scratch","reg-pt.json"),"w"), ensure_ascii=False, indent=1)
print("pt REG", len(bslib4.REG))
