# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · VOORPAGINA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "ELKE WEEK IN HET NEDERLANDS　EVERY WEEK　REAL DUTCH", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "WEEK VAN 2 TOT EN MET 8 NOVEMBER 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "De Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "WEEKBLAD IN HET NEDERLANDS　VOL.2　KLIMAATWEEK　SPEELRONDE 12", 36, "serif", True, OLIVE, anchor="middle", spacing=2)
p.text(975, 372, "TEXT IN DUTCH　EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "DEZE WEEK IS DE KLIMAATWEEK!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Van maandag 2 tot en met zondag 8 november doet heel Nederland mee: bomen planten, energie besparen, fietsen.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "CLIMATE WEEK", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "The whole country joins in　see page 2", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "HET NIEUWS　TOP STORY", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Nederland in de Klimaatweek: bomen, musea en voetbal", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Van de redactie van De Lucerna　Leesniveau: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland. Gemeenten in het hele land organiseren acties: bomen planten, energie besparen, de fiets nemen in plaats van de auto. Iedereen kan meedoen.", size=23)
f.para("In Coevorden, in Drenthe, deelt de gemeente op zaterdag 7 november 200 biologisch geteelde bomen en struiken uit. De herfst is de beste tijd om te planten, zeggen de organisatoren: de grond is nog zacht en de jonge boom kan rustig wortelen.", size=23)
f.para("Het weer hoort bij deze week: de waarschuwingen van het KNMI zijn tegenwoordig lokaal — voor jouw eigen omgeving, niet voor een hele provincie. De codes zijn geel, oranje en rood (pagina 2 en 6).", size=23)
f.para("Cultuur is er ook: zaterdagavond 7 november is het Museumnacht in Amsterdam (meer dan 70 musea open tot 02:00 uur) en in Den Haag is het Crossing Border Festival, van dinsdag tot en met zondag.", size=23)
f.para("Sport: speelronde 12 van de Eredivisie, met zondag Heerenveen tegen Feyenoord (11:15 uur) en Twente tegen Ajax (13:30 uur). En wie zondagavond thuis blijft, kijkt misschien naar Expeditie Robinson (pagina 5).", size=23)
f.bridge("Note | de Klimaatweek = Climate Week · de boom planten = to plant a tree · besparen = to save · de waarschuwing = warning.")
f.box("DE WEEK IN CIJFERS　IN NUMBERS", [
    ("7 — de dagen van de Klimaatweek (the days of the Climate Week)", "serif", False, INK, 20, 1.35),
    ("200 — de bomen en struiken die Coevorden zaterdag uitdeelt (the trees and shrubs Coevorden gives away on Saturday)", "serif", False, INK, 20, 1.35),
    ("70+ — de musea die open zijn op Museumnacht (the museums open on Museum Night, 70+)", "serif", False, INK, 20, 1.35),
    ("9 — de wedstrijden van speelronde 12 in de Eredivisie (the matches of Eredivisie matchday 12)", "serif", False, INK, 20, 1.35),
])
f.head("NU JIJ　YOUR TURN", 25)
f.ex("A2", "complete", "8", "The Climate Week runs 2–8 November",
     "De Klimaatweek duurt van maandag 2 tot en met zondag ___ november.", size=19.5, gap=6)
f.ex("A2", "complete", "200", "Coevorden gives away 200 trees and shrubs",
     "Coevorden deelt op zaterdag ___ bomen en struiken uit.", size=19.5, gap=6)
f.ex("A2", "complete", "7", "Museum Night is on Saturday 7 November",
     "Museumnacht is op zaterdag ___ november.", size=19.5, gap=6)
f.ex("A2", "complete", "11:15", "Heerenveen–Feyenoord kicks off at 11:15",
     "Heerenveen – Feyenoord begint zondag om ___ uur.", size=19.5, gap=6)
f.ex("A2", "complete", "13:30", "Twente–Ajax kicks off at 13:30",
     "Twente – Ajax begint zondag om ___ uur.", size=19.5, gap=6)
f.ex("B1", "complete", "planten", "Plural subject, so planten",
     "In de Klimaatweek ___ (planten) veel mensen een boom.", size=19.5, gap=6)
f.end_report()

# ---- deze week agenda (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "DEZE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "　THIS WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Agenda van de week　THIS WEEK'S EVENTS", 19, "sans", False, GREY)
gt = [
    ("MA 2", "Klimaatweek begint"),
    ("DI 3", "Crossing Border, Den Haag"),
    ("ZA 7", "Museumnacht Amsterdam"),
    ("ZA 7", "200 bomen in Coevorden"),
    ("ZO 8", "Twente – Ajax, 13:30 uur"),
]
byy = gy + 150
for i, (lab, vol) in enumerate(gt):
    p.text(gx + 22, byy + 22, lab, 20, "serif", True, OLIVE)
    p.text(gx + 110, byy + 22, vol, 20, "serif", False, INK)
    byy += 62
p.text(gx + 22, byy + 16, "Alle data en tijden staan ook", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "in de artikelen op pagina 2–4.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "See the articles on pages 2–4", 19, "sans", False, GREY)
p.text(gx + 22, byy + 102, "for all dates and times.", 19, "sans", False, GREY)

# ---- inhoud (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "IN DEZE EDITIE　IN THIS ISSUE", 24, "sans", True, OLIVE)
som = [
    ("Pag. 2", "Klimaatweek, stap voor stap", "A2"),
    ("Pag. 3", "Musea bij nacht en boeken", "A2→B1"),
    ("Pag. 4", "Voetbal: Europa, ronde 12", "B1"),
    ("Pag. 5", "Robinson, ADE, DDW voorbij", "B1"),
    ("Pag. 6", "De codes van het KNMI", "B2"),
    ("Pag. 7", "Woorden van de week", "A2→B2"),
    ("Pag. 8", "Oefeningen en antwoorden", "alle"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- woord van de week (col 3) ----
my = 1652
p.text(gx, my + 24, "HET WOORD VAN DE WEEK", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "«het klimaat»", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 104, "het weer en de natuur om ons heen, over een lange tijd. De Klimaatweek gaat over ons klimaat.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy, "«Climate»: the weather and nature around us, long-term. Climate Week is about our climate.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1853, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "herfstbos.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Een herfstbos in november. De herfst is de beste tijd om een boom te planten: de grond is nog zacht en de jonge boom kan rustig wortelen. (Pagina 2)",
        "Foto: Vovogov90 — CC0")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-extra")
f2.head("NOG MEER DEZE WEEK", 25)
f2.para("PAN Amsterdam (kunst en antiek, RAI) loopt nog tot en met zondag 8 november. En in Zaandam is op 7 en 8 november de Mega Snuffelmarkt, met zo'n 250 kramen.", 22.5)
f2.para("Tweedehands kopen is klimaatvriendelijk: wat al bestaat, hoeft niet opnieuw gemaakt te worden.", 22.5)
f2.end_report()
# col 3 IN HET KORT
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX)
p.text(bx + 22, 1914, "IN HET KORT　IN BRIEF", 24, "sans", True, OLIVE)
brefs = [
    ("DE KLIMAATWEEK · P.2", "2–8 november. Coevorden deelt zaterdag 200 bomen uit."),
    ("DE MUSEA · P.3", "Zaterdagavond Museumnacht: 70+ musea open tot 02:00 uur."),
    ("HET VOETBAL · P.4", "Zondag: Twente – Ajax 13:30, Heerenveen – Feyenoord 11:15."),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz bliksem ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "BLIKSEMQUIZ　LIGHTNING QUIZ", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Read page 1, choose the right answer　answers on page 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "choice", "B", "The Climate Week lasts 7 days (2–8 November)",
      "De Klimaatweek duurt... A. 5 dagen · B. 7 dagen · C. 9 dagen", size=21)
qf.ex("A2", "choice", "B", "Coevorden gives away 200 trees and shrubs",
      "Coevorden deelt zaterdag uit... A. 100 bomen · B. 200 bomen en struiken · C. 70 musea", size=21)
qf.ex("A2", "choice", "C", "Museum Night is in Amsterdam",
      "Museumnacht is in... A. Rotterdam · B. Den Haag · C. Amsterdam", size=21)
qf.ex("A2", "choice", "B", "Twente–Ajax kicks off at 13:30",
      "Twente – Ajax begint zondag om... A. 11:15 uur · B. 13:30 uur · C. 15:45 uur", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-voorpagina.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LEVEN (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LEVEN　LIFE", "De Lucerna", "NIVEAU A2　De Klimaatweek, stap voor stap　The Climate Week, step by step")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("De Klimaatweek: wat kun jij doen?", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2")
f.para("De Klimaatweek is een week waarin heel Nederland nadenkt over het klimaat: het weer, de natuur en de energie die wij gebruiken. Gemeenten, scholen en bedrijven organiseren acties. Iedereen kan meedoen — ook jij.")
f.para("De makkelijkste actie is een boom planten. In de herfst is de grond nog zacht en kan een jonge boom goed wortelen. In Coevorden deelt de gemeente op zaterdag 7 november 200 biologisch geteelde bomen en struiken uit, van 13:00 tot 16:00 uur, op de Fair Groen Coevorden in Zweeloo.")
f.para("Een tweede actie is energie besparen: korter douchen, de verwarming één graad lager zetten, de fiets nemen in plaats van de auto. Kleine stappen, zeggen de organisatoren, maar samen maken ze een groot verschil.")
f.para("En het weer zelf? Het KNMI waarschuwt met kleuren: geel, oranje en rood. Geel betekent: let op, het weer kan gevaarlijk zijn. Oranje: het is gevaarlijk, bereid je voor. Rood: het is zeer gevaarlijk, blijf liever binnen. De waarschuwingen zijn tegenwoordig lokaal: ze gelden voor jouw eigen omgeving, niet voor een hele provincie.")
f.para("Wat doe jij deze week? Plant een boom, spaar energie of ga met de fiets naar school. En praat erover met je vrienden: het klimaat is van ons allemaal.")
f.head("DRIE ACTIES VOOR DEZE WEEK", 25)
f.para("Eén: plant iets groens, al is het maar een struik op je balkon. Twee: bespaar energie, bijvoorbeeld met de verwarming één graad lager. Drie: neem de fiets voor korte ritten — gezond voor jou en goed voor de lucht.")
f.box("ZO ONTHOUD JE HET　REMEMBER", [
    ("«Geel is let op, oranje is gevaarlijk, rood is blijf binnen.» En de waarschuwing geldt voor jouw eigen omgeving.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("het klimaat = climate · wortelen = to take root · besparen = to save · de verwarming = heating · de waarschuwing = warning · lokaal = local.")
f.end_report()

# col 3: image + facts + en jij (sequential, measured)
ix = COLX[3]
image(p, "kinderdijk.jpg", ix, 200, CW, 272)
cy3 = caption(p, ix, 472, CW, "Molens bij Kinderdijk. Wind is al eeuwen een Nederlandse energiebron — nu draaien er ook moderne windmolens op zee.",
              "Foto: Nationaal Archief — CC0")
facts = ["De Klimaatweek duurt van maandag 2 tot en met zondag 8 november.",
         "Coevorden deelt zaterdag 7 november 200 bomen en struiken uit (13:00–16:00 uur, Zweeloo).",
         "Code geel = let op · oranje = gevaarlijk · rood = zeer gevaarlijk, blijf binnen."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 40
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WIST JE DAT?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Wat doe jij in de Klimaatweek: een boom planten, energie besparen of fietsen? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie: de mooiste komen in VOL.3 (pagina 7, «Brieven van lezers»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("What do you do in the Climate Week: plant a tree, save energy or cycle? Write two sentences in Dutch and send them to the editors.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ?　AND YOU?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "What do you do in the Climate Week: plant a tree, save energy or cycle? Write two sentences in Dutch and send them to the editors.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- codes row: 4 boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "DE CODES VAN HET KNMI　KNMI CODES", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "What does each colour mean?", 20, "sans", False, GREY, anchor="end")
codes = [
    ("GEEL", "let op", "The weather may be dangerous: take care"),
    ("ORANJE", "gevaarlijk", "Dangerous: be prepared"),
    ("ROOD", "blijf binnen", "Very dangerous: stay indoors if you can"),
    ("LOKAAL", "jouw omgeving", "The warning is for your own area"),
]
for i, (t, lab, cn) in enumerate(codes):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 116, t, 40, "serif", True, OLIVE)
    yy = p.para(bx + 216, dy + 92, lab, 21.5, "serif", False, INK, CW - 238, 1.36)
    p.para(bx + 216, yy + 20, cn, 19, "sans", False, GREY, CW - 238, 1.3)
p.para(MX, dy + 234, "Let op: een waarschuwing is geen voorspelling voor het hele land — kijk altijd naar jouw eigen plaats. Meer over de codes lees je op pagina 6.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　EXERCISES ON PAGE 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8　levels are mixed; find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　BEGRIJPEN", 25, gap=8)
e.bridge("Read the article on page 2 and choose the right answer.")
e.ex("A2", "choice", "C", "Not a Climate Week action: driving more",
     "Wat doe je in de Klimaatweek NIET? A. een boom planten · B. energie besparen · C. meer autorijden", size=20, gap=4)
e.ex("A2", "choice", "B", "Coevorden gives away 200 trees and shrubs",
     "Coevorden deelt uit... A. 100 bomen · B. 200 bomen en struiken · C. 200 fietsen", size=20, gap=4)
e.ex("A2", "choice", "C", "Code red: very dangerous, stay indoors",
     "Code rood betekent... A. let op · B. gevaarlijk · C. zeer gevaarlijk, blijf binnen", size=20, gap=4)
e.ex("A2", "choice", "B", "Warnings are local, not for a whole province",
     "De waarschuwingen van het KNMI zijn tegenwoordig... A. voor het hele land · B. lokaal, voor je eigen omgeving · C. alleen voor de kust", size=20, gap=4)
e.ex("A2", "choice", "B", "Saving energy: turning the heating down one degree",
     "Energie besparen is... A. langer douchen · B. de verwarming lager zetten · C. meer autorijden", size=20, gap=4)
e.head("B　ACTIES", 25, gap=8)
e.bridge("Fill in with words from page 2.")
e.ex("A2", "complete", "7", "The Climate Week, 2–8 November, lasts 7 days",
     "De Klimaatweek duurt ___ dagen.", instr="Fill in", size=20, gap=4)
e.ex("A2", "complete", "wortelen", "wortelen = to take root (plural subject)",
     "In de herfst ___ (wortelen) de jonge bomen goed.", instr="Fill in", size=20, gap=4)
e.ex("A2", "complete", "besparen", "besparen = to save",
     "Met korter douchen kun je energie ___.", instr="Fill in", size=20, gap=4)
e.ex("A2", "complete", "fiets", "fiets = bicycle",
     "Veel mensen nemen de ___ in plaats van de auto.", instr="Fill in", size=20, gap=4)
e.ex("A2", "complete", "Zweeloo", "The giveaway place is Zweeloo",
     "De bomen in Coevorden worden uitgedeeld in ___.", instr="Fill in", size=20, gap=4)
e.head("C　CODES EN DATUMS", 25, gap=8)
e.bridge("Fill in the colour codes and dates.")
e.ex("A2", "complete", "geel", "Code yellow: take care",
     "Code ___ betekent: let op.", instr="Fill in", size=20, gap=4)
e.ex("A2", "complete", "oranje", "Code orange: dangerous",
     "Code ___ betekent: gevaarlijk, bereid je voor.", instr="Fill in", size=20, gap=4)
e.ex("A2", "complete", "13:00", "The giveaway starts at 13:00",
     "De uitdeling in Coevorden begint om ___ uur.", instr="Fill in", size=20, gap=4)
e.ex("A2", "complete", "8", "The Climate Week ends on Sunday 8 November",
     "De Klimaatweek eindigt op zondag ___ november.", instr="Fill in", size=20, gap=4)
e.head("D　WOORDEN", 25, gap=8)
e.match_set("A2", "matching",
            ["de Klimaatweek", "besparen", "de waarschuwing", "lokaal"],
            ["een bericht dat zegt: let op, gevaarlijk weer",
             "een week vol acties voor het klimaat",
             "voor je eigen omgeving, niet overal",
             "minder energie gebruiken"],
            ["b", "d", "a", "c"],
            ["Klimaatweek = Climate Week b", "besparen = to save d", "waarschuwing = warning a", "lokaal = local c"],
            instr="Match word to meaning")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leven.svg")
print("P2 saved, exercises so far:", len(REG))
