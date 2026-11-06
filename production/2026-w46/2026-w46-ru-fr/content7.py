# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ru-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ЯЗЫК (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ЯЗЫК · LANGUE", "Lucerna", "Фокус на язык · Trois niveaux, trois sujets")

a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · СЛОВА О ПОГОДЕ", 24)
a.para("О ноябре говорим так: предзимье — время между осенью и зимой; мокрый снег — снег с дождём; гололедица — лёд на дороге. Примеры: «Сейчас предзимье», «Синоптики обещают мокрый снег».", 21.5)
a.para("Заморозки — это мороз ночью: «Ночью заморозки, а днём тепло». Тёплая одежда и зонт — лучшие друзья ноября.", 21.5)
a.bridge("предзимье l’avant-hiver ; мокрый снег la neige mouillée ; гололедица le verglas.")
a.ex("A2", "Compléter", "предзимье", "предзимье = l’avant-hiver",
     "Сейчас ___.", instr="Compléter", size=20.5, gap=10)
a.ex("A2", "Compléter", "мокрый", "мокрый снег = la neige mouillée",
     "Синоптики обещают ___ снег.", instr="Compléter", size=20.5, gap=10)
a.ex("A2", "Choix", "B", "гололедица = le verglas",
     "«Гололедица» значит... A. снег с дождём · B. лёд на дороге · C. мороз ночью", size=20.5, gap=10)
a.ex("A2", "Compléter", "заморозки", "заморозки = les gelées nocturnes",
     "Ночью бывают ___.", instr="Compléter", size=20.5, gap=10)
a.end_report()

b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · СЛОВА ПОКУПОК", 24)
b.para("Слова распродажи: посылка — товар, который прислали по почте; отследить — узнать, где посылка; вернуть — отдать товар обратно. Пример: «Посылку надо отследить и проверить».", 21.5)
b.para("Пик — самое большое число: «11 ноября — пик скидок». Промокод действует недолго: проверьте срок, пока он не закончился.", 21.5)
b.bridge("посылка un colis ; отследить suivre ; вернуть renvoyer ; пик le pic.")
b.ex("B1", "Compléter", "Посылку", "посылка = un colis",
     "___ надо отследить и проверить.", instr="Compléter", size=20.5, gap=10)
b.ex("B1", "Compléter", "вернуть", "вернуть = renvoyer",
     "Товар можно ___, если он не подошёл.", instr="Compléter", size=20.5, gap=10)
b.ex("B1", "Choix", "A", "пик = le pic",
     "«Пик скидок» значит... A. скидок больше всего · B. скидок нет · C. скидки закончились", size=20.5, gap=10)
b.ex("B1", "Compléter", "промокод", "промокод = un code promo",
     "Проверьте срок: ___ действует недолго.", instr="Compléter", size=20.5, gap=10)
b.end_report()

c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · КАК ССЫЛАТЬСЯ", 24)
c.para("Когда факт — из прогноза или прессы, говорите так: «синоптики обещают» или «по данным пресс-службы». Это честно: читатель знает, откуда факт.", 21.5)
c.para("Неуверенность — тоже по-русски: «может быть» — возможно; «снег, если и выпадет, быстро растает» — оговорка, а не обещание. Говорить «может быть» — признак хорошего уровня!", 21.5)
c.bridge("синоптики обещают les météorologues promettent ; по данным selon ; может быть peut-être.")
c.ex("B2", "Compléter", "Синоптики обещают", "синоптики обещают = les météorologues promettent",
     "___ первый мокрый снег.", instr="Compléter", size=20.5, gap=10)
c.ex("B2", "Compléter", "может", "может быть = peut-être",
     "Снег ___ быстро растаять.", instr="Compléter", size=20.5, gap=10)
c.ex("B2", "Choix", "B", "может быть = peut-être",
     "«Может быть» значит... A. точно да · B. возможно · C. точно нет", size=20.5, gap=10)
c.ex("B2", "Compléter", "данным", "по данным = selon …",
     "По ___ пресс-службы, продавцов больше 600 тысяч.", instr="Compléter", size=20.5, gap=10)
c.end_report()

bx = COLX[3]
errs = [
    ("«Поздравляю с День полиции!»", "→ После «с» нужен творительный падеж: «с Днём полиции!»", "с + instrumental : с Днём полиции."),
    ("«Я звоню бабушка»", "→ После глагола «звонить» — дательный падеж: «Я звоню бабушке».", "звонить + datif : бабушке."),
    ("«14,4 миллион заказов»", "→ После 14,4 — «миллиона»: «14,4 миллиона заказов».", "Après 14,4 : 14,4 миллиона."),
    ("«Фильм выходит с 12 ноябрь»", "→ Родительный падеж: «с 12 ноября».", "с + génitif (départ) : с 12 ноября."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ОШИБКИ · LES ERREURS", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "«посылка» — товар, который прислали по почте: её надо отследить, получить и проверить."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("посылка = un colis : il faut le suivre, le retirer et le vérifier.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "СЛОВО · LE MOT DE LA SEMAINE", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "посылка = un colis : il faut le suivre, le retirer et le vérifier.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "«Здравствуйте! Я учу русский язык и читаю Lucerna. 10 ноября я поздравлю знакомого полицейского!» — М. (пример от редакции)"
disc_ru = "Настоящих писем и лучших сочинений к сроку сдачи не поступило: здесь пример от редакции. Обещание переносится на VOL.4."
disc_cn = "Aucune lettre ni texte : exemple de la rédaction, promis pour VOL.4."
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
p.text(MX, fy + 24, "ФРАЗЫ НЕДЕЛИ · PHRASES DE LA SEMAINE (CITÉES MOT POUR MOT)", 27, "sans", True, OLIVE)
quotes = [
    ("«Эта неделя в России — обычная»", "Cette semaine en Russie est bien ordinaire.", "Страница 1"),
    ("«В среду, 11 ноября, — день распродажи 11.11: пик скидок»", "Mercredi 11 novembre, c'est le grand jour des soldes : le pic des réductions.", "Страница 1"),
    ("«Это профессиональный праздник: выходного в этот день нет, полицейские работают, а мы их поздравляем»", "C'est une fête professionnelle : pas de jour de repos, les policiers travaillent, et nous les félicitons.", "Страница 2"),
    ("«В ноябре вечера тёмные и долгие: в Москве солнце садится около половины пятого»", "Soirées de novembre sombres et longues : à Moscou, le soleil se couche vers 16 h 30.", "Страница 3"),
    ("«После этого тура — пауза: следующий, 15-й тур, будет только 20 ноября»", "Après cette journée, une pause : la prochaine, la 15e journée, n'aura lieu que le 20 novembre.", "Страница 4"),
    ("«Посылку надо отследить, получить и проверить»", "Un colis doit être suivi, retiré et vérifié.", "Страница 5"),
    ("«Такие недели — самые частые в году, и именно они задают ритм жизни»", "De telles semaines sont les plus fréquentes de l'année, et ce sont elles qui donnent le rythme de la vie.", "Страница 6"),
    ("«В ноябре 20 рабочих дней и 10 выходных»", "Novembre compte 20 jours de travail et 10 jours de repos.", "Страница 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 140
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

py = 2420
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "СЛЕДУЮЩАЯ НЕДЕЛЯ · LA SEMAINE PROCHAINE (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Полные итоги 14-го тура и результат матча Узбекистан — Россия. Плюс «Чёрная пятница» и ваши письма. До понедельника!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-yazyk.svg")
print("P7 saved, exercises so far:", len(REG))
