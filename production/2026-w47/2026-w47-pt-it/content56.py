# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JOVENS (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JOVENS　Giovani", "A Lucerna", "NÍVEL B1　Depois do Enem: a espera começa　Dopo l'esame: comincia l'attesa")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Depois do Enem: a espera começa", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: B1")
f.para("No domingo 15, milhões de estudantes fazem o segundo dia do Enem — Ciências da Natureza e Matemática, das 13h30 às 18h30, 90 questões em cinco horas. Depois da prova, começa a outra parte do exame: a espera pelo gabarito.")
f.para("O que sai primeiro são os gabaritos extraoficiais: na noite do domingo, professores e cursinhos publicam as respostas que eles mesmos montam. Servem para estimar o desempenho — mas não valem como correção oficial.")
f.para("O gabarito oficial é do Inep: o edital diz que ele sai até o 10º dia útil depois do segundo dia de prova. Na prática, é no fim de novembro — e a nota individual só sai em janeiro de 2027. E atenção: o número de acertos não é a nota: o Enem usa a TRI, que pesa a coerência das respostas e a dificuldade das questões.")
f.para("E a semana dos jovens tem mais: sexta, 20, é feriado — um dia para descansar, ler e conversar sobre a Consciência Negra. No sábado, 21, Palmeiras × Flamengo, às 16h30. E na sexta, 27, a Black Friday: compare preços antes de comprar.")
f.box("O PLANO DA ESPERA", [
    ("1. Anote as suas respostas antes de sair da prova (appunta le tue risposte prima di uscire dall'aula)", "serif", False, INK, 21, 1.36),
    ("2. Confira as respostas extraoficiais na noite do dia 15 (controlla le soluzioni ufficiose la sera del 15)", "serif", False, INK, 21, 1.36),
    ("3. Espere o gabarito oficial no portal do Inep (aspetta la soluzione ufficiale sul sito dell'Inep)", "serif", False, INK, 21, 1.36),
    ("4. Não confunda acertos com nota: a TRI decide (il numero di risposte giuste non è il voto: TRI decide)", "serif", False, INK, 21, 1.36),
    ("5. Descanse no feriado: a cabeça agradece (riposa bene durante la festa: il tuo cervello ti ringrazierà)", "serif", False, INK, 21, 1.36),
])
f.gloss("o gabarito la soluzione · oficial ufficiale · extraoficial ufficioso · a espera l'attesa · a nota il voto · pesar soppesare.")
f.end_report()

# col 3: facts + e você + estudo.jpg (sequential)
ix = COLX[3]
facts = ["Mais de 5 milhões de inscritos no Enem 2026 (Inep).",
         "O gabarito oficial sai até o 10º dia útil depois do dia 15.",
         "A nota individual sai em janeiro de 2027."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "OS JOVENS EM NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E você? Na noite da prova, você confere o gabarito ou prefere esperar? Escreva duas frases em português."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("La sera dell'esame, controlli le risposte o preferisci aspettare? Scrivi due frasi e inviale.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E VOCÊ?　Parla di te", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "La sera dell'esame, controlli le risposte o preferisci aspettare? Scrivi due frasi e inviale.", 20, "sans", False, GREY, CW - 44, 1.42)
iy3 = ey3 + eh + 26
image(p, "estudo.jpg", ix, iy3, CW, 280)
caption(p, ix, iy3 + 280, CW,
        "Estudantes em uma biblioteca: depois do segundo dia do Enem, a espera continua até o gabarito oficial.",
        "Foto: Gary Todd / Wikimedia Commons — CC0")
print("P5 col3 ends", iy3 + 280 + 110)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　ESERCIZI DI PAGINA 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　I livelli sono misti — cerca le risposte per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　COMPREENSÃO", 25)
e.bridge("Leggi l'articolo di pagina 5 e scegli la risposta corretta.")
e.ex("B1", "Scelta multipla", "B", "Il secondo giorno sono scienze della natura e matematica, 13:30 a 18:30",
     "No domingo 15, a prova tem... A. redação · B. Natureza e Matemática, das 13h30 às 18h30 · C. só Linguagens", size=20, gap=8)
e.ex("B1", "Scelta multipla", "B", "Le soluzioni ufficiose escono la sera dell'esame, preparate dalle scuole private",
     "Os gabaritos extraoficiais saem... A. em janeiro · B. na noite do dia 15, feitos por cursinhos · C. no portal do Inep", size=20, gap=8)
e.ex("B1", "Scelta multipla", "A", "La soluzione ufficiale è pubblicata dall'Inep prima della fine di novembre",
     "O gabarito oficial é do Inep e sai... A. até o fim de novembro · B. na noite do dia 15 · C. em janeiro de 2027", size=20, gap=8)
e.ex("B1", "Scelta multipla", "B", "Il numero di risposte giuste non è il voto, TRI decide il voto",
     "O número de acertos... A. é a nota final · B. não é a nota: a TRI decide · C. não importa", size=20, gap=8)
e.ex("B1", "Scelta multipla", "B", "I voti individuali non escono prima di gennaio 2027",
     "A nota individual sai... A. na noite do dia 15 · B. em janeiro de 2027 · C. no dia 20", size=20, gap=8)
e.head("B　AS PALAVRAS DO TEXTO", 25)
e.bridge("Completa con le parole del riquadro.")
e.para("gabarito · oficial · extraoficial · espera · nota · pesar", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Completa la frase", "gabarito", "gabarito = la soluzione",
     "Depois da prova, começa a espera pelo ___.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "oficial", "oficial = ufficiale",
     "O gabarito ___ é do Inep.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "extraoficiais", "extraoficial concordanza al plurale: extraoficiais",
     "Os gabaritos ___ saem na noite do domingo.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "espera", "espera = l'attesa",
     "Depois da prova, começa a ___.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "nota", "nota = il voto",
     "O número de acertos não é a ___.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "pesa", "pesar, presente, forma di ela: pesa",
     "A TRI ___ a coerência das respostas.", instr="Completa", size=20, gap=8)
e.head("C　O FUTURO DO PRESENTE", 25)
e.bridge("Completa al futuro (futuro do presente).")
e.ex("B1", "Completa la frase", "sairá", "sair futuro: sairá",
     "O gabarito oficial ___ (sair) até o fim de novembro.", instr="Completa", size=20, gap=8)
e.ex("B1", "Completa la frase", "publicarão", "publicar, futuro, forma di eles: publicarão",
     "Os cursinhos ___ (publicar) as respostas na noite do dia 15.", instr="Completa", size=20, gap=8)
e.ex("B2", "Completa la frase", "decidirá", "decidir futuro: decidirá",
     "A TRI ___ (decidir) a nota de cada candidato.", instr="Completa", size=20, gap=8)
e.ex("B2", "Completa la frase", "chegará", "chegar futuro: chegará",
     "A Black Friday ___ (chegar) na sexta, dia 27.", instr="Completa", size=20, gap=8)
e.head("D　VERDADEIRO OU FALSO?", 25)
e.ex("B1", "Vero o falso", "Verdadeiro", "Vero: le soluzioni ufficiose servono solo a stimare il tuo livello",
     "Os gabaritos extraoficiais servem para estimar o desempenho. Verdadeiro ou falso?", instr="Vero o falso?", size=20, gap=8)
e.ex("B1", "Vero o falso", "Falso", "Falso: la soluzione ufficiale è pubblicata dall'Inep, non dalle scuole private",
     "O gabarito oficial é publicado pelos cursinhos. Verdadeiro ou falso?", instr="Vero o falso?", size=20, gap=8)
e.ex("B2", "Vero o falso", "Verdadeiro", "Vero: TRI valuta la coerenza delle tue risposte e la difficoltà delle domande",
     "A TRI pesa a coerência das respostas e a dificuldade das questões. Verdadeiro ou falso?", instr="Vero o falso?", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jovens.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · APROFUNDAMENTO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("APROFUNDAMENTO　In profondità", "A Lucerna", "NÍVEL B2　O gabarito explicado　La soluzione ufficiale, spiegata")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1520, tag="P6-main")
f.title("O gabarito explicado: como funciona a espera", 32)
f.byline("Da redação da A Lucerna　Nível de leitura: B2")
f.para("O Enem 2026 tem dois domingos: 8 e 15 de novembro. No dia 8: redação, Linguagens e Ciências Humanas, das 13h30 às 19h. No dia 15: Natureza e Matemática, das 13h30 às 18h30. Esta edição cobre a espera que começa depois do segundo domingo.")
f.para("O edital (nº 64/2026) fixa um prazo, não uma data: os gabaritos das provas objetivas saem «até o 10º dia útil após o 2º dia de aplicação». Contar dias úteis não é contar dias: sábados e domingos não contam — e o feriado do dia 20 também não conta.")
f.para("Por isso as contas variam: com o feriado de 20 de novembro na conta, o 10º dia útil cai no fim do mês — entre 27 e 30 de novembro, conforme a contagem. O Inep pode publicar antes do prazo. O caminho é o portal do Inep, na página de Provas e Gabaritos.")
f.para("E depois do gabarito, a nota: a TRI — a Teoria de Resposta ao Item — calcula a nota pela coerência das respostas. Dois candidatos com o mesmo número de acertos podem ter notas diferentes: a TRI olha quais questões cada um acertou. A regra de ouro não muda: primeiro as fáceis, depois as difíceis, e tempo guardado para revisar no fim.")
f.gloss("o prazo la scadenza · o dia útil giorno lavorativo · contar contare · a coerência la coerenza · o chute una risposta a caso.")
f.end_report()

# col 3: timeline + ler os números (sequential, measured)
bx = COLX[3]
p.rect(bx, 200, CW, 654, fill=BOX)  # fix1 (2026-11-11): 640->654 (+14). Last line 'Página do Participante.' baseline sat 0.8px below the old bottom 840, descenders ~4.8px out; +14 gives ink-bottom clearance ~+9px. Next box top (by3=866) is fixed, gap narrows 26->12px.
p.text(bx + 22, 240, "O CAMINHO ATÉ O GABARITO", 22, "sans", True, OLIVE)
steps = [
    ("8 NOV.", "Primeiro dia do Enem: redação, Linguagens e Humanas."),
    ("15 NOV.", "Segundo dia: Natureza e Matemática."),
    ("16 NOV.", "Começa a contagem dos dias úteis."),
    ("20 NOV.", "Feriado nacional — não conta na conta."),
    ("27–30 NOV.", "O prazo do gabarito oficial."),
    ("JAN. 2027", "A nota individual sai na Página do Participante."),
]
sy3 = 282
for w, t in steps:
    p.text(bx + 22, sy3 + 21, w, 20, "sans", True, OLIVE)
    sy3 = p.para(bx + 164, sy3 + 21, t, 21, "serif", False, INK, CW - 186, 1.4) + 16
by3 = 866
bb = ("Diante de um número, faça três perguntas: quem publica? Quando? "
      "É busca, prova ou pesquisa? Sem essas respostas, um número diz pouco.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f0eee5")
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LER OS NÚMEROS", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh)

# ---- charts: a contagem dos dias úteis + dois gabaritos ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, OLIVE, 2)
p.text(MX, gy + 10, "O FIM DE NOVEMBRO EM NÚMEROS　Le cifre di fine novembre (Edital nº 64/2026 do Inep)", 26, "sans", True, OLIVE)
bw_ = 2 * CW + GUT
# left box: a contagem (dias corridos 16-30 = 15: 10 úteis + 5 de folga)
bx1 = MX
p.rect(bx1, gy + 28, bw_, 322, fill=BOX)
p.text(bx1 + 22, gy + 68, "A CONTAGEM　do dia 16 ao dia 30", 21, "sans", True, INK)
contagem = [("dias úteis", 10), ("fins de semana e feriado", 5)]
yy = gy + 100
for lab, v in contagem:
    p.text(bx1 + 22, yy + 24, lab, 20, "serif", True, INK)
    labw = text_w(lab, "serif", True, 20)
    p.rect(bx1 + 40 + labw, yy + 6, v * 30, 22, fill=OLIVE)
    p.text(bx1 + 58 + labw + v * 30, yy + 24, f"{v} dias", 20.5, "serif", False, INK)
    yy += 44
p.para(bx1 + 22, gy + 248, "Dias de 16 a 30 de novembro: 10 úteis + 5 de folga = 15 dias. O 10º dia útil é o prazo do gabarito.", 19.5, "serif", False, INK, bw_ - 44, 1.4)
p.para(bx1 + 22, gy + 322 - 12, "Fonte: Edital nº 64/2026 — «até o 10º dia útil após o 2º dia».", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right box: dois gabaritos
bx2 = COLX[2]
p.rect(bx2, gy + 28, bw_, 322, fill=BOX)
p.text(bx2 + 22, gy + 68, "DOIS GABARITOS　um exame", 21, "sans", True, INK)
doms = [
    "Extraoficial — na noite do dia 15, feito por cursinhos.",
    "Extraoficial — estima o desempenho, não vale como correção.",
    "Oficial — do Inep, até o fim de novembro.",
    "Oficial — é a base da correção das objetivas.",
]
yy = gy + 100
for t in doms:
    p.text(bx2 + 22, yy + 24, t, 20, "serif", False, INK)
    yy += 40
p.para(bx2 + 22, gy + 322 - 34, "Fonte: Inep — o resultado individual sai em janeiro de 2027.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)

# ---- P6 exercises ----
ey = 1930
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCÍCIOS　ESERCIZI DI PAGINA 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　I livelli sono misti — cerca le risposte per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LER OS GRÁFICOS", 25)
e.bridge("Guarda i due grafici qui sopra e scegli la risposta corretta.")
e.ex("B2", "Scelta multipla", "B", "16–30 novembre: 15 giorni in tutto",
     "De 16 a 30 de novembro são... A. 10 dias · B. 15 dias · C. 20 dias", size=17, gap=0)
e.ex("B2", "Scelta multipla", "A", "Giorni lavorativi: 10",
     "Na contagem, os dias úteis são... A. 10 · B. 5 · C. 15", size=17, gap=0)
e.ex("B2", "Scelta multipla", "B", "Fine settimana e festa: 5 giorni",
     "Os fins de semana e o feriado são... A. 10 dias · B. 5 dias · C. 15 dias", size=17, gap=0)
e.ex("B2", "Scelta multipla", "B", "10 + 5 = 15",
     "10 + 5 = ... A. 12 · B. 15 · C. 20", size=17, gap=0)
e.ex("B2", "Scelta multipla", "B", "Il decimo giorno lavorativo è la scadenza della soluzione ufficiale",
     "O 10º dia útil é... A. o dia da prova · B. o prazo do gabarito · C. a nota final", size=17, gap=0)
e.ex("B2", "Scelta multipla", "A", "La soluzione ufficiosa è preparata dalle scuole private la sera dell'esame",
     "O gabarito extraoficial é... A. feito por cursinhos, na noite do dia 15 · B. publicado pelo Inep · C. a nota final", size=17, gap=0)
e.head("B　COMPREENSÃO", 25)
e.ex("B2", "Scelta multipla", "B", "L'Enem si svolge in due domeniche: 8 e 15",
     "O Enem tem... A. um só domingo · B. dois domingos: 8 e 15 · C. três domingos", size=17, gap=0)
e.ex("B2", "Scelta multipla", "B", "Il secondo giorno sono scienze della natura e matematica",
     "No dia 15, a prova tem... A. redação · B. Natureza e Matemática · C. só Matemática", size=17, gap=0)
e.ex("B2", "Scelta multipla", "B", "I fine settimana e la festa non contano come giorni lavorativi",
     "Na contagem dos dias úteis... A. tudo conta · B. sábados, domingos e o feriado não contam · C. só o feriado conta", size=17, gap=0)
e.ex("B2", "Scelta multipla", "B", "I voti individuali escono a gennaio 2027",
     "A nota individual sai... A. em novembro · B. em janeiro de 2027 · C. no dia 15", size=17, gap=0)
e.head("C　OS TEMPOS DO TEXTO", 25)
e.bridge("Completa con la forma verbale corretta secondo il senso della frase.")
e.ex("B2", "Completa la frase", "serão", "futuro: serão",
     "Os gabaritos ___ (ser) publicados até o fim de novembro.", instr="Completa", size=17, gap=0)
e.ex("B2", "Completa la frase", "contam", "presente: contam",
     "Os fins de semana não ___ (contar) na conta.", instr="Completa", size=17, gap=0)
e.ex("B2", "Completa la frase", "fixa", "presente: fixa",
     "O edital ___ (fixar) um prazo, não uma data.", instr="Completa", size=17, gap=0)
e.ex("B2", "Completa la frase", "pesa", "presente: pesa",
     "A TRI ___ (pesar) a coerência das respostas.", instr="Completa", size=17, gap=0)
e.head("D　AS PALAVRAS DA PROVA", 25)
e.bridge("Completa con le parole del riquadro: prazo · dia útil · coerência · chute")
e.ex("B2", "Completa la frase", "prazo", "prazo = la scadenza",
     "O edital fixa um ___, não uma data.", instr="Completa", size=17, gap=0)
e.ex("B2", "Completa la frase", "dia útil", "dia útil = giorno lavorativo",
     "O gabarito sai até o 10º ___ depois do dia 15.", instr="Completa", size=17, gap=0)
e.ex("B2", "Completa la frase", "coerência", "coerência = la coerenza",
     "A TRI olha a ___ das respostas.", instr="Completa", size=17, gap=0)
e.ex("B2", "Completa la frase", "chute", "chute = una risposta a caso",
     "Um ___ certo vale menos do que um acerto consistente.", instr="Completa", size=17, gap=0)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-aprofundamento.svg")
print("P6 saved, exercises so far:", len(REG))
