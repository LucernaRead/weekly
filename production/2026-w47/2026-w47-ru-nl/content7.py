# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ЯЗЫК (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ЯЗЫК　TAAL", "Lucerna", "Фокус на язык　Три уровня, три темы　Drie niveaus, drie thema's")

a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　СЛОВА О ПОГОДЕ", 24)
a.para("О ноябре говорим так: оттепель — тепло, снег тает; мокрый снег — снег с дождём; ледяной дождь — дождь, который замерзает; гололедица — лёд на дороге. Примеры: «Сейчас оттепель», «Синоптики обещают мокрый снег».", 21.5)
a.para("Гололедица опасна: «На дорогах гололедица, будьте осторожны!» Тёплая одежда и зонт — лучшие друзья ноября.", 21.5)
a.bridge("оттепель dooi; мокрый снег natte sneeuw; ледяной дождь ijzel.")
a.ex("A2", "Voltooi de zin", "оттепель", "оттепель = dooi",
     "Сейчас ___: снег тает.", instr="Voltooi de zin", size=20.5, gap=10)
a.ex("A2", "Voltooi de zin", "мокрый", "мокрый снег = natte sneeuw",
     "Синоптики обещают ___ снег.", instr="Voltooi de zin", size=20.5, gap=10)
a.ex("A2", "Meerkeuze", "B", "гололедица = gladheid op de weg",
     "«Гололедица» значит... A. снег с дождём · B. лёд на дороге · C. мороз ночью", size=20.5, gap=10)
a.ex("A2", "Voltooi de zin", "ледяной", "ледяной дождь = ijzel",
     "Идёт ___ дождь, он замерзает.", instr="Voltooi de zin", size=20.5, gap=10)
a.end_report()

b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　СЛОВА ПОКУПОК", 24)
b.para("Слова распродажи: распродажа — большая продажа со скидками; скидка — цена ниже обычной; промокод — код со скидкой. Пример: «Проверьте срок: промокод действует 4–7 дней».", 21.5)
b.para("Возврат — товар возвращают в магазин: «Если товар не подошёл, его можно вернуть». Не спешите с покупкой: сначала список, потом цены, потом промокод.", 21.5)
b.bridge("распродажа grote uitverkoop; скидка korting; промокод kortingscode; возврат retour.")
b.ex("B1", "Voltooi de zin", "распродажа", "распродажа = grote uitverkoop",
     "«Чёрная пятница» — большая ___.", instr="Voltooi de zin", size=20.5, gap=10)
b.ex("B1", "Voltooi de zin", "вернуть", "вернуть = terugsturen",
     "Товар можно ___, если он не подошёл.", instr="Voltooi de zin", size=20.5, gap=10)
b.ex("B1", "Meerkeuze", "A", "скидка = prijs lager dan normaal",
     "«Скидка» значит... A. цена ниже обычной · B. цены нет · C. скидки закончились", size=20.5, gap=10)
b.ex("B1", "Voltooi de zin", "промокод", "промокод = een kortingscode",
     "Проверьте срок: ___ действует недолго.", instr="Voltooi de zin", size=20.5, gap=10)
b.end_report()

c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　КАК ССЫЛАТЬСЯ", 24)
c.para("Когда факт — из прогноза или прессы, говорите так: «синоптики обещают» или «по данным пресс-службы». Это честно: читатель знает, откуда факт.", 21.5)
c.para("Неуверенность — тоже по-русски: «может быть» — возможно; «снег может выпасть, а может и не выпасть» — оговорка, а не обещание. Говорить «может быть» — признак хорошего уровня!", 21.5)
c.bridge("синоптики обещают de weermannen beloven; по данным volgens; может быть misschien.")
c.ex("B2", "Voltooi de zin", "Синоптики обещают", "синоптики обещают = de weermannen beloven",
     "___ дождь с мокрым снегом.", instr="Voltooi de zin", size=20.5, gap=10)
c.ex("B2", "Voltooi de zin", "может", "может быть = misschien",
     "Снег ___ выпасть, а может и не выпасть.", instr="Voltooi de zin", size=20.5, gap=10)
c.ex("B2", "Meerkeuze", "B", "может быть = misschien",
     "«Может быть» значит... A. точно да · B. возможно · C. точно нет", size=20.5, gap=10)
c.ex("B2", "Voltooi de zin", "данным", "по данным = volgens …",
     "По ___ площадки, распродажа — главная в году.", instr="Voltooi de zin", size=20.5, gap=10)
c.end_report()

# --- Pushkin image in the dead space below the A2/B1/B2 columns ---
ix7 = COLX[0]
iw7 = 2 * CW + GUT
image(p, "pushkin.jpg", ix7, 1200, iw7, 280)
cy7 = caption(p, ix7, 1200 + 280, iw7, "Александр Пушкин: портрет Ореста Кипренского, 1827 год. Пушкин — создатель современного русского литературного языка.",
              "Картина: Орест Кипренский — общественное достояние (Wikimedia Commons)")
print("P7 pushkin ends", cy7)

bx = COLX[3]
errs = [
    ("«Поздравляю с День студента!»", "→ После «с» нужен творительный падеж: «с Днём студента!»", "с + instrumentalis: с Днём студента"),
    ("«Я покупаю на чёрная пятница»", "→ После «на» — предложный падеж: «на “чёрной пятнице”».", "на + voorz.: на «чёрной пятнице»."),
    ("«В туре забили 21 голов»", "→ После 21 — «гол»: «забили 21 гол».", "Na 21, гол: забили 21 гол."),
    ("«Фильм выходит с 19 ноябрь»", "→ Родительный падеж: «с 19 ноября».", "с = vanaf: genitief — с 19 ноября."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ОШИБКИ　FOUTENKLINIEK", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "«распродажа» — большая продажа со скидками: её надо планировать, а не спешить."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("распродажа = grote uitverkoop.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "СЛОВО　WOORD VAN DE WEEK", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "распродажа = grote uitverkoop.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "«Здравствуйте! Я учу русский язык и читаю Lucerna. 17 ноября я поздравлю друга-студента с Днём студента!» — М. (пример от редакции)"
disc_ru = "Настоящих писем и лучших сочинений к сроку сдачи не поступило: здесь пример от редакции. Обещание переносится на VOL.5."
disc_cn = "Geen brieven of teksten: voorbeeld van de redactie, beloofd voor VOL.5."
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
p.text(MX, fy + 24, "ФРАЗЫ НЕДЕЛИ　ZINNEN VAN DE WEEK (LETTERLIJK UIT DIT NUMMER)", 27, "sans", True, OLIVE)
quotes = [
    ("«Все восемь матчей 14-го тура завершены»", "Alle acht wedstrijden van speelronde 14 zijn gespeeld.", "Страница 1"),
    ("«Это последний матч сборной в 2026 году»", "Dit is de laatste wedstrijd van de nationale ploeg in 2026.", "Страница 1"),
    ("«Профессиональные праздники не дают выходных»", "Beroepsfeestdagen geven geen vrije dag.", "Страница 2"),
    ("«В ноябре вечера тёмные и долгие»", "De novemberavonden zijn donker en lang.", "Страница 3"),
    ("«После паузы чемпионат возвращается 20 ноября»", "Na de pauze keert de competitie terug op 20 november.", "Страница 4"),
    ("«Умный покупатель не спешит»", "Een slimme koper haast zich niet.", "Страница 5"),
    ("«Такие недели — самые частые в году»", "Weken als deze komen het vaakst voor in het jaar.", "Страница 6"),
    ("«В ноябре 20 рабочих дней и 10 выходных»", "November heeft 20 werkdagen en 10 vrije dagen.", "Страница 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 140
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

py = 2420
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "СЛЕДУЮЩАЯ НЕДЕЛЯ　Volgende week (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Результат матча Узбекистан — Россия и матч Россия — Венесуэла. Итоги 15-го тура. День матери 29 ноября. И ваши письма. До понедельника!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-yazyk.svg")
print("P7 saved, exercises so far:", len(REG))
