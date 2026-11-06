# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ko-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 청년 (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("청년 · 青年", "Lucerna", "레벨 B1 · 엔믹스 컴백과 치이카와 · NMIXX 回歸與吉伊卡哇")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-feature")
f.title("월요일 저녁, 엔믹스가 돌아왔어요", 37)
f.byline("Lucerna 편집부 · 읽기 레벨: B1")
f.para("걸그룹 엔믹스(NMIXX)가 19일 월요일 저녁 6시에 새 앨범을 냈어요. 여섯 번째 미니 앨범 'Strange Muse'예요. 타이틀곡 이름은 '긴 소원'이에요. 영어 제목은 'Birthday Wish'예요.")
f.para("이번 앨범에는 그룹의 첫 유닛 곡도 있어요. 유닛 곡은 작은 팀으로 나눠서 부르는 노래예요. 노래는 월요일 저녁에 멜론 Top 100에서 34위로 시작했어요. 그런데 자정이 되자 5위까지 올라갔어요. 엔믹스의 최고 기록이에요.")
f.para("21일에는 검색에서도 엔믹스가 가장 크게 오른 이름이었어요. 제목 '긴 소원'은 생일에 비는 소원이에요. 여러분도 노래를 들으며 소원을 빌어 보세요.")
f.gloss("컴백 回歸 · 타이틀곡 主打歌 · 유닛 곡 小分隊歌曲 · 자정 午夜 · 빌다 許（願）。")
f.head("영화관 1위 — 치이카와가 돌아왔어요", 25)
f.para("일본 캐릭터 영화 '극장판 치이카와: 인어섬의 비밀'이 한국 영화관에서 다시 1위가 됐어요. 지금까지 본 관객은 150만 명이 넘어요.")
f.para("17일, '치이카와'는 Google 트렌드 한국에서 3위였어요. 1,000회 이상 검색됐어요. 작은 캐릭터가 큰 사랑을 받고 있어요.")
f.gloss("극장판 劇場版 · 인어섬 人魚島 · 누적 累計 · 관객 觀眾。")
f.box("이번 주 청년 숫자 · 本週青年數字", [
    ("34위 → 5위 — '긴 소원'의 멜론 Top 100 순위예요 (월요일 저녁 → 자정)", "serif", False, INK, 20.5, 1.4),
    ("150만 명 — 치이카와 영화를 본 사람 (누적)", "serif", False, INK, 20.5, 1.4),
    ("3위 — 17일 Google 트렌드 한국에서 치이카와", "serif", False, INK, 20.5, 1.4),
])
f.end_report()

# col 3: concert image + melon chart + cinema image
ix = COLX[3]
image(p, "concert.jpg", ix, 200, CW, 220)
cy3 = caption(p, ix, 420, CW, "콘서트 무대 앞의 관객들. 컴백 무대의 열기가 뜨거워요.",
              "사진: US Army — Public domain (Wikimedia Commons) · 자료 사진")
# melon mini chart
my3 = cy3 + 22
p.rect(ix, my3, CW, 218, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, my3 + 36, "「긴 소원」 멜론 순위", 23, "sans", True, OLIVE)
p.text(ix + 22, my3 + 78, "월요일 저녁", 20, "serif", False, INK)
p.rect(ix + 150, my3 + 58, 143, 24, fill=OLIVE)
p.text(ix + 301, my3 + 78, "34위", 20, "sans", True, INK)
p.text(ix + 22, my3 + 122, "자정", 20, "serif", False, INK)
p.rect(ix + 150, my3 + 102, 21, 24, fill=BRICK)
p.text(ix + 179, my3 + 122, "5위", 20, "sans", True, INK)
p.para(ix + 22, my3 + 152, "숫자가 작을수록 높은 순위예요. 막대의 길이는 순위 숫자에 비례해요.", 18.5, "serif", False, GREY, CW - 44, 1.35)
iy3 = my3 + 218 + 24
image(p, "cinema.jpg", ix, iy3, CW, 200)
cy4 = caption(p, ix, iy3 + 200, CW, "영화관. '치이카와'는 한국 영화관에서 다시 1위가 됐어요.",
              "사진: Elijah Flores — CC0 (Wikimedia Commons)")
print("P5 col3 ends", cy4)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "연습 · 第 5 版練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · 이해", 25)
e.glossline("5면의 글을 읽고 맞는 답을 고르세요.")
e.ex("B1", "單選", "B", "這是第六張迷你專輯",
     "엔믹스의 새 앨범은 몇 번째 미니 앨범이에요? A. 다섯 번째 · B. 여섯 번째 · C. 첫 번째", size=20, gap=7)
e.ex("B1", "單選", "B", "主打歌是《긴 소원》",
     "타이틀곡의 이름은 뭐예요? A. Strange Muse · B. 긴 소원 · C. Birthday Party", size=20, gap=7)
e.ex("B1", "單選", "C", "在Melon從第34位起步",
     "노래는 멜론에서 몇 위로 시작했어요? A. 5위 · B. 19위 · C. 34위", size=20, gap=7)
e.ex("B1", "單選", "A", "午夜升到第5位",
     "자정에 몇 위가 됐어요? A. 5위 · B. 3위 · C. 1위", size=20, gap=7)
e.ex("B1", "單選", "B", "吉伊卡哇觀眾超150萬人",
     "치이카와 영화를 본 사람은 몇 명이 넘어요? A. 15만 명 · B. 150만 명 · C. 1,500만 명", size=20, gap=7)
e.head("B · 말 넣기", 25)
e.glossline("빈칸에 알맞은 말을 넣으세요.")
e.ex("B1", "完成句子", "컴백", "컴백＝發新專輯回歸",
     "가수가 새 앨범을 내고 돌아오는 것을 ___이라고 해요.", instr="填空", size=20, gap=7)
e.ex("B1", "完成句子", "타이틀곡", "專輯的代表歌叫主打歌",
     "앨범의 대표 노래를 ___이라고 해요.", instr="填空", size=20, gap=7)
e.ex("B1", "完成句子", "자정", "자정＝夜裡12點",
     "밤 12시를 ___이라고 해요.", instr="填空", size=20, gap=7)
e.ex("B1", "完成句子", "관객", "관객＝看電影的人",
     "영화를 본 사람을 ___이라고 해요.", instr="填空", size=20, gap=7)
e.ex("B1", "完成句子", "누적", "누적＝迄今合計的數",
     "지금까지 모두 합친 숫자를 ___라고 해요.", instr="填空", size=20, gap=7)
e.head("C · 숫자와 날짜", 25)
e.glossline("5면의 숫자로 답하세요.")
e.ex("B1", "完成句子", "6", "專輯週一傍晚6點發行",
     "앨범은 월요일 저녁 ___시에 나왔어요.", instr="填空", size=20, gap=7)
e.ex("B1", "完成句子", "34", "在Melon從第34位起步",
     "노래는 멜론에서 ___위로 시작했어요.", instr="填空", size=20, gap=7)
e.ex("B1", "完成句子", "3", "吉伊卡哇17日趨勢第3",
     "치이카와는 17일 Google 트렌드 한국에서 ___위였어요.", instr="填空", size=20, gap=7)
e.ex("B1", "完成句子", "1,000", "吉伊卡哇被搜1,000次以上",
     "치이카와는 ___회 이상 검색됐어요.", instr="填空", size=20, gap=7)
e.head("D · 문장 만들기", 25)
e.glossline("말을 바른 순서로 놓아 문장을 만드세요.")
e.ex("B1", "造句", "엔믹스는 월요일에 돌아왔어요.", "語序：主語+時間+動詞",
     "엔믹스는 / 월요일에 / 돌아왔어요 → ___", instr="造句", size=20, gap=7)
e.ex("B1", "造句", "노래가 자정에 5위가 됐어요.", "午夜成了第5位",
     "노래가 / 자정에 / 5위가 됐어요 → ___", instr="造句", size=20, gap=7)
e.ex("B1", "造句", "우리는 영화관에서 치이카와를 봐요.", "動作場所用「에서」",
     "우리는 / 영화관에서 / 치이카와를 봐요 → ___", instr="造句", size=20, gap=7)
e.ex("B1", "造句", "팬들이 노래를 들어요.", "主語+賓語+動詞的語序",
     "팬들이 / 노래를 / 들어요 → ___", instr="造句", size=20, gap=7)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-cheongnyeon.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 깊이 읽기 (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("깊이 읽기 · 深讀", "Lucerna", "레벨 B2 · 단풍 절정은 왜 두 개일까요 · 紅葉巔峰為什麼有兩個")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-feature")
f.title("설악산 단풍 절정은 20일? 25일?", 37)
f.byline("Lucerna 편집부 · 읽기 레벨: B2")
f.para("이번 주, 강원도의 산은 단풍으로 물들어요. 그런데 신문과 인터넷에서 설악산 단풍 절정 날짜가 두 개예요. 어떤 곳은 10월 20일, 어떤 곳은 10월 25일이라고 해요. 어느 쪽이 맞을까요?")
f.para("첫 번째 날짜는 산림청과 국립수목원의 지도예요. 이 지도는 9월 22일에 나왔어요. 이 지도에서는 잎의 50% 이상이 물든 때를 절정으로 봐요. 설악산 단풍의 절정은 20일이에요.")
f.para("두 번째 날짜는 웨더아이와 국립공원공단의 예상이에요. 이쪽은 산 전체를 봐요. 산 전체 잎의 약 80%가 물들 때를 절정으로 세요. 그래서 날짜가 25일로 늦어져요.")
f.para("지리산은 산림청의 셈법으로 25일쯤이 절정이에요. 같은 산, 같은 단풍인데 날짜가 다른 이유는 '절정'을 세는 기준이 다르기 때문이에요.")
f.para("그래서 단풍 소식을 읽을 때는 날짜만 보지 마세요. 어떤 기준으로 센 날짜인지 먼저 확인하세요. 두 날짜는 모두 맞을 수 있어요. 보고 싶은 모습이 50%의 단풍인지 80%의 단풍인지 생각하면, 여행 날짜를 정하기 쉬워요.")
f.para("50%의 단풍은 색이 물들기 시작하는 모습이에요. 80%의 단풍은 산 전체가 빨갛고 노랗게 물든 모습이에요. 두 모습은 모두 아름다워요. 여러분은 어느 쪽이 좋아요?")
f.para("단풍은 북쪽의 높은 산에서 시작해요. 그리고 천천히 남쪽으로 내려가요. 설악산과 지리산은 그 시작을 알려 주는 산이에요.")
f.gloss("물들다 染（紅） · 기준 標準 · 세다 數、計算 · 셈법 算法 · 전체 整體。")
f.end_report()

# ---- comparison table (cols 0-2) ----
ty = 1210
p.text(MX, ty + 26, "두 예상 한눈에 보기 · 兩種預報一表看清", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ty + 40, GOLD, 2)
rows = [
    ("구분", "산림청 · 국립수목원", "웨더아이 · 국립공원공단"),
    ("설악산 절정", "10월 20일", "10월 25일"),
    ("절정의 기준", "잎 50% 이상 물들 때", "산 전체 약 80% 물들 때"),
    ("지리산 절정", "10월 25일쯤", "—"),
]
tw = [300, 544, 544]
yy = ty + 58
for r, (c0, c1, c2) in enumerate(rows):
    x0 = MX
    for j, cell in enumerate((c0, c1, c2)):
        hdr = (r == 0)
        p.rect(x0, yy, tw[j], 52, fill=DARK if hdr else (BOX if r % 2 else "#f1ead6"), stroke=LINE, sw=1.1)
        p.text(x0 + 18, yy + 35, cell, 21 if not hdr else 20, "sans" if hdr else "serif", hdr,
               "#f3edda" if hdr else INK)
        x0 += tw[j]
    yy += 52
p.para(MX, yy + 30, "표의 자료: 산림청·국립수목원의 지도 (9월 22일)와 웨더아이·국립공원공단의 예상. 지리산은 산림청의 셈법이에요.", 19.5, "serif", False, GREY, 1388, 1.4)

# col 3: autumn image + how-to-read box
ix = COLX[3]
image(p, "autumn.jpg", ix, 200, CW, 240)
cy3 = caption(p, ix, 440, CW, "가을 단풍이 든 산골짜기. 절정의 날짜는 세는 기준에 따라 달라요.",
              "사진: lumoplank — CC0 (Wikimedia Commons) · 자료 사진")
howto = ["① 날짜를 봐요", "② 기준을 봐요", "③ 두 자료를 비교해요"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in howto) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "예보 읽는 법", 24, "sans", True, OLIVE)
yy3 += 52
for t in howto:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", sy3 + sh)

# ---- P6 exercises ----
ey = 1560
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "연습 · 第 6 版練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · 표 읽기", 25)
e.glossline("6면의 표와 글을 보고 답하세요.")
e.ex("B2", "單選", "A", "山林廳地圖雪嶽山20日",
     "산림청 지도로 설악산 절정은 며칠이에요? A. 20일 · B. 25일 · C. 22일", size=20, gap=7)
e.ex("B2", "單選", "B", "山林廳標準是葉子50%以上",
     "산림청의 절정 기준은 뭐예요? A. 잎 80% · B. 잎 50% 이상 · C. 첫 단풍", size=20, gap=7)
e.ex("B2", "單選", "A", "Weatheri方看全山約80%",
     "웨더아이 쪽의 기준은 뭐예요? A. 산 전체 약 80% · B. 나무 한 그루 · C. 잎 50%", size=20, gap=7)
e.ex("B2", "單選", "A", "山林廳地圖9月22日發布",
     "산림청 지도는 언제 나왔어요? A. 9월 22일 · B. 10월 14일 · C. 10월 20일", size=20, gap=7)
e.ex("B2", "單選", "B", "智異山按山林廳算法約25日",
     "지리산 절정은 언제예요? (산림청 셈법) A. 20일 · B. 25일쯤 · C. 11월", size=20, gap=7)
e.head("B · 이해", 25)
e.glossline("글의 생각을 고르세요.")
e.ex("B2", "單選", "B", "日期不同因標準不同",
     "날짜가 두 개인 이유는 뭐예요? A. 한쪽이 틀려서 · B. 기준이 달라서 · C. 산이 두 개라서", size=20, gap=7)
e.ex("B2", "單選", "B", "先確認標準再看日期",
     "이 글은 무엇을 권해요? A. 날짜만 보세요 · B. 기준을 확인하세요 · C. 가지 마세요", size=20, gap=7)
e.ex("B2", "單選", "B", "兩個日期都可能對",
     "두 날짜에 대한 이 글의 생각은 뭐예요? A. 하나는 틀렸어요 · B. 둘 다 맞을 수 있어요 · C. 둘 다 틀렸어요", size=20, gap=7)
e.ex("B2", "單選", "B", "看80%紅葉25日更接近",
     "산 전체 80%의 단풍을 보고 싶으면 어느 날짜가 좋아요? A. 20일 · B. 25일 · C. 22일", size=20, gap=7)
e.head("C · 말 넣기", 25)
e.glossline("빈칸에 알맞은 말을 넣으세요.")
e.ex("B2", "完成句子", "물들어요", "葉子變紅叫물들어요",
     "가을이 되면 잎이 빨갛게 ___.", instr="填空", size=20, gap=7)
e.ex("B2", "完成句子", "기준", "日期不同因기준不同",
     "날짜가 다른 이유는 ___이 다르기 때문이에요.", instr="填空", size=20, gap=7)
e.ex("B2", "完成句子", "절정", "절정＝最美的時節",
     "단풍이 가장 아름다운 때를 ___이라고 해요.", instr="填空", size=20, gap=7)
e.ex("B2", "完成句子", "세는", "按樹種分別數日期的方法",
     "이 지도는 나무 종류별로 날짜를 ___ 방법이에요.", instr="填空", size=20, gap=7)
e.ex("B2", "完成句子", "비교해", "把兩份資料比較著看",
     "두 자료를 ___ 보세요.", instr="填空", size=20, gap=7)
e.head("D · 맞다 틀리다", 25)
e.glossline("맞으면 O, 틀리면 X를 고르세요.")
e.ex("B2", "判斷", "X", "山林廳標準是50%，非80%",
     "산림청의 절정 기준은 잎의 80%예요.", instr="判斷", size=20, gap=7)
e.ex("B2", "判斷", "O", "Weatheri方看整座山",
     "웨더아이와 국립공원공단은 산 전체를 봐요.", instr="判斷", size=20, gap=7)
e.ex("B2", "判斷", "O", "智異山25日晚於雪嶽山20日",
     "지리산의 절정은 설악산보다 늦어요. (산림청 셈법)", instr="判斷", size=20, gap=7)
e.ex("B2", "判斷", "X", "標準不同日期也會不同",
     "절정 날짜는 기준이 달라도 항상 같아요.", instr="判斷", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-gipi.svg")
print("P6 saved, exercises so far:", len(REG))
