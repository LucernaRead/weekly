# -*- coding: utf-8 -*-
"""Generate W46 NL x ZH-TW transform.py from the EN rep pairs (hidden_files/w46/en-reps.txt).
ZH-TW precedent (W45 NL x ZH-TW): explanations written NATIVELY in
Taiwan/Hong Kong usage (not mechanical s2t conversion); type tokens in
Traditional forms (完形單選, 單選, 詞彙配對, 判斷對錯, 完成句子, 造句,
翻譯, 寫作); instr words localised (判斷, 寫作, 翻譯; all four translation
items carry instr 翻譯, no direction refinement). Badge REPLACES the
strapline at y=372, 19.5pt BRICK. Subtitle uses SPACED form 荷 語 週 報.
P8 sizes stay at CORE values with '— 第 N 版 —' separators. bridge()
renamed to expl(); P7 bridges use '；', glosses ' · ', P8 notes ' = '
with FULL-WIDTH parentheses （）. Disclosure variable KEEPS the name
dt_zh. The TC svglib (TC face) is copied from the W45 zh-tw build AFTER
the transform, not generated here.
"""
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

ZHTW_MAP = {
    "ELKE WEEK IN HET NEDERLANDS · EVERY WEEK · REAL DUTCH":
        "ELKE WEEK IN HET NEDERLANDS · 每週一期 · 讀荷蘭人正在讀的荷蘭語",
    "WEEKBLAD IN HET NEDERLANDS · VOL.3 · SINTERKLAAS · SINT-MAARTEN · ORANJE":
        "荷 語 週 報 · VOL.3 · SINTERKLAAS · SINT-MAARTEN · ORANJE",
    '"SINTERKLAAS IS COMING"': '"辛特克拉斯要來了"',
    '"This week: Sinterklaas comes to the Netherlands · see page 3"':
        '"本週：辛特克拉斯來到荷蘭 · 見第 3 版"',
    'f.bridge("Note | de intocht = arrival · de stoomboot = steamboat · de lampion = lantern.")':
        'f.expl("講解｜de intocht 進城 · de stoomboot 蒸汽船 · de lampion 燈籠。")',
    '"DE WEEK IN CIJFERS · IN NUMBERS"': '"DE WEEK IN CIJFERS · 數字看本週"',
    " (9 Nov: Sinterklaas news)": "（11 月 9 日：辛特克拉斯新聞）",
    " (14 Nov: national arrival, Grave)": "（11 月 14 日：全國進城，赫拉弗）",
    " (15 Nov: 88th)": "（11 月 15 日：第 88 屆）",
    " (Fri 20:45)": "（週五 20:45）",
    '"NU JIJ · YOUR TURN"': '"NU JIJ · 輪到你了"',
    '"The Sinterklaas news starts on 9 November"': '"辛特克拉斯新聞從 11 月 9 日開始"',
    '"The national arrival is in Grave"': '"全國進城在赫拉弗舉行"',
    '"The Amsterdam arrival is on Sunday 15 November"': '"阿姆斯特丹進城在 11 月 15 日週日"',
    '"St Martin\'s Day is on Wednesday 11 November"': '"聖馬丁節在 11 月 11 日週三"',
    '"Netherlands–Greece kicks off at 20:45"': '"荷蘭—希臘之戰 20:45 開踢"',
    '"Plural subject, so zetten"': '"主詞是複數，所以用 zetten"',
    '"· THIS WEEK"': '"· 本週"',
    '"Agenda van de week · THIS WEEK\'S EVENTS"': '"Agenda van de week · 本週大事"',
    '"See pages 2–4 for all dates and times."': '"所有日期和時間見第 2–4 版。"',
    '"IN DEZE EDITIE · IN THIS ISSUE"': '"IN DEZE EDITIE · 本期內容"',
    '"«The intocht»: Sinterklaas arrives in a town by boat, then on horseback, in a festive parade."':
        '"«de intocht»：慶典進城隊伍。"',
    '"IN HET KORT · IN BRIEF"': '"IN HET KORT · 摘要"',
    '"BLIKSEMQUIZ · LIGHTNING QUIZ"': '"BLIKSEMQUIZ · 閃電問答"',
    '"Read page 1, choose the right answer · answers on page 8"':
        '"讀第 1 版，選出正確答案 · 答案在第 8 版"',
    '"The Sinterklaas news starts on Monday 9 November"': '"辛特克拉斯新聞在 11 月 9 日週一開播"',
    '"The Amsterdam arrival is the 88th edition"': '"阿姆斯特丹進城是第 88 屆"',
    'p.band("LEVEN · LIFE", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · St Martin\'s Day: lanterns and songs")':
        'p.band("LEVEN · 生活", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · 聖馬丁節：燈籠與歌聲")',
    '"ZO ONTHOUD JE HET · REMEMBER"': '"ZO ONTHOUD JE HET · 記住它"',
    'f.gloss("de lampion = lantern · delen = to share · de mantel = cloak, coat · de bedelaar = beggar · het erfgoed = heritage · het ledlampje = little LED light.")':
        'f.gloss("de lampion 燈籠 · delen 分享 · de mantel 斗篷 · de bedelaar 乞丐 · het erfgoed 文化遺產 · het ledlampje LED 小燈。")',
    '"On 11 November, will you go singing door to door with a lantern, or would you rather watch the Sinterklaas news? Write two sentences in Dutch and send them to the editors."':
        '"11 月 11 日，你要提著燈籠挨家挨戶唱歌，還是想看辛特克拉斯新聞？用荷蘭語寫兩個句子，寄給編輯部。"',
    '"EN JIJ? · AND YOU?"': '"EN JIJ? · 你呢？"',
    '"SINT-MAARTEN IN VIER WOORDEN · FOUR KEY WORDS"': '"SINT-MAARTEN IN VIER WOORDEN · 四個關鍵詞"',
    '"Wat hoort bij het feest? · Which words belong to the festival?"':
        '"Wat hoort bij het feest? · 哪些詞屬於這個節日？"',
    '"a paper lantern, with an LED light inside"': '"裝著 LED 燈的紙燈籠"',
    '"sharing: giving half a cloak to a beggar"': '"分享：把一半斗篷送給乞丐"',
    '"St Martin\'s city, on the heritage list"': '"聖馬丁之城，列入文化遺產名錄"',
    '"singing St Martin\'s songs door to door"': '"挨家挨戶唱聖馬丁歌曲"',
    '"OEFENINGEN · EXERCISES ON PAGE 2"': '"OEFENINGEN · 第 2 版練習"',
    '"Answers on page 8 · levels are mixed; find your number"':
        '"答案在第 8 版 · 題目程度混編，按題號找"',
    'e.bridge("Read the article on page 2 and choose the right answer.")':
        'e.expl("讀第 2 版文章，選出正確答案。")',
    '"Children go door to door with lanterns"': '"孩子們提著燈籠挨家挨戶"',
    '"Martinus gave half his cloak to a beggar"': '"馬丁努斯把一半斗篷送給了乞丐"',
    '"Utrecht is St Martin\'s city"': '"烏特勒支是聖馬丁之城"',
    '"A lantern takes an LED light, not a candle"': '"燈籠裡放 LED 燈，不放蠟燭"',
    'e.bridge("Fill in with words from page 2.")': 'e.expl("用第 2 版的詞填空。")',
    '"St Martin\'s Day is on 11 November"': '"聖馬丁節在 11 月 11 日"',
    '"lampion = lantern (de)"': '"lampion = 燈籠 (de)"',
    '"delen = to share"': '"delen = 分享"',
    '"mantel = cloak (de)"': '"mantel = 斗篷 (de)"',
    '"St Martin\'s city is Utrecht"': '"聖馬丁之城是烏特勒支"',
    'e.bridge("Fill in with the song words and the safety tip.")':
        'e.expl("用歌詞和安全提示填空。")',
    '"Song words: my little light may shine"': '"歌詞：我的小燈可以發光"',
    '"Lanterns shine brightest when it is dark"': '"天黑時燈籠最亮"',
    '"An LED light is safe"': '"LED 燈很安全"',
    '"Pakjesavond is on 5 December"': '"禮物之夜在 12 月 5 日"',
    '["lampion = lantern b", "delen = to share a", "mantel = cloak d", "erfgoed = heritage c"]':
        '["lampion = 燈籠 b", "delen = 分享 a", "mantel = 斗篷 d", "erfgoed = 文化遺產 c"]',
    'instr="Match word to meaning"': 'instr="把詞和釋義配對"',
    '"HET NIEUWS · TOP STORY"': '"HET NIEUWS · 頭條"',
    'p.band("CULTUUR · CULTURE", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · The Sinterklaas news and Het diner")':
        'p.band("CULTUUR · 文化", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · 辛特克拉斯新聞與《晚餐》")',
    'f.gloss("het journaal = news programme · de flessenpost = message in a bottle · de burgemeester = mayor · de stoet = procession · de leeskring = reading club.")':
        'f.gloss("het journaal 新聞節目 · de flessenpost 瓶中信 · de burgemeester 市長 · de stoet 遊行隊伍 · de leeskring 讀書會。")',
    '"OEFENINGEN · EXERCISES ON PAGE 3"': '"OEFENINGEN · 第 3 版練習"',
    'e.bridge("Read the article on page 3 and choose the right answer.")':
        'e.expl("讀第 3 版文章，選出正確答案。")',
    '"The Sinterklaas news is on every day at 18:00"': '"辛特克拉斯新聞每天 18:00 播出"',
    '"The national arrival is in Grave"': '"全國進城在赫拉弗舉行"',
    '"The Amsterdam boat leaves De Omval at 10:15"': '"阿姆斯特丹的船 10:15 從 De Omval 出發"',
    '"Het diner was written by Herman Koch"': '"《晚餐》是赫爾曼·柯赫寫的"',
    '"Het diner is free to pick up at the library"': '"《晚餐》可以在圖書館免費領取"',
    'e.bridge("Fill in with the words from the box.")': 'e.expl("用方框裡的詞填空。")',
    '"journaal = news programme"': '"journaal = 新聞節目"',
    '"burgemeester = mayor"': '"burgemeester = 市長"',
    '"stoet = procession"': '"stoet = 遊行隊伍"',
    '"flessenpost = message in a bottle"': '"flessenpost = 瓶中信"',
    '"leeskring = reading club"': '"leeskring = 讀書會"',
    'e.bridge("Complete with the present perfect. Watch the auxiliaries hebben/zijn.")':
        'e.expl("用現在完成式填空。注意助動詞 hebben/zijn。")',
    '"beginnen takes zijn: is begonnen"': '"beginnen 用 zijn：is begonnen"',
    '"vinden perfectum: heeft gevonden"': '"vinden 完成式：heeft gevonden"',
    '"aankomen takes zijn: is aangekomen"': '"aankomen 用 zijn：is aangekomen"',
    '"lezen perfectum: hebben gelezen"': '"lezen 完成式：hebben gelezen"',
    'e.bridge("Work it out: answer with the numbers from page 3.")':
        'e.expl("算一算：用第 3 版的數字回答。")',
    '"From 9 to 14 November is 5 days"': '"11 月 9 日到 14 日是 5 天"',
    '"From 9 to 15 November is 6 days"': '"11 月 9 日到 15 日是 6 天"',
    '"The Grave programme, 12:00–16:00, lasts 4 hours"': '"赫拉弗的活動 12:00–16:00，持續 4 小時"',
    '"Het diner is from 2009: 17 years ago in 2026"': '"《晚餐》出版於 2009 年：到 2026 年是 17 年前"',
    'p.band("SPORT", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · Oranje and the Nations League")':
        'p.band("SPORT · 體育", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · 荷蘭隊與國家聯賽")',
    'f.gloss("de groepsfase = group stage · de kwartfinale = quarter-final · ongeslagen = unbeaten · de interland = international match · de stand = the table.")':
        'f.gloss("de groepsfase 小組賽 · de kwartfinale 八強賽 · ongeslagen 不敗 · de interland 國際賽 · de stand 積分榜。")',
    '"OEFENINGEN · EXERCISES ON PAGE 4"': '"OEFENINGEN · 第 4 版練習"',
}
ZHTW_MAP.update({
    'e.bridge("Read the article on page 4 and choose the right answer.")':
        'e.expl("讀第 4 版文章，選出正確答案。")',
    '"Netherlands–Greece, Friday 20:45, in Amsterdam"': '"荷蘭—希臘，週五 20:45，阿姆斯特丹"',
    '"The Netherlands and Greece both have 8 points"': '"荷蘭和希臘都是 8 分"',
    '"The Netherlands scored more goals in the group (7 to 5)"': '"荷蘭在小組裡進球更多（7 比 5）"',
    '"Germany–Netherlands, Monday, in Berlin"': '"德國—荷蘭，週一，柏林"',
    '"Eredivisie matchday 13 is on 21–22 November"': '"荷甲第 13 輪在 11 月 21–22 日"',
    'e.bridge("Fill in with the words from the box. Watch the verb forms.")':
        'e.expl("用方框裡的詞填空。注意動詞形式。")',
    '"groepsfase = group stage"': '"groepsfase = 小組賽"',
    '"kwartfinale plural: kwartfinales"': '"kwartfinale 複數：kwartfinales"',
    '"ongeslagen = unbeaten"': '"ongeslagen = 不敗"',
    '"stand = the table"': '"stand = 積分榜"',
    '"interland = international match"': '"interland = 國際賽"',
    'e.bridge("Complete with the past tense or the perfect tense.")':
        'e.expl("用過去式或完成式填空。")',
    '"spelen past tense: speelde"': '"spelen 過去式：speelde"',
    '"winnen past tense: won"': '"winnen 過去式：won"',
    '"maken past tense: maakte"': '"maken 過去式：maakte"',
    '"komen perfectum takes zijn"': '"komen 完成式用 zijn"',
    '"True: Netherlands–Greece, Friday 20:45"': '"正確：荷蘭—希臘，週五 20:45"',
    '"False: Serbia are bottom with 0 points"': '"錯誤：塞爾維亞 0 分墊底"',
    '"False: Eredivisie matchday 13 is on 21–22 November"': '"錯誤：荷甲第 13 輪在 11 月 21–22 日"',
    '"True: PSV beat Willem II 7–0"': '"正確：PSV 以 7–0 擊敗威廉二世"',
    'p.band("JONGEREN · YOUNG PEOPLE", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · Robinson, the shoe and the wish list")':
        'p.band("JONGEREN · 年輕人", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · 魯濱遜、鞋子與願望清單")',
    " (watch on RTL 4, Sunday 20:00)": "（週日 20:00 在 RTL 4 收看）",
    " (watch the trials: points are won there)": "（看考驗：分數在那裡決定）",
    " (guess with friends who stays longest)": "（和朋友猜誰留得最久）",
    " (then put out your shoe, wish list inside)": "（然後擺出鞋子，裡面放願望清單）",
    'f.gloss("het verlanglijstje = wish list · de verslaggever = reporter · de proef = trial, challenge · stemmen = to vote · de aflevering = episode.")':
        'f.gloss("het verlanglijstje 願望清單 · de verslaggever 記者 · de proef 考驗 · stemmen 投票 · de aflevering 集。")',
    '"On Sunday, do you watch Expeditie Robinson, or would you rather put out your shoe with a wish list? Write two sentences in Dutch and send them in."':
        '"週日你要看《魯濱遜遠征》，還是寧願擺出裝著願望清單的鞋子？用荷蘭語寫兩個句子寄來。"',
    '"EN JIJ? · AND YOU?"': '"EN JIJ? · 你呢？"',
    '"OEFENINGEN · EXERCISES ON PAGE 5"': '"OEFENINGEN · 第 5 版練習"',
    'e.bridge("Read the article on page 5 and choose the right answer.")':
        'e.expl("讀第 5 版文章，選出正確答案。")',
    '"Robinson is on every Sunday at 20:00 on RTL 4"': '"《魯濱遜遠征》每週日 20:00 在 RTL 4 播出"',
    '"19 contestants"': '"19 位參賽者"',
    '"The show is filmed on a desert island in Malaysia"': '"節目在馬來西亞的荒島上拍攝"',
    '"The contestants spend 34 days on the island"': '"參賽者在島上待 34 天"',
    '"A wish list goes in the shoe"': '"願望清單放進鞋子裡"',
    '"verlanglijstje = wish list (het)"': '"verlanglijstje = 願望清單 (het)"',
    '"verslaggever = reporter (de)"': '"verslaggever = 記者 (de)"',
    '"proef = trial, challenge (de)"': '"proef = 考驗 (de)"',
    '"stemmen = to vote"': '"stemmen = 投票"',
    '"aflevering = episode"': '"aflevering = 集"',
    '"kandidaat plural: kandidaten"': '"kandidaat 複數：kandidaten"',
    'e.bridge("Use gaan + infinitive to talk about the future.")':
        'e.expl("用 gaan + 不定詞談論未來。")',
    '"gaat winnen = will win (just a guess)"': '"gaat winnen = 會贏（只是猜測）"',
    '"wij → gaan + infinitive kijken"': '"wij → gaan + 不定詞 kijken"',
    '"hij → gaat zetten"': '"hij → gaat zetten"',
    '"zij (plural) → gaan schrijven"': '"zij（複數）→ gaan schrijven"',
    '"True: the show started on 1 November"': '"正確：節目在 11 月 1 日開播"',
    '"False: the show is filmed in Malaysia"': '"錯誤：節目在馬來西亞拍攝"',
    '"False: the carrot in the shoe is for the horse"': '"錯誤：鞋子裡的胡蘿蔔是給馬的"',
    'p.band("VERDIEPING · IN DEPTH", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · St Martin\'s Day or Halloween?")':
        'p.band("VERDIEPING · 深度", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · 聖馬丁節還是萬聖節？")',
    'f.gloss("de traditie = tradition · griezelen = to scare, to spook · de belangstelling = interest · de achteruitgang = decline · de deskundige = expert.")':
        'f.gloss("de traditie 傳統 · griezelen 嚇人 · de belangstelling 關注 · de achteruitgang 衰退 · de deskundige 專家。")',
    '"Practice data: invented numbers for practice only, not a real survey. Question: what do you do around 11 November? (100 young people)"':
        '"練習數據：僅供練習的虛構數字，不是真實調查。問題：11 月 11 日前後你做什麼？（100 位年輕人）"',
    '"DE GRAFIEK · PRACTICE DATA"': '"DE GRAFIEK · 圖表（練習數據）"',
    '"VOOR OF TEGEN? · FOR OR AGAINST?"': '"VOOR OF TEGEN? · 正方還是反方"',
    '"OEFENINGEN · EXERCISES ON PAGE 6"': '"OEFENINGEN · 第 6 版練習"',
    'e.bridge("Answer from the chart on page 6 (practice data).")':
        'e.expl("根據第 6 版圖表（練習數據）回答。")',
    '"40 young people walk with a lantern"': '"40 位年輕人提著燈籠走"',
    '"25 celebrate Halloween"': '"25 人慶祝萬聖節"',
    '"40 + 20 = 60"': '"40 + 20 = 60"',
    '"15 stay at home"': '"15 人待在家裡"',
    '"The chart counts 100 people: 40+25+20+15"': '"圖表共 100 人：40+25+20+15"',
    'e.bridge("Read the article on page 6 and choose the right answer.")':
        'e.expl("讀第 6 版文章，選出正確答案。")',
    '"In 2025, 26% of Dutch people celebrated Halloween"': '"2025 年，26% 的荷蘭人慶祝了萬聖節"',
    '"The two surveys use different definitions, so they cannot be compared directly"':
        '"兩項調查的定義不同，所以不能直接比較"',
    '"Interest in St Martin\'s Day increased (Stengs, 2025)"': '"人們對聖馬丁節的興趣增加了（Stengs，2025 年）"',
    '"Halloween is about spooking; St Martin\'s Day is about sharing"': '"萬聖節是嚇人；聖馬丁節是分享"',
    '"A tradition lives on when people keep celebrating it"': '"傳統會一直活下去，只要人們繼續慶祝它"',
    'e.bridge("Put the words in the right order to make sentences.")':
        'e.expl("把詞語排成正確的順序，組成句子。")',
    '"traditie = tradition (de)"': '"traditie = 傳統 (de)"',
    '"griezelen = to scare, to spook"': '"griezelen = 嚇人"',
    '"belangstelling = interest (de)"': '"belangstelling = 關注 (de)"',
    '"achteruitgang = decline (de)"': '"achteruitgang = 衰退 (de)"',
    '"Subject + verb + complement + place"': '"主詞 + 動詞 + 補語 + 地點"',
    '"Subject + verb + manner + place"': '"主詞 + 動詞 + 方式 + 地點"',
    '"The als-clause comes last"': '"als 子句放在最後"',
    '"kiezen + hoeft niet + explanation"': '"kiezen + hoeft niet + 解釋"',
    'p.band("TAAL · LANGUAGE", "De Lucerna", "Language focus · Drie niveaus, drie gereedschappen · Three levels, three tools")':
        'p.band("TAAL · 語言", "De Lucerna", "聚焦語言 · Drie niveaus, drie gereedschappen · 三個級別，三件工具")',
    'a.bridge("de stoomboot = steamboat; de intocht = the festive arrival; de schoen zetten = to put out your shoe; de lampion = lantern.")':
        'a.expl("de stoomboot 蒸汽船；de intocht 慶典進城；de schoen zetten 擺鞋子；de lampion 燈籠。")',
    '"de stoomboot = steamboat"': '"de stoomboot = 蒸汽船"',
    '"The intocht is Sinterklaas\'s festive arrival"': '"intocht 是辛特克拉斯的慶典進城"',
    '"lampion = lantern"': '"lampion = 燈籠"',
    'b.bridge("schoentje = little shoe; lichtje = little light; cadeautje = little present. -je means small and affectionate.")':
        'b.expl("schoentje 小鞋子；lichtje 小燈；cadeautje 小禮物。-je 表示小巧和親暱。")',
    '"schoen + -tje: schoentje"': '"schoen + -tje：schoentje"',
    '"licht + -je: lichtje"': '"licht + -je：lichtje"',
    '"cadeau + -tje: cadeautje"': '"cadeau + -tje：cadeautje"',
    '"-je means small and affectionate, not always really small"':
        '"-je 表示小巧和親暱，不一定真的很小"',
    'c.bridge("Als… = If… / When…; als het donker wordt = when it gets dark; als Sinterklaas komt = when Sinterklaas comes.")':
        'c.expl("Als… = 如果…／當…；als het donker wordt = 天黑時；als Sinterklaas komt = 辛特克拉斯來時。")',
    '"Als… = If… / When…"': '"Als… = 如果…／當…"',
    '"An als-clause is a condition, not a question"': '"als 子句是條件，不是疑問"',
    '"The verb comes first in the main clause: gaat de lampion aan"':
        '"主句裡動詞在前：gaat de lampion aan"',
    '"Als Oranje wint… = If Oranje win…"': '"Als Oranje wint… = 荷蘭隊贏了…"',
    '"PAS OP! · ERROR CLINIC"': '"PAS OP! · 易錯診所"',
    '"Sinterklaas is a name, so it takes no article."': '"Sinterklaas 是名字，不加冠詞。"',
    '"mijn schoen = my shoe."': '"mijn schoen = 我的鞋子。"',
    '"Fixed phrase: langs de deuren."': '"固定說法：langs de deuren。"',
    '"Verb first after the als-clause: ben ik blij."': '"als 子句之後動詞在前：ben ik blij。"',
    '"HET WOORD · WORD OF THE WEEK"': '"HET WOORD · 本週生詞"',
    '"schoen zetten = to put out your shoe, with a carrot and a drawing inside."':
        '"schoen zetten = 擺鞋子：放一根胡蘿蔔和一張畫在裡面。"',
})
ZHTW_MAP.update({
    'dt_en = "No real letters or best page-8 texts at press time — example; promise to VOL.4."':
        'dt_zh = "截稿時未收到真實來信或第 8 版最佳作文，刊登示例信，承諾順延 VOL.4。"',
    'len(wrap(dt_en, "sans", False, 20, CW - 44))': 'len(wrap(dt_zh, "sans", False, 20, CW - 44))',
    'p.para(bx + 22, yy3 + 20, dt_en, 20, "sans", False, GREY, CW - 44, 1.42) + 10':
        'p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10',
    '"Editors\' example — send yours for VOL.4!"':
        '"編輯部示例信，非真實來信。歡迎寄來你的真實來信和第 8 版最佳作文，VOL.4 刊登！"',
    '"ZINNEN VAN DE WEEK · PHRASES OF THE WEEK (VERBATIM FROM THIS ISSUE)"':
        '"ZINNEN VAN DE WEEK · 本週金句（逐字摘自本期文章）"',
    '"On Monday 9 November, the Sinterklaas news starts on television."':
        '"11 月 9 日週一，辛特克拉斯新聞在電視上開播。"',
    '"One day later, Sunday 15 November: the Amsterdam arrival, 88th edition."':
        '"一天後，11 月 15 日週日：阿姆斯特丹進城，第 88 屆。"',
    '"St Martin\'s Day is the festival of sharing: sharing light, food and attention."':
        '"聖馬丁節是分享的節日：分享光、食物和關懷。"',
    '"On Saturday 14 November, Sinterklaas officially arrives in Grave."':
        '"11 月 14 日週六，辛特克拉斯正式抵達赫拉弗。"',
    '"On Friday 13 November, Oranje play Greece at home."':
        '"11 月 13 日週五，荷蘭隊在主場對希臘。"',
    '"Every Sunday at 20:00, Expeditie Robinson is on RTL 4."':
        '"每週日 20:00，《魯濱遜遠征》在 RTL 4 播出。"',
    '"St Martin\'s Day is an old tradition in the Netherlands."':
        '"聖馬丁節是荷蘭的古老傳統。"',
    '"A tradition lives on when people keep celebrating it."':
        '"傳統會一直活下去，只要人們繼續慶祝它。"',
    '"VOLGENDE WEEK · NEXT WEEK (VOL.4)"': '"VOLGENDE WEEK · 下期預告 (VOL.4)"',
    'p.band("TOETS EN ANTWOORDEN · TEST AND ANSWERS", "De Lucerna", "Page 8 · De grote toets van de week + alle antwoorden")':
        'p.band("TOETS EN ANTWOORDEN · 練習與答案", "De Lucerna", "第 8 版 · De grote toets van de week + alle antwoorden")',
    '"The Sinterklaas news is on every day at 18:00."': '"辛特克拉斯新聞每天 18:00 播出。"',
    '"The national arrival is in Grave"': '"全國進城在赫拉弗舉行"',
    '"The Sinterklaas news starts on 9 November"': '"辛特克拉斯新聞從 11 月 9 日開始"',
    '"The Amsterdam arrival is the 88th edition"': '"阿姆斯特丹進城是第 88 屆"',
    '"Netherlands–Greece kicks off at 20:45"': '"荷蘭—希臘之戰 20:45 開踢"',
    '"St Martin\'s Day is on 11 November"': '"聖馬丁節在 11 月 11 日"',
    '"Robinson is on RTL 4"': '"《魯濱遜遠征》在 RTL 4 播出"',
    '"St Martin\'s Day is the festival of sharing."': '"聖馬丁節是分享的節日。"',
    '"The Netherlands and Greece both have 8 points"': '"荷蘭和希臘都是 8 分"',
    '"Germany–Netherlands, Monday, in Berlin"': '"德國—荷蘭，週一，柏林"',
    '"St Martin\'s Day is the festival of sharing"': '"聖馬丁節是分享的節日"',
    '"A tradition lives on when people keep celebrating it"': '"傳統會一直活下去，只要人們繼續慶祝它"',
    '"Subject + verb + time"': '"主詞 + 動詞 + 時間"',
    '"Subject + verb + object + place"': '"主詞 + 動詞 + 受詞 + 地點"',
    '"Subject + verb + time + opponent"': '"主詞 + 動詞 + 時間 + 對手"',
    '"Subject + verb + manner + place"': '"主詞 + 動詞 + 方式 + 地點"',
    '"Watch the ordinal 88e"': '"注意序數 88e"',
    '"schoen zetten is a fixed expression"': '"schoen zetten 是固定說法"',
    '["journaal = news programme b", "intocht = the festive arrival d", "lampion = lantern a", "delen = to share c"]':
        '["journaal = 新聞節目 b", "intocht = 慶典進城 d", "lampion = 燈籠 a", "delen = 分享 c"]',
    '"schoen = shoe"': '"schoen = 鞋子"',
    '"wortel = carrot (for the horse)"': '"wortel = 胡蘿蔔（給馬的）"',
    '"verlanglijstje = wish list"': '"verlanglijstje = 願望清單"',
    '"cadeautje = little present"': '"cadeautje = 小禮物"',
    '"18:00 = the Sinterklaas news time"': '"18:00 = 辛特克拉斯新聞時間"',
    '"Sanne lives in Utrecht"': '"珊恩住在烏特勒支"',
    '"On Wednesday she joins the St Martin\'s parade"': '"週三她參加聖馬丁遊行"',
    '"She puts a carrot and a wish list in her shoe"': '"她在鞋子裡放一根胡蘿蔔和一份願望清單"',
    '"She watches the Sinterklaas news every day at 18:00"': '"她每天 18:00 看辛特克拉斯新聞"',
    '"Het diner was published in 2009"': '"《晚餐》出版於 2009 年"',
    '"Sinterklaas receives the key to the city at the Maritime Museum"':
        '"辛特克拉斯在海事博物館接過城市鑰匙"',
    '"Pakjesavond is on Saturday 5 December"': '"禮物之夜在 12 月 5 日週六"',
    '"Grave lies on the river Maas"': '"赫拉弗位於馬斯河畔"',
    '"Compare with the page 3 article"': '"對照第 3 版文章"',
    '"Original sentence from page 2 · delen = to share"': '"第 2 版原句 · delen = 分享"',
    '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Translate into English"':
        '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="翻譯"',
    '"Sint-Maarten is het feest van het delen. → ___", instr="Translate into English"':
        '"Sint-Maarten is het feest van het delen. → ___", instr="翻譯"',
    '"The arrival in Amsterdam is the 88th edition. → ___", instr="Translate into Dutch"':
        '"阿姆斯特丹進城是第 88 屆。→ ___", instr="翻譯"',
    '"I put out my shoe, with a wish list inside. → ___", instr="Translate into Dutch"':
        '"我擺出鞋子，裡面放著願望清單。→ ___", instr="翻譯"',
    '"(open task, model text below)"': '"（開放題，範文見下）"',
    "Writing task (no single answer); model text ({NWORDS} words) below.":
        "寫作題（沒有唯一答案）；範文（{NWORDS} 詞）見下。",
    "See the model text in section H ({NWORDS} words)":
        "範文見 H 部分（{NWORDS} 詞）",
    '"ANTWOORDEN · ANSWER KEY — grouped by page: find your number"':
        '"ANTWOORDEN · 全部答案與簡析（第 1–8 版）"',
    '"Every answer has a short note in English · ✓ marks the writing task"':
        '"每題附一句繁體中文簡析 · 帶 ✓ 的為範文題"',
    '"schoen zetten = to put out your shoe"': '"schoen zetten = 擺鞋子"',
    '"Netherlands–Greece kicks off at 20:45 on Friday"': '"荷蘭—希臘之戰在週五 20:45 開踢"',
    '"The Sinterklaas news is on every day at 18:00"': '"辛特克拉斯新聞每天 18:00 播出"',
    '"The Sinterklaas news starts on Monday 9 November."': '"辛特克拉斯新聞在 11 月 9 日週一開播。"',
    '"hij → gaat zetten"': '"hij → gaat zetten"',
    '"40 + 20 = 60"': '"40 + 20 = 60"',
})

# pairs that need special handling
SKIP_IDX = {0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11}
BADGE_IDX = 14
# pair 7: identity rep on the post-loop 寫作 check form
# pairs 8, 9, 10: P8 sizes stay at CORE values; only the separator TEXT
#   changes (PAGINA -> 第 N 版), handled by the furniture rep below
# pair 11: svglib — skipped; the TC svglib is copied from the W45 zh-tw build
# pair 13: subtitle — spaced form 荷 語 週 報 via map lookup

hdr = '''# -*- coding: utf-8 -*-
"""One-off fan-out transform: W46 NL core (Simplified explanations) -> NL x ZH-TW.
Line-literal replacements only, each asserted. Run once from this dir.
Dutch target text, keys (except re-aimed 137/138), facts, images: untouched.
Furniture per the W43/W45 NL x ZH-TW registry: badge REPLACES strapline
y=372 (19.5pt bold BRICK), footer 荷語週報, gloss prefix 譯注｜ (added by
gloss() itself), P8 sizes at CORE values with '— 第 N 版 —' separators.
Type tokens in Traditional forms; instr words localised (all four
translation items carry instr 翻譯, no direction refinement). bridge()
renamed to expl(); P7 bridges use '；', glosses ' · ', P8 notes ' = '
with FULL-WIDTH parentheses （）. Disclosure variable KEEPS the name
dt_zh. The TC svglib (TC face) is copied from the W45 zh-tw build after
this transform runs.
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
    rep(f, "weekly-report-w46-nl-core/svg", "weekly-report-w46-nl-zh-tw/svg")

# ---------- types + instr (instrs FIRST, cloze before plain choice) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep_opt(f, 'instr="判断"', 'instr="判斷"')
    rep_opt(f, 'instr="写作"', 'instr="寫作"')
    rep_opt(f, 'instr="翻译"', 'instr="翻譯"')
    rep_opt(f, "完形单选", "完形單選")
    rep_opt(f, "词汇配对", "詞彙配對")
    rep_opt(f, "判断对错", "判斷對錯")
    rep_opt(f, "单选", "單選")
    rep_opt(f, "翻译", "翻譯")
    rep_opt(f, "写作", "寫作")

# ---------- furniture ----------
rep("render.py", "weekly-report-w46-nl-core", "weekly-report-w46-nl-zh-tw")
rep("render.py", "De-Lucerna-VOL3.pdf", "De-Lucerna-VOL3-ZH-TW.pdf")
rep_opt("render.py", "Render the NL weekly VOL.3", "Render the NL x ZH-TW weekly VOL.3")
rep_opt("run.py", "Run the IT weekly", "Run the NL x ZH-TW weekly")
rep("bslib4.py", "De Lucerna · 荷兰语周报 VOL.3 · LUCERNA DUTCH WEEKLY",
     "De Lucerna · 荷語週報 VOL.3 · 正文荷語 · 講解繁體中文")
rep("bslib4.py", "译注｜", "譯注｜")
rep("bslib4.py", "    def bridge(self, s, size=20.5, gap=9, fill=GREY):",
     "    def expl(self, s, size=20.5, gap=9, fill=GREY):")
rep("content8.py", 'af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
     'af.para(f"— 第 {pg} 版 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)')
rep("content8.py", 'f.bridge(f"', 'f.expl(f"')

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
    simp = 0
    SIMP_ONLY = set("说话让读这们为时对从给个样点发头长风电车马鱼鸟龙龟买卖读写画听观见贝负质识认议论设许证评课语谢谢谈谣远远还进过运连选达边际陆阳阴云雾惊惧怀态异圣庄庆广厂厅厉压梦毕欢劝仅术机权树桥楼馆饱饮饭饺汤鸡鹅猪猫狮虫蚁赞帮团园围图圆员呜呕备复处务劳动劲奋愿宪岛岁罗罢网纸纹红纪纱线组织终细结绝继断续练缎缓缴罚羡职联声够夸夹夺奋奖奥湾滩浅浆测浓浇浑沟没泽洁渔渗湿溃溅涨渣潜澜炉烂烟烦烧烫爱爷妈国场块坝坞坛坏坚坠垄垒垦垫墙壳壶壮声")

    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py",
              "bslib4.py", "render.py", "run.py"]:
        for ln in open(os.path.join(HERE, f), encoding="utf-8"):
            simp += sum(1 for ch in ln if ch in SIMP_ONLY)
    print("simplified-only chars left:", simp)

if __name__ == "__main__":
    main()
'''

out = []
missing = []
for j, (f, old, new) in enumerate(pairs):
    if j in SKIP_IDX:
        continue
    if j == 7:
        form = 'if e_["type"] == "寫作":'
        out.append((f, form, form))
        continue
    if j == BADGE_IDX:
        badge = ('p.text(975, 372, "荷語正文 · 繁體中文講解 — '
                 '給繁體中文讀者的版本", 19.5, "sans", True, BRICK, anchor="middle")')
        out.append((f, old, badge))
        continue
    if "writing题" in old:
        old = old.replace("writing题", "寫作题")
        out.append((f, old, ZHTW_MAP[new].replace(".bridge(", ".expl(")))
        continue
    if 'instr="Translate' in old:
        old = old.replace('instr="Translate into English"', 'instr="翻譯"')
        old = old.replace('instr="Translate into Dutch"', 'instr="翻譯"')
        old = old.replace('instr="Translate"', 'instr="翻譯"')
    if new in ZHTW_MAP:
        val = ZHTW_MAP[new].replace(".bridge(", ".expl(")
        out.append((f, old, val))
    elif len(new) > 1 and new.startswith('"') and new.endswith('"') and new[1:-1] in ZHTW_MAP:
        out.append((f, old, '"' + ZHTW_MAP[new[1:-1]].replace(".bridge(", ".expl(") + '"'))
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
with open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/transform_zhtw.py", "w", encoding="utf-8") as fh:
    fh.write(hdr)
    for f, old, new in ded:
        fh.write(f"rep({f!r}, {old!r}, {new!r})\n")
    fh.write(tail)
print("wrote", len(ded), "reps")
