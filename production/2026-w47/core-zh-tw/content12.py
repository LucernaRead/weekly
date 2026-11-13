# -*- coding: utf-8 -*-
# W47 zh-tw core, VOL.4, issue week Mon 2026-11-16 to Sun 2026-11-22.
# All target text written natively for the Taiwan / Hong Kong ecosystem.
# W46 promises honoured: Nov 22 full set (night parade, Golden Horse,
# steel festival closing, Xiaoxue) + readers' letters disclosure.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/core-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P1 · front
CURPAGE[0] = 1
p = BSPage4()
# top strip (SOP 1.1): VOL left, region centre, dates right, full-width spaces
p.text(MX, 92, "VOL.4　繁體中文版", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "台灣　香港　TAIWAN AND HONG KONG", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "2026年11月16日至11月22日", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "Lucerna", 196, "serif", True, INK, anchor="middle", family="UnifrakturMaguntia")
p.text(975, 330, "繁體中文週報　VOL.4　遊行　金馬獎　小雪", 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)
p.text(975, 372, "繁體中文正文　英語講解 — Traditional Chinese text with explanations in English, for English-speaking readers", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)
p.text(MX, 490, "頭條　THE BIG STORY", 17, "sans", True, OLIVE)
hl = "週日下午2點，封王遊行天母出發"
p.text(975, 570, hl, 60, "serif", True, INK, anchor="middle", spacing=-0.7)
if text_w(hl, "serif", True, 60) > RIGHT - MX:
    print("  !! P1 HEADLINE TOO WIDE", text_w(hl, "serif", True, 60))
p.text(975, 618, "週日11月22日四件大事同一天　遊行下午2點　金馬獎晚上6點30分　夜間遊行晚上7點", 27, "serif", False, GREY, anchor="middle")

f = Flow(p, [(COLX[0], 3 * CW + 2 * GUT)], 660, 1935, tag="P1-lead")
f.title("封王遊行，本週日天母出發！", 32)
f.byline("Staff report　Source: TSNA sports news and Taipei City Government, Oct 30-31")
f.para("味全龍拿下隊史第6座總冠軍，封王遊行訂在本週日（11月22日）下午2點。封王遊行從天母棒球場出發，終點是台北大巨蛋松菸大道。球團在11月21日、22日兩天，在天母棒球場辦球迷感謝祭：21日有草地音樂會，球迷可以在草坪上搭帳篷過夜；22日有球員互動、拍照和簽名，還有投打棒球教室。")
f.para("穿上紅色衣服，到路邊為龍隊喝采。遊行路線會經過市區，想看遊行的人，要早一點到路邊找好位置，出門之前，也先查公車和捷運的最新公告。")
f.gloss("The Wei Chuan Dragons' championship parade is set for next Sunday (Nov 22) at 14:00, from Tianmu Baseball Stadium to the Taipei Dome. A two-day fans' thanksgiving festival runs Nov 21-22 at Tianmu: a grass concert and overnight camping on the 21st, player activities on the 22nd. Wear red and cheer the Dragons on.")
f.title("夜間遊行最終場，六福村見！", 32)
f.para("同一天晚上，新竹六福村也有大事：墓碑鎮萬聖節10週年，夜間遊行《鹿魔覺醒》在11月22日（週日）晚上7點演最後一場。5米高的巨型鹿魔帶著百鬼走過街道，燈光和音樂一起來，是今年萬聖節最受矚目的夜間遊行。夜間遊行晚上7點，最後一場不要錯過。")
f.para("六福村墓碑鎮從9月12日開始，到11月22日結束。白天也有遊行：日間遊行《異界狂想曲》每天下午2點登場，週二休息。想去的人，出發前先看官方公告，下雨天遊行可能改形式或取消。")
f.gloss("The same evening, Leofoo Village's Tombstone Town closes: its night parade, The Awakening of the Wendigo, plays its final show at 19:00 on Sunday, Nov 22 — a 5-metre giant demon leading a hundred ghosts through the streets. The daytime parade runs daily at 14:00. Check the park's announcements before you go; rain may change the show.")
f.end_report()

rx = COLX[3]
by = 660
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
by2 = by + 488
p.rect(rx, by2, CW, 580, fill=BOX)
yy = by2 + 18
p.text(rx + 22, yy + 26, "本週大事　This week", 25, "sans", True, OLIVE); yy += 58
for t in [
    "週一 11/16 本期出刊，小雪倒數6天",
    "週二 11/17 香港迪士尼聖誕開幕",
    "週二 11/17 西九爵士音樂節第二週開始",
    "週四 11/19 迪士尼新日間城堡演出登場",
    "週六 11/21 球迷感謝祭第一天",
    "週六 11/21 迪士尼聖誕音樂會首場",
    "本週日 11/22 遊行、金馬獎、鋼雕閉幕、夜間遊行",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.3) + 9
by3 = by2 + 598
p.rect(rx, by3, CW, 250, fill=BOX)
yy = by3 + 18
p.text(rx + 22, yy + 26, "本週一詞　Word of the week", 25, "sans", True, OLIVE); yy += 56
p.para(rx + 22, yy + 21, "「封王」 — clinching the championship. 拿下總冠軍，叫封王。", 20, "sans", False, GREY, CW - 44, 1.35)

q = Flow(p, [(COLX[i], CW) for i in range(4)], 2035, 2560, tag="P1-quiz")
q.head("快速測驗　Quick quiz", 25)
q.ex("A2", "單選", "B", "The parade is Sunday, Nov 22, at 14:00.",
     "封王遊行在哪天下午2點出發？", opts=["A. 週六", "B. 週日（11月22日）", "C. 週一"], size=22.5, gap=8)
q.ex("A2", "單選", "C", "The parade starts at Tianmu Baseball Stadium.",
     "封王遊行從哪裡出發？", opts=["A. 台北大巨蛋", "B. 南港展覽館", "C. 天母棒球場"], size=22.5, gap=8)
q.ex("A2", "單選", "A", "The night parade's final show is 19:00 on Nov 22.",
     "六福村夜間遊行最終場晚上幾點？", opts=["A. 晚上7點", "B. 下午2點", "C. 晚上9點"], size=22.5, gap=8)
q.ex("A2", "單選", "B", "The giant demon is 5 metres tall.",
     "夜間遊行的巨型鹿魔有多高？", opts=["A. 1米", "B. 5米", "C. 10米"], size=22.5, gap=8)
q.head("標題填空　Headline words", 25)
q.ex("A2", "完成句子", "封王", "Clinching the championship is 封王.",
     "拿下總冠軍，叫___。", instr="Fill in", size=22.5, gap=8)
q.ex("A2", "完成句子", "大巨蛋", "The parade ends at the Taipei Dome.",
     "封王遊行終點是台北___松菸大道。", instr="Fill in", size=22.5, gap=8)
q.ex("A2", "完成句子", "夜間", "The night parade runs in the evening.",
     "《鹿魔覺醒》是___遊行。", instr="Fill in", size=22.5, gap=8)
q.ex("A2", "完成句子", "感謝祭", "The thanksgiving festival thanks the fans.",
     "球隊謝謝球迷的活動，叫___。", instr="Fill in", size=22.5, gap=8)
q.ex("A2", "完成句子", "鹿魔", "The giant demon leads the night parade.",
     "夜間遊行由5米高的巨型___帶隊。", instr="Fill in", size=22.5, gap=8)
q.ex("A2", "完成句子", "紅色", "Wear red for the Dragons.",
     "看遊行要穿___衣服，為龍隊喝采。", instr="Fill in", size=22.5, gap=8)
q.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ============================================================ P2 · life
CURPAGE[0] = 2
p = BSPage4()
p.band("生活　Life", "Lucerna", "第2版　小雪　雙11包裹　耶誕城　Xiaoxue, Double 11 parcels and Christmasland")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2560, tag="P2-main")
f.title("小雪快到了，保暖先做好", 32)
f.para("本週日（11月22日）是小雪，是二十四節氣的第20個節氣，也是冬天的第2個節氣。小雪的意思是天氣更冷，開始下小雪——在台灣，小雪很少真的下雪，主要是提醒大家：冬天更深了。小雪之後，天氣一天比一天冷，保暖要先做好。")
f.para("小雪之後，東北季風越來越強。保暖要看三個地方：頭、脖子和腳。晚上可以用溫熱水泡腳10到15分鐘，讓身體暖起來，也比較好睡覺。早晚溫差大，外套要隨身帶，出門也要記得帶傘。")
f.gloss("Next Sunday (Nov 22) is Xiaoxue (Minor Snow), the 20th solar term and the second of winter: deeper winter, time to dress warmly. After Xiaoxue the northeast monsoon grows stronger and the weather gets colder day by day. Keep your head, neck and feet warm; a 10-15 minute warm foot soak in the evening helps you sleep.")
f.title("雙11包裹到了，先點收再拆箱", 32)
f.para("雙11買的東西，這週陸續到貨了。包裹到了，不要馬上拆箱：先對數量、看外箱有沒有破掉，拍照留存，再拆開檢查。台灣的消保法有7天鑑賞期：收到商品7天內，可以退貨。但是，有些商品是例外，例如拆封就不能退的個人衛生用品，買之前要先看清楚。")
f.box("練習例子　Practice example", [
    ("阿明在雙11買了一副耳機1,200元、一個背包800元，加起來2,000元。包裹到了，他先點收再拆箱，發現耳機不合用，7天內申請退貨，吊牌沒有拆，店家讓他退貨，他拿回1,200元，實付800元。", "serif", False, INK, 22, 1.4),
    ("Practice numbers: NT$1,200 + NT$800 = NT$2,000; the NT$1,200 headphones returned in full, so he actually paid NT$800.", "sans", False, GREY, 19.5, 1.35),
])
f.title("新北耶誕城開城，燈亮到晚上11點", 32)
f.para("新北歡樂耶誕城在11月13日（週五）開城，一直展到12月27日，一共45天。今年的主題是卡娜赫拉的小動物，市民廣場有巨型熱氣球主燈，還有粉紅郵輪、療癒森林、飄雪秀，另外串聯新北7處燈區。主燈秀每半小時一次，每次5分鐘，亮燈時間是每天下午5點30分到晚上11點。")
f.para("耶誕城不用門票，晚上去最漂亮。假日人很多，想拍照的人，要早一點到，出門之前，也先查交通管制和最新公告。")
f.gloss("New Taipei Christmasland opened Nov 13 and runs to Dec 27 — 45 days — starring Kanahei's Little Animals. The main light show runs every half hour, 5 minutes each, from 17:30 to 23:00 daily. Entry is free; evenings are the best time to go.")
f.head("讀懂了嗎？　Did you get it?", 25)
f.ex("A2", "單選", "B", "Xiaoxue is Sunday, Nov 22.",
     "小雪在哪天？", opts=["A. 11月16日", "B. 11月22日", "C. 11月9日"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "Xiaoxue is the 20th solar term.",
     "小雪是二十四節氣的第幾個？", opts=["A. 第20個", "B. 第2個", "C. 第24個"], size=22.5, gap=8)
f.ex("A2", "單選", "C", "Warm foot soaks last 10-15 minutes.",
     "晚上用溫熱水泡腳，泡多久？", opts=["A. 1分鐘", "B. 1小時", "C. 10到15分鐘"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "Check the parcel before opening it.",
     "包裹到了，第一步要做什麼？", opts=["A. 馬上拆箱", "B. 先點收、看外箱", "C. 直接丟掉"], size=22.5, gap=8)
f.ex("A2", "單選", "C", "The cooling-off period is 7 days.",
     "台灣消保法的鑑賞期是幾天？", opts=["A. 3天", "B. 14天", "C. 7天"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "Christmasland runs Nov 13-Dec 27.",
     "新北耶誕城展到哪天？", opts=["A. 12月27日", "B. 11月22日", "C. 11月16日"], size=22.5, gap=8)
f.head("填一填　Fill in", 25)
f.ex("A2", "完成句子", "小雪", "Xiaoxue is the solar term after Lidong.",
     "立冬之後的下一個節氣是___。", instr="Fill in", size=22.5, gap=8)
f.ex("A2", "完成句子", "保暖", "Dress warmly as winter deepens.",
     "冬天更深了，要注意___。", instr="Fill in", size=22.5, gap=8)
f.ex("A2", "完成句子", "泡腳", "A warm foot soak helps you sleep.",
     "晚上用溫熱水___10到15分鐘。", instr="Fill in", size=22.5, gap=8)
f.ex("A2", "完成句子", "點收", "Check the delivery before opening the box.",
     "包裹到了，先___再拆箱。", instr="Fill in", size=22.5, gap=8)
f.ex("A2", "完成句子", "鑑賞期", "The 7-day cooling-off period.",
     "收到商品7天內可以退貨，叫___。", instr="Fill in", size=22.5, gap=8)
f.ex("A2", "完成句子", "主燈秀", "The main light show repeats every half hour.",
     "耶誕城的___每半小時一次。", instr="Fill in", size=22.5, gap=8)
f.head("算一算　Work it out", 25)
f.ex("A2", "單選", "B", "1,200 + 800 = 2,000 in total.",
     "練習：耳機1,200元加背包800元，一共多少？", opts=["A. 1,000元", "B. 2,000元", "C. 3,000元"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "2,000 − 1,200 = 800 actually paid.",
     "練習：退掉1,200元的耳機，阿明實付多少？", opts=["A. 800元", "B. 1,200元", "C. 2,000元"], size=22.5, gap=8)
f.match_set("A2", "配對",
            ["小雪", "點收", "鑑賞期", "主燈秀"],
            ["立冬之後的節氣", "收到包裹先對數量、看外箱", "收到商品後可以退貨的天數", "耶誕城每半小時一次的燈光表演"],
            ["a", "b", "c", "d"],
            ["小雪 — Minor Snow, the term after Lidong.",
             "點收 — checking a delivery on arrival.",
             "鑑賞期 — the cooling-off period.",
             "主燈秀 — the main light show."],
            instr="Match")
f.end_report()

rx = COLX[3]
image(p, "rain.jpg", rx, 208, CW, 300)
caption(p, rx, 208 + 300 + 6, CW, "冷空氣一波波，雨天出門記得帶傘（資料照片）。小雪將至，保暖先做好。",
        "Photo: CorraleH — CC0 (Wikimedia Commons)")
by = 208 + 300 + 96
p.rect(rx, by, CW, 540, fill=BOX)
yy = by + 18
p.text(rx + 22, yy + 26, "事實框　This week's facts", 24, "sans", True, OLIVE); yy += 56
for t in [
    "小雪：11月22日（日），二十四節氣第20個",
    "保暖：頭、脖子、腳最重要；泡腳10到15分鐘",
    "雙11包裹：先點收、看外箱，7天內可退貨",
    "耶誕城：11月13日到12月27日，一共45天",
    "主燈秀：每天17:30到23:00，每半小時一次",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 558, CW, 250, fill=BOX)
yy = by + 558 + 18
p.text(rx + 22, yy + 26, "你呢？　Over to you", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你的雙11包裹到了嗎？小雪之後，你怎麼保暖？", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Have your Double 11 parcels arrived? How do you keep warm after Xiaoxue?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 558 + 250 + 18
p.rect(rx, by3, CW, 460, fill=BOX)
yy = by3 + 18
p.text(rx + 22, yy + 26, "耶誕城小檔　Christmasland file", 25, "sans", True, OLIVE); yy += 56
for t in [
    "日期：11月13日（五）到12月27日（日）",
    "主題：卡娜赫拉的小動物，萌幻旅行",
    "地點：新北市民廣場周邊，加7處燈區",
    "主燈秀：每日17:30到23:00，每半小時一次",
    "每次5分鐘；周邊燈飾亮到23:00",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.foot(2)
p.save(f"{OUT}/p2-life.svg")
print("P2 saved, exercises so far:", len(REG))
