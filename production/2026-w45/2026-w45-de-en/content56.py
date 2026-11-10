# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUGEND　Youth", "Die Lucerna", "LEVEL B1　Zurück in die Schule　Back to school")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P5-main")
f.title("Zurück in die Schule — und Bayern hat noch frei", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: B1")
f.para("Am Montag, dem 2. November, war es in Baden-Württemberg wieder so weit: Die Schule hat nach den Herbstferien wieder begonnen. Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut — und die ersten Klassenarbeiten kommen bald.")
f.para("In Bayern dagegen ist die Woche noch frei: Dort dauern die Herbstferien in dieser Woche noch an. Wer in München wohnt, kann noch ausschlafen — wer in Stuttgart wohnt, muss schon wieder früh aufstehen. Ein Land, zwei Wochen: So unterschiedlich sind die Ferien in Deutschland.")
f.para("Was macht man in der ersten Schulwoche? Die Lehrerinnen und Lehrer fragen nach den Ferien, die Hefte sind neu, und die Pläne für den Winter stehen schon: Klassenarbeiten, Referate — und bald die ersten Proben für die Weihnachtsfeier.")
f.para("Und nach der Schule? Der Herbst ist die Zeit der Bibliotheken und der Sporthallen: Lesen, was man in den Ferien begonnen hat, oder ein neues Hobby probieren. Unser Tipp: Suchen Sie sich ein Buch für die dunklen Abende — die Bibliotheken haben im November oft neue Bücher und Lesungen.")
f.para("Auch der Sport gehört zur Woche: Am Samstag und Sonntag spielt die Bundesliga — für viele Jugendliche der Ausflug des Wochenendes. Wer in Bayern noch Ferien hat, kann sogar am Freitag schon ins Stadion. Mehr dazu auf Seite 4.")
f.gloss("der Pausenhof = schoolyard · die Klassenarbeit = class test · das Referat = class talk · ausschlafen = to sleep in · die Probe = rehearsal.")
f.end_report()

# col 3: facts + vocab + Und Sie (hand-rolled; CORRECTED height formula — see KIT §geometry)
ix = COLX[3]
facts = ["Baden-Württemberg: Am 2. November hat die Schule wieder begonnen.",
         "Bayern: Die Herbstferien dauern in dieser Woche noch an.",
         "Ein Land, zwei Wochen: So unterschiedlich sind die Ferien in Deutschland."]
sy3 = 200
sh = 45 + 33 * len(facts) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in facts)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "FERIENWECHSEL　Holidays", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 facts ends", sy3 + sh)
words = ["der Pausenhof — schoolyard", "die Klassenarbeit — class test", "das Referat — class talk",
         "der Rucksack — backpack", "ausschlafen — to sleep in", "die Probe — rehearsal"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SCHULWÖRTER　School words", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Wann hat Ihre Schule nach den Ferien wieder begonnen? Und was war Ihr erstes Fach? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("When was your first day back? What was your first lesson? Write two sentences!", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　And you?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "When was your first day back? What was your first lesson? Write two sentences!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- Wochenplan wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 300, fill=BOX)
p.text(sx + 24, 1162, "DER WOCHENPLAN DER REDAKTION　The editors' week", 24, "sans", True, OLIVE)
planrows = [
    ("Mo 2.11.", "Baden-Württemberg: erster Schultag nach den Ferien."),
    ("Di 3.11.", "Champions League am Abend: Bayern bei Atlético (21.00 Uhr)."),
    ("Mi 4.11.", "Dortmund gegen Betis, Leipzig gegen City (21.00 Uhr)."),
    ("Do 5.11.", "Europa League: Hoffenheim bei Crystal Palace (18.45 Uhr)."),
    ("Fr 6.11.", "Bundesliga: Hamburg gegen Gladbach (20.30 Uhr)."),
]
pyy = 1184
for t, txt in planrows:
    p.text(sx + 24, pyy + 24, t, 21, "sans", True, OLIVE)
    p.text(sx + 190, pyy + 24, txt, 21.5, "serif", False, INK)
    pyy += 45

# ---- P5 exercises ----
ey = 1500
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Page 5 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8　Levels mix freely — find each answer by its number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P5-ex")
e.head("A　LESEVERSTEHEN", 25)
e.bridge("Read the page 5 article and choose the right answer.")
e.ex("B1", "multiple choice", "A", "Baden-Württemberg back on 2 November",
     "In Baden-Württemberg beginnt die Schule am... A. 2. November · B. 8. November · C. 31. Oktober", size=20, gap=8)
e.ex("B1", "multiple choice", "B", "Bavaria holidays not over",
     "In Bayern sind die Ferien... A. vorbei · B. noch nicht vorbei · C. erst im Dezember", size=20, gap=8)
e.ex("B1", "multiple choice", "B", "class tests coming in the first week",
     "Was kommt bald in der Schule? A. die Sommerferien · B. die ersten Klassenarbeiten · C. der Abiball", size=20, gap=8)
e.ex("B1", "multiple choice", "B", "Referat = class talk",
     "Was ist ein Referat? A. ein Buch · B. ein Vortrag in der Klasse · C. ein Sportfest", size=20, gap=8)
e.ex("A2", "multiple choice", "A", "Bavarian pupils can go to the stadium on Friday",
     "Wer kann am Freitag schon ins Stadion? A. Wer in Bayern Ferien hat. · B. Wer in Stuttgart wohnt. · C. Niemand.", size=20, gap=8)
e.head("B　WÖRTER AUS DEM TEXT", 25)
e.bridge("Complete with the words from the box.")
e.para("Pausenhof · Klassenarbeit · Referat · ausschlafen · Probe · Rucksack", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "fill-in", "Pausenhof", "playing in the schoolyard",
     "In der Pause spielen die Kinder auf dem ___.", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "Klassenarbeit", "a maths class test",
     "Am Freitag schreiben wir eine ___ in Mathe.", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "Referat", "three books to read for the talk",
     "Für das ___ muss ich drei Bücher lesen.", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "ausschlafen", "sleeping in during the holidays",
     "In den Ferien kann man lange ___.", instr="Fill in", size=20, gap=8)
e.ex("A2", "fill-in", "Probe", "the first rehearsal for Christmas",
     "Für die Weihnachtsfeier gibt es schon die erste ___.", instr="Fill in", size=20, gap=8)
e.ex("A2", "fill-in", "Rucksack", "packed bag: exercise books, pens",
     "Mein ___ ist gepackt: Hefte, Stifte, Pausenbrot.", instr="Fill in", size=20, gap=8)
e.head("C　SÄTZE MIT «WEIL»", 25)
e.bridge("Join the two sentences with weil (the verb goes to the end).")
e.ex("B1", "transformation", "Die Kinder freuen sich, weil die Schule wieder beginnt.", "in a weil clause the verb goes to the end",
     "Die Kinder freuen sich. Die Schule beginnt wieder. (weil) → ___", instr="Rewrite", size=20, gap=8)
e.ex("B1", "transformation", "Er liest ein Buch, weil es draußen kalt ist.", "ist goes to the end",
     "Er liest ein Buch. Es ist draußen kalt. (weil) → ___", instr="Rewrite", size=20, gap=8)
e.ex("B1", "transformation", "Sie geht in die Bibliothek, weil sie ein Referat schreiben muss.", "muss goes to the end",
     "Sie geht in die Bibliothek. Sie muss ein Referat schreiben. (weil) → ___", instr="Rewrite", size=20, gap=8)
e.ex("B1", "transformation", "Bayern hat noch Ferien, weil die Ferien dort später liegen.", "liegen goes to the end",
     "Bayern hat noch Ferien. Die Ferien liegen dort später. (weil) → ___", instr="Rewrite", size=20, gap=8)
e.head("D　RICHTIG ODER FALSCH?", 25)
e.bridge("Right or wrong?")
e.ex("A2", "true/false", "Richtig", "Baden-Württemberg back on 2 November",
     "In Baden-Württemberg hat die Schule am 2. November wieder begonnen. Richtig oder falsch?", instr="True or false?", size=20, gap=8)
e.ex("B1", "true/false", "Falsch", "holidays not over in all of Germany",
     "In ganz Deutschland sind die Herbstferien vorbei. Richtig oder falsch?", instr="True or false?", size=20, gap=8)
e.ex("A2", "true/false", "Richtig", "tests and talks in the first week",
     "Die erste Schulwoche bringt Klassenarbeiten und Referate. Richtig oder falsch?", instr="True or false?", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jugend.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERTIEFUNG　Deep read", "Die Lucerna", "LEVEL B2　Pflege & Stromsteuer　Care and electricity tax")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P6-main")
f.title("Pflege zu Hause: Wer hilft den Angehörigen?", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: B2")
f.para("Am Montag, dem 26. Oktober, um 21.00 Uhr diskutierte die ARD-Sendung „Hart aber fair“: „Pflege zu Hause — Lässt die Politik Angehörige allein?“ Nach Angaben der Sendung brauchen in Deutschland mehr als sechs Millionen Menschen Pflege. Die meisten von ihnen werden zu Hause gepflegt — von rund zehn Millionen Angehörigen.")
f.para("Was heißt „pflegen“ im Alltag? Morgens helfen beim Aufstehen, beim Waschen und Anziehen, beim Essen und bei den Medikamenten — und nachts wach sein, wenn etwas passiert. Viele Angehörige machen das neben dem Beruf, und viele sind selbst schon alt.")
f.para("Die Politik streitet seit Jahren über die Antwort: mehr Geld für die Pflegeversicherung? Mehr Pflegedienste, die zu Hause helfen? Mehr freie Tage für pflegende Angehörige? Die Debatte ist schwierig, weil alles Geld kostet — und weil die Zahl der Pflegebedürftigen weiter steigt.")
f.para("Zweites Thema der Woche: die Stromsteuer. Union und SPD sind sich hier „weiter weit auseinander“, wie es in der Tagesschau heißt: Die eine Seite will die Steuer für alle senken, die andere nur gezielt. Auch der ZEW-Index zeigt, wie wichtig die Frage ist: Die Lage wird etwas besser eingeschätzt (minus 35,9 nach minus 47,1), aber die Erwartungen fielen im Oktober auf 28,1 Punkte.")
f.para("Und was sagt der Präsident des ZEW, Achim Wambach? „Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.“ Mit anderen Worten: Es geht langsam aufwärts — aber von allein geht es nicht.")
f.para("Zwei Debatten, ein Muster: Beide kosten Geld und betreffen fast jeden Haushalt.")
f.gloss("der Angehörige = relative · die Pflegeversicherung = care insurance · der Pflegedienst = care service · die Stagnation = stagnation · der Aufschwung = upturn.")
f.end_report()

# col 3: numbers box + debate box (measured)
ix = COLX[3]
tl = [("6 Mio.", "Menschen in Deutschland brauchen Pflege (ARD „Hart aber fair“, 26. Okt.)."),
      ("10 Mio.", "Angehörige pflegen zu Hause (rund; ARD „Hart aber fair“, 26. Okt.)."),
      ("28,1", "ZEW-Erwartungen im Oktober (minus 6,6 Punkte)."),
      ("−35,9", "ZEW-Lageindex (plus 11,2 Punkte)."),
      ("14,04", "Cent pro Liter: so viel Steuer weniger beim Tanken."),
      ("2,5 Mrd.", "so viel kostet der Tankrabatt den Staat.")]
tlh = 45 + 30.5 * len(tl) + 29.11 * sum(len(wrap(t, "serif", False, 20.5, CW - 152)) for yr, t in tl)
p.rect(ix, 200, CW, tlh, fill=BOX)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DIE ZAHLEN　Numbers", 24, "sans", True, OLIVE)
yy3 += 52
for yr, t in tl:
    p.text(ix + 22, yy3 + 21, yr, 21, "sans", True, OLIVE)
    yy3 = p.para(ix + 130, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 152, 1.42) + 10
print("P6 col3 numbers ends", 200 + tlh)
deb = "Pflege: Wer zu Hause pflegt, braucht mehr Hilfe — darüber streitet die Politik. Stromsteuer: Wie stark sie sinkt, ist noch offen. Beides kostet Geld, beides betrifft fast jeden Haushalt."
hy3 = 200 + tlh + 26
hh = 140 + 29.82 * len(wrap(deb, "serif", False, 21, CW - 44)) + 27.69 * (len(wrap("Care at home needs more help — still debated. The electricity-tax cut is still open. Both cost money and affect nearly every household.", "sans", False, 19.5, CW - 44)) - 1)
p.rect(ix, hy3, CW, hh, fill="#f0eee5")
yy3 = hy3 + 16
p.text(ix + 22, yy3 + 26, "DIE DEBATTE IN EINEM SATZ", 22.5, "sans", True, OLIVE)
yy3 += 50
yy3 = p.para(ix + 22, yy3 + 21, deb, 21, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Care at home needs more help — still debated. The electricity-tax cut is still open. Both cost money and affect nearly every household.", 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", hy3 + hh)

# ---- Pro & Contra wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 252, fill="#f0eee5")
p.text(sx + 24, 1162, "PRO & CONTRA　For and against — the arguments of the debate", 24, "sans", True, OLIVE)
p.text(sx + 24, 1210, "PRO — MEHR HILFE FÜR ANGEHÖRIGE", 21, "sans", True, OLIVE)
p.text(sx + 24 + (swd - 48) // 2, 1210, "CONTRA — GEGEN MEHR GELD", 21, "sans", True, OLIVE)
pro = ["Angehörige kennen den Menschen am besten — Hilfe zu Hause ist menschlicher.",
       "Ein Heimplatz kostet viel mehr als Hilfe zu Hause."]
contra = ["Professionelle Pflege ist sicherer — Angehörige sind oft überfordert.",
          "Der Staat hat nicht genug Geld für alles."]
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
p.text(MX, cy + 28, "WER PFLEGT ZU HAUSE?　Who cares at home?", 26, "sans", True, OLIVE)
bars = [("pflegen Angehörige zu Hause", 68, "family care"),
        ("nutzen einen Pflegedienst", 20, "care service"),
        ("leben im Pflegeheim", 12, "care home")]
byy = cy + 58
for lab, v, zh in bars:
    p.text(MX, byy + 26, lab, 22, "serif", True, INK)
    p.text(MX + 360, byy + 26, zh, 20, "sans", False, GREY)
    p.rect(MX + 470, byy + 4, v * 17, 30, fill=OLIVE)
    p.text(MX + 470 + v * 17 + 16, byy + 26, f"{v} %", 22, "sans", True, OLIVE)
    byy += 52
p.text(MX, byy + 22, "ÜBUNGSDATEN　Practice data — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Practice example, not a real survey.)", 19.5, "sans", False, GREY)

# ---- P6 exercises ----
ey = 1808
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Page 6 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8　Levels mix freely — find each answer by its number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P6-ex")
e.head("A　DAS DIAGRAMM LESEN", 25, gap=9)
e.bridge("Look at the practice chart above and choose the right answer.")
e.ex("B1", "multiple choice", "A", "68% family care",
     "Wie viele Prozent pflegen Angehörige zu Hause (Übungsdaten)? A. 68 % · B. 20 % · C. 12 %", size=20, gap=7)
e.ex("B1", "multiple choice", "B", "care service 20% is second",
     "Was ist die zweitgrößte Gruppe? A. Pflegeheim · B. Pflegedienst · C. Angehörige", size=20, gap=7)
e.ex("B1", "multiple choice", "B", "68 + 20 = 88",
     "Angehörige und Pflegedienst zusammen sind... A. 80 % · B. 88 % · C. 90 %", size=20, gap=7)
e.ex("B2", "multiple choice", "B", "care home 12% is smallest",
     "Welche Gruppe ist kleiner? A. Pflegedienst · B. Pflegeheim · C. beide gleich", size=20, gap=7)
e.ex("B1", "multiple choice", "A", "care home 12%",
     "Wie viele Prozent leben im Pflegeheim? A. 12 % · B. 20 % · C. 68 %", size=20, gap=7)
e.ex("B2", "multiple choice", "B", "68 + 20 + 12 = 100",
     "Die drei Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 %", size=20, gap=7)
e.head("B　LESEVERSTEHEN (B2)", 25, gap=9)
e.bridge("Read the page 6 deep-read article and choose the right answer.")
e.ex("B2", "multiple choice", "B", "the 26 October program discussed care at home",
     "Was diskutierte „Hart aber fair“ in der Sendung am 26. Oktober? A. den Tankrabatt · B. die Pflege zu Hause · C. die Stromsteuer", size=20, gap=7)
e.ex("B2", "multiple choice", "A", "per the ARD program Hart aber fair on 26 October, over six million people need care",
     "Wie viele Menschen brauchen Pflege? A. mehr als sechs Millionen · B. rund eine Million · C. zehn Millionen", size=20, gap=7)
e.ex("B2", "multiple choice", "B", "relatives care at home",
     "Wer pflegt zu Hause? A. die Ärzte · B. die Angehörigen · C. die Politiker", size=20, gap=7)
e.ex("B1", "multiple choice", "B", "per the ARD program Hart aber fair on 26 October, about ten million people care for relatives",
     "Wie viele Menschen pflegen einen Verwandten (rund)? A. sechs Millionen · B. zehn Millionen · C. zwei Millionen", size=20, gap=7)
e.head("C　GRAMMATIK", 25, gap=9)
e.bridge("Fill in with the form in brackets.")
e.ex("B2", "fill-in", "wird", "passive: wird + past participle",
     "Die Frage ___ (werden) am Montag diskutiert.", instr="Fill in", size=20, gap=7)
e.ex("B2", "fill-in", "ob", "ob introduces an indirect question",
     "Die Politik weiß nicht, ___ das Geld reicht.", instr="Fill in", size=20, gap=7)
e.ex("B1", "fill-in", "steigt", "steigen → steigt",
     "Die Zahl der Pflegebedürftigen ___ (steigen) weiter.", instr="Fill in", size=20, gap=7)
e.ex("B2", "fill-in", "sagte", "sagen in the past: sagte",
     "Wambach ___ (sagen): Der Aufschwung trägt sich nicht selbst.", instr="Fill in", size=20, gap=7)
e.head("D　WÖRTER DER DEBATTE", 25, gap=9)
e.bridge("Complete with the words from the box.")
e.para("Pflegeversicherung · Angehörige · Stagnation · Aufschwung", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "fill-in", "Pflegeversicherung", "care insurance should pay more",
     "Die ___ soll mehr Geld für die Pflege zahlen.", instr="Fill in", size=20, gap=7)
e.ex("B2", "fill-in", "Angehörige", "relatives care at home",
     "Viele ___ pflegen ihre Verwandten zu Hause.", instr="Fill in", size=20, gap=7)
e.ex("B2", "fill-in", "Stagnation", "coming out of stagnation",
     "Die Wirtschaft kommt langsam aus der ___ heraus.", instr="Fill in", size=20, gap=7)
e.ex("B1", "fill-in", "Aufschwung", "the upturn not yet self-sustaining",
     "Der ___ trägt sich noch nicht selbst.", instr="Fill in", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-vertiefung.svg")
print("P6 saved, exercises so far:", len(REG))
