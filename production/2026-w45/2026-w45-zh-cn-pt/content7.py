# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Foco na língua", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Três níveis, três temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与冬天 · Compras", 24)
a.para("Palavras de compras desta semana: 现货 (xiànhuò, em estoque), 直降 (zhíjiàng, um corte direto), 立减 (lìjiǎn, desconto no checkout), 结算页 (jiésuàn yè, a página de checkout). Palavras de inverno: 立冬 (lìdōng, Início do Inverno), 补冬 (bǔdōng, comer bem antes do inverno), 厚衣服 (hòu yīfu, roupas quentes).", 21.5)
a.glossline("Os classificadores ainda importam: 一件毛衣 (um suéter), 一条围巾 (um cachecol), 一部电影 (um filme).")
a.ex("A2", "Complete a frase", "件", "毛衣 usa o classificador 件 jiàn.",
     "我想买一___毛衣。", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Escolha múltipla", "A", "直降 significa que o preço em si cai.",
     "「直降」是什么意思? A. 价格直接变低 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "Complete a frase", "立冬", "lìdōng — Início do Inverno, 7 de nov.",
     "11月7日是___。", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Escolha múltipla", "A", "Roupas usam 件, não 个 nem 条.",
     "哪个说法对? A. 一件毛衣 · B. 一个毛衣 · C. 一条毛衣", size=20.5, gap=10)
a.para("Mais um para praticar: 「这件毛衣多少钱?」 (Quanto custa este suéter?) Quando fizer compras, pergunte o preço primeiro e só depois pague.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Hora e datas", 24)
b.para("O chinês dá os horários do maior para o menor: ano, mês, dia, dia da semana, parte do dia, hora. Exemplos desta edição: 「11月7日星期六17点52分」 (sáb. 7 de nov., 17h52), 「11月10日星期二20点」 (ter. 10 de nov., 20h), 「11月15日凌晨3点」 (15 de nov., 3h da manhã). A maior unidade primeiro, nada fora de ordem.", 21.5)
b.glossline("Assim, «sábado à noite, 7 de novembro» vira 11月7日星期六晚上.")
b.ex("B1", "Escolha múltipla", "B", "凌晨 língchén — as horas pequenas depois da meia-noite.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "Complete a frase", "早上", "06:00 é 早上 (manhã), não noite.",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="Complete", size=20.5, gap=10)
b.ex("B1", "Escolha múltipla", "A", "Ordem do maior para o menor: 7 de nov., sábado, 17h52.",
     "哪个顺序对? A. 11月7日星期六17点52分 · B. 17点52分星期六11月7日 · C. 星期六17点52分11月7日", size=20.5, gap=10)
b.ex("B1", "Complete a frase", "周六", "7 de novembro é sábado — 周六.",
     "11月7日是星期六,也可以说___。立冬在这天。", instr="Complete", size=20.5, gap=10)
b.para("Mais duas palavras: 凌晨 (língchén) são as horas pequenas depois da meia-noite, antes do amanhecer; 傍晚 (bàngwǎn) é o trechinho logo antes de escurecer.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Lendo as notícias", 24)
c.para("Quando uma notícia envolve uma afirmação (说法), separe três tipos de frase: afirmações (说法), dados (数据) e propagandas (广告). A página 6 é o exemplo: 「最低价」 é uma afirmação, os 270元 das cestas de prática são dados de prática, e a página de checkout mostra o que você realmente paga.", 21.5)
c.glossline("Pergunte de cada preço: de quem é o número, e onde ele está escrito?")
c.ex("B2", "Escolha múltipla", "C", "「最低价」 é propaganda, não dado medido.",
     "「最低价」在第6版里是什么? A. 数据 · B. 声明 · C. 说法", size=20.5, gap=10)
c.ex("B2", "Complete a frase", "数据", "shùjù — números medidos, não afirmações.",
     "买东西以前,先看___,再看广告。", instr="Complete", size=20.5, gap=10)
c.ex("B2", "Escolha múltipla", "B", "Dados e checkout primeiro; a manchete por último.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "Complete a frase", "结算", "jiésuàn — a página de checkout mostra o preço real.",
     "真正要付的钱,看___页的价格。", instr="Complete", size=20.5, gap=10)
c.para("Tente você: na caixa de calendário da página 1, 「11月7日」 é uma data — um dado. As palavras de uma propaganda são afirmações. Você sabe distingui-las?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de) marca como uma ação é feita."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de) liga verbo + grau: 跑得快."),
    ("「我买了三只毛衣个」", "→ 「我买了三件毛衣。」", "Ordem: número + classificador + substantivo. O 个 final é um a mais; suéteres usam 件."),
    ("「立冬在星期六十一月七日」", "→ 「立冬在11月7日,星期六。」", "Maior → menor: dia da semana por último."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所 · Clínica de erros", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看评价,再下单。」(Primeiro veja as avaliações, depois faça o pedido.) A estrutura 先…再… dá a ordem das ações. Mais: 「先看天气,再出门。」"
wcn = "先 … 再 … — primeiro X, depois Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Estrutura da semana", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在上海。立冬那天,我吃了饺子,也给妈妈打了电话。双11,我买了一件毛衣,现货第二天就到了。」"
lcn = "Exemplo da redação — não é uma carta de verdade. O VOL.1 prometeu cartas verdadeiras dos leitores e o melhor texto do VOL.1 neste VOL.2; até agora nenhuma carta chegou e não há texto publicável, por isso este cantinho ainda traz um exemplo da redação. Adiado, não cancelado. Escreva-nos! Envie a sua carta em chinês — duas frases já bastam — e ela pode sair no próximo número."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
# NOTE: the disclosure above mixes Chinese and English in one string; the
# sans wrap measures CJK and Latin with the same SC face, so the height
# formula above (sans, 20pt) matches the render path. Verified in the build log.
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · Cantinho dos leitores", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · Frases da semana (textuais, dos artigos desta edição)", 27, "sans", True, OLIVE)
quotes = [
    ("「不用等11月11日」", "Não é preciso esperar até 11 de novembro.", "Página 1"),
    ("「下单就能发货」", "Fez o pedido e já despacha.", "Página 2"),
    ("「先看结算页,再付款」", "Veja a página de checkout e só depois pague.", "Página 2"),
    ("「水开始结冰」", "A água começa a congelar.", "Página 3"),
    ("「三场都输了」", "As três séries perdidas.", "Página 4"),
    ("「小局一场没赢」", "Nenhum jogo ganho.", "Página 4"),
    ("「故事够不够好」", "Mas a história é boa o bastante?", "Página 5"),
    ("「别以后,就现在」", "Não depois — agora.", "Página 5"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 150
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 150 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期预告 · Na próxima semana (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "双11当天11月11日星期三,包裹到了吗?S16淘汰赛打完了,谁进了决赛?总决赛北京时间11月15日凌晨3点。还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
