# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-nl-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · VOORPAGINA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1 · EERSTE EDITIE", 23, "sans", True, OLIVE)
p.text(975, 92, 'IN HET NEDERLANDS · ГОЛЛАНДСКИЙ, КОТОРЫЙ ЧИТАЮТ ГОЛЛАНДЦЫ', 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "WEEK VAN 19 TOT EN MET 25 OKTOBER 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "De Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, 'ГОЛЛАНДСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.1 · ЧАСЫ НАЗАД · КАНИКУЛЫ · ADE 30 ЛЕТ', 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "ТЕКСТЫ НА ГОЛЛАНДСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", 19.5, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "ZONDAG GAAT DE KLOK TERUG!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "In de nacht van zaterdag op zondag begint de wintertijd: om 03:00 uur gaat de klok één uur achteruit.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, 'В воскресенье часы — назад', 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, 'Зимнее время · см. страницу 2', 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, 'HET NIEUWS · ГЛАВНОЕ', 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Een volle week: vakantie, design, dance — en een uur extra slaap", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Van de redactie van De Lucerna · Leesniveau: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Het is een volle week in Nederland. De regio's Midden en Zuid hebben de hele week herfstvakantie: van zaterdag 17 tot en met zondag 25 oktober. De regio Noord was vorige week vrij; daar begint de school weer op maandag.", size=24)
f.para("En op de laatste vakantiedag gebeurt er iets bijzonders. In de nacht van zaterdag op zondag gaat de klok één uur achteruit: om 03:00 uur wordt het weer 02:00 uur. De wintertijd begint — en iedereen slaapt een uur langer.", size=24)
f.para("Cultuur is er ook genoeg. In Eindhoven is de Dutch Design Week: zo'n 2.500 ontwerpers tonen hun werk. En in Amsterdam danst de stad vijf dagen lang op het Amsterdam Dance Event — dertig jaar oud en groter dan ooit.", size=24)
f.para("Sportliefhebbers kijken naar zondag: PSV tegen Feyenoord om 14:30 uur en Sparta tegen Ajax om 16:45 uur. En wie zondagavond thuis blijft, kijkt misschien televisie — daarover meer op pagina 5.", size=24)
f.para("Dit is de eerste editie van De Lucerna in het Nederlands: elke week het echte Nederland, helder en eerlijk. Veel plezier met lezen!", size=24)
f.expl('Пояснение — de herfstvakantie — осенние каникулы · achteruit — назад (о часах) · de ontwerper — дизайнер.')
f.box('DE WEEK IN CIJFERS · В ЦИФРАХ', [
    ('9 — de dagen van de Dutch Design Week in Eindhoven (дней Недели дизайна в Эйндховене)', "serif", False, INK, 20, 1.35),
    ('25 — de dag in oktober waarop de wintertijd begint (день октября, когда начинается зимнее время)', "serif", False, INK, 20, 1.35),
    ('30 — de jaren van het Amsterdam Dance Event (лет фестивалю танцевальной музыки в Амстердаме)', "serif", False, INK, 20, 1.35),
    ('2.500 — de ontwerpers op de Dutch Design Week, ongeveer (примерно столько дизайнеров на Неделе дизайна)', "serif", False, INK, 20, 1.35),
])
f.head('NU JIJ · ТЕПЕРЬ ВЫ', 25)
f.ex("A2", 'Дополнение предложения', "herfstvakantie", 'herfstvakantie = осенние каникулы',
     "De regio's Midden en Zuid hebben de hele week ___.", size=19.5, gap=6)
f.ex("A2", 'Дополнение предложения', "achteruit", 'achteruit = назад (перевести часы)',
     "In de nacht van zaterdag op zondag gaat de klok één uur ___.", size=19.5, gap=6)
f.ex("A2", 'Дополнение предложения', "03:00", '03:00 → 02:00 (зимнее время)',
     "Om ___ uur wordt het weer 02:00 uur.", size=19.5, gap=6)
f.ex("A2", 'Дополнение предложения', "Eindhoven", 'Неделя дизайна — в Эйндховене',
     "De Dutch Design Week is in ___.", size=19.5, gap=6)
f.ex("A2", 'Дополнение предложения', "dertig", 'dertig = тридцать (ADE — 30 лет)',
     "Het Amsterdam Dance Event is dit jaar ___ jaar oud.", size=19.5, gap=6)
f.ex("B1", 'Дополнение предложения', "slaapt", 'slapen: iedereen → slaapt',
     "In de wintertijd ___ (slapen) iedereen een uur langer.", size=19.5, gap=6)
f.end_report()

# ---- topzoekopdrachten (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "TOPZOEK-", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "OPDRACHTEN", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, 'Что ищут в Google · zoeken op Google', 19, "sans", False, GREY)
gt = [
    ("de hanslers ruzie", "10.000+"),
    ("uitslagen champions league", "1.000+"),
    ("ade", "500+"),
    ("ballon d'or", "200+"),
    ("thuisbezorgd", "100+"),
]
byy = gy + 150
for i, (lab, vol) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 20, "serif", True, INK)
    p.text(gx + gw - 22, byy + 22, vol, 20, "sans", True, BRICK, anchor="end")
    byy += 62
p.text(gx + 22, byy + 16, "Google Trends, dinsdag 20 oktober:", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "een momentopname; de aantallen zijn", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 68, "schattingen, geen exacte tellingen.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 102, 'Снимок 20 октября: цифры — оценки', 19, "sans", False, GREY)

# ---- inhoud (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, 'IN DEZE EDITIE · В ЭТОМ НОМЕРЕ', 24, "sans", True, OLIVE)
som = [
    ("Pag. 2", "De wintertijd, stap voor stap", "A2"),
    ("Pag. 3", "Design en herfstvakantie", "A2→B1"),
    ("Pag. 4", "Voetbal: Europa en de topper", "B1"),
    ("Pag. 5", "Dance, tv en Robinson", "B1"),
    ("Pag. 6", "Waarom googelt men de klok?", "B2"),
    ("Pag. 7", "Zinnen van de week", "A2→B2"),
    ("Pag. 8", "Oefeningen en antwoorden", "alle"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- woord van de week (col 3) ----
my = 1652
p.text(gx, my + 24, "HET WOORD VAN DE WEEK", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "«de klok verzetten»: de tijd op je klok veranderen — deze week één uur achteruit.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, '«De klok verzetten» — менять время на часах.', 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1853, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "westertoren.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "De Westertoren in Amsterdam. In de nacht van zaterdag op zondag gaat elke klok in Nederland één uur terug: om 03:00 uur wordt het 02:00 uur. (Pagina 2)",
        "Foto: Wim van Rossem / Anefo, Nationaal Archief — CC0")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-tv")
f2.head("DE WEEK OP TV", 25)
f2.para("Op televisie was er ruzie bij De Hanslers, de realityserie van SBS6: de zoekopdracht «de hanslers ruzie» was dinsdag de grootste van het land.", 22.5)
f2.para("En wie zondag na de sport nog energie heeft, danst in Amsterdam: het is de laatste avond van ADE. (Pagina's 4 en 5)", 22.5)
f2.end_report()
# col 3 IN HET KORT
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, 'IN HET KORT · КОРОТКО', 24, "sans", True, OLIVE)
brefs = [
    ("DE KLOK", "Zondag wordt 03:00 uur weer 02:00 uur. Telefoons doen het zelf; de ovenklok niet. (Pagina 2)"),
    ("DE VAKANTIE", "Midden en Zuid zijn de hele week vrij. Noord gaat maandag weer naar school."),
    ("HET DESIGN", "Dutch Design Week in Eindhoven, tot en met zondag 25 oktober. (Pagina 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz bliksem ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, 'BLIKSEMQUIZ · БЛИЦ-ВИКТОРИНА', 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, 'Прочитайте первую страницу и выберите ответ · Ответы — на странице 8', 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", 'Выбор ответа', "B", 'Зимнее время начинается в ночь с субботы на воскресенье',
      "De wintertijd begint... A. op maandag · B. in de nacht van zaterdag op zondag · C. op vrijdag", size=21)
qf.ex("A2", 'Выбор ответа', "B", 'Часы переводят на час назад',
      "Om 03:00 uur gaat de klok... A. een uur vooruit · B. een uur achteruit · C. twee uur achteruit", size=21)
qf.ex("A2", 'Выбор ответа', "C", 'Неделя дизайна — в Эйндховене',
      "De Dutch Design Week is in... A. Amsterdam · B. Rotterdam · C. Eindhoven", size=21)
qf.ex("A2", 'Выбор ответа', "A", 'В воскресенье, начало в 14:30',
      "PSV – Feyenoord begint zondag om... A. 14:30 uur · B. 16:45 uur · C. 20:00 uur", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-voorpagina.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LEVEN (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band('LEVEN · ЖИЗНЬ', "De Lucerna", 'NIVEAU A2 · De wintertijd, stap voor stap · Зимнее время — шаг за шагом')

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("De wintertijd: een uur langer slapen", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: A2")
f.para("Eén keer per jaar krijgt Nederland een cadeau: een uur extra. In de nacht van zaterdag 24 op zondag 25 oktober gaat de klok één uur achteruit. Om 03:00 uur 's nachts wordt het weer 02:00 uur. De zomertijd is voorbij; de wintertijd begint.")
f.para("Hoe onthoud je de richting? Nederlanders gebruiken een ezelsbruggetje: «In het voorjaar gaat de klok vooruit, in het najaar achteruit.» Voorjaar is de lente, najaar is de herfst. Dus nu, in de herfst, gaat de klok terug.")
f.para("Niet alles gaat vanzelf. Je telefoon en je computer veranderen de tijd zelf. Maar de klok in de keuken, de wekker naast je bed en de ovenklok moet je met de hand verzetten. Vergeet ze niet: 's avonds wordt het nu vroeger donker.")
f.para("En de vakantie? De regio's Midden en Zuid hebben de hele week herfstvakantie, van zaterdag 17 tot en met zondag 25 oktober. De regio Noord had vakantie van 10 tot en met 18 oktober; daar begint de school weer op maandag 19 oktober. Let op: de data zijn adviesdata van de Rijksoverheid — scholen mogen een beetje afwijken.")
f.para("Tot slot: de nacht zelf is speciaal. Het uur van 02:00 tot 03:00 komt twee keer voor. Wie om half drie wakker wordt, weet dus niet of het de eerste of de tweede keer half drie is!")
f.para("Wordt het nu vroeger donker? Ja en nee: 's avonds is het eerder donker, maar 's ochtends is het eerder licht. De dag wordt niet korter — het licht schuift alleen een uur.")
f.para("Nederland doet dit niet alleen: in heel Europa gaat de klok in dezelfde nacht achteruit. Wie in het weekend naar Duitsland of Frankrijk reist, hoeft dus niets extra's te doen: overal is het even laat.")
f.head("ETEN BESTELLEN WORDT HELDER", 25)
f.para("Ander nieuws van dinsdag: Thuisbezorgd en Uber Eats stoppen met verborgen kosten. Wie eten bestelt, ziet voortaan vóór het betalen alle extra kosten duidelijk op het scherm. Miljoenen klanten krijgen een kortingsbon als compensatie, schrijven NU.nl en het AD.")
f.box('ZO ONTHOUD JE HET · ПАМЯТКА', [
    ("«Voorjaar vooruit, najaar achteruit.» En in de nacht van zaterdag op zondag geldt: één uur langer slapen.", "serif", False, INK, 21.5, 1.4),
])
f.gloss('het ezelsbruggetje — запоминалка · verzetten — переводить (часы) · de wekker — будильник · de kortingsbon — купон на скидку · verborgen — скрытые · de ovenklok — часы духовки.')
f.end_report()

# col 3: image + facts + en jij (sequential, measured)
ix = COLX[3]
image(p, "zakhorloge.jpg", ix, 200, CW, 272)
cy3 = caption(p, ix, 472, CW, "Een oud zakhorloge. Vroeger verzette iedereen de klok met de hand — nu doet de telefoon het meestal zelf.",
              "Foto: photo-nic.co.uk / Wikimedia Commons — CC0")
facts = ["De wintertijd begint op zondag 25 oktober om 03:00 uur; de klok gaat terug naar 02:00 uur.",
         "De herfstvakantie van Midden en Zuid duurt van 17 tot en met 25 oktober.",
         "De data van de schoolvakanties zijn adviesdata: scholen mogen afwijken."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WIST JE DAT?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Wat doe jij met een uur extra: langer slapen, lezen of sporten? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie: de mooiste komen in VOL.2 (pagina 7, «Brieven van lezers»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap('Что вы сделаете с лишним часом: выспитесь, почитаете или займётесь спортом? Напишите два предложения по-голландски и пришлите в редакцию.', "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, 'EN JIJ? · А ВЫ?', 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, 'Что вы сделаете с лишним часом: выспитесь, почитаете или займётесь спортом? Напишите два предложения по-голландски и пришлите в редакцию.', 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Hoe laat is het? 4 time boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, 'HOE LAAT IS HET? · КОТОРЫЙ ЧАС?', 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, 'De tijd zeggen als een Nederlander · Называем время по-голландски', 20, "sans", False, GREY, anchor="end")
times = [
    ("02:15", "kwart over twee", 'два часа пятнадцать'),
    ("02:30", "half drie", 'внимание: это 2:30, а не 3:30'),
    ("02:45", "kwart voor drie", 'без четверти три'),
    ("03:00", "drie uur", 'момент начала зимнего времени'),
]
for i, (t, lab, cn) in enumerate(times):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 116, t, 40, "serif", True, OLIVE)
    yy = p.para(bx + 150, dy + 92, lab, 21.5, "serif", False, INK, CW - 172, 1.36)
    p.para(bx + 150, yy + 20, cn, 19, "sans", False, GREY, CW - 172, 1.3)
p.para(MX, dy + 234, "Let op de valkuil: «half drie» is half vóór drie — dus 02:30, niet 03:30. En de nacht van de wintertijd heeft het uur van 02:00 tot 03:00 twee keer!", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, 'OEFENINGEN · УПРАЖНЕНИЯ СТРАНИЦЫ 2', 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, 'Ответы — на странице 8 · уровни перемешаны: ищите по номеру', 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · BEGRIJPEN", 25)
e.expl('Прочитайте статью на странице 2 и выберите правильный ответ.')
e.ex("A2", 'Выбор ответа', "B", 'Запоминалка: najaar achteruit (осенью — назад)',
     "De klok gaat achteruit in... A. het voorjaar · B. het najaar · C. de zomer", size=20, gap=8)
e.ex("A2", 'Выбор ответа', "B", "03:00 → 02:00",
     "Om 03:00 uur wordt het... A. 04:00 uur · B. 02:00 uur · C. 03:30 uur", size=20, gap=8)
e.ex("A2", 'Выбор ответа', "C", 'Часы духовки сами не переведутся',
     "Welke klok verandert NIET vanzelf? A. de telefoon · B. de computer · C. de ovenklok", size=20, gap=8)
e.ex("A2", 'Выбор ответа', "B", 'Регион Север в понедельник снова идёт в школу',
     "De regio Noord... A. heeft deze week vakantie · B. gaat maandag weer naar school · C. heeft vakantie tot 25 oktober", size=20, gap=8)
e.ex("A2", 'Выбор ответа', "B", 'Оба сервиса отменяют скрытые сборы',
     "Thuisbezorgd en Uber Eats... A. worden duurder · B. stoppen met verborgen kosten · C. stoppen met bezorgen", size=20, gap=8)
e.head("B · HOE LAAT?", 25)
e.expl('Напишите время по-голландски.')
e.ex("A2", 'Дополнение предложения', "kwart over twee", "kwart over twee = 2:15",
     "02:15 is ___.", instr='Заполните пропуск', size=20, gap=8)
e.ex("A2", 'Дополнение предложения', "half drie", 'half drie = 2:30 (ловушка!)',
     "02:30 is ___.", instr='Заполните пропуск', size=20, gap=8)
e.ex("A2", 'Дополнение предложения', "kwart voor drie", "kwart voor drie = 2:45",
     "02:45 is ___.", instr='Заполните пропуск', size=20, gap=8)
e.ex("A2", 'Дополнение предложения', "drie uur", "три часа ночи (drie uur 's nachts)",
     "De wintertijd begint om ___ 's nachts.", instr='Заполните пропуск', size=20, gap=8)
e.ex("B1", 'Дополнение предложения', "achteruit", "achteruit = назад (о часах)",
     "Om 03:00 uur gaat de klok één uur ___.", instr='Заполните пропуск', size=20, gap=8)
e.head("C · CIJFERS EN DATUMS", 25)
e.expl('Заполните пропуски цифрами со страниц 1 и 2.')
e.ex("A2", 'Дополнение предложения', "25", 'воскресенье, 25 октября',
     "De wintertijd begint op zondag ___ oktober.", instr='Заполните пропуск', size=20, gap=8)
e.ex("A2", 'Дополнение предложения', "17", 'начинается в субботу, 17 октября',
     "De herfstvakantie van Midden en Zuid begint op zaterdag ___ oktober.", instr='Заполните пропуск', size=20, gap=8)
e.ex("B1", 'Дополнение предложения', "9", 'с 17 по 25 октября — 9 дней',
     "De herfstvakantie van Midden en Zuid duurt ___ dagen (17 tot en met 25 oktober).", instr='Заполните пропуск', size=20, gap=8)
e.ex("B1", 'Дополнение предложения', "2.500", 'около 2.500 дизайнеров (страница 1)',
     "Op de Dutch Design Week zijn ongeveer ___ ontwerpers.", instr='Заполните пропуск', size=20, gap=8)
e.head("D · WOORDEN", 25)
e.match_set("A2", 'Сопоставление слов',
            ["de klok verzetten", "het ezelsbruggetje", "de kortingsbon", "verborgen"],
            ["een zinnetje dat helpt om iets te onthouden",
             "de tijd op een klok veranderen",
             "niet zichtbaar, verstopt",
             "een bon voor korting bij een bestelling"],
            ["b", "a", "d", "c"],
            ['verzetten = переводить часы b', 'ezelsbruggetje = запоминалка a', 'kortingsbon = купон на скидку d', 'verborgen = скрытый c'],
            instr='Сопоставьте пары слов')
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leven.svg")
print("P2 saved, exercises so far:", len(REG))
