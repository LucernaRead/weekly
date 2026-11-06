# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-en-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND · Разбор", "The Lucerna", "A2 → B2 · Phrases of the week · Фразы недели")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("LEVEL A2 · База", 27)
cA.head("TELLING THE TIME", 24)
cA.para("It's eight o'clock. · It's half past two. · It's a quarter to eight. For the hour, English always starts with « It's » — never « it has ». The three clocks on page 2 show the week's three times.", 22.5)
cA.head("GOING TO + VERB", 24)
cA.para("For a plan : « She is going to vote on Saturday. » be + going to + the verb, with no change. It is the friendliest future in English — use it for every plan of the week.", 22.5)
cA.box("THE EXAMPLE · Пример", [
    ("« Checks are going to grow in January. » — the Social Security story, from page 2.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("LEVEL B1 · Средний", 27)
cB.head("COMPARATIVES", 24)
cB.para("Short adjective + -er + than : « Austin is hotter than Milwaukee. » Long adjective : more + adjective : « more convenient ». And good becomes better — never « more good ». Page 4 and page 6 are full of them.", 22.5)
cB.head("THE PAST SIMPLE", 24)
cB.para("Regular verbs add -ed : raised, watched. Irregular verbs change : win → won, sweep → swept, beat → beat, go → went. Sports pages are written in this tense — every result is past.", 22.5)
cB.box("THE EXAMPLE · Пример", [
    ("« Maxey scored more points than Brunson. » — comparison and past simple in one line (page 4).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW)], 200, 1150, tag="P7-B2")
cC.head("LEVEL B2 · Сложный", 27)
cC.head("HEADLINE PRESENT", 24)
cC.para("Headlines speak of yesterday in the present : « 76ers win opener », « Early voting opens in Texas ». The present simple makes old news feel live. Read the front page again and find three.", 22.5)
cC.head("WHETHER = IF ?", 24)
cC.para("« Nobody knows whether the Brewers can finish the story. » Whether introduces an open question inside a sentence — more elegant than if, and safe everywhere. It is the word of the deep read (page 6).", 22.5)
cC.box("THE EXAMPLE · Пример", [
    ("« Voting is no longer a day ; it is a season. » — no longer = больше не (page 6).", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-tools")
cD.head("THE TOOLBOX · Инструменты", 27)
cD.para("Three sentences to keep in your pocket, one for each level :", 22.5)
cD.para("A2 — « It's a quarter to eight. »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « The 76ers won, and Maxey scored more than Brunson. »", 22.5)
cD.para("B2 — « Nobody knows whether the story ends with a trophy. »", 22.5, "serif", True, OLIVE)
cD.para("And the newspaper reflex : every phrase of the week comes from an article of this issue. Re-read the article, and the phrase becomes easy.", 22.5)
cD.expl("Пояснение — Три фразы этого выпуска — по одной на уровень; все фразы взяты из статей выпуска, перечитайте их в тексте.")
cD.end_report()

# --- phrases of the week ---
py = 1210
p.hline(MX, RIGHT, py - 14, GOLD, 2)
p.text(MX, py + 26, "PHRASES OF THE WEEK · Фразы недели", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "К каждой фразе — грамматика и задание · Ответы на странице 8", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« On Tuesday, October 20, the 2026–27 season opened with something new : a tripleheader. » (page 4)",
     "Грамматика — Past Simple: open → opened, правильный глагол.",
     "B1", "The World Series ___ (open) on Friday.", "opened", "open → opened"),
    ("« When the prices of food, homes and energy go up, the checks go up too. » (page 2)",
     "Грамматика — go up = расти; в придаточном с when — Present Simple (о закономерностях).",
     "A2", "When energy costs more, the bills ___ too. (go up)", "go up", "go up = расти"),
    ("« Milwaukee swept the Los Angeles Dodgers. » (page 4)",
     "Грамматика — прошедшее время от sweep — swept (неправильный глагол).",
     "B1", "Tampa Bay ___ (beat) Cleveland on Monday.", "beat", "beat → beat (без изменений)"),
    ("« Neither club has ever won the World Series. » (page 4)",
     "Грамматика — neither + глагол в единственном числе: ни один из двух (не выигрывал).",
     "B2", "Neither team ___ (have) a trophy yet.", "has", "neither → has"),
    ("« Voting is no longer a day ; it is a season. » (page 6)",
     "Грамматика — no longer = больше не; ставится после глагола be.",
     "B2", "The game is ___ on television only ; it is on phones too.", "no longer", "no longer = больше не"),
    ("« Voters head to the polls. » (page 6)",
     "Грамматика — head to = отправляться (настоящее время в заголовках).",
     "A2", "On Tuesday, fans ___ to the stadium. (head)", "head", "fans → head (основная форма)"),
    ("« The average retired worker will get about 75 dollars more every month. » (page 2)",
     "Грамматика — about = примерно: для приблизительных чисел.",
     "A2", "The average check is ___ two thousand dollars a month.", "about", "about = примерно"),
    ("« In Europe, the clocks fall back on Sunday — in America, on Sunday, November 1. » (page 2)",
     "Грамматика — fall back = переводить (часы) назад; весной — spring forward.",
     "B1", "In spring, the clocks ___ forward. (spring)", "spring", "spring forward — стрелки вперёд"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 20.5, "serif", True, INK, 1.34, 3)
    pf.expl(point, 19, 4)
    pf.ex(lv, "Практика", key, note, q, size=20.5)
pf.end_report()

# --- bottom: clinic (left) + readers' corner & teaser (right) ---
by7 = 1870
p.hline(MX, RIGHT, by7 - 14, GOLD, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("THE ERROR CLINIC · Ошибки", 25)
cf.expl("В каждом предложении одна ошибка: найдите и исправьте её.")
cf.ex("A2", "Исправление ошибки", "I agree with you.", "agree — глагол, am перед ним не нужен",
     "✗ « I am agree with you. »", instr="Исправьте", size=22.5)
cf.ex("A2", "Исправление ошибки", "Yesterday I went to the game.", "прошедшее время от go — went",
     "✗ « Yesterday I go to the game. »", instr="Исправьте", size=22.5)
cf.ex("B1", "Исправление ошибки", "This week is busier than last week.", "busier уже сравнительная степень, more не нужен",
     "✗ « This week is more busier than last week. »", instr="Исправьте", size=22.5)
cf.ex("B1", "Исправление ошибки", "He doesn't like early voting.", "отрицание в третьем лице: doesn't + инфинитив",
     "✗ « He don't like early voting. »", instr="Исправьте", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(rx + 24, by7 + 48, "READERS' CORNER · Уголок читателя", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« This autumn, I read my first book in English — one page every night, with Lucerna. » — R. T., a reader in Toronto (editor's example : the first real reader letters will take this place in VOL.2)", 21.5, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 206, "Ответ редакции — one page every night — самая надёжная привычка: Present Simple как раз о привычках. Примечание: это письмо — образец редакции; с VOL.2 мы публикуем настоящие письма читателей и разбираем сочинения с 8-й страницы.", 20, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 332
p.rect(rx, ty7, rw, 2540 - ty7, fill=DARK)
p.text(rx + 24, ty7 + 46, "NEXT WEEK · VOL.2 Анонс", 24, "sans", True, "#f3edda")
p.para(rx + 24, ty7 + 84, "Saturday, October 31 : Halloween night, live. Sunday, November 1 : America falls back — one more hour of sleep. Tuesday, November 3 : Election Day. What do Americans read, watch and eat while they wait for the results ?", 21.5, "serif", False, "#e8dfc8", rw - 48, 1.45)
p.para(rx + 24, ty7 + 218, "В следующую субботу — ночь Хэллоуина, в воскресенье вся Америка переводит часы назад, а во вторник, 3 ноября, — день выборов.", 20, "sans", False, "#b3a06a", rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
