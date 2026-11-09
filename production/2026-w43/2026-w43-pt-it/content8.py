# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　ESERCIZI E RISPOSTE", "A Lucerna", "Pagina 8　A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "voltar às urnas = tornare a votare",
     "No domingo, o Brasil volta ___ para o segundo turno. (A. às escolas · B. às urnas)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "4.352 seggi hanno cambiato indirizzo",
     "O TSE mudou o endereço de ___ seções. (A. 4.352 · B. 982)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "l'ultimo dibattito è venerdì 23",
     "O último debate é na ___, 23 de outubro. (A. sexta-feira · B. terça-feira)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "il Vasco è eliminato",
     "Na Sul-Americana, o Vasco está ___. (A. na final · B. eliminado)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "le ricerche di chitarra: +53% dal 2021",
     "Desde 2021, as buscas por guitarra já subiram ___. (A. 53% · B. 74%)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "le prove dell'Enem sono in novembre",
     "As provas do Enem são em ___. (A. outubro · B. novembro)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "vince chi ha più voti validi: votos válidos",
     "No segundo turno, vence quem tiver mais ___ válidos. (A. votos · B. debates)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "niente ora legale in Brasile: l'orologio non cambia",
     "No Brasil, o relógio de domingo ___. (A. volta uma hora · B. não muda)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "voto dalle 8h alle 17h, ora di Brasília",
     "A votação de domingo é... A. das 6h às 15h · B. das 8h às 17h, hora de Brasília · C. das 8h às 20h", size=14.5, gap=0)
f.ex("A2", "单选", "B", "le 982 sono nello Stato di São Paulo",
     "As 982 seções com endereço novo ficam em... A. Minas Gerais · B. São Paulo · C. Bahia", size=14.5, gap=0)
f.ex("A2", "单选", "A", "il moderatore del dibattito è César Tralli",
     "O mediador do debate da Globo é... A. César Tralli · B. Anderson Daronco · C. Davi Lacerda", size=14.5, gap=0)
f.ex("B1", "单选", "C", "Davi Lacerda arbitra Grêmio × Atlético-MG",
     "Davi Lacerda apita... A. Palmeiras × Vasco · B. Vasco × Boca · C. Grêmio × Atlético-MG", size=14.5, gap=0)
f.ex("B1", "单选", "B", "la Prova do Fazendeiro è il mercoledì",
     "A Prova do Fazendeiro é na... A. sexta-feira · B. quarta-feira · C. segunda-feira", size=14.5, gap=0)
f.ex("B1", "单选", "A", "la scheda di conferma è un documento dell'Enem",
     "O Cartão de Confirmação é um documento... A. do Enem · B. da eleição · C. da Copa do Brasil", size=14.5, gap=0)
f.ex("B2", "单选", "B", "+900% = interesse di ricerca",
     "O número +900% mede... A. intenção de voto · B. interesse de busca · C. votos válidos", size=14.5, gap=0)
f.ex("B1", "单选", "B", "Finados è il 2 novembre",
     "Finados, feriado nacional, é no dia... A. 31 de outubro · B. 2 de novembro · C. 15 de novembro", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No primeiro turno, ela votou numa escola perto de casa. Nesta semana, abriu o e-Título e viu uma surpresa: a seção dela é uma das 982 que mudaram de endereço em São Paulo. Domingo, ela acorda cedo, leva o documento com foto e vota na escola nova.", 15.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Marina abita a São Paulo",
     "Onde mora Marina? A. no Rio de Janeiro · B. em São Paulo · C. na Bahia", size=14.5, gap=0)
f.ex("A2", "单选", "A", "il suo seggio ha cambiato indirizzo",
     "O que mudou para Marina? A. o endereço da seção dela · B. o horário da votação · C. o nome da escola", size=14.5, gap=0)
f.ex("A2", "单选", "B", "ha visto il cambiamento nell'app e-Título",
     "Marina viu a mudança... A. na televisão · B. no aplicativo e-Título · C. no jornal de papel", size=14.5, gap=0)
f.ex("A2", "单选", "A", "il titolo deve riassumere tutto il testo",
     "O melhor título é... A. «A seção nova de Marina» · B. «O debate final» · C. «A volta da guitarra»", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "造句", "Domingo é dia de decisão.", "la parola di tempo davanti",
     "domingo / é / dia de decisão → ___", instr="Forma la frase", size=14.5, gap=0)
f.ex("B1", "造句", "O eleitor confere o local no aplicativo.", "soggetto + verbo + oggetto + luogo",
     "o eleitor / confere / o local / no aplicativo → ___", instr="Forma la frase", size=14.5, gap=0)
f.ex("B1", "造句", "Que horas começa a votação?", "l'interrogativo all'inizio",
     "que horas / começa / a votação / ? → ___", instr="Forma la frase", size=14.5, gap=0)
f.ex("B1", "造句", "O Vasco perdeu por 3 a 1.", "soggetto + verbo + risultato",
     "o Vasco / perdeu / por 3 a 1 → ___", instr="Forma la frase", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "翻译", "Domenica, il Brasile torna alle urne.", "(titolo di pagina 1)",
     "Domingo, o Brasil volta às urnas. → ___", instr="Traduci", size=14.5, gap=0)
f.ex("B1", "翻译", "Controlla il tuo seggio prima di uscire di casa.", "Confira = controlla",
     "Confira o seu local antes de sair de casa. → ___", instr="Traduci", size=14.5, gap=0)
f.ex("B1", "翻译", "As buscas por guitarra cresceram 53%.", "cresceram = sono cresciute",
     "Le ricerche di «guitarra» sono aumentate del 53%. → ___", instr="Traduci", size=14.5, gap=0)
f.ex("B2", "翻译", "Quando você chegar, confira a seção.", "futuro del congiuntivo (chegar) + imperativo confira",
     "Quando arriverai, controlla il tuo seggio. → ___", instr="Traduci", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA ELEIÇÃO", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["o segundo turno", "a seção eleitoral", "justificar", "a maioria absoluta"],
            ["explicar por que você não votou",
             "a disputa final entre os dois mais votados",
             "mais da metade dos votos válidos",
             "o lugar exato onde você vota"],
            ["b", "d", "a", "c"],
            ["segundo turno = la sfida finale tra i due più votati: b", "seção = il luogo esatto dove voti: d", "justificar = spiegare perché non hai votato: a", "maioria absoluta = più della metà dei voti validi: c"],
            instr="Abbina")
f.head("G　DIÁLOGO NO DIA DA VOTAÇÃO", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "documento com foto = un documento con foto",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "seção = il seggio concreto (la sala)",
     "— A sua ___ é a 042, na sala 3. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "sull'urna elettronica, digita = digita il numero",
     "— Agora você ___ o número do candidato. (A. escreve · B. digita)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "il tasto verde = conferma (confirma)",
     "— Para terminar, você ___ o voto na tecla verde. (A. confirma · B. apaga)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "obrigado = grazie",
     "— Pronto, você já votou. — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H　ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 25 de outubro, acordo cedo e abro o aplicativo e-Título no celular. "
          "Confiro a minha seção: ela mudou de endereço, e a escola nova fica a dez minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e saio às nove. "
          "Na seção, a fila anda rápido: apresento o documento, digito o número do candidato e confirmo o voto. "
          "Depois, almoço com os amigos e assisto aos resultados à noite. "
          "Para mim, o domingo de eleição é um dia de dever — e de festa da democracia.")
NWORDS = len(MODELO.split())
f.expl(f"Esercizio di scrittura (senza risposta unica); il testo modello ({NWORDS} parole) è qui sotto.")
f.ex("B1", "写作", "(domanda aperta — testo modello qui sotto)", f"Testo modello nella sezione H di questa pagina ({NWORDS} parole)",
     "«O seu domingo 25 de outubro» Escreva 80–100 palavras: onde você vota, o que confere antes de sair, e o seu domingo de decisão.", instr="Scrivi", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　RISPOSTE — ordinate per pagina, cerca il numero", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Una breve nota in italiano per ogni risposta　✓ = esercizio con testo modello", 19.5, "sans", False, GREY, anchor="end")
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
