# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · 연습과 정답", "La Lucerna", "제 8 면 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "B", "성 마르티노 = San Martino",
     "Mercoledì 11 novembre è ___. (A. Natale · B. San Martino)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "포도즙이 새 와인이 된다",
     "A San Martino ogni mosto diventa ___. (A. vino · B. latte)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "이탈리아 대 프랑스는 산 시로에서",
     "Italia–Francia si gioca a ___. (A. San Siro · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "초콜릿 축제는 금요일에 개막",
     "Eurochocolate apre venerdì a ___. (A. Perugia · B. Cuneo)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "토로네 축제는 크레모나에서 열려요",
     "La Festa del Torrone continua a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "포폴리 영화제: 86편",
     "Il Festival dei Popoli ha presentato ___ film. (A. 50 · B. 86)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "벨기에 대 이탈리아는 일요일 밤",
     "Belgio–Italia si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "스크리토린치타는 쿠네오에서 열린다",
     "Scrittorincittà è a ___. (A. Milano · B. Cuneo)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "객관식", "B", "성 마르티노의 여름은 사흘하고 조금 더 지속된다",
     "L'estate di San Martino dura... A. un mese · B. tre giorni e un pochino · C. un'ora", size=15.5, gap=1)
f.ex("A2", "객관식", "B", "망토는 마르티노가 거지와 나눈 것",
     "Martino divide... A. il pane · B. il mantello · C. il vino", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "초콜릿 축제는 제32회",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 67ª edizione", size=15.5, gap=1)
f.ex("B1", "객관식", "B", "조 1위 프랑스 10점",
     "Nel girone di Nations League, la Francia ha... A. 7 punti · B. 10 punti · C. 0 punti", size=15.5, gap=1)
f.ex("B1", "객관식", "C", "알바 트러플 축제는 12월 6일에 끝나요",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "객관식", "A", "DPB는 10월 15일에 보냈어요",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "객관식", "B", "정부 제안은 아직 법률이 아니다",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "객관식", "B", "포폴리 영화제는 11월 8일에 폐막",
     "Il Festival dei Popoli si è chiuso... A. il 31 ottobre · B. l'8 novembre · C. il 15 novembre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Cuneo: mercoledì 11 novembre va a Scrittorincittà e ascolta un autore. Paolo vive a Cremona: sabato 14 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano Belgio–Italia: è San Martino, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "객관식", "B", "줄리아는 수요일에 스크리토린치타에 간다",
     "Chi va a Scrittorincittà? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "Paolo는 토요일에 토로네 축제에 가요",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Cuneo · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "객관식", "B", "작가를 듣는 사람은 줄리아다",
     "L'autore è ascoltato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "제목이 두 도시와 두 축제를 요약해요",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "문장 만들기", "Mercoledì è San Martino.", "시간 표현이 앞에 와요",
     "mercoledì / è / San Martino → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "Eurochocolate è a Perugia dal 13 novembre.", "주어 + essere + 장소 + 날짜",
     "Eurochocolate / è a Perugia / dal 13 novembre → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "A che ora gioca l'Italia?", "의문사구가 문장 앞에 와요",
     "a che ora / gioca / l'Italia / ? → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "Il vino nuovo si assaggia in cantina.", "주어 + 동사 + 장소",
     "il vino nuovo / si assaggia / in cantina → ___", instr="문장 만들기", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "번역", "성 마르티노 축일에 포도즙은 와인이 된다.", "원문과 비교하기",
     "A San Martino ogni mosto diventa vino. → ___", instr="번역", size=15.5, gap=1)
f.ex("B1", "번역", "목요일 밤, 이탈리아 대 프랑스.", "si gioca = 경기가 열린다",
     "Giovedì sera si gioca Italia–Francia. → ___", instr="번역", size=15.5, gap=1)
f.ex("B1", "번역", "일요일 밤, 벨기에 대 이탈리아.", "si gioca = 경기가 열린다",
     "Domenica sera si gioca Belgio–Italia. → ___", instr="번역", size=15.5, gap=1)
f.ex("B2", "번역", "Ogni cifra deve essere chiara.", "dovere = ~해야 한다",
     "모든 숫자는 분명해야 한다. → ___", instr="번역", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "단어 짝짓기",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["la parte del sistema fiscale, un livello di reddito",
             "i soldi che pagano una misura, la sua fonte",
             "la differenza tra spese ed entrate, in rosso",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra=예산 법안 d", "deficit=적자 c", "copertura=재원 b", "scaglione=세율 구간 a"],
            instr="단어와 뜻 짝짓기")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "B", "torrone = 토로네",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "mandorle = 아몬드",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "quanto costa? = 얼마예요?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "pagare con carta = 카드로 결제하기",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "토로네 축제는 11월 22일까지 이어져요",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Mercoledì 11 novembre metto la sciarpa e vado in cantina: è San Martino e il vino nuovo si assaggia. "
          "A scuola parliamo della leggenda del mantello diviso e dell'estate di tre giorni. "
          "Sabato assaggio il torrone con la mia famiglia: preferisco quello di Cremona, con le mandorle e il miele. "
          "Giovedì sera guardiamo Italia–Francia in televisione, alle 20.45. "
          "Domenica, poi, il Belgio: due notti azzurre in una settimana. "
          "San Martino è arrivato, ma la settimana è dolce: vino nuovo, castagne e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove di San Martino.")
NWORDS = len(MODELO.split())
f.bridge(f"쓰기 문제예요 (정답이 하나만 있는 문제는 아니에요). 모범 답안 ({NWORDS}단어)은 아래에 있어요.")
f.ex("B1", "쓰기", "(열린 문제예요. 모범 답안은 아래에 있어요)", f"모범 답안은 이 면 H 구역에 있어요 ({NWORDS}단어)",
     "«La tua settimana di San Martino» Scrivi 80–100 parole: San Martino, cosa assaggi, un evento o una festa del tuo weekend.", instr="쓰기", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, GOLD, 2)
p.text(MX, 1382, "RISPOSTE · 정답 — 면별로 정리했어요. 번호를 찾으면 돼요", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "문제마다 짧은 해설이 있어요 · ✓ 표시는 모범 답안 문제예요", 19.5, "sans", False, GREY, anchor="end")
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
