# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS · ESERCIZI E RISPOSTE", "A Lucerna", "Pagina 8 · A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Cloze", "A", "Il giorno 1 è l'8 novembre",
     "No domingo 8, o Brasil faz ___ do Enem. (A. o primeiro dia · B. o segundo dia)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "I cancelli chiudono alle 13",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "La prova inizia alle 13:30",
     "A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "Finados è il 2 novembre",
     "Finados é no dia ___ de novembro. (A. 2 · B. 15)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "Il ritorno Vasco × Palmeiras è l'8",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "Il lungo weekend è di 3 giorni",
     "O feriadão tem ___ dias. (A. dois · B. três)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "La prova del giorno 8 dura cinque ore e mezza",
     "No dia 8, a prova dura ___ . (A. cinco horas e meia · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "Il giorno 2 è il 15 novembre",
     "O segundo dia do Enem é no dia ___ . (A. 8 · B. 15)", size=14.5, gap=0)
f.head("B · PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Scelta multipla", "B", "Il lungo weekend va dal 31 ottobre al 2 novembre",
     "O feriadão vai... A. de 8 a 15 · B. de 31 de outubro a 2 de novembro · C. de 2 a 5", size=14.5, gap=0)
f.ex("A2", "Scelta multipla", "B", "La tessera di conferma è un documento dell'Enem",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "Scelta multipla", "B", "Il ritorno Atlético-MG × Grêmio è all'Arena MRV",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "Scelta multipla", "B", "La giornata 34 ha partite dal lunedì al venerdì",
     "A rodada 34 do Brasileirão... A. é só no fim de semana · B. vai de segunda a sexta · C. já terminou", size=14.5, gap=0)
f.ex("B1", "Scelta multipla", "B", "A Finados le famiglie portano fiori",
     "Em Finados, as famílias levam... A. fogos · B. flores · C. presentes", size=14.5, gap=0)
f.ex("A2", "Scelta multipla", "B", "Halloween è stato sabato 31 ottobre",
     "Halloween foi... A. no domingo 8 · B. no sábado, 31 de outubro · C. na segunda 2", size=14.5, gap=0)
f.ex("B2", "Scelta multipla", "A", "330 sono i minuti della prova",
     "O número 330 mede... A. os minutos da prova · B. os dias do feriadão · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "Scelta multipla", "A", "Finados si chiama anche Giorno dei Fedeli Defunti",
     "Finados, em português, também se chama... A. Dia dos Fiéis Defuntos · B. Dia da Independência · C. Dia do Trabalho", size=14.5, gap=0)
f.head("C · LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Lucas mora em Belo Horizonte. No domingo 8, ele faz o Enem pela primeira vez. Na segunda, 2, ele descansa no feriadão e revisa um pouco por dia. Na véspera, ele separa o documento e a caneta preta e dorme cedo. No domingo, ele chega ao local às 11h, duas horas antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "Scelta multipla", "B", "Lucas vive a Belo Horizonte",
     "Onde mora Lucas? A. no Rio · B. em Belo Horizonte · C. em São Paulo", size=14.5, gap=0)
f.ex("A2", "Scelta multipla", "B", "Durante il lungo weekend riposa e ripassa un po' ogni giorno",
     "O que Lucas faz no feriadão? A. só festa · B. descansa e revisa um pouco por dia · C. viaja para a praia", size=14.5, gap=0)
f.ex("A2", "Scelta multipla", "B", "La vigilia prepara il documento e la penna nera e va a letto presto",
     "Na véspera, Lucas... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "Scelta multipla", "B", "Arriva in sede alle 11",
     "Lucas chega ao local... A. às 13h30 · B. às 11h · C. às 19h", size=14.5, gap=0)
f.head("D · CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Forma la frase", "Domingo é dia de prova.", "Prima viene la parola di tempo",
     "domingo / é / dia de prova → ___", instr="Forma la frase", size=14.5, gap=0)
f.ex("B1", "Forma la frase", "O candidato confere o cartão no aplicativo.", "Soggetto + verbo + oggetto + luogo",
     "o candidato / confere / o cartão / no aplicativo → ___", instr="Forma la frase", size=14.5, gap=0)
f.ex("B1", "Forma la frase", "Que horas começa a prova?", "Prima viene la frase interrogativa",
     "que horas / começa / a prova / ? → ___", instr="Forma la frase", size=14.5, gap=0)
f.ex("B1", "Forma la frase", "O Brasil lembra os seus mortos.", "Soggetto + verbo + oggetto",
     "o Brasil / lembra / os seus mortos → ___", instr="Forma la frase", size=14.5, gap=0)
f.head("E · TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Traduzione", "Domenica 8 novembre, è il primo giorno dell'Enem.", "Vedi il titolo di pagina 6",
     "Domingo, 8 de novembro, é o primeiro dia do Enem. → ___", instr="Traduci", size=14.5, gap=0)
f.ex("B1", "Traduzione", "Controlla la tessera prima di domenica.", "Conferir = controllare, verificare",
     "Confira o cartão antes do domingo. → ___", instr="Traduci", size=14.5, gap=0)
f.ex("B1", "Traduzione", "O feriadão é de 31 de outubro a 2 de novembro.", "feriadão = il lungo weekend di festa",
     "“Il lungo weekend va dal 31 ottobre al 2 novembre.” → ___", instr="Traduci", size=14.5, gap=0)
f.ex("B2", "Traduzione", "Quando você chegar, apresente o documento com foto.", "congiuntivo futuro chegar + imperativo apresente",
     "Quando arrivi, mostra il documento con foto. → ___", instr="Traduci", size=14.5, gap=0)
f.head("F · AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Abbinamento lessicale",
            ["o feriadão", "o portão", "a reta final", "a segunda chamada"],
            ["a última semana antes da prova",
             "um feriado grudado no fim de semana",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["feriadão = una festa attaccata al weekend (b)", "portão = l'ingresso della sede d'esame (d)", "reta final = l'ultima settimana prima della prova (a)", "segunda chamada = un nuovo ingresso dopo la chiusura (che non esiste nell'Enem) (c)"],
            instr="Abbina")
f.head("G · DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "Cloze", "B", "documento com foto = documento con foto",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "seção = l'aula d'esame (sezione)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "I cancelli chiudono alle 13",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "La prova inizia alle 13:30",
     "— A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "obrigado = grazie",
     "— Boa prova! — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H · ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 8 de novembro, acordo cedo e abro o Cartão de Confirmação no celular. "
          "Confiro o meu local: a escola fica a vinte minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e a caneta preta e saio às onze. "
          "Chego antes do meio-dia, entro com calma e guardo o celular desligado. "
          "A prova começa às 13h30: primeiro a redação, depois Linguagens e Humanas. "
          "Escrevo com calma e reviso no fim. "
          "Às 19h, saio cansado e feliz: o primeiro dia acabou, e o segundo vem no domingo 15.")
NWORDS = len(MODELO.split())
f.bridge(f"Compito di scrittura (senza un'unica risposta giusta); il testo modello ({NWORDS} parole) è qui sotto.")
f.ex("B1", "Scrivi", "(domanda aperta — testo modello qui sotto)", f"Vedi il testo modello nella sezione H di questa pagina ({NWORDS} parole)",
     "«O seu domingo 8 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="Scrivi", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPOSTAS · RISPOSTE — ordinate per pagina, cerca il numero", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Una breve nota per risposta · ✓ = il testo modello", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Scrivi":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13, lh=1.12, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-avaliacao.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
