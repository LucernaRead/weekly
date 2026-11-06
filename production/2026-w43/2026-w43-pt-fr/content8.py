# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-pt-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS · EXERCICES ET RÉPONSES", "A Lucerna", "Page 8 · A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "voltar às urnas = retourner voter",
     "No domingo, o Brasil volta ___ para o segundo turno. (A. às escolas · B. às urnas)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "4.352 bureaux de vote ont changé d'adresse",
     "O TSE mudou o endereço de ___ seções. (A. 4.352 · B. 982)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "le dernier débat a lieu le vendredi 23",
     "O último debate é na ___, 23 de outubro. (A. sexta-feira · B. terça-feira)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "Vasco est éliminé",
     "Na Sul-Americana, o Vasco está ___. (A. na final · B. eliminado)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "les recherches de guitare : +53 % depuis 2021",
     "Desde 2021, as buscas por guitarra já subiram ___. (A. 53% · B. 74%)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "les épreuves de l'Enem sont en novembre",
     "As provas do Enem são em ___. (A. outubro · B. novembro)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "le plus de suffrages exprimés gagne : votos válidos",
     "No segundo turno, vence quem tiver mais ___ válidos. (A. votos · B. debates)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "pas d'heure d'été au Brésil : l'horloge ne change pas",
     "No Brasil, o relógio de domingo ___. (A. volta uma hora · B. não muda)", size=14.5, gap=0)
f.head("B · PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "vote de 8h à 17h, heure de Brasília",
     "A votação de domingo é... A. das 6h às 15h · B. das 8h às 17h, hora de Brasília · C. das 8h às 20h", size=14.5, gap=0)
f.ex("A2", "单选", "B", "les 982 sont dans l'État de São Paulo",
     "As 982 seções com endereço novo ficam em... A. Minas Gerais · B. São Paulo · C. Bahia", size=14.5, gap=0)
f.ex("A2", "单选", "A", "le médiateur du débat est César Tralli",
     "O mediador do debate da Globo é... A. César Tralli · B. Anderson Daronco · C. Davi Lacerda", size=14.5, gap=0)
f.ex("B1", "单选", "C", "Davi Lacerda arbitre Grêmio × Atlético-MG",
     "Davi Lacerda apita... A. Palmeiras × Vasco · B. Vasco × Boca · C. Grêmio × Atlético-MG", size=14.5, gap=0)
f.ex("B1", "单选", "B", "la Prova do Fazendeiro a lieu le mercredi",
     "A Prova do Fazendeiro é na... A. sexta-feira · B. quarta-feira · C. segunda-feira", size=14.5, gap=0)
f.ex("B1", "单选", "A", "la carte de confirmation est un document de l'Enem",
     "O Cartão de Confirmação é um documento... A. do Enem · B. da eleição · C. da Copa do Brasil", size=14.5, gap=0)
f.ex("B2", "单选", "B", "+900 % = l'intérêt de recherche",
     "O número +900% mede... A. intenção de voto · B. interesse de busca · C. votos válidos", size=14.5, gap=0)
f.ex("B1", "单选", "B", "Finados tombe le 2 novembre",
     "Finados, feriado nacional, é no dia... A. 31 de outubro · B. 2 de novembro · C. 15 de novembro", size=14.5, gap=0)
f.head("C · LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No primeiro turno, ela votou numa escola perto de casa. Nesta semana, abriu o e-Título e viu uma surpresa: a seção dela é uma das 982 que mudaram de endereço em São Paulo. Domingo, ela acorda cedo, leva o documento com foto e vota na escola nova.", 15.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Marina habite à São Paulo",
     "Onde mora Marina? A. no Rio de Janeiro · B. em São Paulo · C. na Bahia", size=14.5, gap=0)
f.ex("A2", "单选", "A", "son bureau de vote a changé d'adresse",
     "O que mudou para Marina? A. o endereço da seção dela · B. o horário da votação · C. o nome da escola", size=14.5, gap=0)
f.ex("A2", "单选", "B", "elle a vu le changement dans l'application e-Título",
     "Marina viu a mudança... A. na televisão · B. no aplicativo e-Título · C. no jornal de papel", size=14.5, gap=0)
f.ex("A2", "单选", "A", "le titre doit résumer tout le texte",
     "O melhor título é... A. «A seção nova de Marina» · B. «O debate final» · C. «A volta da guitarra»", size=14.5, gap=0)
f.head("D · CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "造句", "Domingo é dia de decisão.", "le mot de temps en premier",
     "domingo / é / dia de decisão → ___", instr="Former une phrase", size=14.5, gap=0)
f.ex("B1", "造句", "O eleitor confere o local no aplicativo.", "sujet + verbe + complément + lieu",
     "o eleitor / confere / o local / no aplicativo → ___", instr="Former une phrase", size=14.5, gap=0)
f.ex("B1", "造句", "Que horas começa a votação?", "l'interrogatif en tête",
     "que horas / começa / a votação / ? → ___", instr="Former une phrase", size=14.5, gap=0)
f.ex("B1", "造句", "O Vasco perdeu por 3 a 1.", "sujet + verbe + score",
     "o Vasco / perdeu / por 3 a 1 → ___", instr="Former une phrase", size=14.5, gap=0)
f.head("E · TRADUZA", 22, OLIVE, 5)
f.ex("A2", "翻译", "Dimanche, le Brésil retourne aux urnes.", "(titre page 1)",
     "Domingo, o Brasil volta às urnas. → ___", instr="Traduire", size=14.5, gap=0)
f.ex("B1", "翻译", "Vérifiez votre bureau de vote avant de partir de chez vous.", "Confira = vérifiez",
     "Confira o seu local antes de sair de casa. → ___", instr="Traduire", size=14.5, gap=0)
f.ex("B1", "翻译", "As buscas por guitarra cresceram 53%.", "cresceram = en hausse",
     "Les recherches de « guitarra » ont augmenté de 53 %. → ___", instr="Traduire", size=14.5, gap=0)
f.ex("B2", "翻译", "Quando você chegar, confira a seção.", "futur du subjonctif (chegar) + impératif confira",
     "Quand vous arriverez, vérifiez votre bureau de vote. → ___", instr="Traduire", size=14.5, gap=0)
f.head("F · AS PALAVRAS DA ELEIÇÃO", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["o segundo turno", "a seção eleitoral", "justificar", "a maioria absoluta"],
            ["explicar por que você não votou",
             "a disputa final entre os dois mais votados",
             "mais da metade dos votos válidos",
             "o lugar exato onde você vota"],
            ["b", "d", "a", "c"],
            ["segundo turno = le duel final des deux premiers : b", "seção = l'endroit exact du vote : d", "justificar = expliquer pourquoi vous n'avez pas voté : a", "maioria absoluta = plus de la moitié des suffrages : c"],
            instr="Associer")
f.head("G · DIÁLOGO NO DIA DA VOTAÇÃO", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "documento com foto = un document avec photo",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "seção = le bureau concret (la salle)",
     "— A sua ___ é a 042, na sala 3. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "sur l'urne, digita = taper le numéro",
     "— Agora você ___ o número do candidato. (A. escreve · B. digita)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "la touche verte = confirma (confirmer)",
     "— Para terminar, você ___ o voto na tecla verde. (A. confirma · B. apaga)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "obrigado = merci",
     "— Pronto, você já votou. — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H · ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 25 de outubro, acordo cedo e abro o aplicativo e-Título no celular. "
          "Confiro a minha seção: ela mudou de endereço, e a escola nova fica a dez minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e saio às nove. "
          "Na seção, a fila anda rápido: apresento o documento, digito o número do candidato e confirmo o voto. "
          "Depois, almoço com os amigos e assisto aos resultados à noite. "
          "Para mim, o domingo de eleição é um dia de dever — e de festa da democracia.")
NWORDS = len(MODELO.split())
f.expl(f"Exercice d'écriture (sans réponse unique) ; le texte modèle ({NWORDS} mots) est ci-dessous.")
f.ex("B1", "写作", "Question ouverte — texte modèle ci-dessous sur cette page", f"Texte modèle dans la section H de cette page ({NWORDS} mots)",
     "«O seu domingo 25 de outubro» Escreva 80–100 palavras: onde você vota, o que confere antes de sair, e o seu domingo de decisão.", instr="Écrire", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPOSTAS · RÉPONSES — classées par page, cherchez le numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Une courte note en français pour chaque réponse · ✓ = exercice avec texte modèle", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
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
