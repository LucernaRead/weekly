# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ja-proofread-gates/baseline-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 若者・エンタメ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("若者・エンタメ · 青年", "Lucerna", "レベル B1 · 11月11日の分かち合い · 11月11日的分享")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P5-feature")
f.title("「1」が4つ並ぶ日、友達と分ける", 37)
f.byline("Lucerna編集部 · 読むレベル：B1")
f.para("11月11日は、ポッキーの日です。細いお菓子を、友達と分け合う日です。1本ずつ、箱から出して、友達に渡します。SNSでは、友達とポッキーの写真を送り合う人もいます。")
f.para("ポッキーの日は、買うだけの日ではありません。だれかと分ける日です。学校や会社で、「はい、どうぞ」と渡す人もいます。細いお菓子が、人と人をつなぎます。")
f.para("友達と分けて、楽しい11月11日にしましょう。")
f.gloss("渡す 递给 · つなぐ 连接 · 送り合う 互相发送。")
f.head("七五三の写真", 25)
f.para("七五三の季節は、写真の季節でもあります。いこーよの調査（10月21日までの回答、七五三の家庭200）では、写真館やフォトスタジオで撮る家庭が74%でした。神社でのご祈祷を受ける家庭は、71%でした。")
f.para("写真は、家族の思い出になります。着物を着た子どもの写真は、大きくなってからも、家族で見ます。")
f.gloss("思い出 回忆 · 大きくなる 长大。")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你呢？想把波奇递给谁？写两句日语寄来。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？ · 说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你呢？想把波奇递给谁？写两句日语寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · 第 5 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · 理解", 25)
e.bridge("第5版の文章を読んで、正しい答えを選んでください。")
e.ex("B1", "单选", "A", "波奇日要和朋友分享零食",
     "ポッキーの日は、どんな日ですか。 A. 友達と分ける日 · B. 一人で食べる日 · C. 買わない日", size=19, gap=6)
e.ex("B1", "单选", "B", "细长的零食把人与人连接起来",
     "細いお菓子は、何をしますか。 A. 人を分けます · B. 人と人をつなぎます · C. 人を隠します", size=19, gap=6)
e.ex("B1", "单选", "B", "调查显示74%的家庭在照相馆拍照",
     "調査では、写真館で撮る家庭は何%ですか。 A. 71% · B. 74% · C. 26%", size=19, gap=6)
e.ex("B1", "单选", "A", "调查显示71%的家庭在神社接受祈祷",
     "調査では、神社でご祈祷を受ける家庭は何%ですか。 A. 71% · B. 74% · C. 3%", size=19, gap=6)
e.ex("B1", "单选", "C", "七五三的照片是全家的回忆",
     "写真は、何になりますか。 A. ゴミ · B. 宿題 · C. 家族の思い出", size=19, gap=6)
e.head("B · 数字", 25)
e.bridge("第5版の数字を入れてください。")
e.ex("B1", "完成句子", "11", "波奇日在11月11日",
     "ポッキーの日は11月 ___ 日です。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "4", "1111中有4个1",
     "「1111」には、「1」が ___ つ並びます。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "74", "74%的家庭在照相馆拍照",
     "写真館で撮る家庭は ___ %でした。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "71", "71%的家庭接受祈祷",
     "神社でご祈祷を受ける家庭は ___ %でした。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "200", "调查对象是200个七五三家庭",
     "調査は、七五三の家庭 ___ を対象にしました。", instr="填空", size=19, gap=6)
e.head("C · 正しい・正しくない", 25)
e.bridge("正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "判断对错", "×", "波奇日只买不分享是错的",
     "ポッキーの日は、買うだけの日です。", instr="判断", size=19, gap=6)
e.ex("B1", "判断对错", "○", "照片长大后家人还会一起看",
     "写真は、大きくなってからも、家族で見ます。", instr="判断", size=19, gap=6)
e.ex("B1", "判断对错", "×", "照相馆拍照的家庭是71%",
     "写真館で撮る家庭は71%でした。", instr="判断", size=19, gap=6)
e.ex("B1", "判断对错", "○", "波奇日是11月11日",
     "ポッキーの日は、11月11日です。", instr="判断", size=19, gap=6)
e.head("D · 文を完成しましょう", 25)
e.bridge("第5版の文を完成してください。")
e.ex("B1", "完成句子", "分けます", "分ける＝分享",
     "細いお菓子を、友達と ___ 。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "渡す", "渡す＝递给",
     "学校で、「はい、どうぞ」と ___ 人もいます。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "晴れ着", "晴れ着＝庆祝日穿的衣服",
     "お祝いの日に着る服を「___」と言います。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "思い出", "思い出＝回忆",
     "写真は、家族の ___ になります。", instr="填空", size=19, gap=6)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-wakamono.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 深読み (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("深読み · ふかよみ", "Lucerna", "レベル B2 · 紅葉の見頃は南へ · 红叶最佳观赏期向南移动")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P6-feature")
f.title("見頃を追いかけて、南へ", 37)
f.byline("Lucerna編集部 · 読むレベル：B2")
f.para("紅葉の見頃は、北から南へ移ります。ウェザーニューズの10月29日の「第3回紅葉見頃予想」では、東京の高尾山は11月13日ごろから、広島の宮島は11月21日ごろから、京都の嵐山は11月23日ごろから見頃だそうです。")
f.para("同じ発表では、宮城県の鳴子峡は、もう見頃だそうです。11月初めの寒さで、色づきが進みました。その後は、気温が高めの日が多くなります。中旬以降に見頃になる場所は、平年よりやや遅くなる所が多いそうです。")
f.para("日本気象株式会社の9月2日の予想では、東京の紅葉は11月29日ごろ、大阪は12月4日ごろです。どちらも、平年並みの予想です。予報の日にちは、見頃が始まる目安です。いちばん美しい日を表すものではありません。")
f.para("紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。でも、11月は気温の変化が大きい月です。暖かい服と傘の準備も大切です。")
f.gloss("目安 标准 · 色づき 变色 · 変化 变化 · 準備 准备。")
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
p.text(MX, chy + 26, "グラフを読もう · 读图表", 26, "sans", True, OLIVE)
p.text(RIGHT, chy + 26, "練習用データ · 练习数据", 21, "sans", True, BRICK, anchor="end")
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
p.text(MX, ey + 28, "練習 · 第 6 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · 理解", 25)
e.bridge("第6版の文章を読んで、正しい答えを選んでください。")
e.ex("B2", "单选", "B", "高尾山的红叶从11月13日（周五）前后进入见赏期",
     "高尾山の見頃はいつごろからですか。 A. 11月9日 · B. 11月13日ごろ · C. 12月4日", size=19, gap=6)
e.ex("B2", "单选", "B", "宫岛的红叶从11月21日（周六）前后进入见赏期",
     "宮島の見頃はいつごろからですか。 A. 11月13日 · B. 11月21日ごろ · C. 11月29日", size=19, gap=6)
e.ex("B2", "单选", "B", "鸣子峡已经进入见赏期",
     "鳴子峡は、どうですか。 A. まだ色づいていません · B. もう見頃です · C. 12月に見頃です", size=19, gap=6)
e.ex("B2", "单选", "A", "11月中旬以后进入见赏期的地点多比往年稍晚",
     "中旬以降に見頃になる場所は、どうですか。 A. 平年よりやや遅い所が多い · B. 平年より早い所が多い · C. 平年と同じです", size=19, gap=6)
e.ex("B2", "单选", "B", "预报日期是见赏期开始的参考标准",
     "予報の日にちは、何ですか。 A. いちばん美しい日 · B. 見頃が始まる目安 · C. 落葉の日", size=19, gap=6)
e.head("B · グラフ", 25)
e.bridge("練習用データのグラフを見て答えてください。")
e.ex("B2", "完成句子", "山", "图表中最受欢迎的是山",
     "「行きたい場所」で1位は ___ です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "34", "山占34%",
     "山と答えた人は ___ %です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "26", "神社占26%",
     "神社は ___ %です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "8", "山34%与神社26%之差为8",
     "山と神社の差は ___ %です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "60", "34+26=60",
     "山と神社を合わせると ___ %です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "100", "四项合计100%",
     "4つの数字を全部足すと ___ %になります。", instr="填空", size=19, gap=6)
e.head("C · 数字と事実", 25)
e.bridge("第6版の数字を入れてください。")
e.ex("B2", "完成句子", "23", "岚山的红叶从11月23日（周一）前后进入见赏期",
     "嵐山は11月 ___ 日ごろから見頃です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "29", "东京的红叶在11月29日（周日）前后",
     "東京の紅葉は11月 ___ 日ごろです。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "4", "大阪的红叶在12月4日（周五）前后",
     "大阪の紅葉は12月 ___ 日ごろです。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "29", "Weathernews的预报在10月29日（周四）",
     "ウェザーニューズの予報は10月 ___ 日でした。", instr="填空", size=19, gap=6)
e.head("D · 正しい・正しくない", 25)
e.bridge("正しければ○、正しくなければ×を書いてください。")
e.ex("B2", "判断对错", "×", "红叶见赏期从南向北移动是错的",
     "紅葉の見頃は、南から北へ移ります。", instr="判断", size=19, gap=6)
e.ex("B2", "判断对错", "○", "鸣子峡已经进入见赏期",
     "鳴子峡は、もう見頃です。", instr="判断", size=19, gap=6)
e.ex("B2", "判断对错", "×", "图表是真实调查结果",
     "グラフの数字は、本当の調査の結果です。", instr="判断", size=19, gap=6)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-fukayomi.svg")
print("P6 saved, exercises so far:", len(REG))
