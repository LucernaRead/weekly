# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE　EJERCICIOS Y RESPUESTAS", "La Lucerna", "Página 8　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Texto con huecos", "B", "primo freddo = el primer frío",
     "Lunedì 2 novembre arriva il primo ___ della stagione. (A. caldo · B. freddo)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "A", "El Día de Difuntos es el 2 de noviembre",
     "Il 2 novembre è la Commemorazione dei ___. (A. defunti · B. santi)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "A", "El Forum Cultura abre en Milán",
     "Il Forum Cultura apre martedì a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "A", "La final del Panettone es sábado y domingo",
     "La finale del Panettone è sabato e ___ a Milano. (A. domenica · B. lunedì)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "B", "La Festa del Torrone abre en Cremona",
     "La Festa del Torrone apre a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "B", "La 11.ª jornada termina el domingo 8 de noviembre: chiude",
     "L'undicesima giornata ___ domenica 8 novembre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "A", "Fiorentina–Juventus se juega el domingo por la noche",
     "Fiorentina–Juventus si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "B", "El Festival dei Popoli es en Florencia",
     "Il Festival dei Popoli è a ___. (A. Milano · B. Firenze)", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Una opción", "B", "La primera nieve, hacia los 1.300–1.500 m",
     "La prima neve leggera può cadere intorno ai... A. 500 m · B. 1.300–1.500 m · C. 3.000 m", size=15.5, gap=1)
f.ex("A2", "Una opción", "B", "La flor del 2 de noviembre es el crisantemo",
     "Il fiore del 2 novembre è... A. la rosa · B. il crisantemo · C. il tulipano", size=15.5, gap=1)
f.ex("A2", "Una opción", "A", "En la final del Panettone hay pasteleros de 19 países",
     "Alla finale del Panettone partecipano pasticceri da... A. 19 paesi · B. 5 paesi · C. 50 paesi", size=15.5, gap=1)
f.ex("B1", "Una opción", "B", "El Forum Cultura tiene más de 50 eventos",
     "Il Forum Cultura ha... A. 5 eventi · B. più di 50 eventi · C. 19 eventi", size=15.5, gap=1)
f.ex("B1", "Una opción", "C", "La Feria del Tartufo de Alba cierra el 6 de diciembre",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "Una opción", "A", "El DPB partió hacia Bruselas el 15 de octubre",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "Una opción", "B", "Una probabilidad alta no es una certeza",
     "Una probabilità alta... A. è una certezza · B. non è una certezza · C. è un errore", size=15.5, gap=1)
f.ex("B1", "Una opción", "B", "Lucca Comics se cerró el 1 de noviembre",
     "Lucca Comics si è chiusa... A. il 28 ottobre · B. il 1° novembre · C. l'8 novembre", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Milano: sabato 7 novembre va alla finale del Panettone e assaggia il panettone tradizionale. Paolo vive a Cremona: sabato 7 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano la Serie A: fa freddo, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "Una opción", "B", "Giulia va a la final del Panettone en Milán",
     "Chi va alla finale del Panettone? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Una opción", "A", "Paolo va el sábado a la Festa del Torrone",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Milano · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "Una opción", "B", "El panettone tradicional lo prueba Giulia",
     "Il panettone tradizionale è assaggiato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Una opción", "A", "El mejor título: dos ciudades, dos dulces",
     "Il titolo migliore è... A. «Due città, due dolci» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Formar frases", "Lunedì arriva il primo freddo.", "El tiempo va primero",
     "lunedì / arriva / il primo freddo → ___", instr="Forma la frase", size=15.5, gap=1)
f.ex("B1", "Formar frases", "La finale è a Milano il 7 novembre.", "Sujeto + essere + lugar",
     "la finale / è a Milano / il 7 novembre → ___", instr="Forma la frase", size=15.5, gap=1)
f.ex("B1", "Formar frases", "A che ora apre il Forum Cultura?", "Interrogación primero",
     "a che ora / apre / il Forum Cultura / ? → ___", instr="Forma la frase", size=15.5, gap=1)
f.ex("B1", "Formar frases", "Il freddo arriva lunedì.", "Sujeto + verbo + tiempo",
     "il freddo / arriva / lunedì → ___", instr="Forma la frase", size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "El lunes llega el primer frío.", "Compara con el original",
     "Lunedì arriva il primo freddo. → ___", instr="Traduce", size=15.5, gap=1)
f.ex("B1", "翻译", "El público puede probar gratis.", "assaggiare = probar",
     "Il pubblico può assaggiare gratis. → ___", instr="Traduce", size=15.5, gap=1)
f.ex("B1", "翻译", "El domingo por la noche se juega Fiorentina–Juventus.", "si gioca = se juega",
     "Domenica sera si gioca Fiorentina–Juventus. → ___", instr="Traduce", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni previsione deve essere chiara.", "dovere = deber",
     "Cada previsión debe ser clara. → ___", instr="Traduce", size=15.5, gap=1)
f.head("F　LE PAROLE DEL METEO", 22, OLIVE, 5)
f.match_set("B2", "Emparejar palabras",
            ["la probabilità", "la media", "il bollettino", "il modello"],
            ["il valore medio, tra tanti valori",
             "il documento con le previsioni più recenti",
             "il calcolo che prevede il tempo, come l'ECMWF",
             "quanto è possibile che una cosa succeda"],
            ["d", "a", "b", "c"],
            ["probabilità=posibilidad d", "media=media a", "bollettino=boletín meteorológico b", "modello=modelo de previsión c"],
            instr="Empareja")
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Texto con huecos", "B", "torrone = turrón",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "A", "mandorle = almendras",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "B", "quanto costa? = ¿cuánto cuesta?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "A", "pagare con carta = pagar con tarjeta",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "B", "La fiesta dura hasta el 22 de noviembre",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Lunedì 2 novembre metto il cappotto e la sciarpa: arriva il primo freddo e la mattina è pungente. "
          "A scuola parliamo del Forum Cultura di Milano e del Festival dei Popoli di Firenze. "
          "Sabato assaggio il panettone con la mia famiglia: preferisco quello tradizionale, con i canditi. "
          "Domenica sera guardiamo Fiorentina–Juventus in televisione. "
          "Il freddo è arrivato, ma la settimana è dolce: cultura, dolci e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove del freddo.")
NWORDS = len(MODELO.split())
f.bridge(f"Ejercicio de escritura (sin respuesta única); el modelo ({NWORDS} palabras) está abajo.")
f.ex("B1", "Escritura", "(Tarea abierta, modelo abajo)", f"El modelo está en la sección H ({NWORDS} palabras)",
     "«La tua settimana del primo freddo» Scrivi 80–100 parole: il freddo, cosa metti, un evento o una festa del tuo weekend.", instr="Escribe", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, OLIVE, 2)
p.text(MX, 1382, "RISPOSTE　RESPUESTAS — por página, busca el número del ejercicio", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "Cada respuesta lleva una nota breve　✓ marca el ejercicio de escritura", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.14, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Escritura":
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
