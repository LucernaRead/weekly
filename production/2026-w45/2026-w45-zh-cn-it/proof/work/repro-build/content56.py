# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-it-proof/work/repro-out/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 青年 (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("青年 · Youth", "Lucerna", "Livello B1 · AI电影 · 立冬新片 · Film AI e un film d'inverno")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-feature")
f.title("AI拍的电影,有人看吗?", 37)
f.byline("Redazione Lucerna · Livello di lettura B1")
f.para("10月23日,一部特别的电影上映了:《三星堆:未来往事》。特别在哪里?这部电影没有真人演员,所有角色都是电脑做出来的数字形象,画面和部分声音由AI生成。")
f.para("这是国内第一部拿到公映许可证的AI院线电影,片长100分钟,由博纳影业出品。电影讲的是三星堆的故事:古老的青铜器,加上未来的想象。")
f.para("可是,票房不太好。截至10月26日中午,猫眼专业版显示,上映4天,票房约119.2万元。10月24日和25日,平均每场只有2个人看。大家在争:AI能不能拍电影?技术很新,故事够不够好?")
f.para("也有人说,先别急着下结论。AI电影刚起步,画面、人物、台词都还在进步。重要的是:观众走进电影院,是为了看一个好故事,不是只看技术。")
f.gloss("shùzì xíngxiàng 数字形象 — un personaggio digitale · gōngyìng 公映 — un'uscita pubblica al cinema · piàofáng 票房 — gli incassi al botteghino.")
f.head("立冬那天,看一部新电影", 25)
f.para("11月7日星期六立冬,还有一部新电影上映:《我们仅有一次的人生》。宋佳演身患绝症的女火化师黄燕,文淇演失去母亲的少女姚雪。")
f.para("故事从一场意外开始:黄燕弄错了两份骨灰,坦白以后,两家人都不愿换回,只有姚雪相信她。两个人结伴上路,去换回骨灰,在冬天里彼此取暖、彼此救赎。")
f.para("这部电影原名《余烬》,入围过北京国际电影节天坛奖主竞赛单元,还拿了最佳摄影奖,片长114分钟。片方说:别以后,就现在。立冬那天,和重要的人,看冬天的第一部电影。")
f.gloss("huǒhuà 火化 — la cremazione · jiùshú 救赎 — la redenzione, salvarsi a vicenda · yǐhòu 以后 — dopo, un altro giorno.")
f.box("这一周的高频词 · Parole della settimana", [
    ("AI电影 — un film fatto con l'AI: nessun attore in carne e ossa, solo personaggi digitali.", "serif", False, INK, 20, 1.35),
    ("看电影之前,先看简介,再决定要不要买票。", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: popcorn + film dates + 你呢
ix = COLX[3]
image(p, "popcorn.jpg", ix, 200, CW, 220)
cy3 = caption(p, ix, 420, CW, "电影院的爆米花(资料图)。看电影的时候,很多人喜欢买一桶爆米花。",
              "Foto: Based5290 — Public domain (Wikimedia Commons)")
facts = ["10月23日 — 《三星堆:未来往事》上映",
         "10月26日中午 — 票房约119.2万元(猫眼)",
         "11月7日 — 《我们仅有一次的人生》上映",
         "11月7日 — 立冬,冬天第一天"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "电影小日历 · Date dei film", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "你呢?你会去看AI拍的电影吗?立冬那天,你想和谁去看电影?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("E tu? Guarderesti un film fatto dall'AI? Con chi guarderesti un film a 立冬? Scrivi due frasi in cinese.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · E tu?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "E tu? Guarderesti un film fatto dall'AI? Con chi guarderesti un film a 立冬? Scrivi due frasi in cinese.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Esercizi", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · 读一读选一选 · Leggi e scegli", 25)
e.glossline("Leggi la pagina 5 e scegli la risposta migliore.")
e.ex("B1", "单选", "A", "Il film AI non ha attori in carne e ossa.",
     "AI电影特别在哪里? A. 没有真人演员 · B. 全部在国外拍 · C. 只有10分钟", size=19, gap=6)
e.ex("B1", "单选", "B", "Il film AI dura 100 minuti.",
     "《三星堆》片长多少? A. 114分钟 · B. 100分钟 · C. 90分钟", size=19, gap=6)
e.ex("B1", "单选", "A", "A mezzogiorno del 26 ottobre, Maoyan indicava circa 1,192 milioni di yuan.",
     "截至10月26日中午票房约多少? A. 119.2万元 · B. 1192万元 · C. 11.92万元", size=19, gap=6)
e.ex("B1", "单选", "B", "Il nuovo film esce il 7 novembre, a Inizio dell'inverno.",
     "《我们仅有一次的人生》哪天上映? A. 10月23日 · B. 11月7日 · C. 11月15日", size=19, gap=6)
e.ex("B1", "单选", "B", "Huang Yan lavora in un crematorio.",
     "黄燕是什么职业? A. 记者 · B. 火化师 · C. 老师", size=19, gap=6)
e.head("B · 词语填空 · Completa gli spazi", 25)
e.glossline("Completa ogni spazio con la parola giusta.")
e.ex("B1", "完成句子", "数字", "shùzì — i personaggi del film sono immagini digitali.",
     "AI电影的角色是___形象。", instr="Completa", size=19, gap=6)
e.ex("B1", "完成句子", "票房", "piàofáng — incassi al botteghino, circa 1,192 milioni di yuan.",
     "上映4天,___约119.2万元。", instr="Completa", size=19, gap=6)
e.ex("B1", "完成句子", "火化", "huǒhuà — Huang Yan lavora in un crematorio.",
     "黄燕是一名女___师。", instr="Completa", size=19, gap=6)
e.ex("B1", "完成句子", "救赎", "jiùshú — le due donne si salvano a vicenda.",
     "两个人在冬天里彼此取暖、彼此___。", instr="Completa", size=19, gap=6)
e.ex("A2", "完成句子", "立冬", "lìdōng — il nuovo film esce a Inizio dell'inverno.",
     "新电影在___那天上映。", instr="Completa", size=19, gap=6)
e.head("C · 时间与数字 · Tempi e numeri", 25)
e.glossline("Rispondi con date e numeri della pagina 5.")
e.ex("B1", "完成句子", "23", "Il film AI è uscito il 23 ottobre.",
     "AI电影在10月___日上映。", instr="Completa", size=19, gap=6)
e.ex("B1", "完成句子", "100", "Il film AI dura 100 minuti.",
     "AI电影片长___分钟。", instr="Completa", size=19, gap=6)
e.ex("B1", "完成句子", "2", "Il 24–25 ottobre, ogni proiezione ha avuto in media 2 spettatori.",
     "10月24日和25日,平均每场___个人。", instr="Completa", size=19, gap=6)
e.ex("B1", "完成句子", "114", "Il nuovo film dura 114 minuti.",
     "新片片长___分钟。", instr="Completa", size=19, gap=6)
e.head("D · 词语配对 · Abbinamenti", 25)
e.match_set("B1", "词汇配对",
            ["数字形象", "票房", "火化师", "救赎"],
            ["电影卖票的钱",
             "电脑做出来的角色",
             "彼此帮助,重新活好",
             "火化遗体的工作人员"],
            ["b", "a", "d", "c"],
            ["数字形象 = un personaggio digitale, b", "票房 = incassi al botteghino, a", "火化师 = chi lavora in un crematorio, d", "救赎 = salvarsi a vicenda, c"],
            instr="Abbina le parole")
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-qingnian.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 深读 (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("深读 · Deep read", "Lucerna", "Livello B2 · 双11深读 · Perché le regole sono diventate più semplici")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-feature")
f.title("双11的规则,为什么变简单了?", 37)
f.byline("Redazione Lucerna · Livello di lettura B2")
f.para("今年的双11,有三个变化:现货多了,规则简单了,AI进来了。这三个变化,都和一个词有关:不用等。")
f.para("先说现货。以前,双11要先付定金、等很多天,才能付尾款。今年,京东10月12日就开始卖现货,淘宝和天猫10月20日也开始卖现货。现货就是已经在仓库里的货,买了就能发走,不用等生产、不用等预售结束。")
f.para("再说规则。以前,买东西要算满减、凑单、领券,算错了就亏了。今年,更多是官方立减和商品直降:价格直接写在商品页上,结算页的价格就是实付价。规则简单了,算错的机会也少了。")
f.para("还有AI。买之前,可以问一问AI助手:这件东西贵不贵?评价怎么样?有没有更便宜的?豆包今年加了「买前问豆包」的入口,千问等AI应用也接进了购物。AI不会帮你付钱,但可以帮你先看一看。")
f.para("还有新平台。微信小店第一次参加双11,活动从10月12日到11月15日,一共35天。第18个双11,平台多了,玩法也多了。")
f.para("可是,规则简单了,不等于东西一定最便宜。广告里说的「最低价」,要看清楚:是哪一天的价格?包不包运费?能不能退换货?结算页的价格,才是真正要付的钱。")
f.gloss("jiésuàn 结算 — la cassa, il pagamento del conto · yùnfèi 运费 — il costo di consegna · guǎnggào 广告 — una pubblicità.")
f.para("结论:双11变简单了,是因为现货多了、直降多了、AI帮忙了。但是,买东西以前,还是要做三件事:看结算页,看运费,看退换货规则。先看数据,再看广告。")
f.gloss("shuōfǎ 说法 — un'affermazione, quello che qualcuno dice · shùjù 数据 — dati, numeri misurati · tuìhuànhuò 退换货 — resi e cambi.")
f.para("练习篮子:篮子A是毛衣240元加围巾80元,直降50元,实付270元。篮子B是耳机199元,直降20元,实付179元。篮子C是书120元加本子40元,没有直降,实付160元。这些数字是练习数字,不是真实售价。")
f.end_report()

# ---- practice-data chart (cols 0-2), bars exactly proportional from zero ----
ly = 1210
p.text(MX, ly + 26, "三个练习篮子:直降以后实付多少钱 · Cesti di prova", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ly + 40, GOLD, 2)
rows = [("A: 毛衣+围巾", 270), ("B: 耳机", 179), ("C: 书+本子", 160)]
SCALE = 3.0
by0 = ly + 66
for i, (name, val) in enumerate(rows):
    yy = by0 + i * 58
    p.text(MX, yy + 34, name, 24, "sans", True, INK)
    bw_ = val * SCALE
    p.rect(MX + 260, yy + 6, bw_, 34, fill=OLIVE if i == 0 else GOLD)
    p.text(MX + 260 + bw_ + 16, yy + 34, f"{val} 元", 24, "serif", True, INK)
p.para(MX, by0 + 3 * 58 + 16, "Le barre partono da 0 (3 px = 1 yuan). Solo dati di esercizio — non sono prezzi reali. I calcoli sono nell'articolo qui sopra.", 20.5, "serif", False, GREY, 1388, 1.4)

# col 3: key points + three questions + 你呢
ix = COLX[3]
facts = ["现货多了 — 买了就能发走",
         "直降多了 — 结算页就是实付价",
         "AI进来了 — 买前先问一问",
         "结算页的价格才是真价格"]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "深读要点 · Punti chiave", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
qs = ["1. 这是说法,还是数据?",
      "2. 数据是谁量的?哪一天?",
      "3. 结算页的价格是多少?"]
qh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 14 for t in qs) + 30
p.rect(ix, ay3, CW, qh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ay3 + 16
p.text(ix + 22, yy3 + 26, "读新闻三问 · Tre domande", 24, "sans", True, OLIVE)
yy3 += 52
for t in qs:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 8
ey3 = ay3 + qh + 26
etvous = "你呢?买东西以前,你会先看什么?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("E tu? Che cosa controlli prima di comprare? Scrivi due frasi in cinese.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · E tu?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "E tu? Che cosa controlli prima di comprare? Scrivi due frasi in cinese.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", ey3 + eh)

# ---- P6 exercises ----
ey = 1560
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Esercizi", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · 读一读选一选 · Leggi e scegli", 25)
e.glossline("Leggi la pagina 6 e scegli la risposta migliore.")
e.ex("B2", "单选", "A", "Quest'anno le vendite in stock sono molto più grandi.",
     "今年双11第一个变化是什么? A. 现货多了 · B. 只有11月11日卖 · C. 必须先付定金", size=19, gap=6)
e.ex("B2", "单选", "A", "Con 直降 il prezzo alla cassa è quello che paghi.",
     "直降是什么意思? A. 结算页就是实付价 · B. 必须凑单 · C. 先付定金", size=19, gap=6)
e.ex("B2", "单选", "B", "L'AI ti aiuta a controllare prima prezzi e recensioni.",
     "AI能帮你做什么? A. 帮你付钱 · B. 先看一看价格和评价 · C. 直接送货", size=19, gap=6)
e.ex("B2", "单选", "B", "L'evento del negozio WeChat dura 35 giorni.",
     "微信小店活动多少天? A. 13天 · B. 35天 · C. 18天", size=19, gap=6)
e.ex("B2", "单选", "B", "La pagina di pagamento mostra quanto paghi davvero.",
     "真正要付的钱看哪里? A. 广告 · B. 结算页 · C. 朋友圈", size=19, gap=6)
e.head("B · 词语填空 · Completa gli spazi", 25)
e.glossline("Completa ogni spazio con la parola giusta.")
e.ex("B2", "完成句子", "现货", "xiànhuò — merce in stock, pronta per la spedizione.",
     "买了就能发走的货,叫___。", instr="Completa", size=19, gap=6)
e.ex("B2", "完成句子", "直降", "zhíjiàng — il prezzo stesso scende.",
     "价格直接变低,这叫___。", instr="Completa", size=19, gap=6)
e.ex("B2", "完成句子", "结算", "jiésuàn — la pagina di pagamento mostra il prezzo reale.",
     "真正要付的钱,看___页。", instr="Completa", size=19, gap=6)
e.ex("B2", "完成句子", "运费", "yùnfèi — il costo di consegna: controlla se è incluso.",
     "买东西要问:包不包___? ", instr="Completa", size=19, gap=6)
e.ex("B2", "完成句子", "广告", "guǎnggào — il «prezzo più basso» di una pubblicità va verificato.",
     "___里说的最低价,要看清楚。", instr="Completa", size=19, gap=6)
e.head("C · 练习篮子算一算 · Calcoli con i cesti", 25)
e.glossline("Calcola con i cesti di prova.")
e.ex("B2", "完成句子", "270", "240 + 80 = 320, meno 50 = 270 yuan.",
     "篮子A实付___元。", instr="Completa", size=19, gap=6)
e.ex("B2", "完成句子", "179", "199 − 20 = 179 yuan.",
     "篮子B实付___元。", instr="Completa", size=19, gap=6)
e.ex("B2", "完成句子", "160", "120 + 40 = 160 yuan, nessun taglio diretto.",
     "篮子C实付___元。", instr="Completa", size=19, gap=6)
e.ex("B2", "完成句子", "50", "Il cesto A è scontato di 50 yuan.",
     "篮子A直降___元。", instr="Completa", size=19, gap=6)
e.head("D · 词语配对 · Abbinamenti", 25)
e.match_set("B2", "词汇配对",
            ["说法", "数据", "结算页", "运费"],
            ["送货要花的钱",
             "真正要付的钱写在这里",
             "别人说的话,不一定是真的",
             "量出来的数字"],
            ["c", "d", "b", "a"],
            ["说法 = un'affermazione, c", "数据 = numeri misurati, d", "结算页 = la pagina di pagamento, b", "运费 = il costo di consegna, a"],
            instr="Abbina le parole")
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-shendu.svg")
print("P6 saved, exercises so far:", len(REG))
