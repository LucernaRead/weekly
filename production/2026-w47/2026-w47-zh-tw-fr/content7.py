# -*- coding: utf-8 -*-
# W47 zh-tw core, VOL.4: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言　Langue", "Lucerna", "語言聚焦　三個級別　三個主題　Trois niveaux, trois thèmes")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　遊行的話　Mots du défilé", 25)
a.para("Les défilés vous donnent quatre mots utiles : 遊行 (défilé), 封王 (remporter le titre), 夜間 (de nuit) et 終點 (ligne d'arrivée). Apprenez-les une fois, et chaque défilé devient clair.", 22)
a.expl("Quatre mots de défilé : 遊行, 封王, 夜間, 終點.")
a.para("遊行 est une marche de fête dans les rues. 封王 signifie gagner le championnat. 夜間 signifie de nuit — la parade nocturne commence à 19:00. 終點 est l'endroit où le défilé se termine : le Taipei Dome.", 22)
a.ex("A2", "完成句子", "遊行", "Une marche de fête, c'est 遊行.",
     "大家走上街頭慶祝，叫___。", instr="Compléter", size=22, gap=10)
a.ex("A2", "單選", "A", "Le défilé part à 14:00 le 22 nov.",
     "封王遊行幾點出發？", opts=["A. 下午2點", "B. 上午2點", "C. 晚上7點"], size=22, gap=10)
a.ex("A2", "完成句子", "封王", "Remporter le titre, c'est 封王.",
     "拿下總冠軍，叫___。", instr="Compléter", size=22, gap=10)
a.ex("A2", "單選", "A", "La parade nocturne commence à 19:00.",
     "夜間遊行晚上幾點開始？", opts=["A. 晚上7點", "B. 下午2點", "C. 上午10點"], size=22, gap=10)
a.end_report()
# ---- P7 image: below the A2 column (free space) ----
iy7 = a.y + 16
image(p, "books.jpg", COLX[0], iy7, CW, 140)
cy7 = caption(p, COLX[0], iy7 + 140, CW,
              "舊書，越讀越有味道（資料照片）。",
              "Photo : auteur inconnu — CC0 (Wikimedia Commons)")
print("P7 image ends", cy7, "(A2 flow ended", a.y, ")")

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　電影與鋼雕　Cinéma & acier", 25)
b.para("Le cinéma et l'acier partagent les gros titres de cette semaine. Groupez les mots et ils restent : cinéma （入圍、頒獎、星光大道） et acier （鋼雕、保險箱、勞動記憶）.", 22)
b.expl("Groupez les mots : cinéma (入圍/頒獎), acier (鋼雕/保險箱).")
b.para("入圍 signifie être nommé ; 頒獎 signifie remettre les prix. 星光大道 est le tapis rouge avant la cérémonie. 鋼雕 est une sculpture en acier ; 保險箱 est le coffre qui garde les mémoires ouvrières de Kaohsiung.", 22)
b.ex("B1", "完成句子", "入圍", "Être nommé, c'est 入圍.",
     "被選進最後的得獎名單，叫___。", instr="Compléter", size=22, gap=10)
b.ex("B1", "單選", "A", "La cérémonie commence à 18:30 le 22 nov.",
     "金馬獎頒獎典禮幾點開始？", opts=["A. 晚上6點30分", "B. 下午2點", "C. 上午10點"], size=22, gap=10)
b.ex("B1", "完成句子", "鋼雕", "Une sculpture en acier, c'est 鋼雕.",
     "用鋼鐵做的藝術，叫___。", instr="Compléter", size=22, gap=10)
b.ex("B1", "單選", "A", "Le festival de l'acier se termine le 22 nov.",
     "鋼雕藝術節展到哪天？", opts=["A. 11月22日", "B. 11月15日", "C. 11月9日"], size=22, gap=10)
b.para("Astuce mémoire : apprenez d'abord 入圍, puis 星光大道 (le tapis rouge à 17:00, avant la cérémonie), puis la cérémonie （頒獎） à 18:30.", 22)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　節氣與耶誕　Saisons", 25)
c.para("L'hiver apporte ses propres mots. Cette semaine : 小雪 (Neige mineure), 節氣 (terme solaire), 燈秀 (spectacle de lumières) et 市集 (marché).", 22)
c.expl("Quatre mots d'hiver de ce numéro : 小雪, 節氣, 燈秀, 市集.")
c.para("小雪 est le 20e terme solaire, après 立冬. 節氣 signifie terme solaire — 24 par an. 燈秀 est un spectacle de lumières : le spectacle principal a lieu toutes les demi-heures. 市集 est un marché — le marché d'hiver de World of Frozen.", 22)
c.ex("B2", "單選", "A", "Xiaoxue est le 20e terme solaire.",
     "「小雪」是二十四節氣的第幾個？", opts=["A. 第20個", "B. 第2個", "C. 第24個"], size=22, gap=10)
c.ex("B2", "完成句子", "主燈秀", "Le spectacle de lumières principal se répète toutes les demi-heures.",
     "耶誕城的___每半小時一次。", instr="Compléter", size=22, gap=10)
c.ex("B2", "單選", "A", "Le marché d'hiver est à World of Frozen.",
     "想逛冬日市集、買聖誕禮物，要去哪裡？", opts=["A. 魔雪奇緣世界", "B. 維多利亞港", "C. 駁二"], size=22, gap=10)
c.ex("B2", "完成句子", "市集", "Un marché, c'est 市集.",
     "賣東西、逛街的地方，叫___。", instr="Compléter", size=22, gap=10)
c.para("Pas besoin de beaucoup de mots de saison — apprenez-en quatre et l'hiver se rapproche.", 22)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「金馬獎11月15日頒獎」", "→「金馬獎11月22日頒獎，11月15日是爵士之夜」", "La cérémonie est le 22 nov. ; le 15 nov. est une soirée jazz."),
    ("「封王遊行上午2點出發」", "→「封王遊行下午2點出發，上午沒有遊行」", "Le défilé part à 14:00, pas à 02:00."),
    ("「主燈秀每小時一次」", "→「主燈秀每半小時一次，17:30到23:00一共12場」", "Le spectacle principal a lieu toutes les demi-heures : 12 fois, 17:30–23:00."),
]
eh = 74 + sum(72 + len(wrap("✗ " + r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所　Clinique des erreurs", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, "✗ " + wrong, 21.5, "serif", True, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「天氣越冷，越要保暖。」 — 越…越… signifie : plus X, plus Y. 夜越深，燈越亮 (plus la nuit est sombre, plus les lumières sont brillantes)."
wcn = "Structure : 越…越… — plus X, plus Y. Faites votre propre phrase avec."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式　Structure de phrase", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好：本週日我要去看封王遊行，穿紅色衣服為龍隊喝采。晚上回家看金馬獎轉播，還想去高雄看鋼雕，最後一天不要錯過。——台北小讀者（編輯範例）」"
lcn = "Lettre d'exemple de la rédaction, pas une vraie lettre : VOL.3 avait promis de vraies lettres et les meilleurs textes de la page 8 dès ce numéro ; aucune lettre publiable n'était arrivée au bouclage. L'exemple reste, l'invitation reste ouverte."
lt2 = "延期披露：VOL.3曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。"
lh = 164 + (len(wrap(lt, "serif", False, 21.5, CW - 44)) + len(wrap(lt2, "serif", False, 21.5, CW - 44))) * 30.53 + (len(wrap(lcn, "sans", False, 20, CW - 44)) - 1) * 28.4
# exact draw model: lead-in 89 + lt/lt2 block lines x30.53 + gaps 31/30 + lcn lines
# (last baseline + descent 6 + pad 8). The old 62/12/26 formula under-counted
# the lead-in and inter-para gaps by ~20px (caught by occlusion audit, build 10).
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地　Coin des lecteurs", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 24)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "本週金句　Phrases de la semaine — mot pour mot des articles de ce numéro", 27, "sans", True, OLIVE)
quotes = [
    ("「封王遊行從天母棒球場出發」", "Le défilé du titre part du stade de baseball de Tianmu.", "p. 1"),
    ("「夜間遊行晚上7點，最後一場不要錯過」", "La parade nocturne à 19:00 — la dernière représentation, à ne pas manquer.", "p. 1"),
    ("「小雪之後，天氣一天比一天冷」", "Après Xiaoxue, chaque jour est plus froid que le précédent.", "p. 2"),
    ("「主燈秀每半小時一次，每次5分鐘」", "Le spectacle de lumières principal toutes les demi-heures, 5 minutes à chaque fois.", "p. 2"),
    ("「頒獎典禮晚上6點30分開始」", "La cérémonie de remise des prix commence à 18:30.", "p. 3"),
    ("「保險箱裡，裝的是高雄的勞動記憶」", "Dans le coffre : les mémoires ouvrières de Kaohsiung.", "p. 3"),
    ("「穿上紅色衣服，一起上街為龍隊喝采」", "Portez du rouge, descendez dans la rue, encouragez les Dragons.", "p. 4"),
    ("「香港迪士尼聖誕，從11月17日開始」", "Noël à Disneyland commence le 17 nov.", "p. 5"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 132
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 132 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "下期預告　La semaine prochaine (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "下週：金馬獎得獎名單、封王遊行直擊、鋼雕閉幕現場，還有你們的來信和第8版最佳作文。下週見！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
