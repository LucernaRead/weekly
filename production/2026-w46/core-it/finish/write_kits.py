# -*- coding: utf-8 -*-
"""Write WEEKLY-KIT.md for the 10 W46 IT fan-out editions. Reads live file
sizes + pdftotext equality from disk at run time; all prose values below were
measured during the build (see fix/gate records). Run from it-finish/."""
import os, subprocess, json

G = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
H = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files")

ED = {
 "de": dict(native="German", native_name="Deutsch", web="DE", print="DE",
   footer="La Lucerna · ITALIENISCHE WOCHENZEITUNG VOL.3 · TEXT AUF ITALIENISCH · ERKLÄRUNGEN AUF DEUTSCH",
   pageline="Seite {n} von {total}", gloss="HINWEIS · ",
   p8sep="— PAGINA {pg} —", p8size="12.5, lh 1.12, gap 0.5", keystyle="dash style `N. key — note`",
   p8head="RISPOSTE · LÖSUNGEN — nach Seiten geordnet, suchen Sie die Nummer",
   p8note="Zu jeder Aufgabe ein kurzer Hinweis · ✓ = Schreibaufgabe",
   badge="INSERTED at y=574 (22pt BRICK, strapline at y=372 kept): `ITALIENISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`",
   band=("Diese Woche ist Martinswoche", "Die Martinswoche · Siehe Seite 2"),
   subtitle="Der Wochenplan · Cosa succede",
   svglib="Identical to core except one docstring line (Double Ninth wording: `重阳` → `Double Ninth`). No functional difference.",
   cjk="0", cjk_note="No CJK characters in shipped SVGs.",
   valid="forward-miss 0 / reverse-miss 0.",
   fixes="""1. P1 week-plan box: German bottom line `Die Termine folgen den Kalendern der Veranstaltungen; Uhrzeiten können sich ändern.` overflowed the box (ink right 2134.5 > page 1950, clipped) and the box subtitle `Der Wochenplan · Cosa succede, giorno per giorno` crossed the box border (ink right 1929.5 > border 1885.0). Fixed in `content12.py`: subtitle → `Der Wochenplan · Cosa succede`; bottom line → `Termine nach Kalender; Uhrzeiten können sich ändern.`
2. Leftover Simplified Chinese: the answers-note `答案见第 8 版 · 题目可跨级混排，按题号找答案` survived at 5 sites (`content12.py` ×1, `content34.py` ×2, `content56.py` ×2) and the P4 band carried the suffix `周` (`SPORT周`) — the transform lacked those replacements. Fixed: answers-note ×5 → `Lösungen Seite 8 · Stufen gemischt — nach Nummer suchen`; P4 band → `LA SETTIMANA DELLO SPORT · Die Sportwoche`.
3. ROUND 2: the shortened bottom line still crossed its box border by 9.2 px (ink right 1894.2 > border 1885.0; occlusion BOXTITLE flag). Fixed in `content12.py`: bottom line → `Termine nach Kalender; Zeiten können sich ändern.` Re-rendered a second time; re-gated clean.""",
   occ="Round 1: 3 flags (BOXTITLE ×2 + EDGE ×1, all P1). Round 2: 1 flag (BOXTITLE, P1 bottom line +9.2 px). Round 3 (after fix 3): 0 flags."),
 "en": dict(native="English", native_name="English", web="EN", print="EN",
   footer="La Lucerna · ITALIAN WEEKLY VOL.3 · TEXT IN ITALIAN · EXPLANATIONS IN ENGLISH",
   pageline="Page {n} of {total}", gloss="NOTE · ",
   p8sep="— PAGINA {pg} —", p8size="13, lh 1.14, gap 0.5", keystyle="dash style `N. key — note`",
   p8head="RISPOSTE · ANSWER KEY — grouped by page: find your exercise number",
   p8note="Each answer has a one-line note in English · ✓ = model-text task",
   badge="INSERTED at y=574 (22pt BRICK, strapline at y=372 kept): `Text in Italian · Explanations in English — the edition for English-speaking readers`",
   band=("This week is St Martin's week", "St Martin's week · See page 2"),
   subtitle="This week · Cosa succede, giorno per giorno",
   svglib="Identical to core except one docstring line (Double Ninth wording: `重阳` → `Double Ninth`). No functional difference.",
   cjk="0", cjk_note="No CJK characters in shipped SVGs.",
   valid="forward-miss 0 / reverse-miss 0.",
   fixes="No source fixes. Shipped as built by the family transform pipeline; no re-render was needed (gates + proofread clean on first pass).",
   occ="Round 1: 0 flags. Round 2 (final): 0 flags."),
 "es": dict(native="Spanish", native_name="español", web="ES", print="ES",
   footer="La Lucerna · SEMANARIO ITALIANO VOL.3 · TEXTO EN ITALIANO · EXPLICACIONES EN ESPAÑOL",
   pageline="Página {n} de {total}", gloss="Nota — ",
   p8sep="— PAGINA {pg} —", p8size="12.5, lh 1.12, gap 0.5", keystyle="dash style `N. key — note`",
   p8head="RISPOSTE · RESPUESTAS — por página, busca el número del ejercicio",
   p8note="Cada respuesta lleva una nota breve · ✓ marca el ejercicio de escritura",
   badge="REPLACES the strapline slot at y=372 (20pt BRICK): `TEXTOS EN ITALIANO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`",
   band=("Esta semana es la semana de San Martín", "La semana de San Martín · Véase la página 2"),
   subtitle="La semana · Cosa succede, giorno per giorno",
   svglib="Identical to core except one docstring line (Double Ninth wording: `重阳` → `Double Ninth`). No functional difference.",
   cjk="0", cjk_note="No CJK characters in shipped SVGs (post-fix; see fix record).",
   valid="forward-miss 0 / reverse-miss 0.",
   fixes="""1. Instruction string `Emparejar palabras y definiciones` overflowed/clipped at P2 (ink to 1954), overprinted the B1 badge at P4, and overprinted `weekend.` at P8. Fixed in `content12.py`/`content34.py`/`content8.py` (`instr=` ×3) → `Emparejar` (short-instruction precedent: fr `Associer`, pt `Combinar`).
2. Leftover Simplified Chinese: answers-note ×5 (same 5 sites as de) + P4 band suffix `周` (`DEPORTE周`). Fixed: answers-note ×5 → `Respuestas en la página 8 · Niveles mezclados — busca por número`; P4 band → `La semana del deporte`.
3. P7 disclosure (5 lines) let the gold rule strike the last line (`escribid a la redacción.`). Rewritten (2 occurrences: wrap-count + para) → `Ejemplo de la redacción, no una carta real. Al cierre no había cartas reales ni mejores textos de la página 8; la promesa pasa al VOL.4 — escribid a la redacción.` (4 lines). One full re-render; re-gated clean.""",
   occ="Round 1: 4 flags (EDGE ×1 P2, TEXTX ×2 P4/P8, LINEX ×1 P7). Round 2 (after fixes): 0 flags."),
 "fr": dict(native="French", native_name="français", web="FR", print="FR",
   footer="La Lucerna · HEBDOMADAIRE ITALIEN VOL.3 · TEXTE EN ITALIEN · EXPLICATIONS EN FRANÇAIS",
   pageline="Page {n} sur {total}", gloss="Note — ",
   p8sep="— PAGINA {pg} —", p8size="12.5, lh 1.12, gap 0.5", keystyle="dash style `N. key — note`",
   p8head="RISPOSTE · CORRIGÉS — classés par page, cherchez le numéro",
   p8note="Chaque réponse est accompagnée d'une note d'une ligne en français · ✓ = exercice du texte modèle",
   badge="INSERTED at y=574 (22pt BRICK, strapline at y=372 kept): `TEXTES EN ITALIEN · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`",
   band=("Cette semaine, c'est la semaine de la Saint-Martin", "La semaine de la Saint-Martin · Voir page 2"),
   subtitle="Semaine · Cosa succede, giorno per giorno",
   svglib="Identical to core except one docstring line (Double Ninth wording: `重阳` → `Double Ninth Festival`). No functional difference.",
   cjk="0", cjk_note="No CJK characters in shipped SVGs.",
   valid="forward-miss 0 / reverse-miss 8 (the 8 reverse misses are the footer page lines `Page N sur 8`, render-added furniture the validator's strip patterns do not recognise for this edition; no content miss).",
   fixes="No source fixes. Shipped as built by the family transform pipeline; no re-render was needed (gates + proofread clean on first pass).",
   occ="Round 1: 0 flags. Round 2 (final): 0 flags."),
 "ja": dict(native="Japanese", native_name="日本語", web="JA", print="JA",
   footer="La Lucerna · イタリア語週刊 VOL.3 · 本文はイタリア語 · 解説は日本語",
   pageline="{n} ページ（全 {total} ページ）", gloss="解説 — ",
   p8sep="— {pg} ページ —", p8size="13, lh 1.14, gap 0.5", keystyle="dash style `N. key — note`",
   p8head="RISPOSTE · 全解答と解説（1–8ページ）",
   p8note="各問に日本語の短い解説つき · ✓ は模範文のある問題",
   badge="REPLACES the strapline slot at y=372 (20pt BRICK): `イタリア語テキスト · 日本語の解説 — 日本語読者のための版`",
   band=("今週は聖マルティーノの週", "聖マルティーノの週 · 第2版参照"),
   subtitle="今週 · Cosa succede, giorno per giorno",
   svglib="Core svglib PLUS kinsoku `NO_START` handling and a JP face index. Functional: Japanese line-break rules; no other difference.",
   cjk="3015", cjk_note="Added CJK = the Japanese explanation layer itself (kana/kanji). String-set review: 0 Simplified-Chinese-only marker strings; Latin runs in added strings are frozen Italian furniture/grammar items only.",
   valid="forward-miss 1 / reverse-miss 8. The forward miss is the registry-only writing-item note `（自由作文、模範文は以下）` (the SVG renders the equivalent header `模範文（98 語）は下です`); the 8 reverse misses are the footer page lines, render-added furniture. No content miss.",
   fixes="""1. P7 disclosure (5 lines) let the gold rule strike the last line (`ください。`). Rewritten (2 occurrences: wrap-count + para) → `編集部の例文で、実際の手紙ではない。締め切り時に実際の手紙も第8版の最優秀作文も届かず、約束はVOL.4へ。編集部へ手紙を送ってください。` (4 lines). One full re-render; re-gated clean.""",
   occ="Round 1: 1 flag (LINEX, P7). Round 2 (after fix): 0 flags."),
 "ko": dict(native="Korean", native_name="한국어", web="KO", print="KO",
   footer="La Lucerna · 이탈리아어 주간지 VOL.3 · 텍스트는 이탈리아어 · 해설은 한국어",
   pageline="제 {n} 면 / 총 {total} 면", gloss="해설 — ",
   p8sep="— 제 {pg} 면 —", p8size="13, lh 1.14, gap 0.5", keystyle="dash style `N. key — note`",
   p8head="RISPOSTE · 정답 — 면별로 정리했어요. 번호를 찾으면 돼요",
   p8note="문제마다 짧은 해설이 있어요 · ✓ 표시는 모범 답안 문제예요",
   badge="NO P1 BADGE in this edition's transform (the only one of the ten): the pairing is carried by the footer, the top strip (`매주 발행 · 이탈리아가 읽는 이탈리아어`), and the week-plan subtitle. No badge was invented; recorded as the family variant as built.",
   band=("이번 주는 성 마르티노 주간", "성 마르티노 주간 · 2면 참조"),
   subtitle="이번 주 일정 · Cosa succede, giorno per giorno",
   svglib="Identical to core except one docstring line (Double Ninth wording: `重阳` → `Double Ninth`). No functional difference.",
   cjk="3213", cjk_note="Added CJK = the Korean explanation layer itself (Hangul). The 7 Han defect characters found in round 1 (band suffix + bridge fragment) were removed by the fix; post-fix string-set review finds 0 Simplified-Chinese-only marker strings; Latin runs in added strings are frozen Italian furniture/grammar items only.",
   valid="forward-miss 0 / reverse-miss 0.",
   fixes="""1. Leftover Chinese: P4 band `스포츠周` (suffix `周`) → `LA SETTIMANA DELLO SPORT · 스포츠 주간`; P6 bridge fragment `用方框里的词빈칸 채우기：manovra · deficit · copertura · scaglione` → `빈칸 채우기：manovra · deficit · copertura · scaglione`. One full re-render; re-gated clean.""",
   occ="Round 1: 0 flags. Round 2 (final): 0 flags."),
 "nl": dict(native="Dutch", native_name="Nederlands", web="NL", print="NL",
   footer="La Lucerna · ITALIAANS WEEKBLAD VOL.3 · TEKSTEN IN HET ITALIAANS · UITLEG IN HET NEDERLANDS",
   pageline="Pagina {n} van {total}", gloss="Uitleg — ",
   p8sep="— Pagina {pg} —", p8size="13, lh 1.14, gap 0.5", keystyle="dash style `N. key — note`",
   p8head="RISPOSTE · ANTWOORDEN — per pagina gerangschikt: zoek op nummer",
   p8note="Elke opgave heeft een korte uitleg in het Nederlands · ✓ = schrijfopgave met model",
   badge="REPLACES the strapline slot at y=372 (20pt BRICK): `TEKSTEN IN HET ITALIAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`",
   band=("Deze week is Sint-Maartensweek", "De Sint-Maartensweek · Zie pagina 2"),
   subtitle="Deze week · Cosa succede, giorno per giorno",
   svglib="Identical to core except one docstring line (Double Ninth wording: `重阳` → `Double Ninth Festival`). No functional difference.",
   cjk="0", cjk_note="No CJK characters in shipped SVGs.",
   valid="forward-miss 0 / reverse-miss 8 (the 8 reverse misses are the footer page lines `Pagina N van 8`, render-added furniture; no content miss).",
   fixes="""1. P7 disclosure (6 lines) let the gold rule strike the last line (`redactie.`). Rewritten (2 occurrences: wrap-count + para) → `Voorbeeld van de redactie, geen echte brief. Bij het ter perse gaan geen echte brieven en geen beste teksten voor pagina 8; de belofte gaat mee naar VOL.4 — schrijf naar de redactie.` (5 lines). One full re-render; re-gated clean.""",
   occ="Round 1: 1 flag (LINEX, P7). Round 2 (after fix): 0 flags."),
 "pt": dict(native="Portuguese", native_name="português", web="PT", print="PT",
   footer="La Lucerna · SEMANÁRIO ITALIANO VOL.3 · TEXTOS EM ITALIANO · EXPLICAÇÕES EM PORTUGUÊS",
   pageline="Página {n} de {total}", gloss="Nota — ",
   p8sep="— PÁGINA {pg} —", p8size="12.5, lh 1.12, gap 0.5", keystyle="PAREN style `N. key (note)` (this edition only; all others use the dash style) — writing items `N. ✓ note` as everywhere",
   p8head="RISPOSTE · RESPOSTAS — organizadas por página: busque pelo número do exercício",
   p8note="Uma nota breve em português para cada exercício · ✓ = exercício de escrita",
   badge="INSERTED at y=574 (22pt BRICK, strapline at y=372 kept): `TEXTOS EM ITALIANO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`",
   band=("Esta semana é a semana de São Martinho", "A semana de São Martinho · Ver página 2"),
   subtitle="ESTA SEMANA · Cosa succede",
   svglib="Identical to core except one docstring line (Double Ninth wording: `重阳` → `Double Ninth Festival`). No functional difference.",
   cjk="0", cjk_note="No CJK characters in shipped SVGs.",
   valid="forward-miss 0 / reverse-miss 14 (validator normalisation gaps, all adjudicated: P8 keys rendered with a repeated trailing answer letter, e.g. `25. c (mosto=mosto/vinho novo c)`, and `—` vs `(...)` separators — identical content, confirmed CLEAN by `p8.py compare`). No content miss.",
   fixes="No source fixes. Shipped as built by the family transform pipeline; no re-render was needed (gates + proofread clean on first pass).",
   occ="Round 1: 0 flags. Round 2 (final): 0 flags."),
 "ru": dict(native="Russian", native_name="русский", web="RU", print="RU",
   footer="La Lucerna · ИТАЛЬЯНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА ИТАЛЬЯНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ",
   pageline="Страница {n} из {total}", gloss="Пояснение — ",
   p8sep="— СТРАНИЦА {pg} —", p8size="12.5, lh 1.12, gap 0.5", keystyle="dash style `N. key — note`",
   p8head="RISPOSTE · ОТВЕТЫ — по страницам: ищите по номеру задачи",
   p8note="К каждой задаче — пояснение · ✓ — задание с образцом",
   badge="INSERTED at y=574 (22pt BRICK, strapline at y=372 kept): `ТЕКСТЫ НА ИТАЛЬЯНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ`",
   band=("Эта неделя — неделя святого Мартина", "Неделя святого Мартина · См. стр. 2"),
   subtitle="План недели · Cosa succede",
   svglib="Identical to core except one docstring line (Double Ninth wording: `重阳` → `Double Ninth`). No functional difference.",
   cjk="0", cjk_note="No CJK characters in shipped SVGs (post-fix; see fix record).",
   valid="forward-miss 0 / reverse-miss 0.",
   fixes="""1. P1: same two defects as de — bottom line `Даты — по календарям мероприятий; время может измениться.` clipped (ink right 1990.2) and subtitle `План недели · Cosa succede, giorno per giorno` crossed the box border (ink right 1902.8 > 1885.0). Fixed in `content12.py`: subtitle → `План недели · Cosa succede`; bottom line → `Даты — по календарям; время может измениться.`
2. Instruction string `Соединить слова и значения` overprinted `weekend.` at P8 and clipped at the page rule at P2. Fixed ×3 (`content12.py`/`content34.py`/`content8.py`) → `Соединить`.
3. Leftover Simplified Chinese: answers-note ×5 (same 5 sites) + P4 band suffix `周` (`СПОРТ周`). Fixed: answers-note ×5 → `Ответы на стр. 8 · Уровни смешаны — ищите по номеру`; P4 band → `Спортивная неделя`.
4. P7 disclosure 6→5 lines (first rewrite). One full re-render.
5. ROUND 2: P7 LINEX persisted — the disclosure's third line still crossed the gold rule. Root cause found in `content7.py`: the LETTERE box sits lower in this edition because the LA PAROLA gloss above it wraps to 3 lines in Cyrillic, so any ≥3-line disclosure straddles y=1686. Fixed: gloss trimmed 3→2 lines (`mosto = сусло/молодое вино. См. стр. 2: сусло становится вином.`) AND disclosure rewritten 5→3 lines → `Пример от редакции, а не письмо. Писем и лучших сочинений нет; обещание — VOL.4. Пишите нам.` (2 occurrences each: wrap-count + para). `transform.py` was NOT edited (generation artifact; the gloss pair there keeps the older wording — fixes live in `content7.py` and are recorded here). Second full re-render; re-gated clean.""",
   occ="Round 1: 5 flags (BOXTITLE ×2 + EDGE ×1 P1, LINEX ×1 P7, TEXTX ×1 P8). Round 2: 1 flag (LINEX, P7). Round 3 (after fix 5): 0 flags."),
 "zh-tw": dict(native="Traditional Chinese", native_name="繁體中文", web="ZHTW", print="ZHTW",
   footer="La Lucerna · 義大利語週報 VOL.3 · 正文義大利語 · 講解繁體中文",
   pageline="第 {n} 版 / 共 {total} 版", gloss="譯注｜ ",
   p8sep="— PAGINA {pg} —", p8size="13, lh 1.14, gap 0.5", keystyle="dash style `N. key — note`",
   p8head="RISPOSTE · 全部答案與簡析（第 1–8 版）",
   p8note="每題附一句中文簡析 · 帶 ✓ 的為範文題",
   badge="INSERTED at y=574 (22pt BRICK, strapline at y=372 kept): `義大利語正文 · 繁體中文講解 — 給繁體中文讀者的版本`",
   band=("本週是聖馬丁週", "聖馬丁之週 · 詳見第 2 版"),
   subtitle="本週日程 · Cosa succede, giorno per giorno",
   svglib="Core svglib with `_tc_index` / TC face selection. Functional: Traditional Chinese glyphs; no other difference.",
   cjk="972", cjk_note="Added CJK = the Traditional Chinese explanation layer itself. String-set review: 0 Simplified-Chinese-only marker strings — this edition was written natively in Traditional and never converted from the zh-cn core.",
   valid="forward-miss 1 / reverse-miss 0. The forward miss is the registry-only writing-item note `（開放題，範文如下）` (the SVG renders the equivalent header `範文（98 詞）見下`). No content miss.",
   fixes="No source fixes. Shipped as built by the family transform pipeline; no re-render was needed (gates + proofread clean on first pass).",
   occ="Round 1: 0 flags. Round 2 (final): 0 flags."),
}

def txtbytes(path):
    r = subprocess.run(["pdftotext", path, "-"], capture_output=True)
    return r.stdout

for n, e in ED.items():
    d = os.path.join(G, f"weekly-report-w46-it-{n}")
    printf = os.path.join(d, f"La-Lucerna-VOL3-{e['print']}.pdf")
    webf = os.path.join(d, f"La-Lucerna-VOL3-{e['web']}-web.pdf")
    textf = os.path.join(d, f"2026-w46-it-{n}.text.md")
    assert os.path.exists(webf), f"missing web pdf {webf}"
    a, b = txtbytes(printf), txtbytes(webf)
    assert a == b, f"text mismatch {n}"
    assert len(b) > 0 and os.path.getsize(webf) < 7000000, n
    kit = f"""# WEEKLY-KIT — La Lucerna VOL.3 · W46 IT × {e['native']} (2026-w46-it-{n})

## 1. Spec
- Issue: week Mon Nov 9 – Sun Nov 15, 2026; issue dated Mon Nov 9, 2026. VOL.3, Italian target.
- Format: 8 pages, 1950×2700 px, 4 columns, warm ivory paper, dark olive-green accents. Masthead: "La Lucerna" (UnifrakturMaguntia).
- Pairing / explanation layer: **Italian text + explanations in {e['native']} ({e['native_name']})**. The Italian article text is the frozen core layer, byte-identical in content to the W46 IT core (`files/weekly-report-w46-it-core/`); only the explanation layer (glosses, bridges, instructions, answer notes, furniture) is in {e['native']}. Verified by `freeze.py diff` (see §8): every removed string is a Chinese explanation/furniture string, every added string is {e['native']} (plus frozen Italian heads/grammar items).
- Exercises: 150 total, continuously numbered 1–150. By page: P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38. By level: A2 47, B1 70, B2 33. P8 writing model text: 98 words (brief 80–100).
- P8: sections A cronaca 8, B generali 8, C leggi e rispondi 4, D frasi 4, E traduci 4, F matching 4, G dialogo 5, H scrittura 1. Answers generated from the exercise registration table in the build code (content12/34/56/7/8.py), not hand-typed. P8 answer style: {e['keystyle']}; writing items `N. ✓ note`. P8 header: `{e['p8head']}`; note line: `{e['p8note']}`; page separator `{e['p8sep']}` ({e['p8size']}).
- P7 golden sentences: the same 8 quotes as the core, each verified to occur exactly 2× in the joined SVG text (once in its article, once on P7) — see §8.

## 2. Contents per page
Identical Italian content to the core — see `files/weekly-report-w46-it-core/WEEKLY-KIT.md` §2 (P1 Prima / P2 Vita / P3 Cultura / P4 Sport / P5 Giovani / P6 Approfondimento / P7 Lingua / P8 Valutazione e risposte, exercises 1–150 in the same order). Only the explanation layer differs (this KIT §§1, 7–8). No page was restructured for this edition.

## 3. Lead topic
«San Martino» — as the core (W46 IT core KIT §3). No new lead, no new topic introduced by the explanation layer.

## 4. Trend / fact sources
Identical to the core — see `files/weekly-report-w46-it-core/WEEKLY-KIT.md` §4. The explanation layer adds NO new facts: glosses translate the Italian words, bridges paraphrase the Italian articles, and the P6 practice chart keeps its Italian data and its on-page `DATI INVENTATI PER L'ESERCIZIO` disclaimer (chart title translated, data frozen — verified in the freeze diff, §8). No international politics anywhere; Italy domestic politics (manovra) as in the core, with the same `not yet law` disclosures.

## 5. Images (public-domain / CC0 only, per SOP)
Identical to the core — see `files/weekly-report-w46-it-core/WEEKLY-KIT.md` §5 (P3 tartufo PD, P5 castagne CC0, programmatic frost/clocks/chart). No new image in this edition.

## 6. Verification, corrections, and promises
Identical to the core — see `files/weekly-report-w46-it-core/WEEKLY-KIT.md` §6 (Festival date correction, Torrone promise, manovra `not yet law`, no real letters, VOL.4 promises). Fan-out specifics: the P7 disclosure is translated into {e['native']} with the same meaning (editor's example, no real letters/best texts had arrived, promise carries to VOL.4, write to the editors); the P8 E-section keys 137–139 are legitimate translation re-aims (the Italian stems are re-aimed at the {e['native']}-speaking reader — `p8.py` keydiff, §8), key 140 keeps its Italian sentence with a {e['native']} stem gloss. No fabricated readers, letters, names, or quotes.

## 7. Build / repro
- Build dir: `hidden_files/weekly-report-w46-it-{n}-build/` (content12/34/56/7/8.py, bslib4.py, svglib.py, render.py, run.py, transform.py). Single one-process driver: `cd hidden_files/weekly-report-w46-it-{n}-build && ../../tools/venv/bin/python run.py` then `render.py` (tools venv; system python3 has no cairosvg). Render produces cards + print PDF only; the web PDF is built separately with `tools/webpdf.py` (never PIL whole-page JPEG).
- `transform.py` files were NOT edited (W45-harvested generation artifacts); all fixes below were applied to the `content*.py` sources and are recorded here.
- `.text.md` was exported from the edition's own build sources with the AST exporter `hidden_files/w46/it-finish/export_it_textmd.py` (source manuscript, never from PDF/SVG), and validated two-way against the shipped SVGs with `hidden_files/w46/it-finish/validate_textmd.py` — see §8.
- `svglib.py`: {e['svglib']}
- Fix record (source fixes, full re-render + re-gate after each round):
{e['fixes']}

## 8. Gates
- Builder self-check: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; TOTAL 150; levels A2 47 / B1 70 / B2 33; pages 10/18/18/18/18/18/12/38; model text 98 words. {"Build log `hidden_files/w46/it-finish/rerun" + ("2" if n in ('de','ru') else "") + f"-{n}.log` (final render)." if n in ('de','es','ja','ko','nl','ru') else "Counts re-verified on the shipped SVGs via `p8.py` (150 noted), freeze numbering coverage 1–150, and the SVG text layer; no re-render was run for this edition (see fix record)."}
- `tools/freeze.py diff` vs core (log `hidden_files/w46/it-finish/freeze{'3' if n in ('de','ru') else '2'}-{n}.log`): all pages compared; TOTAL added CJK characters {e['cjk']}. {e['cjk_note']} Removed strings are Chinese explanation/furniture strings only; no Italian body string was removed or added (Italian-heavy added strings are frozen box titles and P7 grammar trigger phrases, adjudicated).
- `tools/p8.py compare` vs core P8 (log `hidden_files/w46/it-finish/p8-{'3' if n in ('de','ru') else '2'}-{n}.log`): status CLEAN, 150 noted = 150 noted, missing=[] extra_count=0 uncertain=[], keydiff=[137, 138, 139] — the three E-section re-aims, verified per edition in the proofread (see §6).
- `tools/occlusion_audit.py` (selftest OK every run, log `hidden_files/w46/it-finish/occlusion{'3' if n in ('de','ru') else '2'}-{n}.log`): {e['occ']} Every flag was adjudicated on pixels; final state 0 flags on the 8 shipped SVGs (incl. LINEX + same-baseline furniture scan + chart GRAZE element-check; P6 chart frozen Italian).
- `.text.md` validation: {e['valid']}
- Web PDF: `tools/webpdf.py <svg-dir> La-Lucerna-VOL3-{e['web']}-web.pdf` — {os.path.getsize(webf):,} bytes (< 7 MB); `pdftotext` {len(b):,} bytes, byte-identical to the print PDF's text; 8 pages.
- Golden sentences: all 8 occur exactly 2× in whitespace-normalized joined SVG text (re-checked on the final shipped SVGs).
- Scans: Simplified-Chinese residue 0 in this edition's SVGs (except the native-script editions ja/ko/zh-tw, adjudicated above); gloss headwords attested in body text (12/12); exercise numbers 1–150 complete; dates/weekdays as core (calendar-checked).
- Visual: fixed regions pixel-checked on the final cards (P1 box/subtitle, instruction sites, P7 FRASI band + gold rule, P1 top-band same-baseline scan). Proofread round 1 (gates + pixel adjudication + source scans) and round 2 (full re-gate + explanation-layer read: freeze added strings P1–P7, E-keys, gloss attestation) — zero open issues at定稿.

## 9. Furniture registry (measured from this edition's build sources)
- Footer (bslib4.py, y=2624): `{e['footer']}`
- Page line (bslib4.py): `{e['pageline']}`
- Gloss prefix (bslib4.py `gloss()`): `{e['gloss']}`
- P1 badge: {e['badge']}
- P1 band right lines: `{e['band'][0]}` / `{e['band'][1]}`
- P1 week-plan box subtitle: `{e['subtitle']}`
- Masthead strapline (y=372, 19pt GREY, frozen Italian): `IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA` (replaced by the badge in es/ja/nl — see badge line).
- Top strip (y=92): left `VOL. 3 · TERZA EDIZIONE`, right `SETTIMANA DAL 9 AL 15 NOVEMBRE 2026`, centre `OGNI SETTIMANA IN ITALIANO · <native strapline>` (same-baseline collision scan clean).

## 10. Files shipped (edition dir `files/weekly-report-w46-it-{n}/`)
- `svg/` — 8 shipped SVGs (p1-prima … p8-valutazione).
- `cards/` — 8 PNG cards (1950×2700).
- `La-Lucerna-VOL3-{e['print']}.pdf` — print PDF (vector, text layer), {os.path.getsize(printf):,} bytes.
- `La-Lucerna-VOL3-{e['web']}-web.pdf` — web PDF (text layer, < 7 MB), {os.path.getsize(webf):,} bytes.
- `2026-w46-it-{n}.text.md` — manuscript text export (from the source manuscript, never from PDF), {os.path.getsize(textf):,} bytes, 150 exercises.
- `ABSTRACT.txt` — {e['native']}, one line, no ASCII double quotes.
- `WEEKLY-KIT.md` — this file.
- Gate logs: `hidden_files/w46/it-finish/freeze{'3' if n in ('de','ru') else '2'}-{n}.log`, `p8-{'3' if n in ('de','ru') else '2'}-{n}.log`, `occlusion{'3' if n in ('de','ru') else '2'}-{n}.log`.
"""
    out = os.path.join(d, "WEEKLY-KIT.md")
    open(out, "w", encoding="utf-8").write(kit)
    print(n, "KIT bytes:", len(kit.encode()), "| print:", os.path.getsize(printf), "| web:", os.path.getsize(webf), "| text:", len(b), "| textmd:", os.path.getsize(textf))
print("DONE")
