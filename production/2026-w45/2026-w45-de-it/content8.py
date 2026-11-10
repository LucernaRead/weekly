# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN　Esercizi e risposte", "Die Lucerna", "SCHLUSSTEST　Prova finale　Tutte le risposte in fondo a questa pagina")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "spielt (terza persona singolare)"),
    ("A2", "A", "beginnt (terza persona singolare)"),
    ("A2", "B", "kauft (terza persona singolare)"),
    ("A2", "C", "schnitzt = intagliare la zucca"),
    ("A2", "B", "schläft (terza persona singolare)"),
    ("B1", "B", "Tankrabatt = sconto sul carburante"),
    ("A2", "A", "geht (terza persona singolare)"),
    ("B1", "B", "erzählt (terza persona singolare)"),
]
cnums = [reg_ex(lv, "testo a buchi", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　LÜCKENTEXT　Testo a buchi", 24)
bf.para(f"Lena freut sich auf die Fußballwoche. Am Dienstag sieht sie Bayern bei Atlético Madrid, am Mittwoch Dortmund gegen Real Betis. Am Donnerstag ({cnums[0]})___ Hoffenheim bei Crystal Palace, und am Freitag ({cnums[1]})___ die Bundesliga mit Hamburg gegen Gladbach. Am Samstag ({cnums[2]})___ Lena einen Kürbis und ({cnums[3]})___ ihn zu Hause. Am Sonntag ({cnums[4]})___ sie lange, denn die Woche war anstrengend. In der Schule erzählt sie: „Die Fußballwoche war toll! Und der ({cnums[5]})___ läuft noch bis Dezember.“ Am Montag ({cnums[6]})___ Lena wieder in die Schule und ({cnums[7]})___ von den Spielen.", 20.5)
bf.bridge("Opzioni:")
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
bf.head("B　WISSENSFRAGEN　Quiz", 24)
bf.ex("B1", "scelta multipla", "A", "sconto fino al 31 dicembre 2026",
      "Der Tankrabatt läuft bis... A. 31. Dezember 2026 · B. 1. November · C. 31. Oktober", size=19.5, gap=8)
bf.ex("A2", "scelta multipla", "B", "il Bayern in trasferta dall'Atlético martedì",
      "Bayern spielt am Dienstag bei... A. Galatasaray · B. Atlético Madrid · C. Real Betis", size=19.5, gap=8)
bf.ex("A2", "scelta multipla", "A", "l'Hoffenheim in Europa League dal Crystal Palace",
      "Hoffenheim spielt in der Europa League bei... A. Crystal Palace · B. Marseille · C. Manchester City", size=19.5, gap=8)
bf.ex("B1", "scelta multipla", "B", "le vacanze nel Baden-Württemberg sono finite",
      "In welchem Bundesland sind die Ferien schon vorbei? A. Bayern · B. Baden-Württemberg · C. Berlin", size=19.5, gap=8)
bf.ex("B1", "scelta multipla", "B", "le attese ZEW a 28,1",
      "Der ZEW-Index: Die Erwartungen fielen im Oktober auf... A. 34,7 · B. 28,1 · C. 47,1", size=19.5, gap=8)
bf.ex("A2", "scelta multipla", "A", "Amburgo–Gladbach aprono venerdì",
      "Der 9. Spieltag beginnt am Freitag mit... A. Hamburg–Gladbach · B. Stuttgart–Bremen · C. Köln–Leverkusen", size=19.5, gap=8)
bf.ex("B1", "scelta multipla", "B", "il programma del 26 ottobre ha discusso l'assistenza a casa",
      "„Hart aber fair“ diskutierte in der Sendung am 26. Oktober... A. die Stromsteuer · B. die Pflege zu Hause · C. den Tankrabatt", size=19.5, gap=8)
bf.ex("A2", "scelta multipla", "B", "Ognissanti è il 1° novembre",
      "Allerheiligen ist am... A. 31. Oktober · B. 1. November · C. 2. November", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C　LESEVERSTEHEN　Lettura", 24)
bf.para("Familie Berger aus Stuttgart hat am Montag wieder Schule: Die Kinder gehen um halb acht aus dem Haus. Am Dienstagabend schaut die Familie Bayern bei Atlético im Fernsehen. Am Samstag fährt sie zum Markt und kauft einen Kürbis. Am Sonntag schaut sie Hoffenheim gegen Schalke um 19.30 Uhr. „Eine Woche mit Fußball und Kürbis“, sagt Frau Berger.", 20.5)
bf.ex("B1", "scelta multipla", "A", "halb acht = 7:30",
      "Wann gehen die Kinder aus dem Haus? A. um halb acht · B. um acht · C. um halb neun", size=19.5, gap=8)
bf.ex("A2", "scelta multipla", "B", "guardare il Bayern in trasferta dall'Atlético martedì",
      "Was schaut die Familie am Dienstag? A. Dortmund–Betis · B. Bayern bei Atlético · C. Hoffenheim–Schalke", size=19.5, gap=8)
bf.ex("A2", "scelta multipla", "A", "comprare una zucca sabato",
      "Was kauft die Familie am Samstag? A. einen Kürbis · B. ein Buch · C. ein Kostüm", size=19.5, gap=8)
bf.ex("B1", "scelta multipla", "B", "Hoffenheim–Schalke domenica alle 19:30",
      "Wann spielt Hoffenheim gegen Schalke? A. Samstag 18.30 Uhr · B. Sonntag 19.30 Uhr · C. Freitag 20.30 Uhr", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D　SÄTZE BAUEN　Costruisci frasi", 24)
bf.ex("A2", "costruire frasi", "Die Bundesliga beginnt am Freitag.", "indicazione di tempo all'inizio, verbo in seconda posizione",
      "die Bundesliga / beginnt / am Freitag → ___", instr="Costruisci la frase", size=19.5, gap=8)
bf.ex("A2", "costruire frasi", "Wir schauen Bayern bei Atlético.", "ordine soggetto–verbo–oggetto",
      "wir / schauen / Bayern / bei Atlético → ___", instr="Costruisci la frase", size=19.5, gap=8)
bf.ex("B1", "costruire frasi", "Die Kinder gehen am Montag wieder in die Schule.", "indicazione di tempo all'inizio, verbo in seconda posizione",
      "die Kinder / gehen / am Montag / wieder in die Schule → ___", instr="Costruisci la frase", size=19.5, gap=8)
bf.ex("B1", "costruire frasi", "In Bayern dauern die Ferien noch an.", "luogo all'inizio, verbo in seconda posizione",
      "in Bayern / dauern / die Ferien / noch an → ___", instr="Costruisci la frase", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E　ÜBERSETZEN　Traduzione", 24)
bf.ex("A2", "traduzione", "Lo sconto sul carburante dura fino a dicembre.", "laufen = durare",
      "Der Tankrabatt läuft bis Dezember.", instr="Traduci in italiano", size=19.5, gap=8)
bf.ex("A2", "traduzione", "Guardo il calcio di martedì.", "schauen = guardare",
      "Ich schaue am Dienstag Fußball.", instr="Traduci in italiano", size=19.5, gap=8)
bf.ex("B1", "traduzione", "La scuola è ricominciata.", "wieder begonnen = ricominciato",
      "Die Schule hat wieder begonnen.", instr="Traduci in italiano", size=19.5, gap=8)
bf.ex("B1", "traduzione", "Am Sonntag schlafe ich eine Stunde länger.", "dormire un'ora in più = eine Stunde länger schlafen",
      "Domenica dormo un'ora in più.", instr="Traduci in tedesco", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F　WÖRTER PAAREN　Le coppie", 24)
bf.match_set("B1", "abbinamento",
             ["der Tankrabatt", "die Pflege", "der Advent", "der Pausenhof"],
             ["die Zeit vor Weihnachten, in der man plant und bastelt",
              "die Ermäßigung auf die Energiesteuer beim Tanken",
              "der Hof der Schule, auf dem die Kinder in der Pause spielen",
              "die Hilfe für Menschen, die nicht mehr allein leben können"],
             ["b", "d", "a", "c"],
             ["Tankrabatt = sconto sul carburante b", "Pflege = assistenza d", "Advent = Avvento a", "Pausenhof = cortile della scuola c"],
             instr="Abbina le coppie")

# ---- G. dialogue ----
ddefs = [
    ("A2", "B", "schaust (seconda persona singolare)"),
    ("A2", "A", "siehst (seconda persona singolare)"),
    ("A2", "A", "kochen (prima persona plurale)"),
    ("B1", "B", "machst (seconda persona singolare)"),
    ("B1", "A", "gehe (prima persona singolare)"),
]
dnums = [reg_ex(lv, "completare il dialogo", k, nt) for lv, k, nt in ddefs]
bf.head("G　DIALOG　Completa il dialogo", 24)
bf.para(f"— Hallo, Lena! Schaust du am Dienstag Fußball? — Ja, Bayern bei Atlético! Um 21.00 Uhr. — Und am Mittwoch? — Dortmund gegen Betis. Ich bin für Dortmund. — ({dnums[0]})___ du am Sonntag auch Fußball? — Ja, Hoffenheim gegen Schalke um 19.30 Uhr. — Mit wem ({dnums[1]})___ du das Spiel? — Mit meiner Familie, zu Hause. Wir ({dnums[2]})___ Kürbissuppe. — Lecker! Und was ({dnums[3]})___ du am Montag? — Ich ({dnums[4]})___ wieder in die Schule. Die Ferien sind vorbei!", 20.5)
bf.bridge("Opzioni:")
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
reg_ex("B1", "scrittura", "Domanda aperta — segui i punti del riquadro di scrittura; il testo modello è nel riquadro di questa pagina", "Si valuta secondo i punti indicati")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　SCHREIBEN　Scrittura", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Fußballwoche». Erzählen Sie: Welche Spiele schauen Sie? Mit wem? Was essen Sie beim Spiel? Schreiben Sie auch einen Satz über den Tankrabatt oder die Pflege! Die besten Texte drucken wir in VOL.3 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "Scrivi in tedesco 80–100 parole: «La mia settimana di calcio». Racconta quali partite guardi, con chi, e cosa mangi durante la partita — e aggiungi una frase sullo sconto sul carburante o sull'assistenza.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX)
p.text(mx2 + 22, wy + 38, "MUSTER　Testo modello (84 parole)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche schaue ich viel Fußball. Am Dienstag sehe ich Bayern bei Atlético, am Mittwoch Dortmund gegen Betis. Am Donnerstag spielt Hoffenheim bei Crystal Palace. Am Freitag sehe ich Hamburg gegen Gladbach mit meinem Bruder. Wir essen Brezeln und trinken Apfelschorle. Am Sonntag schauen wir Hoffenheim gegen Schalke. Der Tankrabatt freut mich sehr: Ich tanke 50 Liter und spare rund 8,35 Euro. Am Samstag kaufe ich einen Kürbis und schnitze ihn mit Lena. Am Montag gehe ich zur Arbeit. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 320
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANTWORTEN　TUTTE LE RISPOSTE CON NOTE (PAGINE 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— PAGINA {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
