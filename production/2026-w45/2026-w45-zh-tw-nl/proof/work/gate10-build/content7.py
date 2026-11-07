# -*- coding: utf-8 -*-
# W45 zh-tw core, VOL.2: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-tw-nl-proof/work/gate10-out/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Taalfocus", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Drie niveaus, drie onderwerpen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 展會的話 · Beurswoorden", 24)
a.para("De beurzen van deze week geven je vier nuttige woorden: 旅展 (reisbeurs), 攤位 (stand), 集章 (stempels verzamelen) en 吉祥物大遊行 (mascotteparade). Leer ze één keer en alles wordt duidelijk.", 21.5)
a.glossline("Vier beurswoorden: 旅展, 攤位, 集章, 吉祥物大遊行.")
a.para("旅展 is een afkorting van 旅行展覽會 (reisttentoonstelling). Een 攤位 is één stand op de beurs; Taipei heeft er 1.600. 集章 betekent stempels verzamelen op vaste punten — verzamel alle zes Greenway-stempels en win een prijs.", 21.5)
a.ex("A2", "完成句子", "攤位", "Een stand op de beurs is een 攤位.",
     "旅展裡的一個小展位,叫___。", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "單選", "A", "De mascotteparade is dagelijks om 14.00 uur.",
     "吉祥物大遊行每天幾點?", opts=["A. 下午2點", "B. 中午12點", "C. 晚上7點"], size=20.5, gap=10)
a.ex("A2", "完成句子", "集章", "Stempels verzamelen op vaste punten is 集章.",
     "在6大綠道蓋章收集,叫___。", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "單選", "A", "De reisbeurs is in het Nangang Exhibition Center.",
     "台北旅展在哪裡?", opts=["A. 南港展覽館一館", "B. 台北大巨蛋", "C. 高雄駁二"], size=20.5, gap=10)
a.para("Oefen: 「旅展幾點開門？」 ('Hoe laat opent de beurs?') — vrijdag opent om 12.00 uur, andere dagen om 10.00 uur.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 球賽與節氣 · Sport & seizoenen", 24)
b.para("Sport en seizoenen delen de koppen van deze week. Groepeer de woorden en ze blijven hangen: winnen （封王、完封） en winter （立冬、進補）.", 21.5)
b.glossline("Groepeer de woorden: winnen (封王/完封), winter (立冬/進補).")
b.para("封王 betekent het kampioenschap pakken; 完封 betekent de andere ploeg op 0 houden. 立冬 is de zonneterm waarmee de winter begint; 進補 is voedzaam heet eten vóór de koude maanden.", 21.5)
b.ex("B1", "完成句子", "封王", "De titel winnen is 封王.",
     "拿下總冠軍,叫___。", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "單選", "A", "完封 betekent dat de andere ploeg nul scoort.",
     "「完封」是什麼意思?", opts=["A. 對手得0分", "B. 大勝10分", "C. 打滿9局"], size=20.5, gap=10)
b.ex("B1", "完成句子", "立冬", "Lidong luidt de winter in.",
     "冬天第一個節氣是___。", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Gember-eend is een Lidong-gerecht.",
     "立冬常吃的鍋是哪一種?", opts=["A. 薑母鴨", "B. 冰品", "C. 生魚片"], size=20.5, gap=10)
b.para("Geheugentruc: leer 封王 eerst, dan hoe de titel werd gewonnen （完封）, dan het seizoen （立冬）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 港台說法 · Lokaal taalgebruik", 24)
c.para("Taiwan en Hongkong hebben elk hun eigen zegswijze. Deze week: 打卡 (inchecken met een foto), 討糖 (trick-or-treaten), 踩街 (straatparade in kostuum) en 泡湯 (warmwaterbad).", 21.5)
c.glossline("Vier lokale woorden uit dit nummer: 打卡, 討糖, 踩街, 泡湯.")
c.para("打卡 begon als inklokken op het werk, maar op een beurs of festival betekent het een foto plaatsen: 'Ik was hier'. 討糖 is wat kinderen met Halloween bij winkels zeggen; 踩街 is de gekostumeerde optocht; 泡湯 is een warmwaterbad in de herfst.", 21.5)
c.ex("B2", "單選", "A", "Op een festival betekent 打卡 een foto plaatsen om te zeggen dat je er was.",
     "在旅展、節慶場合,「打卡」是什麼意思?", opts=["A. 拍照分享,說自己來過", "B. 上班簽到", "C. 買門票"], size=20.5, gap=10)
c.ex("B2", "完成句子", "討糖", "Trick-or-treaten is 討糖.",
     "萬聖節小朋友去店家___。", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "單選", "A", "踩街 is een gekostumeerde straatparade.",
     "「踩街」是什麼?", opts=["A. 穿裝扮上街遊行", "B. 在街上跑步", "C. 逛夜市"], size=20.5, gap=10)
c.ex("B2", "完成句子", "泡湯", "Baden in een warmwaterbron is 泡湯.",
     "秋冬去溫泉洗澡、放鬆,叫___。", instr="Vul in", size=20.5, gap=10)
c.para("Vier lokale uitdrukkingen volstaan — elk uitje voelt dan dichterbij.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「龍隊完勝兄弟6比0」", "→「龍隊完封兄弟6比0」", "完勝 betekent ruim winnen; 完封 betekent dat de andere ploeg nul scoorde."),
    ("「立冬就是冬至」", "→「立冬是冬天開始,冬至是白天最短的一天」", "Lidong luidt de winter in; de zonnewende is de kortste dag. Verschillende termen."),
    ("「金融科技週在台北開幕」", "→「金融科技週在香港開幕」", "Controleer de stad: de FinTech Week opent in Hongkong, niet in Taipei."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所 · Foutenkliniek", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先去集章，再去看表演。」 — het frame 先…再… geeft de volgorde aan: eerst X, dan Y. Maak er zelf een: 先比價，再結帳 (vergelijk eerst, betaal dan)."
wcn = "Frame: 先…再… — eerst X, dan Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Zinspatroon", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:上週我去天母討糖,拿到一顆很大的糖果!這週我想去旅展看吉祥物大遊行,還想集滿6大綠道的章。——台北小讀者(編輯範例)」"
lcn = "Voorbeeldbrief — geen echte. Uitstel: VOL.1 beloofde echte brieven en pagina-8-schrijfwerk vanaf dit nummer, maar er kwam niets binnen — voorbeeld blijft, uitnodiging open. Stuur je brief in!"
lt2 = "延期披露:VOL.1曾預告本期起刊登真實讀者來信和第8版最佳作文;截至截稿,本報未收到可刊登的真實來信與投稿,因此本期仍刊登編輯範例,並繼續公開徵集。你的來信,下一期見。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Lezershoek", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Zinnen van de week — woord voor woord uit de artikelen van dit nummer", 27, "sans", True, OLIVE)
quotes = [
    ("「用手機轉帳、掃碼付款、網上買保險，都是金融科技」", "Betaal met je telefoon, scan om te betalen, koop online een verzekering — dat is fintech.", "p. 1"),
    ("「123個國家及城市、1,600個攤位」", "123 landen en steden, 1.600 stands.", "p. 1"),
    ("「需要才買，不要為了折扣買一堆用不到的東西」", "Koop wat je nodig hebt; koop geen stapel dingen die je niet gebruikt alleen voor de korting.", "p. 2"),
    ("「在高雄，鋼鐵也能變成舞台」", "In Kaohsiung kan zelfs staal een podium worden.", "p. 3"),
    ("「福隆的夏天，在10月26日畫下句點」", "De zomer van Fulong kwam op 26 oktober ten einde.", "p. 3"),
    ("「6比0完封兄弟，龍隊拋下紅色彩帶」", "Een 6-0 shutout van de Brothers, en de Dragons gooiden de rode linten.", "p. 4"),
    ("「250家店家一起討糖」", "250 winkels die samen snoep uitdelen.", "p. 5"),
    ("「旅展首日中午12點才開門」", "Op de eerste dag van de beurs gaan de deuren pas om 12.00 uur open.", "p. 6"),
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
p.text(MX + 28, py + 44, "下期預告 · Volgende week (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "下週三雙11,你買了什麼?下週一旅展最後一天直擊,高雄鋼雕藝術節展到11月22日,還有你們的來信和第8版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
