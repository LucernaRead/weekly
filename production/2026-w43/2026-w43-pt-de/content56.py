# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-pt-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JOVENS (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JOVENS · JUGEND", "A Lucerna", "NÍVEL B1 · A Fazenda, o Enem e os planos dos jovens · Realityshow, Enem und die Pläne der Jugend")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Duas votações e uma prova: a semana dos jovens", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: B1")
f.para("A semana dos jovens brasileiros tem três datas. A primeira é da televisão: em A Fazenda 18, o reality da Record, Catherine Bascoy, Gabriel Torres e Thaíde disputam a Prova do Fazendeiro nesta quarta-feira, 21 de outubro. Na internet, a enquete já corre: quem fica e quem sai do jogo?")
f.para("A segunda data é do estudo. Faltam menos de três semanas para o Enem 2026: as provas são nos domingos 8 e 15 de novembro, e mais de 5 milhões de estudantes estão inscritos. Neste mês, o Inep libera o Cartão de Confirmação, o documento que mostra o local da prova de cada aluno. É a reta final: revisar, descansar e conferir o endereço — como na eleição, quem confere antes não se perde no dia.")
f.para("A terceira data é um termômetro. Depois do primeiro turno, as buscas por «como morar fora do Brasil» cresceram 40%, segundo um levantamento com dados do Google. É um comportamento de busca, não um dado de emigração: mostra uma pergunta que muitos jovens fazem nesta semana — ficar ou partir?")
f.box("O PLANO DA RETA FINAL", [
    ("1. Confira o Cartão de Confirmação do Enem (Enem-Bestätigungskarte prüfen)", "serif", False, INK, 21, 1.36),
    ("2. Revise um pouco por dia, sem maratona (jeden Tag etwas, kein Marathon)", "serif", False, INK, 21, 1.36),
    ("3. Durma bem na véspera da prova (am Vorabend gut schlafen)", "serif", False, INK, 21, 1.36),
    ("4. Separe documento e caneta no dia anterior (Ausweis und Stift am Vortag bereitlegen)", "serif", False, INK, 21, 1.36),
    ("5. Domingo 25: vote (se você vota) e descanse (Sonntag, 25.: wählen und ausruhen)", "serif", False, INK, 21, 1.36),
])
f.gloss("a enquete = (Zuschauer-)Abstimmung, Umfrage · a reta final = der Endspurt · o levantamento = Erhebung · a véspera = der Vorabend.")
f.end_report()

# col 3: study image + facts + e você + mega-sena box (sequential)
ix = COLX[3]
image(p, "estudo.jpg", ix, 200, CW, 272)
cy3 = caption(p, ix, 472, CW, "Estudantes em uma biblioteca: para os mais de 5 milhões de inscritos no Enem, é a reta final — provas nos dias 8 e 15 de novembro.",
              "Foto: Gary Todd / Wikimedia Commons — CC0")
facts = ["Mais de 5 milhões de inscritos no Enem 2026 (Inep).",
         "Provas do Enem: domingos 8 e 15 de novembro.",
         "+40%: as buscas por «como morar fora do Brasil» depois do 1º turno."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "OS JOVENS EM NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? Qual é o seu plano para o ano que vem: estudar, trabalhar, viajar? Escreva duas frases em português."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Was planen Sie für nächstes Jahr: lernen, arbeiten, reisen? Schreiben Sie zwei Sätze.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ? · UND SIE?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Was planen Sie für nächstes Jahr: lernen, arbeiten, reisen? Schreiben Sie zwei Sätze.", 20, "sans", False, GREY, CW - 44, 1.42)
ky3 = ey3 + eh + 26
kb = ("Num agregador de tendências, na terça-feira, 20 de outubro, «mega-sena» aparecia como a busca número um do Brasil. É um dado de agregador, não do feed oficial do Google — mas a lição fica: em semana de eleição, o brasileiro também sonha com a loteria.")
kh = 62 + len(wrap(kb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(ix, ky3, CW, kh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ky3 + 16
p.text(ix + 22, yy3 + 26, "E A MEGA-SENA?", 22, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, kb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P5 col3 ends", ky3 + kh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCÍCIOS · ÜBUNGEN · SEITE 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Lösungen auf Seite 8 · gemischte Stufen — nach Nummern suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · COMPREENSÃO", 25)
e.bridge("Lesen Sie Seite 5 und wählen Sie die richtige Antwort.")
e.ex("B1", "单选", "B", "Prova do Fazendeiro: Mittwoch, 21.",
     "A Prova do Fazendeiro de A Fazenda 18 é... A. na sexta-feira · B. na quarta-feira, 21 · C. no domingo, 25", size=20, gap=8)
e.ex("B1", "单选", "C", "Enem am 8. und 15. November",
     "As provas do Enem 2026 são nos dias... A. 25 de outubro e 1º de novembro · B. 1º e 8 de novembro · C. 8 e 15 de novembro", size=20, gap=8)
e.ex("B1", "单选", "A", "über 5 Millionen Angemeldete",
     "O Enem 2026 tem... A. mais de 5 milhões de inscritos · B. 500 mil inscritos · C. 5 milhões de seções", size=20, gap=8)
e.ex("B1", "单选", "B", "die Karte zeigt den Prüfungsort",
     "O Cartão de Confirmação mostra... A. a nota do aluno · B. o local da prova · C. o resultado final", size=20, gap=8)
e.ex("B1", "单选", "C", "Suchen nach „Auswandern“ +40 %",
     "Depois do primeiro turno, cresceram 40% as buscas por... A. «guitarra» · B. «mega-sena» · C. «como morar fora do Brasil»", size=20, gap=8)
e.head("B · AS PALAVRAS DO TEXTO", 25)
e.bridge("Setzen Sie die Wörter aus dem Kasten ein. Achtung: Einige müssen in den Plural.")
e.para("enquete · reta final · inscrito · véspera · levantamento · local", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "enquete", "enquete = Zuschauerabstimmung, Umfrage",
     "Na internet, a ___ pergunta quem fica no jogo.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "完成句子", "inscritos", "Plural zu inscrito: inscritos",
     "Mais de 5 milhões de estudantes estão ___ no Enem.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "完成句子", "reta final", "reta final = Endspurt",
     "Outubro é a ___ dos estudos: falta pouco para a prova.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "完成句子", "véspera", "véspera = Vorabend",
     "Na ___ da prova, o melhor é dormir cedo.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "完成句子", "levantamento", "levantamento = Erhebung",
     "Um ___ com dados do Google mediu as buscas.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "完成句子", "local", "local = Ort",
     "Confira o ___ da sua prova no cartão.", instr="Ausfüllen", size=20, gap=8)
e.head("C · O FUTURO DO PRESENTE", 25)
e.bridge("Ergänzen Sie im Futuro do Presente.")
e.ex("B1", "完成句子", "farão", "fazer, Zukunft (eles, unregelmäßig): farão",
     "Os estudantes ___ (fazer) a prova em novembro.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "完成句子", "mostrará", "mostrar, Zukunft: mostrará",
     "O cartão ___ (mostrar) o local da prova.", instr="Ausfüllen", size=20, gap=8)
e.ex("B2", "完成句子", "disputarão", "disputar, Zukunft Plural: disputarão",
     "Três participantes ___ (disputar) a prova na quarta-feira.", instr="Ausfüllen", size=20, gap=8)
e.ex("B2", "完成句子", "ficará", "ficar, Zukunft: ficará",
     "«Quem ___ (ficar) no jogo?» pergunta a enquete.", instr="Ausfüllen", size=20, gap=8)
e.head("D · VERDADEIRO OU FALSO?", 25)
e.ex("B1", "判断对错", "Verdadeiro", "die Karte erscheint im Oktober",
     "O Cartão de Confirmação sai neste mês de outubro. Verdadeiro ou falso?", instr="Wahr oder falsch?", size=20, gap=8)
e.ex("B1", "判断对错", "Falso", "Falsch: Suchverhalten, keine Auswanderungsdaten",
     "As buscas por «morar fora» são um dado oficial de emigração. Verdadeiro ou falso?", instr="Wahr oder falsch?", size=20, gap=8)
e.ex("B2", "判断对错", "Verdadeiro", "Richtig: zwei „Wahlen“ in einer Woche",
     "Na mesma semana, o Brasil vota no presidente e na enquete de um reality. Verdadeiro ou falso?", instr="Wahr oder falsch?", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jovens.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · APROFUNDAMENTO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("APROFUNDAMENTO · VERTIEFUNG", "A Lucerna", "NÍVEL B2 · O segundo turno, explicado · Die Stichwahl erklärt")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1520, tag="P6-main")
f.title("O segundo turno: como o Brasil escolhe o presidente", 37)
f.byline("Da redação da A Lucerna · Nível de leitura: B2 · A política nacional brasileira")
f.para("No primeiro turno, no dia 4 de outubro, nenhum candidato à Presidência conseguiu mais da metade dos votos válidos. Por isso a Constituição manda repetir a disputa: é o segundo turno, neste domingo, 25 de outubro, só com os dois candidatos mais votados — Lula (PT) e Flávio Bolsonaro (PL).")
f.para("A regra é a maioria absoluta: vence quem tiver mais votos válidos no domingo. O mesmo acontece com os governadores em seis estados e no Distrito Federal, onde também ninguém venceu na primeira rodada.")
f.para("A campanha da última semana tem um centro: o debate. O calendário dos debates mostra o desenho da reta final — a Band fez o seu no domingo, 18 de outubro, às 20h; os debates da Record (11 de outubro) e do pool do SBT (15 de outubro) foram cancelados; e o último encontro é o da TV Globo, na sexta-feira, 23, depois do Jornal Nacional, com mediação de César Tralli e os dois candidatos convidados. Na mesma sexta-feira, termina a propaganda eleitoral gratuita.")
f.para("E os números? Cuidado com a confusão da semana: as porcentagens que circulam — eleições +900%, presidente +250%, multa eleitoral +350% — são dados de busca do Google, publicados antes e depois do primeiro turno. Interesse de busca não é intenção de voto: medir cliques não é medir urnas. Nesta edição, a A Lucerna não publica nenhuma porcentagem como se fosse pesquisa eleitoral.")
f.gloss("os votos válidos = gültige Stimmen · a maioria absoluta = absolute Mehrheit · vencer = gewinnen · a campanha = Wahlkampf · a intenção de voto = Wahlabsicht.")
f.end_report()

# col 3: timeline + ler os números (sequential, measured)
bx = COLX[3]
p.rect(bx, 200, CW, 640, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "O CAMINHO ATÉ A URNA", 22, "sans", True, OLIVE)
steps = [
    ("4 OUT.", "Primeiro turno: nenhum candidato passa da metade dos votos válidos."),
    ("18 OUT.", "Debate da Band, às 20h, no primeiro domingo da reta final."),
    ("23 OUT.", "Último debate, na TV Globo, depois do Jornal Nacional; fim da propaganda gratuita."),
    ("25 OUT.", "Segundo turno: votação das 8h às 17h, hora de Brasília."),
]
sy3 = 282
for w, t in steps:
    p.text(bx + 22, sy3 + 21, w, 20, "sans", True, BRICK)
    sy3 = p.para(bx + 164, sy3 + 21, t, 21, "serif", False, INK, CW - 186, 1.4) + 16
by3 = 866
bb = ("Diante de uma porcentagem, faça três perguntas: quem publica? Quando? "
      "É busca, voto ou pesquisa? Sem essas respostas, um número diz pouco.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LER OS NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh)

# ---- search-data charts (Google data, honestly captioned) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, GOLD, 2)
p.text(MX, gy + 10, "AS BUSCAS DO 1º TURNO · DIE SUCHEN ZUM 1. WAHLGANG (dados do Google)", 26, "sans", True, OLIVE)
bw_ = 2 * CW + GUT
# left box: Google panel, 7 Oct
bx1 = MX
p.rect(bx1, gy + 28, bw_, 322, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx1 + 22, gy + 68, "O PAINEL DO GOOGLE · painel de 7 de outubro", 21, "sans", True, INK)
painel = [("eleições", 900), ("presidente", 250)]
yy = gy + 100
for lab, v in painel:
    p.text(bx1 + 22, yy + 24, lab, 20, "serif", True, INK)
    labw = text_w(lab, "serif", True, 20)
    p.rect(bx1 + 40 + labw, yy + 6, v * 0.37, 22, fill=OLIVE)
    p.text(bx1 + 58 + labw + v * 0.37, yy + 24, f"+{v}%", 20.5, "serif", False, INK)
    yy += 44
p.para(bx1 + 22, gy + 218, "Crescimento do interesse de busca contra a semana anterior ao primeiro turno. É comportamento de busca — não é intenção de voto.", 19.5, "serif", False, INK, bw_ - 44, 1.4)
p.para(bx1 + 22, gy + 322 - 34, "Fonte: Google, dados publicados depois do 1º turno.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right box: voters' questions (Google via UOL)
bx2 = COLX[2]
p.rect(bx2, gy + 28, bw_, 322, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx2 + 22, gy + 68, "AS PERGUNTAS DO ELEITOR · mais buscas", 21, "sans", True, INK)
perg = [("que horas começa a votação?", 550), ("multa eleitoral", 350), ("seção eleitoral", 350)]
yy = gy + 100
for lab, v in perg:
    p.text(bx2 + 22, yy + 24, lab, 20, "serif", True, INK)
    labw = text_w(lab, "serif", True, 20)
    p.rect(bx2 + 40 + labw, yy + 6, v * 0.37, 22, fill=GOLD)
    p.text(bx2 + 58 + labw + v * 0.37, yy + 24, f"+{v}%", 20.5, "serif", False, INK)
    yy += 40
p.para(bx2 + 22, gy + 230, "As perguntas práticas do eleitor também explodiram nas buscas: horário, multa e o lugar de votar.", 19.5, "serif", False, INK, bw_ - 44, 1.4)
p.para(bx2 + 22, gy + 322 - 34, "Fonte: dados do Google publicados pela imprensa (UOL).", 17.5, "sans", False, GREY, bw_ - 44, 1.3)

# ---- P6 exercises ----
ey = 1930
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCÍCIOS · ÜBUNGEN · SEITE 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Lösungen auf Seite 8 · gemischte Stufen — nach Nummern suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LER OS GRÁFICOS", 25)
e.bridge("Antworten zu den Grafiken oben — wählen Sie die richtige.")
e.ex("B2", "单选", "B", "am stärksten: eleições, +900 %",
     "No painel do Google, a busca que mais cresceu foi... A. presidente, +250% · B. eleições, +900% · C. multa eleitoral, +350%", size=17, gap=0)
e.ex("B2", "单选", "A", "«presidente» wächst um +250 %",
     "A busca «presidente» cresceu... A. +250% · B. +900% · C. +350%", size=17, gap=0)
e.ex("B2", "单选", "C", "„Que horas…?“ wächst um +550 %",
     "A pergunta «que horas começa a votação?» cresceu... A. +300% · B. +350% · C. +550%", size=17, gap=0)
e.ex("B2", "单选", "A", "350 + 350 = 700 Punkte",
     "«Multa eleitoral» (+350%) e «seção eleitoral» (+350%), juntas, somam... A. 700 pontos · B. 350 pontos · C. 900 pontos", size=17, gap=0)
e.ex("B2", "单选", "B", "900 − 250 = 650",
     "A diferença entre «eleições» (+900%) e «presidente» (+250%) é de... A. 1.150 · B. 650 · C. 450", size=17, gap=0)
e.ex("B2", "单选", "B", "Suchinteresse ist keine Wahlabsicht",
     "Os dados do painel são... A. uma pesquisa eleitoral oficial · B. interesse de busca, não intenção de voto · C. o resultado da eleição", size=17, gap=0)
e.head("B · COMPREENSÃO", 25)
e.ex("B2", "单选", "B", "keiner über der Hälfte der gültigen Stimmen",
     "O segundo turno existe porque... A. o 1º turno foi cancelado · B. nenhum candidato passou da metade dos votos válidos · C. os debates acabaram", size=17, gap=0)
e.ex("B2", "单选", "A", "die meisten gültigen Stimmen gewinnen",
     "No segundo turno, vence... A. quem tiver mais votos válidos · B. quem vencer o debate · C. quem tiver mais buscas no Google", size=17, gap=0)
e.ex("B2", "单选", "B", "sechs Staaten und der Bundesdistrikt",
     "Além da Presidência, há segundo turno para governador em... A. todos os estados · B. seis estados e no DF · C. dois estados", size=17, gap=0)
e.ex("B2", "单选", "C", "Record und SBT-Pool sagten ab",
     "Na reta final, os debates cancelados foram... A. o da Globo e o da Band · B. só o da Band · C. o da Record e o do pool do SBT", size=17, gap=0)
e.head("C · OS TEMPOS DO TEXTO", 25)
e.bridge("Ergänzen Sie die passende Verbform.")
e.ex("B2", "完成句子", "vencerá", "Zukunft: vencerá",
     "No domingo, ___ (vencer) o candidato com mais votos válidos.", instr="Ausfüllen", size=17, gap=0)
e.ex("B2", "完成句子", "tiver", "nach quem, Futuro do Subjuntivo: tiver",
     "Vence quem ___ (ter) mais votos válidos.", instr="Ausfüllen", size=17, gap=0)
e.ex("B2", "完成句子", "foram", "Vergangenheit Plural: foram cancelados",
     "Os debates da Record e do SBT ___ (ser) cancelados.", instr="Ausfüllen", size=17, gap=0)
e.ex("B2", "完成句子", "termina", "Präsens: termina",
     "Na sexta-feira, ___ (terminar) a propaganda eleitoral gratuita.", instr="Ausfüllen", size=17, gap=0)
e.head("D · AS PALAVRAS DO DEBATE", 25)
e.bridge("Setzen Sie die Wörter aus dem Kasten ein: segundo turno · maioria absoluta · votos válidos · intenção de voto")
e.ex("B2", "完成句子", "segundo turno", "segundo turno = Stichwahl",
     "A disputa final entre os dois mais votados é o ___.", instr="Ausfüllen", size=17, gap=0)
e.ex("B2", "完成句子", "votos válidos", "votos válidos = gültige Stimmen (ohne leere/ungültige)",
     "Só contam os ___: brancos e nulos ficam fora.", instr="Ausfüllen", size=17, gap=0)
e.ex("B2", "完成句子", "maioria absoluta", "maioria absoluta = absolute Mehrheit",
     "Vencer com mais da metade é vencer por ___.", instr="Ausfüllen", size=17, gap=0)
e.ex("B2", "完成句子", "intenção de voto", "Google-Suchen messen keine Wahlabsicht",
     "Busca no Google não mede ___.", instr="Ausfüllen", size=17, gap=0)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-aprofundamento.svg")
print("P6 saved, exercises so far:", len(REG))
