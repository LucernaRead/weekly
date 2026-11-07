# Lucerna Semanario · VOL.1 — Edición zh-TW × ES (繁體中文 × Español)

Fan-out edition of the frozen Traditional Chinese core (VOL.1, week of Mon 19 – Sun 25 Oct 2026):
Traditional Chinese target text unchanged; **all** explanation layer rewritten in Spanish for
Spanish-speaking readers. Built 2026-10-21 by the fan-out builder line. **Independent proofread: PASS (2026-10-21, zero problems — record in §10).**

- Build code: `hidden_files/weekly-report-zhtw-es-build/` (copy of the core build, explanation layer only edited)
- Deliverables in this directory: `svg/` ×8, `cards/` ×8 (1950×2700), `Lucerna-VOL1-ES.pdf` (print),
  `Lucerna-VOL1-ES-web.pdf` (web)

## 1. Baseline proof (method step 1)

The core build directory was copied to `hidden_files/weekly-report-zhtw-es-build/` and run
**unmodified** (only output paths retargeted). All 8 generated SVGs were **byte-identical**
(sha256, 8/8) to the shipped core SVGs in `files/weekly-report-zhtw-vol1/svg/`:

| page | core shipped sha256 |
|---|---|
| p1-front | c37cb10e6c55212a1f611005e73493fe00cedb97a32d68119059185225ebbf0d |
| p2-life | 494af3dafa61625002a1658ff6934fb8539d4821a96719321d429ae525b1e35b |
| p3-culture | 15315e2e8e6cf4731006cdad2052ba22df7061587108f40ba15fcbdaa61040e6 |
| p4-sport | 02d393f9e0a3aa0613e2eaaed211ea384f2f99a0e3095a1e982a80dbfe298cfc |
| p5-youth | fc677f717cbed9675a6d3da7f0b904176cad4714e3247f817353883ce5f9fb58 |
| p6-deep | 1367d4f03a66375ee8000f010d59881cd898fa02baad3f71d5b18275815b2d0d |
| p7-lang | 873a21acba1bf16df0fd23936f1e45800320766763a5caccc6cfd63dedded0e0 |
| p8-test | c532615cbc6df045db8a52662f6e186946aaf37accc6c0fa50ea87a3a79e0743 |

Only after this proof was the explanation layer edited.

## 2. Totals (registry diff vs core: structure identical)

- **150 exercises** — A2 56 · B1 65 · B2 29 (levels identical to core)
- Per page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38 (identical to core)
- Types: 單選 65 · 完成句子 52 · 配對 20 · 完形單選 12 · 寫作 1 (identical)
- Writing model: 134 characters, printed verbatim (verified byte-identical in both editions' P8)
- Final build log: **zero warnings** (no flow overflow, no over-wide heads, no wrap overflow)

## 3. Key-diff registry (the ONLY answer-key change)

Registry dump comparison (structure n/page/level/type: zero diffs) shows exactly **one** key change:

| # | core key | ES key |
|---|---|---|
| 150 | (開放題，範文如下) | (pregunta abierta — modelo a continuación) |

#150 is the open writing task; its key legitimately re-aims at Spanish. Items #137 (品味) and #138 (留友)
are Chinese fill-in keys — target layer, **unchanged** (same as the zh-TW×FR and zh-CN×FR precedents,
where the key diff was likewise #150 only). All 150 P8 answer **notes** were rewritten in Spanish;
none is identical to its English core note.

## 4. CJK invariant & freeze check

- Per-page CJK character multiset diff (core vs ES final SVGs): **zero characters added on every page.**
- Removals are only: the old pairing badge string and footer pairing string (replaced by the Spanish
  furniture below), the English gloss-label prefixes inside `Nota —` boxes, and punctuation-style
  normalisation inside Spanish explanation paragraphs (「」→«», full-width→half-width parentheses in
  P8 key lines, per the established fan-out key format).
- Node-level text diff vs core: every changed node is explanation layer, pairing furniture, a
  documented registry item (§3), or a line-wrap fragment of one of those. No Chinese target string changed.
- OpenCC s2t pass over the visible text behaves identically in both editions (96 variant mappings,
  same distribution — the core's own 台/吃/胡/同 variants; this edition adds none).

## 5. Furniture-string inventory (ES column pattern; widths measured with real font metrics)

- P1 badge (BRICK, size 21, measured 1248px < 1820): `TEXTOS EN CHINO TRADICIONAL · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`
- Footer (all pages): `Lucerna · SEMANARIO CHINO TRADICIONAL VOL.1 · TEXTO EN CHINO TRADICIONAL · EXPLICACIONES EN ESPAÑOL` (measured 1093px) / `Página N de 8`
- Masthead: `Lucerna` (no article), exactly as the core ships
- Gloss prefix: `Nota — ` (replaces the core's English gloss labels)
- Instructions: `Completa` (fill-in, 52×); matching per set — P2/P3 `Une palabra y definición`,
  P4 `Une nombre y dato`, P5 `Une evento y dato`, P6 `Une boleto y dato`; `Redacción` (writing)
- Answer-key format: space before each note parenthesis, half-width parens only; page headers `— Página N —`
- Spanish conventions: thousands with dot (5.000, 40.000), amounts as `258 HK$`, «» quotes inside Spanish text
- Photo credit lines kept byte-identical English (same as the FR fan-out precedent)

## 6. Builder's proofread (own pass, completed)

- Every page read end-to-end in final rendered form; all 150 keys re-derived from the Chinese text.
- P7 phrases of the week: all 8 are verbatim contiguous excerpts; each occurs exactly 2× in the issue;
  page tags (p. 1, 2, 3, 3, 4, 5, 6, 6) correct; writing model verbatim in P8.
- Calendar: every weekday/date claim verified against the real 2026 calendar (重陽 Sun 10/18; HK holiday
  Mon 10/19; G3 Tue 10/20; G4 Wed 10/21; Golden Bell Fri 10/23 + Sat 10/24; 連假 Sat–Mon 10/24–26;
  疏運 10/23–27; Wine & Dine opens Thu 10/29, ends Sun 11/1).
- Wine & Dine arithmetic re-verified in the rendered Spanish apparatus: 40+200+160=400, 400−258=142;
  40+400+260+200=900, 900−558=342; model answer 2×258=516. Figures carried exactly (258 / 400 / 142;
  558 / 900 / 342).
- English-residue scan of final SVG text: no English function words remain (hits are Spanish *a/no*,
  the name 阿May, and option letters).

## 7. Geometric occlusion audit (mandatory gate) — `audit_zh_tw_es.py`

Script validated first on a synthetic positive control: all six planted defect classes fired
(COVER, LINEX, FOOTER, EDGE, STRADDLE, TT-OVERLAP); a clean control page produced 0 flags.
Initial run on this edition: 3 flags.

1. **P2 STRADDLE (real defect, fixed by wording):** the Spanish "Ahora tú" line ended at baseline 1326,
   crossing its box's bottom border (1322). Shortened to «¿Adónde irías en un puente de 3 días?»
   (3 lines → 2). Re-audit: clean.
2. **P6 STRADDLE (real defect, fixed by wording):** the pass-box closing note ended at baseline 1403 vs
   box bottom 1398. Shortened the premium-pass paragraph (6→5 lines) and the note (3→2 lines):
   «Contenido según el desglose oficial; el ahorro es cálculo nuestro.» Re-audit: clean.
3. **P1 LINEX (inherited from core, pixel-adjudicated non-defect):** 'Lucerna' wordmark vs the masthead
   rule. Pixel measurement on the rendered card: wordmark ink bottom = row 221; rows 222–266 contain
   zero dark pixels; the rule sits at rows 267–268 — 45 rows of clear air. Font-metric artifact, same
   flag the core itself produces.

Earlier build-time findings, also fixed by wording only: P7 column-3 flow would have pushed the VOL.2
teaser box past the footer rule (end 2594.66 > 2580) — six Spanish strings tightened, column 3 now ends
at 1649.6, teaser ends 2498; five bilingual heads/box titles shortened after PIL width measurement
(¿Entendido?; El calendario; Partidos; Palabra de la semana; Plan de fin de semana kept as measured inside).

**Final audit state: 0 unresolved flags** (1 inherited, pixel-cleared). All 8 cards visually inspected.

## 8. Image credits (from the core KIT; images unchanged)

| page | file | credit |
|---|---|---|
| P1 | typhoon.jpg | NASA Johnson Space Center — Public domain |
| P2 | rain.jpg | CorraleH — CC0 |
| P3 | chrysanthemum.jpg | Masaki Ikeda (池田正樹) — Public domain |
| P3 | crab.jpg | Fumikas Sagisavas — CC0 |
| P4 | baseball.jpg | unknown author — Public domain |
| P5 | stage.jpg | Kurt Kaiser — CC0 |
| P5 | pumpkin.jpg | Benjamin Balazs — CC0 |
| P6 | harbour.jpg | Wilfredor — CC0 |
| P6 | wine.jpg | Jon Sullivan — Public domain |

(All via Wikimedia Commons; credit lines printed on the pages.)

## 9. Deliverable pins

| file | bytes | sha256 |
|---|---|---|
| Lucerna-VOL1-ES.pdf (print) | 38,405,560 | 9f727fc7191d0c1813a88383cd3c18bafe340eae9c3d6f8be61528a4ac7715ef |
| Lucerna-VOL1-ES-web.pdf (web) | 3,613,115 | 319e5b988998d2a74b4b242fe5d0557229c628c4ac7a5db305f6e90172a21af3 |
| svg/p1-front.svg | 197,790 | 696b342eacbc8006268ca05c126dfa339e06bdbc075ef4bd691602cc7adf1780 |
| svg/p2-life.svg | 361,163 | 17318faab7684ef03e9472e80179f54e3d49c5ad48cec583524e650f2ce81a2a |
| svg/p3-culture.svg | 1,044,529 | 0ee3aa3fbb12ce7bdc5e15411da4e48c9fe26ddacfde5d1cbd7bddcc4de5d636 |
| svg/p4-sport.svg | 792,048 | dae53230d2be9fd59b5cfd44f0373d0c699f3e2d8692be6b5a6de0d8cb381a90 |
| svg/p5-youth.svg | — | efa9523699943a0898e6ed0d53b973fce272e95c123213f9ebcfe08cc4632976 |
| svg/p6-deep.svg | — | 7d37244810910c867973a9be9237f2555cb28b6856e06118234e177534ebb9b0 |
| svg/p7-lang.svg | — | 0326e8f99465ad336a18b6315a7ecc94753eee6468c7eafcae4593f0f41421bf |
| svg/p8-test.svg | — | 5f13a68fc8d7e897f160dd12add1c6c3f881a1e0f6736f5be0b2d388223f4880 |

Web PDF 3,613,115 B < 10 MB ✓. Terminology scan: the banned intermediary-layer term (either script)
occurs 0 times in the paper, this KIT, and the build code.

## 10. Status

Builder's proofread: complete (see §6–§7). No repo insert, no Discord post (per assignment scope).

**Independent proofread: PASS — 2026-10-21, one complete pass, ZERO problems found.** The
proofreader worked independently of the builder (own extraction, own audit code, own registry
dumps from fresh runs of both build sources) and verified:

- **Reproducibility:** fresh runs of the core and ES build sources regenerated all 16 SVGs
  byte-identical to the shipped files (core 8/8 = §1 baseline table; ES 8/8 = §9 pin table).
- **Freeze diff:** node-level text diff vs the core on all 8 pages — every difference is
  explanation layer / pairing furniture / registered items; nothing else moved. CJK character
  multiset per page: ZERO characters added on every page; removals only the old pairing
  furniture (badge/footer strings) and gloss prefixes. OpenCC s2t behaviour identical in both
  editions: 96 mapped characters, the same 9 legitimate Taiwan variant pairs (台→臺 ×62,
  吃→喫 ×23, 胡→衚 ×3, 同→衕 ×3, 出→齣, 表→錶, 峰→峯, 粽→糉, 才→纔) — no simplified-script
  contamination.
- **Registry diff (both registries dumped from source):** structure identical (page/level/type
  for all 150); totals 150 = A2 56 · B1 65 · B2 29; per-page 10/18/18/18/18/18/12/38;
  **key diff = EXACTLY ONE (#150 apparatus line)**; all 150 notes rewritten in Spanish (none
  identical to the core's English, none empty).
- **Keys re-derived:** printed P8 keys parsed from both editions — numbering 1–150 complete in
  both, all key tokens identical except #150; every arithmetic key recomputed (incl. Wine &
  Dine 400−258=142, 900−558=342, 2×258=516 in the writing model); factual keys consistent
  with the articles and the calendar.
- **PRINTED-NOTE SET EQUALITY:** the core build prints all 150 notes unconditionally (rule
  read in the core source); this edition's P8 prints all 150 (parsed). Sets EQUAL = {1…150}.
- **Spanish completeness:** every explanation element read in Spanish across all 8 pages;
  English function-word scan over the visible text = 0 hits; raw-byte term scan finds only
  Spanish words and proper nouns. Politics-term scan = 0.
- **P7 phrases:** all 8 verbatim contiguous excerpts, tags (p. 1, 2, 3, 3, 4, 5, 6, 6), each
  occurring exactly 2× in the full-issue text (1× on its tagged page + 1× on P7). Writing
  model identical to the core's, 134 characters (programmatic comparison).
- **Calendar:** all weekday claims verified against the real 2026 calendar (G1 Sat Oct 17,
  重陽 Sun Oct 18, HK holiday Mon Oct 19, Golden Bell Fri–Sat Oct 23–24, Wine & Dine Thu
  Oct 29 – Sun Nov 1, plus G3–G7, parade Sun Oct 25, main event Mon Oct 26).
- **Furniture:** P1 badge exact; pairing footer + «Página N de 8» on all 8 pages; masthead
  «Lucerna» with no article.
- **Geometric occlusion audit (proofreader's own implementation):** PIL real-font metrics
  (Noto CJK, TC index 3), ink bands baseline −0.88em/+0.30em, line boxes expanded by half
  stroke width, synthetic positive control firing all 6 planted classes (COVER / LINEX /
  FOOTER / EDGE / STRADDLE / TT-OVERLAP) before the real run. Real run: exactly ONE flag —
  the inherited P1 LINEX, pixel-adjudicated NON-DEFECT on the shipped card (wordmark ink rows
  93–221, rows 222–266 empty, rule rows 267–268). The two builder STRADDLE fixes pixel-verified
  on the shipped cards: P2 «Ahora tú» box — last ink row 1304 vs bottom border 1322; P6 pass
  box — closing-note ink ends row 1347 vs box bottom 1398. No other flags on any page.
- **Images & PDFs:** all 9 image payloads byte-identical to the core per page; printed credits
  match the core KIT table on every card (visual check of all 8 cards). Web PDF verified by
  the proofreader's own hashing: **3,613,115 B, sha256
  319e5b988998d2a74b4b242fe5d0557229c628c4ac7a5db305f6e90172a21af3** (< 10 MB); print PDF
  38,405,560 B, sha256 9f727fc7191d0c1813a88383cd3c18bafe340eae9c3d6f8be61528a4ac7715ef;
  both 8 pages.
- **Banned term:** 0 occurrences in the paper SVGs, this KIT, the build code, and both PDFs'
  text layers.

**Verdict: PASS. This edition is final and cleared for repo insertion by the parent line.**
(Proofreader scratch: hidden_files/proof-zhtwes-independent/.)
