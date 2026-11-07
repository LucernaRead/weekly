# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-it-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · 연습과 정답", "La Lucerna", "제 8 면 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "B", "tornare indietro = 뒤로 돌리기",
     "Domenica l'orologio torna ___ di un'ora. (A. avanti · B. indietro)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "시간을 바꾸는 밤은 25시간이에요",
     "La notte tra sabato e domenica dura ___ ore. (A. 25 · B. 23)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "incontrare = 맞붙기/대결",
     "Alle 12:30 l'Inter ___ la Fiorentina a San Siro. (A. incontra · B. visita)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "나폴리–로마 경기는 토요일이에요",
     "Napoli–Roma si gioca ___ alle 18:00. (A. sabato · B. domenica)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "몬타이오네는 트러플 축제예요",
     "A Montaione è la festa del ___. (A. tartufo · B. cinema)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "영화제는 일요일에 막을 내려요: chiude",
     "La Festa del Cinema di Roma ___ domenica 25. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "루카는 10월 28일에 열려요: apre",
     "Lucca Comics ___ il 28 ottobre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "10월 28일은 수요일이에요",
     "Il voto sulla manovra è atteso per ___ 28 ottobre. (A. lunedì · B. mercoledì)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "객관식", "B", "03:00가 02:00로 돌아가요",
     "Il cambio dell'ora: alle 03:00 → ... A. 04:00 · B. 02:00 · C. 01:00", size=15.5, gap=1)
f.ex("A2", "객관식", "B", "«meteo oggi»가 인기 검색 1위예요",
     "«Meteo oggi» è... A. un film · B. la ricerca numero uno · C. una festa", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "폭풍 이름은 Adam이에요",
     "La tempesta della settimana si chiama... A. Adam · B. Legacy · C. Bagòss", size=15.5, gap=1)
f.ex("B1", "객관식", "B", "화이트 트러플 축제는 알바에서 열려요",
     "La Fiera del Tartufo Bianco è a... A. Volterra · B. Alba · C. Bagolino", size=15.5, gap=1)
f.ex("B1", "객관식", "C", "아르테미시아 전시는 피렌체에서 열려요",
     "La mostra su Artemisia è a... A. Roma · B. Lucca · C. Firenze", size=15.5, gap=1)
f.ex("B1", "객관식", "A", "DPB는 10월 15일에 보냈어요",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "객관식", "B", "DPB 숫자는 전망이에요",
     "Le cifre del DPB sono... A. risultati · B. previsioni · C. voti", size=15.5, gap=1)
f.ex("B1", "객관식", "B", "올해 만성절은 11월 1일 일요일이에요",
     "Ognissanti, quest'anno, è... A. lunedì 2 novembre · B. domenica 1° novembre · C. sabato 31 ottobre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Lucca: mercoledì 28 ottobre va a Lucca Comics con il suo cosplay. Paolo vive a Roma: domenica 25 va all'Auditorium per l'ultimo giorno della Festa del Cinema. Sabato, Giulia e Paolo dormono un'ora in più: domenica comincia l'ora solare.", 16.5, lh=1.3, split=False)
f.ex("A2", "객관식", "B", "Giulia가 루카 코믹스에 가요",
     "Chi va a Lucca Comics? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "Paolo는 일요일에 영화제에 가요",
     "Paolo, domenica, va... A. alla Festa del Cinema · B. a Lucca · C. a una sagra", size=15.5, gap=1)
f.ex("A2", "객관식", "B", "코스프레는 Giulia의 것이에요",
     "Il cosplay è di... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "제목이 두 도시와 두 축제를 요약해요",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "문장 만들기", "Domenica dormiamo un'ora in più.", "시간 표현이 앞에 와요",
     "domenica / dormiamo / un'ora in più → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "La fiera è iniziata il 10 ottobre.", "주어 + essere + 과거분사 + 날짜",
     "la fiera / è iniziata / il 10 ottobre → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "A che ora comincia la partita?", "의문사구가 문장 앞에 와요",
     "a che ora / comincia / la partita / ? → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "Il voto slitta a mercoledì.", "주어 + 동사 + 전치사구 순이에요",
     "il voto / slitta / a mercoledì → ___", instr="문장 만들기", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "번역", "일요일에 우리는 한 시간 더 자요.", "원문과 비교하세요",
     "Domenica dormiamo un'ora in più. → ___", instr="번역", size=15.5, gap=1)
f.ex("B1", "번역", "전시는 4월까지 계속 열려 있어요.", "resta aperta = 계속 열려 있는 것",
     "La mostra resta aperta fino ad aprile. → ___", instr="번역", size=15.5, gap=1)
f.ex("B1", "번역", "Sabato alle 18:00 si gioca Napoli–Roma.", "si gioca = 경기가 열려요",
     "토요일 18시에 나폴리–로마 경기가 열려요. → ___", instr="번역", size=15.5, gap=1)
f.ex("B2", "번역", "Ogni cifra deve avere una fonte.", "dovere = 해야 해요",
     "모든 숫자에는 출처가 있어야 해요. → ___", instr="번역", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "단어 짝짓기",
            ["la manovra", "il rinvio", "il miliardo", "la previsione"],
            ["un numero che descrive il futuro",
             "la legge di bilancio dello Stato",
             "quando una cosa arriva più tardi del previsto",
             "mille milioni"],
            ["b", "c", "d", "a"],
            ["manovra=예산 법안 b", "rinvio=예정보다 늦게 오는 것 c", "miliardo=10억 d", "previsione=미래를 설명하는 숫자 a"],
            instr="단어와 뜻 짝짓기")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "B", "tartufo = 트러플",
     "— Cerco il ___ bianco famoso. (A. biglietto · B. tartufo)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "castagne arrosto = 군밤",
     "— Vuole anche le castagne ___? (A. arrosto · B. mute)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "quanto costa? = 얼마예요?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "pagare con carta = 카드로 결제하기",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "음식 축제는 일요일까지 계속돼요",
     "— La sagra è in piazza fino a ___. (A. aprile · B. domenica)", size=15.5, gap=1)
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 25 ottobre mi sveglio tardi: nella notte l'orologio è tornato indietro e ho dormito un'ora in più. "
          "Sabato sera ho cambiato gli orologi di casa: quello del forno e quello vecchio in cucina. "
          "Faccio colazione con calma e vado al mercato con mia sorella. A pranzo guardiamo Inter–Fiorentina: "
          "è la prima partita con l'ora solare. Nel pomeriggio leggo un libro e preparo la settimana. "
          "La sera è già buio presto, ma non mi dispiace: l'autunno è la mia stagione preferita, "
          "con le sagre, il tartufo e le castagne calde.")
NWORDS = len(MODELO.split())
f.expl(f"쓰기 문제예요 (정답이 하나만 있는 문제는 아니에요). 모범 답안 ({NWORDS}단어)은 아래에 있어요.")
f.ex("B1", "쓰기", "(열린 문제예요. 모범 답안은 아래에 있어요)", f"모범 답안은 이 면 H 구역에 있어요 ({NWORDS}단어)",
     "«La tua domenica 25 ottobre» Scrivi 80–100 parole: il cambio dell'ora, cosa fai con l'ora in più, una partita o una festa del tuo weekend.", instr="쓰기", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RISPOSTE · 정답 — 면별로 정리했어요. 번호를 찾으면 돼요", 25, "sans", True, OLIVE)
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
p.save(f"{OUT}/p8-valutazione.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
