import runpy, sys, os, json, collections
os.chdir('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-es-proof/work/replay')
for f in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
    runpy.run_path(f, run_name="__main__")
# REG lives in bslib4 module namespace? runpy separate namespaces share via import: import bslib4
import bslib4
REG=bslib4.REG
print("total", len(REG))
print("per-page", dict(sorted(collections.Counter(e['page'] for e in REG).items())))
print("per-level", dict(sorted(collections.Counter(e['level'] for e in REG).items())))
print("per-type", dict(sorted(collections.Counter(e['type'] for e in REG).items())))
print("sequential", [e['n'] for e in REG]==list(range(1,151)))
json.dump(REG, open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-es-proof/work/reg-dump.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
for e in REG:
    print(e['n'], e['page'], e['level'], e['type'], repr(e.get('key'))[:80])
