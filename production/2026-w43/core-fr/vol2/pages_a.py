# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-vol2/svg")
os.makedirs(OUT, exist_ok=True)
X0, X1 = 64, 1016
W = X1 - X0

def header_band(p, band, title, sub=""):
    p.rect(48, 48, 984, 86, fill=DARK)
    p.text(72, 103, band, 30, "sans", True, "#f3edda")
    p.text(X1 - 24, 103, title, 30, "serif", True, "#f3edda", anchor="end")
    if sub:
        p.text(X1 - 24, 128, sub, 19, "sans", False, "#b3a06a", anchor="end")
    return 168

def foot(p, page_no):
    p.hline(X0, X1, 1336, GOLD, 1.5)
    p.text(X0, 1372, "每日一句 · 法语周报 VOL.1", 20, "sans", False, GREY)
    p.text(X1, 1372, f"第 {page_no} 版 / 共 5 版", 20, "sans", False, GREY, anchor="end")

# ================= Page 1 · 头版 =================
p = Page()
p.text(X0, 96, "VOL. 1 · 第一期", 22, "sans", True, OLIVE)
p.text(540, 96, "墨迹书每日一句", 22, "sans", False, GREY, anchor="middle")
p.text(X1, 96, "2026.10.15 — 10.21", 22, "sans", False, GREY, anchor="end")
p.hline(X0, X1, 116, GOLD, 1.5)
p.text(540, 218, "The Lucerna", 104, family="UnifrakturMaguntia", anchor="middle")
p.text(540, 262, "法 语 周 报 · 每 日 一 句", 40, "serif", True, INK, anchor="middle")
p.text(540, 300, "LUCERNA FRENCH WEEKLY — READ REAL BOOKS, ONE SENTENCE A DAY", 17, "sans", False, GREY, anchor="middle")
p.hline(X0, X1, 322, INK, 2.6); p.hline(X0, X1, 330, INK, 1)

# 时事句 band
p.rect(X0, 352, W, 128, fill=BOX, stroke=LINE, sw=1.5)
p.text(X0 + 26, 398, "本周时事句", 21, "sans", True, BRICK)
p.text(X0 + 26, 442, "« L'automne est le printemps de l'hiver. »", 33, "serif", True, INK)
p.text(X1 - 26, 398, "霜降 · 10月23日(周五)", 21, "sans", True, BRICK, anchor="end")
p.text(X1 - 26, 442, "秋天,是冬天的春天。", 26, "serif", False, GREY, anchor="end")
p.text(X0 + 26, 470, "传为法国画家图卢兹-洛特雷克语。本周五霜降,秋天的最后一个节气——这句正应景。", 20, "sans", False, GREY)

# Left column: 本周时事
lx, lw = X0, 566
y = 512
y = p.section_head(lx, y + 30, "本 周 时 事", 30) + 34
illus_climb(p, lx + 8, y - 6, 0.92)
p.text(lx + 262, y + 26, "重阳已至 · 10月18日(周日)", 26, "serif", True, INK)
y = p.para(lx + 262, y + 62, "九九重阳,登高赏菊。本周的 No.004 正出自《基督山伯爵》:« Attendez et espérez ! »——等待,希望吧:登高望远的人,心里装的正是这两样。", 23, "serif", False, INK, lw - 262, 1.5)
y = max(y, 512 + 44 + 140) + 16
illus_frost(p, lx + 30, y - 4, 1.05)
p.text(lx + 262, y + 26, "霜降将至 · 10月23日(周五)", 26, "serif", True, INK)
y = p.para(lx + 262, y + 62, "秋季最后一个节气。法语里「霜」是 la gelée blanche。下周的每日一句将走进深秋:落叶、寒霜与诸圣节。", 23, "serif", False, INK, lw - 262, 1.5)
y += 22
illus_flame(p, lx + 44, y - 8, 1.0)
p.text(lx + 262, y + 26, "法国热搜 · Google Trends", 26, "serif", True, INK)
y = p.para(lx + 262, y + 62, "本周法国区热搜前三:① 2027 总统大选民调 ② GTA VI ③ NBA 马刺对雷霆。学两个词:le sondage = 民意调查;l'élection présidentielle = 总统大选。", 23, "serif", False, INK, lw - 262, 1.5)

# Right column: 本期目录
rx, rw = 662, X1 - 662
ry = 512
ry = p.section_head(rx, ry + 30, "本 期 目 录", 30, rule_to=X1) + 40
toc = [
    ("No.001", "《小王子》", "ce que"),
    ("No.002", "《谈谈方法》", "donc"),
    ("No.003", "《寓言》", "简单将来时"),
    ("No.004", "《基督山伯爵》", "祈使句 · 重阳"),
    ("No.005", "《西西弗神话》", "il faut"),
    ("No.006", "《追忆似水年华》", "复合过去时"),
    ("No.007", "《悲惨世界》", "ne … que · 压轴"),
]
for no, book, gp in toc:
    p.text(rx, ry, no, 22, "sans", True, OLIVE)
    p.text(rx + 96, ry, book, 22, "serif", True, INK)
    p.text(rx + 96, ry + 29, gp, 19, "sans", False, GREY)
    ry += 68
    p.hline(rx, X1, ry - 12, LINE, 1)
    ry += 4
ry += 10
p.rect(rx, ry, rw, 172, fill=BOX, stroke=LINE, sw=1.5)
p.text(rx + 20, ry + 40, "版面导读", 22, "sans", True, OLIVE)
ry2 = p.para(rx + 20, ry + 78, "第二、三版 名句精讲:七句原文逐句拆解,配仿写跟练。第四、五版 练习专版:五大题型,末版附答案。", 22, "serif", False, INK, rw - 40, 1.5)
foot(p, 1)
p.save(f"{OUT}/p1-cover.svg")
print("P1 done")

# ================= Page 2 · 名句精讲(上) =================
p = Page()
y = header_band(p, "第 二 版", "名句精讲 (上)", "SENTENCE STUDY")
days = [
    ("No.001 · 10月15日 周四", "圣-埃克苏佩里《小王子》",
     "« Tu deviens responsable pour toujours de ce que tu as apprivoisé. »",
     "你要永远为自己所驯养的一切负责。",
     "语法聚焦｜ce que =「所……的(东西)」,引导宾语从句;tu as apprivoisé 是复合过去时,「已经驯养了」。",
     "跟练｜用 ce que 造句:我喜欢我读到的东西 → J'aime ce que je lis.", illus_fox),
    ("No.002 · 10月16日 周五", "笛卡尔《谈谈方法》",
     "« Je pense, donc je suis. »",
     "我思,故我在。",
     "语法聚焦｜donc =「因此、所以」,一词点清因果;suis 是动词 être 的第一人称单数变位「我是」。",
     "跟练｜Je lis, donc j'apprends. 我读,故我学。", illus_thinker),
    ("No.003 · 10月17日 周六", "拉封丹《寓言》",
     "« Petit poisson deviendra grand. »",
     "小鱼会长成大鱼。",
     "语法聚焦｜deviendra 是 devenir 的简单将来时第三人称:devenir 的将来时词干是 deviendr-,再加将来时词尾。",
     "跟练｜Un jour, je parlerai français. 总有一天,我会说法语。", illus_fish),
    ("No.004 · 10月18日 周日 · 重阳", "大仲马《基督山伯爵》",
     "« Attendez et espérez ! »",
     "等待,希望吧!",
     "语法聚焦｜祈使句:对 vous 说话时省去主语 vous,直接用动词的 vous 变位下命令、作叮嘱。这是原书结尾伯爵留给世人的话。",
     "跟练｜对朋友说:Écoute et répète ! 听,然后跟读!", illus_island),
]
for label, book, quote, trans, gram, drill, illus in days:
    p.hline(X0, X1, y - 18, LINE, 1)
    p.text(X0, y + 14, label, 23, "sans", True, OLIVE)
    p.text(X1, y + 14, book, 23, "serif", False, GREY, anchor="end")
    illus(p, 858, y + 26, 1.0)
    yq = p.para(X0, y + 66, quote, 31, "serif", True, INK, 780, 1.32)
    yt = p.para(X0, yq + 4, "译文｜" + trans, 25, "serif", False, GREY, 940, 1.4)
    yg = p.para(X0, yt + 6, gram, 24, "serif", False, INK, 940, 1.45)
    yd = p.para(X0, yg + 4, drill, 24, "serif", False, OLIVE, 940, 1.45)
    y = yd + 15
p.hline(X0, X1, y - 18, LINE, 1)
foot(p, 2)
p.save(f"{OUT}/p2-sentences-a.svg")
print("P2 done, end y =", y)
