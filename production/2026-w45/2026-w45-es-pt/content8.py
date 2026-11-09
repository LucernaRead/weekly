# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS　EXERCÍCIOS E RESPOSTAS", "La Lucerna", "PÁGINA 8　La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "Escolha no texto", "B", "ganó 2–1 = venceu por 2–1",
     "El Madrid ___ 2–1 en el Camp Nou. (A. perdió · B. ganó)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "B", "marcar dos goles = marcar dois golos",
     "Mbappé ___ dos goles en Barcelona. (A. paró · B. marcó)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "primera derrota liguera = primeira derrota na Liga",
     "Fue la primera ___ del Barça en la Liga. (A. derrota · B. victoria)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "B", "recortar = reduzir a diferença",
     "El Madrid ___ la distancia a tres puntos. (A. aumentó · B. recortó)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "acoger = receber (o Bernabéu recebe a NFL)",
     "El Bernabéu ___ un partido de la NFL. (A. acoge · B. cierra)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "B", "el emparrillado = o campo de futebol americano",
     "El Bernabéu cambia el césped por el ___. (A. puente · B. emparrillado)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "no domingo há Atlético–Barça",
     "El domingo se juega el ___ en el Metropolitano. (A. Atlético–Barça · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "himno = o hino",
     "Antes del partido suenan dos ___: el de España y el de EE. UU. (A. himnos · B. puentes)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Escolha múltipla", "B", "nove comunidades têm feriado na segunda",
     "El lunes 2 es fiesta en... A. todas · B. nueve comunidades · C. ninguna", size=15.5, gap=1)
f.ex("A2", "Escolha múltipla", "A", "o Dia de Todos os Santos é 1 de novembro",
     "Todos los Santos es el... A. 1 de noviembre · B. 2 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "Escolha múltipla", "C", "o Atlético–Barça e a NFL são ambos no domingo",
     "El domingo 8 hay... A. solo fútbol · B. solo NFL · C. la NFL y el Atlético–Barça", size=15.5, gap=1)
f.ex("B1", "Escolha múltipla", "B", "na Castanyada comem-se panellets",
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", "Escolha múltipla", "A", "atos da DANA: quinta, 29 de outubro",
     "Los actos de memoria de la DANA fueron el... A. jueves 29 de octubre · B. sábado 31 · C. lunes 2", size=15.5, gap=1)
f.ex("B1", "Escolha múltipla", "C", "as eleições são no dia 29 de novembro",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "Escolha múltipla", "B", "no CIS de outubro: a habitação, 55,7%",
     "Según el CIS de octubre, la vivienda es el principal problema para el... A. 20,9 % · B. 55,7 % · C. 17,1 %", size=15.5, gap=1)
f.ex("B1", "Escolha múltipla", "A", "a campanha começa no dia 13 de novembro",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el lunes 2 es festivo en su comunidad y hace puente. Ana vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El domingo por la tarde, Ana ve la NFL en televisión; por la noche, Pablo ve el Atlético–Barça.", 16.5, lh=1.3, split=False)
f.ex("A2", "Escolha múltipla", "B", "Madrid está na lista de feriados",
     "¿Quién hace puente? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "Escolha múltipla", "A", "na Catalunha, a segunda é dia de trabalho",
     "El lunes 2, Ana... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", "Escolha múltipla", "A", "Ana: só a NFL; Pablo: Atlético–Barça à noite",
     "El domingo, Ana ve... A. solo la NFL · B. solo el Barça · C. la NFL y, por la noche, el Atlético–Barça", size=15.5, gap=1)
f.ex("A2", "Escolha múltipla", "B", "o título resume o contraste entre os dois lugares",
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Formar frases", "El lunes es festivo en Madrid.", "sujeito + verbo + lugar",
     "el lunes / es festivo / en Madrid → ___", instr="Forme a frase", size=15.5, gap=1)
f.ex("A2", "Formar frases", "El domingo vemos la NFL en el Bernabéu.", "tempo em 1.º",
     "el domingo / vemos / la NFL / en el Bernabéu → ___", instr="Forme a frase", size=15.5, gap=1)
f.ex("B1", "Formar frases", "El Atlético–Barça empieza a las nueve.", "a las nueve = às 9h",
     "el Atlético–Barça / empieza / a las nueve → ___", instr="Forme a frase", size=15.5, gap=1)
f.ex("B1", "Formar frases", "¿A qué hora empieza el partido?", "interrogativa no início",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Forme a frase", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Tradução", "Na segunda-feira é feriado em nove comunidades.", "Confira no original",
     "El lunes es festivo en nueve comunidades. → ___", instr="Traduza", size=15.5, gap=1)
f.ex("A2", "Tradução", "No domingo vemos a NFL e o Atlético–Barça.", "Confira no original",
     "El domingo vemos la NFL y el Atlético–Barça. → ___", instr="Traduza", size=15.5, gap=1)
f.ex("B1", "Tradução", "El Bernabéu acoge un partido de la NFL.", "acoger = receber",
     "O Bernabéu recebe um jogo da NFL. → ___", instr="Traduza", size=15.5, gap=1)
f.ex("B2", "Tradução", "Cada gráfico tiene que llevar su fuente.", "tener que = ter de",
     "Cada gráfico tem de indicar a sua fonte. → ___", instr="Traduza", size=15.5, gap=1)
f.head("F　LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "Associar palavras",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo=sondagem c", "muestra=amostra d", "margen de error=margem de erro b", "junta electoral=comissão eleitoral a"],
            instr="Associe")
f.head("G　DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "Escolha no texto", "A", "alquiler = o aluguer",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "tres habitaciones = três quartos",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "¿cuánto cuesta? = quanto custa?",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "firmar = assinar (o contrato)",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "mudanza = a mudança",
     "— La ___ es el lunes 2, que es fiesta. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("Questão de redação (sem resposta única); o texto-modelo (84 palavras) segue abaixo.")
f.ex("B1", "Escrita", "Questão aberta — texto-modelo abaixo, nesta página", "Texto-modelo na seção H desta página (84 palavras)",
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del puente y tu domingo 8.", instr="Escreva", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y aquí el lunes 2 de noviembre sí es festivo: hago puente con mi familia. "
          "El sábado 7 vemos el Valencia–Real Madrid en televisión, y el domingo 8 tenemos dos citas: por la tarde, la NFL en el Bernabéu, y por la noche, el Atlético–Barça. "
          "Mis amigos de Barcelona no tienen puente: el lunes trabajan. Yo, en cambio, descanso un día más y preparo la semana con calma. "
          "El viernes 13 empieza la campaña, y el 29 votamos todos. ¡Qué mes!")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPUESTAS　Respostas — por página, procure pelo número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Cada resposta traz uma breve nota　✓ marca a questão de redação", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Escrita":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
