# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS　练习与答案", "The Lucerna", "FINAL TEST　综合评估　Answers at the bottom of this page 答案在本版下方")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "11 月 11 日是周三"),
    ("A2", "A", "poppy 罂粟花"),
    ("B1", "C", "silence 默哀、寂静"),
    ("A2", "B", "eleven 十一"),
    ("A2", "A", "Pudsey 黄色小熊"),
    ("A2", "C", "will + 动词原形 know"),
    ("B1", "B", "be going to → is going"),
    ("B1", "A", "still 仍然"),
]
cnums = [reg_ex(lv, "完形填空", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　CLOZE　完形填空", 24, gap=8)
bf.para(f"Maya is sixteen. On ({cnums[0]})___, November 11, she wears a red ({cnums[1]})___ to school. At eleven o'clock, the whole school stands in ({cnums[2]})___ for two minutes. « ({cnums[3]})___, eleven, eleven », says her teacher. On Friday, Maya bakes cakes for ({cnums[4]})___, the yellow bear. « When ({cnums[5]})___ we know the total ? » asks Maya. « On Friday night », says her mother. « On Sunday, Maya is ({cnums[6]})___ to watch the game from Munich — and the poppy will ({cnums[7]})___ be on her coat. »", 21.5)
bf.bridge("选项：")
for n, (lv, _k, _nt), opts in zip(cnums, cloze_defs, [
    "A. Monday · B. Wednesday · C. Friday",
    "A. poppy · B. hat · C. ticket",
    "A. noise · B. music · C. silence",
    "A. Ten · B. Eleven · C. Twelve",
    "A. Pudsey · B. Scrooge · C. Dickens",
    "A. do · B. are · C. will",
    "A. goes · B. going · C. go",
    "A. still · B. never · C. soon",
]):
    bf.para(f"{n}. [{lv}] {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B　MULTIPLE CHOICE　单选", 24, gap=8)
mcq = [
    ("A2", "B", "11 点 = eleven o'clock", "The silence begins at 11 a.m. In words : ... A. ten o'clock · B. eleven o'clock · C. twelve o'clock"),
    ("A2", "A", "we → wear 原形", "On Wednesday, we ___ a poppy. A. wear · B. wears · C. wearing"),
    ("B1", "B", "已发生的事用 wrote", "Dickens ___ the story in 1843. A. writes · B. wrote · C. writing"),
    ("B1", "B", "than → 比较级 bigger", "The Allianz Arena is ___ than most NFL stadiums. A. big · B. bigger · C. biggest"),
    ("B2", "A", "despite + 名词：尽管下雨", "___ the rain, the ceremony went on all morning. A. Despite · B. Because · C. Unless"),
    ("B2", "A", "whether = 是否", "Nobody knows ___ this year will be faster. A. whether · B. what · C. who"),
    ("A2", "A", "将来时 will + 动词原形", "The film ___ on Friday, November 13. A. will open · B. will opened · C. will opens"),
    ("B1", "A", "be going to + 原形 watch", "They are going to ___ the game on Sunday. A. watch · B. watches · C. watched"),
    ("B1", "C", "challenge yourself = 接受挑战", "« Challenge yourself » means... A. the show is over · B. voting is closed · C. take on a challenge"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "单选", k, nt, body, size=20.5)

# ---- C. reading ----
bf.head("C　READING　阅读理解", 24, gap=8)
bf.para("On Wednesday morning, Tom, a teacher from Manchester, finished his breakfast and walked to school early. At eleven o'clock, the whole school stood still for two minutes. There was no sound in the hall. « We remember them », said Tom, quietly. In the afternoon, his class baked 26 cakes for Children in Need, and a poppy box stood by the door. On Friday night, Tom watched the appeal show with his family — and Pudsey was, as always, yellow and smiling.", 21.5)
read_qs = [
    ("A2", "B", "原文：a teacher from Manchester", "Tom is... A. a nurse · B. a teacher · C. a driver"),
    ("A2", "B", "全校默哀两分钟", "At eleven o'clock, the school... A. sang · B. stood still for two minutes · C. went home"),
    ("B1", "A", "班级烤了 26 个蛋糕", "His class baked... A. 26 cakes · B. 11 cakes · C. 13 cakes", ),
    ("B1", "B", "Pudsey 一如既往是黄色的", "On Friday night, Pudsey was... A. red · B. yellow and smiling · C. asleep"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "阅读理解", k, nt, body, size=20.5)

# ---- D. sentence building ----
bf.head("D　SENTENCES　完成句子与转换", 24, gap=8)
d_items = [
    ("A2", "On Friday, they will watch the appeal show.", "will + 原形",
     "Will future : « On Friday, they (watch) the appeal show. » → ___"),
    ("B1", "The guns fell silent in 1918.", "fall → fell（不规则变化）",
     "Past simple : « The guns (fall) silent in 1918. »"),
    ("B1", "bigger", "big → bigger（比较级）",
     "Comparative : « The arena is ___ (big) than most stadiums. »"),
    ("B2", "Whether", "whether 引导“是否”从句",
     "Whether : « ___ this year will be faster, nobody knows yet. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "完成句子", k, nt, body, size=20.5)

# ---- E. translation ----
bf.head("E　TRANSLATION　翻译", 24, gap=8)
e_items = [
    ("B2", "耐心是制度的一部分，而不是制度的失败。", "part of 一部分；not a failure 不是失败",
     "Translate : « Patience is part of the system, not a failure of it. »"),
    ("A2", "11 月 11 日周三上午 11 点，英国默哀两分钟。", "at 11 a.m.；two minutes of silence",
     "翻译：At 11 a.m. on Wednesday, November 11, Britain holds two minutes of silence."),
    ("B1", "这周日，NFL 在慕尼黑比赛。", "on Sunday；in Munich",
     "翻译：On Sunday, the NFL plays in Munich."),
    ("B1", "并非每个国家都叫它同一个名字。", "not every 并非每个；call 称呼",
     "Translate : « Not every country calls it by the same name. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "翻译", k, nt, body, size=20.5)

# ---- F. matching ----
bf.head("F　WORDS　词汇配对", 24, gap=8)
bf.match_set("B1", "词汇配对",
             ["a silence", "an armistice", "a runoff", "a miser"],
             ["the second vote, when no one wins a majority",
              "a quiet time with no speaking",
              "an agreement to stop fighting",
              "a person who loves money and hates spending it"],
             ["b", "c", "a", "d"],
             ["silence=默哀 b", "armistice=停战协定 c", "runoff=决胜轮 a", "miser=守财奴 d"],
             instr="配对")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ticket", "ticket = 票"),
    ("A2", "line", "line = 排队（美式英语）"),
    ("A2", "scarf", "scarf = 围巾"),
    ("A2", "anthem", "anthem = 国歌、颂歌"),
    ("B1", "Sunday", "比赛是 11 月 15 日周日"),
]
gnums = [reg_ex(lv, "对话补全", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　对话补全", 24, gap=8)
bf.para(f"— Good morning ! Is this the way to the Allianz Arena ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long ? — No, five minutes only. It is my first NFL game. What do I do with the ({gnums[2]})___ ? — Wear it with pride, and cheer for the Lions. — And the famous ({gnums[3]})___ ? — Two anthems, one game. Enjoy Munich. — I will ! See you on ({gnums[4]})___ ! — Have a good day.", 21.5)
bf.para("Levels : 145–148 [A2] · 149 [B1]", 19.5, "sans", False, GREY, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　WRITING　写作 [B1]", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Wednesday, November 11 ». Tell us : did you stand still at eleven, what did you wear, what did you watch on Friday — and one sentence about the game in Munich on Sunday. The best texts will appear in VOL.4 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "用英语写 80–100 词：我的 11 月 11 日周三。写清你是否在 11 点静立、佩戴了什么、周五看了什么，再写一句周日在慕尼黑的比赛。", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, "MODEL　范文", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Wednesday, November 11, our school stopped for two minutes. At eleven o'clock, the hall went quiet, and I thought about the soldiers of the First World War. In the evening, we watched the news from London, and my mother wore her poppy at dinner. On Friday, we baked 26 cakes for Children in Need, and Pudsey smiled from the television. On Sunday, we watched the game from Munich. It was a week of silence, kindness and sport — and I slept well, because I had remembered.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANSWERS　全部答案与简析（第1–8版）", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 第{pg}版 —", 17, "sans", True, OLIVE, 1.28, 3)
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
