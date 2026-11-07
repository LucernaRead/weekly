# Fix Report — W46 ES family, Round 3 defect D-6 (DE only)
## Edition fixed: 2026-w46-es-de ONLY

- **Issue:** VOL.3, week Mon 2026-11-09 – Sun 2026-11-15. Target language Spanish; reader-native German (de).
- **Authority:** Round 2 independent proofread verdict `hidden_files/w46/es-proofread-gates-round2/proofreader-verdict-round2.md` (FAIL for DE on one blocking defect D-6; KO PASSED Round 2 and the other 9 ES editions PASSED Round 1 — none of them was touched: no file in any other edition dir was read for writing, edited, or re-rendered; `~/workspace/weekly-git` was never touched; `index.json` was never edited; nothing was pushed, inserted, or posted; no subagents were spawned).
- **Method:** fix AT THE SOURCE in the edition transform table; full re-render of the DE edition through the single driver (`hidden_files/w46/build_one.py`, which copies the fixed core build, applies the transforms, runs `run.py` in one process, renders via `tools/venv`, and runs freeze/p8/occlusion). No rendered SVG or PDF was hand-edited. `.text.md` was regenerated with `hidden_files/w46/es_textmd.py` from the edition's own SVG text layer (never from PDF; the exporter reproduces the pre-fix file byte-identically when run on the pre-fix SVGs, and the post-fix diff touches only the fixed line — header preserved verbatim).
- **Seed record (unchanged):** VOL.3, 150 exercises (A2 50 / B1 72 / B2 28), per page 10/18/18/18/18/18/12/38.
- **Status:** defect fixed and re-gated as below. A Round 3 independent proofread (FULL round per SOP §8.4) follows; this report and its re-gating do NOT replace it.

---

## 1. Fix, with before/after quotes

### D-6 (BLOCKING, es-de only) — P2 ¿Y TÚ? box, ungrammatical transitive `sorgen`

- **Source file:** `hidden_files/w46/t_de.py`, line 68 (transform pair scoped to `content12.py`, the ¿Y TÚ? explanation string). This was a Round 1 MISS, not a fix regression: P2 was untouched by the Round 1 fix (which changed only `t_de2.py` line 107 / P7), and the Round 2 freeze-diff comparison shows P2 identical pre/post Round 1 fix.
- **Frozen Spanish prompt (unchanged):** `¿Y tú? ¿Qué harías el miércoles 11: vas a la huelga, trabajas o te quedas en casa? ¿Qué te preocupa más: el salario, la vivienda o los precios? Escribe dos frases en español y envíalas a la redacción: las mejores salen en la página 7, «Cartas de los lectores».`
- **Before (full German explanation sentence):** `Was machst du am Mittwoch, 11. November: streiken, arbeiten oder zu Hause bleiben? Was sorgt dich am meisten: Löhne, Wohnungen oder Preise? Schreib zwei Sätze auf Spanisch an die Redaktion.`
- **After (full German explanation sentence):** `Was machst du am Mittwoch, 11. November: streiken, arbeiten oder zu Hause bleiben? Was beunruhigt dich am meisten: Löhne, Wohnungen oder Preise? Schreib zwei Sätze auf Spanisch an die Redaktion.`
- **Question clause only:**
  - Before: `Was sorgt dich am meisten: Löhne, Wohnungen oder Preise?`
  - After: `Was beunruhigt dich am meisten: Löhne, Wohnungen oder Preise?`
- **Choice rationale:** German `sorgen` takes no accusative object; `beunruhigen` is the correct transitive worry verb and the direct equivalent of the siblings' correct worry-verbs (EN `What worries you most`, FR `qui t'inquiète le plus`, IT `Cosa ti preoccupa di più`, RU `Что беспокоит вас больше всего`). Wording was chosen by wrap simulation with a verbatim call to the build's own `svglib.wrap` at the true draw settings (sans, regular, 20pt, width 390px = CW−44): `beunruhigt` keeps the identical 6-line breaks of the defective render (only line 3 changes; its width 372.4px < 390px), while both `Sorgen`-noun alternatives (`Was bereitet dir am meisten Sorgen…`, `Worüber machst du dir am meisten Sorgen…`) rewrap three lines. The `sich sorgen um` construction used for the Round 1 D-1 fix is a statement form; for this question, `beunruhigt` preserves the `Was … dich am meisten` question frame. The three options (Löhne, Wohnungen, Preise) and the box's meaning are intact.
- **Rendered lines (P2, x=1473, sans 20pt, y=932.74 / 961.14 / 989.54 / 1017.94 / 1046.34 / 1074.74):** `Was machst du am Mittwoch, 11.` → `November: streiken, arbeiten oder zu` → `Hause bleiben? Was beunruhigt dich am` → `meisten: Löhne, Wohnungen oder Preise?` → `Schreib zwei Sätze auf Spanisch an die` → `Redaktion.` — the corrected question renders completely and grammatically, verified visually on the DE P2 card at full frame (see §3).
- **Verification:** the defective string `Was sorgt dich` occurs 0 times in the joined edition text and 0 times in every DE SVG (grep per file); the corrected question occurs exactly once in the joined text. The defective D-1 string `Die Wohnung sorgt` is likewise 0 occurrences (unchanged since Round 1).

**Fixes NOT applied as specified:** none. D-6 was fixed exactly as the verdict specified. Nothing else was changed: the 5 confirmed Round 1 fixes, all 150 keys, the frozen Spanish quotes/labels, the "`12 de noviembre`" distractor in P8 item 122 (frozen-core inheritance per the Round 2 correction, not a defect — left untouched), the M-1/M-5/M-7 adjudications, and the KIT record-only inaccuracies M-2/M-3/M-4 (no KIT churn beyond appending this fix record as §9).

---

## 2. Re-gate results (FINAL artifacts, DE edition only)

Build log: `es-fix-round3/es-de-build.log` (driver log; combined stdout in `build-stdout.log`). The build: **0 FLOW OVERFLOW / 0 HEAD TOO WIDE** (grep-verified in the log; no residue/unreplaced-string warnings from the transform step). Registry in the build log: per-page cumulative 10/28/46/64/82/100/112/150; `by level {'A2': 50, 'B1': 72, 'B2': 28}`; P2 col3 ends at y=1081.5, identical to the pre-fix render.

| Gate | Result | Evidence file |
|---|---|---|
| Freeze (`tools/freeze.py diff` vs core, independently re-run) | exit 0; added CJK 0 on every page; edition CJK total 0 (`cjk_added_total={}`) | `es-de-diff-r3.json`, `freeze-r3.txt` (driver copy: `es-de-diff.json`) |
| P8 (`tools/p8.py compare`, independently re-run) | CLEAN, 150 noted = 150, missing=[], extra_count=0, keydiff=[137, 138] adjudicated (translation keys re-aimed to German; unchanged since Round 1/2) | `es-de-p8-compare-r3.json`, `p8-r3.txt` (driver copy: `es-de-p8-compare.json`) |
| Occlusion (canonical `tools/occlusion_audit.py`, independently re-run) | 0 flags; selftest OK (all 6 planted classes fired exactly once, clean controls silent) | `es-de-occlusion-r3.json`, `occlusion-r3.txt`, `occlusion-selftest-r3.txt` (driver copy: `es-de-occlusion.json`) |
| Same-baseline scan (Round 2 script, DE-only adaptation) | 0 reports (1,589 `<text>` parsed — same count as Round 2) | `same-baseline-r3.txt`, `same_baseline_r3.py` |
| Counts re-measured from SVGs (`counts_recount_r3.py`, DE-only adaptation of the Round 1 recount) | 150; per-page 10/18/18/18/18/18/12/38; all stem sequences seq-ok (138 standalone + 3 grouped sets of 4) | `counts-recount-r3.txt`, `counts_recount_r3.py` |
| P7 quotes (`quotes_r3.py`, DE-only adaptation) | 8/8 Spanish quotes verbatim, each in exactly one article page + P7; 8 translation lines with `(Página N)` tags; Q6 fixed translation re-verified verbatim (`86,9 % der Spanier sorgen sich um die Wohnung. (Página 6)`) | `quotes-r3.txt`, `quotes_r3.py` |
| SVG change isolation (sha256 vs pre-fix, all 12 ES dirs incl. core) | Only `svg/p2-vida.svg` + `cards/p2-vida.png` changed pre-KIT-appendix; P1, P3–P8 SVGs/cards byte-identical; KO + other 9 editions + core byte-identical | `prefix/all-es-files-prefix-hashes.txt`, `all-es-files-postfix-hashes.txt` |
| Cards | 8 × PNG, all 1950×2700 | (sizes in §3) |
| Print PDF | 8 pages, 4,641,045 B | `La-Lucerna-VOL3-DE.pdf` |
| Web PDF (`tools/webpdf.py`, via render.py) | 8 pages, 527,672 B (<7 MB) | `La-Lucerna-VOL3-DE-web.pdf` |
| Text layer (`pdftotext`) | 47,070 B (>0), byte-identical web vs print (`cmp` passed); +5 B vs Round 2's 47,065 B = exactly the `beunruhigt`/`sorgt` length delta (+5 chars) | `de-web.txt`, `de-print.txt` |
| ABSTRACT.txt | 279 B, unchanged; single line + trailing newline, no ASCII `"`, practice-framed, real topics + masthead + VOL.3 + A2–B2 + 150 | (edition dir, untouched) |
| Visual (full frame) | DE P2 — corrected question complete inside the ¿Y TÚ? box, no overflow/overlap; P1/P8 spot checks — clean, unchanged | §3 |

P6 chart bars were not re-measured: `svg/p6-afondo.svg` is byte-identical to the Round 2-verified render (hash isolation above), so the Round 2 bar-width verification (values ×3.2 exact) still stands.

---

## 3. Final file inventory — 2026-w46-es-de

`files/weekly-report-w46-es-de/`

| File | Bytes |
|---|---|
| `2026-w46-es-de.text.md` | 47,077 (regenerated from SVG text layer; +5 vs pre-fix 47,072 = the `beunruhigt`/`sorgt` delta on the one fixed line only) |
| `ABSTRACT.txt` | 279 (untouched) |
| `La-Lucerna-VOL3-DE-web.pdf` | 527,672 (pdftotext 47,070 B) |
| `La-Lucerna-VOL3-DE.pdf` (print) | 4,641,045 (pdftotext 47,070 B, byte-identical to web) |
| `WEEKLY-KIT.md` | 12,401 (fix record appended as §9; §§1–8 untouched) |
| `svg/p1-portada.svg` | 28,579 (unchanged) |
| `svg/p2-vida.svg` | 32,426 (CHANGED — D-6 fix; +5 B) |
| `svg/p3-cultura.svg` | 654,632 (unchanged) |
| `svg/p4-deporte.svg` | 27,384 (unchanged) |
| `svg/p5-juventud.svg` | 28,351 (unchanged) |
| `svg/p6-afondo.svg` | 32,409 (unchanged) |
| `svg/p7-lengua.svg` | 27,500 (unchanged — Round 1 D-1 fix intact) |
| `svg/p8-ejercicios.svg` | 61,653 (unchanged) |
| `cards/*.png` (8) | 724,922 / 812,010 (CHANGED — P2) / 1,118,038 / 661,020 / 676,148 / 764,307 / 644,409 / 1,059,873 (all 1950×2700) |

### Evidence under `hidden_files/w46/es-fix-round3/`

- `FIX-REPORT.md` (this file)
- `es-de-build.log` (fix-round build + render + driver-gate log), `build-stdout.log` (combined driver stdout)
- `es-de-diff.json`, `es-de-p8-compare.json`, `es-de-occlusion.json` (driver gate outputs) and independently re-run `es-de-diff-r3.json`, `es-de-p8-compare-r3.json`, `es-de-occlusion-r3.json` (+ `freeze-r3.txt`, `p8-r3.txt`, `occlusion-r3.txt`, `occlusion-selftest-r3.txt`)
- `same-baseline-r3.txt`, `same_baseline_r3.py`, `counts-recount-r3.txt`, `counts_recount_r3.py`, `quotes-r3.txt`, `quotes_r3.py`
- `de-web.txt`, `de-print.txt` (pdftotext outputs, byte-identical)
- `prefix/` (pre-fix build log + gate JSONs + pre-fix `.text.md` + pre-fix DE hashes + all-editions pre-fix hash list, preserved before the rebuild)
- `all-es-files-postfix-hashes.txt` (post-fix hash list for all 12 ES dirs)

### Source edit (the only content-source change)

- `hidden_files/w46/t_de.py` line 68 (D-6). No other source, edition, core, or shared-tool file was modified. (The shared tools `freeze.py`/`p8.py`/`occlusion_audit.py`/`webpdf.py` were used as-is; the gate scripts in `es-fix-round3/` are DE-only adaptations of prior proofreader/fix scripts, not tool modifications. The `weekly-report-w46-es-de-build/` working copy is regenerated by `build_one.py` from the core build + transforms on every run.)

### Untouched-editions confirmation

Full sha256 comparison of all 252 files across the 12 `files/weekly-report-w46-es-*` dirs (core + 11 editions), pre-fix vs post-fix (before the KIT appendix): exactly 5 files changed, all in `weekly-report-w46-es-de/` (`2026-w46-es-de.text.md`, both PDFs, `cards/p2-vida.png`, `svg/p2-vida.svg`). After appending the §9 KIT record, the 6th changed file is the DE `WEEKLY-KIT.md` itself. The KO edition (`2026-w46-es-ko`, Round 2 PASS) and the other 9 editions are byte-identical to their pre-fix state; the frozen core dir is byte-identical.
