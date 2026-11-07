# -*- coding: utf-8 -*-
# W46 zh-tw core, VOL.3: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-tw-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Focus langue", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Trois niveaux, trois thèmes")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 雙11的話 · Mots du Double 11", 24)
a.para("Le Double 11 vous donne quatre mots utiles : 清單 (liste de courses), 實付金額 (le montant final payé), 領券 (réclamer des coupons) et 鑑賞期 (le délai de rétractation). Apprenez-les une fois, et chaque solde devient claire.", 21.5)
a.glossline("Quatre mots du Double 11 : 清單, 實付金額, 領券, 鑑賞期.")
a.para("清單 est la liste que vous écrivez avant d'acheter. 實付金額 est ce que vous payez vraiment après les réductions. 領券 veut dire réclamer un coupon avant qu'il ne s'épuise. 鑑賞期 : les 7 jours après la livraison pendant lesquels vous pouvez retourner la plupart des articles.", 21.5)
a.ex("A2", "完成句子", "清單", "Une liste de courses, c'est une 清單.",
     "買東西之前,先列___。", instr="Complétez", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Le délai de rétractation est de 7 jours.",
     "鑑賞期是幾天?", opts=["A. 7天", "B. 3天", "C. 14天"], size=20.5, gap=10)
a.ex("A2", "完成句子", "實付金額", "Comparez le montant final que vous payez vraiment.",
     "比價要比___。", instr="Complétez", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Réclamez les coupons avant qu'ils ne s'épuisent.",
     "優惠券要怎麼拿?", opts=["A. 先領,領完就沒有了", "B. 不用領", "C. 過期再領"], size=20.5, gap=10)
a.para("Entraînez-vous : 「我的購物清單是什麼？」 (« Qu'y a-t-il sur ma liste de courses ? ») — écrivez-la d'abord, puis comparez les prix.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 影展與鋼雕 · Cinéma et acier", 24)
b.para("Le cinéma et l'acier partagent les gros titres de la semaine. Groupez les mots et ils restent : cinéma （入圍、頒獎、星光大道） et acier （鋼雕、保險箱、勞動記憶）.", 21.5)
b.glossline("Groupez les mots : cinéma (入圍/頒獎), acier (鋼雕/保險箱).")
b.para("入圍 veut dire être nommé ; 頒獎 veut dire remettre les prix. 星光大道 est le tapis rouge avant la cérémonie. 鋼雕 est une sculpture en acier ; 保險箱 est le coffre-fort qui garde les souvenirs de travail de Kaohsiung.", 21.5)
b.ex("B1", "完成句子", "入圍", "Être nommé, c'est 入圍.",
     "被選進最後的得獎名單,叫___。", instr="Complétez", size=20.5, gap=10)
b.ex("B1", "單選", "A", "La cérémonie commence à 18h30 le 22 nov.",
     "金馬獎頒獎典禮幾點開始?", opts=["A. 晚上6點30分", "B. 下午2點", "C. 上午10點"], size=20.5, gap=10)
b.ex("B1", "完成句子", "鋼雕", "Une sculpture en acier, c'est 鋼雕.",
     "用鋼鐵做的藝術,叫___。", instr="Complétez", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Le festival de l'acier se termine le 22 nov.",
     "鋼雕藝術節展到哪天?", opts=["A. 11月22日", "B. 11月15日", "C. 11月9日"], size=20.5, gap=10)
b.para("Astuce : apprenez d'abord 入圍 — puis la cérémonie （頒獎）, puis le lieu où elle a lieu （星光大道）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 港台說法 · Parlers locaux", 24)
c.para("Taïwan et Hong Kong ont chacun leur façon de dire les choses. Cette semaine : 打卡 (s'enregistrer avec une photo), 集點 (collecter des points), 遊行 (défilé dans la rue) et 感謝祭 (festival de remerciement pour les supporters).", 21.5)
c.glossline("Quatre mots locaux de ce numéro : 打卡, 集點, 遊行, 感謝祭.")
c.para("打卡 à une foire veut dire poster une photo pour dire « j'étais là ». 集點 : gagner des points à chaque séance de sport. 遊行 est la marche de fête dans les rues ; 感謝祭 est le festival de remerciement de l'équipe pour ses supporters.", 21.5)
c.ex("B2", "單選", "A", "集點 veut dire collecter des points en faisant du sport.",
     "「集點」是什麼意思?", opts=["A. 每次運動累積點數", "B. 買門票", "C. 上班簽到"], size=20.5, gap=10)
c.ex("B2", "完成句子", "遊行", "Une marche de fête, c'est 遊行.",
     "大家走上街頭慶祝,叫___。", instr="Complétez", size=20.5, gap=10)
c.ex("B2", "單選", "A", "感謝祭 remercie les supporters.",
     "「感謝祭」是謝謝誰的活動?", opts=["A. 球迷", "B. 店員", "C. 記者"], size=20.5, gap=10)
c.ex("B2", "完成句子", "打卡", "S'enregistrer avec une photo, c'est 打卡.",
     "在嘉年華拍照分享,叫___。", instr="Complétez", size=20.5, gap=10)
c.para("Pas besoin de beaucoup d'expressions locales — apprenez-en quatre et chaque sortie semble plus proche.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「旅展在11月9日開幕」", "→「旅展在11月9日落幕,開幕是11月6日」", "Foire ouverte le 6 nov., fermée le 9 nov. Vérifiez le sens du temps."),
    ("「金馬獎11月15日頒獎」", "→「金馬獎11月22日頒獎,11月15日是嘉年華」", "Cérémonie : 22 nov. ; carnaval : 15 nov. (2e jour)."),
    ("「滿5,000折800,實付5,800元」", "→「滿5,000折800,實付4,200元」", "On soustrait les réductions : 5 000 − 800 = 4 200."),
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
wt = "「雙11不但有折扣,而且有免運。」 — La structure 不但…而且… veut dire : non seulement X, mais aussi Y. À vous : 旅展不但有攤位,而且有表演 (non seulement des stands, mais aussi des spectacles)."
wcn = "Structure : 不但…而且… — non seulement X, mais aussi Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Structure de la semaine", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:雙11我的包裹到了!我買了一本書和一件外套,都沒有超過預算。週末我想去銅鑼灣看夜光巡遊,還想去高雄看鋼雕。——台北小讀者(編輯範例)」"
lcn = "Lettre d'exemple de la rédaction — pas une vraie lettre. VOL.2 promettait de vraies lettres et les meilleurs textes de la page 8 dès ce numéro ; aucune n'était arrivée à la clôture. L'exemple reste, l'invitation aussi."
lt2 = "延期披露:VOL.2曾預告本期起刊登真實讀者來信和第8版最佳作文;截至截稿,本報未收到可刊登的真實來信與投稿,因此本期仍刊登編輯範例,並繼續公開徵集。你的來信,下一期見。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 40
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Coin des lecteurs", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Phrases de la semaine — mot pour mot, tirées des articles de ce numéro", 27, "sans", True, OLIVE)
quotes = [
    ("「先列清單,再比價,最後才結帳」", "D'abord la liste, puis les prix, puis payer.", "p. 1"),
    ("「旅展四天,一次看完123個國家及城市」", "Quatre jours de foire, 123 pays et villes en une visite.", "p. 1"),
    ("「早晚溫差大,外套要隨身帶」", "Grands écarts jour-nuit — gardez une veste avec vous.", "p. 2"),
    ("「金馬影展,就是一年一度的大電影課」", "Le festival Golden Horse, c'est un grand cours de cinéma par an.", "p. 3"),
    ("「保險箱裡,裝的是高雄的勞動記憶」", "Dans le coffre : les souvenirs de travail de Kaohsiung.", "p. 3"),
    ("「穿上紅色衣服,一起上街為龍隊喝采」", "Portez du rouge, descendez dans la rue, encouragez les Dragons.", "p. 4"),
    ("「嘉年華不用門票,全家人都能來玩」", "Pas de billet — toute la famille peut venir jouer.", "p. 5"),
    ("「回饋不是折價,實付金額才是真的」", "Le cashback n'est pas une réduction — c'est le montant payé qui compte.", "p. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 138
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 138 + 4  # fix 2026-11-03: was +18; teaser bottom crossed the footer rule (2587.86 > 2580)
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期預告 · La semaine prochaine (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "下週日11月22日,三件大事同一天:封王遊行下午2點、金馬獎晚上6點30分、鋼雕藝術節閉幕,還有小雪、你們的來信和第8版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
