# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("KULTUR　Cultuur", "Die Lucerna", "A2 → B1　St. Martin, Karneval & Rückblick　Sint Maarten, carnaval en een terugblik")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("St. Martin: Ein Mantel, eine Laterne, eine Gans", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: A2 → B1")
f.para("Wer war St. Martin? Martin von Tours lebte vor mehr als 1600 Jahren. Der Legende nach war er ein römischer Soldat. An einem kalten Wintertag traf er einen Bettler — und teilte seinen Mantel mit ihm. Später wurde Martin Mönch und Bischof von Tours. Sein Gedenktag ist der 11. November.")
f.para("Was machen die Kinder heute? Sie basteln in der Kita und in der Schule bunte Laternen aus Papier. Am Abend ziehen sie singend durch die Straßen: „Ich geh mit meiner Laterne …“ Vorneweg reitet oft der heilige Martin auf einem Pferd. Am Martinsfeuer endet der Zug — und jedes Kind bekommt Gebäck.")
f.para("Und die Gans? Der Legende nach versteckte sich Martin vor seiner Wahl zum Bischof in einem Gänsestall — die Gänse verrieten ihn mit ihrem Geschnatter. Darum gibt es am Martinstag die Martinsgans: Gänsebraten mit Rotkohl und Klößen. Ob die Legende stimmt, weiß niemand genau — aber die Gans schmeckt.")
f.para("Rückblick — ehrlich gesagt: Am Dienstag und Mittwoch, dem 3. und 4. November, spielte die Champions League ihren 4. Spieltag, am Donnerstag, dem 5. November, die Europa League. Am Freitag bis Sonntag, dem 6. bis 8. November, lief der 9. Spieltag der Bundesliga. Die Ergebnisse standen bei Redaktionsschluss am 2. November noch nicht fest. Wir berichten darüber in VOL.4 — versprochen.")
f.para("Und die Kultur im November? Die Museen und Theater spielen ihr Herbstprogramm, die ersten Weihnachtsmärkte bereiten sich vor. Ein Tipp der Redaktion: Gehen Sie an einem grauen Nachmittag ins Museum — dort ist es warm, ruhig und hell. Und wer ein Buch sucht: Die Bibliotheken haben im November oft Lesungen.")
f.para("Für Kinder gibt es in dieser Woche noch ein zweites Highlight: In Köln beginnt am 11. November um 11.11 Uhr die Karnevalssession — mit dem Dreigestirn aus Prinz, Bauer und Jungfrau. Am Abend gehören die Straßen dann den Laternen. Mehr dazu auf Seite 2.")
f.gloss("der Bettler = bedelaar · der Mantel = mantel · das Geschnatter = gesnater · der Gänsestall = ganzenstal · das Dreigestirn = carnavalstriumviraat.")
f.end_report()

# col 3: facts + vocab + Und Sie + Tipp (hand-rolled; CORRECTED height formula — see W45 KIT §geometry)
ix = COLX[3]
facts = ["Der 11. November ist der Gedenktag des heiligen Martin von Tours.",
         "Die Laternenumzüge finden oft auch an Abenden vor oder nach dem 11. November statt.",
         "Karneval und St. Martin teilen sich den 11. November — morgens närrisch, abends still."]
sy3 = 200
sh = 45 + 33 * len(facts) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in facts)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ST. MARTIN　Sint Maarten", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 facts ends", sy3 + sh)
words = ["die Laterne — lantaarn", "der Mantel — mantel", "die Gans — gans",
         "der Weckmann — broodmannetje", "das Martinsfeuer — Sint-Maartensvuur", "das Kostüm — kostuum"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "MARTINSWÖRTER　Sint Maarten", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Haben Sie schon einmal eine Laterne gebastelt? Was singen Kinder in Ihrem Land? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("Heb je een lantaarn gemaakt? Welke liedjes zingen kinderen in jouw land? Schrijf twee Duitse zinnen!", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　En u?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Heb je een lantaarn gemaakt? Welke liedjes zingen kinderen in jouw land? Schrijf twee Duitse zinnen!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 undsie ends", ey3 + eh)
tipp = "Tipp: Basteln Sie eine Laterne aus Papier — ein Glas, ein Licht, ein Lied genügt."
sy3 = ey3 + eh + 26
sh = 45 + 33 + 30.53 * len(wrap(tipp, "serif", False, 21.5, CW - 44))
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DER TIPP　Tip", 24, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, tipp, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Oefeningen pagina 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　De niveaus lopen door elkaar — vind elk antwoord op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P3-ex")
e.head("A　RICHTIG ODER FALSCH?", 25)
e.bridge("Lees het artikel op pagina 3. Juist of onjuist?")
e.ex("A2", "juist-onjuist", "Richtig", "de legende zegt dat Maarten een Romeinse soldaat was",
     "Martin war der Legende nach ein römischer Soldat. Richtig oder falsch?", instr="Beoordeel", size=20, gap=8)
e.ex("A2", "juist-onjuist", "Falsch", "de legende zegt dat de ganzen hem verraadden",
     "Die Gänse haben Martin versteckt. Richtig oder falsch?", instr="Beoordeel", size=20, gap=8)
e.ex("A2", "juist-onjuist", "Richtig", "de herdenkingsdag is 11 november",
     "Der Gedenktag des heiligen Martin ist am 11. November. Richtig oder falsch?", instr="Beoordeel", size=20, gap=8)
e.ex("B1", "juist-onjuist", "Falsch", "uitslagen van 3–8 november onbekend bij het ter perse gaan",
     "Die Ergebnisse vom 3. bis 8. November standen bei Redaktionsschluss fest. Richtig oder falsch?", instr="Beoordeel", size=20, gap=8)
e.ex("A2", "juist-onjuist", "Richtig", "carnaval begint om 11.11 uur",
     "Die Karnevalssession beginnt um 11.11 Uhr. Richtig oder falsch?", instr="Beoordeel", size=20, gap=8)
e.head("B　WÖRTER AUS DEM TEXT", 25)
e.bridge("Vul in met de woorden uit het kader.")
e.para("Mantel · Laterne · Gans · Kostüm · Martinsfeuer", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "invullen", "Mantel", "de mantel gedeeld met de bedelaar",
     "Martin teilte seinen ___ mit einem Bettler.", instr="Vul in", size=20, gap=8)
e.ex("A2", "invullen", "Laterne", "een papieren lantaarn",
     "Die Kinder basteln eine bunte ___ aus Papier.", instr="Vul in", size=20, gap=8)
e.ex("A2", "invullen", "Gans", "de Sint-Maartensgans",
     "Am Martinstag gibt es die Martins___: Gänsebraten.", instr="Vul in", size=20, gap=8)
e.ex("A2", "invullen", "Kostüm", "een carnavalskostuum",
     "In Köln tragen die Jecken ein buntes ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "invullen", "Martinsfeuer", "de optocht eindigt bij het vuur",
     "Am ___ endet der Laternenumzug.", instr="Vul in", size=20, gap=8)
e.head("C　LESEVERSTEHEN", 25)
e.bridge("Kies het juiste antwoord.")
e.ex("A2", "meerkeuze", "B", "Maarten werd later bisschop van Tours",
     "Was wurde Martin später? A. ein König · B. Bischof von Tours · C. ein Bäcker", size=20, gap=8)
e.ex("A2", "meerkeuze", "B", "lantaarnoptochten zijn vaak op avonden in de buurt",
     "Wann finden Laternenumzüge statt? A. nur am 25. Dezember · B. oft auch vor oder nach dem 11. November · C. nur im Sommer", size=20, gap=8)
e.ex("A2", "meerkeuze", "A", "Sint-Maartensgans met rodekool en knoedels",
     "Was isst man am Martinstag? A. Gänsebraten mit Rotkohl und Klößen · B. Eis · C. Pommes", size=20, gap=8)
e.ex("B1", "meerkeuze", "A", "VOL.4 meldt de uitslagen van 3–8 november",
     "Wo berichtet die Redaktion über die Spiele vom 3. bis 8. November? A. in VOL.4 · B. in dieser Ausgabe mit Ergebnissen · C. gar nicht", size=20, gap=8)
e.head("D　SÄTZE BAUEN", 25)
e.bridge("Zet de woorden in een correcte zin.")
e.ex("A2", "zinnen bouwen", "Martin teilte seinen Mantel mit einem Bettler.", "volgorde onderwerp–werkwoord–voorwerp",
     "Martin / teilte / seinen Mantel / mit einem Bettler → ___", instr="Vorm de zin", size=20, gap=8)
e.ex("B1", "zinnen bouwen", "Die Kinder basteln bunte Laternen aus Papier.", "volgorde onderwerp–werkwoord–voorwerp",
     "die Kinder / basteln / bunte Laternen / aus Papier → ___", instr="Vorm de zin", size=20, gap=8)
e.ex("A2", "zinnen bouwen", "Am 11. November beginnt die Karnevalssession in Köln.", "tijdsbepaling eerst, werkwoord tweede",
     "am 11. November / beginnt / die Karnevalssession / in Köln → ___", instr="Vorm de zin", size=20, gap=8)
e.ex("B1", "zinnen bouwen", "Am Martinsfeuer endet der Laternenumzug.", "plaats eerst, werkwoord tweede",
     "am Martinsfeuer / endet / der Laternenumzug → ___", instr="Vorm de zin", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-kultur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　Sport", "Die Lucerna", "LEVEL B1　Nationalelf & NFL　Nationale ploeg en NFL")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Zwei Ballspiele, eine Woche: Nations League und NFL", 32)
f.byline("Von der Lucerna-Sportredaktion　Leseniveau: B1")
f.para("Was für eine Woche für den Fußball! Die Bundesliga pausiert — aber die Nationalmannschaft spielt. Am Freitagabend (20.45 Uhr) trifft Deutschland in Belgrad auf Serbien. Es geht ums Viertelfinale: Deutschland hat fünf Punkte, die Niederlande und Griechenland je acht.")
f.para("Am Donnerstag, dem 5. November, nennt Bundestrainer Jürgen Klopp seinen Kader — in einem Video über die Kanäle des DFB. Am Montag, dem 9. November, reist die Mannschaft nach Herzogenaurach: Dort bereitet sie sich zum letzten Mal in der alten Ausrüstung vor.")
f.para("Das Spiel in Belgrad ist ein Geisterspiel: Das Stadion bleibt wegen einer Strafe der UEFA leer. Deutschland muss ohne Zuschauer gewinnen — nur Siege helfen. Das Hinspiel am 1. Oktober gewann Deutschland mit 2:0.")
f.para("Am Montag, dem 16. November (20.45 Uhr), folgt das zweite Spiel: Deutschland gegen die Niederlande in Berlin. Die ARD überträgt live. Das Hinspiel in Amsterdam endete 1:1 — gut möglich, dass dieses Spiel über das Viertelfinale entscheidet.")
f.para("Und dann der andere Football: Am Sonntag (15.30 Uhr) spielen in München die Detroit Lions gegen die New England Patriots — mit dem deutschen Star Amon-Ra St. Brown. Das Spiel ist ausverkauft, RTL überträgt live.")
f.para("Merken Sie sich auch die Rückkehr der Liga: Am 20. November beginnt der 10. Spieltag mit Bayern gegen Köln. Und die Europapokale kehren am 24. bis 26. November zurück.")
f.gloss("das Geisterspiel = spookwedstrijd · das Hinspiel = heenwedstrijd · ausverkauft = uitverkocht · der Star = ster · gewinnen = winnen.")
f.end_report()

# col 3: kopfball image + Und Sie
bx = COLX[3]
image(p, "kopfball.jpg", bx, 200, CW, 470)
cy3 = caption(p, bx, 670, CW, "Kopfball im Spiel: So sieht ein Duell in der Luft aus — um jeden Ball wird gekämpft. Die Nationalelf spielt in dieser Woche in Belgrad — am Montag danach in Berlin.",
              "Foto: DVIDS (Armed Forces Soccer Championship, Destin, Florida, 2010) — public domain")
ey3 = cy3 + 26
etvous = "Und Sie? Schauen Sie lieber Fußball oder American Football? Und wer gewinnt in Belgrad? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("Voetbal of American football? Wie wint in Belgrado? Schrijf twee Duitse zinnen!", "sans", False, 20, CW - 44)) - 1)
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "UND SIE?　En u?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Voetbal of American football? Wie wint in Belgrado? Schrijf twee Duitse zinnen!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "DER SPIELPLAN　Deze week en volgende week", 26, "sans", True, OLIVE)
rows = [
    ("Do 5.11.", "—", "Bundestrainer Klopp nennt den Kader (DFB-Video)"),
    ("Fr 13.11.", "20.45", "Serbien – Deutschland (Nations League, Belgrad, RTL)"),
    ("So 15.11.", "15.30", "Detroit Lions – New England Patriots (NFL, München, RTL)"),
    ("Mo 16.11.", "20.45", "Deutschland – Niederlande (Nations League, Berlin, ARD)"),
    ("Fr 20.11.", "20.30", "Bayern München – 1. FC Köln (Bundesliga, 10. Spieltag)"),
    ("Sa 21.11.", "15.30", "Borussia Mönchengladbach – Borussia Dortmund · Union Berlin – RB Leipzig"),
    ("Sa 21.11.", "15.30", "Bayer Leverkusen – SC Paderborn · Frankfurt – Hoffenheim · Elversberg – Freiburg"),
    ("Sa 21.11.", "17.30", "FC Schalke 04 – VfB Stuttgart (Topspiel)"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Alle Zeiten in MEZ (Mitteleuropäische Zeit). Am Sonntag, dem 22. November: FC Augsburg – Mainz 05 (15.30 Uhr), Werder Bremen – Hamburger SV (16.30 Uhr). In dieser Woche keine Europapokal-Spiele der Vereine — die Klubs kehren am 24. bis 26. November zurück."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1640
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Oefeningen pagina 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　De niveaus lopen door elkaar — vind elk antwoord op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P4-ex")
e.head("A　LESEVERSTEHEN", 25)
e.bridge("Lees het artikel op pagina 4 en kies het juiste antwoord.")
e.ex("B1", "meerkeuze", "B", "Duitsland 5 punten, Nederland en Griekenland elk 8",
     "Wie viele Punkte hat Deutschland nach vier Spielen? A. acht · B. fünf · C. zwei", size=20, gap=8)
e.ex("B1", "meerkeuze", "B", "de bondscoach noemt de selectie op 5 november",
     "Wann nennt Klopp seinen Kader? A. am 13. November · B. am 5. November · C. am 9. November", size=20, gap=8)
e.ex("B1", "meerkeuze", "C", "leeg stadion in Belgrado",
     "Warum ist das Spiel in Belgrad ein Geisterspiel? A. Es ist Nacht. · B. Es gibt keine Karten. · C. Das Stadion bleibt wegen einer UEFA-Strafe leer.", size=20, gap=8)
e.ex("B1", "meerkeuze", "A", "Duitsland won de heenwedstrijd met 2-0 van Servië",
     "Wie endete das Hinspiel gegen Serbien? A. 2:0 für Deutschland · B. 1:1 · C. 0:2", size=20, gap=8)
e.ex("B1", "meerkeuze", "B", "de NFL-wedstrijd in München is uitverkocht",
     "Das NFL-Spiel in München ist... A. abgesagt · B. ausverkauft · C. gratis", size=20, gap=8)
e.head("B　DIE WÖRTER", 25)
e.match_set("B1", "koppelen",
            ["das Geisterspiel", "das Hinspiel", "der Ausrüster", "ausverkauft"],
            ["das erste Spiel gegen denselben Gegner in einer Runde",
             "ein Spiel ohne Zuschauer im Stadion",
             "die Firma, die die Trikots und Schuhe liefert",
             "alle Karten sind weg, es gibt keine mehr"],
            ["b", "a", "c", "d"],
            ["Geisterspiel=spookwedstrijd b", "Hinspiel=heenwedstrijd a", "Ausrüster=tenueleverancier c", "ausverkauft=uitverkocht d"],
            instr="Combineer")
e.head("C　KOMPARATIV", 25)
e.bridge("Vul in met de vergrotende trap (het woord tussen haakjes is de stellende trap).")
e.ex("B1", "invullen", "mehr", "viel → mehr (Nederland heeft 8 punten, meer dan de 5 van Duitsland)",
     "Die Niederlande haben ___ (viel) Punkte als Deutschland.", instr="Vul in", size=20, gap=8)
e.ex("B1", "invullen", "später", "spät → später (15.30 uur is later dan 11.11 uur)",
     "Das NFL-Spiel beginnt ___ (spät) als die Karnevalseröffnung.", instr="Vul in", size=20, gap=8)
e.ex("B1", "invullen", "leiser", "leise → leiser (een leeg stadion is stiller dan een thuiswedstrijd)",
     "In Belgrad spielt Deutschland ohne Zuschauer — das ist ___ (leise) als ein Heimspiel in Berlin.", instr="Vul in", size=20, gap=8)
e.ex("B1", "invullen", "früher", "früh → früher (5 november is eerder dan 13 november)",
     "Klopp nennt den Kader ___ (früh) als das Spiel in Belgrad.", instr="Vul in", size=20, gap=8)
e.head("D　DIE UHRZEITEN", 25)
e.bridge("Kijk naar het speelschema hierboven en kies het juiste antwoord.")
e.ex("B1", "meerkeuze", "A", "Servië–Duitsland op vrijdag om 20.45 uur",
     "Serbien–Deutschland beginnt um... A. 20.45 Uhr · B. 18.45 Uhr · C. 15.30 Uhr", size=20, gap=8)
e.ex("B1", "meerkeuze", "B", "NFL op zondag om 15.30 uur",
     "Das NFL-Spiel in München beginnt um... A. 20.45 Uhr · B. 15.30 Uhr · C. 11.11 Uhr", size=20, gap=8)
e.ex("B1", "meerkeuze", "C", "Duitsland–Nederland op maandag om 20.45 uur",
     "Deutschland–Niederlande ist am Montag um... A. 15.30 Uhr · B. 17.30 Uhr · C. 20.45 Uhr", size=20, gap=8)
e.ex("B1", "meerkeuze", "A", "Bayern–Keulen op vrijdag om 20.30 uur",
     "Bayern–Köln beginnt am Freitag um... A. 20.30 Uhr · B. 15.30 Uhr · C. 18.30 Uhr", size=20, gap=8)
e.ex("B1", "meerkeuze", "B", "Schalke–Stuttgart op zaterdag om 17.30 uur",
     "Schalke–Stuttgart ist das Topspiel am Samstag um... A. 15.30 Uhr · B. 17.30 Uhr · C. 20.30 Uhr", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
