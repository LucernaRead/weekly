# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA · LANGUAGE", "A Lucerna", "Três níveis, três ferramentas · Three levels, three tools")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · PERGUNTAS E O PRESENTE", 24)
a.para("Para perguntar o essencial da semana: «Que horas começa a prova?» — que horas + verbo no presente. E, para lugares, «Onde fica o meu local?» — onde fica.", 21.5)
a.para("E conferir é especial na primeira pessoa: eu confiro, você confere, ele confere. Nós conferimos, eles conferem.", 21.5)
a.bridge("Questions: que horas (what time) + verb; onde fica asks where a place is; conferir is irregular in the eu form: confiro.")
a.ex("A2", "Complete the sentence", "confiro", "conferir: eu → confiro (irregular)",
     "Eu ___ (conferir) o cartão.", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "Complete the sentence", "confere", "conferir: você → confere",
     "Você ___ (conferir) o local antes de sair.", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "Complete the sentence", "começa", "começar: ela → começa",
     "Que horas ___ (começar) a prova?", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "Multiple choice", "B", "onde asks about place",
     "«___ fica o meu local?» A. Que horas · B. Onde · C. Quando", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · O PRETÉRITO PERFEITO", 24)
b.para("Para contar a semana, usamos o pretérito perfeito: eu revisei, ele chegou, ele dormiu. Revisar é regular: eu revisei, ele revisou.", 21.5)
b.para("E o modelo é simples: chegar → chegou; dormir → dormiu; separar → separei. Atenção ao acento: saíram, caíram.", 21.5)
b.bridge("To tell the week's story we use the pretérito perfeito; revisar is regular (revisei); chegar and dormir take an accent in the past: chegou, dormiu.")
b.ex("B1", "Complete the sentence", "revisei", "revisar, past tense: revisei",
     "Eu ___ (revisar) um pouco por dia.", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "Complete the sentence", "chegou", "chegar, past tense: chegou",
     "O candidato ___ (chegar) cedo.", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "Complete the sentence", "dormiu", "dormir, past tense: dormiu",
     "Ele ___ (dormir) bem na véspera.", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "Multiple choice", "B", "chegaram is the past tense, plural, of chegar",
     "«Os times ___ à volta com tudo em aberto.» A. chega · B. chegaram · C. chegamos", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando você chegar, apresente o documento.» «Quem tiver o cartão, confere o local.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Ter → tiver; ser → for; chegar → chegar (regular). Não confunda com o presente: é a gramática das hipóteses sobre o domingo.", 21.5)
c.bridge("After quando, se and quem, the future takes the subjunctive: tiver, for, chegar — the grammar of Sunday hypotheses.")
c.ex("B2", "Complete the sentence", "tiver", "quem + future subjunctive: tiver",
     "Quem ___ (ter) o cartão confere o local antes do domingo.", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "Complete the sentence", "chegar", "quando + future subjunctive: chegar",
     "Quando você ___ (chegar) ao local, apresente o documento.", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "Complete the sentence", "for", "se + future subjunctive of ser: for",
     "Se o seu local ___ (ser) novo, saia mais cedo de casa.", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "Multiple choice", "B", "quando + future → future subjunctive for",
     "«Quando ___ domingo, o país faz a prova.» A. é · B. for · C. seja", size=20.5, gap=10)
c.end_report()

# ---- col 3: erros comuns + a palavra + cartas ----
bx = COLX[3]
errs = [
    ("«Vou fazer o Enem de caneta azul.»", "→ «De caneta preta.» A caneta do Enem é preta.", "Black pen only — blue will not do."),
    ("«Chego às 13h30, na hora da prova.»", "→ «Chego antes das 13h.» Os portões fecham às 13h.", "Gates close at 13h — 13:30 is too late."),
    ("«Vou revisar a noite inteira na véspera.»", "→ «Vou dormir bem na véspera.» Quem dorme lembra melhor.", "No all-nighter — sleep and remember."),
    ("«O feriadão é de 2 a 5 de novembro.»", "→ «O feriadão é de 31 a 2.» Três dias: sábado, domingo e segunda.", "October 31 to November 2 — three days."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 198
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS · MISTAKES", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 22
wt = "« feriadão »: sábado, domingo e segunda — três dias de descanso."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("feriadão = the long holiday weekend.", "sans", False, 20, CW - 44)) * 29 + 30
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA · WORD OF THE WEEK", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "feriadão = the long holiday weekend.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 22
lt = "«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO"
# FIX1 (independent proof, Problem 1 — promise gap): on-page deferral disclosure.
# VOL.1 promised real letters + best P8 texts for VOL.2; none had arrived by press
# time, so the labeled editor's example stays and the promise carries to VOL.3.
# No letters/texts fabricated; existing labeling kept verbatim.
disc_pt = "Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3."
disc_en = "Editor's note: the real letters and best texts promised in VOL.1 had not arrived by press time — the example stands, and the promise carries over to VOL.3."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Editor's example — not a real letter. Send your letters to the editors: the best will be printed in VOL.3!", "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap(disc_pt, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_en, "sans", False, 19.5, CW - 44)) * 29 + 35
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, "Editor's example — not a real letter. Send your letters to the editors: the best will be printed in VOL.3!", 20, "sans", False, GREY, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 10, disc_pt, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 10, disc_en, 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASES DA SEMANA · PHRASES OF THE WEEK (verbatim from this issue)", 27, "sans", True, OLIVE)
quotes = [
    ("«Do feriadão à prova: a semana do Enem»", "From the long weekend to the exam: Enem week.", "Página 1"),
    ("«Muita gente viaja, visita a família e vai ao cemitério levar flores»", "Many people travel, visit family and take flowers to the cemetery.", "Página 1"),
    ("«Finados é o dia da memória»", "Finados is a day of remembrance.", "Página 2"),
    ("«lembrar é um jeito de continuar perto»", "Remembering is a way of staying close.", "Página 3"),
    ("«cada ponto vale uma posição, cada gol vale uma história»", "Every point is worth a place, every goal a story.", "Página 4"),
    ("«quem dorme bem lembra melhor»", "Sleep well, remember better.", "Página 5"),
    ("«primeiro as fáceis, depois as difíceis»", "The easy ones first, then the hard ones.", "Página 6"),
    ("«Confira o cartão, durma bem, chegue cedo»", "Check your card, sleep well, arrive early.", "Página 2"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 104  # EN: tightened from 108 to restore preview-box clearance after the word-box pad
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA · NEXT WEEK (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Domingo 15 de novembro: o segundo dia do Enem — Natureza e Matemática. E o feriado da Proclamação da República. Mais: as suas cartas e os melhores textos da página 8. Até segunda!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
