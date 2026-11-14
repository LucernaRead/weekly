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
    ("A2", "B", "schnitzen = intagliare (la zucca)"),
    ("A2", "A", "geht in die Bibliothek = va in biblioteca"),
    ("A2", "A", "Uhr zurückgestellt = l'orologio riportato indietro"),
    ("A2", "C", "Winterzeit = inizia l'ora solare"),
    ("A2", "B", "eine Stunde länger = un'ora in più"),
    ("A2", "A", "der erste Frost = la prima brina"),
    ("B1", "B", "gefällt mir gut = mi piace molto"),
    ("A2", "C", "ich gehe (prima persona)"),
]
cnums = [reg_ex(lv, "testo a buchi", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　LÜCKENTEXT　Testo a buchi", 24)
bf.para(f"Jonas freut sich auf das Wochenende. Am Samstag kauft er einen Kürbis und ({cnums[0]})___ ihn zu Hause. Am Nachmittag ({cnums[1]})___ er in die Bibliothek — sie hat am Samstag ein besonderes Programm. Am Abend spielt Dortmund, und Jonas sieht das Spiel mit Freunden. In der Nacht wird die Uhr ({cnums[2]})___: Die ({cnums[3]})___ beginnt. Am Sonntag schläft Jonas eine Stunde ({cnums[4]})___. Draußen ist es kalt, der erste ({cnums[5]})___ ist da. „Ein Sonntag mit 25 Stunden“, sagt Jonas, „({cnums[6]})___ mir gut! Und am Montag ({cnums[7]})___ ich wieder in die Schule.“", 20.5)
bf.expl("Opzioni:")
for n, opts in zip(cnums, [
    "A. kocht · B. schnitzt · C. malt",
    "A. geht · B. schläft · C. kocht",
    "A. zurückgestellt · B. vorgestellt · C. vergessen",
    "A. Sommerzeit · B. Ferienzeit · C. Winterzeit",
    "A. früh · B. länger · C. laut",
    "A. Frost · B. Sommer · C. Frühling",
    "A. geht · B. gefällt · C. macht",
    "A. gehen · B. gehst · C. gehe",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)

# ---- B. general MC ----
bf.head("B　WISSENSFRAGEN　Quiz", 24)
bf.ex("B1", "scelta multipla", "A", "la Giornata delle biblioteche ricorda Preusker",
      "Der Tag der Bibliotheken erinnert an... A. Karl Preusker · B. Martin Luther · C. Lucas Cranach", size=19.5, gap=8)
bf.ex("A2", "scelta multipla", "B", "domenica alle 3 si riporta indietro",
      "Die Uhr wird umgestellt am... A. Freitag um 20.30 Uhr · B. Sonntag um 3.00 Uhr · C. Samstag um Mitternacht", size=19.5, gap=8)
bf.ex("A2", "scelta multipla", "A", "O bis O = da ottobre a Pasqua",
      "„Von O bis O“ heißt: Winterreifen von... A. Oktober bis Ostern · B. Oktober bis Oktober · C. Ostern bis Oktober", size=19.5, gap=8)
bf.ex("B1", "scelta multipla", "B", "il Klassiker si gioca a Dortmund",
      "Am 31. Oktober spielen die Bayern... A. zu Hause · B. in Dortmund · C. in Berlin", size=19.5, gap=8)
bf.ex("B1", "scelta multipla", "B", "la protezione si forma in 10–14 giorni",
      "Die Grippeimpfung schützt nach... A. 2 Tagen · B. 10 bis 14 Tagen · C. 3 Monaten", size=19.5, gap=8)
bf.ex("B1", "scelta multipla", "B", "in farmacia si vaccina dai 18 anni",
      "In Apotheken impft man Menschen... A. ab 6 Jahren · B. ab 18 Jahren · C. nur ab 60", size=19.5, gap=8)
bf.ex("A2", "scelta multipla", "B", "la partita clou del sabato: Dortmund–Francoforte",
      "Das Topspiel am Samstag ist... A. Freiburg–Bayern · B. Dortmund–Frankfurt · C. Stuttgart–Gladbach", size=19.5, gap=8)
bf.ex("A2", "scelta multipla", "B", "l'ora dalle 2 alle 3 appare due volte",
      "Die Stunde 2.00–3.00 Uhr gibt es in der Nacht... A. einmal · B. zweimal · C. gar nicht", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C　LESEVERSTEHEN　Lettura", 24)
bf.para("Frau Berger arbeitet in einer Berliner Bibliothek. Am Samstag, dem 24. Oktober, beginnt sie um halb zehn mit der Arbeit. Heute ist der Tag der Bibliotheken: Um elf Uhr spielt sie mit den Kindern Bibliotheks-Bingo. Am Nachmittag hilft sie bei den Book-Blind-Dates. Um 18 Uhr schließt die Bibliothek. Frau Berger fährt nach Hause und stellt am Abend alle Uhren um — morgen darf sie eine Stunde länger schlafen.", 20.5)
bf.ex("B1", "scelta multipla", "A", "halb zehn = 9:30",
      "Wann beginnt Frau Berger mit der Arbeit? A. um 9.30 Uhr · B. um 10.30 Uhr · C. um halb elf", size=19.5, gap=8)
bf.ex("A2", "scelta multipla", "B", "alle undici gioca a Bingo con i bambini",
      "Was spielt sie um elf Uhr mit den Kindern? A. Fußball · B. Bibliotheks-Bingo · C. Karten", size=19.5, gap=8)
bf.ex("A2", "scelta multipla", "B", "la sera, a casa, regola gli orologi",
      "Was macht sie am Abend zu Hause? A. Sie schnitzt einen Kürbis. · B. Sie stellt die Uhren um. · C. Sie liest ein Buch.", size=19.5, gap=8)
bf.ex("B1", "scelta multipla", "B", "siccome l'orologio va indietro, può dormire di più",
      "Warum darf sie am Sonntag länger schlafen? A. Die Bibliothek ist zu. · B. Die Uhr wird zurückgestellt. · C. Sie hat Urlaub.", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D　SÄTZE BAUEN　Costruisci frasi", 22)  # D5 fix run2
bf.ex("A2", "costruire frasi", "Die Uhr wird am Sonntag zurückgestellt.", "wird in seconda posizione, il participio alla fine",
      "die Uhr / wird / am Sonntag / zurückgestellt → ___", instr="Costruisci la frase", size=19.5, gap=8)
bf.ex("A2", "costruire frasi", "Wir schlafen eine Stunde länger.", "ordine soggetto–verbo–oggetto",
      "wir / schlafen / eine Stunde / länger → ___", instr="Costruisci la frase", size=19.5, gap=8)
bf.ex("B1", "costruire frasi", "Die Kinder freuen sich, weil Ferien sind.", "con weil il verbo va alla fine",
      "die Kinder / freuen sich / weil / Ferien / sind → ___", instr="Costruisci la frase", size=19.5, gap=8)
bf.ex("B1", "costruire frasi", "Am Samstag ist der Tag der Bibliotheken.", "inizia l'indicazione di tempo; il verbo in seconda posizione",
      "am Samstag / ist / der Tag / der Bibliotheken → ___", instr="Costruisci la frase", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E　ÜBERSETZEN　Traduzione", 24)
bf.ex("A2", "traduzione", "La notte ha 25 ore.", "Stunden = ore",
      "Die Nacht hat 25 Stunden.", instr="Traduci in italiano", size=19.5, gap=8)
bf.ex("A2", "traduzione", "Sabato sera sposto l'orologio.", "umstellen = spostare (un orologio)",
      "Ich stelle die Uhr am Samstagabend um.", instr="Traduci in italiano", size=19.5, gap=8)
bf.ex("B1", "traduzione", "Am Sonntag schlafe ich eine Stunde länger.", "dormire un'ora in più = eine Stunde länger schlafen",
      "Domenica dormo un'ora in più.", instr="Traduci in tedesco", size=19.5, gap=8)
bf.ex("B1", "traduzione", "In der Bibliothek kann man Bücher leihen.", "kann man ... leihen = si possono prendere in prestito",
      "In biblioteca si possono prendere in prestito i libri.", instr="Traduci in tedesco", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F　WÖRTER PAAREN　Le coppie", 24)
bf.match_set("B1", "abbinamento",
             ["die Umstellung", "die Mitgliedstaaten", "die Mehrheit", "der Feiertag"],
             ["ein Tag, an dem man nicht arbeiten muss",
              "der Wechsel zwischen Sommer- und Winterzeit",
              "die Länder, die zu einer Union gehören",
              "mehr als die Hälfte, zum Beispiel 84 Prozent"],
             ["b", "c", "d", "a"],
             ["Umstellung = il cambio tra ora legale e ora solare, b", "Mitgliedstaaten = gli Stati membri, c", "Mehrheit = la maggioranza, d", "Feiertag = il giorno festivo, a"],
             instr="Abbina le coppie")

# ---- G. dialogue ----
ddefs = [
    ("A2", "A", "Buch = il libro (per suo figlio)"),
    ("B1", "B", "im ersten Stock = al primo piano (sopra il piano terra)"),
    ("A2", "C", "Bingo = il bingo della biblioteca"),
    ("B1", "A", "Bibliotheksausweis = la tessera della biblioteca"),
    ("B1", "B", "behalten = tenere (il libro)"),
]
dnums = [reg_ex(lv, "completare il dialogo", k, nt) for lv, k, nt in ddefs]
bf.head("G　DIALOG　Completa il dialogo", 24)
bf.para(f"— Guten Tag! Ich suche ein Buch für meinen Sohn. — Gern. Wie alt ist er? — Er ist neun, und er mag Tiere. — Dann ist dieses ({dnums[0]})___ perfekt: „Tiere im Herbst“. Mehr Tierbücher finden Sie im ersten ({dnums[1]})___. — Danke! Gibt es heute auch das ({dnums[2]})___? — Ja, um elf Uhr im Kinderzimmer. Bitte zeigen Sie mir noch Ihren ({dnums[3]})___. — Hier ist er. Wie lange kann ich das Buch ({dnums[4]})___? — Drei Wochen. Viel Spaß beim Lesen!", 20.5)
bf.expl("Opzioni:")
for n, opts in zip(dnums, [
    "A. Buch · B. Bett · C. Brot",
    "A. Keller · B. Stock · C. Garten",
    "A. Fußball · B. Kino · C. Bingo",
    "A. Bibliotheksausweis · B. Bibliotheksausflug · C. Bibliotheksautor",
    "A. essen · B. behalten · C. singen",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1520
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "scrittura", "Domanda aperta — segui i punti del riquadro di scrittura; il testo modello è nel riquadro di questa pagina", "Si valuta secondo i punti indicati")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　SCHREIBEN　Scrittura", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Mein Sonntag, der 25. Oktober». Erzählen Sie: Wie lange schlafen Sie? Was machen Sie am Morgen, am Nachmittag und am Abend? Schreiben Sie auch einen Satz über die Uhr! Die besten Texte drucken wir in VOL.2 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "Scrivi in tedesco 80–100 parole: «La mia domenica, il 25 ottobre». Racconta quanto dormi, cosa fai la mattina, il pomeriggio e la sera, e scrivi anche una frase sull'orologio.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, "MUSTER　Testo modello (87 parole)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Am Sonntag, dem 25. Oktober, schlafe ich eine Stunde länger. Dann frühstücke ich langsam mit meiner Familie. Um elf Uhr gehe ich in den Park, denn die Sonne scheint. Am Nachmittag lese ich mein neues Buch aus der Bibliothek. Am Abend koche ich eine Suppe mit Kürbis. Danach rufe ich meine Freundin an. Wir sprechen über das Fußballspiel am Samstag. Dortmund hat gewonnen, und wir freuen uns. Der Sonntag mit 25 Stunden ist mein Lieblingstag. Ich gehe früh ins Bett, denn am Montag beginnt die Arbeit wieder.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 296
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
