# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/core-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5　若者・エンタメ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("若者・エンタメ　青年", "Lucerna", "レベル B1　流行語30と紅葉の写真　流行语30与红叶照片")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P5-feature")
f.title("今年のことば、30語", 37)
f.byline("Lucerna編集部　読むレベル：B1")
f.para("「新語・流行語大賞」のノミネート30語が、5日（木よう日）に発表されました。今年の世の中を映すことばが、30語選ばれました。トップテンと大賞は、12月1日（火よう日）に発表されます。")
f.para("ノミネートには、『りくりゅう』があります。フィギュアスケートのペア、三浦璃来選手と木原龍一選手のことです。大ヒットした漫画『ちいかわ』も入っています。暑い日を表す『酷暑日』もあります。")
f.para("『好きすぎて滅！』は、M!LKの楽曲の名前です。『ボンボンドロップシール（ボンドロ）』は、シールの名前です。『AI暴走』や『NISA貧乏』など、暮らしを映すことばもあります。")
f.gloss("暮らし 生活　映す 反映　世の中 社会　楽曲 歌曲。")
f.head("紅葉の写真", 25)
f.para("秋は、写真の季節でもあります。京都の嵐山では、23日ごろから紅葉が見頃になります。赤いカエデの写真を、SNSに上げる人も多いです。")
f.para("ことばと写真で、今年の秋を楽しみましょう。あなたの好きな今年のことばは、何ですか。")
f.gloss("上げる 上传　季節 季节。")
f.end_report()

# col 3: arashiyama image + words + numbers + あなた
ix = COLX[3]
image(p, "arashiyama-pond.jpg", ix, 200, CW, 290)
cy3 = caption(p, ix, 490, CW, "京都・嵐山、天龍寺の曹源池。紅葉の見頃は23日ごろからです。",
              "写真：lumoplank — CC0（Wikimedia Commons）")
words5 = ["りくりゅう — 三浦・木原のペア",
          "ちいかわ — 大ヒットした漫画の名前",
          "酷暑日 — とても暑い日のこと"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in words5) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "流行語のことば", 24, "sans", True, OLIVE)
yy3 += 52
for t in words5:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
nums5 = ["30 — ノミネートは30語です",
         "5 — ノミネートの発表は11月5日です",
         "1 — トップテンの発表は12月1日です"]
ny3 = sy3 + sh + 26
nh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in nums5) + 32
p.rect(ix, ny3, CW, nh, fill=BOX)
yy3 = ny3 + 16
p.text(ix + 22, yy3 + 26, "流行語の数字", 24, "sans", True, OLIVE)
yy3 += 52
for t in nums5:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = ny3 + nh + 26
etvous = "あなたは？今年のことば30語の中で、いちばん好きなことばはどれですか。日本語で2文、書いて、送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你呢？今年30个流行语中，最喜欢哪一个？写两句日语寄来。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？　说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你呢？今年30个流行语中，最喜欢哪一个？写两句日语寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "練習　第5版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　理解", 25)
e.bridge("第5版の文章を読んで、正しい答えを選んでください。")
e.ex("B1", "单选", "A", "提名30词发表于11月5日（周四）",
     "ノミネート30語が発表されたのはいつですか。 A. 11月5日　B. 11月19日　C. 12月1日", size=19, gap=6)
e.ex("B1", "单选", "A", "「rikuryuu」是花样滑冰双人组合",
     "りくりゅうは、何ですか。 A. スケートのペア　B. 映画の名前　C. シールの名前", size=19, gap=6)
e.ex("B1", "单选", "A", "「吉伊卡哇」是大热漫画",
     "「ちいかわ」は、何ですか。 A. 大ヒットした漫画　B. 相撲の技　C. お酒の名前", size=19, gap=6)
e.ex("B1", "单选", "C", "前十名与大奖在12月1日发表",
     "トップテンと大賞はいつ発表されますか。 A. 11月5日　B. 11月19日　C. 12月1日", size=19, gap=6)
e.ex("B1", "单选", "B", "岚山见赏期从23日前后开始",
     "嵐山の見頃はいつごろからですか。 A. 19日　B. 23日ごろ　C. 12月1日", size=19, gap=6)
e.head("B　数字", 25)
e.bridge("第5版の数字を入れてください。")
e.ex("B1", "完成句子", "30", "提名共30词",
     "ノミネートは ___ 語です。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "5", "提名在11月5日发表",
     "ノミネートは11月 ___ 日に発表されました。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "1", "前十名在12月1日发表",
     "トップテンは12月 ___ 日に発表されます。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "23", "岚山见赏期从11月23日前后开始",
     "嵐山の見頃は11月 ___ 日ごろからです。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "暑い", "酷暑日＝非常热的日子",
     "『酷暑日』は、とても ___ 日のことです。", instr="填空", size=19, gap=6)
e.head("C　正しい・正しくない", 25)
e.bridge("正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "判断对错", "○", "提名共30个词",
     "ノミネートは30語です。", instr="判断", size=19, gap=6)
e.ex("B1", "判断对错", "×", "前十名还没发表",
     "トップテンは、もう発表されました。", instr="判断", size=19, gap=6)
e.ex("B1", "判断对错", "×", "「rikuryuu」不是电影名",
     "『りくりゅう』は、映画の名前です。", instr="判断", size=19, gap=6)
e.ex("B1", "判断对错", "○", "岚山见赏期从23日前后开始",
     "嵐山の見頃は、23日ごろからです。", instr="判断", size=19, gap=6)
e.head("D　文を完成しましょう", 25)
e.bridge("第5版の文を完成してください。")
e.ex("B1", "完成句子", "選ばれ", "反映今年社会的话语选出了30个",
     "今年の世の中を映すことばが、30語 ___ ました。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "ペア", "「rikuryuu」是三浦璃来与木原龙一的组合",
     "『りくりゅう』は、三浦璃来選手と木原龍一選手の ___ です。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "上げる", "把红色枫叶照片上传到SNS的人很多",
     "赤いカエデの写真を、SNSに ___ 人も多いです。", instr="填空", size=19, gap=6)
e.ex("B1", "完成句子", "発表", "前十名在12月1日发表",
     "トップテンは、12月1日に ___ されます。", instr="填空", size=19, gap=6)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-wakamono.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6　深読み (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("深読み　ふかよみ", "Lucerna", "レベル B2　紅葉は京都へ　红叶移向京都")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P6-feature")
f.title("見頃を追いかけて京都へ", 37)
f.byline("Lucerna編集部　読むレベル：B2")
f.para("紅葉の見頃は、北から南へ、平地へ移っています。ウェザーニューズの10月29日の「第3回紅葉見頃予想」では、東京の高尾山は11月13日ごろ、広島の宮島は11月21日ごろ、京都の嵐山は11月23日ごろから見頃だそうです。")
f.para("嵐山の今の様子は、11月8日の時点で、全体の2割が色づき始めたところだそうです。ウェザーニューズの嵐山のページでは、見頃は11月26日ごろから、落葉はじめは12月12日ごろからと書かれています。")
f.para("日本気象株式会社の9月2日の予想では、東京の紅葉は11月29日ごろ、大阪は12月4日ごろです。どちらも、平年並みの予想です。予報の日にちは、見頃が始まる目安です。")
f.para("ただし、予想は会社によってちがいます。日本気象協会の予想では、嵐山の見頃は11月13日からです。見頃の決め方がちがうからです。日にちだけを見て、決めつけないようにしましょう。")
f.para("紅葉を見に行く人は、予報の日付と今の様子を、両方確かめましょう。京都の11月下旬は、朝晩が冷えます。暖かい服の準備も大切です。")
f.gloss("平地 平地　落葉はじめ 开始落叶　決めつける 断定　確かめる 确认。")
f.end_report()

# col 3: facts + words
ix = COLX[3]
facts6 = ["13 — 高尾山は11月13日ごろから見頃",
          "21 — 宮島は11月21日ごろから見頃",
          "23 — 嵐山は11月23日ごろから見頃",
          "12 — 嵐山の落葉はじめは12月12日ごろ"]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts6) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "今週の数字", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts6:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
words6 = ["追いかける — 後を追って行くこと",
          "見頃 — いちばん美しい時",
          "色づく — 葉の色が変わること"]
wy3 = sy3 + sh + 26
wh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in words6) + 32
p.rect(ix, wy3, CW, wh, fill=BOX)
yy3 = wy3 + 16
p.text(ix + 22, yy3 + 26, "紅葉のことば", 24, "sans", True, OLIVE)
yy3 += 52
for t in words6:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", wy3 + wh)

# ---- practice chart (full width) ----
chy = 1500
p.text(MX, chy + 26, "グラフを読もう　读图表", 26, "sans", True, OLIVE)
p.text(RIGHT, chy + 26, "練習用データ　练习数据", 21, "sans", True, OLIVE, anchor="end")
p.hline(MX, RIGHT, chy + 40, OLIVE, 2)
p.text(MX, chy + 78, "秋の休みに、どこへ行きたいですか（練習用データ — 実際の調査ではありません）", 22, "serif", True, INK)
chart = [("京都", 38), ("浅草", 24), ("高尾山", 22), ("家", 16)]
byy = chy + 104
for name, val in chart:
    p.text(MX, byy + 26, name, 22, "serif", False, INK)
    p.rect(MX + 250, byy, val * 30, 34, fill=OLIVE)
    p.text(MX + 250 + val * 30 + 16, byy + 26, f"{val}%", 22, "sans", True, INK)
    byy += 56
p.para(MX, byy + 22, "このグラフは練習用データです。数字は全部で100%になります。", 19.5, "serif", False, GREY, RIGHT - MX, 1.4)

# ---- P6 exercises ----
ey = 1900
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "練習　第6版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　理解", 25)
e.bridge("第6版の文章を読んで、正しい答えを選んでください。")
e.ex("B2", "单选", "B", "宫岛见赏期从11月21日前后开始",
     "宮島の見頃はいつごろからですか。 A. 11月13日　B. 11月21日ごろ　C. 12月9日", size=19, gap=6)
e.ex("B2", "单选", "B", "到11月8日，岚山两成开始变色",
     "嵐山の今の様子は、11月8日の時点でどうですか。 A. 全体が真っ赤です　B. 2割が色づき始めました　C. もう落葉しています", size=19, gap=6)
e.ex("B2", "单选", "B", "岚山开始落叶在12月12日前后",
     "嵐山の落葉はじめはいつごろからですか。 A. 11月23日　B. 12月12日ごろ　C. 12月4日", size=19, gap=6)
e.ex("B2", "单选", "A", "按日本气象协会预报，岚山见赏期从11月13日开始",
     "日本気象協会の予想では、嵐山の見頃はいつからですか。 A. 11月13日から　B. 11月23日から　C. 12月9日から", size=19, gap=6)
e.ex("B2", "单选", "A", "预报因公司而异是因为见赏期的定义不同",
     "予想が会社によってちがうのは、どうしてですか。 A. 見頃の決め方がちがうから　B. 嵐山が2つあるから　C. 測る機械が壊れたから", size=19, gap=6)
e.head("B　グラフ", 25)
e.bridge("練習用データのグラフを見て答えてください。")
e.ex("B2", "完成句子", "京都", "图表中最想去的是京都",
     "「行きたい場所」で1位は ___ です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "38", "想去京都的人占38%",
     "京都と答えた人は ___ %です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "24", "浅草占24%",
     "浅草は ___ %です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "14", "京都与浅草之差为14%",
     "京都と浅草の差は ___ %です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "62", "38+24=62",
     "京都と浅草を合わせると ___ %です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "100", "四项合计100%",
     "4つの数字を全部足すと ___ %になります。", instr="填空", size=19, gap=6)
e.head("C　数字と事実", 25)
e.bridge("第6版の数字を入れてください。")
e.ex("B2", "完成句子", "13", "高尾山从11月13日前后进入见赏期",
     "高尾山は11月 ___ 日ごろから見頃です。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "29", "东京红叶在11月29日前后",
     "東京の紅葉は11月 ___ 日ごろです。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "4", "大阪红叶在12月4日前后",
     "大阪の紅葉は12月 ___ 日ごろです。", instr="填空", size=19, gap=6)
e.ex("B2", "完成句子", "29", "Weathernews预报在10月29日",
     "ウェザーニューズの予報は10月 ___ 日でした。", instr="填空", size=19, gap=6)
e.head("D　正しい・正しくない", 25)
e.bridge("正しければ○、正しくなければ×を書いてください。")
e.ex("B2", "判断对错", "○", "红叶见赏期从北向南移动",
     "紅葉の見頃は、北から南へ移ります。", instr="判断", size=19, gap=6)
e.ex("B2", "判断对错", "×", "图表是练习数据，不是真实调查",
     "グラフの数字は、本当の調査の結果です。", instr="判断", size=19, gap=6)
e.ex("B2", "判断对错", "×", "各公司对岚山见赏期的预报并不相同",
     "嵐山の見頃の日にちは、どの会社も同じです。", instr="判断", size=19, gap=6)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-fukayomi.svg")
print("P6 saved, exercises so far:", len(REG))
