# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN　시험과 정답", "De Lucerna", "8면　De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "객관식", "B", "신터클라스 뉴스는 11월 9일에 시작해요",
     "Het Sinterklaasjournaal begint op 9 ___. (A. oktober · B. november)", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "전국 도착은 흐라버에서 열려요",
     "De landelijke intocht is in ___. (A. Amsterdam · B. Grave)", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "암스테르담 도착은 88회째예요",
     "De intocht in Amsterdam is de ___ editie. (A. 26e · B. 88e)", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "네덜란드–그리스 경기는 20:45에 시작해요",
     "Oranje – Griekenland begint om ___ uur. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.ex("B1", "객관식", "A", "성 마르틴의 날은 11월 11일이에요",
     "Sint-Maarten is op 11 ___. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "로빈슨은 RTL 4에서 방송해요",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "성 마르틴의 날은 나눔의 축제예요",
     "Sint-Maarten is het feest van het ___. (A. griezelen · B. delen)", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "schoen zetten = 신발 내놓기",
     "«De schoen zetten» betekent ___. (A. schoenen kopen · B. je schoen neerzetten)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "객관식", "A", "신터클라스 뉴스는 매일 18:00에 방송해요",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "흐라버는 마스 강가에 있어요",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "신터클라스는 해양 박물관에서 도시의 열쇠를 받아요",
     "In Amsterdam krijgt Sinterklaas de sleutel bij... A. de Stopera · B. het Scheepvaartmuseum · C. het Leidseplein", size=13.8, gap=0)
f.ex("B1", "객관식", "A", "『Het diner』는 2009년에 출판됐어요",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "네덜란드와 그리스는 둘 다 승점 8점이에요",
     "Na vier wedstrijden hebben Nederland en Griekenland ___ punten. A. 5 · B. 8 · C. 0", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "독일–네덜란드, 월요일, 베를린",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=13.8, gap=0)
f.ex("B2", "객관식", "B", "전통은 사람들이 계속 기념할 때 살아남아요",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "객관식", "C", "팍예스아폰트는 12월 5일 토요일이에요",
     "Pakjesavond is op... A. 11 november · B. 14 november · C. 5 december", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht. Op woensdag 11 november loopt zij met een lampion mee in de Sint Maarten Parade en zingt zij bij elke deur. Elke dag kijkt zij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag kijkt zij op televisie naar de intocht in Grave. Zondag zet zij haar schoen met een wortel en een verlanglijstje. Vrijdag kijkt zij naar Oranje tegen Griekenland.", 15, lh=1.3, split=False)
f.ex("A2", "객관식", "B", "산너는 위트레흐트에 살아요",
     "Waar woont Sanne? A. in Grave · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "수요일에 그녀는 성 마르틴 행렬에 참여해요",
     "Wat doet Sanne op woensdag 11 november? A. Ze kijkt naar Oranje · B. Ze loopt mee in de Sint Maarten Parade · C. Ze leest Het diner", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "그녀는 신발에 당근과 소원 목록을 넣어요",
     "Wat zit er in de schoen van Sanne? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "그녀는 매일 18:00에 신터클라스 뉴스를 봐요",
     "Wanneer kijkt Sanne naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "문장 만들기", "Het Sinterklaasjournaal begint op maandag.", "주어·동사·시간",
     "het sinterklaasjournaal / begint / op maandag → ___", instr="문장 만들기", size=13.8, gap=0)
f.ex("B1", "문장 만들기", "Wij zetten onze schoen bij de deur.", "주어·동사·목적어·장소",
     "wij / zetten / onze schoen / bij de deur → ___", instr="문장 만들기", size=13.8, gap=0)
f.ex("B1", "문장 만들기", "Oranje speelt vrijdag tegen Griekenland.", "주어 + 동사 + 시간 + 상대",
     "oranje / speelt / vrijdag / tegen griekenland → ___", instr="문장 만들기", size=13.8, gap=0)
f.ex("B1", "문장 만들기", "Ik loop met een lampion langs de deuren.", "주어 + 동사 + 양태 + 장소",
     "ik / loop / met een lampion / langs de deuren → ___", instr="문장 만들기", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "번역", "신터클라스 뉴스는 매일 18:00에 방송해요.", "3면 기사와 비교해 보세요",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="한국어로 번역", size=13.8, gap=0)
f.ex("B1", "번역", "성 마르틴의 날은 나눔의 축제예요.", "2면 원문 · delen = 나누다",
     "Sint-Maarten is het feest van het delen. → ___", instr="한국어로 번역", size=13.8, gap=0)
f.ex("B1", "번역", "De intocht in Amsterdam is de 88e editie.", "서수 88e에 주의하세요",
     "암스테르담 도착은 88회째예요. → ___", instr="네덜란드어로 번역", size=13.8, gap=0)
f.ex("B2", "번역", "Ik zet mijn schoen met een verlanglijstje.", "schoen zetten은 고정 표현이에요",
     "소원 목록을 넣은 신발을 내놓아요. → ___", instr="네덜란드어로 번역", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "단어 짝짓기",
            ["het journaal", "de intocht", "de lampion", "delen"],
            ["een papieren lichtje voor 11 november",
             "een dagelijks nieuwsprogramma op televisie",
             "licht en eten geven aan anderen",
             "de feestelijke aankomst van Sinterklaas"],
            ["b", "d", "a", "c"],
            ["journaal = 뉴스 프로그램 b", "intocht = 축제 도착 d", "lampion = 등롱 a", "delen = 나누다 c"],
            instr="단어와 뜻 짝짓기")
f.head("G　DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
f.ex("B1", "객관식", "A", "schoen = 신발",
     "— Mama, waar moet mijn ___? (A. schoen · B. boek)", size=13.8, gap=0)
f.ex("B1", "객관식", "A", "wortel = 당근 (말을 위한 거예요)",
     "— Bij de deur, met een ___ voor het paard. (A. wortel · B. lampion)", size=13.8, gap=0)
f.ex("B1", "객관식", "A", "verlanglijstje = 소원 목록",
     "— En mijn ___ erin? (A. verlanglijstje · B. journaal)", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "cadeautje = 작은 선물",
     "— Ja. Sinterklaas brengt 's nachts een ___. (A. mantel · B. cadeautje)", size=13.8, gap=0)
f.ex("B1", "객관식", "A", "18:00 = 신터클라스 뉴스 시간",
     "— Eerst kijken we om ___ uur naar het Sinterklaasjournaal. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.head("H　SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Maandag 9 november begint het Sinterklaasjournaal. "
          "Ik kijk elke dag om 18:00 uur naar NPO Zapp. "
          "Op woensdag 11 november loop ik met een lampion langs de deuren en zing ik een liedje. "
          "Vrijdag kijk ik naar Oranje tegen Griekenland. "
          "Zaterdag kijk ik naar de intocht in Grave op televisie. "
          "Zondag vaart Sinterklaas in Amsterdam. "
          "Daarna zet ik mijn schoen met een wortel en een verlanglijstje. "
          "Ik hoop op een boek. "
          "Maandag 16 november speelt Oranje in Berlijn tegen Duitsland. "
          "Ik kijk ook dan. "
          "Wat een week vol licht!")
NWORDS = len(MODELO.split())
f.bridge(f"쓰기 문제예요(정답이 하나만 있는 것은 아니에요). 모범 답안은 아래에 있어요({NWORDS}단어).")
f.ex("B1", "쓰기", "(열린 문제, 모범 답안은 아래에 있어요)", f"모범 답안은 H 부분에서 보세요({NWORDS}단어)",
     "«Mijn week met Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, loop jij met een lampion, kijk jij naar het Sinterklaasjournaal, en zet jij je schoen?", instr="쓰기", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　정답 모음 — 면별로 찾으세요", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "모든 정답에는 짧은 한국어 설명이 있어요　✓는 쓰기 문제예요", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
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
