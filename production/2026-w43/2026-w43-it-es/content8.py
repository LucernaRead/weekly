# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-it-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · EJERCICIOS Y RESPUESTAS", "La Lucerna", "Página 8 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Cloze", "B", "tornare indietro = atrasarse",
     "Domenica l'orologio torna ___ di un'ora. (A. avanti · B. indietro)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "la noche del cambio de hora dura 25 horas",
     "La notte tra sabato e domenica dura ___ ore. (A. 25 · B. 23)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "incontrare = enfrentarse a, jugar contra",
     "Alle 12:30 l'Inter ___ la Fiorentina a San Siro. (A. incontra · B. visita)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "Nápoles–Roma se juega el sábado",
     "Napoli–Roma si gioca ___ alle 18:00. (A. sabato · B. domenica)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "en Montaione es la fiesta de la trufa",
     "A Montaione è la festa del ___. (A. tartufo · B. cinema)", size=15.5, gap=1)
f.ex("B1", "Cloze", "B", "el festival cierra el domingo: chiude",
     "La Festa del Cinema di Roma ___ domenica 25. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "Lucca abre el 28 de octubre: apre",
     "Lucca Comics ___ il 28 ottobre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "Cloze", "B", "el 28 de octubre es miércoles",
     "Il voto sulla manovra è atteso per ___ 28 ottobre. (A. lunedì · B. mercoledì)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Opción múltiple", "B", "a las 03:00 se vuelve a las 02:00",
     "Il cambio dell'ora: alle 03:00 → ... A. 04:00 · B. 02:00 · C. 01:00", size=15.5, gap=1)
f.ex("A2", "Opción múltiple", "B", "«meteo oggi» es la búsqueda número uno",
     "«Meteo oggi» è... A. un film · B. la ricerca numero uno · C. una festa", size=15.5, gap=1)
f.ex("A2", "Opción múltiple", "A", "la tormenta se llama Adam",
     "La tempesta della settimana si chiama... A. Adam · B. Legacy · C. Bagòss", size=15.5, gap=1)
f.ex("B1", "Opción múltiple", "B", "la feria de la trufa blanca está en Alba",
     "La Fiera del Tartufo Bianco è a... A. Volterra · B. Alba · C. Bagolino", size=15.5, gap=1)
f.ex("B1", "Opción múltiple", "C", "la exposición de Artemisia está en Florencia",
     "La mostra su Artemisia è a... A. Roma · B. Lucca · C. Firenze", size=15.5, gap=1)
f.ex("B1", "Opción múltiple", "A", "el DPB se envió a Bruselas el 15 de octubre",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "Opción múltiple", "B", "las cifras del DPB son previsiones",
     "Le cifre del DPB sono... A. risultati · B. previsioni · C. voti", size=15.5, gap=1)
f.ex("B1", "Opción múltiple", "B", "Todos los Santos cae este año el domingo 1 de noviembre",
     "Ognissanti, quest'anno, è... A. lunedì 2 novembre · B. domenica 1° novembre · C. sabato 31 ottobre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Lucca: mercoledì 28 ottobre va a Lucca Comics con il suo cosplay. Paolo vive a Roma: domenica 25 va all'Auditorium per l'ultimo giorno della Festa del Cinema. Sabato, Giulia e Paolo dormono un'ora in più: domenica comincia l'ora solare.", 16.5, lh=1.3, split=False)
f.ex("A2", "Opción múltiple", "B", "Giulia va a Lucca Comics",
     "Chi va a Lucca Comics? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Opción múltiple", "A", "Paolo va el domingo a la Festa del Cinema",
     "Paolo, domenica, va... A. alla Festa del Cinema · B. a Lucca · C. a una sagra", size=15.5, gap=1)
f.ex("A2", "Opción múltiple", "B", "el cosplay es de Giulia",
     "Il cosplay è di... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Opción múltiple", "A", "el título resume dos ciudades y dos fiestas",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Formar frases", "Domenica dormiamo un'ora in più.", "el tiempo va primero",
     "domenica / dormiamo / un'ora in più → ___", instr="Forma la frase", size=15.5, gap=1)
f.ex("B1", "Formar frases", "La fiera è iniziata il 10 ottobre.", "sujeto + essere + participio",
     "la fiera / è iniziata / il 10 ottobre → ___", instr="Forma la frase", size=15.5, gap=1)
f.ex("B1", "Formar frases", "A che ora comincia la partita?", "la pregunta va al principio",
     "a che ora / comincia / la partita / ? → ___", instr="Forma la frase", size=15.5, gap=1)
f.ex("B1", "Formar frases", "Il voto slitta a mercoledì.", "sujeto + verbo + complemento",
     "il voto / slitta / a mercoledì → ___", instr="Forma la frase", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "Traducción", "El domingo dormimos una hora más.", "de la página 1",
     "Domenica dormiamo un'ora in più. → ___", instr="Traduce", size=15.5, gap=1)
f.ex("B1", "Traducción", "La exposición sigue abierta hasta abril.", "sigue abierta",
     "La mostra resta aperta fino ad aprile. → ___", instr="Traduce", size=15.5, gap=1)
f.ex("B1", "Traducción", "Sabato alle 18:00 si gioca Napoli–Roma.", "si gioca = se juega",
     "El sábado a las 18:00, Nápoles contra Roma. → ___", instr="Traduce", size=15.5, gap=1)
f.ex("B2", "Traducción", "Ogni cifra deve avere una fonte.", "dovere = deber, tener que",
     "Cada cifra debe tener una fuente. → ___", instr="Traduce", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "Emparejar",
            ["la manovra", "il rinvio", "il miliardo", "la previsione"],
            ["un numero che descrive il futuro",
             "la legge di bilancio dello Stato",
             "quando una cosa arriva più tardi del previsto",
             "mille milioni"],
            ["b", "c", "d", "a"],
            ["manovra = el presupuesto: b", "rinvio = llega más tarde de lo previsto: c", "miliardo = mil millones: d", "previsione = un número que describe el futuro: a"],
            instr="Empareja")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Cloze", "B", "tartufo = la trufa",
     "— Cerco il ___ bianco famoso. (A. biglietto · B. tartufo)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "castagne arrosto = castañas asadas",
     "— Vuole anche le castagne ___? (A. arrosto · B. mute)", size=15.5, gap=1)
f.ex("B1", "Cloze", "B", "quanto costa? = ¿cuánto cuesta?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "pagare con carta = pagar con tarjeta",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Cloze", "B", "la fiesta dura hasta el domingo",
     "— La sagra è in piazza fino a ___. (A. aprile · B. domenica)", size=15.5, gap=1)
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 25 ottobre mi sveglio tardi: nella notte l'orologio è tornato indietro e ho dormito un'ora in più. "
          "Sabato sera ho cambiato gli orologi di casa: quello del forno e quello vecchio in cucina. "
          "Faccio colazione con calma e vado al mercato con mia sorella. A pranzo guardiamo Inter–Fiorentina: "
          "è la prima partita con l'ora solare. Nel pomeriggio leggo un libro e preparo la settimana. "
          "La sera è già buio presto, ma non mi dispiace: l'autunno è la mia stagione preferita, "
          "con le sagre, il tartufo e le castagne calde.")
NWORDS = len(MODELO.split())
f.expl(f"Ejercicio de escritura (sin respuesta única); el texto modelo ({NWORDS} palabras) está a continuación.")
f.ex("B1", "Escritura", "(pregunta abierta — texto modelo a continuación)", f"El modelo está en la sección H ({NWORDS} palabras)",
     "«La tua domenica 25 ottobre» Scrivi 80–100 parole: il cambio dell'ora, cosa fai con l'ora in più, una partita o una festa del tuo weekend.", instr="Escribe", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RISPOSTE · RESPUESTAS — por página, busca el número del ejercicio", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Una breve explicación en español para cada ejercicio · ✓ = ejercicio de escritura", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} ({e_['note']})"
        if e_["type"] == "Escritura":
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
