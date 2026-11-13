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
f.ex("B1", "객관식", "B", "독일–네덜란드, 월요일, 베를린",
     "Duitsland – Nederland is op maandag in ___. (A. Amsterdam · B. Berlijn)", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "네덜란드와 그리스는 둘 다 승점 8점이에요",
     "Nederland en Griekenland hebben allebei ___ punten. (A. 5 · B. 8)", size=13.8, gap=0)
f.ex("B1", "객관식", "A", "네덜란드는 7골을 넣었어요",
     "Nederland maakte ___ doelpunten in vier wedstrijden. (A. 7 · B. 5)", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "Pakjesavond는 12월",
     "Pakjesavond is op ___ december. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "신터클라스 뉴스 18:00",
     "Het Sinterklaasjournaal is elke dag om ___ uur. (A. 12:00 · B. 18:00)", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "로빈슨은 RTL 4에서 방송해요",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "서프리즈 안에는 시가 있다",
     "Bij een surprise hoort een ___. (A. liedje · B. gedicht)", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "groepswinst = 조 우승",
     "«De groepswinst» betekent ___. (A. de laatste plaats · B. de eerste plaats in de groep)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "객관식", "A", "신터클라스 뉴스는 매일 18:00에 방송해요",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "흐라버는 마스 강가에 있어요",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "암스테르담 도착은 88회째예요",
     "De intocht in Amsterdam was de... A. 26e editie · B. 88e editie · C. 30e editie", size=13.8, gap=0)
f.ex("B1", "객관식", "A", "『Het diner』는 2009년에 출판됐어요",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "독일은 홈에서 그리스에 0–1로 졌어요",
     "Duitsland verloor thuis met 0–1 van... A. Servië · B. Griekenland · C. Nederland", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "PSV는 승점 26점으로 에레디비시 선두예요",
     "PSV staat bovenaan in de Eredivisie met ___ punten. A. 25 · B. 26 · C. 8", size=13.8, gap=0)
f.ex("B2", "객관식", "B", "전통은 사람들이 계속 기념할 때 살아남아요",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "객관식", "C", "에레디비시 13라운드는 11월 21–22일이에요",
     "Speelronde 13 is op... A. 13 en 14 november · B. 16 november · C. 21 en 22 november", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Rotterdam. Op maandag 16 november kijkt hij om 20:45 uur naar Duitsland – Nederland in Berlijn. Elke dag kijkt hij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag 21 november kijkt hij naar NEC – PSV. Zondag zet hij zijn schoen met een wortel en een verlanglijstje. Op zondagavond kijkt hij ook naar Expeditie Robinson.", 15, lh=1.3, split=False)
f.ex("A2", "객관식", "B", "단은 로테르담에 살아요",
     "Waar woont Daan? A. in Grave · B. in Rotterdam · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "그는 월요일에 독일–네덜란드 경기를 봐요",
     "Wat doet Daan op maandag 16 november? A. Hij kijkt naar Robinson · B. Hij kijkt naar Duitsland – Nederland · C. Hij leest Het diner", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "그는 신발에 당근과 소원 목록을 넣어요",
     "Wat zit er in de schoen van Daan? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "그는 매일 18시에 신터클라스 뉴스를 봐요",
     "Wanneer kijkt Daan naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "문장 만들기", "Het Sinterklaasjournaal begint om 18:00 uur.", "주어·동사·시간",
     "het sinterklaasjournaal / begint / om 18:00 uur → ___", instr="문장 만들기", size=13.8, gap=0)
f.ex("B1", "문장 만들기", "Wij zetten onze schoen bij de deur.", "주어·동사·목적어·장소",
     "wij / zetten / onze schoen / bij de deur → ___", instr="문장 만들기", size=13.8, gap=0)
f.ex("B1", "문장 만들기", "Oranje speelt maandag in Berlijn.", "주어·동사·시간·장소",
     "oranje / speelt / maandag / in berlijn → ___", instr="문장 만들기", size=13.8, gap=0)
f.ex("B1", "문장 만들기", "Ik zet mijn schoen met een wortel.", "주어·동사·목적어·방식",
     "ik / zet / mijn schoen / met een wortel → ___", instr="문장 만들기", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "번역", "신터클라스 뉴스는 매일 18:00에 방송해요.", "3면 기사와 비교해 보세요",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="한국어로 번역하기", size=13.8, gap=0)
f.ex("B1", "번역", "상위 두 팀이 8강전에 진출해요.", "4면 원문 · kwartfinale = 8강전",
     "De nummers één en twee gaan naar de kwartfinales. → ___", instr="한국어로 번역하기", size=13.8, gap=0)
f.ex("B1", "번역", "De intocht in Amsterdam was de 88e editie.", "서수 88e에 주의하세요",
     "암스테르담 도착은 88회째예요. → ___", instr="네덜란드어로 번역하기", size=13.8, gap=0)
f.ex("B2", "번역", "Ik maak een surprise met een kort gedicht.", "surprise는 고정 표현이에요",
     "작은 시가 담긴 깜짝 선물을 만들어요. → ___", instr="네덜란드어로 번역하기", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "단어 짝짓기",
            ["het journaal", "de groepswinst", "de schoen", "het gedicht"],
            ["een klein versje bij een cadeau",
             "een dagelijks nieuwsprogramma op televisie",
             "de eerste plaats in de groep",
             "die staat 's avonds bij de deur"],
            ["b", "c", "d", "a"],
            ["journaal = 뉴스 프로그램 b", "groepswinst=조 우승 c", "schoen = 신발 d", "gedicht=시 a"],
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
MODELO = ("Maandag 16 november speelt Oranje in Berlijn tegen Duitsland. "
          "Ik kijk om 20:45 uur naar NPO 3. "
          "Elke dag kijk ik om 18:00 uur naar het Sinterklaasjournaal. "
          "Op woensdag schrijf ik een gedicht voor mijn surprise. "
          "Zaterdag kijk ik naar NEC – PSV. "
          "Zondag zet ik mijn schoen met een wortel en een verlanglijstje. "
          "Zondagavond kijk ik naar Expeditie Robinson. "
          "Daarna is het bijna pakjesavond, op zaterdag 5 december. "
          "Ik hoop op een boek. "
          "Wat een week vol voetbal en licht!")
NWORDS = len(MODELO.split())
f.bridge(f"쓰기 과제(정답이 하나가 아니에요); 모범 글({NWORDS}단어)은 아래에 있어요.")
f.ex("B1", "쓰기", "(열린 문제, 모범 답안은 아래에 있어요)", f"모범 답안은 H 부분에서 보세요({NWORDS}단어)",
     "«Mijn week met Oranje en Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, kijk jij naar Duitsland – Nederland, en zet jij je schoen?", instr="쓰기", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()
print("P8-ex flow ended col", f.ci, "y", round(f.y, 1), "(bottom 1252)")

# ---- P8 photo (W47: every page carries a public-domain image) ----
# Placed in the final exercise column, below the flow, only if it fits
# above the answers rule at y=1264 (image + caption must end by 1252).
if f.ci == 3 and f.y + 16 + 200 + 78 <= 1252:
    _px = COLX[f.ci]
    _py = f.y + 16
    image(p, "pen.jpg", _px, _py, CW, 200)
    _cy = caption(p, _px, _py + 200, CW, "Een vulpen op een schrift. Schrijf je opstel eerst met de hand — dan in het net.",
                  "Foto: Aaron Burden / Unsplash — CC0")
    print("P8 photo placed at", _px, _py, "ends", _cy)
else:
    print("!! P8 photo NOT placed: flow ended col", f.ci, "y", round(f.y, 1))

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　정답 — 면별로 정리했어요: 번호를 찾으세요", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "모든 정답에는 한국어 해설이 있어요　✓는 쓰기 과제예요", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
