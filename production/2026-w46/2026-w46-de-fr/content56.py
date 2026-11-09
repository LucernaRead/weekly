# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUGEND　Jeunesse", "Die Lucerna", "LEVEL B1　Laternen, Lieder & Schule　Lanternes, chansons et école")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P5-main")
f.title("Laternen basteln, Lieder singen: Die Woche der Kinder", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: B1")
f.para("Am Montag, dem 9. November, sind alle wieder in der Schule: Auch in Bayern sind die Herbstferien jetzt vorbei. Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut. Und in vielen Klassen wird schon gebastelt: Laternen für St. Martin.")
f.para("Was basteln die Kinder? Bunte Laternen aus Papier, mit Sternen, Monden und Tieren. In der Kita und in der Schule singen sie Martinslieder und üben den Umzug. Am Mittwochabend ziehen sie dann mit ihren Laternen durch die Straßen — vorneweg der heilige Martin auf dem Pferd.")
f.para("Und in Köln? Dort beginnt am Mittwoch um 11.11 Uhr die Karnevalssession. Auch Kinder verkleiden sich: als Prinzessin, als Pirat, als Tier. Aber Vorsicht: Am Vormittag ist Karneval, am Abend ist St. Martin — zwei Feste, zwei Stimmungen, ein Tag.")
f.para("Was macht man nach der Schule im dunklen November? Lesen, was man im Herbst begonnen hat, oder ein neues Hobby probieren. Unser Tipp: Suchen Sie sich ein Buch für die dunklen Abende — die Bibliotheken haben im November oft neue Bücher und Lesungen. Und wer Sport mag: Am Sonntag läuft die NFL im Fernsehen.")
f.para("Auch der Fußball gehört zur Woche: Am Freitag spielt die Nationalmannschaft in Belgrad — viele Jugendliche schauen das Spiel im Fernsehen. Wer in München wohnt, sieht am Sonntag vielleicht sogar die NFL-Stars in der Stadt. Mehr dazu auf Seite 4.")
f.gloss("basteln = bricoler · der Pausenhof = cour de récré · sich verkleiden = se déguiser · die Stimmung = ambiance · der Pirat = pirate.")
f.end_report()

# col 3: facts + vocab + Und Sie (hand-rolled; CORRECTED height formula — see W45 KIT §geometry)
ix = COLX[3]
facts = ["Am 9. November sind alle Bundesländer wieder in der Schule.",
         "In vielen Klassen werden Laternen für St. Martin gebastelt.",
         "Am 11. November: Karneval am Vormittag, Laternen am Abend."]
sy3 = 200
sh = 45 + 33 * len(facts) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in facts)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SCHULWOCHE　La rentrée", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 facts ends", sy3 + sh)
words = ["die Laterne — lanterne", "basteln — bricoler", "das Lied — chanson",
         "das Kostüm — costume", "der Umzug — cortège", "der Stern — étoile"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "MARTINSWÖRTER　Saint-Martin", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Haben Sie als Kind eine Laterne gebastelt? Welches Lied singen Sie im November? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("As-tu fait une lanterne enfant ? Quelle chanson chantes-tu en novembre ? Écris deux phrases en allemand !", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　Et toi ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "As-tu fait une lanterne enfant ? Quelle chanson chantes-tu en novembre ? Écris deux phrases en allemand !", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- Wochenplan wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 300, fill=BOX)
p.text(sx + 24, 1162, "DER WOCHENPLAN DER REDAKTION　La semaine de la rédaction", 24, "sans", True, OLIVE)
planrows = [
    ("Mo 9.11.", "Schule für alle: Auch Bayern ist wieder da."),
    ("Di 10.11.", "Laternen basteln: Die Kitas bereiten den Umzug vor."),
    ("Mi 11.11.", "Karneval um 11.11 Uhr, Laternen am Abend."),
    ("Do 12.11.", "Nach dem Fest: In der Schule wird erzählt und geschrieben."),
    ("Fr 13.11.", "Nations League: Serbien – Deutschland (20.45 Uhr, RTL)."),
]
pyy = 1184
for t, txt in planrows:
    p.text(sx + 24, pyy + 24, t, 21, "sans", True, OLIVE)
    p.text(sx + 190, pyy + 24, txt, 21.5, "serif", False, INK)
    pyy += 45

# ---- P5 exercises ----
ey = 1500
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Exercices page 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　Les niveaux se mélangent — retrouve chaque réponse par son numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P5-ex")
e.head("A　LESEVERSTEHEN", 25)
e.bridge("Lis l'article page 5 et choisis la bonne réponse.")
e.ex("B1", "QCM", "A", "la rentrée partout le 9 novembre",
     "Wann sind alle wieder in der Schule? A. am 9. November · B. am 11. November · C. am 15. November", size=20, gap=8)
e.ex("B1", "QCM", "B", "les enfants fabriquent des lanternes en papier",
     "Was basteln die Kinder? A. ein Kostüm · B. Laternen aus Papier · C. einen Kürbis", size=20, gap=8)
e.ex("B1", "QCM", "B", "carnaval le matin, Saint-Martin l'après-midi",
     "Was ist am 11. November richtig? A. Nur Karneval. · B. Karneval am Vormittag, St. Martin am Abend. · C. Nur St. Martin.", size=20, gap=8)
e.ex("B1", "QCM", "B", "la NFL à la télé dimanche",
     "Was läuft am Sonntag im Fernsehen? A. die Bundesliga · B. die NFL · C. ein Film", size=20, gap=8)
e.ex("A2", "QCM", "A", "regarder l'équipe nationale vendredi",
     "Was schauen viele Jugendliche am Freitag? A. die Nationalmannschaft in Belgrad · B. die NFL · C. den Karneval", size=20, gap=8)
e.head("B　WÖRTER AUS DEM TEXT", 25)
e.bridge("Complète avec les mots de l'encadré.")
e.para("Laterne · basteln · Lied · Kostüm · Umzug · Stern", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "à compléter", "Laterne", "une lanterne en papier",
     "Die Kinder tragen eine bunte ___ durch die Straßen.", instr="Compléter", size=20, gap=8)
e.ex("B1", "à compléter", "basteln", "fabriquer des lanternes",
     "In der Schule ___ die Kinder Laternen.", instr="Compléter", size=20, gap=8)
e.ex("B1", "à compléter", "Lied", "chanter les chansons de la Saint-Martin",
     "Die Kinder singen ein Martins___.", instr="Compléter", size=20, gap=8)
e.ex("B1", "à compléter", "Kostüm", "un costume de carnaval",
     "In Köln tragen die Kinder ein buntes ___.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Umzug", "un cortège aux lanternes",
     "Am Abend zieht der ___ durch die Straßen.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Stern", "l'étoile sur la lanterne",
     "Auf der Laterne ist ein ___.", instr="Compléter", size=20, gap=8)
e.head("C　SÄTZE MIT «WEIL»", 25)
e.bridge("Relie les deux phrases avec weil (le verbe va à la fin).")
e.ex("B1", "transformation", "Die Kinder freuen sich, weil St. Martin kommt.", "dans une subordonnée en weil, le verbe va à la fin",
     "Die Kinder freuen sich. St. Martin kommt. (weil) → ___", instr="Réécrire", size=20, gap=8)
e.ex("B1", "transformation", "Er bleibt zu Hause, weil es dunkel ist.", "ist va à la fin",
     "Er bleibt zu Hause. Es ist dunkel. (weil) → ___", instr="Réécrire", size=20, gap=8)
e.ex("B1", "transformation", "Sie geht in die Bibliothek, weil sie ein Buch lesen will.", "will va à la fin",
     "Sie geht in die Bibliothek. Sie will ein Buch lesen. (weil) → ___", instr="Réécrire", size=20, gap=8)
e.ex("B1", "transformation", "Köln feiert, weil die Karnevalssession beginnt.", "beginnt va à la fin",
     "Köln feiert. Die Karnevalssession beginnt. (weil) → ___", instr="Réécrire", size=20, gap=8)
e.head("D　RICHTIG ODER FALSCH?", 25)
e.bridge("Vrai ou faux ?")
e.ex("A2", "vrai/faux", "Richtig", "la Bavière aussi de retour le 9 novembre",
     "Auch in Bayern sind die Herbstferien am 9. November vorbei. Richtig oder falsch?", instr="Vrai ou faux ?", size=20, gap=8)
e.ex("B1", "vrai/faux", "Falsch", "le cortège aux lanternes a lieu le soir",
     "Der Laternenumzug findet am Vormittag statt. Richtig oder falsch?", instr="Vrai ou faux ?", size=20, gap=8)
e.ex("A2", "vrai/faux", "Richtig", "les enfants chantent les chansons de la Saint-Martin",
     "Die Kinder singen Martinslieder. Richtig oder falsch?", instr="Vrai ou faux ?", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jugend.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERTIEFUNG　Approfondissement", "Die Lucerna", "LEVEL B2　Volkstrauertag & Stromsteuer　Jour du souvenir et taxe sur l'électricité")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P6-main")
f.title("Stille am Sonntag: Was bedeutet der Volkstrauertag?", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: B2")
f.para("Am Sonntag, dem 15. November, ist Volkstrauertag: ein staatlicher Gedenktag. Die Menschen gedenken der Opfer von Gewalt und Krieg aller Nationen. In vielen Städten gibt es Gedenkstunden und Kranzniederlegungen. Der Tag liegt zwei Sonntage vor dem ersten Advent — und er ist ein stiller Tag.")
f.para("Die zentrale Gedenkstunde findet im Bundestag statt. Das ZDF überträgt ab 13.30 Uhr live. In diesem Jahr steht sie im Zeichen der deutsch-österreichischen Verbundenheit: Die Gedenkrede hält der österreichische Bundespräsident Alexander Van der Bellen. Bundespräsident Frank-Walter Steinmeier spricht das Totengedenken.")
f.para("Warum gibt es diesen Tag? Die erste Gedenkstunde fand 1922 im Reichstag statt. Seit 1952 wird der Volkstrauertag zwei Sonntage vor dem ersten Advent begangen. Gedenken heißt hier: innehalten, erinnern — und für Frieden und Versöhnung einstehen.")
f.para("Zweites Thema: die Stromsteuer. Kanzler Friedrich Merz will sie für alle auf das europäische Mindestmaß senken — versprochen war das schon im Koalitionsvertrag. Bisher gilt die Senkung nur für bestimmte Branchen. Haushalte zahlen weiter 2,05 Cent pro Kilowattstunde. Finanzminister Lars Klingbeil zeigt sich offen, zweifelt aber an der Finanzierung.")
f.para("Die Grünen hatten im April einen Entwurf zur Senkung für alle vorgelegt — der Bundestag lehnte ihn mit 310 zu 270 Stimmen ab. Der Haushalt 2027 soll am 27. November verabschiedet werden. Ob eine Einigung gelingt, ist offen.")
f.para("Zwei Themen, ein Muster: Gedenken und Energiepolitik betreffen fast jeden Haushalt. Am Sonntag ist es still im Land. Am Montag geht die Debatte weiter.", gap=0)
f.gloss("gedenken = commémorer · Kranzniederlegung = dépôt de gerbe · stille Tag = jour de silence · Verbundenheit = lien · Versöhnung = réconciliation.", gap=0)
f.end_report()

# col 3: numbers box + debate box (measured)
ix = COLX[3]
tl = [("15.11.", "Volkstrauertag — zwei Sonntage vor dem ersten Advent."),
      ("1922", "erste Gedenkstunde im Reichstag in Berlin."),
      ("13.30", "Uhr: Das ZDF überträgt die Gedenkstunde live."),
      ("2,05", "Cent pro Kilowattstunde: Stromsteuer für Haushalte."),
      ("0,05", "Cent: Stromsteuer für die Industrie seit 2026."),
      ("27.11.", "Verabschiedung des Bundeshaushalts 2027 geplant.")]
tlh = 45 + 30.5 * len(tl) + 29.11 * sum(len(wrap(t, "serif", False, 20.5, CW - 152)) for yr, t in tl)
p.rect(ix, 200, CW, tlh, fill=BOX)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DIE ZAHLEN　Les chiffres", 24, "sans", True, OLIVE)
yy3 += 52
for yr, t in tl:
    p.text(ix + 22, yy3 + 21, yr, 21, "sans", True, OLIVE)
    yy3 = p.para(ix + 130, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 152, 1.42) + 10
print("P6 col3 numbers ends", 200 + tlh)
deb = "Volkstrauertag: Gedenken braucht Stille — darüber sind sich fast alle einig. Stromsteuer: Wie stark sie sinkt, ist noch offen. Beides betrifft fast jeden Haushalt."
hy3 = 200 + tlh + 26
hh = 140 + 29.82 * len(wrap(deb, "serif", False, 21, CW - 44)) + 27.69 * (len(wrap("Jour du souvenir : se souvenir demande du silence — presque tout le monde est d'accord. Taxe sur l'électricité : la baisse reste ouverte. Les deux touchent presque chaque foyer.", "sans", False, 19.5, CW - 44)) - 1)
p.rect(ix, hy3, CW, hh, fill="#f0eee5")
yy3 = hy3 + 16
p.text(ix + 22, yy3 + 26, "DIE DEBATTE IN EINEM SATZ", 22.5, "sans", True, OLIVE)
yy3 += 50
yy3 = p.para(ix + 22, yy3 + 21, deb, 21, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Jour du souvenir : se souvenir demande du silence — presque tout le monde est d'accord. Taxe sur l'électricité : la baisse reste ouverte. Les deux touchent presque chaque foyer.", 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", hy3 + hh)

# ---- Two Sundays wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 252, fill="#f0eee5")
p.text(sx + 24, 1162, "ZWEI SONNTAGE IM NOVEMBER　Deux dimanches de novembre", 24, "sans", True, OLIVE)
p.text(sx + 24, 1210, "VOLKSTRAUERTAG — 15. NOVEMBER", 21, "sans", True, OLIVE)
p.text(sx + 24 + (swd - 48) // 2, 1210, "TOTENSONNTAG — 22. NOVEMBER", 21, "sans", True, OLIVE)
pro = ["Gedenken an die Opfer von Gewalt und Krieg aller Nationen.",
       "Zentrale Gedenkstunde im Bundestag, Kranzniederlegungen im ganzen Land."]
contra = ["Evangelischer Gedenktag für die Verstorbenen.",
          "Eine Woche nach dem Volkstrauertag; dazwischen der Buß- und Bettag (18. November, Feiertag in Sachsen)."]
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
bars = [("Nations League und NFL", 46, "football"),
        ("St. Martin und Karneval", 34, "fêtes"),
        ("Volkstrauertag und Gedenken", 20, "mémoire")]
byy = cy + 58
for lab, v, zh in bars:
    p.text(MX, byy + 26, lab, 22, "serif", True, INK)
    p.text(MX + 360, byy + 26, zh, 20, "sans", False, GREY)
    p.rect(MX + 470, byy + 4, v * 17, 30, fill=OLIVE)
    p.text(MX + 470 + v * 17 + 16, byy + 26, f"{v} %", 22, "sans", True, OLIVE)
    byy += 52
p.text(MX, byy + 22, "ÜBUNGSDATEN　Données d'exercice — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Données d'exercice, pas un vrai sondage.)", 19.5, "sans", False, GREY)

# ---- P6 exercises ----
ey = 1752
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Exercices page 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　Les niveaux se mélangent — retrouve chaque réponse par son numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P6-ex")
e.head("A　DAS DIAGRAMM LESEN", 25, gap=6)
e.bridge("Utilise le graphique d'exercice ci-dessus.", gap=6)
e.ex("B1", "QCM", "A", "le football en tête avec 46 %",
     "Was interessiert die Leser am meisten (Übungsdaten)? A. Nations League und NFL · B. St. Martin · C. Volkstrauertag", size=20, gap=6)
e.ex("B1", "QCM", "B", "les fêtes deuxièmes avec 34 %",
     "Was ist die zweitgrößte Gruppe? A. Volkstrauertag · B. St. Martin und Karneval · C. Nations League", size=20, gap=6)
e.ex("B1", "QCM", "B", "46+34=80",
     "Fußball und Feste zusammen sind... A. 66 % · B. 80 % · C. 100 %", size=20, gap=6)
e.ex("B2", "QCM", "B", "le souvenir le plus petit avec 20 %",
     "Welche Gruppe ist kleiner? A. Feste · B. Gedenken · C. beide gleich", size=20, gap=6)
e.ex("B1", "QCM", "A", "le souvenir 20 %",
     "Wie viele Prozent interessieren sich für den Volkstrauertag? A. 20 % · B. 34 % · C. 46 %", size=20, gap=6)
e.ex("B2", "QCM", "B", "46+34+20=100",
     "Die drei Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 %", size=20, gap=6)
e.head("B　LESEVERSTEHEN (B2)", 25, gap=6)
e.bridge("Lis l'article page 6.", gap=6)
e.ex("B2", "QCM", "B", "le jour du souvenir, c'est le 15 novembre",
     "Wann ist Volkstrauertag? A. 11. November · B. 15. November · C. 22. November", size=20, gap=6)
e.ex("B2", "QCM", "A", "la ZDF en direct dès 13 h 30",
     "Wer überträgt die Gedenkstunde ab 13.30 Uhr? A. das ZDF · B. RTL · C. die ARD", size=20, gap=6)
e.ex("B2", "QCM", "B", "la taxe des foyers est de 2,05 centimes",
     "Wie hoch ist die Stromsteuer für Haushalte? A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent", size=20, gap=6)
e.ex("B1", "QCM", "B", "vote du budget 2027 le 27 novembre",
     "Wann soll der Bundeshaushalt 2027 verabschiedet werden? A. am 15. November · B. am 27. November · C. am 18. November", size=20, gap=6)
e.head("C　GRAMMATIK", 25, gap=6)
e.bridge("Complète avec la forme entre parenthèses.", gap=6)
e.ex("B2", "à compléter", "wird", "passif : wird + participe passé",
     "Die Gedenkstunde ___ (werden) live übertragen.", instr="Compléter", size=20, gap=6)
e.ex("B2", "à compléter", "ob", "ob introduit une question indirecte",
     "Niemand weiß, ___ die Einigung gelingt.", instr="Compléter", size=20, gap=6)
e.ex("B1", "à compléter", "geht", "gehen → geht",
     "Die Debatte ___ (gehen) weiter.", instr="Compléter", size=20, gap=6)
e.ex("B2", "à compléter", "spricht", "sprechen → spricht",
     "Steinmeier ___ (sprechen) das Totengedenken.", instr="Compléter", size=20, gap=6)
e.head("D　WÖRTER DER DEBATTE", 25, gap=6)
e.bridge("Complète avec les mots de l'encadré.", gap=6)
e.para("Kranzniederlegung · Versöhnung · Verbundenheit · gedenken", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "à compléter", "Kranzniederlegung", "une cérémonie de dépôt de gerbe",
     "In vielen Städten gibt es eine ___.", instr="Compléter", size=20, gap=6)
e.ex("B2", "à compléter", "Versöhnung", "pour la paix et la réconciliation",
     "Gedenken heißt: für Frieden und ___ einstehen.", instr="Compléter", size=20, gap=6)
e.ex("B2", "à compléter", "Verbundenheit", "le lien germano-autrichien",
     "Die Gedenkstunde steht im Zeichen der deutsch-österreichischen ___.", instr="Compléter", size=20, gap=6)
e.ex("B1", "à compléter", "gedenken", "se souvenir des victimes",
     "Die Menschen ___ der Opfer von Gewalt und Krieg.", instr="Compléter", size=20, gap=6)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-vertiefung.svg")
print("P6 saved, exercises so far:", len(REG))
