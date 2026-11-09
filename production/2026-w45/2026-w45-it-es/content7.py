# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LINGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LINGUA　LENGUA", "La Lucerna", "Enfoque: lengua　Tre livelli, tre strumenti　Tres niveles, tres herramientas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　IL TEMPO CHE FA", 24)
a.para("Per il tempo usiamo verbi impersonali, sempre alla terza persona singolare: fa freddo, fa caldo, piove, nevica, c'è vento. Non si dice «sono freddo»: si dice «ho freddo» (io) e «fa freddo» (fuori).", 21.5)
a.para("E per vestirsi: metto il cappotto, metti la sciarpa, mette i guanti. Il verbo è mettere, regolare.", 21.5)
a.bridge("Tiempo impersonal (3.ª persona del singular): ho freddo = tengo frío; fa freddo = hace frío.")
a.ex("A2", "Completar las frases", "piove", "piovere, verbo del tiempo: piove",
     "Oggi ___ (piovere) sul versante adriatico.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Completar las frases", "fa", "fa freddo = hace frío (tiempo)",
     "Fuori ___ freddo: metti il cappotto!", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Completar las frases", "nevica", "nevicare: nevica",
     "In montagna ___ (nevicare) intorno ai 1.500 metri.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Una opción", "B", "«Tengo frío» se dice ho freddo",
     "«Io ho freddo» vuol dire... A. fuori fa freddo · B. io sento freddo · C. nevica", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　IL PASSATO PROSSIMO", 24)
b.para("Per raccontare il freddo usiamo il passato prossimo: ausiliare + participio. Con essere — per verbi come arrivare e andare — il participio cambia con la persona: è arrivato (il freddo), sono andati (i pasticceri).", 21.5)
b.para("Con avere: abbiamo assaggiato, ha aperto. Il participio con avere non cambia.", 21.5)
b.bridge("El pasado se cuenta con el passato prossimo: con essere el participio concuerda; con avere no cambia.")
b.ex("B1", "Completar las frases", "è arrivato", "arrivare con essere: è arrivato",
     "Il primo freddo ___ (arrivare) lunedì.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Completar las frases", "abbiamo assaggiato", "assaggiare con avere",
     "Noi ___ (assaggiare) il torrone a Cremona.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Completar las frases", "sono andati", "andare con essere, plural: sono andati",
     "I pasticceri ___ (andare) a Milano.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Una opción", "B", "aprire con avere + participio invariable",
     "Cremona ___ la Festa del Torrone. A. è aperta · B. ha aperto · C. sono aperti", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　IL CONGIUNTIVO", 24)
c.para("Con «è probabile che», «è possibile che» e «bisogna che» usiamo il congiuntivo: piova (piovere), nevichi (nevicare), sia (essere). È la grammatica della probabilità, la stessa di pagina 6.", 21.5)
c.para("Ma dopo «so che» e «i giornali scrivono che» resta l'indicativo: il freddo arriva, la finale è a Milano. Opinioni sì, fatti con l'indicativo.", 21.5)
c.bridge("Tras è probabile che / è possibile che / bisogna che va subjuntivo; tras so che y scrivono che va indicativo.")
c.ex("B2", "Completar las frases", "piova", "è probabile che + subjuntivo: piova",
     "È probabile che domani ___ (piovere) sul versante adriatico.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Completar las frases", "nevichi", "è possibile che + subjuntivo: nevichi",
     "È possibile che in montagna ___ (nevicare) nel weekend.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Completar las frases", "sia", "bisogna che + subjuntivo: sia",
     "Bisogna che la previsione ___ (essere) chiara per tutti.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Una opción", "B", "so che + indicativo: arriva",
     "«So che il freddo...» A. arrivi · B. arriva · C. arrivare", size=20.5, gap=10)
c.end_report()

# ---- col 3: errori tipici + parola + lettori ----
bx = COLX[3]
errs = [
    ("«Fa freddi.»", "→ «Fa freddo.» Dopo fa, freddo non cambia mai: è invariabile.", "Tras fa, freddo no cambia nunca."),
    ("«Ho nevicato ieri.»", "→ «Ha nevicato ieri.» Nevicare è impersonale: solo la terza persona singolare.", "Nevicare: solo 3.ª persona del singular."),
    ("«Pioverà di sicuro.»", "→ «Potrebbe piovere.» Le previsioni danno probabilità, non certezze.", "Probabilidad, no certeza."),
    ("«La gente sono infreddoliti.»", "→ «La gente è infreddolita.» Gente è singolare, come un solo gruppo.", "Gente es singular femenino."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 194
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORI TIPICI　ERRORES TÍPICOS", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 26
wt = "« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("assaggio = degustación. Página 3: en la final del Panettone se prueba gratis.", "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PAROLA　PALABRA CLAVE", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "assaggio = degustación. Página 3: en la final del Panettone se prueba gratis.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 26
lt = "«Ciao! Sono Li, studio italiano a Pechino. Lunedì metto il cappotto e la sciarpa, sabato assaggio il panettone — almeno in foto!» — Li (esempio della redazione)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Ejemplo de la redacción, no carta real; sin mejor texto de página 8. ¡Escríbenos! Las mejores salen en VOL.3.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "LETTERE DEI LETTORI", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Ejemplo de la redacción, no carta real; sin mejor texto de página 8. ¡Escríbenos! Las mejores salen en VOL.3.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frasi della settimana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "FRASI DELLA SETTIMANA　FRASES DE LA SEMANA (TEXTUALES, DE ESTE NÚMERO)", 27, "sans", True, OLIVE)
quotes = [
    ("«arriva il primo freddo vero della stagione»", "Llega el primer frío de verdad de la temporada.", "Pagina 1"),
    ("«Non è una certezza, è una probabilità»", "No es una certeza, es una probabilidad.", "Pagina 1"),
    ("«il 2 novembre è la Commemorazione dei defunti»", "El 2 de noviembre es la Conmemoración de los Difuntos.", "Pagina 2"),
    ("«Fa freddo, copriti bene!»", "¡Hace frío, abrígate bien!", "Pagina 2"),
    ("«il pubblico può assaggiare gratis»", "El público puede probar gratis.", "Pagina 3"),
    ("«il calcio non si ferma per il primo freddo»", "El fútbol no se detiene por el primer frío.", "Pagina 4"),
    ("«la cultura continua»", "La cultura continúa.", "Pagina 5"),
    ("«Una probabilità alta non è una certezza»", "Una probabilidad alta no es una certeza.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- prossima settimana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "LA PROSSIMA SETTIMANA　LA PRÓXIMA SEMANA (VOL.3)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Lunedì 9 novembre: chiude il Festival dei Popoli a Firenze. La Festa del Torrone continua a Cremona fino al 22 novembre. E poi: le vostre lettere vere e i testi migliori della pagina 8. A lunedì!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
