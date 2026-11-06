# -*- coding: utf-8 -*-
# W45 zh-tw core, VOL.2: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Focus langue", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Trois niveaux, trois sujets")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 展會的話 · Les mots des salons", 24)
a.para("Les salons de cette semaine vous offrent quatre mots utiles : 旅展 (salon du voyage), 攤位 (stand), 集章 (tampons) et 吉祥物大遊行 (défilé des mascottes). Apprenez-les une fois, et tout le salon devient clair.", 21.5)
a.glossline("Quatre mots des salons : 旅展, 攤位, 集章, 吉祥物大遊行.")
a.para("旅展 abrège 旅行展覽會 (exposition de voyage). Un 攤位 est un étal du salon ; celui de Taipei en compte 1 600. 集章 veut dire collectionner des tampons à des points précis — les six tampons des voies vertes, et vous gagnez un prix.", 21.5)
a.ex("A2", "完成句子", "攤位", "Un stand à l'intérieur du salon, c'est un 攤位.",
     "旅展裡的一個小展位,叫___。", instr="Complétez", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Le défilé des mascottes a lieu chaque jour à 14 h 00.",
     "吉祥物大遊行每天幾點?", opts=["A. 下午2點", "B. 中午12點", "C. 晚上7點"], size=20.5, gap=10)
a.ex("A2", "完成句子", "集章", "Collectionner les tampons à des points précis, c'est 集章.",
     "在6大綠道蓋章收集,叫___。", instr="Complétez", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Le salon du voyage se tient au Centre des expositions de Nangang.",
     "台北旅展在哪裡?", opts=["A. 南港展覽館一館", "B. 台北大巨蛋", "C. 高雄駁二"], size=20.5, gap=10)
a.para("Entraînez-vous : 「旅展幾點開門？」 (« À quelle heure ouvre le salon ? ») — vendredi à midi, les autres jours à 10 h 00.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 球賽與節氣 · Matchs et saisons", 24)
b.para("Le sport et les saisons partagent les gros titres de cette semaine. Groupez les mots et ils restent : gagner （封王、完封） et l'hiver （立冬、進補）.", 21.5)
b.glossline("Groupez les mots : gagner (封王/完封), l'hiver (立冬/進補).")
b.para("封王 signifie remporter le championnat ; 完封 signifie ne laisser aucun point à l'adversaire, 0 point. 立冬 est le terme solaire qui ouvre l'hiver ; 進補 consiste à manger des plats chauds et nourrissants avant les mois froids.", 21.5)
b.ex("B1", "完成句子", "封王", "Remporter le titre, c'est 封王.",
     "拿下總冠軍,叫___。", instr="Complétez", size=20.5, gap=10)
b.ex("B1", "單選", "A", "完封 signifie que l'adversaire ne marque aucun point.",
     "「完封」是什麼意思?", opts=["A. 對手得0分", "B. 大勝10分", "C. 打滿9局"], size=20.5, gap=10)
b.ex("B1", "完成句子", "立冬", "Lidong marque le début de l'hiver.",
     "冬天第一個節氣是___。", instr="Complétez", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Le canard au gingembre est un plat de Lidong.",
     "立冬常吃的鍋是哪一種?", opts=["A. 薑母鴨", "B. 冰品", "C. 生魚片"], size=20.5, gap=10)
b.para("Astuce mémoire : apprenez d'abord 封王 puis la manière dont il a été gagné （完封）, puis la saison où cela s'est produit （立冬）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 港台說法 · Parlers locaux", 24)
c.para("Taïwan et Hong Kong ont chacun leur façon de dire les choses. Cette semaine : 打卡 (photo de présence), 討糖 (chasse aux bonbons), 踩街 (défilé costumé) et 泡湯 (bain thermal).", 21.5)
c.glossline("Quatre mots locaux de ce numéro : 打卡, 討糖, 踩街, 泡湯.")
c.para("Autrefois 打卡 voulait dire pointer au travail ; dans un salon ou un festival, c'est une photo pour dire « j'y étais ». 討糖 désigne ce que les enfants disent aux boutiques à Halloween ; 踩街 est le défilé costumé lui-même ; 泡湯 est le plaisir automnal d'un bain thermal.", 21.5)
c.ex("B2", "單選", "A", "Lors d'un festival, 打卡 signifie publier une photo pour dire qu'on y était.",
     "在旅展、節慶場合,「打卡」是什麼意思?", opts=["A. 拍照分享,說自己來過", "B. 上班簽到", "C. 買門票"], size=20.5, gap=10)
c.ex("B2", "完成句子", "討糖", "La chasse aux bonbons, c'est 討糖.",
     "萬聖節小朋友去店家___。", instr="Complétez", size=20.5, gap=10)
c.ex("B2", "單選", "A", "踩街 est un défilé costumé dans les rues.",
     "「踩街」是什麼?", opts=["A. 穿裝扮上街遊行", "B. 在街上跑步", "C. 逛夜市"], size=20.5, gap=10)
c.ex("B2", "完成句子", "泡湯", "Se baigner dans une source chaude, c'est 泡湯.",
     "秋冬去溫泉洗澡、放鬆,叫___。", instr="Complétez", size=20.5, gap=10)
c.para("Quatre expressions locales suffisent — chaque sortie vous semblera plus proche.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「龍隊完勝兄弟6比0」", "→「龍隊完封兄弟6比0」", "完勝 = gagner largement ; 完封 = aucun point pour l'adversaire."),
    ("「立冬就是冬至」", "→「立冬是冬天開始,冬至是白天最短的一天」", "Lidong ouvre l'hiver ; le solstice est le jour le plus court."),
    ("「金融科技週在台北開幕」", "→「金融科技週在香港開幕」", "Vérifiez la ville : c'est Hong Kong, pas Taipei."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所 · Clinique des erreurs", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先去集章，再去看表演。」 — 先…再… donne l'ordre : d'abord X, puis Y. Exemple : 先比價，再結帳 (comparez d'abord, puis payez)."
wcn = "Structure : 先…再… — d'abord X, puis Y. À vous !"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · La phrase-modèle", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:上週我去天母討糖,拿到一顆很大的糖果!這週我想去旅展看吉祥物大遊行,還想集滿6大綠道的章。——台北小讀者(編輯範例)」"
lcn = "Lettre d'exemple — pas une vraie lettre. Avis de report : VOL.1 avait promis de vraies lettres et les meilleurs textes de page 8 ; aucun texte publiable n'était arrivé — l'exemple reste, et l'invitation reste ouverte : écrivez-nous !"
lt2 = "延期披露:VOL.1曾預告本期起刊登真實讀者來信和第8版最佳作文;截至截稿,本報未收到可刊登的真實來信與投稿,因此本期仍刊登編輯範例,並繼續公開徵集。你的來信,下一期見。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 56
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Le coin des lecteurs", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Phrases de la semaine — mot pour mot tirées des articles de ce numéro", 27, "sans", True, OLIVE)
quotes = [
    ("「用手機轉帳、掃碼付款、網上買保險，都是金融科技」", "Payer par téléphone, scanner pour payer, acheter une assurance en ligne — c'est la fintech.", "p. 1"),
    ("「123個國家及城市、1,600個攤位」", "123 pays et villes, 1 600 stands.", "p. 1"),
    ("「需要才買，不要為了折扣買一堆用不到的東西」", "Achetez ce dont vous avez besoin ; n'achetez pas un tas de choses dont vous ne vous servirez pas juste pour une réduction.", "p. 2"),
    ("「在高雄，鋼鐵也能變成舞台」", "À Kaohsiung, même l'acier peut devenir une scène.", "p. 3"),
    ("「福隆的夏天，在10月26日畫下句點」", "L'été de Fulong s'est terminé le 26 octobre.", "p. 3"),
    ("「6比0完封兄弟，龍隊拋下紅色彩帶」", "Un blanchissage 6-0 contre les Brothers, et les Dragons ont lancé les rubans rouges.", "p. 4"),
    ("「250家店家一起討糖」", "250 boutiques distribuant des friandises ensemble.", "p. 5"),
    ("「旅展首日中午12點才開門」", "Le premier jour du salon, les portes n'ouvrent qu'à midi.", "p. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 138
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 138 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期預告 · La semaine prochaine (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "下週三雙11,你買了什麼?下週一旅展最後一天直擊,高雄鋼雕藝術節展到11月22日,還有你們的來信和第8版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
