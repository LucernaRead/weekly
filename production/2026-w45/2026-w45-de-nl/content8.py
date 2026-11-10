# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN　Oefeningen & antwoorden", "Die Lucerna", "SCHLUSSTEST　Eindtoets　Alle antwoorden staan onderaan deze pagina")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "spielt (3e persoon enkelvoud)"),
    ("A2", "A", "beginnt (3e persoon enkelvoud)"),
    ("A2", "B", "kauft (3e persoon enkelvoud)"),
    ("A2", "C", "schnitzt (een pompoen uithollen)"),
    ("A2", "B", "schläft (3e persoon enkelvoud)"),
    ("B1", "B", "Tankrabatt (brandstofkorting)"),
    ("A2", "A", "geht (3e persoon enkelvoud)"),
    ("B1", "B", "erzählt (3e persoon enkelvoud)"),
]
cnums = [reg_ex(lv, "gatentekst", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　LÜCKENTEXT　Gatentekst", 24)
bf.para(f"Lena freut sich auf die Fußballwoche. Am Dienstag sieht sie Bayern bei Atlético Madrid, am Mittwoch Dortmund gegen Real Betis. Am Donnerstag ({cnums[0]})___ Hoffenheim bei Crystal Palace, und am Freitag ({cnums[1]})___ die Bundesliga mit Hamburg gegen Gladbach. Am Samstag ({cnums[2]})___ Lena einen Kürbis und ({cnums[3]})___ ihn zu Hause. Am Sonntag ({cnums[4]})___ sie lange, denn die Woche war anstrengend. In der Schule erzählt sie: „Die Fußballwoche war toll! Und der ({cnums[5]})___ läuft noch bis Dezember.“ Am Montag ({cnums[6]})___ Lena wieder in die Schule und ({cnums[7]})___ von den Spielen.", 20.5)
bf.bridge("Opties:")
for n, opts in zip(cnums, [
    "A. spielen · B. spielt · C. spieltet",
    "A. beginnt · B. beginnen · C. begann",
    "A. kaufen · B. kauft · C. kaufte",
    "A. malt · B. kocht · C. schnitzt",
    "A. schlafen · B. schläft · C. schlief",
    "A. Spieltag · B. Tankrabatt · C. Advent",
    "A. geht · B. gehen · C. ging",
    "A. erzählen · B. erzählt · C. erzählte",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)

# ---- B. general MC ----
bf.head("B　WISSENSFRAGEN　Kennis", 24)
bf.ex("B1", "meerkeuze", "A", "korting tot 31 december 2026",
      "Der Tankrabatt läuft bis... A. 31. Dezember 2026 · B. 1. November · C. 31. Oktober", size=19.5, gap=8)
bf.ex("A2", "meerkeuze", "B", "Bayern uit bij Atlético op dinsdag",
      "Bayern spielt am Dienstag bei... A. Galatasaray · B. Atlético Madrid · C. Real Betis", size=19.5, gap=8)
bf.ex("A2", "meerkeuze", "A", "Hoffenheim uit bij Crystal Palace in de Europa League",
      "Hoffenheim spielt in der Europa League bei... A. Crystal Palace · B. Marseille · C. Manchester City", size=19.5, gap=8)
bf.ex("B1", "meerkeuze", "B", "vakantie in Baden-Württemberg voorbij",
      "In welchem Bundesland sind die Ferien schon vorbei? A. Bayern · B. Baden-Württemberg · C. Berlin", size=19.5, gap=8)
bf.ex("B1", "meerkeuze", "B", "ZEW-verwachtingen op 28,1",
      "Der ZEW-Index: Die Erwartungen fielen im Oktober auf... A. 34,7 · B. 28,1 · C. 47,1", size=19.5, gap=8)
bf.ex("A2", "meerkeuze", "A", "Hamburg–Gladbach openen op vrijdag",
      "Der 9. Spieltag beginnt am Freitag mit... A. Hamburg–Gladbach · B. Stuttgart–Bremen · C. Köln–Leverkusen", size=19.5, gap=8)
bf.ex("B1", "meerkeuze", "B", "programma van 26 oktober over zorg thuis",
      "„Hart aber fair“ diskutierte in der Sendung am 26. Oktober... A. die Stromsteuer · B. die Pflege zu Hause · C. den Tankrabatt", size=19.5, gap=8)
bf.ex("A2", "meerkeuze", "B", "Allerheiligen is op 1 november",
      "Allerheiligen ist am... A. 31. Oktober · B. 1. November · C. 2. November", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C　LESEVERSTEHEN　Lezen", 24)
bf.para("Familie Berger aus Stuttgart hat am Montag wieder Schule: Die Kinder gehen um halb acht aus dem Haus. Am Dienstagabend schaut die Familie Bayern bei Atlético im Fernsehen. Am Samstag fährt sie zum Markt und kauft einen Kürbis. Am Sonntag schaut sie Hoffenheim gegen Schalke um 19.30 Uhr. „Eine Woche mit Fußball und Kürbis“, sagt Frau Berger.", 20.5)
bf.ex("B1", "meerkeuze", "A", "halb acht = 7.30 uur",
      "Wann gehen die Kinder aus dem Haus? A. um halb acht · B. um acht · C. um halb neun", size=19.5, gap=8)
bf.ex("A2", "meerkeuze", "B", "dinsdag Bayern uit bij Atlético kijken",
      "Was schaut die Familie am Dienstag? A. Dortmund–Betis · B. Bayern bei Atlético · C. Hoffenheim–Schalke", size=19.5, gap=8)
bf.ex("A2", "meerkeuze", "A", "zaterdag een pompoen kopen",
      "Was kauft die Familie am Samstag? A. einen Kürbis · B. ein Buch · C. ein Kostüm", size=19.5, gap=8)
bf.ex("B1", "meerkeuze", "B", "Hoffenheim–Schalke op zondag om 19.30 uur",
      "Wann spielt Hoffenheim gegen Schalke? A. Samstag 18.30 Uhr · B. Sonntag 19.30 Uhr · C. Freitag 20.30 Uhr", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D　SÄTZE BAUEN　Zinnen bouwen", 24)
bf.ex("A2", "zinnen bouwen", "Die Bundesliga beginnt am Freitag.", "tijdsbepaling vooraan, werkwoord op plaats 2",
      "die Bundesliga / beginnt / am Freitag → ___", instr="Vorm de zin", size=19.5, gap=8)
bf.ex("A2", "zinnen bouwen", "Wir schauen Bayern bei Atlético.", "onderwerp–werkwoord–voorwerp",
      "wir / schauen / Bayern / bei Atlético → ___", instr="Vorm de zin", size=19.5, gap=8)
bf.ex("B1", "zinnen bouwen", "Die Kinder gehen am Montag wieder in die Schule.", "tijdsbepaling vooraan, werkwoord op plaats 2",
      "die Kinder / gehen / am Montag / wieder in die Schule → ___", instr="Vorm de zin", size=19.5, gap=8)
bf.ex("B1", "zinnen bouwen", "In Bayern dauern die Ferien noch an.", "plaats vooraan, werkwoord op plaats 2",
      "in Bayern / dauern / die Ferien / noch an → ___", instr="Vorm de zin", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E　ÜBERSETZEN　Vertalen", 24)
bf.ex("A2", "vertalen", "De brandstofkorting loopt tot december.", "laufen = duren",
      "Der Tankrabatt läuft bis Dezember.", instr="Vertaal naar het Nederlands", size=19.5, gap=8)
bf.ex("A2", "vertalen", "Ik kijk op dinsdag voetbal.", "schauen = kijken",
      "Ich schaue am Dienstag Fußball.", instr="Vertaal naar het Nederlands", size=19.5, gap=8)
bf.ex("B1", "vertalen", "De school is weer begonnen.", "wieder begonnen = weer begonnen",
      "Die Schule hat wieder begonnen.", instr="Vertaal naar het Nederlands", size=19.5, gap=8)
bf.ex("B1", "vertalen", "Am Sonntag schlafe ich eine Stunde länger.", "een uur langer slapen = eine Stunde länger schlafen",
      "Ik slaap op zondag een uur langer.", instr="Vertaal naar het Duits", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F　WÖRTER PAAREN　Koppelen", 24)
bf.match_set("B1", "koppelen",
             ["der Tankrabatt", "die Pflege", "der Advent", "der Pausenhof"],
             ["die Zeit vor Weihnachten, in der man plant und bastelt",
              "die Ermäßigung auf die Energiesteuer beim Tanken",
              "der Hof der Schule, auf dem die Kinder in der Pause spielen",
              "die Hilfe für Menschen, die nicht mehr allein leben können"],
             ["b", "d", "a", "c"],
             ["Tankrabatt = brandstofkorting b", "Pflege = zorg d", "Advent = advent a", "Pausenhof = speelplaats c"],
             instr="Combineer")

# ---- G. dialogue ----
ddefs = [
    ("A2", "B", "schaust (2e persoon enkelvoud)"),
    ("A2", "A", "siehst (2e persoon enkelvoud)"),
    ("A2", "A", "kochen (1e persoon meervoud)"),
    ("B1", "B", "machst (2e persoon enkelvoud)"),
    ("B1", "A", "gehe (1e persoon enkelvoud)"),
]
dnums = [reg_ex(lv, "dialoog aanvullen", k, nt) for lv, k, nt in ddefs]
bf.head("G　DIALOG　Dialoog", 24)
bf.para(f"— Hallo, Lena! Schaust du am Dienstag Fußball? — Ja, Bayern bei Atlético! Um 21.00 Uhr. — Und am Mittwoch? — Dortmund gegen Betis. Ich bin für Dortmund. — ({dnums[0]})___ du am Sonntag auch Fußball? — Ja, Hoffenheim gegen Schalke um 19.30 Uhr. — Mit wem ({dnums[1]})___ du das Spiel? — Mit meiner Familie, zu Hause. Wir ({dnums[2]})___ Kürbissuppe. — Lecker! Und was ({dnums[3]})___ du am Montag? — Ich ({dnums[4]})___ wieder in die Schule. Die Ferien sind vorbei!", 20.5)
bf.bridge("Opties:")
for n, opts in zip(dnums, [
    "A. schaut · B. schaust · C. schauen",
    "A. siehst · B. sehen · C. sieht",
    "A. kochen · B. koche · C. kocht",
    "A. machen · B. machst · C. macht",
    "A. gehe · B. geht · C. gehen",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1520
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "schrijven", "Open opdracht — zie de punten in het schrijfblok; de voorbeeldtekst staat in het schrijfblok op deze pagina", "Beoordeling op basis van de punten")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　SCHREIBEN　Schrijven", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Fußballwoche». Erzählen Sie: Welche Spiele schauen Sie? Mit wem? Was essen Sie beim Spiel? Schreiben Sie auch einen Satz über den Tankrabatt oder die Pflege! Die besten Texte drucken wir in VOL.3 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "Schrijf in het Duits 80–100 woorden: «Mijn voetbalweek». Vertel welke wedstrijden je kijkt, met wie, en wat je eet tijdens de wedstrijd — en voeg één zin toe over de brandstofkorting of de zorg. De beste teksten verschijnen in VOL.3 (pagina 7, «Lezersbrieven»).", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX)
p.text(mx2 + 22, wy + 38, "MUSTER　Voorbeeldtekst (84 woorden)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche schaue ich viel Fußball. Am Dienstag sehe ich Bayern bei Atlético, am Mittwoch Dortmund gegen Betis. Am Donnerstag spielt Hoffenheim bei Crystal Palace. Am Freitag sehe ich Hamburg gegen Gladbach mit meinem Bruder. Wir essen Brezeln und trinken Apfelschorle. Am Sonntag schauen wir Hoffenheim gegen Schalke. Der Tankrabatt freut mich sehr: Ich tanke 50 Liter und spare rund 8,35 Euro. Am Samstag kaufe ich einen Kürbis und schnitze ihn mit Lena. Am Montag gehe ich zur Arbeit. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 320
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANTWORTEN　Alle antwoorden met toelichting (pagina 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Pagina {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f"({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
