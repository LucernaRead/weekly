# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JONGEREN (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JONGEREN　YOUNG PEOPLE", "De Lucerna", "NIVEAU B1　ADE wordt 30, De Hanslers en Robinson　Festival, reality TV and the island show")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Dertig jaar dansen: ADE neemt Amsterdam over", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Amsterdam danst weer. Het Amsterdam Dance Event (ADE) is van woensdag 21 tot en met zondag 25 oktober in Amsterdam. Het festival wordt dertig jaar. Er komen meer dan 3.000 artiesten naar meer dan 200 locaties in de stad.")
f.para("De eerste namen kwamen al in juni: meer dan 250 artiesten, met onder anderen Armin van Buuren, Amelie Lens, Adam Beyer en Skepta. Na de tweede ronde zijn er meer dan 1.500 namen zeker. De krant NRC schreef op 19 oktober over dertig jaar ADE: feesten en netwerken horen bij elkaar op dit festival.")
f.para("Overdag is ADE meer dan dansen: er is ook een conferentie, waar dj's, makers en bedrijven praten over muziek en werk. Feesten én netwerken — precies zoals NRC het beschreef.")
f.para("Thuis op de bank is er ook spanning. De realityserie De Hanslers op SBS6 zorgt voor gesprekken in heel het land: de ruzie tussen Monique en Mike was dinsdag de meest gezochte zoekopdracht van Nederland, met meer dan 10.000 zoekopdrachten.")
f.para("En na ADE begint een ander avontuur: Expeditie Robinson. De 19 kandidaten zijn bekend — onder hen Maxime Meiland, Boaz Kok van de band Goldband en oud-shorttracker Sjinkie Knegt. Het programma begint op zondag 1 november om 20:00 uur op RTL 4.")
f.para("Het eilandprogramma is zwaar: de kandidaten slapen buiten, maken zelf vuur en zoeken hun eigen eten. Wie een proef verliest, kan naar huis worden gestemd; wie het langst blijft, wint. De kandidaten komen uit Nederland en Vlaanderen.")
f.box("ZO PLAN JE ADE　FESTIVAL TIPS", [
    ("1. Kies twee of drie locaties per avond (choose two or three venues per evening)", "serif", False, INK, 21, 1.36),
    ("2. Reis met de trein of de fiets (go by train or bike)", "serif", False, INK, 21, 1.36),
    ("3. Drink water tussen het dansen door (drink water between dances)", "serif", False, INK, 21, 1.36),
    ("4. Spreek een plek af als je je vrienden kwijtraakt (agree a meeting point if you lose your friends)", "serif", False, INK, 21, 1.36),
], tsize=22)
f.gloss("de artiest = a performer · de locatie = a venue · de ruzie = a row, a quarrel · de kandidaat = a contestant · het avontuur = an adventure.")
f.end_report()

# col 3: image + facts + en jij (sequential, measured)
ix = COLX[3]
image(p, "gracht.jpg", ix, 200, CW, 272)
cy3 = caption(p, ix, 472, CW, "Een boot in een Amsterdamse gracht. Tijdens ADE is de hele stad een podium: meer dan 200 locaties.",
              "Foto: W. Punt / Anefo, Nationaal Archief — CC0")
facts = ["Meer dan 3.000 artiesten op ADE, op meer dan 200 locaties.",
         "«de hanslers ruzie»: meer dan 10.000 zoekopdrachten op dinsdag.",
         "Expeditie Robinson: 19 kandidaten; start zondag 1 november, 20:00 uur."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "JONGEREN IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Dans je graag, of kijk je liever naar een serie thuis? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Do you love dancing, or do you prefer a series at home? Write two sentences in Dutch and send them in.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ?　AND YOU?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Do you love dancing, or do you prefer a series at home? Write two sentences in Dutch and send them in.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　EXERCISES ON PAGE 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8　levels are mixed; find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　BEGRIJPEN", 25)
e.note("Read the article on page 5 and choose the right answer.")
e.ex("B1", "choice", "B", "ADE runs from 21 to 25 October",
     "ADE duurt van... A. 17 tot en met 25 oktober · B. 21 tot en met 25 oktober · C. 1 tot en met 5 november", size=20, gap=8)
e.ex("B1", "choice", "C", "More than 3,000 artists in all (250 was just the first list of names)",
     "Er komen meer dan ___ artiesten naar ADE. A. 250 · B. 1.500 · C. 3.000", size=20, gap=8)
e.ex("B1", "choice", "B", "Tuesday's biggest search was the Hanslers row",
     "De meest gezochte zoekopdracht van dinsdag was... A. «ade» · B. «de hanslers ruzie» · C. «uitslagen»", size=20, gap=8)
e.ex("B1", "choice", "B", "Robinson starts on Sunday 1 November",
     "Expeditie Robinson begint op... A. zondag 25 oktober · B. zondag 1 november · C. woensdag 21 oktober", size=20, gap=8)
e.ex("B1", "choice", "C", "Sjinkie Knegt is a former short-track skater",
     "Sjinkie Knegt was vroeger... A. een dj · B. een ontwerper · C. een shorttracker", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.note("Fill in the words from the box.")
e.para("artiesten · locaties · ruzie · kandidaten · avontuur · netwerken", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "complete", "artiesten", "artiesten = artists (plural)",
     "Meer dan 3.000 ___ komen naar Amsterdam.", instr="Fill in", size=20, gap=8)
e.ex("B1", "complete", "locaties", "locaties = venues (plural)",
     "Het festival heeft meer dan 200 ___ in de stad.", instr="Fill in", size=20, gap=8)
e.ex("B1", "complete", "ruzie", "ruzie = a row, a quarrel",
     "De ___ tussen Monique en Mike is groot nieuws.", instr="Fill in", size=20, gap=8)
e.ex("B1", "complete", "kandidaten", "kandidaten = contestants (plural)",
     "Expeditie Robinson heeft 19 ___.", instr="Fill in", size=20, gap=8)
e.ex("B1", "complete", "avontuur", "avontuur = adventure (het-word)",
     "Robinson is een ___ op een eiland.", instr="Fill in", size=20, gap=8)
e.ex("B1", "complete", "netwerken", "netwerken = networking, meeting people",
     "Op ADE horen feesten en ___ bij elkaar.", instr="Fill in", size=20, gap=8)
e.head("C　DE TOEKOMST MET GAAN", 25)
e.note("Use gaan + infinitive for the future.")
e.ex("B1", "complete", "gaat beginnen", "gaat beginnen = is going to start",
     "Expeditie Robinson ___ (beginnen) op 1 november.", instr="Fill in", size=20, gap=8)
e.ex("B1", "complete", "gaan dansen", "wij → gaan + infinitive dansen",
     "Wij ___ (dansen) op ADE in Amsterdam.", instr="Fill in", size=20, gap=8)
e.ex("B2", "complete", "gaat winnen", "gaat winnen = is going to win (a guess)",
     "Wie ___ (winnen) Expeditie Robinson, denk je?", instr="Fill in", size=20, gap=8)
e.ex("B1", "complete", "gaat kijken", "hij → gaat kijken",
     "Hij ___ (kijken) vanavond naar de serie.", instr="Fill in", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "true or false", "Waar", "True: ADE turns thirty",
     "ADE wordt dit jaar dertig jaar. Waar of niet waar?", instr="True or false?", size=20, gap=8)
e.ex("B1", "true or false", "Niet waar", "Not true: it starts on 1 November",
     "Expeditie Robinson begint op 25 oktober. Waar of niet waar?", instr="True or false?", size=20, gap=8)
e.ex("B2", "true or false", "Waar", "True: more than 10,000 searches (Tuesday snapshot)",
     "De zoekopdracht «de hanslers ruzie» had meer dan 10.000 zoekopdrachten. Waar of niet waar?", instr="True or false?", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jongeren.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · VERDIEPING (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERDIEPING　IN DEPTH", "De Lucerna", "NIVEAU B2　Waarom googelt Nederland de klok?　Why the Netherlands googles the clock")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P6-main")
f.title("Waarom googelt Nederland de klok?", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B2")
f.para("Twee keer per jaar stelt heel Nederland dezelfde vraag: gaat de klok vooruit of achteruit? Een onderzoek van Wristler, gepubliceerd op dinsdag 20 oktober, telt de zoekopdrachten van oktober vorig jaar. Het resultaat is verrassend: ongeveer 750.000 keer zochten Nederlanders naar de klokverandering.")
f.para("De twee grootste zoektermen waren «wintertijd» (301.000 keer) en «klok verzetten» (246.000 keer). Samen zijn dat 547.000 zoekopdrachten. De rest — ongeveer 203.000 — waren andere vragen en woorden over de klok.")
f.para("Het mooiste cijfer gaat over de richting. 60.500 mensen vroegen: «wanneer gaat de klok achteruit?» — het goede antwoord. Maar 6.600 mensen vroegen het omgekeerde: «wanneer gaat de klok vooruit?» Ruim negen keer zoveel mensen vragen het goed als fout.")
f.para("Nederland staat niet alleen. Van de 16 landen in het onderzoek zoekt alleen Italië per inwoner nog meer naar de klok. Nederlanders zijn dus kampioen twijfelen — op één land na.")
f.para("Waarom is het zo moeilijk? De regel lijkt simpel, maar het gevoel is anders. Het ezelsbruggetje helpt: in het voorjaar vooruit, in het najaar achteruit. En toch googelt iedereen het elk jaar opnieuw. Misschien is dat de echte traditie: niet de klok, maar de vraag.")
f.head("AFSCHAFFEN OF NIET?", 25)
f.para("Elk jaar komt ook de discussie terug: moeten we de klok nog wel verzetten? Sommigen willen één vaste tijd voor het hele jaar; anderen houden van het lange licht op zomeravonden. Een besluit is er niet — de klok gaat voorlopig twee keer per jaar heen en weer.")
f.para("En dus komt de vraag elk jaar twee keer terug: in oktober voor de wintertijd en in het voorjaar voor de zomertijd. En twee keer per jaar zoekt Nederland weer massaal naar hetzelfde antwoord.")
f.gloss("de zoekopdracht = a search query · tellen = to count · het omgekeerde = the opposite · per inwoner = per inhabitant · twijfelen = to be unsure.")
f.end_report()

# col 3: chart with exactly proportional bars + pro/contra box (sequential, measured)
ix = COLX[3]
rows = [
    ("«wintertijd»", "301.000", 250),
    ("«klok verzetten»", "246.000", 204),
    ("«...klok achteruit?»", "60.500", 50),
    ("«...klok vooruit?»", "6.600", 5),
]
cap = "Zoekopdrachten in oktober vorig jaar. Bron: onderzoek van Wristler, gepubliceerd op 20 oktober 2026."
capcn = "Source: Wristler study, published on 20 October 2026; the searches counted are from October last year"
ch = 62 + len(rows) * 58 + 14 + len(wrap(cap, "serif", False, 19, CW - 44)) * 27 + 6 + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
p.rect(ix, 200, CW, ch, fill=BOX)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DE CIJFERS　THE NUMBERS", 24, "sans", True, OLIVE)
yy3 += 58
for lab, val, bw in rows:
    p.text(ix + 22, yy3 + 20, lab, 19.5, "serif", True, INK)
    p.text(ix + CW - 22, yy3 + 20, val, 19.5, "sans", True, OLIVE, anchor="end")
    p.rect(ix + 22, yy3 + 30, bw, 18, fill=OLIVE)
    yy3 += 58
yy3 += 14
yy3 = p.para(ix + 22, yy3 + 19, cap, 19, "serif", False, GREY, CW - 44, 1.36)
yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, CW - 44, 1.32) + 6
print("P6 chart ends", 200 + ch, "content to", yy3)
by6 = 200 + ch + 26
bt = [
    ("Stoppen met verzetten: één vaste tijd voor het hele jaar is rustiger voor lichaam en planning.", "serif", False, INK, 21, 1.4),
    ("Doorgaan: zo houden we de lange, lichte avonden in de zomer.", "serif", False, INK, 21, 1.4),
    ("De krant kiest niet: wij tellen alleen de zoekopdrachten. En jij?", "serif", False, INK, 21, 1.4),
]
bh = 62 + sum(len(wrap(t, "serif", False, 21, CW - 44)) * 29.5 + 8 for t, *_ in bt) + 16 + 30
p.rect(ix, by6, CW, bh, fill="#f0eee5")
yy3 = by6 + 16
p.text(ix + 22, yy3 + 26, "AFSCHAFFEN OF NIET?　ABOLISH IT?", 19, "sans", True, OLIVE)
yy3 += 52
for t, k, b, fl, s, lh in bt:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.4) + 8
print("P6 col3 ends", by6 + bh)

# ---- P6 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　EXERCISES ON PAGE 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8　levels are mixed; find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEES DE GRAFIEK", 25)
e.note("Answer with the chart on page 6 (Wristler data).")
e.ex("B2", "complete", "301.000", "«wintertijd» was searched 301,000 times (the most)",
     "De meest gezochte term was «wintertijd»: ___ keer.", instr="Fill in", size=21.5, gap=9)
e.ex("B2", "complete", "547.000", "301.000 + 246.000 = 547.000",
     "«wintertijd» en «klok verzetten» samen: ___ zoekopdrachten.", instr="Fill in", size=21.5, gap=9)
e.ex("B2", "complete", "203.000", "750,000 − 547,000 ≈ 203,000 (approximate)",
     "Van de ±750.000 zoekopdrachten waren er ongeveer ___ voor andere vragen.", instr="Fill in", size=21.5, gap=9)
e.ex("B2", "complete", "6.600", "Only 6,600 people asked the wrong way round",
     "Slechts ___ mensen vroegen «vooruit» in plaats van «achteruit».", instr="Fill in", size=21.5, gap=9)
e.ex("B2", "complete", "9", "60,500 ÷ 6,600 ≈ 9 times over",
     "«Achteruit» is ruim ___ keer zo vaak gezocht als «vooruit».", instr="Fill in", size=21.5, gap=9)
e.ex("B2", "choice", "B", "It counts searches from October last year",
     "Het onderzoek telt zoekopdrachten uit... A. oktober 2026 · B. oktober vorig jaar · C. de zomer van 2026", size=21.5, gap=9)
e.head("B　BEGRIJPEN", 25)
e.note("Read the article on page 6 and choose the right answer.")
e.ex("B2", "choice", "B", "Only Italy searches more per inhabitant",
     "Alleen welk land zoekt per inwoner méér naar de klok? A. Duitsland · B. Italië · C. Frankrijk", size=21.5, gap=9)
e.ex("B2", "choice", "B", "The study covers 16 countries",
     "Hoeveel landen deden mee aan het onderzoek? A. 10 · B. 16 · C. 27", size=21.5, gap=9)
e.ex("B2", "choice", "A", "The direction is hard to remember, so people search every year",
     "Waarom googelen mensen de klok elk jaar weer? A. De richting is moeilijk te onthouden · B. De klok verandert nooit · C. Er is geen ezelsbruggetje", size=21.5, gap=9)
e.ex("B2", "choice", "B", "Some people want one fixed time all year",
     "Wat wil een deel van de mensen? A. Twee keer per jaar verzetten, voor altijd · B. Eén vaste tijd voor het hele jaar · C. Nooit meer klokken", size=21.5, gap=9)
e.ex("B1", "choice", "B", "The rhyme: back in autumn",
     "Het ezelsbruggetje zegt: in het najaar gaat de klok... A. vooruit · B. achteruit · C. niet", size=21.5, gap=9)
e.head("C　WOORDEN", 25)
e.note("Fill in the words from the box.")
e.para("zoekopdracht · per inwoner · het omgekeerde · tellen", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B2", "complete", "zoekopdracht", "zoekopdracht = a search query",
     "«wintertijd» was de grootste ___ van oktober.", instr="Fill in", size=21.5, gap=9)
e.ex("B2", "complete", "per inwoner", "per inwoner = per inhabitant",
     "Italië zoekt ___ nog meer dan Nederland.", instr="Fill in", size=21.5, gap=9)
e.ex("B2", "complete", "het omgekeerde", "het omgekeerde = the opposite",
     "«Vooruit» is ___ van «achteruit».", instr="Fill in", size=21.5, gap=9)
e.ex("B2", "complete", "telt", "tellen: het onderzoek → telt",
     "Het onderzoek ___ (tellen) alle zoekopdrachten.", instr="Fill in", size=21.5, gap=9)
e.head("D　MAAK DE ZINNEN", 25)
e.note("Put the words in the right order to make sentences.")
e.ex("B2", "make sentences", "Nederlanders zoeken elk jaar naar de klok.", "The verb zoeken comes second",
     "nederlanders / zoeken / elk jaar / naar de klok → ___", instr="Make the sentence", size=21.5, gap=9)
e.ex("B2", "make sentences", "Alleen Italië zoekt per inwoner meer.", "alleen + the country name comes first",
     "alleen Italië / zoekt / per inwoner / meer → ___", instr="Make the sentence", size=21.5, gap=9)
e.ex("B2", "make sentences", "De discussie komt elk jaar terug.", "terug is a separable prefix: it goes to the end",
     "de discussie / komt / elk jaar / terug → ___", instr="Make the sentence", size=21.5, gap=9)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-verdieping.svg")
print("P6 saved, exercises so far:", len(REG))
