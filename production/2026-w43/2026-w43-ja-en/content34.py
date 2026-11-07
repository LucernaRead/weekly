# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ja-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · ぶんか", "Lucerna", "レベル A2→B1 · 時代祭と週末 · Jidai Matsuri and the weekend")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P3-feature")
f.title("歩く歴史の本 — 京都の時代祭", 37)
f.byline("Lucerna編集部 · 読むレベル：A2→B1")
f.para("10月22日（木よう日）は、京都の『時代祭』の日です。時代祭は、京都の三大祭りの一つです。昔の服を着た約2,000人の行列が、町を歩きます。")
f.para("行列は、京都御苑を12時に出発します。平安神宮に着くのは、14時30分ごろです。行列は『逆の歴史』です。最初は明治時代の姿で、最後は、平安京ができた時代の姿です。歩きながら、日本の長い歴史を見ることができます。")
f.para("土よう日（24日）からは、奈良国立博物館で『正倉院展』が始まります。11月9日までです。正倉院の宝物を近くで見ることができる、秋だけの特別な展覧会です。")
f.para("日よう日（25日）の15時には、大阪天満宮で『流鏑馬神事』があります。馬に乗り、走りながら矢を射る、古い神事です。週末は、関西が文化で熱くなります。")
f.gloss("行列 a procession · 御苑 an imperial garden · 神事 a Shinto rite · 矢 an arrow · 宝物 treasures.")
f.head("行列の見方 — 逆の歴史を歩く", 25)
f.para("行列は『逆の歴史』です。いちばん前は明治時代の姿です。その後、時代は少しずつ古くなります。最後は、平安京ができた時代（794年ごろ）の姿です。歩きながら、時代の旅ができます。")
f.para("行列は約2,000人で、とても長い列です。12時に京都御苑を出発して、14時30分ごろ、平安神宮に着きます。明治時代の服から平安時代の服まで、服の変化も楽しみの一つです。")
f.gloss("姿 a figure in period dress · 変化 change · 楽しみ a pleasure · ごろ around (a time).")
f.end_report()

# col 3: print + calendar + あなた
ix = COLX[3]
image(p, "hiroshige.jpg", ix, 200, CW, 222)
cy3 = caption(p, ix, 422, CW, "明治時代の行列の版画（歌川広重（三代）、1876年）。時代祭の行列も、明治時代の姿から始まります。",
              "版画：歌川広重（三代）— パブリックドメイン（Wikimedia Commons）")
cal = ["22日（木）時代祭 — 京都、12時に出発",
       "24日（土）正倉院展が始まる — 奈良、11月9日まで",
       "25日（日）流鏑馬神事 — 大阪天満宮、15時"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in cal) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "週末の文化カレンダー", 24, "sans", True, OLIVE)
yy3 += 52
for t in cal:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "あなたは？三つのイベントの中で、どれを見たいですか。日本語で2文、書いて送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("And you? Which of the three events do you most want to see? Write two sentences in Japanese and send them in.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？ · Your turn", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "And you? Which of the three events do you most want to see? Write two sentences in Japanese and send them in.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Page 3 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels are mixed — find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · 理解", 25)
e.expl("第3版の文章を読んで、正しい答えを選んでください。")
e.ex("A2", "multiple choice", "A", "Jidai Matsuri is Thu, October 22",
     "時代祭があるのは何日ですか。 A. 22日（木） · B. 24日（土） · C. 25日（日）", size=19, gap=6)
e.ex("A2", "multiple choice", "B", "About 2,000 people take part",
     "行列には何人ぐらい出ますか。 A. 約200人 · B. 約2,000人 · C. 約20,000人", size=19, gap=6)
e.ex("A2", "multiple choice", "B", "It starts from Kyoto Gyoen",
     "行列はどこから出発しますか。 A. 平安神宮 · B. 京都御苑 · C. 大阪天満宮", size=19, gap=6)
e.ex("B1", "multiple choice", "C", "The Shosoin Exhibition is in Nara",
     "正倉院展はどこですか。 A. 京都 · B. 大阪 · C. 奈良", size=19, gap=6)
e.ex("B1", "multiple choice", "A", "Yabusame shoots arrows",
     "流鏑馬神事では、何を射ますか。 A. 矢 · B. ボール · C. 花", size=19, gap=6)
e.head("B · ことば", 25)
e.expl("言葉や数字を入れてください。")
e.ex("A2", "fill-in", "行列", "行列 = a procession",
     "昔の服を着た人の列を「___」と言います。", instr="Fill in", size=19, gap=6)
e.ex("A2", "fill-in", "出発", "出発 = to set off",
     "行列は12時に京都御苑を ___ します。", instr="Fill in", size=19, gap=6)
e.ex("B1", "fill-in", "流鏑馬神事", "流鏑馬神事 = the yabusame rite",
     "馬に乗り、走りながら矢を射る神事は「___」です。", instr="Fill in", size=19, gap=6)
e.ex("A2", "fill-in", "9", "The Shosoin Exhibition ends Nov 9",
     "正倉院展は11月 ___ 日までです。", instr="Fill in", size=19, gap=6)
e.ex("A2", "fill-in", "三大", "One of Kyoto's three great festivals",
     "時代祭は京都の ___ 祭りの一つです。", instr="Fill in", size=19, gap=6)
e.head("C · 文を作りましょう", 25)
e.expl("言葉を並べて、正しい文を作ってください。")
e.ex("B1", "sentence building", "行列は12時に出発します。", "Subject + time + verb",
     "行列は / 12時に / 出発します → ___", instr="Build a sentence", size=19, gap=6)
e.ex("A2", "sentence building", "私は時代祭を見たいです。", "見たい = want to see",
     "私は / 時代祭を / 見たいです → ___", instr="Build a sentence", size=19, gap=6)
e.ex("B1", "sentence building", "正倉院展は土よう日から始まります。", "It starts on Saturday",
     "正倉院展は / 土よう日から / 始まります → ___", instr="Build a sentence", size=19, gap=6)
e.ex("B1", "sentence building", "馬に乗って矢を射ます。", "The て-form links the two actions",
     "馬に乗って / 矢を / 射ます → ___", instr="Build a sentence", size=19, gap=6)
e.head("D · ペアにしましょう", 25)
e.match_set("B1", "matching",
            ["時代祭", "正倉院展", "流鏑馬神事", "日本シリーズ第1戦"],
            ["横浜 — 土よう日18時30分",
             "京都 — 木よう日",
             "奈良 — 土よう日から",
             "大阪 — 日よう日15時"],
            ["b", "c", "d", "a"],
            ["Jidai Matsuri = Kyoto (b)", "Shosoin = Nara (c)", "Yabusame = Osaka (d)", "Series Game 1 = Yokohama (a)"],
            instr="Match events to places")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-bunka.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · スポーツ (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("スポーツ · 体育", "Lucerna", "レベル B1 · 日本シリーズ詳報 · The Japan Series in depth")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P4-feature")
f.title("2年ぶりの同じ対決 — DeNA対ソフトバンク", 37)
f.byline("Lucerna編集部 · 読むレベル：B1")
f.para("今年の日本シリーズは、2024年と同じ対決です。横浜DeNAベイスターズは、セントラル・リーグの3位でした。クライマックスシリーズで阪神に勝って、日本シリーズに出場します。")
f.para("相手は、福岡ソフトバンクホークスです。ソフトバンクはパシフィック・リーグの優勝チームで、日本ハムに勝ちました。レギュラーシーズンの成績は、91勝49敗3分け、勝率は.650でした。DeNAは71勝69敗3分けでした。")
f.para("2024年は、3位のDeNAが優勝しました。今年はどちらが勝つでしょう。第1戦は24日（土）18時30分、第2戦は25日（日）18時、どちらも横浜スタジアムです。この新聞が届く時、試合はまだ始まっていません。結果は来週の新聞でお知らせします！")
f.gloss("勝率 winning percentage · 分け a draw · 成績 a team's record · 出場します to take part.")
f.head("箱根駅伝の予選会 — 10校が決まる", 25)
f.para("来年1月2日・3日の『第103回箱根駅伝』の予選会が、10月17日（土）、立川でありました。45の大学が出場して、上位10人の合計タイムで、本戦に出る10校が決まりました。")
f.para("1位は東洋大学で、タイムは10時間31分30秒でした。最後の10位は法政大学です。法政大学は、11位の国士舘大学より1分46秒速かったです。年明けの本戦が、今から楽しみです。")
f.para("『箱根駅伝予選会 結果』は、17日のGoogleトレンドでも5万回以上検索されました。予選会は、駅伝シーズンの始まりの合図です。大学生たちは、自分の大学の名前を背負って走ります。お正月の本戦では、たくさんの人が道やテレビで応援します。")
f.gloss("予選会 a qualifier · 合計タイム total time · 本戦 the main race · 背負って carrying on the back.")
f.box("日本シリーズの日程 · Series schedule", [
    ("第1戦 — 10月24日（土）18時30分、横浜スタジアム", "serif", False, INK, 20, 1.35),
    ("第2戦 — 10月25日（日）18時、横浜スタジアム", "serif", False, INK, 20, 1.35),
    ("チケットの一般発売は、22日（木）12時に始まりました", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: waseda image + Ohtani box
ix = COLX[3]
image(p, "waseda1911.jpg", ix, 200, CW, 290)
cy3 = caption(p, ix, 490, CW, "1911年の早稲田大学野球部。日本の野球には、100年以上の歴史があります。",
              "写真：Bain News Service — パブリックドメイン（Wikimedia Commons）")
ot = "Googleトレンド日本（10月17日）のまとめでは、『大谷翔平』の検索は20万回以上でした。大谷選手のホームランと、ドジャースがポストシーズンで敗退したニュースで、検索が増えたそうです。『山本由伸』も2万回以上でした。"
oy = cy3 + 24
oh = 62 + len(wrap(ot, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("※まとめにない結果や点数は、本紙では書きません。", "serif", False, 19.5, CW - 44)) * 27 + 20
p.rect(ix, oy, CW, oh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = oy + 16
p.text(ix + 22, yy3 + 26, "検索でもスター", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, ot, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "※まとめにない結果や点数は、本紙では書きません。", 19.5, "serif", False, GREY, CW - 44, 1.38)
print("P4 col3 ends", oy + oh)

# ---- qualifier table (full width) ----
ty = 1490
p.text(MX, ty + 26, "箱根駅伝・予選会の10校 · The ten schools through the qualifier", 26, "sans", True, OLIVE)
p.hline(MX, RIGHT, ty + 40, GOLD, 2)
schools_l = ["1位 東洋大学 — 10時間31分30秒", "2位 中央学院大学", "3位 東海大学", "4位 専修大学", "5位 東京農業大学"]
schools_r = ["6位 山梨学院大学", "7位 大東文化大学", "8位 神奈川大学", "9位 日本体育大学", "10位 法政大学"]
colw2 = (RIGHT - MX - GUT) // 2
for i, s in enumerate(schools_l):
    p.text(MX, ty + 84 + i * 40, s, 21.5, "serif", False, INK)
for i, s in enumerate(schools_r):
    p.text(MX + colw2 + GUT, ty + 84 + i * 40, s, 21.5, "serif", False, INK)
p.para(MX, ty + 84 + 5 * 40 + 6, "予選会は10月17日（土）、立川でありました。45の大学が出場しました。", 20, "serif", False, GREY, RIGHT - MX, 1.4)

# ---- P4 exercises ----
ey = 1840
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Page 4 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels are mixed — find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · 理解", 25)
e.expl("第4版の文章を読んで、正しい答えを選んでください。")
e.ex("B1", "multiple choice", "B", "This year: DeNA vs SoftBank",
     "今年の日本シリーズの対決は？ A. DeNA対日本ハム · B. DeNA対ソフトバンク · C. 阪神対ソフトバンク", size=19, gap=6)
e.ex("B1", "multiple choice", "B", "DeNA beat Hanshin in the Climax Series",
     "DeNAはクライマックスシリーズでどこに勝ちましたか。 A. 日本ハム · B. 阪神 · C. ソフトバンク", size=19, gap=6)
e.ex("B1", "multiple choice", "A", "SoftBank went 91-49 in the regular season",
     "ソフトバンクのレギュラーシーズンの勝敗は？ A. 91勝49敗 · B. 71勝69敗 · C. 49勝91敗", size=19, gap=6)
e.ex("B1", "multiple choice", "B", "DeNA won the 2024 Series",
     "2024年の日本シリーズで優勝したのは？ A. ソフトバンク · B. DeNA · C. 阪神", size=19, gap=6)
e.ex("B1", "multiple choice", "B", "Game 2: Sun the 25th, 18:00",
     "第2戦はいつですか。 A. 24日（土）18時30分 · B. 25日（日）18時 · C. 22日（木）12時", size=19, gap=6)
e.head("B · 数字", 25)
e.expl("第4版の数字を入れてください。")
e.ex("B1", "fill-in", "91", "SoftBank won 91 games",
     "ソフトバンクは ___ 勝しました。", instr="Fill in", size=19, gap=6)
e.ex("B1", "fill-in", "71", "DeNA won 71 games",
     "DeNAは ___ 勝69敗3分けでした。", instr="Fill in", size=19, gap=6)
e.ex("B1", "fill-in", ".650", "SoftBank's percentage: .650",
     "ソフトバンクの勝率は ___ でした。", instr="Fill in", size=19, gap=6)
e.ex("B1", "fill-in", "10", "Toyo's time: 10h 31m 30s",
     "予選会の1位、東洋大学のタイムは ___ 時間31分30秒でした。", instr="Fill in", size=19, gap=6)
e.ex("B1", "fill-in", "1", "Hosei beat Kokushikan by 1m 46s",
     "法政大学は国士舘大学より ___ 分46秒速かったです。", instr="Fill in", size=19, gap=6)
e.head("C · 駅伝", 25)
e.expl("箱根駅伝の記事から答えてください。")
e.ex("B1", "multiple choice", "B", "The qualifier was in Tachikawa",
     "予選会はどこでありましたか。 A. 箱根 · B. 立川 · C. 横浜", size=19, gap=6)
e.ex("B1", "multiple choice", "B", "45 universities took part",
     "予選会に出た大学は？ A. 10校 · B. 45校 · C. 103校", size=19, gap=6)
e.ex("B1", "multiple choice", "A", "Ten schools reach the main race",
     "本戦に出るのは何校ですか。 A. 10校 · B. 11校 · C. 45校", size=19, gap=6)
e.ex("B1", "multiple choice", "B", "The Hakone Ekiden is on Jan 2-3",
     "箱根駅伝の本戦はいつですか。 A. 12月31日 · B. 1月2日・3日 · C. 2月1日", size=19, gap=6)
e.head("D · 正しい・正しくない", 25)
e.expl("文が正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "true/false", "×", "Game 1 is on Saturday",
     "第1戦は日よう日です。", instr="True or false?", size=19, gap=6)
e.ex("B1", "true/false", "×", "DeNA finished 3rd",
     "DeNAはリーグ1位でした。", instr="True or false?", size=19, gap=6)
e.ex("B1", "true/false", "○", "DeNA won in 2024",
     "2024年はDeNAが優勝しました。", instr="True or false?", size=19, gap=6)
e.ex("B1", "true/false", "○", "45 universities ran the qualifier",
     "予選会には45の大学が出ました。", instr="True or false?", size=19, gap=6)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-supotsu.svg")
print("P4 saved, exercises so far:", len(REG))
