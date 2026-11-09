# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　Taal", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　Zinnen van de week en foutenkliniek")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "Deze pagina gaat helemaal over taal: drie korte lessen, de zinnen van de week (allemaal woord voor woord geciteerd uit de artikelen van dit nummer), de foutenkliniek en lezersbrieven.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　UHRZEITEN & DATEN", 24)
fa.para("So sagen Sie Uhrzeiten und Daten: Um 11.11 Uhr beginnt der Karneval. Am 15. November ist Volkstrauertag. Mit werden sprechen Sie über das Passiv: Um 20.45 Uhr wird in Belgrad gespielt. Die NFL wird in München gespielt.")
fa.box("BEISPIELE　Voorbeelden", [("„Um 11.11 Uhr beginnt der Karneval.“　„Am Sonntag wird in München Football gespielt.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "invullen", "wird", "passief: wird + voltooid deelwoord",
      "Am Freitag ___ in Belgrad gespielt.", instr="Vul in", size=20, gap=8)
fa.ex("A2", "invullen", "werden", "meervoud: werden",
      "Am 11. November ___ zwei Feste gefeiert.", instr="Vul in", size=20, gap=8)
fa.ex("A2", "invullen", "wird", "werden + infinitief voor de toekomst",
      "Die Karnevalssession ___ um 11.11 Uhr beginnen.", instr="Vul in", size=20, gap=8)
fa.ex("A2", "meerkeuze", "A", "lijdende vorm",
      "„Es wird gespielt“ ist... A. Passiv · B. Perfekt · C. Imperativ", size=20, gap=8)
fa.end_report()
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1　VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Die Nacht ist länger als der Tag. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es dunkel ist — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE　Voorbeelden", [("„Die Nacht ist länger als der Tag.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "invullen", "länger", "lang → länger (de nacht is langer dan de dag)",
      "Im November ist die Nacht ___ (lang) als der Tag.", instr="Vul in", size=20, gap=8)
fb.ex("B1", "invullen", "weil", "weil leidt een reden in",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="Vul in", size=20, gap=8)
fb.ex("B1", "omvormen", "Viele bleiben zu Hause, weil es dunkel ist.", "in een weil-zin gaat het werkwoord naar het eind",
      "Viele bleiben zu Hause. Es ist dunkel. (weil) → ___", instr="Herschrijf", size=20, gap=8)
fb.ex("B1", "meerkeuze", "A", "länger als = langer dan",
      "„Länger als sonst“ betekent... A. langer dan anders · B. hetzelfde als anders · C. korter dan anders", size=20, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　Voorbeelden", [("„Meiner Meinung nach braucht das Gedenken Stille.“　„Niemand weiß, ob die Einigung gelingt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "invullen", "ob", "ob leidt een indirecte vraag in",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="Vul in", size=20, gap=8)
fc.ex("B2", "invullen", "fraglich", "Es ist fraglich, ob ... = het is twijfelachtig of ...",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="Vul in", size=20, gap=8)
fc.ex("B2", "omvormen", "Ich finde, dass das Gedenken Stille braucht.", "in een dass-zin gaat het werkwoord naar het eind",
      "Ich finde: Das Gedenken braucht Stille. (dass) → ___", instr="Herschrijf", size=20, gap=8)
fc.ex("B2", "meerkeuze", "B", "een beleefde manier om een mening te geven",
      "„Das Gedenken braucht Stille“ höflich sagen: A. „Stille, sofort!“ · B. „Meiner Meinung nach braucht das Gedenken Stille.“ · C. „Die Politik macht alles falsch.“", size=20, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["11.11 Uhr = 11.11 uur",
      "vor leeren Rängen = leeg stadion",
      "Es wird gespielt. = Er wordt gespeeld",
      "Meiner Meinung nach = naar mijn mening",
      "Ich finde, dass = ik vind dat",
      "Es ist fraglich, ob ... = twijfelachtig of"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN　Werktuig", 23, "sans", True, OLIVE)
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
label = "Een voorbeeld van de redactie!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.4."
reader = "„Liebe Lucerna, am Mittwoch bastle ich eine Laterne. Am Abend singe ich mit meiner Klasse. Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.4."
chinese = "Voorbeeld van de redactie, geen echte brief: er waren bij het ter perse gaan geen echte brieven binnen. Stuur ons die van jou voor VOL.4!"
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　Lezersbrieven", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　Nog één woord", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«das Geisterspiel» (Seite 4) : ein Spiel ohne Zuschauer im Stadion. Spookwedstrijd: geen toeschouwers.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1520
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　Zinnen van de week", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "Woord voor woord geciteerd uit de artikelen van dit nummer　bron tussen haakjes", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Die Bundesliga pausiert — aber die Nationalmannschaft spielt.", "De Bundesliga pauzeert — maar het nationale team speelt.", "Seite 4 · B1"),
    ("Um 11.11 Uhr beginnt in Köln die neue Karnevalssession.", "Om 11.11 uur begint in Keulen het nieuwe carnavalsseizoen.", "Seite 2 · A2"),
    ("Sein Gedenktag ist der 11. November.", "Zijn herdenkingsdag is 11 november.", "Seite 3 · A2"),
    ("Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut.", "De rugzakken zijn gepakt, de schoolpleinen zijn weer luid.", "Seite 5 · B1"),
    ("Der November ist dunkel, aber er ist nicht still: Er singt, leuchtet und feiert.", "November is donker, maar niet stil: hij zingt, schijnt en viert feest.", "Seite 2 · A2"),
    ("Das Spiel ist ausverkauft, RTL überträgt live.", "De wedstrijd is uitverkocht; RTL zendt live uit.", "Seite 4 · B1"),
    ("Gedenken heißt hier: innehalten, erinnern — und für Frieden und Versöhnung einstehen.", "Herdenken betekent hier: stilstaan, herinneren — en opkomen voor vrede en verzoening.", "Seite 6 · B2"),
    ("Am Sonntag ist es still im Land.", "Op zondag is het land stil.", "Seite 6 · B2"),
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
p.text(MX, ey + 28, "FEHLERKLINIK　De foutenkliniek", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Vier fouten die leerlingen het vaakst maken　corrigeer ze eerst, controleer dan", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Am Mittwoch die Kinder basteln Laternen.", "Am Mittwoch basteln die Kinder Laternen.", "Werkwoord tweede: ook als het onderwerp niet eerst staat, blijft het werkwoord tweede."),
    ("Halb zwölf ist 12.30 Uhr.", "Halb zwölf ist 11.30 Uhr.", "halb zwölf = 11.30 uur, een halfuur voor twaalf."),
    ("Die Mannschaft ist nach Herzogenaurach gereist am Montag.", "Die Mannschaft ist am Montag nach Herzogenaurach gereist.", "In de Perfekt gaat het voltooid deelwoord naar het eind."),
    ("Er fragt, ob spielt Deutschland am Freitag?", "Er fragt, ob Deutschland am Freitag spielt.", "In een ob-zin gaat het werkwoord naar het eind."),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　Volgend nummer (VOL.4)", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Freitag, 20. November: Die Bundesliga kehrt zurück — Bayern gegen Köln. Dazu die Europapokal-Spieltage (24.–26. November), Buß- und Bettag, Totensonntag — und die Ergebnisse vom 3. bis 8. November. Und Ihre Briefe: Die besten echten Briefe erscheinen in VOL.4!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
