# -*- coding: utf-8 -*-
# W46 zh-tw core, VOL.3: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-tw-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Taalfocus", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Drie niveaus, drie thema's")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 雙11的話 · Double 11-woorden", 24)
a.para("Double 11 geeft je vier nuttige woorden: 清單 (boodschappenlijst), 實付金額 (het eindbedrag dat je betaalt), 領券 (coupons claimen) en 鑑賞期 (de bedenktijd). Leer ze één keer en elke uitverkoop wordt begrijpelijk.", 21.5)
a.glossline("Vier Double 11-woorden: 清單, 實付金額, 領券, 鑑賞期.")
a.para("清單 is de lijst die je schrijft voor je winkelt. 實付金額 is wat je echt betaalt na kortingen. 領券 betekent een coupon claimen voor hij op is. 鑑賞期 is de 7 dagen na levering waarin je de meeste goederen kunt retourneren.", 21.5)
a.ex("A2", "完成句子", "清單", "Een boodschappenlijst is een 清單.",
     "買東西之前,先列___。", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "單選", "A", "De bedenktijd is 7 dagen.",
     "鑑賞期是幾天?", opts=["A. 7天", "B. 3天", "C. 14天"], size=20.5, gap=10)
a.ex("A2", "完成句子", "實付金額", "Vergelijk het eindbedrag dat je echt betaalt.",
     "比價要比___。", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Claim coupons voor ze op zijn.",
     "優惠券要怎麼拿?", opts=["A. 先領,領完就沒有了", "B. 不用領", "C. 過期再領"], size=20.5, gap=10)
a.para("Oefen: 「我的購物清單是什麼？」 ('Wat staat er op mijn boodschappenlijst?') — schrijf hem eerst op en vergelijk dan de prijzen.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 影展與鋼雕 · Film & staal", 24)
b.para("Film en staal delen de koppen van deze week. Groepeer de woorden en ze blijven hangen: film （入圍、頒獎、星光大道） en staal （鋼雕、保險箱、勞動記憶）.", 21.5)
b.glossline("Groepeer de woorden: film (入圍/頒獎), staal (鋼雕/保險箱).")
b.para("入圍 betekent genomineerd worden; 頒獎 betekent prijzen uitreiken. 星光大道 is de rode loper voor de ceremonie. 鋼雕 is een sculptuur van staal; 保險箱 is de kluis met Kaohsiungs herinneringen aan arbeid.", 21.5)
b.ex("B1", "完成句子", "入圍", "Genomineerd worden is 入圍.",
     "被選進最後的得獎名單,叫___。", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "單選", "A", "De ceremonie begint om 18:30 op 22 nov.",
     "金馬獎頒獎典禮幾點開始?", opts=["A. 晚上6點30分", "B. 下午2點", "C. 上午10點"], size=20.5, gap=10)
b.ex("B1", "完成句子", "鋼雕", "Sculptuur van staal is 鋼雕.",
     "用鋼鐵做的藝術,叫___。", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Het staalfestival sluit op 22 nov.",
     "鋼雕藝術節展到哪天?", opts=["A. 11月22日", "B. 11月15日", "C. 11月9日"], size=20.5, gap=10)
b.para("Geheugensteuntje: leer eerst 入圍 — dan de ceremonie （頒獎）, dan de plek waar hij plaatsvindt （星光大道）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 港台說法 · Lokaal taalgebruik", 24)
c.para("Taiwan en Hongkong hebben elk hun eigen manier van zeggen. Deze week: 打卡 (inchecken met een foto), 集點 (punten sparen), 遊行 (straatparade) en 感謝祭 (dankfestival voor fans).", 21.5)
c.glossline("Vier lokale woorden uit dit nummer: 打卡, 集點, 遊行, 感謝祭.")
c.para("打卡 op een beurs betekent een foto plaatsen om te zeggen 'ik was hier'. 集點 is punten verdienen elke keer dat je sport. 遊行 is de feestelijke optocht door de straten; 感謝祭 is het dankfestival van het team voor zijn fans.", 21.5)
c.ex("B2", "單選", "A", "集點 betekent punten sparen als je sport.",
     "「集點」是什麼意思?", opts=["A. 每次運動累積點數", "B. 買門票", "C. 上班簽到"], size=20.5, gap=10)
c.ex("B2", "完成句子", "遊行", "Een feestelijke optocht is 遊行.",
     "大家走上街頭慶祝,叫___。", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "單選", "A", "感謝祭 bedankt de fans.",
     "「感謝祭」是謝謝誰的活動?", opts=["A. 球迷", "B. 店員", "C. 記者"], size=20.5, gap=10)
c.ex("B2", "完成句子", "打卡", "Inchecken met een foto is 打卡.",
     "在嘉年華拍照分享,叫___。", instr="Vul in", size=20.5, gap=10)
c.para("Je hebt niet veel lokale uitdrukkingen nodig — leer er vier en elke uitstap voelt dichterbij.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「旅展在11月9日開幕」", "→「旅展在11月9日落幕,開幕是11月6日」", "De beurs opende 6 nov. en sloot 9 nov. Let op de tijdsrichting."),
    ("「金馬獎11月15日頒獎」", "→「金馬獎11月22日頒獎,11月15日是嘉年華」", "De ceremonie is 22 nov.; 15 nov. is de tweede carnavalsdag."),
    ("「滿5,000折800,實付5,800元」", "→「滿5,000折800,實付4,200元」", "Kortingen trek je af: 5.000 − 800 = 4.200, niet 5.800."),
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
wt = "「雙11不但有折扣,而且有免運。」 — Het patroon 不但…而且… betekent: niet alleen X, maar ook Y. Maak je eigen zin: 旅展不但有攤位,而且有表演 (niet alleen stands, maar ook shows)."
wcn = "Patroon: 不但…而且… — niet alleen X, maar ook Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Zinspatroon", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:雙11我的包裹到了!我買了一本書和一件外套,都沒有超過預算。週末我想去銅鑼灣看夜光巡遊,還想去高雄看鋼雕。——台北小讀者(編輯範例)」"
lcn = "Voorbeeldbrief van de redactie — geen echte brief. VOL.2 beloofde echte lezersbrieven en de beste pagina-8-teksten vanaf dit nummer; er was er geen publiceerbaar binnen voor de deadline. Het voorbeeld blijft, en de uitnodiging ook."
lt2 = "延期披露:VOL.2曾預告本期起刊登真實讀者來信和第8版最佳作文;截至截稿,本報未收到可刊登的真實來信與投稿,因此本期仍刊登編輯範例,並繼續公開徵集。你的來信,下一期見。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 40
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
    ("「先列清單,再比價,最後才結帳」", "Eerst de lijst, dan de prijzen vergelijken, dan betalen.", "p. 1"),
    ("「旅展四天,一次看完123個國家及城市」", "Vier dagen beurs, 123 landen en steden in één bezoek.", "p. 1"),
    ("「早晚溫差大,外套要隨身帶」", "Grote dag-nachtverschillen — houd een jas bij je.", "p. 2"),
    ("「金馬影展,就是一年一度的大電影課」", "Het Golden Horse-festival is één grote filmles per jaar.", "p. 3"),
    ("「保險箱裡,裝的是高雄的勞動記憶」", "In de kluis: Kaohsiungs herinneringen aan arbeid.", "p. 3"),
    ("「穿上紅色衣服,一起上街為龍隊喝采」", "Draag rood, ga de straat op, juich de Dragons toe.", "p. 4"),
    ("「嘉年華不用門票,全家人都能來玩」", "Geen ticket nodig — het hele gezin kan komen spelen.", "p. 5"),
    ("「回饋不是折價,實付金額才是真的」", "Cashback is geen korting — het betaalde bedrag telt.", "p. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 138
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 138 + 4  # fix 2026-11-03: was +18; teaser bottom crossed the footer rule (2586.36 > 2580)
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期預告 · Volgende week (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "下週日11月22日,三件大事同一天:封王遊行下午2點、金馬獎晚上6點30分、鋼雕藝術節閉幕,還有小雪、你們的來信和第8版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
