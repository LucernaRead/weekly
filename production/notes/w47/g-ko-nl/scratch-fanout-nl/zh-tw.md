# zh-tw (Traditional Chinese readers) — 2026-W47 nl fan-out

COMPLETE 2026-11-11 (build 1 final).

## Deliverables

- Print PDF `De-Lucerna-VOL4-nl-zh-tw.pdf`: 25,995,622 bytes,
  sha256 `a2a8652111933af15cec4aeb29fe7aa4f6885cccf42d8dc22392882be34c34cc`
  (CJK fonts embedded, like the core's 25,955,551 B)
- Web PDF `De-Lucerna-VOL4-nl-zh-tw-web.pdf`: 2,343,866 bytes,
  sha256 `daab1ef20d80cf58237db3f901e651bdfd66118091a85be5b0d955c1d2a929dc`
- `.text.md`: 44,126 bytes (142 single + 2 match headers + 8 match items = 150;
  8 golden, 6 gloss)
- `ABSTRACT.txt` (Traditional Chinese, one line, no ASCII double quotes) +
  `WEEKLY-KIT.md`

## Gates (build 1) — ALL PASS

occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, 0 key diffs; freeze
direct sha256 8/8; print/web text posdiff 0 msdiff 0 (8/8 pages); pdftotext
print 44,274 B / web 44,272 B; P8 answer-zone min font 10.12 pt; P8 chips =
core {A2: 8, B1: 24, B2: 3}; §1.1 SVG clean (off-palette {}, VOL.5 = 5 = core).

## Build

- `run.py` exit 0, TOTAL 150, zero OVERFLOW / TOO WIDE warnings.
- `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core).
- `flow[P8-keys] ended col 3/3 y=2441 (bottom 2560)` — 119 px margin, the most
  headroom of all editions, same shape as the core's 2457.
- `render.py` exit 0; `webpdf.py` exit 0.

## Visual — 8/8 clean

P1 numbers box fits col 1; P2 ZO ONTHOUD "口訣" fits, GEDICHT strip gloss
fits its box; P6 chart head fits; P7 BRIEVEN box ends at 1898, exactly as the
core; P8 answers 1–150 complete, pen photo in col 4.

## Fixes (explanation layer only; Dutch text, facts, keys untouched)

None — the only edition that needed no pre-fixes (subtitle 1504 px, numbers
title 367 px, items [2,2,2,2] total 384 px, P6 head 355 px, ZO ONTHOUD
307 px, agenda gloss 202 px, agenda sub-head 275 px, IN DEZE EDITIE head
296 px — all inside their limits at generation). No P1-headline overflow
(bridge 3 lines, ends 1411; box 384 px fits col 1: 1411 + 396 = 1807 ≤ 1828).
No P8-keys overflow (Traditional Chinese notes compact; flow ends 2441).

---

## Re-fanout (build 2, core fix2 5de7492f, 2026-11-11)

- SHAs: print `3a81e9cf00ff56378f692af8e951a4d306d0c68eae113332c8bede67d477eb9b`
  25,993,150 B; web `aedb0d6e80fdb95f3279dea8523b09e2130309f82e26fcf940559405cd1cced7`
  2,369,193 B; text.md `54d20ccd80af265c3ec62d2db0a08cbd1e7ecc559ea1bdc24557b449d293539e`
  44,315 B.
- run.py TOTAL 150, zero OVERFLOW/TOO WIDE. Gates ALL PASS: occlusion 0, p8
  150/150 CLEAN, freeze 8/8, print/web text posdiff 0 msdiff 0 all 8 pages
  (tokens 749/705/664/658/685/648/733/1676), pdftotext 44,323 B both, P8
  10.12pt spans 565, chips match, §1.1 clean.
- check_one ALL PASS (after fixing the check itself: D4-zh-tw-keeps-Chinese
  counted total `答案` = 168 vs want 150 — the extra 18 are instruction/header
  text, identical in the old build; the check now counts markers 142+8=150).
  D3 +71.9; D5 in P4 SVG + text.md; D4 142 `— 答案：` + 8 `(答案 x)`;
  italic print=web=1; terms 聖誕老人新聞 x8, 《荒島遠征》 x3, old terms 0.
  NOTE: the fixed exporter writes `— 答案： B` (space after ：, uniform with
  the other editions); the pre-fix2 export had no space. Diff vs backup is
  289 lines = 142 spacing pairs + term lines — all D4/D3/D5, no other content.
- Creambox: 3 flags, all pixel-probed 0 dark pixels → false positives
  (P2/P5 EN JIJ glosses, P6 chart caption). 0 true overflow.
- Horizontal box-title true-ink check (new): 56 titles ALL PASS, 0 FAIL.
- Visual: 8/8 clean (P1–P8 + crops P2-optc, P4-programma, P2-enjij,
  P6-voorteen, P7-hetwoord, P3-lone-period, P6-caption).
- KNOWN, not fixed (fix3 territory): P3 lone `。` (x=538, y=2280.22; core fix3
  D6 inherited, visually confirmed) + P6 chart-caption gloss `。` at line start
  (x=1462, y=659.44; NEW finding, same breaker class, still present in current
  core f567bcea — fix3 did not cover it; family-wide sweep: only zh-tw has
  orphan-。 lines, other 9 editions 0). P7 has no orphan (D7 did not reproduce
  here). Q140 key lacks `kort` (core-level, es only fixed per coordinator).
- Core HEAD built against: fix2 `5de7492f`. Core fix3 `f567bcea` landed during
  this rebuild; NOT included — separate incremental rebuild pending.
- KIT updated (Files delivered + Re-fanout §).
