# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ja-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 若者・エンタメ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("若者・エンタメ · Youth", "Lucerna", "レベル B1 · ハロウィンと秋まつり · Halloween and autumn festivals")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P5-feature")
f.title("ハロウィンの夜、渋谷のルール", 37)
f.byline("Lucerna編集部 · 読むレベル：B1")
f.para("今年のハロウィンは、10月31日（土よう日）でした。仮装の準備をする人が増えていました。でも、渋谷にはルールがあります。駅の近くでは、一年中、夜18時から朝5時まで、道でお酒を飲むことができません。")
f.para("ゴミを捨てると、その場で2,000円の罰金です。今年の6月から始まったルールです。ハチ公の像は、10月30日から11月1日までフェンスの中にありました。ハロウィンの夜は、お店にお酒を売らないよう、お願いも出ていました。")
f.para("コスプレの大きなイベントは池袋です。『池袋ハロウィンコスプレフェス』は、10月30日から11月1日までの予定でした。ルールを守って、楽しいハロウィンにしましょう。")
f.gloss("罰金 fine · 像 statue · 仮装 dressing up · 守る to follow.")
f.head("秋まつりの週末", 25)
f.para("今週末は、秋まつりの週末でもあります。7日（土）と8日（日）には、『さがみはらフェスタ2026』と『埼玉わんわん秋まつり』があります。8日（日）には、横浜の『中区民祭り ハローよこはま2026』もあります。")
f.para("秋の服の話題も、同じまとめにあります。SNSの話題のまとめ（note、10月22日）では、30代・40代の服として、ペプラムのニットやチェック・ツイードのジャケットが話題だそうです。このまとめは、アンケートの結果ではありません。")
f.gloss("祭り festival · 週末 weekend · 話題 topic.")
f.end_report()

# col 3: pumpkin image + words + あなた
ix = COLX[3]
image(p, "pumpkin.jpg", ix, 200, CW, 262)
cy3 = caption(p, ix, 462, CW, "ハロウィンのかぼちゃ。渋谷では、ルールを守ることが大切でした。",
              "写真：Petr Kratochvil — パブリックドメイン（Wikimedia Commons）")
words5 = ["仮装 — 別の人の服を着ること",
          "コスプレ — キャラクターの服を着ること",
          "フェス — お祭りのイベント"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in words5) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ハロウィンのことば", 24, "sans", True, OLIVE)
yy3 += 52
for t in words5:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "あなたは？秋まつりで、何をしたいですか。日本語で2文、書いて、送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("What about you? What would you like to do at an autumn festival? Write two sentences in Japanese and send them in.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？ · Your turn", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "What about you? What would you like to do at an autumn festival? Write two sentences in Japanese and send them in.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Page 5 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels are mixed — find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · 理解", 25)
e.bridge("第5版の文章を読んで、正しい答えを選んでください。")
e.ex("B1", "multiple choice", "A", "Halloween was October 31 (Saturday)",
     "今年のハロウィンはいつでしたか。 A. 31日（土） · B. 30日（金） · C. 1日（日）", size=19, gap=6)
e.ex("B1", "multiple choice", "B", "Shibuya's street-drinking ban runs 18:00 to 05:00",
     "渋谷で道でお酒を飲めないのは何時から何時までですか。 A. 5時から18時 · B. 18時から5時 · C. 18時から22時", size=19, gap=6)
e.ex("B1", "multiple choice", "B", "Littering costs a 2,000-yen fine",
     "ゴミを捨てた時の罰金はいくらですか。 A. 200円 · B. 2,000円 · C. 20,000円", size=19, gap=6)
e.ex("B1", "multiple choice", "B", "The cosplay festival is in Ikebukuro",
     "コスプレフェスはどこですか。 A. 渋谷 · B. 池袋 · C. 横浜", size=19, gap=6)
e.ex("B1", "multiple choice", "C", "The Naka Ward festival is November 8 (Sunday)",
     "『ハローよこはま2026』はいつですか。 A. 7日（土） · B. 31日（土） · C. 8日（日）", size=19, gap=6)
e.head("B · 数字", 25)
e.bridge("第5版の数字を入れてください。")
e.ex("B1", "fill-in", "31", "Halloween was October 31",
     "ハロウィンは10月 ___ 日（土）でした。", instr="Fill in", size=19, gap=6)
e.ex("B1", "fill-in", "18", "The ban starts at 18:00",
     "道でお酒を飲めないのは、夜 ___ 時からです。", instr="Fill in", size=19, gap=6)
e.ex("B1", "fill-in", "5", "The ban runs to 05:00",
     "道でお酒を飲めないのは、朝 ___ 時までです。", instr="Fill in", size=19, gap=6)
e.ex("B1", "fill-in", "2,000", "Littering costs a 2,000-yen fine",
     "ゴミを捨てると、罰金は ___ 円です。", instr="Fill in", size=19, gap=6)
e.ex("B1", "fill-in", "8", "The Yokohama festival is November 8",
     "『ハローよこはま2026』は11月 ___ 日（日）です。", instr="Fill in", size=19, gap=6)
e.head("C · 正しい・正しくない", 25)
e.bridge("渋谷のルールについて、正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "true/false", "×", "No drinking on the street at night",
     "渋谷では、夜、道でお酒を飲むことができます。", instr="True or false?", size=19, gap=6)
e.ex("B1", "true/false", "○", "The litter fine dates from June this year",
     "ゴミの罰金は、今年の6月からです。", instr="True or false?", size=19, gap=6)
e.ex("B1", "true/false", "×", "The cosplay festival is in Ikebukuro",
     "コスプレフェスは渋谷であります。", instr="True or false?", size=19, gap=6)
e.ex("B1", "true/false", "○", "Halloween was October 31 (Saturday)",
     "ハロウィンは10月31日（土）でした。", instr="True or false?", size=19, gap=6)
e.head("D · 文を完成しましょう", 25)
e.bridge("第5版の文を完成してください。")
e.ex("B1", "fill-in", "飲む", "飲むことができません = cannot drink",
     "駅の近くでは、道でお酒を ___ ことができません。", instr="Fill in", size=19, gap=6)
e.ex("B1", "fill-in", "守って", "守って + 〜しましょう = follow the rules, and let's…",
     "ルールを ___ 、楽しいハロウィンにしましょう。", instr="Fill in", size=19, gap=6)
e.ex("B1", "fill-in", "中", "フェンスの中 = inside the fence",
     "ハチ公の像は、フェンスの ___ にありました。", instr="Fill in", size=19, gap=6)
e.ex("B1", "fill-in", "10月30日", "The festival ran October 30 to November 1",
     "コスプレフェスは ___ から11月1日までの予定でした。", instr="Fill in", size=19, gap=6)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-wakamono.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 深読み (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("深読み · ふかよみ", "Lucerna", "レベル B2 · 暖かい11月と秋の旅 · A warm November and autumn travel")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P6-feature")
f.title("暖かい11月、旅の季節は長くなる", 37)
f.byline("Lucerna編集部 · 読むレベル：B2")
f.para("気象庁の10月20日の3か月予報では、11月から1月まで、全国的に気温は平年より高いそうです。季節風が弱いためです。太平洋側では、雨が多いそうです。冬の始まりの『立冬』は11月7日ですが、今年の11月は暖かい、という予報です。")
f.para("暖かい秋は、旅の計画を変えます。SNSの話題のまとめ（note、10月22日）では、九州の旅の検索が、去年のほぼ2倍になったそうです。でも、1回の旅の予算は下がったそうです。『近くの満足』、つまり、近くで紅葉と温泉とグルメを楽しむ旅が人気だそうです。このまとめは、アンケートの結果ではありません。")
f.para("紅葉の見頃も、今週末が大切です。宮城県の鳴子峡では、10月31日から11月8日の週末が見頃だそうです。気象予報士のブログ（10月18日、17日までの観測による）では、この週末が見頃だそうです。神戸の布引ハーブ園では、7日から12月28日まで、紅葉のライトアップがあります。")
f.para("暖かい11月は、旅の季節が長くなる、ということです。紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。でも、雨が多い予報ですから、傘と暖かい服の準備も大切です。")
f.gloss("予算 budget · 満足 satisfaction · 観測 observation · 追いかける to chase.")
f.end_report()

# col 3: facts + travel words
ix = COLX[3]
facts6 = ["7 — 立冬は11月7日（土）です",
          "7 — 神戸のライトアップは7日から",
          "28 — 神戸のライトアップは12月28日まで",
          "2 — 九州の旅の検索は去年のほぼ2倍"]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts6) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "今週の数字", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts6:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
words6 = ["近場 — 近い場所への旅",
          "温泉 — 温かいお湯の風呂",
          "グルメ — おいしい食べ物"]
wy3 = sy3 + sh + 26
wh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in words6) + 32
p.rect(ix, wy3, CW, wh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = wy3 + 16
p.text(ix + 22, yy3 + 26, "旅のことば", 24, "sans", True, OLIVE)
yy3 += 52
for t in words6:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", wy3 + wh)

# ---- practice chart (full width) ----
chy = 1500
p.text(MX, chy + 26, "グラフを読もう · Reading the chart", 26, "sans", True, OLIVE)
p.text(RIGHT, chy + 26, "練習用データ · Practice data", 21, "sans", True, BRICK, anchor="end")
p.hline(MX, RIGHT, chy + 40, GOLD, 2)
p.text(MX, chy + 78, "秋の旅で、いちばん楽しみにすること（練習用データ — 実際の調査ではありません）", 22, "serif", True, INK)
chart = [("近場の満足", 38), ("温泉", 27), ("紅葉", 21), ("グルメ", 14)]
byy = chy + 104
for name, val in chart:
    p.text(MX, byy + 26, name, 22, "serif", False, INK)
    p.rect(MX + 250, byy, val * 30, 34, fill=OLIVE)
    p.text(MX + 250 + val * 30 + 16, byy + 26, f"{val}%", 22, "sans", True, INK)
    byy += 56
p.para(MX, byy + 22, "このグラフは練習用データです。数字は全部で100%になります。", 19.5, "serif", False, GREY, RIGHT - MX, 1.4)

# ---- P6 exercises ----
ey = 1900
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Page 6 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels are mixed — find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · 理解", 25)
e.bridge("第6版の文章を読んで、正しい答えを選んでください。")
e.ex("B2", "multiple choice", "B", "Temperatures are above average from November to January",
     "気象庁の予報では、気温はどうなりますか。 A. 平年より低い · B. 平年より高い · C. 平年と同じ", size=19, gap=6)
e.ex("B2", "multiple choice", "B", "The Pacific side gets more rain",
     "雨が多いのはどこですか。 A. 日本海側 · B. 太平洋側 · C. 北の地方", size=19, gap=6)
e.ex("B2", "multiple choice", "B", "Kyushu travel searches nearly doubled year on year",
     "九州の旅の検索は、去年と比べてどうなりましたか。 A. 半分 · B. ほぼ2倍 · C. 3倍", size=19, gap=6)
e.ex("B2", "multiple choice", "A", "The budget per trip fell",
     "1回の旅の予算はどうなりましたか。 A. 下がった · B. 上がった · C. 同じ", size=19, gap=6)
e.ex("B2", "multiple choice", "B", "Naruko Gorge peaks over the October 31 – November 8 weekend",
     "鳴子峡の見頃はいつですか。 A. 10月17日 · B. 10月31日から11月8日の週末 · C. 12月28日", size=19, gap=6)
e.head("B · グラフ", 25)
e.bridge("練習用データのグラフを見て答えてください。")
e.ex("B2", "fill-in", "近場の満足", "The chart's top answer is nearby satisfaction",
     "「楽しみにすること」で1位は ___ です。", instr="Fill in", size=19, gap=6)
e.ex("B2", "fill-in", "38", "Nearby satisfaction: 38%",
     "近場の満足と答えた人は ___ %です。", instr="Fill in", size=19, gap=6)
e.ex("B2", "fill-in", "27", "Hot springs: 27%",
     "温泉は ___ %です。", instr="Fill in", size=19, gap=6)
e.ex("B2", "fill-in", "7", "Leaves 21% minus food 14% is 7",
     "紅葉とグルメの差は ___ %です。", instr="Fill in", size=19, gap=6)
e.ex("B2", "fill-in", "65", "38 + 27 = 65",
     "近場の満足と温泉を合わせると ___ %です。", instr="Fill in", size=19, gap=6)
e.ex("B2", "fill-in", "100", "All four add up to 100%",
     "4つの数字を全部足すと ___ %になります。", instr="Fill in", size=19, gap=6)
e.head("C · 数字と事実", 25)
e.bridge("第6版の数字を入れてください。")
e.ex("B2", "fill-in", "7", "立冬 is November 7",
     "立冬は11月 ___ 日（土）です。", instr="Fill in", size=19, gap=6)
e.ex("B2", "fill-in", "28", "The Kobe light-up runs to December 28",
     "神戸のライトアップは12月 ___ 日までです。", instr="Fill in", size=19, gap=6)
e.ex("B2", "fill-in", "2", "Kyushu travel searches are nearly twice last year's",
     "九州の旅の検索は、去年のほぼ ___ 倍です。", instr="Fill in", size=19, gap=6)
e.ex("B2", "fill-in", "20", "The JMA forecast was October 20",
     "気象庁の予報は10月 ___ 日でした。", instr="Fill in", size=19, gap=6)
e.head("D · 正しい・正しくない", 25)
e.bridge("正しければ○、正しくなければ×を書いてください。")
e.ex("B2", "true/false", "×", "November is forecast warmer than average",
     "11月は、平年より寒い予報です。", instr="True or false?", size=19, gap=6)
e.ex("B2", "true/false", "○", "Kyushu travel searches rose",
     "九州の旅の検索は増えました。", instr="True or false?", size=19, gap=6)
e.ex("B2", "true/false", "×", "The chart is practice data",
     "グラフの数字は、本当の調査の結果です。", instr="True or false?", size=19, gap=6)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-fukayomi.svg")
print("P6 saved, exercises so far:", len(REG))
