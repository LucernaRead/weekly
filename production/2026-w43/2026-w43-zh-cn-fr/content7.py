# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zhcn-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Focus langue", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Trois niveaux, trois sujets")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 购物与量词 · Les classificateurs", 24)
a.para("Quand on fait des achats, le chinois utilise des classificateurs (量词) : 一件外套 — un manteau, 一条围巾 — une écharpe, 一斤蟹 — un demi-kilo de crabes, 一只蟹 — un crabe. Le schéma : nombre + classificateur + nom (数词 + 量词 + 名词).", 21.5)
a.expl("Le français compte librement ; le chinois choisit un classificateur pour chaque type de chose — ni pluriel, ni -s.")
a.ex("A2", "完成句子", "件", "Le manteau prend le classificateur jiàn.",
     "我想买一___外套。", instr="Complétez", size=20.5, gap=10)
a.ex("A2", "单选", "B", "L'écharpe prend tiáo, pour les choses longues et souples.",
     "「一条」可以说什么? A. 一条外套 · B. 一条围巾 · C. 一条大闸蟹", size=20.5, gap=10)
a.ex("A2", "完成句子", "斤", "jīn : un demi-kilo ; les prix du marché sont au jīn.",
     "大闸蟹多少钱一___?", instr="Complétez", size=20.5, gap=10)
a.ex("A2", "单选", "A", "Les vêtements prennent jiàn, pas gè ni tiáo.",
     "哪个说法对? A. 一件衣服 · B. 一个衣服 · C. 一条衣服", size=20.5, gap=10)
a.para("Encore un exemple : 「这件外套多少钱?」 (Combien coûte ce manteau ?) Pour vos achats, demandez d'abord le prix, puis payez.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Temps et dates", 24)
b.para("Le chinois énonce les horaires du grand vers le petit : année, mois, jour, jour de la semaine, moment du jour, heure. Exemple : 「10月20日晚上8点」 (le 20 oct., 20 h) — la plus grande unité d'abord, aucun désordre.", 21.5)
b.expl("Ainsi, le français « vendredi soir, 23 octobre » devient 10月23日星期五晚上.")
b.ex("B1", "单选", "B", "língchén : les heures après minuit.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "上午", "La NBA a ouvert le matin, heure de Pékin.",
     "NBA 在北京时间10月21日___开打。(不是晚上)", instr="Complétez", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Ordre grand → petit : 20 oct., soir, 20 h.",
     "哪个顺序对? A. 10月20日晚上8点 · B. 8点晚上10月20日 · C. 晚上8点10月20日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周五", "Le 23 oct. est un vendredi.",
     "10月23日是星期五,也可以说___。霜降在这天。", instr="Complétez", size=20.5, gap=10)
b.para("Deux mots de plus : 凌晨 (língchén), les heures après minuit, avant l'aube ; 傍晚 (bàngwǎn), le court moment juste avant la nuit.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Lire l'actualité", 24)
c.para("Quand un article parle d'un différend (争议), distinguez trois types de phrases : les affirmations en ligne (说法), les déclarations officielles (声明) et les données du marché (数据). Les affirmations peuvent exagérer ; les données doivent garder leur source et leur date. La page 6 est l'exemple : « 暴跌40% » est une affirmation, 77,5 元 et 57,5 元 sont des données, « 崩盘不实 » est une déclaration.", 21.5)
c.expl("Pour chaque chiffre, demandez : qui l'a mesuré, et quand ?") 
c.ex("B2", "单选", "C", "La chute de 40 % : une affirmation en ligne, pas une donnée mesurée.",
     "「暴跌超过40%」在第6版里是什么? A. 数据 · B. 声明 · C. 网上的说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "声明", "shēngmíng : la déclaration officielle de l'association.",
     "协会10月19日发表___,说「崩盘」不是真的。", instr="Complétez", size=20.5, gap=10)
c.ex("B2", "单选", "B", "D'abord les données et la source ; le titre en dernier.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和出处 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "25.8", "La baisse réelle, calculée page 6 : 25,8 %.",
     "第6版真正算出的数据降幅是___%。", instr="Complétez", size=20.5, gap=10)
c.para("À vous d'essayer : dans l'encadré des recherches chaudes page 1, 「第 8 位」 est un classement — une donnée. Les mots d'un titre sont des affirmations. Saurez-vous les distinguer ?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de) indique comment se fait l'action ; il se place avant le verbe."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de) relie un verbe à son complément de degré : 跑得快."),
    ("「我买了三只大闸蟹个」", "→ 「我买了三只大闸蟹。」", "Ordre : nombre + classificateur + nom. Le 个 final est en trop ; les crabes prennent 只."),
    ("「霜降在星期五十月二十三日」", "→ 「霜降在10月23日,星期五。」", "Les horaires vont du grand au petit : mois et jour d'abord, jour de semaine en dernier."),
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
wt = "「先付定金,后付尾款。」(D'abord l'acompte, puis le solde.) Le schéma 先…后/再… donne l'ordre des actions. Autres exemples : 「先看天气,再出门。」「先洗手,再吃饭。」"
wcn = "Schéma : 先 … 后/再 … — d'abord X, ensuite Y. Composez votre propre phrase."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Schéma de phrase", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在多伦多。霜降那天,我吃了柿子,也给妈妈打了电话。我的购物车里有一件外套,还在等付尾款。」"
lcn = "Une lettre d'exemple de la rédaction — pas une vraie. Le VOL.2 publiera de vraies lettres de lecteurs et les meilleurs textes de la page 8 !"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · Le coin des lecteurs", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · Phrases de la semaine (verbatim, tirées de ce numéro)", 27, "sans", True, OLIVE)
quotes = [
    ("「今年的双11来得早」", "Le 双11 de cette année est arrivé tôt.", "p. 1"),
    ("「付完尾款，快递就开始送货了」", "Le solde payé, la livraison commence.", "p. 1"),
    ("「付完尾款，商家就发货」", "Le solde payé, le vendeur expédie.", "p. 2"),
    ("「遥知兄弟登高处，遍插茱萸少一人」", "Le vers célèbre de Wang Wei sur la fête.", "p. 3"),
    ("「两个分数只差2.735分」", "Seulement 2.735 points d'écart entre les deux scores.", "p. 4"),
    ("「最大的看点是詹姆斯」", "La plus grande attraction : LeBron.", "p. 4"),
    ("「看S16，要通宵了」", "Regarder les S16, c'est veiller toute la nuit.", "p. 5"),
    ("「先看数据，再看标题」", "Les données d'abord, le titre ensuite : la règle de la page 6.", "p. 6"),
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
p.text(MX + 28, py + 44, "下期预告 · La semaine prochaine (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16 瑞士轮打完了:LPL 的四支队打得怎么样?双11 的包裹都到了吗?我们追踪报道。11月7日是立冬,冬天要来了。还有你们的来信和第 8 版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
