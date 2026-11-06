# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ja-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 若者・エンタメ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("若者・エンタメ · 青年", "Lucerna", "レベル B1 · 11月11日の分かち合い · 11月11日的分享", face="TC", sub_face="TC")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P5-feature")
f.title("「1」が4つ並ぶ日、友達と分ける", 37)
f.byline("Lucerna編集部 · 読むレベル：B1")
f.para("11月11日は、ポッキーの日です。細いお菓子を、友達と分け合う日です。1本ずつ、箱から出して、友達に渡します。SNSでは、友達とポッキーの写真を送り合う人もいます。")
f.para("ポッキーの日は、買うだけの日ではありません。だれかと分ける日です。学校や会社で、「はい、どうぞ」と渡す人もいます。細いお菓子が、人と人をつなぎます。")
f.para("友達と分けて、楽しい11月11日にしましょう。")
f.gloss("渡す 遞給 · つなぐ 連接 · 送り合う 互相發送。")
f.head("七五三の写真", 25)
f.para("七五三の季節は、写真の季節でもあります。いこーよの調査（10月21日までの回答、七五三の家庭200）では、写真館やフォトスタジオで撮る家庭が74%でした。神社でのご祈祷を受ける家庭は、71%でした。")
f.para("写真は、家族の思い出になります。着物を着た子どもの写真は、大きくなってからも、家族で見ます。")
f.gloss("思い出 回憶 · 大きくなる 長大。")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你呢？想把波奇遞給誰？寫兩句日語寄來。", "sans", False, 20, CW - 44, face="TC")) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？ · 說說你自己", 24, "sans", True, OLIVE, face="TC")
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你呢？想把波奇遞給誰？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42, face="TC")
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · 第 5 版練習", 28, "sans", True, OLIVE, face="TC")
p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end", face="TC")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · 理解", 25)
e.expl("第5版の文章を読んで、正しい答えを選んでください。")
e.ex("B1", "單選", "A", "波奇日要和朋友分享零食",
     "ポッキーの日は、どんな日ですか。 A. 友達と分ける日 · B. 一人で食べる日 · C. 買わない日", size=19, gap=6)
e.ex("B1", "單選", "B", "細長的零食把人與人連接起來",
     "細いお菓子は、何をしますか。 A. 人を分けます · B. 人と人をつなぎます · C. 人を隠します", size=19, gap=6)
e.ex("B1", "單選", "B", "調查顯示74%的家庭在照相館拍照",
     "調査では、写真館で撮る家庭は何%ですか。 A. 71% · B. 74% · C. 26%", size=19, gap=6)
e.ex("B1", "單選", "A", "調查顯示71%的家庭在神社接受祈禱",
     "調査では、神社でご祈祷を受ける家庭は何%ですか。 A. 71% · B. 74% · C. 3%", size=19, gap=6)
e.ex("B1", "單選", "C", "七五三的照片是全家的回憶",
     "写真は、何になりますか。 A. ゴミ · B. 宿題 · C. 家族の思い出", size=19, gap=6)
e.head("B · 数字", 25)
e.expl("第5版の数字を入れてください。")
e.ex("B1", "完成句子", "11", "波奇日在11月11日",
     "ポッキーの日は11月 ___ 日です。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "4", "1111中有4個1",
     "「1111」には、「1」が ___ つ並びます。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "74", "74%的家庭在照相館拍照",
     "写真館で撮る家庭は ___ %でした。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "71", "71%的家庭接受祈禱",
     "神社でご祈祷を受ける家庭は ___ %でした。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "200", "調查對象是200個七五三家庭",
     "調査は、七五三の家庭 ___ を対象にしました。", instr="填空", size=19, gap=6)
e.head("C · 正しい・正しくない", 25)
e.expl("正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "判斷對錯", "×", "波奇日只買不分享是錯的",
     "ポッキーの日は、買うだけの日です。", instr="判斷", size=19, gap=6)
e.ex("B1", "判斷對錯", "○", "照片長大後家人還會一起看",
     "写真は、大きくなってからも、家族で見ます。", instr="判斷", size=19, gap=6)
e.ex("B1", "判斷對錯", "×", "照相館拍照的家庭是71%",
     "写真館で撮る家庭は71%でした。", instr="判斷", size=19, gap=6)
e.ex("B1", "判斷對錯", "○", "波奇日是11月11日",
     "ポッキーの日は、11月11日です。", instr="判斷", size=19, gap=6)
e.head("D · 文を完成しましょう", 25)
e.expl("第5版の文を完成してください。")
e.ex("B1", "完成句子", "分けます", "分ける＝分享",
     "細いお菓子を、友達と ___ 。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "渡す", "渡す＝遞給",
     "学校で、「はい、どうぞ」と ___ 人もいます。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "晴れ着", "晴れ着＝慶祝日穿的衣服",
     "お祝いの日に着る服を「___」と言います。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "思い出", "思い出＝回憶",
     "写真は、家族の ___ になります。", instr="填空", size=19, gap=6)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-wakamono.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 深読み (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("深読み · ふかよみ", "Lucerna", "レベル B2 · 紅葉の見頃は南へ · 紅葉最佳觀賞期向南移動", sub_face="TC")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P6-feature")
f.title("見頃を追いかけて、南へ", 37)
f.byline("Lucerna編集部 · 読むレベル：B2")
f.para("紅葉の見頃は、北から南へ移ります。ウェザーニューズの10月29日の「第3回紅葉見頃予想」では、東京の高尾山は11月13日ごろから、広島の宮島は11月21日ごろから、京都の嵐山は11月23日ごろから見頃だそうです。")
f.para("同じ発表では、宮城県の鳴子峡は、もう見頃だそうです。11月初めの寒さで、色づきが進みました。その後は、気温が高めの日が多くなります。中旬以降に見頃になる場所は、平年よりやや遅くなる所が多いそうです。")
f.para("日本気象株式会社の9月2日の予想では、東京の紅葉は11月29日ごろ、大阪は12月4日ごろです。どちらも、平年並みの予想です。予報の日にちは、見頃が始まる目安です。いちばん美しい日を表すものではありません。")
f.para("紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。でも、11月は気温の変化が大きい月です。暖かい服と傘の準備も大切です。")
f.gloss("目安 標準 · 色づき 變色 · 変化 變化 · 準備 準備。")
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
p.text(MX, chy + 26, "グラフを読もう · 讀圖表", 26, "sans", True, OLIVE, face="TC")
p.text(RIGHT, chy + 26, "練習用データ · 練習數據", 21, "sans", True, BRICK, anchor="end", face="TC")
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
p.text(MX, ey + 28, "練習 · 第 6 版練習", 28, "sans", True, OLIVE, face="TC")
p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end", face="TC")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · 理解", 25)
e.expl("第6版の文章を読んで、正しい答えを選んでください。")
e.ex("B2", "單選", "B", "高尾山的紅葉從11月13日（週五）前後進入見賞期",
     "高尾山の見頃はいつごろからですか。 A. 11月9日 · B. 11月13日ごろ · C. 12月4日", size=19, gap=6)
e.ex("B2", "單選", "B", "宮島的紅葉從11月21日（週六）前後進入見賞期",
     "宮島の見頃はいつごろからですか。 A. 11月13日 · B. 11月21日ごろ · C. 11月29日", size=19, gap=6)
e.ex("B2", "單選", "B", "鳴子峽已經進入見賞期",
     "鳴子峡は、どうですか。 A. まだ色づいていません · B. もう見頃です · C. 12月に見頃です", size=19, gap=6)
e.ex("B2", "單選", "A", "11月中旬以後進入見賞期的地點多比往年稍晚",
     "中旬以降に見頃になる場所は、どうですか。 A. 平年よりやや遅い所が多い · B. 平年より早い所が多い · C. 平年と同じです", size=19, gap=6)
e.ex("B2", "單選", "B", "預報日期是見賞期開始的參考標準",
     "予報の日にちは、何ですか。 A. いちばん美しい日 · B. 見頃が始まる目安 · C. 落葉の日", size=19, gap=6)
e.head("B · グラフ", 25)
e.expl("練習用データのグラフを見て答えてください。")
e.ex("B2", "完成句子", "山", "圖表中最受歡迎的是山",
     "「行きたい場所」で1位は ___ です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "34", "山佔34%",
     "山と答えた人は ___ %です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "26", "神社佔26%",
     "神社は ___ %です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "8", "山34%與神社26%之差為8",
     "山と神社の差は ___ %です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "60", "34+26=60",
     "山と神社を合わせると ___ %です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "100", "四項合計100%",
     "4つの数字を全部足すと ___ %になります。", instr="填空", size=19, gap=6)
e.head("C · 数字と事実", 25)
e.expl("第6版の数字を入れてください。")
e.ex("B2", "完成句子", "23", "嵐山的紅葉從11月23日（週一）前後進入見賞期",
     "嵐山は11月 ___ 日ごろから見頃です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "29", "東京的紅葉在11月29日（週日）前後",
     "東京の紅葉は11月 ___ 日ごろです。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "4", "大阪的紅葉在12月4日（週五）前後",
     "大阪の紅葉は12月 ___ 日ごろです。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "29", "Weathernews的預報在10月29日（週四）",
     "ウェザーニューズの予報は10月 ___ 日でした。", instr="填空", size=19, gap=6)
e.head("D · 正しい・正しくない", 25)
e.expl("正しければ○、正しくなければ×を書いてください。")
e.ex("B2", "判斷對錯", "×", "紅葉見賞期從南向北移動是錯的",
     "紅葉の見頃は、南から北へ移ります。", instr="判斷", size=19, gap=6)
e.ex("B2", "判斷對錯", "○", "鳴子峽已經進入見賞期",
     "鳴子峡は、もう見頃です。", instr="判斷", size=19, gap=6)
e.ex("B2", "判斷對錯", "×", "圖表是真實調查結果",
     "グラフの数字は、本当の調査の結果です。", instr="判斷", size=19, gap=6)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-fukayomi.svg")
print("P6 saved, exercises so far:", len(REG))
