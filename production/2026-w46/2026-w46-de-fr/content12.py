# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-de-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · FRONT PAGE (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3 · DRITTE AUSGABE", 23, "sans", True, OLIVE)
p.text(975, 92, "WÖCHENTLICH AUF DEUTSCH · CHAQUE SEMAINE · L'ALLEMAND QUE LISENT LES ALLEMANDS", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "WOCHE VOM 9. BIS 15. NOVEMBER 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Die Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "JOURNAL ALLEMAND · VOL.3 · ÉQUIPE NATIONALE · SAINT-MARTIN · NFL", 46, "serif", True, INK, anchor="middle")
p.text(975, 372, "TEXTE EN ALLEMAND · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES", 20, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# football band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "LÄNDERSPIELWOCHE — SERBIEN, KARNEVAL, NFL!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Montag bis Sonntag: Nationalelf, St. Martin, American Football — alles in einer Woche", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "SEMAINE INTERNATIONALE · SAINT-MARTIN & NFL", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "Voir page 4", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "DIE TOPMELDUNG · À la une", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Länderspielpause in Deutschland: Kampf ums Viertelfinale, dann die NFL in München", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Von der Lucerna-Redaktion · Leseniveau: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Diese Woche spielt die Bundesliga nicht: Es ist Länderspielpause. Die deutsche Nationalmannschaft trifft am Freitagabend in Belgrad auf Serbien — und am Montag danach in Berlin auf die Niederlande. Es geht ums Viertelfinale.")
f.para("Am Freitag (20.45 Uhr) spielt Deutschland in Belgrad — vor leeren Rängen. Am Montag (20.45 Uhr) folgt das Heimspiel gegen die Niederlande in Berlin.")
f.para("Am Mittwoch ist in Deutschland ein besonderer Tag: Um 11.11 Uhr beginnt in Köln die neue Karnevalssession — und am Abend ziehen Kinder mit Laternen durch die Straßen: Es ist St. Martin.")
f.para("Am Sonntag wird München zur Football-Stadt: Um 15.30 Uhr spielen in der Allianz Arena die Detroit Lions gegen die New England Patriots. Das Spiel ist ausverkauft.")
f.para("Aber diese Woche ist mehr als Sport: Am Sonntag ist auch Volkstrauertag — ein stiller Gedenktag. Die zentrale Gedenkstunde findet im Bundestag statt.")
f.bridge("Notes — die Länderspielpause = trêve internationale · das Viertelfinale = quart de finale · ausverkauft = complet.")
f.box("DIE WOCHE IN ZAHLEN · En chiffres", [
    ("5 — Punkte hat Deutschland nach vier Spielen in der Nations League (l'Allemagne a 5 points après quatre matches)", "serif", False, INK, 20.5, 1.35),
    ("11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln (le carnaval commence à 11 h 11)", "serif", False, INK, 20.5, 1.35),
    ("15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München (le match NFL commence dimanche à 15 h 30)", "serif", False, INK, 20.5, 1.35),
])
f.head("JETZT ÜBEN · À toi de jouer", 25)
f.ex("A2", "à compléter", "Länderspielpause", "semaine de trêve internationale",
     "Diese Woche ist ___: Die Bundesliga spielt nicht, die Nationalmannschaft spielt.", size=20.5)
f.ex("A2", "à compléter", "Belgrad", "capitale de la Serbie",
     "Am Freitag spielt Deutschland in ___ gegen Serbien.", size=20.5)
f.ex("A2", "à compléter", "Karnevals", "le carnaval commence à 11 h 11",
     "Um 11.11 Uhr beginnt in Köln die neue Session des ___.", size=20.5)
f.ex("A2", "à compléter", "München", "la NFL à Munich",
     "Am Sonntag spielen die Lions und die Patriots in ___.", size=20.5)
f.ex("B1", "à compléter", "fünf", "5 points après quatre matches",
     "Deutschland hat nach vier Spielen ___ Punkte.", size=20.5)
f.ex("B1", "à compléter", "Volkstrauertag", "dimanche, jour du souvenir",
     "Am Sonntag ist auch ___: ein stiller Gedenktag.", size=20.5)
f.end_report()

# ---- questions of the week (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "FRAGEN", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "DER WOCHE", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Grandes questions · Die Fragen der Woche", 19, "sans", False, GREY)
gt = [
    ("„Deutschland im Viertelfinale?“", 250),
    ("„Sieg in Belgrad?“", 226),
    ("„Karneval oder Laternen?“", 196),
    ("„NFL in München: Wer gewinnt?“", 158),
    ("„Volkstrauertag — was ist das?“", 122),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE if i == 0 else GOLD)
    byy += 92
p.text(gx + 22, byy + 16, "Die fünf Fragen, über die Deutschland", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "in dieser Woche spricht.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "Les cinq questions qui agitent l'Allemagne.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "IN DIESER AUSGABE · Sommaire", 24, "sans", True, OLIVE)
som = [
    ("S.2", "11. November & Alltag", "A2"),
    ("S.3", "St. Martin & Karneval", "A2→B1"),
    ("S.4", "Nationalelf & NFL", "B1"),
    ("S.5", "Laternen & Kinder", "B1"),
    ("S.6", "Gedenken & Stromsteuer", "B2"),
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
p.para(gx, my + 76, "« das Geisterspiel » : Ein Spiel vor leeren Rängen — ohne Zuschauer im Stadion.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, my + 152, "Un match sans spectateurs. Voir page 4.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "fussball.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Fußball auf dem Rasen: In dieser Woche spielt die Nationalmannschaft in Belgrad — die Bundesliga pausiert. Am Montag danach kommen die Niederlande nach Berlin. (Seite 4)",
        "Foto: Staff Sgt. Stephanie Jacobs, U.S. Air Force — public domain")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-fussball")
f2.head("EINE WOCHE, ZWEI WELTEN", 25)
f2.para("Freitagabend in Belgrad, Sonntag in München: Erst die Nationalelf, dann American Football — eine Woche, zwei Ballspiele.", 22.5)
f2.para("Und am Montag danach? Da spielt Deutschland schon wieder — gegen die Niederlande in Berlin. Die Länderspielpause ist kurz, aber sie ist voll.", 22.5)
f2.end_report()
# col 3 KURZ & GUT
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "KURZ & GUT · En bref", 24, "sans", True, OLIVE)
brefs = [
    ("FUSSBALL", "Nations League: Serbien auswärts, Niederlande zu Hause. (Seite 4)"),
    ("NFL", "Lions gegen Patriots in München, 15.30 Uhr, RTL live. (Seite 4)"),
    ("11. NOVEMBER", "Karneval um 11.11 Uhr in Köln, Laternen am Abend überall. (Seite 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "BLITZQUIZ · Quiz éclair", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lis la une, choisis la bonne réponse · Réponses page 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "QCM", "B", "à l'extérieur en Serbie vendredi",
      "Deutschland spielt am Freitag in... A. Berlin · B. Belgrad · C. München", size=21)
qf.ex("A2", "QCM", "C", "coup d'envoi NFL à 15 h 30",
      "Das NFL-Spiel in München beginnt um... A. 11.11 Uhr · B. 20.45 Uhr · C. 15.30 Uhr", size=21)
qf.ex("A2", "QCM", "A", "le carnaval commence à 11 h 11",
      "Die Karnevalssession beginnt in Köln um... A. 11.11 Uhr · B. 15.30 Uhr · C. 20.45 Uhr", size=21)
qf.ex("A2", "QCM", "A", "le jour du souvenir, c'est dimanche",
      "Der Volkstrauertag ist am... A. Sonntag, 15. November · B. Mittwoch, 11. November · C. Montag, 9. November", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LEBEN · La vie", "Die Lucerna", "LEVEL A2 · Der 11. November & der Alltag · Le 11 novembre et le quotidien")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Ein Mittwoch, zwei Feste: Karneval am Morgen, Laternen am Abend", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: A2")
f.para("Am Mittwoch, dem 11. November, ist in Deutschland viel los: Um 11.11 Uhr beginnt in Köln die neue Karnevalssession. Auf dem Heumarkt und dem Alter Markt feiern die Jecken den Start der „fünften Jahreszeit“ — mit Musik, Kostümen und Konfetti. Der WDR überträgt ab 10.30 Uhr live.")
f.para("Am Abend desselben Tages wird es stiller — und heller: Kinder ziehen mit selbst gebastelten Laternen durch die Straßen und singen Martinslieder. Es ist St. Martin. Vorneweg reitet oft ein Reiter als heiliger Martin, am Feuer wird die Mantelteilung gespielt. Danach gibt es Gebäck: den Weckmann.")
f.para("Warum feiern die Menschen am 11. November gleich zwei Feste? Der Martinstag ist der Gedenktag des heiligen Martin von Tours. Der Karneval beginnt an diesem Tag, weil die Zahl Elf die Narrenzahl ist — 11.11 Uhr, am 11.11. So teilen sich ein alter Heiligentag und ein närrischer Start denselben Mittwoch.")
f.para("Was isst man an diesem Tag? In vielen Familien gibt es die Martinsgans: Gänsebraten mit Rotkohl und Klößen. In Bäckereien gibt es den Weckmann — einen Mann aus Hefeteig. Und wer in Köln feiert, trinkt vielleicht ein Kölsch und singt mit. Am 11. November ist kein Feiertag: Schule und Arbeit laufen normal.")
f.para("Und die dunkle Jahreszeit? Die Abende sind jetzt lang und kalt. Viele Menschen bereiten schon den Advent vor: Sie kaufen Kerzen, backen Plätzchen — oder basteln Laternen mit ihren Kindern. Der November ist dunkel, aber er ist nicht still: Er singt, leuchtet und feiert.")
f.gloss("der Jeck = fou du carnaval (dialecte de Cologne) · die fünfte Jahreszeit = la cinquième saison (carnaval) · die Laterne = lanterne · der Weckmann = bonhomme brioché · die Martinsgans = oie de la Saint-Martin.")
f.end_report()

# col 3: four boxes (hand-rolled; CORRECTED height formula — see W45 KIT §geometry)
ix = COLX[3]
zapf = ["11.11 Uhr — die Karnevalssession in Köln beginnt.",
        "Ab 10.30 Uhr — der WDR überträgt live.",
        "Am Abend — Laternenumzüge in ganz Deutschland."]
sy3 = 200
sh = 45 + 33 * len(zapf) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in zapf)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DER 11. NOVEMBER", 24, "sans", True, OLIVE)
yy3 += 52
for t in zapf:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P2 col3 box1 ends", sy3 + sh)
sav = ["Kein Feiertag: Schule und Arbeit laufen normal.",
       "Die Zahl Elf gilt im Karneval als Narrenzahl.",
       "Der Weckmann heißt anderswo Stutenkerl oder Martinsmann."]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(sav) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in sav)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WUSSTEN SIE DAS?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P2 col3 box2 ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Feiern Sie Karneval oder St. Martin? Was singen Kinder in Ihrem Land? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("Karneval ou Saint-Martin ? Écris deux phrases en allemand !", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE? · Et toi ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Karneval ou Saint-Martin ? Écris deux phrases en allemand !", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 box3 ends", ey3 + eh)
zew = ["Martin von Tours — Soldat, Mönch, Bischof.",
       "Die Legende: Er teilte seinen Mantel.",
       "Die Gans verriet der Legende nach sein Versteck."]
sy3 = ey3 + eh + 26
sh = 45 + 33 * len(zew) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in zew)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "MARTIN IN KÜRZE · En bref", 24, "sans", True, OLIVE)
yy3 += 52
for t in zew:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P2 col3 box4 ends", sy3 + sh)

# ---- Rechnen wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "RECHNEN WIR MAL · Calculons", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Die Uhrzeiten der Woche · Les heures de la semaine", 20, "sans", False, GREY, anchor="end")
lx = MX
ly = dy + 58
for line in [
    ("11.11 Uhr + 6 Stunden", "= etwa 17 Uhr: Die Laternenumzüge beginnen"),
    ("15.30 Uhr — NFL in München", "= 4 Stunden 19 Minuten nach 11.11 Uhr"),
    ("9. bis 15. November", "= 7 Tage: eine volle Länderspielwoche"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 360, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 36
p.para(1090, ly - 108 + 22, "Achtung: Der 11. November ist ein Werktag. Wer nach Köln fährt, sollte früh kommen: Die Altstadt ist voll, und am Abend gehören die Straßen den Kindern mit Laternen!", 20.5, "serif", False, INK, RIGHT - 1090, 1.42)
p.para(1090, ly - 108 + 22 + 4 * 29.1 + 10, "Note : le 11 novembre est un jour travaillé. Arrive tôt à Cologne : la vieille ville est bondée, et le soir les rues sont aux enfants et à leurs lanternes.", 20, "sans", False, GREY, RIGHT - 1090, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · Exercices page 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · Les niveaux se mélangent — retrouve chaque réponse par son numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · WIE VIEL UHR?", 25)
e.bridge("Lis l'article page 2 et complète les heures.")
e.ex("A2", "à compléter", "11.11", "le carnaval commence à 11 h 11",
     "Die Karnevalssession beginnt um ___ Uhr.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "10.30", "la WDR en direct dès 10 h 30",
     "Der WDR überträgt ab ___ Uhr live.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "15.30", "coup d'envoi NFL à 15 h 30",
     "Das NFL-Spiel in München beginnt um ___ Uhr.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "11. November", "la Saint-Martin, c'est le 11 novembre",
     "St. Martin ist am ___.", instr="Compléter", size=20, gap=8)
e.ex("A2", "à compléter", "Mittwoch", "le 11 novembre est un mercredi",
     "Der 11. November 2026 ist ein ___.", instr="Compléter", size=20, gap=8)
e.head("B · DAS PERFEKT", 25)
e.bridge("Réécris au Perfekt (passé composé).")
e.ex("A2", "transformation", "Der Karneval hat in Köln begonnen.", "beginnen → begonnen",
     "Der Karneval (beginnen) in Köln. → ___", instr="Réécrire", size=20, gap=8)
e.ex("A2", "transformation", "Die Kinder haben Martinslieder gesungen.", "singen → gesungen",
     "Die Kinder (singen) Martinslieder. → ___", instr="Réécrire", size=20, gap=8)
e.ex("A2", "transformation", "Wir haben eine Laterne gebastelt.", "basteln → gebastelt",
     "Wir (basteln) eine Laterne. → ___", instr="Réécrire", size=20, gap=8)
e.ex("B1", "transformation", "Martin hat seinen Mantel geteilt.", "teilen → geteilt",
     "Martin (teilen) seinen Mantel. → ___", instr="Réécrire", size=20, gap=8)
e.ex("B1", "transformation", "Viele Familien haben Martinsgans gegessen.", "essen → gegessen",
     "Viele Familien (essen) Martinsgans. → ___", instr="Réécrire", size=20, gap=8)
e.head("C · LESEVERSTEHEN", 25)
e.bridge("Lis l'article page 2 et choisis la bonne réponse.")
e.ex("A2", "QCM", "B", "la WDR en direct dès 10 h 30",
     "Wann überträgt der WDR? A. um 11.11 Uhr · B. ab 10.30 Uhr · C. um 15.30 Uhr", size=20, gap=8)
e.ex("A2", "QCM", "B", "un Weckmann est un bonhomme brioché",
     "Was ist ein Weckmann? A. ein Lied · B. Gebäck aus Hefeteig · C. eine Laterne", size=20, gap=8)
e.ex("A2", "QCM", "A", "le 11 novembre n'est pas férié",
     "Ist der 11. November ein Feiertag? A. Nein, Schule und Arbeit laufen normal. · B. Ja, alles ist geschlossen. · C. Nur in Köln.", size=20, gap=8)
e.ex("A2", "QCM", "B", "l'oie de la Saint-Martin, chou rouge et quenelles",
     "Was isst man mit der Martinsgans? A. Pommes · B. Rotkohl und Klöße · C. Eis", size=20, gap=8)
e.head("D · DIE WÖRTER", 25)
e.match_set("A2", "appariement",
            ["der Jeck", "die Laterne", "der Weckmann", "die Martinsgans"],
            ["das Licht aus Papier, das die Kinder am Abend tragen",
             "der Mann aus Hefeteig, den die Kinder bekommen",
             "der Mensch, der in Köln Karneval feiert",
             "der Gänsebraten am Martinstag"],
            ["c", "a", "b", "d"],
            ["Jeck=fou du carnaval c", "Laterne=lanterne a", "Weckmann=bonhomme brioché b", "Martinsgans=oie de la Saint-Martin d"],
            instr="Relier les paires")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leben.svg")
print("P2 saved, exercises so far:", len(REG))
