# GATE-LOG.md — 2026-W47 it-en (round 1 proofread), mechanical gates self-run

Proofer: 叶子, 2026-11-11. All commands run by the proofer; nothing copied from builder logs.
Paths are absolute. Working directory: ~/workspace/weekly-git.
My scratch dir: ~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-it-en1/

## 0. Hard-gate probes (pre-work, ~2026-11-11 07:27 UTC)

| probe | result |
|---|---|
| `echo probe \| git -C ~/workspace/weekly-git hash-object -w --stdin` | OK (returned a hash) |
| real small file write into `.../hidden_files/w47/` | OK (`probe.txt`, "probe-ok 2026-11-11T07:27:58Z") |

## 1. Identity

- `ls` of the edition dir confirms filenames `La-Lucerna-VOL4-EN.pdf` (print) and
  `La-Lucerna-VOL4-EN-web.pdf` (web).
- `sha256sum` (proofer's own computation, full strings in PROOF-NOTE.md):
  - print `d41e7255d7da8ea63cf07560911a518b2e55a4a7d8a9eb8b0f3c1ae6d3129e2f`,
    14,032,990 bytes — matches KIT §7.
  - web `32a6727966cfa130618c64356cd9db9812f04cbc96e961ff1534b143580e5903`,
    1,259,104 bytes — matches KIT §7.
- Core identity (measured by me 2026-11-11, read-only; the core tree is a different team's
  responsibility and is not modified by this proofread):
  - print PDF `La-Lucerna-VOL4.pdf` 27,726,384 bytes,
    sha256 `fc5e952d08c000920329b60dd9527c98fd206f10abfda5615f374113118d2d3a`
  - web PDF `La-Lucerna-VOL4-web.pdf` 1,758,563 bytes,
    sha256 `4381cdf740fc6d9ae025da733d4e4b2cd357ed299d686e5d37a345d4a3bfc3f5`
  - `git status --porcelain` in this clone shows `production/2026-w47/core-it/` as an
    untracked directory (`??`), so no comparison against a committed core baseline was
    possible from here, and the core's own KIT figures were not re-verified (out of scope
    for this fan-out proofread). The en edition's identity (above) matches its own KIT
    exactly, and its text content matches the core text on the files diffed (gate 7).
    The EN text export on disk is 55,262 bytes (KIT says 55,286; see PROOF-NOTE.md O-10).

## 2. Build interpreter

- KIT §7: reproduce with `tools/venv/bin/python` (Pillow 13.0.0).
- Checked: `tools/venv/bin/python -c 'import PIL; print(PIL.__version__)'` → 13.0.0.
  System `python3` → Pillow 10.2.0 (NOT used for any gate). The ko-family Pillow-version
  flip therefore cannot occur: the same interpreter reproduces the shipped SVGs 8/8
  (see gate 5).

## 3. Occlusion audit

- Command: `tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-it-en/p[1-8].svg`
  (from `~/workspace/weekly-git/tools`).
- Selftest: OK — all 6 occlusion classes fired, clean controls silent.
- Result: 0 flags (all pages clean).
- Note: `--json` combined with `--selftest` did not write an `occlusion.json` file; the
  plain re-run printed "0 flags" to stdout instead. The result is the stdout report, not a
  JSON file.

## 4. p8.py extract + compare

- `tools/p8.py extract production/2026-w47/2026-w47-it-en/p8.svg` → noted 150/150, RC 0.
- `tools/p8.py compare --extract p8-extract.json --dir production/2026-w47/core-it` →
  status CLEAN, missing=[], extra=0.
- keydiff: [137, 138, 139] — RE-AIMED translation items (reader-target sentences translated
  into English, core keys are the Chinese translations). Verified by hand:
  - 137 EN "For Madonna della Salute, people cross the votive bridge." ✓
  - 138 EN "Seven days of books, reasons and madness." ✓
  - 139 EN "For the best read, I turn to the Evening Nugget." ✓
  - 140 IT "Ogni cifra deve essere chiara." — same key value in both (Italian original),
    so it does not appear in the keydiff. ✓

## 5. Freeze (direct sha256 comparison of SVGs)

- `run.py` re-run in a scratch copy (`scratch-proof-it-en1/rerun/edition/`) with the build
  interpreter: RC 0, 0 overflow warnings, TOTAL 150, levels A2 47/B1 70/B2 33,
  pages 10/18/18/18/18/18/12/38, model words 99. P8-keys ended 2514 (bottom 2552);
  P7 col3 ends 1673.0.
- `sha256sum` of the re-run SVGs vs shipped SVGs: 8/8 byte-identical (p1–p8).
- Canonical tool, run in `tools/`: `tools/freeze.py baseline --build <scratch copy> --core-svg
  <edition svg> --out <scratch>/freeze-baseline` → RC 0, "core integrity: shipped core SVGs
  unchanged".
- `tools/freeze.py diff` core vs edition:
  - Added CJK (unexplained fragments): 13 × U+3000 total (P1 1, P2 2, P3 2, P4 2, P5 2,
    P6 2, P7 1, P8 1) — furniture separators, exempt.
  - P8 string diff +164/−629 (expected: Chinese notes → English).
  - "VOL.4 → VOL.5: 3 nodes" aggregate (P2 ×1 cross-reference, P7 ×2 disclosure + next-week).

## 6. Text-layer consistency (print vs web PDF)

- `pdftotext` on both PDFs → Counter of words, compared as multisets: identical,
  7,946 words each, print-only 0, web-only 0.
- Note: the builder's gates5.log says 7,945 (off by 1, counting method); both sides are
  equal here, which is the requirement.
- Web PDF has a real text layer (pdftotext returns full text), 1,259,104 bytes < 7 MB.

## 7. .text.md structural validation

- Validator `tools/.../validate_edition_textmd.py <edition dir> 2026-w47-it-en`:
  forward-miss 0 / reverse-miss 0, RC 0.
- Core↔en `.text.md` diff (difflib, token-based, from the builder's script run by me):
  400 equal blocks, 401 replace blocks, 0 delete/insert.
  - Only Italian prose changed: the 4 P1 cifre heads translated to English
    (Q1...29, Q2...24, Q3...20.45, "oltre 150" — see PROOF-NOTE.md O-1).
  - Everything else changed is explanation-layer Chinese→English swap; all Italian
    article prose, stems, tables, captions, FRASI, model text byte-identical to the core.

## 8. Visual read (fresh renders, proofer's own)

- `pdftoppm -r 110` the print PDF → p-1..p-8.png, each viewed; web PDF P1 & P8 rendered
  and viewed (web == print, no tofu).
- Crops: P1 masthead band right end (final "A" of VENEZIA fully rendered, clear space to
  edge); P8 keys 16–20 (wide gap after ":" on key 16 — see O-4).
- Results: P1–P7 clean, no overflow/overlap/footer intrusion; P8 dense but legible,
  keys flow ends 2514/2552.
- Previously-recorded defects re-verified fixed: P4 E TU box now 2 lines + gloss, flush with
  the table header (build2 occlusion defect); P7 LETTERE disclosure 3 lines ends 1673.0,
  clear of the FRASI hline (build3 LINEX defect).
- Golden sentences: all 8 occur exactly 2× in `.text.md` (article + P7).

## 9. Character scans

- U+2019: 0 in all 8 SVGs; U+2018: 0. Straight apostrophes: 74 total (present, render fine,
  no wide-glyph breakage on P1/P4 lines viewed).
- SVG CJK scan: P1 ideographs = 3, all inside `<title>Lucerna 三色蛾</title>` (moth logo
  metadata, not rendered text; also present in the core). P1–P8 added U+3000 = 13 (frozen).
  P8 fullwidth colon U+FF1A ×7 (notes 16,17,18,19,20,60,61) — see O-4.
- `.text.md` CJK: only 「翻译」 ×4 (Q137–140 type labels, each appearing once in the
  exercise line) + 14 × U+FF1A (7 notes × 2 appearances: exercise list + RISPOSTE) +
  106 × U+3000 (furniture separators). See D-1 and O-4.
- ABSTRACT.txt: CJK 0, fullwidth 0. WEEKLY-KIT.md: CJK 2 — both inside the KIT's own
  sentence "the only CJK is the deliberately kept 「翻译」 type label on Q137–140" (build
  record, not a reader deliverable).

## 10. Counts (all from proofer's own scripts)

- TOTAL 150; A2 47 / B1 70 / B2 33; pages 10/18/18/18/18/18/12/38.
- Badge rects (60×30, rx=2.7) per page: P1 A2 9/B1 1; P2 A2 14/B1 1; P3 A2 8/B1 10;
  P4 B1 13/B2 2; P5 B1 15/B2 3; P6 B2 18; P7 A2 4/B1 4/B2 4; P8 A2 9/B1 23/B2 3.
  Total 141 badges (150 minus the 3 grouped badges 25–28, 52–55, 141–144).
- VOL.4 ×9 across SVGs. VOL.5 = 3 nodes only (legitimate — see gate 5).
- P8 min font: 13.0 px = 9.75 pt (SOP §1.1 floor, exactly at floor).
- Banned words: Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu — 0 in `.text.md`.

## 11. Fact verification (web, 2026-11-11; sources in PROOF-NOTE.md)

- Serie A MD11 (10 scores, 24 goals) ✓; post-MD11 table ✓; Gattuso → Lazio 23 June 2026 ✓
  (ESPN / OneFootball / SoccerNews / Football-Italia).
- ATP Finals 2026 (Zverev No. 1 since 2 Nov, Sinner 2024+2025 champion, out injured 2026,
  Inalpi Arena 15–22 Nov, Cobolli) ✓ (TNT Sports 2026-11-09, LiveTennis, Tennis Majors).
- BookCity 2026 (23–29 Nov, 15th, "Il senno sulla Luna" / Ariosto, IULM) ✓.
- Manovra 2027 (DPB +0.8% / deficit 3.4%, Council of Ministers 28 Oct, ~26 miliardi,
  Irpef 33% bracket 50k→55k, ~5 miliardi banks/insurance, final approval 31 Dec) ✓.
- Weekdays (Europe/Rome `date`): 12 Nov Thu, 15 Nov Sun, 16 Nov Mon, 17 Nov Tue,
  19 Nov Thu, 20 Nov Fri, 21 Nov Sat, 22 Sun, 23 Mon, 24 Tue — all match the paper.
- Not re-surfaced in my searches (rests on core KIT verification, not re-verified):
  bill number C. 3174-bis; hearing dates 9–12 Nov; amendments deadline 17 Nov 18:00.
