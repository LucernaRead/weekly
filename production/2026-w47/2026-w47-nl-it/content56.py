# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JONGEREN (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JONGEREN　GIOVANI", "De Lucerna", "NIVEAU B1　Robinson, de surprise en het gedicht　Robinson, il regalo travestito e la piccola poesia")

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
    ("1. Kijk zondag om 20:00 uur op RTL 4 (guardare su RTL 4, domenica alle 20:00)", "serif", False, INK, 21, 1.36),
    ("2. Let op de proeven: daar worden de punten verdeeld (guarda le prove: lì si assegnano i punti)", "serif", False, INK, 21, 1.36),
    ("3. Raad met vrienden wie het langst blijft (indovina con gli amici chi resta più a lungo)", "serif", False, INK, 21, 1.36),
    ("4. Schrijf daarna een gedicht voor je surprise (scrivi poi una poesia per il tuo regalo travestito)", "serif", False, INK, 21, 1.36),
])
f.gloss("de surprise regalo travestito · het gedicht poesia · de verslaggever reporter · de proef prova · de aflevering puntata.")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("La domenica guardi Expeditie Robinson, o preferisci preparare un regalo travestito con una piccola poesia? Scrivi due frasi in olandese e mandale.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ?　E TU?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "La domenica guardi Expeditie Robinson, o preferisci preparare un regalo travestito con una piccola poesia? Scrivi due frasi in olandese e mandale.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 boxes end", ey3 + eh)
iy5 = ey3 + eh + 26
image(p, "strand.jpg", ix, iy5, CW, 250)
cy5 = caption(p, ix, iy5 + 250, CW, "Een tropische baai met palmen — net als het eiland in Maleisië waar Expeditie Robinson wordt opgenomen.",
              "Foto: Elise Iovenko / Unsplash — CC0")
print("P5 col3 ends", cy5)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　ESERCIZI DI PAGINA 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　I livelli sono mescolati; trova il tuo numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Leggi l'articolo a pagina 5 e scegli la risposta giusta.")
e.ex("B1", "Scelta multipla", "B", "Robinson va in onda ogni domenica alle 20:00 su RTL 4",
     "Expeditie Robinson is elke zondag om... A. 18:00 uur · B. 20:00 uur · C. 12:00 uur", size=20, gap=8)
e.ex("B1", "Scelta multipla", "A", "19 concorrenti",
     "Expeditie Robinson heeft ___ kandidaten. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "Scelta multipla", "C", "Il programma è girato su un'isola deserta in Malesia",
     "De kandidaten leven op een eiland in... A. Spanje · B. Grave · C. Maleisië", size=20, gap=8)
e.ex("B1", "Scelta multipla", "B", "I concorrenti passano 34 giorni sull'isola",
     "De kandidaten blijven ___ dagen op het eiland. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "Scelta multipla", "A", "Un regalo travestito contiene una poesia",
     "Bij een surprise hoort... A. een gedicht · B. een boek · C. een lampion", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("Completa con le parole del riquadro.")
e.para("surprise · gedicht · verslaggever · proef · aflevering · kandidaat", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Completa la frase", "surprise", "surprise = regalo travestito (de)",
     "Ik maak een ___ voor mijn vriendin.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "verslaggever", "verslaggever = reporter (de)",
     "Camille Vanuxem is de ___ van het programma.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "proef", "proef = prova, sfida (de)",
     "Wie een ___ verliest, kan naar huis gaan.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "gedicht", "gedicht = poesia (het)",
     "In vier regels schrijf ik een ___.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "aflevering", "aflevering = puntata",
     "Zondag is er een nieuwe ___ van Robinson.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "kandidaten", "kandidaat, plurale: kandidaten",
     "Er zijn 19 ___ op het eiland.", instr="Completa", size=20, gap=8)
e.head("C　DE TOEKOMST MET GAAN", 25)
e.bridge("Parla del futuro con gaan + infinito.")
e.ex("B1", "Completa la frase", "gaat winnen", "gaat winnen = vincerà (solo un'ipotesi)",
     "Wie ___ (winnen) Expeditie Robinson, denk je?", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "gaan kijken", "wij → gaan + infinito kijken",
     "Wij ___ (kijken) zondag naar de nieuwe aflevering.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "gaat maken", "zij → gaat maken",
     "Zij ___ (maken) zondag een surprise voor pakjesavond.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "gaan schrijven", "zij (plurale) → gaan schrijven",
     "De kinderen ___ (schrijven) een gedicht van vier regels.", instr="Completa", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "Vero o falso", "Waar", "Vero: il programma è iniziato il 1º novembre",
     "Expeditie Robinson begon op 1 november. Waar of niet waar?", instr="Vero o falso?", size=20, gap=8)
e.ex("B1", "Vero o falso", "Niet waar", "Falso: il programma è girato in Malesia",
     "Expeditie Robinson speelt in Spanje. Waar of niet waar?", instr="Vero o falso?", size=20, gap=8)
e.ex("B2", "Vero o falso", "Niet waar", "Falso: quattro versi bastano per una poesia",
     "Een gedicht voor een surprise moet minstens twintig regels hebben. Waar of niet waar?", instr="Vero o falso?", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jongeren.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · VERDIEPING (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERDIEPING　APPROFONDIMENTO", "De Lucerna", "NIVEAU B2　Sinterklaas: oud feest, nieuwe wensen　Sinterklaas: un'antica festa, nuovi desideri")

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
f.gloss("het verlanglijstje lista dei desideri · de surprise regalo travestito · het gedicht poesia · veranderen cambiare · de traditie tradizione.")
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
capcn = "Dati per l'esercizio: numeri inventati, solo per esercitarsi, non un vero sondaggio. Domanda: che cosa metti nella tua scarpa? (100 giovani)"
capcn_w = 377.7  # delta D8: width-scan band 367.4–388.0px keeps the 4 lines; mid 377.7
ch = 62 + len(rows) * 58 + 14 + len(wrap(cap, "serif", False, 19, CW - 44)) * 27 + 6 + len(wrap(capcn, "sans", False, 18.5, capcn_w)) * 26 + 18
p.rect(ix, 200, CW, ch, fill=BOX)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DE GRAFIEK　DATI INVENTATI", 24, "sans", True, OLIVE)
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
p.text(ix + 22, yy3 + 26, "VOOR OF TEGEN?　PRO O CONTRO?", 20, "sans", True, OLIVE)  # D5: 21 -> 20 — advance 403.2px > box 400.5
yy3 += 52
for t, k, b, fl, s, lh in bt:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.4) + 8
print("P6 col3 ends", by6 + bh)

# ---- P6 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　ESERCIZI DI PAGINA 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　I livelli sono mescolati; trova il tuo numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEES DE GRAFIEK", 25)
e.bridge("Rispondi con il grafico a pagina 6 (dati di esercitazione).")
e.ex("B2", "Completa la frase", "35", "35 giovani mettono una carota e un disegno nella scarpa",
     "___ van de 100 jongeren zetten een wortel en een tekening in hun schoen.", instr="Completa", size=21.5, gap=9)
e.ex("B2", "Completa la frase", "30", "30 persone mettono una lista dei desideri",
     "___ jongeren zetten een verlanglijstje in hun schoen.", instr="Completa", size=21.5, gap=9)
e.ex("B2", "Completa la frase", "65", "35 + 30 = 65",
     "Wortel en verlanglijstje samen: ___ jongeren.", instr="Completa", size=21.5, gap=9)
e.ex("B2", "Completa la frase", "15", "15 persone non mettono ancora niente",
     "___ jongeren zetten nog niets in hun schoen.", instr="Completa", size=21.5, gap=9)
e.ex("B2", "Completa la frase", "100", "Il grafico conta 100 persone in tutto: 35+30+20+15",
     "De grafiek telt in totaal ___ jongeren.", instr="Completa", size=21.5, gap=9)
e.head("B　BEGRIJPEN", 25)
e.bridge("Leggi l'articolo a pagina 6 e scegli la risposta giusta.")
e.ex("B2", "Scelta multipla", "B", "Prima si metteva un disegno nella scarpa; ora spesso una lista dei desideri",
     "Vroeger zat er een tekening in de schoen; nu steeds vaker... A. een lampion · B. een verlanglijstje · C. een boek", size=21.5, gap=9)
e.ex("B2", "Scelta multipla", "B", "Una surprise è un regalo nascosto in una confezione strana",
     "Een surprise is een cadeau... A. in een doos van de winkel · B. verstopt in iets geks · C. zonder gedicht", size=21.5, gap=9)
e.ex("B2", "Scelta multipla", "C", "Il notiziario di Sinterklaas è tutti i giorni alle 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 12:00 uur · B. 20:00 uur · C. 18:00 uur", size=21.5, gap=9)
e.ex("B2", "Scelta multipla", "A", "Una tradizione vive quando la gente continua a festeggiarla",
     "Een traditie leeft als... A. mensen haar blijven vieren · B. ze oud is · C. ze op televisie is", size=21.5, gap=9)
e.ex("B2", "Scelta multipla", "B", "San Martino era mercoledì scorso",
     "Sint-Maarten was... A. gisteren · B. vorige week woensdag · C. volgende week", size=21.5, gap=9)
e.head("C　WOORDEN", 25)
e.bridge("Completa con le parole del riquadro.")
e.para("verlanglijstje · surprise · gedicht · veranderen", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B2", "Completa la frase", "verlanglijstje", "verlanglijstje = lista dei desideri (het)",
     "Op het ___ staan drie wensen.", instr="Completa", size=21.5, gap=9)
e.ex("B2", "Completa la frase", "surprise", "surprise = regalo travestito (de)",
     "Het cadeau zit verstopt in een ___.", instr="Completa", size=21.5, gap=9)
e.ex("B2", "Completa la frase", "gedicht", "gedicht = poesia (het)",
     "Bij het cadeau hoort een ___ van vier regels.", instr="Completa", size=21.5, gap=9)
e.ex("B2", "Completa la frase", "verandert", "veranderen → verandert (singolare)",
     "Het feest ___ elk jaar een beetje.", instr="Completa", size=21.5, gap=9)
e.head("D　MAAK DE ZINNEN", 25)
e.bridge("Metti le parole nell'ordine giusto per formare frasi.")
e.ex("B2", "Forma la frase", "Sinterklaas is een oud feest in Nederland.", "Soggetto + verbo + complemento + luogo",
     "sinterklaas / is / een oud feest / in nederland → ___", instr="Forma la frase", size=21.5, gap=9)
e.ex("B2", "Forma la frase", "De kinderen zetten hun schoen bij de deur.", "Soggetto + verbo + complemento + luogo",
     "de kinderen / zetten / hun schoen / bij de deur → ___", instr="Forma la frase", size=21.5, gap=9)
e.ex("B2", "Forma la frase", "Een traditie leeft als mensen haar blijven vieren.", "La frase con als va alla fine",
     "een traditie / leeft / als mensen haar blijven vieren → ___", instr="Forma la frase", size=21.5, gap=9)
e.ex("B2", "Forma la frase", "Het feest verandert, maar het verdwijnt niet.", "veranderen + maar + negazione",
     "het feest / verandert / maar het verdwijnt niet → ___", instr="Forma la frase", size=21.5, gap=9)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-verdieping.svg")
print("P6 saved, exercises so far:", len(REG))
