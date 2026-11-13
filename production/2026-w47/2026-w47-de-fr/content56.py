# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUGEND　Jeunesse", "Die Lucerna", "LEVEL B1　Adventskalender, Wunschzettel & Schule　Calendrier de l'Avent, liste de souhaits et école")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P5-main")
f.title("Adventskalender basteln: 24 Türchen bis Weihnachten", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: B1")
f.para("Am Montag, dem 16. November, öffnen in Köln zwei große Weihnachtsmärkte. Aber für Kinder beginnt die schönste Zeit erst am 1. Dezember: Dann öffnet sich das erste Türchen des Adventskalenders. Bis dahin bleibt Zeit zum Basteln.")
f.para("Was ist ein Adventskalender? Ein Kalender mit 24 Türchen — für jeden Dezembertag bis Weihnachten eines. Hinter jedem Türchen wartet eine kleine Überraschung. Das kann Schokolade, ein Bild oder ein Spruch sein. Viele Familien basteln ihren Kalender selbst: aus Papier, Pappe und viel Fantasie.")
f.para("So alt ist die Idee: Schon im Jahr 1903 gab es einen Adventskalender mit dem Titel „Im Lande des Christkinds“. Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben. Das Bild auf dieser Seite zeigt ihn — über 120 Jahre alt, und die Idee lebt noch heute.")
f.para("Und der Wunschzettel? Im November schreiben viele Kinder ihren Wunschzettel für Weihnachten. Was steht darauf? Ein Buch, ein Spiel, ein Fahrrad — oder ein Besuch auf dem Weihnachtsmarkt. Der Wunschzettel kommt ans Fenster oder geht per Post an das Christkind oder den Weihnachtsmann.")
f.para("Was macht man nach der Schule im dunklen November? Lesen, was man im Herbst begonnen hat, oder einen Adventskalender basteln. In vielen Familien brennt im Advent eine Kerze auf dem Tisch, und auf dem Kalender leuchtet ein Stern. Unser Tipp: Suchen Sie sich ein Buch für die dunklen Abende — die Bibliotheken haben im November oft neue Bücher und Lesungen. Und wer Sport mag: Am Freitag kehrt die Bundesliga zurück.")
f.para("Auch der Fußball gehört zur Woche: Am Montag spielt die Nationalmannschaft in Berlin gegen die Niederlande — viele Jugendliche schauen das Spiel im Fernsehen. Am Freitag spielt der FC Bayern gegen Köln. Mehr dazu auf Seite 4.")
f.gloss("der Adventskalender = calendrier de l'Avent · das Türchen = petite porte · der Wunschzettel = liste de souhaits · das Christkind = Enfant Jésus · basteln = fabriquer.")
f.end_report()

# col 3: facts + vocab + Und Sie (hand-rolled; CORRECTED height formula — see W45 KIT §geometry)
ix = COLX[3]
facts = ["Ein Adventskalender hat 24 Türchen — bis Weihnachten.",
         "Das erste Türchen öffnet sich am 1. Dezember.",
         "Schon 1903 gab es den Kalender „Im Lande des Christkinds“."]
sy3 = 200
sh = 45 + 33 * len(facts) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in facts)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ADVENTSKALENDER", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 facts ends", sy3 + sh)
words = ["das Türchen — petite porte", "der Wunschzettel — liste de souhaits", "das Christkind — Enfant Jésus",
         "die Schokolade — chocolat", "die Kerze — bougie", "der Stern — étoile"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ADVENTSWÖRTER　Avent", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Basteln Sie einen Adventskalender? Was steht auf Ihrem Wunschzettel? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("Fabriquez-vous un calendrier de l'Avent ? Votre liste de souhaits : qu'y a-t-il ? Écrivez en allemand !", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　Et vous ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Fabriquez-vous un calendrier de l'Avent ? Votre liste de souhaits : qu'y a-t-il ? Écrivez en allemand !", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 undsie ends", ey3 + eh)

# ---- Advent calendar image (col 3, below the boxes) ----
iy5 = ey3 + eh + 14  # FIX (2026-11-12): was 26; F1 added one prompt line (+29px) and the col-3 image/caption would cross the P5 exercises hline (occlusion LINEX, credit ink bottom 1746.4 vs hline top 1743). 14px gap puts the caption end at 1749.9, ~8.6px clear; ey stays 1756 so P5-ex is untouched.
image(p, "christkind.jpg", ix, iy5, CW, 313)
cy5 = caption(p, ix, iy5 + 313, CW,
              "Adventskalender aus dem Jahr 1903: „Im Lande des Christkinds“.",
              "Bild: Richard Ernst Kepler, 1903 — public domain")
print("P5 col3 image ends", cy5)

# ---- Wochenplan wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 300, fill=BOX)
p.text(sx + 24, 1162, "DER WOCHENPLAN DER REDAKTION　La semaine de la rédaction", 24, "sans", True, OLIVE)
planrows = [
    ("Mo 16.11.", "Nationalelf in Berlin: Deutschland – Niederlande (20.45 Uhr, ARD)."),
    ("Di 17.11.", "Weihnachtsmarkt am Dom: offizielle Eröffnung um 19 Uhr."),
    ("Mi 18.11.", "Buß- und Bettag: kein Unterricht in Bayern, Feiertag in Sachsen."),
    ("Do 19.11.", "Adventskalender basteln: Papier, Pappe, Schere — und Fantasie."),
    ("Fr 20.11.", "Bundesliga: Bayern – Köln (20.30 Uhr)."),
]
pyy = 1184
for t, txt in planrows:
    p.text(sx + 24, pyy + 24, t, 21, "sans", True, OLIVE)
    p.text(sx + 190, pyy + 24, txt, 21.5, "serif", False, INK)
    pyy += 45

# ---- P5 exercises ----
ey = 1756  # W47 D1: was 1780; col-3 image ends 1732.9, hline at ey-12=1744 clears it (FIX 2026-11-12: image now ends 1749.9, hline still clears it)
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Exercices page 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　Les niveaux se mélangent — cherchez par numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P5-ex")
e.head("A　LESEVERSTEHEN", 25)
e.bridge("Lisez la page 5. Choisissez la bonne réponse.")
e.ex("B1", "choix multiple", "A", "Première porte : 1er décembre",
     "Wann öffnet sich das erste Türchen? A. am 1. Dezember · B. am 16. November · C. am 29. November", size=22, gap=8)
e.ex("B1", "choix multiple", "B", "24 petites portes",
     "Wie viele Türchen hat ein Adventskalender? A. 12 · B. 24 · C. 30", size=22, gap=8)
e.ex("B1", "choix multiple", "B", "« Im Lande des Christkinds » (1903)",
     "Wie heißt der Adventskalender aus dem Jahr 1903? A. „Im Lande des Weihnachtsmanns“ · B. „Im Lande des Christkinds“ · C. „Im Lande der Engel“", size=22, gap=8)
e.ex("B1", "choix multiple", "B", "Liste : Enfant Jésus ou Père Noël",
     "Wohin geht der Wunschzettel? A. an den Osterhasen · B. an das Christkind oder den Weihnachtsmann · C. an den Nikolaus im Sommer", size=22, gap=8)
e.ex("A2", "choix multiple", "A", "Équipe nationale lundi",
     "Was schauen viele Jugendliche am Montag? A. die Nationalmannschaft in Berlin · B. die Bundesliga · C. den Weihnachtsmarkt", size=22, gap=8)
e.head("B　WÖRTER AUS DEM TEXT", 25)
e.bridge("Complétez avec les mots de l'encadré.")
e.para("Türchen · Wunschzettel · Christkind · Schokolade · Kerze · Stern", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "à compléter", "Türchen", "petite porte",
     "Am 1. Dezember öffnet sich das erste ___.", instr="Complétez", size=22, gap=8)
e.ex("B1", "à compléter", "Wunschzettel", "liste de souhaits",
     "Die Kinder schreiben im November ihren ___.", instr="Complétez", size=22, gap=8)
e.ex("B1", "à compléter", "Christkind", "Enfant Jésus",
     "Der Wunschzettel geht an das ___ oder den Weihnachtsmann.", instr="Complétez", size=22, gap=8)
e.ex("B1", "à compléter", "Schokolade", "chocolat",
     "Hinter einem Türchen wartet oft ___.", instr="Complétez", size=22, gap=8)
e.ex("A2", "à compléter", "Kerze", "bougie",
     "Im Advent brennt eine ___ auf dem Tisch.", instr="Complétez", size=22, gap=8)
e.ex("A2", "à compléter", "Stern", "étoile",
     "Auf dem Adventskalender ist ein ___.", instr="Complétez", size=22, gap=8)
e.head("C　SÄTZE MIT «WEIL»", 25)
e.bridge("Reliez deux phrases avec weil.")
e.ex("B1", "transformation", "Die Kinder freuen sich, weil der Advent beginnt.", "weil : verbe en fin",
     "Die Kinder freuen sich. Der Advent beginnt. (weil) → ___", instr="Réécrivez", size=22, gap=8)
e.ex("B1", "transformation", "Er bleibt zu Hause, weil es dunkel ist.", "ist en fin",
     "Er bleibt zu Hause. Es ist dunkel. (weil) → ___", instr="Réécrivez", size=22, gap=8)
e.ex("B1", "transformation", "Sie geht in die Bibliothek, weil sie ein Buch lesen will.", "will en fin",
     "Sie geht in die Bibliothek. Sie will ein Buch lesen. (weil) → ___", instr="Réécrivez", size=22, gap=8)
e.ex("B1", "transformation", "Köln feiert, weil die Weihnachtsmärkte öffnen.", "öffnen en fin",
     "Köln feiert. Die Weihnachtsmärkte öffnen. (weil) → ___", instr="Réécrivez", size=22, gap=8)
e.head("D　RICHTIG ODER FALSCH?", 25)
e.bridge("Vrai ou faux ?")
e.ex("A2", "vrai ou faux", "Richtig", "Marchés de Cologne : 16 novembre",
     "Am 16. November öffnen der Markt am Dom und der Markt der Engel. Richtig oder falsch?", instr="Vrai ou faux ?", size=22, gap=8)
e.ex("B1", "vrai ou faux", "Falsch", "Surprise derrière la porte",
     "Hinter jedem Türchen wartet nichts. Richtig oder falsch?", instr="Vrai ou faux ?", size=22, gap=8)
e.ex("A2", "vrai ou faux", "Richtig", "Liste des enfants à l'Enfant Jésus",
     "Die Kinder schreiben ihren Wunschzettel an das Christkind. Richtig oder falsch?", instr="Vrai ou faux ?", size=22, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jugend.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERTIEFUNG　Approfondissement", "Die Lucerna", "LEVEL B2　Stille Woche & Haushalt　Semaine calme et budget")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P6-main")
f.title("Eine stille Woche: Was bedeuten Buß- und Bettag und Totensonntag?", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: B2")
f.para("Am Mittwoch, dem 18. November, ist Buß- und Bettag. Am Sonntag, dem 22. November, ist Totensonntag. Zwischen beiden Tagen liegt eine stille Woche: keine lauten Feste, keine großen Partys — dafür Zeit zum Nachdenken. Was bedeuten diese Tage?")
f.para("Der Buß- und Bettag ist ein evangelischer Feiertag. Er lädt zur Buße und zum Nachdenken ein: Was war falsch in diesem Jahr? Was kann ich besser machen? Der Tag liegt immer elf Tage vor dem ersten Advent — in diesem Jahr am 18. November. Nur Sachsen feiert ihn als gesetzlichen Feiertag.")
f.para("Der Totensonntag ist der letzte Sonntag des Kirchenjahres. Evangelische Christen gedenken an diesem Tag ihrer Verstorbenen: Sie gehen auf den Friedhof, zünden Kerzen an und legen Blumen nieder. Am nächsten Sonntag beginnt mit dem ersten Advent ein neues Kirchenjahr.")
f.para("Zweites Thema: der Bundeshaushalt 2027. Er soll am Freitag, dem 27. November, verabschiedet werden. Auch die Stromsteuer ist noch offen: Kanzler Friedrich Merz will sie für alle senken. Haushalte zahlen weiter 2,05 Cent pro Kilowattstunde. Ob eine Einigung gelingt, ist offen.")
f.para("Zwei Themen, ein Muster: Die stillen Tage und der Haushalt betreffen fast jeden. Am Sonntag ist es still im Land. Am Montag geht die Debatte weiter — und die Weihnachtsmärkte öffnen wieder.")
f.para("Und die Kirche? Der erste Advent ist am 29. November. Dann beginnt die Adventszeit — mit Kerzen, Liedern und dem ersten Türchen des Adventskalenders. Die stille Woche ist der Übergang: vom November in den Advent.")
f.gloss("die Buße = repentir · das Kirchenjahr = année liturgique · der Verstorbene = le défunt · der Friedhof = cimetière · der Haushalt = budget · die Einigung = accord.")
f.end_report()

# col 3: numbers box + debate box (measured)
ix = COLX[3]
tl = [("18.11.", "Buß- und Bettag — elf Tage vor dem ersten Advent."),
      ("22.11.", "Totensonntag — der letzte Sonntag des Kirchenjahres."),
      ("29.11.", "Erster Advent — Beginn des neuen Kirchenjahres."),
      ("2,05", "Cent pro Kilowattstunde: Stromsteuer für Haushalte."),
      ("27.11.", "Verabschiedung des Bundeshaushalts 2027 geplant."),
      ("1995", "Seit diesem Jahr ist der Buß- und Bettag nur noch in Sachsen ein Feiertag.")]
tlh = 45 + 30.5 * len(tl) + 29.11 * sum(len(wrap(t, "serif", False, 20.5, CW - 152)) for yr, t in tl)
p.rect(ix, 200, CW, tlh, fill=BOX)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DIE ZAHLEN　En chiffres", 24, "sans", True, OLIVE)
yy3 += 52
for yr, t in tl:
    p.text(ix + 22, yy3 + 21, yr, 21, "sans", True, OLIVE)
    yy3 = p.para(ix + 130, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 152, 1.42) + 10
print("P6 col3 numbers ends", 200 + tlh)
deb = "Stille Tage: Gedenken braucht Ruhe — darüber sind sich fast alle einig. Haushalt: Wie stark die Stromsteuer sinkt, ist noch offen. Beides betrifft fast jeden Haushalt."
hy3 = 200 + tlh + 26
hh = 140 + 29.82 * len(wrap(deb, "serif", False, 21, CW - 44)) + 27.69 * (len(wrap("Jours calmes : le recueillement a besoin de calme — presque tout le monde est d'accord. Budget : la baisse de la taxe sur l'électricité reste ouverte. Les deux concernent presque chaque foyer.", "sans", False, 19.5, CW - 44)) - 1)
p.rect(ix, hy3, CW, hh, fill="#f0eee5")
yy3 = hy3 + 16
p.text(ix + 22, yy3 + 26, "DIE DEBATTE IN EINEM SATZ", 22.5, "sans", True, OLIVE)
yy3 += 50
yy3 = p.para(ix + 22, yy3 + 21, deb, 21, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Jours calmes : le recueillement a besoin de calme — presque tout le monde est d'accord. Budget : la baisse de la taxe sur l'électricité reste ouverte. Les deux concernent presque chaque foyer.", 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", hy3 + hh)

# ---- Die stille Woche wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 252, fill="#f0eee5")
p.text(sx + 24, 1162, "DIE STILLE WOCHE　La semaine calme", 24, "sans", True, OLIVE)  # F3 (2026-11-12): gloss restored to "La semaine calme" (was "La semaine"); wide box, no size change.
p.text(sx + 24, 1210, "BUß- UND BETTAG — 18. NOVEMBER", 21, "sans", True, OLIVE)
p.text(sx + 24 + (swd - 48) // 2, 1210, "TOTENSONNTAG — 22. NOVEMBER", 21, "sans", True, OLIVE)
pro = ["Evangelischer Tag zum Nachdenken und Beten.",
       "Feiertag nur in Sachsen; in Bayern kein Unterricht."]
contra = ["Evangelischer Gedenktag für die Verstorbenen.",
          "Weihnachtsmärkte in Köln bleiben geschlossen; danach beginnt die Adventszeit."]
pyy = 1232
for t in pro:
    pyy2 = p.para(sx + 24, pyy + 20, "· " + t, 20.5, "serif", False, INK, (swd - 72) // 2, 1.4)
    pyy = max(pyy, pyy2) + 8
pyy = 1232
for t in contra:
    pyy2 = p.para(sx + 24 + (swd - 48) // 2, pyy + 20, "· " + t, 20.5, "serif", False, INK, (swd - 72) // 2, 1.4)
    pyy = max(pyy, pyy2) + 8

# ---- practice chart (full width) ----
cy = 1420
p.hline(MX, RIGHT, cy - 12, OLIVE, 2)
p.text(MX, cy + 28, "WAS INTERESSIERT DIE LESER?　Qu'est-ce qui intéresse les lecteurs ?", 26, "sans", True, OLIVE)
bars = [("Bundesliga und Nations League", 44, "football"),
        ("Weihnachtsmärkte", 33, "marchés"),
        ("Stille Tage", 23, "calme")]
byy = cy + 58
for lab, v, zh in bars:
    p.text(MX, byy + 26, lab, 22, "serif", True, INK)
    p.text(MX + 360, byy + 26, zh, 20, "sans", False, GREY)
    p.rect(MX + 470, byy + 4, v * 17, 30, fill=OLIVE)
    p.text(MX + 470 + v * 17 + 16, byy + 26, f"{v} %", 22, "sans", True, OLIVE)
    byy += 52
p.text(MX, byy + 22, "ÜBUNGSDATEN　Données d'exercice — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Exemple de la rédaction, pas un vrai sondage.)", 19.5, "sans", False, GREY)

# ---- P6 exercises ----
ey = 1752
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Exercices page 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　Les niveaux se mélangent — cherchez par numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P6-ex")
e.head("A　DAS DIAGRAMM LESEN", 25, gap=6)
e.bridge("Regardez le graphique ci-dessus et choisissez la bonne réponse.", gap=6)
e.ex("B1", "choix multiple", "A", "44 % — le football mène",
     "Was interessiert die Leser am meisten (Übungsdaten)? A. Bundesliga und Nations League · B. Weihnachtsmärkte · C. Stille Tage", size=22, gap=6)
e.ex("B1", "choix multiple", "B", "Marchés : 33 %, 2es",
     "Was ist die zweitgrößte Gruppe? A. Stille Tage · B. Weihnachtsmärkte · C. Bundesliga", size=22, gap=6)
e.ex("B1", "choix multiple", "B", "44+33=77",
     "Fußball und Märkte zusammen sind... A. 67 % · B. 77 % · C. 100 %", size=22, gap=6)
e.ex("B2", "choix multiple", "B", "Jours calmes : 23 %, derniers",
     "Welche Gruppe ist kleiner? A. Märkte · B. Stille Tage · C. beide gleich", size=22, gap=6)
e.ex("B1", "choix multiple", "A", "Jours calmes 23 %",
     "Wie viele Prozent interessieren sich für die stillen Tage? A. 23 % · B. 33 % · C. 44 %", size=22, gap=6)
e.ex("B2", "choix multiple", "B", "44+33+23=100",
     "Die drei Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 %", size=22, gap=6)
e.head("B　LESEVERSTEHEN (B2)", 25, gap=6)
e.bridge("Lisez la page 6 et choisissez la bonne réponse.", gap=6)
e.ex("B2", "choix multiple", "B", "Jour de repentir et de prière, 18 nov.",
     "Wann ist Buß- und Bettag? A. 11. November · B. 18. November · C. 22. November", size=22, gap=6)
e.ex("B2", "choix multiple", "A", "Dernier dimanche liturgique",
     "Was ist der Totensonntag? A. der letzte Sonntag des Kirchenjahres · B. der erste Advent · C. ein Feiertag in ganz Deutschland", size=22, gap=6)
e.ex("B2", "choix multiple", "B", "Taxe électricité : 2,05 centimes",
     "Wie hoch ist die Stromsteuer für Haushalte? A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent", size=22, gap=6)
e.ex("B1", "choix multiple", "B", "Budget 2027 : 27 novembre",
     "Wann soll der Bundeshaushalt 2027 verabschiedet werden? A. am 18. November · B. am 27. November · C. am 22. November", size=22, gap=6)
e.head("C　GRAMMATIK", 25, gap=6)
e.bridge("Complétez avec la forme entre parenthèses.", gap=6)
e.ex("B2", "à compléter", "wird", "passif : wird + Part. II",
     "Der Bundeshaushalt ___ (werden) am 27. November verabschiedet.", instr="Complétez", size=22, gap=6)
e.ex("B2", "à compléter", "ob", "ob : question indirecte",
     "Niemand weiß, ___ die Einigung gelingt.", instr="Complétez", size=22, gap=6)
e.ex("B1", "à compléter", "geht", "gehen → geht",
     "Die Debatte ___ (gehen) weiter.", instr="Complétez", size=22, gap=6)
e.ex("B2", "à compléter", "beginnt", "beginnen → beginnt",
     "Mit dem ersten Advent ___ (beginnen) ein neues Kirchenjahr.", instr="Complétez", size=22, gap=6)
e.head("D　WÖRTER DER DEBATTE", 25, gap=6)
e.bridge("Complétez avec les mots de l'encadré.", gap=6)
e.para("Buße · Kirchenjahr · Friedhof · Einigung", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "à compléter", "Buße", "repentir",
     "Der Buß- und Bettag lädt zur ___ ein.", instr="Complétez", size=22, gap=6)
e.ex("B2", "à compléter", "Kirchenjahr", "année liturgique",
     "Der Totensonntag ist der letzte Sonntag des ___s.", instr="Complétez", size=22, gap=6)
e.ex("B2", "à compléter", "Friedhof", "cimetière",
     "Die Menschen gehen auf den ___ und zünden Kerzen an.", instr="Complétez", size=22, gap=6)
e.ex("B1", "à compléter", "Einigung", "accord",
     "Ob eine ___ gelingt, ist offen.", instr="Complétez", size=22, gap=6)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-vertiefung.svg")
print("P6 saved, exercises so far:", len(REG))
