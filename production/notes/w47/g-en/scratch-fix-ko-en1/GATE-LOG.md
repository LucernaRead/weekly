# GATE LOG — W47 ko-en fix1 (builder self-check gates, 2026-11-11)

Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ko-en/`
Note dir: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ko-en1/`
All tools run from `~/workspace/weekly-git/` with `/usr/bin/python3` for
run.py/textmd.py/freeze/p8/occlusion (locked interpreter per core-ko KIT run 10)
and `tools/venv/bin/python` for render.py/webpdf.py. Outputs in `work/`
(freeze build copy deleted after the run — reproducible intermediate).

## Fixes (source: only `content7.py`, 2 lines)

- D1: `content7.py:81` curly U+201C/U+201D → straight U+0022.
- D2: `content7.py:127` phrase 7 → P1 sentence
  `「수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요」`,
  gloss "After the CSAT ends, Kimchi Day comes on Sunday, Nov 22.", citation (1면).
  P1 sentence verified verbatim in `content12.py:39` (lead_para), in text.md,
  and in core-ko `content12.py:39` + core text.md:27 (coordinator follow-up
  cross-check, 2026-11-11). The P5 candidate was rejected before the
  follow-up arrived: it occurs only in `content7.py:34` (P7's own B1 column),
  never in P1–P6 — using it would have repeated the circularity.
  The follow-up required no change: fix1 already used the P1 sentence.

## Final deliverables (fix1)

| File | Size | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-KO-EN.pdf` (print) | 45,262,615 B | `8a586fdda6a20383649d0df37c13521630e70a1e72137e7ebef217a1a1fcf6a3` |
| `Lucerna-VOL4-KO-EN-web.pdf` (web) | 4,011,394 B (< 7 MB) | `cecc10999ac7987b2834b6cd7304e50e207a4d646938420234e44c1ecbbb27de` |
| `2026-w47-ko-en.text.md` | 26,447 B, 332 items | `f6be0c2316399ad0d4b04b450b75300827a07b088e9332842aecc16c36176b78` |
| `ABSTRACT.txt` | 305 B, untouched | `1187194316bea8381ec48d359fd41698d6e18e8e4dfa090889df92724fabc812` (same as run 2) |

Baseline (proof1 object) for comparison: print 45,262,664 B
`571699d6…cc18`; web 4,013,441 B `02203d24…4323`; text.md 26,389 B, 332 items.

## Gates

| Gate | Command / method | Result |
|---|---|---|
| Build | `/usr/bin/python3 run.py` | rc 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150 (A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38) — log `work/build-fix1.log` |
| SVG scope | sha256 vs run-2 list | P1–P6, P8 byte-identical; **only p7-mal.svg changed** (`cf416bb0…`) — log `work/sha-fix1.txt` |
| Curly-quote zero-scan | U+201C/U+201D/U+2019 over 8 SVGs + text.md | **0 / 0 / 0 everywhere** ✓ (D1 closed) |
| text.md | `textmd.py` | 332 items; new P1 sentence ×2 (P1 lead + P7 phrase 7); old phrase 0×; frame line absent by design (variable arg, same as core — see FIX-LOG) |
| Render | venv `render.py` | rc 0, 8 cards + print PDF 45,262,615 B — log `work/render-fix1.log` |
| Web PDF | venv `webpdf.py svg Lucerna-VOL4-KO-EN-web.pdf` | rc 0, 4,011,394 B, 50,748 text bytes, 534 distinct chars — log `work/webpdf-fix1.log` |
| Freeze baseline | `/usr/bin/python3 tools/freeze.py baseline` | **8/8 byte-identical** — log `work/freeze-baseline-fix1.log` (build copy deleted) |
| Freeze diff | `freeze.py diff` vs core-ko svg | TOTAL added CJK **15** (was 7 in proof1) — see adjudication below; log `work/freeze-diff-fix1.log` |
| p8 extract | `p8.py extract --total 150` | **150/150 noted** ✓ — log `work/p8-extract-fix1.log` |
| p8 compare | `p8.py compare` vs core P8 | **CLEAN**, missing=[] extra=0, keydiff=[137, 138] (expected re-aiming) ✓ — log `work/p8-compare-fix1.log` |
| Occlusion audit | `tools/occlusion_audit.py svg/` | selftest OK (6 classes fired, clean controls silent); **0 flags** ✓ — log `work/occlusion-fix1.log` |
| Boxtitles | `boxtitle-ko.py <ed>` | **8/8 ≤ 386.5px** ✓ |
| Text layers | `pdftotext` print vs web + `cmp` | **50,748 bytes each, byte-identical** ✓ — `work/print-fix1.txt`, `work/web-fix1.txt` |
| P8 min font | PyMuPDF min span size on P8, print + web | **9.975pt both** ≥ 9.75pt ✓ |
| Visual | P7 full page @110dpi + 300dpi crops of frame line + phrase 7 | Both fixed lines render correctly: straight quotes tight, phrase 7 one line + gloss one line, no overlap; full P7 clean — `work/p7-fix1.png`, `work/p7-frame-fix1.png`, `work/p7-phrase7-fix1.png` |
| Print vs web | 72dpi pixel diff, all 8 pages | mean abs diff ≤ 0.47/page (P6 = 0.00); layout identical, image downsampling only ✓ |

## Freeze-diff adjudication (15 added CJK vs proof1's 7)

The core-ko SVGs were rebuilt after proof1 (dated Nov 11 08:40 — the core's
parallel fix of the same phrase 7). This edition's P1–P6/P8 are byte-identical
to proofed run 2, so every P1/P4 delta is core-side, not mine:

- P1 +예/디, P4 +시/리/즈/예/디: core changed two stems in its own fix run —
  P1 quiz stem `…어디예요?` → `…어느 팀이에요?`; P4 stem `한국시리즈 시리즈 전적`
  (duplicated 시리즈, inherited by this edition from core run 10) →
  `한국시리즈 전적`. The edition still carries the old wordings. All added
  chars sit in English-gloss Korean quotations (`예비소집`, `한국시리즈`) or
  frozen Korean stems — the adjudicated Korean class (SOP: 韩语版允许读者语
  注释中引用的韩字，逐字裁定). NOT fixed here: scope is D1+D2 only.
  **For proof2 / coordinator:** the edition now diverges from current core on
  those two stems; the next full proof round should adjudicate whether the
  edition follows core's new wordings.
- P7 +후 (new vs proof1): core's phrase 7 AND its frame example both changed
  to the P1 sentence (no `후`), while this edition keeps `후` only in the
  frame example (`〜 후에`, unchanged pattern example, same as run 2).
  Legitimate; no action.

## Observations for proof2 / coordinator (not defects in this fix)

- O1: core's parallel fix also changed core P7's frame example to the P1
  sentence; this edition's frame example (`content7.py:80`) still uses
  `수능 후에 김치의 날이 와요.` — left unchanged per the fix1 scope
  ("只改金句 #7 这一条"). If the family is to stay in lockstep, that is a
  coordinator decision, not part of D1/D2.
- O2: see freeze-diff adjudication (P1/P4 stem divergence from rebuilt core).

## Scope compliance

- Changed in the edition dir: `content7.py` (2 lines) + regenerated
  `svg/p7-mal.svg`, `cards/` PNGs, both PDFs, text.md. No other file touched.
- No core-ko, no other family, no tools/, no issues/, no insert.py,
  no lint --write, no git writes (edition dir is untracked; verified via SVG
  hashes, not git diff). No subagents spawned.
- No EDQUOT incident this round (45G free at start); freeze build copy
  deleted after use; note dir 5.9M.

## Status

Fix1 build complete, all builder gates green. **NOT delivered as定稿** —
per SOP §8.4 the rebuilt edition needs a fresh full independent proof round
(proof2, to be assigned by the coordinator); this round's clean findings do
not carry over.
