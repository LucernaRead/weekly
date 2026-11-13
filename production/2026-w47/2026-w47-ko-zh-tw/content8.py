# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 시험과 답 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("시험과 답　測驗與答案", "Lucerna", "제8면　이번 주의 큰 시험 + 모든 답")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　이번 주 연표", 21, OLIVE, 5)
f.ex("B1", "克漏字", "A", "泡菜日是11月22日星期日",
     "김치의 날은 11월 ___일이에요. (A. 22 · B. 19)", size=13.8, gap=0)
f.ex("B1", "克漏字", "A", "韓國高考在11月19日星期四",
     "수능은 11월 ___일이에요. (A. 19 · B. 29)", size=13.8, gap=0)
f.ex("B1", "克漏字", "A", "韓史檢定在11月28日星期六",
     "한능검 시험은 11월 ___일이에요. (A. 28 · B. 6)", size=13.8, gap=0)
f.ex("B1", "克漏字", "A", "泡菜節在11月20日星期五",
     "위킴 페스티벌은 11월 ___일이에요. (A. 20 · B. 22)", size=13.8, gap=0)
f.ex("B1", "克漏字", "A", "三星4勝1負奪冠",
     "삼성은 kt를 ___승 1패로 이겼어요. (A. 4 · B. 3)", size=13.8, gap=0)
f.ex("B1", "克漏字", "A", "四口之家泡菜成本199,456韓元",
     "김장비용은 4인 가족 기준 ___원이에요. (A. 199,456 · B. 219,071)", size=13.8, gap=0)
f.ex("B1", "克漏字", "A", "白菜20棵54,980韓元",
     "배추 20포기는 ___원이에요. (A. 54,980 · B. 74,800)", size=13.8, gap=0)
f.ex("B1", "克漏字", "A", "今年考生551,864人",
     "올해 수험생은 ___명이에요. (A. 551,864 · B. 1,312)", size=13.8, gap=0)
f.head("B　일반 문제", 21, OLIVE, 5)
f.ex("A2", "單選", "A", "今年考生551,864人",
     "올해 수험생은 몇 명이에요? A. 551,864명 · B. 1,312명 · C. 3,271명", size=13.8, gap=0)
f.ex("B1", "單選", "B", "考場全國1,312處",
     "시험장은 전국에 몇 곳이에요? A. 551,864곳 · B. 1,312곳 · C. 312곳", size=13.8, gap=0)
f.ex("B1", "單選", "A", "內藏山林業廳預報峰值11月4日",
     "내장산 산림청 예보의 절정은 언제예요? A. 11월 4일 · B. 11월 11일 · C. 10월 16일", size=13.8, gap=0)
f.ex("B1", "單選", "B", "內藏山Weatheri預報峰值11月11日",
     "내장산 웨더아이 예보의 절정은 언제예요? A. 11월 4일 · B. 11월 11일 · C. 11월 9일", size=13.8, gap=0)
f.ex("B1", "單選", "B", "頭輪山林業廳預報峰值11月11日",
     "두륜산 산림청 예보의 절정은 언제예요? A. 11월 4일 · B. 11월 11일 · C. 11월 9일", size=13.8, gap=0)
f.ex("B1", "單選", "A", "第1場kt以8比7獲勝",
     "한국시리즈 1차전은 어떻게 됐어요? A. kt 8대 7 승리 · B. 삼성 3대 2 승리 · C. 비로 취소", size=13.8, gap=0)
f.ex("B1", "單選", "A", "取消名額報名11月11日至13日",
     "한능검 취소 좌석 접수는 언제예요? A. 11월 11일부터 13일까지 · B. 11월 24일부터 · C. 11월 28일", size=13.8, gap=0)
f.ex("A2", "單選", "B", "山火注意期到12月15日",
     "산불조심기간은 언제까지예요? A. 11월 9일까지 · B. 12월 15일까지 · C. 11월 19일까지", size=13.8, gap=0)
f.head("C　읽고 답하기", 21, OLIVE, 5)
f.para("민준이는 수험생이에요. 수요일에 예비소집에 가요. 목요일에 수능을 봐요. 일요일에는 가족과 김치를 나눠 먹어요. 다음 주에는 한능검 시험을 준비해요. 민준이는 한국사를 좋아해요.", 15, lh=1.3, split=False)
f.ex("A2", "單選", "B", "民俊星期三去預備召集",
     "민준이는 수요일에 무엇을 해요? A. 단풍을 봐요 · B. 예비소집에 가요 · C. 시험을 봐요", size=13.8, gap=0)
f.ex("A2", "單選", "A", "星期四參加韓國高考",
     "목요일에 민준이는 무엇을 해요? A. 수능을 봐요 · B. 야구를 봐요 · C. 김치를 담가요", size=13.8, gap=0)
f.ex("A2", "單選", "B", "星期日和家人分享泡菜",
     "일요일에 민준이는 무엇을 해요? A. 시험을 봐요 · B. 가족과 김치를 나눠 먹어요 · C. 단풍을 봐요", size=13.8, gap=0)
f.ex("B1", "單選", "C", "下週準備韓史檢定",
     "다음 주에 민준이는 무엇을 준비해요? A. 수능 · B. 김치의 날 · C. 한능검 시험", size=13.8, gap=0)
f.head("D　문장 만들기", 21, OLIVE, 5)
f.ex("A2", "造句", "저는 수요일에 예비소집에 가요.", "語序：主語+時間+地點+動詞",
     "저는 / 수요일에 / 예비소집에 / 가요 → ___", instr="造句", size=13.8, gap=0)
f.ex("A2", "造句", "우리는 김치를 나눠 먹어요.", "主語+受詞+動詞的語序",
     "우리는 / 김치를 / 나눠 먹어요 → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "민준이는 한국사를 좋아해요.", "좋아하다 = 喜歡",
     "민준이는 / 한국사를 / 좋아해요 → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "수험생은 도서관에서 공부해요.", "動作場所用「에서」",
     "수험생은 / 도서관에서 / 공부해요 → ___", instr="造句", size=13.8, gap=0)
f.head("E　번역", 21, OLIVE, 5)
f.ex("A2", "翻譯", "11月22日是泡菜日。", "對照第2版",
     "11월 22일은 김치의 날이에요. → ___", instr="翻譯", size=13.8, gap=0)
f.ex("A2", "翻譯", "三星時隔12年奪冠。", "對照第4版",
     "삼성이 12년 만에 우승했어요. → ___", instr="翻譯", size=13.8, gap=0)
f.ex("B1", "翻譯", "11월 18일은 예비소집이에요.", "對照第5版",
     "11月18日是預備召集。→ ___", instr="翻譯", size=13.8, gap=0)
f.ex("B2", "翻譯", "일요일에는 가족과 김치를 나눠 먹어요.", "對照第8版C區",
     "我星期日和家人分享泡菜。→ ___", instr="翻譯", size=13.8, gap=0)
f.head("F　이번 주의 말", 21, OLIVE, 5)
f.match_set("B2", "配對",
            ["예비소집", "김치의 날", "발효", "우승"],
            ["김치가 익어가는 과정",
             "시험 전날에 모이는 일",
             "11월 22일의 기념일",
             "경기에서 1등을 하는 일"],
            ["b", "c", "a", "d"],
            ["예비소집 = 預備召集 b", "김치의 날 = 11月22日 c", "발효 = 發酵過程 a", "우승 = 奪冠 d"],
            instr="把詞和釋義配對")
f.head("G　도서관에서", 21, OLIVE, 5)
f.ex("B1", "克漏字", "A", "星期三去預備召集",
     "— 수요일에 무엇을 해요? — ___에 가요. (A. 예비소집 · B. 도서관)", size=13.8, gap=0)
f.ex("B1", "克漏字", "A", "泡菜日是11月22日",
     "— 김치의 날은 언제예요? — 11월 ___일이에요. (A. 22 · B. 19)", size=13.8, gap=0)
f.ex("B1", "克漏字", "A", "韓史檢定在11月28日",
     "— 한능검 시험은 언제예요? — 11월 ___일이에요. (A. 28 · B. 24)", size=13.8, gap=0, bw=334)
f.ex("B1", "克漏字", "A", "四口之家泡菜成本199,456韓元",
     "— 김장비용은 얼마예요? — ___원이에요. (A. 199,456 · B. 219,071)", size=13.8, gap=0)
f.ex("B1", "克漏字", "A", "成績12月11日公布",
     "— 수능 성적은 언제 나와요? — 12월 ___일에 나와요. (A. 11 · B. 19)", size=13.8, gap=0, bw=354)
f.head("H　써 보기", 21, OLIVE, 5)
MODELO = ("나의 김치의 날은 가족과 함께 시작해요. "
          "아침에는 시장에서 배추와 양념을 사요. "
          "점심에는 가족과 김치를 담가요. "
          "양념을 버무리면 손이 차가워지지만 마음은 따뜻해져요. "
          "오후에는 친구에게 김치를 나눠 줘요. "
          "저녁에는 갓 담근 김치와 밥을 먹어요. "
          "김치의 날은 나누는 날이에요. "
          "김치가 익으면 김치찌개를 끓여 먹어요. "
          "겨울 밥상에는 김치가 꼭 있어야 해요. "
          "내년에도 가족과 함께 김장을 담그고 싶어요.")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"쓰기 문제예요 (정답은 하나가 아니에요). 아래에 {NCHARS}자의 예가 있어요.")
f.ex("B1", "寫作", "（開放題，範文如下）", f"本版H區範文（{NCHARS}字）",
     "「나의 김치의 날」에 대해 150~200자로 쓰세요. 김치를 담그는 일, 나누는 일, 먹는 일 중에서 하나를 고르세요.", instr="寫作", size=13.8, gap=0)
f.para("예: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ---- P8 photo (W47 new: P8 gets a PD image) ----
# The exercise flow ends partway down col 3 (W46: y=865, bottom 1252);
# place the photo in that free space in col 3, below the flow end.
pix, piy = COLX[3], f.y + 16
image(p, "kimchi-making2.jpg", pix, piy, CW, 220)
cy8 = caption(p, pix, piy + 220, CW,
        "김치를 담그는 손. 김장철에 찍은 사진이에요.",
        "사진: Anattadairy — CC0 (Wikimedia Commons) · 자료 사진")
print("P8 photo ends", cy8, "flow ended col", f.ci, "y", f.y)

# ================= 답 =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "답　參考答案 — 按版面分頁排列，找到題號即可", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "每題附一句繁體中文簡析　帶 ✓ 的為範文題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 제{pg}면 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "寫作":
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
