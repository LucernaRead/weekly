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
p.band("ÜBUNGEN & ANTWORTEN　Oefeningen en antwoorden", "Die Lucerna", "SCHLUSSTEST　Eindtoets　Alle Antworten unten auf dieser Seite Antwoorden onderaan deze pagina")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1555, tag="P8-battery")  # W47 D1: bottom was 1505; P8 stems at the 15.4pt concession need the extra room (writing strip moves down with wy, same 81px gap as before)

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "A", "schaut (3e pers. enk.)"),
    ("A2", "B", "bastelt (3e pers. enk.)"),
    ("A2", "A", "schreibt (3e pers. enk.)"),
    ("A2", "B", "sieht (3e pers. enk.)"),
    ("A2", "A", "beginnt (3e pers. enk.)"),
    ("A2", "A", "liest (3e pers. enk.)"),
    ("A2", "B", "denkt … nach (3e pers. enk.)"),
    ("A2", "A", "ist (3e pers. enk.)"),
]
cnums = [reg_ex(lv, "gatentekst", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　LÜCKENTEXT　Gatentekst", 24)
bf.para(f"Lena freut sich auf die Novemberwoche. Am Montag ({cnums[0]})___ sie die Nationalelf in Berlin. Am Mittwoch ({cnums[1]})___ sie einen Adventskalender und ({cnums[2]})___ ihren Wunschzettel. Am Freitag ({cnums[3]})___ sie Bayern gegen Köln im Fernsehen. Der Advent ({cnums[4]})___ am 29. November. Die Märkte sind am Sonntag geschlossen — Lena ({cnums[5]})___ ein Buch und ({cnums[6]})___ über den Totensonntag nach. Am Mittwoch ({cnums[7]})___ kein Unterricht in Bayern.", 19.5)
bf.bridge("Opties:")
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
bf.ex("B1", "meerkeuze", "A", "Bundesliga terug op 20 november",
      "Die Bundesliga kehrt zurück am... A. 20. November · B. 13. November · C. 29. November", size=20.5, gap=3)
bf.ex("A2", "meerkeuze", "B", "Bayern–Köln, 20.30 uur",
      "Bayern – Köln beginnt um... A. 15.30 Uhr · B. 20.30 Uhr · C. 17.30 Uhr", size=20.5, gap=3)
bf.ex("B1", "meerkeuze", "B", "Nederland, 16 nov.",
      "Deutschland spielt gegen die Niederlande am... A. 13. November · B. 16. November · C. 22. November", size=20.5, gap=3)
bf.ex("B1", "meerkeuze", "B", "Alleen Saksen is vrij",
      "In welchem Bundesland ist der Buß- und Bettag ein Feiertag? A. Bayern · B. Sachsen · C. Nordrhein-Westfalen", size=20.5, gap=3)
bf.ex("A2", "meerkeuze", "B", "Totensonntag: 22 nov.",
      "Der Totensonntag ist am... A. 18. November · B. 22. November · C. 29. November", size=20.5, gap=3)
bf.ex("A2", "meerkeuze", "A", "Kerstmarkten Keulen: 16 november",
      "Die Weihnachtsmärkte in Köln öffnen am... A. 16. November · B. 23. November · C. 29. November", size=20.5, gap=3)
bf.ex("B1", "meerkeuze", "B", "Stroomtaks: 2,05 cent",
      "Die Stromsteuer für Haushalte beträgt... A. 2,50 Cent · B. 2,05 Cent · C. 0,05 Cent", size=20.5, gap=3)
bf.ex("A2", "meerkeuze", "B", "Eerste zondag van de advent: 29 nov.",
      "Der erste Advent ist am... A. 22. November · B. 29. November · C. 16. November", size=20.5, gap=3)

# ---- C. reading ----
bf.head("C　LESEVERSTEHEN　Lezen", 24)
bf.para("Familie Berger aus Stuttgart hat eine volle Novemberwoche. Am Montag schaut die Familie Deutschland gegen die Niederlande im Fernsehen. Am Mittwoch bastelt die Familie einen Adventskalender. Am Freitag schaut sie Bayern gegen Köln. Am Sonntag ist Totensonntag: Die Familie geht auf den Friedhof und zündet Kerzen an. „Eine stille, schöne Woche“, sagt Frau Berger.", 19.5)
bf.ex("B1", "meerkeuze", "A", "Duitsland–Nederland, maandag",
      "Was schaut die Familie am Montag? A. Deutschland gegen die Niederlande · B. die Bundesliga · C. den Adventskalender", size=20.5, gap=3)
bf.ex("A2", "meerkeuze", "B", "Kalender, woensdag",
      "Was bastelt die Familie am Mittwoch? A. eine Kerze · B. einen Adventskalender · C. einen Weihnachtsbaum", size=20.5, gap=3)
bf.ex("A2", "meerkeuze", "B", "Bayern–Köln, vrijdag",
      "Was schaut die Familie am Freitag? A. Deutschland gegen die Niederlande · B. Bayern gegen Köln · C. die Weihnachtsmärkte", size=20.5, gap=3)
bf.ex("B1", "meerkeuze", "B", "Begraafplaats en kaarsen, zondag",
      "Was macht die Familie am Sonntag? A. Sie geht auf den Weihnachtsmarkt. · B. Sie geht auf den Friedhof und zündet Kerzen an. · C. Sie bastelt einen Adventskalender.", size=20.5, gap=3)

# ---- D. sentence building ----
bf.head("D　SÄTZE BAUEN　Zinnen", 24)
bf.ex("A2", "zinnen bouwen", "Die Bundesliga kehrt am Freitag zurück.", "tijd, werkwoord op 2",
      "die Bundesliga / kehrt / am Freitag / zurück → ___", instr="Bouw een zin", size=20.5, gap=3)
bf.ex("A2", "zinnen bouwen", "Wir basteln im November einen Adventskalender.", "volgorde S-V-O",
      "wir / basteln / einen Adventskalender / im November → ___", instr="Bouw een zin", size=20.5, gap=3)
bf.ex("B1", "zinnen bouwen", "Am Sonntag sind die Weihnachtsmärkte geschlossen.", "tijd, werkwoord op 2",
      "am Sonntag / sind / die Weihnachtsmärkte / geschlossen → ___", instr="Bouw een zin", size=20.5, gap=3)
bf.ex("B1", "zinnen bouwen", "Die Familie geht am Sonntag auf den Friedhof.", "volgorde S-V-O",
      "die Familie / geht / am Sonntag / auf den Friedhof → ___", instr="Bouw een zin", size=20.5, gap=3)

# ---- E. translation ----
bf.head("E　ÜBERSETZEN　Vertaling", 24)
bf.ex("A2", "vertaling", "De Bundesliga keert vrijdag terug.", "kehren zurück = terugkeren",
      "Die Bundesliga kehrt am Freitag zurück. (Vertaal in het Nederlands)", instr="Vertaal in het Nederlands", size=20.5, gap=3)
bf.ex("A2", "vertaling", "De markten zijn zondag dicht.", "geschlossen = dicht",
      "Die Märkte sind am Sonntag geschlossen. (Vertaal in het Nederlands)", instr="Vertaal in het Nederlands", size=20.5, gap=3)
bf.ex("B1", "vertaling", "Ik maak een adventskalender.", "basteln = knutselen",
      "Ich bastle einen Adventskalender. (Vertaal in het Nederlands)", instr="Vertaal in het Nederlands", size=20.5, gap=3)
bf.ex("B1", "vertaling", "Am Montag schaue ich zu Hause Deutschland gegen die Niederlande.", "een wedstrijd kijken = das Spiel schauen",
      "Op maandag kijk ik thuis naar Duitsland tegen Nederland. (Vertaal in het Duits.)", instr="Vertaal in het Duits", size=20.5, gap=3)

# ---- F. matching ----
bf.head("F　WÖRTER PAAREN　Combineren", 22, gap=5)  # fix3b: col3 间距补偿; D5 (2026-11-12): @24pt 440.9px > column 422.5px (HEAD TOO WIDE); @22pt 404.2px fits. No wording change.
bf.match_set("B1", "combineren",
             ["der Wunschzettel", "das Türchen", "der Glühwein", "der Friedhof"],
             ["das kleine Fenster im Adventskalender, hinter dem eine Überraschung wartet",
              "der Ort, an dem man der Verstorbenen gedenkt",
              "die Liste mit Wünschen für Weihnachten",
              "der warme, gewürzte Wein, den man auf Weihnachtsmärkten trinkt"],
             ["c", "a", "d", "b"],
             ["Wunschzettel=verlanglijst c", "Türchen=deurtje a", "Glühwein=glühwein d", "Friedhof=begraafplaats b"],
             instr="Combineer de woorden", gap=0)  # fix3b: col3 间距补偿

# ---- G. dialogue ----
ddefs = [
    ("A2", "A", "öffne (1e pers. enk.)"),
    ("A2", "B", "machst (2e pers. enk.)"),
    ("A2", "A", "schaue (1e pers. enk.)"),
    ("B1", "A", "schaue (1e pers. enk.)"),
    ("A2", "A", "lese (1e pers. enk.)"),
]
dnums = [reg_ex(lv, "dialoog aanvullen", k, nt) for lv, k, nt in ddefs]
bf.head("G　DIALOG　Dialoog", 24, gap=5)  # fix3b: col3 间距补偿
badge_strip(bf, [(lv, n) for n, (lv, _k, _nt) in zip(dnums, ddefs)], gap=3)  # fix3b: col3 间距补偿
bf.para(f"— Hallo, Lena! Bastelst du einen Adventskalender? — Ja, für Weihnachten! Am 1. Dezember ({dnums[0]})___ ich das erste Türchen. — Und was ({dnums[1]})___ du am Freitag? — Ich ({dnums[2]})___ Bayern gegen Köln im Fernsehen. — Und am Montag? — Da ({dnums[3]})___ ich die Nationalelf gegen die Niederlande. — Und am Sonntag? — Da ({dnums[4]})___ ich ein Buch und bleibe zu Hause.", 19.5, gap=3)  # fix3b: col3 间距补偿
bf.bridge("Opties:", gap=3)  # fix3b: col3 间距补偿
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
reg_ex("B1", "schrijven", "Open opdracht — volg de punten in het schrijfblok", "Beoordeeld op de genoemde punten")
wx, ww = span_x(0, 2)
chip(p, wx, wy, "B1")  # D5-de fix: writing (Q150) gets its own level chip
p.text(wx + 72, wy + 26, "H　SCHREIBEN　Schrijven", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Novemberwoche». Erzählen Sie: Was basteln Sie? Welche Spiele schauen Sie? Mit wem? Schreiben Sie auch einen Satz über den Buß- und Bettag oder den Totensonntag! Die besten Texte drucken wir in VOL.5 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "Schrijf in het Duits, 80–100 woorden: «Mijn week in november». Vertel wat je knutselt, welke wedstrijden je kijkt en met wie, en voeg één zin toe over de Buß- und Bettag of Totensonntag.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX)
p.text(mx2 + 22, wy + 38, "MUSTER　Voorbeeldtekst (84 woorden)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche bastle ich einen Adventskalender. Am Mittwoch öffne ich kein Türchen — das erste Türchen öffnet sich erst am 1. Dezember. Am Montag schaue ich mit meiner Familie die Nationalelf gegen die Niederlande. Am Freitag schaue ich Bayern gegen Köln im Fernsehen. Die Bayern führen die Tabelle an. Am Mittwoch ist Buß- und Bettag: In Bayern habe ich keinen Unterricht. Am Sonntag ist Totensonntag. Die Weihnachtsmärkte in Köln sind geschlossen. Ich lese ein Buch und bleibe zu Hause. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 320
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANTWORTEN　Alle antwoorden met uitleg (p. 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Pagina {pg} —", 16, "sans", True, OLIVE, 1.28, 3)
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
