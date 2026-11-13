# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-it-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LINGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LINGUA　LÍNGUA", "La Lucerna", "Foco na língua　Tre livelli, tre strumenti　Três níveis, três ferramentas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　IL FUTURO", 24)
a.para("Per i piani della settimana usiamo il futuro semplice: andremo a Cremona, assaggeremo il torrone, guarderemo Atalanta–Inter. Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.", 21.5)
a.para("E per la settimana prossima: leggeremo a BookCity, che apre lunedì 23 novembre. Il verbo è leggere, regolare al futuro: leggerò.", 21.5)
a.bridge("Fala de planos no futuro: andremo, assaggeremo, guarderemo, leggeremo.")
a.ex("A2", "Completa a frase", "andremo", "andare, futuro, noi: andremo",
     "Domenica noi ___ (andare) a Cremona.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Completa a frase", "assaggeremo", "assaggiare, futuro, noi: assaggeremo",
     "Noi ___ (assaggiare) il torrone.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Completa a frase", "guarderemo", "guardare, futuro, noi: guarderemo",
     "Domenica sera noi ___ (guardare) Atalanta–Inter.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Escolha múltipla", "B", "leggerò é o futuro de leggere",
     "A BookCity io... A. leggo ora · B. leggerò lunedì · C. leggevo ieri", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　IL PASSATO PROSSIMO", 24)
b.para("Per raccontare il weekend usiamo il passato prossimo: ausiliare + participio. Con essere il participio cambia: è partito (il corteo), è finita (la festa).", 21.5)
b.para("Con avere: abbiamo visto, hanno comprato. Il participio con avere non cambia.", 21.5)
b.bridge("Para o passado usa-se o passato prossimo: partire/finire levam essere e o particípio concorda; com avere não muda.")
b.ex("B1", "Completa a frase", "è partito", "partire leva essere: è partito",
     "Il corteo ___ (partire) alle 16.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Completa a frase", "abbiamo visto", "vedere leva avere: abbiamo visto",
     "Domenica noi ___ (vedere) gli sbandieratori.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Completa a frase", "hanno comprato", "comprare leva avere: hanno comprato",
     "I visitatori ___ (comprare) il torrone.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Escolha múltipla", "A", "finire leva essere: è finita",
     "La Festa del Torrone ___ domenica. A. è finita · B. ha finito · C. sono finite", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　IL CONGIUNTIVO", 24)
c.para("Con «è probabile che», «è possibile che» e «bisogna che» usiamo il congiuntivo: piova (piovere), nevichi (nevicare), leggano (leggere). È la grammatica della probabilità, la stessa di pagina 6.", 21.5)
c.para("Ma dopo «so che» e «i giornali scrivono che» resta l'indicativo: il sole torna, la Festa del Torrone è a Cremona. Opinioni sì, fatti con l'indicativo.", 21.5)
c.bridge("Depois de è probabile che / è possibile che / bisogna che usa-se o subjuntivo; depois de so che / scrivono che, o indicativo.")
c.ex("B2", "Completa a frase", "piova", "è probabile che + subjuntivo piova",
     "È probabile che domenica ___ (piovere) a Bergamo.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Completa a frase", "nevichi", "è possibile che + subjuntivo nevichi",
     "È possibile che stasera ___ (nevicare) sulle Alpi.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Completa a frase", "leggano", "bisogna che + subjuntivo leggano",
     "Bisogna che i lettori ___ (leggere) il testo finale.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Escolha múltipla", "B", "so che + indicativo torna",
     "«So che il sole...» A. torni · B. torna · C. tornare", size=20.5, gap=10)
c.end_report()

# ---- Dante image under the B1 column (measured below the flow end) ----
dy0 = b.y + 16
print("P7 B1 flow ends y=", b.y, "dante slot y0=", dy0)
if dy0 + 330 + 100 <= 1560:
    image(p, "dante.jpg", COLX[1] + 87, dy0, 260, 330)
    caption(p, COLX[1] + 87, dy0 + 330, 260, "Dante Alighieri, il padre della lingua italiana.",
            "Foto: Met Museum — CC0")
else:
    print("  !! P7 DANTE NOSPACE: y0=", dy0)

# ---- col 3: errori tipici + parola + lettori ----
bx = COLX[3]
errs = [
    ("«La Lazio hanno 29 punti.»", "→ «La Lazio ha 29 punti.» La Lazio è singolare, il verbo è singolare.", "A Lazio é singular, e o verbo também."),
    ("«È probabile che la Lazio vince.»", "→ «È probabile che la Lazio vinca.» Dopo è probabile che serve il congiuntivo.", "Depois de è probabile che: subjuntivo."),
    ("«Ieri ho andato a Cremona.»", "→ «Ieri sono andato a Cremona.» Andare vuole essere, non avere.", "andare leva essere como auxiliar."),
    ("«Il torrone sono dolce.»", "→ «Il torrone è dolce.» Torrone è singolare, il verbo è singolare.", "Torrone é singular, e o verbo também."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 194
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORI TIPICI　ERROS", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 26
wt = "« la vetta » è il primo posto in classifica: la Lazio è in vetta con 29 punti, l'Inter e la Roma inseguono. Questa settimana vive a pagina 1 e a pagina 4."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("vetta = o topo. Ver páginas 1 e 4 esta semana: a Lazio lidera com 29 pontos.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PAROLA　PALAVRA DA SEMANA", 20.5, "sans", True, OLIVE)  # D5 (2026-11-12): was 23, title ran +42.5px past the box; 20.5 fits
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "vetta = o topo. Ver páginas 1 e 4 esta semana: a Lazio lidera com 29 pontos.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 26
lt = "«Ciao! Questa settimana assaggio il torrone e guardo Atalanta–Inter. E voi? Scriveteci!» — esempio della redazione"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Exemplo da redação, não uma carta real. Sem cartas reais nem melhores redações; a promessa passa ao VOL.5.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "LETTERE DEI LETTORI", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Exemplo da redação, não uma carta real. Sem cartas reais nem melhores redações; a promessa passa ao VOL.5.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frasi della settimana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "FRASI DELLA SETTIMANA　FRASES DA SEMANA (RETIRADAS DESTE NÚMERO)", 27, "sans", True, OLIVE)
quotes = [
    ("«La Lazio resta in vetta»", "A Lazio continua líder.", "Pagina 1"),
    ("«ventiquattro gol in dieci partite»", "Vinte e quatro golos em dez jogos.", "Pagina 1"),
    ("«il ponte votivo sul Canal Grande»", "A ponte votiva sobre o Grande Canal.", "Pagina 2"),
    ("«oltre centocinquanta figuranti in costumi rinascimentali»", "Mais de cento e cinquenta figurantes em trajes renascentistas.", "Pagina 3"),
    ("«la squadra di Gattuso è ancora imbattuta dopo 11 giornate»", "A equipa de Gattuso continua invicta após 11 jornadas.", "Pagina 4"),
    ("«sette giorni di libri, ragioni e follie»", "Sete dias de livros, razão e loucura.", "Pagina 5"),
    ("«il testo può ancora cambiare»", "O texto ainda pode mudar.", "Pagina 6"),
    ("«approvato dal governo non vuol dire già legge»", "A aprovação do governo não significa que já seja lei.", "Pagina 6"),
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
p.text(MX + 28, py + 44, "LA PROSSIMA SETTIMANA　NA PRÓXIMA SEMANA (VOL.5)", 24, "sans", True, "#cac8ba")
p.para(MX + 28, py + 84, "Lunedì 23 novembre apre BookCity a Milano; la 12ª giornata si chiude con i risultati; le due notti azzurre si raccontano con i risultati. E poi: le vostre lettere vere e i testi migliori della pagina 8. A lunedì!", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
