# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · TAAL (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("TAAL　ЯЗЫК", "De Lucerna", "Язык в фокусе　Drie niveaus, drie gereedschappen　Три уровня, три инструмента")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　VOETBALWOORDEN", 24)
a.para("De woorden van deze week horen bij het voetbal: de wedstrijd, de groepswinst, de kwartfinale en scoren. De wedstrijd is maandag in Berlijn: Duitsland tegen Nederland. De groepswinst is de eerste plaats in de groep.", 21.5)
a.para("En scoren: wie een doelpunt maakt, scoort. Nederland maakte 7 doelpunten in vier wedstrijden — meer dan Griekenland (5). Daarom staat Oranje bovenaan. Onthoud ook: de schoen staat klaar voor Sinterklaas.", 21.5)
a.bridge("de wedstrijd матч; de groepswinst победа в группе; de kwartfinale четвертьфинал; scoren забивать.", w=435.85)  # delta D7: width-scan band 419.8–451.9px keeps the 3 lines; mid 435.85 (line 1 measures 419.78px, inside CW 422.5)
a.ex("A2", "Дополнение предложения", "wedstrijd", "de wedstrijd = матч",
     "Duitsland – Nederland is een belangrijke ___.", instr="Заполните пропуск", size=20.5, gap=10)
a.ex("A2", "Дополнение предложения", "groepswinst", "de groepswinst = победа в группе",
     "Wie pakt de ___ in groep 2?", instr="Заполните пропуск", size=20.5, gap=10)
a.ex("A2", "Выбор ответа", "B", "Победа в группе — это первое место в группе",
     "«De groepswinst» is... A. een boek · B. de eerste plaats in de groep · C. een liedje", size=20.5, gap=10)
a.ex("A2", "Дополнение предложения", "scoorde", "Прошедшее время глагола scoren: scoorde",
     "Nederland ___ (scoren) 7 keer in vier wedstrijden.", instr="Заполните пропуск", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　DE VERLEDEN TIJD", 24)
b.para("Nederlands vertelt over het verleden met de verleden tijd: spelen wordt speelde, winnen wordt won, verliezen wordt verloor, maken wordt maakte. Voorbeeld: «PSV won met 2–5 van Cambuur.» «Feyenoord verloor met 5–3 bij Heerenveen.»", 21.5)
b.para("Let op: sommige werkwoorden zijn onregelmatig — winnen/won, verliezen/verloor. Andere zijn regelmatig: spelen/speelde, maken/maakte. Oefen met de uitslagen van deze week.", 21.5)
b.bridge("speelde играл; won выиграл; verloor проиграл; maakte забил. Прошедшее время рассказывает о том, что уже случилось.")
b.ex("B1", "Дополнение предложения", "won", "winnen в прошедшем: won",
     "PSV ___ (winnen) met 2–5 van Cambuur.", instr="Заполните пропуск", size=20.5, gap=10)
b.ex("B1", "Дополнение предложения", "verloor", "verliezen в прошедшем времени: verloor",
     "Feyenoord ___ (verliezen) met 5–3 bij Heerenveen.", instr="Заполните пропуск", size=20.5, gap=10)
b.ex("B1", "Дополнение предложения", "speelde", "spelen в прошедшем: speelde",
     "Ajax ___ (spelen) 2–2 tegen Twente.", instr="Заполните пропуск", size=20.5, gap=10)
b.ex("B1", "Выбор ответа", "B", "won — прошедшее время глагола winnen",
     "«Won» is de verleden tijd van... A. spelen · B. winnen · C. verliezen", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　BIJZINNEN MET OMDAT", 24)
c.para("Met «omdat» zeg je waarom iets gebeurt: «Oranje staat bovenaan, omdat het meer doelpunten maakte.» «Sinterklaas komt 's nachts, omdat de kinderen dan slapen.» De bijzin met «omdat» staat achteraan; het werkwoord staat dan helemaal achteraan in de bijzin.", 21.5)
c.para("Voorbeeld: «Ik zet mijn schoen, omdat ik een cadeautje wil.» «Het feest verandert, omdat mensen anders vieren.» Een omdat-zin is geen vraag — het is een reden: dit gebeurt, omdat dat.", 21.5)
c.bridge("omdat потому что; omdat het meer doelpunten maakte потому что оно забило больше голов; omdat ik een cadeautje wil потому что я хочу подарок.")
c.ex("B2", "Дополнение предложения", "omdat", "omdat = потому что",
     "Oranje staat bovenaan, ___ het meer doelpunten maakte.", instr="Заполните пропуск", size=20.5, gap=10)
c.ex("B2", "Выбор ответа", "B", "Придаточное с omdat называет причину, а не вопрос",
     "«Ik zet mijn schoen, omdat ik een cadeautje wil» is... A. een vraag · B. een reden · C. een bevel", size=20.5, gap=10)
c.ex("B2", "Дополнение предложения", "wil", "Глагол стоит в конце придаточного с omdat: wil",
     "Ik zet mijn schoen, omdat ik een cadeautje ___.", instr="Заполните пропуск", size=20.5, gap=10)
c.ex("B2", "Дополнение предложения", "maakte", "В придаточном с omdat глагол в конце",
     "Oranje staat bovenaan, omdat het meer doelpunten ___.", instr="Заполните пропуск", size=20.5, gap=10)
c.end_report()

# ---- col 3: pas op + het woord + brieven ----
bx = COLX[3]
errs = [
    ("«De Oranje speelt maandag.»", "→ Fout: Oranje is een naam, zonder lidwoord: «Oranje speelt maandag.»", "Oranje — имя собственное."),
    ("«Ik zet een schoen.»", "→ «De schoen zetten» vraagt een bezittelijk woord: «Ik zet mijn schoen.»", "mijn schoen — мой ботинок."),
    ("«PSV winnen met 2–5.»", "→ De verleden tijd van winnen is won: «PSV won met 2–5.»", "Прошедшее время winnen — won."),
    ("«Omdat het regent, ik blijf thuis.»", "→ Na de omdat-zin staat het werkwoord vooraan: «... blijf ik thuis.»", "После omdat глагол стоит первым: blijf ik thuis."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 192
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "PAS OP!　РАЗБОР ОШИБОК", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 18
wt = "«de groepswinst» betekent: de eerste plaats in de groep. Wie de groepswinst pakt, gaat als nummer één naar de kwartfinales."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("groepswinst = победа в группе: первое место в группе, победитель выходит в четвертьфинал.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "HET WOORD　СЛОВО НЕДЕЛИ", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "groepswinst = победа в группе: первое место в группе, победитель выходит в четвертьфинал.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 18
lt = "«Hallo! Ik ben Anna en ik leer Nederlands. Maandag kijk ik naar Oranje tegen Duitsland — en daarna zet ik mijn schoen!» — Anna (voorbeeldbrief van de redactie)"
dt_nl = "Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.5."
dt_zh = "Писем и лучших текстов не поступило — образец; обещание на VOL.5."
dt_zh_w = 384.3  # delta D10: width-scan band 373.2–395.4px keeps the 2 lines; mid 384.3
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(dt_nl, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(dt_zh, "sans", False, 20, dt_zh_w)) * 29 + 10 + len(wrap("Образец от редакции. Присылайте письма для VOL.5!", "sans", False, 20, CW - 44)) * 29 + 34 + 50
# +50 measured correction carried from W45 Fix-1 (rendered spacing runs above formula).
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "BRIEVEN VAN LEZERS", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, dt_nl, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, dt_zh_w, 1.42) + 10  # delta D10: dt_zh_w, see above
p.para(bx + 22, yy3 + 20, "Образец от редакции. Присылайте письма для VOL.5!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- P7 photo (W47: every page carries a public-domain image) ----
ix7, iw7 = span_x(0, 2)
image(p, "boeken.jpg", ix7, 1580, iw7, 240)
cy7 = caption(p, ix7, 1820, iw7, "Boeken in een boekwinkel. In november leest heel Nederland Het diner — gratis in de bibliotheek.",
              "Foto: Cristina Gottardi / Unsplash — CC0")
print("P7 photo ends", cy7)

# ---- zinnen van de week (verbatim from this issue) ----
fy = 1951
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "ZINNEN VAN DE WEEK　ФРАЗЫ НЕДЕЛИ (ДОСЛОВНО ИЗ ЭТОГО НОМЕРА)", 27, "sans", True, OLIVE)
quotes = [
    ("«Op maandag 16 november speelt Oranje in Berlijn tegen Duitsland»", "В понедельник, 16 ноября, Оранье играет с Германией в Берлине.", "Pagina 1"),
    ("«Na vier wedstrijden staan Nederland en Griekenland samen bovenaan met 8 punten»", "После четырёх матчей Нидерланды и Греция вместе лидируют с 8 очками.", "Pagina 1"),
    ("«Op zaterdag 5 december is het pakjesavond: de avond met de grote cadeaus»", "В субботу, 5 декабря, — Пакьесавонд: вечер больших подарков.", "Pagina 2"),
    ("«Op zaterdag 14 november kwam Sinterklaas officieel aan in Nederland»", "В субботу, 14 ноября, Синтерклаас официально прибыл в Нидерланды.", "Pagina 3"),
    ("«Nederland staat eerste, omdat het meer doelpunten maakte: 7 tegen 5»", "Нидерланды первые, потому что забили больше голов: 7 против 5.", "Pagina 4"),
    ("«Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4»", "Каждое воскресенье в 20:00 «Expeditie Robinson» идёт на RTL 4.", "Pagina 5"),
    ("«Sinterklaas is een oud feest in Nederland»", "Синтерклаас — старинный голландский праздник.", "Pagina 6"),
    ("«Een traditie leeft als mensen haar blijven vieren»", "Традиция живёт, пока люди продолжают её праздновать.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 90 + (16 if (i % 4) >= 3 else 0)
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- volgende week ----
py = 2439
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "VOLGENDE WEEK　НА СЛЕДУЮЩЕЙ НЕДЕЛЕ (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Dinsdag 24 november is er Europees voetbal: Real Madrid – PSV en Feyenoord – FC Porto. Zondag 29 november is het Feyenoord – Ajax. En zaterdag 5 december is het pakjesavond. Verder: jullie brieven en de beste teksten van pagina 8. Tot maandag!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-taal.svg")
print("P7 saved, exercises so far:", len(REG))
