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
f.ex("B1", "完形单选", "B", "abrir el marcador = abrir o placar",
     "Doué ___ el marcador en París. (A. cerró · B. abrió)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "poner el 1–1 = fazer o 1–1 (o empate)",
     "Espart ___ el 1–1 para el Barça. (A. perdió · B. puso)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "de cabeza = de cabeça",
     "Lucas Hernández marcó el 2–1 de ___. (A. cabeza · B. penalti)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "volver a + infinitivo = outra vez…",
     "Yamal ___ a empatar: 2–2. (A. salió · B. volvió)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "cerrar el partido = fechar o jogo",
     "Vitinha y Fabián Ruiz ___ el 4–2 al final. (A. abrieron · B. cerraron)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "derrota = a derrota",
     "Fue la primera ___ del Barça este año. (A. victoria · B. derrota)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "no domingo joga-se o Clásico",
     "El domingo se juega el ___ en el Camp Nou. (A. Clásico · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "camiseta = a camisa",
     "El Barça lleva una ___ de GOLF WANG. (A. camiseta · B. bufanda)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "na madrugada de domingo, 03:00 vira 02:00",
     "El cambio: a las... A. 02→03 · B. 03→02 · C. 00→01", size=15.5, gap=1)
f.ex("A2", "单选", "A", "nas Canárias há uma hora a menos",
     "¿Dónde hay una hora menos? A. Canarias · B. Madrid · C. Barcelona", size=15.5, gap=1)
f.ex("A2", "单选", "C", "o Clásico e a F1 são às 21:00",
     "El domingo, 21:00: hay... A. solo fútbol · B. solo coches · C. los dos", size=15.5, gap=1)
f.ex("B1", "单选", "B", "na Castanyada comem-se panellets",
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", "单选", "A", "o Halloween é sábado, 31 de outubro",
     "Halloween es... A. sáb. 31.10 · B. dom. 1.11 · C. lun. 2.11", size=15.5, gap=1)
f.ex("B1", "单选", "C", "as eleições gerais são em 29 de novembro",
     "Las elecciones generales son el... A. 29.10 · B. 1.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "单选", "B", "as duas séries de pesquisas não se misturam",
     "¿Por qué no mezclamos las series? A. son secretas · B. métodos distintos · C. son viejas", size=15.5, gap=1)
f.ex("B1", "单选", "A", "a 1.ª tempestade com nome da temporada",
     "La DANA Adam es... A. la primera tormenta con nombre · B. una fiesta gallega · C. un equipo", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Lucía vive en Sevilla: el lunes 2 es festivo en Andalucía y hace puente. Marta vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El sábado por la noche, Marta celebra la Castanyada con sus amigos: castañas y panellets.", 16.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "a Andaluzia está na lista dos feriados",
     "¿Quién hace puente? A. Marta · B. Lucía · C. las dos", size=15.5, gap=1)
f.ex("A2", "单选", "A", "na Catalunha, a segunda é dia de trabalho",
     "El lunes 2, Marta... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", "单选", "C", "na Castanyada comem-se castanhas e panellets",
     "¿Qué comen Marta y sus amigos? A. flores · B. dulces de Halloween · C. castañas y panellets", size=15.5, gap=1)
f.ex("A2", "单选", "B", "o título resume o contraste entre os dois lugares",
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "造句", "El domingo dormimos una hora más.", "o tempo vem primeiro",
     "el domingo / dormimos / una hora más → ___", instr="Forme a frase", size=15.5, gap=1)
f.ex("A2", "造句", "El lunes es festivo en Madrid.", "sujeito + verbo + lugar",
     "el lunes / es festivo / en Madrid → ___", instr="Forme a frase", size=15.5, gap=1)
f.ex("B1", "造句", "El Clásico empieza a las nueve.", "a las nueve = às nove",
     "el Clásico / empieza / a las nueve → ___", instr="Forme a frase", size=15.5, gap=1)
f.ex("B1", "造句", "¿A qué hora empieza el partido?", "pergunta no começo",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Forme a frase", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "翻译", "No domingo dormimos uma hora a mais.", "Tradução (página 1)",
     "El domingo dormimos una hora más. → ___", instr="Traduza", size=15.5, gap=1)
f.ex("A2", "翻译", "Na segunda-feira é feriado em nove comunidades.", "Tradução (página 3)",
     "El lunes es festivo en nueve comunidades. → ___", instr="Traduza", size=15.5, gap=1)
f.ex("B1", "翻译", "El Clásico se juega el domingo a las nueve de la noche.", "se juega = joga-se, acontece",
     "O Clásico é no domingo às nove da noite. → ___", instr="Traduza", size=15.5, gap=1)
f.ex("B2", "翻译", "Cada gráfico tiene que llevar su fuente.", "tener que = ter de",
     "Cada gráfico tem de indicar a sua fonte. → ___", instr="Traduza", size=15.5, gap=1)
f.head("F　LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["el sondeo", "el indeciso", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "quien aún no sabe a quién votar"],
            ["c", "d", "b", "a"],
            ["sondeo = a pesquisa, c", "indeciso = o indeciso, d", "margen de error = a margem de erro, b", "junta electoral = a comissão eleitoral, a"],
            instr="Associe")
f.head("G　DIÁLOGO EN LA TIENDA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "A", "disfraz = a fantasia",
     "— Busco un ___ para mi hija. (A. disfraz · B. paraguas)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "Monster High faz sucesso com as crianças",
     "— Le encanta ___. (A. Monster High · B. el Samaín)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "¿cuánto cuesta? = quanto custa?",
     "— ¿Cuánto ___? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "pagar = pagar",
     "— ¿Cómo va a ___: con tarjeta o en efectivo? (A. pagar · B. votar)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "o Halloween é no sábado",
     "— Con tarjeta. La fiesta es el ___. (A. sábado · B. lunes)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.expl("Exercício de escrita (sem resposta única); o texto-modelo (82 palavras) está abaixo.")
f.ex("B1", "写作", "Questão aberta — texto-modelo abaixo, nesta página", "Texto-modelo na seção H desta página (82 palavras)",
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del 31 y del 1, y tu lunes.", instr="Escreva", size=15.5, gap=1)
MODELO = ("Vivo en Valencia, y aquí el lunes 2 de noviembre no es festivo: trabajo como un lunes normal. "
          "Mis amigos de Madrid sí hacen puente, ¡qué suerte! El sábado 31 celebro Halloween con mi familia, "
          "y el domingo llevamos flores al cementerio, como cada año. Por la tarde leo un libro en el sofá "
          "y preparo la semana con calma. El lunes, mientras Madrid descansa, yo abro la tienda a las nueve. "
          "No es justo… pero en diciembre, seguro, llega mi puente.")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPUESTAS　Respostas — por página, procure pelo número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Uma nota curta em português por exercício　✓ = exercício de escrita", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "写作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
