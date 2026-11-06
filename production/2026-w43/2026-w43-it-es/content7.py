# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-it-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LINGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LINGUA · LENGUA", "La Lucerna", "Enfoque en la lengua · Tre livelli, tre strumenti · Tres niveles, tres herramientas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · DIRE L'ORA E IL PRESENTE", 24)
a.para("Per dire l'ora: «È l'una», ma «Sono le due, le tre…». «E mezza» è +30 minuti (2:30); «meno un quarto», −15 (2:45).", 21.5)
a.para("E dormire è regolare: dormo, dormi, dorme, dormiamo. Svegliarsi è riflessivo: mi sveglio, si sveglia.", 21.5)
a.expl("Para decir la hora, solo «la una» lleva è; dormire es regular; svegliarsi es un verbo reflexivo.")
a.ex("A2", "Completar", "Sono", "a las diez, Sono: solo la una lleva È",
     "___ le dieci di sera. Comincia il film.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Completar", "dorme", "dormire: lui → dorme",
     "Mio fratello ___ (dormire) fino alle undici domenica.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Completar", "si sveglia", "svegliarsi: lei → si sveglia",
     "Lei ___ (svegliarsi) alle otto.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Opción múltiple", "B", "e mezza = 30 minutos",
     "«Sono le due e mezza» sono le... A. 2:15 · B. 2:30 · C. 2:45", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · IL PASSATO PROSSIMO", 24)
b.para("Per raccontare il weekend usiamo il passato prossimo: ausiliare + participio. Con avere: ho visitato, abbiamo guardato.", 21.5)
b.para("Con essere — per verbi di movimento come andare e arrivare — il participio cambia con la persona: sono andato / sono andata, è iniziata (la fiera).", 21.5)
b.expl("Para contar el fin de semana: passato prossimo; avere + participio, pero essere con los verbos de movimiento (andare, arrivare), con concordancia del participio.")
b.ex("B1", "Completar", "è iniziata", "iniziare lleva essere, femenino: è iniziata",
     "La fiera ___ (iniziare) il 10 ottobre.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Completar", "abbiamo visitato", "visitare lleva avere",
     "Noi ___ (visitare) la mostra mercoledì.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Completar", "è andato", "andare lleva essere: è andato",
     "Marco ___ (andare) alla sagra con gli amici.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Opción múltiple", "B", "arrivare lleva essere + concordancia en plural",
     "I tifosi ___ allo stadio. A. hanno arrivato · B. sono arrivati · C. è arrivati", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · IL CONGIUNTIVO", 24)
c.para("Con «è possibile che», «bisogna che» e «è importante che» usiamo il congiuntivo: slitti (slittare), sia (essere), abbia (avere).", 21.5)
c.para("Ma dopo «so che» e «i giornali scrivono che» resta l'indicativo: il Consiglio si riunisce, la Festa chiude. È la grammatica della pagina 6: opinioni sì, fatti con l'indicativo.", 21.5)
c.expl("Tras è possibile che, bisogna che y è importante che: subjuntivo; tras so che y scrivono che: indicativo.")
c.ex("B2", "Completar", "slitti", "è possibile che + subjuntivo: slitti",
     "È possibile che il voto ___ (slittare) ancora.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Completar", "abbia", "bisogna che + subjuntivo: abbia",
     "Bisogna che ogni cifra ___ (avere) una fonte.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Completar", "chiude", "so che + indicativo: chiude",
     "So che la Festa ___ (chiudere) domenica.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Opción múltiple", "B", "è importante che + subjuntivo: sia",
     "«È importante che il grafico...» A. è chiaro · B. sia chiaro · C. essere chiaro", size=20.5, gap=10)
c.end_report()

# ---- col 3: errori tipici + parola + lettori ----
bx = COLX[3]
errs = [
    ("«Sono le una.»", "→ «È l'una.» Solo l'ora 1:00 usa è; le altre ore usano sono.", "solo la 1:00 lleva è; las demás, sono."),
    ("«Ho andato a Lucca.»", "→ «Sono andato a Lucca.» Andare vuole l'ausiliare essere, non avere.", "andare lleva essere, no avere."),
    ("«Vado a il cinema.»", "→ «Vado al cinema.» A + il si uniscono: al. Anche: del, nel, sul, dal.", "a + il = al; igual: del, nel, sul, dal."),
    ("«La gente sono contenti.»", "→ «La gente è contenta.» Gente è singolare, come un solo gruppo.", "gente es singular, femenino."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 194
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORI TIPICI · ERRORES TÍPICOS", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 26
wt = "« l'anteprima » è la prima volta che il pubblico vede un film. Questa settimana la parola vive a pagina 5: alla Festa del Cinema, molte proiezioni sono anteprime."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("anteprima = preestreno: una película vista por primera vez. Ver página 5.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PAROLA · PALABRA CLAVE", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "anteprima = preestreno: una película vista por primera vez. Ver página 5.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 26
lt = "«Ciao! Sono Li e studio italiano a Pechino. Domenica dormo un'ora in più e poi guardo Inter–Fiorentina. Grazie per il giornale!» — Li (lettera di esempio, scritta dalla redazione)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Carta de ejemplo. En el VOL.2, vuestras cartas y el mejor texto (página 8).", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "LETTERE DEI LETTORI", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Carta de ejemplo. En el VOL.2, vuestras cartas y el mejor texto (página 8).", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frasi della settimana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASI DELLA SETTIMANA · FRASES DE LA SEMANA (TEXTUALES, DE ESTE NÚMERO)", 27, "sans", True, OLIVE)
quotes = [
    ("«alle 03:00 l'orologio torna indietro di un'ora»", "A las 03:00, el reloj se atrasa una hora.", "Pagina 1"),
    ("«È la ricerca numero uno in Italia»", "Es la búsqueda número uno en Italia.", "Pagina 1"),
    ("«L'ora tra le 02:00 e le 03:00 arriva due volte nella stessa notte.»", "La hora de 02:00 a 03:00 llega dos veces en la misma noche.", "Pagina 2"),
    ("«In primavera avanti, in autunno indietro.»", "En primavera se adelanta, en otoño se atrasa.", "Pagina 2"),
    ("«Il re della stagione è il tartufo bianco»", "El rey de la temporada es la trufa blanca.", "Pagina 3"),
    ("«È una partita speciale: è la prima della domenica con l'ora solare.»", "Es un partido especial: el primero del domingo con el horario estándar.", "Pagina 4"),
    ("«Molte sono anteprime: film che il pubblico vede per la prima volta.»", "Muchos son preestrenos: películas que el público ve por primera vez.", "Pagina 5"),
    ("«Un voto previsto non è un voto fatto»", "«Una votación prevista no es una votación hecha».", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- prossima settimana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "LA PROSSIMA SETTIMANA · LA PRÓXIMA SEMANA (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Mercoledì 28 ottobre: il voto sulla manovra a Roma. Dal 28 ottobre al 1° novembre: Lucca Comics & Games, la 60ª edizione. Domenica 1° novembre: Ognissanti — quest'anno cade di domenica, niente ponte. E poi: le vostre lettere e i testi migliori della pagina 8. A lunedì!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
