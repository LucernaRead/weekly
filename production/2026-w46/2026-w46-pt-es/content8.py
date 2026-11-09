# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　PRUEBA Y RESPUESTAS", "A Lucerna", "PÁGINA 8　La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Texto con huecos", "A", "El día 2 es el 15 de noviembre",
     "No domingo 15, o Brasil faz ___ do Enem. (A. o segundo dia · B. o primeiro dia)", size=14.5, gap=0)
f.ex("B1", "Texto con huecos", "B", "Cierre a las 13h",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Texto con huecos", "A", "Termina a las 18:30",
     "A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Texto con huecos", "A", "La Proclamación de la República es el 15 de noviembre",
     "A Proclamação da República é no dia ___ de novembro. (A. 15 · B. 20)", size=14.5, gap=0)
f.ex("B1", "Texto con huecos", "B", "La vuelta Vasco × Palmeiras es el día 8",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "Texto con huecos", "B", "El día 2 tiene 90 preguntas en total",
     "O dia 15 tem ___ questões. (A. 45 · B. 90)", size=14.5, gap=0)
f.ex("B1", "Texto con huecos", "A", "La prueba dura 5 horas",
     "No dia 15, a prova dura ___ . (A. cinco horas · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "Texto con huecos", "B", "El día 1 es el 8 de noviembre",
     "O primeiro dia do Enem foi no dia ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Opción múltiple", "B", "El festivo cae en domingo, el lunes no se recupera",
     "O feriado de 15 de novembro... A. dá folga na segunda · B. cai num domingo · C. muda o relógio", size=14.5, gap=0)
f.ex("A2", "Opción múltiple", "B", "La tarjeta de confirmación pertenece al Enem",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "Opción múltiple", "B", "La vuelta Atlético-MG × Grêmio es en la Arena MRV",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "Opción múltiple", "B", "La jornada 35 solo tiene un partido esta semana, el día 14",
     "A rodada 35 do Brasileirão, nesta semana... A. tem dez jogos · B. só tem Mirassol × Atlético-MG · C. já terminou", size=14.5, gap=0)
f.ex("B1", "Opción múltiple", "B", "La Proclamación de la República fue en 1889",
     "A Proclamação da República foi em... A. 1822 · B. 1889 · C. 1949", size=14.5, gap=0)
f.ex("A2", "Opción múltiple", "B", "El 11.11 es el día de las ofertas",
     "O 11.11 é... A. um feriado nacional · B. o dia das promoções · C. o dia do Enem", size=14.5, gap=0)
f.ex("B2", "Opción múltiple", "A", "300 es la duración de la prueba en minutos",
     "O número 300 mede... A. os minutos da prova · B. os dias do feriado · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "Opción múltiple", "A", "Deodoro fue el primer presidente",
     "Deodoro da Fonseca foi... A. o primeiro presidente · B. o último imperador · C. um jogador", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No domingo 15, ela faz o segundo dia do Enem. Na segunda, 9, ela revisa Natureza um pouco por dia. Na véspera, ela separa o documento e a caneta preta e dorme cedo. No domingo, ela chega ao local às 11h30, uma hora e meia antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "Opción múltiple", "B", "Marina vive en São Paulo",
     "Onde mora Marina? A. no Rio · B. em São Paulo · C. em Belo Horizonte", size=14.5, gap=0)
f.ex("A2", "Opción múltiple", "B", "Ella repasa un poco de ciencias de la naturaleza cada día",
     "O que Marina revisa na semana? A. só Matemática · B. Natureza, um pouco por dia · C. nada", size=14.5, gap=0)
f.ex("A2", "Opción múltiple", "B", "La víspera prepara el documento y el bolígrafo negro y se acuesta pronto",
     "Na véspera, Marina... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "Opción múltiple", "B", "Llega al centro de examen a las 11:30",
     "Marina chega ao local... A. às 13h30 · B. às 11h30 · C. às 18h30", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Formar frases", "Domingo é dia de prova.", "La palabra de tiempo va delante",
     "domingo / é / dia de prova → ___", instr="Forma una frase", size=14.5, gap=0)
f.ex("B1", "Formar frases", "A candidata confere o cartão no aplicativo.", "Sujeto + verbo + objeto + lugar",
     "a candidata / confere / o cartão / no aplicativo → ___", instr="Forma una frase", size=14.5, gap=0)
f.ex("B1", "Formar frases", "Que horas termina a prova?", "El grupo interrogativo va al principio",
     "que horas / termina / a prova / ? → ___", instr="Forma una frase", size=14.5, gap=0)
f.ex("B1", "Formar frases", "O Brasil comemora a Proclamação da República.", "Sujeto + verbo + objeto",
     "o Brasil / comemora / a proclamação / da república → ___", instr="Forma una frase", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Traducción", "El domingo 15 de noviembre es el segundo día del Enem.", "Mira el título de la página 6",
     "Domingo, 15 de novembro, é o segundo dia do Enem. → ___", instr="Traduce", size=14.5, gap=0)
f.ex("B1", "Traducción", "Comprueba la tarjeta antes del domingo.", "Confira = comprueba",
     "Confira o cartão antes do domingo. → ___", instr="Traduce", size=14.5, gap=0)
f.ex("B1", "Traducción", "O feriado cai num domingo.", "feriado = festivo",
     "«El festivo cae en domingo.» → ___", instr="Traduce", size=14.5, gap=0)
f.ex("B2", "Traducción", "Quando você chegar, apresente o documento com foto.", "Futuro de subjuntivo chegar + imperativo apresente",
     "Cuando llegues, muestra el documento con foto. → ___", instr="Traduce", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Emparejar vocabulario",
            ["a proclamação", "o portão", "a república", "a segunda chamada"],
            ["a forma do Estado depois de 1889",
             "o ato de anunciar uma mudança",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["proclamação = anunciar un cambio (b)", "portão = la entrada del centro de examen (d)", "república = la forma de Estado después de 1889 (a)", "segunda chamada = reentrada tras el cierre (no existe en el Enem) (c)"],
            instr="Empareja")
f.head("G　DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "Texto con huecos", "B", "documento com foto = documento con foto",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Texto con huecos", "A", "seção = el aula de examen (la sección)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Texto con huecos", "B", "Las puertas cierran a las 13h",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Texto con huecos", "A", "La prueba termina a las 18:30",
     "— A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Texto con huecos", "B", "obrigado = gracias",
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
f.bridge(f"Ejercicio de escritura (sin respuesta única); el texto modelo ({NWORDS} palabras) está abajo.")
f.ex("B1", "Escritura", "(ejercicio abierto: texto modelo abajo)", f"Mira el texto modelo en la parte H de esta página ({NWORDS} palabras)",
     "«O seu domingo 15 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="Escribe", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　RESPUESTAS — ordenadas por página; busca tu número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Una nota breve por respuesta　✓ = el ejercicio de escritura", 19.5, "sans", False, GREY, anchor="end")
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
