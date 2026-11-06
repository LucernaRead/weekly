# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-de/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Sprachfokus", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Drei Stufen, drei Themen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 天氣的話 · Wetterwörter", 24)
a.para("Sechs Wetterwörter beherrschen die Nachrichten dieser Woche: 海上颱風警報 (Seewarnung), 陸上颱風警報 (Landwarnung), 共伴效應 (gemeinsamer Effekt), 外圍環流 (äußere Zirkulation), 豪雨 (Starkregen), 停班停課 (Arbeit und Schule ausgesetzt).", 21.5)
a.glossline("Einmal lernen — die ganze Woche lesen.")
a.para("Zwei Warnarten: zuerst die 海上警報 (Seewarnung), solange der Taifun auf See ist; dann die 陸上警報 (Landwarnung) bei Landnähe. Stärker als 大雨 ist 豪雨 (Starkregen).", 21.5)
a.ex("A2", "完成句子", "海上", "Seewarnung zuerst — der Taifun ist noch auf See.",
     "颱風還在海上,先發佈___颱風警報。", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "單選", "A", "停班停課 bedeutet: Arbeit und Schule fallen aus.",
     "「停班停課」是什麼意思?", opts=["A. 不上班、不上課", "B. 提早一小時下班", "C. 換到別天上班"], size=20.5, gap=10)
a.ex("A2", "完成句子", "豪", "豪雨 (háo) ist stärker als 大雨.",
     "比大雨還大的雨,叫___雨。", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Die äußere Zirkulation (外圍環流) bringt Regen.",
     "颱風的外圍___會帶來雨。", opts=["A. 環流", "B. 警報", "C. 假期"], size=20.5, gap=10)
a.para("Üben Sie: 「明天會停班停課嗎？」 („Fallen Arbeit und Schule morgen aus?“) — prüfen Sie die Ankündigung Ihrer Stadt.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 日子與節日 · Feiertage", 24)
b.para("Gruppieren Sie die Wörter, dann bleiben sie haften: freie Tage （連假、補假）, Reisen （疏運） und Festspaß （登高、討糖、星光大道）.", 21.5)
b.glossline("In Gruppen lernen: freie Tage, Reisen, Festspaß.")
b.para("連假 ist eine Reihe freier Tage am Stück; fällt ein Feiertag aufs Wochenende, ist der Extratag ein 補假； und die Zusatzzüge und -busse für alle sind die 疏運.", 21.5)
b.ex("B1", "完成句子", "補假", "Ein nachgeholter freier Tag: 補假.",
     "假日逢週日,週一多放一天,叫___。", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "單選", "A", "疏運 = Zusatzverkehr für den Feiertagsansturm.",
     "「疏運」是連假時做什麼?", opts=["A. 加開班次載客", "B. 賣紀念票", "C. 修馬路"], size=20.5, gap=10)
b.ex("B1", "完成句子", "討糖", "討糖 heißt taiwanisch „Süßes oder Saures“.",
     "萬聖節,小朋友去店家___(要糖果)。", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Der Roter-Teppich-Teil eines Preisabends ist die 星光大道.",
     "頒獎典禮走紅毯的部分叫?", opts=["A. 星光大道", "B. 人氣獎", "C. 疏運大道"], size=20.5, gap=10)
b.para("Merktrick: erst 連假, dann die Menschenmengen （疏運） und der Extratag （補假）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 在地說法 · Lokale Ausdrücke", 24)
c.para("Taiwan und Hongkong reden je anders. In Taiwan heißt Threads 「脆」; gute Beiträge speichert man mit 「留友看」 — „für Freunde aufheben“; ein Lob in Zhuyin-Zeichen ist ein 「ㄅ級分」.", 21.5)
c.glossline("Drei taiwanische Internetprägungen — aus einer PopDaily-Übersicht vom Mai 2026, nicht aus dieser Woche.")
c.para("In Hongkong heißt Halloween 「哈囉喂」; Hot Pot heißt 「打邊爐」; günstig und lecker ist 「抵食」; Krabben wiegt man in 「両」, und die Marken des Essensfestivals sind die 「品味券」.", 21.5)
c.ex("B2", "單選", "A", "In Taiwan trägt Threads den Spitznamen 脆 (knusprig).",
     "台灣人把 Threads 暱稱作什麼?", opts=["A. 脆", "B. 脆餅", "C. 推特兒"], size=20.5, gap=10)
c.ex("B2", "完成句子", "留友", "留友看 — für Freunde zum Lesen aufheben.",
     "看到好文,先存起來「___看」。", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "單選", "A", "哈囉喂 ist Hongkongs Halloween.",
     "「哈囉喂」是香港人怎麼說哪個節日?", opts=["A. 萬聖節", "B. 聖誕節", "C. 重陽節"], size=20.5, gap=10)
c.ex("B2", "完成句子", "品味", "Die Coupons heißen 品味券 (Verkostungsmarken).",
     "美酒佳餚巡禮換飲品小食的券,叫___券。", instr="Ausfüllen", size=20.5, gap=10)
c.para("Fünf lokale Ausdrücke genügen — und jedes Gespräch fühlt sich näher an.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「台風來了」", "→「颱風來了」", "Taiwan schreibt 颱風; 台風 ist die japanische Kanji-Schreibung."),
    ("「我買了四兩的蟹」", "→「我買了四両的蟹」", "Krabben: 両 (Tael); 兩 = „zwei“, z. B. 兩隻蟹 (zwei Krabben)."),
    ("「天氣慢慢的變涼」", "→「天氣慢慢地變涼」", "地 (de) markiert, wie eine Handlung geschieht — es steht vor dem Verb."),
    ("「我明天放四天假去玩」", "→「我請了四天假去玩」", "請假 = selbst Urlaub beantragen; 放假 = der freie Tag wird allen gegeben."),
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
wt = "「先看警報，再決定出不出門。」 — Das Muster 先…再… ordnet zwei Handlungen: erst X, dann Y. Wie gemacht für die Taifunwoche: 先查公告，再改行程 (erst Hinweise prüfen, dann Pläne ändern)."
wcn = "Muster: 先…再… — erst X, dann Y. Bilden Sie damit Ihren eigenen Satz."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Satzmuster", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:重陽節我跟阿公去登高,他走得比我還快!晚上我們吃大閘蟹,蟹黃真的好多。下週我想去看台灣大賽。——台北小讀者(編輯範例)」"
lcn = "Ein Beispielbrief der Redaktion — kein echter. VOL.2 druckt echte Leserbriefe und die beste Schreibaufgabe von Seite 8!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Leserecke", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Sätze der Woche — Wort für Wort aus den Artikeln dieser Ausgabe", 27, "sans", True, OLIVE)
quotes = [
    ("「路徑還有變數,會不會登陸,還沒有人知道」", "Die Zugbahn kann sich noch ändern; niemand weiß bisher, ob er an Land geht.", "S. 1"),
    ("「請四天假,換九天連假」", "Vier Tage Urlaub, neun Tage frei.", "S. 2"),
    ("「登高望遠,人也精神了」", "Steigen Sie hoch, schauen Sie weit — und fühlen Sie sich erfrischt.", "S. 3"),
    ("「農曆九月吃蟹乸,農曆十月吃蟹公」", "Weibliche Krabben im 9. Mondmonat, männliche im 10.", "S. 3"),
    ("「先贏四場的隊伍,就是今年的總冠軍」", "Wer zuerst vier Siege hat, ist der Meister dieses Jahres.", "S. 4"),
    ("「颱風改了日期,卻改不了大家過節的心情」", "Der Taifun änderte den Termin, nicht die Feststimmung.", "S. 5"),
    ("「三百四十多個攤位,把世界搬到海邊」", "Über 340 Stände bringen die Welt an den Hafen.", "S. 6"),
    ("「星期五、六的晚上,今年第一次開到凌晨一時」", "Freitag- und Samstagnächte laufen erstmals bis 1 Uhr nachts.", "S. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 146
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 146 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期預告 · Nächste Woche (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "台灣大賽冠軍出爐!美酒佳餚巡禮開幕直擊,天母搞什麼鬼主活動、福隆沙雕最後一天,還有你們的來信和第 8 版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
