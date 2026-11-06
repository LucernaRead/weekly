# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-it-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · PRIMA PAGINA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2 · SECONDA EDIZIONE", 23, "sans", True, OLIVE)
p.text(975, 92, "OGNI SETTIMANA IN ITALIANO · ELKE WEEK · HET ITALIAANS DAT DE ITALIANEN LEZEN", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "SETTIMANA DAL 2 ALL'8 NOVEMBRE 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "La Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "ITALIAANS WEEKBLAD · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A", 43, "serif", True, INK, anchor="middle")
p.text(975, 372, "TEKSTEN IN HET ITALIAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 20, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "ARRIVA IL PRIMO FREDDO!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "La settimana in cui l'Italia si copre: freddo, piogge e la prima neve in montagna.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "DE EERSTE KOU KOMT ERAAN", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "De week van de eerste kou · zie pagina 2", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "LA NOTIZIA · HET HOOFDNIEUWS", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Arriva il primo freddo: l'Italia si copre e si mette a tavola", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Dalla redazione de La Lucerna · Livello di lettura: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Lunedì 2 novembre l'Italia cambia faccia: arriva il primo freddo vero della stagione, con piogge sul versante adriatico e la prima neve leggera in montagna, intorno ai 1.300–1.500 metri.")
f.para("Le previsioni parlano di un novembre più freddo della media. Non è una certezza, è una probabilità: a pagina 6 impariamo a leggerle senza paura.")
f.para("Il freddo, però, non ferma l'Italia: martedì 3 novembre apre a Milano il Forum Cultura, con più di 50 eventi tra musei e biblioteche, e nel fine settimana il paese si mette a tavola.")
f.para("Sabato 7 e domenica 8 novembre, a Milano, c'è la finale della Coppa del Mondo del Panettone, con pasticceri da 19 paesi; a Cremona apre la Festa del Torrone, fino al 22 novembre.")
f.para("E lo sport chiude la settimana: l'undicesima giornata di Serie A si gioca da venerdì 6 a domenica 8 novembre, con Genoa–Milan, Inter–Como e Fiorentina–Juventus domenica 8 novembre.")
f.para("Questa è la seconda edizione de La Lucerna in italiano: ogni settimana leggiamo l'Italia vera con te. Benvenuti al freddo!")
f.bridge("Uitleg — il primo freddo = eerste kou · il versante adriatico = Adriatische kant · la previsione = prognose · assaggi = proeven.")
f.box("LA SETTIMANA IN CIFRE · IN CIJFERS", [
    ("1.300–1.500 — i metri di quota dove può cadere la prima neve leggera(hoogte van de eerste lichte sneeuw)", "serif", False, INK, 20.5, 1.35),
    ("50+ — gli eventi del Forum Cultura di Milano, dal 3 all'8 novembre(50+ Forum Cultura-evenementen in Milaan)", "serif", False, INK, 20.5, 1.35),
    ("19 — i paesi dei pasticceri alla finale del Panettone a Milano(landen bij de Panettone-finale in Milaan)", "serif", False, INK, 20.5, 1.35),
    ("11ª — la giornata di Serie A del fine settimana(speelronde 11 dit weekend)", "serif", False, INK, 20.5, 1.35),
], tsize=20)
f.head("ADESSO TU · NU JIJ", 25)
f.ex("A2", "Voltooi de zin", "freddo", "il primo freddo = de eerste kou",
     "Lunedì 2 novembre arriva il primo ___ vero della stagione.", size=20, gap=7)
f.ex("A2", "Voltooi de zin", "neve", "la prima neve leggera = eerste lichte sneeuw",
     "In montagna può cadere la prima ___ leggera.", size=20, gap=7)
f.ex("A2", "Voltooi de zin", "Milano", "Forum Cultura en Panettone-finale: allebei in Milaan",
     "Il Forum Cultura apre martedì a ___.", size=20, gap=7)
f.ex("A2", "Voltooi de zin", "Torrone", "Het feest in Cremona heet Festa del Torrone",
     "A Cremona apre la Festa del ___.", size=20, gap=7)
f.ex("A2", "Voltooi de zin", "domenica", "Speelronde 11 sluit op zondag",
     "Genoa–Milan, Inter–Como e Fiorentina–Juventus si giocano ___ 8 novembre.", size=20, gap=7)
f.ex("B1", "Voltooi de zin", "previsioni", "previsioni = voorspellingen (meervoud)",
     "Le ___ parlano di un novembre più freddo della media.", size=20, gap=7)
f.end_report()

# ---- la settimana (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "LA SETTIMANA", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "GIORNO PER GIORNO", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Deze week · Cosa succede, giorno per giorno", 19, "sans", False, GREY)
sett = [
    "LUN 2 — Commemorazione dei defunti; scuole chiuse in alcune regioni.",
    "MAR 3 — Apre il Forum Cultura a Milano; in serata, le coppe europee.",
    "MER–GIO 4–5 — Quarta giornata delle coppe europee.",
    "VEN 6 — Apre l'11ª giornata di Serie A.",
    "SAB 7 — Finale del Panettone a Milano; apre il Torrone a Cremona.",
    "DOM 8 — Serie A, 11ª giornata: le tre grandi di domenica.",
]
byy = gy + 150
for t in sett:
    byy = p.para(gx + 22, byy + 16, t, 20, "serif", False, INK, gw - 44, 1.36) + 6
p.text(gx + 22, byy + 16, "Le date sono quelle del calendario", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "degli eventi; gli orari possono cambiare.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "Data per kalender; tijden kunnen wijzigen.", 16.5, "sans", False, GREY)

# ---- sommario (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "IN QUESTO NUMERO · INHOUD", 24, "sans", True, OLIVE)
som = [
    ("Pag. 2", "Il freddo e il 2 novembre", "A2"),
    ("Pag. 3", "Panettone e torrone", "A2→B1"),
    ("Pag. 4", "La Serie A", "B1"),
    ("Pag. 5", "Dopo Lucca, i giovani", "B1"),
    ("Pag. 6", "Leggere le previsioni", "B2"),
    ("Pag. 7", "Frasi della settimana", "A2→B2"),
    ("Pag. 8", "Esercizi e risposte", "tutti"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- parola della settimana (col 3) ----
my = 1652
p.text(gx, my + 24, "LA PAROLA DELLA SETTIMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "« il primo freddo » : il primo freddo serio dopo un autunno mite. Questa settimana ha un programma: cultura, dolci, calcio.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "Eerste serieuze kou na een milde herfst.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1864, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
p.rect(ix, iy, iw, 320, fill=BOX, stroke=LINE, sw=1.4)
illus_frost(p, ix + iw // 2 - 70, iy + 80, 2.0)
caption(p, ix, iy + 320, iw,
        "Il fiocco di neve: la prima neve leggera può cadere in montagna, intorno ai 1.300–1.500 metri. In pianura, per ora, arriva solo il freddo — e la voglia di dolci caldi. (Pagina 2)",
        "Disegno della redazione")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-freddo")
f2.head("IL FREDDO È ARRIVATO", 25)
f2.para("Giornate più corte, la prima neve in montagna, i musei che aprono le porte e le piazze che profumano di dolci: l'Italia di novembre mostra questa settimana tutto il suo programma.", 22.5)
f2.para("Il suo regalo per i lettori è un weekend di assaggi. Prendilo — e continua a leggere a pagina 2!", 22.5)
f2.end_report()
# col 3 IN BREVE
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "IN BREVE · IN HET KORT", 24, "sans", True, OLIVE)
brefs = [
    ("FREDDO", "Lunedì 2 novembre arriva il primo freddo: piogge adriatiche, neve in montagna. (Pagina 2)"),
    ("CULTURA", "Il Forum Cultura apre martedì 3 novembre: più di 50 eventi. (Pagina 5)"),
    ("DOLCI", "Weekend: finale del Panettone a Milano, Torrone a Cremona. (Pagina 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz lampo ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "QUIZ LAMPO · BLITSQUIZ", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lees de voorpagina en kies het juiste antwoord · Antwoorden op pagina 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "Meerkeuze", "A", "De eerste kou komt op maandag 2 november",
      "Il primo freddo arriva... A. lunedì 2 novembre · B. sabato 7 novembre · C. domenica 1° novembre", size=21)
qf.ex("A2", "Meerkeuze", "B", "Eerste sneeuw rond 1.300–1.500 meter",
      "La prima neve leggera può cadere intorno ai... A. 500 metri · B. 1.300–1.500 metri · C. 3.000 metri", size=21)
qf.ex("A2", "Meerkeuze", "C", "De Panettone-finale is in Milaan",
      "La finale della Coppa del Mondo del Panettone è a... A. Cremona · B. Firenze · C. Milano", size=21)
qf.ex("A2", "Meerkeuze", "B", "Speelronde 11 sluit op zondag",
      "L'undicesima giornata di Serie A chiude... A. venerdì · B. domenica · C. lunedì", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-prima.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VITA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VITA · LEVEN", "La Lucerna", "LIVELLO A2 · Il primo freddo e il 2 novembre · Eerste kou en 2 november")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Il primo freddo: come ci si veste e che cosa si mangia", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: A2")
f.para("Il primo freddo si sente subito: la mattina l'aria è pungente, la sera il buio arriva presto. Allora gli italiani tirano fuori dall'armadio il cappotto, la sciarpa e i guanti. Vestirsi «a strati» è la regola: una maglia, un maglione e, sopra, il cappotto.")
f.para("In casa si accendono i termosifoni. La sera, la cucina profuma di zuppe e di castagne arrosto: il freddo porta con sé i piatti caldi dell'autunno. E al mattino, prima di uscire, tutti guardano il cielo — e il telefono, per le previsioni.")
f.para("Il lunedì di questa settimana è un giorno speciale: il 2 novembre è la Commemorazione dei defunti, il giorno in cui gli italiani ricordano le persone care che non ci sono più. Molti portano i crisantemi al cimitero: è il fiore di novembre.")
f.para("E la scuola? Il 2 novembre è festa in Calabria, Campania, Emilia-Romagna, Sardegna, Sicilia, Umbria, Valle d'Aosta e Trento; in Veneto le scuole sono chiuse dal 30 ottobre al 2 novembre, e a Bolzano la sospensione dura dal 2 all'8 novembre. In altre regioni, invece, è un lunedì normale.")
f.head("E LA SETTIMANA SCORSA?", 25)
f.para("La settimana scorsa si è chiusa con due appuntamenti attesi: la 60ª edizione di Lucca Comics & Games, dal 28 ottobre al 1° novembre, e la festa di Ognissanti, domenica 1° novembre. Quest'anno Ognissanti è caduta di domenica: niente ponte, come avevamo previsto nel VOL.1.", 23.5)
f.para("Anche la manovra, la legge di bilancio, era attesa al voto intorno al 28 ottobre: il punto difficile resta il contributo di banche e assicurazioni. Al momento di andare in stampa, l'esito non era ancora confermato: ne parliamo a pagina 6.", 23.5)
f.bridge("Bij het ter perse gaan was de uitslag nog niet bevestigd — zie pagina 6.")
f.box("LA FRASE PER RICORDARE · EZELSBRUG", [
    ("«Fa freddo, copriti bene!» Così dicono le nonne italiane: quando arriva il primo freddo, il consiglio è uno solo — vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),
], tsize=20)
f.gloss("il cappotto = jas · la sciarpa = sjaal · i guanti = handschoenen · a strati = in laagjes · il termosifone = radiator · il crisantemo = chrysant")
f.end_report()

# col 3: facts + e tu? (sequential, measured)
ix = COLX[3]
facts = ["Il primo freddo porta piogge sul versante adriatico e neve leggera in montagna, intorno ai 1.300–1.500 metri.",
         "Il 2 novembre è la Commemorazione dei defunti: il fiore del giorno è il crisantemo.",
         "In alcune regioni il 2 novembre è festa per le scuole; in altre è un lunedì normale."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LO SAPEVI?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Che cosa metti quando arriva il primo freddo: cappotto, sciarpa o guanti? Scrivi due frasi in italiano e mandale alla redazione: le migliori escono nel VOL.3 (pagina 7, «Lettere dei lettori»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Jas, sjaal of handschoenen? Schrijf twee zinnen in het Italiaans.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU? · EN JIJ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Jas, sjaal of handschoenen? Schrijf twee zinnen in het Italiaans.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Il 2 novembre wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "IL 2 NOVEMBRE · ALLERZIELEN", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Un giorno di memoria, in tutta Italia", 20, "sans", False, GREY, anchor="end")
p.para(MX, dy + 72, "Il 2 novembre, il giorno dopo Ognissanti, gli italiani vanno al cimitero con i crisantemi: fiori bianchi, gialli e viola per ricordare chi non c'è più. È un giorno silenzioso, di famiglia. Le scuole, in molte regioni, restano chiuse — e il lunedì comincia piano, con il primo freddo.", 22.5, "serif", False, INK, RIGHT - MX, 1.45)
p.para(MX, dy + 196, "Attenzione alla parola: «defunto» è una parola gentile per dire «morto». «Commemorazione» vuol dire «ricordo insieme»: si commemora una persona, si ricorda un giorno.", 21, "serif", False, INK, RIGHT - MX, 1.45)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · OEFENINGEN VAN PAGINA 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · Niveaus staan door elkaar: zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · CHE COSA SERVE?", 25)
e.bridge("Vul de zinnen aan in het Italiaans.")
e.ex("A2", "Voltooi de zin", "cappotto", "cappotto = jas",
     "Quando fa freddo, metto il ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "sciarpa", "sciarpa = sjaal",
     "Per il collo, metto la ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "guanti", "guanti = handschoenen (meervoud)",
     "Per le mani, metto i ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "crisantemi", "crisantemi = chrysanten (meervoud)",
     "Il 2 novembre portiamo i ___ al cimitero.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "termosifoni", "termosifoni = radiatoren (meervoud)",
     "In casa si accendono i ___.", instr="Vul in", size=20, gap=8)
e.head("B · IL PRESENTE", 25)
e.bridge("Vul de tegenwoordige tijd van de werkwoorden in.")
e.ex("A2", "Voltooi de zin", "fa", "fare freddo: fa freddo (weer)",
     "La mattina ___ freddo.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "metto", "mettere: io → metto",
     "Io ___ il cappotto prima di uscire.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "portano", "portare: loro → portano",
     "Molti italiani ___ i crisantemi al cimitero.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "guardano", "guardare: loro → guardano",
     "Tutti ___ il cielo prima di uscire.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "resta", "restare: la scuola → resta (lei)",
     "In molte regioni, la scuola ___ chiusa il 2 novembre.", instr="Vul in", size=20, gap=8)
e.head("C · COMPRENSIONE", 25)
e.bridge("Lees het artikel op pagina 2 en kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "2 november is de herdenking",
     "Il 2 novembre è... A. Ognissanti · B. la Commemorazione dei defunti · C. il primo giorno di scuola", size=20, gap=8)
e.ex("A2", "Meerkeuze", "A", "De bloem van 2 november is de chrysant",
     "Il fiore del 2 novembre è... A. il crisantemo · B. la rosa · C. il tulipano", size=20, gap=8)
e.ex("A2", "Meerkeuze", "C", "In laagjes kleden: a strati",
     "Vestirsi «a strati» vuol dire... A. vestirsi di nero · B. vestirsi in fretta · C. mettere più strati, uno sopra l'altro", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Allerheiligen valt dit jaar op zondag, geen lang weekend",
     "Ognissanti, quest'anno, è caduta... A. di lunedì · B. di domenica · C. di sabato", size=20, gap=8)
e.head("D · LE PAROLE DEL FREDDO", 25)
e.match_set("A2", "Woorden koppelen",
            ["il cappotto", "la sciarpa", "il crisantemo", "il termosifone"],
            ["il fiore di novembre, per il 2 novembre",
             "il calorifero di casa, che si accende d'inverno",
             "il vestito lungo e pesante per il freddo",
             "la striscia di lana per il collo"],
            ["c", "d", "a", "b"],
            ["cappotto = warme jas c", "sciarpa = sjaal d", "crisantemo = novemberbloem a", "termosifone = radiator b"],
            instr="Koppel woord en betekenis")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vita.svg")
print("P2 saved, exercises so far:", len(REG))
