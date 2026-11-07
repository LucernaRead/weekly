# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-de-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE · Taal", "Die Lucerna", "A2 → B2 · Sätze der Woche & Fehlerklinik · Zinnen van de week & foutenkliniek")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "Deze pagina is voor de taal: drie kleine lessen, de zinnen van de week uit dit nummer (allemaal letterlijk uit de artikelen van deze week), onze foutenkliniek — en uw brieven.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2 · DIE UHRZEIT & «WERDEN»", 24)
fa.para("So sagen Sie die Zeit: Es ist halb drei (2.30 Uhr), Viertel vor acht (7.45 Uhr). Mit werden sprechen Sie über die Zukunft: Morgen wird es kalt. Am Sonntag wird die Uhr umgestellt.")
fa.box("BEISPIELE · Voorbeelden", [("„Es ist Viertel vor acht.“ · „Morgen wird es sonnig.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "Voltooi de zin", "vor", "7.45 = kwart voor acht",
      "Es ist Viertel ___ acht. (7.45 Uhr)", instr="Vul in", size=20, gap=8)
fa.ex("A2", "Voltooi de zin", "wird", "wird + voltooid deelwoord (passief)",
      "Am Sonntag ___ die Uhr zurückgestellt. (werden)", instr="Vul in", size=20, gap=8)
fa.ex("A2", "Voltooi de zin", "wird", "werden + infinitief voor de toekomst",
      "Morgen ___ es in Berlin regnen. (werden)", instr="Vul in", size=20, gap=8)
fa.ex("A2", "Meerkeuze", "A", "halb vier = 3:30",
      "„Halb vier“ ist... A. 3.30 Uhr · B. 4.30 Uhr · C. 16.00 Uhr", size=20, gap=8)
fa.end_report()
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1 · VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Die Nacht ist länger als sonst. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es regnet — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE · Voorbeelden", [("„Der Zug ist schneller als das Auto.“ · „Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "Voltooi de zin", "länger", "lang → länger (de nacht van 25 uur)",
      "Die Nacht zum Sonntag ist ___ (lang) als andere Nächte.", instr="Vul in", size=20, gap=8)
fb.ex("B1", "Voltooi de zin", "weil", "weil geeft een reden",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="Vul in", size=20, gap=8)
fb.ex("B1", "Zinsomvorming", "Viele reisen, weil Herbstferien sind.", "in een weil-zin staat het werkwoord aan het einde",
      "Viele reisen. Es sind Herbstferien. (weil) → ___", instr="Herschrijf", size=20, gap=8)
fb.ex("B1", "Meerkeuze", "A", "vergrotende trap: kürzer",
      "Die Tage werden im Herbst... A. kürzer · B. kurz · C. der kürzeste", size=20, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2 · MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE · Voorbeelden", [("„Meiner Meinung nach bleibt die Umstellung.“ · „Niemand weiß, ob sie nächstes Jahr noch gilt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "Voltooi de zin", "ob", "ob leidt een indirecte vraag in",
      "Ich weiß nicht, ___ die Umstellung bleibt.", instr="Vul in", size=20, gap=8)
fc.ex("B2", "Voltooi de zin", "fraglich", "Es ist fraglich, ob ... = nog onzeker",
      "Es ist ___ , ob die Mitgliedstaaten sich einigen.", instr="Vul in", size=20, gap=8)
fc.ex("B2", "Zinsomvorming", "Ich finde, dass die Sommerzeit gut ist.", "in een dass-zin staat het werkwoord aan het einde",
      "Ich finde: Die Sommerzeit ist gut. (dass) → ___", instr="Herschrijf", size=20, gap=8)
fc.ex("B2", "Meerkeuze", "B", "Meiner Meinung nach = beleefd je mening geven",
      "Höflich eine Meinung sagen: A. „Das ist Quatsch!“ · B. „Meiner Meinung nach ist das zu kompliziert.“ · C. „Du liegst falsch.“", size=20, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word ---
ix = COLX[3]
tb = ["Es ist halb drei. = 2.30 Uhr (niet 3.30)",
      "eine Stunde länger schlafen = een uur langer slapen",
      "Von O bis O: oktober tot Pasen",
      "Meiner Meinung nach ... = naar mijn mening ...",
      "Ich finde, dass ... = ik vind dat ... (werkwoord aan het einde)",
      "Es ist fraglich, ob ... = nog onzeker"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN · Op zak", 23, "sans", True, OLIVE)
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
reader = "„Liebe Lucerna, ich stelle meine Uhren schon am Samstagabend um. Dann ist der Sonntag ganz ruhig. Viele Grüße — ein Leser“"
rh = 62 + 30 + len(wrap("Ein Beispiel der Redaktion — VOL.2 druckt Ihre Briefe!", "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap("Schreiben Sie uns Ihre Sätze von Seite 2, 3 und 5 — und Ihre Texte zur Schreibaufgabe auf Seite 8!", "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap("Voorbeeld van de redactie — in VOL.2 komen echte brieven en teksten van p. 8.", "sans", False, 19.5, CW - 44)) * 28 + 40
p.rect(ix, ry, CW, rh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE · Lezersbrieven", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, "Ein Beispiel der Redaktion — VOL.2 druckt Ihre Briefe!", 20, "sans", True, BRICK, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, "Schreiben Sie uns Ihre Sätze von Seite 2, 3 und 5 — und Ihre Texte zur Schreibaufgabe auf Seite 8!", 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, "Voorbeeld van de redactie — in VOL.2 komen echte brieven en teksten van p. 8.", 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT · Nog één woord", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«der Klassiker» (Seite 4): das größte Spiel der Saison — Bayern gegen Dortmund. Duitse voetbal-klassieker.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1520
p.hline(MX, RIGHT, py - 12, GOLD, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE · Zinnen van de week", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "Letterlijke citaten uit dit nummer · Tussen haakjes staat de bron", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Die Nacht hat dann 25 Stunden, und alle dürfen eine Stunde länger schlafen.", "Die nacht heeft dan 25 uur, en iedereen mag een uur langer slapen.", "Seite 1 · A2"),
    ("Im Frühjahr stellt man die Gartenmöbel VOR das Haus — im Herbst stellt man sie ZURÜCK ins Haus.", "In het voorjaar zet je de tuinmeubelen VÓÓR het huis — in de herfst zet je ze TERUG in huis. (Ezelsbruggetje)", "Seite 2 · A2"),
    ("Wer vom 26. bis 29. Oktober einen geschnitzten Kürbis abgibt, bekommt für den 31. Oktober ein Freiticket für ein Kind.", "Wie van 26-29 oktober een pompoen inlevert, krijgt een vrijkaartje voor een kind.", "Seite 3 · B1"),
    ("Borussia Dortmund gewann am Dienstagabend 2:1 bei Sabah FK in Baku.", "Borussia Dortmund won dinsdagavond met 2:1 bij Sabah FK in Bakoe.", "Seite 4 · B1"),
    ("Man wählt ein Buch, ohne es zu kennen.", "Je kiest een boek, zonder het te kennen. (Het blind date van de bibliotheek.)", "Seite 5 · B1"),
    ("84 Prozent von ihnen wollten die Umstellung abschaffen.", "84 procent van hen wilde de klokverzetting afschaffen.", "Seite 6 · B2"),
    ("Die Stunde von 2.00 bis 3.00 Uhr gibt es in dieser Nacht zweimal.", "In deze nacht komt het uur van 2.00 tot 3.00 uur twee keer voor.", "Seite 2 · A2"),
    ("Aber die Regierungen der Mitgliedstaaten wurden sich nicht einig — und so blieb alles, wie es ist.", "Maar de regeringen van de lidstaten werden het niet eens — en zo bleef alles, zoals het was.", "Seite 6 · B2"),
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
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "FEHLERKLINIK · Foutenkliniek", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "De vier fouten die leerders het vaakst maken · Verbeter ze eerst zelf, kijk dan naar het antwoord", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Ich habe 25 Jahre alt.", "Ich bin 25 Jahre alt.", "Leeftijd gaat met sein, niet met haben!"),
    ("Halb drei ist 3.30 Uhr.", "Halb drei ist 2.30 Uhr.", "halb drei = half drie (2.30 uur, vóór drei)."),
    ("Berlin ist größer wie Hamburg.", "Berlin ist größer als Hamburg.", "Na de vergrotende trap gebruik je als, niet wie."),
    ("Ich bleibe zu Hause, weil ich lese ein Buch.", "Ich bleibe zu Hause, weil ich ein Buch lese.", "In een weil-zin staat het werkwoord aan het einde."),
]
for i, (wrong, right, note) in enumerate(clinic):
    cx = COLX[i]
    p.text(cx, ey + 84, "FALSCH", 19, "sans", True, BRICK)
    yy = p.para(cx, ey + 112, wrong, 20.5, "serif", False, INK, CW, 1.38)
    p.text(cx, yy + 28, "RICHTIG", 19, "sans", True, OLIVE)
    yy = p.para(cx, yy + 56, right, 20.5, "serif", True, INK, CW, 1.38)
    p.para(cx, yy + 26, note, 19, "sans", False, GREY, CW, 1.35)

# --- next issue teaser ---
ty = 2400
p.rect(MX, ty, RIGHT - MX, 130, fill=DARK)
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE · In het volgende nummer (VOL.2)", 24, "sans", True, "#f3edda")
p.para(MX + 26, ty + 82, "Samstag, 31. Oktober: Halloween UND Reformationstag UND der Klassiker in Dortmund · Sonntag, 1. November: Allerheiligen · Baden-Württemberg startet in die Herbstferien · dazu Ihre Leserbriefe und die besten Texte von Seite 8!", 21, "serif", False, "#e8dfc8", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
