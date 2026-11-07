# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ru-en-proof/freeze-baseline/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · КУЛЬТУРА (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("КУЛЬТУРА · Culture", "Lucerna", "УРОВЕНЬ A2 → B1 · День народного единства и среда в городе · Unity Day and Wednesday in town")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("4 ноября: один день праздника", 37)
f.byline("От редакции Lucerna · Уровень чтения: A2 → B1")
f.para("В среду, 4 ноября, в России — выходной. Праздник называется День народного единства. Праздник появился в 2005 году и напоминает о событиях 1612 года, но сегодня это прежде всего обычный выходной посреди недели.")
f.para("Как отмечают этот день? В среду города устраивают ярмарки и концерты. Люди гуляют с семьёй, покупают еду и подарки на ярмарке и слушают музыку.")
f.para("Для школьников среда — последний день каникул: в четверг уже снова в школу. Поэтому среда — день семьи: утром можно выспаться, днём пойти на ярмарку, а вечером вернуться домой.")
f.para("А ещё среда — хороший день для короткой поездки: уехать утром и вернуться вечером. Один день — и уже маленькое путешествие!")
f.gloss("напоминает о recalls · прежде всего above all · ярмарке a fair.")
f.head("СРЕДА В ГОРОДЕ", 25)
f.para("Что можно делать в среду? Пойти на ярмарку: там продают еду, тёплые вещи и подарки. Пойти на концерт: музыка звучит на площадях и в парках. Или просто погулять: ноябрьский город красив, когда светит солнце.")
f.para("Не забудьте тёплую одежду: в ноябре уже холодно. Шапка, шарф и тёплая куртка — лучшие друзья ноября.")
f.gloss("площадях squares · погулять to go for a walk · светит солнце the sun is shining.")
f.end_report()

ix = COLX[3]
facts = ["4 ноября — День народного единства, выходной.",
         "Праздник появился в 2005 году.",
         "Среда — последний день школьных каникул.",
         "В четверг, 5 ноября, — снова в школу."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ГЛАВНОЕ — КОРОТКО", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ideas = ["Утром — выспаться: никуда не спешить.",
         "Днём — ярмарка или концерт в городе.",
         "Вечером — домой, к семье: среда короткая."]
sy3b = sy3 + sh + 24
shb = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in ideas) + 32
p.rect(ix, sy3b, CW, shb, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = sy3b + 16
p.text(ix + 22, yy3 + 26, "КАК ПРОВЕСТИ СРЕДУ", 24, "sans", True, OLIVE)
yy3 += 52
for t in ideas:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 ends", sy3b + shb)

ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Page 3 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels mixed — find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.bridge("Read the page 3 articles and choose the right answer.")
e.ex("A2", "multiple choice", "B", "4 November is Unity Day",
     "День народного единства — это... A. 2 ноября · B. 4 ноября · C. 5 ноября", size=20, gap=8)
e.ex("A2", "multiple choice", "A", "The holiday began in 2005",
     "Праздник появился в... A. 2005 году · B. 1612 году · C. 2026 году", size=20, gap=8)
e.ex("A2", "multiple choice", "B", "On Wednesday towns hold fairs and concerts",
     "В среду города устраивают... A. дерби · B. ярмарки и концерты · C. распродажу", size=20, gap=8)
e.ex("A2", "multiple choice", "C", "Back to school on Thursday",
     "Школьники идут в школу... A. в среду · B. в пятницу · C. в четверг", size=20, gap=8)
e.ex("B1", "multiple choice", "A", "Because Wednesday is the last holiday day",
     "Почему среда — день семьи? A. Это последний день каникул · B. Это выходной в субботу · C. Это первый день каникул", size=20, gap=8)
e.head("B · ГЛАГОЛЫ И ФОРМЫ", 25)
e.bridge("Fill in the right verb form or the right case.")
e.ex("B1", "fill-in", "устраивают", "устраивать → устраивают",
     "Города ___ ярмарки и концерты. (устраивать)", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "гуляют", "гулять → гуляют",
     "Люди ___ с семьёй. (гулять)", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "вернуться", "вернуться = to return",
     "Вечером можно ___ домой. (вернуться)", instr="Fill in", size=20, gap=8)
e.ex("A2", "fill-in", "выспаться", "выспаться = to sleep in",
     "Утром можно ___. (выспаться)", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "ноября", "4 + genitive: ноября",
     "В среду, 4 ___ , — выходной. (ноябрь)", instr="Fill in", size=20, gap=8)
e.head("C · ПРАЗДНИК", 25)
e.match_set("B1", "matching",
            ["ярмарка", "концерт", "выходной", "путешествие"],
            ["день, когда не работают",
             "место, где продают еду и подарки",
             "поездка в другой город",
             "музыка на площади или в парке"],
            ["b", "d", "a", "c"],
            ["Fair b", "Concert d", "Day off a", "Trip c"],
            instr="Match the pairs")
e.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.bridge("Build correct sentences from the words.")
e.ex("A2", "sentence building", "Города устраивают ярмарки и концерты.", "Subject + verb + object",
     "города / устраивают / ярмарки и концерты → ___", instr="sentence building", size=20, gap=8)
e.ex("A2", "sentence building", "Люди гуляют с семьёй.", "Subject + verb + adverbial",
     "люди / гуляют / с семьёй → ___", instr="sentence building", size=20, gap=8)
e.ex("B1", "sentence building", "В четверг школьники идут в школу.", "Time first, verb second",
     "в четверг / школьники / идут в школу → ___", instr="sentence building", size=20, gap=8)
e.ex("B1", "sentence building", "Утром можно выспаться.", "можно + infinitive",
     "утром / можно / выспаться → ___", instr="sentence building", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-kultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · СПОРТ (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("СПОРТ · Sport", "Lucerna", "УРОВЕНЬ B1 · 14-й тур: последний перед паузой · Round 14: the last before the break")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1100, tag="P4-main")
f.title("14-й тур: последний перед паузой", 37)
f.byline("От спортивной редакции Lucerna · Уровень чтения: B1")
f.para("В понедельник, 2 ноября, закрывается 13-й тур: «Крылья Советов» играют с «Зенитом» в 18:00. А уже в пятницу начинается 14-й тур чемпионата России.")
f.para("В пятницу «Локомотив» играет с «Рубином». Главный матч тура — в субботу, 7 ноября: «Краснодар» играет с ЦСКА в 19:30 на «Ozon Арене».")
f.para("В воскресенье, 8 ноября, — три матча: «Спартак» играет с «Акроном» в 16:15, «Зенит» — с «Ростовом», а «Крылья Советов» — с «Оренбургом».")
f.para("После этого тура — пауза: следующий, 15-й тур, будет только 20 ноября. Поэтому 14-й тур — последний шанс увидеть футбол до долгого перерыва.")
f.para("А в прошлом туре ЦСКА победил «Спартак» в дерби 2:0 — об этом мы написали на 2-й странице.")
f.gloss("закрывается ends (a round) · перерыва the break · шанс a chance.")
f.end_report()

bx = COLX[3]
image(p, "football1912.jpg", bx, 200, CW, 250)
cy4 = caption(p, bx, 450, CW, "Сборная России по футболу на Олимпиаде 1912 года. Футболу в России — больше ста лет.",
              "Фото: автор неизвестен, 1912 — общественное достояние (Wikimedia Commons)")
tour = ["14-й тур: 6–8 ноября.",
        "Главный матч: «Краснодар» — ЦСКА, суббота, 19:30.",
        "15-й тур — только 20 ноября: потом пауза."]
sy4 = cy4 + 22
sh4 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in tour) + 32
p.rect(bx, sy4, CW, sh4, fill=BOX, stroke=LINE, sw=1.4)
yy4 = sy4 + 16
p.text(bx + 22, yy4 + 26, "ТУР В ЦИФРАХ", 24, "sans", True, OLIVE)
yy4 += 52
for t in tour:
    yy4 = p.para(bx + 22, yy4 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P4 col3 ends", sy4 + sh4)

ty = 1160
p.text(MX, ty, "14-Й ТУР: КАЛЕНДАРЬ · Fixtures: round 14", 26, "sans", True, OLIVE)
rows = [
    ("Пт 6.11.", "—", "«Локомотив» — «Рубин» — первый матч тура"),
    ("Сб 7.11.", "19:30", "«Краснодар» — ЦСКА — главный матч (Ozon Арена)"),
    ("Вс 8.11.", "16:15", "«Спартак» — «Акрон»"),
    ("Вс 8.11.", "—", "«Зенит» — «Ростов»"),
    ("Вс 8.11.", "—", "«Крылья Советов» — «Оренбург»"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Внимание: время московское. После тура — пауза до 20 ноября."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Page 4 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels mixed — find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.bridge("Read the page 4 article and choose the right answer.")
e.ex("B1", "multiple choice", "B", "Round 14 starts on Friday",
     "14-й тур начинается... A. в понедельник · B. в пятницу · C. в воскресенье", size=20, gap=8)
e.ex("B1", "multiple choice", "B", "Top match Saturday 19:30",
     "Матч «Краснодар» — ЦСКА будет... A. в пятницу · B. в субботу в 19:30 · C. в воскресенье", size=20, gap=8)
e.ex("B1", "multiple choice", "C", "Spartak vs Akron Sunday 16:15",
     "«Спартак» играет с «Акроном»... A. в субботу · B. в пятницу · C. в воскресенье в 16:15", size=20, gap=8)
e.ex("B1", "multiple choice", "A", "Round 15 on 20 November",
     "15-й тур будет... A. 20 ноября · B. 8 ноября · C. 6 ноября", size=20, gap=8)
e.ex("B1", "multiple choice", "B", "Round 13 ends on Monday",
     "13-й тур закрывается... A. в воскресенье · B. в понедельник · C. в субботу", size=20, gap=8)
e.head("B · КАЛЕНДАРЬ И ДАТЫ", 25)
e.bridge("Fill in the numbers and words from page 4.")
e.ex("A2", "fill-in", "2", "Monday, 2 November",
     "13-й тур закрывается ___ ноября.", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "7", "Saturday, 7 November",
     "Матч «Краснодар» — ЦСКА будет ___ ноября.", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "19:30", "Starts 19:30",
     "Матч начинается в ___ (время).", instr="Fill in", size=20, gap=8)
e.ex("A2", "fill-in", "16:15", "Starts 16:15",
     "«Спартак» — «Акрон» начинается в ___ (время).", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "20", "20 November",
     "15-й тур будет ___ ноября.", instr="Fill in", size=20, gap=8)
e.head("C · КОМАНДЫ И МАТЧИ", 25)
e.match_set("B1", "matching",
            ["«Локомотив»", "«Краснодар»", "«Спартак»", "«Зенит»"],
            ["играет с ЦСКА в субботу в 19:30",
             "играет с «Рубином» в пятницу",
             "играет с «Акроном» в воскресенье в 16:15",
             "играет с «Ростовом»"],
            ["b", "a", "c", "d"],
            ["Lokomotiv b", "Krasnodar a", "Spartak c", "Zenit d"],
            instr="Match the pairs")
e.head("D · ВРЕМЯ ГЛАГОЛА", 25)
e.bridge("Put the bracketed verbs in the right tense.")
e.ex("B1", "fill-in", "играет", "играть → играет",
     "В субботу «Краснодар» ___ с ЦСКА. (играть)", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "будет", "будет = will be",
     "15-й тур ___ только 20 ноября. (быть)", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "закрывается", "закрываться → закрывается",
     "13-й тур ___ в понедельник. (закрываться)", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "победил", "победить → победил",
     "В прошлом туре ЦСКА ___ «Спартак» 2:0. (победить)", instr="Fill in", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
