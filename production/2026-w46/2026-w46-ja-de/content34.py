# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ja-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · ぶんか", "Lucerna", "レベル A2→B1 · 七五三と酉の市 · Shichi-Go-San und Tori-no-ichi")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P3-feature")
f.title("七五三 — 着物の子どもと神社", 37)
f.byline("Lucerna編集部 · 読むレベル：A2→B1")
f.para("七五三は、3歳と5歳と7歳の子どものお祝いです。男の子は3歳と5歳、女の子は3歳と7歳でお祝いします。11月15日ごろに、神社へお参りに行きます。")
f.para("子どもは、着物やはかまを着ます。家族と写真を撮ります。神社では、千歳飴をもらいます。今の形は、江戸時代に始まったと言われています。")
f.para("兵庫県の西宮神社では、例年5,000組以上が七五三参りに来るそうです。11月15日だけではありません。いこーよの調査（10月21日までの回答、七五三の家庭200）では、お参りは「11月上旬」が26%でいちばん多く、「11月15日」は3%でした。日にちは、家族によってちがいます。")
f.para("七五三は、子どもの成長を祝う日です。元気に大きくなってほしい、という家族の願いがあります。")
f.gloss("成長 Wachstum · 元気 gesund · 願い ein Wunsch · 日にち das Datum.")
f.head("酉の市と熊手", 25)
f.para("酉の市は、11月の酉の日に開くお祭りです。浅草の鷲神社では、一の酉が7日（土よう日）でした。二の酉は、19日（木よう日）です。2026年は、三の酉がありません。")
f.para("酉の市では、熊手を買います。熊手は、商売繁盛の縁起物です。大きな熊手を、家族や店の人と、いっしょに買う人もいます。")
f.gloss("商売繁盛 blühende Geschäfte · 縁起物 Glücksbringer · 並ぶ sich anstellen.")
f.end_report()

# col 3: print + calendar + あなた
ix = COLX[3]
image(p, "hiroshige.jpg", ix, 200, CW, 222)
cy3 = caption(p, ix, 422, CW, "明治時代の行列の版画（歌川広重（三代）、1876年）。昔の日本の行列の美しさです。",
              "版画：歌川広重（三代）— パブリックドメイン（Wikimedia Commons）")
cal = ["9日（月）読書週間が終わります",
       "11日（水）ポッキーの日",
       "13日（金）ごろ 高尾山の紅葉が見頃",
       "15日（日）七五三の中心の日",
       "19日（木）酉の市・二の酉"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in cal) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "今週の文化カレンダー", 24, "sans", True, OLIVE)
yy3 += 52
for t in cal:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "あなたは？七五三の日に、どんな写真を撮りたいですか。日本語で2文、書いて送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Welches Foto möchtest du an Shichi-Go-San machen? Schreibe zwei Sätze auf Japanisch und schicke sie ein.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？ · Und du?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Welches Foto möchtest du an Shichi-Go-San machen? Schreibe zwei Sätze auf Japanisch und schicke sie ein.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Übungen Seite 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8 · Stufen gemischt — nach Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · 理解", 25)
e.bridge("第3版の文章を読んで、正しい答えを選んでください。")
e.ex("A2", "Multiple Choice", "A", "Shichi-Go-San feiert Kinder von 3, 5 und 7 Jahren",
     "七五三は、だれのお祝いですか。 A. 3歳・5歳・7歳の子ども · B. 20歳の大人 · C. 100歳のお年寄り", size=19, gap=6)
e.ex("A2", "Multiple Choice", "B", "Jungen feiern mit 3 und 5, Mädchen mit 3 und 7",
     "女の子は、何歳でお祝いしますか。 A. 3歳と5歳 · B. 3歳と7歳 · C. 5歳と7歳", size=19, gap=6)
e.ex("B1", "Multiple Choice", "B", "Besuche häufen sich Anfang November (26 %)",
     "調査では、お参りがいちばん多いのはいつですか。 A. 11月15日 · B. 11月上旬 · C. 12月", size=19, gap=6)
e.ex("B1", "Multiple Choice", "A", "Ni-no-tori des Tori-no-ichi ist am 19. November (Donnerstag)",
     "二の酉はいつですか。 A. 19日（木） · B. 7日（土） · C. 15日（日）", size=19, gap=6)
e.ex("A2", "Multiple Choice", "C", "2026 gibt es kein San-no-tori",
     "2026年の酉の市は、どうですか。 A. 三の酉まであります · B. 一の酉だけです · C. 二の酉までです", size=19, gap=6)
e.head("B · ことば", 25)
e.bridge("言葉や数字を入れてください。")
e.ex("A2", "Ausfüllen", "神社", "Shichi-Go-San-Kinder gehen zum Beten zum Schrein",
     "七五三の子どもは、___ へお参りに行きます。", instr="Ausfüllen", size=19, gap=6)
e.ex("A2", "Ausfüllen", "千歳飴", "rot-weißes langes Bonbon",
     "神社では、___ をもらいます。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "熊手", "熊手 = Glücksrechen für gute Geschäfte",
     "酉の市では、___ を買います。", instr="Ausfüllen", size=19, gap=6)
e.ex("A2", "Ausfüllen", "15", "Shichi-Go-San findet um den 15. November statt",
     "七五三は、11月 ___ 日ごろに行います。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "26", "Besuche Anfang November lagen in der Umfrage bei 26 %",
     "調査では、「11月上旬」は ___ %でした。", instr="Ausfüllen", size=19, gap=6)
e.head("C · 文を作りましょう", 25)
e.bridge("言葉を並べて、正しい文を作ってください。")
e.ex("B1", "Satzbau", "七五三は子どものお祝いです。", "Subjekt + Beschreibung",
     "七五三は / 子どもの / お祝いです → ___", instr="Satz bilden", size=19, gap=6)
e.ex("A2", "Satzbau", "神社へお参りに行きます。", "Ort + へ + Verb",
     "神社へ / お参りに / 行きます → ___", instr="Satz bilden", size=19, gap=6)
e.ex("B1", "Satzbau", "千歳飴をもらいます。", "Objekt + Verb",
     "千歳飴を / もらいます → ___", instr="Satz bilden", size=19, gap=6)
e.ex("B1", "Satzbau", "酉の市で熊手を買います。", "Einen Kumade auf dem Tori-no-ichi kaufen",
     "酉の市で / 熊手を / 買います → ___", instr="Satz bilden", size=19, gap=6)
e.head("D · ペアにしましょう", 25)
e.match_set("B1", "Zuordnen",
            ["七五三", "千歳飴", "熊手", "酉の市"],
            ["11月の酉の日に開くお祭り",
             "3歳・5歳・7歳の子どものお祝い",
             "商売繁盛の縁起物",
             "赤と白の長い飴"],
            ["b", "d", "c", "a"],
            ["七五三 = ein Fest für Kinder von 3, 5 und 7 Jahren b", "千歳飴 = rot-weißes langes Bonbon d", "熊手 = Glücksrechen c", "酉の市 = ein Fest an den Hahntagen im November a"],
            instr="Wörter zuordnen")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-bunka.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · スポーツ (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("スポーツ · 体育", "Lucerna", "レベル B1 · 日本シリーズ4連勝 · Vier Siege in Folge in der Japan Series")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P4-feature")
f.title("4連勝 — 接戦の日本シリーズ", 37)
f.byline("Lucerna編集部 · 読むレベル：B1")
f.para("日本シリーズは、10月24日（土よう日）に始まりました。福岡ソフトバンクホークスと、横浜DeNAベイスターズの対戦でした。第1戦は、ソフトバンクが3対1で勝ちました。第2戦も、ソフトバンクが4対3で勝ちました。2試合とも、延長戦でした。")
f.para("第3戦は、10月27日（火よう日）、福岡でした。ソフトバンクが2対1で勝ちました。延長10回に、正木智也選手のサヨナラホームランで決まりました。第4戦は、10月28日（水よう日）に、ソフトバンクが4対2で勝ちました。")
f.para("ソフトバンクが4連勝で日本一になりました。2年連続、13度目の日本一です。第5戦から第7戦は、行われませんでした。シリーズのMVPは、正木智也選手です。4試合とも、2点差以内の接戦でした。第1戦から第3戦まで、3試合連続の延長戦は、日本シリーズで初めてだそうです。")
f.gloss("接戦 ein enges Spiel · サヨナラ Walk-off (Sayonara) · 連続 in Folge.")
f.head("シリーズの記録", 25)
f.box("日本シリーズの記録 · Bilanz", [
    ("第1戦 — 10月24日（土）横浜：ソフトバンク 3-1 DeNA（延長11回）", "serif", False, INK, 20, 1.35),
    ("第2戦 — 10月25日（日）横浜：ソフトバンク 4-3 DeNA（延長10回）", "serif", False, INK, 20, 1.35),
    ("第3戦 — 10月27日（火）福岡：ソフトバンク 2-1 DeNA（延長10回）", "serif", False, INK, 20, 1.35),
    ("第4戦 — 10月28日（水）福岡：ソフトバンク 4-2 DeNA", "serif", False, INK, 20, 1.35),
    ("第5戦〜第7戦 — 行われませんでした", "serif", False, GREY, 20, 1.35),
    ("MVP — 正木智也選手（ソフトバンク）", "serif", False, INK, 20, 1.35),
])
f.para("前号（VOL.2）では、第3戦からの結果が分かりませんでした。今号で、全部の結果をお知らせします。")
f.gloss("前号 die letzte Ausgabe · 全部 alles.")
f.end_report()

# col 3: stadium image + 4-win box
ix = COLX[3]
image(p, "stadium.jpg", ix, 200, CW, 290)
cy3 = caption(p, ix, 490, CW, "横浜スタジアム。第1戦と第2戦は、ここで戦いました。",
              "写真：Syced — CC0（Wikimedia Commons）")
ot = "4連勝は、4試合とも勝つことです。2年連続の日本一は、去年も今年も優勝した、という意味です。13度目は、13回目です。"
oy = cy3 + 24
oh = 62 + len(wrap(ot, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("※記録は各試合の報道によるものです。", "serif", False, 19.5, CW - 44)) * 27 + 20 + 8
p.rect(ix, oy, CW, oh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = oy + 16
p.text(ix + 22, yy3 + 26, "4連勝の意味", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, ot, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "※記録は各試合の報道によるものです。", 19.5, "serif", False, GREY, CW - 44, 1.38)
print("P4 col3 ends", oy + oh)

# ---- sumo box (full width) ----
ty = 1490
p.text(MX, ty + 26, "大相撲九州場所が始まりました · Das Kyushu-Sumoturnier hat begonnen", 26, "sans", True, OLIVE)
p.hline(MX, RIGHT, ty + 40, GOLD, 2)
p.para(MX, ty + 78, "大相撲の九州場所は、8日（日よう日）に福岡国際センターで始まりました。横綱は大の里と豊昇龍です。10月26日に発表された番付では、美ノ海が新小結になりました。沖縄県の力士で初めての三役だそうです。玉鷲は、41歳11か月で再入幕しました。場所は、22日（日よう日）までです。今週の勝敗は、次号でお知らせします。", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1840
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Übungen Seite 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8 · Stufen gemischt — nach Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · 理解", 25)
e.bridge("第4版の文章を読んで、正しい答えを選んでください。")
e.ex("B1", "Multiple Choice", "B", "Spiel 3: SoftBank gewann 2:1",
     "第3戦のスコアは？ A. 4-2 · B. 2-1 · C. 1-2", size=19, gap=6)
e.ex("B1", "Multiple Choice", "B", "Masaki schlug den Walk-off-Homerun in Spiel 3",
     "第3戦のサヨナラホームランを打ったのは？ A. 山川選手 · B. 正木選手 · C. 川村選手", size=19, gap=6)
e.ex("B1", "Multiple Choice", "A", "Spiel 4: SoftBank gewann 4:2",
     "第4戦のスコアは？ A. 4-2 · B. 2-4 · C. 3-1", size=19, gap=6)
e.ex("B1", "Multiple Choice", "B", "MVP der Serie ist Masaki Tomoya",
     "シリーズのMVPはだれですか。 A. 山川選手 · B. 正木選手 · C. 筒香選手", size=19, gap=6)
e.ex("B1", "Multiple Choice", "A", "Die Spiele 5 bis 7 fanden nicht statt",
     "第5戦から第7戦は、どうなりましたか。 A. 行われませんでした · B. 横浜で行われました · C. 福岡で行われました", size=19, gap=6)
e.head("B · 数字", 25)
e.bridge("第4版の数字を入れてください。")
e.ex("B1", "Ausfüllen", "2", "SoftBank erzielte 2 Punkte in Spiel 3",
     "第3戦、ソフトバンクは ___ 点取りました。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "4", "SoftBank erzielte 4 Punkte in Spiel 4",
     "第4戦、ソフトバンクは ___ 点取りました。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "10", "Spiel 3 ging bis ins 10. Inning",
     "第3戦は延長 ___ 回で決まりました。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "13", "SoftBanks 13. Titel",
     "ソフトバンクは ___ 度目の日本一です。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "3", "Die ersten drei Spiele gingen alle in die Verlängerung",
     "第1戦から第3戦まで、___ 試合連続の延長戦でした。", instr="Ausfüllen", size=19, gap=6)
e.head("C · ことばと記録", 25)
e.bridge("第4版の記事から答えてください。")
e.ex("B1", "Multiple Choice", "B", "接戦 = ein enges Spiel",
     "「接戦」とは何ですか。 A. 大差の試合 · B. 点差が小さい試合 · C. 試合がないこと", size=19, gap=6)
e.ex("B1", "Multiple Choice", "A", "Das Kyushu-Turnier findet im Fukuoka Kokusai Center statt",
     "九州場所はどこですか。 A. 福岡国際センター · B. 横浜スタジアム · C. 東京ドーム", size=19, gap=6)
e.ex("B1", "Multiple Choice", "B", "Der neue Komusubi ist Umi-no-umi",
     "新小結になったのはだれですか。 A. 玉鷲 · B. 美ノ海 · C. 大の里", size=19, gap=6)
e.ex("B1", "Multiple Choice", "A", "Das Sumoturnier läuft bis zum 22. November (Sonntag)",
     "九州場所はいつまでですか。 A. 22日（日） · B. 15日（日） · C. 28日（水）", size=19, gap=6)
e.head("D · 正しい・正しくない", 25)
e.bridge("文が正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "Richtig/Falsch", "○", "Vier Siege in Folge zum Titel",
     "ソフトバンクは、4連勝しました。", instr="Richtig/Falsch", size=19, gap=6)
e.ex("B1", "Richtig/Falsch", "×", "Spiel 3 fand in Yokohama statt",
     "第3戦は横浜で行われました。", instr="Richtig/Falsch", size=19, gap=6)
e.ex("B1", "Richtig/Falsch", "×", "Spiel 5 fand auch statt",
     "第5戦も行われました。", instr="Richtig/Falsch", size=19, gap=6)
e.ex("B1", "Richtig/Falsch", "○", "Die ersten drei Spiele gingen alle in die Verlängerung",
     "第1戦から第3戦まで、延長戦でした。", instr="Richtig/Falsch", size=19, gap=6)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-supotsu.svg")
print("P4 saved, exercises so far:", len(REG))
