# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ru-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ЯЗЫК (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ЯЗЫК · LENGUA", "Lucerna", "Фокус на язык · Tres niveles, tres temas")

a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · СЛОВА О ПОГОДЕ", 24)
a.para("О ноябре говорим так: предзимье — время между осенью и зимой; мокрый снег — снег с дождём; гололедица — лёд на дороге. Примеры: «Сейчас предзимье», «Синоптики обещают мокрый снег».", 21.5)
a.para("Заморозки — это мороз ночью: «Ночью заморозки, а днём тепло». Тёплая одежда и зонт — лучшие друзья ноября.", 21.5)
a.bridge("предзимье el preinvierno; мокрый снег la nieve húmeda; гололедица el hielo en la calzada.")
a.ex("A2", "Completar", "предзимье", "предзимье = el preinvierno",
     "Сейчас ___.", instr="Completar", size=20.5, gap=10)
a.ex("A2", "Completar", "мокрый", "мокрый снег = la nieve húmeda",
     "Синоптики обещают ___ снег.", instr="Completar", size=20.5, gap=10)
a.ex("A2", "Opción múltiple", "B", "гололедица = el hielo en la calzada",
     "«Гололедица» значит... A. снег с дождём · B. лёд на дороге · C. мороз ночью", size=20.5, gap=10)
a.ex("A2", "Completar", "заморозки", "заморозки = las heladas nocturnas",
     "Ночью бывают ___.", instr="Completar", size=20.5, gap=10)
a.end_report()

b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · СЛОВА ПОКУПОК", 24)
b.para("Слова распродажи: посылка — товар, который прислали по почте; отследить — узнать, где посылка; вернуть — отдать товар обратно. Пример: «Посылку надо отследить и проверить».", 21.5)
b.para("Пик — самое большое число: «11 ноября — пик скидок». Промокод действует недолго: проверьте срок, пока он не закончился.", 21.5)
b.bridge("посылка un paquete; отследить rastrear; вернуть devolver; пик el pico.")
b.ex("B1", "Completar", "Посылку", "посылка = un paquete",
     "___ надо отследить и проверить.", instr="Completar", size=20.5, gap=10)
b.ex("B1", "Completar", "вернуть", "вернуть = devolver",
     "Товар можно ___, если он не подошёл.", instr="Completar", size=20.5, gap=10)
b.ex("B1", "Opción múltiple", "A", "пик = el pico",
     "«Пик скидок» значит... A. скидок больше всего · B. скидок нет · C. скидки закончились", size=20.5, gap=10)
b.ex("B1", "Completar", "промокод", "промокод = un código promocional",
     "Проверьте срок: ___ действует недолго.", instr="Completar", size=20.5, gap=10)
b.end_report()

c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · КАК ССЫЛАТЬСЯ", 24)
c.para("Когда факт — из прогноза или прессы, говорите так: «синоптики обещают» или «по данным пресс-службы». Это честно: читатель знает, откуда факт.", 21.5)
c.para("Неуверенность — тоже по-русски: «может быть» — возможно; «снег, если и выпадет, быстро растает» — оговорка, а не обещание. Говорить «может быть» — признак хорошего уровня!", 21.5)
c.bridge("синоптики обещают los meteorólogos prometen; по данным según; может быть quizá.")
c.ex("B2", "Completar", "Синоптики обещают", "синоптики обещают = los meteorólogos prometen",
     "___ первый мокрый снег.", instr="Completar", size=20.5, gap=10)
c.ex("B2", "Completar", "может", "может быть = quizá",
     "Снег ___ быстро растаять.", instr="Completar", size=20.5, gap=10)
c.ex("B2", "Opción múltiple", "B", "может быть = quizá",
     "«Может быть» значит... A. точно да · B. возможно · C. точно нет", size=20.5, gap=10)
c.ex("B2", "Completar", "данным", "по данным = según …",
     "По ___ пресс-службы, продавцов больше 600 тысяч.", instr="Completar", size=20.5, gap=10)
c.end_report()

bx = COLX[3]
errs = [
    ("«Поздравляю с День полиции!»", "→ После «с» нужен творительный падеж: «с Днём полиции!»", "с + instrumental: с Днём полиции."),
    ("«Я звоню бабушка»", "→ После глагола «звонить» — дательный падеж: «Я звоню бабушке».", "звонить + dativo: бабушке."),
    ("«14,4 миллион заказов»", "→ После 14,4 — «миллиона»: «14,4 миллиона заказов».", "Tras 14,4: 14,4 миллиона."),
    ("«Фильм выходит с 12 ноябрь»", "→ Родительный падеж: «с 12 ноября».", "с 'desde' + genitivo: с 12 ноября."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ОШИБКИ · CLÍNICA DE ERRORES", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "«посылка» — товар, который прислали по почте: её надо отследить, получить и проверить."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("посылка = un paquete: hay que rastrearlo, recogerlo y revisarlo.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "СЛОВО · LA PALABRA", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "посылка = un paquete: hay que rastrearlo, recogerlo y revisarlo.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "«Здравствуйте! Я учу русский язык и читаю Lucerna. 10 ноября я поздравлю знакомого полицейского!» — М. (пример от редакции)"
disc_ru = "Настоящих писем и лучших сочинений к сроку сдачи не поступило: здесь пример от редакции. Обещание переносится на VOL.4."
disc_cn = "Sin cartas ni mejores textos: ejemplo de la redacción; promesa para el VOL.4."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(disc_ru, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_cn, "sans", False, 20, CW - 44)) * 29 + 60
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "ПИСЬМА ЧИТАТЕЛЕЙ", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, disc_ru, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, disc_cn, 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

fy = 1816
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "ФРАЗЫ НЕДЕЛИ · FRASES DE LA SEMANA (CITADAS AL PIE DE LA LETRA)", 27, "sans", True, OLIVE)
quotes = [
    ("«Эта неделя в России — обычная»", "Esta semana en Rusia es de lo más normal.", "Страница 1"),
    ("«В среду, 11 ноября, — день распродажи 11.11: пик скидок»", "El miércoles 11 de noviembre es el gran día de las rebajas: el pico de los descuentos.", "Страница 1"),
    ("«Это профессиональный праздник: выходного в этот день нет, полицейские работают, а мы их поздравляем»", "Es una fiesta profesional: no hay día libre, la policía trabaja y nosotros la felicitamos.", "Страница 2"),
    ("«В ноябре вечера тёмные и долгие: в Москве солнце садится около половины пятого»", "Tardes de noviembre oscuras y largas: en Moscú el sol se pone hacia las 16:30.", "Страница 3"),
    ("«После этого тура — пауза: следующий, 15-й тур, будет только 20 ноября»", "Tras esta jornada viene un parón: la siguiente, la jornada 15, no será hasta el 20 de noviembre.", "Страница 4"),
    ("«Посылку надо отследить, получить и проверить»", "Un paquete debe rastrearse, recogerse y revisarse.", "Страница 5"),
    ("«Такие недели — самые частые в году, и именно они задают ритм жизни»", "Semanas así son las más frecuentes del año, y son precisamente ellas las que marcan el ritmo de la vida.", "Страница 6"),
    ("«В ноябре 20 рабочих дней и 10 выходных»", "Noviembre tiene 20 días laborables y 10 días libres.", "Страница 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 140
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

py = 2420
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "СЛЕДУЮЩАЯ НЕДЕЛЯ · LA SEMANA QUE VIENE (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Полные итоги 14-го тура и результат матча Узбекистан — Россия. Плюс «Чёрная пятница» и ваши письма. До понедельника!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-yazyk.svg")
print("P7 saved, exercises so far:", len(REG))
