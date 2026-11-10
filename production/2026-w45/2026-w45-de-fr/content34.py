# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("KULTUR　Culture", "Die Lucerna", "A2 → B1　Ferienwechsel & Herbst　Changement de vacances et automne")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Ferienwechsel: Die einen kommen, die anderen gehen", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: A2 → B1")
f.para("In dieser Woche wechseln die Ferien: In Baden-Württemberg ist die Schule schon wieder losgegangen — die Herbstferien dort sind vorbei. In Bayern dagegen haben die Schülerinnen und Schüler noch frei: Dort dauern die Herbstferien in dieser Woche noch an.")
f.para("Was macht man im November? Der Herbst zeigt seine ruhige Seite: Man liest, man kocht Kürbissuppe, man geht spazieren — und man plant schon den Advent. Die Tage sind kurz, die Abende lang. Viele Familien nutzen die freie Zeit für Ausflüge in die Berge oder an einen See — bevor der Winter kommt.")
f.para("Rückblick: Am Samstag, dem 31. Oktober, war Halloween — und zugleich Reformationstag in neun Bundesländern. Ebenfalls am 31. Oktober spielte Bayern in Dortmund — der Klassiker. Einen Tag später, am Sonntag, dem 1. November, war Allerheiligen: ein Feiertag in Baden-Württemberg, Bayern, Nordrhein-Westfalen, Rheinland-Pfalz und dem Saarland. Die Geschäfte blieben geschlossen, viele Menschen besuchten die Gräber ihrer Angehörigen.")
f.para("Und die Kultur? Die Museen und Theater spielen ihr Herbstprogramm. Ein Tipp der Redaktion: Gehen Sie an einem grauen Nachmittag ins Museum — dort ist es warm, ruhig und hell. Und wer ein Buch sucht: Die Bibliotheken haben im November oft Lesungen und Büchertische zum Herbst.")
f.para("Auch der Fußball gehört zum Herbst: Am Samstag und Sonntag spielt die Bundesliga — für viele Familien der Ausflug des Wochenendes. Mehr dazu auf Seite 4.")
f.para("Für Kinder gibt es in dieser Woche noch ein Highlight: Die Laternen für St. Martin werden schon gebastelt — der 11. November kommt bald. Mehr dazu in der nächsten Ausgabe.")
f.gloss("der Ferienwechsel = changement de vacances · die Schülerin = élève · der Ausflug = excursion · der Advent = Avent · die Lesung = lecture.")
f.end_report()

# col 3: facts + vocab + Und Sie + Tipp (hand-rolled; CORRECTED height formula — see KIT §geometry)
ix = COLX[3]
facts = ["Baden-Württemberg ist seit Montag, dem 2. November, wieder in der Schule.",
         "Bayern hat in dieser Woche noch Herbstferien — als einziges Bundesland.",
         "Allerheiligen am 1. November ist ein stiller Feiertag: Die Geschäfte bleiben zu."]
sy3 = 200
sh = 45 + 33 * len(facts) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in facts)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "FERIENWECHSEL　Vacances", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 facts ends", sy3 + sh)
words = ["der Nebel — brouillard", "das Laub — feuillage", "der Kürbis — citrouille",
         "die Kerze — bougie", "der Spaziergang — promenade", "die Lesung — lecture"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "HERBSTWÖRTER　Automne", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Lesen Sie im Herbst mehr als im Sommer? Welches Buch liegt gerade auf Ihrem Nachttisch? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("Lisez-vous plus en automne ? Votre livre de chevet ? Écrivez en allemand !", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　Et vous ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Lisez-vous plus en automne ? Votre livre de chevet ? Écrivez en allemand !", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 undsie ends", ey3 + eh)
tipp = "Tipp: An einem grauen Nachmittag ins Museum — dort ist es warm."
sy3 = ey3 + eh + 26
sh = 45 + 33 + 30.53 * len(wrap(tipp, "serif", False, 21.5, CW - 44))
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DER TIPP　Conseil de la rédaction", 24, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, tipp, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Exercices de la page 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　Les niveaux se mélangent — retrouvez chaque réponse par son numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P3-ex")
e.head("A　RICHTIG ODER FALSCH?", 25)
e.bridge("Lisez l'article de la page 3. Vrai ou faux ?")
e.ex("A2", "vrai/faux", "Richtig", "Bade-Wurtemberg reprend lundi",
     "In Baden-Württemberg sind die Herbstferien vorbei. Richtig oder falsch?", instr="Vrai ou faux ?", size=20, gap=8)
e.ex("A2", "vrai/faux", "Falsch", "la Bavière est encore en vacances cette semaine",
     "Bayern hat in dieser Woche keine Ferien mehr. Richtig oder falsch?", instr="Vrai ou faux ?", size=20, gap=8)
e.ex("A2", "vrai/faux", "Richtig", "Toussaint le 1er novembre",
     "Allerheiligen ist am 1. November. Richtig oder falsch?", instr="Vrai ou faux ?", size=20, gap=8)
e.ex("B1", "vrai/faux", "Falsch", "le 31 octobre est aussi le jour de la Réforme (neuf Länder)",
     "Am 31. Oktober war nur Halloween, kein Feiertag. Richtig oder falsch?", instr="Vrai ou faux ?", size=20, gap=8)
e.ex("A2", "vrai/faux", "Falsch", "magasins fermés à la Toussaint",
     "Die Geschäfte sind an Allerheiligen geöffnet. Richtig oder falsch?", instr="Vrai ou faux ?", size=20, gap=8)
e.head("B　WÖRTER AUS DEM TEXT", 25)
e.bridge("Complétez avec les mots de l'encadré.")
e.para("Ferienwechsel · Ausflug · Lesung · Advent · Nebel", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "à compléter", "Ferienwechsel", "changement de vacances",
     "In dieser Woche ist ___: Die einen kommen, die anderen gehen.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Ausflug", "une excursion à la montagne",
     "Viele Familien machen einen ___ in die Berge.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Lesung", "une lecture à la bibliothèque",
     "In der Bibliothek gibt es eine ___ zum Herbst.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Advent", "l'Avent préparé en novembre",
     "Im November plant man schon den ___.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Nebel", "brouillard sur le lac",
     "Am Morgen liegt ___ über dem See.", instr="Compléter", size=20, gap=8)
e.head("C　LESEVERSTEHEN", 25)
e.bridge("Choisissez la bonne réponse.")
e.ex("A2", "QCM", "B", "vacances finies en Bade-Wurtemberg",
     "Wo sind die Ferien schon vorbei? A. in Bayern · B. in Baden-Württemberg · C. in Berlin", size=20, gap=8)
e.ex("A2", "QCM", "B", "une fête calme",
     "Was ist Allerheiligen? A. ein lautes Fest · B. ein stiller Feiertag · C. ein Schultag", size=20, gap=8)
e.ex("A2", "QCM", "A", "visite des tombes à la Toussaint",
     "Was machen viele an Allerheiligen? A. Sie besuchen Gräber. · B. Sie gehen in die Schule. · C. Sie kaufen Kostüme.", size=20, gap=8)
e.ex("B1", "QCM", "A", "jours courts, donc longues soirées",
     "Warum sind die Abende lang? A. Die Tage sind kurz. · B. Die Uhren gehen vor. · C. Die Ferien sind lang.", size=20, gap=8)
e.head("D　SÄTZE BAUEN", 25)
e.bridge("Mettez les mots dans le bon ordre.")
e.ex("A2", "construction de phrase", "In Baden-Württemberg ist die Schule wieder losgegangen.", "temps et lieu en tête, verbe en deuxième position",
     "in Baden-Württemberg / ist / die Schule / wieder losgegangen → ___", instr="Former une phrase", size=20, gap=8)
e.ex("B1", "construction de phrase", "Bayern hat in dieser Woche noch Ferien.", "complément de temps en tête, verbe en deuxième position",
     "Bayern / hat / in dieser Woche / noch Ferien → ___", instr="Former une phrase", size=20, gap=8)
e.ex("A2", "construction de phrase", "Viele Familien machen einen Ausflug in die Berge.", "ordre sujet–verbe–complément",
     "viele Familien / machen / einen Ausflug / in die Berge → ___", instr="Former une phrase", size=20, gap=8)
e.ex("B1", "construction de phrase", "An Allerheiligen bleiben die Geschäfte geschlossen.", "bleiben + geschlossen",
     "an Allerheiligen / bleiben / die Geschäfte / geschlossen → ___", instr="Former une phrase", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-kultur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　Sport", "Die Lucerna", "LEVEL B1　Europapokal & Bundesliga　Coupes d'Europe et Bundesliga")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Englische Woche: Vier Nächte, dann der Spieltag", 32)
f.byline("Von der Lucerna-Sportredaktion　Leseniveau: B1")
f.para("Was für eine Fußballwoche! Am Dienstag und Mittwoch spielt die Champions League, am Donnerstag die Europa League — und am Freitag beginnt schon der 9. Spieltag der Bundesliga. Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.")
f.para("Am Dienstagabend wird es ernst: Bayern München spielt um 21.00 Uhr bei Atlético Madrid. Schon um 18.45 Uhr spielt der VfB Stuttgart bei Galatasaray in Istanbul. Zwei schwere Auswärtsspiele für die deutschen Teams.")
f.para("Am Mittwochabend (21.00 Uhr) geht es weiter: Borussia Dortmund empfängt Real Betis Sevilla, und RB Leipzig spielt gegen Manchester City. Für Leipzig ist es das schwerste Spiel der Woche: City ist der Favorit — aber zu Hause ist alles möglich.")
f.para("Am Donnerstagabend (18.45 Uhr) spielt die TSG Hoffenheim in der Europa League bei Crystal Palace in London. Auch Bayer Leverkusen ist in Europa dabei: Die Werkself spielt um 21.00 Uhr gegen Marseille.")
f.para("Und dann die Bundesliga: Am Freitag (20.30 Uhr) eröffnen Hamburg und Mönchengladbach den 9. Spieltag. Am Samstag folgen fünf Spiele, das Topspiel ist Stuttgart gegen Bremen (18.30 Uhr). Am Sonntag: Köln–Leverkusen (15.30 Uhr), Freiburg–Union Berlin (17.30 Uhr) und Hoffenheim–Schalke (19.30 Uhr).")
f.para("Merken Sie sich auch den nächsten Sonntag: Am 15. November spielt die NFL in München — American Football in der Allianz Arena! Mehr dazu in der nächsten Ausgabe.")
f.gloss("die Englische Woche = semaine anglaise · auswärts = à l'extérieur · empfangen = recevoir · der Favorit = favori · eröffnen = ouvrir.")
f.end_report()

# col 3: kopfball image + Und Sie
bx = COLX[3]
image(p, "kopfball.jpg", bx, 200, CW, 470)
cy3 = caption(p, bx, 670, CW, "Kopfball im Spiel: So sieht ein Duell in der Luft aus — um jeden Ball wird gekämpft.",
              "Foto: DVIDS (Armed Forces Soccer Championship, Destin, Florida, 2010) — public domain")
ey3 = cy3 + 26
etvous = "Und Sie? Für wen sind Sie in dieser Woche — Bayern, Dortmund, Leipzig oder Stuttgart? Und wer gewinnt am Samstag das Topspiel? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("Qui soutenez-vous ? Qui gagne samedi ? Écrivez deux phrases en allemand !", "sans", False, 20, CW - 44)) - 1)
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "UND SIE?　Et vous ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Qui soutenez-vous ? Qui gagne samedi ? Écrivez deux phrases en allemand !", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "DER 9. SPIELTAG　Les matches de la 9e journée", 26, "sans", True, OLIVE)
rows = [
    ("Fr 6.11.", "20.30", "Hamburger SV – Borussia Mönchengladbach"),
    ("Sa 7.11.", "15.30", "Borussia Dortmund – SV Elversberg · SC Paderborn 07 – Eintracht Frankfurt"),
    ("Sa 7.11.", "15.30", "1. FSV Mainz 05 – FC Bayern München · RB Leipzig – FC Augsburg"),
    ("Sa 7.11.", "18.30", "VfB Stuttgart – Werder Bremen (Topspiel)"),
    ("Sa 7.11.", "20.30", "Hertha BSC – VfL Wolfsburg (2. Bundesliga)"),
    ("So 8.11.", "15.30", "1. FC Köln – Bayer 04 Leverkusen"),
    ("So 8.11.", "17.30", "SC Freiburg – 1. FC Union Berlin"),
    ("So 8.11.", "19.30", "TSG Hoffenheim – FC Schalke 04"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Alle Zeiten in MEZ (Mitteleuropäische Zeit). Die Europa-Spiele: Dienstag bis Donnerstag, die Liga: Freitag bis Sonntag. Die Hertha-Zeile ist 2. Bundesliga."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1640
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Exercices de la page 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　Les niveaux se mélangent — retrouvez chaque réponse par son numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P4-ex")
e.head("A　LESEVERSTEHEN", 25)
e.bridge("Lisez l'article de la page 4 et choisissez la bonne réponse.")
e.ex("B1", "QCM", "B", "Bayern à l'Atlético mardi",
     "Bayern spielt am Dienstag... A. zu Hause gegen Atlético · B. bei Atlético Madrid · C. bei Galatasaray", size=20, gap=8)
e.ex("B1", "QCM", "B", "Stuttgart : coup d'envoi à 18 h 45",
     "Stuttgart spielt am Dienstag um... A. 21.00 Uhr · B. 18.45 Uhr · C. 20.30 Uhr", size=20, gap=8)
e.ex("B1", "QCM", "C", "Dortmund reçoit le Betis",
     "Dortmund empfängt am Mittwoch... A. Manchester City · B. Marseille · C. Real Betis Sevilla", size=20, gap=8)
e.ex("B1", "QCM", "A", "Hoffenheim à Crystal Palace en Ligue Europa",
     "Hoffenheim spielt in der Europa League bei... A. Crystal Palace · B. Galatasaray · C. Real Betis", size=20, gap=8)
e.ex("B1", "QCM", "B", "le grand match de samedi : Stuttgart–Brême",
     "Das Topspiel am Samstag ist... A. Hamburg–Gladbach · B. Stuttgart–Bremen · C. Köln–Leverkusen", size=20, gap=8)
e.head("B　DIE WÖRTER", 25)
e.match_set("B1", "appariement",
            ["die Englische Woche", "auswärts", "der Favorit", "eröffnen"],
            ["eine Woche mit Spielen unter der Woche und am Wochenende",
             "nicht zu Hause, sondern beim Gegner",
             "das Team, das wahrscheinlich gewinnt",
             "den Anfang machen, ein Spiel beginnen"],
            ["a", "b", "c", "d"],
            ["Englische Woche = semaine anglaise a", "auswärts = à l'extérieur b", "Favorit = favori c", "eröffnen = ouvrir d"],
            instr="Relier les paires")
e.head("C　KOMPARATIV", 25)
e.bridge("Complétez au comparatif (le mot entre parenthèses est au positif).")
e.ex("B1", "à compléter", "schwerer", "schwer → schwerer",
     "Für Leipzig wird der Abend gegen City ___ (schwer) als normal.", instr="Compléter", size=20, gap=8)
e.ex("B1", "à compléter", "später", "spät → später (19 h 30, le plus tard)",
     "Das Sonntagsspiel Hoffenheim–Schalke beginnt ___ (spät) als die anderen.", instr="Compléter", size=20, gap=8)
e.ex("B1", "à compléter", "mehr", "viel → mehr (les supporters en veulent plus)",
     "Die Fans wollen ___ (viel) Tore sehen.", instr="Compléter", size=20, gap=8)
e.ex("B1", "à compléter", "früher", "früh → früher (18 h 45, c'est plus tôt que 21 h 00)",
     "Stuttgart spielt schon um 18.45 Uhr — ___ (früh) als das Bayern-Spiel.", instr="Compléter", size=20, gap=8)
e.head("D　DIE UHRZEITEN", 25)
e.bridge("Regardez le tableau des matches ci-dessus et choisissez la bonne réponse.")
e.ex("B1", "QCM", "A", "Hambourg–Gladbach vendredi 20 h 30",
     "Das Spiel Hamburg–Gladbach beginnt um... A. 20.30 Uhr · B. 18.30 Uhr · C. 15.30 Uhr", size=20, gap=8)
e.ex("B1", "QCM", "B", "Stuttgart–Brême samedi 18 h 30",
     "Stuttgart–Bremen ist das Topspiel am Samstag um... A. 15.30 Uhr · B. 18.30 Uhr · C. 20.30 Uhr", size=20, gap=8)
e.ex("B1", "QCM", "C", "Hoffenheim–Schalke dimanche 19 h 30",
     "Hoffenheim–Schalke beginnt am Sonntag um... A. 15.30 Uhr · B. 17.30 Uhr · C. 19.30 Uhr", size=20, gap=8)
e.ex("B1", "QCM", "A", "Fribourg–Union dimanche 17 h 30",
     "Freiburg–Union beginnt um... A. 17.30 Uhr · B. 19.30 Uhr · C. 15.30 Uhr", size=20, gap=8)
e.ex("B1", "QCM", "B", "Ligue Europa jeudi, Hoffenheim à 18 h 45",
     "Die Europa League am Donnerstag: Hoffenheim spielt um... A. 21.00 Uhr · B. 18.45 Uhr · C. 20.30 Uhr", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
