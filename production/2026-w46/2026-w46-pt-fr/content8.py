# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　TEST ET RÉPONSES", "A Lucerna", "PAGE 8　La grande épreuve de la semaine + toutes les réponses")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Texte à trous", "A", "Le jour 2, c’est le 15 novembre",
     "No domingo 15, o Brasil faz ___ do Enem. (A. o segundo dia · B. o primeiro dia)", size=14.5, gap=0)
f.ex("B1", "Texte à trous", "B", "Fermeture à 13h",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Texte à trous", "A", "Fin à 18h30",
     "A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Texte à trous", "A", "La Proclamation de la République, c’est le 15 novembre",
     "A Proclamação da República é no dia ___ de novembro. (A. 15 · B. 20)", size=14.5, gap=0)
f.ex("B1", "Texte à trous", "B", "Le retour Vasco × Palmeiras, c’est le 8",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "Texte à trous", "B", "Le jour 2 compte 90 questions en tout",
     "O dia 15 tem ___ questões. (A. 45 · B. 90)", size=14.5, gap=0)
f.ex("B1", "Texte à trous", "A", "L’épreuve dure 5 heures",
     "No dia 15, a prova dura ___ . (A. cinco horas · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "Texte à trous", "B", "Le jour 1, c’est le 8 novembre",
     "O primeiro dia do Enem foi no dia ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Choix multiple", "B", "Le jour férié tombe un dimanche, pas de récupération le lundi",
     "O feriado de 15 de novembro... A. dá folga na segunda · B. cai num domingo · C. muda o relógio", size=14.5, gap=0)
f.ex("A2", "Choix multiple", "B", "La carte de confirmation appartient à l’Enem",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "Choix multiple", "B", "Le retour Atlético-MG × Grêmio se joue à l’Arena MRV",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "Choix multiple", "B", "La 35e journée n’a qu’un match cette semaine, le 14",
     "A rodada 35 do Brasileirão, nesta semana... A. tem dez jogos · B. só tem Mirassol × Atlético-MG · C. já terminou", size=14.5, gap=0)
f.ex("B1", "Choix multiple", "B", "La Proclamation de la République date de 1889",
     "A Proclamação da República foi em... A. 1822 · B. 1889 · C. 1949", size=14.5, gap=0)
f.ex("A2", "Choix multiple", "B", "Le 11.11, c’est le jour des promos",
     "O 11.11 é... A. um feriado nacional · B. o dia das promoções · C. o dia do Enem", size=14.5, gap=0)
f.ex("B2", "Choix multiple", "A", "300, c’est la durée de l’épreuve en minutes",
     "O número 300 mede... A. os minutos da prova · B. os dias do feriado · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "Choix multiple", "A", "Deodoro a été le premier président",
     "Deodoro da Fonseca foi... A. o primeiro presidente · B. o último imperador · C. um jogador", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No domingo 15, ela faz o segundo dia do Enem. Na segunda, 9, ela revisa Natureza um pouco por dia. Na véspera, ela separa o documento e a caneta preta e dorme cedo. No domingo, ela chega ao local às 11h30, uma hora e meia antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "Choix multiple", "B", "Marina habite à São Paulo",
     "Onde mora Marina? A. no Rio · B. em São Paulo · C. em Belo Horizonte", size=14.5, gap=0)
f.ex("A2", "Choix multiple", "B", "Elle révise un peu de sciences de la nature chaque jour",
     "O que Marina revisa na semana? A. só Matemática · B. Natureza, um pouco por dia · C. nada", size=14.5, gap=0)
f.ex("A2", "Choix multiple", "B", "La veille, elle prépare sa pièce d’identité et son stylo noir et se couche tôt",
     "Na véspera, Marina... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "Choix multiple", "B", "Elle arrive au centre d’examen à 11h30",
     "Marina chega ao local... A. às 13h30 · B. às 11h30 · C. às 18h30", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Former une phrase", "Domingo é dia de prova.", "Le mot de temps est en tête",
     "domingo / é / dia de prova → ___", instr="Forme une phrase", size=14.5, gap=0)
f.ex("B1", "Former une phrase", "A candidata confere o cartão no aplicativo.", "Sujet + verbe + objet + lieu",
     "a candidata / confere / o cartão / no aplicativo → ___", instr="Forme une phrase", size=14.5, gap=0)
f.ex("B1", "Former une phrase", "Que horas termina a prova?", "La phrase interrogative est en tête",
     "que horas / termina / a prova / ? → ___", instr="Forme une phrase", size=14.5, gap=0)
f.ex("B1", "Former une phrase", "O Brasil comemora a Proclamação da República.", "Sujet + verbe + objet",
     "o Brasil / comemora / a proclamação / da república → ___", instr="Forme une phrase", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Traduction", "Dimanche 15 novembre, c’est le deuxième jour de l’Enem.", "Voir le titre de la page 6",
     "Domingo, 15 de novembro, é o segundo dia do Enem. → ___", instr="Traduis", size=14.5, gap=0)
f.ex("B1", "Traduction", "Vérifie la carte avant dimanche.", "Confira = vérifie",
     "Confira o cartão antes do domingo. → ___", instr="Traduis", size=14.5, gap=0)
f.ex("B1", "Traduction", "O feriado cai num domingo.", "feriado = jour férié",
     "« Le jour férié tombe un dimanche. » → ___", instr="Traduis", size=14.5, gap=0)
f.ex("B2", "Traduction", "Quando você chegar, apresente o documento com foto.", "Futur du subjonctif chegar + impératif apresente",
     "Quand tu arrives, montre ta pièce d’identité avec photo. → ___", instr="Traduis", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Associer le vocabulaire",
            ["a proclamação", "o portão", "a república", "a segunda chamada"],
            ["a forma do Estado depois de 1889",
             "o ato de anunciar uma mudança",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["proclamação = annoncer un changement (b)", "portão = l’entrée du centre d’examen (d)", "república = la forme d’État après 1889 (a)", "segunda chamada = réadmission après fermeture (n’existe pas à l’Enem) (c)"],
            instr="Associe les mots")
f.head("G　DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "Texte à trous", "B", "documento com foto = pièce d’identité avec photo",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Texte à trous", "A", "seção = la salle d’examen (le secteur)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Texte à trous", "B", "Fermeture des grilles à 13h",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Texte à trous", "A", "L’épreuve finit à 18h30",
     "— A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Texte à trous", "B", "obrigado = merci",
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
f.bridge(f"Exercice d’écriture (pas de réponse unique) ; le texte modèle ({NWORDS} mots) est ci-dessous.")
f.ex("B1", "Écriture", "(exercice ouvert — texte modèle ci-dessous)", f"Voir le texte modèle dans la partie H de cette page ({NWORDS} mots)",
     "«O seu domingo 15 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="Écris", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　RÉPONSES — classées par page ; trouve ton numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Une courte note par réponse　✓ = l’exercice d’écriture", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Écriture":
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
