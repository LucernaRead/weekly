# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · МОЛОДЁЖЬ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("МОЛОДЁЖЬ　JÓVENES", "Lucerna", "УРОВЕНЬ B1　11 ноября: день покупок и посылок　11 de noviembre: día de compras y paquetes")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P5-feature")
f.title("11 ноября: день покупок и посылок", 32)
f.byline("От редакции Lucerna　Уровень чтения: B1")
f.para("В среду, 11 ноября, — главный день распродажи 11.11: пик скидок. Распродажа на Ozon идёт с 22 октября по 12 ноября. По данным пресс-службы, к ноябрьским акциям присоединились больше 600 тысяч продавцов — на 16% больше, чем год назад.")
f.para("В прошлом году, 11 ноября 2025 года, на Ozon сделали больше 14,4 миллиона заказов за один день. Чаще всего покупают смартфоны, ноутбуки и крупную бытовую технику — так пишут о структуре спроса.")
f.para("А что потом? Посылку надо отследить, получить и проверить. Если товар не подошёл, его можно вернуть: с 11 по 30 ноября ожидается пик возвратов — многие заказывают несколько размеров для примерки.")
f.para("И не забывайте о промокодах: советы покупателям напоминают, что промокоды на электронику действуют обычно всего 4–7 дней. Проверьте срок кода, пока он не закончился!")
f.gloss("отследить rastrear · подошёл convenía · примерки probarse (ropa).")
f.head("А ЧТО ДАЛЬШЕ?", 25)
f.para("Распродажа не заканчивается 11 ноября: «Чёрная пятница» на Ozon пройдёт с 13 ноября по 2 декабря, в «М.Видео» начнётся 12 ноября, а на Wildberries — с 16 по 30 ноября. Но умный покупатель не спешит: сначала список, потом цены, потом промокод.")
f.para("А вы уже получили свои посылки? Напишите нам: что вы купили на 11.11?")
f.gloss("закончился terminó · спешит tiene prisa.")
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
p.text(MX, ey + 28, "УПРАЖНЕНИЯ　EJERCICIOS DE LA PÁGINA 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8　Los niveles pueden mezclarse; busca por número de ejercicio", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　ПОНИМАНИЕ", 25)
e.bridge("Lee el artículo de la página 5 y elige las respuestas correctas.")
e.ex("A2", "Opción múltiple", "B", "Las rebajas empezaron el 22 de octubre",
     "Распродажа 11.11 на Ozon идёт... A. с 12 ноября · B. с 22 октября · C. с 16 ноября", size=20, gap=8)
e.ex("A2", "Opción múltiple", "C", "Más de 600.000 vendedores",
     "К акциям присоединились... A. 14,4 млн продавцов · B. 16 продавцов · C. больше 600 тысяч продавцов", size=20, gap=8)
e.ex("B1", "Opción múltiple", "A", "14,4 millones de pedidos el 11 de noviembre de 2025",
     "11 ноября 2025 года на Ozon сделали... A. больше 14,4 млн заказов · B. 600 тысяч заказов · C. 16 заказов", size=20, gap=8)
e.ex("B1", "Opción múltiple", "B", "Pico de devoluciones del 11 al 30 de noviembre",
     "Пик возвратов ожидается... A. 22 октября · B. 11–30 ноября · C. 12 ноября", size=20, gap=8)
e.ex("A2", "Opción múltiple", "A", "Black Friday de Ozon desde el 13 de noviembre",
     "«Чёрная пятница» на Ozon начнётся... A. 13 ноября · B. 11 ноября · C. 22 октября", size=20, gap=8)
e.head("B　СЛОВА ПОКУПОК", 25)
e.bridge("Completa con palabras de la página 5.")
e.ex("A2", "Completar", "посылку", "посылка = un paquete",
     "Надо отследить и получить ___.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "вернуть", "вернуть = devolver",
     "Если товар не подошёл, его можно ___.", instr="Completar", size=20, gap=8)
e.ex("A2", "Completar", "промокод", "промокод = un código promocional",
     "Проверьте срок: ___ действует 4–7 дней.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "заказов", "заказ = un pedido",
     "В прошлом году сделали 14,4 млн ___.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "пик", "пик скидок = el pico de los descuentos",
     "11 ноября — ___ скидок.", instr="Completar", size=20, gap=8)
e.head("C　ПОКУПКИ", 25)
e.match_set("B1", "Emparejamiento",
            ["посылка", "возврат", "промокод", "пик"],
            ["код со скидкой",
             "товар возвращают в магазин",
             "самое большое число заказов",
             "товар, который прислали по почте"],
            ["d", "b", "a", "c"],
            ["paquete d", "devolución b", "código promocional a", "pico c"],
            instr="Empareja")
e.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.bridge("Forma frases correctas con las palabras.")
e.ex("B1", "Frases", "Посылку надо отследить и проверить.", "Verbo modal + infinitivo",
     "посылку / надо / отследить и проверить → ___", instr="Frases", size=20, gap=8)
e.ex("A2", "Frases", "Сначала составьте список покупок.", "Imperativo + objeto",
     "сначала / составьте / список покупок → ___", instr="Frases", size=20, gap=8)
e.ex("B1", "Frases", "Промокод действует 4–7 дней.", "Sujeto + verbo + tiempo",
     "промокод / действует / 4–7 дней → ___", instr="Frases", size=20, gap=8)
e.ex("B1", "Frases", "Не спешите с покупкой.", "Imperativo negativo: не спешите",
     "не спешите / с покупкой → ___", instr="Frases", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-molodezh.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · БОЛЬШОЙ РАЗБОР (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("БОЛЬШОЙ РАЗБОР　EN PROFUNDIDAD", "Lucerna", "УРОВЕНЬ B2　Обычная неделя: пять рабочих дней　Una semana normal: cinco días laborables")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-main")
f.title("Обычная неделя: как её прожить", 32)
f.byline("От редакции Lucerna　Уровень чтения: B2")
f.para("Неделя с 9 по 15 ноября — обычная: пять рабочих дней, а потом выходные. Никаких праздников посреди недели, никаких коротких дней. Такие недели — самые частые в году, и именно они задают ритм жизни.")
f.para("В ноябре 20 рабочих дней и 10 выходных. Профессиональные праздники — День полиции, День экономиста — не меняют календарь: они не дают выходных. Поэтому обычная неделя — это честные пять дней работы и учёбы.")
f.para("Как прожить такую неделю хорошо? Планируйте: в понедельник — самое трудное, в среду — середина, а в пятницу — уже почти выходные. Вечером в среду можно пойти в кино, а в субботу — выспаться.")
f.para("Обычная неделя — это ещё и время посылок: заказы с 11.11 приходят именно на этой неделе. Проверьте посылку, примерьте покупку — и не забудьте вернуть то, что не подошло.")
f.gloss("задают ритм marcan el ritmo · честные de verdad, auténticos · середина el medio.")
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
p.text(bx + 22, yy6 + 26, "ЗА И ПРОТИВ　PROS Y CONTRAS", 24, "sans", True, OLIVE)
yy6 += 52
for t in pc:
    yy6 = p.para(bx + 22, yy6 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", sy6b + sh6b)

dy = 1300
p.text(MX, dy + 26, "НЕДЕЛЯ ДЕНЬ ЗА ДНЁМ　LA SEMANA DÍA A DÍA", 26, "sans", True, OLIVE)
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
p.text(MX, chy + 26, "ЧЕМ ЗАЙМУТСЯ НА ЭТОЙ НЕДЕЛЕ?　DATOS DE PRÁCTICA", 26, "sans", True, OLIVE)
p.text(MX, chy + 56, "Esta es una encuesta de práctica de la redacción — no son estadísticas reales.", 19.5, "sans", False, OLIVE)
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
p.text(MX, ey + 28, "УПРАЖНЕНИЯ　EJERCICIOS DE LA PÁGINA 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8　Los niveles pueden mezclarse; busca por número de ejercicio", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　КАЛЕНДАРЬ И ДИАГРАММА", 25)
e.bridge("Responde con la tira-calendario y el gráfico de práctica.")
e.ex("B2", "Opción múltiple", "B", "2 días libres en la semana (sábado, domingo)",
     "Сколько выходных дней в неделе 9–15 ноября? A. 0 · B. 2 · C. 5", size=20, gap=8)
e.ex("B2", "Completar", "5", "5 días laborables en la semana",
     "На этой неделе ___ рабочих дней.", instr="Completar", size=20, gap=8)
e.ex("B2", "Opción múltiple", "B", "Datos de práctica: trabajo y estudio a la cabeza",
     "По учебным данным, больше всего людей... A. пойдут в кино · B. будут работать и учиться · C. займутся спортом", size=20, gap=8)
e.ex("B2", "Completar", "24", "Datos de práctica: 24 %",
     "По учебным данным, покупками на 11.11 займутся ___ % людей.", instr="Completar", size=20, gap=8)
e.ex("B2", "Completar", "20", "Datos de práctica: 20 %",
     "По учебным данным, кино и книгами займутся ___ % людей.", instr="Completar", size=20, gap=8)
e.ex("B2", "Opción múltiple", "B", "Las fiestas profesionales no dan día libre",
     "Профессиональные праздники... A. дают выходной · B. не меняют календарь · C. переносят выходные", size=20, gap=8)
e.head("B　ПО ТЕКСТУ", 25)
e.bridge("Completa con palabras de la página 6.")
e.ex("B2", "Completar", "ритм", "ритм = el ritmo",
     "Обычные недели задают ___ жизни.", instr="Completar", size=20, gap=8)
e.ex("B2", "Completar", "середина", "середина недели = mitad de semana",
     "Среда — ___ недели.", instr="Completar", size=20, gap=8)
e.ex("B2", "Completar", "ровный", "ровный ритм = un ritmo regular",
     "Ритм обычной недели — ___.", instr="Completar", size=20, gap=8)
e.ex("B2", "Completar", "пять", "Cinco días laborables seguidos: пять дней",
     "Обычная неделя — это ___ рабочих дней подряд.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "рабочие", "рабочие дни = días laborables",
     "Понедельник–пятница — ___ дни.", instr="Completar", size=20, gap=8)
e.ex("B2", "Completar", "посреди", "посреди = en medio",
     "Праздников ___ недели нет.", instr="Completar", size=20, gap=8)
e.ex("B2", "Completar", "выспаться", "выспаться = dormir bien, descansar",
     "В субботу можно ___.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "работаем", "работать → работаем",
     "Пять дней ___ , два дня отдыхаем.", instr="Completar", size=20, gap=8)
e.head("C　СОЕДИНИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.bridge("Une las dos frases en una sola.")
e.ex("B2", "Transformación", "Неделя обычная, поэтому ритм ровный.", "поэтому = por eso",
     "Неделя обычная. Ритм ровный. → ___ (поэтому)", instr="Transformación", size=20, gap=8)
e.ex("B2", "Transformación", "В понедельник трудно начать, а в пятницу уже почти выходные.", "а marca un contraste",
     "В понедельник трудно начать. В пятницу уже почти выходные. → ___ (а)", instr="Transformación", size=20, gap=8)
e.ex("B1", "Transformación", "Одни идут в кино, а другие остаются дома.", "а marca un contraste",
     "Одни идут в кино. Другие остаются дома. → ___ (а)", instr="Transformación", size=20, gap=8)
e.ex("B1", "Transformación", "Люди проверяют посылки или возвращают покупки.", "или = o",
     "Люди проверяют посылки. Люди возвращают покупки. → ___ (или)", instr="Transformación", size=20, gap=8)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-razbor.svg")
print("P6 saved, exercises so far:", len(REG))
