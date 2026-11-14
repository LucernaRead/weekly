# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN　연습과 정답", "Die Lucerna", "SCHLUSSTEST　종합 평가　Alle Antworten unten auf dieser Seite　정답은 이 면 아래쪽에")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "schnitzen = 호박 조각하기"),
    ("A2", "A", "geht in die Bibliothek = 도서관에 가다"),
    ("A2", "A", "Uhr zurückgestellt = 시계를 뒤로"),
    ("A2", "C", "Winterzeit = 표준시 시작"),
    ("A2", "B", "eine Stunde länger 한 시간 더"),
    ("A2", "A", "der erste Frost = 첫 서리"),
    ("B1", "B", "gefällt mir gut = 마음에 들어요"),
    ("A2", "C", "ich gehe (1인칭)"),
]
cnums = [reg_ex(lv, "빈칸 채우기", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　LÜCKENTEXT　빈칸 채우기", 24)
bf.para(f"Jonas freut sich auf das Wochenende. Am Samstag kauft er einen Kürbis und ({cnums[0]})___ ihn zu Hause. Am Nachmittag ({cnums[1]})___ er in die Bibliothek — sie hat am Samstag ein besonderes Programm. Am Abend spielt Dortmund, und Jonas sieht das Spiel mit Freunden. In der Nacht wird die Uhr ({cnums[2]})___: Die ({cnums[3]})___ beginnt. Am Sonntag schläft Jonas eine Stunde ({cnums[4]})___. Draußen ist es kalt, der erste ({cnums[5]})___ ist da. „Ein Sonntag mit 25 Stunden“, sagt Jonas, „({cnums[6]})___ mir gut! Und am Montag ({cnums[7]})___ ich wieder in die Schule.“", 20.5)
bf.expl("선택지:")
for n, opts in zip(cnums, [
    "A. kocht · B. schnitzt · C. malt",
    "A. geht · B. schläft · C. kocht",
    "A. zurückgestellt · B. vorgestellt · C. vergessen",
    "A. Sommerzeit · B. Ferienzeit · C. Winterzeit",
    "A. früh · B. länger · C. laut",
    "A. Frost · B. Sommer · C. Frühling",
    "A. geht · B. gefällt · C. macht",
    "A. gehen · B. gehst · C. gehe",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)

# ---- B. general MC ----
bf.head("B　WISSENSFRAGEN　종합 문제", 24)
bf.ex("B1", "객관식", "A", "도서관의 날은 Preusker를 기념해요",
      "Der Tag der Bibliotheken erinnert an... A. Karl Preusker · B. Martin Luther · C. Lucas Cranach", size=19.5, gap=8)
bf.ex("A2", "객관식", "B", "일요일 새벽 3시에 뒤로",
      "Die Uhr wird umgestellt am... A. Freitag um 20.30 Uhr · B. Sonntag um 3.00 Uhr · C. Samstag um Mitternacht", size=19.5, gap=8)
bf.ex("A2", "객관식", "A", "O bis O = 10월부터 부활절까지",
      "„Von O bis O“ heißt: Winterreifen von... A. Oktober bis Ostern · B. Oktober bis Oktober · C. Ostern bis Oktober", size=19.5, gap=8)
bf.ex("B1", "객관식", "B", "데어 클라시커는 도르트문트에서",
      "Am 31. Oktober spielen die Bayern... A. zu Hause · B. in Dortmund · C. in Berlin", size=19.5, gap=8)
bf.ex("B1", "객관식", "B", "면역은 10–14일에 생겨요",
      "Die Grippeimpfung schützt nach... A. 2 Tagen · B. 10 bis 14 Tagen · C. 3 Monaten", size=19.5, gap=8)
bf.ex("B1", "객관식", "B", "약국 접종은 18세부터",
      "In Apotheken impft man Menschen... A. ab 6 Jahren · B. ab 18 Jahren · C. nur ab 60", size=19.5, gap=8)
bf.ex("A2", "객관식", "B", "토요일 빅매치는 도르트문트–프랑크푸르트",
      "Das Topspiel am Samstag ist... A. Freiburg–Bayern · B. Dortmund–Frankfurt · C. Stuttgart–Gladbach", size=19.5, gap=8)
bf.ex("A2", "객관식", "B", "2–3시는 두 번 있어요",
      "Die Stunde 2.00–3.00 Uhr gibt es in der Nacht... A. einmal · B. zweimal · C. gar nicht", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C　LESEVERSTEHEN　독해", 24)
bf.para("Frau Berger arbeitet in einer Berliner Bibliothek. Am Samstag, dem 24. Oktober, beginnt sie um halb zehn mit der Arbeit. Heute ist der Tag der Bibliotheken: Um elf Uhr spielt sie mit den Kindern Bibliotheks-Bingo. Am Nachmittag hilft sie bei den Book-Blind-Dates. Um 18 Uhr schließt die Bibliothek. Frau Berger fährt nach Hause und stellt am Abend alle Uhren um — morgen darf sie eine Stunde länger schlafen.", 20.5)
bf.ex("B1", "객관식", "A", "halb zehn = 9:30",
      "Wann beginnt Frau Berger mit der Arbeit? A. um 9.30 Uhr · B. um 10.30 Uhr · C. um halb elf", size=19.5, gap=8)
bf.ex("A2", "객관식", "B", "11시에 아이들과 Bingo",
      "Was spielt sie um elf Uhr mit den Kindern? A. Fußball · B. Bibliotheks-Bingo · C. Karten", size=19.5, gap=8)
bf.ex("A2", "객관식", "B", "저녁에 집에서 시계를 맞춰요",
      "Was macht sie am Abend zu Hause? A. Sie schnitzt einen Kürbis. · B. Sie stellt die Uhren um. · C. Sie liest ein Buch.", size=19.5, gap=8)
bf.ex("B1", "객관식", "B", "시계를 뒤로 돌려서 더 잘 수 있어요",
      "Warum darf sie am Sonntag länger schlafen? A. Die Bibliothek ist zu. · B. Die Uhr wird zurückgestellt. · C. Sie hat Urlaub.", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D　SÄTZE BAUEN　문장 만들기", 22)  # D5 fix run2
bf.ex("A2", "문장 만들기", "Die Uhr wird am Sonntag zurückgestellt.", "wird는 두 번째, Partizip은 끝에",
      "die Uhr / wird / am Sonntag / zurückgestellt → ___", instr="문장 만들기", size=19.5, gap=8)
bf.ex("A2", "문장 만들기", "Wir schlafen eine Stunde länger.", "주어-동사-목적어 순서",
      "wir / schlafen / eine Stunde / länger → ___", instr="문장 만들기", size=19.5, gap=8)
bf.ex("B1", "문장 만들기", "Die Kinder freuen sich, weil Ferien sind.", "weil 문장은 동사가 끝에",
      "die Kinder / freuen sich / weil / Ferien / sind → ___", instr="문장 만들기", size=19.5, gap=8)
bf.ex("B1", "문장 만들기", "Am Samstag ist der Tag der Bibliotheken.", "시간 표현으로 시작, 동사는 두 번째",
      "am Samstag / ist / der Tag / der Bibliotheken → ___", instr="문장 만들기", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E　ÜBERSETZEN　번역", 24)
bf.ex("A2", "번역", "이 밤은 25시간이에요.", "Stunden = 시간",
      "Die Nacht hat 25 Stunden. (한국어로)", instr="번역", size=19.5, gap=8)
bf.ex("A2", "번역", "저는 토요일 저녁에 시계를 맞춰요.", "umstellen = (시계를) 맞추다",
      "Ich stelle die Uhr am Samstagabend um. (한국어로 번역하세요)", instr="번역", size=19.5, gap=8)
bf.ex("B1", "번역", "Am Sonntag schlafe ich eine Stunde länger.", "한 시간 더 자기 = eine Stunde länger schlafen",
      "일요일에 한 시간 더 자요. (독일어로)", instr="번역", size=19.5, gap=8)
bf.ex("B1", "번역", "In der Bibliothek kann man Bücher leihen.", "kann man ... leihen = 빌릴 수 있어요",
      "도서관에서 책을 빌릴 수 있어요. (독일어로)", instr="번역", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F　WÖRTER PAAREN　단어 짝짓기", 24)
bf.match_set("B1", "단어 짝짓기",
             ["die Umstellung", "die Mitgliedstaaten", "die Mehrheit", "der Feiertag"],
             ["ein Tag, an dem man nicht arbeiten muss",
              "der Wechsel zwischen Sommer- und Winterzeit",
              "die Länder, die zu einer Union gehören",
              "mehr als die Hälfte, zum Beispiel 84 Prozent"],
             ["b", "c", "d", "a"],
             ["Umstellung = 서머타임·표준시 전환 b", "Mitgliedstaaten = 회원국 c", "Mehrheit = 다수 d", "Feiertag = 공휴일 a"],
             instr="단어와 뜻 짝짓기")

# ---- G. dialogue ----
ddefs = [
    ("A2", "A", "Buch = 책 (아들을 위한 책)"),
    ("B1", "B", "im ersten Stock = 2층 (독일식 1층)"),
    ("A2", "C", "Bingo = 도서관 빙고"),
    ("B1", "A", "Bibliotheksausweis = 도서관 카드"),
    ("B1", "B", "behalten = 빌려 두다"),
]
dnums = [reg_ex(lv, "대화 완성", k, nt) for lv, k, nt in ddefs]
bf.head("G　DIALOG　대화 완성", 24)
bf.para(f"— Guten Tag! Ich suche ein Buch für meinen Sohn. — Gern. Wie alt ist er? — Er ist neun, und er mag Tiere. — Dann ist dieses ({dnums[0]})___ perfekt: „Tiere im Herbst“. Mehr Tierbücher finden Sie im ersten ({dnums[1]})___. — Danke! Gibt es heute auch das ({dnums[2]})___? — Ja, um elf Uhr im Kinderzimmer. Bitte zeigen Sie mir noch Ihren ({dnums[3]})___. — Hier ist er. Wie lange kann ich das Buch ({dnums[4]})___? — Drei Wochen. Viel Spaß beim Lesen!", 20.5)
bf.expl("선택지:")
for n, opts in zip(dnums, [
    "A. Buch · B. Bett · C. Brot",
    "A. Keller · B. Stock · C. Garten",
    "A. Fußball · B. Kino · C. Bingo",
    "A. Bibliotheksausweis · B. Bibliotheksausflug · C. Bibliotheksautor",
    "A. essen · B. behalten · C. singen",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1520
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "쓰기", "열린 문제 — 기준은 쓰기 칸에, 모범 답안은 8면 쓰기 칸 안에", "항목대로 채점해요")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　SCHREIBEN　쓰기", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Mein Sonntag, der 25. Oktober». Erzählen Sie: Wie lange schlafen Sie? Was machen Sie am Morgen, am Nachmittag und am Abend? Schreiben Sie auch einen Satz über die Uhr! Die besten Texte drucken wir in VOL.2 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "독일어로 80–100단어를 쓰세요: «나의 10월 25일 일요일». 얼마나 자는지, 오전·오후·저녁에 무엇을 하는지 쓰고, 시계에 대한 문장도 하나 쓰세요.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, "MUSTER　모범 답안 (87단어)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Am Sonntag, dem 25. Oktober, schlafe ich eine Stunde länger. Dann frühstücke ich langsam mit meiner Familie. Um elf Uhr gehe ich in den Park, denn die Sonne scheint. Am Nachmittag lese ich mein neues Buch aus der Bibliothek. Am Abend koche ich eine Suppe mit Kürbis. Danach rufe ich meine Freundin an. Wir sprechen über das Fußballspiel am Samstag. Dortmund hat gewonnen, und wir freuen uns. Der Sonntag mit 25 Stunden ist mein Lieblingstag. Ich gehe früh ins Bett, denn am Montag beginnt die Arbeit wieder.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 296
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANTWORTEN　모든 정답과 해설 (1–8면)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 제 {pg} 면 —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13.0, "sans", False, INK, 1.26, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
