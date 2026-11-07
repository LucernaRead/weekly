# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-pt-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS · TEST AND ANSWERS", "A Lucerna", "PAGE 8 · The big test of the week + all the answers")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Cloze", "B", "voltar às urnas = to go to the polls",
     "No domingo, o Brasil volta ___ para o segundo turno. (A. às escolas · B. às urnas)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "4.352 polling stations changed address",
     "O TSE mudou o endereço de ___ seções. (A. 4.352 · B. 982)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "The last debate is on Friday the 23rd",
     "O último debate é na ___, 23 de outubro. (A. sexta-feira · B. terça-feira)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "Vasco are eliminated",
     "Na Sul-Americana, o Vasco está ___. (A. na final · B. eliminado)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "Guitar searches are up 53% since 2021",
     "Desde 2021, as buscas por guitarra já subiram ___. (A. 53% · B. 74%)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "The Enem exams are in November",
     "As provas do Enem são em ___. (A. outubro · B. novembro)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "Most valid votes wins: votos válidos",
     "No segundo turno, vence quem tiver mais ___ válidos. (A. votos · B. debates)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "No daylight saving in Brazil; clocks stay put",
     "No Brasil, o relógio de domingo ___. (A. volta uma hora · B. não muda)", size=14.5, gap=0)
f.head("B · PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Multiple choice", "B", "Voting 8h–17h, Brasília time",
     "A votação de domingo é... A. das 6h às 15h · B. das 8h às 17h, hora de Brasília · C. das 8h às 20h", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "The 982 are in São Paulo state",
     "As 982 seções com endereço novo ficam em... A. Minas Gerais · B. São Paulo · C. Bahia", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "A", "The debate host is César Tralli",
     "O mediador do debate da Globo é... A. César Tralli · B. Anderson Daronco · C. Davi Lacerda", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "C", "Davi Lacerda referees Grêmio × Atlético-MG",
     "Davi Lacerda apita... A. Palmeiras × Vasco · B. Vasco × Boca · C. Grêmio × Atlético-MG", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "B", "The Prova do Fazendeiro is on Wednesday",
     "A Prova do Fazendeiro é na... A. sexta-feira · B. quarta-feira · C. segunda-feira", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "A", "The confirmation card is an Enem document",
     "O Cartão de Confirmação é um documento... A. do Enem · B. da eleição · C. da Copa do Brasil", size=14.5, gap=0)
f.ex("B2", "Multiple choice", "B", "+900% is search-interest data",
     "O número +900% mede... A. intenção de voto · B. interesse de busca · C. votos válidos", size=14.5, gap=0)
f.ex("B1", "Multiple choice", "B", "Finados is on November 2",
     "Finados, feriado nacional, é no dia... A. 31 de outubro · B. 2 de novembro · C. 15 de novembro", size=14.5, gap=0)
f.head("C · LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No primeiro turno, ela votou numa escola perto de casa. Nesta semana, abriu o e-Título e viu uma surpresa: a seção dela é uma das 982 que mudaram de endereço em São Paulo. Domingo, ela acorda cedo, leva o documento com foto e vota na escola nova.", 15.5, lh=1.3, split=False)
f.ex("A2", "Multiple choice", "B", "Marina lives in São Paulo",
     "Onde mora Marina? A. no Rio de Janeiro · B. em São Paulo · C. na Bahia", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "A", "Her polling station changed address",
     "O que mudou para Marina? A. o endereço da seção dela · B. o horário da votação · C. o nome da escola", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "B", "She saw the change in the e-Título",
     "Marina viu a mudança... A. na televisão · B. no aplicativo e-Título · C. no jornal de papel", size=14.5, gap=0)
f.ex("A2", "Multiple choice", "A", "The title must sum up the whole text",
     "O melhor título é... A. «A seção nova de Marina» · B. «O debate final» · C. «A volta da guitarra»", size=14.5, gap=0)
f.head("D · CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Sentence building", "Domingo é dia de decisão.", "The time word comes first",
     "domingo / é / dia de decisão → ___", instr="Build the sentence", size=14.5, gap=0)
f.ex("B1", "Sentence building", "O eleitor confere o local no aplicativo.", "S + V + O + place",
     "o eleitor / confere / o local / no aplicativo → ___", instr="Build the sentence", size=14.5, gap=0)
f.ex("B1", "Sentence building", "Que horas começa a votação?", "Question phrase first",
     "que horas / começa / a votação / ? → ___", instr="Build the sentence", size=14.5, gap=0)
f.ex("B1", "Sentence building", "O Vasco perdeu por 3 a 1.", "Subject + verb + score",
     "o Vasco / perdeu / por 3 a 1 → ___", instr="Build the sentence", size=14.5, gap=0)
f.head("E · TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Translation", "On Sunday, Brazil goes back to the polls.", "See page 1",
     "Domingo, o Brasil volta às urnas. → ___", instr="Translate", size=14.5, gap=0)
f.ex("B1", "Translation", "Check your polling place before you leave home.", "Confira = please check, make sure",
     "Confira o seu local antes de sair de casa. → ___", instr="Translate", size=14.5, gap=0)
f.ex("B1", "Translation", "As buscas por guitarra cresceram 53%.", "cresceram = grew",
     "Searches for “guitar” grew by 53%. → ___", instr="Translate", size=14.5, gap=0)
f.ex("B2", "Translation", "Quando você chegar, confira a seção.", "Fut. subj. + imper.",
     "When you arrive, check your polling station. → ___", instr="Translate", size=14.5, gap=0)
f.head("F · AS PALAVRAS DA ELEIÇÃO", 22, OLIVE, 5)
f.match_set("B2", "Vocabulary matching",
            ["o segundo turno", "a seção eleitoral", "justificar", "a maioria absoluta"],
            ["explicar por que você não votou",
             "a disputa final entre os dois mais votados",
             "mais da metade dos votos válidos",
             "o lugar exato onde você vota"],
            ["b", "d", "a", "c"],
            ["segundo turno = the final of the top two (b)", "seção = the exact place where you vote (d)", "justificar = to explain why you did not vote (a)", "maioria absoluta = more than half of the valid votes (c)"],
            instr="Match the pairs")
f.head("G · DIÁLOGO NO DIA DA VOTAÇÃO", 22, OLIVE, 5)
f.ex("B1", "Cloze", "B", "documento com foto = a photo document",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "seção is the exact polling place (room)",
     "— A sua ___ é a 042, na sala 3. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "On the voting machine you digita (type the number)",
     "— Agora você ___ o número do candidato. (A. escreve · B. digita)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "The green key = confirma (confirm)",
     "— Para terminar, você ___ o voto na tecla verde. (A. confirma · B. apaga)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "obrigado = thank you",
     "— Pronto, você já votou. — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H · ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 25 de outubro, acordo cedo e abro o aplicativo e-Título no celular. "
          "Confiro a minha seção: ela mudou de endereço, e a escola nova fica a dez minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e saio às nove. "
          "Na seção, a fila anda rápido: apresento o documento, digito o número do candidato e confirmo o voto. "
          "Depois, almoço com os amigos e assisto aos resultados à noite. "
          "Para mim, o domingo de eleição é um dia de dever — e de festa da democracia.")
NWORDS = len(MODELO.split())
f.bridge(f"Writing task (no single correct answer); the model text ({NWORDS} words) is below.")
f.ex("B1", "Writing", "(open task — model text below)", f"See the model text in section H of this page ({NWORDS} words)",
     "«O seu domingo 25 de outubro» Escreva 80–100 palavras: onde você vota, o que confere antes de sair, e o seu domingo de decisão.", instr="Writing", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPOSTAS · ANSWER KEY — grouped by page; find your number", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "One short note per answer · ✓ = the writing model", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2606, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.21, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Writing":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 14, lh=1.21, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-avaliacao.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
