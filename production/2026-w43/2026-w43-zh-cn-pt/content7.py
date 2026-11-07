# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Foco na língua", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Três níveis, três temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 购物与量词 · Os classificadores", 24)
a.para("Quando você faz compras, o chinês usa classificadores (量词): 一件外套 (um casaco), 一条围巾 (um cachecol), 一斤蟹 (meio quilo de caranguejo), 一只蟹 (um caranguejo). O padrão é: número + classificador + substantivo (数词 + 量词 + 名词).", 21.5)
a.glossline("O português conta as coisas de forma livre; o chinês escolhe um classificador para cada tipo de coisa — sem plural, sem -s.")
a.ex("A2", "Complete a frase", "件", "wàitào usa o classificador jiàn.",
     "我想买一___外套。", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Escolha múltipla", "B", "wéijīn usa tiáo: coisas longas e macias.",
     "「一条」可以说什么? A. 一条外套 · B. 一条围巾 · C. 一条大闸蟹", size=20.5, gap=10)
a.ex("A2", "Complete a frase", "斤", "jīn — meio quilo; os preços do mercado são por jīn.",
     "大闸蟹多少钱一___?", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Escolha múltipla", "A", "Roupas usam jiàn, não gè nem tiáo.",
     "哪个说法对? A. 一件衣服 · B. 一个衣服 · C. 一条衣服", size=20.5, gap=10)
a.para("Mais um para praticar: 「这件外套多少钱?」 (Quanto custa este casaco?) Quando fizer compras, pergunte o preço primeiro, depois pague.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Hora e datas", 24)
b.para("O chinês dá os horários do maior para o menor: ano, mês, dia, dia da semana, parte do dia, hora. Exemplo: 「10月20日晚上8点」 (20 de outubro, 20h) — a maior unidade primeiro, nada fora de ordem.", 21.5)
b.glossline("Assim, «sexta-feira à noite, 23 de outubro» vira 10月23日星期五晚上.")
b.ex("B1", "Escolha múltipla", "B", "língchén — as horas pequenas depois da meia-noite.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "Complete a frase", "上午", "A NBA abriu de manhã, hora de Pequim.",
     "NBA 在北京时间10月21日___开打。(不是晚上)", instr="Complete", size=20.5, gap=10)
b.ex("B1", "Escolha múltipla", "A", "Do maior para o menor: 20/out, noite, 8 horas.",
     "哪个顺序对? A. 10月20日晚上8点 · B. 8点晚上10月20日 · C. 晚上8点10月20日", size=20.5, gap=10)
b.ex("B1", "Complete a frase", "周五", "23 de outubro é sexta-feira — zhōuwǔ.",
     "10月23日是星期五,也可以说___。霜降在这天。", instr="Complete", size=20.5, gap=10)
b.para("Mais duas palavras: 凌晨 (língchén) são as horas pequenas depois da meia-noite, antes do amanhecer; 傍晚 (bàngwǎn) é o trechinho logo antes de escurecer.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Lendo as notícias", 24)
c.para("Quando uma notícia envolve uma disputa (争议), separe três tipos de frase: afirmações on-line (说法), declarações oficiais (声明) e dados de mercado (数据). As afirmações podem exagerar; os dados precisam manter a fonte e a data. A página 6 é o exemplo: 「暴跌40%」 é uma afirmação, 77,5 元 e 57,5 元 são dados, 「崩盘不实」 é uma declaração.", 21.5)
c.glossline("Pergunte de cada número: quem o mediu, e quando?") 
c.ex("B2", "Escolha múltipla", "C", "«bàodiē 40%» era uma afirmação on-line, não um dado medido.",
     "「暴跌超过40%」在第6版里是什么? A. 数据 · B. 声明 · C. 网上的说法", size=20.5, gap=10)
c.ex("B2", "Complete a frase", "声明", "shēngmíng — a declaração oficial da associação.",
     "协会10月19日发表___,说「崩盘」不是真的。", instr="Complete", size=20.5, gap=10)
c.ex("B2", "Escolha múltipla", "B", "Primeiro os dados e a fonte; a manchete por último.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和出处 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "Complete a frase", "25.8", "A queda real, calculada na página 6, é de 25,8%.",
     "第6版真正算出的数据降幅是___%。", instr="Complete", size=20.5, gap=10)
c.para("Tente você: na caixa de buscas em alta da página 1, 「第 8 位」 é uma posição — um dado. As palavras de uma manchete são afirmações. Você sabe distingui-las?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de) marca como uma ação é feita; vem antes do verbo."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de) liga um verbo a um complemento de grau: 跑得快."),
    ("「我买了三只大闸蟹个」", "→ 「我买了三只大闸蟹。」", "Ordem: número + classificador + substantivo. O 个 final é um a mais; caranguejos usam 只."),
    ("「霜降在星期五十月二十三日」", "→ 「霜降在10月23日,星期五。」", "Os horários vão do maior para o menor: mês e dia primeiro, o dia da semana por último."),
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
wt = "「先付定金,后付尾款。」(Primeiro o sinal, depois o saldo.) A estrutura 先…后/再… dá a ordem das ações. Mais: 「先看天气,再出门。」「先洗手,再吃饭。」"
wcn = "Estrutura: 先 … 后/再 … — primeiro X, depois Y. Crie a sua própria frase."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Estrutura da semana", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在多伦多。霜降那天,我吃了柿子,也给妈妈打了电话。我的购物车里有一件外套,还在等付尾款。」"
lcn = "Uma carta de exemplo da redação — não é uma carta de verdade. O VOL.2 publicará as cartas verdadeiras dos leitores e o melhor texto da página 8!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
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
    ("「今年的双11来得早」", "O 双11 deste ano chegou cedo.", "Página 1"),
    ("「付完尾款，快递就开始送货了」", "Pago o saldo, a entrega começa.", "Página 1"),
    ("「付完尾款，商家就发货」", "Assim que você paga o saldo, o vendedor despacha.", "Página 2"),
    ("「遥知兄弟登高处，遍插茱萸少一人」", "O verso famoso de Wang Wei sobre o Chóngyáng (poema).", "Página 3"),
    ("「两个分数只差2.735分」", "As duas pontuações diferem por apenas 2.735 pontos.", "Página 4"),
    ("「最大的看点是詹姆斯」", "A maior atração é LeBron.", "Página 4"),
    ("「看S16，要通宵了」", "Assistir ao S16 significa ficar acordado a noite toda.", "Página 5"),
    ("「先看数据，再看标题」", "Primeiro os dados, a manchete por último (a regra da página 6).", "Página 6"),
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
p.text(MX + 28, py + 44, "下期预告 · Na próxima semana (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16 瑞士轮打完了:LPL 的四支队打得怎么样?双11 的包裹都到了吗?我们追踪报道。11月7日是立冬,冬天要来了。还有你们的来信和第 8 版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
