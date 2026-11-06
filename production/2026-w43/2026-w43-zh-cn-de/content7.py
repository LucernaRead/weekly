# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Sprachfokus", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Drei Niveaus, drei Themen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 购物与量词 · Klassifikatoren", 24)
a.para("Beim Einkaufen nutzt das Chinesische Zähleinheitswörter (量词): 一件外套 (ein Mantel), 一条围巾 (ein Schal), 一斤蟹 (ein halbes Kilo Krabben), 一只蟹 (eine Krabbe). Das Muster lautet: Zahl + Zähleinheitswort + Nomen (数词 + 量词 + 名词).", 21.5)
a.glossline("Das Deutsche zählt locker; das Chinesische wählt für jede Art von Ding ein eigenes Zähleinheitswort — kein Plural, kein -s.")
a.ex("A2", "完成句子", "件", "外套 nimmt das Zähleinheitswort 件 jiàn.",
     "我想买一___外套。", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "单选", "B", "围巾 nimmt 条 tiáo (lange, weiche Dinge).",
     "「一条」可以说什么? A. 一条外套 · B. 一条围巾 · C. 一条大闸蟹", size=20.5, gap=10)
a.ex("A2", "完成句子", "斤", "斤 jīn — ein halbes Kilo; Marktpreise gelten pro 斤.",
     "大闸蟹多少钱一___?", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "单选", "A", "Kleidung nimmt 件, nicht 个 oder 条.",
     "哪个说法对? A. 一件衣服 · B. 一个衣服 · C. 一条衣服", size=20.5, gap=10)
a.para("Noch eines zum Üben: 「这件外套多少钱?」 (Wie viel kostet dieser Mantel?) Fragen Sie beim Einkaufen zuerst nach dem Preis, dann zahlen Sie.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Zeit & Daten", 24)
b.para("Das Chinesische nennt Zeiten groß → klein: Jahr, Monat, Tag, Wochentag, Tageszeit, Stunde. Beispiel: 「10月20日晚上8点」 (20. Okt., 20 Uhr) — die größte Einheit zuerst, nichts vertauscht.", 21.5)
b.glossline("So wird aus dem Deutschen «Freitagabend, 23. Okt.» im Chinesischen 10月23日星期五晚上.")
b.ex("B1", "单选", "B", "凌晨 língchén — die frühen Stunden nach Mitternacht.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "上午", "Die NBA startete am Morgen, Pekinger Zeit.",
     "NBA 在北京时间10月21日___开打。(不是晚上)", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Reihenfolge groß → klein: 20. Okt., Abend, 20 Uhr.",
     "哪个顺序对? A. 10月20日晚上8点 · B. 8点晚上10月20日 · C. 晚上8点10月20日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周五", "Der 23. Okt. ist ein Freitag — 周五.",
     "10月23日是星期五,也可以说___。霜降在这天。", instr="Ausfüllen", size=20.5, gap=10)
b.para("Zwei weitere Wörter: 凌晨 (língchén) sind die frühen Stunden nach Mitternacht, vor der Dämmerung; 傍晚 (bàngwǎn) ist die kurze Zeit kurz vor dem Dunkelwerden.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Nachrichten lesen", 24)
c.para("Wenn ein Bericht einen Streit (争议) behandelt, trennen Sie drei Satzarten: Behauptungen im Netz (说法), offizielle Stellungnahmen (声明) und Marktdaten (数据). Behauptungen können übertreiben; Daten brauchen Quelle und Datum. Seite 6 ist das Beispiel: 「暴跌40%」 ist eine Behauptung, 77,5 元 und 57,5 元 sind Daten, 「崩盘不实」 ist eine Stellungnahme.", 21.5)
c.glossline("Fragen Sie bei jeder Zahl: Wer hat sie gemessen, und wann?") 
c.ex("B2", "单选", "C", "「暴跌40%」 war Netzbehauptung, nicht Messdaten.",
     "「暴跌超过40%」在第6版里是什么? A. 数据 · B. 声明 · C. 网上的说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "声明", "声明 shēngmíng — die offizielle Verbandsstellungnahme.",
     "协会10月19日发表___,说「崩盘」不是真的。", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Erst Daten und Quelle; die Schlagzeile zuletzt.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和出处 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "25.8", "Der errechnete Rückgang auf Seite 6: 25,8 %.",
     "第6版真正算出的数据降幅是___%。", instr="Ausfüllen", size=20.5, gap=10)
c.para("Versuchen Sie es selbst: Im Hot-Search-Kasten auf Seite 1 ist 「第 8 位」 ein Rang — Daten. Die Wörter einer Schlagzeile sind Behauptungen. Können Sie sie auseinanderhalten?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de) zeigt, wie eine Handlung geschieht; es steht vor dem Verb."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de) verbindet ein Verb mit einer Gradangabe: 跑得快."),
    ("「我买了三只大闸蟹个」", "→ 「我买了三只大闸蟹。」", "Reihenfolge: Zahl + Zähleinheitswort + Nomen. Das letzte 个 ist zu viel; Krabben nehmen 只."),
    ("「霜降在星期五十月二十三日」", "→ 「霜降在10月23日,星期五。」", "Zeiten gehen groß → klein: Monat und Tag zuerst, der Wochentag zuletzt."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所 · Fehlerklinik", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先付定金,后付尾款。」(Erst die Anzahlung, dann der Restbetrag.) Das Muster 先…后/再… ordnet die Handlungen. Mehr: 「先看天气,再出门。」「先洗手,再吃饭。」"
wcn = "Muster: 先 … 后/再 … — erst X, dann Y. Bilden Sie einen eigenen Satz."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Satzmuster", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在多伦多。霜降那天,我吃了柿子,也给妈妈打了电话。我的购物车里有一件外套,还在等付尾款。」"
lcn = "Ein Beispielbrief der Redaktion — kein echter. VOL.2 druckt echte Leserbriefe und die besten Texte von Seite 8!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · Leserecke", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · Sätze der Woche (wörtlich, aus den Artikeln dieser Ausgabe)", 27, "sans", True, OLIVE)
quotes = [
    ("「今年的双11来得早」", "Der 双11 kam dieses Jahr früh.", "S. 1"),
    ("「付完尾款，快递就开始送货了」", "Ist der Restbetrag gezahlt, beginnt die Lieferung.", "S. 1"),
    ("「付完尾款，商家就发货」", "Zahlen Sie den Restbetrag, versendet der Verkäufer.", "S. 2"),
    ("「遥知兄弟登高处，遍插茱萸少一人」", "Wang Weis berühmte 重阳-Zeile (Gedicht).", "S. 3"),
    ("「两个分数只差2.735分」", "Die beiden Punktzahlen unterscheiden sich nur um 2,735 Punkte.", "S. 4"),
    ("「最大的看点是詹姆斯」", "Die größte Attraktion ist LeBron.", "S. 4"),
    ("「看S16，要通宵了」", "S16 zu schauen heißt, die ganze Nacht wach zu bleiben.", "S. 5"),
    ("「先看数据，再看标题」", "Erst die Daten, dann die Schlagzeile (Regel von Seite 6).", "S. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 150
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 150 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期预告 · Nächste Woche (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16 瑞士轮打完了:LPL 的四支队打得怎么样?双11 的包裹都到了吗?我们追踪报道。11月7日是立冬,冬天要来了。还有你们的来信和第 8 版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
