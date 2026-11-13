# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　Kultur", "A Lucerna", "A2 → B1　Zumbi e Palmares: a história do 20 de novembro")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 200, 1560, tag="P3-main")
f.title("Zumbi e Palmares: a história do 20 de novembro", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: A2 → B1")
f.para("Em 20 de novembro de 1695, morre Zumbi dos Palmares, o último grande líder do Quilombo dos Palmares, em Alagoas. A data virou o Dia Nacional de Zumbi e da Consciência Negra: em 2011, a Lei nº 12.519 criou o dia e, em 2023, a Lei nº 14.759 fez dele feriado nacional.")
f.para("Palmares foi o maior quilombo do Brasil: no século XVII, milhares de africanos escravizados que fugiam formaram uma comunidade livre na Serra da Barriga. Zumbi nasceu em Palmares e defendeu o quilombo por anos contra as tropas coloniais.")
f.para("O que a data celebra? A resistência, a história e a cultura afro-brasileiras — a capoeira, o samba, a culinária, a literatura. E também a reflexão: o combate ao racismo continua, todos os dias.")
f.para("E por que 20 de novembro? Porque é o dia da morte de Zumbi. O Brasil lembra o líder para não esquecer a história: sem memória, não há futuro. Na página 2, o feriadão; na página 5, a semana dos jovens.")
f.gloss("o quilombo eine Siedlung entflohener Sklaven · a resistência Widerstand · escravizado versklavte Person · o líder Anführer · a memória Erinnerung · o combate Kampf.")
f.head("UM DIA, DOIS SENTIDOS", 25)
f.para("Um feriado é descanso — e memória. No dia 20, o Brasil descansa e lembra: a liberdade que Palmares defendeu é a mesma que o país celebra hoje, na capoeira, no samba e nas ruas.")
f.end_report()

# col 2: Zumbi painting (portrait, natural aspect 713x960 -> 340x458)
zx = COLX[2]
image(p, "zumbi.jpg", zx + 41, 200, 340, 458)
caption(p, zx, 200 + 458, CW,
        "Zumbi dos Palmares, em pintura de Antônio Parreiras (1927): o líder do quilombo, na mata, com a sua arma.",
        "Pintura: Antônio Parreiras / Wikimedia Commons — Domínio público")

# col 3: calendar box + e você + words box (sequential)
ix = COLX[3]
semana = ["Seg 16 — começa a semana do feriado.",
          "Ter 17 — Singapura × Brasil, às 7h.",
          "Sex 20 — o feriado da Consciência Negra.",
          "Sáb 21 — Palmeiras × Flamengo, às 16h30."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in semana) + 58  # fix1 (2026-11-11): +26 (was +32). Last line '16h30.' sat 15.6px BELOW the old bottom 525; +26 gives ink-bottom clearance ~+11px. Boxes below (ey3/ky3) derive from sh and shift down with it.
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "A SEMANA, DIA A DIA", 24, "sans", True, OLIVE)
yy3 += 52
for t in semana:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? No seu país, há um herói ou uma heroína que lutou pela liberdade? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Gibt es in Ihrem Land eine Heldin oder einen Helden, die oder der für die Freiheit gekämpft hat? Schreiben Sie zwei Sätze und schicken Sie sie ein.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　Erzählen Sie von sich", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Gibt es in Ihrem Land eine Heldin oder einen Helden, die oder der für die Freiheit gekämpft hat? Schreiben Sie zwei Sätze und schicken Sie sie ein.", 20, "sans", False, GREY, CW - 44, 1.42)
ky3 = ey3 + eh + 26
kb = "a consciência · o quilombo · a resistência · Zumbi · Palmares · «resistir» — seis palavras para um feriado de memória."
kh = 62 + len(wrap(kb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(ix, ky3, CW, kh, fill=BOX)
yy3 = ky3 + 16
p.text(ix + 22, yy3 + 26, "PALAVRAS DA MEMÓRIA", 22, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, kb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P3 col3 ends", ky3 + kh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　SEITE 3 ÜBUNGEN", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Lösungen auf Seite 8　Die Niveaus sind gemischt — suchen Sie die Lösungen nach Nummern", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("Lesen Sie den Artikel auf Seite 3 und wählen Sie die richtige Antwort.")
e.ex("A2", "Multiple Choice", "C", "Zumbi starb am 20. November 1695",
     "Zumbi dos Palmares morreu... A. em 1889 · B. em 2011 · C. em 20 de novembro de 1695", size=20, gap=8)
e.ex("A2", "Multiple Choice", "A", "Palmares lag in Alagoas",
     "O Quilombo dos Palmares ficava... A. em Alagoas · B. no Rio · C. em São Paulo", size=20, gap=8)
e.ex("A2", "Multiple Choice", "B", "Das Gesetz von 2023 machte den 20. November zu einem nationalen Feiertag",
     "A Lei nº 14.759, de 2023... A. criou o dia 20 · B. fez do dia 20 feriado nacional · C. acabou com o feriado", size=20, gap=8)
e.ex("A2", "Multiple Choice", "B", "Palmares war das größte Quilombo Brasiliens",
     "Palmares foi... A. uma cidade portuguesa · B. o maior quilombo do Brasil · C. um time de futebol", size=20, gap=8)
e.ex("B1", "Multiple Choice", "A", "Dieser Tag erinnert an Widerstand, Geschichte und afrobrasilianische Kultur",
     "O dia 20 celebra... A. a resistência e a cultura afro-brasileira · B. a Proclamação da República · C. o Enem", size=20, gap=8)
e.head("B　AS PALAVRAS DO TEXTO", 25)
e.bridge("Ergänzen Sie mit den Wörtern aus dem Kasten.")
e.para("quilombo · resistência · escravizado · líder · memória · combate", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Sätze vervollständigen", "quilombo", "quilombo = eine Siedlung entflohener Sklaven",
     "Palmares foi o maior ___ do Brasil.", instr="Ergänzen Sie", size=20, gap=8)
e.ex("A2", "Sätze vervollständigen", "resistência", "resistência = Widerstand",
     "O dia 20 celebra a ___ do povo negro.", instr="Ergänzen Sie", size=20, gap=8)
e.ex("A2", "Sätze vervollständigen", "escravizados", "escravizado im Plural angepasst: escravizados",
     "Milhares de africanos ___ fugiam e formavam quilombos.", instr="Ergänzen Sie", size=20, gap=8)
e.ex("A2", "Sätze vervollständigen", "líder", "líder = Anführer",
     "Zumbi foi o último grande ___ de Palmares.", instr="Ergänzen Sie", size=20, gap=8)
e.ex("A2", "Sätze vervollständigen", "memória", "memória = Erinnerung",
     "Sem ___ , não há futuro.", instr="Ergänzen Sie", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "combate", "combate = Kampf",
     "O ___ ao racismo continua todos os dias.", instr="Ergänzen Sie", size=20, gap=8)
e.head("C　O PRETÉRITO PERFEITO", 25)
e.bridge("Ergänzen Sie in der Vergangenheit (pretérito perfeito).")
e.ex("B1", "Sätze vervollständigen", "morreu", "morrer, Vergangenheit, ele-Form: morreu",
     "Zumbi ___ (morrer) em 20 de novembro de 1695.", instr="Ergänzen Sie", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "nasceu", "nascer, Vergangenheit, ele-Form: nasceu",
     "Zumbi ___ (nascer) em Palmares.", instr="Ergänzen Sie", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "defendeu", "defender, Vergangenheit, ele-Form: defendeu",
     "Zumbi ___ (defender) o quilombo por anos.", instr="Ergänzen Sie", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "formaram", "formar, Vergangenheit, eles-Form: formaram",
     "Os fugitivos ___ (formar) uma comunidade livre.", instr="Ergänzen Sie", size=20, gap=8)
e.head("D　CONSTRUA AS FRASES", 25)
e.bridge("Bilden Sie aus den Wörtern richtige Sätze.")
e.ex("B1", "Satzbildung", "O dia 20 de novembro é feriado nacional.", "Subjekt + é + Prädikativ",
     "o dia 20 / é / feriado nacional → ___", instr="Satzbildung", size=20, gap=8)
e.ex("A2", "Satzbildung", "Zumbi foi o líder de Palmares.", "Subjekt + Verb + Prädikativ",
     "zumbi / foi / o líder / de palmares → ___", instr="Satzbildung", size=20, gap=8)
e.ex("B1", "Satzbildung", "Palmares foi o maior quilombo do Brasil.", "Subjekt + Verb + Prädikativ",
     "palmares / foi / o maior quilombo / do brasil → ___", instr="Satzbildung", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · ESPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("ESPORTE　Sport", "A Lucerna", "NÍVEL B1　A final da Copa do Brasil　Das Finale der Copa do Brasil steht fest")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Grêmio e Palmeiras decidem a Copa do Brasil", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: B1")
f.para("A pergunta da semana passada tem resposta: quem vai à final da Copa do Brasil? No sábado, 7, o Grêmio empatou por 1 a 1 com o Atlético-MG, na Arena MRV, e passou com 3 a 1 no total: havia vencido a ida por 2 a 0, em Porto Alegre. Renan Lodi abriu o placar para o Atlético e Carlos Vinícius empatou para o Grêmio.")
f.para("No domingo, 8, o Vasco venceu o Palmeiras por 2 a 1, em São Januário — mas o Palmeiras havia vencido a ida por 1 a 0, e o agregado ficou em 2 a 2. Nos pênaltis, o Palmeiras venceu por 5 a 4 e foi à final. Foi a segunda semifinal decidida nos detalhes: um empate que bastou, e uma disputa de pênaltis.")
f.para("A final é em jogo único, no dia 6 de dezembro, no Mané Garrincha, em Brasília. O Grêmio busca o sexto título — e joga a décima final da sua história. O Palmeiras busca o quinto título da Copa do Brasil. Quem ganha, levanta a taça e garante vaga na próxima Libertadores.")
f.para("E o Brasileirão volta depois da pausa: a rodada 35 termina na quarta, 18, e na quinta, 19 — Cruzeiro × Palmeiras e Flamengo × Athletico-PR na quarta; Vasco × Internacional e São Paulo × Fluminense na quinta. No sábado, 21, às 16h30, Palmeiras × Flamengo: o jogo que pode decidir o título. E em Interlagos, no domingo 8, Lando Norris venceu o Grande Prêmio de São Paulo, com Verstappen em segundo e Hadjar em terceiro; a Mercedes garantiu o título de construtores.")
f.gloss("o agregado Gesamtergebnis · os pênaltis Elfmeterschießen · a decisão das Finale · o título Titel · a pausa die Pause · a taça Pokal.")
f.end_report()

# col 3: data box + e você (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX)
p.text(bx + 22, 240, "OS FINALISTAS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Ida, dom 1º — Grêmio 2 × 0 Atlético-MG; Palmeiras 1 × 0 Vasco. Volta, sáb 7 — Atlético-MG 1 × 1 Grêmio (total 3 × 1). Volta, dom 8 — Vasco 2 × 1 Palmeiras (total 2 × 2; pênaltis 5 × 4). Final — 6 de dezembro, Mané Garrincha, Brasília.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "E você? Na final, Grêmio ou Palmeiras — para quem você torce? Escreva duas frases em português e mande para a redação."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Im Finale: Sind Sie für Grêmio oder für Palmeiras? Schreiben Sie zwei Sätze und schicken Sie sie ein.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E VOCÊ?　Erzählen Sie von sich", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Im Finale: Sind Sie für Grêmio oder für Palmeiras? Schreiben Sie zwei Sätze und schicken Sie sie ein.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "A SEMANA DO FUTEBOL　Fußballwoche", 26, "sans", True, OLIVE)
rows = [
    ("Sáb 7.11", "Copa do Brasil", "Atlético-MG 1 × 1 Grêmio — a volta; o Grêmio passa com 3 × 1 no total"),
    ("Dom 8.11", "Copa do Brasil", "Vasco 2 × 1 Palmeiras — a volta; nos pênaltis, 5 × 4 para o Palmeiras"),
    ("Dom 8.11", "Fórmula 1", "Norris vence em Interlagos; Verstappen é 2º, Hadjar é 3º"),
    ("Qua 18.11", "Brasileirão", "Cruzeiro × Palmeiras, às 20h30 — rodada 35; Flamengo × Athletico-PR, às 20h30"),
    ("Qui 19.11", "Brasileirão", "Vasco × Internacional, às 19h30; São Paulo × Fluminense, às 21h30"),
    ("Sáb 21.11", "Brasileirão", "Palmeiras × Flamengo, às 16h30, Nubank Parque — o jogo do título"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Nota: esta edição fechou em 10 de novembro. Os jogos de 14 a 22 ainda não tinham acontecido — os resultados saem na próxima edição."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　SEITE 4 ÜBUNGEN", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Lösungen auf Seite 8　Die Niveaus sind gemischt — suchen Sie die Lösungen nach Nummern", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("Lesen Sie den Artikel auf Seite 4 und wählen Sie die richtige Antwort.")
e.ex("B1", "Multiple Choice", "A", "Im Rückspiel spielte Grêmio 1:1 gegen Atlético-MG und kam mit 3:1 im Gesamtergebnis weiter",
     "Na volta, Atlético-MG × Grêmio foi... A. 1 a 1, e o Grêmio passou com 3 a 1 no total · B. 2 a 0 para o Atlético · C. 0 a 0", size=20, gap=8)
e.ex("B1", "Multiple Choice", "B", "Vasco gewann das Rückspiel mit 2:1, doch das Gesamtergebnis war 2:2 und Palmeiras kam im Elfmeterschießen weiter",
     "Na volta, Vasco × Palmeiras foi... A. 1 a 0 para o Palmeiras · B. 2 a 1 para o Vasco, e o Palmeiras passou nos pênaltis · C. 0 a 0", size=20, gap=8)
e.ex("B1", "Multiple Choice", "B", "Elfmeterschießen 5:4: Palmeiras ist weiter",
     "Nos pênaltis, o Palmeiras venceu por... A. 4 a 3 · B. 5 a 4 · C. 6 a 5", size=20, gap=8)
e.ex("B1", "Multiple Choice", "B", "Das Finale ist ein einziges Spiel am 6. Dezember im Mané Garrincha",
     "A final da Copa do Brasil é... A. em dois jogos · B. em jogo único, no dia 6 de dezembro · C. no dia 15", size=20, gap=8)
e.ex("B1", "Multiple Choice", "A", "Norris gewann den Großen Preis von São Paulo, Verstappen wurde Zweiter",
     "O Grande Prêmio de São Paulo foi vencido por... A. Lando Norris · B. Max Verstappen · C. Isack Hadjar", size=20, gap=8)
e.head("B　AS PALAVRAS", 25)
e.match_set("B1", "Wortschatz-Zuordnung",
            ["o agregado", "a volta", "os pênaltis", "a taça"],
            ["o segundo jogo de um confronto",
             "o placar dos dois jogos somados",
             "o prêmio do campeão",
             "a disputa da marca dos onze metros"],
            ["b", "a", "d", "c"],
            ["agregado=die beiden Spiele zusammengerechnet b", "volta=das zweite Spiel einer Begegnung a", "pênaltis=das Elfmeterschießen vom Elfmeterpunkt d", "taça=die Meistertrophäe c"],
            instr="Paare zuordnen")
e.head("C　COMPARATIVOS", 25)
e.bridge("Ergänzen Sie die richtige Vergleichsform in Klammern.")
e.ex("B1", "Sätze vervollständigen", "mais", "3 > 1:mais",
     "Três gols são ___ do que um gol. (mais / menos)", instr="Ergänzen Sie", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "mais", "5 > 4:mais",
     "Cinco pênaltis são ___ do que quatro. (mais / menos)", instr="Ergänzen Sie", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "mais", "16:30 < 17:00:mais cedo",
     "16h30 é ___ cedo do que 17h. (mais / menos)", instr="Ergänzen Sie", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "menos", "2 Tage < 7 Tage: menos",
     "Dois dias são ___ do que uma semana. (mais / menos)", instr="Ergänzen Sie", size=20, gap=8)
e.head("D　O PRETÉRITO PERFEITO", 25)
e.bridge("Vervollständigen Sie die Sätze in der Vergangenheit (pretérito perfeito).")
e.ex("B1", "Sätze vervollständigen", "empatou", "empatar, Vergangenheit, ele-Form: empatou",
     "O Grêmio ___ (empatar) por 1 a 1.", instr="Ergänzen Sie", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "venceu", "vencer, Vergangenheit, ele-Form: venceu",
     "O Vasco ___ (vencer) por 2 a 1.", instr="Ergänzen Sie", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "abriu", "abrir, Vergangenheit, ele-Form: abriu",
     "Renan Lodi ___ (abrir) o placar.", instr="Ergänzen Sie", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "garantiu", "garantir, Vergangenheit, ela-Form: garantiu",
     "A Mercedes ___ (garantir) o título de construtores.", instr="Ergänzen Sie", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "foram", "ser Vergangenheit, Plural: foram",
     "Os jogos de volta ___ (ser) no fim de semana.", instr="Ergänzen Sie", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-esporte.svg")
print("P4 saved, exercises so far:", len(REG))
