# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · МОЛОДЁЖЬ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("МОЛОДЁЖЬ　JONGEREN", "Lucerna", "УРОВЕНЬ B1　«Чёрная пятница»: скидки с 16 ноября　«Black Friday»: uitverkoop vanaf 16 november")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P5-feature")
f.title("«Чёрная пятница»: скидки с 16 ноября", 32)
f.byline("От редакции Lucerna　Уровень чтения: B1")
f.para("«Чёрная пятница» — большая распродажа в конце ноября. Календарная дата в 2026 году — пятница, 27 ноября, а «Киберпонедельник» — 30 ноября. Но в России акции идут дольше: на маркетплейсах скидки начинаются уже в середине месяца. В России «чёрную пятницу» проводят с 2013 года.")
f.para("Когда и где? На Ozon — с 13 ноября по 2 декабря, на Wildberries — с 16 по 30 ноября: это главная распродажа года на площадке. В «М.Видео» акции идут с 12 ноября, на «Яндекс Маркете» — предварительно с 25 по 27 ноября, на Lamoda — с 27 по 30 ноября.")
f.para("А что потом? Посылку надо отследить, получить и проверить. Если товар не подошёл, его можно вернуть: с 11 по 30 ноября ожидается пик возвратов — многие заказывают несколько размеров для примерки.")
f.para("Умный покупатель не спешит: сначала список, потом цены, потом промокод. Проверьте старую цену: «скидка 90%» не всегда значит, что товар дешёвый. И помните: промокоды на электронику действуют обычно всего 4–7 дней.")
f.gloss("календарная дата kalenderdatum · подошёл paste goed · примерки passen.")
f.head("А ЧТО С 11.11?", 25)
f.para("Распродажа 11.11 на Ozon шла с 22 октября по 12 ноября. В прошлом году, 11 ноября 2025 года, на Ozon сделали больше 14,4 миллиона заказов за один день. Чаще всего покупают смартфоны, ноутбуки и крупную бытовую технику.")
f.para("А вы уже получили свои посылки с 11.11? Напишите нам: что вы купили — и что купите на «чёрную пятницу»?")
f.gloss("в прошлом году vorig jaar · бытовую технику huishoudelijke apparaten.")
f.end_report()

ix = COLX[3]
image(p, "market.jpg", ix, 200, CW, 280)
cy5 = caption(p, ix, 480, CW, "На рынке: свежие овощи и фрукты. Покупки — тоже выбор: сравнить цены и не спешить.",
              "Фото: Престон Керес (USDA) — общественное достояние (Wikimedia Commons)")
facts = ["«Чёрная пятница» — 27 ноября.",
         "Ozon: 13 ноября – 2 декабря.",
         "Wildberries: 16–30 ноября.",
         "«М.Видео»: с 12 ноября.",
         "«Яндекс Маркет»: 25–27 ноября.",
         "«Киберпонедельник» — 30 ноября."]
sy5 = cy5 + 24
sh5 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy5, CW, sh5, fill=BOX)
yy5 = sy5 + 16
p.text(ix + 22, yy5 + 26, "ЧЁРНАЯ ПЯТНИЦА: ДАТЫ", 24, "sans", True, OLIVE)
yy5 += 52
for t in facts:
    yy5 = p.para(ix + 22, yy5 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 ends", sy5 + sh5)

ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ　OEFENINGEN BIJ PAGINA 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　Niveaus kunnen gemengd zijn; zoek op opgavenummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　ПОНИМАНИЕ", 25)
e.bridge("Lees pagina 5 en kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "De Black Friday op de kalender is vrijdag 27 november",
     "Календарная дата «чёрной пятницы» в 2026 году — это... A. 16 ноября · B. 27 ноября · C. 30 ноября", size=20, gap=8)
e.ex("A2", "Meerkeuze", "C", "Black Friday op Wildberries: 16–30 november",
     "«Чёрная пятница» на Wildberries идёт... A. 13 ноября – 2 декабря · B. 25–27 ноября · C. 16–30 ноября", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "Black Friday op Ozon: 13 november–2 december",
     "«Чёрная пятница» на Ozon идёт... A. с 13 ноября по 2 декабря · B. с 16 по 30 ноября · C. с 25 по 27 ноября", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Cyber Monday is op 30 november",
     "«Киберпонедельник» будет... A. 27 ноября · B. 30 ноября · C. 12 ноября", size=20, gap=8)
e.ex("A2", "Meerkeuze", "A", "In Rusland bestaat Black Friday sinds 2013",
     "В России «чёрную пятницу» проводят... A. с 2013 года · B. с 2025 года · C. с 2016 года", size=20, gap=8)
e.head("B　СЛОВА ПОКУПОК", 25)
e.bridge("Vul in met de woorden van pagina 5.")
e.ex("A2", "Voltooi de zin", "распродажа", "распродажа = grote uitverkoop",
     "«Чёрная пятница» — большая ___.", instr="Voltooi de zin", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "вернуть", "вернуть = terugsturen",
     "Если товар не подошёл, его можно ___.", instr="Voltooi de zin", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "промокод", "промокод = een kortingscode",
     "Проверьте срок: ___ действует 4–7 дней.", instr="Voltooi de zin", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "заказов", "заказ = een bestelling",
     "В прошлом году сделали 14,4 млн ___.", instr="Voltooi de zin", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "скидка", "скидка = korting",
     "«___ 90%» не всегда значит, что товар дешёвый.", instr="Voltooi de zin", size=20, gap=8)
e.head("C　ПОКУПКИ", 25)
e.match_set("B1", "Woorden koppelen",
            ["распродажа", "возврат", "промокод", "скидка"],
            ["код со скидкой",
             "товар возвращают в магазин",
             "цена ниже обычной",
             "большая продажа со скидками"],
            ["d", "b", "a", "c"],
            ["Grote uitverkoop d", "retour b", "kortingscode a", "Korting c"],
            instr="Koppel")
e.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.bridge("Maak juiste zinnen van de woorden.")
e.ex("B1", "Zinnen bouwen", "Сначала список, потом цены, потом промокод.", "Eerst de lijst, dan de prijzen, dan de kortingscode",
     "сначала / список, / потом / цены, / потом / промокод → ___", instr="Zinnen bouwen", size=20, gap=8)
e.ex("A2", "Zinnen bouwen", "«Чёрная пятница» начинается 16 ноября.", "Onderwerp + werkwoord + tijd",
     "«чёрная пятница» / начинается / 16 ноября → ___", instr="Zinnen bouwen", size=20, gap=8)
e.ex("B1", "Zinnen bouwen", "Промокод действует 4–7 дней.", "Onderwerp + werkwoord + tijd",
     "промокод / действует / 4–7 дней → ___", instr="Zinnen bouwen", size=20, gap=8)
e.ex("B1", "Zinnen bouwen", "Не спешите с покупкой.", "Ontkennende gebiedende wijs: не спешите",
     "не спешите / с покупкой → ___", instr="Zinnen bouwen", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-molodezh.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · БОЛЬШОЙ РАЗБОР (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("БОЛЬШОЙ РАЗБОР　UITGEDIEPT", "Lucerna", "УРОВЕНЬ B2　Неделя 16–22 ноября: как её прожить　De week van 16–22 november: hoe beleef je hem")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-main")
f.title("Неделя 16–22 ноября: как её прожить", 32)
f.byline("От редакции Lucerna　Уровень чтения: B2")
f.para("Неделя с 16 по 22 ноября — обычная: пять рабочих дней, а потом выходные. Никаких праздников посреди недели, никаких коротких дней. Такие недели — самые частые в году, и именно они задают ритм жизни.")
f.para("В ноябре 20 рабочих дней и 10 выходных. Профессиональные праздники — День студента, День психолога — не меняют календарь: они не дают выходных. Поэтому обычная неделя — это честные пять дней работы и учёбы.")
f.para("Как прожить такую неделю хорошо? Планируйте: в понедельник — самое трудное, в среду — середина, а в пятницу — уже почти выходные. Вечером в четверг можно пойти в кино, а в субботу — выспаться и посмотреть футбол: 15-й тур!")
f.para("Обычная неделя — это ещё и время посылок и скидок: заказы с 11.11 приходят именно на этой неделе, а «чёрная пятница» уже началась. Проверьте посылку, примерьте покупку — и не забудьте вернуть то, что не подошло.")
f.gloss("задают ритм bepalen het ritme · честные echte, eerlijke · середина het midden.")
f.end_report()

bx = COLX[3]
cal = ["16–20 ноября — пять рабочих дней",
       "17 ноября — День студента (вторник)",
       "18 ноября — день рождения Деда Мороза",
       "21–22 ноября — выходные + 15-й тур"]
sy6 = 200
sh6 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in cal) + 32
p.rect(bx, sy6, CW, sh6, fill=BOX)
yy6 = sy6 + 16
p.text(bx + 22, yy6 + 26, "НЕДЕЛЯ 16–22 НОЯБРЯ", 24, "sans", True, OLIVE)
yy6 += 52
for t in cal:
    yy6 = p.para(bx + 22, yy6 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
pc = ["За: ритм ровный, ничего не сбивается.",
      "Против: ни одного праздника посреди недели."]
sy6b = sy6 + sh6 + 24
sh6b = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in pc) + 32
p.rect(bx, sy6b, CW, sh6b, fill="#f0eee5")
yy6 = sy6b + 16
p.text(bx + 22, yy6 + 26, "ЗА И ПРОТИВ　VOOR EN TEGEN", 23, "sans", True, OLIVE)
yy6 += 52
for t in pc:
    yy6 = p.para(bx + 22, yy6 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", sy6b + sh6b)

dy = 1300
p.text(MX, dy + 26, "НЕДЕЛЯ ДЕНЬ ЗА ДНЁМ　DE WEEK DAG NA DAG", 26, "sans", True, OLIVE)
days = [("16", "пн"), ("17", "вт"), ("18", "ср"), ("19", "чт"), ("20", "пт"), ("21", "сб"), ("22", "вс")]
cellw = (RIGHT - MX) // 7
for i, (dn, wd) in enumerate(days):
    cx = MX + i * cellw
    if i in (5, 6):
        fillc = "#efe3bd"
    else:
        fillc = BOX
    p.rect(cx + 2, dy + 44, cellw - 4, 96, fill=fillc, stroke=LINE, sw=1.2)
    p.text(cx + cellw / 2, dy + 92, dn, 30, "serif", True, INK, anchor="middle")
    p.text(cx + cellw / 2, dy + 124, wd, 19, "sans", False, GREY, anchor="middle")
p.para(MX, dy + 168, "Светлое — рабочие дни (16–20 ноября) · жёлтое — выходные (21–22 ноября) · праздников посреди недели нет.", 20, "serif", False, GREY, RIGHT - MX, 1.35)

chy = dy + 226
p.text(MX, chy + 26, "ЧЕМ ЗАЙМУТСЯ НА ЭТОЙ НЕДЕЛЕ?　УЧЕБНЫЕ ДАННЫЕ　OEFENGEGEVENS", 26, "sans", True, OLIVE)
p.text(MX, chy + 56, "Это учебный опрос редакции для упражнений — не настоящая статистика. Dit is een oefenenquête van de redactie — geen echte statistiek.", 19.5, "sans", False, OLIVE)
chart = [("Работа и учёба", 38), ("Покупки и скидки", 26),
         ("Кино и книги", 18), ("Спорт и прогулки", 18)]
yy = chy + 84
for lab, val in chart:
    w_px = round(val * 600 / 38)
    p.text(MX, yy + 24, lab, 21.5, "serif", False, INK)
    p.rect(MX + 620, yy + 2, w_px, 30, fill=OLIVE)
    p.text(MX + 620 + w_px + 14, yy + 24, f"{val}%", 21.5, "sans", True, OLIVE)
    yy += 46
print("P6 chart ends", yy)

ey = yy + 44
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ　OEFENINGEN BIJ PAGINA 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　Niveaus kunnen gemengd zijn; zoek op opgavenummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　КАЛЕНДАРЬ И ДИАГРАММА", 25)
e.bridge("Antwoord met de kalenderstrook en de oefengrafiek.")
e.ex("B2", "Meerkeuze", "B", "2 vrije dagen in de week (zaterdag en zondag)",
     "Сколько выходных дней в неделе 16–22 ноября? A. 0 · B. 2 · C. 5", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "5", "5 werkdagen in de week",
     "На этой неделе ___ рабочих дней.", instr="Voltooi de zin", size=20, gap=8)
e.ex("B2", "Meerkeuze", "B", "Oefengegevens: werk en studie bovenaan",
     "По учебным данным, больше всего людей... A. пойдут в кино · B. будут работать и учиться · C. займутся спортом", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "26", "Oefengegevens: 26 %",
     "По учебным данным, покупками и скидками займутся ___ % людей.", instr="Voltooi de zin", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "18", "Oefengegevens: 18 %",
     "По учебным данным, кино и книгами займутся ___ % людей.", instr="Voltooi de zin", size=20, gap=8)
e.ex("B2", "Meerkeuze", "B", "Beroepsfeestdagen geven geen vrije dag",
     "Профессиональные праздники... A. дают выходной · B. не меняют календарь · C. переносят выходные", size=20, gap=8)
e.head("B　ПО ТЕКСТУ", 25)
e.bridge("Vul in met de woorden van pagina 6.")
e.ex("B2", "Voltooi de zin", "ритм", "ритм = het ritme",
     "Обычные недели задают ___ жизни.", instr="Voltooi de zin", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "середина", "середина недели = midden van de week",
     "Среда — ___ недели.", instr="Voltooi de zin", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "ровный", "ровный ритм = een regelmatig ritme",
     "Ритм обычной недели — ___.", instr="Voltooi de zin", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "пять", "Vijf werkdagen achter elkaar: пять дней",
     "Обычная неделя — это ___ рабочих дней подряд.", instr="Voltooi de zin", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "рабочие", "рабочие дни = werkdagen",
     "Понедельник–пятница — ___ дни.", instr="Voltooi de zin", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "посреди", "посреди = in het midden",
     "Праздников ___ недели нет.", instr="Voltooi de zin", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "выспаться", "выспаться = goed slapen, uitslapen",
     "В субботу можно ___.", instr="Voltooi de zin", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "работаем", "работать → работаем",
     "Пять дней ___ , два дня отдыхаем.", instr="Voltooi de zin", size=20, gap=8)
e.head("C　СОЕДИНИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.bridge("Voeg de twee zinnen samen tot één zin.")
e.ex("B2", "Zinsomvorming", "Неделя обычная, поэтому ритм ровный.", "поэтому = daarom",
     "Неделя обычная. Ритм ровный. → ___ (поэтому)", instr="Zinsomvorming", size=20, gap=8)
e.ex("B2", "Zinsomvorming", "В понедельник трудно начать, а в пятницу уже почти выходные.", "а markeert een tegenstelling",
     "В понедельник трудно начать. В пятницу уже почти выходные. → ___ (а)", instr="Zinsomvorming", size=20, gap=8)
e.ex("B1", "Zinsomvorming", "Одни идут в кино, а другие остаются дома.", "а markeert een tegenstelling",
     "Одни идут в кино. Другие остаются дома. → ___ (а)", instr="Zinsomvorming", size=20, gap=8)
e.ex("B1", "Zinsomvorming", "Люди проверяют посылки или возвращают покупки.", "или = of",
     "Люди проверяют посылки. Люди возвращают покупки. → ___ (или)", instr="Zinsomvorming", size=20, gap=8)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-razbor.svg")
print("P6 saved, exercises so far:", len(REG))
