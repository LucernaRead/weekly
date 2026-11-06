# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/de-ko-proof/baseline-rerun/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUGEND · 青年", "Die Lucerna", "LEVEL B1 · Zurück in die Schule · 重返校园")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P5-main")
f.title("Zurück in die Schule — und Bayern hat noch frei", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B1")
f.para("Am Montag, dem 2. November, war es in Baden-Württemberg wieder so weit: Die Schule hat nach den Herbstferien wieder begonnen. Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut — und die ersten Klassenarbeiten kommen bald.")
f.para("In Bayern dagegen ist die Woche noch frei: Dort dauern die Herbstferien in dieser Woche noch an. Wer in München wohnt, kann noch ausschlafen — wer in Stuttgart wohnt, muss schon wieder früh aufstehen. Ein Land, zwei Wochen: So unterschiedlich sind die Ferien in Deutschland.")
f.para("Was macht man in der ersten Schulwoche? Die Lehrerinnen und Lehrer fragen nach den Ferien, die Hefte sind neu, und die Pläne für den Winter stehen schon: Klassenarbeiten, Referate — und bald die ersten Proben für die Weihnachtsfeier.")
f.para("Und nach der Schule? Der Herbst ist die Zeit der Bibliotheken und der Sporthallen: Lesen, was man in den Ferien begonnen hat, oder ein neues Hobby probieren. Unser Tipp: Suchen Sie sich ein Buch für die dunklen Abende — die Bibliotheken haben im November oft neue Bücher und Lesungen.")
f.para("Auch der Sport gehört zur Woche: Am Samstag und Sonntag spielt die Bundesliga — für viele Jugendliche der Ausflug des Wochenendes. Wer in Bayern noch Ferien hat, kann sogar am Freitag schon ins Stadion. Mehr dazu auf Seite 4.")
f.gloss("der Pausenhof 课间操场 · die Klassenarbeit 课堂测验 · das Referat 课堂报告 · ausschlafen 睡懒觉 · die Probe 排练。")
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
words = ["der Pausenhof — 课间操场", "die Klassenarbeit — 课堂测验", "das Referat — 课堂报告",
         "der Rucksack — 书包", "ausschlafen — 睡懒觉", "die Probe — 排练"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SCHULWÖRTER · 校园词汇", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Wann hat Ihre Schule nach den Ferien wieder begonnen? Und was war Ihr erstes Fach? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("你的学校假期后哪天开学？第一节是什么课？写两句德语寄来。", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE? · 说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你的学校假期后哪天开学？第一节是什么课？写两句德语寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- Wochenplan wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "DER WOCHENPLAN DER REDAKTION · 编辑部一周计划", 24, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "ÜBUNGEN · 第 5 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · LESEVERSTEHEN", 25)
e.bridge("读第 5 版文章，选出正确答案。")
e.ex("B1", "单选", "A", "BW 11 月 2 日开学",
     "In Baden-Württemberg beginnt die Schule am... A. 2. November · B. 8. November · C. 31. Oktober", size=20, gap=8)
e.ex("B1", "单选", "B", "巴伐利亚假期未结束",
     "In Bayern sind die Ferien... A. vorbei · B. noch nicht vorbei · C. erst im Dezember", size=20, gap=8)
e.ex("B1", "单选", "B", "开学周有课堂测验",
     "Was kommt bald in der Schule? A. die Sommerferien · B. die ersten Klassenarbeiten · C. der Abiball", size=20, gap=8)
e.ex("B1", "单选", "B", "Referat = 课堂报告",
     "Was ist ein Referat? A. ein Buch · B. ein Vortrag in der Klasse · C. ein Sportfest", size=20, gap=8)
e.ex("A2", "单选", "A", "巴伐利亚学生周五可去球场",
     "Wer kann am Freitag schon ins Stadion? A. Wer in Bayern Ferien hat. · B. Wer in Stuttgart wohnt. · C. Niemand.", size=20, gap=8)
e.head("B · WÖRTER AUS DEM TEXT", 25)
e.bridge("用方框里的词填空。")
e.para("Pausenhof · Klassenarbeit · Referat · ausschlafen · Probe · Rucksack", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "Pausenhof", "课间操场上玩",
     "In der Pause spielen die Kinder auf dem ___.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "Klassenarbeit", "数学课堂测验",
     "Am Freitag schreiben wir eine ___ in Mathe.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "Referat", "报告要读三本书",
     "Für das ___ muss ich drei Bücher lesen.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "ausschlafen", "假期可以睡懒觉",
     "In den Ferien kann man lange ___.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Probe", "圣诞演出的第一次排练",
     "Für die Weihnachtsfeier gibt es schon die erste ___.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Rucksack", "书包里有本子铅笔",
     "Mein ___ ist gepackt: Hefte, Stifte, Pausenbrot.", instr="填空", size=20, gap=8)
e.head("C · SÄTZE MIT «WEIL»", 25)
e.bridge("用 weil 连接两个句子（动词放句末）。")
e.ex("B1", "句型转换", "Die Kinder freuen sich, weil die Schule wieder beginnt.", "weil 句动词置尾",
     "Die Kinder freuen sich. Die Schule beginnt wieder. (weil) → ___", instr="改写", size=20, gap=8)
e.ex("B1", "句型转换", "Er liest ein Buch, weil es draußen kalt ist.", "ist 置尾",
     "Er liest ein Buch. Es ist draußen kalt. (weil) → ___", instr="改写", size=20, gap=8)
e.ex("B1", "句型转换", "Sie geht in die Bibliothek, weil sie ein Referat schreiben muss.", "muss 置尾",
     "Sie geht in die Bibliothek. Sie muss ein Referat schreiben. (weil) → ___", instr="改写", size=20, gap=8)
e.ex("B1", "句型转换", "Bayern hat noch Ferien, weil die Ferien dort später liegen.", "liegen 置尾",
     "Bayern hat noch Ferien. Die Ferien liegen dort später. (weil) → ___", instr="改写", size=20, gap=8)
e.head("D · RICHTIG ODER FALSCH?", 25)
e.bridge("判断对错。")
e.ex("A2", "判断对错", "Richtig", "BW 11 月 2 日复课",
     "In Baden-Württemberg hat die Schule am 2. November wieder begonnen. Richtig oder falsch?", instr="判断", size=20, gap=8)
e.ex("B1", "判断对错", "Falsch", "全德假期并未都结束",
     "In ganz Deutschland sind die Herbstferien vorbei. Richtig oder falsch?", instr="判断", size=20, gap=8)
e.ex("A2", "判断对错", "Richtig", "开学周有测验与报告",
     "Die erste Schulwoche bringt Klassenarbeiten und Referate. Richtig oder falsch?", instr="判断", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jugend.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERTIEFUNG · 深读", "Die Lucerna", "LEVEL B2 · Pflege & Stromsteuer · 护理与电力税")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P6-main")
f.title("Pflege zu Hause: Wer hilft den Angehörigen?", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B2")
f.para("Am Montag, dem 26. Oktober, um 21.00 Uhr diskutierte die ARD-Sendung „Hart aber fair“: „Pflege zu Hause — Lässt die Politik Angehörige allein?“ Nach Angaben der Sendung brauchen in Deutschland mehr als sechs Millionen Menschen Pflege. Die meisten von ihnen werden zu Hause gepflegt — von rund zehn Millionen Angehörigen.")
f.para("Was heißt „pflegen“ im Alltag? Morgens helfen beim Aufstehen, beim Waschen und Anziehen, beim Essen und bei den Medikamenten — und nachts wach sein, wenn etwas passiert. Viele Angehörige machen das neben dem Beruf, und viele sind selbst schon alt.")
f.para("Die Politik streitet seit Jahren über die Antwort: mehr Geld für die Pflegeversicherung? Mehr Pflegedienste, die zu Hause helfen? Mehr freie Tage für pflegende Angehörige? Die Debatte ist schwierig, weil alles Geld kostet — und weil die Zahl der Pflegebedürftigen weiter steigt.")
f.para("Zweites Thema der Woche: die Stromsteuer. Union und SPD sind sich hier „weiter weit auseinander“, wie es in der Tagesschau heißt: Die eine Seite will die Steuer für alle senken, die andere nur gezielt. Auch der ZEW-Index zeigt, wie wichtig die Frage ist: Die Lage wird etwas besser eingeschätzt (minus 35,9 nach minus 47,1), aber die Erwartungen fielen im Oktober auf 28,1 Punkte.")
f.para("Und was sagt der Präsident des ZEW, Achim Wambach? „Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.“ Mit anderen Worten: Es geht langsam aufwärts — aber von allein geht es nicht.")
f.para("Zwei Debatten, ein Muster: Beide kosten Geld und betreffen fast jeden Haushalt.")
f.gloss("der Angehörige 亲属 · die Pflegeversicherung 护理保险 · der Pflegedienst 护理服务机构 · die Stagnation 停滞 · der Aufschwung 复苏。")
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
p.text(ix + 22, yy3 + 26, "DIE ZAHLEN · 本周数字", 24, "sans", True, OLIVE)
yy3 += 52
for yr, t in tl:
    p.text(ix + 22, yy3 + 21, yr, 21, "sans", True, BRICK)
    yy3 = p.para(ix + 130, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 152, 1.42) + 10
print("P6 col3 numbers ends", 200 + tlh)
deb = "Pflege: Wer zu Hause pflegt, braucht mehr Hilfe — darüber streitet die Politik. Stromsteuer: Wie stark sie sinkt, ist noch offen. Beides kostet Geld, beides betrifft fast jeden Haushalt."
hy3 = 200 + tlh + 26
hh = 140 + 29.82 * len(wrap(deb, "serif", False, 21, CW - 44)) + 27.69 * (len(wrap("护理：在家护理需要更多帮助——对此政界仍在争论。电力税：降多少尚未确定。两者都花钱，都关系到几乎每个家庭。", "sans", False, 19.5, CW - 44)) - 1)
p.rect(ix, hy3, CW, hh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = hy3 + 16
p.text(ix + 22, yy3 + 26, "DIE DEBATTE IN EINEM SATZ", 22.5, "sans", True, OLIVE)
yy3 += 50
yy3 = p.para(ix + 22, yy3 + 21, deb, 21, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "护理：在家护理需要更多帮助——对此政界仍在争论。电力税：降多少尚未确定。两者都花钱，都关系到几乎每个家庭。", 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", hy3 + hh)

# ---- Pro & Contra wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 252, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "PRO & CONTRA · 正方与反方 — die Argumente der Debatte", 24, "sans", True, OLIVE)
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
p.text(MX, cy + 28, "WER PFLEGT ZU HAUSE? · 谁在家护理？", 26, "sans", True, OLIVE)
bars = [("pflegen Angehörige zu Hause", 68, "家属护理"),
        ("nutzen einen Pflegedienst", 20, "专业上门"),
        ("leben im Pflegeheim", 12, "住养老院")]
byy = cy + 58
for lab, v, zh in bars:
    p.text(MX, byy + 26, lab, 22, "serif", True, INK)
    p.text(MX + 360, byy + 26, zh, 20, "sans", False, GREY)
    p.rect(MX + 470, byy + 4, v * 17, 30, fill=OLIVE)
    p.text(MX + 470 + v * 17 + 16, byy + 26, f"{v} %", 22, "sans", True, BRICK)
    byy += 52
p.text(MX, byy + 22, "ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）", 19.5, "sans", False, GREY)

# ---- P6 exercises ----
ey = 1808
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · 第 6 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · DAS DIAGRAMM LESEN", 25, gap=9)
e.bridge("看上面的练习图表，选出正确答案。")
e.ex("B1", "单选", "A", "68% 家属护理",
     "Wie viele Prozent pflegen Angehörige zu Hause (Übungsdaten)? A. 68 % · B. 20 % · C. 12 %", size=20, gap=7)
e.ex("B1", "单选", "B", "专业上门 20% 第二",
     "Was ist die zweitgrößte Gruppe? A. Pflegeheim · B. Pflegedienst · C. Angehörige", size=20, gap=7)
e.ex("B1", "单选", "B", "68+20=88",
     "Angehörige und Pflegedienst zusammen sind... A. 80 % · B. 88 % · C. 90 %", size=20, gap=7)
e.ex("B2", "单选", "B", "养老院 12% 最小",
     "Welche Gruppe ist kleiner? A. Pflegedienst · B. Pflegeheim · C. beide gleich", size=20, gap=7)
e.ex("B1", "单选", "A", "养老院 12%",
     "Wie viele Prozent leben im Pflegeheim? A. 12 % · B. 20 % · C. 68 %", size=20, gap=7)
e.ex("B2", "单选", "B", "68+20+12=100",
     "Die drei Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 %", size=20, gap=7)
e.head("B · LESEVERSTEHEN (B2)", 25, gap=9)
e.bridge("读第 6 版深读文章，选出正确答案。")
e.ex("B2", "单选", "B", "10 月 26 日节目讨论居家护理",
     "Was diskutierte „Hart aber fair“ in der Sendung am 26. Oktober? A. den Tankrabatt · B. die Pflege zu Hause · C. die Stromsteuer", size=20, gap=7)
e.ex("B2", "单选", "A", "据 ARD《Hart aber fair》10 月 26 日节目，600 多万人需要护理",
     "Wie viele Menschen brauchen Pflege? A. mehr als sechs Millionen · B. rund eine Million · C. zehn Millionen", size=20, gap=7)
e.ex("B2", "单选", "B", "家属居家护理",
     "Wer pflegt zu Hause? A. die Ärzte · B. die Angehörigen · C. die Politiker", size=20, gap=7)
e.ex("B1", "单选", "B", "据 ARD《Hart aber fair》10 月 26 日节目，约 1000 万人护理亲属",
     "Wie viele Menschen pflegen einen Verwandten (rund)? A. sechs Millionen · B. zehn Millionen · C. zwei Millionen", size=20, gap=7)
e.head("C · GRAMMATIK", 25, gap=9)
e.bridge("用括号里的形式填空。")
e.ex("B2", "完成句子", "wird", "被动：wird + Partizip II",
     "Die Frage ___ (werden) am Montag diskutiert.", instr="填空", size=20, gap=7)
e.ex("B2", "完成句子", "ob", "ob 引导间接疑问句",
     "Die Politik weiß nicht, ___ das Geld reicht.", instr="填空", size=20, gap=7)
e.ex("B1", "完成句子", "steigt", "steigen → steigt",
     "Die Zahl der Pflegebedürftigen ___ (steigen) weiter.", instr="填空", size=20, gap=7)
e.ex("B2", "完成句子", "sagte", "sagen 过去时 sagte",
     "Wambach ___ (sagen): Der Aufschwung trägt sich nicht selbst.", instr="填空", size=20, gap=7)
e.head("D · WÖRTER DER DEBATTE", 25, gap=9)
e.bridge("用方框里的词填空。")
e.para("Pflegeversicherung · Angehörige · Stagnation · Aufschwung", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "Pflegeversicherung", "护理保险出更多钱",
     "Die ___ soll mehr Geld für die Pflege zahlen.", instr="填空", size=20, gap=7)
e.ex("B2", "完成句子", "Angehörige", "亲属居家护理",
     "Viele ___ pflegen ihre Verwandten zu Hause.", instr="填空", size=20, gap=7)
e.ex("B2", "完成句子", "Stagnation", "走出停滞",
     "Die Wirtschaft kommt langsam aus der ___ heraus.", instr="填空", size=20, gap=7)
e.ex("B1", "完成句子", "Aufschwung", "复苏尚未自我维持",
     "Der ___ trägt sich noch nicht selbst.", instr="填空", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-vertiefung.svg")
print("P6 saved, exercises so far:", len(REG))
