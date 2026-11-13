# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-it-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · PRIMA PAGINA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 4　QUARTA EDIZIONE", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "OGNI SETTIMANA IN ITALIANO　CADA SEMANA　EL ITALIANO QUE LEE ITALIA", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "SETTIMANA DAL 16 AL 22 NOVEMBRE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "La Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SEMANARIO ITALIANO　VOL.4　LA SERIE A　IL TORRONE　VENEZIA", 36, "serif", True, OLIVE, anchor="middle", spacing=11.0)
p.text(975, 372, "IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "LA LAZIO RESTA PRIMA!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Lazio 29 punti, Inter e Roma inseguono: la Serie A racconta l'11ª giornata.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "Esta semana: jornada 11 de la Serie A", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "La Lazio lidera con 29 puntos　Ver página 4", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "LA NOTIZIA　LA NOTICIA", 22, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "La Lazio resta in vetta: Inter e Roma inseguono", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Dalla redazione de La Lucerna　Livello di lettura: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("La Lazio è ancora prima: dopo il pareggio 1–1 a Napoli, la prima della classe ha 29 punti ed è ancora imbattuta. L'Inter vince 2–0 con il Como e sale a 28 punti, la Roma batte 3–0 il Sassuolo e arriva a 27.")
f.para("L'11ª giornata, giocata dal 6 all'8 novembre, ha portato ventiquattro gol in dieci partite. Il Milan vince 2–1 a Genova e prende il quarto posto, con 24 punti; Fiorentina e Juventus chiudono 2–2. In coda, l'Udinese è ultima, con 5 punti.")
f.para("Sabato 21 novembre torna la Serie A con la 12ª giornata: domenica sera, a Bergamo, c'è Atalanta–Inter. Sabato 21 la Lazio capolista gioca in casa con il Lecce.")
f.para("E domenica 22 novembre è anche il giorno dei dolci: a Cremona chiude la Festa del Torrone, con il corteo storico e la rievocazione del matrimonio Sforza–Visconti; a Perugia chiude Eurochocolate, con il maestro Iginio Massari.")
f.para("A Torino, domenica 22 novembre, si gioca la finale delle Nitto ATP Finals: otto campioni, una settimana di tennis, e l'Italia con Flavio Cobolli. A Venezia, sabato 21, c'è la Madonna della Salute.")
f.para("Questa è la quarta edizione de La Lucerna in italiano. Benvenuti in una settimana di calcio, dolci e musica!")
f.bridge("Nota — la vetta, la cima / el liderato · imbattuto, invicto · il capolista, el líder · chiudere, cerrar.")
f.box("LA SETTIMANA IN CIFRE　EN CIFRAS", [  # D5 (2026-11-12): subtitle shortened LA SEMANA EN CIFRAS -> EN CIFRAS (full title needed 14.5pt to fit); tsize 19.5 fits
    ("29 — los puntos de la Lazio, primera tras 11 jornadas (la Lazio lidera)", "serif", False, INK, 20.5, 1.35),
    ("24 — los goles de la jornada 11, en diez partidos (24 goles en 10 partidos)", "serif", False, INK, 20.5, 1.35),
    ("20.45 — la hora del Atalanta–Inter, domingo 22 de noviembre (20:45)", "serif", False, INK, 20.5, 1.35),
    ("más de 150 — los figurantes del desfile de clausura (más de 150 figurantes)", "serif", False, INK, 20.5, 1.35),
], tsize=19.5)
f.head("ADESSO TU　AHORA TE TOCA A TI", 22.5)  # D5 (2026-11-12): was 25, head ran +40.2px past the column (HEAD TOO WIDE); 22.5 fits
f.ex("A2", "Completa la frase", "Lazio", "La Lazio es líder",
     "La prima in classifica è la ___.", size=20, gap=7)
f.ex("A2", "Completa la frase", "Napoli", "La Lazio empató en Nápoles",
     "La Lazio pareggia 1–1 a ___.", size=20, gap=7)
f.ex("A2", "Completa la frase", "Como", "El Inter ganó 2–0 al Como",
     "L'Inter vince 2–0 con il ___.", size=20, gap=7)
f.ex("A2", "Completa la frase", "Sassuolo", "La Roma ganó 3–0 al Sassuolo",
     "La Roma batte 3–0 il ___.", size=20, gap=7)
f.ex("A2", "Completa la frase", "Bergamo", "El Atalanta–Inter es en Bérgamo",
     "Atalanta–Inter si gioca a ___.", size=20, gap=7)
f.ex("B1", "Completa la frase", "Cremona", "La fiesta del Torrone cierra en Cremona",
     "La Festa del Torrone chiude a ___.", size=20, gap=7)
f.end_report()

# ---- la settimana (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "LA SETTIMANA", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "GIORNO PER GIORNO", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Esta semana　Cosa succede, giorno per giorno", 18, "sans", False, GREY)  # D5 (2026-11-12): was 19, line ran +6.6px past the box (pre-D5 +12.6px); 18 fits
sett = [
    "LUN 16 — Manovra in Parlamento: emendamenti entro il 17, ore 18.",
    "MAR 17 — Scade il termine per gli emendamenti.",
    "GIO 19 — A Torino proseguono le Nitto ATP Finals.",
    "VEN 20 — A Perugia, Eurochocolate: «I tesori della Calabria Straordinaria», ore 18.15.",
    "SAB 21 — Madonna della Salute a Venezia; torna la Serie A.",
    "DOM 22 — Chiudono Torrone ed Eurochocolate; finale ATP; Atalanta–Inter.",
]
byy = gy + 148
for t in sett:
    byy = p.para(gx + 22, byy + 16, t, 19, "serif", False, INK, gw - 44, 1.36) + 2
byy = p.para(gx + 22, byy + 16, "Le date sono quelle degli eventi; gli orari possono cambiare.", 18.5, "sans", False, GREY, gw - 44, 1.36) + 4
p.para(gx + 22, byy + 2, "Las fechas siguen el calendario de cada evento; los horarios pueden cambiar.", 16.5, "sans", False, GREY, gw - 44, 1.35)
print("P1 settimana ends", byy)

# ---- sommario (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill=BOX)
p.text(gx + 22, sy + 40, "IN QUESTO NUMERO　SUMARIO", 22.5, "sans", True, OLIVE)  # D5 (2026-11-12): was 24, title ran +21.9px past the box; 22.5 fits
som = [
    ("Pag. 2", "Venezia e gli alberi", "A2"),
    ("Pag. 3", "Torrone e cioccolato", "A2→B1"),
    ("Pag. 4", "La Serie A e il tennis", "B1"),
    ("Pag. 5", "I giovani leggono", "B1"),
    ("Pag. 6", "La manovra in Parlamento", "B2"),
    ("Pag. 7", "Frasi della settimana", "A2→B2"),
    ("Pag. 8", "Esercizi e risposte", "tutti"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- parola della settimana (col 3) ----
my = 1652
p.text(gx, my + 24, "LA PAROLA DELLA SETTIMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
y2 = p.para(gx, my + 76, "« la vetta » : il primo posto in classifica. La Lazio è in vetta con 29 punti.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "«la vetta»: la cabeza de la tabla. La Lazio lidera con 29 puntos.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1864, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "stadio.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Un vecchio stadio italiano: il calcio si gioca da più di cent'anni, e ogni domenica gli stadi si riempiono di tifosi. (Pagina 4)",
        "Foto: Wikimedia Commons — dominio pubblico")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-domenica")
f2.head("LA DOMENICA DEL 22", 25)
f2.para("Domenica 22 novembre è una giornata da ricordare: a Cremona il corteo del Torrone, a Perugia il cioccolato, a Torino la finale del tennis e a Bergamo la grande partita della sera.", 22.5)
f2.para("Il consiglio della redazione: scegliete una festa, guardate una partita — e continuate a leggere a pagina 2!", 22.5)
f2.end_report()
# col 3 IN BREVE
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX)
p.text(bx + 22, 1914, "IN BREVE　EN BREVE", 24, "sans", True, OLIVE)
brefs = [
    ("TORRONE", "La Festa del Torrone chiude domenica 22 novembre a Cremona. (Pagina 3)"),
    ("MANOVRA", "Audizioni in Parlamento dal 9 al 12 novembre; emendamenti entro martedì 17. (Pagina 6)"),
    ("TENNIS", "Nitto ATP Finals a Torino, dal 15 al 22 novembre. (Pagina 4)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.30) + 8

# ---- quiz lampo ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "QUIZ LAMPO　QUIZ RELÁMPAGO", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lee la portada y elige la respuesta correcta　Respuestas en la página 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "Opción múltiple", "A", "La Lazio lidera con 29 puntos",
      "La prima in classifica è... A. la Lazio · B. l'Inter · C. la Roma", size=21)
qf.ex("A2", "Opción múltiple", "B", "24 goles en la jornada 11",
      "L'11ª giornata ha portato... A. 10 gol · B. 24 gol · C. 31 gol", size=21)
qf.ex("A2", "Opción múltiple", "C", "El Atalanta–Inter es en Bérgamo",
      "Atalanta–Inter si gioca... A. a Torino · B. a Milano · C. a Bergamo", size=21)
qf.ex("A2", "Opción múltiple", "B", "La fiesta del Torrone cierra en Cremona",
      "La Festa del Torrone chiude... A. a Perugia · B. a Cremona · C. ad Alba", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-prima.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VITA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VITA　VIDA COTIDIANA", "La Lucerna", "LIVELLO A2　Venezia, gli alberi e la musica　Venecia, los árboles y la música")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Venezia prega, l'Italia pianta alberi: il 21 novembre", 37)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: A2")
f.para("Sabato 21 novembre Venezia celebra la festa della Madonna della Salute. I veneziani attraversano il ponte votivo sul Canal Grande per arrivare alla Basilica di Santa Maria della Salute: un ponte di barche, costruito per un giorno, per una festa che dura da quasi quattrocento anni.")
f.para("La festa nasce da un voto del 1630, durante la peste: la città promise una chiesa alla Madonna se la peste finiva. La basilica, disegnata da Baldassarre Longhena, fu costruita tra il 1631 e il 1687. Ancora oggi, il 21 novembre, i fedeli portano candele accese e pregano per la salute della famiglia.")
f.para("A tavola, il piatto della festa è la castradina: carne di montone salata e affumicata, cotta a lungo con le verze. La tradizione dice che si mangia la sera prima, il 20 novembre, in famiglia. È il piatto della tradizione veneziana.")
f.para("Lo stesso giorno, il 21 novembre, in tutta Italia è la Giornata nazionale degli alberi: una festa nata nel 1898 come festa dell'albero, oggi una giornata per piantare alberi e per pensare al verde delle città. E domenica 22 novembre è Santa Cecilia, la patrona della musica e dei musicisti.")
f.head("E LA SETTIMANA SCORSA?", 25)
f.para("La settimana scorsa si è chiusa con due feste dolci ancora aperte: la Festa del Torrone a Cremona e Eurochocolate a Perugia, che chiudono domenica 22 novembre. E due grandi appuntamenti di sport: le due notti azzurre della Nazionale e l'inizio delle Nitto ATP Finals a Torino.", 23.5)
f.para("Anche la manovra, la legge di bilancio, ha fatto un passo: dal 9 al 12 novembre le commissioni Bilancio di Camera e Senato hanno ascoltato enti e istituzioni. Al momento di andare in stampa, il testo non era ancora legge: ne parliamo a pagina 6.", 23.5)
f.bridge("Al cierre de esta edición, el proyecto de presupuestos aún no era ley — ver página 6.")
f.box("LA FRASE PER RICORDARE　RECORDAR", [  # D5 (2026-11-12): subtitle shortened PARA RECORDAR -> RECORDAR (full title needed 16pt to fit); tsize 18.5 fits
    ("«La salute è la prima ricchezza.» A Venezia, il 21 novembre, la parola «salute» vuol dire salute del corpo e della famiglia.", "serif", False, INK, 21.5, 1.4),
], tsize=18.5)
f.gloss("la salute, la salud · il ponte votivo, el puente votivo · la candela, la vela · la peste, la peste · il voto, el voto · piantare, plantar.")
f.end_report()

# col 3: salute image + facts + e tu? (sequential)
ix = COLX[3]
image(p, "salute.jpg", ix, 200, CW, 270)
cy3 = caption(p, ix, 470, CW, "Venezia, il Molo e la Basilica della Salute: il 21 novembre i veneziani attraversano il ponte votivo per pregare.",
              "Foto: Canaletto — Wikimedia Commons, dominio pubblico")
facts = ["21 novembre: Madonna della Salute a Venezia, con il ponte di barche sul Canal Grande.",
         "21 novembre: Giornata nazionale degli alberi in tutta Italia.",
         "22 novembre: Santa Cecilia, patrona della musica e dei musicisti."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LO SAPEVI?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Hai mai attraversato un ponte votivo o piantato un albero? Scrivi due frasi in italiano e mandale alla redazione: le migliori escono nel VOL.5 (pagina 7, «Lettere dei lettori»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("¿Has cruzado alguna vez un puente votivo o plantado un árbol? Escribe dos frases en italiano a la redacción.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU?　¿Y TÚ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "¿Has cruzado alguna vez un puente votivo o plantado un árbol? Escribe dos frases en italiano a la redacción.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Il 21 novembre wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "IL 21 NOVEMBRE　21 DE NOVIEMBRE", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Una festa, una giornata verde", 20, "sans", False, GREY, anchor="end")
p.para(MX, dy + 72, "Il 21 novembre è un giorno con due facce: a Venezia si prega per la salute, in tutta Italia si piantano alberi. La prima è una festa antica, nata da un voto del 1630; la seconda è una giornata giovane, nata come festa dell'albero nel 1898 e diventata giornata nazionale con una legge del 2013.", 22.5, "serif", False, INK, RIGHT - MX, 1.45)
p.para(MX, dy + 196, "Attenzione alla parola: «salute» vuol dire salute, stare bene. «La Madonna della Salute» è la Madonna che protegge la salute. E «piantare» vuol dire mettere una pianta nella terra.", 21, "serif", False, INK, RIGHT - MX, 1.45)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　EJERCICIOS PÁGINA 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8　Los niveles se mezclan: busca por número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　CHE COSA SERVE?", 25)
e.bridge("Completa las frases en italiano.")
e.ex("A2", "Completa la frase", "Salute", "la Madonna della Salute",
     "A Venezia il 21 novembre è la festa della Madonna della ___.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completa la frase", "ponte", "el puente votivo",
     "I veneziani attraversano il ___ votivo sul Canal Grande.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completa la frase", "candele", "velas (plural)",
     "I fedeli portano ___ accese in basilica.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completa la frase", "alberi", "árboles (plural)",
     "Il 21 novembre in tutta Italia si piantano gli ___.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completa la frase", "musica", "Santa Cecilia es la patrona de la música",
     "Santa Cecilia è la patrona della ___.", instr="Completa", size=20, gap=8)
e.head("B　IL PRESENTE", 25)
e.bridge("Completa con el presente.")
e.ex("A2", "Completa la frase", "attraversano", "attraversare:i veneziani → attraversano",
     "I veneziani ___ il ponte votivo.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completa la frase", "portano", "portare:i fedeli → portano",
     "I fedeli ___ candele accese.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completa la frase", "piantiamo", "piantare:noi → piantiamo",
     "Noi ___ un albero nel giardino della scuola.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completa la frase", "prega", "pregare:la famiglia → prega",
     "La famiglia ___ per la salute.", instr="Completa", size=20, gap=8)
e.ex("A2", "Completa la frase", "mangia", "mangiare:la famiglia → mangia",
     "La famiglia ___ la castradina la sera prima.", instr="Completa", size=20, gap=8)
e.head("C　COMPRENSIONE", 25)
e.bridge("Lee el artículo de la página 2 y elige la respuesta correcta.")
e.ex("A2", "Opción múltiple", "B", "El puente votivo está sobre el canal",
     "Il ponte votivo è... A. di pietra · B. sul Canal Grande · C. in montagna", size=20, gap=8)
e.ex("A2", "Opción múltiple", "A", "La Madonna della Salute nace de un voto de 1630",
     "La festa nasce da un voto del... A. 1630 · B. 1687 · C. 1898", size=20, gap=8)
e.ex("A2", "Opción múltiple", "C", "El día de los árboles es el 21 de noviembre",
     "La Giornata nazionale degli alberi è il... A. 22 novembre · B. 20 novembre · C. 21 novembre", size=20, gap=8)
e.ex("B1", "Opción múltiple", "B", "Santa Cecilia es la patrona de la música",
     "Santa Cecilia è la patrona... A. dei marinai · B. della musica · C. degli alberi", size=20, gap=8)
e.head("D　LE PAROLE DI VENEZIA", 25)
e.match_set("A2", "Relaciona las palabras",
            ["la salute", "il ponte votivo", "la candela", "piantare"],
            ["mettere una pianta nella terra",
             "il ponte di barche per la festa in novembre",
             "stare bene, la prima ricchezza",
             "la piccola luce di cera accesa in chiesa"],
            ["c", "b", "d", "a"],
            ["salute = la salud, c", "ponte votivo = puente votivo, b", "candela = vela, d", "piantare = plantar, a"],
            instr="Relaciona las palabras")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vita.svg")
print("P2 saved, exercises so far:", len(REG))
