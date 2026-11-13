# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 표지 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 4　제4호", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "매주 한국어로　每週一期　한국 사람이 읽는 한국어를 읽어요", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "2026년 11월 16일(월) ~ 22일(일)", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "한국어판　VOL.4　수능　김치의 날　한국시리즈", 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)
p.text(975, 372, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "수능 주간이에요 — 김치의 날도 와요", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "예비소집은 11월 18일, 수능은 11월 19일이에요. 김치의 날 소식은 3면을 보세요.", 23, "serif", False, ONCLOTH)
p.text(RIGHT - 30, 524, "수능", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "韓國高考週 — 泡菜日也來了", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "톱 뉴스　頭條", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "수능 D-1, 김치의 날 — 삼성 12년 만의 우승", 56, "serif", True, INK, 1323.5, 1.06)
p.text(MX, hy + 24, "수요일 11월 18일은 예비소집, 목요일 11월 19일은 수능 날이에요", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 26, "Lucerna 편집부　읽기 레벨: A2", 17, "sans", False, GREY)
hy += 40
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.lead_para("11월 16일 월요일부터 22일 일요일까지, 이번 주는 수능 주간이에요. 수요일 11월 18일에는 예비소집이 있고, 목요일 11월 19일에는 수능이 있어요. 수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요.", 24)
f.para("수능 카운트다운을 세어 봐요. 월요일 11월 16일에는 3일이 남아요. 수요일 11월 18일에는 1일이 남아요. 그래서 18일을 'D-1'이라고 해요. 목요일 11월 19일은 'D-데이'예요. 시험 날의 특별한 조치는 11월 19일에만 적용돼요. 이번 주의 다른 날의 조치가 아니에요.", 24)
f.para("야구 소식도 있어요. 한국시리즈에서는 삼성이 kt wiz를 4승 1패로 이겼어요. 마지막 5차전은 11월 8일 대구에서 삼성이 12대 1로 이겼어요. 2014년 이후 12년 만의 우승이에요. 자세한 이야기는 4면에 있어요.", 24)
f.para("김장 이야기도 계속돼요. 한국농수산식품유통공사가 11월 9일 기준으로 조사한 김장비용은 4인 가족 20포기 기준 199,456원이에요. 지난해 11월 상순보다 9.0% 내렸어요. 배추 값은 내렸는데 새우젓 값은 올랐어요. 자세한 이야기는 2면에 있어요.", 24)
f.para("김치의 날 이야기도 있어요. 11월 22일 일요일은 김치의 날이에요. 11월 20일 금요일에는 서울에서 위킴 페스티벌이 열려요. 김치의 날이 왜 11월 22일인지, 3면에서 알아봐요.", 24)
f.para("한능검 소식도 있어요. 취소 좌석 접수는 11월 11일부터 13일까지예요. 사진 등록은 11월 11일 10시부터, 수험표는 11월 24일 10시부터 받을 수 있어요. 시험은 11월 28일 토요일이에요.", 24)
f.gloss("예비소집 = 預備召集 · 우승 = 奪冠 · 조사하다 = 調查 · 페스티벌 = 節日慶典 · 취소 = 取消")
f.box("숫자로 보는 이번 주　數字看本週", [
    ("3 — 11월 16일에는 수능까지 3일이 남아요 (D-3)", "serif", False, INK, 20, 1.35),
    ("1 — 11월 18일에는 수능까지 1일이 남아요 (D-1)", "serif", False, INK, 20, 1.35),
    ("199,456 — 4인 가족 김장비용, 199,456원 (11월 9일 기준)", "serif", False, INK, 20, 1.35),
    ("4–1 — 삼성이 kt wiz를 4승 1패로 이겼어요", "serif", False, INK, 20, 1.35),
    ("12 — 삼성이 12년 만에 한국시리즈에서 우승했어요", "serif", False, INK, 20, 1.35),
])
f.head("지금 바로 연습　即學即練", 25)
f.ex("A2", "填空", "1", "11月18日是D-1",
     "11월 18일에는 수능까지 ___일이 남았어요.", size=19, gap=5)
f.ex("A2", "填空", "김장", "泡菜季正忙",
     "이번 주는 ___이 한창인 주간이에요.", size=19, gap=5)
f.ex("A2", "填空", "19", "韓國高考在11月19日星期四",
     "수능은 11월 ___일에 있어요.", size=19, gap=5)
f.ex("A2", "填空", "3", "11月16日是D-3",
     "11월 16일에는 수능까지 ___일이 남았어요.", size=19, gap=5)
f.ex("A2", "填空", "4승 1패", "三星4勝1負勝kt",
     "삼성은 kt wiz를 ___로 이겼어요.", size=19, gap=5)
f.ex("A2", "填空", "11", "取消名額報名11月11日起",
     "한능검 취소 좌석 접수는 11월 ___일부터예요.", size=19, gap=5)
f.end_report()

# ---- calendar box (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "이번 주 달력", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "11월 16일 ~ 22일의 약속", 24, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "날짜가 정해진 일만 모았어요", 19, "sans", False, GREY)
topics = [
    "11월 16일(월) — 수능 D-3, 이번 주의 시작",
    "11월 18일(수) — 예비소집, 수능 D-1",
    "11월 19일(목) — 수능 D-데이",
    "11월 20일(금) — 위킴 페스티벌 (서울)",
    "11월 22일(일) — 김치의 날",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 10
yy_n = p.para(gx + 22, byy + 12, "11월 1일부터 12월 15일까지 가을철 산불조심기간이에요. 산에 갈 때는 불을 조심하세요.", 19, "serif", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 636, "자료: 한국농수산식품유통공사 (11월 10일)", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "KBO 한국시리즈 결과 (11월 8일)", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f0eee5")
p.text(gx + 22, sy + 40, "이번 호의 내용　本期目錄", 24, "sans", True, OLIVE)
som = [
    ("2면", "김장비용과 김치의 날, 한능검", "A2"),
    ("3면", "김치의 날과 늦가을 단풍", "A2→B1"),
    ("4면", "한국시리즈 우승과 K리그", "B1"),
    ("5면", "수능 주간과 예비소집", "B1"),
    ("6면", "예보에서 결과로", "B2"),
    ("7면", "김치의 날과 날짜의 말", "A2→B2"),
    ("8면", "시험과 답", "全部"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

# ---- word of the week (col 3) ----
my = 1636
p.text(gx, my + 24, "이번 주의 말　本週詞語", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
y2 = p.para(gx, my + 76, "「예비소집」 — 시험 전날에 모여서 수험표를 받고 시험장을 확인하는 모임이에요. 예: '11월 18일에는 예비소집이 있어요.'", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "예비소집 = 預備召集。", 19, "sans", False, GREY, gw, 1.35)

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
f2.para("월요일에는 수능까지 3일이 남아요. 수요일에는 예비소집이 있어요. 목요일에는 수능이 있어요. 일요일에는 김치의 날이 와요.", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX)
p.text(bx + 22, 1914, "짧은 소식　快訊", 24, "sans", True, OLIVE)
brefs = [
    ("김장", "김장비용이 지난해보다 9.0% 내렸어요. (2면)"),
    ("단풍", "예보 날짜가 지났어요. 관측은 3면을 보세요."),
    ("야구", "삼성이 12년 만에 한국시리즈에서 우승했어요. (4면)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "퀴즈　閃電問答", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "讀頭版，選出正確答案　答案見第8版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "單選", "A", "11月18日是D-1",
      "11월 18일은 수능까지 며칠이 남았어요? A. 1일 · B. 3일 · C. 7일", size=21)
qf.ex("A2", "單選", "A", "泡菜成本比去年降9.0%",
      "김장비용은 지난해보다 어떻게 됐어요? A. 9.0% 내렸어요 · B. 9.0% 올랐어요 · C. 그대로예요", size=21)
qf.ex("A2", "單選", "A", "泡菜日是11月22日星期日",
      "김치의 날은 언제예요? A. 11월 22일 · B. 11월 19일 · C. 11월 28일", size=21)
qf.ex("A2", "單選", "A", "韓國大賽三星奪冠",
      "한국시리즈에서 우승한 팀은 어느 팀이에요? A. 삼성 · B. kt wiz · C. LG", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-pyoji.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 생활 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("생활　生活", "Lucerna", "레벨 A2　김장비용과 김치의 날, 한능검　泡菜成本與泡菜日、韓史檢定")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("김장비용이 내렸어요 — 김치의 날에는 김치를 나눠요", 37)
f.byline("Lucerna 편집부　읽기 레벨: A2")
f.para("김장비용이 내렸어요. 한국농수산식품유통공사가 11월 9일 기준으로 조사했어요. 4인 가족이 배추 20포기로 김장하는 데 드는 비용은 199,456원이에요. 지난해 11월 상순 평균 219,071원보다 9.0% 내렸어요. 평년보다도 13.4% 낮아요.")
f.para("비용이 내린 이유는 배추예요. 배추 20포기는 54,980원이에요. 지난해 74,800원보다 26.5% 내렸어요. 가을배추를 많이 심었고 작황도 좋았어요. 고춧가루는 1.8%, 무는 5.6% 내렸어요. 그런데 깐마늘과 새우젓 값은 올랐어요. 그래서 할인 지원이 이어져요.", w=424)
f.para("서울시 할인 행사는 11월 11일까지예요. 하나로마트 18곳에서 김장 재료 6종을 최대 반값에 팔아요. 깐마늘, 알타리무, 흙쪽파, 생강, 당근, 배가 대상이에요. 해양수산부 행사에서는 새우젓과 천일염을 싸게 살 수 있어요.")
f.gloss("조사하다 = 調查 · 작황 = 收成、長勢 · 이어지다 = 延續 · 할인 = 折扣")
f.head("김치의 날 — 11월 22일 일요일", 25)
f.para("11월 22일은 김치의 날이에요. 2020년 2월에 법으로 정한 기념일이에요. 11은 김치 재료를 하나하나, 22는 김치의 22가지 효능을 뜻해요. 김장문화는 유네스코 인류무형문화유산으로 등재됐어요.")
f.para("올해 김치의 날 전에는 위킴 페스티벌이 있어요. 11월 20일 금요일 오후 2시부터 5시 30분까지 서울 aT센터에서 열려요. 주제는 '우리의 발효과학, 모두의 김치'예요. 김치의 과학과 미래를 이야기해요.", w=384)
f.gloss("효능 = 功效 · 등재되다 = 列入、登記 · 발효 = 發酵")
f.box("한능검 접수　韓史檢定報名", [
    ("시험: 한국사능력검정시험 81회, 11월 28일 토요일 10시, 심화만 봐요", "serif", False, INK, 20, 1.35),
    ("취소 좌석 접수: 11월 11일부터 13일까지 (시간은 누리집에서 확인하세요)", "serif", False, INK, 20, 1.35),
    ("사진 등록: 11월 11일 10시부터", "serif", False, INK, 20, 1.35),
    ("수험표: 11월 24일 10시부터 받을 수 있어요", "serif", False, INK, 20, 1.35),
    ("응시료: 심화 27,000원 · 접수 취소 전액 환불은 11월 17일 17시까지", "serif", False, INK, 20, 1.35),
])
f.head("김장 나눔", 25)
f.para("김장을 담가서 나누는 사람도 많아요. 한국타이어앤테크놀로지는 11월 10일 대전 법동종합사회복지관에서 '사랑의 김장나눔' 봉사활동을 했어요. 김치를 담가서 어려운 이웃에게 나눠 주는 일이에요.", w=420)
f.para("집에서 김장을 담글 때는 이웃과 나누세요. 김장김치 한 통이 겨울 밥상을 따뜻하게 해요. 나누는 마음이 김장의 뜻이에요.")
f.gloss("봉사활동 = 志願活動 · 이웃 = 鄰居 · 따뜻하다 = 溫暖")
f.head("겨울 밥상", 25)
f.para("갓 담근 김치는 아삭해요. 시간이 지나면 맛이 깊어져요. 김장김치와 밥만 있어도 한 끼가 돼요. 추운 날에는 김치찌개가 생각나요.")
f.para("김치찌개를 끓일 때는 불을 약하게 해요. 천천히 끓여야 맛이 좋아요. 찌개가 끓으면 김이 올라와요.")
f.gloss("아삭하다 = 脆脆的 · 약하다 = 弱 · 김 = 蒸氣")
f.box("김장 장보기 목록　泡菜採購清單", [
    ("배추 — 20포기 54,980원 (11월 9일 기준)", "serif", False, INK, 20, 1.35),
    ("무와 양념 채소 — 마늘, 생강, 대파", "serif", False, INK, 20, 1.35),
    ("새우젓 — 값이 올랐어요, 할인 행사 확인 필수", "serif", False, INK, 20, 1.35),
    ("천일염과 고춧가루", "serif", False, INK, 20, 1.35),
    ("김장비용 확인하기 (11월 9일 조사 199,456원)", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: ssam image + facts + 당신 (sequential, measured)
ix = COLX[3]
image(p, "ssam.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "쌈 채소와 쌈장. 겨울 식탁의 한국 음식이에요. 김장 사진이 아니에요.",
              "사진: wizdata — CC0 (Wikimedia Commons) · 자료 사진")
facts = ["배추 20포기: 54,980원 (11월 9일)",
         "김장비용: 199,456원 (4인 가족)",
         "김치의 날: 11월 22일 일요일",
         "한능검 시험: 11월 28일 토요일"]
sy3 = cy3 + 24
fw = [CW - 44 - 50 if i == 0 else CW - 44 for i in range(len(facts))]
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, w)) * 30.5 + 33 for t, w in zip(facts, fw)) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "알고 있나요", 24, "sans", True, OLIVE)
yy3 += 52
for t, w in zip(facts, fw):
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, w, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "당신은? 김치의 날에 친구와 나누고 싶은 김치는 무엇이에요? 한국어로 두 문장 써서 보내 주세요."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你呢？泡菜日想和朋友分享哪種泡菜？寫兩句韓語寄來。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "당신은?　說說你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你呢？泡菜日想和朋友分享哪種泡菜？寫兩句韓語寄來。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- D-day strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "날짜 세는 말　數日子的說法", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "수능 날짜와 김치의 날　韓國高考日期與泡菜日", 20, "sans", False, GREY, anchor="end")
words = [
    ("D-3", "11월 16일, 수능까지 3일이 남았어요", "11月16日，還剩3天"),
    ("D-1", "11월 18일, 수능까지 1일이 남았어요", "11月18日，還剩1天"),
    ("D-데이", "11월 19일, 오늘이 바로 그날이에요", "11月19日，就是今天"),
    ("김치의 날", "11월 22일, 김치를 나누는 날이에요", "11月22日，分享泡菜的日子"),
]
for i, (t, lab, cn) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 228, "문장으로 외워요: 「수능까지 3일 남았어요. 오늘이 D-3예요.」", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "연습　第2版練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案見第8版　題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　이해", 25)
e.glossline("2면의 글을 읽고 맞는 답을 고르세요.")
e.ex("A2", "單選", "A", "白菜20棵54,980韓元",
     "배추 20포기는 얼마예요? A. 54,980원 · B. 74,800원 · C. 199,456원", size=19, gap=6)
e.ex("A2", "單選", "A", "比平年低13.4%",
     "김장비용은 평년보다 어떻게 됐어요? A. 13.4% 낮아요 · B. 13.4% 높아요 · C. 그대로예요", size=19, gap=6)
e.ex("A2", "單選", "A", "折扣賣6種泡菜食材",
     "할인 행사에서 김장 재료는 몇 종을 팔아요? A. 6종 · B. 4종 · C. 20종", size=19, gap=6)
e.ex("A2", "單選", "A", "韓史檢定在11月28日星期六",
     "한능검 시험은 언제예요? A. 11월 28일 · B. 11월 20일 · C. 11월 24일", size=19, gap=6)
e.ex("A2", "單選", "A", "泡菜節在11月20日星期五",
     "위킴 페스티벌은 언제예요? A. 11월 20일 · B. 11월 22일 · C. 11월 19일", size=19, gap=6, bw=334)
e.head("B　말 넣기", 25)
e.glossline("빈칸에 알맞은 말을 넣으세요.")
e.ex("A2", "填空", "한창", "泡菜季正忙",
     "이번 주는 김장이 ___이에요.", instr="填空", size=19, gap=6)
e.ex("A2", "填空", "22", "泡菜日是11月22日",
     "김치의 날은 11월 ___일이에요.", instr="填空", size=19, gap=6)
e.ex("A2", "填空", "54,980", "白菜20棵54,980韓元",
     "배추 20포기는 ___원이에요.", instr="填空", size=19, gap=6)
e.ex("A2", "填空", "토", "韓史檢定在星期六",
     "한능검 시험은 11월 28일 ___요일이에요.", instr="填空", size=19, gap=6)
e.ex("B1", "填空", "배추", "泡菜成本下降因白菜降價",
     "김장비용이 내린 이유는 ___ 때문이에요.", instr="填空", size=19, gap=6)
e.head("C　숫자와 날짜", 25)
e.glossline("1면과 2면의 숫자와 날짜로 답하세요.")
e.ex("A2", "填空", "199,456", "四口之家泡菜成本199,456韓元",
     "김장비용은 4인 가족 기준 ___원이에요.", instr="填空", size=19, gap=6)
e.ex("A2", "填空", "1.8", "辣椒粉降了1.8%",
     "고춧가루는 ___% 내렸어요.", instr="填空", size=19, gap=6)
e.ex("A2", "填空", "26.5", "白菜20棵比去年降26.5%",
     "배추 20포기는 지난해보다 ___% 내렸어요.", instr="填空", size=19, gap=6)
e.ex("B1", "填空", "13", "取消名額報名11月11日至13日",
     "취소 좌석 접수는 11월 11일부터 ___일까지예요.", instr="填空", size=19, gap=6, bw=354)
e.match_set("A2", "配對",
            ["김장비용", "김치의 날", "위킴 페스티벌", "한능검"],
            ["11월 22일의 법정기념일",
             "한국사 시험의 줄임말",
             "11월 20일 서울에서 열리는 김치 행사",
             "4인 가족 기준 199,456원"],
            ["d", "a", "c", "b"],
            ["김장비용 = 四口之家199,456韓元 d", "김치의 날 = 11月22日 a", "위킴 페스티벌 = 11月20日首爾 c", "한능검 = 韓國史考試簡稱 b"],
            instr="把詞和說明配對", head="D　짝 맞추기")  # W47-KO fix4: head kept with block — P2 D was orphaned same as P4 D (4th proof missed it; see FIX-NOTE §4)
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-saenghwal.svg")
print("P2 saved, exercises so far:", len(REG))
