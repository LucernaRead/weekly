# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ja-de-proof/ed-scratch-svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · ぶんか", "Lucerna", "レベル A2→B1 · 文化の日と金沢 · Kulturtag und Kanazawa")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P3-feature")
f.title("文化の日 — 金沢で、伝統と出会う週", 37)
f.byline("Lucerna編集部 · 読むレベル：A2→B1")
f.para("11月3日（火よう日）は、文化の日です。自由と平和を大切にし、文化をすすめる日です。全国で、文化のイベントがあります。")
f.para("東京の杉並区では、3日（火）に家族オーケストラのイベントがあります。家族で音楽を楽しむイベントです。")
f.para("金沢では、今週、文化のイベントがたくさんあります。3日には『市民美術の日 オープンまるびぃ2026』と『加賀カランコロン』の市場があります。10月30日から11月8日までは、石川県立美術館で『第73回日本伝統工芸展金沢展』があります。")
f.para("金沢城と兼六園では、秋のライトアップの週です。7日（土）も、ライトアップがあります。伝統工芸と紅葉と光を、いっしょに楽しむことができます。")
f.gloss("市場 Markt · 工芸 Kunsthandwerk · 光 Licht · 楽しむ genießen.")
f.head("伝統工芸展の見方", 25)
f.para("伝統工芸展では、日本の伝統の技による作品を見ることができます。陶器や漆器、染物や金工などです。作った人の名前と、材料の名前も、よく見てください。")
f.para("金沢の伝統工芸は、加賀友禅や金箔が有名です。展覧会は11月8日（日）までです。ゆっくり見るには、午前中がおすすめです。")
f.gloss("陶器 Keramik · 漆器 Lackwaren · 染物 gefärbte Textilien · 金箔 Blattgold.")
f.end_report()

# col 3: print + calendar + あなた
ix = COLX[3]
image(p, "hiroshige.jpg", ix, 200, CW, 222)
cy3 = caption(p, ix, 422, CW, "明治時代の行列の版画（歌川広重（三代）、1876年）。文化の日の芸術のように、昔の日本の美しさです。",
              "版画：歌川広重（三代）— パブリックドメイン（Wikimedia Commons）")
cal = ["3日（火）文化の日 — 全国で文化のイベント",
       "3日（火）杉並・家族オーケストラ",
       "10月30日〜11月8日 伝統工芸展金沢展",
       "7日（土）金沢城・兼六園のライトアップ"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in cal) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "今週の文化カレンダー", 24, "sans", True, OLIVE)
yy3 += 52
for t in cal:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "あなたは？文化の日に、どんな文化のイベントへ行きたいですか。日本語で2文、書いて送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Und Sie? Zu welcher Kulturveranstaltung möchten Sie am Kulturtag gehen? Schreiben Sie zwei Sätze auf Japanisch und schicken Sie sie ein!", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？ · Sie sind dran", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Und Sie? Zu welcher Kulturveranstaltung möchten Sie am Kulturtag gehen? Schreiben Sie zwei Sätze auf Japanisch und schicken Sie sie ein!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Übungen Seite 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8 · Stufen gemischt — nach Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · 理解", 25)
e.bridge("第3版の文章を読んで、正しい答えを選んでください。")
e.ex("A2", "Multiple Choice", "A", "Der Kulturtag ist am 3. November (Dienstag)",
     "文化の日はいつですか。 A. 3日（火） · B. 7日（土） · C. 9日（月）", size=19, gap=6)
e.ex("A2", "Multiple Choice", "B", "Die Veranstaltung in Suginami ist ein Familienorchester",
     "杉並区のイベントは何ですか。 A. 伝統工芸展 · B. 家族オーケストラ · C. ライトアップ", size=19, gap=6)
e.ex("B1", "Multiple Choice", "C", "Kunsthandwerksausstellung im Ishikawa-Kunstmuseum",
     "伝統工芸展はどこですか。 A. 金沢城 · B. 兼六園 · C. 石川県立美術館", size=19, gap=6)
e.ex("B1", "Multiple Choice", "B", "Die Ausstellung läuft bis zum 8. November (Sonntag)",
     "伝統工芸展はいつまでですか。 A. 11月3日 · B. 11月8日 · C. 11月9日", size=19, gap=6)
e.ex("A2", "Multiple Choice", "A", "Beleuchtung: Burg Kanazawa und Kenrokuen",
     "ライトアップはどこですか。 A. 金沢城と兼六園 · B. 杉並区 · C. 神戸", size=19, gap=6)
e.head("B · ことば", 25)
e.bridge("言葉や数字を入れてください。")
e.ex("A2", "Ausfüllen", "市場", "市場 = Markt",
     "『加賀カランコロン』の ___ があります。", instr="Ausfüllen", size=19, gap=6)
e.ex("A2", "Ausfüllen", "工芸", "工芸 = Kunsthandwerk",
     "日本の伝統の技で作った作品は「伝統 ___ 」です。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "陶器", "陶器 = Keramik",
     "伝統工芸の例：___ や漆器、染物や金工です。", instr="Ausfüllen", size=19, gap=6)
e.ex("A2", "Ausfüllen", "8", "工艺展到11月8日",
     "展覧会は11月 ___ 日（日）までです。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "金箔", "金箔 = Blattgold",
     "金沢の伝統工芸：加賀友禅や ___ が有名です。", instr="Ausfüllen", size=19, gap=6)
e.head("C · 文を作りましょう", 25)
e.bridge("言葉を並べて、正しい文を作ってください。")
e.ex("B1", "Satzbau", "文化の日は3日です。", "Subjekt + Zeit",
     "文化の日は / 3日です → ___", instr="Satz bilden", size=19, gap=6)
e.ex("A2", "Satzbau", "金沢で工芸展があります。", "Ort + で + あります",
     "金沢で / 工芸展が / あります → ___", instr="Satz bilden", size=19, gap=6)
e.ex("B1", "Satzbau", "ライトアップを見たいです。", "見たい = sehen wollen",
     "ライトアップを / 見たいです → ___", instr="Satz bilden", size=19, gap=6)
e.ex("B1", "Satzbau", "家族で音楽を楽しみます。", "zusammen mit der Familie",
     "家族で / 音楽を / 楽しみます → ___", instr="Satz bilden", size=19, gap=6)
e.head("D · ペアにしましょう", 25)
e.match_set("B1", "Zuordnen",
            ["文化の日", "伝統工芸展", "家族オーケストラ", "ライトアップ"],
            ["金沢城と兼六園 — 7日も",
             "11月3日（火）",
             "石川県立美術館 — 11月8日まで",
             "杉並区 — 3日"],
            ["b", "c", "d", "a"],
            ["文化の日 = 3. November b", "工芸展 = Museum c", "オーケストラ = Suginami d", "ライトアップ = Burg Kanazawa a"],
            instr="Ereignisse den Orten und Daten zuordnen")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-bunka.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · スポーツ (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("スポーツ · 体育", "Lucerna", "レベル B1 · 日本シリーズ横浜の2試合 · Die Japan Series: zwei Spiele in Yokohama")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P4-feature")
f.title("延長戦の連続 — 横浜の2試合", 37)
f.byline("Lucerna編集部 · 読むレベル：B1")
f.para("日本シリーズの第1戦は、10月24日（土よう日）、横浜スタジアムでした。福岡ソフトバンクホークスが、横浜DeNAベイスターズに3対1で勝ちました。試合は延長11回まで続き、4時間12分でした。観客は33,388人でした。")
f.para("第2戦は、25日（日よう日）でした。ソフトバンクが4対3で勝ちました。8回に筒香嘉智選手の3点ホームランでDeNAが逆転しました。でも、9回に山川穂高選手のホームランで同点になり、延長10回に川村友斗選手のホームランでソフトバンクが勝ちました。試合時間は3時間36分、観客は33,432人でした。")
f.para("これで、ソフトバンクが2連勝でスタートしました。過去の記録をまとめると、2連勝で始めたチームの優勝率は73%です。2年前の2024年も、DeNAはホームで2連敗した後、4連勝して優勝しました。相川監督は『4つ勝つかどうかの戦いなので』と話しました。")
f.gloss("延長 Verlängerung · 逆転 Aufholjagd · 同点 Gleichstand · 優勝率 Titelquote.")
f.head("シリーズの日程", 25)
f.box("日本シリーズの日程 · Spielplan", [
    ("第1戦 — 10月24日（土）横浜：ソフトバンク 3-1 DeNA（延長11回）", "serif", False, INK, 20, 1.35),
    ("第2戦 — 10月25日（日）横浜：ソフトバンク 4-3 DeNA（延長10回）", "serif", False, INK, 20, 1.35),
    ("第3戦 — 10月27日（火）福岡", "serif", False, INK, 20, 1.35),
    ("第4戦 — 10月28日（水）福岡", "serif", False, INK, 20, 1.35),
    ("第5戦 — 10月29日（木）福岡", "serif", False, INK, 20, 1.35),
    ("第6戦 — 10月31日（土）横浜", "serif", False, INK, 20, 1.35),
    ("第7戦 — 11月1日（日）横浜", "serif", False, INK, 20, 1.35),
    ("※ 第3戦からの結果は、次号（VOL.3）で総括します", "serif", False, GREY, 20, 1.35),
])
f.para("シリーズの最終結果は、次号（VOL.3）のスポーツ面で総括します。第3戦からの結果は、本号の締め切りまでに確認できませんでした。")
f.gloss("総括 Rückblick · 締め切り Redaktionsschluss · 確認する bestätigen.")
f.end_report()

# col 3: stadium image + 73% box
ix = COLX[3]
image(p, "stadium.jpg", ix, 200, CW, 290)
cy3 = caption(p, ix, 490, CW, "横浜スタジアム。第1戦と第2戦は、ここで戦いました。",
              "写真：Syced — CC0（Wikimedia Commons）")
ot = "2連勝で始めたチームが優勝する確率は、73%です。4チームのうち、3チームぐらいが優勝する、という意味です。"
oy = cy3 + 24
oh = 62 + len(wrap(ot, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("※確率は過去の記録のまとめです。", "serif", False, 19.5, CW - 44)) * 27 + 20 + 8
p.rect(ix, oy, CW, oh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = oy + 16
p.text(ix + 22, yy3 + 26, "73%の意味", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, ot, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "※確率は過去の記録のまとめです。", 19.5, "serif", False, GREY, CW - 44, 1.38)
print("P4 col3 ends", oy + oh)

# ---- two-game record table (full width) ----
ty = 1490
p.text(MX, ty + 26, "横浜の2試合の記録 · Die zwei Yokohama-Spiele im Überblick", 26, "sans", True, OLIVE)
p.hline(MX, RIGHT, ty + 40, GOLD, 2)
rec_l = ["第1戦 — 10月24日（土）横浜：ソフトバンク 3-1 DeNA", "延長11回 · 4時間12分 · 観客 33,388人"]
rec_r = ["第2戦 — 10月25日（日）横浜：ソフトバンク 4-3 DeNA", "延長10回 · 3時間36分 · 観客 33,432人"]
colw2 = (RIGHT - MX - GUT) // 2
for i, s in enumerate(rec_l):
    p.text(MX, ty + 84 + i * 40, s, 21.5, "serif", False, INK)
for i, s in enumerate(rec_r):
    p.text(MX + colw2 + GUT, ty + 84 + i * 40, s, 21.5, "serif", False, INK)
p.para(MX, ty + 84 + 2 * 40 + 6, "2試合とも延長戦でした。横浜のファンは、2試合とも悔しい夜を過ごしました。", 20, "serif", False, GREY, RIGHT - MX, 1.4)

# ---- P4 exercises ----
ey = 1840
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Übungen Seite 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8 · Stufen gemischt — nach Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · 理解", 25)
e.bridge("第4版の文章を読んで、正しい答えを選んでください。")
e.ex("B1", "Multiple Choice", "B", "Spiel 1: SoftBank schlug DeNA 3:1",
     "第1戦のスコアは？ A. 4-3 · B. 3-1 · C. 1-3", size=19, gap=6)
e.ex("B1", "Multiple Choice", "B", "Tsutsugos 3-Punkte-Homerun wendete Spiel 2",
     "第2戦でDeNAを逆転させたのは？ A. 山川のホームラン · B. 筒香の3点ホームラン · C. 川村のホームラン", size=19, gap=6)
e.ex("B1", "Multiple Choice", "A", "SoftBank startete mit zwei Siegen in Folge",
     "2連勝でスタートしたのは？ A. ソフトバンク · B. DeNA · C. 阪神", size=19, gap=6)
e.ex("B1", "Multiple Choice", "B", "Teams mit 2:0-Start gewinnen in 73 % der Fälle den Titel",
     "2連勝で始めたチームの優勝率は？ A. 24% · B. 73% · C. 100%", size=19, gap=6)
e.ex("B1", "Multiple Choice", "A", "DeNA gewann 2024 den Titel",
     "2024年に優勝したのは？ A. DeNA · B. ソフトバンク · C. 阪神", size=19, gap=6)
e.head("B · 数字", 25)
e.bridge("第4版の数字を入れてください。")
e.ex("B1", "Ausfüllen", "3", "SoftBank erzielte 3 Punkte in Spiel 1",
     "第1戦、ソフトバンクは ___ 点取りました。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "4", "SoftBank erzielte 4 Punkte in Spiel 2",
     "第2戦、ソフトバンクは ___ 点取りました。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "11", "Spiel 1 ging über 11 Innings",
     "第1戦は延長 ___ 回まで続きました。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "10", "Spiel 2 ging über 10 Innings",
     "第2戦は延長 ___ 回まで続きました。", instr="Ausfüllen", size=19, gap=6)
e.ex("B1", "Ausfüllen", "73", "Titelquote 73 %",
     "2連勝で始めたチームの優勝率は ___ %です。", instr="Ausfüllen", size=19, gap=6)
e.head("C · ことばと記録", 25)
e.bridge("第4版の記事から答えてください。")
e.ex("B1", "Multiple Choice", "B", "延長 = Verlängerung",
     "「延長」とは何ですか。 A. 試合が短くなること · B. 試合が長く続くこと · C. 試合がないこと", size=19, gap=6)
e.ex("B1", "Multiple Choice", "A", "Spiel 1: 33.388 Zuschauer",
     "第1戦の観客は何人でしたか。 A. 33,388人 · B. 33,432人 · C. 33,000人", size=19, gap=6)
e.ex("B1", "Multiple Choice", "B", "Spiel 2: 33.432 Zuschauer",
     "第2戦の観客は何人でしたか。 A. 33,388人 · B. 33,432人 · C. 33,000人", size=19, gap=6)
e.ex("B1", "Multiple Choice", "A", "Trainer Aikawa sprach vom Kampf um vier Siege",
     "相川監督は何と言いましたか。 A. 4つ勝つかどうかの戦い · B. もう終わり · C. 2つで十分", size=19, gap=6)
e.head("D · 正しい・正しくない", 25)
e.bridge("文が正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "Richtig/Falsch", "×", "Spiel 1 war an einem Samstag",
     "第1戦は日よう日でした。", instr="Richtig/Falsch", size=19, gap=6)
e.ex("B1", "Richtig/Falsch", "○", "SoftBank gewann zweimal in Folge",
     "ソフトバンクが2連勝しました。", instr="Richtig/Falsch", size=19, gap=6)
e.ex("B1", "Richtig/Falsch", "×", "Auch Spiel 2 ging in die Verlängerung",
     "第2戦は9回で終わりました。", instr="Richtig/Falsch", size=19, gap=6)
e.ex("B1", "Richtig/Falsch", "○", "DeNA gewann 2024",
     "2024年はDeNAが優勝しました。", instr="Richtig/Falsch", size=19, gap=6)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-supotsu.svg")
print("P4 saved, exercises so far:", len(REG))
