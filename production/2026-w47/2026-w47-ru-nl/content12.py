# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · ПЕРВАЯ ПОЛОСА (A2) =================
CURPAGE[0] = 1
p = BSPage4()

p.text(MX, 92, "VOL. 4　ЧЕТВЁРТЫЙ ВЫПУСК", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ　TEKSTEN IN HET RUSSISCH　UITLEG IN HET NEDERLANDS", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "НЕДЕЛЯ С 16 ПО 22 НОЯБРЯ 2026 ГОДА", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "РУССКАЯ ГАЗЕТА　VOL.4　ФУТБОЛ　РАСПРОДАЖИ　КИНО", 36, "serif", True, OLIVE, anchor="middle", spacing=6)
p.text(975, 372, "ЕЖЕНЕДЕЛЬНАЯ  ГАЗЕТА  ДЛЯ  ИЗУЧАЮЩИХ  РУССКИЙ  ЯЗЫК  —  НАСТОЯЩАЯ  РОССИЯ,  ПО-РУССКИ", 16, "sans", False, GREY, anchor="middle")
# D2-kicker fix (2026-11-11, ru-zh-tw proof1 D2): the 9 single spaces in this
# kicker were double-spaced. Noto Sans CJK SC space is only 3.58px at 16px
# and neighbouring glyphs overhang their advance, so word-ink gaps were
# 1.4–2.6px (ГАЗЕТА/ДЛЯ, ИЗУЧАЮЩИХ/РУССКИЙ, НАСТОЯЩАЯ/РОССИЯ); routing the
# space to Noto Sans gains only +0.58px and reflows the whole book, so the
# data-only fix is used instead. Row widens +32.2px, stays centred on 975.
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "14-Й ТУР СЫГРАН!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "«Зенит» и «Динамо» — по 31 очку. А впереди — «чёрная пятница» и 15-й тур.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "Speelronde 14 is gespeeld", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "Speelronde 15 op 20 november　zie pagina 4", 18, "sans", False, GOOSE, anchor="end")

hy = 590
p.text(MX, hy + 26, "ГЛАВНАЯ ТЕМА　HOOFDTHEMA", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "14-й тур: «Зенит» и «Динамо» — по 31 очку", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 30, "Восемь матчей, 21 гол: как завершился 14-й тур и что будет дальше", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "От редакции Lucerna　Уровень чтения: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Все восемь матчей 14-го тура завершены: тур сыграли 6–8 ноября. «Зенит» и «Динамо» набрали по 31 очку и делят первое место в таблице. «Спартак» — третий, у него 29 очков, а у «Краснодара» и ЦСКА — по 26.", size=24)
f.para("Самый яркий матч тура — «Краснодар» — ЦСКА 4:2 в субботу, 7 ноября. А «Локомотив» проиграл «Рубину» 0:1 и оказался на 15-м месте, в зоне вылета.", size=24)
f.para("В четверг, 12 ноября, сборная России играла с Узбекистаном в Ташкенте. Честно: на момент сдачи номера, 10 ноября, результат этого матча ещё не был известен. Полный итог — в VOL.5.", size=24)
f.para("А во вторник, 17 ноября, сборная играет с Венесуэлой в Краснодаре, в 19:00. Это последний матч сборной в 2026 году. Первый матч двух сборных в истории!", size=24)
f.para("И ещё: 16 ноября на Wildberries начинается «чёрная пятница», а 20 ноября возвращается чемпионат — 15-й тур. Об этом — весь наш номер. Приятного чтения!", size=24)
f.bridge("зона вылета degradatiezone · на момент сдачи bij het ter perse gaan · в истории voor het eerst in de geschiedenis.")
f.box("ТУР В ЦИФРАХ　IN CIJFERS", [
    ("8 — матчей сыграли в 14-м туре: все восемь завершены", "serif", False, INK, 20, 1.35),
    ("21 — гол забили в туре: самый яркий матч — 4:2", "serif", False, INK, 20, 1.35),
    ("31 — очко у «Зенита» и «Динамо»: они делят 1-е место", "serif", False, INK, 20, 1.35),
    ("20 — ноября возвращается чемпионат: 15-й тур", "serif", False, INK, 20, 1.35),
])
f.head("СЕЙЧАС ВЫ　NU U", 25)
f.ex("A2", "Voltooi de zin", "8", "Speelronde 14 eindigde op 8 november",
     "14-й тур завершился ___ ноября.", size=19.5, gap=6)
f.ex("A2", "Voltooi de zin", "31", "Zenit en Dinamo hebben elk 31 punten",
     "«Зенит» и «Динамо» набрали по ___ очку.", size=19.5, gap=6)
f.ex("A2", "Voltooi de zin", "17", "17 november — tegen Venezuela",
     "Сборная играет с Венесуэлой ___ ноября.", size=19.5, gap=6)
f.ex("A2", "Voltooi de zin", "16", "Black Friday begint op 16 november",
     "«Чёрная пятница» на Wildberries — с ___ ноября.", size=19.5, gap=6)
f.ex("A2", "Voltooi de zin", "20", "Speelronde 15 op 20 november",
     "Чемпионат возвращается ___ ноября: 15-й тур.", size=19.5, gap=6)
f.ex("B1", "Voltooi de zin", "21", "21 doelpunten in speelronde 14",
     "В 14-м туре забили ___ гол.", size=19.5, gap=6)
f.end_report()

gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "О ЧЁМ ПИШУТ", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "СМИ　DE MEDIA", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Главные темы недели в российских СМИ", 19, "sans", False, GREY)
topics = [
    "14-й тур: итоги и таблица",
    "Сборная: Узбекистан и Венесуэла",
    "«Чёрная пятница»: скидки с 16 ноября",
    "Кино 19 ноября: пять премьер",
    "Погода: дождь с мокрым снегом",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 26
p.text(gx + 22, gy + 636, "По российским СМИ, ноябрь 2026 г.", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "Uit Russische media, november 2026", 19, "sans", False, GREY)

sy = 1296
p.rect(gx, sy, gw, 330, fill="#f0eee5")
p.text(gx + 22, sy + 40, "В ЭТОМ НОМЕРЕ　INHOUD", 24, "sans", True, OLIVE)
som = [
    ("Стр. 2", "Студенты и Дед Мороз", "A2"),
    ("Стр. 3", "Кино 19 ноября", "A2→B1"),
    ("Стр. 4", "14-й тур: все результаты", "B1"),
    ("Стр. 5", "«Чёрная пятница»", "B1"),
    ("Стр. 6", "Неделя 16–22 ноября", "B2"),
    ("Стр. 7", "Фразы недели", "A2→B2"),
    ("Стр. 8", "Тест и все ответы", "все"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

my = 1636
p.text(gx, my + 24, "СЛОВО НЕДЕЛИ　WOORD VAN DE WEEK", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "«чёрная пятница»", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "большая распродажа в конце ноября: скидки в магазинах и на маркетплейсах.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "чёрная пятница = Black Friday (uitverkoop).", 19, "sans", False, GREY, gw, 1.35)

p.hline(MX, RIGHT, 1856, LINE, 1.2)  # 2026-11-10: was 1844 — the rule struck through
# the descenders/CJK bottoms of the «СЛОВО НЕДЕЛИ» gloss line (ink to 1848.5;
# occlusion LINEX x3, pixel-confirmed). Gloss ends 1848.5, rule 1856, photo 1874.
iy = 1874
ix, iw = span_x(0, 2)
image(p, "autumn_path.jpg", ix, iy, iw, 320, par="xMidYMax slice")
caption(p, ix, iy + 320, iw,
        "Ноябрь в парке: листья почти облетели, скамейки пустые. До зимы — совсем немного.",
        "Фото: Toxer427 — лицензия CC0 (Wikimedia Commons)")
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-snow")
f2.head("СНЕГ БУДЕТ?", 25)
f2.para("Синоптики обещают дождь с мокрым снегом 17–19 ноября. Устойчивый снег ляжет позже, чем обычно: метеорологическая зима придёт только в двадцатые числа ноября.", 22.5)
f2.para("А пока — оттепель, лужи и ледяной дождь. Не забудьте тёплую одежду и зонт!", 22.5)
f2.end_report()
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX)
p.text(bx + 22, 1914, "КОРОТКО　KORT", 24, "sans", True, OLIVE)
brefs = [
    ("ВТОРНИК", "17 ноября — День студента. И Россия — Венесуэла в 19:00."),
    ("СРЕДА", "18 ноября — день рождения Деда Мороза."),
    ("ПЯТНИЦА", "20 ноября — возвращается чемпионат: 15-й тур."),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "БЛИЦ-ВИКТОРИНА　BLITSQUIZ", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lees pagina 1 en kies het juiste antwoord　Antwoorden op pagina 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "Meerkeuze", "A", "Zenit en Dinamo hebben elk 31 punten",
      "Сколько очков у «Зенита» и «Динамо»? A. 31 · B. 29 · C. 26", size=21)
qf.ex("A2", "Meerkeuze", "A", "Krasnodar versloeg CSKA met 4:2",
      "Как сыграли «Краснодар» и ЦСКА? A. 4:2 · B. 2:4 · C. 0:0", size=21)
qf.ex("A2", "Meerkeuze", "B", "17 november — tegen Venezuela",
      "Когда сборная играет с Венесуэлой? A. 12 ноября · B. 17 ноября · C. 20 ноября", size=21)
qf.ex("A2", "Meerkeuze", "A", "Black Friday begint op 16 november",
      "Когда начинается «чёрная пятница» на Wildberries? A. 16 ноября · B. 13 ноября · C. 27 ноября", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-pervaya.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · ЖИЗНЬ (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("ЖИЗНЬ　LEVEN", "Lucerna", "УРОВЕНЬ A2　День студента, день рождения Деда Мороза и погода　Studentendag, verjaardag van Grootvader Vorst en het weer")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Студенты и Дед Мороз: 17 и 18 ноября", 32)
f.byline("От редакции Lucerna　Уровень чтения: A2")
f.para("Во вторник, 17 ноября, — Международный день студента. Этот праздник отмечают студенты всего мира: решение о нём приняли в Праге в 1946 году. В России главный студенческий день — другой: 25 января, Татьянин день. Но 17 ноября — тоже повод поздравить студентов!")
f.para("А в среду, 18 ноября, — день рождения Деда Мороза. Праздник отмечают в Великом Устюге, на родине Деда Мороза. Там его дом, там почта Деда Мороза — и туда дети пишут письма с желаниями.")
f.para("На этой неделе есть и другие даты: 19 ноября — День преподавателя высшей школы, 20 ноября — Всемирный день ребёнка, 21 ноября — День работника налоговых органов, 22 ноября — День психолога. Профессиональные праздники не дают выходных: это рабочие дни, а праздники — повод сказать спасибо.")
f.para("А погода? Синоптики обещают дождь с мокрым снегом 17–19 ноября. Днём будет +3…+5 градусов, ночью — от −1 до +2. Солнце садится около 16:20 — вечера тёмные и короткие.")
f.gloss("поздравить feliciteren · родина geboortestreek · повод aanleiding.")
f.head("ЧТО ПОЖЕЛАТЬ?", 25)
f.para("Студенту можно пожелать: «С Днём студента! Успехов в учёбе!» А Деду Морозу дети пишут письма: «Дорогой Дед Мороз! Подари мне, пожалуйста…» — и дальше самое главное желание.")
f.para("А вы что пожелаете? Напишите два предложения по-русски: одно — студенту, одно — Деду Морозу.")
f.gloss("успехов succes · желание een wens.")
f.end_report()

ix = COLX[3]
last = ["16 ноября — День толерантности.",
        "17 ноября — День студента.",
        "18 ноября — день рождения Деда Мороза.",
        "19 ноября — День преподавателя.",
        "20 ноября — День ребёнка.",
        "21 ноября — День налоговика.",
        "22 ноября — День психолога."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in last) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ПРАЗДНИКИ НЕДЕЛИ", 24, "sans", True, OLIVE)
yy3 += 52
for t in last:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "А вы? Что вы пожелаете студенту и Деду Морозу? Напишите два предложения по-русски и пришлите в редакцию: лучшие мы напечатаем в VOL.5 (страница 7, «Письма читателей»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("En u? Schrijf twee zinnen in het Russisch naar de redactie: één voor een student, één voor Grootvader Vorst.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "А ВЫ?　EN U?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "En u? Schrijf twee zinnen in het Russisch naar de redactie: één voor een student, één voor Grootvader Vorst.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

siy = ey3 + eh + 24
image(p, "yuon_winter.jpg", ix, siy, CW, 240)
cy2 = caption(p, ix, siy + 240, CW, "«Зима. Ростов»: картина Константина Юона. Зима в городе — снег, крыши и дым из труб.",
              "Картина: Константин Юон — общественное достояние (Wikimedia Commons)")
print("P2 winter ends", cy2)

dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "СЛОВА НЕДЕЛИ　WOORDEN VAN DE WEEK", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Четыре слова о ноябрьской погоде　Vier woorden over het novemberweer", 20, "sans", False, GREY, anchor="end")
words = [
    ("оттепель", "тепло зимой: снег тает", "Dooi"),
    ("мокрый снег", "снег с дождём, он тает", "natte sneeuw"),
    ("ледяной дождь", "дождь, который замерзает", "ijzel"),
    ("гололедица", "лёд на дороге", "gladheid op de weg"),
]
for i, (t, lab, cn) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 234, "Запомните: в оттепель идёт мокрый снег и ледяной дождь, а ночью — гололедица. Синоптики советуют: не забывайте о зимних шинах и тёплой одежде.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ　OEFENINGEN BIJ PAGINA 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　Niveaus kunnen gemengd zijn; zoek op opgavenummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　ПОНИМАНИЕ", 25)
e.bridge("Lees pagina 2 en kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "De Internationale Dag van de Student is 17 november",
     "Международный день студента — это... A. 25 января · B. 17 ноября · C. 18 ноября", size=19, gap=6)
e.ex("A2", "Meerkeuze", "B", "De belangrijkste studentendag in Rusland is 25 januari",
     "Главный студенческий день в России — это... A. 17 ноября · B. 25 января · C. 18 ноября", size=19, gap=6)
e.ex("A2", "Meerkeuze", "B", "De verjaardag van Grootvader Vorst wordt gevierd in Veliki Oestjoeg",
     "День рождения Деда Мороза отмечают... A. в Москве · B. в Великом Устюге · C. в Ростове", size=19, gap=6)
e.ex("A2", "Meerkeuze", "C", "22 november — Dag van de Psycholoog",
     "День психолога — это... A. 19 ноября · B. 21 ноября · C. 22 ноября", size=19, gap=6)
e.ex("A2", "Meerkeuze", "B", "Beroepsfeestdagen voegen geen vrije dagen toe",
     "Профессиональные праздники... A. дают выходной · B. не дают выходного · C. переносят выходные", size=19, gap=6)
e.head("B　СЛОВА НЕДЕЛИ", 25)
e.bridge("Vul in met de woorden van pagina 2.")
e.ex("A2", "Voltooi de zin", "оттепель", "оттепель = dooi",
     "Сейчас ___: снег тает.", instr="Voltooi de zin", size=19, gap=6)
e.ex("A2", "Voltooi de zin", "мокрый", "мокрый снег = natte sneeuw",
     "Синоптики обещают ___ снег.", instr="Voltooi de zin", size=19, gap=6)
e.ex("A2", "Voltooi de zin", "ледяной", "ледяной дождь = ijzel",
     "Идёт ___ дождь, он замерзает.", instr="Voltooi de zin", size=19, gap=6)
e.ex("B1", "Voltooi de zin", "гололедица", "гололедица = gladheid op de weg",
     "На дорогах возможна ___.", instr="Voltooi de zin", size=19, gap=6)
e.ex("B1", "Voltooi de zin", "желании", "желание = een wens",
     "Дети пишут Деду Морозу о своём ___.", instr="Voltooi de zin", size=19, gap=6)
# D6 fix (2026-11-11): key was "желание" (nominative) — wrong: "о своём ___"
# governs the prepositional, and neuter -ие nouns take -и: о желании.
# Stem + note ("желание = 愿望", dictionary form) unchanged; cf. Q38 ноября.
e.head("C　ЧИСЛА И ДАТЫ", 25)
e.bridge("Vul in met de cijfers en data van pagina 1–2.")
e.ex("A2", "Voltooi de zin", "1946", "Het besluit werd genomen in Praag in 1946",
     "Решение о Дне студента приняли в ___ году.", instr="Voltooi de zin", size=19, gap=6)
e.ex("B1", "Voltooi de zin", "16:20", "Het wordt donker rond 16:20",
     "В Москве солнце садится около ___.", instr="Voltooi de zin", size=19, gap=6)
e.ex("A2", "Voltooi de zin", "17", "17 november — Studentendag",
     "День студента — ___ ноября.", instr="Voltooi de zin", size=19, gap=6)
e.ex("B1", "Voltooi de zin", "18", "18 november — verjaardag van Grootvader Vorst",
     "День рождения Деда Мороза — ___ ноября.", instr="Voltooi de zin", size=19, gap=6)
e.head("D　ПРАЗДНИКИ НЕДЕЛИ", 25)
e.match_set("A2", "Woorden koppelen",
            ["17 ноября", "18 ноября", "20 ноября", "22 ноября"],
            ["День психолога",
             "День студента",  # D2 fix (2026-11-11): was "Международный день студента" —
             # match_set wrap() budgets the option without the "b. " prefix, so the
             # full phrase rendered to x=1870, +8px past the 1862 content edge.
             # Shortened form (same holiday, key b unchanged); "Международный …"
             # stays verbatim in the P2 article + Q11 stem.
             "Всемирный день ребёнка",
             "день рождения Деда Мороза"],
            ["b", "d", "c", "a"],
            ["Studentendag b", "Verjaardag van Grootvader Vorst d", "Wereldkinderdag c", "Dag van de Psycholoog a"],
            instr="Koppel")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-zhizn.svg")
print("P2 saved, exercises so far:", len(REG))
