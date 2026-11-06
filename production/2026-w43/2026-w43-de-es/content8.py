# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-de-es/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN · Ejercicios y respuestas", "Die Lucerna", "SCHLUSSTEST · Test final · Todas las respuestas, al final de esta página")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "schnitzen = tallar (la calabaza)"),
    ("A2", "A", "geht in die Bibliothek = va a la biblioteca"),
    ("A2", "A", "Uhr zurückgestellt = el reloj, atrasado"),
    ("A2", "C", "Winterzeit = empieza el horario de invierno"),
    ("A2", "B", "eine Stunde länger = una hora más de sueño"),
    ("A2", "A", "der erste Frost = la primera escarcha"),
    ("B1", "B", "gefällt mir gut = me gusta mucho"),
    ("A2", "C", "ich gehe (primera persona)"),
]
cnums = [reg_ex(lv, "texto con huecos", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · LÜCKENTEXT · Huecos", 24)
bf.para(f"Jonas freut sich auf das Wochenende. Am Samstag kauft er einen Kürbis und ({cnums[0]})___ ihn zu Hause. Am Nachmittag ({cnums[1]})___ er in die Bibliothek — sie hat am Samstag ein besonderes Programm. Am Abend spielt Dortmund, und Jonas sieht das Spiel mit Freunden. In der Nacht wird die Uhr ({cnums[2]})___: Die ({cnums[3]})___ beginnt. Am Sonntag schläft Jonas eine Stunde ({cnums[4]})___. Draußen ist es kalt, der erste ({cnums[5]})___ ist da. „Ein Sonntag mit 25 Stunden“, sagt Jonas, „({cnums[6]})___ mir gut! Und am Montag ({cnums[7]})___ ich wieder in die Schule.“", 20.5)
bf.expl("Opciones:")
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
bf.head("B · WISSENSFRAGEN · Quiz", 24)
bf.ex("B1", "opción múltiple", "A", "el Día de las Bibliotecas recuerda a Preusker",
      "Der Tag der Bibliotheken erinnert an... A. Karl Preusker · B. Martin Luther · C. Lucas Cranach", size=19.5, gap=8)
bf.ex("A2", "opción múltiple", "B", "el domingo a las 3 se atrasa una hora",
      "Die Uhr wird umgestellt am... A. Freitag um 20.30 Uhr · B. Sonntag um 3.00 Uhr · C. Samstag um Mitternacht", size=19.5, gap=8)
bf.ex("A2", "opción múltiple", "A", "O bis O = de octubre a Pascua",
      "„Von O bis O“ heißt: Winterreifen von... A. Oktober bis Ostern · B. Oktober bis Oktober · C. Ostern bis Oktober", size=19.5, gap=8)
bf.ex("B1", "opción múltiple", "B", "el Klassiker se juega en Dortmund",
      "Am 31. Oktober spielen die Bayern... A. zu Hause · B. in Dortmund · C. in Berlin", size=19.5, gap=8)
bf.ex("B1", "opción múltiple", "B", "la protección se forma en 10 a 14 días",
      "Die Grippeimpfung schützt nach... A. 2 Tagen · B. 10 bis 14 Tagen · C. 3 Monaten", size=19.5, gap=8)
bf.ex("B1", "opción múltiple", "B", "en las farmacias se vacuna a partir de los 18 años",
      "In Apotheken impft man Menschen... A. ab 6 Jahren · B. ab 18 Jahren · C. nur ab 60", size=19.5, gap=8)
bf.ex("A2", "opción múltiple", "B", "el partido destacado del sábado: Dortmund–Fráncfort",
      "Das Topspiel am Samstag ist... A. Freiburg–Bayern · B. Dortmund–Frankfurt · C. Stuttgart–Gladbach", size=19.5, gap=8)
bf.ex("A2", "opción múltiple", "B", "la hora de 2 a 3 aparece dos veces",
      "Die Stunde 2.00–3.00 Uhr gibt es in der Nacht... A. einmal · B. zweimal · C. gar nicht", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C · LESEVERSTEHEN · Lectura", 24)
bf.para("Frau Berger arbeitet in einer Berliner Bibliothek. Am Samstag, dem 24. Oktober, beginnt sie um halb zehn mit der Arbeit. Heute ist der Tag der Bibliotheken: Um elf Uhr spielt sie mit den Kindern Bibliotheks-Bingo. Am Nachmittag hilft sie bei den Book-Blind-Dates. Um 18 Uhr schließt die Bibliothek. Frau Berger fährt nach Hause und stellt am Abend alle Uhren um — morgen darf sie eine Stunde länger schlafen.", 20.5)
bf.ex("B1", "opción múltiple", "A", "halb zehn = 9:30",
      "Wann beginnt Frau Berger mit der Arbeit? A. um 9.30 Uhr · B. um 10.30 Uhr · C. um halb elf", size=19.5, gap=8)
bf.ex("A2", "opción múltiple", "B", "a las once juega al Bingo con los niños",
      "Was spielt sie um elf Uhr mit den Kindern? A. Fußball · B. Bibliotheks-Bingo · C. Karten", size=19.5, gap=8)
bf.ex("A2", "opción múltiple", "B", "por la noche, en casa, ajusta los relojes",
      "Was macht sie am Abend zu Hause? A. Sie schnitzt einen Kürbis. · B. Sie stellt die Uhren um. · C. Sie liest ein Buch.", size=19.5, gap=8)
bf.ex("B1", "opción múltiple", "B", "como el reloj se atrasa, puede dormir más",
      "Warum darf sie am Sonntag länger schlafen? A. Die Bibliothek ist zu. · B. Die Uhr wird zurückgestellt. · C. Sie hat Urlaub.", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D · SÄTZE BAUEN · Formar frases", 24)
bf.ex("A2", "formar frases", "Die Uhr wird am Sonntag zurückgestellt.", "wird en segunda posición, el participio al final",
      "die Uhr / wird / am Sonntag / zurückgestellt → ___", instr="Forma la frase", size=19.5, gap=8)
bf.ex("A2", "formar frases", "Wir schlafen eine Stunde länger.", "orden sujeto–verbo–complemento",
      "wir / schlafen / eine Stunde / länger → ___", instr="Forma la frase", size=19.5, gap=8)
bf.ex("B1", "formar frases", "Die Kinder freuen sich, weil Ferien sind.", "el verbo va al final en la frase con weil",
      "die Kinder / freuen sich / weil / Ferien / sind → ___", instr="Forma la frase", size=19.5, gap=8)
bf.ex("B1", "formar frases", "Am Samstag ist der Tag der Bibliotheken.", "empieza la indicación de tiempo; el verbo, en segunda posición",
      "am Samstag / ist / der Tag / der Bibliotheken → ___", instr="Forma la frase", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E · ÜBERSETZEN · Traducción", 24)
bf.ex("A2", "traducción", "La noche tiene 25 horas.", "Stunden = horas",
      "Die Nacht hat 25 Stunden.", instr="Traduce al español", size=19.5, gap=8)
bf.ex("A2", "traducción", "El sábado por la noche ajusto el reloj.", "umstellen = ajustar (un reloj)",
      "Ich stelle die Uhr am Samstagabend um.", instr="Traduce al español", size=19.5, gap=8)
bf.ex("B1", "traducción", "Am Sonntag schlafe ich eine Stunde länger.", "dormir una hora más = eine Stunde länger schlafen",
      "El domingo duermo una hora más.", instr="Traduce al alemán", size=19.5, gap=8)
bf.ex("B1", "traducción", "In der Bibliothek kann man Bücher leihen.", "kann man ... leihen = se pueden tomar prestados",
      "En la biblioteca se pueden prestar libros.", instr="Traduce al alemán", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F · WÖRTER PAAREN · Parejas", 24)
bf.match_set("B1", "emparejar",
             ["die Umstellung", "die Mitgliedstaaten", "die Mehrheit", "der Feiertag"],
             ["ein Tag, an dem man nicht arbeiten muss",
              "der Wechsel zwischen Sommer- und Winterzeit",
              "die Länder, die zu einer Union gehören",
              "mehr als die Hälfte, zum Beispiel 84 Prozent"],
             ["b", "c", "d", "a"],
             ["Umstellung = el cambio entre horario de verano e invierno, b", "Mitgliedstaaten = los Estados miembros, c", "Mehrheit = la mayoría, d", "Feiertag = el día festivo, a"],
             instr="Une las parejas")

# ---- G. dialogue ----
ddefs = [
    ("A2", "A", "Buch = el libro (para su hijo)"),
    ("B1", "B", "im ersten Stock = en el primer piso (sobre la planta baja)"),
    ("A2", "C", "Bingo = el bingo de la biblioteca"),
    ("B1", "A", "Bibliotheksausweis = el carné de la biblioteca"),
    ("B1", "B", "behalten = quedarse con (el libro)"),
]
dnums = [reg_ex(lv, "completar el diálogo", k, nt) for lv, k, nt in ddefs]
bf.head("G · DIALOG · Completar el diálogo", 24)
bf.para(f"— Guten Tag! Ich suche ein Buch für meinen Sohn. — Gern. Wie alt ist er? — Er ist neun, und er mag Tiere. — Dann ist dieses ({dnums[0]})___ perfekt: „Tiere im Herbst“. Mehr Tierbücher finden Sie im ersten ({dnums[1]})___. — Danke! Gibt es heute auch das ({dnums[2]})___? — Ja, um elf Uhr im Kinderzimmer. Bitte zeigen Sie mir noch Ihren ({dnums[3]})___. — Hier ist er. Wie lange kann ich das Buch ({dnums[4]})___? — Drei Wochen. Viel Spaß beim Lesen!", 20.5)
bf.expl("Opciones:")
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
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "redacción", "Pregunta abierta — sigue los puntos del cuadro de escritura; el texto modelo está en el cuadro de esta página", "Se califica según los puntos indicados")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · SCHREIBEN · Redacción", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Mein Sonntag, der 25. Oktober». Erzählen Sie: Wie lange schlafen Sie? Was machen Sie am Morgen, am Nachmittag und am Abend? Schreiben Sie auch einen Satz über die Uhr! Die besten Texte drucken wir in VOL.2 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "Escribe en alemán 80–100 palabras: «Mi domingo, el 25 de octubre». Cuenta cuánto duermes, qué haces por la mañana, por la tarde y por la noche, y escribe también una frase sobre el reloj.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MUSTER · Texto modelo (87 palabras)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Am Sonntag, dem 25. Oktober, schlafe ich eine Stunde länger. Dann frühstücke ich langsam mit meiner Familie. Um elf Uhr gehe ich in den Park, denn die Sonne scheint. Am Nachmittag lese ich mein neues Buch aus der Bibliothek. Am Abend koche ich eine Suppe mit Kürbis. Danach rufe ich meine Freundin an. Wir sprechen über das Fußballspiel am Samstag. Dortmund hat gewonnen, und wir freuen uns. Der Sonntag mit 25 Stunden ist mein Lieblingstag. Ich gehe früh ins Bett, denn am Montag beginnt die Arbeit wieder.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 296
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "ANTWORTEN · Todas las respuestas con explicación (páginas 1 a 8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Página {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
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
