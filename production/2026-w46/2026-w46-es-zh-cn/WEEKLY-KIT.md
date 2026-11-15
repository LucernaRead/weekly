# WEEKLY-KIT · 2026-w46-es-zh-cn — La Lucerna, Spanish Weekly VOL.3, explanations in Simplified Chinese

Slug: `2026-w46-es-zh-cn`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: Simplified Chinese — the core's own explanation language, unchanged.
Build dir: `hidden_files/weekly-report-w46-es-zh-cn-build/` (copy of the fixed W46 core build; minimal transform `hidden_files/w46/t_zhcn.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Why a distinct edition

W45 Spanish shipped no separate zh-cn build: the W45 es-zh-cn repo edition is the core itself (identical abstracts, no separate local build/files dir). The W46 task requires 11 distinct fan-out edition dirs, so zh-cn is built as its own edition: core text verbatim + its own pairing badge, pairing footer and P8 separator + its own KIT/ABSTRACT/`.text.md`. This follows the ZH-TW pattern for the three pairing elements only; no explanation string was changed.

## 2. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-es-zh-cn.pdf` 4,874,811 B; web PDF `2026-w46-es-zh-cn.web.pdf` 756,631 B (<7 MB), text layer 44,633 B via `pdftotext`, byte-identical to the print PDF's text.
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

## D5 rebuild (2026-11-15)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target es --reader zh-cn --week 2026-w46` (`--check` dry-run clean first). Mode cjk; `_D5_READER = "zh-cn"`. Routing test `test_d5_routing.py` FAILURES: 0. fix2 retained (`_QUOTE_CLS` x4).
- Pre-fix census (baseline build): D5 Latin-in-CJK 339, D5 Cyrillic-in-CJK 0, curly-in-CJK 3, curly total 6 (all Newsreader). Run2 census: Latin 0 / Cyrillic 0 / curly-in-CJK 0; curly total 6 all Newsreader; Noto Sans 0.
- run1 gates 18/19; run1 -> run2 fixes (font-size reduction only, no copy changes):
- `content12.py:49` — P1 numbers f.box tsize added 21.5 (was default 23) (margin 5.3px)
- `content56.py:28` — P5 plan f.box tsize added 22 (was default 23) (margin 4.5px)
- run2 gates 19/19 ALL-GREEN. G8 CLEAN (core-es P8 compare; keydiff [137, 138]; zh-cn keydiff [] — core-es is the zh-cn template). G10 CJK added 1 (P6 U+3000 run-split, as W45 es); Latin added 221 (run-split). G12 28 titles, 354 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal. G14 0 defects; P8 200 rows, slack 58.4px. G15a text-layer diff 0; text.md DIFF 86 lines, native verifier ADOPT (REWRAP 23, 0 UNEXPECTED). G15b CARRYOVER FAIL svg=5905 md=7977 (record-only, D27).
- D18 gap 103.0px; D37 N/A (no badge line in the box zone; strapline y=372 above box top 588); D39(4) P7 band bottom vs footer 2596: +4.6px (pre-existing, baseline identical).
- Old (baseline build) print `La-Lucerna-VOL3-es-zh-cn.pdf` 16,098,719 B SHA256 `85b59aa553fcff1053c41e4fbd271c1c48301b3b92e6a077e0ac67baf423f9ef`; web 976,795 B SHA256 `a635f4250e466c7c1c955ea5e32c642a7f4230e1b1e92ddd3aca8ada6cca9792`.
- New (run2) print `La-Lucerna-VOL3-es-zh-cn.pdf` 4,874,811 B SHA256 `75783010e42b644b7a191b92a539bcc3d225372f4e2316cfc47170c9bd4015b5`; web `2026-w46-es-zh-cn.web.pdf` 756,631 B SHA256 `d33dae9eabbeeb01e78e7336b3ad918962126f36e22a4b012538260a5515cc60`; text.md 44,710 B SHA256 `bb704230b486d73d976168f9d11588b9e60d424fe2770a81d11a2acbabc6d35a` (textexp output, `logs/2026-w46-es-zh-cn/2026-w46-es-zh-cn.text.md.run2`; the `<slug>.text.md` in the edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it).
- Logs: `logs/2026-w46-es-zh-cn/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-zh-cn/g*-run2.log`, `logs/2026-w46-es-zh-cn/census-run2.json`, `logs/2026-w46-es-zh-cn/freeze-diff-run2.json`. D5 report: `notes/g-es/scratch-d5-rebuild-es/2026-w46-es-zh-cn-D5-REPORT.md`.
