# -*- coding: utf-8 -*-
"""Generate W46 NL x JA transform.py from the EN rep pairs (hidden_files/w46/en-reps.txt).
JA precedent (W45 NL x JA): type tokens TRANSLATED to Japanese; instr words
localised; per-direction 日本語に訳す/オランダ語に訳す. Badge REPLACES the
strapline at y=372, 19.5pt BRICK. Subtitle uses spaced kana. P8 sizes stay at
CORE values (Flow 2552, separators 14/1.16/2, keys 13.5/1.16/0.5) with the
separator text '— N ページ —'. bridge() renamed to expl(); P7 bridges use
'；', glosses use ' · ', P8 notes use ' = ' with FULL-WIDTH parentheses
（）. The JP svglib (JP face + kinsoku patch) is copied from the W45 JA
build AFTER the transform, not generated here. Disclosure variable dt_ja."""
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

JA_MAP = {
    "ELKE WEEK IN HET NEDERLANDS · EVERY WEEK · REAL DUTCH":
        "ELKE WEEK IN HET NEDERLANDS · 毎週一号 · オランダ人が読んでいるオランダ語を読む",
    "SINTERKLAAS IS COMING": "シンタクラースがやって来る",
    "This week: Sinterklaas comes to the Netherlands · see page 3":
        "今週：シンタクラースがオランダにやって来る · 3ページ参照",
    'f.bridge("Note | de intocht = arrival · de stoomboot = steamboat · de lampion = lantern.")':
        'f.bridge("解説 — de intocht 到着 · de stoomboot 蒸気船 · de lampion ランタン。")',
    "DE WEEK IN CIJFERS · IN NUMBERS": "DE WEEK IN CIJFERS · 数字で見る今週",
    " (9 Nov: Sinterklaas news)": "（11月9日：シンタクラース・ニュース開始）",
    " (14 Nov: national arrival, Grave)": "（11月14日：グラーフェ全国到着）",
    " (15 Nov: 88th)": "（11月15日：アムステルダム到着、第88回）",
    " (Fri 20:45)": "（金曜20:45）",
    "NU JIJ · YOUR TURN": "NU JIJ · 君の番",
    "The Sinterklaas news starts on 9 November": "シンタクラース・ニュースは11月9日に始まる",
    "The national arrival is in Grave": "全国到着はグラーフェ",
    "The Amsterdam arrival is on Sunday 15 November": "アムステルダム到着は11月15日（日）",
    "St Martin's Day is on Wednesday 11 November": "聖マルティン祭は11月11日（水）",
    "Netherlands–Greece kicks off at 20:45": "オランダ対ギリシャ、20:45キックオフ",
    "Plural subject, so zetten": "複数主語だから zetten",
    "· THIS WEEK": "· 今週の予定",
    "Agenda van de week · THIS WEEK'S EVENTS": "Agenda van de week · 今週の出来事",
    "See pages 2–4 for all dates and times.": "すべての日時については2～4ページ参照。",
    "IN DEZE EDITIE · IN THIS ISSUE": "IN DEZE EDITIE · 今号の内容",
    "«The intocht»: Sinterklaas arrives in a town by boat, then on horseback, in a festive parade.":
        "「de intocht」：祝祭の到着行列。",
    "IN HET KORT · IN BRIEF": "IN HET KORT · 要約",
    "BLIKSEMQUIZ · LIGHTNING QUIZ": "BLIKSEMQUIZ · 閃光クイズ",
    "Read page 1, choose the right answer · answers on page 8":
        "1ページを読んで、正しい答えを選ぼう · 答えは8ページ",
    "The Sinterklaas news starts on Monday 9 November": "シンタクラース・ニュースは11月9日（月）に始まる",
    "The Amsterdam arrival is the 88th edition": "アムステルダム到着は第88回",
    'p.band("LEVEN · LIFE", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · St Martin\'s Day: lanterns and songs")':
        'p.band("LEVEN · 生活", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · 聖マルティン祭：ランタンと歌")',
    "ZO ONTHOUD JE HET · REMEMBER": "ZO ONTHOUD JE HET · 覚え方",
    'f.gloss("de lampion = lantern · delen = to share · de mantel = cloak, coat · de bedelaar = beggar · het erfgoed = heritage · het ledlampje = little LED light.")':
        'f.gloss("de lampion ランタン · delen 分け合う · de mantel マント · de bedelaar 物乞い · het erfgoed 文化遺産 · het ledlampje LEDライト。")',
    "On 11 November, will you go singing door to door with a lantern, or would you rather watch the Sinterklaas news? Write two sentences in Dutch and send them to the editors.":
        "11月11日、ランタンを持って戸別に歌いに行く？それともシンタクラース・ニュースを見る？オランダ語で2文書いて編集部に送ろう。",
    "EN JIJ? · AND YOU?": "EN JIJ? · 君は？",
    "SINT-MAARTEN IN VIER WOORDEN · FOUR KEY WORDS": "SINT-MAARTEN IN VIER WOORDEN · 4つのキーワード",
    "Wat hoort bij het feest? · Which words belong to the festival?":
        "Wat hoort bij het feest? · 祭りに合う言葉はどれ？",
    "a paper lantern, with an LED light inside": "紙のランタン、中にLEDライト",
    "sharing: giving half a cloak to a beggar": "分け合う：マントの半分を物乞いに与える",
    "St Martin's city, on the heritage list": "聖マルティンの町、遺産リスト入り",
    "singing St Martin's songs door to door": "戸別に聖マルティンの歌を歌う",
    "OEFENINGEN · EXERCISES ON PAGE 2": "OEFENINGEN · 2ページの練習",
    "Answers on page 8 · levels are mixed; find your number": "答えは8ページ · レベルは混ざっている、番号で探そう",
    'e.bridge("Read the article on page 2 and choose the right answer.")':
        'e.bridge("2ページの記事を読んで、正しい答えを選ぼう。")',
    "Children go door to door with lanterns": "子どもたちはランタンを持って戸別に回る",
    "Martinus gave half his cloak to a beggar": "マルティヌスはマントの半分を物乞いに与えた",
    "Utrecht is St Martin's city": "ユトレヒトは聖マルティンの町",
    "A lantern takes an LED light, not a candle": "ランタンにはろうそくではなくLEDライト",
    'e.bridge("Fill in with words from page 2.")': 'e.bridge("2ページの言葉で空所を埋めよう。")',
    "St Martin's Day is on 11 November": "聖マルティン祭は11月11日",
    "lampion = lantern (de)": "lampion = ランタン（de）",
    "delen = to share": "delen = 分け合う",
    "mantel = cloak (de)": "mantel = マント（de）",
    "St Martin's city is Utrecht": "聖マルティンの町はユトレヒト",
    'e.bridge("Fill in with the song words and the safety tip.")':
        'e.bridge("歌の言葉と安全のヒントで空所を埋めよう。")',
    "Song words: my little light may shine": "歌の言葉：私の小さな灯りがともる",
    "Lanterns shine brightest when it is dark": "暗いときランタンは最も明るく輝く",
    "An LED light is safe": "LEDライトは安全",
    "Pakjesavond is on 5 December": "パッケスアーフォントは12月5日",
    '["lampion = lantern b", "delen = to share a", "mantel = cloak d", "erfgoed = heritage c"]':
        '["lampion = ランタン b", "delen = 分け合う a", "mantel = マント d", "erfgoed = 文化遺産 c"]',
    'instr="Match word to meaning"': 'instr="語と意味を結ぶ"',
    "HET NIEUWS · TOP STORY": "HET NIEUWS · トップ記事",
    # EN fix-(f) shortened forms
    "mijn schoen = my shoe.": "mijn schoen = 私の靴。",
    "Fixed phrase: langs de deuren.": "決まり文句：langs de deuren。",
    "Verb first after the als-clause: ben ik blij.": "als節の後では動詞が先頭：ben ik blij。",
    "schoen zetten = to put out your shoe, with a carrot and a drawing inside.":
        "schoen zetten = 靴を出す、ニンジンと絵を入れて。",
    'dt_en = "No real letters or best page-8 texts at press time — example; promise to VOL.4."':
        'dt_ja = "締切時に本物の手紙と8ページの優秀作文はなく、例文を掲載。約束はVOL.4へ。"',
    "WEEKBLAD IN HET NEDERLANDS · VOL.3 · SINTERKLAAS · SINT-MAARTEN · ORANJE":
        "オ ラ ン ダ 語 週 刊 · VOL.3 · SINTERKLAAS · SINT-MAARTEN · ORANJE",
}
JA_MAP.update({
    'p.band("CULTUUR · CULTURE", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · The Sinterklaas news and Het diner")':
        'p.band("CULTUUR · 文化", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · シンタクラース・ニュースと『Het diner』")',
    'f.gloss("het journaal = news programme · de flessenpost = message in a bottle · de burgemeester = mayor · de stoet = procession · de leeskring = reading club.")':
        'f.gloss("het journaal ニュース番組 · de flessenpost 瓶の手紙 · de burgemeester 市長 · de stoet 行列 · de leeskring 読書会。")',
    "OEFENINGEN · EXERCISES ON PAGE 3": "OEFENINGEN · 3ページの練習",
    'e.bridge("Read the article on page 3 and choose the right answer.")':
        'e.bridge("3ページの記事を読んで、正しい答えを選ぼう。")',
    "The Sinterklaas news is on every day at 18:00": "シンタクラース・ニュースは毎日18:00に放送される",
    "The Amsterdam boat leaves De Omval at 10:15": "アムステルダムの船は10:15にデ・オムファルを出る",
    "Het diner was written by Herman Koch": "『Het diner』はヘルマン・コッホの作品",
    "Het diner is free to pick up at the library": "『Het diner』は図書館で無料でもらえる",
    'e.bridge("Fill in with the words from the box.")': 'e.bridge("枠の中の言葉で空所を埋めよう。")',
    "journaal = news programme": "journaal = ニュース番組",
    "burgemeester = mayor": "burgemeester = 市長",
    "stoet = procession": "stoet = 行列",
    "flessenpost = message in a bottle": "flessenpost = 瓶の手紙",
    "leeskring = reading club": "leeskring = 読書会",
    'e.bridge("Complete with the present perfect. Watch the auxiliaries hebben/zijn.")':
        'e.bridge("現在完了形で補おう。助動詞hebben／zijnに注意。")',
    "beginnen takes zijn: is begonnen": "beginnenはzijnを取る：is begonnen",
    "vinden perfectum: heeft gevonden": "vindenの完了形：heeft gevonden",
    "aankomen takes zijn: is aangekomen": "aankomenはzijnを取る：is aangekomen",
    "lezen perfectum: hebben gelezen": "lezenの完了形：hebben gelezen",
    'e.bridge("Work it out: answer with the numbers from page 3.")':
        'e.bridge("計算しよう：3ページの数字で答えよう。")',
    "From 9 to 14 November is 5 days": "11月9日から14日までは5日間",
    "From 9 to 15 November is 6 days": "11月9日から15日までは6日間",
    "The Grave programme, 12:00–16:00, lasts 4 hours": "グラーフェのプログラム、12:00～16:00は4時間",
    "Het diner is from 2009: 17 years ago in 2026": "『Het diner』は2009年の作品：2026年で17年前",
    'p.band("SPORT", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · Oranje and the Nations League")':
        'p.band("SPORT · スポーツ", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · オラニエとネーションズリーグ")',
    'f.gloss("de groepsfase = group stage · de kwartfinale = quarter-final · ongeslagen = unbeaten · de interland = international match · de stand = the table.")':
        'f.gloss("de groepsfase グループリーグ · de kwartfinale 準々決勝 · ongeslagen 無敗 · de interland 国際試合 · de stand 順位表。")',
    "OEFENINGEN · EXERCISES ON PAGE 4": "OEFENINGEN · 4ページの練習",
    'e.bridge("Read the article on page 4 and choose the right answer.")':
        'e.bridge("4ページの記事を読んで、正しい答えを選ぼう。")',
    "Netherlands–Greece, Friday 20:45, in Amsterdam": "オランダ対ギリシャ、金曜20:45、アムステルダム",
    "The Netherlands and Greece both have 8 points": "オランダとギリシャはともに勝ち点8",
    "The Netherlands scored more goals in the group (7 to 5)": "オランダはグループで多く得点した：7対5",
    "Germany–Netherlands, Monday, in Berlin": "ドイツ対オランダ、月曜、ベルリン",
    "Eredivisie matchday 13 is on 21–22 November": "エールディヴィジ第13節は11月21～22日",
    'e.bridge("Fill in with the words from the box. Watch the verb forms.")':
        'e.bridge("枠の中の言葉で空所を埋めよう。動詞の形に注意。")',
    "groepsfase = group stage": "groepsfase = グループリーグ",
    "kwartfinale plural: kwartfinales": "kwartfinale、複数形：kwartfinales",
    "ongeslagen = unbeaten": "ongeslagen = 無敗",
    "stand = the table": "stand = 順位表",
    "interland = international match": "interland = 国際試合",
    'e.bridge("Complete with the past tense or the perfect tense.")':
        'e.bridge("過去形か完了形で補おう。")',
    "spelen past tense: speelde": "spelenの過去形：speelde",
    "winnen past tense: won": "winnenの過去形：won",
    "maken past tense: maakte": "makenの過去形：maakte",
    "komen perfectum takes zijn": "komenの完了形はzijnを取る",
    "True: Netherlands–Greece, Friday 20:45": "正しい：オランダ対ギリシャ、金曜20:45",
    "False: Serbia are bottom with 0 points": "誤り：セルビアは勝ち点0で最下位",
    "False: Eredivisie matchday 13 is on 21–22 November": "誤り：エールディヴィジ第13節は11月21～22日",
    "True: PSV beat Willem II 7–0": "正しい：PSVがヴィレムIIに7対0で勝利",
    'p.band("JONGEREN · YOUNG PEOPLE", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · Robinson, the shoe and the wish list")':
        'p.band("JONGEREN · 若者", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · ロビンソン、靴と願い事リスト")',
    " (watch on RTL 4, Sunday 20:00)": "（日曜20:00にRTL 4で見る）",
    " (watch the trials: points are won there)": "（トライアルを見る：得点はそこで決まる）",
    " (guess with friends who stays longest)": "（友達と誰が一番長く残るか予想する）",
    " (then put out your shoe, wish list inside)": "（それから靴を出す、願い事リスト入りで）",
    'f.gloss("het verlanglijstje = wish list · de verslaggever = reporter · de proef = trial, challenge · stemmen = to vote · de aflevering = episode.")':
        'f.gloss("het verlanglijstje 願い事リスト · de verslaggever リポーター · de proef トライアル、試練 · stemmen 投票する · de aflevering エピソード。")',
    "On Sunday, do you watch Expeditie Robinson, or would you rather put out your shoe with a wish list? Write two sentences in Dutch and send them in.":
        "日曜は『Expeditie Robinson』を見る？それとも願い事リスト入りの靴を出す？オランダ語で2文書いて送ろう。",
    "OEFENINGEN · EXERCISES ON PAGE 5": "OEFENINGEN · 5ページの練習",
    'e.bridge("Read the article on page 5 and choose the right answer.")':
        'e.bridge("5ページの記事を読んで、正しい答えを選ぼう。")',
    "Robinson is on every Sunday at 20:00 on RTL 4": "ロビンソンは毎週日曜20:00にRTL 4で放送",
    "19 contestants": "19人の参加者",
    "The show is filmed on a desert island in Malaysia": "番組はマレーシアの無人島で撮影される",
    "The contestants spend 34 days on the island": "参加者は島で34日間過ごす",
    "A wish list goes in the shoe": "願い事リストは靴の中に入れる",
    "verlanglijstje = wish list (het)": "verlanglijstje = 願い事リスト（het）",
    "verslaggever = reporter (de)": "verslaggever = リポーター（de）",
    "proef = trial, challenge (de)": "proef = トライアル、試練（de）",
    "stemmen = to vote": "stemmen = 投票する",
    "aflevering = episode": "aflevering = エピソード",
    "kandidaat plural: kandidaten": "kandidaat、複数形：kandidaten",
    'e.bridge("Use gaan + infinitive to talk about the future.")':
        'e.bridge("gaan＋不定詞で未来について話そう。")',
    "gaat winnen = will win (just a guess)": "gaat winnen = 勝つだろう（単なる予想）",
    "wij → gaan + infinitive kijken": "wij → gaan＋不定詞 kijken",
    "hij → gaat zetten": "hij → gaat zetten",
    "zij (plural) → gaan schrijven": "zij（複数）→ gaan schrijven",
    "True: the show started on 1 November": "正しい：番組は11月1日に始まった",
    "False: the show is filmed in Malaysia": "誤り：番組はマレーシアで撮影される",
    "False: the carrot in the shoe is for the horse": "誤り：靴の中のニンジンは馬のため",
    'p.band("VERDIEPING · IN DEPTH", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · St Martin\'s Day or Halloween?")':
        'p.band("VERDIEPING · 深掘り", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · 聖マルティン祭かハロウィンか")',
    'f.gloss("de traditie = tradition · griezelen = to scare, to spook · de belangstelling = interest · de achteruitgang = decline · de deskundige = expert.")':
        'f.gloss("de traditie 伝統 · griezelen 怖がらせる · de belangstelling 関心 · de achteruitgang 衰退 · de deskundige 専門家。")',
    "Practice data: invented numbers for practice only, not a real survey. Question: what do you do around 11 November? (100 young people)":
        "練習データ：練習用の作られた数字で、実際の調査ではない。質問：11月11日ごろ、あなたは何をしますか。（100人の若者）",
    "DE GRAFIEK · PRACTICE DATA": "DE GRAFIEK · グラフ（練習データ）",
    "VOOR OF TEGEN? · FOR OR AGAINST?": "VOOR OF TEGEN? · 賛成か反対か",
    "OEFENINGEN · EXERCISES ON PAGE 6": "OEFENINGEN · 6ページの練習",
    'e.bridge("Answer from the chart on page 6 (practice data).")':
        'e.bridge("6ページのグラフ（練習データ）から答えよう。")',
    "40 young people walk with a lantern": "40人の若者がランタンを持って歩く",
    "25 celebrate Halloween": "25人がハロウィンを祝う",
    "40 + 20 = 60": "40 + 20 = 60",
    "15 stay at home": "15人は家にいる",
    "The chart counts 100 people: 40+25+20+15": "グラフは100人を数える：40+25+20+15",
    'e.bridge("Read the article on page 6 and choose the right answer.")':
        'e.bridge("6ページの記事を読んで、正しい答えを選ぼう。")',
    "In 2025, 26% of Dutch people celebrated Halloween": "2025年、オランダ人の26%がハロウィンを祝った",
    "The two surveys use different definitions, so they cannot be compared directly":
        "2つの調査は定義が違うため、直接比較できない",
    "Interest in St Martin's Day increased (Stengs, 2025)": "聖マルティン祭への関心は高まった（Stengs、2025年）",
    "Halloween is about spooking; St Martin's Day is about sharing": "ハロウィンは怖がらせること、聖マルティン祭は分け合うこと",
    "A tradition lives on when people keep celebrating it": "伝統は、人々が祝い続けると生き続ける",
    'e.bridge("Put the words in the right order to make sentences.")':
        'e.bridge("言葉を正しい順序に並べて文を作ろう。")',
    "traditie = tradition (de)": "traditie = 伝統（de）",
    "griezelen = to scare, to spook": "griezelen = 怖がらせる",
    "belangstelling = interest (de)": "belangstelling = 関心（de）",
    "achteruitgang = decline (de)": "achteruitgang = 衰退（de）",
    "Subject + verb + complement + place": "主語＋動詞＋補語＋場所",
    "Subject + verb + manner + place": "主語＋動詞＋様態＋場所",
    "The als-clause comes last": "als節は文末に来る",
    "kiezen + hoeft niet + explanation": "kiezen＋hoeft niet＋説明",
})
JA_MAP.update({
    'p.band("TAAL · LANGUAGE", "De Lucerna", "Language focus · Drie niveaus, drie gereedschappen · Three levels, three tools")':
        'p.band("TAAL · 言語", "De Lucerna", "言語に注目 · Drie niveaus, drie gereedschappen · 3レベル、3つの道具")',
    'a.bridge("de stoomboot = steamboat; de intocht = the festive arrival; de schoen zetten = to put out your shoe; de lampion = lantern.")':
        'a.bridge("de stoomboot 蒸気船；de intocht 祝祭の到着；de schoen zetten 靴を出す；de lampion ランタン。")',
    "de stoomboot = steamboat": "de stoomboot = 蒸気船",
    "The intocht is Sinterklaas's festive arrival": "intochtとはシンタクラースの祝祭の到着のこと",
    "lampion = lantern": "lampion = ランタン",
    'b.bridge("schoentje = little shoe; lichtje = little light; cadeautje = little present. -je means small and affectionate.")':
        'b.bridge("schoentje 小さな靴；lichtje 小さな灯り；cadeautje 小さな贈り物。-jeは小さくて愛情のある意味。")',
    "schoen + -tje: schoentje": "schoen + -tje: schoentje",
    "licht + -je: lichtje": "licht + -je: lichtje",
    "cadeau + -tje: cadeautje": "cadeau + -tje: cadeautje",
    '"-je means small and affectionate, not always really small"':
        '"-jeは小さくて愛情のある意味、いつも本当に小さいわけではない"',
    'c.bridge("Als… = If… / When…; als het donker wordt = when it gets dark; als Sinterklaas komt = when Sinterklaas comes.")':
        'c.bridge("Als… もし…／～のとき；als het donker wordt 暗くなるとき；als Sinterklaas komt シンタクラースが来るとき。")',
    '"Als… = If… / When…"': '"Als… もし…／～のとき"',
    '"An als-clause is a condition, not a question"': '"als節は条件であって、疑問ではない"',
    '"The verb comes first in the main clause: gaat de lampion aan"':
        '"主節では動詞が先頭に来る：gaat de lampion aan"',
    '"Als Oranje wint… = If Oranje win…"': '"Als Oranje wint… オラニエが勝てば…"',
    "PAS OP! · ERROR CLINIC": "PAS OP! · 間違いクリニック",
    '"Sinterklaas is a name, so it takes no article."': '"Sinterklaasは名前なので、冠詞はつかない。"',
    '"Putting out your shoe takes mijn schoen (my shoe)."': '"mijn schoen = 私の靴。"',
    '"The fixed phrase is langs de deuren (plural)."': '"決まり文句：langs de deuren。"',
    '"After the als-clause, the main-clause verb comes first: ben ik blij."': '"als節の後では動詞が先頭：ben ik blij。"',
    "HET WOORD · WORD OF THE WEEK": "HET WOORD · 今週の単語",
    '"schoen zetten = to put out your shoe: put your shoe by the door, with a carrot and a drawing inside, for Sinterklaas."':
        '"schoen zetten = 靴を出す：ドアのそばに靴を置き、ニンジンと絵を入れて、シンタクラースのために。"',
    'len(wrap(dt_en, "sans", False, 20, CW - 44))': 'len(wrap(dt_ja, "sans", False, 20, CW - 44))',
    'p.para(bx + 22, yy3 + 20, dt_en, 20, "sans", False, GREY, CW - 44, 1.42) + 10':
        'p.para(bx + 22, yy3 + 20, dt_ja, 20, "sans", False, GREY, CW - 44, 1.42) + 10',
    '"Editors\' example — send yours for VOL.4!"':
        '"編集部の例文です。送ってください！"',
    "ZINNEN VAN DE WEEK · PHRASES OF THE WEEK (VERBATIM FROM THIS ISSUE)":
        "ZINNEN VAN DE WEEK · 今週の名文（本号の記事から逐語引用）",
    "On Monday 9 November, the Sinterklaas news starts on television.":
        "11月9日（月）、シンタクラース・ニュースがテレビで始まる。",
    "One day later, Sunday 15 November: the Amsterdam arrival, 88th edition.":
        "その翌日、11月15日（日）：アムステルダム到着、第88回。",
    "St Martin's Day is the festival of sharing: sharing light, food and attention.":
        "聖マルティン祭は分け合いの祭り：光、食べ物、気遣いを分け合う。",
    "On Saturday 14 November, Sinterklaas officially arrives in Grave.":
        "11月14日（土）、シンタクラースはグラーフェに公式に到着する。",
    "On Friday 13 November, Oranje play Greece at home.":
        "11月13日（金）、オラニエはホームでギリシャと対戦する。",
    "Every Sunday at 20:00, Expeditie Robinson is on RTL 4.":
        "毎週日曜20:00、『Expeditie Robinson』はRTL 4で放送される。",
    "St Martin's Day is an old tradition in the Netherlands.":
        "聖マルティン祭はオランダの古い伝統だ。",
    "A tradition lives on when people keep celebrating it.":
        "伝統は、人々が祝い続けると生き続ける。",
    "VOLGENDE WEEK · NEXT WEEK (VOL.4)": "VOLGENDE WEEK · 来週（VOL.4）",
    'p.band("TOETS EN ANTWOORDEN · TEST AND ANSWERS", "De Lucerna", "Page 8 · De grote toets van de week + alle antwoorden")':
        'p.band("TOETS EN ANTWOORDEN · テストと解答", "De Lucerna", "8ページ · De grote toets van de week + alle antwoorden")',
    "Robinson is on RTL 4": "ロビンソンはRTL 4で放送される",
    "St Martin's Day is the festival of sharing.": "聖マルティン祭は分け合いの祭り。",
    "St Martin's Day is the festival of sharing": "聖マルティン祭は分け合いの祭り",
    "Subject + verb + time": "主語＋動詞＋時間",
    "Subject + verb + object + place": "主語＋動詞＋目的語＋場所",
    "Subject + verb + time + opponent": "主語＋動詞＋時間＋相手",
    "Watch the ordinal 88e": "序数88eに注意",
    "schoen zetten is a fixed expression": "schoen zettenは決まり文句",
    '["journaal = news programme b", "intocht = the festive arrival d", "lampion = lantern a", "delen = to share c"]':
        '["journaal = ニュース番組 b", "intocht = 祝祭の到着 d", "lampion = ランタン a", "delen = 分け合う c"]',
    "schoen = shoe": "schoen = 靴",
    "wortel = carrot (for the horse)": "wortel = ニンジン（馬のため）",
    "verlanglijstje = wish list": "verlanglijstje = 願い事リスト",
    "cadeautje = little present": "cadeautje = 小さな贈り物",
    "18:00 = the Sinterklaas news time": "18:00 = シンタクラース・ニュースの時間",
    "Sanne lives in Utrecht": "サンネはユトレヒトに住んでいる",
    "On Wednesday she joins the St Martin's parade": "水曜日、彼女は聖マルティンのパレードに参加する",
    "She puts a carrot and a wish list in her shoe": "彼女は靴にニンジンと願い事リストを入れる",
    "She watches the Sinterklaas news every day at 18:00": "彼女は毎日18:00にシンタクラース・ニュースを見る",
    "Het diner was published in 2009": "『Het diner』は2009年に出版された",
    "Sinterklaas receives the key to the city at the Maritime Museum":
        "シンタクラースは海事博物館で市の鍵を受け取る",
    "Pakjesavond is on Saturday 5 December": "パッケスアーフォントは12月5日（土）",
    "Grave lies on the river Maas": "グラーフェはマース川沿いにある",
    "Compare with the page 3 article": "3ページの記事と比べよう",
    "Original sentence from page 2 · delen = to share": "2ページの原文 · delen = 分け合う",
    '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Translate into English"':
        '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="日本語に訳す"',
    '"Sint-Maarten is het feest van het delen. → ___", instr="Translate into English"':
        '"Sint-Maarten is het feest van het delen. → ___", instr="日本語に訳す"',
    '"The arrival in Amsterdam is the 88th edition. → ___", instr="Translate into Dutch"':
        '"アムステルダム到着は第88回。→ ___", instr="オランダ語に訳す"',
    '"I put out my shoe, with a wish list inside. → ___", instr="Translate into Dutch"':
        '"靴を出す、中に願い事リストを入れて。→ ___", instr="オランダ語に訳す"',
    '"(open task, model text below)"': '"（自由課題、模範文は下記）"',
    "Writing task (no single answer); model text ({NWORDS} words) below.":
        "作文問題（正解は一つではない）；模範文（{NWORDS}語）は下記。",
    "See the model text in section H ({NWORDS} words)":
        "模範文はHセクション参照（{NWORDS}語）",
    "ANTWOORDEN · ANSWER KEY — grouped by page: find your number":
        "ANTWOORDEN · 解答一覧 — ページごとに探そう",
    "Every answer has a short note in English · ✓ marks the writing task":
        "すべての答えに日本語の短い解説つき · ✓は作文問題",
    "schoen zetten = to put out your shoe": "schoen zetten = 靴を出す",
    "Netherlands–Greece kicks off at 20:45 on Friday": "オランダ対ギリシャ、金曜20:45キックオフ",
    "The Sinterklaas news is on every day at 18:00.": "シンタクラース・ニュースは毎日18:00に放送される。",
    "The Sinterklaas news starts on Monday 9 November.": "シンタクラース・ニュースは11月9日（月）に始まる。",
    "hij → gaat zetten": "hij → gaat zetten",
    "40 + 20 = 60": "40 + 20 = 60",
})

# pairs that need special handling
SKIP_IDX = {0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11}
BADGE_IDX = 14
# pair 7: identity rep on the post-loop 作文 check form
# pairs 8, 9, 10: P8 sizes stay at CORE values; only the separator TEXT
#   changes (PAGINA -> N ページ), handled by the furniture rep below
# pair 11: svglib — skipped; the JP svglib is copied from the W45 JA build
# pair 13: subtitle — spaced-kana line via map lookup

hdr = '''# -*- coding: utf-8 -*-
"""One-off fan-out transform: W46 NL core (Chinese explanations) -> NL x JA.
Line-literal replacements only, each asserted. Run once from this dir.
Dutch target text, keys (except re-aimed 137/138), facts, images: untouched.
Furniture per the W43/W45 NL x JA registry: badge REPLACES strapline y=372
(19.5pt bold BRICK), footer オランダ語週刊, gloss prefix 解説 —, P8 sizes at
CORE values with '— N ページ —' separators. Type tokens TRANSLATED to
Japanese; instr words localised; per-direction 日本語に訳す/オランダ語に訳す.
bridge() renamed to expl(); P7 bridges use '；', glosses ' · ', P8 notes
' = ' with FULL-WIDTH parentheses. Disclosure variable dt_ja. The JP
svglib (JP face + kinsoku patch) is copied from the W45 JA build after
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
    rep(f, "weekly-report-w46-nl-core/svg", "weekly-report-w46-nl-ja/svg")

# ---------- types + instr (instrs FIRST, cloze before plain choice) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep_opt(f, 'instr="填空"', 'instr="空所補充"')
    rep_opt(f, 'instr="判断"', 'instr="正誤"')
    rep_opt(f, 'instr="造句"', 'instr="文を作る"')
    rep_opt(f, 'instr="写作"', 'instr="作文"')
    rep_opt(f, 'instr="翻译"', 'instr="翻訳"')
    rep_opt(f, "完形单选", "穴埋め選択")
    rep_opt(f, "完成句子", "文の完成")
    rep_opt(f, "词汇配对", "対応付け")
    rep_opt(f, "判断对错", "正誤判断")
    rep_opt(f, "单选", "選択問題")
    rep_opt(f, "造句", "文を作る")
    rep_opt(f, "翻译", "翻訳")
    rep_opt(f, "写作", "作文")

# ---------- furniture ----------
rep("render.py", "weekly-report-w46-nl-core", "weekly-report-w46-nl-ja")
rep("render.py", "De-Lucerna-VOL3.pdf", "De-Lucerna-VOL3-JA.pdf")
rep_opt("render.py", "Render the NL weekly VOL.3", "Render the NL x JA weekly VOL.3")
rep_opt("run.py", "Run the IT weekly", "Run the NL x JA weekly")
rep("bslib4.py", "De Lucerna · 荷兰语周报 VOL.3 · LUCERNA DUTCH WEEKLY",
     "De Lucerna · オランダ語週刊 VOL.3 · 本文はオランダ語 · 解説は日本語")
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"{n} ページ（全 {total} ページ）"')
rep("bslib4.py", "译注｜", "解説 — ")
rep("bslib4.py", "    def bridge(self, s, size=20.5, gap=9, fill=GREY):",
     "    def expl(self, s, size=20.5, gap=9, fill=GREY):")
rep("content8.py", 'af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
     'af.para(f"— {pg} ページ —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)')
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
        form = 'if e_["type"] == "作文":'
        out.append((f, form, form))
        continue
    if j == BADGE_IDX:
        badge = ('p.text(975, 372, "オランダ語テキスト · 日本語の解説 — '
                 '日本語読者のための版", 19.5, "sans", True, BRICK, anchor="middle")')
        out.append((f, old, badge))
        continue
    if "题（无唯一答案）" in old or new.startswith("Writing task (no single answer)"):
        old = old.replace("writing题", "作文题")
        out.append((f, old, JA_MAP[new].replace(".bridge(", ".expl(")))
        continue
    if 'instr="Translate' in old:
        old = old.replace('instr="Translate into English"', 'instr="翻訳"')
        old = old.replace('instr="Translate into Dutch"', 'instr="翻訳"')
        old = old.replace('instr="Translate"', 'instr="翻訳"')
    if "writing题" in old:
        raise SystemExit(f"unexpected writing-form old at pair {j}: {old!r}")
    if new in JA_MAP:
        val = JA_MAP[new].replace(".bridge(", ".expl(")
        out.append((f, old, val))
    elif len(new) > 1 and new.startswith('"') and new.endswith('"') and new[1:-1] in JA_MAP:
        out.append((f, old, '"' + JA_MAP[new[1:-1]].replace(".bridge(", ".expl(") + '"'))
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
with open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/transform_ja.py", "w", encoding="utf-8") as fh:
    fh.write(hdr)
    for f, old, new in ded:
        fh.write(f"rep({f!r}, {old!r}, {new!r})\n")
    fh.write(tail)
print("wrote", len(ded), "reps")
