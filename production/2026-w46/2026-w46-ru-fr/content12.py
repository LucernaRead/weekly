# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ru-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · ПЕРВАЯ ПОЛОСА (A2) =================
CURPAGE[0] = 1
p = BSPage4()

p.text(MX, 92, "VOL. 3 · ТРЕТИЙ ВЫПУСК", 23, "sans", True, OLIVE)
p.text(975, 92, "КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · TEXTE EN RUSSE · EXPLICATIONS EN FRANÇAIS", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "НЕДЕЛЯ С 9 ПО 15 НОЯБРЯ 2026 ГОДА", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "РУССКАЯ ГАЗЕТА · VOL.3 · ОБЫЧНАЯ НЕДЕЛЯ · СКИДКИ · ФУТБОЛ", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "TEXTES EN RUSSE · EXPLICATIONS EN FRANÇAIS — L’ÉDITION POUR LES LECTEURS FRANCOPHONES", 20, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "ОБЫЧНАЯ НЕДЕЛЯ — И ЭТО ХОРОШО!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Пять рабочих дней, ни одного праздника. А в среду — 11.11 и День экономиста.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "Une semaine ordinaire", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "Le jour des soldes du 11 novembre · voir pages 5–6", 21, "sans", False, "#b3a06a", anchor="end")

hy = 580
p.text(MX, hy + 26, "ГЛАВНАЯ ТЕМА · À LA UNE", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Обычная неделя: пять рабочих дней", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "Ни одного выходного посреди недели: как Россия живёт первую полную неделю ноября", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "От редакции Lucerna · Уровень чтения: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Эта неделя в России — обычная. В понедельник, 9 ноября, люди идут на работу и в школу. Никаких праздников посреди недели: пять рабочих дней подряд, а потом выходные.", size=24)
f.para("Во вторник, 10 ноября, — День полиции. Это профессиональный праздник, а не выходной: полицейские в этот день работают, а мы их поздравляем.", size=24)
f.para("В среду, 11 ноября, — день распродажи 11.11: пик скидок. А ещё 11 ноября — День экономиста. Два праздника в один день — и оба без выходного!", size=24)
f.para("В четверг, 12 ноября, сборная России по футболу играет с Узбекистаном в Ташкенте. А в чемпионате — пауза: 14-й тур сыграли 6–8 ноября, а 15-й тур будет только 20 ноября.", size=24)
f.para("Как прожить обычную неделю без праздников? Об этом — весь наш номер. Приятного чтения!", size=24)
f.bridge("обычная ordinaire · подряд d’affilée · пик скидок le pic des soldes.")
f.box("НЕДЕЛЯ В ЦИФРАХ · EN CHIFFRES", [
    ("5 — рабочих дней на этой неделе: с понедельника по пятницу", "serif", False, INK, 20, 1.35),
    ("10 — ноября, вторник: День полиции(10 novembre — Jour de la police)", "serif", False, INK, 20, 1.35),
    ("11 — ноября, среда: день распродажи 11.11(le jour des soldes)", "serif", False, INK, 20, 1.35),
    ("20 — рабочих дней в ноябре всего(20 jours de travail en novembre)", "serif", False, INK, 20, 1.35),
])
f.head("СЕЙЧАС ВЫ · À VOUS", 25)
f.ex("A2", "Compléter", "9", "Lundi 9 novembre",
     "Обычная неделя начинается ___ ноября.", size=19.5, gap=6)
f.ex("A2", "Compléter", "5", "5 jours de travail dans la semaine",
     "На этой неделе ___ рабочих дней.", size=19.5, gap=6)
f.ex("A2", "Compléter", "10", "10 novembre — Jour de la police",
     "День полиции — ___ ноября.", size=19.5, gap=6)
f.ex("A2", "Compléter", "11", "11 novembre — jour des soldes",
     "День распродажи 11.11 — ___ ноября.", size=19.5, gap=6)
f.ex("A2", "Compléter", "12", "12 novembre — contre l’Ouzbékistan",
     "Сборная России играет ___ ноября.", size=19.5, gap=6)
f.ex("B1", "Compléter", "20", "15e journée le 20 novembre",
     "15-й тур чемпионата будет ___ ноября.", size=19.5, gap=6)
f.end_report()

gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "О ЧЁМ ПИШУТ", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "СМИ · LES MÉDIAS", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Главные темы недели в российских СМИ", 19, "sans", False, GREY)
topics = [
    "Обычная неделя: пять рабочих дней",
    "11.11: день скидок и посылок",
    "День полиции 10 ноября",
    "14-й тур: итоги ждём в VOL.4",
    "Сборная: матч в Ташкенте 12 ноября",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 26
p.text(gx + 22, gy + 636, "По российским СМИ, ноябрь 2026 г.", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "D’après les médias russes, novembre 2026", 19, "sans", False, GREY)

sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "В ЭТОМ НОМЕРЕ · AU SOMMAIRE", 24, "sans", True, OLIVE)
som = [
    ("Стр. 2", "День полиции 10 ноября", "A2"),
    ("Стр. 3", "Кино в ноябре", "A2→B1"),
    ("Стр. 4", "14-й тур и сборная", "B1"),
    ("Стр. 5", "День покупок 11.11", "B1"),
    ("Стр. 6", "Обычная неделя: разбор", "B2"),
    ("Стр. 7", "Фразы недели", "A2→B2"),
    ("Стр. 8", "Тест и все ответы", "все"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

my = 1636
p.text(gx, my + 24, "СЛОВО НЕДЕЛИ · LE MOT DE LA SEMAINE", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "«предзимье» — время между осенью и зимой: дождь с мокрым снегом и первые заморозки.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "предзимье = l’avant-hiver.", 19, "sans", False, GREY, gw, 1.35)

p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "autumn_path.jpg", ix, iy, iw, 320, par="xMidYMax slice")
caption(p, ix, iy + 320, iw,
        "Ноябрь в парке: листья почти облетели, скамейки пустые. Впереди — предзимье.",
        "Фото: Toxer427 — лицензия CC0 (Wikimedia Commons)")
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-snow")
f2.head("ПЕРВЫЙ СНЕГ?", 25)
f2.para("Синоптики обещали первый мокрый снег ещё 3–4 ноября. Снег, если и выпадет, быстро растает: устойчивый снежный покров ляжет только в конце ноября.", 22.5)
f2.para("А пока — дождь, туман и первые заморозки. Не забудьте тёплую одежду и зонт!", 22.5)
f2.end_report()
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "КОРОТКО · EN BREF", 24, "sans", True, OLIVE)
brefs = [
    ("ВТОРНИК", "10 ноября — День полиции. Рабочий день, не выходной."),
    ("СРЕДА", "11 ноября — 11.11: пик скидок. И День экономиста."),
    ("ЧЕТВЕРГ", "12 ноября — Узбекистан — Россия в Ташкенте."),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "БЛИЦ-ВИКТОРИНА · QUIZ ÉCLAIR", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lisez la première page et choisissez la bonne réponse · Réponses page 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "Choix", "A", "5 jours de travail dans la semaine",
      "Сколько рабочих дней на этой неделе? A. 5 · B. 4 · C. 3", size=21)
qf.ex("A2", "Choix", "B", "10 novembre — Jour de la police",
      "День полиции — это... A. 9 ноября · B. 10 ноября · C. 11 ноября", size=21)
qf.ex("A2", "Choix", "C", "11 novembre — jour des soldes",
      "День распродажи 11.11 — это... A. 9 ноября · B. 10 ноября · C. 11 ноября", size=21)
qf.ex("A2", "Choix", "A", "Jeudi contre l’Ouzbékistan",
      "Сборная России играет в четверг с... A. Узбекистаном · B. Венесуэлой · C. ЦСКА", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-pervaya.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · ЖИЗНЬ (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("ЖИЗНЬ · VIE QUOTIDIENNE", "Lucerna", "УРОВЕНЬ A2 · День полиции, День экономиста и обычная неделя · Jour de la police, Jour des économistes et une semaine ordinaire")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("10 ноября: День полиции", 37)
f.byline("От редакции Lucerna · Уровень чтения: A2")
f.para("Во вторник, 10 ноября, в России — День сотрудника органов внутренних дел. Многие по привычке называют его Днём полиции. Это профессиональный праздник: выходного в этот день нет, полицейские работают, а мы их поздравляем.")
f.para("У праздника давняя история: он отсчитывается с 1962 года, а дату выбрали не случайно — 10 ноября 1917 года было подписано постановление о создании рабочей милиции. С тех пор 10 ноября — день тех, кто охраняет порядок.")
f.para("А в среду, 11 ноября, — День экономиста. Тоже профессиональный праздник и тоже без выходного. Получается: на этой неделе два праздника — и ни одного лишнего выходного!")
f.para("В ноябре вообще 20 рабочих дней и 10 выходных. Профессиональные праздники не добавляют выходных: они просто повод сказать спасибо и поздравить.")
f.gloss("по привычке par habitude · охраняют порядок maintiennent l’ordre · повод une occasion, un prétexte.")
f.head("КАК ПОЗДРАВИТЬ?", 25)
f.para("Поздравить просто: «Поздравляю с Днём полиции!» или «Спасибо за вашу работу!» А ещё можно написать открытку или позвонить знакомым, кто работает в полиции.")
f.para("Поздравления принимают и экономисты: «Поздравляю с Днём экономиста!» — 11 ноября, в среду. Не перепутайте даты: полиция — 10 ноября, экономисты — 11 ноября.")
f.gloss("поздравляю je félicite · перепутайте ne confondez pas.")
f.end_report()

ix = COLX[3]
last = ["10 ноября — День полиции (вторник).",
        "11 ноября — День экономиста (среда).",
        "13 ноября — День войск РХБ защиты.",
        "14 ноября — День социолога.",
        "15 ноября — Всероссийский день призывника."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in last) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ПРАЗДНИКИ НЕДЕЛИ", 24, "sans", True, OLIVE)
yy3 += 52
for t in last:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "А вы? Кого вы поздравите 10 ноября? Напишите два предложения по-русски и пришлите в редакцию: лучшие мы напечатаем в VOL.4 (страница 7, «Письма читателей»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Et vous ? Qui féliciterez-vous le 10 novembre ? Écrivez deux phrases en russe à la rédaction.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "А ВЫ? · ET VOUS ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Et vous ? Qui féliciterez-vous le 10 novembre ? Écrivez deux phrases en russe à la rédaction.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

siy = ey3 + eh + 24
image(p, "snowflake.jpg", ix, siy, CW, 300)
cy2 = caption(p, ix, siy + 300, CW, "Снежинка под микроскопом: фотография Уилсона Бентли, около 1890–1920-х годов.",
              "Фото: Уилсон Бентли — общественное достояние (Wikimedia Commons)")
print("P2 snowflake ends", cy2)

dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "СЛОВА НЕДЕЛИ · LES MOTS DE LA SEMAINE", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Четыре слова о предзимье · Quatre mots sur l’avant-hiver", 20, "sans", False, GREY, anchor="end")
words = [
    ("предзимье", "время между осенью и зимой", "l’avant-hiver"),
    ("мокрый снег", "снег с дождём, он тает", "la neige mouillée"),
    ("гололедица", "лёд на дороге", "le verglas"),
    ("заморозки", "ночью мороз, днём тепло", "les gelées nocturnes"),
]
for i, (t, lab, cn) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 234, "Запомните: в предзимье бывает мокрый снег и гололедица. Синоптики советуют: не забывайте о зимних шинах и тёплой одежде.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · EXERCICES DE LA PAGE 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · Les niveaux peuvent être mélangés ; cherchez par numéro d’exercice", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.bridge("Lisez l’article de la page 2 et choisissez les bonnes réponses.")
e.ex("A2", "Choix", "A", "Le 10 novembre est un jour de travail",
     "День полиции — это... A. рабочий день · B. выходной · C. воскресенье", size=19, gap=6)
e.ex("A2", "Choix", "B", "Le Jour de la police date de 1962",
     "Праздник отсчитывается с... A. 1917 года · B. 1962 года · C. 2005 года", size=19, gap=6)
e.ex("A2", "Choix", "B", "11 novembre — Jour des économistes",
     "День экономиста — это... A. 10 ноября · B. 11 ноября · C. 12 ноября", size=19, gap=6)
e.ex("A2", "Choix", "C", "Novembre compte 20 jours de travail",
     "Сколько рабочих дней в ноябре? A. 10 · B. 15 · C. 20", size=19, gap=6)
e.ex("A2", "Choix", "B", "Les fêtes professionnelles n’ajoutent pas de jours de repos",
     "Профессиональные праздники... A. дают выходной · B. не дают выходного · C. переносят выходные", size=19, gap=6)
e.head("B · СЛОВА НЕДЕЛИ", 25)
e.bridge("Complétez avec les mots de la page 2.")
e.ex("A2", "Compléter", "предзимье", "предзимье = l’avant-hiver",
     "Сейчас ___: время между осенью и зимой.", instr="Compléter", size=19, gap=6)
e.ex("A2", "Compléter", "мокрый", "мокрый снег = la neige mouillée",
     "Синоптики обещают ___ снег.", instr="Compléter", size=19, gap=6)
e.ex("A2", "Compléter", "гололедица", "гололедица = le verglas",
     "На дорогах возможна ___.", instr="Compléter", size=19, gap=6)
e.ex("B1", "Compléter", "заморозки", "заморозки = les gelées nocturnes",
     "Ночью бывают слабые ___.", instr="Compléter", size=19, gap=6)
e.ex("B1", "Compléter", "порядок", "охранять порядок = maintenir l’ordre",
     "Полиция охраняет ___.", instr="Compléter", size=19, gap=6)
e.head("C · ЧИСЛА И ДАТЫ", 25)
e.bridge("Complétez avec les chiffres et les dates des pages 1–2.")
e.ex("A2", "Compléter", "9", "Lundi 9 novembre",
     "Неделя начинается ___ ноября.", instr="Compléter", size=19, gap=6)
e.ex("B1", "Compléter", "1917", "le décret du 10 novembre 1917",
     "Постановление о милиции подписали в ___ году.", instr="Compléter", size=19, gap=6)
e.ex("A2", "Compléter", "10", "10 jours de repos en novembre",
     "В ноябре ___ выходных и праздничных дней.", instr="Compléter", size=19, gap=6)
e.ex("B1", "Compléter", "15", "15 novembre — Jour des conscrits",
     "День призывника — ___ ноября.", instr="Compléter", size=19, gap=6)
e.head("D · ПРАЗДНИКИ НЕДЕЛИ", 25)
e.match_set("A2", "Appariement",
            ["10 ноября", "11 ноября", "13 ноября", "15 ноября"],
            ["День экономиста",
             "День войск РХБ защиты",
             "Всероссийский день призывника",
             "День полиции"],
            ["d", "a", "b", "c"],
            ["Jour de la police d", "Jour des économistes a", "Jour des troupes RCB b", "Jour des conscrits c"],
            instr="Associer")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-zhizn.svg")
print("P2 saved, exercises so far:", len(REG))
