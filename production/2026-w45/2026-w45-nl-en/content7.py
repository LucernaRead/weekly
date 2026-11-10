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
a.head("A2　KLIMAATWOORDEN", 24)
a.para("De woorden van deze week horen bij de Klimaatweek: het klimaat, de boom planten, besparen en de waarschuwing. Het klimaat is het weer en de natuur over een lange tijd — niet het weer van vandaag.", 21.5)
a.para("En de codes: geel is let op, oranje is gevaarlijk, rood is blijf binnen. Onthoud ook: een waarschuwing geldt voor jouw eigen omgeving.", 21.5)
a.bridge("het klimaat = climate (long-term); een boom planten = to plant a tree; besparen = to save; de waarschuwing = warning.")
a.ex("A2", "complete", "planten", "wij → planten",
     "In de Klimaatweek ___ (planten) wij een boom.", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "complete", "bespaar", "je → bespaar",
     "Met de fiets ___ (besparen) je energie.", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "choice", "B", "Climate is the weather and nature over a long time",
     "«Het klimaat» is... A. het weer van vandaag · B. het weer en de natuur over een lange tijd · C. een museum", size=20.5, gap=10)
a.ex("A2", "complete", "blijf", "rood = stay indoors",
     "Code rood betekent: ___ binnen.", instr="Fill in", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　SCHEIDBARE WERKWOORDEN", 24)
b.para("Deze week doen we iets met scheidbare werkwoorden: meedoen (deed mee, meegedaan), opruimen (ruimde op, opgeruimd) en vastzetten (zette vast, vastgezet). Het eerste deel gaat in de zin naar het einde.", 21.5)
b.para("Voorbeeld: «Ik doe mee aan de Klimaatweek.» «Wij hebben de tuin opgeruimd.» «Zij zette de losse spullen vast.» Let op de volgorde: het deel staat achteraan.", 21.5)
b.bridge("meedoen = to take part: ik doe mee; opruimen = to tidy up: wij hebben opgeruimd; vastzetten = to secure: zij zette vast.")
b.ex("B1", "complete", "doe mee", "ik → doe mee",
     "Ik ___ (meedoen) aan de Klimaatweek.", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "complete", "opgeruimd", "opruimen past participle: opgeruimd",
     "Wij hebben de tuin ___ (opruimen).", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "complete", "zette vast", "vastzetten past tense: zette vast",
     "Zij ___ (vastzetten) de losse spullen.", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "choice", "B", "meedoen = to take part",
     "«Meedoen» betekent... A. meekijken · B. deelnemen, erbij zijn · C. weggaan", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　EEN MENING GEVEN", 24)
c.para("Over het klimaat heeft iedereen een mening. Beleefd geef je die zo: «Ik vind dat ...», «Volgens mij ...» of «Het lijkt me dat ...» Zo praat je mee over de Klimaatweek én over de codes van het KNMI.", 21.5)
c.para("Voorbeeld: «Volgens mij moet iedereen meedoen.» «Het lijkt me dat lokaal waarschuwen beter is.» Een mening is geen feit — zeg er dus bij dat het jouw mening is.", 21.5)
c.bridge("Ik vind dat… = I think that…; Volgens mij… = In my opinion…; Het lijkt me dat… = It seems to me that…")
c.ex("B2", "complete", "Volgens", "Volgens mij… = In my opinion…",
     "___ mij moet iedereen meedoen aan de Klimaatweek.", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "choice", "B", "Ik vind dat… expresses an opinion",
     "«Ik vind dat iedereen moet meedoen» is... A. een bevel · B. een mening · C. een vraag", size=20.5, gap=10)
c.ex("B2", "complete", "lijkt", "Het lijkt me dat… = It seems to me that…",
     "Het ___ me dat lokaal waarschuwen beter is.", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "complete", "mij", "Volgens mij… = In my opinion…",
     "Volgens ___ is fietsen beter dan autorijden.", instr="Fill in", size=20.5, gap=10)
c.end_report()

# ---- col 3: pas op + het woord + brieven ----
bx = COLX[3]
errs = [
    ("«Het klimaat is slecht weer.»", "→ Fout: het klimaat is het weer over een lange tijd.", "Long-term weather, not today's."),
    ("«Ik doe mee aan de klimaatweek.»", "→ «Klimaatweek» krijgt een hoofdletter: het is een naam.", "Klimaatweek is a name: capital K."),
    ("«Ik plant een bomen.»", "→ «Een» is enkelvoud: «een boom» of «bomen».", "«Een» is singular: «een boom» or «bomen»."),
    ("«Omdat het regent, ik blijf thuis.»", "→ Na «omdat» staat het werkwoord op plaats 2: «... blijf ik thuis.»", "Main-clause verb second: blijf ik."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 192
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "PAS OP!　ERROR CLINIC", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 18
wt = "«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("meedoen = to take part.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "HET WOORD　WORD OF THE WEEK", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "meedoen = to take part.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 18
lt = "«Hallo! Ik ben Li en ik leer Nederlands in Shanghai. In de Klimaatweek plant ik een boom op mijn balkon!» — Li (voorbeeldbrief van de redactie)"
# Fix-1 disclosure (independent proof Problem 2): on-page, Dutch + matching Chinese.
# No real letters/best P8 texts had arrived by press time, so the labeled example
# stands and the promise carries to VOL.3. Existing labeling/invitation kept verbatim.
dt_nl = "Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3."
dt_en = "No real letters or best page-8 texts yet — hence this example; promise carries to VOL.3."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(dt_nl, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(dt_en, "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap("Editors' example — not real. Send your real letters and best page-8 texts: we will print them in VOL.3!", "sans", False, 20, CW - 44)) * 29 + 34 + 50
# +50 measured correction: rendered inter-paragraph spacing runs ~20px above the
# formula per added paragraph (verified on the rendered SVG: last baseline sat
# 21px below the box edge before this correction).
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "BRIEVEN VAN LEZERS", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, dt_nl, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, dt_en, 20, "sans", False, GREY, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Editors' example — not real. Send your real letters and best page-8 texts: we will print them in VOL.3!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- zinnen van de week (verbatim from this issue) ----
# Fix-1 layout only: fy moved down for the taller BRIEVEN box; row pitch
# 158 -> 90 (rows have ~77px of content from quote top to Chinese descender,
# so 90px still leaves a clear gap); no quote text changed.
fy = 1951
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "ZINNEN VAN DE WEEK　PHRASES OF THE WEEK (VERBATIM FROM THIS ISSUE)", 27, "sans", True, OLIVE)
quotes = [
    ("«Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland»", "From Monday 2 to Sunday 8 November, it is Climate Week in the Netherlands.", "Pagina 1"),
    ("«De herfst is de beste tijd om te planten»", "Autumn is the best time to plant.", "Pagina 1"),
    ("«Geel betekent: let op, het weer kan gevaarlijk zijn»", "Yellow means: take care, the weather may be dangerous.", "Pagina 2"),
    ("«Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts»", "More than 70 museums are open from 19:00 in the evening to 02:00 at night.", "Pagina 3"),
    ("«Ajax won donderdag 22 oktober met 2–0 van Atalanta»", "On Thursday 22 October Ajax beat Atalanta 2–0.", "Pagina 4"),
    ("«Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur»", "On Sunday 1 November Expeditie Robinson started on RTL 4, at 20:00.", "Pagina 5"),
    ("«Een code is geen verbod, maar een advies»", "A code is not a ban, but advice.", "Pagina 6"),
    ("«Het weer is van ons allemaal, maar het raakt ons allemaal anders»", "The weather belongs to us all, but it affects us all differently.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 90
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- volgende week ----
# Fix-1 layout only: py moved down (fy shift minus pitch saving); text unchanged.
py = 2439
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "VOLGENDE WEEK　NEXT WEEK (VOL.3)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Zondag 15 november komt Sinterklaas aan in Amsterdam. En woensdag 11 november is het Sint-Maarten: kinderen gaan met lampionnen langs de deuren. Verder: jullie brieven en de beste teksten van pagina 8. Tot maandag!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-taal.svg")
print("P7 saved, exercises so far:", len(REG))
