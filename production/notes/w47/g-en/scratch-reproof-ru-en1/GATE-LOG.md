# GATE LOG — 2026-W47 ru-en, re-proofread of the fix1 (S1) build

- Edition: `2026-w47-ru-en`, VOL.4, issue 16–22 November 2026.
- Proofer: independent re-proofread, 2026-11-11. Scratch:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-ru-en1/`
- Interpreter: repo `tools/venv/bin/python` unless noted. No production file
  written; rebuilds only in `rebuild-copy/`; delivered PDFs only read.
- Verdict: (b) — see PROOF-NOTE.md (R1 P6 title −0.7 render px, R2
  `miss-tr-en.json` stale). Everything below is what I measured myself.

## 0. Identity (checked first, before any other work)

| File | Bytes | SHA-256 (measured) | FIX-LOG final table | Match |
|---|---|---|---|---|
| `Lucerna-VOL4-ru-en.pdf` (print) | 21,251,086 | `9a159cd59f32443eb8d612eb05959ff7af3273d4c3796da0b2b2f6a7f1800b0a` | same | YES |
| `Lucerna-VOL4-ru-en-web.pdf` (web) | 3,380,694 | `7e465d67a96c3e47aa415cc530160de2df9f9b2d9f923e85366da28b8e263ed5` | same | YES |
| `2026-w47-ru-en.text.md` | 62,818 | `5960b7a649a8b50036fefa0b16580a2209bc694ea45fb5377a9ee39d9c1296ee` | same | YES |

Intermediate print SHA `023d9fd1…` (FIX-LOG line 19) is an early rebuild product,
not a deliverable. `git` untouched; no commit/push.

## 1. S1 re-measurement (the fix1 defect)

| Check | Method | Measured | Bar | Result |
|---|---|---|---|---|
| Title ink right (PIL) | `s1_measure.py`, `occlusion_audit.ink_box` per run, 23pt bold | `ТУР` 556.5–600.5; `В` 604.7–620.5; `ЦИФРАХ` 625.4–722.9; `　The round` 726.6–**865.6**; box right 961.0; clearance **95.4 px** | ink right ≤ 957 | PASS |
| Title ink right (render px) | 4× crops from DELIVERED print+web PDFs, cream col 1292, ink col 1001 | clearance **291 render px = 97.0 SVG px**, print/web crops byte-identical (`099ba2c6…`) | ≥ +5 render px | PASS |
| Four-way sync | grep content12.py:52, text.md L25, map-en.json lit, svg/p1 | all `The round`; `The round in numbers` 0× in all four | consistent | PASS (live places) |
| Fourth place | `miss-tr-en.json:33` lit value | still `The round in numbers` | consistent | **FAIL → R2** |
| Spill sweep | shared `spill.py` | 32 cream boxes, 32 titles, **0 escapes, 0 bad titles**, 43 below candidates, RESULT: PASS | 0 escapes | PASS |

## 2. Full-line box titles (32, my own measurement)

Method: `s1_measure.py` — full title line ink (all runs on the top baseline in
each cream box), PIL true ink. Proof1's sweep measured only the first run per
title and cannot see full-line overhang; its "+6.8px tightest" is a kicker-gap
value, not a title figure (see PROOF-NOTE R1).

| Rank | Page | Title (first run) | Ink right | Box right | Clearance |
|---|---|---|---|---|---|
| tightest | p6 | `ЗА` (`ЗА И ПРОТИВ　FOR AND AGAINST`) | 1862.2 | 1862.0 | **−0.2 px PIL / −0.7 px render / −1.5 px PDF bbox → R1** |
| 2nd | p1 | `В` (right-column box) | 1847.9 | 1862.0 | +14.1 px |
| 3rd | p3 | `Note — ` | 936.5 | 961.0 | +24.5 px |
| 4th | p6 | `Note — ` | 925.9 | 961.0 | +35.1 px |
| 5th | p2 | `Note — ` | 923.0 | 961.0 | +38.0 px |
| 6th | p2 | `Note — ` | 919.5 | 961.0 | +41.5 px |

Negative clearances: 1 of 32 (R1). Core p6 title for comparison: ink right
1745.4, clearance +116.6 px (fan-out-introduced overhang).

## 3. Mechanical gates

| Gate | Command / log | Measured | Result |
|---|---|---|---|
| run.py | `gates/run.log` (in `rebuild-copy/`) | rc=0, TOTAL **150** (A2 50 / B1 76 / B2 24; by page 10/18/18/18/18/18/12/38; model words 97), 0 FLOW OVERFLOW / HEAD TOO WIDE | PASS |
| Rebuild reproducibility | `gates/svg-prod.sha256` vs `gates/svg-rebuild.sha256` | all 8 SVGs byte-identical to shipped | PASS |
| Occlusion audit | `tools/occlusion_audit.py <ed>/svg --json gates/occlusion.json` | rc=1 (by-design flags-present signal); **42 TEXTX, 0 LINEX, 0 COVER, 0 FOOTER, 0 EDGE, 0 BOXTITLE** | flags present, adjudicated below |
| Occlusion adjudication (edition assets) | `adjudicate_ru.py gates/occlusion.json <edition>` | Counter {'CLEAR': 42}, 0 UNRESOLVED → **42/42 CLEAR** (incl. both P8 `ОТВЕТЫ`, gaps 19/20 px) | PASS |
| Occlusion adjudication (core assets, control) | `adjudicate_ru.py gates/occlusion.json <core-ru>` | 38 CLEAR + 4 UNRESOLVED (P5 `смартфоны`, P7 `ЯЗЫК`, P8 `ОТВЕТЫ` ×2) — adjudicator artifact, neighbour English runs exist only in the edition | artifact, not a defect |
| p8 extract | `tools/p8.py extract --p8 <ed>/svg/p8-test.svg --total 150 --json gates/p8-extract.json` | rc=0, noted set **150/150** | PASS |
| p8 compare | `tools/p8.py compare --core-p8 <core>/svg/p8-test.svg --edition-p8 <ed>/svg/p8-test.svg --total 150` | rc=0, status **CLEAN**, missing=[] extra=[] uncertain=[], **keydiff=[137, 138, 139, 140]** | PASS |
| Registry vs P8 (keycheck) | `dump_reg.py` in `rebuild-copy/` → `gates/registry.json` (150 entries) vs `gates/p8-extract.json` | **149/150** match; only Q150: registry `(Open task; model text below)` vs P8 `✓` (expected) | PASS |
| Freeze baseline (core) | `tools/freeze.py baseline --build <core-ru> --core-svg <core-ru>/svg --out gates/freeze-std` | rc=0, **8/8** SVGs byte-identical; core SVGs unchanged by the run | PASS |
| Freeze baseline (edition) | `tools/freeze.py baseline --build <ed> --core-svg <ed>/svg --out gates/freeze-ed` | rc=0, **8/8** SVGs byte-identical; repointed files: none | PASS |
| Freeze diff | `tools/freeze.py diff --core-svg <core>/svg --edition-svg <ed>/svg --json gates/freeze-diff.json` | rc=0; per page +/−: p1 +20/−21, p2 +39/−36, p3 +26/−28, p4 +28/−28, p5 +29/−27, p6 +34/−32, p7 +49/−51, p8 +173/−627; removed count-sum 850, distinct 484 (per-page-summed; global 451); added count-sum 398; Cyrillic-bearing removed exactly 15 (`можно` + 14 Morozko words); added Cyrillic 0; added CJK 8, all U+3000 (1/page); P1 added `　The round` present | PASS |
| check_core | `check_core.py <edition>` | rc=0, golden BAD **0**, gloss fails **0**, P8 SVG text 10,561 chars; 1 orphan line-start (P7 y553 `”».`, known benign) + 1 same-baseline collision (P1 y1712 `чёрная`, known) | PASS |
| s11_check | `s11_check.py <edition>` | rc=0, **FAILURES: none**; paper #fbfaf6; badges A2/B1/B2; foot VOL.4 + full-width space; VOL.3 ×1 (P4 correction); masthead 196 px; band 46 px; left margin 88.0; web 3,380,694 B < 7 MB; web text > 0; **P8 min font ≥ 9.75 pt: 9.75** | PASS |
| P8 min font (direct) | PyMuPDF spans on P8, print + web PDFs | **9.75 pt** both; 411 spans < 10 pt; 902 spans each | PASS (SOP §1.1 floor 9.75) |
| Creambox scan | detailed `creambox2.py <ed>/svg/*.svg` | 1,156 lines; diff vs proof1 `creambox.log`: **exactly 1 line** (P1 title `'The round'` vs `'The round in numbers'`) | PASS |
| Fonts (recorded only) | `pdffonts` print + web | **72 entries print, 72 web**, all emb/sub/uni; web embeds Lucerna*-renamed subsets incl. both italic faces | recorded |

## 4. Print/web text layer

| Check | Measured | Result |
|---|---|---|
| Plain `pdftotext` | **57,318 bytes each, byte-identical** (`cmp` clean) | PASS |
| `pdftotext -layout` | **111,875 bytes each, byte-identical** | PASS |
| Character multiset (fitz) | identical overall (**30,354** non-whitespace chars) and per page | PASS |
| Span-text multisets | identical, all 8 pages | PASS |
| Abutting span-pair gap diff | max **0.00 pt** | PASS |
| Intra-span char-pair gap diff | max **0.00 pt** | PASS |
| D2 pinned spots (6) | P1 headline 133.018, P4 heading 106.464, P1 contents-1 1138.695, P4 band-sub 1008.743, P1 contents-3 1122.225, P5 title 80.112 — all diff **0.000 pt** | PASS |
| D3 `а`→`»` gap | −2.193 pt both PDFs | PASS |
| D3 italic faces | web embeds `LucernaNotoSerif-Italic` + `LucernaNewsreader-Italic`; P1 italic chars 16 = print | PASS |
| D3 space char (corrected direct measurement) | bbox **[1145.576, 1266.762, 1148.108, 1288.725]**, width 2.532 pt, byte-identical print/web (= proof2 pinned values) | PASS |
| D1 straight quotes | P5 band subtitle `"Black Friday"` straight in both PDFs; no curly quotes in P5 text | PASS |
| verify_mine2 summary | all PASS except the known D3-space finder bug FAIL (script looks for consecutive `я`,`п` and misses the space char; corrected above) | PASS with note |

## 5. Kicker (9 double spaces, P1 y=372)

Method: `kicker_measure.py` — run-level ink gaps between consecutive visible
runs (separator runs stripped before `ink_box`).

| Boundary | Gap (px) |
|---|---|
| ЕЖЕНЕДЕЛЬНАЯ → ГАЗЕТА | 5.0 |
| ГАЗЕТА → ДЛЯ | 5.4 |
| ДЛЯ → ИЗУЧАЮЩИХ | 6.3 |
| ИЗУЧАЮЩИХ → РУССКИЙ | 11.8 |
| РУССКИЙ → ЯЗЫК | 8.4 |
| ЯЗЫК → — | 5.4 |
| — → НАСТОЯЩАЯ | 7.2 |
| НАСТОЯЩАЯ → РОССИЯ | 9.5 |
| , → ПО | 7.1 |

List **[5.0, 5.4, 6.3, 11.8, 8.4, 5.4, 7.2, 9.5, 7.1]**, min **5.0 px ≥ 4 — PASS**.
Reproduces fix1's list exactly. Proof1's list ([7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4,
6.8, 7.6]) not reproduced by this or fix1's method. (No-space joins excluded:
РОССИЯ→',' 0.6, ПО→'-' 0.7, '-'→'РУССКИ' 0.0 — hyphen/comma joins, not gaps.)

## 6. 150 questions (hand verification)

- text.md (838 lines) read in full by me; every stem/option/key hand-checked
  against the article text (`gates/stem-key-compare.log`,
  `gates/final-checks.log`).
- Stems (Cyrillic) vs core text.md: **0 Russian differences** (1 diff is gloss
  language only: Q46 `(можно + 不定式)` vs `(can + infinitive)`).
- Key parts vs core key list: exactly 5 diffs = Q137–140 (English translation
  keys, by design) + Q150 (open task). All other 145 key parts byte-identical.
- Stem keys vs answer-list keys: **0 mismatches** (20 matching items carry keys
  inline in the group line; all 20 agree with the answer list).
- Q20 key `желании` (registry = P8 extract = core); Q25 option `День студента`
  (text.md L187, key b); Q73 stem L405 + key list L753, P8 key `заказов`.
- Model text **97 words** (claimed 97). `___` ×87 = core ×87.
- Dates/weekdays checked with `date -d`: 16 Mon, 17 Tue, 18 Wed, 19 Thu, 20 Fri,
  21 Sat, 22 Sun; 6–8 Nov Fri–Sun; 27 Nov Fri (Black Friday); 30 Nov Mon
  (Cyber Monday). 21 goals in round 14 summed from the P4 SVG results table
  (0:1, 1:2, 1:0, 4:2, 2:0, 2:1, 2:2, 0:1); 38+26+18+18=100 chart; 20 working
  days; golden sentences 8/8 verbatim with correct page refs; error clinic 4/4.
- ABSTRACT.txt: 355 bytes, 1 line, no ASCII double quotes, VOL.4 + A2–B2 +
  150 exercises + real topics.

## 7. Regression (D1 / D2 / D6 / Q20 / Q73 / kicker / fonts)

| Item | Evidence | Result |
|---|---|---|
| D1 (core fix1, 4 KEEP strings) | text.md L459 `УЧЕБНЫЕ ДАННЫЕ`, L504 `Три уровня, три темы`, L596 `Большой тест недели + все ответы` | present |
| D2 (Q25) | `Международный день студента` ×2 = core ×2; Q25 option L187 `День студента (key b · Students' Day b)` | present |
| D6 (Q20) | `желании` ×2 = core ×2 (L173 stem + L694 key list) | present |
| Q73 | stem L405, key list L753, P8 key `заказов` | present |
| Kicker | §5 above | PASS |
| Fonts | §3, recorded only (72/72) | recorded |

## 8. SVG regression vs proof1 backup (`scratch-proof-ru-en2/rerun/svg/`)

| Page | Result |
|---|---|
| p1-pervaya.svg | DIFFERS — exactly 1 line: title run `　The round in numbers` → `　The round` |
| p2–p8 (7 files) | byte-identical |

## 9. Visual read

All 8 pages rendered from the DELIVERED print PDF (`fresh/p1.png` … `p8.png`,
975×1350) and read in full; P1/P6 title crops read at 4×. No overflow, overlap,
clipping, or missing content except R1 (invisible at 100%); P8 key complete to
Q150; no text crossing the footer line. O1 narrow-gap class visible in gloss
notes (P3 `биографияbiopic`, P5 `календарнаядатаcalendar`, P7
`Профессиональныепраздники`) — same adjudicated class as proof1 O1, readable,
byte-identical print/web; not re-flagged.
