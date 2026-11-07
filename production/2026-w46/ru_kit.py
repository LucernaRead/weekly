# -*- coding: utf-8 -*-
"""Generate per-edition WEEKLY-KIT.md + ABSTRACT.txt + <slug>.text.md for the
W46 RU family from a gates JSON (ru-gates.json, written after gating).
Usage: ru_kit.py <gates-json>
Editions: core (zh-cn) + 10 fan-outs. KIT structure mirrors the W45 RU core KIT.
"""
import json, os, subprocess, sys

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
W46 = os.path.join(GOAL, "hidden_files/w46")

EDITIONS = {
    "core": dict(native="zh-cn", native_name="Simplified Chinese", native_label="简体中文",
                 suffix="", build="weekly-report-w46-ru-build", eddir="weekly-report-w46-ru-core",
                 slug="2026-w46-ru-core", title="VOL.3 · Russian text · Simplified Chinese explanations",
                 writing_type="写作", pairing_line="target language Russian × reader native language Simplified Chinese (zh-cn)",
                 furniture="Masthead carries no article (Russian is article-less per `tools/tables.py`): masthead is `Lucerna`; the top strip reads `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · 俄语正文 · 中文讲解`; the footer on every page reads `Lucerna · 俄语周报 VOL.3 · LUCERNA RUSSIAN WEEKLY` and the page number in Chinese (`第 N 版 / 共 8 版`).",
                 expl="all explanation is in Simplified Chinese — glosses, exercise instructions, answer notes, section furniture and footers. Russian is the only target-language text. This core IS the zh-cn edition for abstract purposes, so `ABSTRACT.txt` is one Simplified Chinese line (see §8)."),
    "en": dict(native="en", native_name="English", native_label="English",
               suffix="EN", build="weekly-report-w46-ru-en-build", eddir="weekly-report-w46-ru-en",
               slug="2026-w46-ru-en", title="VOL.3 · Russian text · English explanations",
               writing_type="writing", pairing_line="target language Russian × reader native language English (en)",
               furniture="Masthead `Lucerna` (no article); the top strip reads `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · RUSSIAN TEXT · ENGLISH EXPLANATIONS`; the P1 subtitle slot carries the pairing badge `TEXT IN RUSSIAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS`; the footer on every page reads `Lucerna · RUSSIAN WEEKLY VOL.3 · Russian text · English explanations` with `Page N of 8`.",
               expl="all explanation is in English — glosses, exercise instructions, answer notes, section furniture and footers. The Russian article text, exercise stems/keys and golden sentences are frozen from the core; only the explanation layer was rewritten."),
    "de": dict(native="de", native_name="German", native_label="Deutsch",
               suffix="DE", build="weekly-report-w46-ru-de-build", eddir="weekly-report-w46-ru-de",
               slug="2026-w46-ru-de", title="VOL.3 · Russian text · German explanations",
               writing_type="Schreiben", pairing_line="target language Russian × reader native language German (de)",
               furniture="Masthead `Lucerna` (no article); the top strip reads `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · RUSSISCHER TEXT · DEUTSCHE ERKLÄRUNGEN`; the P1 subtitle slot carries the pairing badge `RUSSISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`; the footer on every page reads `Lucerna · RUSSISCHE WOCHENZEITUNG VOL.3 · TEXT AUF RUSSISCH · ERKLÄRUNGEN AUF DEUTSCH` with `Seite N von 8`.",
               expl="all explanation is in German — glosses, exercise instructions, answer notes, section furniture and footers. The Russian article text, exercise stems/keys and golden sentences are frozen from the core; only the explanation layer was rewritten."),
    "fr": dict(native="fr", native_name="French", native_label="Français",
               suffix="FR", build="weekly-report-w46-ru-fr-build", eddir="weekly-report-w46-ru-fr",
               slug="2026-w46-ru-fr", title="VOL.3 · Russian text · French explanations",
               writing_type="Rédaction", pairing_line="target language Russian × reader native language French (fr)",
               furniture="Masthead `Lucerna` (no article); the top strip reads `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · TEXTE EN RUSSE · EXPLICATIONS EN FRANÇAIS`; the P1 subtitle slot carries the pairing badge `TEXTES EN RUSSE · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`; the footer on every page reads `Lucerna · HEBDOMADAIRE RUSSE VOL.3 · TEXTE EN RUSSE · EXPLICATIONS EN FRANÇAIS` with `Page N sur 8`.",
               expl="all explanation is in French — glosses, exercise instructions, answer notes, section furniture and footers. The Russian article text, exercise stems/keys and golden sentences are frozen from the core; only the explanation layer was rewritten."),
    "es": dict(native="es", native_name="Spanish", native_label="Español",
               suffix="ES", build="weekly-report-w46-ru-es-build", eddir="weekly-report-w46-ru-es",
               slug="2026-w46-ru-es", title="VOL.3 · Russian text · Spanish explanations",
               writing_type="Redacción", pairing_line="target language Russian × reader native language Spanish (es)",
               furniture="Masthead `Lucerna` (no article); the top strip reads `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · TEXTO EN RUSO · EXPLICACIONES EN ESPAÑOL`; the P1 subtitle slot carries the pairing badge `TEXTOS EN RUSO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`; the footer on every page reads `Lucerna · SEMANARIO RUSO VOL.3 · TEXTO EN RUSO · EXPLICACIONES EN ESPAÑOL` with `Página N de 8`.",
               expl="all explanation is in Spanish — glosses, exercise instructions, answer notes, section furniture and footers. The Russian article text, exercise stems/keys and golden sentences are frozen from the core; only the explanation layer was rewritten."),
    "it": dict(native="it", native_name="Italian", native_label="Italiano",
               suffix="IT", build="weekly-report-w46-ru-it-build", eddir="weekly-report-w46-ru-it",
               slug="2026-w46-ru-it", title="VOL.3 · Russian text · Italian explanations",
               writing_type="Composizione", pairing_line="target language Russian × reader native language Italian (it)",
               furniture="Masthead `Lucerna` (no article); the top strip reads `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · TESTI IN RUSSO · SPIEGAZIONI IN ITALIANO`; the P1 subtitle slot carries the pairing badge `TESTI IN RUSSO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI`; the footer on every page reads `Lucerna · SETTIMANALE RUSSO VOL.3 · TESTI IN RUSSO · SPIEGAZIONI IN ITALIANO` with `Pagina N di 8`.",
               expl="all explanation is in Italian — glosses, exercise instructions, answer notes, section furniture and footers. The Russian article text, exercise stems/keys and golden sentences are frozen from the core; only the explanation layer was rewritten."),
    "pt": dict(native="pt", native_name="Portuguese", native_label="Português",
               suffix="PT", build="weekly-report-w46-ru-pt-build", eddir="weekly-report-w46-ru-pt",
               slug="2026-w46-ru-pt", title="VOL.3 · Russian text · Portuguese explanations",
               writing_type="Escrita", pairing_line="target language Russian × reader native language Portuguese (pt)",
               furniture="Masthead `Lucerna` (no article); the top strip reads `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · TEXTOS EM RUSSO · EXPLICAÇÕES EM PORTUGUÊS`; the P1 subtitle slot carries the pairing badge `TEXTOS EM RUSSO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`; the footer on every page reads `Lucerna · SEMANÁRIO RUSSO VOL.3 · TEXTOS EM RUSSO · EXPLICAÇÕES EM PORTUGUÊS` with `Página N de 8`.",
               expl="all explanation is in Portuguese — glosses, exercise instructions, answer notes, section furniture and footers. The Russian article text, exercise stems/keys and golden sentences are frozen from the core; only the explanation layer was rewritten."),
    "nl": dict(native="nl", native_name="Dutch", native_label="Nederlands",
               suffix="NL", build="weekly-report-w46-ru-nl-build", eddir="weekly-report-w46-ru-nl",
               slug="2026-w46-ru-nl", title="VOL.3 · Russian text · Dutch explanations",
               writing_type="Schrijven", pairing_line="target language Russian × reader native language Dutch (nl)",
               furniture="Masthead `Lucerna` (no article); the top strip reads `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · TEKSTEN IN HET RUSSISCH · UITLEG IN HET NEDERLANDS`; the P1 subtitle slot carries the pairing badge `TEKSTEN IN HET RUSSISCH · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`; the footer on every page reads `Lucerna · RUSSISCH WEEKBLAD VOL.3 · TEKSTEN IN HET RUSSISCH · UITLEG IN HET NEDERLANDS` with `Pagina N van 8`.",
               expl="all explanation is in Dutch — glosses, exercise instructions, answer notes, section furniture and footers. The Russian article text, exercise stems/keys and golden sentences are frozen from the core; only the explanation layer was rewritten."),
    "ja": dict(native="ja", native_name="Japanese", native_label="日本語",
               suffix="JA", build="weekly-report-w46-ru-ja-build", eddir="weekly-report-w46-ru-ja",
               slug="2026-w46-ru-ja", title="VOL.3 · Russian text · Japanese explanations",
               writing_type="作文", pairing_line="target language Russian × reader native language Japanese (ja)",
               furniture="Masthead `Lucerna` (no article); the top strip reads `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · 毎週一号 · ロシア人が読んでいるロシア語を読む`; the P1 subtitle slot carries the pairing badge `ロシア語テキスト · 日本語の解説 — 日本語読者のための版`; the footer on every page reads `Lucerna · ロシア語週刊 VOL.3 · 本文はロシア語 · 解説は日本語` with `N ページ（全 8 ページ）`. Typeset with the W45 RU×JA `svglib.py` (JP face index + kinsoku handling).",
               expl="all explanation is in Japanese — glosses, exercise instructions, answer notes, section furniture and footers. The Russian article text, exercise stems/keys and golden sentences are frozen from the core; only the explanation layer was rewritten."),
    "ko": dict(native="ko", native_name="Korean", native_label="한국어",
               suffix="KO", build="weekly-report-w46-ru-ko-build", eddir="weekly-report-w46-ru-ko",
               slug="2026-w46-ru-ko", title="VOL.3 · Russian text · Korean explanations",
               writing_type="쓰기", pairing_line="target language Russian × reader native language Korean (ko)",
               furniture="Masthead `Lucerna` (no article); the top strip reads `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · 매주 발행 · 러시아가 읽는 러시아어`; the pairing badge `러시아어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판` is inserted at (975, 574) below the kept Russian subtitle (W45 RU×KO pattern); the footer on every page reads `Lucerna · 러시아어 주간지 VOL.3 · 텍스트는 러시아어 · 해설은 한국어` with `제 N 면 / 총 8 면`.",
               expl="all explanation is in Korean — glosses, exercise instructions, answer notes, section furniture and footers. The Russian article text, exercise stems/keys and golden sentences are frozen from the core; only the explanation layer was rewritten."),
    "zh-tw": dict(native="zh-tw", native_name="Traditional Chinese", native_label="繁體中文",
                 suffix="ZH-TW", build="weekly-report-w46-ru-zh-tw-build", eddir="weekly-report-w46-ru-zh-tw",
                 slug="2026-w46-ru-zh-tw", title="VOL.3 · Russian text · Traditional Chinese explanations",
                 writing_type="寫作", pairing_line="target language Russian × reader native language Traditional Chinese (zh-tw)",
                 furniture="Masthead `Lucerna` (no article); the top strip reads `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · 每週一期 · 讀俄羅斯人正在讀的俄語`; the pairing badge `俄語正文 · 繁體中文講解 — 給繁體中文讀者的版本` is inserted at (975, 574) below the kept Russian subtitle (W45 RU×ZH-TW pattern); the footer on every page reads `Lucerna · 俄語週報 VOL.3 · 正文俄語 · 講解繁體中文` with `第 N 版 / 共 8 版`. Typeset with the W45 RU×ZH-TW `svglib.py` (TC face index + Noto CJK TC families).",
                 expl="all explanation is in Traditional Chinese — glosses, exercise instructions, answer notes, section furniture and footers. The Russian article text, exercise stems/keys and golden sentences are frozen from the core; only the explanation layer was rewritten. Simplified and Traditional Chinese are independent editions; nothing was converted from the Simplified core."),
}

ABSTRACTS = {
    "core": "Lucerna俄语周报VOL.3：11月9日至15日平常的一周、11月10日警察节、11月11日大促与经济学家日、俄超第14轮赛果未知、11月12日国家队对乌兹别克斯坦，A2到B2，适合想学俄语的中国读者做以本周话题为素材的150道练习。",
    "en": "Lucerna Russian Weekly VOL.3: an ordinary week 9–15 November, Police Day on 10 November, the 11.11 sale and Economists' Day, round 14 results unknown at press time and Russia v Uzbekistan on 12 November; A2 to B2, 150 exercises on this week's topics for English-speaking learners of Russian.",
    "de": "Lucerna Russische Wochenzeitung VOL.3: eine gewöhnliche Woche vom 9. bis 15. November, Tag der Polizei am 10. November, der 11.11-Sale und Tag der Ökonomen, Ergebnisse des 14. Spieltags bei Redaktionsschluss unbekannt und Russland gegen Usbekistan am 12. November; A2 bis B2, 150 Übungen zu den Themen der Woche für deutschsprachige Russischlernende.",
    "fr": "Lucerna Hebdomadaire russe VOL.3 : une semaine ordinaire du 9 au 15 novembre, Jour de la police le 10 novembre, les soldes du 11.11 et le Jour des économistes, résultats de la 14e journée inconnus à la mise sous presse et Russie contre Ouzbékistan le 12 novembre ; A2 à B2, 150 exercices sur les sujets de la semaine pour les francophones qui apprennent le russe.",
    "es": "Lucerna Semanario ruso VOL.3: una semana normal del 9 al 15 de noviembre, Día de la Policía el 10 de noviembre, las rebajas del 11.11 y el Día del Economista, resultados de la jornada 14 desconocidos al cierre y Rusia contra Uzbekistán el 12 de noviembre; A2 a B2, 150 ejercicios sobre los temas de la semana para hispanohablantes que aprenden ruso.",
    "it": "Lucerna Settimanale russo VOL.3: una settimana normale dal 9 al 15 novembre, Giorno della polizia il 10 novembre, gli sconti dell'11.11 e il Giorno degli economisti, risultati della 14ª giornata sconosciuti alla chiusura e Russia contro Uzbekistan il 12 novembre; A2–B2, 150 esercizi sui temi della settimana per chi studia il russo in italiano.",
    "pt": "Lucerna Semanário russo VOL.3: uma semana normal de 9 a 15 de novembro, Dia da Polícia a 10 de novembro, os descontos do 11.11 e o Dia do Economista, resultados da jornada 14 desconhecidos ao fecho e Rússia contra o Usbequistão a 12 de novembro; A2 a B2, 150 exercícios sobre os temas da semana para quem aprende russo em português.",
    "nl": "Lucerna Russisch Weekblad VOL.3: een gewone week van 9 tot 15 november, Dag van de Politie op 10 november, de kortingen van 11.11 en Dag van de Econoom, uitslagen van speelronde 14 onbekend bij het ter perse gaan en Rusland tegen Oezbekistan op 12 november; A2 tot B2, 150 oefeningen over de thema's van de week voor Nederlandstaligen die Russisch leren.",
    "ja": "Lucernaロシア語週刊VOL.3：11月9～15日のふつうの週、11月10日の警察の日、11.11セールと経済学者の日、第14節の結果は締切時点で不明、11月12日のロシア対ウズベキスタン戦。A2からB2、ロシア語を学ぶ日本語読者のための今週の話題による150問の練習。",
    "ko": "Lucerna 러시아어 주간지 VOL.3: 11월 9~15일 평범한 한 주, 11월 10일 경찰의 날, 11.11 세일과 경제학자의 날, 마감 시점에 알려지지 않은 14라운드 결과와 11월 12일 러시아 대 우즈베키스탄전. A2부터 B2, 러시아어를 배우는 한국어 독자를 위한 이번 주 화제 150문제.",
    "zh-tw": "Lucerna俄語週報VOL.3：11月9日至15日平常的一週、11月10日警察節、11月11日大促與經濟學家日、俄超第14輪賽果未知、11月12日國家隊對烏茲別克斯坦，A2到B2，適合想學俄語的繁體中文讀者做以本週話題為素材的150道練習。",
}

CONTENT = """- **P1 · Первая (A2) — “Обычная неделя: пять рабочих дней”.** Lead: the ordinary week — five working days in a row, Police Day, the 11.11 sale, the national team. Numbers box, media-topics box, contents, word of the week “предзимье”, autumn-park photo, “Первый снег?” box, blitz quiz (ex. 1–10).
- **P2 · Жизнь (A2) — “10 ноября: День полиции”.** Police Day history (1962; the 10 November 1917 militia decree), Economist Day, professional holidays add no days off; holidays-of-the-week box; “А вы?” letter call for VOL.4; Bentley snowflake photo; weather words — предзимье, мокрый снег, гололедица, заморозки (ex. 11–28).
- **P3 · Культура (A2→B1) — “Кино в середине ноября”.** “Лиля” (from 12 Nov), “Эбенезер” (mid-November, no exact date claimed), “В сердце Нэшвилла” (streaming 13 Nov) (ex. 29–46).
- **P4 · Спорт (B1) — “14-й тур: итоги неизвестны”.** Honest press-time disclosure: round-14 results were unknown when the issue was built (2 Nov); verified 7-fixture table only, round-13 results box, 1912 football photo, national-team note (Uzbekistan–Russia, Thu 12 Nov, Tashkent; no kickoff time printed — sources conflicted) (ex. 47–64).
- **P5 · Молодёжь (B1) — “11 ноября: день покупок и посылок”.** Sale facts (Ozon 11.11, 22 Oct – 12 Nov; 600,000+ sellers, +16% YoY; 14.4m orders on 11 Nov 2025), parcels/returns/promo codes, Black Friday ahead; market photo (ex. 65–82).
- **P6 · Разбор (B2) — “Обычная неделя: как её прожить”.** Rhythm of an ordinary week, 9–15 Nov day strip, labelled PRACTICE-DATA chart (Работа и учёба 42, Покупки 24, Кино и книги 20, Спорт 14; sums to 100%), pro/contra box (ex. 83–100).
- **P7 · Язык (A2/B1/B2 + error clinic + word box + readers' corner + golden sentences + VOL.4 teaser) (ex. 101–112).** Three level columns (weather words, parcel words, attribution: “синоптики обещают”, “по данным”, “может быть”), four-item error clinic, word box “посылка”, readers' corner (see §6), 8 golden sentences with page references, teaser: full round-14 results, Uzbekistan–Russia result, Black Friday, readers' letters.
- **P8 · Тест (ex. 113–150 + all 150 keys).** A chronicle cloze 8, B general questions 8, C reading about Masha 4, D sentence building 4, E RU→reader-language translation 4, F word matching 4, G pickup-point dialogue cloze 5, H writing 1 + 87-word model text (“Моя обычная неделя в ноябре”, brief 80–100)."""

SOURCES = """- **Trend research (browser.search, Russian-language ecosystem, 2026-11-02):** trend-first selection from Russian-language media/social heat + calendar nodes for 9–15 Nov 2026. Anniversaries/commemorations were NOT used as living trends.
- **RPL round 14 fixtures (7 verified, rusfootball.info matchcenter crawled 2026-11-02 11:55 UTC + Sportradar/Sports.ru listings):** Fri 6 Nov Lokomotiv–Rubin 19:30; Sat 7 Nov Fakel–Dinamo 14:00, Akhmat–Rodina 16:30, Krasnodar–CSKA 19:30 (Ozon Arena); Sun 8 Nov Spartak–Akron 16:15, Zenit–Rostov (time unverified), Krylia Sovetov–Orenburg (time unverified). Moscow time. No 8th fixture verified — only these 7 are printed. Results UNKNOWN at press time (2 Nov); the issue says so on the page and carries full results to VOL.4. Never invented.
- **RPL round 13 verified results (rusfootball.info matchcenter, 2026-11-02):** Rubin 1–0 Fakel (31 Oct), Krasnodar 1–2 Rodina (31 Oct, via Regnum), Orenburg 0–0 CSKA (1 Nov), Dynamo Makhachkala 0–3 Rostov (1 Nov), Baltika 2–1 Akron (1 Nov), Lokomotiv 0–4 Spartak (1 Nov). Krylia Sovetov–Zenit (Mon 2 Nov 18:00) was still to be played at build time — stated as played after press time, result unknown. Next round: 15th round only 20 Nov 2026 (pause after round 14; carried from the W45 KIT).
- **11.11 sale:** Ozon 11.11 sale 22 Oct – 12 Nov 2026; >600,000 sellers joined, +16% year-on-year (Ozon press service via RIA/vc.ru, Oct 2026). 11 Nov 2025: >14.4m orders in one day on Ozon (Retail.ru via vc.ru). Top categories: smartphones, laptops, large appliances (wek.ru). Returns peak 11–30 Nov; promo codes on electronics typically valid 4–7 days (wek.ru advice). Black Friday: Ozon 13 Nov–2 Dec; M.Video from 12 Nov; Wildberries 16–30 Nov; Yandex Market provisionally 25–27 Nov.
- **Calendar nodes 9–15 Nov 2026 (weekdays verified with `date -d`, Europe/Moscow: 9 Mon, 10 Tue, 11 Wed, 12 Thu, 13 Fri, 14 Sat, 15 Sun):** 10 Nov Day of Police / internal-affairs officers (professional holiday, working day; history since 1962, date from the 10 Nov 1917 decree on workers' militia — Tolk); 11 Nov Economist Day; 13 Nov Day of RCB protection troops; 14 Nov Day of Sociologist; 15 Nov All-Russian Conscript Day. November overall: 20 working days, 10 days off (mk.ru / regions.ru). Professional holidays give no extra day off.
- **Weather (forecast only, never claimed as fallen):** Forecasters (Fobos: Leus/Tishkovets, via MK/regions.ru, 1–2 Nov 2026) promised first wet snow 3–4 Nov, ~1 cm temporary cover melting quickly; stable snow only end of Nov. Moscow sunset ~16:30–16:48. October 2026 was the 2nd warmest on record in Moscow (Fobos via mentoday.ru).
- **Cinema:** “Лиля” (Lilya Brik / Mayakovsky biopic, dir. Vera Storozheva) from 12 Nov (rss.plus listing); “Эбенезер” (Dickens retelling, Johnny Depp as young Scrooge) mid-November (MAXIM/respawn — exact date conflicts 12 vs 13 Nov, so the issue says “in mid-November” only); “В сердце Нэшвилла” (Jessica Chastain) streaming 13 Nov (vtomske.ru).
- **National team:** Friendly Uzbekistan–Russia, Thu 12 Nov, Tashkent, Pakhtakor stadium (Sport-Express / sports.ru, RFU 26 Oct). Extended squad 36 players incl. Golovin, Zakharyan, Batrakov. Venezuela–Russia 17 Nov in Krasnodar is OUTSIDE the week — mentioned only as the next match. Kickoff time OMITTED: Sport-Express gave 13:00 but sports.ru said the time was unannounced — conflict, so no time printed.
- **W45 promises honored (cross-checked against the W45 RU core KIT, which wins over the extractor file `hidden_files/w46/w45-promises.md` — no conflicts found):** 11.11 sale day (P1/P5 lead); round-14 results handled honestly (unknown at press time, schedule only, full results carried to VOL.4); reader letters — no fabrication, editor's example + on-page disclosure, promise carried forward (see §6). Handover items for OTHER targets found in the extractor file (DE Volkstrauertag/St. Martin, EN Veterans Day/NFL Munich, ES campaign, FR Senate/Armistice, IT Festival dei Popoli, JA Reading Week/Japan Series, NL Sinterklaas, PT Enem, ZH S16 final, ZHTW ITF) were NOT imported into the Russian family.
- **Editorial red lines observed:** no international politics, wars or geopolitics anywhere; Russian domestic life/culture/sport only."""

IMAGES = """- **P1 autumn park photo** (`autumn_path.jpg`, reused from the W43/W45 builds): Toxer427, CC0, Wikimedia Commons. Captioned as a November park scene.
- **P2 snowflake photo** (`snowflake.jpg`, reused from the W45 build): Wilson Bentley, c.1890–1920s, public domain.
- **P4 1912 football photo** (`football1912.jpg`, reused from the W43/W45 builds): Russia 1912 Olympics squad, unknown author, public domain.
- **P5 market photo** (`market.jpg`, reused from the W45 build): USDA farmers-market stand photo, Artist field Preston Keres (USDA), public domain (“Please credit: USDA Photo by Preston Keres”). Captioned honestly as a market scene, NOT claimed to be Moscow."""

def kit_text(key, e, g):
    pdf = f"Lucerna-VOL3{('-' + e['suffix']) if e['suffix'] else ''}.pdf"
    webpdf = f"Lucerna-VOL3{('-' + e['suffix']) if e['suffix'] else ''}-web.pdf"
    return f"""# WEEKLY-KIT — Lucerna Russian Weekly, VOL.3 (W46 {e['native']})

## 1. Spec

- **Edition:** Русский (Russian) target-language core, VOL.3; reader language {e['native_name']} ({e['native']}).
- **Issue week:** Monday 9 November – Sunday 15 November 2026. **Issue date:** Monday 9 November 2026.
- **Pairing:** {e['pairing_line']}.
  {e['furniture']}
- **Explanation-layer convention:** {e['expl']}
- **Format:** 8 pages (multiple of 4), 1950×2700 px per page, 4 columns, warm ivory paper, dark olive-green accents. Pipeline: Python → SVG → CairoSVG → PNG/PDF.
- **Exercises:** **150 total, continuously numbered 1–150**, registered in code and rendered as the P8 answer key. By page: P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38. By level: A2 51, B1 75, B2 24. By type: {g['types']}.
  P8 model writing text (“Моя обычная неделя в ноябре”) = **87 words** (brief: 80–100).
- **P7 golden sentences:** 8 sentences, each occurring exactly twice in the issue — once in its own article, once in the P7 “ФРАЗЫ НЕДЕЛИ” list (verified programmatically on page-joined SVG text, §7). All 8 come from this issue's own articles: P1 ×2, P2 ×1, P3 ×1, P4 ×1, P5 ×1, P6 ×2. Page references on P7 are kept in Russian (`Страница N`) in every edition.
- **No invented facts.** No standings are printed (the trend pool gives none). No invented poll, quote or account data. Round-14 results are explicitly unknown at press time (see §3). The P6 chart is labeled practice data (УЧЕБНЫЕ ДАННЫЕ + “not real statistics” line) and sums to 100% (42/24/20/14) with proportional bars.

## 2. Content per page

{CONTENT}

## 3. Trend / fact sources (all in-week or just-passed reports)

{SOURCES}

## 4. Images (public-domain / CC0 only; credit from the Wikimedia Commons Artist field)

{IMAGES}

## 5. Build / reproduce

Build code (copied from the W46 RU core build and repointed; fan-out transform via `hidden_files/w46/ru-transform.py` + `ru_maps.py`, which asserts every translation-map key occurs, no source-language explanation string remains, and Cyrillic content is unchanged except whitelisted furniture/badge lines):
`hidden_files/{e['build']}/` — `content12.py` (P1+P2), `content34.py` (P3+P4), `content56.py` (P5+P6), `content7.py` (P7), `content8.py` (P8 + registry). One process only (never run content modules standalone):

```
cd hidden_files/{e['build']}
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py
```

Outputs in this dir: `svg/` (8 SVGs), `cards/` (8 page PNGs),
`{pdf}` ({g['print_bytes']:,} bytes, print), `{webpdf}`
({g['web_bytes']:,} bytes, web, under the 7 MB limit).
Final build: {g['overflow_line']}; TOTAL 150; model words 87.
Web PDF built with `tools/webpdf.py` (real text layer, never a PIL whole-page JPEG拼合): pdftotext bytes {g['web_text_bytes']:,}; print-vs-web text identical after whitespace normalisation ({g['text_chars']:,} chars each).

## 6. Readers' corner — no fabrication (on-page disclosure, not KIT-only)

No real reader, letter, name or quote is fabricated. P7 prints a clearly labeled editor's example (“— М. (пример от редакции)”) AND an on-page disclosure in Russian and in the reader language stating plainly that no real reader letters or best P8 texts had arrived by press time, so the example stands and the promise carries to VOL.4. The disclosure is rendered inside the letters box on P7 (verified visually: box fully inside its border, clear of the “ФРАЗЫ НЕДЕЛИ” rule). The VOL.4 teaser repeats the call for letters.

## 7. Self-proofread record (full pass, 2026-11-02)

- **Defects found and fixed during the core build (all re-rendered and re-verified):**
  1. P7 letters-box LINEX: the disclosure's last line crossed the box rule — letter/disclosure text shortened, golden section moved down (`fy` 1770→1816), quote pitch 145→140, teaser moved to y=2420, box-height formula +34; the disclosure text now ends above the rule at 1802 in every edition (box bottom 1789.46 in the core, at most 1818 in the fan-outs where the rule passes only through empty box padding — verified on the rendered cards).
  2. P8 translation stem reused golden sentence #6 (“Посылку надо отследить…”) — reworded to “Посылку нужно отследить, получить и проверить.” so each golden sentence occurs exactly 2×.
  3. E3 translation key carried a stray “→ ___” (visible in the printed answer key) — removed; the key is now the plain translated sentence.
- **Programmatic checks after the final build (all pass):**
  - Golden sentences: 8/8 exactly 2×, each on its article page + P7 (check_core.py).
  - Gloss headwords: 0 fails; orphan line-starts: 0; same-baseline collisions: 0.
  - P8 keys: all 150 present in the rendered P8 (`p8.py extract` 150/150).
  - Exercise counts verified from the registry: {g['counts_line']}.
- **Occlusion audit (mandatory gate):** `tools/occlusion_audit.py`, selftest first (planted classes fired, clean controls silent). Final run: **{g['occlusion']}** (`{g['occlusion_file']}`).
- **P8 compare (mandatory gate):** `tools/p8.py compare` vs the core edition: **{g['p8_compare']}**.
- **Freeze diff (mandatory gate):** `tools/freeze.py diff` vs the core edition: **{g['freeze_diff']}**.
- **Visual check:** P1 + P7 cards read in full; P4 exercise block ends clear of the footer line; P6 chart labels clear of bars (GRAZE element-check clean). {g['visual_note']}
- **Accepted disclosed pattern (not a defect):** feature-column whitespace on P1–P6 (third column partly empty below the gloss box) matches the shipped W43/W45 pattern. No filler prose was added to fill columns.

## 8. Abstract

`ABSTRACT.txt` in this dir: one {e['native_name']} line, no ASCII double quotes, naming the real W46 topics (ordinary week 9–15 Nov, Police Day 10 Nov, 11.11 sale + Economist Day, round-14 results unknown, Uzbekistan–Russia 12 Nov) + masthead (Lucerna VOL.3), levels (A2–B2) and exercise count (150).

## 9. Delivery status

Finalized, NOT pushed, NOT posted: per the task brief, repo insertion is done by the coordinator (serialized). No git push, no Discord post, no user message was made from this build. `<slug>.text.md` in this dir is exported from the source manuscript via `hidden_files/w46/ru_textmd.py` (AST walk of `content*.py`, never from a PDF), with the P8 answer key reconstructed from the collected exercise registry.
"""

def main():
    gates = json.load(open(sys.argv[1], encoding="utf-8"))
    for key, e in EDITIONS.items():
        g = gates[key]
        ed = os.path.join(GOAL, "files", e["eddir"])
        os.makedirs(ed, exist_ok=True)
        open(os.path.join(ed, "WEEKLY-KIT.md"), "w", encoding="utf-8").write(kit_text(key, e, g))
        open(os.path.join(ed, "ABSTRACT.txt"), "w", encoding="utf-8").write(ABSTRACTS[key] + "\n")
        out = os.path.join(ed, e["slug"] + ".text.md")
        subprocess.run([os.path.join(GOAL, "tools/venv/bin/python"),
                        os.path.join(W46, "ru_textmd.py"),
                        os.path.join(GOAL, "hidden_files", e["build"]),
                        out, e["title"], e["writing_type"]],
                       check=True)
        print("wrote", ed)

if __name__ == "__main__":
    main()
