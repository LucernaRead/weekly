# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/zh-cn-fix-round3/gates/freeze-baseline/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 青年 (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("青年 · Youth", "Lucerna", "Level B1 · 老电影重映 · 读书月 · A classic returns & Reading Month")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-feature")
f.title("老电影回来了,你去看吗?", 37)
f.byline("Lucerna editors · Reading level B1")
f.para("11月13日星期五,一部老电影要重映了:《海上钢琴师》。这部电影是1998年的意大利电影,导演是朱塞佩·托纳托雷,讲的是一个在船上出生、长大,从来没有下过船的钢琴师的故事。")
f.para("这一次重映,是4K修复版:老电影,新画面,声音和画面都更清楚了。这部电影在中国很受欢迎,豆瓣上有190多万人打分,分数是9.3分。2019年,它第一次在中国上映;现在,它又回来了。")
f.para("为什么老电影还要重映?因为好故事不会老。有人第一次看,有人再看一次:第一次看故事,第二次看音乐,第三次看人生选择——下船,还是不下船?")
f.para("也有人说,先别急着买票。老电影重映,票价和新片差不多,时间也不短。看之前,先看一看简介,再决定要不要去电影院。")
f.gloss("chóngyìng 重映 — to re-release, to show again · xiūfù 修复 — to restore (a film) · xuǎnzé 选择 — a choice, to choose.")
f.head("读书月:书,要走出去读", 25)
f.para("深圳读书月还在进行。11月7日,国际美术馆日:在艺术品中间读书,听一场关于阅读的讲座。11月14日,文化馆之夜:读者亲手摸古籍、抄经典。读书不只在家里,还可以走出去,在美术馆、在文化馆里读。")
f.para("读书月有七个场馆一起参加:美术馆、科学馆、图书馆、文化馆,还有湾区之眼。11月1日开幕,主题是悦读深圳、阅连世界。")
f.gloss("jiǎngzuò 讲座 — a talk, a lecture · chǎngguǎn 场馆 — a venue, a cultural venue.")
f.box("这一周的高频词 · Words of the week", [
    ("重映 — an old film shown again: 4K修复版,画面更清楚。", "serif", False, INK, 20, 1.35),
    ("看电影之前,先看简介,再决定要不要买票。", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: popcorn + film dates + 你呢
ix = COLX[3]
image(p, "popcorn.jpg", ix, 200, CW, 220)
cy3 = caption(p, ix, 420, CW, "电影院的爆米花(资料图)。看电影的时候,很多人喜欢买一桶爆米花。",
              "Photo: Based5290 — Public domain (Wikimedia Commons)")
facts = ["1998年 — 《海上钢琴师》第一次上映",
         "2019年 — 第一次在中国上映",
         "11月13日 — 4K修复版重映",
         "11月14日 — 深圳读书月文化馆之夜"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "电影小日历 · Film dates", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "你呢?你会去看重映的老电影吗?这个月,你在读什么书?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("And you? Would you watch a re-released classic? What are you reading this month? Write two sentences in Chinese.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · And you?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "And you? Would you watch a re-released classic? What are you reading this month? Write two sentences in Chinese.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · 读一读选一选 · Read & choose", 25)
e.glossline("Read page 5 and choose the best answer.")
e.ex("B1", "单选", "A", "The Pianist never left the ship.",
     "《海上钢琴师》讲的是谁? A. 从没下过船的钢琴师 · B. 船长 · C. 画家", size=19, gap=6)
e.ex("B1", "单选", "B", "The re-release is on Nov 13.",
     "重映在哪天? A. 11月11日 · B. 11月13日 · C. 11月15日", size=19, gap=6)
e.ex("B1", "单选", "A", "The film was first released in 1998.",
     "这部电影是哪年的? A. 1998年 · B. 2019年 · C. 2026年", size=19, gap=6)
e.ex("B1", "单选", "B", "Reading Month opened on Nov 1.",
     "深圳读书月哪天开幕? A. 11月7日 · B. 11月1日 · C. 11月14日", size=19, gap=6)
e.ex("B1", "单选", "B", "The culture night is on Nov 14.",
     "文化馆之夜在哪天? A. 11月7日 · B. 11月14日 · C. 11月1日", size=19, gap=6)
e.head("B · 词语填空 · Word blanks", 25)
e.glossline("Fill each blank with the right word.")
e.ex("B1", "完成句子", "重映", "chóngyìng — to show an old film again.",
     "老电影11月13日___了。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "修复", "xiūfù — the 4K version restores the old film.",
     "这一次是4K___版,画面更清楚。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "选择", "xuǎnzé — the pianist's choice: to leave the ship or not.",
     "电影讲了一个人生___:下船,还是不下船?", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "讲座", "jiǎngzuò — a talk about reading, at the art museum.",
     "美术馆日,还有一场关于阅读的___。", instr="Fill in", size=19, gap=6)
e.ex("A2", "完成句子", "场馆", "chǎngguǎn — seven venues take part in Reading Month.",
     "读书月有七个___一起参加。", instr="Fill in", size=19, gap=6)
e.head("C · 时间与数字 · Times & numbers", 25)
e.glossline("Answer with dates and numbers from page 5.")
e.ex("B1", "完成句子", "1998", "The film was first released in 1998.",
     "《海上钢琴师》是___年的电影。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "9.3", "Its Douban score is 9.3.",
     "豆瓣分数是___分。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "190", "More than 1.9 million people rated it on Douban.",
     "豆瓣上有___多万人打分。", instr="Fill in", size=19, gap=6)
e.ex("B1", "完成句子", "7", "Seven venues take part in Reading Month.",
     "读书月有___个场馆一起参加。", instr="Fill in", size=19, gap=6)
e.head("D · 词语配对 · Matching", 25)
e.match_set("B1", "词汇配对",
            ["重映", "修复", "讲座", "场馆"],
            ["办活动的地方,美术馆、图书馆",
             "听人讲,学东西的活动",
             "把老电影修好,画面更清楚",
             "老电影再上映一次"],
            ["d", "c", "b", "a"],
            ["重映 = shown again, d", "修复 = restored, c", "讲座 = a talk, b", "场馆 = a venue, a"],
            instr="Match the words")
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-qingnian.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 深读 (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("深读 · Deep read", "Lucerna", "Level B2 · 包裹深读 · Why the parcel peak comes in waves")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-feature")
f.title("包裹的高峰,为什么分三波?", 37)
f.byline("Lucerna editors · Reading level B2")
f.para("今年的双11,快递的高峰分三波,不是一天。第一波在10月20日到21日,第二波在10月31日,第三波在11月11日,也是最大的一波。为什么会这样?因为双11本身分三段:现货先卖,高潮场再来,最后一天收尾。")
f.para("先说第一波。10月20日晚上8点,淘宝和天猫付尾款、现货开售,很多人同一天付钱、下单。云仓的单量一下子到了日常的2.5倍。快递网点那天通宵收件,包裹开始一波一波地走。")
f.para("再说小高峰和大高峰。报道说,小高峰的单量约是日常的1.5倍,大高峰约是日常的3到4倍。10月31日是第二波,11月11日是第三波,也是最高峰:那天,各大平台都进入收尾,更多人下单,包裹也最多。")
f.para("还有前置的办法。顺丰今年推了预售极速达:付定金的时候,包裹就先送到离你近的地方,付了尾款,很快就能送到。前置的货量比去年多了35%。也就是说,有的包裹在你下单以前,已经在路上了。")
f.para("可是,高峰分三波,不等于包裹都准时到。天气、路况、网点的人手,都会影响速度。报道里,末端网点的收件量只比双11以前多了约20%,比云仓的涨幅小:前端多,末端慢,包裹就要排队。")
f.para("所以,买东西以前,还是要做三件事:看结算页,看运费,看退换货规则。包裹到了以后,先打开看一看,再确认收货。先看数据,再看广告,高峰来了也不慌。")
f.gloss("qiánzhì 前置 — placed in advance, moved forward early · mòduān 末端 — the last-mile end, the local delivery point · páiduì 排队 — to queue, to wait in line.")
f.para("结论:双11的包裹分三波,是因为活动分三段,人也分三批下单。高峰不是一天,是一段时间。知道这一点,等包裹的时候,就不用天天着急了。")
f.gloss("shuōfǎ 说法 — a claim, what someone says · shùjù 数据 — data, measured numbers · yùbào 预报 — a forecast, what is predicted, not yet fact.")
f.end_report()

# ---- reported-multiples chart (cols 0-2) ----
ly = 1210
p.text(MX, ly + 26, "快递单量:日常的几倍 · Reported parcel volumes (multiples of a normal day)", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ly + 40, GOLD, 2)
rows = [("日常", 1.0, "1 倍"), ("小高峰", 1.5, "约 1.5 倍"), ("首波 10月20日", 2.5, "2.5 倍"), ("大高峰 11月11日", 3.5, "3 到 4 倍")]
SCALE = 220.0
by0 = ly + 60
for i, (name, val, lab) in enumerate(rows):
    yy = by0 + i * 50
    p.text(MX, yy + 30, name, 24, "sans", True, INK)
    bw_ = val * SCALE
    p.rect(MX + 260, yy + 4, bw_, 30, fill=OLIVE if i == 0 else GOLD)
    p.text(MX + 260 + bw_ + 16, yy + 30, lab, 24, "serif", True, INK)
p.para(MX, by0 + 4 * 50 + 12, "Bars from 0; the last bar is drawn at 3.5, the middle of the reported 3–4 range. Multiples reported by 第一财经, Oct 23 (cloud warehouses and couriers); not parcel counts. Practice reading only.", 20.5, "serif", False, GREY, 1388, 1.4)

# col 3: key points + three questions + 你呢
ix = COLX[3]
facts = ["三波高峰 — 10月20日,10月31日,11月11日",
         "小高峰约 1.5 倍,大高峰 3 到 4 倍",
         "前置包裹 — 下单以前,已经在路上",
         "先看结算页,再确认收货"]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "深读要点 · Key points", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
qs = ["1. 这是说法,还是数据?",
      "2. 数据是谁量的?哪一天?",
      "3. 预报和事实,分得清吗?"]
qh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 14 for t in qs) + 30
p.rect(ix, ay3, CW, qh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ay3 + 16
p.text(ix + 22, yy3 + 26, "读新闻三问 · Three questions", 24, "sans", True, OLIVE)
yy3 += 52
for t in qs:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 8
ey3 = ay3 + qh + 26
etvous = "你呢?你的包裹等了几天?你会先打开看一看吗?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("And you? How many days did your parcel take? Do you open it and check first? Write two sentences in Chinese.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · And you?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "And you? How many days did your parcel take? Do you open it and check first? Write two sentences in Chinese.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", ey3 + eh)

# ---- P6 exercises ----
ey = 1560
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · 读一读选一选 · Read & choose", 25)
e.glossline("Read page 6 and choose the best answer.")
e.ex("B2", "单选", "A", "The parcel peak comes in three waves.",
     "快递高峰分几波? A. 三波 · B. 一波 · C. 五波", size=19, gap=6)
e.ex("B2", "单选", "A", "The first wave was on Oct 20–21.",
     "第一波在哪两天? A. 10月20日到21日 · B. 11月11日 · C. 10月12日", size=19, gap=6)
e.ex("B2", "单选", "B", "The biggest peak is on Nov 11.",
     "最大的一波在哪天? A. 10月31日 · B. 11月11日 · C. 11月13日", size=19, gap=6)
e.ex("B2", "单选", "B", "Front-loaded goods rose 35% year on year.",
     "顺丰前置货量比去年多了多少? A. 20% · B. 35% · C. 50%", size=19, gap=6)
e.ex("B2", "单选", "B", "Open the parcel and check before confirming receipt.",
     "包裹到了以后,先做什么? A. 直接确认收货 · B. 先打开看一看 · C. 先放一个月", size=19, gap=6)
e.head("B · 词语填空 · Word blanks", 25)
e.glossline("Fill each blank with the right word.")
e.ex("B2", "完成句子", "三波", "sānbō — the peak comes in three waves.",
     "快递高峰分___。", instr="Fill in", size=19, gap=6)
e.ex("B2", "完成句子", "前置", "qiánzhì — goods placed in advance, near the buyer.",
     "顺丰推了预售极速达,包裹先___了。", instr="Fill in", size=19, gap=6)
e.ex("B2", "完成句子", "末端", "mòduān — the local delivery end; its volume rose about 20%.",
     "___网点的收件量只多了约20%。", instr="Fill in", size=19, gap=6)
e.ex("B2", "完成句子", "排队", "páiduì — parcels queue when the last mile is slower.",
     "前端多,末端慢,包裹就要___。", instr="Fill in", size=19, gap=6)
e.ex("B2", "完成句子", "预报", "yùbào — a forecast is predicted, not yet fact.",
     "天气预报是___,不是已经发生的事。", instr="Fill in", size=19, gap=6)
e.head("C · 图表读数 · Read the chart", 25)
e.glossline("Read the chart on page 6.")
e.ex("B2", "完成句子", "1.5", "A small peak is about 1.5 times a normal day.",
     "小高峰约是日常的___倍。", instr="Fill in", size=19, gap=6)
e.ex("B2", "完成句子", "2.5", "The first wave reached 2.5 times a normal day.",
     "首波单量到了日常的___倍。", instr="Fill in", size=19, gap=6)
e.ex("B2", "完成句子", "3.5", "The last bar is drawn at 3.5, the middle of 3–4.",
     "图里大高峰画的是___倍。", instr="Fill in", size=19, gap=6)
e.ex("B2", "完成句子", "20", "Local outlets' intake rose about 20%.",
     "末端网点收件量多了约___%。", instr="Fill in", size=19, gap=6)
e.head("D · 词语配对 · Matching", 25)
e.match_set("B2", "词汇配对",
            ["说法", "数据", "预报", "前置"],
            ["还没发生的事,先猜一猜",
             "提前放到离买家近的地方",
             "别人说的话,不一定是真的",
             "量出来的数字"],
            ["c", "d", "a", "b"],
            ["说法 = a claim, c", "数据 = measured numbers, d", "预报 = a forecast, a", "前置 = placed in advance, b"],
            instr="Match the words")
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-shendu.svg")
print("P6 saved, exercises so far:", len(REG))
