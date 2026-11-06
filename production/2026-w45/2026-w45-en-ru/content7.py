# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-en-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND · Разбор", "The Lucerna", "A2 → B2 · Phrases of the week · Фразы недели")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("LEVEL A2 · База", 27)
cA.head("FALLING BACK", 24)
cA.para("« The clocks fell back. » Fall back = to go back one hour. The past is fell back, not « falled back ». The repeated hour on November 1 is the example of the week (page 2).", 22.5)
cA.head("GOING TO + VERB", 24)
cA.para("For a plan : « She is going to vote on Tuesday. » be + going to + the verb, with no change. It is the friendliest future in English — use it for every plan of the week.", 22.5)
cA.box("THE EXAMPLE · Пример", [
    ("« Americans are going to vote on Tuesday. » — the election story, from page 1.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("LEVEL B1 · Средний", 27)
cB.head("COMPARATIVES", 24)
cB.para("Short adjective + -er + than : « The Bernabéu is bigger than most stadiums. » Long adjective : more + adjective : « more convenient ». And good becomes better — never « more good ». Page 4 is full of them.", 22.5)
cB.head("THE PAST SIMPLE", 24)
cB.para("Regular verbs add -ed : changed, watched. Irregular verbs change : fall → fell, go → went, choose → chose. Use it for what is already finished — the clocks that fell back on November 1, and the « as-if-finished » retellings on page 4. The November 3 election and the November 8 games are still to come at press time, so their results are not past yet.", 22.5)
cB.box("THE EXAMPLE · Пример", [
    ("« The clocks fell back on Sunday, November 1. » — fall → fell (page 2).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW)], 200, 1150, tag="P7-B2")
cC.head("LEVEL B2 · Сложный", 27)
cC.head("HEADLINE PRESENT", 24)
cC.para("Headlines speak of yesterday in the present : « America votes », « Bengals play in Madrid ». The present simple makes old news feel live. Read the front page again and find three.", 22.5)
cC.head("WHETHER = IF ?", 24)
cC.para("« Nobody knows whether the race is called yet. » Whether introduces an open question inside a sentence — more elegant than if, and safe everywhere. It is the word for election-night uncertainty.", 22.5)
cC.box("THE EXAMPLE · Пример", [
    ("« Patience is part of the system, not a failure of it. » — part of = часть (page 6).", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-tools")
cD.head("THE TOOLBOX · Инструменты", 27)
cD.para("Three sentences to keep in your pocket, one for each level :", 22.5)
cD.para("A2 — « It is one o'clock — again ! »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « The clocks fell back on Sunday. »", 22.5)
cD.para("B2 — « Nobody knows whether the race is called yet. »", 22.5, "serif", True, OLIVE)
cD.para("And the newspaper reflex : every phrase of the week comes from an article of this issue. Re-read the article, and the phrase becomes easy.", 22.5)
cD.bridge("Три фразы на каждый день, по одной на уровень; все фразы недели — из статей этого номера: перечитай оригинал, и они запомнятся.")
cD.end_report()

# --- phrases of the week ---
py = 1210
p.hline(MX, RIGHT, py - 14, GOLD, 2)
p.text(MX, py + 26, "PHRASES OF THE WEEK · Фразы недели", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "К каждой фразе — грамматика и вопрос · Ответы на стр. 8", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« Tuesday, November 3, is Election Day in the United States. » (page 1)",
     "Грамматика — is = быть; дата — именная часть сказуемого.",
     "A2", "Election Day ___ on Tuesday, November 3. (be)", "is", "is = быть"),
    ("« The hour from 1 to 2 happened twice. » (page 2)",
     "Грамматика — прошедшее время happen — happened, правильное образование.",
     "A2", "The hour ___ twice on Sunday. (happen)", "happened", "happen → happened"),
    ("« Which film would you choose ? » (page 3)",
     "Грамматика — would + инфинитив выражает предпочтение.",
     "B1", "Which film ___ you choose ? (would)", "would", "would + инфинитив"),
    ("« Two games, two continents, one league — that is the modern NFL. » (page 4)",
     "Грамматика — that is = то есть; после тире — итог.",
     "B1", "That ___ the modern NFL. (be)", "is", "that is = то есть"),
    ("« The results will still be there in the morning. » (page 5)",
     "Грамматика — will still = всё ещё; still стоит после will.",
     "B2", "The results ___ still be there. (will)", "will", "will still = всё ещё"),
    ("« Patience is part of the system, not a failure of it. » (page 6)",
     "Грамматика — part of = часть; not даёт противопоставление.",
     "B2", "Patience ___ part of the system. (be)", "is", "is part of = часть"),
    ("« Not every place changes. » (page 2)",
     "Грамматика — not every + глагол в ед. ч.: меняется не всё.",
     "A2", "Not every place ___ . (change)", "changes", "not every → changes"),
    ("« One Sunday is not enough — good thing the week has seven days. » (page 4)",
     "Грамматика — has = иметь; the week в ед. ч. требует has.",
     "B1", "The week ___ seven days. (have)", "has", "have → has"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 20.5, "serif", True, INK, 1.34, 3)
    pf.bridge(point, 19, 4)
    pf.ex(lv, "Потренироваться", key, note, q, size=20.5)
pf.end_report()

# --- bottom: clinic (left) + readers' corner & teaser (right) ---
by7 = 1870
p.hline(MX, RIGHT, by7 - 14, GOLD, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("THE ERROR CLINIC · Ошибки", 25)
cf.bridge("В каждой фразе одна ошибка: найди и исправь её.")
cf.ex("A2", "Исправить", "He doesn't like voting early.", "отрицание в 3-м лице: doesn't + инфинитив",
     "✗ « He don't like voting early. »", instr="Исправь", size=22.5)
cf.ex("A2", "Исправить", "Yesterday the clocks fell back.", "прошедшее время fall — fell",
     "✗ « Yesterday the clocks falled back. »", instr="Исправь", size=22.5)
cf.ex("B1", "Исправить", "This game is bigger than last week's.", "bigger уже сравнительная степень: more не нужно",
     "✗ « This game is more bigger than last week's. »", instr="Исправь", size=22.5)
cf.ex("B1", "Исправить", "She is going to watch the film on Friday.", "после going to — инфинитив",
     "✗ « She is going to watches the film on Friday. »", instr="Исправь", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(rx + 24, by7 + 48, "READERS' CORNER · Уголок читателя", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)", 21.5, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 206, "Примечание редакции: в VOL.1 было обещано публиковать настоящие письма в VOL.2, но к сдаче номера редакция не получила ни настоящих писем, ни лучшего сочинения с 8-й страницы VOL.1; мы ничего не выдумываем, а пример остаётся помеченным. Присылайте ваши письма и сочинения! В VOL.3 мы опубликуем полученные письма.", 20, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 332
p.rect(rx, ty7, rw, 2540 - ty7, fill=DARK)
p.text(rx + 24, ty7 + 46, "NEXT WEEK · VOL.3 · Анонс", 24, "sans", True, "#f3edda")
p.para(rx + 24, ty7 + 84, "Wednesday, November 11 : Veterans Day. Sunday, November 15 : the NFL in Munich. And the midterm results, reported — who won, and what changes.", 21.5, "serif", False, "#e8dfc8", rw - 48, 1.45)
p.para(rx + 24, ty7 + 218, "В среду — День ветеранов; в воскресенье — матч NFL в Мюнхене; а также итоги промежуточных выборов.", 20, "sans", False, "#b3a06a", rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
