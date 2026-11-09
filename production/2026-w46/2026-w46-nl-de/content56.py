# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JONGEREN (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JONGEREN　JUGENDLICHE", "De Lucerna", "NIVEAU B1　Robinson, de schoen en het verlanglijstje　Robinson, der Schuh und der Wunschzettel")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Robinson op zondag — en de schoen staat klaar", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4. Negentien bekende Nederlanders en Vlamingen leven 34 dagen op een onbewoond eiland in Maleisië. Nicolette Kluijver en Edson da Graça presenteren het programma, Camille Vanuxem is de verslaggever.")
f.para("De kandidaten slapen buiten en moeten alles zelf doen: vuur maken, eten zoeken, proeven winnen. Wie een proef verliest, kan naar huis worden gestemd. Wie het langst blijft, wint de expeditie. Het seizoen begon op zondag 1 november — en elke week wordt het spel harder.")
f.para("Deze week is zondag 15 november een drukke dag: overdag de intocht in Amsterdam, 's avonds een nieuwe aflevering van Robinson. En na de intocht mag de schoen. Ook jongeren zetten hun schoen — met een verlanglijstje erin, in plaats van alleen een tekening.")
f.para("Een verlanglijstje schrijven is ook Nederlands oefenen: schrijf in het Nederlands wat je wilt, waarom je het wilt en voor wie je het nog meer opschrijft. Sinterklaas leest Nederlands, zeggen kinderen — en de redactie ook.")
f.head("JONGEREN EN DE SCHOEN", 25)
f.para("De schoen zetten is niet alleen voor kleine kinderen. Jongeren zetten hun schoen met een wortel voor het paard, een tekening — of een verlanglijstje met drie wensen. Klein of groot, een wens op papier is het begin van Sinterklaas.")
f.box("ZO KIJK JE ROBINSON", [
    ("1. Kijk zondag om 20:00 uur op RTL 4 (sonntags 20:00 Uhr auf RTL 4 ansehen)", "serif", False, INK, 21, 1.36),
    ("2. Let op de proeven: daar worden de punten verdeeld (auf die Prüfungen achten: Punkte gibt es dort)", "serif", False, INK, 21, 1.36),
    ("3. Raad met vrienden wie het langst blijft (mit Freunden raten, wer am längsten bleibt)", "serif", False, INK, 21, 1.36),
    ("4. Zet daarna je schoen: met een verlanglijstje erin (dann Schuh hinstellen, Wunschzettel darin)", "serif", False, INK, 21, 1.36),
])
f.gloss("het verlanglijstje = Wunschzettel · de verslaggever = Reporter · de proef = Prüfung · stemmen = abstimmen · de aflevering = Folge.")
f.end_report()

# col 3: facts + en jij (sequential, measured; no photo this page)
ix = COLX[3]
facts = ["Expeditie Robinson: 19 kandidaten; elke zondag 20:00 uur, RTL 4.",
         "34 dagen op een onbewoond eiland in Maleisië; presentatie: Nicolette Kluijver en Edson da Graça.",
         "Na de intocht (15 november) mag de schoen, met een wortel en een verlanglijstje."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 64
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "JONGEREN IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Kijk jij zondag naar Expeditie Robinson, of zet je liever je schoen met een verlanglijstje? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Am Sonntag: Schaust du Expeditie Robinson, oder stellst du lieber deinen Schuh mit Wunschzettel hin? Schreibe zwei Sätze auf Niederländisch und schicke sie ein.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ?　UND DU?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Am Sonntag: Schaust du Expeditie Robinson, oder stellst du lieber deinen Schuh mit Wunschzettel hin? Schreibe zwei Sätze auf Niederländisch und schicke sie ein.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　ÜBUNGEN AUF SEITE 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8　Niveaus gemischt; Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Lies den Artikel auf Seite 5 und wähle die richtige Antwort.")
e.ex("B1", "wählen", "B", "Robinson läuft jeden Sonntag um 20:00 Uhr auf RTL 4",
     "Expeditie Robinson is elke zondag om... A. 18:00 uur · B. 20:00 uur · C. 12:00 uur", size=20, gap=8)
e.ex("B1", "wählen", "A", "19 Kandidaten",
     "Expeditie Robinson heeft ___ kandidaten. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "wählen", "C", "Die Sendung wird auf einer unbewohnten Insel in Malaysia gedreht",
     "De kandidaten leven op een eiland in... A. Spanje · B. Grave · C. Maleisië", size=20, gap=8)
e.ex("B1", "wählen", "B", "Die Kandidaten verbringen 34 Tage auf der Insel",
     "De kandidaten blijven ___ dagen op het eiland. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "wählen", "A", "Ein Wunschzettel kommt in den Schuh",
     "Jongeren zetten hun schoen met... A. een verlanglijstje · B. een boek · C. een lampion", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("Ergänze mit den Wörtern aus dem Kasten.")
e.para("verlanglijstje · verslaggever · proef · stemmen · aflevering · kandidaat", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "ergänzen", "verlanglijstje", "verlanglijstje = Wunschzettel, het-Wort",
     "In mijn schoen zit een ___ met drie wensen.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "verslaggever", "verslaggever = Reporter, de-Wort",
     "Camille Vanuxem is de ___ van het programma.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "proef", "proef = Prüfung, de-Wort",
     "Wie een ___ verliest, kan naar huis gaan.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "stemmen", "stemmen = abstimmen",
     "De kandidaten ___ wie naar huis moet.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "aflevering", "aflevering = Folge",
     "Zondag is er een nieuwe ___ van Robinson.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "kandidaten", "kandidaat, Plural: kandidaten",
     "Er zijn 19 ___ op het eiland.", instr="Einsetzen", size=20, gap=8)
e.head("C　DE TOEKOMST MET GAAN", 25)
e.bridge("Sprich mit gaan + Infinitiv über die Zukunft.")
e.ex("B1", "ergänzen", "gaat winnen", "gaat winnen = wird gewinnen, nur vermutet",
     "Wie ___ (winnen) Expeditie Robinson, denk je?", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "gaan kijken", "wij → gaan + Infinitiv kijken",
     "Wij ___ (kijken) zondag naar de nieuwe aflevering.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "gaat zetten", "hij → gaat zetten",
     "Hij ___ (zetten) zondagavond zijn schoen.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "gaan schrijven", "zij (Plural) → gaan schrijven",
     "De kinderen ___ (schrijven) een verlanglijstje.", instr="Einsetzen", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "richtig/falsch", "Waar", "Richtig: Die Sendung begann am 1. November",
     "Expeditie Robinson begon op 1 november. Waar of niet waar?", instr="Richtig oder falsch?", size=20, gap=8)
e.ex("B1", "richtig/falsch", "Niet waar", "Falsch: Die Sendung wird in Malaysia gedreht",
     "Expeditie Robinson speelt in Spanje. Waar of niet waar?", instr="Richtig oder falsch?", size=20, gap=8)
e.ex("B2", "richtig/falsch", "Niet waar", "Falsch: Die Karotte im Schuh ist für das Pferd",
     "De wortel in de schoen is voor Sinterklaas. Waar of niet waar?", instr="Richtig oder falsch?", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jongeren.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · VERDIEPING (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERDIEPING　VERTIEFUNG", "De Lucerna", "NIVEAU B2　Sint-Maarten of Halloween?　Martinstag oder Halloween?")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P6-main")
f.title("Sint-Maarten of Halloween: moet je kiezen?", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B2")
f.para("Sint-Maarten is een oude traditie in Nederland. Kinderen lopen al meer dan honderd jaar met lampionnen langs de deuren. Halloween is nieuwer in Nederland — en het groeit: volgens onderzoeksbureau Motivaction vierde in 2025 26 procent van de Nederlanders Halloween, tegenover 21 procent een jaar eerder.")
f.para("Maar let op de cijfers: de onderzoeken gebruiken verschillende definities en zijn daarom niet rechtstreeks vergelijkbaar. En een lege stoep betekent niet automatisch dat Sint-Maarten verdwijnt. In sommige plaatsen verplaatst de viering zich naar winkelcentra en georganiseerde optochten, waar kinderen samen langs deelnemende winkels lopen.")
f.para("Deskundigen zien Sint-Maarten niet verdwijnen. Antropoloog Irene Stengs van het Meertens Instituut zei in 2025 dat de belangstelling voor Sint-Maarten is toegenomen. Traditiedeskundige Ineke Strouken ziet geen duidelijke landelijke achteruitgang. Het feest verandert, zeggen zij — het verdwijnt niet.")
f.para("De twee feesten zijn ook anders. Halloween draait om griezelen en verkleden; Sint-Maarten draait om delen en aandacht voor anderen. Veel kinderen doen allebei: griezelen op 31 oktober, zingen op 11 november. Kiezen hoeft niet — het zijn twee feesten, in twee weken, met twee soorten licht.")
f.para("Een traditie leeft als mensen haar blijven vieren. Op straat, in het winkelcentrum of allebei: de lampion gaat aan als het donker wordt, en het liedje klinkt bij elke deur.")
f.head("VOOR OF TEGEN KIEZEN?", 25)
f.para("Voorstanders van kiezen zeggen: één feest is genoeg, anders wordt november één lange verkleedweek. Tegenstanders zeggen: feesten groeien naast elkaar, zoals talen naast elkaar groeien. De krant kiest niet: vier wat je viert — maar zing op 11 november in ieder geval één liedje.")
f.gloss("de traditie = Tradition · griezelen = erschrecken · de belangstelling = Interesse · de achteruitgang = Rückgang · de deskundige = Experte.")
f.end_report()

# col 3: OEFENDATA chart + pro/contra box (sequential, measured)
ix = COLX[3]
rows = [
    ("Ik loop met een lampion", "40", 160),
    ("Ik vier Halloween", "25", 100),
    ("Ik doe allebei", "20", 80),
    ("Ik blijf thuis", "15", 60),
]
cap = "OEFENDATA — verzonnen cijfers om mee te oefenen, geen echte enquête. Vraag: wat doe jij rond 11 november? (100 jongeren)"
capcn = "Übungsdaten: erfundene Zahlen, keine echte Umfrage. Frage: Was machst du um den 11. November? (100 Jugendliche)"
ch = 62 + len(rows) * 58 + 14 + len(wrap(cap, "serif", False, 19, CW - 44)) * 27 + 6 + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
p.rect(ix, 200, CW, ch, fill=BOX)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DE GRAFIEK　ÜBUNGSDATEN", 24, "sans", True, OLIVE)
yy3 += 58
for lab, val, bw in rows:
    p.text(ix + 22, yy3 + 20, lab, 19.5, "serif", True, INK)
    p.text(ix + CW - 22, yy3 + 20, val, 19.5, "sans", True, OLIVE, anchor="end")
    p.rect(ix + 22, yy3 + 30, bw, 18, fill=OLIVE)
    yy3 += 58
yy3 += 14
yy3 = p.para(ix + 22, yy3 + 19, cap, 19, "serif", False, GREY, CW - 44, 1.36)
yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, CW - 44, 1.32) + 6
print("P6 chart ends", 200 + ch, "content to", yy3)
by6 = 200 + ch + 26
bt = [
    ("Voor kiezen: één feest is genoeg in november.", "serif", False, INK, 21, 1.4),
    ("Tegen kiezen: feesten groeien naast elkaar, zoals talen.", "serif", False, INK, 21, 1.4),
    ("De krant kiest niet: vier wat je viert. En zing op 11 november één liedje. En jij?", "serif", False, INK, 21, 1.4),
]
bh = 62 + sum(len(wrap(t, "serif", False, 21, CW - 44)) * 29.5 + 8 for t, *_ in bt) + 16 + 30
p.rect(ix, by6, CW, bh, fill="#f0eee5")
yy3 = by6 + 16
p.text(ix + 22, yy3 + 26, "VOOR OF TEGEN?　PRO UND KONTRA", 21, "sans", True, OLIVE)
yy3 += 52
for t, k, b, fl, s, lh in bt:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.4) + 8
print("P6 col3 ends", by6 + bh)

# ---- P6 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　ÜBUNGEN AUF SEITE 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8　Niveaus gemischt; Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEES DE GRAFIEK", 25)
e.bridge("Antworte mit der Grafik auf Seite 6 (Übungsdaten).")
e.ex("B2", "ergänzen", "40", "40 Jugendliche mit Laterne",
     "___ van de 100 jongeren lopen met een lampion.", instr="Einsetzen", size=21.5, gap=9)
e.ex("B2", "ergänzen", "25", "25 feiern Halloween",
     "___ jongeren vieren Halloween.", instr="Einsetzen", size=21.5, gap=9)
e.ex("B2", "ergänzen", "60", "40 + 20 = 60",
     "Lampion lopen en allebei samen: ___ jongeren.", instr="Einsetzen", size=21.5, gap=9)
e.ex("B2", "ergänzen", "15", "15 bleiben zu Hause",
     "___ jongeren blijven thuis.", instr="Einsetzen", size=21.5, gap=9)
e.ex("B2", "ergänzen", "100", "Die Grafik zählt 100 Personen: 40+25+20+15",
     "De grafiek telt in totaal ___ jongeren.", instr="Einsetzen", size=21.5, gap=9)
e.head("B　BEGRIJPEN", 25)
e.bridge("Lies den Artikel auf Seite 6 und wähle die richtige Antwort.")
e.ex("B2", "wählen", "B", "2025 feierten 26 % der Niederländer Halloween",
     "Volgens Motivaction vierde in 2025 ___ procent Halloween. A. 21 · B. 26 · C. 11", size=21.5, gap=9)
e.ex("B2", "wählen", "B", "Die zwei Umfragen nutzen verschiedene Definitionen, man kann sie nicht direkt vergleichen",
     "De onderzoeken zijn... A. precies hetzelfde · B. niet rechtstreeks vergelijkbaar · C. allebei fout", size=21.5, gap=9)
e.ex("B2", "wählen", "C", "Das Interesse am Martinstag nahm zu, so Stengs 2025",
     "Irene Stengs zei in 2025 dat de belangstelling voor Sint-Maarten... A. verdween · B. gelijk bleef · C. is toegenomen", size=21.5, gap=9)
e.ex("B2", "wählen", "A", "Halloween geht um Gruseln, Martinstag um Teilen",
     "Halloween draait om griezelen; Sint-Maarten draait om... A. delen · B. voetbal · C. boeken", size=21.5, gap=9)
e.ex("B2", "wählen", "B", "Eine Tradition lebt, wenn Menschen sie weiter feiern",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=21.5, gap=9)
e.head("C　WOORDEN", 25)
e.bridge("Ergänze mit den Wörtern aus dem Kasten.")
e.para("traditie · griezelen · belangstelling · achteruitgang", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B2", "ergänzen", "traditie", "traditie = Tradition, de-Wort",
     "Sint-Maarten is een oude ___.", instr="Einsetzen", size=21.5, gap=9)
e.ex("B2", "ergänzen", "griezelen", "griezelen = erschrecken",
     "Met Halloween gaan kinderen ___ en zich verkleden.", instr="Einsetzen", size=21.5, gap=9)
e.ex("B2", "ergänzen", "belangstelling", "belangstelling = Interesse, de-Wort",
     "De ___ voor Sint-Maarten is toegenomen.", instr="Einsetzen", size=21.5, gap=9)
e.ex("B2", "ergänzen", "achteruitgang", "achteruitgang = Rückgang, de-Wort",
     "Strouken ziet geen duidelijke landelijke ___.", instr="Einsetzen", size=21.5, gap=9)
e.head("D　MAAK DE ZINNEN", 25)
e.bridge("Bringe die Wörter in die richtige Reihenfolge.")
e.ex("B2", "Sätze bilden", "Sint-Maarten is een oude traditie in Nederland.", "Subjekt + Verb + Ergänzung + Ort",
     "sint-maarten / is / een oude traditie / in nederland → ___", instr="Bilde den Satz", size=21.5, gap=9)
e.ex("B2", "Sätze bilden", "De kinderen lopen met lampionnen langs de deuren.", "Subjekt + Verb + Art und Weise + Ort",
     "de kinderen / lopen / met lampionnen / langs de deuren → ___", instr="Bilde den Satz", size=21.5, gap=9)
e.ex("B2", "Sätze bilden", "Een traditie leeft als mensen haar blijven vieren.", "Der als-Satz steht am Ende",
     "een traditie / leeft / als mensen haar blijven vieren → ___", instr="Bilde den Satz", size=21.5, gap=9)
e.ex("B2", "Sätze bilden", "Kiezen hoeft niet: het zijn twee feesten.", "kiezen + hoeft niet + Erklärung",
     "kiezen / hoeft niet / het zijn twee feesten → ___", instr="Bilde den Satz", size=21.5, gap=9)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-verdieping.svg")
print("P6 saved, exercises so far:", len(REG))
