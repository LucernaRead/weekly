# -*- coding: utf-8 -*-
# W46 zh-tw core, VOL.3, issue week Mon 2026-11-09 to Sun 2026-11-15.
# All target text written natively for the Taiwan / Hong Kong ecosystem.
# W45 promises honoured: ITF final day (Nov 9) + Double 11 (Nov 11) full
# coverage, steel festival closing stretch, readers' letters disclosure.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zhtw-core/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P1 · front
CURPAGE[0] = 1
p = BSPage4()
p.text(975, 218, "Lucerna", 168, "serif", True, INK, anchor="middle", family="UnifrakturMaguntia")
p.hline(MX, RIGHT, 268, INK, 3)
p.text(975, 316, "繁體中文版 · VOL.3 · 2026年11月9日(一)至11月15日(日) · 台灣 / 香港", 27, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 340, GOLD, 2)
p.text(975, 378, "繁體中文正文 · 英語講解 — Traditional Chinese text · Explanations in English · the edition for English-speaking readers", 21, "sans", True, OLIVE, anchor="middle")
p.text(975, 410, "雙11購物節 · 旅展落幕 · 藝趣嘉年華——本週台港最熱的三件事", 30, "sans", True, BRICK, anchor="middle")
hl = "雙11來了!旅展落幕,購物車先列好"
p.text(975, 518, hl, 96, "serif", True, INK, anchor="middle")
if text_w(hl, "serif", True, 96) > RIGHT - MX:
    print("  !! P1 HEADLINE TOO WIDE", text_w(hl, "serif", True, 96))
p.text(975, 572, "週三11月11日全年最大檔 · 旅展123國、1600攤 · 週末銅鑼灣免費嘉年華", 27, "serif", False, GREY, anchor="middle")

f = Flow(p, [(COLX[0], 3 * CW + 2 * GUT)], 640, 1935, tag="P1-lead")
f.title("旅展週一落幕,四天一次看完世界", 40)
f.byline("Staff report · Source: Taiwan Visitors Association announcements and press reports (Oct 16-27)")
f.para("2026 ITF 台灣國際旅展,週一(11月9日)在台北南港展覽館一館落幕。旅展四天,一次看完123個國家及城市,1,600個攤位,從機票、飯店、餐券,到郵輪、南極行程,一次看完。今年旅展邁入第40年、第34屆,正式改名「ITF 台灣國際旅展」,主題是「世界旅人,台灣啟程」。")
f.para("四天裡,大會舞台有多國文化展演,每日下午2點有吉祥物大遊行。旅展不只在現場:部分航空公司的線上旅展延長到11月中下旬,在家也能比價。買票、買券之前,要先看清楚使用日期和條件,不要只看折扣有多大。")
f.gloss("The 2026 ITF Taiwan International Travel Fair closed Monday (Nov 9) at the Nangang Exhibition Center: 123 countries and cities, 1,600 booths over four days. In its 40th year and 34th edition, the fair took the new name ITF Taiwan International Travel Fair. Some airlines' online fairs run into mid-to-late November — check dates and terms before you buy.")
f.title("週三雙11,全年最大購物檔", 40)
f.para("週三(11月11日)是雙11,各大電商早就開始暖身。蝦皮購物今年和長榮航空合作,從10月26日到11月13日,連續19天抽出23張來回機票,11月11日當天抽出洛杉磯來回機票兩張。先列清單,再比價,最後才結帳,才是聰明買法。")
f.para("折扣、回饋、免運,常常不能同時用。領券要先看門檻和名額:有的券先領先用,領完就沒有了。比價要比「實付金額」,也就是最後真正付出去的錢,不是只看折扣數字有多大。")
f.gloss("Double 11 falls on Wednesday (Nov 11). Shopee's draw with EVA Air runs Oct 26-Nov 13: 23 return tickets over 19 days, with two Los Angeles return tickets on Nov 11 itself. Discounts, cashback and free delivery often cannot be combined — compare the final amount you actually pay, and check each coupon's threshold and quota first.")
f.end_report()

rx = COLX[3]
by = 640
p.rect(rx, by, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "旅展四天小檔 · Fair file", 25, "sans", True, OLIVE); yy += 56
for t in [
    "日期:11月6日(五)到11月9日(一)",
    "地點:台北南港展覽館一館1樓、4樓",
    "規模:123個國家及城市、1,600個攤位",
    "門票:預售180元,現場200元",
    "時間:首日中午12點開門,其餘10點到18點",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
by2 = by + 488
p.rect(rx, by2, CW, 560, fill=BOX, stroke=LINE, sw=1.4)
yy = by2 + 18
p.text(rx + 22, yy + 26, "本週大事 · This week", 25, "sans", True, OLIVE); yy += 58
for t in [
    "週一 11/9 旅展最後一天,18:00閉幕",
    "週三 11/11 雙11購物節,全年最大檔",
    "週五 11/13 香港圓方體能競技場開賽",
    "週六 11/14 銅鑼灣藝趣嘉年華開幕",
    "週六 11/14 鋼雕藝術節週末節目登場",
    "週日 11/15 藝趣嘉年華第二天",
    "下週日 11/22 金馬獎、封王遊行、鋼雕閉幕",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.3) + 9
by3 = by2 + 578
p.rect(rx, by3, CW, 250, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by3 + 18
p.text(rx + 22, yy + 26, "本週一詞 · Word of the week", 25, "sans", True, OLIVE); yy += 56
p.para(rx + 22, yy + 21, "「實付金額」 — the final amount you actually pay, after discounts and coupons. Compare this number, not the discount headline.", 20, "sans", False, GREY, CW - 44, 1.35)

q = Flow(p, [(COLX[i], CW) for i in range(4)], 2035, 2540, tag="P1-quiz")
q.head("快速測驗 · Quick quiz", 26)
q.ex("A2", "單選", "B", "The travel fair closed Monday, Nov 9.",
     "台北旅展哪天落幕?", opts=["A. 週日", "B. 週一(11月9日)", "C. 週三"], size=22.5, gap=8)
q.ex("A2", "單選", "A", "The fair gathers 123 countries and cities.",
     "旅展集結幾個國家及城市?", opts=["A. 123個", "B. 23個", "C. 1,600個"], size=22.5, gap=8)
q.ex("A2", "單選", "C", "Double 11 is Wednesday, Nov 11.",
     "雙11是星期幾?", opts=["A. 週一", "B. 週五", "C. 週三(11月11日)"], size=22.5, gap=8)
q.ex("A2", "單選", "B", "The mascot parade runs daily at 14:00.",
     "旅展吉祥物大遊行每天幾點?", opts=["A. 中午12點", "B. 下午2點", "C. 晚上7點"], size=22.5, gap=8)
q.head("標題填空 · Headline words", 26)
q.ex("A2", "完成句子", "1,600", "The travel fair has 1,600 booths.",
     "台北旅展有___個攤位。", instr="Fill in", size=22.5, gap=8)
q.ex("A2", "完成句子", "200", "On-site tickets cost NT$200.",
     "旅展現場票是___元。", instr="Fill in", size=22.5, gap=8)
q.ex("A2", "完成句子", "23", "23 return tickets are drawn over 19 days.",
     "蝦皮和長榮航空一共抽出___張來回機票。", instr="Fill in", size=22.5, gap=8)
q.ex("A2", "完成句子", "19", "The ticket draw runs 19 days.",
     "抽機票活動一連___天。", instr="Fill in", size=22.5, gap=8)
q.ex("A2", "完成句子", "實付金額", "Compare the final amount you actually pay.",
     "比價要比___。", instr="Fill in", size=22.5, gap=8)
q.ex("A2", "完成句子", "清單", "List your shopping list first, then compare prices.",
     "買東西之前,先列___。", instr="Fill in", size=22.5, gap=8)
q.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ============================================================ P2 · life
CURPAGE[0] = 2
p = BSPage4()
p.band("生活 · Life", "Lucerna", "第 2 版 · 東北季風、泡湯、雙11退貨 · Monsoon rain, hot springs and 11.11 returns")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P2-main")
f.title("北台灣濕涼到雙11,外套隨身帶", 34)
f.para("東北季風一波接一波,北台灣這週又濕又涼。氣象專家提醒,北北基宜一路濕涼到11月11日,白天高溫只有24到27度,清晨和夜間低溫會跌破20度。早晚溫差大,外套要隨身帶,出門也要記得帶傘。")
f.para("高雄就不一樣了:白天高溫28到30度,夜間22到25度,天氣舒適,只是日夜溫差也大。南北天氣差很多,出門旅行之前,先查目的地的天氣,不要只看台北的預報就打包行李。")
f.gloss("The northeast monsoon keeps northern Taiwan wet and cool into Nov 11: daytime highs of 24-27 degrees, lows below 20 at night and in the early morning. Kaohsiung stays warm at 28-30 degrees by day. Check the forecast for your destination before you pack.")
f.title("秋冬泡湯,安全第一", 34)
f.para("天氣轉涼,泡湯的人多了。泡湯之前,先吃一點東西,不要空腹,也不要吃太飽。泡湯時間不要太長,覺得頭暈、心跳很快,就要馬上起來休息。心臟不好、血壓不穩的人,泡湯之前先問醫生。")
f.para("泡湯也要看水質和衛生:先沖澡再下水,不要在池裡搓洗身體。毛巾不要放進池水裡。泡完湯,記得多喝水,讓身體慢慢回溫。")
f.gloss("Hot-spring season is here. Eat a little first, keep soaks short, and get out at once if you feel dizzy. Shower before entering the pool, keep towels out of the water, and drink water afterwards.")
f.title("雙11買了不合用?退貨有規則", 34)
f.para("雙11買東西,最怕買了不合用。台灣的消保法有7天鑑賞期:收到商品7天內,可以退貨。但是,有些商品是例外,例如拆封就不能退的個人衛生用品、容易壞的生鮮食品,買之前要先看清楚。")
f.box("練習例子 · Practice example", [
    ("小美在雙11買了一件外套3,000元,收到後發現尺寸不合。她在7天內申請退貨,外套沒有拆吊牌,店家讓她退貨,她拿回3,000元。", "serif", False, INK, 22, 1.4),
    ("Practice numbers: NT$3,000 coat, returned within 7 days with the tag on — full refund of NT$3,000.", "sans", False, GREY, 19.5, 1.35),
])
f.head("讀懂了嗎? · Did you get it?", 28)
f.ex("A2", "單選", "A", "Northern Taiwan stays wet and cool to Nov 11.",
     "北台灣濕涼的天氣會持續到哪天?", opts=["A. 11月11日", "B. 11月6日", "C. 11月22日"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "Lows fall below 20 degrees in the north.",
     "北台灣清晨和夜間低溫大約幾度?", opts=["A. 25度以上", "B. 跌破20度", "C. 30度"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "Kaohsiung stays 28-30 degrees by day.",
     "高雄白天高溫大約幾度?", opts=["A. 28到30度", "B. 20到22度", "C. 15度"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "Get out at once if you feel dizzy in the pool.",
     "泡湯覺得頭暈,應該怎麼做?", opts=["A. 繼續泡", "B. 馬上起來休息", "C. 泡更久"], size=22.5, gap=8)
f.ex("A2", "單選", "C", "The cooling-off period is 7 days.",
     "台灣消保法的鑑賞期是幾天?", opts=["A. 3天", "B. 14天", "C. 7天"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "Check the exceptions before you buy.",
     "買東西之前,要先看清楚什麼?", opts=["A. 退貨例外和條件", "B. 店員的名字", "C. 包裝顏色"], size=22.5, gap=8)
f.head("填一填 · Fill in", 28)
f.ex("A2", "完成句子", "東北季風", "The northeast monsoon brings wet, cool weather.",
     "北台灣變濕變涼,是___的影響。", instr="Fill in", size=22.5, gap=8)
f.ex("A2", "完成句子", "外套", "Mornings and evenings are cool: bring a jacket.",
     "早晚溫差大,___要隨身帶。", instr="Fill in", size=22.5, gap=8)
f.ex("A2", "完成句子", "泡湯", "Hot springs are popular as the weather cools.",
     "天氣轉涼,___的人多了。", instr="Fill in", size=22.5, gap=8)
f.ex("A2", "完成句子", "鑑賞期", "The 7-day cooling-off period.",
     "收到商品7天內可以退貨,叫___。", instr="Fill in", size=22.5, gap=8)
f.ex("A2", "完成句子", "吊牌", "Keep the tag on for a return.",
     "退貨的外套不能拆___。", instr="Fill in", size=22.5, gap=8)
f.ex("A2", "完成句子", "預報", "Check the destination forecast before packing.",
     "旅行之前,先查目的地的天氣___。", instr="Fill in", size=22.5, gap=8)
f.head("算一算 · Work it out", 28)
f.ex("A2", "單選", "B", "3,000 refunded in full: 3,000 − 0 = 3,000.",
     "練習:外套3,000元全額退貨,小美拿回多少?", opts=["A. 0元", "B. 3,000元", "C. 1,500元"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "27 − 20 = 7 degrees of difference.",
     "北台灣白天27度、低溫20度,溫差幾度?", opts=["A. 7度", "B. 47度", "C. 2度"], size=22.5, gap=8)
f.match_set("A2", "配對",
            ["東北季風", "溫差", "泡湯", "鑑賞期"],
            ["從東北方吹來的涼風", "白天和夜間的溫度差", "去溫泉洗澡、放鬆", "收到商品後可以退貨的天數"],
            ["a", "b", "c", "d"],
            ["東北季風 — the northeast monsoon.",
             "溫差 — the temperature difference.",
             "泡湯 — soaking in a hot spring.",
             "鑑賞期 — the cooling-off period."],
            instr="Match")
f.end_report()

rx = COLX[3]
image(p, "rain.jpg", rx, 208, CW, 300)
caption(p, rx, 208 + 300 + 6, CW, "秋雨綿綿,出門記得帶傘(資料照片)。北台灣本週又濕又涼。",
        "Photo: CorraleH — CC0 (Wikimedia Commons)")
by = 208 + 300 + 96
p.rect(rx, by, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "事實框 · This week's facts", 24, "sans", True, OLIVE); yy += 56
for t in [
    "北北基宜:濕涼到11月11日,低溫跌破20度",
    "高雄:白天28到30度,夜間22到25度",
    "雙11:週三11月11日,先領券、比實付金額",
    "鑑賞期:收到商品7天內可退貨,例外先看清",
    "泡湯:先沖澡再下水,頭暈馬上起來",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 250, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢? · Over to you", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你喜歡泡湯嗎?雙11你買了什麼?退過貨嗎?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Do you like hot springs? What did you buy on Double 11? Have you ever returned something?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 488 + 250 + 18
p.rect(rx, by3, CW, 460, fill=BOX, stroke=LINE, sw=1.4)
yy = by3 + 18
p.text(rx + 22, yy + 26, "退貨前先看 · Before you return", 25, "sans", True, OLIVE); yy += 56
for t in [
    "7天內申請退貨,商品要保持完整",
    "吊牌不要拆,包裝盡量留好",
    "個人衛生用品拆封,可能不能退",
    "生鮮食品容易壞,例外要先看",
    "跨境包裹2,000元以下免稅,超過要補稅",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.foot(2)
p.save(f"{OUT}/p2-life.svg")
print("P2 saved, exercises so far:", len(REG))
