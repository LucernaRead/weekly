# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-cn-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 头版 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3 · 第 3 号", 23, "sans", True, OLIVE)
p.text(975, 92, "每周读中文 · Lire du vrai chinois, chaque semaine", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "2026年11月9日（周一）— 15日（周日）", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "简体中文版 · VOL.3 · 双11 · 消防日 · S16", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "给学中文的人的周报 — Lire la vraie Chine, en chinois", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)
# pairing badge: which text, which explanation language, which reader
p.text(975, 434, "TEXTES EN CHINOIS SIMPLIFIÉ · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES", 19.5, "sans", True, OLIVE, anchor="middle")

# band
p.rect(MX, 458, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 512, "双11到了,包裹一波一波地来", 36, "sans", True, "#f3edda")
p.text(MX + 30, 556, "11月10日晚上8点高潮场开始,11月11日是双11,周日凌晨3点是S16总决赛。", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 512, "双11×S16", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 556, "La semaine de shopping rencontre la finale · voir pages 2 et 4", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "头条 · À la une", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "双11到了,包裹也要到了", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "11月11日星期三是双11,高潮场从前一天晚上8点开始——先买,再等包裹来", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "Rédaction Lucerna · Niveau de lecture A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("今年的双11,现货从10月12日就开始卖了。京东10月12日晚上8点开始卖现货,淘宝和天猫10月20日晚上8点现货开售,现货一直卖到11月13日。")
f.para("11月10日星期二晚上8点,高潮场开始。11月11日星期三,是双11的正日子。这一天包裹最多,快递也最忙。")
f.para("快递的高峰不是一天,而是三波:10月20日到21日是第一波,10月31日是第二波,11月11日是第三波,也是最大的一波。")
f.para("这一周还有两件大事:11月9日星期一是全国消防日,主题是全民消防、生命至上;11月15日星期日凌晨3点,是S16总决赛。")
f.para("买东西的时候,今年的规则还是更简单:很多商品直接降价,结算页的价格就是实付价。买之前,先看好运费和退换货的规则。")
f.para("这是《Lucerna》简体中文版第3号。每周,我们用简单的中文,带你读真正的中国新闻。欢迎你!")
f.gloss("gāocháochǎng 高潮场 — la grande vente · bāoguǒ 包裹 — un colis · gāofēng 高峰 — un pic, le moment le plus chargé · jiésuàn 结算 — la caisse, le règlement.")
f.box("数字看本周 · Chiffres de la semaine", [
    ("10 nov. 20:00 — grande vente (高潮场)", "serif", False, INK, 20, 1.35),
    ("11 nov. — jour du Double 11, 3e pic de colis", "serif", False, INK, 20, 1.35),
    ("9 nov., lundi — Journée nationale du feu (消防日)", "serif", False, INK, 20, 1.35),
    ("15 nov. 03:00 — finale S16 (Pékin)", "serif", False, INK, 20, 1.35),
])
f.head("即学即练 · Essaie tout de suite", 25)
f.ex("A2", "完成句子", "10", "La grande vente commence le 10 novembre à 20 h 00.",
     "高潮场从11月___日晚上8点开始。", instr="Compléter la phrase", size=19.5, gap=6)
f.ex("A2", "完成句子", "三", "Le pic des colis vient en trois vagues.",
     "快递高峰分___波。", instr="Compléter la phrase", size=19.5, gap=6)
f.ex("A2", "完成句子", "11", "Le jour du Double 11, c'est le 11 novembre.",
     "双11在11月___日。", instr="Compléter la phrase", size=19.5, gap=6)
f.ex("A2", "完成句子", "消防", "Le 9 novembre, c'est la Journée nationale du feu.",
     "11月9日是全国___日。", instr="Compléter la phrase", size=19.5, gap=6)
f.ex("A2", "完成句子", "15", "La finale S16, c'est le 15 novembre, heure de Pékin.",
     "S16总决赛在11月___日凌晨3点。", instr="Compléter la phrase", size=19.5, gap=6)
f.ex("A2", "完成句子", "13", "La vente en stock dure jusqu'au 13 novembre.",
     "现货一直卖到11月___日。", instr="Compléter la phrase", size=19.5, gap=6)
f.end_report()

# ---- this-week calendar box (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "本周日历 · Cette semaine", 25, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "11月9日—15日 · 9–15 nov.", 22, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Ce qui se passe cette semaine", 19, "sans", False, GREY)
topics = [
    "周一 11月9日 — 全国消防日,消防宣传月",
    "周二 11月10日 20:00 — 双11高潮场开始",
    "周三 11月11日 — 双11正日子,包裹高峰",
    "周五 11月13日 — 老电影《海上钢琴师》重映",
    "周日 11月15日 03:00 — S16总决赛",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 10
p.para(gx + 22, byy + 12, "Quarts de finale du 4 au 7 nov. et demi-finales du 8 au 9 nov., toujours à 06:00 heure de Pékin. Au bouclage (2 nov.), les finalistes ne sont pas encore connus. La finale, c'est le 15 nov. à 03:00 heure de Pékin.", 18.5, "sans", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 636, "Toutes les heures, heure de Pékin", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "Bouclage : 2 nov. — résultats à venir", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "本期目录 · Sommaire", 24, "sans", True, OLIVE)
som = [
    ("2版", "双11那一周:买、等、收包裹", "A2"),
    ("3版", "消防日:先学会保护自己", "A2→B1"),
    ("4版", "S16:瑞士轮打完,八强出炉", "B1"),
    ("5版", "老电影重映与读书月", "B1"),
    ("6版", "包裹深读:高峰为什么分三波", "B2"),
    ("7版", "词语精讲", "A2→B2"),
    ("8版", "测验与答案", "全部"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

# ---- word of the week (col 3) ----
my = 1636
p.text(gx, my + 24, "本周词 · Mot de la semaine", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
p.para(gx, my + 76, "「包裹」 bāoguǒ — un colis. Ce qu'on achète au Double 11 est mis dans un colis et livré jusqu'à toi. Exemple : 「我的包裹到了,去快递柜拿。」", 21.5, "serif", False, INK, gw, 1.4)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "locker.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "快递柜(资料图)。包裹到了,先看取件码,再去快递柜拿。",
        "Photo: Map hobby — CC0 (Wikimedia Commons)")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-week")
f2.head("忙碌的一周", 25)
f2.para("这一周又买东西,又看比赛:周一消防日,周三双11,周日凌晨还有总决赛。先看好日历,再安排时间吧。", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "快讯 · Brèves", 24, "sans", True, OLIVE)
brefs = [
    ("消防日", "11月9日是第35个全国消防日,11月是消防宣传月。(第 3 版)"),
    ("S16", "瑞士轮打完,三支中国队进了八强,四分之一决赛11月4日开始。(第 4 版)"),
    ("电影", "《海上钢琴师》4K修复版11月13日重映。(第 5 版)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "闪电问答 · Quiz éclair", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lis la page 1 et choisis · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "单选", "A", "La grande vente commence le 10 novembre à 20 h 00.",
      "高潮场从哪天晚上8点开始? A. 11月10日 · B. 11月11日 · C. 10月20日", size=21)
qf.ex("A2", "单选", "B", "Le 9 novembre, c'est la Journée nationale du feu.",
      "全国消防日在11月几日? A. 11月7日 · B. 11月9日 · C. 11月11日", size=21)
qf.ex("A2", "单选", "C", "Le pic des colis vient en trois vagues.",
      "快递高峰分几波? A. 一波 · B. 两波 · C. 三波", size=21)
qf.ex("A2", "单选", "A", "La finale S16, c'est à 03:00 heure de Pékin, le 15 novembre.",
      "S16总决赛在北京时间几点? A. 凌晨3点 · B. 早上6点 · C. 晚上8点", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-touiban.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 生活 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("生活 · La vie", "Lucerna", "Level A2 · 双11那一周 · 天冷了 · Semaine de shopping et jours plus froids")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("双11那一周:买、等、收包裹", 37)
f.byline("Rédaction Lucerna · Niveau de lecture A2")
f.para("双11不是一天,是一段时间。现货从10月开始卖,11月10日晚上8点高潮场开始,11月11日是正日子,现货一直卖到11月13日。")
f.para("今年的玩法和去年差不多:很多商品还是现货,还是直接降价。买之前,先看结算页,再决定买不买。结算页的价格,才是真正要付的钱。")
f.para("买完以后,就要等包裹了。包裹不会一天都到:第一波在10月20日到21日,第二波在10月31日,第三波在11月11日。每一波以后,快递员都最忙。")
f.para("包裹到了,手机会收到取件码。去快递柜拿的时候,先看好取件码,再开柜门。东西拿回家,先打开看一看:对不对?有没有坏?有问题,早点联系卖家。")
f.para("这一周,天气也冷了。11月4日到7日,又有冷空气来,很多地方的气温会创今年下半年的新低。出门以前,先看天气预报,加一件厚衣服。北方很多地方已经开始供暖,家里暖和了。")
f.gloss("qǔjiànmǎ 取件码 — un code de retrait pour colis · kuàidìguì 快递柜 — un casier à colis · mài jiā 卖家 — un vendeur · gōngnuǎn 供暖 — le chauffage central.")
f.head("冷空气来了,怎么穿", 25)
f.para("Les prévisions disent : l'air froid arrive du 4 au 7 novembre, et beaucoup d'endroits connaîtront leurs températures les plus basses de la seconde moitié de l'année. Au nord, Harbin pourrait passer sous zéro en journée ; au sud, des villes comme Wuhan et Hefei pourraient rester sous 15 degrés le 8 novembre. Habille-toi selon l'endroit où tu vis — une seule règle ne convient pas à tout le pays.")
f.box("Exemple d'entraînement · 练习例子", [
    ("一件毛衣 260 元,一条围巾 90 元,一起 350 元。", "serif", False, INK, 20, 1.35),
    ("直降 60 元,实付 290 元。结算页的价格就是实付价。", "serif", False, INK, 20, 1.35),
])
f.head("天冷了,吃什么好", 25)
f.para("立冬已经过了,冬天真的来了。天冷的时候,吃点热的,喝点热的,身体暖和。北方吃饺子、喝羊肉汤,南方吃汤圆、喝热汤,都是冬天里的热饭。")
f.para("11月上旬,有的学校还在期中考试,日子各不相同。天冷加考试,更要早点睡觉,别熬夜。")
f.gloss("yángròutāng 羊肉汤 — soupe de mouton · rètāng 热汤 — soupe chaude · áoyè 熬夜 — veiller tard.")
f.box("本周生活小日历 · Dates clés", [
    ("周一 11月9日 — 全国消防日", "serif", False, INK, 20, 1.35),
    ("周二 11月10日 20:00 — 双11高潮场开始", "serif", False, INK, 20, 1.35),
    ("周三 11月11日 — 双11正日子,包裹高峰", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: valley image + facts + 你呢 (sequential, measured)
ix = COLX[3]
image(p, "valley.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "秋天的山谷,红叶正当时。天冷了,山里的叶子也要落了。",
              "Photo: Paul Gilmore — CC0 (Wikimedia Commons)")
facts = ["高潮场 11 月 10 日 20:00 开始。",
         "双11正日子在 11 月 11 日星期三。",
         "现货期到 11 月 13 日。",
         "冷空气 11 月 4 日到 7 日来。"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "你知道吗 · Le savais-tu ?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "你呢?这个双11,你买了什么?你的包裹到了吗?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Et toi ? Qu'as-tu acheté pour ce 双11 ? Ton colis est-il arrivé ? Écris deux phrases en chinois.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · Et toi ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Et toi ? Qu'as-tu acheté pour ce 双11 ? Ton colis est-il arrivé ? Écris deux phrases en chinois.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- word strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "双11词语卡 · Mots du shopping", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Quatre mots que tu verras dans chaque appli de shopping", 20, "sans", False, GREY, anchor="end")
words = [
    ("高潮场", "gāocháochǎng · la grande vente", "heures de pointe, dès le 10 nov. 20:00"),
    ("包裹", "bāoguǒ · un colis", "ce que tu attends après ta commande"),
    ("取件码", "qǔjiànmǎ · un code de retrait", "le code qui ouvre le casier"),
    ("供暖", "gōngnuǎn · le chauffage central", "le chauffage commence dans le nord"),
]
for i, (t, lab, en) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, en, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 222, "Retiens la phrase : 「包裹到了,先看取件码,再去快递柜拿。」", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Exercices", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · 读一读选一选 · Lire et choisir", 25)
e.glossline("Lis la page 2 et choisis la meilleure réponse.")
e.ex("A2", "单选", "A", "La grande vente commence le 10 novembre à 20 h 00.",
     "高潮场从哪天晚上8点开始? A. 11月10日 · B. 11月11日 · C. 11月13日", size=19, gap=6)
e.ex("A2", "单选", "B", "La vente en stock dure jusqu'au 13 novembre.",
     "现货一直卖到哪天? A. 11月11日 · B. 11月13日 · C. 10月20日", size=19, gap=6)
e.ex("A2", "单选", "A", "Le troisième pic de colis, c'est le 11 novembre.",
     "第三波包裹高峰在哪天? A. 11月11日 · B. 10月31日 · C. 10月20日", size=19, gap=6)
e.ex("A2", "单选", "A", "L'air froid arrive du 4 au 7 novembre.",
     "冷空气哪几天来? A. 11月4日到7日 · B. 11月9日到11日 · C. 11月13日到15日", size=19, gap=6)
e.ex("A2", "单选", "B", "Vérifie le code de retrait avant d'ouvrir le casier.",
     "去快递柜拿包裹,先看什么? A. 天气预报 · B. 取件码 · C. 电影票", size=19, gap=6)
e.head("B · 词语填空 · Mots à trous", 25)
e.glossline("Remplis chaque blanc avec le bon mot.")
e.ex("A2", "完成句子", "包裹", "bāoguǒ — un colis.",
     "买的东西装在___里,送到你手里。", instr="Compléter", size=19, gap=6)
e.ex("A2", "完成句子", "取件码", "qǔjiànmǎ — le code qui ouvre le casier.",
     "去快递柜拿包裹,先看___。", instr="Compléter", size=19, gap=6)
e.ex("A2", "完成句子", "供暖", "gōngnuǎn — le chauffage commence dans le nord.",
     "北方很多地方已经开始___了。", instr="Compléter", size=19, gap=6)
e.ex("A2", "完成句子", "高潮场", "gāocháochǎng — la grande vente.",
     "11月10日晚上8点,___开始了。", instr="Compléter", size=19, gap=6)
e.ex("B1", "完成句子", "卖家", "màijiā — un vendeur ; le contacter en cas de problème.",
     "东西有问题,早点联系___。", instr="Compléter", size=19, gap=6)
e.head("C · 数字与日期 · Nombres", 25)
e.glossline("Utilise l'exemple d'entraînement de cette page.")
e.ex("A2", "完成句子", "260", "Le pull coûte 260 yuans dans l'exemple.",
     "练习例子里,毛衣___元。", instr="Compléter", size=19, gap=6)
e.ex("A2", "完成句子", "350", "260 + 90 = 350 yuans ensemble.",
     "毛衣和围巾一起___元。", instr="Compléter", size=19, gap=6)
e.ex("B1", "完成句子", "290", "350 − 60 = 290 yuans après la remise directe.",
     "直降以后实付___元。", instr="Compléter", size=19, gap=6)
e.ex("B1", "完成句子", "60", "La remise directe dans l'exemple est de 60 yuans.",
     "练习例子里直降___元。", instr="Compléter", size=19, gap=6)
e.head("D · 词语配对 · Appariement", 25)
e.match_set("A2", "词汇配对",
            ["高潮场", "包裹", "取件码", "供暖"],
            ["北方冬天家里暖和,靠它",
             "打开快递柜要用的号码",
             "买的东西,装在里面送来",
             "双11最忙的卖货时间"],
            ["d", "c", "b", "a"],
            ["高潮场 = la grande vente, d", "包裹 = un colis, c", "取件码 = un code de retrait, b", "供暖 = le chauffage central, a"],
            instr="Associe les mots")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-shenghuo.svg")
print("P2 saved, exercises so far:", len(REG))
