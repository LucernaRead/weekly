# FIX-LOG — core-nl fix rounds 2–5 (2026-11-11)

## Fix round 5 — D11 P4 HET PROGRAMMA box last line spills below the box (2026-11-11)

Handover: fix5 agent cd9d373a was drained mid-run by a runtime
restart. Its source edit was already on disk (`content34.py:134`,
62 → 89 + comment) but its build log was empty (0 bytes) and no
gates had run. This agent (nl5b) took over from that breakpoint:
verified the edit independently from first principles before keeping
it, and re-ran the full build + gate suite from scratch. Nothing of
the previous agent's work was taken on trust.

Scope: D11 only, core-nl only, no fan-out rebuild, no commit, no
push. Pre-work probes passed first (`/dev/null` present;
`git hash-object -w` OK in-repo; goals-side probe file written).
Pre-fix SHA check against the fix4 final state: print
`2c7f2c6f…ecd3c` / 25,955,580 B, web `434626f5…53df5` /
2,103,990 B, text.md `0b97a48d…7050c` / 44,093 B — all three matched
disk exactly. The previous agent's partial run was also detected:
`svg/p1–p7` mtimes 15:25:44–15:26:21 UTC, `svg/p8` still 14:52:57
(re-proof's run) — the drain hit between `content7.py` and
`content8.py`. Pre-build hash check: only `p4-sport.svg` differed
from its baseline snapshot, the other 7 byte-identical to fix4.

### D11 — P4 HET PROGRAMMA box last line outside the box

- **Evidence (pre-fix, re-proof §6, re-verified on disk):** P4 col3
  cream box `<rect x="1439.5" y="591.6" width="422.5"
  height="611.0">`, bottom 1202.6; last line `18:45 uur.`
  (`<text x="1461.5" y="1209.49" font-size="21.5">`), baseline
  +6.89px below the box bottom, true ink +6.4px. Pre-existing
  (fix2's D5 added the 5th fact; fix2 FIX-LOG's "line inside the
  box" does not match measurement).
- **Root cause (independently re-derived, `verify-d11.py`):**
  `Page.para` puts the first baseline exactly at its `y` and
  advances `21.5 × 1.42 = 30.53`/line. The render loop reaches the
  first fact baseline at box-top + 16 (pad) + 52 (title block) + 21
  (para y-offset) = **89px**, but the height formula reserved only
  62px at the top — 27px short. Five facts wrap 3/3/3/2/3 = 14 lines
  (real `wrap()`); simulated baselines 680.60 … 1148.43 / 1178.96 /
  **1209.49**; last-baseline offset from box top **617.89**.
  Old `sh = 62 + Σ(n·30.5+12) + 32 + 30 = 611`; new
  `sh = 89 + 487 + 62 = 638`. True ink of `18:45 uur.` ends 0.75px
  above its baseline (PIL 4× Newsreader mask; no descenders), so
  old ink margin was −6.14px and new is +20.86px.
- **Fix (only `content34.py:130–134`, kept from the previous
  agent after verification):** top reserve 62 → 89; nothing else
  in the formula changed (the 30.5 vs true 30.53 under-counts by
  0.42px over 14 lines, absorbed by the 20.11px margin — left as
  is, minimal change). Box bottom 1202.6 → **1229.6**; last-baseline
  margin **+20.11px**; `P4 col3 ends 1229.6`; exercises hline at
  y=1608, clearance 378.40px. P3's same-shape box cross-checked
  (tail 64): margin +16.20px, no spill.
- **Re-measurement (rebuilt SVG + renders):** box bottom 1229.6,
  last baseline 1209.49 (+20.11px); true ink lowest row y=1209.00
  (cards 1×) / 1209.12 (print PDF 150dpi), margins +20.60/+20.48px;
  7px strip below the box bottom: **0** non-paper pixels on both
  renders. 150dpi crop `render/crop-p4-programma.png` confirms by
  eye: `18:45 uur.` inside the cream box with clear margin below.

### Spill sweep — full week (the creambox blind spot)

Re-proof's `spill_sweep_reproof.py` (copied, logic unchanged):
every cream box, texts 0–60px below/above/outside it. `check_creambox.py`
skips whole lines whose baseline is outside the rect, and occlusion
BOXTITLE only counts stroked boxes — this sweep covers both gaps.
**Result: 0 spills on all 8 pages.** The P4 box has no below hit at
all; the nearest BELOW hit anywhere is +24px (`HET WOORD VAN DE
WEEK`, next section head). Other BELOW hits (+32/+44/+50.5/+60px)
are all independent blocks (quiz instruction, footer note, gloss
box, section heads), adjudicated in the scratch FIX-LOG. ABOVE/SIDE
hits are captions/credits and neighbouring boxes' own titles.
**Tool debt: this sweep must be added to the standing pre-insert
gates** — it is the only check that can see a whole line outside a
fill-only box.

### D8 / D9 / D10 regression (fix4's fixes intact)

- D8: P6 caption lines `…非真实调查。` (635.02) /
  `问题：你在鞋里放什么？（100 名年轻人）` (659.44), 2 lines,
  baselines unchanged; crop confirms 。 at line-1 end.
- D9: Q140 three-way MATCH (registry = text.md:416 = P8 node,
  `…met een kort gedicht.`); crop confirms printed.
- D10: P7 letters lines `…最佳作文，` (1754.27) /
  `刊登示例信，承诺顺延 VOL.5。` (1782.67), 2 lines, baselines
  unchanged; crop confirms ， at line-1 end.
- p6/p7/p8 SVGs byte-identical to fix4, so no regression by
  construction; the checks above confirm it on rebuilt output.

### D5 font (record only, not fixed)

Same script as re-proof: font totals Noto Sans CJK SC 619 /
Newsreader 1215 / Noto Serif CJK SC 305 / UnifrakturMaguntia 1;
pure-Latin-on-CJK segments per page 38/23/30/29/29/26/18/52 =
**245** — identical to re-proof. Recorded, not fixed, not a gate.

### Fix-round-5 gates (final build, 2026-11-11)

- Build: `run.py` exit 0, TOTAL 150, by page 10/18/18/18/18/18/12/38,
  A2 46 / B1 73 / B2 31; `render.py` exit 0 (twice, byte-identical);
  zero FLOW OVERFLOW / HEAD TOO WIDE warnings. SVG hashes: **only
  `p4-sport.svg` changed** vs fix4 (`c82c9a3c…` → `6e05d5a0…`,
  byte-identical to the previous agent's partial-run p4); the other
  7 are byte-identical.
- `occlusion_audit.py svg/`: selftest OK, **0 flags** (incl.
  BOXTITLE 0).
- Creambox: same 3 CREAM-BOTTOM flags (P2/P5/P6, ≤1.6px); 7px strip
  below each box bottom: **0** non-paper pixels; true-ink clearances
  +3.4/+3.5/+3.6px. P4 now 0 flags. **True overflow 0.**
- Spill sweep: **0 spills** (§ above).
- `p8.py extract --total 150`: noted set **150/150**.
- P8 keys vs text.md vs registry (re-proof `p8compare_reproof.py`,
  verbatim file `p8-compare-fix5b.json`): **149/149 three-way MATCH**
  (DIFF 0, MISSING 0); #150 open-writing exception (P8 key `✓`,
  text.md 81-word Tekstmodel). Match keys: 25–28 = d/c/a/b,
  141–144 = b/c/d/a.
- Orphan sweep (re-proof script, PIL + svglib + brute force):
  1421 lines; (a)=**0**/(b)=**0** both methods, all pages; brute
  force 12 closer-leading fragments, leftmost **0**.
- Freeze (clean-dir re-run of `run.py`): **8/8 MATCH**.
- P8 answer font size (PyMuPDF): min = **10.12pt** ≥ 10pt.
- Web vs print text layer (PyMuPDF, 0.1pt): multiset diff **0** all
  8 pages; positional diff only P1's 2 tokens (`De`/`Lucerna`,
  x 394.0 vs 393.8 — the known 0.2pt font-subset micro-shift, same
  as re-proof). pdftotext: print 44,197 = web 44,197 = scratch
  re-render 44,197 B, byte-identical. Delivered web (2,104,000 B)
  vs scratch re-render (2,103,997 B, −3 B): single differing region
  is one font-subset stream (obj 20, Length 2174 vs 2173) —
  fontTools subsetting is non-deterministic run to run; text layer
  identical, not a defect.
- D3 regression (PIL true ink, 4× draw + getbbox method): P2 right
  a +98.2 / b +46.0 / c +72.2 / d +55.8; left 25–28 +272.8/+280.2/
  +200.0/+259.2 (within ~1.5px of re-proof's `font.getbbox` values;
  the gap is the render method, all far inside edge 1862). Quote
  sweep: ASCII `"` 0, backtick 0, `« »` 35/35, `“ ”` 1/1, md same.
  Golden lines 8/8 verbatim; Q150 model 81 words by direct count
  of text.md:432 (the gates script's regex fallback reports 110 —
  it grabs the wrong paragraph, same miscount re-proof noted).
- Core text.md re-export (`export47.py`, exit 0): **44,093 bytes,
  byte-identical to fix4** (`0b97a48d…7050c`); 432 lines;
  142 + 2 + 8 = 150 exercises; 8 golden lines; 6 gloss lines.
- Visual: print PDF 150dpi `render/p-1..p-8.png`, all 8 pages
  viewed, no new defect; crops `crop-p4-programma.png` (D11),
  `crop-p6-d8.png`, `crop-p7-d10.png`, `crop-p8-q140.png` all
  confirmed by eye.

## New SHAs (lowercase) + bytes — fix round 5

- Print PDF `De-Lucerna-VOL4.pdf`:
  `b7d4a9cddbc38dd56ddd22cd2ae15a2e04ba1988670b6cf384eafbc66bd7ce47`
  (25,955,578 bytes)
- Web PDF `De-Lucerna-VOL4-web.pdf`:
  `5a47449cdff7d5847aee81c1c5b0f1af54cfeda873c5b55058a6d18f0e10404c`
  (2,104,000 bytes)
- Core text.md `2026-w47-nl-zh-cn.text.md`:
  `0b97a48dc248c9cf3dc28f21b55e06a1e0dc7dea7db5f6e46e55f2f2fed7050c`
  (44,093 bytes — **unchanged from fix4**)

## Files changed (this round, NOT committed)

Per the repo rule, only sources + text.md + docs would be committed.
This round changed: `content34.py` (D11, one hunk, written by the
previous fix5 agent and independently verified + kept by this
agent), `WEEKLY-KIT.md` (§16), `FIX-LOG.md` (this file).
`2026-w47-nl-zh-cn.text.md` was re-exported in place but is
byte-identical, so it carries no change. Unchanged, not in this
round: `bslib4.py`, `content12.py`, `content56.py`, `content7.py`,
`content8.py`. Rebuilt on disk, NOT committed (render cache):
`svg/p4-sport.svg` (other 7 SVGs byte-identical to the fix4 build),
`cards/*.png`, `De-Lucerna-VOL4.pdf`, `De-Lucerna-VOL4-web.pdf`.
Fan-out text.md/PDFs NOT rebuilt in this round — coordinator's fix5
incremental rebuild.

Not committed (goals-side scratch):
`hidden_files/w47/scratch-fix-nl5b/` (logs, measurements, renders,
gates, `p8-compare-fix5b.json`, `orphan-sweep-fix5b.json`, crops;
`export47.py` + `stub_bslib47.py` copies of the fix4 exporter;
re-proof gate scripts copied with scratch path repointed).
Read-only source reused from `scratch-fix-nl5/`:
`svg-hashes-before.txt`, `text-before-fix5.md` (nothing written
there).

---

## Fix round 4 — D8 line-initial 。 (P6) + D9 Q140 missing kort + D10 line-initial ， (P7, found by the improved sweep) (2026-11-11)

Scope as tasked: D8 + D9 only, core-nl only, no fan-out rebuild, no
commit, no push. Pre-work probes passed first (`/dev/null` present;
`git hash-object -w --stdin` OK; goals-side probe file written).
Pre-fix SHA check against the fix3定稿: print
`82427d3f…b9eb7` / 25,955,581 B, web `44553e5c…cd5a39` /
2,103,999 B, text.md `2f2a650b…b25d92e` / 44,088 B — all three matched
disk exactly (HEAD `f567bcea` fix3) before any edit.

One scope note: the task named two source files (D8 → `content56.py`,
D9 → `content8.py`). The improved orphan sweep the task itself
requires (both classes, 0/0) surfaced a third defect of the same class
on P7 (D10, pre-existing — P7 SVG byte-identical fix3→fix4 before the
fix). Meeting the (b)=0 gate required fixing it, so a third source
file (`content7.py`) was changed; the reason and the evidence are
recorded under D10 below. Nothing else was touched.

### D8 — P6 caption line-initial 。 (chart caption, col 3)

- **Evidence (pre-fix, verified on disk):** `svg/p6-verdieping.svg`:
  `练习数据：虚构数字，仅供练习，非真实调查` (x=1461.5, y=635.02,
  18.5px), then `。问题：你在鞋里放什么？（100 名年轻人）` (x=1461.5,
  y=659.44) — the 。 closing the first sentence sits at the start of
  the second line. Source: `content56.py:143` `capcn`, rendered by
  `p.para(..., CW - 44, 1.32)`.
- **Root cause:** greedy `wrap()` at 378.5px: line 1 measures 370.0px,
  adding the full-width 。 (18.5px) would make 388.5px > 378.5px, so
  the 。 wraps to line 2. Fix3's sweep only checked lone 。 on its own
  line, so this line-initial case was missed.
- **Fix:** `content56.py`: new `capcn_w = CW - 25` (397.5px), used in
  BOTH the box-height computation (`len(wrap(capcn, ..., capcn_w))`)
  and the `p.para` call. Width scan (sans 18.5): band 388.5–406.5px
  wraps to the same 2 lines with 。 at the end of line 1;
  397.5px is the band middle (9px from each edge). Direction note:
  fix3 narrowed; here narrowing cannot keep 2 lines — every width
  that clears the orphan forces 3 lines (+26px box growth, downstream
  shift). Widening literally puts 。 back at the end of line 1, keeps
  2 lines, box height unchanged, zero y shift. Line 1 ends at
  ix+22+388.5 = 1850.0, 12px inside the box right edge (1862.0);
  the creambox CREAM-RIGHT threshold (edge − 8 = 1854) still clears
  by 4px. No wording, key, or fact changed.
- **Re-measurement (rebuilt SVG):** lines are
  `['练习数据：虚构数字，仅供练习，非真实调查。', '问题：你在鞋里放什么？（100 名年轻人）']`;
  baselines unchanged (635.02 / 659.44); `P6 chart ends 665`,
  `P6 col3 ends 1000.0` — identical to the fix3 build. Card crop
  `scratch-fix-nl4/crop-p6-fixed.png` confirms visually.

### D9 — Q140 answer missing kort

- **Evidence (pre-fix, verified on disk):** core text.md:416:
  `140. [B2 · 翻译] 我做一个带小诗的伪装礼物。→ ___ — 答案：Ik maak een surprise met een gedicht.（surprise 是固定搭配）`.
  The stem says 带小诗 ("with a small poem"); the Dutch source
  sentence (text.md:73) says `Twee: schrijf een gedicht — kort is ook
  goed.` The answer dropped `kort`.
- **Fix (only `content8.py:75`):** registry key
  `Ik maak een surprise met een gedicht.` →
  `Ik maak een surprise met een kort gedicht.` ("只补 kort"). The
  note `surprise 是固定搭配` is unchanged: it stays true of the new
  answer, and `kort` is already glossed by the stem itself (带小诗)
  and by text.md:73 (`kort is ook goed`), so no note change was
  needed. NOT copied from the nl-es edition (which fixed the same
  item independently as `... kort gedicht.（…; corto = kort）`) — the
  core fix was made from the core source alone.
- **Three-source consistency (rebuilt + re-exported):** registry key,
  text.md:416 answer, and P8 SVG answer node all read
  `Ik maak een surprise met een kort gedicht.` — see
  `p8-compare-fix4.json` entry 140 (MATCH). The other 149 keys are
  untouched: only line 75 of `content8.py` changed, and the 3-way
  compare shows all 149 non-150 questions MATCH (see gates).

### D10 — P7 line-initial ， (readers'-letters box, col 3) — found by this round's improved sweep

- **Evidence (pre-fix, verified on disk):** `svg/p7-taal.svg`
  (byte-identical to fix3 — pre-existing, not introduced by fix4):
  `截稿时未收到真实来信或第 8 版最佳作文` (x=1461.5, y=1754.27,
  20px), then `，刊登示例信，承诺顺延 VOL.5。` (x=1461.5,
  y=1782.67). Source: `content7.py:91` `dt_zh`, rendered by
  `p.para(..., CW - 44, 1.42)`. Found by the class-(b) sweep on the
  D8+D9 build (the only (b) hit on all 8 pages).
- **Root cause:** same as D8 — `wrap()` at 378.5px: line 1 measures
  360.06px, adding ， (20px) would make 380.06px > 378.5px.
- **Fix:** `content7.py`: new `dt_zh_w = CW - 32` (390.5px), used in
  BOTH the `lh` height computation and the `p.para` call. Width scan
  (sans 20): band 380.5–400.0px wraps to the same 2 lines with ， at
  the end of line 1; 390.5px is the band middle (10px from the lower
  edge, 9.5px from the upper). Narrowing was considered and rejected:
  ~350–360px also clears it in 2 lines but splits 作文 across lines
  （最佳作 / 文，…); widening keeps 作文 whole and the ， at line-1
  end. 2 lines kept, box height unchanged, zero y shift. Line 1 ends
  at bx+22+380.06 = 1841.6, 20px inside the box right edge (1862.0).
  No wording, key, or fact changed.
- **Re-measurement (rebuilt SVG):** lines are
  `['截稿时未收到真实来信或第 8 版最佳作文，', '刊登示例信，承诺顺延 VOL.5。']`;
  baselines unchanged (1754.27 / 1782.67); `P7 col3 ends 1898.0` —
  identical to the fix3 build. Card crop
  `scratch-fix-nl4/crop-p7-fixed.png` confirms visually.

### Full-edition orphan-punctuation sweep (rebuilt SVGs, all 8 pages, both classes)

Method: `<text>` elements grouped by baseline y and split into line
segments on x-gaps > 60px (separate columns/blocks), with the
D1-fix leading-space elements concatenated before checking —
plus an independent brute-force cross-check over every `<text>`
element (any element starting with a closer, adjudicated by whether
it is leftmost on its baseline):

- Class (a) lone `。` owning its whole line: **0** on all 8 pages.
- Class (b) line-initial `。/，/、/：/；/！/？/` or closing quote
  (`” ’ 」 』 ） 》 »`): **0** on all 8 pages (final build).
  Pre-D10 sweep on the D8+D9 build found exactly 1: the P7 ， above.
  The cross-check lists 11 mid-line run fragments starting with a
  closer (P1 `：柏林奥林匹克`; P8's 4 `：` and 7 `）` answer-zone
  inline locators) — none is leftmost on its baseline, all excluded,
  same as the fix3/proof2 treatment of the P8 locators.

### D5 font (record only, not fixed)

Per the task instruction and the proof3 note (§4, "全周级已知待定项，
只记录"): Latin-only text segments landing on CJK fonts. Fix4 recount
on the final SVGs (method: SVG `<text>` elements whose stripped
content contains `[A-Za-z]` and no CJK-range character):
font totals Noto Sans CJK SC 619 / Newsreader 1215 / Noto Serif CJK SC
305 / UnifrakturMaguntia 1; pure-Latin-on-CJK segments per page
37/18/24/24/24/21/14/44 = **206**. (Proof3 recorded 245 with a method
not preserved as a script in `scratch-proof-core-nl3`, so the two
counts are not directly comparable; the item stays a week-wide known
pending item, recorded, not fixed, not a gate.)

### Fix-round-4 gates (final build, 2026-11-11)

- Build: `run.py` exit 0, TOTAL 150, by page 10/18/18/18/18/18/12/38,
  A2 46 / B1 73 / B2 31; `render.py` exit 0 (venv python — system
  python3 has no cairosvg; repo AGENTS.md mandates
  `tools/venv/bin/python`), zero FLOW OVERFLOW / HEAD TOO WIDE
  warnings. SVG hashes: only `p6-verdieping.svg`, `p7-taal.svg`,
  `p8-toets.svg` changed vs fix3; the other 5 are byte-identical.
- `occlusion_audit.py svg/`: selftest OK, **0 flags** (incl. the
  BOXTITLE class: 0 boxtitle overflow).
- Creambox check (fix3's `check_creambox.py`, re-run): same 3
  CREAM-BOTTOM flags (P2 y=1383.36 / P5 y=932.05 / P6 y=659.44, all
  ≤1.6px); 7px strip below each box bottom probed pixel by pixel on
  the rebuilt card PNGs: **0 non-paper pixels** — all three are the
  known false positives (Latin 0.3×size descender allowance on
  CJK-only last lines), same as proof2/fix3. True-ink clearances
  +3.4 / +3.5 / +3.6px. **True overflow 0.**
- `p8.py extract --p8 svg/p8-toets.svg --total 150`: noted set
  **150/150**.
- P8 keys vs text.md vs registry (new `p8compare_fix4.py`, verbatim
  per-question file `p8-compare-fix4.json`, 150 entries): **149/149
  three-way MATCH** (DIFF 0, MISSING 0); the only non-match is #150,
  the open-writing exception (P8 key `✓`, text.md carries the 81-word
  Tekstmodel, registry key is the open-writing placeholder). Match
  keys re-confirmed: 25–28 = d/c/a/b, 141–144 = b/c/d/a. This
  supersedes the fix3 compare, whose 8 "mismatches" were a parser
  artifact (match-item answers on range-header lines); the fix4
  parser reads the match-item lines directly, so all 150 are now
  covered by the mechanical compare. Q140 hand-verified on top:
  stem （带小诗） + text.md:73 (`kort is ook goed`) + new answer all
  agree; the other 149 keys are byte-identical to the proof3
  hand-verified set (150/150 PASS there), and their source lines are
  untouched in this round.
- Freeze (direct sha256, clean-dir re-run of `run.py`): **8/8 MATCH**.
- P8 answer font size (PyMuPDF): min = **10.12pt** ≥ 9.75pt floor.
- Web vs print text layer (PyMuPDF position-sorted): all 8 pages
  positional diff 0, multiset diff 0 (tokens 760/715/673/671/700/659/
  738/1686 = 6,521; P8 is +1 vs fix3's 1685 — the added `kort`).
  pdftotext: print 44,197 bytes, web 44,197 bytes (byte-identical;
  the +5 `kort ` bytes are offset by blank-line reflow in pdftotext's
  P8 block order — the token comparison above is authoritative).
  Print-text diff vs fix3 shows exactly the D8 reflow (2 lines), the
  D9 `kort` line, and pdftotext reading-order shuffling of the same
  P8 key lines (139/141–144/146–147/102, content unchanged).
- D3 regression re-measured (`step3_gates_fix4.py`, fix3's script with
  two of its bugs fixed — the `noted_set` key and the golden-lines
  `re.findall` on a list): P2 D-option true-ink clearances identical
  to fix3 (c +71.5, a +97.5, b +44.5, d +55.5; left 25–28
  +278.5/+285.5/+208.5/+265.5). Quote sweep: ASCII `"` 0, backtick 0,
  `« »` paired on P1/P2/P7/P8, `“ ”` only the P1 pair. Golden lines
  8/8 verbatim in body; Q150 model 81 words (80 excluding the
  standalone `–`), within 80–100.
- Core text.md re-export (`export47.py`, exit 0): 44,093 bytes
  (was 44,088, +5 = `kort `), **diff vs fix3 is exactly line 416**;
  432 lines; 142 + 2 + 8 = 150 exercises; 8 golden lines; 6 gloss
  lines. (Re-export re-run after D10 as well: byte-identical — D10
  changes no text content.)
- Visual: card crops `crop-p6-fixed.png` (caption 。 back at line-1
  end), `crop-p7-fixed.png` (， back at line-1 end),
  `crop-p8-q140.png` (`140. Ik maak een surprise met een kort
  gedicht. — surprise 是固定搭配`) all confirmed by eye.

## New SHAs (lowercase) + bytes — fix round 4

- Print PDF `De-Lucerna-VOL4.pdf`:
  `2c7f2c6fb3c443fa32a6055bfa4a368f11a761c75de0995b776204510a7ecd3c`
  (25,955,580 bytes)
- Web PDF `De-Lucerna-VOL4-web.pdf`:
  `434626f58b605b8ba0878b7d52de32e8255f2ad43489e133e602faef49853df5`
  (2,103,990 bytes)
- Core text.md `2026-w47-nl-zh-cn.text.md`:
  `0b97a48dc248c9cf3dc28f21b55e06a1e0dc7dea7db5f6e46e55f2f2fed7050c`
  (44,093 bytes — **changed from fix3, +5 bytes, line 416 only**)

## Files changed (this round, NOT committed)

Per the repo rule (AGENTS.md: rendered SVGs/PNGs/PDFs are reproducible
render cache, not kept in `production/`), only sources + text.md + docs
would be committed. This round changed: `content56.py` (D8 call sites),
`content8.py` (D9 key), `content7.py` (D10 call sites),
`2026-w47-nl-zh-cn.text.md` (re-export, line 416 only),
`WEEKLY-KIT.md` (§15), `FIX-LOG.md` (this file). Unchanged, not in
this round: `bslib4.py` (no new mechanism needed — `Page.para`
already takes the wrap width; fix3's `Flow.para`/`Flow.bridge` `w`
was not extended), `content12.py`, `content34.py`. Rebuilt on disk,
NOT committed (render cache): `svg/p6-verdieping.svg`,
`svg/p7-taal.svg`, `svg/p8-toets.svg` (other 5 SVGs byte-identical to
the fix3 build), `cards/*.png`, `De-Lucerna-VOL4.pdf`,
`De-Lucerna-VOL4-web.pdf`. Fan-out text.md/PDFs NOT rebuilt in this
round — coordinator's fix4 incremental rebuild.

Not committed (goals-side scratch):
`hidden_files/w47/scratch-fix-nl4/` (logs, measurements, renders,
gates, `p8-compare-fix4.json`, `orphan-sweep-fix4.json`, crops;
`export47.py` + `stub_bslib47.py` copies of the fix3 exporter).

---

## Fix round 3 — D6/D7 orphan 。 (2026-11-11)

Core-nl reopened after independent re-proof (proof2,
`hidden_files/w47/scratch-proof-core-nl2/PROOF-NOTE.md`, conclusion (b)):
fix2's D3/D4/D5 all regressed PASS, 150 exercises, 16 mechanical gates,
all external facts PASS — but 2 new defects of the same class (both
pre-existing fix-round leftovers missed by proof1, NOT introduced by
fix2). Scope: D6 + D7 only. No wording, key, or fact changed anywhere;
only the two line breaks moved. Fan-out editions NOT rebuilt in this
round (nl re-fan-out is rebuilding 10 editions from the fix2 core in
parallel — coordinator to schedule the fix3 incremental rebuild).

### D6 — P3 trailing 。 alone on its own line (section C, HET PERFECTUM bridge)

- **Evidence (pre-fix, verified on disk):** `svg/p3-cultuur.svg`:
  bridge `用现在完成时补全，注意助动词 hebben/zijn` (x=538.5, y=2250.5,
  20.5px), then `。` alone in its own `<text>` (x=538.5, y=2280.225) —
  the only character on the line. Print-PDF crop in proof2
  `render/crop-p3-orphan.png`. text.md carries the sentence on one line
  with its 。 (the wrapper ejected it at the SVG layer).
- **Root cause:** the greedy `wrap()` at the full column width (422.5px)
  happens to push the final `。` onto a second line by itself.
- **Fix:** `bslib4.py`: `Flow.para` / `Flow.bridge` take a new optional
  `w` parameter (wrap-width override; default = column width, so every
  existing call is unaffected). `content34.py`: that one bridge call
  passes `w=CW - 40` (382.5px). Width scan: every width in 300–405px
  wraps to the same two lines
  `用现在完成时补全，注意助动词 / hebben/zijn。`; 382.5px sits 22.5px
  below the 405px threshold. Still 2 lines — no downstream y shift.
- **Re-measurement (rebuilt SVG):** lines are
  `['用现在完成时补全，注意助动词', 'hebben/zijn。']`; the orphan is
  gone. Print-PDF crop `render/crop-p3-fixed.png` confirms visually.

### D7 — P7 trailing 。 alone on its own line (A2 VOETBALWOORDEN gloss bridge)

- **Evidence (pre-fix, verified on disk):** `svg/p7-taal.svg`:
  `；de kwartfinale 四分之一决赛；scoren 进球` (x=88.0, y=755.385,
  20.5px), then `。` alone in its own `<text>` (x=88.0, y=785.11).
  Print-PDF crop in proof2 `render/crop-p7-orphan.png`.
- **Root cause:** same as D6.
- **Fix:** `content7.py`: that one bridge call passes `w=CW - 35`
  (387.5px). Width scan: every width in 377.5–395px wraps to the same
  three lines `de wedstrijd 比赛；de groepswinst 小组 / 头名；de kwartfinale
  四分之一决赛； / scoren 进球。`; 387.5px is the middle of the band.
  Still 3 lines — no downstream y shift.
- **Re-measurement (rebuilt SVG):** last line is `scoren 进球。`; the
  orphan is gone. Print-PDF crop `render/crop-p7-fixed.png` confirms
  visually.

### Full-edition orphan-punctuation sweep (rebuilt SVGs, all 8 pages)

`<text>` elements grouped by baseline y (a lone character counts as an
orphan only if it owns its whole baseline):

- Lone `。`: **0** on all 8 pages.
- Lone closing quotes `» ” ’ ） 」 》`: **0** on all 8 pages.
- Lone `：` / `–`: **0** as well.
- P8's 7 lone `）` `<text>` elements each share their baseline with 4–6
  siblings — answer-zone inline locators, not orphans (excluded, same as
  proof2).

### Side note: exporter stub (goals-side tool, not committed)

`scratch-nl/stub_bslib47.py` (the recording stub `export47.py` runs the
content files against) overrode `Flow.para`/`Flow.bridge` without `w`,
so the first text.md re-export died with
`TypeError: Flow.para() got an unexpected keyword argument 'w'`. Added
`w=None` pass-through to both overrides (signature compatibility only;
exported text unaffected). Re-export then exited 0 and produced a
byte-identical text.md.

### Fix-round-3 gates (final build, 2026-11-11)

- Build: `run.py` exit 0, TOTAL 150, by page 10/18/18/18/18/18/12/38,
  A2 46 / B1 73 / B2 31; `render.py` exit 0, zero FLOW OVERFLOW / HEAD
  TOO WIDE warnings. SVG hashes: only `p3-cultuur.svg` and
  `p7-taal.svg` changed; the other 6 are byte-identical to fix2.
- `occlusion_audit.py svg/`: selftest OK, **0 flags**.
- Creambox check (same `check_creambox.py` as fix2): same 3 CREAM-BOTTOM
  flags (P2/P5/P6, ≤1.6px); 7px strip below each box bottom probed
  pixel by pixel on the card PNGs: **0 non-paper pixels** — all three
  are the known false positives (CJK last line measured with a Latin
  0.3×size descender allowance), same as proof2. **True overflow 0.**
  (Note: my full-width band scan for P6 bottomed at 664.44 because the
  cream fill itself trips the non-paper threshold; proof2's narrower
  glyph scan gave ink bottom 661.4, clearance +3.6px. The decisive
  below-box strip probe agrees in both rounds: 0 ink.)
- `p8.py extract --p8 svg/p8-toets.svg --total 150`: noted set **150/150**.
- P8 keys vs text.md (proof2's `step3b_p8compare.py`, rerun unmodified
  except the scratch path): output **byte-identical to proof2's own run**
  — the 8 "mismatches" are all match items 25–28/141–144 whose text.md
  answers live on range-header lines (parser yields None); the match
  keys themselves agree: 25–28 = d/c/a/b, 141–144 = b/c/d/a. text.md
  is byte-identical to fix2 and the P8 keys match the proof2-verified
  set, so the 150 keys needed no fresh hand-check (nothing changed).
- Freeze (direct sha256, clean-dir re-run of `run.py`): **8/8 MATCH**.
- P8 answer font size (PyMuPDF): min = **10.12pt** ≥ 9.75pt floor.
- Web vs print text layer (PyMuPDF position-sorted): all 8 pages
  positional diff 0, multiset diff 0 (tokens 760/715/673/671/700/659/
  738/1685 = 6,520). pdftotext: print 44,197 bytes, web 44,197 bytes.
  (1 byte less than fix2's 44,198: the D6 reflow drops the single space
  that separated 助动词 from hebben/zijn — fix2's line 1 ended with
  "…助动词 hebben/zijn" (55B incl. that space) and the orphan "。" (4B);
  fix3's lines are 43B + 15B. The D7 hunk is byte-neutral (107B = 107B).
  The print-text diff vs fix2 shows exactly the two reflowed passages
  and nothing else.)
- D3 regression re-measured (proof2's `step3_gates.py`): P2 D-option
  true-ink clearances identical to proof2 (c +71.5, a +97.5, b +44.5,
  d +55.5; left 25–28 +278.5/+285.5/+208.5/+265.5). Quote sweep:
  ASCII `"` 0, backtick 0, `« »` paired on P1/P2/P7/P8, `“ ”` only the
  P1 pair. Golden lines 8/8 verbatim in body; Q150 model 81 words
  (80 excluding the standalone `–`), within 80–100.
  (Two pre-existing quirks in proof2's `step3_gates.py`, same in its
  own run: it crashes after the quote section on `re.findall(..., md)`
  where `md` is a list — the golden-lines section was re-run separately
  (`golden-fix3.txt`, 8/8); and its embedded p8-extract subsection
  reports noted set 0 because it omits `--json` — the standalone
  `p8.py extract` (150/150) is authoritative.)
- Core text.md re-export (`export47.py`, exit 0): 44,088 bytes,
  **byte-identical to fix2** (SHA `2f2a650b…b25d92e` unchanged); 432
  lines; 142 + 2 + 8 = 150 exercises; 8 golden lines; 6 gloss lines.
- Print PDF viewed page by page (PyMuPDF self-render 1.5×,
  `render/p1–p8.png`): P1/P2/P4/P5/P6/P8 clean; P3/P7 fixed spots
  confirmed by crops. No new findings. (Pre-existing proof2 N3 — P7
  VOLGENDE WEEK dark band tight to its last line — unchanged, out of
  scope for this round.)

## New SHAs (lowercase) + bytes — fix round 3

- Print PDF `De-Lucerna-VOL4.pdf`:
  `82427d3f80af23588726311dd415ff9caefe0cc153dc3b3637444babd4bc9eb7`
  (25,955,581 bytes)
- Web PDF `De-Lucerna-VOL4-web.pdf`:
  `44553e5c77d3fbf796939fc35bc43721292e44f1669253cd23fc76c47bcd5a39`
  (2,103,999 bytes)
- Core text.md `2026-w47-nl-zh-cn.text.md`:
  `2f2a650b54989e7b4b656f21cc2ae613e9dc42425a56106f03e00dff6b25d92e`
  (44,088 bytes — **unchanged from fix2**)

## Files changed (this commit, fix round 3)

Per the repo rule (AGENTS.md: rendered SVGs/PNGs/PDFs are reproducible
render cache, not kept in `production/`), only sources + text.md + docs
are committed. The rebuilt SVGs/cards/PDFs stay on disk for the
coordinator's insert flow; their SHAs are recorded above and in
WEEKLY-KIT.md §14.

- `production/2026-w47/core-nl/bslib4.py` (`w` wrap-width override on
  `Flow.para`/`Flow.bridge` — mechanism for both fixes; **first added
  to the repo in this commit**, previously untracked on disk)
- `production/2026-w47/core-nl/content34.py` (D6 call site)
- `production/2026-w47/core-nl/content7.py` (D7 call site — **first added
  to the repo in this commit**, previously untracked on disk; same
  precedent as fix2 first adding `content12.py`/`content34.py`)
- `production/2026-w47/core-nl/WEEKLY-KIT.md` (§14)
- `production/2026-w47/core-nl/FIX-LOG.md` (this file)

Unchanged, not in this commit: `content12.py` (D3 fix2 intact),
`2026-w47-nl-zh-cn.text.md` (byte-identical). Rebuilt on disk, NOT
committed (render cache): `svg/p3-cultuur.svg`, `svg/p7-taal.svg`
(other 6 SVGs byte-identical to the fix2 build), `cards/*.png`,
`De-Lucerna-VOL4.pdf`, `De-Lucerna-VOL4-web.pdf`. Fan-out text.md/PDFs
NOT rebuilt in this round — coordinator's fix3 incremental rebuild.

Not committed (goals-side scratch, same as prior rounds):
`hidden_files/w47/scratch-fix-core-nl3/` (logs, measurements, renders,
gates), `hidden_files/w47/scratch-nl/stub_bslib47.py` (the `w`
pass-through — the exporter stub lives outside the repo).

---


Core-nl reopened after nl-de proof1 (b) found D3 + D4; nl-es proof1 D5 was
verified as a true core defect and merged into this round. Scope: D3 + D4 +
D5 only. nl-de D1/D2 (German box overflow) are edition-level, pending
re-fan-out + per-edition fix1 — not in this round. D5 (web PDF italic loss)
is handled by rebuilding all web PDFs with the patched webpdf.py before
insert — not in this round.

## D3 — P2 section-D option c past the right content edge (+8.6px)

- **Evidence (pre-fix, verified on disk):** `svg/p2-leven.svg` contained
  `<text x="1473.5" y="2233" font-family="Newsreader" font-size="23">c. eten
  voor het paard van Sinterklaas</text>`. PIL measurement (Newsreader 23px):
  advance 397.1px, right edge 1870.6, content right edge 1862 → **+8.6px
  over** (matches proof1's three methods +8.5/+13.1/+11.5).
- **Root cause:** `match_set` wraps the right-side string first, then
  prepends the "c. " letter — wrap fits the bare string inside its 388.5px
  budget, but the ~23px prefix pushes the rendered line over the edge.
  Same class as fix round 1 D2 (advance estimate below true ink).
- **Fix (only `content12.py`):** `"eten voor het paard van Sinterklaas"`
  → `"eten voor Sinterklaas' paard"` (same meaning, possessive shortening;
  key c, item count, semantics unchanged). An in-content line break is not
  possible: `wrap()` only breaks at spaces and takes no manual-break token.
- **Re-measurement (rebuilt SVG, real rendered lines, PIL):**
  c "c. eten voor Sinterklaas' paard" right edge 1790.1, clearance **+71.9px**
  (gate ≥ +5px). Same-page D options re-measured: a two lines +97.8 /
  +269.4, b +45.5, d +55.5; left column 25–28 all ≥ +199. No new overflow.
  P2 card visually checked.

## D4 — text.md answer marker not localized (mechanism-level)

- **Evidence (pre-fix, verified on disk):** each of the 9 nl fan-out
  text.md files contained 150 occurrences of 「答案」 (142 single-exercise
  `— 答案：` + 8 match-item `(答案 key · …)`); core text.md has 162 lines
  containing 「答案」.
- **Root cause:** `hidden_files/w47/scratch-fanout-nl/export_fanout.py`
  hardcoded `— 答案：` in `fmt_ex` and `(答案 …)` in `fmt_match`.
- **Corrections to proof1:** (1) 「— Antwort:」 is German — it applies to
  the de reader edition only, not to the whole family; (2) core-nl (zh-cn
  reader) and nl-zh-tw (zh-tw reader) correctly use Chinese 「答案：」 and
  were NOT touched.
- **Fix:** added an `ANSWER_MARK` table to `export_fanout.py` and routed
  `fmt_ex` / `fmt_match` / the self-check regex through it:
  de `— Antwort:` / `Antwort`; en `— Correct:` / `Correct`;
  es `— Respuesta:` / `Respuesta`; fr `— Réponse:` / `Réponse`;
  it `— Risposta:` / `Risposta`; ja `— 答え：` / `答え`;
  ko `— 정답：` / `정답`; pt `— Resposta:` / `Resposta`;
  ru `— Ответ：` / `Ответ`. Match items use the bare word
  (e.g. `(Antwort c · …)`). The en form follows the existing precedent in
  the en family (`— Correct:` in en-fr / en-es / en-it / en-pt / en-nl /
  en-ru / en-ja text.md); other families carry no inline-marker precedent
  (their exporters hardcode English or have no inline marker), so the
  prescribed forms were used as given. Only the 9 text.md files were
  re-exported; no PDF was rebuilt.
- **Verification (per edition):** 「答案」 residual **0** in all 9;
  142 new exercise markers + 8 new match words each; line count 430 = 430
  unchanged; diff vs pre-re-export snapshot: exactly 300 changed lines per
  edition (150 old + 150 new), every changed line containing an old or new
  marker — no other content changed. zh-tw untouched (162 「答案」 lines,
  control). The exporter change lives in goals-side scratch (same as prior
  rounds' exporters, not committed to the repo).

## D5 — Q63 / Q126 "PSV 26 points lead the Eredivisie" has no source in this issue

- **Evidence (pre-fix, verified on disk):** core text.md line 215 (Q63
  note) and line 397 (Q126 stem + note) state PSV lead with 26 points, but
  no article, box or chart in the issue prints "PSV 26 points / leading the
  Eredivisie" (no `26 punten` anywhere in the SVGs; P4 only has Nations
  League group points; the body only gives round-12 scores Cambuur–PSV 2–5
  and Heerenveen–Feyenoord 5–3 plus the round-13 fixtures). The fact is
  externally true, but a reader cannot derive or verify the exact number
  26 from this issue — Q126's precise number could only be guessed from
  outside knowledge.
- **Fix chosen: (1) add the fact to the body** — not (2) rewrite Q126.
  Before writing, every number was verified against public sources:
  VAVEL, PitchLab, Sports Mole, Sports Oracle, TuringStats and 4 more all
  agree — after round 12 (8 Nov 2026): PSV 26 pts (1st), Feyenoord 25 (2nd),
  Ajax 25 (3rd).
- **Change (only `content34.py`):** P4 HET PROGRAMMA box gained a 5th fact:
  `"Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten."`
  (parallels the existing "Stand na 4 wedstrijden: …" fact; 2 lines, box
  +73px, P4 col3 ends 1129.6 → 1202.6, ~400px clear of the exercises rule
  at 1608). Q63's note and Q126's stem/note are unchanged — with this line
  both are now directly verifiable from the text (26 readable; 25 is
  Feyenoord's points, a live distractor; 8 is the Nations League points).
- **Re-measurement:** the line is present in the P4 SVG, in both PDFs'
  text layers and in the re-exported text.md (line 188); P4 card visually
  checked (line inside the box, clear margins). The 9 fan-out PDFs still
  lack the line — they inherit it at re-fan-out from the fixed core; not
  rebuilt in this round.

## Gates (final build, 2026-11-11)

- `run.py` exit 0: TOTAL 150, by page 10/18/18/18/18/18/12/38,
  A2 46 / B1 73 / B2 31; `render.py` exit 0; zero FLOW OVERFLOW /
  HEAD TOO WIDE warnings.
- `occlusion_audit.py svg/`: selftest OK, **0 flags**.
- Creambox check (`scratch-fix-core-nl1/check_creambox.py`, PIL true-ink
  measurement of every text inside every cream `#f0eee5` box + page-edge
  scan): **0 real overflows**. The v2 geometric scan flagged 3
  CREAM-BOTTOM lines (P2/P5/P6, ≤1.6px); a pixel probe on the rendered
  cards found 0 ink pixels in the 7px strip below each box — the flags are
  artifacts of a Latin 0.3×size descent allowance applied to CJK-only last
  lines (no descenders), identical in the pre-fix build.
- `p8.py extract --total 150`: noted set **150/150**.
- Freeze (direct sha256, clean-dir re-run of `run.py`): **8/8 MATCH**.
- P8 answer font size (PyMuPDF): min = median = **10.12pt** ≥ 9.75pt floor.
- Web vs print text layer (PyMuPDF position-sorted): all 8 pages positional
  diff 0, multiset diff 0 (tokens 751/706/665/659/686/649/736/1668 = 6,520).
  pdftotext: print 44,198 bytes, web 44,198 bytes.
- Full re-proofread of rebuilt print PDF text vs fix-round text: diff only
  14 lines — the D3 string (1 place) + the D5 line (2 lines) + pdftotext
  reading-order shifts of the same P4 sentences. P2/P4 cards viewed.
- Core text.md re-export (`export47.py`, exit 0): 44,088 bytes;
  142 + 2 + 8 = 150 exercises; 8 golden lines; 6 gloss lines. Diff vs
  pre-rebuild: only the D3 match line (line 124) and the D5 box line
  (+line 188).

## New SHAs (lowercase) + bytes

- Print PDF `De-Lucerna-VOL4.pdf`:
  `5308f4a321e6176acfe58b69b858413183093097559b6fe3bd9a50eb5bd361f8`
  (25,955,593 bytes)
- Web PDF `De-Lucerna-VOL4-web.pdf`:
  `a5f7ecba7d8436fb9173f2f468b6074e98514e316964b6e50c8cd966d6a1cfd3`
  (2,104,002 bytes)
- Core text.md `2026-w47-nl-zh-cn.text.md`:
  `2f2a650b54989e7b4b656f21cc2ae613e9dc42425a56106f03e00dff6b25d92e`
  (44,088 bytes)
- Fan-out text.md (9, marker-only re-export, 430 lines each):
  - nl-de `8e7a9935d9488306798f1eb32729ff53616c362b13b8396900b1301b44444e68`
  - nl-en `eea7dff83ae166d32e84494105132f8cda2eef7de4525749e63db8292bb62738`
  - nl-es `982d3fb694ee820fd27954cc004517b487eaf4294b567f9a05ba198afdbaee8b`
  - nl-fr `5a2275c2d535b410bf207d8a7df956b3724d9f9cc1fb0bbcb5c1d192c8784f41`
  - nl-it `4e4b505acfe00a97d36f6b0bf8e32650c4130118171011241104adf1411df3af`
  - nl-ja `a5c66d8e50746750d2ebe955dab4a793060e08251dd01be3e9b7208da10c404f`
  - nl-ko `702e12429b09648655760352f966574f4483c5b63413d2d22a9ebd861f26683a`
  - nl-pt `5686b0b8cecdf16f3df92bcad915ae8ca85a7eeedee34b45e35b9e31f2ccc033`
  - nl-ru `bb43662b68f56e072b19ba5544ae70208786775fcdfa03f3d47776c55b7d6ee1`

## Files changed (this commit)

Per the repo rule (AGENTS.md: rendered SVGs/PNGs/PDFs are reproducible
render cache, not kept in `production/`), only sources + text.md + docs are
committed. The rebuilt SVGs/cards/PDFs stay on disk for the coordinator's
insert flow; their SHAs are recorded above and in WEEKLY-KIT.md §13.

- `production/2026-w47/core-nl/content12.py` (D3)
- `production/2026-w47/core-nl/content34.py` (D5)
- `production/2026-w47/core-nl/2026-w47-nl-zh-cn.text.md`
- `production/2026-w47/core-nl/WEEKLY-KIT.md` (§13)
- `production/2026-w47/core-nl/FIX-LOG.md` (this file)
- `production/2026-w47/fanout-nl/2026-w47-nl-{de,en,es,fr,it,ja,ko,pt,ru}/2026-w47-nl-<r>.text.md`
  (D4 marker-only re-export)

Rebuilt on disk, NOT committed (render cache): `svg/p2-leven.svg`,
`svg/p4-sport.svg` (other 6 SVGs byte-identical to the fix-round build),
`cards/*.png`, `De-Lucerna-VOL4.pdf`, `De-Lucerna-VOL4-web.pdf`.

Not committed (goals-side scratch, same as prior rounds):
`hidden_files/w47/scratch-fix-core-nl1/` (logs, measurements, snapshots,
repro), `hidden_files/w47/scratch-fanout-nl/export_fanout.py` (ANSWER_MARK
change — the exporter itself lives outside the repo).
