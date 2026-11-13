# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("KULTUR　문화", "Die Lucerna", "A2 → B1　Weihnachtsmärkte & die stille Woche　크리스마스 시장과 조용한 한 주")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Weihnachtsmärkte öffnen — aber am Sonntag bleiben sie zu", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: A2 → B1")
f.para("Am Montag, dem 16. November, öffnen in Köln zwei große Weihnachtsmärkte: der Markt am Dom auf dem Roncalliplatz und der Markt der Engel auf dem Neumarkt. Beide Märkte sind bis zum 23. Dezember geöffnet — mit einer Ausnahme.")
f.para("Die Ausnahme ist der Sonntag, der 22. November: Totensonntag. An diesem stillen Tag bleiben die Märkte geschlossen. Erst am Montag öffnen sie wieder. Auch der Hafenweihnachtsmarkt am Schokoladenmuseum ist schon seit dem 13. November geöffnet.")
f.para("Was gibt es auf einem Weihnachtsmarkt? Kleine Holzbuden mit Kunsthandwerk, Kerzen und Spielzeug. Dazu Glühwein für die Erwachsenen, Kinderpunsch für die Kinder — und überall der Duft von gebrannten Mandeln und Lebkuchen. Vor dem Dom steht ein großer, geschmückter Weihnachtsbaum.")
f.para("Ein Blick zurück: Vor fast 100 Jahren sah ein Weihnachtsmarkt noch ganz anders aus. Ein Gemälde von Wilhelm Ritter aus dem Jahr 1930 zeigt einen Weihnachtsmarkt in Nürnberg — auf der vorderen Insel Schütt: Holzbuden, Menschen, Lichter — und doch schon dieselbe Stimmung wie heute. Mehr dazu beim Bild auf dieser Seite.")
f.para("Und der Advent? Der erste Advent ist erst am Sonntag, dem 29. November. Die Märkte beginnen fast zwei Wochen früher. Wer den ersten Advent feiern will, muss noch warten — aber die Lichter leuchten schon. Viele Kinder haben ihren Adventskalender schon zu Hause — aber das erste Türchen öffnet sich erst am 1. Dezember.")
f.para("Wer einen Markt besuchen will, braucht warme Kleidung und etwas Zeit: Die Buden öffnen am Nachmittag und schließen am Abend. Am Wochenende ist es voller — wer es ruhiger mag, kommt unter der Woche. Kinder lieben die Karussells und die Lichter am Abend.")
f.para("Auch Aachen feiert: Der Aachener Weihnachtsmarkt öffnet am 20. November und bleibt bis zum 23. Dezember geöffnet. Wer in Nordrhein-Westfalen wohnt, hat die Wahl zwischen Köln und Aachen — beide Märkte sind berühmt für ihre Lichter und ihre Stimmung.")
f.para("Und was kostet ein Besuch? Der Eintritt ist frei — man zahlt nur, was man isst und trinkt. Ein Becher Glühwein kostet ein paar Euro, dazu ein Pfand für den Becher. Viele Besucher nehmen ihren Becher als Andenken mit nach Hause.")
f.para("Ein Tipp der Redaktion: Gehen Sie am besten an einem Wochentag — da ist es ruhiger als am Wochenende. Und nehmen Sie warme Kleidung mit: Abends wird es auf dem Markt schnell kalt.")
f.gloss("der Weihnachtsmarkt = 크리스마스 시장 · die Holzbude = 나무 가판대 · der Glühwein = 글뤼바인 · gebrannte Mandeln = 구운 아몬드 · der Lebkuchen = 레프쿠헨 · die Stimmung = 분위기.")
f.end_report()

# col 2: historical market painting (below the article flow; dynamic y so it never overlaps the flow)
ix2 = COLX[2]
iy3 = f.y + 20
image(p, "weihnachtsmarkt1930.jpg", ix2, iy3, CW, 323)
cy3 = caption(p, ix2, iy3 + 323, CW,
        "Weihnachtsmarkt in Nürnberg im Jahr 1930 — Gemälde von Wilhelm Ritter. Holzbuden, Menschen, Lichter: Die Stimmung ist heute noch dieselbe.",
        "Gemälde: Wilhelm Ritter (1860–1948) — public domain")
print("P3 image at", iy3, "ends", cy3)

# col 3: facts + vocab + Und Sie + Tipp (hand-rolled; CORRECTED height formula — see W45 KIT §geometry)
ix = COLX[3]
facts = ["Der Markt am Dom und der Markt der Engel öffnen am 16. November.",
         "Am 22. November bleiben die Märkte geschlossen — Totensonntag.",
         "Die offizielle Eröffnung am Dom ist am Dienstag, 17. November, um 19 Uhr."]
sy3 = 200
sh = 45 + 33 * len(facts) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in facts)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WEIHNACHTEN IN KÖLN", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 facts ends", sy3 + sh)
words = ["der Weihnachtsmarkt — 크리스마스 시장", "der Glühwein — 글뤼바인", "der Lebkuchen — 레프쿠헨",
         "der Adventskalender — 대림절 달력", "der Weihnachtsbaum — 크리스마스 트리", "die Kerze — 촛불"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WEIHNACHTSWÖRTER　크리스마스", 21, "sans", True, OLIVE)  # D5 (2026-11-12): @24pt 435.8px ran +34.9px past the box; @21pt 381.3px fits 400.5 (22pt leaves only 1.0px spare). No wording change.
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Gehen Sie gern auf einen Weihnachtsmarkt? Was trinken und essen Sie dort? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("크리스마스 시장에 가는 것을 좋아하나요? 거기서 무엇을 먹고 마시나요? 독일어로 두 문장 써 보세요!", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "크리스마스 시장에 가는 것을 좋아하나요? 거기서 무엇을 먹고 마시나요? 독일어로 두 문장 써 보세요!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 undsie ends", ey3 + eh)
tipp = "Tipp: Kommen Sie an einem Wochentag — da ist der Markt ruhiger als am Wochenende."
sy3 = ey3 + eh + 26
sh = 45 + 33 + 30.53 * len(wrap(tipp, "serif", False, 21.5, CW - 44))
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DER TIPP　편집부의 팁", 24, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, tipp, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1680  # fan-out: col3 stack taller than fr; P3 tip 3rd line crossed ex rule at 1608 (en precedent ey=1680)
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　3쪽 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8쪽　수준이 섞여 있습니다 — 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P3-ex")
e.head("A　RICHTIG ODER FALSCH?", 25)
e.bridge("3쪽 글을 읽으세요. 맞나요, 틀렸나요?")
e.ex("A2", "맞다/틀리다", "Richtig", "대성당 시장 11월 16일 개장",
     "Die Weihnachtsmärkte in Köln öffnen am 16. November. Richtig oder falsch?", instr="맞나요, 틀렸나요?", size=22, gap=8)
e.ex("A2", "맞다/틀리다", "Falsch", "Totensonntag에는 시장이 닫습니다",
     "Die Märkte sind am Totensonntag geöffnet. Richtig oder falsch?", instr="맞나요, 틀렸나요?", size=22, gap=8)
e.ex("A2", "맞다/틀리다", "Richtig", "대림절 첫 주일: 11월 29일",
     "Der erste Advent ist am 29. November. Richtig oder falsch?", instr="맞나요, 틀렸나요?", size=22, gap=8)
e.ex("B1", "맞다/틀리다", "Falsch", "1930년 그림: 뉘른베르크 시장",
     "Das Gemälde von Wilhelm Ritter zeigt einen Markt in Köln. Richtig oder falsch?", instr="맞나요, 틀렸나요?", size=22, gap=8)
e.ex("A2", "맞다/틀리다", "Richtig", "공식 개장: 11월 17일 19:00",
     "Die offizielle Eröffnung am Dom ist am 17. November um 19 Uhr. Richtig oder falsch?", instr="맞나요, 틀렸나요?", size=22, gap=8)
e.head("B　WÖRTER AUS DEM TEXT", 25)
e.bridge("상자 속 단어로 완성하세요.")
e.para("Weihnachtsmärkte · Glühwein · Lebkuchen · Advent · Weihnachtsbaum", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "빈칸 채우기", "Weihnachtsmärkte", "크리스마스 시장",
     "Am Montag öffnen in Köln der Markt am Dom und der Markt der Engel, zwei große ___.", instr="채우세요", size=22, gap=8)
e.ex("A2", "빈칸 채우기", "Glühwein", "글뤼바인",
     "Die Erwachsenen trinken auf dem Markt ___.", instr="채우세요", size=22, gap=8)
e.ex("A2", "빈칸 채우기", "Lebkuchen", "레프쿠헨",
     "Überall riecht es nach gebrannten Mandeln und ___.", instr="채우세요", size=22, gap=8)
e.ex("A2", "빈칸 채우기", "Advent", "대림절",
     "Der erste ___ ist am 29. November.", instr="채우세요", size=22, gap=8)
e.ex("A2", "빈칸 채우기", "Weihnachtsbaum", "크리스마스 트리",
     "Vor dem Dom steht ein großer, geschmückter ___.", instr="채우세요", size=22, gap=8)
e.head("C　LESEVERSTEHEN", 25)
e.bridge("정답을 고르세요.")
e.ex("A2", "선택 문제", "B", "항구 시장 11월 13일부터 개장",
     "Welcher Markt ist schon seit dem 13. November geöffnet? A. der Markt am Dom · B. der Hafenweihnachtsmarkt · C. der Markt der Engel", size=22, gap=8)
e.ex("A2", "선택 문제", "B", "시장은 12월 23일까지",
     "Bis wann sind die Märkte am Dom und am Neumarkt geöffnet? A. bis zum 22. November · B. bis zum 23. Dezember · C. bis zum 29. November", size=22, gap=8)
e.ex("A2", "선택 문제", "A", "그림은 1930년의 뉘른베르크",
     "Was zeigt das Gemälde von Wilhelm Ritter? A. einen Weihnachtsmarkt in Nürnberg im Jahr 1930 · B. den Kölner Dom heute · C. einen Adventskalender", size=22, gap=8)
e.ex("B1", "선택 문제", "A", "시장은 대림절 약 2주 전에 개장",
     "Wie viel früher als der erste Advent beginnen die Märkte? A. Sie öffnen fast zwei Wochen früher. · B. Der Advent ist schon vorbei. · C. Die Märkte sind neu.", size=22, gap=8)
e.head("D　SÄTZE BAUEN", 25)
e.bridge("단어를 모아 올바른 문장을 만드세요.")
e.ex("A2", "문장 만들기", "Am 16. November öffnen die Weihnachtsmärkte in Köln.", "시간 먼저, 동사는 두 번째",
     "am 16. November / öffnen / die Weihnachtsmärkte / in Köln → ___", instr="문장을 만드세요", size=22, gap=8)
e.ex("B1", "문장 만들기", "Am Totensonntag bleiben die Märkte geschlossen.", "시간 먼저, 동사는 두 번째",
     "am Totensonntag / bleiben / die Märkte / geschlossen → ___", instr="문장을 만드세요", size=22, gap=8)
e.ex("A2", "문장 만들기", "Vor dem Dom steht ein großer Weihnachtsbaum.", "장소, 동사는 두 번째",
     "vor dem Dom / steht / ein großer Weihnachtsbaum → ___", instr="문장을 만드세요", size=22, gap=8)
e.ex("B1", "문장 만들기", "Die Lichter leuchten schon vor dem ersten Advent.", "주어-동사 구조",
     "die Lichter / leuchten / schon / vor dem ersten Advent → ___", instr="문장을 만드세요", size=22, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-kultur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　스포츠", "Die Lucerna", "LEVEL B1　Ergebnisse & Rückkehr　결과와 리그 복귀")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Die Woche der Ergebnisse — und die Rückkehr der Liga", 32)
f.byline("Von der Lucerna-Sportredaktion　Leseniveau: B1")
f.para("Die Ergebnisse stehen fest: Am Dienstag und Mittwoch, dem 3. und 4. November, spielte die Champions League ihren 4. Spieltag der Ligaphase. Der FC Bayern gewann in Madrid bei Atlético mit 2:0 — die Tore schossen Lennart Karl und Konrad Laimer.")
f.para("Borussia Dortmund gewann zu Hause gegen Betis Sevilla mit 2:1. Doch es gab auch Niederlagen: RB Leipzig verlor gegen Manchester City mit 2:3, und der VfB Stuttgart verlor in Istanbul bei Galatasaray mit 0:2.")
f.para("Am Donnerstag, dem 5. November, spielten die anderen Europapokale: Bayer Leverkusen verlor in der Europa League gegen Marseille mit 0:1. Die TSG Hoffenheim spielte bei Crystal Palace 1:1. Der SC Freiburg gewann in der Conference League in Trabzon mit 1:0.")
f.para("In der Bundesliga fielen am 9. Spieltag 30 Tore in neun Spielen. Der FC Bayern gewann in Mainz mit 2:1. Borussia Dortmund schlug Elversberg mit 2:1. Das torreichste Spiel war Leipzig gegen Augsburg: 5:2. Der Hamburger SV gewann am Freitag gegen Gladbach mit 3:1.")
f.para("Am Montag, dem 16. November, spielt die Nationalmannschaft in Berlin gegen die Niederlande. Es ist das letzte Gruppenspiel der Nations League — und es geht um das Viertelfinale. Deutschland hat fünf Punkte, die Niederlande acht. Nur die ersten beiden kommen weiter.")
f.para("Und dann kehrt die Liga zurück: Am Freitag, dem 20. November, spielt Bayern gegen Köln. Am Samstag folgen fünf Spiele um 15.30 Uhr — und am Abend Schalke gegen Stuttgart. Der 10. Spieltag endet am Sonntag mit Bremen gegen Hamburg.")
f.gloss("das Tor = 골 · der Spieltag = 라운드 · torreich = 골이 많은 · die Ligaphase = 리그 단계 · weiterkommen = 진출하다.")
f.end_report()

# col 3: kopfball image + Und Sie
bx = COLX[3]
image(p, "kopfball.jpg", bx, 200, CW, 470)
cy3 = caption(p, bx, 670, CW, "Kopfball im Spiel: So sieht ein Duell in der Luft aus — um jeden Ball wird gekämpft. Am Freitag kehrt die Bundesliga zurück: Bayern gegen Köln. (Seite 4)",
              "Foto: DVIDS (Armed Forces Soccer Championship, Destin, Florida, 2010) — public domain")
ey3 = cy3 + 26
etvous = "Und Sie? Bundesliga oder Nationalelf? Wer gewinnt in München? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("분데스리가와 국가대표, 어느 쪽? 뮌헨에서 이기는 건? 독일어로 두 문장 써 보세요!", "sans", False, 20, CW - 44)) - 1)
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "UND SIE?　여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "분데스리가와 국가대표, 어느 쪽? 뮌헨에서 이기는 건? 독일어로 두 문장 써 보세요!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- results + fixture table (full width) ----
ty = 1140
p.text(MX, ty, "DIE ERGEBNISSE & DER SPIELPLAN　결과와 일정", 26, "sans", True, OLIVE)
rows = [
    ("Di 3.11.", "—", "Champions League: Atlético – Bayern 0:2"),
    ("Mi 4.11.", "—", "Champions League: Dortmund – Betis 2:1 · Leipzig – Man. City 2:3"),
    ("Do 5.11.", "—", "Europapokale: Leverkusen – Marseille 0:1 · Crystal Palace – Hoffenheim 1:1 · Trabzonspor – Freiburg 0:1"),
    ("Fr 6.11.", "20.30", "Bundesliga: Hamburg – Gladbach 3:1"),
    ("Sa 7.11.", "15.30", "Bundesliga: Mainz – Bayern 1:2 · Dortmund – Elversberg 2:1"),
    ("Sa 7.11.", "15.30", "Bundesliga: Leipzig – Augsburg 5:2 · Paderborn – Frankfurt 2:2"),
    ("Sa 7.11.", "18.30", "Bundesliga: Stuttgart – Bremen 1:0"),
    ("So 8.11.", "—", "Bundesliga: Köln – Leverkusen 1:2 · Freiburg – Union 2:0 · Hoffenheim – Schalke 2:1"),
    ("Mo 16.11.", "20.45", "Nations League: Deutschland – Niederlande (Berlin, ARD)"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Alle Zeiten in MEZ. Der 10. Spieltag: Freitag, 20. November, 20.30 Uhr Bayern – Köln. Samstag fünf Spiele um 15.30 Uhr, Schalke – Stuttgart um 18.30 Uhr. Sonntag: Augsburg – Mainz (15.30 Uhr), Bremen – Hamburg (17.30 Uhr). Die Champions League kehrt am 24. und 25. November zurück (Arsenal – Dortmund, Leipzig – Lens; Inter – Stuttgart, Lille – Bayern), die Europa League am 26. November (Dinamo Zagreb – Leverkusen, Hoffenheim – Sturm Graz)."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1740
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　4쪽 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8쪽　수준이 섞여 있습니다 — 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P4-ex")
e.head("A　LESEVERSTEHEN", 25)
e.bridge("4쪽을 읽고 정답을 고르세요.")
e.ex("B1", "선택 문제", "B", "바이에른, 아틀레티코에 원정 2-0 승리",
     "Wie spielte Bayern in Madrid? A. 1:2 · B. 2:0 · C. 1:1", size=22, gap=8)
e.ex("B1", "선택 문제", "B", "라이프치히, 맨시티에 2-3 패배",
     "Wie endete Leipzig gegen Manchester City? A. 3:2 für Leipzig · B. 2:3 für Manchester City · C. 1:1", size=22, gap=8)
e.ex("B1", "선택 문제", "C", "프라이부르크, 트라브존 원정 1-0 승리",
     "Wer gewann in der Conference League in Trabzon? A. Leverkusen · B. Hoffenheim · C. Freiburg", size=22, gap=8)
e.ex("B1", "선택 문제", "A", "9라운드 30골",
     "Wie viele Tore fielen am 9. Spieltag? A. 30 · B. 25 · C. 20", size=22, gap=8)
e.ex("B1", "선택 문제", "B", "네덜란드 8, 독일 5",
     "Wie viele Punkte haben die Niederlande und Deutschland? A. 5 und 8 · B. 8 und 5 · C. 8 und 8", size=22, gap=8)
e.head("B　DIE WÖRTER", 25)
e.match_set("B1", "짝 맞추기",
            ["das Tor", "der Spieltag", "torreich", "weiterkommen"],
            ["in die nächste Runde kommen",
             "der Tag, an dem die Spiele stattfinden",
             "mit vielen Toren",
             "der Treffer im Fußball"],
            ["d", "b", "c", "a"],
            ["Tor=골 d", "Spieltag=라운드 b", "torreich=골이 많은 c", "weiterkommen=진출하다 a"],
            instr="짝을 맞추세요")
e.head("C　KOMPARATIV", 25)
e.bridge("비교급으로 완성하세요(괄호 안은 원급).")
e.ex("B1", "빈칸 채우기", "mehr", "viel → mehr (5-2가 2-1보다 골이 많음)",
     "Leipzig schoss ___ (viel) Tore als Dortmund.", instr="채우세요", size=22, gap=8)
e.ex("B1", "빈칸 채우기", "später", "spät → später (20:30이 15:30보다 늦음)",
     "Bayern gegen Köln beginnt ___ (spät) als die Samstagsspiele.", instr="채우세요", size=22, gap=8)
e.ex("B1", "빈칸 채우기", "früher", "früh → früher (11월 3일이 11월 8일보다 빠름)",
     "Die Champions League spielte ___ (früh) als die Bundesliga am Sonntag.", instr="채우세요", size=22, gap=8)
e.ex("B1", "빈칸 채우기", "mehr", "viel → mehr (네덜란드 8, 독일 5)",
     "Die Niederlande haben ___ (viel) Punkte als Deutschland.", instr="채우세요", size=22, gap=8)
e.head("D　DIE UHRZEITEN", 25)
e.bridge("위의 일정표를 보고 정답을 고르세요.")
e.ex("B1", "선택 문제", "A", "독일 대 네덜란드, 월요일 20:45",
     "Deutschland–Niederlande ist am Montag um... A. 20.45 Uhr · B. 18.45 Uhr · C. 15.30 Uhr", size=22, gap=8)
e.ex("B1", "선택 문제", "B", "바이에른 대 쾰른, 금요일 20:30",
     "Bayern–Köln beginnt am Freitag um... A. 15.30 Uhr · B. 20.30 Uhr · C. 18.30 Uhr", size=22, gap=8)
e.ex("B1", "선택 문제", "C", "샬케 대 슈투트가르트, 토요일 18:30",
     "Schalke–Stuttgart ist am Samstag um... A. 15.30 Uhr · B. 20.45 Uhr · C. 18.30 Uhr", size=22, gap=8)
e.ex("B1", "선택 문제", "A", "브레멘 대 함부르크, 일요일 17:30",
     "Bremen–Hamburg ist am Sonntag um... A. 17.30 Uhr · B. 15.30 Uhr · C. 20.30 Uhr", size=22, gap=8)
e.ex("B1", "선택 문제", "B", "함부르크, 글라트바흐에 금요일 3-1 승리",
     "Wie endete Hamburg gegen Gladbach? A. 1:3 · B. 3:1 · C. 2:2", size=22, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
