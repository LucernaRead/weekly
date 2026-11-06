# Lucerna Weekly — W45 Korean × Italian edition (KO×IT)

**Status: builder-complete NOT finalized** — finalization is the independent
proofreader's decision, not the builder's. This edition has NOT been posted
to Discord, NOT sent to the main chat, NOT inserted into any repo.

- Issue week: Mon 2026-11-02 – Sun 2026-11-08 (VOL.2)
- Pairing: target Korean × reader-native Italian. Masthead takes NO article
  (Korean). Pairing badge on P1 masthead + every page footer (full names).
- Target-language text frozen; explanation layer entirely in Italian. The
  intermediary term, in any language form, appears in NO deliverable
  (SVG scan: 0 hits).
- Delivery dir: `files/weekly-report-w45-ko-it/` — svg×8, cards×8, dual PDF,
  this KIT, `ABSTRACT.txt`.
- Build tree: `hidden_files/weekly-report-w45-ko-it-build/` — single source
  of fix-round edits: `scratch/transform.py` (one-off, NOT imported by
  `run.py`/`render.py`). Nothing under `tools/` was modified.

## Toolchain (interpreters + versions)

- `run.py` and `render.py` both run under `tools/venv/bin/python`:
  Python 3.12.3, venv PIL 13.0.0. (System python3 is also 3.12.3 but was
  not used for build/render; audit measurement uses venv PIL.)
- `tools/p8.py` sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`
  — the adopted new version (dash branch verified TRUSTED).
- `tools/occlusion_audit.py` sha256 `e1f92b42eb8996fe04c5ffb60c4ec23e1911239a5f94b76808f01ed9414addf2`.
- `tools/freeze.py` sha256 `d9adfa486a788e57e15805d383f5691094067d26f1884c127dea4d1a1e587d54`.

## Baseline proof (core untouched)

The W45 KO core build was copied to the ko-it build dir, OUT repointed,
and re-rendered in a single process with venv `run.py`: all 8 regenerated
SVGs byte-identical to the shipped core SVGs (8/8 MATCH). Core and W43
directories were read-only throughout.

## Counts (all equal to the W45 KO core)

- TOTAL 150 exercises, continuous registry 1–150 (P8 noted set 150/150).
- Levels: A2 51 / B1 72 / B2 27.
- Pages: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- Types (Italian labels): Completa la frase 48, Scelta multipla 52,
  Abbinamento 16, Cloze 13, Costruisci la frase 8, Trasforma la frase 4,
  Vero o falso 4, Traduzione 4, Scrittura 1.
- P8: 38 items (A 8, B 8, C 4, D 4, E 4, F 4, G 5, H 1).
- Model essay: 6 lines byte-identical to core; body 157 chars (spaces
  removed) = core = brief.
- P7 golden sentences: whole-issue frequencies 5 / 2 / 4 / 2 / 2 / 2 / 2 / 2
  in BOTH core and edition; all 8 verbatim-contiguous excerpts of this
  issue, on their tagged pages (1면 / 1면 / 1면 / 2면 / 3면 / 4면 / 5면 / 6면).
- Gloss (·-split items, source gloss()/expl()/glossline() strings
  attributed by CURPAGE, rendered headwords verified on-page):
  per page 5 / 16 / 13 / 6 / 12 / 8 / 6 = 66 total, core = edition exactly.
  Every item's Korean headword occurs in its page's rendered SVG.
  (Open observation: the task brief quoted 84 gloss items; the item-level
  count reproducibly gives 66. The 84 figure is likely a wrapped-line
  fragment basis, not items. The item-level gate passes 66 = 66.)
- P8 answer-flow end: col 3 y=2366 (< 2540). P7 teaser end: 2517.94 (< 2540).
- Zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final run.

## P8 adjudication (explicit, from printed lines — not tool output alone)

- `p8.py compare`, both paths (dir compare + `--total 150` file compare):
  core 150 noted, edition 150 noted, status CLEAN, missing=[],
  extra_count=0, keydiff=[137, 138].
- Printed-line adjudication:
  - 137: core key `11月7日是立冬。` → edition key
    `Il 7 novembre è l'ipdong.` — note `Confronta con pag. 1`
    (core: 对照第 1 版). Re-aimed to Italian. Item number verified from
    the core render, not copied from sibling editions.
  - 138: core key `离高考还剩 12 天。` → edition key
    `Mancano 12 giorni all'esame.` — note `Confronta con pag. 5`
    (core: 对照第 5 版). Re-aimed to Italian.
  - 139: Korean key UNCHANGED `특별 조치는 11월 19일에만 적용돼요.` —
    note localized `Confronta con pag. 6` (core: 对照第 6 版).
  - 140: Korean key UNCHANGED `저는 토요일에 내장산에 단풍을 보러 가요.` —
    note localized `Confronta con pag. 3` (core: 对照第 3 版).
  - 150: apparatus in Italian:
    `✓ Il modello è nella sezione H di questa pagina (157 caratteri)`.
  - Separator lines kept in Korean (`— 제N면 —`), per the W43 pattern.
- P8 notes: purely Italian. Han ideographs in edition P8: 0. Han
  ideographs in all edition SVGs: 0.

## Freeze diff (core vs edition)

- Every removed string is Chinese explanation-layer or Chinese furniture;
  every added string is its Italian counterpart or a documented registry
  item; zero Korean target-text changes.
- Added CJK total: 1 — the syllable 절 in P8 item 104's note
  (`104. A — 절기 = i 24 periodi dell'anno`), where the Korean headword
  절기 is cited before its Italian gloss. This is the W43 citation pattern
  (Korean headword + reader-language gloss) and the README #5 legitimate
  case for KO targets — adjudicated, not residue.

## Geometry gates (all measured, none truncated)

- Canonical `tools/occlusion_audit.py`: selftest OK (all 6 planted classes
  fire, clean controls silent). Edition: 0 flags. Core: 0 flags.
  NEW vs core: 0.
- Same-baseline ink collisions: 0 (audit TEXTX class, 0 flags).
- Full-page right-edge scan (audit ink boxes): max text ink right =
  1885.0/1885.1 on every page in both editions (right content edge, 65px
  clear of the page edge); no text ink within 5px of the right page edge.
- Full-page frame scan: 0 shapes outside page bounds on every page.
- P6 chart/table labels: later-drawn-rect ink coverage max 0% (< 30%),
  computed with the audit's getmetrics baseline-anchored ink boxes.
  (Order-agnostic 100% hits are table-cell backgrounds painted UNDER the
  labels, identical in core — not coverage.)
- Korean orphan scan (README #16: window 10–45, ≥3-syllable-tail standard,
  all prose columns incl. P8 answer lines, parenthesised fragments,
  line-start orphan punctuation, mid-word splits): run as a
  core-vs-edition differential, because the Korean text is frozen.
  A naive SVG-only scan over-flags normal word wraps, so the gate is:
  (a) pure-Korean node strings multiset — removed strings are all Chinese
  furniture / Chinese instructions (legitimate replacement); added strings
  are exactly 3, all whole-word wraps inside Italian notes/instructions,
  adjudicated below; (b) no new mid-word split, no line-start orphan
  punctuation. NEW orphan sites: 0.
  - P6 `«틀리다».` — tail of the Italian D-section instruction
    (`Se la frase è giusta scegli «맞다», se è sbagliata «틀리다».`);
    whole quoted word, not a fragment.
  - P7 `«〜부터 〜까지예요?»` — the frozen pattern title in the frame box;
    whole phrase, not a fragment.
  - P8 `바뀌었어요` — whole-word continuation of item 60's Italian note
    (`Il passato di 바뀌다 è 바뀌었어요`); split at a space, not mid-word.
- P7 letter box: label `Esempio della redazione, non vera.` + frozen
  Korean disclosure + 2-line Italian disclosure
  `Nessuna lettera vera né tema di pag. 8: la promessa passa al VOL.3. Scriveteci!`
  — covers: no real letters, no P8 compositions, VOL.3 deferral, and an
  explicit public-solicitation imperative (`Scriveteci!`) inside the
  letters box. Example-standing is covered by the label line + the frozen
  Korean disclosure. Teaser/preview/exercise-hint lines were NOT counted
  as solicitation. VOL.3 preview + letters-corner promises are carried
  as next-issue obligations.

## Images (payload basis stated)

- Basis: BOTH the base64 text embedded in the SVG and the decoded JPEG
  bytes were hashed; both match the core per page.
- Counts: 1 / 1 / 2 / 1 / 1 / 0 / 0 / 0 (P1–P8).
- P1 lumoplank CC0 — base64 `535fff46b7cef223…`, decoded `6f7f33ed8f40f3c0…`
  (JPEG 1920×1280).
- P2 wizdata CC0 — base64 `e66d2b455ec68fd1…`, decoded `96a6a19b612a4b28…`
  (JPEG 1920×1301).
- P3 Udonhan1992 CC0 — base64 `e266b6ee1a870864…`, decoded
  `158ea3a0e81f041d…` (JPEG 1920×1080); Paul Cézanne PD — base64
  `5bea45d1f81e0716…`, decoded `214cc390ac7cbcb0…` (JPEG 1920×1535).
- P4 Bain News Service PD — base64 `1a7e7d6d5ffcede7…`, decoded
  `18ad8ae06fac2860…` (JPEG 1024×743).
- P5 Gary Todd CC0 — base64 `6a1bab177d540192…`, decoded
  `35e7dc69d4178491…` (JPEG 1920×1280).
- Credit lines use the Commons API Artist field verbatim; every credited
  image is placed (payloads above). Credit lines stay in Korean
  (`사진: … — CC0 / Public domain (Wikimedia Commons) · 자료 사진`),
  exactly as in the W43 ko-it precedent — NOT a deviation.
- Only explicit public-domain/CC0 images; no other images.

## Furniture — three-way comparison (measured values)

| Item | W45 KO core | W43 ko-it | This edition (W45 ko-it) |
|---|---|---|---|
| Pairing badge | — (core has none) | `TESTI IN COREANO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI`, y=394, 20pt bold, BRICK #a4553a, width 823.58px | IDENTICAL to W43 (y=394, 20pt bold, #a4553a, 823.58px) |
| Subtitle (y=330, 40pt bold) | `한국어판 · VOL.2 · 입동 · 단풍 · 김장`, 640.91px | `SETTIMANALE COREANO · VOL.1 · 태풍 참피 · 가을야구 · 단풍`, 1176.79px | `SETTIMANALE COREANO · VOL.2 · 입동 · 단풍 · 김장`, 1009.83px |
| Footer (y=2624, 20pt) | — (Chinese footer) | `Lucerna · SETTIMANALE COREANO VOL.1 · TESTI IN COREANO · SPIEGAZIONI IN ITALIANO`, 834.86px | Same geometry, VOL.2: `Lucerna · SETTIMANALE COREANO VOL.2 · TESTI IN COREANO · SPIEGAZIONI IN ITALIANO`, 834.86px |
| Page line (y=2624, 20pt, end x=1885) | — (Chinese) | `Pagina 1 di 8`, 116.75px | IDENTICAL |
| Gloss prefix | `译注｜` | `Nota — ` | `Nota — ` (same as W43) |
| P8 E-pattern | keys 137/138 Chinese translations, notes 对照第 1/5 版; 139/140 Korean keys, notes 对照第 6/3 版 | keys 137/138 re-aimed to Italian, notes `Confronta con pag. 1/2`; 139/140 Korean keys, Italian notes; 150 apparatus Italian | keys 137/138 re-aimed to Italian, notes `Confronta con pag. 1/5`; 139/140 Korean keys, notes `Confronta con pag. 6/3`; 150 apparatus Italian |
| Type labels | 完成句子 / 单选 / 词汇配对 / 完形单选 / 造句 / 句型转换 / 判断 / 翻译 / 写作 | Completa la frase / Scelta multipla / Abbinamento / Cloze / Costruisci la frase / Trasforma la frase / Vero o falso / Traduzione / Scrittura | Same Italian labels as W43 |
| Masthead article | none (Korean) | none (Korean) | none (Korean) |
| P1 band right lines | Korean + Chinese | Italian | `L'IPDONG` 24pt bold 112.97px; `L'ipdong è sabato 7 novembre · Inizia la stagione del kimchi` 21pt 582.77px; left line 2 ends clear of the right lines' left edge |
| Box titles shortened for fit (23pt bold, inner limit 416px) | — | — | 한능검 `Iscrizioni all'esame` 353.4px (full form 450.8px rejected); 단풍 prep `Cosa portare` 329.7px (full 468.2px rejected); 청년 numbers `I numeri` 286.2px (full 414.8px rejected, 1.2px slack); numbers box `In cifre` 291.0px; winter list `Lista invernale` 330.1px |
| P1 head / P6 table title / P2 D-day strip | — | — | P1 head `지금 바로 연습 · Pratica subito` 348.4px @25pt (limit 434px); P6 table title 1049.8px @26pt bold (limit 1388px); P2 D-day right strip 771.0px @20pt |

W43 deviations (this edition vs W43 ko-it; all else identical or
issue-content-driven):
1. VOL.1 → VOL.2 (issue volume).
2. Subtitle themes: W43 (태풍 참피 · 가을야구 · 단풍) → W45 (입동 · 단풍 · 김장).
3. Letter-box trailing pad +26 → +60 (+34px): the inherited height formula
   undercounts the true content extent by ~26px — proven by the CORE's
   own geometry (the core's last letter-box line sits 26px below its box;
   the core escapes the audit only because Chinese has no descenders).
   With the 2-line Italian disclosure the last line's measured ink bottom
   is 1740.83 (baseline 1736.33 + 4.50 descent, audit PIL metrics) and the
   new border is 1743.94 (margin 3.11px). P7 col3 ends 1743.94, teaser ends
   2517.94 (< 2540).
4. P1 gloss: `ipdong` transliteration kept (ko-en precedent; the P1
   word-of-the-week gloss explains ipdong in full); 3 lines with the
   `Nota — ` prefix (prefix-aware counting — see fix log round 2).
5. P5 g1 gloss dropped `(dell'esame)` (round-2 overflow fix).
6. P1 calendar note shortened to one line (round-3 TEXTX fix).
7. P7 disclosure 3 lines → 2 lines (round-3 BOXTITLE fix).
8. P8 E redirect page refs follow THIS issue's content (pag. 1/5/6/3),
   not W43's (pag. 1/2 pattern); item numbers 137/138 verified from the
   core render.
9. Images are this issue's photos (same credit format, same per-page
   counts as the core).

## Fix log (all edits via scratch/transform.py only)

- Round 0 substring-order recovery: a short literal (`三连胜晋级`) applied
  before its long form (`KIA三连胜晋级`) corrupted the latter. Sources
  restored pristine from the core build, order fixed long-before-short,
  and a programmatic substring-collision audit found one more violation
  (`实际观测10月16日` before `설악산=实际观测10月16日 c`), also fixed.
  Post-fix audit: 0 violations, 0 duplicate old strings.
- Round 1 (missed/mistranscribed literals): `全部`→`Tutti`;
  `日期不同因为标准不同`→`Le date differiscono per il criterio`;
  `特别措施只适用于考试日`→`Le misure speciali valgono solo il giorno dell'esame`;
  `内藏山公团预报峰值11月11日`→`Naejangsan, previsione dei parchi: picco l'11 novembre`;
  `月出山林业厅预报峰值11月9日`→`Wolcchulsan, previsione forestale: picco il 9 novembre`;
  `首尔报名窗口10点至12点`→`Iscrizioni a Seul dalle 10 alle 12`.
  A feared P7 `（3版）` corruption was checked and disproven (P7 already
  read `Le date differiscono per il criterio (pag. 3)`); the `svglib.py`
  full-width paren is the legitimate kinsoku set, not residue.
- Round 2 (prefix-aware gloss fix): gloss line counts MUST be measured
  WITH the `译注｜`/`Nota — ` prefix (prefix-free counts were wrong).
  Core P1 gloss = 3 lines with prefix vs round-1 Italian = 4; core P5 g1 =
  2 lines vs round-1 Italian = 3. Each extra line pushed a later box
  across a column break (column-break cascade → FLOW OVERFLOW on P1 and
  P5). Fixes: P1 gloss → `입동 = ipdong · 절정 = picco · 김장 = kimchi invernale · 상륙하다 = toccare terra · 온대저기압 = ciclone extratropicale`
  (3 lines with prefix); P5 g1 → `정리 = ripasso · 끈끈하다 = appiccicoso · 합격 = superamento`
  (2 lines with prefix). Round-2 run: zero FLOW OVERFLOW / HEAD TOO WIDE.
- Round 3 (audit fixes, both NEW vs core):
  - (a) P1 TEXTX (real defect): the 2-line Italian calendar note's line 2
    (`numero.`, baseline 1215.08) collided with the fixed source line
    (baseline 1216.00). Fixed to one line:
    `Cinque date: l'ossatura di questo numero.` (verified 1 line at
    18.5px/390px; restores core-like clearance).
  - (b) P7 BOXTITLE: the Italian disclosure's line 2 descenders crossed
    the letter-box border by 1.9px (ink bottom 1740.8 vs border 1738.94).
    Fixed by the 2-line disclosure (see above) + the trailing-pad
    correction (+26 → +60).
  - Transform idempotency fix in the same round: entries whose output was
    superseded by a later fix entry now skip instead of failing on
    re-run (a re-run had failed at the superseded round-0 P1 gloss entry
    and applied nothing; after the fix, round 3 applied cleanly).
  - Pre-fix baselines: `hidden_files/weekly-report-w45-ko-it-build/round-baselines/round1-sha256.txt`
    (round-1 SVGs) and `round2-sha256.txt` (round-2 SVGs). Post-round-3
    check vs the round-2 baseline: ONLY p1 and p7 changed; p2–p6, p8
    byte-identical — the round-3 footprint is exactly scoped.
- Final re-render: single-process venv `run.py` (zero warnings) + venv
  `render.py`; cards/PDFs rebuilt from the final SVGs (deterministic:
  PDF byte counts identical to the round-3 render).

## Visual check (all 8 cards)

All 8 cards (1950×2700 PNGs) visually checked: no blank pages, no missing
images, no overflow, no visible collisions. P1 calendar box single-line
note clear of source lines; P7 letter box fully contains both Italian
disclosure lines; P6 table labels complete and unclipped; P8 keys list
shows the Italian E-redirects and the Italian 150 apparatus.

## Delivered files + hashes (final render)

- `svg/p1-pyoji.svg` sha256 `67593753f48125b684e668bc25b53ec78391811d258e8b60848858b09d3856c1`
- `svg/p2-saenghwal.svg` sha256 `13fa9b3e25cb4d06c0a7a65aa55843806d207a67613eab43539e8a50a717a206`
- `svg/p3-munhwa.svg` sha256 `a1804d1de00365fd5cd88f546e3b9046fff4a76e33b5857b4dd6bd74c9163798`
- `svg/p4-seupocheu.svg` sha256 `429af03560529941b0212ada96912c08fdbcd141b8f545242c6fb8b53af1d615`
- `svg/p5-cheongnyeon.svg` sha256 `5b9d433b0d74146a6e14dbccda48b60f5c016f21354af437991b671034237486`
- `svg/p6-gipi.svg` sha256 `9d5a67c7c0579173bc3cdc6d1c75cc36de65df7c343e298fa843ff9b71de20d8`
- `svg/p7-mal.svg` sha256 `02ed62e4b9f6d3765561e1f13c034411ffb50d85b6af887c92220ef4a075426b`
- `svg/p8-siheom.svg` sha256 `63896ee51b9e205b6058d27b918ae7d5bc58411ca15af2ad73b7426dbffe6abe`
- `Lucerna-VOL2-IT.pdf` (print): 8 pages, 32,551,109 bytes,
  sha256 `3daf94d0d8ab500b86a221bd6bab737fa8a0bc5244d4d13773af86e1f9daa54c`
- `Lucerna-VOL2-IT-web.pdf` (web): 8 pages, 3,558,396 bytes (< 10 MB),
  sha256 `ce556beff78568f82afca371c9f2f3eca58d7473250cd4ae10f6855e4f054e1f`
- `cards/` p1–p8 PNGs, 1950×2700 each.
- `ABSTRACT.txt`: Italian, single line, no ASCII double quotes, real topic
  keywords (ipdong 7 novembre, ultimo weekend delle foglie, stagione del
  kimchi, conto alla rovescia per l'esame) + learner search phrase
  (impara il coreano leggendo notizie vere).

## Open observations (for the independent proofreader)

1. Brief's gloss total (84) vs measured item-level total (66) — see Counts.
   The item-level gate passes; confirm the counting basis.
2. The CORE's own letter-box height formula undercounts by ~26px (its last
   line sits below its box). This edition corrects it; the core line may
   want the same note.
3. P8 item 104's cited Korean headword 절기 (see Freeze diff) — adjudicated
   legitimate; confirm the citation pattern is still desired.
4. Credit lines stay in Korean per the W43 ko-it precedent — confirm this
   is still desired for W45 (rather than Italian `Foto:` labels).
5. Orphan-scan method: the edition gate is a core-vs-edition differential
   on frozen Korean strings + adjudication of the 3 changed lines (a naive
   SVG-only scan over-flags normal wraps). The proofreader's independent
   scan should state its criterion (README #16: window 10–45,
   ≥3-syllable-tail).
6. No international politics in this issue; Korean domestic politics only
   (CSAT-day measures dated 11 November 19 only), per the editorial line.
