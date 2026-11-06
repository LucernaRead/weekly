# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ja-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · ぶんか", "Lucerna", "レベル A2→B1 · 文化の日と金沢 · La Journée de la culture et Kanazawa")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P3-feature")
f.title("文化の日 — 金沢で、伝統と出会う週", 37)
f.byline("Lucerna編集部 · 読むレベル：A2→B1")
f.para("11月3日（火よう日）は、文化の日です。自由と平和を大切にし、文化をすすめる日です。全国で、文化のイベントがあります。")
f.para("東京の杉並区では、3日（火）に家族オーケストラのイベントがあります。家族で音楽を楽しむイベントです。")
f.para("金沢では、今週、文化のイベントがたくさんあります。3日には『市民美術の日 オープンまるびぃ2026』と『加賀カランコロン』の市場があります。10月30日から11月8日までは、石川県立美術館で『第73回日本伝統工芸展金沢展』があります。")
f.para("金沢城と兼六園では、秋のライトアップの週です。7日（土）も、ライトアップがあります。伝統工芸と紅葉と光を、いっしょに楽しむことができます。")
f.gloss("市場 marché · 工芸 artisanat · 光 lumière · 楽しむ apprécier.")
f.head("伝統工芸展の見方", 25)
f.para("伝統工芸展では、日本の伝統の技による作品を見ることができます。陶器や漆器、染物や金工などです。作った人の名前と、材料の名前も、よく見てください。")
f.para("金沢の伝統工芸は、加賀友禅や金箔が有名です。展覧会は11月8日（日）までです。ゆっくり見るには、午前中がおすすめです。")
f.gloss("陶器 poterie · 漆器 laque · 染物 textiles teints · 金箔 feuille d'or.")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Et vous ? À quel événement culturel aimeriez-vous aller pour la Journée de la culture ? Écrivez deux phrases en japonais et envoyez-les-nous.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？ · À vous la parole", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Et vous ? À quel événement culturel aimeriez-vous aller pour la Journée de la culture ? Écrivez deux phrases en japonais et envoyez-les-nous.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Exercices · page 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · niveaux mélangés, cherchez par numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · 理解", 25)
e.bridge("第3版の文章を読んで、正しい答えを選んでください。")
e.ex("A2", "Choix multiple", "A", "La Journée de la culture, c'est le 3 novembre (mardi)",
     "文化の日はいつですか。 A. 3日（火） · B. 7日（土） · C. 9日（月）", size=19, gap=6)
e.ex("A2", "Choix multiple", "B", "L'événement de Suginami est un orchestre familial",
     "杉並区のイベントは何ですか。 A. 伝統工芸展 · B. 家族オーケストラ · C. ライトアップ", size=19, gap=6)
e.ex("B1", "Choix multiple", "C", "L'exposition d'artisanat : musée d'art d'Ishikawa",
     "伝統工芸展はどこですか。 A. 金沢城 · B. 兼六園 · C. 石川県立美術館", size=19, gap=6)
e.ex("B1", "Choix multiple", "B", "L'exposition dure jusqu'au 8 novembre (dimanche)",
     "伝統工芸展はいつまでですか。 A. 11月3日 · B. 11月8日 · C. 11月9日", size=19, gap=6)
e.ex("A2", "Choix multiple", "A", "Les illuminations : château de Kanazawa et Kenrokuen",
     "ライトアップはどこですか。 A. 金沢城と兼六園 · B. 杉並区 · C. 神戸", size=19, gap=6)
e.head("B · ことば", 25)
e.bridge("言葉や数字を入れてください。")
e.ex("A2", "Compléter", "市場", "市場 = marché",
     "『加賀カランコロン』の ___ があります。", instr="Complétez", size=19, gap=6)
e.ex("A2", "Compléter", "工芸", "工芸 = artisanat",
     "日本の伝統の技で作った作品は「伝統 ___ 」です。", instr="Complétez", size=19, gap=6)
e.ex("B1", "Compléter", "陶器", "陶器 = poterie",
     "伝統工芸の例：___ や漆器、染物や金工です。", instr="Complétez", size=19, gap=6)
e.ex("A2", "Compléter", "8", "L'exposition dure jusqu'au 8 novembre",
     "展覧会は11月 ___ 日（日）までです。", instr="Complétez", size=19, gap=6)
e.ex("B1", "Compléter", "金箔", "金箔 = feuille d'or",
     "金沢の伝統工芸：加賀友禅や ___ が有名です。", instr="Complétez", size=19, gap=6)
e.head("C · 文を作りましょう", 25)
e.bridge("言葉を並べて、正しい文を作ってください。")
e.ex("B1", "Former une phrase", "文化の日は3日です。", "sujet + temps",
     "文化の日は / 3日です → ___", instr="Formez la phrase", size=19, gap=6)
e.ex("A2", "Former une phrase", "金沢で工芸展があります。", "lieu + で + あります",
     "金沢で / 工芸展が / あります → ___", instr="Formez la phrase", size=19, gap=6)
e.ex("B1", "Former une phrase", "ライトアップを見たいです。", "見たい = vouloir voir",
     "ライトアップを / 見たいです → ___", instr="Formez la phrase", size=19, gap=6)
e.ex("B1", "Former une phrase", "家族で音楽を楽しみます。", "en famille",
     "家族で / 音楽を / 楽しみます → ___", instr="Formez la phrase", size=19, gap=6)
e.head("D · ペアにしましょう", 25)
e.match_set("B1", "Appariement",
            ["文化の日", "伝統工芸展", "家族オーケストラ", "ライトアップ"],
            ["金沢城と兼六園 — 7日も",
             "11月3日（火）",
             "石川県立美術館 — 11月8日まで",
             "杉並区 — 3日"],
            ["b", "c", "d", "a"],
            ["文化の日 = 3 novembre b", "工芸展 = musée c", "オーケストラ = Suginami d", "ライトアップ = château de Kanazawa a"],
            instr="Événement, lieu et date")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-bunka.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · スポーツ (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("スポーツ · 体育", "Lucerna", "レベル B1 · 日本シリーズ横浜の2試合 · Les Japan Series : deux matchs à Yokohama")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P4-feature")
f.title("延長戦の連続 — 横浜の2試合", 37)
f.byline("Lucerna編集部 · 読むレベル：B1")
f.para("日本シリーズの第1戦は、10月24日（土よう日）、横浜スタジアムでした。福岡ソフトバンクホークスが、横浜DeNAベイスターズに3対1で勝ちました。試合は延長11回まで続き、4時間12分でした。観客は33,388人でした。")
f.para("第2戦は、25日（日よう日）でした。ソフトバンクが4対3で勝ちました。8回に筒香嘉智選手の3点ホームランでDeNAが逆転しました。でも、9回に山川穂高選手のホームランで同点になり、延長10回に川村友斗選手のホームランでソフトバンクが勝ちました。試合時間は3時間36分、観客は33,432人でした。")
f.para("これで、ソフトバンクが2連勝でスタートしました。過去の記録をまとめると、2連勝で始めたチームの優勝率は73%です。2年前の2024年も、DeNAはホームで2連敗した後、4連勝して優勝しました。相川監督は『4つ勝つかどうかの戦いなので』と話しました。")
f.gloss("延長 manches supplémentaires · 逆転 retournement · 同点 égalité · 優勝率 taux de titre.")
f.head("シリーズの日程", 25)
f.box("日本シリーズの日程 · Calendrier", [
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
f.gloss("総括 bilan · 締め切り date limite · 確認する vérifier.")
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
p.text(MX, ty + 26, "横浜の2試合の記録 · Les deux matchs de Yokohama, en chiffres", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "練習 · Exercices · page 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · niveaux mélangés, cherchez par numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · 理解", 25)
e.bridge("第4版の文章を読んで、正しい答えを選んでください。")
e.ex("B1", "Choix multiple", "B", "Match 1 : SoftBank bat DeNA 3–1",
     "第1戦のスコアは？ A. 4-3 · B. 3-1 · C. 1-3", size=19, gap=6)
e.ex("B1", "Choix multiple", "B", "Le home run de 3 points de Tsutsugo a renversé le match 2",
     "第2戦でDeNAを逆転させたのは？ A. 山川のホームラン · B. 筒香の3点ホームラン · C. 川村のホームラン", size=19, gap=6)
e.ex("B1", "Choix multiple", "A", "SoftBank a commencé par deux victoires d'affilée",
     "2連勝でスタートしたのは？ A. ソフトバンク · B. DeNA · C. 阪神", size=19, gap=6)
e.ex("B1", "Choix multiple", "B", "Mener 2–0, c'est gagner le titre dans 73 % des cas",
     "2連勝で始めたチームの優勝率は？ A. 24% · B. 73% · C. 100%", size=19, gap=6)
e.ex("B1", "Choix multiple", "A", "DeNA a remporté le titre en 2024",
     "2024年に優勝したのは？ A. DeNA · B. ソフトバンク · C. 阪神", size=19, gap=6)
e.head("B · 数字", 25)
e.bridge("第4版の数字を入れてください。")
e.ex("B1", "Compléter", "3", "SoftBank a marqué 3 points au match 1",
     "第1戦、ソフトバンクは ___ 点取りました。", instr="Complétez", size=19, gap=6)
e.ex("B1", "Compléter", "4", "SoftBank a marqué 4 points au match 2",
     "第2戦、ソフトバンクは ___ 点取りました。", instr="Complétez", size=19, gap=6)
e.ex("B1", "Compléter", "11", "Le match 1 est allé jusqu'à la 11e manche",
     "第1戦は延長 ___ 回まで続きました。", instr="Complétez", size=19, gap=6)
e.ex("B1", "Compléter", "10", "Le match 2 est allé jusqu'à la 10e manche",
     "第2戦は延長 ___ 回まで続きました。", instr="Complétez", size=19, gap=6)
e.ex("B1", "Compléter", "73", "Taux de titre : 73 %",
     "2連勝で始めたチームの優勝率は ___ %です。", instr="Complétez", size=19, gap=6)
e.head("C · ことばと記録", 25)
e.bridge("第4版の記事から答えてください。")
e.ex("B1", "Choix multiple", "B", "延長 = le match qui se prolonge",
     "「延長」とは何ですか。 A. 試合が短くなること · B. 試合が長く続くこと · C. 試合がないこと", size=19, gap=6)
e.ex("B1", "Choix multiple", "A", "Public du match 1 : 33 388",
     "第1戦の観客は何人でしたか。 A. 33,388人 · B. 33,432人 · C. 33,000人", size=19, gap=6)
e.ex("B1", "Choix multiple", "B", "Public du match 2 : 33 432",
     "第2戦の観客は何人でしたか。 A. 33,388人 · B. 33,432人 · C. 33,000人", size=19, gap=6)
e.ex("B1", "Choix multiple", "A", "L'entraîneur Aikawa : un combat en quatre victoires",
     "相川監督は何と言いましたか。 A. 4つ勝つかどうかの戦い · B. もう終わり · C. 2つで十分", size=19, gap=6)
e.head("D · 正しい・正しくない", 25)
e.bridge("文が正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "Vrai ou faux", "×", "Le match 1 avait lieu samedi",
     "第1戦は日よう日でした。", instr="Vrai ou faux ?", size=19, gap=6)
e.ex("B1", "Vrai ou faux", "○", "SoftBank a gagné deux fois d'affilée",
     "ソフトバンクが2連勝しました。", instr="Vrai ou faux ?", size=19, gap=6)
e.ex("B1", "Vrai ou faux", "×", "Le match 2 est aussi allé en manches supplémentaires",
     "第2戦は9回で終わりました。", instr="Vrai ou faux ?", size=19, gap=6)
e.ex("B1", "Vrai ou faux", "○", "DeNA a gagné en 2024",
     "2024年はDeNAが優勝しました。", instr="Vrai ou faux ?", size=19, gap=6)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-supotsu.svg")
print("P4 saved, exercises so far:", len(REG))
