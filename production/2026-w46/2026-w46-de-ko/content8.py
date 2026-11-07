# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-de-ko/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN · 연습과 답", "Die Lucerna", "SCHLUSSTEST · 최종 테스트 · Alle Antworten unten auf dieser Seite — 모든 답은 이 페이지 하단에")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "A", "beginnt(3인칭 단수)"),
    ("A2", "B", "bastelt(3인칭 단수)"),
    ("A2", "A", "geht(3인칭 단수)"),
    ("A2", "B", "singt(3인칭 단수)"),
    ("A2", "A", "schaut(3인칭 단수)"),
    ("B1", "B", "sieht(3인칭 단수)"),
    ("A2", "B", "erzählt(3인칭 단수)"),
    ("B1", "A", "beginnt(3인칭 단수)"),
]
cnums = [reg_ex(lv, "빈칸 채우기", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · LÜCKENTEXT · 빈칸 채우기", 24)
bf.para(f"Lena freut sich auf die Novemberwoche. Am Montag ({cnums[0]})___ die Schule wieder, und Lena ({cnums[1]})___ eine Laterne aus Papier. Am Mittwoch ({cnums[2]})___ sie mit ihrer Klasse beim Laternenumzug mit und ({cnums[3]})___ Martinslieder. Am Freitagabend ({cnums[4]})___ sie Deutschland in Belgrad. Am Sonntag ({cnums[5]})___ sie die NFL in München im Fernsehen. In der Schule ({cnums[6]})___ Lena: „Die Woche war toll! Der Karneval ({cnums[7]})___ um 11.11 Uhr.“", 20.5)
bf.bridge("선택지:")
for n, opts in zip(cnums, [
    "A. beginnt · B. beginnen · C. begann",
    "A. basteln · B. bastelt · C. bastelte",
    "A. geht · B. gehen · C. ging",
    "A. singen · B. singt · C. sang",
    "A. schaut · B. schauen · C. schaute",
    "A. sehen · B. sieht · C. sah",
    "A. erzählen · B. erzählt · C. erzählte",
    "A. beginnt · B. beginnen · C. begann",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)

# ---- B. general MC ----
bf.head("B · WISSENSFRAGEN · 퀴즈", 24)
bf.ex("B1", "객관식", "A", "카니발은 11시 11분에 개막",
      "Die Karnevalssession beginnt um... A. 11.11 Uhr · B. 15.30 Uhr · C. 20.45 Uhr", size=19.5, gap=8)
bf.ex("A2", "객관식", "B", "금요일 세르비아 원정",
      "Deutschland spielt am Freitag in... A. Berlin · B. Belgrad · C. München", size=19.5, gap=8)
bf.ex("A2", "객관식", "C", "NFL 일요일 15시 30분",
      "Das NFL-Spiel in München beginnt um... A. 11.11 Uhr · B. 20.45 Uhr · C. 15.30 Uhr", size=19.5, gap=8)
bf.ex("B1", "객관식", "A", "추모의 날은 11월 15일",
      "Der Volkstrauertag ist am... A. 15. November · B. 11. November · C. 22. November", size=19.5, gap=8)
bf.ex("B1", "객관식", "B", "가정용 전기세는 2.05센트",
      "Die Stromsteuer für Haushalte beträgt... A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent", size=19.5, gap=8)
bf.ex("A2", "객관식", "B", "감독은 11월 5일에 명단을 발표한다",
      "Klopp nennt seinen Kader am... A. 13. November · B. 5. November · C. 9. November", size=19.5, gap=8)
bf.ex("B1", "객관식", "A", "ZDF 13시 30분부터 생중계",
      "Die Gedenkstunde überträgt ab 13.30 Uhr... A. das ZDF · B. RTL · C. die ARD", size=19.5, gap=8)
bf.ex("A2", "객관식", "C", "Totensonntag는 11월 22일",
      "Der Totensonntag ist am... A. 15. November · B. 18. November · C. 22. November", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C · LESEVERSTEHEN · 읽기", 24)
bf.para("Familie Berger aus Stuttgart hat am Montag wieder Schule: Die Kinder gehen um halb acht aus dem Haus. Am Mittwoch bastelt die Familie eine Laterne aus Papier. Am Freitag schaut sie Deutschland in Belgrad im Fernsehen. Am Sonntag schaut sie das NFL-Spiel um 15.30 Uhr. „Eine Woche mit Laternen und Football“, sagt Frau Berger.", 20.5)
bf.ex("B1", "객관식", "A", "halb acht = 7:30",
      "Wann gehen die Kinder aus dem Haus? A. um halb acht · B. um acht · C. um halb neun", size=19.5, gap=8)
bf.ex("A2", "객관식", "B", "수요일에 등불 만들기",
      "Was bastelt die Familie am Mittwoch? A. ein Kostüm · B. eine Laterne · C. einen Kürbis", size=19.5, gap=8)
bf.ex("A2", "객관식", "A", "금요일에 독일 보기",
      "Was schaut die Familie am Freitag? A. Deutschland in Belgrad · B. die NFL · C. den Karneval", size=19.5, gap=8)
bf.ex("B1", "객관식", "B", "NFL 일요일 15시 30분",
      "Wann schaut die Familie das NFL-Spiel? A. Samstag 18.30 Uhr · B. Sonntag 15.30 Uhr · C. Freitag 20.45 Uhr", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D · SÄTZE BAUEN · 문장 만들기", 24)
bf.ex("A2", "문장 만들기", "Die Karnevalssession beginnt am Mittwoch.", "시간 표현, 동사는 두 번째",
      "die Karnevalssession / beginnt / am Mittwoch → ___", instr="문장 만들기", size=19.5, gap=8)
bf.ex("A2", "문장 만들기", "Wir basteln eine Laterne aus Papier.", "주어-동사-목적어 순서",
      "wir / basteln / eine Laterne / aus Papier → ___", instr="문장 만들기", size=19.5, gap=8)
bf.ex("B1", "문장 만들기", "Die Kinder gehen am Montag wieder in die Schule.", "시간 표현이 먼저, 동사는 두 번째",
      "die Kinder / gehen / am Montag / wieder in die Schule → ___", instr="문장 만들기", size=19.5, gap=8)
bf.ex("B1", "문장 만들기", "Am Sonntag ist Volkstrauertag in ganz Deutschland.", "장소와 시간이 먼저, 동사는 두 번째",
      "am Sonntag / ist / Volkstrauertag / in ganz Deutschland → ___", instr="문장 만들기", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E · ÜBERSETZEN · 번역", 24)
bf.ex("A2", "번역", "카니발은 11시 11분에 쾰른에서 개막합니다.", "beginnen＝시작하다",
      "Der Karneval beginnt um 11.11 Uhr in Köln.（한국어로 번역하세요）", instr="번역", size=19.5, gap=8)
bf.ex("A2", "번역", "수요일에 등불을 만듭니다.", "basteln＝만들다",
      "Ich bastle am Mittwoch eine Laterne.（한국어로 번역하세요）", instr="번역", size=19.5, gap=8)
bf.ex("B1", "번역", "학교는 11월 9일에 다시 시작했습니다.", "wieder begonnen＝다시 시작했다",
      "Die Schule hat am 9. November wieder begonnen.（한국어로 번역하세요）", instr="번역", size=19.5, gap=8)
bf.ex("B1", "번역", "Am Sonntag schaue ich das NFL-Spiel.", "경기를 보다＝das Spiel schauen",
      "일요일에 NFL 경기를 봅니다.（독일어로 번역하세요）", instr="독일어로 번역", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F · WÖRTER PAAREN · 단어 짝짓기", 24)
bf.match_set("B1", "단어 짝짓기",
             ["der Mantel", "die Laterne", "das Geisterspiel", "die Versöhnung"],
             ["das Licht aus Papier, das die Kinder am Abend tragen",
              "der warme Umhang, den Martin mit dem Bettler teilte",
              "die Aussöhnung nach einem Streit — Frieden zwischen Menschen",
              "ein Spiel ohne Zuschauer im Stadion"],
             ["b", "a", "d", "c"],
             ["Mantel=망토 b", "Laterne=등불 a", "Geisterspiel=무관중 경기 d", "Versöhnung=화해 c"],
             instr="단어와 뜻 짝짓기")

# ---- G. dialogue ----
ddefs = [
    ("A2", "B", "singst(2인칭 단수)"),
    ("A2", "A", "macht(2인칭 복수)"),
    ("A2", "A", "essen(1인칭 복수)"),
    ("B1", "B", "machst(2인칭 단수)"),
    ("B1", "A", "schaue(1인칭 단수)"),
]
dnums = [reg_ex(lv, "대화 완성", k, nt) for lv, k, nt in ddefs]
bf.head("G · DIALOG · 대화 완성", 24)
bf.para(f"— Hallo, Lena! Bastelst du eine Laterne? — Ja, für St. Martin! Am Mittwoch gehen wir mit. — ({dnums[0]})___ du auch Martinslieder? — Ja, mit meiner Klasse. — Und was ({dnums[1]})___ ihr am Abend? — Wir singen und laufen mit den Laternen. Am Sonntag ({dnums[2]})___ wir Brezeln und schauen die NFL. — Lecker! Und was ({dnums[3]})___ du am Freitag? — Ich ({dnums[4]})___ Deutschland in Belgrad im Fernsehen!", 20.5)
bf.bridge("선택지:")
for n, opts in zip(dnums, [
    "A. singe · B. singst · C. singen",
    "A. macht · B. machen · C. machst",
    "A. essen · B. esse · C. esst",
    "A. machen · B. machst · C. macht",
    "A. schaue · B. schaust · C. schaut",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1520
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "쓰기", "열린 과제 — 쓰기 상자의 항목을 따르세요. 모범 답안은 이 페이지의 상자 안에 있습니다", "나열된 항목에 따라 채점됩니다")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · SCHREIBEN · 쓰기", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Novemberwoche». Erzählen Sie: Was basteln Sie? Welche Spiele schauen Sie? Mit wem? Schreiben Sie auch einen Satz über St. Martin oder den Volkstrauertag! Die besten Texte drucken wir in VOL.4 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "독일어로 80~100단어로 쓰세요. «11월의 나의 한 주». 무엇을 만드는지, 어떤 경기를 누구와 보는지 말하고——성 마르틴의 날이나 추모의 날에 대해 한 문장을 더하세요.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MUSTER · 모범 답안 (84단어)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche bastle ich eine Laterne. Am Mittwoch singe ich mit meiner Klasse Martinslieder und gehe beim Laternenumzug mit. Am Freitag schaue ich mit meiner Familie Deutschland in Belgrad im Fernsehen. Das Spiel ist ein Geisterspiel — ohne Zuschauer. Am Sonntag schaue ich die NFL in München im Fernsehen. Die Lions spielen gegen die Patriots. Der Karneval beginnt um 11.11 Uhr in Köln. Am Sonntag esse ich Brezeln und trinke Apfelschorle. Am Montag gehe ich wieder in die Schule. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 320
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "ANTWORTEN · 모든 답과 해설（1~8쪽）", 26, "sans", True, OLIVE)
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
