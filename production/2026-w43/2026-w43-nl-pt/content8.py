# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-nl-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · Teste e respostas", "De Lucerna", "Página 8 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "Cloze", "B", "No outono, o relógio atrasa",
     "In de nacht van zaterdag op zondag gaat de klok één uur ___. (A. vooruit · B. achteruit)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "As férias de Midden e Zuid vão até 25 de outubro",
     "De herfstvakantie van Midden en Zuid duurt tot en met zondag ___ oktober. (A. 25 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "A Design Week é em Eindhoven",
     "De Dutch Design Week is in ___. (A. Eindhoven · B. Amsterdam)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "O PSV venceu no Porto, fora de casa",
     "PSV won in de Champions League bij ___. (A. Atalanta · B. FC Porto)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "O ADE faz 30 anos este ano",
     "ADE wordt dit jaar ___ jaar. (A. 25 · B. 30)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Robinson começa em novembro",
     "Expeditie Robinson begint op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "O maior termo sobre o relógio foi «wintertijd»",
     "De grootste zoekterm over de klok was «___». (A. wintertijd · B. klok vooruit)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "half drie = 2:30",
     "«Half drie» is ___. (A. 03:30 · B. 02:30)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "Escolha múltipla", "B", "O horário de inverno começa às 03:00",
     "De wintertijd begint om... A. 02:00 uur · B. 03:00 uur · C. middernacht", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "A", "A região Noord teve férias de 10 a 18 de outubro",
     "Welke regio had vakantie van 10 tot en met 18 oktober? A. Noord · B. Midden · C. Zuid", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "C", "Bilhete de estudante: € 19,50",
     "Een studentenkaartje voor de DDW kost... A. € 32,50 · B. € 25,00 · C. € 19,50", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "A", "O Feyenoord joga na quarta em Sevilha",
     "Feyenoord speelt woensdag in... A. Sevilla · B. Porto · C. Eindhoven", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "Sparta – Ajax começa às 16:45",
     "Sparta – Ajax begint zondag om... A. 14:30 uur · B. 16:45 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "Os 19 candidatos são neerlandeses e flamengos",
     "De 19 kandidaten van Expeditie Robinson zijn... A. allemaal dj's · B. Nederlanders en Vlamingen · C. alleen sporters", size=13.8, gap=0)
f.ex("B2", "Escolha múltipla", "B", "Os 6.600 perguntaram ao contrário",
     "De 6.600 zoekopdrachten vroegen naar... A. achteruit · B. vooruit · C. wintertijd", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "A", "A plataforma mostra todos os custos extras com clareza",
     "Thuisbezorgd laat voortaan... A. alle extra kosten duidelijk zien · B. geen eten meer bezorgen · C. alleen kortingsbonnen zien", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht, in de regio Midden. Zij heeft de hele week herfstvakantie. Op woensdag gaat zij met haar zus naar Eindhoven, naar de Dutch Design Week. Zaterdagavond zet zij alle klokken in huis één uur achteruit — behalve haar telefoon, die doet het zelf. Zondag slaapt zij lang uit: het is de laatste dag van de vakantie.", 15, lh=1.3, split=False)
f.ex("A2", "Escolha múltipla", "B", "Sanne mora em Utrecht",
     "Waar woont Sanne? A. in Venlo · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "B", "É férias de outono na região dela",
     "Waarom heeft Sanne de hele week vrij? A. Zij is ziek · B. Het is herfstvakantie in haar regio · C. Zij werkt niet", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "B", "No sábado à noite, ela acerta os relógios",
     "Wat doet Sanne zaterdagavond? A. Zij gaat dansen · B. Zij zet de klokken achteruit · C. Zij pakt haar koffer", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "C", "O telefone muda sozinho, sem acertar à mão",
     "Welke klok zet Sanne NIET met de hand achteruit? A. de ovenklok · B. de wekker · C. haar telefoon", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Forme a frase", "De klok gaat één uur achteruit.", "sujeito + verbo + direção",
     "de klok / gaat / één uur / achteruit → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("B1", "Forme a frase", "Wij gaan zondag naar de topper.", "sujeito + verbo + lugar",
     "wij / gaan / zondag / naar de topper → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("B1", "Forme a frase", "Hoe laat begint de wedstrijd?", "A pergunta vai no início",
     "hoe laat / begint / de wedstrijd / ? → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("B1", "Forme a frase", "PSV won met 1–0 in Porto.", "verbo + resultado + lugar",
     "psv / won / met 1–0 / in porto → ___", instr="Forme a frase", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "Traduza", "Domingo o relógio atrasa: dormir uma hora a mais!", "Compare com a faixa da página 1",
     "Zondag gaat de klok terug: een uur langer slapen! → ___", instr="Traduza", size=13.8, gap=0)
f.ex("B1", "Traduza", "O seu telefone e o seu computador mudam a hora sozinhos.", "Frase da página 2 · veranderen = mudar",
     "Je telefoon en je computer veranderen de tijd zelf. → ___", instr="Traduza", size=13.8, gap=0)
f.ex("B1", "Traduza", "De Dutch Design Week is in Eindhoven.", "Atenção à expressão de lugar in Eindhoven",
     "A Dutch Design Week é em Eindhoven. → ___", instr="Traduza", size=13.8, gap=0)
f.ex("B2", "Traduza", "Zondag heb ik een uur langer geslapen.", "perfectum: heb geslapen",
     "No domingo, dormi uma hora a mais. → ___", instr="Traduza", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "Associação",
            ["de klok verzetten", "het ezelsbruggetje", "eropuit gaan", "bijslapen"],
            ["extra slapen om uit te rusten",
             "het huis uit gaan voor iets leuks",
             "een hulpmiddel om iets te onthouden",
             "de tijd op een klok veranderen"],
            ["d", "c", "b", "a"],
            ["verzetten = acertar o relógio d", "ezelsbruggetje = frase para memorizar c", "eropuit = sair para passear b", "bijslapen = dormir para recuperar a"],
            instr="Associe as palavras")
f.head("G · DIALOOG BIJ DE DDW", 21, OLIVE, 5)
f.ex("B1", "Cloze", "B", "kaartje = bilhete",
     "— Goedemorgen! Een ___ voor de Dutch Design Week, alstublieft. (A. ezelsbruggetje · B. kaartje)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "student = estudante (bilhete € 19,50)",
     "— Natuurlijk. Bent u ___? Studenten betalen € 19,50. (A. student · B. ontwerper)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "tot hoe laat = até que horas (aberto)",
     "— Ja! Hier is mijn studentenkaart. En tot hoe ___ zijn jullie open? (A. lang · B. laat)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "veel plezier = divirta-se",
     "— Tot 18:00 uur. Veel ___ met de ontwerpen! (A. plezier · B. slaap)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "tot ziens = até logo",
     "— Dank u wel, tot ___! (A. straks · B. ziens)", size=13.8, gap=0)
f.head("H · SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Zondag 25 oktober word ik laat wakker: het is de laatste dag van mijn herfstvakantie. "
          "Ik heb een uur langer geslapen, want vannacht ging de klok achteruit. "
          "Na het ontbijt ga ik met mijn vrienden naar het bos; de bladeren zijn geel en rood. "
          "'s Middags kijken wij thuis naar PSV tegen Feyenoord op televisie. "
          "Mijn zus gaat naar Amsterdam voor ADE, maar ik blijf liever thuis met een boek. "
          "'s Avonds pak ik mijn tas voor school: morgen begint het gewone leven weer. "
          "Wat een week!")
NWORDS = len(MODELO.split())
f.expl(f"Questão de escrita (sem resposta única); o modelo ({NWORDS} palavras) está abaixo.")
f.ex("B1", "Escreva", "(pergunta aberta — modelo abaixo)", f"Modelo na seção H desta página ({NWORDS} palavras)",
     "«Jouw zondag 25 oktober» Schrijf 80–100 woorden: wat doe jij op de laatste vakantiedag, hoe laat sta jij op, en wat doe jij 's middags?", instr="Escreva", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ANTWOORDEN · Respostas — por página: procure o número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Nota em português em cada resposta · ✓ = com modelo", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Escreva":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-toets.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
