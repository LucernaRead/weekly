# GATE-LOG.md — 2026-W47 it-en (re-proof, second round after fix1), mechanical gates self-run

Proofer: independent re-proof, 2026-11-11. All commands run by the proofer; nothing
copied from builder/fix1 logs. Working directory: my scratch dir
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it-en1/`
`PYTHONDONTWRITEBYTECODE=1` throughout. TMPDIR = my scratch `tmp/` (never /tmp).

## 0. Hard-gate probes (pre-work, 2026-11-11 ~20:52 UTC)

| probe | result |
|---|---|
| `git -C ~/workspace/weekly-git hash-object -w /dev/null` | OK (`e69de29bb2…`, RC=0) |
| real file write into scratch `scratch-reproof-it-en1/probe.txt` | OK |

## 1. Identity (three SHA — task values, verified by my own sha256sum)

- print `70061d6a2c613154928c27e6fe8e6962a9036ff72223a49bbdb238cf6f84047c`, 14,032,933 B — MATCHES task
- web `d037ccdf8a7f1ac94dc288625f33bf2348ffaf4582e37e9e4dfb5449771e06fc`, 1,291,161 B — MATCHES
- text.md `2168a652d7608744c2dbd06924909f990c95ab9b5cc48a9d1abe3ea1fad1959b`, 55,204 B / 1317 lines — MATCHES
- Re-verified at the end of the round (same three hashes). KIT §12 lines 97–99 carry
  the same three SHAs with old SHAs retained; §7 untouched.

## 2. Build interpreter

`tools/venv/bin/python` → Pillow 13.0.0 (same as the build). fitz/PyMuPDF available
in the same venv (used for the text-layer bbox method).

## 3. run.py re-run (scratch copy, OUT repointed — production NOT written) — RC=0, TOTAL 150, 0 overflow

- Setup: copied `content*.py`, `bslib4.py`, `svglib.py`, `run.py`, `assets/` to
  `rerun/edition/`; patched the hardcoded OUT (line 6 of all five content files)
  from the production svg dir to `rerun/edition/svg`; grepped the copies —
  zero `weekly-git/production` strings remained before running (the `render.py`
  BASE hardcode was never executed; my own `rerender.py` reads the shipped SVGs
  read-only instead). This avoids proof2's incident, where the unpatched re-run
  rewrote the production SVGs (mtimes 2026-11-11 20:19 UTC).
- Result: RC=0; 0 occurrences of FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE;
  TOTAL 150; levels A2 47 / B1 70 / B2 33; pages 10/18/18/18/18/18/12/38;
  model words 99. P1-headline ends 1362; P4 col3 ends 1140.45; P7 col3 ends 1673.0;
  P8-keys flow ends col 3 y=2514 (bottom 2552). Log: `rerun/run.log`.
- Production untouched: edition SVGs re-hashed after the run — 8/8 identical to
  `svg-sha-before.txt` (recorded before any build step).

## 4. SVG rebuild 8/8 + print PDF re-render byte-identical

- Re-run SVGs (written only into `rerun/edition/svg/`) vs the shipped SVGs:
  `cmp` 8/8 byte-identical (p1–p8).
- Print PDF re-render: my own `rerender.py` (same steps as edition `render.py`:
  cairosvg svg2pdf per page + pypdf merge, reading the shipped SVGs read-only,
  writing only to scratch) → `rerender-print.pdf` 14,032,933 bytes, sha256
  `70061d6a2c613154928c27e6fe8e6962a9036ff72223a49bbdb238cf6f84047c` —
  **BYTE-IDENTICAL to the delivered print PDF** (log: `rerender.log`).
- Web PDF was NOT re-rendered (task: web PDF bytes are not reproducible; only
  its text layer was compared — gate 8).

## 5. Freeze (canonical tool — TRUE core build, NOT self-comparison)

- Correctness note: proof2 ran `freeze.py baseline` with `--core-svg` pointed at
  the EDITION svg dir (build-copy of the edition vs its own shipped SVGs — a
  self-comparison). This round instead ran the canonical form: `--build` the
  CORE build dir, `--core-svg` the CORE svg subdir. Before running, the build
  source was verified to be the core: `core-it/content12.py` contains
  `数字看本周` 1× and `FIGURES` 0×.
- `tools/freeze.py baseline --build production/2026-w47/core-it --core-svg
  production/2026-w47/core-it/svg --out <scratch>/freeze-baseline` → RC=0,
  **8/8 SVGs byte-identical** (repointed files: render.py, content12/34/56/7/8.py);
  "core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)".
  Log: `freeze-baseline.log`. Core SVGs re-hashed again at the end of the round:
  8/8 match the freeze log hashes.
- `tools/freeze.py diff --core-svg core-it/svg --edition-svg it-en/svg
  --json en/freeze-diff.json` → RC=0; per-page added CJK = 13 × U+3000 only
  (furniture separators, exempt); non-space added CJK = {}. Log: `freeze-diff.log`.
- The EDITION's reproducibility is proven separately by gate 3/4 (run.py re-run
  8/8 + print PDF re-render byte-identical), not by a self-comparing freeze run.

## 6. Occlusion audit (canonical tool)

- `tools/occlusion_audit.py --selftest` → RC=0, all 6 classes fire, clean controls silent.
- `tools/occlusion_audit.py <edition svg>` → RC=0, **0 flags** on the 8 shipped SVGs.
- Caveat carried from proof2: BOXTITLE covers bordered boxes only; borderless
  cream boxes need the cream-box scan (gate 7), which found 0 overflow.

## 7. D-1/D-2/D-3 triple measurement (my own fresh script) + cream-box scan

- Script: `verify_triple.py` (written fresh this round), log `verify-triple.log`.
  Three methods per item (threshold spare ≥ +5 px):
  - D-1 P1 `LA SETTIMANA IN CIFRE　FIGURES`: PIL ink 556.5..944.0 vs box
    538.5..961.0 → **+17.0**; render pixels darkest ink right x=941 → **+20**;
    fitz text-layer words x 556.5..944.1 → **+16.9** (print and web identical).
  - D-2 P2 `LA FRASE PER RICORDARE　LEARN`: PIL ink 556.5..947.2 → **+13.8**;
    pixels x=945 → **+16**; text-layer x 556.5..948.6 → **+12.4** (print/web same).
  - D-3 P7 `ERRORI TIPICI　TYPICAL ERRORS`: PIL ink 1461.5..1835.2 vs box
    1439.5..1862.0 → **+26.8**; pixels x=1833 → **+29**; text-layer x 1461.5..1836.1
    → **+25.9** (print/web same).
  - All nine cells reproduce fix1's claimed values exactly, independently measured.
    Tightest value anywhere: D-2 method ③ at +12.4 px — comfortably above the floor;
    no 0-px borderline case.
  - Visual: 2× crops `pages/crop-p1-cifre.png`, `crop-p2-frase.png`,
    `crop-p7-errori.png` (cut from the 96 dpi render of the DELIVERED print PDF,
    viewed) — all three titles fully inside their cream boxes.
- Cream-box scan (`cream_spill_orphan.py`, my own run; 29 cream rects P1–P7, P8 has 0):
  **0 CREAM-X, 0 CREAM-Y, 0 SPILL-PAGE, 0 SPILL-FOOTER**. Text nodes scanned:
  P1 175, P2 179, P3 178, P4 173, P5 168, P6 191, P7 161, P8 380. Log: `cream-scan.log`.
- ORPHAN flags: **3**, all adjudicated NOT defects — each node verified by me as
  byte-identical (same text, same x/y, same font) in the core SVGs: P6 "18." at
  1603.5/641.6; P8 "due" at 538.5/818.975; P8 Q137 "___" blank at 773.3/1187.825.
  Frozen Italian text, inherited wraps (PROOF-NOTE O-10).
- Reconstruction proof (only-3-titles-changed): substituting the 3 new titles back
  to the 3 old ones in a scratch copy of `.text.md` reproduces proof2's old SHA
  `f12950aa…` exactly; p3–p6/p8 SVGs are byte-identical to fix1's pre-fix baseline
  copies, and p1/p2/p7 with the title substituted back are byte-identical too.

## 8. Text-layer consistency (print vs web PDF)

- `pdftotext -layout` on both PDFs → 109,235 bytes each; word multiset identical,
  7931 words each; char multiset equal; **exact text equal**. New titles present 1×
  each in both; old strings (`THIS WEEK IN NUMBERS`, `COMMON MISTAKES`) 0× in both.
  Files: `print.txt`, `web.txt`.
- Web PDF 1,291,161 bytes < 7 MB, real text layer (ToUnicode present). Web P1 and P8
  rendered (`pages/web-p1-1.png`, `pages/web-p8-8.png`) and viewed: identical to
  print, no tofu.

## 9. p8.py extract + compare (canonical tool)

- `tools/p8.py extract --p8 svg/p8-valutazione.svg --total 150` → noted 150/150, RC=0.
- `tools/p8.py compare --core-p8 core-it/svg/p8-valutazione.svg --edition-p8 …` →
  status **CLEAN**, missing=[] extra=0, keydiff **[137, 138, 139]** (expected re-aimed
  reader-sentence keys; verified by hand: 137 "For Madonna della Salute, people
  cross the votive bridge.", 138 "On Sunday evening, Atalanta play Inter.",
  139 "On Saturday, Lazio play Lecce at home."; 140 "Ogni cifra deve essere
  chiara." is the Italian sentence in both, so no diff — correct behaviour).
  Logs: `p8-extract.log`, `p8-compare.log`; JSONs in `en/`.

## 10. gates.py re-run (20/20 PASS)

Copied `gates.py` + `validate_edition_textmd.py` from proof2's scratch into my
scratch, repointed SCRATCH at my dir, and used the EDITED `translations.py`
(fix1r2 copy, with the three new `"en"` values). Ran with the tools venv python
against the shipped edition. Log: `gates-en.log`.
Results (all PASS): occlusion 0 flags · p8 extract noted 150 · p8 compare CLEAN
keydiffs [137,138,139] · freeze diff 0 unexplained fragments (P1–7) · freeze diff
report present (pages 1–8) · freeze strict-cjk (only U+3000, 13×) · print/web text
multiset identical (7931/7931 words, chars equal) · web < 7 MB · print size sane ·
P8 min font 13.0 px · paper #fbfaf6 present · no gold/brick/near-black · VOL.5 only
in the 3 legitimate nodes · VOL.4 count 9 · badge colours present · no double outer
frame (0 full-page rects) · textmd validate forward-miss 0 / reverse-miss 0 ·
answers 150/150 · keys 1–150 match core (except 137–139 + writing) · notes match
translations.py (except 137–140 + writing). Final line: "GATES ALL PASS".

## 11. §1.1 scans (from gates.py + proofer's own)

- Paper `#fbfaf6` present on all 8 pages; bad colours
  `#c9a227/#b8860b/#8b4513/#a0522d/#1a1a1a/#000000/#d4af37` — 0 hits.
- VOL.4 count 9 across SVGs; VOL.5 = 3 text nodes only (P2 cross-reference,
  P7 LETTERE disclosure, P7 next-week preview — same 3 as the core).
- Badge colours A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f` present.
- No double outer frame: 0 full-page rects.
- P8 min font: 13.0 SVG px = 9.75 pt (SOP §1.1 floor, exactly at floor).
- "·" total in SVGs: 149 (core pattern: options/gloss lists only).

## 12. Character scans

- `.text.md` CJK ideographs: **0**. U+3000 ×106, U+FF1A ×14.
- U+2019: 0 in all 8 SVGs and in `.text.md`; U+2018: 0.
- SVG CJK scan: P1 ideographs = 3, all inside `<title>Lucerna 三色蛾</title>`
  (moth logo metadata, not rendered text; also present in the core).
- Banned terms (Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu): 0 in `.text.md`.
- ABSTRACT.txt: CJK 0, fullwidth 0, one line, no ASCII double quotes.

## 13. 150-key three-source audit (proofer's own script)

- Inline stem keys parsed 150/150; RISPOSTE keys parsed 150/150; P8 printed keys
  150/150 (from `en/p8-extract.json`).
- Stem keys vs RISPOSTE: 0 real mismatches (8 apparent diffs are the parser
  catching the explanatory note inside nested parentheses — key heads match, e.g.
  Q13 `candele`, Q58 `più bella`, Q77 `ci sarà`).
- P8 printed keys vs RISPOSTE: 0 mismatches (Q150 open writing task excluded from
  the key comparison; it carries the ✓ model-text marker).
- Model text: 99 words (range 80–100).

## 14. Visual read (fresh renders, proofer's own)

- `pdftoppm -r 96` the delivered print PDF → `pages/p-1.png` … `pages/p-8.png`
  (1950×2700 each), all 8 viewed. Web P1/P8 viewed (see gate 8).
- Results: P1 — clean (cifre title fully in box, +20 px pixel spare); P2 — clean
  (frase title fully in box); P3 — clean (core-pattern mid-page whitespace);
  P4 — clean (E TU box 2 lines + gloss, flush with the results table; results
  table clean); P5 — clean (core-pattern whitespace); P6 — clean except inherited
  "18." orphan line (O-10); P7 — clean (errori title fully in box, final "S" well
  inside; LETTERE disclosure 3 lines clear of the FRASI hline); P8 — dense but
  legible, "Translate into English/Italian" labels correct, model text present,
  keys flow ends 2514/2552, no footer intrusion.
- No overflow, overlap, footer intrusion, or tofu anywhere.

## 15. Fact / date verification (this round)

- Dates/weekdays (Europe/Rome `date`): Nov 6 Fri, Nov 7 Sat, Nov 8 Sun, Nov 9 Mon,
  Nov 12 Thu, Nov 15 Sun, Nov 16 Mon, Nov 17 Tue, Nov 19 Thu, Nov 20 Fri,
  Nov 21 Sat, Nov 22 Sun, Nov 23 Mon, Nov 24 Tue, Dec 2 Wed, Dec 6 Sun,
  Dec 31 Thu — all match the paper. MD11 days Fri 6 / Sat 7 / Sun 8 Nov 2026 confirmed.
- Arithmetic re-verified by hand (MD11 goals 24; Q85 13−11=2; Q86 6+7=13; model
  text 99 words counted by script).
- Golden sentences: all 8 verified verbatim in their articles and on P7 FRASI.
- Serie A / ATP Finals / BookCity / Manovra / Eurochocolate / Torrone facts:
  proof1/proof2 web verifications stand (re-checked only for internal consistency
  in this round); no new fact introduced by fix1 (only the 3 gloss words changed,
  and the Italian halves are byte-identical).
- Not re-surfaced in this round's searches (rest on the core KIT's stated
  verification, as in proof2): bill number C. 3174-bis; hearing dates Nov 9–12;
  amendments deadline Nov 17 18:00.
