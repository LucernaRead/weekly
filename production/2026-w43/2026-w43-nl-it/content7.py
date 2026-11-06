# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-nl-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · TAAL (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("TAAL · LINGUA", "De Lucerna", "La lingua in primo piano · Drie niveaus, drie gereedschappen · Tre livelli, tre strumenti")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · DE KLOK EN HOE LAAT", 24)
a.para("Vraag: «Hoe laat is het?» Antwoord met kwart en half: kwart over twee (02:15), half drie (02:30), kwart voor drie (02:45). Let op: half drie is half vóór drie — dus half vóór het hele uur.", 21.5)
a.para("En de klok verzetten: in oktober gaat hij achteruit, in het voorjaar vooruit. Eén uur maar — maar iedereen praat erover.", 21.5)
a.expl("Nota — hoe laat chiede l'ora; half drie sono le 2:30 (mezz'ora prima delle tre); in ottobre indietro, in primavera avanti.")
a.ex("A2", "Completa la frase", "kwart over drie", "kwart over drie = le 3:15",
     "03:15 is ___.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Completa la frase", "half vier", "half vier = le 3:30",
     "03:30 is ___.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Scelta multipla", "B", "half vijf = le 4:30 (domanda trappola)",
     "«Half vijf» is... A. 05:30 · B. 04:30 · C. 04:45", size=20.5, gap=10)
a.ex("A2", "Completa la frase", "achteruit", "In ottobre l'orologio va indietro",
     "In oktober gaat de klok ___.", instr="Completa", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · VAKANTIE EN VRIJE TIJD", 24)
b.para("In de herfstvakantie gaan families eropuit: naar een museum, het bos of een andere stad. En thuis bijslapen hoort er ook bij: een uur extra in bed is ook vakantie.", 21.5)
b.para("Werkwoorden van de week: eropuit gaan (ging, gegaan) en bijslapen (sliep bij, bijgeslapen). Let op: bijslapen is scheidbaar — «ik sliep zondag lekker bij».", 21.5)
b.expl("Nota — eropuit gaan uscire per divertirsi; bijslapen dormire per recuperare, verbo separabile: ik sliep bij.")
b.ex("B1", "Completa la frase", "eropuit", "eropuit = uscire, andare in giro",
     "In de vakantie gaan wij ___: naar het bos en een museum.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Completa la frase", "bijgeslapen", "Participio di bijslapen: bijgeslapen",
     "Zondag heb ik lekker ___ (bijslapen).", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Completa la frase", "gingen", "Passato plurale di gaan: gingen",
     "Gisteren ___ (gaan) wij naar Eindhoven.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Scelta multipla", "A", "bijslapen = dormire per recuperare",
     "«Bijslapen» betekent... A. extra slapen om uit te rusten · B. vroeg opstaan · C. buiten slapen", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · RUZIE EN MENINGEN", 24)
c.para("Televisie geeft woorden voor ruzie: «een ruzie hebben met iemand», «het ergens niet mee eens zijn». Een sterke, informele zin is: «Dat slaat nergens op!» Dat betekent: dat is onzin. Gebruik hem voorzichtig — hij is informeel.", 21.5)
c.para("Een mening beleefd geven doe je zo: «Ik vind dat ...», «Volgens mij ...» of «Het lijkt me dat ...» Zo praat je mee over De Hanslers én over de klok.", 21.5)
c.expl("Nota — ruzie lite; slaat nergens op è informale («non ha senso»), usalo con cautela; Ik vind dat… esprime un'opinione in modo gentile.")
c.ex("B2", "Completa la frase", "ruzie", "ruzie = la lite (con de)",
     "Monique en Mike hebben ___ in de serie.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Scelta multipla", "B", "«Volgens mij…» è un inizio gentile",
     "Je begint je mening beleefd met... A. Dat slaat nergens op! · B. Volgens mij is dat goed. · C. Ruzie!", size=20.5, gap=10)
c.ex("B2", "Completa la frase", "onzin", "onzin = una sciocchezza, senza senso",
     "«Dat slaat nergens op» betekent: dat is ___.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Completa la frase", "eens", "het eens zijn met iemand = essere d'accordo con qualcuno",
     "Ik ben het helemaal met je ___.", instr="Completa", size=20.5, gap=10)
c.end_report()

# ---- col 3: pas op + het woord + brieven ----
bx = COLX[3]
errs = [
    ("«Half drie is 03:30.»", "→ Fout: half drie is 02:30. «Half» is vóór het uur, niet erna.", "half drie = le 2:30, prima delle tre."),
    ("«De klok gaat voorruit.»", "→ «Vooruit» is één woord — en in oktober gaat de klok achteruit.", "vooruit: una sola parola."),
    ("«Ik loop naar de huisje.»", "→ Altijd «het» bij verkleinwoorden: «het huisje».", "I diminutivi: sempre «het»."),
    ("«Ik blijf thuis, omdat ik heb geen tijd.»", "→ Na «omdat» staat het werkwoord aan het einde: «... geen tijd heb.»", "Dopo «omdat», verbo alla fine."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 192
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "PAS OP! · ERRORI FREQUENTI", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 18
wt = "«eropuit» betekent: het huis uit gaan om iets leuks te doen — naar een museum, het bos of een festival. In de herfstvakantie gaat heel Nederland eropuit."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("eropuit = uscire per divertirsi: al museo, nel bosco o a un festival.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "HET WOORD · LA PAROLA", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "eropuit = uscire per divertirsi: al museo, nel bosco o a un festival.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 18
lt = "«Hallo! Ik ben Chen en ik leer Nederlands in Beijing. In oktober slaap ik één uur langer — net als jullie!» — Chen (voorbeeldbrief van de redactie)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Esempio della redazione. Nel VOL.2: lettere vere e miglior testo di pagina 8!", "sans", False, 20, CW - 44)) * 29 + 34
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "BRIEVEN VAN LEZERS", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Esempio della redazione. Nel VOL.2: lettere vere e miglior testo di pagina 8!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- zinnen van de week (verbatim from this issue) ----
fy = 1712
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "ZINNEN VAN DE WEEK · FRASI DELLA SETTIMANA (PAROLA PER PAROLA, DA QUESTA EDIZIONE)", 27, "sans", True, OLIVE)
quotes = [
    ("«De wintertijd begint — en iedereen slaapt een uur langer»", "Comincia l'ora solare — e tutti dormono un'ora in più.", "Pagina 1"),
    ("«In het voorjaar gaat de klok vooruit, in het najaar achteruit»", "In primavera l'orologio va avanti, in autunno indietro.", "Pagina 2"),
    ("«Thuisbezorgd en Uber Eats stoppen met verborgen kosten»", "Thuisbezorgd e Uber Eats mettono fine ai costi nascosti.", "Pagina 2"),
    ("«Ongeveer 2.500 ontwerpers laten hun werk zien»", "Circa 2.500 designer mostrano il loro lavoro.", "Pagina 3"),
    ("«PSV won dinsdag met 1–0 bij FC Porto»", "Martedì il PSV ha vinto 1–0 a Porto.", "Pagina 4"),
    ("«Er komen meer dan 3.000 artiesten naar meer dan 200 locaties in de stad»", "Più di 3.000 artisti in più di 200 luoghi della città.", "Pagina 5"),
    ("«ongeveer 750.000 keer zochten Nederlanders naar de klokverandering»", "Gli olandesi hanno cercato il cambio dell'ora circa 750.000 volte.", "Pagina 6"),
    ("«Samen zijn dat 547.000 zoekopdrachten»", "Insieme fanno 547.000 ricerche.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- volgende week ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "VOLGENDE WEEK · LA PROSSIMA SETTIMANA (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Zondag 1 november begint Expeditie Robinson (20:00 uur, RTL 4): wie van de 19 kandidaten is de sterkste? Verder: de uitslagen van de Europese voetbalweek, de laatste verhalen van ADE en de Dutch Design Week, en jullie brieven en beste teksten van pagina 8. Tot maandag!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-taal.svg")
print("P7 saved, exercises so far:", len(REG))
