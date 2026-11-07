# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-pt-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA · 語言", "A Lucerna", "聚焦語言 · Três níveis, três ferramentas · 三個級別，三件工具")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · PERGUNTAS E O PRESENTE", 24)
a.para("Para perguntar o essencial da semana: «Que horas começa a prova?» — que horas + verbo no presente. E, para lugares, «Onde fica o meu local?» — onde fica.", 21.5)
a.para("E conferir é especial na primeira pessoa: eu confiro, você confere, ele confere. Nós conferimos, eles conferem.", 21.5)
a.bridge("提問句：que horas（幾點）+ 動詞；onde fica 問地點；conferir 的 eu 形式不規則：confiro")
a.ex("A2", "完成句子", "confiro", "conferir：eu → confiro（不規則）",
     "Eu ___ (conferir) o cartão.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "confere", "conferir：você → confere",
     "Você ___ (conferir) o local antes de sair.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "termina", "terminar：ela → termina",
     "Que horas ___ (terminar) a prova do dia 15?", instr="填空", size=20.5, gap=10)
a.ex("A2", "單選", "B", "onde 問地點",
     "«___ fica o meu local?» A. Que horas · B. Onde · C. Quando", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · O PRETÉRITO PERFEITO", 24)
b.para("Para contar a semana, usamos o pretérito perfeito: o Grêmio venceu, Maurício marcou, o candidato chegou. Vencer é regular: eu venci, ele venceu.", 21.5)
b.para("E o modelo é simples: marcar → marcou; chegar → chegou; dormir → dormiu. Atenção ao acento: saíram, caíram.", 21.5)
b.bridge("講一週的事用過去時（pretérito perfeito）；vencer 規則（venceu）；marcar/chegar/dormir 的過去時注意重音。")
b.ex("B1", "完成句子", "venceu", "vencer 過去時：venceu",
     "O Grêmio ___ (vencer) por 2 a 0.", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "marcou", "marcar 過去時：marcou",
     "Maurício ___ (marcar) o gol do Palmeiras.", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "chegou", "chegar 過去時：chegou",
     "O candidato ___ (chegar) cedo.", instr="填空", size=20.5, gap=10)
b.ex("B1", "單選", "B", "venceram 是 vencer 的過去時複數",
     "«Os times ___ a ida com vantagem.» A. vence · B. venceram · C. vencemos", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando você chegar, apresente o documento.» «Quem tiver o cartão, confere o local.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Ter → tiver; ser → for; chegar → chegar (regular). Não confunda com o presente: é a gramática das hipóteses sobre o domingo.", 21.5)
c.bridge("quando、se、quem 後用虛擬式將來：tiver、for、chegar（週日假設）。")
c.ex("B2", "完成句子", "tiver", "quem + 虛擬式將來：tiver",
     "Quem ___ (ter) o cartão confere o local antes do domingo.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "chegar", "quando + 虛擬式將來：chegar",
     "Quando você ___ (chegar) ao local, apresente o documento.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "for", "se + ser 的虛擬式將來：for",
     "Se o seu local ___ (ser) novo, saia mais cedo de casa.", instr="填空", size=20.5, gap=10)
c.ex("B2", "單選", "B", "quando + 未來 → 虛擬式將來 for",
     "«Quando ___ domingo, o país faz a prova.» A. é · B. for · C. seja", size=20.5, gap=10)
c.end_report()

# ---- col 3: erros comuns + a palavra + cartas ----
bx = COLX[3]
errs = [
    ("«Vou fazer o Enem de caneta azul.»", "→ «De caneta preta.» A caneta do Enem é preta.", "高考用黑筆，藍筆不行。"),
    ("«Chego às 13h30, na hora da prova.»", "→ «Chego antes das 13h.» Os portões fecham às 13h.", "13 點關門，13:30 到就晚了。"),
    ("«No dia 15, a prova termina às 19h.»", "→ «Termina às 18h30.» Às 19h, só no dia 8.", "15 日考試 18:30 結束，19 點是 8 日的時間。"),
    ("«O feriado dá folga na segunda.»", "→ «O feriado cai num domingo.» Não há folga extra.", "假日落在週日，週一不補休。"),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 198
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS · 常見錯誤", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 22
wt = "« proclamação »: o ato de anunciar — em 1889, o fim da monarquia e o começo da República."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("proclamação = 宣佈；1889 年君主制結束、共和國開始。", "sans", False, 20, CW - 44)) * 29 + 30
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA · 本週生詞", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "proclamação = 宣佈；1889 年君主制結束、共和國開始。", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 22
lt = "«Vou fazer o segundo dia no domingo 15. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO"
# W46 disclosure: VOL.2 promised real letters + best P8 texts for VOL.3; none had
# arrived by press time, so the labeled editor's example stands and the promise
# carries to VOL.4. No letters/texts fabricated; labeling kept verbatim in form.
disc_pt = "Nota da redação: as cartas reais e os melhores textos prometidos no VOL.2 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.4."
disc_tw = "編輯部說明：上期（VOL.2）承諾的真實來信與最佳作文截稿時未收到，本期仍刊示例，順延至下期（VOL.4）。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("編輯部示例，非真實來信。真實來信請寄編輯部，下期見！", "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap(disc_pt, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_tw, "sans", False, 19.5, CW - 44)) * 29 + 35
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, "編輯部示例，非真實來信。真實來信請寄編輯部，下期見！", 20, "sans", False, GREY, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 10, disc_pt, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 10, disc_tw, 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASES DA SEMANA · 本週金句（逐字摘自本期文章）", 27, "sans", True, OLIVE)
quotes = [
    ("«Dois domingos, um feriado: o Brasil faz o segundo dia do Enem»", "兩個週日、一個假日：巴西迎來高考第二天。", "Página 1"),
    ("«A prova e o feriado chegam no mesmo dia»", "考試和假日在同一天到來。", "Página 1"),
    ("«o feriado não muda o relógio»", "假日不改變時鐘。", "Página 2"),
    ("«A monarquia acabou»", "君主制結束了。", "Página 3"),
    ("«quem vai à final da Copa do Brasil?»", "誰能進巴西杯決賽？", "Página 4"),
    ("«quem dorme bem lembra melhor»", "睡得好，記得牢。", "Página 5"),
    ("«primeiro as fáceis, depois as difíceis»", "先做容易的，再做難的。", "Página 6"),
    ("«Confira o cartão, durma bem, chegue cedo»", "核對確認卡、睡好、早到。", "Página 2"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 108
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA · 下期預告 (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Sexta, 20 de novembro: o feriado da Consciência Negra. E os finalistas da Copa do Brasil, os gabaritos do Enem e as suas cartas e os melhores textos da página 8. Até segunda!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
