# -*- coding: utf-8 -*-
"""Fix 3 for W45 ESxNL: telegraphic P8-note trims (W43 ESxNL round-2
precedent). Keys untouched; each trim verified 2 -> 1 wrapped lines at
serif 13.2 / width 434 with the build's own wrap(). Saves 4 lines (~60px)
against the 15px P8-keys overflow."""
import pathlib, sys
B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-nl-build')
def rep(fn, old, new, expect):
    p = B / fn
    t = p.read_text(encoding='utf-8')
    c = t.count(old)
    if c != expect:
        print(f'COUNT MISMATCH {fn}: {old!r} found {c}, expected {expect}'); sys.exit(1)
    p.write_text(t.replace(old, new), encoding='utf-8')
    print(f'{fn}: trimmed {old[:40]!r}...')
rep('content12.py', "de lijsten zijn ingediend; nu worden de programma's geschreven",
    "lijsten ingediend; nu de programma's geschreven", 1)
rep('content34.py', 'de DANA-herdenking was op donderdag 29 oktober',
    'DANA-herdenking: donderdag 29 oktober', 1)
rep('content56.py', 'een peiling is een momentopname met een foutmarge, van één dag',
    'een peiling: momentopname met foutmarge, van één dag', 1)
rep('content8.py', "Ana kijkt alleen naar de NFL; Pablo kijkt 's avonds naar Atlético–Barça",
    "Ana: alleen NFL; Pablo: Atlético–Barça 's avonds", 1)
print('FIX3 OK')
