# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Focus langue", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Trois niveaux, trois sujets")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与冬天 · Shopping", 24)
a.para("Les mots du shopping de cette semaine : 现货 (xiànhuò, en stock), 直降 (zhíjiàng, une baisse directe), 立减 (lìjiǎn, déduit à la caisse), 结算页 (jiésuàn yè, la page de caisse). Les mots de l'hiver : 立冬 (lìdōng, début de l'hiver), 补冬 (bǔdōng, bien manger avant l'hiver), 厚衣服 (hòu yīfu, vêtements chauds).", 21.5)
a.glossline("Les classificateurs comptent toujours : 一件毛衣 (un pull), 一条围巾 (une écharpe), 一部电影 (un film).")
a.ex("A2", "完成句子", "件", "máoyī prend le classificateur jiàn.",
     "我想买一___毛衣。", instr="Complétez", size=20.5, gap=10)
a.ex("A2", "单选", "A", "zhíjiàng veut dire que le prix lui-même baisse.",
     "「直降」是什么意思? A. 价格直接变低 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "立冬", "lìdōng — début de l'hiver, 7 novembre.",
     "11月7日是___。", instr="Complétez", size=20.5, gap=10)
a.ex("A2", "单选", "A", "Les vêtements prennent jiàn, pas gè ni tiáo.",
     "哪个说法对? A. 一件毛衣 · B. 一个毛衣 · C. 一条毛衣", size=20.5, gap=10)
a.para("Encore un à pratiquer : 「这件毛衣多少钱?」 (Combien coûte ce pull ?) Quand vous achetez, demandez d'abord le prix, puis payez.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Heures et dates", 24)
b.para("Le chinois donne les heures du grand au petit : année, mois, jour, jour de semaine, moment de la journée, heure. Exemples de ce numéro : 「11月7日星期六17点52分」 (sam. 7 nov., 17 h 52), 「11月10日星期二20点」 (mar. 10 nov., 20 h), 「11月15日凌晨3点」 (15 nov., 3 h du matin). La plus grande unité d'abord, rien dans le désordre.", 21.5)
b.glossline("Ainsi, le français « samedi soir, 7 novembre » devient 11月7日星期六晚上.")
b.ex("B1", "单选", "B", "língchén — les petites heures après minuit.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "06 h 00 correspond à zǎoshang et non au soir.",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="Complétez", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Ordre du grand au petit : 7 nov., samedi, 17 h 52.",
     "哪个顺序对? A. 11月7日星期六17点52分 · B. 17点52分星期六11月7日 · C. 星期六17点52分11月7日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周六", "Le 7 novembre est un samedi — zhōuliù.",
     "11月7日是星期六,也可以说___。立冬在这天。", instr="Complétez", size=20.5, gap=10)
b.para("Deux mots de plus : 凌晨 (língchén), ce sont les petites heures après minuit, avant l'aube ; 傍晚 (bàngwǎn), c'est le court moment juste avant la nuit.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Lire les infos", 24)
c.para("Quand un article comporte une affirmation (说法), séparez trois sortes de phrases : les affirmations (说法), les données (数据) et les publicités (广告). La page 6 en est l'exemple : 「最低价」 est une affirmation, les 270元 des paniers d'entraînement sont des données d'entraînement, et la page de caisse montre ce que vous payez vraiment.", 21.5)
c.glossline("Pour chaque prix, demandez-vous : ce nombre vient de qui, et où est-il écrit ?")
c.ex("B2", "单选", "C", "« zuìdījià » : affirmation publicitaire, pas donnée mesurée.",
     "「最低价」在第6版里是什么? A. 数据 · B. 声明 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — des nombres mesurés, pas des affirmations.",
     "买东西以前,先看___,再看广告。", instr="Complétez", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Données et page de caisse d'abord, titre en dernier.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "结算", "jiésuàn — la page de caisse montre le vrai prix.",
     "真正要付的钱,看___页的价格。", instr="Complétez", size=20.5, gap=10)
c.para("Essayez vous-même : dans le calendrier de la page 1, 「11月7日」 est une date — une donnée. Les mots d'une publicité sont des affirmations. Saurez-vous les distinguer ?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de) indique comment se fait une action."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de) relie verbe + degré : 跑得快."),
    ("「我买了三只毛衣个」", "→ 「我买了三件毛衣。」", "Nombre + classificateur + nom. Le 个 est en trop."),
    ("「立冬在星期六十一月七日」", "→ 「立冬在11月7日,星期六。」", "Du grand au petit, le jour de semaine en dernier."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所 · Clinique des erreurs", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看评价,再下单。」(Vérifiez les avis, puis commandez.) La structure 先…再… donne l'ordre des actions."
wcn = "Structure : 先 … 再 … — d'abord X, puis Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Structure de phrase", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在上海。立冬那天,我吃了饺子,也给妈妈打了电话。双11,我买了一件毛衣,现货第二天就到了。」"
lcn = "编辑部示例信,不是真实来信。编辑部说明:VOL.1曾预告本期(VOL.2)刊登真实读者来信和VOL.1第8版最佳作文;至今没有收到真实来信,也没有可刊登的投稿,所以本期仍刊登编辑部示例,并继续征集。延期不是取消。Note de la rédaction : le VOL.1 avait promis de vraies lettres et la meilleure rédaction du VOL.1. Aucune n'est arrivée : voici encore un exemple de la rédaction. Reporté, pas annulé. Écrivez-nous ! Envoyez votre lettre en chinois."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
# NOTE: the disclosure above mixes Chinese and English in one string; the
# sans wrap measures CJK and Latin with the same SC face, so the height
# formula above (sans, 20pt) matches the render path. Verified in the build log.
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · Courrier des lecteurs", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · Phrases de la semaine (verbatim, tirées des articles de ce numéro)", 27, "sans", True, OLIVE)
quotes = [
    ("「不用等11月11日」", "Pas besoin d'attendre le 11 novembre.", "p. 1"),
    ("「下单就能发货」", "Commandez et c'est expédié.", "p. 2"),
    ("「先看结算页,再付款」", "Vérifiez la page de caisse, puis payez.", "p. 2"),
    ("「水开始结冰」", "L'eau commence à geler.", "p. 3"),
    ("「三场都输了」", "Les trois séries perdues.", "p. 4"),
    ("「小局一场没赢」", "Pas une seule manche gagnée.", "p. 4"),
    ("「故事够不够好」", "Mais l'histoire est-elle assez bonne ?", "p. 5"),
    ("「别以后,就现在」", "Pas plus tard — maintenant.", "p. 5"),
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
p.text(MX + 28, py + 44, "下期预告 · La semaine prochaine (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "双11当天11月11日星期三,包裹到了吗?S16淘汰赛打完了,谁进了决赛?总决赛北京时间11月15日凌晨3点。还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
