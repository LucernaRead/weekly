# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ja-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 若者・エンタメ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("若者・エンタメ · Jongeren", "Lucerna", "レベル B1 · 11月11日の分かち合い · Delen op 11 november")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P5-feature")
f.title("「1」が4つ並ぶ日、友達と分ける", 37)
f.byline("Lucerna編集部 · 読むレベル：B1")
f.para("11月11日は、ポッキーの日です。細いお菓子を、友達と分け合う日です。1本ずつ、箱から出して、友達に渡します。SNSでは、友達とポッキーの写真を送り合う人もいます。")
f.para("ポッキーの日は、買うだけの日ではありません。だれかと分ける日です。学校や会社で、「はい、どうぞ」と渡す人もいます。細いお菓子が、人と人をつなぎます。")
f.para("友達と分けて、楽しい11月11日にしましょう。")
f.gloss("渡す overhandigen · つなぐ verbinden · 送り合う elkaar sturen.")
f.head("七五三の写真", 25)
f.para("七五三の季節は、写真の季節でもあります。いこーよの調査（10月21日までの回答、七五三の家庭200）では、写真館やフォトスタジオで撮る家庭が74%でした。神社でのご祈祷を受ける家庭は、71%でした。")
f.para("写真は、家族の思い出になります。着物を着た子どもの写真は、大きくなってからも、家族で見ます。")
f.gloss("思い出 een herinnering · 大きくなる opgroeien.")
f.end_report()

# col 3: words + numbers + あなた
ix = COLX[3]
words5 = ["分ける — 友達とお菓子を分けること",
          "渡す — 人に物をあげること",
          "晴れ着 — お祝いの日に着る服"]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in words5) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "11月11日のことば", 24, "sans", True, OLIVE)
yy3 += 52
for t in words5:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
nums5 = ["74% — 写真館で撮る家庭（調査）",
         "71% — 神社でご祈祷を受ける家庭（調査）"]
ny3 = sy3 + sh + 26
nh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in nums5) + 32
p.rect(ix, ny3, CW, nh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ny3 + 16
p.text(ix + 22, yy3 + 26, "七五三の調査の数字", 24, "sans", True, OLIVE)
yy3 += 52
for t in nums5:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
p.para(ix + 22, yy3 + 18, "※数字は、いこーよの調査（10月21日までの回答）によるものです。", 19, "serif", False, GREY, CW - 44, 1.35)
ey3 = ny3 + nh + 26
etvous = "あなたは？ポッキーを、だれに渡したいですか。日本語で2文、書いて、送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Aan wie wil je Pocky geven? Schrijf twee zinnen in het Japans en stuur ze in.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？ · Jouw beurt", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Aan wie wil je Pocky geven? Schrijf twee zinnen in het Japans en stuur ze in.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Oefeningen pagina 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · Niveaus door elkaar — zoek je nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · 理解", 25)
e.bridge("第5版の文章を読んで、正しい答えを選んでください。")
e.ex("B1", "meerkeuze", "A", "Pocky-dag betekent snacks delen met vrienden",
     "ポッキーの日は、どんな日ですか。 A. 友達と分ける日 · B. 一人で食べる日 · C. 買わない日", size=19, gap=6)
e.ex("B1", "meerkeuze", "B", "De dunne snacks verbinden mensen",
     "細いお菓子は、何をしますか。 A. 人を分けます · B. 人と人をつなぎます · C. 人を隠します", size=19, gap=6)
e.ex("B1", "meerkeuze", "B", "74 % van de gezinnen laat foto's maken in een studio, zegt de enquête",
     "調査では、写真館で撮る家庭は何%ですか。 A. 71% · B. 74% · C. 26%", size=19, gap=6)
e.ex("B1", "meerkeuze", "A", "71 % van de gezinnen krijgt een gebed in de schrijn, zegt de enquête",
     "調査では、神社でご祈祷を受ける家庭は何%ですか。 A. 71% · B. 74% · C. 3%", size=19, gap=6)
e.ex("B1", "meerkeuze", "C", "Shichi-Go-San-foto's zijn een familieherinnering",
     "写真は、何になりますか。 A. ゴミ · B. 宿題 · C. 家族の思い出", size=19, gap=6)
e.head("B · 数字", 25)
e.bridge("第5版の数字を入れてください。")
e.ex("B1", "invullen", "11", "Pocky-dag is 11 november",
     "ポッキーの日は11月 ___ 日です。", instr="Vul in", size=19, gap=6)
e.ex("B1", "invullen", "4", "1111 heeft vier enen",
     "「1111」には、「1」が ___ つ並びます。", instr="Vul in", size=19, gap=6)
e.ex("B1", "invullen", "74", "74 % van de gezinnen laat foto's maken in een studio",
     "写真館で撮る家庭は ___ %でした。", instr="Vul in", size=19, gap=6)
e.ex("B1", "invullen", "71", "71 % van de gezinnen krijgt een gebed",
     "神社でご祈祷を受ける家庭は ___ %でした。", instr="Vul in", size=19, gap=6)
e.ex("B1", "invullen", "200", "De enquête omvatte 200 Shichi-Go-San-gezinnen",
     "調査は、七五三の家庭 ___ を対象にしました。", instr="Vul in", size=19, gap=6)
e.head("C · 正しい・正しくない", 25)
e.bridge("正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "waar/onwaar", "×", "Pocky-dag gaat niet alleen om kopen",
     "ポッキーの日は、買うだけの日です。", instr="Waar of onwaar?", size=19, gap=6)
e.ex("B1", "waar/onwaar", "○", "Het gezin bekijkt de foto's nog als de kinderen groot zijn",
     "写真は、大きくなってからも、家族で見ます。", instr="Waar of onwaar?", size=19, gap=6)
e.ex("B1", "waar/onwaar", "×", "Gezinnen die een studio gebruiken: 71 %",
     "写真館で撮る家庭は71%でした。", instr="Waar of onwaar?", size=19, gap=6)
e.ex("B1", "waar/onwaar", "○", "Pocky-dag is 11 november",
     "ポッキーの日は、11月11日です。", instr="Waar of onwaar?", size=19, gap=6)
e.head("D · 文を完成しましょう", 25)
e.bridge("第5版の文を完成してください。")
e.ex("B1", "invullen", "分けます", "分ける = delen",
     "細いお菓子を、友達と ___ 。", instr="Vul in", size=19, gap=6)
e.ex("B1", "invullen", "渡す", "渡す = overhandigen",
     "学校で、「はい、どうぞ」と ___ 人もいます。", instr="Vul in", size=19, gap=6)
e.ex("B1", "invullen", "晴れ着", "晴れ着 = feestkleding",
     "お祝いの日に着る服を「___」と言います。", instr="Vul in", size=19, gap=6)
e.ex("B1", "invullen", "思い出", "思い出 = een herinnering",
     "写真は、家族の ___ になります。", instr="Vul in", size=19, gap=6)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-wakamono.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 深読み (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("深読み · ふかよみ", "Lucerna", "レベル B2 · 紅葉の見頃は南へ · Het bladseizoen gaat naar het zuiden")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P6-feature")
f.title("見頃を追いかけて、南へ", 37)
f.byline("Lucerna編集部 · 読むレベル：B2")
f.para("紅葉の見頃は、北から南へ移ります。ウェザーニューズの10月29日の「第3回紅葉見頃予想」では、東京の高尾山は11月13日ごろから、広島の宮島は11月21日ごろから、京都の嵐山は11月23日ごろから見頃だそうです。")
f.para("同じ発表では、宮城県の鳴子峡は、もう見頃だそうです。11月初めの寒さで、色づきが進みました。その後は、気温が高めの日が多くなります。中旬以降に見頃になる場所は、平年よりやや遅くなる所が多いそうです。")
f.para("日本気象株式会社の9月2日の予想では、東京の紅葉は11月29日ごろ、大阪は12月4日ごろです。どちらも、平年並みの予想です。予報の日にちは、見頃が始まる目安です。いちばん美しい日を表すものではありません。")
f.para("紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。でも、11月は気温の変化が大きい月です。暖かい服と傘の準備も大切です。")
f.gloss("目安 een richtlijn · 色づき verkleuring · 変化 verandering · 準備 voorbereiding.")
f.end_report()

# col 3: facts + words
ix = COLX[3]
facts6 = ["13 — 高尾山は11月13日ごろから見頃",
          "21 — 宮島は11月21日ごろから見頃",
          "23 — 嵐山は11月23日ごろから見頃",
          "29 — 東京の紅葉は11月29日ごろ（日本気象）"]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts6) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "今週の数字", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts6:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
words6 = ["追いかける — 後を追って行くこと",
          "見頃 — いちばん美しい時",
          "落葉 — 木から落ちた葉"]
wy3 = sy3 + sh + 26
wh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in words6) + 32
p.rect(ix, wy3, CW, wh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = wy3 + 16
p.text(ix + 22, yy3 + 26, "紅葉のことば", 24, "sans", True, OLIVE)
yy3 += 52
for t in words6:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", wy3 + wh)

# ---- practice chart (full width) ----
chy = 1500
p.text(MX, chy + 26, "グラフを読もう · De grafiek lezen", 26, "sans", True, OLIVE)
p.text(RIGHT, chy + 26, "練習用データ · Oefendata", 21, "sans", True, BRICK, anchor="end")
p.hline(MX, RIGHT, chy + 40, GOLD, 2)
p.text(MX, chy + 78, "秋の休みに、どこへ行きたいですか（練習用データ — 実際の調査ではありません）", 22, "serif", True, INK)
chart = [("山", 34), ("神社", 26), ("公園", 24), ("町", 16)]
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
p.text(MX, ey + 28, "練習 · Oefeningen pagina 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · Niveaus door elkaar — zoek je nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · 理解", 25)
e.bridge("第6版の文章を読んで、正しい答えを選んでください。")
e.ex("B2", "meerkeuze", "B", "De bladeren van de berg Takao pieken vanaf ongeveer 13 november (vrijdag)",
     "高尾山の見頃はいつごろからですか。 A. 11月9日 · B. 11月13日ごろ · C. 12月4日", size=19, gap=6)
e.ex("B2", "meerkeuze", "B", "De bladeren op Miyajima pieken vanaf ongeveer 21 november (zaterdag)",
     "宮島の見頃はいつごろからですか。 A. 11月13日 · B. 11月21日ごろ · C. 11月29日", size=19, gap=6)
e.ex("B2", "meerkeuze", "B", "De Naruko-kloof is al op zijn best",
     "鳴子峡は、どうですか。 A. まだ色づいていません · B. もう見頃です · C. 12月に見頃です", size=19, gap=6)
e.ex("B2", "meerkeuze", "A", "Plekken die na half november pieken, zijn meestal later dan gemiddeld",
     "中旬以降に見頃になる場所は、どうですか。 A. 平年よりやや遅い所が多い · B. 平年より早い所が多い · C. 平年と同じです", size=19, gap=6)
e.ex("B2", "meerkeuze", "B", "Voorspelde data markeren het begin van de beste tijd",
     "予報の日にちは、何ですか。 A. いちばん美しい日 · B. 見頃が始まる目安 · C. 落葉の日", size=19, gap=6)
e.head("B · グラフ", 25)
e.bridge("練習用データのグラフを見て答えてください。")
e.ex("B2", "invullen", "山", "Bergen staan bovenaan de grafiek",
     "「行きたい場所」で1位は ___ です。", instr="Vul in", size=19, gap=6)
e.ex("B2", "invullen", "34", "Bergen: 34 %",
     "山と答えた人は ___ %です。", instr="Vul in", size=19, gap=6)
e.ex("B2", "invullen", "26", "Schrijnen: 26 %",
     "神社は ___ %です。", instr="Vul in", size=19, gap=6)
e.ex("B2", "invullen", "8", "Bergen 34 % min heiligdommen 26 % is 8",
     "山と神社の差は ___ %です。", instr="Vul in", size=19, gap=6)
e.ex("B2", "invullen", "60", "34 + 26 = 60",
     "山と神社を合わせると ___ %です。", instr="Vul in", size=19, gap=6)
e.ex("B2", "invullen", "100", "De vier samen zijn 100 %",
     "4つの数字を全部足すと ___ %になります。", instr="Vul in", size=19, gap=6)
e.head("C · 数字と事実", 25)
e.bridge("第6版の数字を入れてください。")
e.ex("B2", "invullen", "23", "De bladeren in Arashiyama pieken vanaf ongeveer 23 november (maandag)",
     "嵐山は11月 ___ 日ごろから見頃です。", instr="Vul in", size=19, gap=6)
e.ex("B2", "invullen", "29", "De bladeren in Tokio pieken rond 29 november (zondag)",
     "東京の紅葉は11月 ___ 日ごろです。", instr="Vul in", size=19, gap=6)
e.ex("B2", "invullen", "4", "De bladeren in Osaka pieken rond 4 december (vrijdag)",
     "大阪の紅葉は12月 ___ 日ごろです。", instr="Vul in", size=19, gap=6)
e.ex("B2", "invullen", "29", "De voorspelling van Weathernews was van 29 oktober (donderdag)",
     "ウェザーニューズの予報は10月 ___ 日でした。", instr="Vul in", size=19, gap=6)
e.head("D · 正しい・正しくない", 25)
e.bridge("正しければ○、正しくなければ×を書いてください。")
e.ex("B2", "waar/onwaar", "×", "Dat het bladseizoen van zuid naar noord gaat, is fout",
     "紅葉の見頃は、南から北へ移ります。", instr="Waar of onwaar?", size=19, gap=6)
e.ex("B2", "waar/onwaar", "○", "De Naruko-kloof is al op zijn best",
     "鳴子峡は、もう見頃です。", instr="Waar of onwaar?", size=19, gap=6)
e.ex("B2", "waar/onwaar", "×", "De grafiek toont echte enquêteresultaten",
     "グラフの数字は、本当の調査の結果です。", instr="Waar of onwaar?", size=19, gap=6)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-fukayomi.svg")
print("P6 saved, exercises so far:", len(REG))
