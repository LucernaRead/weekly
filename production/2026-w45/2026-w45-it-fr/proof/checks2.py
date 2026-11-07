import json, re, glob
from xml.etree import ElementTree as ET
from collections import Counter
G = '/home/hatch/workspace/goals/lucernaread-social-media-operations'
def texts(p):
    t = ET.parse(p)
    return [(el.get('x'), el.get('y'), el.get('font-size'), el.text or '') for el in t.iter() if el.tag.endswith('text') and (el.text or '').strip()]
def is_cjk(s):
    return any('\u4e00' <= c <= '\u9fff' for c in s)
# 1. freeze diff removed non-CJK
d = json.load(open(G+'/hidden_files/w45/it-fr-proof/freeze-diff.json'))
for pg, v in d['pages'].items():
    removed = v.get('removed', []) if isinstance(v, dict) else []
    noncjk = [s for s in removed if not is_cjk(s)]
    print(f"== {pg} removed_noncjk={len(noncjk)}")
    for s in noncjk: print(f"   REMOVED: {s!r}")
    added = v.get('added', []) if isinstance(v, dict) else []
    print(f"   added sample CJK? {[s for s in added if is_cjk(s)][:5]} added_total={len(added)}")
# 2. P8 extracts
import subprocess, sys
for lbl, p in [('CORE', G+'/files/weekly-report-w45-it-core/svg/p8-valutazione.svg'),
               ('ED', G+'/files/weekly-report-w45-it-fr/svg/p8-valutazione.svg')]:
    r = subprocess.run([G+'/tools/venv/bin/python', G+'/tools/p8.py', 'extract', '--p8', p, '--total', '150'],
                       capture_output=True, text=True)
    open(G+f'/hidden_files/w45/it-fr-proof/p8-extract-{lbl.lower()}.txt','w').write(r.stdout + r.stderr)
    print(f"--- p8 extract {lbl} rc={r.returncode} ---")
    print(r.stdout[:2000]); print(r.stderr[:500])
