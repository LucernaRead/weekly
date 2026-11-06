# -*- coding: utf-8 -*-
"""One-off generator: JA x EN transform -> JA x NL transform.

Reads the sibling W45 JA x EN transform.py (kept here as
transform-en-reference.py, read-only input), keeps every OLD (Chinese /
frozen) string byte-identical, and replaces every NEW (English) string
with its Dutch rendering per the shipped W43 JA x NL precedent
(files/weekly-report-ja-nl, badge/footer/page-line/gloss-prefix/section
heads) plus fresh Dutch translations of the W45 notes. Output is
transform.py in this directory. After generation, transform.py is the
single source of the edition build (ja-de precedent: gen_transform.py
kept alongside for provenance).
"""
import ast
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "transform-en-reference.py")
DST = os.path.join(HERE, "transform.py")

# Exact English new-side string -> Dutch rendering. Keys must match the
# EN transform's new sides verbatim (full string, or a substring where
# the new side is a whole code line, e.g. the masthead badge line).
EN2NL = {
    # --- GLOBAL: registry type names / instructions ---
    'instr="Build a sentence"': 'instr="Bouw een zin"',
    'instr="Translate"': 'instr="Vertaal"',
    'instr="Writing"': 'instr="Schrijven"',
    'instr="True or false?"': 'instr="Waar of onwaar?"',
    'instr="Fill in"': 'instr="Vul in"',
    'instr="Match words to meanings"': 'instr="Koppel woorden aan betekenissen"',
    'instr="Match events to places and dates"': 'instr="Koppel activiteiten aan plaatsen en tijden"',
    '"cloze"': '"gatentekst"',
    '"multiple choice"': '"meerkeuze"',
    '"fill-in"': '"zinnen aanvullen"',
    '"matching"': '"combineren"',
    '"sentence building"': '"zinnen bouwen"',
    '"true/false"': '"waar of onwaar"',
    '"translation"': '"vertalen"',
    '"writing"': '"schrijven"',
    # --- GLOBAL: shared furniture ---
    '"あなたは？ \u00b7 Your turn"': '"あなたは？ \u00b7 En jij?"',
    '"Answers on page 8 · Levels are mixed — find your number"': '"Antwoorden op pagina 8 · Niveaus gemengd: zoek je nummer op"',
    # --- NOTES (answer-note renderings) ---
    "Culture Day is November 3 (Tuesday)": "Cultuurdag is op 3 november (dinsdag)",
    "Reading Week runs to November 9 (Monday)": "De Leesweek loopt tot 9 november (maandag)",
    "The Kobe illuminations start on the 7th (Saturday)": "De verlichting in Kobe begint op 7 november (zaterdag)",
    "Culture Day brings cultural events nationwide": "Op Cultuurdag overal culturele activiteiten",
    "The illuminations start in Kobe": "De verlichting in Kobe begint",
    "Nabe dinners are 1.5 times last year's": "Nabe-avonden zijn 1,5 keer zoveel als vorig jaar",
    "The announcement was October 21": "De aankondiging was op 21 oktober",
    "Temperatures are above average from November to January": "Temperaturen november–januari hoger dan gemiddeld",
    "The clothing and food topics come from the note roundup": "De kleding- en eettips komen uit het note-overzicht",
    "Nabe ingredients appeared a month early": "Nabe-ingrediënten lagen een maand eerder in de winkels",
    "The JMA forecast was October 20": "De voorspelling van het JMA was op 20 oktober",
    "The Suginami event is a family orchestra": "Het evenement in Suginami is een familieorkest",
    "The craft exhibition is at the Ishikawa Prefectural Museum of Art": "De ambachtstentoonstelling is in het Ishikawa Prefectural Museum of Art",
    "The exhibition runs to November 8": "De tentoonstelling loopt tot 8 november",
    "The light-up is at Kanazawa Castle and Kenrokuen": "De verlichting is bij Kasteel Kanazawa en Kenrokuen",
    "The exhibition runs to November 8 (Sunday)": "De tentoonstelling loopt tot 8 november (zondag)",
    "Game 1: SoftBank beat DeNA 3–1": "Wedstrijd 1: SoftBank won met 3–1 van DeNA",
    "Tsutsugo's 3-run homer turned Game 2 around": "Tsutsugo's homerun van 3 punten bracht in wedstrijd 2 de ommekeer",
    "SoftBank started with two straight wins": "SoftBank begon met twee zeges op rij",
    "Teams starting 2–0 win the title 73% of the time": "Teams met een 2–0-start worden in 73% kampioen",
    "DeNA won the title in 2024": "In 2024 werd DeNA kampioen",
    "SoftBank scored 3 in Game 1": "In wedstrijd 1 scoorde SoftBank 3 punten",
    "SoftBank scored 4 in Game 2": "In wedstrijd 2 scoorde SoftBank 4 punten",
    "Game 1 went to 11 innings": "Wedstrijd 1 duurde tot de 11e inning",
    "Game 2 went to 10 innings": "Wedstrijd 2 duurde tot de 10e inning",
    "Title rate 73%": "Kampioenspercentage 73%",
    "Game 1 crowd: 33,388": "Wedstrijd 1: 33.388 toeschouwers",
    "Game 2 crowd: 33,432": "Wedstrijd 2: 33.432 toeschouwers",
    "Manager Aikawa spoke of a four-win fight": "Manager Aikawa sprak van een strijd om vier zeges",
    "Game 1 was on Saturday": "Wedstrijd 1 was op zaterdag",
    "SoftBank won two straight": "SoftBank won twee keer op rij",
    "Game 2 also went to extra innings": "Wedstrijd 2 ging ook naar verlenging",
    "DeNA won in 2024": "In 2024 won DeNA de titel",
    "Halloween was October 31 (Saturday)": "Halloween was op 31 oktober (zaterdag)",
    "Shibuya's street-drinking ban runs 18:00 to 05:00": "In Shibuya geldt het drinkverbod op straat van 18.00 tot 5.00 uur",
    "Littering costs a 2,000-yen fine": "Afval op straat gooien kost een boete van 2.000 yen",
    "The cosplay festival is in Ikebukuro": "Het verkleedfestival is in Ikebukuro",
    "The Naka Ward festival is November 8 (Sunday)": "Het Naka-festival in Yokohama is op 8 november (zondag)",
    "Halloween was October 31": "Halloween was op 31 oktober",
    "The ban starts at 18:00": "Het verbod begint om 18.00 uur",
    "The ban runs to 05:00": "Het verbod loopt tot 5.00 uur 's ochtends",
    "The Yokohama festival is November 8": "Het festival in Yokohama is op 8 november",
    "No drinking on the street at night": "'s Nachts mag je niet op straat drinken",
    "The litter fine dates from June this year": "De afvalboete geldt sinds juni van dit jaar",
    "立冬 is November 7 (Saturday)": "立冬 is op 7 november (zaterdag)",
    "立冬 is November 7": "立冬 is op 7 november",
    "Halloween was October 31 (Saturday)": "Halloween was op 31 oktober (zaterdag)",
    "The festival ran October 30 to November 1": "Het festival duurde van 30 oktober tot 1 november",
    "The Pacific side gets more rain": "De Pacifische kant krijgt meer regen",
    "Kyushu travel searches nearly doubled year on year": "Zoekopdrachten voor Kyushu-reizen zijn bijna verdubbeld ten opzichte van vorig jaar",
    "The budget per trip fell": "Het budget per reis is gedaald",
    "Naruko Gorge peaks over the October 31 – November 8 weekend": "Naruko-kloof is op haar mooist in het weekend van 31 oktober tot 8 november",
    "The chart's top answer is nearby satisfaction": "Het populairste antwoord in de grafiek is voldoening dichtbij",
    "Nearby satisfaction: 38%": "Voldoening dichtbij: 38%",
    "Hot springs: 27%": "Onsen: 27%",
    "Leaves 21% minus food 14% is 7": "Bladeren 21% min eten 14% is 7",
    "All four add up to 100%": "Alle vier samen zijn 100%",
    "The Kobe light-up runs to December 28": "De verlichting in Kobe loopt tot 28 december",
    "Kyushu travel searches are nearly twice last year's": "Zoekopdrachten voor Kyushu-reizen zijn ongeveer twee keer zoveel als vorig jaar",
    "The JMA forecast was October 20": "De JMA-voorspelling was op 20 oktober",
    "November is forecast warmer than average": "November wordt naar verwachting warmer dan gemiddeld",
    "Kyushu travel searches rose": "Zoekopdrachten voor Kyushu-reizen zijn toegenomen",
    "The chart is practice data": "De grafiek bevat oefengegevens",
    "Reading Week started October 27 (Tuesday)": "De Leesweek begon op 27 oktober (dinsdag)",
    "Reading Week runs to November 9": "De Leesweek loopt tot 9 november",
    "The library event is book introductions": "Het bibliotheekevenement biedt boekintroducties",
    "Game 2: SoftBank won 4–3": "Wedstrijd 2: SoftBank won met 4–3",
    "The Kobe light-up starts on the 7th": "De verlichting in Kobe begint op de 7e",
    "Title rate for 2–0 starts: 73%": "Kampioenspercentage bij een 2–0-start: 73%",
    "The JMA forecast: warmer than average": "Het JMA voorspelt temperaturen boven het gemiddelde",
    "On Tuesday Mika goes to Kanazawa with her family": "Op dinsdag gaat Mika met haar familie naar Kanazawa",
    "In Kanazawa she sees the craft exhibition and the light-up": "In Kanazawa bekijkt ze de ambachtstentoonstelling en de verlichting",
    "On Saturday she goes to Kobe with friends": "Op zaterdag gaat ze met vrienden naar Kobe",
    "She wants to borrow 2 books for Reading Week": "Voor de Leesweek wil ze 2 boeken lenen",
    "starting with two straight wins": "beginnen met twee zeges op rij",
    "Reading Week runs to November 9 (page 7)": "De Leesweek loopt tot 9 november (pagina 7)",
    "See page 3": "Zie pagina 3",
    "See page 5": "Zie pagina 5",
    "See page 7": "Zie pagina 7",
    "See page 6 (Kobe illuminations)": "Zie pagina 6 (de verlichting in Kobe)",
}

EN2NL.update({
    # --- NOTES: gloss-style (Japanese headword + Dutch gloss) ---
    "見頃 = best viewing season": "見頃 = mooiste periode om te kijken",
    "立冬 = the start of winter": "立冬 = het begin van de winter",
    "「ゆる」 = not forcing it": "「ゆる」 = jezelf niet forceren",
    "ゆる = relaxed, not forcing it": "ゆる = ontspannen, jezelf niet forceren",
    "蒸し器 = a steamer basket": "蒸し器 = een stoommandje",
    "整える = to put in order": "整える = in orde brengen",
    "鍋 = a one-pot dish": "鍋 = een eenpansgerecht",
    "サクサクdeコパン passed 13 million servings": "サクサクdeコパン passeerde 13 miljoen porties",
    "ゆる = relaxed b": "ゆる = ontspannen b",
    "蒸し器 = steamer basket a": "蒸し器 = stoommandje a",
    "麻辣湯 = spicy soup dish d": "麻辣湯 = pittige soep d",
    "予報 = weather forecast c": "予報 = weersvoorspelling c",
    "市場 = market": "市場 = markt",
    "工芸 = craft": "工芸 = ambacht",
    "陶器 = pottery": "陶器 = aardewerk",
    "金箔 = gold leaf": "金箔 = bladgoud",
    "subject + time": "onderwerp + tijd",
    "place + で + あります": "plaats + で + あります",
    "見たい = want to see": "見たい = willen zien",
    "together with family": "samen met familie",
    "文化の日 = November 3 b": "文化の日 = 3 november b",
    "工芸展 = museum c": "工芸展 = museum c",
    "オーケストラ = Suginami d": "オーケストラ = Suginami d",
    "ライトアップ = Kanazawa Castle a": "ライトアップ = Kasteel Kanazawa a",
    "延長 = the game going long": "延長 = verlenging",
    "飲むことができません = cannot drink": "飲むことができません = niet mogen drinken",
    "守って + 〜しましょう = follow the rules, and let's…": "守って + 〜しましょう = regels volgen, laten we…",
    "フェンスの中 = inside the fence": "フェンスの中 = binnen het hek",
    "The slogan is 「静かだけど、冒険中。」": "De slogan is 「静かだけど、冒険中。」",
    "見頃 = when the leaves look their best": "見頃 = wanneer de bladeren het mooist zijn",
    "紅葉狩り = going out to see the leaves": "紅葉狩り = herfstbladeren gaan bekijken",
    "ライトアップ = lighting up at night": "ライトアップ = 's nachts met licht verlichten",
    "落葉 = fallen leaves": "落葉 = gevallen bladeren",
    "1.5倍 = 50% more than last year": "1,5 keer = 50% meer dan vorig jaar",
    "73% ≈ 3 in 4": "73% ≈ 3 op de 4",
    "サクサクdeコパン reached 13 million servings": "サクサクdeコパン bereikte 13 miljoen porties",
    "Japan Series Game 1 was October 24 (Saturday)": "Japan Series wedstrijd 1 was op 24 oktober (zaterdag)",
    "subject + time + place + verb": "onderwerp + tijd + plaats + werkwoord",
    "use 「で」 for place": "Gebruik 「で」 voor een plaats",
    "見頃 = best viewing season b": "見頃 = mooiste periode b",
    "鍋 = one-pot dish d": "鍋 = eenpansgerecht d",
    "落葉 = fallen leaves a": "落葉 = gevallen bladeren a",
    "予算 = budget c": "予算 = budget c",
    "見せてください = please show": "見せてください = alstublieft laten zien",
    "借りられます = can borrow (potential form)": "借りられます = kunnen lenen (mogelijkheidsvorm)",
    "「紅葉の本」 is popular": "「紅葉の本」 is populair",
    "どういたしまして = you're welcome": "どういたしまして = graag gedaan",
    # --- bslib4 furniture ---
    '"Note — "': '"Uitleg — "',
    '"Lucerna · JAPANESE WEEKLY VOL.2 · Japanese text · English explanations"': '"Lucerna · JAPANS WEEKBLAD VOL.2 · TEKSTEN IN HET JAPANS · UITLEG IN HET NEDERLANDS"',
    'f"Page {n} of {total}"': 'f"Pagina {n} van {total}"',
    # --- P1 masthead / top strip / dark band ---
    "TEXT IN JAPANESE · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS": "TEKSTEN IN HET JAPANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS",
    "毎週、日本語で · Weekly · 日本人が読んでいる日本語を読む": "毎週、日本語で · Elke week · 日本人が読んでいる日本語を読む",
    '"Tuesday is Culture Day"': '"Dinsdag is het Cultuurdag"',
    '"After the holiday, the autumn-leaf weekend arrives · See page 3"': '"Na de feestdag komt het herfstbladerenweekend · zie pagina 3"',
    '"トップニュース · Top story"': '"トップニュース · Hoofdnieuws"',
    '"祝日 holiday · 見頃 best viewing season · 暦 calendar · お届けします to bring to you."': '"祝日 feestdag · 見頃 mooiste periode · 暦 kalender · お届けします om aan u te bezorgen."',
    '"数字で見る今週 · Week in numbers"': '"数字で見る今週 · In cijfers"',
    '"今すぐ練習 · Practice now"': '"今すぐ練習 · Meteen oefenen"',
    '"These four topics shape this issue."': '"Deze vier onderwerpen bepalen dit nummer."',
    '"Dates in articles; not exact statistics"': '"Data in de artikelen; geen exacte cijfers"',
    '"この号の内容 · In this issue"': '"この号の内容 · In dit nummer"',
    '"今週のことば · Word of the week"': '"今週のことば · Woord van de week"',
    '"ゆる = relaxed, not forcing it."': '"ゆる = ontspannen, jezelf niet forceren."',
    '"短いニュース · News in brief"': '"短いニュース · Kort nieuws"',
    '"クイズ · Quick quiz"': '"クイズ · Bliksemquiz"',
    '"Read the front page and choose · Answers on page 8"': '"Lees de voorpagina en kies · Antwoorden op pagina 8"',
    # --- P2 ---
    '"レベル A2 · ゆる整え食と暖かい11月 · Gentle food and a warm November"': '"レベル A2 · ゆる整え食と暖かい11月 · Rustig eten en een warme november"',
    '"蒸す to steam · 並ぶ to appear on shelves · 食卓 the dinner table · 超える to pass."': '"蒸す stomen · 並ぶ in de winkels liggen · 食卓 de eettafel · 超える passeren."',
    '"予報 forecast · 平年 an average year · 季節風 seasonal wind · 話題 topic · 値上がり price rises."': '"予報 voorspelling · 平年 een gemiddeld jaar · 季節風 seizoenswind · 話題 onderwerp · 値上がり prijsstijgingen."',
    '"What about you? On a cold day, what nabe would you like to eat? Write two sentences in Japanese and send them in."': '"En jij? Welke nabe wil je eten op een koude dag? Schrijf twee zinnen in het Japans en stuur ze op."',
    '"季節のことば · Words of the season"': '"季節のことば · Seizoenswoorden"',
    '"ゆる整え食の4つの言葉 · Four words for gentle eating"': '"ゆる整え食の4つの言葉 · Vier woorden voor rustig eten"',
    '"a one-pot dish"': '"een eenpansgerecht"',
    '"a steamer basket"': '"een stoommandje"',
    '"relaxed, not forcing it"': '"ontspannen, jezelf niet forceren"',
    '"to put body and mind in order"': '"lichaam en geest in orde brengen"',
    '"練習 · Page 2 exercises"': '"練習 · Oefeningen van pagina 2"',
    # --- P3/P4 ---
    '"レベル A2→B1 · 文化の日と金沢 · Culture Day and Kanazawa"': '"レベル A2→B1 · 文化の日と金沢 · Cultuurdag en Kanazawa"',
    '"市場 market · 工芸 craft · 光 light · 楽しむ to enjoy."': '"市場 markt · 工芸 ambacht · 光 licht · 楽しむ genieten."',
    '"陶器 pottery · 漆器 lacquerware · 染物 dyed textiles · 金箔 gold leaf."': '"陶器 aardewerk · 漆器 lakwerk · 染物 geverfde stoffen · 金箔 bladgoud."',
    '"What about you? What cultural event would you like to go to on Culture Day? Write two sentences in Japanese and send them in."': '"En jij? Aan welk cultureel evenement wil je meedoen op Cultuurdag? Schrijf twee zinnen in het Japans en stuur ze op."',
    '"練習 · Page 3 exercises"': '"練習 · Oefeningen van pagina 3"',
    '"レベル B1 · 日本シリーズ横浜の2試合 · The Japan Series: two games in Yokohama"': '"レベル B1 · 日本シリーズ横浜の2試合 · De Japan Series: twee wedstrijden in Yokohama"',
    '"延長 extra innings · 逆転 comeback · 同点 tie · 優勝率 title rate."': '"延長 verlenging · 逆転 ommekeer · 同点 gelijke stand · 優勝率 kampioenspercentage."',
    '"総括 roundup · 締め切り deadline · 確認する to confirm."': '"総括 overzicht · 締め切り deadline · 確認する controleren."',
    '"日本シリーズの日程 · Series schedule"': '"日本シリーズの日程 · Schema"',
    '"横浜の2試合の記録 · The two Yokohama games, on record"': '"横浜の2試合の記録 · De twee wedstrijden in Yokohama, op een rij"',
    '"練習 · Page 4 exercises"': '"練習 · Oefeningen van pagina 4"',
    # --- P5/P6 ---
    '"若者・エンタメ · Youth"': '"若者・エンタメ · Jongeren"',
    '"レベル B1 · ハロウィンと秋まつり · Halloween and autumn festivals"': '"レベル B1 · ハロウィンと秋まつり · Halloween en herfstfestivals"',
    '"罰金 fine · 像 statue · 仮装 dressing up · 守る to follow."': '"罰金 boete · 像 standbeeld · 仮装 verkleden · 守る je houden aan."',
    '"祭り festival · 週末 weekend · 話題 topic."': '"祭り festival · 週末 weekend · 話題 onderwerp."',
    '"What about you? What would you like to do at an autumn festival? Write two sentences in Japanese and send them in."': '"En jij? Wat wil je doen op een herfstfestival? Schrijf twee zinnen in het Japans en stuur ze op."',
    '"練習 · Page 5 exercises"': '"練習 · Oefeningen van pagina 5"',
    '"レベル B2 · 暖かい11月と秋の旅 · A warm November and autumn travel"': '"レベル B2 · 暖かい11月と秋の旅 · Een warme november en herfstreizen"',
    '"予算 budget · 満足 satisfaction · 観測 observation · 追いかける to chase."': '"予算 budget · 満足 voldoening · 観測 waarneming · 追いかける najagen."',
    '"グラフを読もう · Reading the chart"': '"グラフを読もう · Lees de grafiek"',
    '"練習用データ · Practice data"': '"練習用データ · Oefengegevens"',
    '"練習 · Page 6 exercises"': '"練習 · Oefeningen van pagina 6"',
    # --- P7 ---
    '"ことば · Language"': '"ことば · Taal"',
    '"言語フォーカス · 三つのレベル、三つのテーマ · Three levels, three themes"': '"言語フォーカス · 三つのレベル、三つのテーマ · Drie niveaus, drie thema’s"',
    '"読書週間 Reading Week · 紹介 introduction · 読み聞かせ reading aloud."': '"読書週間 Leesweek · 紹介 introductie · 読み聞かせ voorlezen."',
    '"見頃 best viewing season · 紅葉狩り leaf-viewing outings · 落葉 fallen leaves"': '"見頃 mooiste periode · 紅葉狩り herfstbladeren bekijken · 落葉 gevallen bladeren"',
    '"〜倍 times · 〜% percent · 〜万食 ten-thousand servings."': '"〜倍 keer · 〜% procent · 〜万食 tienduizend porties."',
    '"まちがい診療所 · Error clinic"': '"まちがい診療所 · Foutenkliniek"',
    '"With 「昨日」, use the past tense."': '"Gebruik bij 「昨日」 de verleden tijd."',
    '"Add 「こと」 to turn a verb into a noun phrase."': '"Voeg 「こと」 toe om van een werkwoord een zelfstandig naamwoord te maken."',
    '"Count places with 「か所」."': '"Tel plaatsen met 「か所」."',
    '"Use 「で」 for the place where an action happens."': '"Gebruik 「で」 voor de plaats waar een handeling gebeurt."',
    '"今週のフレーム · Frame of the week"': '"今週のフレーム · De zin van de week"',
    '"Breakdown: gently putting body and mind in order."': '"Uitleg: lichaam en geest rustig in orde brengen."',
    ("読者の手紙 · Readers" + chr(92) + chr(39) + " corner"): "読者の手紙 · Lezershoek",
    '"今週のフレーズ · Phrases of the week (verbatim from this issue)"': '"今週のフレーズ · Zinnen van de week (letterlijk uit dit nummer)"',
    '"Culture Day is Tuesday, November 3."': '"Cultuurdag is op dinsdag 3 november."',
    '"It is a slow, gently ordered Japanese November."': '"Dit is een langzame, rustig geordende Japanse november."',
    '"ゆる means not forcing it, taking it slowly."': '"Yuru betekent: jezelf niet forceren, het rustig aan doen."',
    '"Nabe ingredients appeared in shops a month early."': '"Nabe-ingrediënten lagen een maand eerder in de winkels."',
    '"You can enjoy traditional crafts, autumn leaves, and lights together."': '"Je kunt traditionele ambachten, herfstbladeren en verlichting tegelijk beleven."',
    '"SoftBank started with two straight wins."': '"SoftBank begon met twee zeges op rij."',
    '"Follow the rules and have a happy Halloween."': '"Houd je aan de regels en vier een fijne Halloween."',
    '"Leaf-viewers can chase the best season from north to south."': '"Wie herfstbladeren gaat bekijken, kan van noord naar zuid de mooiste periode volgen."',
    '"p.1"': '"Pagina 1"',
    '"p.2"': '"Pagina 2"',
    '"p.3"': '"Pagina 3"',
    '"p.4"': '"Pagina 4"',
    '"p.5"': '"Pagina 5"',
    '"p.6"': '"Pagina 6"',
    '"来週 · Next issue (VOL.3)"': '"来週 · Volgend nummer (VOL.3)"',
    # --- P8 ---
    '"テストと答え · Test and answers"': '"テストと答え · Toets en antwoorden"',
    '"Culture Day is November 3."': '"Cultuurdag is op 3 november."',
    '"If you drop litter, the fine is 2,000 yen."': '"Wie afval op straat gooit, krijgt een boete van 2.000 yen."',
    '"Reading Week starts on October 27. → ___"': '"De Leesweek begint op 27 oktober. → ___"',
    '"I want to go to Kobe to see the autumn-leaf illuminations. → ___"': '"Ik wil naar Kobe om de herfstverlichting te zien. → ___"',
    '"Writing task (no single correct answer); the model text ({NCHARS} characters) is below."': '"Schrijfopdracht (geen enig juist antwoord); de voorbeeldtekst ({NCHARS} tekens) staat hieronder."',
    '"(open task — model text below)"': '"(open opdracht — voorbeeldtekst hieronder)"',
    '"Model text in section H on this page ({NCHARS} characters)"': '"Voorbeeldtekst in deel H van deze pagina ({NCHARS} tekens)"',
    '"答え · Answers — grouped by page; just find your number"': '"答え · Antwoorden — gegroepeerd per pagina: zoek je nummer op"',
    '"A short English note with every answer · ✓ = the model-text item"': '"Bij elk antwoord een korte notitie in het Nederlands · ✓ = de vraag met de voorbeeldtekst"',
    'f"— Page {pg} —"': 'f"— Pagina {pg} —"',
    # --- render filenames ---
    '"Lucerna-VOL2-EN.pdf"': '"Lucerna-VOL2-NL.pdf"',
    '"Lucerna-VOL2-EN-web.pdf"': '"Lucerna-VOL2-NL-web.pdf"',
})

# --- Readers'-corner disclosure fragments (EN literal pieces -> Dutch) ---
EN2NL.update({
    ("Editor" + chr(92) + "'s sample, not a real letter. No real letters or best "): "Voorbeeldbrief, geen echte brief. Er waren nog geen echte brieven of beste ",
    "Page 8 compositions had arrived by the deadline; both will appear ": "P8-opstellen binnen; beide verschijnen ",
    "in VOL.3. Send us your letter in Japanese — selected letters will ": "in VOL.3. Stuur je Japanse brief op — gekozen brieven ",
    "be printed in VOL.3!": "komen in VOL.3!",
})

# Strings that stay identical (numbers / code geometry, no EN text).
KEEP = {"38 + 27 = 65"}


def main():
    text = open(SRC, encoding="utf-8").read()
    # 1. EN -> NL replacements, longest keys first (prefix safety, e.g.
    # "The exhibition runs to November 8" before "... (Sunday)").
    for key in sorted(EN2NL, key=len, reverse=True):
        if key in text:
            text = text.replace(key, EN2NL[key])
    # 2. Plain renames (paths, filenames, variable, docstring language).
    for old, new in [
        ("weekly-report-w45-ja-en", "weekly-report-w45-ja-nl"),
        ("JA x EN", "JA x NL"),
        ("JA×EN", "JA×NL"),
        ("ld_en", "ld_nl"),
        ("English", "Dutch"),
    ]:
        text = text.replace(old, new)
    # 3. Docstring header rewrite.
    text = text.replace(
        "JA core (VOL.2, Chinese explanations) -> JA x NL edition transform.",
        "JA core (VOL.2, Chinese explanations) -> JA x NL edition transform.")
    # 4. NL-specific additions the EN sibling does not have:
    # (a) P8 band right: W43 JA x NL prints "Pagina 8", while W45 JA x EN
    # kept the frozen Japanese "第 8 面". Same-pairing precedent wins.
    marker = '    "content8.py": ['
    assert text.count(marker) == 1, text.count(marker)
    text = text.replace(
        marker,
        marker + '\n        (\'"第 8 面 · 週の大きなテスト + 全ての答え"\', '
        '\'"Pagina 8 · 週の大きなテスト + 全ての答え"\'),', 1)
    # (a2) Matching instructions, P2 + P8 only (W43 JA x NL precedent:
    # those two slots overflow with the full Dutch instruction; P3's
    # wider slot keeps the full form via GLOBAL). PER_FILE runs before
    # GLOBAL, so GLOBAL's full form then applies nowhere in these files.
    marker12 = '    "content12.py": ['
    assert text.count(marker12) == 1
    text = text.replace(
        marker12,
        marker12 + '\n        (\'instr="把词和释义配对"\', \'instr="Combineer"\'),', 1)
    text = text.replace(
        marker,
        marker + '\n        (\'instr="把词和释义配对"\', \'instr="Combineer"\'),', 1)
    # (b) E-zone directional instructions (W43 JA x NL precedent):
    # GLOBAL maps instr 翻译 -> "Vertaal"; the four E items then get a
    # direction per item. Implemented as a post-pass in main() below.
    postpass = '''
    # NL post-pass: directional E-zone instructions. content8.py holds
    # exactly the four translation items (verified: core has exactly
    # four instr="翻译"); the two items whose "→ ___" prompt is a Dutch
    # sentence (139/140) translate INTO Japanese, the two whose prompt
    # is Japanese (137/138) translate INTO Dutch.
    import re as _re
    _c8 = open(os.path.join(HERE, "content8.py"), encoding="utf-8").read()
    _lines = _c8.split("\\n")
    _n_nl = _n_ja = 0
    for _i, _ln in enumerate(_lines):
        if 'instr="Vertaal"' in _ln and "→ ___" in _ln:
            _m = _re.search(r'"([^"]*) → ___"', _ln)
            assert _m, _ln
            _first = _m.group(1)[:1]
            if _first.isascii() and _first.isalpha():
                _lines[_i] = _ln.replace('instr="Vertaal"',
                                          'instr="Vertaal naar het Japans"')
                _n_ja += 1
            else:
                _lines[_i] = _ln.replace('instr="Vertaal"',
                                          'instr="Vertaal naar het Nederlands"')
                _n_nl += 1
    assert (_n_nl, _n_ja) == (2, 2), (_n_nl, _n_ja)
    open(os.path.join(HERE, "content8.py"), "w", encoding="utf-8").write(
        "\\n".join(_lines))
    print("E-zone directional instr: 2x Nederlands, 2x Japans")
'''
    hook = '''    print("OUT dir:", EDITION)'''
    assert hook in text
    text = text.replace(hook, postpass + hook, 1)
    # 5. Header comment: record the derivation + W43 deviations.
    header_note = ('JA x NL derivation note: this transform was generated from\n'
                   'the sibling W45 JA x EN transform (same OLD strings, NEW\n'
                   'strings rendered in Dutch). W43 JA x NL precedent governs\n'
                   'furniture: badge/footer/page-line/gloss-prefix/section heads\n'
                   'verbatim from files/weekly-report-ja-nl; masthead geometry\n'
                   'wordmark 248 / subtitle 316 / badge 356 19pt / tagline 390 /\n'
                   'rules 406/413 / band 424 (W43 JA x NL measured; the README #20\n'
                   "generalization's 262 wordmark is NOT followed for this pair).\n"
                   'P8 band right "Pagina 8" follows W43 JA x NL (JA x EN kept the\n'
                   'frozen Japanese label). E-zone instructions are directional\n'
                   "(W43 JA x NL), unlike JA x EN's plain Translate.\n\n")
    old_doc = text.split('"""', 2)
    assert len(old_doc) == 3
    # Replace only the docstring body (first quoted block) with the note
    # + the original body, keeping the rest of the file intact.
    body = old_doc[1]
    text = '"""' + header_note + body + '"""' + old_doc[2]
    open(DST, "w", encoding="utf-8").write(text)
    print("wrote", DST, len(text), "chars")


if __name__ == "__main__":
    main()
