# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA · TAAL", "A Lucerna", "Focus op taal · Três níveis, três ferramentas · drie niveaus, drie hulpmiddelen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · PERGUNTAS E O PRESENTE", 24)
a.para("Para perguntar o essencial da semana: «Que horas começa a prova?» — que horas + verbo no presente. E, para lugares, «Onde fica o meu local?» — onde fica.", 21.5)
a.para("E conferir é especial na primeira pessoa: eu confiro, você confere, ele confere. Nós conferimos, eles conferem.", 21.5)
a.expl("Uitleg — Vragen: que horas (hoe laat) + werkwoord; onde fica vraagt naar een plaats; conferir is onregelmatig in de eu-vorm: confiro.")
a.ex("A2", "Voltooi de zin", "confiro", "conferir: eu → confiro (onregelmatig)",
     "Eu ___ (conferir) o cartão.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Voltooi de zin", "confere", "conferir: você → confere",
     "Você ___ (conferir) o local antes de sair.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Voltooi de zin", "começa", "começar: ela → começa",
     "Que horas ___ (começar) a prova?", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Meerkeuze", "B", "onde vraagt naar een plaats",
     "«___ fica o meu local?» A. Que horas · B. Onde · C. Quando", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · O PRETÉRITO PERFEITO", 24)
b.para("Para contar a semana, usamos o pretérito perfeito: eu revisei, ele chegou, ele dormiu. Revisar é regular: eu revisei, ele revisou.", 21.5)
b.para("E o modelo é simples: chegar → chegou; dormir → dormiu; separar → separei. Atenção ao acento: saíram, caíram.", 21.5)
b.expl("Uitleg — Om de week te vertellen gebruiken we de pretérito perfeito; revisar is regelmatig (revisei); chegar en dormir krijgen een accent in de verleden tijd: chegou, dormiu.")
b.ex("B1", "Voltooi de zin", "revisei", "revisar, verleden tijd: revisei",
     "Eu ___ (revisar) um pouco por dia.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Voltooi de zin", "chegou", "chegar, verleden tijd: chegou",
     "O candidato ___ (chegar) cedo.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Voltooi de zin", "dormiu", "dormir, verleden tijd: dormiu",
     "Ele ___ (dormir) bem na véspera.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Meerkeuze", "B", "chegaram is de verleden tijd (meervoud) van chegar",
     "«Os times ___ à volta com tudo em aberto.» A. chega · B. chegaram · C. chegamos", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando você chegar, apresente o documento.» «Quem tiver o cartão, confere o local.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Ter → tiver; ser → for; chegar → chegar (regular). Não confunda com o presente: é a gramática das hipóteses sobre o domingo.", 21.5)
c.expl("Uitleg — Na quando, se en quem staat de toekomst in de aanvoegende wijs: tiver, for, chegar — de grammatica van zondagse hypotheses.")
c.ex("B2", "Voltooi de zin", "tiver", "quem + aanvoegende wijs toekomst: tiver",
     "Quem ___ (ter) o cartão confere o local antes do domingo.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Voltooi de zin", "chegar", "quando + aanvoegende wijs toekomst: chegar",
     "Quando você ___ (chegar) ao local, apresente o documento.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Voltooi de zin", "for", "se + aanvoegende wijs toekomst van ser: for",
     "Se o seu local ___ (ser) novo, saia mais cedo de casa.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Meerkeuze", "B", "quando + toekomst → aanvoegende wijs toekomst for",
     "«Quando ___ domingo, o país faz a prova.» A. é · B. for · C. seja", size=20.5, gap=10)
c.end_report()

# ---- col 3: erros comuns + a palavra + cartas ----
bx = COLX[3]
errs = [
    ("«Vou fazer o Enem de caneta azul.»", "→ «De caneta preta.» A caneta do Enem é preta.", "Alleen zwarte pen, geen blauwe."),
    ("«Chego às 13h30, na hora da prova.»", "→ «Chego antes das 13h.» Os portões fecham às 13h.", "Poorten dicht om 13h: 13:30 is te laat."),
    ("«Vou revisar a noite inteira na véspera.»", "→ «Vou dormir bem na véspera.» Quem dorme lembra melhor.", "Niet doorhalen: slaap en onthoud."),
    ("«O feriadão é de 2 a 5 de novembro.»", "→ «O feriadão é de 31 a 2.» Três dias: sábado, domingo e segunda.", "31 oktober tot 2 november: 3 dagen."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 198
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS · PAS OP!", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 22
wt = "« feriadão »: sábado, domingo e segunda — três dias de descanso."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("feriadão = het lange feestweekend, drie dagen.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA · WOORD VAN DE WEEK", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "feriadão = het lange feestweekend, drie dagen.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 22
lt = "«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO"
# FIX1 (independent proof, Problem 1 — promise gap): on-page deferral disclosure.
# VOL.1 promised real letters + best P8 texts for VOL.2; none had arrived by press
# time, so the labeled editor's example stays and the promise carries to VOL.3.
# No letters/texts fabricated; existing labeling kept verbatim.
disc_pt = "Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3."
disc_nl = "Opmerking van de redactie: de echte brieven en beste teksten uit VOL.1 waren nog niet binnen — het voorbeeld blijft, de belofte gaat naar VOL.3."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Voorbeeld van de redactie — geen echte brief. Stuur je brief op: de beste verschijnen op pagina 7 in VOL.3!", "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap(disc_pt, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_nl, "sans", False, 19.5, CW - 44)) * 29 + 35
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, "Voorbeeld van de redactie — geen echte brief. Stuur je brief op: de beste verschijnen op pagina 7 in VOL.3!", 20, "sans", False, GREY, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 10, disc_pt, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 10, disc_nl, 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASES DA SEMANA · ZINNEN VAN DE WEEK (letterlijk uit deze editie)", 27, "sans", True, OLIVE)
quotes = [
    ("«Do feriadão à prova: a semana do Enem»", "Van het lange weekend naar het examen: Enem-week.", "Página 1"),
    ("«Muita gente viaja, visita a família e vai ao cemitério levar flores»", "Veel mensen reizen, bezoeken familie en brengen bloemen naar de begraafplaats.", "Página 1"),
    ("«Finados é o dia da memória»", "Finados is een dag van herinnering.", "Página 2"),
    ("«lembrar é um jeito de continuar perto»", "Herinneren is een manier om dichtbij te blijven.", "Página 3"),
    ("«cada ponto vale uma posição, cada gol vale uma história»", "Elk punt is een plaats waard, elk doelpunt een verhaal.", "Página 4"),
    ("«quem dorme bem lembra melhor»", "Goed slapen, beter onthouden.", "Página 5"),
    ("«primeiro as fáceis, depois as difíceis»", "Eerst de makkelijke, dan de moeilijke.", "Página 6"),
    ("«Confira o cartão, durma bem, chegue cedo»", "Controleer je kaart, slaap goed, kom vroeg.", "Página 2"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 96  # NL round 3: tightened from 104 so the last quote translation clears the preview box
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA · VOLGENDE WEEK (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Domingo 15 de novembro: o segundo dia do Enem — Natureza e Matemática. E o feriado da Proclamação da República. Mais: as suas cartas e os melhores textos da página 8. Até segunda!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
