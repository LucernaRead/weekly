import content12, content34, content56, content7, content8
import bslib4, json
from collections import Counter
REG=bslib4.REG
print("total",len(REG))
print("levels",Counter(e['level'] for e in REG))
print("pages",Counter(e['page'] for e in REG))
NOTE_EXTRA={11,12,14,19,29,30,31,33,41,44,47,48,51,58,64,66,67,68,69,71,74,88,89,91,92,93,102}
printed=[e['n'] for e in REG if e['note'] and (e['page']==8 or len(e['note'])<=10 or e['type'] in ("Correzione","Lettura del grafico") or e['n'] in NOTE_EXTRA)]
print("ed-rule printed",len(printed),printed)
json.dump(REG,open('hidden_files/w45/en-it-proof/regdump-ed/ed-REG.json','w'),ensure_ascii=False,indent=1)
