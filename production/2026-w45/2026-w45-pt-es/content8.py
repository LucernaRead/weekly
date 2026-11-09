# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　EVALUACIÓN Y RESPUESTAS", "A Lucerna", "Página 8　A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Cloze", "A", "El día 1 es el 8 de noviembre",
     "No domingo 8, o Brasil faz ___ do Enem. (A. o primeiro dia · B. o segundo dia)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "Cierre a las 13h",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "Empieza a las 13:30",
     "A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "Finados es el 2 de noviembre",
     "Finados é no dia ___ de novembro. (A. 2 · B. 15)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "El partido de vuelta Vasco × Palmeiras es el día 8",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "El puente festivo dura 3 días",
     "O feriadão tem ___ dias. (A. dois · B. três)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "El examen del día 8 dura cinco horas y media",
     "No dia 8, a prova dura ___ . (A. cinco horas e meia · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "El día 2 es el 15 de noviembre",
     "O segundo dia do Enem é no dia ___ . (A. 8 · B. 15)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Opción múltiple", "B", "El puente festivo va del 31 de octubre al 2 de noviembre",
     "O feriadão vai... A. de 8 a 15 · B. de 31 de outubro a 2 de novembro · C. de 2 a 5", size=14.5, gap=0)
f.ex("A2", "Opción múltiple", "B", "La tarjeta de confirmación es un documento del Enem",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "Opción múltiple", "B", "El partido de vuelta Atlético-MG × Grêmio es en la Arena MRV",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "Opción múltiple", "B", "La jornada 34 tiene partidos de lunes a viernes",
     "A rodada 34 do Brasileirão... A. é só no fim de semana · B. vai de segunda a sexta · C. já terminou", size=14.5, gap=0)
f.ex("B1", "Opción múltiple", "B", "En Finados, las familias llevan flores",
     "Em Finados, as famílias levam... A. fogos · B. flores · C. presentes", size=14.5, gap=0)
f.ex("A2", "Opción múltiple", "B", "Halloween fue el sábado 31 de octubre",
     "Halloween foi... A. no domingo 8 · B. no sábado, 31 de outubro · C. na segunda 2", size=14.5, gap=0)
f.ex("B2", "Opción múltiple", "A", "330 son los minutos del examen",
     "O número 330 mede... A. os minutos da prova · B. os dias do feriadão · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "Opción múltiple", "A", "Finados también se llama el Día de los Fieles Difuntos",
     "Finados, em português, também se chama... A. Dia dos Fiéis Defuntos · B. Dia da Independência · C. Dia do Trabalho", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Lucas mora em Belo Horizonte. No domingo 8, ele faz o Enem pela primeira vez. Na segunda, 2, ele descansa no feriadão e revisa um pouco por dia. Na véspera, ele separa o documento e a caneta preta e dorme cedo. No domingo, ele chega ao local às 11h, duas horas antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "Opción múltiple", "B", "Lucas vive en Belo Horizonte",
     "Onde mora Lucas? A. no Rio · B. em Belo Horizonte · C. em São Paulo", size=14.5, gap=0)
f.ex("A2", "Opción múltiple", "B", "Durante el puente festivo descansa y repasa un poco cada día",
     "O que Lucas faz no feriadão? A. só festa · B. descansa e revisa um pouco por dia · C. viaja para a praia", size=14.5, gap=0)
f.ex("A2", "Opción múltiple", "B", "La noche anterior prepara su documento y su bolígrafo negro y se acuesta temprano",
     "Na véspera, Lucas... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "Opción múltiple", "B", "Llega al lugar del examen a las 11h",
     "Lucas chega ao local... A. às 13h30 · B. às 11h · C. às 19h", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Construir frases", "Domingo é dia de prova.", "La palabra de tiempo va primero",
     "domingo / é / dia de prova → ___", instr="Forma la frase", size=14.5, gap=0)
f.ex("B1", "Construir frases", "O candidato confere o cartão no aplicativo.", "Sujeto + verbo + objeto + lugar",
     "o candidato / confere / o cartão / no aplicativo → ___", instr="Forma la frase", size=14.5, gap=0)
f.ex("B1", "Construir frases", "Que horas começa a prova?", "La expresión interrogativa va al inicio",
     "que horas / começa / a prova / ? → ___", instr="Forma la frase", size=14.5, gap=0)
f.ex("B1", "Construir frases", "O Brasil lembra os seus mortos.", "Sujeto + verbo + objeto",
     "o Brasil / lembra / os seus mortos → ___", instr="Forma la frase", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Traducción", "El domingo 8 de noviembre es el primer día del Enem.", "Véase el titular de la página 6",
     "Domingo, 8 de novembro, é o primeiro dia do Enem. → ___", instr="Traduce", size=14.5, gap=0)
f.ex("B1", "Traducción", "Comprueba tu tarjeta antes del domingo.", "Confira = comprueba",
     "Confira o cartão antes do domingo. → ___", instr="Traduce", size=14.5, gap=0)
f.ex("B1", "Traducción", "O feriadão é de 31 de outubro a 2 de novembro.", "feriadão = el puente festivo",
     "“El puente festivo va del 31 de octubre al 2 de noviembre.” → ___", instr="Traduce", size=14.5, gap=0)
f.ex("B2", "Traducción", "Quando você chegar, apresente o documento com foto.", "futuro de subjuntivo chegar + imperativo apresente",
     "Cuando llegues, presenta tu documento con foto. → ___", instr="Traduce", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Emparejar vocabulario",
            ["o feriadão", "o portão", "a reta final", "a segunda chamada"],
            ["a última semana antes da prova",
             "um feriado grudado no fim de semana",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["feriadão = un festivo junto al fin de semana: b", "portão = la entrada del lugar del examen: d", "reta final = la última semana antes del examen: a", "segunda chamada = una nueva entrada tras el cierre (que no existe en el Enem): c"],
            instr="Relaciona")
f.head("G　DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "Cloze", "B", "documento com foto = documento con foto",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "sección = la zona del examen (la sala)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "Las puertas cierran a las 13h",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "A", "El examen empieza a las 13:30",
     "— A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Cloze", "B", "obrigado = gracias",
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
f.bridge(f"Ejercicio de escritura (sin respuesta única); el texto modelo ({NWORDS} palabras) está abajo.")
f.ex("B1", "Escritura", "(pregunta abierta)", f"el texto modelo está en la sección H: {NWORDS} palabras",
     "«O seu domingo 8 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="Escribe", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　RESPUESTAS — ordenadas por página, busca el número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Una nota breve en español para cada respuesta　✓ = el texto modelo", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Escritura":
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
