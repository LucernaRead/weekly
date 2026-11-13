# GATE-LOG — 2026-W47 ru-fr · proof1 (independent proofread)

**Edition:** `production/2026-w47/2026-w47-ru-fr/` · **Date:** 2026-11-11
**Scratch:** `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-fr1/`
**Tools:** `~/workspace/weekly-git/tools/venv/bin/python`; canonical creambox at
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`
(md5 `ee7a55d8b2057cf4ad42a97bb1197383`, verified matching).
**Environment:** `TMPDIR` = scratch `tmp/` for every command (system /tmp is 512 M and often full).
No source file was modified, rebuilt, committed or pushed.

## §0 Identity (disk = task)

| File | SHA-256 | Bytes |
|---|---|---|
| `Lucerna-VOL4-ru-fr.pdf` | `b9476fc2d49584d134e61d59f587bd24e76f4da0caf66de03884ba86523f3629` | 21,260,891 |
| `Lucerna-VOL4-ru-fr-web.pdf` | `78a56be6b7094ce1e9dd2435f174e4e8bb563e6c7363b2a2f82815dfd17128fe` | 3,346,639 (< 7 MB) |
| `2026-w47-ru-fr.text.md` | `4be2d24b46e1396219b1b74af4468d27f4b62a38c2f2af539532615bce8675f6` | 63,489 (838 lines) |

Core for comparisons: `production/2026-w47/core-ru/` (SVGs `p1-pervaya.svg` … `p8-test.svg`,
same names in the edition). Edition dir is untracked in git
(`?? production/2026-w47/2026-w47-ru-fr/`).

## §1 Occlusion audit — 42 flags, all TEXTX, all adjudicated CLEAR

- Tool: `tools/occlusion_audit.py`; selftest OK — planted classes fired
  `{BOXTITLE: 1, COVER: 1, EDGE: 1, FOOTER: 1, LINEX: 1, TEXTX: 1}`, clean controls silent.
- Edition run (`logs/occlusion.log`, `logs/occlusion.json`):
  `42 flags {'TEXTX': 42}`, 0 COVER / LINEX / FOOTER / EDGE / BOXTITLE.
  All 42 are same-line word↔punctuation/quote adjacency, ink-box overhang 3.0–8.0 px.
- Adjudication (three attempts, final method is `adjudicate4.py`, numpy, polarity-free,
  background = median colour of the junction window, one page at a time):
  - `adjudicate.py` (crude SVG matching): 28/42 same-baseline; remaining 14 were
    script matching artefacts (matched the wrong same-word element), not real geometry.
  - `adjudicate2.py` (raster junction scan): 25/42 CLEAR, 17 "TOUCH?" — all 17 had a
    polarity-detection bug (light=1 wrongly set for body text on paper; it detected
    paper as ink). Proved by the P6 `DONNÉES` case (visually clear + 2.88 px dark-ink
    blank, yet adjudicate2 said TOUCH?).
  - `adjudicate3.py` (polarity-free, pure-Python pixel loops) aborted without output
    (render pages are 4062×5625 px; loop too slow) — replaced by `adjudicate4.py`.
  - `adjudicate4.py` (numpy): **38/42 raster CLEAR** (widest blank column run in the
    junction window > 0, range 0.48–10.56 SVG px; the 0.48 px cases are the
    P1/P4 `ЦСКА` and P1 `пятница` junctions, glyphs still separated).
  - Remaining 4 (all `Краснодар»`, P1 ×1 at [101.2, 1200.5, 233.7, 1224.8],
    P4 ×3 at [101.2, 578.7, 233.7, 602.9], [101.2, 685.6, 233.7, 709.9],
    [1042.2, 2215.4, 1174.7, 2239.6]): the column test sees ink in every column of
    the zone because the `р`-bowl and the `»` chevrons occupy overlapping columns at
    different heights. Crops `crop-krasnodar-0.png` … `-3.png` (6× upscaled) show a
    clear light gap between the `р` bowl and the first `»` chevron — glyphs do not
    touch. Tool overhang 3.1×11.0 px is the ink-box (side-bearing) artefact.
  - **Final: 42/42 CLEAR.** 3 band-title junctions additionally verified by crops:
    P8 `ОТВЕТЫ | TEST` (`crop-p8-band.png`), P7 `ЯЗЫК | LANGUE` (`crop-p7-band.png`),
    P6 `НЕДЕЛЕ? | DONNÉES` (`crop-p6-chart.png`) — all clear gaps; the flag comes
    from the leading U+3000 in the French subtitle element (blank space, no raster ink).

## §2 Creambox (canonical, all 8 SVGs) — `logs/creambox.log`

- All inside-only clearances positive except one (see below).
- P7 toolbox (must-check (c)): 3 boxes, min inside clearance +11.9,
  min desc-clear +5.9 — **PASS**.
  `box y=992 bottom=1214.7 last baseline 1202.8 clearance +11.9 desc-clear +5.9 | 'распродажа'`
  (other two: +40.5/+34.7 and +23.3/+17.3). Summary line:
  `P7-TOOLBOX summary: 3 boxes, min inside clearance +11.9, min desc-clear +5.9`.
- P2 tight box (OBS-1, not a defect):
  `box y=795 bottom=1159.0 last baseline 1154.0 clearance +5.0 | 'pour le Père Gel.'`
  `inside-only: last baseline 1154.0 clearance +5.0 desc-clear -1.0 | 'pour le Père Gel.'`
  PIL true-ink measurement (`ink_check.py`, crop `crop-p2-boxbottom.png`): the
  descender of the last line ends **+1.24 SVG px above the box bottom** — inside the
  box. The tool's −1.0 desc-clear over-estimates the descender; true ink rules.
- P6 `BELOW-WINDOW +28.0 y=1468.0` (chart box, legend line below the window) is a
  next-element false positive, not a spill.
- P8 has no cream boxes.

## §3 p8 compare — CLEAN, keydiff [137,138,139,140]

- `logs/p8-core.log/json`, `logs/p8-edition.log/json`, `logs/p8-compare.log/json`.
- `core …/core-ru/svg/p8-test.svg: 150 noted`
  `edition …/2026-w47-ru-fr/svg/p8-test.svg: 150 noted`
  `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]`
- Keydiff adjudication: the four E-section keys are translation keys and are
  **correctly re-aimed at French** in this edition:
  137 `Mardi 17 novembre, Journée des étudiants.` · 138 `Un colis doit être suivi,
  retiré et vérifié.` · 139 `Mardi, la Russie joue contre le Venezuela.` ·
  140 `Bonne Journée des étudiants à toutes et à tous !`
  The core keys are the Chinese forms (e.g. 137 `11月17日星期二，大学生节。`) — by
  design, the core ships the first-channel reader language and each fan-out re-aims
  them. Translations checked for correctness (see keycheck-150.json notes).

## §4 Freeze — 8/8 byte-identical

- `logs/freeze-baseline.log`: `baseline: 8/8 SVGs byte-identical (repointed files: none)`,
  all eight `OK … core <sha> produced <sha>`; `core integrity: shipped core SVGs
  unchanged by the run (8 files re-hashed)`.
  (KIT's "0/8 = known redirect limitation" is wrong — the baseline run reports 8/8 directly.)
- `logs/freeze-diff.log/json` (`--core-svg core-ru/svg`, the SVG directory):
  P1 +19/−22, P2 +38/−36, P3 +27/−28, P4 +28/−28, P5 +27/−27, P6 +34/−54,
  P7 +50/−55, P8 +173/−639 strings (P8 is the French answer notes vs Russian core).
  Added CJK: **only U+3000** (ideographic space, SOP §1.1 separator), 6 total —
  1 each on P1–P5 and P8, 0 on P6/P7. `TOTAL added CJK characters: 6`.

## §5 Keycheck — 150/150 hand-verified (`keycheck-150.json`)

- Builder `build_keycheck.py` parses text.md stems + answer lines and compares
  against printed keys (`logs/p8-edition.json`) and core keys (`logs/p8-core.json`).
- Printed keys vs text.md keys: **0 mismatches** (per-page/per-level breakdown below).
  Q150 is a representation difference only: printed key is the checkmark `✓`
  (see-model-text marker, same in the core); text.md writes the parenthetical
  `(Question ouverte, texte modèle ci-dessous)` with the same meaning.
- Levels: A2 50 / B1 76 / B2 24. Types: Compléter 54, Choix 55, Appariement 20,
  Phrases 12, Transformer 4, Traduction 4, Rédaction 1 (total 150).
  Per page (Answers sections): P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38.
- Hand verification method: stems + keys read in text.md in full; each key re-checked
  against the article / P4 results table (all 8 match scores: Lokomotiv–Rubin 0:1,
  Fakel–Dynamo 1:2, Akhmat–Rodina 1:0, Krasnodar–CSKA 4:2, Krylia–Orenburg 2:0,
  Spartak–Akron 2:1, Zenit–Rostov 2:2, Baltika–Dynamo Mkh 0:1) / P6 chart
  (38/26/18/18 sums to 100) / matching option lists in the SVG
  (P2 D: a=День психолога, b=Международный день студента, c=Всемирный день ребёнка,
  d=день рождения Деда Мороза; P3 C; P4 C; P5 C; P8 F: a=результат матча, b=лёд на
  дороге, c=тепло зимой, d=большая продажа со скидками) / P8 G dialogue read in
  context (145 A `скидкой`, 146 B `чёрная пятница`, 147 B `промокод`, 148 A `целый`,
  149 B `покупок`); P7 golden sentences 8/8 verbatim with correct page refs
  (P1×2, P2×1, P3×1, P4×1, P5×1, P6×2).
- Model text (section H): **97 words** (brief 80–100 ✓).
- Q62 note: `15-й тур ___ 20–22 ноября (быть)` → `будет` is acceptable Russian,
  core-frozen wording; not a fan-out defect.
- P8 separators in SVG/PDF are real page numbers (`— СТРАНИЦА 1 —` … `8 —`); text.md's
  `— СТРАНИЦА? —` matches core-ru text.md line 668 — exporter format, not a defect.

## §6 Box titles / horizontal overflow (must-check (a)) — PASS

- PIL true-ink on the 200 dpi render (`ink_check.py`, crop `crop-p1-head.png`):
  P1 head `ТУР В ЦИФРАХ　EN CHIFFRES` ink max-x 895.7 SVG vs box right edge 961;
  Q6 chip (B1 badge rect x=989.0, y=1146.055, w=60, h=30; `6.` at x=1061) → **93.3 px clear**.
  No box-title or subtitle overflow on any page at full-page visual read.
- (b) P3/P5 right-column cream-box descender spill — does NOT reproduce (PIL ink):
  P3 boxes +68.3/+68.7 px, P5 +63.9 px above box bottom.
- P1 byline `От редакцииLucerna` — verified non-defect: PIL column measurement shows
  the word gap is **4.8 SVG px**, identical to the sibling word space in the same line
  (4.8 px); the `Уровень|чтения` space is 5.3 px (crops `crop-p1-byline*.png`).

## §7 Print vs web text layer — D1 (defect) + non-defect findings

- `pdftotext` both PDFs → `logs/print.txt` (57,796 B) / `logs/web.txt` (57,844 B);
  8 pages each. Non-space character multiset **equal** (30,708 each).
  Multiset difference: web +42 spaces / +6 newlines only (segmentation noise; in the
  web's favour in places, e.g. print merges `От редакцииLucerna`, `Главныетемы`).
- **D1 (blocking, mechanism): web PDF italic triplet — reproduced at span level.**
  Print P1: `«` = `Newsreader16pt-Italic`; `чёрная пятница` = `NotoSerif-MediumItalic`
  16.12; `»` = `Newsreader16pt-Italic`. Web P1: the term span is
  `LucernaNotoSerif-Regular` 16.12 with stored text **`чёрнаяпятница`** (space lost);
  `pdffonts`/span scan finds **zero italic faces** in the web PDF
  (only Regular/Bold), while print has `Newsreader16pt-Italic` + `NotoSerif-MediumItalic`.
  Web text layer has 2× ` »` vs print 1× (the extra one is web P1
  `«чёрная пятница »`; print's single ` »` is the legitimate French
  `« Black Friday »` on P5). The upright second occurrence of the term (P1, 15.75 pt
  `NotoSerif-Medium`) is intact in both PDFs — only italic spans are affected.
  Fix: `webpdf.py` must subset/embed the two italic faces; rebuild + re-verify with a
  span-level font check (pdftotext alone re-inserts the space from glyph positions
  and can mask symptom 1).
- **"14- й" is NOT a defect** (pdftotext artefact only): PyMuPDF span texts store
  `14-й тур` 17× in both PDFs; `search_for('14- й')` finds 0 instances in the web PDF.
  The hyphen+й split appears only in pdftotext's layout extraction.

## §8 P8 min font — 9.75 pt (measured, both PDFs)

- PyMuPDF span sizes on P8 (print): 9.75 pt is the minimum (385 spans at 9.75;
  next sizes 9.98, 10.35, 10.88 … 34.5); all-page minimum also 9.75 pt.
  Size distribution identical print vs web. SOP §1.1 floor is 9.75 pt (W46 mode) —
  at the floor, **PASS** (KIT's number happened to agree, but this is a fresh
  measurement, not a trust of KIT).

## §9 Curly quotes — only the intentional P7 pair

- SVG scan: `«`/`»` counts are balanced on every page (P1 25/25, P2 4/4, P3 21/21,
  P4 73/73, P5 22/22, P6 1/1, P7 36/36, P8 17/17).
  U+201C/U+201D: only 2 in all SVGs — P7 `“` (x=1503.4, y=552.64) and `”».`
  (x=1683.6, y=552.64), Newsreader font, around `чёрной пятнице` — the task's stated
  intentional exception. No U+2019 anywhere; print-PDF curly counts: `“` 1, `”` 1,
  `’` 0; straight apostrophes 38 (French elision).
- Section E type tags: no `翻譯`/`翻译` residue; tags are French
  (`[Traduction]`, `[Traduire en français]`). 0 CJK in text.md / ABSTRACT.txt.

## §10 Content read + dates

- All 8 print-PDF pages read visually at 200 dpi (`render/p-1.png` … `p-8.png`):
  visually clean, no overflow/overlap/clipping; footers `Page N sur 8`; masthead,
  strip and footer wording correct; P1 tagline word spaces present at high zoom
  (downscale artefact only). `ABSTRACT.txt` (435 bytes): one French line, correct
  topics, A2–B2, 150 exercices, no ASCII double quotes.
- Dates/weekdays verified by calendar: Nov 2026 — 16 Mon, 17 Tue, 18 Wed, 19 Thu,
  20 Fri, 21–22 Sat–Sun; 12 Nov Thu; 27 Nov Fri (Black Friday); 30 Nov Mon (Cyber
  Monday); 29 Nov Sun (Mother's Day, last Sunday); Nov has 20 working + 10
  non-working days (9 weekend days + 4 Nov Unity Day) — the P6 claim is correct.
- `vœu` is spelled correctly (1× in P2 SVG, 3× in text.md) — KIT's "voeu (no œ)"
  ruling is wrong.

## §11 External fact sources (core facts)

1. **Students' Day, Prague 1946** — confirmed. The 17 November observance was
   confirmed at the World Congress of Students held in Prague in 1946 (multiple
   university sources; e.g. https://bolashaq.edu.kz/en/novosti-en/17-november-international-students-day/ ,
   https://www.kaznu.kz:443/en/15531/news/one/26994/ ,
   https://tsu.ge/en/vocational-center/news/November-17-is-International-Students'-Day! ,
   https://nuaca.am/archives/news/nuaca-rector-y-vardanyans-congratulatory-message-on-students-day/?lang=en ).
   Note the standard account also records the 1941 London declaration and the 1939
   Prague events; the edition's wording ("решение о нём приняли в Праге в 1946 году")
   matches the standard "confirmed at the 1946 Prague congress" account.
2. **«Бумажный тигр» at Cannes 2026** — confirmed. James Gray's *Paper Tiger*,
   crime drama, world premiere in competition at the 2026 Cannes Film Festival,
   16 May 2026 ( https://en.wikipedia.org/wiki/Paper_Tiger_(2026_film) ,
   https://www.digitaltrends.com/movies/exclusive-paper-tiger-press-conference-james-gray-adam-driver-miles-teller/ ).
3. **«Рокки — это я» / Peter Farrelly** — confirmed. *I Play Rocky*, directed by
   Peter Farrelly, about Stallone writing and starring in *Rocky* (1976), in theatres
   Nov 2026 ( https://www.moviefone.com/news/movie-review-i-play-rocky/ ,
   https://www.screendaily.com/reviews/i-play-rocky-review-peter-farrelly-turns-story-behind-sylvester-stallones-breakout-into-a-sentimental-uninspiring-pastiche/5220366.article ).
4. **«Увидеть всё» / A24 Holmes documentary** — confirmed. *You Can See Everything*,
   A24 documentary by Nathan Fielder and Lance Oppenheim about Elizabeth Holmes /
   Theranos, surprise Telluride premiere 6 Sep 2026, US theatrical 16 Oct 2026
   ( https://www.screendaily.com/reviews/you-can-see-everything-review-disgraced-theranos-ceo-elizabeth-holmes-proves-a-slippery-subject-for-fascinating-documentary/5221147.article ,
   https://www.engadget.com/2252334/new-elizabeth-holmes-documentary-nathan-fielder-and-lance-oppenheim-coming-from-a24/ ,
   https://www.bbntimes.com/society/elizabeth-holmes-documentary-you-can-see-everything-premieres ).
5. Not independently verified (open items O1/O2 in PROOF-NOTE): the Ozon 14.4 M
   orders figure (11 Nov 2025) and the Russian 19 Nov cinema dates for the five
   P3 premieres; both are internally consistent and the international dates cluster
   in the same window. Core-level, not fan-out defects.

## §12 Non-defect rulings (summary)

- (a) P1 head/chip overflow — no. (b) P3/P5 descender spill — no; P2 "А ВЫ?" box
  tight (+1.24 px true ink) but inside. (c) P7 toolbox — PASS (+11.9/+5.9).
  (d) §E tags — clean French. (e) web italic triplet — REPRODUCED → D1.
- `14- й` — pdftotext artefact only, not in the stored text. P1 byline gap — 4.8 px,
  normal. P3/P5 mid-page whitespace, P7 Pushkin tight crop, Q147 wording, Q62 core
  phrasing — observations, not defects.
- KIT corrections: `vœu` (not "voeu"); freeze baseline is 8/8 directly (not "0/8,
  known limitation"); ABSTRACT.txt is 435 bytes (not 434).
