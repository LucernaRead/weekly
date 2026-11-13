# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-it-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE　연습과 정답", "La Lucerna", "8면　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "빈칸 선택", "B", "라치오 = Lazio",
     "La prima in classifica è la ___. (A. Roma · B. Lazio)", size=15.5, gap=1)
f.ex("B1", "빈칸 선택", "A", "11라운드 총 24골",
     "L'11ª giornata ha portato ___ gol. (A. 24 · B. 31)", size=15.5, gap=1)
f.ex("B1", "빈칸 선택", "A", "아탈란타 대 인터는 베르가모에서",
     "Atalanta–Inter si gioca a ___. (A. Bergamo · B. Torino)", size=15.5, gap=1)
f.ex("B1", "빈칸 선택", "A", "토로네 축제는 일요일에 폐막",
     "La Festa del Torrone chiude domenica a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "빈칸 선택", "B", "초콜릿 축제는 페루자에서",
     "Eurochocolate chiude a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "빈칸 선택", "B", "성모 건강 축일은 11월 21일",
     "La Madonna della Salute si celebra il ___ novembre. (A. 20 · B. 21)", size=15.5, gap=1)
f.ex("B1", "빈칸 선택", "A", "북시티는 11월 23일에 개막",
     "BookCity apre lunedì ___. (A. 23 novembre · B. 22 novembre)", size=15.5, gap=1)
f.ex("B1", "빈칸 선택", "B", "토리노 영화제는 11월 24일에 개막",
     "Il Torino Film Festival apre... A. il 20 novembre · B. il 24 novembre", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "객관식", "B", "라치오가 29점으로 선두",
     "La prima in classifica ha... A. 28 punti · B. 29 punti · C. 27 punti", size=15.5, gap=1)
f.ex("A2", "객관식", "B", "인터가 코모를 2-0으로 이겼다",
     "L'Inter vince 2–0 con... A. la Roma · B. il Como · C. il Milan", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "초콜릿 축제는 제32회",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 15ª edizione", size=15.5, gap=1)
f.ex("B1", "객관식", "C", "우디네세는 5점으로 최하위",
     "L'ultima in classifica è... A. il Monza · B. il Venezia · C. l'Udinese", size=15.5, gap=1)
f.ex("B1", "객관식", "C", "알바 트러플 축제는 12월 6일까지",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "객관식", "A", "수정안 마감은 11월 17일 18시",
     "Il termine per gli emendamenti è... A. il 17 novembre · B. il 9 novembre · C. il 31 dicembre", size=15.5, gap=1)
f.ex("B2", "객관식", "B", "정부 제안이 곧 법률은 아니다",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "객관식", "B", "성모 건강 축일은 1630년의 서원에서 비롯됐다",
     "La festa della Salute nasce da un voto del... A. 1687 · B. 1630 · C. 1898", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Venezia: sabato 21 novembre attraversa il ponte votivo e porta una candela in basilica. Paolo vive a Cremona: domenica 22 novembre guarda il corteo del Torrone e assaggia il dolce con la sua famiglia. Domenica sera, Giulia e Paolo guardano Atalanta–Inter: è la festa del torrone, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "객관식", "B", "줄리아는 토요일에 성모 건강 축일에 간다",
     "Chi va alla Madonna della Salute? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "파올로는 일요일에 토로네 행렬을 본다",
     "Paolo, domenica, guarda... A. il corteo del Torrone · B. il ponte votivo · C. lo stadio", size=15.5, gap=1)
f.ex("A2", "객관식", "B", "초는 줄리아가 가져간다",
     "La candela è portata da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "제목은 두 도시, 두 축제를 아우른다",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "문장 만들기", "Domenica è il 22 novembre.", "시간 말이 먼저",
     "domenica / è / il 22 novembre → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "Eurochocolate chiude a Perugia il 22 novembre.", "주어 + 동사 + 장소 + 날짜",
     "Eurochocolate / chiude / a Perugia / il 22 novembre → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "A che ora gioca la Lazio?", "의문어구는 문장 맨 앞에",
     "a che ora / gioca / la Lazio / ? → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "Il torrone si assaggia a Cremona.", "주어 + 동사 + 장소",
     "il torrone / si assaggia / a Cremona → ___", instr="문장 만들기", size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", "번역하기", "성모 건강 축일에는 사람들이 서원의 다리를 건넌다.", "원문과 비교하세요",
     "Per la Madonna della Salute si attraversa il ponte votivo. → ___", instr="한국어로 번역하세요", size=15.5, gap=1)
f.ex("B1", "번역하기", "일요일 저녁, 아탈란타가 인터와 경기한다.", "si gioca = 경기가 있다",
     "Domenica sera si gioca Atalanta–Inter. → ___", instr="한국어로 번역하세요", size=15.5, gap=1)
f.ex("B1", "번역하기", "토요일, 라치오는 홈에서 레체와 경기한다.", "in casa = 홈에서",
     "Sabato la Lazio gioca in casa con il Lecce. → ___", instr="한국어로 번역하세요", size=15.5, gap=1)
f.ex("B2", "번역하기", "Ogni cifra deve essere chiara.", "dovere = ~해야 한다",
     "모든 숫자는 분명해야 합니다. → ___", instr="이탈리아어로 번역하세요", size=15.5, gap=1)
f.head("F　LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "단어 짝짓기",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["un livello di reddito del sistema fiscale",
             "i soldi che pagano una misura",
             "la differenza tra spese ed entrate",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra = 예산안 d", "deficit = 적자 c", "copertura = 재원 b", "scaglione = 세율 구간 a"],
            instr="단어와 뜻을 연결하세요")
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "빈칸 선택", "B", "torrone = 누가",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "빈칸 선택", "A", "mandorle = 아몬드",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "빈칸 선택", "B", "quanto costa? = 얼마예요?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "빈칸 선택", "A", "pagare con carta = 카드로 내다",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "빈칸 선택", "B", "토로네 축제는 11월 22일까지 이어진다",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 22 novembre metto la sciarpa e vado a Cremona: è l'ultimo giorno della Festa del Torrone e il corteo passa in piazza del Comune. "
          "Assaggio il torrone con la mia famiglia: preferisco quello con le mandorle e il miele, a forma di Torrazzo. "
          "La sera guardiamo Atalanta–Inter, alle 20.45, e la Lazio è ancora prima con 29 punti. "
          "Sabato, a Venezia, c'era la Madonna della Salute: il ponte votivo e le candele accese. "
          "La settimana è dolce e azzurra: torrone, cioccolato e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove della settimana.")
NWORDS = len(MODELO.split())
f.bridge(f"쓰기 과제(정답이 하나가 아닙니다); 모범 답안({NWORDS}단어) 아래.")
f.ex("B1", "쓰기", "(열린 문제 — 모범 답안은 아래에)", f"모범 답안은 이 면 H 구역에（{NWORDS}단어)",
     "«La tua domenica del 22 novembre» Scrivi 80–100 parole: una festa, una partita, cosa assaggi.", instr="쓰기", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()
print("P8 exercises flow ends col", f.ci, "y=", f.y)
# ---- Vermeer image under the exercises flow (measured slot, col 3) ----
if f.y + 10 + 170 + 70 <= 1332:
    image(p, "lettera.jpg", COLX[3], f.y + 10, CW, 170)
    caption(p, COLX[3], f.y + 180, CW, "Una donna scrive una lettera: la scrittura è l'ultimo esercizio della settimana.",
            "Foto: Johannes Vermeer — Wikimedia Commons, dominio pubblico")
    print("P8 lettera image placed at y=", f.y + 10)
else:
    print("  !! P8 LETTERA NOSPACE: flow ends y=", f.y)

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, OLIVE, 2)
p.text(MX, 1382, "RISPOSTE　정답 — 면별로 정리: 번호로 찾으세요", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "각 정답에 한국어 한 줄 설명　✓ = 모범 답안 과제", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 제 {pg} 면 —", 14, "sans", True, OLIVE, lh=1.14, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "쓰기":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13, lh=1.14, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-valutazione.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
