# -*- coding: utf-8 -*-
# W48 zh-tw core, VOL.5: P8 test & keys (keys generated from the registry).
# Test flow A-E, then a writing strip (task + model + photo), then keys.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w48/2026-w48-zh-tw-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P8 · test & keys
CURPAGE[0] = 8
p = BSPage4()
p.band("測驗與答案　테스트와 정답", "Lucerna", "第8版　本週大測驗　全部答案　이번 주 큰 테스트와 모든 정답")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 200, 1050, tag="P8-ex")
f.head("A　判斷對錯　맞거나 틀리거나", 21, OLIVE, 5)
f.ex("A2", "完形單選", "A", "퍼레이드는 일요일 11월 22일 14:00예요.",
     "封王遊行11月22日下午2點出發。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "시상식은 11월 22일이에요. 11월 15일이 아니에요.",
     "金馬獎頒獎典禮在11月15日。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Disney 크리스마스는 11월 17일에 시작해요.",
     "香港迪士尼聖誕11月17日開始。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "deTour는 11월 29일에 막을 내려요.",
     "deTour設計節11月29日閉幕。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "샤오쉐는 11월 22일이에요.",
     "小雪在11月22日。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B2", "完形單選", "A", "Kenny G가 11월 24일에 재즈 페스티벌을 마무리해요.",
     "爵士音樂節11月24日由肯尼·基收尾。(A. 對 · B. 錯)", size=13.8, gap=0)
f.head("B　本週大測驗　이번 주 큰 퀴즈", 21, OLIVE, 5)
f.ex("A2", "單選", "B", "퍼레이드는 Taipei Dome에서 끝나요.",
     "封王遊行終點是哪裡？ A. 天母棒球場 · B. 台北大巨蛋 · C. 駁二", size=13.8, gap=0)
f.ex("A2", "單選", "B", "11월 20일~29일은 모두 10일이에요.",
     "deTour設計節一共幾天？ A. 9天 · B. 10天 · C. 11天", size=13.8, gap=0)
f.ex("B1", "單選", "A", "Xiaoxue는 스물네 절기 중 스무 번째예요.",
     "小雪是二十四節氣的第幾個？ A. 第20個 · B. 第2個 · C. 第24個", size=13.8, gap=0)
f.ex("B1", "單選", "B", "메인 라이트 쇼는 한 번에 5분이에요.",
     "耶誕城主燈秀每次幾分鐘？ A. 30分鐘 · B. 5分鐘 · C. 1小時", size=13.8, gap=0)
f.ex("B1", "單選", "C", "출품작 587편.",
     "金馬獎有幾部影片報名？ A. 87部 · B. 57部 · C. 587部", size=13.8, gap=0)
f.ex("B1", "單選", "A", "11월 18일~1월 5일은 49일이에요.",
     "中環聖誕小鎮一共幾天？ A. 49天 · B. 48天 · C. 45天", size=13.8, gap=0)
f.ex("B2", "單選", "A", "11월 17일~1월 3일은 48일이에요.",
     "迪士尼聖誕一共幾天？ A. 48天 · B. 38天 · C. 58天", size=13.8, gap=0)
f.ex("B2", "單選", "B", "e스포츠 결승전은 11월 28일~29일에 열려요.",
     "電競總決賽在哪兩天？", opts=["A. 11月27、28日", "B. 11月28、29日", "C. 11月29、30日"], size=13.8, gap=0)
f.ex("B2", "單選", "A", "100점이면 EasyCard 충전금으로 바꿀 수 있어요.",
     "滿幾個U幣可以換成悠遊卡儲值金？ A. 100個 · B. 50個 · C. 10個", size=13.8, gap=0)
f.ex("B2", "單選", "B", "11월 23일부터 11월 27일까지는 4일이에요.",
     "MegaBox 11月23日開幕，黑色星期五11月27日，中間隔幾天？", opts=["A. 3天", "B. 4天", "C. 5天"], size=13.8, gap=0)
f.head("C　完成句子　문장 완성하기", 21, OLIVE, 5)
f.ex("A2", "完成句子", "封王", "우승을 확정하는 것은 封王이에요.",
     "拿下總冠軍，叫___。", instr="빈칸 채우기", size=13.8, gap=0)
f.ex("A2", "完成句子", "黑色", "《善男信女》는 블랙 코미디예요.",
     "《善男信女》是香港___喜劇。", instr="빈칸 채우기", size=13.8, gap=0)
f.ex("B1", "完成句子", "點收", "상자를 열기 전에 배송을 확인해요.",
     "包裹到了，先___再拆箱。", instr="빈칸 채우기", size=13.8, gap=0)
f.ex("B1", "完成句子", "入圍", "후보에 오르는 것은 入圍예요.",
     "被選進得獎名單，叫___。", instr="빈칸 채우기", size=13.8, gap=0)
f.ex("B1", "完成句子", "遊行", "축하 행진은 遊行이에요.",
     "大家走上街頭慶祝，叫___。", instr="빈칸 채우기", size=13.8, gap=0)
f.ex("B1", "完成句子", "集點", "포인트를 모으는 것은 集點이에요.",
     "每次運動累積點數，叫___。", instr="빈칸 채우기", size=13.8, gap=0)
f.ex("B1", "完成句子", "主燈秀", "메인 라이트 쇼는 30분마다 반복돼요.",
     "耶誕城的___每半小時一次。", instr="빈칸 채우기", size=13.8, gap=0)
f.ex("B1", "完成句子", "市集", "시장은 市集이에요.",
     "賣東西、逛街的地方，叫___。", instr="빈칸 채우기", size=13.8, gap=0)
f.ex("B2", "完成句子", "時間軸", "타임라인을 읽고 일주일을 계획하세요.",
     "先看___，再決定去哪一件。", instr="빈칸 채우기", size=13.8, gap=0)
f.ex("B2", "完成句子", "閉幕", "deTour는 11월 29일에 막을 내려요.",
     "11月29日也是deTour設計節___的日子。", instr="빈칸 채우기", size=13.8, gap=0)
f.head("D　讀一讀，答一答　읽고 답하기", 21, OLIVE, 5)
f.para("阿玲住在香港。11月29日（週日）早上，她先查好設計節的時間，中午去中環PMQ看deTour最後一天。下午，她去國際金融中心看city'super聖誕品味嘉年華，嘉年華中午12點到晚上9點。晚上回家，她和媽媽一起看耶誕城主燈秀的照片。同一天，新北耶誕城有電競總決賽。", 15, lh=1.3, split=False)
f.ex("A2", "單選", "A", "그녀는 정오에 Central의 PMQ에서 deTour를 봐요.",
     "阿玲週日中午去哪裡？ A. 中環PMQ · B. 天母棒球場 · C. 駁二", size=13.8, gap=0)
f.ex("B1", "單選", "A", "카니발은 12:00~21:00에 열려요.",
     "city'super嘉年華幾點開始？ A. 12:00 · B. 11:00 · C. 9:00", size=13.8, gap=0)
f.ex("B1", "單選", "A", "카니발은 IFC에서 열려요.",
     "city'super嘉年華在哪裡？ A. 國際金融中心商場 · B. 九龍灣MegaBox · C. 中環皇后像廣場", size=13.8, gap=0)
f.ex("B1", "單選", "A", "순서: 디자인 페스티벌 먼저, 그다음 카니발이에요.",
     "這一天她的順序是？", opts=["A. 先看設計節，再看嘉年華", "B. 先看嘉年華，再看設計節", "C. 只看電競總決賽"], size=13.8, gap=0)
f.ex("B2", "單選", "A", "11월 29일은 deTour의 마지막 날이에요.",
     "11月29日還是哪一個日子？", opts=["A. deTour設計節最後一天", "B. 金馬獎頒獎典禮", "C. 爵士音樂節開幕"], size=13.8, gap=0)
f.head("E　情景說話　상황 속에서 말하기", 21, OLIVE, 5)
f.ex("B1", "完形單選", "A", "퍼레이드는 일요일 11월 22일이에요.",
     "— 封王遊行哪天出發？ — ___出發。(A. 11月22日 · B. 11月15日)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "deTour는 11월 29일에 막을 내려요.",
     "— deTour設計節哪天閉幕？ — ___(A. 11月29日 · B. 11月22日)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "메인 라이트 쇼는 한 번에 5분이에요.",
     "— 主燈秀每次幾分鐘？ — ___(A. 5分鐘 · B. 30分鐘)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "시상식은 11월 22일이에요.",
     "— 金馬獎哪天頒獎？ — ___(A. 11月22日 · B. 11月15日)", size=13.8, gap=0)
f.ex("A2", "完形單選", "A", "Xiaoxue는 스물네 절기 중 스무 번째예요.",
     "— 小雪是第幾個節氣？ — ___(A. 第20個 · B. 第2個)", size=13.8, gap=0)
f.ex("B2", "完形單選", "A", "주말이 되면 Christmasland가 활기를 띠어요. 一…就….",
     "— 一到週末，耶誕城就怎麼樣？ — ___(A. 很熱鬧 · B. 沒有人)", size=13.8, gap=0)
f.end_report()

# ================= F · writing strip (task + model) =================
# The notes photo fills the flow's last column below the last test item.
img_y = int(f.y) + 30
image(p, "notes.jpg", COLX[3], img_y, CW, 200)
caption(p, COLX[3], img_y + 206, CW, "寫下來，才記得住（資料照片）。",
        "사진: 연필로 메모하기 — CC0 (Unsplash)")
MODELO = ("早上我先列好清單，查好設計節的時間，才出門。"
          "11月29日是星期日，也是deTour設計節的最後一天。中午，我去中環PMQ看設計節，免費入場。"
          "下午，我去國際金融中心看聖誕品味嘉年華。晚上回家，我和媽媽一起看耶誕城主燈秀的照片。"
          "一天看了兩件大事，聖誕節快到了，出門要記得保暖。")
NCHARS = len(MODELO.replace(" ", ""))
print("MODEL chars:", NCHARS)
wy = 1050 + 30  # full-width strip below the test flow (bottom 1050)
p.hline(MX, RIGHT, wy - 16, OLIVE, 2)
wx, ww = span_x(0, 3)
p.text(wx, wy + 26, "F　寫一寫　써 보기", 25, "sans", True, OLIVE)
n = reg_ex("B2", "寫作", "(開放題，範文如下)", f"개방형 과제 — 모범 답안은 위 F란에 실려 있어요 ({NCHARS}자)")
chip(p, wx, wy + 48, "B2")
p.text(wx + 72, wy + 48 + 23, f"{n}.", 24, "sans", True, OLIVE)
p.text(wx + 142, wy + 48 + 23, "작문", 19.5, "sans", False, GREY)
ly = p.para(wx, wy + 48 + 36 + 20, "寫一寫《我的一天：11月29日》：11月29日你做了什麼？看了哪一件大事？天氣怎麼樣？寫 120～180 字。", 20, "serif", False, INK, ww, 1.45) + 6
ly = p.para(wx, ly + 18, "모범 답안: " + MODELO, 16, "serif", False, INK, ww, 1.35)
strip_end = ly
print("P8 writing strip ends", strip_end, "(flow ended", f.y, ")")

# ================= keys =================
ky = strip_end + 30
p.hline(MX, RIGHT, ky - 14, OLIVE, 2)
p.text(MX, ky + 26, "答案　정답 — 페이지 순서대로, 각 문항마다 짧은 한국어 설명과 함께", 25, "sans", True, OLIVE)
p.text(RIGHT, ky + 26, "모든 설명은 한국어　✓ = 작문 모범 답안", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 제{pg} —", 13.0, "sans", True, OLIVE, lh=1.12, gap=1, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "寫作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.0, "sans", False, INK, lh=1.12, gap=1, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, exercises total:", len(REG))
