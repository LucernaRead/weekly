# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ru-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · ПЕРВАЯ ПОЛОСА (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1 · ПЕРВЫЙ ВЫПУСК", 23, "sans", True, OLIVE)
p.text(975, 92, "КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · OGNI SETTIMANA · IL RUSSO CHE LEGGE LA RUSSIA", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "НЕДЕЛЯ С 19 ПО 25 ОКТЯБРЯ 2026 ГОДА", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SETTIMANALE RUSSO · VOL.1 · ПЕРВЫЙ СНЕГ · КАНИКУЛЫ · ДЕРБИ", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "TESTI IN RUSSO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI", 20, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "ПЕРВЫЙ СНЕГ — УЖЕ НА ЭТОЙ НЕДЕЛЕ!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Синоптики ждут первые снежинки в Москве 21–23 октября. Но прогнозы расходятся.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "LA PRIMA NEVE — QUESTA SETTIMANA", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "Le previsioni non coincidono · vedi pagina 2", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "ГЛАВНАЯ ТЕМА · Il tema principale", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Первый снег — уже на этой неделе!", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "А в субботу начинаются каникулы — целых 12 дней отдыха", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "От редакции Lucerna · Уровень чтения: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Первый снег может выпасть уже на этой неделе. Синоптики ждут первые снежинки в среду, в четверг или в пятницу — с 21 по 23 октября. На улице будет около нуля градусов.", size=24)
f.para("Правда, прогнозы расходятся. Один синоптик говорит: снег будет в среду. Другой говорит: снега надо ждать в конце октября. Кто прав? Мы узнаем очень скоро — читайте 2-ю страницу.", size=24)
f.para("А у школьников — последняя учебная неделя. В пятницу, 23 октября, — последний учебный день, а в субботу начинаются осенние каникулы. Каникулы длинные: двенадцать дней, с 24 октября по 4 ноября.", size=24)
f.para("В четверг в кино выходят четыре новые сказки — об этом на 3-й странице. А в воскресенье — главное футбольное дерби страны: ЦСКА играет со «Спартаком». Начало в 16:00 по московскому времени.", size=24)
f.para("Это первый номер Lucerna по-русски. Каждую неделю мы пишем о настоящей России — просто и честно. Приятного чтения!", size=24)
f.expl("Nota — синоптики i meteorologi · снежинки i fiocchi di neve · расходятся non coincidono (le previsioni).")
f.box("НЕДЕЛЯ В ЦИФРАХ · In cifre", [
    ("12 — дней осенних каникул: с 24 октября по 4 ноября", "serif", False, INK, 20, 1.35),
    ("4 — новые сказки в кино в четверг, 22 октября (quattro fiabe nuove al cinema da giovedì)", "serif", False, INK, 20, 1.35),
    ("8 — матчей в 12-м туре чемпионата России по футболу (12ª giornata del campionato russo di calcio)", "serif", False, INK, 20, 1.35),
    ("215 — лет назад, 19 октября 1811 года, открылся Царскосельский лицей", "serif", False, INK, 20, 1.35),
])
f.head("СЕЙЧАС ВЫ · Ora tocca a te", 25)
f.ex("A2", "Completare", "снег", "первый снег = la prima neve",
     "Первый ___ может выпасть уже на этой неделе.", size=19.5, gap=6)
f.ex("A2", "Completare", "23", "Previsioni: dal 21 al 23",
     "Синоптики ждут снег с 21 по ___ октября.", size=19.5, gap=6)
f.ex("A2", "Completare", "учебный", "последний учебный день = l'ultimo giorno di scuola",
     "В пятницу — последний ___ день.", size=19.5, gap=6)
f.ex("A2", "Completare", "двенадцать", "12 giorni = двенадцать дней",
     "Каникулы длятся ___ дней подряд.", size=19.5, gap=6)
f.ex("A2", "Completare", "«Спартаком»", "Il derby: ЦСКА — «Спартак»; со + strumentale",
     "В воскресенье ЦСКА играет со ___.", size=19.5, gap=6)
f.ex("B1", "Completare", "выходят", "выходить → выходят (presente, 3ª persona plurale)",
     "В четверг в кино ___ (выходить) четыре сказки.", size=19.5, gap=6)
f.end_report()

# ---- media heat box (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "О ЧЁМ ПИШУТ", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "СМИ · Sui media", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Главные темы недели в российских СМИ", 19, "sans", False, GREY)
topics = [
    "Первый снег в Москве: когда он выпадет?",
    "Осенние каникулы: целых 12 дней отдыха",
    "Дерби ЦСКА — «Спартак» в воскресенье",
    "Четыре сказки в кино с четверга",
    "Хэллоуин 31 октября: костюмы и билеты",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 26
p.text(gx + 22, gy + 636, "По российским СМИ, 15–20 октября 2026 г.", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "Dai media russi, 15–20 ottobre 2026", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "В ЭТОМ НОМЕРЕ · Sommario", 24, "sans", True, OLIVE)
som = [
    ("Стр. 2", "Шины, погода, День отца", "A2"),
    ("Стр. 3", "Лицей и сказки в кино", "A2→B1"),
    ("Стр. 4", "Дерби ЦСКА — «Спартак»", "B1"),
    ("Стр. 5", "Хэллоуин и планы", "B1"),
    ("Стр. 6", "12 дней каникул: разбор", "B2"),
    ("Стр. 7", "Фразы недели", "A2→B2"),
    ("Стр. 8", "Тест и все ответы", "все"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

# ---- word of the week (col 3) ----
my = 1636
p.text(gx, my + 24, "СЛОВО НЕДЕЛИ · La parola", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "«похолодает» — станет холодно, температура ниже. Завтра похолодает: будет около нуля.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "похолодает = farà più freddo.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "yuon_winter.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Зима в русском городе. Скоро так будет и в Москве: синоптики ждут первый снег уже 21–23 октября. (Страница 2)",
        "Картина: Константин Юон, «Зима. Ростов» — общественное достояние (Wikimedia Commons)")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-school")
f2.head("ПОСЛЕДНЯЯ УЧЕБНАЯ НЕДЕЛЯ", 25)
f2.para("Понедельник, 19 октября, — первый день последней учебной недели. В пятницу школьники идут в школу в последний раз — а потом отдыхают двенадцать дней.", 22.5)
f2.para("Что делать на каникулах? На 6-й странице — большой разбор и идеи для всей семьи.", 22.5)
f2.end_report()
# col 3 КОРОТКО
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "КОРОТКО · In breve", 24, "sans", True, OLIVE)
brefs = [
    ("СНЕГ", "Первые снежинки — 21–23 октября. Снег выпадет и быстро растает: это ещё не зима."),
    ("КАНИКУЛЫ", "С 24 октября по 4 ноября — 12 дней. 4 ноября — День народного единства."),
    ("ДЕРБИ", "В воскресенье в 16:00 ЦСКА играет со «Спартаком». Подробнее — на 4-й странице."),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "БЛИЦ-ВИКТОРИНА · Quiz lampo", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Leggi la prima pagina e scegli la risposta giusta · Risposte a pagina 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "Scelta multipla", "B", "Previsioni: dal 21 al 23",
      "Первый снег в Москве ждут... A. в ноябре · B. 21–23 октября · C. в декабре", size=21)
qf.ex("A2", "Scelta multipla", "B", "Il 24 ottobre è sabato",
      "Каникулы начинаются... A. в пятницу · B. в субботу · C. в понедельник", size=21)
qf.ex("A2", "Scelta multipla", "C", "Le vacanze durano 12 giorni",
      "Сколько дней длятся каникулы? A. 9 · B. 10 · C. 12", size=21)
qf.ex("A2", "Scelta multipla", "A", "Il derby di domenica: ЦСКА — «Спартак»",
      "Дерби в воскресенье — это матч... A. ЦСКА — «Спартак» · B. «Зенит» — «Динамо» · C. «Ахмат» — «Оренбург»", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-pervaya.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · ЖИЗНЬ (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("ЖИЗНЬ · Vita", "Lucerna", "УРОВЕНЬ A2 · Погода, шины и поздравления · Meteo, gomme e auguri")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Первый снег: что говорят синоптики", 37)
f.byline("От редакции Lucerna · Уровень чтения: A2")
f.para("На этой неделе в Москве похолодает. Днём будет около нуля градусов, а ночью — ещё холоднее. Синоптики говорят: первый снег может быть в среду, 21 октября, в четверг или в пятницу.")
f.para("Прогнозы расходятся: один синоптик обещает снег в среду, а другой — мокрый снег в конце октября. Поэтому не верьте только одному прогнозу: смотрите прогноз каждый день.")
f.para("Настоящего снежного покрова ещё не будет: снег выпадет и быстро растает. Но первый снег — это знак: зима близко. Пора доставать тёплую одежду: шапку, шарф, перчатки и тёплую куртку.")
f.gloss("снежный покров il manto nevoso · растает si scioglierà · доставать tirare fuori (i vestiti invernali).")
f.head("ПОРА МЕНЯТЬ РЕЗИНУ", 25)
f.para("У водителей осенью есть важное дело — поменять резину на зимнюю. Когда на улице плюс пять — семь градусов, пора менять резину. В средней полосе России это время — конец октября и начало ноября.")
f.para("На шиномонтаже сейчас очереди: все водители думают одинаково. Опытные водители не ждут первого снега и меняют резину раньше: летняя резина на снегу — это опасно.")
f.gloss("резину le gomme (da летняя, estive, a зимняя, invernali) · шиномонтаж il gommista · очереди le code.")
f.head("С ДНЁМ ОТЦА!", 25)
f.para("В воскресенье, 18 октября, в России был День отца. Этот праздник отмечают в третье воскресенье октября, и в 2026 году его отмечают уже в шестой раз. В воскресенье страна поздравляла пап: дети дарили открытки и подарки и говорили тёплые слова.")
f.para("Как поздравить папу по-русски? Скажите: «Поздравляю с Днём отца!» И добавьте пожелание: «Желаю здоровья, счастья и хорошего настроения!» Так говорят в России в праздник.")
f.gloss("с Днём отца Buona Festa del Papà! (поздравляю + с + strumentale) · открытки i biglietti di auguri · пожелание un augurio.")
f.end_report()

# col 3: image + facts + а вы (sequential, measured)
ix = COLX[3]
image(p, "snowflake.jpg", ix, 200, CW, 272)
cy3 = caption(p, ix, 472, CW, "Каждая снежинка — особенная. Эту снежинку сфотографировал Уилсон Бентли больше ста лет назад.",
              "Фото: Уилсон Бентли — общественное достояние (Wikimedia Commons)")
facts = ["Первый снег в Москве ждут 21–23 октября, но прогнозы расходятся.",
         "Резину меняют, когда на улице плюс пять — семь градусов.",
         "Каникулы у школьников — с 24 октября по 4 ноября: 12 дней."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ЗНАЕТЕ ЛИ ВЫ?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "А вы? Что вы делаете, когда выпадает первый снег: радуетесь, фотографируете или просто надеваете тёплую куртку? Напишите два предложения по-русски и пришлите в редакцию: лучшие мы напечатаем в VOL.2 (страница 7, «Письма читателей»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("E tu? Cosa fai quando cade la prima neve? Scrivi due frasi in russo e mandale alla redazione.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "А ВЫ? · E tu?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "E tu? Cosa fai quando cade la prima neve? Scrivi due frasi in russo e mandale alla redazione.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- weather words strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "СЛОВА О ПОГОДЕ · Parole del meteo", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Четыре слова о первом снеге · Quattro parole sulla prima neve", 20, "sans", False, GREY, anchor="end")
words = [
    ("похолодает", "станет холодно", "farà più freddo"),
    ("выпадет снег", "снег начнёт падать", "nevicherà"),
    ("мокрый снег", "снег с дождём", "nevischio"),
    ("растает", "снег станет водой", "si scioglierà"),
]
for i, (t, lab, cn) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 234, "Запомните пару: снег выпадает (несов.) — снег выпал (сов.). А завтра снег выпадет и быстро растает.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Esercizi della pagina 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8 · livelli mescolati: cerca per numero di esercizio", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.expl("Leggi i testi di pagina 2 e scegli la risposta corretta.")
e.ex("A2", "Scelta multipla", "B", "Previsioni: dal 21 al 23",
     "Первый снег в Москве ждут... A. в конце октября · B. 21–23 октября · C. в ноябре", size=19, gap=6)
e.ex("A2", "Scelta multipla", "B", "Due previsioni diverse: testo di pagina 2",
     "Почему прогнозы разные? A. Синоптики не работают · B. Один обещает снег в среду, другой — в конце октября · C. Снега не будет", size=19, gap=6)
e.ex("A2", "Scelta multipla", "A", "La prima neve si scioglie presto",
     "Первый снег быстро... A. растает · B. останется на всю зиму · C. будет идти месяц", size=19, gap=6)
e.ex("A2", "Scelta multipla", "B", "Le gomme si cambiano a +5…+7 gradi",
     "Резину меняют, когда на улице... A. ноль градусов · B. плюс пять — семь градусов · C. минус десять градусов", size=19, gap=6)
e.ex("A2", "Scelta multipla", "C", "La Festa del Papà è stata il 18 ottobre",
     "День отца в России был... A. 19 октября · B. 25 октября · C. 18 октября", size=19, gap=6)
e.head("B · СЛОВА О ПОГОДЕ", 25)
e.expl("Completa con le parole del riquadro o con la forma corretta del verbo.")
e.ex("A2", "Completare", "похолодает", "похолодать → похолодает (futuro)",
     "Завтра ___: будет около нуля градусов. (похолодать)", instr="Completa", size=19, gap=6)
e.ex("A2", "Completare", "выпадет", "выпасть → выпадет",
     "Первый снег ___ и быстро растает. (выпасть)", instr="Completa", size=19, gap=6)
e.ex("A2", "Completare", "мокрый", "мокрый снег = nevischio",
     "Снег с дождём — это ___ снег.", instr="Completa", size=19, gap=6)
e.ex("A2", "Completare", "шарф", "шапка e шарф sono vestiti invernali",
     "Надень шапку и ___: на улице холодно!", instr="Completa", size=19, gap=6)
e.ex("B1", "Completare", "очереди", "plurale di очередь: очереди",
     "На шиномонтаже сейчас большие ___.", instr="Completa", size=19, gap=6)
e.head("C · ЧИСЛА И ДАТЫ", 25)
e.expl("Completa con i numeri e le date delle pagine 1 e 2.")
e.ex("A2", "Completare", "24", "Il 24 ottobre è sabato",
     "Каникулы начинаются ___ октября.", instr="Completa", size=19, gap=6)
e.ex("B1", "Completare", "третье", "la terza domenica: третье воскресенье",
     "День отца отмечают в ___ воскресенье октября.", instr="Completa", size=19, gap=6)
e.ex("A2", "Completare", "25", "Il 25 ottobre è domenica",
     "Дерби ЦСКА — «Спартак» будет ___ октября.", instr="Completa", size=19, gap=6)
e.ex("B1", "Completare", "шестой", "sesta volta dal 2021: шестой раз",
     "В 2026 году День отца отмечают уже в ___ раз.", instr="Completa", size=19, gap=6)
e.head("D · ПОЗДРАВЛЕНИЯ", 25)
e.match_set("A2", "Abbinamento",
            ["С Днём отца!", "С днём рождения!", "С Новым годом!", "Желаю здоровья!"],
            ["это пожелание: мы желаем человеку быть здоровым",
             "так поздравляют папу в третье воскресенье октября",
             "так поздравляют первого января",
             "так поздравляют в день, когда человек родился"],
            ["b", "d", "c", "a"],
            ["auguri per la Festa del Papà b", "auguri di compleanno d", "auguri di Capodanno c", "augurio di salute a"],
            instr="Abbina")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-zhizn.svg")
print("P2 saved, exercises so far:", len(REG))
