# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-it-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LINGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LINGUA · TAAL", "La Lucerna", "Focus op de taal · Tre livelli, tre strumenti · Drie niveaus, drie hulpmiddelen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · DIRE L'ORA E IL PRESENTE", 24)
a.para("Per dire l'ora: «È l'una», ma «Sono le due, le tre…». «E mezza» è +30 minuti (2:30); «meno un quarto», −15 (2:45).", 21.5)
a.para("E dormire è regolare: dormo, dormi, dorme, dormiamo. Svegliarsi è riflessivo: mi sveglio, si sveglia.", 21.5)
a.expl("Alleen 1 uur gebruikt è; dormire is regelmatig; svegliarsi is wederkerend.")
a.ex("A2", "Voltooi de zin", "Sono", "10 uur gebruikt Sono (alleen l'una gebruikt È)",
     "___ le dieci di sera. Comincia il film.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Voltooi de zin", "dorme", "dormire: lui → dorme",
     "Mio fratello ___ (dormire) fino alle undici domenica.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Voltooi de zin", "si sveglia", "svegliarsi: lei → si sveglia",
     "Lei ___ (svegliarsi) alle otto.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Meerkeuze", "B", "e mezza = 30 minuten",
     "«Sono le due e mezza» sono le... A. 2:15 · B. 2:30 · C. 2:45", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · IL PASSATO PROSSIMO", 24)
b.para("Per raccontare il weekend usiamo il passato prossimo: ausiliare + participio. Con avere: ho visitato, abbiamo guardato.", 21.5)
b.para("Con essere — per verbi di movimento come andare e arrivare — il participio cambia con la persona: sono andato / sono andata, è iniziata (la fiera).", 21.5)
b.expl("Over het weekend vertel je met de passato prossimo: avere + deelwoord; bewegingswerkwoorden als andare en arrivare gebruiken essere, en het deelwoord past zich aan in geslacht en getal.")
b.ex("B1", "Voltooi de zin", "è iniziata", "iniziare gebruikt essere; vrouwelijk: è iniziata",
     "La fiera ___ (iniziare) il 10 ottobre.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Voltooi de zin", "abbiamo visitato", "visitare gebruikt avere",
     "Noi ___ (visitare) la mostra mercoledì.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Voltooi de zin", "è andato", "andare gebruikt essere: è andato",
     "Marco ___ (andare) alla sagra con gli amici.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Meerkeuze", "B", "arrivare gebruikt essere + aanpassing aan het meervoud",
     "I tifosi ___ allo stadio. A. hanno arrivato · B. sono arrivati · C. è arrivati", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · IL CONGIUNTIVO", 24)
c.para("Con «è possibile che», «bisogna che» e «è importante che» usiamo il congiuntivo: slitti (slittare), sia (essere), abbia (avere).", 21.5)
c.para("Ma dopo «so che» e «i giornali scrivono che» resta l'indicativo: il Consiglio si riunisce, la Festa chiude. È la grammatica della pagina 6: opinioni sì, fatti con l'indicativo.", 21.5)
c.expl("Na è possibile che, bisogna che en è importante che staat de aanvoegende wijs; na so che en scrivono che de aantonende wijs.")
c.ex("B2", "Voltooi de zin", "slitti", "è possibile che + aanvoegende wijs: slitti",
     "È possibile che il voto ___ (slittare) ancora.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Voltooi de zin", "abbia", "bisogna che + aanvoegende wijs: abbia",
     "Bisogna che ogni cifra ___ (avere) una fonte.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Voltooi de zin", "chiude", "so che + aantonende wijs: chiude",
     "So che la Festa ___ (chiudere) domenica.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Meerkeuze", "B", "è importante che + aanvoegende wijs: sia",
     "«È importante che il grafico...» A. è chiaro · B. sia chiaro · C. essere chiaro", size=20.5, gap=10)
c.end_report()

# ---- col 3: errori tipici + parola + lettori ----
bx = COLX[3]
errs = [
    ("«Sono le una.»", "→ «È l'una.» Solo l'ora 1:00 usa è; le altre ore usano sono.", "Alleen 1:00 gebruikt è, de rest sono."),
    ("«Ho andato a Lucca.»", "→ «Sono andato a Lucca.» Andare vuole l'ausiliare essere, non avere.", "Andare neemt essere, niet avere."),
    ("«Vado a il cinema.»", "→ «Vado al cinema.» A + il si uniscono: al. Anche: del, nel, sul, dal.", "a + il wordt al; ook: del, nel, sul, dal."),
    ("«La gente sono contenti.»", "→ «La gente è contenta.» Gente è singolare, come un solo gruppo.", "Gente: enkelvoud en vrouwelijk."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 194
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORI TIPICI · VEEL FOUTEN", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 26
wt = "« l'anteprima » è la prima volta che il pubblico vede un film. Questa settimana la parola vive a pagina 5: alla Festa del Cinema, molte proiezioni sono anteprime."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("anteprima = première. Op pagina 5 draaien films voor het eerst.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PAROLA · WOORD VAN DE WEEK", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "anteprima = première. Op pagina 5 draaien films voor het eerst.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 26
lt = "«Ciao! Sono Li e studio italiano a Pechino. Domenica dormo un'ora in più e poi guardo Inter–Fiorentina. Grazie per il giornale!» — Li (lettera di esempio, scritta dalla redazione)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Voorbeeldbrief van de redactie, geen echte brief. VOL.2 plaatst echte brieven en de beste tekst van pagina 8 — schrijf ons!", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "LETTERE DEI LETTORI", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Voorbeeldbrief van de redactie, geen echte brief. VOL.2 plaatst echte brieven en de beste tekst van pagina 8 — schrijf ons!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frasi della settimana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASI DELLA SETTIMANA · ZINNEN VAN DE WEEK (woordelijk uit dit nummer)", 27, "sans", True, OLIVE)
quotes = [
    ("«alle 03:00 l'orologio torna indietro di un'ora»", "03:00: de klok gaat een uur terug.", "Pagina 1"),
    ("«È la ricerca numero uno in Italia»", "Dit is de meest gezochte term van Italië.", "Pagina 1"),
    ("«L'ora tra le 02:00 e le 03:00 arriva due volte nella stessa notte.»", "Het uur van 02:00 tot 03:00 komt twee keer voor in dezelfde nacht.", "Pagina 2"),
    ("«In primavera avanti, in autunno indietro.»", "In de lente vooruit, in de herfst terug.", "Pagina 2"),
    ("«Il re della stagione è il tartufo bianco»", "De koning van het seizoen is de witte truffel.", "Pagina 3"),
    ("«È una partita speciale: è la prima della domenica con l'ora solare.»", "Deze wedstrijd is bijzonder: de eerste van de zondag met wintertijd.", "Pagina 4"),
    ("«Molte sono anteprime: film che il pubblico vede per la prima volta.»", "Veel zijn premières: films die het publiek voor het eerst ziet.", "Pagina 5"),
    ("«Un voto previsto non è un voto fatto»", "Een geplande stemming is nog geen stemming.", "Pagina 6"),
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
p.text(MX + 28, py + 44, "LA PROSSIMA SETTIMANA · VOLGENDE WEEK (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Mercoledì 28 ottobre: il voto sulla manovra a Roma. Dal 28 ottobre al 1° novembre: Lucca Comics & Games, la 60ª edizione. Domenica 1° novembre: Ognissanti — quest'anno cade di domenica, niente ponte. E poi: le vostre lettere e i testi migliori della pagina 8. A lunedì!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
