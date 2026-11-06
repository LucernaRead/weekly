# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUGEND · 청소년", "Die Lucerna", "LEVEL B1 · Zurück in die Schule · 학교로 돌아가기")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P5-main")
f.title("Zurück in die Schule — und Bayern hat noch frei", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B1")
f.para("Am Montag, dem 2. November, war es in Baden-Württemberg wieder so weit: Die Schule hat nach den Herbstferien wieder begonnen. Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut — und die ersten Klassenarbeiten kommen bald.")
f.para("In Bayern dagegen ist die Woche noch frei: Dort dauern die Herbstferien in dieser Woche noch an. Wer in München wohnt, kann noch ausschlafen — wer in Stuttgart wohnt, muss schon wieder früh aufstehen. Ein Land, zwei Wochen: So unterschiedlich sind die Ferien in Deutschland.")
f.para("Was macht man in der ersten Schulwoche? Die Lehrerinnen und Lehrer fragen nach den Ferien, die Hefte sind neu, und die Pläne für den Winter stehen schon: Klassenarbeiten, Referate — und bald die ersten Proben für die Weihnachtsfeier.")
f.para("Und nach der Schule? Der Herbst ist die Zeit der Bibliotheken und der Sporthallen: Lesen, was man in den Ferien begonnen hat, oder ein neues Hobby probieren. Unser Tipp: Suchen Sie sich ein Buch für die dunklen Abende — die Bibliotheken haben im November oft neue Bücher und Lesungen.")
f.para("Auch der Sport gehört zur Woche: Am Samstag und Sonntag spielt die Bundesliga — für viele Jugendliche der Ausflug des Wochenendes. Wer in Bayern noch Ferien hat, kann sogar am Freitag schon ins Stadion. Mehr dazu auf Seite 4.")
f.gloss("der Pausenhof 쉬는 시간 운동장 · die Klassenarbeit 학급 시험 · das Referat 수업 발표 · ausschlafen 늦잠 자기 · die Probe 연습.")
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
p.text(ix + 22, yy3 + 26, "FERIENWECHSEL · 방학 교체", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 facts ends", sy3 + sh)
words = ["der Pausenhof — 쉬는 시간 운동장", "die Klassenarbeit — 학급 시험", "das Referat — 수업 발표",
         "der Rucksack — 책가방", "ausschlafen — 늦잠 자기", "die Probe — 연습"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SCHULWÖRTER · 학교 단어", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Wann hat Ihre Schule nach den Ferien wieder begonnen? Und was war Ihr erstes Fach? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("여러분 학교는 방학 뒤에 며칠에 개학했나요? 첫 수업은 어떤 과목이었나요? 독일어로 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE? · 여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "여러분 학교는 방학 뒤에 며칠에 개학했나요? 첫 수업은 어떤 과목이었나요? 독일어로 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- Wochenplan wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "DER WOCHENPLAN DER REDAKTION · 편집부 주간 계획", 24, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "ÜBUNGEN · 5면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에 · 번호로 정답을 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · LESEVERSTEHEN", 25)
e.expl("5면 기사를 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "A", "바덴뷔르템베르크는 11월 2일에 개학해요",
     "In Baden-Württemberg beginnt die Schule am... A. 2. November · B. 8. November · C. 31. Oktober", size=20, gap=8)
e.ex("B1", "객관식", "B", "바이에른은 방학이 아직 끝나지 않았어요",
     "In Bayern sind die Ferien... A. vorbei · B. noch nicht vorbei · C. erst im Dezember", size=20, gap=8)
e.ex("B1", "객관식", "B", "개학 주에는 학급 시험이 있어요",
     "Was kommt bald in der Schule? A. die Sommerferien · B. die ersten Klassenarbeiten · C. der Abiball", size=20, gap=8)
e.ex("B1", "객관식", "B", "Referat = 수업 발표",
     "Was ist ein Referat? A. ein Buch · B. ein Vortrag in der Klasse · C. ein Sportfest", size=20, gap=8)
e.ex("A2", "객관식", "A", "바이에른 방학 중인 학생은 금요일에 이미 경기장에 갈 수 있어요",
     "Wer kann am Freitag schon ins Stadion? A. Wer in Bayern Ferien hat. · B. Wer in Stuttgart wohnt. · C. Niemand.", size=20, gap=8)
e.head("B · WÖRTER AUS DEM TEXT", 25)
e.expl("네모 안의 단어로 빈칸을 채우세요.")
e.para("Pausenhof · Klassenarbeit · Referat · ausschlafen · Probe · Rucksack", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "Pausenhof", "쉬는 시간 운동장에서 놀아요",
     "In der Pause spielen die Kinder auf dem ___.", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "Klassenarbeit", "수학 학급 시험",
     "Am Freitag schreiben wir eine ___ in Mathe.", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "Referat", "발표를 위해 세 권의 책을 읽어야 해요",
     "Für das ___ muss ich drei Bücher lesen.", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "ausschlafen", "방학에는 늦잠을 잘 수 있어요",
     "In den Ferien kann man lange ___.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Probe", "올해 크리스마스 공연의 첫 연습",
     "Für die Weihnachtsfeier gibt es schon die erste ___.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Rucksack", "책가방 안에는 공책과 연필이 있어요",
     "Mein ___ ist gepackt: Hefte, Stifte, Pausenbrot.", instr="빈칸", size=20, gap=8)
e.head("C · SÄTZE MIT «WEIL»", 25)
e.expl("weil로 두 문장을 연결하세요(동사는 문장 끝에).")
e.ex("B1", "문장 전환", "Die Kinder freuen sich, weil die Schule wieder beginnt.", "weil 절은 동사가 끝에 와요",
     "Die Kinder freuen sich. Die Schule beginnt wieder. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Er liest ein Buch, weil es draußen kalt ist.", "ist가 끝에 와요",
     "Er liest ein Buch. Es ist draußen kalt. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Sie geht in die Bibliothek, weil sie ein Referat schreiben muss.", "muss가 끝에 와요",
     "Sie geht in die Bibliothek. Sie muss ein Referat schreiben. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Bayern hat noch Ferien, weil die Ferien dort später liegen.", "liegen이 끝에 와요",
     "Bayern hat noch Ferien. Die Ferien liegen dort später. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
e.head("D · RICHTIG ODER FALSCH?", 25)
e.expl("맞는지 틀리는지 판단하세요.")
e.ex("A2", "참/거짓 판단", "Richtig", "바덴뷔르템베르크는 11월 2일에 다시 개학했어요",
     "In Baden-Württemberg hat die Schule am 2. November wieder begonnen. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("B1", "참/거짓 판단", "Falsch", "독일 전역의 가을 방학이 끝난 것은 아니에요",
     "In ganz Deutschland sind die Herbstferien vorbei. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("A2", "참/거짓 판단", "Richtig", "개학 주에는 시험과 발표가 있어요",
     "Die erste Schulwoche bringt Klassenarbeiten und Referate. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jugend.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERTIEFUNG · 심화 읽기", "Die Lucerna", "LEVEL B2 · Pflege & Stromsteuer · 돌봄과 전기세")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P6-main")
f.title("Pflege zu Hause: Wer hilft den Angehörigen?", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B2")
f.para("Am Montag, dem 26. Oktober, um 21.00 Uhr diskutierte die ARD-Sendung „Hart aber fair“: „Pflege zu Hause — Lässt die Politik Angehörige allein?“ Nach Angaben der Sendung brauchen in Deutschland mehr als sechs Millionen Menschen Pflege. Die meisten von ihnen werden zu Hause gepflegt — von rund zehn Millionen Angehörigen.")
f.para("Was heißt „pflegen“ im Alltag? Morgens helfen beim Aufstehen, beim Waschen und Anziehen, beim Essen und bei den Medikamenten — und nachts wach sein, wenn etwas passiert. Viele Angehörige machen das neben dem Beruf, und viele sind selbst schon alt.")
f.para("Die Politik streitet seit Jahren über die Antwort: mehr Geld für die Pflegeversicherung? Mehr Pflegedienste, die zu Hause helfen? Mehr freie Tage für pflegende Angehörige? Die Debatte ist schwierig, weil alles Geld kostet — und weil die Zahl der Pflegebedürftigen weiter steigt.")
f.para("Zweites Thema der Woche: die Stromsteuer. Union und SPD sind sich hier „weiter weit auseinander“, wie es in der Tagesschau heißt: Die eine Seite will die Steuer für alle senken, die andere nur gezielt. Auch der ZEW-Index zeigt, wie wichtig die Frage ist: Die Lage wird etwas besser eingeschätzt (minus 35,9 nach minus 47,1), aber die Erwartungen fielen im Oktober auf 28,1 Punkte.")
f.para("Und was sagt der Präsident des ZEW, Achim Wambach? „Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.“ Mit anderen Worten: Es geht langsam aufwärts — aber von allein geht es nicht.")
f.para("Zwei Debatten, ein Muster: Beide kosten Geld und betreffen fast jeden Haushalt.")
f.gloss("der Angehörige 가족 · die Pflegeversicherung 요양 보험 · der Pflegedienst 요양 서비스 기관 · die Stagnation 침체 · der Aufschwung 회복.")
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
p.text(ix + 22, yy3 + 26, "DIE ZAHLEN · 이번 주 숫자", 24, "sans", True, OLIVE)
yy3 += 52
for yr, t in tl:
    p.text(ix + 22, yy3 + 21, yr, 21, "sans", True, BRICK)
    yy3 = p.para(ix + 130, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 152, 1.42) + 10
print("P6 col3 numbers ends", 200 + tlh)
deb = "Pflege: Wer zu Hause pflegt, braucht mehr Hilfe — darüber streitet die Politik. Stromsteuer: Wie stark sie sinkt, ist noch offen. Beides kostet Geld, beides betrifft fast jeden Haushalt."
hy3 = 200 + tlh + 26
hh = 140 + 29.82 * len(wrap(deb, "serif", False, 21, CW - 44)) + 27.69 * (len(wrap("돌봄: 집에서 돌보는 일에는 더 많은 도움이 필요해요. 이에 대해 정치권은 아직 논쟁 중이에요. 전기세: 얼마나 내려갈지는 아직 정해지지 않았어요. 두 문제 모두 돈이 들고, 거의 모든 가정에 영향을 미쳐요.", "sans", False, 19.5, CW - 44)) - 1)
p.rect(ix, hy3, CW, hh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = hy3 + 16
p.text(ix + 22, yy3 + 26, "DIE DEBATTE IN EINEM SATZ", 22.5, "sans", True, OLIVE)
yy3 += 50
yy3 = p.para(ix + 22, yy3 + 21, deb, 21, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "돌봄: 집에서 돌보는 일에는 더 많은 도움이 필요해요. 이에 대해 정치권은 아직 논쟁 중이에요. 전기세: 얼마나 내려갈지는 아직 정해지지 않았어요. 두 문제 모두 돈이 들고, 거의 모든 가정에 영향을 미쳐요.", 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", hy3 + hh)

# ---- Pro & Contra wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 252, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "PRO & CONTRA · 찬반 — die Argumente der Debatte", 24, "sans", True, OLIVE)
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
p.text(MX, cy + 28, "WER PFLEGT ZU HAUSE? · 누가 집에서 돌봐요?", 26, "sans", True, OLIVE)
bars = [("pflegen Angehörige zu Hause", 68, "가족 돌봄"),
        ("nutzen einen Pflegedienst", 20, "방문 돌봄"),
        ("leben im Pflegeheim", 12, "요양원 생활")]
byy = cy + 58
for lab, v, zh in bars:
    p.text(MX, byy + 26, lab, 22, "serif", True, INK)
    p.text(MX + 360, byy + 26, zh, 20, "sans", False, GREY)
    p.rect(MX + 470, byy + 4, v * 17, 30, fill=OLIVE)
    p.text(MX + 470 + v * 17 + 16, byy + 26, f"{v} %", 22, "sans", True, BRICK)
    byy += 52
p.text(MX, byy + 22, "ÜBUNGSDATEN · 연습 데이터 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (이 그림 숫자는 편집부 연습 예시예요. 실제 조사가 아니에요.)", 19.5, "sans", False, GREY)

# ---- P6 exercises ----
ey = 1808
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · 6면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에 · 번호로 정답을 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · DAS DIAGRAMM LESEN", 25, gap=9)
e.expl("위 연습 그래프를 보고 정답을 고르세요.")
e.ex("B1", "객관식", "A", "68%는 가족 돌봄이에요",
     "Wie viele Prozent pflegen Angehörige zu Hause (Übungsdaten)? A. 68 % · B. 20 % · C. 12 %", size=20, gap=7)
e.ex("B1", "객관식", "B", "방문 돌봄 20%가 두 번째예요",
     "Was ist die zweitgrößte Gruppe? A. Pflegeheim · B. Pflegedienst · C. Angehörige", size=20, gap=7)
e.ex("B1", "객관식", "B", "68+20=88",
     "Angehörige und Pflegedienst zusammen sind... A. 80 % · B. 88 % · C. 90 %", size=20, gap=7)
e.ex("B2", "객관식", "B", "요양원 12%가 가장 작아요",
     "Welche Gruppe ist kleiner? A. Pflegedienst · B. Pflegeheim · C. beide gleich", size=20, gap=7)
e.ex("B1", "객관식", "A", "요양원은 12%예요",
     "Wie viele Prozent leben im Pflegeheim? A. 12 % · B. 20 % · C. 68 %", size=20, gap=7)
e.ex("B2", "객관식", "B", "68+20+12=100",
     "Die drei Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 %", size=20, gap=7)
e.head("B · LESEVERSTEHEN (B2)", 25, gap=9)
e.expl("6면 심화 기사를 읽고 정답을 고르세요.")
e.ex("B2", "객관식", "B", "10월 26일 방송은 집에서의 돌봄을 다뤘어요",
     "Was diskutierte „Hart aber fair“ in der Sendung am 26. Oktober? A. den Tankrabatt · B. die Pflege zu Hause · C. die Stromsteuer", size=20, gap=7)
e.ex("B2", "객관식", "A", "ARD 《Hart aber fair》 10월 26일 방송에 따르면 600만 명이 넘는 사람들이 돌봄이 필요해요",
     "Wie viele Menschen brauchen Pflege? A. mehr als sechs Millionen · B. rund eine Million · C. zehn Millionen", size=20, gap=7)
e.ex("B2", "객관식", "B", "가족이 집에서 돌봐요",
     "Wer pflegt zu Hause? A. die Ärzte · B. die Angehörigen · C. die Politiker", size=20, gap=7)
e.ex("B1", "객관식", "B", "ARD 《Hart aber fair》 10월 26일 방송에 따르면 약 1,000만 명이 가족을 돌봐요",
     "Wie viele Menschen pflegen einen Verwandten (rund)? A. sechs Millionen · B. zehn Millionen · C. zwei Millionen", size=20, gap=7)
e.head("C · GRAMMATIK", 25, gap=9)
e.expl("괄호 안의 형태로 빈칸을 채우세요.")
e.ex("B2", "문장 완성", "wird", "수동태: wird + 과거분사",
     "Die Frage ___ (werden) am Montag diskutiert.", instr="빈칸", size=20, gap=7)
e.ex("B2", "문장 완성", "ob", "ob는 간접 의문문을 이끌어요",
     "Die Politik weiß nicht, ___ das Geld reicht.", instr="빈칸", size=20, gap=7)
e.ex("B1", "문장 완성", "steigt", "steigen → steigt",
     "Die Zahl der Pflegebedürftigen ___ (steigen) weiter.", instr="빈칸", size=20, gap=7)
e.ex("B2", "문장 완성", "sagte", "sagen의 과거형은 sagte예요",
     "Wambach ___ (sagen): Der Aufschwung trägt sich nicht selbst.", instr="빈칸", size=20, gap=7)
e.head("D · WÖRTER DER DEBATTE", 25, gap=9)
e.expl("네모 안의 단어로 빈칸을 채우세요.")
e.para("Pflegeversicherung · Angehörige · Stagnation · Aufschwung", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "Pflegeversicherung", "요양 보험이 돌봄에 더 많은 돈을 내야 해요",
     "Die ___ soll mehr Geld für die Pflege zahlen.", instr="빈칸", size=20, gap=7)
e.ex("B2", "문장 완성", "Angehörige", "가족이 집에서 돌봐요",
     "Viele ___ pflegen ihre Verwandten zu Hause.", instr="빈칸", size=20, gap=7)
e.ex("B2", "문장 완성", "Stagnation", "침체에서 천천히 벗어나고 있어요",
     "Die Wirtschaft kommt langsam aus der ___ heraus.", instr="빈칸", size=20, gap=7)
e.ex("B1", "문장 완성", "Aufschwung", "회복이 아직 스스로 이어지지 않아요",
     "Der ___ trägt sich noch nicht selbst.", instr="빈칸", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-vertiefung.svg")
print("P6 saved, exercises so far:", len(REG))
