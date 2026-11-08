# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P8: 38 exercises + registry-generated answers. Dash style, as W45.
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
f.ex("B1", "Escolha no texto", "B", "visita a Chequia = visita à Chéquia",
     "El jueves, la Roja ___ a Chequia en Praga. (A. recibe · B. visita)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "B", "recibir a Inglaterra = receber a Inglaterra em casa",
     "El domingo, España ___ a Inglaterra en Madrid. (A. visita · B. recibe)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "la lista = lista de convocados",
     "De la Fuente dio ___ el viernes 6. (A. la lista · B. la huelga)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "B", "la huelga dura 24 horas = a greve dura 24 horas",
     "La huelga del miércoles ___ 24 horas. (A. empieza · B. dura)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "empieza la campaña = começa a campanha",
     "El viernes 13 ___ la campaña electoral. (A. empieza · B. termina)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "B", "el sobre = envelope",
     "El voto por correo llega en un ___. (A. puente · B. sobre)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "Espanha–Inglaterra no domingo",
     "El domingo se juega el ___ en el Metropolitano. (A. España–Inglaterra · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "veranillo = veranico",
     "En noviembre llega el ___ de San Martín. (A. veranillo · B. puente)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Escolha múltipla", "B", "A greve geral é quarta, 11 de novembro",
     "La huelga general es el... A. lunes 9 · B. miércoles 11 · C. viernes 13", size=15.5, gap=1)
f.ex("A2", "Escolha múltipla", "A", "São Martinho, 11 de novembro",
     "San Martín es el... A. 11 de noviembre · B. 12 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "Escolha múltipla", "C", "Espanha–Inglaterra e greve, ambos esta semana",
     "Esta semana hay... A. solo fútbol · B. solo huelga · C. la huelga y el España–Inglaterra", size=15.5, gap=1)
f.ex("B1", "Escolha múltipla", "B", "No magosto comem-se castanhas assadas",
     "¿Qué se come en el magosto? A. flan · B. castañas asadas · C. chocolate", size=15.5, gap=1)
f.ex("B1", "Escolha múltipla", "A", "Lema da greve: salários, moradia, preços",
     "El lema de la huelga es... A. «Salarios, vivienda y precios» · B. «Fútbol y fiesta» · C. «Cine y series»", size=15.5, gap=1)
f.ex("B1", "Escolha múltipla", "C", "As eleições são em 29 de novembro",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "Escolha múltipla", "B", "Barômetro de habitação do CIS: 86,9% preocupados",
     "Según el CIS de vivienda, está preocupado el... A. 13,5 % · B. 86,9 % · C. 79 %", size=15.5, gap=1)
f.ex("B1", "Escolha múltipla", "A", "A campanha começa em 13 de novembro",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el miércoles 11 sigue la huelga en las noticias y el domingo ve el España–Inglaterra en el Metropolitano. Ana vive en Barcelona: el miércoles 11 trabaja, y el domingo ve el partido por televisión. Los dos leen los programas antes de votar el 29.", 16.5, lh=1.3, split=False)
f.ex("A2", "Escolha múltipla", "B", "Pablo vai ao Metropolitano no domingo",
     "¿Quién ve el partido en el Metropolitano? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "Escolha múltipla", "A", "Ana trabalha na quarta",
     "El miércoles 11, Ana... A. trabaja · B. va a la huelga · C. duerme", size=15.5, gap=1)
f.ex("A2", "Escolha múltipla", "A", "Os dois leem os programas antes de votar",
     "Antes de votar, los dos... A. leen los programas · B. ven «Infamia» · C. viajan a Praga", size=15.5, gap=1)
f.ex("A2", "Escolha múltipla", "B", "O título resume o contraste entre dois lugares",
     "El mejor título es... A. «Una tormenta» · B. «Dos miércoles» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Formar frases", "El miércoles hay huelga general.", "Sujeito + verbo + lugar",
     "el miércoles / hay / huelga general → ___", instr="Forme a frase", size=15.5, gap=1)
f.ex("A2", "Formar frases", "El domingo vemos el España–Inglaterra.", "O tempo antes",
     "el domingo / vemos / el España–Inglaterra → ___", instr="Forme a frase", size=15.5, gap=1)
f.ex("B1", "Formar frases", "La campaña empieza a las cero horas.", "a las cero horas = à meia-noite",
     "la campaña / empieza / a las cero horas → ___", instr="Forme a frase", size=15.5, gap=1)
f.ex("B1", "Formar frases", "¿A qué hora empieza el partido?", "A palavra interrogativa no início",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Forme a frase", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Tradução", "Quarta, greve geral em toda a Espanha.", "Compare com o original.",
     "El miércoles hay huelga general en toda España. → ___", instr="Traduza", size=15.5, gap=1)
f.ex("A2", "Tradução", "Domingo assistimos a Espanha–Inglaterra.", "Compare com o original.",
     "El domingo vemos el España–Inglaterra. → ___", instr="Traduza", size=15.5, gap=1)
f.ex("B1", "Tradução", "El voto por correo llega a casa.", "llegar a casa = chegar em casa",
     "O voto pelo correio chega em casa. → ___", instr="Traduza", size=15.5, gap=1)
f.ex("B2", "Tradução", "Cada gráfico tiene que llevar su fuente.", "tener que = ter de",
     "Todo gráfico deve indicar a fonte. → ___", instr="Traduza", size=15.5, gap=1)
f.head("F　LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "Associar palavras",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo=pesquisa c", "muestra=amostra d", "margen de error=margem de erro b", "junta electoral=comissão eleitoral a"],
            instr="Associe")
f.head("G　DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "Escolha no texto", "A", "alquiler = aluguel",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "tres habitaciones = três quartos",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "¿cuánto cuesta? = quanto custa?",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "firmar = assinar (um contrato)",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "Escolha no texto", "A", "mudanza = mudança",
     "— La ___ es el miércoles 11, día de huelga. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("Questão de redação (sem resposta única); o texto modelo (84 palavras) está abaixo.")
f.ex("B1", "Escrita", "Questão aberta — texto modelo abaixo, nesta página", "Texto modelo na seção H desta página (84 palavras)",
     "«¿Qué harías tú por la vivienda?» Escribe 80–100 palabras: tu plan del miércoles 11, tu domingo 15 y tu voto del 29.", instr="Escreva", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y el miércoles 11 sigo la huelga en las noticias: salarios, vivienda y precios, los tres temas de la semana. "
          "El viernes 13 empieza la campaña, y el domingo 15 veo el España–Inglaterra con mi familia. "
          "El jueves 12 veo el Chequia–España en Praga por televisión, a las 20:45. "
          "Mis amigos de Barcelona no tienen huelga en su empresa: el miércoles trabajan. Yo, en cambio, leo los programas con calma y preparo mi voto por correo. "
          "El 29 votamos. ¡Qué semana!")
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
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.12, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Escrita":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.2, lh=1.12, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
