# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语　Point de langue", "Lucerna", "语言聚焦　三个级别，三个主题　Trois niveaux, trois sujets")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　决赛与包裹　Finale et colis", 24)
a.para("Mots de la semaine : 决赛 (juésài, la finale), 冠军 (guànjūn, le champion), 半决赛 (bànjuésài, la demi-finale), 到货 (dàohuò, arrivé), 退换货 (tuìhuànhuò, retours et échanges), 价保 (jiàbǎo, protection du prix).", 21.5)
a.glossline("Les classificateurs comptent toujours : 一个包裹 (un colis), 一部电影 (un film), 一场演练 (un exercice).")
a.ex("A2", "完成句子", "个", "包裹 prend le classificateur 个 gè.",
     "我拿了___包裹。", instr="Compléter", size=20, gap=10)
a.ex("A2", "单选", "A", "决赛 veut dire la finale, le dernier match.",
     "「决赛」是什么意思？ A. 最后一场比赛 · B. 第一场比赛 · C. 练习赛", size=20, gap=10)
a.ex("A2", "完成句子", "决赛", "juésài — la finale ; BLG contre GEN le 15 nov.",
     "11月15日凌晨3点，BLG和GEN打___。", instr="Compléter", size=20, gap=10)
a.ex("A2", "单选", "A", "Les colis prennent 个 — pas 只 ni 条.",
     "哪个说法对？ A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20, gap=10)
a.para("Encore un à pratiquer : 「我的包裹到了吗？」 (Mon colis est-il arrivé ?) Quand tu attends un colis, demande d'abord, puis va à la consigne.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　时间与日期　Heure et dates", 24)
b.para("En chinois, les heures vont du grand au petit : année, mois, jour, jour de semaine, moment de la journée, heure. Exemples de ce numéro : 「11月15日星期日凌晨3点」 (dim. 15 nov., 3 h du matin), 「11月22日星期日」 (dim. 22 nov.), 「11月21日星期六」 (sam. 21 nov.). La plus grande unité d'abord, rien dans le désordre.", 21.5)
b.glossline("Ainsi « Sunday, Nov 22 » en anglais devient 11月22日星期日.")
b.ex("B1", "单选", "B", "凌晨 língchén — les petites heures après minuit.",
     "「凌晨3点」是什么时候？ A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20, gap=10)
b.ex("B1", "完成句子", "早上", "06:00, c'est 早上 — pas le soir.",
     "半决赛在北京时间11月8日___6点开始。（不是晚上）", instr="Compléter", size=20, gap=10)
b.ex("B1", "单选", "A", "Ordre du grand au petit : 22 nov., dimanche.",
     "哪个顺序对？ A. 11月22日星期日 · B. 星期日11月22日 · C. 星期日小雪11月22日", size=20, gap=10)
b.ex("B1", "完成句子", "周日", "Le 22 nov. est un dimanche — 周日.",
     "11月22日是星期日，也可以说___。小雪在这天。", instr="Compléter", size=20, gap=10)
b.para("Deux mots de plus : 凌晨 (língchén), ce sont les petites heures après minuit, avant l'aube ; 傍晚 (bàngwǎn), c'est le court moment juste avant la nuit.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　读新闻　Lire les infos", 24)
c.para("Quand une histoire contient une affirmation (说法), sépare trois sortes de phrases : les affirmations (说法), les données (数据) et les prévisions (预报). La page 6 est l'exemple : « 没有爆掉 » est une affirmation sur les colis de cette année, le total 139.38亿件 est une donnée rapportée — déjà comptée, pas une supposition — et « 第三波是最高峰 » est une prévision de 中通云仓 : attendue, pas encore comptée.", 21.5)
c.glossline("Pour chaque chiffre, demande : à qui est ce chiffre, et quand a-t-il été mesuré ?")
c.ex("B2", "单选", "A", "« 139.38亿件 » : chiffre définitif de la poste, déjà compté.",
     "「139.38亿件」在第6版里是什么？ A. 已经数完的事实 · B. 邮政局的预计 · C. 广告词", size=20, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — des chiffres mesurés, pas des affirmations.",
     "买东西以前，先看___，再看广告。", instr="Compléter", size=20, gap=10)
c.ex("B2", "单选", "B", "Données et caisse d'abord, titre en dernier.",
     "读新闻时，哪个做法最好？ A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — une prévision est prédite, pas encore un fait.",
     "「第三波是最高峰」是___，还没发生。", instr="Compléter", size=20, gap=10)
c.para("Essaie toi-même : dans l'encadré calendrier de la page 1, « 11月22日 » est une date — une donnée. Les mots d'une publicité sont des affirmations. Peux-tu les distinguer ?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters + image ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) indique comment une action est faite."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) relie verbe + degré : 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "Ordre : nombre + classificateur + nom."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日，星期日凌晨3点。」", "Les heures vont du grand au petit : le jour de la semaine en dernier."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所　Clinique des erreurs", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看预报，再决定穿什么。」La structure 先…再… donne l'ordre des actions."
wcn = "Cadre : 先 … 再 … — d'abord X, puis Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式　Structure de phrase", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好！我住在上海。11月9日半决赛，我看了BLG打T1，3比1，真好看！双11我买了一件外套，包裹两天就到了。你们呢？」"
lcn = "编辑部示例信，不是真实来信。VOL.3曾预告本期刊登真实来信和最佳作文；截至11月10日截稿，仍未收到，继续征集。延期不是取消。Note de la rédaction : VOL.3 avait promis de vraies lettres dans VOL.4 ; aucune n'est arrivée au 10 nov. Reporté, pas annulé."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地　Coin des lecteurs", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- P7 image (brush) below the letters box ----
iy7 = col3_end + 12
image(p, "brush.jpg", bx, iy7, CW, 130)
cy7 = caption(p, bx, iy7 + 130, CW, "毛笔（资料图）。写中文，先从一笔一画开始。",
              "Photo : Mx. Granger — CC0 (Wikimedia Commons)")
img_end = cy7
print("P7 image ends", img_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, img_end + 44)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "本周金句　Phrases de la semaine (mot pour mot, tirées des articles de ce numéro)", 27, "sans", True, OLIVE)
quotes = [
    ("「决赛对阵GEN」", "La finale : BLG contre GEN.", "p. 1"),
    ("「包裹都到了吗」", "Tous les colis sont-ils arrivés ?", "p. 2"),
    ("「小雪气寒而将雪矣」", "Petite Neige : l'air se refroidit, la neige arrive.", "p. 3"),
    ("「两支中国队进了四强」", "Deux équipes chinoises ont atteint les demi-finales.", "p. 4"),
    ("「先看简介，再决定」", "Lis d'abord le résumé, puis décide.", "p. 5"),
    ("「无高峰，全高峰」", "Pas un seul pic — chaque jour est un pic.", "p. 6"),
    ("「先打开看一看，再确认收货」", "Ouvre et vérifie d'abord, puis confirme la réception.", "p. 6"),
    ("「悦读深圳」", "Lire avec joie à Shenzhen — le thème du Mois de la lecture de Shenzhen.", "p. 3"),
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
p.text(MX + 28, py + 44, "下期预告　La semaine prochaine (VOL.5)", 24, "sans", True, GOOSE)
p.para(MX + 28, py + 84, "S16总决赛打完了，谁是冠军？小雪之后，冬天怎么过？还有你们的来信和第8版最佳作文。下周见！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
