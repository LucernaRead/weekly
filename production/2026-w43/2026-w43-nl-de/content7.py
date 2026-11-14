# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · TAAL (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("TAAL　SPRACHE", "De Lucerna", "Sprache im Fokus　Drie niveaus, drie gereedschappen　Drei Stufen, drei Werkzeuge")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　DE KLOK EN HOE LAAT", 24)
a.para("Vraag: «Hoe laat is het?» Antwoord met kwart en half: kwart over twee (02:15), half drie (02:30), kwart voor drie (02:45). Let op: half drie is half vóór drie — dus half vóór het hele uur.", 21.5)
a.para("En de klok verzetten: in oktober gaat hij achteruit, in het voorjaar vooruit. Eén uur maar — maar iedereen praat erover.", 21.5)
a.note_line("hoe laat = nach der Uhrzeit fragen; half drie ist 2:30 (eine halbe Stunde vor drei); im Oktober zurück, im Frühjahr vor.")
a.ex("A2", "ergänzen", "kwart over drie", "kwart over drie = 3:15",
     "03:15 is ___.", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "ergänzen", "half vier", "half vier = 3:30",
     "03:30 is ___.", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "wählen", "B", "half vijf = 4:30 (Fangfrage)",
     "«Half vijf» is... A. 05:30 · B. 04:30 · C. 04:45", size=20.5, gap=10)
a.ex("A2", "ergänzen", "achteruit", "Im Oktober geht die Uhr zurück",
     "In oktober gaat de klok ___.", instr="Ausfüllen", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　VAKANTIE EN VRIJE TIJD", 24)
b.para("In de herfstvakantie gaan families eropuit: naar een museum, het bos of een andere stad. En thuis bijslapen hoort er ook bij: een uur extra in bed is ook vakantie.", 21.5)
b.para("Werkwoorden van de week: eropuit gaan (ging, gegaan) en bijslapen (sliep bij, bijgeslapen). Let op: bijslapen is scheidbaar — «ik sliep zondag lekker bij».", 21.5)
b.note_line("eropuit gaan = ausgehen, etwas unternehmen; bijslapen = nachschlafen — ein trennbares Verb: ik sliep bij.")
b.ex("B1", "ergänzen", "eropuit", "eropuit = hinausgehen, etwas unternehmen",
     "In de vakantie gaan wij ___: naar het bos en een museum.", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "ergänzen", "bijgeslapen", "Partizip von bijslapen: bijgeslapen",
     "Zondag heb ik lekker ___ (bijslapen).", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "ergänzen", "gingen", "Imperfekt Plural von gaan: gingen",
     "Gisteren ___ (gaan) wij naar Eindhoven.", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "wählen", "A", "bijslapen = nachschlafen, sich ausruhen",
     "«Bijslapen» betekent... A. extra slapen om uit te rusten · B. vroeg opstaan · C. buiten slapen", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　RUZIE EN MENINGEN", 24)
c.para("Televisie geeft woorden voor ruzie: «een ruzie hebben met iemand», «het ergens niet mee eens zijn». Een sterke, informele zin is: «Dat slaat nergens op!» Dat betekent: dat is onzin. Gebruik hem voorzichtig — hij is informeel.", 21.5)
c.para("Een mening beleefd geven doe je zo: «Ik vind dat ...», «Volgens mij ...» of «Het lijkt me dat ...» Zo praat je mee over De Hanslers én over de klok.", 21.5)
c.note_line("ruzie = Streit; slaat nergens op ist umgangssprachlich: »Das ist Unsinn« — vorsichtig verwenden; Ik vind dat … = höflich eine Meinung äußern.")
c.ex("B2", "ergänzen", "ruzie", "ruzie = Streit (de-Wort)",
     "Monique en Mike hebben ___ in de serie.", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "wählen", "B", "Volgens mij … ist ein höflicher Anfang",
     "Je begint je mening beleefd met... A. Dat slaat nergens op! · B. Volgens mij is dat goed. · C. Ruzie!", size=20.5, gap=10)
c.ex("B2", "ergänzen", "onzin", "onzin = Unsinn",
     "«Dat slaat nergens op» betekent: dat is ___.", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "ergänzen", "eens", "het eens zijn met iemand = jemandem zustimmen",
     "Ik ben het helemaal met je ___.", instr="Ausfüllen", size=20.5, gap=10)
c.end_report()

# ---- col 3: pas op + het woord + brieven ----
bx = COLX[3]
errs = [
    ("«Half drie is 03:30.»", "→ Fout: half drie is 02:30. «Half» is vóór het uur, niet erna.", "half drie ist 2:30 — halb vor drei!"),
    ("«De klok gaat voorruit.»", "→ «Vooruit» is één woord — en in oktober gaat de klok achteruit.", "vooruit: ein Wort; Oktober: zurück!"),
    ("«Ik loop naar de huisje.»", "→ Altijd «het» bij verkleinwoorden: «het huisje».", "Verkleiningswoorden: immer »het«!"),
    ("«Ik blijf thuis, omdat ik heb geen tijd.»", "→ Na «omdat» staat het werkwoord aan het einde: «... geen tijd heb.»", "Nach »omdat« steht das Verb am Ende."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 192
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "PAS OP!　FEHLERKLINIK", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 18
wt = "«eropuit» betekent: het huis uit gaan om iets leuks te doen — naar een museum, het bos of een festival. In de herfstvakantie gaat heel Nederland eropuit."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("eropuit = hinausgehen und etwas Schönes tun.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "HET WOORD　WORT DER WOCHE", 21, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "eropuit = hinausgehen und etwas Schönes tun.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 18
lt = "«Hallo! Ik ben Emma en ik leer Nederlands in Berlijn. In oktober slaap ik één uur langer — net als jullie!» — Emma (voorbeeldbrief van de redactie)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Beispielbrief der Redaktion. VOL.2: echte Briefe + die beste Arbeit von Seite 8!", "sans", False, 20, CW - 44)) * 29 + 34
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "BRIEVEN VAN LEZERS", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Beispielbrief der Redaktion. VOL.2: echte Briefe + die beste Arbeit von Seite 8!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- zinnen van de week (verbatim from this issue) ----
fy = 1712
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "ZINNEN VAN DE WEEK　SÄTZE DER WOCHE (WÖRTLICH AUS DIESER AUSGABE)", 27, "sans", True, OLIVE)
quotes = [
    ("«De wintertijd begint — en iedereen slaapt een uur langer»", "Die Winterzeit beginnt — und alle schlafen eine Stunde länger.", "Pagina 1"),
    ("«In het voorjaar gaat de klok vooruit, in het najaar achteruit»", "Im Frühjahr geht die Uhr vor, im Herbst zurück.", "Pagina 2"),
    ("«Thuisbezorgd en Uber Eats stoppen met verborgen kosten»", "Thuisbezorgd und Uber Eats schaffen versteckte Kosten ab.", "Pagina 2"),
    ("«Ongeveer 2.500 ontwerpers laten hun werk zien»", "Etwa 2.500 Designer zeigen ihre Arbeit.", "Pagina 3"),
    ("«PSV won dinsdag met 1–0 bij FC Porto»", "PSV gewann am Dienstag mit 1–0 in Porto.", "Pagina 4"),
    ("«Er komen meer dan 3.000 artiesten naar meer dan 200 locaties in de stad»", "Mehr als 3.000 Künstler kommen zu mehr als 200 Orten in der Stadt.", "Pagina 5"),
    ("«ongeveer 750.000 keer zochten Nederlanders naar de klokverandering»", "Etwa 750.000 Mal suchten die Niederländer nach der Zeitumstellung.", "Pagina 6"),
    ("«Samen zijn dat 547.000 zoekopdrachten»", "Zusammen sind das 547.000 Suchanfragen.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- volgende week ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "VOLGENDE WEEK　NÄCHSTE AUSGABE (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Zondag 1 november begint Expeditie Robinson (20:00 uur, RTL 4): wie van de 19 kandidaten is de sterkste? Verder: de uitslagen van de Europese voetbalweek, de laatste verhalen van ADE en de Dutch Design Week, en jullie brieven en beste teksten van pagina 8. Tot maandag!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-taal.svg")
print("P7 saved, exercises so far:", len(REG))
