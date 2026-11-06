# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-de-es/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN · Ejercicios y respuestas", "Die Lucerna", "SCHLUSSTEST · Prueba final · Alle Antworten unten auf dieser Seite — todas las respuestas abajo en esta página")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "A", "beginnt (3.ª pers. sing.)"),
    ("A2", "B", "bastelt (3.ª pers. sing.)"),
    ("A2", "A", "geht (3.ª pers. sing.)"),
    ("A2", "B", "singt (3.ª pers. sing.)"),
    ("A2", "A", "schaut (3.ª pers. sing.)"),
    ("B1", "B", "sieht (3.ª pers. sing.)"),
    ("A2", "B", "erzählt (3.ª pers. sing.)"),
    ("B1", "A", "beginnt (3.ª pers. sing.)"),
]
cnums = [reg_ex(lv, "Huecos", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · LÜCKENTEXT · Huecos", 24)
bf.para(f"Lena freut sich auf die Novemberwoche. Am Montag ({cnums[0]})___ die Schule wieder, und Lena ({cnums[1]})___ eine Laterne aus Papier. Am Mittwoch ({cnums[2]})___ sie mit ihrer Klasse beim Laternenumzug mit und ({cnums[3]})___ Martinslieder. Am Freitagabend ({cnums[4]})___ sie Deutschland in Belgrad. Am Sonntag ({cnums[5]})___ sie die NFL in München im Fernsehen. In der Schule ({cnums[6]})___ Lena: „Die Woche war toll! Der Karneval ({cnums[7]})___ um 11.11 Uhr.“", 20.5)
bf.bridge("Opciones:")
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
bf.head("B · WISSENSFRAGEN · Quiz", 24)
bf.ex("B1", "opción múltiple", "A", "el carnaval empieza a las 11.11",
      "Die Karnevalssession beginnt um... A. 11.11 Uhr · B. 15.30 Uhr · C. 20.45 Uhr", size=19.5, gap=8)
bf.ex("A2", "opción múltiple", "B", "fuera, en Serbia, el viernes",
      "Deutschland spielt am Freitag in... A. Berlin · B. Belgrad · C. München", size=19.5, gap=8)
bf.ex("A2", "opción múltiple", "C", "NFL el domingo a las 15.30",
      "Das NFL-Spiel in München beginnt um... A. 11.11 Uhr · B. 20.45 Uhr · C. 15.30 Uhr", size=19.5, gap=8)
bf.ex("B1", "opción múltiple", "A", "el día de recuerdo es el 15 de noviembre",
      "Der Volkstrauertag ist am... A. 15. November · B. 11. November · C. 22. November", size=19.5, gap=8)
bf.ex("B1", "opción múltiple", "B", "el impuesto de los hogares es 2,05 céntimos",
      "Die Stromsteuer für Haushalte beträgt... A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent", size=19.5, gap=8)
bf.ex("A2", "opción múltiple", "B", "el seleccionador anuncia la lista el 5 de noviembre",
      "Klopp nennt seinen Kader am... A. 13. November · B. 5. November · C. 9. November", size=19.5, gap=8)
bf.ex("B1", "opción múltiple", "A", "la ZDF en directo desde las 13.30",
      "Die Gedenkstunde überträgt ab 13.30 Uhr... A. das ZDF · B. RTL · C. die ARD", size=19.5, gap=8)
bf.ex("A2", "opción múltiple", "C", "Totensonntag es el 22 de noviembre",
      "Der Totensonntag ist am... A. 15. November · B. 18. November · C. 22. November", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C · LESEVERSTEHEN · Lectura", 24)
bf.para("Familie Berger aus Stuttgart hat am Montag wieder Schule: Die Kinder gehen um halb acht aus dem Haus. Am Mittwoch bastelt die Familie eine Laterne aus Papier. Am Freitag schaut sie Deutschland in Belgrad im Fernsehen. Am Sonntag schaut sie das NFL-Spiel um 15.30 Uhr. „Eine Woche mit Laternen und Football“, sagt Frau Berger.", 20.5)
bf.ex("B1", "opción múltiple", "A", "halb acht = 7:30",
      "Wann gehen die Kinder aus dem Haus? A. um halb acht · B. um acht · C. um halb neun", size=19.5, gap=8)
bf.ex("A2", "opción múltiple", "B", "hacer un farolillo el miércoles",
      "Was bastelt die Familie am Mittwoch? A. ein Kostüm · B. eine Laterne · C. einen Kürbis", size=19.5, gap=8)
bf.ex("A2", "opción múltiple", "A", "ver a Alemania el viernes",
      "Was schaut die Familie am Freitag? A. Deutschland in Belgrad · B. die NFL · C. den Karneval", size=19.5, gap=8)
bf.ex("B1", "opción múltiple", "B", "NFL el domingo a las 15.30",
      "Wann schaut die Familie das NFL-Spiel? A. Samstag 18.30 Uhr · B. Sonntag 15.30 Uhr · C. Freitag 20.45 Uhr", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D · SÄTZE BAUEN · Formar frases", 24)
bf.ex("A2", "formar frases", "Die Karnevalssession beginnt am Mittwoch.", "el tiempo, el verbo en segundo lugar",
      "die Karnevalssession / beginnt / am Mittwoch → ___", instr="Forma la frase", size=19.5, gap=8)
bf.ex("A2", "formar frases", "Wir basteln eine Laterne aus Papier.", "orden sujeto–verbo–objeto",
      "wir / basteln / eine Laterne / aus Papier → ___", instr="Forma la frase", size=19.5, gap=8)
bf.ex("B1", "formar frases", "Die Kinder gehen am Montag wieder in die Schule.", "el tiempo primero, el verbo en segundo lugar",
      "die Kinder / gehen / am Montag / wieder in die Schule → ___", instr="Forma la frase", size=19.5, gap=8)
bf.ex("B1", "formar frases", "Am Sonntag ist Volkstrauertag in ganz Deutschland.", "lugar y tiempo primero, verbo en segundo lugar",
      "am Sonntag / ist / Volkstrauertag / in ganz Deutschland → ___", instr="Forma la frase", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E · ÜBERSETZEN · Traducción", 24)
bf.ex("A2", "traducción", "El carnaval empieza a las 11.11 en Colonia.", "beginnen = empezar",
      "Der Karneval beginnt um 11.11 Uhr in Köln. (traducir al español)", instr="Traduce al español", size=19.5, gap=8)
bf.ex("A2", "traducción", "Hago un farolillo el miércoles.", "basteln = hacer manualidades",
      "Ich bastle am Mittwoch eine Laterne. (traducir al español)", instr="Traduce al español", size=19.5, gap=8)
bf.ex("B1", "traducción", "Las clases volvieron a empezar el 9 de noviembre.", "wieder begonnen = vuelto a empezar",
      "Die Schule hat am 9. November wieder begonnen. (traducir al español)", instr="Traduce al español", size=19.5, gap=8)
bf.ex("B1", "traducción", "Am Sonntag schaue ich das NFL-Spiel.", "ver un partido = das Spiel schauen",
      "Veo el partido de la NFL el domingo. (traducir al alemán)", instr="Traduce al alemán", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F · WÖRTER PAAREN · Parejas", 24)
bf.match_set("B1", "emparejar",
             ["der Mantel", "die Laterne", "das Geisterspiel", "die Versöhnung"],
             ["das Licht aus Papier, das die Kinder am Abend tragen",
              "der warme Umhang, den Martin mit dem Bettler teilte",
              "die Aussöhnung nach einem Streit — Frieden zwischen Menschen",
              "ein Spiel ohne Zuschauer im Stadion"],
             ["b", "a", "d", "c"],
             ["Mantel=manto b", "Laterne=farolillo a", "Geisterspiel=partido fantasma d", "Versöhnung=reconciliación c"],
             instr="Une las parejas")

# ---- G. dialogue ----
ddefs = [
    ("A2", "B", "singst (2.ª pers. sing.)"),
    ("A2", "A", "macht (2.ª pers. pl.)"),
    ("A2", "A", "essen (1.ª pers. pl.)"),
    ("B1", "B", "machst (2.ª pers. sing.)"),
    ("B1", "A", "schaue (1.ª pers. sing.)"),
]
dnums = [reg_ex(lv, "Completar el diálogo", k, nt) for lv, k, nt in ddefs]
bf.head("G · DIALOG · Completar el diálogo", 24)
bf.para(f"— Hallo, Lena! Bastelst du eine Laterne? — Ja, für St. Martin! Am Mittwoch gehen wir mit. — ({dnums[0]})___ du auch Martinslieder? — Ja, mit meiner Klasse. — Und was ({dnums[1]})___ ihr am Abend? — Wir singen und laufen mit den Laternen. Am Sonntag ({dnums[2]})___ wir Brezeln und schauen die NFL. — Lecker! Und was ({dnums[3]})___ du am Freitag? — Ich ({dnums[4]})___ Deutschland in Belgrad im Fernsehen!", 20.5)
bf.bridge("Opciones:")
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
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "Redacción", "Tarea abierta — sigue los puntos del recuadro; el texto modelo está en el recuadro de esta página", "Se evalúa según los puntos listados")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · SCHREIBEN · Redacción", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Novemberwoche». Erzählen Sie: Was basteln Sie? Welche Spiele schauen Sie? Mit wem? Schreiben Sie auch einen Satz über St. Martin oder den Volkstrauertag! Die besten Texte drucken wir in VOL.4 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "Escribe en alemán, 80–100 palabras: «Mi semana de noviembre». Di qué haces, qué partidos ves y con quién — y añade una frase sobre San Martín o el día de recuerdo.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MUSTER · Texto modelo (84 palabras)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche bastle ich eine Laterne. Am Mittwoch singe ich mit meiner Klasse Martinslieder und gehe beim Laternenumzug mit. Am Freitag schaue ich mit meiner Familie Deutschland in Belgrad im Fernsehen. Das Spiel ist ein Geisterspiel — ohne Zuschauer. Am Sonntag schaue ich die NFL in München im Fernsehen. Die Lions spielen gegen die Patriots. Der Karneval beginnt um 11.11 Uhr in Köln. Am Sonntag esse ich Brezeln und trinke Apfelschorle. Am Montag gehe ich wieder in die Schule. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 320
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "ANTWORTEN · Todas las respuestas con notas (páginas 1–8)", 26, "sans", True, OLIVE)
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
    kf.para(" · ".join(parts), 12, "sans", False, INK, 1.22, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
