# -*- coding: utf-8 -*-
# W47 zh-tw core, VOL.4: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言　언어", "Lucerna", "語言聚焦　三個級別　三個主題　세 단계, 세 가지 주제")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　遊行的話　퍼레이드 단어", 25)
a.para("퍼레이드에서 네 가지 유용한 단어를 배울 수 있어요. 遊行(퍼레이드), 封王(우승 확정), 夜間(밤), 終點(끝나는 곳). 한 번 외우면 어떤 퍼레이드든 이해가 돼요.", 22)
a.expl("퍼레이드 단어 네 가지: 遊行, 封王, 夜間, 終點.")
a.para("遊行은 거리를 행진하는 축하 행진이에요. 封王은 우승하는 것을 뜻해요. 夜間은 밤을 뜻해요. 야간 퍼레이드는 19:00에 시작해요. 終點은 퍼레이드가 끝나는 곳, Taipei Dome이에요.", 22)
a.ex("A2", "完成句子", "遊行", "축하 행진은 遊行이에요.",
     "大家走上街頭慶祝，叫___。", instr="빈칸 채우기", size=22, gap=10)
a.ex("A2", "單選", "A", "퍼레이드는 11월 22일 14:00에 출발해요.",
     "封王遊行幾點出發？", opts=["A. 下午2點", "B. 上午2點", "C. 晚上7點"], size=22, gap=10)
a.ex("A2", "完成句子", "封王", "우승을 확정하는 것은 封王이에요.",
     "拿下總冠軍，叫___。", instr="빈칸 채우기", size=22, gap=10)
a.ex("A2", "單選", "A", "야간 퍼레이드는 19:00에 시작해요.",
     "夜間遊行晚上幾點開始？", opts=["A. 晚上7點", "B. 下午2點", "C. 上午10點"], size=22, gap=10)
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
b.head("B1　電影與鋼雕　영화와 강철", 25)
b.para("영화와 강철이 이번 주 헤드라인을 나눠요. 단어를 묶으면 잘 외워져요. 영화（入圍、頒獎、星光大道）와 강철（鋼雕、保險箱、勞動記憶）.", 22)
b.expl("단어를 묶어 봐요. 영화(入圍/頒獎), 강철(鋼雕/保險箱).")
b.para("入圍는 후보에 오르는 것을 뜻해요. 頒獎은 상을 수여하는 것을 뜻해요. 星光大道는 시상식 전의 레드카펫이에요. 鋼雕는 강철로 만든 조각이에요. 保險箱은 Kaohsiung의 노동 기억을 담은 금고예요.", 22)
b.ex("B1", "完成句子", "入圍", "후보에 오르는 것은 入圍예요.",
     "被選進最後的得獎名單，叫___。", instr="빈칸 채우기", size=22, gap=10)
b.ex("B1", "單選", "A", "시상식은 11월 22일 18:30에 시작해요.",
     "金馬獎頒獎典禮幾點開始？", opts=["A. 晚上6點30分", "B. 下午2點", "C. 上午10點"], size=22, gap=10)
b.ex("B1", "完成句子", "鋼雕", "강철로 만든 조각은 鋼雕예요.",
     "用鋼鐵做的藝術，叫___。", instr="빈칸 채우기", size=22, gap=10)
b.ex("B1", "單選", "A", "강철 축제는 11월 22일에 폐막해요.",
     "鋼雕藝術節展到哪天？", opts=["A. 11月22日", "B. 11月15日", "C. 11月9日"], size=22, gap=10)
b.para("외우는 요령: 먼저 入圍를 외우고, 그다음 星光大道(17:00 레드카펫, 시상식 전), 그다음 시상식(頒獎) 18:30을 외워요.", 22)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　節氣與耶誕　계절", 25)
c.para("겨울에는 겨울만의 단어가 있어요. 이번 주: 小雪(소설), 節氣(절기), 燈秀(라이트 쇼), 市集(시장).", 22)
c.expl("이번 호의 겨울 단어 네 가지: 小雪, 節氣, 燈秀, 市集.")
c.para("小雪은 스물네 절기 중 스무 번째, 立冬 다음이에요. 節氣는 절기를 뜻해요. 일 년에 24개예요. 燈秀는 라이트 쇼예요. 메인 쇼는 30분마다 열려요. 市集은 시장이에요. World of Frozen의 겨울 시장이죠.", 22)
c.ex("B2", "單選", "A", "Xiaoxue는 스물네 절기 중 스무 번째예요.",
     "「小雪」是二十四節氣的第幾個？", opts=["A. 第20個", "B. 第2個", "C. 第24個"], size=22, gap=10)
c.ex("B2", "完成句子", "主燈秀", "메인 라이트 쇼는 30분마다 반복돼요.",
     "耶誕城的___每半小時一次。", instr="빈칸 채우기", size=22, gap=10)
c.ex("B2", "單選", "A", "겨울 시장은 World of Frozen에 있어요.",
     "想逛冬日市集、買聖誕禮物，要去哪裡？", opts=["A. 魔雪奇緣世界", "B. 維多利亞港", "C. 駁二"], size=22, gap=10)
c.ex("B2", "完成句子", "市集", "시장은 市集이에요.",
     "賣東西、逛街的地方，叫___。", instr="빈칸 채우기", size=22, gap=10)
c.para("계절 단어를 많이 알 필요는 없어요. 네 개만 외우면 겨울이 가까워져요.", 22)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「金馬獎11月15日頒獎」", "→「金馬獎11月22日頒獎，11月15日是爵士之夜」", "시상식은 11월 22일이에요. 15일은 재즈의 밤이에요."),
    ("「封王遊行上午2點出發」", "→「封王遊行下午2點出發，上午沒有遊行」", "퍼레이드는 14:00에 출발해요, 02:00이 아니에요."),
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
wt = "「天氣越冷，越要保暖。」 — 틀 越…越…은 X할수록 더 Y하다는 뜻이에요. 직접 만들어 봐요. 夜越深，燈越亮(밤이 깊을수록 불빛은 더 밝아져요)."
wcn = "틀: 越…越… — X할수록 더 Y하다. 이걸로 문장을 직접 만들어 봐요."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式　이번 주 문장 틀", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好：本週日我要去看封王遊行，穿紅色衣服為龍隊喝采。晚上回家看金馬獎轉播，還想去高雄看鋼雕，最後一天不要錯過。——台北小讀者（編輯範例）」"
lcn = "편집부의 예시 편지예요. 진짜 편지가 아니에요. 연기 안내: VOL.3에서는 이번 호부터 진짜 독자 편지와 8면 최우수 작문을 싣겠다고 예고했지만, 마감까지 게재할 만한 편지가 도착하지 않았어요. 그래서 예시를 싣고, 초대는 계속 열려 있어요."
lt2 = "延期披露：VOL.3曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。"
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
    ("「封王遊行從天母棒球場出發」", "우승 퍼레이드는 Tianmu Baseball Stadium을 출발해요.", "1쪽"),
    ("「夜間遊行晚上7點，最後一場不要錯過」", "야간 퍼레이드 19:00, 마지막 공연이에요. 놓치지 마세요.", "1쪽"),
    ("「小雪之後，天氣一天比一天冷」", "Xiaoxue 뒤로는 하루하루 더 추워져요.", "2쪽"),
    ("「主燈秀每半小時一次，每次5分鐘」", "메인 라이트 쇼는 30분마다, 한 번에 5분이에요.", "2쪽"),
    ("「頒獎典禮晚上6點30分開始」", "시상식은 18:30에 시작해요.", "3쪽"),
    ("「保險箱裡，裝的是高雄的勞動記憶」", "금고 안에는 Kaohsiung의 노동 기억이 있어요.", "3쪽"),
    ("「穿上紅色衣服，一起上街為龍隊喝采」", "빨간 옷을 입고 거리로 나와 Dragons를 응원해요.", "4쪽"),
    ("「香港迪士尼聖誕，從11月17日開始」", "Disneyland 크리스마스는 11월 17일에 시작해요.", "5쪽"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 132
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 132 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "下期預告　다음 주 (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "下週：金馬獎得獎名單、封王遊行直擊、鋼雕閉幕現場，還有你們的來信和第8版最佳作文。下週見！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
