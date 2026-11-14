# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ЯЗЫК (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ЯЗЫК　Lengua", "Lucerna", "Фокус на язык　Три уровня, три темы　Tres niveles, tres temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　ПОГОДА СЛОВАМИ", 24)
a.para("О погоде говорим так: похолодает — станет холодно; выпадет снег — снег начнёт падать; растает — снег станет водой. Примеры из нашей газеты: «Завтра похолодает», «Снег выпадет и быстро растает».", 21.5)
a.para("Снег бывает разный: первый снег, мокрый снег (снег с дождём) и снежный покров (снег, который лежит на земле).", 21.5)
a.expl("похолодает hará más frío; выпадет снег caerá nieve; растает se derretirá; мокрый снег aguanieve.")
a.ex("A2", "Completar", "похолодает", "похолодает = bajará la temperatura",
     "«Завтра ___» — температура станет ниже.", instr="Completar", size=20.5, gap=10)
a.ex("A2", "Completar", "мокрый", "мокрый снег = aguanieve",
     "Снег с дождём — это ___ снег.", instr="Completar", size=20.5, gap=10)
a.ex("A2", "Opción múltiple", "B", "растает = se convierte en agua",
     "«Снег растает» значит... A. снег будет идти · B. снег станет водой · C. снег будет лежать", size=20.5, gap=10)
a.ex("A2", "Completar", "выпадет", "выпасть → выпадет",
     "Первый снег ___ в среду или в четверг. (выпасть)", instr="Completar", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　ШКОЛА И ПОЗДРАВЛЕНИЯ", 24)
b.para("Слова недели: учебный день — день, когда есть уроки; каникулы — время без уроков; отдыхать — не работать и не учиться. Пример: «А потом — каникулы!»", 21.5)
b.para("Поздравляем так: поздравляю + с + творительный падеж. «Поздравляю с праздником!», «Поздравляю с Днём отца!» Слово после «с» меняется: праздник → с праздником, день → с днём.", 21.5)
b.expl("поздравляю + с + instrumental: с праздником, с Днём отца — la fórmula fija rusa para felicitar.")
b.ex("B1", "Completar", "уроков", "без + genitivo: без уроков",
     "Каникулы — это время без ___.", instr="Completar", size=20.5, gap=10)
b.ex("B1", "Completar", "праздником", "с + instrumental: с праздником",
     "Поздравляю с ___ ! (праздник)", instr="Completar", size=20.5, gap=10)
b.ex("B1", "Completar", "днём", "с + instrumental: с днём",
     "Поздравляю с ___ рождения! (день)", instr="Completar", size=20.5, gap=10)
b.ex("B1", "Opción múltiple", "B", "La forma correcta: с праздником",
     "Как правильно? A. Поздравляю с праздник! · B. Поздравляю с праздником! · C. Поздравляю праздника!", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　ПРОГНОЗ И ВЕРОЯТНОСТЬ", 24)
c.para("Синоптики говорят осторожно: «по прогнозу» — по данным прогноза; «вероятно» — скорее да, чем нет; «синоптики обещают снег» — обещать + инфинитив. Если два прогноза разные, мы говорим: прогнозы не совпадают.", 21.5)
c.para("Ещё слова: «может выпасть» — возможно, выпадет; «настоящий снежный покров» — снег, который лежит долго и не тает. Говорить «может быть» и «вероятно» — признак хорошего уровня!", 21.5)
c.expl("по прогнозу según el pronóstico; вероятно probablemente; обещать + infinitivo — para expresar incertidumbre.")
c.ex("B2", "Completar", "По", "по прогнозу = según el pronóstico",
     "___ прогнозу, завтра будет снег.", instr="Completar", size=20.5, gap=10)
c.ex("B2", "Completar", "обещают", "обещать → обещают",
     "Синоптики ___ снег в среду. (обещать)", instr="Completar", size=20.5, gap=10)
c.ex("B2", "Opción múltiple", "B", "вероятно = probablemente, casi seguro",
     "«Вероятно» значит... A. точно да · B. скорее да, чем нет · C. точно нет", size=20.5, gap=10)
c.ex("B2", "Completar", "расходятся", "прогнозы расходятся = las previsiones no coinciden",
     "Если два прогноза разные, прогнозы ___.", instr="Completar", size=20.5, gap=10)
c.end_report()

# ---- col 3: error clinic + word + letters ----
bx = COLX[3]
errs = [
    ("«Поздравляю с День отца!»", "→ После «с» нужен творительный падеж: «с Днём отца!»", "Instrumental tras «с»: с Днём отца."),
    ("«Мы едем к бабушка»", "→ После «к» — дательный падеж: «Мы едем к бабушке».", "Dativo tras «к»: к бабушке."),
    ("«У «Зенита» 24 очков»", "→ После 2, 3, 4 — «очка» (24 очка), после 5 — «очков» (25 очков).", "Con 2, 3, 4 → очка; con 5 o más → очков."),
    ("«Конкурс с первый октябрь»", "→ «С» (начало) требует родительного падежа: «с первого октября».", "Genitivo tras «с»: с первого октября."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ОШИБКИ　Clínica de errores", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "«единоличный лидер» — команда, которая одна стоит на первом месте: у неё больше очков, чем у всех других. Сейчас единоличный лидер — «Динамо»."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("единоличный лидер = el único líder: más puntos que nadie.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "СЛОВО　La palabra", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "единоличный лидер = el único líder: más puntos que nadie.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "«Здравствуйте! Я учу русский язык в Пекине. У нас снег бывает редко, а я очень жду первый снег — как москвичи!» — Ли (пример от редакции)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Ejemplo ficticio de la redacción. VOL.2: ¡cartas reales y los mejores textos!", "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "ПИСЬМА ЧИТАТЕЛЕЙ", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Ejemplo ficticio de la redacción. VOL.2: ¡cartas reales y los mejores textos!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- phrases of the week (verbatim from this issue) ----
fy = 1712
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "ФРАЗЫ НЕДЕЛИ　Frases de la semana (literalmente, de los textos de este número)", 27, "sans", True, OLIVE)
quotes = [
    ("«Первый снег может выпасть уже на этой неделе»", "La primera nevada puede caer ya esta semana.", "Страница 1"),
    ("«Прогнозы расходятся: один синоптик обещает снег в среду, а другой — мокрый снег в конце октября»", "Las previsiones difieren: uno promete nieve el miércoles y otro, aguanieve a finales de octubre.", "Страница 2"),
    ("«Когда на улице плюс пять — семь градусов, пора менять резину»", "Cuando fuera hace entre cinco y siete grados, es hora de cambiar los neumáticos.", "Страница 2"),
    ("«Друзья мои, прекрасен наш союз!»", "Del «19 de octubre» de Pushkin: «¡Amigos míos, hermosa es nuestra unión!»", "Страница 3"),
    ("«В четверг в кино выходят сразу четыре сказки»", "El jueves se estrenan de golpe cuatro cuentos en el cine.", "Страница 3"),
    ("«Динамо — единоличный лидер: у него 25 очков»", "El Dinamo, líder en solitario: 25 puntos.", "Страница 4"),
    ("«В субботу, 31 октября, Москва празднует Хэллоуин»", "El sábado 31 de octubre, Moscú celebra Halloween.", "Страница 5"),
    ("«Каникулы получаются длинными: двенадцать дней подряд»", "Las vacaciones salen largas: doce días seguidos.", "Страница 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "СЛЕДУЮЩАЯ НЕДЕЛЯ　La próxima semana (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Кто победил в дерби ЦСКА — «Спартак»? И выпал ли первый снег? В среду, 28 октября, — День бабушек и дедушек, а в субботу — Хэллоуин. И главное: начинаются каникулы! Плюс ваши письма и лучшие сочинения со страницы 8. До понедельника!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-yazyk.svg")
print("P7 saved, exercises so far:", len(REG))
