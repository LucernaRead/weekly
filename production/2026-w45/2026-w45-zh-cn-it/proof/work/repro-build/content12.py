# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-it-proof/work/repro-out/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 头版 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2 · 第 2 号", 23, "sans", True, OLIVE)
p.text(975, 92, "每周读中文 · Leggi il cinese vero, ogni settimana", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "2026年11月2日（周一）— 8日（周日）", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SETTIMANALE CINESE SEMPLIFICATO · VOL.2 · 双11 · 立冬 · S16", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "给学中文的人的周报 — Leggi la Cina vera, in cinese", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)
# pairing badge: which text, which explanation language, which reader
p.text(975, 434, "TESTI IN CINESE SEMPLIFICATO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI", 19.5, "sans", True, OLIVE, anchor="middle")

# band
p.rect(MX, 458, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 512, "双11还在进行,周六就立冬了", 36, "sans", True, "#f3edda")
p.text(MX + 30, 556, "现货一直卖到 11 月 13 日,11 月 7 日星期六立冬,冬天要来了。", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 512, "双11×立冬", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 556, "Settimana di shopping e inverno · vedi le pagine 2–3", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "头条 · Titolo principale", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "双11还在进行,冬天也要来了", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "11月7日星期六立冬,现货一直卖到11月13日——这一周,先买东西,再迎冬天", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "Redazione Lucerna · Livello di lettura A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("今年的双11已经开始了。京东10月12日晚上8点开始卖现货,淘宝和天猫10月15日晚上8点开始预售,10月20日晚上8点付尾款、现货开售。", size=24)
f.para("现货会一直卖到11月13日。所以这一周,不用等11月11日,双11已经在进行了。", size=24)
f.para("这一周还有一件大事:11月7日星期六是立冬。立冬是冬天的第一个节气,冬天要来了。", size=24)
f.para("买东西的时候,今年的规则更简单了:很多商品直接降价,不用再算复杂的满减。买之前,还可以问一问AI助手,比一比价格。", size=24)
f.para("11月7日星期六,还有一部新电影上映:《我们仅有一次的人生》。第5版有介绍。", size=24)
f.para("这是《Lucerna》简体中文版第2号。每周,我们用简单的中文,带你读真正的中国新闻。欢迎你!", size=24)
f.gloss("xiànhuò 现货 — merce in stock, pronta per la spedizione · lìjiǎn 立减 — uno sconto immediato alla cassa · zhíjiàng 直降 — un taglio diretto del prezzo · jiéqì 节气 — i 24 termini solari che dividono l'anno.")
f.box("数字看本周 · I numeri di questa settimana", [
    ("13 novembre — l'ultimo giorno delle vendite in stock", "serif", False, INK, 20, 1.35),
    ("7 novembre, sabato — 立冬 (Inizio dell'inverno)", "serif", False, INK, 20, 1.35),
    ("12 ottobre, ore 20:00 — JD.com: inizio delle vendite in stock", "serif", False, INK, 20, 1.35),
    ("10 novembre, ore 20:00 — il picco delle vendite (高潮场) inizia la prossima settimana", "serif", False, INK, 20, 1.35),
])
f.head("即学即练 · Prova subito", 25)
f.ex("A2", "完成句子", "10", "Le vendite in stock di JD.com sono iniziate il 12 ottobre.",
     "京东___月12日开始卖现货。", instr="Completa", size=19.5, gap=6)
f.ex("A2", "完成句子", "预售", "Le prevendite di Taobao e Tmall sono iniziate il 15 ottobre.",
     "淘宝和天猫10月15日开始___。", instr="Completa", size=19.5, gap=6)
f.ex("A2", "完成句子", "13", "Le vendite in stock durano fino al 13 novembre.",
     "现货一直卖到11月___日。", instr="Completa", size=19.5, gap=6)
f.ex("A2", "完成句子", "立冬", "L'Inizio dell'inverno cade sabato 7 novembre.",
     "11月7日星期六是___。", instr="Completa", size=19.5, gap=6)
f.ex("A2", "完成句子", "一", "L'Inizio dell'inverno è il primo termine solare dell'inverno.",
     "立冬是冬天的第___个节气。", instr="Completa", size=19.5, gap=6)
f.ex("A2", "完成句子", "降价", "Quest'anno molte merci sono scontate direttamente.",
     "今年的规则更简单了:很多商品直接___。", instr="Completa", size=19.5, gap=6)
f.end_report()

# ---- this-week calendar box (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "本周日历 · Questa settimana", 25, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "11月2日—8日 · 2–8 novembre", 22, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Che cosa succede questa settimana", 19, "sans", False, GREY)
topics = [
    "周一 11月2日 — 双11现货进行时",
    "周三—周六早上6点 — S16四分之一决赛",
    "周六 11月7日 — 立冬,新片上映",
    "周日 11月8日 — 中国记者节,S16半决赛",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 10
p.para(gx + 22, byy + 12, "La fase svizzera finisce il 1º novembre, quindi al momento di andare in stampa non si conoscono ancora le squadre dei quarti. I quarti si giocano dal 4 al 7 novembre, la prima semifinale l'8 novembre, sempre alle 06:00, ora di Pechino.", 18.5, "sans", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 636, "Tutti gli orari sono di Pechino", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "Le squadre S16 dipendono dalla fase svizzera", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "本期目录 · Sommario", 24, "sans", True, OLIVE)
som = [
    ("2版", "双11与立冬生活", "A2"),
    ("3版", "立冬:冬天的第一个节气", "A2→B1"),
    ("4版", "S16:出局与冲八强", "B1"),
    ("5版", "AI电影与立冬新片", "B1"),
    ("6版", "双11深读:规则变简单了", "B2"),
    ("7版", "词语精讲", "A2→B2"),
    ("8版", "测验与答案", "全部"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

# ---- word of the week (col 3) ----
my = 1636
p.text(gx, my + 24, "本周词 · Parola della settimana", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
p.para(gx, my + 76, "「立冬」 lìdōng — Inizio dell'inverno: il primo termine solare dell'inverno. 立冬到了,冬天要来了。Esempio: 「立冬那天,我们吃饺子。」", 21.5, "serif", False, INK, gw, 1.4)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "locker.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "快递柜(资料图)。现货期里,包裹会陆续送到你手里。",
        "Foto: Map hobby — CC0 (Wikimedia Commons)")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-week")
f2.head("忙碌的一周", 25)
f2.para("这一周又买东西,又迎冬天:周六立冬,周日还有半决赛。先看好日历,再安排周末吧。", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "快讯 · Notizie flash", 24, "sans", True, OLIVE)
brefs = [
    ("立冬", "周六立冬:北方吃饺子,南方吃法各不同。(第 3 版)"),
    ("S16", "一号种子AL出局,IG、TES、BLG冲八强。(第 4 版)"),
    ("电影", "AI电影票房遇冷,大家在争AI能不能拍电影。(第 5 版)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "闪电问答 · Quiz lampo", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Leggi la pagina 1 e scegli · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "单选", "A", "Le vendite in stock durano fino al 13 novembre.",
      "现货一直卖到哪一天? A. 11月13日 · B. 11月11日 · C. 10月20日", size=21)
qf.ex("A2", "单选", "B", "L'Inizio dell'inverno è sabato 7 novembre.",
      "立冬在11月几日? A. 11月1日 · B. 11月7日 · C. 11月11日", size=21)
qf.ex("A2", "单选", "C", "Le vendite in stock di JD.com sono iniziate il 12 ottobre.",
      "京东现货从哪天开始? A. 10月15日 · B. 10月20日 · C. 10月12日", size=21)
qf.ex("A2", "单选", "A", "Quest'anno molte merci sono scontate direttamente.",
      "今年双11,很多商品怎么便宜? A. 直接降价 · B. 必须先付定金 · C. 只有11月11日便宜", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-touiban.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 生活 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("生活 · Life", "Lucerna", "Livello A2 · 双11购物生活 · 立冬生活 · Shopping e primi giorni d'inverno")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("双11购物生活:现货、直降,还有AI帮忙", 37)
f.byline("Redazione Lucerna · Livello di lettura A2")
f.para("双11不是一天,是一段时间。京东从10月12日开始卖现货,淘宝和天猫从10月20日开始卖现货,现货一直卖到11月13日。")
f.para("今年和以前不一样:以前要先付定金、等付尾款,现在很多商品直接就是现货。现货就是已经在仓库里的货,下单就能发货。")
f.para("规则也更简单了。以前常见的跨店满减少了,更多是官方立减和商品直降:价格直接变低,不用再算来算去。买之前,还可以问一问AI助手,比如豆包的「买前问豆包」,比一比价格、看一看评价。")
f.para("微信小店今年第一次参加双11,活动从10月12日到11月15日,一共35天。第18个双11,有了新平台,也有了新玩法。")
f.para("这一周,冬天也要来了。11月7日星期六立冬,天气会一天比一天冷。厚外套、围巾、帽子,是很多人购物车里的东西。买之前,先看好尺码,再看退换货的规则。")
f.gloss("cāngkù 仓库 — un magazzino · píngjià 评价 — una recensione, quello che dicono i compratori · chǐmǎ 尺码 — una taglia · tuìhuànhuò 退换货 — resi e cambi.")
f.head("满减与直降 · Vecchio e nuovo", 25)
f.para("La vecchia regola che molti compratori conoscevano era 「满300减50」 (spendi 300 yuan, risparmi 50). Quest'anno lo schema più comune è 直降 (zhíjiàng): il prezzo stesso scende, e il prezzo alla cassa è quello che paghi. L'esempio qui sotto usa numeri di esercizio, non prezzi reali.")
f.box("Esempio pratico · 练习例子", [
    ("一件毛衣 240 元,一条围巾 80 元,一起 320 元。", "serif", False, INK, 20, 1.35),
    ("直降 50 元,实付 270 元。先看结算页,再决定买不买。", "serif", False, INK, 20, 1.35),
])
f.head("立冬生活:加衣服,吃点热的", 25)
f.para("立冬是冬天的开始,但不是每个地方同时变冷。中国南北很大,有的地方立冬还很暖和,有的地方已经要穿棉衣了。")
f.para("北方很多地方立冬吃饺子,因为「饺子」和「交子」声音很像,是秋冬交替的意思。南方有的地方吃鸡鸭鱼肉,有的地方吃汤圆、糍粑,都是补冬:冬天以前,吃点好的,身体暖和。")
f.para("11月上旬,有的学校要期中考试,日子各不相同,不是全国统一的日子。考试周里,早点睡觉,比熬夜更重要。")
f.gloss("bǔdōng 补冬 — mangiare bene prima dell'inverno · jiāozǐ 饺子 — ravioli · cíbā 糍粑 — dolci di riso glutinoso · qīzhōng 期中 — esami di metà periodo.")
f.box("本周生活小日历 · Le date di questa settimana", [
    ("周六 11月7日 — 立冬:吃饺子,加衣服", "serif", False, INK, 20, 1.35),
    ("周日 11月8日 — 中国记者节", "serif", False, INK, 20, 1.35),
    ("下周二 11月10日 20:00 — 双11高潮场开始", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: valley image + facts + 你呢 (sequential, measured)
ix = COLX[3]
image(p, "valley.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "秋天的山谷,红叶正当时。立冬以后,秋天就真的要过去了。",
              "Foto: Paul Gilmore — CC0 (Wikimedia Commons)")
facts = ["现货期到 11 月 13 日。",
         "立冬在 11 月 7 日星期六。",
         "微信小店活动到 11 月 15 日。"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "你知道吗 · Lo sapevi?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "你呢?这个双11,你想买什么?立冬那天,你想吃什么?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("E tu? Che cosa vuoi comprare in questo 双11? Che cosa mangeresti a 立冬? Scrivi due frasi in cinese.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · E tu?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "E tu? Che cosa vuoi comprare in questo 双11? Che cosa mangeresti a 立冬? Scrivi due frasi in cinese.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- word strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "购物词语卡 · Parole per lo shopping", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Quattro parole che vedrai in ogni app di shopping", 20, "sans", False, GREY, anchor="end")
words = [
    ("现货", "xiànhuò · merce in stock", "disponibile ora, pronta per la spedizione"),
    ("直降", "zhíjiàng · un taglio diretto del prezzo", "il prezzo scende direttamente, senza calcoli"),
    ("立减", "lìjiǎn · uno sconto immediato", "scontato alla cassa"),
    ("补冬", "bǔdōng · nutrirsi per l'inverno", "mangiare bene prima dell'inverno"),
]
for i, (t, lab, en) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, en, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 222, "Ricorda la frase: 「买现货不用等,先看结算页,再付款。」", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Esercizi", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · 读一读选一选 · Leggi e scegli", 25)
e.glossline("Leggi la pagina 2 e scegli la risposta migliore.")
e.ex("A2", "单选", "A", "Le vendite in stock di JD.com sono iniziate il 12 ottobre.",
     "京东现货从哪天开始? A. 10月12日 · B. 10月15日 · C. 10月20日", size=19, gap=6)
e.ex("A2", "单选", "B", "Le vendite in stock di Taobao e Tmall sono iniziate il 20 ottobre.",
     "淘宝和天猫现货从哪天开始? A. 10月12日 · B. 10月20日 · C. 11月11日", size=19, gap=6)
e.ex("A2", "单选", "A", "直降 significa che il prezzo stesso scende.",
     "直降是什么意思? A. 价格直接变低 · B. 必须先付定金 · C. 只有11月11日便宜", size=19, gap=6)
e.ex("A2", "单选", "A", "Dopo 立冬 il tempo diventa più freddo giorno dopo giorno.",
     "立冬以后天气怎么样? A. 一天比一天冷 · B. 一天比一天热 · C. 完全不变", size=19, gap=6)
e.ex("A2", "单选", "B", "L'evento del negozio WeChat dura fino al 15 novembre.",
     "微信小店活动到哪天? A. 11月13日 · B. 11月15日 · C. 11月11日", size=19, gap=6)
e.head("B · 词语填空 · Completa gli spazi", 25)
e.glossline("Completa ogni spazio con la parola giusta.")
e.ex("A2", "完成句子", "现货", "xiànhuò — merce in stock, pronta per la spedizione.",
     "已经在仓库里的货,叫___。", instr="Completa", size=19, gap=6)
e.ex("A2", "完成句子", "直降", "zhíjiàng — il prezzo stesso scende.",
     "价格直接变低,这叫___。", instr="Completa", size=19, gap=6)
e.ex("A2", "完成句子", "补冬", "bǔdōng — mangiare bene prima dell'inverno.",
     "冬天以前吃点好的,这叫___。", instr="Completa", size=19, gap=6)
e.ex("A2", "完成句子", "饺子", "jiǎozǐ — le famiglie del nord li mangiano a 立冬.",
     "北方很多地方立冬吃___。", instr="Completa", size=19, gap=6)
e.ex("B1", "完成句子", "期中", "qīzhōng — gli esami di metà periodo cadono all'inizio di novembre in alcune scuole.",
     "11月上旬,有的学校要___考试。", instr="Completa", size=19, gap=6)
e.head("C · 数字与日期 · Numeri e date", 25)
e.glossline("Usa l'esempio pratico di questa pagina.")
e.ex("A2", "完成句子", "240", "Il maglione costa 240 yuan nell'esempio.",
     "练习例子里,毛衣___元。", instr="Completa", size=19, gap=6)
e.ex("A2", "完成句子", "320", "240 + 80 = 320 yuan in tutto.",
     "毛衣和围巾一起___元。", instr="Completa", size=19, gap=6)
e.ex("B1", "完成句子", "270", "320 − 50 = 270 yuan dopo il taglio diretto.",
     "直降以后实付___元。", instr="Completa", size=19, gap=6)
e.ex("B1", "完成句子", "35", "L'evento del negozio WeChat dura 35 giorni in tutto.",
     "微信小店活动一共___天。", instr="Completa", size=19, gap=6)
e.head("D · 词语配对 · Abbinamenti", 25)
e.match_set("A2", "词汇配对",
            ["现货", "直降", "立减", "补冬"],
            ["冬天以前吃点好的,身体暖和",
             "已经在仓库里,马上就能发走",
             "结算时直接减掉的钱",
             "商品价格直接变低"],
            ["b", "d", "c", "a"],
            ["xiànhuò 现货 = merce in stock, b", "zhíjiàng 直降 = il prezzo scende, d", "lìjiǎn 立减 = sconto alla cassa, c", "bǔdōng 补冬 = mangiare bene prima dell'inverno, a"],
            instr="Abbina le parole")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-shenghuo.svg")
print("P2 saved, exercises so far:", len(REG))
