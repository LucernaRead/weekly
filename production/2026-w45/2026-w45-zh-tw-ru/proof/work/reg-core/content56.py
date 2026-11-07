# -*- coding: utf-8 -*-
# W45 zh-tw core, VOL.2: P5 youth, P6 deep read.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations//home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-tw-ru-proof/work/reg-core/svg/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P5 · youth
CURPAGE[0] = 5
p = BSPage4()
p.band("青年 · Youth", "Lucerna", "第 5 版 · 天母萬聖節回顧、旅展攻略 · Halloween recap and the travel-fair game plan")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P5-main")
f.title("天母萬聖節回顧:討糖、踩街、南瓜桶", 34)
f.para("上週的天母很熱鬧。第18屆「天母搞什麼鬼」原訂10月24日辦主活動,受到颱風影響,改成兩天:10月25日(週日)晚上7點,百鬼夜行討糖踩街從新光三越台北天母店出發,沿著忠誠路二段走到大葉高島屋;10月26日(週一)下午1點到晚上8點,主活動在天母運動公園登場。")
f.para("討糖是重點:250家店家一起討糖,三大百貨在10月26日下午1點同步發放4,500個限量南瓜桶。今年還跟日本人氣角色塔麻歌子30週年合作,很多大小朋友穿上萬聖裝扮,到店家喊一聲 Trick or Treat,就能拿到糖果。")
f.gloss("Tianmu's Halloween (Oct 25-26, postponed from Oct 24 by the typhoon): the Oct 25 night parade marched from Shin Kong Mitsukoshi Tianmu along Zhongcheng Road to Dayeh Takashimaya, and the Oct 26 main event ran 13:00-20:00 at Tianmu Sports Park, with 250 shops giving treats and 4,500 pumpkin buckets from three department stores.")
f.title("旅展青年攻略:先看表演,再比價", 34)
f.para("週五旅展開幕,年輕人怎麼逛?先看表演:大會舞台有多國文化展演,包括日本山形花笠舞、韓國觀光公社帶來的跆拳道與喜劇武術表演《JUMP》;每日下午2點,吉祥物大遊行準時出發,還能參加粉絲見面會。")
f.para("再比價:機票優惠要看清楚。廉航最低票價通常不含託運行李,加上行李費,價差可能縮小,甚至反轉。報導整理的例子:國泰航空東京來回含稅13,433元起,購票到11月13日。所有價格都以實際訂票結果為準,不同日期價格不同。")
f.gloss("Travel-fair game plan: watch the shows first (Yamagata flower-hat dance, Korea's JUMP taekwondo-comedy show, the daily 14:00 mascot parade), then compare prices — budget fares often exclude checked baggage, so add that cost before you decide.")
f.title("雙11:購物車先列好", 34)
f.para("下週三就是雙11。聰明的做法是:這週先把購物車列好,刪掉不需要的,留下真正要買的;設好預算,超過預算的東西,先放一邊。折扣會過去,帳單會留下來。")
f.box("練習例子 · Practice example", [
    ("小林的購物車一共6,200元,預算只有5,000元。他刪掉一件1,200元的外套,購物車變成5,000元,正好符合預算。", "serif", False, INK, 22, 1.4),
    ("Practice numbers: NT$6,200 − NT$1,200 = NT$5,000, exactly his budget.", "sans", False, GREY, 19.5, 1.35),
])
f.head("讀懂了嗎? · Did you get it?", 28)
f.ex("B1", "單選", "B", "The night parade marched on Sunday, Oct 25, at 19:00.",
     "百鬼夜行討糖踩街在哪天晚上?", opts=["A. 週六晚上", "B. 週日(10月25日)晚上7點", "C. 週一晚上"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "The main event ran 13:00-20:00 at Tianmu Sports Park.",
     "天母主活動在哪裡、幾點到幾點?", opts=["A. 天母運動公園,下午1點到晚上8點", "B. 大葉高島屋,早上9點到下午5點", "C. 新光三越,晚上7點到9點"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "250 shops gave treats.",
     "天母商圈有幾家店家一起討糖?", opts=["A. 25家", "B. 150家", "C. 250家"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "4,500 pumpkin buckets were given out.",
     "三大百貨發放幾個限量南瓜桶?", opts=["A. 450個", "B. 4,500個", "C. 45,000個"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "The mascot parade runs daily at 14:00.",
     "旅展吉祥物大遊行每天幾點?", opts=["A. 下午2點", "B. 中午12點", "C. 晚上7點"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "Budget fares often exclude checked baggage.",
     "廉航最低票價通常不含什麼?", opts=["A. 機上餐點", "B. 託運行李", "C. 登機證"], size=22.5, gap=8)
f.head("填一填 · Fill in", 28)
f.ex("B1", "完成句子", "忠誠路", "The parade marched along Zhongcheng Road.",
     "百鬼夜行沿著___二段走。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "塔麻歌子", "The Tamagotchi 30th anniversary collaboration.",
     "今年天母萬聖節跟___30週年合作。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "花笠舞", "The Yamagata flower-hat dance performs on stage.",
     "旅展舞台有日本山形___。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "預算", "Set a budget before Double 11.",
     "雙11之前,先設好___。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "行李費", "Add baggage fees before comparing fares.",
     "比機票價錢,要先加上___再比較。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "購物車", "List your cart first, then delete what you do not need.",
     "雙11之前,先把___列好。", instr="Fill in", size=22.5, gap=8)
f.head("算一算 · Work it out", 28)
f.ex("B1", "單選", "B", "6,200 − 1,200 = 5,000, exactly the budget.",
     "練習:購物車6,200元,刪掉1,200元外套,剩下多少?", opts=["A. 4,000元", "B. 5,000元", "C. 7,400元"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "The parade starts at 19:00; the main event the next day at 13:00.",
     "踩街晚上7點出發,主活動隔天下午幾點開始?", opts=["A. 下午1點", "B. 上午10點", "C. 晚上7點"], size=22.5, gap=8)
f.match_set("B1", "配對",
            ["討糖", "踩街", "南瓜桶", "打卡"],
            ["萬聖節向店家要糖果", "穿上裝扮上街遊行", "裝糖果的萬聖節桶子", "拍照標記地點、分享到社群"],
            ["a", "b", "c", "d"],
            ["討糖 — trick-or-treating.",
             "踩街 — parading through the streets in costume.",
             "南瓜桶 — a pumpkin bucket for treats.",
             "打卡 — checking in with a photo on social media."],
            instr="Match")
f.end_report()

rx = COLX[3]
image(p, "pumpkin.jpg", rx, 208, CW, 300)
caption(p, rx, 208 + 300 + 6, CW, "雕刻好的南瓜燈(資料照片)。天母萬聖節,南瓜桶是小朋友的最愛。",
        "Photo: Benjamin Balazs — CC0 (Wikimedia Commons)")
by = 208 + 300 + 96
p.rect(rx, by, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "天母時間表 · Tianmu schedule", 25, "sans", True, OLIVE); yy += 56
for t in [
    "原訂:10月24日主活動,因颱風延期",
    "10月25日(日)19:00:百鬼夜行踩街",
    "起點:新光三越台北天母店",
    "終點:大葉高島屋,沿忠誠路二段",
    "10月26日(一)13:00-20:00:主活動,天母運動公園",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 250, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢? · Over to you", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你扮過萬聖節裝扮嗎?最想扮什麼角色?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Have you ever worn a Halloween costume? Which character would you most want to be?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 488 + 250 + 18
p.rect(rx, by3, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
yy = by3 + 18
p.text(rx + 22, yy + 26, "旅展表演 · Stage shows", 25, "sans", True, OLIVE); yy += 56
for t in [
    "日本山形花笠舞",
    "韓國跆拳道與喜劇武術《JUMP》",
    "吉祥物大遊行:每日下午2點",
    "粉絲見面會:遊行之後",
    "旅遊產品說明會:西班牙朝聖之路、日本自由行",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.foot(5)
p.save(f"{OUT}/p5-youth.svg")
print("P5 saved, exercises so far:", len(REG))

# ============================================================ P6 · deep read
CURPAGE[0] = 6
p = BSPage4()
p.band("深讀 · Deep read", "Lucerna", "第 6 版 · 金融科技週深讀 + 讀圖表 · FinTech in depth, and reading a chart")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 860, tag="P6-main")
f.title("金融科技週深讀:三個加號", 34)
f.byline("Staff report · Source: event organisers' press release (Oct 23) and event FAQ")
f.para("金融科技週的三大方向,名字裡都有一個「＋」。第一個是金融＋:金融業本來就有錢、有客戶,加上科技,就能把服務做得更快、更方便。第二個是人工智慧＋:人工智慧走進銀行、投資、保險,幫忙看數據、抓風險、回客戶問題。第三個是全球擴張:一家香港的新創公司,能不能把產品賣到東南亞、歐洲、北美?金融科技週就是幫大家牽線的地方。")
f.para("數字會說話:預計逾45,000人、120多個經濟體、逾1,000位講者、逾800家參展商和新創公司、逾30個代表團、100多場社區活動。這些數字不是比賽誰大,而是告訴你:金融科技已經不是少數人的話題,而是整個城市、整個區域都在談的事。")
f.para("對學中文的人,金融科技週也是一堂課。展區裡的產品介紹、論壇上的演講題目,用的都是今天的中文:支付、數位資產、財富科技、保險科技。聽不懂沒關係,先記住四個詞,下次再聽,就聽得懂一半了。")
f.gloss("Three plus signs: Finance+ (finance plus technology), AI+ (artificial intelligence inside banks, investment and insurance) and global expansion (helping start-ups sell worldwide). The scale — 45,000+ people, 120+ economies, 1,000+ speakers, 800+ exhibitors and start-ups, 30+ delegations, 100+ community events — shows fintech is now a whole-city topic.")
f.end_report()

# ---- chart: ITF opening hours per day ----
chy = 900
p.hline(MX, COLX[0] + 3 * CW + 2 * GUT, chy - 18, GOLD, 2)
p.text(MX, chy + 28, "旅展每日開放時數 · ITF opening hours per day — bars drawn in proportion to hours", 27, "sans", True, OLIVE)
BX = MX + 215
SCALE = 100.0
hours = [("11/6(五)", 6), ("11/7(六)", 8), ("11/8(日)", 8), ("11/9(一)", 8)]
ry = chy + 62
for label, val in hours:
    p.text(MX + 20, ry + 26, label, 22, "serif", False, INK)
    p.text(BX - 14, ry + 26, str(val), 22, "serif", True, INK, anchor="end")
    p.rect(BX, ry, val * SCALE, 34, fill="#3e4c2a")
    ry += 52
chart_end = ry + 10
p.text(MX, chart_end + 24, "旅展首日中午12點才開門,開放6小時;11月7到9日每天上午10點到下午6點,各8小時。展期共4天,總開放時數 6 + 8 + 8 + 8 = 30 小時。", 21, "serif", False, GREY)
p.text(MX, chart_end + 56, "Source: published fair hours (Nov 6: 12:00-18:00; Nov 7-9: 10:00-18:00). Total: 30 hours.", 20, "sans", False, GREY)

e = Flow(p, [(COLX[i], CW) for i in range(3)], int(chart_end) + 96, 2540, tag="P6-ex")
e.head("看圖答題 · Read the chart", 28)
e.ex("B2", "單選", "A", "Nov 6 is the shortest day: 6 hours.",
     "旅展哪一天開放時間最短?", opts=["A. 11月6日(6小時)", "B. 11月7日", "C. 11月9日"], size=22.5, gap=8)
e.ex("B2", "單選", "B", "Nov 8 runs 10:00-18:00: 8 hours.",
     "11月8日開放幾小時?", opts=["A. 6小時", "B. 8小時", "C. 10小時"], size=22.5, gap=8)
e.ex("B2", "單選", "C", "6 + 8 + 8 + 8 = 30 hours in total.",
     "展期4天,總開放時數是多少?", opts=["A. 24小時", "B. 28小時", "C. 30小時"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "Nov 6 opens at noon, not 10:00.",
     "旅展首日幾點開門?", opts=["A. 中午12點", "B. 上午10點", "C. 下午2點"], size=22.5, gap=8)
e.head("深讀測驗 · Deep-read quiz", 28)
e.ex("B2", "單選", "B", "Finance+ means finance plus technology.",
     "「金融＋」是什麼意思?", opts=["A. 金融業加薪", "B. 金融加上科技", "C. 金融業加班"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "AI helps read data, spot risks and answer clients.",
     "人工智慧在金融業幫忙做什麼?", opts=["A. 看數據、抓風險、回客戶問題", "B. 印鈔票", "C. 蓋銀行大樓"], size=22.5, gap=8)
e.ex("B2", "單選", "C", "Global expansion means selling products worldwide.",
     "「全球擴張」是幫新創公司做什麼?", opts=["A. 在香港開分店", "B. 請更多員工", "C. 把產品賣到世界各地"], size=22.5, gap=8)
e.ex("B2", "單選", "B", "More than 1,000 speakers take part.",
     "金融科技週有幾位以上講者?", opts=["A. 100位", "B. 1,000位", "C. 10,000位"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "The main conference runs Nov 2-3.",
     "金融科技週主會議是哪兩天?", opts=["A. 11月2、3日", "B. 11月5、6日", "C. 11月7、8日"], size=22.5, gap=8)
e.ex("B2", "單選", "C", "Community events number 100+ through the week.",
     "金融科技週整週有多少場以上社區活動?", opts=["A. 10場", "B. 50場", "C. 100場"], size=22.5, gap=8)
e.head("填一填 · Fill in", 28)
e.ex("B2", "完成句子", "支付", "Payments is one of the main-conference topics.",
     "主會議主題包括___、數位資產、財富科技、保險科技。", instr="Fill in", size=22.5, gap=8)
e.ex("B2", "完成句子", "數位資產", "Digital assets is a main-conference topic.",
     "主會議主題包括支付、___、財富科技、保險科技。", instr="Fill in", size=22.5, gap=8)
e.ex("B2", "完成句子", "保險科技", "Insurtech is a main-conference topic.",
     "主會議主題包括支付、數位資產、財富科技、___。", instr="Fill in", size=22.5, gap=8)
e.ex("B2", "完成句子", "牽線", "The week connects start-ups with the world.",
     "金融科技週幫新創公司___、走向世界。", instr="Fill in", size=22.5, gap=8)
e.ex("B2", "完成句子", "30", "Total opening hours: 30.",
     "旅展4天總開放時數是___小時。", instr="Fill in", size=22.5, gap=8)
e.ex("B2", "完成句子", "12", "Nov 6 opens at noon (12:00).",
     "旅展首日中午___點才開門。", instr="Fill in", size=22.5, gap=8)
e.ex("B2", "完成句子", "1,600", "The travel fair has 1,600 booths.",
     "台北旅展有___個攤位。", instr="Fill in", size=22.5, gap=8)
e.ex("B2", "完成句子", "45,000", "More than 45,000 people are expected.",
     "金融科技週預計逾___人參加。", instr="Fill in", size=22.5, gap=8)
e.end_report()

rx = COLX[3]
by = 208
p.rect(rx, by, CW, 620, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "數字一覽 · By the numbers", 25, "sans", True, OLIVE); yy += 56
for t in [
    "參加人數:逾45,000人",
    "經濟體:120多個",
    "講者:逾1,000人",
    "參展商和新創:逾800家",
    "代表團:逾30個",
    "社區活動:100多場",
    "主會議:11月2、3日,香港會議展覽中心",
    "專題論壇:10個",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
by2 = by + 620 + 18
p.rect(rx, by2, CW, 504, fill=BOX, stroke=LINE, sw=1.4)
yy = by2 + 18
p.text(rx + 22, yy + 26, "比價提醒 · Compare carefully", 25, "sans", True, OLIVE); yy += 56
yy = p.para(rx + 22, yy + 24, "報導整理的例子:國泰航空東京來回含稅13,433元起,購票到11月13日。廉航最低票價通常不含託運行李,加上行李費再比較。", 22, "serif", False, INK, CW - 44, 1.36) + 6
p.para(rx + 22, yy + 21, "Example from press reports (Oct 20): Cathay Pacific Taipei-Tokyo return from NT$13,433 including tax, book by Nov 13. Always compare with baggage fees added — and check the live booking result, as prices vary by date.", 19.5, "sans", False, GREY, CW - 44, 1.35)
p.foot(6)
p.save(f"{OUT}/p6-deep.svg")
print("P6 saved, exercises so far:", len(REG))
