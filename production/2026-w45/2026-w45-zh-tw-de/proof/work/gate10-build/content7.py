# -*- coding: utf-8 -*-
# W45 zh-tw core, VOL.2: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-tw-de-proof/work/gate10-out/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Sprachfokus", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Drei Stufen, drei Themen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 展會的話 · Messewörter", 24)
a.para("Die Messen dieser Woche geben Ihnen vier nützliche Wörter: 旅展 (Reisemesse), 攤位 (Stand), 集章 (Stempelsammeln) und 吉祥物大遊行 (Maskottchenparade). Einmal gelernt, ist die ganze Messe klar.", 21.5)
a.glossline("Vier Messewörter: 旅展, 攤位, 集章, 吉祥物大遊行.")
a.para("旅展 ist kurz für 旅行展覽會 (Reiseausstellung). Ein 攤位 ist ein Stand in der Messe; Taipeh hat 1.600 davon. 集章 heißt Stempel an festen Punkten sammeln — alle sechs Greenway-Stempel bringen einen Preis.", 21.5)
a.ex("A2", "完成句子", "攤位", "Ein Stand in der Messe ist ein 攤位.",
     "旅展裡的一個小展位,叫___。", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Die Maskottchenparade läuft täglich um 14:00 Uhr.",
     "吉祥物大遊行每天幾點?", opts=["A. 下午2點", "B. 中午12點", "C. 晚上7點"], size=20.5, gap=10)
a.ex("A2", "完成句子", "集章", "Stempel an festen Punkten sammeln heißt 集章.",
     "在6大綠道蓋章收集,叫___。", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Die Reisemesse ist im Nangang Exhibition Center.",
     "台北旅展在哪裡?", opts=["A. 南港展覽館一館", "B. 台北大巨蛋", "C. 高雄駁二"], size=20.5, gap=10)
a.para("Üben Sie: 「旅展幾點開門？」 („Wann öffnet die Messe?“) — freitags erst mittags, sonst um 10:00 Uhr.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 球賽與節氣 · Spiele, Jahreszeit", 24)
b.para("Sport und Jahreszeiten teilen sich die Schlagzeilen dieser Woche. In Gruppen gelernt, bleiben die Wörter haften: Gewinnen （封王、完封） und Winter （立冬、進補）.", 21.5)
b.glossline("In Gruppen lernen: Gewinnen (封王/完封), Winter (立冬/進補).")
b.para("封王 heißt die Meisterschaft sichern; 完封 heißt die andere Seite ohne Punkte lassen, 0 Runs. 立冬 ist der Solartermin, der den Winter beginnt; 進補 heißt vor der Kälte nahrhaftes, heißes Essen.", 21.5)
b.ex("B1", "完成句子", "封王", "Den Titel gewinnen heißt 封王.",
     "拿下總冠軍,叫___。", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "單選", "A", "完封 heißt: Die andere Seite punktet nullmal.",
     "「完封」是什麼意思?", opts=["A. 對手得0分", "B. 大勝10分", "C. 打滿9局"], size=20.5, gap=10)
b.ex("B1", "完成句子", "立冬", "Lidong beginnt den Winter.",
     "冬天第一個節氣是___。", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Ingwerente ist ein Lidong-Gericht.",
     "立冬常吃的鍋是哪一種?", opts=["A. 薑母鴨", "B. 冰品", "C. 生魚片"], size=20.5, gap=10)
b.para("Merktrick: zuerst 封王 lernen, dann die Art des Sieges （完封）, dann die Jahreszeit （立冬）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 港台說法 · Lokale Ausdrücke", 24)
c.para("Taiwan und Hongkong sagen manches auf eigene Art. Diese Woche: 打卡 (Foto-Check-in), 討糖 (Süßes einfordern), 踩街 (Kostümparade) und 泡湯 (Quellbad).", 21.5)
c.glossline("Vier lokale Wörter aus dieser Ausgabe: 打卡, 討糖, 踩街, 泡湯.")
c.para("打卡 hieß zuerst Einstempeln am Arbeitsplatz, auf Festen aber: ein Foto posten — Ich war hier. 討糖 sagen Kinder an Halloween in Geschäften; 踩街 ist die Kostümparade selbst; 泡湯 ist das Herbstvergnügen im heißen Quellbad.", 21.5)
c.ex("B2", "單選", "A", "Auf einem Fest postet man mit 打卡 ein Foto und zeigt: Ich war da.",
     "在旅展、節慶場合,「打卡」是什麼意思?", opts=["A. 拍照分享,說自己來過", "B. 上班簽到", "C. 買門票"], size=20.5, gap=10)
c.ex("B2", "完成句子", "討糖", "Süßes einfordern heißt 討糖.",
     "萬聖節小朋友去店家___。", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "單選", "A", "踩街 ist eine Straßenparade im Kostüm.",
     "「踩街」是什麼?", opts=["A. 穿裝扮上街遊行", "B. 在街上跑步", "C. 逛夜市"], size=20.5, gap=10)
c.ex("B2", "完成句子", "泡湯", "In einer heißen Quelle baden heißt 泡湯.",
     "秋冬去溫泉洗澡、放鬆,叫___。", instr="Ausfüllen", size=20.5, gap=10)
c.para("Vier Ausdrücke genügen — und jeder Ausflug fühlt sich näher an.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「龍隊完勝兄弟6比0」", "→「龍隊完封兄弟6比0」", "hoch gewinnen heißt 完勝 und null Punkte für die andere Seite heißt 完封."),
    ("「立冬就是冬至」", "→「立冬是冬天開始,冬至是白天最短的一天」", "Lidong: Winterbeginn; Sonnenwende: kürzester Tag. Verschiedene Begriffe."),
    ("「金融科技週在台北開幕」", "→「金融科技週在香港開幕」", "Stadt prüfen: FinTech Week in Hongkong, nicht Taipeh."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所 · Fehlerklinik", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先去集章，再去看表演。」 — 先…再… = erst X, dann Y. Bilden Sie selbst einen Satz: 先比價，再結帳 (erst vergleichen, dann bezahlen)."
wcn = "Muster 先…再…: erst X, dann Y — selbst einen Satz bilden."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Satzmuster", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:上週我去天母討糖,拿到一顆很大的糖果!這週我想去旅展看吉祥物大遊行,還想集滿6大綠道的章。——台北小讀者(編輯範例)」"
lcn = "Beispielbrief der Redaktion — kein echter Brief. VOL.1 versprach echte Briefe und die beste Seite-8-Aufgabe ab dieser Ausgabe; bis Redaktionsschluss kam nichts Veröffentlichbares — das Beispiel bleibt, und die Einladung bleibt offen: Schicken Sie uns Ihren Brief!"
lt2 = "延期披露:VOL.1曾預告本期起刊登真實讀者來信和第8版最佳作文;截至截稿,本報未收到可刊登的真實來信與投稿,因此本期仍刊登編輯範例,並繼續公開徵集。你的來信,下一期見。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 40
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Leserecke", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Sätze der Woche — Wort für Wort aus den Artikeln dieser Ausgabe", 27, "sans", True, OLIVE)
quotes = [
    ("「用手機轉帳、掃碼付款、網上買保險，都是金融科技」", "Per Handy überweisen, per Scan bezahlen, online versichern — das ist Fintech.", "S. 1"),
    ("「123個國家及城市、1,600個攤位」", "123 Länder und Städte, 1.600 Stände.", "S. 1"),
    ("「需要才買，不要為了折扣買一堆用不到的東西」", "Kaufen Sie, was Sie brauchen; kaufen Sie keinen Stapel Dinge, die Sie nicht nutzen, nur wegen eines Rabatts.", "S. 2"),
    ("「在高雄，鋼鐵也能變成舞台」", "In Kaohsiung kann sogar Stahl zur Bühne werden.", "S. 3"),
    ("「福隆的夏天，在10月26日畫下句點」", "Fulongs Sommer endete am 26. Oktober.", "S. 3"),
    ("「6比0完封兄弟，龍隊拋下紅色彩帶」", "Ein 6:0-Shutout gegen die Brothers, und die Dragons warfen die roten Bänder.", "S. 4"),
    ("「250家店家一起討糖」", "250 Geschäfte verteilen gemeinsam Süßes.", "S. 5"),
    ("「旅展首日中午12點才開門」", "Am ersten Messetag öffnen die Türen erst mittags.", "S. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 138
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 138 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期預告 · Nächste Woche (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "下週三雙11,你買了什麼?下週一旅展最後一天直擊,高雄鋼雕藝術節展到11月22日,還有你們的來信和第8版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
