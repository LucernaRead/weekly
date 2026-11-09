# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · TAAL (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("TAAL　A língua", "De Lucerna", "A língua em foco　Drie niveaus, drie gereedschappen　Três níveis, três ferramentas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　DE KLOK EN HOE LAAT", 24)
a.para("Vraag: «Hoe laat is het?» Antwoord met kwart en half: kwart over twee (02:15), half drie (02:30), kwart voor drie (02:45). Let op: half drie is half vóór drie — dus half vóór het hele uur.", 21.5)
a.para("En de klok verzetten: in oktober gaat hij achteruit, in het voorjaar vooruit. Eén uur maar — maar iedereen praat erover.", 21.5)
a.expl("hoe laat pergunta as horas; half drie é 2:30 (meia hora antes das três); em outubro atrasa, na primavera adianta.")
a.ex("A2", "Complete a frase", "kwart over drie", "kwart over drie = 3:15",
     "03:15 is ___.", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Complete a frase", "half vier", "half vier = 3:30",
     "03:30 is ___.", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Escolha múltipla", "B", "half vijf = 4:30 (pegadinha)",
     "«Half vijf» is... A. 05:30 · B. 04:30 · C. 04:45", size=20.5, gap=10)
a.ex("A2", "Complete a frase", "achteruit", "em outubro o relógio atrasa",
     "In oktober gaat de klok ___.", instr="Complete", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　VAKANTIE EN VRIJE TIJD", 24)
b.para("In de herfstvakantie gaan families eropuit: naar een museum, het bos of een andere stad. En thuis bijslapen hoort er ook bij: een uur extra in bed is ook vakantie.", 21.5)
b.para("Werkwoorden van de week: eropuit gaan (ging, gegaan) en bijslapen (sliep bij, bijgeslapen). Let op: bijslapen is scheidbaar — «ik sliep zondag lekker bij».", 21.5)
b.expl("eropuit gaan sair para passear; bijslapen dormir para recuperar — verbo separável: ik sliep bij.")
b.ex("B1", "Complete a frase", "eropuit", "eropuit = sair para passear",
     "In de vakantie gaan wij ___: naar het bos en een museum.", instr="Complete", size=20.5, gap=10)
b.ex("B1", "Complete a frase", "bijgeslapen", "particípio de bijslapen: bijgeslapen",
     "Zondag heb ik lekker ___ (bijslapen).", instr="Complete", size=20.5, gap=10)
b.ex("B1", "Complete a frase", "gingen", "passado plural de gaan: gingen",
     "Gisteren ___ (gaan) wij naar Eindhoven.", instr="Complete", size=20.5, gap=10)
b.ex("B1", "Escolha múltipla", "A", "bijslapen = dormir para recuperar",
     "«Bijslapen» betekent... A. extra slapen om uit te rusten · B. vroeg opstaan · C. buiten slapen", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　RUZIE EN MENINGEN", 24)
c.para("Televisie geeft woorden voor ruzie: «een ruzie hebben met iemand», «het ergens niet mee eens zijn». Een sterke, informele zin is: «Dat slaat nergens op!» Dat betekent: dat is onzin. Gebruik hem voorzichtig — hij is informeel.", 21.5)
c.para("Een mening beleefd geven doe je zo: «Ik vind dat ...», «Volgens mij ...» of «Het lijkt me dat ...» Zo praat je mee over De Hanslers én over de klok.", 21.5)
c.expl("ruzie briga; slaat nergens op é informal («não faz sentido») — use com cuidado; Ik vind dat… é um jeito educado de opinar.")
c.ex("B2", "Complete a frase", "ruzie", "ruzie = briga (de)",
     "Monique en Mike hebben ___ in de serie.", instr="Complete", size=20.5, gap=10)
c.ex("B2", "Escolha múltipla", "B", "Volgens mij… é um começo educado",
     "Je begint je mening beleefd met... A. Dat slaat nergens op! · B. Volgens mij is dat goed. · C. Ruzie!", size=20.5, gap=10)
c.ex("B2", "Complete a frase", "onzin", "onzin = bobagem, sem sentido",
     "«Dat slaat nergens op» betekent: dat is ___.", instr="Complete", size=20.5, gap=10)
c.ex("B2", "Complete a frase", "eens", "het eens zijn met iemand = concordar com alguém",
     "Ik ben het helemaal met je ___.", instr="Complete", size=20.5, gap=10)
c.end_report()

# ---- col 3: pas op + het woord + brieven ----
bx = COLX[3]
errs = [
    ("«Half drie is 03:30.»", "→ Fout: half drie is 02:30. «Half» is vóór het uur, niet erna.", "half drie é 2:30: o «half» vem antes."),
    ("«De klok gaat voorruit.»", "→ «Vooruit» is één woord — en in oktober gaat de klok achteruit.", "Uma palavra só; em outubro, para trás."),
    ("«Ik loop naar de huisje.»", "→ Altijd «het» bij verkleinwoorden: «het huisje».", "O diminutivo leva «het»: het huisje."),
    ("«Ik blijf thuis, omdat ik heb geen tijd.»", "→ Na «omdat» staat het werkwoord aan het einde: «... geen tijd heb.»", "Com «omdat», o verbo vai ao fim."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 192
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "PAS OP!　Clínica de erros", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 18
wt = "«eropuit» betekent: het huis uit gaan om iets leuks te doen — naar een museum, het bos of een festival. In de herfstvakantie gaat heel Nederland eropuit."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("eropuit = sair para se divertir: ir a um museu, à floresta ou a um festival.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "HET WOORD　A palavra", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "eropuit = sair para se divertir: ir a um museu, à floresta ou a um festival.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 18
lt = "«Hallo! Ik ben Chen en ik leer Nederlands in Beijing. In oktober slaap ik één uur langer — net als jullie!» — Chen (voorbeeldbrief van de redactie)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Exemplo da redação; o VOL.2 trará cartas reais e os melhores da página 8.", "sans", False, 20, CW - 44)) * 29 + 34
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "BRIEVEN VAN LEZERS", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Exemplo da redação; o VOL.2 trará cartas reais e os melhores da página 8.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- zinnen van de week (verbatim from this issue) ----
fy = 1712
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "ZINNEN VAN DE WEEK　Frases da semana (deste número)", 27, "sans", True, OLIVE)
quotes = [
    ("«De wintertijd begint — en iedereen slaapt een uur langer»", "Começa o horário de inverno — e todos dormem uma hora a mais.", "Página 1"),
    ("«In het voorjaar gaat de klok vooruit, in het najaar achteruit»", "Na primavera o relógio anda para a frente; no outono, para trás.", "Página 2"),
    ("«Thuisbezorgd en Uber Eats stoppen met verborgen kosten»", "Thuisbezorgd e Uber Eats acabam com os custos escondidos.", "Página 2"),
    ("«Ongeveer 2.500 ontwerpers laten hun werk zien»", "Cerca de 2.500 designers mostram o seu trabalho.", "Página 3"),
    ("«PSV won dinsdag met 1–0 bij FC Porto»", "O PSV venceu por 1–0 no Porto, na terça-feira.", "Página 4"),
    ("«Er komen meer dan 3.000 artiesten naar meer dan 200 locaties in de stad»", "Mais de 3.000 artistas em mais de 200 locais da cidade.", "Página 5"),
    ("«ongeveer 750.000 keer zochten Nederlanders naar de klokverandering»", "Os neerlandeses pesquisaram a mudança do relógio cerca de 750.000 vezes.", "Página 6"),
    ("«Samen zijn dat 547.000 zoekopdrachten»", "Juntos, são 547.000 pesquisas.", "Página 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- volgende week ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "VOLGENDE WEEK　Na próxima semana (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Zondag 1 november begint Expeditie Robinson (20:00 uur, RTL 4): wie van de 19 kandidaten is de sterkste? Verder: de uitslagen van de Europese voetbalweek, de laatste verhalen van ADE en de Dutch Design Week, en jullie brieven en beste teksten van pagina 8. Tot maandag!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-taal.svg")
print("P7 saved, exercises so far:", len(REG))
