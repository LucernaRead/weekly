# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-de-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE · La lingua", "Die Lucerna", "A2 → B2 · Sätze der Woche & Fehlerklinik · Frasi della settimana e clinica degli errori")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "Questa pagina è tutta lingua: tre brevi lezioni, le frasi della settimana (citate parola per parola dagli articoli di questo numero), la clinica degli errori e le lettere dei lettori.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2 · UHRZEITEN & DATEN", 24)
fa.para("So sagen Sie Uhrzeiten und Daten: Um 11.11 Uhr beginnt der Karneval. Am 15. November ist Volkstrauertag. Mit werden sprechen Sie über das Passiv: Um 20.45 Uhr wird in Belgrad gespielt. Die NFL wird in München gespielt.")
fa.box("BEISPIELE · Esempi", [("„Um 11.11 Uhr beginnt der Karneval.“ · „Am Sonntag wird in München Football gespielt.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "completare", "wird", "passivo: wird + participio passato",
      "Am Freitag ___ in Belgrad gespielt.", instr="Completa", size=20, gap=8)
fa.ex("A2", "completare", "werden", "plurale: werden",
      "Am 11. November ___ zwei Feste gefeiert.", instr="Completa", size=20, gap=8)
fa.ex("A2", "completare", "wird", "werden + infinito per il futuro",
      "Die Karnevalssession ___ um 11.11 Uhr beginnen.", instr="Completa", size=20, gap=8)
fa.ex("A2", "scelta multipla", "A", "forma passiva",
      "„Es wird gespielt“ ist... A. Passiv · B. Perfekt · C. Imperativ", size=20, gap=8)
fa.end_report()
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1 · VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Die Nacht ist länger als der Tag. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es dunkel ist — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE · Esempi", [("„Die Nacht ist länger als der Tag.“ · „Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "completare", "länger", "lang → länger (la notte è più lunga del giorno)",
      "Im November ist die Nacht ___ (lang) als der Tag.", instr="Completa", size=20, gap=8)
fb.ex("B1", "completare", "weil", "weil introduce una causa",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="Completa", size=20, gap=8)
fb.ex("B1", "trasformazione", "Viele bleiben zu Hause, weil es dunkel ist.", "in una subordinata con weil il verbo va alla fine",
      "Viele bleiben zu Hause. Es ist dunkel. (weil) → ___", instr="Riscrivi", size=20, gap=8)
fb.ex("B1", "scelta multipla", "A", "länger als = più lungo di",
      "„Länger als sonst“ significa... A. più lungo del solito · B. come al solito · C. più corto del solito", size=20, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2 · MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE · Esempi", [("„Meiner Meinung nach braucht das Gedenken Stille.“ · „Niemand weiß, ob die Einigung gelingt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "completare", "ob", "ob introduce una domanda indiretta",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="Completa", size=20, gap=8)
fc.ex("B2", "completare", "fraglich", "Es ist fraglich, ob ... = è dubbio che ...",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="Completa", size=20, gap=8)
fc.ex("B2", "trasformazione", "Ich finde, dass das Gedenken Stille braucht.", "in una subordinata con dass il verbo va alla fine",
      "Ich finde: Das Gedenken braucht Stille. (dass) → ___", instr="Riscrivi", size=20, gap=8)
fc.ex("B2", "scelta multipla", "B", "un modo gentile di dare un'opinione",
      "„Das Gedenken braucht Stille“ höflich sagen: A. „Stille, sofort!“ · B. „Meiner Meinung nach braucht das Gedenken Stille.“ · C. „Die Politik macht alles falsch.“", size=20, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["11.11 Uhr = 11.11",
      "vor leeren Rängen = stadio vuoto",
      "Es wird gespielt. = Si gioca",
      "Meiner Meinung nach = secondo me",
      "Ich finde, dass = penso che",
      "Es ist fraglich, ob ... = è dubbio che"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN · Attrezzi", 23, "sans", True, OLIVE)
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
label = "Un esempio della redazione!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.4."
reader = "„Liebe Lucerna, am Mittwoch bastle ich eine Laterne. Am Abend singe ich mit meiner Klasse. Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.4."
chinese = "Esempio della redazione, non una vera lettera: nessuna vera lettera era arrivata alla chiusura. Mandateci le vostre per VOL.4!"
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16
p.rect(ix, ry, CW, rh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE · Lettere", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, BRICK, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT · Ancora una parola", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«das Geisterspiel» (Seite 4) : ein Spiel ohne Zuschauer im Stadion. Partita fantasma: una partita senza spettatori.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1520
p.hline(MX, RIGHT, py - 12, GOLD, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE · Frasi della settimana", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "Citato parola per parola dagli articoli di questo numero · fonte tra parentesi", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Die Bundesliga pausiert — aber die Nationalmannschaft spielt.", "La Bundesliga si ferma — ma gioca la nazionale.", "Seite 4 · B1"),
    ("Um 11.11 Uhr beginnt in Köln die neue Karnevalssession.", "Alle 11.11 inizia a Colonia la nuova sessione di carnevale.", "Seite 2 · A2"),
    ("Sein Gedenktag ist der 11. November.", "Il suo giorno del ricordo è l'11 novembre.", "Seite 3 · A2"),
    ("Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut.", "Gli zaini sono pronti, i cortili tornano rumorosi.", "Seite 5 · B1"),
    ("Der November ist dunkel, aber er ist nicht still: Er singt, leuchtet und feiert.", "Novembre è buio, ma non silenzioso: canta, brilla e festeggia.", "Seite 2 · A2"),
    ("Das Spiel ist ausverkauft, RTL überträgt live.", "La partita è esaurita; RTL trasmette in diretta.", "Seite 4 · B1"),
    ("Gedenken heißt hier: innehalten, erinnern — und für Frieden und Versöhnung einstehen.", "Qui ricordare significa: fermarsi, ricordare — e difendere la pace e la riconciliazione.", "Seite 6 · B2"),
    ("Am Sonntag ist es still im Land.", "Domenica il paese è silenzioso.", "Seite 6 · B2"),
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
p.text(MX, ey + 28, "FEHLERKLINIK · La clinica degli errori", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Quattro errori frequenti degli studenti · correggili prima, poi controlla", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Am Mittwoch die Kinder basteln Laternen.", "Am Mittwoch basteln die Kinder Laternen.", "Verbo al secondo posto: anche se il soggetto non è primo, il verbo resta secondo."),
    ("Halb zwölf ist 12.30 Uhr.", "Halb zwölf ist 11.30 Uhr.", "halb zwölf = 11.30, mezz'ora prima di zwölf."),
    ("Die Mannschaft ist nach Herzogenaurach gereist am Montag.", "Die Mannschaft ist am Montag nach Herzogenaurach gereist.", "Nel Perfekt il participio passato va alla fine."),
    ("Er fragt, ob spielt Deutschland am Freitag?", "Er fragt, ob Deutschland am Freitag spielt.", "In una subordinata con ob il verbo va alla fine."),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE · Prossimo numero (VOL.4)", 24, "sans", True, "#f3edda")
p.para(MX + 26, ty + 82, "Freitag, 20. November: Die Bundesliga kehrt zurück — Bayern gegen Köln. Dazu die Europapokal-Spieltage (24.–26. November), Buß- und Bettag, Totensonntag — und die Ergebnisse vom 3. bis 8. November. Und Ihre Briefe: Die besten echten Briefe erscheinen in VOL.4!", 21, "serif", False, "#e8dfc8", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
