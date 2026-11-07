# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-ko/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN · 연습과 정답", "Die Lucerna", "SCHLUSSTEST · 종합 평가 · Alle Antworten unten auf dieser Seite · 정답은 이 면 아래쪽에")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "spielt(3인칭 단수)"),
    ("A2", "A", "beginnt(3인칭 단수)"),
    ("A2", "B", "kauft(3인칭 단수)"),
    ("A2", "C", "schnitzt는 호박을 조각해요"),
    ("A2", "B", "schläft(3인칭 단수)"),
    ("B1", "B", "Tankrabatt 유가 할인"),
    ("A2", "A", "geht(3인칭 단수)"),
    ("B1", "B", "erzählt(3인칭 단수)"),
]
cnums = [reg_ex(lv, "빈칸 채우기", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · LÜCKENTEXT · 빈칸 채우기", 24)
bf.para(f"Lena freut sich auf die Fußballwoche. Am Dienstag sieht sie Bayern bei Atlético Madrid, am Mittwoch Dortmund gegen Real Betis. Am Donnerstag ({cnums[0]})___ Hoffenheim bei Crystal Palace, und am Freitag ({cnums[1]})___ die Bundesliga mit Hamburg gegen Gladbach. Am Samstag ({cnums[2]})___ Lena einen Kürbis und ({cnums[3]})___ ihn zu Hause. Am Sonntag ({cnums[4]})___ sie lange, denn die Woche war anstrengend. In der Schule erzählt sie: „Die Fußballwoche war toll! Und der ({cnums[5]})___ läuft noch bis Dezember.“ Am Montag ({cnums[6]})___ Lena wieder in die Schule und ({cnums[7]})___ von den Spielen.", 20.5)
bf.expl("선택지:")
for n, opts in zip(cnums, [
    "A. spielen · B. spielt · C. spieltet",
    "A. beginnt · B. beginnen · C. begann",
    "A. kaufen · B. kauft · C. kaufte",
    "A. malt · B. kocht · C. schnitzt",
    "A. schlafen · B. schläft · C. schlief",
    "A. Spieltag · B. Tankrabatt · C. Advent",
    "A. geht · B. gehen · C. ging",
    "A. erzählen · B. erzählt · C. erzählte",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)

# ---- B. general MC ----
bf.head("B · WISSENSFRAGEN · 종합 문제", 24)
bf.ex("B1", "객관식", "A", "세금 인하는 2026년 12월 31일까지예요",
      "Der Tankrabatt läuft bis... A. 31. Dezember 2026 · B. 1. November · C. 31. Oktober", size=19.5, gap=8)
bf.ex("A2", "객관식", "B", "바이에른은 화요일에 아틀레티코 원정 경기를 해요",
      "Bayern spielt am Dienstag bei... A. Galatasaray · B. Atlético Madrid · C. Real Betis", size=19.5, gap=8)
bf.ex("A2", "객관식", "A", "유로파리그에서 호펜하임은 크리스털 팰리스 원정을 가요",
      "Hoffenheim spielt in der Europa League bei... A. Crystal Palace · B. Marseille · C. Manchester City", size=19.5, gap=8)
bf.ex("B1", "객관식", "B", "이번 주 바덴뷔르템베르크는 방학이 끝났어요",
      "In welchem Bundesland sind die Ferien schon vorbei? A. Bayern · B. Baden-Württemberg · C. Berlin", size=19.5, gap=8)
bf.ex("B1", "객관식", "B", "ZEW 전망은 28.1이에요",
      "Der ZEW-Index: Die Erwartungen fielen im Oktober auf... A. 34,7 · B. 28,1 · C. 47,1", size=19.5, gap=8)
bf.ex("A2", "객관식", "A", "금요일 함부르크–묀헨글라트바흐전으로 개막해요",
      "Der 9. Spieltag beginnt am Freitag mit... A. Hamburg–Gladbach · B. Stuttgart–Bremen · C. Köln–Leverkusen", size=19.5, gap=8)
bf.ex("B1", "객관식", "B", "10월 26일 방송은 집에서의 돌봄을 다뤘어요",
      "„Hart aber fair“ diskutierte in der Sendung am 26. Oktober... A. die Stromsteuer · B. die Pflege zu Hause · C. den Tankrabatt", size=19.5, gap=8)
bf.ex("A2", "객관식", "B", "모든 성인의 날 11월 1일",
      "Allerheiligen ist am... A. 31. Oktober · B. 1. November · C. 2. November", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C · LESEVERSTEHEN · 읽기 이해", 24)
bf.para("Familie Berger aus Stuttgart hat am Montag wieder Schule: Die Kinder gehen um halb acht aus dem Haus. Am Dienstagabend schaut die Familie Bayern bei Atlético im Fernsehen. Am Samstag fährt sie zum Markt und kauft einen Kürbis. Am Sonntag schaut sie Hoffenheim gegen Schalke um 19.30 Uhr. „Eine Woche mit Fußball und Kürbis“, sagt Frau Berger.", 20.5)
bf.ex("B1", "객관식", "A", "halb acht = 7:30",
      "Wann gehen die Kinder aus dem Haus? A. um halb acht · B. um acht · C. um halb neun", size=19.5, gap=8)
bf.ex("A2", "객관식", "B", "화요일에는 바이에른의 아틀레티코 원정 경기를 봐요",
      "Was schaut die Familie am Dienstag? A. Dortmund–Betis · B. Bayern bei Atlético · C. Hoffenheim–Schalke", size=19.5, gap=8)
bf.ex("A2", "객관식", "A", "토요일에는 호박을 사요",
      "Was kauft die Familie am Samstag? A. einen Kürbis · B. ein Buch · C. ein Kostüm", size=19.5, gap=8)
bf.ex("B1", "객관식", "B", "호펜하임–샬케전은 일요일 19:30에 시작해요",
      "Wann spielt Hoffenheim gegen Schalke? A. Samstag 18.30 Uhr · B. Sonntag 19.30 Uhr · C. Freitag 20.30 Uhr", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D · SÄTZE BAUEN · 문장 만들기", 24)
bf.ex("A2", "문장 만들기", "Die Bundesliga beginnt am Freitag.", "시간 부사구가 앞에 오고 동사는 두 번째 자리에 와요",
      "die Bundesliga / beginnt / am Freitag → ___", instr="문장 만들기", size=19.5, gap=8)
bf.ex("A2", "문장 만들기", "Wir schauen Bayern bei Atlético.", "주어·동사·목적어 순서예요",
      "wir / schauen / Bayern / bei Atlético → ___", instr="문장 만들기", size=19.5, gap=8)
bf.ex("B1", "문장 만들기", "Die Kinder gehen am Montag wieder in die Schule.", "시간 부사구가 앞에 오고 동사는 두 번째 자리에 와요",
      "die Kinder / gehen / am Montag / wieder in die Schule → ___", instr="문장 만들기", size=19.5, gap=8)
bf.ex("B1", "문장 만들기", "In Bayern dauern die Ferien noch an.", "장소가 앞에 오고 동사는 두 번째 자리에 와요",
      "in Bayern / dauern / die Ferien / noch an → ___", instr="문장 만들기", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E · ÜBERSETZEN · 번역", 24)
bf.ex("A2", "번역", "유가 할인은 12월까지 계속돼요.", "laufen = 계속되다",
      "Der Tankrabatt läuft bis Dezember. (한국어로)", instr="번역", size=19.5, gap=8)
bf.ex("A2", "번역", "저는 화요일에 축구를 봐요.", "schauen = 보다",
      "Ich schaue am Dienstag Fußball. (한국어로)", instr="번역", size=19.5, gap=8)
bf.ex("B1", "번역", "학교가 다시 개학했어요.", "wieder begonnen = 다시 시작하다",
      "Die Schule hat wieder begonnen. (한국어로)", instr="번역", size=19.5, gap=8)
bf.ex("B1", "번역", "Am Sonntag schlafe ich eine Stunde länger.", "한 시간 더 자기 = eine Stunde länger schlafen",
      "일요일에 한 시간 더 자요. (독일어로)", instr="번역", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F · WÖRTER PAAREN · 단어 짝짓기", 24)
bf.match_set("B1", "단어 짝짓기",
             ["der Tankrabatt", "die Pflege", "der Advent", "der Pausenhof"],
             ["die Zeit vor Weihnachten, in der man plant und bastelt",
              "die Ermäßigung auf die Energiesteuer beim Tanken",
              "der Hof der Schule, auf dem die Kinder in der Pause spielen",
              "die Hilfe für Menschen, die nicht mehr allein leben können"],
             ["b", "d", "a", "c"],
             ["Tankrabatt=유가 할인 b", "Pflege=돌봄 d", "Advent=대림절 a", "Pausenhof=쉬는 시간 운동장 c"],
             instr="단어와 뜻 짝짓기")

# ---- G. dialogue ----
ddefs = [
    ("A2", "B", "schaust(2인칭 단수)"),
    ("A2", "A", "siehst(2인칭 단수)"),
    ("A2", "A", "kochen(1인칭 복수)"),
    ("B1", "B", "machst(2인칭 단수)"),
    ("B1", "A", "gehe(1인칭 단수)"),
]
dnums = [reg_ex(lv, "대화 완성", k, nt) for lv, k, nt in ddefs]
bf.head("G · DIALOG · 대화 완성", 24)
bf.para(f"— Hallo, Lena! Schaust du am Dienstag Fußball? — Ja, Bayern bei Atlético! Um 21.00 Uhr. — Und am Mittwoch? — Dortmund gegen Betis. Ich bin für Dortmund. — ({dnums[0]})___ du am Sonntag auch Fußball? — Ja, Hoffenheim gegen Schalke um 19.30 Uhr. — Mit wem ({dnums[1]})___ du das Spiel? — Mit meiner Familie, zu Hause. Wir ({dnums[2]})___ Kürbissuppe. — Lecker! Und was ({dnums[3]})___ du am Montag? — Ich ({dnums[4]})___ wieder in die Schule. Die Ferien sind vorbei!", 20.5)
bf.expl("선택지:")
for n, opts in zip(dnums, [
    "A. schaut · B. schaust · C. schauen",
    "A. siehst · B. sehen · C. sieht",
    "A. kochen · B. koche · C. kocht",
    "A. machen · B. machst · C. macht",
    "A. gehe · B. geht · C. gehen",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1520
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "쓰기", "열린 문제 — 기준은 쓰기 칸에, 모범 답안은 8면 쓰기 칸 안에", "항목대로 채점해요")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · SCHREIBEN · 쓰기", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Fußballwoche». Erzählen Sie: Welche Spiele schauen Sie? Mit wem? Was essen Sie beim Spiel? Schreiben Sie auch einen Satz über den Tankrabatt oder die Pflege! Die besten Texte drucken wir in VOL.3 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "독일어로 80–100단어로 《나의 축구 주간》을 써 보세요. 어떤 경기를 보는지, 누구와 함께 보는지, 경기를 보며 무엇을 먹는지 쓰고, 유가 할인이나 돌봄에 대한 문장도 한 문장 써요.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MUSTER · 모범 답안 (84단어)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche schaue ich viel Fußball. Am Dienstag sehe ich Bayern bei Atlético, am Mittwoch Dortmund gegen Betis. Am Donnerstag spielt Hoffenheim bei Crystal Palace. Am Freitag sehe ich Hamburg gegen Gladbach mit meinem Bruder. Wir essen Brezeln und trinken Apfelschorle. Am Sonntag schauen wir Hoffenheim gegen Schalke. Der Tankrabatt freut mich sehr: Ich tanke 50 Liter und spare rund 8,35 Euro. Am Samstag kaufe ich einen Kürbis und schnitze ihn mit Lena. Am Montag gehe ich zur Arbeit. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 320
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "ANTWORTEN · 모든 정답과 해설 (1–8면)", 26, "sans", True, OLIVE)
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
