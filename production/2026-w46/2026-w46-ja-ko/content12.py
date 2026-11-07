# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ja-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 表紙 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3 · 第3号", 23, "sans", True, OLIVE)
p.text(975, 92, "毎週、日本語で · 매주 · 日本人が読んでいる日本語を読む", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "2026年11月9日（月）〜15日（日）", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 316, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")
p.text(975, 356, "일본어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판", 19, "sans", True, BRICK, anchor="middle")
p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "日よう日は七五三！", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "11月15日（日）は七五三の中心の日です。神社へ、着物の子どもが集まります。", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "일요일은 시치고상", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "단풍철은 남쪽으로 이동 · 6면 참조", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "トップニュース · 톱 뉴스", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "七五三の週と、読書週間の終わり", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "本を閉じて、神社へ — 秋の終わりの日本の11月です", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "Lucerna編集部 · 読むレベル：A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("読書週間は、9日（月よう日）で終わります。10月27日（火よう日）に始まりました。今年のスローガンは『静かだけど、冒険中。』でした。")
f.para("15日（日よう日）は、七五三の中心の日です。3歳と5歳と7歳の子どもが、神社へお参りに行きます。着物を着た子どもが、たくさんいます。")
f.para("紅葉の見頃は、南へ移っています。ウェザーニューズの10月29日の予報では、東京の高尾山は13日（金よう日）ごろから見頃だそうです。宮城県の鳴子峡は、もう見頃だそうです。")
f.para("7日（土よう日）には、浅草で酉の市（一の酉）がありました。熊手を買う人の夜でした。二の酉は、19日（木よう日）です。")
f.para("『Lucerna』日本語版の第3号です。今週も、本物の日本のニュースを、やさしい日本語でお届けします。どうぞ楽しんでください！")
f.gloss("終わる 끝나다 · お参り 참배하러 가다 · 移る 이동하다 · 熊手 행운의 갈퀴.")
f.box("数字で見る今週 · 숫자로 보는 이번 주", [
    ("3 — 七五三は3歳・5歳・7歳のお祝いです", "serif", False, INK, 20, 1.35),
    ("11 — ポッキーの日は11月11日（水）です", "serif", False, INK, 20, 1.35),
    ("15 — 七五三の中心の日は11月15日（日）です", "serif", False, INK, 20, 1.35),
    ("4 — ソフトバンクが4連勝で日本一になりました", "serif", False, INK, 20, 1.35),
])
f.head("今すぐ練習 · 지금 연습", 25)
f.ex("A2", "빈칸 채우기", "9", "독서주간은 11월 9일(월요일)에 끝난다",
     "読書週間は11月 ___ 日（月よう日）で終わります。", size=19.5, gap=6)
f.ex("A2", "빈칸 채우기", "15", "시치고상은 11월 15일(일요일)이 중심이다",
     "七五三の中心の日は11月 ___ 日（日よう日）です。", size=19.5, gap=6)
f.ex("A2", "빈칸 채우기", "見頃", "見頃 = 가장 보기 좋은 시기",
     "紅葉の ___ は、南へ移っています。", size=19.5, gap=6)
f.ex("A2", "빈칸 채우기", "19", "도리노이치의 니노토리는 11월 19일(목요일)이다",
     "二の酉は、11月 ___ 日（木よう日）です。", size=19.5, gap=6)
f.ex("A2", "빈칸 채우기", "13", "다카오산의 단풍은 13일(금요일)경부터 절정이다",
     "高尾山は ___ 日（金よう日）ごろから見頃だそうです。", size=19.5, gap=6)
f.ex("A2", "빈칸 채우기", "七五三", "시치고상 아이들은 신사에 참배하러 간다",
     "___ の子どもが、神社へお参りに行きます。", size=19.5, gap=6)
f.end_report()

# ---- trend box (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "今週のトレンド", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "日本の「今、熱い話題」", 24, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "発表と予報の日付つきでお届けします", 19, "sans", False, GREY)
topics = [
    "読書週間 — 9日（月）で終わります",
    "七五三 — 15日（日）が中心の日です",
    "紅葉の見頃 — 高尾山は13日ごろ",
    "ポッキーの日 — 11日（水）",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 26
yy_n = p.para(gx + 22, byy + 24, "紅葉の予報は、ウェザーニューズの発表（10月29日）です。", 19, "serif", False, GREY, gw - 44, 1.35)
yy_n2 = p.para(gx + 22, yy_n + 24, "この4つの話題は、今週の新聞のテーマです。", 19, "serif", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 636, "出典：各発表・予報の日付は記事の中にあります", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "날짜는 기사에 있음; 정확한 통계가 아님", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "この号の内容 · 이번 호 내용", 24, "sans", True, OLIVE)
som = [
    ("2面", "ポッキーの日と千歳飴", "A2"),
    ("3面", "七五三と酉の市", "A2→B1"),
    ("4面", "日本シリーズ4連勝", "B1"),
    ("5面", "11月11日の分かち合い", "B1"),
    ("6面", "紅葉の見頃は南へ", "B2"),
    ("7面", "読書と七五三のことば", "A2→B2"),
    ("8面", "テストと答え", "전 수준"),
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
y2 = p.para(gx, my + 76, "「千歳飴（ちとせあめ）」 — 七五三の子どもがもらう、赤と白の長い飴です。長く生きてほしい、という願いのお菓子です。", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "千歳飴 = 시치고상의 붉고 흰 사탕.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "maple.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "秋のカエデの葉。今週、見頃は南へ移ります。（6面）",
        "写真：Poliphilo — CC0（Wikimedia Commons）")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-tori")
f2.head("酉の市の一の酉", 25)
f2.para("酉の市は、11月の酉の日に開くお祭りです。7日（土よう日）は、一の酉でした。浅草の鷲神社では、午前0時の太鼓から、熊手の店が一日中並びました。二の酉は、19日（木よう日）です。", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "短いニュース · 짧은 뉴스", 24, "sans", True, OLIVE)
brefs = [
    ("相撲", "九州場所は8日（日）に始まりました。（4面）"),
    ("ポッキーの日", "11日（水）は「1」が4つ並ぶ日です。（2面）"),
    ("七五三", "15日（日）が中心の日です。（3面）"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "クイズ · 빠른 퀴즈", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "1면을 읽고 고르세요 · 답은 8면", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "객관식", "A", "독서주간은 11월 9일(월요일)에 끝난다",
      "読書週間はいつ終わりますか。 A. 9日（月） · B. 15日（日） · C. 19日（木）", size=21)
qf.ex("A2", "객관식", "C", "시치고상은 11월 15일(일요일)이 중심이다",
      "七五三の中心の日はいつですか。 A. 9日（月） · B. 11日（水） · C. 15日（日）", size=21)
qf.ex("A2", "객관식", "B", "다카오산의 단풍은 13일(금요일)경부터 절정이다",
      "高尾山の見頃はいつごろからですか。 A. 7日（土） · B. 13日（金） · C. 19日（木）", size=21)
qf.ex("A2", "객관식", "B", "니노토리는 11월 19일(목요일)이다",
      "二の酉はいつですか。 A. 7日（土） · B. 19日（木） · C. 15日（日）", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-hyoushi.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 生活 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("生活 · くらし", "Lucerna", "レベル A2 · ポッキーの日と千歳飴 · 포키데이와 지토세아메")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("11月11日 — 細いお菓子", 37)
f.byline("Lucerna編集部 · 読むレベル：A2")
f.para("11月11日（水よう日）は、『ポッキー＆プリッツの日』です。江崎グリコが、1999年に決めました。細いお菓子の形が、数字の「1」に似ているからです。")
f.para("1999年は、平成11年でした。平成11年11月11日には、数字の「1」が6つ並びました。「1111」は、細い棒が4本並んでいるように見えます。友達とお菓子を分け合う日です。")
f.para("『ポッキー＆プリッツの日』は、1999年に始まりました。ポッキーは、チョコレートがかかった細いビスケットです。プリッツは、塩味の細いビスケットです。")
f.gloss("細い 가늘다 · 似ている 닮다 · 分け合う 나누다 · 塩味 짠맛.")
f.head("七五三の甘いもの", 25)
f.para("七五三の子どもは、千歳飴をもらいます。千歳飴は、赤と白の長い飴です。千歳飴は、長く生きてほしい、という願いのお菓子です。神社で、家族と写真を撮る子どもも多いです。")
f.para("11月は、甘いものが多い月です。ポッキーを分け合って、千歳飴をもらって、秋の終わりを楽しみましょう。")
f.gloss("願い 소원 · 撮る 사진을 찍다 · 楽しむ 즐기다.")
f.end_report()

# col 3: numbers box + 11/11 box + あなた (sequential, measured)
ix = COLX[3]
nums = ["1999年 — 『ポッキー＆プリッツの日』が始まった年",
        "11月11日 — 「1」が4つ並ぶ日",
        "6つ — 平成11年11月11日の「1」の数",
        "4本 — 「1111」は細い棒が4本に見えます"]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in nums) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "11月11日の数字", 24, "sans", True, OLIVE)
yy3 += 52
for t in nums:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
fc = ["ポッキー — チョコレートの細いビスケット",
      "プリッツ — 塩味の細いビスケット",
      "千歳飴 — 赤と白の長い飴"]
fy3 = sy3 + sh + 26
fh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in fc) + 32
p.rect(ix, fy3, CW, fh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = fy3 + 16
p.text(ix + 22, yy3 + 26, "11月の細いお菓子", 24, "sans", True, OLIVE)
yy3 += 52
for t in fc:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = fy3 + fh + 26
etvous = "あなたは？11月11日に、だれとポッキーを分け合いたいですか。日本語で2文、書いて、送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("11월 11일에 누구와 포키를 나누고 싶나요? 일본어로 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？ · 당신의 차례", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "11월 11일에 누구와 포키를 나누고 싶나요? 일본어로 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- season words strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "11月のことば · 11월 단어", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "「1」の日と七五三の4つの言葉 · 1의 날과 시치고상의 네 단어", 20, "sans", False, GREY, anchor="end")
words = [
    ("ポッキー", "チョコレートの細いお菓子", "초콜릿을 입힌 막대"),
    ("千歳飴（ちとせあめ）", "赤と白の長い飴", "길고 붉고 흰 사탕"),
    ("熊手（くまで）", "商売繁盛の縁起物", "사업 번창을 위한 행운의 갈퀴"),
    ("見頃（みごろ）", "いちばん美しい時", "가장 보기 좋은 시기"),
]
for i, (t, lab, cn) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 234, "文で覚えましょう：『11月11日に、友達とポッキーを分け合います。』", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · 2면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "답은 8면 · 수준이 섞여 있어요 — 번호를 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · 理解", 25)
e.bridge("第2版の文章を読んで、正しい答えを選んでください。")
e.ex("A2", "객관식", "B", "포키데이는 1999년에 시작됐다",
     "『ポッキー＆プリッツの日』はいつからですか。 A. 1989年 · B. 1999年 · C. 2009年", size=19, gap=6)
e.ex("A2", "객관식", "A", "11월 11일로 정한 것은 가느다란 과자가 숫자 1처럼 보이기 때문이다",
     "11月11日が選ばれたのは、どうしてですか。 A. お菓子の形が「1」に似ているから · B. 休みの日だから · C. 紅葉の日だから", size=19, gap=6)
e.ex("A2", "객관식", "C", "헤이세이 11년 11월 11일에는 1이 여섯 개였다",
     "平成11年11月11日には、「1」がいくつ並びましたか。 A. 4つ · B. 5つ · C. 6つ", size=19, gap=6)
e.ex("A2", "객관식", "B", "지토세아메는 길고 붉고 흰 사탕이다",
     "千歳飴は、どんな飴ですか。 A. 黒い丸い飴 · B. 赤と白の長い飴 · C. 緑の四角い飴", size=19, gap=6)
e.ex("A2", "객관식", "A", "지토세아메는 장수 기원을 담고 있다",
     "千歳飴の願いは何ですか。 A. 長く生きてほしい · B. 速く走ってほしい · C. 高く飛んでほしい", size=19, gap=6)
e.head("B · ことば", 25)
e.bridge("言葉や数字を入れてください。")
e.ex("A2", "빈칸 채우기", "ポッキー", "초콜릿을 입힌 막대",
     "チョコレートの細いお菓子を「___」と言います。", instr="빈칸을 채우세요", size=19, gap=6)
e.ex("A2", "빈칸 채우기", "千歳飴", "길고 붉고 흰 사탕",
     "赤と白の長い飴を「___」と言います。", instr="빈칸을 채우세요", size=19, gap=6)
e.ex("A2", "빈칸 채우기", "熊手", "熊手 = 사업 번창을 위한 행운의 갈퀴",
     "商売繁盛の縁起物を「___」と言います。", instr="빈칸을 채우세요", size=19, gap=6)
e.ex("B1", "빈칸 채우기", "1999", "포키데이는 1999년에 시작됐다",
     "『ポッキー＆プリッツの日』は ___ 年に始まりました。", instr="빈칸을 채우세요", size=19, gap=6)
e.ex("A2", "빈칸 채우기", "11", "포키데이는 11월 11일이다",
     "『ポッキー＆プリッツの日』は ___ 月11日です。", instr="빈칸을 채우세요", size=19, gap=6)
e.head("C · 数字と日付", 25)
e.bridge("第2版の数字と日付で答えてください。")
e.ex("A2", "빈칸 채우기", "11", "포키데이는 11월 11일(수요일)이다",
     "ポッキーの日は11月 ___ 日（水）です。", instr="빈칸을 채우세요", size=19, gap=6)
e.ex("A2", "빈칸 채우기", "6", "헤이세이 11년 11월 11일에는 1이 여섯 개였다",
     "平成11年11月11日には、「1」が ___ つ並びました。", instr="빈칸을 채우세요", size=19, gap=6)
e.ex("A2", "빈칸 채우기", "4", "1111은 가느다란 막대 네 개처럼 보인다",
     "「1111」は、細い棒が ___ 本に見えます。", instr="빈칸을 채우세요", size=19, gap=6)
e.ex("B1", "빈칸 채우기", "1999", "포키데이는 1999년에 시작됐다",
     "江崎グリコは ___ 年に、この日を決めました。", instr="빈칸을 채우세요", size=19, gap=6)
e.head("D · ペアにしましょう", 25)
e.match_set("A2", "연결하기",
            ["ポッキー", "プリッツ", "千歳飴", "熊手"],
            ["赤と白の長い飴",
             "商売繁盛の縁起物",
             "塩味の細いビスケット",
             "チョコレートの細いビスケット"],
            ["d", "c", "a", "b"],
            ["ポッキー = 초콜릿을 입힌 막대 d", "プリッツ = 짠 가느다란 과자 c", "千歳飴 = 길고 붉고 흰 사탕 a", "熊手 = 행운의 갈퀴 b"],
            instr="단어와 뜻을 연결하세요")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-kurashi.svg")
print("P2 saved, exercises so far:", len(REG))
