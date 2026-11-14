# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band('VALUTAZIONE E RISPOSTE · AVALIAÇÃO E RESPOSTAS', "La Lucerna", 'Página 8 · La grande prova della settimana + tutte le risposte')

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", 'Cloze', "B", 'tornare indietro = voltar atrás',
     "Domenica l'orologio torna ___ di un'ora. (A. avanti · B. indietro)", size=15.5, gap=1)
f.ex("B1", 'Cloze', "A", 'a noite da mudança de hora tem 25 horas',
     "La notte tra sabato e domenica dura ___ ore. (A. 25 · B. 23)", size=15.5, gap=1)
f.ex("B1", 'Cloze', "A", 'incontrare = enfrentar, jogar contra',
     "Alle 12:30 l'Inter ___ la Fiorentina a San Siro. (A. incontra · B. visita)", size=15.5, gap=1)
f.ex("B1", 'Cloze', "A", 'Napoli–Roma é no sábado',
     "Napoli–Roma si gioca ___ alle 18:00. (A. sabato · B. domenica)", size=15.5, gap=1)
f.ex("B1", 'Cloze', "A", 'em Montaione é a festa da trufa',
     "A Montaione è la festa del ___. (A. tartufo · B. cinema)", size=15.5, gap=1)
f.ex("B1", 'Cloze', "B", 'o festival fecha no domingo: chiude',
     "La Festa del Cinema di Roma ___ domenica 25. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", 'Cloze', "A", 'Lucca abre em 28 de outubro: apre',
     "Lucca Comics ___ il 28 ottobre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", 'Cloze', "B", '28 de outubro é quarta-feira',
     "Il voto sulla manovra è atteso per ___ 28 ottobre. (A. lunedì · B. mercoledì)", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", 'Escolha múltipla', "B", 'às 03:00 volta para as 02:00',
     "Il cambio dell'ora: alle 03:00 → ... A. 04:00 · B. 02:00 · C. 01:00", size=15.5, gap=1)
f.ex("A2", 'Escolha múltipla', "B", '«meteo oggi» é a busca número um',
     "«Meteo oggi» è... A. un film · B. la ricerca numero uno · C. una festa", size=15.5, gap=1)
f.ex("A2", 'Escolha múltipla', "A", 'a tempestade se chama Adam',
     "La tempesta della settimana si chiama... A. Adam · B. Legacy · C. Bagòss", size=15.5, gap=1)
f.ex("B1", 'Escolha múltipla', "B", 'a feira da trufa branca é em Alba',
     "La Fiera del Tartufo Bianco è a... A. Volterra · B. Alba · C. Bagolino", size=15.5, gap=1)
f.ex("B1", 'Escolha múltipla', "C", 'a mostra de Artemisia é em Florença',
     "La mostra su Artemisia è a... A. Roma · B. Lucca · C. Firenze", size=15.5, gap=1)
f.ex("B1", 'Escolha múltipla', "A", 'o DPB foi enviado em 15 de outubro',
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", 'Escolha múltipla', "B", 'os números do DPB são previsões',
     "Le cifre del DPB sono... A. risultati · B. previsioni · C. voti", size=15.5, gap=1)
f.ex("B1", 'Escolha múltipla', "B", 'Todos os Santos este ano é domingo, 1º de novembro',
     "Ognissanti, quest'anno, è... A. lunedì 2 novembre · B. domenica 1° novembre · C. sabato 31 ottobre", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Lucca: mercoledì 28 ottobre va a Lucca Comics con il suo cosplay. Paolo vive a Roma: domenica 25 va all'Auditorium per l'ultimo giorno della Festa del Cinema. Sabato, Giulia e Paolo dormono un'ora in più: domenica comincia l'ora solare.", 16.5, lh=1.3, split=False)
f.ex("A2", 'Escolha múltipla', "B", 'Giulia vai à Lucca Comics',
     "Chi va a Lucca Comics? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", 'Escolha múltipla', "A", 'Paolo vai domingo ao festival de cinema',
     "Paolo, domenica, va... A. alla Festa del Cinema · B. a Lucca · C. a una sagra", size=15.5, gap=1)
f.ex("A2", 'Escolha múltipla', "B", 'o cosplay é de Giulia',
     "Il cosplay è di... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", 'Escolha múltipla', "A", 'o título resume duas cidades e duas festas',
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", 'Formar frases', "Domenica dormiamo un'ora in più.", 'o tempo vem primeiro',
     "domenica / dormiamo / un'ora in più → ___", instr='Forme a frase', size=15.5, gap=1)
f.ex("B1", 'Formar frases', "La fiera è iniziata il 10 ottobre.", 'sujeito + essere + particípio',
     "la fiera / è iniziata / il 10 ottobre → ___", instr='Forme a frase', size=15.5, gap=1)
f.ex("B1", 'Formar frases', "A che ora comincia la partita?", 'a pergunta vai no início',
     "a che ora / comincia / la partita / ? → ___", instr='Forme a frase', size=15.5, gap=1)
f.ex("B1", 'Formar frases', "Il voto slitta a mercoledì.", 'sujeito + verbo + complemento',
     "il voto / slitta / a mercoledì → ___", instr='Forme a frase', size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", 'Tradução', 'No domingo dormimos uma hora a mais.', 'da página 1',
     "Domenica dormiamo un'ora in più. → ___", instr='Traduza', size=15.5, gap=1)
f.ex("B1", 'Tradução', 'A exposição continua aberta até abril.', 'resta aperta = fica aberta',
     "La mostra resta aperta fino ad aprile. → ___", instr='Traduza', size=15.5, gap=1)
f.ex("B1", 'Tradução', "Sabato alle 18:00 si gioca Napoli–Roma.", 'si gioca = joga-se',
     'Sábado às 18:00, Napoli contra Roma. → ___', instr='Traduza', size=15.5, gap=1)
f.ex("B2", 'Tradução', "Ogni cifra deve avere una fonte.", 'dovere = dever, precisar',
     'Cada número precisa ter uma fonte. → ___', instr='Traduza', size=15.5, gap=1)
f.head("F　LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", 'Combinar',
            ["la manovra", "il rinvio", "il miliardo", "la previsione"],
            ["un numero che descrive il futuro",
             "la legge di bilancio dello Stato",
             "quando una cosa arriva più tardi del previsto",
             "mille milioni"],
            ["b", "c", "d", "a"],
            ['manovra = a lei do orçamento: b', 'rinvio = chega mais tarde do que o previsto: c', 'miliardo = um bilhão: d', 'previsione = um número que descreve o futuro: a'],
            instr='Combine')
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", 'Cloze', "B", 'tartufo = a trufa',
     "— Cerco il ___ bianco famoso. (A. biglietto · B. tartufo)", size=15.5, gap=1)
f.ex("B1", 'Cloze', "A", 'castagne arrosto = castanhas assadas',
     "— Vuole anche le castagne ___? (A. arrosto · B. mute)", size=15.5, gap=1)
f.ex("B1", 'Cloze', "B", 'quanto costa? = quanto custa?',
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", 'Cloze', "A", 'pagare con carta = pagar com cartão',
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", 'Cloze', "B", 'a festa dura até domingo',
     "— La sagra è in piazza fino a ___. (A. aprile · B. domenica)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 25 ottobre mi sveglio tardi: nella notte l'orologio è tornato indietro e ho dormito un'ora in più. "
          "Sabato sera ho cambiato gli orologi di casa: quello del forno e quello vecchio in cucina. "
          "Faccio colazione con calma e vado al mercato con mia sorella. A pranzo guardiamo Inter–Fiorentina: "
          "è la prima partita con l'ora solare. Nel pomeriggio leggo un libro e preparo la settimana. "
          "La sera è già buio presto, ma non mi dispiace: l'autunno è la mia stagione preferita, "
          "con le sagre, il tartufo e le castagne calde.")
NWORDS = len(MODELO.split())
f.expl(f"Exercício de escrita (sem resposta única); o texto modelo ({NWORDS} palavras) está logo abaixo.")
f.ex("B1", 'Escrita', '(pergunta aberta — texto modelo abaixo)', f"O modelo está na seção H desta página ({NWORDS} palavras)",
     "«La tua domenica 25 ottobre» Scrivi 80–100 parole: il cambio dell'ora, cosa fai con l'ora in più, una partita o una festa del tuo weekend.", instr='Escreva', size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, 'RISPOSTE · RESPOSTAS — organizadas por página: busque pelo número do exercício', 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, 'Uma nota breve em português para cada exercício · ✓ = exercício de escrita', 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} ({e_['note']})"
        if e_["type"] == 'Escrita':
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
