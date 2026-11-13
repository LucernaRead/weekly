# -*- coding: utf-8 -*-
# W47 zh-tw core, VOL.4: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言　ことば", "Lucerna", "語言聚焦　三個級別　三個主題　三つのレベル、三つのテーマ")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　遊行的話　パレードのことば", 25)
a.para("パレードからは四つの便利な言葉が学べる。遊行（パレード）、封王（優勝を決める）、夜間（夜の）、終點（ゴール）。一度覚えれば、どのパレードも意味が分かる。", 22)
a.expl("パレードの四つの言葉：遊行、封王、夜間、終點。")
a.para("遊行は通りを進む祝いの行進だ。封王は優勝すること。夜間は夜のことで、ナイトパレードは19:00に始まる。終點はパレードの終点、台北ドームだ。", 22)
a.ex("A2", "完成句子", "遊行", "お祝いの行進は遊行だ。",
     "大家走上街頭慶祝，叫___。", instr="穴埋め", size=22, gap=10)
a.ex("A2", "單選", "A", "パレードは11月22日14:00に出発する。",
     "封王遊行幾點出發？", opts=["A. 下午2點", "B. 上午2點", "C. 晚上7點"], size=22, gap=10)
a.ex("A2", "完成句子", "封王", "優勝を決めることは封王だ。",
     "拿下總冠軍，叫___。", instr="穴埋め", size=22, gap=10)
a.ex("A2", "單選", "A", "ナイトパレードは19:00に始まる。",
     "夜間遊行晚上幾點開始？", opts=["A. 晚上7點", "B. 下午2點", "C. 上午10點"], size=22, gap=10)
a.end_report()
# ---- P7 image: below the A2 column (free space) ----
iy7 = a.y + 16
image(p, "books.jpg", COLX[0], iy7, CW, 140)
cy7 = caption(p, COLX[0], iy7 + 140, CW,
              "舊書，越讀越有味道（資料照片）。",
              "写真：作者不詳 — CC0（Wikimedia Commons）")
print("P7 image ends", cy7, "(A2 flow ended", a.y, ")")

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　電影與鋼雕　映画と鋼鉄", 25)
b.para("映画と鋼鉄が今週の見出しを分け合う。言葉をグループに分ければ覚えやすい。映画（入圍、頒獎、星光大道）と鋼鉄（鋼雕、保險箱、勞動記憶）だ。", 22)
b.expl("言葉を分けよう。映画（入圍／頒獎）、鋼鉄（鋼雕／保險箱）。")
b.para("入圍はノミネートされること。頒獎は賞を授与すること。星光大道は式典の前のレッドカーペットだ。鋼雕は鋼で作った彫刻。保險箱は高雄の労働の記憶を収めた金庫だ。", 22)
b.ex("B1", "完成句子", "入圍", "ノミネートされることは入圍だ。",
     "被選進最後的得獎名單，叫___。", instr="穴埋め", size=22, gap=10)
b.ex("B1", "單選", "A", "授賞式は11月22日18:30に始まる。",
     "金馬獎頒獎典禮幾點開始？", opts=["A. 晚上6點30分", "B. 下午2點", "C. 上午10點"], size=22, gap=10)
b.ex("B1", "完成句子", "鋼雕", "鋼で作った彫刻は鋼雕だ。",
     "用鋼鐵做的藝術，叫___。", instr="穴埋め", size=22, gap=10)
b.ex("B1", "單選", "A", "鋼雕芸術祭は11月22日に閉幕する。",
     "鋼雕藝術節展到哪天？", opts=["A. 11月22日", "B. 11月15日", "C. 11月9日"], size=22, gap=10)
b.para("覚え方のコツ：まず入圍、次に星光大道（式典の前のレッドカーペット、17:00）、そして式典（頒獎、18:30）の順に覚えよう。", 22)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　節氣與耶誕　季節", 25)
c.para("冬には冬のことばがある。今週は小雪（小雪）、節氣（節気）、燈秀（ライトショー）、市集（市場）だ。", 22)
c.expl("今号の冬のことば四つ：小雪、節氣、燈秀、市集。")
c.para("小雪は二十四節気の第20番目、立冬の次だ。節氣は節気のことで、一年に24ある。燈秀はライトショーで、メインショーは30分ごとに開かれる。市集は市場で、ワールド・オブ・フローズンの冬のマーケットのことだ。", 22)
c.ex("B2", "單選", "A", "小雪は二十四節気の第20番目だ。",
     "「小雪」是二十四節氣的第幾個？", opts=["A. 第20個", "B. 第2個", "C. 第24個"], size=22, gap=10)
c.ex("B2", "完成句子", "主燈秀", "メインのライトショーは30分ごとに繰り返される。",
     "耶誕城的___每半小時一次。", instr="穴埋め", size=22, gap=10)
c.ex("B2", "單選", "A", "冬のマーケットはワールド・オブ・フローズンにある。",
     "想逛冬日市集、買聖誕禮物，要去哪裡？", opts=["A. 魔雪奇緣世界", "B. 維多利亞港", "C. 駁二"], size=22, gap=10)
c.ex("B2", "完成句子", "市集", "市場は市集だ。",
     "賣東西、逛街的地方，叫___。", instr="穴埋め", size=22, gap=10)
c.para("季節のことばは多くいらない。四つ覚えれば、冬がぐっと近くなる。", 22)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「金馬獎11月15日頒獎」", "→「金馬獎11月22日頒獎，11月15日是爵士之夜」", "授賞式は11月22日。15日はジャズの夜だ。"),
    ("「封王遊行上午2點出發」", "→「封王遊行下午2點出發，上午沒有遊行」", "パレードは14:00出発、02:00ではない。"),
    ("「主燈秀每小時一次」", "→「主燈秀每半小時一次，17:30到23:00一共12場」", "メインのライトショーは30分ごと。17:30から23:00まで12回ある。"),
]
eh = 74 + sum(72 + len(wrap("✗ " + r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所　まちがい診療所", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, "✗ " + wrong, 21.5, "serif", True, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「天氣越冷，越要保暖。」——構文越…越…は「Xすればするほど、Yになる」という意味だ。自分で作ってみよう。夜越深，燈越亮（夜が深まるほど、明かりは明るくなる）。"
wcn = "構文：越…越…——Xすればするほど、Yになる。これで文を作ってみよう。"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式　今週の構文", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好：本週日我要去看封王遊行，穿紅色衣服為龍隊喝采。晚上回家看金馬獎轉播，還想去高雄看鋼雕，最後一天不要錯過。——台北小讀者（編輯範例）」"
lcn = "編集部の例文の手紙であり、本物の手紙ではない。延期のお知らせ：VOL.3では今号から本物の読者の手紙と第8面の最優秀作文を掲載すると予告したが、締め切りまでに掲載できるものは届かなかった。そのため例文を掲載し、募集は引き続き行う。"
lt2 = "延期披露：VOL.3曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。"
lh = 164 + (len(wrap(lt, "serif", False, 21.5, CW - 44)) + len(wrap(lt2, "serif", False, 21.5, CW - 44))) * 30.53 + (len(wrap(lcn, "sans", False, 20, CW - 44)) - 1) * 28.4
# exact draw model: lead-in 89 + lt/lt2 block lines x30.53 + gaps 31/30 + lcn lines
# (last baseline + descent 6 + pad 8). The old 62/12/26 formula under-counted
# the lead-in and inter-para gaps by ~20px (caught by occlusion audit, build 10).
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地　読者の広場", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 24)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "本週金句　今週の金句——今号の記事から一字一句そのまま", 27, "sans", True, OLIVE)
quotes = [
    ("「封王遊行從天母棒球場出發」", "優勝パレードは天母野球場を出発する。", "1ページ"),
    ("「夜間遊行晚上7點，最後一場不要錯過」", "ナイトパレード19:00——最後の公演、お見逃しなく。", "1ページ"),
    ("「小雪之後，天氣一天比一天冷」", "小雪のあと、日ごとに寒くなる。", "2ページ"),
    ("「主燈秀每半小時一次，每次5分鐘」", "メインのライトショーは30分ごと、1回5分。", "2ページ"),
    ("「頒獎典禮晚上6點30分開始」", "授賞式は18:30に始まる。", "3ページ"),
    ("「保險箱裡，裝的是高雄的勞動記憶」", "金庫の中は高雄の労働の記憶。", "3ページ"),
    ("「穿上紅色衣服，一起上街為龍隊喝采」", "赤を着て通りに出て、龍チームを応援しよう。", "4ページ"),
    ("「香港迪士尼聖誕，從11月17日開始」", "ディズニーのクリスマスは11月17日から始まる。", "5ページ"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 132
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 132 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "下期預告　来週 (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "下週：金馬獎得獎名單、封王遊行直擊、鋼雕閉幕現場，還有你們的來信和第8版最佳作文。下週見！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
