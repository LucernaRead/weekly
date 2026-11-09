# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　TOETS EN ANTWOORDEN", "A Lucerna", "Pagina 8　A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Gatentekst", "A", "Dag 1 is op 8 november",
     "No domingo 8, o Brasil faz ___ do Enem. (A. o primeiro dia · B. o segundo dia)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "De poorten sluiten om 13h",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "Het examen begint om 13:30",
     "A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "Finados is op 2 november",
     "Finados é no dia ___ de novembro. (A. 2 · B. 15)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "De return Vasco × Palmeiras is op 8 november",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "Het lange weekend duurt 3 dagen",
     "O feriadão tem ___ dias. (A. dois · B. três)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "Het examen van dag 8 duurt vijf en een half uur",
     "No dia 8, a prova dura ___ . (A. cinco horas e meia · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "Dag 2 is op 15 november",
     "O segundo dia do Enem é no dia ___ . (A. 8 · B. 15)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Meerkeuze", "B", "Het lange weekend loopt van 31 oktober tot 2 november",
     "O feriadão vai... A. de 8 a 15 · B. de 31 de outubro a 2 de novembro · C. de 2 a 5", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "B", "De bevestigingskaart is een document van het Enem",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "Meerkeuze", "B", "De return Atlético-MG × Grêmio is in de Arena MRV",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "Meerkeuze", "B", "Speelronde 34 heeft van maandag tot vrijdag wedstrijden",
     "A rodada 34 do Brasileirão... A. é só no fim de semana · B. vai de segunda a sexta · C. já terminou", size=14.5, gap=0)
f.ex("B1", "Meerkeuze", "B", "Op Finados brengen families bloemen mee",
     "Em Finados, as famílias levam... A. fogos · B. flores · C. presentes", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "B", "Halloween was op zaterdag 31 oktober",
     "Halloween foi... A. no domingo 8 · B. no sábado, 31 de outubro · C. na segunda 2", size=14.5, gap=0)
f.ex("B2", "Meerkeuze", "A", "330 is de duur van het examen in minuten",
     "O número 330 mede... A. os minutos da prova · B. os dias do feriadão · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "Meerkeuze", "A", "Finados heet ook de Dag van de Gelovige Zielen",
     "Finados, em português, também se chama... A. Dia dos Fiéis Defuntos · B. Dia da Independência · C. Dia do Trabalho", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Lucas mora em Belo Horizonte. No domingo 8, ele faz o Enem pela primeira vez. Na segunda, 2, ele descansa no feriadão e revisa um pouco por dia. Na véspera, ele separa o documento e a caneta preta e dorme cedo. No domingo, ele chega ao local às 11h, duas horas antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "Meerkeuze", "B", "Lucas woont in Belo Horizonte",
     "Onde mora Lucas? A. no Rio · B. em Belo Horizonte · C. em São Paulo", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "B", "In het lange weekend rust hij uit en herhaalt hij elke dag een beetje",
     "O que Lucas faz no feriadão? A. só festa · B. descansa e revisa um pouco por dia · C. viaja para a praia", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "B", "De avond ervoor legt hij document en zwarte pen klaar en gaat hij vroeg slapen",
     "Na véspera, Lucas... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "B", "Hij komt om 11h aan op de examenlocatie",
     "Lucas chega ao local... A. às 13h30 · B. às 11h · C. às 19h", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Bouw de zin", "Domingo é dia de prova.", "Het tijdwoord staat vooraan",
     "domingo / é / dia de prova → ___", instr="Bouw de zin", size=14.5, gap=0)
f.ex("B1", "Bouw de zin", "O candidato confere o cartão no aplicativo.", "Onderwerp + werkwoord + voorwerp + plaats",
     "o candidato / confere / o cartão / no aplicativo → ___", instr="Bouw de zin", size=14.5, gap=0)
f.ex("B1", "Bouw de zin", "Que horas começa a prova?", "De vraagwoordgroep staat vooraan",
     "que horas / começa / a prova / ? → ___", instr="Bouw de zin", size=14.5, gap=0)
f.ex("B1", "Bouw de zin", "O Brasil lembra os seus mortos.", "Onderwerp + werkwoord + voorwerp",
     "o Brasil / lembra / os seus mortos → ___", instr="Bouw de zin", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Vertaal", "Zondag 8 november is de eerste dag van het Enem.", "zie de kop van pagina 6",
     "Domingo, 8 de novembro, é o primeiro dia do Enem. → ___", instr="Vertaal", size=14.5, gap=0)
f.ex("B1", "Vertaal", "Controleer je kaart vóór zondag.", "Confira = controleer",
     "Confira o cartão antes do domingo. → ___", instr="Vertaal", size=14.5, gap=0)
f.ex("B1", "Vertaal", "O feriadão é de 31 de outubro a 2 de novembro.", "feriadão = het lange weekend",
     "“Het lange weekend loopt van 31 oktober tot 2 november.” → ___", instr="Vertaal", size=14.5, gap=0)
f.ex("B2", "Vertaal", "Quando você chegar, apresente o documento com foto.", "aanvoegende wijs toekomst chegar + gebiedende wijs apresente",
     "Als je aankomt, toon dan je document met foto. → ___", instr="Vertaal", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Woorden koppelen",
            ["o feriadão", "o portão", "a reta final", "a segunda chamada"],
            ["a última semana antes da prova",
             "um feriado grudado no fim de semana",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["feriadão = een feestdag vast aan het weekend (b)", "portão = de ingang van de examenlocatie (d)", "reta final = de laatste week vóór het examen (a)", "segunda chamada = opnieuw binnenkomen na sluiting (bij het Enem onmogelijk) (c)"],
            instr="Combineer")
f.head("G　DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "Gatentekst", "B", "documento com foto = document met foto",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "seção = de examenzaal (de sectie)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "De poorten sluiten om 13h",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "Het examen begint om 13:30",
     "— A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "obrigado = dank je",
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
f.expl(f"Uitleg — Schrijfopdracht (geen uniek antwoord); de voorbeeldtekst ({NWORDS} woorden) staat hieronder.")
f.ex("B1", "Schrijven", "(open vraag — voorbeeldtekst hieronder)", f"voorbeeldtekst in deel H ({NWORDS} woorden)",
     "«O seu domingo 8 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="Schrijven", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　ANTWOORDEN — per pagina geordend, zoek het nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "bij elk antwoord een korte uitleg in het Nederlands　✓ = met voorbeeldtekst", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Pagina {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schrijven":
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
