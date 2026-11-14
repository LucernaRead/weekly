# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LINGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LINGUA　SPRACHE", "La Lucerna", "Im Fokus: Sprache　Tre livelli, tre strumenti　Drei Stufen, drei Werkzeuge")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　DIRE L'ORA E IL PRESENTE", 24)
a.para("Per dire l'ora: «È l'una», ma «Sono le due, le tre…». «E mezza» è +30 minuti (2:30); «meno un quarto», −15 (2:45).", 21.5)
a.para("E dormire è regolare: dormo, dormi, dorme, dormiamo. Svegliarsi è riflessivo: mi sveglio, si sveglia.", 21.5)
a.noteline("Nur bei 1 Uhr heißt es è; dormire ist regelmäßig; svegliarsi ist ein Reflexivverb.")
a.ex("A2", "Sätze vervollständigen", "Sono", "um zehn Uhr heißt es Sono (nur l'una mit È)",
     "___ le dieci di sera. Comincia il film.", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "Sätze vervollständigen", "dorme", "dormire: lui → dorme",
     "Mio fratello ___ (dormire) fino alle undici domenica.", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "Sätze vervollständigen", "si sveglia", "svegliarsi: lei → si sveglia",
     "Lei ___ (svegliarsi) alle otto.", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "Eine Antwort", "B", "e mezza = 30 Minuten",
     "«Sono le due e mezza» sono le... A. 2:15 · B. 2:30 · C. 2:45", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　IL PASSATO PROSSIMO", 24)
b.para("Per raccontare il weekend usiamo il passato prossimo: ausiliare + participio. Con avere: ho visitato, abbiamo guardato.", 21.5)
b.para("Con essere — per verbi di movimento come andare e arrivare — il participio cambia con la persona: sono andato / sono andata, è iniziata (la fiera).", 21.5)
b.noteline("Fürs Wochenende: passato prossimo — avere + Partizip; Bewegungsverben (andare, arrivare) mit essere, das Partizip richtet sich nach der Person.")
b.ex("B1", "Sätze vervollständigen", "è iniziata", "iniziare mit essere, weiblich: è iniziata",
     "La fiera ___ (iniziare) il 10 ottobre.", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "Sätze vervollständigen", "abbiamo visitato", "visitare mit avere",
     "Noi ___ (visitare) la mostra mercoledì.", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "Sätze vervollständigen", "è andato", "andare mit essere: è andato",
     "Marco ___ (andare) alla sagra con gli amici.", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "Eine Antwort", "B", "arrivare mit essere + Angleichung im Plural",
     "I tifosi ___ allo stadio. A. hanno arrivato · B. sono arrivati · C. è arrivati", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　IL CONGIUNTIVO", 24)
c.para("Con «è possibile che», «bisogna che» e «è importante che» usiamo il congiuntivo: slitti (slittare), sia (essere), abbia (avere).", 21.5)
c.para("Ma dopo «so che» e «i giornali scrivono che» resta l'indicativo: il Consiglio si riunisce, la Festa chiude. È la grammatica della pagina 6: opinioni sì, fatti con l'indicativo.", 21.5)
c.noteline("Nach è possibile che / bisogna che / è importante che steht der congiuntivo; nach so che und scrivono che der Indikativ.")
c.ex("B2", "Sätze vervollständigen", "slitti", "è possibile che + congiuntivo: slitti",
     "È possibile che il voto ___ (slittare) ancora.", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "Sätze vervollständigen", "abbia", "bisogna che + congiuntivo: abbia",
     "Bisogna che ogni cifra ___ (avere) una fonte.", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "Sätze vervollständigen", "chiude", "so che + Indikativ: chiude",
     "So che la Festa ___ (chiudere) domenica.", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "Eine Antwort", "B", "è importante che + congiuntivo: sia",
     "«È importante che il grafico...» A. è chiaro · B. sia chiaro · C. essere chiaro", size=20.5, gap=10)
c.end_report()

# ---- col 3: errori tipici + parola + lettori ----
bx = COLX[3]
errs = [
    ("«Sono le una.»", "→ «È l'una.» Solo l'ora 1:00 usa è; le altre ore usano sono.", "Nur 1:00 mit è, sonst sono."),
    ("«Ho andato a Lucca.»", "→ «Sono andato a Lucca.» Andare vuole l'ausiliare essere, non avere.", "andare steht mit essere."),
    ("«Vado a il cinema.»", "→ «Vado al cinema.» A + il si uniscono: al. Anche: del, nel, sul, dal.", "a + il wird al; vgl. del, nel."),
    ("«La gente sono contenti.»", "→ «La gente è contenta.» Gente è singolare, come un solo gruppo.", "gente ist Singular (feminin)."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 194
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORI TIPICI　FEHLERKLINIK", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 26
wt = "« l'anteprima » è la prima volta che il pubblico vede un film. Questa settimana la parola vive a pagina 5: alla Festa del Cinema, molte proiezioni sono anteprime."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("anteprima = Premiere (Seite 5: viele Premieren).", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PAROLA　WORT DER WOCHE", 22, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "anteprima = Premiere (Seite 5: viele Premieren).", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 26
lt = "«Ciao! Sono Li e studio italiano a Pechino. Domenica dormo un'ora in più e poi guardo Inter–Fiorentina. Grazie per il giornale!» — Li (lettera di esempio, scritta dalla redazione)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Beispielbrief der Redaktion, keine echte Leserpost. VOL.2: echte Briefe + bester Seite-8-Text — schreiben Sie uns!", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "LETTERE DEI LETTORI", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Beispielbrief der Redaktion, keine echte Leserpost. VOL.2: echte Briefe + bester Seite-8-Text — schreiben Sie uns!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frasi della settimana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "FRASI DELLA SETTIMANA　SÄTZE DER WOCHE (wörtlich aus dieser Ausgabe)", 27, "sans", True, OLIVE)
quotes = [
    ("«alle 03:00 l'orologio torna indietro di un'ora»", "Um 03:00 geht die Uhr eine Stunde zurück.", "Pagina 1"),
    ("«È la ricerca numero uno in Italia»", "Es ist die Suche Nummer eins in Italien.", "Pagina 1"),
    ("«L'ora tra le 02:00 e le 03:00 arriva due volte nella stessa notte.»", "Die Stunde von 02:00 bis 03:00 gibt es zweimal in derselben Nacht.", "Pagina 2"),
    ("«In primavera avanti, in autunno indietro.»", "Im Frühling vor, im Herbst zurück.", "Pagina 2"),
    ("«Il re della stagione è il tartufo bianco»", "Der König der Saison ist der weiße Trüffel.", "Pagina 3"),
    ("«È una partita speciale: è la prima della domenica con l'ora solare.»", "Ein besonderes Spiel: das erste am Sonntag mit Winterzeit.", "Pagina 4"),
    ("«Molte sono anteprime: film che il pubblico vede per la prima volta.»", "Viele sind Premieren: Filme, die das Publikum zum ersten Mal sieht.", "Pagina 5"),
    ("«Un voto previsto non è un voto fatto»", "Eine geplante Abstimmung ist keine erfolgte Abstimmung.", "Pagina 6"),
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
p.text(MX + 28, py + 44, "LA PROSSIMA SETTIMANA　NÄCHSTE WOCHE (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Mercoledì 28 ottobre: il voto sulla manovra a Roma. Dal 28 ottobre al 1° novembre: Lucca Comics & Games, la 60ª edizione. Domenica 1° novembre: Ognissanti — quest'anno cade di domenica, niente ponte. E poi: le vostre lettere e i testi migliori della pagina 8. A lunedì!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
