# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　Lingua", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　Frasi della settimana e clinica degli errori")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "Questa pagina è tutta per la lingua: tre piccole lezioni, le frasi della settimana (tutte dagli articoli di questo numero), la clinica degli errori e le vostre lettere.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　DIE UHRZEIT & «WERDEN»", 24)
fa.para("So sagen Sie die Zeit: Es ist halb drei (2.30 Uhr), Viertel vor acht (7.45 Uhr). Mit werden sprechen Sie über die Zukunft: Morgen wird es kalt. Am Sonntag wird die Uhr umgestellt.")
fa.box("BEISPIELE　Esempi", [("„Es ist Viertel vor acht.“　„Morgen wird es sonnig.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "completare", "vor", "7:45 = le otto meno un quarto",
      "Es ist Viertel ___ acht. (7.45 Uhr)", instr="Completa", size=20, gap=8)
fa.ex("A2", "completare", "wird", "wird + Partizip II (passivo)",
      "Am Sonntag ___ die Uhr zurückgestellt. (werden)", instr="Completa", size=20, gap=8)
fa.ex("A2", "completare", "wird", "werden + infinito per il futuro",
      "Morgen ___ es in Berlin regnen. (werden)", instr="Completa", size=20, gap=8)
fa.ex("A2", "scelta multipla", "A", "halb vier = 3:30",
      "„Halb vier“ ist... A. 3.30 Uhr · B. 4.30 Uhr · C. 16.00 Uhr", size=20, gap=8)
fa.end_report()
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1　VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Die Nacht ist länger als sonst. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es regnet — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE　Esempi", [("„Der Zug ist schneller als das Auto.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "completare", "länger", "lang → länger (la notte di 25 ore)",
      "Die Nacht zum Sonntag ist ___ (lang) als andere Nächte.", instr="Completa", size=20, gap=8)
fb.ex("B1", "completare", "weil", "weil introduce la causa",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="Completa", size=20, gap=8)
fb.ex("B1", "trasformazione", "Viele reisen, weil Herbstferien sind.", "con weil il verbo va alla fine",
      "Viele reisen. Es sind Herbstferien. (weil) → ___", instr="Riscrivi", size=20, gap=8)
fb.ex("B1", "scelta multipla", "A", "comparativo: kürzer",
      "Die Tage werden im Herbst... A. kürzer · B. kurz · C. der kürzeste", size=20, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　Esempi", [("„Meiner Meinung nach bleibt die Umstellung.“　„Niemand weiß, ob sie nächstes Jahr noch gilt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "completare", "ob", "ob introduce una domanda indiretta",
      "Ich weiß nicht, ___ die Umstellung bleibt.", instr="Completa", size=20, gap=8)
fc.ex("B2", "completare", "fraglich", "Es ist fraglich, ob ... = non è chiaro se ...",
      "Es ist ___ , ob die Mitgliedstaaten sich einigen.", instr="Completa", size=20, gap=8)
fc.ex("B2", "trasformazione", "Ich finde, dass die Sommerzeit gut ist.", "con dass il verbo va alla fine",
      "Ich finde: Die Sommerzeit ist gut. (dass) → ___", instr="Riscrivi", size=20, gap=8)
fc.ex("B2", "scelta multipla", "B", "Meiner Meinung nach = esprimere un'opinione con cortesia",
      "Höflich eine Meinung sagen: A. „Das ist Quatsch!“ · B. „Meiner Meinung nach ist das zu kompliziert.“ · C. „Du liegst falsch.“", size=20, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word ---
ix = COLX[3]
tb = ["Es ist halb drei. = 2.30 Uhr (non le 3.30)",
      "eine Stunde länger schlafen = dormire un'ora in più",
      "Von O bis O = gomme, ottobre-Pasqua",
      "Meiner Meinung nach ... = secondo me ...",
      "Ich finde, dass ... = penso che ... (verbo alla fine)",
      "Es ist fraglich, ob ... = non è chiaro se"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN　Gli utili", 21, "sans", True, OLIVE)  # D5 fix run2
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
reader = "„Liebe Lucerna, ich stelle meine Uhren schon am Samstagabend um. Dann ist der Sonntag ganz ruhig. Viele Grüße — ein Leser“"
rh = 62 + 30 + len(wrap("Ein Beispiel der Redaktion — VOL.2 druckt Ihre Briefe!", "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap("Schreiben Sie uns Ihre Sätze von Seite 2, 3 und 5 — und Ihre Texte zur Schreibaufgabe auf Seite 8!", "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap("Esempio della redazione: in VOL.2 le vostre lettere vere e i migliori testi di pagina 8.", "sans", False, 19.5, CW - 44)) * 28 + 40
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　Le vostre lettere", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, "Ein Beispiel der Redaktion — VOL.2 druckt Ihre Briefe!", 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, "Schreiben Sie uns Ihre Sätze von Seite 2, 3 und 5 — und Ihre Texte zur Schreibaufgabe auf Seite 8!", 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, "Esempio della redazione: in VOL.2 le vostre lettere vere e i migliori testi di pagina 8.", 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　Una parola in più", 21, "sans", True, OLIVE)  # D5 fix run2
p.para(ix + 22, wy3 + 78, "«der Klassiker» (Seite 4): das größte Spiel der Saison — Bayern gegen Dortmund. Il classico tedesco.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1520
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　Frasi della settimana", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "Citazioni letterali dagli articoli di questo numero　la fonte tra parentesi", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Die Nacht hat dann 25 Stunden, und alle dürfen eine Stunde länger schlafen.", "Quella notte ha 25 ore, e tutti possono dormire un'ora in più.", "Seite 1 · A2"),
    ("Im Frühjahr stellt man die Gartenmöbel VOR das Haus — im Herbst stellt man sie ZURÜCK ins Haus.", "In primavera i mobili da giardino vanno DAVANTI alla casa; in autunno tornano DENTRO. (il trucco)", "Seite 2 · A2"),
    ("Wer vom 26. bis 29. Oktober einen geschnitzten Kürbis abgibt, bekommt für den 31. Oktober ein Freiticket für ein Kind.", "Zucca intagliata consegnata dal 26 al 29 ottobre: ingresso gratis per un bambino il 31.", "Seite 3 · B1"),
    ("Borussia Dortmund gewann am Dienstagabend 2:1 bei Sabah FK in Baku.", "Il Borussia Dortmund ha vinto 2:1 martedì sera a Baku contro il Sabah FK.", "Seite 4 · B1"),
    ("Man wählt ein Buch, ohne es zu kennen.", "Si sceglie un libro senza conoscerlo. (l'appuntamento al buio della biblioteca)", "Seite 5 · B1"),
    ("84 Prozent von ihnen wollten die Umstellung abschaffen.", "L'84% di loro voleva abolire il cambio dell'ora.", "Seite 6 · B2"),
    ("Die Stunde von 2.00 bis 3.00 Uhr gibt es in dieser Nacht zweimal.", "Quella notte, l'ora dalle 2.00 alle 3.00 appare due volte.", "Seite 2 · A2"),
    ("Aber die Regierungen der Mitgliedstaaten wurden sich nicht einig — und so blieb alles, wie es ist.", "Ma i governi degli Stati membri non si sono messi d'accordo — e tutto è rimasto com'era.", "Seite 6 · B2"),
]
for i, (q, zh, tag) in enumerate(phrases):
    cx = COLX[i % 4]; cyy = py + 56 + (i // 4) * 204
    quote = "„" + q + "“"
    qlines = len(wrap(quote, "serif", True, 20.5, CW))
    p.para(cx, cyy + 21, quote, 20.5, "serif", True, INK, CW, 1.38)
    t_y = cyy + 21 + (qlines - 1) * 28.3 + 36
    tlines = len(wrap(zh, "sans", False, 19, CW))
    p.para(cx, t_y, zh, 19, "sans", False, GREY, CW, 1.35)
    p.text(cx, t_y + (tlines - 1) * 25.6 + 30, tag, 18, "sans", True, OLIVE)

# --- error clinic ---
ey = 1980
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "FEHLERKLINIK　Clinica degli errori", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "I quattro errori più frequenti　Correggili prima tu, poi guarda la risposta", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Ich habe 25 Jahre alt.", "Ich bin 25 Jahre alt.", "L'età va con sein, non con haben!"),
    ("Halb drei ist 3.30 Uhr.", "Halb drei ist 2.30 Uhr.", "halb drei = le due e mezza (prima di drei)."),
    ("Berlin ist größer wie Hamburg.", "Berlin ist größer als Hamburg.", "Dopo il comparativo va als, non wie."),
    ("Ich bleibe zu Hause, weil ich lese ein Buch.", "Ich bleibe zu Hause, weil ich ein Buch lese.", "Con weil il verbo va alla fine."),
]
for i, (wrong, right, note) in enumerate(clinic):
    cx = COLX[i]
    p.text(cx, ey + 84, "FALSCH", 19, "sans", True, OLIVE)
    yy = p.para(cx, ey + 112, wrong, 20.5, "serif", False, INK, CW, 1.38)
    p.text(cx, yy + 28, "RICHTIG", 19, "sans", True, OLIVE)
    yy = p.para(cx, yy + 56, right, 20.5, "serif", True, INK, CW, 1.38)
    p.para(cx, yy + 26, note, 19, "sans", False, GREY, CW, 1.35)

# --- next issue teaser ---
ty = 2400
p.rect(MX, ty, RIGHT - MX, 130, fill=CLOTH)
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　Nel prossimo numero (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Samstag, 31. Oktober: Halloween UND Reformationstag UND der Klassiker in Dortmund · Sonntag, 1. November: Allerheiligen · Baden-Württemberg startet in die Herbstferien · dazu Ihre Leserbriefe und die besten Texte von Seite 8!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
