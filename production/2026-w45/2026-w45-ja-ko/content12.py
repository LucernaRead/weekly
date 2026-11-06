# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ja-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 表紙 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2 · 第2号", 23, "sans", True, OLIVE)
p.text(975, 92, "毎週、日本語で · 매주 발행 · 日本人が読んでいる日本語を読む", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "2026年11月2日（月）〜8日（日）", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 248, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 316, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")
p.text(975, 356, "일본어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판", 19, "sans", True, BRICK, anchor="middle")
p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "火よう日は文化の日！", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "11月3日（火）は祝日です。紅葉の週末へ、ゆるく出かけましょう。", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "화요일은 문화의 날", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "연휴 뒤 단풍 주말이 와요 · 자세한 것은 3면", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "トップニュース · 헤드라인", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "文化の日と紅葉の週末", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "ゆるく整える日本の11月 — 祝日と紅葉と読書の週です", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "Lucerna編集部 · 読むレベル：A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("文化の日は、11月3日（火よう日）です。祝日ですから、学校も会社も休みです。文化の日には、全国で文化のイベントがあります。")
f.para("今週は、『読書週間』の週でもあります。読書週間は、10月27日（火よう日）に始まりました。11月9日（月よう日）までです。今年のスローガンは『静かだけど、冒険中。』です。")
f.para("週末には、紅葉が見頃になります。宮城県の鳴子峡では、10月31日から11月8日の週末が見頃だそうです。神戸の布引ハーブ園では、7日（土よう日）から紅葉のライトアップが始まります。")
f.para("7日（土よう日）は、暦の上で『立冬』です。冬の始まりの日です。でも、今年の11月は暖かいそうです。ゆっくり、ゆるく整える日本の11月です。")
f.para("『Lucerna』日本語版の第2号です。今週も、本物の日本のニュースを、やさしい日本語でお届けします。どうぞ楽しんでください！")
f.gloss("祝日 공휴일 · 見頃 가장 보기 좋은 때 · 暦 달력 · お届けします 전해 드려요.")
f.box("数字で見る今週 · 한 주의 숫자", [
    ("3 — 文化の日は11月3日（火）です", "serif", False, INK, 20, 1.35),
    ("7 — 立冬は11月7日（土）です", "serif", False, INK, 20, 1.35),
    ("9 — 読書週間は11月9日（月）までです", "serif", False, INK, 20, 1.35),
    ("1.5 — 鍋の食卓は去年の1.5倍（8〜10月、味の素の発表より）", "serif", False, INK, 20, 1.35),
])
f.head("今すぐ練習 · 바로 연습", 25)
f.ex("A2", "문장 완성", "3", "문화의 날은 11월 3일(화)이에요",
     "文化の日は11月 ___ 日（火よう日）です。", size=19.5, gap=6)
f.ex("A2", "문장 완성", "9", "독서 주간은 11월 9일(월)까지예요",
     "読書週間は11月 ___ 日（月よう日）までです。", size=19.5, gap=6)
f.ex("A2", "문장 완성", "見頃", "見頃 = 가장 보기 좋은 때",
     "週末には、紅葉が ___ になります。", size=19.5, gap=6)
f.ex("A2", "문장 완성", "立冬", "立冬 = 겨울의 시작",
     "7日（土）は、暦の上で『___』です。", size=19.5, gap=6)
f.ex("A2", "문장 완성", "7", "고베 라이트업은 7일(토)부터 시작해요",
     "神戸のライトアップは ___ 日（土よう日）から始まります。", size=19.5, gap=6)
f.ex("A2", "문장 완성", "文化の日", "문화의 날에는 전국에서 문화 행사가 열려요",
     "___ には、全国で文化のイベントがあります。", size=19.5, gap=6)
f.end_report()

# ---- trend box (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "今週のトレンド", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "日本の「今、熱い話題」", 24, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "発表と予報の日付つきでお届けします", 19, "sans", False, GREY)
topics = [
    "ゆる整え食 — 味の素、10月21日発表",
    "紅葉の週末 — 鳴子峡と神戸",
    "読書週間 — 11月9日まで",
    "暖かい11月 — 気象庁、10月20日予報",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 26
yy_n = p.para(gx + 22, byy + 24, "暮らしの話題は、noteの10月22日のまとめ（SNSの話題）によるものです。アンケートの結果ではありません。", 19, "serif", False, GREY, gw - 44, 1.35)
p.para(gx + 22, yy_n + 24, "この4つの話題は、今週の新聞のテーマです。", 19, "serif", False, GREY, gw - 44, 1.35)
p.para(gx + 22, yy_n + 52, "이 네 가지 주제가 이번 호 신문의 주제예요.", 18.5, "sans", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 636, "出典：各発表・予報の日付は記事の中にあります", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "날짜는 기사 참조 · 정확한 통계 아님", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "この号の内容 · 이번 호 목차", 24, "sans", True, OLIVE)
som = [
    ("2面", "ゆる整え食と暖かい11月", "A2"),
    ("3面", "文化の日と金沢", "A2→B1"),
    ("4面", "日本シリーズ横浜の2試合", "B1"),
    ("5面", "ハロウィンと秋まつり", "B1"),
    ("6面", "暖かい11月と秋の旅", "B2"),
    ("7面", "読書と紅葉のことば", "A2→B2"),
    ("8面", "テストと答え", "全部"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

# ---- word of the week (col 3) ----
my = 1636
p.text(gx, my + 24, "今週のことば · 이번 주 단어", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "「ゆる」 — ゆるく、無理をしないで。力を抜いて、ゆっくりすることです。今週のキーワードは『ゆるく整える』です。", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "ゆる = 무리하지 않고, 여유롭게.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "maple.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "秋のカエデの葉。今週末、山や公園で紅葉が見頃になります。（6面）",
        "写真：Poliphilo — CC0（Wikimedia Commons）")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-weekend")
f2.head("読書週間の今週", 25)
f2.para("読書週間は今週も続きます。9日（月よう日）で終わります。本を読む人には、いちばん楽しい週です。図書館のイベントもあります。", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "短いニュース · 짧은 소식", 24, "sans", True, OLIVE)
brefs = [
    ("文化の日", "3日（火）は祝日です。金沢のイベントもあります。（3面）"),
    ("立冬", "7日（土）は、暦の上で冬の始まりです。（6面）"),
    ("ライトアップ", "神戸では7日から紅葉のライトアップです。（6面）"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "クイズ · 번개 퀴즈", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "1면을 읽고 알맞은 답을 고르세요 · 정답은 8면", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "객관식", "B", "문화의 날은 11월 3일(화)이에요",
      "文化の日はいつですか。 A. 2日（月） · B. 3日（火） · C. 7日（土）", size=21)
qf.ex("A2", "객관식", "C", "독서 주간은 11월 9일(월)까지예요",
      "読書週間はいつまでですか。 A. 3日（火） · B. 8日（日） · C. 9日（月）", size=21)
qf.ex("A2", "객관식", "B", "입동은 11월 7일(토)이에요",
      "立冬はいつですか。 A. 3日（火） · B. 7日（土） · C. 9日（月）", size=21)
qf.ex("A2", "객관식", "A", "라이트업은 고베에서 시작해요",
      "ライトアップが始まるのはどこですか。 A. 神戸 · B. 金沢 · C. 鳴子峡", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-hyoushi.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 生活 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("生活 · くらし", "Lucerna", "レベル A2 · ゆる整え食と暖かい11月 · 가볍게 차리는 식탁과 따뜻한 11월")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("「ゆる整え食」— 無理をしない冬の食卓", 37)
f.byline("Lucerna編集部 · 読むレベル：A2")
f.para("味の素は10月21日、冬の食トレンド『ゆる整え食』を発表しました。『ゆる』は、無理をしない、ゆっくり、という意味です。『整える』は、体と心を整える、という意味です。")
f.para("『ゆる整え食』の食べ物は、せいろで蒸した料理、麻辣湯（マーラータン）、一つの鍋で作るスープなどです。8月から10月まで、家で鍋を食べる食卓は、去年の1.5倍になったそうです。スーパーでは、鍋の材料が1か月早く並び始めました。")
f.para("『サクサクdeコパン』は、1年ぐらいで1,300万食を超えたそうです。忙しい人でも、簡単に作れる食べ物が人気です。")
f.gloss("蒸す 찌다 · 並ぶ 진열되다 · 食卓 식탁 · 超える 넘다.")
f.head("暖かい11月", 25)
f.para("気象庁の10月20日の3か月予報では、11月から1月まで、全国的に気温は平年より高いそうです。季節風が弱いためです。太平洋側では、雨が多いそうです。11月は暖かい、という予報です。")
f.para("SNSの話題のまとめ（note、10月22日）では、30代・40代の服として、ペプラムのニットやチェック・ツイードのジャケットが話題だそうです。値上がりの中で、『考えなくていい』服の選び方や、一品だけの食事も話題です。このまとめは、アンケートの結果ではありません。")
f.gloss("予報 예보 · 平年 평년 · 季節風 계절풍 · 話題 화제 · 値上がり 가격 상승.")
f.end_report()

# col 3: numbers box + forecast box + あなた (sequential, measured)
ix = COLX[3]
nums = ["1.5倍 — 鍋の食卓（8〜10月、去年と比べて）",
        "1,300万食 — 『サクサクdeコパン』（1年ぐらいで）",
        "1か月早く — スーパーに鍋の材料が並び始めました",
        "10月21日 — 味の素の発表の日"]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in nums) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ゆる整え食の数字", 24, "sans", True, OLIVE)
yy3 += 52
for t in nums:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
fc = ["全国的に気温は平年より高い（11月〜1月）",
      "季節風が弱いため、暖かいそうです",
      "太平洋側では、雨が多いそうです"]
fy3 = sy3 + sh + 26
fh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in fc) + 32
p.rect(ix, fy3, CW, fh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = fy3 + 16
p.text(ix + 22, yy3 + 26, "暖かい11月の予報", 24, "sans", True, OLIVE)
yy3 += 52
for t in fc:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = fy3 + fh + 26
etvous = "あなたは？寒い日に、どんな鍋を食べたいですか。日本語で2文、書いて、送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("여러분은요? 추운 날에는 어떤 나베를 먹고 싶어요? 일본어로 두 문장 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？ · 여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "여러분은요? 추운 날에는 어떤 나베를 먹고 싶어요? 일본어로 두 문장 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- season words strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "季節のことば · 계절의 말", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "ゆる整え食の4つの言葉 · 가볍게 차리는 식탁의 단어 네 개", 20, "sans", False, GREY, anchor="end")
words = [
    ("鍋（なべ）", "一つの鍋で作る料理", "한 솥 요리"),
    ("蒸し器（せいろ）", "蒸すための道具", "찜기"),
    ("ゆる", "無理をしないさま", "무리하지 않고 여유롭게"),
    ("整える", "体と心をよくする", "몸과 마음을 다스리기"),
]
for i, (t, lab, cn) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 234, "文で覚えましょう：『ゆる整え食で、体を整えましょう。』", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · 2면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면 · 레벨이 섞인 문제예요. 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · 理解", 25)
e.bridge("第2版の文章を読んで、正しい答えを選んでください。")
e.ex("A2", "객관식", "B", "「ゆる」 = 무리하지 않기",
     "『ゆる』の意味は？ A. 速い · B. 無理をしない · C. 熱い", size=19, gap=6)
e.ex("A2", "객관식", "B", "나베 식탁은 지난해의 1.5배예요",
     "鍋の食卓は、去年と比べてどうなりましたか。 A. 半分 · B. 1.5倍 · C. 3倍", size=19, gap=6)
e.ex("A2", "객관식", "A", "발표는 10월 21일이었어요",
     "味の素の発表はいつでしたか。 A. 10月21日 · B. 10月20日 · C. 10月22日", size=19, gap=6)
e.ex("A2", "객관식", "C", "11월부터 1월까지 기온은 평년보다 높아요",
     "気象庁の予報では、気温はどうなりますか。 A. 平年より低い · B. 平年と同じ · C. 平年より高い", size=19, gap=6)
e.ex("A2", "객관식", "B", "옷과 음식 화제는 note 정리에서 왔어요",
     "服と食事の話題は、どこから来ましたか。 A. アンケート · B. noteのまとめ · C. 気象庁", size=19, gap=6)
e.head("B · ことば", 25)
e.bridge("言葉や数字を入れてください。")
e.ex("A2", "문장 완성", "ゆる", "ゆる = 무리하지 않고 여유롭게",
     "無理をしないことを「___」と言います。", instr="빈칸 채우기", size=19, gap=6)
e.ex("A2", "문장 완성", "蒸し器", "蒸し器 = 찜기",
     "蒸すための道具を「___」と言います。", instr="빈칸 채우기", size=19, gap=6)
e.ex("A2", "문장 완성", "整える", "整える = 몸과 마음을 다스리기",
     "体と心をよくすることを「___」と言います。", instr="빈칸 채우기", size=19, gap=6)
e.ex("B1", "문장 완성", "1.5", "나베 식탁은 지난해의 1.5배예요",
     "鍋の食卓は、去年の ___ 倍になりました。", instr="빈칸 채우기", size=19, gap=6)
e.ex("A2", "문장 완성", "鍋", "鍋 = 한 솥 요리",
     "一つの鍋で作る料理を「___」と言います。", instr="빈칸 채우기", size=19, gap=6)
e.head("C · 数字と日付", 25)
e.bridge("第2版の数字と日付で答えてください。")
e.ex("A2", "문장 완성", "21", "발표는 10월 21일이었어요",
     "味の素の発表は10月 ___ 日でした。", instr="빈칸 채우기", size=19, gap=6)
e.ex("A2", "문장 완성", "1", "나베 재료가 한 달 일찍 진열됐어요",
     "鍋の材料は ___ か月早く並び始めました。", instr="빈칸 채우기", size=19, gap=6)
e.ex("A2", "문장 완성", "20", "기상청 예보는 10월 20일이었어요",
     "気象庁の予報は10月 ___ 日でした。", instr="빈칸 채우기", size=19, gap=6)
e.ex("B1", "문장 완성", "1,300", "사쿠사쿠de코판이 1,300만 끼를 넘었어요",
     "『サクサクdeコパン』は ___ 万食を超えました。", instr="빈칸 채우기", size=19, gap=6)
e.head("D · ペアにしましょう", 25)
e.match_set("A2", "단어 짝짓기",
            ["ゆる", "蒸し器", "麻辣湯", "予報"],
            ["蒸すための道具",
             "無理をしないさま",
             "天気の予想",
             "辛いスープの料理"],
            ["b", "a", "d", "c"],
            ["ゆる = 무리하지 않고 여유롭게 b", "蒸し器 = 찜기 a", "麻辣湯 = 매운 수프 요리 d", "予報 = 날씨 예상 c"],
            instr="단어와 뜻 짝짓기")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-kurashi.svg")
print("P2 saved, exercises so far:", len(REG))
