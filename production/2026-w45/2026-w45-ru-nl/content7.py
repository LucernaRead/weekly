# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ЯЗЫК (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ЯЗЫК · Taal", "Lucerna", "Фокус на язык · Три уровня, три темы · Drie niveaus, drie thema's")

a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · НЕДЕЛЯ СЛОВАМИ", 24)
a.para("О неделе говорим так: выходной — день, когда не работают; будни — рабочие дни; сокращённый день — день на час короче. Примеры: «В среду — выходной», «3 ноября — сокращённый день».", 21.5)
a.para("Отпуск — это дни отдыха от работы. Взять отпуск — значит не работать несколько дней. Пример: «Я беру отпуск в четверг».", 21.5)
a.bridge("выходной vrije dag; будни werkdagen; сокращённый день verkorte werkdag.")
a.ex("A2", "Voltooi de zin", "выходной", "выходной = vrije dag",
     "В среду — ___.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Voltooi de zin", "сокращённый", "сокращённый день = verkorte werkdag",
     "3 ноября — ___ день.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Meerkeuze", "B", "будни = werkdagen",
     "«Будни» значит... A. выходные · B. рабочие дни · C. праздники", size=20.5, gap=10)
a.ex("A2", "Voltooi de zin", "отдыха", "отдых от работы = verlof",
     "Отпуск — это дни ___ от работы.", instr="Vul in", size=20.5, gap=10)
a.end_report()

b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · СЛОВА ПОКУПОК", 24)
b.para("Слова распродажи: скидка — товар стоит дешевле; цена — сколько стоит товар; список — что вы хотите купить. Пример: «Сначала составьте список, потом сравните цены».", 21.5)
b.para("Промокод вводят при покупке: код даёт скидку. Глагол «вводить» — ввести: «Введите промокод!» — так пишут в приложениях.", 21.5)
b.bridge("скидка korting; цена prijs; список lijst; ввести промокод invoeren.")
b.ex("B1", "Voltooi de zin", "Промокод", "промокод = promocode",
     "___ — это код со скидкой.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Voltooi de zin", "список", "список покупок = boodschappenlijst",
     "Мой ___ покупок готов.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Meerkeuze", "A", "скидка = goedkoper",
     "«Скидка» значит... A. товар стоит дешевле · B. товар стоит дороже · C. товара нет", size=20.5, gap=10)
b.ex("B1", "Voltooi de zin", "цены", "сравнить цены = prijzen vergelijken",
     "Сравните ___ в разных магазинах.", instr="Vul in", size=20.5, gap=10)
b.end_report()

c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · КАК ССЫЛАТЬСЯ", 24)
c.para("Когда факт — не ваш, а из прессы, говорите так: «по сообщениям торговой прессы» или «торговая пресса пишет». Это честно: читатель знает, откуда факт.", 21.5)
c.para("Неуверенность — тоже по-русски: «может быть» — возможно; «может быть меньше» — возможно, будет меньше. Говорить «может быть» — признак хорошего уровня!", 21.5)
c.bridge("по сообщениям volgens berichten; пишет schrijft; может быть misschien.")
c.ex("B2", "Voltooi de zin", "По сообщениям", "по сообщениям = volgens berichten",
     "___ торговой прессы, скидок может быть меньше.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Voltooi de zin", "может", "может быть = misschien",
     "Скидок ___ быть меньше.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Meerkeuze", "B", "может быть = misschien",
     "«Может быть» значит... A. точно да · B. возможно · C. точно нет", size=20.5, gap=10)
c.ex("B2", "Voltooi de zin", "пишет", "писать → пишет",
     "Торговая пресса ___: скидок может быть меньше.", instr="Vul in", size=20.5, gap=10)
c.end_report()

bx = COLX[3]
errs = [
    ("«Поздравляю с День единства!»", "→ После «с» нужен творительный падеж: «с Днём единства!»", "Instrumentalis na «с»: с Днём единства."),
    ("«Мы едем к бабушка»", "→ После «к» — дательный падеж: «Мы едем к бабушке».", "Datief na «к»: к бабушке."),
    ("«Скидка 25 процента»", "→ После 5 и больше — «процентов»: «25 процентов».", "Vanaf 5: процентов: 25 процентов."),
    ("«Распродажа с 22 октябрь»", "→ Родительный падеж: «с 22 октября».", "Genitief na «с» (beginpunt): с 22 октября."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ОШИБКИ · Foutenkliniek", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "«промокод» — код со скидкой: его вводят при покупке, и цена становится ниже."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("промокод = promocode.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "СЛОВО · Woordbox", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "промокод = promocode.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "«Здравствуйте! Я учу русский язык и читаю Lucerna. В среду, 4 ноября, я тоже отдохну: пойду на ярмарку с семьёй!» — М. (пример от редакции)"
disc_ru = "Настоящих писем и лучших сочинений к сроку сдачи не поступило: здесь снова пример от редакции. Обещание переносится на VOL.3."
disc_cn = "Nog geen echte brieven of beste teksten — redactievoorbeeld; belofte voor VOL.3. Stuur je brief en je beste tekst voor VOL.3!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(disc_ru, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_cn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "ПИСЬМА ЧИТАТЕЛЕЙ", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, disc_ru, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, disc_cn, 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

fy = 1799  # FIX P7: +29 = 1 extra disclosure line; box bottom 1727.58 -> 1756.58, hline gap stays 28.42
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "ФРАЗЫ НЕДЕЛИ · Zinnen van de week (letterlijk uit dit nummer)", 27, "sans", True, OLIVE)
quotes = [
    ("«Среда, 4 ноября, — выходной посреди рабочей недели»", "Woensdag 4 november is een vrije dag midden in de werkweek.", "Страница 1"),
    ("«Как жить неделю с праздником посреди недели»", "Hoe leef je een week met een feestdag in het midden?", "Страница 1"),
    ("«Во вторник, 3 ноября, рабочий день короче на час»", "Op dinsdag 3 november is de werkdag een uur korter.", "Страница 2"),
    ("«В среду города устраивают ярмарки и концерты»", "Op woensdag houden steden markten en concerten.", "Страница 3"),
    ("«В воскресенье, 8 ноября, — три матча»", "Op zondag 8 november zijn er drie wedstrijden.", "Страница 4"),
    ("«Сначала — список: что вам правда нужно»", "Eerst de lijst: wat heb je echt nodig?", "Страница 5"),
    ("«Многие берут отпуск в четверг и в пятницу»", "Veel mensen nemen donderdag en vrijdag vrij.", "Страница 6"),
    ("«Пять дней — почти маленькие каникулы»", "Vijf dagen — bijna een kleine vakantie!", "Страница 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 145
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

py = 2433  # FIX P7: +29, follows golden block shift; preview bottom 2551, footer line 2580 margin 29
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "СЛЕДУЮЩАЯ НЕДЕЛЯ · Volgende week (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "11 ноября — день распродажи 11.11: что купили читатели? Плюс итоги 14-го тура и ваши письма. До понедельника!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-yazyk.svg")
print("P7 saved, exercises so far:", len(REG))
