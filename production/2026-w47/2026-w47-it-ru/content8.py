# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-it-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE　ТЕСТ И ОТВЕТЫ", "La Lucerna", "Стр. 8　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Вставьте слово", "B", "Лацио = Lazio",
     "La prima in classifica è la ___. (A. Roma · B. Lazio)", size=15.5, gap=1)
f.ex("B1", "Вставьте слово", "A", "24 гола в 11-м туре",
     "L'11ª giornata ha portato ___ gol. (A. 24 · B. 31)", size=15.5, gap=1)
f.ex("B1", "Вставьте слово", "A", "«Аталанта» — «Интер» в Бергамо",
     "Atalanta–Inter si gioca a ___. (A. Bergamo · B. Torino)", size=15.5, gap=1)
f.ex("B1", "Вставьте слово", "A", "Фестиваль торроне закрывается в воскресенье",
     "La Festa del Torrone chiude domenica a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "Вставьте слово", "B", "Фестиваль шоколада — в Перудже",
     "Eurochocolate chiude a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "Вставьте слово", "B", "Мадонна делла Салюте — 21 ноября",
     "La Madonna della Salute si celebra il ___ novembre. (A. 20 · B. 21)", size=15.5, gap=1)
f.ex("B1", "Вставьте слово", "A", "BookCity открывается 23 ноября",
     "BookCity apre lunedì ___. (A. 23 novembre · B. 22 novembre)", size=15.5, gap=1)
f.ex("B1", "Вставьте слово", "B", "Туринский кинофестиваль открывается 24 ноября",
     "Il Torino Film Festival apre... A. il 20 novembre · B. il 24 novembre", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Выберите ответ", "B", "«Лацио» лидирует с 29 очками",
     "La prima in classifica ha... A. 28 punti · B. 29 punti · C. 27 punti", size=15.5, gap=1)
f.ex("A2", "Выберите ответ", "B", "«Интер» обыграл «Комо» 2:0",
     "L'Inter vince 2–0 con... A. la Roma · B. il Como · C. il Milan", size=15.5, gap=1)
f.ex("A2", "Выберите ответ", "A", "Фестиваль шоколада проходит в 32-й раз",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 15ª edizione", size=15.5, gap=1)
f.ex("B1", "Выберите ответ", "C", "«Удинезе» последний с 5 очками",
     "L'ultima in classifica è... A. il Monza · B. il Venezia · C. l'Udinese", size=15.5, gap=1)
f.ex("B1", "Выберите ответ", "C", "Ярмарка трюфелей в Альбе — до 6 декабря",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "Выберите ответ", "A", "Срок подачи поправок — 17 ноября, 18:00",
     "Il termine per gli emendamenti è... A. il 17 novembre · B. il 9 novembre · C. il 31 dicembre", size=15.5, gap=1)
f.ex("B2", "Выберите ответ", "B", "Предложение правительства — ещё не закон",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "Выберите ответ", "B", "Праздник Мадонны делла Салюте — от обета 1630 года",
     "La festa della Salute nasce da un voto del... A. 1687 · B. 1630 · C. 1898", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Venezia: sabato 21 novembre attraversa il ponte votivo e porta una candela in basilica. Paolo vive a Cremona: domenica 22 novembre guarda il corteo del Torrone e assaggia il dolce con la sua famiglia. Domenica sera, Giulia e Paolo guardano Atalanta–Inter: è la festa del torrone, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "Выберите ответ", "B", "Джулия идёт на Мадонну делла Салюте в субботу",
     "Chi va alla Madonna della Salute? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Выберите ответ", "A", "Паоло смотрит шествие торроне в воскресенье",
     "Paolo, domenica, guarda... A. il corteo del Torrone · B. il ponte votivo · C. lo stadio", size=15.5, gap=1)
f.ex("A2", "Выберите ответ", "B", "Свечу приносит Джулия",
     "La candela è portata da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Выберите ответ", "A", "Заголовок объединяет два города и два праздника",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Составьте предложения", "Domenica è il 22 novembre.", "Сначала слово времени",
     "domenica / è / il 22 novembre → ___", instr="Составьте предложения", size=15.5, gap=1)
f.ex("B1", "Составьте предложения", "Eurochocolate chiude a Perugia il 22 novembre.", "Подлежащее + глагол + место + дата",
     "Eurochocolate / chiude / a Perugia / il 22 novembre → ___", instr="Составьте предложения", size=15.5, gap=1)
f.ex("B1", "Составьте предложения", "A che ora gioca la Lazio?", "Вопрос — в начале",
     "a che ora / gioca / la Lazio / ? → ___", instr="Составьте предложения", size=15.5, gap=1)
f.ex("B1", "Составьте предложения", "Il torrone si assaggia a Cremona.", "Подлежащее + глагол + место",
     "il torrone / si assaggia / a Cremona → ___", instr="Составьте предложения", size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", "Переведите", "В праздник Мадонны делла Салюте люди переходят обетный мост.", "Сравните с оригиналом",
     "Per la Madonna della Salute si attraversa il ponte votivo. → ___", instr="Переведите на русский", size=15.5, gap=1)
f.ex("B1", "Переведите", "В воскресенье вечером «Аталанта» играет с «Интером».", "si gioca = играется",
     "Domenica sera si gioca Atalanta–Inter. → ___", instr="Переведите на русский", size=15.5, gap=1)
f.ex("B1", "Переведите", "В субботу «Лацио» играет дома с «Лечче».", "in casa = дома",
     "Sabato la Lazio gioca in casa con il Lecce. → ___", instr="Переведите на русский", size=15.5, gap=1)
f.ex("B2", "Переведите", "Ogni cifra deve essere chiara.", "dovere = должен",
     "Каждая цифра должна быть понятной. → ___", instr="Переведите на итальянский", size=15.5, gap=1)
f.head("F　LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "Подберите слова",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["un livello di reddito del sistema fiscale",
             "i soldi che pagano una misura",
             "la differenza tra spese ed entrate",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra = бюджетный законопроект, d", "deficit = дефицит, c", "copertura = финансирование, b", "scaglione = ступень налоговой шкалы, a"],
            instr="Соедините слова")
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Вставьте слово", "B", "torrone = торроне (нуга)",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "Вставьте слово", "A", "mandorle = миндаль",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "Вставьте слово", "B", "quanto costa? = сколько это стоит?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Вставьте слово", "A", "pagare con carta = платить картой",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Вставьте слово", "B", "Фестиваль торроне длится до 22 ноября",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 22 novembre metto la sciarpa e vado a Cremona: è l'ultimo giorno della Festa del Torrone e il corteo passa in piazza del Comune. "
          "Assaggio il torrone con la mia famiglia: preferisco quello con le mandorle e il miele, a forma di Torrazzo. "
          "La sera guardiamo Atalanta–Inter, alle 20.45, e la Lazio è ancora prima con 29 punti. "
          "Sabato, a Venezia, c'era la Madonna della Salute: il ponte votivo e le candele accese. "
          "La settimana è dolce e azzurra: torrone, cioccolato e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove della settimana.")
NWORDS = len(MODELO.split())
f.bridge(f"Письменное задание (нет единственного ответа); образец текста ({NWORDS} слов) ниже.")
f.ex("B1", "Письмо", "(Открытое задание — образец текста ниже)", f"Образец текста в разделе H ниже ({NWORDS} слов)",
     "«La tua domenica del 22 novembre» Scrivi 80–100 parole: una festa, una partita, cosa assaggi.", instr="Напишите", size=15.5, gap=1)
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
p.text(MX, 1382, "RISPOSTE　ОТВЕТЫ — ПО СТРАНИЦАМ: НАЙДИТЕ СВОЙ НОМЕР", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "У каждого ответа — короткое примечание на русском　✓ = задание с образцом текста", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 14, "sans", True, OLIVE, lh=1.14, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Письмо":
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
