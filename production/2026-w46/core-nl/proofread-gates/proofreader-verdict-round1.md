# Independent Proofread — Verdict Round 1

## Lucerna Weekly W46 · NL family · Issue Mon 2026-11-09 – Sun 2026-11-15, 2026

- Proofreader: independent subagent (did NOT build these editions). Proofreader only: nothing was fixed, re-rendered, or edited; no edition file was touched; `~/workspace/weekly-git` untouched; `index.json` untouched; nothing pushed, inserted, or posted.
- Gate: proofread-until-zero. This verdict is a hard shipping gate.
- Date of proofread: Mon 2026-11-02 / Tue 2026-11-03 EST (re-runs executed by the proofreader; all gates re-run independently, builder outputs not trusted).
- Scope: all 11 NL-target editions, one per reader-native language:
  `2026-w46-nl-de`, `-en`, `-es`, `-fr`, `-it`, `-ja`, `-ko`, `-pt`, `-ru`, `-zh-cn`, `-zh-tw`.
- Directory resolution: the frozen core directory `files/weekly-report-w46-nl-core/` IS the `2026-w46-nl-zh-cn` edition (Dutch text, Simplified Chinese explanations; text export `2026-w46-nl-zh-cn.text.md`). There is no separate `weekly-report-w46-nl-zh-cn/` directory. No double-counting.

## Final verdict

**ROUND 1 FAIL (blocking defects: F-1 abstract news framing in all 11 editions; F-2a core P2 lone 。; F-2b core + zh-tw P6 gloss lone 。; E-1 fr + pt P3 stranded "3."; E-2 zh-tw P6 chart line-start 。; E-3 zh-tw P8 H-intro lone 。)**

No edition is shippable as-is. After fixes, a FULL re-proofread of all 11 editions is required (SOP: proofread-until-zero, no sampling).

## Per-edition PASS/FAIL

| Edition (slug) | Verdict | Blocking defects |
|---|---|---|
| 2026-w46-nl-zh-cn (core) | **FAIL** | F-1, F-2a, F-2b |
| 2026-w46-nl-de | **FAIL** | F-1 |
| 2026-w46-nl-en | **FAIL** | F-1 |
| 2026-w46-nl-es | **FAIL** | F-1 |
| 2026-w46-nl-fr | **FAIL** | F-1, E-1 |
| 2026-w46-nl-it | **FAIL** | F-1 |
| 2026-w46-nl-ja | **FAIL** | F-1 |
| 2026-w46-nl-ko | **FAIL** | F-1 |
| 2026-w46-nl-pt | **FAIL** | F-1, E-1 |
| 2026-w46-nl-ru | **FAIL** | F-1 |
| 2026-w46-nl-zh-tw | **FAIL** | F-1, F-2b, E-2, E-3 |

## Defect list (complete, with evidence)

### A. Frozen-core defects (origin in the frozen NL core; inherited where noted)

#### F-1 — BLOCKING — ABSTRACT news framing, all 11 editions

Every `ABSTRACT.txt` is single-line, contains 0 ASCII double-quotes, is written in the reader's native language, and names real topics/dates/levels/counts — but every one ends with news-framing equivalent to the forbidden "learn Dutch from this week's news" (task item 7; standing rule 2026-10-28: abstracts must use PRACTICE framing, never news framing — "用一周新闻学X / 以新闻学 / 读新闻学 / 用报纸学" forbidden; rewrite as "以本周话题为素材的 N 道练习" equivalent).

Required fix direction: reframe the closing clause in each native language as practice framing, e.g. "150 practice exercises on this week's topics" equivalent, keeping the verified facts/dates/levels/counts. The abstract facts themselves are correct (the Germany match is preview-only content, correctly included as a topic).

Evidence — verbatim closing clause of each `ABSTRACT.txt` (file: `<edition-dir>/ABSTRACT.txt`, single line):

- zh-cn (core): `…适合学荷兰语的读者通过荷兰新闻学荷兰语。` — "learn Dutch through Dutch news".
- de: `…die Niederländisch durch niederländische Nachrichten lernen.`
- en: `…for readers learning Dutch through Dutch news.`
- es: `…para aprender neerlandés con las noticias neerlandesas.`
- fr: `…pour apprendre le néerlandais par les nouvelles néerlandaises.`
- it: `…per imparare l'olandese con le notizie olandesi.`
- ja: `…オランダのニュースからオランダ語を学ぶ。`
- ko: `…네덜란드 뉴스로 네덜란드어를 배웁니다.`
- pt: `…para aprender neerlandês com as notícias neerlandesas.`
- ru: `…для изучения голландского по голландским новостям.`
- zh-tw: `…用荷蘭新聞學荷蘭語。`

#### F-2a — BLOCKING — Core P2 EN JIJ box: lone 。 orphan (core only)

File: `files/weekly-report-w46-nl-core/svg/p2-leven.svg`, text element x=1473, y=1416.64, 20.5pt (approx), content exactly `。`, on its own line below the invitation lines (y=1359.84, y=1388.24, ending `…寄给编辑部`). Visually confirmed in crop `crops/core-p2-orphan.png`: a solitary 。 sits alone at the bottom-left of the box. Correct text: the 。 must join the preceding line (`…写两句荷兰语寄给编辑部。`), no orphan line.

#### F-2b — BLOCKING — Core + zh-tw P6 gloss: lone 。 orphan (frozen-core text, inherited identically by zh-tw)

File: `files/weekly-report-w46-nl-core/svg/p6-verdieping.svg` AND `files/weekly-report-w46-nl-zh-tw/svg/p6-verdieping.svg`, text element x=1007, y=327.675, content exactly `。`, on its own line after the gloss line `…de deskundige 专家/專家` (y=297.95). Visually confirmed in crops `crops/core-p6-gloss-orphan.png` and `crops/zhtw-p6-gloss-orphan.png`. Correct text: the 。 must join the gloss line. NOTE: core KIT §8(7) claims this P6 gloss orphan was fixed — REFUTED, the lone 。 remains in the shipped core (see KIT adjudications).

### B. Edition-specific defects

#### E-1 — BLOCKING — FR + PT P3 bridge (section D · REKENEN): stranded "3." on its own line

Files: `files/weekly-report-w46-nl-fr/svg/p3-cultuur.svg` and `files/weekly-report-w46-nl-pt/svg/p3-cultuur.svg`, text element x=989, y=1984.225, 20.5pt, content exactly `3.`, alone on line 2 of the bridge.

- FR line 1: `Calcule: réponds avec les chiffres de la page` — line 2: `3.`
- PT line 1: `Calcula: responde com os números da página` — line 2: `3.`
- Control (EN, correct): line 2 reads `page 3.` together; ES likewise `página 3.` together.

Visually confirmed in crops `crops/fr-p3-orphan3.png`, `crops/pt-p3-orphan3.png` (vs control `crops/en-p3-orphan3.png`). Correct text: re-wrap so the page number joins the preceding line (`…de la page 3.` / `…da página 3.`), as in EN/ES. Consequence: exercise stems below shift down ~30px; no overlap was found by geometry (occlusion 0 flags), but the stranded number is a visible typographic defect under the zero-defect gate.

#### E-2 — BLOCKING — ZH-TW P6 chart explanation: line starting with 。

File: `files/weekly-report-w46-nl-zh-tw/svg/p6-verdieping.svg`, text element x=1473, y=685.28, content `。問題：11 月 11 日前後你做什麼？（100 位年` — a line beginning with 。, following `練習數據：僅供練習的虛構數字，不是真實調查` (y=660.86). The core equivalent wraps cleanly. Visually confirmed in crop `crops/zhtw-p6-chart-orphan.png`. Correct text: re-wrap so 。 closes the preceding line (no line may start with 。).

#### E-3 — BLOCKING — ZH-TW P8 H-intro: lone 。 orphan

File: `files/weekly-report-w46-nl-zh-tw/svg/p8-toets.svg`, text element x=1451, y=592.495, content exactly `。`, on its own line after `寫作題（沒有唯一答案）；範文（89 詞）見下` (y=562.77). The core equivalent fits on one line. Visually confirmed in crop `crops/zhtw-p8-h-orphan.png`. Correct text: the 。 must join the preceding line.

## Non-blocking observations (recorded, NOT counted as blocking defects)

- **O-1 — Core pairing badge (coordinator to adjudicate against literal task item 6).** The core (zh-cn) P1 has NO distinct pairing-badge element: P1 y=372 is the frozen Dutch strapline `DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS` (19pt, fill #57523f). Pairing is signalled by the Chinese subtitle (`荷兰语周报 · VOL.3 · …`), the Chinese top strip, Chinese page lines, and Chinese footers. This matches the shipped W45 core precedent exactly (checked: `files/weekly-report-w45-nl-core/svg/p1-voorpagina.svg`, VOL.2 — identical design, no badge element). Core KIT §1's claim "Pairing badge on P1 (subtitle slot)" is REFUTED as worded. Classified as a KIT-claim inaccuracy / precedent-consistent design, not a reader-facing defect — but the coordinator must rule whether the literal badge requirement applies to the core edition.
- **O-2 — KO disclosed wrap orphans (non-blocking, precedent-matched).** KO P6 gloss tail `가.` (x=1007, y=327.675) and P7 bridge tail `요.` (x=527, y=785.11) are single-syllable orphans, exactly the 2 disclosed in KO KIT §9, same count as shipped W45 KO. Line-start orphan punctuation: 0. Mid-word splits with ≥3-syllable tails are as in the builder koscan and are treated as accepted Korean wrapping per toolkit README note 16 (e.g. P3 `주의|하세요`, P5 `네덜|란드어로`, P7 `보내|주세요`, P8 `마|지막에`). P2 `LED 등.` is a complete word, not an orphan. Do not count as blocking unless the coordinator directs otherwise.
- **O-3 — JA typographic artifacts (not defects).** JA bylines on P4/P6 render `Leesniveau: B1/B2` joined in one element while the core splits the level into a following `B1`/`B2` element — content identical. JA P8 item 100 note uses full-width `＋` (`kiezen＋hoeft niet`) vs core ASCII `+` — typography only; `p8.py` still CLEAN.
- **O-4 — P1 bridge shortening (deliberate, consistent).** Core P1 bridge has 4 items (intocht, stoomboot, aanmeren, lampion); ALL 10 fan-outs have 3 items (`aanmeren` dropped). Documented as deliberate shortening in EN KIT §8(a); consistent everywhere; explanation-layer shortening, not a freeze violation.
- **O-5 — P7 quote page tags in PT/RU (precedent, not a defect).** PT and RU P7 quotes use Dutch `(Pagina N)` tags, not the native forms their KITs claim (`(Página N)` / `(Страница N)`). The artifacts follow the EN-family precedent (Dutch page word kept; P8 separators ARE native: PT `— PÁGINA n —`, RU `— СТРАНИЦА n —`). KIT claims REFUTED; artifact NOT a reader defect.
- **O-6 — ABSTRACT trailing newline.** Core `ABSTRACT.txt` ends with a newline (`wc -l` = 1); all 10 fan-out abstracts have no trailing newline (`wc -l` = 0). Both are valid single-line files; not a defect.

## Gate outputs summary (all re-run by the proofreader)

All gate JSONs/logs are saved under `hidden_files/w46/nl-proofread-gates/`.

1. **FREEZE** (`tools/freeze.py diff`, logs `gates-freeze-p8.log`, JSONs `freeze-*.json`).
   - Core-vs-itself sanity: +0/−0 all pages, added CJK 0, exit 0.
   - Latin + RU editions (de, en, es, fr, it, pt, ru) with `--strict-cjk`: added CJK 0, edition CJK total 0, exit 0.
   - Non-strict: JA added CJK 3,341; KO 3,581; ZH-TW 1,241. All added chars are the native script (JA kana/kanji/punctuation; KO 0 Han characters; ZH-TW Traditional forms, 0 simplified-only chars in SVG text scan). No Dutch target-text changes except adjudicated items O-3/O-4. Strapline handling matches each KIT (EN/JA/KO/PT/RU/ZH-TW remove the Dutch strapline, badge replaces it; DE/ES/FR/IT keep it verbatim, badge inserted at y=568).
2. **P8** (`tools/p8.py compare`, JSONs `p8-*.json`): ALL 10 fan-outs CLEAN — core 150 = edition 150, missing=[], extra=0, keydiff=[137,138] (legal re-aims: translation items NL→native; keys are native translations). Core extract: noted set 150/150.
3. **OCCLUSION** (`tools/occlusion_audit.py`, log `gates-occlusion.log`, JSONs `occlusion-*.json`): selftest OK (all 6 planted classes fired, clean controls silent). Edition-alone runs: 0 flags in all 11. `--core` NEW-vs-core runs: 0 new flags in all 10 fan-outs. Note: the occlusion audit is blind to the wrap orphans in F-2/E-1/E-2/E-3 (no ≥30% coverage, line-crossing, footer, edge, or text-overlap) — 0 flags is consistent with, not contradictory to, those defects.
4. **COUNTS** (proofreader script `count_check.py`, `counts.json`/`counts.log`): total **150** in every edition. Method: standalone `N.` stem elements + text.md bracketed items count 142; the other 8 are the two matching sets (P2 items 25–28, A2; P8 items 141–144, B2) rendered/entered as range headers `25–28.` / `141–144.` plus sub-lines. Per-page: **10 / 18 / 18 / 18 / 18 / 18 / 12 / 38**. Levels: **A2 47 / B1 72 / B2 31** (text.md bracketed 43/72/27 + match sets 4×A2 + 4×B2). Types (core): 完成句子 65, 单选 44, 词汇配对 8, 判断对错 7, 造句 8, 完形单选 13, 翻译 4, 写作 1. FR/PT P3 SVG stem count 19 with a duplicate standalone `3.` was the E-1 wrap orphan, not a duplicate exercise.
5. **P7 GOLDEN SENTENCES** (verified against rendered SVG, `p7-verbatim.log`): all 8 Dutch quotes verbatim (contiguous, whitespace-normalized) in P1–P6 body AND on P7, in all 11 editions. Page tags in order: (Pagina 1, 1, 2, 3, 4, 5, 6, 6). P7 bridges: 4 / 3 / 3 items in all editions including core, identical Dutch headwords, native glosses. Glosses under quotes in each reader-native language with correct dates/weekdays (spot-checked DE/JA/KO/RU).
6. **GLOSSES** (`gloss_check.py`, `gloss.json`/`gloss.log`): P2–P6 gloss counts **6 / 5 / 5 / 5 / 5** in every edition, identical Dutch headwords in identical order.
7. **P6 CHART** (measured from SVG rects/text, `chart-p7-gloss.log`): four olive bars at x=1473, y=304/362/420/478, widths **160 / 100 / 80 / 60** (values 40/25/20/15, scale 4 px/person), fill `#3e4c2a`, IDENTICAL in every edition. Category labels above bars; values at x=1863 beyond longest bar end (1633) — no coverage. Chart title carries the practice-data label in each native language; Dutch `OEFENDATA` line frozen.
8. **MODEL ESSAY + ANSWER ARITHMETIC** (`essay-answers.log`, `gloss-essay-answers.log`): model essay `Mijn week met Sinterklaas` = **89 words** (recounted word-by-word), in the 80–100 band, present verbatim on P8 in all editions with the 89-word note in the native language. Arithmetic verified from EN text.md: items 43 (5 days, 9→14 Nov), 44 (6 days, 9→15), 45 (4 hours, 12:00–16:00), 46 (17 years, 2009→2026), 83–87 (40, 25, 60=40+20, 15, 100=40+25+20+15), 61–64 true/false vs articles, 88–92 Motivaction/Stengs items — all correct.
9. **DATES/WEEKDAYS** (verified with `TZ='Europe/Amsterdam' date -d`): 2026-11-09 Mon, 11-10 Tue, 11-11 Wed, 11-12 Thu, 11-13 Fri, 11-14 Sat, 11-15 Sun, 11-16 Mon, 2026-12-05 Sat. All KIT/date claims consistent.
10. **BADGE / FOOTERS / IMAGES / READER-FACING SWEEP** (`badge-credits-sweep.log`): badge elements (P1, center-anchored x=975) — EN y=372, 20pt bold, fill `#3e4c2a`; DE/ES/FR/IT y=568, 20pt bold, fill `#a4553a`; JA/KO/PT/RU/ZH-TW y=372, 19.5pt bold, fill `#a4553a`. Badge texts match KIT furniture strings verbatim. Badge ink widths measured from rendered pixels: EN 950px, JA 542px (KIT 541.8), KO 466px, PT 1102px, RU 1040px (KIT 1033.4), ZH-TW 450px (KIT 444.9); DE/ES/FR/IT right edges consistent with KIT widths 1025.4/1116.5/1075.1/857.2 within a few px (left side contaminated by other brick ink in the band) — all centered on x=975. Footers: pairing footer on all 8 pages of all 11 editions at y=2624, fill `#57523f`, native pairing wording + native page line. Images: counts per page **[1,1,1,1,0,0,0,0]** in every edition; all 4 photo credits present and identical frozen Dutch `Foto: …` lines. Reader-facing sweep over all SVG text: only hits are `VOL.4` in legitimate content (VOLGENDE WEEK box + promise carry-forward + P2 EN JIJ box) — SOP §10 promise carry-forward, not a defect. No week/language codes, structure labels, repo links, or SOP/proofread/audit wording. Native-language residue scan (`residue-scan.log`): 0 English-word hits in non-EN added strings except PT `Complete` (6×, Portuguese imperative homograph, documented in PT KIT §4, W45 precedent — clean); long Dutch strings are all bilingual furniture heads; JA simplified-only hits are Japanese kanji false positives; KO 0 Han chars; ZH-TW 0 simplified-only chars.
11. **W45 PROMISES** (verified in rendered SVG text, all 11 editions; source `hidden_files/w46/nl-promises-check.md` + W45 NL KIT): honoured — Sinterklaas Amsterdam arrival Sun 15 Nov + Sint-Maarten Wed 11 Nov as lead topics; readers' corner = labelled editor's example (`Anna (voorbeeldbrief van de redactie)`) + Dutch disclosure (`nog geen echte brieven…`) + native-language disclosure in every edition (incl. EN: "No real letters or best page-8 texts at press time — example; promise to VOL.4.") + promise carried to VOL.4; VOLGENDE WEEK box contains Germany result Mon 16 Nov in Berlin, pakjesavond Sat 5 Dec, letters/best P8 texts; P2 EN JIJ box promises best entries in VOL.4.
12. **PDF + ABSTRACT FORMAT** (`pdf-check.log`): every `*-web.pdf` has a real text layer — pdftotext bytes 44,406–55,313 (>0), 8 pages, page size 1462.5×2025 pts, sizes 774,922–1,614,950 bytes (all ≤7 MB). Text-byte counts match KIT claims exactly except RU KIT §7 (55,344, stale; §9's 55,313 matches the measured 55,313). Every `ABSTRACT.txt` is single-line with 0 ASCII double-quotes. (Abstract FRAMING fails per F-1; format passes.)
13. **MASTHEAD PIXEL CHECK** (`masthead-pixel.log`): all cards 1950×2700. Ink in wordmark/subtitle/badge/insert bands stays within x=26..1923 (frame clearance holds) in all editions. Top-strip row y=85: left cluster, center cluster (native strip text, centered within ~13px of frame center 975), and frozen right cluster (x=1404–1923, identical in all editions) with clear gaps — RU middle cluster ends x=1281, right cluster starts x=1404 (122px gap; no collision, Fix 8 history clear). Visually confirmed in crops `ru-p1-topstrip.png`, `ko-p1-masthead.png`.
14. **VISUAL — P1 + P8 FULL FRAME, ALL 11 EDITIONS** (crops `*-p1-view.png`, `*-p8-view.png`): viewed every edition. No overflow, overlap, missing glyphs/tofu, or missing image credits on any P1 or P8. P2–P7 covered by the geometric gates plus the zone crops below. Kinsoku: JA 0 true line-start closer hits, 0 lines ending with openers; ZH-TW/core lone-punct scan otherwise clean apart from F-2/E-2/E-3.
15. **ZONE CROPS** (visual confirmation of defects): `fr/pt-p3-orphan3.png` (E-1 confirmed; `en-p3-orphan3.png` control correct), `core-p2-orphan.png` (F-2a), `core/zhtw-p6-gloss-orphan.png` (F-2b), `zhtw-p6-chart-orphan.png` (E-2), `zhtw-p8-h-orphan.png` (E-3).

## KIT-claim adjudications

- **CONFIRMED:** counts/levels/types, P8 CLEAN + keydiffs, freeze strict-CJK 0 (Latin/RU), KO/ZH-TW freeze totals, chart bars, P7 verbatim + bridges + glosses, badge strings/fills/geometries + ink widths (within ≤7px), footers, images/credits, essay 89 words, answer arithmetic, W45 promises, native disclosures, PDF text bytes/sizes (except RU §7, see below), reader-facing sweep, masthead clearance/centering, KO disclosed orphans as stated.
- **REFUTED (record inaccuracy; edition defect only where noted):**
  - JA freeze total 3,377 → shipped files measure 3,341 (builder log itself shows 3,377, then 3,367 across runs as P1/P7 changed; substance holds — all added chars Japanese). Record inaccuracy only.
  - PT/RU KIT §5 P7 quote-tag forms (`(Página N)` / `(Страница N)`) → artifacts use Dutch `(Pagina N)`. Precedent-consistent; not a reader defect (O-5).
  - Core KIT §1 badge claim → no distinct badge element in core (O-1; coordinator to adjudicate).
  - Core KIT §8(7) P6 gloss-orphan fix claim → lone 。 remains (defect F-2b).
  - RU KIT §7 web-PDF text bytes 55,344 → measured 55,313 (KIT §9 states 55,313 correctly). Record inaccuracy only.
- **UNVERIFIABLE:** none remaining. All KIT claims were adjudicated from re-runs, pixel measurement, or rendered-SVG inspection.

## Seed record (for the coordinator's insert step)

- **Target VOL number: VOL.3.**
- **Re-measured exercise total: 150; level split A2 47 / B1 72 / B2 31; per-page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.**
- **Core P1 article opening sentences, verbatim in Dutch** (verified against rendered core P1 SVG text, left column, reading order):
  1. `Op maandag 9 november begint het Sinterklaasjournaal op televisie.`
  2. `Elke dag om 18:00 uur volgen kinderen op NPO Zapp hoe Sinterklaas en zijn Pieten zich voorbereiden op de reis naar Nederland.`
  3. `Op zaterdag 14 november komt Sinterklaas officieel aan in Nederland.`

## Required follow-up

1. Fix F-1 (all 11 abstracts — practice framing), F-2a/F-2b (core, + zh-tw inheritance), E-1 (fr, pt), E-2/E-3 (zh-tw). Fix at the frozen-core source where the defect originates (F-2) and re-derive affected fan-outs; do not patch editions individually where the text is frozen.
2. Coordinator ruling requested on O-1 (core badge) and confirmation of O-2 tolerance (KO orphans) before Round 2.
3. Full re-proofread of all 11 editions after fixes (proofread-until-zero; no sampling).

**ROUND 1 FAIL (blocking defects: F-1 abstract news framing in all 11 editions; F-2a core P2 lone 。; F-2b core + zh-tw P6 gloss lone 。; E-1 fr + pt P3 stranded "3."; E-2 zh-tw P6 chart line-start 。; E-3 zh-tw P8 H-intro lone 。)**
