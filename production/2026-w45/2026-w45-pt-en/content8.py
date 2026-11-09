# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　TEST AND ANSWERS", "A Lucerna", "PAGE 8　The big test of the week + all the answers")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Cloze", "A", "Day 1 is on November 8",
     "No domingo 8, o Brasil faz ___ do Enem. (A. o primeiro dia · B. o segundo dia)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "The gates close at 13h",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "The exam starts at 13:30",
     "A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "Finados is on November 2",
     "Finados é no dia ___ de novembro. (A. 2 · B. 15)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "The Vasco × Palmeiras second leg is on the 8th",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "The long weekend is 3 days",
     "O feriadão tem ___ dias. (A. dois · B. três)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "The day-8 exam lasts five and a half hours",
     "No dia 8, a prova dura ___ . (A. cinco horas e meia · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "Day 2 is on November 15",
     "O segundo dia do Enem é no dia ___ . (A. 8 · B. 15)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Multiple choice", "B", "The long weekend runs October 31 to November 2",
     "O feriadão vai... A. de 8 a 15 · B. de 31 de outubro a 2 de novembro · C. de 2 a 5", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "The confirmation card is an Enem document",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "B", "The Atlético-MG × Grêmio second leg is at Arena MRV",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "B", "Round 34 has games Monday to Friday",
     "A rodada 34 do Brasileirão... A. é só no fim de semana · B. vai de segunda a sexta · C. já terminou", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "B", "On Finados, families bring flowers",
     "Em Finados, as famílias levam... A. fogos · B. flores · C. presentes", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "Halloween was Saturday, October 31",
     "Halloween foi... A. no domingo 8 · B. no sábado, 31 de outubro · C. na segunda 2", size=14.5, gap=0)
f.ex("B2", "Multiple choice", "A", "330 is the exam's length in minutes",
     "O número 330 mede... A. os minutos da prova · B. os dias do feriadão · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "A", "Finados is also called the Day of the Faithful Departed",
     "Finados, em português, também se chama... A. Dia dos Fiéis Defuntos · B. Dia da Independência · C. Dia do Trabalho", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Lucas mora em Belo Horizonte. No domingo 8, ele faz o Enem pela primeira vez. Na segunda, 2, ele descansa no feriadão e revisa um pouco por dia. Na véspera, ele separa o documento e a caneta preta e dorme cedo. No domingo, ele chega ao local às 11h, duas horas antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "Multiple choice", "B", "Lucas lives in Belo Horizonte",
     "Onde mora Lucas? A. no Rio · B. em Belo Horizonte · C. em São Paulo", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "Over the long weekend he rests and revises a little each day",
     "O que Lucas faz no feriadão? A. só festa · B. descansa e revisa um pouco por dia · C. viaja para a praia", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "The night before, he sets out his document and black pen and sleeps early",
     "Na véspera, Lucas... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "He reaches the venue at 11h",
     "Lucas chega ao local... A. às 13h30 · B. às 11h · C. às 19h", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Sentence building", "Domingo é dia de prova.", "The time word comes first",
     "domingo / é / dia de prova → ___", instr="Build the sentence", size=14.5, gap=0)
f.ex("B1", "Sentence building", "O candidato confere o cartão no aplicativo.", "Subject + verb + object + place",
     "o candidato / confere / o cartão / no aplicativo → ___", instr="Build the sentence", size=14.5, gap=0)
f.ex("B1", "Sentence building", "Que horas começa a prova?", "The question phrase comes first",
     "que horas / começa / a prova / ? → ___", instr="Build the sentence", size=14.5, gap=0)
f.ex("B1", "Sentence building", "O Brasil lembra os seus mortos.", "Subject + verb + object",
     "o Brasil / lembra / os seus mortos → ___", instr="Build the sentence", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Translation", "Sunday, November 8, is the first day of the Enem.", "See the page 6 headline",
     "Domingo, 8 de novembro, é o primeiro dia do Enem. → ___", instr="Translate", size=14.5, gap=0)
f.ex("B1", "Translation", "Check your card before Sunday.", "Confira = check, confirm",
     "Confira o cartão antes do domingo. → ___", instr="Translate", size=14.5, gap=0)
f.ex("B1", "Translation", "O feriadão é de 31 de outubro a 2 de novembro.", "feriadão = the long holiday weekend",
     "“The long holiday weekend runs from October 31 to November 2.” → ___", instr="Translate", size=14.5, gap=0)
f.ex("B2", "Translation", "Quando você chegar, apresente o documento com foto.", "future subjunctive chegar + imperative apresente",
     "When you arrive, show your photo ID. → ___", instr="Translate", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Vocabulary matching",
            ["o feriadão", "o portão", "a reta final", "a segunda chamada"],
            ["a última semana antes da prova",
             "um feriado grudado no fim de semana",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["feriadão = a holiday joined to the weekend (b)", "portão = the exam venue entrance (d)", "reta final = the last week before the exam (a)", "segunda chamada = re-entry after closing (there is none in the Enem) (c)"],
            instr="Match the pairs")
f.head("G　DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "Cloze", "B", "documento com foto = photo ID",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "seção = the exam room (section)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "The gates close at 13h",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "The exam starts at 13:30",
     "— A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "obrigado = thank you",
     "— Boa prova! — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H　ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 8 de novembro, acordo cedo e abro o Cartão de Confirmação no celular. "
          "Confiro o meu local: a escola fica a vinte minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e a caneta preta e saio às onze. "
          "Chego antes do meio-dia, entro com calma e guardo o celular desligado. "
          "A prova começa às 13h30: primeiro a redação, depois Linguagens e Humanas. "
          "Escrevo com calma e reviso no fim. "
          "Às 19h, saio cansado e feliz: o primeiro dia acabou, e o segundo vem no domingo 15.")
NWORDS = len(MODELO.split())
f.bridge(f"Writing task (no single correct answer); the model text ({NWORDS} words) is below.")
f.ex("B1", "Writing", "(open task — model text below)", f"See the model text in section H of this page ({NWORDS} words)",
     "«O seu domingo 8 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="Writing", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　ANSWER KEY — grouped by page; find your number", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "One short note per answer　✓ = the writing model", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Writing":
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
