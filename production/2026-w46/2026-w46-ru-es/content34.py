# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ru-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · КУЛЬТУРА (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("КУЛЬТУРА · CULTURA", "Lucerna", "УРОВЕНЬ A2 → B1 · Кино в середине ноября · El cine a mediados de noviembre")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Кино в середине ноября", 37)
f.byline("От редакции Lucerna · Уровень чтения: A2 → B1")
f.para("В ноябре вечера тёмные и долгие: в Москве солнце садится около половины пятого. Самое время пойти в кино или посмотреть фильм дома. В середине ноября в прокат выходят сразу несколько интересных фильмов.")
f.para("12 ноября в прокат выходит фильм «Лиля» — история жизни Лили Брик, музы поэта Владимира Маяковского. Это биография: фильм рассказывает о любви, поэзии и Москве начала прошлого века.")
f.para("А ещё в середине ноября — фильм «Эбенезер»: новое прочтение «Рождественской песни» Чарльза Диккенса. Джонни Депп играет молодого Эбенезера Скруджа — ещё до того, как он стал скупым и одиноким.")
f.para("А дома, на стриминге, 13 ноября выходит фильм «В сердце Нэшвилла» с Джессикой Честейн: бывшая звезда кантри расследует исчезновение племянницы. Кино — хороший план на тёмный ноябрьский вечер!")
f.gloss("садится se pone (el sol) · музы las musas · скупым tacaño.")
f.head("КИНО ДОМА И В КИНОТЕАТРЕ", 25)
f.para("Что выбрать: кинотеатр или дом? В кинотеатре — большой экран и звук. Дома — плед, чай и пауза, когда захочется. Главное — хороший фильм и хорошая компания.")
f.para("Не забудьте: ноябрьские вечера холодные. Тёплая одежда — лучший друг кинозрителя, как и зонт по дороге в кино.")
f.gloss("плед una manta · кинозрителя un espectador de cine.")
f.end_report()

ix = COLX[3]
facts = ["«Лиля» — с 12 ноября: история Лили Брик.",
         "«Эбенезер» — в середине ноября: Диккенс по-новому.",
         "«В сердце Нэшвилла» — 13 ноября, стриминг.",
         "В Москве темнеет около половины пятого."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ГЛАВНОЕ — КОРОТКО", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ideas = ["Вечером — в кино: «Лиля» или «Эбенезер».",
         "Дома — стриминг: «В сердце Нэшвилла».",
         "С друзьями: обсудить фильм после сеанса."]
sy3b = sy3 + sh + 24
shb = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in ideas) + 32
p.rect(ix, sy3b, CW, shb, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = sy3b + 16
p.text(ix + 22, yy3 + 26, "КАК ПРОВЕСТИ ВЕЧЕР", 24, "sans", True, OLIVE)
yy3 += 52
for t in ideas:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 ends", sy3b + shb)

ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · EJERCICIOS DE LA PÁGINA 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8 · Los niveles pueden mezclarse; busca por número de ejercicio", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.bridge("Lee el artículo de la página 3 y elige las respuestas correctas.")
e.ex("A2", "Opción múltiple", "B", "Lilia se estrena el 12 de noviembre",
     "Фильм «Лиля» выходит... A. 13 ноября · B. 12 ноября · C. 19 ноября", size=20, gap=8)
e.ex("A2", "Opción múltiple", "A", "Lilia Brik fue la musa de Mayakovski",
     "Лиля Брик — это... A. муза Маяковского · B. певица кантри · C. актриса из Нэшвилла", size=20, gap=8)
e.ex("A2", "Opción múltiple", "B", "Johnny Depp interpreta al joven Scrooge",
     "Джонни Депп играет... A. Маяковского · B. молодого Скруджа · C. детектива", size=20, gap=8)
e.ex("A2", "Opción múltiple", "C", "En el corazón de Nashville en streaming el 13 de noviembre",
     "«В сердце Нэшвилла» выходит... A. в кинотеатре · B. 12 ноября · C. 13 ноября на стриминге", size=20, gap=8)
e.ex("B1", "Opción múltiple", "A", "En Moscú oscurece hacia las 16:30",
     "В Москве в ноябре темнеет... A. около половины пятого · B. в восемь вечера · C. в полночь", size=20, gap=8)
e.head("B · ГЛАГОЛЫ И ФОРМЫ", 25)
e.bridge("Completa la forma verbal o el caso correcto.")
e.ex("B1", "Completar", "выходит", "выходить → выходит",
     "Фильм «Лиля» ___ 12 ноября. (выходить)", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "рассказывает", "рассказывать → рассказывает",
     "Фильм ___ о любви и поэзии. (рассказывать)", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "играет", "играть → играет",
     "Джонни Депп ___ Скруджа. (играть)", instr="Completar", size=20, gap=8)
e.ex("A2", "Completar", "посмотреть", "посмотреть = ver",
     "Вечером можно ___ фильм дома. (посмотреть)", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "ноября", "12 + genitivo: ноября",
     "Фильм выходит 12 ___. (ноябрь)", instr="Completar", size=20, gap=8)
e.head("C · КИНО", 25)
e.match_set("B1", "Emparejamiento",
            ["биография", "стриминг", "сеанс", "зритель"],
            ["человек, который смотрит фильм",
             "фильм о жизни реального человека",
             "показ фильма в кинотеатре",
             "фильмы смотрят дома через интернет"],
            ["b", "d", "c", "a"],
            ["biopic b", "streaming d", "sesión c", "espectador a"],
            instr="Empareja")
e.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.bridge("Forma frases correctas con las palabras.")
e.ex("A2", "Frases", "Фильм «Лиля» выходит 12 ноября.", "Sujeto + verbo + tiempo",
     "фильм «Лиля» / выходит / 12 ноября → ___", instr="Frases", size=20, gap=8)
e.ex("A2", "Frases", "Джонни Депп играет Скруджа.", "Sujeto + verbo + objeto",
     "Джонни Депп / играет / Скруджа → ___", instr="Frases", size=20, gap=8)
e.ex("B1", "Frases", "В ноябре вечера тёмные и долгие.", "El tiempo primero, el predicado después",
     "в ноябре / вечера / тёмные и долгие → ___", instr="Frases", size=20, gap=8)
e.ex("B1", "Frases", "Вечером можно посмотреть фильм дома.", "poder + infinitivo",
     "вечером / можно / посмотреть фильм дома → ___", instr="Frases", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-kultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · СПОРТ (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("СПОРТ · DEPORTE", "Lucerna", "УРОВЕНЬ B1 · 14-й тур: итоги неизвестны + сборная · Jornada 14: resultados desconocidos + la selección")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1100, tag="P4-main")
f.title("14-й тур: итоги неизвестны", 37)
f.byline("От спортивной редакции Lucerna · Уровень чтения: B1")
f.para("14-й тур чемпионата России сыграли 6–8 ноября. Но честно: на момент сдачи нашего номера, 2 ноября, результаты тура ещё не были известны. Поэтому в этом номере — расписание тура, а полные итоги мы напечатаем в VOL.4.")
f.para("Главный матч тура — в субботу, 7 ноября: «Краснодар» играет с ЦСКА в 19:30 на «Ozon Арене». В пятницу, 6 ноября, «Локомотив» играет с «Рубином» в 19:30.")
f.para("В субботу играют ещё «Факел» с «Динамо» в 14:00 и «Ахмат» с «Родиной» в 16:30. А в воскресенье, 8 ноября, — «Спартак» с «Акроном» в 16:15, «Зенит» с «Ростовом» и «Крылья Советов» с «Оренбургом».")
f.para("После этого тура — пауза: следующий, 15-й тур, будет только 20 ноября. А сборная России 12 ноября играет товарищеский матч с Узбекистаном в Ташкенте.")
f.para("В прошлом, 13-м туре «Спартак» победил «Локомотив» 4:0, а ЦСКА сыграл вничью с «Оренбургом» 0:0 — об этом в таблице справа.")
f.gloss("на момент сдачи al cierre de la edición · вничью empate · товарищеский amistoso.")
f.end_report()

bx = COLX[3]
image(p, "football1912.jpg", bx, 200, CW, 250)
cy4 = caption(p, bx, 450, CW, "Сборная России по футболу на Олимпиаде 1912 года. Футболу в России — больше ста лет.",
              "Фото: автор неизвестен, 1912 — общественное достояние (Wikimedia Commons)")
tour = ["13-й тур: «Спартак» — «Локомотив» 4:0.",
        "ЦСКА — «Оренбург» 0:0.",
        "«Рубин» — «Факел» 1:0, «Балтика» — «Акрон» 2:1.",
        "«Динамо» Махачкала — «Ростов» 0:3.",
        "«Краснодар» — «Родина» 1:2."]
sy4 = cy4 + 22
sh4 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in tour) + 32
p.rect(bx, sy4, CW, sh4, fill=BOX, stroke=LINE, sw=1.4)
yy4 = sy4 + 16
p.text(bx + 22, yy4 + 26, "13-Й ТУР: РЕЗУЛЬТАТЫ", 24, "sans", True, OLIVE)
yy4 += 52
for t in tour:
    yy4 = p.para(bx + 22, yy4 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P4 col3 ends", sy4 + sh4)

ty = 1160
p.text(MX, ty, "14-Й ТУР: КАЛЕНДАРЬ · CALENDARIO DE LA JORNADA 14 (RESULTADOS DESCONOCIDOS)", 26, "sans", True, OLIVE)
rows = [
    ("Пт 6.11.", "19:30", "«Локомотив» — «Рубин» — первый матч тура"),
    ("Сб 7.11.", "14:00", "«Факел» — «Динамо»"),
    ("Сб 7.11.", "16:30", "«Ахмат» — «Родина»"),
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
tnote = "Внимание: время московское. Результаты тура на момент сдачи номера неизвестны — полные итоги в VOL.4. Матч «Крылья Советов» — «Зенит» (2 ноября) тоже сыгран после сдачи номера."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · EJERCICIOS DE LA PÁGINA 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8 · Los niveles pueden mezclarse; busca por número de ejercicio", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.bridge("Lee el artículo de la página 4 y elige las respuestas correctas.")
e.ex("B1", "Opción múltiple", "B", "Resultados de la jornada 14 desconocidos al cierre",
     "Почему в номере нет итогов 14-го тура? A. Тур не сыграли · B. Номер сдан 2 ноября · C. Тур отменили", size=20, gap=8)
e.ex("B1", "Opción múltiple", "B", "El gran partido: sábado 19:30",
     "Матч «Краснодар» — ЦСКА будет... A. в пятницу · B. в субботу в 19:30 · C. в воскресенье", size=20, gap=8)
e.ex("B1", "Opción múltiple", "C", "Spartak contra Akron, domingo 16:15",
     "«Спартак» играет с «Акроном»... A. в субботу · B. в пятницу · C. в воскресенье в 16:15", size=20, gap=8)
e.ex("B1", "Opción múltiple", "A", "Jornada 15 el 20 de noviembre",
     "15-й тур будет... A. 20 ноября · B. 8 ноября · C. 6 ноября", size=20, gap=8)
e.ex("B1", "Opción múltiple", "B", "La selección juega el jueves en Taskent",
     "Сборная России играет 12 ноября с... A. Венесуэлой · B. Узбекистаном в Ташкенте · C. «Ростовом»", size=20, gap=8)
e.head("B · КАЛЕНДАРЬ И ДАТЫ", 25)
e.bridge("Completa: números y palabras (página 4).")
e.ex("A2", "Completar", "6", "Viernes 6 de noviembre",
     "14-й тур начинается ___ ноября.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "7", "Sábado 7 de noviembre",
     "Матч «Краснодар» — ЦСКА будет ___ ноября.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "19:30", "Empieza a las 19:30",
     "Матч начинается в ___ (время).", instr="Completar", size=20, gap=8)
e.ex("A2", "Completar", "16:15", "Empieza a las 16:15",
     "«Спартак» — «Акрон» начинается в ___ (время).", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "20", "20 de noviembre",
     "15-й тур будет ___ ноября.", instr="Completar", size=20, gap=8)
e.head("C · КОМАНДЫ И МАТЧИ", 25)
e.match_set("B1", "Emparejamiento",
            ["«Локомотив»", "«Краснодар»", "«Спартак»", "«Зенит»"],
            ["играет с ЦСКА в субботу в 19:30",
             "играет с «Рубином» в пятницу",
             "играет с «Акроном» в воскресенье в 16:15",
             "играет с «Ростовом»"],
            ["b", "a", "c", "d"],
            ["Lokomotiv b", "Krasnodar a", "Spartak c", "Zenit d"],
            instr="Empareja")
e.head("D · ВРЕМЯ ГЛАГОЛА", 25)
e.bridge("Completa con el tiempo correcto del verbo entre paréntesis.")
e.ex("B1", "Completar", "играет", "играть → играет",
     "В субботу «Краснодар» ___ с ЦСКА. (играть)", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "будет", "будет = será",
     "15-й тур ___ только 20 ноября. (быть)", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "сыграли", "сыграть → сыграли",
     "14-й тур ___ 6–8 ноября. (сыграть)", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "победил", "победить → победил",
     "В 13-м туре «Спартак» ___ «Локомотив» 4:0. (победить)", instr="Completar", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
