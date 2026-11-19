# -*- coding: utf-8 -*-
# W48 zh-tw core, VOL.5: P3 culture, P4 sport.
# P3: Golden Horse winning films in cinemas + deTour design festival (Nov 20-29)
#     + Charlie and the Chocolate Factory musical.
# P4: Dragons championship parade report (Nov 22) + U-Sport November points.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w48/2026-w48-zh-tw-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P3 · culture
CURPAGE[0] = 3
p = BSPage4()
p.band("文化　문화", "Lucerna", "第3版　得獎片　設計節　音樂劇　鋼雕閉幕　수상작, 디자인, 뮤지컬, 강철 예술의 마지막 날")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2560, tag="P3-main")
f.title("金馬得獎片進戲院", 32)
f.para("2026台北金馬影展從11月6日放到11月22日，一共17天。今年有587部影片報名，入圍名單在10月1日公佈，《狂忘警探》入圍11項，是入圍最多的影片。頒獎典禮在11月22日晚上舉行。")
f.para("典禮結束之後，得獎片陸續進戲院。香港黑色喜劇《善男信女》入圍9項，11月20日已經在全台上映，講一個做錯的外送餐點，怎麼演變成一場笑中帶淚的都市報復戰。得獎片進戲院，不要錯過。")
f.gloss("2026 Taipei Golden Horse Film Festival은 11월 6일~22일(17일) 열렸어요. 출품작 587편, 후보 발표는 10월 1일, 한 작품이 11개 부문 후보로 선두예요. 11월 22일 시상식 뒤에는 수상작들이 영화관에 걸려요. 홍콩 블랙 코미디 We Are Born Good(9개 부문 후보)은 11월 20일에 전역에서 개봉했어요.")
f.title("設計節：不完美，也可以很美", 32)
f.para("香港設計節deTour 2026從11月20日放到11月29日，一共10天，地點在中環PMQ元創方，免費入場。今年的主題是「不完美，更美好」，一共展出14件作品，分成三個展區：概念實驗室、真實場域和未來軌道。")
f.para("今年最受矚目的是搞笑發明家Matty Benedetto的Department of Everyday Problems：把冷氣機滴水、工業海綿這些生活小煩惱，變成有趣的生活設計。設計節每天上午11點到晚上8點開放，11月20日只開到下午3點。")
f.gloss("홍콩의 디자인 페스티벌 deTour 2026은 11월 20일~29일(10일) Central의 PMQ에서 열려요. 입장은 무료, 주제는 \"BETTER, NOT PERFECT\"예요. 열네 개 작품이 세 개 구역에 전시돼요. 가장 인기 있는 작품은 Matty Benedetto의 Department of Everyday Problems로, 물 떨어지는 에어컨과 산업용 스펀지를 재치 있는 디자인으로 바꿨어요. 매일 11:00~20:00에 열려요(11월 20일은 15:00까지).")
f.title("音樂劇：巧克力工廠來香港", 32)
f.para("音樂劇《查理與巧克力工廠》在香港上演，從11月4日演到12月6日。週二到週四晚上7點一場，週五晚上7點30分一場，週六下午2點30分和晚上7點30分各一場，週日上午11點30分和下午4點30分各一場，週一休息。喜歡音樂劇的人，本週末就可以去看。")
f.gloss("뮤지컬 Charlie and the Chocolate Factory는 11월 4일부터 12월 6일까지 홍콩에서 공연해요. 화요일부터 일요일까지, 월요일 공연은 없어요. 주말 공연은 하루 두 번 해요. 이번 주말에 가기 좋아요.")
# Keep the steel title with its paragraph + gloss: if less than 420px remains
# in this column, move the whole block to the next column (a title at the
# very bottom of a column orphans its body — Build 6 defect).
if f.bottom - f.y < 420 and f.ci < len(f.cols) - 1:
    f.ci += 1
    f.y = f.top
f.title("鋼雕藝術節閉幕", 32)
f.para("高雄國際鋼雕藝術節在11月22日閉幕。藝術節從10月23日放到11月22日，主題是 SUPER STAGE，地點在駁二蓬萊區B3倉庫、哈瑪星鐵道園區和鹽埕街區。85歲的藝術家林洪玉秀用金屬網做的《萬年吉祥花》，是這次最受注目的作品；現場還有一座用鋼鐵做的保險箱，叫 SUPER SAFE，裝著高雄的勞動記憶。")
f.gloss("Kaohsiung 국제 Steel Sculpture Festival은 10월 23일~11월 22일 SUPER STAGE 주제로 Pier-2, Hamasen, Yancheng에서 열린 뒤 11월 22일에 막을 내렸어요. 85세 Lin Hongyuxiu는 금속 그물로 만든 《萬年吉祥花》를 선보였어요. SUPER SAFE 강철 금고에는 Kaohsiung의 노동 기억이 담겨 있어요.")
f.head("讀懂了嗎？　이해했나요?", 25)
f.ex("A2", "單選", "A", "영화제는 11월 6일~22일이에요.",
     "金馬影展放到哪天？", opts=["A. 11月22日", "B. 11月15日", "C. 11月29日"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "올해 출품작은 587편이에요.",
     "今年金馬獎有幾部影片報名？", opts=["A. 87部", "B. 587部", "C. 57部"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "디자인 페스티벌은 11월 20일~29일에 열려요.",
     "deTour設計節放到哪天？", opts=["A. 11月22日", "B. 11月20日", "C. 11月29日"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "디자인 페스티벌은 Central의 PMQ에서 열려요.",
     "deTour設計節在哪裡舉行？", opts=["A. 中環PMQ元創方", "B. 天母棒球場", "C. 駁二"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "뮤지컬은 11월 4일~12월 6일에 공연해요.",
     "《查理與巧克力工廠》演到哪天？", opts=["A. 11月22日", "B. 12月6日", "C. 11月29日"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "월요일 공연은 없어요.",
     "音樂劇哪天休息？", opts=["A. 週六", "B. 週日", "C. 週一"], size=22.5, gap=8)
# Keep the 填一填 header with its exercises: if <420px remain in this
# column (header + first fill-in), start the section in the next column
# instead of orphaning the header at the column bottom (D6, third-round
# proof: header at col 2 bottom y=2463.8, items 35-40 at col 3 top).
if f.bottom - f.y < 420 and f.ci < len(f.cols) - 1:
    f.ci += 1
    f.y = f.top
f.head("填一填　빈칸 채우기", 25)
f.ex("A2", "完成句子", "入圍", "후보 발표는 10월 1일이었어요.",
     "金馬獎___名單在10月1日公佈。", instr="빈칸 채우기", size=22.5, gap=8)
f.ex("A2", "完成句子", "星光大道", "레드카펫은 17:00에 시작해요.",
     "頒獎典禮前，先走___。", instr="빈칸 채우기", size=22.5, gap=8)
f.ex("B1", "完成句子", "設計節", "deTour는 홍콩의 디자인 페스티벌이에요.",
     "11月20日到29日，中環有___。", instr="빈칸 채우기", size=22.5, gap=8)
f.ex("B1", "完成句子", "免費", "deTour 입장은 무료예요.",
     "deTour設計節入場是___的。", instr="빈칸 채우기", size=22.5, gap=8)
f.ex("B1", "完成句子", "音樂劇", "뮤지컬은 무대에서 노래하고 춤춰요.",
     "《查理與巧克力工廠》是一齣___。", instr="빈칸 채우기", size=22.5, gap=8)
f.ex("B1", "完成句子", "柯煒林", "올해 시상식 사회는 Will Or가 맡아요.",
     "今年金馬獎主持人是___。", instr="빈칸 채우기", size=22.5, gap=8)
# Keep the 算一算 header with its exercises: if <420px remain in this
# column (header + ex 41 + ex 42), start the section in the next column
# instead of orphaning the header at the column bottom (W48 Build 5).
if f.bottom - f.y < 420 and f.ci < len(f.cols) - 1:
    f.ci += 1
    f.y = f.top
f.head("算一算　계산해 보기", 25)
f.ex("B1", "單選", "C", "11월 6일~22일은 양쪽 끝을 포함해 17일이에요.",
     "金馬影展11月6日到11月22日，一共幾天？", opts=["A. 15天", "B. 16天", "C. 17天"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "11월 20일~29일은 모두 10일이에요.",
     "deTour設計節11月20日到11月29日，一共幾天？", opts=["A. 9天", "B. 10天", "C. 11天"], size=22.5, gap=8)
f.match_set("B1", "配對",
            ["入圍", "頒獎", "設計", "音樂劇"],
            ["被選進最後的得獎名單", "把獎頒給得獎的人", "把想法變成好用的東西", "在舞台上唱歌跳舞的戲"],
            ["a", "b", "c", "d"],
            ["入圍 — 후보에 오르는 것.",
             "頒獎 — 상을 수여하는 것.",
             "設計 — 아이디어를 유용한 것으로 바꾸는 것.",
             "音樂劇 — 무대에서 노래하고 춤추는 뮤지컬."],
            instr="짝짓기")
f.end_report()

rx = COLX[3]
image(p, "stage.jpg", rx, 208, CW, 300)
by = caption(p, rx, 208 + 300 + 6, CW, "一百多年前的劇場舞台（資料照片）。從舞台到銀幕，故事一直在演。",
        "사진: Webster & Stevens — 퍼블릭 도메인 (Wikimedia Commons)") + 18
p.rect(rx, by, CW, 470, fill=BOX)
yy = by + 18
p.text(rx + 22, yy + 26, "金馬小表　Golden Horse 안내", 25, "sans", True, OLIVE); yy += 56
for t in [
    "影展：11月6日到11月22日，一共17天",
    "報名：587部影片，入圍10月1日公佈",
    "頒獎：11月22日（日），台北流行音樂中心",
    "星光大道：下午5點；典禮：晚上6點30分",
    "主題：再見江湖；主持人：柯煒林",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 250, fill=BOX)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢？　여러분은요?", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你最想看哪一部得獎片？你去過中環PMQ看展嗎？", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "어떤 수상작을 가장 보고 싶어요? PMQ에서 전시를 본 적이 있어요?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 488 + 250 + 18
p.rect(rx, by3, CW, 450, fill=BOX)
yy = by3 + 18
p.text(rx + 22, yy + 26, "設計節小檔　deTour 파일", 25, "sans", True, OLIVE); yy += 56
for t in [
    "日期：11月20日到11月29日，一共10天",
    "地點：中環PMQ元創方，免費入場",
    "主題：BETTER, NOT PERFECT",
    "作品：14件，三個展區",
    "時間：每天11點到20點，11月20日到15點",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
by4 = by3 + 468
p.rect(rx, by4, CW, 430, fill=BOX)
yy = by4 + 18
p.text(rx + 22, yy + 26, "音樂劇小檔　뮤지컬 파일", 25, "sans", True, OLIVE); yy += 56
for t in [
    "劇名：《查理與巧克力工廠》",
    "檔期：11月4日到12月6日",
    "週二到週四：晚上7點一場",
    "週五：晚上7點30分；週六：兩場",
    "週日：上午11點30分、下午4點30分；週一休息",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ============================================================ P4 · sport
CURPAGE[0] = 4
p = BSPage4()
p.band("體育　스포츠", "Lucerna", "第4版　封王遊行　運動集點　우승 퍼레이드와 스포츠 포인트")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 1020, tag="P4-main")
f.title("11月22日，封王遊行天母出發！", 32)
f.byline("편집부 리포트　출처: TSNA 스포츠 뉴스와 타이베이시, 10월 30일~31일")
f.para("味全龍拿下隊史第6座總冠軍，封王遊行在11月22日（週日）下午2點出發，從天母棒球場到台北大巨蛋松菸大道。球團在11月21日、22日兩天，在天母棒球場辦球迷感謝祭：21日有草地音樂會，球迷可以在草坪上搭帳篷過夜；22日有球員互動、拍照和簽名，還有投打棒球教室。")
f.para("台北市政府也一起慶祝：11月整個月，市民到267間運動場館運動，U幣集點翻倍送。平常運動一次拿5個U幣，11月拿10個，滿100個U幣可以換成悠遊卡儲值金。穿上紅色衣服，一起上街為龍隊喝采，也順便養成運動習慣。")
f.gloss("Wei Chuan Dragons 우승 퍼레이드는 일요일 11월 22일 14:00에 Tianmu Baseball Stadium에서 Taipei Dome까지 출발했어요. Tianmu에서는 11월 21일~22일 이틀 동안 팬 감사제가 열렸어요. 21일에는 잔디 콘서트와 캠핑, 22일에는 선수들과 함께하는 행사가 있었어요. Taipei City는 11월 한 달 동안 U-Sport 포인트를 두 배로 줘요. 방문할 때마다 5점이 아니라 10점, 267개 장소에서요.")
f.title("棒球詞卡　야구 단어", 32)
f.para("遊行：大家走上街頭慶祝，叫遊行。感謝祭：球隊謝謝球迷的活動，叫感謝祭。集點：每次運動累積點數，叫集點。封王：拿下總冠軍，叫封王——上週本報已經教過這個詞了。")
f.gloss("네 단어: 遊行(퍼레이드), 感謝祭(팬 감사제), 集點(포인트 모으기), 封王(우승 확정).")
f.end_report()

# ---- chart: U-Sport points in November (10 points per visit, 100 to convert) ----
chy = 1070
p.hline(MX, COLX[0] + 3 * CW + 2 * GUT, chy - 18, OLIVE, 2)
p.text(MX, chy + 28, "U幣集點怎麼算　U-Sport 포인트 — 막대 길이는 포인트에 비례", 27, "sans", True, OLIVE)
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
p.text(MX, chart_end + 56, "참고｜ 11월 방문은 한 번에 10점(평소에는 5점)을 줘요. 10번 × 10 = 100점, 교환 기준이에요.", 20, "sans", False, GREY)

e = Flow(p, [(COLX[i], CW) for i in range(3)], int(chart_end) + 64, 2560, tag="P4-ex")
e.head("讀懂了嗎？　이해했나요?", 25)
e.ex("B1", "單選", "B", "퍼레이드는 일요일 11월 22일 14:00예요.",
     "封王遊行在哪天下午2點出發？", opts=["A. 11月15日", "B. 11月22日", "C. 11月29日"], size=22, gap=6)
e.ex("B1", "單選", "C", "퍼레이드는 Tianmu Baseball Stadium에서 출발해요.",
     "封王遊行從哪裡出發？", opts=["A. 台北大巨蛋", "B. 南港展覽館", "C. 天母棒球場"], size=22, gap=6)
e.ex("B1", "單選", "A", "축제는 11월 21일~22일 Tianmu에서 열려요.",
     "球迷感謝祭在哪兩天舉行？", opts=["A. 11月21、22日", "B. 11月14、15日", "C. 11月6、7日"], size=22, gap=6)
e.ex("B1", "單選", "B", "11월 방문은 한 번에 10점을 줘요.",
     "11月運動一次拿幾個U幣？", opts=["A. 5個", "B. 10個", "C. 100個"], size=22, gap=6)
e.ex("B1", "單選", "A", "100점이면 EasyCard 충전금으로 바꿀 수 있어요.",
     "滿幾個U幣可以換成悠遊卡儲值金？", opts=["A. 100個", "B. 50個", "C. 10個"], size=22, gap=6)
e.ex("B1", "單選", "C", "267곳이 참여해요.",
     "U幣集點有幾間運動場館參加？", opts=["A. 67間", "B. 167間", "C. 267間"], size=22, gap=6)
e.head("填一填　빈칸 채우기", 25)
e.ex("B1", "完成句子", "大巨蛋", "퍼레이드는 Taipei Dome에서 끝나요.",
     "封王遊行終點是台北___松菸大道。", instr="빈칸 채우기", size=22, gap=6)
e.ex("B1", "完成句子", "遊行", "퍼레이드: 모두가 축하하러 거리로 나오는 것.",
     "大家走上街頭慶祝，叫___。", instr="빈칸 채우기", size=22, gap=6)
e.ex("B1", "完成句子", "感謝祭", "감사제는 팬들에게 감사하는 축제예요.",
     "球隊謝謝球迷的活動，叫___。", instr="빈칸 채우기", size=22, gap=6)
e.ex("B1", "完成句子", "集點", "운동할 때마다 포인트를 모으는 것.",
     "每次運動累積點數，叫___。", instr="빈칸 채우기", size=22, gap=6)
e.ex("B1", "完成句子", "帳篷", "팬들은 잔디에서 하룻밤을 보내요.",
     "球迷可以在草坪上搭___過夜。", instr="빈칸 채우기", size=22, gap=6)
e.ex("B1", "完成句子", "紅色", "Dragons를 위해 빨간 옷을 입어요.",
     "看遊行要穿___衣服，為龍隊喝采。", instr="빈칸 채우기", size=22, gap=6)
e.head("看圖答題　그림을 읽고 답하기", 25)
e.ex("B1", "單選", "B", "5번 × 10점 = 50점.",
     "運動5次，一共幾個U幣？", opts=["A. 10個", "B. 50個", "C. 100個"], size=22, gap=6)
e.ex("B1", "單選", "C", "7번 × 10 = 70점. 100까지 30점이 더 필요해요.",
     "運動7次，一共70個U幣，還差幾個滿100個？", opts=["A. 10個", "B. 20個", "C. 30個"], size=22, gap=6)
e.match_set("B1", "配對",
            ["遊行", "感謝祭", "集點", "封王"],
            ["走上街頭慶祝", "球隊謝謝球迷的活動", "每次運動累積點數", "拿下總冠軍"],
            ["a", "b", "c", "d"],
            ["遊行 — 거리를 행진하는 퍼레이드.",
             "感謝祭 — 팬 감사제.",
             "集點 — 포인트 모으기.",
             "封王 — 우승을 확정하는 것."],
            instr="짝짓기")
e.end_report()

rx = COLX[3]
image(p, "baseball.jpg", rx, 208, CW, 300)
caption(p, rx, 208 + 300 + 6, CW, "棒球舊照（資料照片）。11月22日，龍隊封王遊行從天母出發。",
        "사진: Bain News Service — 퍼블릭 도메인 (Wikimedia Commons)")
by = 208 + 300 + 132
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
p.rect(rx, by + 488, CW, 244, fill=BOX)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢？　여러분은요?", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你看了封王遊行嗎？你一週運動幾次？", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "우승 퍼레이드를 봤어요? 일주일에 운동을 몇 번 해요?", 20, "sans", False, GREY, CW - 44, 1.3)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
