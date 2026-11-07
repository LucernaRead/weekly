# -*- coding: utf-8 -*-
"""W45 zh-tw x it fan-out transform. Applied ONLY to this build copy.
Line/literal based (never AST byte offsets, never repr literals in
f-strings). Every replacement asserts its expected occurrence count.
Run: python transform.py  (from this build dir; idempotent-guarded: it
refuses to run twice on already-transformed files for unique strings
because counts would fail — re-copy from the core build to re-run.)
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhtw-core"
MY_DIR = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-it"
CORE_DIR_TILDE = "~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhtw-core"
# Default OUT = the delivery dir. Gate 10 may override via env to a scratch
# dir so the solo-repro run never touches delivered files; unset = delivery.
MY_DIR_TILDE = os.environ.get("ZH_TW_IT_OUT", "~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-it")

LOG = []


def rep(path, old, new, count):
    with open(path, encoding="utf-8") as fh:
        s = fh.read()
    n = s.count(old)
    assert n == count, f"{os.path.basename(path)}: expected {count}x {old[:70]!r}, found {n}x"
    s = s.replace(old, new)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(s)
    LOG.append(f"{os.path.basename(path)}: {count}x {old[:60]!r} -> {new[:60]!r}")


def rep_all(path, old, new):
    with open(path, encoding="utf-8") as fh:
        s = fh.read()
    n = s.count(old)
    assert n >= 1, f"{os.path.basename(path)}: expected >=1x {old[:70]!r}, found 0"
    s = s.replace(old, new)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(s)
    LOG.append(f"{os.path.basename(path)}: {n}x {old[:60]!r} -> {new[:60]!r}")


def main():
    # ---- repoint OUT / BASE (core dir -> my delivery dir) ----
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        p = os.path.join(HERE, f)
        rep(p, CORE_DIR_TILDE, MY_DIR_TILDE, 1)
    rp = os.path.join(HERE, "render.py")
    rep(rp, CORE_DIR_TILDE, MY_DIR_TILDE, 1)
    rep(rp, '"Lucerna-VOL2.pdf"', '"Lucerna-VOL2-IT.pdf"', 1)
    rep(rp, '"Lucerna-VOL2-web.pdf"', '"Lucerna-VOL2-IT-web.pdf"', 1)

    # ---- bslib4: footer + gloss prefix (W43 zh-tw-it precedent) ----
    b = os.path.join(HERE, "bslib4.py")
    rep(b, "Lucerna · 繁體中文週報 VOL.2 · 繁體中文正文 · 英語講解 · Traditional Chinese text · English explanations",
        "Lucerna · SETTIMANALE CINESE TRADIZIONALE VOL.2 · TESTI IN CINESE TRADIZIONALE · SPIEGAZIONI IN ITALIANO", 1)
    rep(b, 'f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} di {total}"', 1)
    rep(b, '"Notes｜" + s', '"Nota — " + s', 1)

    c12 = os.path.join(HERE, "content12.py")
    # ---- P1 ----
    rep(c12, 'p.text(975, 378, "繁體中文正文 · 英語講解 — Traditional Chinese text · Explanations in English · the edition for English-speaking readers", 21, "sans", True, OLIVE, anchor="middle")',
        'p.text(975, 378, "TESTI IN CINESE TRADIZIONALE · SPIEGAZIONI IN ITALIANO — L\'EDIZIONE PER I LETTORI ITALIANI", 21, "sans", True, BRICK, anchor="middle")', 1)
    rep(c12, "Staff report · Source: event organisers' press release (Oct 23) and event FAQ",
        "Dalla redazione · Fonte: comunicato stampa degli organizzatori (23 ott.) e FAQ dell'evento", 1)
    rep(c12, "Hong Kong FinTech Week x StartmeupHK 2026 opens Monday (Nov 2) and runs to Friday (Nov 6). The main conference and exhibition are at the Hong Kong Convention and Exhibition Centre on Nov 2-3, with 100+ community events through the week. Expect 45,000+ people from 120+ economies, 1,000+ speakers and 800+ exhibitors and start-ups.",
        "La Hong Kong FinTech Week x StartmeupHK 2026 apre lunedì (2 nov.) e dura fino a venerdì (6 nov.). La conferenza principale e la mostra sono all'Hong Kong Convention and Exhibition Centre il 2–3 nov., con oltre 100 eventi comunitari durante la settimana. Attesi oltre 45.000 partecipanti da più di 120 economie, oltre 1.000 relatori e oltre 800 espositori e start-up.", 1)
    rep(c12, "The Taipei International Travel Fair (ITF) opens Friday (Nov 6) at noon at the Nangang Exhibition Center and runs to Monday (Nov 9): 123 countries and cities, 1,600 booths, a daily 14:00 mascot parade and travel talks.",
        "La Fiera Internazionale del Turismo di Taipei (ITF) apre venerdì (6 nov.) a mezzogiorno al Nangang Exhibition Center e dura fino a lunedì (9 nov.): 123 paesi e città, 1.600 stand, una sfilata quotidiana delle mascotte alle 14:00 e incontri di viaggio.", 1)
    rep(c12, "本週大事 · This week", "本週大事 · Questa settimana", 1)
    rep(c12, "本週一詞 · Word of the week", "本週一詞 · Parola settimanale", 1)
    rep(c12, "「金融科技」 — fintech: using technology to run financial services, like paying by phone or scanning a code to pay.",
        "「金融科技」 — fintech: usare la tecnologia per gestire i servizi finanziari, come pagare con il telefono o scansionando un codice.", 1)
    rep(c12, "快速測驗 · Quick quiz", "快速測驗 · Quiz rapido", 1)
    rep(c12, "標題填空 · Headline words", "標題填空 · Parole dei titoli", 1)
    for old, new in [
        ("FinTech Week opens on Monday, Nov 2.", "La FinTech Week apre lunedì 2 novembre."),
        ("The main conference is at the Hong Kong Convention and Exhibition Centre.", "La conferenza principale è all'Hong Kong Convention and Exhibition Centre."),
        ("More than 45,000 people are expected.", "Sono attesi oltre 45.000 partecipanti."),
        ("The travel fair opens Friday, Nov 6, at noon.", "La fiera dei viaggi apre venerdì 6 novembre a mezzogiorno."),
        ("Participants come from 120+ economies.", "I partecipanti arrivano da oltre 120 economie."),
        ("More than 800 exhibitors and start-ups take part.", "Partecipano oltre 800 espositori e start-up."),
        ("The travel fair gathers 123 countries and cities.", "La fiera dei viaggi riunisce 123 paesi e città."),
        ("The travel fair has 1,600 booths.", "La fiera dei viaggi ha 1.600 stand."),
        ("Saturday, Nov 7 is the Start of Winter solar term.", "Sabato 7 novembre è il termine solare dell'inizio dell'inverno."),
        ("The travel fair runs to Monday, Nov 9.", "La fiera dei viaggi dura fino a lunedì 9 novembre."),
    ]:
        rep(c12, old, new, 1)
    rep_all(c12, 'instr="Fill in"', 'instr="Completa"')
    # ---- P2 ----
    rep(c12, 'p.band("生活 · Life", "Lucerna", "第 2 版 · 天氣、泡湯、旅展與雙11 · Weather, hot springs, the travel fair and 11.11")',
        'p.band("生活 · Vita quotidiana", "Lucerna", "第 2 版 · 天氣、泡湯、旅展與雙11 · Meteo, sorgenti termali, fiera dei viaggi e Doppio 11")', 1)
    rep(c12, "The northeast monsoon cools northern Taiwan, and Saturday (Nov 7) is Lidong, the Start of Winter: the day winter begins in the 24 solar terms. Many people mark it with a hot, nourishing pot meal.",
        "Il monsone di nord-est rinfresca il nord di Taiwan, e sabato (7 nov.) è Lìdōng, l'inizio dell'inverno: il giorno in cui comincia l'inverno nei 24 termini solari. Molti lo celebrano con un pasto caldo e nutriente in pentola.", 1)
    rep(c12, "Autumn and winter are for hot springs and hiking. The travel fair's trail encyclopaedia collects 56 routes, and the 6 Greenways stamp challenge covers the Tamsui-Kavalan, Raknus Selu, Mountain-to-Sea, Centenary, Indigenous and Sugar-Rail trails.",
        "Autunno e inverno sono la stagione delle sorgenti termali e delle escursioni. L'enciclopedia dei sentieri della fiera raccoglie 56 percorsi, e la sfida dei timbri delle 6 Greenway copre i sentieri Tamsui-Kavalan, Raknus Selu, Mountain-to-Sea, Centenary, Indigenous e Sugar-Rail.", 1)
    rep(c12, "練習例子 · Practice example", "練習例子 · Esempio pratico", 1)
    rep(c12, "Practice numbers: NT$2,400 + NT$1,600 = NT$4,000, exactly her budget — so she can buy both.",
        "Conti: 2.400 NT$ + 1.600 NT$ = 4.000 NT$, esattamente il suo budget — quindi può comprare entrambi.", 1)
    rep(c12, "讀懂了嗎? · Did you get it?", "讀懂了嗎? · Hai capito?", 1)
    rep(c12, "填一填 · Fill in", "填一填 · Completa", 1)
    rep(c12, "算一算 · Work it out", "算一算 · Facciamo i conti", 1)
    for old, new in [
        ("Lidong, the Start of Winter, is Saturday, Nov 7.", "Lìdōng, l'inizio dell'inverno, è sabato 7 novembre."),
        ("The northeast monsoon cools northern Taiwan.", "Il monsone di nord-est rinfresca il nord di Taiwan."),
        ("The trail encyclopaedia collects 56 routes.", "L'enciclopedia dei sentieri raccoglie 56 percorsi."),
        ("The stamp challenge has 6 Greenways.", "La sfida dei timbri conta 6 Greenway."),
        ("Double 11 falls on Wednesday, Nov 11.", "Il Doppio 11 cade mercoledì 11 novembre."),
        ("Before paying, check tax, delivery and returns.", "Prima di pagare, controlla tasse, consegna e resi."),
        ("A hot pot meal marks Lidong: 進補.", "Un pasto caldo in pentola celebra Lìdōng: jìnbǔ."),
        ("Check the jacket: mornings and evenings are cool.", "Porta una giacca: mattine e sere sono fresche."),
        ("Autumn and winter are good for hot springs.", "Autunno e inverno sono la stagione delle sorgenti termali."),
        ("Collect stamps on the 6 Greenways.", "Raccogli i timbri delle 6 Greenway."),
        ("Set a budget before Double 11 shopping.", "Stabilisci un budget prima degli acquisti del Doppio 11."),
        ("The Tamsui-Kavalan Trail is one of the 6 Greenways.", "Il sentiero Tamsui-Kavalan è una delle 6 Greenway."),
        ("2,400 + 1,600 = 4,000, exactly the budget.", "2.400 + 1.600 = 4.000, esattamente il budget."),
        ("The budget is 4,000 and the total is 4,000: nothing over.", "Il budget è 4.000 e il totale è 4.000: nessuno sforamento."),
        ("立冬 — the Start of Winter solar term.", "Lìdōng — il termine solare dell'inizio dell'inverno."),
        ("進補 — eating nourishing hot food for winter.", "Jìnbǔ — mangiare cibi caldi e nutrienti per l'inverno."),
        ("泡湯 — soaking in a hot spring.", "Pàotāng — immergersi in una sorgente termale."),
        ("集章 — collecting stamps at set points.", "Jí zhāng — raccogliere timbri in punti stabiliti."),
    ]:
        rep(c12, old, new, 1)
    rep(c12, 'instr="Match"', 'instr="Abbina parola e definizione"', 1)
    rep(c12, "事實框 · This week's facts", "事實框 · I fatti della settimana", 1)
    rep(c12, "你呢? · Over to you", "你呢? · E tu?", 1)
    rep(c12, "What hot pot would you eat for Lidong? What is in your Double 11 cart?",
        "Che pentola calda mangeresti per Lìdōng? Cosa c'è nel tuo carrello del Doppio 11?", 1)
    rep(c12, "封王優惠 · Champion deals", "封王優惠 · Offerte dei campioni", 1)

    c34 = os.path.join(HERE, "content34.py")
    # ---- P3 ----
    rep(c34, 'p.band("文化 · Culture", "Lucerna", "第 3 版 · 立冬、鋼雕與沙雕落幕 · Lidong, steel art and the sand festival finale")',
        'p.band("文化 · Cultura", "Lucerna", "第 3 版 · 立冬、鋼雕與沙雕落幕 · Lìdōng, arte d\'acciaio e finale del festival della sabbia")', 1)
    rep(c34, "Lidong is the first solar term of winter: winter begins. People mark it with hot pot dishes like ginger duck, lamb hotpot and sesame chicken — warming food before the cold months.",
        "Lìdōng è il primo termine solare dell'inverno: l'inverno comincia. La gente lo celebra con piatti caldi in pentola come anatra allo zenzero, hotpot di agnello e pollo al sesamo — cibi che scaldano prima dei mesi freddi.", 1)
    rep(c34, "Kaohsiung's International Steel Sculpture Festival (Oct 23-Nov 22) turns warehouses, factories, the harbour and streets into a stage — SUPER STAGE — with an international forum on making, design and art in daily life.",
        "Il Festival Internazionale di Scultura d'Acciaio di Kaohsiung (23 ott.–22 nov.) trasforma magazzini, fabbriche, porto e strade in un palcoscenico — SUPER STAGE — con un forum internazionale su produzione, design e arte nella vita quotidiana.", 1)
    rep(c34, "The Fulong International Sand Sculpture Art Festival closed Oct 26 after its 19th season (May 29-Oct 26): 40+ sculptures by 15+ artists, built from Fulong's golden sand around film characters from Jurassic World, Shrek, Kung Fu Panda and Back to the Future.",
        "Il Festival Internazionale di Sculture di Sabbia di Fulong si è chiuso il 26 ott. dopo la 19ª edizione (29 mag.–26 ott.): oltre 40 sculture di oltre 15 artisti, costruite con la sabbia dorata di Fulong intorno a personaggi di Jurassic World, Shrek, Kung Fu Panda e Ritorno al futuro.", 1)
    rep_all(c34, "讀懂了嗎? · Did you get it?", "讀懂了嗎? · Hai capito?")
    rep_all(c34, "填一填 · Fill in", "填一填 · Completa")
    rep(c34, "算一算 · Work it out", "算一算 · Facciamo i conti", 1)
    for old, new in [
        ("Lidong means winter begins.", "Lìdōng significa che l'inverno comincia."),
        ("Ginger duck is a typical Lidong dish.", "L'anatra allo zenzero è un piatto tipico di Lìdōng."),
        ("The steel festival runs Oct 23-Nov 22.", "Il festival dell'acciaio dura dal 23 ottobre al 22 novembre."),
        ("The venues include Pier-2's Penglai B3 warehouse.", "Le sedi includono il magazzino Penglai B3 del Pier-2."),
        ("The sand festival closed on Oct 26.", "Il festival della sabbia si è chiuso il 26 ottobre."),
        ("The sand festival made 40+ sculptures.", "Il festival della sabbia ha realizzato oltre 40 sculture."),
        ("Lidong is a solar term (節氣).", "Lìdōng è un termine solare (jiéqì)."),
        ("Sesame chicken is a Lidong dish.", "Il pollo al sesamo è un piatto di Lìdōng."),
        ("Steel is Kaohsiung's material and memory.", "L'acciaio è il materiale e la memoria di Kaohsiung."),
        ("Hamasen Railway Park is a venue.", "Il parco ferroviario di Hamasen è una delle sedi."),
        ("Fulong's sand is golden.", "La sabbia di Fulong è dorata."),
        ("Jurassic World is one of the film characters.", "Jurassic World è uno dei personaggi dei film."),
        ("May 29-31 (3) + Jun 30 + Jul 31 + Aug 31 + Sep 30 + Oct 26 = 151 days.", "29–31 mag. (3) + 30 giu. + 31 lug. + 31 ago. + 30 set. + 26 ott. = 151 giorni."),
        ("Oct 23-31 (9) + Nov 22 = 31 days.", "23–31 ott. (9) + 22 nov. = 31 giorni."),
        ("立冬 — the first solar term of winter.", "Lìdōng — il primo termine solare dell'inverno."),
        ("進補 — nourishing food before winter.", "Jìnbǔ — cibo nutriente prima dell'inverno."),
        ("鋼雕 — sculpture made of steel.", "Gāngdiāo — scultura fatta d'acciaio."),
        ("沙雕 — sculpture built from sand.", "Shādiāo — scultura costruita con la sabbia."),
    ]:
        rep(c34, old, new, 1)
    rep_all(c34, 'instr="Match"', 'instr="Abbina parola e definizione"')
    rep_all(c34, 'instr="Fill in"', 'instr="Completa"')
    rep(c34, "節氣小表 · Solar terms", "節氣小表 · Termini solari", 1)
    rep_all(c34, "你呢? · Over to you", "你呢? · E tu?")
    rep(c34, "Have you seen the Fulong sand sculptures? Which film character would you most want to see in sand?",
        "Hai visto le sculture di sabbia di Fulong? Quale personaggio dei film vorresti più vedere nella sabbia?", 1)
    rep(c34, "鋼雕行程 · Plan your visit", "鋼雕行程 · Pianifica la visita", 1)
    # ---- P4 ----
    rep(c34, 'p.band("體育 · Sport", "Lucerna", "第 4 版 · 台灣大賽封王 · The Taiwan Series is decided")',
        'p.band("體育 · Sport", "Lucerna", "第 4 版 · 台灣大賽封王 · La Serie di Taiwan è decisa")', 1)
    rep(c34, "Staff report · Source: TSNA sports news, Oct 26",
        "Dalla redazione · Fonte: TSNA, notizie sportive, 26 ott.", 1)
    rep(c34, "The Wei Chuan Dragons beat the CTBC Brothers 6-0 in Game 6 (Oct 26, Taipei Dome) to win the 2026 Taiwan Series 4-2 — the first-ever Dragons-Brothers final and the Dragons' 6th title. Starter C.C. Mercedes threw 8 shutout innings and was named Series MVP.",
        "I Wei Chuan Dragons hanno battuto i CTBC Brothers 6-0 in gara 6 (26 ott., Taipei Dome) vincendo la Taiwan Series 2026 per 4-2 — la prima finale Dragons-Brothers di sempre e il 6° titolo dei Dragons. Il partente C.C. Mercedes ha lanciato 8 inning senza subire punti ed è stato nominato MVP della serie.", 1)
    rep(c34, "Four words: 完封 (shutout), 封王 (clinching the title), 全壘打 (home run), MVP (most valuable player).",
        "Quattro parole: 完封 (shutout), 封王 (vincere il titolo), 全壘打 (fuoricampo), MVP (giocatore più prezioso).", 1)
    rep(c34, "第六戰得分走勢 · Game 6 runs by inning — bars drawn in proportion to runs",
        "第六戰得分走勢 · Gara 6, punti per inning — barre in proporzione ai punti", 1)
    rep(c34, "Note: the Dragons did not bat in the bottom of the 9th — leading 6-0 after the top of the 9th, the game was over. 1 + 5 = 6.",
        "Nota: i Dragons non hanno battuto nella parte bassa del 9° inning — in vantaggio 6-0 dopo la parte alta del 9°, la partita era finita. 1 + 5 = 6.", 1)
    rep(c34, "看圖答題 · Read the chart", "看圖答題 · Leggi il grafico", 1)
    for old, new in [
        ("The Dragons won Game 6, 6-0.", "I Dragons hanno vinto gara 6 per 6-0."),
        ("The series ended 4-2 to the Dragons.", "La serie è finita 4-2 per i Dragons."),
        ("Mercedes threw 8 shutout innings.", "Mercedes ha lanciato 8 inning senza subire punti."),
        ("Mercedes was named Series MVP.", "Mercedes è stato nominato MVP della serie."),
        ("The Dragons' 6th title in team history.", "Il 6° titolo della storia dei Dragons."),
        ("Three shutouts in one series is a first.", "Tre shutout in una serie: un primato."),
        ("Game 6 was played at the Taipei Dome.", "Gara 6 si è giocata al Taipei Dome."),
        ("A shutout: the other side scores zero.", "Uno shutout: l'altra squadra segna zero."),
        ("Winning the title is 封王.", "Vincere il titolo è fēng wáng."),
        ("A ball hit out of the park is a home run.", "Una palla battuta fuori dal campo è un fuoricampo."),
        ("Mercedes allowed 1 run in 14 innings.", "Mercedes ha concesso 1 punto in 14 inning."),
        ("The Dragons scored 5 runs in the 8th inning.", "I Dragons hanno segnato 5 punti nell'8° inning."),
        ("The 8th inning: 5 runs, the biggest bar.", "L'8° inning: 5 punti, la barra più grande."),
        ("1 + 5 = 6 runs in total.", "1 + 5 = 6 punti in totale."),
        ("完封 — a shutout: the other side scores zero.", "Wánfēng — uno shutout: l'altra squadra segna zero."),
        ("封王 — clinching the championship.", "Fēng wáng — vincere il campionato."),
        ("全壘打 — a home run.", "Quánlěi dǎ — un fuoricampo."),
        ("安打 — a base hit.", "Āndǎ — una valida."),
    ]:
        rep(c34, old, new, 1)
    rep(c34, "系列賽小檔 · Series file", "系列賽小檔 · Scheda della serie", 1)
    rep(c34, "Which team do you support? Have you ever watched a baseball game live?",
        "Per quale squadra tifi? Hai mai visto una partita di baseball dal vivo?", 1)
    c56 = os.path.join(HERE, "content56.py")
    # ---- P5 ----
    rep(c56, 'p.band("青年 · Youth", "Lucerna", "第 5 版 · 天母萬聖節回顧、旅展攻略 · Halloween recap and the travel-fair game plan")',
        'p.band("青年 · Giovani", "Lucerna", "第 5 版 · 天母萬聖節回顧、旅展攻略 · Halloween a Tianmu e guida alla fiera")', 1)
    rep(c56, "Tianmu's Halloween (Oct 25-26, postponed from Oct 24 by the typhoon): the Oct 25 night parade marched from Shin Kong Mitsukoshi Tianmu along Zhongcheng Road to Dayeh Takashimaya, and the Oct 26 main event ran 13:00-20:00 at Tianmu Sports Park, with 250 shops giving treats and 4,500 pumpkin buckets from three department stores.",
        "L'Halloween di Tianmu (25–26 ott., rinviato dal 24 ott. per il tifone): la sfilata notturna del 25 ott. è partita dallo Shin Kong Mitsukoshi Tianmu lungo Zhongcheng Road fino al Dayeh Takashimaya, e l'evento principale del 26 ott. si è svolto dalle 13:00 alle 20:00 al Tianmu Sports Park, con 250 negozi che offrivano dolcetti e 4.500 secchielli zucca da tre grandi magazzini.", 1)
    rep(c56, "Travel-fair game plan: watch the shows first (Yamagata flower-hat dance, Korea's JUMP taekwondo-comedy show, the daily 14:00 mascot parade), then compare prices — budget fares often exclude checked baggage, so add that cost before you decide.",
        "Guida alla fiera: prima guarda gli spettacoli (la danza dei cappelli di fiori di Yamagata, lo spettacolo JUMP di taekwondo e comicità della Corea, la sfilata quotidiana delle mascotte alle 14:00), poi confronta i prezzi — le tariffe low cost spesso escludono il bagaglio in stiva, quindi aggiungi quel costo prima di decidere.", 1)
    rep(c56, "練習例子 · Practice example", "練習例子 · Esempio pratico", 1)
    rep(c56, "Practice numbers: NT$6,200 − NT$1,200 = NT$5,000, exactly his budget.",
        "Conti: 6.200 NT$ − 1.200 NT$ = 5.000 NT$, esattamente il suo budget.", 1)
    rep(c56, "讀懂了嗎? · Did you get it?", "讀懂了嗎? · Hai capito?", 1)
    rep_all(c56, "填一填 · Fill in", "填一填 · Completa")
    rep(c56, "算一算 · Work it out", "算一算 · Facciamo i conti", 1)
    for old, new in [
        ("The night parade marched on Sunday, Oct 25, at 19:00.", "La sfilata notturna si è svolta domenica 25 ottobre alle 19:00."),
        ("The main event ran 13:00-20:00 at Tianmu Sports Park.", "L'evento principale si è svolto dalle 13:00 alle 20:00 al Tianmu Sports Park."),
        ("250 shops gave treats.", "250 negozi offrivano dolcetti."),
        ("4,500 pumpkin buckets were given out.", "Sono stati distribuiti 4.500 secchielli zucca."),
        ("The mascot parade runs daily at 14:00.", "La sfilata delle mascotte si svolge ogni giorno alle 14:00."),
        ("Budget fares often exclude checked baggage.", "Le tariffe low cost spesso escludono il bagaglio in stiva."),
        ("The parade marched along Zhongcheng Road.", "La sfilata ha percorso Zhongcheng Road."),
        ("The Tamagotchi 30th anniversary collaboration.", "La collaborazione per il 30° anniversario di Tamagotchi."),
        ("The Yamagata flower-hat dance performs on stage.", "La danza dei cappelli di fiori di Yamagata si esibisce sul palco."),
        ("Set a budget before Double 11.", "Stabilisci un budget prima del Doppio 11."),
        ("Add baggage fees before comparing fares.", "Aggiungi le tariffe per il bagaglio prima di confrontare i prezzi."),
        ("List your cart first, then delete what you do not need.", "Elenca prima il carrello, poi elimina ciò che non ti serve."),
        ("6,200 − 1,200 = 5,000, exactly the budget.", "6.200 − 1.200 = 5.000, esattamente il budget."),
        ("The parade starts at 19:00; the main event the next day at 13:00.", "La sfilata parte alle 19:00; l'evento principale il giorno dopo alle 13:00."),
        ("討糖 — trick-or-treating.", "Tǎotáng — dolcetto o scherzetto."),
        ("踩街 — parading through the streets in costume.", "Cǎijiē — sfilare per le strade in costume."),
        ("南瓜桶 — a pumpkin bucket for treats.", "Nánguā tǒng — un secchiello zucca per i dolcetti."),
        ("打卡 — checking in with a photo on social media.", "Dǎkǎ — fare check-in con una foto sui social."),
    ]:
        rep(c56, old, new, 1)
    rep(c56, 'instr="Match"', 'instr="Abbina parola e definizione"', 1)
    rep_all(c56, 'instr="Fill in"', 'instr="Completa"')
    rep(c56, "天母時間表 · Tianmu schedule", "天母時間表 · Programma di Tianmu", 1)
    rep(c56, "你呢? · Over to you", "你呢? · E tu?", 1)
    rep(c56, "Have you ever worn a Halloween costume? Which character would you most want to be?",
        "Hai mai indossato un costume di Halloween? Quale personaggio vorresti più essere?", 1)
    rep(c56, "旅展表演 · Stage shows", "旅展表演 · Spettacoli dal vivo", 1)
    # ---- P6 ----
    rep(c56, 'p.band("深讀 · Deep read", "Lucerna", "第 6 版 · 金融科技週深讀 + 讀圖表 · FinTech in depth, and reading a chart")',
        'p.band("深讀 · Approfondimento", "Lucerna", "第 6 版 · 金融科技週深讀 + 讀圖表 · FinTech in profondità e leggere un grafico")', 1)
    rep(c56, "Staff report · Source: event organisers' press release (Oct 23) and event FAQ",
        "Dalla redazione · Fonte: comunicato stampa degli organizzatori (23 ott.) e FAQ dell'evento", 1)
    rep(c56, "Three plus signs: Finance+ (finance plus technology), AI+ (artificial intelligence inside banks, investment and insurance) and global expansion (helping start-ups sell worldwide). The scale — 45,000+ people, 120+ economies, 1,000+ speakers, 800+ exhibitors and start-ups, 30+ delegations, 100+ community events — shows fintech is now a whole-city topic.",
        "Tre segni più: Finance+ (finanza più tecnologia), IA+ (intelligenza artificiale in banche, investimenti e assicurazioni) ed espansione globale (aiutare le start-up a vendere in tutto il mondo). La portata — oltre 45.000 persone, oltre 120 economie, oltre 1.000 relatori, oltre 800 espositori e start-up, oltre 30 delegazioni, oltre 100 eventi comunitari — mostra che il fintech è ormai un tema di tutta la città.", 1)
    rep(c56, "旅展每日開放時數 · ITF opening hours per day — bars drawn in proportion to hours",
        "旅展每日開放時數 · Ore di apertura ITF al giorno — barre in proporzione alle ore", 1)
    rep(c56, "Source: published fair hours (Nov 6: 12:00-18:00; Nov 7-9: 10:00-18:00). Total: 30 hours.",
        "Fonte: orari ufficiali pubblicati (6 nov.: 12:00–18:00; 7–9 nov.: 10:00–18:00). Totale: 30 ore.", 1)
    rep(c56, "看圖答題 · Read the chart", "看圖答題 · Leggi il grafico", 1)
    rep(c56, "深讀測驗 · Deep-read quiz", "深讀測驗 · Quiz di approfondimento", 1)
    for old, new in [
        ("Nov 6 is the shortest day: 6 hours.", "Il 6 novembre è il giorno più breve: 6 ore."),
        ("Nov 8 runs 10:00-18:00: 8 hours.", "L'8 novembre va dalle 10:00 alle 18:00: 8 ore."),
        ("6 + 8 + 8 + 8 = 30 hours in total.", "6 + 8 + 8 + 8 = 30 ore in totale."),
        ("Nov 6 opens at noon, not 10:00.", "Il 6 novembre apre a mezzogiorno, non alle 10:00."),
        ("Finance+ means finance plus technology.", "Finance+ significa finanza più tecnologia."),
        ("AI helps read data, spot risks and answer clients.", "L'IA aiuta a leggere dati, individuare rischi e rispondere ai clienti."),
        ("Global expansion means selling products worldwide.", "L'espansione globale significa vendere prodotti in tutto il mondo."),
        ("More than 1,000 speakers take part.", "Partecipano oltre 1.000 relatori."),
        ("The main conference runs Nov 2-3.", "La conferenza principale si svolge il 2–3 novembre."),
        ("Community events number 100+ through the week.", "Gli eventi comunitari sono oltre 100 durante la settimana."),
        ("Payments is one of the main-conference topics.", "I pagamenti sono uno dei temi della conferenza principale."),
        ("Digital assets is a main-conference topic.", "Le attività digitali sono un tema della conferenza principale."),
        ("Insurtech is a main-conference topic.", "L'insurtech è un tema della conferenza principale."),
        ("The week connects start-ups with the world.", "La settimana collega le start-up con il mondo."),
        ("Total opening hours: 30.", "Ore totali di apertura: 30."),
        ("Nov 6 opens at noon (12:00).", "Il 6 novembre apre a mezzogiorno (12:00)."),
        ("The travel fair has 1,600 booths.", "La fiera dei viaggi ha 1.600 stand."),
        ("More than 45,000 people are expected.", "Sono attesi oltre 45.000 partecipanti."),
    ]:
        rep(c56, old, new, 1)
    rep(c56, "數字一覽 · By the numbers", "數字一覽 · I numeri", 1)
    rep(c56, "比價提醒 · Compare carefully", "比價提醒 · Confronta con attenzione", 1)
    rep(c56, "Example from press reports (Oct 20): Cathay Pacific Taipei-Tokyo return from NT$13,433 including tax, book by Nov 13. Always compare with baggage fees added — and check the live booking result, as prices vary by date.",
        "Esempio da notizie stampa (20 ott.): Cathay Pacific Taipei-Tokyo andata e ritorno da 13.433 NT$ tasse incluse, prenotazioni entro il 13 nov. Confronta sempre aggiungendo le tariffe per il bagaglio — e verifica il risultato della prenotazione in tempo reale, perché i prezzi variano in base alla data.", 1)

    c7 = os.path.join(HERE, "content7.py")
    # ---- P7 ----
    rep(c7, 'p.band("語言 · Language focus", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Three levels, three topics")',
        'p.band("語言 · Focus sulla lingua", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Tre livelli, tre temi")', 1)
    rep(c7, "A2 · 展會的話 · Fair words", "A2 · 展會的話 · Parole della fiera", 1)
    rep(c7, "This week's fairs give you four useful words: 旅展 (travel fair), 攤位 (booth), 集章 (stamp-collecting) and 吉祥物大遊行 (mascot parade). Learn them once, and the whole travel fair makes sense.",
        "Le fiere di questa settimana ti danno quattro parole utili: 旅展 (fiera dei viaggi), 攤位 (stand), 集章 (raccolta di timbri) e 吉祥物大遊行 (sfilata delle mascotte). Imparale una volta, e tutta la fiera avrà senso.", 1)
    rep(c7, "Four fair words: 旅展, 攤位, 集章, 吉祥物大遊行.",
        "Quattro parole della fiera: 旅展, 攤位, 集章, 吉祥物大遊行.", 1)
    rep(c7, "旅展 is short for 旅行展覽會 (travel exhibition). A 攤位 is one stall inside the fair; the Taipei fair has 1,600 of them. 集章 means collecting stamps at set points — collect all six Greenway stamps and you win a prize.",
        "旅展 è l'abbreviazione di 旅行展覽會 (mostra di viaggi). Un 攤位 è un singolo stand dentro la fiera; la fiera di Taipei ne ha 1.600. 集章 significa raccogliere timbri in punti stabiliti — raccogli tutti e sei i timbri Greenway e vinci un premio.", 1)
    rep(c7, "Practise: 「旅展幾點開門？」 ('What time does the fair open?') — Friday opens at noon, other days at 10:00.",
        "Esercitati: «旅展幾點開門?» («A che ora apre la fiera?») — il venerdì apre a mezzogiorno, gli altri giorni alle 10:00.", 1)
    rep(c7, "B1 · 球賽與節氣 · Games & seasons", "B1 · 球賽與節氣 · Partite e stagioni", 1)
    rep(c7, "Sport and seasons share this week's headlines. Group the words and they stick: winning （封王、完封） and winter （立冬、進補）.",
        "Sport e stagioni condividono i titoli di questa settimana. Raggruppa le parole e restano in mente: vincere （封王、完封） e inverno （立冬、進補）.", 1)
    rep(c7, "Group the words: winning (封王/完封), winter (立冬/進補).",
        "Raggruppa le parole: vincere (封王/完封), inverno (立冬/進補).", 1)
    rep(c7, "封王 means clinching the championship; 完封 means shutting the other side out, 0 runs. 立冬 is the solar term that starts winter; 進補 is eating nourishing hot food before the cold months.",
        "封王 significa vincere il campionato; 完封 significa non far segnare l'altra squadra, 0 punti. 立冬 è il termine solare che dà inizio all'inverno; 進補 è mangiare cibi caldi e nutrienti prima dei mesi freddi.", 1)
    rep(c7, "Memory trick: learn 封王 first, then the way it was won （完封）, then the season it happened in （立冬）.",
        "Trucco di memoria: impara prima 封王, poi il modo in cui è stato vinto （完封）, poi la stagione in cui è successo （立冬）.", 1)
    rep(c7, "B2 · 港台說法 · Local talk", "B2 · 港台說法 · Modi di dire locali", 1)
    rep(c7, "Taiwan and Hong Kong each have their own way of saying things. This week: 打卡 (check in with a photo), 討糖 (trick-or-treat), 踩街 (street parade in costume) and 泡湯 (soak in a hot spring).",
        "Taiwan e Hong Kong hanno ciascuno il proprio modo di dire le cose. Questa settimana: 打卡 (fare check-in con una foto), 討糖 (dolcetto o scherzetto), 踩街 (sfilata in costume) e 泡湯 (immergersi in una sorgente termale).", 1)
    rep(c7, "Four local words from this issue: 打卡, 討糖, 踩街, 泡湯.",
        "Quattro parole locali da questo numero: 打卡, 討糖, 踩街, 泡湯.", 1)
    rep(c7, "打卡 started as clocking in at work, but at a fair or festival it means posting a photo to say 'I was here'. 討糖 is what children say at shops at Halloween; 踩街 is the costumed parade itself; 泡湯 is the autumn pleasure of a hot-spring bath.",
        "打卡 nasceva come timbratura del cartellino al lavoro, ma in una fiera o a un festival significa pubblicare una foto per dire «ero qui». 討糖 è ciò che i bambini dicono nei negozi a Halloween; 踩街 è la sfilata in costume stessa; 泡湯 è il piacere autunnale di un bagno termale.", 1)
    rep(c7, "You don't need many local sayings — learn four and every outing feels closer.",
        "Non ti servono molti modi di dire locali — imparane quattro e ogni uscita sembrerà più vicina.", 1)
    for old, new in [
        ("A booth inside the fair is a 攤位.", "Uno stand dentro la fiera è un tānwèi."),
        ("The mascot parade runs daily at 14:00.", "La sfilata delle mascotte si svolge ogni giorno alle 14:00."),
        ("Collecting stamps at set points is 集章.", "Raccogliere timbri in punti stabiliti è jí zhāng."),
        ("The travel fair is at the Nangang Exhibition Center.", "La fiera dei viaggi è al Nangang Exhibition Center."),
        ("Winning the title is 封王.", "Vincere il titolo è fēng wáng."),
        ("完封 means the other side scores zero.", "Wánfēng significa che l'altra squadra segna zero."),
        ("Lidong starts winter.", "Lìdōng dà inizio all'inverno."),
        ("Ginger duck is a Lidong dish.", "L'anatra allo zenzero è un piatto di Lìdōng."),
        ("At a festival, 打卡 means posting a photo to say you were there.", "A un festival, dǎkǎ significa pubblicare una foto per dire che eri lì."),
        ("Trick-or-treating is 討糖.", "Il dolcetto o scherzetto è tǎotáng."),
        ("踩街 is a costumed street parade.", "Cǎijiē è una sfilata in costume."),
        ("Soaking in a hot spring is 泡湯.", "Immergersi in una sorgente termale è pàotāng."),
    ]:
        rep(c7, old, new, 1)
    rep_all(c7, 'instr="Fill in"', 'instr="Completa"')
    rep(c7, "易錯診所 · Error clinic", "易錯診所 · Clinica degli errori", 1)
    for old, new in [
        ("完勝 means winning big; 完封 means the other side scored zero.", "完勝 significa vincere alla grande; 完封 significa che l'altra squadra ha segnato zero."),
        ("Lidong starts winter; the Solstice is the shortest day. Different terms.", "Lìdōng dà inizio all'inverno; il solstizio è il giorno più corto. Termini diversi."),
        ("Check the city: FinTech Week opens in Hong Kong, not Taipei.", "Controlla la città: la FinTech Week apre a Hong Kong, non a Taipei."),
    ]:
        rep(c7, old, new, 1)
    rep(c7, "本週句式 · Sentence frame", "本週句式 · Struttura settimanale", 1)
    rep(c7, "「先去集章，再去看表演。」 — the frame 先…再… gives the order of two actions: first X, then Y. Make your own: 先比價，再結帳 (compare prices first, then pay).",
        "「先去集章，再去看表演。」 — lo schema 先…再… dà l'ordine di due azioni: prima X, poi Y. Costruisci la tua: 先比價，再結帳 (prima confronta i prezzi, poi paga).", 1)
    rep(c7, "Frame: 先…再… — first X, then Y. Make your own sentence with it.",
        "Schema: 先…再… — prima X, poi Y. Costruisci una frase tua.", 1)
    rep(c7, "讀者園地 · Readers' corner", "讀者園地 · L'angolo dei lettori", 1)
    rep(c7, "An editor's example letter — not a real one. Deferral notice: VOL.1 promised real letters and best page-8 writing from this issue; none publishable had arrived by press time, so the example stays and the invitation stays open.",
        "Una lettera di esempio della redazione — non una vera. Avviso di rinvio: il VOL.1 aveva promesso lettere vere dei lettori e i migliori componimenti di pagina 8 a partire da questo numero; entro la chiusura non ne era arrivato nessuno pubblicabile, quindi resta l'esempio della redazione e l'invito resta aperto. Scrivici: la tua lettera, nel prossimo numero!", 1)
    rep(c7, "本週金句 · Phrases of the week — word for word from this issue's articles",
        "本週金句 · Frasi della settimana — parola per parola dagli articoli di questo numero", 1)
    for old, new in [
        ("Pay by phone, scan to pay, buy insurance online — that is fintech.", "Paga con il telefono, scansiona per pagare, compra assicurazioni online: questo è il fintech."),
        ("123 countries and cities, 1,600 booths.", "123 paesi e città, 1.600 stand."),
        ("Buy what you need; don't buy a pile of things you won't use just for a discount.", "Compra ciò che ti serve; non comprare un mucchio di cose che non userai solo per uno sconto."),
        ("In Kaohsiung, even steel can become a stage.", "A Kaohsiung, anche l'acciaio può diventare un palcoscenico."),
        ("Fulong's summer came to an end on October 26.", "L'estate di Fulong è finita il 26 ottobre."),
        ("A 6-0 shutout of the Brothers, and the Dragons threw the red ribbons.", "Uno shutout per 6-0 contro i Brothers, e i Dragons hanno lanciato i nastri rossi."),
        ("250 shops giving treats together.", "250 negozi che offrono dolcetti insieme."),
        ("On the fair's first day the doors open only at noon.", "Il primo giorno della fiera le porte aprono solo a mezzogiorno."),
    ]:
        rep(c7, old, new, 1)
    rep(c7, "下期預告 · Next week (VOL.3)", "下期預告 · La prossima settimana (VOL.3)", 1)

    c8 = os.path.join(HERE, "content8.py")
    # ---- P8 (IT-column paren style per W43 zh-tw-it build code) ----
    rep(c8, 'p.band("測驗與答案 · Test & keys", "Lucerna", "第 8 版 · 本週大測驗 + 全部答案 · This week\'s test and every answer key")',
        'p.band("測驗與答案 · Test e risposte", "Lucerna", "第 8 版 · 本週大測驗 + 全部答案 · Il test della settimana e tutte le risposte")', 1)
    rep(c8, "A · 判斷對錯 · True or false", "A · 判斷對錯 · Vero o falso", 1)
    rep(c8, "B · 本週大測驗 · The big quiz", "B · 本週大測驗 · Il grande quiz", 1)
    rep(c8, "C · 完成句子 · Fill in", "C · 完成句子 · Completa le frasi", 1)
    rep(c8, "D · 讀一讀,答一答 · Read and answer", "D · 讀一讀,答一答 · Leggi e rispondi", 1)
    rep(c8, "E · 情景說話 · Say it in context", "E · 情景說話 · Dillo nel contesto", 1)
    rep(c8, "F · 寫一寫 · Writing", "F · 寫一寫 · Scrittura", 1)
    for old, new in [
        ("FinTech Week opens Monday, Nov 2.", "La FinTech Week apre lunedì 2 novembre."),
        ("Lidong is Nov 7, not Nov 6.", "Lìdōng è il 7 novembre, non il 6."),
        ("The Dragons won the series 4-2.", "I Dragons hanno vinto la serie 4-2."),
        ("Game 6 ended 6-0, not 6-3.", "Gara 6 è finita 6-0, non 6-3."),
        ("The sand festival closed Oct 26.", "Il festival della sabbia si è chiuso il 26 ottobre."),
        ("The travel fair opens at noon on Nov 6, not 10:00.", "La fiera dei viaggi apre a mezzogiorno il 6 novembre, non alle 10:00."),
        ("The main conference is Nov 2-3.", "La conferenza principale è il 2–3 novembre."),
        ("The travel fair runs to Monday, Nov 9.", "La fiera dei viaggi dura fino a lunedì 9 novembre."),
        ("The steel festival runs to Nov 22.", "Il festival dell'acciaio dura fino al 22 novembre."),
        ("The night parade marched Oct 25 at 19:00.", "La sfilata notturna si è svolta il 25 ottobre alle 19:00."),
        ("Double 11 is Wednesday, Nov 11.", "Il Doppio 11 è mercoledì 11 novembre."),
        ("Mercedes allowed 1 run in 14 innings.", "Mercedes ha concesso 1 punto in 14 inning."),
        ("The mascot parade runs daily at 14:00.", "La sfilata delle mascotte si svolge ogni giorno alle 14:00."),
        ("The trail encyclopaedia collects 56 routes.", "L'enciclopedia dei sentieri raccoglie 56 percorsi."),
        ("Total opening hours: 6 + 8 + 8 + 8 = 30.", "Ore totali di apertura: 6 + 8 + 8 + 8 = 30."),
        ("The stamp challenge covers 6 Greenways.", "La sfida dei timbri copre 6 Greenway."),
        ("Fintech: technology running financial services.", "Fintech: la tecnologia che gestisce i servizi finanziari."),
        ("Lidong starts winter.", "Lìdōng dà inizio all'inverno."),
        ("A shutout: the other side scores zero.", "Uno shutout: l'altra squadra segna zero."),
        ("Winning the title is 封王.", "Vincere il titolo è fēng wáng."),
        ("Trick-or-treating is 討糖.", "Il dolcetto o scherzetto è tǎotáng."),
        ("Collecting stamps is 集章.", "Raccogliere timbri è jí zhāng."),
        ("The travel fair is at the Nangang Exhibition Center.", "La fiera dei viaggi è al Nangang Exhibition Center."),
        ("Pier-2 hosts the steel festival.", "Il Pier-2 ospita il festival dell'acciaio."),
        ("Global expansion: selling products worldwide.", "Espansione globale: vendere prodotti in tutto il mondo."),
        ("AI inside finance is 人工智慧＋.", "L'IA nella finanza: réngōng zhìnéng."),
        ("He goes to the travel fair on Friday at noon.", "Va alla fiera dei viaggi venerdì a mezzogiorno."),
        ("The parade is at 14:00.", "La sfilata è alle 14:00."),
        ("A set of 4 coupons costs 4,100 (list price 8,200).", "Un set di 4 buoni costa 4.100 (prezzo di listino 8.200)."),
        ("He eats ginger duck for Lidong on Saturday.", "Mangia anatra allo zenzero per Lìdōng sabato."),
        ("Order: fair, then Lidong pot, then the coupon set for a buffet.", "Ordine: fiera, poi pentola di Lìdōng, poi il set di buoni per un buffet."),
        ("The travel fair opens Friday at noon.", "La fiera dei viaggi apre venerdì a mezzogiorno."),
        ("Lidong is the first solar term of winter.", "Lìdōng è il primo termine solare dell'inverno."),
        ("A shutout means the other side scores zero.", "Uno shutout significa che l'altra squadra segna zero."),
        ("The mascot parade is at 14:00 daily.", "La sfilata delle mascotte è alle 14:00 ogni giorno."),
        ("Compare prices first, then pay: 先比價，再結帳.", "Prima confronta i prezzi, poi paga: xiān bǐjià, zài jiézhàng."),
    ]:
        rep_all(c8, old, new)
    rep_all(c8, 'instr="Fill in"', 'instr="Completa"')
    rep(c8, 'instr="Writing"', 'instr="Scrittura"', 1)
    rep(c8, 'f.glossline(f"Writing — there is no single right answer. A {NCHARS}-character model follows.")',
        'f.glossline(f"Scrittura — non esiste un\'unica risposta giusta. Segue un modello di {NCHARS} caratteri.")', 1)
    rep(c8, '"(開放題,範文如下)"', '"(domanda aperta — modello qui sotto)"', 1)
    rep(c8, 'f"Open task - the model answer is printed in section F above ({NCHARS} characters)"',
        'f"Domanda aperta — il modello è sopra, in F ({NCHARS} caratteri)"', 1)
    rep(c8, '"Model answer: " + MODELO', '"Risposta modello: " + MODELO', 1)
    rep(c8, "答案 · Answer keys — in page order, with a short English note for every item",
        "答案 · Risposte — in ordine di pagina, con una breve nota in italiano per ogni esercizio", 1)
    rep(c8, "All notes in English · ✓ = the writing model",
        "Tutte le note in italiano · ✓ = il modello di scrittura", 1)
    rep(c8, 'af.para(f"— Page {pg} —"', 'af.para(f"— Pagina {pg} —"', 1)
    rep(c8, 'txt = f"{e_[\'n\']}. {e_[\'key\']} — {e_[\'note\']}"',
        'txt = f"{e_[\'n\']}. {e_[\'key\']} ({e_[\'note\']})"', 1)
    rep(c8, 'txt = f"{e_[\'n\']}. ✓ {e_[\'note\']}"',
        'txt = f"{e_[\'n\']}. ✓ ({e_[\'note\']})"', 1)
    # ---- fix round 2 (folded into the transform, not left as build-copy edits) ----
    # P6 head too wide (498.2 > 434 column): shorten, wording only.
    rep(c56, "深讀測驗 · Quiz di approfondimento", "深讀測驗 · Quiz avanzato", 1)
    # P7 col3 grew +113.52 vs core (clinic +1 line, letters +3 lines), pushing
    # the teaser to 2656.88 over the footer. Shorten clinic #1 by 1 line and
    # the Italian disclosure by 3 lines (same content: example label +
    # deferral + invitation), restoring core geometry exactly.
    rep(c7, "完勝 significa vincere alla grande; 完封 significa che l'altra squadra ha segnato zero.",
        "完勝 = vincere alla grande; 完封 = l'altra squadra segna zero.", 1)
    rep(c7, "Una lettera di esempio della redazione — non una vera. Avviso di rinvio: il VOL.1 aveva promesso lettere vere dei lettori e i migliori componimenti di pagina 8 a partire da questo numero; entro la chiusura non ne era arrivato nessuno pubblicabile, quindi resta l'esempio della redazione e l'invito resta aperto. Scrivici: la tua lettera, nel prossimo numero!",
        "Lettera di esempio della redazione, non vera. Avviso di rinvio: il VOL.1 aveva promesso lettere vere e i migliori testi di pagina 8 da questo numero; alla chiusura non ne era arrivato nessuno pubblicabile, quindi resta l'esempio. Scrivici!", 1)
    # ---- fix round 3: strict-CJK +1 on P7 ----
    # The B1 memory-trick comma sat directly after 封王, so svglib _fw()
    # converted it to a full-width ， that the core does not have.
    # Reword with 'e' instead of the comma (wording only, same meaning).
    rep(c7, "Trucco di memoria: impara prima 封王, poi il modo in cui è stato vinto （完封）, poi la stagione in cui è successo （立冬）.",
        "Trucco di memoria: impara prima 封王 e poi il modo in cui è stato vinto （完封）, poi la stagione in cui è successo （立冬）.", 1)
    # ---- fix round 4: occlusion audit NEW flags (3) ----
    # P5 box title ink 1909.2 > border 1885: drop 'di' (wording only).
    rep(c56, "天母時間表 · Programma di Tianmu", "天母時間表 · Programma Tianmu", 1)
    # P6 box title ink 1920.5 > border 1885: shorter wording, same meaning.
    rep(c56, "比價提醒 · Confronta con attenzione", "比價提醒 · Confronta i prezzi", 1)
    # P7 letters box: last line ink bottom 1756.1 > border 1745.4. The box
    # height formula under-measures the rendered stack by ~6px (the core
    # escapes the same straddle only because its last line's ink centre
    # sits 0.2px outside the audit's expanded box). Add 14px bottom
    # padding so the last line sits inside; teaser moves to 2557.36,
    # still clear of the 2580 footer rule.
    rep(c7, "len(wrap(lcn, \"sans\", False, 20, CW - 44)) * 29 + 26",
        "len(wrap(lcn, \"sans\", False, 20, CW - 44)) * 29 + 40", 1)
    # ---- fix round 5: residual-English sweep of the rendered SVGs ----
    # P4 word-card title kept its English half (missed in the first pass).
    rep(c34, "棒球詞卡 · Baseball words", "棒球詞卡 · Parole del baseball", 1)
    # 'low cost' (P5 gloss + P5 note) -> plain Italian 'economiche'.
    rep(c56, "le tariffe low cost spesso escludono il bagaglio in stiva",
        "le tariffe economiche spesso escludono il bagaglio in stiva", 1)
    rep(c56, "Le tariffe low cost spesso escludono il bagaglio in stiva.",
        "Le tariffe economiche spesso escludono il bagaglio in stiva.", 1)
    print("\n".join(LOG))
    print("TRANSFORM DONE")


if __name__ == "__main__":
    main()
