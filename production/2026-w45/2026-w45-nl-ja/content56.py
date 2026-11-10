# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JONGEREN (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JONGEREN　若者", "De Lucerna", "NIVEAU B1　Robinson is begonnen, ADE en DDW voorbij　ロビンソン開幕、ADEとDDW閉幕")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Expeditie Robinson is begonnen!", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur. Negentien kandidaten leven op een onbewoond eiland. De eerste aflevering is geweest — nu begint het echte spel: vuur maken, eten zoeken, proeven winnen.")
f.para("De kandidaten slapen buiten en moeten alles zelf doen. Wie een proef verliest, kan naar huis worden gestemd. Wie het langst blijft, wint de expeditie. De kandidaten komen uit Nederland en Vlaanderen, en ze kennen elkaar nog niet allemaal.")
f.para("Twee festivals zijn intussen voorbij. ADE en de Dutch Design Week sloten allebei op zondag 25 oktober. ADE werd dertig jaar, met meer dan 3.000 artiesten op meer dan 200 locaties in Amsterdam. De Design Week in Eindhoven toonde werk van ongeveer 2.500 ontwerpers.")
f.para("Wat blijft er over? De muziek van ADE, de ideeën van de Design Week — en de vraag wie Robinson wint. Daarover lees je volgende week meer. En deze week is er genoeg te doen: het is Klimaatweek, dus ga naar buiten, plant iets groens of fiets naar de Snuffelmarkt in Zaandam.")
f.head("JONGEREN EN HET KLIMAAT", 25)
f.para("Jongeren doen veel in de Klimaatweek: fietsen in plaats van rijden, tweedehands kopen in plaats van nieuw, minder plastic gebruiken. Kleine keuzes, zeggen klimaatclubs, maar als miljoenen jongeren ze maken, tellen ze op.")
f.box("ZO KIJK JE ROBINSON", [
    ("1. Kijk zondag om 20:00 uur op RTL 4（日曜夜20:00にRTL 4で見る）", "serif", False, INK, 21, 1.36),
    ("2. Let op de proeven: daar worden de punten verdeeld（競技に注目：得点はそこで決まる）", "serif", False, INK, 21, 1.36),
    ("3. Raad met vrienden wie het langst blijft（友だちと最後まで残る人を予想）", "serif", False, INK, 21, 1.36),
    ("4. Volgende week lees je hier hoe het verder ging（来週ここで続きを報道）", "serif", False, INK, 21, 1.36),
])
f.gloss("het eiland 島 · de proef 競技・試練 · stemmen 投票する · de aflevering （1）話 · voorbij 終わった。")
f.end_report()

# col 3: facts + en jij (sequential, measured; no photo this page)
ix = COLX[3]
facts = ["Expeditie Robinson: 19 kandidaten; start zondag 1 november, 20:00 uur, RTL 4.",
         "ADE 30 jaar: meer dan 3.000 artiesten, meer dan 200 locaties; gesloten zondag 25 oktober.",
         "Dutch Design Week: ongeveer 2.500 ontwerpers; gesloten zondag 25 oktober."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "JONGEREN IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Kijk jij naar Expeditie Robinson, of doe je liever zelf iets buiten? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("『エクスペディティ・ロビンソン』を見る？それとも自分で外に出かける方が好き？オランダ語で2文書いて送ってください。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ?　あなたは?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "『エクスペディティ・ロビンソン』を見る？それとも自分で外に出かける方が好き？オランダ語で2文書いて送ってください。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　5ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　問題はレベル混合、番号で探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　BEGRIJPEN", 25)
e.expl("5ページの記事を読んで正しい答えを選んでください。")
e.ex("B1", "選択問題", "B", "ロビンソンは11月1日（日）に開始",
     "Expeditie Robinson begon op... A. zondag 25 oktober · B. zondag 1 november · C. woensdag 21 oktober", size=20, gap=8)
e.ex("B1", "選択問題", "A", "19人の参加者",
     "Expeditie Robinson heeft ___ kandidaten. A. 19 · B. 30 · C. 200", size=20, gap=8)
e.ex("B1", "選択問題", "C", "ADE は今年30年",
     "ADE werd dit jaar... A. 25 jaar · B. 26 jaar · C. 30 jaar", size=20, gap=8)
e.ex("B1", "選択問題", "B", "デザインウィークは約2,500人のデザイナー",
     "De Design Week toonde werk van ongeveer... A. 250 ontwerpers · B. 2.500 ontwerpers · C. 3.000 ontwerpers", size=20, gap=8)
e.ex("B1", "選択問題", "A", "ADE と DDW は10月25日（日）に閉幕",
     "ADE en de Design Week sloten op... A. zondag 25 oktober · B. zondag 1 november · C. zaterdag 7 november", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.expl("枠内の単語で空所を補充してください。")
e.para("eiland · proef · stemmen · aflevering · voorbij · kandidaat", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "文の完成", "eiland", "eiland = 島（het）",
     "Robinson speelt op een onbewoond ___.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "proef", "proef = 競技・試練（de）",
     "Wie een ___ verliest, kan naar huis gaan.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "stemmen", "stemmen = 投票する",
     "De kandidaten ___ wie naar huis moet.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "aflevering", "aflevering = （1）話",
     "De eerste ___ was zondag 1 november.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "voorbij", "voorbij = 終わった",
     "ADE is ___: het festival is afgelopen.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "kandidaten", "kandidaat 複数形：kandidaten",
     "Er zijn 19 ___ op het eiland.", instr="空所補充", size=20, gap=8)
e.head("C　DE TOEKOMST MET GAAN", 25)
e.expl("gaan + 不定詞で未来を表してください。")
e.ex("B1", "文の完成", "gaat winnen", "gaat winnen = 勝つだろう（推測）",
     "Wie ___ (winnen) Expeditie Robinson, denk je?", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "gaan kijken", "wij → gaan + 不定詞 kijken",
     "Wij ___ (kijken) zondag naar de nieuwe aflevering.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "gaat praten", "hij → gaat praten",
     "Hij ___ (praten) morgen met vrienden over de proef.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "gaan zoeken", "zij（複数）→ gaan zoeken",
     "De kandidaten ___ (zoeken) morgen eten op het eiland.", instr="空所補充", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "正誤判断", "Waar", "正：11月1日に開始",
     "Expeditie Robinson begon op 1 november. Waar of niet waar?", instr="正誤", size=20, gap=8)
e.ex("B1", "正誤判断", "Niet waar", "誤：ADE は今年30年",
     "ADE werd dit jaar 26 jaar. Waar of niet waar?", instr="正誤", size=20, gap=8)
e.ex("B2", "正誤判断", "Niet waar", "誤：10月25日に閉幕済み",
     "De Design Week is nog bezig. Waar of niet waar?", instr="正誤", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jongeren.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · VERDIEPING (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERDIEPING　深掘り", "De Lucerna", "NIVEAU B2　De codes van het KNMI　KNMIの警報を深掘り")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P6-main")
f.title("Geel, oranje, rood: hoe werken de codes?", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B2")
f.para("Het KNMI waarschuwt Nederland al jaren met kleuren. Maar de waarschuwingen zijn veranderd: vroeger golden ze voor een hele provincie, nu zijn ze lokaal. Dat betekent: jouw stad kan code oranje hebben, terwijl het twintig kilometer verderop rustig is.")
f.para("Waarom lokaal? Omdat het weer lokaal is. Een zware bui kan over één stad vallen en de buurstad overslaan. Een waarschuwing voor een hele provincie waarschuwt dan mensen die niets merken — en die letten de volgende keer minder op. Meteorologen noemen dat waarschuwingsmoeheid.")
f.para("De kleuren zelf zijn simpel. Geel: het weer kan gevaarlijk zijn, let op. Oranje: het weer ís gevaarlijk, bereid je voor — zet losse spullen vast, rijd voorzichtig. Rood: het weer is zeer gevaarlijk, ga niet de weg op als het niet moet. Rood komt weinig voor.")
f.para("Het systeem heeft ook kritiek: sommige mensen vinden de codes verwarrend — wat is het verschil tussen geel en oranje als je toch naar buiten moet? Het KNMI antwoordt: kijk altijd naar de tekst bij de code, niet alleen naar de kleur. De tekst zegt wat er écht gebeurt, waar en wanneer.")
f.para("Voor jou als lezer is de les duidelijk. Een code is geen verbod, maar een advies. Lees de waarschuwing, kijk naar je eigen plaats en beslis zelf. En in de Klimaatweek past dat goed. Het weer is van ons allemaal, maar het raakt ons allemaal anders.")
f.head("VOOR OF TEGEN LOKAAL?", 25)
f.para("Voorstanders zeggen: lokaal is eerlijker, want alleen wie het treft, wordt gewaarschuwd. Tegenstanders zeggen: lokaal is verwarrend, want de buurstad heeft een andere kleur. Het KNMI houdt vast aan lokaal: beter precies dan algemeen, zeggen de meteorologen.")
f.gloss("de meteoroloog 気象学者 · waarschuwingsmoeheid 警報疲れ · vastzetten 固定する · het advies 助言 · de voorstander 賛成者。")
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
capcn = "練習データ：架空の数字で、練習用です。本当の調査ではありません。質問：オレンジ警報のとき、あなたはどうする？（100人の若者）"
ch = 62 + len(rows) * 58 + 14 + len(wrap(cap, "serif", False, 19, CW - 44)) * 27 + 6 + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
p.rect(ix, 200, CW, ch, fill=BOX)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DE GRAFIEK　グラフ（練習データ）", 24, "sans", True, OLIVE)
yy3 += 58
for lab, val, bw in rows:
    p.text(ix + 22, yy3 + 20, lab, 19.5, "serif", True, INK)
    p.text(ix + CW - 22, yy3 + 20, val, 19.5, "sans", True, OLIVE, anchor="end")
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
p.rect(ix, by6, CW, bh, fill="#f0eee5")
yy3 = by6 + 16
p.text(ix + 22, yy3 + 26, "VOOR OF TEGEN?　賛成か反対か", 21, "sans", True, OLIVE)
yy3 += 52
for t, k, b, fl, s, lh in bt:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.4) + 8
print("P6 col3 ends", by6 + bh)

# ---- P6 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　6ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　問題はレベル混合、番号で探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEES DE GRAFIEK", 25)
e.expl("6ページのグラフ（練習データ）を見て答えてください。")
e.ex("B2", "文の完成", "45", "45人の若者が家にいることを選ぶ",
     "Bij code oranje blijft ___ van de 100 jongeren thuis.", instr="空所補充", size=21.5, gap=9)
e.ex("B2", "文の完成", "25", "25人はまず警報の文章を読む",
     "___ jongeren kijken eerst naar de tekst.", instr="空所補充", size=21.5, gap=9)
e.ex("B2", "文の完成", "70", "45 + 25 = 70",
     "Thuis blijven en eerst de tekst lezen samen: ___ jongeren.", instr="空所補充", size=21.5, gap=9)
e.ex("B2", "文の完成", "10", "10人は分からない",
     "___ jongeren weten het niet.", instr="空所補充", size=21.5, gap=9)
e.ex("B2", "文の完成", "100", "グラフは合計100人：45+25+20+10",
     "De grafiek telt in totaal ___ jongeren.", instr="空所補充", size=21.5, gap=9)
e.head("B　BEGRIJPEN", 25)
e.expl("6ページの記事を読んで正しい答えを選んでください。")
e.ex("B2", "選択問題", "B", "以前の警報は州全体向けだった",
     "Vroeger golden waarschuwingen voor... A. één stad · B. een hele provincie · C. het hele land", size=21.5, gap=9)
e.ex("B2", "選択問題", "B", "今の警報は地域向けだ",
     "Tegenwoordig zijn waarschuwingen... A. voor het hele land · B. lokaal · C. alleen voor de kust", size=21.5, gap=9)
e.ex("B2", "選択問題", "C", "赤：非常に危険、必要がなければ外出しない",
     "Code rood betekent... A. let op · B. bereid je voor · C. zeer gevaarlijk, ga niet de weg op", size=21.5, gap=9)
e.ex("B2", "選択問題", "A", "警報疲れ：警報が多すぎて注意しなくなる",
     "Waarschuwingsmoeheid is... A. moe van waarschuwingen, dus minder opletten · B. moe van het weer · C. een nieuwe code", size=21.5, gap=9)
e.ex("B2", "選択問題", "B", "KNMI 曰く：コードの横の文章を見よ",
     "Het KNMI zegt: kijk niet alleen naar de kleur, maar naar... A. de wind · B. de tekst bij de code · C. de televisie", size=21.5, gap=9)
e.head("C　WOORDEN", 25)
e.expl("枠内の単語で空所を補充してください。")
e.para("lokaal · waarschuwingsmoeheid · vastzetten · advies", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B2", "文の完成", "lokaal", "lokaal = 地域の",
     "De waarschuwing geldt voor jouw eigen stad: ze is ___.", instr="空所補充", size=21.5, gap=9)
e.ex("B2", "文の完成", "waarschuwingsmoeheid", "waarschuwingsmoeheid = 警報疲れ",
     "Wie te vaak onnodig wordt gewaarschuwd, krijgt ___.", instr="空所補充", size=21.5, gap=9)
e.ex("B2", "文の完成", "vastzetten", "vastzetten = 固定する",
     "Bij code oranje moet je losse spullen ___.", instr="空所補充", size=21.5, gap=9)
e.ex("B2", "文の完成", "advies", "advies = 助言（het）",
     "Een code is geen verbod, maar een ___.", instr="空所補充", size=21.5, gap=9)
e.head("D　MAAK DE ZINNEN", 25)
e.expl("単語を並べて正しい文を作ってください。")
e.ex("B2", "文を作る", "De waarschuwing geldt voor jouw stad.", "主語 + 動詞 + 場所",
     "de waarschuwing / geldt / voor jouw stad → ___", instr="文を作る", size=21.5, gap=9)
e.ex("B2", "文を作る", "Kijk altijd naar de tekst bij de code.", "命令文：動詞が先頭に",
     "kijk / altijd / naar de tekst / bij de code → ___", instr="文を作る", size=21.5, gap=9)
e.ex("B2", "文を作る", "Rood komt weinig voor.", "weinig voor = めったに起こらない",
     "rood / komt / weinig / voor → ___", instr="文を作る", size=21.5, gap=9)
e.ex("B2", "文を作る", "Het weer raakt ons allemaal anders.", "raakt + 目的語 + 様態",
     "het weer / raakt / ons / allemaal anders → ___", instr="文を作る", size=21.5, gap=9)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-verdieping.svg")
print("P6 saved, exercises so far:", len(REG))
