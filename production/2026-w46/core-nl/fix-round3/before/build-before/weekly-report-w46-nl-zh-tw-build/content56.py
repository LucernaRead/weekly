# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-nl-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JONGEREN (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JONGEREN · 年輕人", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · 魯濱遜、鞋子與願望清單")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Robinson op zondag — en de schoen staat klaar", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: B1")
f.para("Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4. Negentien bekende Nederlanders en Vlamingen leven 34 dagen op een onbewoond eiland in Maleisië. Nicolette Kluijver en Edson da Graça presenteren het programma, Camille Vanuxem is de verslaggever.")
f.para("De kandidaten slapen buiten en moeten alles zelf doen: vuur maken, eten zoeken, proeven winnen. Wie een proef verliest, kan naar huis worden gestemd. Wie het langst blijft, wint de expeditie. Het seizoen begon op zondag 1 november — en elke week wordt het spel harder.")
f.para("Deze week is zondag 15 november een drukke dag: overdag de intocht in Amsterdam, 's avonds een nieuwe aflevering van Robinson. En na de intocht mag de schoen. Ook jongeren zetten hun schoen — met een verlanglijstje erin, in plaats van alleen een tekening.")
f.para("Een verlanglijstje schrijven is ook Nederlands oefenen: schrijf in het Nederlands wat je wilt, waarom je het wilt en voor wie je het nog meer opschrijft. Sinterklaas leest Nederlands, zeggen kinderen — en de redactie ook.")
f.head("JONGEREN EN DE SCHOEN", 25)
f.para("De schoen zetten is niet alleen voor kleine kinderen. Jongeren zetten hun schoen met een wortel voor het paard, een tekening — of een verlanglijstje met drie wensen. Klein of groot, een wens op papier is het begin van Sinterklaas.")
f.box("ZO KIJK JE ROBINSON", [
    ("1. Kijk zondag om 20:00 uur op RTL 4（週日 20:00 在 RTL 4 收看）", "serif", False, INK, 21, 1.36),
    ("2. Let op de proeven: daar worden de punten verdeeld（看考驗：分數在那裡決定）", "serif", False, INK, 21, 1.36),
    ("3. Raad met vrienden wie het langst blijft（和朋友猜誰留得最久）", "serif", False, INK, 21, 1.36),
    ("4. Zet daarna je schoen: met een verlanglijstje erin（然後擺出鞋子，裡面放願望清單）", "serif", False, INK, 21, 1.36),
])
f.gloss("het verlanglijstje 願望清單 · de verslaggever 記者 · de proef 考驗 · stemmen 投票 · de aflevering 集。")
f.end_report()

# col 3: facts + en jij (sequential, measured; no photo this page)
ix = COLX[3]
facts = ["Expeditie Robinson: 19 kandidaten; elke zondag 20:00 uur, RTL 4.",
         "34 dagen op een onbewoond eiland in Maleisië; presentatie: Nicolette Kluijver en Edson da Graça.",
         "Na de intocht (15 november) mag de schoen, met een wortel en een verlanglijstje."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 64
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "JONGEREN IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Kijk jij zondag naar Expeditie Robinson, of zet je liever je schoen met een verlanglijstje? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("週日你要看《魯濱遜遠征》，還是寧願擺出裝著願望清單的鞋子？用荷蘭語寫兩個句子寄來。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ? · 你呢？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "週日你要看《魯濱遜遠征》，還是寧願擺出裝著願望清單的鞋子？用荷蘭語寫兩個句子寄來。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "OEFENINGEN · 第 5 版練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案在第 8 版 · 題目程度混編，按題號找", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · BEGRIJPEN", 25)
e.expl("讀第 5 版文章，選出正確答案。")
e.ex("B1", "單選", "B", "《魯濱遜遠征》每週日 20:00 在 RTL 4 播出",
     "Expeditie Robinson is elke zondag om... A. 18:00 uur · B. 20:00 uur · C. 12:00 uur", size=20, gap=8)
e.ex("B1", "單選", "A", "19 位參賽者",
     "Expeditie Robinson heeft ___ kandidaten. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "單選", "C", "節目在馬來西亞的荒島上拍攝",
     "De kandidaten leven op een eiland in... A. Spanje · B. Grave · C. Maleisië", size=20, gap=8)
e.ex("B1", "單選", "B", "參賽者在島上待 34 天",
     "De kandidaten blijven ___ dagen op het eiland. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "單選", "A", "願望清單放進鞋子裡",
     "Jongeren zetten hun schoen met... A. een verlanglijstje · B. een boek · C. een lampion", size=20, gap=8)
e.head("B · WOORDEN UIT DE TEKST", 25)
e.expl("用方框裡的詞填空。")
e.para("verlanglijstje · verslaggever · proef · stemmen · aflevering · kandidaat", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "verlanglijstje", "verlanglijstje = 願望清單 (het)",
     "In mijn schoen zit een ___ met drie wensen.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "verslaggever", "verslaggever = 記者 (de)",
     "Camille Vanuxem is de ___ van het programma.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "proef", "proef = 考驗 (de)",
     "Wie een ___ verliest, kan naar huis gaan.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "stemmen", "stemmen = 投票",
     "De kandidaten ___ wie naar huis moet.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "aflevering", "aflevering = 集",
     "Zondag is er een nieuwe ___ van Robinson.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "kandidaten", "kandidaat 複數：kandidaten",
     "Er zijn 19 ___ op het eiland.", instr="填空", size=20, gap=8)
e.head("C · DE TOEKOMST MET GAAN", 25)
e.expl("用 gaan + 不定詞談論未來。")
e.ex("B1", "完成句子", "gaat winnen", "gaat winnen = 會贏（只是猜測）",
     "Wie ___ (winnen) Expeditie Robinson, denk je?", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaan kijken", "wij → gaan + 不定詞 kijken",
     "Wij ___ (kijken) zondag naar de nieuwe aflevering.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaat zetten", "hij → gaat zetten",
     "Hij ___ (zetten) zondagavond zijn schoen.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaan schrijven", "zij（複數）→ gaan schrijven",
     "De kinderen ___ (schrijven) een verlanglijstje.", instr="填空", size=20, gap=8)
e.head("D · WAAR OF NIET WAAR?", 25)
e.ex("B1", "判斷對錯", "Waar", "正確：節目在 11 月 1 日開播",
     "Expeditie Robinson begon op 1 november. Waar of niet waar?", instr="判斷", size=20, gap=8)
e.ex("B1", "判斷對錯", "Niet waar", "錯誤：節目在馬來西亞拍攝",
     "Expeditie Robinson speelt in Spanje. Waar of niet waar?", instr="判斷", size=20, gap=8)
e.ex("B2", "判斷對錯", "Niet waar", "錯誤：鞋子裡的胡蘿蔔是給馬的",
     "De wortel in de schoen is voor Sinterklaas. Waar of niet waar?", instr="判斷", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jongeren.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · VERDIEPING (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERDIEPING · 深度", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · 聖馬丁節還是萬聖節？")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P6-main")
f.title("Sint-Maarten of Halloween: moet je kiezen?", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: B2")
f.para("Sint-Maarten is een oude traditie in Nederland. Kinderen lopen al meer dan honderd jaar met lampionnen langs de deuren. Halloween is nieuwer in Nederland — en het groeit: volgens onderzoeksbureau Motivaction vierde in 2025 26 procent van de Nederlanders Halloween, tegenover 21 procent een jaar eerder.")
f.para("Maar let op de cijfers: de onderzoeken gebruiken verschillende definities en zijn daarom niet rechtstreeks vergelijkbaar. En een lege stoep betekent niet automatisch dat Sint-Maarten verdwijnt. In sommige plaatsen verplaatst de viering zich naar winkelcentra en georganiseerde optochten, waar kinderen samen langs deelnemende winkels lopen.")
f.para("Deskundigen zien Sint-Maarten niet verdwijnen. Antropoloog Irene Stengs van het Meertens Instituut zei in 2025 dat de belangstelling voor Sint-Maarten is toegenomen. Traditiedeskundige Ineke Strouken ziet geen duidelijke landelijke achteruitgang. Het feest verandert, zeggen zij — het verdwijnt niet.")
f.para("De twee feesten zijn ook anders. Halloween draait om griezelen en verkleden; Sint-Maarten draait om delen en aandacht voor anderen. Veel kinderen doen allebei: griezelen op 31 oktober, zingen op 11 november. Kiezen hoeft niet — het zijn twee feesten, in twee weken, met twee soorten licht.")
f.para("Een traditie leeft als mensen haar blijven vieren. Op straat, in het winkelcentrum of allebei: de lampion gaat aan als het donker wordt, en het liedje klinkt bij elke deur.")
f.head("VOOR OF TEGEN KIEZEN?", 25)
f.para("Voorstanders van kiezen zeggen: één feest is genoeg, anders wordt november één lange verkleedweek. Tegenstanders zeggen: feesten groeien naast elkaar, zoals talen naast elkaar groeien. De krant kiest niet: vier wat je viert — maar zing op 11 november in ieder geval één liedje.")
f.gloss("de traditie 傳統 · griezelen 嚇人 · de belangstelling 關注· de achteruitgang 衰退 · de deskundige 專家。")
f.end_report()

# col 3: OEFENDATA chart + pro/contra box (sequential, measured)
ix = COLX[3]
rows = [
    ("Ik loop met een lampion", "40", 160),
    ("Ik vier Halloween", "25", 100),
    ("Ik doe allebei", "20", 80),
    ("Ik blijf thuis", "15", 60),
]
cap = "OEFENDATA — verzonnen cijfers om mee te oefenen, geen echte enquête. Vraag: wat doe jij rond 11 november? (100 jongeren)"
capcn = "練習數據：虛構數字，僅供練習，非真實調查。問題：11 月 11 日前後你做什麼？（100 位年輕人）"
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
    ("Voor kiezen: één feest is genoeg in november.", "serif", False, INK, 21, 1.4),
    ("Tegen kiezen: feesten groeien naast elkaar, zoals talen.", "serif", False, INK, 21, 1.4),
    ("De krant kiest niet: vier wat je viert. En zing op 11 november één liedje. En jij?", "serif", False, INK, 21, 1.4),
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
p.text(RIGHT, ey + 28, "答案在第 8 版 · 題目程度混編，按題號找", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LEES DE GRAFIEK", 25)
e.expl("根據第 6 版圖表（練習數據）回答。")
e.ex("B2", "完成句子", "40", "40 位年輕人提著燈籠走",
     "___ van de 100 jongeren lopen met een lampion.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "25", "25 人慶祝萬聖節",
     "___ jongeren vieren Halloween.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "60", "40 + 20 = 60",
     "Lampion lopen en allebei samen: ___ jongeren.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "15", "15 人待在家裡",
     "___ jongeren blijven thuis.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "100", "圖表共 100 人：40+25+20+15",
     "De grafiek telt in totaal ___ jongeren.", instr="填空", size=21.5, gap=9)
e.head("B · BEGRIJPEN", 25)
e.expl("讀第 6 版文章，選出正確答案。")
e.ex("B2", "單選", "B", "2025 年，26% 的荷蘭人慶祝了萬聖節",
     "Volgens Motivaction vierde in 2025 ___ procent Halloween. A. 21 · B. 26 · C. 11", size=21.5, gap=9)
e.ex("B2", "單選", "B", "兩項調查的定義不同，所以不能直接比較",
     "De onderzoeken zijn... A. precies hetzelfde · B. niet rechtstreeks vergelijkbaar · C. allebei fout", size=21.5, gap=9)
e.ex("B2", "單選", "C", "人們對聖馬丁節的興趣增加了（Stengs，2025 年）",
     "Irene Stengs zei in 2025 dat de belangstelling voor Sint-Maarten... A. verdween · B. gelijk bleef · C. is toegenomen", size=21.5, gap=9)
e.ex("B2", "單選", "A", "萬聖節是嚇人；聖馬丁節是分享",
     "Halloween draait om griezelen; Sint-Maarten draait om... A. delen · B. voetbal · C. boeken", size=21.5, gap=9)
e.ex("B2", "單選", "B", "傳統會一直活下去，只要人們繼續慶祝它",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=21.5, gap=9)
e.head("C · WOORDEN", 25)
e.expl("用方框裡的詞填空。")
e.para("traditie · griezelen · belangstelling · achteruitgang", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B2", "完成句子", "traditie", "traditie = 傳統 (de)",
     "Sint-Maarten is een oude ___.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "griezelen", "griezelen = 嚇人",
     "Met Halloween gaan kinderen ___ en zich verkleden.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "belangstelling", "belangstelling = 關注 (de)",
     "De ___ voor Sint-Maarten is toegenomen.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "achteruitgang", "achteruitgang = 衰退 (de)",
     "Strouken ziet geen duidelijke landelijke ___.", instr="填空", size=21.5, gap=9)
e.head("D · MAAK DE ZINNEN", 25)
e.expl("把詞語排成正確的順序，組成句子。")
e.ex("B2", "造句", "Sint-Maarten is een oude traditie in Nederland.", "主詞 + 動詞 + 補語 + 地點",
     "sint-maarten / is / een oude traditie / in nederland → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "De kinderen lopen met lampionnen langs de deuren.", "主詞 + 動詞 + 方式 + 地點",
     "de kinderen / lopen / met lampionnen / langs de deuren → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "Een traditie leeft als mensen haar blijven vieren.", "als 子句放在最後",
     "een traditie / leeft / als mensen haar blijven vieren → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "Kiezen hoeft niet: het zijn twee feesten.", "kiezen + hoeft niet + 解釋",
     "kiezen / hoeft niet / het zijn twee feesten → ___", instr="造句", size=21.5, gap=9)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-verdieping.svg")
print("P6 saved, exercises so far:", len(REG))
