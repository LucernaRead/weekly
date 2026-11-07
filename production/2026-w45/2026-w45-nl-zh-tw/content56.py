# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JONGEREN (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JONGEREN · 青年", "De Lucerna", "NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · 荒島節目開播、音樂節與設計週落幕")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Expeditie Robinson is begonnen!", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: B1")
f.para("Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur. Negentien kandidaten leven op een onbewoond eiland. De eerste aflevering is geweest — nu begint het echte spel: vuur maken, eten zoeken, proeven winnen.")
f.para("De kandidaten slapen buiten en moeten alles zelf doen. Wie een proef verliest, kan naar huis worden gestemd. Wie het langst blijft, wint de expeditie. De kandidaten komen uit Nederland en Vlaanderen, en ze kennen elkaar nog niet allemaal.")
f.para("Twee festivals zijn intussen voorbij. ADE en de Dutch Design Week sloten allebei op zondag 25 oktober. ADE werd dertig jaar, met meer dan 3.000 artiesten op meer dan 200 locaties in Amsterdam. De Design Week in Eindhoven toonde werk van ongeveer 2.500 ontwerpers.")
f.para("Wat blijft er over? De muziek van ADE, de ideeën van de Design Week — en de vraag wie Robinson wint. Daarover lees je volgende week meer. En deze week is er genoeg te doen: het is Klimaatweek, dus ga naar buiten, plant iets groens of fiets naar de Snuffelmarkt in Zaandam.")
f.head("JONGEREN EN HET KLIMAAT", 25)
f.para("Jongeren doen veel in de Klimaatweek: fietsen in plaats van rijden, tweedehands kopen in plaats van nieuw, minder plastic gebruiken. Kleine keuzes, zeggen klimaatclubs, maar als miljoenen jongeren ze maken, tellen ze op.")
f.box("ZO KIJK JE ROBINSON", [
    ("1. Kijk zondag om 20:00 uur op RTL 4（週日晚 20:00 在 RTL 4 收看）", "serif", False, INK, 21, 1.36),
    ("2. Let op de proeven: daar worden de punten verdeeld（注意比賽項目：分數在那裡決出）", "serif", False, INK, 21, 1.36),
    ("3. Raad met vrienden wie het langst blijft（和朋友猜誰能留到最後）", "serif", False, INK, 21, 1.36),
    ("4. Volgende week lees je hier hoe het verder ging（下週這裡繼續報導進展）", "serif", False, INK, 21, 1.36),
])
f.gloss("het eiland 島 · de proef 比賽項目、考驗 · stemmen 投票 · de aflevering （一）集 · voorbij 過去了、結束了。")
f.end_report()

# col 3: facts + en jij (sequential, measured; no photo this page)
ix = COLX[3]
facts = ["Expeditie Robinson: 19 kandidaten; start zondag 1 november, 20:00 uur, RTL 4.",
         "ADE 30 jaar: meer dan 3.000 artiesten, meer dan 200 locaties; gesloten zondag 25 oktober.",
         "Dutch Design Week: ongeveer 2.500 ontwerpers; gesloten zondag 25 oktober."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "JONGEREN IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Kijk jij naar Expeditie Robinson, of doe je liever zelf iets buiten? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你看《荒島遠征》嗎，還是更愛自己出門活動？寫兩句荷蘭語寄來。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ? · 說說你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你看《荒島遠征》嗎，還是更愛自己出門活動？寫兩句荷蘭語寄來。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "OEFENINGEN · 第 5 版練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · BEGRIJPEN", 25)
e.expl("讀第 5 版文章，選出正確答案。")
e.ex("B1", "單選", "B", "Robinson 在 11 月 1 日週日開始",
     "Expeditie Robinson begon op... A. zondag 25 oktober · B. zondag 1 november · C. woensdag 21 oktober", size=20, gap=8)
e.ex("B1", "單選", "A", "19 位參賽者",
     "Expeditie Robinson heeft ___ kandidaten. A. 19 · B. 30 · C. 200", size=20, gap=8)
e.ex("B1", "單選", "C", "ADE 今年 30 年",
     "ADE werd dit jaar... A. 25 jaar · B. 26 jaar · C. 30 jaar", size=20, gap=8)
e.ex("B1", "單選", "B", "設計週約 2.500 位設計師",
     "De Design Week toonde werk van ongeveer... A. 250 ontwerpers · B. 2.500 ontwerpers · C. 3.000 ontwerpers", size=20, gap=8)
e.ex("B1", "單選", "A", "ADE 與 DDW 在 10 月 25 日週日落幕",
     "ADE en de Design Week sloten op... A. zondag 25 oktober · B. zondag 1 november · C. zaterdag 7 november", size=20, gap=8)
e.head("B · WOORDEN UIT DE TEKST", 25)
e.expl("用方框裡的詞填空。")
e.para("eiland · proef · stemmen · aflevering · voorbij · kandidaat", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "eiland", "eiland = 島（het）",
     "Robinson speelt op een onbewoond ___.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "proef", "proef = 比賽項目、考驗（de）",
     "Wie een ___ verliest, kan naar huis gaan.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "stemmen", "stemmen = 投票",
     "De kandidaten ___ wie naar huis moet.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "aflevering", "aflevering = （一）集",
     "De eerste ___ was zondag 1 november.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "voorbij", "voorbij = 過去了、結束了",
     "ADE is ___: het festival is afgelopen.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "kandidaten", "kandidaat 複數：kandidaten",
     "Er zijn 19 ___ op het eiland.", instr="填空", size=20, gap=8)
e.head("C · DE TOEKOMST MET GAAN", 25)
e.expl("用 gaan + 不定式說將來。")
e.ex("B1", "完成句子", "gaat winnen", "gaat winnen = 會贏（只是猜測）",
     "Wie ___ (winnen) Expeditie Robinson, denk je?", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaan kijken", "wij → gaan + 不定式 kijken",
     "Wij ___ (kijken) zondag naar de nieuwe aflevering.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaat praten", "hij → gaat praten",
     "Hij ___ (praten) morgen met vrienden over de proef.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaan zoeken", "zij (複數) → gaan zoeken",
     "De kandidaten ___ (zoeken) morgen eten op het eiland.", instr="填空", size=20, gap=8)
e.head("D · WAAR OF NIET WAAR?", 25)
e.ex("B1", "判斷對錯", "Waar", "對：11 月 1 日開始",
     "Expeditie Robinson begon op 1 november. Waar of niet waar?", instr="判斷", size=20, gap=8)
e.ex("B1", "判斷對錯", "Niet waar", "錯：ADE 今年 30 年",
     "ADE werd dit jaar 26 jaar. Waar of niet waar?", instr="判斷", size=20, gap=8)
e.ex("B2", "判斷對錯", "Niet waar", "錯：10 月 25 日已落幕",
     "De Design Week is nog bezig. Waar of niet waar?", instr="判斷", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jongeren.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · VERDIEPING (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERDIEPING · 深讀", "De Lucerna", "NIVEAU B2 · De codes van het KNMI · 氣象預警深度解讀")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P6-main")
f.title("Geel, oranje, rood: hoe werken de codes?", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: B2")
f.para("Het KNMI waarschuwt Nederland al jaren met kleuren. Maar de waarschuwingen zijn veranderd: vroeger golden ze voor een hele provincie, nu zijn ze lokaal. Dat betekent: jouw stad kan code oranje hebben, terwijl het twintig kilometer verderop rustig is.")
f.para("Waarom lokaal? Omdat het weer lokaal is. Een zware bui kan over één stad vallen en de buurstad overslaan. Een waarschuwing voor een hele provincie waarschuwt dan mensen die niets merken — en die letten de volgende keer minder op. Meteorologen noemen dat waarschuwingsmoeheid.")
f.para("De kleuren zelf zijn simpel. Geel: het weer kan gevaarlijk zijn, let op. Oranje: het weer ís gevaarlijk, bereid je voor — zet losse spullen vast, rijd voorzichtig. Rood: het weer is zeer gevaarlijk, ga niet de weg op als het niet moet. Rood komt weinig voor.")
f.para("Het systeem heeft ook kritiek: sommige mensen vinden de codes verwarrend — wat is het verschil tussen geel en oranje als je toch naar buiten moet? Het KNMI antwoordt: kijk altijd naar de tekst bij de code, niet alleen naar de kleur. De tekst zegt wat er écht gebeurt, waar en wanneer.")
f.para("Voor jou als lezer is de les duidelijk. Een code is geen verbod, maar een advies. Lees de waarschuwing, kijk naar je eigen plaats en beslis zelf. En in de Klimaatweek past dat goed. Het weer is van ons allemaal, maar het raakt ons allemaal anders.")
f.head("VOOR OF TEGEN LOKAAL?", 25)
f.para("Voorstanders zeggen: lokaal is eerlijker, want alleen wie het treft, wordt gewaarschuwd. Tegenstanders zeggen: lokaal is verwarrend, want de buurstad heeft een andere kleur. Het KNMI houdt vast aan lokaal: beter precies dan algemeen, zeggen de meteorologen.")
f.gloss("de meteoroloog 氣象學家 · waarschuwingsmoeheid 預警疲勞 · vastzetten 固定好 · het advies 建議、忠告 · de voorstander 支持者。")
f.end_report()

# col 3: OEFENDATA chart + pro/contra box (sequential, measured)
ix = COLX[3]
rows = [
    ("Ik blijf thuis", "45", 180),
    ("Ik kijk eerst naar de tekst", "25", 100),
    ("Ik ga toch naar buiten", "20", 80),
    ("Ik weet het niet", "10", 40),
]
cap = "OEFENDATA — verzonnen cijfers om mee te oefenen, geen echte enquête. Vraag: wat doe jij bij code oranje? (100 jongeren)"
capcn = "練習數據：虛構數字，僅供練習，非真實調查。問題：橙色預警時你會怎麼做？（100 名年輕人）"
ch = 62 + len(rows) * 58 + 14 + len(wrap(cap, "serif", False, 19, CW - 44)) * 27 + 6 + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
p.rect(ix, 200, CW, ch, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DE GRAFIEK · 圖表（練習數據）", 24, "sans", True, OLIVE)
yy3 += 58
for lab, val, bw in rows:
    p.text(ix + 22, yy3 + 20, lab, 19.5, "serif", True, INK)
    p.text(ix + CW - 22, yy3 + 20, val, 19.5, "sans", True, BRICK, anchor="end")
    p.rect(ix + 22, yy3 + 30, bw, 18, fill=OLIVE)
    yy3 += 58
yy3 += 14
yy3 = p.para(ix + 22, yy3 + 19, cap, 19, "serif", False, GREY, CW - 44, 1.36)
yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, CW - 44, 1.32) + 6
print("P6 chart ends", 200 + ch, "content to", yy3)
by6 = 200 + ch + 26
bt = [
    ("Voor lokaal: alleen wie het treft, wordt gewaarschuwd.", "serif", False, INK, 21, 1.4),
    ("Tegen lokaal: de buurstad heeft een andere kleur — verwarrend.", "serif", False, INK, 21, 1.4),
    ("De krant kiest niet: lees de tekst bij de code, niet alleen de kleur. En jij?", "serif", False, INK, 21, 1.4),
]
bh = 62 + sum(len(wrap(t, "serif", False, 21, CW - 44)) * 29.5 + 8 for t, *_ in bt) + 16 + 30
p.rect(ix, by6, CW, bh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = by6 + 16
p.text(ix + 22, yy3 + 26, "VOOR OF TEGEN? · 正方還是反方", 21, "sans", True, OLIVE)
yy3 += 52
for t, k, b, fl, s, lh in bt:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.4) + 8
print("P6 col3 ends", by6 + bh)

# ---- P6 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "OEFENINGEN · 第 6 版練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LEES DE GRAFIEK", 25)
e.expl("看第 6 版圖表（練習數據）回答。")
e.ex("B2", "完成句子", "45", "45 名年輕人選擇待在家裡",
     "Bij code oranje blijft ___ van de 100 jongeren thuis.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "25", "25 人先看預警文字",
     "___ jongeren kijken eerst naar de tekst.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "70", "45 + 25 = 70",
     "Thuis blijven en eerst de tekst lezen samen: ___ jongeren.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "10", "10 人不知道",
     "___ jongeren weten het niet.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "100", "圖表共 100 人：45+25+20+10",
     "De grafiek telt in totaal ___ jongeren.", instr="填空", size=21.5, gap=9)
e.head("B · BEGRIJPEN", 25)
e.expl("讀第 6 版文章，選出正確答案。")
e.ex("B2", "單選", "B", "以前預警針對整個省",
     "Vroeger golden waarschuwingen voor... A. één stad · B. een hele provincie · C. het hele land", size=21.5, gap=9)
e.ex("B2", "單選", "B", "如今預警是本地的",
     "Tegenwoordig zijn waarschuwingen... A. voor het hele land · B. lokaal · C. alleen voor de kust", size=21.5, gap=9)
e.ex("B2", "單選", "C", "紅色：非常危險，非必要不上路",
     "Code rood betekent... A. let op · B. bereid je voor · C. zeer gevaarlijk, ga niet de weg op", size=21.5, gap=9)
e.ex("B2", "單選", "A", "預警疲勞：警告太多導致不再注意",
     "Waarschuwingsmoeheid is... A. moe van waarschuwingen, dus minder opletten · B. moe van het weer · C. een nieuwe code", size=21.5, gap=9)
e.ex("B2", "單選", "B", "KNMI 說：看代碼旁邊的文字",
     "Het KNMI zegt: kijk niet alleen naar de kleur, maar naar... A. de wind · B. de tekst bij de code · C. de televisie", size=21.5, gap=9)
e.head("C · WOORDEN", 25)
e.expl("用方框裡的詞填空。")
e.para("lokaal · waarschuwingsmoeheid · vastzetten · advies", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B2", "完成句子", "lokaal", "lokaal = 本地的",
     "De waarschuwing geldt voor jouw eigen stad: ze is ___.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "waarschuwingsmoeheid", "waarschuwingsmoeheid = 預警疲勞",
     "Wie te vaak onnodig wordt gewaarschuwd, krijgt ___.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "vastzetten", "vastzetten = 固定好",
     "Bij code oranje moet je losse spullen ___.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "advies", "advies = 建議（het）",
     "Een code is geen verbod, maar een ___.", instr="填空", size=21.5, gap=9)
e.head("D · MAAK DE ZINNEN", 25)
e.expl("把詞組成正確的句子。")
e.ex("B2", "造句", "De waarschuwing geldt voor jouw stad.", "主語 + 動詞 + 地點",
     "de waarschuwing / geldt / voor jouw stad → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "Kijk altijd naar de tekst bij de code.", "祈使句：動詞在首位",
     "kijk / altijd / naar de tekst / bij de code → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "Rood komt weinig voor.", "weinig voor = 很少出現",
     "rood / komt / weinig / voor → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "Het weer raakt ons allemaal anders.", "raakt + 賓語 + 方式",
     "het weer / raakt / ons / allemaal anders → ___", instr="造句", size=21.5, gap=9)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-verdieping.svg")
print("P6 saved, exercises so far:", len(REG))
