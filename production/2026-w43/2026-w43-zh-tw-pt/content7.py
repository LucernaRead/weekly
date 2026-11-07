# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Foco na língua", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Três níveis, três temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 天氣的話 · Palavras do tempo", 24)
a.para("A semana do tufão enche as notícias de palavras do tempo — aprenda as seis que você mais vai ver: 海上颱風警報 (alerta marítimo), 陸上颱風警報 (alerta terrestre), 共伴效應 (efeito conjunto), 外圍環流 (circulação externa), 豪雨 (chuva torrencial), 停班停課 (trabalho e aula suspensos).", 21.5)
a.glossline("Seis palavras do tempo percorrem as notícias da semana — aprenda uma vez e leia a semana toda.")
a.para("Os alertas são de dois tipos: primeiro o 海上警報 (alerta marítimo), enquanto o tufão ainda está no mar; depois o 陸上警報 (alerta terrestre), quando ele se aproxima da terra. Chuva mais forte que 大雨 é 豪雨 (chuva torrencial).", 21.5)
a.ex("A2", "完成句子", "海上", "Primeiro vem o alerta marítimo, enquanto o tufão ainda está no mar.",
     "颱風還在海上,先發佈___颱風警報。", instr="Complete", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Tíng bān tíng kè significa trabalho e aula suspensos.",
     "「停班停課」是什麼意思?", opts=["A. 不上班、不上課", "B. 提早一小時下班", "C. 換到別天上班"], size=20.5, gap=10)
a.ex("A2", "完成句子", "豪", "Háo yǔ é mais forte que dà yǔ.",
     "比大雨還大的雨,叫___雨。", instr="Complete", size=20.5, gap=10)
a.ex("A2", "單選", "A", "A circulação externa do tufão (wàiwéi huánliú) traz a chuva.",
     "颱風的外圍___會帶來雨。", opts=["A. 環流", "B. 警報", "C. 假期"], size=20.5, gap=10)
a.para("Pratique: «明天會停班停課嗎？» («Amanhã vai ter trabalho e aula?») — veja o anúncio da sua cidade.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 日子與節日 · Dias e festas", 24)
b.para("Os dias desta semana são especiais. Agrupe as palavras e elas ficam: folgas （連假、補假）, viagens （疏運） e diversão de festa （登高、討糖、星光大道）.", 21.5)
b.glossline("Agrupe as palavras: folgas (連假/補假), viagens (疏運), diversão de festa (登高/討糖/星光大道).")
b.para("連假 é uma sequência de dias livres seguidos; quando um feriado cai no fim de semana e um dia útil é liberado em troca, esse dia extra é um 補假； e os trens e ônibus extras que levam todo mundo para fora e de volta para casa são o 疏運.", 21.5)
b.ex("B1", "完成句子", "補假", "Um dia de compensação: bǔjià.",
     "假日逢週日,週一多放一天,叫___。", instr="Complete", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Shūyùn = transporte extra para o movimento do feriado.",
     "「疏運」是連假時做什麼?", opts=["A. 加開班次載客", "B. 賣紀念票", "C. 修馬路"], size=20.5, gap=10)
b.ex("B1", "完成句子", "討糖", "Tǎotáng é o jeito taiwanês de dizer «doces ou travessuras».",
     "萬聖節,小朋友去店家___(要糖果)。", instr="Complete", size=20.5, gap=10)
b.ex("B1", "單選", "A", "A parte do tapete vermelho de uma noite de prêmios é a xīngguāng dàdào.",
     "頒獎典禮走紅毯的部分叫?", opts=["A. 星光大道", "B. 人氣獎", "C. 疏運大道"], size=20.5, gap=10)
b.para("Truque de memória: aprenda primeiro 連假， depois a multidão que ele move （疏運） e o dia extra que ele acrescenta （補假）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 在地說法 · Jeito local de falar", 24)
c.para("Taiwan e Hong Kong têm cada um seu jeito de dizer as coisas. Em Taiwan, o Threads é apelidado de «脆»; um bom post se salva com «留友看» — «guardar para os amigos verem»; e um elogio avaliado com símbolos zhuyin é um «ㄅ級分».", 21.5)
c.glossline("Três expressões da internet taiwanesa — todas de uma seleção da PopDaily de maio de 2026 com os memes do ano, não das notícias desta semana.")
c.para("Em Hong Kong, o Halloween é «哈囉喂»; o hot pot é «打邊爐»; barato e gostoso é «抵食»; os caranguejos se pesam em «両», e as fichas do festival gastronômico são as «品味券».", 21.5)
c.ex("B2", "單選", "A", "Em Taiwan, o Threads é apelidado de cuì (crocante).",
     "台灣人把 Threads 暱稱作什麼?", opts=["A. 脆", "B. 脆餅", "C. 推特兒"], size=20.5, gap=10)
c.ex("B2", "完成句子", "留友", "Liú yǒu kàn — salve para os amigos lerem também.",
     "看到好文,先存起來「___看」。", instr="Complete", size=20.5, gap=10)
c.ex("B2", "單選", "A", "Hāluō wèi é o Halloween de Hong Kong.",
     "「哈囉喂」是香港人怎麼說哪個節日?", opts=["A. 萬聖節", "B. 聖誕節", "C. 重陽節"], size=20.5, gap=10)
c.ex("B2", "完成句子", "品味", "Os cupons do festival são as pǐnwèi quàn (fichas de degustação).",
     "美酒佳餚巡禮換飲品小食的券,叫___券。", instr="Complete", size=20.5, gap=10)
c.para("Você não precisa de muitos jeitos locais — aprenda cinco e toda conversa fica mais próxima.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「台風來了」", "→「颱風來了」", "Taiwan escreve 颱風; 台風 é a grafia em kanji japonês."),
    ("「我買了四兩的蟹」", "→「我買了四両的蟹」", "Os caranguejos se pesam em 両 (taéis); 兩 é o «dois» do dia a dia, como em 兩隻蟹 (dois caranguejos)."),
    ("「天氣慢慢的變涼」", "→「天氣慢慢地變涼」", "地 (de) indica como uma ação acontece, antes do verbo."),
    ("「我明天放四天假去玩」", "→「我請了四天假去玩」", "請假 = pedir a folga você mesmo; 放假 = a folga é dada a todos."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所 · Clínica de erros", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "«先看警報，再決定出不出門。» — a estrutura 先…再… dá a ordem de duas ações: primeiro X, depois Y. É feita para a semana do tufão: 先查公告，再改行程 (veja os avisos primeiro, depois mude os planos)."
wcn = "Estrutura: 先…再… — primeiro X, depois Y. Crie a sua própria frase com ela."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Estrutura da semana", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:重陽節我跟阿公去登高,他走得比我還快!晚上我們吃大閘蟹,蟹黃真的好多。下週我想去看台灣大賽。——台北小讀者(編輯範例)」"
lcn = "Uma carta de exemplo da redação — não é uma de verdade. O VOL.2 vai publicar cartas reais dos leitores e a melhor redação da página 8!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Cantinho dos leitores", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Frases da semana — palavra por palavra dos artigos desta edição", 27, "sans", True, OLIVE)
quotes = [
    ("「路徑還有變數,會不會登陸,還沒有人知道」", "A trajetória ainda pode mudar; ninguém sabe ainda se ele vai tocar a terra.", "p. 1"),
    ("「請四天假,換九天連假」", "Quatro dias de folga, nove dias livres.", "p. 2"),
    ("「登高望遠,人也精神了」", "Suba alto, olhe longe — e se sinta renovado.", "p. 3"),
    ("「農曆九月吃蟹乸,農曆十月吃蟹公」", "Fêmeas no 9.º mês lunar, machos no 10.º.", "p. 3"),
    ("「先贏四場的隊伍,就是今年的總冠軍」", "O primeiro time a chegar a quatro vitórias é o campeão deste ano.", "p. 4"),
    ("「颱風改了日期,卻改不了大家過節的心情」", "O tufão mudou a data, não o clima de festa.", "p. 5"),
    ("「三百四十多個攤位,把世界搬到海邊」", "Mais de 340 barracas trazem o mundo para o porto.", "p. 6"),
    ("「星期五、六的晚上,今年第一次開到凌晨一時」", "As noites de sexta e sábado vão até a 1h pela primeira vez.", "p. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 146
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 146 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期預告 · Na próxima semana (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "台灣大賽冠軍出爐!美酒佳餚巡禮開幕直擊,天母搞什麼鬼主活動、福隆沙雕最後一天,還有你們的來信和第 8 版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
