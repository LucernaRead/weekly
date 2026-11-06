# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 头版 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1 · 第 1 号", 23, "sans", True, OLIVE)
p.text(975, 92, "每周读中文 · 本物の中国語を、毎週読もう", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "2026年10月19日（周一）— 25日（周日）", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "简体中文版 · VOL.1 · 双11 · 大闸蟹 · 霜降", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "给学中文的人的周报 — 本物の中国を、中国語で読む", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)
# pairing badge: which text, which explanation language, which reader
p.text(975, 434, "中国語（簡体字）テキスト · 日本語の解説 — 日本語読者のための版", 19.5, "sans", True, BRICK, anchor="middle")

# band
p.rect(MX, 458, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 512, "双11到了「付尾款周」!周二晚 8 点,天猫付尾款", 36, "sans", True, "#f3edda")
p.text(MX + 30, 556, "京东已经开卖;现货一直卖到 11 月 13 日,这一周就能买。", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 512, "付尾款周", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 556, "残金支払いウィーク · 大事な日時は2ページ", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "头条 · トップ記事", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "双11到了「付尾款」的这一周", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "周二 20:00,天猫付尾款、现货开售——今年的购物季来得更早,也更长", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "Lucerna 編集部 · 読解レベル A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("今年的双11来得早。京东10月12日晚上8点就开始卖现货,10月20日晚上8点还有「开门红」。", size=24)
f.para("淘宝和天猫10月15日晚上8点开始预售。预售,就是先付一点定金,把看好的东西先订下来。", size=24)
f.para("10月20日晚上8点,是今年双11最重要的时间:大家付尾款,现货也同时开售。付完尾款,快递就开始送货了。", size=24)
f.para("现货会一直卖到11月13日。所以这一周,不用等11月11日,双11已经开始了。", size=24)
f.para("这一周,手机上最常见的话是:定金、尾款、满减、凑单、红包口令。第2版有双11日历和买东西的办法。", size=24)
f.para("这是《Lucerna》简体中文版第1号。每周,我们用简单的中文,带你读真正的中国新闻。欢迎你!", size=24)
f.gloss("yùshòu 预售 — 予約販売：売り出す日より前に注文すること · dìngjīn 定金 — 手付金 · wěikuǎn 尾款 — 残金、あとで払う分 · xiànhuò 现货 — 在庫品、すぐ送れる商品。")
f.box("数字看本周 · 数字で見る今週", [
    ("10月20日 20:00 — 天猫で残金の支払い開始；現物販売もスタート", "serif", False, INK, 20, 1.35),
    ("11月13日 — 現物販売期間の最終日", "serif", False, INK, 20, 1.35),
    ("10月15日 — 淘宝と天猫の予約販売が始まった日", "serif", False, INK, 20, 1.35),
    ("8位 — 「大闸蟹价格」がホット検索スナップショットで入った順位（右の欄）", "serif", False, INK, 20, 1.35),
])
f.head("即学即练 · すぐ練習", 25)
f.ex("A2", "完成句子", "12", "京東（JD.com）は10月12日に現物販売を開始。",
     "京东10月___日开始卖现货。", instr="空所補充", size=19.5, gap=6)
f.ex("A2", "完成句子", "10", "天猫の予約販売は10月に開始。",
     "天猫预售___月15日开始。", instr="空所補充", size=19.5, gap=6)
f.ex("A2", "完成句子", "8", "残金の支払いは夜8時に開始。",
     "付尾款的时间是10月20日晚上___点。", instr="空所補充", size=19.5, gap=6)
f.ex("A2", "完成句子", "定金", "予約販売では、まず手付金を払う。",
     "预售的时候先付___。", instr="空所補充", size=19.5, gap=6)
f.ex("A2", "完成句子", "13", "現物販売は11月13日まで。",
     "现货一直卖到11月___日。", instr="空所補充", size=19.5, gap=6)
f.ex("A2", "完成句子", "尾款", "残金を払うと、配送が始まる。",
     "付完___,快递就开始送货了。", instr="空所補充", size=19.5, gap=6)
f.end_report()

# ---- search heat box (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "本周热搜 · 今週のホット検索", 25, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "大家在搜什么 · みんなの検索", 22, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "微博ホット検索ミラーのスナップショット", 19, "sans", False, GREY)
topics = [
    "大闸蟹价格争议 — 第 8 位",
    "NBA 新赛季 — 第 9 位(热度约 34.9 万)",
    "中国体操男队世锦赛铜牌 — 第 19 位",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 10
p.para(gx + 22, byy + 12, "順位と熱度の数字は、10月21日00:30に取得した第三者のミラー・スナップショットによるものです。数字はおおよその目安として見てください。三つの話題はすべて今号で取り上げています。", 18.5, "sans", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 636, "出典：微博ホット検索ミラー（rddh.cn）", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "スナップショット：2026-10-21 00:30", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "本期目录 · 目次", 24, "sans", True, OLIVE)
som = [
    ("2版", "双11日历与本周生活", "A2"),
    ("3版", "重阳刚过,霜降要来", "A2→B1"),
    ("4版", "体操摘铜,NBA 开赛", "B1"),
    ("5版", "电竞 S16 与维密秀", "B1"),
    ("6版", "大闸蟹「价格崩盘」是真的吗", "B2"),
    ("7版", "词语精讲", "A2→B2"),
    ("8版", "测验与答案", "全部"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

# ---- word of the week (col 3) ----
my = 1636
p.text(gx, my + 24, "本周词 · 今週の言葉", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
p.para(gx, my + 76, "「尾款」 wěikuǎn — 残金：代金の最後に払う部分。先付定金，后付尾款（まず手付金、次に残金）。例：「尾款付完，快递就来了。」", 21.5, "serif", False, INK, gw, 1.4)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "locker.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "快递柜(资料图)。付完尾款,这一周,包裹会陆续送到你手里。",
        "Photo: Map hobby — CC0 (Wikimedia Commons)")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-week")
f2.head("忙碌的一周", 25)
f2.para("这一周又买东西,又过节气:周五是霜降,秋天快要过完了。周六凌晨还有电竞比赛。先看好日历,再安排周末吧。", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "快讯 · 速報", 24, "sans", True, OLIVE)
brefs = [
    ("霜降", "周五霜降:吃柿子,加衣服,看红叶。(第 3 版)"),
    ("体操", "中国体操男队在世锦赛拿到铜牌。(第 4 版)"),
    ("S16", "周六凌晨 1 点,S16 瑞士轮开打。(第 5 版)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "闪电问答 · クイッククイズ", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "1ページを読んで選ぼう · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "单选", "A", "残金の支払いは10月20日に開始。",
      "天猫付尾款是哪一天? A. 10月20日 · B. 11月11日 · C. 10月15日", size=21)
qf.ex("A2", "单选", "B", "予約販売では、まず手付金を払う。",
      "预售的时候先付什么? A. 尾款 · B. 定金 · C. 快递费", size=21)
qf.ex("A2", "单选", "C", "カニの話題はスナップショットで8位。",
      "「大闸蟹价格」在热搜快照里是第几位? A. 第 9 位 · B. 第 19 位 · C. 第 8 位", size=21)
qf.ex("A2", "单选", "A", "現物販売は11月13日まで。",
      "现货一直卖到哪一天? A. 11月13日 · B. 11月11日 · C. 10月31日", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-touiban.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 生活 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("生活 · 暮らし", "Lucerna", "レベル A2 · 双11日历 · 霜降生活 · カレンダーと晩秋の暮らし")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("双11日历:哪天付钱,哪天收货", 37)
f.byline("Lucerna 編集部 · 読解レベル A2")
f.para("双11不是一天,是一段时间。今年从10月中旬就开始了。先记住三个日子:10月15日、10月20日、11月13日。")
f.para("10月15日晚上8点,淘宝、天猫开始预售。预售时先付定金,把喜欢的东西订下来。定金不多,但付了定金,就要记得付尾款。")
f.para("10月20日晚上8点付尾款。尾款就是总价减去定金。付完尾款,商家就发货。京东10月20日晚上8点还有「开门红」,很多现货直接开卖。")
f.para("从10月20日到11月13日是现货期。不想等预售的人,可以在这段时间直接买。这一周包裹很多,收货可能比平时慢一点。")
f.gloss("zǒngjià 总价 — 合計金額 · fāhuò 发货 — 商品を送ること · shāngjiā 商家 — 売り手、お店。")
f.head("满减怎么玩 · 满减の仕組み", 25)
f.para("お店ではよく「满300减50」（300元買うと50元引き）のようなキャンペーンがあります。これが mǎnjiǎn 满减、つまり「買って値引き」です。かごの中身が300元に足りなければ、小さな物を一つ足して金額をそろえます：これが còudān 凑单です。下の例は練習用の数字を使っています。")
f.box("练习例子 · 練習の例", [
    ("一件外套 260 元,一条围巾 60 元,一起 320 元。", "serif", False, INK, 20, 1.35),
    ("满 300 减 50,实付 270 元。先付定金 30 元,尾款是 270 − 30 = 240 元。", "serif", False, INK, 20, 1.35),
])
f.head("周五霜降:秋天的最后一个节气", 25)
f.para("10月23日,星期五,是霜降。霜降是二十四节气里的第十八个,也是秋天的最后一个节气。霜降以后,11月7日就是立冬,冬天要来了。")
f.para("霜降的时候,早上的草地上会有白白的霜。天气一天比一天冷,要记得加衣服。老话说:「补冬不如补霜降。」霜降时吃得好一点,冬天身体才好。")
f.para("霜降吃柿子。还有一句话:「霜降吃柿子,嘴唇不会裂。」这个周末,去看看红叶、吃一个柿子,就是很好的安排。")
f.gloss("jiéqì 节气 — 一年を分ける24の節気 · shuāng 霜 — 霜 · lìdōng 立冬 — 冬の始まり（11月7日）。")
f.box("本周生活小日历 · 今週の日付", [
    ("周二 20:00 — 天猫付尾款,京东「开门红」", "serif", False, INK, 20, 1.35),
    ("周五 — 霜降:吃柿子,赏红叶,加衣服", "serif", False, INK, 20, 1.35),
    ("周六 01:00 — S16 瑞士轮开打(第 5 版)", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: valley image + facts + 你呢 (sequential, measured)
ix = COLX[3]
image(p, "valley.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "秋天的山谷,红叶正当时。霜降前后,是看红叶的好时候。",
              "Photo: Paul Gilmore — CC0 (Wikimedia Commons)")
facts = ["霜降是二十四节气里的第 18 个。",
         "霜降以后是立冬,今年在 11 月 7 日。",
         "上周日(10 月 18 日)是重阳节,故事在第 3 版。"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "你知道吗 · 知ってた？", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "你呢?你住的地方,霜降的时候冷不冷?这个双11,你想买什么?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("あなたは？あなたの住む所は、霜降のころ寒いですか？この双11で何を買いたいですか？中国語で2文書いて送ってください。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "あなたは？あなたの住む所は、霜降のころ寒いですか？この双11で何を買いたいですか？中国語で2文書いて送ってください。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- word strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "购物词语卡 · 買い物言葉カード", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "買い物アプリで必ず見る4つの言葉", 20, "sans", False, GREY, anchor="end")
words = [
    ("定金", "dìngjīn · 手付金", "代金の一部、最初に払う分"),
    ("尾款", "wěikuǎn · 残金", "代金の最後に払う分"),
    ("满减", "mǎnjiǎn · 買って値引き", "金額がそろえば値段が下がる"),
    ("红包", "hóngbāo · お年玉袋", "縁起物の赤い封筒に入ったお金"),
]
for i, (t, lab, en) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, en, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 234, "この文を覚えよう：「先付定金，后付尾款，买满三百还能减五十。」", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · 練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · 读一读选一选 · 読んで選ぼう", 25)
e.glossline("2ページを読んで、いちばん良い答えを選ぼう。")
e.ex("A2", "单选", "A", "ショッピング期間の最初の重要日は10月15日。",
     "双11第一个要记的日子是哪天? A. 10月15日 · B. 11月11日 · C. 11月13日", size=19, gap=6)
e.ex("A2", "单选", "B", "予約販売では、まず手付金を払う。",
     "预售的时候先付什么? A. 尾款 · B. 定金 · C. 全款", size=19, gap=6)
e.ex("A2", "单选", "A", "残金を払うと、お店が出荷する。",
     "付完尾款以后,商家做什么? A. 发货 · B. 退定金 · C. 关门", size=19, gap=6)
e.ex("A2", "单选", "B", "霜降は18番目の節気。",
     "霜降是第几个节气? A. 第16个 · B. 第18个 · C. 第24个", size=19, gap=6)
e.ex("A2", "单选", "A", "立冬は霜降の次。",
     "霜降以后是哪个节气? A. 立冬 · B. 冬至 · C. 寒露", size=19, gap=6)
e.head("B · 词语填空 · 単語を入れよう", 25)
e.glossline("正しい言葉を空欄に入れよう。")
e.ex("A2", "完成句子", "定金", "dìngjīn 定金 — 予約販売で払う手付金。",
     "预售时先付___。", instr="空所補充", size=19, gap=6)
e.ex("A2", "完成句子", "尾款", "wěikuǎn 尾款 — 合計から手付金を引いた残金。",
     "总价减去定金,就是___。", instr="空所補充", size=19, gap=6)
e.ex("A2", "完成句子", "满减", "mǎnjiǎn 满减 — 300元買うと50元引き。",
     "买满300元便宜50元,这叫___。", instr="空所補充", size=19, gap=6)
e.ex("A2", "完成句子", "霜", "shuāng 霜 — 草の上の白い霜。",
     "霜降的早上,草地上有白白的___。", instr="空所補充", size=19, gap=6)
e.ex("B1", "完成句子", "节气", "jiéqì 节气 — 霜降は秋最後の節気。",
     "二十四___里,霜降是秋天的最后一个。", instr="空所補充", size=19, gap=6)
e.head("C · 数字与日期 · 数字と日付", 25)
e.glossline("このページの練習の例を使おう。")
e.ex("A2", "完成句子", "260", "例のコートは260元。",
     "练习例子里,外套___元。", instr="空所補充", size=19, gap=6)
e.ex("A2", "完成句子", "320", "260 + 60 = 320元（合計）。",
     "外套和围巾一起___元。", instr="空所補充", size=19, gap=6)
e.ex("B1", "完成句子", "270", "320 − 50 = 270元（値引き後）。",
     "满减以后实付___元。", instr="空所補充", size=19, gap=6)
e.ex("B1", "完成句子", "240", "残金は 270 − 30 = 240元。",
     "练习例子里的尾款是___元。", instr="空所補充", size=19, gap=6)
e.head("D · 词语配对 · ペアにしよう", 25)
e.match_set("A2", "词汇配对",
            ["定金", "尾款", "满减", "节气"],
            ["划分一年的 24 个时间点",
             "先付的一小部分钱",
             "买满多少,便宜多少",
             "最后付的那部分钱"],
            ["b", "d", "c", "a"],
            ["dìngjīn 定金 = 最初に払う、b", "wěikuǎn 尾款 = 最後に払う、d", "mǎnjiǎn 满减 = 買って値引き、c", "jiéqì 节气 = 一年を分ける24の区切り、a"],
            instr="語と意味を結ぶ")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-shenghuo.svg")
print("P2 saved, exercises so far:", len(REG))
