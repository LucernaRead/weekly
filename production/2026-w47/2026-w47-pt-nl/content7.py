# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA　Taal", "A Lucerna", "Taal in de schijnwerpers　Três níveis, três ferramentas　Drie niveaus, drie instrumenten")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　O FERIADO E AS DATAS", 24)
a.para("Para falar de um feriado, usamos «em» com a data: «em 20 de novembro». E, para o dia, «no dia 20». E o verbo da semana é «cair»: o feriado cai numa sexta — cair é o verbo dos feriados no calendário.", 21.5)
a.para("E «aproveitar» é o verbo do feriadão: eu aproveito, você aproveita, nós aproveitamos.", 21.5)
a.bridge("Om over een feestdag te praten, gebruik je em + de datum (em 20 de novembro), no dia 20; cair betekent 'vallen op een dag'; en de vervoegingen van aproveitar.")
a.ex("A2", "Maak de zin af", "em", "em + datum: em 20 de novembro",
     "O feriado é ___ 20 de novembro.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Maak de zin af", "numa", "cair numa sexta-feira:valt op een vrijdag",
     "O feriado cai ___ sexta-feira.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Maak de zin af", "é", "ser, tegenwoordige tijd, vorm van ele: é",
     "Que dia ___ (ser) o feriado?", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Meerkeuze", "B", "aproveitar: vorm van nós aproveitamos",
     "«Nós ___ o feriadão.» A. aproveita · B. aproveitamos · C. aproveito", size=20.5, gap=10)
a.end_report()
a_end = a.y

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　O PRETÉRITO PERFEITO", 24)
b.para("Para contar o fim de semana da Copa, usamos o pretérito perfeito: o Grêmio empatou, o Vasco venceu, Norris venceu. Empatar é regular: eu empatei, ele empatou.", 21.5)
b.para("E o modelo é simples: abrir → abriu; garantir → garantiu; sair → saiu. Atenção ao acento: saíram, caíram.", 21.5)
b.bridge("Om het Copa-weekend te vertellen gebruik je de verleden tijd (pretérito perfeito); empatar is regelmatig (empatou); let op het accent in de verleden tijd van abrir, garantir en sair.")
b.ex("B1", "Maak de zin af", "empatou", "empatar verleden tijd: empatou",
     "O Grêmio ___ (empatar) por 1 a 1.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Maak de zin af", "venceu", "vencer verleden tijd: venceu",
     "O Vasco ___ (vencer) por 2 a 1.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Maak de zin af", "abriu", "abrir verleden tijd: abriu",
     "Renan Lodi ___ (abrir) o placar.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Meerkeuze", "B", "saíram is de verleden tijd, meervoud, van sair",
     "«Os finalistas ___ no fim de semana.» A. saem · B. saíram · C. sairão", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando sair o gabarito, confira as respostas.» «Se a sua nota for boa, comemore.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Sair → sair; ser → for; ter → tiver. Não confunda com o presente: é a gramática das hipóteses sobre o gabarito.", 21.5)
c.bridge("quando, se, quem krijgen de toekomende tijd van de aanvoegende wijs: sair, for, tiver (de grammatica van het wachten op de officiële antwoorden).")
c.ex("B2", "Maak de zin af", "sair", "quando + toekomende tijd van de aanvoegende wijs: sair",
     "Quando ___ (sair) o gabarito, confira as respostas.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Maak de zin af", "for", "se + ser toekomende tijd van de aanvoegende wijs: for",
     "Se a sua nota ___ (ser) boa, comemore.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Maak de zin af", "tiver", "quem + toekomende tijd van de aanvoegende wijs: tiver",
     "Quem ___ (ter) o cartão confere o local antes do domingo.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Meerkeuze", "B", "quando + de toekomst → toekomende tijd van de aanvoegende wijs sair",
     "«Quando ___ o gabarito, o país respira.» A. sai · B. sair · C. saia", size=20.5, gap=10)
c.end_report()

# ---- image under the A2 column: Os Lusíadas, 1572 ----
iy7 = a_end + 30
image(p, "lusiadas.jpg", COLX[0] + 81, iy7, 260, 392)
caption(p, COLX[0], iy7 + 392, CW,
        "A primeira edição de «Os Lusíadas», de Luís de Camões, Lisboa, 1572: a língua portuguesa impressa há mais de 450 anos.",
        "Domínio público / Wikimedia Commons")
print("P7 image ends ~", iy7 + 392 + 110)

# ---- col 3: erros comuns + a palavra + cartas ----
bx = COLX[3]
errs = [
    ("«O gabarito já saiu no domingo 15.»", "→ «Só o extraoficial.» O oficial do Inep sai até o fim de novembro.", "De officiële antwoorden komen pas eind november."),
    ("«O feriado dá folga na segunda, 23.»", "→ «Não há folga extra.» O feriadão termina no domingo 22.", "Het lange weekend eindigt op zondag; op maandag is er geen vrije dag."),
    ("«O Palmeiras passou no tempo normal.»", "→ «Passou nos pênaltis, 5 a 4.» No tempo normal, o Vasco venceu por 2 a 1.", "Palmeiras door na strafschoppen 5–4; in de reguliere tijd won Vasco met 2–1."),
    ("«O dia 20 cai num domingo.»", "→ «Cai numa sexta-feira.» O feriadão vai de 20 a 22.", "20 november is een vrijdag; het lange weekend loopt tot zondag 22."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 198
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS　Fouten", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 22
wt = "« consciência »: saber e lembrar — de si, da história e dos outros. «Consciência Negra» é a memória da luta e da cultura afro-brasileiras."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("consciência = bewustzijn, geweten: de herinnering aan het verzet en de cultuur.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA　Woord van de week", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "consciência = bewustzijn, geweten: de herinnering aan het verzet en de cultuur.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 22
lt = "«Vou aproveitar o feriadão para ler sobre Zumbi. Bom feriado!» — EXEMPLO DA REDAÇÃO"
# W47 disclosure: VOL.3 promised real letters + best P8 texts for VOL.4; none had
# arrived by press time, so the labeled editor's example stands and the promise
# carries to VOL.5. No letters/texts fabricated; labeling kept verbatim in form.
disc_pt = "Nota da redação: as cartas reais e os melhores textos do VOL.3 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.5."
disc_nl = "Opmerking van de redactie: geen echte brieven of beste teksten uit VOL.3 — het voorbeeld blijft, de belofte naar VOL.5."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Voorbeeld van de redactie — geen echte brief. Stuur je brief op!", "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap(disc_pt, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_nl, "sans", False, 19.5, CW - 44)) * 29 + 22
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, "Voorbeeld van de redactie — geen echte brief. Stuur je brief op!", 20, "sans", False, GREY, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 10, disc_pt, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 10, disc_nl, 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 16)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "FRASES DA SEMANA　Zinnen van de week (letterlijk uit dit nummer)", 27, "sans", True, OLIVE)
quotes = [
    ("«Consciência Negra: sexta é feriado em todo o país»", "Dag van het Zwarte Bewustzijn: nationale feestdag op vrijdag.", "Página 1"),
    ("«o feriado abre um fim de semana de três dias»", "De feestdag opent een weekend van drie dagen.", "Página 1"),
    ("«Zumbi nasceu em Palmares»", "Zumbi werd geboren in Palmares.", "Página 3"),
    ("«sem memória, não há futuro»", "Zonder geheugen is er geen toekomst.", "Página 3"),
    ("«o agregado ficou em 2 a 2»", "De totaalscore eindigde op 2–2.", "Página 4"),
    ("«a espera pelo gabarito»", "Wachten op de officiële antwoorden.", "Página 5"),
    ("«primeiro as fáceis, depois as difíceis»", "Eerst de makkelijke, dan de moeilijke.", "Página 6"),
    ("«Confira o transporte, guarde o documento e aproveite o feriadão»", "Check het vervoer, neem je documenten mee en geniet goed van het lange weekend.", "Página 2"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 80
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA　Volgende week (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Sexta, 27 de novembro: a Black Friday. E o gabarito oficial do Enem, até o fim do mês — e a final da Copa se aproxima: dia 6 de dezembro, em Brasília. Até segunda!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
