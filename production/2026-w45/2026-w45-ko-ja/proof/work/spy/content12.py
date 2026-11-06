# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ko-ja-proof/work/spy/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 표지 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2 · 제2호", 23, "sans", True, OLIVE)
p.text(975, 92, "매주 한국어로 · 毎週一号 · 한국 사람이 읽는 한국어를 읽어요", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "2026년 11월 2일(월) ~ 8일(일)", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "한국어판 · VOL.2 · 입동 · 단풍 · 김장", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "韓国語テキスト · 日本語の解説 — 日本語読者のための版", 19.5, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "11월 7일은 입동이에요 — 겨울의 시작, 단풍의 끝", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "김장철이 열리고, 수능까지 12일이 남아요. 이번 주의 달력은 오른쪽을 보세요.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "立冬", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "立冬は11月7日土曜日 · キムジャンの始まり", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "톱 뉴스 · トップニュース", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "겨울이 오는 주간 — 단풍의 끝, 김장의 시작", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "토요일 11월 7일은 입동 — 24절기 중 겨울의 첫 절기예요", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "Lucerna 편집부 · 읽기 레벨: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("11월 2일 월요일부터 8일 일요일까지, 이번 주는 겨울이 시작되는 주간이에요. 토요일 11월 7일은 입동이에요. 입동은 24절기 중 겨울의 첫 절기예요.", size=24)
f.para("단풍의 마지막 주말이에요. 그런데 단풍 절정 날짜는 하나가 아니에요. 내장산은 산림청·국립수목원 예보로 11월 4일이 절정이고, 국립공원공단 예보로는 11월 11일이 절정이에요. 그래서 7일과 8일은 두 예보 사이에 있는, 절정에 가까운 주말이라고만 말할 수 있어요. 월출산과 북한산 이야기는 3면에 있어요.", size=24)
f.para("김장철도 열렸어요. 김장은 겨울 내내 먹는 김치를 담그는 일이에요. 배추와 무, 양념을 준비해서 가족이 함께 담가요.", size=24)
f.para("수능 카운트다운도 계속돼요. 수능은 11월 19일 목요일이에요. 이번 주 월요일 11월 2일에는 17일이 남아요. 토요일 11월 7일에는 12일이 남아요. 시험 날의 특별한 조치는 11월 19일에만 적용돼요. 이번 주의 조치가 아니에요.", size=24)
f.para("지난 소식도 확인해요. 태풍 참피는 한국 본토에 상륙하지 않았어요. 제주도 남쪽 바다를 지나 10월 26일에 온대저기압으로 바뀌었어요. 야구에서는 KIA가 준플레이오프에서 LG를 3연승으로 이겼어요. 플레이오프는 10월 25일 비 때문에 일정이 바뀌었어요.", size=24)
f.para("한능검 소식도 있어요. 한국사능력검정시험 81회 접수가 이번 주에 시작돼요. 서울·강원·제주 지역은 11월 6일 오전 10시부터 12시까지 단 2시간만 따로 받아요.", size=24)
f.gloss("입동 立冬、冬の始まり · 절정 最盛期 · 김장 冬越しキムチ作り · 상륙하다 上陸する · 온대저기압 温帯低気圧。")
f.box("숫자로 보는 이번 주 · 今週を数字で見る", [
    ("7 — 입동은 11월 7일 토요일이에요", "serif", False, INK, 20, 1.35),
    ("17 — 11월 2일에는 수능까지 17일이 남아요 (D-17)", "serif", False, INK, 20, 1.35),
    ("12 — 11월 7일에는 수능까지 12일이 남아요 (D-12)", "serif", False, INK, 20, 1.35),
    ("2 — 서울 한능검 접수는 11월 6일 10시부터 12시까지 단 2시간이에요", "serif", False, INK, 20, 1.35),
    ("415.5 — 한라산 삼각봉에 온 비, 415.5밀리미터 (10월 23~26일)", "serif", False, INK, 20, 1.35),
])
f.head("지금 바로 연습 · すぐ練習", 25)
f.ex("A2", "文完成", "7", "立冬は11月7日土曜日",
     "입동은 11월 ___일이에요.", size=19.5, gap=6)
f.ex("A2", "文完成", "김치", "キムジャン＝冬越しキムチを漬けること",
     "김장은 겨울에 먹는 ___를 담그는 일이에요.", size=19.5, gap=6)
f.ex("A2", "文完成", "19", "修能は11月19日木曜日",
     "수능은 11월 ___일에 있어요.", size=19.5, gap=6)
f.ex("A2", "文完成", "17", "11月2日はD-17",
     "11월 2일에는 수능까지 ___일이 남았어요.", size=19.5, gap=6)
f.ex("A2", "文完成", "상륙", "台風は韓国本土に上陸しなかった",
     "참피는 한국 본토에 ___하지 않았어요.", size=19.5, gap=6)
f.ex("A2", "文完成", "10", "ソウルの申込み窓口は11月6日10–12時",
     "한능검 서울 접수는 11월 6일 ___시부터 12시까지예요.", size=19.5, gap=6)
f.end_report()

# ---- calendar box (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "이번 주 달력", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "11월 2일 ~ 8일의 약속", 24, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "날짜가 정해진 일만 모았어요", 19, "sans", False, GREY)
topics = [
    "11월 3일(화) — 한능검 접수 시작 (인천·경기 10시)",
    "11월 4~8일 — 청송사과축제 현장 행사",
    "11월 6일(금) — 한능검 서울·강원·제주 접수 10~12시",
    "11월 7일(토) — 입동 · 단풍 마지막 주말",
    "11월 8일(일) — 단풍 주말 계속",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 10
yy_n = p.para(gx + 22, byy + 12, "11월 1일부터는 가을철 산불조심기간이에요. 산에 갈 때는 불을 조심하세요.", 19, "serif", False, GREY, gw - 44, 1.35)
p.para(gx + 22, yy_n + 24, "이 다섯 가지 날짜가 이번 주 신문의 뼈대예요.", 19, "serif", False, GREY, gw - 44, 1.35)
p.para(gx + 22, yy_n + 52, "この五つの日付が、今号の骨組みです。", 18.5, "sans", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 636, "자료: 국사편찬위원회 공지 (10월 19일)", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "산림청·국립공원공단 예보 (9월 22일)", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "이번 호의 내용 · 今号の目次", 24, "sans", True, OLIVE)
som = [
    ("2면", "김장과 겨울 준비, 한능검", "A2"),
    ("3면", "단풍 마지막 주말", "A2→B1"),
    ("4면", "가을야구 소식", "B1"),
    ("5면", "수능 카운트다운과 할로윈", "B1"),
    ("6면", "수능까지 12일, 깊이 읽기", "B2"),
    ("7면", "입동과 날짜의 말", "A2→B2"),
    ("8면", "시험과 답", "全レベル"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

# ---- word of the week (col 3) ----
my = 1636
p.text(gx, my + 24, "이번 주의 말 · 今週のことば", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "「입동」 — 겨울의 시작을 알리는 절기예요. 입동이 지나면 겨울 준비가 본격적으로 시작돼요. 예: '11월 7일은 입동이에요.'", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "입동 ＝ 立冬、冬の始まりの節気。", 19, "sans", False, GREY, gw, 1.35)

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
f2.head("바쁜 주말", 25)
f2.para("토요일은 입동이에요. 단풍 구경을 가면 낮은 길부터 보세요. 일요일에도 단풍 주말이 계속돼요. 산에 갈 때는 산불조심기간이라는 것을 잊지 마세요.", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "짧은 소식 · 短いニュース", 24, "sans", True, OLIVE)
brefs = [
    ("참피", "참피는 본토에 상륙하지 않고 10월 26일에 온대저기압으로 바뀌었어요. (4면)"),
    ("야구", "KIA가 준플레이오프에서 LG를 3연승으로 이겼어요. (4면)"),
    ("수능", "11월 2일은 D-17, 7일은 D-12예요. (6면)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "퀴즈 · クイズ", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "トップ記事を読んで正しい答えを選ぼう · 答えは8ページ", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "単択", "A", "立冬＝冬の始まりの節気",
      "입동은 무슨 뜻이에요? A. 겨울의 시작 · B. 가을의 끝 · C. 여름의 시작", size=21)
qf.ex("A2", "単択", "A", "内藏山の二つの予報：11月4日と11月11日",
      "내장산 절정 예보 두 개는 언제예요? A. 11월 4일과 11일 · B. 10월 20일과 25일 · C. 11월 7일과 8일", size=21)
qf.ex("A2", "単択", "A", "キムジャン＝冬越しキムチを漬けること",
      "김장은 무엇을 담그는 일이에요? A. 김치 · B. 된장 · C. 간장", size=21)
qf.ex("A2", "単択", "A", "10月25日の初戦は雨で延期",
      "플레이오프에서 비로 미뤄진 경기는 언제였어요? A. 10월 25일 1차전 · B. 10월 20일 3차전 · C. 11월 2일 한국시리즈", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-pyoji.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 생활 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("생활 · 生活", "Lucerna", "레벨 A2 · 김장과 겨울 준비, 한능검 · キムジャンと冬支度、韓史試験の申込み")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("김장철이 왔어요 — 겨울을 준비하는 집", 37)
f.byline("Lucerna 편집부 · 읽기 레벨: A2")
f.para("김장은 겨울 내내 먹는 김치를 담그는 일이에요. 배추를 소금에 절이고, 무와 양념을 넣어 버무려요. 가족이 함께 담그면 하루가 금방 가요. 이웃과 나눠 먹는 집도 있어요.")
f.para("요즘은 김치를 사서 먹는 집도 많아요. 그래도 김장철이면 시장은 더 바빠져요. 배추와 양념을 사는 사람이 늘어나요. 겨울 김치는 집집마다 맛이 달라요.")
f.para("김장 말고도 겨울 준비가 많아요. 두꺼운 이불을 꺼내고, 난방이 잘 되는지 봐요. 옷장에서는 겨울옷을 앞으로 꺼내요. 따뜻한 국과 찌개가 식탁에 자주 올라와요.", w=424)
f.gloss("절이다 塩漬けにする · 버무리다 和える · 난방 暖房 · 식탁 食卓。")
f.head("산불조심기간이 시작됐어요", 25)
f.para("11월 1일부터 12월 15일까지는 가을철 산불조심기간이에요. 단풍 구경을 가는 사람이 많아서, 산에서는 불을 더 조심해야 해요. 산에 라이터나 불을 가져가면 벌금을 낼 수 있어요. 벌금은 최대 30만 원이에요.")
f.para("산에 갈 때는 정해진 길로 다니세요. 담배를 피우지 마세요. 불을 피우지 마세요. 작은 불씨가 큰 산불이 될 수 있어요.", w=384)
f.gloss("산불 山火事 · 벌금 罰金 · 불씨 火の粉。")
f.box("한능검 접수 · 韓史試験の申込み", [
    ("시험: 한국사능력검정시험 81회, 11월 28일 토요일, 심화만 봐요", "serif", False, INK, 20, 1.35),
    ("11월 3일(화) 10시 — 인천·경기 접수 시작", "serif", False, INK, 20, 1.35),
    ("11월 6일(금) 10시~12시 — 서울·강원·제주 접수, 단 2시간만 따로 받아요", "serif", False, INK, 20, 1.35),
    ("11월 6일(금) 13시부터 — 남은 자리로 전국 접수가 열려요 (11월 10일 17시까지)", "serif", False, INK, 20, 1.35),
    ("응시료: 심화 27,000원 · 접수 취소 전액 환불은 11월 17일 17시까지", "serif", False, INK, 20, 1.35),
])
f.head("겨울 밥상", 25)
f.para("김장김치는 겨울 밥상의 주인공이에요. 갓 담근 김치는 아삭하고, 시간이 지나면 맛이 깊어져요. 김장김치와 밥만 있어도 한 끼가 돼요.")
f.para("추운 날에는 따뜻한 국이 생각나요. 미역국, 된장국, 김치찌개 — 김이 나는 국을 먹으면 몸이 따뜻해져요. 국을 끓일 때는 재료를 천천히 넣어요.")
f.gloss("아삭하다 シャキシャキした · 김 湯気 · 깊어지다 深まる。")
f.head("겨울 옷장 정리", 25)
f.para("옷장 정리는 버리는 일이 아니에요. 작은 옷은 동생에게 물려주고, 낡은 옷은 깨끗이 빨아서 정리해요. 정리가 끝나면 겨울이 와도 두렵지 않아요.")
f.gloss("물려주다 受け継ぐ · 낡다 古びた · 두렵다 怖い。")
f.box("겨울 준비 목록 · 冬支度リスト", [
    ("두꺼운 이불 꺼내기", "serif", False, INK, 20, 1.35),
    ("난방이 잘 되는지 보기", "serif", False, INK, 20, 1.35),
    ("겨울옷 앞으로 꺼내기", "serif", False, INK, 20, 1.35),
    ("김장하기", "serif", False, INK, 20, 1.35),
    ("따뜻한 차 준비하기", "serif", False, INK, 20, 1.35),
])
f.head("시장에서 김장 준비", 25)
f.para("김장철이면 시장은 더 바빠져요. 배추를 고를 때는 잎이 단단한 것을 골라요. 무는 묵직한 것이 좋아요. 장을 볼 때는 목록을 적어 가면 편해요.")
f.para("김장을 담글 때는 손이 차가워져요. 따뜻한 물을 준비하고, 앞치마를 입어요. 가족이 함께하면 김장이 빨리 끝나요.")
f.gloss("묵직하다 ずっしりした · 앞치마 エプロン · 목록 リスト。")
f.end_report()

# col 3: ssam image + facts + 당신 (sequential, measured)
ix = COLX[3]
image(p, "ssam.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "쌈 채소와 쌈장. 겨울 식탁의 한국 음식이에요. 김장 사진이 아니에요.",
              "사진: wizdata — CC0 (Wikimedia Commons) · 자료 사진")
facts = ["김장은 겨울 내내 먹는 김치를 담그는 일이에요.",
         "산불조심기간은 11월 1일부터 12월 15일까지예요.",
         "한능검 서울 접수는 11월 6일 10시부터 12시까지예요."]
sy3 = cy3 + 24
# W45-KO fix: facts[0] alone narrows (340) so its final line is not lone 일이에요.
fw = [CW - 44 - 50 if i == 0 else CW - 44 for i in range(len(facts))]
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, w)) * 30.5 + 33 for t, w in zip(facts, fw)) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "알고 있나요", 24, "sans", True, OLIVE)
yy3 += 52
for t, w in zip(facts, fw):
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, w, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "당신은? 겨울을 준비할 때 가장 먼저 하는 일은 무엇이에요? 한국어로 두 문장 써서 보내 주세요."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("あなたは？冬支度でいちばん初めにすることは何ですか。韓国語で二文送ってください。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "당신은? · あなたの場合", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "あなたは？冬支度でいちばん初めにすることは何ですか。韓国語で二文送ってください。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- D-day strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "날짜 세는 말 · 日付を数える言い方", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "수능까지 남은 날로 날짜를 세는 네 가지 말 · 修能までの日数で日付を数える四つの言い方", 20, "sans", False, GREY, anchor="end")
words = [
    ("D-17", "11월 2일, 수능까지 17일이 남았어요", "11月2日、あと17日"),
    ("D-12", "11월 7일, 수능까지 12일이 남았어요", "11月7日、あと12日"),
    ("D-1", "11월 18일, 내일이에요", "11月18日、明日です"),
    ("D-데이", "11월 19일, 오늘이 바로 그날이에요", "11月19日、今日です"),
]
for i, (t, lab, cn) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 228, "문장으로 외워요: 「수능까지 17일 남았어요. 오늘이 D-17예요.」", 20.5, "serif", False, INK, RIGHT - MX, 1.42)  # kept at dy+228 (W43 patch: dy+234 grazed the exercises rule at 1804)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "연습 · 2ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ · 問題はレベル混在、番号で探そう", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · 이해", 25)
e.glossline("2면의 글을 읽고 맞는 답을 고르세요.")
e.ex("A2", "単択", "A", "キムジャン＝冬越しキムチを漬けること",
     "김장은 무엇을 담그는 일이에요? A. 김치 · B. 된장 · C. 간장", size=19, gap=6)
e.ex("A2", "単択", "A", "山火事注意期間は11月1日から",
     "산불조심기간은 언제부터예요? A. 11월 1일 · B. 12월 15일 · C. 11월 7일", size=19, gap=6)
e.ex("A2", "単択", "A", "山に火を持ち込むと最高30万ウォンの罰金",
     "산에 불을 가져가면 어떻게 돼요? A. 벌금 최대 30만 원 · B. 상을 받아요 · C. 아무 일도 없어요", size=19, gap=6)
e.ex("A2", "単択", "A", "韓史試験は11月28日土曜日",
     "한능검 시험은 며칠에 있어요? A. 11월 28일 · B. 11월 6일 · C. 11월 19일", size=19, gap=6)
e.ex("A2", "単択", "A", "ソウルの申込みは10時から12時まで",
     "한능검 서울 접수는 언제예요? A. 11월 6일 10시부터 12시까지 · B. 11월 3일 하루 종일 · C. 11월 10일 오후", size=19, gap=6, bw=334)
e.head("B · 말 넣기", 25)
e.glossline("빈칸에 알맞은 말을 넣으세요.")
e.ex("A2", "文完成", "배추", "白菜を塩漬けにする",
     "___를 소금에 절여요.", instr="空所補充", size=19, gap=6)
e.ex("A2", "文完成", "양념", "大根と調味料を入れて和える",
     "무와 ___을 넣어 버무려요.", instr="空所補充", size=19, gap=6)
e.ex("A2", "文完成", "월동", "冬支度＝冬のための準備",
     "두꺼운 이불을 꺼내는 것은 ___ 준비예요.", instr="空所補充", size=19, gap=6)
e.ex("A2", "文完成", "조심", "山では火に気をつける",
     "산에 갈 때는 불을 ___하세요.", instr="空所補充", size=19, gap=6)
e.ex("B1", "文完成", "접수", "11月3日から申込み開始",
     "한능검 ___가 11월 3일부터 시작돼요.", instr="空所補充", size=19, gap=6)
e.head("C · 숫자와 날짜", 25)
e.glossline("1면과 2면의 숫자와 날짜로 답하세요.")
e.ex("A2", "文完成", "15", "山火事注意期間は12月15日まで",
     "산불조심기간은 12월 ___일까지예요.", instr="空所補充", size=19, gap=6)
e.ex("A2", "文完成", "30만", "最高30万ウォンの罰金",
     "산에 불을 가져가면 벌금은 최대 ___원이에요.", instr="空所補充", size=19, gap=6)
e.ex("A2", "文完成", "27,000", "深化試験の受験料27,000ウォン",
     "한능검 심화 응시료는 ___원이에요.", instr="空所補充", size=19, gap=6)
e.ex("B1", "文完成", "13", "11月6日13時から全国で残り枠の申込み",
     "11월 6일 ___시부터 남은 자리로 전국 접수가 열려요.", instr="空所補充", size=19, gap=6, bw=354)
e.head("D · 짝 맞추기", 25)
e.match_set("A2", "語彙対応",
            ["김장", "월동 준비", "산불조심", "한능검"],
            ["겨울 김치를 담그는 일",
             "한국사 시험의 줄임말",
             "두꺼운 이불과 난방을 준비하는 일",
             "산에서 불을 조심하는 기간"],
            ["a", "c", "d", "b"],
            ["김장=冬越しキムチを漬けること a", "월동 준비=冬支度 c", "산불조심=山での火への注意 d", "한능검=韓史試験の略称 b"],
            instr="語と意味を結ぶ")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-saenghwal.svg")
print("P2 saved, exercises so far:", len(REG))
