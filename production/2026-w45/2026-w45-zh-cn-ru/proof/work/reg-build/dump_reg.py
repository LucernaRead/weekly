import runpy, sys, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)) if '__file__' in dir() else os.getcwd())
for f in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
from collections import Counter
reg=bslib4.REG
out={"total":len(reg),"by_level":dict(Counter(e["level"] for e in reg)),
     "by_page":dict(sorted(Counter(e["page"] for e in reg).items())),
     "by_type":dict(Counter(e["type"] for e in reg)),
     "items":[{"n":e.get("n"),"page":e.get("page"),"level":e.get("level"),"type":e.get("type"),"key":e.get("key"),"note":e.get("note")} for e in reg]}
# writing model length: find MODELO in content8 namespace? use bslib4? print keys
print("TOTAL",len(reg),"LEVELS",out["by_level"],"PAGES",out["by_page"],"TYPES",out["by_type"])
json.dump(out,open(sys.argv[1],'w',encoding='utf-8'),ensure_ascii=False,indent=1)
