# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ko-ja-proof/work/spy/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 말 공부 (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("말 공부 · 言葉の勉強", "Lucerna", "언어 포커스 · 세 가지 레벨, 세 가지 주제 · 3つのレベル、3つのテーマ")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 입동의 말", 24)
a.para("겨울이 시작되는 절기를 '입동'이라고 해요. 입동이 지나면 겨울 준비가 본격적으로 시작돼요. 겨울 내내 먹는 김치를 담그는 일을 '김장'이라고 해요.", 21.5)
a.para("겨울을 나기 위한 준비를 '월동 준비'라고 해요. 두꺼운 이불, 난방, 겨울옷이 월동 준비예요. 입동, 김장, 월동 준비 — 세 말이 이번 주의 겨울을 말해요.", 21.5)
a.glossline("본격적 本格的 · 나다 過ごす。")
a.ex("A2", "文完成", "입동", "立冬＝冬の始まりの節気",
     "11월 7일은 ___이에요.", instr="空所補充", size=20.5, gap=10)
a.ex("A2", "単択", "A", "キムジャン＝冬越しキムチを漬けること",
     "'김장'은 무슨 뜻이에요? A. 겨울 김치를 담그는 일 · B. 사과 축제 · C. 야구 경기", size=20.5, gap=10)
a.ex("A2", "文完成", "월동", "冬支度＝冬のための準備",
     "두꺼운 이불을 꺼내는 것은 ___ 준비예요.", instr="空所補充", size=20.5, gap=10)
a.ex("A2", "単択", "A", "節気＝一年24の時節",
     "'절기'는 무슨 뜻이에요? A. 일 년의 24개 시점 · B. 김치 이름 · C. 산 이름", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 날짜 세는 말", 24)
b.para("한국에서는 중요한 날까지 남은 날짜를 'D-17'처럼 써요. 오늘이 11월 2일, 수능이 11월 19일이니까 오늘이 D-17예요. 토요일 11월 7일은 D-12예요.", 21.5)
b.para("내일이 바로 그날이면 D-1, 오늘이 바로 그날이면 D-데이예요. 달력에서 날짜를 셀 때 자주 쓰는 말이에요.", 21.5)
b.glossline("남다 残る · 바로 ちょうど。")
b.ex("B1", "文完成", "D-12", "11月7日はD-12",
     "수능까지 12일이 남았어요. 오늘이 ___예요.", instr="空所補充", size=20.5, gap=10)
b.ex("B1", "単択", "B", "D-1＝明日",
     "D-1은 무슨 뜻이에요? A. 어제 · B. 내일 · C. 오늘", size=20.5, gap=10)
b.ex("B1", "文完成", "17", "11月2日はD-17",
     "11월 2일은 D-___예요.", instr="空所補充", size=20.5, gap=10)
b.ex("B1", "単択", "A", "D-dayは当日そのもの",
     "맞는 말은 어느 것이에요? A. D-데이는 바로 그날이에요 · B. D-12는 12일이 지났어요 · C. D-1은 일주일 전이에요", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 예보 읽는 법", 24)
c.para("예보를 읽을 때는 날짜와 함께 '기준'을 봐야 해요. 산림청은 잎의 50%, 공단은 산 전체의 약 80%를 절정의 기준으로 해요. 기준이 다르면 날짜도 달라져요.", 21.5)
c.para("그리고 '예상'과 '관측'도 나눠야 해요. 예상은 미리 짐작한 날짜, 관측은 실제로 본 날짜예요. 설악산 실제 관측은 10월 16일이었어요. (3면)", 21.5)
c.glossline("짐작하다 推測する · 나누다 区別する。")
c.ex("B2", "文完成", "기준", "日付が違うのは基準が違うから（3ページ）",
     "두 날짜가 다른 이유는 ___이 다르기 때문이에요.", instr="空所補充", size=20.5, gap=10)
c.ex("B2", "単択", "A", "山林庁の基準は葉の50%",
     "산림청의 절정 기준은 뭐예요? A. 잎의 50% · B. 산 전체의 80% · C. 첫눈이 오는 날", size=20.5, gap=10)
c.ex("B2", "文完成", "관측", "実際の観測は10月16日",
     "설악산 실제 ___은 10월 16일이었어요.", instr="空所補充", size=20.5, gap=10)
c.ex("B2", "単択", "B", "予報は基準と日付を一緒に見る",
     "예보를 읽을 때 먼저 볼 것은 뭐예요? A. 날짜만 · B. 기준과 날짜 · C. 사진", size=20.5, gap=10)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「학교를 갔어요」", "→ '가다' 앞에서는 '에'예요: '학교에 갔어요'.", "行く先には「에」を使い、「를」は使いません。"),
    ("「김치를 담궜어요」", "→ '담그다'의 과거형은 '담갔어요'예요.", "「담그다」の過去形は「담갔어요」です。"),
    ("「수능까지12일 남았어요」", "→ 숫자는 띄어 써요: '수능까지 12일 남았어요'.", "数字の前には空白を入れます。"),
    ("「서울에에서 만났어요」", "→ 조사는 하나만 써요: '서울에서 만났어요'.", "助詞は一つだけ使います。"),
]
# W45-KO fix: clinic item 3's correction alone narrows (310) so its final
# line is 12일 남았어요'. instead of lone 남았어요'.
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44 - 80 if errs.index(r) == 2 else CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "실수 병원 · まちがいクリニック", 23, "sans", True, OLIVE)
yy3 += 54
for i, (wrong, right, cn) in enumerate(errs):
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44 - 80 if i == 2 else CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「〜부터 〜까지」 — '11월 1일부터 12월 15일까지 산불조심기간이에요.' 기간을 말할 때 쓰는 틀이에요. 물어볼 때는 '〜부터 〜까지예요?'라고 해요."
wcn = "文型の解説：「〜から〜まで」。質問：「〜부터 〜까지예요?」"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "이번 주의 틀 · 今週の文型", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「안녕하세요. 저는 대학생이에요. 토요일에는 내장산에 단풍을 보러 가요. 일요일에는 집에서 김장을 도와요. 겨울이 와도 따뜻하게 지내고 싶어요.」 — 독자 편지의 예"
lcn = "編集部の例文です。本物の手紙ではありません。"
lko = "알려요: 이 편지는 편집부가 쓴 예예요. 마감 때까지 진짜 독자 편지와 8면 쓰기 우수작이 도착하지 않았어요. 그래서 예가 실렸고, 지난 호의 약속은 VOL.3으로 이어져요."
lcn2 = "締切までに本物の手紙も8ページの最優秀作文も届かず、例を載せました。約束はVOL.3に引き継ぎます。あなたの手紙と8ページの最優秀作文を送ってください！"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 12 + len(wrap(lko, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 66
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "독자의 편지 · 読者の手紙", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lko, 20.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn2, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "이번 주의 문장 · 今週の名文（本号の文章から一字一句そのまま）", 27, "sans", True, OLIVE)
quotes = [
    ("「11월 7일은 입동이에요」", "11月7日は立冬です。", "1면"),
    ("「절정에 가까운 주말이라고만 말할 수 있어요」", "ピークに近い週末としか言えません。", "1면"),
    ("「김장은 겨울 내내 먹는 김치를 담그는 일이에요」", "キムジャンとは、冬越しキムチを漬けることです。", "1면"),
    ("「수능까지 17일 남았어요. 오늘이 D-17예요」", "修能まであと17日、今日はD-17です。", "2면"),
    ("「낮은 길은 더 늦게 물들어요」", "低い道の方がもっと遅く色づきます。", "3면"),
    ("「KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요」", "KIAタイガースがLGツインズに三連勝しました。", "4면"),
    ("「온 나라가 수험생을 응원해요」", "全国が受験生を応援しています。", "5면"),
    ("「날짜를 먼저 보세요」", "まず日付を見てください。", "6면"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 102
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 102 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "다음 주 · 次号予告 (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "다음 주에는 김장이 한창이에요. 수능까지 일주일이 남았어요. 한능검 시험이 가까워져요. 플레이오프와 한국시리즈 소식도 전해요. 여러분의 편지와 8면 쓰기 우수작도 실어요. 기대해 주세요!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-mal.svg")
print("P7 saved, exercises so far:", len(REG))
