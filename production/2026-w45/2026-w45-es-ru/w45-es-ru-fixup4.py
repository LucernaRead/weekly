# -*- coding: utf-8 -*-
"""W45 ESxRU fix-up 4: P7 quote-5 gloss wrapped so its page label split
across two rendered lines ('(Страница' / '5)'). Shorten the gloss so
the note + label fit on one line at 19.5pt in the 896px quote column
(measured with svglib.wrap: 2 lines -> 1 line). Spanish quote untouched.
"""
import pathlib, sys

B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-ru-build')
p = B / 'content7.py'
t = p.read_text(encoding='utf-8')
old = '«Бернабеу» меняет газон на решётку: американский футбол приходит в Мадрид.'
new = '«Бернабеу» меняет газон на решётку: американский футбол в Мадриде.'
c = t.count(old)
if c != 1:
    print(f'COUNT MISMATCH: {old!r} found {c}, expected 1'); sys.exit(1)
p.write_text(t.replace(old, new), encoding='utf-8')
print('FIXUP4 DONE')
