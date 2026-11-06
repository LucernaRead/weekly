# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-nl-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTUUR (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTUUR · КУЛЬТУРА", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · Новости Синтерклааса и «Het diner»")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Het Sinterklaasjournaal begint: aftellen naar Grave", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: A2 → B1")
f.para("Op maandag 9 november begint het Sinterklaasjournaal op NPO Zapp. Elke dag om 18:00 uur vertelt presentatrice Merel Westrik hoe de voorbereidingen gaan. Aan het einde van vorig jaar gooide Sinterklaas een fles in zee met een aanwijzing — de flessenpost werd gevonden en leidde naar Grave.")
f.para("Op zaterdag 14 november komt Sinterklaas officieel aan in Grave. Rond 12:00 uur meert de stoomboot aan bij de Maaskade, aan de Maas. Burgemeester Marieke Moorman ontvangt Sinterklaas. Het programma in Grave duurt van 12:00 tot 16:00 uur en is live te zien op NPO Zapp (NPO 3), vanaf 12:00 uur.")
f.para("Een dag later vaart Sinterklaas in Amsterdam: de boot vertrekt om 10:15 uur bij De Omval en vaart over de Amstel naar het Scheepvaartmuseum, waar hij rond 11:30 uur aankomt. Daar krijgt hij de sleutel van de stad van burgemeester Halsema en de kinderburgemeester. Om 13:00 uur begint de stoet te paard bij de Stopera, via het Rembrandtplein en de Utrechtsestraat naar het Leidseplein.")
f.para("November is ook de maand van Heel Nederland Leest: heel Nederland leest dit jaar Het diner van Herman Koch, uit 2009. Het boek is vanaf 1 november gratis af te halen in de bibliotheek, ook als je geen lid bent. Er is ook een grootletterboek, een Makkelijk Lezen-editie, een e-book en een luisterboek. In bibliotheken zijn er leeskringen — ook voor mensen die Nederlands leren.")
f.head("LEZEN EN KIJKEN", 25)
f.para("Twee feesten in één week: 's avonds om 18:00 uur het Sinterklaasjournaal kijken, en overdag een boek lezen. Neem Het diner mee naar huis en praat erover met vrienden: samen lezen is leuker dan alleen lezen.")
f.para("En wie zaterdag naar Grave kijkt op televisie, ziet de eerste intocht van dit jaar. Zondag volgt Amsterdam. Daarna begint de tijd van de schoen — en van verlanglijstjes.")
f.gloss("het journaal — новости · de flessenpost — письмо в бутылке · de burgemeester — мэр · de stoet — шествие · de leeskring — читательский кружок.")
f.end_report()

# col 3: image + facts box (sequential, measured)
ix = COLX[3]
image(p, "gracht.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Een boot in een Amsterdamse gracht. Zondag vaart de stoomboot van Sinterklaas over de Amstel naar het Scheepvaartmuseum.",
              "Foto: W. Punt / Anefo, Nationaal Archief — CC0")
facts = ["Sinterklaasjournaal: vanaf maandag 9 november, elke dag 18:00 uur, NPO Zapp.",
         "Landelijke intocht: zaterdag 14 november, Grave, Maaskade, vanaf 12:00 uur op tv.",
         "Amsterdam: zondag 15 november, boot 10:15 uur, stoet 13:00 uur, 88e editie.",
         "Heel Nederland Leest: Het diner, gratis in de bibliotheek, heel november."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 64
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SINTERKLAAS IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "OEFENINGEN · УПРАЖНЕНИЯ НА СТРАНИЦЕ 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8 · уровни смешаны; ищи свой номер", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · BEGRIJPEN", 25)
e.expl("Прочитай статью на странице 3 и выбери правильный ответ.")
e.ex("A2", "Выбор ответа", "B", "Новости Синтерклааса идут каждый день в 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 12:00 uur · B. 18:00 uur · C. 20:45 uur", size=20, gap=8)
e.ex("A2", "Выбор ответа", "B", "Национальное прибытие — в Граве",
     "De landelijke intocht is in... A. Amsterdam · B. Grave · C. Utrecht", size=20, gap=8)
e.ex("A2", "Выбор ответа", "C", "Амстердамский корабль отходит от Де Омвал в 10:15",
     "De boot in Amsterdam vertrekt om... A. 12:00 uur · B. 13:00 uur · C. 10:15 uur", size=20, gap=8)
e.ex("A2", "Выбор ответа", "A", "«Het diner» написал Герман Кох",
     "Heel Nederland Leest leest dit jaar... A. Het diner van Herman Koch · B. een boek van Merel Westrik · C. een boek over Grave", size=20, gap=8)
e.ex("A2", "Выбор ответа", "B", "«Het diner» можно бесплатно взять в библиотеке",
     "Het diner is gratis af te halen in... A. de boekwinkel · B. de bibliotheek · C. het museum", size=20, gap=8)
e.head("B · WOORDEN UIT DE TEKST", 25)
e.expl("Заполни словами из рамки.")
e.para("journaal · burgemeester · stoet · leeskring · flessenpost", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Дополнение предложения", "journaal", "journaal — новости",
     "Het Sinterklaas___ begint op 9 november.", instr="Заполните пропуск", size=20, gap=8)
e.ex("A2", "Дополнение предложения", "burgemeester", "burgemeester — мэр",
     "De ___ ontvangt Sinterklaas in Grave.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "stoet", "stoet — шествие",
     "Om 13:00 uur begint de ___ te paard.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "flessenpost", "flessenpost — письмо в бутылке",
     "De ___ leidde naar Grave.", instr="Заполните пропуск", size=20, gap=8)
e.ex("A2", "Дополнение предложения", "leeskring", "leeskring — читательский кружок",
     "In de bibliotheek is er een ___ over Het diner.", instr="Заполните пропуск", size=20, gap=8)
e.head("C · HET PERFECTUM", 25)
e.expl("Заполни в перфекте. Следи за вспомогательными глаголами hebben/zijn.")
e.ex("B1", "Дополнение предложения", "is begonnen", "beginnen требует zijn: is begonnen",
     "Het Sinterklaasjournaal ___ (beginnen) op 9 november.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "heeft gevonden", "vinden в перфекте: heeft gevonden",
     "Iemand ___ (vinden) de flessenpost.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "is aangekomen", "aankomen требует zijn: is aangekomen",
     "Sinterklaas ___ (aankomen) in Grave.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "hebben gelezen", "lezen в перфекте: hebben gelezen",
     "Veel mensen ___ (lezen) Het diner in november.", instr="Заполните пропуск", size=20, gap=8)
e.head("D · REKENEN", 25)
e.expl("Посчитай: ответь числами со страницы 3.")
e.ex("B1", "Дополнение предложения", "5", "С 9 по 14 ноября — 5 дней",
     "Van 9 tot 14 november: ___ dagen.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "6", "С 9 по 15 ноября — 6 дней",
     "Van 9 tot 15 november: ___ dagen.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "4", "Программа в Граве, 12:00–16:00, длится 4 часа",
     "Het programma in Grave duurt van 12:00 tot 16:00 uur: ___ uur.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B2", "Дополнение предложения", "17", "«Het diner» — 2009 года: 17 лет назад в 2026 году",
     "Het diner is uit 2009; in 2026 is dat ___ jaar geleden.", instr="Заполните пропуск", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultuur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · СПОРТ", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · Оранье и Лига наций")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P4-feature")
f.title("Oranje: twee wedstrijden, één doel", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: B1")
f.para("Op vrijdag 13 november speelt Oranje thuis tegen Griekenland. De wedstrijd begint om 20:45 uur in de Johan Cruijff ArenA in Amsterdam. Het is de vijfde wedstrijd in de groepsfase van de Nations League — en een beslissende: de nummers één en twee van de groep gaan naar de kwartfinales in maart 2027.")
f.para("Na vier wedstrijden staan Nederland en Griekenland samen bovenaan met 8 punten. Duitsland heeft 5 punten, Servië heeft 0 punten. Nederland staat eerste, omdat het meer doelpunten maakte: 7 tegen 5. Oranje is nog ongeslagen: 1–1 thuis tegen Duitsland, 2–1 uit bij Servië, 2–2 uit bij Griekenland en 2–1 thuis tegen Servië.")
f.para("Drie dagen later, op maandag 16 november, speelt Oranje uit tegen Duitsland in Berlijn, ook om 20:45 uur. De spelers melden zich op maandag 9 november in Zeist. Daarna is er geen interland meer tot maart: dan zijn de kwartfinales.")
f.para("De Eredivisie ligt deze week stil: het is interlandperiode. Speelronde 13 is pas op 21 en 22 november, met zaterdag NEC tegen PSV en Feyenoord tegen Excelsior, en zondag Twente tegen Willem II en Ajax tegen ADO Den Haag. Vorige week, in speelronde 11, won PSV met 7–0 van Willem II en won Ajax met 1–0 van AZ.")
f.head("DE STAND IN GROEP 2", 25)
f.para("Nederland 8 punten, Griekenland 8, Duitsland 5, Servië 0. Twee landen gaan door. Vrijdag tegen Griekenland is dus bijna een finale — en maandag in Berlijn de tweede.")
f.gloss("de groepsfase — групповой этап · de kwartfinale — четвертьфинал · ongeslagen — непобеждённый · de interland — международный матч · de stand — турнирная таблица.")
f.end_report()

# col 3: image + programme box (sequential, measured)
ix = COLX[3]
image(p, "elftal1912.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Het Nederlands elftal in 1912. Oranje speelt al meer dan honderd jaar in het oranje.",
              "Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein")
facts = ["Vrijdag 13 november, 20:45 uur: Nederland – Griekenland, Johan Cruijff ArenA.",
         "Maandag 16 november, 20:45 uur: Duitsland – Nederland, Berlijn.",
         "Stand na 4 wedstrijden: Nederland 8, Griekenland 8, Duitsland 5, Servië 0 punten.",
         "Speelronde 11: PSV – Willem II 7–0; Ajax – AZ 1–0; Feyenoord – Fortuna 1–1; Cambuur – Go Ahead Eagles 4–0."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "HET PROGRAMMA", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P4 col3 ends", sy3 + sh)

# ---- P4 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "OEFENINGEN · УПРАЖНЕНИЯ НА СТРАНИЦЕ 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8 · уровни смешаны; ищи свой номер", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · BEGRIJPEN", 25)
e.expl("Прочитай статью на странице 4 и выбери правильный ответ.")
e.ex("B1", "Выбор ответа", "B", "Нидерланды — Греция, пятница 20:45, в Амстердаме",
     "Nederland – Griekenland is op... A. maandag 16 november · B. vrijdag 13 november · C. zaterdag 14 november", size=20, gap=8)
e.ex("B1", "Выбор ответа", "C", "У Нидерландов и Греции по 8 очков",
     "Na vier wedstrijden hebben Nederland en Griekenland... A. 5 punten · B. 7 punten · C. 8 punten", size=20, gap=8)
e.ex("B1", "Выбор ответа", "A", "Нидерланды забили в группе больше голов: 7 против 5",
     "Nederland staat eerste, omdat het... A. meer doelpunten maakte · B. meer wedstrijden speelde · C. thuis speelt", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "Германия — Нидерланды, понедельник, в Берлине",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "13-й тур Эредивизи — 21–22 ноября",
     "Speelronde 13 is op... A. 13 en 14 november · B. 21 en 22 november · C. 9 en 10 november", size=20, gap=8)
e.head("B · WOORDEN UIT DE TEKST", 25)
e.expl("Заполни словами из рамки. Следи за формами глаголов.")
e.para("groepsfase · kwartfinale · ongeslagen · interland · stand", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Дополнение предложения", "groepsfase", "groepsfase — групповой этап",
     "Het is de vijfde wedstrijd in de ___.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "kwartfinales", "kwartfinale, множественное число: kwartfinales",
     "De nummers één en twee gaan naar de ___.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "ongeslagen", "ongeslagen — непобеждённый",
     "Oranje is nog ___ na vier wedstrijden.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "stand", "stand — турнирная таблица",
     "Op de ___ staat Servië onderaan met 0 punten.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "interland", "interland — международный матч",
     "Na deze week is er geen ___ meer tot maart.", instr="Заполните пропуск", size=20, gap=8)
e.head("C · VERLEDEN TIJD", 25)
e.expl("Заполни в прошедшем времени или в перфекте.")
e.ex("B1", "Дополнение предложения", "speelde", "spelen в прошедшем: speelde",
     "Oranje ___ (spelen) 1–1 tegen Duitsland.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "won", "winnen в прошедшем: won",
     "PSV ___ (winnen) met 7–0 van Willem II.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B1", "Дополнение предложения", "maakte", "maken в прошедшем: maakte",
     "Nederland ___ (maken) 7 doelpunten in vier wedstrijden.", instr="Заполните пропуск", size=20, gap=8)
e.ex("B2", "Дополнение предложения", "zijn gekomen", "komen в перфекте требует zijn",
     "De spelers ___ (komen) maandag in Zeist bij elkaar.", instr="Заполните пропуск", size=20, gap=8)
e.head("D · WAAR OF NIET WAAR?", 25)
e.ex("B1", "Верно или неверно", "Waar", "Верно: Нидерланды — Греция, пятница 20:45",
     "Nederland – Griekenland begint vrijdag om 20:45 uur. Waar of niet waar?", instr="Верно или нет?", size=20, gap=8)
e.ex("B1", "Верно или неверно", "Niet waar", "Неверно: Сербия последняя с 0 очками",
     "Servië heeft 8 punten in groep 2. Waar of niet waar?", instr="Верно или нет?", size=20, gap=8)
e.ex("B1", "Верно или неверно", "Niet waar", "Неверно: 13-й тур Эредивизи — 21–22 ноября",
     "Speelronde 13 is deze week. Waar of niet waar?", instr="Верно или нет?", size=20, gap=8)
e.ex("B1", "Верно или неверно", "Waar", "Верно: ПСВ обыграл «Виллем II» 7:0",
     "PSV won met 7–0 van Willem II. Waar of niet waar?", instr="Верно или нет?", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
