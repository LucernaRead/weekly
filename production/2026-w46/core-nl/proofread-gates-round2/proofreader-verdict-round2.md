# Round 2 Proofreader Verdict — Lucerna Weekly W46 (NL family)

- **Issue:** W46, dated Mon 2026-11-09 – Sun 2026-11-15, 2026. VOL.3.
- **Scope:** all 11 NL-target editions: `2026-w46-nl-de`, `-en`, `-es`, `-fr`, `-it`, `-ja`, `-ko`, `-pt`, `-ru`, `-zh-cn`, `-zh-tw`.
- **Directory note:** `files/weekly-report-w46-nl-core/` IS the `2026-w46-nl-zh-cn` edition. It is not a 12th edition.
- **Role:** independent proofreader (Round 2). The proofreader did not build or fix these editions and edited no edition file, re-rendered nothing, touched no `weekly-git`, no `index.json`, pushed nothing, inserted nothing, posted nothing.
- **Basis:** full SOP read; Round 1 verdict read; FIX-REPORT read; all gates re-run independently from `hidden_files/w46/nl-proofread-gates-round2/` with the shared toolkit (`freeze.py`, `p8.py`, `occlusion_audit.py`, `webpdf.py` rules). The fix worker's gate JSONs were not trusted.
- **Gate directory:** `hidden_files/w46/nl-proofread-gates-round2/` — `run_gates.sh`, `gates-freeze-p8.log`, `gates-occlusion.log`, `freeze-*.json` (11), `p8-*.json` (11), `p8-extract-*.json` (10), `occlusion-*.json` (11), `occlusion-*-vs-core.json` (10), `counts.json`, `checks.py`, `checks.log` (sections 1–10 complete), `pdf-check.log`, `crops/` (zone crops + half-size P1/P8 cards).

## Final verdict

**ROUND 2 FAIL — blocking defects: N-1 (core/zh-cn) and N-2 (fr). All Round 1 fixes are CONFIRMED; no other defect was found.**

Per-edition verdicts (on the artifacts as rendered for this round):

| Edition | Verdict | Reason |
|---|---|---|
| 2026-w46-nl-de | PASS | All checks passed on current artifacts. |
| 2026-w46-nl-en | PASS | All checks passed on current artifacts. |
| 2026-w46-nl-es | PASS | All checks passed on current artifacts. |
| 2026-w46-nl-fr | **FAIL** | N-2 (blocking). |
| 2026-w46-nl-it | PASS | All checks passed on current artifacts. |
| 2026-w46-nl-ja | PASS | All checks passed on current artifacts. |
| 2026-w46-nl-ko | PASS | All checks passed on current artifacts. |
| 2026-w46-nl-pt | PASS | All checks passed on current artifacts. |
| 2026-w46-nl-ru | PASS | All checks passed on current artifacts. |
| 2026-w46-nl-zh-cn (core) | **FAIL** | N-1 (blocking). |
| 2026-w46-nl-zh-tw | PASS | All checks passed on current artifacts. |

The 9 PASS editions pass **on the current artifacts**. Fixing N-1/N-2 at the source requires re-rendering and, if the core source changes, re-derivation of the fan-outs; under SOP §8.4 (proofread-until-zero) the whole issue must then pass a full Round 3 re-proofread before shipping. Nothing in this verdict authorises shipping any edition before Round 3.

## 1. Fix verification

### F-1 — abstracts (all 11): CONFIRMED

All 11 `ABSTRACT.txt` files are practice-framed, single-line, contain 0 ASCII double-quotes, carry the topic, levels and `150`, and keep the facts/dates intact. Diff against the fix worker's `hidden_files/w46/nl-fix/before/ABSTRACT-*.txt` copies shows only the closing clause changed in every edition; the common prefix is identical. Byte sizes match FIX-REPORT exactly: core 368, de 428, en 382, es 448, fr 454, it 405, ja 440, ko 427, pt 445, ru 667, zh-tw 339. Trailing-newline state preserved (core: one line with newline; the other 10: no trailing newline). Topic words such as "news" / "ニュース" remain only as topic names, not as "learn from the news" framing. FR's ASCII apostrophe in `d'entraînement` and EN's in `week's` are apostrophes, not double-quotes. No news-framing remains in any language.

### F-2a — core P2 lone `。` / deleted `更`: CONFIRMED (defect gone). Deletion ruling: ACCEPTABLE.

- Evidence: core `svg/p2-leven.svg`, EN JIJ box, x=1473, exactly two lines: y=1359.84 `11 月 11 日你会提灯笼挨家唱歌，还是爱看` and y=1388.24 `圣诞老人新闻？写两句荷兰语寄给编辑部。` Full sentence: `11 月 11 日你会提灯笼挨家唱歌，还是爱看圣诞老人新闻？写两句荷兰语寄给编辑部。` No lone `。` anywhere on the page (independent orphan scan: 0 lone `。`, 0 line-start `。` in all 8 pages × 11 editions). Full-frame P2 card viewed clean.
- **Ruling on the deleted `更` — ACCEPTABLE, not a meaning defect.** The sentence reads correctly: `还是…爱看` preserves the singing-vs-watching alternative against the Dutch source `of kijk je liever…` (`liever` = rather/preferably). Deleting `更` weakens the comparative emphasis ("even more") but does not falsify the meaning: the choice between going door to door singing and watching the Sinterklaas news is intact, and the imperative that follows is unchanged. The defect (orphaned punctuation) is gone and no new meaning defect was introduced.

### F-2b — core + zh-tw P6 gloss lone `。`: CONFIRMED (defect gone). Change (a) ruling: ACCEPTABLE. Change (b) ruling: ACCEPTABLE (non-blocking observation recorded).

- Evidence: core P6 gloss, x=1007, three lines (y=238.5 / 268.225 / 297.95): `译注｜de traditie 传统 · griezelen 吓人 ·` / `de belangstelling 兴趣· de achteruitgang` / `衰退 · de deskundige 专家。` zh-tw mirrors it, ending `專家。`. No lone `。`. Full-frame P6 cards (core and zh-tw) viewed clean; zone crop of the core gloss viewed: the middot is clearly distinct from `兴趣`, no collision, separator function intact.
- **Ruling (a) `扮鬼吓人` → `吓人` — ACCEPTABLE.** `吓人` is an accurate gloss for `griezelen` (to scare / to spook); the P6 article itself defines the festival as `Halloween draait om griezelen` (Halloween is about spooking/scaring). The worker's precedent claim is verified: zh-tw already uses `嚇人` (the Traditional form of `吓人`). All other editions gloss `griezelen` with the same scare/spook meaning without the dress-up nuance (DE/EN "to scare/to spook", ES "asustar", FR "faire peur", IT "spaventare", RU "пугать"). The fuller `扮鬼吓人` is deliberately retained where it belongs — the core P8 note for item 94 (`94. griezelen — griezelen = 扮鬼吓人`, x=989, y=1848.3) and the text.md item 91/94 explanations — a different context, not an inconsistency requiring change.
- **Ruling (b) tightened separator `兴趣· de` — ACCEPTABLE, with the source-level inconsistency recorded.** The tight middot is the only unspaced separator in the core/zh-tw P6 gloss (the other 4 separators in the same gloss use spaced ` · `; a full-edition tight-middot scan found only this line plus intentional Korean morpheme dots and the name dot in `赫尔曼·科赫`). At render level there is no visual defect: the crop shows the middot distinct and legible, the occlusion audit reports 0 flags, and no reader-facing confusion is possible. A stroke-level pixel-gap measurement run was inconclusive (ink runs fragment per glyph stroke and do not isolate the separator) and is **not** cited as evidence; the ruling rests on the rendered crop, the SVG string, and the occlusion result. The one-space inconsistency is recorded here explicitly rather than hidden, and is non-blocking. (Observation O-R2-1; see §5.)

### E-1 — fr + pt P3 stranded "3.": CONFIRMED

- FR P3, single line (x=989, y=1954.5): `Calcule: réponds par les chiffres de la page 3.` Correct French; the space before the colon is French convention; `réponds par les chiffres` = answer using the figures. No stranded `3.`.
- PT P3, single line: `Calcula: responde com números da página 3.` Correct Portuguese (`com números` without article is grammatical). No stranded `3.`.
- Full-frame P3 cards (fr, pt) viewed: exercises 43/44 follow with normal spacing; no overlap or defect.

### E-2 — zh-tw P6 caption: CONFIRMED

zh-tw P6 caption line 1 (y=660.86) ends `。`: `練習數據：虛構數字，僅供練習，非真實調查。`; line 2 (y=685.28) starts `問題：`. Verified character-by-character as the exact Traditional mirror of the core caption `练习数据：虚构数字，仅供练习，非真实调查。` Full-frame zh-tw P6 card viewed clean.

### E-3 — zh-tw P8 H-intro: CONFIRMED

zh-tw P8, single line (x=1451, y=562.77): `寫作題（無唯一答案）；範文（89 詞）見下。` One line, no lone `。`, meaning preserved (`無唯一答案` = no unique answer, same as `沒有唯一答案`). Full-frame zh-tw P8 card viewed clean.

### Regression sweep: no fix introduced a new defect

Orphan/stranded-number scan re-run independently over all 8 pages × 11 editions: 0 lone-`。` elements, 0 line-start-`。` elements, exactly 142 exact `N.` elements per edition, all at stem x-coordinates (137/599/1061/1523), 0 stranded numbers. KO retains the 2 accepted `가.`/`요.` orphans per O-2 (not counted, not re-raised).

### KIT corrections: PARTIAL (present as fix-record glosses; original stale lines unchanged — internal KIT matter, not reader-facing, non-blocking)

A fix record section is present in all 11 KITs. However, the corrections live **in the fix-record gloss only**: core KIT §1 still literally reads "Pairing badge on P1 (subtitle slot)" in §1 itself (glossed in the record as the subtitle-slot furniture, W45 precedent); the JA KIT body still states the stale freeze total 3,377 (record corrects it to 3,341, line 158, plus a corrected re-gate line); the RU KIT §7 still states stale 55,344 text bytes / 809,351 bytes (record corrects to 55,313 / 809,219; §9 already states 55,313). The measured values in this round (JA added CJK 3,341; RU web-PDF text bytes 55,313) match the record corrections, so the corrections are accurate. Recommendation for the next KIT pass: rewrite the stale lines themselves so the record is not the only place the correction lives. Not a shipping defect: no reader sees a KIT.

## 2. Full key-letter verification — 150/150

Every answer key 1–150 was verified **semantically** in the NL core text.md (read in full, 469 lines) against the Dutch articles, grammar, and recomputed arithmetic, and in all 11 editions' P8 renderings. `p8.py` set-equality was used only as a cross-check, never as the verification itself.

- **Core: 150/150 keys semantically CORRECT.** Adjudicated points (none is a key error): item 6 `zetten` (plural subject); item 53 `kwartfinales` (plural required); item 60 `zijn gekomen` (correct perfect of `komen` with `zijn`; simple past `kwamen` would also be grammatical, but the exercise targets the perfectum, as its note states); item 100 `Kiezen hoeft niet: het zijn twee feesten.` (colon joining the explanation is acceptable; the article uses an em dash); item 127 repeats item 92's stem/options/key verbatim (design repetition, same correct key B, not an error); item 111 `gaat` (verb-first main clause after `als`, separable `gaat…aan`).
- **Arithmetic recomputed:** 43: 14−9=5; 44: 15−9=6; 45: 16:00−12:00=4 hours; 46: 2026−2009=17; 83: 40; 84: 25; 85: 40+20=60; 86: 15; 87: 40+25+20+15=100. All correct.
- **All 11 editions' P8 renderings: 150/150 noted** (extracts). Per-edition key extracts diffed against the verified core keys programmatically: the **only** differences in all 10 fan-outs are items 137/138 (see below). The full rendered core P8 answer list was eyeballed against text.md keys; all listed keys matched (including chart numbers, `103. B`, `142. d`).
- **Items 137/138 — legal re-aims, verified semantically in every edition** from the rendered P8 notes and text.md E-sections. Core keys: 137 = `Het Sinterklaasjournaal is elke dag om 18:00 uur te zien.`; 138 = `Sint-Maarten is het feest van het delen.` Fan-out renderings are correct translations into the reader's native language, e.g. DE `Das Sinterklaasjournaal läuft jeden Tag um 18:00 Uhr.` / `Martinstag ist das Fest des Teilens.`; EN `The Sinterklaas news is on every day at 18:00.` / `St Martin's Day is the festival of sharing.`; JA `シンタクラース・ニュースは毎日18:00に放送される。` / `聖マルティン祭は分け合いの祭り。`; RU `Новости Синтерклааса идут каждый день в 18:00.` / `День святого Мартина — праздник того, чтобы делиться.`; zh-tw mirrors the core in Traditional. (RU item 138's extract key truncates at the internal em dash — a tool extraction artifact; the full rendered SVG note was verified correct.) The `p8.py` keydiff [137,138] is therefore adjudicated as expected and correct.

### Matching blocks — quoted option-by-option

**Block P2, items 25–28** (stems: 25. `de lampion`, 26. `delen`, 27. `de mantel`, 28. `het erfgoed`).
Options: a. `licht delen met anderen, eten delen`; b. `een papieren lichtje voor 11 november`; c. `wat een land bewaart uit het verleden`; d. `een lange jas tegen de kou`.
Keys: 25→b, 26→a, 27→d, 28→c. **All correct; bijection complete (a/b/c/d each used once).**

| Item | Stem | Key | Verification |
|---|---|---|---|
| 25 | de lampion | b | A paper lantern for 11 November — correct. |
| 26 | delen | a | Sharing light/food with others — correct (article: `licht delen, eten delen`). |
| 27 | de mantel | d | A long coat against the cold — correct (Martin's cloak). |
| 28 | het erfgoed | c | What a country preserves from the past — correct. |

**Block P8 (F · WOORDEN VAN DE WEEK), items 141–144** (stems: 141. `het journaal`, 142. `de intocht`, 143. `de lampion`, 144. `delen`).
Options: a. `een papieren lichtje voor 11 november`; b. `een dagelijks nieuwsprogramma op televisie`; c. `licht en eten geven aan anderen`; d. `de feestelijke aankomst van Sinterklaas`.
Keys: 141→b, 142→d, 143→a, 144→c. **All correct; bijection complete (a/b/c/d each used once).**

| Item | Stem | Key | Verification |
|---|---|---|---|
| 141 | het journaal | b | A daily TV news programme — correct (Sinterklaasjournaal, 18:00 daily). |
| 142 | de intocht | d | The festive arrival of Sinterklaas — correct. |
| 143 | de lampion | a | A paper lantern for 11 November — correct. |
| 144 | delen | c | Giving light and food to others — correct. |

No wrong key letter was found in any edition. **Key verification result: 150/150 in the core and 150/150 in each of the 11 editions' P8 renderings.**

## 3. New / residual defects (pre-existing; missed by Round 1)

Both are reader-facing, both in P8 answer notes, both violate MUST-VERIFY item 4 (every explanation/note in the reader's native language; no untranslated strings). Both are **BLOCKING** under proofread-until-zero — the same standard Round 1 applied to single orphaned punctuation marks. Neither was introduced by the fix: both were present in the Round 1 artifacts (Round 1's residue scan covered only *added* strings for the core item and used a wordlist that missed `Compare` for the FR item). Both also appear in the corresponding `.text.md` exports, so the fix must be made at the source, not in the SVG alone.

### N-1 — BLOCKING — core (zh-cn) P8, item 103 note: English word `arrival` inside a Chinese explanation

- **File:** `files/weekly-report-w46-nl-core/svg/p8-toets.svg`, text element x=989, y=2210.12. Also in `2026-w46-nl-zh-cn.text.md`, item 103 explanation.
- **Wrong text (verbatim):** `103. B — 入城式是圣诞老人的隆重 arrival`
- The key letter B is correct; only the note wording is defective. `arrival` is not a Dutch word and is not cited from the article; it is the English translation of `aankomst` inserted into a Chinese sentence.
- **Uniqueness evidence:** all 10 other editions' item 103 notes are fully in their native language (DE `…festlicher Einzug`; EN `…festive arrival`; ES `…llegada festiva…`; FR `…l'arrivée festive…`; IT `…arrivo festoso…`; JA `…祝祭の到着…`; KO `…축제 도착…`; PT `…chegada festiva…`; RU `…праздничное прибытие…`; zh-tw `intocht 是辛特克拉斯的慶典進城`). Visible in the full-frame core P8 card view.
- **Suggested correct text** (minimal fix, same note style, no final `。` as in the original): `103. B — 入城式是圣诞老人的隆重到来` (fixer to confirm exact wording/fit; mirroring zh-tw's `慶典進城` as `庆典进城` would also be acceptable).

### N-2 — BLOCKING — FR P8, item 137 note: English verb `Compare` inside a French explanation

- **File:** `files/weekly-report-w46-nl-fr/svg/p8-toets.svg`, text elements x=1451, y=1930.48 (line 1) and y=1945.04 (line 2). Also in `2026-w46-nl-fr.text.md`, item 137 (`（Compare avec l'article page 3）`).
- **Wrong text (verbatim, two lines):** `137. Le journal de Sinterklaas passe chaque jour à 18 h 00. —` / `Compare avec l'article page 3`
- The translation key itself is correct; only the parenthetical note's first word is English. The EN edition legitimately has `Compare with…`; the FR transform evidently copied the EN note prefix.
- **Suggested correct text:** `Comparez avec l'article page 3` (imperative; `À comparer avec l'article page 3` also acceptable; fixer to confirm fit on the wrapped second line).

No other new or residual defect was found. The full native-language sweeps (script inventory, English-token scan, extended wordlist sweep, cross-language leak scan of distinctive native words) found **no other leaks**; false positives were adjudicated clean (frozen footer `LUCERNA DUTCH WEEKLY`; FR `festive`/`article`/`attention` are French words; ES/PT `original` is Spanish/Portuguese; PT `Complete` is the Portuguese imperative homograph, Round 1 precedent — clean; Dutch body words `is`/`in`/`of`/`over` are Dutch, not English residue; Dutch `week` is a Dutch word, not the English token).

## 4. Full re-gate summary (independently re-run)

- **Freeze** (`tools/freeze.py diff`): core self-diff +0/−0 all pages, added CJK 0. Core per-page CJK totals [196, 220, 141, 136, 217, 184, 379, 1144] — P2 220 (was 221) and P6 184 (was 186) reconcile exactly with F-2a (−1 char) and F-2b (−2 chars). Latin + RU editions (de/en/es/fr/it/pt/ru) with `--strict-cjk`: added CJK 0, edition CJK total 0. JA added CJK 3,341 (327 distinct; hiragana 1005, katakana 1161, han 1042, CJK punct 72, fullwidth 61; no other scripts). KO added 3,581 (3571 Hangul + 10 CJK punct; 0 Han). zh-tw added 1,238 (−3 vs Round 1's 1,241, reconciling E-2 −2 and E-3 −1); 0 simplified-only characters on the spot-list scan of zh-tw SVG texts (core P1 sanity check found 23 simplified characters, as expected for zh-cn).
- **P8** (`tools/p8.py`): core extract 150/150. All 10 fan-out compares CLEAN, missing=[], extra=0, keydiff=[137,138] (adjudicated above).
- **Occlusion** (`tools/occlusion_audit.py`, selftest OK on every run — all 6 planted classes fired, clean controls silent): 0 flags in all 11 edition-alone runs; 0 new flags in all 10 `--core` NEW-vs-core runs. All 21 JSONs verified programmatically (`flag_count=0`, `new_flag_count=0`). Occlusion is blind to the N-1/N-2 textual residues (no geometry defect), consistent with Round 1's blind-spot note.
- **Counts** (re-measured): total 150 in every edition. text.md bracketed items 142 (missing exactly the 8 range-header items 25–28, 141–144); levels from bracketed 43/72/27 + 4 A2 + 4 B2 = A2 47 / B1 72 / B2 31. Per-page totals 10/18/18/18/18/18/12/38. SVG stems 142, no missing, no dupes; SVG per-page standalone [10,14,18,18,18,18,12,34] + range headers = totals above. Core types: 完成句子 65, 单选 44, 判断对错 7, 造句 8, 完形单选 13, 翻译 4, 写作 1. (Manuscript-label note, not reader-facing: KO text.md merges choice+cloze as `객관식` 57 = 44+13 exactly; ES/FR/PT/EN text.md type labels use Chinese/English words while rendered SVG stems use native type words — verified FR `Compléter`/`Traduire`, PT `Traduza para o neerlandês`.)
- **Gloss:** text.md gloss blocks 5 per edition, counts 6/5/5/5/5 in every edition, identical Dutch headwords in identical order (P2: de lampion, delen, de mantel, de bedelaar, het erfgoed, het ledlampje; P3: het journaal, de flessenpost, de burgemeester, de stoet, de leeskring; P4: de groepsfase, de kwartfinale, ongeslagen, de interland, de stand; P5: het verlanglijstje, de verslaggever, de proef, stemmen, de aflevering; P6: de traditie, griezelen, de belangstelling, de achteruitgang, de deskundige). SVG headword presence verified per page in all 11 editions (all present).
- **P6 chart:** rects measured from SVG in all editions: x=1473, y=304/362/420/478, widths 160/100/80/60, height 18, fill `#3e4c2a` — values 40/25/20/15, scale 4 px/person. Chart labels frozen Dutch in all editions: `Ik loop met een lampion` 40, `Ik vier Halloween` 25, `Ik doe allebei` 20, `Ik blijf thuis` 15. Values at x=1863, beyond the longest bar end (1633) — no coverage.
- **P7 golden sentences:** 8/8 verbatim (whitespace-normalised) on P7 AND in P1–P6 body text in all 11 editions. Page tags in order Pagina 1,1,2,3,4,5,6,6 in all 11.
- **Model essay:** 89 words in all 11 text.md files, byte-identical text across all 11 editions, beginning `Maandag 9 november begint het Sinterklaasjournaal. Ik kijk elke dag om 18:00 uur naar NPO Zapp. … Wat een week vol licht!`
- **Kinsoku:** scan of core/JA/zh-tw for line-start closers (`。、，,」』）］｝〉》】､・.!?%)`) and line-end openers (`「『（［｛〈《【`): 0 hits. JA 0 true line-start closer hits, consistent with Round 1.
- **Badge/footer/images:** footers 8/8 pages and page lines 8/8 in all editions (y=2624). Images per page [1,1,1,1,0,0,0,0] in every edition; all 4 photo credits present and identical frozen Dutch `Foto: …` lines (Wim van Rossem/Anefo; Nationaal Archief; W. Punt/Anefo; Spaarnestad Photo). P1 pairing: core y=372 Dutch strapline (no distinct badge element — O-1 accepted, not re-raised); DE/ES/FR/IT keep strapline at y=372 + badge at y=568; EN/JA/KO/PT/RU/ZH-TW badge replaces strapline at y=372. Badge texts match KIT furniture strings. Masthead ink bounding-box: x range 26–1923 in the y=30..430 band in all 11 P1 cards — clearance holds on every edition.
- **W45 promises** (re-verified in rendered SVG text, all 11): Sinterklaas Amsterdam arrival Sun 15 Nov + Sint-Maarten Wed 11 Nov as lead topics; readers' corner = labelled editor's example (`Anna (voorbeeldbrief van de redactie)`) + Dutch disclosure (`nog geen echte brieven…`) + native-language disclosure in every edition; VOLGENDE WEEK box contains Germany result Mon 16 Nov in Berlin, pakjesavond Sat 5 Dec, letters/best P8 texts; VOL.4 promise carried; P2 EN JIJ box promises best entries in VOL.4.
- **PDF text layer** (pdftotext + pypdf, `pdf-check.log`): all 11 web PDFs 8 pages, 1462.5×2025.0 pt, text bytes 44,394–55,313 (>0), web ≤7 MB (largest: zh-tw 1,615,015 B), web vs print text identical in every edition. RU web text bytes 55,313 (matches the corrected KIT §9).
- **Weekday/date claims** verified independently (`TZ='Europe/Amsterdam' date -d`): 2026-11-09 Mon, 11-10 Tue, 11-11 Wed, 11-12 Thu, 11-13 Fri, 11-14 Sat, 11-15 Sun, 11-16 Mon, 12-05 Sat.
- **ABSTRACT.txt valid** in all 11 editions (see §1 F-1).

## 5. Cards viewed; non-defects recorded

- **Full-frame P1 + P8 cards viewed for all 11 editions** (core at full resolution; the other 10 at half-size downscales preserving whole-page layout): no overflow, overlap, missing glyphs/tofu, or missing image credits. RU P1 top-strip middle/right clusters have a clear gap, consistent with Round 1. No other visual defect found.
- **Changed pages viewed at full frame:** P2 core, P6 core, P6 zh-tw, P3 fr, P3 pt — all clean (see §1).
- **zh-tw P8 F-option vs model-text column** (fix worker's non-defect observation): checked by SVG coordinates — F options at x=1023 (option b line y=878.05); essay lines at x=1451 (y=872.625, 891.475), identical coordinates in the core. No overlap; occlusion TEXTX 0 flags confirms. The zone crop (`crops/zhtw-p8-f-essay.png`) was viewed: the two columns are clearly separated. **Non-defect, confirmed.**
- **Adjudicated non-defects not re-raised:** O-1 core badge (coordinator ruling: ACCEPTED — pairing via subtitle/strip/footers, W45 precedent); O-2 KO orphans `가.`/`요.` (precedent-matched, no action); O-3/O-4/O-5 (no action).
- **Observation O-R2-1 (non-blocking):** F-2b(b) tightened separator `兴趣· de` — source-level one-space inconsistency, no render defect (see §1 ruling). Recorded, not a defect.

## 6. Required next steps

1. Fix N-1 at the core source (text.md + build source) and N-2 at the FR source/transform. Do not patch SVGs alone.
2. Re-render the affected editions. If the core source change requires re-derivation, re-derive all fan-outs and re-verify byte-for-byte reproducibility (transforms FAILED: 0), taking care that the core note-string change propagates through the transform old-strings without altering any other string.
3. Full Round 3 independent re-proofread of all 11 editions (proofread-until-zero: any source change restarts the cycle). Round 3 must re-run the full gate set and the full native-language residue sweep, and must re-verify that the 9 editions passing here are unchanged apart from any intended re-derivation.
4. (Non-blocking, next KIT pass) Rewrite the stale KIT lines themselves (core §1 badge wording, JA freeze total 3,377, RU §7 55,344/809,351) instead of relying on the fix-record glosses.

**ROUND 2 FAIL (blocking defects: N-1 core P8 item 103 `arrival`; N-2 fr P8 item 137 `Compare`).**
