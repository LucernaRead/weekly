# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　TOETS EN ANTWOORDEN", "A Lucerna", "PAGINA 8　De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Gatentekst", "A", "Dag 2 is op 15 november",
     "No domingo 15, o Brasil faz ___ do Enem. (A. o segundo dia · B. o primeiro dia)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "Sluiting om 13 uur",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "Einde om 18:30",
     "A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "De Proclamatie van de Republiek is op 15 november",
     "A Proclamação da República é no dia ___ de novembro. (A. 15 · B. 20)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "De terugwedstrijd Vasco × Palmeiras is op de 8e",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "Dag 2 heeft in totaal 90 vragen",
     "O dia 15 tem ___ questões. (A. 45 · B. 90)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "Het examen duurt 5 uur",
     "No dia 15, a prova dura ___ . (A. cinco horas · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "Dag 1 is op 8 november",
     "O primeiro dia do Enem foi no dia ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Meerkeuze", "B", "De feestdag valt op zondag, maandag geen inhaal",
     "O feriado de 15 de novembro... A. dá folga na segunda · B. cai num domingo · C. muda o relógio", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "B", "De bevestigingskaart hoort bij de Enem",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "Meerkeuze", "B", "De terugwedstrijd Atlético-MG × Grêmio is in de Arena MRV",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "Meerkeuze", "B", "Speelronde 35 heeft deze week maar één wedstrijd, op de 14e",
     "A rodada 35 do Brasileirão, nesta semana... A. tem dez jogos · B. só tem Mirassol × Atlético-MG · C. já terminou", size=14.5, gap=0)
f.ex("B1", "Meerkeuze", "B", "De Proclamatie van de Republiek was in 1889",
     "A Proclamação da República foi em... A. 1822 · B. 1889 · C. 1949", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "B", "11.11 is de dag van de aanbiedingen",
     "O 11.11 é... A. um feriado nacional · B. o dia das promoções · C. o dia do Enem", size=14.5, gap=0)
f.ex("B2", "Meerkeuze", "A", "300 is de examenduur in minuten",
     "O número 300 mede... A. os minutos da prova · B. os dias do feriado · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "Meerkeuze", "A", "Deodoro was de eerste president",
     "Deodoro da Fonseca foi... A. o primeiro presidente · B. o último imperador · C. um jogador", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No domingo 15, ela faz o segundo dia do Enem. Na segunda, 9, ela revisa Natureza um pouco por dia. Na véspera, ela separa o documento e a caneta preta e dorme cedo. No domingo, ela chega ao local às 11h30, uma hora e meia antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "Meerkeuze", "B", "Marina woont in São Paulo",
     "Onde mora Marina? A. no Rio · B. em São Paulo · C. em Belo Horizonte", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "B", "Ze herhaalt elke dag een beetje natuurwetenschappen",
     "O que Marina revisa na semana? A. só Matemática · B. Natureza, um pouco por dia · C. nada", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "B", "De avond ervoor legt ze document en zwarte pen klaar en gaat vroeg slapen",
     "Na véspera, Marina... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "Meerkeuze", "B", "Ze komt om 11:30 aan bij het examencentrum",
     "Marina chega ao local... A. às 13h30 · B. às 11h30 · C. às 18h30", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Zinnen maken", "Domingo é dia de prova.", "Het tijdwoord staat vooraan",
     "domingo / é / dia de prova → ___", instr="Maak een zin", size=14.5, gap=0)
f.ex("B1", "Zinnen maken", "A candidata confere o cartão no aplicativo.", "Onderwerp + werkwoord + lijdend voorwerp + plaats",
     "a candidata / confere / o cartão / no aplicativo → ___", instr="Maak een zin", size=14.5, gap=0)
f.ex("B1", "Zinnen maken", "Que horas termina a prova?", "De vraagzin staat vooraan",
     "que horas / termina / a prova / ? → ___", instr="Maak een zin", size=14.5, gap=0)
f.ex("B1", "Zinnen maken", "O Brasil comemora a Proclamação da República.", "Onderwerp + werkwoord + lijdend voorwerp",
     "o Brasil / comemora / a proclamação / da república → ___", instr="Maak een zin", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Vertaling", "Zondag 15 november is de tweede dag van de Enem.", "Zie de titel van pagina 6",
     "Domingo, 15 de novembro, é o segundo dia do Enem. → ___", instr="Vertaal", size=14.5, gap=0)
f.ex("B1", "Vertaling", "Controleer de kaart vóór zondag.", "Confira = controleer",
     "Confira o cartão antes do domingo. → ___", instr="Vertaal", size=14.5, gap=0)
f.ex("B1", "Vertaling", "O feriado cai num domingo.", "feriado = feestdag",
     "“De feestdag valt op een zondag.” → ___", instr="Vertaal", size=14.5, gap=0)
f.ex("B2", "Vertaling", "Quando você chegar, apresente o documento com foto.", "Futuro van de aanvoegende wijs chegar + gebiedende wijs apresente",
     "Laat bij aankomst je document met foto zien. → ___", instr="Vertaal", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Woordenschat koppelen",
            ["a proclamação", "o portão", "a república", "a segunda chamada"],
            ["a forma do Estado depois de 1889",
             "o ato de anunciar uma mudança",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["proclamação = een verandering aankondigen (b)", "portão = de ingang van het examencentrum (d)", "república = de staatsvorm na 1889 (a)", "segunda chamada = opnieuw binnen na sluiting (bestaat niet bij de Enem) (c)"],
            instr="Koppel")
f.head("G　DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "Gatentekst", "B", "documento com foto = document met foto",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "seção = de examenruimte (de sectie)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "De poorten sluiten om 13 uur",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "A", "Het examen eindigt om 18:30",
     "— A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Gatentekst", "B", "obrigado = dank je",
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
f.bridge(f"Schrijfopdracht (geen enkel juist antwoord); de modeltekst ({NWORDS} woorden) staat hieronder.")
f.ex("B1", "Schrijven", "(open opdracht — modeltekst hieronder)", f"Zie de modeltekst in deel H van deze pagina ({NWORDS} woorden)",
     "«O seu domingo 15 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="Schrijf", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　ANTWOORDEN — per pagina geordend; zoek je nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Een korte toelichting per antwoord　✓ = de schrijfopdracht", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
