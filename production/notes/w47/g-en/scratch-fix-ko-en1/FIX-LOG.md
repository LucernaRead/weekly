# FIX LOG — W47 ko-en fix1 (proof1 defects D1 + D2), 2026-11-11

- Edition: `2026-w47-ko-en` (target ko, reader English), VOL.4
- Baseline (proof1 object, verified on disk before any edit):
  - Print PDF `Lucerna-VOL4-KO-EN.pdf` 45,262,664 B, SHA-256
    `571699d675bd31f2cc656698df05908e6843517b8cc28b5e0b849a0f6f48cc18` ✓
  - Web PDF `Lucerna-VOL4-KO-EN-web.pdf` 4,013,441 B, SHA-256
    `02203d2490905b9d863c935ede7b378eb87bd00ce9bf5069ab8bbc2f109d4323` ✓
  - text.md 26,389 B, 683 lines, 332 items ✓
- Sources read before work: SOP.md §8 + §1.1 (full), AGENTS.md,
  coordinator brief (`goals/.../hidden_files/w47/briefs/brief-coordinator.md`
  — the `weekly-git/hidden_files/w47/briefs/` path in the task does not exist),
  proof1 PROOF-NOTE.md + GATE-LOG.md (full).
- Probe: `git hash-object -w` OK; note dir writable; `df` 45G free.

## Defect verification (on disk, before edit)

- D1 (中): U+201C ×2 / U+201D ×2, all in `svg/p7-mal.svg`, all other 7 SVGs 0;
  U+2019 = 0 everywhere. Source `content7.py:81`:
  `wcn = "Frame: “after ~”. Ask: “〜 후에 뭐 해요?”"`. Straight `'` ×65
  across the 8 SVGs (incl. the Korean frame example directly above this line).
  VERIFIED.
- D2 (低): phrase 7 `「수능 후에 김치의 날이 와요」` occurs in `svg/p7-mal.svg`
  only (frame example + phrases list); absent from P1–P6. Replacement
  candidates checked verbatim against sources:
  - P1 (chosen): `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요` —
    `content12.py:39` lead_para, present in text.md; in the P1 SVG it is split
    across wrapped lines (space dropped at the wrap, as in the drop-cap case).
  - P5 (REJECTED): `수능이 끝나고 사흘 뒤에 김치의 날이 와요` occurs ONLY in
    `content7.py:34` (the P7 B1 column itself) — grep over `content56.py` and
    `svg/p5-cheongnyeon.svg` / `svg/p6-gipi.svg` = 0. It is not a P1–P6
    article sentence, so swapping it in would repeat the same circularity.
    The proof note's "P5/P7-B1" attribution is imprecise; P1 is the valid
    verbatim article source. Citation becomes (1면).
- Scope: only `content7.py` in the edition dir + this note dir. No core-ko,
  no other family, no tools/, no issues/, no insert.py, no lint --write,
  no git writes.

## Fixes applied

- D1: `content7.py:81` — curly double quotes U+201C/U+201D → straight
  double quotes U+0022 (escaped `\"` inside the Python double-quoted literal):
  `wcn = "Frame: \"after ~\". Ask: \"〜 후에 뭐 해요?\""`.
- D2: `content7.py:127` (phrases list item 7 only) —
  `("「수능 후에 김치의 날이 와요」", "After the CSAT comes Kimchi Day.", "7면")`
  →
  `("「수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요」", "After the CSAT ends, Kimchi Day comes on Sunday, Nov 22.", "1면")`.
  Other 7 phrases untouched. The P7 frame example line (`content7.py:80`,
  `wt = ... '수능 후에 김치의 날이 와요.' ...`) is a pattern example, not a
  verbatim-claim item — left unchanged per task scope ("只改金句 #7 这一条").

## Rebuild (fix1)

- Build interpreter lock (core-ko KIT lesson, run 10): `/usr/bin/python3` for
  run.py / textmd.py (PIL 10.2.0 metrics); `tools/venv/bin/python` for
  render.py / webpdf.py only.
- Commands (to be filled with logs as they run):
  1. `/usr/bin/python3 run.py` — rebuild 8 SVGs.
  2. `/usr/bin/python3 textmd.py . 2026-w47-ko-en 2026-w47-ko-en.text.md "Lucerna Korean Weekly VOL.4 — Korean text, English explanations (2026-W47)"`
  3. `tools/venv/bin/python render.py` — cards PNGs + print PDF.
  4. `tools/venv/bin/python ../../tools/webpdf.py svg Lucerna-VOL4-KO-EN-web.pdf` — web PDF.
  5. Gates: U+201C/U+201D/U+2019 zero-scan (8 SVGs + text.md + ABSTRACT.txt),
     freeze baseline, freeze diff, p8 extract + compare, occlusion audit,
     text-layer byte identity print vs web, P8 min font, SVG hash list,
     P7 visual zoom re-check of both fixed lines, print-vs-web pixel diff.

## Results

- Build: `/usr/bin/python3 run.py` rc 0, 0 warnings, TOTAL 150 (same split as
  run 2). Only `svg/p7-mal.svg` changed vs run-2 hashes (P1–P6/P8 identical).
- U+201C/U+201D/U+2019 zero-scan over 8 SVGs + text.md: **0/0/0** (D1 closed).
- text.md regenerated: 332 items, 26,447 B; new P1 sentence ×2, old phrase 0×.
- Print PDF: 45,262,615 B, SHA-256
  `8a586fdda6a20383649d0df37c13521630e70a1e72137e7ebef217a1a1fcf6a3`.
- Web PDF: 4,011,394 B (< 7 MB), SHA-256
  `cecc10999ac7987b2834b6cd7304e50e207a4d646938420234e44c1ecbbb27de`,
  50,748 text bytes.
- Builder gates (full table in GATE-LOG.md): freeze baseline 8/8; p8 extract
  150/150, compare CLEAN keydiff [137,138]; occlusion 0 flags (selftest OK);
  boxtitles 8/8 ≤ 386.5px; text layers print = web 50,748 B byte-identical;
  P8 min font 9.975pt both PDFs; print-vs-web pixel diff ≤ 0.47/page;
  P7 visual 300dpi crops confirm both fixed lines render correctly.
- Freeze diff vs core: added CJK 15 (was 7 in proof1) — all adjudicated in
  GATE-LOG.md: core-ko was rebuilt after proof1 (its own parallel fix),
  changing two stems; this edition's P1–P6/P8 are byte-identical to proofed
  run 2, so the deltas are core-side. Two stem divergences + the frame-example
  wording are flagged as observations for proof2/coordinator, NOT changed
  here (scope is D1+D2 only).
- Coordinator follow-up (2026-11-11): D2 must use the P1 sentence, never the
  P5 sentence — fix1 already used the P1 sentence; verified against core
  `content12.py:39` + core text.md:27; no change needed.
- No EDQUOT incident; freeze build copy deleted after use; note dir 5.9M.
- Status: fix1 complete, all builder gates green. Per SOP §8.4 the rebuilt
  edition awaits a fresh full independent proof round (proof2, coordinator
  to assign); this fix is NOT a定稿 claim.
