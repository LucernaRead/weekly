# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zhcn-vol1/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Language focus", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Three levels, three topics")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 购物与量词 · Measure words", 24)
a.para("When you shop, Chinese uses measure words (量词): 一件外套 (a coat), 一条围巾 (a scarf), 一斤蟹 (half a kilo of crab), 一只蟹 (one crab). The pattern is: number + measure word + noun (数词 + 量词 + 名词).", 21.5)
a.glossline("English counts things loosely; Chinese picks a measure word for each kind of thing — no plural, no -s.")
a.ex("A2", "完成句子", "件", "外套 takes the measure word 件 jiàn.",
     "我想买一___外套。", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "单选", "B", "围巾 takes 条 tiáo (long, soft things).",
     "「一条」可以说什么? A. 一条外套 · B. 一条围巾 · C. 一条大闸蟹", size=20.5, gap=10)
a.ex("A2", "完成句子", "斤", "斤 jīn — half a kilo; market prices are per 斤.",
     "大闸蟹多少钱一___?", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "单选", "A", "Clothes take 件, not 个 or 条.",
     "哪个说法对? A. 一件衣服 · B. 一个衣服 · C. 一条衣服", size=20.5, gap=10)
a.para("One more to practise: 「这件外套多少钱?」 (How much is this coat?) When you shop, ask the price first, then pay.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Time & dates", 24)
b.para("Chinese gives times big → small: year, month, day, weekday, part of day, hour. Example: 「10月20日晚上8点」 (Oct 20, 8 p.m.) — the biggest unit first, nothing out of order.", 21.5)
b.glossline("So English «Friday evening, Oct 23» becomes 10月23日星期五晚上.")
b.ex("B1", "单选", "B", "凌晨 língchén — the small hours after midnight.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "上午", "The NBA opened in the morning, Beijing time.",
     "NBA 在北京时间10月21日___开打。(不是晚上)", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Big → small order: Oct 20, evening, 8 o'clock.",
     "哪个顺序对? A. 10月20日晚上8点 · B. 8点晚上10月20日 · C. 晚上8点10月20日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周五", "Oct 23 is a Friday — 周五.",
     "10月23日是星期五,也可以说___。霜降在这天。", instr="Fill in", size=20.5, gap=10)
b.para("Two more words: 凌晨 (língchén) is the small hours after midnight, before dawn; 傍晚 (bàngwǎn) is the short stretch just before dark.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Reading the news", 24)
c.para("When a story involves a dispute (争议), separate three kinds of sentence: online claims (说法), official statements (声明) and market data (数据). Claims can exaggerate; data must keep its source and its date. Page 6 is the example: 「暴跌40%」 is a claim, 77.5 元 and 57.5 元 are data, 「崩盘不实」 is a statement.", 21.5)
c.glossline("Ask of every number: who measured it, and when?") 
c.ex("B2", "单选", "C", "「暴跌40%」 was an online claim, not measured data.",
     "「暴跌超过40%」在第6版里是什么? A. 数据 · B. 声明 · C. 网上的说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "声明", "声明 shēngmíng — the association's official statement.",
     "协会10月19日发表___,说「崩盘」不是真的。", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Data and source first; the headline last.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和出处 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "25.8", "The real, computed drop on page 6 is 25.8%.",
     "第6版真正算出的数据降幅是___%。", instr="Fill in", size=20.5, gap=10)
c.para("Try it yourself: in the page-1 hot-search box, 「第 8 位」 is a ranking — data. The words in a headline are claims. Can you tell them apart?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de) marks how an action is done; it goes before the verb."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de) links a verb to a degree complement: 跑得快."),
    ("「我买了三只大闸蟹个」", "→ 「我买了三只大闸蟹。」", "Order: number + measure word + noun. The final 个 is one too many; crabs take 只."),
    ("「霜降在星期五十月二十三日」", "→ 「霜降在10月23日,星期五。」", "Times go big → small: month and day first, weekday last."),
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
wt = "「先付定金,后付尾款。」(First the deposit, then the balance.) The frame 先…后/再… gives the order of actions. More: 「先看天气,再出门。」「先洗手,再吃饭。」"
wcn = "Frame: 先 … 后/再 … — first X, then Y. Make your own sentence."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Sentence frame", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在多伦多。霜降那天,我吃了柿子,也给妈妈打了电话。我的购物车里有一件外套,还在等付尾款。」"
lcn = "An editor's example letter — not a real one. VOL.2 will print real readers' letters and the best page-8 writing!"
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
    ("「今年的双11来得早」", "This year's 双11 came early.", "p. 1"),
    ("「付完尾款，快递就开始送货了」", "Once the balance is paid, delivery starts.", "p. 1"),
    ("「付完尾款，商家就发货」", "Once you pay the balance, the seller ships.", "p. 2"),
    ("「遥知兄弟登高处，遍插茱萸少一人」", "Wang Wei's famous 重阳 line (poem).", "p. 3"),
    ("「两个分数只差2.735分」", "The two scores differ by only 2.735 points.", "p. 4"),
    ("「最大的看点是詹姆斯」", "The biggest draw is LeBron.", "p. 4"),
    ("「看S16，要通宵了」", "Watching S16 means staying up all night.", "p. 5"),
    ("「先看数据，再看标题」", "Data first, headline last (page 6's rule).", "p. 6"),
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
p.text(MX + 28, py + 44, "下期预告 · Next week (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16 瑞士轮打完了:LPL 的四支队打得怎么样?双11 的包裹都到了吗?我们追踪报道。11月7日是立冬,冬天要来了。还有你们的来信和第 8 版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
