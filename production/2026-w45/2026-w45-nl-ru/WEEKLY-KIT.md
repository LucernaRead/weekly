# WEEKLY KIT — De Lucerna VOL.2 · Dutch × Russian (W45)

- **Issue week:** Monday 2 November – Sunday 8 November 2026, dated Monday 2 November 2026.
- **Pairing:** target language Dutch (Nederlands), reader native language Russian.
  Masthead: **De Lucerna**. Footer target name: **ГОЛЛАНДСКИЙ** (everyday Russian form,
  per W43 shipped NL×RU adjudication; overrides the НИДЕРЛАНДСКИЙ variant in the EN×RU
  KIT §3 name table).
- **Base:** W45 Dutch core (`files/weekly-report-w45-nl-core/`), VOL.2, 8 pages, 1950×2700,
  4 columns. Core build dir was never imported in place (README #11); registry work used
  the freeze scratch copy at `tools/scratch/baseline-w45-nl-ru/build-copy/`.
- **Build tree:** `hidden_files/weekly-report-w45-nl-ru-build/` (build logs, freeze/p8/
  occlusion/rowcheck raw outputs, `scratch/transform.py` — single source of truth for
  every fix edit; pristine core copies preserved at `scratch/pre-transform/`).

## 1. Core measured values (from the core WEEKLY-KIT.md, verified by registry diff)

- **Total 150 exercises.** Per page: **10 / 18 / 18 / 18 / 18 / 18 / 12 / 38**.
- **Levels:** A2 47, B1 72, B2 31.
- **Types:** 完成句子 65, 单选 44, 词汇配对 8, 判断对错 7, 造句 8, 完形单选 13, 翻译 4, 写作 1.
- **P8 model essay:** 87 words (requirement 80–100), identical in both editions.
- Registry diff (RU vs core): page diffs 0, level diffs 0, counts and levels identical.

## 2. Freeze gate — Dutch body text frozen

- `freeze.py baseline` reproduced the core shipped SVGs **8/8 byte-identical** before the
  transform (core SVGs re-hashed unchanged after the build: p1 `5424557b…`, p2 `78e6fcd2…`,
  p3 `5b9854e3…`, p4 `cc227fd9…`, p5 `e58064c9…`, p6 `6583fe28…`, p7 `65cfe2b3…`,
  p8 `fe22a151…`).
- Final freeze diff: **added CJK characters = 0 on all 8 pages** (core CJK totals
  191/212/153/126/214/192/373/1033 → edition 0).
- Removed strings without CJK, all adjudicated: P1 only the subtitle-slot strapline
  (replaced by the badge per W43 precedent); P6 a lone `）` wrap fragment of a removed
  Chinese line; P7 wrap tails `bomen。`, `thuis。`, `zij zette vast。`, `。` (tails of Chinese
  explanation lines citing Dutch words); P8 the eight `— PAGINA N —` separators
  (→ СТРАНИЦА, W43 precedent). All other removed strings contain CJK.
- Mechanical source-diff proof: every changed source line's old version either contains
  CJK or is one of exactly five structural items (P1 372 strapline→badge; P8 separators;
  P8 answer size; bridge→expl definition rename; PDF names). Dutch article text untouched.
- **P7 word-box definition retained verbatim:** ««meedoen» betekent: deelnemen, erbij
  zijn. In de Klimaatweek doet heel Nederland mee.» — present in both core and edition
  P7; only the explanation gloss was localized. No freeze violation.

## 3. P8 gate

- `p8.py compare` (explicit `--core-p8`/`--edition-p8`, total 150): **CLEAN, 150 = 150,
  missing=[], extra_count=0**. Extract confirms noted set 150/150.
- Line-level keydiff = [7, 17, 70, 71, 76, 96, 137, 138, 148]; registry keydiff = exactly
  **[137, 138, 150]** — all legitimate translation re-aims:
  - #137/#138 keys → Russian translations («Неделя климата длится семь дней.» /
    «Код «оранжевый» означает: приготовьтесь.»);
  - #139/#140 stems → Russian («Ночь музеев длится с 19:00 до 02:00. → ___» /
    «Я участвую в Неделе климата. → ___») with Dutch keys unchanged;
  - #150 writing key → «(открытый вопрос — образец ниже)», note → «Образец — в разделе
    H этой страницы (87 слов)».
- The other 7 line-level items were each verified against printed P8 lines: printed keys
  identical (7: B; 17: wortelen; 70: eiland; 71: proef; 76: gaat winnen; 96: advies; 148: B)
  — only the note after `—` changed (translation) plus 13.0pt re-wrap. None of the keys
  contains parentheses, so no parenthesis-branch extraction artifact is involved.
  Item 150 is absent from the line-level keydiff because writing items print as
  «N. ✓ note»; its printed RU line is «150. ✓ Образец — в разделе H этой страницы
  (87 слов)».
- Notes unchanged and language-neutral (Dutch grammar/arithmetic fragments): #6
  «veel mensen → planten», #78 «hij → gaat praten», #85 «45 + 25 = 70», #101
  «wij → planten», #102 «je → bespaar», #104 «rood = blijf binnen», #105 «ik → doe mee».
- **P8 answer size ruling:** 13.5→13.0pt at line-height 1.16 (W43 NL×RU precedent —
  Russian notes overflowed at 13.5).

## 4. Occlusion + same-baseline + chart gates

- `occlusion_audit.py` (final run): **edition 0 flags, core 0 flags, NEW vs core 0**
  (selftest passed first).
- Same-baseline ink-collision scan (`rowcheck.py`, svglib advance widths, <5px flag):
  **edition 8, core 8 — identical sets**, all P1 inhoud rows of the frozen Dutch layout
  (gaps 3.9px, one 0.4px); **NEW collisions 0**. P1 top band: no flags after the fix-2
  shortening (center vs date gap ≥5px advance).
- **P1 subtitle frame-margin fix (fix 3, found in visual review):** the first Russian
  subtitle at 40pt serif bold measured 1890.2px wide (ink 29.9–1920.1), pressing the
  28/40 outer frame lines — outside the audit's EDGE (page-bounds) class. Shortened to
  «ГОЛЛАНДСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · КЛИМАТ · НОЧЬ МУЗЕЕВ · 12-Й ТУР» (1673.6px,
  ink 138.2–1811.8, inside margins 65–1885). All three topics retained.
- P6 chart-label coverage (baseline-anchored PIL ink, NOT getbbox ascender-relative):
  bars identical to core (180/100/80/40, h 18, same y); **label ink covered by bars =
  0.0 for all rows**; labels sit above bars with a clear vertical gap. OEFENDATA nature
  stated in the Dutch caption + Russian capcn («Тренировочные данные: выдуманные цифры
  только для практики, а не настоящий опрос. Вопрос: что вы делаете при коде
  «оранжевый»? (100 молодых людей)»). Bar values 45/25/20/10, total 100.
- Render warnings: zero FLOW OVERFLOW / HEAD TOO WIDE in the final run. Flow ends:
  P1-headline 1452 (core-identical), P2-ex 2407 (core-identical), P3-ex 2584 (flow-y only;
  last ink 2570 < footer line 2580 — accounting drift, not ink overflow), P8-keys 2565
  (flow-y only; last answer ink 2549.26, ink bottom ≈2554 < 2580).

## 5. Gloss counts (split on `·` in the rendered gloss() string itself)

- gloss() total: **core 26 = edition 26** (P2 6, P3 5, P4 5, P5 5, P6 5).
- P1 expl 4 = 4; P7 bridges 4/3/3 = 4/3/3 (RU P7 bridges use ASCII `;` separators following
  the W43 RU precedent; segment counts match).
- Gloss prefix «Пояснение — »: 6 occurrences (P1 expl 1 + P2–P6 gloss boxes 5). W43's
  count of 9 included P7 bridges carrying the prefix; the W45 core P7 bridges carry no
  prefix, so 6 is the correct W45 figure.

## 6. P7 golden sentences and phrases

- All 8 golden sentences appear exactly **2×** in the edition (source article page + P7),
  same as core, verbatim Dutch.
- P7 quote label sequence: **[1,1,2,3,4,5,6,6]** = core (W43 pattern «(Страница N)»,
  counts 1,2,2,3,4,5,6,6 in W43's own ordering).
- All 8 phrases verified present on their labeled source pages in the edition
  (P1×2, P2, P3, P4, P5, P6×2).

## 7. Readers' corner (P7, no fabrication)

- Dutch example letter kept verbatim, labeled editor's example:
  ««Hallo! Ik ben Li en ik leer Nederlands in Shanghai. In de Klimaatweek plant ik een
  boom op mijn balkon!» — Li (voorbeeldbrief van de redactie)».
- Dutch disclosure kept verbatim: «Ter perse: nog geen echte brieven of beste
  pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3.»
- Russian disclosure: «Настоящих писем и лучших сочинений со страницы 8 пока нет —
  печатаем пример; обещание — в VOL.3.» (covers: no real letters, no best P8 texts,
  example + VOL.3 promise).
- Explicit Russian invitation (imperative + publication promise):
  **«Присылайте ваши настоящие письма — опубликуем в VOL.3!»**
- VOL.3 preview box (P7, Dutch, frozen) mentions Sinterklaas arrival Amsterdam Sun 15 Nov
  and Sint-Maarten Wed 11 Nov plus readers' letters and best P8 texts.

## 8. Residual / purity scans (rendered RU SVGs)

- CJK total: **0**. «桥接»: **0**. «— PAGINA»: **0**. «译注»: **0**.
  «НИДЕРЛАНДСКИЙ»: **0** (ГОЛЛАНДСКИЙ uniform).
- «(Pagina» count 1 — the P1 photo caption «…(Pagina 2)», frozen Dutch article-adjacent
  text, not a P7 label or P8 separator.
- Footers: left string «De Lucerna · ГОЛЛАНДСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА
  ГОЛЛАНДСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ» **8/8**; «Страница N из 8» **8/8**; VOL.2 in
  8 footers + P1 subtitle line.
- P8 separators «— СТРАНИЦА N —» ×8 (1–8).
- Explanation layer fully Russian; no other-family residue; no international-politics
  content in the explanation layer.

## 9. Images (public domain / CC0 only, credits from Commons API Artist field)

All 4 image payloads byte-identical to the core, same geometry, identical credit lines:

| Page | Image | Credit |
|------|-------|--------|
| P1 | herfstbos | Foto: Vovogov90 — CC0 |
| P2 | kinderdijk | Foto: Nationaal Archief — CC0 |
| P3 | gracht | Foto: W. Punt / Anefo, Nationaal Archief — CC0 |
| P4 | elftal1912 | Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein |

P5–P8 carry no images in the core and none here. Every credited image is laid out.

## 10. W43 furniture comparison (measured from shipped W43 NL×RU SVGs)

| Item | W43 shipped | W45 NL×RU | Match |
|------|-------------|-----------|-------|
| Badge slot | P1 y=372 (subtitle slot, Dutch strapline dropped) | same slot | ✓ |
| Badge text | ТЕКСТЫ НА ГОЛЛАНДСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ | identical | ✓ |
| Badge style | x=975, 19.5pt, bold, BRICK #a4553a, text-anchor=middle | identical | ✓ |
| Footer template | De Lucerna · ГОЛЛАНДСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.n · ТЕКСТЫ НА ГОЛЛАНДСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ | VOL.2, same template | ✓ (VOL differs by design) |
| Page line | x=1885, y=2624, 20pt, end-anchored, «Страница N из 8» | identical | ✓ |
| Gloss prefix | «Пояснение — » | same prefix (count 6 vs W43 9 — see §5 for the structural reason) | ✓ |
| P8 separators | «— СТРАНИЦА N —» ×8 | ×8 | ✓ |
| P7 quote labels | «(Страница N)» | same form and sequence | ✓ |
| Bilingual heads | Dutch original · Russian short form | same pattern (ГЛАВНОЕ / ТЕПЕРЬ ВЫ / БЛИЦ-ВИКТОРИНА / ЖИЗНЬ / КУЛЬТУРА / СПОРТ / МОЛОДЁЖЬ / РАЗБОР / ЯЗЫК / КЛИНИКА ОШИБОК / СЛОВО НЕДЕЛИ / ФРАЗЫ НЕДЕЛИ + «дословно из статей этого номера» / ТЕСТ И ОТВЕТЫ; narrow forms В ЦИФРАХ, ПАМЯТКА, ОТМЕНЯТЬ?, А ВЫ?, КОРОТКО) | ✓ |

Conflict resolved: the EN×RU KIT §3 name table's НИДЕРЛАНДСКИЙ variant is overridden by
the W43 NL×RU shipped measurement (ГОЛЛАНДСКИЙ throughout), per tools/README
data-contradiction rule #9.

## 11. Fix-round history (all edits in `scratch/transform.py`, pristine restore + one-process re-render each round)

- **Fix 1 — flow overflows:** Russian-length cascades (P1 cijfers box moved column on a
  5px fit miss; one extra P2 bridge line shifted every column break). Shortened P1 cijfers
  item 2 parenthetical, P2 bridges to one line each, P8 answers 13.5→13.0pt, P7 PAS OP
  notes compressed to core line counts, P7 disclosure shortened, P7 invitation set,
  P1 woord note set to 2 lines matching core geometry.
- **Fix 2 — occlusion flags (6 NEW, all genuine Russian-width defects):** P1 top-strip
  center dropped «КАЖДУЮ НЕДЕЛЮ · » (right edge 1400.0 vs date left 1419.8); P1 band right
  line 2 → «По всей стране · см. страницу 2»; P1 agenda footer → «Расписание недели — на
  страницах 2–4»; P6 chart title → «DE GRAFIEK · ГРАФИК»; P7 first golden-sentence
  translation → one line «Со 2 по 8 ноября, с понедельника по воскресенье, — Неделя
  климата.»; P7 disclosure → 3 lines. Result: audit 0/0/NEW 0.
- **Fix 3 — P1 subtitle frame margin (visual review):** subtitle shortened (§4); audit
  re-confirmed 0/0/NEW 0; all 8 cards visually reviewed after fix 3 (P1 re-checked,
  P2–P8 unchanged in content).
- Pre-re-render SHA snapshots were written to `build-log-fix1-presha.txt` before each
  fix round, as required.

## 12. Toolchain

- **run.py:** `tools/venv/bin/python` (Python 3.12.3, PIL 13.0.0).
- **render.py:** `tools/venv/bin/python` (Python 3.12.3, PIL 13.0.0, cairosvg 2.9.1) —
  system python3 (3.12.3, PIL 10.2.0) lacks cairosvg and was not used.
- Line widths measured from rendered SVGs (svglib advance widths); baseline SVGs
  reproduced 8/8 byte-identical before the transform.

## 13. Deliverables and hashes

- SVG: `svg/p{1-voorpagina,2-leven,3-cultuur,4-sport,5-jongeren,6-verdieping,7-taal,8-toets}.svg`
- Cards: `cards/*.png`, 8 × 1950×2700.
- Print PDF: `De-Lucerna-VOL2-RU.pdf` — 8 pages, 7,879,024 bytes,
  sha256 `b9bfc7488f4b4bea2ce6f05d34fab684de2823902b2d61b1b7a70d33e185ff60`.
- Web PDF: `De-Lucerna-VOL2-RU-web.pdf` — 8 pages, 3,751,768 bytes (<10 MB),
  sha256 `84d97625639e9df8ed6ab04947da6b35cdbb8b1aa1f3b919ff82401b7389c6d8`.
- Edition SVG sha256 (final render): p1 `6f1b411d…`, p2 `485524e1…`, p3 `5235b69f…`,
  p4 `fc1763b7…`, p5 `6d433e58…`, p6 `e1d2513a…`, p7 `38e03c39…`, p8 `12777082…`.
- `ABSTRACT.txt`: Russian, single line, no ASCII double quotes, with real topic keywords
  and a learner search phrase.

## 14. Status

**Builder-complete.** All hard gates measured and passed. NOT finalized — finalization
requires independent proofread. Not posted to Discord, not sent to the main chat, not
pushed to git.
