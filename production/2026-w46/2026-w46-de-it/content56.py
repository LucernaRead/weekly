# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUGEND　Giovani", "Die Lucerna", "LEVEL B1　Laternen, Lieder & Schule　Lanterne, canzoni e scuola")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P5-main")
f.title("Laternen basteln, Lieder singen: Die Woche der Kinder", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: B1")
f.para("Am Montag, dem 9. November, sind alle wieder in der Schule: Auch in Bayern sind die Herbstferien jetzt vorbei. Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut. Und in vielen Klassen wird schon gebastelt: Laternen für St. Martin.")
f.para("Was basteln die Kinder? Bunte Laternen aus Papier, mit Sternen, Monden und Tieren. In der Kita und in der Schule singen sie Martinslieder und üben den Umzug. Am Mittwochabend ziehen sie dann mit ihren Laternen durch die Straßen — vorneweg der heilige Martin auf dem Pferd.")
f.para("Und in Köln? Dort beginnt am Mittwoch um 11.11 Uhr die Karnevalssession. Auch Kinder verkleiden sich: als Prinzessin, als Pirat, als Tier. Aber Vorsicht: Am Vormittag ist Karneval, am Abend ist St. Martin — zwei Feste, zwei Stimmungen, ein Tag.")
f.para("Was macht man nach der Schule im dunklen November? Lesen, was man im Herbst begonnen hat, oder ein neues Hobby probieren. Unser Tipp: Suchen Sie sich ein Buch für die dunklen Abende — die Bibliotheken haben im November oft neue Bücher und Lesungen. Und wer Sport mag: Am Sonntag läuft die NFL im Fernsehen.")
f.para("Auch der Fußball gehört zur Woche: Am Freitag spielt die Nationalmannschaft in Belgrad — viele Jugendliche schauen das Spiel im Fernsehen. Wer in München wohnt, sieht am Sonntag vielleicht sogar die NFL-Stars in der Stadt. Mehr dazu auf Seite 4.")
f.gloss("basteln = costruire · der Pausenhof = cortile · sich verkleiden = travestirsi · die Stimmung = atmosfera · der Pirat = pirata.")
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
p.text(ix + 22, yy3 + 26, "SCHULWOCHE　A scuola", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 facts ends", sy3 + sh)
words = ["die Laterne — lanterna", "basteln — costruire", "das Lied — canzone",
         "das Kostüm — costume", "der Umzug — corteo", "der Stern — stella"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "MARTINSWÖRTER　San Martino", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Haben Sie als Kind eine Laterne gebastelt? Welches Lied singen Sie im November? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("Hai fatto una lanterna da bambino? Quale canzone canti a novembre? Scrivi due frasi in tedesco!", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　E tu?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Hai fatto una lanterna da bambino? Quale canzone canti a novembre? Scrivi due frasi in tedesco!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- Wochenplan wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 300, fill=BOX)
p.text(sx + 24, 1162, "DER WOCHENPLAN DER REDAKTION　La settimana della redazione", 24, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "ÜBUNGEN　Esercizi pagina 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　I livelli si mescolano: trova ogni risposta dal suo numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P5-ex")
e.head("A　LESEVERSTEHEN", 25)
e.bridge("Leggi l'articolo di pagina 5 e scegli la risposta giusta.")
e.ex("B1", "scelta multipla", "A", "la scuola ricomincia ovunque il 9 novembre",
     "Wann sind alle wieder in der Schule? A. am 9. November · B. am 11. November · C. am 15. November", size=20, gap=8)
e.ex("B1", "scelta multipla", "B", "i bambini fanno lanterne di carta",
     "Was basteln die Kinder? A. ein Kostüm · B. Laternen aus Papier · C. einen Kürbis", size=20, gap=8)
e.ex("B1", "scelta multipla", "B", "carnevale al mattino, San Martino al pomeriggio",
     "Was ist am 11. November richtig? A. Nur Karneval. · B. Karneval am Vormittag, St. Martin am Abend. · C. Nur St. Martin.", size=20, gap=8)
e.ex("B1", "scelta multipla", "B", "la NFL in TV domenica",
     "Was läuft am Sonntag im Fernsehen? A. die Bundesliga · B. die NFL · C. ein Film", size=20, gap=8)
e.ex("A2", "scelta multipla", "A", "guardare la nazionale venerdì",
     "Was schauen viele Jugendliche am Freitag? A. die Nationalmannschaft in Belgrad · B. die NFL · C. den Karneval", size=20, gap=8)
e.head("B　WÖRTER AUS DEM TEXT", 25)
e.bridge("Completa con le parole del riquadro.")
e.para("Laterne · basteln · Lied · Kostüm · Umzug · Stern", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "completare", "Laterne", "una lanterna di carta",
     "Die Kinder tragen eine bunte ___ durch die Straßen.", instr="Completa", size=20, gap=8)
e.ex("B1", "completare", "basteln", "fare le lanterne",
     "In der Schule ___ die Kinder Laternen.", instr="Completa", size=20, gap=8)
e.ex("B1", "completare", "Lied", "cantare le canzoni di San Martino",
     "Die Kinder singen ein Martins___.", instr="Completa", size=20, gap=8)
e.ex("B1", "completare", "Kostüm", "un costume di carnevale",
     "In Köln tragen die Kinder ein buntes ___.", instr="Completa", size=20, gap=8)
e.ex("A2", "completare", "Umzug", "un corteo con le lanterne",
     "Am Abend zieht der ___ durch die Straßen.", instr="Completa", size=20, gap=8)
e.ex("A2", "completare", "Stern", "la stella sulla lanterna",
     "Auf der Laterne ist ein ___.", instr="Completa", size=20, gap=8)
e.head("C　SÄTZE MIT «WEIL»", 25)
e.bridge("Unisci le due frasi con weil (il verbo va alla fine).")
e.ex("B1", "trasformazione", "Die Kinder freuen sich, weil St. Martin kommt.", "in una subordinata con weil il verbo va alla fine",
     "Die Kinder freuen sich. St. Martin kommt. (weil) → ___", instr="Riscrivi", size=20, gap=8)
e.ex("B1", "trasformazione", "Er bleibt zu Hause, weil es dunkel ist.", "ist va alla fine",
     "Er bleibt zu Hause. Es ist dunkel. (weil) → ___", instr="Riscrivi", size=20, gap=8)
e.ex("B1", "trasformazione", "Sie geht in die Bibliothek, weil sie ein Buch lesen will.", "will va alla fine",
     "Sie geht in die Bibliothek. Sie will ein Buch lesen. (weil) → ___", instr="Riscrivi", size=20, gap=8)
e.ex("B1", "trasformazione", "Köln feiert, weil die Karnevalssession beginnt.", "beginnt va alla fine",
     "Köln feiert. Die Karnevalssession beginnt. (weil) → ___", instr="Riscrivi", size=20, gap=8)
e.head("D　RICHTIG ODER FALSCH?", 25)
e.bridge("Vero o falso?")
e.ex("A2", "vero/falso", "Richtig", "anche la Baviera torna il 9 novembre",
     "Auch in Bayern sind die Herbstferien am 9. November vorbei. Richtig oder falsch?", instr="Vero o falso?", size=20, gap=8)
e.ex("B1", "vero/falso", "Falsch", "il corteo con le lanterne è la sera",
     "Der Laternenumzug findet am Vormittag statt. Richtig oder falsch?", instr="Vero o falso?", size=20, gap=8)
e.ex("A2", "vero/falso", "Richtig", "i bambini cantano le canzoni di San Martino",
     "Die Kinder singen Martinslieder. Richtig oder falsch?", instr="Vero o falso?", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jugend.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERTIEFUNG　Approfondimento", "Die Lucerna", "LEVEL B2　Volkstrauertag & Stromsteuer　Giorno del ricordo e tassa sull'elettricità")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P6-main")
f.title("Stille am Sonntag: Was bedeutet der Volkstrauertag?", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: B2")
f.para("Am Sonntag, dem 15. November, ist Volkstrauertag: ein staatlicher Gedenktag. Die Menschen gedenken der Opfer von Gewalt und Krieg aller Nationen. In vielen Städten gibt es Gedenkstunden und Kranzniederlegungen. Der Tag liegt zwei Sonntage vor dem ersten Advent — und er ist ein stiller Tag.")
f.para("Die zentrale Gedenkstunde findet im Bundestag statt. Das ZDF überträgt ab 13.30 Uhr live. In diesem Jahr steht sie im Zeichen der deutsch-österreichischen Verbundenheit: Die Gedenkrede hält der österreichische Bundespräsident Alexander Van der Bellen. Bundespräsident Frank-Walter Steinmeier spricht das Totengedenken.")
f.para("Warum gibt es diesen Tag? Die erste Gedenkstunde fand 1922 im Reichstag statt. Seit 1952 wird der Volkstrauertag zwei Sonntage vor dem ersten Advent begangen. Gedenken heißt hier: innehalten, erinnern — und für Frieden und Versöhnung einstehen.")
f.para("Zweites Thema: die Stromsteuer. Kanzler Friedrich Merz will sie für alle auf das europäische Mindestmaß senken — versprochen war das schon im Koalitionsvertrag. Bisher gilt die Senkung nur für bestimmte Branchen. Haushalte zahlen weiter 2,05 Cent pro Kilowattstunde. Finanzminister Lars Klingbeil zeigt sich offen, zweifelt aber an der Finanzierung.")
f.para("Die Grünen hatten im April einen Entwurf zur Senkung für alle vorgelegt — der Bundestag lehnte ihn mit 310 zu 270 Stimmen ab. Der Haushalt 2027 soll am 27. November verabschiedet werden. Ob eine Einigung gelingt, ist offen.")
f.para("Zwei Themen, ein Muster: Gedenken und Energiepolitik betreffen fast jeden Haushalt. Am Sonntag ist es still im Land. Am Montag geht die Debatte weiter.", gap=0)
f.gloss("gedenken = commemorare · Kranzniederlegung = deposizione di corone · stille Tag = giorno di silenzio · Verbundenheit = legame · Versöhnung = riconciliazione.", gap=0)
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
p.text(ix + 22, yy3 + 26, "DIE ZAHLEN　I numeri", 24, "sans", True, OLIVE)
yy3 += 52
for yr, t in tl:
    p.text(ix + 22, yy3 + 21, yr, 21, "sans", True, OLIVE)
    yy3 = p.para(ix + 130, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 152, 1.42) + 10
print("P6 col3 numbers ends", 200 + tlh)
deb = "Volkstrauertag: Gedenken braucht Stille — darüber sind sich fast alle einig. Stromsteuer: Wie stark sie sinkt, ist noch offen. Beides betrifft fast jeden Haushalt."
hy3 = 200 + tlh + 26
hh = 140 + 29.82 * len(wrap(deb, "serif", False, 21, CW - 44)) + 27.69 * (len(wrap("Giorno del ricordo: ricordare chiede silenzio — quasi tutti sono d'accordo. Tassa sull'elettricità: quanto scenderà è ancora aperto. Entrambi riguardano quasi ogni famiglia.", "sans", False, 19.5, CW - 44)) - 1)
p.rect(ix, hy3, CW, hh, fill="#f0eee5")
yy3 = hy3 + 16
p.text(ix + 22, yy3 + 26, "DIE DEBATTE IN EINEM SATZ", 22.5, "sans", True, OLIVE)
yy3 += 50
yy3 = p.para(ix + 22, yy3 + 21, deb, 21, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Giorno del ricordo: ricordare chiede silenzio — quasi tutti sono d'accordo. Tassa sull'elettricità: quanto scenderà è ancora aperto. Entrambi riguardano quasi ogni famiglia.", 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", hy3 + hh)

# ---- Two Sundays wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 252, fill="#f0eee5")
p.text(sx + 24, 1162, "ZWEI SONNTAGE IM NOVEMBER　Due domeniche di novembre", 24, "sans", True, OLIVE)
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
p.text(MX, cy + 28, "WAS INTERESSIERT DIE LESER?　Cosa interessa ai lettori?", 26, "sans", True, OLIVE)
bars = [("Nations League und NFL", 46, "calcio"),
        ("St. Martin und Karneval", 34, "feste"),
        ("Volkstrauertag und Gedenken", 20, "memoria")]
byy = cy + 58
for lab, v, zh in bars:
    p.text(MX, byy + 26, lab, 22, "serif", True, INK)
    p.text(MX + 360, byy + 26, zh, 20, "sans", False, GREY)
    p.rect(MX + 470, byy + 4, v * 17, 30, fill=OLIVE)
    p.text(MX + 470 + v * 17 + 16, byy + 26, f"{v} %", 22, "sans", True, OLIVE)
    byy += 52
p.text(MX, byy + 22, "ÜBUNGSDATEN　Dati di esercizio — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Dati di esercizio, non un vero sondaggio.)", 19.5, "sans", False, GREY)

# ---- P6 exercises ----
ey = 1752
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Esercizi pagina 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　I livelli si mescolano: trova ogni risposta dal suo numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P6-ex")
e.head("A　DAS DIAGRAMM LESEN", 25, gap=6)
e.bridge("Usa il grafico di esercizio qui sopra.", gap=6)
e.ex("B1", "scelta multipla", "A", "il calcio in testa con il 46%",
     "Was interessiert die Leser am meisten (Übungsdaten)? A. Nations League und NFL · B. St. Martin · C. Volkstrauertag", size=20, gap=6)
e.ex("B1", "scelta multipla", "B", "le feste seconde con il 34%",
     "Was ist die zweitgrößte Gruppe? A. Volkstrauertag · B. St. Martin und Karneval · C. Nations League", size=20, gap=6)
e.ex("B1", "scelta multipla", "B", "46+34=80",
     "Fußball und Feste zusammen sind... A. 66 % · B. 80 % · C. 100 %", size=20, gap=6)
e.ex("B2", "scelta multipla", "B", "il ricordo il più piccolo con il 20%",
     "Welche Gruppe ist kleiner? A. Feste · B. Gedenken · C. beide gleich", size=20, gap=6)
e.ex("B1", "scelta multipla", "A", "il ricordo 20%",
     "Wie viele Prozent interessieren sich für den Volkstrauertag? A. 20 % · B. 34 % · C. 46 %", size=20, gap=6)
e.ex("B2", "scelta multipla", "B", "46+34+20=100",
     "Die drei Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 %", size=20, gap=6)
e.head("B　LESEVERSTEHEN (B2)", 25, gap=6)
e.bridge("Leggi l'articolo di pagina 6.", gap=6)
e.ex("B2", "scelta multipla", "B", "il giorno del ricordo è il 15 novembre",
     "Wann ist Volkstrauertag? A. 11. November · B. 15. November · C. 22. November", size=20, gap=6)
e.ex("B2", "scelta multipla", "A", "la ZDF in diretta dalle 13.30",
     "Wer überträgt die Gedenkstunde ab 13.30 Uhr? A. das ZDF · B. RTL · C. die ARD", size=20, gap=6)
e.ex("B2", "scelta multipla", "B", "la tassa delle famiglie è di 2,05 centesimi",
     "Wie hoch ist die Stromsteuer für Haushalte? A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent", size=20, gap=6)
e.ex("B1", "scelta multipla", "B", "voto del bilancio 2027 il 27 novembre",
     "Wann soll der Bundeshaushalt 2027 verabschiedet werden? A. am 15. November · B. am 27. November · C. am 18. November", size=20, gap=6)
e.head("C　GRAMMATIK", 25, gap=6)
e.bridge("Completa con la forma tra parentesi.", gap=6)
e.ex("B2", "completare", "wird", "passivo: wird + participio passato",
     "Die Gedenkstunde ___ (werden) live übertragen.", instr="Completa", size=20, gap=6)
e.ex("B2", "completare", "ob", "ob introduce una domanda indiretta",
     "Niemand weiß, ___ die Einigung gelingt.", instr="Completa", size=20, gap=6)
e.ex("B1", "completare", "geht", "gehen → geht",
     "Die Debatte ___ (gehen) weiter.", instr="Completa", size=20, gap=6)
e.ex("B2", "completare", "spricht", "sprechen → spricht",
     "Steinmeier ___ (sprechen) das Totengedenken.", instr="Completa", size=20, gap=6)
e.head("D　WÖRTER DER DEBATTE", 25, gap=6)
e.bridge("Completa con le parole del riquadro.", gap=6)
e.para("Kranzniederlegung · Versöhnung · Verbundenheit · gedenken", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "completare", "Kranzniederlegung", "una cerimonia di deposizione di corone",
     "In vielen Städten gibt es eine ___.", instr="Completa", size=20, gap=6)
e.ex("B2", "completare", "Versöhnung", "per la pace e la riconciliazione",
     "Gedenken heißt: für Frieden und ___ einstehen.", instr="Completa", size=20, gap=6)
e.ex("B2", "completare", "Verbundenheit", "il legame tedesco-austriaco",
     "Die Gedenkstunde steht im Zeichen der deutsch-österreichischen ___.", instr="Completa", size=20, gap=6)
e.ex("B1", "completare", "gedenken", "ricordare le vittime",
     "Die Menschen ___ der Opfer von Gewalt und Krieg.", instr="Completa", size=20, gap=6)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-vertiefung.svg")
print("P6 saved, exercises so far:", len(REG))
