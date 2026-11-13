# PROOF-NOTE — 2026-W47 ko-it (proof1, independent)

- Edition: `2026-w47-ko-it` (target ko, reader Italian). Builder: fan-out #3, run 1.
- Proof date: 2026-11-11. Proofer: independent (not the builder / fan-out agent).
- Work dir: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ko-it/`
  (all proof work here; nothing written to the repo side except the git-probe
  `hash-object -w` object, which is the instructed probe; no commit, no push).
- Interpreter lock honoured: freeze baseline/diff, run.py, check_core,
  check_gloss, textmd, boxtitle, keycheck, census, occlusion all on
  `/usr/bin/python3` (Pillow 10.2.0 / FreeType 2.13.2); render/webpdf on
  `tools/venv/bin/python`. The freeze.py runtime guard's ko exemption
  (Pillow 10 for the ko family) was verified in the source before running;
  no guard bypass, no tool edits.

## Verdict

**(a) 定稿零缺陷 — zero defects. Cleared for final.**

No (b) items. All carry-forward items from FANOUT-REPORT-ko3.md re-verified
independently below; every one holds.

## SHA verification (three delivered files + core, before AND after proof)

| File | Bytes | SHA-256 | Before | After |
|---|---|---|---|---|
| `Lucerna-VOL4-KO-IT.pdf` (print) | 45,676,964 | `54e35033290e55ff439025e873dab750770cfcff730f907e2fecbb9d5c0aa4b0` | ✓ match task | ✓ unchanged |
| `Lucerna-VOL4-KO-IT-web.pdf` (web) | 4,025,960 | `f6135c5054ca28278a66c8b074a578d99061a7cf93bf7a0dd0749916115a4900` | ✓ match task | ✓ unchanged |
| `2026-w47-ko-it.text.md` | 35,213 | `247ed6bd653c78b62e26a25322bef7e07a22c028cdbf3436878f6c9aad85575c` | ✓ match task | ✓ unchanged |
| core-ko `Lucerna-VOL4.pdf` | 46,232,227 | `53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27` | ✓ match FANOUT | ✓ unchanged |
| core-ko `Lucerna-VOL4-web.pdf` | 4,232,878 | `9592945ae188dc8e50394fcab1ded155baaff63161bcf0b5f7ecbc6898c43bc7` | ✓ match FANOUT | ✓ unchanged |
| core-ko `2026-w47-ko-zh-cn.text.md` | 34,606 | `da1d3a323f7c83eb95fe989e59f56ca6a706282c443f20cc5792c3f73468181a` | ✓ match FANOUT | ✓ unchanged |

- ABSTRACT.txt: 364 B, SHA `c3e23f5ab61b434c4f0b8a35e4970eec308c31cdfdc56f9d0946c255b1237fbe`
  (matches FANOUT record).
- Source md5s: `svglib.py` `1c94d836d46fcf6fc67e88b0f0febd34`,
  `textmd.py` `bc6394a387d15d4726e194687320da20` — identical to core / builder.

## Gates (all independently re-run; see GATE-LOG.md for logs)

| Gate | Result |
|---|---|
| run.py (system python3, scratch copy) | rc=0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150; A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2442, P7 teaser 2483.7 — identical to builder |
| Rebuilt SVGs | 8/8 SHA-identical to shipped SVGs (`rerun-svg.sha`) |
| freeze baseline (system python3) | **8/8 byte-identical**, rc=0; core SVGs re-hashed unchanged |
| freeze diff vs core | added CJK **7, all U+3000** (footer separators, 1 per page) |
| occlusion audit (true-ink, selftest first) | **0 flags**; selftest all 6 planted classes fired, clean controls silent; core 0 flags, NEW vs core 0 |
| p8.py extract | 150/150 noted |
| p8.py compare vs core | **CLEAN**, missing=[] extra=0 uncertain=[], keydiff=[137, 138] (E-group re-aimed at Italian — see §Adjudicated) |
| keycheck (own REG extraction vs own P8 extract) | **150/150**: 149 exact + #150 `✓` (trunc-ok, core-identical); per page 10/10, 18/18, 18/18, 18/18, 18/18, 18/18, 12/12, 38/38 |
| check_core | rc=0: gloss fails 0, P7 phrases 8/8 verbatim, orphan issues 0; dates verified (Nov 16 Mon D-3, Nov 18 Wed D-1, Nov 19 Thu D-day, Nov 22 Sun 김치의 날, Nov 28 Sat) |
| check_gloss | rc=0, gloss fails 0 |
| textmd re-export (system python3) | 449 items, **byte-identical** to shipped text.md (SHA matches) |
| print/web text layers | **byte-identical** under two independent extractors: PyMuPDF (48,319 bytes each) and pdftotext (51,894 bytes each — the builder's number; the absolute difference is extractor joining, not content) |
| web PDF re-render (scratch copy only, venv webpdf.py) | rc=0, 8 pages, text layer byte-identical to shipped web PDF; 4,025,961 B vs shipped 4,025,960 B, SHA differs (expected: fontTools clock in head.modified + CreationDate). Shipped web PDF untouched. |
| P8 min font (PyMuPDF, print PDF) | **9.975pt** ≥ 9.75pt (whole-page 359 spans; 166 at-min — same at-min set as builder's 171-span region measurement) |
| boxtitle widths | **8/8 ≤ 386.5px** (see §P5) |
| curly sweep U+201C/U+201D/U+2019 | **0/0/0** across all 8 SVGs + text.md |
| hanzi residual in `<text>` | **0** (the 3 CJK chars found by raw regex are the `<title>Lucerna 三色蛾</title>` moth-asset metadata, byte-identical in core P1 — not rendered text) |
| lone-punctuation sweep | 9 line-start `·` hits, all wrapped-option/gloss continuations (`· B. …`, `· C. …`, `· 볶음밥 = …`, `· 나누다 = …`) — same mechanism as core's 7; check_core orphan scan 0. Not a defect. |
| §1.1 style audit | paper/VOL.4/`·` counts identical to core page-by-page; P7 VOL.5 3→2 by design (removed `lko`/`lcn2` lines); unknown colours identical to core (P1 only) |
| census (ex/match + D6) | 166 items, **0 missing**; D6 missing 0 |
| 150-item three-source hand verification | own REG extraction (content files) == builder record table 150/150 rows (type/key/note/page); == P8 SVG keys 150/150; stems/notes cross-checked vs text.md via census (0 missing) + full text.md read. See §150 items. |
| 8-page visual read (100dpi PNGs from shipped print PDF) | 8/8, zero issues |
| Old-version comparison | N/A — no prior ko-it edition existed (new in fan-out #3) |

## Carry-forward checks (FANOUT-REPORT-ko3.md)

### 1. P5 box-title defect class — FIXED at map source, re-verified
- All 8 box titles fit; tightest is P2 `김장 장보기 목록　Lista della spesa`
  366.7px → **margin 19.8px**.
- P5 `이번 주 청년 숫자　Numeri giovani` = **359.4px → margin 27.1px**
  (was 399.8px as `Numeri dei giovani` before the map-source fix).
  Rendered on P5, confirmed visually inside its cream box with clear space.
- Full list (boxtitle-proof.log): 286.2 / 243.4 / 366.7 / 345.8 / 359.4 /
  320.2 / 273.0 / 330.6 px — 8/8 ≤ 386.5px.

### 2. `Tutto` is_prose quirk — classifier quirk only, no substantive effect
- Source: `content12.py:101` `("8면", "시험과 답", "Tutto")` — the level-tag
  column; core has `"全部"` at the identical position. `Tutto` is the
  faithful Italian rendering of core's `全部` (P8 covers all levels),
  exactly parallel to ko-fr's `Tout`.
- Renders correctly in the shipped P1 SVG (`x=1840, y=1600`, right-aligned
  level column) and is visible on the P1 render.
- Dropped from text.md solely by `textmd.py:is_prose`: the Latin branch
  requires a space + length ≥ 8; `Tutto` is 5 chars with no space.
  The row's other fields (`8면`, `시험과 답`) ARE in text.md, and the P8
  header `시험과 답 Test e risposte` carries the Italian elsewhere.
  No content is lost anywhere a reader looks (PDF, SVG, text.md prose).

### 3. `작황 = il raccolto` (gloss choice, not a defect)
- Core gloss (content12.py:174): `작황 收成、长势`. it: `il raccolto`;
  de chose `Ernteaussichten`. `il raccolto` (the harvest) is a defensible
  A2 short gloss for 작황; the `长势` (growth-conditions) nuance is not
  fully captured by either Latin gloss. No correction warranted; recorded
  for the record, not counted as a finding.

## 150 items — three-source hand verification

- Source 1 (edition sources): fresh independent REG extraction
  (`reg150.py`, own code path — `ex()` args + `match_set` expansion +
  `CURPAGE` tracking) = 150 items, pages 10/18/18/18/18/18/12/38.
- Source 2 (builder record table): 150/150 rows match on
  (n, page, type, key, note); the single apparent diff is my regex
  capturing the record's `#150` SVG cell as `OK ✓` instead of `OK` —
  a parsing artefact, not a content difference.
- Source 3 (P8 SVG keys, own `p8.py extract`): 0 mismatches
  (150/150; #150 `✓` adjudicated, core-identical).
- Notes audit: 25 notes contain Hangul — every one is the item's own
  Korean headword/answer form (`내장산 = previsione di Weatheri`,
  `이기다: passato 이겼어요`, `「에서」` as the grammar point, etc.),
  i.e. headword references by design. No untranslated residue.
- Stems audit: Latin letters in stems are only proper names
  (`kt wiz`, `LG`, `kt`) and the two P8 translation items #139/#140,
  whose Italian source sentences are the exercise by design.
- Full text.md read (449 items, both chunks): dates, D-counts, prices
  (199,456 / 54,980 / 219,071 / 5,557), scores (4-1, 12-1, 8-7),
  and the P5/P6 Nov-19-only measures statement all consistent with the
  sources and with check_core's date arithmetic. P7 Frame line carries
  the new core sentence `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요`
  with straight 「」 quotes; the editorial note correctly discloses the
  example letter / no real letters / promise moved to VOL.5.

## Adjudicated (not defects — inherited from core or by design)

- p8 keydiff [137, 138]: E-group translation items re-aimed at Italian
  (#137 `Il 22 nov. è il Giorno del Kimchi. — Vedi p. 2`,
  #138 `Samsung ha vinto il titolo dopo 12 anni. — Vedi p. 4`) — W46 precedent.
- #150 key renders as `✓` in core and edition alike; the
  `(compito libero — testo modello qui sotto)` text is the exercise stem,
  not the printed key. H model text (169 chars) present on P8.
- P8 match-item notes repeat the option letter: the letter is in the
  source note literal itself — core's own convention.
- #43/#123/#124 `previsione di Weatheri`: core's own rendering of 웨더아이
  (private weather company, corrected in core run 4) — not a typo.
- text.md 449 vs core 452: exactly 3 accounted drops — `Tutto`
  (is_prose quirk, §2 above), `lcn2` + `lko` removed by design.
- Freeze diff added CJK 7, all U+3000 footer separators — same pattern as
  the other Latin editions.
- P7 VOL.5 3→2 by design (removed `lko`/`lcn2` disclosure lines).
- P8 answer-note stem 10.35pt is the recorded core adjudication.
- P4/P5/P6 mid-page whitespace is the core's own feature-ends-early
  geometry (P4-feature ends y=740, P5 y=881, P6 y=515) — layout as designed.

## "next Sunday" freeze rule
- Searched `core-ko/`, `2026-w47-ko-it/` (`*.py`, `*.md`, `*.json`) and
  `tools/tables.py`: **0 hits** for "next Sunday". The rule has no
  applicable object in this edition; nothing was applied or assumed.

## D5 font census (recorded only, no verdict per task)
- `Noto Sans CJK SC` segments in the 8 it SVGs: **0**.
- Font families actually used (`<text>` elements): it `Noto Sans CJK KR`
  620 / `Noto Serif CJK KR` 881 / `UnifrakturMaguntia` 1; core 603 / 877 / 1.
  (The Latin explanation layer is set in Noto Sans CJK KR; recorded as a
  count only.)

## Defect list
**None — zero defects.** No (b) items, no repairs routed.

## Notes on method
- `~/workspace/weekly-git/AGENTS.md` was read during this proof (runtime
  house-rules notice). Its "run Python tools with tools/venv" line is the
  general rule; this family's task brief + the freeze.py guard's ko
  exemption (Pillow 10, system python3) govern ko builds, and were
  followed — no conflict arose in practice.
- One self-caught procedural correction: the first occlusion run used
  `--selftest`, which runs ONLY the selftest (no directory audit); the
  gate was re-run without the flag, with `--core core-ko/svg`, giving the
  0-flags result above. The earlier 1-line log is superseded by
  `occlusion-proof.log` / `occlusion-proof.json`.
- Freeze `--out` build-copy (11 MB) and the scratch web re-render
  (4,025,961 B) were deleted after their results were logged; the shipped
  web PDF was never overwritten (re-render written only to the scratch dir).
