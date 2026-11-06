# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · МОЛОДЁЖЬ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("МОЛОДЁЖЬ · Jongeren", "Lucerna", "УРОВЕНЬ B1 · Распродажа 11.11: как покупать умно · 11.11-sale: slim winkelen")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P5-feature")
f.title("11.11: как покупать умно", 37)
f.byline("От редакции Lucerna · Уровень чтения: B1")
f.para("Всю неделю идёт распродажа 11.11: она началась 22 октября и закончится 12 ноября. Скидки везде: в приложениях, на сайтах и в магазинах. Но большая скидка — ещё не хорошая покупка.")
f.para("Промокод — это код со скидкой. Его вводят при покупке — и цена становится ниже. Промокоды ищут в приложениях, в письмах магазинов и у блогеров.")
f.para("Как проверить цену? Сравните цену в разных магазинах. Посмотрите историю цены: если товар подорожал вчера, а сегодня «со скидкой» стоит столько же — это не скидка. И не спешите: положите товар в список и подумайте один день.")
f.para("Торговая пресса пишет: в ноябре скидок может быть меньше, а выбор — уже. Продавцы публично спорят о новых правилах распродажи. Поэтому умный покупатель сравнивает, а не хватает первое попавшееся.")
f.gloss("приложения apps · вводят invoeren · хватает grijpen.")
f.head("СПИСОК ПОКУПОК", 25)
f.para("Сначала — список: что вам правда нужно? Потом — цены: сколько стоит товар в трёх магазинах? Потом — промокод: есть ли код со скидкой? И только потом — покупка.")
f.para("Студенты так и делают: список, цены, промокод — и никаких лишних покупок. А вы уже составили свой список к 11.11?")
f.gloss("лишних overbodig · составили opgesteld.")
f.end_report()

ix = COLX[3]
image(p, "market.jpg", ix, 200, CW, 280)
cy5 = caption(p, ix, 480, CW, "На рынке: свежие овощи и фрукты. Покупки — тоже выбор: сравнить цены и не спешить.",
              "Фото: Престон Керес (USDA) — общественное достояние (Wikimedia Commons)")
facts = ["Распродажа 11.11: 22 октября – 12 ноября.",
         "Промокод — код со скидкой.",
         "Торговая пресса: скидок может быть меньше.",
         "Правило: список, цены, промокод — потом покупка."]
sy5 = cy5 + 24
sh5 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy5, CW, sh5, fill=BOX, stroke=LINE, sw=1.4)
yy5 = sy5 + 16
p.text(ix + 22, yy5 + 26, "11.11 В ЦИФРАХ", 24, "sans", True, OLIVE)
yy5 += 52
for t in facts:
    yy5 = p.para(ix + 22, yy5 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 ends", sy5 + sh5)

ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Oefeningen pagina 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · Niveaus door elkaar — zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.bridge("Lees de artikelen op pagina 5 en kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "Sale begonnen op 22 oktober",
     "Распродажа 11.11 началась... A. 12 ноября · B. 22 октября · C. 4 ноября", size=20, gap=8)
e.ex("A2", "Meerkeuze", "C", "Sale tot 12 november",
     "Распродажа закончится... A. 8 ноября · B. 4 ноября · C. 12 ноября", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "Een promocode is een kortingscode",
     "Промокод — это... A. код со скидкой · B. название магазина · C. список покупок", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Prijzen in verschillende winkels vergelijken",
     "Как проверить цену? A. Купить сразу · B. Сравнить цены в магазинах · C. Спросить у друзей", size=20, gap=8)
e.ex("A2", "Meerkeuze", "A", "Maak eerst een lijst",
     "Сначала нужно составить... A. список покупок · B. промокод · C. приложение", size=20, gap=8)
e.head("B · СЛОВА ПОКУПОК", 25)
e.bridge("Vul de woorden van pagina 5 in.")
e.ex("A2", "Voltooi de zin", "скидки", "скидки = kortingen",
     "На распродаже везде ___.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "промокод", "промокод = promocode",
     "Введите ___ при покупке — цена станет ниже.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "список", "список покупок = boodschappenlijst",
     "Сначала составьте ___ покупок.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "сравните", "сравнить → сравните (gebiedende wijs)",
     "___ цену в разных магазинах! (сравнить)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "историю", "история цены = prijsgeschiedenis",
     "Посмотрите ___ цены товара.", instr="Vul in", size=20, gap=8)
e.head("C · ПОКУПКИ", 25)
e.match_set("B1", "Woorden koppelen",
            ["скидка", "промокод", "список", "цена"],
            ["код со скидкой",
             "сколько стоит товар",
             "что вы хотите купить",
             "товар стоит дешевле"],
            ["d", "a", "c", "b"],
            ["Korting d", "Promocode a", "Lijst c", "Prijs b"],
            instr="Koppel de paren")
e.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.bridge("Maak correcte zinnen van de woorden.")
e.ex("B1", "Zinnen bouwen", "Промокод — это код со скидкой.", "Definitiezin: это",
     "промокод / — это / код со скидкой → ___", instr="Zinnen bouwen", size=20, gap=8)
e.ex("A2", "Zinnen bouwen", "Сначала составьте список покупок.", "Gebiedende wijs + lijdend voorwerp",
     "сначала / составьте / список покупок → ___", instr="Zinnen bouwen", size=20, gap=8)
e.ex("B1", "Zinnen bouwen", "Сравните цену в разных магазинах.", "Gebiedende wijs + plaats",
     "сравните / цену / в разных магазинах → ___", instr="Zinnen bouwen", size=20, gap=8)
e.ex("B1", "Zinnen bouwen", "Не спешите с покупкой.", "Ontkennende gebiedende wijs: не спешите",
     "не спешите / с покупкой → ___", instr="Zinnen bouwen", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-molodezh.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · БОЛЬШОЙ РАЗБОР (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("БОЛЬШОЙ РАЗБОР · Diepgaand", "Lucerna", "УРОВЕНЬ B2 · Неделя с праздником посреди · Een week met een feestdag in het midden")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-main")
f.title("Неделя с праздником посреди: как её прожить", 36)
f.byline("От редакции Lucerna · Уровень чтения: B2")
f.para("Неделя со 2 по 8 ноября — странная: два дня работаем, один день отдыхаем, два дня работаем — и выходные. Такие недели сбивают ритм: в понедельник трудно начать, а в четверг трудно вернуться.")
f.para("Многие берут отпуск в четверг и в пятницу. Так получается пять дней отдыха подряд: среда, четверг, пятница, суббота и воскресенье. Пять дней — почти маленькие каникулы!")
f.para("Вторая стратегия — короткая поездка: уехать в среду утром и вернуться вечером. Один день — и уже путешествие. Третья — остаться дома: выспаться, погулять и никуда не спешить.")
f.para("В такие недели офисы обычно тише: кто-то в отпуске, кто-то работает из дома. А в четверг и в пятницу — снова рабочие дни, и ритм возвращается.")
f.gloss("сбивают ритм halen je uit je ritme · подряд achter elkaar · из дома vanuit huis (werken).")
f.end_report()

bx = COLX[3]
cal = ["2–3 ноября — рабочие дни (3 ноября — на час короче)",
       "4 ноября — выходной: День народного единства",
       "5–6 ноября — снова рабочие дни",
       "7–8 ноября — выходные"]
sy6 = 200
sh6 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in cal) + 32
p.rect(bx, sy6, CW, sh6, fill=BOX, stroke=LINE, sw=1.4)
yy6 = sy6 + 16
p.text(bx + 22, yy6 + 26, "НЕДЕЛЯ 2–8 НОЯБРЯ", 24, "sans", True, OLIVE)
yy6 += 52
for t in cal:
    yy6 = p.para(bx + 22, yy6 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
pc = ["За: пять дней отдыха подряд — почти каникулы.",
      "Против: ритм сбивается, а в четверг трудно вернуться."]
sy6b = sy6 + sh6 + 24
sh6b = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in pc) + 32
p.rect(bx, sy6b, CW, sh6b, fill="#f1ead6", stroke=LINE, sw=1.4)
yy6 = sy6b + 16
p.text(bx + 22, yy6 + 26, "ЗА И ПРОТИВ · Voor en tegen", 24, "sans", True, OLIVE)
yy6 += 52
for t in pc:
    yy6 = p.para(bx + 22, yy6 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", sy6b + sh6b)

dy = 1300
p.text(MX, dy + 26, "НЕДЕЛЯ ДЕНЬ ЗА ДНЁМ · De week dag voor dag", 26, "sans", True, OLIVE)
days = [("2", "пн"), ("3", "вт"), ("4", "ср"), ("5", "чт"), ("6", "пт"), ("7", "сб"), ("8", "вс")]
cellw = (RIGHT - MX) // 7
for i, (dn, wd) in enumerate(days):
    cx = MX + i * cellw
    if i == 2:
        fillc = "#e3b7a4"
    elif i == 1:
        fillc = "#efe3bd"
    elif i in (5, 6):
        fillc = "#efe3bd"
    else:
        fillc = BOX
    p.rect(cx + 2, dy + 44, cellw - 4, 96, fill=fillc, stroke=LINE, sw=1.2)
    p.text(cx + cellw / 2, dy + 92, dn, 30, "serif", True, INK, anchor="middle")
    p.text(cx + cellw / 2, dy + 124, wd, 19, "sans", False, GREY, anchor="middle")
p.para(MX, dy + 168, "Светлое — рабочие дни · жёлтое — короткий вторник и выходные · розовое — праздник 4 ноября.", 20, "serif", False, GREY, RIGHT - MX, 1.35)

chy = dy + 226
p.text(MX, chy + 26, "КАК ПРОВЕДУТ СРЕДУ 4 НОЯБРЯ? · УЧЕБНЫЕ ДАННЫЕ · Oefengegevens", 26, "sans", True, OLIVE)
p.text(MX, chy + 56, "Это учебный опрос редакции для упражнений — не настоящая статистика. Dit zijn oefengegevens van de redactie, geen echte statistiek.", 19.5, "sans", False, BRICK)
chart = [("Дома с семьёй", 34), ("Короткая поездка", 28),
         ("Ярмарка или концерт", 22), ("Просто выспятся", 16)]
yy = chy + 84
for lab, val in chart:
    w_px = round(val * 600 / 34)
    p.text(MX, yy + 24, lab, 21.5, "serif", False, INK)
    p.rect(MX + 620, yy + 2, w_px, 30, fill=OLIVE)
    p.text(MX + 620 + w_px + 14, yy + 24, f"{val}%", 21.5, "sans", True, BRICK)
    yy += 46
print("P6 chart ends", yy)

ey = yy + 44
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Oefeningen pagina 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · Niveaus door elkaar — zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · КАЛЕНДАРЬ И ДИАГРАММА", 25)
e.bridge("Beantwoord aan de hand van de kalenderstrook en de oefengrafiek.")
e.ex("B2", "Meerkeuze", "B", "3 vrije dagen in de week (woensdag, zaterdag, zondag)",
     "Сколько выходных дней в неделе 2–8 ноября? A. 2 · B. 3 · C. 5", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "3", "De korte werkdag is 3 november",
     "Короткий день недели — ___ ноября.", instr="Vul in", size=20, gap=8)
e.ex("B2", "Meerkeuze", "B", "Oefengegevens: de meesten blijven thuis bij familie",
     "По учебным данным, больше всего людей... A. поедут в поездку · B. останутся дома с семьёй · C. пойдут на ярмарку", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "28", "Oefengegevens: 28%",
     "По учебным данным, в короткую поездку поедут ___ % людей.", instr="Vul in", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "22", "Oefengegevens: 22%",
     "По учебным данным, на ярмарку или концерт пойдут ___ % людей.", instr="Vul in", size=20, gap=8)
e.ex("B2", "Meerkeuze", "B", "4 november is Dag van de Eenheid",
     "4 ноября — это... A. рабочий день · B. День народного единства · C. начало каникул", size=20, gap=8)
e.head("B · ПО ТЕКСТУ", 25)
e.bridge("Vul de woorden van pagina 6 in.")
e.ex("B2", "Voltooi de zin", "отпуск", "отпуск = verlof",
     "Многие берут ___ в четверг и в пятницу.", instr="Vul in", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "пять", "vijf dagen achter elkaar: пять дней",
     "Так получается ___ дней отдыха подряд.", instr="Vul in", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "тише", "тише = stiller",
     "В такие недели офисы обычно ___.", instr="Vul in", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "один", "Dagtocht: на один день",
     "Короткая поездка — на ___ день.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "рабочие", "рабочие дни = werkdagen",
     "В четверг и в пятницу — снова ___ дни.", instr="Vul in", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "посреди", "посреди = in het midden",
     "Среда — выходной ___ недели.", instr="Vul in", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "выспаться", "выспаться = uitslapen",
     "Дома можно ___ и никуда не спешить.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "отдыхаем", "отдыхать → отдыхаем",
     "Два дня работаем, один день ___, два дня работаем.", instr="Vul in", size=20, gap=8)
e.head("C · СОЕДИНИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.bridge("Voeg de twee zinnen samen tot één zin.")
e.ex("B2", "Zinsomvorming", "Люди берут отпуск в четверг и в пятницу и получают пять дней отдыха.", "Verbind met и",
     "Люди берут отпуск в четверг и в пятницу. Они получают пять дней отдыха. → ___ (и)", instr="Herschrijf", size=20, gap=8)
e.ex("B2", "Zinsomvorming", "Среда — выходной, поэтому школьники отдыхают.", "поэтому = dus, daarom",
     "Среда — выходной. Школьники отдыхают. → ___ (поэтому)", instr="Herschrijf", size=20, gap=8)
e.ex("B1", "Zinsomvorming", "Одни едут в поездку, а другие остаются дома.", "а voor contrast",
     "Одни едут в поездку. Другие остаются дома. → ___ (а)", instr="Herschrijf", size=20, gap=8)
e.ex("B1", "Zinsomvorming", "Люди идут на ярмарку или остаются дома.", "или = of",
     "Люди идут на ярмарку. Люди остаются дома. → ___ (или)", instr="Herschrijf", size=20, gap=8)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-razbor.svg")
print("P6 saved, exercises so far:", len(REG))
