# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA · 언어", "A Lucerna", "언어 집중 · Três níveis, três ferramentas · 세 단계, 세 가지 도구")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · PERGUNTAS E O PRESENTE", 24)
a.para("Para perguntar o essencial da semana: «Que horas começa a prova?» — que horas + verbo no presente. E, para lugares, «Onde fica o meu local?» — onde fica.", 21.5)
a.para("E conferir é especial na primeira pessoa: eu confiro, você confere, ele confere. Nós conferimos, eles conferem.", 21.5)
a.bridge("의문문: que horas (몇 시) + 동사; onde fica는 장소를 물어요; conferir의 eu 형태는 불규칙해요: confiro")
a.ex("A2", "문장 완성", "confiro", "conferir: eu → confiro (불규칙)",
     "Eu ___ (conferir) o cartão.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "confere", "conferir: você → confere",
     "Você ___ (conferir) o local antes de sair.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "começa", "começar: ela → começa",
     "Que horas ___ (começar) a prova?", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "객관식", "B", "onde는 장소를 물어요",
     "«___ fica o meu local?» A. Que horas · B. Onde · C. Quando", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · O PRETÉRITO PERFEITO", 24)
b.para("Para contar a semana, usamos o pretérito perfeito: eu revisei, ele chegou, ele dormiu. Revisar é regular: eu revisei, ele revisou.", 21.5)
b.para("E o modelo é simples: chegar → chegou; dormir → dormiu; separar → separei. Atenção ao acento: saíram, caíram.", 21.5)
b.bridge("한 주 일을 말할 때는 과거형(pretérito perfeito)을 써요; revisar는 규칙적이에요(revisei); chegar/dormir의 과거형은 강세에 주의하세요.")
b.ex("B1", "문장 완성", "revisei", "revisar 과거형: revisei",
     "Eu ___ (revisar) um pouco por dia.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "chegou", "chegar 과거형: chegou",
     "O candidato ___ (chegar) cedo.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "dormiu", "dormir 과거형: dormiu",
     "Ele ___ (dormir) bem na véspera.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "객관식", "B", "chegaram은 chegar의 과거형 복수예요",
     "«Os times ___ à volta com tudo em aberto.» A. chega · B. chegaram · C. chegamos", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando você chegar, apresente o documento.» «Quem tiver o cartão, confere o local.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Ter → tiver; ser → for; chegar → chegar (regular). Não confunda com o presente: é a gramática das hipóteses sobre o domingo.", 21.5)
c.bridge("quando, se, quem 뒤에는 접속법 미래를 써요: tiver, for, chegar (일요일 가정).")
c.ex("B2", "문장 완성", "tiver", "quem + 접속법 미래: tiver",
     "Quem ___ (ter) o cartão confere o local antes do domingo.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "chegar", "quando + 접속법 미래: chegar",
     "Quando você ___ (chegar) ao local, apresente o documento.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "for", "se + ser의 접속법 미래: for",
     "Se o seu local ___ (ser) novo, saia mais cedo de casa.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "객관식", "B", "quando + 미래 → 접속법 미래 for",
     "«Quando ___ domingo, o país faz a prova.» A. é · B. for · C. seja", size=20.5, gap=10)
c.end_report()

# ---- col 3: erros comuns + a palavra + cartas ----
bx = COLX[3]
errs = [
    ("«Vou fazer o Enem de caneta azul.»", "→ «De caneta preta.» A caneta do Enem é preta.", "엔엠에는 검은 펜을 써요, 파란 펜은 안 돼요."),
    ("«Chego às 13h30, na hora da prova.»", "→ «Chego antes das 13h.» Os portões fecham às 13h.", "13시에 문이 닫혀요, 13:30에 도착하면 늦어요."),
    ("«Vou revisar a noite inteira na véspera.»", "→ «Vou dormir bem na véspera.» Quem dorme lembra melhor.", "시험 전날 밤 벼락치기는 소용없어요, 푹 자야 기억이 나요."),
    ("«O feriadão é de 2 a 5 de novembro.»", "→ «O feriadão é de 31 a 2.» Três dias: sábado, domingo e segunda.", "연휴는 10월 31일부터 11월 2일까지 3일이에요."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 198
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS · 흔한 실수", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 22
wt = "« feriadão »: sábado, domingo e segunda — três dias de descanso."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("feriadão = 주말과 이어진 3일 연휴예요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA · 이번 주 단어", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "feriadão = 주말과 이어진 3일 연휴예요.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 22
lt = "«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO"
# FIX1 (independent proof, Problem 1 — promise gap): on-page deferral disclosure.
# VOL.1 promised real letters + best P8 texts for VOL.2; none had arrived by press
# time, so the labeled editor's example stays and the promise carries to VOL.3.
# No letters/texts fabricated; existing labeling kept verbatim.
disc_pt = "Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3."
disc_ko = "편집부 알림: VOL.1에서 약속한 실제 편지와 최고의 작문은 마감 때까지 오지 않았어요. 이번 호에는 예시를 싣고, 약속은 VOL.3으로 이어져요."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("편집부 예시예요, 실제 편지가 아니에요. 편지를 편집부로 보내 주세요! VOL.3에 실어요!", "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap(disc_pt, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_ko, "sans", False, 19.5, CW - 44)) * 29 + 35
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, "편집부 예시예요, 실제 편지가 아니에요. 편지를 편집부로 보내 주세요! VOL.3에 실어요!", 20, "sans", False, GREY, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 10, disc_pt, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 10, disc_ko, 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASES DA SEMANA · 이번 주 금문장 (이 판의 문장 그대로)", 27, "sans", True, OLIVE)
quotes = [
    ("«Do feriadão à prova: a semana do Enem»", "연휴에서 시험까지: 엔엠 주간.", "Página 1"),
    ("«Muita gente viaja, visita a família e vai ao cemitério levar flores»", "많은 사람들이 여행하고, 가족을 만나고, 묘지에 꽃을 가져가요.", "Página 1"),
    ("«Finados é o dia da memória»", "위령절은 추억의 날이에요.", "Página 2"),
    ("«lembrar é um jeito de continuar perto»", "추억하는 것은 가까이 지내는 방법이에요.", "Página 3"),
    ("«cada ponto vale uma posição, cada gol vale uma história»", "1점은 한 순위, 1골은 한 이야기예요.", "Página 4"),
    ("«quem dorme bem lembra melhor»", "푹 자면 잘 기억나요.", "Página 5"),
    ("«primeiro as fáceis, depois as difíceis»", "쉬운 것부터, 어려운 것은 나중에.", "Página 6"),
    ("«Confira o cartão, durma bem, chegue cedo»", "확인 카드를 확인하고, 푹 자고, 일찍 도착하세요.", "Página 2"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 104  # KO: tightened from 128 (ES precedent) so quotes clear the preview box
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA · 다음 주 예고 (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Domingo 15 de novembro: o segundo dia do Enem — Natureza e Matemática. E o feriado da Proclamação da República. Mais: as suas cartas e os melhores textos da página 8. Até segunda!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
