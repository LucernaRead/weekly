# FIX-REPORT — Lucerna Weekly W46 DE family, Round 1 fixes

- **Issue:** VOL.3, Mon 2026-11-09 – Sun 2026-11-15. Target German (DE). Press time 2 November 2026.
- **Verdict:** `hidden_files/w46/de-proofread-gates/proofreader-verdict-round1.md` (2026-11-03), ROUND 1 FAIL — all 11 editions blocked.
- **Fix worker:** 2026-11-03. All fixes applied AT THE SOURCE (build-dir `content*.py` / `svglib.py` + `ABSTRACT.txt`), fully re-rendered. No SVG/PDF was hand-edited. `.text.md` files were regenerated from the source manuscript (never hand-edited, never extracted from PDF).
- **Scope:** 11 editions: `2026-w46-de-en, -es, -fr, -it, -ja, -ko, -nl, -pt, -ru, -zh-cn, -zh-tw`. `files/weekly-report-w46-de-core/` is a DUPLICATE of the de-zh-cn edition, not a 12th edition; the per-edition dir is canonical. The core build dir (`hidden_files/weekly-report-w46-de-build/`) is the frozen-core record.
- **Result:** every verdict defect fixed; re-gates pass on the final artifacts (see §6). A Round 2 independent proofread follows — this re-gating does not replace it.
- **Seed record (proofreader's, not re-derived):** 150 exercises (A2 66 / B1 70 / B2 14); per-page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.

## 1. Method and build architecture

- Frozen core build: `hidden_files/weekly-report-w46-de-build/` (`bslib4.py`, `svglib.py`, `content12/34/56/7/8.py`, one-process `run.py`; `OUT` → `files/weekly-report-w46-de-core/svg`).
- Each fan-out build: `hidden_files/weekly-report-w46-de-<lang>-build/`, a copy of the core build with `OUT` repointed and a `transform.py` applied (whole-line/exact-literal replacements of Chinese explanation-layer strings only; German body text identical across all 12 build dirs). Core fixes were therefore applied to the same line in every build dir.
- The transform sources (`tr-*.py`, `en-pairs.json` under `hidden_files/w46/`) were NOT regenerated — source edits live in the build dirs only.
- Per-edition render/verify: `hidden_files/w46/de-<lang>/render.py` (cards PNG @1950 + print PDF via CairoSVG/pypdf + web PDF via `tools/webpdf.py`) and `verify.py` (one-process re-run, byte-identity, verbatim 8/8, furniture checks).
- Text export: `hidden_files/w46/export_textmd.py` (AST extraction from build-dir sources, in order; headers preserved verbatim).
- Every build was run SEQUENTIALLY (one at a time), each logging 150 exercises and 0 `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings. Final build logs: core/ja/ko/pt/zh-cn/zh-tw `*-run3.log`; es/fr/ru `*-run4.log` (run4 = occlusion spacing fixes, §5); en/it/nl `*-run.log`.
- Fix scripts (assertion-checked, exact occurrence counts): `hidden_files/w46/de-fix/apply_fixes.py` (88 content edits + 12 ABSTRACT rewrites, `FAILURES: 0`), `kinsoku_patch.py` (v1), `kinsoku_patch2.py` (v2), `/tmp/occl_patch.py` (occlusion spacing fixes, §5 — literals recorded in §5).
- Fix verifier: `hidden_files/w46/de-fix/verify_fixes.py` — 188 checks on the final SVGs + abstracts, **0 failures** (`verify-fixes3.log`). Checks: D-CORE-1 caption + P1/P4 facts, D-TOOLBOX incl. controls, D-IT-1, D-NL-1, D-RU-1, M-1, M-2, M-3, M-4 (JA fragment-based), T-1, D-PT-1 forbidden/required tokens + retained disclosure, D-ABSTRACT format/practice/banned per edition, GOLDEN sentences exactly 2×, P6 bars [340, 578, 782], lone-punctuation scan (all editions), kinsoku scan (CJK editions only, brackets-only END set).

## 2. Blocking defects

### D-CORE-1 — P4 photo caption misdates the Berlin game (frozen core, all 11)

- Source: `content34.py` in the core build dir and the same line in all 11 fan-out build dirs (caption call, P4).
- Before: `Die Nationalelf spielt in dieser Woche in Belgrad und Berlin.`
- After: `Die Nationalelf spielt in dieser Woche in Belgrad — am Montag danach in Berlin.`
- Grounds: the Berlin game (Germany–Netherlands) is Mon 16 Nov 2026, outside the issue week; the issue's own P1 caption and P4 article both say Berlin is "am Montag danach" / 16 Nov. The P4 credit line is untouched. Caption wrap simulated before the fix: old and new both 4 lines at 19pt serif, width 434, so `cy3`/`ey3` layout is unchanged. Verified against the P1 caption + P4 article facts in every edition (fix verifier) and visually on the core P4 card.

### D-ABSTRACT — news-learning framing in all 11 abstracts

- Coordinator ruling applied: SOP §9 itself sanctions "learn French by reading"-type phrasing, but the user's explicit 2026-10-28 rule banning news-learning framing governs — the STRICT gate stands. The SOP §9 example is a documentation inconsistency to align AFTER W46 ships; the SOP was not edited in this round.
- Format was otherwise PASS in all 11 (single line, 0 ASCII double-quotes, reader-native, practice facts present). Only the closing sentence was rewritten; facts/topics/levels/counts are otherwise verbatim. Abstract text appears on no rendered page.
- Before (verdict quotes): en `…learn German by reading real German news`; zh-cn `通过德国新闻学德语`; es/fr/it/ja/ko/nl/pt/ru equivalents in the same pattern.
- After (closing sentences, full tails replaced; each file single line + trailing newline, no ASCII double-quote asserted):
  - zh-cn / core: `150 道以本周话题为素材的练习。`
  - zh-tw: `150 道以本週話題為素材的練習。`
  - en: `150 exercises on this week's topics.`
  - es: `150 ejercicios sobre los temas de esta semana.`
  - fr: `150 exercices sur les sujets de cette semaine.`
  - it: `150 esercizi sui temi di questa settimana.`
  - ja: `今週の話題を素材にした150問の練習問題。`
  - ko: `이번 주 화제를 소재로 한 연습문제 150개.`
  - nl: `150 oefeningen over de onderwerpen van deze week.`
  - pt: `150 exercícios sobre os temas desta semana.`
  - ru: `150 упражнений по темам этой недели.`

### D-CORE-3 + M-5 — orphan punctuation / wrap punctuation (frozen core pattern)

Fixed at the WRAP level in `svglib.py` (see §4, kinsoku v1+v2). No content string was changed for any kinsoku/orphan defect.

- D-CORE-3: lone `。` element (x=1473, y=1175.88) under the UND SIE? Chinese line on P2, core/zh-cn/zh-tw renderings. Gone on the re-rendered core P2 card; scan 0 violations.
- M-5: JA P2 gloss dangling `（`; KO P2 leading `）`; ZH-CN/ZH-TW P6 line starting with `。`; core P8 note wraps (24 instances in the proofreader's scan). All 0 on the final scan.

### D-TOOLBOX — P7 `Es wird gespielt.` glossed as FUTURE (EN/ES/FR/IT/PT/RU)

Standing alone the form is PRESENT passive; the same page contrasts ex. 103 (future) vs ex. 104 (Passiv, key A). Source: each edition's `content7.py` toolbox gloss line. NL (`Er wordt gespeeld`), JA, KO were correct and untouched. Core/zh-cn `比赛将进行（被动）` is future-leaning but tagged （被动） — observation only, untouched.

| Edition | Before | After |
|---|---|---|
| en | `It will be played` | `It is played` |
| es | `Se jugará` | `Se juega` |
| fr | `Il sera joué` | `Il est joué` |
| it | `Si giocherà` | `Si gioca` |
| pt | `Vai ser jogado` | `Joga-se` |
| ru | `Будет сыграно` | `Играется` |

The ex. 103/104 contrast reads correctly on every re-rendered P7 (visually confirmed EN/ES/FR; fix verifier checks the gloss strings + controls). Note: toolbox gloss lines are absent from BOTH pre-fix and post-fix `.text.md` files — a pre-existing exporter coverage gap (`export_textmd.py` does not walk the wordbox entries), not a fix gap; toolbox fixes are verified at SVG level.

### D-IT-1 — IT only, P3 gloss noun/verb mismatch

- Source: IT `content34.py`. Before: `das Geschnatter = starnazzare`. After: `das Geschnatter = lo starnazzare` (nominalised infinitive, closest to the family's en `cackling` / fr `caquètement`; `il garrito` was the alternative). Visually confirmed on the IT P3 card.

### D-NL-1 — NL only, P6 gloss corrupted

- Source: NL `content56.py`. Before: `Uitleg — gedenken = herdenken · Kranzniederlegung = krans · stille Tag = stille dag · verbondenheid · verzoening.` After: `gedenken = herdenken · die Kranzniederlegung = kranslegging · der stille Tag = stille dag · die Verbundenheit = verbondenheid · die Versöhnung = verzoening.` (includes the M-2 full form `kranslegging` and `der` before `stille Tag`, parallel to the EN/core gloss). Visually confirmed on the NL P6 card.

### D-RU-1 — RU only, P7 NOCH EIN WORT truncated definition

- Source: RU `content7.py`. Before: `«das Geisterspiel» (Seite 4): Spiel ohne Zuschauer.` After: `«das Geisterspiel» (Seite 4): ein Spiel ohne Zuschauer im Stadion. Матч-призрак.` Visually confirmed on the RU P7 card (see also the §5 spacing follow-up this longer box required).

### D-KO-1 — KO only, three stray punctuation orphans

- Two lone `。` on P5 (x=1007/y=628.7 under the gloss box; x=527/y=2220.2 under the C-section bridge) + one lone `)` on P8 (x=989/y=1901, end of the Page-6 answers block, closing paren of item 100's note `(희생자 추모)`). All fixed by kinsoku re-wrap at source (§4); no stray punctuation node remains (element scan 0; both P5 sites visually confirmed clean on crops). The KO KIT §4 account is corrected in the KO fix record: its P1 bridge-gloss shortening did not remove these three orphans — they were still present in the Round 1 renderings.

### D-PT-1 — PT only, mixed tu/você address

- Decision: normalise to **você-form** (predominant in the edition's instructions), headers AND the P8 parenthetical consistently.
- Sources: PT `content12/34/56/7/8.py`. Headers `Lê/Escreve…` → `Leia/Escreva…`, `Escolhe` → `Escolha`, `Reescreve` → `Reescreva`, `Olha` → `Olhe`, `Junta` → `Junte`, `Usa` → `Use`, P7 `corrige-os` → você-form; M-3 invitations in você-form (see §3); P8 `(traduz para português/alemão)` → `(Traduza para o português/alemão)` alongside `Traduza para o português`.
- Retained deliberately: the readers'-corner disclosure `Enviem-nos as vossas para VOL.4!` — plural address to all readers, internally consistent (`Enviem` + `vossas`).
- **Follow-up miss (found by `verify_fixes.py`, fixed in this round):** two `e.bridge("Completa com as palavras do quadro.")` occurrences in PT `content56.py` (P5/P6 bridges) were missed by the first edit pass — only the `content34.py` copy had been edited. Both corrected to `Complete com as palavras do quadro.` (count asserted 2) before the final PT render; a sweep of all PT build sources for tu-forms found only infinitive labels (`Completar frases`) otherwise. PT `.text.md` now shows 5× `Complete com`, 0× `Completa com`. Visually confirmed on the PT P8 card; P5/P6 bridges confirmed in the final SVGs.
- Observation (NOT fixed, out of scope — see §7): one P8 line starts with `...)`, a pre-existing Latin-edition wrap above all P8 edits in flow order; the Round 1 kinsoku scan covered CJK editions only.

## 3. Minors

### M-1 — bare-German headers

Full glosses measured at 23pt bold sans do NOT fit the 412px available (box width 434, text at ix+22): es 543.7, fr 451.3, it 551.5, nl 503.8, pt 542.8, ru 577.5. Short glosses were used instead, each measured to fit (deviation from the verdict's "match the en pattern" wording, forced by layout — stated plainly):

| Edition | Header after | Measured width |
|---|---|---|
| es P7 | `DER WERKZEUGKASTEN · Útiles` | 369.2px |
| fr P7 | `DER WERKZEUGKASTEN · Outils` | 371.0px |
| it P7 | `DER WERKZEUGKASTEN · Attrezzi` | 389.9px |
| nl P7 | `DER WERKZEUGKASTEN · Werktuig` | 405.9px (6px margin; occlusion audit 0) |
| pt P7 | `DER WERKZEUGKASTEN · Caixa` | 365.2px |
| ru P7 | `DER WERKZEUGKASTEN · Ящик` | 369.3px |
| ja P7 | `DER WERKZEUGKASTEN · 道具箱` | 372.3px |
| ko P7 | `DER WERKZEUGKASTEN · 도구 상자` | 394.4px |

EN already had `· Toolbox` (untouched). RU P1 `IN DIESER AUSGABE`: the full gloss `· Содержание` measures 424.0px (over 412 — the KIT-documented shortening IS load-bearing); restored gloss `· В номере` (382.5px at 24pt) applied. Visually confirmed ES/FR/RU P7.

### M-2 — bare-noun `Kranzniederlegung` glosses

Full forms taken from the same editions' P8 key 97, gloss-sized:

| Edition | Before | After |
|---|---|---|
| es | `ofrenda` | `ofrenda floral` |
| fr | `gerbe` | `dépôt de gerbe` |
| it | `corona` | `deposizione di corone` |
| pt | `coroa` | `deposição de coroas` |
| ru | `венок` | `возложение венков` |
| nl | `krans` | `kranslegging` |

NL reasoning: `kranslegging` is the action noun parallel to en `wreath-laying`; P8 key 97 retains the fuller `een kransleggingsceremonie`. The ES KIT §4 `ofrenda` shortening is corrected in the ES fix record (full form restored).
Fit accommodation (spacing only, NO text change, in es/fr/it/pt/ru/nl `content56.py`): the full-form gloss wraps to 5 lines (was 4), adding 29.7px to the P6-main Flow (cols 0–2, top 200, bottom 1080), which ends at y=1062 with 18px slack — a 11.7px overflow. The final German P6 para `gap=0` (was default 10) + the P6 gloss call `gap=0` (was default 12). Predicted end y=1069.7; confirmed on rebuild: P6-main ends y=1070 in the six editions, 1062 in the others; zero FLOW OVERFLOW / HEAD TOO WIDE. Synonym compressions were simulated first and rejected: they save only ~40–55px of width and do not drop a line, so they cannot fix fit (box height depends only on line count).

### M-3 — UND SIE? invitations thinned (es/fr/it/nl/pt/ru)

Restored to the full two-question + write-two-sentences form on P3/P4/P5 (P2 already matches the EN/core one-question pattern in all editions — P2 unchanged except PT address form). Each old string occurred 2× per file (eh height formula + rendered para); both updated. Full before/after table (gloss strings only; the German `etvous` paragraph is frozen and unchanged):

| Ed. | Page/file | Before | After |
|---|---|---|---|
| es | P3/P4 `content34.py` | `¿Hiciste un farolillo? ¡Escribe dos frases en alemán!` | `¿Hiciste un farolillo? ¿Qué canciones cantan los niños en tu país? ¡Escribe dos frases en alemán!` |
| es | P3/P4 `content34.py` | `¿Fútbol o fútbol americano? ¿Quién gana? ¡Dos frases!` | `¿Fútbol o fútbol americano? ¿Quién gana en Belgrado? ¡Escribe dos frases en alemán!` |
| es | P5 `content56.py` | `¿Un farolillo de niño? ¿Tu canción? ¡Dos frases!` | `¿Hiciste un farolillo de niño? ¿Qué canción cantas en noviembre? ¡Escribe dos frases en alemán!` |
| fr | P3/P4 `content34.py` | `Tu as fait une lanterne ? Écris deux phrases en allemand !` | `Tu as fait une lanterne ? Quelles chansons chantent les enfants dans ton pays ? Écris deux phrases en allemand !` |
| fr | P3/P4 `content34.py` | `Foot ou foot US ? Qui gagne ? Deux phrases en allemand !` | `Foot ou foot US ? Qui gagne à Belgrade ? Écris deux phrases en allemand !` |
| fr | P5 `content56.py` | `Une lanterne enfant ? Ta chanson ? Deux phrases en allemand !` | `As-tu fait une lanterne enfant ? Quelle chanson chantes-tu en novembre ? Écris deux phrases en allemand !` |
| it | P3/P4 `content34.py` | `Hai fatto una lanterna? Scrivi due frasi in tedesco!` | `Hai fatto una lanterna? Quali canzoni cantano i bambini nel tuo paese? Scrivi due frasi in tedesco!` |
| it | P3/P4 `content34.py` | `Calcio o football americano? Chi vince? Due frasi!` | `Calcio o football americano? Chi vince a Belgrado? Scrivi due frasi in tedesco!` |
| it | P5 `content56.py` | `Una lanterna da bambino? La tua canzone? Due frasi!` | `Hai fatto una lanterna da bambino? Quale canzone canti a novembre? Scrivi due frasi in tedesco!` |
| nl | P3/P4 `content34.py` | `Heb je een lantaarn gemaakt? Twee Duitse zinnen!` | `Heb je een lantaarn gemaakt? Welke liedjes zingen kinderen in jouw land? Schrijf twee Duitse zinnen!` |
| nl | P3/P4 `content34.py` | `Voetbal of American football? Wie wint? Twee zinnen!` | `Voetbal of American football? Wie wint er in Belgrado? Schrijf twee Duitse zinnen!` |
| nl | P5 `content56.py` | `Een lantaarn als kind? Jouw lied? Twee zinnen!` | `Heb je als kind een lantaarn gemaakt? Welk lied zing jij in november? Schrijf twee Duitse zinnen!` |
| pt | P3/P4 `content34.py` | `Fizeste uma lanterna? Escreve duas frases em alemão!` | `Fez uma lanterna? Que canções cantam as crianças no seu país? Escreva duas frases em alemão!` |
| pt | P3/P4 `content34.py` | `Futebol ou futebol americano? Quem ganha? Duas frases!` | `Futebol ou futebol americano? Quem ganha em Belgrado? Escreva duas frases em alemão!` |
| pt | P5 `content56.py` | `Uma lanterna em criança? A tua canção? Duas frases!` | `Fez uma lanterna em criança? Que canção canta em novembro? Escreva duas frases em alemão!` |
| ru | P3/P4 `content34.py` | `Вы делали фонарик? Напишите два предложения!` | `Вы делали фонарик? Какие песни поют дети в вашей стране? Напишите два предложения!` |
| ru | P3/P4 `content34.py` | `Футбол или американский футбол? Кто победит? Два предложения!` | `Футбол или американский футбол? Кто победит в Белграде? Напишите два предложения!` |
| ru | P5 `content56.py` | `Фонарик в детстве? Ваша песня? Два предложения!` | `Вы делали фонарик в детстве? Какую песню вы поёте в ноябре? Напишите два предложения!` |

JA/KO/ZH-TW keep their fuller invitations (untouched); EN untouched. Visually confirmed ES P3, IT P3. The restored boxes overflowed two fixed page stacks — fixed by spacing only, see §5 (no M-3 text was re-shortened).

### M-4 — JA/KO P8 translation-register mix

Majority rule, one edit each, in `content8.py`:
- JA → PLAIN (137 plain, 139 plain, 138 polite): key 138 `水曜日にランタンを作ります。` → `水曜日にランタンを作る。` Confirmed via P8 SVG grep (`作ります` absent from all JA SVGs; key 138 wraps as `水曜日にランタンを` / `作る。`).
- KO → POLITE (138/139 polite, 137 plain): key 137 `카니발은 11시 11분에 쾰른에서 개막한다.` → `카니발은 11시 11분에 쾰른에서 개막합니다.`

### M-6 — KO P1 flow quirk

Exercise 1 sat in the middle column (x=599), 2–6 in the right column (x=1061); JETZT ÜBEN head at x=527, y=1677.125. Fix: the KO P1 bridge gloss (`content12.py`) was lengthened from 2 lines to 4 by adding `· die Bundesliga＝분데스리가 · die Nationalmannschaft＝국가대표팀` (both words appear in the P1 article; simulated with the patched `wrap()` first). Result matches EN geometry exactly: head x=527 y=1736.575, ex. 1–6 all x=1061 with EN-identical baselines (848.6/971.6/1094.5/1217.4/1340.4/1463.3). Visually confirmed on the KO P1 card; holds on the final render.

### T-1 — ZH-TW P8 header separator

- Source: ZH-TW `content8.py`. Before: `Alle Antworten unten auf dieser Seite 答案在本版下方`. After: `Alle Antworten unten auf dieser Seite — 答案在本版下方` (band subtitle width 782.9px, end-anchored, no same-baseline conflict). Confirmed in SVG text and the P8 band crop.

### Item 11 (docs) — stale builder freeze archives for en/nl/ru

Regenerated from the shipped SVGs on 2026-11-03 (same `freeze.py diff` invocation, JSON + stdout text into `hidden_files/w46/de-{en,nl,ru}-freeze.json/.txt`; all exit 0, added CJK 0). The stale archives were copied aside first into `de-fix/stale-de-{en,nl,ru}-freeze.json/.txt`. The regenerated `.txt` diffs vs stale are small string-count shifts from the Round 1 fixes (re-wraps changing string splits) — e.g. en P4 +26→+25 strings, P8 −137→−138; nl P3 +41→+42; ru P3 +45→+46. Regeneration recorded in the en/nl/ru KITs.

### DO NOT CHANGE — honoured

O-1 (core/zh-cn keep the German subtitle slot, grey #57523f, no distinct badge line); the P8 key-67 note; W45-promise wording; all frozen German body text beyond D-CORE-1/D-CORE-3/M-5.

## 4. Kinsoku fix — v1, follow-up finding, v2

`wrap()` in `svglib.py` is greedy (Latin words whole, CJK per char; tokens are maximal runs of non-CJK non-space chars, so `76.` is ONE token, plus each CJK char and each space as its own token; a space token at a break is dropped). It is used both for drawing and height measurement, so wrap changes stay self-consistent. Wrap simulations with each edition's real fonts reproduced every proofreader orphan exactly before patching.

**v1** (`de-fix/kinsoku_patch.py`, log `kinsoku_patch.log`): post-processing added to the CJK build `svglib.py` copies — (a) START repair (oidashi, copied from the JA build): a line must not start with closing punctuation, pull the previous line's last char down, line count unchanged; (b) NEW END repair: a line must not end with an opening bracket, push it to the next line's head, shedding trailing glyphs forward (NO_START pairs together) if the receiving line exceeds `max_w`; (c) JA seam repair (cascade, SEAM_SLACK=28). NO_START sets: core/zh-cn/zh-tw `。、，．！？：；）」』】})`; KO adds `,.:;!?`; JA keeps its existing set verbatim. NO_END (all): `（(［｛〈《「『`. Applied to core, zh-cn, zh-tw, ko (full block) and ja (END pass only). Latin/Cyrillic builds untouched. Verified on copies first (`de-fix/scratch-svglib/`): all reproduced orphans fixed, zero remaining START/END/lone-punct flags, no line over `max_w+28`, line counts preserved.

**Follow-up finding (fix verifier, first run 188/195 PASS):** a NEW orphan the proofreader's pre-fix scan never flagged — a core/zh-cn P8 keys-paragraph line starting with ASCII `.` (`.Die Kinder freuen sich, weil …`, previous line ending `· 76`). Root cause proven by simulation: the RAW greedy `wrap()` is correct (line ends `· 76.`, 431.0px ≤ 434); the v1 END-pass shedding loop shed a single `.` off `76.` when the receiving line overflowed, splitting the token. Three other first-run flags were triaged as non-defects: the JA P1 line ending `・` (byproduct of the pre-existing JA START repair; `・` is not an opening bracket); core/zh-cn P7 lines ending `……` (`…` U+2026 is not an opening bracket); the PT P8 `...)` line-start (pre-existing Latin wrap, out of scope — §2/§7).

**v2** (`de-fix/kinsoku_patch2.py`, log `kinsoku_patch2.log`): module-level helpers before `def wrap()` in all 5 CJK `svglib.py` files — `_kinsoku_shed_piece(line, no_start)` (NO_START glyph goes with the glyph before it; a trailing ASCII-punctuated Latin token goes whole, never splitting `76.`; else one glyph) and `_kinsoku_join_piece(piece, next)` (restores the space the raw wrap consumed at the break when a punctuated Latin token rejoins Latin text, i.e. `76.` + `Die` → `76. Die`; never inserts a space before CJK). NO_START sets extended with ASCII `,.:;!?` for core/zh-cn/zh-tw and JA. Shedding loops replaced to use the helpers, with a guard never emptying a donor line. A final polish block (START sweep then END sweep, single-glyph moves only, receiving lines within `max_w + SEAM_SLACK`) was inserted before `wrap()`'s return. A helper-order bug found during simulation (NO_START-pair rule checked before the punctuated-token rule shed `6.` and produced `· 7` / `6. Die`) was fixed by reordering (punctuated-token first) in all 5 files and in the patch record. Re-simulation of the exact core P8-keys paragraph: zero violations, line 3 ends `·` (422.1px), line 4 starts `76. Die Kinder…` (433.6px, space restored). Backups of the pre-v2 (v1) files: `de-fix/svglib-pre-v2/`. The corrected `verify_fixes.py` uses brackets-only OPEN_END, CLOSE_START with ASCII punct (matching the proofreader's KO flags), and scopes the kinsoku check to CJK editions only. Final scan on shipped SVGs: 0 violations; the core P8 keys block was visually confirmed clean at full frame (`· 75. Stern…` / `76. Die Kinder freuen sich, weil St. Martin kommt.…`).

## 5. Occlusion follow-up — spacing-only recoveries for the restored boxes

The first full re-gate (gates-run.log) showed 4 occlusion failures caused by the mandated restorations: the full M-3 invitations (and the D-RU-1 definition) need one more line than the thinned versions the stacks were built around, and the P3/P4/P7 stacks have fixed bottoms (exercises rule / SPIELPLAN table / SÄTZE rule). All five sites were fixed by SPACING ONLY — no restored text was re-shortened, no frozen text touched. Measured geometry drove each fix; predicted positions matched the rebuilds exactly.

- **ES/PT/RU P4** (COVER: last gloss line `alemán!` / `em alemão!` / `предложения!` at baseline y=1162.82 covered 39–58% by the SPIELPLAN first-row rect at y=1156; undsie box y=864.9 h=320.12 bottom=1185.02; IT/NL/EN flush at bottom 1156.02): in each edition's `content34.py` P4 block — caption gap `ey3 = cy3 + 26` → `+ 10`; German→gloss inter-para `+ 10` → `+ 2` and gloss offset `yy3 + 20` → `yy3 + 15` (P4 occurrence only, anchored on the P4 gloss string); eh constant `140` → `127`. Net: box up 16px, gloss lines up 29px, box bottom 1156.02, last gloss baseline 1133.82 — exactly the EN/IT/NL geometry. Confirmed visually (ES/PT cards: full gloss visible, box flush above the table).
- **FR/RU P3** (LINEX: `genügt.` baseline 1623.66 struck by the exercises rule at y=1608; BOXTITLE artifact: the grown TIPP box bottom 1643.19 overlapped the exercises-head subtitle's y-range): in each edition's `content34.py` — the three col-3 gaps `26` → `14` (facts→vocab), `14` (vocab→undsie), `10` (undsie→tipp). Net: TIPP box up 40px (bottom 1603.19, `genügt.` baseline 1583.66, clear of the rule). Confirmed visually (FR/RU cards).
- **RU P7** (LINEX: `Матч-призрак.` baseline 1522.72 struck by the SÄTZE rule at y=1508; the LESERBRIEFE box above has only ~5.7px slack, so its height could not be trimmed): in RU `content7.py` — box gap `wy3 = ry + rh + 16` → `+ 8`; NOCH EIN WORT para offset `wy3 + 78` → `wy3 + 68`; para leading `1.42` → `1.28`. Net: gloss baseline 1498.98, clear of the rule; box bottom 1528.5. The gold rule now passes through the box's empty bottom padding below the gloss (no text struck or obscured — same class as the EN P3 box/rule touch); recorded here plainly. Confirmed visually.
- Rebuilt es/fr/pt/ru (`*-run4.log`, 150 exercises, 0 warnings), re-rendered + re-verified (`*-render3.log`, `*-verify3.log`, exit 0), re-gated: occlusion **0 flags in all 12 editions** (see §6).

## 6. Re-gate results (final artifacts, 2026-11-03)

Gate runner: `de-fix/run_gates.sh` (`gates-run2.log`; first run `gates-run.log` is the pre-§5 run). Freeze: `tools/freeze.py diff --strict-cjk` (logs + JSONs `freeze-<ed>.log/.json`). P8: `tools/p8.py compare --total 150` (`p8-<ed>.log/.json`). Occlusion: `tools/occlusion_audit.py` incl. selftest (`occlusion-<ed>.log/.json`). Counts: proofreader's `count_exercises.py` (`counts.json/.log`). PDF text: `de-fix/pdf_text_check.py` (`pdf-text.log`).

| Edition | Freeze | P8 compare | Occlusion | Counts |
|---|---|---|---|---|
| core (dup) | exit 0 | CLEAN 150/150, keydiff [] | 0 flags | 149 + 150 |
| en | exit 0, added CJK 0 | CLEAN 150/150, keydiff [137, 138, 139, 140, 150] | 0 flags | 149 + 150 |
| es | exit 0, added CJK 0 | CLEAN 150/150, keydiff [137, 138, 139, 140, 150] | 0 flags | 149 + 150 |
| fr | exit 0, added CJK 0 | CLEAN 150/150, keydiff [137, 138, 139, 140, 150] | 0 flags | 149 + 150 |
| it | exit 0, added CJK 0 | CLEAN 150/150, keydiff [137, 138, 139, 140, 150] | 0 flags | 149 + 150 |
| ja | exit 1 by design, +3275 added CJK (adjudicated reader Japanese; −1 vs Round 1 +3276, explained by the M-4 `作ります`→`作る` removal) | CLEAN 150/150, keydiff [137, 138, 139, 140, 150] | 0 flags | 149 + 150 |
| ko | exit 1 by design, +3213 added CJK (adjudicated reader Korean; +17 vs Round 1 +3196: +10 M-6 bridge gloss, +7 M-4 polite endings) | CLEAN 150/150, keydiff [137, 138, 139, 140, 150] | 0 flags | 149 + 150 |
| nl | exit 0, added CJK 0 | CLEAN 150/150, keydiff [137, 138, 139, 140, 150] | 0 flags | 149 + 150 |
| pt | exit 0, added CJK 0 | CLEAN 150/150, keydiff [137, 138, 139, 140, 150] | 0 flags | 149 + 150 |
| ru | exit 0, added CJK 0 | CLEAN 150/150, keydiff [137, 138, 139, 140, 150] | 0 flags | 149 + 150 |
| zh-cn | exit 0, +0/−0 vs core (identical) | CLEAN 150/150, keydiff [] | 0 flags | 149 + 150 |
| zh-tw | exit 1 by design, +1043 added CJK (adjudicated Traditional; exact match to Round 1) | CLEAN 150/150, keydiff [137, 138, 139, 140, 150] | 0 flags | 149 + 150 |

- **P8 keydiff correction:** the measured set is [137, 138, 139, 140, 150] in all 10 fan-outs. Key 140 is the fourth E-section translation item (core `翻译 我周日看 NFL 比赛。（译成德语）` vs en `Translate into German I watch the NFL game on Sunday. (translate into German)`), the same legitimate class as 137–139; the verdict text listed [137, 138, 139, 150], omitting 140. Key 150 is the open-task label. No added/removed German tokens: the only long removed German string is the P1 subtitle slot → pairing badge (documented furniture).
- **Counts:** 149 numbered scanned + writing item 150 = 150 in every edition; per-page 10/18/18/18/18/18/12/37 (+150 on P8 = 38); level chips A2 57 / B1 70 / B2 14 / 8 untagged (113–120) — identical to the proofreader's `counts.json` for all 12 editions (the seed A2 66 = 57 chipped + 8 untagged + item 150).
- **PDF text:** 0 failures. Every web PDF ≤ 7 MB, `pdftotext` bytes > 0 for web + print, web/print normalised text EQUAL (see §7 for bytes; RU web 112,527 vs print 112,528 raw bytes, equal after normalisation, as designed).
- **Other checks:** P6 bars 782/578/340px = 46/34/20 (sum 100); MUSTER 84 words; P7 golden sentences exactly 2× each; P8 separators 8 half-width paren keys present; badge present; verify.py per edition exit 0 (150, verbatim 8/8, SVGs byte-identical on re-run, footer/page lines 8/8).
- **Visual checks at full frame** (card PNGs): viewed on the FINAL renders — core P8 keys block (76 fix), ES P4 / PT P4 / FR P3 / RU P3 / RU P7 (§5 spacing sites, all clean, no text struck or covered). Viewed on the first renders and re-verified on the final SVGs by the element/kinsoku scan (0 violations) and string checks — core P2 (kinsoku clean), core P4 (caption), EN P7 (toolbox), ES P7 (M-1 + toolbox), ES P6 (M-2 gloss + gap), ES P3 (M-3), FR P7 (M-1 + toolbox), IT P3 (D-IT-1 + M-3), JA P2 (kinsoku `（`), KO P1 (M-6; head/exercise geometry re-measured on the final SVG: head x=527 y=1736.575, ex. 1–6 all x=1061, EN-identical baselines), KO P5 gloss/bridge crops (orphans gone), NL P6 (D-NL-1), PT P8 (você-form), ZH-TW P8 band (T-1 separator; also string-checked on the final SVG). Verified by scan/simulation only (not re-viewed at full frame after v2): JA P1 Fragen box (wrap simulation, zero bracket violations; JA web PDF byte-identical to the v1 render), KO P8 orphan site, ZH-CN/ZH-TW P6 + P8 re-wraps, ZH-CN P2/P4. No overflow/overlap, no lone punctuation, no new orphan introduced anywhere in the scanned set.

## 7. Final per-edition file inventory

Per edition: 8 SVGs + 8 card PNGs + print PDF + web PDF + `<slug>.text.md` + `ABSTRACT.txt` + `WEEKLY-KIT.md` (with the §6/§9 fix record appended). Web PDFs are the repo-shipped PDFs (`<slug>.pdf` name in the repo; local print masters are larger). `.text.md` regenerated 2026-11-03 (`textmd-regen2.log`): 695 items per edition; golden 8/8 for core/zh-cn. Diffs vs the pre-fix `.text.md` files (`de-fix/old-textmd/`) show ONLY fix lines (caption, M-1 headers, M-2 glosses, M-3 invitations, M-4 register lines, D-IT-1, D-NL-1, D-RU-1, RU P1 gloss, T-1 separator, PT você forms + parentheticals, KO bridge). Pre-fix SVG hashes: `de-fix/pre-fix-svg-hashes.json` (96 SVGs).

| Edition (slug) | `.text.md` bytes | Web PDF bytes | Web `pdftotext` bytes | Print PDF bytes |
|---|---|---|---|---|
| core = 2026-w46-de-zh-cn (dup dir) | 37,769 | 1,670,976 | 101,893 | 16,578,272 |
| 2026-w46-de-en | 39,149 | 1,064,527 | 109,368 | 4,042,817 |
| 2026-w46-de-es | 40,339 | 1,072,192 | 109,052 | 4,046,980 |
| 2026-w46-de-fr | 40,310 | 1,070,381 | 110,734 | 4,103,392 |
| 2026-w46-de-it | 39,886 | 1,063,875 | 113,365 | 4,041,774 |
| 2026-w46-de-ja | 40,519 | 1,751,022 | 104,728 | 18,320,241 |
| 2026-w46-de-ko | 39,689 | 1,402,710 | 105,582 | 9,079,304 |
| 2026-w46-de-nl | 39,664 | 1,067,037 | 109,947 | 4,101,965 |
| 2026-w46-de-pt | 40,066 | 1,075,707 | 109,621 | 4,049,201 |
| 2026-w46-de-ru | 45,792 | 1,105,562 | 112,527 | 3,975,824 |
| 2026-w46-de-zh-cn | 37,769 | 1,670,976 | 101,893 | 16,578,272 |
| 2026-w46-de-zh-tw | 37,707 | 2,038,468 | 101,973 | 16,633,809 |

## 8. Deviations from the verdict wording (stated plainly)

1. **M-1 short glosses** instead of the full `· Toolbox`-pattern glosses in es/fr/it/nl/pt/ru — the full forms do not fit the 412px slot (measured 451–578px). Short glosses measured to fit; RU P1 uses `· В номере` because `· Содержание` (424px) does not fit.
2. **M-2 spacing accommodation** (gap=0 on the final P6 para + gloss call) — the mandated full-form gloss adds a 5th line the flow cannot hold; no text was shortened instead.
3. **NL `kranslegging`** instead of the full ceremony form — action noun parallel to en `wreath-laying`; P8 key 97 keeps the fuller form.
4. **Kinsoku v2 follow-up**: the v1 END repair introduced one new wrap (split `76.`); v2's token-aware shedding + polish fixed it and re-verified the whole CJK set. Two wraps total were changed by v2 beyond v1 (the `76.` line and its neighbours); no content strings changed.
5. **§5 spacing recoveries**: the verdict's M-3/D-RU-1 restorations overflowed fixed page stacks (P3 rule, P4 table, P7 rule); recovered by spacing only (gaps/offsets/leading/eh constants listed in §5). No restored text was re-shortened.
6. **P8 keydiff [137, 138, 139, 140, 150]** vs the verdict's [137, 138, 139, 150] — 140 is the fourth E-section item, same legitimate class (§6).
7. **PT P8 `...)` line-start left as-is** — pre-existing Latin wrap, out of the Round 1 scan scope; needs a verdict-level decision if Round 2 flags it.
8. **No fix could not be applied as specified.** Every verdict defect (blocking + minors + T-1 + docs item 11) is fixed; items 1–7 above are method deviations, not omissions.

## 9. Records and logs

- Fix record appended to all 11 edition KITs (`## 6. Round 1 fix record`) and the core KIT (`## 9`), with defect/fix quotes and per-edition re-gate evidence.
- This report: `hidden_files/w46/de-fix/FIX-REPORT.md`.
- Logs/JSONs under `hidden_files/w46/de-fix/`: per-edition run/render/verify logs (final: `*-run3.log`/`*-run4.log`, `*-render2.log`/`*-render3.log`, `*-verify2.log`/`*-verify3.log`; en/it/nl `*-run/render/verify.log`); `run_gates.sh`, `gates-run.log` (pre-§5), `gates-run2.log` (final); `freeze-*.log/.json`, `p8-*.log/.json`, `occlusion-*.log/.json`, `counts.json/.log`, `pdf-text.log`; `verify_fixes.py` + `verify-fixes.log`/`verify-fixes2.log`/`verify-fixes3.log`; `apply_fixes.py` + `apply_fixes.log`; `kinsoku_patch.py/.log`, `kinsoku_patch2.py/.log`; `svglib-pre-v2/` backups; `scratch-svglib/` simulation copies (do not ship); `old-textmd/` pre-fix `.text.md` files; `pre-fix-svg-hashes.json`; `stale-de-{en,nl,ru}-freeze.json/.txt`; `textmd-regen.log`, `textmd-regen2.log`.
- Nothing was pushed, inserted, or posted: work is local only (`~/workspace/weekly-git` untouched, `index.json` untouched, no Discord). A Round 2 independent proofread follows.
