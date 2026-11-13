# GATE LOG — W47 ko-en proof2 (fan-out #3 rebuild; independent re-runs, 2026-11-11)

Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ko-en/` (read-only; all runs that write used scratch copies)
Core dir: `~/workspace/weekly-git/production/2026-w47/core-ko/` (read-only)
Scratch: `hidden_files/w47/scratch-proof-ko-en2/` — `work/` (logs/JSONs/scripts), `pages-print/` (110 dpi renders)
Interpreters: system `/usr/bin/python3` (Pillow 10.2.0 / FreeType 2.13.2) for run.py / freeze / checks / keycheck / textmd / scans; `tools/venv/bin/python` (Pillow 13.0.0) for render-adjacent tools (occlusion, p8, p8font) per the family rule. TMPDIR pointed at `work/tmp`.

| Gate | Command / method | Result |
|---|---|---|
| Hashes (brief) | `sha256sum` print + web + text.md | print `1e2247c6…b22c0` 45,262,667 B ✓; web `8fe16cdd…e182` 4,011,476 B ✓; text.md `9339a993…f846` 34,922 B ✓ — all match brief and ko3 record |
| Hashes (core) | `sha256sum` core-ko three files | print `53bf14ed…a2f27` 46,232,227 B ✓; web `9592945a…c7` 4,232,878 B ✓; text.md `da1d3a32…181a` 34,606 B ✓ — match #3 baseline; core untouched |
| SVG hashes | `sha256sum svg/*.svg` vs `ko3/en/sha-en-run1.txt` | all 8 match builder record ✓ |
| run.py | scratch copy (`*.py` + `assets/`), `/usr/bin/python3 run.py` | rc=0, 0 FLOW OVERFLOW / 0 HEAD TOO WIDE, TOTAL 150; A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; rebuilt 8 SVGs byte-identical to shipped — `work/run-proof2.log`, `work/svg-rebuild-compare.log` (first attempt failed only because `assets/` was missing from the copy; re-run with assets is the rc=0 above) |
| Freeze baseline | `/usr/bin/python3 freeze.py baseline --build core-ko --core-svg core-ko/svg --out work/freeze-baseline` | **8/8 byte-identical** (repointed: content12/34/56/7/8, check_gloss, render, check_core; core integrity OK) — `work/freeze-baseline-proof2.log` (build-copy deleted after verification) |
| Freeze baseline (venv control) | `tools/venv/bin/python freeze.py baseline …` | **ABORT rc=2** as prescribed (ko family requires Pillow 10; venv has 13) — expected control, guard not bypassed/modified — `work/freeze-baseline-venv.log` |
| Freeze diff | `/usr/bin/python3 freeze.py diff --core-svg core-ko/svg --edition-svg ed/svg --json work/freeze-diff-proof2.json` | added CJK **7, all U+3000** (P2–P8 +1 each, footer 3-vs-2; P1 net 0) — `work/freeze-diff-proof2.log/.json`; per-page U+3000 totals independently recomputed and matched |
| Occlusion audit | `tools/venv/bin/python occlusion_audit.py <ed> --core <core> --json work/occlusion-proof2.json` | selftest OK (6 classes fired, clean controls silent); **0 flags**; core 0; NEW 0 — `work/occlusion-proof2.log/.json` |
| p8 extract | `tools/venv/bin/python p8.py extract --p8 ed/svg/p8-siheom.svg --total 150 --json work/p8-proof2.json` | **150/150 noted** — `work/p8-extract-proof2.log`, `work/p8-proof2.json` |
| p8 compare | `tools/venv/bin/python p8.py compare --core-p8 core/svg/p8-siheom.svg --edition-p8 ed/svg/p8-siheom.svg --total 150 --json work/p8compare-proof2.json` | **CLEAN**, missing=[] extra=0, keydiff=[137, 138] (expected) — `work/p8-compare-proof2.log`, `work/p8compare-proof2.json` |
| Text layers | `pdftotext` print vs web (plain and `-layout`) + per-page byte counts | **byte-identical both ways**: 50,786 B plain; 102,397 B `-layout`; all 8 pages non-empty in both — `work/print.txt`, `work/web.txt`, `work/print-nolayout.txt`, `work/web-nolayout.txt` |
| Print vs web pixels | 72 dpi pdftoppm both PDFs, mean abs diff | P1 0.322, P2 0.084, P3 0.145, P4 0.164, P5 0.100, P6 0.000, P7 0.588, P8 0.091 — layout identical |
| P8 min font | `tools/venv/bin/python ko3/p8font.py <pdf>` (print + web) | **9.975pt** both (167 spans, 162 at-min), PASS ≥9.75pt — `work/p8font-proof2.log` |
| Boxtitle | `/usr/bin/python3 ko3/boxtitle-ko.py <ed>` | **8/8 ≤386.5px** (336.5 / 373.1 / 330.1 / 329.0 / 358.4 / 236.6 / 359.9 / 312.1) — `work/boxtitle-proof2.log` |
| check_core + check_gloss | adapted `work/check-edition-proof2.py en "Note — "` (copies of core checks, ED/BUILD repointed at the edition) | rc=0; gloss fails 0; phrases 8/8 verbatim; orphan scan 0; dates OK — `work/check-proof2.log` |
| Curly sweep | Python count U+201C/U+201D/U+2019 in 8 SVGs + text.md + ABSTRACT.txt | **0/0/0** — `work/scans-proof2c.log` |
| Hanzi residual | CJK Unified U+4E00–U+9FFF inside `<text>` | **0** |
| Orphan punctuation | `<text>` that IS a lone 。/」/』/：/–/— or STARTS with one | **0 hits** |
| Creambox audit | 49 × `#f0eee5` rects, true-ink bottom (audit formula, real Noto CJK fonts) vs box bottom | **49/49 PASS**; tightest P2/P3/P5 "And you?" boxes +5.1 px (core's own: +2.5 px); P7 frame +9.9 px; rest ≥10.9 px — `work/scans-proof2c.log` (v1 used wrong font dir and v2 a wrong ink formula; v3 uses the audit's `baseline − ascent + getbbox` and is the reported run) |
| keycheck | adapted `work/keycheck-proof2.py en` on my own p8 extract + REG from scratch copy | **150/150** (149 exact + #150 `✓`); per-page 10/18/18/18/18/18/12/38 — `work/keycheck-proof2.log`, `work/reg-proof2.json` |
| §1.1 counts | VOL.4 / VOL.5 / `·` / Lucerna per page, edition vs core | VOL.4 and `·` identical (13/21/20/14/20/31/17/38); VOL.5 P7 3→2 by design |
| #2 vs #3 SVGs | `sha256sum` vs `fanout-ko/en/sha-en-run2.txt` | P2/P3/P5/P6/P8 byte-identical; P1/P4/P7 changed only (see PROOF-NOTE) |
| #2 vs #3 text | own SVG-text extraction (1,496 lines) vs proof1 `work/svg-text.txt` | real changes only: P1 Q10 + P4 Q47/Q48 stem fixes, P7 frame + phrase #7; rest is extractor whitespace — `work/svg-text-proof2.txt`, `work/svg-text-diff-vs-proof1.txt` |
| #2 vs #3 pixels | 110 dpi renders vs proof1 `pages-print/` | mean ~4–5 on ALL pages incl. byte-identical P8; ±1 px shift and 2 px blur do not explain it — renderer-session confound, NOT used as evidence |
| Visual | 8 print pages @110 dpi + 300 dpi P7 frame crop | 8/8 clean; D1 straight quotes confirmed visually — `pages-print/p-1.png` … `p-8.png`, `work/p7-frame-zoom-proof2.png`, `work/p7-phrases7-zoom-proof2.png` |
| text.md | full read (917 lines) + re-export from scratch copy | 449 items; re-export **byte-identical** (34,922 B) — `work/textmd-reexport2.md`, `work/textmd-proof2b.log` |
| ABSTRACT.txt | read + sha256 | 305 B, SHA `11871943…abc812`, 1 line, 0 ASCII `"`, all required elements ✓ |
| H model text | recount from P8 SVG lines | **169 chars excl. spaces (221 incl.)**, same convention as core |
| Fonts (D5, record only) | `pdffonts` print + web | print: NotoSansCJKkr / NotoSerifCJKkr (Reg+Bold, subset) + UnifrakturMaguntia; web: same families, `Lucerna`-prefixed subsets; no Newsreader in either |

## Incidents
- One `muse.exec` call was aborted by a runtime restart mid-task; the 72 dpi web render it interrupted came out truncated (w-5.png) and was re-rendered cleanly (rc=0, all 8 pages). No other work was affected; `/dev/null` present throughout.
- `run.py` on the first scratch copy failed with `FileNotFoundError: assets/lucerna-moth.svg` because only `*.py` had been copied; the copy was completed with `assets/` and re-ran rc=0. No production file was involved.
- A shell `grep -c $'…'` curly count on text.md returned a bogus 267 (quoting artifact); re-checked with Python — 0, matching the scan script.
- Cleanup after verification: deleted regenerable bulk only (freeze build-copies, 72 dpi renders, full 300 dpi page, build-copy SVGs, textmd copy); all logs, JSONs, hashes, renders and crops retained. Final note-dir size 16 MB. No production file modified; no commit; no push.
