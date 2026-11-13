# ko (Korean readers) — 2026-W47 nl fan-out

COMPLETE 2026-11-11 (build 1 final).

## Deliverables

- Print PDF `De-Lucerna-VOL4-nl-ko.pdf`: 17,281,555 bytes,
  sha256 `d72e53eb31c222fb3882b5644162a8292ec1a8ba0b3481b3b6099f98f710fed8`
- Web PDF `De-Lucerna-VOL4-nl-ko-web.pdf`: 1,884,427 bytes,
  sha256 `a5b50f5985fa7da5dd213ece619c21004c9a4d8698a7c331e5dca64aeecac119`
- `.text.md`: 47,383 bytes (142 single + 2 match headers + 8 match items = 150;
  8 golden, 6 gloss)
- `ABSTRACT.txt` (Korean, one line, no ASCII double quotes) + `WEEKLY-KIT.md`

## Gates (build 1) — ALL PASS

occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, 0 key diffs; freeze
direct sha256 8/8; print/web text posdiff 0 msdiff 0 (8/8 pages); pdftotext
print 47,558 B / web 47,557 B; P8 answer-zone min font 10.12 pt; P8 chips =
core {A2: 8, B1: 24, B2: 3}; §1.1 SVG clean (off-palette {}, VOL.5 = 5 = core).

## Build

- `run.py` exit 0, TOTAL 150, zero OVERFLOW / TOO WIDE warnings.
- `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core).
- `flow[P8-keys] ended col 3/3 y=2472 (bottom 2560)`.
- `render.py` exit 0; `webpdf.py` exit 0.

## Visual — 8/8 clean

P1 numbers box fits col 1; P2 ZO ONTHOUD "기억해요" fits, GEDICHT strip gloss
fits its box; P6 chart head fits; P7 BRIEVEN box ends above the ZINNEN rule
(g2 is 3 lines with a lower ly=1330); P8 answers 1–150 complete, pen photo in
col 4.

## Fixes (explanation layer only; Dutch text, facts, keys untouched)

1. Subtitle → 36 pt / spacing 11.5 (W46 ko). Numbers title → "이번 주 숫자".
   Numbers items shortened ([2,1,2,2]). P6 head kept "그래프(연습 데이터)".
   ZO ONTHOUD → "기억해요" (was 416 px).
2. P7 BRIEVEN glosses shortened (g1 2 lines; g2 3 lines, ly lowered to 1330;
   box ends 1927; VOL.5 kept).
3. No P1-headline overflow (bridge 3 lines, ends 1411; box 357 px fits col 1).
   No P8-keys overflow (Korean notes compact; flow ends 2472).

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 2)

Rebuilt from fixed core (D3 + D5 + D4 export + proof1 D7 fix). Build only, no commit/push. Logs: `scratch-refanout-nl/ko-{build,check,creambox}.log`, review `ko-review/`.

- D3 short form in P2, clearance +71.9px; D5 standings line in P4 box + text.md; D4 142 `— 정답：` + 8 `(정답 x)`, 答案 0; italic print=web=1.
- D7 (task item 5): P2 EN JIJ gloss reflowed by dropping `함께`; now 3 lines, last line ends `...편집부에 보내세요.` — period attached, no orphan `.` (verified visually on the P2 card).
- text.md diff vs build 1: exactly 5 lines (D3 2 + D5 1 + gloss 2).
- Gates: occlusion 0, p8 150/150 CLEAN, freeze 8/8, print/web text diff 0 (tokens 733/713/668/667/695/657/754/1639), pdftotext 47,613 B both, P8 10.12pt, spans 613, chips A2:8/B1:24/B2:3, §1.1 clean.
- Creambox: 3 CREAM-BOTTOM flags, all pixel-probed 0 dark pixels → false positives (descent allowance artifacts). 0 true overflow.
- Visual: 8/8 pages clean.
- Q140 recorded not fixed (key lacks `kort`; source has 작은 시) — coordinator scope: es only.

## Deliverables (re-fanout build 2, core HEAD `5de7492f`)

- Print PDF `De-Lucerna-VOL4-nl-ko.pdf`: 17,281,343 bytes (CJK fonts embedded),
  sha256 `aaeeba2cb7f59bb0e8d50d6614b09f3831c4ade3be3cff52f03d8f71e25113bd`
- Web PDF `De-Lucerna-VOL4-nl-ko-web.pdf`: 1,919,763 bytes,
  sha256 `ed38e32febf217635830d3d6a7d7fa4b0c52f5db37493f78ce4bb8a0204065d5`
- `2026-w47-nl-ko.text.md` (47,580 B), `ABSTRACT.txt`, `WEEKLY-KIT.md` (Re-fanout §)

Status: COMPLETE — all gates pass, 8/8 pages + 4 crops viewed clean. Core fix3 (D6/D7 orphan 。) NOT included — separate incremental rebuild pending.
