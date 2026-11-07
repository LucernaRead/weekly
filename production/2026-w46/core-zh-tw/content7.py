# -*- coding: utf-8 -*-
# W46 zh-tw core, VOL.3: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zhtw-core/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Language focus", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Three levels, three topics")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 雙11的話 · Double 11 words", 24)
a.para("Double 11 gives you four useful words: 清單 (shopping list), 實付金額 (the final amount you pay), 領券 (claiming coupons) and 鑑賞期 (the cooling-off period). Learn them once, and every sale makes sense.", 21.5)
a.glossline("Four Double 11 words: 清單, 實付金額, 領券, 鑑賞期.")
a.para("清單 is the list you write before you shop. 實付金額 is what you actually pay after discounts. 領券 means claiming a coupon before it runs out. 鑑賞期 is the 7 days after delivery when you can return most goods.", 21.5)
a.ex("A2", "完成句子", "清單", "A shopping list is a 清單.",
     "買東西之前,先列___。", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "單選", "A", "The cooling-off period is 7 days.",
     "鑑賞期是幾天?", opts=["A. 7天", "B. 3天", "C. 14天"], size=20.5, gap=10)
a.ex("A2", "完成句子", "實付金額", "Compare the final amount you actually pay.",
     "比價要比___。", instr="Fill in", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Claim coupons before they run out.",
     "優惠券要怎麼拿?", opts=["A. 先領,領完就沒有了", "B. 不用領", "C. 過期再領"], size=20.5, gap=10)
a.para("Practise: 「我的購物清單是什麼？」 ('What is on my shopping list?') — write it first, then compare prices.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 影展與鋼雕 · Film & steel", 24)
b.para("Film and steel share this week's headlines. Group the words and they stick: film （入圍、頒獎、星光大道） and steel （鋼雕、保險箱、勞動記憶）.", 21.5)
b.glossline("Group the words: film (入圍/頒獎), steel (鋼雕/保險箱).")
b.para("入圍 means being nominated; 頒獎 means presenting the awards. 星光大道 is the red carpet before the ceremony. 鋼雕 is sculpture made of steel; 保險箱 is the safe that holds Kaohsiung's labour memories.", 21.5)
b.ex("B1", "完成句子", "入圍", "Being nominated is 入圍.",
     "被選進最後的得獎名單,叫___。", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "單選", "A", "The ceremony starts at 18:30 on Nov 22.",
     "金馬獎頒獎典禮幾點開始?", opts=["A. 晚上6點30分", "B. 下午2點", "C. 上午10點"], size=20.5, gap=10)
b.ex("B1", "完成句子", "鋼雕", "Sculpture made of steel is 鋼雕.",
     "用鋼鐵做的藝術,叫___。", instr="Fill in", size=20.5, gap=10)
b.ex("B1", "單選", "A", "The steel festival closes Nov 22.",
     "鋼雕藝術節展到哪天?", opts=["A. 11月22日", "B. 11月15日", "C. 11月9日"], size=20.5, gap=10)
b.para("Memory trick: learn 入圍 first, then the ceremony （頒獎）, then the place it happens （星光大道）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 港台說法 · Local talk", 24)
c.para("Taiwan and Hong Kong each have their own way of saying things. This week: 打卡 (check in with a photo), 集點 (collecting points), 遊行 (street parade) and 感謝祭 (fans' thanksgiving festival).", 21.5)
c.glossline("Four local words from this issue: 打卡, 集點, 遊行, 感謝祭.")
c.para("打卡 at a fair means posting a photo to say 'I was here'. 集點 is earning points each time you exercise. 遊行 is the celebration march through the streets; 感謝祭 is the team's thank-you festival for its fans.", 21.5)
c.ex("B2", "單選", "A", "集點 means collecting points when you exercise.",
     "「集點」是什麼意思?", opts=["A. 每次運動累積點數", "B. 買門票", "C. 上班簽到"], size=20.5, gap=10)
c.ex("B2", "完成句子", "遊行", "A celebration march is 遊行.",
     "大家走上街頭慶祝,叫___。", instr="Fill in", size=20.5, gap=10)
c.ex("B2", "單選", "A", "感謝祭 thanks the fans.",
     "「感謝祭」是謝謝誰的活動?", opts=["A. 球迷", "B. 店員", "C. 記者"], size=20.5, gap=10)
c.ex("B2", "完成句子", "打卡", "Checking in with a photo is 打卡.",
     "在嘉年華拍照分享,叫___。", instr="Fill in", size=20.5, gap=10)
c.para("You don't need many local sayings — learn four and every outing feels closer.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「旅展在11月9日開幕」", "→「旅展在11月9日落幕,開幕是11月6日」", "The fair opened Nov 6 and closed Nov 9. Check the direction of time."),
    ("「金馬獎11月15日頒獎」", "→「金馬獎11月22日頒獎,11月15日是嘉年華」", "The ceremony is Nov 22; Nov 15 is the carnival's second day."),
    ("「滿5,000折800,實付5,800元」", "→「滿5,000折800,實付4,200元」", "Discounts subtract: 5,000 − 800 = 4,200, not 5,800."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所 · Error clinic", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「雙11不但有折扣,而且有免運。」 — the frame 不但…而且… joins two good things: not only X, but also Y. Make your own: 旅展不但有攤位,而且有表演 (not only booths, but also shows)."
wcn = "Frame: 不但…而且… — not only X, but also Y. Make your own sentence with it."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Sentence frame", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:雙11我的包裹到了!我買了一本書和一件外套,都沒有超過預算。週末我想去銅鑼灣看夜光巡遊,還想去高雄看鋼雕。——台北小讀者(編輯範例)」"
lcn = "An editor's example letter — not a real one. Deferral notice: VOL.2 promised real letters and best page-8 writing from this issue; none publishable had arrived by press time, so the example stays and the invitation stays open."
lt2 = "延期披露:VOL.2曾預告本期起刊登真實讀者來信和第8版最佳作文;截至截稿,本報未收到可刊登的真實來信與投稿,因此本期仍刊登編輯範例,並繼續公開徵集。你的來信,下一期見。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Readers' corner", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Phrases of the week — word for word from this issue's articles", 27, "sans", True, OLIVE)
quotes = [
    ("「先列清單,再比價,最後才結帳」", "List first, compare prices, then pay.", "p. 1"),
    ("「旅展四天,一次看完123個國家及城市」", "Four days of fair, 123 countries and cities in one visit.", "p. 1"),
    ("「早晚溫差大,外套要隨身帶」", "Big day-night temperature gaps — keep a jacket with you.", "p. 2"),
    ("「金馬影展,就是一年一度的大電影課」", "The Golden Horse festival is one big film class a year.", "p. 3"),
    ("「保險箱裡,裝的是高雄的勞動記憶」", "Inside the safe: Kaohsiung's labour memories.", "p. 3"),
    ("「穿上紅色衣服,一起上街為龍隊喝采」", "Wear red, take to the streets, cheer the Dragons.", "p. 4"),
    ("「嘉年華不用門票,全家人都能來玩」", "No ticket needed — the whole family can come and play.", "p. 5"),
    ("「回饋不是折價,實付金額才是真的」", "Cashback is not a discount — the amount paid is what counts.", "p. 6"),
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
p.text(MX + 28, py + 44, "下期預告 · Next week (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "下週日11月22日,三件大事同一天:封王遊行下午2點、金馬獎晚上6點30分、鋼雕藝術節閉幕,還有小雪、你們的來信和第8版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
