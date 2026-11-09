# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA　LINGUA", "A Lucerna", "Três níveis, três ferramentas　Tre livelli, tre strumenti")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　PERGUNTAS E O PRESENTE", 24)
a.para("Para perguntar o essencial da semana: «Que horas começa a prova?» — que horas + verbo no presente. E, para lugares, «Onde fica o meu local?» — onde fica.", 21.5)
a.para("E conferir é especial na primeira pessoa: eu confiro, você confere, ele confere. Nós conferimos, eles conferem.", 21.5)
a.bridge("Domande: que horas (a che ora) + verbo; onde fica chiede dove si trova un luogo; conferir è irregolare nella forma eu: confiro.")
a.ex("A2", "Completa la frase", "confiro", "conferir: eu → confiro (irregolare)",
     "Eu ___ (conferir) o cartão.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Completa la frase", "confere", "conferir: você → confere",
     "Você ___ (conferir) o local antes de sair.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Completa la frase", "começa", "começar: ela → começa",
     "Que horas ___ (começar) a prova?", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Scelta multipla", "B", "onde chiede il luogo",
     "«___ fica o meu local?» A. Que horas · B. Onde · C. Quando", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　O PRETÉRITO PERFEITO", 24)
b.para("Para contar a semana, usamos o pretérito perfeito: eu revisei, ele chegou, ele dormiu. Revisar é regular: eu revisei, ele revisou.", 21.5)
b.para("E o modelo é simples: chegar → chegou; dormir → dormiu; separar → separei. Atenção ao acento: saíram, caíram.", 21.5)
b.bridge("Per raccontare la settimana usiamo il pretérito perfeito; revisar è regolare (revisei); chegar e dormir prendono l'accento al passato: chegou, dormiu.")
b.ex("B1", "Completa la frase", "revisei", "revisar, passato: revisei",
     "Eu ___ (revisar) um pouco por dia.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Completa la frase", "chegou", "chegar, passato: chegou",
     "O candidato ___ (chegar) cedo.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Completa la frase", "dormiu", "dormir, passato: dormiu",
     "Ele ___ (dormir) bem na véspera.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Scelta multipla", "B", "chegaram è il passato, plurale, di chegar",
     "«Os times ___ à volta com tudo em aberto.» A. chega · B. chegaram · C. chegamos", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando você chegar, apresente o documento.» «Quem tiver o cartão, confere o local.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Ter → tiver; ser → for; chegar → chegar (regular). Não confunda com o presente: é a gramática das hipóteses sobre o domingo.", 21.5)
c.bridge("Dopo quando, se e quem, il futuro vuole il congiuntivo: tiver, for, chegar — la grammatica delle ipotesi sulla domenica.")
c.ex("B2", "Completa la frase", "tiver", "quem + futuro del congiuntivo: tiver",
     "Quem ___ (ter) o cartão confere o local antes do domingo.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Completa la frase", "chegar", "quando + futuro del congiuntivo: chegar",
     "Quando você ___ (chegar) ao local, apresente o documento.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Completa la frase", "for", "se + futuro del congiuntivo di ser: for",
     "Se o seu local ___ (ser) novo, saia mais cedo de casa.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Scelta multipla", "B", "quando + futuro → futuro del congiuntivo for",
     "«Quando ___ domingo, o país faz a prova.» A. é · B. for · C. seja", size=20.5, gap=10)
c.end_report()

# ---- col 3: erros comuns + a palavra + cartas ----
bx = COLX[3]
errs = [
    ("«Vou fazer o Enem de caneta azul.»", "→ «De caneta preta.» A caneta do Enem é preta.", "Solo penna nera — la blu non va bene."),
    ("«Chego às 13h30, na hora da prova.»", "→ «Chego antes das 13h.» Os portões fecham às 13h.", "I cancelli chiudono alle 13 — le 13:30 sono troppo tardi."),
    ("«Vou revisar a noite inteira na véspera.»", "→ «Vou dormir bem na véspera.» Quem dorme lembra melhor.", "Niente notte in bianco — dormi e ricorda."),
    ("«O feriadão é de 2 a 5 de novembro.»", "→ «O feriadão é de 31 a 2.» Três dias: sábado, domingo e segunda.", "Dal 31 ottobre al 2 novembre — tre giorni."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 198
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS　ERRORI", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 22
wt = "« feriadão »: sábado, domingo e segunda — três dias de descanso."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("feriadão = il lungo weekend di festa.", "sans", False, 20, CW - 44)) * 29 + 30
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA　LA PAROLA", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "feriadão = il lungo weekend di festa.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 22
lt = "«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO"
# FIX1 (independent proof, Problem 1 — promise gap): on-page deferral disclosure.
# VOL.1 promised real letters + best P8 texts for VOL.2; none had arrived by press
# time, so the labeled editor's example stays and the promise carries to VOL.3.
# No letters/texts fabricated; existing labeling kept verbatim.
disc_pt = "Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3."
disc_it = "Nota della redazione: le lettere vere e i migliori testi promessi nel VOL.1 non erano arrivati alla chiusura — resta l'esempio e la promessa passa al VOL.3."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Esempio della redazione — non è una lettera vera. Mandate le vostre lettere: le migliori saranno pubblicate nel VOL.3!", "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap(disc_pt, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_it, "sans", False, 19.5, CW - 44)) * 29 + 35
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, "Esempio della redazione — non è una lettera vera. Mandate le vostre lettere: le migliori saranno pubblicate nel VOL.3!", 20, "sans", False, GREY, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 10, disc_pt, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 10, disc_it, 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 44)
p.hline(MX, RIGHT, fy - 2, OLIVE, 2)  # rule below the CARTAS box (fy-14 cut the last line)
p.text(MX, fy + 24, "FRASES DA SEMANA　FRASI DELLA SETTIMANA (tratte parola per parola da questo numero)", 27, "sans", True, OLIVE)
quotes = [
    ("«Do feriadão à prova: a semana do Enem»", "Dal lungo weekend all'esame: la settimana dell'Enem.", "Página 1"),
    ("«Muita gente viaja, visita a família e vai ao cemitério levar flores»", "Molti viaggiano, visitano la famiglia e portano fiori al cimitero.", "Página 1"),
    ("«Finados é o dia da memória»", "Finados è un giorno di ricordo.", "Página 2"),
    ("«lembrar é um jeito de continuar perto»", "Ricordare è un modo per restare vicini.", "Página 3"),
    ("«cada ponto vale uma posição, cada gol vale uma história»", "Ogni punto vale un posto, ogni gol una storia.", "Página 4"),
    ("«quem dorme bem lembra melhor»", "Dormi bene, ricorda meglio.", "Página 5"),
    ("«primeiro as fáceis, depois as difíceis»", "Prima le facili, poi le difficili.", "Página 6"),
    ("«Confira o cartão, durma bem, chegue cedo»", "Controlla la tessera, dormi bene, arriva presto.", "Página 2"),
]
colw = (RIGHT - MX - GUT) // 2
fr_end = 0  # lowest Frases translation end (adaptive band)
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 92  # IT: tightened from 104 (EN) so quote row 4 clears the VOL.3 preview box
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    fr_end = max(fr_end, p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35))

# ---- próxima semana ----
py = max(2404, fr_end - 12)  # adaptive: keep the band clear of the Frases translations
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA　IL PROSSIMO NUMERO (VOL.3)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Domingo 15 de novembro: o segundo dia do Enem — Natureza e Matemática. E o feriado da Proclamação da República. Mais: as suas cartas e os melhores textos da página 8. Até segunda!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
