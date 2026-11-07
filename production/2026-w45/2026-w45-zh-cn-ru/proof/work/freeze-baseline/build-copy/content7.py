# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-ru-proof/work/freeze-baseline/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Language focus", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Three levels, three topics")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与冬天 · Shopping", 24)
a.para("Shopping words for this week: 现货 (xiànhuò, in stock), 直降 (zhíjiàng, a direct cut), 立减 (lìjiǎn, off at checkout), 结算页 (jiésuàn yè, the checkout page). Winter words: 立冬 (lìdōng, Start of Winter), 补冬 (bǔdōng, eating well before winter), 厚衣服 (hòu yīfu, warm clothes).", 21.5)
a.glossline("Measure words still matter: 一件毛衣 (a sweater), 一条围巾 (a scarf), 一部电影 (a film).")
a.ex("A2", "完成句子", "件", "毛衣 takes the measure word 件 jiàn.",
     "我想买一___毛衣。", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "单选", "A", "直降 means the price itself drops.",
     "「直降」是什么意思? A. 价格直接变低 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "立冬", "lìdōng — Start of Winter, Nov 7.",
     "11月7日是___。", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "单选", "A", "Clothes take 件, not 个 or 条.",
     "哪个说法对? A. 一件毛衣 · B. 一个毛衣 · C. 一条毛衣", size=20.5, gap=10)
a.para("One more to practise: 「这件毛衣多少钱?」 (How much is this sweater?) When you shop, ask the price first, then pay.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Time & dates", 24)
b.para("Chinese gives times big → small: year, month, day, weekday, part of day, hour. Examples from this issue: 「11月7日星期六17点52分」 (Sat Nov 7, 17:52), 「11月10日星期二20点」 (Tue Nov 10, 20:00), 「11月15日凌晨3点」 (Nov 15, 3 a.m.). The biggest unit first, nothing out of order.", 21.5)
b.glossline("So English «Saturday evening, Nov 7» becomes 11月7日星期六晚上.")
b.ex("B1", "单选", "B", "凌晨 língchén — the small hours after midnight.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "06:00 is 早上 (morning), not evening.",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Big → small order: Nov 7, Saturday, 17:52.",
     "哪个顺序对? A. 11月7日星期六17点52分 · B. 17点52分星期六11月7日 · C. 星期六17点52分11月7日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周六", "Nov 7 is a Saturday — 周六.",
     "11月7日是星期六,也可以说___。立冬在这天。", instr="Fill in", size=20.5, gap=10)
b.para("Two more words: 凌晨 (língchén) is the small hours after midnight, before dawn; 傍晚 (bàngwǎn) is the short stretch just before dark.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Reading the news", 24)
c.para("When a story involves a claim (说法), separate three kinds of sentence: claims (说法), data (数据) and advertisements (广告). Page 6 is the example: 「最低价」 is a claim, the practice baskets' 270元 is practice data, and the checkout page shows what you really pay.", 21.5)
c.glossline("Ask of every price: whose number is it, and where is it written?")
c.ex("B2", "单选", "C", "「最低价」 is an advertising claim, not measured data.",
     "「最低价」在第6版里是什么? A. 数据 · B. 声明 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — measured numbers, not claims.",
     "买东西以前,先看___,再看广告。", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Data and the checkout page first; the headline last.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "结算", "jiésuàn — the checkout page shows the real price.",
     "真正要付的钱,看___页的价格。", instr="Fill in", size=20.5, gap=10)
c.para("Try it yourself: in the page-1 calendar box, 「11月7日」 is a date — data. The words in an advertisement are claims. Can you tell them apart?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de) marks how an action is done."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de) links verb + degree: 跑得快."),
    ("「我买了三只毛衣个」", "→ 「我买了三件毛衣。」", "Order: number + measure word + noun. The final 个 is one too many; sweaters take 件."),
    ("「立冬在星期六十一月七日」", "→ 「立冬在11月7日,星期六。」", "Times go big → small: weekday last."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所 · Error clinic", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看评价,再下单。」(First check the reviews, then order.) The frame 先…再… gives the order of actions. More: 「先看天气,再出门。」"
wcn = "Frame: 先 … 再 … — first X, then Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Sentence frame", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在上海。立冬那天,我吃了饺子,也给妈妈打了电话。双11,我买了一件毛衣,现货第二天就到了。」"
lcn = "编辑部示例信,不是真实来信。编辑部说明:VOL.1曾预告本期(VOL.2)刊登真实读者来信和VOL.1第8版最佳作文;至今没有收到真实来信,也没有可刊登的投稿,所以本期仍刊登编辑部示例,并继续征集。延期不是取消。Editor's note: VOL.1 promised real letters and the best VOL.1 writing in VOL.2. None have arrived, so this corner still prints an editor's example. Deferred, not cancelled."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
# NOTE: the disclosure above mixes Chinese and English in one string; the
# sans wrap measures CJK and Latin with the same SC face, so the height
# formula above (sans, 20pt) matches the render path. Verified in the build log.
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · Readers' corner", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · Phrases of the week (verbatim, from this issue's own articles)", 27, "sans", True, OLIVE)
quotes = [
    ("「不用等11月11日」", "No need to wait for Nov 11.", "p. 1"),
    ("「下单就能发货」", "Order it and it ships.", "p. 2"),
    ("「先看结算页,再付款」", "Check the checkout page, then pay.", "p. 2"),
    ("「水开始结冰」", "The water begins to freeze.", "p. 3"),
    ("「三场都输了」", "All three series lost.", "p. 4"),
    ("「小局一场没赢」", "Not a single game won.", "p. 4"),
    ("「故事够不够好」", "But is the story good enough?", "p. 5"),
    ("「别以后,就现在」", "Not later — now.", "p. 5"),
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
p.text(MX + 28, py + 44, "下期预告 · Next week (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "双11当天11月11日星期三,包裹到了吗?S16淘汰赛打完了,谁进了决赛?总决赛北京时间11月15日凌晨3点。还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
