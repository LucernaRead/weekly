# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ja-de-proof/ed-scratch-svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 若者・エンタメ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("若者・エンタメ · Jugend", "Lucerna", "レベル B1 · ハロウィンと秋まつり · Halloween und Herbstfeste")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P5-feature")
f.title("ハロウィンの夜、渋谷のルール", 37)
f.byline("Lucerna編集部 · 読むレベル：B1")
f.para("今年のハロウィンは、10月31日（土よう日）でした。仮装の準備をする人が増えていました。でも、渋谷にはルールがあります。駅の近くでは、一年中、夜18時から朝5時まで、道でお酒を飲むことができません。")
f.para("ゴミを捨てると、その場で2,000円の罰金です。今年の6月から始まったルールです。ハチ公の像は、10月30日から11月1日までフェンスの中にありました。ハロウィンの夜は、お店にお酒を売らないよう、お願いも出ていました。")
f.para("コスプレの大きなイベントは池袋です。『池袋ハロウィンコスプレフェス』は、10月30日から11月1日までの予定でした。ルールを守って、楽しいハロウィンにしましょう。")
f.gloss("罰金 Geldstrafe · 像 Statue · 仮装 Verkleidung · 守る einhalten.")
f.head("秋まつりの週末", 25)
f.para("今週末は、秋まつりの週末でもあります。7日（土）と8日（日）には、『さがみはらフェスタ2026』と『埼玉わんわん秋まつり』があります。8日（日）には、横浜の『中区民祭り ハローよこはま2026』もあります。")
f.para("秋の服の話題も、同じまとめにあります。SNSの話題のまとめ（note、10月22日）では、30代・40代の服として、ペプラムのニットやチェック・ツイードのジャケットが話題だそうです。このまとめは、アンケートの結果ではありません。")
f.gloss("祭り Fest · 週末 Wochenende · 話題 Thema.")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Und Sie? Was möchten Sie auf einem Herbstfest tun? Schreiben Sie zwei Sätze auf Japanisch und schicken Sie sie ein!", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？ · Sie sind dran", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Und Sie? Was möchten Sie auf einem Herbstfest tun? Schreiben Sie zwei Sätze auf Japanisch und schicken Sie sie ein!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Übungen Seite 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8 · Stufen gemischt — nach Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · 理解", 25)
e.bridge("第5版の文章を読んで、正しい答えを選んでください。")
e.ex("B1", "Multiple Choice", "A", "Halloween war am 31. Oktober (Samstag)",
     "今年のハロウィンはいつでしたか。 A. 31日（土） · B. 30日（金） · C. 1日（日）", size=19, gap=6)
e.ex("B1", "Multiple Choice", "B", "Shibuya: Alkoholverbot 18:00–05:00 Uhr",
     "渋谷で道でお酒を飲めないのは何時から何時までですか。 A. 5時から18時 · B. 18時から5時 · C. 18時から22時", size=19, gap=6)
e.ex("B1", "Multiple Choice", "B", "Weggeworfener Müll kostet 2.000 Yen Strafe",
     "ゴミを捨てた時の罰金はいくらですか。 A. 200円 · B. 2,000円 · C. 20,000円", size=19, gap=6)
e.ex("B1", "Multiple Choice", "B", "Das Cosplay-Festival ist in Ikebukuro",
     "コスプレフェスはどこですか。 A. 渋谷 · B. 池袋 · C. 横浜", size=19, gap=6)
e.ex("B1", "Multiple Choice", "C", "Bürgerfest Naka, Yokohama, 8. November (Sonntag)",
     "『ハローよこはま2026』はいつですか。 A. 7日（土） · B. 31日（土） · C. 8日（日）", size=19, gap=6)
e.head("B · 数字", 25)
e.bridge("第5版の数字を入れてください。")
e.ex("B1", "Ausfüllen", "31", "Halloween war am 31. Oktober",
     "ハロウィンは10月 ___ 日（土）でした。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "18", "Das Verbot beginnt um 18:00 Uhr",
     "道でお酒を飲めないのは、夜 ___ 時からです。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "5", "Das Verbot läuft bis 05:00 Uhr",
     "道でお酒を飲めないのは、朝 ___ 時までです。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "2,000", "Weggeworfener Müll kostet 2.000 Yen Strafe",
     "ゴミを捨てると、罰金は ___ 円です。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "8", "Das Yokohama-Festival ist am 8. November",
     "『ハローよこはま2026』は11月 ___ 日（日）です。", instr="Ausfüllen", size=19, gap=6)
e.head("C · 正しい・正しくない", 25)
e.bridge("渋谷のルールについて、正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "Richtig/Falsch", "×", "Nachts kein Trinken auf der Straße",
     "渋谷では、夜、道でお酒を飲むことができます。", instr="Richtig/Falsch", size=19, gap=6)
e.ex("B1", "Richtig/Falsch", "○", "Die Müllstrafe gilt seit Juni dieses Jahres",
     "ゴミの罰金は、今年の6月からです。", instr="Richtig/Falsch", size=19, gap=6)
e.ex("B1", "Richtig/Falsch", "×", "Das Cosplay-Festival ist in Ikebukuro",
     "コスプレフェスは渋谷であります。", instr="Richtig/Falsch", size=19, gap=6)
e.ex("B1", "Richtig/Falsch", "○", "Halloween war am 31. Oktober (Samstag)",
     "ハロウィンは10月31日（土）でした。", instr="Richtig/Falsch", size=19, gap=6)
e.head("D · 文を完成しましょう", 25)
e.bridge("第5版の文を完成してください。")
e.ex("B1", "Ausfüllen", "飲む", "飲むことができません = nicht trinken können",
     "駅の近くでは、道でお酒を ___ ことができません。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "守って", "守って + 〜しましょう = Regeln einhalten, los!",
     "ルールを ___ 、楽しいハロウィンにしましょう。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "中", "フェンスの中 = innerhalb des Zauns",
     "ハチ公の像は、フェンスの ___ にありました。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "10月30日", "Das Festival lief vom 30. Oktober bis 1. November",
     "コスプレフェスは ___ から11月1日までの予定でした。", instr="Ausfüllen", size=19, gap=6)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-wakamono.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 深読み (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("深読み · ふかよみ", "Lucerna", "レベル B2 · 暖かい11月と秋の旅 · Ein warmer November und Herbstreisen")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P6-feature")
f.title("暖かい11月、旅の季節は長くなる", 37)
f.byline("Lucerna編集部 · 読むレベル：B2")
f.para("気象庁の10月20日の3か月予報では、11月から1月まで、全国的に気温は平年より高いそうです。季節風が弱いためです。太平洋側では、雨が多いそうです。冬の始まりの『立冬』は11月7日ですが、今年の11月は暖かい、という予報です。")
f.para("暖かい秋は、旅の計画を変えます。SNSの話題のまとめ（note、10月22日）では、九州の旅の検索が、去年のほぼ2倍になったそうです。でも、1回の旅の予算は下がったそうです。『近くの満足』、つまり、近くで紅葉と温泉とグルメを楽しむ旅が人気だそうです。このまとめは、アンケートの結果ではありません。")
f.para("紅葉の見頃も、今週末が大切です。宮城県の鳴子峡では、10月31日から11月8日の週末が見頃だそうです。気象予報士のブログ（10月18日、17日までの観測による）では、この週末が見頃だそうです。神戸の布引ハーブ園では、7日から12月28日まで、紅葉のライトアップがあります。")
f.para("暖かい11月は、旅の季節が長くなる、ということです。紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。でも、雨が多い予報ですから、傘と暖かい服の準備も大切です。")
f.gloss("予算 Budget · 満足 Zufriedenheit · 観測 Beobachtung · 追いかける verfolgen.")
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
p.text(MX, chy + 26, "グラフを読もう · Diagramm lesen", 26, "sans", True, OLIVE)
p.text(RIGHT, chy + 26, "練習用データ · Übungsdaten", 21, "sans", True, BRICK, anchor="end")
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
p.text(MX, ey + 28, "練習 · Übungen Seite 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8 · Stufen gemischt — nach Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · 理解", 25)
e.bridge("第6版の文章を読んで、正しい答えを選んでください。")
e.ex("B2", "Multiple Choice", "B", "November–Januar: wärmer als im Durchschnitt",
     "気象庁の予報では、気温はどうなりますか。 A. 平年より低い · B. 平年より高い · C. 平年と同じ", size=19, gap=6)
e.ex("B2", "Multiple Choice", "B", "Auf der Pazifikseite regnet es mehr",
     "雨が多いのはどこですか。 A. 日本海側 · B. 太平洋側 · C. 北の地方", size=19, gap=6)
e.ex("B2", "Multiple Choice", "B", "Kyushu-Reisen: Suche fast verdoppelt",
     "九州の旅の検索は、去年と比べてどうなりましたか。 A. 半分 · B. ほぼ2倍 · C. 3倍", size=19, gap=6)
e.ex("B2", "Multiple Choice", "A", "Das Budget pro Reise sank",
     "1回の旅の予算はどうなりましたか。 A. 下がった · B. 上がった · C. 同じ", size=19, gap=6)
e.ex("B2", "Multiple Choice", "B", "Naruko-Schlucht: Höhepunkt 31. Oktober bis 8. November",
     "鳴子峡の見頃はいつですか。 A. 10月17日 · B. 10月31日から11月8日の週末 · C. 12月28日", size=19, gap=6)
e.head("B · グラフ", 25)
e.bridge("練習用データのグラフを見て答えてください。")
e.ex("B2", "Ausfüllen", "近場の満足", "Grafik-Top: Zufriedenheit in der Nähe",
     "「楽しみにすること」で1位は ___ です。", instr="Ausfüllen", size=19, gap=6)
e.ex("B2", "Ausfüllen", "38", "Zufriedenheit in der Nähe: 38 %",
     "近場の満足と答えた人は ___ %です。", instr="Ausfüllen", size=19, gap=6)
e.ex("B2", "Ausfüllen", "27", "Heiße Quellen: 27 %",
     "温泉は ___ %です。", instr="Ausfüllen", size=19, gap=6)
e.ex("B2", "Ausfüllen", "7", "Laub 21 % minus Essen 14 % ist 7",
     "紅葉とグルメの差は ___ %です。", instr="Ausfüllen", size=19, gap=6)
e.ex("B2", "Ausfüllen", "65", "38 + 27 = 65",
     "近場の満足と温泉を合わせると ___ %です。", instr="Ausfüllen", size=19, gap=6)
e.ex("B2", "Ausfüllen", "100", "Alle vier ergeben zusammen 100 %",
     "4つの数字を全部足すと ___ %になります。", instr="Ausfüllen", size=19, gap=6)
e.head("C · 数字と事実", 25)
e.bridge("第6版の数字を入れてください。")
e.ex("B2", "Ausfüllen", "7", "立冬 ist am 7. November",
     "立冬は11月 ___ 日（土）です。", instr="Ausfüllen", size=19, gap=6)
e.ex("B2", "Ausfüllen", "28", "Die Beleuchtung in Kobe läuft bis zum 28. Dezember",
     "神戸のライトアップは12月 ___ 日までです。", instr="Ausfüllen", size=19, gap=6)
e.ex("B2", "Ausfüllen", "2", "Die Suche nach Kyushu-Reisen hat sich fast verdoppelt",
     "九州の旅の検索は、去年のほぼ ___ 倍です。", instr="Ausfüllen", size=19, gap=6)
e.ex("B2", "Ausfüllen", "20", "Die JMA-Prognose war am 20. Oktober",
     "気象庁の予報は10月 ___ 日でした。", instr="Ausfüllen", size=19, gap=6)
e.head("D · 正しい・正しくない", 25)
e.bridge("正しければ○、正しくなければ×を書いてください。")
e.ex("B2", "Richtig/Falsch", "×", "November: wärmer als im Durchschnitt",
     "11月は、平年より寒い予報です。", instr="Richtig/Falsch", size=19, gap=6)
e.ex("B2", "Richtig/Falsch", "○", "Die Suche nach Kyushu-Reisen stieg",
     "九州の旅の検索は増えました。", instr="Richtig/Falsch", size=19, gap=6)
e.ex("B2", "Richtig/Falsch", "×", "Die Grafik zeigt Übungsdaten",
     "グラフの数字は、本当の調査の結果です。", instr="Richtig/Falsch", size=19, gap=6)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-fukayomi.svg")
print("P6 saved, exercises so far:", len(REG))
