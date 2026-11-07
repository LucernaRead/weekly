# -*- coding: utf-8 -*-
"""Generate W46 NL x ES transform.py from the EN rep pairs (/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-reps.txt).
ES precedent (W45 NL x ES): type tokens stay Chinese (registry-only, never
printed); only instr words localised. Badge INSERTED y=568, strapline kept.
P8 keys 13.0/1.12/0.4, Flow/separator at core values. Glosses/bridges use
': ' separators; P8 notes use ' = '. Disclosure variable renamed dt_zh->dt_es."""
import re

lines = open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-reps.txt", encoding="utf-8").read().splitlines()
pairs = []
i = 0
while i < len(lines):
    m = re.match(r"^(\S+)\tOLD\t(.*)$", lines[i])
    if not m:
        i += 1
        continue
    m2 = re.match(r"^(\S+)\tNEW\t(.*)$", lines[i + 1])
    assert m2 and m2.group(1) == m.group(1), (i, lines[i], lines[i + 1])
    pairs.append((m.group(1), m.group(2), m2.group(2)))
    i += 2
assert len(pairs) == 265, len(pairs)

ES_MAP = {
    "ELKE WEEK IN HET NEDERLANDS · EVERY WEEK · REAL DUTCH":
        "ELKE WEEK IN HET NEDERLANDS · CADA SEMANA EN NEERLANDÉS",
    "WEEKBLAD IN HET NEDERLANDS · VOL.3 · SINTERKLAAS · SINT-MAARTEN · ORANJE":
        "SEMANARIO NEERLANDÉS · VOL.3 · SINTERKLAAS · SINT-MAARTEN · ORANJE",
    "SINTERKLAAS IS COMING": "LLEGA SINTERKLAAS",
    "This week: Sinterklaas comes to the Netherlands · see page 3":
        "Esta semana: Sinterklaas llega a los Países Bajos · véase la página 3",
    'f.bridge("Note | de intocht = arrival · de stoomboot = steamboat · de lampion = lantern.")':
        'f.bridge("de intocht: la llegada · de stoomboot: el barco de vapor · de lampion: el farolillo.")',
    "DE WEEK IN CIJFERS · IN NUMBERS": "DE WEEK IN CIJFERS · EN CIFRAS",
    " (9 Nov: Sinterklaas news)": " (9 nov.: noticiario de Sinterklaas)",
    " (14 Nov: national arrival, Grave)": " (14 nov.: llegada en Grave)",
    " (15 Nov: 88th)": " (15 nov.: 88.ª edición)",
    " (Fri 20:45)": " (vie. 20:45)",
    "NU JIJ · YOUR TURN": "NU JIJ · TE TOCA",
    "The Sinterklaas news starts on 9 November": "El noticiario de Sinterklaas empieza el 9 de noviembre",
    "The national arrival is in Grave": "La llegada nacional es en Grave",
    "The Amsterdam arrival is on Sunday 15 November": "La llegada a Ámsterdam es el domingo 15 de noviembre",
    "St Martin's Day is on Wednesday 11 November": "San Martín cae miércoles 11 de noviembre",
    "Netherlands–Greece kicks off at 20:45": "Países Bajos–Grecia, saque inicial a las 20:45",
    "Plural subject, so zetten": "Sujeto plural, así que zetten.",
    "· THIS WEEK": "· ESTA SEMANA",
    "Agenda van de week · THIS WEEK'S EVENTS": "Agenda van de week · AGENDA",
    "See pages 2–4 for all dates and times.": "Todas las fechas y horas, en las páginas 2–4.",
    "IN DEZE EDITIE · IN THIS ISSUE": "IN DEZE EDITIE · SUMARIO",
    "«The intocht»: Sinterklaas arrives in a town by boat, then on horseback, in a festive parade.":
        "«La intocht»: Sinterklaas llega a una ciudad en barco y luego a caballo, en un desfile festivo.",
    "IN HET KORT · IN BRIEF": "IN HET KORT · EN BREVE",
    "BLIKSEMQUIZ · LIGHTNING QUIZ": "BLIKSEMQUIZ · QUIZ RELÁMPAGO",
    "Read page 1, choose the right answer · answers on page 8":
        "Lee la página 1, elige la respuesta correcta · respuestas en la página 8",
    "The Sinterklaas news starts on Monday 9 November": "El noticiario de Sinterklaas empieza el lunes 9 de noviembre",
    "The Amsterdam arrival is the 88th edition": "La llegada a Ámsterdam es la 88.ª edición",
    'p.band("LEVEN · LIFE", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · St Martin\'s Day: lanterns and songs")':
        'p.band("LEVEN · VIDA", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · San Martín: farolillos y canciones")',
    "ZO ONTHOUD JE HET · REMEMBER": "ZO ONTHOUD JE HET · RECUERDA",
    'f.gloss("de lampion = lantern · delen = to share · de mantel = cloak, coat · de bedelaar = beggar · het erfgoed = heritage · het ledlampje = little LED light.")':
        'f.gloss("de lampion: el farolillo · delen: compartir · de mantel: la capa · de bedelaar: el mendigo · het erfgoed: el patrimonio · het ledlampje: la lamparita LED.")',
    "On 11 November, will you go singing door to door with a lantern, or would you rather watch the Sinterklaas news? Write two sentences in Dutch and send them to the editors.":
        "El 11 de noviembre, ¿irás cantando de puerta en puerta con un farolillo o preferirás ver el noticiario de Sinterklaas? Escribe dos frases en neerlandés y envíalas a la redacción.",
    "EN JIJ? · AND YOU?": "EN JIJ? · ¿Y TÚ?",
    "SINT-MAARTEN IN VIER WOORDEN · FOUR KEY WORDS": "SINT-MAARTEN IN VIER WOORDEN · CUATRO PALABRAS CLAVE",
    "Wat hoort bij het feest? · Which words belong to the festival?":
        "Wat hoort bij het feest? · ¿Qué palabras van con la fiesta?",
    "a paper lantern, with an LED light inside": "un farolillo de papel, con una luz LED dentro",
    "sharing: giving half a cloak to a beggar": "compartir: dar media capa a un mendigo",
    "St Martin's city, on the heritage list": "la ciudad de san Martín, patrimonio",
    "singing St Martin's songs door to door": "cantar canciones de San Martín de puerta en puerta",
    "OEFENINGEN · EXERCISES ON PAGE 2": "OEFENINGEN · EJERCICIOS PÁGINA 2",
    "Answers on page 8 · levels are mixed; find your number": "Respuestas en la página 8 · niveles mezclados; busca tu número",
    'e.bridge("Read the article on page 2 and choose the right answer.")':
        'e.bridge("Lee el artículo de la página 2 y elige la respuesta correcta.")',
    "Children go door to door with lanterns": "Los niños van de puerta en puerta con farolillos",
    "Martinus gave half his cloak to a beggar": "Martinus dio media capa a un mendigo",
    "Utrecht is St Martin's city": "Utrecht es la ciudad de san Martín",
    "A lantern takes an LED light, not a candle": "Un farolillo lleva luz LED, no una vela",
    'e.bridge("Fill in with words from page 2.")': 'e.bridge("Completa con palabras de la página 2.")',
    "St Martin's Day is on 11 November": "San Martín cae el 11 de noviembre",
    "lampion = lantern (de)": "lampion = farolillo, palabra con de",
    "delen = to share": "delen = compartir",
    "mantel = cloak (de)": "mantel = capa, palabra con de",
    "St Martin's city is Utrecht": "La ciudad de san Martín es Utrecht",
    'e.bridge("Fill in with the song words and the safety tip.")':
        'e.bridge("Completa con las palabras de la canción y el consejo de seguridad.")',
    "Song words: my little light may shine": "Palabras de la canción: que brille mi lucecita",
    "Lanterns shine brightest when it is dark": "Los farolillos brillan más cuando está oscuro",
    "An LED light is safe": "Una luz LED es segura",
    "Pakjesavond is on 5 December": "Pakjesavond cae el 5 de diciembre",
    '["lampion = lantern b", "delen = to share a", "mantel = cloak d", "erfgoed = heritage c"]':
        '["lampion = farolillo b", "delen = compartir a", "mantel = capa d", "erfgoed = patrimonio c"]',
    'instr="Match word to meaning"': 'instr="Relacionar"',
    "HET NIEUWS · TOP STORY": "HET NIEUWS · PORTADA",
}

ES_MAP.update({
    'p.band("CULTUUR · CULTURE", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · The Sinterklaas news and Het diner")':
        'p.band("CULTUUR · CULTURA", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · El noticiario de Sinterklaas y Het diner")',
    'f.gloss("het journaal = news programme · de flessenpost = message in a bottle · de burgemeester = mayor · de stoet = procession · de leeskring = reading club.")':
        'f.gloss("het journaal: el noticiario · de flessenpost: el mensaje en una botella · de burgemeester: el alcalde · de stoet: el desfile · de leeskring: el club de lectura.")',
    "OEFENINGEN · EXERCISES ON PAGE 3": "OEFENINGEN · EJERCICIOS PÁGINA 3",
    'e.bridge("Read the article on page 3 and choose the right answer.")':
        'e.bridge("Lee el artículo de la página 3 y elige la respuesta correcta.")',
    "The Sinterklaas news is on every day at 18:00": "El noticiario de Sinterklaas se emite cada día a las 18:00",
    "The Amsterdam boat leaves De Omval at 10:15": "El barco de Ámsterdam sale de De Omval a las 10:15",
    "Het diner was written by Herman Koch": "Het diner fue escrito por Herman Koch",
    "Het diner is free to pick up at the library": "Het diner se recoge gratis en la biblioteca",
    'e.bridge("Fill in with the words from the box.")': 'e.bridge("Completa con las palabras del recuadro.")',
    "journaal = news programme": "journaal = noticiario",
    "burgemeester = mayor": "burgemeester = alcalde",
    "stoet = procession": "stoet = desfile",
    "flessenpost = message in a bottle": "flessenpost = mensaje en una botella",
    "leeskring = reading club": "leeskring = club de lectura",
    'e.bridge("Complete with the present perfect. Watch the auxiliaries hebben/zijn.")':
        'e.bridge("Completa en perfecto. Fíjate en los auxiliares hebben/zijn.")',
    "beginnen takes zijn: is begonnen": "beginnen lleva zijn: is begonnen",
    "vinden perfectum: heeft gevonden": "vinden en perfecto: heeft gevonden",
    "aankomen takes zijn: is aangekomen": "aankomen lleva zijn: is aangekomen",
    "lezen perfectum: hebben gelezen": "lezen en perfecto: hebben gelezen",
    'e.bridge("Work it out: answer with the numbers from page 3.")':
        'e.bridge("Calcula: responde con los números de la página 3.")',
    "From 9 to 14 November is 5 days": "Del 9 al 14 de noviembre hay 5 días",
    "From 9 to 15 November is 6 days": "Del 9 al 15 de noviembre hay 6 días",
    "The Grave programme, 12:00–16:00, lasts 4 hours": "El programa de Grave, de 12:00 a 16:00, dura 4 horas",
    "Het diner is from 2009: 17 years ago in 2026": "Het diner es de 2009: hace 17 años en 2026",
    'p.band("SPORT", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · Oranje and the Nations League")':
        'p.band("SPORT · DEPORTE", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · Oranje y la Liga de Naciones")',
    'f.gloss("de groepsfase = group stage · de kwartfinale = quarter-final · ongeslagen = unbeaten · de interland = international match · de stand = the table.")':
        'f.gloss("de groepsfase: la fase de grupos · de kwartfinale: los cuartos de final · ongeslagen: invicto · de interland: el partido internacional · de stand: la clasificación.")',
    "OEFENINGEN · EXERCISES ON PAGE 4": "OEFENINGEN · EJERCICIOS PÁGINA 4",
    'e.bridge("Read the article on page 4 and choose the right answer.")':
        'e.bridge("Lee el artículo de la página 4 y elige la respuesta correcta.")',
    "Netherlands–Greece, Friday 20:45, in Amsterdam": "Países Bajos–Grecia, viernes 20:45, en Ámsterdam",
    "The Netherlands and Greece both have 8 points": "Países Bajos y Grecia tienen 8 puntos cada uno",
    "The Netherlands scored more goals in the group (7 to 5)": "Países Bajos marcó más goles en el grupo: 7 contra 5",
    "Germany–Netherlands, Monday, in Berlin": "Alemania–Países Bajos, lunes, en Berlín",
    "Eredivisie matchday 13 is on 21–22 November": "La jornada 13 de la Eredivisie es el 21–22 de noviembre",
    'e.bridge("Fill in with the words from the box. Watch the verb forms.")':
        'e.bridge("Completa con las palabras del recuadro. Fíjate en las formas verbales.")',
    "groepsfase = group stage": "groepsfase = fase de grupos",
    "kwartfinale plural: kwartfinales": "kwartfinale, plural: kwartfinales",
    "ongeslagen = unbeaten": "ongeslagen = invicto",
    "stand = the table": "stand = clasificación",
    "interland = international match": "interland = partido internacional",
    'e.bridge("Complete with the past tense or the perfect tense.")':
        'e.bridge("Completa en pasado o en perfecto.")',
    "spelen past tense: speelde": "spelen en pasado: speelde",
    "winnen past tense: won": "winnen en pasado: won",
    "maken past tense: maakte": "maken en pasado: maakte",
    "komen perfectum takes zijn": "komen en perfecto lleva zijn",
    "True: Netherlands–Greece, Friday 20:45": "Verdadero: Países Bajos–Grecia, viernes 20:45",
    "False: Serbia are bottom with 0 points": "Falso: Serbia es colista con 0 puntos",
    "False: Eredivisie matchday 13 is on 21–22 November": "Falso: la jornada 13 de la Eredivisie es el 21–22 de noviembre",
    "True: PSV beat Willem II 7–0": "Verdadero: el PSV ganó 7–0 a Willem II",
    'p.band("JONGEREN · YOUNG PEOPLE", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · Robinson, the shoe and the wish list")':
        'p.band("JONGEREN · JUVENTUD", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · Robinson, el zapato y la lista de deseos")',
    " (watch on RTL 4, Sunday 20:00)": " (ver en RTL 4, domingo 20:00)",
    " (watch the trials: points are won there)": " (mira las pruebas: allí se ganan los puntos)",
    " (guess with friends who stays longest)": " (adivina con amigos quién aguanta más)",
    " (then put out your shoe, wish list inside)": " (luego pon tu zapato, con la lista dentro)",
    'f.gloss("het verlanglijstje = wish list · de verslaggever = reporter · de proef = trial, challenge · stemmen = to vote · de aflevering = episode.")':
        'f.gloss("het verlanglijstje: la lista de deseos · de verslaggever: el reportero · de proef: la prueba · stemmen: votar · de aflevering: el episodio.")',
    "On Sunday, do you watch Expeditie Robinson, or would you rather put out your shoe with a wish list? Write two sentences in Dutch and send them in.":
        "El domingo, ¿ves Expeditie Robinson o prefieres poner tu zapato con una lista de deseos? Escribe dos frases en neerlandés y envíalas.",
    "OEFENINGEN · EXERCISES ON PAGE 5": "OEFENINGEN · EJERCICIOS PÁGINA 5",
    'e.bridge("Read the article on page 5 and choose the right answer.")':
        'e.bridge("Lee el artículo de la página 5 y elige la respuesta correcta.")',
    "Robinson is on every Sunday at 20:00 on RTL 4": "Robinson se emite cada domingo a las 20:00 en RTL 4",
    "19 contestants": "19 concursantes",
    "The show is filmed on a desert island in Malaysia": "El programa se graba en una isla desierta de Malasia",
    "The contestants spend 34 days on the island": "Los concursantes pasan 34 días en la isla",
    "A wish list goes in the shoe": "Una lista de deseos va en el zapato",
    "verlanglijstje = wish list (het)": "verlanglijstje = lista de deseos, palabra con het",
    "verslaggever = reporter (de)": "verslaggever = reportero, palabra con de",
    "proef = trial, challenge (de)": "proef = prueba, palabra con de",
    "stemmen = to vote": "stemmen = votar",
    "aflevering = episode": "aflevering = episodio",
    "kandidaat plural: kandidaten": "kandidaat, plural: kandidaten",
    'e.bridge("Use gaan + infinitive to talk about the future.")':
        'e.bridge("Habla del futuro con gaan + infinitivo.")',
    "gaat winnen = will win (just a guess)": "gaat winnen = va a ganar, solo una suposición",
    "wij → gaan + infinitive kijken": "wij → gaan + infinitivo kijken",
    "hij → gaat zetten": "hij → gaat zetten",
    "zij (plural) → gaan schrijven": "zij (plural) → gaan schrijven",
    "True: the show started on 1 November": "Verdadero: el programa empezó el 1 de noviembre",
    "False: the show is filmed in Malaysia": "Falso: el programa se graba en Malasia",
    "False: the carrot in the shoe is for the horse": "Falso: la zanahoria del zapato es para el caballo",
    'p.band("VERDIEPING · IN DEPTH", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · St Martin\'s Day or Halloween?")':
        'p.band("VERDIEPING · EN PROFUNDIDAD", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · ¿San Martín o Halloween?")',
    'f.gloss("de traditie = tradition · griezelen = to scare, to spook · de belangstelling = interest · de achteruitgang = decline · de deskundige = expert.")':
        'f.gloss("de traditie: la tradición · griezelen: asustar · de belangstelling: el interés · de achteruitgang: el declive · de deskundige: el experto.")',
    "Practice data: invented numbers for practice only, not a real survey. Question: what do you do around 11 November? (100 young people)":
        "Datos de práctica: cifras inventadas, no una encuesta real. Pregunta: ¿qué haces alrededor del 11 de noviembre? (100 jóvenes)",
    "DE GRAFIEK · PRACTICE DATA": "DE GRAFIEK · DATOS DE PRÁCTICA",
    "VOOR OF TEGEN? · FOR OR AGAINST?": "VOOR OF TEGEN? · PRO Y CONTRA",
    "OEFENINGEN · EXERCISES ON PAGE 6": "OEFENINGEN · EJERCICIOS PÁGINA 6",
    'e.bridge("Answer from the chart on page 6 (practice data).")':
        'e.bridge("Responde con el gráfico de la página 6 (datos de práctica).")',
    "40 young people walk with a lantern": "40 jóvenes van con farolillo",
    "25 celebrate Halloween": "25 celebran Halloween",
    "40 + 20 = 60": "40 + 20 = 60",
    "15 stay at home": "15 se quedan en casa",
    "The chart counts 100 people: 40+25+20+15": "El gráfico cuenta 100 personas: 40+25+20+15",
    'e.bridge("Read the article on page 6 and choose the right answer.")':
        'e.bridge("Lee el artículo de la página 6 y elige la respuesta correcta.")',
    "In 2025, 26% of Dutch people celebrated Halloween": "En 2025, el 26 % de los neerlandeses celebró Halloween",
    "The two surveys use different definitions, so they cannot be compared directly":
        "Las dos encuestas usan definiciones distintas, no se pueden comparar directamente",
    "Interest in St Martin's Day increased (Stengs, 2025)": "El interés por San Martín aumentó, según Stengs 2025",
    "Halloween is about spooking; St Martin's Day is about sharing": "Halloween va de asustar; San Martín, de compartir",
    "A tradition lives on when people keep celebrating it": "Una tradición vive cuando la gente sigue celebrándola",
    'e.bridge("Put the words in the right order to make sentences.")':
        'e.bridge("Pon las palabras en el orden correcto para formar frases.")',
    "traditie = tradition (de)": "traditie = tradición, palabra con de",
    "griezelen = to scare, to spook": "griezelen = asustar",
    "belangstelling = interest (de)": "belangstelling = interés, palabra con de",
    "achteruitgang = decline (de)": "achteruitgang = declive, palabra con de",
    "Subject + verb + complement + place": "Sujeto + verbo + complemento + lugar",
    "Subject + verb + manner + place": "Sujeto + verbo + modo + lugar",
    "The als-clause comes last": "La cláusula con als va al final",
    "kiezen + hoeft niet + explanation": "kiezen + hoeft niet + explicación",
})

ES_MAP.update({
    'p.band("TAAL · LANGUAGE", "De Lucerna", "Language focus · Drie niveaus, drie gereedschappen · Three levels, three tools")':
        'p.band("TAAL · LENGUA", "De Lucerna", "La lengua, en primer plano · Drie niveaus, drie gereedschappen · Tres niveles, tres herramientas")',
    'a.bridge("de stoomboot = steamboat; de intocht = the festive arrival; de schoen zetten = to put out your shoe; de lampion = lantern.")':
        'a.bridge("de stoomboot: el barco de vapor; de intocht: la llegada festiva; de schoen zetten: poner el zapato; de lampion: el farolillo.")',
    "de stoomboot = steamboat": "de stoomboot = barco de vapor",
    "The intocht is Sinterklaas's festive arrival": "La intocht es la llegada festiva de Sinterklaas",
    "lampion = lantern": "lampion = farolillo",
    'b.bridge("schoentje = little shoe; lichtje = little light; cadeautje = little present. -je means small and affectionate.")':
        'b.bridge("schoentje: zapatito; lichtje: lucecita; cadeautje: regalito. -je significa pequeño y cariñoso.")',
    "schoen + -tje: schoentje": "schoen + -tje: schoentje",
    "licht + -je: lichtje": "licht + -je: lichtje",
    "cadeau + -tje: cadeautje": "cadeau + -tje: cadeautje",
    '"-je means small and affectionate, not always really small"':
        '"-je significa pequeño y cariñoso, no siempre realmente pequeño"',
    'c.bridge("Als… = If… / When…; als het donker wordt = when it gets dark; als Sinterklaas komt = when Sinterklaas comes.")':
        'c.bridge("Als…: si… / cuando…; als het donker wordt: cuando oscurece; als Sinterklaas komt: cuando viene Sinterklaas.")',
    '"Als… = If… / When…"': '"Als…: si… / cuando…"',
    '"An als-clause is a condition, not a question"': '"Una cláusula con als es una condición, no una pregunta"',
    '"The verb comes first in the main clause: gaat de lampion aan"':
        '"El verbo va primero en la oración principal: gaat de lampion aan"',
    '"Als Oranje wint… = If Oranje win…"': '"Als Oranje wint…: si Oranje gana…"',
    "PAS OP! · ERROR CLINIC": "PAS OP! · CLÍNICA DE ERRORES",
    '"Sinterklaas is a name, so it takes no article."': '"Sinterklaas es un nombre, sin artículo."',
    "mijn schoen = my shoe.": "mijn schoen = mi zapato.",
    "Fixed phrase: langs de deuren.": "Expresión fija: langs de deuren.",
    "Verb first after the als-clause: ben ik blij.": "Verbo primero: ben ik blij.",
    "schoen zetten = to put out your shoe, with a carrot and a drawing inside.": "schoen zetten = poner el zapato, con una zanahoria y un dibujo dentro.",
    'dt_en = "No real letters or best page-8 texts at press time — example; promise to VOL.4."': 'dt_es = "Sin cartas reales ni mejores textos: ejemplo; promesa para el VOL.4."',
    '"Putting out your shoe takes mijn schoen (my shoe)."': '"mijn schoen = mi zapato."',
    '"The fixed phrase is langs de deuren (plural)."': '"Expresión fija: langs de deuren."',
    '"After the als-clause, the main-clause verb comes first: ben ik blij."': '"Verbo primero: ben ik blij."',
    "HET WOORD · WORD OF THE WEEK": "HET WOORD · LA PALABRA",
    '"schoen zetten = to put out your shoe: put your shoe by the door, with a carrot and a drawing inside, for Sinterklaas."':
        '"schoen zetten = poner el zapato, con una zanahoria y un dibujo dentro."',
    'len(wrap(dt_en, "sans", False, 20, CW - 44))': 'len(wrap(dt_es, "sans", False, 20, CW - 44))',
    'p.para(bx + 22, yy3 + 20, dt_en, 20, "sans", False, GREY, CW - 44, 1.42) + 10':
        'p.para(bx + 22, yy3 + 20, dt_es, 20, "sans", False, GREY, CW - 44, 1.42) + 10',
    '"Editors\' example — send yours for VOL.4!"':
        '"Ejemplo de la redacción. ¡Envíanos cartas y textos para el VOL.4!"',
    "ZINNEN VAN DE WEEK · PHRASES OF THE WEEK (VERBATIM FROM THIS ISSUE)":
        "ZINNEN VAN DE WEEK · FRASES DE LA SEMANA (LITERALES DE ESTE NÚMERO)",
    "On Monday 9 November, the Sinterklaas news starts on television.":
        "El lunes 9 de noviembre empieza en televisión el noticiario de Sinterklaas.",
    "One day later, Sunday 15 November: the Amsterdam arrival, 88th edition.":
        "Al día siguiente, domingo 15 de noviembre: Ámsterdam, 88.ª edición.",
    "St Martin's Day is the festival of sharing: sharing light, food and attention.":
        "San Martín es la fiesta de compartir: compartir luz, comida y atención.",
    "On Saturday 14 November, Sinterklaas officially arrives in Grave.":
        "El sábado 14 de noviembre, Sinterklaas llega oficialmente a Grave.",
    "On Friday 13 November, Oranje play Greece at home.":
        "El viernes 13 de noviembre, Oranje juega en casa contra Grecia.",
    "Every Sunday at 20:00, Expeditie Robinson is on RTL 4.":
        "Cada domingo a las 20:00, Expeditie Robinson se emite en RTL 4.",
    "St Martin's Day is an old tradition in the Netherlands.":
        "San Martín es una vieja tradición en los Países Bajos.",
    "VOLGENDE WEEK · NEXT WEEK (VOL.4)": "VOLGENDE WEEK · LA SEMANA QUE VIENE (VOL.4)",
    'p.band("TOETS EN ANTWOORDEN · TEST AND ANSWERS", "De Lucerna", "Page 8 · De grote toets van de week + alle antwoorden")':
        'p.band("TOETS EN ANTWOORDEN · PRUEBA Y RESPUESTAS", "De Lucerna", "Página 8 · De grote toets van de week + alle antwoorden")',
    "Robinson is on RTL 4": "Robinson se emite en RTL 4",
    "St Martin's Day is the festival of sharing.": "San Martín es la fiesta de compartir.",
    "St Martin's Day is the festival of sharing": "San Martín es la fiesta de compartir",
    "Subject + verb + time": "Sujeto + verbo + tiempo",
    "Subject + verb + object + place": "Sujeto + verbo + objeto + lugar",
    "Subject + verb + time + opponent": "Sujeto + verbo + tiempo + rival",
    "Watch the ordinal 88e": "Fíjate en el ordinal 88e",
    "schoen zetten is a fixed expression": "schoen zetten es una expresión fija",
    '["journaal = news programme b", "intocht = the festive arrival d", "lampion = lantern a", "delen = to share c"]':
        '["journaal = noticiario b", "intocht = llegada festiva d", "lampion = farolillo a", "delen = compartir c"]',
    "schoen = shoe": "schoen = zapato",
    "wortel = carrot (for the horse)": "wortel = zanahoria para el caballo",
    "verlanglijstje = wish list": "verlanglijstje = lista de deseos",
    "cadeautje = little present": "cadeautje = regalito",
    "18:00 = the Sinterklaas news time": "18:00 = la hora del noticiario de Sinterklaas",
    "Sanne lives in Utrecht": "Sanne vive en Utrecht",
    "On Wednesday she joins the St Martin's parade": "El miércoles se une al desfile de San Martín",
    "She puts a carrot and a wish list in her shoe": "Pone una zanahoria y una lista de deseos en su zapato",
    "She watches the Sinterklaas news every day at 18:00": "Ve el noticiario de Sinterklaas cada día a las 18:00",
    "Het diner was published in 2009": "Het diner se publicó en 2009",
    "Sinterklaas receives the key to the city at the Maritime Museum":
        "Sinterklaas recibe la llave de la ciudad en el Museo Marítimo",
    "Pakjesavond is on Saturday 5 December": "Pakjesavond cae sábado 5 de diciembre",
    "Grave lies on the river Maas": "Grave está junto al río Mosa",
    "Compare with the page 3 article": "Compara con el artículo de la página 3",
    "Original sentence from page 2 · delen = to share": "Frase original de la página 2 · delen = compartir",
    '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Translate into English"':
        '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Traducir"',
    '"Sint-Maarten is het feest van het delen. → ___", instr="Translate into English"':
        '"Sint-Maarten is het feest van het delen. → ___", instr="Traducir"',
    '"The arrival in Amsterdam is the 88th edition. → ___", instr="Translate into Dutch"':
        '"La llegada a Ámsterdam es la 88.ª edición. → ___", instr="Traducir"',
    '"I put out my shoe, with a wish list inside. → ___", instr="Translate into Dutch"':
        '"Pongo mi zapato, con una lista de deseos dentro. → ___", instr="Traducir"',
    '"(open task, model text below)"': '"(tarea abierta, texto modelo abajo)"',
    "Writing task (no single answer); model text ({NWORDS} words) below.":
        "Tarea de escritura (sin respuesta única); texto modelo ({NWORDS} palabras) abajo.",
    "See the model text in section H ({NWORDS} words)": "Véase el texto modelo en la sección H ({NWORDS} palabras)",
    "ANTWOORDEN · ANSWER KEY — grouped by page: find your number":
        "ANTWOORDEN · SOLUCIONES — agrupadas por página: busca tu número",
    "Every answer has a short note in English · ✓ marks the writing task":
        "Cada respuesta con una nota breve en español · ✓ marca la tarea de escritura",
    "schoen zetten = to put out your shoe": "schoen zetten = poner el zapato",
    "Netherlands–Greece kicks off at 20:45 on Friday": "Países Bajos–Grecia, saque inicial el viernes a las 20:45",
    "A tradition lives on when people keep celebrating it.":
        "Una tradición vive cuando la gente sigue celebrándola.",
    "The Sinterklaas news is on every day at 18:00.":
        "El noticiario de Sinterklaas se emite cada día a las 18:00.",
})

SKIP_IDX = {0, 1, 2, 3, 4, 5, 6, 8, 9, 11}
BADGE_IDX = 14

hdr = '''# -*- coding: utf-8 -*-
"""One-off fan-out transform: W46 NL core (Chinese explanations) -> NL x ES.
Line-literal replacements only, each asserted. Run once from this dir.
Dutch target text, keys (except re-aimed 137/138), facts, images: untouched.
Furniture per the W43/W45 NL x ES registry: badge INSERTED y=568 (strapline
kept), footer SEMANARIO NEERLANDÉS, gloss prefix Nota —, P8 keys
13.0/1.12/0.4 with Flow/separator at core values. Type tokens stay Chinese
(registry-only, never printed); only instr words localised. Glosses/bridges
use ': ' separators; P8 notes use ' = '. Disclosure variable renamed dt_es.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
R = []

def rep(f, old, new):
    R.append((f, old, new))

def rep_opt(f, old, new):
    R.append((f, old, new, True))

# ---------- global path (content files) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w46-nl-core/svg", "weekly-report-w46-nl-es/svg")

# ---------- instr words only (types stay Chinese) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep_opt(f, 'instr="填空"', 'instr="Completar"')
    rep_opt(f, 'instr="判断"', 'instr="¿Verdadero o falso?"')
    rep_opt(f, 'instr="造句"', 'instr="Formar la frase"')
    rep_opt(f, 'instr="写作"', 'instr="Escribir"')
    rep_opt(f, 'instr="翻译"', 'instr="Traducir"')

# ---------- furniture ----------
rep("render.py", "weekly-report-w46-nl-core", "weekly-report-w46-nl-es")
rep("render.py", "De-Lucerna-VOL3.pdf", "De-Lucerna-VOL3-ES.pdf")
rep("render.py", "Render the NL weekly VOL.3", "Render the NL x ES weekly VOL.3")
rep("run.py", "Run the IT weekly", "Run the NL x ES weekly")
rep("bslib4.py", "De Lucerna · 荷兰语周报 VOL.3 · LUCERNA DUTCH WEEKLY",
     "De Lucerna · SEMANARIO NEERLANDÉS VOL.3 · TEXTO EN NEERLANDÉS · EXPLICACIONES EN ESPAÑOL")
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"')
rep("bslib4.py", "译注｜", "Nota — ")
rep("svglib.py", "for 重阳", "for Double Ninth")

# ---------- literal replacements ----------
'''

tail = '''
# ---------- apply ----------
def main():
    failed = 0
    for item in R:
        f, old, new = item[0], item[1], item[2]
        opt = len(item) > 3
        path = os.path.join(HERE, f)
        txt = open(path, encoding="utf-8").read()
        n = txt.count(old)
        if n == 0 and not opt:
            failed += 1
            print(f"FAILED {f}: {old[:70]!r}")
        txt = txt.replace(old, new)
        open(path, "w", encoding="utf-8").write(txt)
    print("TOTAL replacements:", len(R), "FAILED:", failed)
    import re as _re
    cjk = 0
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py",
              "bslib4.py", "render.py", "run.py"]:
        for ln in open(os.path.join(HERE, f), encoding="utf-8"):
            if _re.search(r"[\\u4e00-\\u9fff]", ln):
                cjk += 1
    print(cjk)

if __name__ == "__main__":
    main()
'''

out = []
missing = []
for j, (f, old, new) in enumerate(pairs):
    if j in SKIP_IDX or j == 7:
        continue
    if j == BADGE_IDX:
        badge = ('p.text(975, 568, "TEXTOS EN NEERLANDÉS · EXPLICACIONES EN ESPAÑOL — '
                 'LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 20, "sans", True, BRICK, anchor="middle")')
        new_de = old + "\n# pairing badge (brick red, under the band) — W43 NL x ES measured: y=568, 20pt bold BRICK\n" + badge
        out.append((f, old, new_de))
        continue
    if j == 10:
        out.append((f, old, 'af.para(txt, 13.0, lh=1.12, gap=0.4, split=False)'))
        continue
    if "题（无唯一答案）" in old or new.startswith("Writing task (no single answer)"):
        old = "写作题（无唯一答案）；范文（{NWORDS} 词）见下。"
        out.append((f, old, ES_MAP[new]))
        continue
    if 'instr="Translate"' in old:
        old = old.replace('instr="Translate"', 'instr="Traducir"')
    if "writing题" in old:
        raise SystemExit(f"unexpected writing-form old at pair {j}: {old!r}")
    if new in ES_MAP:
        out.append((f, old, ES_MAP[new]))
    elif len(new) > 1 and new.startswith('"') and new.endswith('"') and new[1:-1] in ES_MAP:
        out.append((f, old, '"' + ES_MAP[new[1:-1]] + '"'))
    else:
        missing.append((j, f, new))
if missing:
    print("UNMAPPED:", len(missing))
    for j, f, new in missing:
        print(j, f, new)
    raise SystemExit(1)
seen = set()
ded = []
for p in out:
    if p in seen:
        continue
    seen.add(p)
    ded.append(p)
with open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/transform_es.py", "w", encoding="utf-8") as fh:
    fh.write(hdr)
    for f, old, new in ded:
        fh.write(f"rep({f!r}, {old!r}, {new!r})\n")
    fh.write(tail)
print("wrote", len(ded), "reps")
