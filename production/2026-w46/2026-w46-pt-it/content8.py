# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　PROVA E RISPOSTE", "A Lucerna", "PAGINA 8　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Testo con buchi", "A", "Il giorno 2 è il 15 novembre",
     "No domingo 15, o Brasil faz ___ do Enem. (A. o segundo dia · B. o primeiro dia)", size=14.5, gap=0)
f.ex("B1", "Testo con buchi", "B", "Chiusura alle 13",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Testo con buchi", "A", "Finisce alle 18:30",
     "A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Testo con buchi", "A", "La Proclamazione della Repubblica è il 15 novembre",
     "A Proclamação da República é no dia ___ de novembro. (A. 15 · B. 20)", size=14.5, gap=0)
f.ex("B1", "Testo con buchi", "B", "Il ritorno Vasco × Palmeiras è il giorno 8",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "Testo con buchi", "B", "Il giorno 2 ha 90 domande in tutto",
     "O dia 15 tem ___ questões. (A. 45 · B. 90)", size=14.5, gap=0)
f.ex("B1", "Testo con buchi", "A", "La prova dura 5 ore",
     "No dia 15, a prova dura ___ . (A. cinco horas · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "Testo con buchi", "B", "Il giorno 1 è l’8 novembre",
     "O primeiro dia do Enem foi no dia ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Scelta multipla", "B", "La festa cade di domenica, il lunedì non si recupera",
     "O feriado de 15 de novembro... A. dá folga na segunda · B. cai num domingo · C. muda o relógio", size=14.5, gap=0)
f.ex("A2", "Scelta multipla", "B", "La carta di conferma appartiene all’Enem",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "Scelta multipla", "B", "Il ritorno Atlético-MG × Grêmio è all’Arena MRV",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "Scelta multipla", "B", "La 35ª giornata ha una sola partita questa settimana, il 14",
     "A rodada 35 do Brasileirão, nesta semana... A. tem dez jogos · B. só tem Mirassol × Atlético-MG · C. já terminou", size=14.5, gap=0)
f.ex("B1", "Scelta multipla", "B", "La Proclamazione della Repubblica è del 1889",
     "A Proclamação da República foi em... A. 1822 · B. 1889 · C. 1949", size=14.5, gap=0)
f.ex("A2", "Scelta multipla", "B", "L’11.11 è il giorno delle offerte",
     "O 11.11 é... A. um feriado nacional · B. o dia das promoções · C. o dia do Enem", size=14.5, gap=0)
f.ex("B2", "Scelta multipla", "A", "300 è la durata della prova in minuti",
     "O número 300 mede... A. os minutos da prova · B. os dias do feriado · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "Scelta multipla", "A", "Deodoro è stato il primo presidente",
     "Deodoro da Fonseca foi... A. o primeiro presidente · B. o último imperador · C. um jogador", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No domingo 15, ela faz o segundo dia do Enem. Na segunda, 9, ela revisa Natureza um pouco por dia. Na véspera, ela separa o documento e a caneta preta e dorme cedo. No domingo, ela chega ao local às 11h30, uma hora e meia antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "Scelta multipla", "B", "Marina abita a São Paulo",
     "Onde mora Marina? A. no Rio · B. em São Paulo · C. em Belo Horizonte", size=14.5, gap=0)
f.ex("A2", "Scelta multipla", "B", "Ripassa un po’ di scienze della natura ogni giorno",
     "O que Marina revisa na semana? A. só Matemática · B. Natureza, um pouco por dia · C. nada", size=14.5, gap=0)
f.ex("A2", "Scelta multipla", "B", "La vigilia prepara documento e penna nera e va a letto presto",
     "Na véspera, Marina... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "Scelta multipla", "B", "Arriva al centro d’esame alle 11:30",
     "Marina chega ao local... A. às 13h30 · B. às 11h30 · C. às 18h30", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Formare frasi", "Domingo é dia de prova.", "La parola del tempo sta davanti",
     "domingo / é / dia de prova → ___", instr="Forma una frase", size=14.5, gap=0)
f.ex("B1", "Formare frasi", "A candidata confere o cartão no aplicativo.", "Soggetto + verbo + oggetto + luogo",
     "a candidata / confere / o cartão / no aplicativo → ___", instr="Forma una frase", size=14.5, gap=0)
f.ex("B1", "Formare frasi", "Que horas termina a prova?", "Il gruppo interrogativo sta all’inizio",
     "que horas / termina / a prova / ? → ___", instr="Forma una frase", size=14.5, gap=0)
f.ex("B1", "Formare frasi", "O Brasil comemora a Proclamação da República.", "Soggetto + verbo + oggetto",
     "o Brasil / comemora / a proclamação / da república → ___", instr="Forma una frase", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Traduzione", "Domenica 15 novembre è il secondo giorno dell’Enem.", "Vedi il titolo di pagina 6",
     "Domingo, 15 de novembro, é o segundo dia do Enem. → ___", instr="Traduci", size=14.5, gap=0)
f.ex("B1", "Traduzione", "Controlla la carta prima di domenica.", "Confira = controlla",
     "Confira o cartão antes do domingo. → ___", instr="Traduci", size=14.5, gap=0)
f.ex("B1", "Traduzione", "O feriado cai num domingo.", "feriado = festa",
     "«La festa cade di domenica.» → ___", instr="Traduci", size=14.5, gap=0)
f.ex("B2", "Traduzione", "Quando você chegar, apresente o documento com foto.", "Futuro del congiuntivo chegar + imperativo apresente",
     "Quando arrivi, mostra il documento con foto. → ___", instr="Traduci", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Abbinare il lessico",
            ["a proclamação", "o portão", "a república", "a segunda chamada"],
            ["a forma do Estado depois de 1889",
             "o ato de anunciar uma mudança",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["proclamação = annunciare un cambiamento (b)", "portão = l’ingresso del centro d’esame (d)", "república = la forma di Stato dopo il 1889 (a)", "segunda chamada = rientro dopo la chiusura (non esiste all’Enem) (c)"],
            instr="Abbina")
f.head("G　DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "Testo con buchi", "B", "documento com foto = documento con foto",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Testo con buchi", "A", "seção = l’aula d’esame (il settore)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Testo con buchi", "B", "I cancelli chiudono alle 13",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Testo con buchi", "A", "La prova finisce alle 18:30",
     "— A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Testo con buchi", "B", "obrigado = grazie",
     "— Boa prova! — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H　ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 15 de novembro, acordo cedo e abro o Cartão de Confirmação no celular. "
          "Confiro o meu local: a escola fica a vinte minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e a caneta preta e saio às onze. "
          "Chego antes do meio-dia, entro com calma e guardo o celular desligado. "
          "A prova começa às 13h30: primeiro Natureza, depois Matemática. "
          "Resolvo com calma e reviso no fim. "
          "Às 18h30, saio cansada e feliz: o Enem acabou, e o feriado continua em casa.")
NWORDS = len(MODELO.split())
f.bridge(f"Esercizio di scrittura (senza risposta unica); il testo modello ({NWORDS} parole) è qui sotto.")
f.ex("B1", "Scrittura", "(esercizio aperto — testo modello qui sotto)", f"Vedi il testo modello nella parte H di questa pagina ({NWORDS} parole)",
     "«O seu domingo 15 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="Scrivi", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　RISPOSTE — ordinate per pagina; trova il tuo numero", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Una breve nota per risposta　✓ = l’esercizio di scrittura", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Scrittura":
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
