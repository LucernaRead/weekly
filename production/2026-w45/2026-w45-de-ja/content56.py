# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUGEND　若者", "Die Lucerna", "LEVEL B1　Zurück in die Schule　学校へ戻る")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P5-main")
f.title("Zurück in die Schule — und Bayern hat noch frei", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: B1")
f.para("Am Montag, dem 2. November, war es in Baden-Württemberg wieder so weit: Die Schule hat nach den Herbstferien wieder begonnen. Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut — und die ersten Klassenarbeiten kommen bald.")
f.para("In Bayern dagegen ist die Woche noch frei: Dort dauern die Herbstferien in dieser Woche noch an. Wer in München wohnt, kann noch ausschlafen — wer in Stuttgart wohnt, muss schon wieder früh aufstehen. Ein Land, zwei Wochen: So unterschiedlich sind die Ferien in Deutschland.")
f.para("Was macht man in der ersten Schulwoche? Die Lehrerinnen und Lehrer fragen nach den Ferien, die Hefte sind neu, und die Pläne für den Winter stehen schon: Klassenarbeiten, Referate — und bald die ersten Proben für die Weihnachtsfeier.")
f.para("Und nach der Schule? Der Herbst ist die Zeit der Bibliotheken und der Sporthallen: Lesen, was man in den Ferien begonnen hat, oder ein neues Hobby probieren. Unser Tipp: Suchen Sie sich ein Buch für die dunklen Abende — die Bibliotheken haben im November oft neue Bücher und Lesungen.")
f.para("Auch der Sport gehört zur Woche: Am Samstag und Sonntag spielt die Bundesliga — für viele Jugendliche der Ausflug des Wochenendes. Wer in Bayern noch Ferien hat, kann sogar am Freitag schon ins Stadion. Mehr dazu auf Seite 4.")
f.gloss("der Pausenhof 休み時間の校庭 · die Klassenarbeit 授業内テスト · das Referat 授業での発表 · ausschlafen 朝寝坊する · die Probe 稽古。")
f.end_report()

# col 3: facts + vocab + Und Sie (hand-rolled; CORRECTED height formula — see KIT §geometry)
ix = COLX[3]
facts = ["Baden-Württemberg: Am 2. November hat die Schule wieder begonnen.",
         "Bayern: Die Herbstferien dauern in dieser Woche noch an.",
         "Ein Land, zwei Wochen: So unterschiedlich sind die Ferien in Deutschland."]
sy3 = 200
sh = 45 + 33 * len(facts) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in facts)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "FERIENWECHSEL　休暇の交代", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 facts ends", sy3 + sh)
words = ["der Pausenhof — 休み時間の校庭", "die Klassenarbeit — 授業内テスト", "das Referat — 授業での発表",
         "der Rucksack — リュック", "ausschlafen — 朝寝坊する", "die Probe — 稽古"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SCHULWÖRTER　学校の単語", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Wann hat Ihre Schule nach den Ferien wieder begonnen? Und was war Ihr erstes Fach? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("あなたの学校は休暇明けいつ始まりましたか。最初の授業は何でしたか。ドイツ語で二文送ってください。", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "あなたの学校は休暇明けいつ始まりましたか。最初の授業は何でしたか。ドイツ語で二文送ってください。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- Wochenplan wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 300, fill=BOX)
p.text(sx + 24, 1162, "DER WOCHENPLAN DER REDAKTION　編集部の一週間", 24, "sans", True, OLIVE)
planrows = [
    ("Mo 2.11.", "Baden-Württemberg: erster Schultag nach den Ferien."),
    ("Di 3.11.", "Champions League am Abend: Bayern bei Atlético (21.00 Uhr)."),
    ("Mi 4.11.", "Dortmund gegen Betis, Leipzig gegen City (21.00 Uhr)."),
    ("Do 5.11.", "Europa League: Hoffenheim bei Crystal Palace (18.45 Uhr)."),
    ("Fr 6.11.", "Bundesliga: Hamburg gegen Gladbach (20.30 Uhr)."),
]
pyy = 1184
for t, txt in planrows:
    p.text(sx + 24, pyy + 24, t, 21, "sans", True, OLIVE)
    p.text(sx + 190, pyy + 24, txt, 21.5, "serif", False, INK)
    pyy += 45

# ---- P5 exercises ----
ey = 1500
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　5ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベルは混ざっています。番号で答えを探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P5-ex")
e.head("A　LESEVERSTEHEN", 25)
e.bridge("5ページの記事を読んで、正しい答えを選ぼう。")
e.ex("B1", "選択肢", "A", "バーデン＝ヴュルテンベルクは11月2日に再開",
     "In Baden-Württemberg beginnt die Schule am... A. 2. November · B. 8. November · C. 31. Oktober", size=20, gap=8)
e.ex("B1", "選択肢", "B", "バイエルンの休暇はまだ終わっていない",
     "In Bayern sind die Ferien... A. vorbei · B. noch nicht vorbei · C. erst im Dezember", size=20, gap=8)
e.ex("B1", "選択肢", "B", "新学期の週に授業内テストがある",
     "Was kommt bald in der Schule? A. die Sommerferien · B. die ersten Klassenarbeiten · C. der Abiball", size=20, gap=8)
e.ex("B1", "選択肢", "B", "Referat = 授業での発表",
     "Was ist ein Referat? A. ein Buch · B. ein Vortrag in der Klasse · C. ein Sportfest", size=20, gap=8)
e.ex("A2", "選択肢", "A", "バイエルンの生徒は金曜に競技場へ行ける",
     "Wer kann am Freitag schon ins Stadion? A. Wer in Bayern Ferien hat. · B. Wer in Stuttgart wohnt. · C. Niemand.", size=20, gap=8)
e.head("B　WÖRTER AUS DEM TEXT", 25)
e.bridge("枠の中の単語で空所を埋めよう。")
e.para("Pausenhof · Klassenarbeit · Referat · ausschlafen · Probe · Rucksack", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "文完成", "Pausenhof", "休み時間の校庭で遊ぶ",
     "In der Pause spielen die Kinder auf dem ___.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文完成", "Klassenarbeit", "数学の授業内テスト",
     "Am Freitag schreiben wir eine ___ in Mathe.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文完成", "Referat", "発表のために三冊読む",
     "Für das ___ muss ich drei Bücher lesen.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文完成", "ausschlafen", "休暇中は朝寝坊できる",
     "In den Ferien kann man lange ___.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文完成", "Probe", "クリスマス劇の最初の稽古",
     "Für die Weihnachtsfeier gibt es schon die erste ___.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文完成", "Rucksack", "リュックの中にノートと鉛筆",
     "Mein ___ ist gepackt: Hefte, Stifte, Pausenbrot.", instr="空所補充", size=20, gap=8)
e.head("C　SÄTZE MIT «WEIL»", 25)
e.bridge("weil で二つの文をつなげよう（動詞は文末へ）。")
e.ex("B1", "文の書き換え", "Die Kinder freuen sich, weil die Schule wieder beginnt.", "weil の文では動詞が文末へ",
     "Die Kinder freuen sich. Die Schule beginnt wieder. (weil) → ___", instr="書きかえ", size=20, gap=8)
e.ex("B1", "文の書き換え", "Er liest ein Buch, weil es draußen kalt ist.", "ist が文末へ",
     "Er liest ein Buch. Es ist draußen kalt. (weil) → ___", instr="書きかえ", size=20, gap=8)
e.ex("B1", "文の書き換え", "Sie geht in die Bibliothek, weil sie ein Referat schreiben muss.", "muss が文末へ",
     "Sie geht in die Bibliothek. Sie muss ein Referat schreiben. (weil) → ___", instr="書きかえ", size=20, gap=8)
e.ex("B1", "文の書き換え", "Bayern hat noch Ferien, weil die Ferien dort später liegen.", "liegen が文末へ",
     "Bayern hat noch Ferien. Die Ferien liegen dort später. (weil) → ___", instr="書きかえ", size=20, gap=8)
e.head("D　RICHTIG ODER FALSCH?", 25)
e.bridge("正誤を判断しよう。")
e.ex("A2", "正誤判断", "Richtig", "バーデン＝ヴュルテンベルクは11月2日に再開",
     "In Baden-Württemberg hat die Schule am 2. November wieder begonnen. Richtig oder falsch?", instr="正誤", size=20, gap=8)
e.ex("B1", "正誤判断", "Falsch", "ドイツ全土で休暇が終わったわけではない",
     "In ganz Deutschland sind die Herbstferien vorbei. Richtig oder falsch?", instr="正誤", size=20, gap=8)
e.ex("A2", "正誤判断", "Richtig", "新学期の週にテストと発表がある",
     "Die erste Schulwoche bringt Klassenarbeiten und Referate. Richtig oder falsch?", instr="正誤", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jugend.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERTIEFUNG　深読み", "Die Lucerna", "LEVEL B2　Pflege & Stromsteuer　介護と電気税")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P6-main")
f.title("Pflege zu Hause: Wer hilft den Angehörigen?", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: B2")
f.para("Am Montag, dem 26. Oktober, um 21.00 Uhr diskutierte die ARD-Sendung „Hart aber fair“: „Pflege zu Hause — Lässt die Politik Angehörige allein?“ Nach Angaben der Sendung brauchen in Deutschland mehr als sechs Millionen Menschen Pflege. Die meisten von ihnen werden zu Hause gepflegt — von rund zehn Millionen Angehörigen.")
f.para("Was heißt „pflegen“ im Alltag? Morgens helfen beim Aufstehen, beim Waschen und Anziehen, beim Essen und bei den Medikamenten — und nachts wach sein, wenn etwas passiert. Viele Angehörige machen das neben dem Beruf, und viele sind selbst schon alt.")
f.para("Die Politik streitet seit Jahren über die Antwort: mehr Geld für die Pflegeversicherung? Mehr Pflegedienste, die zu Hause helfen? Mehr freie Tage für pflegende Angehörige? Die Debatte ist schwierig, weil alles Geld kostet — und weil die Zahl der Pflegebedürftigen weiter steigt.")
f.para("Zweites Thema der Woche: die Stromsteuer. Union und SPD sind sich hier „weiter weit auseinander“, wie es in der Tagesschau heißt: Die eine Seite will die Steuer für alle senken, die andere nur gezielt. Auch der ZEW-Index zeigt, wie wichtig die Frage ist: Die Lage wird etwas besser eingeschätzt (minus 35,9 nach minus 47,1), aber die Erwartungen fielen im Oktober auf 28,1 Punkte.")
f.para("Und was sagt der Präsident des ZEW, Achim Wambach? „Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.“ Mit anderen Worten: Es geht langsam aufwärts — aber von allein geht es nicht.")
f.para("Zwei Debatten, ein Muster: Beide kosten Geld und betreffen fast jeden Haushalt.")
f.gloss("der Angehörige 家族 · die Pflegeversicherung 介護保険 · der Pflegedienst 訪問介護サービス · die Stagnation 停滞 · der Aufschwung 回復。")
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
p.rect(ix, 200, CW, tlh, fill=BOX)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DIE ZAHLEN　今週の数字", 24, "sans", True, OLIVE)
yy3 += 52
for yr, t in tl:
    p.text(ix + 22, yy3 + 21, yr, 21, "sans", True, OLIVE)
    yy3 = p.para(ix + 130, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 152, 1.42) + 10
print("P6 col3 numbers ends", 200 + tlh)
deb = "Pflege: Wer zu Hause pflegt, braucht mehr Hilfe — darüber streitet die Politik. Stromsteuer: Wie stark sie sinkt, ist noch offen. Beides kostet Geld, beides betrifft fast jeden Haushalt."
hy3 = 200 + tlh + 26
hh = 140 + 29.82 * len(wrap(deb, "serif", False, 21, CW - 44)) + 27.69 * (len(wrap("介護：家での介護にもっと助けが必要です——政界ではまだ議論中です。電気税：どれだけ下がるかは未定です。どちらもお金がかかり、ほぼすべての家庭に関わります。", "sans", False, 19.5, CW - 44)) - 1)
p.rect(ix, hy3, CW, hh, fill="#f0eee5")
yy3 = hy3 + 16
p.text(ix + 22, yy3 + 26, "DIE DEBATTE IN EINEM SATZ", 22.5, "sans", True, OLIVE)
yy3 += 50
yy3 = p.para(ix + 22, yy3 + 21, deb, 21, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "介護：家での介護にもっと助けが必要です——政界ではまだ議論中です。電気税：どれだけ下がるかは未定です。どちらもお金がかかり、ほぼすべての家庭に関わります。", 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", hy3 + hh)

# ---- Pro & Contra wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 252, fill="#f0eee5")
p.text(sx + 24, 1162, "PRO & CONTRA　賛成と反対 — die Argumente der Debatte", 24, "sans", True, OLIVE)
p.text(sx + 24, 1210, "PRO — MEHR HILFE FÜR ANGEHÖRIGE", 21, "sans", True, OLIVE)
p.text(sx + 24 + (swd - 48) // 2, 1210, "CONTRA — GEGEN MEHR GELD", 21, "sans", True, OLIVE)
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
p.hline(MX, RIGHT, cy - 12, OLIVE, 2)
p.text(MX, cy + 28, "WER PFLEGT ZU HAUSE?　家で介護するのは誰？", 26, "sans", True, OLIVE)
bars = [("pflegen Angehörige zu Hause", 68, "家族の介護"),
        ("nutzen einen Pflegedienst", 20, "訪問介護"),
        ("leben im Pflegeheim", 12, "介護施設")]
byy = cy + 58
for lab, v, zh in bars:
    p.text(MX, byy + 26, lab, 22, "serif", True, INK)
    p.text(MX + 360, byy + 26, zh, 20, "sans", False, GREY)
    p.rect(MX + 470, byy + 4, v * 17, 30, fill=OLIVE)
    p.text(MX + 470 + v * 17 + 16, byy + 26, f"{v} %", 22, "sans", True, OLIVE)
    byy += 52
p.text(MX, byy + 22, "ÜBUNGSDATEN　練習データ — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（この図の数字は編集部の練習例であり、本物の調査ではありません。）", 19.5, "sans", False, GREY)

# ---- P6 exercises ----
ey = 1808
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　6ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベルは混ざっています。番号で答えを探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P6-ex")
e.head("A　DAS DIAGRAMM LESEN", 25, gap=9)
e.bridge("上の練習グラフを見て、正しい答えを選ぼう。")
e.ex("B1", "選択肢", "A", "68% 家族の介護",
     "Wie viele Prozent pflegen Angehörige zu Hause (Übungsdaten)? A. 68 % · B. 20 % · C. 12 %", size=20, gap=7)
e.ex("B1", "選択肢", "B", "訪問介護 20% が第2位",
     "Was ist die zweitgrößte Gruppe? A. Pflegeheim · B. Pflegedienst · C. Angehörige", size=20, gap=7)
e.ex("B1", "選択肢", "B", "68+20=88",
     "Angehörige und Pflegedienst zusammen sind... A. 80 % · B. 88 % · C. 90 %", size=20, gap=7)
e.ex("B2", "選択肢", "B", "介護施設 12% が最小",
     "Welche Gruppe ist kleiner? A. Pflegedienst · B. Pflegeheim · C. beide gleich", size=20, gap=7)
e.ex("B1", "選択肢", "A", "介護施設 12%",
     "Wie viele Prozent leben im Pflegeheim? A. 12 % · B. 20 % · C. 68 %", size=20, gap=7)
e.ex("B2", "選択肢", "B", "68+20+12=100",
     "Die drei Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 %", size=20, gap=7)
e.head("B　LESEVERSTEHEN (B2)", 25, gap=9)
e.bridge("6ページの深読み記事を読んで、正しい答えを選ぼう。")
e.ex("B2", "選択肢", "B", "10月26日の番組は家での介護を議論した",
     "Was diskutierte „Hart aber fair“ in der Sendung am 26. Oktober? A. den Tankrabatt · B. die Pflege zu Hause · C. die Stromsteuer", size=20, gap=7)
e.ex("B2", "選択肢", "A", "ARD『Hart aber fair』10月26日の番組によれば、600万人以上が介護を必要としている",
     "Wie viele Menschen brauchen Pflege? A. mehr als sechs Millionen · B. rund eine Million · C. zehn Millionen", size=20, gap=7)
e.ex("B2", "選択肢", "B", "家族が家で介護する",
     "Wer pflegt zu Hause? A. die Ärzte · B. die Angehörigen · C. die Politiker", size=20, gap=7)
e.ex("B1", "選択肢", "B", "ARD『Hart aber fair』10月26日の番組によれば、約1000万人が家族を介護している",
     "Wie viele Menschen pflegen einen Verwandten (rund)? A. sechs Millionen · B. zehn Millionen · C. zwei Millionen", size=20, gap=7)
e.head("C　GRAMMATIK", 25, gap=9)
e.bridge("かっこ内の形で空所を埋めよう。")
e.ex("B2", "文完成", "wird", "受動態：wird + Partizip II",
     "Die Frage ___ (werden) am Montag diskutiert.", instr="空所補充", size=20, gap=7)
e.ex("B2", "文完成", "ob", "ob が間接疑問文を導く",
     "Die Politik weiß nicht, ___ das Geld reicht.", instr="空所補充", size=20, gap=7)
e.ex("B1", "文完成", "steigt", "steigen → steigt",
     "Die Zahl der Pflegebedürftigen ___ (steigen) weiter.", instr="空所補充", size=20, gap=7)
e.ex("B2", "文完成", "sagte", "sagen の過去形 sagte",
     "Wambach ___ (sagen): Der Aufschwung trägt sich nicht selbst.", instr="空所補充", size=20, gap=7)
e.head("D　WÖRTER DER DEBATTE", 25, gap=9)
e.bridge("枠の中の単語で空所を埋めよう。")
e.para("Pflegeversicherung · Angehörige · Stagnation · Aufschwung", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "文完成", "Pflegeversicherung", "介護保険がもっとお金を出す",
     "Die ___ soll mehr Geld für die Pflege zahlen.", instr="空所補充", size=20, gap=7)
e.ex("B2", "文完成", "Angehörige", "家族が家で介護する",
     "Viele ___ pflegen ihre Verwandten zu Hause.", instr="空所補充", size=20, gap=7)
e.ex("B2", "文完成", "Stagnation", "停滞から抜け出す",
     "Die Wirtschaft kommt langsam aus der ___ heraus.", instr="空所補充", size=20, gap=7)
e.ex("B1", "文完成", "Aufschwung", "回復はまだ自立していない",
     "Der ___ trägt sich noch nicht selbst.", instr="空所補充", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-vertiefung.svg")
print("P6 saved, exercises so far:", len(REG))
