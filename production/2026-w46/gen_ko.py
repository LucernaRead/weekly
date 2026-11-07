# -*- coding: utf-8 -*-
"""Generate W46 NL x KO transform.py from the EN rep pairs (hidden_files/w46/en-reps.txt).
KO precedent (W45 NL x KO): type tokens TRANSLATED to Korean; instr words
localised; per-direction 한국어로 번역/네덜란드어로 번역. Badge REPLACES the
strapline at y=372, 19.5pt BRICK. P8 sizes stay at CORE values (Flow 2552,
separators 14/1.16/2, keys 13.5/1.16/0.5) with the separator text
'— 제 N 면 —'. bridge() KEPT; gloss() adds the '해설 — ' prefix itself.
P7 bridges use ';', glosses ' · ', P8 notes ' = ' with HALF-WIDTH
parentheses (). Disclosure variable KEEPS the name dt_zh. svglib is
byte-identical to the core svglib (SC face renders Hangul) — no svglib rep.
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

KO_MAP = {
    "ELKE WEEK IN HET NEDERLANDS · EVERY WEEK · REAL DUTCH":
        "ELKE WEEK IN HET NEDERLANDS · 매주 발행 · 네덜란드인이 읽는 네덜란드어",
    "WEEKBLAD IN HET NEDERLANDS · VOL.3 · SINTERKLAAS · SINT-MAARTEN · ORANJE":
        "네덜란드어 주간지 · VOL.3 · 신터클라스 · 성 마르틴의 날 · 오라녜",
    '"SINTERKLAAS IS COMING"': '"신터클라스가 오고 있어요"',
    '"This week: Sinterklaas comes to the Netherlands · see page 3"':
        '"이번 주: 신터클라스가 네덜란드에 와요 · 3면 참조"',
    'f.bridge("Note | de intocht = arrival · de stoomboot = steamboat · de lampion = lantern.")':
        'f.bridge("해설 — de intocht 도착 · de stoomboot 증기선 · de lampion 등롱.")',
    '"DE WEEK IN CIJFERS · IN NUMBERS"': '"DE WEEK IN CIJFERS · 이번 주 숫자"',
    " (9 Nov: Sinterklaas news)": " (11월 9일: 신터클라스 뉴스)",
    " (14 Nov: national arrival, Grave)": " (11월 14일: 전국 도착, 흐라버)",
    " (15 Nov: 88th)": " (15일: 88회)",
    " (Fri 20:45)": " (금요일 20:45)",
    '"NU JIJ · YOUR TURN"': '"NU JIJ · 여러분 차례"',
    '"The Sinterklaas news starts on 9 November"': '"신터클라스 뉴스는 11월 9일에 시작해요"',
    '"The national arrival is in Grave"': '"전국 도착은 흐라버에서 열려요"',
    '"The Amsterdam arrival is on Sunday 15 November"': '"암스테르담 도착은 11월 15일 일요일이에요"',
    '"St Martin\'s Day is on Wednesday 11 November"': '"성 마르틴의 날은 11월 11일 수요일이에요"',
    '"Netherlands–Greece kicks off at 20:45"': '"네덜란드–그리스 경기는 20:45에 시작해요"',
    '"Plural subject, so zetten"': '"복수 주어라서 zetten이에요"',
    '"· THIS WEEK"': '"· 이번 주"',
    '"Agenda van de week · THIS WEEK\'S EVENTS"': '"Agenda van de week · 이번 주 일정"',
    '"See pages 2–4 for all dates and times."': '"모든 날짜와 시간은 2–4면을 보세요."',
    '"IN DEZE EDITIE · IN THIS ISSUE"': '"IN DEZE EDITIE · 이번 호 내용"',
    '"«The intocht»: Sinterklaas arrives in a town by boat, then on horseback, in a festive parade."':
        '"«de intocht»: 축제 도착 행렬이에요."',
    '"IN HET KORT · IN BRIEF"': '"IN HET KORT · 요약"',
    '"BLIKSEMQUIZ · LIGHTNING QUIZ"': '"BLIKSEMQUIZ · 번개 퀴즈"',
    '"Read page 1, choose the right answer · answers on page 8"':
        '"1면을 읽고 정답을 고르세요 · 정답은 8면"',
    '"The Sinterklaas news starts on Monday 9 November"': '"신터클라스 뉴스는 11월 9일 월요일에 시작해요"',
    '"The Amsterdam arrival is the 88th edition"': '"암스테르담 도착은 88회째예요"',
    'p.band("LEVEN · LIFE", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · St Martin\'s Day: lanterns and songs")':
        'p.band("LEVEN · 생활", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · 성 마르틴의 날: 등롱과 노래")',
    '"ZO ONTHOUD JE HET · REMEMBER"': '"ZO ONTHOUD JE HET · 기억해요"',
    'f.gloss("de lampion = lantern · delen = to share · de mantel = cloak, coat · de bedelaar = beggar · het erfgoed = heritage · het ledlampje = little LED light.")':
        'f.gloss("de lampion 등롱 · delen 나누다 · de mantel 외투 · de bedelaar 거지 · het erfgoed 문화유산 · het ledlampje 작은 LED 등.")',
    'instr="Match word to meaning"': 'instr="단어와 뜻 짝짓기"', 
    '"On 11 November, will you go singing door to door with a lantern, or would you rather watch the Sinterklaas news? Write two sentences in Dutch and send them to the editors."':
        '"11월 11일, 등롱을 들고 집집마다 노래하러 갈 거예요, 아니면 신터클라스 뉴스를 볼 거예요? 네덜란드어로 두 문장을 써서 편집부에 보내 주세요."',
    '"EN JIJ? · AND YOU?"': '"EN JIJ? · 여러분은요?"',
    '"SINT-MAARTEN IN VIER WOORDEN · FOUR KEY WORDS"': '"SINT-MAARTEN IN VIER WOORDEN · 네 단어"',
    '"Wat hoort bij het feest? · Which words belong to the festival?"':
        '"Wat hoort bij het feest? · 축제에 어울리는 단어는?"',
    '"a paper lantern, with an LED light inside"': '"LED 등이 들어 있는 종이 등롱"',
    '"sharing: giving half a cloak to a beggar"': '"나누기: 외투 절반을 거지에게"',
    '"St Martin\'s city, on the heritage list"': '"성 마르틴의 도시, 문화유산 목록에 올라 있어요"',
    '"singing St Martin\'s songs door to door"': '"집집마다 성 마르틴 노래 부르기"',
    '"OEFENINGEN · EXERCISES ON PAGE 2"': '"OEFENINGEN · 2면 연습"',
    '"Answers on page 8 · levels are mixed; find your number"':
        '"정답은 8면 · 문제는 수준이 섞여 있어요, 번호로 찾으세요"',
    'e.bridge("Read the article on page 2 and choose the right answer.")':
        'e.bridge("2면 기사를 읽고 정답을 고르세요.")',
    '"Children go door to door with lanterns"': '"아이들은 등롱을 들고 집집마다 다녀요"',
    '"Martinus gave half his cloak to a beggar"': '"마르티누스는 외투 절반을 거지에게 주었어요"',
    '"Utrecht is St Martin\'s city"': '"위트레흐트는 성 마르틴의 도시예요"',
    '"A lantern takes an LED light, not a candle"': '"등롱에는 촛불이 아니라 LED 등을 넣어요"',
    'e.bridge("Fill in with words from page 2.")': 'e.bridge("2면 단어로 채우세요.")',
    '"St Martin\'s Day is on 11 November"': '"성 마르틴의 날은 11월 11일이에요"',
    '"lampion = lantern (de)"': '"lampion = 등롱 (de)"',
    '"delen = to share"': '"delen = 나누다"',
    '"mantel = cloak (de)"': '"mantel = 외투 (de)"',
    '"St Martin\'s city is Utrecht"': '"성 마르틴의 도시는 위트레흐트예요"',
    'e.bridge("Fill in with the song words and the safety tip.")':
        'e.bridge("노랫말과 안전 수칙으로 채우세요.")',
    '"Song words: my little light may shine"': '"노랫말: 내 작은 불이 빛나도 돼요"',
    '"Lanterns shine brightest when it is dark"': '"등롱은 어두울 때 가장 밝게 빛나요"',
    '"An LED light is safe"': '"LED 등은 안전해요"',
    '"Pakjesavond is on 5 December"': '"팍예스아폰트는 12월 5일이에요"',
    '["lampion = lantern b", "delen = to share a", "mantel = cloak d", "erfgoed = heritage c"]':
        '["lampion = 등롱 b", "delen = 나누다 a", "mantel = 외투 d", "erfgoed = 문화유산 c"]',
    '"HET NIEUWS · TOP STORY"': '"HET NIEUWS · 톱 기사"',
    'p.band("CULTUUR · CULTURE", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · The Sinterklaas news and Het diner")':
        'p.band("CULTUUR · 문화", "De Lucerna", "NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · 신터클라스 뉴스와 『Het diner』")',
    'f.gloss("het journaal = news programme · de flessenpost = message in a bottle · de burgemeester = mayor · de stoet = procession · de leeskring = reading club.")':
        'f.gloss("het journaal 뉴스 프로그램 · de flessenpost 병에 넣은 편지 · de burgemeester 시장 · de stoet 행렬 · de leeskring 독서 모임.")',
    '"OEFENINGEN · EXERCISES ON PAGE 3"': '"OEFENINGEN · 3면 연습"',
    'e.bridge("Read the article on page 3 and choose the right answer.")':
        'e.bridge("3면 기사를 읽고 정답을 고르세요.")',
    '"The Sinterklaas news is on every day at 18:00"': '"신터클라스 뉴스는 매일 18:00에 방송해요"',
    '"The national arrival is in Grave"': '"전국 도착은 흐라버에서 열려요"',
    '"The Amsterdam boat leaves De Omval at 10:15"': '"암스테르담 배는 10:15에 더 옴팔을 떠나요"',
    '"Het diner was written by Herman Koch"': '"『Het diner』는 헤르만 코흐가 썼어요"',
    '"Het diner is free to pick up at the library"': '"『Het diner』는 도서관에서 무료로 가져갈 수 있어요"',
    'e.bridge("Fill in with the words from the box.")': 'e.bridge("상자 속 단어로 채우세요.")',
    '"journaal = news programme"': '"journaal = 뉴스 프로그램"',
    '"burgemeester = mayor"': '"burgemeester = 시장"',
    '"stoet = procession"': '"stoet = 행렬"',
    '"flessenpost = message in a bottle"': '"flessenpost = 병에 넣은 편지"',
    '"leeskring = reading club"': '"leeskring = 독서 모임"',
    'e.bridge("Complete with the present perfect. Watch the auxiliaries hebben/zijn.")':
        'e.bridge("현재완료로 채우세요. 조동사 hebben/zijn에 주의하세요.")',
    '"beginnen takes zijn: is begonnen"': '"beginnen은 zijn을 써요: is begonnen"',
    '"vinden perfectum: heeft gevonden"': '"vinden 완료형: heeft gevonden"',
    '"aankomen takes zijn: is aangekomen"': '"aankomen은 zijn을 써요: is aangekomen"',
    '"lezen perfectum: hebben gelezen"': '"lezen 완료형: hebben gelezen"',
    'e.bridge("Work it out: answer with the numbers from page 3.")':
        'e.bridge("계산해 보세요: 3면 숫자로 답하세요.")',
    '"From 9 to 14 November is 5 days"': '"11월 9일부터 14일까지는 5일이에요"',
    '"From 9 to 15 November is 6 days"': '"11월 9일부터 15일까지는 6일이에요"',
    '"The Grave programme, 12:00–16:00, lasts 4 hours"': '"흐라버 프로그램 12:00–16:00은 4시간이에요"',
    '"Het diner is from 2009: 17 years ago in 2026"': '"『Het diner』는 2009년 작품: 2026년이면 17년 전이에요"',
    'p.band("SPORT", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · Oranje and the Nations League")':
        'p.band("SPORT · 스포츠", "De Lucerna", "NIVEAU B1 · Oranje en de Nations League · 오라녜와 네이션스리그")',
    'f.gloss("de groepsfase = group stage · de kwartfinale = quarter-final · ongeslagen = unbeaten · de interland = international match · de stand = the table.")':
        'f.gloss("de groepsfase 조별 리그 · de kwartfinale 8강전 · ongeslagen 무패 · de interland 국가대표 경기 · de stand 순위표.")',
    '"OEFENINGEN · EXERCISES ON PAGE 4"': '"OEFENINGEN · 4면 연습"',
}
KO_MAP.update({
    'e.bridge("Read the article on page 4 and choose the right answer.")':
        'e.bridge("4면 기사를 읽고 정답을 고르세요.")',
    '"Netherlands–Greece, Friday 20:45, in Amsterdam"': '"네덜란드–그리스, 금요일 20:45, 암스테르담"',
    '"The Netherlands and Greece both have 8 points"': '"네덜란드와 그리스는 둘 다 승점 8점이에요"',
    '"The Netherlands scored more goals in the group (7 to 5)"': '"네덜란드는 조에서 더 많은 골을 넣었어요(7대 5)"',
    '"Germany–Netherlands, Monday, in Berlin"': '"독일–네덜란드, 월요일, 베를린"',
    '"Eredivisie matchday 13 is on 21–22 November"': '"에레디비시 13라운드는 11월 21–22일이에요"',
    'e.bridge("Fill in with the words from the box. Watch the verb forms.")':
        'e.bridge("상자 속 단어로 채우세요. 동사 형태에 주의하세요.")',
    '"groepsfase = group stage"': '"groepsfase = 조별 리그"',
    '"kwartfinale plural: kwartfinales"': '"kwartfinale 복수형: kwartfinales"',
    '"ongeslagen = unbeaten"': '"ongeslagen = 무패"',
    '"stand = the table"': '"stand = 순위표"',
    '"interland = international match"': '"interland = 국가대표 경기"',
    'e.bridge("Complete with the past tense or the perfect tense.")':
        'e.bridge("과거형이나 완료형으로 채우세요.")',
    '"spelen past tense: speelde"': '"spelen 과거형: speelde"',
    '"winnen past tense: won"': '"winnen 과거형: won"',
    '"maken past tense: maakte"': '"maken 과거형: maakte"',
    '"komen perfectum takes zijn"': '"komen 완료형은 zijn을 써요"',
    '"True: Netherlands–Greece, Friday 20:45"': '"참: 네덜란드–그리스, 금요일 20:45"',
    '"False: Serbia are bottom with 0 points"': '"거짓: 세르비아는 승점 0점으로 최하위예요"',
    '"False: Eredivisie matchday 13 is on 21–22 November"': '"거짓: 에레디비시 13라운드는 11월 21–22일이에요"',
    '"True: PSV beat Willem II 7–0"': '"참: PSV가 빌럼 II를 7–0으로 이겼어요"',
    'p.band("JONGEREN · YOUNG PEOPLE", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · Robinson, the shoe and the wish list")':
        'p.band("JONGEREN · 청소년", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · 로빈슨, 신발과 소원 목록")',
    " (watch on RTL 4, Sunday 20:00)": " (일요일 20:00에 RTL 4에서 봐요)",
    " (watch the trials: points are won there)": " (트라이얼을 봐요: 점수는 거기서 결정돼요)",
    " (guess with friends who stays longest)": " (친구들과 누가 가장 오래 남을지 맞춰 봐요)",
    " (then put out your shoe, wish list inside)": " (그다음에는 소원 목록을 넣은 신발을 내놓아요)",
    'f.gloss("het verlanglijstje = wish list · de verslaggever = reporter · de proef = trial, challenge · stemmen = to vote · de aflevering = episode.")':
        'f.gloss("het verlanglijstje 소원 목록 · de verslaggever 리포터 · de proef 트라이얼, 도전 · stemmen 투표하다 · de aflevering 회차.")',
    '"On Sunday, do you watch Expeditie Robinson, or would you rather put out your shoe with a wish list? Write two sentences in Dutch and send them in."':
        '"일요일에는 Expeditie Robinson을 봐요, 아니면 소원 목록을 넣은 신발을 내놓을래요? 네덜란드어로 두 문장을 써서 보내 주세요."',
    '"EN JIJ? · AND YOU?"': '"EN JIJ? · 여러분은요?"',
    '"OEFENINGEN · EXERCISES ON PAGE 5"': '"OEFENINGEN · 5면 연습"',
    'e.bridge("Read the article on page 5 and choose the right answer.")':
        'e.bridge("5면 기사를 읽고 정답을 고르세요.")',
    '"Robinson is on every Sunday at 20:00 on RTL 4"': '"로빈슨은 매주 일요일 20:00에 RTL 4에서 방송해요"',
    '"19 contestants"': '"참가자 19명"',
    '"The show is filmed on a desert island in Malaysia"': '"이 프로그램은 말레이시아의 무인도에서 촬영해요"',
    '"The contestants spend 34 days on the island"': '"참가자들은 섬에서 34일을 보내요"',
    '"A wish list goes in the shoe"': '"소원 목록은 신발 안에 들어가요"',
    '"verlanglijstje = wish list (het)"': '"verlanglijstje = 소원 목록 (het)"',
    '"verslaggever = reporter (de)"': '"verslaggever = 리포터 (de)"',
    '"proef = trial, challenge (de)"': '"proef = 트라이얼, 도전 (de)"',
    '"stemmen = to vote"': '"stemmen = 투표하다"',
    '"aflevering = episode"': '"aflevering = 회차"',
    '"kandidaat plural: kandidaten"': '"kandidaat 복수형: kandidaten"',
    'e.bridge("Use gaan + infinitive to talk about the future.")':
        'e.bridge("gaan + 부정사로 미래에 대해 말해 보세요.")',
    '"gaat winnen = will win (just a guess)"': '"gaat winnen = 이길 거예요(그냥 추측)"',
    '"wij → gaan + infinitive kijken"': '"wij → gaan + 부정사 kijken"',
    '"hij → gaat zetten"': '"hij → gaat zetten"',
    '"zij (plural) → gaan schrijven"': '"zij (복수) → gaan schrijven"',
    '"True: the show started on 1 November"': '"참: 이 프로그램은 11월 1일에 시작했어요"',
    '"False: the show is filmed in Malaysia"': '"거짓: 이 프로그램은 말레이시아에서 촬영해요"',
    '"False: the carrot in the shoe is for the horse"': '"거짓: 신발 속 당근은 말을 위한 거예요"',
    'p.band("VERDIEPING · IN DEPTH", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · St Martin\'s Day or Halloween?")':
        'p.band("VERDIEPING · 심층", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · 성 마르틴의 날이냐, 핼러윈이냐?")',
    'f.gloss("de traditie = tradition · griezelen = to scare, to spook · de belangstelling = interest · de achteruitgang = decline · de deskundige = expert.")':
        'f.gloss("de traditie 전통 · griezelen 무섭게 하다 · de belangstelling 관심 · de achteruitgang 쇠퇴 · de deskundige 전문가.")',
    '"Practice data: invented numbers for practice only, not a real survey. Question: what do you do around 11 November? (100 young people)"':
        '"연습용 데이터: 연습용으로 만든 숫자예요, 실제 조사가 아니에요. 질문: 11월 11일 즈음에 무엇을 해요? (청소년 100명)"',
    '"DE GRAFIEK · PRACTICE DATA"': '"DE GRAFIEK · 그래프(연습용 데이터)"',
    '"VOOR OF TEGEN? · FOR OR AGAINST?"': '"VOOR OF TEGEN? · 찬반 토론"',
    '"OEFENINGEN · EXERCISES ON PAGE 6"': '"OEFENINGEN · 6면 연습"',
    'e.bridge("Answer from the chart on page 6 (practice data).")':
        'e.bridge("6면 그래프(연습용 데이터)에서 답하세요.")',
    '"40 young people walk with a lantern"': '"청소년 40명이 등롱을 들고 걸어요"',
    '"25 celebrate Halloween"': '"25명이 핼러윈을 기념해요"',
    '"40 + 20 = 60"': '"40 + 20 = 60"',
    '"15 stay at home"': '"15명은 집에 있어요"',
    '"The chart counts 100 people: 40+25+20+15"': '"그래프는 100명을 세요: 40+25+20+15"',
    'e.bridge("Read the article on page 6 and choose the right answer.")':
        'e.bridge("6면 기사를 읽고 정답을 고르세요.")',
    '"In 2025, 26% of Dutch people celebrated Halloween"': '"2025년에는 네덜란드 사람의 26%가 핼러윈을 기념했어요"',
    '"The two surveys use different definitions, so they cannot be compared directly"':
        '"두 조사는 정의가 달라서 직접 비교할 수 없어요"',
    '"Interest in St Martin\'s Day increased (Stengs, 2025)"': '"성 마르틴의 날에 대한 관심이 늘었어요(Stengs, 2025년)"',
    '"Halloween is about spooking; St Martin\'s Day is about sharing"': '"핼러윈은 무섭게 하는 것이고, 성 마르틴의 날은 나누는 것이에요"',
    '"A tradition lives on when people keep celebrating it"': '"전통은 사람들이 계속 기념할 때 살아남아요"',
    'e.bridge("Put the words in the right order to make sentences.")':
        'e.bridge("단어를 올바른 순서로 배열해 문장을 만드세요.")',
    '"traditie = tradition (de)"': '"traditie = 전통 (de)"',
    '"griezelen = to scare, to spook"': '"griezelen = 무섭게 하다"',
    '"belangstelling = interest (de)"': '"belangstelling = 관심 (de)"',
    '"achteruitgang = decline (de)"': '"achteruitgang = 쇠퇴 (de)"',
    '"Subject + verb + complement + place"': '"주어·동사·보어·장소"',
    '"Subject + verb + manner + place"': '"주어·동사·양태·장소"',
    '"The als-clause comes last"': '"als 절은 마지막에 와요"',
    '"kiezen + hoeft niet + explanation"': '"kiezen + hoeft niet + 설명"',
    'p.band("TAAL · LANGUAGE", "De Lucerna", "Language focus · Drie niveaus, drie gereedschappen · Three levels, three tools")':
        'p.band("TAAL · 언어", "De Lucerna", "언어에 집중 · Drie niveaus, drie gereedschappen · 세 단계, 세 가지 도구")',
    'a.bridge("de stoomboot = steamboat; de intocht = the festive arrival; de schoen zetten = to put out your shoe; de lampion = lantern.")':
        'a.bridge("de stoomboot 증기선; de intocht 축제 도착; de schoen zetten 신발 내놓기; de lampion 등롱.")',
    '"de stoomboot = steamboat"': '"de stoomboot = 증기선"',
    '"The intocht is Sinterklaas\'s festive arrival"': '"intocht는 신터클라스의 축제 도착이에요"',
    '"lampion = lantern"': '"lampion = 등롱"',
    'b.bridge("schoentje = little shoe; lichtje = little light; cadeautje = little present. -je means small and affectionate.")':
        'b.bridge("schoentje 작은 신발; lichtje 작은 불빛; cadeautje 작은 선물. -je는 작고 애정 어린 뜻이에요.")',
    '"schoen + -tje: schoentje"': '"schoen + -tje: schoentje"',
    '"licht + -je: lichtje"': '"licht + -je: lichtje"',
    '"cadeau + -tje: cadeautje"': '"cadeau + -tje: cadeautje"',
    '"-je means small and affectionate, not always really small"':
        '"-je는 작고 애정 어린 뜻이에요, 항상 실제로 작은 것은 아니에요"',
    'c.bridge("Als… = If… / When…; als het donker wordt = when it gets dark; als Sinterklaas komt = when Sinterklaas comes.")':
        'c.bridge("Als… = 만약… / ~할 때; als het donker wordt = 어두워지면; als Sinterklaas komt = 신터클라스가 오면.")',
    '"Als… = If… / When…"': '"Als… = 만약… / ~할 때"',
    '"An als-clause is a condition, not a question"': '"als 절은 조건이지, 질문이 아니에요"',
    '"The verb comes first in the main clause: gaat de lampion aan"':
        '"주절에서는 동사가 먼저 와요: gaat de lampion aan"',
    '"Als Oranje wint… = If Oranje win…"': '"Als Oranje wint… = 오라녜가 이기면…"',
    '"PAS OP! · ERROR CLINIC"': '"PAS OP! · 실수 클리닉"',
    '"Sinterklaas is a name, so it takes no article."': '"Sinterklaas는 이름이라서 관사가 없어요."',
    '"mijn schoen = my shoe."': '"mijn schoen = 내 신발이에요."',
    '"Fixed phrase: langs de deuren."': '"고정 표현: langs de deuren."',
    '"Verb first after the als-clause: ben ik blij."': '"als 절 뒤에서는 동사가 먼저 와요: ben ik blij."',
    '"HET WOORD · WORD OF THE WEEK"': '"HET WOORD · 이번 주 단어"',
    '"schoen zetten = to put out your shoe, with a carrot and a drawing inside."':
        '"schoen zetten = 신발 내놓기: 당근과 그림을 넣어 두는 거예요."',
})
KO_MAP.update({
    'dt_en = "No real letters or best page-8 texts at press time — example; promise to VOL.4."':
        'dt_zh = "실제 편지와 최고 작문이 없어 예시를 싣고, 약속은 VOL.4로 이어져요."',
    'len(wrap(dt_en, "sans", False, 20, CW - 44))': 'len(wrap(dt_zh, "sans", False, 20, CW - 44))',
    'p.para(bx + 22, yy3 + 20, dt_en, 20, "sans", False, GREY, CW - 44, 1.42) + 10':
        'p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10',
    '"Editors\' example — send yours for VOL.4!"':
        '"편집부 예시예요. 여러분의 편지와 작문을 보내 주세요!"',
    '"ZINNEN VAN DE WEEK · PHRASES OF THE WEEK (VERBATIM FROM THIS ISSUE)"':
        '"ZINNEN VAN DE WEEK · 이번 주 금문장(본문에서 그대로 가져왔어요)"',
    '"On Monday 9 November, the Sinterklaas news starts on television."':
        '"11월 9일 월요일에 신터클라스 뉴스가 TV에서 시작해요."',
    '"One day later, Sunday 15 November: the Amsterdam arrival, 88th edition."':
        '"그다음 날인 11월 15일 일요일: 암스테르담 도착, 88회째예요."',
    '"St Martin\'s Day is the festival of sharing: sharing light, food and attention."':
        '"성 마르틴의 날은 나눔의 축제예요: 빛과 음식과 관심을 나누어요."',
    '"On Saturday 14 November, Sinterklaas officially arrives in Grave."':
        '"11월 14일 토요일에 신터클라스는 흐라버에 공식적으로 도착해요."',
    '"On Friday 13 November, Oranje play Greece at home."':
        '"11월 13일 금요일에 오라녜는 홈에서 그리스와 경기를 해요."',
    '"Every Sunday at 20:00, Expeditie Robinson is on RTL 4."':
        '"매주 일요일 20:00에 Expeditie Robinson은 RTL 4에서 방송해요."',
    '"St Martin\'s Day is an old tradition in the Netherlands."':
        '"성 마르틴의 날은 네덜란드의 오래된 전통이에요."',
    '"A tradition lives on when people keep celebrating it."':
        '"전통은 사람들이 계속 기념할 때 살아남아요."',
    '"VOLGENDE WEEK · NEXT WEEK (VOL.4)"': '"VOLGENDE WEEK · 다음 호 예고 (VOL.4)"',
    'p.band("TOETS EN ANTWOORDEN · TEST AND ANSWERS", "De Lucerna", "Page 8 · De grote toets van de week + alle antwoorden")':
        'p.band("TOETS EN ANTWOORDEN · 시험과 정답", "De Lucerna", "8면 · De grote toets van de week + alle antwoorden")',
    '"The Sinterklaas news is on every day at 18:00."': '"신터클라스 뉴스는 매일 18:00에 방송해요."',
    '"The national arrival is in Grave"': '"전국 도착은 흐라버에서 열려요"',
    '"The Sinterklaas news starts on 9 November"': '"신터클라스 뉴스는 11월 9일에 시작해요"',
    '"The Amsterdam arrival is the 88th edition"': '"암스테르담 도착은 88회째예요"',
    '"Netherlands–Greece kicks off at 20:45"': '"네덜란드–그리스 경기는 20:45에 시작해요"',
    '"St Martin\'s Day is on 11 November"': '"성 마르틴의 날은 11월 11일이에요"',
    '"Robinson is on RTL 4"': '"로빈슨은 RTL 4에서 방송해요"',
    '"St Martin\'s Day is the festival of sharing."': '"성 마르틴의 날은 나눔의 축제예요."',
    '"The Netherlands and Greece both have 8 points"': '"네덜란드와 그리스는 둘 다 승점 8점이에요"',
    '"Germany–Netherlands, Monday, in Berlin"': '"독일–네덜란드, 월요일, 베를린"',
    '"St Martin\'s Day is the festival of sharing"': '"성 마르틴의 날은 나눔의 축제예요"',
    '"A tradition lives on when people keep celebrating it"': '"전통은 사람들이 계속 기념할 때 살아남아요"',
    '"Subject + verb + time"': '"주어·동사·시간"',
    '"Subject + verb + object + place"': '"주어·동사·목적어·장소"',
    '"Subject + verb + time + opponent"': '"주어 + 동사 + 시간 + 상대"',
    '"Subject + verb + manner + place"': '"주어 + 동사 + 양태 + 장소"',
    '"Watch the ordinal 88e"': '"서수 88e에 주의하세요"',
    '"schoen zetten is a fixed expression"': '"schoen zetten은 고정 표현이에요"',
    '["journaal = news programme b", "intocht = the festive arrival d", "lampion = lantern a", "delen = to share c"]':
        '["journaal = 뉴스 프로그램 b", "intocht = 축제 도착 d", "lampion = 등롱 a", "delen = 나누다 c"]',
    '"schoen = shoe"': '"schoen = 신발"',
    '"wortel = carrot (for the horse)"': '"wortel = 당근 (말을 위한 거예요)"',
    '"verlanglijstje = wish list"': '"verlanglijstje = 소원 목록"',
    '"cadeautje = little present"': '"cadeautje = 작은 선물"',
    '"18:00 = the Sinterklaas news time"': '"18:00 = 신터클라스 뉴스 시간"',
    '"Sanne lives in Utrecht"': '"산너는 위트레흐트에 살아요"',
    '"On Wednesday she joins the St Martin\'s parade"': '"수요일에 그녀는 성 마르틴 행렬에 참여해요"',
    '"She puts a carrot and a wish list in her shoe"': '"그녀는 신발에 당근과 소원 목록을 넣어요"',
    '"She watches the Sinterklaas news every day at 18:00"': '"그녀는 매일 18:00에 신터클라스 뉴스를 봐요"',
    '"Het diner was published in 2009"': '"『Het diner』는 2009년에 출판됐어요"',
    '"Sinterklaas receives the key to the city at the Maritime Museum"':
        '"신터클라스는 해양 박물관에서 도시의 열쇠를 받아요"',
    '"Pakjesavond is on Saturday 5 December"': '"팍예스아폰트는 12월 5일 토요일이에요"',
    '"Grave lies on the river Maas"': '"흐라버는 마스 강가에 있어요"',
    '"Compare with the page 3 article"': '"3면 기사와 비교해 보세요"',
    '"Original sentence from page 2 · delen = to share"': '"2면 원문 · delen = 나누다"',
    '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Translate into English"':
        '"Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="한국어로 번역"',
    '"Sint-Maarten is het feest van het delen. → ___", instr="Translate into English"':
        '"Sint-Maarten is het feest van het delen. → ___", instr="한국어로 번역"',
    '"The arrival in Amsterdam is the 88th edition. → ___", instr="Translate into Dutch"':
        '"암스테르담 도착은 88회째예요. → ___", instr="네덜란드어로 번역"',
    '"I put out my shoe, with a wish list inside. → ___", instr="Translate into Dutch"':
        '"소원 목록을 넣은 신발을 내놓아요. → ___", instr="네덜란드어로 번역"',
    '"(open task, model text below)"': '"(열린 문제, 모범 답안은 아래에 있어요)"',
    "Writing task (no single answer); model text ({NWORDS} words) below.":
        "쓰기 문제예요(정답이 하나만 있는 것은 아니에요). 모범 답안은 아래에 있어요({NWORDS}단어).",
    "See the model text in section H ({NWORDS} words)":
        "모범 답안은 H 부분에서 보세요({NWORDS}단어)",
    '"ANTWOORDEN · ANSWER KEY — grouped by page: find your number"':
        '"ANTWOORDEN · 정답 모음 — 면별로 찾으세요"',
    '"Every answer has a short note in English · ✓ marks the writing task"':
        '"모든 정답에는 짧은 한국어 설명이 있어요 · ✓는 쓰기 문제예요"',
    '"schoen zetten = to put out your shoe"': '"schoen zetten = 신발 내놓기"',
    '"Netherlands–Greece kicks off at 20:45 on Friday"': '"네덜란드–그리스 경기는 금요일 20:45에 시작해요"',
    '"The Sinterklaas news is on every day at 18:00"': '"신터클라스 뉴스는 매일 18:00에 방송해요"',
    '"The Sinterklaas news starts on Monday 9 November."': '"신터클라스 뉴스는 11월 9일 월요일에 시작해요."',
    '"hij → gaat zetten"': '"hij → gaat zetten"',
    '"40 + 20 = 60"': '"40 + 20 = 60"',
})

# pairs that need special handling
SKIP_IDX = {0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11}
BADGE_IDX = 14
# pair 7: identity rep on the post-loop 쓰기 check form
# pairs 8, 9, 10: P8 sizes stay at CORE values; only the separator TEXT
#   changes (PAGINA -> 제 N 면), handled by the furniture rep below
# pair 11: svglib — skipped; KO svglib is byte-identical to the core svglib
# pair 13: subtitle — Korean topic words via map lookup

hdr = '''# -*- coding: utf-8 -*-
"""One-off fan-out transform: W46 NL core (Chinese explanations) -> NL x KO.
Line-literal replacements only, each asserted. Run once from this dir.
Dutch target text, keys (except re-aimed 137/138), facts, images: untouched.
Furniture per the W43/W45 NL x KO registry: badge REPLACES strapline y=372
(19.5pt bold BRICK), footer 네덜란드어 주간지, gloss prefix 해설 — (added
by gloss() itself), P8 sizes at CORE values with '— 제 N 면 —' separators.
Type tokens TRANSLATED to Korean; instr words localised; per-direction
한국어로 번역/네덜란드어로 번역. bridge() KEPT. P7 bridges use ';',
glosses ' · ', P8 notes ' = ' with HALF-WIDTH parentheses. Disclosure
variable KEEPS the name dt_zh. svglib unchanged (SC face renders Hangul).
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
    rep(f, "weekly-report-w46-nl-core/svg", "weekly-report-w46-nl-ko/svg")

# ---------- types + instr (instrs FIRST, cloze before plain choice) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep_opt(f, 'instr="填空"', 'instr="빈칸 채우기"')
    rep_opt(f, 'instr="判断"', 'instr="참 / 거짓"')
    rep_opt(f, 'instr="造句"', 'instr="문장 만들기"')
    rep_opt(f, 'instr="写作"', 'instr="쓰기"')
    rep_opt(f, 'instr="翻译"', 'instr="번역"')
    rep_opt(f, "完形单选", "객관식")
    rep_opt(f, "完成句子", "문장 완성")
    rep_opt(f, "词汇配对", "단어 짝짓기")
    rep_opt(f, "判断对错", "참/거짓 판단")
    rep_opt(f, "单选", "객관식")
    rep_opt(f, "造句", "문장 만들기")
    rep_opt(f, "翻译", "번역")
    rep_opt(f, "写作", "쓰기")

# ---------- furniture ----------
rep("render.py", "weekly-report-w46-nl-core", "weekly-report-w46-nl-ko")
rep("render.py", "De-Lucerna-VOL3.pdf", "De-Lucerna-VOL3-KO.pdf")
rep_opt("render.py", "Render the NL weekly VOL.3", "Render the NL x KO weekly VOL.3")
rep_opt("run.py", "Run the IT weekly", "Run the NL x KO weekly")
rep("bslib4.py", "De Lucerna · 荷兰语周报 VOL.3 · LUCERNA DUTCH WEEKLY",
     "De Lucerna · 네덜란드어 주간지 VOL.3 · 텍스트는 네덜란드어 · 해설은 한국어")
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"제 {n} 면 / 총 {total} 면"')
rep("bslib4.py", "译注｜", "해설 — ")
rep("content8.py", 'af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
     'af.para(f"— 제 {pg} 면 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)')

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
        form = 'if e_["type"] == "쓰기":'
        out.append((f, form, form))
        continue
    if j == BADGE_IDX:
        badge = ('p.text(975, 372, "네덜란드어 텍스트 · 한국어 해설 — '
                 '한국어 독자를 위한 판", 19.5, "sans", True, BRICK, anchor="middle")')
        out.append((f, old, badge))
        continue
    if "writing题" in old:
        old = old.replace("writing题", "쓰기题")
        out.append((f, old, KO_MAP[new]))
        continue
    if 'instr="Translate' in old:
        old = old.replace('instr="Translate into English"', 'instr="번역"')
        old = old.replace('instr="Translate into Dutch"', 'instr="번역"')
        old = old.replace('instr="Translate"', 'instr="번역"')
    if new in KO_MAP:
        out.append((f, old, KO_MAP[new]))
    elif len(new) > 1 and new.startswith('"') and new.endswith('"') and new[1:-1] in KO_MAP:
        out.append((f, old, '"' + KO_MAP[new[1:-1]] + '"'))
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
with open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/transform_ko.py", "w", encoding="utf-8") as fh:
    fh.write(hdr)
    for f, old, new in ded:
        fh.write(f"rep({f!r}, {old!r}, {new!r})\n")
    fh.write(tail)
print("wrote", len(ded), "reps")
