# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ЯЗЫК (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ЯЗЫК　LINGUA", "Lucerna", "Фокус на язык　Tre livelli, tre temi")

a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　СЛОВА О ПОГОДЕ", 24)
a.para("О ноябре говорим так: предзимье — время между осенью и зимой; мокрый снег — снег с дождём; гололедица — лёд на дороге. Примеры: «Сейчас предзимье», «Синоптики обещают мокрый снег».", 21.5)
a.para("Заморозки — это мороз ночью: «Ночью заморозки, а днём тепло». Тёплая одежда и зонт — лучшие друзья ноября.", 21.5)
a.bridge("предзимье il preinverno; мокрый снег la neve bagnata; гололедица il ghiaccio sulla strada.")
a.ex("A2", "Completare", "предзимье", "предзимье = il preinverno",
     "Сейчас ___.", instr="Completare", size=20.5, gap=10)
a.ex("A2", "Completare", "мокрый", "мокрый снег = la neve bagnata",
     "Синоптики обещают ___ снег.", instr="Completare", size=20.5, gap=10)
a.ex("A2", "Scelta multipla", "B", "гололедица = il ghiaccio sulla strada",
     "«Гололедица» значит... A. снег с дождём · B. лёд на дороге · C. мороз ночью", size=20.5, gap=10)
a.ex("A2", "Completare", "заморозки", "заморозки = le gelate notturne",
     "Ночью бывают ___.", instr="Completare", size=20.5, gap=10)
a.end_report()

b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　СЛОВА ПОКУПОК", 24)
b.para("Слова распродажи: посылка — товар, который прислали по почте; отследить — узнать, где посылка; вернуть — отдать товар обратно. Пример: «Посылку надо отследить и проверить».", 21.5)
b.para("Пик — самое большое число: «11 ноября — пик скидок». Промокод действует недолго: проверьте срок, пока он не закончился.", 21.5)
b.bridge("посылка un pacco; отследить tracciare; вернуть restituire; пик il picco.")
b.ex("B1", "Completare", "Посылку", "посылка = un pacco",
     "___ надо отследить и проверить.", instr="Completare", size=20.5, gap=10)
b.ex("B1", "Completare", "вернуть", "вернуть = restituire",
     "Товар можно ___, если он не подошёл.", instr="Completare", size=20.5, gap=10)
b.ex("B1", "Scelta multipla", "A", "пик = il picco",
     "«Пик скидок» значит... A. скидок больше всего · B. скидок нет · C. скидки закончились", size=20.5, gap=10)
b.ex("B1", "Completare", "промокод", "промокод = un codice promozionale",
     "Проверьте срок: ___ действует недолго.", instr="Completare", size=20.5, gap=10)
b.end_report()

c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　КАК ССЫЛАТЬСЯ", 24)
c.para("Когда факт — из прогноза или прессы, говорите так: «синоптики обещают» или «по данным пресс-службы». Это честно: читатель знает, откуда факт.", 21.5)
c.para("Неуверенность — тоже по-русски: «может быть» — возможно; «снег, если и выпадет, быстро растает» — оговорка, а не обещание. Говорить «может быть» — признак хорошего уровня!", 21.5)
c.bridge("синоптики обещают i meteorologi promettono; по данным secondo; может быть forse.")
c.ex("B2", "Completare", "Синоптики обещают", "синоптики обещают = i meteorologi promettono",
     "___ первый мокрый снег.", instr="Completare", size=20.5, gap=10)
c.ex("B2", "Completare", "может", "может быть = forse",
     "Снег ___ быстро растаять.", instr="Completare", size=20.5, gap=10)
c.ex("B2", "Scelta multipla", "B", "может быть = forse",
     "«Может быть» значит... A. точно да · B. возможно · C. точно нет", size=20.5, gap=10)
c.ex("B2", "Completare", "данным", "по данным = secondo …",
     "По ___ пресс-службы, продавцов больше 600 тысяч.", instr="Completare", size=20.5, gap=10)
c.end_report()

bx = COLX[3]
errs = [
    ("«Поздравляю с День полиции!»", "→ После «с» нужен творительный падеж: «с Днём полиции!»", "с + strumentale: с Днём полиции."),
    ("«Я звоню бабушка»", "→ После глагола «звонить» — дательный падеж: «Я звоню бабушке».", "звонить + dativo: бабушке."),
    ("«14,4 миллион заказов»", "→ После 14,4 — «миллиона»: «14,4 миллиона заказов».", "Dopo 14,4: 14,4 миллиона."),
    ("«Фильм выходит с 12 ноябрь»", "→ Родительный падеж: «с 12 ноября».", "с 'da' + genitivo: с 12 ноября."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ОШИБКИ　CLINICA DEGLI ERRORI", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "«посылка» — товар, который прислали по почте: её надо отследить, получить и проверить."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("посылка = un pacco: va tracciato, ritirato e controllato.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "СЛОВО　LA PAROLA", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "посылка = un pacco: va tracciato, ritirato e controllato.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "«Здравствуйте! Я учу русский язык и читаю Lucerna. 10 ноября я поздравлю знакомого полицейского!» — М. (пример от редакции)"
disc_ru = "Настоящих писем и лучших сочинений к сроку сдачи не поступило: здесь пример от редакции. Обещание переносится на VOL.4."
disc_cn = "Nessuna lettera né miglior testo: esempio della redazione; promessa per il VOL.4."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(disc_ru, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_cn, "sans", False, 20, CW - 44)) * 29 + 60
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "ПИСЬМА ЧИТАТЕЛЕЙ", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, disc_ru, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, disc_cn, 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

fy = 1816
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "ФРАЗЫ НЕДЕЛИ　FRASI DELLA SETTIMANA (CITATE ALLA LETTERA)", 27, "sans", True, OLIVE)
quotes = [
    ("«Эта неделя в России — обычная»", "Questa settimana in Russia è del tutto normale.", "Страница 1"),
    ("«В среду, 11 ноября, — день распродажи 11.11: пик скидок»", "Mercoledì 11 novembre è il grande giorno degli sconti: il picco degli sconti.", "Страница 1"),
    ("«Это профессиональный праздник: выходного в этот день нет, полицейские работают, а мы их поздравляем»", "È una festa professionale: niente giorno libero, la polizia lavora e noi ci congratuliamo con lei.", "Страница 2"),
    ("«В ноябре вечера тёмные и долгие: в Москве солнце садится около половины пятого»", "Sere di novembre buie e lunghe: a Mosca il sole tramonta verso le 16:30.", "Страница 3"),
    ("«После этого тура — пауза: следующий, 15-й тур, будет только 20 ноября»", "Dopo questo turno, una pausa: il prossimo, il 15º turno, sarà solo il 20 novembre.", "Страница 4"),
    ("«Посылку надо отследить, получить и проверить»", "Un pacco va tracciato, ritirato e controllato.", "Страница 5"),
    ("«Такие недели — самые частые в году, и именно они задают ритм жизни»", "Settimane così sono le più frequenti dell'anno, e sono proprio loro a dare il ritmo alla vita.", "Страница 6"),
    ("«В ноябре 20 рабочих дней и 10 выходных»", "Novembre ha 20 giorni lavorativi e 10 giorni liberi.", "Страница 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 140
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

py = 2420
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "СЛЕДУЮЩАЯ НЕДЕЛЯ　LA SETTIMANA PROSSIMA (VOL.4)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Полные итоги 14-го тура и результат матча Узбекистан — Россия. Плюс «Чёрная пятница» и ваши письма. До понедельника!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-yazyk.svg")
print("P7 saved, exercises so far:", len(REG))
