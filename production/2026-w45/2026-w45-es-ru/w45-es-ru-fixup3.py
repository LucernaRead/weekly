# -*- coding: utf-8 -*-
"""W45 ESxRU fix-up 3: restore frozen Spanish body text corrupted by the
global P7-label replacement.

The main transform replaced 'Página N' -> 'Страница N' globally; that
also hit one frozen Spanish body string on P1 (BREVES EUROPA item,
'(Página 4)'), which must stay Spanish. The P7 quote labels (content7)
are the intended targets and are untouched by this fix. Count asserted.
"""
import pathlib, sys

B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-ru-build')
p = B / 'content12.py'
t = p.read_text(encoding='utf-8')
old = 'Villarreal–PSG. (Страница 4)'
new = 'Villarreal–PSG. (Página 4)'
c = t.count(old)
if c != 1:
    print(f'COUNT MISMATCH: {old!r} found {c}, expected 1'); sys.exit(1)
p.write_text(t.replace(old, new), encoding='utf-8')
print(f'  1x :: restored frozen BREVES (Página 4)')
print('FIXUP3 DONE')
