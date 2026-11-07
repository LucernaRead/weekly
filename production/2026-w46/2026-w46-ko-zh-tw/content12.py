# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ko-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 표지 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3 · 제3호", 23, "sans", True, OLIVE)
p.text(975, 92, "매주 한국어로 · 每週一期 · 한국 사람이 읽는 한국어를 읽어요", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "2026년 11월 9일(월) ~ 15일(일)", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "한국어판 · VOL.3 · 김장 · 수능 · 11월 11일", 40, "serif", True, INK, anchor="middle")
p.text(975, 366, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")
p.text(975, 394, "韓語正文 · 繁體中文講解 — 給繁體中文讀者的版本", 20, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 412, INK, 3); p.hline(MX, RIGHT, 421, INK, 1.2)

# band
p.rect(MX, 433, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 487, "김장이 한창이에요 — 수능까지 일주일이 남았어요", 36, "sans", True, "#f3edda")
p.text(MX + 30, 531, "단풍 예보 날짜가 이번 주에 있어요. 한국시리즈 소식은 4면을 보세요.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 487, "醃泡菜", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 531, "醃泡菜季正忙 · 高考剩一週", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "톱 뉴스 · 頭條", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "김장 한창, 수능 D-7 — 11월 11일은 세 가지 이름의 날", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "목요일 11월 12일은 수능까지 딱 일주일 남는 날이에요", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "Lucerna 편집부 · 읽기 레벨: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("11월 9일 월요일부터 15일 일요일까지, 이번 주는 김장이 한창인 주간이에요. 배추 값은 내렸는데 새우젓 값은 올랐어요. 장을 볼 때는 가격을 하나하나 확인하는 것이 좋아요.")
f.para("수능 카운트다운도 계속돼요. 수능은 11월 19일 목요일이에요. 월요일 11월 9일에는 10일이 남아요. 목요일 11월 12일에는 7일이 남아요. 그래서 12일을 'D-7'이라고 해요. 시험 날의 특별한 조치는 11월 19일에만 적용돼요. 이번 주의 조치가 아니에요.")
f.para("단풍 이야기도 아직 끝나지 않았어요. 산림청 예보로 월출산 절정은 11월 9일, 국립공원공단 예보로 내장산 절정은 11월 11일이에요. 예보 날짜라고 해서 실제 관측 날짜와 같다고 말하면 안 돼요. 자세한 이야기는 3면에 있어요.")
f.para("수요일 11월 11일은 이름이 세 개인 날이에요. 빼빼로데이, 농업인의 날, 가래떡데이 — 같은 날짜, 다른 이름이에요. 왜 같은 날인지, 3면에서 알아봐요.")
f.para("야구 소식도 있어요. 플레이오프에서는 삼성이 KIA를 3승 2패로 이겼어요. 한국시리즈에서는 kt wiz와 삼성이 싸워요. 발표된 일정과 이 신문의 마감일은 4면에서 확인하세요.")
f.para("한능검 소식도 있어요. 정기 접수는 11월 10일 화요일 17시에 닫혀요. 취소 좌석 접수는 11월 11일부터 13일까지예요. 시험은 11월 28일 토요일이에요.")
f.gloss("한창이다 正忙 · 새우젓 醃蝦醬 · 절정 最盛期、高峰 · 예보 預報 · 관측 觀測。")
f.box("숫자로 보는 이번 주 · 數字看本週", [
    ("10 — 11월 9일에는 수능까지 10일이 남아요 (D-10)", "serif", False, INK, 20, 1.35),
    ("7 — 11월 12일에는 수능까지 7일이 남아요 (D-7)", "serif", False, INK, 20, 1.35),
    ("3 — 11월 11일은 이름이 세 개인 날이에요", "serif", False, INK, 20, 1.35),
    ("17 — 한능검 정기 접수는 11월 10일 17시에 닫혀요", "serif", False, INK, 20, 1.35),
    ("5,557 — 배추 한 포기 소매 가격, 5,557원 (10월 16일 기준)", "serif", False, INK, 20, 1.35),
])
f.head("지금 바로 연습 · 即學即練", 25)
f.ex("A2", "完成句子", "7", "11月12日是D-7",
     "11월 12일에는 수능까지 ___일이 남았어요.", size=19.5, gap=6)
f.ex("A2", "完成句子", "김장", "泡菜季正忙",
     "이번 주는 ___이 한창인 주간이에요.", size=19.5, gap=6)
f.ex("A2", "完成句子", "19", "高考在11月19日週四",
     "수능은 11월 ___일에 있어요.", size=19.5, gap=6)
f.ex("A2", "完成句子", "10", "11月9日是D-10",
     "11월 9일에는 수능까지 ___일이 남았어요.", size=19.5, gap=6)
f.ex("A2", "完成句子", "3승 2패", "三星3勝2負晉級",
     "삼성은 KIA를 ___로 이겼어요.", size=19.5, gap=6)
f.ex("A2", "完成句子", "17", "定期報名11月10日17點截止",
     "한능검 정기 접수는 11월 10일 ___시에 닫혀요.", size=19.5, gap=6)
f.end_report()

# ---- calendar box (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "이번 주 달력", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "11월 9일 ~ 15일의 약속", 24, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "날짜가 정해진 일만 모았어요", 19, "sans", False, GREY)
topics = [
    "11월 9일(월) — 소방의 날 · 월출산 절정 예보",
    "11월 10일(화) — 한능검 정기 접수 마감 17시",
    "11월 11일(수) — 빼빼로데이 · 농업인의 날",
    "11월 12일(목) — 수능 D-7, 일주일 남았어요",
    "11월 15일(일) — 한국시리즈 7차전 (필요하면)",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 10
yy_n = p.para(gx + 22, byy + 12, "11월 1일부터는 가을철 산불조심기간이에요. 산에 갈 때는 불을 조심하세요.", 19, "serif", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 636, "자료: 국사편찬위원회 공지 (10월 19일)", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "산림청·국립공원공단 예보 (9월 22일)", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "이번 호의 내용 · 本期目錄", 24, "sans", True, OLIVE)
som = [
    ("2면", "김장 가격과 겨울 준비, 한능검", "A2"),
    ("3면", "단풍과 11월 11일의 세 이름", "A2→B1"),
    ("4면", "플레이오프 결과와 한국시리즈", "B1"),
    ("5면", "수능 D-7 주간과 빼빼로데이", "B1"),
    ("6면", "예보와 발표를 읽는 법", "B2"),
    ("7면", "김장과 날짜의 말", "A2→B2"),
    ("8면", "시험과 답", "全部"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

# ---- word of the week (col 3) ----
my = 1636
p.text(gx, my + 24, "이번 주의 말 · 本週詞語", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "「한창」 — 일이 가장 바쁘고 활발한 때를 말해요. 김장이 한창이면 온 집안이 바빠요. 예: '이번 주는 김장이 한창이에요.'", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "한창 ＝ 正忙、最忙的時候。", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "autumn.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "가을 산골짜기의 단풍. (홋카이도 핫코다산 자료 사진) 한국의 단풍 이야기는 3면에 있어요.",
        "사진: lumoplank — CC0 (Wikimedia Commons) · 자료 사진")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-weekend")
f2.head("바쁜 한 주", 25)
f2.para("월요일에는 소방의 날이에요. 수요일에는 이름이 세 개인 날이 와요. 목요일에는 수능까지 일주일이 남아요. 일요일에는 한국시리즈 마지막 경기가 있을 수도 있어요.", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "짧은 소식 · 快訊", 24, "sans", True, OLIVE)
brefs = [
    ("김장", "배추 값은 내렸고 새우젓 값은 올랐어요. (2면)"),
    ("단풍", "월출산 예보는 9일, 내장산 예보는 11일이에요. (3면)"),
    ("야구", "삼성이 플레이오프에서 KIA를 이겼어요. (4면)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "퀴즈 · 閃電問答", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "讀頭版，選出正確答案 · 答案見第 8 版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "單選", "A", "11月12日是D-7",
      "11월 12일은 수능까지 며칠이 남았어요? A. 7일 · B. 10일 · C. 4일", size=21)
qf.ex("A2", "單選", "A", "白菜降價、蝦醬漲價",
      "김장 재료 값은 어떻게 됐어요? A. 배추는 내리고 새우젓은 올랐어요 · B. 둘 다 올랐어요 · C. 둘 다 내렸어요", size=21)
qf.ex("A2", "單選", "A", "11月11日有三個名字",
      "11월 11일은 이름이 몇 개예요? A. 세 개 · B. 한 개 · C. 두 개", size=21)
qf.ex("A2", "單選", "A", "季後賽三星3勝2負勝KIA",
      "플레이오프에서 이긴 팀은 어디예요? A. 삼성 · B. KIA · C. LG", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-pyoji.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 생활 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("생활 · 生活", "Lucerna", "레벨 A2 · 김장 가격과 겨울 준비, 한능검 · 泡菜價格與過冬準備、韓史考試")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("김장이 한창이에요 — 장을 볼 때 가격부터 보세요", 37)
f.byline("Lucerna 편집부 · 읽기 레벨: A2")
f.para("김장이 한창이에요. 올해는 배추 값이 내렸어요. 한국농수산식품유통공사가 집계한 10월 16일 소매 가격으로 배추 한 포기는 5,557원이에요. 1년 전보다 10.3% 내렸어요. 가을배추 생산량이 많아서 그래요.")
f.para("그런데 새우젓 값은 크게 올랐어요. 새우젓 1킬로그램이 20,269원이에요. 1년 전보다 32.5% 올랐어요. 그래서 올해 김장비는 젓갈이 좌우한다고 말해요. 채소 값은 내렸는데, 젓갈 값 때문에 장바구니가 가볍지 않아요.")
f.para("할인 행사도 있어요. 서울시는 11월 5일부터 11일까지 하나로마트 18곳에서 김장 재료 6종을 최대 반값에 팔아요. 깐마늘, 알타리무, 흙쪽파, 생강, 당근, 배가 대상이에요. 해양수산부 행사에서는 새우젓과 천일염을 싸게 살 수 있어요.", w=424)
f.gloss("집계하다 統計 · 좌우하다 左右、決定 · 장바구니 菜籃子 · 대상 對象。")
f.head("소방의 날 — 11월 9일 월요일", 25)
f.para("11월 9일은 소방의 날이에요. 119라는 긴급 신고 번호에서 온 날짜예요. 소방관의 노고에 감사하는 날이에요. 집에서는 소화기가 있는지, 불이 날 때 나갈 길이 막혀 있지 않은지 확인해요.")
f.para("산불조심기간도 계속돼요. 11월 1일부터 12월 15일까지예요. 산에 갈 때는 불을 조심하세요. 산에 라이터나 불을 가져가면 벌금을 낼 수 있어요. 벌금은 최대 30만 원이에요.", w=384)
f.gloss("노고 辛勞 · 소화기 滅火器 · 막히다 堵塞。")
f.box("한능검 접수 · 韓史考試報名", [
    ("시험: 한국사능력검정시험 81회, 11월 28일 토요일, 심화만 봐요", "serif", False, INK, 20, 1.35),
    ("정기 접수: 11월 3일부터 11월 10일 17시까지 (지역별 첫날이 달라요)", "serif", False, INK, 20, 1.35),
    ("11월 6일 13시부터 — 남은 자리로 전국 접수가 열려요 (11월 10일 17시까지)", "serif", False, INK, 20, 1.35),
    ("취소 좌석 접수: 11월 11일부터 13일까지 (시간은 누리집에서 확인하세요)", "serif", False, INK, 20, 1.35),
    ("응시료: 심화 27,000원 · 접수 취소 전액 환불은 11월 17일 17시까지", "serif", False, INK, 20, 1.35),
])
f.head("김장하는 날", 25)
f.para("김장하는 날에는 온 가족이 모여요. 절인 배추에 양념을 버무려요. 양념에는 고춧가루, 마늘, 생강, 새우젓이 들어가요.", w=420)
f.para("요즘은 절임배추를 사서 담그는 집도 많아요. 절임배추를 쓰면 소금에 절이는 시간을 아낄 수 있어요. 그래도 양념 맛은 집집마다 달라요.")
f.gloss("절임배추 提前醃好的白菜 · 버무리다 拌 · 아끼다 節省。")
f.head("겨울 밥상", 25)
f.para("갓 담근 김치는 아삭해요. 시간이 지나면 맛이 깊어져요. 김장김치와 밥만 있어도 한 끼가 돼요. 추운 날에는 김치찌개가 생각나요.")
f.para("김치찌개를 끓일 때는 불을 약하게 해요. 천천히 끓여야 맛이 좋아요. 찌개가 끓으면 김이 올라와요.")
f.gloss("아삭하다 脆脆的 · 약하다 弱 · 김 蒸汽。")
f.box("김장 장보기 목록 · 泡菜採購清單", [
    ("배추 — 한 포기 5,557원 (10월 16일 기준)", "serif", False, INK, 20, 1.35),
    ("무와 양념 채소 — 마늘, 생강, 대파", "serif", False, INK, 20, 1.35),
    ("새우젓 — 1킬로그램 20,269원, 가격 확인 필수", "serif", False, INK, 20, 1.35),
    ("천일염과 고춧가루", "serif", False, INK, 20, 1.35),
    ("할인 행사 날짜 확인하기 (11월 5~11일)", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: ssam image + facts + 당신 (sequential, measured)
ix = COLX[3]
image(p, "ssam.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "쌈 채소와 쌈장. 겨울 식탁의 한국 음식이에요. 김장 사진이 아니에요.",
              "사진: wizdata — CC0 (Wikimedia Commons) · 자료 사진")
facts = ["배추 한 포기: 5,557원 (10월 16일)",
         "새우젓 1킬로그램: 20,269원",
         "소방의 날: 11월 9일 월요일",
         "한능검 접수 마감: 11월 10일 17시"]
sy3 = cy3 + 24
fw = [CW - 44 - 50 if i == 0 else CW - 44 for i in range(len(facts))]
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, w)) * 30.5 + 33 for t, w in zip(facts, fw)) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "알고 있나요", 24, "sans", True, OLIVE)
yy3 += 52
for t, w in zip(facts, fw):
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, w, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "당신은? 김장을 담글 때 가장 중요하다고 생각하는 재료는 무엇이에요? 한국어로 두 문장 써서 보내 주세요."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你呢？醃泡菜時你認為最重要的材料是什麼？寫兩句韓語寄來。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "당신은? · 說說你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你呢？醃泡菜時你認為最重要的材料是什麼？寫兩句韓語寄來。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- D-day strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "날짜 세는 말 · 數日子的說法", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "수능까지 남은 날로 날짜를 세는 네 가지 말 · 用高考倒數計時數日子的四個說法", 20, "sans", False, GREY, anchor="end")
words = [
    ("D-10", "11월 9일, 수능까지 10일이 남았어요", "11 月 9 日，還剩 10 天"),
    ("D-7", "11월 12일, 수능까지 7일이 남았어요", "11 月 12 日，還剩 7 天"),
    ("D-4", "11월 15일, 수능까지 4일이 남았어요", "11 月 15 日，還剩 4 天"),
    ("D-데이", "11월 19일, 오늘이 바로 그날이에요", "11 月 19 日，就是今天"),
]
for i, (t, lab, cn) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 228, "문장으로 외워요: 「수능까지 7일 남았어요. 오늘이 D-7예요.」", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "연습 · 第 2 版練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · 이해", 25)
e.glossline("2면의 글을 읽고 맞는 답을 고르세요.")
e.ex("A2", "單選", "A", "白菜一棵5,557韓元",
     "배추 한 포기는 얼마예요? A. 5,557원 · B. 20,269원 · C. 27,000원", size=19, gap=6)
e.ex("A2", "單選", "A", "蝦醬漲了32.5%",
     "새우젓 값은 어떻게 됐어요? A. 32.5% 올랐어요 · B. 10.3% 내렸어요 · C. 그대로예요", size=19, gap=6)
e.ex("A2", "單選", "A", "消防日是11月9日週一",
     "소방의 날은 언제예요? A. 11월 9일 · B. 11월 11일 · C. 11월 19일", size=19, gap=6)
e.ex("A2", "單選", "A", "定期報名截止11月10日17點",
     "한능검 정기 접수는 언제 닫혀요? A. 11월 10일 17시 · B. 11월 13일 · C. 11월 28일", size=19, gap=6)
e.ex("A2", "單選", "A", "首爾折扣11月5日至11日",
     "서울시 할인 행사는 언제예요? A. 11월 5일부터 11일까지 · B. 10월 16일 하루 · C. 12월 15일까지", size=19, gap=6, bw=334)
e.head("B · 말 넣기", 25)
e.glossline("빈칸에 알맞은 말을 넣으세요.")
e.ex("A2", "完成句子", "한창", "泡菜季正忙",
     "이번 주는 김장이 ___이에요.", instr="填空", size=19, gap=6)
e.ex("A2", "完成句子", "양념", "調料裡有辣椒粉、大蒜、生薑、蝦醬",
     "___에는 고춧가루와 마늘, 생강이 들어가요.", instr="填空", size=19, gap=6)
e.ex("A2", "完成句子", "소방", "消防日源於119",
     "11월 9일은 ___의 날이에요.", instr="填空", size=19, gap=6)
e.ex("A2", "完成句子", "조심", "進山要小心火",
     "산에 갈 때는 불을 ___하세요.", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "좌우", "今年泡菜費由醬類左右",
     "올해 김장비는 젓갈이 ___한다고 해요.", instr="填空", size=19, gap=6)
e.head("C · 숫자와 날짜", 25)
e.glossline("1면과 2면의 숫자와 날짜로 답하세요.")
e.ex("A2", "完成句子", "5,557", "白菜一棵5,557韓元",
     "배추 한 포기는 ___원이에요.", instr="填空", size=19, gap=6)
e.ex("A2", "完成句子", "20,269", "蝦醬1公斤20,269韓元",
     "새우젓 1킬로그램은 ___원이에요.", instr="填空", size=19, gap=6)
e.ex("A2", "完成句子", "17", "定期報名截止17點",
     "한능검 정기 접수는 11월 10일 ___시에 닫혀요.", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "13", "取消名額報名11月11日至13日",
     "취소 좌석 접수는 11월 11일부터 ___일까지예요.", instr="填空", size=19, gap=6, bw=354)
e.head("D · 짝 맞추기", 25)
e.match_set("A2", "詞彙配對",
            ["김장", "새우젓", "소방의 날", "한능검"],
            ["겨울 김치를 담그는 일",
             "한국사 시험의 줄임말",
             "값이 크게 오른 젓갈",
             "119에서 온 11월 9일의 날"],
            ["a", "c", "d", "b"],
            ["김장=醃過冬泡菜 a", "새우젓=漲價的蝦醬 c", "소방의 날=11月9日 d", "한능검=韓國史考試簡稱 b"],
            instr="把詞和說明配對")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-saenghwal.svg")
print("P2 saved, exercises so far:", len(REG))
