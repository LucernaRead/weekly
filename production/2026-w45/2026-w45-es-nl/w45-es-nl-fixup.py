# -*- coding: utf-8 -*-
"""W45 ESxNL layout fixups (W45 ESxEN KIT §3 precedents, wording-neutral):
P6 exercises 19pt/gap3 -> 18.5pt/gap2 (Dutch notes overflow at 19pt, as
English did); P8 answer lines 13.5pt/1.16 -> 13.2pt/1.12 (same reason).
Answer-generation code otherwise byte-identical (dash style untouched).
"""
import pathlib, sys
B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-nl-build')

def rep(fn, old, new, expect):
    p = B / fn
    t = p.read_text(encoding='utf-8')
    c = t.count(old)
    if c != expect:
        print(f'COUNT MISMATCH {fn}: {old!r} found {c}, expected {expect}'); sys.exit(1)
    p.write_text(t.replace(old, new), encoding='utf-8')
    print(f'{fn}: {old!r} x{c} -> {new!r}')

rep('content56.py', 'size=19, gap=3', 'size=18.5, gap=2', 18)
rep('content8.py', 'af.para(txt, 13.5, lh=1.16', 'af.para(txt, 13.2, lh=1.12', 1)
rep('content8.py', 'lh=1.16, gap=2', 'lh=1.12, gap=2', 1)
print('FIXUP OK')
