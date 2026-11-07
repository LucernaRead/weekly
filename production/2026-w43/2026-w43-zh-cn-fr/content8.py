# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zhcn-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 测验与答案 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("测验与答案 · Test et réponses", "Lucerna", "第 8 版 · 本周大测验 + 全部答案 · Le test de la semaine et toutes les réponses")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判断对错 · Vrai ou faux", 21, OLIVE, 5)
f.ex("A2", "完形单选", "A", "La fête tombe le 9e jour du 9e mois lunaire.",
     "重阳节在农历九月初九。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "B", "Le 23 oct. vient APRÈS le 18 oct. cette année.",
     "霜降在重阳节以前。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "A", "En prévente, on paie d'abord l'acompte.",
     "预售的时候先付定金。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "La finale S16 est à New York ; LA a accueilli les qualifications.",
     "S16 总决赛在洛杉矶。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "A", "Le paiement du solde a ouvert le 20 oct. à 20 h.",
     "付尾款的时间是10月20日晚上8点。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "La baisse mesurée : environ 25,8 %, pas 40 %.",
     "大闸蟹的价格真的降了40%。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Les Chinois ont pris le bronze avec 249.193 points.",
     "中国体操男队拿到铜牌。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "C'était le 10e défilé Victoria's Secret de Liu Wen.",
     "刘雯第十次走上维密的舞台。(A. 对 · B. 错)", size=13.8, gap=0)
f.head("B · 本周大测验 · Le grand quiz", 21, OLIVE, 5)
f.ex("A2", "单选", "B", "Les ventes en stock durent jusqu'au 13 nov.",
     "双11 现货一直卖到哪天? A. 11月11日 · B. 11月13日 · C. 10月31日", size=13.8, gap=0)
f.ex("A2", "单选", "A", "Les kakis sont le fruit de cette date.",
     "霜降吃的是什么? A. 柿子 · B. 月饼 · C. 粽子", size=13.8, gap=0)
f.ex("B1", "单选", "C", "La finale féminine : le 22 oct. à 01 h 30, heure de Pékin.",
     "体操女团决赛在北京时间几点? A. 10月21日上午 · B. 10月22日晚上8点 · C. 10月22日凌晨1点30分", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Production attendue au lac Yangcheng : environ 10 100 tonnes.",
     "阳澄湖大闸蟹预计总产量是多少? A. 约1.01万吨 · B. 约10.1万吨 · C. 约101万吨", size=13.8, gap=0)
f.ex("A2", "单选", "C", "Le terme tombe le vendredi 23 oct.",
     "霜降在10月几日? A. 20日 · B. 7日 · C. 23日", size=13.8, gap=0)
f.ex("B1", "单选", "B", "AL est la tête de série n° 1 de la LPL aux S16.",
     "LPL 的四支队里,哪支是一号种子? A. BLG · B. AL · C. IG", size=13.8, gap=0)
f.ex("B2", "单选", "B", "Prix au sortir de l'eau : à peu près le niveau des trois dernières années.",
     "协会说出水价怎么样? A. 涨了很多 · B. 和最近三年差不多 · C. 只有去年的一半", size=13.8, gap=0)
f.ex("A2", "单选", "A", "Neuvième mois lunaire : les femelles d'abord.",
     "农历九月先吃什么蟹? A. 母蟹 · B. 公蟹 · C. 小蟹", size=13.8, gap=0)
f.ex("B1", "单选", "C", "LeBron a débuté sous le maillot des 76ers.",
     "詹姆斯穿上哪支队的球衣? A. 尼克斯 · B. 凯尔特人 · C. 76人", size=13.8, gap=0)
f.ex("B2", "单选", "A", "Le tablier rond de la femelle.",
     "「九月圆脐十月尖」里,「圆脐」说的是: A. 母蟹的肚脐形状 · B. 月亮的形状 · C. 蟹的大小", size=13.8, gap=0)
f.head("C · 完成句子 · Complétez les phrases", 21, OLIVE, 5)
f.ex("A2", "完成句子", "尾款", "Heure du solde : le 20 oct., 20 h.",
     "10月20日晚上8点付___。", instr="Complétez", size=13.8, gap=0)
f.ex("A2", "完成句子", "定金", "En prévente : l'acompte d'abord, le solde ensuite.",
     "预售先付___,后付尾款。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "满减", "mǎnjiǎn : 300 d'achat, 50 de moins.",
     "买满300减50,这叫___。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "鹿特丹", "Les Mondiaux de gymnastique étaient à Rotterdam.",
     "体操世锦赛在荷兰___举行。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "艾伦", "Le tour suisse des S16 est à Allen, au Texas.",
     "S16 瑞士轮在美国___市举行。", instr="Complétez", size=13.8, gap=0)
f.ex("A2", "完成句子", "柿子", "Des kakis à cette date, et les lèvres ne gercent pas.",
     "霜降吃___,嘴唇不会裂。", instr="Complétez", size=13.8, gap=0)
f.ex("B2", "完成句子", "滞销", "zhìxiāo : ventes lentes, dans quelques zones périphériques seulement.",
     "少数外围产区的蟹有点___,卖得慢。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "直播", "zhíbō : le défilé était diffusé en direct.",
     "维密秀在网上___,很多人在线看。", instr="Complétez", size=13.8, gap=0)
f.ex("B2", "完成句子", "声明", "shēngmíng : la déclaration officielle de l'association.",
     "协会发表___,说「崩盘」不是真的。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "通宵", "tōngxiāo : éveillé toute la nuit pour le match.",
     "比赛在凌晨,看比赛的人要___。", instr="Complétez", size=13.8, gap=0)
f.head("D · 读一读,答一答 · Lisez et répondez", 21, OLIVE, 5)
f.para("小林住在上海。他在网上看中了一件外套,先付了30元定金。10月20日晚上8点,他付了尾款。周五是霜降,他下班后去超市买了柿子。周六凌晨1点,他起来看 S16 的瑞士轮比赛,AL 打得很好。看完比赛,他睡了一个好觉。", 15, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Il a payé un acompte de 30 yuans.",
     "小林先付了多少钱定金? A. 20元 · B. 30元 · C. 50元", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Ce vendredi-là, il a acheté des kakis après le travail.",
     "霜降那天他做了什么? A. 下班后买柿子 · B. 陪妈妈爬山 · C. 通宵看比赛", size=13.8, gap=0)
f.ex("B1", "单选", "C", "Il a regardé à 01 h samedi.",
     "他看比赛的时间是? A. 周五晚上8点 · B. 周六上午 · C. 周六凌晨1点", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Il a regardé le tour suisse des S16.",
     "他看的是哪个比赛? A. NBA · B. S16 瑞士轮 · C. 体操世锦赛", size=13.8, gap=0)
f.ex("B2", "单选", "A", "Ordre : les achats, puis le terme solaire, puis le match.",
     "这段话的顺序是什么? A. 先购物,再过节气,再看比赛 · B. 先看比赛,再购物 · C. 先过节气,再看比赛,再购物", size=13.8, gap=0)
f.ex("B2", "完成句子", "上海", "Xiao Lin habite à Shanghai.",
     "小林住在___。", instr="Complétez", size=13.8, gap=0)
f.head("E · 情景说话 · En situation", 21, OLIVE, 5)
f.ex("B1", "完形单选", "B", "La livraison commence une fois le solde payé.",
     "— 我的包裹到了吗? — 付完___,快递就开始送了。(A. 定金 · B. 尾款)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Le dicton : mieux vaut bien manger à cette date qu'en hiver.",
     "— 霜降要多穿点吗? — 要。___不如补霜降,先吃点好的。(A. 补冬 · B. 补夏)", size=13.8, gap=0)
f.ex("B2", "完形单选", "A", "Règle de la page 6 : les données d'abord, le titre ensuite.",
     "— 这条新闻说价格崩盘,可信吗? — 先看___,再看标题。(A. 数据 · B. 评论)", size=13.8, gap=0)
f.head("F · 写一写 · À vos plumes", 21, OLIVE, 5)
MODELO = ("我的双11购物车里有三样东西:一件外套、一条围巾和一盒柿子。"
          "外套260元,围巾60元,柿子40元,一共360元。"
          "今年有满300减50的活动,实付310元。"
          "我在预售时先付了30元定金,10月20日晚上8点付尾款280元。"
          "付完尾款,我就等快递了。霜降快到了,我想穿新外套、吃甜柿子,过一个暖和的秋天。")
NCHARS = len(MODELO.replace(" ", ""))
f.expl(f"Écriture — il n'y a pas de réponse unique. Un modèle de {NCHARS} caractères suit.")
f.ex("B1", "写作", "(question ouverte — modèle ci-dessous)", f"Question ouverte — le modèle est dans la section F de cette page, {NCHARS} caractères",
     "写一写《我的双11购物车》:你想买什么?先付多少定金?尾款多少?一共多少钱?写 120~180 字。", instr="Écrivez", size=13.8, gap=0)
f.para("Modèle : " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= keys =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答案 · Réponses — par page, avec une note pour chaque réponse", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Toutes les notes en français · ✓ = l'exercice d'écriture", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Page {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} ({e_['note']})"
        if e_["type"] == "写作":
            txt = f"{e_['n']}. ✓ ({e_['note']})"
        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ceyan.svg")
print("P8 saved, exercises total:", len(REG))
from collections import Counter
print("levels:", Counter(e_["level"] for e_ in REG))
print("writing model chars:", NCHARS)
