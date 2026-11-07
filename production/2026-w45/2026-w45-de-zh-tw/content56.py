# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUGEND · 青年", "Die Lucerna", "LEVEL B1 · Zurück in die Schule · 重返校園")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P5-main")
f.title("Zurück in die Schule — und Bayern hat noch frei", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B1")
f.para("Am Montag, dem 2. November, war es in Baden-Württemberg wieder so weit: Die Schule hat nach den Herbstferien wieder begonnen. Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut — und die ersten Klassenarbeiten kommen bald.")
f.para("In Bayern dagegen ist die Woche noch frei: Dort dauern die Herbstferien in dieser Woche noch an. Wer in München wohnt, kann noch ausschlafen — wer in Stuttgart wohnt, muss schon wieder früh aufstehen. Ein Land, zwei Wochen: So unterschiedlich sind die Ferien in Deutschland.")
f.para("Was macht man in der ersten Schulwoche? Die Lehrerinnen und Lehrer fragen nach den Ferien, die Hefte sind neu, und die Pläne für den Winter stehen schon: Klassenarbeiten, Referate — und bald die ersten Proben für die Weihnachtsfeier.")
f.para("Und nach der Schule? Der Herbst ist die Zeit der Bibliotheken und der Sporthallen: Lesen, was man in den Ferien begonnen hat, oder ein neues Hobby probieren. Unser Tipp: Suchen Sie sich ein Buch für die dunklen Abende — die Bibliotheken haben im November oft neue Bücher und Lesungen.")
f.para("Auch der Sport gehört zur Woche: Am Samstag und Sonntag spielt die Bundesliga — für viele Jugendliche der Ausflug des Wochenendes. Wer in Bayern noch Ferien hat, kann sogar am Freitag schon ins Stadion. Mehr dazu auf Seite 4.")
f.gloss("der Pausenhof 課間操場 · die Klassenarbeit 課堂測驗 · das Referat 課堂報告 · ausschlafen 睡懶覺 · die Probe 排練。")
f.end_report()

# col 3: facts + vocab + Und Sie (hand-rolled; CORRECTED height formula — see KIT §geometry)
ix = COLX[3]
facts = ["Baden-Württemberg: Am 2. November hat die Schule wieder begonnen.",
         "Bayern: Die Herbstferien dauern in dieser Woche noch an.",
         "Ein Land, zwei Wochen: So unterschiedlich sind die Ferien in Deutschland."]
sy3 = 200
sh = 45 + 33 * len(facts) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in facts)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "FERIENWECHSEL · 假期交接", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 facts ends", sy3 + sh)
words = ["der Pausenhof — 課間操場", "die Klassenarbeit — 課堂測驗", "das Referat — 課堂報告",
         "der Rucksack — 書包", "ausschlafen — 睡懶覺", "die Probe — 排練"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SCHULWÖRTER · 校園詞彙", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Wann hat Ihre Schule nach den Ferien wieder begonnen? Und was war Ihr erstes Fach? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("你的學校假期後哪天開學？第一節是什麼課？寫兩句德語寄來。", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE? · 說說你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你的學校假期後哪天開學？第一節是什麼課？寫兩句德語寄來。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- Wochenplan wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "DER WOCHENPLAN DER REDAKTION · 編輯部一週計劃", 24, "sans", True, OLIVE)
planrows = [
    ("Mo 2.11.", "Baden-Württemberg: erster Schultag nach den Ferien."),
    ("Di 3.11.", "Champions League am Abend: Bayern bei Atlético (21.00 Uhr)."),
    ("Mi 4.11.", "Dortmund gegen Betis, Leipzig gegen City (21.00 Uhr)."),
    ("Do 5.11.", "Europa League: Hoffenheim bei Crystal Palace (18.45 Uhr)."),
    ("Fr 6.11.", "Bundesliga: Hamburg gegen Gladbach (20.30 Uhr)."),
]
pyy = 1184
for t, txt in planrows:
    p.text(sx + 24, pyy + 24, t, 21, "sans", True, BRICK)
    p.text(sx + 190, pyy + 24, txt, 21.5, "serif", False, INK)
    pyy += 45

# ---- P5 exercises ----
ey = 1500
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · 第 5 版練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · LESEVERSTEHEN", 25)
e.expl("讀第 5 版文章，選出正確答案。")
e.ex("B1", "單選", "A", "BW 11 月 2 日開學",
     "In Baden-Württemberg beginnt die Schule am... A. 2. November · B. 8. November · C. 31. Oktober", size=20, gap=8)
e.ex("B1", "單選", "B", "巴伐利亞假期未結束",
     "In Bayern sind die Ferien... A. vorbei · B. noch nicht vorbei · C. erst im Dezember", size=20, gap=8)
e.ex("B1", "單選", "B", "開學週有課堂測驗",
     "Was kommt bald in der Schule? A. die Sommerferien · B. die ersten Klassenarbeiten · C. der Abiball", size=20, gap=8)
e.ex("B1", "單選", "B", "Referat = 課堂報告",
     "Was ist ein Referat? A. ein Buch · B. ein Vortrag in der Klasse · C. ein Sportfest", size=20, gap=8)
e.ex("A2", "單選", "A", "巴伐利亞學生週五可去球場",
     "Wer kann am Freitag schon ins Stadion? A. Wer in Bayern Ferien hat. · B. Wer in Stuttgart wohnt. · C. Niemand.", size=20, gap=8)
e.head("B · WÖRTER AUS DEM TEXT", 25)
e.expl("用方框裡的詞填空。")
e.para("Pausenhof · Klassenarbeit · Referat · ausschlafen · Probe · Rucksack", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "Pausenhof", "課間操場上玩",
     "In der Pause spielen die Kinder auf dem ___.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "Klassenarbeit", "數學課堂測驗",
     "Am Freitag schreiben wir eine ___ in Mathe.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "Referat", "報告要讀三本書",
     "Für das ___ muss ich drei Bücher lesen.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "ausschlafen", "假期可以睡懶覺",
     "In den Ferien kann man lange ___.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Probe", "聖誕演出的第一次排練",
     "Für die Weihnachtsfeier gibt es schon die erste ___.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Rucksack", "書包裡有本子鉛筆",
     "Mein ___ ist gepackt: Hefte, Stifte, Pausenbrot.", instr="填空", size=20, gap=8)
e.head("C · SÄTZE MIT «WEIL»", 25)
e.expl("用 weil 連接兩個句子（動詞放句末）。")
e.ex("B1", "句型轉換", "Die Kinder freuen sich, weil die Schule wieder beginnt.", "weil 句動詞置尾",
     "Die Kinder freuen sich. Die Schule beginnt wieder. (weil) → ___", instr="改寫", size=20, gap=8)
e.ex("B1", "句型轉換", "Er liest ein Buch, weil es draußen kalt ist.", "ist 置尾",
     "Er liest ein Buch. Es ist draußen kalt. (weil) → ___", instr="改寫", size=20, gap=8)
e.ex("B1", "句型轉換", "Sie geht in die Bibliothek, weil sie ein Referat schreiben muss.", "muss 置尾",
     "Sie geht in die Bibliothek. Sie muss ein Referat schreiben. (weil) → ___", instr="改寫", size=20, gap=8)
e.ex("B1", "句型轉換", "Bayern hat noch Ferien, weil die Ferien dort später liegen.", "liegen 置尾",
     "Bayern hat noch Ferien. Die Ferien liegen dort später. (weil) → ___", instr="改寫", size=20, gap=8)
e.head("D · RICHTIG ODER FALSCH?", 25)
e.expl("判斷對錯。")
e.ex("A2", "判斷對錯", "Richtig", "BW 11 月 2 日複課",
     "In Baden-Württemberg hat die Schule am 2. November wieder begonnen. Richtig oder falsch?", instr="判斷", size=20, gap=8)
e.ex("B1", "判斷對錯", "Falsch", "全德假期並未都結束",
     "In ganz Deutschland sind die Herbstferien vorbei. Richtig oder falsch?", instr="判斷", size=20, gap=8)
e.ex("A2", "判斷對錯", "Richtig", "開學週有測驗與報告",
     "Die erste Schulwoche bringt Klassenarbeiten und Referate. Richtig oder falsch?", instr="判斷", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jugend.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERTIEFUNG · 深讀", "Die Lucerna", "LEVEL B2 · Pflege & Stromsteuer · 護理與電力稅")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P6-main")
f.title("Pflege zu Hause: Wer hilft den Angehörigen?", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B2")
f.para("Am Montag, dem 26. Oktober, um 21.00 Uhr diskutierte die ARD-Sendung „Hart aber fair“: „Pflege zu Hause — Lässt die Politik Angehörige allein?“ Nach Angaben der Sendung brauchen in Deutschland mehr als sechs Millionen Menschen Pflege. Die meisten von ihnen werden zu Hause gepflegt — von rund zehn Millionen Angehörigen.")
f.para("Was heißt „pflegen“ im Alltag? Morgens helfen beim Aufstehen, beim Waschen und Anziehen, beim Essen und bei den Medikamenten — und nachts wach sein, wenn etwas passiert. Viele Angehörige machen das neben dem Beruf, und viele sind selbst schon alt.")
f.para("Die Politik streitet seit Jahren über die Antwort: mehr Geld für die Pflegeversicherung? Mehr Pflegedienste, die zu Hause helfen? Mehr freie Tage für pflegende Angehörige? Die Debatte ist schwierig, weil alles Geld kostet — und weil die Zahl der Pflegebedürftigen weiter steigt.")
f.para("Zweites Thema der Woche: die Stromsteuer. Union und SPD sind sich hier „weiter weit auseinander“, wie es in der Tagesschau heißt: Die eine Seite will die Steuer für alle senken, die andere nur gezielt. Auch der ZEW-Index zeigt, wie wichtig die Frage ist: Die Lage wird etwas besser eingeschätzt (minus 35,9 nach minus 47,1), aber die Erwartungen fielen im Oktober auf 28,1 Punkte.")
f.para("Und was sagt der Präsident des ZEW, Achim Wambach? „Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.“ Mit anderen Worten: Es geht langsam aufwärts — aber von allein geht es nicht.")
f.para("Zwei Debatten, ein Muster: Beide kosten Geld und betreffen fast jeden Haushalt.")
f.gloss("der Angehörige 親屬 · die Pflegeversicherung 護理保險 · der Pflegedienst 護理服務機構 · die Stagnation 停滯 · der Aufschwung 復甦。")
f.end_report()

# col 3: numbers box + debate box (measured)
ix = COLX[3]
tl = [("6 Mio.", "Menschen in Deutschland brauchen Pflege (ARD „Hart aber fair“, 26. Okt.)."),
      ("10 Mio.", "Angehörige pflegen zu Hause (rund; ARD „Hart aber fair“, 26. Okt.)."),
      ("28,1", "ZEW-Erwartungen im Oktober (minus 6,6 Punkte)."),
      ("−35,9", "ZEW-Lageindex (plus 11,2 Punkte)."),
      ("14,04", "Cent pro Liter: so viel Steuer weniger beim Tanken."),
      ("2,5 Mrd.", "so viel kostet der Tankrabatt den Staat.")]
tlh = 45 + 30.5 * len(tl) + 29.11 * sum(len(wrap(t, "serif", False, 20.5, CW - 152)) for yr, t in tl)
p.rect(ix, 200, CW, tlh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DIE ZAHLEN · 本週數字", 24, "sans", True, OLIVE)
yy3 += 52
for yr, t in tl:
    p.text(ix + 22, yy3 + 21, yr, 21, "sans", True, BRICK)
    yy3 = p.para(ix + 130, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 152, 1.42) + 10
print("P6 col3 numbers ends", 200 + tlh)
deb = "Pflege: Wer zu Hause pflegt, braucht mehr Hilfe — darüber streitet die Politik. Stromsteuer: Wie stark sie sinkt, ist noch offen. Beides kostet Geld, beides betrifft fast jeden Haushalt."
hy3 = 200 + tlh + 26
hh = 140 + 29.82 * len(wrap(deb, "serif", False, 21, CW - 44)) + 27.69 * (len(wrap("護理：在家護理需要更多幫助——對此政界仍在爭論。電力稅：降多少尚未確定。兩者都花錢，都關係到幾乎每個家庭。", "sans", False, 19.5, CW - 44)) - 1)
p.rect(ix, hy3, CW, hh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = hy3 + 16
p.text(ix + 22, yy3 + 26, "DIE DEBATTE IN EINEM SATZ", 22.5, "sans", True, OLIVE)
yy3 += 50
yy3 = p.para(ix + 22, yy3 + 21, deb, 21, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "護理：在家護理需要更多幫助——對此政界仍在爭論。電力稅：降多少尚未確定。兩者都花錢，都關係到幾乎每個家庭。", 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", hy3 + hh)

# ---- Pro & Contra wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 252, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "PRO & CONTRA · 正方與反方 — die Argumente der Debatte", 24, "sans", True, OLIVE)
p.text(sx + 24, 1210, "PRO — MEHR HILFE FÜR ANGEHÖRIGE", 21, "sans", True, BRICK)
p.text(sx + 24 + (swd - 48) // 2, 1210, "CONTRA — GEGEN MEHR GELD", 21, "sans", True, BRICK)
pro = ["Angehörige kennen den Menschen am besten — Hilfe zu Hause ist menschlicher.",
       "Ein Heimplatz kostet viel mehr als Hilfe zu Hause."]
contra = ["Professionelle Pflege ist sicherer — Angehörige sind oft überfordert.",
          "Der Staat hat nicht genug Geld für alles."]
pyy = 1232
for t in pro:
    pyy2 = p.para(sx + 24, pyy + 20, "· " + t, 20.5, "serif", False, INK, (swd - 72) // 2, 1.4)
    pyy = max(pyy, pyy2) + 8
pyy = 1232
for t in contra:
    pyy2 = p.para(sx + 24 + (swd - 48) // 2, pyy + 20, "· " + t, 20.5, "serif", False, INK, (swd - 72) // 2, 1.4)
    pyy = max(pyy, pyy2) + 8

# ---- practice chart (full width) ----
cy = 1420
p.hline(MX, RIGHT, cy - 12, GOLD, 2)
p.text(MX, cy + 28, "WER PFLEGT ZU HAUSE? · 誰在家護理？", 26, "sans", True, OLIVE)
bars = [("pflegen Angehörige zu Hause", 68, "家屬護理"),
        ("nutzen einen Pflegedienst", 20, "專業到府"),
        ("leben im Pflegeheim", 12, "住養老院")]
byy = cy + 58
for lab, v, zh in bars:
    p.text(MX, byy + 26, lab, 22, "serif", True, INK)
    p.text(MX + 360, byy + 26, zh, 20, "sans", False, GREY)
    p.rect(MX + 470, byy + 4, v * 17, 30, fill=OLIVE)
    p.text(MX + 470 + v * 17 + 16, byy + 26, f"{v} %", 22, "sans", True, BRICK)
    byy += 52
p.text(MX, byy + 22, "ÜBUNGSDATEN · 練習數據 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本圖數字為編輯部練習示例，非真實調查。）", 19.5, "sans", False, GREY)

# ---- P6 exercises ----
ey = 1808
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · 第 6 版練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · DAS DIAGRAMM LESEN", 25, gap=9)
e.expl("看上面的練習圖表，選出正確答案。")
e.ex("B1", "單選", "A", "68% 家屬護理",
     "Wie viele Prozent pflegen Angehörige zu Hause (Übungsdaten)? A. 68 % · B. 20 % · C. 12 %", size=20, gap=7)
e.ex("B1", "單選", "B", "專業到府 20% 第二",
     "Was ist die zweitgrößte Gruppe? A. Pflegeheim · B. Pflegedienst · C. Angehörige", size=20, gap=7)
e.ex("B1", "單選", "B", "68+20=88",
     "Angehörige und Pflegedienst zusammen sind... A. 80 % · B. 88 % · C. 90 %", size=20, gap=7)
e.ex("B2", "單選", "B", "養老院 12% 最小",
     "Welche Gruppe ist kleiner? A. Pflegedienst · B. Pflegeheim · C. beide gleich", size=20, gap=7)
e.ex("B1", "單選", "A", "養老院 12%",
     "Wie viele Prozent leben im Pflegeheim? A. 12 % · B. 20 % · C. 68 %", size=20, gap=7)
e.ex("B2", "單選", "B", "68+20+12=100",
     "Die drei Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 %", size=20, gap=7)
e.head("B · LESEVERSTEHEN (B2)", 25, gap=9)
e.expl("讀第 6 版深讀文章，選出正確答案。")
e.ex("B2", "單選", "B", "10 月 26 日節目討論居家護理",
     "Was diskutierte „Hart aber fair“ in der Sendung am 26. Oktober? A. den Tankrabatt · B. die Pflege zu Hause · C. die Stromsteuer", size=20, gap=7)
e.ex("B2", "單選", "A", "據 ARD《Hart aber fair》10 月 26 日節目，600 多萬人需要護理",
     "Wie viele Menschen brauchen Pflege? A. mehr als sechs Millionen · B. rund eine Million · C. zehn Millionen", size=20, gap=7)
e.ex("B2", "單選", "B", "家屬居家護理",
     "Wer pflegt zu Hause? A. die Ärzte · B. die Angehörigen · C. die Politiker", size=20, gap=7)
e.ex("B1", "單選", "B", "據 ARD《Hart aber fair》10 月 26 日節目，約 1000 萬人護理親屬",
     "Wie viele Menschen pflegen einen Verwandten (rund)? A. sechs Millionen · B. zehn Millionen · C. zwei Millionen", size=20, gap=7)
e.head("C · GRAMMATIK", 25, gap=9)
e.expl("用括號裡的形式填空。")
e.ex("B2", "完成句子", "wird", "被動：wird + Partizip II",
     "Die Frage ___ (werden) am Montag diskutiert.", instr="填空", size=20, gap=7)
e.ex("B2", "完成句子", "ob", "ob 引導間接疑問句",
     "Die Politik weiß nicht, ___ das Geld reicht.", instr="填空", size=20, gap=7)
e.ex("B1", "完成句子", "steigt", "steigen → steigt",
     "Die Zahl der Pflegebedürftigen ___ (steigen) weiter.", instr="填空", size=20, gap=7)
e.ex("B2", "完成句子", "sagte", "sagen 過去時 sagte",
     "Wambach ___ (sagen): Der Aufschwung trägt sich nicht selbst.", instr="填空", size=20, gap=7)
e.head("D · WÖRTER DER DEBATTE", 25, gap=9)
e.expl("用方框裡的詞填空。")
e.para("Pflegeversicherung · Angehörige · Stagnation · Aufschwung", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "Pflegeversicherung", "護理保險出更多錢",
     "Die ___ soll mehr Geld für die Pflege zahlen.", instr="填空", size=20, gap=7)
e.ex("B2", "完成句子", "Angehörige", "親屬居家護理",
     "Viele ___ pflegen ihre Verwandten zu Hause.", instr="填空", size=20, gap=7)
e.ex("B2", "完成句子", "Stagnation", "走出停滯",
     "Die Wirtschaft kommt langsam aus der ___ heraus.", instr="填空", size=20, gap=7)
e.ex("B1", "完成句子", "Aufschwung", "復甦尚未自我維持",
     "Der ___ trägt sich noch nicht selbst.", instr="填空", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-vertiefung.svg")
print("P6 saved, exercises so far:", len(REG))
