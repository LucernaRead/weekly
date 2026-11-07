# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · 시험과 정답", "De Lucerna", "8면 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "B", "기후 주간은 11월 8일까지예요",
     "De Klimaatweek duurt van 2 tot en met ___ november. (A. 7 · B. 8)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "B", "쿠포르던에서 나무와 관목 200그루를 나눠 줘요",
     "Coevorden deelt ___ bomen en struiken uit. (A. 100 · B. 200)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "B", "박물관의 밤은 11월 7일이에요",
     "Museumnacht is op zaterdag ___ november. (A. 6 · B. 7)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "B", "트벤테-아약스 경기는 13:30에 시작해요",
     "Twente – Ajax begint om ___ uur. (A. 11:15 · B. 13:30)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "A", "아약스가 아탈란타를 2-0으로 이겼어요",
     "Ajax won van Atalanta met ___. (A. 2–0 · B. 4–1)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "A", "로빈슨은 11월에 시작했어요",
     "Expeditie Robinson begon op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "B", "주황색 경보: 날씨가 위험해요",
     "Code oranje betekent: het weer is ___. (A. veilig · B. gevaarlijk)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "B", "meedoen = 참여하다",
     "«Meedoen» betekent ___. (A. weggaan · B. deelnemen)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "객관식", "A", "기후 주간은 11월 2일 월요일에 시작해요",
     "De Klimaatweek begint op... A. maandag 2 november · B. dinsdag 3 november · C. zaterdag 7 november", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "나눠 주는 곳은 즈벨로예요",
     "De bomen in Coevorden worden uitgedeeld in... A. Amsterdam · B. Zweeloo · C. Rotterdam", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "크로싱 보더는 헤이그에 있어요",
     "Crossing Border is in... A. Amsterdam · B. Den Haag · C. Utrecht", size=13.8, gap=0)
f.ex("B1", "객관식", "A", "PAN은 RAI 전시장에 있어요",
     "PAN Amsterdam is in... A. de RAI · B. het Rijksmuseum · C. de Jaarbeurs", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "레알 베티스가 페예노르트를 1-0으로 이겼어요",
     "Real Betis – Feyenoord eindigde... A. 0–0 · B. 1–0 · C. 0–1", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "10라운드 뒤 아약스는 21점이에요",
     "Na 10 ronden heeft Ajax ___ punten. A. 24 · B. 21 · C. 20", size=13.8, gap=0)
f.ex("B2", "객관식", "B", "경보 피로: 경보가 너무 많아서 주의를 덜 기울이게 돼요",
     "Waarschuwingsmoeheid betekent... A. moe van het weer · B. minder opletten door te veel waarschuwingen · C. een nieuwe code", size=13.8, gap=0)
f.ex("B1", "객관식", "C", "잔담 벼룩시장에는 약 250개의 노점이 있어요",
     "De Snuffelmarkt in Zaandam heeft zo'n ___ kramen. A. 70 · B. 200 · C. 250", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Coevorden. Op zaterdag 7 november gaat hij naar de Fair Groen in Zweeloo en haalt hij een gratis struik op. 's Avonds kijkt hij naar de foto's van Museumnacht in Amsterdam — zelf gaat hij niet, want zondag speelt zijn club Twente tegen Ajax om 13:30 uur. En in de Klimaatweek fietst Daan elke dag naar school, ook als het regent.", 15, lh=1.3, split=False)
f.ex("A2", "객관식", "B", "단은 쿠포르던에 살아요",
     "Waar woont Daan? A. in Zweeloo · B. in Coevorden · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "그는 토요일에 무료 관목 하나를 받아 갔어요",
     "Wat haalt Daan op zaterdag op? A. een fiets · B. een gratis struik · C. een kaartje", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "일요일에 트벤테 대 아약스 경기가 있어요",
     "Waarom gaat Daan zaterdagavond niet naar Amsterdam? A. Hij heeft geen kaartje · B. Zondag speelt Twente tegen Ajax · C. Hij houdt niet van musea", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "기후 주간에 그는 매일 자전거로 학교에 가요",
     "Wat doet Daan in de Klimaatweek? A. Hij rijdt elke dag met de auto · B. Hij fietst elke dag naar school · C. Hij blijft thuis", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "문장 만들기", "De Klimaatweek begint op maandag.", "주어 + 동사 + 시간",
     "de klimaatweek / begint / op maandag → ___", instr="문장 만들기", size=13.8, gap=0)
f.ex("B1", "문장 만들기", "Wij planten een boom in de tuin.", "주어 + 동사 + 목적어 + 장소",
     "wij / planten / een boom / in de tuin → ___", instr="문장 만들기", size=13.8, gap=0)
f.ex("B1", "문장 만들기", "Twente speelt zondag tegen Ajax.", "주어 + 동사 + 시간 + 상대 팀",
     "twente / speelt / zondag / tegen ajax → ___", instr="문장 만들기", size=13.8, gap=0)
f.ex("B1", "문장 만들기", "Ik doe mee aan de Klimaatweek.", "분리 동사 mee는 문장 끝에 와요",
     "ik / doe / mee / aan de klimaatweek → ___", instr="문장 만들기", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "번역", "기후 주간은 7일 동안 이어져요.", "1면 헤드라인 참조",
     "De Klimaatweek duurt zeven dagen. → ___", instr="한국어로 번역", size=13.8, gap=0)
f.ex("B1", "번역", "주황색 경보는 대비하라는 뜻이에요.", "2면 원문 · bereid je voor는 대비하라는 뜻이에요",
     "Code oranje betekent: bereid je voor. → ___", instr="한국어로 번역", size=13.8, gap=0)
f.ex("B1", "번역", "Museumnacht duurt van 19:00 uur tot 02:00 uur.", "시간 표현 van...tot...에 주의하세요",
     "박물관의 밤은 저녁 7시부터 새벽 2시까지예요. → ___", instr="네덜란드어로 번역", size=13.8, gap=0)
f.ex("B2", "번역", "Ik doe mee aan de Klimaatweek.", "meedoen은 분리 동사예요",
     "저는 기후 주간에 참여해요. → ___", instr="네덜란드어로 번역", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "단어 짝짓기",
            ["het klimaat", "meedoen", "de waarschuwing", "vastzetten"],
            ["een bericht over gevaarlijk weer",
             "deelnemen, erbij zijn",
             "het weer en de natuur over een lange tijd",
             "losse spullen stevig maken"],
            ["c", "b", "a", "d"],
            ["klimaat=기후 c", "meedoen=참여하다 b", "waarschuwing=경보 a", "vastzetten=고정하기 d"],
            instr="단어와 뜻 짝짓기")
f.head("G · DIALOOG BIJ DE BOMEN", 21, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "A", "boom = 나무",
     "— Goedemiddag! Ik kom voor een ___. (A. boom · B. fiets)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "A", "struik = 관목",
     "— Natuurlijk. Wilt u een boom of een ___? (A. struik · B. auto)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "A", "planten = 심다",
     "— Een struik, graag. En waar moet ik hem ___? (A. planten · B. kopen)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "B", "zachte = 부드러운(토양)",
     "— In de tuin, in de ___ grond. (A. harde · B. zachte)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "A", "나눠 주기는 16:00에 끝나요",
     "— De uitdeling duurt tot ___ uur. (A. 16:00 · B. 20:00)", size=13.8, gap=0)
f.head("H · SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Maandag 2 november begint de Klimaatweek in Nederland. "
          "Ik doe mee: ik fiets elke dag naar school en ik zet de verwarming één graad lager. "
          "Op zaterdag 7 november ga ik met mijn vader naar Coevorden, want daar deelt de gemeente gratis bomen uit. "
          "Wij nemen een struik mee voor onze tuin. "
          "'s Avonds kijken wij op televisie naar de foto's van Museumnacht in Amsterdam. "
          "Zondag kijken wij naar Twente tegen Ajax. "
          "Mijn zus plant ook een boom op haar balkon. "
          "Wat een week voor het klimaat!")
NWORDS = len(MODELO.split())
f.bridge(f"쓰기 문제예요(정답이 하나가 아니에요). 모범 답안({NWORDS}단어)은 아래에 있어요.")
f.ex("B1", "쓰기", "(열린 문제, 모범 답안은 아래에)", f"모범 답안은 이 면 H 구역에 있어요({NWORDS}단어)",
     "«Jouw week in de Klimaatweek» Schrijf 80–100 woorden: wat doe jij in de Klimaatweek, plant jij iets, fiets jij, en kijk jij naar Museumnacht of voetbal?", instr="쓰기", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ANTWOORDEN · 정답 — 면별로 정리했어요, 번호로 찾으세요", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "문제마다 짧은 해설이 있어요 · ✓ 표시는 모범 답안 문제예요", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 제 {pg} 면 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "쓰기":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-toets.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
