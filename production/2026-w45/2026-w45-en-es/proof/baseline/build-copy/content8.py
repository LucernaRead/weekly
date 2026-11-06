# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/en-es-proof/baseline/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS · 练习与答案", "The Lucerna", "FINAL TEST · 综合评估 · Answers at the bottom of this page 答案在本版下方")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "11 月 3 日是周二"),
    ("A2", "A", "pizza 披萨"),
    ("B1", "C", "map 地图逐州变色"),
    ("A2", "B", "close 接近的"),
    ("A2", "A", "sticker 贴纸"),
    ("A2", "C", "will + 动词原形 know"),
    ("B1", "B", "be going to → is going"),
    ("B1", "A", "still 仍然"),
]
cnums = [reg_ex(lv, "完形填空", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · CLOZE · 完形填空", 24, gap=8)
bf.para(f"Leo is sixteen. On Tuesday, November 3, it is ({cnums[0]})___. His family does not cook dinner : they order ({cnums[1]})___. On television, the ({cnums[2]})___ changes colour, state by state. « Ohio is very ({cnums[3]})___ ! » says his father. At nine o'clock, Leo's mother comes home from voting, with a ({cnums[4]})___ on her jacket : « I VOTED ». « When ({cnums[5]})___ we know the results ? » asks Leo. « Tomorrow », says his mother. « Tomorrow, Leo is ({cnums[6]})___ to read the results at school — and the map will ({cnums[7]})___ be on television tonight. »", 21.5)
bf.bridge("选项：")
for n, (lv, _k, _nt), opts in zip(cnums, cloze_defs, [
    "A. Monday · B. Election Day · C. Halloween",
    "A. pizza · B. salad · C. soup",
    "A. phone · B. table · C. map",
    "A. far · B. close · C. big",
    "A. sticker · B. hat · C. ticket",
    "A. do · B. are · C. will",
    "A. goes · B. going · C. go",
    "A. still · B. never · C. soon",
]):
    bf.para(f"{n}. [{lv}] {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B · MULTIPLE CHOICE · 单选", 24, gap=8)
mcq = [
    ("A2", "B", "1:30 = half past one", "The clocks show 1:30. In words : ... A. one o'clock · B. half past one · C. a quarter to one"),
    ("A2", "A", "we → get 原形", "On Sunday, we ___ an extra hour of sleep. A. get · B. gets · C. getting"),
    ("B1", "B", "已发生的事用 fell", "The clocks ___ back on Sunday. A. fall · B. fell · C. falling"),
    ("B1", "B", "than → 比较级 bigger", "The Bernabéu is ___ than most stadiums. A. big · B. bigger · C. biggest"),
    ("B2", "A", "despite + 名词：尽管下雨", "___ the rain, the game went on all evening. A. Despite · B. Because · C. Unless"),
    ("B2", "A", "whether = 是否", "Nobody knows ___ the race is called yet. A. whether · B. what · C. who"),
    ("A2", "A", "将来时 will + 动词原形", "The film ___ on Friday, November 6. A. will open · B. will opened · C. will opens"),
    ("B1", "A", "be going to + 原形 vote", "They are going to ___ on Tuesday. A. vote · B. votes · C. voted"),
    ("B1", "C", "too close to call = 难分胜负", "« Too close to call » means... A. the winner is clear · B. voting is over · C. we do not know yet"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "单选", k, nt, body, size=20.5)

# ---- C. reading ----
bf.head("C · READING · 阅读理解", 24, gap=8)
bf.para("On Saturday morning, Sam, a teacher from Ohio, finished his breakfast and walked to the early-voting place near his school. There was no line. « On Tuesday, I teach all day », he explains. « Today, I have time. » Five minutes later, his ballot was in the box, and a sticker on his jacket said : I VOTED. On Tuesday night, Sam watched the map with his family — and Ohio was, as always, too close to call.", 21.5)
read_qs = [
    ("A2", "B", "原文：a teacher from Ohio", "Sam is... A. a nurse · B. a teacher · C. a driver"),
    ("A2", "B", "周二他全天教书", "He voted early because on Tuesday he... A. travels · B. teaches all day · C. sleeps"),
    ("B1", "A", "贴纸上写着 I VOTED", "His sticker said... A. I VOTED · B. VOTE ON TUESDAY · C. OHIO FIRST"),
    ("B1", "B", "俄亥俄一如既往难分胜负", "On Tuesday night, Ohio was... A. clear · B. too close to call · C. finished early"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "阅读理解", k, nt, body, size=20.5)

# ---- D. sentence building ----
bf.head("D · SENTENCES · 完成句子与转换", 24, gap=8)
d_items = [
    ("A2", "On Friday, they are going to watch the cat film.", "are going to + 原形",
     "Be going to : « On Friday, they (watch) the cat film. » → ___"),
    ("B1", "The clocks fell back on Sunday.", "fall → fell（不规则变化）",
     "Past simple : « The clocks (fall) back on Sunday. »"),
    ("B1", "taller", "tall → taller（比较级）",
     "Comparative : « The hat is ___ (tall) than the Cat. »"),
    ("B2", "Whether", "whether 引导“是否”从句",
     "Whether : « ___ the race is called, nobody knows yet. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "完成句子", k, nt, body, size=20.5)

# ---- E. translation ----
bf.head("E · TRANSLATION · 翻译", 24, gap=8)
e_items = [
    ("B2", "耐心是制度的一部分，而不是制度的失败。", "part of 一部分；not a failure 不是失败",
     "Translate : « Patience is part of the system, not a failure of it. »"),
    ("A2", "11 月 3 日周二是美国的选举日。", "Election Day 选举日；on Tuesday",
     "翻译：Tuesday, November 3, is Election Day in the United States."),
    ("B1", "这周日，NFL 在马德里比赛。", "on Sunday；in Madrid",
     "翻译：On Sunday, the NFL plays in Madrid."),
    ("B1", "并非每处都拨回时钟。", "not every 并非每处；change 变化",
     "Translate : « Not every place changes. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "翻译", k, nt, body, size=20.5)

# ---- F. matching ----
bf.head("F · WORDS · 词汇配对", 24, gap=8)
bf.match_set("B1", "词汇配对",
             ["a midterm", "a governor", "a ballot", "turnout"],
             ["the number of people who vote",
              "an election in the middle of a term",
              "the person who leads a state",
              "the paper you mark your choice on"],
             ["b", "c", "d", "a"],
             ["midterm = 中期选举 b", "governor = 州长 c", "ballot = 选票 d", "turnout = 投票率 a"],
             instr="配对")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ID", "投票时出示证件 ID"),
    ("A2", "line", "line = 排队（美式英语）"),
    ("A2", "ballot", "ballot = 选票"),
    ("A2", "sticker", "sticker = 贴纸"),
    ("B1", "Tuesday", "选举日是 11 月 3 日周二"),
]
gnums = [reg_ex(lv, "对话补全", k, nt) for lv, k, nt in dlg_defs]
bf.head("G · DIALOGUE · 对话补全", 24, gap=8)
bf.para(f"— Good morning ! Is this the voting place ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long today ? — No, five minutes only. On Tuesday it will be very long ! — Good. It is my first vote. What do I do with the ({gnums[2]})___ ? — Mark your choices, check them twice, then put it in the box. — Thank you. And the famous ({gnums[3]})___ ? Everybody has one on their jacket. — The sticker ! Here it is : « I VOTED ». Wear it with pride. — I will ! See you on ({gnums[4]})___ , in the results ! — Ha ! Have a good day.", 21.5)
bf.para("Levels : 145–148 [A2] · 149 [B1]", 19.5, "sans", False, GREY, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · WRITING · 写作 [B1]", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Tuesday, November 3 ». Tell us : did you watch the results, what did you eat, what did the map show — and one sentence about the clocks that fell back on Sunday night. The best texts will appear in VOL.3 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "用英语写 80–100 词：我的 11 月 3 日周二。写清你是否看了结果、吃了什么、地图显示了什么，再写一句周日夜里拨回的时钟。", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MODEL · 范文", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Tuesday, November 3, our family watched the election results at home. We ate pizza, because nobody wanted to cook on such a night. On television, the map changed colour, state by state, and my father said : « Ohio is too close to call ! » I did not understand every state, but I understood the pizza and the excitement. On Sunday night, the clocks had fallen back, so I slept one hour more. It was a long night, and a very American one.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "ANSWERS · 全部答案与简析（第 1–8 版）", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):
            s += f"（{e['note']}）"
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
