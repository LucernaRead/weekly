# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-vol3/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 头版 =================
p = BSPage()
p.text(MX, 104, "VOL. 1 · 第一期 · 总第 1 期", 23, "sans", True, OLIVE)
p.text(780, 104, "墨迹书每日一句", 23, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 104, "2026年10月15日 — 10月21日", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 124, GOLD, 1.6)
p.text(780, 252, "The Lucerna", 150, family="UnifrakturMaguntia", anchor="middle")
p.text(780, 322, "法 语 周 报 · 每 日 一 句", 52, "serif", True, INK, anchor="middle")
p.text(780, 362, "LUCERNA FRENCH WEEKLY — READ REAL BOOKS, ONE SENTENCE A DAY", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 388, INK, 3); p.hline(MX, RIGHT, 397, INK, 1.2)

# 时事句 band
p.rect(MX, 420, RIGHT - MX, 128, fill=BOX, stroke=LINE, sw=1.5)
p.text(MX + 28, 468, "本周时事句", 22, "sans", True, BRICK)
p.text(RIGHT - 28, 468, "霜降 · 10月23日(周五) · 秋季最后一个节气", 22, "sans", True, BRICK, anchor="end")
p.text(MX + 28, 518, "« L'automne est le printemps de l'hiver. »", 36, "serif", True, INK)
p.text(RIGHT - 28, 518, "秋天,是冬天的春天。", 27, "serif", False, GREY, anchor="end")
p.text(MX + 28, 540, "传为法国画家图卢兹-洛特雷克语。霜降将至,这句正应景:秋天收尾的地方,藏着春天的开头。", 20, "sans", False, GREY)

# Row 1: feature (span 0-1) + 时事 (col 2)
fy = 592
x, w = span_x(0, 2)
fy = p.shead(x, fy + 30, "头 条 · 本周特稿", w) + 40
fy = p.para(x, fy, "秋天,是读书人的季节", 40, "serif", True, INK, w, 1.2) + 4
fy = p.para(x, fy, "本报编辑部 · 小墨 撰文", 20, "sans", False, GREY, w, 1.3) + 10
fy = p.para(x, fy, "L'automne est la saison des lecteurs. Dehors, les feuilles tombent ; dedans, les pages tournent. En France, la « rentrée littéraire » est le grand rendez-vous des livres : chaque automne, des centaines de romans nouveaux arrivent en librairie. Mais l'automne est aussi la saison des classiques. Quand les soirées deviennent longues, on ouvre Hugo, Camus ou Saint-Exupéry, et l'on lit lentement, une phrase après l'autre. C'est exactement le pari de ce journal : sept phrases par semaine, lues pour de vrai, dans le texte. Petit poisson deviendra grand — et petit lecteur deviendra grand lecteur.", 24, "serif", False, INK, w, 1.52) + 8
fy = p.para(x, fy, "译读｜秋天是读书人的季节。窗外落叶,窗内翻书。法国有「文学开学季」:每到秋天,数百部新小说上市。但秋天同样属于经典——夜变长了,就打开雨果、加缪、圣-埃克苏佩里,一句一句慢慢读。这正是本报的赌注:每周七句,读原文,读真书。", 23, "serif", False, GREY, w, 1.5)
print("P1 feature ends", fy)

cx = COLX[2]
cy = 592
cy = p.shead(cx, cy + 30, "本 周 时 事", CW) + 40
illus_climb(p, cx + 6, cy - 8, 1.25)
cy = p.item(cx + 300, cy + 30, "", "", CW - 300)
p.text(cx + 302, cy + 4, "重阳已至", 27, "serif", True, INK)
cy2 = p.para(cx + 302, cy + 40, "10月18日(周日)", 22, "serif", False, GREY, CW - 302, 1.35)
cy = max(cy2, cy + 158) + 8
cy = p.para(cx, cy, "九九重阳,登高赏菊。本周 No.004 正出自《基督山伯爵》:« Attendez et espérez ! »——等待,希望吧。登高望远的人,心里装的正是这两样东西。", 23, "serif", False, INK, CW, 1.5) + 14
illus_frost(p, cx + 16, cy - 6, 1.5)
p.text(cx + 130, cy + 30, "霜降将至 · 10月23日(周五)", 26, "serif", True, INK)
cy = p.para(cx + 130, cy + 66, "法语里「霜」是 la gelée blanche。", 22, "serif", False, GREY, CW - 130, 1.4) + 6
cy = p.para(cx, cy, "秋季最后一个节气。下周走进深秋:落叶、寒霜,和 11 月 1 日的诸圣节(预告见第五版)。", 23, "serif", False, INK, CW, 1.5)
print("P1 right col ends", cy)

# Row 2: 目录 (span 0-1) + 法国热搜 (col 2)
ry = 1240
x, w = span_x(0, 2)
ry = p.shead(x, ry + 30, "本 期 目 录 · 本周七句", w) + 42
toc = [
    ("No.001", "圣-埃克苏佩里《小王子》", "ce que 所……的"),
    ("No.002", "笛卡尔《谈谈方法》", "donc 因此"),
    ("No.003", "拉封丹《寓言》", "简单将来时"),
    ("No.004", "大仲马《基督山伯爵》", "祈使句 · 重阳"),
    ("No.005", "加缪《西西弗神话》", "il faut 应该"),
    ("No.006", "普鲁斯特《追忆似水年华》", "复合过去时"),
    ("No.007", "雨果《悲惨世界》", "ne … que 只有 · 压轴"),
]
for no, book, gp in toc:
    p.text(x, ry, no, 24, "sans", True, OLIVE)
    p.text(x + 120, ry, book, 24, "serif", True, INK)
    p.text(x + w, ry, gp, 22, "serif", False, GREY, anchor="end")
    ry += 34
    p.hline(x, x + w, ry - 10, LINE, 1)
    ry += 12
print("P1 toc ends", ry)

hy = 1240
hy = p.shead(cx, hy + 30, "法国热搜 · 趋势榜", CW) + 42
illus_flame(p, cx + 2, hy - 30, 1.15)
hy = p.para(cx + 56, hy + 4, "Google Trends 法国区(10月20日截取)", 21, "sans", False, GREY, CW - 56, 1.35) + 16
trends = [
    ("1", "2027 总统大选民调", "5 000+"),
    ("2", "GTA VI", "500+"),
    ("3", "NBA 马刺对雷霆", "200+"),
    ("4", "托尼·帕克", "200+"),
    ("5", "乌克兰局势", "100+"),
]
for rank, t, heat in trends:
    p.text(cx, hy, rank, 24, "sans", True, BRICK)
    p.text(cx + 40, hy, t, 23, "serif", False, INK)
    p.text(cx + CW, hy, heat, 21, "sans", False, GREY, anchor="end")
    hy += 40
hy = p.para(cx, hy + 6, "学两个词:le sondage = 民意调查;l'élection présidentielle = 总统大选。第三版阅读 C 篇,就带你读这件事。", 22, "serif", False, OLIVE, CW, 1.48)
print("P1 trends ends", hy)

# Row 3: 七句速览 strip + 谚语 (row 3, cols 1-2)
sy = 1718
p.hline(MX, RIGHT, sy - 22, INK, 1.6)
sy = p.shead(MX, sy + 28, "七 句 速 览 · 先睹为快", RIGHT - MX) + 38
quotes = [
    "« Tu deviens responsable pour toujours de ce que tu as apprivoisé. »",
    "« Je pense, donc je suis. »",
    "« Petit poisson deviendra grand. »",
    "« Attendez et espérez ! »",
    "« Il faut imaginer Sisyphe heureux. »",
    "« Longtemps, je me suis couché de bonne heure. »",
    "« Il n'y a que de mauvais cultivateurs. »",
]
qx = [MX, MX + 492, MX + 984]
for i, q in enumerate(quotes):
    col = i % 3
    row = i // 3
    p.para(qx[col], sy + row * 74, q, 21, "serif", False, GREY, 452, 1.35)
p.para(qx[1], sy + 2 * 74, "本周谚语｜« Petit à petit, l'oiseau fait son nid. » 一点一点,小鸟筑成巢——和 « Petit poisson deviendra grand » 一个意思:慢慢来,比较快。第二版精讲,第四版做题。", 21, "serif", False, OLIVE, 944, 1.38)
print("P1 bottom ends", sy + 2 * 74 + 62)
p.foot(1)
p.save(f"{OUT}/b1-front.svg")
print("P1 saved")

# ================= P2 · 精讲版 =================
p = BSPage()
y = p.band("第 二 版", "名句精讲 · 词汇 · 语法", "SENTENCE STUDY · WORDS · GRAMMAR")
days = [
    ("No.001 · 周四", "《小王子》",
     "« Tu deviens responsable pour toujours de ce que tu as apprivoisé. »",
     "译｜你要永远为自己所驯养的一切负责。",
     "聚焦｜ce que =「所……的」,引导宾语从句;tu as apprivoisé 是复合过去时。跟练:J'aime ce que je lis. 我喜欢我读到的东西。"),
    ("No.002 · 周五", "《谈谈方法》",
     "« Je pense, donc je suis. »",
     "译｜我思,故我在。",
     "聚焦｜donc =「因此」,一词点清因果;suis 是 être 的「我是」。跟练:Je lis, donc j'apprends."),
    ("No.003 · 周六", "《寓言》",
     "« Petit poisson deviendra grand. »",
     "译｜小鱼会长成大鱼。",
     "聚焦｜deviendra:devenir 的简单将来时,词干 deviendr- + 词尾 -a。跟练:Un jour, je parlerai français."),
    ("No.004 · 周日 · 重阳", "《基督山伯爵》",
     "« Attendez et espérez ! »",
     "译｜等待,希望吧!",
     "聚焦｜祈使句:省去主语 vous,直接用动词下令、叮嘱。原书结尾伯爵留给世人的话。跟练:Écoute et répète !"),
    ("No.005 · 周一", "《西西弗神话》",
     "« Il faut imaginer Sisyphe heureux. »",
     "译｜应该想象西西弗是幸福的。",
     "聚焦｜il faut + 动词原形 =「应该、必须」,无人称句式。跟练:Il faut répéter chaque jour."),
    ("No.006 · 周二", "《追忆似水年华》",
     "« Longtemps, je me suis couché de bonne heure. »",
     "译｜长久以来,我总是早早地睡下。",
     "聚焦｜je me suis couché:自反动词复合过去时,助动词用 être。跟练:Hier, je me suis levé tôt."),
]
col_of = [0, 0, 1, 1, 2, 2]
ys = {0: y + 16, 1: y + 16, 2: y + 16}
for idx, (label, book, quote, trans, gram) in enumerate(days):
    c = col_of[idx]
    x = COLX[c]
    yy = ys[c]
    if idx % 2 == 1:
        p.hline(x, x + CW, yy - 16, LINE, 1)
    p.text(x, yy + 8, label, 22, "sans", True, OLIVE)
    p.text(x + CW, yy + 8, book, 22, "serif", False, GREY, anchor="end")
    yy = p.para(x, yy + 52, quote, 27, "serif", True, INK, CW, 1.3) + 4
    yy = p.para(x, yy, trans, 23, "serif", False, GREY, CW, 1.4) + 3
    yy = p.para(x, yy, gram, 22.5, "serif", False, INK, CW, 1.45)
    ys[c] = yy + 30
print("P2 entry columns end", ys)

# No.007 span
y7 = max(ys.values()) + 6
p.hline(MX, RIGHT, y7 - 14, INK, 1.6)
p.text(MX, y7 + 22, "No.007 · 周三 · 本周压轴", 23, "sans", True, BRICK)
p.text(RIGHT, y7 + 22, "雨果《悲惨世界》", 23, "serif", False, GREY, anchor="end")
illus_sprout(p, RIGHT - 190, y7 + 30, 1.35)
y7 = p.para(MX, y7 + 74, "« Il n'y a ni mauvaises herbes ni mauvais hommes. Il n'y a que de mauvais cultivateurs. »", 29, "serif", True, INK, 1180, 1.32) + 6
x, w = span_x(0, 2)
y7a = p.para(x, y7, "读者问｜后面这个 que 是什么意思?换成 pas 行不行?", 23, "serif", False, INK, w, 1.42) + 2
y7a = p.para(x, y7a, "小墨答｜ne … que 是「只有」:前面全部否定,que 后面留下唯一的例外——只有不会耕种的人。换成 pas 就成了 ne … pas「没有」,意思全反了。为什么?看右栏的语法专题。", 23, "serif", False, INK, w, 1.42)
y7b = p.para(COLX[2], y7 + 48, "读原著｜这句话在《悲惨世界》里说的是教育与成长:没有天生的坏学生,只有不会耕种的人。第三版有雨果小传。", 22, "serif", False, GREY, CW, 1.45)
y7 = max(y7a, y7b) + 20
print("P2 007 ends", y7)

# Bottom: 词汇拓展 (span 0-1) + 语法专题 (col 2)
x, w = span_x(0, 2)
vy = p.shead(x, y7 + 28, "词 汇 拓 展 · 本周二十词", w) + 40
words = [
    ("apprivoiser", "驯养"), ("responsable", "负责的"), ("donc", "因此"), ("devenir", "变成"),
    ("espérer", "希望"), ("heureux", "幸福的"), ("se coucher", "睡下"), ("tôt", "早"),
    ("cultivateur", "耕种者"), ("herbe", "草"), ("feuille", "叶子"), ("saison", "季节"),
    ("lentement", "慢慢地"), ("lecteur", "读者"), ("page", "页"), ("classique", "经典的"),
    ("jardin", "花园"), ("grandir", "长大"), ("patience", "耐心"), ("rêver", "做梦"),
]
cell_w = w // 4
for i, (wf, gl) in enumerate(words):
    cx2 = x + (i % 4) * cell_w
    cy2 = vy + (i // 4) * 84
    p.text(cx2, cy2, wf, 23, "serif", True, INK)
    p.text(cx2, cy2 + 32, gl, 20, "serif", False, GREY)
vy = vy + 5 * 84 + 4
print("P2 vocab ends", vy)

gy = y7
gy = p.shead(COLX[2], gy + 28, "语 法 专 题", CW) + 40
gy = p.para(COLX[2], gy, "简单将来时:词干 = 动词原形(+r),词尾:-ai, -as, -a, -ons, -ez, -ont。不规则词干:être→ser-, avoir→aur-, aller→ir-, devenir→deviendr-。", 22, "serif", False, INK, CW, 1.45) + 8
gy = p.para(COLX[2], gy, "复合过去时用 être 的动词:aller, venir, arriver, partir, entrer, sortir, monter, descendre, naître, mourir, rester, tomber——外加全部自反动词(se lever, se coucher…)。", 22, "serif", False, INK, CW, 1.45) + 8
gy = p.para(COLX[2], gy, "ne … pas 还是 ne … que?pas =「不、没有」:Je ne bois pas d'eau.(我不喝水)que =「只有」:Je ne bois que de l'eau.(我只喝水)注意:pas 后面 de 不带冠词,que 后面照常。", 22, "serif", False, INK, CW, 1.45)
print("P2 grammar ends", gy)

# 易错诊所 strip
ey = max(vy, gy) + 18
p.hline(MX, RIGHT, ey - 8, LINE, 1)
ey = p.shead(MX, ey + 26, "易 错 诊 所", RIGHT - MX) + 36
errs = [
    "✗ Il faut à lire. → ✓ Il faut lire.(faut 后直接跟原形)",
    "✗ J'ai me couché tôt. → ✓ Je me suis couché tôt.(自反动词用 être)",
    "✗ Poisson deviendra grand hier. → ✓ …est devenu grand.(将来时不配 hier)",
]
for i, e in enumerate(errs):
    p.para(MX + i * 492, ey, e, 21.5, "serif", False, INK, 470, 1.42)
print("P2 errors end", ey + 100)

# 生词闪卡 strip
fy2 = ey + 128
p.hline(MX, RIGHT, fy2 - 16, LINE, 1)
fy2 = p.shead(MX, fy2 + 26, "生 词 闪 卡 · 遮住右边,说出中文", RIGHT - MX) + 38
cell = (RIGHT - MX) // 5
for i, (wf, gl) in enumerate(words[:10]):
    xx = MX + (i % 5) * cell
    yy = fy2 + (i // 5) * 78
    p.text(xx, yy, wf, 23, "serif", True, INK)
    p.text(xx, yy + 32, gl, 19, "serif", False, GREY)
print("P2 flash ends", fy2 + 2 * 78)
p.foot(2)
p.save(f"{OUT}/b2-study.svg")
print("P2 saved")
