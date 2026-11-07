# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-pt-de-build/repro-check2/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA · SPRACHE", "A Lucerna", "Im Fokus: Sprache · Três níveis, três ferramentas · Drei Stufen, drei Werkzeuge")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · PERGUNTAS E O PRESENTE", 24)
a.para("Para perguntar o essencial da semana: «Que horas começa a prova?» — que horas + verbo no presente. E, para lugares, «Onde fica o meu local?» — onde fica.", 21.5)
a.para("E conferir é especial na primeira pessoa: eu confiro, você confere, ele confere. Nós conferimos, eles conferem.", 21.5)
a.bridge("Fragen bilden: que horas (wie viel Uhr) + Verb; onde fica fragt nach dem Ort. Conferir ist bei eu unregelmäßig: confiro.")
a.ex("A2", "完成句子", "confiro", "conferir: eu confiro, unregelmäßig",
     "Eu ___ (conferir) o cartão.", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "完成句子", "confere", "conferir: você confere",
     "Você ___ (conferir) o local antes de sair.", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "完成句子", "começa", "começar: ela começa",
     "Que horas ___ (começar) a prova?", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "单选", "B", "onde fragt nach dem Ort",
     "«___ fica o meu local?» A. Que horas · B. Onde · C. Quando", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · O PRETÉRITO PERFEITO", 24)
b.para("Para contar a semana, usamos o pretérito perfeito: eu revisei, ele chegou, ele dormiu. Revisar é regular: eu revisei, ele revisou.", 21.5)
b.para("E o modelo é simples: chegar → chegou; dormir → dormiu; separar → separei. Atenção ao acento: saíram, caíram.", 21.5)
b.bridge("Die Woche erzählt man im Pretérito Perfeito; revisar ist regelmäßig (revisei); bei chegar und dormir auf den Akzent achten: chegou, dormiu.")
b.ex("B1", "完成句子", "revisei", "revisar, Vergangenheit: revisei",
     "Eu ___ (revisar) um pouco por dia.", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "完成句子", "chegou", "chegar, Vergangenheit: chegou",
     "O candidato ___ (chegar) cedo.", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "完成句子", "dormiu", "dormir, Vergangenheit: dormiu",
     "Ele ___ (dormir) bem na véspera.", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "单选", "B", "chegaram = Vergangenheit Plural von chegar",
     "«Os times ___ à volta com tudo em aberto.» A. chega · B. chegaram · C. chegamos", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando você chegar, apresente o documento.» «Quem tiver o cartão, confere o local.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Ter → tiver; ser → for; chegar → chegar (regular). Não confunda com o presente: é a gramática das hipóteses sobre o domingo.", 21.5)
c.bridge("Nach quando, se und quem steht das Futuro do Subjuntivo: tiver, for, chegar — Hypothesen zum Sonntag.")
c.ex("B2", "完成句子", "tiver", "quem + Futuro do Subjuntivo: tiver",
     "Quem ___ (ter) o cartão confere o local antes do domingo.", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "完成句子", "chegar", "quando + Futuro do Subjuntivo: chegar",
     "Quando você ___ (chegar) ao local, apresente o documento.", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "完成句子", "for", "se + Futuro do Subjuntivo von ser: for",
     "Se o seu local ___ (ser) novo, saia mais cedo de casa.", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "单选", "B", "quando + Zukunft → Futuro do Subjuntivo: for",
     "«Quando ___ domingo, o país faz a prova.» A. é · B. for · C. seja", size=20.5, gap=10)
c.end_report()

# ---- col 3: erros comuns + a palavra + cartas ----
bx = COLX[3]
errs = [
    ("«Vou fazer o Enem de caneta azul.»", "→ «De caneta preta.» A caneta do Enem é preta.", "Nur schwarzer Stift — blau gilt nicht."),
    ("«Chego às 13h30, na hora da prova.»", "→ «Chego antes das 13h.» Os portões fecham às 13h.", "13 Uhr Schluss — 13:30 Uhr ist zu spät."),
    ("«Vou revisar a noite inteira na véspera.»", "→ «Vou dormir bem na véspera.» Quem dorme lembra melhor.", "Kein Pauken nachts — Schlaf hilft mehr."),
    ("«O feriadão é de 2 a 5 de novembro.»", "→ «O feriadão é de 31 a 2.» Três dias: sábado, domingo e segunda.", "Feriadão: 31. Oktober bis 2. November."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 198
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS · HÄUFIGE FEHLER", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 22
wt = "« feriadão »: sábado, domingo e segunda — três dias de descanso."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("feriadão = langes Feiertagswochenende.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA · WORT DER WOCHE", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "feriadão = langes Feiertagswochenende.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 14
lt = "«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO"
# FIX1 (independent proof, Problem 1 — promise gap): on-page deferral disclosure.
# VOL.1 promised real letters + best P8 texts for VOL.2; none had arrived by press
# time, so the labeled editor's example stays and the promise carries to VOL.3.
# No letters/texts fabricated; existing labeling kept verbatim.
disc_pt = "Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3."
disc_cn = "Anmerkung: Echte Briefe und beste Texte kamen bis Redaktionsschluss nicht an — Beispiel bleibt, Versprechen gilt für VOL.3."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Beispiel der Redaktion. Schreiben Sie uns! Beste Briefe erscheinen in VOL.3.", "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap(disc_pt, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_cn, "sans", False, 19.5, CW - 44)) * 29 + 35
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, "Beispiel der Redaktion. Schreiben Sie uns! Beste Briefe erscheinen in VOL.3.", 20, "sans", False, GREY, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 10, disc_pt, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 10, disc_cn, 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASES DA SEMANA · SÄTZE DER WOCHE (wörtlich aus dieser Ausgabe)", 27, "sans", True, OLIVE)
quotes = [
    ("«Do feriadão à prova: a semana do Enem»", "Vom langen Wochenende zur Prüfung: die Enem-Woche.", "Página 1"),
    ("«Muita gente viaja, visita a família e vai ao cemitério levar flores»", "Viele reisen, besuchen die Familie und bringen Blumen auf den Friedhof.", "Página 1"),
    ("«Finados é o dia da memória»", "Finados ist der Tag der Erinnerung.", "Página 2"),
    ("«lembrar é um jeito de continuar perto»", "Erinnern heißt, weiterhin nahe zu bleiben.", "Página 3"),
    ("«cada ponto vale uma posição, cada gol vale uma história»", "Jeder Punkt ist ein Platz wert, jedes Tor eine Geschichte.", "Página 4"),
    ("«quem dorme bem lembra melhor»", "Wer gut schläft, behält mehr.", "Página 5"),
    ("«primeiro as fáceis, depois as difíceis»", "Zuerst die leichten Aufgaben, dann die schweren.", "Página 6"),
    ("«Confira o cartão, durma bem, chegue cedo»", "Karte prüfen, gut schlafen, früh da sein.", "Página 2"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 128  # FIX1: tightened from 158 so the taller letters box leaves the preview box clear
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA · NÄCHSTE AUSGABE (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Domingo 15 de novembro: o segundo dia do Enem — Natureza e Matemática. E o feriado da Proclamação da República. Mais: as suas cartas e os melhores textos da página 8. Até segunda!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
