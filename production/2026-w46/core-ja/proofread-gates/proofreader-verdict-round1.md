# Independent Proofread Verdict — Round 1: Lucerna Weekly W46, JA family

- Issue: VOL.3, Mon 2026-11-09 – Sun 2026-11-15. Target language: Japanese.
- Scope: all 11 editions — 2026-w46-ja-de, -en, -es, -fr, -it, -ko, -nl, -pt, -ru, -zh-cn, -zh-tw.
  The core directory `files/weekly-report-w46-ja-core/` IS the zh-cn edition (KIT slug
  `2026-w46-ja-zh-cn`); no separate `weekly-report-w46-ja-zh-cn` build dir exists.
- Proofreader: independent Round 1 (proofreader did not build these editions). No edition file
  was edited, re-rendered, pushed, inserted, or posted anywhere. Frozen core build sources were
  not modified (core SVG sha256 verified identical before/after all gate runs).
- Method: SOP read in full; all 11 WEEKLY-KIT.md read; canonical tools re-run by the
  proofreader with `tools/venv/bin/python` — `freeze.py` baseline + `diff --strict-cjk`,
  `p8.py` extract/compare, `occlusion_audit.py` — plus a kinsoku/orphan scan replicating
  `hidden_files/w46/check_edition.py` definitions extended to line-END punctuation, SVG-attribute
  badge measurement, pixel measurement of rendered P1 cards, pdftotext web-vs-print comparison,
  full-text residue scans, weekday/date verification, and full-frame visual review of P1 and P8
  cards for all 11 editions plus P3/P6/P7 spot checks (core).
- Gate artifacts: `hidden_files/w46/ja-proofread-gates/` — `freeze-<code>.json` (11),
  `p8compare-<code>.json` (11), `occlusion-<code>.json` (11), `p8extract-core.json`,
  `freeze-baseline.json/.log`, `gates-run.log`, `kinsoku-orphan.json`,
  `kinsoku_orphan_scan.py`, `core-svg-sha256-before/after.txt`, `abstracts.txt`,
  `extra-checks.log`, `run_gates.sh`, `baseline-ja/` (build-copy scratch).

## Per-edition verdicts

| Edition | Verdict | Blocking defects |
|---|---|---|
| 2026-w46-ja-zh-cn (core) | FAIL | D-CORE-01, D-CORE-02 |
| 2026-w46-ja-de | FAIL | D-CORE-01, D-CORE-02 (inherited; no edition-specific defects) |
| 2026-w46-ja-en | FAIL | D-CORE-01, D-CORE-02 (inherited; no edition-specific defects) |
| 2026-w46-ja-es | FAIL | D-CORE-01, D-CORE-02 (inherited; no edition-specific defects) |
| 2026-w46-ja-fr | FAIL | D-CORE-01, D-CORE-02 (inherited; no edition-specific defects) |
| 2026-w46-ja-it | FAIL | D-CORE-01, D-CORE-02 (inherited; no edition-specific defects) |
| 2026-w46-ja-ko | FAIL | D-CORE-01, D-CORE-02 (inherited; no edition-specific defects) |
| 2026-w46-ja-nl | FAIL | D-CORE-01, D-CORE-02 (inherited; no edition-specific defects) |
| 2026-w46-ja-pt | FAIL | D-CORE-01, D-CORE-02 (inherited; no edition-specific defects) |
| 2026-w46-ja-ru | FAIL | D-CORE-01, D-CORE-02 (inherited; no edition-specific defects) |
| 2026-w46-ja-zh-tw | FAIL | D-CORE-01, D-CORE-02, D-ZHTW-01, D-ZHTW-02 |

No edition is shippable in Round 1. All 11 fail on the two inherited frozen-core defects;
zh-tw fails additionally on two unconverted Simplified-residue strings.

## Defect list

### A. Frozen-core defects (present in the core and inherited byte-identically by all 10 fan-outs)

**D-CORE-01 — Kinsoku: two lines end with an opening parenthesis "（" (frozen Japanese body text).**
The builder's kinsoku scan covered line-START punctuation only and missed line ends.
Independent scan (line-start hits 0, orphan issues 0 in all 11 editions; line-END hits exactly
these 2 sites in all 11 editions). Both sites visually confirmed on rendered cards.

- (a) P1, quiz item 8, `p1-hyoushi.svg` line y=2419.0 (all 11 editions):
  Wrong: `七五三の中心の日はいつですか。 A. 9日（` — line ends with "（", the closing
  `月）` falls to the next line.
  Correct: rewrap so the option is not split after "（" — e.g. move `A. 9日（月）` whole to
  the next line (or shorten the stem). Any rewrap that keeps "（…）" intact on one line.
- (b) P3, item 32, `p3-bunka.svg` line y=2163.2 (all 11 editions):
  Wrong: `二の酉はいつですか。 A. 19日（木） · B. 7日（` — line ends with "（", `土）`
  falls to the next line.
  Correct: rewrap so `B. 7日（土）` is intact on one line.
  Fix location: frozen core text layout; the fix propagates to all fan-outs. Round 2 must
  re-run the kinsoku scan including line-END punctuation on all 11 editions.

**D-CORE-02 — ABSTRACT.txt framing violates the practice-framing rule (all 11 editions).**
Format passes everywhere (single line + trailing newline, no ASCII double-quote,
reader-native language). Framing fails everywhere: every abstract closes with the prohibited
"learn Japanese through/by reading real Japanese news" construction. Standing rule
(user 2026-10-28): the abstract's product is the practice; never "learn Japanese from this
week's news" or equivalents ("用一周新闻学X / 以新闻学 / 读新闻学 / 用报纸学"); rewrite as
"150 exercises built from this week's topics" ("以本周话题为素材的 N 道练习").
Offending tails (verbatim, full texts in `abstracts.txt`):

- zh-cn: `…适合想通过读日语新闻学日语的读者。`
- zh-tw: `…透過真實日本新聞學日語。`
- en: `…for readers learning Japanese through real Japanese news.`
- de: `…für alle, die Japanisch durch echte japanische Nachrichten lernen.`
- es: `…para aprender japonés con noticias japonesas reales.`
- fr: `…pour apprendre le japonais à travers de vraies nouvelles japonaises.`
- it: `…per imparare il giapponese con vere notizie giapponesi.`
- ko: `…실제 일본 뉴스로 일본어를 배웁니다.`
- nl: `…om Japans te leren met echt Japans nieuws.`
- pt: `…para aprender japonês com notícias japonesas reais.`
- ru: `…для изучающих японский по настоящим японским новостям.`
  Correct: rewrite each abstract's closing clause into practice framing in its own native
  language, e.g. zh-cn `…共150道以本周话题为素材的练习。` (equivalents in each language:
  "150 exercises built from this week's topics"). Keep single-line, no ASCII double-quote,
  reader-native. The KIT claim "ABSTRACT.txt valid" is REFUTED on framing (format confirmed).

### B. Edition-specific defects

**D-ZHTW-01 — zh-tw P7, unconverted Simplified Chinese (SC residue).**
File `files/weekly-report-w46-ja-zh-tw/svg/p7-kotoba.svg`, text element y=784.04 (error-clinic
note under `「神社に千歳飴をもらいます」`):
Wrong: `得到东西的场所用「で」。` — contains Simplified-only 东 / 西 (as 东西) / 场所.
Correct (Traditional): `得到東西的場所用「で」。`
This refutes the zh-tw KIT §6 claim of "0 Simplified-only characters remain". A full
Simplified-only-character scan of all zh-tw SVGs found exactly these 2 strings (this one and
D-ZHTW-02); all other core SC strings were converted (selectivity verified: P8 keys 75 and 95
WERE converted). A second sweep with a wider SC-only set found no further hits (one apparent
hit, P6 `本当の調査`, is frozen Japanese, not residue).

**D-ZHTW-02 — zh-tw P8, unconverted Simplified Chinese in answer key 42 (SC residue).**
File `files/weekly-report-w46-ja-zh-tw/svg/p8-tesuto.svg`, text element y=1428.984:
Wrong: `42. 熊手を買います。 — 在酉の市买熊手` — contains Simplified-only 买.
Correct (Traditional, minimal fix): `42. 熊手を買います。 — 在酉の市買熊手`
Note: the KIT §6 records two other mixed notes found and added to the MAP
("地点＋へ＋动词", "动词名词化时要加「こと」。"); these two strings were missed by that pass.

### C. Cosmetic observations — NOT defects, no action required

- O-01: P8 key 92 spacing differs: core/zh-tw `92. 60 — 34+26=60` vs other fan-outs
  `92. 60 — 34 + 26 = 60`. Key value identical (60); P8 set equality holds. Cosmetic only.
- O-02: the zh-cn core has no brick pairing badge: its P1 subtitle line sits at y=330 in
  fill `#28251d` (`日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間`) with strapline y=372.
  This matches the shipped W45 JA core masthead geometry exactly (verified on
  `files/weekly-report-w45-ja-core/svg/p1-hyoushi.svg`: same y=330 subtitle, no badge), and
  the pairing is visibly labelled by the subtitle line plus the footer
  (`Lucerna · 日语周报 VOL.3 · LUCERNA JAPANESE WEEKLY`). Design parity, not a defect.
- O-03: IT P1 numbers-box title (`Settimana in numeri`) sits tight to the box edge; the
  occlusion audit reports 0 flags and ink clears the border. Tight but passing.
- O-04: NL P8 keys-flow end-y measured 2537.4 vs KIT "2536" — a 1.4-unit rounding
  difference; keys clear the footer by ~87 units. Not a defect.
- O-05: P1 numbers-box item 4 wraps leaving `した` on its own line — an ordinary wrap, not an
  orphan fragment under the scan definitions. Not a defect.

## KIT-claim adjudication

- Exercise total 150; split A2 46 / B1 75 / B2 29; by-page 10/18/18/18/18/18/12/38 —
  CONFIRMED (re-measured from rendered SVGs in all 11 editions; stems numbered 1–150
  continuous, no gaps/dups; P8 keys are the second 1–150 set as designed; pairing method:
  nearest level badge within the stem's column; 5 badges are group/range labels, so the raw
  badge-element count is 145 — the pairing result, not the raw count, is the split).
- Occlusion audit 0 flags — CONFIRMED (canonical tool re-run, all 11 editions, all 8 pages,
  `flag_count: 0`, empty flags lists).
- P1 masthead pixel clearance — CONFIRMED (rendered-card pixel measurement, all 11: subtitle
  band, badge band 338–359, strapline band 374–390 separated by ≥14 units; top-strip segment
  gaps ≥423 / ≥224 units; no collisions).
- P8 compare CLEAN, core 150 / edition 150, missing [] / extra [], keydiff [137,138]
  (zh-tw [138], zh-cn []) — CONFIRMED. Keydiffs adjudicated LEGITIMATE REDIRECTS, not missing
  notes: items 137–138 keep byte-identical Japanese stems with native-language keys (hence the
  diff); items 139–140 carry native-language stems with byte-identical Japanese keys; verified
  element-by-element in en/ko/ru/zh-tw/core.
- Freeze `--strict-cjk` 0 added CJK (de/en/es/fr/it/nl/pt/ru/zh-cn) — CONFIRMED (exit 0).
  ko exit 1 — adjudicated LEGITIMATE: all Han characters in ko ⊆ core Han set (0 new Han);
  308 distinct Hangul syllables (matches KIT); only added non-Hangul chars are `!:;? ~`.
  zh-tw exit 1 — PARTLY REFUTED: unexplained chars 將/請/講/輯 are legitimate hand-written
  Traditional strings (disclosure, badge, 編輯部); BUT 2 Simplified-residue strings remain
  (D-ZHTW-01/02), refuting "0 Simplified-only characters remain".
- Freeze removed-string review — CONFIRMED: every removed kana-bearing string on P1–P7 is a
  bilingual header/dek/gloss line or quoted headword (explanation-layer churn); no frozen
  Japanese article sentence was removed or altered on P1–P6; P8 removals are the Chinese keys
  replaced by native keys, as designed. Core SVGs unchanged before/after (sha256 diff empty).
- Badge geometry + fill — CONFIRMED for all 10 fan-outs, measured from SVG attributes (not
  trusted from KITs): badge text x=975, y=356, fill `#a4553a` (BRICK), 19pt, weight 700,
  center-anchored; wordmark baseline y=262, subtitle y=316, strapline y=390 in all fan-outs.
  Footer labels distinct and correct per edition (verified). Core geometry per O-02.
- Web PDF ≤7 MB with real text layer, pdftotext identical to print — CONFIRMED: sizes
  2,254,301–2,875,035 B; pdftotext bytes > 0 for all 11; web-vs-print pdftotext byte-identical
  for all 11 (see `extra-checks.log`).
- ABSTRACT.txt format (single-line, no ASCII double-quote, reader-native) — CONFIRMED.
  Framing — REFUTED (D-CORE-02).
- P6 chart bars measured x=315, widths 1020/780/720/480 = 30×34/26/24/16; labels 山 34%,
  神社 26%, 公園 24%, 町 16%, sum 100%; practice-data label present — CONFIRMED. Chart is
  frozen Japanese; fan-out identity follows from freeze CJK 0.
- P7 golden phrases (8, verbatim contiguous excerpts from the issue's own articles) —
  CONFIRMED: whitespace-stripped counts exactly 2× each in zh-cn/en/ko/zh-tw; per-page matrix
  verified for core (P1 phrases 1–2, P2 3–4, P3 5, P4 6, P5 7, P6 8, P7 all 8, P8 0).
- P8 model text 154 characters — CONFIRMED (non-space count 154).
- P7 teaser / P8 keys-flow end-y claims — CONFIRMED in substance (measured keys-flow max y
  excl. footer 2514.9–2537.4 across editions, footer baseline 2624; clear in all editions).
- "No FLOW OVERFLOW / HEAD TOO WIDE" (builder self-check) — UNVERIFIABLE from artifacts alone
  (builder-internal); visual review of all P1/P8 cards + core P3/P6/P7 + 0 occlusion flags
  supports no overflow.
- By-type exercise counts (完成句子 50 · 单选 51 · 完形单选 13 · 词汇配对 12 · 判断对错 11 ·
  造句 8 · 翻译 4 · 写作 1) — arithmetic sums to 150 CONFIRMED; per-type re-measurement
  UNVERIFIABLE from rendered artifacts (no type registry in the edition dirs).
- Weekday/date claims — CONFIRMED: all 7 explicit month+day+weekday claims in core SVGs
  correct (2026-10-24 Sat, 10-25 Sun, 10-27 Tue, 10-28 Wed, 11-09 Mon, 11-11 Wed, 11-15 Sun);
  issue dates Mon 2026-11-09 – Sun 2026-11-15 correct.
- Native-language correctness — CONFIRMED except D-ZHTW-01/02: no Chinese-prose residue in
  the 9 non-Chinese editions (0 marker hits); no English residue in non-EN editions (FR
  "Note —" is its own gloss label; "Page 1 sur 8" is French); ko SC scan clean; zh-tw TC
  font faces present for the explanation layer (340 TC-face elements); no Hangul/Cyrillic
  wrong-script residue found; gloss headwords occur in their articles (spot-checked P1/P6).
- Reader-facing sweep — CONFIRMED: no week/language codes, repo links, SOP/proofread/audit
  wording, or structure labels on any rendered page. Only "VOL.4" hits, all in the P7
  next-issue teaser/disclosure (the publication's own public volume label, same class as the
  VOL.3 masthead furniture).
- Image credits — CONFIRMED: the only 3 photos in the issue (P1 maple, P3 Hiroshige III 1876
  print, P4 stadium) are all credited on-page (Poliphilo CC0; 歌川広重（三代） public domain;
  Syced CC0 — all Wikimedia Commons, matching the VOL.1 verified set). P2/P5/P6/P7/P8 contain
  no photos.
- W45 promises (core KIT §4) — all 4 CONFIRMED honoured:
  1. Reading Week ends Mon 9 Nov closing report — P1 lead + P7 A2 column.
  2. Japan Series final-result roundup (G3–G7 gap) — P4: G1 24 Oct 3-1 (11 inn), G2 25 Oct
     4-3 (10 inn), G3 27 Oct Fukuoka 2-1 (10 inn, Tomoya walk-off HR), G4 28 Oct 4-2,
     G5–G7 not played, MVP Tomoya, 13th title, 2 straight years; no invented results.
  3. Foliage-peak continuation — P1 + P6 (Weathernews 29 Oct 3rd forecast; JMC 2 Sep forecast;
     peaks Takao ~13 Nov, Miyajima 21 Nov, Arashiyama 23 Nov, Tokyo ~29 Nov, Osaka ~4 Dec).
  4. Real readers' letters + best P8 writing — no real letters/texts are evidenced to have
     arrived; P7 prints a labelled editor's example (generic, no invented sender name) PLUS
     an on-page disclosure in Japanese + Simplified Chinese (core) / a single native-language
     disclosure (each fan-out, verified in all 11 including zh-tw Traditional and NL/RU),
     stating none had arrived by deadline and carrying the promise to VOL.4; the VOL.4 teaser
     repeats the carry-over. No fabricated reader, letter, name, or quote appears.
- Kinsoku line-START scan (builder) — CONFIRMED for starts (0 hits); scope INCOMPLETE — line
  ends were not scanned (D-CORE-01).

## Gate outputs summary

- Freeze baseline: exit 0, 8/8 core SVGs byte-identical (`freeze-baseline.json`).
- Freeze diff `--strict-cjk`: exit 0 for de/en/es/fr/it/nl/pt/ru/zh-cn (added CJK `{}`);
  exit 1 for ko and zh-tw only, as the KITs state (adjudicated above).
- P8 compare: CLEAN for all 11 (`p8compare-<code>.json`).
- Occlusion audit: 0 flags for all 11 (`occlusion-<code>.json`).
- Kinsoku/orphan scan: line-start hits 0, orphan issues 0, line-END hits 2 (frozen sites,
  all editions) — `kinsoku-orphan.json`, `kinsoku_orphan_scan.py`.
- PDF: all ≤7 MB, pdftotext > 0, web==print byte-identical — `extra-checks.log`.
- Visual: P1 + P8 cards viewed full-frame for all 11 editions; P3/P6/P7 core cards viewed.
  No overflow, overlap, missing glyphs/tofu, or missing credits found beyond the defects
  listed above. (P1 Q8 and P3 Q32 kinsoku dangles visible in render — D-CORE-01.)

## Seed record (for the coordinator's insert step)

- Volume: VOL.3.
- Issue dates: Mon 2026-11-09 – Sun 2026-11-15.
- Exercise total (re-measured): 150. Level split (re-measured): A2 46 / B1 75 / B2 29.
- Core P1 article opening, 3 sentences verbatim (Japanese, target language):

読書週間は、9日（月よう日）で終わります。10月27日（火よう日）に始まりました。今年のスローガンは『静かだけど、冒険中。』でした。

## Required for Round 2

1. Fix D-CORE-01 in the frozen core (rewrap P1 item 8 and P3 item 32 so no line ends with
   "（"); re-run the kinsoku scan including line-END punctuation on all 11 editions.
2. Rewrite all 11 ABSTRACT.txt closings into practice framing (D-CORE-02); re-verify
   single-line / no ASCII double-quote / reader-native.
3. Fix D-ZHTW-01 and D-ZHTW-02 (Traditional conversion); re-run the Simplified-only scan
   on zh-tw and re-run freeze/P8/occlusion for the rebuilt editions.
4. Round 2 independent proofread must re-verify the fixed sites plus a fresh full-gate run
   before any edition ships. Nothing in this round's PASS column may be assumed to survive
   a rebuild.

ROUND 1 FAIL
