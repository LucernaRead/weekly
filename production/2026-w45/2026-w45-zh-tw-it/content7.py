# -*- coding: utf-8 -*-
# W45 zh-tw core, VOL.2: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-it/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Focus sulla lingua", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Tre livelli, tre temi")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 展會的話 · Parole della fiera", 24)
a.para("Le fiere di questa settimana ti danno quattro parole utili: 旅展 (fiera dei viaggi), 攤位 (stand), 集章 (raccolta di timbri) e 吉祥物大遊行 (sfilata delle mascotte). Imparale una volta, e tutta la fiera avrà senso.", 21.5)
a.glossline("Quattro parole della fiera: 旅展, 攤位, 集章, 吉祥物大遊行.")
a.para("旅展 è l'abbreviazione di 旅行展覽會 (mostra di viaggi). Un 攤位 è un singolo stand dentro la fiera; la fiera di Taipei ne ha 1.600. 集章 significa raccogliere timbri in punti stabiliti — raccogli tutti e sei i timbri Greenway e vinci un premio.", 21.5)
a.ex("A2", "完成句子", "攤位", "Uno stand dentro la fiera è un tānwèi.",
     "旅展裡的一個小展位,叫___。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "單選", "A", "La sfilata delle mascotte si svolge ogni giorno alle 14:00.",
     "吉祥物大遊行每天幾點?", opts=["A. 下午2點", "B. 中午12點", "C. 晚上7點"], size=20.5, gap=10)
a.ex("A2", "完成句子", "集章", "Raccogliere timbri in punti stabiliti è jí zhāng.",
     "在6大綠道蓋章收集,叫___。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "單選", "A", "La fiera dei viaggi è al Nangang Exhibition Center.",
     "台北旅展在哪裡?", opts=["A. 南港展覽館一館", "B. 台北大巨蛋", "C. 高雄駁二"], size=20.5, gap=10)
a.para("Esercitati: «旅展幾點開門?» («A che ora apre la fiera?») — il venerdì apre a mezzogiorno, gli altri giorni alle 10:00.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 球賽與節氣 · Partite e stagioni", 24)
b.para("Sport e stagioni condividono i titoli di questa settimana. Raggruppa le parole e restano in mente: vincere （封王、完封） e inverno （立冬、進補）.", 21.5)
b.glossline("Raggruppa le parole: vincere (封王/完封), inverno (立冬/進補).")
b.para("封王 significa vincere il campionato; 完封 significa non far segnare l'altra squadra, 0 punti. 立冬 è il termine solare che dà inizio all'inverno; 進補 è mangiare cibi caldi e nutrienti prima dei mesi freddi.", 21.5)
b.ex("B1", "完成句子", "封王", "Vincere il titolo è fēng wáng.",
     "拿下總冠軍,叫___。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Wánfēng significa che l'altra squadra segna zero.",
     "「完封」是什麼意思?", opts=["A. 對手得0分", "B. 大勝10分", "C. 打滿9局"], size=20.5, gap=10)
b.ex("B1", "完成句子", "立冬", "Lìdōng dà inizio all'inverno.",
     "冬天第一個節氣是___。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "單選", "A", "L'anatra allo zenzero è un piatto di Lìdōng.",
     "立冬常吃的鍋是哪一種?", opts=["A. 薑母鴨", "B. 冰品", "C. 生魚片"], size=20.5, gap=10)
b.para("Trucco di memoria: impara prima 封王 e poi il modo in cui è stato vinto （完封）, poi la stagione in cui è successo （立冬）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 港台說法 · Modi di dire locali", 24)
c.para("Taiwan e Hong Kong hanno ciascuno il proprio modo di dire le cose. Questa settimana: 打卡 (fare check-in con una foto), 討糖 (dolcetto o scherzetto), 踩街 (sfilata in costume) e 泡湯 (immergersi in una sorgente termale).", 21.5)
c.glossline("Quattro parole locali da questo numero: 打卡, 討糖, 踩街, 泡湯.")
c.para("打卡 nasceva come timbratura del cartellino al lavoro, ma in una fiera o a un festival significa pubblicare una foto per dire «ero qui». 討糖 è ciò che i bambini dicono nei negozi a Halloween; 踩街 è la sfilata in costume stessa; 泡湯 è il piacere autunnale di un bagno termale.", 21.5)
c.ex("B2", "單選", "A", "A un festival, dǎkǎ significa pubblicare una foto per dire che eri lì.",
     "在旅展、節慶場合,「打卡」是什麼意思?", opts=["A. 拍照分享,說自己來過", "B. 上班簽到", "C. 買門票"], size=20.5, gap=10)
c.ex("B2", "完成句子", "討糖", "Il dolcetto o scherzetto è tǎotáng.",
     "萬聖節小朋友去店家___。", instr="Completa", size=20.5, gap=10)
c.ex("B2", "單選", "A", "Cǎijiē è una sfilata in costume.",
     "「踩街」是什麼?", opts=["A. 穿裝扮上街遊行", "B. 在街上跑步", "C. 逛夜市"], size=20.5, gap=10)
c.ex("B2", "完成句子", "泡湯", "Immergersi in una sorgente termale è pàotāng.",
     "秋冬去溫泉洗澡、放鬆,叫___。", instr="Completa", size=20.5, gap=10)
c.para("Non ti servono molti modi di dire locali — imparane quattro e ogni uscita sembrerà più vicina.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「龍隊完勝兄弟6比0」", "→「龍隊完封兄弟6比0」", "完勝 = vincere alla grande; 完封 = l'altra squadra segna zero."),
    ("「立冬就是冬至」", "→「立冬是冬天開始,冬至是白天最短的一天」", "Lìdōng dà inizio all'inverno; il solstizio è il giorno più corto. Termini diversi."),
    ("「金融科技週在台北開幕」", "→「金融科技週在香港開幕」", "Controlla la città: la FinTech Week apre a Hong Kong, non a Taipei."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所 · Clinica degli errori", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先去集章，再去看表演。」 — lo schema 先…再… dà l'ordine di due azioni: prima X, poi Y. Costruisci la tua: 先比價，再結帳 (prima confronta i prezzi, poi paga)."
wcn = "Schema: 先…再… — prima X, poi Y. Costruisci una frase tua."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Struttura settimanale", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:上週我去天母討糖,拿到一顆很大的糖果!這週我想去旅展看吉祥物大遊行,還想集滿6大綠道的章。——台北小讀者(編輯範例)」"
lcn = "Lettera di esempio della redazione, non vera. Avviso di rinvio: il VOL.1 aveva promesso lettere vere e i migliori testi di pagina 8 da questo numero; alla chiusura non ne era arrivato nessuno pubblicabile, quindi resta l'esempio. Scrivici!"
lt2 = "延期披露:VOL.1曾預告本期起刊登真實讀者來信和第8版最佳作文;截至截稿,本報未收到可刊登的真實來信與投稿,因此本期仍刊登編輯範例,並繼續公開徵集。你的來信,下一期見。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 40
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · L'angolo dei lettori", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Frasi della settimana — parola per parola dagli articoli di questo numero", 27, "sans", True, OLIVE)
quotes = [
    ("「用手機轉帳、掃碼付款、網上買保險，都是金融科技」", "Paga con il telefono, scansiona per pagare, compra assicurazioni online: questo è il fintech.", "p. 1"),
    ("「123個國家及城市、1,600個攤位」", "123 paesi e città, 1.600 stand.", "p. 1"),
    ("「需要才買，不要為了折扣買一堆用不到的東西」", "Compra ciò che ti serve; non comprare un mucchio di cose che non userai solo per uno sconto.", "p. 2"),
    ("「在高雄，鋼鐵也能變成舞台」", "A Kaohsiung, anche l'acciaio può diventare un palcoscenico.", "p. 3"),
    ("「福隆的夏天，在10月26日畫下句點」", "L'estate di Fulong è finita il 26 ottobre.", "p. 3"),
    ("「6比0完封兄弟，龍隊拋下紅色彩帶」", "Uno shutout per 6-0 contro i Brothers, e i Dragons hanno lanciato i nastri rossi.", "p. 4"),
    ("「250家店家一起討糖」", "250 negozi che offrono dolcetti insieme.", "p. 5"),
    ("「旅展首日中午12點才開門」", "Il primo giorno della fiera le porte aprono solo a mezzogiorno.", "p. 6"),
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
p.text(MX + 28, py + 44, "下期預告 · La prossima settimana (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "下週三雙11,你買了什麼?下週一旅展最後一天直擊,高雄鋼雕藝術節展到11月22日,還有你們的來信和第8版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
