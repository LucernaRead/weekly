# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zhtw-vol1/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P5 · youth
CURPAGE[0] = 5
p = BSPage4()
p.band("青年 · Youth", "Lucerna", "第 5 版 · 金鐘獎雙夜與萬聖節地圖 · Golden Bell nights and the Halloween map")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P5-main")
f.title("金鐘獎61:連兩晚的電視大日子", 34)
f.para("台灣電視界最大的獎「金鐘獎」,今年第61屆,連辦兩晚:週五(10月23日)是節目類,主持人陳漢典;週六(10月24日)是戲劇類,主持人陳庭妮。地點都在台北流行音樂中心。")
f.para("兩晚都一樣:下午5點先走星光大道,晚上7點典禮開始。戲劇類的入圍名單裡,《我們與惡的距離 II》和《忘了我記得》各入圍13項,並列第一,是今年的大熱門。")
f.para("最熱鬧的是「最具人氣戲劇節目獎」:粉絲投票到週六下午5點截止,結果當晚在典禮上公佈。這週颱風靠近,主辦單位說,正密切注意天氣,兩晚典禮照常準備。")
f.gloss("The 61st Golden Bell Awards run two nights at the Taipei Music Center: programme awards on Friday, drama awards on Saturday. Two dramas lead with 13 nominations each, and the popularity vote closes at 17:00 on Saturday.")
f.title("萬聖節地圖 · 台灣:天母改期,桃園開城", 34)
f.para("台北天母的「天母搞什麼鬼」今年第18屆,原訂週五、週六舉行,因為薔琵颱風,10月19日宣佈改期:「百鬼夜行」討糖踩街改到週日(10月25日)晚上7點,從新光三越天母店出發,沿忠誠路二段走;主活動改到下週一(10月26日)在天母運動公園,下期再報。")
f.para("颱風改了日期,卻改不了大家過節的心情。今年有塔麻歌子30週年聯名,250家商圈店家免費討糖,三大百貨共發4,500個限量南瓜桶;往年參加人數超過30萬人次,整條街都是變裝的人。")
f.para("桃園萬聖城週六(10月24日)開城,做到11月1日:今年第一次和史努比(PEANUTS)聯名,有9座主題裝置,每晚還有動畫秀。六福村的「墓碑鎮」也開放到11月22日。")
f.title("萬聖節地圖 · 香港:哈囉喂開玩", 34)
f.para("香港海洋公園的「哈囉喂全園祭」做到11月1日,主題是「詭魅墓會」,由王嘉爾擔任創意總監。四大驚嚇體驗,驚嚇指數從5到5+;「日連夜」驚嚇場次這個週末連開三天(10月23日到25日),鬼屋下午5點開到晚上11點。香港迪士尼的萬聖節活動也做到11月1日;週六、週日晚上,還有萬聖節限定的電車和觀光巴士。")
f.gloss("In Hong Kong, Ocean Park's Halloween Fest runs scare nights this weekend (haunted houses 17:00-23:00), with Jackson Wang as creative director; Disney's Halloween Time also runs to Nov 1.")
f.head("讀懂了嗎? · Did you get it?", 28)
f.ex("B1", "單選", "A", "Programme awards are on Friday night.",
     "節目類金鐘獎在哪天頒?", opts=["A. 週五", "B. 週六", "C. 週日"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "The ceremony starts at 19:00; the red carpet is at 17:00.",
     "戲劇類典禮幾點開始?", opts=["A. 17:00", "B. 19:00", "C. 21:00"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "Each of the two leading dramas has 13 nominations.",
     "兩部領跑的戲劇,各入圍幾項?", opts=["A. 10項", "B. 13項", "C. 16項"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "Voting closes at 17:00 on Saturday.",
     "人氣獎投票什麼時候截止?", opts=["A. 週五19:00", "B. 週六17:00", "C. 週六19:00"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "The typhoon forced the Tianmu event to move.",
     "天母踩街為什麼改期?", opts=["A. 下大雨", "B. 颱風", "C. 人太多"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "The parade moved to Sunday at 19:00.",
     "踩街改到哪天幾點?", opts=["A. 週日19:00", "B. 週六19:00", "C. 週一19:00"], size=22.5, gap=8)
f.head("填一填 · Fill in", 28)
f.ex("B1", "完成句子", "陳庭妮", "Chen Ting-ni hosts the drama night.",
     "戲劇類金鐘獎的主持人是___。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "忠誠路", "The parade walks along Zhongcheng Road Section 2.",
     "踩街從天母店出發,沿___二段走。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "史努比", "Taoyuan's Halloween city teams up with Snoopy this year.",
     "桃園萬聖城今年和___聯名(那隻有名的卡通狗)。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "詭魅墓會", "The Grave Rave is this year's Ocean Park theme.",
     "海洋公園哈囉喂今年的主題是「___」。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "23", "The haunted houses close at 23:00.",
     "鬼屋從17:00開到晚上___:00。", instr="Fill in", size=22.5, gap=8)
f.match_set("B1", "配對",
            ["金鐘獎", "天母搞什麼鬼", "桃園萬聖城", "哈囉喂"],
            ["台北流行音樂中心,連辦兩晚", "踩街改到週日19:00", "史努比聯名,週六開城", "海洋公園,王嘉爾任創意總監"],
            ["a", "b", "c", "d"],
            ["金鐘獎 — two nights at the Taipei Music Center.",
             "天母搞什麼鬼 — its parade moved to Sunday 19:00.",
             "桃園萬聖城 — Snoopy tie-in, opens Saturday.",
             "哈囉喂 — Ocean Park's Halloween Fest, Jackson Wang directing."],
            instr="Match")
f.head("算一算 · Work it out", 28)
f.ex("B1", "完成句子", "26", "13 + 13 = 26 nominations between the two dramas.",
     "兩部戲的入圍項數加起來:13 + 13 = ___項。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "2", "From 17:00 to 19:00 is 2 hours.",
     "投票截止17:00到典禮開始19:00,相隔___小時。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "6", "17:00 to 23:00 is 6 hours of haunted houses.",
     "鬼屋17:00到23:00,一晚開___小時。", instr="Fill in", size=22.5, gap=8)
f.end_report()

rx = COLX[3]
image(p, "stage.jpg", rx, 208, CW, 290)
cy = caption(p, rx, 208 + 290 + 6, CW, "典禮開始前,觀眾等著紅幕升起(資料照片)。",
             "Photo: Kurt Kaiser — CC0 (Wikimedia Commons)")
iy2 = int(cy) + 18
image(p, "pumpkin.jpg", rx, iy2, CW, 290)
cy2 = caption(p, rx, iy2 + 290 + 6, CW, "南瓜燈準備好了,你呢?",
              "Photo: Benjamin Balazs — CC0 (Wikimedia Commons)")
by = int(cy2) + 18
p.rect(rx, by, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "週末行程 · Weekend plan", 25, "sans", True, OLIVE); yy += 56
for t in [
    "週五晚:金鐘獎節目類(北流)",
    "週六17:00:人氣獎投票截止",
    "週六晚:金鐘獎戲劇類,結果公佈",
    "週五到日:海洋公園驚嚇場次",
    "週日晚19:00:天母百鬼夜行踩街",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
wx, wy, ww = COLX[2], 1620, 2 * CW + GUT
p.rect(wx, wy, ww, 620, fill=BOX, stroke=LINE, sw=1.4)
yy = wy + 20
p.text(wx + 26, yy + 28, "週末行程表 · Weekend planner", 26, "sans", True, OLIVE); yy += 66
yy = p.para(wx + 26, yy + 22, "If the typhoon moves anything, check the latest announcement before you go out.", 20, "sans", False, GREY, ww - 52, 1.35) + 8
for t in [
    "週五 10/23:金鐘獎節目類(台北流行音樂中心)· 台灣大賽 G5(如有需要)· 海洋公園驚嚇場次",
    "週六 10/24:金鐘獎戲劇類 19:00 · 人氣獎 17:00 截止 · 桃園萬聖城開城 · 台灣大賽 G6(如有需要)",
    "週日 10/25:天母百鬼夜行踩街 19:00 · 台灣大賽 G7(如有需要)· 週年慶兩店最後一天",
    "下週一 10/26:天母主活動(天母運動公園)· 福隆沙雕最後一天 —— 下期報導",
]:
    yy = p.para(wx + 26, yy + 25, "· " + t, 23, "serif", False, INK, ww - 52, 1.4) + 10
p.foot(5)
p.save(f"{OUT}/p5-youth.svg")
print("P5 saved, exercises so far:", len(REG))

# ============================================================ P6 · deep read
CURPAGE[0] = 6
p = BSPage4()
p.band("深讀 · Deep read", "Lucerna", "第 6 版 · 美酒佳餚巡禮倒數 · Counting down to the Wine & Dine Festival")
f = Flow(p, [(COLX[0], 3 * CW + 2 * GUT)], 208, 1150, tag="P6-lead")
f.title("美酒佳餚巡禮:三百多個攤位,把世界搬到海邊", 38)
f.byline("Staff report · Sources: Hong Kong Tourism Board, the HKTB event pages and Hong Kong media guides (October 2026)")
f.para("下週四(10月29日),香港旅發局的旗艦活動「美酒佳餚巡禮」在中環海濱活動空間和添馬公園開幕,做到11月1日(日)。今年的主題是「品味世界之最」:逾340個攤位、約31個國家及地區參加。三百四十多個攤位,把世界搬到海邊——走一圈,等於環遊世界吃一遍。")
f.para("今年有兩個第一次:第一次設「品酒導賞路線」,有人帶你一攤一攤喝、一攤一攤吃;星期五、六的晚上,今年第一次開到凌晨一時,海邊的晚餐可以慢慢吃。門票10月12日起公開發售,這個星期是最後搶票期。")
f.para("最大的話題,是兩位韓國《黑白大廚》名廚來港。Edward Lee 參加10月30日的「歲月之味」十手聯乘晚宴,每位2,380港幣;崔鉉碩10月31日和香港主廚溫有成做四手聯乘午宴,每位1,580港幣。名廚的場次票最少,想吃要先搶。")
f.gloss("Hong Kong's Wine & Dine Festival opens next Thursday at the Central Harbourfront: 340+ booths from about 31 places, guided tasting routes for the first time, and two star-chef events that sell out first.")
f.end_report()

# ---- chart: ticket prices, bars drawn from zero, exactly proportional ----
chy = 1030
p.hline(MX, COLX[0] + 3 * CW + 2 * GUT, chy - 18, GOLD, 2)
p.text(MX, chy + 28, "門票一覽 · Ticket prices (HK$) — bars drawn in proportion to the price", 27, "sans", True, OLIVE)
rows = [("入場券", 40, GOLD), ("品味券(單張)", 25, GOLD), ("品味證", 258, OLIVE), ("尊尚品酒證", 558, OLIVE)]
BX = MX + 215           # bar origin (the zero line)
SCALE = 1.8             # px per HK$
ry = chy + 58
p.add(f'<line x1="{BX}" y1="{ry - 8}" x2="{BX}" y2="{ry + 4 * 54 - 22}" stroke="#57523f" stroke-width="1.6"/>')
for label, val, colr in rows:
    p.text(BX - 16, ry + 26, label, 23, "serif", True, INK, anchor="end")
    p.rect(BX, ry, val * SCALE, 34, fill=colr)
    p.text(BX + val * SCALE + 14, ry + 26, f"HK${val}", 23, "sans", True, INK)
    ry += 54
for tick in (0, 200, 400):
    tx = BX + tick * SCALE
    p.add(f'<line x1="{tx}" y1="{ry - 30}" x2="{tx}" y2="{ry - 22}" stroke="#57523f" stroke-width="1.6"/>')
    p.text(tx, ry + 4, str(tick), 19, "sans", False, GREY, anchor="middle")
p.para(MX, ry + 30, "Source: ticket prices published by the HKTB. Both passes include tasting tokens and a wine glass; the right-hand column breaks down which pass is better value.", 20, "sans", False, GREY, 3 * CW + 2 * GUT, 1.35)
chart_end = ry + 66

e = Flow(p, [(COLX[i], CW) for i in range(3)], int(chart_end) + 26, 2540, tag="P6-ex")
e.head("看圖答題 · Read the chart", 28)
e.ex("B2", "單選", "B", "The pass bundles items worth HK$400 in total.",
     "品味證的內容總值是多少?", opts=["A. 258港幣", "B. 400港幣", "C. 640港幣"], size=22.5, gap=8)
e.ex("B2", "單選", "B", "400 - 258 = 142 saved against buying separately.",
     "買品味證,比逐樣買省多少?", opts=["A. 82港幣", "B. 142港幣", "C. 200港幣"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "Eight HK$25 tasting tokens make the HK$200 part.",
     "品味證裡有幾張品味券?", opts=["A. 8張", "B. 16張", "C. 25張"], size=22.5, gap=8)
e.ex("B2", "單選", "B", "558 - 258 = 300 Hong Kong dollars.",
     "尊尚品酒證比品味證貴多少?", opts=["A. 258港幣", "B. 300港幣", "C. 558港幣"], size=22.5, gap=8)
e.ex("B2", "完成句子", "800", "2,380 - 1,580 = 800 Hong Kong dollars.",
     "兩場名廚活動:晚宴2,380元、午宴1,580元,相差___元。", instr="Fill in", size=22.5, gap=8)
e.head("讀懂了嗎? · Did you get it?", 28)
e.ex("B2", "單選", "A", "The festival is at the Central Harbourfront and Tamar Park.",
     "活動在哪裡舉行?", opts=["A. 中環海濱", "B. 尖沙咀", "C. 香港迪士尼"], size=22.5, gap=8)
e.ex("B2", "單選", "B", "Oct 29 to Nov 1 is 4 days.",
     "活動一共幾天?", opts=["A. 3天", "B. 4天", "C. 5天"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "Guided tasting routes are new this year.",
     "今年第一次推出什麼?", opts=["A. 品酒導賞路線", "B. 夜市小吃街", "C. 海上煙火"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "Edward Lee's ten-hand dinner is on Oct 30.",
     "Edward Lee 的晚宴在哪天?", opts=["A. 10月30日", "B. 10月31日", "C. 11月1日"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "Choi Hyun-seok cooks lunch with Wan Yau-shing.",
     "崔鉉碩的午宴和誰聯乘?", opts=["A. 溫有成", "B. Edward Lee", "C. 王嘉爾"], size=22.5, gap=8)
e.head("填一填 · Fill in", 28)
e.ex("B2", "完成句子", "世界", "The theme is 'Taste the Best of the World'.",
     "今年的主題是「品味___之最」。", instr="Fill in", size=22.5, gap=8)
e.ex("B2", "完成句子", "340", "More than 340 booths take part.",
     "參加的攤位逾___個。", instr="Fill in", size=22.5, gap=8)
e.ex("B2", "完成句子", "1", "Friday and Saturday nights now run to 1 a.m.",
     "週五、六晚延長至凌晨___:00。", instr="Fill in", size=22.5, gap=8)
e.ex("B2", "完成句子", "12", "Tickets went on sale on Oct 12.",
     "門票從10月___日起公開發售。", instr="Fill in", size=22.5, gap=8)
e.match_set("B2", "配對",
            ["入場券", "品味券", "品味證", "尊尚品酒證"],
            ["40元,只入場", "25元一張,換飲品和小食", "258元,含券和標準酒杯", "558元,含尊尚名酒區入場券"],
            ["a", "b", "c", "d"],
            ["入場券 — HK$40, admission only.",
             "品味券 — HK$25 each, swapped for drinks and snacks.",
             "品味證 — HK$258, tokens and a standard glass included.",
             "尊尚品酒證 — HK$558, with the grand tasting lounge pass."],
            instr="Match")
e.end_report()

rx = COLX[3]
image(p, "harbour.jpg", rx, 208, CW, 250)
cy = caption(p, rx, 208 + 250 + 6, CW, "維多利亞港邊的中環海濱,下週四起擺滿攤位。",
             "Photo: Wilfredor — CC0 (Wikimedia Commons)")
iy2 = int(cy) + 16
image(p, "wine.jpg", rx, iy2, CW, 250)
cy2 = caption(p, rx, iy2 + 250 + 6, CW, "美酒配小食,是巡禮的主角。",
              "Photo: Jon Sullivan — Public domain (Wikimedia Commons)")
by = int(cy2) + 16
p.rect(rx, by, CW, 504, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "票券拆解 · Pass breakdown", 23, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 21, "The 品味證 (tasting pass) costs HK$258 and bundles HK$400 of items: admission HK$40 + 8 tasting tokens HK$200 + a standard wine glass HK$160 — a saving of HK$142.", 20.5, "sans", False, INK, CW - 44, 1.38) + 6
yy = p.para(rx + 22, yy + 21, "The 尊尚品酒證 (premium pass) costs HK$558 and bundles HK$900: admission HK$40 + 16 tokens HK$400 + the premium glass HK$260 + premium-zone entry and e-vouchers HK$200 — a saving of HK$342.", 20.5, "sans", False, INK, CW - 44, 1.38) + 6
p.para(rx + 22, yy + 20, "Contents valued from the official ticket breakdown; the savings are our arithmetic.", 19.5, "sans", False, GREY, CW - 44, 1.32)
sy = by + 522
p.text(rx, sy + 28, "副篇:週年慶的兩種買法", 25, "sans", True, OLIVE)
p.hline(rx, rx + CW, sy + 42, GOLD, 2)
yy = p.para(rx, sy + 42 + 26, "今年週年慶有兩個畫面:一邊,工商時報點名首日熱賣品是 iPhone 18 Pro Max 和 Apple Watch 12,高價 3C 第一天就賣得最好;另一邊,更多人拿著攻略算滿千送百,一千元、一千元地湊。有人說,這叫「K 型消費」。", 22, "serif", False, INK, CW, 1.42)
yy = p.para(rx, yy + 26, "熱度看數字:新光三越首波六店,開賣第一天業績破 15.5 億元新台幣,來客逾 14.5 萬人次;信義新天地的寶可夢遊行,預購期單日就吸了 31 萬人次。", 22, "serif", False, INK, CW, 1.42)
p.para(rx, yy + 24, "Two ways to shop the sale: big-ticket tech sells out on day one, while everyone else counts coupons to the last hundred dollars.", 19.5, "sans", False, GREY, CW, 1.32)
p.foot(6)
p.save(f"{OUT}/p6-deep.svg")
print("P6 saved, exercises so far:", len(REG))
