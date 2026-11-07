# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-cn-core/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Language focus", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Three levels, three topics")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与包裹 · Shopping", 24)
a.para("Shopping words for this week: 高潮场 (gāocháochǎng, the peak sale period), 包裹 (bāoguǒ, a parcel), 取件码 (qǔjiànmǎ, a pick-up code), 快递柜 (kuàidìguì, a parcel locker). Safety words: 消防 (xiāofáng, fire prevention), 疏散 (shūsàn, to evacuate), 自救 (zìjiù, self-rescue).", 21.5)
a.glossline("Measure words still matter: 一个包裹 (a parcel), 一部电影 (a film), 一场演练 (a drill).")
a.ex("A2", "完成句子", "个", "包裹 takes the measure word 个 gè.",
     "我拿了___包裹。", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "单选", "A", "高潮场 means the peak sale period.",
     "「高潮场」是什么意思? A. 最忙的卖货时间 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "消防", "xiāofáng — fire prevention, Nov 9.",
     "11月9日是全国___日。", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "单选", "A", "Parcels take 个, not 只 or 条.",
     "哪个说法对? A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20.5, gap=10)
a.para("One more to practise: 「我的包裹到了吗?」 (Has my parcel arrived?) When you wait for a parcel, ask first, then go to the locker.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Time & dates", 24)
b.para("Chinese gives times big → small: year, month, day, weekday, part of day, hour. Examples from this issue: 「11月9日星期一」 (Mon Nov 9), 「11月10日星期二20点」 (Tue Nov 10, 20:00), 「11月15日星期日凌晨3点」 (Sun Nov 15, 3 a.m.). The biggest unit first, nothing out of order.", 21.5)
b.glossline("So English «Monday, Nov 9» becomes 11月9日星期一.")
b.ex("B1", "单选", "B", "凌晨 língchén — the small hours after midnight.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "06:00 is 早上 (morning), not evening.",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Big → small order: Nov 15, Sunday, 03:00.",
     "哪个顺序对? A. 11月15日星期日凌晨3点 · B. 凌晨3点星期日11月15日 · C. 星期日凌晨3点11月15日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周一", "Nov 9 is a Monday — 周一.",
     "11月9日是星期一,也可以说___。消防日在这天。", instr="Fill in", size=20.5, gap=10)
b.para("Two more words: 凌晨 (língchén) is the small hours after midnight, before dawn; 傍晚 (bàngwǎn) is the short stretch just before dark.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Reading the news", 24)
c.para("When a story involves a claim (说法), separate three kinds of sentence: claims (说法), data (数据) and forecasts (预报). Page 6 is the example: 「最大的一波」 is a claim about Nov 11, the multiples 1.5 and 2.5 are reported data, and the cold-air temperatures are a forecast — predicted, not yet fact.", 21.5)
c.glossline("Ask of every number: whose number is it, and when was it measured?")
c.ex("B2", "单选", "C", "「最大的一波」 is a claim about the Nov 11 peak, not measured data.",
     "「最大的一波」在第6版里是什么? A. 数据 · B. 预报 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — measured numbers, not claims.",
     "买东西以前,先看___,再看广告。", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Data and the checkout page first; the headline last.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — a forecast is predicted, not yet fact.",
     "冷空气的温度是___,还没发生。", instr="Fill in", size=20.5, gap=10)
c.para("Try it yourself: in the page-1 calendar box, 「11月11日」 is a date — data. The words in an advertisement are claims. Can you tell them apart?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) marks how an action is done."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) links verb + degree: 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "Order: number + measure word + noun."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日,星期日凌晨3点。」", "Times go big → small: weekday last."),
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
wt = "「先看取件码,再开柜门。」(Check the code, then open the locker.) The frame 先…再… gives the order of actions."
wcn = "Frame: 先 … 再 … — first X, then Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Sentence frame", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在北京。11月9日学校做了消防演练,我学会了走楼梯。双11我买了一本书,包裹两天就到了。周日凌晨,我想看S16总决赛!」"
lcn = "编辑部示例信,不是真实来信。VOL.2曾预告本期刊登真实来信和最佳作文;截至11月2日截稿,仍未收到,本期仍刊示例,继续征集。延期不是取消。Editor's note: VOL.2 promised real letters in VOL.3; none arrived by Nov 2. The example stands. Deferred, not cancelled."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
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
    ("「双11的正日子」", "Double 11 day itself.", "p. 1"),
    ("「先看结算页,再决定买不买」", "Check the checkout page, then decide.", "p. 2"),
    ("「提高自防自救能力」", "Raise self-protection and self-rescue ability.", "p. 3"),
    ("「三支队进了八强」", "Three teams reached the quarter-finals.", "p. 4"),
    ("「输了就回家」", "Lose and you go home.", "p. 4"),
    ("「老电影,新画面」", "An old film, a new picture.", "p. 5"),
    ("「快递的高峰分三波」", "The parcel peak comes in three waves.", "p. 6"),
    ("「着火了不坐电梯」", "In a fire, do not take the lift.", "p. 3"),
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
p.text(MX + 28, py + 44, "下期预告 · Next week (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16总决赛打完了,谁是冠军?包裹都到了吗?还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
