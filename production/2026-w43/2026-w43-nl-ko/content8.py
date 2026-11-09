# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN　시험과 정답", "De Lucerna", "제 8 면　De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "B", "가을에 시계 뒤로 돌리기",
     "In de nacht van zaterdag op zondag gaat de klok één uur ___. (A. vooruit · B. achteruit)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "A", "중부와 남부의 가을 방학은 10월 25일까지",
     "De herfstvakantie van Midden en Zuid duurt tot en met zondag ___ oktober. (A. 25 · B. 18)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "A", "디자인 위크는 에인트호번에서 열려요",
     "De Dutch Design Week is in ___. (A. Eindhoven · B. Amsterdam)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "B", "PSV가 원정에서 포르투를 이겼어요",
     "PSV won in de Champions League bij ___. (A. Atalanta · B. FC Porto)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "B", "ADE는 올해 30년",
     "ADE wordt dit jaar ___ jaar. (A. 25 · B. 30)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "A", "Robinson은 11월에 시작해요",
     "Expeditie Robinson begint op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "A", "가장 큰 시계 검색어는 wintertijd",
     "De grootste zoekterm over de klok was «___». (A. wintertijd · B. klok vooruit)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "B", "half drie = 2:30",
     "«Half drie» is ___. (A. 03:30 · B. 02:30)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "객관식", "B", "겨울 시간은 새벽 03:00에 시작해요",
     "De wintertijd begint om... A. 02:00 uur · B. 03:00 uur · C. middernacht", size=13.8, gap=0)
f.ex("A2", "객관식", "A", "북부 지역은 10월 10–18일 방학",
     "Welke regio had vakantie van 10 tot en met 18 oktober? A. Noord · B. Midden · C. Zuid", size=13.8, gap=0)
f.ex("A2", "객관식", "C", "학생표 € 19,50",
     "Een studentenkaartje voor de DDW kost... A. € 32,50 · B. € 25,00 · C. € 19,50", size=13.8, gap=0)
f.ex("B1", "객관식", "A", "페예노르트는 수요일 세비야에서",
     "Feyenoord speelt woensdag in... A. Sevilla · B. Porto · C. Eindhoven", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "스파르타–아약스는 16:45 시작",
     "Sparta – Ajax begint zondag om... A. 14:30 uur · B. 16:45 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("B1", "객관식", "B", "참가자 19명은 네덜란드인과 플람스인",
     "De 19 kandidaten van Expeditie Robinson zijn... A. allemaal dj's · B. Nederlanders en Vlamingen · C. alleen sporters", size=13.8, gap=0)
f.ex("B2", "객관식", "B", "6,600명은 \"앞으로\"를 검색했어요(반대로 물은 것)",
     "De 6.600 zoekopdrachten vroegen naar... A. achteruit · B. vooruit · C. wintertijd", size=13.8, gap=0)
f.ex("B1", "객관식", "A", "플랫폼은 앞으로 모든 추가 비용을 명확히 보여 줘요",
     "Thuisbezorgd laat voortaan... A. alle extra kosten duidelijk zien · B. geen eten meer bezorgen · C. alleen kortingsbonnen zien", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht, in de regio Midden. Zij heeft de hele week herfstvakantie. Op woensdag gaat zij met haar zus naar Eindhoven, naar de Dutch Design Week. Zaterdagavond zet zij alle klokken in huis één uur achteruit — behalve haar telefoon, die doet het zelf. Zondag slaapt zij lang uit: het is de laatste dag van de vakantie.", 15, lh=1.3, split=False)
f.ex("A2", "객관식", "B", "Sanne는 위트레흐트에 살아요",
     "Waar woont Sanne? A. in Venlo · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "그녀의 지역은 가을 방학 중이에요",
     "Waarom heeft Sanne de hele week vrij? A. Zij is ziek · B. Het is herfstvakantie in haar regio · C. Zij werkt niet", size=13.8, gap=0)
f.ex("A2", "객관식", "B", "그녀는 토요일 저녁 시계를 돌려요",
     "Wat doet Sanne zaterdagavond? A. Zij gaat dansen · B. Zij zet de klokken achteruit · C. Zij pakt haar koffer", size=13.8, gap=0)
f.ex("B1", "객관식", "C", "휴대폰은 스스로 시간을 바꿔요, 손으로 돌릴 필요 없어요",
     "Welke klok zet Sanne NIET met de hand achteruit? A. de ovenklok · B. de wekker · C. haar telefoon", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "문장 만들기", "De klok gaat één uur achteruit.", "주어 + 동사 + 목적어 + 방향",
     "de klok / gaat / één uur / achteruit → ___", instr="문장 만들기", size=13.8, gap=0)
f.ex("B1", "문장 만들기", "Wij gaan zondag naar de topper.", "주어 + 동사 + 시간 + 장소",
     "wij / gaan / zondag / naar de topper → ___", instr="문장 만들기", size=13.8, gap=0)
f.ex("B1", "문장 만들기", "Hoe laat begint de wedstrijd?", "의문 표현이 문장 앞에",
     "hoe laat / begint / de wedstrijd / ? → ___", instr="문장 만들기", size=13.8, gap=0)
f.ex("B1", "문장 만들기", "PSV won met 1–0 in Porto.", "주어 + 동사 + 결과 + 장소",
     "psv / won / met 1–0 / in porto → ___", instr="문장 만들기", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "번역", "일요일에 시계가 뒤로 가요: 한 시간 더 자기!", "1면 헤드라인 참조",
     "Zondag gaat de klok terug: een uur langer slapen! → ___", instr="번역", size=13.8, gap=0)
f.ex("B1", "번역", "휴대폰과 컴퓨터는 스스로 시간을 바꿔요.", "2면 원문 · veranderen 바꾸다",
     "Je telefoon en je computer veranderen de tijd zelf. → ___", instr="번역", size=13.8, gap=0)
f.ex("B1", "번역", "De Dutch Design Week is in Eindhoven.", "장소 표현 in Eindhoven에 주의",
     "네덜란드 디자인 위크는 에인트호번에 있어요. → ___", instr="번역", size=13.8, gap=0)
f.ex("B2", "번역", "Zondag heb ik een uur langer geslapen.", "perfectum：heb geslapen",
     "일요일에 저는 한 시간 더 잤어요. → ___", instr="번역", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "단어 짝짓기",
            ["de klok verzetten", "het ezelsbruggetje", "eropuit gaan", "bijslapen"],
            ["extra slapen om uit te rusten",
             "het huis uit gaan voor iets leuks",
             "een hulpmiddel om iets te onthouden",
             "de tijd op een klok veranderen"],
            ["d", "c", "b", "a"],
            ["verzetten=시계 돌리기 d", "ezelsbruggetje=암기 문구 c", "eropuit=나들이 가기 b", "bijslapen=늦잠 보충 a"],
            instr="단어와 뜻 짝짓기")
f.head("G　DIALOOG BIJ DE DDW", 21, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "B", "kaartje = 표",
     "— Goedemorgen! Een ___ voor de Dutch Design Week, alstublieft. (A. ezelsbruggetje · B. kaartje)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "A", "student = 학생(표값 € 19,50)",
     "— Natuurlijk. Bent u ___? Studenten betalen € 19,50. (A. student · B. ontwerper)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "B", "tot hoe laat = 몇 시까지 열어요",
     "— Ja! Hier is mijn studentenkaart. En tot hoe ___ zijn jullie open? (A. lang · B. laat)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "A", "veel plezier = 재미있게 보내세요",
     "— Tot 18:00 uur. Veel ___ met de ontwerpen! (A. plezier · B. slaap)", size=13.8, gap=0)
f.ex("B1", "빈칸 채우기", "B", "tot ziens = 안녕히 가세요",
     "— Dank u wel, tot ___! (A. straks · B. ziens)", size=13.8, gap=0)
f.head("H　SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Zondag 25 oktober word ik laat wakker: het is de laatste dag van mijn herfstvakantie. "
          "Ik heb een uur langer geslapen, want vannacht ging de klok achteruit. "
          "Na het ontbijt ga ik met mijn vrienden naar het bos; de bladeren zijn geel en rood. "
          "'s Middags kijken wij thuis naar PSV tegen Feyenoord op televisie. "
          "Mijn zus gaat naar Amsterdam voor ADE, maar ik blijf liever thuis met een boek. "
          "'s Avonds pak ik mijn tas voor school: morgen begint het gewone leven weer. "
          "Wat een week!")
NWORDS = len(MODELO.split())
f.expl(f"쓰기 문제예요(정답이 하나가 아니에요); 모범 답안({NWORDS}단어)은 아래에 있어요.")
f.ex("B1", "쓰기", "(열린 문제, 모범 답안은 아래에)", f"모범 답안은 이 면 H 구역에 있어요 ({NWORDS}단어)",
     "«Jouw zondag 25 oktober» Schrijf 80–100 woorden: wat doe jij op de laatste vakantiedag, hoe laat sta jij op, en wat doe jij 's middags?", instr="쓰기", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　정답 — 면별로 정리했어요, 번호로 찾으세요", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "문제마다 짧은 해설이 있어요　✓ 표시는 모범 답안 문제예요", 19.5, "sans", False, GREY, anchor="end")
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
