# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LÍNGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LÍNGUA　語言", "A Lucerna", "聚焦語言　Três níveis, três ferramentas　三個程度，三件工具")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　O FERIADO E AS DATAS", 24)
a.para("Para falar de um feriado, usamos «em» com a data: «em 20 de novembro». E, para o dia, «no dia 20». E o verbo da semana é «cair»: o feriado cai numa sexta — cair é o verbo dos feriados no calendário.", 21.5)
a.para("E «aproveitar» é o verbo do feriadão: eu aproveito, você aproveita, nós aproveitamos.", 21.5)
a.bridge("說假日用 em + 日期（em 20 de novembro）、no dia 20；cair 表「落在某日」；aproveitar 的變位。")
a.ex("A2", "完成句子", "em", "em + 日期：em 20 de novembro",
     "O feriado é ___ 20 de novembro.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "numa", "cair numa sexta-feira：落在週五",
     "O feriado cai ___ sexta-feira.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "é", "ser 現在式 ele 形式：é",
     "Que dia ___ (ser) o feriado?", instr="填空", size=20.5, gap=10)
a.ex("A2", "單選", "B", "aproveitar：nós 形式 aproveitamos",
     "«Nós ___ o feriadão.» A. aproveita · B. aproveitamos · C. aproveito", size=20.5, gap=10)
a.end_report()
a_end = a.y

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　O PRETÉRITO PERFEITO", 24)
b.para("Para contar o fim de semana da Copa, usamos o pretérito perfeito: o Grêmio empatou, o Vasco venceu, Norris venceu. Empatar é regular: eu empatei, ele empatou.", 21.5)
b.para("E o modelo é simples: abrir → abriu; garantir → garantiu; sair → saiu. Atenção ao acento: saíram, caíram.", 21.5)
b.bridge("講巴西盃週末用過去式（pretérito perfeito）；empatar 規則（empatou）；abrir/garantir/sair 的過去式注意重音。")
b.ex("B1", "完成句子", "empatou", "empatar 過去式：empatou",
     "O Grêmio ___ (empatar) por 1 a 1.", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "venceu", "vencer 過去式：venceu",
     "O Vasco ___ (vencer) por 2 a 1.", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "abriu", "abrir 過去式：abriu",
     "Renan Lodi ___ (abrir) o placar.", instr="填空", size=20.5, gap=10)
b.ex("B1", "單選", "B", "saíram 是 sair 的過去式複數",
     "«Os finalistas ___ no fim de semana.» A. saem · B. saíram · C. sairão", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　O FUTURO DO SUBJUNTIVO", 24)
c.para("Depois de «quando», «se» e «quem», o futuro pede o subjuntivo: «Quando sair o gabarito, confira as respostas.» «Se a sua nota for boa, comemore.»", 21.5)
c.para("É o tempo da página 6: regras e condições. Sair → sair; ser → for; ter → tiver. Não confunda com o presente: é a gramática das hipóteses sobre o gabarito.", 21.5)
c.bridge("quando、se、quem 後面用虛擬式未來：sair、for、tiver（等官方答案的假設）。")
c.ex("B2", "完成句子", "sair", "quando + 虛擬式未來：sair",
     "Quando ___ (sair) o gabarito, confira as respostas.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "for", "se + ser 的虛擬式未來：for",
     "Se a sua nota ___ (ser) boa, comemore.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "tiver", "quem + 虛擬式未來：tiver",
     "Quem ___ (ter) o cartão confere o local antes do domingo.", instr="填空", size=20.5, gap=10)
c.ex("B2", "單選", "B", "quando + 未來 → 虛擬式未來 sair",
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
    ("«O gabarito já saiu no domingo 15.»", "→ «Só o extraoficial.» O oficial do Inep sai até o fim de novembro.", "官方答案要到 11 月底才出，週日晚上只有非官方版。"),
    ("«O feriado dá folga na segunda, 23.»", "→ «Não há folga extra.» O feriadão termina no domingo 22.", "連休週日結束，週一不補休。"),
    ("«O Palmeiras passou no tempo normal.»", "→ «Passou nos pênaltis, 5 a 4.» No tempo normal, o Vasco venceu por 2 a 1.", "帕爾梅拉斯十二碼 5 比 4 晉級，正規時間瓦斯科 2 比 1 贏了。"),
    ("«O dia 20 cai num domingo.»", "→ «Cai numa sexta-feira.» O feriadão vai de 20 a 22.", "11 月 20 日是週五，連休到 22 日週日。"),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 198
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERROS COMUNS　常見錯誤", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 22
wt = "« consciência »: saber e lembrar — de si, da história e dos outros. «Consciência Negra» é a memória da luta e da cultura afro-brasileiras."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("consciência = 意識、良知；黑人意識日：銘記抗爭與文化。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "A PALAVRA　本週生詞", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "consciência = 意識、良知；黑人意識日：銘記抗爭與文化。", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 22
lt = "«Vou aproveitar o feriadão para ler sobre Zumbi. Bom feriado!» — EXEMPLO DA REDAÇÃO"
# W47 disclosure: VOL.3 promised real letters + best P8 texts for VOL.4; none had
# arrived by press time, so the labeled editor's example stands and the promise
# carries to VOL.5. No letters/texts fabricated; labeling kept verbatim in form.
disc_pt = "Nota da redação: as cartas reais e os melhores textos do VOL.3 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.5."
disc_zh_tw = "編輯部說明：上期（VOL.3）承諾的真實來信與最佳作文截稿時未收到，本期仍刊示例，順延至下期（VOL.5）。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("編輯部示例，非真實來信。真實來信請寄編輯部，下期見！", "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap(disc_pt, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(disc_zh_tw, "sans", False, 19.5, CW - 44)) * 29 + 22
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DOS LEITORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, "編輯部示例，非真實來信。真實來信請寄編輯部，下期見！", 20, "sans", False, GREY, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 10, disc_pt, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 10, disc_zh_tw, 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases da semana (verbatim from this issue) ----
fy = max(1712, ly + lh + 16)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "FRASES DA SEMANA　本週金句（逐字摘自本期文章）", 27, "sans", True, OLIVE)
quotes = [
    ("«Consciência Negra: sexta é feriado em todo o país»", "黑人意識日：週五全國放假。", "Página 1"),
    ("«o feriado abre um fim de semana de três dias»", "假日開啟一個三天週末。", "Página 1"),
    ("«Zumbi nasceu em Palmares»", "祖比生於帕爾馬雷斯。", "Página 3"),
    ("«sem memória, não há futuro»", "沒有記憶，就沒有未來。", "Página 3"),
    ("«o agregado ficou em 2 a 2»", "總比數定格在 2 比 2。", "Página 4"),
    ("«a espera pelo gabarito»", "等待官方答案。", "Página 5"),
    ("«primeiro as fáceis, depois as difíceis»", "先做容易的，再做難的。", "Página 6"),
    ("«Confira o transporte, guarde o documento e aproveite o feriadão»", "先查交通、備好證件，再好好享受連假。", "Página 2"),
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
p.text(MX + 28, py + 44, "A PRÓXIMA SEMANA　下期預告 (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Sexta, 27 de novembro: a Black Friday. E o gabarito oficial do Enem, até o fim do mês — e a final da Copa se aproxima: dia 6 de dezembro, em Brasília. Até segunda!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
