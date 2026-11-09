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
f.ex("B1", "Cloze", "A", "Day 2 is on November 15",
     "No domingo 15, o Brasil faz ___ do Enem. (A. o segundo dia · B. o primeiro dia)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "The gates close at 13h",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "ends at 18:30",
     "A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "The Proclamation of the Republic is on November 15",
     "A Proclamação da República é no dia ___ de novembro. (A. 15 · B. 20)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "The Vasco × Palmeiras second leg is on the 8th",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "Day 2 has 90 questions in total",
     "O dia 15 tem ___ questões. (A. 45 · B. 90)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "The exam lasts 5 hours",
     "No dia 15, a prova dura ___ . (A. cinco horas · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "Day 1 is on November 8",
     "O primeiro dia do Enem foi no dia ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Multiple choice", "B", "The holiday falls on a Sunday, with no Monday off",
     "O feriado de 15 de novembro... A. dá folga na segunda · B. cai num domingo · C. muda o relógio", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "The confirmation card is an Enem document",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "B", "The Atlético-MG × Grêmio second leg is at Arena MRV",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "B", "Round 35 has only one game this week, on the 14th",
     "A rodada 35 do Brasileirão, nesta semana... A. tem dez jogos · B. só tem Mirassol × Atlético-MG · C. já terminou", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "B", "The Proclamation of the Republic was in 1889",
     "A Proclamação da República foi em... A. 1822 · B. 1889 · C. 1949", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "11.11 is the day of promotions",
     "O 11.11 é... A. um feriado nacional · B. o dia das promoções · C. o dia do Enem", size=14.5, gap=0)
f.ex("B2", "Multiple choice", "A", "300 is the exam length in minutes",
     "O número 300 mede... A. os minutos da prova · B. os dias do feriado · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "A", "Deodoro was the first president",
     "Deodoro da Fonseca foi... A. o primeiro presidente · B. o último imperador · C. um jogador", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No domingo 15, ela faz o segundo dia do Enem. Na segunda, 9, ela revisa Natureza um pouco por dia. Na véspera, ela separa o documento e a caneta preta e dorme cedo. No domingo, ela chega ao local às 11h30, uma hora e meia antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "Multiple choice", "B", "Marina lives in São Paulo",
     "Onde mora Marina? A. no Rio · B. em São Paulo · C. em Belo Horizonte", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "She revises a little natural science each day",
     "O que Marina revisa na semana? A. só Matemática · B. Natureza, um pouco por dia · C. nada", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "The night before, she sets out her document and black pen and sleeps early",
     "Na véspera, Marina... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "She reaches the venue at 11:30",
     "Marina chega ao local... A. às 13h30 · B. às 11h30 · C. às 18h30", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Sentence building", "Domingo é dia de prova.", "The time word comes first",
     "domingo / é / dia de prova → ___", instr="Build the sentence", size=14.5, gap=0)
f.ex("B1", "Sentence building", "A candidata confere o cartão no aplicativo.", "Subject + verb + object + place",
     "a candidata / confere / o cartão / no aplicativo → ___", instr="Build the sentence", size=14.5, gap=0)
f.ex("B1", "Sentence building", "Que horas termina a prova?", "The question phrase comes first",
     "que horas / termina / a prova / ? → ___", instr="Build the sentence", size=14.5, gap=0)
f.ex("B1", "Sentence building", "O Brasil comemora a Proclamação da República.", "Subject + verb + object",
     "o Brasil / comemora / a proclamação / da república → ___", instr="Build the sentence", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Translation", "Sunday, November 15, is the second day of the Enem.", "See the page 6 headline",
     "Domingo, 15 de novembro, é o segundo dia do Enem. → ___", instr="Translate", size=14.5, gap=0)
f.ex("B1", "Translation", "Check your card before Sunday.", "Confira = check, confirm",
     "Confira o cartão antes do domingo. → ___", instr="Translate", size=14.5, gap=0)
f.ex("B1", "Translation", "O feriado cai num domingo.", "feriado = holiday",
     "“The holiday falls on a Sunday.” → ___", instr="Translate", size=14.5, gap=0)
f.ex("B2", "Translation", "Quando você chegar, apresente o documento com foto.", "future subjunctive chegar + imperative apresente",
     "When you arrive, show your photo ID. → ___", instr="Translate", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Vocabulary matching",
            ["a proclamação", "o portão", "a república", "a segunda chamada"],
            ["a forma do Estado depois de 1889",
             "o ato de anunciar uma mudança",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["proclamação = announcing a change (b)", "portão = the exam venue entrance (d)", "república = the form of the State after 1889 (a)", "segunda chamada = re-entry after closing (there is none in the Enem) (c)"],
            instr="Match the pairs")
f.head("G　DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "Cloze", "B", "documento com foto = photo ID",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "seção = the exam room (section)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "The gates close at 13h",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "The exam ends at 18:30",
     "— A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "obrigado = thank you",
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
f.bridge(f"Writing task (no single correct answer); the model text ({NWORDS} words) is below.")
f.ex("B1", "Writing", "(open task — model text below)", f"See the model text in section H of this page ({NWORDS} words)",
     "«O seu domingo 15 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="Writing", size=14.5, gap=0)
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
