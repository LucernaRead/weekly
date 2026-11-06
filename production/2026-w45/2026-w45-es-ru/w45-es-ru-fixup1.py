# -*- coding: utf-8 -*-
"""W45 ESxRU fix-up 1: two literals the main transform missed (found by
the post-transform residue scan). Literal replacements with asserted
counts, build copy only."""
import pathlib, sys

B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-ru-build')

def rep(files, old, new, expect):
    total = 0
    for fn in files:
        p = B / fn
        t = p.read_text(encoding='utf-8')
        c = t.count(old)
        total += c
        if c:
            p.write_text(t.replace(old, new), encoding='utf-8')
    if total != expect:
        print(f'COUNT MISMATCH: {old!r} found {total}, expected {expect}'); sys.exit(1)
    print(f'  {total}x :: {old!r} -> {new!r}')

# P8 B-section note missed by the main pair list
rep(['content8.py'], '马竞–巴萨与 NFL 都在周日',
    '«Атлетико» — «Барса» и NFL — в воскресенье', 1)
# P5 C-section notes: bare grammatical term in Spanish notes
rep(['content56.py'], '原形', 'инфинитив', 4)
print('FIXUP1 DONE')
