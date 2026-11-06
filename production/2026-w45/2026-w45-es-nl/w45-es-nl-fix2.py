# -*- coding: utf-8 -*-
"""Fix 2 for W45 ESxNL: match_set type names (line-break pattern missed by
the transform loop) + P8 note trims (keys untouched) to clear the overflow."""
import pathlib, sys
B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-nl-build')
def rep(fn, old, new, expect):
    p = B / fn
    t = p.read_text(encoding='utf-8')
    c = t.count(old)
    if c != expect:
        print(f'COUNT MISMATCH {fn}: {old!r} found {c}, expected {expect}'); sys.exit(1)
    p.write_text(t.replace(old, new), encoding='utf-8')
    print(f'{fn}: {old!r} x{c}')
rep('content12.py', 'match_set("A2", "词汇配对",', 'match_set("A2", "Woorden combineren",', 1)
rep('content34.py', 'match_set("B1", "词汇配对",', 'match_set("B1", "Woorden combineren",', 1)
rep('content8.py', 'match_set("B2", "词汇配对",', 'match_set("B2", "Woorden combineren",', 1)
print('FIX2 type names OK')
