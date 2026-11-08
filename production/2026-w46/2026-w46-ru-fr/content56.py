# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · МОЛОДЁЖЬ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("МОЛОДЁЖЬ　JEUNESSE", "Lucerna", "УРОВЕНЬ B1　11 ноября: день покупок и посылок　11 novembre : jour des achats et des colis")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P5-feature")
f.title("11 ноября: день покупок и посылок", 32)
f.byline("От редакции Lucerna　Уровень чтения: B1")
f.para("В среду, 11 ноября, — главный день распродажи 11.11: пик скидок. Распродажа на Ozon идёт с 22 октября по 12 ноября. По данным пресс-службы, к ноябрьским акциям присоединились больше 600 тысяч продавцов — на 16% больше, чем год назад.")
f.para("В прошлом году, 11 ноября 2025 года, на Ozon сделали больше 14,4 миллиона заказов за один день. Чаще всего покупают смартфоны, ноутбуки и крупную бытовую технику — так пишут о структуре спроса.")
f.para("А что потом? Посылку надо отследить, получить и проверить. Если товар не подошёл, его можно вернуть: с 11 по 30 ноября ожидается пик возвратов — многие заказывают несколько размеров для примерки.")
f.para("И не забывайте о промокодах: советы покупателям напоминают, что промокоды на электронику действуют обычно всего 4–7 дней. Проверьте срок кода, пока он не закончился!")
f.gloss("отследить suivre · подошёл convenait · примерки essayage.")
f.head("А ЧТО ДАЛЬШЕ?", 25)
f.para("Распродажа не заканчивается 11 ноября: «Чёрная пятница» на Ozon пройдёт с 13 ноября по 2 декабря, в «М.Видео» начнётся 12 ноября, а на Wildberries — с 16 по 30 ноября. Но умный покупатель не спешит: сначала список, потом цены, потом промокод.")
f.para("А вы уже получили свои посылки? Напишите нам: что вы купили на 11.11?")
f.gloss("закончился s’est terminé · спешит est pressé.")
f.end_report()

ix = COLX[3]
image(p, "market.jpg", ix, 200, CW, 280)
cy5 = caption(p, ix, 480, CW, "На рынке: свежие овощи и фрукты. Покупки — тоже выбор: сравнить цены и не спешить.",
              "Фото: Престон Керес (USDA) — общественное достояние (Wikimedia Commons)")
facts = ["11.11 на Ozon: 22 октября – 12 ноября.",
         "Больше 600 тысяч продавцов (+16%).",
         "В 2025 году — 14,4 млн заказов за день.",
         "Пик возвратов: 11–30 ноября.",
         "«Чёрная пятница»: с 12–13 ноября."]
sy5 = cy5 + 24
sh5 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy5, CW, sh5, fill=BOX)
yy5 = sy5 + 16
p.text(ix + 22, yy5 + 26, "11.11 В ЦИФРАХ", 24, "sans", True, OLIVE)
yy5 += 52
for t in facts:
    yy5 = p.para(ix + 22, yy5 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 ends", sy5 + sh5)

ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ　EXERCICES DE LA PAGE 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　Les niveaux peuvent être mélangés ; cherchez par numéro d’exercice", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　ПОНИМАНИЕ", 25)
e.bridge("Lisez l’article de la page 5 et choisissez les bonnes réponses.")
e.ex("A2", "Choix", "B", "Les soldes ont commencé le 22 octobre",
     "Распродажа 11.11 на Ozon идёт... A. с 12 ноября · B. с 22 октября · C. с 16 ноября", size=20, gap=8)
e.ex("A2", "Choix", "C", "Plus de 600 000 vendeurs",
     "К акциям присоединились... A. 14,4 млн продавцов · B. 16 продавцов · C. больше 600 тысяч продавцов", size=20, gap=8)
e.ex("B1", "Choix", "A", "14,4 millions de commandes le 11 novembre 2025",
     "11 ноября 2025 года на Ozon сделали... A. больше 14,4 млн заказов · B. 600 тысяч заказов · C. 16 заказов", size=20, gap=8)
e.ex("B1", "Choix", "B", "Pic des retours du 11 au 30 novembre",
     "Пик возвратов ожидается... A. 22 октября · B. 11–30 ноября · C. 12 ноября", size=20, gap=8)
e.ex("A2", "Choix", "A", "Black Friday Ozon à partir du 13 novembre",
     "«Чёрная пятница» на Ozon начнётся... A. 13 ноября · B. 11 ноября · C. 22 октября", size=20, gap=8)
e.head("B　СЛОВА ПОКУПОК", 25)
e.bridge("Complétez avec les mots de la page 5.")
e.ex("A2", "Compléter", "посылку", "посылка = un colis",
     "Надо отследить и получить ___.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter", "вернуть", "вернуть = renvoyer",
     "Если товар не подошёл, его можно ___.", instr="Compléter", size=20, gap=8)
e.ex("A2", "Compléter", "промокод", "промокод = un code promo",
     "Проверьте срок: ___ действует 4–7 дней.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter", "заказов", "заказ = une commande",
     "В прошлом году сделали 14,4 млн ___.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter", "пик", "пик скидок = le pic des soldes",
     "11 ноября — ___ скидок.", instr="Compléter", size=20, gap=8)
e.head("C　ПОКУПКИ", 25)
e.match_set("B1", "Appariement",
            ["посылка", "возврат", "промокод", "пик"],
            ["код со скидкой",
             "товар возвращают в магазин",
             "самое большое число заказов",
             "товар, который прислали по почте"],
            ["d", "b", "a", "c"],
            ["colis d", "retour b", "code promo a", "pic c"],
            instr="Associer")
e.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.bridge("Formez des phrases correctes avec les mots.")
e.ex("B1", "Phrases", "Посылку надо отследить и проверить.", "Verbe modal + infinitif",
     "посылку / надо / отследить и проверить → ___", instr="Phrases", size=20, gap=8)
e.ex("A2", "Phrases", "Сначала составьте список покупок.", "Impératif + objet",
     "сначала / составьте / список покупок → ___", instr="Phrases", size=20, gap=8)
e.ex("B1", "Phrases", "Промокод действует 4–7 дней.", "Sujet + verbe + temps",
     "промокод / действует / 4–7 дней → ___", instr="Phrases", size=20, gap=8)
e.ex("B1", "Phrases", "Не спешите с покупкой.", "Impératif négatif : не спешите",
     "не спешите / с покупкой → ___", instr="Phrases", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-molodezh.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · БОЛЬШОЙ РАЗБОР (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("БОЛЬШОЙ РАЗБОР　EN PROFONDEUR", "Lucerna", "УРОВЕНЬ B2　Обычная неделя: пять рабочих дней　Une semaine ordinaire : cinq jours de travail")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-main")
f.title("Обычная неделя: как её прожить", 32)
f.byline("От редакции Lucerna　Уровень чтения: B2")
f.para("Неделя с 9 по 15 ноября — обычная: пять рабочих дней, а потом выходные. Никаких праздников посреди недели, никаких коротких дней. Такие недели — самые частые в году, и именно они задают ритм жизни.")
f.para("В ноябре 20 рабочих дней и 10 выходных. Профессиональные праздники — День полиции, День экономиста — не меняют календарь: они не дают выходных. Поэтому обычная неделя — это честные пять дней работы и учёбы.")
f.para("Как прожить такую неделю хорошо? Планируйте: в понедельник — самое трудное, в среду — середина, а в пятницу — уже почти выходные. Вечером в среду можно пойти в кино, а в субботу — выспаться.")
f.para("Обычная неделя — это ещё и время посылок: заказы с 11.11 приходят именно на этой неделе. Проверьте посылку, примерьте покупку — и не забудьте вернуть то, что не подошло.")
f.gloss("задают ритм donnent le rythme · честные de vrais, honnêtes · середина le milieu.")
f.end_report()

bx = COLX[3]
cal = ["9–13 ноября — пять рабочих дней",
       "10 ноября — День полиции (рабочий день)",
       "11 ноября — 11.11 и День экономиста",
       "14–15 ноября — выходные"]
sy6 = 200
sh6 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in cal) + 32
p.rect(bx, sy6, CW, sh6, fill=BOX)
yy6 = sy6 + 16
p.text(bx + 22, yy6 + 26, "НЕДЕЛЯ 9–15 НОЯБРЯ", 24, "sans", True, OLIVE)
yy6 += 52
for t in cal:
    yy6 = p.para(bx + 22, yy6 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
pc = ["За: ритм ровный, ничего не сбивается.",
      "Против: ни одного праздника посреди недели."]
sy6b = sy6 + sh6 + 24
sh6b = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in pc) + 32
p.rect(bx, sy6b, CW, sh6b, fill="#f0eee5")
yy6 = sy6b + 16
p.text(bx + 22, yy6 + 26, "ЗА И ПРОТИВ　POUR ET CONTRE", 24, "sans", True, OLIVE)
yy6 += 52
for t in pc:
    yy6 = p.para(bx + 22, yy6 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", sy6b + sh6b)

dy = 1300
p.text(MX, dy + 26, "НЕДЕЛЯ ДЕНЬ ЗА ДНЁМ　LA SEMAINE JOUR APRÈS JOUR", 26, "sans", True, OLIVE)
days = [("9", "пн"), ("10", "вт"), ("11", "ср"), ("12", "чт"), ("13", "пт"), ("14", "сб"), ("15", "вс")]
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
p.para(MX, dy + 168, "Светлое — рабочие дни (9–13 ноября) · жёлтое — выходные (14–15 ноября) · праздников посреди недели нет.", 20, "serif", False, GREY, RIGHT - MX, 1.35)

chy = dy + 226
p.text(MX, chy + 26, "ЧЕМ ЗАЙМУТСЯ НА ЭТОЙ НЕДЕЛЕ?　DONNÉES D’EXERCICE", 26, "sans", True, OLIVE)
p.text(MX, chy + 56, "Ceci est un sondage d’exercice de la rédaction — pas de vraies statistiques.", 19.5, "sans", False, OLIVE)
chart = [("Работа и учёба", 42), ("Покупки на 11.11", 24),
         ("Кино и книги", 20), ("Спорт и прогулки", 14)]
yy = chy + 84
for lab, val in chart:
    w_px = round(val * 600 / 42)
    p.text(MX, yy + 24, lab, 21.5, "serif", False, INK)
    p.rect(MX + 620, yy + 2, w_px, 30, fill=OLIVE)
    p.text(MX + 620 + w_px + 14, yy + 24, f"{val}%", 21.5, "sans", True, OLIVE)
    yy += 46
print("P6 chart ends", yy)

ey = yy + 44
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ　EXERCICES DE LA PAGE 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　Les niveaux peuvent être mélangés ; cherchez par numéro d’exercice", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　КАЛЕНДАРЬ И ДИАГРАММА", 25)
e.bridge("Répondez à l’aide de la bande-calendrier et du graphique d’exercice.")
e.ex("B2", "Choix", "B", "2 jours de repos dans la semaine (samedi, dimanche)",
     "Сколько выходных дней в неделе 9–15 ноября? A. 0 · B. 2 · C. 5", size=20, gap=8)
e.ex("B2", "Compléter", "5", "5 jours de travail dans la semaine",
     "На этой неделе ___ рабочих дней.", instr="Compléter", size=20, gap=8)
e.ex("B2", "Choix", "B", "Données d’exercice : le travail et les études en tête",
     "По учебным данным, больше всего людей... A. пойдут в кино · B. будут работать и учиться · C. займутся спортом", size=20, gap=8)
e.ex("B2", "Compléter", "24", "Données d’exercice : 24 %",
     "По учебным данным, покупками на 11.11 займутся ___ % людей.", instr="Compléter", size=20, gap=8)
e.ex("B2", "Compléter", "20", "Données d’exercice : 20 %",
     "По учебным данным, кино и книгами займутся ___ % людей.", instr="Compléter", size=20, gap=8)
e.ex("B2", "Choix", "B", "Les fêtes professionnelles ne donnent pas de jour de repos",
     "Профессиональные праздники... A. дают выходной · B. не меняют календарь · C. переносят выходные", size=20, gap=8)
e.head("B　ПО ТЕКСТУ", 25)
e.bridge("Complétez avec les mots de la page 6.")
e.ex("B2", "Compléter", "ритм", "ритм = le rythme",
     "Обычные недели задают ___ жизни.", instr="Compléter", size=20, gap=8)
e.ex("B2", "Compléter", "середина", "середина недели = le milieu de la semaine",
     "Среда — ___ недели.", instr="Compléter", size=20, gap=8)
e.ex("B2", "Compléter", "ровный", "ровный ритм = un rythme régulier",
     "Ритм обычной недели — ___.", instr="Compléter", size=20, gap=8)
e.ex("B2", "Compléter", "пять", "Cinq jours de travail d’affilée : пять дней",
     "Обычная неделя — это ___ рабочих дней подряд.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter", "рабочие", "рабочие дни = les jours de travail",
     "Понедельник–пятница — ___ дни.", instr="Compléter", size=20, gap=8)
e.ex("B2", "Compléter", "посреди", "посреди = au milieu",
     "Праздников ___ недели нет.", instr="Compléter", size=20, gap=8)
e.ex("B2", "Compléter", "выспаться", "выспаться = bien dormir, récupérer",
     "В субботу можно ___.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter", "работаем", "работать → работаем",
     "Пять дней ___ , два дня отдыхаем.", instr="Compléter", size=20, gap=8)
e.head("C　СОЕДИНИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.bridge("Réunissez les deux phrases en une seule.")
e.ex("B2", "Transformer", "Неделя обычная, поэтому ритм ровный.", "поэтому = donc",
     "Неделя обычная. Ритм ровный. → ___ (поэтому)", instr="Transformer", size=20, gap=8)
e.ex("B2", "Transformer", "В понедельник трудно начать, а в пятницу уже почти выходные.", "а marque un contraste",
     "В понедельник трудно начать. В пятницу уже почти выходные. → ___ (а)", instr="Transformer", size=20, gap=8)
e.ex("B1", "Transformer", "Одни идут в кино, а другие остаются дома.", "а marque un contraste",
     "Одни идут в кино. Другие остаются дома. → ___ (а)", instr="Transformer", size=20, gap=8)
e.ex("B1", "Transformer", "Люди проверяют посылки или возвращают покупки.", "или = ou",
     "Люди проверяют посылки. Люди возвращают покупки. → ___ (или)", instr="Transformer", size=20, gap=8)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-razbor.svg")
print("P6 saved, exercises so far:", len(REG))
