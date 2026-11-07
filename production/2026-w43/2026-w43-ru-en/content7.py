# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ru-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ЯЗЫК (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ЯЗЫК · Language", "Lucerna", "Фокус на язык · Три уровня, три темы · Three levels, three topics")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · ПОГОДА СЛОВАМИ", 24)
a.para("О погоде говорим так: похолодает — станет холодно; выпадет снег — снег начнёт падать; растает — снег станет водой. Примеры из нашей газеты: «Завтра похолодает», «Снег выпадет и быстро растает».", 21.5)
a.para("Снег бывает разный: первый снег, мокрый снег (снег с дождём) и снежный покров (снег, который лежит на земле).", 21.5)
a.note("похолодает it turns cold; выпадет снег snow falls; растает it melts; мокрый снег wet snow.")
a.ex("A2", "fill-in", "похолодает", "похолодает = the temperature will drop",
     "«Завтра ___» — температура станет ниже.", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "fill-in", "мокрый", "мокрый снег = wet snow",
     "Снег с дождём — это ___ снег.", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "multiple choice", "B", "растает = turns into water",
     "«Снег растает» значит... A. снег будет идти · B. снег станет водой · C. снег будет лежать", size=20.5, gap=10)
a.ex("A2", "fill-in", "выпадет", "выпасть → выпадет",
     "Первый снег ___ в среду или в четверг. (выпасть)", instr="Fill in", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · ШКОЛА И ПОЗДРАВЛЕНИЯ", 24)
b.para("Слова недели: учебный день — день, когда есть уроки; каникулы — время без уроков; отдыхать — не работать и не учиться. Пример: «А потом — каникулы!»", 21.5)
b.para("Поздравляем так: поздравляю + с + творительный падеж. «Поздравляю с праздником!», «Поздравляю с Днём отца!» Слово после «с» меняется: праздник → с праздником, день → с днём.", 21.5)
b.note("поздравляю + с + instrumental: с праздником, с Днём отца — the fixed Russian greeting formula.")
b.ex("B1", "fill-in", "уроков", "без + genitive: без уроков",
     "Каникулы — это время без ___.", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "fill-in", "праздником", "с + instrumental: с праздником",
     "Поздравляю с ___ ! (праздник)", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "fill-in", "днём", "с + instrumental: с днём",
     "Поздравляю с ___ рождения! (день)", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "multiple choice", "B", "Correct form: с праздником",
     "Как правильно? A. Поздравляю с праздник! · B. Поздравляю с праздником! · C. Поздравляю праздника!", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · ПРОГНОЗ И ВЕРОЯТНОСТЬ", 24)
c.para("Синоптики говорят осторожно: «по прогнозу» — по данным прогноза; «вероятно» — скорее да, чем нет; «синоптики обещают снег» — обещать + инфинитив. Если два прогноза разные, мы говорим: прогнозы не совпадают.", 21.5)
c.para("Ещё слова: «может выпасть» — возможно, выпадет; «настоящий снежный покров» — снег, который лежит долго и не тает. Говорить «может быть» и «вероятно» — признак хорошего уровня!", 21.5)
c.note("по прогнозу according to the forecast; вероятно probably; обещать + infinitive — how to sound unsure.")
c.ex("B2", "fill-in", "По", "по прогнозу = according to the forecast",
     "___ прогнозу, завтра будет снег.", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "fill-in", "обещают", "обещать → обещают",
     "Синоптики ___ снег в среду. (обещать)", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "multiple choice", "B", "вероятно = more likely than not",
     "«Вероятно» значит... A. точно да · B. скорее да, чем нет · C. точно нет", size=20.5, gap=10)
c.ex("B2", "fill-in", "расходятся", "прогнозы расходятся = the forecasts disagree",
     "Если два прогноза разные, прогнозы ___.", instr="Fill in", size=20.5, gap=10)
c.end_report()

# ---- col 3: error clinic + word + letters ----
bx = COLX[3]
errs = [
    ("«Поздравляю с День отца!»", "→ После «с» нужен творительный падеж: «с Днём отца!»", "Instrumental after «с»: с Днём отца."),
    ("«Мы едем к бабушка»", "→ После «к» — дательный падеж: «Мы едем к бабушке».", "Dative after «к»: к бабушке."),
    ("«У «Зенита» 24 очков»", "→ После 2, 3, 4 — «очка» (24 очка), после 5 — «очков» (25 очков).", "2, 3, 4 → очка; 5 and up → очков."),
    ("«Конкурс с первый октябрь»", "→ «С» (начало) требует родительного падежа: «с первого октября».", "«С» (a start) + genitive: с первого октября."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ОШИБКИ · Error clinic", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "«единоличный лидер» — команда, которая одна стоит на первом месте: у неё больше очков, чем у всех других. Сейчас единоличный лидер — «Динамо»."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("единоличный лидер = the team alone in first place.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "СЛОВО · Word box", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "единоличный лидер = the team alone in first place.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "«Здравствуйте! Я учу русский язык в Пекине. У нас снег бывает редко, а я очень жду первый снег — как москвичи!» — Ли (пример от редакции)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("An editor's example, not a real letter. VOL.2 prints real letters and best writing!", "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "ПИСЬМА ЧИТАТЕЛЕЙ", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "An editor's example, not a real letter. VOL.2 prints real letters and best writing!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- phrases of the week (verbatim from this issue) ----
fy = 1712
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "ФРАЗЫ НЕДЕЛИ · Phrases of the week (verbatim from this issue)", 27, "sans", True, OLIVE)
quotes = [
    ("«Первый снег может выпасть уже на этой неделе»", "The first snow may fall as early as this week.", "Страница 1"),
    ("«Прогнозы расходятся: один синоптик обещает снег в среду, а другой — мокрый снег в конце октября»", "The forecasts disagree: one forecaster promises snow on Wednesday, another wet snow at the end of October.", "Страница 2"),
    ("«Когда на улице плюс пять — семь градусов, пора менять резину»", "When it is plus five to seven degrees outside, it is time to change your tires.", "Страница 2"),
    ("«Друзья мои, прекрасен наш союз!»", "From Pushkin's “19 October”: My friends, how beautiful our union is!", "Страница 3"),
    ("«В четверг в кино выходят сразу четыре сказки»", "On Thursday, no fewer than four fairy-tale films open at once.", "Страница 3"),
    ("«Динамо — единоличный лидер: у него 25 очков»", "Dynamo are the sole leaders: 25 points.", "Страница 4"),
    ("«В субботу, 31 октября, Москва празднует Хэллоуин»", "On Saturday, 31 October, Moscow celebrates Halloween.", "Страница 5"),
    ("«Каникулы получаются длинными: двенадцать дней подряд»", "The holidays turn out long: twelve days in a row.", "Страница 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "СЛЕДУЮЩАЯ НЕДЕЛЯ · Next week (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Кто победил в дерби ЦСКА — «Спартак»? И выпал ли первый снег? В среду, 28 октября, — День бабушек и дедушек, а в субботу — Хэллоуин. И главное: начинаются каникулы! Плюс ваши письма и лучшие сочинения со страницы 8. До понедельника!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-yazyk.svg")
print("P7 saved, exercises so far:", len(REG))
