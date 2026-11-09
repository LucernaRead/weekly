# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN　Oefeningen & antwoorden", "Die Lucerna", "SCHLUSSTEST　Eindtoets　Alle Antworten unten auf dieser Seite — alle antwoorden onderaan deze pagina")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "A", "beginnt (3e persoon enkelvoud)"),
    ("A2", "B", "bastelt (3e persoon enkelvoud)"),
    ("A2", "A", "geht (3e persoon enkelvoud)"),
    ("A2", "B", "singt (3e persoon enkelvoud)"),
    ("A2", "A", "schaut (3e persoon enkelvoud)"),
    ("B1", "B", "sieht (3e persoon enkelvoud)"),
    ("A2", "B", "erzählt (3e persoon enkelvoud)"),
    ("B1", "A", "beginnt (3e persoon enkelvoud)"),
]
cnums = [reg_ex(lv, "gatentekst", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　LÜCKENTEXT　Gatentekst", 24)
bf.para(f"Lena freut sich auf die Novemberwoche. Am Montag ({cnums[0]})___ die Schule wieder, und Lena ({cnums[1]})___ eine Laterne aus Papier. Am Mittwoch ({cnums[2]})___ sie mit ihrer Klasse beim Laternenumzug mit und ({cnums[3]})___ Martinslieder. Am Freitagabend ({cnums[4]})___ sie Deutschland in Belgrad. Am Sonntag ({cnums[5]})___ sie die NFL in München im Fernsehen. In der Schule ({cnums[6]})___ Lena: „Die Woche war toll! Der Karneval ({cnums[7]})___ um 11.11 Uhr.“", 20.5)
bf.bridge("Opties:")
for n, opts in zip(cnums, [
    "A. beginnt · B. beginnen · C. begann",
    "A. basteln · B. bastelt · C. bastelte",
    "A. geht · B. gehen · C. ging",
    "A. singen · B. singt · C. sang",
    "A. schaut · B. schauen · C. schaute",
    "A. sehen · B. sieht · C. sah",
    "A. erzählen · B. erzählt · C. erzählte",
    "A. beginnt · B. beginnen · C. begann",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)

# ---- B. general MC ----
bf.head("B　WISSENSFRAGEN　Quiz", 24)
bf.ex("B1", "meerkeuze", "A", "carnaval begint om 11.11 uur",
      "Die Karnevalssession beginnt um... A. 11.11 Uhr · B. 15.30 Uhr · C. 20.45 Uhr", size=19.5, gap=8)
bf.ex("A2", "meerkeuze", "B", "uit in Servië op vrijdag",
      "Deutschland spielt am Freitag in... A. Berlin · B. Belgrad · C. München", size=19.5, gap=8)
bf.ex("A2", "meerkeuze", "C", "NFL op zondag om 15.30 uur",
      "Das NFL-Spiel in München beginnt um... A. 11.11 Uhr · B. 20.45 Uhr · C. 15.30 Uhr", size=19.5, gap=8)
bf.ex("B1", "meerkeuze", "A", "de herdenkingsdag is 15 november",
      "Der Volkstrauertag ist am... A. 15. November · B. 11. November · C. 22. November", size=19.5, gap=8)
bf.ex("B1", "meerkeuze", "B", "de stroomtaks voor huishoudens is 2,05 cent",
      "Die Stromsteuer für Haushalte beträgt... A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent", size=19.5, gap=8)
bf.ex("A2", "meerkeuze", "B", "de bondscoach noemt de selectie op 5 november",
      "Klopp nennt seinen Kader am... A. 13. November · B. 5. November · C. 9. November", size=19.5, gap=8)
bf.ex("B1", "meerkeuze", "A", "ZDF live vanaf 13.30 uur",
      "Die Gedenkstunde überträgt ab 13.30 Uhr... A. das ZDF · B. RTL · C. die ARD", size=19.5, gap=8)
bf.ex("A2", "meerkeuze", "C", "Totensonntag is 22 november",
      "Der Totensonntag ist am... A. 15. November · B. 18. November · C. 22. November", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C　LESEVERSTEHEN　Lezen", 24)
bf.para("Familie Berger aus Stuttgart hat am Montag wieder Schule: Die Kinder gehen um halb acht aus dem Haus. Am Mittwoch bastelt die Familie eine Laterne aus Papier. Am Freitag schaut sie Deutschland in Belgrad im Fernsehen. Am Sonntag schaut sie das NFL-Spiel um 15.30 Uhr. „Eine Woche mit Laternen und Football“, sagt Frau Berger.", 20.5)
bf.ex("B1", "meerkeuze", "A", "halb acht = 7:30",
      "Wann gehen die Kinder aus dem Haus? A. um halb acht · B. um acht · C. um halb neun", size=19.5, gap=8)
bf.ex("A2", "meerkeuze", "B", "een lantaarn maken op woensdag",
      "Was bastelt die Familie am Mittwoch? A. ein Kostüm · B. eine Laterne · C. einen Kürbis", size=19.5, gap=8)
bf.ex("A2", "meerkeuze", "A", "Duitsland kijken op vrijdag",
      "Was schaut die Familie am Freitag? A. Deutschland in Belgrad · B. die NFL · C. den Karneval", size=19.5, gap=8)
bf.ex("B1", "meerkeuze", "B", "NFL op zondag om 15.30 uur",
      "Wann schaut die Familie das NFL-Spiel? A. Samstag 18.30 Uhr · B. Sonntag 15.30 Uhr · C. Freitag 20.45 Uhr", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D　SÄTZE BAUEN　Zinnen", 24)
bf.ex("A2", "zinnen bouwen", "Die Karnevalssession beginnt am Mittwoch.", "tijdsbepaling, werkwoord tweede",
      "die Karnevalssession / beginnt / am Mittwoch → ___", instr="Vorm de zin", size=19.5, gap=8)
bf.ex("A2", "zinnen bouwen", "Wir basteln eine Laterne aus Papier.", "volgorde onderwerp–werkwoord–voorwerp",
      "wir / basteln / eine Laterne / aus Papier → ___", instr="Vorm de zin", size=19.5, gap=8)
bf.ex("B1", "zinnen bouwen", "Die Kinder gehen am Montag wieder in die Schule.", "tijdsbepaling eerst, werkwoord tweede",
      "die Kinder / gehen / am Montag / wieder in die Schule → ___", instr="Vorm de zin", size=19.5, gap=8)
bf.ex("B1", "zinnen bouwen", "Am Sonntag ist Volkstrauertag in ganz Deutschland.", "plaats en tijd eerst, werkwoord tweede",
      "am Sonntag / ist / Volkstrauertag / in ganz Deutschland → ___", instr="Vorm de zin", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E　ÜBERSETZEN　Vertalen", 24)
bf.ex("A2", "vertalen", "Het carnaval begint om 11.11 uur in Keulen.", "beginnen = beginnen",
      "Der Karneval beginnt um 11.11 Uhr in Köln. (vertaal naar het Nederlands)", instr="Vertaal naar het Nederlands", size=19.5, gap=8)
bf.ex("A2", "vertalen", "Ik maak een lantaarn op woensdag.", "basteln = knutselen",
      "Ich bastle am Mittwoch eine Laterne. (vertaal naar het Nederlands)", instr="Vertaal naar het Nederlands", size=19.5, gap=8)
bf.ex("B1", "vertalen", "School begon weer op 9 november.", "wieder begonnen = weer begonnen",
      "Die Schule hat am 9. November wieder begonnen. (vertaal naar het Nederlands)", instr="Vertaal naar het Nederlands", size=19.5, gap=8)
bf.ex("B1", "vertalen", "Am Sonntag schaue ich das NFL-Spiel.", "een wedstrijd kijken = das Spiel schauen",
      "Ik kijk de NFL-wedstrijd op zondag. (vertaal naar het Duits)", instr="Vertaal naar het Duits", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F　WÖRTER PAAREN　Koppelen", 24)
bf.match_set("B1", "koppelen",
             ["der Mantel", "die Laterne", "das Geisterspiel", "die Versöhnung"],
             ["das Licht aus Papier, das die Kinder am Abend tragen",
              "der warme Umhang, den Martin mit dem Bettler teilte",
              "die Aussöhnung nach einem Streit — Frieden zwischen Menschen",
              "ein Spiel ohne Zuschauer im Stadion"],
             ["b", "a", "d", "c"],
             ["Mantel=mantel b", "Laterne=lantaarn a", "Geisterspiel=spookwedstrijd d", "Versöhnung=verzoening c"],
             instr="Combineer")

# ---- G. dialogue ----
ddefs = [
    ("A2", "B", "singst (2e persoon enkelvoud)"),
    ("A2", "A", "macht (2e persoon meervoud)"),
    ("A2", "A", "essen (1e persoon meervoud)"),
    ("B1", "B", "machst (2e persoon enkelvoud)"),
    ("B1", "A", "schaue (1e persoon enkelvoud)"),
]
dnums = [reg_ex(lv, "dialoog aanvullen", k, nt) for lv, k, nt in ddefs]
bf.head("G　DIALOG　Dialoog aanvullen", 24)
bf.para(f"— Hallo, Lena! Bastelst du eine Laterne? — Ja, für St. Martin! Am Mittwoch gehen wir mit. — ({dnums[0]})___ du auch Martinslieder? — Ja, mit meiner Klasse. — Und was ({dnums[1]})___ ihr am Abend? — Wir singen und laufen mit den Laternen. Am Sonntag ({dnums[2]})___ wir Brezeln und schauen die NFL. — Lecker! Und was ({dnums[3]})___ du am Freitag? — Ich ({dnums[4]})___ Deutschland in Belgrad im Fernsehen!", 20.5)
bf.bridge("Opties:")
for n, opts in zip(dnums, [
    "A. singe · B. singst · C. singen",
    "A. macht · B. machen · C. machst",
    "A. essen · B. esse · C. esst",
    "A. machen · B. machst · C. macht",
    "A. schaue · B. schaust · C. schaut",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1520
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "schrijven", "Open taak — volg de punten in het schrijfkader; de modeltekst staat in het kader op deze pagina", "Beoordeeld op de genoemde punten")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　SCHREIBEN　Schrijven", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Novemberwoche». Erzählen Sie: Was basteln Sie? Welche Spiele schauen Sie? Mit wem? Schreiben Sie auch einen Satz über St. Martin oder den Volkstrauertag! Die besten Texte drucken wir in VOL.4 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "Schrijf in het Duits, 80–100 woorden: «Mijn week in november». Zeg wat je maakt, welke wedstrijden je kijkt en met wie — en voeg één zin toe over Sint Maarten of de herdenkingsdag.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX)
p.text(mx2 + 22, wy + 38, "MUSTER　Voorbeeldtekst (84 woorden)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche bastle ich eine Laterne. Am Mittwoch singe ich mit meiner Klasse Martinslieder und gehe beim Laternenumzug mit. Am Freitag schaue ich mit meiner Familie Deutschland in Belgrad im Fernsehen. Das Spiel ist ein Geisterspiel — ohne Zuschauer. Am Sonntag schaue ich die NFL in München im Fernsehen. Die Lions spielen gegen die Patriots. Der Karneval beginnt um 11.11 Uhr in Köln. Am Sonntag esse ich Brezeln und trinke Apfelschorle. Am Montag gehe ich wieder in die Schule. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 320
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANTWORTEN　Alle antwoorden met notities (pagina 1–8)", 26, "sans", True, OLIVE)
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
    kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
