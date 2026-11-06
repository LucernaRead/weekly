import runpy, sys, os, json
os.chdir("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/es-fr-proof/core-reg/build")
for f in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
json.dump(bslib4.REG, open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/es-fr-proof/core-reg/reg.json","w"), ensure_ascii=False, indent=1)
print("core REG", len(bslib4.REG))
