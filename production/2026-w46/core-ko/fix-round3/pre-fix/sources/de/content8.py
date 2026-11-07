# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ko-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 시험과 답 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("시험과 답 · Test und Antworten", "Lucerna", "제8면 · 이번 주의 큰 시험 + 모든 답")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 이번 주 연표", 21, OLIVE, 5)
f.ex("B1", "Lückentext", "A", "Der Tag der Feuerwehr ist Montag, der 9. November",
     "소방의 날은 11월 ___일이에요. (A. 9 · B. 11)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die Suneung ist am Donnerstag, dem 19. November",
     "수능은 11월 ___일이에요. (A. 19 · B. 29)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die Geschichtsprüfung ist Samstag, der 28. November",
     "한능검 시험은 11월 ___일이에요. (A. 28 · B. 6)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Der Tag mit den drei Namen ist der 11. November",
     "이름이 세 개인 날은 11월 ___일이에요. (A. 11 · B. 9)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Samsung zieht mit 3:2 weiter",
     "삼성은 KIA를 ___승 2패로 이겼어요. (A. 3 · B. 2)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Ein Chinakohl: 5.557 Won",
     "배추 한 포기는 ___원이에요. (A. 5,557 · B. 20,269)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Garnelen: 20.269 Won pro Kilo",
     "새우젓 1킬로그램은 ___원이에요. (A. 20,269 · B. 5,557)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Seoraksan, echte Beobachtung: Höhepunkt am 16. Oktober",
     "설악산 실제 관측 절정은 10월 ___일이었어요. (A. 16 · B. 20)", size=13.8, gap=0)
f.head("B · 일반 문제", 21, OLIVE, 5)
f.ex("A2", "Auswahl", "A", "Dieses Jahr 551.864 Prüflinge",
     "올해 수험생은 몇 명이에요? A. 551,864명 · B. 1,312명 · C. 3,271명", size=13.8, gap=0)
f.ex("B1", "Auswahl", "B", "1.312 Prüfungsorte im ganzen Land",
     "시험장은 전국에 몇 곳이에요? A. 551,864곳 · B. 1,312곳 · C. 312곳", size=13.8, gap=0)
f.ex("B1", "Auswahl", "A", "Wolchulsan, Forstbehörde: Höhepunkt am 9. November",
     "월출산 산림청 예보의 절정은 언제예요? A. 11월 9일 · B. 11월 11일 · C. 11월 4일", size=13.8, gap=0)
f.ex("B1", "Auswahl", "B", "Naejangsan, Parks-Behörde: Höhepunkt am 11. November",
     "내장산 공단 예보의 절정은 언제예요? A. 11월 4일 · B. 11월 11일 · C. 11월 9일", size=13.8, gap=0)
f.ex("B1", "Auswahl", "B", "Duryunsan, Forstbehörde: Höhepunkt am 11. November",
     "두륜산 산림청 예보의 절정은 언제예요? A. 11월 4일 · B. 11월 11일 · C. 11월 9일", size=13.8, gap=0)
f.ex("B1", "Auswahl", "A", "Playoff, Spiel 1, 26. Oktober: KIA 5:1",
     "플레이오프 1차전은 어떻게 됐어요? A. KIA 5대 1 승리 · B. 삼성 8대 3 승리 · C. 비로 취소", size=13.8, gap=0)
f.ex("B1", "Auswahl", "A", "Anmeldeschluss: 10. November, 17 Uhr",
     "한능검 정기 접수는 언제 닫혀요? A. 11월 10일 17시 · B. 11월 13일 · C. 11월 28일", size=13.8, gap=0)
f.ex("A2", "Auswahl", "B", "Die Waldbrand-Warnzeit dauert bis zum 15. Dezember",
     "산불조심기간은 언제까지예요? A. 11월 9일까지 · B. 12월 15일까지 · C. 11월 19일까지", size=13.8, gap=0)
f.head("C · 읽고 답하기", 21, OLIVE, 5)
f.para("지민이는 대학생이에요. 수요일에 친구에게 가래떡을 나눠 줘요. 토요일에는 가족과 김장을 도와요. 다음 주에는 한능검 시험을 준비해요. 지민이는 한국사를 좋아해요.", 15, lh=1.3, split=False)
f.ex("A2", "Auswahl", "B", "Jimin teilt am Mittwoch Garaetteok",
     "지민이는 수요일에 무엇을 해요? A. 단풍을 봐요 · B. 가래떡을 나눠 줘요 · C. 시험을 봐요", size=13.8, gap=0)
f.ex("A2", "Auswahl", "A", "Am Samstag beim Kimjang helfen",
     "토요일에 지민이는 무엇을 해요? A. 가족과 김장을 도와요 · B. 야구를 봐요 · C. 시험을 봐요", size=13.8, gap=0)
f.ex("A2", "Auswahl", "B", "Nächste Woche die Geschichtsprüfung vorbereiten",
     "다음 주에 지민이는 무엇을 준비해요? A. 수능 · B. 한능검 시험 · C. 빼빼로데이", size=13.8, gap=0)
f.ex("B1", "Auswahl", "C", "Jimin mag koreanische Geschichte",
     "지민이는 무엇을 좋아해요? A. 야구 · B. 사과 · C. 한국사", size=13.8, gap=0)
f.head("D · 문장 만들기", 21, OLIVE, 5)
f.ex("A2", "Sätze bilden", "저는 수요일에 가래떡을 나눠 줘요.", "Wortstellung: Subjekt + Zeit + Objekt + Verb",
     "저는 / 수요일에 / 가래떡을 나눠 줘요 → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("A2", "Sätze bilden", "우리는 김장을 도와요.", "Wortstellung: Subjekt + Objekt + Verb",
     "우리는 / 김장을 / 도와요 → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "지민이는 단풍을 보러 가요.", "보러 가요 = hingehen, um zu sehen",
     "지민이는 / 단풍을 / 보러 가요 → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "수험생은 도서관에서 공부해요.", "Für den Ort einer Handlung steht 에서",
     "수험생은 / 도서관에서 / 공부해요 → ___", instr="Sätze bilden", size=13.8, gap=0)
f.head("E · 번역", 21, OLIVE, 5)
f.ex("A2", "Übersetzen", "Der 12. November ist D-7.", "Siehe Seite 1",
     "11월 12일은 D-7예요. → ___", instr="Übersetzen", size=13.8, gap=0)
f.ex("A2", "Übersetzen", "Kimjang ist in vollem Gange.", "Siehe Seite 2",
     "김장이 한창이에요. → ___", instr="Übersetzen", size=13.8, gap=0)
f.ex("B1", "Übersetzen", "11월 11일은 이름이 세 개예요.", "Siehe Seite 3",
     "Der 11. November hat drei Namen. → ___", instr="Übersetzen", size=13.8, gap=0)
f.ex("B2", "Übersetzen", "저는 수요일에 친구에게 가래떡을 나눠 줘요.", "Siehe Seite 5",
     "Am Mittwoch teile ich Garaetteok mit einer Freundin. → ___", instr="Übersetzen", size=13.8, gap=0)
f.head("F · 이번 주의 말", 21, OLIVE, 5)
f.match_set("B2", "Paare zuordnen",
            ["절정", "김장", "예보", "관측"],
            ["겨울 김치를 담그는 일",
             "단풍이 가장 아름다운 때",
             "실제로 본 날짜나 날씨",
             "미리 알린 날짜나 날씨"],
            ["b", "a", "d", "c"],
            ["절정 = beste Zeit b", "김장 = Winter-Kimchi a", "예보 = Vorhersage im Voraus d", "관측 = echte Beobachtung c"],
            instr="Wort–Bedeutung zuordnen")
f.head("G · 도서관에서", 21, OLIVE, 5)
f.ex("B1", "Lückentext", "A", "Am Mittwoch Garaetteok teilen",
     "— 수요일에 무엇을 해요? — ___을 나눠 줘요. (A. 가래떡 · B. 김치)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Kimjang = Winter-Kimchi",
     "— 김장은 뭐예요? — 겨울 ___를 담그는 일이에요. (A. 김치 · B. 사과)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die reguläre Anmeldung endet am 10. November um 17 Uhr",
     "— 한능검 정기 접수는 언제 닫혀요? — 11월 10일 ___시에 닫혀요. (A. 17 · B. 13)", size=13.8, gap=0, bw=334)
f.ex("B1", "Lückentext", "A", "Die Daten unterscheiden sich, weil die Kriterien sich unterscheiden",
     "— 단풍 절정 날짜가 왜 달라요? — ___이 달라서예요. (A. 기준 · B. 날씨)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die Maßnahmen gelten nur am 19. November",
     "— 수능 조치는 언제 적용돼요? — 11월 ___일에만 적용돼요. (A. 19 · B. 9)", size=13.8, gap=0, bw=354)
f.head("H · 써 보기", 21, OLIVE, 5)
MODELO = ("나의 11월 11일은 세 가지 이름으로 시작해요. "
          "아침에는 친구에게 빼빼로를 건네고, 점심에는 가래떡을 나눠 먹어요. "
          "농업인의 날이라 쌀밥이 더 고마워요. 오후에는 가족과 김장을 도와요. "
          "배추에 양념을 버무리면 손이 차가워져요. 저녁에는 따뜻한 김치찌개를 먹어요. "
          "수능까지 일주일이 남았지만, 오늘은 나누는 날이에요. "
          "내일도 친구와 함께 단풍 사진을 보고 싶어요.")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"(Schreibaufgabe — es gibt keine einzige richtige Antwort). Unten steht ein Beispiel mit {NCHARS} Zeichen.")
f.ex("B1", "Schreiben", "(offene Aufgabe — Mustertext unten)", f"Mustertext in Abschnitt H auf dieser Seite ({NCHARS} Zeichen)",
     "「나의 11월 11일」에 대해 150~200자로 쓰세요. 빼빼로데이, 농업인의 날, 가래떡데이 중에서 하나를 고르세요.", instr="Schreiben", size=13.8, gap=0)
f.para("예: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 답 =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "답 · Lösungen — nach Seiten geordnet; einfach die Nummer suchen", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Jede Aufgabe mit kurzer Anmerkung · ✓ = Schreibaufgabe mit Mustertext", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 제{pg}면 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schreiben":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-siheom.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model chars:", NCHARS)
