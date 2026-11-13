# GATE-LOG.md — 2026-W47 it-en (round 2 proofread, re-fan-out), mechanical gates self-run

Proofer: independent proof2, 2026-11-11. All commands run by the proofer; nothing
copied from builder logs. Working directory: ~/workspace/weekly-git.
My scratch dir: ~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-en1/
`PYTHONDONTWRITEBYTECODE=1` throughout. TMPDIR = my scratch (never /tmp).

## 0. Hard-gate probes (pre-work, 2026-11-11 ~20:16 UTC)

| probe | result |
|---|---|
| `git -C ~/workspace/weekly-git hash-object -w /dev/null` | OK (`e69de29bb2…`, RC=0) |
| real file write into scratch `scratch-proof2-it-en1/probe.txt` | OK |

## 1. Identity (KIT §1 three SHA)

Proofer's own `sha256sum`:
- print `3b6b2d2c9067aa88e22914a83ef4ca6ddf37ce2e98e154c80bd9ca7fb79190fd`, 14,032,945 B — MATCHES task + KIT §7
- web `03bb1ff239dc46d408130d8c828417e004a9a0b488ba50e8594f5a8122dd5e2f`, 1,291,182 B — MATCHES
- text.md `f12950aa8561371585da7ada54b15eb83df595ccb0fe51cfa513650dffd6a984`, 55,221 B / 1317 lines — MATCHES

## 2. Build interpreter

`tools/venv/bin/python -c 'import PIL'` → Pillow 13.0.0 (same as the build).
System python3 → Pillow 10.2.0, not used.

## 3. run.py re-run (in a scratch copy) — RC=0, TOTAL 150, 0 overflow

Command: copied the whole edition dir to `scratch/rerun/edition` (minus
`cards/`, `__pycache__/`, `svg/`), ran `tools/venv/bin/python run.py` there,
output to `rerun/run.log`.
Result: RC=0; 0 occurrences of FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE;
TOTAL 150; levels A2 47 / B1 70 / B2 33; pages 10/18/18/18/18/18/12/38;
model words 99. P1-headline ends 1362; P4 col3 ends 1140.45; P7 col3 ends 1673.0;
P8-keys flow ends col 3 y=2514 (bottom 2552).

**IMPORTANT — production write incident (transparent record):** the edition's
`content*.py` hardcode `OUT = ~/workspace/weekly-git/production/2026-w47/2026-w47-it-en/svg`,
so this scratch-copy run REWROTE the production SVGs (mtimes 2026-11-11 20:19 UTC).
No other production file was touched. The rewritten SVGs were verified
byte-identical 8/8 against the re-fan-out freeze-baseline copy in
`scratch-fanout-it/en/freeze-baseline/svg/` (cmp, 8/8 IDENTICAL), and the
delivered print PDF re-rendered from them is byte-identical to the shipped PDF
(gate 4). Production content is therefore unaltered; only mtimes changed.
The canonical `freeze.py baseline` run (gate 5) rewrites output paths into its
scratch tree and does NOT touch production — that is the safe path; direct
`run.py` re-runs must patch OUT first. This is also why proof1's "8/8 in a
scratch copy" claim is silently the same behaviour.

## 4. SVG rebuild 8/8 + print PDF re-render byte-identical

- Re-run SVGs (written to production by the hardcoded OUT, see §3) vs the
  re-fan-out freeze-baseline SVG copies: `cmp` 8/8 byte-identical
  (p1–p8 sha256 recorded in the proofer's notes; e.g. p1
  `59dddb7541b7…`, p8 `af25b666b16e…`).
- Print PDF re-render: my own `rerender.py` (same steps as edition `render.py`:
  cairosvg svg2pdf per page + pypdf merge, reading the shipped SVGs read-only,
  writing only to scratch) → `rerender-print.pdf` 14,032,945 bytes, sha256
  `3b6b2d2c9067aa88e22914a83ef4ca6ddf37ce2e98e154c80bd9ca7fb79190fd` —
  **BYTE-IDENTICAL to the delivered print PDF**. (Edition `render.py` was NOT
  run as-is: its BASE is hardcoded to production and it would overwrite the
  delivered PDF and `cards/`.)
- Web PDF was NOT re-rendered (task: web PDF bytes are not reproducible; only
  its text layer was compared — gate 8).

## 5. Freeze (canonical tool)

- `tools/freeze.py baseline --build <scratch rerun copy> --core-svg <edition svg> --out <scratch>/freeze-baseline` → RC=0, 8/8 "OK" (produced sha256 ==
  core sha256 for all 8 SVGs); "core integrity: shipped core SVGs unchanged by
  the run (8 files re-hashed)". Log: `freeze-baseline.log`.
- `tools/freeze.py diff` core vs edition (via the gates.py copy, JSON in
  `en/freeze-diff.json`): pages 1–8 present; every added/removed text-node
  fragment on P1–P7 explained by a translations.py value/key, a NOTE/gloss
  composite, a gloss + " (Pagina N)" composite, or generated page furniture —
  **0 unexplained fragments**. Strict-CJK: added CJK = 13 × U+3000 only
  (furniture separators, exempt); non-space added CJK = {}.
  Note: `freeze.py diff` exit code is 1 for Latin editions in this setup (the
  strict-CJK report lists the exempt U+3000); the gate reads the JSON, not the RC.

## 6. Occlusion audit (canonical tool)

- `tools/occlusion_audit.py <edition svg>` (selftest OK — all 6 classes fire,
  clean controls silent): **0 flags** on the 8 shipped SVGs.
- Caveat recorded in PROOF-NOTE.md: BOXTITLE covers bordered boxes only;
  borderless cream boxes are blind to horizontal overflow — the cream-box scan
  (gate 7) is the supplement, and it found D-1/D-2/D-3.

## 7. Cream-box PIL true-ink scan + spill scan + orphan scan (my script)

Script: `cream_spill_orphan.py` (uses `occlusion_audit.ink_box` true ink;
29 cream rects `#f0eee5` across P1–P7; P8 has 0 cream rects).
- Text nodes scanned: P1 175, P2 179, P3 178, P4 173, P5 168, P6 191, P7 161, P8 380.
- CREAM-X flags: **3** — P1 cifre title ink 556.5..1118.0 vs box ..961.0 (D-1);
  P2 frase title 556.5..1000.8 vs box ..961.0 (D-2); P7 errori title
  1461.5..1868.5 vs box ..1862.0 (D-3). All three confirmed by pixel measurement
  on the 96 dpi render of the delivered print PDF (overhangs 155 / 39 / 6 px)
  and by 2× crops (`pages/crop-p1-cifre.png`, `crop-p2-frase.png`,
  `crop-p7-errori.png`). Core contrast: core titles fit (960.0/961, 918/961,
  1735.8/1862).
- CREAM-Y flags: 0. SPILL-PAGE flags: 0 (no ink outside 1950×2700).
  SPILL-FOOTER flags: 0 (no ink below y=2580 outside furniture).
- ORPHAN flags: **3**, all adjudicated NOT defects — each node is byte-identical
  (same text, same x/y) in the core SVGs (P6 "18." at 1603.5/641.6; P8 "due" at
  538.5/818.975; P8 Q137 "___" blank). Frozen Italian text, inherited wraps.
  See PROOF-NOTE.md O-10; crops `crop-p6-orphan.png`, `crop-p8-q118.png`.

## 8. Text-layer consistency (print vs web PDF)

- `pdftotext -layout` on both PDFs → word multiset identical, 7934 words each,
  char multiset equal, 0 diffs. Both extract 109,236 bytes.
- Web PDF 1,291,182 bytes < 7 MB, real text layer (ToUnicode present).
  Web P1 and P8 rendered (`pages/web-p1-1.png`, `pages/web-p8-8.png`) and viewed:
  identical to print, no tofu. D-1/D-2/D-3 visible in the web render too.

## 9. p8.py extract + compare (canonical tool)

- `tools/p8.py extract --p8 svg/p8-valutazione.svg --total 150` → noted 150/150, RC=0.
- `tools/p8.py compare --core-p8 core-it/svg/p8-valutazione.svg --edition-p8 …` →
  status CLEAN, keydiff **[137, 138, 139]** (expected re-aimed reader-sentence
  keys; verified by hand: 137 "For Madonna della Salute, people cross the votive
  bridge.", 138 "On Sunday evening, Atalanta play Inter.",
  139 "On Saturday, Lazio play Lecce at home."; 140 "Ogni cifra deve essere
  chiara." is the Italian sentence in both, so no diff — correct behaviour).

## 10. gates.py copy re-run (20/20 PASS)

Copied `gates.py` + `translations.py` + `validate_edition_textmd.py` from
`scratch-fanout-it/` into my scratch, repointed SCRATCH at my dir, ran with the
tools venv python against the shipped edition. Log: `gates-en.log`.
Results (all PASS): occlusion 0 flags · p8 extract noted 150 · p8 compare CLEAN
keydiffs [137,138,139] · freeze diff 0 unexplained · freeze diff report present
(pages 1–8) · freeze strict-cjk (only U+3000) · print/web text multiset identical
(7934/7934 words, chars equal) · web < 7 MB · print size sane · P8 min font
13.0 px · paper #fbfaf6 present · no gold/brick/near-black · VOL.5 only in the 3
legitimate nodes · VOL.4 count 9 · badge colours present · no double outer frame
(0 full-page rects) · textmd validate forward-miss 0 / reverse-miss 0 ·
answers 150/150 · keys 1–150 match core (except 137–139 + writing) · notes match
translations.py (except 137–140 + writing). Final line: "GATES ALL PASS".
Caveat: these 20 gates do not measure cream-box title fit — that is gate 7 above.

## 11. §1.1 scans (from gates.py + proofer's own)

- Paper `#fbfaf6` present; bad colours `#c9a227/#b8860b/#8b4513/#a0522d/#1a1a1a/#000000/#d4af37` — 0 hits.
- VOL.4 count 9 across SVGs; VOL.5 = 3 text nodes only (P2 cross-reference,
  P7 LETTERE disclosure, P7 next-week preview — same 3 as the core).
- Badge colours A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f` present.
- No double outer frame: 0 full-page rects.
- P8 min font: 13.0 SVG px = 9.75 pt (SOP §1.1 floor, exactly at floor).
- "·" total in SVGs: 149 (core pattern: options/gloss lists only).

## 12. Character scans

- `.text.md` CJK ideographs: **0** (proof1 D-1 fixed). U+3000 ×106, U+FF1A ×14.
- U+2019: 0 in all 8 SVGs and in `.text.md`; U+2018: 0.
- SVG CJK scan: P1 ideographs = 3, all inside `<title>Lucerna 三色蛾</title>`
  (moth logo metadata, not rendered text; also present in the core).
- Banned terms (Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu): 0 in `.text.md`.
- ABSTRACT.txt: CJK 0, fullwidth 0, one line, no ASCII double quotes.

## 13. Title count (measured, not assumed)

- Article headlines: 6 (P1–P6). All-caps title/furniture lines in `.text.md`: 85.
  Page sections: 8 + 1 answer-key section. The string "56" occurs only twice in
  `.text.md` (exercise 56, stem + key). No element of this edition counts 56.

## 14. Visual read (fresh renders, proofer's own)

- `pdftoppm -r 96` the delivered print PDF → `pages/p-1.png` … `pages/p-8.png`
  (1950×2700 each), all 8 viewed. Web P1/P8 viewed (see gate 8).
- Results: P1 — D-1 visible (cifre title off its box); P2 — D-2 visible (frase
  title off its box); P3 — clean (core-pattern mid-page whitespace);
  P4 — clean (E TU box 2 lines + gloss, flush with the table; results table clean);
  P5 — clean (core-pattern whitespace); P6 — clean except inherited "18." orphan
  line (O-10); P7 — D-3 visible (errori title S straddles the box edge),
  LETTERE disclosure 3 lines clear of the FRASI hline; P8 — dense but legible,
  "Translate into English/Italian" labels correct, model text present, keys flow
  ends 2514/2552, no footer intrusion.
- No overflow, overlap, footer intrusion, or tofu other than D-1/D-2/D-3.

## 15. Fact verification (web, 2026-11-11)

- Eurochocolate 2026 = 32ª edizione, Nov 13–22, theme "Fate Dolci", Calabria
  guest region, Massari at the Nov 22 finale — confirmed (eurochocolate.net;
  tagumbria.it; latuaetruria.it). Q30/Q123 correct.
- Festa del Torrone 2026 = 29ª edizione, Nov 7–22, 16 days / 3 weekends, theme
  "Il Confine", Torrone d'Oro to Davide Simonetta (Cremona-born) 11:00 Palatorrone
  Sun 22, corteo 16:00, re-enactment 17:00 — confirmed (milanodimoda.it;
  foodtour.info; dossiercultura.it). All P3 times/numbers match.
- Weekdays (Europe/Rome `date`): Nov 9 Mon, Nov 12 Thu, Nov 15 Sun, Nov 16 Mon,
  Nov 17 Tue, Nov 19 Thu, Nov 20 Fri, Nov 21 Sat, Nov 22 Sun, Nov 23 Mon,
  Nov 24 Tue, Dec 2 Wed, Dec 6 Sun, Dec 31 Thu — all match the paper. MD11 days
  Fri 6 / Sat 7 / Sun 8 Nov 2026 confirmed.
- Serie A / ATP Finals / BookCity / Manovra facts: proof1's web verifications
  stand (re-checked only where this round added coverage, i.e. the two edition
  numbers above); arithmetic re-verified by hand (MD11 goals 24; Q85 13−11=2;
  Q86 6+7=13; model text 99 words counted by hand).
- Not re-surfaced in this round's searches (rest on the core KIT's stated
  verification, as in proof1): bill number C. 3174-bis; hearing dates Nov 9–12;
  amendments deadline Nov 17 18:00.
