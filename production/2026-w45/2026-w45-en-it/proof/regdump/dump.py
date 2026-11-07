import content12, content34, content56, content7, content8
import bslib4, json
from collections import Counter
REG=bslib4.REG
print("total",len(REG))
# core printed rule from content8 source: note and (pg==8 or len(note)<=10 or type in (改错,图表读数))
printed=[e['n'] for e in REG if e['note'] and (e['page']==8 or len(e['note'])<=10 or e['type'] in ("改错","图表读数"))]
print("core-rule printed count",len(printed))
print(printed)
print("levels",Counter(e['level'] for e in REG))
print("pages",Counter(e['page'] for e in REG))
print("per-page-level",{p:dict(Counter(e['level'] for e in REG if e['page']==p)) for p in range(1,9)})
# also: items with empty note
print("empty-note",[e['n'] for e in REG if not e['note']])
json.dump(REG,open('hidden_files/w45/en-it-proof/regdump/core-REG.json','w'),ensure_ascii=False,indent=1)
