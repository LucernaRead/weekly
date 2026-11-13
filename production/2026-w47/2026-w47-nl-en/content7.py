# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · TAAL (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("TAAL　LANGUAGE", "De Lucerna", "Language focus　Drie niveaus, drie gereedschappen　Three levels, three tools")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　VOETBALWOORDEN", 24)
a.para("De woorden van deze week horen bij het voetbal: de wedstrijd, de groepswinst, de kwartfinale en scoren. De wedstrijd is maandag in Berlijn: Duitsland tegen Nederland. De groepswinst is de eerste plaats in de groep.", 21.5)
a.para("En scoren: wie een doelpunt maakt, scoort. Nederland maakte 7 doelpunten in vier wedstrijden — meer dan Griekenland (5). Daarom staat Oranje bovenaan. Onthoud ook: de schoen staat klaar voor Sinterklaas.", 21.5)
a.bridge("de wedstrijd match; de groepswinst group win; de kwartfinale quarter-final; scoren to score.")
a.ex("A2", "complete", "wedstrijd", "de wedstrijd = match",
     "Duitsland – Nederland is een belangrijke ___.", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "complete", "groepswinst", "de groepswinst = group win",
     "Wie pakt de ___ in groep 2?", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "choice", "B", "Group win means finishing first in the group",
     "«De groepswinst» is... A. een boek · B. de eerste plaats in de groep · C. een liedje", size=20.5, gap=10)
a.ex("A2", "complete", "scoorde", "Past tense of scoren: scoorde",
     "Nederland ___ (scoren) 7 keer in vier wedstrijden.", instr="Fill in", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　DE VERLEDEN TIJD", 24)
b.para("Nederlands vertelt over het verleden met de verleden tijd: spelen wordt speelde, winnen wordt won, verliezen wordt verloor, maken wordt maakte. Voorbeeld: «PSV won met 2–5 van Cambuur.» «Feyenoord verloor met 5–3 bij Heerenveen.»", 21.5)
b.para("Let op: sommige werkwoorden zijn onregelmatig — winnen/won, verliezen/verloor. Andere zijn regelmatig: spelen/speelde, maken/maakte. Oefen met de uitslagen van deze week.", 21.5)
b.bridge("speelde played; won won; verloor lost; maakte scored. The past tense talks about things that already happened.")
b.ex("B1", "complete", "won", "winnen past tense: won",
     "PSV ___ (winnen) met 2–5 van Cambuur.", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "complete", "verloor", "verliezen past tense: verloor",
     "Feyenoord ___ (verliezen) met 5–3 bij Heerenveen.", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "complete", "speelde", "spelen past tense: speelde",
     "Ajax ___ (spelen) 2–2 tegen Twente.", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "choice", "B", "won is the past tense of winnen",
     "«Won» is de verleden tijd van... A. spelen · B. winnen · C. verliezen", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　BIJZINNEN MET OMDAT", 24)
c.para("Met «omdat» zeg je waarom iets gebeurt: «Oranje staat bovenaan, omdat het meer doelpunten maakte.» «Sinterklaas komt 's nachts, omdat de kinderen dan slapen.» De bijzin met «omdat» staat achteraan; het werkwoord staat dan helemaal achteraan in de bijzin.", 21.5)
c.para("Voorbeeld: «Ik zet mijn schoen, omdat ik een cadeautje wil.» «Het feest verandert, omdat mensen anders vieren.» Een omdat-zin is geen vraag — het is een reden: dit gebeurt, omdat dat.", 21.5)
c.bridge("omdat because; omdat het meer doelpunten maakte because it scored more goals; omdat ik een cadeautje wil because I want a present.")
c.ex("B2", "complete", "omdat", "omdat = because",
     "Oranje staat bovenaan, ___ het meer doelpunten maakte.", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "choice", "B", "An omdat-clause gives a reason, not a question",
     "«Ik zet mijn schoen, omdat ik een cadeautje wil» is... A. een vraag · B. een reden · C. een bevel", size=20.5, gap=10)
c.ex("B2", "complete", "wil", "The verb goes at the end of the omdat-clause: wil",
     "Ik zet mijn schoen, omdat ik een cadeautje ___.", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "complete", "maakte", "In the omdat-clause, maakte goes last",
     "Oranje staat bovenaan, omdat het meer doelpunten ___.", instr="Fill in", size=20.5, gap=10)
c.end_report()

# ---- col 3: pas op + het woord + brieven ----
bx = COLX[3]
errs = [
    ("«De Oranje speelt maandag.»", "→ Fout: Oranje is een naam, zonder lidwoord: «Oranje speelt maandag.»", "Oranje is a proper name, so it takes no article."),
    ("«Ik zet een schoen.»", "→ «De schoen zetten» vraagt een bezittelijk woord: «Ik zet mijn schoen.»", "mijn schoen = my shoe."),
    ("«PSV winnen met 2–5.»", "→ De verleden tijd van winnen is won: «PSV won met 2–5.»", "The past tense of winnen is won."),
    ("«Omdat het regent, ik blijf thuis.»", "→ Na de omdat-zin staat het werkwoord vooraan: «... blijf ik thuis.»", "After an omdat-clause, the main-clause verb comes first: blijf ik thuis."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 192
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "PAS OP!　WATCH OUT", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 18
wt = "«de groepswinst» betekent: de eerste plaats in de groep. Wie de groepswinst pakt, gaat als nummer één naar de kwartfinales."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("groepswinst = group win: first in the group, and the winner goes to the quarter-finals.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "HET WOORD　WORD OF THE WEEK", 20, "sans", True, OLIVE)  # D5: 23 -> 20 — advance 438.5px > box 400.5
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "groepswinst = group win: first in the group, and the winner goes to the quarter-finals.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 18
lt = "«Hallo! Ik ben Anna en ik leer Nederlands. Maandag kijk ik naar Oranje tegen Duitsland — en daarna zet ik mijn schoen!» — Anna (voorbeeldbrief van de redactie)"
dt_nl = "Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.5."
dt_zh = "No letters or best P8 texts yet — an example; VOL.5 next."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(dt_nl, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(dt_zh, "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap("Editor's example, not a real letter. Send yours — we print them in VOL.5!", "sans", False, 20, CW - 44)) * 29 + 34 + 50
# +50 measured correction carried from W45 Fix-1 (rendered spacing runs above formula).
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "BRIEVEN VAN LEZERS", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, dt_nl, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Editor's example, not a real letter. Send yours — we print them in VOL.5!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- P7 photo (W47: every page carries a public-domain image) ----
ix7, iw7 = span_x(0, 2)
image(p, "boeken.jpg", ix7, 1580, iw7, 240)
cy7 = caption(p, ix7, 1820, iw7, "Boeken in een boekwinkel. In november leest heel Nederland Het diner — gratis in de bibliotheek.",
              "Foto: Cristina Gottardi / Unsplash — CC0")
print("P7 photo ends", cy7)

# ---- zinnen van de week (verbatim from this issue) ----
fy = 1951
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "ZINNEN VAN DE WEEK　SENTENCES OF THE WEEK (VERBATIM FROM THIS ISSUE)", 27, "sans", True, OLIVE)
quotes = [
    ("«Op maandag 16 november speelt Oranje in Berlijn tegen Duitsland»", "On Monday 16 November, Oranje play Germany in Berlin.", "Pagina 1"),
    ("«Na vier wedstrijden staan Nederland en Griekenland samen bovenaan met 8 punten»", "After four matches, the Netherlands and Greece top the table together on 8 points.", "Pagina 1"),
    ("«Op zaterdag 5 december is het pakjesavond: de avond met de grote cadeaus»", "Saturday 5 December is Pakjesavond: the evening of the big presents.", "Pagina 2"),
    ("«Op zaterdag 14 november kwam Sinterklaas officieel aan in Nederland»", "On Saturday 14 November, Sinterklaas officially arrived in the Netherlands.", "Pagina 3"),
    ("«Nederland staat eerste, omdat het meer doelpunten maakte: 7 tegen 5»", "The Netherlands are first because they scored more goals: 7 against 5.", "Pagina 4"),
    ("«Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4»", "Every Sunday at 20:00, Expeditie Robinson is on RTL 4.", "Pagina 5"),
    ("«Sinterklaas is een oud feest in Nederland»", "Sinterklaas is an old Dutch festival.", "Pagina 6"),
    ("«Een traditie leeft als mensen haar blijven vieren»", "A tradition lives on when people keep celebrating it.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 90 + (16 if (i % 4) >= 3 else 0)
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- volgende week ----
py = 2439
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "VOLGENDE WEEK　NEXT WEEK (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Dinsdag 24 november is er Europees voetbal: Real Madrid – PSV en Feyenoord – FC Porto. Zondag 29 november is het Feyenoord – Ajax. En zaterdag 5 december is het pakjesavond. Verder: jullie brieven en de beste teksten van pagina 8. Tot maandag!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-taal.svg")
print("P7 saved, exercises so far:", len(REG))
