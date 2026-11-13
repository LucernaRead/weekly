# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JONGEREN (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JONGEREN　МОЛОДЁЖЬ", "De Lucerna", "NIVEAU B1　Robinson, de surprise en het gedicht　Робинзон, подарок-сюрприз и стихотворение")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Robinson op zondag — en de surprises", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4. Negentien bekende Nederlanders en Vlamingen leven 34 dagen op een onbewoond eiland in Maleisië. Nicolette Kluijver en Edson da Graça presenteren het programma, Camille Vanuxem is de verslaggever.")
f.para("De kandidaten slapen buiten en moeten alles zelf doen: vuur maken, eten zoeken, proeven winnen. Wie een proef verliest, kan naar huis worden gestemd. Wie het langst blijft, wint de expeditie. Het seizoen begon op zondag 1 november — en elke week wordt het spel harder. Zondag 22 november is er een nieuwe aflevering.")
f.para("Zondagavond is ook de avond van de surprises: over dertien dagen is het pakjesavond, op zaterdag 5 december. Jongeren maken een surprise voor een vriend of vriendin: een cadeau in een gekke verpakking, met een gedicht erbij. Een surprise maken is ook Nederlands oefenen: schrijf het gedicht in het Nederlands.")
f.para("Een gedicht hoeft niet lang te zijn: vier regels zijn genoeg. Vertel in het gedicht wie het cadeau krijgt, waarom juist die persoon, en wat erin zit — maar verklap de surprise niet te snel. Sinterklaas leest Nederlands, zeggen kinderen — en de redactie ook.")
f.head("JONGEREN EN DE SURPRISE", 25)
f.para("Een surprise is niet alleen voor kleine kinderen. Jongeren maken surprises met een wortel voor het paard, een tekening — of een gedicht van vier regels. Klein of groot, een gedicht op papier is het begin van pakjesavond.")
f.box("ZO KIJK JE ROBINSON", [
    ("1. Kijk zondag om 20:00 uur op RTL 4 (смотреть на RTL 4, в воскресенье в 20:00)", "serif", False, INK, 21, 1.36),
    ("2. Let op de proeven: daar worden de punten verdeeld (следите за испытаниями: там разыгрываются очки)", "serif", False, INK, 21, 1.36),
    ("3. Raad met vrienden wie het langst blijft (угадайте с друзьями, кто продержится дольше всех)", "serif", False, INK, 21, 1.36),
    ("4. Schrijf daarna een gedicht voor je surprise (а потом напишите стихотворение для своего подарка-сюрприза)", "serif", False, INK, 21, 1.36),
])
f.gloss("de surprise подарок-сюрприз · het gedicht стихотворение · de verslaggever репортёр · de proef испытание · de aflevering выпуск.")
f.end_report()

# col 3: facts + en jij + photo (sequential, measured)
ix = COLX[3]
facts = ["Expeditie Robinson: 19 kandidaten; elke zondag 20:00 uur, RTL 4.",
         "34 dagen op een onbewoond eiland in Maleisië; presentatie: Nicolette Kluijver en Edson da Graça.",
         "Pakjesavond is op zaterdag 5 december — nog 13 dagen vanaf zondag 22 november."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 64
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "JONGEREN IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Kijk jij zondag naar Expeditie Robinson, of maak je liever een surprise met een gedicht? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("В воскресенье ты смотришь «Expeditie Robinson» или лучше сделаешь подарок-сюрприз с маленьким стихотворением? Напиши два предложения по-нидерландски и отправь их.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ?　А ТЫ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "В воскресенье ты смотришь «Expeditie Robinson» или лучше сделаешь подарок-сюрприз с маленьким стихотворением? Напиши два предложения по-нидерландски и отправь их.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 boxes end", ey3 + eh)
iy5 = ey3 + eh + 26
image(p, "strand.jpg", ix, iy5, CW, 250)
cy5 = caption(p, ix, iy5 + 250, CW, "Een tropische baai met palmen — net als het eiland in Maleisië waar Expeditie Robinson wordt opgenomen.",
              "Foto: Elise Iovenko / Unsplash — CC0")
print("P5 col3 ends", cy5)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　УПРАЖНЕНИЯ НА СТРАНИЦЕ 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8　Уровни смешанные; ищите свой номер", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Прочитай статью на странице 5 и выбери правильный ответ.")
e.ex("B1", "Выбор ответа", "B", "«Робинсон» идёт каждое воскресенье в 20:00 на RTL 4",
     "Expeditie Robinson is elke zondag om... A. 18:00 uur · B. 20:00 uur · C. 12:00 uur", size=20, gap=8)
e.ex("B1", "Выбор ответа", "A", "19 участников",
     "Expeditie Robinson heeft ___ kandidaten. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "Выбор ответа", "C", "Шоу снимают на необитаемом острове в Малайзии",
     "De kandidaten leven op een eiland in... A. Spanje · B. Grave · C. Maleisië", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "Участники проводят на острове 34 дня",
     "De kandidaten blijven ___ dagen op het eiland. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "Выбор ответа", "A", "В подарке-сюрпризе есть стихотворение",
     "Bij een surprise hoort... A. een gedicht · B. een boek · C. een lampion", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("Заполни словами из рамки.")
e.para("surprise · gedicht · verslaggever · proef · aflevering · kandidaat", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Дополнение предложения", "surprise", "surprise = подарок-сюрприз (de)",
     "Ik maak een ___ voor mijn vriendin.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "verslaggever", "verslaggever — репортёр (de)",
     "Camille Vanuxem is de ___ van het programma.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "proef", "proef — испытание (de)",
     "Wie een ___ verliest, kan naar huis gaan.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "gedicht", "gedicht = стихотворение (het)",
     "In vier regels schrijf ik een ___.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "aflevering", "aflevering — выпуск",
     "Zondag is er een nieuwe ___ van Robinson.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "kandidaten", "kandidaat, множественное число: kandidaten",
     "Er zijn 19 ___ op het eiland.", instr="Заполните пропуск", size=20, gap=8)
e.head("C　DE TOEKOMST MET GAAN", 25)
e.bridge("Говори о будущем с gaan + инфинитив.")
e.ex("B1", "Дополнение предложения", "gaat winnen", "gaat winnen — выиграет (только догадка)",
     "Wie ___ (winnen) Expeditie Robinson, denk je?", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "gaan kijken", "wij → gaan + инфинитив kijken",
     "Wij ___ (kijken) zondag naar de nieuwe aflevering.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "gaat maken", "zij → gaat maken",
     "Zij ___ (maken) zondag een surprise voor pakjesavond.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "gaan schrijven", "zij (множественное число) → gaan schrijven",
     "De kinderen ___ (schrijven) een gedicht van vier regels.", instr="Заполните пропуск", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "Верно или неверно", "Waar", "Верно: шоу началось 1 ноября",
     "Expeditie Robinson begon op 1 november. Waar of niet waar?", instr="Верно или нет?", size=20, gap=8)
e.ex("B1", "Верно или неверно", "Niet waar", "Неверно: шоу снимают в Малайзии",
     "Expeditie Robinson speelt in Spanje. Waar of niet waar?", instr="Верно или нет?", size=20, gap=8)
e.ex("B2", "Верно или неверно", "Niet waar", "Неверно: четырёх строк хватает",
     "Een gedicht voor een surprise moet minstens twintig regels hebben. Waar of niet waar?", instr="Верно или нет?", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jongeren.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · VERDIEPING (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERDIEPING　ГЛУБЖЕ В ТЕМУ", "De Lucerna", "NIVEAU B2　Sinterklaas: oud feest, nieuwe wensen　Синтерклаас: старый праздник, новые желания")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P6-main")
f.title("Sinterklaas: oud feest, nieuwe wensen", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B2")
f.para("Sinterklaas is een oud feest in Nederland. Kinderen zetten al meer dan honderd jaar hun schoen bij de deur. Maar het feest verandert: vroeger zat er een tekening in de schoen, nu steeds vaker een verlanglijstje — soms op papier, soms op een telefoon.")
f.para("Ook pakjesavond verandert. Vroeger kreeg je een cadeau in een doos; nu maken veel families een surprise: het cadeau zit verstopt in iets geks, met een gedicht erbij. Het gedicht is vaak het leukste van de avond — grappig, lief of een beetje plagend.")
f.para("Deskundigen zien het feest niet verdwijnen. Het Sinterklaasjournaal is elke dag om 18:00 uur op televisie en de landelijke intocht in Grave was live op NPO 3 te zien. Het feest verandert, zeggen zij — het verdwijnt niet.")
f.para("De twee weken rond Sinterklaas zijn ook anders dan vroeger. Sint-Maarten was vorige week woensdag: kinderen liepen met lampionnen langs de deuren. Nu staat de schoen klaar. Twee feesten van licht en geven, in twee weken — met twee soorten wensen: een wortel voor het paard, een lijstje voor de Sint.")
f.para("Een traditie leeft als mensen haar blijven vieren. Op straat, in de huiskamer of allebei: de schoen staat klaar als het donker wordt, en het gedicht klinkt op pakjesavond bij elk cadeau.")
f.head("VOOR OF TEGEN EEN LIJSTJE?", 25)
f.para("Voorstanders van het lijstje zeggen: zo krijgt iedereen wat hij echt wil. Tegenstanders zeggen: een verrassing is leuker dan een lijstje. De krant kiest niet: schrijf wat je wilt — maar schrijf het in het Nederlands.")
f.gloss("het verlanglijstje список желаний · de surprise подарок-сюрприз · het gedicht стихотворение · veranderen меняться · de traditie традиция.")
f.end_report()

# col 3: OEFENDATA chart + pro/contra box (sequential, measured)
ix = COLX[3]
rows = [
    ("Een wortel en een tekening", "35", 140),
    ("Een verlanglijstje", "30", 120),
    ("Een gedicht", "20", 80),
    ("Nog niets", "15", 60),
]
cap = "OEFENDATA — verzonnen cijfers om mee te oefenen, geen echte enquête. Vraag: wat zet jij in je schoen? (100 jongeren)"
capcn = "Учебные данные: выдуманные числа, только для упражнения, не настоящий опрос. Вопрос: что ты кладёшь в ботинок? (100 молодых людей)"
capcn_w = 369.3  # delta D8: width-scan band 353.1–385.5px keeps the 4 lines; mid 369.3
ch = 62 + len(rows) * 58 + 14 + len(wrap(cap, "serif", False, 19, CW - 44)) * 27 + 6 + len(wrap(capcn, "sans", False, 18.5, capcn_w)) * 26 + 18
p.rect(ix, 200, CW, ch, fill=BOX)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DE GRAFIEK　УЧЕБНЫЕ ДАННЫЕ", 22, "sans", True, OLIVE)  # fix 2026-11-12: 24 -> 22pt — boxtitle +14.1px right overflow (Newsreader wider); 22pt saves ~34.5px. Text unchanged.
yy3 += 58
for lab, val, bw in rows:
    p.text(ix + 22, yy3 + 20, lab, 19.5, "serif", True, INK)
    p.text(ix + CW - 22, yy3 + 20, val, 19.5, "sans", True, OLIVE, anchor="end")
    p.rect(ix + 22, yy3 + 30, bw, 18, fill=OLIVE)
    yy3 += 58
yy3 += 14
yy3 = p.para(ix + 22, yy3 + 19, cap, 19, "serif", False, GREY, CW - 44, 1.36)
yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, capcn_w, 1.32) + 6  # delta D8: capcn_w, see above
print("P6 chart ends", 200 + ch, "content to", yy3)
by6 = 200 + ch + 26
bt = [
    ("Voor een lijstje: zo krijgt iedereen wat hij echt wil.", "serif", False, INK, 21, 1.4),
    ("Tegen een lijstje: een verrassing is leuker dan een lijstje.", "serif", False, INK, 21, 1.4),
    ("De krant kiest niet: schrijf wat je wilt. En jij?", "serif", False, INK, 21, 1.4),
]
bh = 62 + sum(len(wrap(t, "serif", False, 21, CW - 44)) * 29.5 + 8 for t, *_ in bt) + 16 + 30
p.rect(ix, by6, CW, bh, fill="#f0eee5")
yy3 = by6 + 16
p.text(ix + 22, yy3 + 26, "VOOR OF TEGEN?　ЗА ИЛИ ПРОТИВ?", 20, "sans", True, OLIVE)  # fix 2026-11-12: 21 -> 20pt — boxtitle +9.7px right overflow on final '?' (Newsreader wider); 20pt saves ~19.4px. Text unchanged.
yy3 += 52
for t, k, b, fl, s, lh in bt:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.4) + 8
print("P6 col3 ends", by6 + bh)

# ---- P6 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　УПРАЖНЕНИЯ НА СТРАНИЦЕ 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8　Уровни смешанные; ищите свой номер", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEES DE GRAFIEK", 25)
e.bridge("Ответь по графику на странице 6 (учебные данные).")
e.ex("B2", "Дополнение предложения", "35", "35 молодых людей кладут морковь и рисунок",
     "___ van de 100 jongeren zetten een wortel en een tekening in hun schoen.", instr="Заполните пропуск", size=21.5, gap=9)
e.ex("B2", "Дополнение предложения", "30", "30 человек кладут список желаний",
     "___ jongeren zetten een verlanglijstje in hun schoen.", instr="Заполните пропуск", size=21.5, gap=9)
e.ex("B2", "Дополнение предложения", "65", "35 + 30 = 65",
     "Wortel en verlanglijstje samen: ___ jongeren.", instr="Заполните пропуск", size=21.5, gap=9)
e.ex("B2", "Дополнение предложения", "15", "15 человек пока ничего не кладут",
     "___ jongeren zetten nog niets in hun schoen.", instr="Заполните пропуск", size=21.5, gap=9)
e.ex("B2", "Дополнение предложения", "100", "На диаграмме всего 100 человек: 35+30+20+15",
     "De grafiek telt in totaal ___ jongeren.", instr="Заполните пропуск", size=21.5, gap=9)
e.head("B　BEGRIJPEN", 25)
e.bridge("Прочитай статью на странице 6 и выбери правильный ответ.")
e.ex("B2", "Выбор ответа", "B", "Раньше рисунок, теперь список желаний",
     "Vroeger zat er een tekening in de schoen; nu steeds vaker... A. een lampion · B. een verlanglijstje · C. een boek", size=21.5, gap=9)
e.ex("B2", "Выбор ответа", "B", "Surprise — подарок в странной упаковке",
     "Een surprise is een cadeau... A. in een doos van de winkel · B. verstopt in iets geks · C. zonder gedicht", size=21.5, gap=9)
e.ex("B2", "Выбор ответа", "C", "Новости Синтерклааса — каждый день в 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 12:00 uur · B. 20:00 uur · C. 18:00 uur", size=21.5, gap=9)
e.ex("B2", "Выбор ответа", "A", "Традиция живёт, пока её празднуют",
     "Een traditie leeft als... A. mensen haar blijven vieren · B. ze oud is · C. ze op televisie is", size=21.5, gap=9)
e.ex("B2", "Выбор ответа", "B", "День святого Мартина был в прошлую среду",
     "Sint-Maarten was... A. gisteren · B. vorige week woensdag · C. volgende week", size=21.5, gap=9)
e.head("C　WOORDEN", 25)
e.bridge("Заполни словами из рамки.")
e.para("verlanglijstje · surprise · gedicht · veranderen", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B2", "Дополнение предложения", "verlanglijstje", "verlanglijstje — список желаний (het)",
     "Op het ___ staan drie wensen.", instr="Заполните пропуск", size=21.5, gap=9)
e.ex("B2", "Дополнение предложения", "surprise", "surprise = подарок-сюрприз (de)",
     "Het cadeau zit verstopt in een ___.", instr="Заполните пропуск", size=21.5, gap=9)
e.ex("B2", "Дополнение предложения", "gedicht", "gedicht = стихотворение (het)",
     "Bij het cadeau hoort een ___ van vier regels.", instr="Заполните пропуск", size=21.5, gap=9)
e.ex("B2", "Дополнение предложения", "verandert", "veranderen → verandert (единственное число)",
     "Het feest ___ elk jaar een beetje.", instr="Заполните пропуск", size=21.5, gap=9)
e.head("D　MAAK DE ZINNEN", 25)
e.bridge("Поставь слова в правильном порядке, чтобы получились предложения.")
e.ex("B2", "Составление предложения", "Sinterklaas is een oud feest in Nederland.", "П + Г + Д + место",
     "sinterklaas / is / een oud feest / in nederland → ___", instr="Составление предложения", size=21.5, gap=9)
e.ex("B2", "Составление предложения", "De kinderen zetten hun schoen bij de deur.", "П + Г + Д + место",
     "de kinderen / zetten / hun schoen / bij de deur → ___", instr="Составление предложения", size=21.5, gap=9)
e.ex("B2", "Составление предложения", "Een traditie leeft als mensen haar blijven vieren.", "als в конце",
     "een traditie / leeft / als mensen haar blijven vieren → ___", instr="Составление предложения", size=21.5, gap=9)
e.ex("B2", "Составление предложения", "Het feest verandert, maar het verdwijnt niet.", "veranderen + maar + отрицание",
     "het feest / verandert / maar het verdwijnt niet → ___", instr="Составление предложения", size=21.5, gap=9)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-verdieping.svg")
print("P6 saved, exercises so far:", len(REG))
