# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　TEST UND LÖSUNGEN", "A Lucerna", "SEITE 8　A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "A", "Tag 1 ist am 8. November",
     "No domingo 8, o Brasil faz ___ do Enem. (A. o primeiro dia · B. o segundo dia)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "Die Tore schließen um 13 Uhr",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "13:30 Uhr: Beginn",
     "A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "Finados ist am 2. November",
     "Finados é no dia ___ de novembro. (A. 2 · B. 15)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "Rückspiel Vasco × Palmeiras am Sonntag, 8.",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "Der Feriadão dauert 3 Tage",
     "O feriadão tem ___ dias. (A. dois · B. três)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "Die Prüfung am Tag 8 dauert fünfeinhalb Stunden",
     "No dia 8, a prova dura ___ . (A. cinco horas e meia · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "Tag 2 ist am 15. November",
     "O segundo dia do Enem é no dia ___ . (A. 8 · B. 15)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "Feriadão: 31. Oktober bis 2. November",
     "O feriadão vai... A. de 8 a 15 · B. de 31 de outubro a 2 de novembro · C. de 2 a 5", size=14.5, gap=0)
f.ex("A2", "单选", "B", "Die Bestätigungskarte gehört zum Enem",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "单选", "B", "Rückspiel Atlético-MG × Grêmio in der Arena MRV",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "单选", "B", "Die 34. Runde geht von Montag bis Freitag",
     "A rodada 34 do Brasileirão... A. é só no fim de semana · B. vai de segunda a sexta · C. já terminou", size=14.5, gap=0)
f.ex("B1", "单选", "B", "An Finados bringen die Familien Blumen",
     "Em Finados, as famílias levam... A. fogos · B. flores · C. presentes", size=14.5, gap=0)
f.ex("A2", "单选", "B", "Halloween war am Samstag, dem 31. Oktober",
     "Halloween foi... A. no domingo 8 · B. no sábado, 31 de outubro · C. na segunda 2", size=14.5, gap=0)
f.ex("B2", "单选", "A", "330 sind die Minuten der Prüfung",
     "O número 330 mede... A. os minutos da prova · B. os dias do feriadão · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "单选", "A", "Finados heißt auch Dia dos Fiéis Defuntos",
     "Finados, em português, também se chama... A. Dia dos Fiéis Defuntos · B. Dia da Independência · C. Dia do Trabalho", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Lucas mora em Belo Horizonte. No domingo 8, ele faz o Enem pela primeira vez. Na segunda, 2, ele descansa no feriadão e revisa um pouco por dia. Na véspera, ele separa o documento e a caneta preta e dorme cedo. No domingo, ele chega ao local às 11h, duas horas antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Lucas wohnt in Belo Horizonte",
     "Onde mora Lucas? A. no Rio · B. em Belo Horizonte · C. em São Paulo", size=14.5, gap=0)
f.ex("A2", "单选", "B", "Im Feriadão ruht er aus, wiederholt täglich etwas",
     "O que Lucas faz no feriadão? A. só festa · B. descansa e revisa um pouco por dia · C. viaja para a praia", size=14.5, gap=0)
f.ex("A2", "单选", "B", "Am Vorabend: Ausweis und Stift bereit, früh schlafen",
     "Na véspera, Lucas... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "单选", "B", "Er kommt um 11 Uhr am Prüfungsort an",
     "Lucas chega ao local... A. às 13h30 · B. às 11h · C. às 19h", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "造句", "Domingo é dia de prova.", "Zeitangabe zuerst",
     "domingo / é / dia de prova → ___", instr="Sätze bilden", size=14.5, gap=0)
f.ex("B1", "造句", "O candidato confere o cartão no aplicativo.", "S + V + O + Ort",
     "o candidato / confere / o cartão / no aplicativo → ___", instr="Sätze bilden", size=14.5, gap=0)
f.ex("B1", "造句", "Que horas começa a prova?", "Fragewort am Anfang",
     "que horas / começa / a prova / ? → ___", instr="Sätze bilden", size=14.5, gap=0)
f.ex("B1", "造句", "O Brasil lembra os seus mortos.", "Subjekt + Verb + Objekt",
     "o Brasil / lembra / os seus mortos → ___", instr="Sätze bilden", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "翻译", "Sonntag, 8. November ist Tag 1 des Enem.", "vgl. Seite 6",
     "Domingo, 8 de novembro, é o primeiro dia do Enem. → ___", instr="Übersetzen", size=14.5, gap=0)
f.ex("B1", "翻译", "Prüfen Sie die Karte vor dem Sonntag.", "confira = prüfen Sie",
     "Confira o cartão antes do domingo. → ___", instr="Übersetzen", size=14.5, gap=0)
f.ex("B1", "翻译", "O feriadão é de 31 de outubro a 2 de novembro.", "feriadão = langes Feiertagswochenende",
     "„Der Feriadão geht vom 31. Oktober bis zum 2. November.“ → ___", instr="Übersetzen", size=14.5, gap=0)
f.ex("B2", "翻译", "Quando você chegar, apresente o documento com foto.", "Futuro do Subjuntivo chegar + Imperativ apresente",
     "„Wenn Sie ankommen, zeigen Sie bitte Ihren Ausweis mit Foto vor.“ → ___", instr="Übersetzen", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["o feriadão", "o portão", "a reta final", "a segunda chamada"],
            ["a última semana antes da prova",
             "um feriado grudado no fim de semana",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["feriadão = Feiertag am Wochenende: b", "portão = Eingang zum Prüfungsort: d", "reta final = letzte Woche vor der Prüfung: a", "segunda chamada = kein Einlass nach Schluss: c"],
            instr="Zuordnen")
f.head("G　DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "documento com foto = Ausweis mit Foto",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "seção = Prüfungsraum, Sektion",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "Die Tore schließen um 13 Uhr",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "Die Prüfung beginnt um 13:30 Uhr",
     "— A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "obrigado = danke",
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
f.bridge(f"Schreibaufgabe (offen); Mustertext ({NWORDS} Wörter) unten.")
f.ex("B1", "写作", "(offene Aufgabe — Mustertext unten)", f"Mustertext in Bereich H auf dieser Seite ({NWORDS} Wörter)",
     "«O seu domingo 8 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="Schreiben", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　LÖSUNGEN — nach Seiten geordnet, nach Nummer suchen", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Jede Nummer mit kurzer deutscher Erklärung　✓ = Aufgabe mit Mustertext", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "写作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-avaliacao.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
