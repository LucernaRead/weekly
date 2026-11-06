# WEEKLY-KIT · 2026-w46-es-zh-cn — La Lucerna, Spanish Weekly VOL.3, explanations in Simplified Chinese

Slug: `2026-w46-es-zh-cn`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: Simplified Chinese — the core's own explanation language, unchanged.
Build dir: `hidden_files/weekly-report-w46-es-zh-cn-build/` (copy of the fixed W46 core build; minimal transform `hidden_files/w46/t_zhcn.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Why a distinct edition

W45 Spanish shipped no separate zh-cn build: the W45 es-zh-cn repo edition is the core itself (identical abstracts, no separate local build/files dir). The W46 task requires 11 distinct fan-out edition dirs, so zh-cn is built as its own edition: core text verbatim + its own pairing badge, pairing footer and P8 separator + its own KIT/ABSTRACT/`.text.md`. This follows the ZH-TW pattern for the three pairing elements only; no explanation string was changed.

## 2. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-ZH-CN.pdf` 17,612,019 B (SC font embedding); web PDF `La-Lucerna-VOL3-ZH-CN-web.pdf` 1,083,484 B (<7 MB), text layer 44,933 B via `pdftotext`, byte-identical to the print PDF's text.
`.text.md` exported from this edition's own SVG text layer (never from PDF).

## 3. The only three deltas vs the core (verified by `freeze.py diff`)

1. Pairing badge replacing the y=372 subtitle slot, 19.5pt sans bold BRICK: `西班牙语正文 · 简体中文讲解 — 给简体中文读者的版本` (ZH-TW pattern, Simplified form).
2. Pairing footer on every page (bslib4 foot()): `La Lucerna · 西班牙语周报 VOL.3 · 正文西班牙语 · 讲解简体中文` (replaces the core's `… · LUCERNA SPANISH WEEKLY`).
3. P8 separator: `— 第 {pg} 版 —` (replaces the core's `— PÁGINA {pg} —`; ZH-TW pattern, Simplified form).
Everything else — name line, top strip, bands, gloss prefix `讲解｜`, P8 header, type names, disclosure — is the core's own Simplified text, unchanged. PDF filenames suffixed per the fan-out convention (`La-Lucerna-VOL3-ZH-CN.pdf`).

## 4. Gates (final render)

- Builder self-check: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises; `p8.py extract` 150/150.
- `freeze.py diff` vs core SVGs: added strings are exactly the badge (1), the footer (8 pages) and the 8 separators; removed strings are exactly the subtitle line, the core footer (8 pages) and the 8 Spanish separators. Added CJK = 0 (all characters already present in the core).
- `p8.py compare` vs core P8: CLEAN, 150/150, keydiff=[] — byte-identical answer keys.
- `tools/occlusion_audit.py`: 0 flags (`hidden_files/w46/es-zh-cn-occlusion.json`, selftest passed).
- Same-baseline furniture scan + chart GRAZE element-check (`hidden_files/w46/checks.py`): 7 rowcheck reports, all P1 contents-list 4.0px gaps — the core pattern, no overlap; chart 0 overlaps.
- Web PDF text layer: 44,933 B, identical to print text; <7 MB.
- Visual: P1 inspected — badge in place, footer pairing correct, name line and top strip unchanged from the core.

## 5. Fixups

Core letters-box fix inherited via the build from the fixed core build. First build wrote unsuffixed PDF filenames (the core's names); filename pairs were added to `t_zhcn.py` and the edition rebuilt — the stale unsuffixed files were removed, only the suffixed pair remains.

## 6. Promises, sources, credits

As in the core: 13 Nov campaign start and 29 Nov vote lead the issue; the unverified 12 Nov decree date was NOT reintroduced; reader letters: labelled editor's example (Ana) + bilingual disclosure, promise carried to VOL.4, no reader fabricated. Sources, image credits and the full article record: see the core KIT `files/weekly-report-w46-es-core/WEEKLY-KIT.md`.

## 7. Reproduction

`python3 hidden_files/w46/build_one.py zh-cn t_zhcn` (copies the fixed core build, applies `t_zhcn.py`, runs `run.py`, renders via `tools/venv`, gates freeze/p8/occlusion). Gate outputs: `hidden_files/w46/es-zh-cn-diff.json`, `es-zh-cn-p8-compare.json`, `es-zh-cn-occlusion.json`, `es-zh-cn-build.log`; gate record in `hidden_files/w46/es-gates.log`. Independent proofread (§8.4 SOP) still outstanding — do not claim finalisation.
