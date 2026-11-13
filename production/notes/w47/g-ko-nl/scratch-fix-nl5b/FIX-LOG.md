# FIX-LOG — core-nl fix round 5 (D11, 2026-11-11)

Fix agent nl5b. Takes over from fix5 agent cd9d373a, drained mid-run by a
runtime restart. **Nothing of its work was taken on trust: its on-disk
source edit was independently re-derived from `svglib.py` semantics before
being kept, and the whole build + gate suite was re-run from scratch.**

## 0. Handover — what was found on disk

- Probes first: `/dev/null` exists; `git hash-object -w` inside
  `~/workspace/weekly-git` rc=0 (an earlier attempt from `$HOME` failed
  with rc=128 only because the cwd was not a repo — re-probed in-repo,
  pass); scratch dir
  `hidden_files/w47/scratch-fix-nl5b/` writable (probe file written).
- Baseline three items verified byte-for-byte against the task brief
  (fix4 final state — the previous agent had **not** rebuilt the PDFs):
  - print `De-Lucerna-VOL4.pdf`:
    `2c7f2c6fb3c443fa32a6055bfa4a368f11a761c75de0995b776204510a7ecd3c` /
    25,955,580 B ✓
  - web `De-Lucerna-VOL4-web.pdf`:
    `434626f58b605b8ba0878b7d52de32e8255f2ad43489e133e602faef49853df5` /
    2,103,990 B ✓
  - text `2026-w47-nl-zh-cn.text.md`:
    `0b97a48dc248c9cf3dc28f21b55e06a1e0dc7dea7db5f6e46e55f2f2fed7050c` /
    44,093 B ✓ (identical to `scratch-fix-nl5/text-before-fix5.md`)
- Previous agent's footprint:
  - `content34.py:134` edited on disk (the only source hunk in
    `git diff`): `sh = 62 + …` → `sh = 89 + …`, with a 4-line comment
    claiming top reserve 89 (16 pad + 52 title block + 21 para offset),
    last baseline 617.89 below the top, sh=638 leaving 20.11px.
  - `scratch-fix-nl5/build-fix5.log` is **empty (0 bytes)** — no build
    log survived. But `svg/p1–p7` mtimes are 15:25:44–15:26:21 UTC
    (its run) while `svg/p8` is still 14:52:57 (re-proof's run): the
    drain hit between `content7.py` (P7 saved 15:26:21) and
    `content8.py` (P8 never rewritten). Its run was partial — p1–p7
    rewritten, p8 untouched. Pre-build hash check in this round:
    only `p4-sport.svg` differed from `svg-hashes-before.txt`
    (`6e05d5a0…` vs `c82c9a3c…`); the other 7 were byte-identical to
    fix4, so the partial run changed nothing else.
  - D8 (`content56.py:151 capcn_w`), D9 (`content8.py:75 kort`),
    D10 (`content7.py:99 dt_zh_w`) untouched by either agent this
    round — verified in `git diff` (only the one `content34.py`
    hunk) and re-verified by the regression checks in §6.

## 1. D11 — independent verification (not the previous agent's numbers)

Re-derived from first principles with the real `wrap()`/`para()`
semantics of `svglib.py` (`verify-d11.py`, log `verify-d11.log`):

- `Page.para(x, y, …)`: first baseline exactly at `y`; each line
  advances `size*lh`; returns `last_baseline + size*lh`.
- `caption()`: fr para at `y+24` (19pt, lh 1.35 → 25.65/line); credit
  para at `y+2` (15.5pt, lh 1.3 → 20.15/line). P4 image ends y=450;
  caption wraps 2+2 lines → `cy3 = 567.60`, `sy3 = cy3 + 24 = 591.60`
  — matches the SVG rect `y=591.6` exactly.
- P4 facts wrap at `CW − 44 = 378.5px`, 21.5pt serif: counts
  **3/3/3/2/3 = 14 lines** (last fact: `Speelronde 13: zaterdag NEC
  – PSV` / `16:30 uur; Feyenoord – Excelsior` / `18:45 uur.`).
- Render loop: `yy3 = sy3+16`; title baseline `yy3+26 = sy3+42`;
  `yy3 += 52` → `sy3+68`; per fact first baseline `yy3+21`, advance
  `21.5 × 1.42 = 30.53`/line, `para` return +12 gap. Simulated
  baselines: 680.60 … 1148.43 / 1178.96 / **1209.49**.
  - First fact baseline offset from box top: **exactly 89.00**
    (= 16 pad + 52 title block + 21 para offset). The formula's
    top reserve of 62 was 27px short — the root cause, confirmed
    independently.
  - Last baseline offset: **617.89**; absolute y = **1209.49** —
    identical to the re-proof measurement.
  - Old `sh=611`: box bottom 1202.60, last-baseline margin **−6.89px**;
    true ink (PIL 4× Newsreader mask of `18:45 uur.`: glyphs end
    0.75px above the baseline, no descenders in the line) bottom
    1208.74, margin **−6.14px** (re-proof's card probe measured
    −6.4px at render scale — same spill within rounding).
  - New `sh=638`: box bottom **1229.60**, last-baseline margin
    **+20.11px**, true-ink margin **+20.86px**.
  - Formula re-check: `89 + Σ(n·30.5+12) + 32 + 30 = 89 + 487 + 62
    = 638.0` ✓ (old: `62 + 487 + 62 = 611.0` ✓).
  - Two small notes, both harmless and left as-is (minimal change):
    the formula uses 30.5 vs the true advance 30.53 — a 0.42px
    cumulative under-count over 14 lines, absorbed by the 20.11px
    margin; the `32 + 30` tail is pure bottom pad (20.11px after
    the last baseline, vs 16px top pad — balanced).
  - Downstream: `P4 col3 ends` 1202.6 → 1229.6; exercises hline at
    y=1608, clearance **378.40px** — no impact.
  - Cross-check, same code shape on P3 (4 facts, tail 64):
    `sy3=597.10`, `sh=509.5`, last baseline 1090.40, box bottom
    1106.60, margin **+16.20px** — inside, no spill. (P3's larger
    tail is why the same −27px top error did not spill there.)
- **Verdict: the previous agent's edit is arithmetically correct.
  Kept unchanged** — no source line was modified by this agent.

### The change (only `content34.py:130–134`, one hunk)

```diff
-sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
+# Fix5 D11: top reserve was 62 but box-top -> first baseline is really
+# 16 (pad) + 52 (title block) + 21 (para y-offset) = 89; the 27px shortfall
+# put the last baseline 6.89px below the box bottom. With 89 the simulated
+# last baseline sits 617.89 below the top and sh=638 leaves 20.11px below it.
+sh = 89 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
```

## 2. Build (all rebuilt in this round, venv python)

- `run.py` rc=0 (`build-fix5b.log`): TOTAL **150**, by page
  10/18/18/18/18/18/12/38, A2 46 / B1 73 / B2 31; 0 FLOW OVERFLOW /
  HEAD TOO WIDE. `P4 col3 ends 1229.6`; `P3 col3 ends 1106.6`,
  `P6 chart ends 665`, `P6 col3 ends 1000.0`, `P7 col3 ends 1898.0`
  — all identical to fix4 except P4 (+27.0, as designed).
- SVG hashes after build (`svg-hashes-after.txt` vs
  `scratch-fix-nl5/svg-hashes-before.txt`): **only `p4-sport.svg`
  changed** (`c82c9a3c…` → `6e05d5a0…` — byte-identical to the
  previous agent's partial-run p4, confirming the rebuild is
  deterministic); the other 7 SVGs are byte-identical to fix4.
- `render.py` rc=0 (`render-fix5b.log`, repeat
  `render-fix5b-repeat.log`): 8 cards; print PDF 25,955,578 B,
  SHA `b7d4a9cddbc38dd56ddd22cd2ae15a2e04ba1988670b6cf384eafbc66bd7ce47`.
  Two consecutive renders are byte-identical. (The −2 B vs fix4's
  25,955,580 B is the p4 content-stream change; fix4's own render
  log showed 25,955,582 B for the same delivered PDF, so ±2 B
  render variation was already observed before.)
- `tools/webpdf.py` rc=0 (`webpdf-fix5b.log`): web PDF 2,104,000 B,
  SHA `5a47449cdff7d5847aee81c1c5b0f1af54cfeda873c5b55058a6d18f0e10404c`,
  44,197 text bytes (unchanged).
- text.md re-export (`export47.py` + `stub_bslib47.py`, copies of
  the fix4 exporter, rc=0, `export-fix5b.log`): **byte-identical**,
  SHA `0b97a48d…7050c`, 44,093 B, 432 lines, 142 + 2 + 8 = 150
  exercises, 8 golden, 6 gloss. D11 changes no text content, as
  expected.

## 3. D11 triple measurement (rebuilt build)

Box (rebuilt SVG): `x=1439.5 y=591.6 w=422.5 h=638.0`,
bottom **1229.6**; last line `<text x=1461.5 y=1209.49 size=21.5>`
`18:45 uur.`

| # | Method | Result |
|---|---|---|
| 1 | SVG geometry | last baseline 1209.49, margin to box bottom **+20.11px** |
| 2a | True ink, cards 1× (`inkprobe-d11-fix5b.py`) | lowest true-ink row y=**1209.00**, margin **+20.60px**; 7px strip below box bottom: **0** non-paper pixels |
| 2b | True ink, print PDF 150dpi (`render/p-4.png`, scale 1.5625) | lowest true-ink row y=**1209.12**, margin **+20.48px**; 7px strip below box bottom: **0** non-paper pixels |
| 3 | Visual, 150dpi crop (`render/crop-p4-programma.png`) | `18:45 uur.` sits inside the cream box with a clear cream margin below it; box bottom edge visible beneath the line. **Pass by eye.** |

Repair values to record: box bottom 1229.6, last baseline 1209.49,
true-ink bottom 1209.00 (cards) / 1209.12 (print 150dpi), margins
+20.11px (baseline) / +20.48–20.60px (ink). Old spill was +6.89px
baseline / +6.4px ink — now +20px inside.

## 4. Spill sweep — full week, 8 pages (the creambox blind spot)

Method: re-proof's `spill_sweep_reproof.py`, copied to this scratch
as `spill_sweep_reproof.py` (source noted in the file header;
unchanged logic). For every cream (`#f0eee5`) rect, lists texts whose
baseline is 0–60px below the box bottom / 0–60px above the box top /
0–60px outside the box's x-range with baseline inside its y-range.
`check_creambox.py` skips whole lines whose baseline is outside the
rect, and occlusion BOXTITLE only counts stroked boxes — this sweep
covers both blind spots. Log: `spill-sweep-fix5b.log`.

**Result: 0 spills.** The P4 box now has NO below hit at all. All
remaining hits adjudicated (nearest BELOW hit anywhere is +24px):

BELOW hits (all independent blocks, not box content):
- P1 box bottom 1652.0: +24.00 `HET WOORD VAN DE WEEK` — next section head.
- P1 box bottom 2304.0: +44.00 `读头版，选出正确答案 答案见第8版` — quiz instruction line.
- P2 box bottom 1768.0: +32.00 `Let op: schrijf je gedicht in het Nederlands…` — note under the four-word boxes.
- P5 box bottom 1076.4: +50.50 `译注｜de surprise…` — gloss box below.
- P7 box bottom 1011.5: +60.00 `HET WOORD 本周生词` — next section head.
- P7 box bottom 1311.5: +60.00 `BRIEVEN VAN LEZERS` — next section head.

ABOVE hits are captions/credits/preceding paragraphs belonging to the
block above each box (e.g. P4 `domein` photo credit −44.15px; P6 D8
caption lines −55.98/−31.56px above the VOOR OF TEGEN box; P7 gloss
lines above the letters box). SIDE hits are neighbouring boxes' own
titles at the same y (P2 `WORTEL`/`LIJSTJE`/`GEDICHT` — each belongs
to its own box) and P1 col-2 feature text beside the DEZE WEEK box.
None is box content outside its box.

**Tool debt (for the coordinator): this sweep must be added to the
standing pre-insert gates** — `check_creambox.py` + occlusion cannot
see a whole line outside a fill-only box (this is exactly how D11
shipped in fix2 and survived fix3/fix4). Script + result are kept in
this scratch (`spill_sweep_reproof.py`, `spill-sweep-fix5b.log`).

## 5. Full gate table (final build)

| Gate | Command / method | Result |
|---|---|---|
| run.py | `tools/venv/bin/python run.py` | rc=0, TOTAL 150, 0 overflow warnings |
| SVG scope | hashes vs fix4 before | **only p4 changed**, other 7 byte-identical |
| render.py | 2 runs | rc=0, byte-identical SHA `b7d4a9cd…` |
| text.md | re-export | byte-identical `0b97a48d…` |
| freeze baseline | `tools/freeze.py baseline --build <core> --core-svg <svg> --out scratch-fix-nl5b/freeze` | rc=0, **8/8 MATCH**; core SVGs unchanged by the run |
| occlusion | `tools/occlusion_audit.py svg/` (selftest first) | selftest OK, **0 flags** (BOXTITLE 0) |
| creambox | re-proof `check_creambox_reproof.py` | same 3 known CREAM-BOTTOM flags (P2/P5/P6, ≤1.6px); P4 now 0 |
| creambox true ink | `inkprobe2_reproof.py` (copied) | 3 strips: **0** non-paper pixels; clearances +3.4/+3.5/+3.6px; P7 golden lowest ink 2378.0, footer band top 2439, margin 61.0px |
| spill sweep | §4 | **0 spills**, 8 pages |
| p8 extract | `tools/p8.py extract --total 150` | noted set **150/150** |
| 3-way key compare | re-proof `p8compare_reproof.py` | **MATCH 149/149, DIFF 0, MISSING 0**; #150 open-writing exception; Q140 four-source MATCH; 25–28=d/c/a/b, 141–144=b/c/d/a |
| orphan sweep | re-proof `orphan_sweep_reproof.py` (PIL + svglib + brute force) | 1421 lines; (a)=**0**/(b)=**0** both methods, all pages; brute force 12 closer-leading fragments, leftmost **0** |
| print vs web text | re-proof `gates_reproof.py` (PyMuPDF, 0.1pt) | multiset diff **0** all 8 pages; positional diff **only P1 2 tokens** (`De`/`Lucerna` x 394.0 vs 393.8, the known 0.2pt font-subset micro-shift, also present in re-proof) |
| pdftotext | print / web / scratch web re-render | 44,197 = 44,197 = 44,197 B, **byte-identical** |
| web byte check | delivered vs scratch re-render (2,104,000 vs 2,103,997 B, −3 B) | single differing region = one font-subset stream (obj 20, Length 2174 vs 2173, same Length1 3320) — fontTools subsetting is non-deterministic run to run; text layer identical. Not a defect. |
| P8 min font | PyMuPDF spans, print P8 | **10.12pt** ≥ 10pt (561 spans at 10.12) |
| D3 regression | PIL true ink, P2 (method: 4× draw + getbbox) | right a +98.2 / b +46.0 / c +72.2 / d +55.8; left 25 +272.8 / 26 +280.2 / 27 +200.0 / 28 +259.2 — all far inside edge 1862. (Within ~1.5px of re-proof's `font.getbbox` values; the gap is the render method, not the content.) |
| quotes | print text + text.md | ASCII `"` 0, backtick 0, `« »` 35/35, `“ ”` 1/1, md same |
| golden lines | 8 verbatim in text.md | **8/8** |
| Q150 model | direct count, text.md:432 | **81 words** excl. standalone `–` (82 incl.), in 80–100. (Note: the gates script's regex fallback reports 110 — it grabs the wrong paragraph; re-proof noted the same miscount. The direct line count is authoritative.) |
| D5 fonts | record only, not judged | totals Noto Sans CJK SC 619 / Newsreader 1215 / Noto Serif CJK SC 305 / UnifrakturMaguntia 1; pure-Latin-on-CJK **245** (per page 38/23/30/29/29/26/18/52) — identical to re-proof's count by the same script. Not fixed, not a gate. |
| 8-page visual | print PDF 150dpi `render/p-1..p-8.png` | all 8 viewed; no new defect (see §7) |

## 6. D8 / D9 / D10 regression (fix4's three fixes intact)

- **D8** (P6 caption): SVG lines `练习数据：虚构数字，仅供练习，非真实调查。`
  (635.02) / `问题：你在鞋里放什么？（100 名年轻人）` (659.44) —
  2 lines, baselines unchanged; crop `render/crop-p6-d8.png`: 。
  at line-1 end, line 2 starts with 问题. **Intact.**
- **D9** (Q140): `p8-compare-fix5b.json` #140 MATCH —
  registry key = text.md:416 = P8 node =
  `Ik maak een surprise met een kort gedicht.`; crop
  `render/crop-p8-q140.png` shows it printed. **Intact.**
- **D10** (P7 letters): SVG lines `截稿时未收到真实来信或第 8 版最佳作文，`
  (1754.27) / `刊登示例信，承诺顺延 VOL.5。` (1782.67) — 2 lines,
  baselines unchanged; crop `render/crop-p7-d10.png`: ， at line-1
  end, line 2 starts with 刊. **Intact.**
- p6/p7/p8 SVGs are byte-identical to fix4 (§2) — the three fixes
  cannot have regressed by construction, and the checks above
  confirm it on the rebuilt output.

## 7. Visual (print PDF 150dpi, `render/p-1..p-8.png`)

- P1: clean. NU JIJ 1–6, BLIKSEMQUIZ 7–10 complete.
- P2: clean. `c. eten voor Sinterklaas' paard` inside; the
  "D WOORDEN" head/content split across col 3/4 is the pre-existing
  layout already noted in re-proof (observation, not a defect).
- P3: clean. D6/D7 repairs hold; SINTERKLAAS IN CIJFERS box contents
  all inside (its +16.20px margin verified in §1).
- P4: **D11 fixed** — HET PROGRAMMA box holds all 5 facts with a
  clear cream margin under `18:45 uur.`; exercises below untouched.
- P5: clean. EN JIJ box last line inside; Q73 fill-in area normal.
- P6: clean. D8 caption two lines; VOOR OF TEGEN box complete.
- P7: clean. D10 letters two lines; 8 golden quotes + page notes;
  VOLGENDE WEEK dark band still tight at its bottom edge (proof2 N3,
  pre-existing observation, unchanged).
- P8: clean. Q140 key with kort; Q150 model (81 words); all 150
  answers present.

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

Before → after (three items): print `2c7f2c6f…ecd3c` / 25,955,580 B →
`b7d4a9cd…7ce47` / 25,955,578 B; web `434626f5…53df5` / 2,103,990 B →
`5a47449c…0404c` / 2,104,000 B; text `0b97a48d…7050c` / 44,093 B →
unchanged.

## Files changed (this round, NOT committed)

Per the repo rule, only sources + text.md + docs would be committed.
This round: `content34.py` (D11, one hunk — written by the previous
agent, independently verified and kept by this agent),
`FIX-LOG.md`, `WEEKLY-KIT.md` (§16). `2026-w47-nl-zh-cn.text.md`
was re-exported in place but is byte-identical, so it carries no
change. Unchanged: `bslib4.py`, `content12.py`, `content56.py`,
`content7.py`, `content8.py`. Rebuilt on disk, NOT committed (render
cache): `svg/p4-sport.svg` (other 7 byte-identical to fix4),
`cards/*.png`, `De-Lucerna-VOL4.pdf`, `De-Lucerna-VOL4-web.pdf`.
Fan-out text.md/PDFs NOT rebuilt in this round — coordinator's fix5
incremental rebuild.

Not committed (goals-side scratch):
`hidden_files/w47/scratch-fix-nl5b/` — `probe.txt`, `verify-d11.py` /
`verify-d11.log`, `build-fix5b.log`, `render-fix5b.log` /
`render-fix5b-repeat.log`, `export-fix5b.log`, `webpdf-fix5b.log`,
`export47.py` / `stub_bslib47.py` (fix4 exporter copies),
`svg-hashes-prebuild.txt` / `svg-hashes-after.txt`,
`freeze/` + `freeze.log`, `occlusion.log`, `creambox-fix5b.log`,
`inkprobe2-fix5b.log`, `inkprobe-d11-fix5b.py` /
`inkprobe-d11-fix5b.log`, `p8-fix5b.log`, `p8-extract.json`,
`p8-compare-fix5b.json` / `p8compare-fix5b.log`,
`orphan-sweep-fix5b.json` / `orphan-sweep-fix5b.log`,
`spill-sweep-fix5b.log`, `gates-fix5b.json` / `gates-fix5b.log`,
`print-text-fix5b.txt` / `web-text-fix5b.txt` /
`web2-text-fix5b.txt`, `webpdf/web.pdf` (scratch re-render),
`q150-line432.txt`, `render/` (8 pages at 150dpi + 4 crops),
`check_creambox_reproof.py` / `gates_reproof.py` /
`inkprobe2_reproof.py` / `orphan_sweep_reproof.py` /
`p8compare_reproof.py` / `spill_sweep_reproof.py` (re-proof scripts,
copied with scratch path repointed; logic unchanged), this FIX-LOG.md.
Read-only source reused from `scratch-fix-nl5/`: `svg-hashes-before.txt`,
`text-before-fix5.md` (baseline snapshots; nothing written there).
