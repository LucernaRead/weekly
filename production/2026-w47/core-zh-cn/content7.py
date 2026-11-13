# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/core-zh-cn/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语　Language focus", "Lucerna", "语言聚焦　三个级别，三个主题　Three levels, three topics")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　决赛与包裹　Final & parcels", 24)
a.para("Words for this week: 决赛 (juésài, the final), 冠军 (guànjūn, the champion), 半决赛 (bànjuésài, the semi-final), 到货 (dàohuò, arrived), 退换货 (tuìhuànhuò, returns and exchanges), 价保 (jiàbǎo, price protection).", 21.5)
a.glossline("Measure words still matter: 一个包裹 (a parcel), 一部电影 (a film), 一场演练 (a drill).")
a.ex("A2", "完成句子", "个", "包裹 takes the measure word 个 gè.",
     "我拿了___包裹。", instr="Fill in", size=20, gap=10)
a.ex("A2", "单选", "A", "决赛 means the final, the last match.",
     "「决赛」是什么意思？ A. 最后一场比赛 · B. 第一场比赛 · C. 练习赛", size=20, gap=10)
a.ex("A2", "完成句子", "决赛", "juésài — the final; BLG vs GEN on Nov 15.",
     "11月15日凌晨3点，BLG和GEN打___。", instr="Fill in", size=20, gap=10)
a.ex("A2", "单选", "A", "Parcels take 个, not 只 or 条.",
     "哪个说法对？ A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20, gap=10)
a.para("One more to practise: 「我的包裹到了吗？」 (Has my parcel arrived?) When you wait for a parcel, ask first, then go to the locker.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　时间与日期　Time & dates", 24)
b.para("Chinese gives times big → small: year, month, day, weekday, part of day, hour. Examples from this issue: 「11月15日星期日凌晨3点」 (Sun Nov 15, 3 a.m.), 「11月22日星期日」 (Sun Nov 22), 「11月21日星期六」 (Sat Nov 21). The biggest unit first, nothing out of order.", 21.5)
b.glossline("So English «Sunday, Nov 22» becomes 11月22日星期日.")
b.ex("B1", "单选", "B", "凌晨 língchén — the small hours after midnight.",
     "「凌晨3点」是什么时候？ A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20, gap=10)
b.ex("B1", "完成句子", "早上", "06:00 is 早上 (morning), not evening.",
     "半决赛在北京时间11月8日___6点开始。（不是晚上）", instr="Fill in", size=20, gap=10)
b.ex("B1", "单选", "A", "Big → small order: Nov 22, Sunday.",
     "哪个顺序对？ A. 11月22日星期日 · B. 星期日11月22日 · C. 星期日小雪11月22日", size=20, gap=10)
b.ex("B1", "完成句子", "周日", "Nov 22 is a Sunday — 周日.",
     "11月22日是星期日，也可以说___。小雪在这天。", instr="Fill in", size=20, gap=10)
b.para("Two more words: 凌晨 (língchén) is the small hours after midnight, before dawn; 傍晚 (bàngwǎn) is the short stretch just before dark.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　读新闻　Reading the news", 24)
c.para("When a story involves a claim (说法), separate three kinds of sentence: claims (说法), data (数据) and forecasts (预报). Page 6 is the example: 「没有爆掉」 is a claim about this year's parcels, the 139.38亿件 total is reported data — already counted, not a guess — and 「第三波是最高峰」 is a forecast from 中通云仓: expected, not yet counted.", 21.5)
c.glossline("Ask of every number: whose number is it, and when was it measured?")
c.ex("B2", "单选", "A", "「139.38亿件」 is a final count from the postal bureau, already counted.",
     "「139.38亿件」在第6版里是什么？ A. 已经数完的事实 · B. 邮政局的预计 · C. 广告词", size=20, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — measured numbers, not claims.",
     "买东西以前，先看___，再看广告。", instr="Fill in", size=20, gap=10)
c.ex("B2", "单选", "B", "Data and the checkout page first; the headline last.",
     "读新闻时，哪个做法最好？ A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — a forecast is predicted, not yet fact.",
     "「第三波是最高峰」是___，还没发生。", instr="Fill in", size=20, gap=10)
c.para("Try it yourself: in the page-1 calendar box, 「11月22日」 is a date — data. The words in an advertisement are claims. Can you tell them apart?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters + image ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) marks how an action is done."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) links verb + degree: 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "Order: number + measure word + noun."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日，星期日凌晨3点。」", "Times go big → small: weekday last."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所　Error clinic", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看预报，再决定穿什么。」The frame 先…再… gives the order of actions."
wcn = "Frame: 先 … 再 … — first X, then Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式　Sentence frame", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好！我住在上海。11月9日半决赛，我看了BLG打T1，3比1，真好看！双11我买了一件外套，包裹两天就到了。你们呢？」"
lcn = "编辑部示例信，不是真实来信。VOL.3曾预告本期刊登真实来信和最佳作文；截至11月10日截稿，仍未收到，继续征集。延期不是取消。Editor's note: VOL.3 promised real letters in VOL.4; none arrived by Nov 10. Deferred, not cancelled."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地　Readers' corner", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- P7 image (brush) below the letters box ----
iy7 = col3_end + 12
image(p, "brush.jpg", bx, iy7, CW, 130)
cy7 = caption(p, bx, iy7 + 130, CW, "毛笔（资料图）。写中文，先从一笔一画开始。",
              "Photo: Mx. Granger — CC0 (Wikimedia Commons)")
img_end = cy7
print("P7 image ends", img_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, img_end + 44)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "本周金句　Phrases of the week (verbatim, from this issue's own articles)", 27, "sans", True, OLIVE)
quotes = [
    ("「决赛对阵GEN」", "The final: BLG vs GEN.", "p. 1"),
    ("「包裹都到了吗」", "Have the parcels all arrived?", "p. 2"),
    ("「小雪气寒而将雪矣」", "Minor Snow: the air turns cold, snow is coming.", "p. 3"),
    ("「两支中国队进了四强」", "Two Chinese teams reached the semi-finals.", "p. 4"),
    ("「先看简介，再决定」", "Read the synopsis first, then decide.", "p. 5"),
    ("「无高峰，全高峰」", "No one peak — every day is a peak.", "p. 6"),
    ("「先打开看一看，再确认收货」", "Open and check first, then confirm receipt.", "p. 6"),
    ("「悦读深圳」", "Joyful reading in Shenzhen — the theme of Shenzhen Reading Month.", "p. 3"),
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
p.text(MX + 28, py + 44, "下期预告　Next week (VOL.5)", 24, "sans", True, GOOSE)
p.para(MX + 28, py + 84, "S16总决赛打完了，谁是冠军？小雪之后，冬天怎么过？还有你们的来信和第8版最佳作文。下周见！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
