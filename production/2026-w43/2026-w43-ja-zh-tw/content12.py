# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 表紙 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1　第1号", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "毎週、日本語で　每週一期　日本人が読んでいる日本語を読む", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "2026年10月19日（月）〜25日（日）", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 316, "日本語版　VOL.1　日本シリーズ　紅葉　読書の秋", 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)
p.text(975, 356, "日語正文　繁體中文講解 — 給繁體中文讀者的版本", 16, "sans", False, GREY, anchor="middle")
p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "土よう日、日本シリーズが始まる！", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "横浜スタジアムで DeNA 対ソフトバンク — 2年ぶりの対決です。第1戦は18時30分。", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "週六，日本大賽開幕", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "時隔兩年的對決　詳見第4版", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "トップニュース　頭條", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "土よう日、日本シリーズが始まる！", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 30, "DeNA 対ソフトバンク — 2年ぶりの同じ対決です", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "Lucerna編集部　読むレベル：A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("日本シリーズの第1戦は、10月24日（土よう日）の18時30分、横浜スタジアムです。戦うのは、横浜DeNAベイスターズと福岡ソフトバンクホークスです。", size=24)
f.para("この対決は2年ぶりです。2024年も同じ2チームでした。その年は、リーグ3位だったDeNAが優勝しました。今年もDeNAは3位から勝ち上がって、クライマックスシリーズで阪神に勝ちました。", size=24)
f.para("第2戦は25日（日よう日）の18時です。チケットの一般発売は、22日（木よう日）の12時に始まりました。", size=24)
f.para("土よう日は、愛知・名古屋の『アジアパラ競技大会』の最終日でもあります。大会は18日（日よう日）に始まりました。日本で初めてのアジアパラ競技大会です。スポーツが熱い週末になります。", size=24)
f.para("『Lucerna』日本語版の第1号です。毎週、本物の日本のニュースを、やさしい日本語でお届けします。どうぞ楽しんでください！", size=24)
f.gloss("戦う 對戰 · 勝ち上がる 一路勝出晉級 · 第1戦 第一場比賽 · お届けします 為您送上。")
f.box("数字で見る今週　數字看本週", [
    ("45 — アジアパラ競技大会に参加する国と地域の数（過去最多）", "serif", False, INK, 20, 1.35),
    ("18 — アジアパラ競技大会の競技の数", "serif", False, INK, 20, 1.35),
    ("2 — 日本シリーズは、2年ぶりの同じ対決です", "serif", False, INK, 20, 1.35),
    ("18:30 — 日本シリーズ第1戦の開始時間（土よう日）", "serif", False, INK, 20, 1.35),
])
f.head("今すぐ練習　即學即練", 25)
f.ex("A2", "完成句子", "土よう日", "第1戰在10月24日，星期六",
     "日本シリーズの第1戦は、10月24日（___）です。", size=19.5, gap=6)
f.ex("A2", "完成句子", "18", "第1戰在18時30分開始",
     "第1戦は ___ 時30分に始まります。", size=19.5, gap=6)
f.ex("A2", "完成句子", "横浜", "橫濱體育場",
     "試合は ___ スタジアムです。", size=19.5, gap=6)
f.ex("A2", "完成句子", "3", "DeNA從聯賽第3名晉級",
     "今年もDeNAはリーグ ___ 位から勝ち上がりました。", size=19.5, gap=6)
f.ex("A2", "完成句子", "22", "門票22日（週四）12時公開發售",
     "チケットの一般発売は ___ 日（木よう日）12時でした。", size=19.5, gap=6)
f.ex("A2", "完成句子", "最終日", "週六也是亞殘運會的最後一天",
     "土よう日は、アジアパラ競技大会の ___ でもあります。", size=19.5, gap=6)
f.end_report()

# ---- search heat box (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "検索の熱ワード", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "GOOGLEトレンド日本", 24, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "10月17日のまとめ（note掲載）より", 19, "sans", False, GREY)
topics = [
    "ジェラードン（コント）— 20万回以上",
    "大谷翔平（野球）— 20万回以上",
    "箱根駅伝予選会 結果 — 5万回以上",
    "山本由伸（野球）— 2万回以上",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 26
yy_n = p.para(gx + 22, byy + 24, "検索数は概数です。日本の「今、熱い言葉」の目安にしてください。", 19, "serif", False, GREY, gw - 44, 1.35)
yy_m = p.para(gx + 22, yy_n + 24, "この4つの言葉は、今週の新聞のテーマです。", 19, "serif", False, GREY, gw - 44, 1.35)
p.para(gx + 22, yy_m + 2, "這四個詞，都是本期報紙的主題。", 18.5, "sans", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 662, "データ：Googleトレンド日本（10月17日）", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 690, "數據為10月17日趨勢彙總的約數，非精確統計", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f0eee5")
p.text(gx + 22, sy + 40, "この号の内容　本期目錄", 24, "sans", True, OLIVE)
som = [
    ("2面", "紅葉と秋の食", "A2"),
    ("3面", "時代祭と週末の文化", "A2→B1"),
    ("4面", "日本シリーズ詳報", "B1"),
    ("5面", "コントとハロウィン", "B1"),
    ("6面", "アジアパラ大会を読む", "B2"),
    ("7面", "読書週間とことば", "A2→B2"),
    ("8面", "テストと答え", "全部"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

# ---- word of the week (col 3) ----
my = 1636
p.text(gx, my + 24, "今週のことば　本週單字", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "「見頃（みごろ）」", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 102, "見るのにいちばんいい時。花や紅葉がいちばん美しい時です。今週末、北の地方で紅葉が見頃になります。", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 8, "見頃（みごろ）＝ 最佳觀賞期。", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "stadium.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "横浜スタジアム。日本シリーズの第1戦と第2戦は、ここで戦います。（4面）",
        "写真：Syced — CC0（Wikimedia Commons）")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-weekend")
f2.head("スポーツの週末", 25)
f2.para("土よう日は、日本シリーズの開幕と、アジアパラ競技大会の最終日が重なります。日よう日は第2戦です。テレビの前が忙しい週末になります。", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX)
p.text(bx + 22, 1914, "短いニュース　快訊", 24, "sans", True, OLIVE)
brefs = [
    ("紅葉", "日光のいろは坂は、23日（金）から見頃です。（2面）"),
    ("文化", "奈良の正倉院展は、24日（土）から。11月9日までです。（3面）"),
    ("神事", "大阪天満宮の流鏑馬神事は、25日（日）15時です。（3面）"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "クイズ　閃電問答", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "讀頭版，選出正確答案　答案見第8版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "單選", "A", "第1戦は10月24日（土）",
      "日本シリーズの第1戦はいつですか。 A. 24日（土） · B. 25日（日） · C. 22日（木）", size=21)
qf.ex("A2", "單選", "B", "第1戰的地點是橫濱",
      "第1戦の場所はどこですか。 A. 東京 · B. 横浜 · C. 福岡", size=21)
qf.ex("A2", "單選", "B", "亞殘運會週六閉幕",
      "アジアパラ競技大会の最終日は？ A. 金よう日 · B. 土よう日 · C. 月よう日", size=21)
qf.ex("A2", "單選", "C", "DeNA是聯賽第3名",
      "DeNAはリーグ何位でしたか。 A. 1位 · B. 2位 · C. 3位", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-hyoushi.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 生活 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("生活　くらし", "Lucerna", "レベル A2　紅葉と秋の味覚　紅葉與秋日味覺")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("紅葉前線、南へ — 今週末は北の山が見頃です", 32)
f.byline("Lucerna編集部　読むレベル：A2")
f.para("秋が深くなりました。紅葉前線は北から南へ下りています。今週末、北の地方の山や公園で、紅葉がいちばん美しくなります。")
f.para("日本気象株式会社（tenki.jp）の10月14日の予想では、奥入瀬渓流は15日から見頃です。日光のいろは坂は23日（金よう日）から、裏磐梯の五色沼と北海道の大沼公園は24日（土よう日）から見頃です。層雲峡は、21日の時点で、もう葉が落ち始めていました。この予想は、天気で変わることがあります。")
f.para("京都の高尾など、本州の平地の見頃は、もっと後です。11月の半ばから終わりごろです。ですから、『紅葉狩り』に出かける人は、この週末、北の地方へ行きます。")
f.gloss("前線 前線 · 渓流 溪谷河流 · 時点 時刻 · 平地 平原地區。")
f.head("東京では「餅」が人気", 25)
f.para("Googleは10月8日、世界の10の都市の『食トレンド』を発表しました。東京では、『餅』の言葉がある口コミが、前の年より168%増えました。")
f.para("『抹茶』の言葉があるメニューも、10都市のほとんどで増えました。シカゴでは82%、サンティアゴでは84%増えました。秋は、食の季節でもあります。")
f.gloss("口コミ 網上評論 · 増える 增加 · 発表する 公布。")
f.box("『見頃』の使い方　「見頃」的用法", [
    ("「桜の見頃は3月です」", "serif", False, INK, 20, 1.35),
    ("「今年の紅葉は、11月が見頃です」", "serif", False, INK, 20, 1.35),
    ("「見頃を過ぎると、葉が落ちます」", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: maple image + facts + mochi image + あなた (sequential, measured)
ix = COLX[3]
image(p, "maple.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "秋のカエデの葉。北の地方では、今週末が見頃です。",
              "写真：Poliphilo — CC0（Wikimedia Commons）")
facts = ["日光のいろは坂の見頃は、23日（金）からです。",
         "大沼公園と五色沼の見頃は、24日（土）からです。",
         "京都・高尾の見頃は、11月の半ばからです。"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "知っていますか", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
my3 = sy3 + sh + 26
image(p, "mochi.jpg", ix, my3, CW, 180)
cy4 = caption(p, ix, my3 + 180, CW, "手作りの餅。東京では『餅』の口コミが増えています。",
              "写真：Fumikas Sagisavas — CC0（Wikimedia Commons）")
ey3 = cy4 + 18
etvous = "あなたは？今週末、どこへ紅葉を見に行きたいですか。日本語で2文、書いて、送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你呢？這週末想去哪裡看紅葉？寫兩句日語寄來。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？　說說你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你呢？這週末想去哪裡看紅葉？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- season words strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "季節のことば　季節詞語", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "紅葉の季節の4つの言葉　關於紅葉季的四個詞", 20, "sans", False, GREY, anchor="end")
words = [
    ("見頃（みごろ）", "いちばん美しい時", "最佳觀賞期"),
    ("紅葉狩り", "紅葉を見に行くこと", "看紅葉出遊"),
    ("前線（ぜんせん）", "北から南へ動く線", "（氣象）鋒面"),
    ("落ち葉（おちば）", "木から落ちた葉", "落葉"),
]
for i, (t, lab, cn) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 234, "文で覚えましょう：『紅葉前線が下りて、今週末は紅葉狩りの週末です。』", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "練習　第2版練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案見第8版　題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　理解", 25)
e.expl("第2版の文章を読んで、正しい答えを選んでください。")
e.ex("A2", "單選", "B", "紅葉前線自北向南",
     "紅葉前線は、どちらへ下りていますか。 A. 南から北 · B. 北から南 · C. 東から西", size=19, gap=6)
e.ex("A2", "單選", "B", "いろは坂の見頃は23日（金）から",
     "いろは坂の見頃はいつからですか。 A. 15日 · B. 23日 · C. 24日", size=19, gap=6)
e.ex("A2", "單選", "A", "層雲峽的葉子已開始掉落",
     "層雲峡は、21日の時点でどうでしたか。 A. 葉が落ち始めていた · B. まだ青かった · C. 雪だった", size=19, gap=6)
e.ex("A2", "單選", "C", "京都高尾的見頃在11月中旬以後",
     "京都・高尾の見頃はいつですか。 A. 今週末 · B. 10月の終わり · C. 11月の半ばから", size=19, gap=6)
e.ex("A2", "單選", "B", "東京增加的是「餅」的評論",
     "東京で増えたのは、どんな口コミですか。 A. 抹茶 · B. 餅 · C. 紅葉", size=19, gap=6)
e.head("B　ことば", 25)
e.expl("言葉や数字を入れてください。")
e.ex("A2", "完成句子", "見頃", "見頃＝最佳觀賞期",
     "紅葉がいちばん美しい時を「___」と言います。", instr="填空", size=19, gap=6)
e.ex("A2", "完成句子", "紅葉狩り", "紅葉狩り＝去看紅葉",
     "紅葉を見に行くことを「___」と言います。", instr="填空", size=19, gap=6)
e.ex("A2", "完成句子", "168", "「餅」的評論比去年增加168%",
     "『餅』の口コミは、前の年より ___ %増えました。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "82", "芝加哥的抹茶菜單增加82%",
     "シカゴでは、抹茶のメニューが ___ %増えました。", instr="填空", size=19, gap=6)
e.ex("A2", "完成句子", "落ち葉", "落ち葉＝落葉",
     "木から落ちた葉を「___」と言います。", instr="填空", size=19, gap=6)
e.head("C　数字と日付", 25)
e.expl("第1・2版の数字と日付で答えてください。")
e.ex("A2", "完成句子", "15", "奧入瀨溪流15日開始見頃",
     "奥入瀬渓流の見頃は ___ 日からです。", instr="填空", size=19, gap=6)
e.ex("A2", "完成句子", "24", "大沼公園24日（土）開始見頃",
     "大沼公園の見頃は ___ 日（土）からです。", instr="填空", size=19, gap=6)
e.ex("A2", "完成句子", "8", "Google在10月8日公布",
     "Googleの発表は10月 ___ 日でした。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "84", "聖地亞哥增加84%",
     "サンティアゴでは、抹茶のメニューが ___ %増えました。", instr="填空", size=19, gap=6)
e.head("D　ペアにしましょう", 25)
e.match_set("A2", "詞彙配對",
            ["日光のいろは坂", "大沼公園", "京都・高尾", "奥入瀬渓流"],
            ["見頃は15日から",
             "見頃は23日（金）から",
             "見頃は24日（土）から",
             "見頃は11月の半ばから"],
            ["b", "c", "d", "a"],
            ["いろは坂＝23日 b", "大沼公園＝24日 c", "京都・高尾＝11月 d", "奥入瀬＝15日 a"],
            instr="把場所和見頃日期配對")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-kurashi.svg")
print("P2 saved, exercises so far:", len(REG))
