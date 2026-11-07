# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-nl-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · TESTE E RESPOSTAS", "De Lucerna", "Página 8 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "cloze choice", "B", "As notícias do Sinterklaas começam a 9 de novembro",
     "Het Sinterklaasjournaal begint op 9 ___. (A. oktober · B. november)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "A chegada nacional é em Grave",
     "De landelijke intocht is in ___. (A. Amsterdam · B. Grave)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "A chegada a Amesterdão é a 88.ª edição",
     "De intocht in Amsterdam is de ___ editie. (A. 26e · B. 88e)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "Países Baixos–Grécia, pontapé inicial às 20:45",
     "Oranje – Griekenland begint om ___ uur. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "O São Martinho é a 11 de novembro",
     "Sint-Maarten is op 11 ___. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "O Robinson passa na RTL 4",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "O São Martinho é a festa da partilha",
     "Sint-Maarten is het feest van het ___. (A. griezelen · B. delen)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "schoen zetten = pôr o sapato",
     "«De schoen zetten» betekent ___. (A. schoenen kopen · B. je schoen neerzetten)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "choice", "A", "As notícias do Sinterklaas passam todos os dias às 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "choice", "B", "Grave fica no rio Maas",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "choice", "B", "O Sinterklaas recebe a chave da cidade no Museu Marítimo",
     "In Amsterdam krijgt Sinterklaas de sleutel bij... A. de Stopera · B. het Scheepvaartmuseum · C. het Leidseplein", size=13.8, gap=0)
f.ex("B1", "choice", "A", "Het diner foi publicado em 2009",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "choice", "B", "Os Países Baixos e a Grécia têm ambos 8 pontos",
     "Na vier wedstrijden hebben Nederland en Griekenland ___ punten. A. 5 · B. 8 · C. 0", size=13.8, gap=0)
f.ex("B1", "choice", "B", "Alemanha–Países Baixos, segunda-feira, em Berlim",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=13.8, gap=0)
f.ex("B2", "choice", "B", "Uma tradição vive quando as pessoas continuam a celebrá-la",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "choice", "C", "O Pakjesavond é no sábado, 5 de dezembro",
     "Pakjesavond is op... A. 11 november · B. 14 november · C. 5 december", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht. Op woensdag 11 november loopt zij met een lampion mee in de Sint Maarten Parade en zingt zij bij elke deur. Elke dag kijkt zij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag kijkt zij op televisie naar de intocht in Grave. Zondag zet zij haar schoen met een wortel en een verlanglijstje. Vrijdag kijkt zij naar Oranje tegen Griekenland.", 15, lh=1.3, split=False)
f.ex("A2", "choice", "B", "A Sanne vive em Utrecht",
     "Waar woont Sanne? A. in Grave · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "choice", "B", "Na quarta-feira, ela junta-se ao desfile de São Martinho",
     "Wat doet Sanne op woensdag 11 november? A. Ze kijkt naar Oranje · B. Ze loopt mee in de Sint Maarten Parade · C. Ze leest Het diner", size=13.8, gap=0)
f.ex("A2", "choice", "B", "Ela põe uma cenoura e uma lista de desejos no seu sapato",
     "Wat zit er in de schoen van Sanne? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "choice", "B", "Ela vê as notícias do Sinterklaas todos os dias às 18:00",
     "Wanneer kijkt Sanne naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "make sentences", "Het Sinterklaasjournaal begint op maandag.", "Sujeito + verbo + tempo",
     "het sinterklaasjournaal / begint / op maandag → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("B1", "make sentences", "Wij zetten onze schoen bij de deur.", "Sujeito + verbo + objeto + lugar",
     "wij / zetten / onze schoen / bij de deur → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("B1", "make sentences", "Oranje speelt vrijdag tegen Griekenland.", "Sujeito + verbo + tempo + adversário",
     "oranje / speelt / vrijdag / tegen griekenland → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("B1", "make sentences", "Ik loop met een lampion langs de deuren.", "Sujeito + verbo + modo + lugar",
     "ik / loop / met een lampion / langs de deuren → ___", instr="Forme a frase", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "translate", "As notícias do Sinterklaas passam todos os dias às 18:00.", "Compara com o artigo da página 3",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Traduza para o português", size=13.8, gap=0)
f.ex("B1", "translate", "O São Martinho é a festa da partilha.", "Frase original da página 2 · delen = partilhar",
     "Sint-Maarten is het feest van het delen. → ___", instr="Traduza para o português", size=13.8, gap=0)
f.ex("B1", "translate", "De intocht in Amsterdam is de 88e editie.", "Atenção ao ordinal 88e",
     "A chegada a Amesterdão é a 88.ª edição. → ___", instr="Traduza para o neerlandês", size=13.8, gap=0)
f.ex("B2", "translate", "Ik zet mijn schoen met een verlanglijstje.", "schoen zetten é uma expressão fixa",
     "Ponho o sapato, com uma lista de desejos dentro. → ___", instr="Traduza para o neerlandês", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "matching",
            ["het journaal", "de intocht", "de lampion", "delen"],
            ["een papieren lichtje voor 11 november",
             "een dagelijks nieuwsprogramma op televisie",
             "licht en eten geven aan anderen",
             "de feestelijke aankomst van Sinterklaas"],
            ["b", "d", "a", "c"],
            ["journaal = noticiário b", "intocht = chegada festiva d", "lampion = lanterna a", "delen = partilhar c"],
            instr="Associe a palavra ao significado")
f.head("G · DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
f.ex("B1", "cloze choice", "A", "schoen = sapato",
     "— Mama, waar moet mijn ___? (A. schoen · B. boek)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "wortel = cenoura (para o cavalo)",
     "— Bij de deur, met een ___ voor het paard. (A. wortel · B. lampion)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "verlanglijstje = lista de desejos",
     "— En mijn ___ erin? (A. verlanglijstje · B. journaal)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "cadeautje = presentinho",
     "— Ja. Sinterklaas brengt 's nachts een ___. (A. mantel · B. cadeautje)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "18:00 = a hora das notícias do Sinterklaas",
     "— Eerst kijken we om ___ uur naar het Sinterklaasjournaal. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.head("H · SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Maandag 9 november begint het Sinterklaasjournaal. "
          "Ik kijk elke dag om 18:00 uur naar NPO Zapp. "
          "Op woensdag 11 november loop ik met een lampion langs de deuren en zing ik een liedje. "
          "Vrijdag kijk ik naar Oranje tegen Griekenland. "
          "Zaterdag kijk ik naar de intocht in Grave op televisie. "
          "Zondag vaart Sinterklaas in Amsterdam. "
          "Daarna zet ik mijn schoen met een wortel en een verlanglijstje. "
          "Ik hoop op een boek. "
          "Maandag 16 november speelt Oranje in Berlijn tegen Duitsland. "
          "Ik kijk ook dan. "
          "Wat een week vol licht!")
NWORDS = len(MODELO.split())
f.bridge(f"Tarefa de escrita (sem resposta única); texto modelo ({NWORDS} palavras) abaixo.")
f.ex("B1", "writing", "(tarefa aberta, texto modelo abaixo)", f"Vê o texto modelo na secção H ({NWORDS} palavras)",
     "«Mijn week met Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, loop jij met een lampion, kijk jij naar het Sinterklaasjournaal, en zet jij je schoen?", instr="Escreva", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ANTWOORDEN · CHAVE DE RESPOSTAS — agrupadas por página: encontra o teu número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Cada resposta com uma breve nota em português · ✓ marca a tarefa de escrita", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
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
