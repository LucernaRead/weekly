# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　Language", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　Sentences of the week and the error clinic")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "This page is all about language: three short lessons, the sentences of the week (all quoted verbatim from this issue), the error clinic — and your letters.", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　DATEN SAGEN", 24)
fa.para("So sagen Sie Daten: Am 18. November ist Buß- und Bettag. Am 29. November ist der erste Advent. Mit werden sprechen Sie über das Passiv: Um 20.30 Uhr wird in München gespielt.")
fa.box("BEISPIELE　Examples", [("„Am 18. November ist Buß- und Bettag.“　„Um 20.30 Uhr wird in München gespielt.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "fill-in", "wird", "wird + past participle",
      "Am Freitag ___ in München gespielt.", instr="Fill in", size=22, gap=8)
fa.ex("A2", "fill-in", "werden", "Plural: werden",
      "Die Weihnachtsmärkte ___ am Montag geöffnet.", instr="Fill in", size=22, gap=8)
fa.ex("A2", "fill-in", "wird", "werden + infinitive: future",
      "Der Adventskalender ___ am 1. Dezember beginnen.", instr="Fill in", size=22, gap=8)
fa.ex("A2", "multiple choice", "A", "passive",
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
fb.box("BEISPIELE　Examples", [("„Der November ist stiller als der Oktober.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "fill-in", "stiller", "still → stiller (quieter than October)",
      "Im November ist es ___ (still) als im Oktober.", instr="Fill in", size=22, gap=8)
fb.ex("B1", "fill-in", "weil", "weil: reason",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="Fill in", size=22, gap=8)
fb.ex("B1", "transformation", "Viele bleiben zu Hause, weil es dunkel ist.", "weil: verb last",
      "Viele bleiben zu Hause. Es ist dunkel. (weil) → ___", instr="Rewrite", size=22, gap=8)
fb.ex("B1", "multiple choice", "A", "stiller als = quieter than …",
      "„Stiller als sonst“ heißt... A. quieter than usual · B. the same as usual · C. noisier than usual", size=22, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　Examples", [("„Meiner Meinung nach braucht das Gedenken Stille.“　„Niemand weiß, ob die Einigung gelingt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "fill-in", "ob", "ob: indirect question",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="Fill in", size=22, gap=8)
fc.ex("B2", "fill-in", "fraglich", "fraglich: whether … is still doubtful",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="Fill in", size=22, gap=8)
fc.ex("B2", "transformation", "Ich finde, dass das Gedenken Stille braucht.", "dass: verb last",
      "Ich finde: Das Gedenken braucht Stille. (dass) → ___", instr="Rewrite", size=22, gap=8)
fc.ex("B2", "multiple choice", "B", "polite opinion",
      "„Das Gedenken braucht Stille“ höflich sagen: A. „Stille, sofort!“ · B. „Meiner Meinung nach braucht das Gedenken Stille.“ · C. „Die Politik macht alles falsch.“", size=22, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["18. November = 18 November",
      "der Buß- und Bettag = repentance and prayer",
      "vor fast leeren Rängen = in front of almost empty stands",
      "Es wird gespielt. = The match will be played (passive)",
      "Meiner Meinung nach = In my opinion",
      "Es ist fraglich, ob ... = Whether … is open"]
tbh = None  # computed below from the simulated ink end (D3 fix, see note)
# D3 fix (2026-11-11): the old formula (62 + sum(lines*29.5+6) + 90) misses the
# +20.5 first-baseline offset of every p.para call, so the box (bottom 783.5)
# ended 0.4px ABOVE the last baseline 783.9 -- the 'g' of 'fraglich' spilled
# ~4.7px onto bare paper (creambox clearance -0.4, the only negative box).
# p.para returns first_baseline + nlines*20.5*1.42 and the loop adds +6 after
# each entry; simulate that exactly, then keep 16px below the last baseline
# (inside the +10.4..+47.7 range of the other cream boxes; ~11px below the
# descender). ry/rh/wy3 below shift down by the same delta; NOCH EIN WORT
# then ends ~1534.4, still 13.6px clear of the 1548 Saetze rule.
_tb_y = CTOP + 16 + 52
for _t in tb:
    _tb_y += 20.5 + len(wrap(_t, "serif", False, 20.5, CW - 44)) * 20.5 * 1.42 + 6
_last_base = _tb_y - 6 - 20.5 * 1.42
tbh = _last_base - CTOP + 16
p.rect(ix, CTOP, CW, tbh, fill=BOX)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN　Toolbox", 21, "sans", True, OLIVE)  # D5 (2026-11-12): @23pt 423.1px ran +23.0px past the box; @21pt 386.4px fits 400.5. No wording change.
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
label = "Ein Beispiel der Redaktion!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.5."
reader = "„Liebe Lucerna, im November bastle ich einen Adventskalender. Am 1. Dezember öffne ich das erste Türchen. Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.5."
chinese = "Editor's example — no real letters had arrived by press time. Send us your writing for VOL.5."
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　Readers' letters", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　One more word", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«der Adventskalender» (page 5): a calendar with 24 little doors until Christmas. Advent calendar.", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1560
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　Sentences of the week", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "Quoted verbatim from this issue　Source in brackets", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln.", "After a two-week break, Bayern play Cologne on Friday evening.", "Seite 1 · A2"),
    ("Es geht ums Viertelfinale der Nations League.", "It is all about the Nations League quarter-final.", "Seite 1 · A2"),
    ("Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag.", "Only in Saxony is the Buß- und Bettag a public holiday.", "Seite 2 · A2"),
    ("Die Märkte beginnen fast zwei Wochen früher.", "The markets start almost two weeks early.", "Seite 3 · A2"),
    ("Hinter jedem Türchen wartet eine kleine Überraschung.", "Behind every little door waits a small surprise.", "Seite 5 · B1"),
    ("Der FC Bayern gewann in Mainz mit 2:1.", "Bayern won 2–1 in Mainz.", "Seite 4 · B1"),
    ("Die stille Woche ist der Übergang: vom November in den Advent.", "The quiet week is the transition: from November into Advent.", "Seite 6 · B2"),
    ("Am Sonntag ist es still im Land.", "On Sunday, the whole country is quiet.", "Seite 6 · B2"),
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
p.text(MX, ey + 28, "FEHLERKLINIK　Error clinic", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Learners' four most common mistakes　Correct them first, then check", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Am Mittwoch die Kinder basteln einen Adventskalender.", "Am Mittwoch basteln die Kinder einen Adventskalender.", "Verb second: even when the subject is not first, the verb stays second."),
    ("Halb neun ist 9.30 Uhr.", "Halb neun ist 8.30 Uhr.", "halb neun = half past eight (before neun)."),
    ("Die Mannschaft ist nach Berlin gereist am Montag.", "Die Mannschaft ist am Montag nach Berlin gereist.", "Perfekt: participle last"),
    ("Er fragt, ob spielt die Nationalelf am Montag?", "Er fragt, ob die Nationalelf am Montag spielt.", "ob: verb last"),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　Next issue (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Sonntag, 29. November: Der erste Advent beginnt — Kerzen, Lieder und das erste Türchen. Dazu die Ergebnisse der Europapokale (24.–26. November), der 11. Spieltag und die Weihnachtsmärkte in vollem Gang. Und Ihre Briefe: Die besten echten Briefe erscheinen in VOL.5!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
