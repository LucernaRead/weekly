import sys, os, json, runpy
# re-run in one process with OUT pointed at scratch to dump REG without touching delivery
import shutil
os.makedirs('/tmp/nl-reg-scratch', exist_ok=True)
# monkeypatch: run content modules via runpy but redirect OUT by editing? simpler: import bslib4 REG after run
# Instead: run run.py in-process (it writes delivery SVGs again, identical) then dump REG from bslib4 module state
sys.path.insert(0, '.')
import bslib4
# run.py uses runpy per file with run_name __main__; REG lives in bslib4 module imported by contents
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
from collections import Counter
reg = bslib4.REG
print('total', len(reg))
print('levels', dict(Counter(e['level'] for e in reg)))
print('pages', dict(Counter(e['page'] for e in reg)))
print('types', dict(Counter(e['type'] for e in reg)))
print('numbers continuous:', [e['n'] for e in reg] == list(range(1, 151)))
json.dump(reg, open('reg-dump.json', 'w', encoding='utf-8'), ensure_ascii=False)
