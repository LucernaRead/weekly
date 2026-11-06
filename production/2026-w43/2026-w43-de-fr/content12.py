# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-de-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · FRONT PAGE (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1 · ERSTE AUSGABE", 23, "sans", True, OLIVE)
p.text(975, 92, "WÖCHENTLICH AUF DEUTSCH · CHAQUE SEMAINE · L'ALLEMAND DES ALLEMANDS", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "WOCHE VOM 19. BIS 25. OKTOBER 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Die Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "JOURNAL ALLEMAND · VOL.1 · HORLOGES · VACANCES · GELÉE", 46, "serif", True, INK, anchor="middle")
p.text(975, 372, "TEXTE EN ALLEMAND · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES", 20, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# clock band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "SONNTAG WIRD DIE UHR ZURÜCKGESTELLT — EINE STUNDE LÄNGER SCHLAFEN!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "In der Nacht von Samstag auf Sonntag endet die Sommerzeit: Um 3.00 Uhr springt die Uhr auf 2.00 Uhr zurück.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "L'heure recule dimanche", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "La nuit de 25 heures · page 2", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "DIE TOPMELDUNG · À la une", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Eine Stunde geschenkt: Deutschland stellt die Uhren zurück — und elf Länder haben Ferien", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Von der Lucerna-Redaktion · Leseniveau: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Am Sonntag ist es wieder so weit: Deutschland stellt die Uhren um. In der Nacht von Samstag auf Sonntag endet die Sommerzeit. Um 3.00 Uhr wird die Uhr eine Stunde zurückgestellt — auf 2.00 Uhr. Die Nacht hat dann 25 Stunden, und alle dürfen eine Stunde länger schlafen.")
f.para("Warum? Im Sommer ist es abends länger hell — das war die Idee: mehr Licht am Abend. Im Oktober sind die Tage schon kurz, und die Winterzeit beginnt — bis zum 28. März 2027.")
f.para("Und das ist nicht alles: Elf Bundesländer haben in dieser Woche gleichzeitig Herbstferien — der Höhepunkt in diesem Herbst. Viele Familien reisen, und die Züge und Freizeitparks sind voll.")
f.para("Auch der Sport liebt diese Woche: Am Dienstag und Mittwoch spielt die Champions League, am Freitag beginnt der 7. Spieltag der Bundesliga. Am Sonntag spielen Hoffenheim und Freiburg schon in der neuen Zeit — mehr dazu auf Seite 4.")
f.para("Das ist die erste Ausgabe von Die Lucerna auf Deutsch. Jede Woche lesen wir mit Ihnen das echte Deutschland — langsam, klar und ehrlich. Willkommen!")
f.expl("Notes — umstellen = régler · zurückstellen = reculer · Sommerzeit = heure d'été · Winterzeit = heure d'hiver · Bundesland = État fédéré.")
f.box("DIE WOCHE IN ZAHLEN · Chiffres", [
    ("25 — Stunden hat die Nacht von Samstag auf Sonntag (25 heures)", "serif", False, INK, 20.5, 1.35),
    ("11 — Bundesländer haben gleichzeitig Herbstferien (11 Länder en vacances)", "serif", False, INK, 20.5, 1.35),
    ("8 000+ — Bibliotheken gibt es in Deutschland (plus de 8 000)", "serif", False, INK, 20.5, 1.35),
])
f.head("JETZT ÜBEN · Pratiquez", 25)
f.ex("A2", "à compléter", "zurückgestellt", "zurückstellen = reculer",
     "Am Sonntag wird die Uhr eine Stunde ___.", size=20.5)
f.ex("A2", "à compléter", "25", "la nuit de 25 heures",
     "Die Nacht von Samstag auf Sonntag hat ___ Stunden.", size=20.5)
f.ex("A2", "à compléter", "Herbstferien", "les vacances d'automne",
     "Elf Bundesländer haben in dieser Woche ___.", size=20.5)
f.ex("A2", "à compléter", "Winterzeit", "jusqu'au 28 mars 2027",
     "Am Sonntag beginnt die ___ — sie dauert bis zum 28. März 2027.", size=20.5)
f.ex("B1", "à compléter", "länger", "dormir une heure de plus",
     "In der Nacht zum Sonntag dürfen alle eine Stunde ___ schlafen.", size=20.5)
f.ex("B1", "à compléter", "elf", "11 Länder en vacances en même temps",
     "In dieser Woche haben ___ Bundesländer gleichzeitig Ferien.", size=20.5)
f.end_report()

# ---- questions of the week (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "FRAGEN", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "DER WOCHE", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Les questions des guides allemands", 19, "sans", False, GREY)
gt = [
    ("„Vor oder zurück?“", 250),
    ("„Wann wird umgestellt?“", 226),
    ("„Handy: allein um?“", 196),
    ("„Warum Sommerzeit?“", 158),
    ("„Bleibt das für immer?“", 122),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE if i == 0 else GOLD)
    byy += 92
p.text(gx + 22, byy + 16, "Die fünf Fragen stellen die Ratgeber", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "in ganz Deutschland in dieser Woche.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "Les guides y répondent dans tout le pays.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "IN DIESER AUSGABE · Sommaire", 24, "sans", True, OLIVE)
som = [
    ("S.2", "Die Uhr & der erste Frost", "A2"),
    ("S.3", "Zwei Feste, ein Tag", "A2→B1"),
    ("S.4", "Königsklasse & Liga", "B1"),
    ("S.5", "Ferien ohne Schule", "B1"),
    ("S.6", "Umstellung abschaffen?", "B2"),
    ("S.7", "Sätze der Woche", "A2→B2"),
    ("S.8", "Übungen & Lösungen", "alle"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 72, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "DAS WORT DER WOCHE", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
p.para(gx, my + 76, "« zurückstellen » : Die Uhr geht eine Stunde zurück; Gegenteil: vorstellen.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, my + 152, "Reculer (une horloge). Contraire : vorstellen. L'astuce : page 2.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "frost.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Raureif an den Zweigen: In der Nacht zum Dienstag kam der erste Frost des Herbstes — östlich von Weser und Werra lokal bis minus ein Grad, am Boden bis minus drei Grad. (Seite 2)",
        "Foto: Courtney Celley, U.S. Fish and Wildlife Service — public domain")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-herbst")
f2.head("DER HERBST BEGINNT RICHTIG", 25)
f2.para("Kurze Tage, die ersten kalten Nächte, volle Bibliotheken und ein Spieltag in zwei Zeiten: Der Herbst zeigt in dieser Woche sein ganzes Programm.", 22.5)
f2.para("Sein Geschenk an alle Leser ist eine Stunde mehr Schlaf. Nehmen Sie sie — und lesen Sie weiter auf Seite 2!", 22.5)
f2.end_report()
# col 3 KURZ & GUT
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "KURZ & GUT · En bref", 24, "sans", True, OLIVE)
brefs = [
    ("UHRZEIT", "Sonntag, 3.00 Uhr: Die Uhren gehen eine Stunde zurück. (Seite 2)"),
    ("BIBLIOTHEKEN", "Samstag ist Tag der Bibliotheken — Berlin macht eine ganze Aktionswoche. (Seite 5)"),
    ("FUSSBALL", "Am Sonntag spielt die Bundesliga zum ersten Mal in der Winterzeit. (Seite 4)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "BLITZQUIZ · Quiz éclair", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lisez la une et choisissez la bonne réponse · Réponses page 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "QCM", "B", "on recule d'une heure dimanche",
      "Die Uhren werden am Sonntag... A. eine Stunde vorgestellt · B. eine Stunde zurückgestellt · C. gar nicht umgestellt", size=21)
qf.ex("A2", "QCM", "C", "11 Länder ont les vacances d'automne",
      "Wie viele Bundesländer haben Herbstferien? A. fünf · B. neun · C. elf", size=21)
qf.ex("A2", "QCM", "A", "l'heure d'hiver dure jusqu'au 28 mars 2027",
      "Die Winterzeit dauert bis... A. 28. März 2027 · B. 1. November · C. 31. Oktober", size=21)
qf.ex("A2", "QCM", "B", "Journée des bibliothèques : samedi 24 octobre",
      "Der Tag der Bibliotheken ist am... A. Freitag · B. Samstag · C. Sonntag", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LEBEN · Vie", "Die Lucerna", "LEVEL A2 · Die Uhr, der Frost & die Reifen · Horloges, gel et pneus")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Eine Stunde mehr: Die längste Nacht des Jahres", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: A2")
f.para("Sie kommt nur einmal im Jahr: die Nacht mit 25 Stunden. In der Nacht von Samstag, dem 24. Oktober, auf Sonntag, den 25. Oktober, endet in Deutschland die Sommerzeit. Um 3.00 Uhr springen die Uhren auf 2.00 Uhr zurück.")
f.para("Die Stunde von 2.00 bis 3.00 Uhr gibt es in dieser Nacht zweimal. Die Physikalisch-Technische Bundesanstalt — sie wacht in Braunschweig über die genaue Zeit — nennt die erste Stunde 2A und die zweite 2B. Wer um 2.30 Uhr aufwacht, weiß also nicht: Ist es die erste oder die zweite halbe Stunde?")
f.para("Was muss ich selbst umstellen? Handy und Computer machen es allein. Die Funkuhr am Bett auch. Aber die Uhr am Backofen, die alte Wanduhr in der Küche und die Uhr im Auto brauchen Ihre Hand. Unser Tipp: Stellen Sie die Uhren schon am Samstagabend um — dann ist der Sonntagmorgen ganz entspannt.")
f.para("Und warum das alles? Die Sommerzeit kam 1980 nach Deutschland — beide deutsche Staaten begannen damals mit ihr. Die Idee: Am Abend bleibt es länger hell, und das Land braucht weniger Licht. Ob die Idee heute noch stimmt, lesen Sie auf Seite 6.")
f.box("DER MERKSATZ · L'astuce", [
    ("„Im Frühjahr stellt man die Gartenmöbel VOR das Haus — im Herbst stellt man sie ZURÜCK ins Haus.“ So merken sich die Deutschen die Richtung: vor im Frühjahr, zurück im Herbst.", "serif", False, INK, 21.5, 1.4),
])
f.head("DER ERSTE FROST IST DA", 25)
f.para("Der Herbst begann in dieser Woche mit kalten Fingern: In der Nacht von Montag auf Dienstag (19./20. Oktober) kam der erste Frost. Die Temperaturen fielen auf 8 bis 0 Grad, östlich von Weser und Werra lokal auf minus 1 Grad; am Boden gab es bis minus 3 Grad. Die Gärtner deckten ihre Pflanzen ab, und am Morgen kratzten die ersten Autofahrer ihre Scheiben frei.", 23.5)
f.para("Ab der Nacht zum Mittwoch kommt dann Regen aus dem Westen — die Nächte werden milder. Aber der Frost ist eine Warnung: Der Winter ist nicht mehr weit.", 23.5)
f.para("Für Autofahrer heißt der Oktober: Winterreifen! Die Regel heißt „Von O bis O“ — von Oktober bis Ostern. Wichtig: Ein Gesetz mit festen Daten gibt es nicht. Winterreifen sind Pflicht, wenn es glatt ist — bei Eis, Schneematsch und Frost. Und seit Oktober 2024 reicht das alte M+S-Zeichen nicht mehr: Der Reifen braucht das Alpensymbol, einen Berg mit Schneeflocke.", 23.5)
f.gloss("die Bundesanstalt = l'institut fédéral (la PTB veille sur l'heure exacte en Allemagne) · der Frost = le gel · der Reifen = le pneu · glatt = glissant · der Schneematsch = la neige fondue.")
f.end_report()

# col 3: image + facts (sequential, measured)
ix = COLX[3]
image(p, "atomuhr.jpg", ix, 200, CW, 430)
cy3 = caption(p, ix, 630, CW, "Die NIST-F1 in den USA: eine der genauesten Uhren der Welt. Auch Deutschlands Zeit kommt aus einer Atomuhr — die PTB in Braunschweig sendet das Funksignal.",
              "Foto: NIST — public domain")
sav = ["Die Nacht zum Sonntag hat 25 Stunden — die längste Nacht des Jahres.",
       "Die Stunde von 2.00 bis 3.00 Uhr gibt es in dieser Nacht zweimal: 2A und 2B.",
       "Unter 7 Grad greifen Winterreifen besser, sagen die Reifenexperten."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in sav) + 14
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WUSSTEN SIE DAS?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "Und Sie? Haben Sie eine Funkuhr zu Hause? Stellen Sie Ihre Uhren selbst um? Schreiben Sie zwei Sätze auf Deutsch und schicken Sie sie an die Redaktion: Die besten kommen in VOL.2 (Seite 7, «Leserbriefe»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Avez-vous une horloge radio-pilotée ? Vous réglez vos horloges vous-même ? Écrivez deux phrases en allemand !", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE? · À vous", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Avez-vous une horloge radio-pilotée ? Vous réglez vos horloges vous-même ? Écrivez deux phrases en allemand !", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Telling the time wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "DIE UHRZEIT SAGEN · Dire l'heure", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Die Zeiten der Woche · Toutes les heures de la semaine", 20, "sans", False, GREY, anchor="end")

def clock(cx, cy, r, hh, mm, label):
    p.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fdfaf0" stroke="{INK}" stroke-width="3"/>')
    import math
    for k in range(12):
        a = math.radians(k * 30)
        x1, y1 = cx + (r - 12) * math.sin(a), cy - (r - 12) * math.cos(a)
        x2, y2 = cx + r * math.sin(a), cy - r * math.cos(a)
        p.add(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{INK}" stroke-width="2.4"/>')
    ah = math.radians((hh % 12) * 30 + mm * 0.5)
    am = math.radians(mm * 6)
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.55)*math.sin(ah):.0f}" y2="{cy - (r*0.55)*math.cos(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.82)*math.sin(am):.0f}" y2="{cy - (r*0.82)*math.cos(am):.0f}" stroke="{BRICK}" stroke-width="4" stroke-linecap="round"/>')
    p.text(cx, cy + r + 34, label, 22, "serif", True, INK, anchor="middle")

clock(240, dy + 130, 70, 8, 0, "Es ist acht Uhr.")
clock(560, dy + 130, 70, 2, 30, "Es ist halb drei (2.30 Uhr).")
clock(880, dy + 130, 70, 7, 45, "Es ist Viertel vor acht.")
lx = 1090
ly = dy + 58
for line in [
    ("halb drei", "= 2.30 Uhr ! (et non 3.30)"),
    ("Viertel vor acht", "= 7.45 Uhr (huit heures moins le quart)"),
    ("Viertel nach acht", "= 8.15 Uhr (huit heures et quart)"),
    ("Mittag / Mitternacht", "= 12.00 Uhr am Tag / in der Nacht"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 300, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 36
p.para(lx, ly + 22, "Wichtig: Dortmund–Frankfurt beginnt Samstag um 18.30 Uhr — noch Sommerzeit. Freiburg–Bayern am Sonntag um 17.30 Uhr — schon Winterzeit.", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · Exercices de la page 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · Les niveaux se mélangent — chaque réponse par son numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · WIE SPÄT IST ES?", 25)
e.expl("Regardez les heures et complétez les phrases.")
e.ex("A2", "à compléter", "halb", "halb drei = 2 h 30 (la demie vient avant drei)",
     "2:30 — Es ist ___ drei.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Viertel vor", "7 h 45 = huit heures moins le quart",
     "7:45 — Es ist ___ acht.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Viertel nach", "8 h 15 = huit heures et quart",
     "8:15 — Es ist ___ acht.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Mitternacht", "0 h 00 = minuit",
     "0:00 — Es ist ___. Die Stadt schläft.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Mittag", "12 h 00 dans la journée = midi",
     "12:00 am Tag — Es ist ___. Zeit für Suppe!", instr="Compléter", size=20, gap=8)
e.head("B · DAS PERFEKT", 25)
e.expl("Mettez les phrases au Perfekt (passé composé).")
e.ex("A2", "transformation", "Deutschland hat die Uhren am Sonntag umgestellt.", "trennbar: um-ge-stellt",
     "Deutschland (umstellen) die Uhren am Sonntag. → ___", instr="Réécrire", size=20, gap=8)
e.ex("A2", "transformation", "Die Nacht hat 25 Stunden gehabt.", "haben → gehabt",
     "Die Nacht (haben) 25 Stunden. → ___", instr="Réécrire", size=20, gap=8)
e.ex("B1", "transformation", "Der Frost ist in der Nacht zum Dienstag gekommen.", "kommen va avec sein",
     "Der Frost (kommen) in der Nacht zum Dienstag. → ___", instr="Réécrire", size=20, gap=8)
e.ex("A2", "transformation", "Wir haben eine Stunde länger geschlafen.", "schlafen → geschlafen",
     "Wir (schlafen) eine Stunde länger. → ___", instr="Réécrire", size=20, gap=8)
e.ex("B1", "transformation", "Die Familien sind in den Ferien gereist.", "reisen va avec sein",
     "Die Familien (reisen) in den Ferien. → ___", instr="Réécrire", size=20, gap=8)
e.head("C · LESEVERSTEHEN", 25)
e.expl("Lisez l'article page 2 et choisissez la bonne réponse.")
e.ex("A2", "QCM", "C", "2A et 2B : l'heure existe deux fois",
     "Die Stunde 2.00–3.00 Uhr gibt es... A. nie · B. einmal · C. zweimal", size=20, gap=8)
e.ex("A2", "QCM", "C", "l'horloge du four se règle à la main",
     "Was stellt sich NICHT allein um? A. Handy · B. Computer · C. Backofen-Uhr", size=20, gap=8)
e.ex("A2", "QCM", "A", "le premier gel dans la nuit de lundi à mardi",
     "Der erste Frost kam in der Nacht... A. von Montag auf Dienstag · B. von Freitag auf Samstag · C. am Sonntag", size=20, gap=8)
e.ex("A2", "QCM", "B", "le symbole alpin est exigé depuis 2024",
     "Winterreifen brauchen seit 2024... A. M+S-Zeichen · B. Alpensymbol · C. roten Punkt", size=20, gap=8)
e.head("D · DIE WÖRTER", 25)
e.match_set("A2", "appariement",
            ["der Frost", "der Reifen", "die Funkuhr", "glatt"],
            ["Uhr mit automatischem Zeitsignal",
             "Frost an Pflanzen und Scheiben",
             "der runde Gummiteil am Auto",
             "so rutschig wie Eis"],
            ["b", "c", "a", "d"],
            ["Frost = le gel sur les plantes et les vitres, b (la définition est approximative)", "Reifen = l'anneau de caoutchouc de la voiture, c", "Funkuhr = une horloge qui reçoit le signal toute seule, a", "glatt = glissant comme la glace, d"],
            instr="Relier les paires")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leben.svg")
print("P2 saved, exercises so far:", len(REG))
