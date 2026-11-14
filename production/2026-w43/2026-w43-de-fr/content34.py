# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("KULTUR　Culture", "Die Lucerna", "A2 → B1　Zwei Feste an einem Tag　Deux fêtes le même jour")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Zwei Feste an einem Tag: Halloween trifft den Reformationstag", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: A2 → B1")
f.para("Am Samstag, dem 31. Oktober, ist in Deutschland viel los: Zwei Feste fallen auf denselben Tag. Die Kinder feiern Halloween — und neun Bundesländer haben einen Feiertag: den Reformationstag.")
f.para("Was ist Halloween? Kinder ziehen Kostüme an und gehen am Abend von Haus zu Haus. Sie rufen: „Süßes oder Saures!“ und bekommen Süßigkeiten. In den Fenstern leuchten Kürbisse mit Gesichtern, und in vielen Straßen stehen Kerzen und kleine Lichter. Die Geschäfte sind schon bereit: Die Discounter verkaufen seit dem 12. Oktober Kostüme und Dekoration.")
f.para("Und der Reformationstag? An diesem Tag im Jahr 1517 soll Martin Luther seine 95 Thesen an die Tür der Schlosskirche in Wittenberg genagelt haben. Damit begann die Reformation — die Kirche teilte sich, und Europa veränderte sich. Heute ist der Tag ein gesetzlicher Feiertag in Brandenburg, Bremen, Hamburg, Mecklenburg-Vorpommern, Niedersachsen, Sachsen, Sachsen-Anhalt, Schleswig-Holstein und Thüringen.")
f.para("In diesem Jahr fällt der 31. Oktober auf einen Samstag — ein Extra-Freitag entsteht so nicht. Einen Tag später, am Sonntag, dem 1. November, ist Allerheiligen: ein Feiertag in Baden-Württemberg, Bayern, Nordrhein-Westfalen, Rheinland-Pfalz und dem Saarland. Dort bleiben die Geschäfte auch am Sonntag geschlossen — wie jeden Sonntag.")
f.para("Halloween im Zoo? In Osnabrück gibt es in diesem Jahr eine schöne Aktion: Wer vom 26. bis 29. Oktober einen geschnitzten Kürbis abgibt, bekommt für den 31. Oktober ein Freiticket für ein Kind. Die Kürbisse werden Dekoration rund um den Unterirdischen Zoo. Im Erlebnispark Funny-World in Kappel-Grafenhausen leuchten am 30. und 31. Oktober mehr als 600 Kürbisse.")
f.para("Zwei Feste, ein Tag — und eine Frage für unsere Leser: Feiern die Deutschen am 31. Oktober lieber leise oder lieber laut? Schreiben Sie uns! Die Redaktion sammelt die Antworten für die nächste Ausgabe.")
f.gloss("das Kostüm = le déguisement · der Kürbis = la citrouille · der Feiertag = le jour férié · die These = la thèse · gesetzlich = légal · das Freiticket = le billet gratuit · schnitzen = sculpter.")
f.end_report()

# col 3: Luther image + facts (sequential)
ix = COLX[3]
image(p, "luther.jpg", ix, 200, CW, 470)
cy3 = caption(p, ix, 670, CW, "Martin Luther (1483–1546), gemalt von Lucas Cranach dem Älteren, 1528. Seine 95 Thesen von 1517 veränderten Europa.",
              "Gemälde: Lucas Cranach d. Ä., 1528 (Veste Coburg) — public domain")
facts = ["Der 31. Oktober ist in neun Bundesländern ein Feiertag — 2026 fällt er auf einen Samstag.",
         "Allerheiligen am 1. November ist ein stiller Feiertag: keine lauten Feste, die Geschäfte bleiben zu.",
         "Mehr als 600 geschnitzte Kürbisse leuchten in Funny-World (Kappel-Grafenhausen)."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 34  # D5 fix run2
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ZWEI FESTE, EIN TAG", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "Und Sie? Verkleiden Sie sich an Halloween? Oder ist der 31. Oktober für Sie ein ruhiger Tag? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Vous vous déguisez pour Halloween ? Ou le 31 octobre est-il un jour calme pour vous ? Écrivez deux phrases en allemand !", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　À vous", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Vous vous déguisez pour Halloween ? Ou le 31 octobre est-il un jour calme pour vous ? Écrivez deux phrases en allemand !", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Exercices de la page 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　Les niveaux se mélangent — chaque réponse par son numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P3-ex")
e.head("A　RICHTIG ODER FALSCH?", 25)
e.expl("Lisez l'article page 3. Vrai ou faux ?")
e.ex("A2", "vrai/faux", "Richtig", "neuf Länder ont la Fête de la Réforme comme jour férié",
     "Der Reformationstag ist in neun Bundesländern ein Feiertag. Richtig oder falsch?", instr="Vrai ou faux ?", size=20, gap=8)
e.ex("A2", "vrai/faux", "Falsch", "Luther : c'était en 1517, pas en 1715",
     "Martin Luther nagelte seine Thesen im Jahr 1715 an die Tür. Richtig oder falsch?", instr="Vrai ou faux ?", size=20, gap=8)
e.ex("A2", "vrai/faux", "Richtig", "une citrouille déposée du 26 au 29 octobre donne un billet enfant pour le 31",
     "Im Zoo Osnabrück gibt es für einen Kürbis ein Freiticket für ein Kind. Richtig oder falsch?", instr="Vrai ou faux ?", size=20, gap=8)
e.ex("B1", "vrai/faux", "Falsch", "le 31 octobre tombe un samedi cette année — pas de jour libre en semaine en plus",
     "Der 31. Oktober gibt den Menschen in diesem Jahr einen freien Freitag. Richtig oder falsch?", instr="Vrai ou faux ?", size=20, gap=8)
e.ex("A2", "vrai/faux", "Richtig", "plus de 600 citrouilles à Funny-World",
     "In Funny-World leuchten mehr als 600 Kürbisse. Richtig oder falsch?", instr="Vrai ou faux ?", size=20, gap=8)
e.head("B　WÖRTER AUS DEM TEXT", 25)
e.expl("Complétez avec les mots du cadre.")
e.para("Kostüm · Kürbis · Feiertag · Süßes · Kerze", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "à compléter", "Kostüm", "les enfants enfilent un Kostüm (déguisement)",
     "Die Kinder ziehen ein ___ an und gehen von Haus zu Haus.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Kürbis", "une lanterne en Kürbis (citrouille)",
     "Im Fenster leuchtet ein ___ mit einem Gesicht.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Feiertag", "Feiertag = jour férié",
     "Der Reformationstag ist ein gesetzlicher ___.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Süßes", "Süßes oder Saures!",
     "Die Kinder rufen an der Tür: „___ oder Saures!“", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Kerzen", "Kerzen = des bougies (pluriel)",
     "In vielen Straßen stehen ___ und kleine Lichter.", instr="Compléter", size=20, gap=8)
e.head("C　LESEVERSTEHEN", 25)
e.expl("Choisissez la bonne réponse.")
e.ex("A2", "QCM", "B", "les enfants vont de maison en maison le soir",
     "Wann gehen die Kinder von Haus zu Haus? A. am Morgen · B. am Abend · C. in der Nacht um drei", size=20, gap=8)
e.ex("A2", "QCM", "A", "en 1517, à la porte de l'église du château",
     "Luthers Thesen hingen 1517 an der Tür... A. der Schlosskirche · B. des Rathauses · C. der Schule", size=20, gap=8)
e.ex("B1", "QCM", "B", "la Toussaint est le 1er novembre",
     "Allerheiligen ist am... A. 31. Oktober · B. 1. November · C. 2. November", size=20, gap=8)
e.ex("B1", "QCM", "B", "les citrouilles décorent les abords du zoo souterrain",
     "Wo stehen die Kürbisse dann im Zoo? A. Im Restaurant. · B. Rund um den Unterirdischen Zoo. · C. Am Eingang.", size=20, gap=8)
e.head("D　SÄTZE BAUEN", 25)
e.expl("Mettez les mots dans le bon ordre pour former une phrase.")
e.ex("A2", "construction de phrase", "Die Kinder rufen an der Tür: Süßes oder Saures!", "sujet + verbe en deuxième position",
     "die Kinder / rufen / an der Tür / Süßes oder Saures → ___", instr="Former une phrase", size=20, gap=8)
e.ex("B1", "construction de phrase", "Neun Bundesländer haben am 31. Oktober einen Feiertag.", "on commence par le nombre ; le verbe reste en deuxième position",
     "neun Bundesländer / haben / am 31. Oktober / einen Feiertag → ___", instr="Former une phrase", size=20, gap=8)
e.ex("A2", "à compléter", "bekommen die Kinder Süßigkeiten", "bekommen = recevoir (les enfants reçoivent des bonbons)",
     "Die Kinder bekommen an Halloween Süßigkeiten. → An Halloween ___.", instr="Réécrire", size=20, gap=8)
e.ex("B1", "construction de phrase", "Die Geschäfte bleiben am Sonntag geschlossen.", "bleiben + geschlossen",
     "die Geschäfte / bleiben / am Sonntag / geschlossen → ___", instr="Former une phrase", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-kultur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　Sport", "Die Lucerna", "LEVEL B1　Champions League & Bundesliga　La Ligue des champions et la Bundesliga")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Königsklasse in der Woche der zwei Zeiten", 32)
f.byline("Von der Lucerna-Sportredaktion　Leseniveau: B1")
f.para("Was für eine Fußballwoche! Am Dienstag und Mittwoch spielt die Champions League ihren 3. Spieltag, am Freitag beginnt die Bundesliga — und am Sonntag wechselt mittendrin die Zeit: Die Liga spielt zum ersten Mal in dieser Saison in der Winterzeit.")
f.para("Der Dienstag brachte zwei deutsche Spiele. Borussia Dortmund gewann am Dienstagabend 2:1 bei Sabah FK in Baku. Der BVB nahm die drei Punkte mit nach Hause. Der VfB Stuttgart spielte zu Hause 1:1 gegen Atlético Madrid: Julián Álvarez machte den Ausgleich für die Spanier — ein Punkt für den VfB.")
f.para("Heute Abend (Anstoß 21.00 Uhr) wird es noch größer: Der FC Bayern empfängt den FC Arsenal, und RB Leipzig spielt bei Real Madrid. Für Leipzig ist es ein schwerer Abend: Am Wochenende verlor die Mannschaft in der Liga 1:6 bei den Bayern. In Madrid muss Leipzig mutiger spielen. Ob das gegen Real reicht? Die Antwort gibt es heute Nacht.")
f.para("Am Freitag um 20.30 Uhr beginnt der 7. Spieltag der Bundesliga: Stuttgart spielt gegen Mönchengladbach — noch in der Sommerzeit (MESZ). Am Samstag folgen fünf Spiele am Nachmittag; das Topspiel am Abend ist Borussia Dortmund gegen Eintracht Frankfurt um 18.30 Uhr. Und am Sonntag spielt die Liga dann in der neuen Zeit (MEZ): Hoffenheim gegen Leverkusen um 15.30 Uhr, Freiburg gegen die Bayern um 17.30 Uhr.")
f.para("Merken Sie sich auch den nächsten Samstag: Am 31. Oktober spielen die Bayern in Dortmund — der Klassiker! Mehr dazu in der nächsten Ausgabe.")
f.gloss("die Königsklasse = la « classe royale », le surnom de la Ligue des champions · der Spieltag = la journée de championnat · der Anstoß = le coup d'envoi · der Ausgleich = l'égalisation · empfangen = recevoir (jouer à domicile) · mutig = courageux.")
f.end_report()

# col 3: Klassiker box + Und Sie (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 330, fill=BOX)
p.text(bx + 22, 240, "DER KLASSIKER RUFT", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Am Samstag, dem 31. Oktober, spielen die Bayern bei Borussia Dortmund — das größte Spiel der Hinrunde. Halloween, Feiertag und der Klassiker an einem Tag: Die nächste Ausgabe wird voll! (Seite 7)", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 556
etvous = "Und Sie? Für wen sind Sie am Wochenende — Bayern, Dortmund oder Leipzig? Und wer gewinnt den Klassiker am 31. Oktober? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Vous supportez qui, ce week-end — le Bayern, Dortmund ou Leipzig ? Et qui gagne le Klassiker le 31 octobre ? Écrivez deux phrases en allemand !", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "UND SIE?　À vous", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Vous supportez qui, ce week-end — le Bayern, Dortmund ou Leipzig ? Et qui gagne le Klassiker le 31 octobre ? Écrivez deux phrases en allemand !", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "DER 7. SPIELTAG　La 7e journée", 26, "sans", True, OLIVE)
rows = [
    ("Fr 23.10.", "20.30 (MESZ)", "VfB Stuttgart – Borussia Mönchengladbach"),
    ("Sa 24.10.", "18.30 (MESZ)", "Borussia Dortmund – Eintracht Frankfurt (Topspiel)"),
    ("Sa 24.10.", "nachmittags", "1. FC Köln – FC Schalke 04 · FC Augsburg – 1. FC Union Berlin"),
    ("Sa 24.10.", "nachmittags", "1. FSV Mainz 05 – Werder Bremen · RB Leipzig – SV Elversberg"),
    ("Sa 24.10.", "nachmittags", "SC Paderborn 07 – Hamburger SV"),
    ("So 25.10.", "15.30 (MEZ)", "TSG Hoffenheim – Bayer 04 Leverkusen"),
    ("So 25.10.", "17.30 (MEZ)", "SC Freiburg – FC Bayern München"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Achtung, Zeit-Fans: Am Freitag und Samstag gilt noch die Sommerzeit (MESZ), am Sonntag schon die Winterzeit (MEZ) — die Uhren wurden in der Nacht umgestellt."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Exercices de la page 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　Les niveaux se mélangent — chaque réponse par son numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P4-ex")
e.head("A　LESEVERSTEHEN", 25)
e.expl("Lisez l'article page 4 et choisissez la bonne réponse.")
e.ex("B1", "QCM", "A", "Dortmund gagne 2:1 à l'extérieur contre Sabah",
     "Dortmund spielte am Dienstag... A. 2:1 in Baku · B. 1:1 zu Hause · C. 0:2 in Madrid", size=20, gap=8)
e.ex("B1", "QCM", "B", "Álvarez égalise pour l'Atlético",
     "Wer traf für Atlético zum Ausgleich? A. ein Stuttgarter · B. Julián Álvarez · C. ein Torwart", size=20, gap=8)
e.ex("B1", "QCM", "C", "Leipzig a perdu 1:6 contre le Bayern en championnat",
     "Leipzig verlor am Wochenende... A. 0:1 · B. 2:2 · C. 1:6 bei den Bayern", size=20, gap=8)
e.ex("B1", "QCM", "A", "la journée commence vendredi à 20 h 30 avec Stuttgart–Gladbach",
     "Der Spieltag beginnt am Freitag mit... A. Stuttgart–Gladbach · B. Dortmund–Frankfurt · C. Freiburg–Bayern", size=20, gap=8)
e.ex("B1", "QCM", "B", "dimanche, l'heure d'hiver (MEZ) s'applique déjà",
     "Am Sonntag gilt schon die... A. Sommerzeit · B. Winterzeit · C. Frühlingszeit", size=20, gap=8)
e.head("B　DIE WÖRTER", 25)
e.match_set("B1", "appariement",
            ["der Ausgleich", "der Spieltag", "der Anstoß", "die Königsklasse"],
            ["der Moment, in dem ein Spiel beginnt",
             "das Tor zum gleichen Stand, zum Beispiel 1:1",
             "ein Tag, an dem alle Teams spielen",
             "der Spitzname der Champions League"],
            ["b", "c", "a", "d"],
            ["Ausgleich = l'égalisation, b", "Spieltag = la journée, c", "Anstoß = le coup d'envoi, a", "Königsklasse = le surnom de la Ligue des champions, d"],
            instr="Relier les paires")
e.head("C　KOMPARATIV", 25)
e.expl("Complétez avec le comparatif (le mot entre parenthèses est la forme de base).")
e.ex("B1", "à compléter", "größer", "groß → größer (la plus grande nuit de la semaine)",
     "Der Mittwoch ist noch ___ (groß) als der Dienstag: Bayern gegen Arsenal!", instr="Compléter", size=20, gap=8)
e.ex("B1", "à compléter", "schwerer", "schwer → schwerer",
     "Für Leipzig wird der Abend in Madrid ___ (schwer) als normal.", instr="Compléter", size=20, gap=8)
e.ex("B1", "à compléter", "später", "spät → später (le coup d'envoi de vendredi, 20 h 30, est le plus tardif)",
     "Das Freitagsspiel beginnt ___ (spät) als die Sonntagsspiele.", instr="Compléter", size=20, gap=8)
e.ex("B1", "à compléter", "mehr", "viel → mehr (les supporters en veulent plus)",
     "Die Fans wollen ___ (viel) Tore sehen.", instr="Compléter", size=20, gap=8)
e.head("D　DAS PRÄTERITUM", 25)
e.expl("Mettez les phrases au Präteritum (passé simple).")
e.ex("B1", "transformation", "Dortmund gewann 2:1 in Baku.", "gewinnen → gewann",
     "Dortmund gewinnt 2:1 in Baku. → ___", instr="Réécrire", size=20, gap=8)
e.ex("B1", "transformation", "Álvarez machte den Ausgleich.", "machen → machte",
     "Álvarez macht den Ausgleich. → ___", instr="Réécrire", size=20, gap=8)
e.ex("B1", "transformation", "Stuttgart spielte 1:1 gegen Atlético.", "spielen → spielte",
     "Stuttgart spielt 1:1 gegen Atlético. → ___", instr="Réécrire", size=20, gap=8)
e.ex("B1", "transformation", "Leipzig verlor 1:6 bei den Bayern.", "verlieren → verlor",
     "Leipzig verliert 1:6 bei den Bayern. → ___", instr="Réécrire", size=20, gap=8)
e.ex("B1", "transformation", "Die Fans waren nervös.", "sein → waren (pluriel)",
     "Die Fans sind nervös. → ___", instr="Réécrire", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
