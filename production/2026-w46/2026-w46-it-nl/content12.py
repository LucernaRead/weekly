# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · PRIMA PAGINA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3 · TERZA EDIZIONE", 23, "sans", True, OLIVE)
p.text(975, 92, "OGNI SETTIMANA IN ITALIANO · ELKE WEEK · HET ITALIAANS DAT DE ITALIANEN LEZEN", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "SETTIMANA DAL 9 AL 15 NOVEMBRE 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "La Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "ITALIAANS WEEKBLAD · VOL.3 · SAN MARTINO · IL VINO NUOVO · L'ITALIA", 43, "serif", True, INK, anchor="middle")
p.text(975, 372, "TEKSTEN IN HET ITALIAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 20, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "SAN MARTINO, IL VINO NUOVO!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Tre giorni di sole, castagne e cantine aperte: l'autunno italiano si assaggia.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "Deze week is Sint-Maartensweek", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "De Sint-Maartensweek · Zie pagina 2", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "LA NOTIZIA · HET HOOFDNIEUWS", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "San Martino porta il vino nuovo: l'Italia assaggia l'autunno", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Dalla redazione de La Lucerna · Livello di lettura: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Mercoledì 11 novembre è San Martino: secondo il proverbio, «a San Martino ogni mosto diventa vino». Si aprono le cantine, si assaggia il vino nuovo e si mangiano le castagne: è l'estate di San Martino, tre giorni di sole dopo il primo freddo.")
f.para("La leggenda racconta che Martino, soldato romano, divise il suo mantello con un mendicante infreddolito — e il sole tornò a splendere: un'estate breve, «tre giorni e un pochino», nel cuore di novembre.")
f.para("Lunedì 9 novembre c'è l'Eurogruppo a Bruxelles; ieri si è chiuso a Firenze il Festival dei Popoli: 86 film, dal 31 ottobre all'8 novembre.")
f.para("Giovedì 12 novembre l'Italia gioca con la Francia a San Siro; domenica 15 novembre chiude il girone a Bruxelles, con il Belgio. Due notti azzurre, alle 20.45.")
f.para("E il fine settimana è dolce: venerdì 13 novembre apre a Perugia Eurochocolate, fino al 22 novembre; a Cremona continua la Festa del Torrone, fino al 22 novembre.")
f.para("Questa è la terza edizione de La Lucerna in italiano. Benvenuti a San Martino!")
f.bridge("Uitleg — l'estate di San Martino: de zomer van Sint-Maarten · il mosto most/nieuwe wijn · la cantina wijnkelder · assaggiare proeven.")
f.box("LA SETTIMANA IN CIFRE", [
    ("11 — november, Sint-Maartensdag, woensdag (Sint-Maarten, wo. 11 november)", "serif", False, INK, 20.5, 1.35),
    ("20.45 — aftrap van de twee azzurre-avonden, donderdag en zondag (aftrap van de twee interlands)", "serif", False, INK, 20.5, 1.35),
    ("32e — editie van Eurochocolate in Perugia, vanaf 13 november (32e Eurochocolate, Perugia)", "serif", False, INK, 20.5, 1.35),
    ("29e — editie van de Festa del Torrone in Cremona (29e Torrone-feest, Cremona)", "serif", False, INK, 20.5, 1.35),
])
f.head("ADESSO TU · NU JIJ", 25)
f.ex("A2", "Voltooi de zin", "San Martino", "Sint-Maarten is op 11 november",
     "Mercoledì 11 novembre è ___.", size=20, gap=7)
f.ex("A2", "Voltooi de zin", "mosto", "mosto = most/nieuwe wijn",
     "A San Martino ogni ___ diventa vino.", size=20, gap=7)
f.ex("A2", "Voltooi de zin", "cantine", "cantine = wijnkelders (meervoud)",
     "In tutta Italia si aprono le ___.", size=20, gap=7)
f.ex("A2", "Voltooi de zin", "Francia", "Donderdag: Italië–Frankrijk",
     "Giovedì 12 novembre l'Italia gioca con la ___.", size=20, gap=7)
f.ex("A2", "Voltooi de zin", "Perugia", "Chocoladefestival in Perugia",
     "Eurochocolate apre venerdì a ___.", size=20, gap=7)
f.ex("B1", "Voltooi de zin", "Torrone", "Het feest in Cremona heet Festa del Torrone",
     "A Cremona continua la Festa del ___.", size=20, gap=7)
f.end_report()

# ---- la settimana (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "LA SETTIMANA", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "GIORNO PER GIORNO", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Deze week · Cosa succede, giorno per giorno", 19, "sans", False, GREY)
sett = [
    "LUN 9 — Eurogruppo a Bruxelles; il Festival dei Popoli si è chiuso ieri.",
    "MAR 10 — Cantine Aperte a San Martino: il vino nuovo si assaggia.",
    "MER 11 — San Martino: mosto, castagne e l'estate di tre giorni.",
    "GIO 12 — Italia–Francia a San Siro, Nations League, ore 20.45.",
    "VEN 13 — Apre Eurochocolate a Perugia; a Torino, la notte del tennis.",
    "SAB–DOM 14–15 — Torrone a Cremona; Belgio–Italia domenica sera.",
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
    ("Pag. 2", "San Martino e il vino nuovo", "A2"),
    ("Pag. 3", "Torrone e cioccolato", "A2→B1"),
    ("Pag. 4", "Le notti azzurre", "B1"),
    ("Pag. 5", "I giovani leggono", "B1"),
    ("Pag. 6", "La manovra spiegata", "B2"),
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
y2 = p.para(gx, my + 76, "« l'estate di San Martino » : tre giorni miti dopo il primo freddo, con il sole della leggenda del mantello diviso.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "«De zomer van Sint-Maarten»: drie milde dagen.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1864, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
p.rect(ix, iy, iw, 320, fill=BOX, stroke=LINE, sw=1.4)
illus_frost(p, ix + iw // 2 - 70, iy + 80, 2.0)
caption(p, ix, iy + 320, iw,
        "Il fiocco di neve e il sole di San Martino: il primo freddo è arrivato, ma la tradizione promette tre giorni miti — «tre giorni e un pochino». (Pagina 2)",
        "Disegno della redazione")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-freddo")
f2.head("IL SOLE DI NOVEMBRE", 25)
f2.para("Giornate più corte, le cantine aperte, le piazze che profumano di castagne: l'Italia di novembre mostra questa settimana il suo autunno più dolce.", 22.5)
f2.para("Il suo regalo per i lettori è un bicchiere di vino nuovo — da assaggiare, non da bere in fretta. Prendilo — e continua a leggere a pagina 2!", 22.5)
f2.end_report()
# col 3 IN BREVE
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "IN BREVE · IN HET KORT", 24, "sans", True, OLIVE)
brefs = [
    ("FESTIVAL", "Il Festival dei Popoli si è chiuso domenica 8 novembre: 86 film a Firenze. (Pagina 2)"),
    ("MANOVRA", "Il Consiglio dei ministri ha approvato il disegno di legge il 28 ottobre: non è ancora legge. (Pagina 6)"),
    ("RICERCA", "I Giorni della Ricerca AIRC durano fino al 15 novembre. (Pagina 4)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.30) + 8

# ---- quiz lampo ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "QUIZ LAMPO · BLITSQUIZ", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lees de voorpagina en kies het juiste antwoord · Antwoorden op pagina 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "Meerkeuze", "A", "Sint-Maarten is woensdag 11 november",
      "San Martino è... A. mercoledì 11 novembre · B. sabato 14 novembre · C. domenica 1° novembre", size=21)
qf.ex("A2", "Meerkeuze", "B", "De Sint-Maartenslegende: de gedeelde mantel",
      "La leggenda di San Martino racconta... A. un viaggio · B. un mantello diviso · C. una gara", size=21)
qf.ex("A2", "Meerkeuze", "C", "Italië–Frankrijk in San Siro",
      "Italia–Francia si gioca... A. a Bruxelles · B. a Perugia · C. a San Siro", size=21)
qf.ex("A2", "Meerkeuze", "B", "Chocoladefestival opent in Perugia",
      "Eurochocolate apre... A. a Cremona · B. a Perugia · C. a Firenze", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-prima.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VITA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VITA · LEVEN", "La Lucerna", "LIVELLO A2 · San Martino e il vino nuovo · Sint-Maarten en nieuwe wijn")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("San Martino in casa e in cantina: vino nuovo, castagne, oca", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: A2")
f.para("San Martino si sente a tavola: le castagne arrosto scaldano le mani, il vino nuovo si assaggia nelle cantine e, in molte case, si prepara l'oca arrosto. È la festa dell'autunno che diventa inverno, con il profumo del mosto che diventa vino.")
f.para("La leggenda è semplice e bella: Martino, soldato romano, incontra un mendicante che trema di freddo e divide con lui il mantello. La notte dopo, racconta la tradizione, il sole torna: per tre giorni fa quasi estate. «L'estate di San Martino dura tre giorni e un pochino», dice il proverbio.")
f.para("Un tempo, l'11 novembre era anche un giorno di traslochi: «fare San Martino» voleva dire cambiare casa, perché molti contratti di lavoro nei campi finivano in autunno. Oggi la parola resta, e le feste di paese restano: fiere, bancarelle, oca e castagne in tutta Italia.")
f.para("E le cantine? Dal 1° al 15 novembre, con Cantine Aperte a San Martino, le aziende aprono le porte: visite, degustazioni e incontri con chi il vino lo fa. Sulle colline del Prosecco, patrimonio UNESCO, il vino nuovo si assaggia dove nasce, tra i vigneti gialli di novembre.")
f.head("E LA SETTIMANA SCORSA?", 25)
f.para("La settimana scorsa si è chiusa con il Festival dei Popoli a Firenze: la 67ª edizione, dal 31 ottobre all'8 novembre, con 86 film di cinema documentario e il tema «Il cinema che sceglie da che parte stare». Il 4 novembre, nel sessantesimo anniversario dell'alluvione di Firenze, è stato presentato «Angeli del fango».", 23.5)
f.para("Nello stesso weekend si è chiuso il Forum Cultura di Milano, con più di 50 eventi, e si sono aperte la finale del Panettone e la Festa del Torrone. Anche la manovra, la legge di bilancio, ha fatto un passo: il Consiglio dei ministri ha approvato il disegno di legge il 28 ottobre. Al momento di andare in stampa, il testo non era ancora legge: ne parliamo a pagina 6.", 23.5)
f.bridge("Bij het ter perse gaan was de begroting nog geen wet — zie pagina 6.")
f.box("LA FRASE PER RICORDARE", [
    ("«A San Martino ogni mosto diventa vino.» Così dice il proverbio: l'11 novembre il mosto è pronto, e il vino nuovo si assaggia.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("il mosto most/nieuwe wijn · la cantina wijnkelder · la castagna kastanje · l'oca gans · il mantello mantel · traslocare verhuizen.")
f.end_report()

# col 3: facts + e tu? (sequential, measured)
ix = COLX[3]
facts = ["L'11 novembre è San Martino: il proverbio dice che ogni mosto diventa vino.",
         "La leggenda del mantello diviso spiega l'estate di tre giorni.",
         "Cantine Aperte a San Martino: dal 1° al 15 novembre, vino nuovo nelle cantine."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LO SAPEVI?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Hai mai assaggiato il vino nuovo o le castagne arrosto? Scrivi due frasi in italiano e mandale alla redazione: le migliori escono nel VOL.4 (pagina 7, «Lettere dei lettori»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Heb je nieuwe wijn of geroosterde kastanjes geproefd? Schrijf twee zinnen in het Italiaans aan de redactie.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU? · EN JIJ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Heb je nieuwe wijn of geroosterde kastanjes geproefd? Schrijf twee zinnen in het Italiaans aan de redactie.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Il 11 novembre wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "L'11 NOVEMBRE · Sint-Maarten", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Un santo, un mantello, tre giorni di sole", 20, "sans", False, GREY, anchor="end")
p.para(MX, dy + 72, "Martino di Tours visse nel IV secolo: soldato romano, poi vescovo. La sua festa è l'11 novembre, il giorno della sua sepoltura, nel 397. La leggenda del mantello diviso è diventata un'immagine dell'autunno europeo: un gesto di generosità, e il sole che torna per tre giorni.", 22.5, "serif", False, INK, RIGHT - MX, 1.45)
p.para(MX, dy + 196, "Attenzione alla parola: «mosto» è il succo d'uva prima che diventi vino. «Fare San Martino», invece, è un modo di dire antico: vuol dire traslocare, cambiare casa.", 21, "serif", False, INK, RIGHT - MX, 1.45)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · OEFENINGEN VAN PAGINA 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · Niveaus staan door elkaar: zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · CHE COSA SERVE?", 25)
e.bridge("Vul de zinnen aan in het Italiaans.")
e.ex("A2", "Voltooi de zin", "mosto", "mosto = most/nieuwe wijn",
     "A San Martino ogni ___ diventa vino.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "cantina", "cantina = wijnkelder",
     "Il vino nuovo si assaggia in ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "castagne", "castagne = kastanjes (meervoud)",
     "A San Martino si mangiano le ___ arrosto.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "mantello", "mantello = mantel",
     "Martino divide il suo ___ con il mendicante.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "oca", "oca = gans",
     "In molte case si prepara l'___ arrosto.", instr="Vul in", size=20, gap=8)
e.head("B · IL PRESENTE", 25)
e.bridge("Vul de tegenwoordige tijd van de werkwoorden in.")
e.ex("A2", "Voltooi de zin", "divide", "dividere: Martino → divide",
     "Martino ___ il mantello con il mendicante.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "assaggiamo", "assaggiare: noi → assaggiamo",
     "Noi ___ il vino nuovo in cantina.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "aprono", "aprire: le cantine → aprono",
     "Le cantine ___ le porte a novembre.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "mangiamo", "mangiare: noi → mangiamo",
     "Noi ___ le castagne arrosto.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "dura", "durare: l'estate → dura (zij)",
     "L'estate di San Martino ___ tre giorni e un pochino.", instr="Vul in", size=20, gap=8)
e.head("C · COMPRENSIONE", 25)
e.bridge("Lees het artikel op pagina 2 en kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "De Sint-Maartenslegende: de gedeelde mantel",
     "La leggenda di San Martino racconta... A. un viaggio · B. un mantello diviso · C. una gara", size=20, gap=8)
e.ex("A2", "Meerkeuze", "A", "«fare San Martino» betekende vroeger verhuizen",
     "«Fare San Martino», un tempo, voleva dire... A. traslocare · B. vendemmiare · C. viaggiare", size=20, gap=8)
e.ex("A2", "Meerkeuze", "C", "Wijnkelders open tot 15 november",
     "Cantine Aperte a San Martino dura fino al... A. 7 novembre · B. 11 novembre · C. 15 novembre", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Festival dei Popoli: 86 films",
     "Il Festival dei Popoli ha presentato... A. 50 film · B. 86 film · C. 19 film", size=20, gap=8)
e.head("D · LE PAROLE DI SAN MARTINO", 25)
e.match_set("A2", "Woorden koppelen",
            ["il mosto", "la cantina", "il mantello", "traslocare"],
            ["il luogo dove si fa e si conserva il vino",
             "cambiare casa, andare a vivere altrove",
             "il succo d'uva prima che diventi vino",
             "la lunga veste che protegge dal freddo"],
            ["c", "a", "d", "b"],
            ["mosto=most/nieuwe wijn c", "cantina=wijnkelder a", "mantello=mantel d", "traslocare=verhuizen b"],
            instr="Koppel woord en betekenis")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vita.svg")
print("P2 saved, exercises so far:", len(REG))
