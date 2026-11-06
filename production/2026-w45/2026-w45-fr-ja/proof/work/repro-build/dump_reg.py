import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content12, content34, content56, content7, content8
import bslib4
from collections import Counter
reg=bslib4.REG
print('total', len(reg))
print('levels', dict(Counter(r['level'] for r in reg)))
print('pages', {p: len([r for r in reg if r['page']==p]) for p in sorted(set(r['page'] for r in reg))})
print('keys sample 107,120,135,150:', [(r['n'], r['key']) for r in reg if r['n'] in (107,120,135,150)])
json.dump(reg, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reg.json'),'w'), ensure_ascii=False)
