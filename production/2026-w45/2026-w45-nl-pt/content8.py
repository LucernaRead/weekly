# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN　Teste e respostas", "De Lucerna", "Página 8　De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "cloze choice", "B", "A Semana do Clima vai até 8 de novembro",
     "De Klimaatweek duurt van 2 tot en met ___ november. (A. 7 · B. 8)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "Coevorden distribui 200 árvores e arbustos",
     "Coevorden deelt ___ bomen en struiken uit. (A. 100 · B. 200)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "A Noite dos Museus é em 7 de novembro",
     "Museumnacht is op zaterdag ___ november. (A. 6 · B. 7)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "Twente–Ajax começa às 13h30",
     "Twente – Ajax begint om ___ uur. (A. 11:15 · B. 13:30)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "O Ajax venceu o Atalanta por 2–0",
     "Ajax won van Atalanta met ___. (A. 2–0 · B. 4–1)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "O Robinson começou em novembro",
     "Expeditie Robinson begon op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "Código laranja: o tempo é perigoso",
     "Code oranje betekent: het weer is ___. (A. veilig · B. gevaarlijk)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "meedoen = participar",
     "«Meedoen» betekent ___. (A. weggaan · B. deelnemen)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "choice", "A", "A Semana do Clima começa na segunda-feira, 2 de novembro",
     "De Klimaatweek begint op... A. maandag 2 november · B. dinsdag 3 november · C. zaterdag 7 november", size=13.8, gap=0)
f.ex("A2", "choice", "B", "O local da distribuição é Zweeloo",
     "De bomen in Coevorden worden uitgedeeld in... A. Amsterdam · B. Zweeloo · C. Rotterdam", size=13.8, gap=0)
f.ex("A2", "choice", "B", "O Crossing Border é em Haia",
     "Crossing Border is in... A. Amsterdam · B. Den Haag · C. Utrecht", size=13.8, gap=0)
f.ex("B1", "choice", "A", "O PAN é no RAI",
     "PAN Amsterdam is in... A. de RAI · B. het Rijksmuseum · C. de Jaarbeurs", size=13.8, gap=0)
f.ex("B1", "choice", "B", "O Real Betis venceu o Feyenoord por 1–0",
     "Real Betis – Feyenoord eindigde... A. 0–0 · B. 1–0 · C. 0–1", size=13.8, gap=0)
f.ex("B1", "choice", "B", "Após 10 rodadas, o Ajax tem 21 pontos",
     "Na 10 ronden heeft Ajax ___ punten. A. 24 · B. 21 · C. 20", size=13.8, gap=0)
f.ex("B2", "choice", "B", "Fadiga de avisos: avisos demais, por isso as pessoas deixam de prestar atenção",
     "Waarschuwingsmoeheid betekent... A. moe van het weer · B. minder opletten door te veel waarschuwingen · C. een nieuwe code", size=13.8, gap=0)
f.ex("B1", "choice", "C", "A feira de Zaandam tem cerca de 250 barracas",
     "De Snuffelmarkt in Zaandam heeft zo'n ___ kramen. A. 70 · B. 200 · C. 250", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Coevorden. Op zaterdag 7 november gaat hij naar de Fair Groen in Zweeloo en haalt hij een gratis struik op. 's Avonds kijkt hij naar de foto's van Museumnacht in Amsterdam — zelf gaat hij niet, want zondag speelt zijn club Twente tegen Ajax om 13:30 uur. En in de Klimaatweek fietst Daan elke dag naar school, ook als het regent.", 15, lh=1.3, split=False)
f.ex("A2", "choice", "B", "Daan mora em Coevorden",
     "Waar woont Daan? A. in Zweeloo · B. in Coevorden · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "choice", "B", "No sábado ele pega um arbusto grátis",
     "Wat haalt Daan op zaterdag op? A. een fiets · B. een gratis struik · C. een kaartje", size=13.8, gap=0)
f.ex("A2", "choice", "B", "No domingo o Twente joga contra o Ajax",
     "Waarom gaat Daan zaterdagavond niet naar Amsterdam? A. Hij heeft geen kaartje · B. Zondag speelt Twente tegen Ajax · C. Hij houdt niet van musea", size=13.8, gap=0)
f.ex("B1", "choice", "B", "Na Semana do Clima ele vai de bicicleta para a escola todos os dias",
     "Wat doet Daan in de Klimaatweek? A. Hij rijdt elke dag met de auto · B. Hij fietst elke dag naar school · C. Hij blijft thuis", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "make sentences", "De Klimaatweek begint op maandag.", "Sujeito + verbo + tempo",
     "de klimaatweek / begint / op maandag → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("B1", "make sentences", "Wij planten een boom in de tuin.", "Sujeito + verbo + objeto + lugar",
     "wij / planten / een boom / in de tuin → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("B1", "make sentences", "Twente speelt zondag tegen Ajax.", "Sujeito + verbo + tempo + adversário",
     "twente / speelt / zondag / tegen ajax → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("B1", "make sentences", "Ik doe mee aan de Klimaatweek.", "Verbo separável: mee vai por último",
     "ik / doe / mee / aan de klimaatweek → ___", instr="Forme a frase", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "translate", "A Semana do Clima dura sete dias.", "Compare com o título da página 1",
     "De Klimaatweek duurt zeven dagen. → ___", instr="Traduza para o português", size=13.8, gap=0)
f.ex("B1", "translate", "Código laranja significa: prepare-se.", "Da página 2 · bereid je voor = prepare-se",
     "Code oranje betekent: bereid je voor. → ___", instr="Traduza para o português", size=13.8, gap=0)
f.ex("B1", "translate", "Museumnacht duurt van 19:00 uur tot 02:00 uur.", "Atenção à expressão de tempo van...tot...",
     "A Museumnacht dura das 19h00 às 2h00. → ___", instr="Traduza para o neerlandês", size=13.8, gap=0)
f.ex("B2", "translate", "Ik doe mee aan de Klimaatweek.", "meedoen é um verbo separável",
     "Participo na Semana do Clima. → ___", instr="Traduza para o neerlandês", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "matching",
            ["het klimaat", "meedoen", "de waarschuwing", "vastzetten"],
            ["een bericht over gevaarlijk weer",
             "deelnemen, erbij zijn",
             "het weer en de natuur over een lange tijd",
             "losse spullen stevig maken"],
            ["c", "b", "a", "d"],
            ["klimaat = clima c", "meedoen = participar b", "waarschuwing = aviso a", "vastzetten = prender d"],
            instr="Palavra e significado")
f.head("G　DIALOOG BIJ DE BOMEN", 21, OLIVE, 5)
f.ex("B1", "cloze choice", "A", "boom = árvore",
     "— Goedemiddag! Ik kom voor een ___. (A. boom · B. fiets)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "struik = arbusto",
     "— Natuurlijk. Wilt u een boom of een ___? (A. struik · B. auto)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "planten = plantar",
     "— Een struik, graag. En waar moet ik hem ___? (A. planten · B. kopen)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "zachte = macia (solo)",
     "— In de tuin, in de ___ grond. (A. harde · B. zachte)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "A distribuição vai até as 16h00",
     "— De uitdeling duurt tot ___ uur. (A. 16:00 · B. 20:00)", size=13.8, gap=0)
f.head("H　SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Maandag 2 november begint de Klimaatweek in Nederland. "
          "Ik doe mee: ik fiets elke dag naar school en ik zet de verwarming één graad lager. "
          "Op zaterdag 7 november ga ik met mijn vader naar Coevorden, want daar deelt de gemeente gratis bomen uit. "
          "Wij nemen een struik mee voor onze tuin. "
          "'s Avonds kijken wij op televisie naar de foto's van Museumnacht in Amsterdam. "
          "Zondag kijken wij naar Twente tegen Ajax. "
          "Mijn zus plant ook een boom op haar balkon. "
          "Wat een week voor het klimaat!")
NWORDS = len(MODELO.split())
f.bridge(f"Tarefa de escrita (sem resposta única); modelo ({NWORDS} palavras) abaixo.")
f.ex("B1", "writing", "(tarefa aberta — modelo abaixo)", f"Ver o modelo na seção H ({NWORDS} palavras)",
     "«Jouw week in de Klimaatweek» Schrijf 80–100 woorden: wat doe jij in de Klimaatweek, plant jij iets, fiets jij, en kijk jij naar Museumnacht of voetbal?", instr="Escreva", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　Respostas — por página: procure o número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Nota em português em cada resposta　✓ = com modelo", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 13.5, "sans", True, OLIVE, lh=1.17, gap=1.5, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "writing":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.0, lh=1.14, gap=0.3, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-toets.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
