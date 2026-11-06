# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ko-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 시험과 답 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("시험과 답 · Test and answers", "Lucerna", "제8면 · 이번 주의 큰 시험 + 모든 답")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 이번 주 연표", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "Champi is this year's Typhoon No. 30",
     "태풍 참피는 제___호 태풍이에요. (A. 30 · B. 13)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "KMA changed the forecast on the 21st",
     "기상청이 예보를 바꾼 날은 10월 ___일이에요. (A. 20 · B. 21)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "The CSAT is on Thursday, Nov 19",
     "수능은 11월 ___일이에요. (A. 19 · B. 29)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "The Silver Grass Festival runs until Oct 23",
     "서울억새축제는 10월 ___일까지예요. (A. 23 · B. 25)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "The playoff starts on Sunday",
     "플레이오프는 ___요일에 시작해요. (A. 토 · B. 일)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "It climbed to No. 5 by midnight",
     "엔믹스의 노래는 자정에 ___위까지 올라갔어요. (A. 34 · B. 5)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Seoraksan peaks on the 20th on the Forest Service map",
     "산림청 지도로 설악산 절정은 10월 ___일이에요. (A. 20 · B. 25)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Chiikawa admissions passed 1.5 million",
     "치이카와 영화의 관객은 ___만 명이 넘어요. (A. 150 · B. 15)", size=13.8, gap=0)
f.head("B · 일반 문제", 21, OLIVE, 5)
f.ex("A2", "multiple choice", "A", "551,864 candidates this year",
     "올해 수험생은 몇 명이에요? A. 551,864명 · B. 1,312명 · C. 75,000명", size=13.8, gap=0)
f.ex("B1", "multiple choice", "B", "1,312 test sites nationwide",
     "시험장은 전국에 몇 곳이에요? A. 551,864곳 · B. 1,312곳 · C. 312곳", size=13.8, gap=0)
f.ex("B1", "multiple choice", "A", "Top winds of 59 metres per second",
     "참피의 최대 풍속은 얼마예요? A. 초속 59미터 · B. 초속 30미터 · C. 905미터", size=13.8, gap=0)
f.ex("A2", "multiple choice", "B", "Emoticons for the first 75,000 people",
     "청송 이모티콘은 몇 명까지 받을 수 있어요? A. 7,500명 · B. 75,000명 · C. 750,000명", size=13.8, gap=0)
f.ex("A2", "multiple choice", "C", "Chiikawa was No. 3 in trends on the 17th",
     "치이카와는 10월 17일 트렌드에서 몇 위였어요? A. 1위 · B. 5위 · C. 3위", size=13.8, gap=0)
f.ex("A2", "multiple choice", "A", "The 25th Seoul Silver Grass Festival",
     "서울억새축제는 몇 회예요? A. 25회 · B. 20회 · C. 30회", size=13.8, gap=0)
f.ex("B1", "multiple choice", "B", "Weatheri puts Seoraksan's peak on Oct 25",
     "웨더아이와 국립공원공단의 설악산 절정은 며칠이에요? A. 10월 20일 · B. 10월 25일 · C. 11월 4일", size=13.8, gap=0)
f.ex("A2", "multiple choice", "A", "The Korean Series starts Nov 2",
     "한국시리즈는 언제부터예요? A. 11월 2일 · B. 10월 25일 · C. 11월 19일", size=13.8, gap=0)
f.head("C · 읽고 답하기", 21, OLIVE, 5)
f.para("민준이는 대학생이에요. 이번 주 금요일에 친구와 하늘공원에 가요. 억새축제의 마지막 날이에요. 토요일에는 집에서 태풍 소식을 봐요. 일요일에는 야구 플레이오프를 봐요. 민준이는 KIA를 응원해요.", 15, lh=1.3, split=False)
f.ex("A2", "multiple choice", "B", "Minjun goes to Haneul Park on Friday",
     "민준이는 금요일에 어디에 가요? A. 청송 · B. 하늘공원 · C. 제주도", size=13.8, gap=0)
f.ex("A2", "multiple choice", "A", "Because it is the festival's last day",
     "금요일에 하늘공원에 왜 가요? A. 억새축제 마지막 날이라서 · B. 사과를 사려고 · C. 야구를 보려고", size=13.8, gap=0)
f.ex("A2", "multiple choice", "B", "He watches the typhoon news at home on Saturday",
     "토요일에 민준이는 무엇을 해요? A. 산에 가요 · B. 태풍 소식을 봐요 · C. 시험을 봐요", size=13.8, gap=0)
f.ex("B1", "multiple choice", "C", "Minjun roots for KIA",
     "민준이는 어느 팀을 응원해요? A. LG · B. 삼성 · C. KIA", size=13.8, gap=0)
f.head("D · 문장 만들기", 21, OLIVE, 5)
f.ex("A2", "sentence building", "저는 금요일에 하늘공원에 가요.", "Word order: subject + time + place + verb",
     "저는 / 금요일에 / 하늘공원에 가요 → ___", instr="Build a sentence", size=13.8, gap=0)
f.ex("A2", "sentence building", "태풍이 북쪽으로 오고 있어요.", "북쪽으로 = towards the north",
     "태풍이 / 북쪽으로 / 오고 있어요 → ___", instr="Build a sentence", size=13.8, gap=0)
f.ex("B1", "sentence building", "우리는 단풍을 보러 가요.", "보러 가요 = go to see",
     "우리는 / 단풍을 / 보러 가요 → ___", instr="Build a sentence", size=13.8, gap=0)
f.ex("B1", "sentence building", "누나는 도서관에서 공부해요.", "에서 marks the place where an action happens",
     "누나는 / 도서관에서 / 공부해요 → ___", instr="Build a sentence", size=13.8, gap=0)
f.head("E · 번역", 21, OLIVE, 5)
f.ex("A2", "translation", "The typhoon's path can still change.", "From page 1",
     "태풍의 경로는 아직 바뀔 수 있어요. → ___", instr="Translate", size=13.8, gap=0)
f.ex("A2", "translation", "There are 29 days left until the exam.", "From page 2",
     "시험까지 29일이 남았어요. → ___", instr="Translate", size=13.8, gap=0)
f.ex("B1", "translation", "주말에는 최신 날씨를 확인하세요.", "From page 1",
     "Please check the latest weather this weekend. → ___", instr="Translate", size=13.8, gap=0)
f.ex("B2", "translation", "저는 금요일에 하늘공원에 억새를 보러 가요.", "From page 3",
     "On Friday I go to Haneul Park to see the silver grass. → ___", instr="Translate", size=13.8, gap=0)
f.head("F · 이번 주의 말", 21, OLIVE, 5)
f.match_set("B2", "matching",
            ["북상하다", "절정", "진로", "수험생"],
            ["시험을 보는 학생",
             "북쪽으로 올라가다",
             "가장 아름다운 때",
             "태풍이 가는 길"],
            ["b", "c", "d", "a"],
            ["북상하다 = to move north (b)", "절정 = the peak, the best time (c)", "진로 = path, course (d)", "수험생 = test-taker (a)"],
            instr="Match word to meaning")
f.head("G · 도서관에서", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "The CSAT is on Nov 19",
     "— 수능이 언제예요? — 11월 ___이에요. (A. 19일 · B. 21일)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "Subways run more often on test-day morning",
     "— 시험 날 아침에 지하철은요? — 더 자주 ___. (A. 쉬어요 · B. 다녀요)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Planes do not land during the listening test",
     "— 비행기는요? — 듣기 시간에는 뜨거나 ___ 않아요. (A. 내리지 · B. 보지)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "D-29 means 29 days left",
     "— D-29가 뭐예요? — 시험까지 29일이 ___ 뜻이에요. (A. 지났다는 · B. 남았다는)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "Cheer: 힘내세요! ('You can do it!')",
     "— 응원 한마디 해 주세요. — ___! (A. 안녕히 가세요 · B. 힘내세요)", size=13.8, gap=0)
f.head("H · 써 보기", 21, OLIVE, 5)
MODELO = ("나의 가을 주말은 야구와 단풍의 주말이에요. "
          "토요일 아침에는 먼저 태풍 소식을 확인해요. 바람이 강하면 밖에 나가지 않아요. "
          "오후에는 집에서 야구 플레이오프를 봐요. 저는 KIA를 응원해요. "
          "일요일에는 친구와 산에 가요. 단풍이 절정이라서 아주 예뻐요. "
          "사진을 많이 찍고 싶어요. 집에 돌아와서는 찍은 사진을 보고 짧은 일기를 써요. "
          "가을은 짧지만 재미있는 일이 많은 계절이에요.")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"A writing task (there is no single correct answer). A model of {NCHARS} characters is below.")
f.ex("B1", "writing", "(open task — model text below)", f"Model text in section H on this page ({NCHARS} characters)",
     "「나의 가을 주말」에 대해 150~200자로 쓰세요. 날씨, 야구, 단풍 중에서 하나를 고르세요.", instr="Write", size=13.8, gap=0)
f.para("예: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 답 =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "답 · Answer key — grouped by page; find your item number", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Each item has a short English note · ✓ marks the model-writing item", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    head_txt = f"— 제{pg}면 —"
    first_ = by_page[pg][0]
    ftxt = f"{first_['n']}. {first_['key']} — {first_['note']}"
    if first_["type"] == "writing":
        ftxt = f"{first_['n']}. ✓ {first_['note']}"
    # keep-with-next (independent proofread fix): a group heading must not be
    # orphaned at a column foot — if heading + its first key do not both fit
    # in the current column, start the group in the next column. The heading's
    # true footprint in para() is size (first baseline) + line stack + gap.
    need = (13.3 + af._ph(head_txt, 13.3, "sans", True, af.w, 1.16) + 2
            + af._ph(ftxt, 13.3, "serif", False, af.w, 1.16) + 0.5)
    if af.y + need > af.bottom and af.ci < len(af.cols) - 1:
        af.ci += 1
        af.y = af.top
    af.para(head_txt, 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "writing":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-siheom.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model chars:", NCHARS)
