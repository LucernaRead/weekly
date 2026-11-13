# -*- coding: utf-8 -*-
# W47 zh-tw core, VOL.4: P3 culture, P4 sport.
# P3: Golden Horse Awards (Nov 22) + steel festival closing (Nov 22).
# P4: Dragons championship parade (Nov 22) + U-Sport November points.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/core-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P3 · culture
CURPAGE[0] = 3
p = BSPage4()
p.band("文化　Culture", "Lucerna", "第3版　金馬獎　鋼雕閉幕　The Golden Horse Awards and steel art's final day")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2560, tag="P3-main")
f.title("金馬獎本週日頒獎，誰會得獎？", 32)
f.para("2026台北金馬影展從11月6日放到11月22日，入圍影片都在影展放映。今年有587部影片報名，入圍名單在10月1日公布，《狂忘警探》入圍11項，是入圍最多的影片。頒獎典禮在本週日（11月22日）舉行，地點在台北流行音樂中心，下午5點先走星光大道，頒獎典禮晚上6點30分開始。今年的主題是「再見江湖」，主持人是香港演員柯煒林，第一次主持金馬獎。得獎名單要到典禮當天才揭曉，現在誰也不知道誰會得獎。")
f.para("金馬獎，就是一年一度的大電影課：看片、聽影人分享、學電影怎麼拍。影展最後一天就是頒獎典禮，想看入圍電影的人，要把握最後一週。")
f.gloss("The 2026 Taipei Golden Horse Film Festival runs Nov 6-22: 587 entries, nominations announced Oct 1, with one film leading at 11 nominations. The 63rd Golden Horse Awards follow on Sunday, Nov 22 at the Taipei Music Center — red carpet 17:00, ceremony 18:30, hosted by Will Or (Ko Wai-lam). No winner is known until the night itself.")
f.title("鋼雕藝術節：最後一週，快去看", 32)
f.para("2026高雄國際鋼雕藝術節展到11月22日，主題是 SUPER STAGE，地點在駁二蓬萊區B3倉庫、哈瑪星鐵道園區、鹽埕街區。最後一個週末是11月21日、22日，想去的人，先查主辦單位的最新公告。平日上午10點到下午6點；週五、週末和假期，開到晚上8點。")
f.para("主題展「安全第一 SUPER SAFE」把蓬萊B3倉庫變成一座「保險箱」：保險箱裡，裝的是高雄的勞動記憶。85歲素人藝術家林洪玉秀用金屬紗網編出永不凋謝的花，作品叫《萬年吉祥花》，是本屆最動人的亮點之一。她年輕時在鹽埕學裁縫，為新娘縫婚紗，如今把人生經歷編進金屬花裡。")
f.gloss("Kaohsiung's International Steel Sculpture Festival (Oct 23-Nov 22, SUPER STAGE) reaches its final weekend, Nov 21-22, at the Penglai B3 warehouse, Hamasen and Yancheng. The SUPER SAFE theme show turns the warehouse into a steel safe holding Kaohsiung's labour memories — including 85-year-old Lin Hung Yu-hsiu's everlasting metal flowers.")
f.title("電影小課：1902年的月球之旅", 32)
f.para("一百多年前，電影還是黑白默片：沒有聲音，也沒有顏色。法國導演梅里愛在1902年拍了《月球之旅》，講一群人坐大砲做的太空船飛上月球，是最早的科幻電影之一。今天看金馬獎，也要記得：電影從黑白默片走到今天，走了一百多年。")
f.gloss("Over a century ago, films were black-and-white and silent. French director Georges Méliès's A Trip to the Moon (1902) — a crew fired at the Moon in a cannon-built spaceship — is one of the earliest science-fiction films. The Golden Horse Awards celebrate a century of that journey.")
f.head("讀懂了嗎？　Did you get it?", 25)
f.ex("A2", "單選", "A", "The film festival runs Nov 6-22.",
     "金馬影展放到哪天？", opts=["A. 11月22日", "B. 11月15日", "C. 11月9日"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "587 films entered this year.",
     "今年金馬獎有幾部影片報名？", opts=["A. 87部", "B. 587部", "C. 57部"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "The ceremony is Sunday, Nov 22.",
     "第63屆金馬獎頒獎典禮在哪天？", opts=["A. 11月15日", "B. 11月9日", "C. 11月22日"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "The ceremony starts at 18:30.",
     "金馬獎頒獎典禮晚上幾點開始？", opts=["A. 6點30分", "B. 5點", "C. 8點"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "The steel festival closes Nov 22.",
     "高雄鋼雕藝術節展到哪天？", opts=["A. 11月15日", "B. 11月22日", "C. 12月22日"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "A Trip to the Moon was made in 1902.",
     "《月球之旅》是哪一年拍的？", opts=["A. 2026年", "B. 1920年", "C. 1902年"], size=22.5, gap=8)
f.head("填一填　Fill in", 25)
f.ex("A2", "完成句子", "入圍", "The nomination list was announced Oct 1.",
     "金馬獎___名單在10月1日公布。", instr="Fill in", size=22.5, gap=8)
f.ex("A2", "完成句子", "星光大道", "The red carpet starts at 17:00.",
     "頒獎典禮前，先走___。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "保險箱", "The warehouse becomes a steel safe.",
     "主題展把倉庫變成一座___。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "鹽埕", "Yancheng is one of the festival districts.",
     "鋼雕藝術節的地點包括駁二、哈瑪星和___街區。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "默片", "Early films were black-and-white and silent.",
     "一百多年前的電影是黑白___。", instr="Fill in", size=22.5, gap=8)
f.ex("B1", "完成句子", "柯煒林", "Will Or hosts this year's ceremony.",
     "今年金馬獎主持人是___。", instr="Fill in", size=22.5, gap=8)
f.head("算一算　Work it out", 25)
f.ex("B1", "單選", "C", "Nov 6-22 inclusive is 17 days.",
     "金馬影展11月6日到11月22日，一共幾天？", opts=["A. 15天", "B. 16天", "C. 17天"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "From 17:00 to 18:30 is 1.5 hours.",
     "星光大道下午5點開始，典禮晚上6點30分開始，中間隔多久？", opts=["A. 1小時", "B. 1小時30分", "C. 2小時"], size=22.5, gap=8)
f.match_set("B1", "配對",
            ["入圍", "頒獎", "鋼雕", "默片"],
            ["被選進最後的得獎名單", "把獎頒給得獎的人", "用鋼鐵做的藝術", "沒有聲音的早期電影"],
            ["a", "b", "c", "d"],
            ["入圍 — being nominated.",
             "頒獎 — presenting awards.",
             "鋼雕 — sculpture made of steel.",
             "默片 — a silent film."],
            instr="Match")
f.end_report()

rx = COLX[3]
image(p, "moon.jpg", rx, 208, CW, 300)
by = caption(p, rx, 208 + 300 + 6, CW, "1902年電影《月球之旅》劇照（資料照片）。電影從黑白默片走到今天的金馬獎。",
        "Photo: Georges Méliès — Public domain (Wikimedia Commons)") + 18
p.rect(rx, by, CW, 470, fill=BOX)
yy = by + 18
p.text(rx + 22, yy + 26, "金馬小表　Golden Horse file", 25, "sans", True, OLIVE); yy += 56
for t in [
    "影展：11月6日到11月22日",
    "報名：587部影片，入圍10月1日公布",
    "頒獎：11月22日（日），台北流行音樂中心",
    "星光大道：下午5點；典禮：晚上6點30分",
    "主題：再見江湖；主持人：柯煒林",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 250, fill=BOX)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢？　Over to you", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你最想看哪一部入圍電影？你去過駁二看展嗎？", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Which nominated film would you most want to see? Have you visited an exhibition at Pier-2?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 488 + 250 + 18
p.rect(rx, by3, CW, 450, fill=BOX)
yy = by3 + 18
p.text(rx + 22, yy + 26, "鋼雕閉幕行程　Final weekend", 25, "sans", True, OLIVE); yy += 56
for t in [
    "日期：10月23日到11月22日",
    "地點：駁二蓬萊區B3倉庫、哈瑪星鐵道園區、鹽埕街區",
    "最後週末：11月21日（六）、22日（日）",
    "平日10點到18點；週五、週末、假期到20點",
    "閉幕當天也是小雪，小雪是11月22日",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
by4 = by3 + 468
p.rect(rx, by4, CW, 430, fill=BOX)
yy = by4 + 18
p.text(rx + 22, yy + 26, "電影小檔　Cinema file", 25, "sans", True, OLIVE); yy += 56
for t in [
    "影展放映：11月6日到11月22日",
    "地點：威秀影城台北信義、MUVIE CINEMAS",
    "《月球之旅》：1902年，法國，梅里愛",
    "最早的科幻電影之一，黑白默片",
    "金馬獎：一年一度的大電影課",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ============================================================ P4 · sport
CURPAGE[0] = 4
p = BSPage4()
p.band("體育　Sport", "Lucerna", "第4版　封王遊行　運動集點　The championship parade and sports points")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 1020, tag="P4-main")
f.title("本週日，封王遊行天母出發！", 32)
f.byline("Staff report　Source: TSNA sports news and Taipei City Government, Oct 30-31")
f.para("味全龍拿下隊史第6座總冠軍，封王遊行訂在本週日（11月22日）下午2點，從天母棒球場出發，終點是台北大巨蛋松菸大道。球團在11月21日、22日兩天，在天母棒球場辦球迷感謝祭：21日有草地音樂會，球迷可以在草坪上搭帳篷過夜；22日有球員互動、拍照和簽名，還有投打棒球教室。")
f.para("台北市政府也一起慶祝：11月整個月，市民到267間運動場館運動，U幣集點翻倍送。平常運動一次拿5個U幣，11月拿10個，滿100個U幣可以換成悠遊卡儲值金。穿上紅色衣服，一起上街為龍隊喝采，也順便養成運動習慣。")
f.gloss("The Wei Chuan Dragons' championship parade is set for next Sunday (Nov 22) at 14:00, from Tianmu Baseball Stadium to the Taipei Dome. A two-day fans' thanksgiving festival runs Nov 21-22 at Tianmu: a grass concert and overnight camping on the 21st, player activities on the 22nd. Taipei City doubles U-Sport points all November: 10 points per visit instead of 5, at 267 venues.")
f.title("棒球詞卡　Baseball words", 32)
f.para("遊行：大家走上街頭慶祝，叫遊行。感謝祭：球隊謝謝球迷的活動，叫感謝祭。集點：每次運動累積點數，叫集點。封王：拿下總冠軍，叫封王——上週本報已經教過這個詞了。")
f.gloss("Four words: 遊行 (parade), 感謝祭 (fans' thanksgiving festival), 集點 (collecting points), 封王 (clinching the title).")
f.end_report()

# ---- chart: U-Sport points in November (10 points per visit, 100 to convert) ----
chy = 1070
p.hline(MX, COLX[0] + 3 * CW + 2 * GUT, chy - 18, OLIVE, 2)
p.text(MX, chy + 28, "U幣集點怎麼算　U-Sport points — bars drawn in proportion to points", 27, "sans", True, OLIVE)
BX = MX + 215
SCALE = 9.0
rows = [("運動1次", 10), ("運動5次", 50), ("運動10次", 100)]
ry = chy + 54
for label, val in rows:
    p.text(MX + 20, ry + 22, label, 22, "serif", False, INK)
    p.text(BX - 14, ry + 22, str(val), 22, "serif", True, INK, anchor="end")
    if val > 0:
        p.rect(BX, ry, val * SCALE, 28, fill=OLIVE)
    ry += 40
chart_end = ry + 10
p.text(MX, chart_end + 24, "11月運動一次拿10個U幣，5次50個，10次100個，滿100個可以換成悠遊卡儲值金。平常一次只有5個U幣。", 21, "serif", False, GREY)
p.text(MX, chart_end + 56, "Note: November visits earn 10 points each (usually 5). 10 visits × 10 = 100 points, the conversion threshold.", 20, "sans", False, GREY)

e = Flow(p, [(COLX[i], CW) for i in range(3)], int(chart_end) + 64, 2560, tag="P4-ex")
e.head("讀懂了嗎？　Did you get it?", 25)
e.ex("B1", "單選", "B", "The parade is Sunday, Nov 22, at 14:00.",
     "封王遊行在哪天下午2點出發？", opts=["A. 11月15日", "B. 11月22日", "C. 11月9日"], size=22, gap=6)
e.ex("B1", "單選", "C", "The parade starts at Tianmu Baseball Stadium.",
     "封王遊行從哪裡出發？", opts=["A. 台北大巨蛋", "B. 南港展覽館", "C. 天母棒球場"], size=22, gap=6)
e.ex("B1", "單選", "A", "The festival runs Nov 21-22 at Tianmu.",
     "球迷感謝祭在哪兩天舉行？", opts=["A. 11月21、22日", "B. 11月14、15日", "C. 11月6、7日"], size=22, gap=6)
e.ex("B1", "單選", "B", "November visits earn 10 points each.",
     "11月運動一次拿幾個U幣？", opts=["A. 5個", "B. 10個", "C. 100個"], size=22, gap=6)
e.ex("B1", "單選", "A", "100 points convert to EasyCard stored value.",
     "滿幾個U幣可以換成悠遊卡儲值金？", opts=["A. 100個", "B. 50個", "C. 10個"], size=22, gap=6)
e.ex("B1", "單選", "C", "267 venues take part.",
     "U幣集點有幾間運動場館參加？", opts=["A. 67間", "B. 167間", "C. 267間"], size=22, gap=6)
e.head("填一填　Fill in", 25)
e.ex("B1", "完成句子", "大巨蛋", "The parade ends at the Taipei Dome.",
     "封王遊行終點是台北___松菸大道。", instr="Fill in", size=22, gap=6)
e.ex("B1", "完成句子", "遊行", "A parade: everyone takes to the streets to celebrate.",
     "大家走上街頭慶祝，叫___。", instr="Fill in", size=22, gap=6)
e.ex("B1", "完成句子", "感謝祭", "The thanksgiving festival thanks the fans.",
     "球隊謝謝球迷的活動，叫___。", instr="Fill in", size=22, gap=6)
e.ex("B1", "完成句子", "集點", "Collecting points each time you exercise.",
     "每次運動累積點數，叫___。", instr="Fill in", size=22, gap=6)
e.ex("B1", "完成句子", "帳篷", "Fans camp overnight on the grass.",
     "球迷可以在草坪上搭___過夜。", instr="Fill in", size=22, gap=6)
e.ex("B1", "完成句子", "紅色", "Wear red for the Dragons.",
     "看遊行要穿___衣服，為龍隊喝采。", instr="Fill in", size=22, gap=6)
e.head("看圖答題　Read the chart", 25)
e.ex("B1", "單選", "B", "5 visits × 10 points = 50 points.",
     "運動5次，一共幾個U幣？", opts=["A. 10個", "B. 50個", "C. 100個"], size=22, gap=6)
e.ex("B1", "單選", "C", "7 visits × 10 = 70 points; 30 more to reach 100.",
     "運動7次，一共70個U幣，還差幾個滿100個？", opts=["A. 10個", "B. 20個", "C. 30個"], size=22, gap=6)
e.match_set("B1", "配對",
            ["遊行", "感謝祭", "集點", "封王"],
            ["走上街頭慶祝", "球隊謝謝球迷的活動", "每次運動累積點數", "拿下總冠軍"],
            ["a", "b", "c", "d"],
            ["遊行 — a parade through the streets.",
             "感謝祭 — a fans' thanksgiving festival.",
             "集點 — collecting points.",
             "封王 — clinching the championship."],
            instr="Match")
e.end_report()

rx = COLX[3]
image(p, "baseball.jpg", rx, 208, CW, 300)
caption(p, rx, 208 + 300 + 6, CW, "棒球舊照（資料照片）。本週日，龍隊封王遊行從天母出發。",
        "Photo: Bain News Service — Public domain (Wikimedia Commons)")
by = 208 + 300 + 132
p.rect(rx, by, CW, 470, fill=BOX)
yy = by + 18
p.text(rx + 22, yy + 26, "遊行小檔　Parade file", 25, "sans", True, OLIVE); yy += 56
for t in [
    "遊行：11月22日（日）下午2點出發",
    "起點：天母棒球場；終點：台北大巨蛋松菸大道",
    "感謝祭：11月21、22日，天母棒球場",
    "21日：草地音樂會、草坪搭帳篷過夜",
    "22日：球員互動、拍照、簽名、棒球教室",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 244, fill=BOX)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢？　Over to you", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你會去看封王遊行嗎？你一週運動幾次？", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Will you watch the championship parade? How many times a week do you exercise?", 20, "sans", False, GREY, CW - 44, 1.3)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
