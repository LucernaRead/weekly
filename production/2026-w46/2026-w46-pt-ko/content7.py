# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA　언어", "A Lucerna", "Três níveis, três ferramentas　세 단계, 세 가지 도구")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　PERGUNTAS E O PRESENTE", 24)
a.para("Para perguntar o essencial da semana: «Que horas começa a prova?» — que horas + verbo no presente. E, para lugares, «Onde fica o meu local?» — onde fica.", 21.5)
a.para("E conferir é especial na primeira pessoa: eu confiro, você confere, ele confere. Nós conferimos, eles conferem.", 21.5)
a.bridge("의문문: que horas(몇 시) + 동사. onde fica는 장소를 묻어요. conferir의 eu형은 불규칙: confiro.")
a.ex("A2", "문장 완성하기", "confiro", "conferir: eu → confiro(불규칙)",
     "Eu ___ (conferir) o cartão.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성하기", "confere", "conferir: você → confere",
     "Você ___ (conferir) o local antes de sair.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성하기", "termina", "terminar: ela → termina",
     "Que horas ___ (terminar) a prova do dia 15?", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "객관식", "B", "onde는 장소를 물어요",
     "«___ fica o meu local?» A. Que horas · B. Onde · C. Quando", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　O PRETÉRITO PERFEITO", 24)
b.para("Para contar a semana, usamos o pretérito perfeito: o Grêmio venceu, Maurício marcou, o candidato chegou. Vencer é regular: eu venci, ele venceu.", 21.5)
b.para("E o modelo é simples: marcar → marcou; chegar → chegou; dormir → dormiu. Atenção ao acento: saíram, caíram.", 21.5)
b.bridge("한 주의 일을 말할 때는 과거형(pretérito perfeito)을 써요. vencer는 규칙적(venceu). marcar·chegar·dormir의 과거형 강세에 주의하세요.")
b.ex("B1", "문장 완성하기", "venceu", "vencer 과거형: venceu",
     "O Grêmio ___ (vencer) por 2 a 0.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성하기", "marcou", "marcar 과거형: marcou",
     "Maurício ___ (marcar) o gol do Palmeiras.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성하기", "chegou", "chegar 과거형: chegou",
     "O candidato ___ (chegar) cedo.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "객관식", "B", "venceram은 vencer의 과거형 복수예요",
     "«Os times ___ a ida com vantagem.» A. vence · B. venceram · C. vencemos", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando você chegar, apresente o documento.» «Quem tiver o cartão, confere o local.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Ter → tiver; ser → for; chegar → chegar (regular). Não confunda com o presente: é a gramática das hipóteses sobre o domingo.", 21.5)
c.bridge("quando·se·quem 뒤에는 미래 접속법: tiver·for·chegar(일요일 가정의 문법).")
c.ex("B2", "문장 완성하기", "tiver", "quem + 미래 접속법: tiver",
     "Quem ___ (ter) o cartão confere o local antes do domingo.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성하기", "chegar", "quando + 미래 접속법: chegar",
     "Quando você ___ (chegar) ao local, apresente o documento.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성하기", "for", "se + ser의 미래 접속법: for",
     "Se o seu local ___ (ser) novo, saia mais cedo de casa.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "객관식", "B", "quando + 미래 → 미래 접속법 for",
     "«Quando ___ domingo, o país faz a prova.» A. é · B. for · C. seja", size=20.5, gap=10)
c.end_report()

# ---- col 3: erros comuns + a palavra + cartas ----
bx = COLX[3]
errs = [
    ("«Vou fazer o Enem de caneta azul.»", "→ «De caneta preta.» A caneta do Enem é preta.", "검은 펜만 써요. 파란 펜은 안 돼요."),
    ("«Chego às 13h30, na hora da prova.»", "→ «Chego antes das 13h.» Os portões fecham às 13h.", "13시 폐문. 13:30에 오면 늦어요."),
    ("«No dia 15, a prova termina às 19h.»", "→ «Termina às 18h30.» Às 19h, só no dia 8.", "15일 시험은 18:30에 끝나요. 8일은 19시 종료."),
    ("«O feriado dá folga na segunda.»", "→ «O feriado cai num domingo.» Não há folga extra.", "공휴일이 일요일에 겹쳐도 월요일에 쉬지 않아요."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 40))) * 29.5 + 10 for r in errs) + 16 + 198
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS　흔한 실수", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 40, 1.36) + 10
wy = 200 + eh + 22
wt = "« proclamação »: o ato de anunciar — em 1889, o fim da monarquia e o começo da República."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("proclamação = 선포. 1889년, 군주제가 끝나고 공화국이 시작되었어요.", "sans", False, 20, CW - 44)) * 29 + 30
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA　이번 주 단어", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "proclamação = 선포. 1889년, 군주제가 끝나고 공화국이 시작되었어요.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 22
lt = "«Vou fazer o segundo dia no domingo 15. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO"
# W46 disclosure: VOL.2 promised real letters + best P8 texts for VOL.3; none had
# arrived by press time, so the labeled editor's example stands and the promise
# carries to VOL.4. No letters/texts fabricated; labeling kept verbatim in form.
disc_pt = "Nota da redação: as cartas reais e os melhores textos prometidos no VOL.2 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.4."
disc_ko = "편집부 알림: VOL.2에서 약속한 실제 편지와 최고의 작문은 마감 때까지 오지 않았어요. 이번 호에는 예시를 싣고, 약속은 VOL.4로 이어져요."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("편집부 예시예요, 실제 편지가 아니에요. 편지를 편집부로 보내 주세요!", "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap(disc_pt, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_ko, "sans", False, 19.5, CW - 44)) * 29 + 35
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, "편집부 예시예요, 실제 편지가 아니에요. 편지를 편집부로 보내 주세요!", 20, "sans", False, GREY, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 10, disc_pt, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 10, disc_ko, 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 30)
p.hline(MX, RIGHT, fy - 2, OLIVE, 2)  # rule below the CARTAS box (fy-14 cut the last line)
p.text(MX, fy + 24, "FRASES DA SEMANA　이번 주의 명문장(이 호 기사에서 그대로 인용)", 27, "sans", True, OLIVE)
quotes = [
    ("«Dois domingos, um feriado: o Brasil faz o segundo dia do Enem»", "두 번의 일요일, 하나의 공휴일: 브라질은 Enem 둘째 날을 맞이해요.", "Página 1"),
    ("«A prova e o feriado chegam no mesmo dia»", "시험과 공휴일이 같은 날에 와요.", "Página 1"),
    ("«o feriado não muda o relógio»", "공휴일은 시계를 바꾸지 않아요.", "Página 2"),
    ("«A monarquia acabou»", "군주제는 끝났어요.", "Página 3"),
    ("«quem vai à final da Copa do Brasil?»", "코파 두 브라지우 결승에는 누가 오를까요?", "Página 4"),
    ("«quem dorme bem lembra melhor»", "잠을 잘 자면 잘 기억해요.", "Página 5"),
    ("«primeiro as fáceis, depois as difíceis»", "쉬운 것부터, 그다음에 어려운 것.", "Página 6"),
    ("«Confira o cartão, durma bem, chegue cedo»", "확인 카드를 확인하고, 푹 자고, 일찍 오세요.", "Página 2"),
]
colw = (RIGHT - MX - GUT) // 2
fr_end = 0  # lowest Frases translation end (adaptive band)
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 94
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    fr_end = max(fr_end, p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35))

# ---- próxima semana ----
py = max(2404, fr_end - 12)  # adaptive: keep the band clear of the Frases translations
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA　다음 주 예고 (VOL.4)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Sexta, 20 de novembro: o feriado da Consciência Negra. E os finalistas da Copa do Brasil, os gabaritos do Enem e as suas cartas e os melhores textos da página 8. Até segunda!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
