# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-cn-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Le point langue", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Trois niveaux, trois thèmes")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与包裹 · Le shopping", 24)
a.para("Mots du shopping pour cette semaine : 高潮场 (gāocháochǎng, la grande vente), 包裹 (bāoguǒ, un colis), 取件码 (qǔjiànmǎ, un code de retrait), 快递柜 (kuàidìguì, un casier à colis). Mots de sécurité : 消防 (xiāofáng, prévention incendie), 疏散 (shūsàn, évacuer), 自救 (zìjiù, autosauvetage).", 21.5)
a.glossline("Les classificateurs comptent toujours : 一个包裹 (un colis), 一部电影 (un film), 一场演练 (un exercice).")
a.ex("A2", "完成句子", "个", "包裹 prend le classificateur 个 gè.",
     "我拿了___包裹。", instr="Compléter", size=20.5, gap=10)
a.ex("A2", "单选", "A", "高潮场 signifie la grande vente.",
     "「高潮场」是什么意思? A. 最忙的卖货时间 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "消防", "xiāofáng — prévention incendie, 9 nov.",
     "11月9日是全国___日。", instr="Compléter", size=20.5, gap=10)
a.ex("A2", "单选", "A", "Les colis prennent 个 — pas 只 ni 条.",
     "哪个说法对? A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20.5, gap=10)
a.para("Encore un pour s'entraîner : 「我的包裹到了吗?」 (Mon colis est-il arrivé ?) Quand tu attends un colis, demande d'abord, puis va au casier.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Heures et dates", 24)
b.para("Le chinois donne les heures du grand au petit : année, mois, jour, jour de la semaine, moment de la journée, heure. Exemples de ce numéro : 「11月9日星期一」 (lun. 9 nov.), 「11月10日星期二20点」 (mar. 10 nov., 20 h 00), 「11月15日星期日凌晨3点」 (dim. 15 nov., 3 h du matin). La plus grande unité d'abord, rien dans le désordre.", 21.5)
b.glossline("Ainsi, l'anglais « Monday, Nov 9 » devient 11月9日星期一.")
b.ex("B1", "单选", "B", "凌晨 língchén — les petites heures après minuit.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "06:00, c'est 早上 — pas le soir.",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="Compléter", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Ordre grand → petit : 15 nov., dimanche, 03:00.",
     "哪个顺序对? A. 11月15日星期日凌晨3点 · B. 凌晨3点星期日11月15日 · C. 星期日凌晨3点11月15日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周一", "Le 9 novembre, c'est un lundi — 周一.",
     "11月9日是星期一,也可以说___。消防日在这天。", instr="Compléter", size=20.5, gap=10)
b.para("Deux mots de plus : 凌晨 (língchén), ce sont les petites heures après minuit, avant l'aube ; 傍晚 (bàngwǎn), c'est le court moment juste avant la nuit.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Lire les nouvelles", 24)
c.para("Quand une histoire contient une affirmation (说法), sépare trois sortes de phrases : les affirmations (说法), les données (数据) et les prévisions (预报). La page 6 est l'exemple : 「最大的一波」 est une affirmation sur le 11 novembre, les multiples 1,5 et 2,5 sont des données rapportées, et les températures de l'air froid sont une prévision — prédite, pas encore un fait.", 21.5)
c.glossline("Pour chaque chiffre, demande : à qui est ce chiffre, et quand a-t-il été mesuré ?")
c.ex("B2", "单选", "C", "「最大的一波」 : affirmation, pas données mesurées.",
     "「最大的一波」在第6版里是什么? A. 数据 · B. 预报 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — des chiffres mesurés, pas des affirmations.",
     "买东西以前,先看___,再看广告。", instr="Compléter", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Données et caisse d'abord, titre en dernier.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — une prévision est prédite, pas encore un fait.",
     "冷空气的温度是___,还没发生。", instr="Compléter", size=20.5, gap=10)
c.para("Essaie toi-même : dans le calendrier de la page 1, 「11月11日」 est une date — des données. Les mots d'une publicité sont des affirmations. Peux-tu les distinguer ?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) indique comment une action est faite."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) relie verbe + degré : 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "Ordre : nombre + classificateur + nom."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日,星期日凌晨3点。」", "Les heures vont du grand au petit : le jour de la semaine en dernier."),
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
wt = "「先看取件码,再开柜门。」(Vérifie le code, puis ouvre le casier.) Le cadre 先…再… donne l'ordre des actions."
wcn = "Cadre : 先 … 再 … — d'abord X, puis Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Structure de phrase", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在北京。11月9日学校做了消防演练,我学会了走楼梯。双11我买了一本书,包裹两天就到了。周日凌晨,我想看S16总决赛!」"
lcn = "编辑部示例信,不是真实来信。VOL.2曾预告本期刊登真实来信和最佳作文;截至11月2日截稿,仍未收到,本期仍刊示例,继续征集。延期不是取消。Note de la rédaction : VOL.2 promettait de vraies lettres dans VOL.3 ; aucune n'est arrivée au 2 nov. L'exemple reste. Reporté, pas annulé."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · Coin des lecteurs", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · Phrases de la semaine (mot pour mot, tirées des propres articles de ce numéro)", 27, "sans", True, OLIVE)
quotes = [
    ("「双11的正日子」", "Le jour du Double 11 lui-même.", "p. 1"),
    ("「先看结算页,再决定买不买」", "Vérifie la page de caisse, puis décide.", "p. 2"),
    ("「提高自防自救能力」", "Renforcer la capacité d'autoprotection et d'autosauvetage.", "p. 3"),
    ("「三支队进了八强」", "Trois équipes ont atteint les quarts de finale.", "p. 4"),
    ("「输了就回家」", "Perdre, et tu rentres chez toi.", "p. 4"),
    ("「老电影,新画面」", "Un vieux film, une nouvelle image.", "p. 5"),
    ("「快递的高峰分三波」", "Le pic des colis vient en trois vagues.", "p. 6"),
    ("「着火了不坐电梯」", "En cas d'incendie, ne prends pas l'ascenseur.", "p. 3"),
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
p.text(MX + 28, py + 44, "下期预告 · La semaine prochaine (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16总决赛打完了,谁是冠军?包裹都到了吗?还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
