# -*- coding: utf-8 -*-
# W47 zh-tw core, VOL.4: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言　Língua", "Lucerna", "語言聚焦　三個級別　三個主題　Três níveis, três temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　遊行的話　Palavras do desfile", 25)
a.para("Os desfiles lhe dão quatro palavras úteis: 遊行 (desfile), 封王 (conquistar o título), 夜間 (noturno) e 終點 (linha de chegada). Aprenda-as uma vez e todo desfile fará sentido.", 22)
a.expl("Quatro palavras de desfile: 遊行, 封王, 夜間, 終點.")
a.para("遊行 é uma marcha de celebração pelas ruas. 封王 significa ganhar o campeonato. 夜間 significa à noite — a parada noturna começa às 19:00. 終點 é onde o desfile termina: o Taipei Dome.", 22)
a.ex("A2", "完成句子", "遊行", "Uma marcha de celebração é 遊行.",
     "大家走上街頭慶祝，叫___。", instr="Completar", size=22, gap=10)
a.ex("A2", "單選", "A", "O desfile sai às 14:00 em 22 nov.",
     "封王遊行幾點出發？", opts=["A. 下午2點", "B. 上午2點", "C. 晚上7點"], size=22, gap=10)
a.ex("A2", "完成句子", "封王", "Conquistar o título é 封王.",
     "拿下總冠軍，叫___。", instr="Completar", size=22, gap=10)
a.ex("A2", "單選", "A", "A parada noturna começa às 19:00.",
     "夜間遊行晚上幾點開始？", opts=["A. 晚上7點", "B. 下午2點", "C. 上午10點"], size=22, gap=10)
a.end_report()
# ---- P7 image: below the A2 column (free space) ----
iy7 = a.y + 16
image(p, "books.jpg", COLX[0], iy7, CW, 140)
cy7 = caption(p, COLX[0], iy7 + 140, CW,
              "舊書，越讀越有味道（資料照片）。",
              "Foto: autor desconhecido — CC0 (Wikimedia Commons)")
print("P7 image ends", cy7, "(A2 flow ended", a.y, ")")

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　電影與鋼雕　Cinema e aço", 25)
b.para("O cinema e o aço dividem as manchetes desta semana. Agrupe as palavras e elas fixam: cinema （入圍、頒獎、星光大道） e aço （鋼雕、保險箱、勞動記憶）.", 22)
b.expl("Agrupe as palavras: cinema (入圍/頒獎), aço (鋼雕/保險箱).")
b.para("入圍 significa ser indicado; 頒獎 significa entregar os prêmios. 星光大道 é o tapete vermelho antes da cerimônia. 鋼雕 é uma escultura de aço; 保險箱 é o cofre que guarda as memórias do trabalho de Kaohsiung.", 22)
b.ex("B1", "完成句子", "入圍", "Ser indicado é 入圍.",
     "被選進最後的得獎名單，叫___。", instr="Completar", size=22, gap=10)
b.ex("B1", "單選", "A", "A cerimônia começa às 18:30 em 22 nov.",
     "金馬獎頒獎典禮幾點開始？", opts=["A. 晚上6點30分", "B. 下午2點", "C. 上午10點"], size=22, gap=10)
b.ex("B1", "完成句子", "鋼雕", "Uma escultura de aço é 鋼雕.",
     "用鋼鐵做的藝術，叫___。", instr="Completar", size=22, gap=10)
b.ex("B1", "單選", "A", "O festival do aço termina em 22 nov.",
     "鋼雕藝術節展到哪天？", opts=["A. 11月22日", "B. 11月15日", "C. 11月9日"], size=22, gap=10)
b.para("Truque de memória: aprenda primeiro 入圍, depois 星光大道 (o tapete vermelho às 17:00, antes da cerimônia), e depois a cerimônia （頒獎） às 18:30.", 22)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　節氣與耶誕　Estações", 25)
c.para("O inverno traz suas próprias palavras. Esta semana: 小雪 (Neve Menor), 節氣 (termo solar), 燈秀 (show de luzes) e 市集 (mercado).", 22)
c.expl("Quatro palavras de inverno desta edição: 小雪, 節氣, 燈秀, 市集.")
c.para("小雪 é o 20.º termo solar, depois de 立冬. 節氣 significa termo solar — 24 por ano. 燈秀 é um show de luzes: o principal acontece a cada meia hora. 市集 é um mercado — o mercado de inverno de World of Frozen.", 22)
c.ex("B2", "單選", "A", "Xiaoxue é o 20.º termo solar.",
     "「小雪」是二十四節氣的第幾個？", opts=["A. 第20個", "B. 第2個", "C. 第24個"], size=22, gap=10)
c.ex("B2", "完成句子", "主燈秀", "O show de luzes principal se repete a cada meia hora.",
     "耶誕城的___每半小時一次。", instr="Completar", size=22, gap=10)
c.ex("B2", "單選", "A", "O mercado de inverno fica em World of Frozen.",
     "想逛冬日市集、買聖誕禮物，要去哪裡？", opts=["A. 魔雪奇緣世界", "B. 維多利亞港", "C. 駁二"], size=22, gap=10)
c.ex("B2", "完成句子", "市集", "Um mercado é 市集.",
     "賣東西、逛街的地方，叫___。", instr="Completar", size=22, gap=10)
c.para("Não é preciso muitas palavras de estação — aprenda quatro e o inverno parecerá mais perto.", 22)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「金馬獎11月15日頒獎」", "→「金馬獎11月22日頒獎，11月15日是爵士之夜」", "A cerimônia é em 22 nov.; 15 nov. é uma noite de jazz."),
    ("「封王遊行上午2點出發」", "→「封王遊行下午2點出發，上午沒有遊行」", "O desfile sai às 14:00, não às 02:00."),
    ("「主燈秀每小時一次」", "→「主燈秀每半小時一次，17:30到23:00一共12場」", "O show principal acontece a cada meia hora: 12 vezes, das 17:30 às 23:00."),
]
eh = 74 + sum(72 + len(wrap("✗ " + r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所　Clínica de erros", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, "✗ " + wrong, 21.5, "serif", True, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「天氣越冷，越要保暖。」 — 越…越… significa: quanto mais X, mais Y. 夜越深，燈越亮 (quanto mais escura a noite, mais brilhantes as luzes)."
wcn = "Estrutura: 越…越… — quanto mais X, mais Y. Crie sua própria frase com ela."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式　Estrutura de frase", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好：本週日我要去看封王遊行，穿紅色衣服為龍隊喝采。晚上回家看金馬獎轉播，還想去高雄看鋼雕，最後一天不要錯過。——台北小讀者（編輯範例）」"
lcn = "Carta de exemplo da redação, não é uma carta real: VOL.3 prometeu cartas reais de leitores e os melhores textos da página 8 a partir desta edição; até o fechamento nenhuma publicável havia chegado. O exemplo fica e o convite continua aberto."
lt2 = "延期披露：VOL.3曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。"
lh = 164 + (len(wrap(lt, "serif", False, 21.5, CW - 44)) + len(wrap(lt2, "serif", False, 21.5, CW - 44))) * 30.53 + (len(wrap(lcn, "sans", False, 20, CW - 44)) - 1) * 28.4
# exact draw model: lead-in 89 + lt/lt2 block lines x30.53 + gaps 31/30 + lcn lines
# (last baseline + descent 6 + pad 8). The old 62/12/26 formula under-counted
# the lead-in and inter-para gaps by ~20px (caught by occlusion audit, build 10).
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地　Cantinho dos leitores", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 24)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "本週金句　Frases da semana — palavra por palavra dos artigos desta edição", 27, "sans", True, OLIVE)
quotes = [
    ("「封王遊行從天母棒球場出發」", "O desfile do título sai do Estádio de Beisebol de Tianmu.", "p. 1"),
    ("「夜間遊行晚上7點，最後一場不要錯過」", "A parada noturna às 19:00 — o último show, não perca.", "p. 1"),
    ("「小雪之後，天氣一天比一天冷」", "Depois de Xiaoxue, cada dia é mais frio que o anterior.", "p. 2"),
    ("「主燈秀每半小時一次，每次5分鐘」", "O show de luzes principal a cada meia hora, 5 minutos cada vez.", "p. 2"),
    ("「頒獎典禮晚上6點30分開始」", "A cerimônia de premiação começa às 18:30.", "p. 3"),
    ("「保險箱裡，裝的是高雄的勞動記憶」", "Dentro do cofre: as memórias do trabalho de Kaohsiung.", "p. 3"),
    ("「穿上紅色衣服，一起上街為龍隊喝采」", "Vista vermelho, vá para a rua, torça pelos Dragons.", "p. 4"),
    ("「香港迪士尼聖誕，從11月17日開始」", "O Natal na Disneyland começa em 17 nov.", "p. 5"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 132
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 132 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "下期預告　Na próxima semana (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "下週：金馬獎得獎名單、封王遊行直擊、鋼雕閉幕現場，還有你們的來信和第8版最佳作文。下週見！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
