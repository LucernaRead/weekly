# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-pt-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS · TEST UND ANTWORTEN", "A Lucerna", "SEITE 8 · Die große Prüfung der Woche + alle Antworten")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Lückentext", "A", "Tag 2 ist am 15. November",
     "No domingo 15, o Brasil faz ___ do Enem. (A. o segundo dia · B. o primeiro dia)", size=14.5, gap=0)
f.ex("B1", "Lückentext", "B", "Die Tore schließen um 13 Uhr",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Lückentext", "A", "Ende um 18:30 Uhr",
     "A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Lückentext", "A", "Der Tag der Ausrufung der Republik ist am 15. November",
     "A Proclamação da República é no dia ___ de novembro. (A. 15 · B. 20)", size=14.5, gap=0)
f.ex("B1", "Lückentext", "B", "Das Rückspiel Vasco × Palmeiras ist am 8.",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "Lückentext", "B", "Tag 2 hat insgesamt 90 Fragen",
     "O dia 15 tem ___ questões. (A. 45 · B. 90)", size=14.5, gap=0)
f.ex("B1", "Lückentext", "A", "Die Prüfung dauert 5 Stunden",
     "No dia 15, a prova dura ___ . (A. cinco horas · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "Lückentext", "B", "Tag 1 ist am 8. November",
     "O primeiro dia do Enem foi no dia ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.head("B · PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Multiple Choice", "B", "Der Feiertag fällt auf einen Sonntag, montags gibt es keinen Ausgleich",
     "O feriado de 15 de novembro... A. dá folga na segunda · B. cai num domingo · C. muda o relógio", size=14.5, gap=0)
f.ex("A2", "Multiple Choice", "B", "Die Bestätigungskarte gehört zum Enem",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "Multiple Choice", "B", "Das Rückspiel Atlético-MG × Grêmio ist in der Arena MRV",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "Multiple Choice", "B", "Der 35. Spieltag hat diese Woche nur ein Spiel, am 14.",
     "A rodada 35 do Brasileirão, nesta semana... A. tem dez jogos · B. só tem Mirassol × Atlético-MG · C. já terminou", size=14.5, gap=0)
f.ex("B1", "Multiple Choice", "B", "Die Ausrufung der Republik war 1889",
     "A Proclamação da República foi em... A. 1822 · B. 1889 · C. 1949", size=14.5, gap=0)
f.ex("A2", "Multiple Choice", "B", "Der 11.11. ist der Tag der Aktionen",
     "O 11.11 é... A. um feriado nacional · B. o dia das promoções · C. o dia do Enem", size=14.5, gap=0)
f.ex("B2", "Multiple Choice", "A", "300 ist die Prüfungsdauer in Minuten",
     "O número 300 mede... A. os minutos da prova · B. os dias do feriado · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "Multiple Choice", "A", "Deodoro war der erste Präsident",
     "Deodoro da Fonseca foi... A. o primeiro presidente · B. o último imperador · C. um jogador", size=14.5, gap=0)
f.head("C · LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No domingo 15, ela faz o segundo dia do Enem. Na segunda, 9, ela revisa Natureza um pouco por dia. Na véspera, ela separa o documento e a caneta preta e dorme cedo. No domingo, ela chega ao local às 11h30, uma hora e meia antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "Multiple Choice", "B", "Marina wohnt in São Paulo",
     "Onde mora Marina? A. no Rio · B. em São Paulo · C. em Belo Horizonte", size=14.5, gap=0)
f.ex("A2", "Multiple Choice", "B", "Sie wiederholt jeden Tag ein bisschen Naturwissenschaften",
     "O que Marina revisa na semana? A. só Matemática · B. Natureza, um pouco por dia · C. nada", size=14.5, gap=0)
f.ex("A2", "Multiple Choice", "B", "Am Vorabend legt sie Ausweis und schwarzen Stift bereit und geht früh schlafen",
     "Na véspera, Marina... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "Multiple Choice", "B", "Sie kommt um 11:30 Uhr am Prüfungsort an",
     "Marina chega ao local... A. às 13h30 · B. às 11h30 · C. às 18h30", size=14.5, gap=0)
f.head("D · CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Satzbau", "Domingo é dia de prova.", "Das Zeitwort steht vorn",
     "domingo / é / dia de prova → ___", instr="Satz bilden", size=14.5, gap=0)
f.ex("B1", "Satzbau", "A candidata confere o cartão no aplicativo.", "Subjekt + Verb + Objekt + Ort",
     "a candidata / confere / o cartão / no aplicativo → ___", instr="Satz bilden", size=14.5, gap=0)
f.ex("B1", "Satzbau", "Que horas termina a prova?", "Die Fragephrase steht am Satzanfang",
     "que horas / termina / a prova / ? → ___", instr="Satz bilden", size=14.5, gap=0)
f.ex("B1", "Satzbau", "O Brasil comemora a Proclamação da República.", "Subjekt + Verb + Objekt",
     "o Brasil / comemora / a proclamação / da república → ___", instr="Satz bilden", size=14.5, gap=0)
f.head("E · TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Übersetzung", "Sonntag, der 15. November, ist der zweite Tag des Enem.", "Siehe die Überschrift auf Seite 6",
     "Domingo, 15 de novembro, é o segundo dia do Enem. → ___", instr="Übersetzen", size=14.5, gap=0)
f.ex("B1", "Übersetzung", "Prüfe die Karte vor Sonntag.", "Confira = prüfen, bestätigen",
     "Confira o cartão antes do domingo. → ___", instr="Übersetzen", size=14.5, gap=0)
f.ex("B1", "Übersetzung", "O feriado cai num domingo.", "feriado = Feiertag",
     "„Der Feiertag fällt auf einen Sonntag.“ → ___", instr="Übersetzen", size=14.5, gap=0)
f.ex("B2", "Übersetzung", "Quando você chegar, apresente o documento com foto.", "Futur des Konjunktivs chegar + Imperativ apresente",
     "Wenn du ankommst, zeig bitte deinen Ausweis mit Foto. → ___", instr="Übersetzen", size=14.5, gap=0)
f.head("F · AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Wortschatz zuordnen",
            ["a proclamação", "o portão", "a república", "a segunda chamada"],
            ["a forma do Estado depois de 1889",
             "o ato de anunciar uma mudança",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["proclamação = eine Veränderung ankündigen (b)", "portão = der Eingang zum Prüfungsort (d)", "república = die Staatsform nach 1889 (a)", "segunda chamada = Wiedereinlass nach Schließung (gibt es beim Enem nicht) (c)"],
            instr="Paare zuordnen")
f.head("G · DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "Lückentext", "B", "documento com foto = Ausweis mit Foto",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Lückentext", "A", "seção = der Prüfungsraum (Abschnitt)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Lückentext", "B", "Die Tore schließen um 13 Uhr",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Lückentext", "A", "Die Prüfung endet um 18:30 Uhr",
     "— A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Lückentext", "B", "obrigado = danke",
     "— Boa prova! — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H · ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 15 de novembro, acordo cedo e abro o Cartão de Confirmação no celular. "
          "Confiro o meu local: a escola fica a vinte minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e a caneta preta e saio às onze. "
          "Chego antes do meio-dia, entro com calma e guardo o celular desligado. "
          "A prova começa às 13h30: primeiro Natureza, depois Matemática. "
          "Resolvo com calma e reviso no fim. "
          "Às 18h30, saio cansada e feliz: o Enem acabou, e o feriado continua em casa.")
NWORDS = len(MODELO.split())
f.bridge(f"Schreibaufgabe (keine einzige richtige Antwort); der Mustertext ({NWORDS} Wörter) steht unten.")
f.ex("B1", "Schreiben", "(offene Aufgabe — Mustertext unten)", f"Siehe den Mustertext in Abschnitt H dieser Seite ({NWORDS} Wörter)",
     "«O seu domingo 15 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="Schreiben", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPOSTAS · LÖSUNGEN — nach Seiten geordnet; such deine Nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Eine kurze Notiz pro Antwort · ✓ = die Schreibaufgabe", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schreiben":
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
