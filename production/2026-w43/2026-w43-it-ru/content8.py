# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-it-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · ПРОВЕРКА И ОТВЕТЫ", "La Lucerna", "Страница 8 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Тест с пропусками", "B", "tornare indietro = назад",
     "Domenica l'orologio torna ___ di un'ora. (A. avanti · B. indietro)", size=15.5, gap=1)
f.ex("B1", "Тест с пропусками", "A", "ночь перевода часов длится 25 часов",
     "La notte tra sabato e domenica dura ___ ore. (A. 25 · B. 23)", size=15.5, gap=1)
f.ex("B1", "Тест с пропусками", "A", "incontrare = встречать, играть против",
     "Alle 12:30 l'Inter ___ la Fiorentina a San Siro. (A. incontra · B. visita)", size=15.5, gap=1)
f.ex("B1", "Тест с пропусками", "A", "«Наполи» — «Рома» в субботу",
     "Napoli–Roma si gioca ___ alle 18:00. (A. sabato · B. domenica)", size=15.5, gap=1)
f.ex("B1", "Тест с пропусками", "A", "в Монтайоне — праздник трюфеля",
     "A Montaione è la festa del ___. (A. tartufo · B. cinema)", size=15.5, gap=1)
f.ex("B1", "Тест с пропусками", "B", "фестиваль закрывается в воскресенье: chiude",
     "La Festa del Cinema di Roma ___ domenica 25. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "Тест с пропусками", "A", "Лукка открывается 28 октября: apre",
     "Lucca Comics ___ il 28 ottobre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "Тест с пропусками", "B", "28 октября — среда",
     "Il voto sulla manovra è atteso per ___ 28 ottobre. (A. lunedì · B. mercoledì)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Выбор ответа", "B", "03:00 снова станут 02:00",
     "Il cambio dell'ora: alle 03:00 → ... A. 04:00 · B. 02:00 · C. 01:00", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "B", "«meteo oggi» — запрос № 1",
     "«Meteo oggi» è... A. un film · B. la ricerca numero uno · C. una festa", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "A", "шторм называется Adam",
     "La tempesta della settimana si chiama... A. Adam · B. Legacy · C. Bagòss", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "B", "ярмарка белого трюфеля — в Альбе",
     "La Fiera del Tartufo Bianco è a... A. Volterra · B. Alba · C. Bagolino", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "C", "выставка Артемизии — во Флоренции",
     "La mostra su Artemisia è a... A. Roma · B. Lucca · C. Firenze", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "A", "DPB отправлен 15 октября",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "Выбор ответа", "B", "цифры DPB — прогнозы",
     "Le cifre del DPB sono... A. risultati · B. previsioni · C. voti", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "B", "День всех святых в этом году — воскресенье, 1 ноября",
     "Ognissanti, quest'anno, è... A. lunedì 2 novembre · B. domenica 1° novembre · C. sabato 31 ottobre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Lucca: mercoledì 28 ottobre va a Lucca Comics con il suo cosplay. Paolo vive a Roma: domenica 25 va all'Auditorium per l'ultimo giorno della Festa del Cinema. Sabato, Giulia e Paolo dormono un'ora in più: domenica comincia l'ora solare.", 16.5, lh=1.3, split=False)
f.ex("A2", "Выбор ответа", "B", "Giulia едет на Lucca Comics",
     "Chi va a Lucca Comics? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "A", "Paolo в воскресенье идёт на кинофестиваль",
     "Paolo, domenica, va... A. alla Festa del Cinema · B. a Lucca · C. a una sagra", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "B", "косплей — у Giulia",
     "Il cosplay è di... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "A", "заголовок — о двух городах и двух праздниках",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Составьте предложение", "Domenica dormiamo un'ora in più.", "время впереди",
     "domenica / dormiamo / un'ora in più → ___", instr="Составьте предложение", size=15.5, gap=1)
f.ex("B1", "Составьте предложение", "La fiera è iniziata il 10 ottobre.", "essere + причастие",
     "la fiera / è iniziata / il 10 ottobre → ___", instr="Составьте предложение", size=15.5, gap=1)
f.ex("B1", "Составьте предложение", "A che ora comincia la partita?", "вопрос — в начале",
     "a che ora / comincia / la partita / ? → ___", instr="Составьте предложение", size=15.5, gap=1)
f.ex("B1", "Составьте предложение", "Il voto slitta a mercoledì.", "субъект + глагол",
     "il voto / slitta / a mercoledì → ___", instr="Составьте предложение", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "Перевод", "В воскресенье мы спим на час дольше.", "См. оригинал",
     "Domenica dormiamo un'ora in più. → ___", instr="Перевод", size=15.5, gap=1)
f.ex("B1", "Перевод", "Выставка открыта до апреля.", "resta aperta: открыта",
     "La mostra resta aperta fino ad aprile. → ___", instr="Перевод", size=15.5, gap=1)
f.ex("B1", "Перевод", "Sabato alle 18:00 si gioca Napoli–Roma.", "si gioca = играют",
     "В субботу в 18:00 «Наполи» играет с «Ромой». → ___", instr="Перевод", size=15.5, gap=1)
f.ex("B2", "Перевод", "Ogni cifra deve avere una fonte.", "dovere = должен, нужно",
     "У каждой цифры должен быть источник. → ___", instr="Перевод", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "Соедините пары",
            ["la manovra", "il rinvio", "il miliardo", "la previsione"],
            ["un numero che descrive il futuro",
             "la legge di bilancio dello Stato",
             "quando una cosa arriva più tardi del previsto",
             "mille milioni"],
            ["b", "c", "d", "a"],
            ["manovra = бюджетный закон b", "rinvio = прибытие позже срока c", "miliardo = миллиард d", "previsione = цифра о будущем a"],
            instr="Соедините пары")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Тест с пропусками", "B", "tartufo = трюфель",
     "— Cerco il ___ bianco famoso. (A. biglietto · B. tartufo)", size=15.5, gap=1)
f.ex("B1", "Тест с пропусками", "A", "castagne arrosto = жареные каштаны",
     "— Vuole anche le castagne ___? (A. arrosto · B. mute)", size=15.5, gap=1)
f.ex("B1", "Тест с пропусками", "B", "quanto costa? = сколько стоит?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Тест с пропусками", "A", "pagare con carta = платить картой",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Тест с пропусками", "B", "праздник еды — до воскресенья",
     "— La sagra è in piazza fino a ___. (A. aprile · B. domenica)", size=15.5, gap=1)
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 25 ottobre mi sveglio tardi: nella notte l'orologio è tornato indietro e ho dormito un'ora in più. "
          "Sabato sera ho cambiato gli orologi di casa: quello del forno e quello vecchio in cucina. "
          "Faccio colazione con calma e vado al mercato con mia sorella. A pranzo guardiamo Inter–Fiorentina: "
          "è la prima partita con l'ora solare. Nel pomeriggio leggo un libro e preparo la settimana. "
          "La sera è già buio presto, ma non mi dispiace: l'autunno è la mia stagione preferita, "
          "con le sagre, il tartufo e le castagne calde.")
NWORDS = len(MODELO.split())
f.expl(f"Задание на письмо (единственного ответа нет); образец ({NWORDS} слов) — ниже.")
f.ex("B1", "Письмо", "(открытый вопрос — образец ниже)", f"Образец — в разделе H этой страницы ({NWORDS} слов)",
     "«La tua domenica 25 ottobre» Scrivi 80–100 parole: il cambio dell'ora, cosa fai con l'ora in più, una partita o una festa del tuo weekend.", instr="Письмо", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RISPOSTE · ОТВЕТЫ — по страницам: ищите по номеру задачи", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "К каждой задаче — пояснение · ✓ — задание с образцом", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Письмо":
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
