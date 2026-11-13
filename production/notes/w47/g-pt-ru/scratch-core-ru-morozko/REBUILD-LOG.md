# W47 core-ru P8 Morozko layout fix — PROBE LOG (probe A1, scratch only)

Date: 2026-11-11/12 UTC. Task: restore the P8 Morozko image + caption on core-ru,
lost to the `content8.py:131–140` conditional after the Medium spacing fix
grew the P8 keys flow. Probe only — NO production file touched, NO
commit/push/lint. text.md unchanged.

## 0. Preconditions verified

- `svglib.py` md5 at task start: `781059e6784b789c1179446e15b8f6ad` (Medium fix),
  verified in production `core-ru/` before any build.
- Wave-C numbers re-verified from the scratch rebuild logs + production SVGs:
  old production keys end col 3 y **2188.39** → Morozko placed, ends 2579.99;
  Medium-fix scratch keys end y **2216.58** (+28.19) → `P8 morozko SKIPPED`.
- ⚠️ **Second spacing fix landed MID-PROBE (see §6).** Production
  `svglib.py` was rewritten at 2026-11-12 00:00:33 UTC in ALL 11 ru dirs
  (new md5 `ee3211298f274e02ade2d4ca318ce354`). My probe copies were made
  23:56:17 UTC, BEFORE that write, and still carry the Medium-only md5
  `781059e6…` — so the probe below tests exactly the measurement state the
  task specified. Re-verification after wave C re-runs with the second fix
  is REQUIRED (see §6).

## 1. Geometry: what the numbers mean (measured, not assumed)

Page: 1950×2700 (`bslib4.py`: `PW, PH`). `CONTENT_BOTTOM = 2560` — soft
content guard. Footer: rule line at **y=2596**, footer text baseline 2624
(`BSPage4.foot`) — **2596 is the hard limit**; anything crossing it touches
the footer rule.

`content8.py:129–140` (core-ru, unchanged except the fix):
- `img_y = af.y + 24` — keys-end y + 24 gap. Old: 2188.39+24 = 2212.39;
  new: 2216.58+24 = **2240.58**.
- `img_h = 250` — image height (width fixed CW=422.5, `xMidYMid slice`).
- `+90` — caption allowance in the guard. **It is an UNDERESTIMATE.**
  Measured true caption height (from the old production P8 SVG):
  caption() = 24 gap + 2 lines × 19pt × 1.35 (= 51.30) + 2 gap +
  2 credit lines × 15.5pt × 1.30 (= 40.30) = **117.6**, not 90.
  Verified by wrap() with the NEW (Medium-fix) svglib: caption still wraps
  2 lines, credit still 2 lines → true height unchanged at 117.6.
- Guard `img_y + img_h + 90 < 2560` ⟺ keys end y < **2196**.
- Old build: 2212.39+250+90 = 2552.39 < 2560 ✓ placed; but TRUE caption end
  cy8 = **2579.99** — i.e. the shipped build ALREADY overruns CONTENT_BOTTOM
  by 19.99, ending 16.01 above the footer rule. 2560 is a soft guard the
  shipped paper violates; 2596 is the real edge.
- True-fit limit at img_h=250: keys end + 24 + 250 + 117.6 < 2596 ⟺ keys end
  < **2204.4**. The guard (2196) is 8.4 pts stricter than reality.

Consequence for candidate (b) — loosen the threshold alone: at the new keys
end 2216.58 with img_h=250, the true caption end would be
2240.58+250+117.6 = **2608.18 — 12.18 past the footer rule (2596)**. The
caption's last line box would cross the footer rule. **(b) alone is unsafe
at full height; REJECTED with proof.** (Note: it would only work for an
edition whose keys end is < 2204.4 — among ru editions, only ru-ja at
2203.08; out of scope, see §5.)

## 2. Chosen fix — probe A1 (ONE line, content8.py only)

```diff
--- production/2026-w47/core-ru/content8.py
+++ (probe copy only)
@@ -130,7 +130,7 @@
 img_y = af.y + 24
-img_h = 250
+img_h = 200
 if af.ci == 3 and img_y + img_h + 90 < 2560:
```

Conditional, `+90`, threshold, caption code, `bslib4.py`, `svglib.py`,
text.md — all untouched. Core-ru only; no shared-renderer change.

Predicted geometry at new keys end 2216.58:
- Guard: 2240.58 + 200 + 90 = **2530.58 < 2560, slack 29.42**.
- Image: 2240.58–2440.58. True caption end: 2440.58 + 117.6 = **2558.18**.
- **Margins (for the wave-C re-run):**
  - vs skip threshold (image disappears): **29.42 pts** of further keys
    growth (~2 key lines at 14.69 each) before the skip trips again.
  - vs CONTENT_BOTTOM 2560 (soft): **1.82 pts** — nearly zero; ANY further
    keys growth pushes the caption past 2560, exactly as the OLD shipped
    build already was (2579.99). Passing 2560 is not a failure per se.
  - vs footer rule 2596 (hard): **37.82 pts** — the caption stays clear of
    the footer until keys grow another 37.82.
- Image cost: height −20% (250→200). Slice crop: portrait 906×1129 shown at
  422.5 wide → scale set by width; visible vertical fraction 47.5% → 38%.
  No distortion (slice, not stretch). Visual check in §4: both figures
  remain fully in frame.
- Considered alternative (computed, NOT built): img_h=221 matches the old
  shipped caption-end envelope (true end 2579.18 ≈ old 2579.99) but leaves
  only 8.42 guard slack and still ends past 2560 — thinner on every margin
  than 200, for 21 pts of image height. Rejected. Stricter variant if the
  re-run wants 2560 headroom: img_h=195 (true end 2553.18, 6.82 inside 2560,
  guard slack 24.42) — not probed; 200 already passes every hard gate.

## 3. Probe method

Scratch dir:
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-core-ru-morozko/`
- `production-before.sha256` — 45-file SHA-256 of production core-ru before.
- `probe-a1/` — `run_build.py --dry-run` copy of production core-ru
  (verified byte-identical `content8.py` first), then the one-line patch.
- `probe-a1-run/` — `run_build.py --build <patched copy> --steps run,render`
  output (`build-copy/` holds SVGs + print PDF; web PDF built with
  `tools/webpdf.py` on the scratch svg dir).
- Production integrity: re-hashed after — 44/45 files identical; the ONLY
  diff is `svglib.py`, rewritten by the second-fix worker at 00:00:33 UTC
  (§6), not by this probe. No production file was written by me.

Build result (`probe-a1-run/run-build.log`):
- `P8 keys end col 3 y 2216.5800000000017` (unchanged — keys unaffected)
- `P8 morozko ends 2558.180000000002` — exactly the predicted 2558.18
- `TOTAL 150`, run.py exit 0, render.py exit 0
- Print PDF 31,427,603 B (old production 31,429,147; −1,544);
  web PDF 4,024,331 B (old 4,025,900; −1,569), 56,083 text bytes.

## 4. Probe gates — ALL PASS (first attempt; no failed candidate)

| Gate | Result |
|---|---|
| Morozko image + caption on P8 | YES. SVG `<image x=1439.5 y=2240.58 w=422.5 h=200>`; caption baselines 2464.58 / 2490.23 (19pt), credit 2517.88 / 2538.03 (15.5pt); all caption words present incl. `Морозко` / `Билибина` / `(Wikimedia Commons)`; `cy8` 2558.18 |
| P8 images back to 6 | YES. Print PDF per-page images `[1,1,0,1,1,0,1,1]` total 6 (P8=1); web PDF identical; old production identical |
| p8 extract | **150/150** |
| p8 compare vs old baseline | **CLEAN, keydiff []** (`scratch-ru-rebuild-C/core-ru/p8-baseline.svg`) |
| check_core | rc=0: golden BAD 0, gloss 0, orphans 5 (same P7 set as KIT), collisions **0**; P8 SVG text chars 8193 (old 8191 — SVG `<text>` segmentation only; PDF text layer proves 0 char diff, see below) |
| occlusion_audit | **0 flags** (selftest OK: all planted classes fired) |
| freeze diff vs Medium-fix scratch build | P1–P7 **+0/−0 strings**; P8 **+32/−0** — every added string is a Morozko caption/credit word or punctuation; added Latin 1 = `(Wikimedia Commons)` (restored credit line, present in old build); CJK totals unchanged all pages |
| freeze diff vs OLD production | Only space/punct re-segmentation; **0 Cyrillic-bearing strings removed or added on any page**; CJK totals unchanged all pages |
| print/web text layers | Multiset identical overall + per page (8/8), raw text byte-identical; 25,934 chars both |
| probe vs OLD print text | **0 OLD-only, 0 probe-only** chars (25,934 = 25,934) |
| census print = web | **12 JOIN verdicts, byte-identical set to wave-C Medium build** (11 second-class + `ГЛАГОЛЫИ` artifact 2.62pt, identical gaps); byline 2.89/2.82, prof 4.39/3.48/3.67/3.95 — the layout fix changes nothing about spacing. The second-class blocker stays with the second-fix worker |
| text.md | Byte-identical to production (both `.text.md` files) |
| Visual (CairoSVG render of P8, Morozko region) | Morozko figure (hat, beard, fur coat, staff) + girl in red headscarf fully in frame; composition reads the same as the old h=250 crop, slightly tighter top/bottom; caption 2 lines + credit 2 lines legible, clear of the footer rule; 24-pt gap between last key line and image top, no overlap. (Old render shows the pre-existing fused `Зимняясказка` / `достояние(Wikimedia` joins; probe render shows them correctly spaced.) |

No probe attempt failed: A1 (img_h=200) passed every gate on the first
build, so no second candidate was built. The 221 alternative was evaluated
by computation only (§2).

## 5. Blast radius — the other 10 ru editions (production SVGs + print PDFs, read-only)

Method: keys-end y from production `svg/p8-test.svg` — image y − 24 when
placed; else last key-line baseline in col 4 + 15.19 (13.0pt × 1.13 + 0.5
gap). Validated EXACTLY against known log values: ru-ko 2231.27,
core-ru / ru-zh-tw 2188.39 (all to 2 decimals). Cross-checked with print-PDF
P8 image counts (placed = 1, skipped = 0). Threshold: keys end < 2196
(guard); true-fit limit at h=250 is < 2204.4. Margin = 2196 − keys end
(positive = headroom before the skip trips).

| Edition | P8 keys end y | Margin vs 2196 | Morozko in production? | Print images total (P8) |
|---|---|---|---|---|
| core-ru (ref) | 2188.39 | **+7.61** | placed | 6 (1) |
| ru-zh-tw | 2188.39 | **+7.61** | placed (Medium-fix rebuild: unchanged 2188.39, survives) | 6 (1) |
| ru-ja | 2203.08 | −7.08 | SKIPPED (only edition inside the true-fit limit 2204.4 — a threshold-only fix would restore it) | 5 (0) |
| ru-ko | 2231.27 | −35.27 | SKIPPED (Medium-fix rebuild: unchanged 2231.27, never had it) | 5 (0) |
| ru-en | 2288.84 | −92.84 | SKIPPED | 5 (0) |
| ru-fr | 2317.03 | −121.03 | SKIPPED | 5 (0) |
| ru-pt | 2317.03 | −121.03 | SKIPPED | 5 (0) |
| ru-de | 2331.72 | −135.72 | SKIPPED | 5 (0) |
| ru-es | 2331.72 | −135.72 | SKIPPED | 5 (0) |
| ru-it | 2331.72 | −135.72 | SKIPPED | 5 (0) |
| ru-nl | 2389.29 | −193.29 | SKIPPED | 5 (0) |

Findings:
- **9 of 10 ru editions ALREADY ship P8 without Morozko in production.**
  The skip is the norm for ru, not the exception — only core-ru and
  ru-zh-tw (both at 2188.39, margin +7.61) have it. Nothing in this probe
  changes that; restoring the other 9 needs per-edition layout decisions
  (out of scope, not attempted, not rebuilt).
- **ru-zh-tw is the at-risk survivor:** margin only +7.61. Any further keys
  growth > 7.61 (e.g. from the second fix, if it reflows anything) trips
  its skip too. The Medium fix grew its keys by 0.00, but the second fix
  is unmeasured yet.
- Production keys-end values above are under the OLD measurement. Medium-fix
  deltas known: core-ru +28.19, ru-ko +0.00, ru-zh-tw +0.00 — growth is
  edition-specific (depends on which key lines re-wrap), so the other 8
  editions' post-fix keys-end values are unknown until wave C re-runs.
  Any edition within ~30 pts of the threshold should be treated as
  at-risk-after-fix; on current numbers that is only ru-ja (−7.08) and
  ru-zh-tw (+7.61) — the rest are already far past it.
- All 10 editions share the identical conditional (`img_h=250`, `+90`,
  `<2560`, `content8.py:131–140`); ru-zh-cn has no production dir in this
  clone (its text.md lives inside core-ru, byte-identical to core-ru's).

## 6. Second-fix landing — what changed under this probe, and what must be re-verified

- At 2026-11-12 00:00:33 UTC, while the probe build was running, the
  second-fix worker rewrote `svglib.py` in ALL 11 ru dirs (md5
  `781059e6…` → `ee3211298f274e02ade2d4ca318ce354`). The new code adds
  `_run_w` (unkerned run measurement, sum of single-char advances), used
  ONLY inside `Page.text` for run placement; its own comment states
  "text_w/wrap keep the kerned getlength, so line-breaking is byte-identical
  to the shipped layout (no reflow anywhere)".
- My probe is unaffected in validity: both probe copies carry the
  Medium-only svglib (md5 verified `781059e6…` in `probe-a1/build-copy`
  and `probe-a1-run/build-copy`), and every number in §§1–4 was produced
  under it.
- **Re-verification required when wave C re-runs with the second fix:**
  (1) confirm keys-end y is still 2216.58 (the fix claims no reflow —
  unverified until the re-run); (2) re-run the §4 gates on the rebuilt
  output; (3) check the re-run's census (the 11 second-class joins should
  clear). If keys-end moves, judge against the §2 margins: skip trips at
  +29.42 growth, footer-rule crossing at +37.82; the 1.82 soft-guard
  margin vs 2560 will go first and is not a failure by the shipped
  build's own standard (old caption ended 2579.99).
- The `production-before.sha256` snapshot in this dir predates the
  second-fix write; its only diff vs post-probe production is that one
  file, changed by the other worker.

## 7. Disposition

- RECOMMENDED FIX (for the wave-C re-run to apply + re-verify, NOT applied
  to production here): `core-ru/content8.py:133`, `img_h = 250` → `img_h =
  200`. One line, core-ru only.
- Production untouched (except the second-fix worker's own `svglib.py`
  write, §6). No sync, no KIT edit, no commit/push/lint.
- Scratch kept at:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-core-ru-morozko/`
  (`probe-a1/` patched source copy, `probe-a1-run/` built outputs +
  `run-build.log`, gate JSONs, `freeze-diff-*.json`, `census-*-probe.json`,
  `p8-*.json`, `occlusion-probe.json`, `production-before.sha256`).
