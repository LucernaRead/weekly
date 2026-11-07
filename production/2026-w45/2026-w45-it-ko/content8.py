# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-it-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · 연습과 정답", "La Lucerna", "제 8 면 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "B", "primo freddo = 첫 추위",
     "Lunedì 2 novembre arriva il primo ___ della stagione. (A. caldo · B. freddo)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "추모의 날은 11월 2일이에요",
     "Il 2 novembre è la Commemorazione dei ___. (A. defunti · B. santi)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "문화 포럼은 밀라노에서 열려요",
     "Il Forum Cultura apre martedì a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "파네토네 결승은 토요일과 일요일이에요",
     "La finale del Panettone è sabato e ___ a Milano. (A. domenica · B. lunedì)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "토로네 축제는 크레모나에서 열려요",
     "La Festa del Torrone apre a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "세리에 A 11라운드는 일요일에 끝나요: chiude",
     "L'undicesima giornata ___ domenica 8 novembre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "피오렌티나–유벤투스는 일요일 저녁에 열려요",
     "Fiorentina–Juventus si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "민속 영화제는 피렌체에서 열려요",
     "Il Festival dei Popoli è a ___. (A. Milano · B. Firenze)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "객관식", "B", "초설은 1,300–1,500m쯤에 내려요",
     "La prima neve leggera può cadere intorno ai... A. 500 m · B. 1.300–1.500 m · C. 3.000 m", size=15.5, gap=1)
f.ex("A2", "객관식", "B", "추모의 날 꽃은 국화예요",
     "Il fiore del 2 novembre è... A. la rosa · B. il crisantemo · C. il tulipano", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "파네토네 결승에는 19개국 제빵사가 참가해요",
     "Alla finale del Panettone partecipano pasticceri da... A. 19 paesi · B. 5 paesi · C. 50 paesi", size=15.5, gap=1)
f.ex("B1", "객관식", "B", "문화 포럼에는 50개가 넘는 행사가 있어요",
     "Il Forum Cultura ha... A. 5 eventi · B. più di 50 eventi · C. 19 eventi", size=15.5, gap=1)
f.ex("B1", "객관식", "C", "알바 트러플 축제는 12월 6일에 끝나요",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "객관식", "A", "DPB는 10월 15일에 보냈어요",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "객관식", "B", "확률은 확실한 것과 달라요",
     "Una probabilità alta... A. è una certezza · B. non è una certezza · C. è un errore", size=15.5, gap=1)
f.ex("B1", "객관식", "B", "루카 코믹스는 11월 1일에 막을 내렸어요",
     "Lucca Comics si è chiusa... A. il 28 ottobre · B. il 1° novembre · C. l'8 novembre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Milano: sabato 7 novembre va alla finale del Panettone e assaggia il panettone tradizionale. Paolo vive a Cremona: sabato 7 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano la Serie A: fa freddo, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "객관식", "B", "Giulia는 밀라노 파네토네 결승에 가요",
     "Chi va alla finale del Panettone? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "Paolo는 토요일에 토로네 축제에 가요",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Milano · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "객관식", "B", "전통 파네토네는 Giulia가 맛본 거예요",
     "Il panettone tradizionale è assaggiato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "제목이 두 도시와 두 축제를 요약해요",
     "Il titolo migliore è... A. «Due città, due dolci» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "문장 만들기", "Lunedì arriva il primo freddo.", "시간 표현이 앞에 와요",
     "lunedì / arriva / il primo freddo → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "La finale è a Milano il 7 novembre.", "주어 + essere + 장소 + 날짜",
     "la finale / è a Milano / il 7 novembre → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "A che ora apre il Forum Cultura?", "의문사구가 문장 앞에 와요",
     "a che ora / apre / il Forum Cultura / ? → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "Il freddo arriva lunedì.", "주어 + 동사 + 시간 순이에요",
     "il freddo / arriva / lunedì → ___", instr="문장 만들기", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "번역", "월요일에 첫 추위가 찾아왔어요.", "원문과 비교하세요",
     "Lunedì arriva il primo freddo. → ___", instr="번역", size=15.5, gap=1)
f.ex("B1", "번역", "관객이 무료로 맛볼 수 있어요.", "assaggiare gratis = 무료로 맛보기",
     "Il pubblico può assaggiare gratis. → ___", instr="번역", size=15.5, gap=1)
f.ex("B1", "번역", "일요일 저녁, 피오렌티나–유벤투스 경기가 있어요.", "si gioca = 경기가 열려요",
     "Domenica sera si gioca Fiorentina–Juventus. → ___", instr="번역", size=15.5, gap=1)
f.ex("B2", "번역", "Ogni previsione deve essere chiara.", "dovere = 해야 해요",
     "모든 예보는 분명해야 해요. → ___", instr="번역", size=15.5, gap=1)
f.head("F · LE PAROLE DEL METEO", 22, OLIVE, 5)
f.match_set("B2", "단어 짝짓기",
            ["la probabilità", "la media", "il bollettino", "il modello"],
            ["il valore medio, tra tanti valori",
             "il documento con le previsioni più recenti",
             "il calcolo che prevede il tempo, come l'ECMWF",
             "quanto è possibile che una cosa succeda"],
            ["d", "a", "b", "c"],
            ["probabilità=가능성 d", "media=평균값 a", "bollettino=예보 공보 b", "modello=예보 모형 c"],
            instr="단어와 뜻 짝짓기")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "B", "torrone = 토로네",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "mandorle 아몬드",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "quanto costa? = 얼마예요?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "pagare con carta = 카드로 결제하기",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "토로네 축제는 11월 22일까지 이어져요",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Lunedì 2 novembre metto il cappotto e la sciarpa: arriva il primo freddo e la mattina è pungente. "
          "A scuola parliamo del Forum Cultura di Milano e del Festival dei Popoli di Firenze. "
          "Sabato assaggio il panettone con la mia famiglia: preferisco quello tradizionale, con i canditi. "
          "Domenica sera guardiamo Fiorentina–Juventus in televisione. "
          "Il freddo è arrivato, ma la settimana è dolce: cultura, dolci e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove del freddo.")
NWORDS = len(MODELO.split())
f.bridge(f"쓰기 문제예요 (정답이 하나만 있는 문제는 아니에요). 모범 답안 ({NWORDS}단어)은 아래에 있어요.")
f.ex("B1", "쓰기", "(열린 문제예요. 모범 답안은 아래에 있어요)", f"모범 답안은 이 면 H 구역에 있어요 ({NWORDS}단어)",
     "«La tua settimana del primo freddo» Scrivi 80–100 parole: il freddo, cosa metti, un evento o una festa del tuo weekend.", instr="쓰기", size=15.5, gap=1)
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
