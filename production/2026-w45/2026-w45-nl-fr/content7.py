# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · TAAL (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("TAAL · LANGUE", "De Lucerna", "La langue en gros plan · Drie niveaus, drie gereedschappen · Trois niveaux, trois outils")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · KLIMAATWOORDEN", 24)
a.para("De woorden van deze week horen bij de Klimaatweek: het klimaat, de boom planten, besparen en de waarschuwing. Het klimaat is het weer en de natuur over een lange tijd — niet het weer van vandaag.", 21.5)
a.para("En de codes: geel is let op, oranje is gevaarlijk, rood is blijf binnen. Onthoud ook: een waarschuwing geldt voor jouw eigen omgeving.", 21.5)
a.bridge("het klimaat : le climat, à long terme · een boom planten : planter un arbre · besparen : économiser · de waarschuwing : l'avertissement.")
a.ex("A2", "完成句子", "planten", "wij → planten",
     "In de Klimaatweek ___ (planten) wij een boom.", instr="Compléter", size=20.5, gap=10)
a.ex("A2", "完成句子", "bespaar", "je → bespaar",
     "Met de fiets ___ (besparen) je energie.", instr="Compléter", size=20.5, gap=10)
a.ex("A2", "单选", "B", "Le climat, c'est le temps et la nature à long terme",
     "«Het klimaat» is... A. het weer van vandaag · B. het weer en de natuur over een lange tijd · C. een museum", size=20.5, gap=10)
a.ex("A2", "完成句子", "blijf", "code rouge = restez à l'intérieur",
     "Code rood betekent: ___ binnen.", instr="Compléter", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · SCHEIDBARE WERKWOORDEN", 24)
b.para("Deze week doen we iets met scheidbare werkwoorden: meedoen (deed mee, meegedaan), opruimen (ruimde op, opgeruimd) en vastzetten (zette vast, vastgezet). Het eerste deel gaat in de zin naar het einde.", 21.5)
b.para("Voorbeeld: «Ik doe mee aan de Klimaatweek.» «Wij hebben de tuin opgeruimd.» «Zij zette de losse spullen vast.» Let op de volgorde: het deel staat achteraan.", 21.5)
b.bridge("meedoen : participer, ik doe mee · opruimen : ranger, wij hebben opgeruimd · vastzetten : bien fixer, zij zette vast.")
b.ex("B1", "完成句子", "doe mee", "ik → doe mee",
     "Ik ___ (meedoen) aan de Klimaatweek.", instr="Compléter", size=20.5, gap=10)
b.ex("B1", "完成句子", "opgeruimd", "participe passé de opruimen : opgeruimd",
     "Wij hebben de tuin ___ (opruimen).", instr="Compléter", size=20.5, gap=10)
b.ex("B1", "完成句子", "zette vast", "vastzetten au passé : zette vast",
     "Zij ___ (vastzetten) de losse spullen.", instr="Compléter", size=20.5, gap=10)
b.ex("B1", "单选", "B", "meedoen = participer",
     "«Meedoen» betekent... A. meekijken · B. deelnemen, erbij zijn · C. weggaan", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · EEN MENING GEVEN", 24)
c.para("Over het klimaat heeft iedereen een mening. Beleefd geef je die zo: «Ik vind dat ...», «Volgens mij ...» of «Het lijkt me dat ...» Zo praat je mee over de Klimaatweek én over de codes van het KNMI.", 21.5)
c.para("Voorbeeld: «Volgens mij moet iedereen meedoen.» «Het lijkt me dat lokaal waarschuwen beter is.» Een mening is geen feit — zeg er dus bij dat het jouw mening is.", 21.5)
c.bridge("Ik vind dat… : je trouve que… · Volgens mij… : à mon avis… · Het lijkt me dat… : il me semble que…")
c.ex("B2", "完成句子", "Volgens", "Volgens mij… = à mon avis…",
     "___ mij moet iedereen meedoen aan de Klimaatweek.", instr="Compléter", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Ik vind dat… exprime une opinion",
     "«Ik vind dat iedereen moet meedoen» is... A. een bevel · B. een mening · C. een vraag", size=20.5, gap=10)
c.ex("B2", "完成句子", "lijkt", "Het lijkt me dat… = il me semble que…",
     "Het ___ me dat lokaal waarschuwen beter is.", instr="Compléter", size=20.5, gap=10)
c.ex("B2", "完成句子", "mij", "Volgens mij… = à mon avis…",
     "Volgens ___ is fietsen beter dan autorijden.", instr="Compléter", size=20.5, gap=10)
c.end_report()

# ---- col 3: pas op + het woord + brieven ----
bx = COLX[3]
errs = [
    ("«Het klimaat is slecht weer.»", "→ Fout: het klimaat is het weer over een lange tijd.", "Le climat = le temps à long terme, pas celui d'aujourd'hui."),
    ("«Ik doe mee aan de klimaatweek.»", "→ «Klimaatweek» krijgt een hoofdletter: het is een naam.", "Klimaatweek, nom propre : majuscule."),
    ("«Ik plant een bomen.»", "→ «Een» is enkelvoud: «een boom» of «bomen».", "Singulier : een boom ; pluriel : bomen."),
    ("«Omdat het regent, ik blijf thuis.»", "→ Na «omdat» staat het werkwoord op plaats 2: «... blijf ik thuis.»", "Après omdat, le verbe principal est en 2e position : blijf ik thuis."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 192
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "PAS OP! · PIÈGES FRÉQUENTS", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 18
wt = "«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("meedoen = participer.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "HET WOORD · MOT DE LA SEMAINE", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "meedoen = participer.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 18
lt = "«Hallo! Ik ben Li en ik leer Nederlands in Shanghai. In de Klimaatweek plant ik een boom op mijn balkon!» — Li (voorbeeldbrief van de redactie)"
# Fix-1 disclosure (independent proof Problem 2): on-page, Dutch + matching French.
# No real letters/best P8 texts had arrived by press time, so the labeled example
# stands and the promise carries to VOL.3. Existing labeling/invitation kept verbatim.
dt_nl = "Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3."
dt_fr = "Aucune vraie lettre ni meilleur texte de page 8 reçu : voici cet exemple ; promesse reportée au VOL.3."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(dt_nl, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(dt_fr, "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap("Exemple de la rédaction. Envoyez vos vraies lettres et textes de page 8 : nous les publierons dans le VOL.3 !", "sans", False, 20, CW - 44)) * 29 + 34 + 50
# +50 measured correction: rendered inter-paragraph spacing runs ~20px above the
# formula per added paragraph (verified on the rendered SVG: last baseline sat
# 21px below the box edge before this correction).
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "BRIEVEN VAN LEZERS", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, dt_nl, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, dt_fr, 20, "sans", False, GREY, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Exemple de la rédaction. Envoyez vos vraies lettres et textes de page 8 : nous les publierons dans le VOL.3 !", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- zinnen van de week (verbatim from this issue) ----
# Fix-1 layout only: fy moved down for the taller BRIEVEN box; row pitch
# 158 -> 90 (rows have ~77px of content from quote top to Chinese descender,
# so 90px still leaves a clear gap); no quote text changed.
fy = 1951
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "ZINNEN VAN DE WEEK · PHRASES DE LA SEMAINE (MOT POUR MOT, DE CETTE ÉDITION)", 27, "sans", True, OLIVE)
quotes = [
    ("«Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland»", "Du lundi 2 au dimanche 8 novembre, c'est la Semaine du climat aux Pays-Bas.", "Pagina 1"),
    ("«De herfst is de beste tijd om te planten»", "L'automne est le meilleur moment pour planter.", "Pagina 1"),
    ("«Geel betekent: let op, het weer kan gevaarlijk zijn»", "Jaune signifie : attention, le temps peut devenir dangereux.", "Pagina 2"),
    ("«Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts»", "Plus de 70 musées sont ouverts de 19 heures le soir à 2 heures la nuit.", "Pagina 3"),
    ("«Ajax won donderdag 22 oktober met 2–0 van Atalanta»", "L'Ajax a battu l'Atalanta 2–0, jeudi 22 octobre.", "Pagina 4"),
    ("«Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur»", "Dimanche 1er novembre, Expeditie Robinson a commencé sur RTL 4, à 20 heures.", "Pagina 5"),
    ("«Een code is geen verbod, maar een advies»", "Un code n'est pas une interdiction, mais un conseil.", "Pagina 6"),
    ("«Het weer is van ons allemaal, maar het raakt ons allemaal anders»", "Le temps appartient à nous tous, mais il nous touche tous différemment.", "Pagina 6"),
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
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "VOLGENDE WEEK · LA SEMAINE PROCHAINE (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Zondag 15 november komt Sinterklaas aan in Amsterdam. En woensdag 11 november is het Sint-Maarten: kinderen gaan met lampionnen langs de deuren. Verder: jullie brieven en de beste teksten van pagina 8. Tot maandag!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-taal.svg")
print("P7 saved, exercises so far:", len(REG))
