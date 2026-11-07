# -*- coding: utf-8 -*-
"""W45 zh-tw core (EN explanations) -> zh-tw x DE fan-out transform.

Transform-first discipline: EVERY explanation-layer change lives here.
Run on a fresh copy of the zh-tw core build; never hand-edit build copies.
Usage: python3 transform.py <build_dir> <edition_base_path>
  build_dir: directory holding the core build copy (bslib4.py, content*.py, render.py)
  edition_base_path: OUT/BASE path written into content*/render.py, e.g.
    ~/workspace/.../files/weekly-report-w45-zh-tw-de  (real build) or an
    absolute scratch path (Gate 10 replay).
Rules: whole-string literal replacements only (README #17/#18); each pair
asserts its total occurrence count across the target files before replacing.
Target Traditional Chinese text is NEVER touched by any pair below.
"""
import sys, os

BUILD = sys.argv[1]
EDITION_BASE = sys.argv[2]
CORE_DIRNAME = "weekly-report-w45-zhtw-core"

# (old, new, expected_total_occurrences, files) ; files=None means all content+bslib4+render
CONTENT = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]

PAIRS = [
    # ---- repointing (setup, not content) ----
    # Full OUT/BASE path literal; EDITION_BASE is supplied on the command line
    # (tilde form for the real delivery dir, absolute form for Gate 10 scratch).
    ("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhtw-core",
     None, 6, CONTENT + ["render.py"]),
    ("Lucerna-VOL2-web.pdf", "Lucerna-VOL2-DE-web.pdf", 1, ["render.py"]),
    ("Lucerna-VOL2.pdf", "Lucerna-VOL2-DE.pdf", 1, ["render.py"]),
    # ---- bslib4 furniture ----
    ("Lucerna · 繁體中文週報 VOL.2 · 繁體中文正文 · 英語講解 · Traditional Chinese text · English explanations",
     "Lucerna · CHINESISCHE WOCHENZEITUNG VOL.2 · TEXT AUF CHINESISCH (TRADITIONELL) · ERKLÄRUNGEN AUF DEUTSCH", 1, ["bslib4.py"]),
    ('f"第 {n} 版 / 共 {total} 版"', 'f"Seite {n} von {total}"', 1, ["bslib4.py"]),
    ('("Notes｜" + s,', '("Hinweis · " + s,', 1, ["bslib4.py"]),
    # ---- P1 masthead badge: in-place replacement at y=378, 21pt bold, BRICK (zh-tw family precedent) ----
    ('p.text(975, 378, "繁體中文正文 · 英語講解 — Traditional Chinese text · Explanations in English · the edition for English-speaking readers", 21, "sans", True, OLIVE, anchor="middle")',
     'p.text(975, 378, "CHINESISCHER TEXT (TRADITIONELL) · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", 21, "sans", True, BRICK, anchor="middle")', 1, ["content12.py"]),
    # ---- bylines (apparatus) ----
    ("Staff report · Source: event organisers' press release (Oct 23) and event FAQ",
     "Redaktionsbericht · Quelle: Pressemitteilung der Veranstalter (23. Okt.) und FAQ der Veranstaltung", 2, CONTENT),
    ("Staff report · Source: TSNA sports news, Oct 26",
     "Redaktionsbericht · Quelle: TSNA-Sportnachrichten, 26. Okt.", 1, CONTENT),
    # ---- band titles + subtitles ----
    ("生活 · Life", "生活 · Leben", 1, CONTENT),
    ("文化 · Culture", "文化 · Kultur", 1, CONTENT),
    ("體育 · Sport", "體育 · Sport", 1, CONTENT),  # identical in DE; listed to record the check (no-op guard below)
    ("青年 · Youth", "青年 · Jugend", 1, CONTENT),
    ("深讀 · Deep read", "深讀 · Vertiefung", 1, CONTENT),
    ("語言 · Language focus", "語言 · Sprachfokus", 1, CONTENT),
    ("測驗與答案 · Test & keys", "測驗與答案 · Test & Lösungen", 1, CONTENT),
    ("第 2 版 · 天氣、泡湯、旅展與雙11 · Weather, hot springs, the travel fair and 11.11",
     "第 2 版 · 天氣、泡湯、旅展與雙11 · Wetter, heiße Quellen, Reisemesse und 11.11", 1, CONTENT),
    ("第 3 版 · 立冬、鋼雕與沙雕落幕 · Lidong, steel art and the sand festival finale",
     "第 3 版 · 立冬、鋼雕與沙雕落幕 · Lidong, Stahlkunst und das Sandfestival-Finale", 1, CONTENT),
    ("第 4 版 · 台灣大賽封王 · The Taiwan Series is decided",
     "第 4 版 · 台灣大賽封王 · Die Taiwan Series ist entschieden", 1, CONTENT),
    ("第 5 版 · 天母萬聖節回顧、旅展攻略 · Halloween recap and the travel-fair game plan",
     "第 5 版 · 天母萬聖節回顧、旅展攻略 · Halloween-Rückblick und Reisemesse-Plan", 1, CONTENT),
    ("第 6 版 · 金融科技週深讀 + 讀圖表 · FinTech in depth, and reading a chart",
     "第 6 版 · 金融科技週深讀 + 讀圖表 · FinTech vertieft und Diagramme lesen", 1, CONTENT),
    ("語言聚焦 · 三個級別,三個主題 · Three levels, three topics",
     "語言聚焦 · 三個級別,三個主題 · Drei Stufen, drei Themen", 1, CONTENT),
    ("第 8 版 · 本週大測驗 + 全部答案 · This week's test and every answer key",
     "第 8 版 · 本週大測驗 + 全部答案 · Der große Test der Woche und alle Lösungen", 1, CONTENT),
    # ---- section heads / box titles ----
    ("本週大事 · This week", "本週大事 · Diese Woche", 1, CONTENT),
    ("本週一詞 · Word of the week", "本週一詞 · Wort der Woche", 1, CONTENT),
    ("快速測驗 · Quick quiz", "快速測驗 · Schnelltest", 1, CONTENT),
    ("標題填空 · Headline words", "標題填空 · Schlagzeilenwörter", 1, CONTENT),
    ("讀懂了嗎? · Did you get it?", "讀懂了嗎? · Alles verstanden?", 4, CONTENT),
    ("填一填 · Fill in", "填一填 · Einsetzen", 5, CONTENT),
    ("算一算 · Work it out", "算一算 · Nachrechnen", 3, CONTENT),
    ("看圖答題 · Read the chart", "看圖答題 · Diagramm lesen", 2, CONTENT),
    ("深讀測驗 · Deep-read quiz", "深讀測驗 · Quiz zur Vertiefung", 1, CONTENT),
    ("練習例子 · Practice example", "練習例子 · Übungsbeispiel", 2, CONTENT),
    ("事實框 · This week's facts", "事實框 · Fakten der Woche", 1, CONTENT),
    ("你呢? · Over to you", "你呢? · Und Sie?", 4, CONTENT),
    ("封王優惠 · Champion deals", "封王優惠 · Meisterrabatte", 1, CONTENT),
    ("節氣小表 · Solar terms", "節氣小表 · Solarterme", 1, CONTENT),
    ("鋼雕行程 · Plan your visit", "鋼雕行程 · Besuchsplan", 1, CONTENT),
    ("系列賽小檔 · Series file", "系列賽小檔 · Seriensteckbrief", 1, CONTENT),
    ("天母時間表 · Tianmu schedule", "天母時間表 · Tianmu-Zeitplan", 1, CONTENT),
    ("旅展表演 · Stage shows", "旅展表演 · Bühnenprogramm", 1, CONTENT),
    ("數字一覽 · By the numbers", "數字一覽 · Zahlen im Überblick", 1, CONTENT),
    ("比價提醒 · Compare carefully", "比價提醒 · Preise vergleichen", 1, CONTENT),
    ("棒球詞卡 · Baseball words", "棒球詞卡 · Baseballwörter", 1, CONTENT),
    ("A2 · 展會的話 · Fair words", "A2 · 展會的話 · Messewörter", 1, CONTENT),
    ("B1 · 球賽與節氣 · Games & seasons", "B1 · 球賽與節氣 · Spiele, Jahreszeit", 1, CONTENT),
    ("B2 · 港台說法 · Local talk", "B2 · 港台說法 · Lokale Ausdrücke", 1, CONTENT),
    ("易錯診所 · Error clinic", "易錯診所 · Fehlerklinik", 1, CONTENT),
    ("本週句式 · Sentence frame", "本週句式 · Satzmuster", 1, CONTENT),
    ("讀者園地 · Readers' corner", "讀者園地 · Leserecke", 1, CONTENT),
    ("本週金句 · Phrases of the week — word for word from this issue's articles",
     "本週金句 · Sätze der Woche — Wort für Wort aus den Artikeln dieser Ausgabe", 1, CONTENT),
    ("下期預告 · Next week (VOL.3)", "下期預告 · Nächste Woche (VOL.3)", 1, CONTENT),
    ("A · 判斷對錯 · True or false", "A · 判斷對錯 · Richtig oder falsch", 1, CONTENT),
    ("B · 本週大測驗 · The big quiz", "B · 本週大測驗 · Das große Quiz", 1, CONTENT),
    ("C · 完成句子 · Fill in", "C · 完成句子 · Einsetzen", 1, CONTENT),
    ("D · 讀一讀,答一答 · Read and answer", "D · 讀一讀,答一答 · Lesen & antworten", 1, CONTENT),
    ("E · 情景說話 · Say it in context", "E · 情景說話 · Im Kontext sagen", 1, CONTENT),
    ("F · 寫一寫 · Writing", "F · 寫一寫 · Schreiben", 1, CONTENT),
    # ---- instruction words ----
    ('instr="Fill in"', 'instr="Ausfüllen"', 54, CONTENT),
    ('instr="Match"', 'instr="Zuordnen"', 4, CONTENT),
    ('instr="Writing"', 'instr="Schreiben"', 1, CONTENT),
    # ---- P8 keys furniture ----
    ("答案 · Answer keys — in page order, with a short English note for every item",
     "答案 · Lösungen — in Seitenreihenfolge, mit einer kurzen deutschen Anmerkung zu jeder Aufgabe", 1, CONTENT),
    ("All notes in English · ✓ = the writing model",
     "Alle Anmerkungen auf Deutsch · ✓ = der Schreib-Mustertext", 1, CONTENT),
    ('f"— Page {pg} —"', 'f"— Seite {pg} —"', 1, CONTENT),
    ('f"Writing — there is no single right answer. A {NCHARS}-character model follows."',
     'f"Schreiben — es gibt keine einzige richtige Antwort. Es folgt ein Mustertext mit {NCHARS} Zeichen."', 1, CONTENT),
    ('f"Open task - the model answer is printed in section F above ({NCHARS} characters)"',
     'f"Offene Aufgabe — der Mustertext steht oben in Abschnitt F ({NCHARS} Zeichen)"', 1, CONTENT),
    ('"(開放題,範文如下)"', '"(offene Aufgabe — Mustertext unten)"', 1, CONTENT),
    ('"Model answer: " + MODELO', '"Mustertext: " + MODELO', 1, CONTENT),
]

PAIRS += [
    # ---- gloss boxes (12) ----
    ("Hong Kong FinTech Week x StartmeupHK 2026 opens Monday (Nov 2) and runs to Friday (Nov 6). The main conference and exhibition are at the Hong Kong Convention and Exhibition Centre on Nov 2-3, with 100+ community events through the week. Expect 45,000+ people from 120+ economies, 1,000+ speakers and 800+ exhibitors and start-ups.",
     "Die Hong Kong FinTech Week x StartmeupHK 2026 eröffnet am Montag (2. Nov.) und läuft bis Freitag (6. Nov.). Hauptkonferenz und Ausstellung sind am 2.–3. Nov. im Hong Kong Convention and Exhibition Centre, dazu über 100 Gemeinschaftsveranstaltungen in der Woche. Erwartet werden über 45.000 Menschen aus über 120 Volkswirtschaften, über 1.000 Rednerinnen und Redner sowie über 800 Aussteller und Start-ups.", 1, CONTENT),
    ("The Taipei International Travel Fair (ITF) opens Friday (Nov 6) at noon at the Nangang Exhibition Center and runs to Monday (Nov 9): 123 countries and cities, 1,600 booths, a daily 14:00 mascot parade and travel talks.",
     "Die Taipei International Travel Fair (ITF) eröffnet am Freitag (6. Nov.) mittags im Nangang Exhibition Center und läuft bis Montag (9. Nov.): 123 Länder und Städte, 1.600 Stände, täglich um 14:00 Uhr eine Maskottchenparade und Reisevorträge.", 1, CONTENT),
    ("The northeast monsoon cools northern Taiwan, and Saturday (Nov 7) is Lidong, the Start of Winter: the day winter begins in the 24 solar terms. Many people mark it with a hot, nourishing pot meal.",
     "Der Nordostmonsun kühlt Nordtaiwan ab, und Samstag (7. Nov.) ist Lidong, Winterbeginn: der Tag, an dem der Winter in den 24 Solarterminen beginnt. Viele begehen ihn mit einem heißen, nährenden Topfgericht.", 1, CONTENT),
    ("Autumn and winter are for hot springs and hiking. The travel fair's trail encyclopaedia collects 56 routes, and the 6 Greenways stamp challenge covers the Tamsui-Kavalan, Raknus Selu, Mountain-to-Sea, Centenary, Indigenous and Sugar-Rail trails.",
     "Herbst und Winter sind für heiße Quellen und Wandern da. Die Wander-Enzyklopädie der Reisemesse versammelt 56 Routen, und die 6-Greenways-Stempelaktion umfasst die Trails Tamsui-Kavalan, Raknus Selu, Mountain-to-Sea, Centenary, Indigenous und Sugar-Rail.", 1, CONTENT),
    ("Lidong is the first solar term of winter: winter begins. People mark it with hot pot dishes like ginger duck, lamb hotpot and sesame chicken — warming food before the cold months.",
     "Lidong ist der erste Solartermin des Winters: Der Winter beginnt. Man begeht ihn mit Topfgerichten wie Ingwerente, Lamm-Hotpot und Sesamhuhn — wärmendem Essen vor den kalten Monaten.", 1, CONTENT),
    ("Kaohsiung's International Steel Sculpture Festival (Oct 23-Nov 22) turns warehouses, factories, the harbour and streets into a stage — SUPER STAGE — with an international forum on making, design and art in daily life.",
     "Kaohsiungs Internationales Stahlskulpturen-Festival (23. Okt.–22. Nov.) verwandelt Lagerhallen, Fabriken, Hafen und Straßen in eine Bühne — SUPER STAGE — mit einem internationalen Forum über Herstellen, Design und Kunst im Alltag.", 1, CONTENT),
    ("The Fulong International Sand Sculpture Art Festival closed Oct 26 after its 19th season (May 29-Oct 26): 40+ sculptures by 15+ artists, built from Fulong's golden sand around film characters from Jurassic World, Shrek, Kung Fu Panda and Back to the Future.",
     "Das Fulong International Sand Sculpture Art Festival endete am 26. Okt. nach seiner 19. Saison (29. Mai–26. Okt.): über 40 Skulpturen von über 15 Künstlerinnen und Künstlern, aus Fulongs goldenem Sand gebaut, rund um Filmfiguren aus Jurassic World, Shrek, Kung Fu Panda und Back to the Future.", 1, CONTENT),
    ("The Wei Chuan Dragons beat the CTBC Brothers 6-0 in Game 6 (Oct 26, Taipei Dome) to win the 2026 Taiwan Series 4-2 — the first-ever Dragons-Brothers final and the Dragons' 6th title. Starter C.C. Mercedes threw 8 shutout innings and was named Series MVP.",
     "Die Wei Chuan Dragons schlugen die CTBC Brothers im 6. Spiel mit 6:0 (26. Okt., Taipei Dome) und gewannen die Taiwan Series 2026 mit 4:2 — das erste Dragons-Brothers-Finale überhaupt und der 6. Titel der Dragons. Starter C.C. Mercedes warf 8 Shutout-Innings und wurde Series MVP.", 1, CONTENT),
    ("Four words: 完封 (shutout), 封王 (clinching the title), 全壘打 (home run), MVP (most valuable player).",
     "Vier Wörter: 完封 (Shutout), 封王 (Meisterschaft sichern), 全壘打 (Home Run), MVP (wertvollster Spieler).", 1, CONTENT),
    ("Tianmu's Halloween (Oct 25-26, postponed from Oct 24 by the typhoon): the Oct 25 night parade marched from Shin Kong Mitsukoshi Tianmu along Zhongcheng Road to Dayeh Takashimaya, and the Oct 26 main event ran 13:00-20:00 at Tianmu Sports Park, with 250 shops giving treats and 4,500 pumpkin buckets from three department stores.",
     "Tianmus Halloween (25.–26. Okt., vom 24. Okt. wegen des Taifuns verschoben): Die Nachtparade am 25. Okt. zog von Shin Kong Mitsukoshi Tianmu über die Zhongcheng Road nach Dayeh Takashimaya, und die Hauptveranstaltung am 26. Okt. lief 13:00–20:00 Uhr im Tianmu Sports Park, mit 250 Geschäften, die Süßes verteilten, und 4.500 Kürbiseimern von drei Kaufhäusern.", 1, CONTENT),
    ("Travel-fair game plan: watch the shows first (Yamagata flower-hat dance, Korea's JUMP taekwondo-comedy show, the daily 14:00 mascot parade), then compare prices — budget fares often exclude checked baggage, so add that cost before you decide.",
     "Reisemesse-Plan: erst die Shows ansehen (Yamagata-Blumenhut-Tanz, Koreas JUMP-Taekwondo-Comedy-Show, die tägliche Maskottchenparade um 14:00 Uhr), dann Preise vergleichen — Billigtarife enthalten oft kein Aufgabegepäck, also erst diese Kosten dazurechnen.", 1, CONTENT),
    ("Three plus signs: Finance+ (finance plus technology), AI+ (artificial intelligence inside banks, investment and insurance) and global expansion (helping start-ups sell worldwide). The scale — 45,000+ people, 120+ economies, 1,000+ speakers, 800+ exhibitors and start-ups, 30+ delegations, 100+ community events — shows fintech is now a whole-city topic.",
     "Drei Pluszeichen: Finance+ (Finanzen plus Technik), AI+ (künstliche Intelligenz in Banken, Investment und Versicherungen) und globale Expansion (Start-ups helfen, weltweit zu verkaufen). Das Ausmaß — über 45.000 Menschen, über 120 Volkswirtschaften, über 1.000 Rednerinnen und Redner, über 800 Aussteller und Start-ups, über 30 Delegationen, über 100 Gemeinschaftsveranstaltungen — zeigt: Fintech ist jetzt ein Thema der ganzen Stadt.", 1, CONTENT),
    # ---- word of the week, practice examples, chart titles/notes, compare box ----
    ("「金融科技」 — fintech: using technology to run financial services, like paying by phone or scanning a code to pay.",
     "「金融科技」 — Fintech: Finanzdienstleistungen mit Technik betreiben, etwa per Handy überweisen oder per Code bezahlen.", 1, CONTENT),
    ("Practice numbers: NT$2,400 + NT$1,600 = NT$4,000, exactly her budget — so she can buy both.",
     "Übungszahlen: NT$2.400 + NT$1.600 = NT$4.000, genau ihr Budget — sie kann also beides kaufen.", 1, CONTENT),
    ("Practice numbers: NT$6,200 − NT$1,200 = NT$5,000, exactly his budget.",
     "Übungszahlen: NT$6.200 − NT$1.200 = NT$5.000, genau sein Budget.", 1, CONTENT),
    ("第六戰得分走勢 · Game 6 runs by inning — bars drawn in proportion to runs",
     "第六戰得分走勢 · Spiel-6-Punkte nach Inning — Balken proportional zu den Punkten", 1, CONTENT),
    ("Note: the Dragons did not bat in the bottom of the 9th — leading 6-0 after the top of the 9th, the game was over. 1 + 5 = 6.",
     "Hinweis: Die Dragons schlugen im unteren 9. Inning nicht mehr — nach dem oberen 9. Inning führten sie 6:0, das Spiel war vorbei. 1 + 5 = 6.", 1, CONTENT),
    ("旅展每日開放時數 · ITF opening hours per day — bars drawn in proportion to hours",
     "旅展每日開放時數 · ITF-Öffnungszeiten pro Tag — Balken proportional zu den Stunden", 1, CONTENT),
    ("Source: published fair hours (Nov 6: 12:00-18:00; Nov 7-9: 10:00-18:00). Total: 30 hours.",
     "Quelle: veröffentlichte Messezeiten (6. Nov.: 12:00–18:00 Uhr; 7.–9. Nov.: 10:00–18:00 Uhr). Insgesamt: 30 Stunden.", 1, CONTENT),
    ("Example from press reports (Oct 20): Cathay Pacific Taipei-Tokyo return from NT$13,433 including tax, book by Nov 13. Always compare with baggage fees added — and check the live booking result, as prices vary by date.",
     "Beispiel aus Pressemeldungen (20. Okt.): Cathay Pacific Taipeh–Tokio hin und zurück ab NT$13.433 inkl. Steuern, Buchung bis 13. Nov. Immer erst mit Gepäckgebühren vergleichen — und das Live-Buchungsergebnis prüfen, denn die Preise variieren je nach Datum.", 1, CONTENT),
    # ---- Over to you questions ----
    ("What hot pot would you eat for Lidong? What is in your Double 11 cart?",
     "Welchen Hotpot würden Sie zu Lidong essen? Was liegt in Ihrem 11.11-Warenkorb?", 1, CONTENT),
    ("Have you seen the Fulong sand sculptures? Which film character would you most want to see in sand?",
     "Haben Sie die Sandskulpturen in Fulong schon gesehen? Welche Filmfigur würden Sie am liebsten in Sand sehen?", 1, CONTENT),
    ("Which team do you support? Have you ever watched a baseball game live?",
     "Welches Team unterstützen Sie? Haben Sie schon einmal ein Baseballspiel live gesehen?", 1, CONTENT),
    ("Have you ever worn a Halloween costume? Which character would you most want to be?",
     "Haben Sie schon einmal ein Halloweenkostüm getragen? Welche Figur wären Sie am liebsten?", 1, CONTENT),
    # ---- P7 columns ----
    ("This week's fairs give you four useful words: 旅展 (travel fair), 攤位 (booth), 集章 (stamp-collecting) and 吉祥物大遊行 (mascot parade). Learn them once, and the whole travel fair makes sense.",
     "Die Messen dieser Woche geben Ihnen vier nützliche Wörter: 旅展 (Reisemesse), 攤位 (Stand), 集章 (Stempelsammeln) und 吉祥物大遊行 (Maskottchenparade). Einmal gelernt, ist die ganze Messe klar.", 1, CONTENT),
    ("Four fair words: 旅展, 攤位, 集章, 吉祥物大遊行.",
     "Vier Messewörter: 旅展, 攤位, 集章, 吉祥物大遊行.", 1, CONTENT),
    ("旅展 is short for 旅行展覽會 (travel exhibition). A 攤位 is one stall inside the fair; the Taipei fair has 1,600 of them. 集章 means collecting stamps at set points — collect all six Greenway stamps and you win a prize.",
     "旅展 ist kurz für 旅行展覽會 (Reiseausstellung). Ein 攤位 ist ein Stand in der Messe; Taipeh hat 1.600 davon. 集章 heißt Stempel an festen Punkten sammeln — alle sechs Greenway-Stempel bringen einen Preis.", 1, CONTENT),
    ("Practise: 「旅展幾點開門？」 ('What time does the fair open?') — Friday opens at noon, other days at 10:00.",
     "Üben Sie: 「旅展幾點開門？」 („Wann öffnet die Messe?“) — freitags erst mittags, sonst um 10:00 Uhr.", 1, CONTENT),
    ("Sport and seasons share this week's headlines. Group the words and they stick: winning （封王、完封） and winter （立冬、進補）.",
     "Sport und Jahreszeiten teilen sich die Schlagzeilen dieser Woche. In Gruppen gelernt, bleiben die Wörter haften: Gewinnen （封王、完封） und Winter （立冬、進補）.", 1, CONTENT),
    ("Group the words: winning (封王/完封), winter (立冬/進補).",
     "In Gruppen lernen: Gewinnen (封王/完封), Winter (立冬/進補).", 1, CONTENT),
    ("封王 means clinching the championship; 完封 means shutting the other side out, 0 runs. 立冬 is the solar term that starts winter; 進補 is eating nourishing hot food before the cold months.",
     "封王 heißt die Meisterschaft sichern; 完封 heißt die andere Seite ohne Punkte lassen, 0 Runs. 立冬 ist der Solartermin, der den Winter beginnt; 進補 heißt vor der Kälte nahrhaftes, heißes Essen.", 1, CONTENT),
    ("Memory trick: learn 封王 first, then the way it was won （完封）, then the season it happened in （立冬）.",
     "Merktrick: zuerst 封王 lernen, dann die Art des Sieges （完封）, dann die Jahreszeit （立冬）.", 1, CONTENT),
    ("Taiwan and Hong Kong each have their own way of saying things. This week: 打卡 (check in with a photo), 討糖 (trick-or-treat), 踩街 (street parade in costume) and 泡湯 (soak in a hot spring).",
     "Taiwan und Hongkong sagen manches auf eigene Art. Diese Woche: 打卡 (Foto-Check-in), 討糖 (Süßes einfordern), 踩街 (Kostümparade) und 泡湯 (Quellbad).", 1, CONTENT),
    ("Four local words from this issue: 打卡, 討糖, 踩街, 泡湯.",
     "Vier lokale Wörter aus dieser Ausgabe: 打卡, 討糖, 踩街, 泡湯.", 1, CONTENT),
    ("打卡 started as clocking in at work, but at a fair or festival it means posting a photo to say 'I was here'. 討糖 is what children say at shops at Halloween; 踩街 is the costumed parade itself; 泡湯 is the autumn pleasure of a hot-spring bath.",
     "打卡 hieß zuerst Einstempeln am Arbeitsplatz, auf Festen aber: ein Foto posten — Ich war hier. 討糖 sagen Kinder an Halloween in Geschäften; 踩街 ist die Kostümparade selbst; 泡湯 ist das Herbstvergnügen im heißen Quellbad.", 1, CONTENT),
    ("You don't need many local sayings — learn four and every outing feels closer.",
     "Vier Ausdrücke genügen — und jeder Ausflug fühlt sich näher an.", 1, CONTENT),
    # ---- error clinic notes ----
    ("完勝 means winning big; 完封 means the other side scored zero.",
     "hoch gewinnen heißt 完勝 und null Punkte für die andere Seite heißt 完封.", 1, CONTENT),
    ("Lidong starts winter; the Solstice is the shortest day. Different terms.",
     "Lidong: Winterbeginn; Sonnenwende: kürzester Tag. Verschiedene Begriffe.", 1, CONTENT),
    ("Check the city: FinTech Week opens in Hong Kong, not Taipei.",
     "Stadt prüfen: FinTech Week in Hongkong, nicht Taipeh.", 1, CONTENT),
    # ---- sentence frame ----
    ("「先去集章，再去看表演。」 — the frame 先…再… gives the order of two actions: first X, then Y. Make your own: 先比價，再結帳 (compare prices first, then pay).",
     "「先去集章，再去看表演。」 — 先…再… = erst X, dann Y. Bilden Sie selbst einen Satz: 先比價，再結帳 (erst vergleichen, dann bezahlen).", 1, CONTENT),
    ("Frame: 先…再… — first X, then Y. Make your own sentence with it.",
     "Muster 先…再…: erst X, dann Y — selbst einen Satz bilden.", 1, CONTENT),
    # ---- readers corner disclosure (German: no genuine letters + open invitation) ----
    ("An editor's example letter — not a real one. Deferral notice: VOL.1 promised real letters and best page-8 writing from this issue; none publishable had arrived by press time, so the example stays and the invitation stays open.",
     "Beispielbrief der Redaktion — kein echter Brief. VOL.1 versprach echte Briefe und die beste Seite-8-Aufgabe ab dieser Ausgabe; bis Redaktionsschluss kam nichts Veröffentlichbares — das Beispiel bleibt, und die Einladung bleibt offen: Schicken Sie uns Ihren Brief!", 1, CONTENT),
    # ---- P7 phrases ----
    ("Pay by phone, scan to pay, buy insurance online — that is fintech.",
     "Per Handy überweisen, per Scan bezahlen, online versichern — das ist Fintech.", 1, CONTENT),
    ("123 countries and cities, 1,600 booths.",
     "123 Länder und Städte, 1.600 Stände.", 1, CONTENT),
    ("Buy what you need; don't buy a pile of things you won't use just for a discount.",
     "Kaufen Sie, was Sie brauchen; kaufen Sie keinen Stapel Dinge, die Sie nicht nutzen, nur wegen eines Rabatts.", 1, CONTENT),
    ("In Kaohsiung, even steel can become a stage.",
     "In Kaohsiung kann sogar Stahl zur Bühne werden.", 1, CONTENT),
    ("Fulong's summer came to an end on October 26.",
     "Fulongs Sommer endete am 26. Oktober.", 1, CONTENT),
    ("A 6-0 shutout of the Brothers, and the Dragons threw the red ribbons.",
     "Ein 6:0-Shutout gegen die Brothers, und die Dragons warfen die roten Bänder.", 1, CONTENT),
    ("250 shops giving treats together.",
     "250 Geschäfte verteilen gemeinsam Süßes.", 1, CONTENT),
    ("On the fair's first day the doors open only at noon.",
     "Am ersten Messetag öffnen die Türen erst mittags.", 1, CONTENT),
    ('"p. 1"', '"S. 1"', 2, CONTENT),
    ('"p. 2"', '"S. 2"', 1, CONTENT),
    ('"p. 3"', '"S. 3"', 2, CONTENT),
    ('"p. 4"', '"S. 4"', 1, CONTENT),
    ('"p. 5"', '"S. 5"', 1, CONTENT),
    ('"p. 6"', '"S. 6"', 1, CONTENT),
]

PAIRS += [
    # ---- layout fixes (folded into the transform; never direct build-copy edits) ----
    # P2 Over-to-you box: German question wraps one line longer than the English
    # (audit: ink 1326.4 > border 1322.0). Grow 230 -> 250 (W43 DE precedent grew
    # its P2 box the same way) and shift the Champion-deals box +20. Scoped to
    # content12.py only: content34.py P4 carries an identical rect literal whose
    # box is clean and must not move.
    ('p.rect(rx, by + 488, CW, 230, fill="#f1ead6", stroke=LINE, sw=1.4)',
     'p.rect(rx, by + 488, CW, 250, fill="#f1ead6", stroke=LINE, sw=1.4)', 1, ["content12.py"]),
    ("by3 = by + 488 + 230 + 18", "by3 = by + 488 + 250 + 18", 1, ["content12.py"]),
    # P7 readers box: auto-height formula underestimates the German disclosure's
    # ink descent by 5.9px (audit: ink 1749.8 > border 1743.9). Add 14px bottom
    # padding to the readers-box height only; teaser then ends at 2555.86, still
    # clear of the 2580 footer rule.
    ("len(wrap(lcn, \"sans\", False, 20, CW - 44)) * 29 + 26",
     "len(wrap(lcn, \"sans\", False, 20, CW - 44)) * 29 + 40", 1, ["content7.py"]),
]

PAIRS += [
    # ---- exercise notes (order matters: longer strings before their prefixes) ----
    ("FinTech Week opens on Monday, Nov 2.", "Die FinTech Week eröffnet am Montag, 2. Nov.", 1, CONTENT),
    ("The main conference is at the Hong Kong Convention and Exhibition Centre.", "Die Hauptkonferenz ist im Hong Kong Convention and Exhibition Centre.", 1, CONTENT),
    ("More than 45,000 people are expected.", "Über 45.000 Menschen werden erwartet.", 2, CONTENT),
    ("The travel fair opens Friday, Nov 6, at noon.", "Die Reisemesse eröffnet am Freitag, 6. Nov., mittags.", 1, CONTENT),
    ("Participants come from 120+ economies.", "Die Teilnehmer kommen aus über 120 Volkswirtschaften.", 1, CONTENT),
    ("More than 800 exhibitors and start-ups take part.", "Über 800 Aussteller und Start-ups nehmen teil.", 1, CONTENT),
    ("The travel fair gathers 123 countries and cities.", "Die Reisemesse versammelt 123 Länder und Städte.", 1, CONTENT),
    ("The travel fair has 1,600 booths.", "Die Reisemesse hat 1.600 Stände.", 2, CONTENT),
    ("Saturday, Nov 7 is the Start of Winter solar term.", "Samstag, 7. Nov., ist der Solartermin Winterbeginn.", 1, CONTENT),
    ("The travel fair runs to Monday, Nov 9.", "Die Reisemesse läuft bis Montag, 9. Nov.", 2, CONTENT),
    ("Lidong, the Start of Winter, is Saturday, Nov 7.", "Lidong, der Winterbeginn, ist am Samstag, 7. Nov.", 1, CONTENT),
    ("The northeast monsoon cools northern Taiwan.", "Der Nordostmonsun kühlt Nordtaiwan ab.", 1, CONTENT),
    ("The trail encyclopaedia collects 56 routes.", "Die Wander-Enzyklopädie versammelt 56 Routen.", 2, CONTENT),
    ("The stamp challenge has 6 Greenways.", "Die Stempelaktion hat 6 Greenways.", 1, CONTENT),
    ("Double 11 falls on Wednesday, Nov 11.", "Double 11 fällt auf Mittwoch, 11. Nov.", 1, CONTENT),
    ("Before paying, check tax, delivery and returns.", "Vor dem Bezahlen Steuern, Lieferung und Rückgabe prüfen.", 1, CONTENT),
    ("A hot pot meal marks Lidong: 進補.", "Ein Topfgericht zu Lidong heißt 進補.", 1, CONTENT),
    ("Check the jacket: mornings and evenings are cool.", "An die Jacke denken: Morgens und abends ist es kühl.", 1, CONTENT),
    ("Autumn and winter are good for hot springs.", "Herbst und Winter sind gut für heiße Quellen.", 1, CONTENT),
    ("Collect stamps on the 6 Greenways.", "Stempel auf den 6 Greenways sammeln.", 1, CONTENT),
    ("Set a budget before Double 11 shopping.", "Vor dem Double-11-Einkauf ein Budget festlegen.", 1, CONTENT),
    ("Set a budget before Double 11.", "Vor Double 11 ein Budget festlegen.", 1, CONTENT),
    ("The Tamsui-Kavalan Trail is one of the 6 Greenways.", "Der Tamsui-Kavalan-Trail ist einer der 6 Greenways.", 1, CONTENT),
    ("2,400 + 1,600 = 4,000, exactly the budget.", "2.400 + 1.600 = 4.000, genau das Budget.", 1, CONTENT),
    ("The budget is 4,000 and the total is 4,000: nothing over.", "Das Budget ist 4.000 und die Summe ist 4.000: nichts darüber.", 1, CONTENT),
    ("立冬 — the Start of Winter solar term.", "立冬 — der Solartermin Winterbeginn.", 1, CONTENT),
    ("進補 — eating nourishing hot food for winter.", "進補 — nahrhaftes, heißes Essen für den Winter.", 1, CONTENT),
    ("泡湯 — soaking in a hot spring.", "泡湯 — in einer heißen Quelle baden.", 1, CONTENT),
    ("集章 — collecting stamps at set points.", "集章 — Stempel an festen Punkten sammeln.", 1, CONTENT),
    ("Lidong means winter begins.", "Lidong heißt: Der Winter beginnt.", 1, CONTENT),
    ("Ginger duck is a typical Lidong dish.", "Ingwerente ist ein typisches Lidong-Gericht.", 1, CONTENT),
    ("The steel festival runs Oct 23-Nov 22.", "Das Stahlfestival läuft vom 23. Okt. bis 22. Nov.", 1, CONTENT),
    ("The venues include Pier-2's Penglai B3 warehouse.", "Zu den Orten gehört Pier-2s Penglai-B3-Lagerhaus.", 1, CONTENT),
    ("The sand festival closed on Oct 26.", "Das Sandfestival endete am 26. Okt.", 1, CONTENT),
    ("The sand festival made 40+ sculptures.", "Das Sandfestival schuf über 40 Skulpturen.", 1, CONTENT),
    ("Lidong is a solar term (節氣).", "Lidong ist ein Solartermin (節氣).", 1, CONTENT),
    ("Sesame chicken is a Lidong dish.", "Sesamhuhn ist ein Lidong-Gericht.", 1, CONTENT),
    ("Steel is Kaohsiung's material and memory.", "Stahl ist Kaohsiungs Material und Erinnerung.", 1, CONTENT),
    ("Hamasen Railway Park is a venue.", "Der Hamasen Railway Park ist ein Veranstaltungsort.", 1, CONTENT),
    ("Fulong's sand is golden.", "Fulongs Sand ist golden.", 1, CONTENT),
    ("Jurassic World is one of the film characters.", "Jurassic World ist eine der Filmfiguren.", 1, CONTENT),
    ("May 29-31 (3) + Jun 30 + Jul 31 + Aug 31 + Sep 30 + Oct 26 = 151 days.", "29.–31. Mai (3) + 30. Juni + 31. Juli + 31. Aug. + 30. Sept. + 26. Okt. = 151 Tage.", 1, CONTENT),
    ("Oct 23-31 (9) + Nov 22 = 31 days.", "23.–31. Okt. (9) + 22. Nov. = 31 Tage.", 1, CONTENT),
    ("立冬 — the first solar term of winter.", "立冬 — der erste Solartermin des Winters.", 1, CONTENT),
    ("進補 — nourishing food before winter.", "進補 — nahrhafte Speisen vor dem Winter.", 1, CONTENT),
    ("鋼雕 — sculpture made of steel.", "鋼雕 — Skulptur aus Stahl.", 1, CONTENT),
    ("沙雕 — sculpture built from sand.", "沙雕 — Skulptur aus Sand gebaut.", 1, CONTENT),
    ("The Dragons won Game 6, 6-0.", "Die Dragons gewannen Spiel 6 mit 6:0.", 1, CONTENT),
    ("The series ended 4-2 to the Dragons.", "Die Serie endete 4:2 für die Dragons.", 1, CONTENT),
    ("Mercedes threw 8 shutout innings.", "Mercedes warf 8 Shutout-Innings.", 1, CONTENT),
    ("Mercedes was named Series MVP.", "Mercedes wurde Series MVP.", 1, CONTENT),
    ("The Dragons' 6th title in team history.", "Der 6. Titel der Dragons in der Vereinsgeschichte.", 1, CONTENT),
    ("Three shutouts in one series is a first.", "Drei Shutouts in einer Serie sind eine Premiere.", 1, CONTENT),
    ("Game 6 was played at the Taipei Dome.", "Spiel 6 wurde im Taipei Dome ausgetragen.", 1, CONTENT),
    ("A shutout: the other side scores zero.", "Ein Shutout: Die andere Seite punktet nullmal.", 2, CONTENT),
    ("Winning the title is 封王.", "Den Titel gewinnen heißt 封王.", 3, CONTENT),
    ("A ball hit out of the park is a home run.", "Ein Ball aus dem Park geschlagen ist ein Home Run.", 1, CONTENT),
    ("Mercedes allowed 1 run in 14 innings.", "Mercedes ließ in 14 Innings 1 Run zu.", 2, CONTENT),
    ("The Dragons scored 5 runs in the 8th inning.", "Die Dragons erzielten im 8. Inning 5 Runs.", 1, CONTENT),
    ("The 8th inning: 5 runs, the biggest bar.", "Das 8. Inning: 5 Runs, der größte Balken.", 1, CONTENT),
    ("1 + 5 = 6 runs in total.", "1 + 5 = 6 Runs insgesamt.", 1, CONTENT),
    ("完封 — a shutout: the other side scores zero.", "完封 — ein Shutout: Die andere Seite punktet nullmal.", 1, CONTENT),
    ("封王 — clinching the championship.", "封王 — die Meisterschaft sichern.", 1, CONTENT),
    ("全壘打 — a home run.", "全壘打 — ein Home Run.", 1, CONTENT),
    ("安打 — a base hit.", "安打 — ein Base Hit.", 1, CONTENT),
    ("The night parade marched on Sunday, Oct 25, at 19:00.", "Die Nachtparade zog am Sonntag, 25. Okt., um 19:00 Uhr.", 1, CONTENT),
    ("The main event ran 13:00-20:00 at Tianmu Sports Park.", "Die Hauptveranstaltung lief 13:00–20:00 Uhr im Tianmu Sports Park.", 1, CONTENT),
    ("250 shops gave treats.", "250 Geschäfte verteilten Süßes.", 1, CONTENT),
    ("4,500 pumpkin buckets were given out.", "4.500 Kürbiseimer wurden verteilt.", 1, CONTENT),
    ("The mascot parade runs daily at 14:00.", "Die Maskottchenparade läuft täglich um 14:00 Uhr.", 3, CONTENT),
    ("Budget fares often exclude checked baggage.", "Billigtarife enthalten oft kein Aufgabegepäck.", 1, CONTENT),
    ("The parade marched along Zhongcheng Road.", "Die Parade zog entlang der Zhongcheng Road.", 1, CONTENT),
    ("The Tamagotchi 30th anniversary collaboration.", "Die Tamagotchi-Kooperation zum 30. Jubiläum.", 1, CONTENT),
    ("The Yamagata flower-hat dance performs on stage.", "Der Yamagata-Blumenhut-Tanz tritt auf der Bühne auf.", 1, CONTENT),
    ("Add baggage fees before comparing fares.", "Vor dem Preisvergleich Gepäckgebühren dazurechnen.", 1, CONTENT),
    ("List your cart first, then delete what you do not need.", "Zuerst den Warenkorb auflisten, dann streichen, was man nicht braucht.", 1, CONTENT),
    ("6,200 − 1,200 = 5,000, exactly the budget.", "6.200 − 1.200 = 5.000, genau das Budget.", 1, CONTENT),
    ("The parade starts at 19:00; the main event the next day at 13:00.", "Die Parade beginnt um 19:00 Uhr; die Hauptveranstaltung am nächsten Tag um 13:00 Uhr.", 1, CONTENT),
    ("討糖 — trick-or-treating.", "討糖 — Süßes einfordern.", 1, CONTENT),
    ("踩街 — parading through the streets in costume.", "踩街 — Parade in Kostüm durch die Straßen.", 1, CONTENT),
    ("南瓜桶 — a pumpkin bucket for treats.", "南瓜桶 — ein Kürbiseimer für Süßes.", 1, CONTENT),
    ("打卡 — checking in with a photo on social media.", "打卡 — mit Foto in sozialen Medien einchecken.", 1, CONTENT),
    ("Nov 6 is the shortest day: 6 hours.", "Der 6. Nov. ist der kürzeste Tag: 6 Stunden.", 1, CONTENT),
    ("Nov 8 runs 10:00-18:00: 8 hours.", "Der 8. Nov. läuft 10:00–18:00 Uhr: 8 Stunden.", 1, CONTENT),
    ("6 + 8 + 8 + 8 = 30 hours in total.", "6 + 8 + 8 + 8 = 30 Stunden insgesamt.", 1, CONTENT),
    ("Nov 6 opens at noon, not 10:00.", "Der 6. Nov. öffnet mittags, nicht um 10:00 Uhr.", 1, CONTENT),
    ("Finance+ means finance plus technology.", "Finance+ heißt Finanzen plus Technik.", 1, CONTENT),
    ("AI helps read data, spot risks and answer clients.", "KI hilft, Daten zu lesen, Risiken zu erkennen und Kunden zu antworten.", 1, CONTENT),
    ("Global expansion means selling products worldwide.", "Globale Expansion heißt Produkte weltweit verkaufen.", 1, CONTENT),
    ("More than 1,000 speakers take part.", "Über 1.000 Rednerinnen und Redner nehmen teil.", 1, CONTENT),
    ("The main conference runs Nov 2-3.", "Die Hauptkonferenz läuft am 2.–3. Nov.", 1, CONTENT),
    ("Community events number 100+ through the week.", "Die Gemeinschaftsveranstaltungen zählen über 100 in der Woche.", 1, CONTENT),
    ("Payments is one of the main-conference topics.", "Zahlungen ist eines der Hauptkonferenz-Themen.", 1, CONTENT),
    ("Digital assets is a main-conference topic.", "Digitale Vermögenswerte ist ein Hauptkonferenz-Thema.", 1, CONTENT),
    ("Insurtech is a main-conference topic.", "Insurtech ist ein Hauptkonferenz-Thema.", 1, CONTENT),
    ("The week connects start-ups with the world.", "Die Woche verbindet Start-ups mit der Welt.", 1, CONTENT),
    ("Total opening hours: 30.", "Öffnungszeiten insgesamt: 30.", 1, CONTENT),
    ("Nov 6 opens at noon (12:00).", "Der 6. Nov. öffnet mittags (12:00 Uhr).", 1, CONTENT),
    ("A booth inside the fair is a 攤位.", "Ein Stand in der Messe ist ein 攤位.", 1, CONTENT),
    ("Collecting stamps at set points is 集章.", "Stempel an festen Punkten sammeln heißt 集章.", 1, CONTENT),
    ("The travel fair is at the Nangang Exhibition Center.", "Die Reisemesse ist im Nangang Exhibition Center.", 2, CONTENT),
    ("完封 means the other side scores zero.", "完封 heißt: Die andere Seite punktet nullmal.", 1, CONTENT),
    ("Lidong starts winter.", "Lidong beginnt den Winter.", 2, CONTENT),
    ("Ginger duck is a Lidong dish.", "Ingwerente ist ein Lidong-Gericht.", 1, CONTENT),
    ("At a festival, 打卡 means posting a photo to say you were there.", "Auf einem Fest postet man mit 打卡 ein Foto und zeigt: Ich war da.", 1, CONTENT),
    ("Trick-or-treating is 討糖.", "Süßes einfordern heißt 討糖.", 2, CONTENT),
    ("踩街 is a costumed street parade.", "踩街 ist eine Straßenparade im Kostüm.", 1, CONTENT),
    ("Soaking in a hot spring is 泡湯.", "In einer heißen Quelle baden heißt 泡湯.", 1, CONTENT),
    ("FinTech Week opens Monday, Nov 2.", "Die FinTech Week eröffnet am Montag, 2. Nov.", 1, CONTENT),
    ("Lidong is Nov 7, not Nov 6.", "Lidong ist am 7. Nov., nicht am 6. Nov.", 1, CONTENT),
    ("The Dragons won the series 4-2.", "Die Dragons gewannen die Serie mit 4:2.", 2, CONTENT),
    ("Game 6 ended 6-0, not 6-3.", "Spiel 6 endete 6:0, nicht 6:3.", 1, CONTENT),
    ("The sand festival closed Oct 26.", "Das Sandfestival endete am 26. Okt.", 1, CONTENT),
    ("The travel fair opens at noon on Nov 6, not 10:00.", "Die Reisemesse öffnet am 6. Nov. mittags, nicht um 10:00 Uhr.", 1, CONTENT),
    ("The main conference is Nov 2-3.", "Die Hauptkonferenz ist am 2.–3. Nov.", 1, CONTENT),
    ("The steel festival runs to Nov 22.", "Das Stahlfestival läuft bis 22. Nov.", 1, CONTENT),
    ("The night parade marched Oct 25 at 19:00.", "Die Nachtparade zog am 25. Okt. um 19:00 Uhr.", 1, CONTENT),
    ("Double 11 is Wednesday, Nov 11.", "Double 11 ist am Mittwoch, 11. Nov.", 1, CONTENT),
    ("The stamp challenge covers 6 Greenways.", "Die Stempelaktion umfasst 6 Greenways.", 1, CONTENT),
    ("Total opening hours: 6 + 8 + 8 + 8 = 30.", "Öffnungszeiten insgesamt: 6 + 8 + 8 + 8 = 30.", 1, CONTENT),
    ("Fintech: technology running financial services.", "Fintech: Technik, die Finanzdienstleistungen betreibt.", 1, CONTENT),
    ("Collecting stamps is 集章.", "Stempel sammeln heißt 集章.", 1, CONTENT),
    ("Pier-2 hosts the steel festival.", "Pier-2 beherbergt das Stahlfestival.", 1, CONTENT),
    ("Global expansion: selling products worldwide.", "Globale Expansion: Produkte weltweit verkaufen.", 1, CONTENT),
    ("AI inside finance is 人工智慧＋.", "KI im Finanzwesen ist 人工智慧＋.", 1, CONTENT),
    ("He goes to the travel fair on Friday at noon.", "Er geht am Freitag mittags zur Reisemesse.", 1, CONTENT),
    ("The parade is at 14:00.", "Die Parade ist um 14:00 Uhr.", 1, CONTENT),
    ("A set of 4 coupons costs 4,100 (list price 8,200).", "Ein Set aus 4 Gutscheinen kostet 4.100 (Listenpreis 8.200).", 1, CONTENT),
    ("He eats ginger duck for Lidong on Saturday.", "Er isst am Samstag zu Lidong Ingwerente.", 1, CONTENT),
    ("Order: fair, then Lidong pot, then the coupon set for a buffet.", "Reihenfolge: Messe, dann Lidong-Topf, dann das Gutscheinset fürs Buffet.", 1, CONTENT),
    ("The travel fair opens Friday at noon.", "Die Reisemesse eröffnet am Freitag mittags.", 1, CONTENT),
    ("Lidong is the first solar term of winter.", "Lidong ist der erste Solartermin des Winters.", 1, CONTENT),
    ("A shutout means the other side scores zero.", "Ein Shutout heißt: Die andere Seite punktet nullmal.", 1, CONTENT),
    ("The mascot parade is at 14:00 daily.", "Die Maskottchenparade ist täglich um 14:00 Uhr.", 1, CONTENT),
    ("Compare prices first, then pay: 先比價，再結帳.", "Erst Preise vergleichen, dann bezahlen: 先比價，再結帳.", 1, CONTENT),
]


def main():
    texts = {}
    for fname in set(f for _, _, _, fl in PAIRS for f in fl):
        path = os.path.join(BUILD, fname)
        texts[fname] = open(path, encoding="utf-8").read()
    for idx, (old, new, expected, fl) in enumerate(PAIRS):
        if new is None:
            new = EDITION_BASE
        total = sum(texts[f].count(old) for f in fl)
        assert total == expected, (
            f"PAIR {idx} count mismatch for {old[:70]!r}: found {total}, expected {expected}")
        if old == new:
            print(f"pair {idx}: check-only (identical) {old[:60]!r} x{total}")
            continue
        for f in fl:
            texts[f] = texts[f].replace(old, new)
        print(f"pair {idx}: replaced x{total} {old[:60]!r}")
    for fname, s in texts.items():
        open(os.path.join(BUILD, fname), "w", encoding="utf-8").write(s)
    print(f"TRANSFORM DONE: {len(PAIRS)} pairs applied in {BUILD}")


if __name__ == "__main__":
    main()
