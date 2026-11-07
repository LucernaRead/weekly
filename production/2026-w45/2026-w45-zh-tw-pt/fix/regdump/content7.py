# -*- coding: utf-8 -*-
# W45 zh-tw core, VOL.2: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45-zh-tw-pt-fix/regdump/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Foco linguístico", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Três níveis, três temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 展會的話 · Palavras da feira", 24)
a.para("As feiras desta semana trazem quatro palavras úteis: 旅展 (feira de viagens), 攤位 (estande), 集章 (colecionar carimbos) e 吉祥物大遊行 (desfile de mascotes). Aprenda-as uma vez e toda a feira de viagens fará sentido.", 21.5)
a.glossline("Quatro palavras da feira: 旅展, 攤位, 集章, 吉祥物大遊行.")
a.para("旅展 é a forma curta de 旅行展覽會 (exposição de viagens). Um 攤位 é um estande dentro da feira; a feira de Taipé tem 1.600 deles. 集章 significa colecionar carimbos em pontos determinados — colecione os seis carimbos das Trilhas Verdes e você ganhará um prêmio.", 21.5)
a.ex("A2", "完成句子", "攤位", "Um estande dentro da feira é um tānwèi.",
     "旅展裡的一個小展位,叫___。", instr="Complete", size=20.5, gap=10)
a.ex("A2", "單選", "A", "O desfile de mascotes acontece todos os dias às 14:00.",
     "吉祥物大遊行每天幾點?", opts=["A. 下午2點", "B. 中午12點", "C. 晚上7點"], size=20.5, gap=10)
a.ex("A2", "完成句子", "集章", "Colecionar carimbos em pontos determinados é jízhāng.",
     "在6大綠道蓋章收集,叫___。", instr="Complete", size=20.5, gap=10)
a.ex("A2", "單選", "A", "A feira de viagens é no Centro de Exposições de Nangang.",
     "台北旅展在哪裡?", opts=["A. 南港展覽館一館", "B. 台北大巨蛋", "C. 高雄駁二"], size=20.5, gap=10)
a.para("Pratique: 「旅展幾點開門？」 («A que horas a feira abre?») — sexta-feira abre ao meio-dia e nos outros dias às 10:00.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 球賽與節氣 · Jogos e estações", 24)
b.para("Esporte e estações dividem as manchetes desta semana. Agrupe as palavras e elas fixam: vencer （封王、完封） e inverno （立冬、進補）.", 21.5)
b.glossline("Agrupe as palavras: vencer (封王/完封), inverno (立冬/進補).")
b.para("封王 significa conquistar o campeonato; 完封 significa não deixar o adversário marcar, 0 pontos. 立冬 é o termo solar que inicia o inverno; 進補 é comer alimentos quentes e nutritivos antes dos meses frios.", 21.5)
b.ex("B1", "完成句子", "封王", "Conquistar o título é fēng wáng.",
     "拿下總冠軍,叫___。", instr="Complete", size=20.5, gap=10)
b.ex("B1", "單選", "A", "wánfēng significa que o adversário marca zero.",
     "「完封」是什麼意思?", opts=["A. 對手得0分", "B. 大勝10分", "C. 打滿9局"], size=20.5, gap=10)
b.ex("B1", "完成句子", "立冬", "Lidong inicia o inverno.",
     "冬天第一個節氣是___。", instr="Complete", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Pato com gengibre é um prato do Lidong.",
     "立冬常吃的鍋是哪一種?", opts=["A. 薑母鴨", "B. 冰品", "C. 生魚片"], size=20.5, gap=10)
b.para("Truque de memória: aprenda 封王 primeiro, depois o jeito como foi vencido （完封） e depois a estação em que aconteceu （立冬）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 港台說法 · Jeito local de falar", 24)
c.para("Taiwan e Hong Kong têm, cada um, seu jeito de dizer as coisas. Esta semana: 打卡 (registrar-se com uma foto), 討糖 (pedir doces no Halloween), 踩街 (desfile de rua fantasiado) e 泡湯 (banho em águas termais).", 21.5)
c.glossline("Quatro palavras locais desta edição: 打卡, 討糖, 踩街, 泡湯.")
c.para("打卡 começou como bater o ponto no trabalho, mas em uma feira ou festival significa postar uma foto para dizer 'estive aqui'. 討糖 é o que as crianças dizem nas lojas no Halloween; 踩街 é o próprio desfile fantasiado; 泡湯 é o prazer outonal de um banho em águas termais.", 21.5)
c.ex("B2", "單選", "A", "Em um festival, dǎkǎ significa postar uma foto para dizer que você esteve lá.",
     "在旅展、節慶場合,「打卡」是什麼意思?", opts=["A. 拍照分享,說自己來過", "B. 上班簽到", "C. 買門票"], size=20.5, gap=10)
c.ex("B2", "完成句子", "討糖", "Pedir doces no Halloween é tǎotáng.",
     "萬聖節小朋友去店家___。", instr="Complete", size=20.5, gap=10)
c.ex("B2", "單選", "A", "cǎijiē é um desfile de rua fantasiado.",
     "「踩街」是什麼?", opts=["A. 穿裝扮上街遊行", "B. 在街上跑步", "C. 逛夜市"], size=20.5, gap=10)
c.ex("B2", "完成句子", "泡湯", "Banho em águas termais é pàotāng.",
     "秋冬去溫泉洗澡、放鬆,叫___。", instr="Complete", size=20.5, gap=10)
c.para("Você não precisa de muitas expressões locais — aprenda quatro e cada passeio parecerá mais próximo.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「龍隊完勝兄弟6比0」", "→「龍隊完封兄弟6比0」", "完勝 significa vencer com folga; 完封 significa que o adversário marcou zero."),
    ("「立冬就是冬至」", "→「立冬是冬天開始,冬至是白天最短的一天」", "Lidong inicia o inverno; o Solstício é o dia mais curto. Termos diferentes."),
    ("「金融科技週在台北開幕」", "→「金融科技週在香港開幕」", "Confira a cidade: a Semana FinTech abre em Hong Kong, não em Taipé."),
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
wt = "「先去集章，再去看表演。」 — a estrutura 先…再… indica a ordem de duas ações: primeiro X, depois Y. Crie a sua: 先比價，再結帳 (compare os preços primeiro e pague depois)."
wcn = "Estrutura: 先…再… — primeiro X, depois Y. Crie sua própria frase com ela."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Estrutura da semana", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:上週我去天母討糖,拿到一顆很大的糖果!這週我想去旅展看吉祥物大遊行,還想集滿6大綠道的章。——台北小讀者(編輯範例)」"
lcn = "Carta de exemplo da redação, não uma carta real. Aviso: o VOL.1 prometeu cartas reais e a melhor redação da página 8 desde esta edição; até o fechamento nenhuma publicável chegou, por isso o exemplo fica e o convite continua aberto."
lt2 = "延期披露:VOL.1曾預告本期起刊登真實讀者來信和第8版最佳作文;截至截稿,本報未收到可刊登的真實來信與投稿,因此本期仍刊登編輯範例,並繼續公開徵集。你的來信,下一期見。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Cantinho do leitor", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42)
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Frases da semana — palavra por palavra dos artigos desta edição", 27, "sans", True, OLIVE)
quotes = [
    ("「用手機轉帳、掃碼付款、網上買保險，都是金融科技」", "Pagar pelo celular, escanear para pagar, comprar seguro on-line — isso é fintech.", "p. 1"),
    ("「123個國家及城市、1,600個攤位」", "123 países e cidades, 1.600 estandes.", "p. 1"),
    ("「需要才買，不要為了折扣買一堆用不到的東西」", "Compre o que você precisa; não compre um monte de coisas que não vai usar só por causa de um desconto.", "p. 2"),
    ("「在高雄，鋼鐵也能變成舞台」", "Em Kaohsiung, até o aço pode virar palco.", "p. 3"),
    ("「福隆的夏天，在10月26日畫下句點」", "O verão de Fulong chegou ao fim em 26 de outubro.", "p. 3"),
    ("「6比0完封兄弟，龍隊拋下紅色彩帶」", "Um 6 a 0 sem sofrer pontos contra os Brothers, e os Dragons jogaram as fitas vermelhas.", "p. 4"),
    ("「250家店家一起討糖」", "250 lojas distribuindo doces juntas.", "p. 5"),
    ("「旅展首日中午12點才開門」", "No primeiro dia da feira, as portas abrem só ao meio-dia.", "p. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 138
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 138 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期預告 · Na próxima semana (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "下週三雙11,你買了什麼?下週一旅展最後一天直擊,高雄鋼雕藝術節展到11月22日,還有你們的來信和第8版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
