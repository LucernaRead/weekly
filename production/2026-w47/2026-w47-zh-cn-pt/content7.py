# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语　Foco de língua", "Lucerna", "语言聚焦　三个级别，三个主题　Três níveis, três temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　决赛与包裹　Final e pacotes", 24)
a.para("Palavras da semana: 决赛 (juésài, a final), 冠军 (guànjūn, o campeão), 半决赛 (bànjuésài, a meia-final), 到货 (dàohuò, chegada), 退换货 (tuìhuànhuò, devoluções e trocas), 价保 (jiàbǎo, proteção de preço).", 21.5)
a.glossline("Os classificadores ainda importam: 一个包裹 (uma encomenda), 一部电影 (um filme), 一场演练 (um simulacro).")
a.ex("A2", "完成句子", "个", "包裹 leva o classificador 个 gè.",
     "我拿了___包裹。", instr="Completa", size=20, gap=10)
a.ex("A2", "单选", "A", "决赛 quer dizer a final, o último jogo.",
     "「决赛」是什么意思？ A. 最后一场比赛 · B. 第一场比赛 · C. 练习赛", size=20, gap=10)
a.ex("A2", "完成句子", "决赛", "juésài — a final; BLG contra GEN a 15 nov.",
     "11月15日凌晨3点，BLG和GEN打___。", instr="Completa", size=20, gap=10)
a.ex("A2", "单选", "A", "As encomendas levam 个 — não 只 nem 条.",
     "哪个说法对？ A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20, gap=10)
a.para("Mais um para praticar: 「我的包裹到了吗？」 (A minha encomenda chegou?) Quando esperas uma encomenda, pergunta primeiro e depois vai ao cacifo.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　时间与日期　Hora e datas", 24)
b.para("O chinês ordena o tempo do maior para o menor: ano, mês, dia, dia da semana, parte do dia, hora. Exemplos deste número: 「11月15日星期日凌晨3点」 (dom. 15 nov., 3 da manhã), 「11月22日星期日」 (dom. 22 nov.), 「11月21日星期六」 (sáb. 21 nov.). A unidade maior primeiro, nada fora de ordem.", 21.5)
b.glossline("Assim, «Sunday, Nov 22» em inglês fica 11月22日星期日.")
b.ex("B1", "单选", "B", "凌晨 língchén — as horas pequenas depois da meia-noite.",
     "「凌晨3点」是什么时候？ A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20, gap=10)
b.ex("B1", "完成句子", "早上", "As 06:00 são 早上 — não à noite.",
     "半决赛在北京时间11月8日___6点开始。（不是晚上）", instr="Completa", size=20, gap=10)
b.ex("B1", "单选", "A", "Ordem do maior para o menor: 22 nov., domingo.",
     "哪个顺序对？ A. 11月22日星期日 · B. 星期日11月22日 · C. 星期日小雪11月22日", size=20, gap=10)
b.ex("B1", "完成句子", "周日", "22 nov. é domingo — 周日.",
     "11月22日是星期日，也可以说___。小雪在这天。", instr="Completa", size=20, gap=10)
b.para("Mais duas palavras: 凌晨 (língchén) são as horas pequenas depois da meia-noite, antes do amanhecer; 傍晚 (bàngwǎn) é o curto intervalo mesmo antes de escurecer.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　读新闻　Ler as notícias", 24)
c.para("Quando uma história inclui uma afirmação (说法), separa três tipos de frases: afirmações (说法), dados (数据) e previsões (预报). A página 6 é o exemplo: « 没有爆掉 » é uma afirmação sobre as encomendas deste ano, o total 139.38亿件 são dados publicados — já contados, não uma suposição — e « 第三波是最高峰 » é uma previsão de 中通云仓: esperada, ainda não contada.", 21.5)
c.glossline("Pergunta perante cada número: de quem é e quando foi medido?")
c.ex("B2", "单选", "A", "« 139.38亿件 » é uma contagem final da administração postal, já contada.",
     "「139.38亿件」在第6版里是什么？ A. 已经数完的事实 · B. 邮政局的预计 · C. 广告词", size=20, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — números medidos, não afirmações.",
     "买东西以前，先看___，再看广告。", instr="Completa", size=20, gap=10)
c.ex("B2", "单选", "B", "Dados e página de pagamento primeiro, título por último.",
     "读新闻时，哪个做法最好？ A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — uma previsão, ainda não um facto.",
     "「第三波是最高峰」是___，还没发生。", instr="Completa", size=20, gap=10)
c.para("Experimenta: no quadro do calendário da página 1, « 11月22日 » é uma data — um dado. As palavras de um anúncio são afirmações. Consegues distingui-las?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters + image ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) marca como se faz uma ação."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) liga verbo + grau: 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "Ordem: número + classificador + substantivo."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日，星期日凌晨3点。」", "As horas vão do maior ao menor: o dia da semana por último."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所　Clínica de erros", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看预报，再决定穿什么。」A estrutura 先…再… dá a ordem das ações."
wcn = "Estrutura: 先 … 再 … — primeiro X, depois Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式　Estrutura frásica", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好！我住在上海。11月9日半决赛，我看了BLG打T1，3比1，真好看！双11我买了一件外套，包裹两天就到了。你们呢？」"
lcn = "编辑部示例信，不是真实来信。VOL.3曾预告本期刊登真实来信和最佳作文；截至11月10日截稿，仍未收到，继续征集。延期不是取消。Nota da redação: VOL.3 prometeu cartas reais; nenhuma chegou até 10 nov. Adiado, não cancelado."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地　Cantinho dos leitores", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- P7 image (brush) below the letters box ----
iy7 = col3_end + 12
image(p, "brush.jpg", bx, iy7, CW, 130)
cy7 = caption(p, bx, iy7 + 130, CW, "毛笔（资料图）。写中文，先从一笔一画开始。",
              "Foto: Mx. Granger — CC0 (Wikimedia Commons)")
img_end = cy7
print("P7 image ends", img_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, img_end + 44)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "本周金句　Frases da semana (à letra, dos artigos deste número)", 27, "sans", True, OLIVE)
quotes = [
    ("「决赛对阵GEN」", "A final: BLG contra GEN.", "Página 1"),
    ("「包裹都到了吗」", "Todas as encomendas chegaram?", "Página 2"),
    ("「小雪气寒而将雪矣」", "Neve Pequena: o ar arrefece, a neve vem aí.", "Página 3"),
    ("「两支中国队进了四强」", "Duas equipas chinesas chegaram às meias-finais.", "Página 4"),
    ("「先看简介，再决定」", "Lê primeiro a sinopse e depois decide.", "Página 5"),
    ("「无高峰，全高峰」", "Nenhum pico único — cada dia é um pico.", "Página 6"),
    ("「先打开看一看，再确认收货」", "Abre e verifica primeiro, depois confirma a receção.", "Página 6"),
    ("「悦读深圳」", "Ler com alegria em Shenzhen — o tema do Mês da Leitura de Shenzhen.", "Página 3"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 120
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 120 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "下期预告　Na próxima semana (VOL.5)", 24, "sans", True, GOOSE)
p.para(MX + 28, py + 84, "S16总决赛打完了，谁是冠军？小雪之后，冬天怎么过？还有你们的来信和第8版最佳作文。下周见！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
