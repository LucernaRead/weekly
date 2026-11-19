# -*- coding: utf-8 -*-
# W48 zh-tw core, VOL.5: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w48/2026-w48-zh-tw-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言　언어", "Lucerna", "語言聚焦　三個級別　三個主題　세 단계, 세 가지 주제")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　聖誕的話　크리스마스 단어", 25)
a.para("크리스마스에는 크리스마스만의 단어가 있어요. 이번 주: 聖誕(크리스마스), 市集(시장), 亮燈(점등)과 打卡(사진 인증).", 22)
a.expl("이번 호의 크리스마스 단어 네 개: 聖誕, 市集, 亮燈, 打卡.")
a.para("聖誕는 크리스마스예요. 시즌은 Central에서 시작돼요. 市集는 시장이에요. World of Frozen의 겨울 마켓이요. 亮燈는 불을 켠다는 뜻이에요. 트리 점등식이요. 打卡는 소셜 미디어에 사진을 올리며 인증한다는 뜻이에요.", 22)
a.ex("A2", "完成句子", "聖誕", "12월 25일은 크리스마스예요.",
     "12月25日是___節。", instr="빈칸 채우기", size=22, gap=10)
a.ex("A2", "單選", "A", "Christmas Town은 Statue Square에 있어요.",
     "中環聖誕小鎮在哪裡？", opts=["A. 皇后像廣場", "B. 天母棒球場", "C. 駁二"], size=22, gap=10)
a.ex("A2", "完成句子", "市集", "시장은 市集이에요.",
     "賣東西、逛街的地方，叫___。", instr="빈칸 채우기", size=22, gap=10)
a.ex("A2", "單選", "A", "트리 점등식은 亮燈禮예요.",
     "聖誕樹亮燈的儀式，叫什麼？", opts=["A. 亮燈禮", "B. 感謝祭", "C. 閉幕禮"], size=22, gap=10)
a.end_report()
# ---- P7 image: below the A2 column (free space) ----
iy7 = a.y + 16
image(p, "books.jpg", COLX[0], iy7, CW, 140)
cy7 = caption(p, COLX[0], iy7 + 140, CW,
              "舊書，越讀越有味道（資料照片）。",
              "사진: 저자 미상 — CC0 (Wikimedia Commons)")
print("P7 image ends", cy7, "(A2 flow ended", a.y, ")")

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　金馬與設計　영화와 디자인", 25)
b.para("영화와 디자인이 이번 주 헤드라인을 나눠 가졌어요. 단어를 묶어서 외우면 잘 외워져요. 영화（入圍、頒獎、得獎）와 디자인（設計、展區、作品）.", 22)
b.expl("단어를 묶어 보세요. 영화(入圍/頒獎), 디자인(設計/作品).")
b.para("入圍는 후보에 오른다는 뜻, 頒獎는 상을 수여한다는 뜻이에요. 得獎는 상을 받는다는 뜻, 設計는 디자인이라는 뜻이에요. deTour는 세 개 구역에서 14개 작품을 선보여요.", 22)
b.ex("B1", "完成句子", "入圍", "후보에 오르는 것은 入圍예요.",
     "被選進最後的得獎名單，叫___。", instr="빈칸 채우기", size=22, gap=10)
b.ex("B1", "單選", "A", "시상식은 11월 22일 18:30에 시작해요.",
     "金馬獎頒獎典禮幾點開始？", opts=["A. 晚上6點30分", "B. 下午2點", "C. 上午10點"], size=22, gap=10)
b.ex("B1", "完成句子", "設計", "아이디어를 유용한 것으로 바꾸는 것이 設計예요.",
     "把想法變成好用的東西，叫___。", instr="빈칸 채우기", size=22, gap=10)
b.ex("B1", "單選", "C", "deTour는 14개 작품을 선보여요.",
     "deTour設計節一共展出幾件作品？", opts=["A. 4件", "B. 10件", "C. 14件"], size=22, gap=10)
b.para("외우는 요령: 먼저 入圍를 외우고, 그다음 星光大道(17:00 레드카펫, 시상식 전), 그다음 시상식(頒獎) 18:30을 외워요.", 22)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　時間與安排　계획 세우기", 25)
c.para("일주일을 계획하려면 시간 단어가 필요해요. 이번 주: 時間軸(타임라인), 取捨(선택), 開幕(개막)과 閉幕(폐막).", 22)
c.expl("이번 호의 계획 단어 네 개: 時間軸, 取捨, 開幕, 閉幕.")
c.para("時間軸는 타임라인이에요. 다섯 개의 큰 날짜가 한 줄에 있어요. 取捨는 선택한다는 뜻이에요. 모든 것을 볼 수는 없어요. 開幕는 개막, 閉幕는 폐막이에요. deTour는 11월 29일에 막을 내려요.", 22)
c.ex("B2", "單選", "A", "MegaBox는 11월 23일에 문을 열어요. 가장 이른 표시예요.",
     "時間軸上，最早開始的是哪一件大事？", opts=["A. MegaBox開幕", "B. 爵士閉幕", "C. 電競總決賽"], size=22, gap=10)
c.ex("B2", "完成句子", "時間軸", "타임라인을 읽고 일주일을 계획하세요.",
     "先看___，再決定去哪一件。", instr="빈칸 채우기", size=22, gap=10)
c.ex("B2", "單選", "C", "deTour는 11월 29일에 막을 내려요.",
     "deTour設計節哪天閉幕？", opts=["A. 11月22日", "B. 11月24日", "C. 11月29日"], size=22, gap=10)
c.ex("B2", "完成句子", "取捨", "다 볼 수는 없어요. 골라요.",
     "五件大事同一週，要學會___。", instr="빈칸 채우기", size=22, gap=10)
c.para("계획 단어를 많이 알 필요는 없어요. 네 개만 배우면 일주일이 가까워져요.", 22)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「deTour 11月20日到12月29日」", "→「deTour 11月20日到11月29日，一共10天」", "deTour는 11월 20일~29일, 10일간 열려요. 12월 29일까지가 아니에요."),
    ("「黑色星期五是11月28日」", "→「黑色星期五是11月27日（週五），11月28日是週六」", "블랙프라이데이는 11월 27일 금요일, 11월 28일은 토요일이에요."),
    ("「主燈秀每小時一次」", "→「主燈秀每半小時一次，17:30到23:00一共12場」", "메인 라이트 쇼는 30분마다 열려요. 17:30부터 23:00까지 12번이에요."),
]
eh = 74 + sum(72 + len(wrap("✗ " + r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所　오류 클리닉", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, "✗ " + wrong, 21.5, "serif", True, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「一到週末，耶誕城就熱鬧起來。」 — 문형 一…就…는 X하자마자 Y라는 뜻이에요. 직접 만들어 보세요. 一看到聖誕樹，就想拍照(성탄 트리를 보자마자 사진을 찍고 싶어요)."
wcn = "문형: 一…就… — X하자마자 Y해요. 직접 문장을 만들어 보세요."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式　이번 주 문장 틀", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好：上週日，我穿紅色衣服去看封王遊行，為龍隊喝采。晚上回家看金馬獎轉播，等得獎名單揭曉。這個週末，我想去新北耶誕市集看電競總決賽。——台北小讀者（編輯範例）」"
lcn = "편집부의 예시 편지예요. 진짜 편지가 아니에요. 연기 안내: VOL.4에서는 이번 호부터 진짜 독자 편지와 8면 최우수 작문을 싣겠다고 예고했지만, 마감까지 게재할 만한 편지가 도착하지 않았어요. 그래서 예시를 싣고, 초대는 계속 열려 있어요."
lt2 = "延期披露：VOL.4曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。"
lh = 164 + (len(wrap(lt, "serif", False, 21.5, CW - 44)) + len(wrap(lt2, "serif", False, 21.5, CW - 44))) * 30.53 + (len(wrap(lcn, "sans", False, 20, CW - 44)) - 1) * 28.4
# exact draw model: lead-in 89 + lt/lt2 block lines x30.53 + gaps 31/30 + lcn lines
# (last baseline + descent 6 + pad 8). The old 62/12/26 formula under-counted
# the lead-in and inter-para gaps by ~20px (caught by occlusion audit, build 10).
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地　독자 광장", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 24)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "本週金句　이번 주 문장 — 이번 호 기사에서 그대로 가져온 문장", 27, "sans", True, OLIVE)
quotes = [
    ("「得獎名單在典禮當天晚上揭曉」", "수상자는 당일 밤에 발표돼요.", "1쪽"),
    ("「封王遊行從天母棒球場出發」", "우승 퍼레이드는 Tianmu Baseball Stadium을 출발해요.", "1쪽"),
    ("「小雪之後，天氣一天比一天冷」", "Xiaoxue 뒤로는 하루하루 더 추워져요.", "2쪽"),
    ("「主燈秀每半小時一次，每次5分鐘」", "메인 라이트 쇼는 30분마다, 한 번에 5분이에요.", "2쪽"),
    ("「得獎片進戲院，不要錯過」", "수상작들이 영화관에 걸려요. 놓치지 마세요.", "3쪽"),
    ("「不完美，更美好」", "완벽하지 않아도 더 좋아요.", "3쪽"),
    ("「穿上紅色衣服，一起上街為龍隊喝采」", "빨간 옷을 입고 거리로 나와 Dragons를 응원해요.", "4쪽"),
    ("「香港聖誕，從中環開始」", "홍콩 크리스마스는 Central에서 시작돼요.", "5쪽"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 128
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 128 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "下期預告　다음 주 (VOL.6)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "下週：金馬獎得獎名單完整報導、得獎片進戲院、聖誕市集與耶誕演唱會，還有你們的來信和第8版最佳作文。下週見！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
