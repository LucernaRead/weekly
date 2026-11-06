# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ru-es-proof/rerun-svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ЯЗЫК (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ЯЗЫК · Idioma", "Lucerna", "Фокус на язык · Три уровня, три темы · Tres niveles, tres temas")

a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · НЕДЕЛЯ СЛОВАМИ", 24)
a.para("О неделе говорим так: выходной — день, когда не работают; будни — рабочие дни; сокращённый день — день на час короче. Примеры: «В среду — выходной», «3 ноября — сокращённый день».", 21.5)
a.para("Отпуск — это дни отдыха от работы. Взять отпуск — значит не работать несколько дней. Пример: «Я беру отпуск в четверг».", 21.5)
a.bridge("выходной día festivo; будни días laborables; сокращённый день día de trabajo más corto.")
a.ex("A2", "Completar", "выходной", "выходной = día festivo",
     "В среду — ___.", instr="Completar", size=20.5, gap=10)
a.ex("A2", "Completar", "сокращённый", "сокращённый день = día de trabajo más corto",
     "3 ноября — ___ день.", instr="Completar", size=20.5, gap=10)
a.ex("A2", "Opción múltiple", "B", "будни = días laborables",
     "«Будни» значит... A. выходные · B. рабочие дни · C. праздники", size=20.5, gap=10)
a.ex("A2", "Completar", "отдыха", "отдых от работы = vacaciones",
     "Отпуск — это дни ___ от работы.", instr="Completar", size=20.5, gap=10)
a.end_report()

b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · СЛОВА ПОКУПОК", 24)
b.para("Слова распродажи: скидка — товар стоит дешевле; цена — сколько стоит товар; список — что вы хотите купить. Пример: «Сначала составьте список, потом сравните цены».", 21.5)
b.para("Промокод вводят при покупке: код даёт скидку. Глагол «вводить» — ввести: «Введите промокод!» — так пишут в приложениях.", 21.5)
b.bridge("скидка descuento; цена precio; список lista; ввести промокод introducir un código promocional.")
b.ex("B1", "Completar", "Промокод", "промокод = código de descuento",
     "___ — это код со скидкой.", instr="Completar", size=20.5, gap=10)
b.ex("B1", "Completar", "список", "список покупок = lista de la compra",
     "Мой ___ покупок готов.", instr="Completar", size=20.5, gap=10)
b.ex("B1", "Opción múltiple", "A", "скидка = más barato",
     "«Скидка» значит... A. товар стоит дешевле · B. товар стоит дороже · C. товара нет", size=20.5, gap=10)
b.ex("B1", "Completar", "цены", "сравнить цены = comparar precios",
     "Сравните ___ в разных магазинах.", instr="Completar", size=20.5, gap=10)
b.end_report()

c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · КАК ССЫЛАТЬСЯ", 24)
c.para("Когда факт — не ваш, а из прессы, говорите так: «по сообщениям торговой прессы» или «торговая пресса пишет». Это честно: читатель знает, откуда факт.", 21.5)
c.para("Неуверенность — тоже по-русски: «может быть» — возможно; «может быть меньше» — возможно, будет меньше. Говорить «может быть» — признак хорошего уровня!", 21.5)
c.bridge("по сообщениям según se informa; пишет escribe; может быть quizá.")
c.ex("B2", "Completar", "По сообщениям", "по сообщениям = según se informa",
     "___ торговой прессы, скидок может быть меньше.", instr="Completar", size=20.5, gap=10)
c.ex("B2", "Completar", "может", "может быть = quizá",
     "Скидок ___ быть меньше.", instr="Completar", size=20.5, gap=10)
c.ex("B2", "Opción múltiple", "B", "может быть = quizá",
     "«Может быть» значит... A. точно да · B. возможно · C. точно нет", size=20.5, gap=10)
c.ex("B2", "Completar", "пишет", "писать → пишет",
     "Торговая пресса ___: скидок может быть меньше.", instr="Completar", size=20.5, gap=10)
c.end_report()

bx = COLX[3]
errs = [
    ("«Поздравляю с День единства!»", "→ После «с» нужен творительный падеж: «с Днём единства!»", "«с» + instrumental: с Днём единства."),
    ("«Мы едем к бабушка»", "→ После «к» — дательный падеж: «Мы едем к бабушке».", "Tras «к» va el dativo: к бабушке."),
    ("«Скидка 25 процента»", "→ После 5 и больше — «процентов»: «25 процентов».", "Desde 5: «процентов»: 25 процентов."),
    ("«Распродажа с 22 октябрь»", "→ Родительный падеж: «с 22 октября».", "Genitivo tras «с» (origen): с 22 октября."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ОШИБКИ · Clínica de errores", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "«промокод» — код со скидкой: его вводят при покупке, и цена становится ниже."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("промокод = código de descuento.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "СЛОВО · Palabra de la semana", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "промокод = código de descuento.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "«Здравствуйте! Я учу русский язык и читаю Lucerna. В среду, 4 ноября, я тоже отдохну: пойду на ярмарку с семьёй!» — М. (пример от редакции)"
disc_ru = "Настоящих писем и лучших сочинений к сроку сдачи не поступило: здесь снова пример от редакции. Обещание переносится на VOL.3."
disc_cn = "Sin cartas ni textos al cierre: ejemplo de la redacción. La promesa pasa a VOL.3."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(disc_ru, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_cn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "ПИСЬМА ЧИТАТЕЛЕЙ", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, disc_ru, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, disc_cn, 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

fy = 1770
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "ФРАЗЫ НЕДЕЛИ · Frases de la semana (textuales de esta edición)", 27, "sans", True, OLIVE)
quotes = [
    ("«Среда, 4 ноября, — выходной посреди рабочей недели»", "El miércoles 4 de noviembre es festivo en medio de la semana laboral.", "Страница 1"),
    ("«Как жить неделю с праздником посреди недели»", "¿Cómo vivir una semana con un festivo en medio?", "Страница 1"),
    ("«Во вторник, 3 ноября, рабочий день короче на час»", "El martes 3 de noviembre, la jornada es una hora más corta.", "Страница 2"),
    ("«В среду города устраивают ярмарки и концерты»", "El miércoles, las ciudades organizan ferias y conciertos.", "Страница 3"),
    ("«В воскресенье, 8 ноября, — три матча»", "El domingo 8 de noviembre hay tres partidos.", "Страница 4"),
    ("«Сначала — список: что вам правда нужно»", "Primero la lista: ¿qué necesitas de verdad?", "Страница 5"),
    ("«Многие берут отпуск в четверг и в пятницу»", "Muchos se toman vacaciones el jueves y el viernes.", "Страница 6"),
    ("«Пять дней — почти маленькие каникулы»", "¡Cinco días, casi unas minivacaciones!", "Страница 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 145
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "СЛЕДУЮЩАЯ НЕДЕЛЯ · La próxima semana (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "11 ноября — день распродажи 11.11: что купили читатели? Плюс итоги 14-го тура и ваши письма. До понедельника!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-yazyk.svg")
print("P7 saved, exercises so far:", len(REG))
