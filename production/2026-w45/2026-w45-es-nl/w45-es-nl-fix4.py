# -*- coding: utf-8 -*-
"""Fix 4: missed apparatus fragment (原形 acoger) in a P5 exercise stem,
found by the edition CJK scan (P5 edition CJK = 2). EN sibling renders
'(infinitive: acoger)'; NL renders '(infinitief: acoger)'."""
import pathlib, sys
B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-nl-build')
p = B / 'content56.py'
t = p.read_text(encoding='utf-8')
old, new = '(原形 acoger)', '(infinitief: acoger)'
c = t.count(old)
assert c == 1, c
p.write_text(t.replace(old, new), encoding='utf-8')
print('FIX4 OK')
