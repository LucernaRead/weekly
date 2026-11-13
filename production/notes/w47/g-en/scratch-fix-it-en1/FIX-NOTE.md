# FIX-NOTE — 2026-W47 it-en fix1 (D-1 only)

- Builder: fix1 (2026-11-11). Proof: proof1 (叶子), PROOF-NOTE.md + GATE-LOG.md in `scratch-proof-it-en1/`.
- Scope: ONLY D-1. O-1–O-10 untouched; core-it untouched; W46 it-en untouched; no commit/push, no insert.py, no lint --write.

## Defect D-1

`2026-w47-it-en.text.md` Q137–140 exercise lines carried the frozen Chinese
registry type label `翻译` (lines 969/971/973/975). The P8 render already said
"Translate into English" / "Translate into Italian", and every other type in
the edition was already English — only `翻译` was kept (W46 precedent in
`translations.py`, deliberately NOT in the table).

## Fix (fan-out-local, export-level)

- Method: re-ran the same AST exporter `build_edition.py` used
  (`production/2026-w46/core-it/finish/export_it_textmd.py`, imported
  read-only, NOT modified), with the registry type translated at emit time:
  `翻译` → `Translate` (`[A2 · 翻译]` → `[A2 · Translate]`).
  Script: `fix_export.py` in this scratch dir.
- Verification before overwrite: plain re-export reproduced the shipped file
  byte-for-byte (55,262 B); fixed export differed in exactly the 4 exercise
  lines (plus their blank separators inside the diff hunk; asserted each added
  line equals the removed line with only the label changed).
- Changed file: `production/2026-w47/2026-w47-it-en/2026-w47-it-en.text.md`,
  lines 969/971/973/975 only:
  - `137. [A2 · Translate] …`, `138. [B1 · Translate] …`,
    `139. [B1 · Translate] …`, `140. [B2 · Translate] …`
- RISPOSTE section unchanged (carries no type label; writing_type is "Writing").
- No build input touched: `content*.py`, `bslib4.py`, `render.py`, SVGs all untouched.

## New .text.md

- SHA-256: `7160560555042d9992fda8cb8b21b3067eb8374a6279a50b19abdc3443e69c30`
- Size: 55,274 bytes (was 55,262), 1317 lines (unchanged).
- CJK scan: ideographs U+4E00–U+9FFF = **0**; `翻译` = 0; `· Translate]` = 4.
  Remaining non-ASCII: 106 × U+3000 (furniture separators, unchanged) +
  14 × U+FF1A (7 frozen P8 notes × 2 appearances, O-4, unchanged).
- U+2019 in .text.md: 0.

## PDFs — UNCHANGED (no re-render; export only)

- Print `La-Lucerna-VOL4-EN.pdf`: 14,032,990 B,
  sha256 `d41e7255d7da8ea63cf07560911a518b2e55a4a7d8a9eb8b0f3c1ae6d3129e2f`
- Web `La-Lucerna-VOL4-EN-web.pdf`: 1,259,104 B,
  sha256 `32a6727966cfa130618c64356cd9db9812f04cbc96e961ff1534b143580e5903`
- Both match the proof1 target SHAs exactly. Print/web pdftotext multiset
  identical: 7,946 words each, 0 diff.

## Gates (all green, re-run post-fix; logs in this dir)

| gate | result |
|---|---|
| p8 extract | 150/150, rc 0 |
| p8 compare vs core-it | CLEAN, missing=[], extra=0, keydiff=[137,138,139] (expected re-aim) |
| .text.md validator | forward-miss 0 / reverse-miss 0, rc 0 |
| U+2019 full scan (8 SVGs) | 0 (U+2018 also 0) |
| CJK scan (.text.md) | ideographs 0, 翻译 0 (see above) |
| occlusion audit | 0 flags (selftest OK, all 6 classes fired) |
| freeze baseline | 8/8 SVGs byte-identical; shipped SVGs unchanged by the run |
| freeze diff core↔en | added CJK 13 × U+3000 only (furniture); P8 +164/−629 as in proof1 |
| SVG SHA before/after fix | 8/8 identical |
| VOL | VOL.4 ×9; VOL.5 ×3, all 3 in the legitimate nodes (P2 cross-ref, P7 disclosure, P7 next-week preview) |
| P8 min font | 13.0 px = 9.75 pt (SOP §1.1 floor) |

## Notes / gaps

- Probe pre-work: `git hash-object -w` OK; real file write into
  `weekly-git/hidden_files/w47/` OK (probe file removed afterwards). Disk 45G free.
- brief-coordinator.md does NOT exist at the tasked path
  `~/workspace/weekly-git/hidden_files/w47/briefs/`; the file actually read was
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/briefs/brief-coordinator.md`.
- O-10 (KIT says .text.md 55,286 B, disk was 55,262 B): after the fix the file
  is 55,274 B — still not the KIT figure; KIT figure remains unexplained
  (likely a KIT typo, as the proofer suggested). Not a content defect; KIT not edited (out of scope).
- It-en edition dir is untracked in git (`??`), so no git diff is available;
  identity is established by the SHA-256 values above.

## Other it-family editions — 「翻译」 residue (report only, NOT fixed)

All 9 other built W47 it editions carry the same 4 × `翻译` at lines 969/971/973/975
(Q137–140), same pattern as it-en had. it-zh-cn is not built yet (no .text.md).

| edition | .text.md | 「翻译」 count |
|---|---|---|
| it-de | exists | 4 |
| it-fr | exists | 4 |
| it-es | exists | 4 |
| it-pt | exists | 4 |
| it-nl | exists | 4 |
| it-ru | exists | 4 |
| it-ja | exists | 4 |
| it-ko | exists | 4 |
| it-zh-tw | exists | 4 |
| it-zh-cn | NOT BUILT | — (no file to check) |

Note: for ja/ko/zh-tw the residue is also `翻译` (Chinese characters) inside the
type label, not their own reader language; each edition's proof1 handles it.
W46 it-en has the same residue (per proof1) — already-published week, NOT touched.
