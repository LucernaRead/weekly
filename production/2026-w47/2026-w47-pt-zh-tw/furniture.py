# -*- coding: utf-8 -*-
"""Per-reader-language furniture for W47 PT fan-out.
footer / badge / subtitle values are the W46 pt-<lang> shipped strings
(VOL.3 -> VOL.4); tables.py furniture has no established column for
en/ja/ko/ru/zh-tw, so the W46 shipped artifact is the precedent.
"""
FURN = {
"en": {
  "footer": "VOL.4\u3000Text in Portuguese\u3000Explanations in English",
  "page_line": 'f"Page {n} of {total}"',
  "gloss": "Note | ",
  "badge372": "TEXT IN PORTUGUESE\u3000EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS",
  "sub330": "PORTUGUESE WEEKLY\u3000VOL.4\u3000CONSCIÊNCIA NEGRA\u3000GABARITO DO ENEM\u3000A FINAL DA COPA",
  "sub330_size": 32,
  "disc_var": "disc_en",
  "disc_text": "Editor's note: no real letters or best texts for VOL.3 had arrived — the example stands; the promise carries to VOL.5.",
  "p7_geo": {"letters_pad": 22, "fy_gap": 30, "quote_step": 76},
  "label_nospace": "Editor'sexample—notarealletter",
  "footer_joined": "A Lucerna VOL.4 Text in Portuguese Explanations in English",
  "page_fmt": "Page {i} of 8",
  "lang_name": "EN",
  "p8_keys_small": True,
  "model_bridge": "Writing task (no single correct answer); the model text ({NWORDS} words) is below.",
  "model_note": "See the model text in section H of this page ({NWORDS} words)",
  "textmd_header_title": "Portuguese Weekly VOL.4",
  "textmd_header_sub": "Week of 16–22 November 2026 · Texts in Portuguese · Explanations in English · Levels A2–B2 · 150 exercises",
  "textmd_extra": {
    "三天连休 · 11月20日周五 · 黑人意识日全国假日":
      "a three-day holiday · Friday 20 November · Black Consciousness Day, a national holiday",
    "Três dias, uma semana（三天连休，一周安排）: SEX 20 — o feriado começa（11月20日周五放假）· SÁB 21 — Palmeiras × Flamengo, às 16h30（周六 16:30 帕弗之战）· DOM 22 — o fim do feriadão（周日连休结束）· SEG 23 — tudo volta ao normal（周一恢复正常）.":
      "Três dias, uma semana (Three days off, one week planned): SEX 20 — o feriado começa (Friday 20 November, a holiday) · SÁB 21 — Palmeiras × Flamengo, às 16h30 (Saturday 16:30 the Palmeiras–Flamengo clash) · DOM 22 — o fim do feriadão (On Sunday the long weekend ends) · SEG 23 — tudo volta ao normal (On Monday everything goes back to normal).",
    "范文见本版 H 区（88 词）":
      "See the model text in section H of this page (88 words)",
  },
},
"de": {
  "footer": "PORTUGIESISCHE WOCHENZEITUNG VOL.4\u3000TEXT AUF PORTUGIESISCH\u3000ERKLÄRUNGEN AUF DEUTSCH",
  "page_line": 'f"Seite {n} von {total}"',
  "gloss": "HINWEIS · ",
  "badge372": "PORTUGIESISCHER TEXT\u3000DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER",
  "sub330": "PORTUGIESISCHE WOCHENZEITUNG\u3000VOL.4\u3000CONSCIÊNCIA NEGRA\u3000GABARITO DO ENEM\u3000A FINAL DA COPA",
  "sub330_size": 28,
  "disc_var": "disc_de",
  "disc_text": "Anmerkung der Redaktion: Bis zum Redaktionsschluss keine echten Briefe und besten Texte für VOL.3 — das Beispiel bleibt; das Versprechen gilt für VOL.5.",
  "p7_geo": {"letters_pad": 22, "fy_gap": 16, "quote_step": 76},
  "label_nospace": "BeispielderRedaktion—keinechterLeserbrief",
  "footer_joined": "A Lucerna PORTUGIESISCHE WOCHENZEITUNG VOL.4 TEXT AUF PORTUGIESISCH ERKLÄRUNGEN AUF DEUTSCH",
  "page_fmt": "Seite {i} von 8",
  "lang_name": "DE",
  "p8_keys_small": True,
  "model_bridge": "Schreibaufgabe (keine eindeutige Antwort); der Mustertext ({NWORDS} Wörter) steht unten.",
  "model_note": "Siehe den Mustertext in Abschnitt H auf dieser Seite ({NWORDS} Wörter)",
  "textmd_header_title": "Portugiesische Wochenzeitung VOL.4",
  "textmd_header_sub": "Woche vom 16.–22. November 2026 · Texte auf Portugiesisch · Erklärungen auf Deutsch · Niveaus A2–B2 · 150 Übungen",
  "textmd_extra": {
    "三天连休 · 11月20日周五 · 黑人意识日全国假日":
      "ein dreitägiges Feiertagswochenende · Freitag, 20. November · Tag des Schwarzen Bewusstseins, ein nationaler Feiertag",
    "Três dias, uma semana（三天连休，一周安排）: SEX 20 — o feriado começa（11月20日周五放假）· SÁB 21 — Palmeiras × Flamengo, às 16h30（周六 16:30 帕弗之战）· DOM 22 — o fim do feriadão（周日连休结束）· SEG 23 — tudo volta ao normal（周一恢复正常）.":
      "Três dias, uma semana (Drei freie Tage, eine Woche geplant): SEX 20 — o feriado começa (Freitag, 20. November, ein Feiertag) · SÁB 21 — Palmeiras × Flamengo, às 16h30 (Samstag 16:30, das Palmeiras–Flamengo-Duell) · DOM 22 — o fim do feriadão (Am Sonntag endet das lange Wochenende) · SEG 23 — tudo volta ao normal (Am Montag ist wieder alles normal).",
    "范文见本版 H 区（88 词）":
      "Siehe den Mustertext in Abschnitt H auf dieser Seite (88 Wörter)",
    "(verbatim from this issue)":
      "(wörtlich aus dieser Ausgabe)",
  },
},
"fr": {
  "footer": "HEBDOMADAIRE PORTUGAIS VOL.4\u3000TEXTE EN PORTUGAIS\u3000EXPLICATIONS EN FRANÇAIS",
  "page_line": 'f"Page {n} sur {total}"',
  "gloss": "Note — ",
  "badge372": "TEXTES EN PORTUGAIS\u3000EXPLICATIONS EN FRANÇAIS — L’ÉDITION POUR LES LECTEURS FRANCOPHONES",
  "sub330": "HEBDOMADAIRE PORTUGAIS\u3000VOL.4\u3000CONSCIÊNCIA NEGRA\u3000GABARITO DO ENEM\u3000A FINAL DA COPA",
  "sub330_size": 30,
  "disc_var": "disc_fr",
  "disc_text": "Note de la rédaction : ni lettres ni meilleurs textes du VOL.3 avant le bouclage — l'exemple reste, la promesse passe au VOL.5.",
  "p7_geo": {"letters_pad": 22, "fy_gap": 16, "quote_step": 80},
  "label_nospace": "Exempledelarédaction—pasunevraielettre",
  "footer_joined": "A Lucerna HEBDOMADAIRE PORTUGAIS VOL.4 TEXTE EN PORTUGAIS EXPLICATIONS EN FRANÇAIS",
  "page_fmt": "Page {i} sur 8",
  "lang_name": "FR",
  "p8_keys_small": True,
  "model_bridge": "Exercice d'écriture (pas de réponse unique) ; le texte modèle ({NWORDS} mots) est ci-dessous.",
  "model_note": "Voir le texte modèle dans la section H de cette page ({NWORDS} mots)",
  "textmd_header_title": "Hebdomadaire Portugais VOL.4",
  "textmd_header_sub": "Semaine du 16 au 22 novembre 2026 · Textes en portugais · Explications en français · Niveaux A2–B2 · 150 exercices",
  "textmd_extra": {
    "三天连休 · 11月20日周五 · 黑人意识日全国假日":
      "un week-end prolongé de trois jours · vendredi 20 novembre · le Jour de la Conscience noire, un jour férié national",
    "Três dias, uma semana（三天连休，一周安排）: SEX 20 — o feriado começa（11月20日周五放假）· SÁB 21 — Palmeiras × Flamengo, às 16h30（周六 16:30 帕弗之战）· DOM 22 — o fim do feriadão（周日连休结束）· SEG 23 — tudo volta ao normal（周一恢复正常）.":
      "Três dias, uma semana (Trois jours de congé, une semaine planifiée) : SEX 20 — o feriado começa (vendredi 20 novembre, jour férié) · SÁB 21 — Palmeiras × Flamengo, às 16h30 (samedi 16h30, le choc Palmeiras–Flamengo) · DOM 22 — o fim do feriadão (le dimanche, le long week-end se termine) · SEG 23 — tudo volta ao normal (le lundi, tout redevient normal).",
    "范文见本版 H 区（88 词）":
      "Voir le texte modèle dans la section H de cette page (88 mots)",
    "(verbatim from this issue)":
      "(extraites mot pour mot de ce numéro)",
  },
},
"es": {
  "footer": "SEMANARIO PORTUGUÉS VOL.4\u3000TEXTO EN PORTUGUÉS\u3000EXPLICACIONES EN ESPAÑOL",
  "page_line": 'f"Página {n} de {total}"',
  "gloss": "Nota — ",
  "badge372": "TEXTOS EN PORTUGUÉS\u3000EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES",
  "sub330": "SEMANARIO PORTUGUÉS\u3000VOL.4\u3000CONSCIÊNCIA NEGRA\u3000GABARITO DO ENEM\u3000A FINAL DA COPA",
  "sub330_size": 30,
  "disc_var": "disc_es",
  "disc_text": "Nota de la redacción: sin cartas reales ni mejores textos del VOL.3 — queda el ejemplo y la promesa pasa al VOL.5.",
  "p7_geo": {"letters_pad": 22, "fy_gap": 16, "quote_step": 80},
  "label_nospace": "Ejemplodelaredacción,nounacartareal",
  "footer_joined": "A Lucerna SEMANARIO PORTUGUÉS VOL.4 TEXTO EN PORTUGUÉS EXPLICACIONES EN ESPAÑOL",
  "page_fmt": "Página {i} de 8",
  "lang_name": "ES",
  "p8_keys_small": True,
  "model_bridge": "Ejercicio de escritura (sin respuesta única); el texto modelo ({NWORDS} palabras) está abajo.",
  "model_note": "Ver el texto modelo en la sección H de esta página ({NWORDS} palabras)",
  "textmd_header_title": "Semanario Portugués VOL.4",
  "textmd_header_sub": "Semana del 16 al 22 de noviembre de 2026 · Textos en portugués · Explicaciones en español · Niveles A2–B2 · 150 ejercicios",
  "textmd_extra": {
    "三天连休 · 11月20日周五 · 黑人意识日全国假日":
      "un puente de tres días · viernes 20 de noviembre · el Día de la Conciencia Negra, festivo nacional",
    "Três dias, uma semana（三天连休，一周安排）: SEX 20 — o feriado começa（11月20日周五放假）· SÁB 21 — Palmeiras × Flamengo, às 16h30（周六 16:30 帕弗之战）· DOM 22 — o fim do feriadão（周日连休结束）· SEG 23 — tudo volta ao normal（周一恢复正常）.":
      "Três dias, uma semana (Tres días de fiesta, una semana planificada): SEX 20 — o feriado começa (viernes 20 de noviembre, fiesta) · SÁB 21 — Palmeiras × Flamengo, às 16h30 (sábado 16:30, el clásico Palmeiras–Flamengo) · DOM 22 — o fim do feriadão (el domingo termina el puente) · SEG 23 — tudo volta ao normal (el lunes todo vuelve a la normalidad).",
    "范文见本版 H 区（88 词）":
      "Ver el texto modelo en la sección H de esta página (88 palabras)",
    "(verbatim from this issue)":
      "(citadas palabra por palabra de este número)",
  },
},
"it": {
  "footer": "SETTIMANALE PORTOGHESE VOL.4\u3000TESTI IN PORTOGHESE\u3000SPIEGAZIONI IN ITALIANO",
  "page_line": 'f"Pagina {n} di {total}"',
  "gloss": "Nota — ",
  "badge372": "TESTI IN PORTOGHESE\u3000SPIEGAZIONI IN ITALIANO — L’EDIZIONE PER I LETTORI ITALIANI",
  "sub330": "SETTIMANALE PORTOGHESE\u3000VOL.4\u3000CONSCIÊNCIA NEGRA\u3000GABARITO DO ENEM\u3000A FINAL DA COPA",
  "sub330_size": 30,
  "disc_var": "disc_it",
  "disc_text": "Nota della redazione: né lettere vere né migliori testi del VOL.3 — resta l'esempio e la promessa passa al VOL.5.",
  "p7_geo": {"letters_pad": 22, "fy_gap": 16, "quote_step": 80},
  "label_nospace": "Esempiodellaredazione—nonunaveraletter",
  "footer_joined": "A Lucerna SETTIMANALE PORTOGHESE VOL.4 TESTI IN PORTOGHESE SPIEGAZIONI IN ITALIANO",
  "page_fmt": "Pagina {i} di 8",
  "lang_name": "IT",
  "p8_keys_small": True,
  "model_bridge": "Esercizio di scrittura (senza risposta unica); il testo modello ({NWORDS} parole) è sotto.",
  "model_note": "Vedi il testo modello nella sezione H di questa pagina ({NWORDS} parole)",
  "textmd_header_title": "Settimanale Portoghese VOL.4",
  "textmd_header_sub": "Settimana dal 16 al 22 novembre 2026 · Testi in portoghese · Spiegazioni in italiano · Livelli A2–B2 · 150 esercizi",
  "textmd_extra": {
    "三天连休 · 11月20日周五 · 黑人意识日全国假日":
      "un ponte di tre giorni · venerdì 20 novembre · il Giorno della Coscienza Nera, festa nazionale",
    "Três dias, uma semana（三天连休，一周安排）: SEX 20 — o feriado começa（11月20日周五放假）· SÁB 21 — Palmeiras × Flamengo, às 16h30（周六 16:30 帕弗之战）· DOM 22 — o fim do feriadão（周日连休结束）· SEG 23 — tudo volta ao normal（周一恢复正常）.":
      "Três dias, uma semana (Tre giorni di festa, una settimana organizzata): SEX 20 — o feriado começa (venerdì 20 novembre, festa) · SÁB 21 — Palmeiras × Flamengo, às 16h30 (sabato 16:30, il classico Palmeiras–Flamengo) · DOM 22 — o fim do feriadão (domenica finisce il ponte) · SEG 23 — tudo volta ao normal (lunedì tutto torna alla normalità).",
    "范文见本版 H 区（88 词）":
      "Vedi il testo modello nella sezione H di questa pagina (88 parole)",
    "(verbatim from this issue)":
      "(citate parola per parola da questo numero)",
  },
},
"nl": {
  "footer": "PORTUGEES WEEKBLAD VOL.4\u3000TEKSTEN IN HET PORTUGEES\u3000UITLEG IN HET NEDERLANDS",
  "page_line": 'f"Pagina {n} van {total}"',
  "gloss": "Uitleg — ",
  "badge372": "TEKSTEN IN HET PORTUGEES\u3000UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS",
  "sub330": "PORTUGEES WEEKBLAD\u3000VOL.4\u3000CONSCIÊNCIA NEGRA\u3000GABARITO DO ENEM\u3000A FINAL DA COPA",
  "sub330_size": 32,
  "disc_var": "disc_nl",
  "disc_text": "Opmerking van de redactie: geen echte brieven of beste teksten uit VOL.3 — het voorbeeld blijft, de belofte naar VOL.5.",
  "p7_geo": {"letters_pad": 22, "fy_gap": 16, "quote_step": 80},
  "label_nospace": "Voorbeeldvanderedactie—geenechtebrief",
  "footer_joined": "A Lucerna PORTUGEES WEEKBLAD VOL.4 TEKSTEN IN HET PORTUGEES UITLEG IN HET NEDERLANDS",
  "page_fmt": "Pagina {i} van 8",
  "lang_name": "NL",
  "p8_keys_small": True,
  "model_bridge": "Schrijfopdracht; de modeltekst ({NWORDS} woorden) staat hieronder.",
  "model_note": "Zie de modeltekst in onderdeel H van deze pagina ({NWORDS} woorden)",
  "textmd_header_title": "Portugees Weekblad VOL.4",
  "textmd_header_sub": "Week van 16 tot 22 november 2026 · Teksten in het Portugees · Uitleg in het Nederlands · Niveaus A2–B2 · 150 oefeningen",
  "textmd_extra": {
    "三天连休 · 11月20日周五 · 黑人意识日全国假日":
      "een lang weekend van drie dagen · vrijdag 20 november · de Dag van het Zwarte Bewustzijn, nationale feestdag",
    "Três dias, uma semana（三天连休，一周安排）: SEX 20 — o feriado começa（11月20日周五放假）· SÁB 21 — Palmeiras × Flamengo, às 16h30（周六 16:30 帕弗之战）· DOM 22 — o fim do feriadão（周日连休结束）· SEG 23 — tudo volta ao normal（周一恢复正常）.":
      "Três dias, uma semana (Drie vrije dagen, een week gepland): SEX 20 — o feriado começa (vrijdag 20 november, feestdag) · SÁB 21 — Palmeiras × Flamengo, às 16h30 (zaterdag 16:30, de kraker Palmeiras–Flamengo) · DOM 22 — o fim do feriadão (zondag eindigt het lange weekend) · SEG 23 — tudo volta ao normal (maandag wordt alles weer normaal).",
    "范文见本版 H 区（88 词）":
      "Zie de modeltekst in onderdeel H van deze pagina (88 woorden)",
    "(verbatim from this issue)":
      "(letterlijk uit dit nummer)",
  },
},
"ru": {
  "footer": "ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.4\u3000ТЕКСТЫ НА ПОРТУГАЛЬСКОМ\u3000ОБЪЯСНЕНИЯ НА РУССКОМ",
  "page_line": 'f"Страница {n} из {total}"',
  "gloss": "Пояснение — ",
  "badge372": "ТЕКСТЫ НА ПОРТУГАЛЬСКОМ\u3000ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ",
  "sub330": "ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК\u3000VOL.4\u3000CONSCIÊNCIA NEGRA\u3000GABARITO DO ENEM\u3000A FINAL DA COPA",
  "sub330_size": 28,
  "disc_var": "disc_ru",
  "disc_text": "Примечание: настоящих писем и лучших текстов из VOL.3 не пришло. Пример остаётся, обещание — в VOL.5.",
  "p7_geo": {"letters_pad": 22, "fy_gap": 16, "quote_step": 80},
  "label_nospace": "Примерредакции—ненастоящееписьмо",
  "footer_joined": "A Lucerna ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.4 ТЕКСТЫ НА ПОРТУГАЛЬСКОМ ОБЪЯСНЕНИЯ НА РУССКОМ",
  "page_fmt": "Страница {i} из 8",
  "lang_name": "RU",
  "p8_keys_small": True,
  "model_bridge": "Письменное задание; образец текста ({NWORDS} слов) — ниже.",
  "model_note": "Смотри образец текста в разделе H ({NWORDS} слов)",
  "textmd_header_title": "Португальский еженедельник VOL.4",
  "textmd_header_sub": "Неделя 16–22 ноября 2026 года · Тексты на португальском · Объяснения на русском · Уровни A2–B2 · 150 упражнений",
  "textmd_extra": {
    "三天连休 · 11月20日周五 · 黑人意识日全国假日":
      "трёхдневные выходные · пятница, 20 ноября · День чёрного сознания, национальный праздник",
    "Três dias, uma semana（三天连休，一周安排）: SEX 20 — o feriado começa（11月20日周五放假）· SÁB 21 — Palmeiras × Flamengo, às 16h30（周六 16:30 帕弗之战）· DOM 22 — o fim do feriadão（周日连休结束）· SEG 23 — tudo volta ao normal（周一恢复正常）.":
      "Três dias, uma semana (Три выходных дня, одна спланированная неделя): SEX 20 — o feriado começa (пятница, 20 ноября, выходной) · SÁB 21 — Palmeiras × Flamengo, às 16h30 (суббота, 16:30, дерби Палмейрас–Фламенго) · DOM 22 — o fim do feriadão (в воскресенье длинные выходные заканчиваются) · SEG 23 — tudo volta ao normal (в понедельник всё возвращается в норму).",
    "范文见本版 H 区（88 词）":
      "Смотри образец текста в разделе H (88 слов)",
    "(verbatim from this issue)":
      "(дословно из этого номера)",
  },
},
"ja": {
  "footer": "ポルトガル語週刊 VOL.4\u3000本文はポルトガル語\u3000解説は日本語",
  "page_line": 'f"{n}ページ（全{total}ページ）"',
  "gloss": "解説 — ",
  "badge372": "ポルトガル語テキスト\u3000日本語の解説 — 日本語読者のための版",
  "sub330": "ポルトガル語週刊\u3000VOL.4\u3000CONSCIÊNCIA NEGRA\u3000GABARITO DO ENEM\u3000A FINAL DA COPA",
  "sub330_size": 34,
  "disc_var": "disc_ja",
  "disc_text": "編集部注：VOL.3 で約束した実際の手紙と最優秀作文は締切までに届かず、本号は例文を掲載し、約束は VOL.5 へ延期します。",
  "p7_geo": {"letters_pad": 22, "fy_gap": 16, "quote_step": 80},
  "label_nospace": "編集部の作例です",
  "footer_joined": "A Lucerna ポルトガル語週刊 VOL.4 本文はポルトガル語 解説は日本語",
  "page_fmt": "{i}ページ（全8ページ）",
  "lang_name": "JA",
  "p8_keys_small": False,
  "model_bridge": "作文の課題（正解は1つではありません）。模範文（{NWORDS}語）は下です。",
  "model_note": "模範文はこのページのHの部分にあります（{NWORDS}語）",
  "textmd_header_title": "ポルトガル語週刊 VOL.4",
  "textmd_header_sub": "2026年11月16日〜22日 · 本文はポルトガル語 · 解説は日本語 · レベルA2–B2 · 練習問題150問",
  "textmd_extra": {
    "三天连休 · 11月20日周五 · 黑人意识日全国假日":
      "3連休 · 11月20日金曜日 · 黒人意識の日、全国の祝日",
    "Três dias, uma semana（三天连休，一周安排）: SEX 20 — o feriado começa（11月20日周五放假）· SÁB 21 — Palmeiras × Flamengo, às 16h30（周六 16:30 帕弗之战）· DOM 22 — o fim do feriadão（周日连休结束）· SEG 23 — tudo volta ao normal（周一恢复正常）.":
      "Três dias, uma semana（3連休、1週間の計画）: SEX 20 — o feriado começa（11月20日金曜日、祝日）· SÁB 21 — Palmeiras × Flamengo, às 16h30（土曜日16:30、パルメイラス対フラメンゴ）· DOM 22 — o fim do feriadão（日曜日、連休が終わります）· SEG 23 — tudo volta ao normal（月曜日にはすべて元に戻ります）。",
    "范文见本版 H 区（88 词）":
      "模範文はこのページのHの部分にあります（88語）",
    "(verbatim from this issue)":
      "（本号の記事から一字一句）",
  },
},
"ko": {
  "footer": "포르투갈어 주간지 VOL.4\u3000텍스트는 포르투갈어\u3000해설은 한국어",
  "page_line": 'f"제 {n} 면 / 총 {total} 면"',
  "gloss": "해설 — ",
  "badge372": "포르투갈어 텍스트\u3000한국어 해설 — 한국어 독자를 위한 판",
  "sub330": "포르투갈어 주간지\u3000VOL.4\u3000CONSCIÊNCIA NEGRA\u3000GABARITO DO ENEM\u3000A FINAL DA COPA",
  "sub330_size": 32,
  "disc_var": "disc_ko",
  "disc_text": "편집부 알림: VOL.3에서 약속한 실제 편지와 최고의 작문은 마감 때까지 오지 않았어요. 이번 호에는 예시를 싣고, 약속은 VOL.5로 이어져요。",
  "p7_geo": {"letters_pad": 22, "fy_gap": 16, "quote_step": 80},
  "label_nospace": "편집부예시예요,실제편지가아니에요",
  "footer_joined": "A Lucerna 포르투갈어 주간지 VOL.4 텍스트는 포르투갈어 해설은 한국어",
  "page_fmt": "제 {i} 면 / 총 8 면",
  "lang_name": "KO",
  "p8_keys_small": False,
  "model_bridge": "작문 과제（정답은 하나가 아니에요）. 모범 글（{NWORDS}단어）은 아래에 있어요。",
  "model_note": "모범 글은 이 페이지 H 부분에 있어요（{NWORDS}단어）",
  "textmd_header_title": "포르투갈어 주간지 VOL.4",
  "textmd_header_sub": "2026년 11월 16일~22일 · 텍스트는 포르투갈어 · 해설은 한국어 · 수준 A2–B2 · 연습 문제 150개",
  "textmd_extra": {
    "三天连休 · 11月20日周五 · 黑人意识日全国假日":
      "3일 연휴 · 11월 20일 금요일 · 흑인 의식의 날, 전국 공휴일",
    "Três dias, uma semana（三天连休，一周安排）: SEX 20 — o feriado começa（11月20日周五放假）· SÁB 21 — Palmeiras × Flamengo, às 16h30（周六 16:30 帕弗之战）· DOM 22 — o fim do feriadão（周日连休结束）· SEG 23 — tudo volta ao normal（周一恢复正常）.":
      "Três dias, uma semana（3일 연휴, 일주일 계획）: SEX 20 — o feriado começa（11월 20일 금요일, 공휴일）· SÁB 21 — Palmeiras × Flamengo, às 16h30（토요일 16:30, 파우메이라스 대 플라멩구）· DOM 22 — o fim do feriadão（일요일에 연휴가 끝나요）· SEG 23 — tudo volta ao normal（월요일에는 모든 게 정상으로 돌아와요）。",
    "范文见本版 H 区（88 词）":
      "모범 글은 이 페이지 H 부분에 있어요（88단어）",
    "(verbatim from this issue)":
      "（이 호 기사에서 한 자 한 자）",
  },
},
"zh_tw": {
  "footer": "葡萄牙語週報 VOL.4\u3000正文葡萄牙語\u3000講解繁體中文",
  "page_line": 'f"第{n}版／共{total}版"',
  "gloss": "譯注｜",
  "badge372": "葡萄牙語正文\u3000繁體中文講解 — 給繁體中文讀者的版本",
  "sub330": "葡萄牙語週報\u3000VOL.4\u3000CONSCIÊNCIA NEGRA\u3000GABARITO DO ENEM\u3000A FINAL DA COPA",
  "sub330_size": 34,
  "disc_var": "disc_zh_tw",
  "disc_text": "編輯部說明：上期（VOL.3）承諾的真實來信與最佳作文截稿時未收到，本期仍刊示例，順延至下期（VOL.5）。",
  "p7_geo": {"letters_pad": 22, "fy_gap": 16, "quote_step": 80},
  "label_nospace": "編輯部示例，非真實來信",
  "footer_joined": "A Lucerna 葡萄牙語週報 VOL.4 正文葡萄牙語 講解繁體中文",
  "page_fmt": "第{i}版／共8版",
  "lang_name": "ZH-TW",
  "p8_keys_small": False,
  "model_bridge": "寫作題（無唯一答案）；範文（{NWORDS} 詞）見下。",
  "model_note": "範文見本版 H 區（{NWORDS} 詞）",
  "textmd_header_title": "葡萄牙語週報 VOL.4",
  "textmd_header_sub": "2026 年 11 月 16–22 日 · 正文葡萄牙語 · 講解繁體中文 · 程度 A2–B2 · 150 道練習題",
  "textmd_extra": {
    "三天连休 · 11月20日周五 · 黑人意识日全国假日":
      "三天連假 · 11月20日週五 · 黑人意識日全國假日",
    "Três dias, uma semana（三天连休，一周安排）: SEX 20 — o feriado começa（11月20日周五放假）· SÁB 21 — Palmeiras × Flamengo, às 16h30（周六 16:30 帕弗之战）· DOM 22 — o fim do feriadão（周日连休结束）· SEG 23 — tudo volta ao normal（周一恢复正常）.":
      "Três dias, uma semana（三天連假，一週安排）: SEX 20 — o feriado começa（11月20日週五放假）· SÁB 21 — Palmeiras × Flamengo, às 16h30（週六 16:30 帕弗之戰）· DOM 22 — o fim do feriadão（週日連假結束）· SEG 23 — tudo volta ao normal（週一恢復正常）。",
    "范文见本版 H 区（88 词）":
      "範文見本版 H 區（88 詞）",
    "(verbatim from this issue)":
      "（逐字摘自本期文章）",
  },
},
}
