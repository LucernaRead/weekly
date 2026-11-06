# -*- coding: utf-8 -*-
"""Generate W46 NL x IT transform.py from the EN rep pairs (hidden_files/w46/en-reps.txt).
IT precedent (W45 NL x IT): types TRANSLATED (Cloze/Completa la frase/...);
instr words localised; per-direction Traduci in italiano/olandese. Badge
INSERTED y=568, strapline kept. Subtitle at 36pt (full-line rep). P8 sizes as
EN/DE (Flow 2540, separators 13.5/1.17/1.5, keys 13.0/1.14/0.3). Glosses/bridges
use ' = ' + '; '. P7 notes telegraphic."""
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

IT_MAP = {
    "ELKE WEEK IN HET NEDERLANDS · EVERY WEEK · REAL DUTCH":
        "ELKE WEEK IN HET NEDERLANDS · OGNI SETTIMANA IN OLANDESE",
    "SINTERKLAAS IS COMING": "ARRIVA SINTERKLAAS",
    "This week: Sinterklaas comes to the Netherlands · see page 3":
        "Questa settimana: Sinterklaas arriva nei Paesi Bassi · vedi pagina 3",
    'f.bridge("Note | de intocht = arrival · de stoomboot = steamboat · de lampion = lantern.")':
        'f.bridge("Nota — de intocht = l\'arrivo · de stoomboot = il battello a vapore · de lampion = la lanterna.")',
    "DE WEEK IN CIJFERS · IN NUMBERS": "DE WEEK IN CIJFERS · IN CIFRE",
    " (9 Nov: Sinterklaas news)": " (9 nov.: notiziario)",
    " (14 Nov: national arrival, Grave)": " (14 nov.: Grave)",
    " (15 Nov: 88th)": " (15 nov.: 88ª)",
    " (Fri 20:45)": " (ven. 20:45)",
    "NU JIJ · YOUR TURN": "NU JIJ · TOCCA A TE",
    "The Sinterklaas news starts on 9 November": "Il notiziario di Sinterklaas inizia il 9 novembre",
    "The national arrival is in Grave": "L'arrivo nazionale è a Grave",
    "The Amsterdam arrival is on Sunday 15 November": "L'arrivo ad Amsterdam è domenica 15 novembre",
    "St Martin's Day is on Wednesday 11 November": "San Martino cade mercoledì 11 novembre",
    "Netherlands–Greece kicks off at 20:45": "Paesi Bassi–Grecia, calcio d'inizio alle 20:45",
    "Plural subject, so zetten": "Plurale → zetten.",
    "· THIS WEEK": "· QUESTA SETTIMANA",
    "Agenda van de week · THIS WEEK'S EVENTS": "Agenda van de week · GLI APPUNTAMENTI",
    "See pages 2–4 for all dates and times.": "Tutte le date e gli orari, pagine 2–4.",
    "IN DEZE EDITIE · IN THIS ISSUE": "IN DEZE EDITIE · SOMMARIO",
    "«The intocht»: Sinterklaas arrives in a town by boat, then on horseback, in a festive parade.":
        "«L'intocht»: Sinterklaas arriva in città in barca, poi a cavallo, in un corteo festoso.",
    "IN HET KORT · IN BRIEF": "IN HET KORT · IN BREVE",
    "BLIKSEMQUIZ · LIGHTNING QUIZ": "BLIKSEMQUIZ · QUIZ LAMPO",
    "Read page 1, choose the right answer · answers on page 8":
        "Leggi pagina 1, scegli la risposta giusta · risposte a pagina 8",
    "The Sinterklaas news starts on Monday 9 November": "Il notiziario di Sinterklaas inizia lunedì 9 novembre",
    "The Amsterdam arrival is the 88th edition": "L'arrivo ad Amsterdam è l'88ª edizione",
    'p.band("LEVEN · LIFE", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · St Martin\'s Day: lanterns and songs")':
        'p.band("LEVEN · VITA", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · San Martino: lanterne e canzoni")',
    "ZO ONTHOUD JE HET · REMEMBER": "ZO ONTHOUD JE HET · RICORDA",
    'f.gloss("de lampion = lantern · delen = to share · de mantel = cloak, coat · de bedelaar = beggar · het erfgoed = heritage · het ledlampje = little LED light.")':
        'f.gloss("de lampion = la lanterna · delen = condividere · de mantel = il mantello · de bedelaar = il mendicante · het erfgoed = il patrimonio · het ledlampje = la lucina LED.")',
    "On 11 November, will you go singing door to door with a lantern, or would you rather watch the Sinterklaas news? Write two sentences in Dutch and send them to the editors.":
        "L'11 novembre andrai a cantare di porta in porta con una lanterna, o preferirai guardare il notiziario di Sinterklaas? Scrivi due frasi in olandese e mandale alla redazione.",
    "EN JIJ? · AND YOU?": "EN JIJ? · E TU?",
    "SINT-MAARTEN IN VIER WOORDEN · FOUR KEY WORDS": "SINT-MAARTEN IN VIER WOORDEN · QUATTRO PAROLE CHIAVE",
    "Wat hoort bij het feest? · Which words belong to the festival?":
        "Wat hoort bij het feest? · Quali parole vanno con la festa?",
    "a paper lantern, with an LED light inside": "una lanterna di carta, con una luce LED dentro",
    "sharing: giving half a cloak to a beggar": "condividere: dare metà mantello a un mendicante",
    "St Martin's city, on the heritage list": "la città di san Martino, patrimonio",
    "singing St Martin's songs door to door": "cantare le canzoni di San Martino di porta in porta",
    "OEFENINGEN · EXERCISES ON PAGE 2": "OEFENINGEN · ESERCIZI PAGINA 2",
    "Answers on page 8 · levels are mixed; find your number": "Risposte a pagina 8 · livelli mescolati; cerca il tuo numero",
    'e.bridge("Read the article on page 2 and choose the right answer.")':
        'e.bridge("Leggi l\'articolo a pagina 2 e scegli la risposta giusta.")',
    "Children go door to door with lanterns": "I bambini vanno di porta in porta con le lanterne",
    "Martinus gave half his cloak to a beggar": "Martinus ha dato metà del suo mantello a un mendicante",
    "Utrecht is St Martin's city": "Utrecht è la città di san Martino",
    "A lantern takes an LED light, not a candle": "Una lanterna ha una luce LED, non una candela",
    'e.bridge("Fill in with words from page 2.")': 'e.bridge("Completa con le parole di pagina 2.")',
    "St Martin's Day is on 11 November": "San Martino cade l'11 novembre",
    "lampion = lantern (de)": "lampion = lanterna (de)",
    "delen = to share": "delen = condividere",
    "mantel = cloak (de)": "mantel = mantello (de)",
    "St Martin's city is Utrecht": "La città di san Martino è Utrecht",
    'e.bridge("Fill in with the song words and the safety tip.")':
        'e.bridge("Completa con le parole della canzone e il consiglio di sicurezza.")',
    "Song words: my little light may shine": "Parole della canzone: la mia lucina può brillare",
    "Lanterns shine brightest when it is dark": "Le lanterne brillano di più quando è buio",
    "An LED light is safe": "Una luce LED è sicura",
    "Pakjesavond is on 5 December": "Pakjesavond cade il 5 dicembre",
    '["lampion = lantern b", "delen = to share a", "mantel = cloak d", "erfgoed = heritage c"]':
        '["lampion = lanterna b", "delen = condividere a", "mantel = mantello d", "erfgoed = patrimonio c"]',
    'instr="Match word to meaning"': 'instr="Abbina la parola al significato"',
    "HET NIEUWS · TOP STORY": "HET NIEUWS · IN PRIMA PAGINA",
    # EN fix-(f) shortened forms (re-extracted pairs carry the fixed strings)
    "mijn schoen = my shoe.": "mijn schoen = la mia scarpa.",
    "Fixed phrase: langs de deuren.": "Espressione fissa: langs de deuren.",
    "Verb first after the als-clause: ben ik blij.": "Verbo per primo: ben ik blij.",
    "schoen zetten = to put out your shoe, with a carrot and a drawing inside.":
        "schoen zetten = mettere fuori la scarpa, con una carota e un disegno dentro.",
    'dt_en = "No real letters or best page-8 texts at press time — example; promise to VOL.4."':
        'dt_it = "Niente lettere vere, niente testi migliori — esempio; promessa al VOL.4."',
}
IT_MAP.update({
    'p.band("CULTUUR · CULTURE", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · Sinterklaas news and Het diner")':
        'p.band("CULTUUR · CULTURA", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · Il notiziario di Sinterklaas e Het diner")',
    'f.gloss("het journaal = news programme · de flessenpost = message in a bottle · de burgemeester = mayor · de stoet = procession · de leeskring = reading club.")':
        'f.gloss("het journaal = il notiziario · de flessenpost = il messaggio in bottiglia · de burgemeester = il sindaco · de stoet = il corteo · de leeskring = il circolo di lettura.")',
    "OEFENINGEN · EXERCISES ON PAGE 3": "OEFENINGEN · ESERCIZI PAGINA 3",
    'e.bridge("Read the article on page 3 and choose the right answer.")':
        'e.bridge("Leggi l\'articolo a pagina 3 e scegli la risposta giusta.")',
    "The Sinterklaas news is on every day at 18:00": "Il notiziario di Sinterklaas va in onda ogni giorno alle 18:00",
    "The Amsterdam boat leaves De Omval at 10:15": "Il battello di Amsterdam parte da De Omval alle 10:15",
    "Het diner was written by Herman Koch": "Het diner è stato scritto da Herman Koch",
    "Het diner is free to pick up at the library": "Het diner si ritira gratis in biblioteca",
    'e.bridge("Fill in with words from the box.")': 'e.bridge("Completa con le parole del riquadro.")',
    "journaal = news programme": "journaal = notiziario",
    "burgemeester = mayor": "burgemeester = sindaco",
    "stoet = procession": "stoet = corteo",
    "flessenpost = message in a bottle": "flessenpost = messaggio in bottiglia",
    "leeskring = reading club": "leeskring = circolo di lettura",
    'e.bridge("Fill in the perfect tense. Watch the helpers hebben/zijn.")':
        'e.bridge("Completa al passato prossimo. Attenzione agli ausiliari hebben/zijn.")',
    "beginnen takes zijn: is begonnen": "beginnen vuole zijn: is begonnen",
    "vinden in the perfect: heeft gevonden": "vinden al perfetto: heeft gevonden",
    "aankomen takes zijn: is aangekomen": "aankomen vuole zijn: is aangekomen",
    "lezen in the perfect: hebben gelezen": "lezen al perfetto: hebben gelezen",
    'e.bridge("Work it out: answer with numbers from page 3.")':
        'e.bridge("Calcola: rispondi con i numeri di pagina 3.")',
    "9 to 14 November is 5 days": "Dal 9 al 14 novembre sono 5 giorni",
    "9 to 15 November is 6 days": "Dal 9 al 15 novembre sono 6 giorni",
    "Grave programme, 12:00–16:00, lasts 4 hours": "Il programma di Grave, 12:00–16:00, dura 4 ore",
    "Het diner is from 2009: 17 years ago in 2026": "Het diner è del 2009: 17 anni fa nel 2026",
    'p.band("SPORT", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · Oranje and the Nations League")':
        'p.band("SPORT", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · Oranje e la Nations League")',
    'f.gloss("de groepsfase = group stage · de kwartfinale = quarter-final · ongeslagen = unbeaten · de interland = international match · de stand = table, standings.")':
        'f.gloss("de groepsfase = la fase a gironi · de kwartfinale = i quarti di finale · ongeslagen = imbattuto · de interland = la partita internazionale · de stand = la classifica.")',
    "OEFENINGEN · EXERCISES ON PAGE 4": "OEFENINGEN · ESERCIZI PAGINA 4",
    'e.bridge("Read the article on page 4 and choose the right answer.")':
        'e.bridge("Leggi l\'articolo a pagina 4 e scegli la risposta giusta.")',
    "Netherlands–Greece, Friday 20:45, in Amsterdam": "Paesi Bassi–Grecia, venerdì 20:45, ad Amsterdam",
    "The Netherlands and Greece both have 8 points": "Paesi Bassi e Grecia hanno entrambi 8 punti",
    "The Netherlands scored more goals in the group: 7 to 5": "I Paesi Bassi hanno segnato più gol nel girone: 7 a 5",
    "Germany–Netherlands, Monday, in Berlin": "Germania–Paesi Bassi, lunedì, a Berlino",
    "Eredivisie matchday 13 is 21–22 November": "La 13ª giornata di Eredivisie è il 21–22 novembre",
    'e.bridge("Fill in with words from the box. Watch the verb forms.")':
        'e.bridge("Completa con le parole del riquadro. Attenzione alle forme verbali.")',
    "groepsfase = group stage": "groepsfase = fase a gironi",
    "kwartfinale, plural: kwartfinales": "kwartfinale, plurale: kwartfinales",
    "ongeslagen = unbeaten": "ongeslagen = imbattuto",
    "stand = table, standings": "stand = classifica",
    "interland = international match": "interland = partita internazionale",
    'e.bridge("Fill in the past tense or the perfect tense.")':
        'e.bridge("Completa al passato o al perfetto.")',
    "spelen in the past: speelde": "spelen al passato: speelde",
    "winnen in the past: won": "winnen al passato: won",
    "maken in the past: maakte": "maken al passato: maakte",
    "komen in the perfect takes zijn": "komen al perfetto vuole zijn",
    "TRUE: Netherlands–Greece, Friday 20:45": "Vero: Paesi Bassi–Grecia, venerdì 20:45",
    "FALSE: Serbia are bottom with 0 points": "Falso: la Serbia è ultima con 0 punti",
    "FALSE: Eredivisie matchday 13 is 21–22 November": "Falso: la 13ª giornata di Eredivisie è il 21–22 novembre",
    "TRUE: PSV beat Willem II 7–0": "Vero: il PSV ha battuto il Willem II 7–0",
    'p.band("JONGEREN · YOUTH", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · Robinson, the shoe and the wish list")':
        'p.band("JONGEREN · GIOVANI", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · Robinson, la scarpa e la lista dei desideri")',
    " (watch on RTL 4, Sunday 20:00)": " (guarda su RTL 4, domenica 20:00)",
    " (watch the trials: points are won there)": " (guarda le prove: i punti si vincono lì)",
    " (guess with friends who lasts longest)": " (indovina con gli amici chi resta più a lungo)",
    " (then put out your shoe, list inside)": " (poi metti fuori la scarpa, con la lista dentro)",
    'f.gloss("het verlanglijstje = wish list · de verslaggever = reporter · de proef = trial, challenge · stemmen = to vote · de aflevering = episode.")':
        'f.gloss("het verlanglijstje = la lista dei desideri · de verslaggever = il reporter · de proef = la prova · stemmen = votare · de aflevering = la puntata.")',
    "On Sunday, will you watch Expeditie Robinson, or would you rather put out your shoe with a wish list inside? Write two sentences in Dutch and send them in.":
        "Domenica guardi Expeditie Robinson, o preferisci mettere fuori la scarpa con la lista dei desideri? Scrivi due frasi in olandese e mandale.",
    "OEFENINGEN · EXERCISES ON PAGE 5": "OEFENINGEN · ESERCIZI PAGINA 5",
    'e.bridge("Read the article on page 5 and choose the right answer.")':
        'e.bridge("Leggi l\'articolo a pagina 5 e scegli la risposta giusta.")',
    "Robinson is on every Sunday at 20:00 on RTL 4": "Robinson va in onda ogni domenica alle 20:00 su RTL 4",
    "19 candidates": "19 concorrenti",
    "The programme is filmed on a deserted island in Malaysia": "Il programma è girato su un'isola deserta in Malesia",
    "The candidates spend 34 days on the island": "I concorrenti passano 34 giorni sull'isola",
    "A wish list goes in the shoe": "Una lista dei desideri va nella scarpa",
    "verlanglijstje = wish list (het)": "verlanglijstje = lista dei desideri (het)",
    "verslaggever = reporter (de)": "verslaggever = reporter (de)",
    "proef = trial, challenge (de)": "proef = prova, sfida (de)",
    "stemmen = to vote": "stemmen = votare",
    "aflevering = episode": "aflevering = puntata",
    "kandidaat, plural: kandidaten": "kandidaat, plurale: kandidaten",
    'e.bridge("Talk about the future with gaan + infinitive.")':
        'e.bridge("Parla del futuro con gaan + infinito.")',
    "gaat winnen = will win (just a guess)": "gaat winnen = vincerà (solo un'ipotesi)",
    "wij → gaan + infinitive kijken": "wij → gaan + infinito kijken",
    "hij → gaat zetten": "hij → gaat zetten",
    "zij (plural) → gaan schrijven": "zij (plurale) → gaan schrijven",
    "TRUE: the programme started on 1 November": "Vero: il programma è iniziato il 1º novembre",
    "FALSE: the programme is filmed in Malaysia": "Falso: il programma è girato in Malesia",
    "FALSE: the carrot in the shoe is for the horse": "Falso: la carota nella scarpa è per il cavallo",
    'p.band("VERDIEPING · IN DEPTH", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · St Martin\'s Day or Halloween?")':
        'p.band("VERDIEPING · APPROFONDIMENTO", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · San Martino o Halloween?")',
    'f.gloss("de traditie = tradition · griezelen = to scare · de belangstelling = interest · de achteruitgang = decline · de deskundige = expert.")':
        'f.gloss("de traditie = la tradizione · griezelen = spaventare · de belangstelling = l\'interesse · de achteruitgang = il declino · de deskundige = l\'esperto.")',
    "Practice data: invented numbers, not a real survey. Question: what do you do around 11 November? (100 young people)":
        "Dati di esercitazione: numeri inventati, non un vero sondaggio. Domanda: cosa fai intorno all'11 novembre? (100 giovani)",
    "DE GRAFIEK · PRACTICE DATA": "DE GRAFIEK · DATI INVENTATI",
    "VOOR OF TEGEN? · FOR OR AGAINST?": "VOOR OF TEGEN? · PRO O CONTRO?",
    "OEFENINGEN · EXERCISES ON PAGE 6": "OEFENINGEN · ESERCIZI PAGINA 6",
    'e.bridge("Answer with the chart on page 6 (practice data).")':
        'e.bridge("Rispondi con il grafico a pagina 6 (dati di esercitazione).")',
    "40 young people walk with a lantern": "40 giovani camminano con una lanterna",
    "25 celebrate Halloween": "25 festeggiano Halloween",
    "40 + 20 = 60": "40 + 20 = 60",
    "15 stay at home": "15 restano a casa",
    "The chart counts 100 people: 40+25+20+15": "Il grafico conta 100 persone: 40+25+20+15",
    'e.bridge("Read the article on page 6 and choose the right answer.")':
        'e.bridge("Leggi l\'articolo a pagina 6 e scegli la risposta giusta.")',
    "In 2025, 26% of Dutch people celebrated Halloween": "Nel 2025, il 26% degli olandesi ha festeggiato Halloween",
    "The two surveys use different definitions and cannot be compared directly":
        "I due sondaggi usano definizioni diverse, non si possono confrontare direttamente",
    "Interest in St Martin's Day rose, said Stengs in 2025": "L'interesse per San Martino è aumentato, secondo Stengs 2025",
    "Halloween is scaring; St Martin's Day is sharing": "Halloween è spaventare; San Martino è condividere",
    "A tradition lives when people keep celebrating it": "Una tradizione vive quando la gente continua a festeggiarla",
    'e.bridge("Put the words in the right order to make sentences.")':
        'e.bridge("Metti le parole nell\'ordine giusto per formare frasi.")',
    "traditie = tradition (de)": "traditie = tradizione (de)",
    "griezelen = to scare": "griezelen = spaventare",
    "belangstelling = interest (de)": "belangstelling = interesse (de)",
    "achteruitgang = decline (de)": "achteruitgang = declino (de)",
    "Subject + verb + object + place": "Soggetto + verbo + complemento + luogo",
    "Subject + verb + manner + place": "Soggetto + verbo + modo + luogo",
    "The als-clause goes at the end": "La frase con als va alla fine",
    "kiezen + hoeft niet + explanation": "kiezen + hoeft niet + spiegazione",
})
IT_MAP.update({
    'p.band("TAAL · LANGUAGE", "De Lucerna", "Focus op taal · Drie niveaus, drie gereedschappen · Language in focus · Three levels, three tools")':
        'p.band("TAAL · LINGUA", "De Lucerna", "Focus sulla lingua · Drie niveaus, drie gereedschappen · Tre livelli, tre strumenti")',
    'a.bridge("de stoomboot = steamboat; de intocht = festive arrival; de schoen zetten = to put out your shoe; de lampion = lantern.")':
        'a.bridge("de stoomboot = il battello a vapore; de intocht = l\'arrivo festoso; de schoen zetten = mettere fuori la scarpa; de lampion = la lanterna.")',
    "de stoomboot = steamboat": "de stoomboot = battello a vapore",
    "The intocht is Sinterklaas' festive arrival": "L'intocht è l'arrivo festoso di Sinterklaas",
    "lampion = lantern": "lampion = lanterna",
    'b.bridge("schoentje = little shoe; lichtje = little light; cadeautje = little gift. -je means small and affectionate.")':
        'b.bridge("schoentje = scarpina; lichtje = lucina; cadeautje = regalino. -je significa piccolo e affettuoso.")',
    '"-je means small and affectionate, not always really small"':
        '"-je significa piccolo e affettuoso, non sempre davvero piccolo"',
    'c.bridge("Als… = If… / When…; als het donker wordt = when it gets dark; als Sinterklaas komt = when Sinterklaas comes.")':
        'c.bridge("Als… = Se… / Quando…; als het donker wordt = quando fa buio; als Sinterklaas komt = quando arriva Sinterklaas.")',
    '"Als… = If… / When…"': '"Als… = Se… / Quando…"',
    '"An als-clause is a condition, not a question"': '"Una frase con als è una condizione, non una domanda"',
    '"The verb comes first in the main clause: gaat de lampion aan"':
        '"Il verbo viene per primo nella frase principale: gaat de lampion aan"',
    '"Als Oranje wint… = If Oranje wins…"': '"Als Oranje wint… = Se Oranje vince…"',
    "PAS OP! · ERROR CLINIC": "PAS OP! · CLINICA DEGLI ERRORI",
    '"Sinterklaas is a name, no article."': '"Sinterklaas è un nome, senza articolo."',
    '"Putting out your shoe takes mijn schoen (my shoe)."': '"mijn schoen = la mia scarpa."',
    '"The fixed phrase is langs de deuren (plural)."': '"Espressione fissa: langs de deuren."',
    '"After the als-clause, the main-clause verb comes first: ben ik blij."': '"Verbo per primo: ben ik blij."',
    "HET WOORD · WORD OF THE WEEK": "HET WOORD · LA PAROLA",
    '"schoen zetten = to put out your shoe: put your shoe by the door, with a carrot and a drawing inside, for Sinterklaas."':
        '"schoen zetten = mettere fuori la scarpa, con una carota e un disegno dentro."',
    'len(wrap(dt_en, "sans", False, 20, CW - 44))': 'len(wrap(dt_it, "sans", False, 20, CW - 44))',
    'p.para(bx + 22, yy3 + 20, dt_en, 20, "sans", False, GREY, CW - 44, 1.42) + 10':
        'p.para(bx + 22, yy3 + 20, dt_it, 20, "sans", False, GREY, CW - 44, 1.42) + 10',
    '"Editors\' example — send yours for VOL.4!"':
        '"Esempio della redazione. Mandaci lettere e testi per il VOL.4!"',
    "ZINNEN VAN DE WEEK · PHRASES OF THE WEEK (VERBATIM FROM THIS ISSUE)":
        "ZINNEN VAN DE WEEK · FRASI DELLA SETTIMANA (LETTERALI DA QUESTO NUMERO)",
    "On Monday 9 November, the Sinterklaas news starts on television.":
        "Lunedì 9 novembre inizia in televisione il notiziario di Sinterklaas.",
    "One day later, Sunday 15 November: the Amsterdam arrival, 88th edition.":
        "Il giorno dopo, domenica 15 novembre: l'arrivo ad Amsterdam, 88ª edizione.",
    "St Martin's Day is the festival of sharing: sharing light, sharing food, sharing attention.":
        "San Martino è la festa della condivisione: condividere luce, cibo e attenzione.",
    "On Saturday 14 November, Sinterklaas officially arrives in Grave.":
        "Sabato 14 novembre Sinterklaas arriva ufficialmente a Grave.",
    "On Friday 13 November, Oranje play at home against Greece.":
        "Venerdì 13 novembre Oranje gioca in casa contro la Grecia.",
    "Every Sunday at 20:00, Expeditie Robinson is on RTL 4.":
        "Ogni domenica alle 20:00, Expeditie Robinson va in onda su RTL 4.",
    "St Martin's Day is an old tradition in the Netherlands.":
        "San Martino è una vecchia tradizione nei Paesi Bassi.",
    "VOLGENDE WEEK · NEXT WEEK (VOL.4)": "VOLGENDE WEEK · LA PROSSIMA SETTIMANA (VOL.4)",
    'p.band("TOETS EN ANTWOORDEN · TEST AND ANSWERS", "De Lucerna", "Pagina 8 · De grote toets van de week + alle antwoorden")':
        'p.band("TOETS EN ANTWOORDEN · TEST E RISPOSTE", "De Lucerna", "Pagina 8 · De grote toets van de week + alle antwoorden")',
    "Robinson is on RTL 4": "Robinson va in onda su RTL 4",
    "St Martin's Day is the festival of sharing.": "San Martino è la festa della condivisione.",
    "St Martin's Day is the festival of sharing": "San Martino è la festa della condivisione",
    "Subject + verb + time": "Soggetto + verbo + tempo",
    "Subject + verb + object + place": "Soggetto + verbo + complemento + luogo",
    "Subject + verb + time + opponent": "Soggetto + verbo + tempo + avversario",
    "Watch the ordinal 88e": "Attenzione all'ordinale 88e",
    "schoen zetten is a fixed phrase": "schoen zetten è un'espressione fissa",
    '["journaal = news programme b", "intocht = festive arrival d", "lampion = lantern a", "delen = to share c"]':
        '["journaal = notiziario b", "intocht = arrivo festoso d", "lampion = lanterna a", "delen = condividere c"]',
    "schoen = shoe": "schoen = scarpa",
    "wortel = carrot (for the horse)": "wortel = carota (per il cavallo)",
    "verlanglijstje = wish list": "verlanglijstje = lista dei desideri",
    "cadeautje = little gift": "cadeautje = regalino",
    "18:00 = the Sinterklaas news time": "18:00 = l'ora del notiziario di Sinterklaas",
    "Sanne lives in Utrecht": "Sanne vive a Utrecht",
    "On Wednesday she joins the St Martin's parade": "Mercoledì si unisce alla sfilata di San Martino",
    "She puts a carrot and a wish list in her shoe": "Mette una carota e una lista dei desideri nella sua scarpa",
    "She watches the Sinterklaas news every day at 18:00": "Guarda il notiziario di Sinterklaas ogni giorno alle 18:00",
    "Het diner was published in 2009": "Het diner è stato pubblicato nel 2009",
    "Sinterklaas receives the key to the city at the Maritime Museum":
        "Sinterklaas riceve la chiave della città al Museo marittimo",
    "Pakjesavond is on Saturday 5 December": "Pakjesavond cade sabato 5 dicembre",
    "Grave lies on the river Maas": "Grave si trova sul fiume Mosa",
    "Compare with the article on page 3": "Confronta con l'articolo di pagina 3",
    "Original sentence from page 2 · delen = to share": "Frase originale da pagina 2 · delen = condividere",
    '"The Sinterklaas news is on every day at 18:00. → ___", instr="Translate"':
        '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Traduci in italiano"',
    '"St Martin\'s Day is the festival of sharing. → ___", instr="Translate"':
        '"Sint-Maarten is het feest van het delen. → ___", instr="Traduci in italiano"',
    '"The arrival in Amsterdam is the 88th edition. → ___", instr="Translate"':
        '"L\'arrivo ad Amsterdam è l\'88ª edizione. → ___", instr="Traduci in olandese"',
    '"I put out my shoe, with a wish list inside. → ___", instr="Translate"':
        '"Metto fuori la scarpa, con una lista dei desideri dentro. → ___", instr="Traduci in olandese"',
    '"(open task, model text below)"': '"(compito aperto, testo modello sotto)"',
    "ANTWOORDEN · ANSWER KEY — grouped by page: find your number":
        "ANTWOORDEN · CHIAVE DELLE RISPOSTE — raggruppate per pagina: trova il tuo numero",
    "Every answer with a short note in English · ✓ marks the writing task":
        "Ogni risposta con una breve nota in italiano · ✓ segna il compito di scrittura",
    "schoen zetten = to put out your shoe": "schoen zetten = mettere fuori la scarpa",
    "Netherlands–Greece kicks off on Friday at 20:45": "Paesi Bassi–Grecia, calcio d'inizio venerdì alle 20:45",

})
IT_MAP.update({
    "hij → gaat zetten": "hij → gaat zetten",
    "40 + 20 = 60": "40 + 20 = 60",
    "schoen + -tje: schoentje": "schoen + -tje: schoentje",
    "licht + -je: lichtje": "licht + -je: lichtje",
    "cadeau + -tje: cadeautje": "cadeau + -tje: cadeautje",
    "The Sinterklaas news starts on Monday 9 November.": "Il notiziario di Sinterklaas inizia lunedì 9 novembre.",
    "Writing task (no single answer); model text ({NWORDS} words) below.":
        "Compito di scrittura (senza risposta unica); testo modello ({NWORDS} parole) sotto.",
    "See the model text in section H ({NWORDS} words)":
        "Vedi il testo modello nella sezione H ({NWORDS} parole)",
    '"The Sinterklaas news is on every day at 18:00. → ___", instr="Translate"':
        '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Traduci in italiano"',
    '"St Martin\'s Day is the festival of sharing. → ___", instr="Translate"':
        '"Sint-Maarten is het feest van het delen. → ___", instr="Traduci in italiano"',
    '"The arrival in Amsterdam is the 88th edition. → ___", instr="Translate"':
        '"L\'arrivo ad Amsterdam è l\'88ª edizione. → ___", instr="Traduci in olandese"',
    '"I put out my shoe, with a wish list inside. → ___", instr="Translate"':
        '"Metto fuori la scarpa, con una lista dei desideri dentro. → ___", instr="Traduci in olandese"',
})

IT_MAP.update({
    'p.band("CULTUUR · CULTURE", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · The Sinterklaas news and Het diner")':
        'p.band("CULTUUR · CULTURA", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · Il notiziario di Sinterklaas e Het diner")',
    'e.bridge("Fill in with the words from the box.")': 'e.bridge("Completa con le parole del riquadro.")',
    'e.bridge("Complete with the present perfect. Watch the auxiliaries hebben/zijn.")':
        'e.bridge("Completa al passato prossimo. Attenzione agli ausiliari hebben/zijn.")',
    '"vinden perfectum: heeft gevonden"': '"vinden al perfetto: heeft gevonden"',
    '"lezen perfectum: hebben gelezen"': '"lezen al perfetto: hebben gelezen"',
    'e.bridge("Work it out: answer with the numbers from page 3.")':
        'e.bridge("Calcola: rispondi con i numeri di pagina 3.")',
    '"From 9 to 14 November is 5 days"': '"Dal 9 al 14 novembre sono 5 giorni"',
    '"From 9 to 15 November is 6 days"': '"Dal 9 al 15 novembre sono 6 giorni"',
    '"The Grave programme, 12:00–16:00, lasts 4 hours"': '"Il programma di Grave, 12:00–16:00, dura 4 ore"',
    'f.gloss("de groepsfase = group stage · de kwartfinale = quarter-final · ongeslagen = unbeaten · de interland = international match · de stand = the table.")':
        'f.gloss("de groepsfase = la fase a gironi · de kwartfinale = i quarti di finale · ongeslagen = imbattuto · de interland = la partita internazionale · de stand = la classifica.")',
    '"The Netherlands scored more goals in the group (7 to 5)"': '"I Paesi Bassi hanno segnato più gol nel girone: 7 a 5"',
    '"Eredivisie matchday 13 is on 21–22 November"': '"La 13ª giornata di Eredivisie è il 21–22 novembre"',
    'e.bridge("Fill in with the words from the box. Watch the verb forms.")':
        'e.bridge("Completa con le parole del riquadro. Attenzione alle forme verbali.")',
    '"kwartfinale plural: kwartfinales"': '"kwartfinale, plurale: kwartfinales"',
    '"stand = the table"': '"stand = classifica"',
    'e.bridge("Complete with the past tense or the perfect tense.")':
        'e.bridge("Completa al passato o al perfetto.")',
    '"spelen past tense: speelde"': '"spelen al passato: speelde"',
    '"winnen past tense: won"': '"winnen al passato: won"',
    '"maken past tense: maakte"': '"maken al passato: maakte"',
    '"komen perfectum takes zijn"': '"komen al perfetto vuole zijn"',
    '"True: Netherlands–Greece, Friday 20:45"': '"Vero: Paesi Bassi–Grecia, venerdì 20:45"',
    '"False: Serbia are bottom with 0 points"': '"Falso: la Serbia è ultima con 0 punti"',
    '"False: Eredivisie matchday 13 is on 21–22 November"': '"Falso: la 13ª giornata di Eredivisie è il 21–22 novembre"',
    '"True: PSV beat Willem II 7–0"': '"Vero: il PSV ha battuto il Willem II 7–0"',
    'p.band("JONGEREN · YOUNG PEOPLE", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · Robinson, the shoe and the wish list")':
        'p.band("JONGEREN · GIOVANI", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · Robinson, la scarpa e la lista dei desideri")',
    " (guess with friends who stays longest)": " (indovina con gli amici chi resta più a lungo)",
    " (then put out your shoe, wish list inside)": " (poi metti fuori la scarpa, con la lista dentro)",
    '"On Sunday, do you watch Expeditie Robinson, or would you rather put out your shoe with a wish list? Write two sentences in Dutch and send them in."':
        '"Domenica guardi Expeditie Robinson, o preferisci mettere fuori la scarpa con la lista dei desideri? Scrivi due frasi in olandese e mandale."',
    '"19 contestants"': '"19 concorrenti"',
    '"The show is filmed on a desert island in Malaysia"': '"Il programma è girato su un\'isola deserta in Malesia"',
    '"The contestants spend 34 days on the island"': '"I concorrenti passano 34 giorni sull\'isola"',
    '"kandidaat plural: kandidaten"': '"kandidaat, plurale: kandidaten"',
    'e.bridge("Use gaan + infinitive to talk about the future.")':
        'e.bridge("Parla del futuro con gaan + infinito.")',
    '"True: the show started on 1 November"': '"Vero: il programma è iniziato il 1º novembre"',
    '"False: the show is filmed in Malaysia"': '"Falso: il programma è girato in Malesia"',
    '"False: the carrot in the shoe is for the horse"': '"Falso: la carota nella scarpa è per il cavallo"',
    'f.gloss("de traditie = tradition · griezelen = to scare, to spook · de belangstelling = interest · de achteruitgang = decline · de deskundige = expert.")':
        'f.gloss("de traditie = la tradizione · griezelen = spaventare · de belangstelling = l\'interesse · de achteruitgang = il declino · de deskundige = l\'esperto.")',
    '"Practice data: invented numbers for practice only, not a real survey. Question: what do you do around 11 November? (100 young people)"':
        '"Dati di esercitazione: numeri inventati, non un vero sondaggio. Domanda: cosa fai intorno all\'11 novembre? (100 giovani)"',
    'e.bridge("Answer from the chart on page 6 (practice data).")':
        'e.bridge("Rispondi con il grafico a pagina 6 (dati di esercitazione).")',
    '"The two surveys use different definitions, so they cannot be compared directly"':
        '"I due sondaggi usano definizioni diverse, non si possono confrontare direttamente"',
    '"Interest in St Martin\'s Day increased (Stengs, 2025)"': '"L\'interesse per San Martino è aumentato, secondo Stengs 2025"',
    '"Halloween is about spooking; St Martin\'s Day is about sharing"': '"Halloween è spaventare; San Martino è condividere"',
    '"A tradition lives on when people keep celebrating it"': '"Una tradizione vive quando la gente continua a festeggiarla"',
    '"A tradition lives on when people keep celebrating it."': '"Una tradizione vive quando la gente continua a festeggiarla."',
    '"griezelen = to scare, to spook"': '"griezelen = spaventare"',
    '"Subject + verb + complement + place"': '"Soggetto + verbo + complemento + luogo"',
    '"The als-clause comes last"': '"La frase con als va alla fine"',
    'p.band("TAAL · LANGUAGE", "De Lucerna", "Language focus · Drie niveaus, drie gereedschappen · Three levels, three tools")':
        'p.band("TAAL · LINGUA", "De Lucerna", "Focus sulla lingua · Drie niveaus, drie gereedschappen · Tre livelli, tre strumenti")',
    'a.bridge("de stoomboot = steamboat; de intocht = the festive arrival; de schoen zetten = to put out your shoe; de lampion = lantern.")':
        'a.bridge("de stoomboot = il battello a vapore; de intocht = l\'arrivo festoso; de schoen zetten = mettere fuori la scarpa; de lampion = la lanterna.")',
    '"The intocht is Sinterklaas\'s festive arrival"': '"L\'intocht è l\'arrivo festoso di Sinterklaas"',
    'b.bridge("schoentje = little shoe; lichtje = little light; cadeautje = little present. -je means small and affectionate.")':
        'b.bridge("schoentje = scarpina; lichtje = lucina; cadeautje = regalino. -je significa piccolo e affettuoso.")',
    '"Als Oranje wint… = If Oranje win…"': '"Als Oranje wint… = Se Oranje vince…"',
    '"Sinterklaas is a name, so it takes no article."': '"Sinterklaas è un nome, senza articolo."',
    '"St Martin\'s Day is the festival of sharing: sharing light, food and attention."':
        '"San Martino è la festa della condivisione: condividere luce, cibo e attenzione."',
    '"On Friday 13 November, Oranje play Greece at home."': '"Venerdì 13 novembre Oranje gioca in casa contro la Grecia."',
    'p.band("TOETS EN ANTWOORDEN · TEST AND ANSWERS", "De Lucerna", "Page 8 · De grote toets van de week + alle antwoorden")':
        'p.band("TOETS EN ANTWOORDEN · TEST E RISPOSTE", "De Lucerna", "Pagina 8 · De grote toets van de week + alle antwoorden")',
    '"The Sinterklaas news is on every day at 18:00."': '"Il notiziario di Sinterklaas va in onda ogni giorno alle 18:00."',
    '"schoen zetten is a fixed expression"': '"schoen zetten è un\'espressione fissa"',
    '["journaal = news programme b", "intocht = the festive arrival d", "lampion = lantern a", "delen = to share c"]':
        '["journaal = notiziario b", "intocht = arrivo festoso d", "lampion = lanterna a", "delen = condividere c"]',
    '"cadeautje = little present"': '"cadeautje = regalino"',
    '"Compare with the page 3 article"': '"Confronta con l\'articolo di pagina 3"',
    '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Translate into English"':
        '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Traduci in italiano"',
    '"Sint-Maarten is het feest van het delen. → ___", instr="Translate into English"':
        '"Sint-Maarten is het feest van het delen. → ___", instr="Traduci in italiano"',
    '"The arrival in Amsterdam is the 88th edition. → ___", instr="Translate into Dutch"':
        '"L\'arrivo ad Amsterdam è l\'88ª edizione. → ___", instr="Traduci in olandese"',
    '"I put out my shoe, with a wish list inside. → ___", instr="Translate into Dutch"':
        '"Metto fuori la scarpa, con una lista dei desideri dentro. → ___", instr="Traduci in olandese"',
    '"Every answer has a short note in English · ✓ marks the writing task"':
        '"Ogni risposta con una breve nota in italiano · ✓ segna il compito di scrittura"',
    '"Netherlands–Greece kicks off at 20:45 on Friday"': '"Paesi Bassi–Grecia, calcio d\'inizio venerdì alle 20:45"',
})

# pairs that need special handling
SKIP_IDX = {0, 1, 2, 3, 4, 5, 6, 11, 13}
BADGE_IDX = 14
# pair 7: identity rep on the post-loop Scrittura check form
# pairs 8, 9: P8 Flow/separator — same as EN, pass through unchanged
# pair 10: P8 keys line — IT value 13.0/1.14/0.3 (same as EN)
# pair 13: subtitle — skipped; full-line 36pt rep in furniture below

hdr = '''# -*- coding: utf-8 -*-
"""One-off fan-out transform: W46 NL core (Chinese explanations) -> NL x IT.
Line-literal replacements only, each asserted. Run once from this dir.
Dutch target text, keys (except re-aimed 137/138), facts, images: untouched.
Furniture per the W43/W45 NL x IT registry: badge INSERTED y=568 (strapline
kept), footer SETTIMANALE OLANDESE, gloss prefix Nota —, P8 keys
13.0/1.14/0.3 with Flow 2540 and separators 13.5/1.17/1.5 (EN/DE sizes).
Type tokens TRANSLATED (Cloze/Completa la frase/...); instr words localised;
per-direction Traduci in italiano/olandese. Glosses/bridges use ' = ' + '; '.
Disclosure variable renamed dt_it.
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
    rep(f, "weekly-report-w46-nl-core/svg", "weekly-report-w46-nl-it/svg")

# ---------- types + instr (instrs FIRST, cloze before plain choice) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep_opt(f, 'instr="填空"', 'instr="Completa"')
    rep_opt(f, 'instr="判断"', 'instr="Vero o falso?"')
    rep_opt(f, 'instr="造句"', 'instr="Forma la frase"')
    rep_opt(f, 'instr="写作"', 'instr="Scrivi"')
    rep_opt(f, "完形单选", "Cloze")
    rep_opt(f, "完成句子", "Completa la frase")
    rep_opt(f, "词汇配对", "Abbinamento")
    rep_opt(f, "判断对错", "Vero o falso")
    rep_opt(f, "单选", "Scelta multipla")
    rep_opt(f, "造句", "Forma la frase")
    rep_opt(f, "翻译", "Traduzione")
    rep_opt(f, "写作", "Scrittura")

# ---------- furniture ----------
rep("render.py", "weekly-report-w46-nl-core", "weekly-report-w46-nl-it")
rep("render.py", "De-Lucerna-VOL3.pdf", "De-Lucerna-VOL3-IT.pdf")
rep_opt("render.py", "Render the NL weekly VOL.3", "Render the NL x IT weekly VOL.3")
rep_opt("run.py", "Run the IT weekly", "Run the NL x IT weekly")
rep("bslib4.py", "De Lucerna · 荷兰语周报 VOL.3 · LUCERNA DUTCH WEEKLY",
     "De Lucerna · SETTIMANALE OLANDESE VOL.3 · TESTI IN OLANDESE · SPIEGAZIONI IN ITALIANO")
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} di {total}"')
rep("bslib4.py", "译注｜", "Nota — ")
rep("svglib.py", "for 重阳", "for Double Ninth")
rep("content12.py", 'p.text(975, 330, "荷 兰 语 周 报 · VOL.3 · SINTERKLAAS · SINT-MAARTEN · ORANJE", 40, "serif", True, INK, anchor="middle")',
     'p.text(975, 330, "SETTIMANALE OLANDESE · VOL.3 · SINTERKLAAS · SINT-MAARTEN · ORANJE", 36, "serif", True, INK, anchor="middle")')

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
    if j in SKIP_IDX:
        continue
    if j == 7:
        form = 'if e_["type"] == "Scrittura":'
        out.append((f, form, form))
        continue
    if j == BADGE_IDX:
        badge = ('p.text(975, 568, "TESTI IN OLANDESE · SPIEGAZIONI IN ITALIANO — '
                 'L\'EDIZIONE PER I LETTORI ITALIANI", 20, "sans", True, BRICK, anchor="middle")')
        new_de = old + "\n# pairing badge (brick red, under the band) — W43 NL x IT measured: y=568, 20pt bold BRICK\n" + badge
        out.append((f, old, new_de))
        continue
    if j in (8, 9):
        out.append((f, old, new))
        continue
    if j == 10:
        out.append((f, old, 'af.para(txt, 13.0, lh=1.14, gap=0.3, split=False)'))
        continue
    if "题（无唯一答案）" in old or new.startswith("Writing task (no single answer)"):
        old = old.replace("writing题", "Scrittura题")
        out.append((f, old, IT_MAP[new]))
        continue
    if 'instr="Translate' in old:
        old = old.replace('instr="Translate into English"', 'instr="Traduzione"')
        old = old.replace('instr="Translate into Dutch"', 'instr="Traduzione"')
        old = old.replace('instr="Translate"', 'instr="Traduzione"')
    if "writing题" in old:
        raise SystemExit(f"unexpected writing-form old at pair {j}: {old!r}")
    if new in IT_MAP:
        out.append((f, old, IT_MAP[new]))
    elif len(new) > 1 and new.startswith('"') and new.endswith('"') and new[1:-1] in IT_MAP:
        out.append((f, old, '"' + IT_MAP[new[1:-1]] + '"'))
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
with open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/transform_it.py", "w", encoding="utf-8") as fh:
    fh.write(hdr)
    for f, old, new in ded:
        fh.write(f"rep({f!r}, {old!r}, {new!r})\n")
    fh.write(tail)
print("wrote", len(ded), "reps")
