# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　Taal", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　Zinnen van de week en de foutenkliniek")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "Deze pagina gaat over taal: drie korte lessen, de zinnen van de week (letterlijk uit dit nummer), de foutenkliniek — en jullie brieven.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　DATEN SAGEN", 24)
fa.para("So sagen Sie Daten: Am 18. November ist Buß- und Bettag. Am 29. November ist der erste Advent. Mit werden sprechen Sie über das Passiv: Um 20.30 Uhr wird in München gespielt.")
fa.box("BEISPIELE　Voorbeelden", [("„Am 18. November ist Buß- und Bettag.“　„Um 20.30 Uhr wird in München gespielt.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "invullen", "wird", "lijdende vorm: wird + voltooid deelwoord",
      "Am Freitag ___ in München gespielt.", instr="Vul in", size=22, gap=8)
fa.ex("A2", "invullen", "werden", "Meervoud: werden",
      "Die Weihnachtsmärkte ___ am Montag geöffnet.", instr="Vul in", size=22, gap=8)
fa.ex("A2", "invullen", "wird", "werden + infinitief: toekomst",
      "Der Adventskalender ___ am 1. Dezember beginnen.", instr="Vul in", size=22, gap=8)
fa.ex("A2", "meerkeuze", "A", "lijdende vorm",
      "„Es wird gespielt“ ist... A. Passiv · B. Perfekt · C. Imperativ", size=22, gap=8)
fa.end_report()
# --- P7 image: reading room, below the A2 column (col 0 free space) ---
iy7 = fa.y + 16
image(p, "lesesaal.jpg", COLX[0], iy7, CW, 145)  # W47 D1: was 150; A2 flow grew with 16.5pt stems, keep caption clear of the 1548 rule
cy7 = caption(p, COLX[0], iy7 + 150, CW,
              "Der große Lesesaal der Library of Congress in Washington.",
              "Foto: Carol M. Highsmith — public domain")
print("P7 image ends", cy7, "(A2 flow ended", fa.y, ")")
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1　VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Der November ist stiller als der Oktober. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es dunkel ist — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE　Voorbeelden", [("„Der November ist stiller als der Oktober.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "invullen", "stiller", "still → stiller (stiller dan oktober)",
      "Im November ist es ___ (still) als im Oktober.", instr="Vul in", size=22, gap=8)
fb.ex("B1", "invullen", "weil", "weil: de reden",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="Vul in", size=22, gap=8)
fb.ex("B1", "omzetten", "Viele bleiben zu Hause, weil es dunkel ist.", "weil: werkwoord achteraan",
      "Viele bleiben zu Hause. Es ist dunkel. (weil) → ___", instr="Herschrijf", size=22, gap=8)
fb.ex("B1", "meerkeuze", "A", "stiller als = stiller dan …",
      "„Stiller als sonst“ heißt... A. stiller dan anders · B. hetzelfde als anders · C. lawaaiiger dan anders", size=22, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　Voorbeelden", [("„Meiner Meinung nach braucht das Gedenken Stille.“　„Niemand weiß, ob die Einigung gelingt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "invullen", "ob", "ob: indirecte vraag",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="Vul in", size=22, gap=8)
fc.ex("B2", "invullen", "fraglich", "fraglich: nog onzeker",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="Vul in", size=22, gap=8)
fc.ex("B2", "omzetten", "Ich finde, dass das Gedenken Stille braucht.", "dass: werkwoord achteraan",
      "Ich finde: Das Gedenken braucht Stille. (dass) → ___", instr="Herschrijf", size=22, gap=8)
fc.ex("B2", "meerkeuze", "B", "beleefd je mening geven",
      "„Das Gedenken braucht Stille“ höflich sagen: A. „Stille, sofort!“ · B. „Meiner Meinung nach braucht das Gedenken Stille.“ · C. „Die Politik macht alles falsch.“", size=22, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["18. November = 18 november",
      "der Buß- und Bettag = dag van boete en gebed",
      "vor fast leeren Rängen = voor bijna lege tribunes",
      "Es wird gespielt. = De wedstrijd wordt gespeeld (lijdende vorm)",
      "Meiner Meinung nach = Naar mijn mening",
      "Es ist fraglich, ob ... = nog onzeker"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110  # fix1 D1: pad 90 -> 110 (= core-de value) + rail raised (RTOP, see below). Formula misses the +20.5/entry p.para offset (6 entries = +123), only partly offset by the 29.5 vs 29.11 line-height gap: clearance = pad - 90.0 for nl (10 lines), so 90 gave +0.0 (last baseline 813.0 exactly on the box bottom 813.0, 'fraglich' descender ~4.7 below the box). 110 gives clearance +20.0, same class as core +18.8. Occlusion audit cannot see this defect class (text drawn after its own box, nothing covers it) -- the old "validated by occlusion 0 flags" claim was false. Edition-local fix only; shared helper untouched.
RTOP = CTOP - 20  # fix1 D1: col-3 rail raised 20 so the +20 pad leaves the rail bottom exactly where it was (toolbox bottom 813.0, LESERBRIEFE y 829, NOCH EIN WORT ends 1547.5, still 0.5px before the 1548 Satze rule -- a flat +20 pad alone would push it to 1567.5, past the rule). Above-box slack is ~63px (P7 intro ends at baseline 262, toolbox top was 330), 20 used, ~43 left; the box top now sits 20px above the A2/B1/B2 heads (330) -- no overlap, nothing is drawn in col 3 between y 267 and 330.
p.rect(ix, RTOP, CW, tbh, fill=BOX)
yy3 = RTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN　Werktuig", 20, "sans", True, OLIVE)  # D5 (2026-11-12): @23pt 438.9px ran +39.0px past the box; @20pt 381.7px fits 400.5 (21pt still +0.3px over). No wording change.
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = RTOP + tbh + 16
label = "Ein Beispiel der Redaktion!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.5."
reader = "„Liebe Lucerna, im November bastle ich einen Adventskalender. Am 1. Dezember öffne ich das erste Türchen. Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.5."
chinese = "Voorbeeld van de redactie: er was nog geen echte brief binnen voor de deadline. Stuur je teksten voor VOL.5!"
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　Brieven van lezers", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　Nog één woord", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«der Adventskalender» (p. 5): een kalender met 24 deurtjes.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1560
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　Zinnen van de week", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "Letterlijk uit dit nummer　Bron tussen haakjes", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln.", "Na twee weken pauze speelt Bayern vrijdagavond tegen Köln.", "Seite 1 · A2"),
    ("Es geht ums Viertelfinale der Nations League.", "Het gaat om de kwartfinale van de Nations League.", "Seite 1 · A2"),
    ("Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag.", "Alleen in Saksen is de Buß- und Bettag een feestdag.", "Seite 2 · A2"),
    ("Die Märkte beginnen fast zwei Wochen früher.", "De markten openen bijna twee weken eerder.", "Seite 3 · A2"),
    ("Hinter jedem Türchen wartet eine kleine Überraschung.", "Achter elk deurtje wacht een kleine verrassing.", "Seite 5 · B1"),
    ("Der FC Bayern gewann in Mainz mit 2:1.", "Bayern won met 2–1 in Mainz.", "Seite 4 · B1"),
    ("Die stille Woche ist der Übergang: vom November in den Advent.", "De stille week is de overgang: van november naar de advent.", "Seite 6 · B2"),
    ("Am Sonntag ist es still im Land.", "Op zondag is het hele land stil.", "Seite 6 · B2"),
]
for i, (q, zh, tag) in enumerate(phrases):
    cx = COLX[i % 4]; cyy = py + 56 + (i // 4) * 190
    quote = "„" + q + "“"
    qlines = len(wrap(quote, "serif", True, 20.5, CW))
    p.para(cx, cyy + 21, quote, 20.5, "serif", True, INK, CW, 1.38)
    t_y = cyy + 21 + (qlines - 1) * 28.3 + 36
    tlines = len(wrap(zh, "sans", False, 19, CW))
    p.para(cx, t_y, zh, 19, "sans", False, GREY, CW, 1.35)
    p.text(cx, t_y + (tlines - 1) * 25.6 + 30, tag, 18, "sans", True, OLIVE)

# --- error clinic ---
ey = 2020
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "FEHLERKLINIK　Foutenkliniek", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "De vier meest gemaakte fouten　Verbeter eerst zelf, kijk dan na", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Am Mittwoch die Kinder basteln einen Adventskalender.", "Am Mittwoch basteln die Kinder einen Adventskalender.", "Werkwoord op 2: het werkwoord blijft tweede, ook zonder onderwerp vooraan."),
    ("Halb neun ist 9.30 Uhr.", "Halb neun ist 8.30 Uhr.", "halb neun = half negen (vóór neun)."),
    ("Die Mannschaft ist nach Berlin gereist am Montag.", "Die Mannschaft ist am Montag nach Berlin gereist.", "In de Perfekt staat het deelwoord achteraan."),
    ("Er fragt, ob spielt die Nationalelf am Montag?", "Er fragt, ob die Nationalelf am Montag spielt.", "In de bijzin met ob staat het werkwoord achteraan."),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　Volgend nummer (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Sonntag, 29. November: Der erste Advent beginnt — Kerzen, Lieder und das erste Türchen. Dazu die Ergebnisse der Europapokale (24.–26. November), der 11. Spieltag und die Weihnachtsmärkte in vollem Gang. Und Ihre Briefe: Die besten echten Briefe erscheinen in VOL.5!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
