# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-pt-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS · TOETS EN ANTWOORDEN", "A Lucerna", "Pagina 8 · A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Gatentekst", "B", "voltar às urnas = gaan stemmen",
     "No domingo, o Brasil volta ___ para o segundo turno. (A. às escolas · B. às urnas)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "4.352 stembureaus met nieuw adres",
     "O TSE mudou o endereço de ___ seções. (A. 4.352 · B. 982)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "het laatste debat is op vrijdag 23",
     "O último debate é na ___, 23 de outubro. (A. sexta-feira · B. terça-feira)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "Vasco is uitgeschakeld",
     "Na Sul-Americana, o Vasco está ___. (A. na final · B. eliminado)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "zoekopdrachten naar gitaar +53% sinds 2021",
     "Desde 2021, as buscas por guitarra já subiram ___. (A. 53% · B. 74%)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "het Enem is in november",
     "As provas do Enem são em ___. (A. outubro · B. novembro)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "wie de meeste stemmen heeft, wint: votos válidos",
     "No segundo turno, vence quem tiver mais ___ válidos. (A. votos · B. debates)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "Brazilië heeft geen zomertijd; de klok blijft staan",
     "No Brasil, o relógio de domingo ___. (A. volta uma hora · B. não muda)", size=14.5, gap=0)
f.head("B · PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Meerkeuze", "B", "stemmen van 8h–17h, tijd van Brasília",
     "A votação de domingo é... A. das 6h às 15h · B. das 8h às 17h, hora de Brasília · C. das 8h às 20h", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "B", "982 in de staat São Paulo",
     "As 982 seções com endereço novo ficam em... A. Minas Gerais · B. São Paulo · C. Bahia", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "A", "debatleider is César Tralli",
     "O mediador do debate da Globo é... A. César Tralli · B. Anderson Daronco · C. Davi Lacerda", size=14.5, gap=0)
f.ex("B1", "Meerkeuze", "C", "Davi Lacerda fluit Grêmio × Atlético-MG",
     "Davi Lacerda apita... A. Palmeiras × Vasco · B. Vasco × Boca · C. Grêmio × Atlético-MG", size=14.5, gap=0)
f.ex("B1", "Meerkeuze", "B", "de Prova do Fazendeiro is op woensdag",
     "A Prova do Fazendeiro é na... A. sexta-feira · B. quarta-feira · C. segunda-feira", size=14.5, gap=0)
f.ex("B1", "Meerkeuze", "A", "de bevestigingskaart is een document van het Enem",
     "O Cartão de Confirmação é um documento... A. do Enem · B. da eleição · C. da Copa do Brasil", size=14.5, gap=0)
f.ex("B2", "Meerkeuze", "B", "+900% is een cijfer over zoekinteresse",
     "O número +900% mede... A. intenção de voto · B. interesse de busca · C. votos válidos", size=14.5, gap=0)
f.ex("B1", "Meerkeuze", "B", "Finados is op 2 november",
     "Finados, feriado nacional, é no dia... A. 31 de outubro · B. 2 de novembro · C. 15 de novembro", size=14.5, gap=0)
f.head("C · LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No primeiro turno, ela votou numa escola perto de casa. Nesta semana, abriu o e-Título e viu uma surpresa: a seção dela é uma das 982 que mudaram de endereço em São Paulo. Domingo, ela acorda cedo, leva o documento com foto e vota na escola nova.", 15.5, lh=1.3, split=False)
f.ex("A2", "Meerkeuze", "B", "Marina woont in São Paulo",
     "Onde mora Marina? A. no Rio de Janeiro · B. em São Paulo · C. na Bahia", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "A", "haar stembureau veranderde van adres",
     "O que mudou para Marina? A. o endereço da seção dela · B. o horário da votação · C. o nome da escola", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "B", "ze zag de verandering in de e-Título",
     "Marina viu a mudança... A. na televisão · B. no aplicativo e-Título · C. no jornal de papel", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "A", "de titel moet de hele tekst samenvatten",
     "O melhor título é... A. «A seção nova de Marina» · B. «O debate final» · C. «A volta da guitarra»", size=14.5, gap=0)
f.head("D · CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Bouw de zin", "Domingo é dia de decisão.", "het tijdwoord staat vooraan",
     "domingo / é / dia de decisão → ___", instr="Bouw de zin", size=14.5, gap=0)
f.ex("B1", "Bouw de zin", "O eleitor confere o local no aplicativo.", "onderwerp + werkwoord + voorwerp + plaats",
     "o eleitor / confere / o local / no aplicativo → ___", instr="Bouw de zin", size=14.5, gap=0)
f.ex("B1", "Bouw de zin", "Que horas começa a votação?", "vraagwoordgroep vooraan",
     "que horas / começa / a votação / ? → ___", instr="Bouw de zin", size=14.5, gap=0)
f.ex("B1", "Bouw de zin", "O Vasco perdeu por 3 a 1.", "onderw. + ww. + uitslag",
     "o Vasco / perdeu / por 3 a 1 → ___", instr="Bouw de zin", size=14.5, gap=0)
f.head("E · TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Vertaal", "Zondag keert Brazilië terug naar de stembus.", "zie kop p. 1",
     "Domingo, o Brasil volta às urnas. → ___", instr="Vertaal", size=14.5, gap=0)
f.ex("B1", "Vertaal", "Controleer je stemlocatie voordat je van huis gaat.", "Confira = controleer",
     "Confira o seu local antes de sair de casa. → ___", instr="Vertaal", size=14.5, gap=0)
f.ex("B1", "Vertaal", "As buscas por guitarra cresceram 53%.", "cresceram = groeiden",
     "De zoekopdrachten naar «guitarra» groeiden met 53%. → ___", instr="Vertaal", size=14.5, gap=0)
f.ex("B2", "Vertaal", "Quando você chegar, confira a seção.", "aanv. wijs toekomst + gebiedende wijs confira",
     "Controleer je stembureau zodra je aankomt. → ___", instr="Vertaal", size=14.5, gap=0)
f.head("F · AS PALAVRAS DA ELEIÇÃO", 22, OLIVE, 5)
f.match_set("B2", "Woorden koppelen",
            ["o segundo turno", "a seção eleitoral", "justificar", "a maioria absoluta"],
            ["explicar por que você não votou",
             "a disputa final entre os dois mais votados",
             "mais da metade dos votos válidos",
             "o lugar exato onde você vota"],
            ["b", "d", "a", "c"],
            ["segundo turno = het beslissingsduel tussen twee b", "seção = de exacte plek van je stem d", "justificar = uitleggen waarom je niet stemde a", "maioria absoluta = > de helft van de geldige stemmen c"],
            instr="Combineer")
f.head("G · DIÁLOGO NO DIA DA VOTAÇÃO", 22, OLIVE, 5)
f.ex("B1", "Gatentekst", "B", "documento com foto = document met foto",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "seção is het concrete stembureau (de zaal)",
     "— A sua ___ é a 042, na sala 3. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "digita = het nummer intypen op de stemmachine",
     "— Agora você ___ o número do candidato. (A. escreve · B. digita)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "de groene toets = confirma (bevestigen)",
     "— Para terminar, você ___ o voto na tecla verde. (A. confirma · B. apaga)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "obrigado = dank je",
     "— Pronto, você já votou. — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H · ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 25 de outubro, acordo cedo e abro o aplicativo e-Título no celular. "
          "Confiro a minha seção: ela mudou de endereço, e a escola nova fica a dez minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e saio às nove. "
          "Na seção, a fila anda rápido: apresento o documento, digito o número do candidato e confirmo o voto. "
          "Depois, almoço com os amigos e assisto aos resultados à noite. "
          "Para mim, o domingo de eleição é um dia de dever — e de festa da democracia.")
NWORDS = len(MODELO.split())
f.expl(f"Uitleg — Schrijfopdracht (geen uniek antwoord); de voorbeeldtekst ({NWORDS} woorden) staat hieronder.")
f.ex("B1", "Schrijven", "(open vraag — voorbeeldtekst hieronder)", f"voorbeeldtekst in deel H ({NWORDS} woorden)",
     "«O seu domingo 25 de outubro» Escreva 80–100 palavras: onde você vota, o que confere antes de sair, e o seu domingo de decisão.", instr="Schrijven", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPOSTAS · ANTWOORDEN — per pagina geordend, zoek het nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "bij elk antwoord een korte uitleg in het Nederlands · ✓ = met voorbeeldtekst", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Pagina {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schrijven":
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
