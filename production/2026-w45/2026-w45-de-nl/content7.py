# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE · Taal", "Die Lucerna", "A2 → B2 · Sätze der Woche & Fehlerklinik · Zinnen van de week & foutenkliniek")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "Deze pagina gaat helemaal over taal: drie korte lessen, de zinnen van de week (woord voor woord uit de artikelen van dit nummer), de foutenkliniek en lezersbrieven.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2 · DIE ZAHLEN & «WERDEN»", 24)
fa.para("So sagen Sie die Zahlen: 14,04 Cent pro Liter, rund 8,35 Euro für 50 Liter. Mit werden sprechen Sie über die Zukunft und das Passiv: Am Freitag wird gespielt. Der Tankrabatt wird bis Dezember gelten.")
fa.box("BEISPIELE · Voorbeelden", [("„Am Freitag wird gespielt.“ · „Der Tankrabatt gilt bis Dezember.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "invullen", "wird", "passief: wird + voltooid deelwoord",
      "Am Freitag ___ gespielt: Hamburg gegen Gladbach.", instr="Vul in", size=20, gap=8)
fa.ex("A2", "invullen", "werden", "meervoud: werden",
      "Am Sonntag ___ drei Spiele gespielt.", instr="Vul in", size=20, gap=8)
fa.ex("A2", "invullen", "wird", "werden + infinitief voor de toekomst",
      "Der Tankrabatt ___ bis Dezember gelten.", instr="Vul in", size=20, gap=8)
fa.ex("A2", "meerkeuze", "A", "passief",
      "„Es wird gespielt“ ist... A. Passiv · B. Perfekt · C. Imperativ", size=20, gap=8)
fa.end_report()
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1 · VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Der Abend ist länger als sonst. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es kalt ist — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE · Voorbeelden", [("„Das Spiel ist später als sonst.“ · „Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "invullen", "später", "spät → später (19.30 uur is het laatst)",
      "Das Spiel Hoffenheim–Schalke ist ___ (spät) als die anderen Sonntagsspiele.", instr="Vul in", size=20, gap=8)
fb.ex("B1", "invullen", "weil", "weil geeft een reden",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="Vul in", size=20, gap=8)
fb.ex("B1", "omvormen", "Viele bleiben zu Hause, weil es kalt ist.", "in een weil-zin staat het werkwoord achteraan",
      "Viele bleiben zu Hause. Es ist kalt. (weil) → ___", instr="Herschrijf", size=20, gap=8)
fb.ex("B1", "meerkeuze", "A", "länger als = langer dan",
      "„Länger als sonst“ heißt... A. langer dan gewoonlijk · B. hetzelfde als gewoonlijk · C. korter dan gewoonlijk", size=20, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2 · MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE · Voorbeelden", [("„Meiner Meinung nach braucht die Pflege mehr Geld.“ · „Niemand weiß, ob die Steuer sinkt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "invullen", "ob", "ob leidt een indirecte vraag in",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="Vul in", size=20, gap=8)
fc.ex("B2", "invullen", "fraglich", "Es ist fraglich, ob ... = het is de vraag of ...",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="Vul in", size=20, gap=8)
fc.ex("B2", "omvormen", "Ich finde, dass die Pflege mehr Hilfe braucht.", "in een dass-zin staat het werkwoord achteraan",
      "Ich finde: Die Pflege braucht mehr Hilfe. (dass) → ___", instr="Herschrijf", size=20, gap=8)
fc.ex("B2", "meerkeuze", "B", "een mening beleefd zeggen",
      "„Die Pflege braucht mehr Geld“ höflich sagen: A. „Mehr Geld, sofort!“ · B. „Meiner Meinung nach braucht die Pflege mehr Geld.“ · C. „Die Politik macht alles falsch.“", size=20, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["14,04 Cent = 14,04 cent per liter",
      "rund 8,35 Euro = ongeveer 8,35 euro",
      "Es wird gespielt. = Er wordt gespeeld",
      "Meiner Meinung nach ... = Naar mijn mening ...",
      "Ich finde, dass ... = Ik vind dat ...",
      "Es ist fraglich, ob ... = de vraag of"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN · Op zak", 23, "sans", True, OLIVE)
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
label = "Een voorbeeld van de redactie!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3."
reader = "„Liebe Lucerna, am Dienstag schaue ich Bayern bei Atlético. Die Fußballwoche ist toll! Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.3."
note_nl = "Geen echte brief: nog geen brieven of beste pagina-8-tekst; belofte naar VOL.3."
invite_nl = "Schrijf ons! Stuur je echte brieven in!"
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(note_nl, "sans", False, 19.5, CW - 44)) * 28 + 8 \
    + len(wrap(invite_nl, "serif", False, 20.5, CW - 44)) * 29.5 + 40 + 32
# NOTE (fix1): the +16 corrects the readers-box formula's per-paragraph
# transition undercount (each drawn para adds its size on top of the
# formula's +8 gap); without it the last Chinese line was painted over by
# the word box below (occlusion COVER flag on the first fix1 render).
p.rect(ix, ry, CW, rh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE · Lezersbrieven", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, BRICK, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 19.5, note_nl, 19.5, "sans", False, GREY, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 20.5, invite_nl, 20.5, "serif", False, INK, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT · Nog één woord", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«der Tankrabatt» (Seite 2): die gesenkte Steuer auf Benzin und Diesel. Brandstofkorting.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1520
p.hline(MX, RIGHT, py - 12, GOLD, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE · Zinnen van de week", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "Woord voor woord uit dit nummer", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.", "Vier voetbalavonden achter elkaar, dan een heel weekend competitie.", "Seite 4 · B1"),
    ("Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.", "De energiebelasting op benzine en diesel daalt met 14,04 cent per liter.", "Seite 2 · A2"),
    ("Wer 50 Liter tankt, spart rund 8,35 Euro.", "Wie 50 liter tankt, bespaart ongeveer 8,35 euro.", "Seite 2 · A2"),
    ("Die Schule hat nach den Herbstferien wieder begonnen.", "Na de herfstvakantie is de school weer begonnen.", "Seite 5 · B1"),
    ("Die Tage sind kurz, die Abende lang.", "De dagen zijn kort, de avonden lang.", "Seite 3 · A2"),
    ("Zwei schwere Auswärtsspiele für die deutschen Teams.", "Twee zware uitwedstrijden voor de Duitse teams.", "Seite 4 · B1"),
    ("Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.", "De economie komt langzaam uit de stagnatie, maar het herstel draagt zichzelf nog niet.", "Seite 6 · B2"),
    ("Es geht langsam aufwärts — aber von allein geht es nicht.", "Het gaat langzaam beter — maar niet vanzelf.", "Seite 6 · B2"),
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
p.text(RIGHT, ey + 28, "Vier fouten die leerders het vaakst maken · verbeter eerst zelf, kijk dan", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Die Schule beginnt wieder in Baden-Württemberg am Montag.", "In Baden-Württemberg beginnt die Schule am Montag wieder.", "Werkwoord op plaats 2: ook als het onderwerp niet vooraan staat, blijft het werkwoord op de tweede plaats."),
    ("Halb acht ist 8.30 Uhr.", "Halb acht ist 7.30 Uhr.", "halb acht = half acht (vóór achten)."),
    ("Die Preise sind gefallen um 14 Cent.", "Die Preise sind um 14 Cent gefallen.", "In de Perfekt staat het voltooid deelwoord achteraan."),
    ("Er fragt, ob kommt der Bus?", "Er fragt, ob der Bus kommt.", "In een ob-zin staat het werkwoord achteraan."),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE · Volgend nummer (VOL.3)", 24, "sans", True, "#f3edda")
p.para(MX + 26, ty + 82, "Sonntag, 15. November: Volkstrauertag und NFL in München — American Football in der Allianz Arena · dazu St. Martin am 11. November, die Europapokal-Rückspiele und Ihre Briefe: Schreiben Sie uns! Die besten echten Briefe erscheinen in VOL.3!", 21, "serif", False, "#e8dfc8", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
