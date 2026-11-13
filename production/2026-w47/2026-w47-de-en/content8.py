# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()

# ---- D5-de fix (W47 fix round 3): level chips for items that Flow.ex() never
# draws one for — the cloze option lines (Q113-120), the dialogue
# (Q145-149, one shared paragraph, no option lines) and writing (Q150).
# Copied from fr core content8.py D5 helpers, with de's own sizes
# (cloze option lines are 18.5 in de, not 19.5 as in fr).
# Both helpers DRAW ONLY: they never touch REG, so numbering is unchanged.
def badge_opt(flow, level, n, opts, size=18.5, lh=1.32, gap=2):
    """One cloze option line with its own level chip: chip at the row
    head, the option-line text shifted right by 72px.
    Under the text-export stubs (no _fit/_ph: export_text.py) this only
    records the option line, exactly as the old bf.para call did."""
    body = f"{n}. {opts}"
    if not hasattr(flow, "_fit"):
        flow.p.para(flow.x, flow.y + size, body, size, "sans", False, INK, 422.5, lh)
        return flow.y
    w = flow.w - 72
    lines = wrap(body, "sans", False, size, w)
    h = size + len(lines) * size * lh
    flow._fit(h + gap)
    x, y = flow.x, flow.y
    chip(flow.p, x, y, level)
    flow.y = flow.p.para(x + 72, y + size, body, size, "sans", False, INK, w, lh) + gap
    return flow.y

def badge_strip(flow, items, size=19.5, gap=9):
    """Row(s) of level chips, one per (level, n): chip + 'N.' per item,
    packed 3 per row. For items that share one paragraph (dialogue).
    Under the text-export stubs this draws nothing (chips carry no text
    for the export; the numbers already sit in the dialogue paragraph)."""
    if not hasattr(flow, "_fit"):
        return flow.y
    widths = [60 + 6 + text_w(f"{n}.", "sans", True, size) for _lv, n in items]
    rows, cur, curw = [], [], 0.0
    for it, w in zip(items, widths):
        if cur and curw + 14 + w > flow.w:
            rows.append(cur); cur, curw = [], 0.0
        cur.append((it, w)); curw += (14 if cur else 0) + w
    if cur:
        rows.append(cur)
    h = len(rows) * 30 + (len(rows) - 1) * 4  # fix3b: 行距 8->4 (chip 高 30，行距 34)
    flow._fit(h + gap)
    x0, y0 = flow.x, flow.y
    for ri, row in enumerate(rows):
        x = x0; y = y0 + ri * 34  # fix3b: 与上行一致
        for (lv, n), _w in row:
            chip(flow.p, x, y, lv)
            flow.p.text(x + 66, y + 22, f"{n}.", size, "sans", True, OLIVE)
            x += _w + 14
    flow.y = y0 + h + gap
    return flow.y
p.band("ÜBUNGEN & ANTWORTEN　Exercises and answers", "Die Lucerna", "SCHLUSSTEST　Final test　Alle Antworten unten auf dieser Seite Answers at the bottom of this page")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1555, tag="P8-battery")  # W47 D1: bottom was 1505; P8 stems at the 15.4pt concession need the extra room (writing strip moves down with wy, same 81px gap as before)

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "A", "schaut (3rd pers. sg.)"),
    ("A2", "B", "bastelt (3rd pers. sg.)"),
    ("A2", "A", "schreibt (3rd pers. sg.)"),
    ("A2", "B", "sieht (3rd pers. sg.)"),
    ("A2", "A", "beginnt (3rd pers. sg.)"),
    ("A2", "A", "liest (3rd pers. sg.)"),
    ("A2", "B", "denkt … nach (3rd pers. sg.)"),
    ("A2", "A", "ist (3rd pers. sg.)"),
]
cnums = [reg_ex(lv, "cloze", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　LÜCKENTEXT　Cloze", 24)
bf.para(f"Lena freut sich auf die Novemberwoche. Am Montag ({cnums[0]})___ sie die Nationalelf in Berlin. Am Mittwoch ({cnums[1]})___ sie einen Adventskalender und ({cnums[2]})___ ihren Wunschzettel. Am Freitag ({cnums[3]})___ sie Bayern gegen Köln im Fernsehen. Der Advent ({cnums[4]})___ am 29. November. Die Märkte sind am Sonntag geschlossen — Lena ({cnums[5]})___ ein Buch und ({cnums[6]})___ über den Totensonntag nach. Am Mittwoch ({cnums[7]})___ kein Unterricht in Bayern.", 19.5)
bf.bridge("Options:")
for n, (lv, _k, _nt), opts in zip(cnums, cloze_defs, [
    "A. schaut · B. schauen · C. schaute",
    "A. basteln · B. bastelt · C. bastelte",
    "A. schreibt · B. schreiben · C. schrieb",
    "A. sehen · B. sieht · C. sah",
    "A. beginnt · B. beginnen · C. begann",
    "A. liest · B. lesen · C. las",
    "A. denken · B. denkt · C. dachte",
    "A. ist · B. sind · C. war",
]):
    badge_opt(bf, lv, n, opts)

# ---- B. general MC ----
# W47 fix3b (收尾): B–E 共 20 个 ex() 的 gap 6→3 —— 上一棒 FIX-LOG 称已改，实测文件仍为 gap=6，
# 三份 build12 日志字节相同即为明证；此处才是真正落盘。省 20×3=60px，电池流 1472.44→1412.44，P8 图恢复 ~139.6px。
bf.head("B　WISSENSFRAGEN　Quiz", 24)
bf.ex("B1", "multiple choice", "A", "Bundesliga returns 20 November",
      "Die Bundesliga kehrt zurück am... A. 20. November · B. 13. November · C. 29. November", size=20.5, gap=3)
bf.ex("A2", "multiple choice", "B", "Bayern v Cologne 20.30",
      "Bayern – Köln beginnt um... A. 15.30 Uhr · B. 20.30 Uhr · C. 17.30 Uhr", size=20.5, gap=3)
bf.ex("B1", "multiple choice", "B", "v Netherlands 16 November",
      "Deutschland spielt gegen die Niederlande am... A. 13. November · B. 16. November · C. 22. November", size=20.5, gap=3)
bf.ex("B1", "multiple choice", "B", "Only Saxony has the day off",
      "In welchem Bundesland ist der Buß- und Bettag ein Feiertag? A. Bayern · B. Sachsen · C. Nordrhein-Westfalen", size=20.5, gap=3)
bf.ex("A2", "multiple choice", "B", "Totensonntag: 22 November",
      "Der Totensonntag ist am... A. 18. November · B. 22. November · C. 29. November", size=20.5, gap=3)
bf.ex("A2", "multiple choice", "A", "Cologne markets open 16 November",
      "Die Weihnachtsmärkte in Köln öffnen am... A. 16. November · B. 23. November · C. 29. November", size=20.5, gap=3)
bf.ex("B1", "multiple choice", "B", "Household electricity tax 2.05 cents",
      "Die Stromsteuer für Haushalte beträgt... A. 2,50 Cent · B. 2,05 Cent · C. 0,05 Cent", size=20.5, gap=3)
bf.ex("A2", "multiple choice", "B", "first Advent: 29 November",
      "Der erste Advent ist am... A. 22. November · B. 29. November · C. 16. November", size=20.5, gap=3)

# ---- C. reading ----
bf.head("C　LESEVERSTEHEN　Reading", 24)
bf.para("Familie Berger aus Stuttgart hat eine volle Novemberwoche. Am Montag schaut die Familie Deutschland gegen die Niederlande im Fernsehen. Am Mittwoch bastelt die Familie einen Adventskalender. Am Freitag schaut sie Bayern gegen Köln. Am Sonntag ist Totensonntag: Die Familie geht auf den Friedhof und zündet Kerzen an. „Eine stille, schöne Woche“, sagt Frau Berger.", 19.5)
bf.ex("B1", "multiple choice", "A", "Germany v Netherlands on Monday",
      "Was schaut die Familie am Montag? A. Deutschland gegen die Niederlande · B. die Bundesliga · C. den Adventskalender", size=20.5, gap=3)
bf.ex("A2", "multiple choice", "B", "Advent calendar on Wednesday",
      "Was bastelt die Familie am Mittwoch? A. eine Kerze · B. einen Adventskalender · C. einen Weihnachtsbaum", size=20.5, gap=3)
bf.ex("A2", "multiple choice", "B", "Bayern v Cologne on Friday",
      "Was schaut die Familie am Freitag? A. Deutschland gegen die Niederlande · B. Bayern gegen Köln · C. die Weihnachtsmärkte", size=20.5, gap=3)
bf.ex("B1", "multiple choice", "B", "Cemetery and candles on Sunday",
      "Was macht die Familie am Sonntag? A. Sie geht auf den Weihnachtsmarkt. · B. Sie geht auf den Friedhof und zündet Kerzen an. · C. Sie bastelt einen Adventskalender.", size=20.5, gap=3)

# ---- D. sentence building ----
bf.head("D　SÄTZE BAUEN　Sentences", 24)
bf.ex("A2", "sentence building", "Die Bundesliga kehrt am Freitag zurück.", "time, verb second",
      "die Bundesliga / kehrt / am Freitag / zurück → ___", instr="Build a sentence", size=20.5, gap=3)
bf.ex("A2", "sentence building", "Wir basteln im November einen Adventskalender.", "S-V-O order",
      "wir / basteln / einen Adventskalender / im November → ___", instr="Build a sentence", size=20.5, gap=3)
bf.ex("B1", "sentence building", "Am Sonntag sind die Weihnachtsmärkte geschlossen.", "time first, verb second",
      "am Sonntag / sind / die Weihnachtsmärkte / geschlossen → ___", instr="Build a sentence", size=20.5, gap=3)
bf.ex("B1", "sentence building", "Die Familie geht am Sonntag auf den Friedhof.", "S-V-O order",
      "die Familie / geht / am Sonntag / auf den Friedhof → ___", instr="Build a sentence", size=20.5, gap=3)

# ---- E. translation ----
bf.head("E　ÜBERSETZEN　Translation", 24)
bf.ex("A2", "translation", "The Bundesliga returns on Friday.", "kehren zurück = to return",
      "Die Bundesliga kehrt am Freitag zurück. (Translate into English)", instr="Translate into English", size=20.5, gap=3)
bf.ex("A2", "translation", "The markets are shut on Sunday.", "geschlossen = shut",
      "Die Märkte sind am Sonntag geschlossen. (Translate into English)", instr="Translate into English", size=20.5, gap=3)
bf.ex("B1", "translation", "I am making an Advent calendar.", "basteln = to make, to craft",
      "Ich bastle einen Adventskalender. (Translate into English)", instr="Translate into English", size=20.5, gap=3)
bf.ex("B1", "translation", "Am Montag schaue ich zu Hause Deutschland gegen die Niederlande.", "watching a game = das Spiel schauen",
      "On Monday I watch Germany against the Netherlands at home. (Translate into German.)", instr="Translate into German", size=20.5, gap=3)

# ---- F. matching ----
bf.head("F　WÖRTER PAAREN　Matching", 24, gap=5)  # fix3b: col3 间距补偿
bf.match_set("B1", "matching",
             ["der Wunschzettel", "das Türchen", "der Glühwein", "der Friedhof"],
             ["das kleine Fenster im Adventskalender, hinter dem eine Überraschung wartet",
              "der Ort, an dem man der Verstorbenen gedenkt",
              "die Liste mit Wünschen für Weihnachten",
              "der warme, gewürzte Wein, den man auf Weihnachtsmärkten trinkt"],
             ["c", "a", "d", "b"],
             ["Wunschzettel=wish list c", "Türchen=little door a", "Glühwein=mulled wine d", "Friedhof=cemetery b"],
             instr="Match the words", gap=0)  # fix3b: col3 间距补偿

# ---- G. dialogue ----
ddefs = [
    ("A2", "A", "öffne (1st pers. sg.)"),
    ("A2", "B", "machst (2nd pers. sg.)"),
    ("A2", "A", "schaue (1st pers. sg.)"),
    ("B1", "A", "schaue (1st pers. sg.)"),
    ("A2", "A", "lese (1st pers. sg.)"),
]
dnums = [reg_ex(lv, "dialogue completion", k, nt) for lv, k, nt in ddefs]
bf.head("G　DIALOG　Dialogue", 24, gap=5)  # fix3b: col3 间距补偿
badge_strip(bf, [(lv, n) for n, (lv, _k, _nt) in zip(dnums, ddefs)], gap=3)  # fix3b: col3 间距补偿
bf.para(f"— Hallo, Lena! Bastelst du einen Adventskalender? — Ja, für Weihnachten! Am 1. Dezember ({dnums[0]})___ ich das erste Türchen. — Und was ({dnums[1]})___ du am Freitag? — Ich ({dnums[2]})___ Bayern gegen Köln im Fernsehen. — Und am Montag? — Da ({dnums[3]})___ ich die Nationalelf gegen die Niederlande. — Und am Sonntag? — Da ({dnums[4]})___ ich ein Buch und bleibe zu Hause.", 19.5, gap=3)  # fix3b: col3 间距补偿
bf.bridge("Options:", gap=3)  # fix3b: col3 间距补偿
for n, opts in zip(dnums, [
    "A. öffne · B. öffnest · C. öffnen",
    "A. mache · B. machst · C. macht",
    "A. schaue · B. schaust · C. schaut",
    "A. schaue · B. schaust · C. schaut",
    "A. lese · B. liest · C. lesen",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 0)  # fix3b: col3 间距补偿，单行选项行无需行距
bf.end_report()

# ---- P8 image: football 1905, col 3 below the battery ----
wy = 1650  # W47 D1: was 1600; battery bottom moved to 1555, strip follows (keys end ~2378, bottom 2560)
iy8 = bf.y + 12
ih8 = min(140, (wy - 14) - (iy8 + 72))
print("P8 image height", ih8)
image(p, "fussball1905.jpg", COLX[3], iy8, CW, ih8)
cy8 = caption(p, COLX[3], iy8 + ih8, CW,
              "Fußball 1905: Schweiz gegen Frankreich.",
              "Foto: unbekannter Fotograf, 1905 — public domain")
print("P8 battery ends col3", bf.y, "| image ends", cy8)

# ---- writing strip ----
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "writing", "Open task — follow the points in the writing box", "Marked against the points listed")
wx, ww = span_x(0, 2)
chip(p, wx, wy, "B1")  # D5-de fix: writing (Q150) gets its own level chip
p.text(wx + 72, wy + 26, "H　SCHREIBEN　Writing", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Novemberwoche». Erzählen Sie: Was basteln Sie? Welche Spiele schauen Sie? Mit wem? Schreiben Sie auch einen Satz über den Buß- und Bettag oder den Totensonntag! Die besten Texte drucken wir in VOL.5 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "Write in German, 80–100 words: „My week in November“. Say what you make, which games you watch and with whom — and add one sentence about the Buß- und Bettag or Totensonntag.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX)
p.text(mx2 + 22, wy + 38, "MUSTER　Model text (84 words)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche bastle ich einen Adventskalender. Am Mittwoch öffne ich kein Türchen — das erste Türchen öffnet sich erst am 1. Dezember. Am Montag schaue ich mit meiner Familie die Nationalelf gegen die Niederlande. Am Freitag schaue ich Bayern gegen Köln im Fernsehen. Die Bayern führen die Tabelle an. Am Mittwoch ist Buß- und Bettag: In Bayern habe ich keinen Unterricht. Am Sonntag ist Totensonntag. Die Weihnachtsmärkte in Köln sind geschlossen. Ich lese ein Buch und bleibe zu Hause. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 320
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANTWORTEN　All answers with notes (pages 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Page {pg} —", 16, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13.25, "sans", False, INK, 1.18, 4)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
