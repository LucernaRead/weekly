# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-de-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUGEND · 청소년", "Die Lucerna", "LEVEL B1 · Laternen, Lieder & Schule · 등불, 노래, 학교")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P5-main")
f.title("Laternen basteln, Lieder singen: Die Woche der Kinder", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B1")
f.para("Am Montag, dem 9. November, sind alle wieder in der Schule: Auch in Bayern sind die Herbstferien jetzt vorbei. Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut. Und in vielen Klassen wird schon gebastelt: Laternen für St. Martin.")
f.para("Was basteln die Kinder? Bunte Laternen aus Papier, mit Sternen, Monden und Tieren. In der Kita und in der Schule singen sie Martinslieder und üben den Umzug. Am Mittwochabend ziehen sie dann mit ihren Laternen durch die Straßen — vorneweg der heilige Martin auf dem Pferd.")
f.para("Und in Köln? Dort beginnt am Mittwoch um 11.11 Uhr die Karnevalssession. Auch Kinder verkleiden sich: als Prinzessin, als Pirat, als Tier. Aber Vorsicht: Am Vormittag ist Karneval, am Abend ist St. Martin — zwei Feste, zwei Stimmungen, ein Tag.")
f.para("Was macht man nach der Schule im dunklen November? Lesen, was man im Herbst begonnen hat, oder ein neues Hobby probieren. Unser Tipp: Suchen Sie sich ein Buch für die dunklen Abende — die Bibliotheken haben im November oft neue Bücher und Lesungen. Und wer Sport mag: Am Sonntag läuft die NFL im Fernsehen.")
f.para("Auch der Fußball gehört zur Woche: Am Freitag spielt die Nationalmannschaft in Belgrad — viele Jugendliche schauen das Spiel im Fernsehen. Wer in München wohnt, sieht am Sonntag vielleicht sogar die NFL-Stars in der Stadt. Mehr dazu auf Seite 4.")
f.gloss("basteln＝만들다 · der Pausenhof＝운동장 · sich verkleiden＝분장하다 · die Stimmung＝분위기 · der Pirat＝해적。")
f.end_report()

# col 3: facts + vocab + Und Sie (hand-rolled; CORRECTED height formula — see W45 KIT §geometry)
ix = COLX[3]
facts = ["Am 9. November sind alle Bundesländer wieder in der Schule.",
         "In vielen Klassen werden Laternen für St. Martin gebastelt.",
         "Am 11. November: Karneval am Vormittag, Laternen am Abend."]
sy3 = 200
sh = 45 + 33 * len(facts) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in facts)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SCHULWOCHE · 학교", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 facts ends", sy3 + sh)
words = ["die Laterne — 등불", "basteln — 만들다", "das Lied — 노래",
         "das Kostüm — 의상", "der Umzug — 행렬", "der Stern — 별"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "MARTINSWÖRTER · 성 마르틴", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Haben Sie als Kind eine Laterne gebastelt? Welches Lied singen Sie im November? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("어릴 때 등불을 만들었나요? 독일어로 두 문장!", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE? · 당신은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "어릴 때 등불을 만들었나요? 독일어로 두 문장!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- Wochenplan wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "DER WOCHENPLAN DER REDAKTION · 편집부의 한 주", 24, "sans", True, OLIVE)
planrows = [
    ("Mo 9.11.", "Schule für alle: Auch Bayern ist wieder da."),
    ("Di 10.11.", "Laternen basteln: Die Kitas bereiten den Umzug vor."),
    ("Mi 11.11.", "Karneval um 11.11 Uhr, Laternen am Abend."),
    ("Do 12.11.", "Nach dem Fest: In der Schule wird erzählt und geschrieben."),
    ("Fr 13.11.", "Nations League: Serbien – Deutschland (20.45 Uhr, RTL)."),
]
pyy = 1184
for t, txt in planrows:
    p.text(sx + 24, pyy + 24, t, 21, "sans", True, BRICK)
    p.text(sx + 190, pyy + 24, txt, 21.5, "serif", False, INK)
    pyy += 45

# ---- P5 exercises ----
ey = 1500
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · 5쪽 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "답은 8쪽 · 수준이 섞여 있습니다. 번호로 답을 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · LESEVERSTEHEN", 25)
e.bridge("5쪽 기사를 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "A", "학교는 11월 9일에 모든 곳에서 다시 시작",
     "Wann sind alle wieder in der Schule? A. am 9. November · B. am 11. November · C. am 15. November", size=20, gap=8)
e.ex("B1", "객관식", "B", "아이들은 종이 등불을 만든다",
     "Was basteln die Kinder? A. ein Kostüm · B. Laternen aus Papier · C. einen Kürbis", size=20, gap=8)
e.ex("B1", "객관식", "B", "오전에는 카니발, 오후에는 성 마르틴",
     "Was ist am 11. November richtig? A. Nur Karneval. · B. Karneval am Vormittag, St. Martin am Abend. · C. Nur St. Martin.", size=20, gap=8)
e.ex("B1", "객관식", "B", "일요일 TV로 NFL",
     "Was läuft am Sonntag im Fernsehen? A. die Bundesliga · B. die NFL · C. ein Film", size=20, gap=8)
e.ex("A2", "객관식", "A", "금요일에 대표팀 보기",
     "Was schauen viele Jugendliche am Freitag? A. die Nationalmannschaft in Belgrad · B. die NFL · C. den Karneval", size=20, gap=8)
e.head("B · WÖRTER AUS DEM TEXT", 25)
e.bridge("상자의 단어로 완성하세요.")
e.para("Laterne · basteln · Lied · Kostüm · Umzug · Stern", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "Laterne", "종이 등불",
     "Die Kinder tragen eine bunte ___ durch die Straßen.", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "basteln", "등불 만들기",
     "In der Schule ___ die Kinder Laternen.", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "Lied", "성 마르틴 노래 부르기",
     "Die Kinder singen ein Martins___.", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "Kostüm", "카니발 의상",
     "In Köln tragen die Kinder ein buntes ___.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Umzug", "등불 행렬",
     "Am Abend zieht der ___ durch die Straßen.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Stern", "등불 위의 별",
     "Auf der Laterne ist ein ___.", instr="빈칸", size=20, gap=8)
e.head("C · SÄTZE MIT «WEIL»", 25)
e.bridge("두 문장을 weil로 연결하세요（동사는 맨 끝으로）。")
e.ex("B1", "문장 전환", "Die Kinder freuen sich, weil St. Martin kommt.", "weil 절에서는 동사가 맨 끝으로",
     "Die Kinder freuen sich. St. Martin kommt. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Er bleibt zu Hause, weil es dunkel ist.", "ist는 맨 끝으로",
     "Er bleibt zu Hause. Es ist dunkel. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Sie geht in die Bibliothek, weil sie ein Buch lesen will.", "will은 맨 끝으로",
     "Sie geht in die Bibliothek. Sie will ein Buch lesen. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Köln feiert, weil die Karnevalssession beginnt.", "beginnt는 맨 끝으로",
     "Köln feiert. Die Karnevalssession beginnt. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
e.head("D · RICHTIG ODER FALSCH?", 25)
e.bridge("맞나요, 틀렸나요?")
e.ex("A2", "참-거짓 판단", "Richtig", "바이에른도 11월 9일에 복귀",
     "Auch in Bayern sind die Herbstferien am 9. November vorbei. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("B1", "참-거짓 판단", "Falsch", "등불 행렬은 저녁에",
     "Der Laternenumzug findet am Vormittag statt. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("A2", "참-거짓 판단", "Richtig", "아이들은 성 마르틴 노래를 부른다",
     "Die Kinder singen Martinslieder. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jugend.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERTIEFUNG · 심화 읽기", "Die Lucerna", "LEVEL B2 · Volkstrauertag & Stromsteuer · 추모의 날과 전기세")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P6-main")
f.title("Stille am Sonntag: Was bedeutet der Volkstrauertag?", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B2")
f.para("Am Sonntag, dem 15. November, ist Volkstrauertag: ein staatlicher Gedenktag. Die Menschen gedenken der Opfer von Gewalt und Krieg aller Nationen. In vielen Städten gibt es Gedenkstunden und Kranzniederlegungen. Der Tag liegt zwei Sonntage vor dem ersten Advent — und er ist ein stiller Tag.")
f.para("Die zentrale Gedenkstunde findet im Bundestag statt. Das ZDF überträgt ab 13.30 Uhr live. In diesem Jahr steht sie im Zeichen der deutsch-österreichischen Verbundenheit: Die Gedenkrede hält der österreichische Bundespräsident Alexander Van der Bellen. Bundespräsident Frank-Walter Steinmeier spricht das Totengedenken.")
f.para("Warum gibt es diesen Tag? Die erste Gedenkstunde fand 1922 im Reichstag statt. Seit 1952 wird der Volkstrauertag zwei Sonntage vor dem ersten Advent begangen. Gedenken heißt hier: innehalten, erinnern — und für Frieden und Versöhnung einstehen.")
f.para("Zweites Thema: die Stromsteuer. Kanzler Friedrich Merz will sie für alle auf das europäische Mindestmaß senken — versprochen war das schon im Koalitionsvertrag. Bisher gilt die Senkung nur für bestimmte Branchen. Haushalte zahlen weiter 2,05 Cent pro Kilowattstunde. Finanzminister Lars Klingbeil zeigt sich offen, zweifelt aber an der Finanzierung.")
f.para("Die Grünen hatten im April einen Entwurf zur Senkung für alle vorgelegt — der Bundestag lehnte ihn mit 310 zu 270 Stimmen ab. Der Haushalt 2027 soll am 27. November verabschiedet werden. Ob eine Einigung gelingt, ist offen.")
f.para("Zwei Themen, ein Muster: Gedenken und Energiepolitik betreffen fast jeden Haushalt. Am Sonntag ist es still im Land. Am Montag geht die Debatte weiter.")
f.gloss("gedenken＝추모하다 · Kranzniederlegung＝헌화 · stille Tag＝조용한 날 · Verbundenheit＝유대 · Versöhnung＝화해。")
f.end_report()

# col 3: numbers box + debate box (measured)
ix = COLX[3]
tl = [("15.11.", "Volkstrauertag — zwei Sonntage vor dem ersten Advent."),
      ("1922", "erste Gedenkstunde im Reichstag in Berlin."),
      ("13.30", "Uhr: Das ZDF überträgt die Gedenkstunde live."),
      ("2,05", "Cent pro Kilowattstunde: Stromsteuer für Haushalte."),
      ("0,05", "Cent: Stromsteuer für die Industrie seit 2026."),
      ("27.11.", "Verabschiedung des Bundeshaushalts 2027 geplant.")]
tlh = 45 + 30.5 * len(tl) + 29.11 * sum(len(wrap(t, "serif", False, 20.5, CW - 152)) for yr, t in tl)
p.rect(ix, 200, CW, tlh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DIE ZAHLEN · 숫자", 24, "sans", True, OLIVE)
yy3 += 52
for yr, t in tl:
    p.text(ix + 22, yy3 + 21, yr, 21, "sans", True, BRICK)
    yy3 = p.para(ix + 130, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 152, 1.42) + 10
print("P6 col3 numbers ends", 200 + tlh)
deb = "Volkstrauertag: Gedenken braucht Stille — darüber sind sich fast alle einig. Stromsteuer: Wie stark sie sinkt, ist noch offen. Beides betrifft fast jeden Haushalt."
hy3 = 200 + tlh + 26
hh = 140 + 29.82 * len(wrap(deb, "serif", False, 21, CW - 44)) + 27.69 * (len(wrap("추모의 날: 추모에는 고요함이 필요하다——거의 모두가 동의한다. 전기세: 얼마나 내릴지는 아직 미정이다. 둘 다 거의 모든 가정에 영향을 미친다.", "sans", False, 19.5, CW - 44)) - 1)
p.rect(ix, hy3, CW, hh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = hy3 + 16
p.text(ix + 22, yy3 + 26, "DIE DEBATTE IN EINEM SATZ", 22.5, "sans", True, OLIVE)
yy3 += 50
yy3 = p.para(ix + 22, yy3 + 21, deb, 21, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "추모의 날: 추모에는 고요함이 필요하다——거의 모두가 동의한다. 전기세: 얼마나 내릴지는 아직 미정이다. 둘 다 거의 모든 가정에 영향을 미친다.", 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", hy3 + hh)

# ---- Two Sundays wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 252, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "ZWEI SONNTAGE IM NOVEMBER · 11월의 두 일요일", 24, "sans", True, OLIVE)
p.text(sx + 24, 1210, "VOLKSTRAUERTAG — 15. NOVEMBER", 21, "sans", True, BRICK)
p.text(sx + 24 + (swd - 48) // 2, 1210, "TOTENSONNTAG — 22. NOVEMBER", 21, "sans", True, BRICK)
pro = ["Gedenken an die Opfer von Gewalt und Krieg aller Nationen.",
       "Zentrale Gedenkstunde im Bundestag, Kranzniederlegungen im ganzen Land."]
contra = ["Evangelischer Gedenktag für die Verstorbenen.",
          "Eine Woche nach dem Volkstrauertag; dazwischen der Buß- und Bettag (18. November, Feiertag in Sachsen)."]
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
p.text(MX, cy + 28, "WAS INTERESSIERT DIE LESER? · 독자의 관심은?", 26, "sans", True, OLIVE)
bars = [("Nations League und NFL", 46, "축구"),
        ("St. Martin und Karneval", 34, "축제"),
        ("Volkstrauertag und Gedenken", 20, "추모")]
byy = cy + 58
for lab, v, zh in bars:
    p.text(MX, byy + 26, lab, 22, "serif", True, INK)
    p.text(MX + 360, byy + 26, zh, 20, "sans", False, GREY)
    p.rect(MX + 470, byy + 4, v * 17, 30, fill=OLIVE)
    p.text(MX + 470 + v * 17 + 16, byy + 26, f"{v} %", 22, "sans", True, BRICK)
    byy += 52
p.text(MX, byy + 22, "ÜBUNGSDATEN · 연습용 자료 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（연습용 자료이며 실제 설문 조사가 아닙니다.）", 19.5, "sans", False, GREY)

# ---- P6 exercises ----
ey = 1808
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · 6쪽 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "답은 8쪽 · 수준이 섞여 있습니다. 번호로 답을 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · DAS DIAGRAMM LESEN", 25, gap=9)
e.bridge("위 연습용 도표를 사용하세요.")
e.ex("B1", "객관식", "A", "축구가 46%로 선두",
     "Was interessiert die Leser am meisten (Übungsdaten)? A. Nations League und NFL · B. St. Martin · C. Volkstrauertag", size=20, gap=7)
e.ex("B1", "객관식", "B", "축제가 34%로 2위",
     "Was ist die zweitgrößte Gruppe? A. Volkstrauertag · B. St. Martin und Karneval · C. Nations League", size=20, gap=7)
e.ex("B1", "객관식", "B", "46+34=80",
     "Fußball und Feste zusammen sind... A. 66 % · B. 80 % · C. 100 %", size=20, gap=7)
e.ex("B2", "객관식", "B", "추모가 20%로 가장 적다",
     "Welche Gruppe ist kleiner? A. Feste · B. Gedenken · C. beide gleich", size=20, gap=7)
e.ex("B1", "객관식", "A", "추모 20%",
     "Wie viele Prozent interessieren sich für den Volkstrauertag? A. 20 % · B. 34 % · C. 46 %", size=20, gap=7)
e.ex("B2", "객관식", "B", "46+34+20=100",
     "Die drei Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 %", size=20, gap=7)
e.head("B · LESEVERSTEHEN (B2)", 25, gap=9)
e.bridge("6쪽 기사를 읽으세요.")
e.ex("B2", "객관식", "B", "추모의 날은 11월 15일",
     "Wann ist Volkstrauertag? A. am 11. November · B. am 15. November · C. am 22. November", size=20, gap=7)
e.ex("B2", "객관식", "A", "ZDF 13시 30분부터 생중계",
     "Wer überträgt die Gedenkstunde ab 13.30 Uhr? A. das ZDF · B. RTL · C. die ARD", size=20, gap=7)
e.ex("B2", "객관식", "B", "가정용 전기세는 2.05센트",
     "Wie hoch ist die Stromsteuer für Haushalte? A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent", size=20, gap=7)
e.ex("B1", "객관식", "B", "2027년 예산 표결은 11월 27일",
     "Wann soll der Bundeshaushalt 2027 verabschiedet werden? A. am 15. November · B. am 27. November · C. am 18. November", size=20, gap=7)
e.head("C · GRAMMATIK", 25, gap=9)
e.bridge("괄호 안의 형태로 채우세요.")
e.ex("B2", "문장 완성", "wird", "수동태: wird＋과거분사",
     "Die Gedenkstunde ___ (werden) live übertragen.", instr="빈칸", size=20, gap=7)
e.ex("B2", "문장 완성", "ob", "ob는 간접의문문을 이끈다",
     "Niemand weiß, ___ die Einigung gelingt.", instr="빈칸", size=20, gap=7)
e.ex("B1", "문장 완성", "geht", "gehen → geht",
     "Die Debatte ___ (gehen) weiter.", instr="빈칸", size=20, gap=7)
e.ex("B2", "문장 완성", "spricht", "sprechen → spricht",
     "Steinmeier ___ (sprechen) das Totengedenken.", instr="빈칸", size=20, gap=7)
e.head("D · WÖRTER DER DEBATTE", 25, gap=9)
e.bridge("상자의 단어로 완성하세요.")
e.para("Kranzniederlegung · Versöhnung · Verbundenheit · gedenken", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "Kranzniederlegung", "헌화식",
     "In vielen Städten gibt es eine ___.", instr="빈칸", size=20, gap=7)
e.ex("B2", "문장 완성", "Versöhnung", "평화와 화해를 위해",
     "Gedenken heißt: für Frieden und ___ einstehen.", instr="빈칸", size=20, gap=7)
e.ex("B2", "문장 완성", "Verbundenheit", "독일-오스트리아 유대",
     "Die Gedenkstunde steht im Zeichen der deutsch-österreichischen ___.", instr="빈칸", size=20, gap=7)
e.ex("B1", "문장 완성", "gedenken", "희생자 추모",
     "Die Menschen ___ der Opfer von Gewalt und Krieg.", instr="빈칸", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-vertiefung.svg")
print("P6 saved, exercises so far:", len(REG))
