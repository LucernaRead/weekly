# -*- coding: utf-8 -*-
# W48 zh-tw core, VOL.5, issue week Mon 2026-11-23 to Sun 2026-11-29.
# All target text written natively for the Taiwan / Hong Kong ecosystem.
# W47 promises honoured: Golden Horse preview (full winners' report in VOL.6),
# parade report, steel festival closing (recap), readers' letters disclosure
# (rolls to VOL.6).
# NOTE (press time, before the Nov 22 evening ceremony): this issue previews
# the ceremony — nominees and what to watch — and names no winners; the
# headline, sub-headline and Notes all use preview wording, and the full
# winners' report is in VOL.6. No winner is invented anywhere.
# All exercises are winner-independent.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w48/2026-w48-zh-tw-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P1 · front
CURPAGE[0] = 1
p = BSPage4()
# top strip (SOP 1.1): VOL left, region centre, dates right, full-width spaces
p.text(MX, 92, "VOL.5　繁體中文版", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "台灣　香港　타이완과 홍콩", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "2026年11月23日至11月29日", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "Lucerna", 196, "serif", True, INK, anchor="middle", family="UnifrakturMaguntia")
p.text(975, 330, "繁體中文週報　VOL.5　金馬獎　遊行　聖誕", 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)
p.text(975, 372, "繁體中文正文　韓國語講解 — 번체 중국어 본문과 한국어 해설, 한국어를 모국어로 하는 독자를 위한 판", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)
p.text(MX, 490, "頭條　톱 기사", 17, "sans", True, OLIVE)
hl = "金馬63之夜，名單今晚揭曉"
p.text(975, 570, hl, 60, "serif", True, INK, anchor="middle", spacing=-0.7)
if text_w(hl, "serif", True, 60) > RIGHT - MX:
    print("P1 HEADLINE TOO WIDE", text_w(hl, "serif", True, 60))
p.text(975, 618, "11月22日台北流行音樂中心　星光大道下午5點　典禮晚上6點30分", 27, "serif", False, GREY, anchor="middle")

f = Flow(p, [(COLX[0], 3 * CW + 2 * GUT)], 660, 1935, tag="P1-lead")
f.title("金馬獎得獎名單今晚揭曉！", 32)
f.byline("편집부 리포트　출처: Golden Horse 집행위원회, 10월 1일 후보 발표")
f.para("第63屆金馬獎頒獎典禮在11月22日（週日）晚上舉行，地點在台北流行音樂中心。典禮晚上6點30分開始，之前下午5點先走星光大道。今年的主題是「再見江湖」，主持人是香港演員柯煒林，第一次主持金馬獎。得獎名單在典禮當天晚上揭曉。")
f.para("《狂忘警探》入圍11項，是今年入圍最多的影片；《女孩》入圍10項，《善男信女》入圍9項。得獎名單要等典禮晚上才揭曉，完整名單下期再報。")
f.para("金馬獎，就是一年一度的大電影課：看片、聽影人分享、學電影怎麼拍。典禮結束之後，得獎片陸續進戲院，影迷可以再去戲院看一遍。")
f.gloss("제63회 Golden Horse 시상식은 일요일 11월 22일 Taipei Music Center에서 열려요. 레드카펫 17:00, 시상식 18:30, 주제는 「再見江湖」 (Farewell, Jianghu), 사회는 Will Or (Ko Wai-lam)이 맡아요. 수상자는 당일 밤에 발표돼요.")
f.title("封王遊行，11月22日出發！", 32)
f.para("味全龍拿下隊史第6座總冠軍，封王遊行在11月22日（週日）下午2點出發。封王遊行從天母棒球場出發，終點是台北大巨蛋松菸大道。球團在11月21日、22日兩天，在天母棒球場辦球迷感謝祭：21日有草地音樂會，球迷可以在草坪上搭帳篷過夜；22日有球員互動、拍照和簽名，還有投打棒球教室。")
f.para("穿上紅色衣服，到路邊為龍隊喝采。遊行路線經過市區，想看遊行的人，要早一點到路邊找好位置，出門之前，也先查公車和捷運的最新公告。")
f.gloss("Wei Chuan Dragons 우승 퍼레이드는 일요일 11월 22일 14:00에 Tianmu Baseball Stadium에서 Taipei Dome까지 출발했어요. Tianmu에서는 11월 21일~22일 이틀 동안 팬 감사제가 열렸어요. 21일에는 잔디 콘서트와 캠핑, 22일에는 선수들과 함께하는 행사가 있었어요. 빨간 옷을 입고 Dragons를 응원해요.")
f.end_report()

rx = COLX[3]
by = 660
p.rect(rx, by, CW, 470, fill=BOX)
yy = by + 18
p.text(rx + 22, yy + 26, "遊行小檔　퍼레이드 안내", 25, "sans", True, OLIVE); yy += 56
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
p.text(rx + 22, yy + 26, "本週大事　이번 주 소식", 25, "sans", True, OLIVE); yy += 58
for t in [
"週一 11/23 MegaBox聖誕開幕",
"週二 11/24 爵士閉幕，肯尼·基",
"週五 11/27 黑色星期五",
"週五 11/27 白沙道氣球預熱",
"週六 11/28 耶誕城電競總決賽第一天",
"週六 11/28 聖誕老人秘密王國開幕",
"週日 11/29 deTour閉幕、city'super嘉年華",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.3) + 9
by3 = by2 + 598
p.rect(rx, by3, CW, 250, fill=BOX)
yy = by3 + 18
p.text(rx + 22, yy + 26, "本週一詞　이번 주 단어", 25, "sans", True, OLIVE); yy += 56
p.para(rx + 22, yy + 21, "「揭曉」 — 발표한다는 뜻이에요(수상자를). 수상자 명단 발표를 揭曉라고 해요.", 20, "sans", False, GREY, CW - 44, 1.35)

q = Flow(p, [(COLX[i], CW) for i in range(4)], 2035, 2560, tag="P1-quiz")
q.head("快速測驗　빠른 퀴즈", 25)
q.ex("A2", "單選", "B", "시상식은 일요일 11월 22일이에요.",
"金馬獎頒獎典禮在哪天舉行？", opts=["A. 11月15日", "B. 11月22日", "C. 11月29日"], size=22.5, gap=8)
q.ex("A2", "單選", "B", "시상식은 타이베이 음악 센터예요.",
"頒獎典禮在哪裡舉行？", opts=["A. 天母棒球場", "B. 台北流行音樂中心", "C. 駁二"], size=22.5, gap=8)
q.ex("A2", "單選", "C", "11개 부문 후보에 오른 영화는 《狂忘警探》예요.",
"今年入圍最多的影片是哪一部？", opts=["A. 《女孩》", "B. 《雙囍》", "C. 《狂忘警探》"], size=22.5, gap=8)
q.ex("A2", "單選", "C", "퍼레이드는 Tianmu Baseball Stadium에서 출발해요.",
"封王遊行從哪裡出發？", opts=["A. 台北大巨蛋", "B. 南港展覽館", "C. 天母棒球場"], size=22.5, gap=8)
q.head("標題填空　헤드라인 단어", 25)
q.ex("A2", "完成句子", "揭曉", "수상자 명단이 발표돼요. 揭曉예요.",
"金馬獎得獎名單___。", instr="빈칸 채우기", size=22.5, gap=8)
q.ex("A2", "完成句子", "大巨蛋", "퍼레이드는 Taipei Dome에서 끝나요.",
"封王遊行終點是台北___松菸大道。", instr="빈칸 채우기", size=22.5, gap=8)
q.ex("A2", "完成句子", "感謝祭", "감사제는 팬들에게 감사하는 축제예요.",
"球隊謝謝球迷的活動，叫___。", instr="빈칸 채우기", size=22.5, gap=8)
q.ex("A2", "完成句子", "紅色", "Dragons를 위해 빨간 옷을 입어요.",
"看遊行要穿___衣服，為龍隊喝采。", instr="빈칸 채우기", size=22.5, gap=8)
q.ex("A2", "完成句子", "星光大道", "레드카펫은 17:00에 시작해요.",
"典禮前，先走___。", instr="빈칸 채우기", size=22.5, gap=8)
q.ex("A2", "完成句子", "再見江湖", "올해 주제는 「再見江湖」예요.",
"今年金馬獎的主題是「___」。", instr="빈칸 채우기", size=22.5, gap=8)
q.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ============================================================ P2 · life
CURPAGE[0] = 2
p = BSPage4()
p.band("生活　생활", "Lucerna", "第2版　小雪之後　黑色星期五　耶誕市集　Xiaoxue 뒤, 블랙프라이데이와 크리스마스 마켓")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2560, tag="P2-main")
f.title("小雪之後，冬天怎麼過", 32)
f.para("11月22日是小雪，是二十四節氣的第20個節氣，也是冬天的第2個節氣。小雪的意思是天氣更冷，開始下小雪——在台灣，小雪很少真的下雪，主要是提醒大家：冬天更深了。小雪之後，天氣一天比一天冷，保暖要先做好。")
f.para("小雪之後，東北季風越來越強。保暖要看三個地方：頭、脖子和腳。晚上可以用溫熱水泡腳10到15分鐘，讓身體暖起來，也比較好睡覺。早晚溫差大，外套要隨身帶，出門也要記得帶傘。")
f.gloss("Xiaoxue(소설)는 11월 22일에 왔어요. 스물네 절기 중 스무 번째이자 겨울의 두 번째 절기예요. 겨울이 깊어지니 따뜻하게 입어야 해요. Xiaoxue 뒤에는 북동 계절풍이 강해지고 날이 갈수록 추워져요. 머리, 목, 발을 따뜻하게 하고, 저녁에 10~15분 따뜻한 족욕을 하면 잠이 잘 와요.")
f.title("黑色星期五，先列清單再下單", 32)
f.para("11月27日（週五）是黑色星期五，一年一度的大減價日子。買東西之前，先列清單：真的需要的才買，不要看到便宜就下單。結帳之前，先比價、看退貨規定，台灣的消保法有7天鑑賞期：收到商品7天內，可以退貨。但是，有些商品是例外，例如拆封就不能退的個人衛生用品，買之前要先看清楚。")
f.box("練習例子　연습 예시", [
("阿明在黑色星期五買了一副耳機1,200元、一個背包800元，加起來2,000元。包裹到了，他先點收再拆箱，發現耳機不合用，7天內申請退貨，吊牌沒有拆，店家讓他退貨，他拿回1,200元，實付800元。", "serif", False, INK, 22, 1.4),
("숫자 연습: NT$1,200 + NT$800 = NT$2,000. NT$1,200짜리 헤드폰은 전액 환불받았으니 실제로 낸 돈은 NT$800이에요.", "sans", False, GREY, 19.5, 1.35),
])
f.title("新北耶誕市集開市，電競總決賽登場", 32)
f.para("新北歡樂耶誕城在11月13日開城，一直展到12月27日，一共45天。今年的主題是卡娜赫拉的小動物，市民廣場有巨型熱氣球主燈，還有粉紅郵輪、療癒森林、飄雪秀，另外串聯新北7處燈區。主燈秀每半小時一次，每次5分鐘，亮燈時間是每天下午5點30分到晚上11點。")
f.para("本週耶誕城更熱鬧：11月27日到29日有新北耶誕市集，結合亞洲電子競技公開賽，有特色店家、聖誕老人見面會和舞台互動；11月28日、29日，《特戰英豪》與《英雄聯盟》總決賽登場。市集每天上午11點到晚上10點，晚上去最漂亮。")
f.gloss("New Taipei Christmasland는 11월 13일~12월 27일, 45일 동안 열려요. 주인공은 Kanahei's Little Animals예요. 메인 라이트 쇼는 매일 17:30부터 23:00까지 30분마다 5분 열려요. 이번 주 크리스마스 마켓은 11월 27일~29일(11:00~22:00)에 아시아 e스포츠 오픈과 함께 열리고, Valorant와 League of Legends 결승전은 11월 28일~29일에 열려요.")
f.head("讀懂了嗎？　이해했나요?", 25)
f.ex("A2", "單選", "B", "샤오쉐는 11월 22일이에요.",
"小雪在哪天？", opts=["A. 11月16日", "B. 11月22日", "C. 11月29日"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "Xiaoxue는 스물네 절기 중 스무 번째예요.",
"小雪是二十四節氣的第幾個？", opts=["A. 第20個", "B. 第2個", "C. 第24個"], size=22.5, gap=8)
f.ex("A2", "單選", "C", "따뜻한 족욕은 10~15분이에요.",
"晚上用溫熱水泡腳，泡多久？", opts=["A. 1分鐘", "B. 1小時", "C. 10到15分鐘"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "블랙프라이데이는 11월 27일 금요일이에요.",
"黑色星期五在哪天？", opts=["A. 11月26日", "B. 11月27日", "C. 11月28日"], size=22.5, gap=8)
f.ex("A2", "單選", "C", "청약 철회 기간은 7일이에요.",
"台灣消保法的鑑賞期是幾天？", opts=["A. 3天", "B. 14天", "C. 7天"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "Christmasland는 11월 13일~12월 27일이에요.",
"新北耶誕城展到哪天？", opts=["A. 12月27日", "B. 11月22日", "C. 11月29日"], size=22.5, gap=8)
f.head("填一填　빈칸 채우기", 25)
f.ex("A2", "完成句子", "小雪", "Xiaoxue는 입동 다음 절기예요.",
"立冬之後的下一個節氣是___。", instr="빈칸 채우기", size=22.5, gap=8)
f.ex("A2", "完成句子", "保暖", "겨울이 깊어지면 따뜻하게 입어요.",
"冬天更深了，要注意___。", instr="빈칸 채우기", size=22.5, gap=8)
f.ex("A2", "完成句子", "泡腳", "따뜻한 족욕은 잠을 도와줘요.",
"晚上用溫熱水___10到15分鐘。", instr="빈칸 채우기", size=22.5, gap=8)
f.ex("A2", "完成句子", "點收", "상자를 열기 전에 배송을 확인해요.",
"包裹到了，先___再拆箱。", instr="빈칸 채우기", size=22.5, gap=8)
f.ex("A2", "完成句子", "鑑賞期", "7일 청약 철회 기간.",
"收到商品7天內可以退貨，叫___。", instr="빈칸 채우기", size=22.5, gap=8)
f.ex("A2", "完成句子", "主燈秀", "메인 라이트 쇼는 30분마다 반복돼요.",
"耶誕城的___每半小時一次。", instr="빈칸 채우기", size=22.5, gap=8)
f.head("算一算　계산해 보기", 25)
f.ex("A2", "單選", "B", "1,200 + 800 = 모두 2,000.",
"練習：耳機1,200元加背包800元，一共多少？", opts=["A. 1,000元", "B. 2,000元", "C. 3,000元"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "2,000 − 1,200 = 실제로 낸 돈은 800.",
"練習：退掉1,200元的耳機，阿明實付多少？", opts=["A. 800元", "B. 1,200元", "C. 2,000元"], size=22.5, gap=8)
f.match_set("A2", "配對",
["黑色星期五", "點收", "鑑賞期", "主燈秀"],
["一年一度的大減價日子", "收到包裹先對數量、看外箱", "收到商品後可以退貨的天數", "耶誕城每半小時一次的燈光表演"],
["a", "b", "c", "d"],
["黑色星期五 — 블랙프라이데이, 큰 세일 날.",
"點收 — 배송을 받고 확인하는 것.",
"鑑賞期 — 청약 철회 기간.",
"主燈秀 — 메인 라이트 쇼."],
instr="짝짓기")
f.end_report()

rx = COLX[3]
image(p, "rain.jpg", rx, 208, CW, 300)
caption(p, rx, 208 + 300 + 6, CW, "冷空氣一波波，雨天出門記得帶傘（資料照片）。小雪之後，保暖先做好。",
"사진: CorraleH — CC0 (Wikimedia Commons)")
by = 208 + 300 + 96
p.rect(rx, by, CW, 540, fill=BOX)
yy = by + 18
p.text(rx + 22, yy + 26, "事實框　이번 주 사실", 24, "sans", True, OLIVE); yy += 56
for t in [
"小雪：11月22日（日），二十四節氣第20個",
"保暖：頭、脖子、腳最重要；泡腳10到15分鐘",
"黑色星期五：11月27日（五），先列清單再下單",
"耶誕城：11月13日到12月27日，一共45天",
"主燈秀：每天17:30到23:00，每半小時一次",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 558, CW, 250, fill=BOX)
yy = by + 558 + 18
p.text(rx + 22, yy + 26, "你呢？　여러분은요?", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "黑色星期五你會買什麼？小雪之後，你怎麼保暖？", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "블랙프라이데이에 무엇을 살 거예요? Xiaoxue 뒤에는 어떻게 몸을 따뜻하게 해요?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 558 + 250 + 18
p.rect(rx, by3, CW, 460, fill=BOX)
yy = by3 + 18
p.text(rx + 22, yy + 26, "耶誕市集小檔　마켓 파일", 25, "sans", True, OLIVE); yy += 56
for t in [
"市集：11月27日到29日，每天11:00到22:00",
"地點：新北市民廣場周邊，結合電競公開賽",
"總決賽：11月28、29日，《特戰英豪》《英雄聯盟》",
"主燈秀：每日17:30到23:00，每半小時一次",
"每次5分鐘；周邊燈飾亮到23:00",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.foot(2)
p.save(f"{OUT}/p2-life.svg")
print("P2 saved, exercises so far:", len(REG))
