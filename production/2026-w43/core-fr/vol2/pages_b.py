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

# ================= Page 3 · 名句精讲(下)+词汇 =================
p = Page()
y = header_band(p, "第 三 版", "名句精讲 (下) · 词汇小站", "SENTENCE STUDY & WORDS")
days = [
    ("No.005 · 10月19日 周一", "加缪《西西弗神话》",
     "« Il faut imaginer Sisyphe heureux. »",
     "应该想象西西弗是幸福的。",
     "语法聚焦｜il faut + 动词原形 =「应该、必须」,法语最常用的无人称句式:Il faut lire. 必须阅读。",
     "跟练｜Il faut répéter chaque jour. 必须每天重复。", illus_sisyphus),
    ("No.006 · 10月20日 周二", "普鲁斯特《追忆似水年华》",
     "« Longtemps, je me suis couché de bonne heure. »",
     "长久以来,我总是早早地睡下。",
     "语法聚焦｜je me suis couché 是复合过去时:自反动词 se coucher 的助动词要用 être;bonne heure 在这里指「早」。",
     "跟练｜Hier, je me suis levé tôt. 昨天我起得很早。", illus_moon),
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
    y = yd + 14

# No.007 special with dialogue
p.hline(X0, X1, y - 18, LINE, 1)
p.text(X0, y + 14, "No.007 · 10月21日 周三 · 本周压轴", 23, "sans", True, BRICK)
p.text(X1, y + 14, "雨果《悲惨世界》", 23, "serif", False, GREY, anchor="end")
illus_sprout(p, 880, y + 26, 1.0)
yq = p.para(X0, y + 66, "« Il n'y a ni mauvaises herbes ni mauvais hommes. Il n'y a que de mauvais cultivateurs. »", 30, "serif", True, INK, 800, 1.32)
p.text(X0, yq + 8, "读者问", 20, "sans", True, GREY)
yq = p.para(X0 + 86, yq + 10, "后面这个 que 是什么意思?换成 pas 行不行?", 24, "serif", False, INK, 850, 1.4)
p.text(X0, yq + 6, "小墨答", 20, "sans", True, OLIVE)
yq = p.para(X0 + 86, yq + 8, "ne … que 是「只有」:前面全部否定,que 后面留下唯一的例外——只有不会耕种的人。换成 pas 就成了 ne … pas「没有」,雨果的意思全反了。练习在第四版。", 24, "serif", False, INK, 850, 1.42)
y = yq + 8

# 词汇小站
y = p.section_head(X0, y + 16, "词 汇 小 站 · 本周十词", 28) + 30
words = [
    ("apprivoiser", "v. 驯养;使亲近"), ("responsable", "adj. 负责的"),
    ("donc", "conj. 因此,所以"), ("devenir", "v. 变成,成为"),
    ("espérer", "v. 希望,期待"), ("heureux", "adj. 幸福的"),
    ("se coucher", "v.pr. 睡下,就寝"), ("tôt", "adv. 早"),
    ("cultivateur", "n.m. 耕种者"), ("herbe", "n.f. 草,野草"),
]
col_w = 476
for i, (wfr, gloss) in enumerate(words):
    cx = X0 + (i % 2) * col_w
    cy = y + (i // 2) * 47
    p.text(cx, cy, wfr, 26, "serif", True, INK)
    p.text(cx + 218, cy, gloss, 23, "serif", False, GREY)
y = y + 5 * 47 + 4
foot(p, 3)
p.save(f"{OUT}/p3-sentences-b.svg")
print("P3 done, end y =", y)

# ================= Page 4 · 练习专版(上) =================
p = Page()
y = header_band(p, "第 四 版", "练习专版 (上)", "EXERCISES I")
y = p.section_head(X0, y + 26, "一、单项选择 (每题只有一个正确答案)", 28) + 40
qs = [
    ("1. Tu deviens responsable de ce ___ tu as apprivoisé.", "A. qui    B. que    C. dont    D. quoi"),
    ("2. Petit poisson ___ grand un jour.", "A. deviendra    B. devient    C. devenait    D. devenu"),
    ("3. — ___ et espérez ! dit le comte.", "A. Attend    B. Attends    C. Attendez    D. Attendre"),
    ("4. Il faut ___ de bonne heure.", "A. se coucher    B. se couche    C. couché    D. couchant"),
    ("5. Hier, je me ___ couché très tôt.", "A. ai    B. suis    C. es    D. a"),
    ("6. Je ne lis ___ des romans français.", "A. pas    B. que    C. rien    D. plus"),
    ("7. Je pense, ___ je suis.", "A. parce que    B. mais    C. donc    D. alors"),
    ("8. Il n'y a ni thé ___ café.", "A. ou    B. et    C. ni    D. non"),
]
col_w = 476
for i, (q, opts) in enumerate(qs):
    cx = X0 + (i % 2) * col_w
    cy = y + (i // 2) * 106
    qy = p.para(cx, cy, q, 24, "serif", False, INK, col_w - 24, 1.35)
    p.para(cx, qy + 2, opts, 23, "serif", False, GREY, col_w - 24, 1.3)
y = y + 4 * 106 + 6

y = p.section_head(X0, y + 4, "二、完形填空 (用本周语法补全短文)", 28) + 38
y = p.para(X0, y, "L'automne est arrivé. Les feuilles (1)___ jaunes et rouges. Le matin, il faut (2)___ un manteau chaud. Mon grand-père dit toujours : « Petit poisson (3)___ grand. » Alors je ne m'inquiète (4)___ : je lis un peu de français chaque jour, et le soir, je (5)___ couche de bonne heure en rêvant en français.", 25, "serif", False, INK, W, 1.5)
y += 6
opts = [
    "1. A. devient   B. deviennent   C. deviendra   D. devenu",
    "2. A. mettre   B. mets   C. mis   D. mettant",
    "3. A. devient   B. deviendra   C. devenait   D. deviendrez",
    "4. A. pas   B. que   C. rien   D. jamais",
    "5. A. me   B. te   C. se   D. nous",
]
for o in opts:
    y = p.para(X0, y, o, 23, "serif", False, GREY, W, 1.35) + 2
y += 8
y = p.section_head(X0, y + 4, "三、翻译句子 (用上本周句型)", 28) + 38
trs = [
    "1. 我只喝水。(ne … que)",
    "2. 他应该早睡。(il faut …)",
    "3. 没有坏草,只有不会耕种的人。(Il n'y a …)",
]
for t in trs:
    p.text(X0, y, t, 25, "serif", False, INK)
    p.hline(X0 + 30, X1 - 30, y + 30, LINE, 1.2)
    y += 66
foot(p, 4)
p.save(f"{OUT}/p4-exercises-a.svg")
print("P4 done, end y =", y)

# ================= Page 5 · 练习专版(下)+答案 =================
p = Page()
y = header_band(p, "第 五 版", "练习专版 (下) · 参考答案", "EXERCISES II & KEY")
y = p.section_head(X0, y + 26, "四、阅读理解 (先读短文,再答问题)", 28) + 34
y = p.para(X0, y, "La fête du Double Neuf", 28, "serif", True, INK, 700, 1.3) + 2
y = p.para(X0, y, "Le 18 octobre, la Chine a célébré la fête du Double Neuf (Chongyang). Ce jour-là, on monte sur les hauteurs, on admire les chrysanthèmes et on pense aux personnes âgées. En France, il n'y a pas de fête des grands-parents en automne ; mais le 1er novembre, pour la Toussaint, les familles déposent aussi des chrysanthèmes sur les tombes. Deux pays, deux traditions, mais la même fleur et la même idée : ne pas oublier ceux qui nous ont fait grandir.", 25, "serif", False, INK, W, 1.45)
y += 4
rqs = [
    "1. Quand a-t-on célébré la fête du Double Neuf cette année ?",
    "2. Que fait-on ce jour-là ? (donne deux actions)",
    "3. Quelle fête française est mentionnée dans le texte ?",
    "4. Quel est le point commun entre les deux traditions ?",
]
for q in rqs:
    y = p.para(X0, y, q, 24, "serif", False, INK, W, 1.35)
    p.hline(X0 + 30, X1 - 30, y + 4, LINE, 1.2)
    y += 34
y += 2
y = p.section_head(X0, y + 4, "五、写作一角 · Mon automne", 28) + 36
y = p.para(X0, y, "写 4–5 句法语,描述你的秋天:天气、落叶、你在读的书、你的希望。可用下面的开头:", 24, "serif", False, INK, W, 1.4)
y = p.para(X0, y, "En automne, … / Je lis … / Il faut … / J'espère …", 24, "serif", True, OLIVE, W, 1.4)
for i in range(1):
    p.hline(X0 + 30, X1 - 30, y + 20, LINE, 1.2)
    y += 48
y += 6
y = p.section_head(X0, y + 4, "参 考 答 案", 28, BRICK) + 32
y = p.para(X0, y, "单选:1 B  2 A  3 C  4 A  5 B  6 B  7 C  8 C。完形:1 B  2 A  3 B  4 A  5 A。阅读:1. Le 18 octobre. 2. On monte sur les hauteurs et on admire les chrysanthèmes. 3. La Toussaint. 4. Les chrysanthèmes et le souvenir des aînés. 翻译参考:1. Je ne bois que de l'eau. 2. Il faut se coucher de bonne heure. 3. Il n'y a pas de mauvaises herbes, il n'y a que de mauvais cultivateurs.", 20, "serif", False, GREY, W, 1.42)
y += 8
p.rect(X0, y, W, 118, fill=DARK)
p.text(X0 + 26, y + 42, "下周预告 · VOL.2「深秋与节日」", 25, "sans", True, "#f3edda")
p.para(X0 + 26, y + 76, "霜降(10月23日)开篇;11月1日诸圣节 la Toussaint:法国人为何在这一天献菊花?下周揭晓。", 21, "serif", False, "#e8dfc8", W - 52, 1.4)
foot(p, 5)
p.save(f"{OUT}/p5-exercises-b.svg")
print("P5 done, end y =", y)
