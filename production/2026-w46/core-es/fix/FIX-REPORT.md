# Fix Report — W46 ES family, Round 1 defects D-1–D-5
## Editions fixed: 2026-w46-es-de and 2026-w46-es-ko ONLY

- **Issue:** VOL.3, week Mon 2026-11-09 – Sun 2026-11-15. Target language Spanish; reader-native German (de) / Korean (ko).
- **Authority:** Round 1 independent proofread verdict `hidden_files/w46/es-proofread-gates/proofreader-verdict-round1.md` (FAIL: D-1 in DE, D-2–D-5 in KO; the other 9 editions PASSED and were NOT touched — no file in any other edition dir was read for writing, edited, or re-rendered; `~/workspace/weekly-git` was never touched; `index.json` was never edited; nothing was pushed, inserted, or posted).
- **Method:** every fix AT THE SOURCE in the edition transform tables; full re-render of both editions through the single driver (`hidden_files/w46/build_one.py`, which copies the fixed core build, applies the transforms, runs `run.py` in one process, renders via `tools/venv`, and runs freeze/p8/occlusion). No rendered SVG or PDF was hand-edited. `.text.md` files were regenerated with `hidden_files/w46/es_textmd.py` from each edition's own SVG text layer (never from PDF; existing headers preserved verbatim — verified: the exporter reproduces the pre-fix files byte-identically when run on the pre-fix SVGs, and the post-fix diffs touch only the fixed passages).
- **Seed record (unchanged):** VOL.3, 150 exercises (A2 50 / B1 72 / B2 28), per page 10/18/18/18/18/18/12/38.
- **Status:** fixes applied and re-gated as below. A Round 2 independent proofread follows; this report and its re-gating do NOT replace it.

---

## 1. Fixes, with before/after quotes

### D-1 (BLOCKING, es-de only) — P7 golden sentences Q6, ungrammatical German translation

- **Source file:** `hidden_files/w46/t_de2.py`, line 107 (transform pair scoped to `content7.py`).
- **Frozen Spanish quote (unchanged):** `«La vivienda preocupa al 86,9 % de los españoles.»`
- **Before (printed translation):** `Die Wohnung sorgt 86,9 % der Spanier. (Página 6)`
- **After (printed translation):** `86,9 % der Spanier sorgen sich um die Wohnung. (Página 6)`
- **Choice rationale:** the `sich sorgen um` construction is the wording most consistent with the edition's own usage — DE P8 answer 127 reads `CIS-Wohnungsbarometer: 86,9 % sorgen sich um die Wohnung` (correct, unchanged). The alternative in the verdict (`Die Wohnungsfrage bereitet 86,9 % der Spanier Sorgen.`) was not used. The frozen Spanish quote and the `(Página 6)` page label are unchanged.
- **Verification:** rendered DE P7 SVG line reads `86,9 % der Spanier sorgen sich um die Wohnung. (Página 6)`; the defective string `Die Wohnung sorgt` occurs 0 times in the edition SVGs; all 8 P7 quotes + 8 translations verified (see §4); DE P7 card viewed full-frame — the fixed translation sits on one clean line under the frozen quote, no overflow/overlap.

### D-2 (BLOCKING, es-ko only) — P1 cifras box, word split `총|파업`

- **Source file:** `hidden_files/w46/t_ko.py`, cifras pair scoped to `content12.py`.
- **Before:** `24 — horas dura la huelga general del miércoles 11 de noviembre (11월 11일 총파업은 24시간이에요)`
- **After:** `24 — horas dura la huelga general del miércoles 11 de noviembre (11월 11일, 총파업 24시간이에요)`
- **Meaning/facts preserved:** date (11월 11일), general strike (총파업), 24 hours (24시간) all present; the parenthetical still glosses the same Spanish clause. Only the connective was restructured (은 → comma) so the wrap break falls at the space after the comma.
- **Rendered lines (P1, x=545, 20.5pt):** `miércoles 11 de noviembre (11월 11일,` → `총파업 24시간이에요)` — `총파업` whole. Verified visually on the KO P1 card.

### D-3 (BLOCKING, es-ko only) — P2 calendar, word split `세|스타오`

- **Source file:** `hidden_files/w46/t_ko.py`, calendar pair scoped to `content12.py`.
- **Before:** `(토요일 세스타오에서 연방컵 결승)`
- **After:** `(토요일에 세스타오에서 열리는 연방컵 결승)`
- **Meaning/facts preserved:** Saturday (토요일), Sestao (세스타오), Federation Cup final (연방컵 결승) all present; `열리는` ("held") makes explicit what the final being in Sestao already implied — no new fact.
- **Rendered lines (P2, x=545, 21pt):** `Federación en Sestao, 19:00 (토요일에` → `세스타오에서 열리는 연방컵 결승)` — `세스타오` whole. Verified visually on the KO P2 card.
- **Scan note:** the independent orphan scan flags this fixed site as a candidate (see §2, candidate #1) because the previous line ends in Hangul and the continuation's first word has ≥3 syllables. It is adjudicated a FALSE POSITIVE: the break falls at the space between the complete words `토요일에` and `세스타오에서` in the source string — a word-boundary wrap, not a mid-word split.

### D-4 (BLOCKING, es-ko only) — P4 exercise instruction, word split `채|우세요`

- **Source file:** `hidden_files/w46/t_ko.py`, bridge pair scoped to `content34.py` (section C, comparatives).
- **Before:** `괄호 안 단어의 비교급이나 -ísimo 형태로 빈칸을 채우세요.`
- **After:** `빈칸을 채우세요. 괄호 안 단어의 비교급이나 -ísimo 형태를 쓰세요.`
- **Meaning/instruction semantics preserved:** same two instructions in two sentences — "Fill in the blanks. Use the comparative or -ísimo form of the word in the parentheses." The Chinese source (`用括号里词的比较级或 -ísimo 形式填空。`) is unchanged and still fully rendered.
- **Rendered lines (P4, x=527, 20.5pt):** `빈칸을 채우세요. 괄호 안 단어의 비교급이나 -ísimo` → `형태를 쓰세요.` — `채우세요` whole on line 1. Verified visually on the KO P4 card. (The renderer absorbed `-ísimo` onto line 1; the break remains at a space between complete words either way.)

### D-5 (BLOCKING, es-ko only) — P5 exercise instruction, word split `나타|내세요`

- **Source file:** `hidden_files/w46/t_ko2.py`, bridge pair scoped to `content56.py` (section C, ir a + infinitive).
- **Before:** `ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’을 나타내세요.`
- **After:** `ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’이라는 뜻을 나타내세요.`
- **Meaning/instruction semantics preserved:** all elements kept — `ir a + 동사 원형`, rewrite the sentences (문장을 바꿔), express '~will' (’~할 것’이라는 뜻을 나타내세요). The Chinese source (`用 ir a + 原形动词改写句子，表示“将要”。`) is unchanged and still fully rendered.
- **Rendered lines (P5, x=527, 20.5pt):** `ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’이라는` → `뜻을 나타내세요.` — `나타내세요` whole on line 2. Verified visually on the KO P5 card.

**Rewording method (all four KO fixes):** candidates were wrap-simulated offline with a verbatim copy of the build `svglib.py` wrap/measurement code (`es-fix/sim_wrap.py`, `es-fix/sim_candidates.py`, `sim_candidates2.py`, `sim_candidates3.py`) at the true draw widths/fonts (cifras/calendar: serif 20.5/21pt, width 398; bridges: sans 20.5pt, width 434). Candidates were chosen so the wrap break falls at a space with the at-risk word whole and with slack against the renderer's ~1-syllable measurement variance (the build KIT notes the offline estimate can run ~10px under the render). The rendered SVGs were then verified directly by line dumps, the full orphan scan, and full-frame card reads — the simulation was a guide, not the gate.

**Fixes NOT applied as specified:** none. All five defects were fixed exactly as the verdict specified. (M-6 and the M-5 ruling are checks/decisions, recorded in §3 — neither required a content fix.)

---

## 2. Full KO orphan scan — binding README #16 standard (FULL RESULTS)

- **Standard:** tools README #16 (extended): window 10–45 (line pitch), line-initial orphan punctuation AND mid-word splits with ≥3-syllable tails, for EVERY prose column (calendar, plan, ¿Y TÚ?, cifras boxes, glosses, bridges, P8 notes — including parenthesised fragments).
- **Implementation:** verbatim copy of the proofreader's independent scan (`es-fix/ko_orphan_independent.py`, run from `es-fix/` against the FINAL KO SVGs; output saved as `es-fix/ko-orphan-independent-round2.txt`). The builder's narrower `es_ko_orphan.py` (S1/S2 only) was also re-run as a supplement: **0 reports, groupings agree** (`es-fix/es_ko_orphan-round2.txt`).
- **Round 1 baseline (same script, pre-fix):** 12 candidates — the 4 defects D-2–D-5 + 8 false positives.
- **Round 2 result (post-fix): 9 candidates, 0 TRUE splits.** All 9 are adjudicated FALSE POSITIVES (breaks at word boundaries). The complete candidate list, verbatim from the scan output:

| # | File | Type | Lines (y) | Previous line tail | Continuation line head | Adjudication |
|---|---|---|---|---|---|---|
| 1 | p2-vida.svg | TAIL≥3 | 887.5 → 916.1 | `Federación en Sestao, 19:00 (토요일에` | `세스타오에서 열리는 연방컵 결승)` | FALSE POSITIVE (new, at fixed D-3 site): break at the space between complete words `토요일에` and `세스타오에서` in the source string. Not a mid-word split. |
| 2 | p2-vida.svg | TAIL≥3 | 268.2 → 298.0 | `sindicato는 노동조합이에요 · el salario는` | `월급이에요 · el alquiler는 임대료예요 · los` | FALSE POSITIVE (Round 1 #3, byte-identical): break after particle `는`; continuation is a new word. |
| 3 | p3-cultura.svg | TAIL≥3 | 387.5 → 417.2 | `해설 — la capa는 망토예요 · el mendigo는` | `거지예요 · el veranillo는 늦가을 따뜻한 날,` | FALSE POSITIVE (Round 1 #4, byte-identical): break after particle `는`; continuation is a new word. |
| 4 | p3-cultura.svg | TAIL≥3 | 1472.3 → 1500.7 | `veranillo 같은 늦가을 따뜻한 날이 있나요? 두` | `문장을 써서 보내 주세요.` | FALSE POSITIVE (Round 1 #5, byte-identical): break after complete word `두`; continuation is a new word. |
| 5 | p4-deporte.svg | TAIL≥3 | 843.1 → 871.5 | `일요일 20:45에 어떤 경기를 보세요? 스페인 대` | `잉글랜드, 누가 이길까요? 답을 스페인어로 두` | FALSE POSITIVE (Round 1 #6, byte-identical): break after complete word `대`; continuation is a new word. |
| 6 | p5-juventud.svg | TAIL≥3 | 885.8 → 915.5 | `해설 — el sobre는 봉투예요 · la papeleta는` | `투표용지예요 · el censo는 명부예요 · la` | FALSE POSITIVE (Round 1 #7, byte-identical): break after particle `는`; continuation is a new word. |
| 7 | p7-lengua.svg | TAIL≥3 | 1191.2 → 1219.6 | `huelga general = 총파업: 모두가 같은 날 일을` | `멈춰요.` | FALSE POSITIVE (Round 1 #10, byte-identical): break after complete word `일을`; continuation is a new word. |
| 8 | p8-ejercicios.svg | TAIL≥3 | 2328.0 → 2343.7 | ` Falso — 우마니타리오스 축제는 아스투리아스에서 열려요, 갈리시아가` | `아니에요` | FALSE POSITIVE (Round 1 #11, byte-identical): break after complete word `갈리시아가`; continuation is a new word. |
| 9 | p8-ejercicios.svg | TAIL≥3 | 2403.0 → 2418.7 | `성 마르틴 식사에는 fabada, casadiellas, panchón이` | `나와요` | FALSE POSITIVE (Round 1 #12, byte-identical): break after particle `이`; continuation is a new word. |

- **Defect sites now clean:** D-2 (P1 cifras), D-4 (P4 bridge), D-5 (P5 bridge) produce NO scan candidates at all. D-3 produces only candidate #1 above, adjudicated a word-boundary false positive. No S1 line-initial orphan-punctuation flags were raised anywhere in the KO edition.
- **Conclusion:** 0 true mid-word splits remain in the KO edition under the binding standard. The 8 Round 1 false positives recur byte-identically (same files, y-coordinates, and text) and stay adjudicated as such.

---

## 3. M-6 CHECK and coordinator ruling M-5

### M-6 — core dir ABSTRACT.txt wording: STALE ARTIFACT, LEFT UNTOUCHED

- **Finding:** `files/weekly-report-w46-es-core/` is a stale artifact / frozen-core reference, NOT a shippable edition dir. Its abstract was NOT rewritten and it was NOT re-gated.
- **Evidence:**
  1. Its own KIT (`files/weekly-report-w46-es-core/WEEKLY-KIT.md`) self-identifies it as the core: "VOL.3（西班牙语核心版第三期）" (Spanish core edition, VOL.3), with explanation layer in Chinese as the core's reference explanations.
  2. Its deliverable names do not follow the 11-edition pattern: PDFs are `La-Lucerna-VOL3.pdf` / `La-Lucerna-VOL3-web.pdf` (no native-language suffix, unlike e.g. `La-Lucerna-VOL3-DE.pdf`), and its text file is `2026-w46-es-core.text.md` (the slug `2026-w46-es-core` is not one of the 11 edition slugs).
  3. The shared toolkit treats it as the frozen reference: `tools/freeze.py diff --core-svg` points at its `svg/` dir, and `build_one.py` copies its build dir (`hidden_files/weekly-report-w46-es-build`) as the base for every fan-out.
  4. The shippable Chinese-explanation edition exists separately as `files/weekly-report-w46-es-zh-cn/` (Round 1 PASS, practice-framed abstract, own suffixed render) — the core dir is not needed to ship a Chinese edition.
  5. The Round 1 verdict states the same ("a stale artifact dir and was used only as the frozen-core reference, not as an edition"), and the coordinator's reconciliation confirms it ("es-core is a stale artifact, ignore").
- **Consequence:** the core `ABSTRACT.txt` wording (`通过西班牙新闻学西班牙语`) was left exactly as-is. No other edition's abstract was touched (all 11 pass).

### M-5 — disclosure asymmetry (DE/NL/RU native notes): NO ACTION, per coordinator ruling

ACCEPTED as non-defect: the full disclosure IS on the page in the frozen Spanish text directly above each native note in the same letters box (geometry verified by the proofreader). No native-note text was added to the DE edition. The DE letters box is byte-identical to the pre-fix render (P7 change is confined to the Q6 translation line; letters-box geometry unchanged).

### Also unchanged per the brief

M-1 (KO P3 gloss separator, disclosed in KIT, all terms present); M-2/M-3/M-4 (KIT inaccuracies only, record-only — note the DE KIT §1 byte claim of 47,074 B was already refuted in Round 1; the re-measured DE pdftotext figure is now 47,065 B, recorded in §4, and the KIT §1 text was NOT rewritten); M-7 (frozen Spanish furniture, evidenced frozen); M-8 (EN abstract newline / IT KIT bytes — other editions, out of scope); the frozen Spanish quotes; P8 Q132 key B (weak but defensible, adjudicated in Round 1); all other answer keys.

---

## 4. Re-gate results (FINAL artifacts, both editions)

Build logs: `es-fix/es-de-build.log`, `es-fix/es-ko-build.log`. Both builds: **0 FLOW OVERFLOW / 0 HEAD TOO WIDE** (grep-verified in the logs; no residue/unreplaced-string warnings from the transform step).

| Gate | es-de | es-ko |
|---|---|---|
| Build registry | 150 total; A2 50 / B1 72 / B2 28; per page 10/18/18/18/18/18/12/38 | 150 total; A2 50 / B1 72 / B2 28; per page 10/18/18/18/18/18/12/38 |
| Counts re-measured from SVGs (`es-fix/counts_recount.py`) | 150; stem sequences P1 1–10, P2 11–28, P3 29–46, P4 47–64, P5 65–82, P6 83–100, P7 101–112, P8 113–150 — all seq-ok (138 standalone `N.` + 3 grouped sets of 4) | Same sequences, all seq-ok, 150 |
| Freeze (`tools/freeze.py diff` vs core) | CONFIRMED pattern: added CJK 0 on every page; edition CJK 0 (`es-fix/es-de-diff.json`, `cjk_added_total={}`) | CONFIRMED pattern: added CJK all Hangul (3,506 chars, 318 distinct syllables), Hanzi 0 (`es-fix/es-ko-diff.json`) |
| P6 re-wrap | Reflow only: non-CJK word-multiset lost = only replaced footer words (LUCERNA/SPANISH/WEEKLY); the 16 Spanish exercise fragments are re-joined in added strings, none lost | Reflow only: P6 removed set contains no Spanish exercise fragments at all (furniture/Chinese only, KO kept core P6 sizes); lost = only replaced footer words |
| P8 (`tools/p8.py compare`) | CLEAN, 150/150, missing=[], extra_count=0, keydiff=[137, 138] adjudicated (translation keys re-aimed to German; bodies 139/140 likewise) | CLEAN, 150/150, missing=[], extra_count=0, keydiff=[137, 138] adjudicated (same) |
| Occlusion (`tools/occlusion_audit.py`, canonical) | 0 flags; selftest OK (all 6 planted classes fired exactly once, clean controls silent) | 0 flags; selftest OK |
| Same-baseline scan (proofreader script) | 0 reports | 0 reports |
| Orphan scan (README #16) | n/a (Latin script) | 9 candidates, 0 true splits (see §2); builder S1/S2 scan 0 reports, groupings agree |
| P7 quotes | 8/8 Spanish quotes verbatim, each in exactly one article page + P7; 8/8 German translations present (Q6 fixed, others byte-identical in the freeze diff); defective string absent | n/a (no quote defect; KO P7 SVG byte-identical to pre-fix) |
| SVG change isolation (sha256 vs pre-fix) | Only `p7-lengua.svg` changed; P1–P6, P8 byte-identical | Only `p1-portada.svg`, `p2-vida.svg`, `p4-deporte.svg`, `p5-juventud.svg` changed; P3, P6, P7, P8 byte-identical |
| Cards | 8 × PNG, 1950×2700 | 8 × PNG, 1950×2700 |
| Print PDF | 8 pages, 4,641,037 B | 8 pages, 9,349,457 B |
| Web PDF (`tools/webpdf.py`) | 8 pages, 527,663 B (<7 MB) | 8 pages, 854,202 B (<7 MB) |
| Text layer (`pdftotext`) | 47,065 B (>0), byte-identical web vs print (`cmp` passed) | 48,448 B (>0), byte-identical web vs print (`cmp` passed) |
| Visual (full frame) | DE P7 — fixed Q6 line clean, page otherwise unchanged | KO P1 (cifras), P2 (calendar), P4 (bridge), P5 (bridge) — all four fixed lines clean, no overflow/overlap |

KIT records: fix record appended as §8 to `files/weekly-report-w46-es-de/WEEKLY-KIT.md` and to `files/weekly-report-w46-es-ko/WEEKLY-KIT.md` (append-only; earlier sections untouched). Pre-fix gate evidence preserved in `es-fix/prefix/`.

---

## 5. Final file inventory (both editions)

### 2026-w46-es-de — `files/weekly-report-w46-es-de/`

| File | Bytes |
|---|---|
| `2026-w46-es-de.text.md` | 47,072 (regenerated from SVG text layer; +9 vs pre-fix 47,063 = the Q6 line only) |
| `ABSTRACT.txt` | 279 (untouched) |
| `La-Lucerna-VOL3-DE-web.pdf` | 527,663 (pdftotext 47,065 B) |
| `La-Lucerna-VOL3-DE.pdf` (print) | 4,641,037 (pdftotext 47,065 B, byte-identical to web) |
| `WEEKLY-KIT.md` | 8,436 (fix record appended as §8) |
| `svg/p1-portada.svg` | 28,579 (unchanged) |
| `svg/p2-vida.svg` | 32,421 (unchanged) |
| `svg/p3-cultura.svg` | 654,632 (unchanged) |
| `svg/p4-deporte.svg` | 27,384 (unchanged) |
| `svg/p5-juventud.svg` | 28,351 (unchanged) |
| `svg/p6-afondo.svg` | 32,409 (unchanged) |
| `svg/p7-lengua.svg` | 27,500 (CHANGED — D-1 fix) |
| `svg/p8-ejercicios.svg` | 61,653 (unchanged) |
| `cards/*.png` (8) | 724,922 / 812,228 / 1,118,038 / 661,020 / 676,148 / 764,307 / 644,409 / 1,059,873 (all 1950×2700) |

### 2026-w46-es-ko — `files/weekly-report-w46-es-ko/`

| File | Bytes |
|---|---|
| `2026-w46-es-ko.text.md` | 48,561 (regenerated from SVG text layer; +31 vs pre-fix 48,530 = the 4 fixed passages only) |
| `ABSTRACT.txt` | 309 (untouched) |
| `La-Lucerna-VOL3-KO-web.pdf` | 854,202 (pdftotext 48,448 B) |
| `La-Lucerna-VOL3-KO.pdf` (print) | 9,349,457 (pdftotext 48,448 B, byte-identical to web) |
| `WEEKLY-KIT.md` | 12,458 (fix record appended as §8) |
| `svg/p1-portada.svg` | 28,559 (CHANGED — D-2 fix) |
| `svg/p2-vida.svg` | 31,698 (CHANGED — D-3 fix) |
| `svg/p3-cultura.svg` | 654,326 (unchanged) |
| `svg/p4-deporte.svg` | 26,981 (CHANGED — D-4 fix) |
| `svg/p5-juventud.svg` | 27,648 (CHANGED — D-5 fix) |
| `svg/p6-afondo.svg` | 32,382 (unchanged) |
| `svg/p7-lengua.svg` | 26,686 (unchanged) |
| `svg/p8-ejercicios.svg` | 60,393 (unchanged) |
| `cards/*.png` (8) | 750,449 / 837,604 / 1,109,251 / 672,076 / 688,395 / 749,635 / 658,567 / 1,168,674 (all 1950×2700) |

### Evidence under `hidden_files/w46/es-fix/`

- `FIX-REPORT.md` (this file)
- `es-de-build.log`, `es-ko-build.log` (fix-round build + render logs)
- `es-de-diff.json`, `es-ko-diff.json` (freeze diffs), `es-de-p8-compare.json`, `es-ko-p8-compare.json`, `es-de-occlusion.json`, `es-ko-occlusion.json`
- `ko-orphan-independent-round2.txt` (full README #16 scan output, 9 candidates), `ko_orphan_independent.py` (scan implementation, copy of the proofreader's), `ko-orphan-independent-round1.txt` (Round 1 baseline, 12 candidates), `es_ko_orphan-round2.txt` (builder S1/S2 scan, 0 reports)
- `counts-recount.txt`, `counts_recount.py` (independent stem recount)
- `prefix/` (pre-fix build logs + gate JSONs, preserved before the rebuilds overwrote them)
- `sim_wrap.py`, `sim_candidates.py`, `sim_candidates2.py`, `sim_candidates3.py`, `svglib_sim.py` (offline wrap-simulation working files)

### Source edits (the only content-source changes)

- `hidden_files/w46/t_de2.py` line 107 (D-1)
- `hidden_files/w46/t_ko.py` cifras pair, calendar pair, P4 bridge pair (D-2, D-3, D-4)
- `hidden_files/w46/t_ko2.py` P5 bridge pair (D-5)

No other source, edition, core, or shared-tool file was modified. (The shared tools `freeze.py`/`p8.py`/`occlusion_audit.py`/`webpdf.py` were used as-is; the orphan-scan and recount scripts in `es-fix/` are new working files, not tool modifications.)
