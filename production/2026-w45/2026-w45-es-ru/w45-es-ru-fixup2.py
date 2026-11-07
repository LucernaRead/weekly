# -*- coding: utf-8 -*-
"""W45 ESxRU fix-up 2: geometry fixes from build 1 + first occlusion run.

1. P6 exercise flow overflow (3 items clamped past bottom 2580): W45
   ESxEN precedent — P6 exercises 19pt/gap3 -> 18.5pt/gap2 (build copy
   only; P5 calls use size=20/gap=8 and are untouched).
2. P8 answer flow overflow (9 items clamped): W45 ESxEN precedent —
   answer lines 13.5pt/1.16 -> 13.2pt/1.12, section separators
   1.16 -> 1.12 (dash style and generation code otherwise unchanged).
3. P7 column-3 overgrowth (preview box pushed to y=2691, off-page):
   telegraphic trims of the Russian notes only (Spanish frozen lines
   untouched), restoring preview geometry to ~core (preview y 2437.6
   vs core 2440.08; box bottom 2555.6, 24.4px above the footer rule):
   errs notes -3 lines, palabra note 4 -> 2 lines, disclosure note
   7 -> 3 lines (all three disclosure facts kept; the trailing
   invitation clause is dropped, same class as ESxEN's dropped
   trailing call — the letters box itself still invites letters).
4. P2/P5 box-title BOXTITLE flags (Russian titles crossing the box
   border at x=961): shorten to the W43-style short forms.
All replacements literal with asserted counts.
"""
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
    print(f'  {total}x :: {old[:70]!r} -> {new[:70]!r}')

# 1. P6 exercise size (content56 P6 section only uses size=19, gap=3)
rep(['content56.py'], 'size=19, gap=3', 'size=18.5, gap=2', 18)
# 2. P8 answer size
rep(['content8.py'], 'af.para(f"— СТРАНИЦА {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
    'af.para(f"— СТРАНИЦА {pg} —", 14, "sans", True, OLIVE, lh=1.12, gap=2, split=False)', 1)
rep(['content8.py'], 'af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)',
    'af.para(txt, 13.2, lh=1.12, gap=0.5, split=False)', 1)
# 3a. errs notes (Russian only)
rep(['content7.py'], 'mejor уже сравнительная степень, más не нужен.',
    'mejor уже сравнение: без más.', 1)
rep(['content7.py'], 'gente — собирательное существительное в единственном числе, глагол тоже.',
    'gente — единственное число: глагол тоже.', 1)
rep(['content7.py'], 'creo que выражает уверенность — изъявительное наклонение: es.',
    'creo que: изъявительное, es.', 1)
# 3b. palabra note 4 -> 2 lines (date fact kept: campaign from the 13th)
rep(['content7.py'], 'precampaña = предкампания: недели перед официальной кампанией. Весь выпуск — предкампания; кампания стартует в пятницу, 13-го.',
    'precampaña = предкампания: недели перед кампанией (с 13-го — кампания).', 2)
# 3c. disclosure note 7 -> 3 lines; three facts kept, invitation dropped
rep(['content7.py'], 'Примечание редакции: к сдаче номера настоящих писем читателей и лучших сочинений со страницы 8 не поступило, поэтому печатаем редакционный пример, а обещание переносится на VOL.3. Присылайте письма!',
    'Примечание редакции: писем и лучших текстов со страницы 8 нет; печатаем пример, обещание — на VOL.3.', 1)
# 4. box titles
rep(['content12.py'], 'EL CALENDARIO · Календарь недели', 'EL CALENDARIO · Календарь', 1)
rep(['content56.py'], 'EL PLAN DEL PUENTE · План на пуэнте', 'EL PLAN DEL PUENTE · План', 1)
print('FIXUP2 DONE')
