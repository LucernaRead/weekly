# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTUUR (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTUUR　KULTUR", "De Lucerna", "NIVEAU A2 → B1　Dutch Design Week en de herfstvakantie　Design Week und Herbstferien")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Ontwerpen in Eindhoven: de Dutch Design Week", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2 → B1")
f.para("Negen dagen lang is Eindhoven de designhoofdstad van Nederland. De Dutch Design Week duurt van zaterdag 17 tot en met zondag 25 oktober. Het is de 26e editie, met als thema «R.A.W.». Ongeveer 2.500 ontwerpers laten hun werk zien: meubels, kleding, websites en dingen die nog geen naam hebben.")
f.para("Waar gaat het over? De ontwerpers werken met materialen: oud plastic wordt een stoel, en planten worden materiaal voor huizen. Dat werken met de natuur heet biodesign. Ook kunstmatige intelligentie (AI) helpt mee aan nieuwe vormen.")
f.para("Een normaal kaartje kost € 32,50; studenten betalen € 19,50. Wie jong is en van maken houdt, is hier op de goede plek: je mag veel dingen aanraken en vragen stellen aan de makers.")
f.head("EROPUIT IN DE HERFSTVAKANTIE", 22)
f.para("Geen school, wel musea: in de herfstvakantie organiseren musea extra activiteiten voor families. Het Limburgs Museum in Venlo heeft van 17 tot en met 25 oktober een speciaal vakantieprogramma, met een gratis familiedag op zaterdag 24 oktober.")
f.para("Let op: niet heel Nederland is vrij. De regio Noord had vorige week vakantie, van 10 tot en met 18 oktober; daar zitten de kinderen deze week weer gewoon in de klas. Alleen Midden en Zuid hebben nu herfstvakantie.")
f.para("Buiten is het ook mooi: het bos is geel en rood, en overal liggen kastanjes en eikels op de grond. Een wandeling in het herfstbos is het goedkoopste uitje van de week.")
f.gloss("de ontwerper = Designer · het materiaal = Material · aanraken = anfassen, berühren · de kastanje = Kastanie · eropuit = hinausgehen, etwas unternehmen.")
f.end_report()

# col 3: two images + facts box (sequential, measured)
ix = COLX[3]
image(p, "kinderdijk.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "De molens van Kinderdijk: een klassiek uitje in de herfstvakantie. Veel families gaan deze week eropuit.",
              "Foto: Nationaal Archief / Wikimedia Commons — CC0")
image(p, "herfstbos.jpg", ix, cy3 + 22, CW, 236)
cy3b = caption(p, ix, cy3 + 22 + 236, CW, "Het herfstbos: geel en rood, met kastanjes op de grond.",
               "Foto: Vovogov90 / Wikimedia Commons — CC0")
facts = ["26e editie van de Dutch Design Week, thema «R.A.W.»",
         "Ongeveer 2.500 ontwerpers in Eindhoven.",
         "Kaartjes: € 32,50; studenten € 19,50."]
sy3 = cy3b + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DDW IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　ÜBUNGEN", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8　Aufgaben gemischt — nach der Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　BEGRIJPEN", 25)
e.note_line("Lies den Text auf Seite 3 und wähle die richtige Antwort.")
e.ex("A2", "wählen", "B", "Die Design Week ist in Eindhoven",
     "De Dutch Design Week is in... A. Amsterdam · B. Eindhoven · C. Venlo", size=20, gap=8)
e.ex("A2", "wählen", "B", "17. bis 25. Oktober = 9 Tage",
     "De Design Week duurt... A. vijf dagen · B. negen dagen · C. twee weken", size=20, gap=8)
e.ex("A2", "wählen", "A", "Das Thema ist «R.A.W.»",
     "Het thema van dit jaar is... A. «R.A.W.» · B. «Natuur» · C. «30 jaar»", size=20, gap=8)
e.ex("B1", "wählen", "B", "Biodesign arbeitet mit Pflanzen und Naturmaterial",
     "Biodesign werkt met... A. alleen oude meubels · B. planten en materialen uit de natuur · C. alleen websites", size=20, gap=8)
e.ex("B1", "wählen", "A", "Kostenloser Familientag: Samstag, 24. Oktober",
     "De gratis familiedag in Venlo is op... A. zaterdag 24 oktober · B. zondag 25 oktober · C. maandag 19 oktober", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.note_line("Fülle die Wörter aus dem Kasten ein. Achtung: Einige Wörter stehen im Plural.")
e.para("ontwerper · materiaal · thema · aanraken · kastanjes · eropuit", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "ergänzen", "ontwerpers", "Plural von ontwerper: ontwerpers",
     "Ongeveer 2.500 ___ laten hun werk zien in Eindhoven.", instr="Ausfüllen", size=20, gap=8)
e.ex("A2", "ergänzen", "thema", "thema = Thema (het-Wort)",
     "Het ___ van de Design Week is «R.A.W.».", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "materiaal", "materiaal = Material",
     "Planten worden ___ voor nieuwe huizen.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "aanraken", "aanraken = anfassen",
     "Op de Design Week mag je veel dingen ___.", instr="Ausfüllen", size=20, gap=8)
e.ex("A2", "ergänzen", "kastanjes", "kastanjes = Kastanien",
     "In het bos liggen ___ en eikels op de grond.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "eropuit", "eropuit = hinausgehen, etwas unternehmen",
     "In de vakantie gaan families ___: naar een museum of het bos.", instr="Ausfüllen", size=20, gap=8)
e.head("C　HET PERFECTUM", 25)
e.note_line("Ergänze im Perfectum — achte auf das Hilfsverb hebben/zijn.")
e.ex("B1", "ergänzen", "heeft gemaakt", "maken steht mit hebben: heeft gemaakt",
     "De ontwerper ___ (maken) een stoel van oud plastic.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "zijn gegaan", "gaan steht mit zijn: zijn gegaan",
     "Wij ___ (gaan) naar het museum in Venlo.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "heeft gezien", "zien ist unregelmäßig: heeft gezien",
     "Zij ___ (zien) het werk van 2.500 ontwerpers.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "zijn gekomen", "komen steht mit zijn: zijn gekomen",
     "Veel families ___ (komen) naar Eindhoven.", instr="Ausfüllen", size=20, gap=8)
e.head("D　REKENEN", 25)
e.note_line("Rechne mit: Antworte mit den Zahlen von Seite 3.")
e.ex("B1", "ergänzen", "9", "17. bis 25. = 9 Tage",
     "De Design Week duurt van 17 tot en met 25 oktober: ___ dagen.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "24", "Familientag am 24. Oktober",
     "De gratis familiedag in het Limburgs Museum is op zaterdag ___ oktober.", instr="Ausfüllen", size=20, gap=8)
e.ex("B2", "ergänzen", "71,50", "19,50 + 19,50 + 32,50 = 71,50",
     "Twee studenten en één volwassene kopen een kaartje. Samen betalen zij € ___.", instr="Ausfüllen", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultuur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　SPORT", "De Lucerna", "NIVEAU B1　Europese week en de topper van zondag　Europawoche und der Sonntagskracher")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P4-feature")
f.title("Europese week: PSV wint in Porto, zondag de topper", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Wat een week voor het Nederlandse voetbal. Zes clubs spelen in Europa. PSV won dinsdag met 1–0 bij FC Porto in de Champions League: een kleine uitslag, maar drie grote punten.")
f.para("Op woensdag speelt Feyenoord in Sevilla tegen Real Betis. Op donderdag komen Ajax (thuis tegen Atalanta), AZ, NEC en FC Twente in actie. De uitslagen van woensdag en donderdag lees je volgende week: deze krant was toen al gedrukt.")
f.para("En dan zondag: de topper. PSV speelt thuis tegen Feyenoord, om 14:30 uur. Later op de middag speelt Sparta tegen Ajax, om 16:45 uur. Het is speelronde 10 van de Eredivisie — en de laatste dag van de herfstvakantie voor Midden en Zuid.")
f.para("Ook op Google is de Europese week groot: de zoekopdracht «uitslagen champions league» haalde dinsdag meer dan 1.000 zoekopdrachten in Nederland. Iedereen wil de uitslagen van alle clubs tegelijk zien.")
f.head("DE BALLON D'OR", 25)
f.para("Op internet praat iedereen over de Ballon d'Or: wie is de beste speler van het jaar? De namen van Yamal, Mbappé en Kane komen vaak voorbij. Maar er is nog geen winnaar: het is speculatie, geen nieuws. Wie is jouw favoriet?")
f.gloss("de uitslag = Ergebnis · winnen = gewinnen · in actie komen = antreten, spielen · de speelronde = Spieltag · de winnaar = Sieger.")
f.end_report()

# col 3: image + programme box (sequential, measured)
ix = COLX[3]
image(p, "elftal1912.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Het Nederlands elftal in 1912. Voetbal is al meer dan honderd jaar de sport van Nederland.",
              "Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein")
facts = ["Dinsdag 20 oktober: FC Porto – PSV 0–1 (Champions League).",
         "Woensdag 21 oktober: Real Betis – Feyenoord (in Sevilla).",
         "Donderdag 22 oktober: Ajax – Atalanta; ook AZ, NEC en FC Twente spelen.",
         "Zondag 25 oktober: PSV – Feyenoord (14:30) en Sparta – Ajax (16:45)."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "HET PROGRAMMA", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P4 col3 ends", sy3 + sh)

# ---- P4 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　ÜBUNGEN", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8　Aufgaben gemischt — nach der Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　BEGRIJPEN", 25)
e.note_line("Lies den Text auf Seite 4 und wähle die richtige Antwort.")
e.ex("B1", "wählen", "B", "PSV gewann auswärts 1–0 in Porto",
     "PSV won dinsdag... A. thuis met 1–0 · B. bij FC Porto met 1–0 · C. met 3–0 in Rotterdam", size=20, gap=8)
e.ex("B1", "wählen", "A", "Feyenoord spielt am Mittwoch in Sevilla",
     "Feyenoord speelt op woensdag... A. in Sevilla · B. in Rotterdam · C. in Porto", size=20, gap=8)
e.ex("B1", "wählen", "B", "Ajax spielt am Donnerstag gegen Atalanta",
     "Ajax speelt donderdag... A. tegen Porto · B. tegen Atalanta · C. tegen Feyenoord", size=20, gap=8)
e.ex("B1", "wählen", "C", "Der Kracher ist am Sonntag um 14:30 Uhr",
     "De topper PSV – Feyenoord is... A. op zaterdag om 14:30 · B. op zondag om 16:45 · C. op zondag om 14:30", size=20, gap=8)
e.ex("B1", "wählen", "B", "Sparta – Ajax beginnt um 16:45 Uhr",
     "Sparta – Ajax begint om... A. 14:30 uur · B. 16:45 uur · C. 20:00 uur", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.note_line("Fülle die Wörter aus dem Kasten ein.")
e.para("uitslag · winnaar · speelronde · in actie · thuis · speculatie", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "ergänzen", "uitslag", "uitslag = Ergebnis",
     "De ___ van Porto – PSV was 1–0.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "winnaar", "winnaar = Sieger",
     "Er is nog geen ___ van de Ballon d'Or.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "speelronde", "speelronde = Spieltag",
     "Het is ___ 10 van de Eredivisie.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "in actie", "in actie komen = antreten",
     "Op donderdag komen vier clubs ___.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "thuis", "thuis = zu Hause (Heimspiel)",
     "Ajax speelt donderdag ___ tegen Atalanta.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "speculatie", "speculatie = Spekulation, Vermutung",
     "De Ballon d'Or-verhalen zijn ___: er is nog geen winnaar.", instr="Ausfüllen", size=20, gap=8)
e.head("C　VERLEDEN TIJD", 25)
e.note_line("Ergänze in der Vergangenheit (Imperfekt oder Perfectum).")
e.ex("B1", "ergänzen", "won", "Imperfekt von winnen: won",
     "PSV ___ (winnen) dinsdag met 1–0 in Porto.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "heeft gewonnen", "Perfectum: heeft gewonnen",
     "De club ___ (winnen) de wedstrijd in Porto.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "ergänzen", "ging", "Imperfekt von gaan: ging",
     "De bal ___ (gaan) in het doel: 1–0!", instr="Ausfüllen", size=20, gap=8)
e.ex("B2", "ergänzen", "zijn gekomen", "Perfectum von komen steht mit zijn",
     "Veel supporters ___ (komen) naar het stadion.", instr="Ausfüllen", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "richtig/falsch", "Waar", "Wahr: Auswärtssieg mit 1–0",
     "PSV won in de Champions League bij FC Porto. Waar of niet waar?", instr="Beurteilen", size=20, gap=8)
e.ex("B1", "richtig/falsch", "Niet waar", "Nicht wahr: Es gibt noch keinen Sieger — nur Spekulation",
     "De Ballon d'Or heeft al een winnaar. Waar of niet waar?", instr="Beurteilen", size=20, gap=8)
e.ex("B2", "richtig/falsch", "Niet waar", "Nicht wahr: Das Spiel ist auswärts in Sevilla",
     "Feyenoord speelt woensdag thuis in Rotterdam. Waar of niet waar?", instr="Beurteilen", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
