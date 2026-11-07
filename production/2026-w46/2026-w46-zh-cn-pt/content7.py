# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-cn-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · O foco da língua", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Três níveis, três temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与包裹 · Compras", 24)
a.para("Palavras de compras desta semana: 高潮场 (gāocháochǎng, a venda de pico), 包裹 (bāoguǒ, uma encomenda), 取件码 (qǔjiànmǎ, um código de levantamento), 快递柜 (kuàidìguì, um cacifo de encomendas). Palavras de segurança: 消防 (xiāofáng, prevenção de incêndios), 疏散 (shūsàn, evacuar), 自救 (zìjiù, autorresgate).", 21.5)
a.glossline("Os classificadores ainda importam: 一个包裹 (uma encomenda), 一部电影 (um filme), 一场演练 (um simulacro).")
a.ex("A2", "完成句子", "个", "包裹 leva o classificador 个 gè.",
     "我拿了___包裹。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "单选", "A", "高潮场 significa a venda de pico.",
     "「高潮场」是什么意思? A. 最忙的卖货时间 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "消防", "xiāofáng — prevenção; 9 nov. Dia do Fogo.",
     "11月9日是全国___日。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "单选", "A", "As encomendas levam 个 — não 只 nem 条.",
     "哪个说法对? A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20.5, gap=10)
a.para("Mais uma para treinar: 「我的包裹到了吗?」 (A minha encomenda já chegou?) Quando esperas uma encomenda, pergunta primeiro e depois vai ao cacifo.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Horas e datas", 24)
b.para("O chinês dá as horas do maior para o menor: ano, mês, dia, dia da semana, parte do dia, hora. Exemplos deste número: 「11月9日星期一」 (seg. 9 nov.), 「11月10日星期二20点」 (ter. 10 nov., 20:00), 「11月15日星期日凌晨3点」 (dom. 15 nov., 3 da manhã). A maior unidade primeiro, nada fora de ordem.", 21.5)
b.glossline("Assim, o inglês «Monday, Nov 9» torna-se 11月9日星期一.")
b.ex("B1", "单选", "B", "凌晨 língchén — as horas pequenas depois da meia-noite.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "As 06:00 são 早上 — não à tarde.",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="Completa", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Ordem grande → pequeno: 15 nov., domingo, 03:00.",
     "哪个顺序对? A. 11月15日星期日凌晨3点 · B. 凌晨3点星期日11月15日 · C. 星期日凌晨3点11月15日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周一", "9 de novembro é segunda-feira — 周一.",
     "11月9日是星期一,也可以说___。消防日在这天。", instr="Completa", size=20.5, gap=10)
b.para("Mais duas palavras: 凌晨 (língchén) são as horas pequenas depois da meia-noite, antes do amanhecer; 傍晚 (bàngwǎn) é o curto intervalo mesmo antes de escurecer.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Ler as notícias", 24)
c.para("Quando uma história inclui uma afirmação (说法), separa três tipos de frase: afirmações (说法), dados (数据) e previsões (预报). A página 6 é o exemplo: 「最大的一波」 é uma afirmação sobre 11 de novembro, os múltiplos 1,5 e 2,5 são dados reportados, e as temperaturas do ar frio são uma previsão — prevista, ainda não um facto.", 21.5)
c.glossline("Pergunta perante cada número: de quem é e quando foi medido?")
c.ex("B2", "单选", "C", "「最大的一波」 é uma afirmação, não dados medidos.",
     "「最大的一波」在第6版里是什么? A. 数据 · B. 预报 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — números medidos, não afirmações.",
     "买东西以前,先看___,再看广告。", instr="Completa", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Dados e página de pagamento primeiro, título por último.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — uma previsão, ainda não um facto.",
     "冷空气的温度是___,还没发生。", instr="Completa", size=20.5, gap=10)
c.para("Tenta tu: no calendário da página 1, 「11月11日」 é uma data — dados. As palavras de um anúncio são afirmações. Consegues distingui-las?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) marca como se faz uma ação."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) liga verbo + grau: 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "Ordem: número + classificador + substantivo."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日,星期日凌晨3点。」", "As horas vão do maior ao menor: o dia da semana por último."),
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
wt = "「先看取件码,再开柜门。」(Vê o código e abre o cacifo.) A estrutura 先…再… dá a ordem das ações."
wcn = "Estrutura: 先 … 再 … — primeiro X, depois Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Estrutura de frase", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在北京。11月9日学校做了消防演练,我学会了走楼梯。双11我买了一本书,包裹两天就到了。周日凌晨,我想看S16总决赛!」"
lcn = "编辑部示例信,不是真实来信。VOL.2曾预告本期刊登真实来信和最佳作文;截至11月2日截稿,仍未收到,本期仍刊示例,继续征集。延期不是取消。Nota da redação: VOL.2 prometeu cartas reais em VOL.3; nenhuma chegou até 2 nov. O exemplo fica. Adiado, não cancelado."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · Canto dos leitores", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · Frases da semana (textuais, dos artigos deste número)", 27, "sans", True, OLIVE)
quotes = [
    ("「双11的正日子」", "O próprio dia do Double 11.", "Página 1"),
    ("「先看结算页,再决定买不买」", "Vê a página de pagamento e decide.", "Página 2"),
    ("「提高自防自救能力」", "Reforçar a autoproteção e o autorresgate.", "Página 3"),
    ("「三支队进了八强」", "Três equipas nos quartos.", "Página 4"),
    ("「输了就回家」", "Perdes e vais para casa.", "Página 4"),
    ("「老电影,新画面」", "Um filme antigo, uma imagem nova.", "Página 5"),
    ("「快递的高峰分三波」", "O pico de encomendas vem em três ondas.", "Página 6"),
    ("「着火了不坐电梯」", "Num incêndio, não tomes o elevador.", "Página 3"),
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
p.text(MX + 28, py + 44, "下期预告 · Na próxima semana (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16总决赛打完了,谁是冠军?包裹都到了吗?还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
