# -*- coding: utf-8 -*-
"""Generate W46 NL x PT transform.py from the EN rep pairs (hidden_files/w46/en-reps.txt).
PT precedent (W45 NL x PT): type tokens are ENGLISH (complete/choice/...,
registry-only); instr words localised to Portuguese; per-direction Traduza
para o português/neerlandês. Badge REPLACES the strapline at y=372, 19.5pt
BRICK. Subtitle stays Dutch (passthrough). P8 sizes as EN/DE (Flow 2540,
separators 13.5/1.17/1.5, keys 13.0/1.14/0.3) with the accented PÁGINA
separator. Glosses/bridges use ' = ' + ' · '; P7 bridges use '; '. Keep P1
bridge and word-gloss SHORT (W45 PT overflow lessons)."""
import re

REPFILE = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-reps.txt"
lines = open(REPFILE, encoding="utf-8").read().splitlines()
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

PT_MAP = {
    "ELKE WEEK IN HET NEDERLANDS · EVERY WEEK · REAL DUTCH":
        "ELKE WEEK IN HET NEDERLANDS · O NEERLANDÊS QUE OS NEERLANDESES LEEM",
    "SINTERKLAAS IS COMING": "O SINTERKLAAS ESTÁ A CHEGAR",
    "This week: Sinterklaas comes to the Netherlands · see page 3":
        "Esta semana: o Sinterklaas chega aos Países Baixos · ver página 3",
    'f.bridge("Note | de intocht = arrival · de stoomboot = steamboat · de lampion = lantern.")':
        'f.bridge("Nota — de intocht = a chegada · de stoomboot = o barco a vapor · de lampion = a lanterna.")',
    "DE WEEK IN CIJFERS · IN NUMBERS": "DE WEEK IN CIJFERS · NÚMEROS",
    " (9 Nov: Sinterklaas news)": " (9 nov.: notícias do Sinterklaas)",
    " (14 Nov: national arrival, Grave)": " (14 nov.: chegada nacional, Grave)",
    " (15 Nov: 88th)": " (15 nov.: 88.ª edição)",
    " (Fri 20:45)": " (sex. 20:45)",
    "NU JIJ · YOUR TURN": "NU JIJ · A TUA VEZ",
    "The Sinterklaas news starts on 9 November": "As notícias do Sinterklaas começam a 9 de novembro",
    "The national arrival is in Grave": "A chegada nacional é em Grave",
    "The Amsterdam arrival is on Sunday 15 November": "A chegada a Amesterdão é no domingo, 15 de novembro",
    "St Martin's Day is on Wednesday 11 November": "O São Martinho é na quarta-feira, 11 de novembro",
    "Netherlands–Greece kicks off at 20:45": "Países Baixos–Grécia, pontapé inicial às 20:45",
    "Plural subject, so zetten": "Plural → zetten.",
    "· THIS WEEK": "· ESTA SEMANA",
    "Agenda van de week · THIS WEEK'S EVENTS": "Agenda van de week · ACONTECIMENTOS",
    "See pages 2–4 for all dates and times.": "Todas as datas e horas, páginas 2–4.",
    "IN DEZE EDITIE · IN THIS ISSUE": "IN DEZE EDITIE · NESTE NÚMERO",
    "«The intocht»: Sinterklaas arrives in a town by boat, then on horseback, in a festive parade.":
        "«A intocht»: o Sinterklaas chega a uma cidade de barco e depois a cavalo, em desfile festivo.",
    "IN HET KORT · IN BRIEF": "IN HET KORT · EM RESUMO",
    "BLIKSEMQUIZ · LIGHTNING QUIZ": "BLIKSEMQUIZ · QUIZ RELÂMPAGO",
    "Read page 1, choose the right answer · answers on page 8":
        "Lê a página 1, escolhe a resposta certa · respostas na página 8",
    "The Sinterklaas news starts on Monday 9 November": "As notícias do Sinterklaas começam na segunda-feira, 9 de novembro",
    "The Amsterdam arrival is the 88th edition": "A chegada a Amesterdão é a 88.ª edição",
    'p.band("LEVEN · LIFE", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · St Martin\'s Day: lanterns and songs")':
        'p.band("LEVEN · VIDA", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · São Martinho: lanternas e canções")',
    "ZO ONTHOUD JE HET · REMEMBER": "ZO ONTHOUD JE HET · LEMBRA-TE",
    'f.gloss("de lampion = lantern · delen = to share · de mantel = cloak, coat · de bedelaar = beggar · het erfgoed = heritage · het ledlampje = little LED light.")':
        'f.gloss("de lampion = a lanterna · delen = partilhar · de mantel = o manto · de bedelaar = o mendigo · het erfgoed = o património · het ledlampje = a luzinha LED.")',
    "On 11 November, will you go singing door to door with a lantern, or would you rather watch the Sinterklaas news? Write two sentences in Dutch and send them to the editors.":
        "A 11 de novembro, vais cantar de porta em porta com uma lanterna ou preferes ver as notícias do Sinterklaas? Escreve duas frases em neerlandês e envia-as à redação.",
    "EN JIJ? · AND YOU?": "EN JIJ? · E TU?",
    "SINT-MAARTEN IN VIER WOORDEN · FOUR KEY WORDS": "SINT-MAARTEN IN VIER WOORDEN · QUATRO PALAVRAS-CHAVE",
    "Wat hoort bij het feest? · Which words belong to the festival?":
        "Wat hoort bij het feest? · Que palavras pertencem à festa?",
    "a paper lantern, with an LED light inside": "uma lanterna de papel, com uma luz LED dentro",
    "sharing: giving half a cloak to a beggar": "partilhar: dar metade do manto a um mendigo",
    "St Martin's city, on the heritage list": "a cidade de São Martinho, património",
    "singing St Martin's songs door to door": "cantar as canções de São Martinho de porta em porta",
    "OEFENINGEN · EXERCISES ON PAGE 2": "OEFENINGEN · EXERCÍCIOS DA PÁGINA 2",
    "Answers on page 8 · levels are mixed; find your number": "Respostas na página 8 · níveis misturados; procura o teu número",
    'e.bridge("Read the article on page 2 and choose the right answer.")':
        'e.bridge("Lê o artigo da página 2 e escolhe a resposta certa.")',
    "Children go door to door with lanterns": "As crianças vão de porta em porta com lanternas",
    "Martinus gave half his cloak to a beggar": "Martinus deu metade do seu manto a um mendigo",
    "Utrecht is St Martin's city": "Utrecht é a cidade de São Martinho",
    "A lantern takes an LED light, not a candle": "Uma lanterna leva uma luz LED, não uma vela",
    'e.bridge("Fill in with words from page 2.")': 'e.bridge("Completa com as palavras da página 2.")',
    "St Martin's Day is on 11 November": "O São Martinho é a 11 de novembro",
    "lampion = lantern (de)": "lampion = lanterna (de)",
    "delen = to share": "delen = partilhar",
    "mantel = cloak (de)": "mantel = manto (de)",
    "St Martin's city is Utrecht": "A cidade de São Martinho é Utrecht",
    'e.bridge("Fill in with the song words and the safety tip.")':
        'e.bridge("Completa com as palavras da canção e o conselho de segurança.")',
    "Song words: my little light may shine": "Palavras da canção: a minha luzinha pode brilhar",
    "Lanterns shine brightest when it is dark": "As lanternas brilham mais quando está escuro",
    "An LED light is safe": "Uma luz LED é segura",
    "Pakjesavond is on 5 December": "O Pakjesavond é a 5 de dezembro",
    '["lampion = lantern b", "delen = to share a", "mantel = cloak d", "erfgoed = heritage c"]':
        '["lampion = lanterna b", "delen = partilhar a", "mantel = manto d", "erfgoed = património c"]',
    "HET NIEUWS · TOP STORY": "HET NIEUWS · MANCHETE",
    # EN fix-(f) shortened forms
    "mijn schoen = my shoe.": "mijn schoen = o meu sapato.",
    "Fixed phrase: langs de deuren.": "Expressão fixa: langs de deuren.",
    "Verb first after the als-clause: ben ik blij.": "Verbo em primeiro lugar: ben ik blij.",
    "schoen zetten = to put out your shoe, with a carrot and a drawing inside.":
        "schoen zetten = pôr o sapato, com uma cenoura e um desenho dentro.",
    'dt_en = "No real letters or best page-8 texts at press time — example; promise to VOL.4."':
        'dt_pt = "Sem cartas reais nem melhores textos — exemplo; promessa para o VOL.4."',
}
PT_MAP.update({
    'p.band("CULTUUR · CULTURE", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · The Sinterklaas news and Het diner")':
        'p.band("CULTUUR · CULTURA", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · As notícias do Sinterklaas e Het diner")',
    'f.gloss("het journaal = news programme · de flessenpost = message in a bottle · de burgemeester = mayor · de stoet = procession · de leeskring = reading club.")':
        'f.gloss("het journaal = o noticiário · de flessenpost = a mensagem na garrafa · de burgemeester = o presidente da câmara · de stoet = o cortejo · de leeskring = o círculo de leitura.")',
    "OEFENINGEN · EXERCISES ON PAGE 3": "OEFENINGEN · EXERCÍCIOS DA PÁGINA 3",
    'e.bridge("Read the article on page 3 and choose the right answer.")':
        'e.bridge("Lê o artigo da página 3 e escolhe a resposta certa.")',
    "The Sinterklaas news is on every day at 18:00": "As notícias do Sinterklaas passam todos os dias às 18:00",
    "The Amsterdam boat leaves De Omval at 10:15": "O barco de Amesterdão parte de De Omval às 10:15",
    "Het diner was written by Herman Koch": "Het diner foi escrito por Herman Koch",
    "Het diner is free to pick up at the library": "Het diner levanta-se grátis na biblioteca",
    'e.bridge("Fill in with the words from the box.")': 'e.bridge("Completa com as palavras do quadro.")',
    "journaal = news programme": "journaal = noticiário",
    "burgemeester = mayor": "burgemeester = presidente da câmara",
    "stoet = procession": "stoet = cortejo",
    "flessenpost = message in a bottle": "flessenpost = mensagem na garrafa",
    "leeskring = reading club": "leeskring = círculo de leitura",
    'e.bridge("Complete with the present perfect. Watch the auxiliaries hebben/zijn.")':
        'e.bridge("Completa no pretérito perfeito. Atenção aos auxiliares hebben/zijn.")',
    "beginnen takes zijn: is begonnen": "beginnen leva zijn: is begonnen",
    "vinden perfectum: heeft gevonden": "vinden no perfeito: heeft gevonden",
    "aankomen takes zijn: is aangekomen": "aankomen leva zijn: is aangekomen",
    "lezen perfectum: hebben gelezen": "lezen no perfeito: hebben gelezen",
    'e.bridge("Work it out: answer with the numbers from page 3.")':
        'e.bridge("Calcula: responde com os números da página 3.")',
    "From 9 to 14 November is 5 days": "De 9 a 14 de novembro são 5 dias",
    "From 9 to 15 November is 6 days": "De 9 a 15 de novembro são 6 dias",
    "The Grave programme, 12:00–16:00, lasts 4 hours": "O programa de Grave, 12:00–16:00, dura 4 horas",
    "Het diner is from 2009: 17 years ago in 2026": "Het diner é de 2009: há 17 anos em 2026",
    'p.band("SPORT", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · Oranje and the Nations League")':
        'p.band("SPORT", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · Oranje e a Liga das Nações")',
    'f.gloss("de groepsfase = group stage · de kwartfinale = quarter-final · ongeslagen = unbeaten · de interland = international match · de stand = the table.")':
        'f.gloss("de groepsfase = a fase de grupos · de kwartfinale = os quartos de final · ongeslagen = invicto · de interland = o jogo internacional · de stand = a classificação.")',
    "OEFENINGEN · EXERCISES ON PAGE 4": "OEFENINGEN · EXERCÍCIOS DA PÁGINA 4",
    'e.bridge("Read the article on page 4 and choose the right answer.")':
        'e.bridge("Lê o artigo da página 4 e escolhe a resposta certa.")',
    "Netherlands–Greece, Friday 20:45, in Amsterdam": "Países Baixos–Grécia, sexta-feira 20:45, em Amesterdão",
    "The Netherlands and Greece both have 8 points": "Os Países Baixos e a Grécia têm ambos 8 pontos",
    "The Netherlands scored more goals in the group (7 to 5)": "Os Países Baixos marcaram mais golos no grupo: 7 a 5",
    "Germany–Netherlands, Monday, in Berlin": "Alemanha–Países Baixos, segunda-feira, em Berlim",
    "Eredivisie matchday 13 is on 21–22 November": "A 13.ª jornada da Eredivisie é a 21–22 de novembro",
    'e.bridge("Fill in with the words from the box. Watch the verb forms.")':
        'e.bridge("Completa com as palavras do quadro. Atenção às formas verbais.")',
    "groepsfase = group stage": "groepsfase = fase de grupos",
    "kwartfinale plural: kwartfinales": "kwartfinale, plural: kwartfinales",
    "ongeslagen = unbeaten": "ongeslagen = invicto",
    "stand = the table": "stand = classificação",
    "interland = international match": "interland = jogo internacional",
    'e.bridge("Complete with the past tense or the perfect tense.")':
        'e.bridge("Completa no passado ou no perfeito.")',
    "spelen past tense: speelde": "spelen no passado: speelde",
    "winnen past tense: won": "winnen no passado: won",
    "maken past tense: maakte": "maken no passado: maakte",
    "komen perfectum takes zijn": "komen no perfeito leva zijn",
    "True: Netherlands–Greece, Friday 20:45": "Verdadeiro: Países Baixos–Grécia, sexta-feira 20:45",
    "False: Serbia are bottom with 0 points": "Falso: a Sérvia é última com 0 pontos",
    "False: Eredivisie matchday 13 is on 21–22 November": "Falso: a 13.ª jornada da Eredivisie é a 21–22 de novembro",
    "True: PSV beat Willem II 7–0": "Verdadeiro: o PSV bateu o Willem II por 7–0",
    'p.band("JONGEREN · YOUNG PEOPLE", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · Robinson, the shoe and the wish list")':
        'p.band("JONGEREN · JOVENS", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · Robinson, o sapato e a lista de desejos")',
    " (watch on RTL 4, Sunday 20:00)": " (ver na RTL 4, domingo 20:00)",
    " (watch the trials: points are won there)": " (ver as provas: os pontos ganham-se aí)",
    " (guess with friends who stays longest)": " (adivinha com amigos quem fica mais tempo)",
    " (then put out your shoe, wish list inside)": " (depois põe o sapato, lista dentro)",
    'f.gloss("het verlanglijstje = wish list · de verslaggever = reporter · de proef = trial, challenge · stemmen = to vote · de aflevering = episode.")':
        'f.gloss("het verlanglijstje = a lista de desejos · de verslaggever = o repórter · de proef = a prova · stemmen = votar · de aflevering = o episódio.")',
    "On Sunday, do you watch Expeditie Robinson, or would you rather put out your shoe with a wish list? Write two sentences in Dutch and send them in.":
        "No domingo, vês o Expeditie Robinson ou preferes pôr o sapato com uma lista de desejos? Escreve duas frases em neerlandês e envia-as.",
    "OEFENINGEN · EXERCISES ON PAGE 5": "OEFENINGEN · EXERCÍCIOS DA PÁGINA 5",
    'e.bridge("Read the article on page 5 and choose the right answer.")':
        'e.bridge("Lê o artigo da página 5 e escolhe a resposta certa.")',
    "Robinson is on every Sunday at 20:00 on RTL 4": "O Robinson passa todos os domingos às 20:00 na RTL 4",
    "19 contestants": "19 concorrentes",
    "The show is filmed on a desert island in Malaysia": "O programa é filmado numa ilha deserta na Malásia",
    "The contestants spend 34 days on the island": "Os concorrentes passam 34 dias na ilha",
    "A wish list goes in the shoe": "Uma lista de desejos vai para o sapato",
    "verlanglijstje = wish list (het)": "verlanglijstje = lista de desejos (het)",
    "verslaggever = reporter (de)": "verslaggever = repórter (de)",
    "proef = trial, challenge (de)": "proef = prova, desafio (de)",
    "stemmen = to vote": "stemmen = votar",
    "aflevering = episode": "aflevering = episódio",
    "kandidaat plural: kandidaten": "kandidaat, plural: kandidaten",
    'e.bridge("Use gaan + infinitive to talk about the future.")':
        'e.bridge("Fala do futuro com gaan + infinitivo.")',
    "gaat winnen = will win (just a guess)": "gaat winnen = vai ganhar (só um palpite)",
    "wij → gaan + infinitive kijken": "wij → gaan + infinitivo kijken",
    "hij → gaat zetten": "hij → gaat zetten",
    "zij (plural) → gaan schrijven": "zij (plural) → gaan schrijven",
    "True: the show started on 1 November": "Verdadeiro: o programa começou a 1 de novembro",
    "False: the show is filmed in Malaysia": "Falso: o programa é filmado na Malásia",
    "False: the carrot in the shoe is for the horse": "Falso: a cenoura no sapato é para o cavalo",
    'p.band("VERDIEPING · IN DEPTH", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · St Martin\'s Day or Halloween?")':
        'p.band("VERDIEPING · APROFUNDAMENTO", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · São Martinho ou Halloween?")',
    'f.gloss("de traditie = tradition · griezelen = to scare, to spook · de belangstelling = interest · de achteruitgang = decline · de deskundige = expert.")':
        'f.gloss("de traditie = a tradição · griezelen = assustar · de belangstelling = o interesse · de achteruitgang = o declínio · de deskundige = o especialista.")',
    "Practice data: invented numbers for practice only, not a real survey. Question: what do you do around 11 November? (100 young people)":
        "Dados de treino: números inventados, não um inquérito real. Pergunta: o que fazes por volta de 11 de novembro? (100 jovens)",
    "DE GRAFIEK · PRACTICE DATA": "DE GRAFIEK · DADOS DE TREINO",
    "VOOR OF TEGEN? · FOR OR AGAINST?": "VOOR OF TEGEN? · PRÓS E CONTRAS",
    "OEFENINGEN · EXERCISES ON PAGE 6": "OEFENINGEN · EXERCÍCIOS DA PÁGINA 6",
    'e.bridge("Answer from the chart on page 6 (practice data).")':
        'e.bridge("Responde com o gráfico da página 6 (dados de treino).")',
    "40 young people walk with a lantern": "40 jovens caminham com uma lanterna",
    "25 celebrate Halloween": "25 celebram o Halloween",
    "40 + 20 = 60": "40 + 20 = 60",
    "15 stay at home": "15 ficam em casa",
    "The chart counts 100 people: 40+25+20+15": "O gráfico conta 100 pessoas: 40+25+20+15",
    'e.bridge("Read the article on page 6 and choose the right answer.")':
        'e.bridge("Lê o artigo da página 6 e escolhe a resposta certa.")',
    "In 2025, 26% of Dutch people celebrated Halloween": "Em 2025, 26% dos neerlandeses celebraram o Halloween",
    "The two surveys use different definitions, so they cannot be compared directly":
        "Os dois inquéritos usam definições diferentes, por isso não podem ser comparados diretamente",
    "Interest in St Martin's Day increased (Stengs, 2025)": "O interesse pelo São Martinho aumentou (Stengs, 2025)",
    "Halloween is about spooking; St Martin's Day is about sharing": "O Halloween é assustar; o São Martinho é partilhar",
    "A tradition lives on when people keep celebrating it": "Uma tradição vive quando as pessoas continuam a celebrá-la",
    'e.bridge("Put the words in the right order to make sentences.")':
        'e.bridge("Põe as palavras na ordem certa para formar frases.")',
    "traditie = tradition (de)": "traditie = tradição (de)",
    "griezelen = to scare, to spook": "griezelen = assustar",
    "belangstelling = interest (de)": "belangstelling = interesse (de)",
    "achteruitgang = decline (de)": "achteruitgang = declínio (de)",
    "Subject + verb + complement + place": "Sujeito + verbo + complemento + lugar",
    "Subject + verb + manner + place": "Sujeito + verbo + modo + lugar",
    "The als-clause comes last": "A oração com als vem no fim",
    "kiezen + hoeft niet + explanation": "kiezen + hoeft niet + explicação",
})
PT_MAP.update({
    'p.band("TAAL · LANGUAGE", "De Lucerna", "Language focus · Drie niveaus, drie gereedschappen · Three levels, three tools")':
        'p.band("TAAL · LÍNGUA", "De Lucerna", "Foco na língua · Drie niveaus, drie gereedschappen · Três níveis, três ferramentas")',
    'a.bridge("de stoomboot = steamboat; de intocht = the festive arrival; de schoen zetten = to put out your shoe; de lampion = lantern.")':
        'a.bridge("de stoomboot = o barco a vapor; de intocht = a chegada festiva; de schoen zetten = pôr o sapato; de lampion = a lanterna.")',
    "de stoomboot = steamboat": "de stoomboot = barco a vapor",
    "The intocht is Sinterklaas's festive arrival": "A intocht é a chegada festiva do Sinterklaas",
    "lampion = lantern": "lampion = lanterna",
    'b.bridge("schoentje = little shoe; lichtje = little light; cadeautje = little present. -je means small and affectionate.")':
        'b.bridge("schoentje = sapatinho; lichtje = luzinha; cadeautje = presentinho. -je significa pequeno e afetuoso.")',
    "schoen + -tje: schoentje": "schoen + -tje: schoentje",
    "licht + -je: lichtje": "licht + -je: lichtje",
    "cadeau + -tje: cadeautje": "cadeau + -tje: cadeautje",
    '"-je means small and affectionate, not always really small"':
        '"-je significa pequeno e afetuoso, nem sempre muito pequeno"',
    'c.bridge("Als… = If… / When…; als het donker wordt = when it gets dark; als Sinterklaas komt = when Sinterklaas comes.")':
        'c.bridge("Als… = Se… / Quando…; als het donker wordt = quando escurece; als Sinterklaas komt = quando o Sinterklaas chega.")',
    '"Als… = If… / When…"': '"Als… = Se… / Quando…"',
    '"An als-clause is a condition, not a question"': '"Uma oração com als é uma condição, não uma pergunta"',
    '"The verb comes first in the main clause: gaat de lampion aan"':
        '"O verbo vem em primeiro lugar na oração principal: gaat de lampion aan"',
    '"Als Oranje wint… = If Oranje win…"': '"Als Oranje wint… = Se o Oranje ganhar…"',
    "PAS OP! · ERROR CLINIC": "PAS OP! · CLÍNICA DE ERROS",
    '"Sinterklaas is a name, so it takes no article."': '"Sinterklaas é um nome, sem artigo."',
    '"Putting out your shoe takes mijn schoen (my shoe)."': '"mijn schoen = o meu sapato."',
    '"The fixed phrase is langs de deuren (plural)."': '"Expressão fixa: langs de deuren."',
    '"After the als-clause, the main-clause verb comes first: ben ik blij."': '"Verbo em primeiro lugar: ben ik blij."',
    "HET WOORD · WORD OF THE WEEK": "HET WOORD · PALAVRA DA SEMANA",
    '"schoen zetten = to put out your shoe: put your shoe by the door, with a carrot and a drawing inside, for Sinterklaas."':
        '"schoen zetten = pôr o sapato, com uma cenoura e um desenho dentro."',
    'len(wrap(dt_en, "sans", False, 20, CW - 44))': 'len(wrap(dt_pt, "sans", False, 20, CW - 44))',
    'p.para(bx + 22, yy3 + 20, dt_en, 20, "sans", False, GREY, CW - 44, 1.42) + 10':
        'p.para(bx + 22, yy3 + 20, dt_pt, 20, "sans", False, GREY, CW - 44, 1.42) + 10',
    '"Editors\' example — send yours for VOL.4!"':
        '"Exemplo da redação. Envia cartas e textos para o VOL.4!"',
    "ZINNEN VAN DE WEEK · PHRASES OF THE WEEK (VERBATIM FROM THIS ISSUE)":
        "ZINNEN VAN DE WEEK · FRASES DA SEMANA (LITERAIS DESTE NÚMERO)",
    "On Monday 9 November, the Sinterklaas news starts on television.":
        "Na segunda-feira, 9 de novembro, as notícias do Sinterklaas começam na televisão.",
    "One day later, Sunday 15 November: the Amsterdam arrival, 88th edition.":
        "Um dia depois, domingo, 15 de novembro: a chegada a Amesterdão, 88.ª edição.",
    "St Martin's Day is the festival of sharing: sharing light, food and attention.":
        "O São Martinho é a festa da partilha: partilhar luz, comida e atenção.",
    "On Saturday 14 November, Sinterklaas officially arrives in Grave.":
        "No sábado, 14 de novembro, o Sinterklaas chega oficialmente a Grave.",
    "On Friday 13 November, Oranje play Greece at home.":
        "Na sexta-feira, 13 de novembro, o Oranje joga em casa contra a Grécia.",
    "Every Sunday at 20:00, Expeditie Robinson is on RTL 4.":
        "Todos os domingos às 20:00, o Expeditie Robinson passa na RTL 4.",
    "St Martin's Day is an old tradition in the Netherlands.":
        "O São Martinho é uma velha tradição nos Países Baixos.",
    "A tradition lives on when people keep celebrating it.":
        "Uma tradição vive quando as pessoas continuam a celebrá-la.",
    "VOLGENDE WEEK · NEXT WEEK (VOL.4)": "VOLGENDE WEEK · PRÓXIMA SEMANA (VOL.4)",
    'p.band("TOETS EN ANTWOORDEN · TEST AND ANSWERS", "De Lucerna", "Page 8 · De grote toets van de week + alle antwoorden")':
        'p.band("TOETS EN ANTWOORDEN · TESTE E RESPOSTAS", "De Lucerna", "Página 8 · De grote toets van de week + alle antwoorden")',
    "Robinson is on RTL 4": "O Robinson passa na RTL 4",
    "St Martin's Day is the festival of sharing.": "O São Martinho é a festa da partilha.",
    "St Martin's Day is the festival of sharing": "O São Martinho é a festa da partilha",
    "Subject + verb + time": "Sujeito + verbo + tempo",
    "Subject + verb + object + place": "Sujeito + verbo + objeto + lugar",
    "Subject + verb + time + opponent": "Sujeito + verbo + tempo + adversário",
    "Watch the ordinal 88e": "Atenção ao ordinal 88e",
    "schoen zetten is a fixed expression": "schoen zetten é uma expressão fixa",
    '["journaal = news programme b", "intocht = the festive arrival d", "lampion = lantern a", "delen = to share c"]':
        '["journaal = noticiário b", "intocht = chegada festiva d", "lampion = lanterna a", "delen = partilhar c"]',
    "schoen = shoe": "schoen = sapato",
    "wortel = carrot (for the horse)": "wortel = cenoura (para o cavalo)",
    "verlanglijstje = wish list": "verlanglijstje = lista de desejos",
    "cadeautje = little present": "cadeautje = presentinho",
    "18:00 = the Sinterklaas news time": "18:00 = a hora das notícias do Sinterklaas",
    "Sanne lives in Utrecht": "A Sanne vive em Utrecht",
    "On Wednesday she joins the St Martin's parade": "Na quarta-feira, ela junta-se ao desfile de São Martinho",
    "She puts a carrot and a wish list in her shoe": "Ela põe uma cenoura e uma lista de desejos no seu sapato",
    "She watches the Sinterklaas news every day at 18:00": "Ela vê as notícias do Sinterklaas todos os dias às 18:00",
    "Het diner was published in 2009": "Het diner foi publicado em 2009",
    "Sinterklaas receives the key to the city at the Maritime Museum":
        "O Sinterklaas recebe a chave da cidade no Museu Marítimo",
    "Pakjesavond is on Saturday 5 December": "O Pakjesavond é no sábado, 5 de dezembro",
    "Grave lies on the river Maas": "Grave fica no rio Maas",
    "Compare with the page 3 article": "Compara com o artigo da página 3",
    "Original sentence from page 2 · delen = to share": "Frase original da página 2 · delen = partilhar",
    '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Translate into English"':
        '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Traduza para o português"',
    '"Sint-Maarten is het feest van het delen. → ___", instr="Translate into English"':
        '"Sint-Maarten is het feest van het delen. → ___", instr="Traduza para o português"',
    '"The arrival in Amsterdam is the 88th edition. → ___", instr="Translate into Dutch"':
        '"A chegada a Amesterdão é a 88.ª edição. → ___", instr="Traduza para o neerlandês"',
    '"I put out my shoe, with a wish list inside. → ___", instr="Translate into Dutch"':
        '"Ponho o sapato, com uma lista de desejos dentro. → ___", instr="Traduza para o neerlandês"',
    '"(open task, model text below)"': '"(tarefa aberta, texto modelo abaixo)"',
    "Writing task (no single answer); model text ({NWORDS} words) below.":
        "Tarefa de escrita (sem resposta única); texto modelo ({NWORDS} palavras) abaixo.",
    "See the model text in section H ({NWORDS} words)":
        "Vê o texto modelo na secção H ({NWORDS} palavras)",
    "ANTWOORDEN · ANSWER KEY — grouped by page: find your number":
        "ANTWOORDEN · CHAVE DE RESPOSTAS — agrupadas por página: encontra o teu número",
    "Every answer has a short note in English · ✓ marks the writing task":
        "Cada resposta com uma breve nota em português · ✓ marca a tarefa de escrita",
    "schoen zetten = to put out your shoe": "schoen zetten = pôr o sapato",
    "Netherlands–Greece kicks off at 20:45 on Friday": "Países Baixos–Grécia, pontapé inicial na sexta-feira às 20:45",
    "The Sinterklaas news is on every day at 18:00.": "As notícias do Sinterklaas passam todos os dias às 18:00.",
    "The Sinterklaas news starts on Monday 9 November.": "As notícias do Sinterklaas começam na segunda-feira, 9 de novembro.",
    "hij → gaat zetten": "hij → gaat zetten",
    "40 + 20 = 60": "40 + 20 = 60",
})

# pairs that need special handling
SKIP_IDX = {0, 1, 2, 3, 4, 5, 6, 11}
BADGE_IDX = 14
# pair 7: identity rep on the post-loop "writing" check form — skipped (loop leaves it)
# pair 8: P8 Flow line — passthrough (2540, same as EN)
# pair 9: P8 separator — PT accented PÁGINA form
# pair 10: P8 keys line — PT value 13.0/1.14/0.3 (same as EN)
# pair 13: subtitle — passthrough (Dutch line, same as EN)

hdr = '''# -*- coding: utf-8 -*-
"""One-off fan-out transform: W46 NL core (Chinese explanations) -> NL x PT.
Line-literal replacements only, each asserted. Run once from this dir.
Dutch target text, keys (except re-aimed 137/138), facts, images: untouched.
Furniture per the W43/W45 NL x PT registry: badge REPLACES strapline y=372
(19.5pt bold BRICK), footer SEMANÁRIO NEERLANDÊS, gloss prefix Nota —, P8
keys 13.0/1.14/0.3 with Flow 2540 and accented PÁGINA separators. Type
tokens are ENGLISH (registry-only, never printed); only instr words
localised; per-direction Traduza para o português/neerlandês. Glosses use
' = ' + ' · '; P7 bridges use '; '. Disclosure variable renamed dt_pt.
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
    rep(f, "weekly-report-w46-nl-core/svg", "weekly-report-w46-nl-pt/svg")

# ---------- types (English) + instr (instrs FIRST, cloze before plain choice) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep_opt(f, 'instr="填空"', 'instr="Complete"')
    rep_opt(f, 'instr="判断"', 'instr="Verdadeiro ou falso?"')
    rep_opt(f, 'instr="造句"', 'instr="Forme a frase"')
    rep_opt(f, 'instr="写作"', 'instr="Escreva"')
    rep_opt(f, 'instr="翻译"', 'instr="Traduzir"')
    rep_opt(f, "完形单选", "cloze choice")
    rep_opt(f, "完成句子", "complete")
    rep_opt(f, "词汇配对", "matching")
    rep_opt(f, "判断对错", "true or false")
    rep_opt(f, "单选", "choice")
    rep_opt(f, "造句", "make sentences")
    rep_opt(f, "翻译", "translate")
    rep_opt(f, "写作", "writing")

# ---------- furniture ----------
rep("render.py", "weekly-report-w46-nl-core", "weekly-report-w46-nl-pt")
rep("render.py", "De-Lucerna-VOL3.pdf", "De-Lucerna-VOL3-PT.pdf")
rep_opt("render.py", "Render the NL weekly VOL.3", "Render the NL x PT weekly VOL.3")
rep_opt("run.py", "Run the IT weekly", "Run the NL x PT weekly")
rep("bslib4.py", "De Lucerna · 荷兰语周报 VOL.3 · LUCERNA DUTCH WEEKLY",
     "De Lucerna · SEMANÁRIO NEERLANDÊS VOL.3 · TEXTOS EM NEERLANDÊS · EXPLICAÇÕES EM PORTUGUÊS")
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
        badge = ('p.text(975, 372, "TEXTOS EM NEERLANDÊS · EXPLICAÇÕES EM PORTUGUÊS — '
                 'A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 19.5, "sans", True, BRICK, anchor="middle")')
        out.append((f, old, badge))
        continue
    if j == 8 or j == 13:
        out.append((f, old, new))
        continue
    if j == 9:
        out.append((f, old, 'af.para(f"— PÁGINA {pg} —", 13.5, "sans", True, OLIVE, lh=1.17, gap=1.5, split=False)'))
        continue
    if j == 10:
        out.append((f, old, 'af.para(txt, 13.0, lh=1.14, gap=0.3, split=False)'))
        continue
    if "题（无唯一答案）" in old or new.startswith("Writing task (no single answer)"):
        out.append((f, old, PT_MAP[new]))
        continue
    if 'instr="Translate' in old:
        old = old.replace('instr="Translate into English"', 'instr="Traduzir"')
        old = old.replace('instr="Translate into Dutch"', 'instr="Traduzir"')
        old = old.replace('instr="Translate"', 'instr="Traduzir"')
    if new == 'instr="Match word to meaning"':
        val = 'instr="Ligue palavra-significado"' if f == "content12.py" else 'instr="Associe a palavra ao significado"'
        out.append((f, old, val))
        continue
    if "writing题" in old:
        raise SystemExit(f"unexpected writing-form old at pair {j}: {old!r}")
    if new in PT_MAP:
        out.append((f, old, PT_MAP[new]))
    elif len(new) > 1 and new.startswith('"') and new.endswith('"') and new[1:-1] in PT_MAP:
        out.append((f, old, '"' + PT_MAP[new[1:-1]] + '"'))
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
with open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/transform_pt.py", "w", encoding="utf-8") as fh:
    fh.write(hdr)
    for f, old, new in ded:
        fh.write(f"rep({f!r}, {old!r}, {new!r})\n")
    fh.write(tail)
print("wrote", len(ded), "reps")
