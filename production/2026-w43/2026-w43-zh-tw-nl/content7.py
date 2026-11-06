# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Taalfocus", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Drie niveaus, drie thema's")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 天氣的話 · Weerwoorden", 24)
a.para("De tyfoonweek vult het nieuws met weerwoorden — leer de zes die je het vaakst ziet: 海上颱風警報 (zeewaarschuwing), 陸上颱風警報 (landwaarschuwing), 共伴效應 (gezamenlijk effect), 外圍環流 (buitenste circulatie), 豪雨 (stortregen), 停班停課 (werk en school opgeschort).", 21.5)
a.glossline("Zes weerwoorden, het hele nieuws van de week — één keer leren, de hele week lezen.")
a.para("Twee soorten waarschuwingen: eerst een 海上警報 (zeewaarschuwing), zolang de tyfoon op zee is; een 陸上警報 (landwaarschuwing) als hij nadert. Zwaardere regen dan 大雨 is 豪雨 (stortregen).", 21.5)
a.ex("A2", "完成句子", "海上", "Een zeewaarschuwing komt eerst, zolang de tyfoon nog op zee is.",
     "颱風還在海上,先發佈___颱風警報。", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Tíngbān tíngkè betekent dat werk en school stilliggen.",
     "「停班停課」是什麼意思?", opts=["A. 不上班、不上課", "B. 提早一小時下班", "C. 換到別天上班"], size=20.5, gap=10)
a.ex("A2", "完成句子", "豪", "Háoyǔ is zwaarder dan dàyǔ.",
     "比大雨還大的雨,叫___雨。", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "單選", "A", "De buitenste circulatie (wàiwéi huánliú) brengt regen.",
     "颱風的外圍___會帶來雨。", opts=["A. 環流", "B. 警報", "C. 假期"], size=20.5, gap=10)
a.para("Oefen: 「明天會停班停課嗎？」 ('Werk en school morgen vrij?') — controleer de aankondiging van je stad.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 日子與節日 · Feestdagen", 24)
b.para("Bijzondere dagen deze week. Groepeer de woorden, dan blijven ze hangen: vrije dagen （連假、補假）, reizen （疏運）, en feestplezier （登高、討糖、星光大道）.", 21.5)
b.glossline("Groepeer de woorden: vrije dagen (連假/補假), reizen (疏運), feestplezier (登高/討糖/星光大道).")
b.para("連假 is een reeks vrije dagen op een rij; valt een feestdag in het weekend en is een weekdag in plaats daarvan vrij, dan is die extra dag een 補假； en de extra treinen en bussen voor iedereen zijn de 疏運.", 21.5)
b.ex("B1", "完成句子", "補假", "Een inhaaldag: bǔjià.",
     "假日逢週日,週一多放一天,叫___。", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Shūyùn = extra vervoer voor de vakantiedrukte.",
     "「疏運」是連假時做什麼?", opts=["A. 加開班次載客", "B. 賣紀念票", "C. 修馬路"], size=20.5, gap=10)
b.ex("B1", "完成句子", "討糖", "Tǎotáng is Taiwanees voor trick-or-treat.",
     "萬聖節,小朋友去店家___(要糖果)。", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Het rode-loperdeel heet xīngguāng dàdào.",
     "頒獎典禮走紅毯的部分叫?", opts=["A. 星光大道", "B. 人氣獎", "C. 疏運大道"], size=20.5, gap=10)
b.para("Geheugentruc: leer 連假 eerst, dan de drukte （疏運） en de extra dag （補假）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 在地說法 · Lokaal taalgebruik", 24)
c.para("Taiwan en Hongkong zeggen dingen elk op hun eigen manier. Threads heet in Taiwan 「脆」; een goede post bewaar je met 「留友看」 — 'bewaren voor je vrienden'; en een compliment in zhuyin-symbolen is een 「ㄅ級分」.", 21.5)
c.glossline("Drie Taiwanese internetmunten — allemaal uit een PopDaily-overzicht van mei 2026 met de memes van het jaar, niet uit het nieuws van deze week.")
c.para("In Hongkong is Halloween 「哈囉喂」; hotpot is 「打邊爐」; goedkoop en lekker is 「抵食」; krabben weeg je in 「両」, en de festivalmunten zijn 「品味券」.", 21.5)
c.ex("B2", "單選", "A", "In Taiwan heeft Threads de bijnaam cuì (knapperig).",
     "台灣人把 Threads 暱稱作什麼?", opts=["A. 脆", "B. 脆餅", "C. 推特兒"], size=20.5, gap=10)
c.ex("B2", "完成句子", "留友", "Liúyǒu kàn — bewaar het voor je vrienden.",
     "看到好文,先存起來「___看」。", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "單選", "A", "Hāluōwèi is Halloween in het Hongkongs.",
     "「哈囉喂」是香港人怎麼說哪個節日?", opts=["A. 萬聖節", "B. 聖誕節", "C. 重陽節"], size=20.5, gap=10)
c.ex("B2", "完成句子", "品味", "De festivalbonnen zijn pǐnwèiquàn (proefmunten).",
     "美酒佳餚巡禮換飲品小食的券,叫___券。", instr="Vul in", size=20.5, gap=10)
c.para("Leer vijf plaatselijke uitdrukkingen en elk gesprek voelt dichterbij.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「台風來了」", "→「颱風來了」", "Taiwan schrijft 颱風; 台風 is de Japanse kanji-spelling."),
    ("「我買了四兩的蟹」", "→「我買了四両的蟹」", "Krabben weeg je in 両 (taels); 兩 is 'twee' — zie 兩隻蟹 (twee krabben)."),
    ("「天氣慢慢的變涼」", "→「天氣慢慢地變涼」", "地 (de) markeert hoe een handeling gebeurt, vóór het werkwoord."),
    ("「我明天放四天假去玩」", "→「我請了四天假去玩」", "請假 = zelf verlof vragen; 放假 = de vrije dag is voor iedereen."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所 · Foutenkliniek", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看警報，再決定出不出門。」 — het patroon 先…再… geeft de volgorde aan: eerst X, dan Y. Gemaakt voor de tyfoonweek: 先查公告，再改行程 (eerst de aankondigingen checken, dan plannen wijzigen)."
wcn = "Patroon: 先…再… — eerst X, dan Y. Maak er zelf een zin mee."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Zinspatroon", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:重陽節我跟阿公去登高,他走得比我還快!晚上我們吃大閘蟹,蟹黃真的好多。下週我想去看台灣大賽。——台北小讀者(編輯範例)」"
lcn = "Voorbeeldbrief van de redactie — geen echte. VOL.2 drukt echte lezersbrieven en het beste schrijfwerk van pagina 8!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Lezershoek", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Zinnen van de week — woord voor woord uit de artikelen van dit nummer", 27, "sans", True, OLIVE)
quotes = [
    ("「路徑還有變數,會不會登陸,還沒有人知道」", "Het spoor kan nog veranderen; niemand weet nog of hij aan land komt.", "p. 1"),
    ("「請四天假,換九天連假」", "Vier dagen verlof, negen dagen vrij.", "p. 2"),
    ("「登高望遠,人也精神了」", "Klim hoog, kijk ver — en voel je verfrist.", "p. 3"),
    ("「農曆九月吃蟹乸,農曆十月吃蟹公」", "Vrouwtjescrabs in de 9e maanmaand, mannetjes in de 10e.", "p. 3"),
    ("「先贏四場的隊伍,就是今年的總冠軍」", "Wie het eerst vier wedstrijden wint, is de kampioen van dit jaar.", "p. 4"),
    ("「颱風改了日期,卻改不了大家過節的心情」", "De tyfoon veranderde de datum, niet de feeststemming.", "p. 5"),
    ("「三百四十多個攤位,把世界搬到海邊」", "Meer dan 340 kraampjes brengen de wereld naar de haven.", "p. 6"),
    ("「星期五、六的晚上,今年第一次開到凌晨一時」", "Vrijdag- en zaterdagavonden lopen voor het eerst tot 1:00 's nachts.", "p. 6"),
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
p.text(MX + 28, py + 44, "下期預告 · Volgende week (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "台灣大賽冠軍出爐!美酒佳餚巡禮開幕直擊,天母搞什麼鬼主活動、福隆沙雕最後一天,還有你們的來信和第 8 版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
