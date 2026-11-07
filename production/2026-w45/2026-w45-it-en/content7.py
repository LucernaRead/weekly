# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-it-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LINGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LINGUA · Language", "La Lucerna", "Language focus · Tre livelli, tre strumenti · Three levels, three tools")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · IL TEMPO CHE FA", 24)
a.para("Per il tempo usiamo verbi impersonali, sempre alla terza persona singolare: fa freddo, fa caldo, piove, nevica, c'è vento. Non si dice «sono freddo»: si dice «ho freddo» (io) e «fa freddo» (fuori).", 21.5)
a.para("E per vestirsi: metto il cappotto, metti la sciarpa, mette i guanti. Il verbo è mettere, regolare.", 21.5)
a.bridge("Weather uses impersonal verbs (third person singular): ‘I am cold’ is ho freddo, ‘it is cold outside’ is fa freddo.")
a.ex("A2", "完成句子", "piove", "piovere, weather verb: piove",
     "Oggi ___ (piovere) sul versante adriatico.", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "完成句子", "fa", "fa freddo = the weather is cold",
     "Fuori ___ freddo: metti il cappotto!", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "完成句子", "nevica", "nevicare: nevica",
     "In montagna ___ (nevicare) intorno ai 1.500 metri.", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "单选", "B", "‘I am cold’ is ho freddo",
     "«Io ho freddo» vuol dire... A. fuori fa freddo · B. io sento freddo · C. nevica", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · IL PASSATO PROSSIMO", 24)
b.para("Per raccontare il freddo usiamo il passato prossimo: ausiliare + participio. Con essere — per verbi come arrivare e andare — il participio cambia con la persona: è arrivato (il freddo), sono andati (i pasticceri).", 21.5)
b.para("Con avere: abbiamo assaggiato, ha aperto. Il participio con avere non cambia.", 21.5)
b.bridge("For the past use the passato prossimo: arrivare/andare take essere and the participle agrees; with avere it never changes.")
b.ex("B1", "完成句子", "è arrivato", "arrivare takes essere: è arrivato",
     "Il primo freddo ___ (arrivare) lunedì.", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "完成句子", "abbiamo assaggiato", "assaggiare takes avere",
     "Noi ___ (assaggiare) il torrone a Cremona.", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "完成句子", "sono andati", "andare takes essere, plural sono andati",
     "I pasticceri ___ (andare) a Milano.", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "单选", "B", "aprire takes avere + invariable participle",
     "Cremona ___ la Festa del Torrone. A. è aperta · B. ha aperto · C. sono aperti", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · IL CONGIUNTIVO", 24)
c.para("Con «è probabile che», «è possibile che» e «bisogna che» usiamo il congiuntivo: piova (piovere), nevichi (nevicare), sia (essere). È la grammatica della probabilità, la stessa di pagina 6.", 21.5)
c.para("Ma dopo «so che» e «i giornali scrivono che» resta l'indicativo: il freddo arriva, la finale è a Milano. Opinioni sì, fatti con l'indicativo.", 21.5)
c.bridge("After è probabile che / è possibile che / bisogna che use the subjunctive; after so che / scrivono che use the indicative.")
c.ex("B2", "完成句子", "piova", "è probabile che + subjunctive piova",
     "È probabile che domani ___ (piovere) sul versante adriatico.", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "完成句子", "nevichi", "è possibile che + subjunctive nevichi",
     "È possibile che in montagna ___ (nevicare) nel weekend.", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "完成句子", "sia", "bisogna che + subjunctive sia",
     "Bisogna che la previsione ___ (essere) chiara per tutti.", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "单选", "B", "so che + indicative arriva",
     "«So che il freddo...» A. arrivi · B. arriva · C. arrivare", size=20.5, gap=10)
c.end_report()

# ---- col 3: errori tipici + parola + lettori ----
bx = COLX[3]
errs = [
    ("«Fa freddi.»", "→ «Fa freddo.» Dopo fa, freddo non cambia mai: è invariabile.", "After fa, freddo never changes."),
    ("«Ho nevicato ieri.»", "→ «Ha nevicato ieri.» Nevicare è impersonale: solo la terza persona singolare.", "Nevicare takes third person singular only."),
    ("«Pioverà di sicuro.»", "→ «Potrebbe piovere.» Le previsioni danno probabilità, non certezze.", "Probabilities, not certainties."),
    ("«La gente sono infreddoliti.»", "→ «La gente è infreddolita.» Gente è singolare, come un solo gruppo.", "Gente is singular feminine."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 194
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORI TIPICI · Common mistakes", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 26
wt = "« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("assaggio = tasting. See page 3: free tasting at the Panettone final.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PAROLA · Word of the week", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "assaggio = tasting. See page 3: free tasting at the Panettone final.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 26
lt = "«Ciao! Sono Li, studio italiano a Pechino. Lunedì metto il cappotto e la sciarpa, sabato assaggio il panettone — almeno in foto!» — Li (esempio della redazione)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Editor's sample, not a real letter: no real letters yet, no best page-8 essay yet — both promised for VOL.3. Write to us!", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "LETTERE DEI LETTORI", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Editor's sample, not a real letter: no real letters yet, no best page-8 essay yet — both promised for VOL.3. Write to us!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frasi della settimana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASI DELLA SETTIMANA · PHRASES OF THE WEEK (verbatim from this issue)", 27, "sans", True, OLIVE)
quotes = [
    ("«arriva il primo freddo vero della stagione»", "The first real cold of the season arrives.", "Pagina 1"),
    ("«Non è una certezza, è una probabilità»", "It is not a certainty, it is a probability.", "Pagina 1"),
    ("«il 2 novembre è la Commemorazione dei defunti»", "2 November is the Commemoration of the Dead.", "Pagina 2"),
    ("«Fa freddo, copriti bene!»", "It's cold, wrap up well!", "Pagina 2"),
    ("«il pubblico può assaggiare gratis»", "The public can taste for free.", "Pagina 3"),
    ("«il calcio non si ferma per il primo freddo»", "Football does not stop for the first cold.", "Pagina 4"),
    ("«la cultura continua»", "Culture goes on.", "Pagina 5"),
    ("«Una probabilità alta non è una certezza»", "A high probability is not a certainty.", "Pagina 6"),
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
p.text(MX + 28, py + 44, "LA PROSSIMA SETTIMANA · NEXT WEEK (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Lunedì 9 novembre: chiude il Festival dei Popoli a Firenze. La Festa del Torrone continua a Cremona fino al 22 novembre. E poi: le vostre lettere vere e i testi migliori della pagina 8. A lunedì!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
