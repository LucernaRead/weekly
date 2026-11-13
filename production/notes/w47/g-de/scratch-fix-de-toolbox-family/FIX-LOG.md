# FIX-LOG — 2026-W47 de-toolbox family fix1 (6 editions: de-fr / de-it / de-nl / de-ru / de-ja / de-ko)

- Scope: ONLY D1 (P7 DER WERKZEUGKASTEN box too short) on the 6 editions above.
  Fixer: de-toolbox-family fix1 builder (leaf). Date: 2026-11-11.
- Scratch: `hidden_files/w47/scratch-fix-de-toolbox-family/`
  (FIX-LOG.md + `creambox.py` + `creambox-de-<lang>-{pref,post}.log` + `gates.sh` + `d2scan.py` +
  `gates-<lang>/` per-edition gate logs/renders + `content7-<lang>-postfix.py` revert-test copies).
  Build logs live in `hidden_files/w47/scratch-fanout-de/<lang>/` (the shared build driver).
- NOT touched: de-en (fix1 running in parallel), de-es (already fixed), de-pt (proof2 in flight),
  de-zh-tw (proof1 in flight), core-de (read-only reference), `tools/`, `issues/`, `covers/`.
  No commit, no push, no subagent. Proof2 to be assigned separately by the coordinator.

## 0. Probes + pre-fix state

- Probe at task start: `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` OK;
  real test file written in `hidden_files/w47/scratch-fix-de-toolbox-family/`. Re-probed OK before
  every write batch. /tmp was 3% used at start (not full as briefed); intermediates still kept in
  the workspace scratch dir, never /tmp. Disk: no quota pressure.
- SOP §8 + §1.1, repo AGENTS.md, coordinator brief, de-es proof1 PROOF-NOTE §D1 and de-es fix1
  FIX-LOG (incl. root-cause arithmetic, 10-edition sweep table, pt/nl/ru caveat) all read first.
- Pre-fix SHA-256 (all three deliverables per edition, verified before editing):

| Edition | Print PDF (bytes) | Web PDF (bytes) | text.md (bytes) |
|---|---|---|---|
| de-fr | `126e9522eb9980012692bf84e7ed5e420032fd2574ea355ac62466529c0e0700` (10,932,570) | `727c8b8a4f7ee27d0687b4503f0cf47c3e766f081538aa9ce1cf06da55f842f5` (1,556,917) | `3ef1934af59e6ba8f6cf59d1cd24fcfdd30f1a25e5b8c1a4f544446bd7ff0db6` (50,042) |
| de-it | `0d7be5816da194742ed4b25e10e15b3a35353e243535c4361e12722c300bbb93` (10,965,095) | `dbbe5880e1b8b1309e981f021c8e41e2f862fe62629816c2be8c9e90a3290f46` (1,553,872) | `1594ba080bece8b9a947cf011a64a355125b8869f82413ccdb03ae31a269f255` (49,712) |
| de-nl | `8f47eea85f54067532cad3e21ba74d3ed98133a3eabc5605dcb34ca3cca8d6d6` (10,964,699) | `be22a1b5beda4dcaaeccbcffcb7a122e01bb3f92a488d896fd261808ffc34551` (1,553,854) | `e904fb3d7ee18a72c1316f8693f39436ff9390648261d6fbad18afcfb7fc848e` (49,403) |
| de-ru | `17f334608c1dfe2cf00ce8b955e8968fce23e53b6322dfd53986845ed995c40a` (10,954,761) | `76f1aba78b60027a74a365bb2d189c62300dac49b5a25a476a499546531cb02a` (1,605,337) | `dee6697b0ec3ff279ad4508dcc7d7402952d40fcc8670b1208a2de9158074958` (56,231) |
| de-ja | `f412f930242d16c87a7fb783506f6e92e5020a40e323edfdb1243dfd82db459d` (23,901,736) | `29f65fec5681e46f5b927171163c5d66559e61ed275d998583653574d8e8294a` (2,113,024) | `a59f784705bec4329b7dfa19321256c2469ab7680212302481876fc96f957f69` (51,913) |
| de-ko | `d0cb457ce4d856726b279f792156a005f376441a7f2353c75f7c50346235dc67` (15,907,001) | `fe4b835a037d93c33240292af4300f5e487ac33861df66c0f33e60c374fd29d0` (1,906,546) | `fd2dbd047e23bcd0fffc5245ee8d529b9e848adc11133ff46f490b304b8a66a2` (51,498) |

## 1. Defect D1 as measured per edition (creambox.py, pre-fix)

Method copied from de-es fix1 (`scratch-fix-de-es1/creambox.py`): every `#f0eee5` box in
`svg/p7-sprache.svg` matched against text baselines in its column. The −35.0 rows are the
matcher's known false positives (A2/B1/B2 BEISPIELE boxes matched against exercise numbers below
them, same in all editions incl. core); only the col-3 rail (toolbox / LESERBRIEFE / NOCH EIN WORT)
is read here. Full logs: `creambox-de-<lang>-pref.log`.

| Edition | Σlines (measured wraps) | Toolbox bottom | Last baseline | Clearance | LESERBRIEFE clr | NOCH EIN WORT ends |
|---|---|---|---|---|---|---|
| de-fr | 9 [1,2,2,2,1,1] | 783.5 | 783.9 | **−0.4** | +10.4 | 1518.0 |
| de-it | 9 [1,2,2,2,1,1] | 783.5 | 783.9 | **−0.4** | +10.4 | 1518.0 |
| de-nl | 10 [1,2,2,2,2,1] | 813.0 | 813.0 | **+0.0** | +10.4 | 1547.5 |
| de-ru | 10 [1,2,2,2,1,2] | 813.0 | 813.0 | **+0.0** | +10.4 | 1547.5 |
| de-ja | 8 [1,1,2,2,1,1] | 754.0 | 754.8 | **−0.8** | +10.4 | 1488.5 |
| de-ko | 8 [1,1,2,2,1,1] | 754.0 | 754.8 | **−0.8** | +10.4 | 1488.5 |

Σlines measured directly per edition by running each edition's own `bslib4.wrap` over its 6 `tb`
entries (not copied from es). All 6 editions have the defect in ink terms (4 negative, 2 at exactly
0.0 where the `fraglich` descender ~4.7 still spills below the box edge). Occlusion audit is blind
to this class in all 6 (text drawn after its own box, nothing covers it).

## 2. Root cause, derived per edition (not copied from es)

Same shared formula in every edition's `content7.py:76`:

```python
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 90
```

- Geometry: box bottom = 330 + 62 + (29.5·Σ + 36) + pad = 428 + 29.5Σ + pad.
  Last baseline L: title ends at yy3=398; each entry advances 20.5 + n·29.11 + 6
  (`Page.para`: first baseline at yy3+20.5, lines at 20.5·1.42 = 29.11, returns last baseline
  + 29.11, caller adds 6) — so L = 398 + 5·26.5 + 20.5 + (Σ−1)·29.11 = 521.89 + 29.11Σ.
  Check against measurement: Σ=8 → 754.8 ✓; Σ=9 → 783.9 ✓; Σ=10 → 813.0 ✓.
- Hence clearance(pad) = pad + 0.39Σ − 93.89, i.e. per edition:
  fr/it (Σ=9): pad − 90.4; nl/ru (Σ=10): pad − 90.0; ja/ko (Σ=8): pad − 90.8.
  The formula under-counts by the +20.5/entry para offset (6 entries = +123), only partly
  compensated by the 29.5-vs-29.11 line-height overestimate (+0.39/line).
- Core-de uses pad **110** on the same formula (+18.8 clearance, Σ=7). The fan-out cut it to 90
  with a "validated by en/fr occlusion 0 flags" comment — void validation, see §1.

## 3. Fix design per edition

### 3a. fr / it / ja / ko — pad 90 → 110 (restores the core value)

Downward slack is ample (NOCH EIN WORT ends 1518.0 / 1488.5, 30 / 59.5px before the 1548 rule).
One line per edition (`content7.py:76` only) + arithmetic comment, same pattern as de-es fix1.

| Edition | Pad | Clearance −0.4/−0.8 → | Toolbox bottom → | NOCH EIN WORT ends → |
|---|---|---|---|---|
| de-fr | 110 | **+19.6** | 803.5 | 1538.0 (10px before 1548) |
| de-it | 110 | **+19.6** | 803.5 | 1538.0 (10px before 1548) |
| de-ja | 110 | **+19.2** | 774.0 | 1508.5 |
| de-ko | 110 | **+19.2** | 774.0 | 1508.5 |

LESERBRIEFE shifts +20 down in all four (y 819.5 / 790, 16px gap from toolbox bottom preserved,
its own +10.4 clearance unchanged). Nothing else on P7 moves (A2/B1/B2 flows, image, phrases
py=1560 fixed, clinic, teaser all untouched). No text changed anywhere.

### 3b. nl / ru — pad 90 → 110 PLUS whole col-3 rail raised 20 (RTOP)

- Flat pad 110 is impossible here: NOCH EIN WORT already ends at **1547.5**, 0.5px before the
  1548 Sätze-der-Woche rule — a flat +20 would push it to 1567.5, past the rule. Any positive
  downward shift breaks the rule, so the minimum-pad alternative is also impossible.
- Upward slack measured (not assumed): P7 intro is 2 single lines in all 6 editions (baselines
  226 German / 262 native, verified in the SVG for nl and ru; nothing else drawn in col 3
  between y 267 and 330 — the only element in that band is the toolbox rect itself). Slack above
  the toolbox ≈ 330 − 267 ≈ **63px** ≫ 6px required. Both nl and ru qualify for the upward
  design, so no edition is left unrepaired.
- Fix (`content7.py:76–77,84` only): pad 90 → 110 **and** `RTOP = CTOP − 20` (310), used for
  the toolbox rect y, the rail text start (`yy3 = RTOP + 16`) and `ry = RTOP + tbh + 16`
  (wy3 derives from ry, so NOCH EIN WORT follows). CTOP itself is untouched — the A2/B1/B2
  columns still start at 330.
- Verified geometry (identical in nl and ru):
  toolbox box y 330 → **310**, bottom **813.0 (unchanged)**; last baseline 813.0 → **793.0**;
  clearance **+20.0**; LESERBRIEFE y 829 / bottom 1381.5 (+10.4, unchanged); NOCH EIN WORT
  y 1398 / ends **1547.5 (unchanged**, still 0.5px before the 1548 rule, +42.9 unchanged).
- Cosmetic note: the toolbox box top now sits 20px above the A2/B1/B2 column heads (330).
  Full P7 renders viewed at 100 dpi (nl + ru): the raised top reads cleanly against the intro
  gap, no collision, no excess whitespace. The title/entries all moved up together, so the
  inside layout is identical (same 16px title offset, same entry spacing).

## 4. Rebuilds + gates (all 6)

Driver: `tools/venv/bin/python build_edition.py <lang>` from `scratch-fanout-de/`
(run.py → render.py → webpdf → verify → occlusion → p8 extract/compare → freeze diff →
pdftotext print/web → chips → text export → P8-min). It does NOT re-run transform, so the
fix survives. Extra gates per edition (`gates.sh <lang> <trdir>` in this scratch dir):
creambox re-measure, `freeze_direct.py` (rendered 8/8 + source), `keycheck.py`,
`boxtitle.py`, parametrized `d2scan.py`, §1.1 grep, bent-quote + Q34 spot checks,
P7 100 dpi full page + 300 dpi toolbox zoom (print + web), P8-min + chips recompute.
**All 6 editions: driver ALL GATES PASS** (for ja/nl the driver's tail scrolled off in the
background delivery, but every gate it checks was re-verified from its fresh log files —
see per-edition rows below; P8-min/chips recomputed independently).

### Per-edition results

| Edition | Toolbox clr | NOCH EIN WORT ends | Print PDF (new SHA) | Web PDF (new SHA) | text.md |
|---|---|---|---|---|---|
| de-fr | +19.6 (803.5) | 1538.0 | 10,932,565 B (−5) `0df35360ac599e8af590f990ae302dfe17f8daf23904bbc4e5aac6d641ecc413` | 1,600,197 B (+43,280) `5262bfaea8f8947874171b558e704e36bc7f138e3c9419afce5809a76836b167` | 50,042 B `3ef1934a…` UNCHANGED |
| de-it | +19.6 (803.5) | 1538.0 | 10,965,087 B (−8) `ca802fb853eb3f18c61cddd5da406c72c9c0471cabd84c76731478f4cdf6f2c0` | 1,596,994 B (+43,122) `09fb247059a96c37c0fa1fe0178b7dacf35cd1e5500fe6f089b929c722c82300` | 49,712 B `1594ba08…` UNCHANGED |
| de-nl | +20.0 (813.0) | 1547.5 | 10,964,697 B (−2) `c8a5f5e2ea2affc15df0aef472ce08f74e3ae5cc826d2ef49d636c866c083521` | 1,596,830 B (+42,976) `4ed5b46e385815a4358cb01407e0a476f69cdc9885801756998410fd5e336d8a` | 49,403 B `e904fb3d…` UNCHANGED |
| de-ru | +20.0 (813.0) | 1547.5 | 10,954,759 B (−2) `d8f84e0500e23c19aed45e5eda095a37c8c55ca71c8e94aa43fdd0f0b5d4bf1e` | 1,647,527 B (+42,190) `462f516d1087dc7d997f9b7be66ccd842b7225fed37601ffcbf7c54ee9407c41` | 56,231 B `dee6697b…` UNCHANGED |
| de-ja | +19.2 (774.0) | 1508.5 | 23,901,741 B (+5) `2638a6e62c00da39933a3e921bb74d0d81d6cc00ddf2eff50000c182554f98e1` | 2,155,095 B (+42,071) `161f2dd0bdfefecffe06944ded2d22f22410daeb321e7bc387c745da9cbcce16` | 51,913 B `a59f7847…` UNCHANGED |
| de-ko | +19.2 (774.0) | 1508.5 | 15,907,006 B (+5) `1ee2229f5e0d9803d9b32e9c048027a1bced2783bacac9ed72a83499cd866bcc` | 1,909,587 B (+3,041) `9a0699420966ff7354c3e11d078a2e46ecde8ff35badab03f2be7f8722fe6776` | 51,498 B `fd2dbd04…` UNCHANGED |

Web-PDF growth (+42–43k, ko only +3,041) is the working-tree `webpdf.py` now embedding the
`LucernaNewsreader-Bold` subset (fr 23,780 B / it 23,444 B / nl 22,408 B / ru 21,696 B /
ja 21,596 B in the webpdf log) — the same effect de-es fix1 recorded for pt/ko/zh-tw; ko's
rebuild-B web PDF already carried the subset, hence the small delta. All web PDFs < 7 MB,
8 pages, real text layer, default word multiset identical to print (fr 50,879 B / it 50,592 B /
nl 50,192 B / ru 57,607 B / ja 52,873 B / ko 52,318 B, print = web in every edition);
`-raw` normalised identical everywhere).

### Gate summary (identical pattern in all 6 unless noted)

- `run.py`: exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150. P7 col3 ends:
  fr/it 1538.0, nl/ru 1547.5, ja/ko 1508.5 — exactly as designed.
- `verify.py`: TOTAL 150, numbering continuous, SVGs byte-identical after re-run,
  SOP 1.1 style audit True (old-style hexes []), verbatim OK, P8 floor True.
- `occlusion_audit.py` real run (no `--selftest`): **0 flags** in all 6.
- `p8.py extract` 150/150, `compare` vs core **CLEAN**, keydiff=[137, 138, 139, 150] in all 6.
- `freeze.py diff`: fr/it/nl/ru +7 CJK, all U+3000; ja +2,994 / ko +3,096 (the CJK
  explanation layers themselves).
- `freeze_direct.py`: rendered **8/8** in all 6. Source PASS (0 unaccounted) in fr, it, nl,
  ru, ko. **ja source FAIL is pre-existing** — see §5. Frozen shas identical to pre-fix in
  every edition (fr/it/nl: 083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 /
  b7aa0771 / 57e118e7; ru: 73347f49 / 689045ad / f356adcf / df1bebf7 / e7b235f9 / 2bbe05f9 /
  591dc064 / 7016818d; ko: 73347f49 / 689045ad / 8b2e9eba / df1bebf7 / e7b235f9 / 2bbe05f9 /
  591dc064 / f6dd4a15; ja counts identical to rebuild-B: 144/164/200/166/179/173/163/183).
- `keycheck.py`: fr/it/nl/ru/ja **149/150** (Q150 extractor truncation only, expected);
  ko **148/150** (Q139 + Q150 — both pre-existing extractor join artifacts, documented in
  the ko KIT §6, byte-identical mismatches to rebuild-B — see §5).
- `boxtitle.py`: **7/7 fit** in all 6 (fr/it run from `scratch-fanout-de-rebuild-A/`, which
  holds the current `tr_fr.py`/`tr_it.py` — see §5 for why the other copy must not be used).
- `d2scan.py`: fr 58 / it 58 / nl 54 / ru 80 / ja 67 / ko 72 abutting pairs, **0 with web
  gap > 0.5pt** in all 6.
- P8 minimum span size (PyMuPDF): **9.94pt** in all 6 (≥ 9.75pt floor). Chips 141 in all 6
  (10/15/18/15/18/18/12/35; P8 A2 22 / B1 13 / B2 0).
- §1.1 grep: palette hexes in SVGs are all §1.1 values; verify.py style audit True in all 6.
- Bent quotes: U+201C 33 / U+201D 0 / U+201E 33 / U+2019 0 in all 6 text.md (all paired).
- Q34: new singular stem 1× / old plural 0× in content34.py, .text.md, p3 SVG, print and web
  text layers (spot-checked p3 SVG + text.md; freeze P3 sha unchanged proves the layers).
- Visual: P7 100 dpi full page + 300 dpi toolbox zoom viewed for **every edition** — last
  entry fully inside the cream box (clear cream below the `fraglich` descender); nl/ru full
  pages confirm the raised box top reads cleanly with no collision. Print/web toolbox zooms
  are pixel-identical in all 6 (same sha256 for both renders per edition).

## 5. Pre-existing non-D1 findings (NOT regressions, NOT fixed here — out of scope)

Each was verified pre-existing by a pad-90 revert re-run and/or byte-identical pre-fix records.
The D1 scope allows only the `content7.py` pad/RTOP lines; none of these is touched by that fix.

1. **fr — stale `tr_fr.py` in `scratch-fanout-de/`:** `freeze_direct.py` / `boxtitle.py` run
   from `scratch-fanout-de/` read the pre-rebuild-4 `tr_fr.py` (long box titles) and report
   source FAIL (4 unaccounted abbreviated titles) / boxtitle 1/7. Run from
   `scratch-fanout-de-rebuild-A/` (current `tr_fr.py`, shortened titles) both pass:
   freeze_direct source PASS + rendered 8/8; boxtitle 7/7. The rendered titles themselves
   measure 7/7 (max 376.9 ≤ 400.5). Proven pre-existing: freeze_direct re-run with pad
   reverted to 90 gives the same 4 unaccounted. (The fr KIT rebuild-4 note already records
   that the titles were shortened in the sources; the stale TR copy was never updated.)
2. **ja — `freeze_direct` source FAIL (documented JP font switch):** unaccounted removed
   `Noto Serif CJK SC` (1) / added `JP`, `Noto Sans CJK JP`, `Noto Serif CJK JP` (3) —
   `svglib.py` CJK font-name literals not covered by `tr_ja.py` accounting. Byte-identical
   to the rebuild-B pre-fix run (same 4 strings) and to a pad-90 revert re-run. Rendered 8/8
   with frozen counts identical to rebuild-B. Already documented in the ja KIT §3/§5.
   Fix belongs to the tool/tr accounting, not to this D1 fix.
3. **ko — keycheck 148/150:** Q139 space-join (`대림절 달력을` + `만들고 있습니다.`) and Q150
   PREFIX — both extractor join artifacts, verified correct in the P8 SVG, documented in the
   ko KIT §6; byte-identical mismatches to the rebuild-B keycheck. Unchanged by this fix.
4. **it — same stale-copy note as fr (weaker):** `scratch-fanout-de/tr_it.py` is also stale;
   `freeze_direct`/`boxtitle`/`keycheck` for it were therefore run from
   `scratch-fanout-de-rebuild-A/` (current `tr_it.py`), where all pass. No defect in the
   edition itself.

## 6. pad 90 — shared-source investigation

**There IS a single shared origin, with per-language copies:**

- Origin: `hidden_files/w47/scratch-fanout-de/gen_tr.py` ~L116–117 defines
  `TB_OLD` (pad 110, the core value) → `TB_NEW` (pad 90 + the "90 validated by en/fr
  occlusion 0 flags" comment) and emits it into every generated `tr_<lang>.py` as a
  `LAYOUT_<LANG>` replacement pair.
- Per-language copies: `scratch-fanout-de/tr_<lang>.py` (and the rebuild-A batch copies
  `scratch-fanout-de-rebuild-A/tr_{en,es,fr,it,pt}.py`) each carry their own copy of the
  pair (en's comment differs slightly: "90 puts the Leserbriefe box 10px below the toolbox ink").
- Applier: `scratch-fanout-de/transform.py:311` reads `LAYOUT_<UP>` from `tr_<lang>.py` and
  applies the string replacement to the edition's `content7.py` during fan-out.
- So pad 90 was **not** written per-edition by hand — it was injected once, centrally, by
  the fan-out generator, and then frozen into all 10 editions' `content7.py` files.

**Recommendation (for the coordinator — NOT done here, this round must not touch the shared
source):** fix `gen_tr.py`'s `TB_NEW` to pad 110 (or better, fix the formula to count the
+20.5/entry para offset) and regenerate the `tr_<lang>.py` files, so any future re-transform
does not re-inject pad 90 into these editions. Note the nl/ru RTOP design cannot be expressed
in the current one-line LAYOUT replacement mechanism — if the family rollout goes through
transform, nl/ru/pt need a dedicated layout entry (rect-y + rail-start + ry lines), not just
the pad literal. Also note the stale-copy trap found in §5.1/§5.4: `scratch-fanout-de/tr_fr.py`
and `tr_it.py` are outdated; only the rebuild-A copies are current — any future transform run
must use the current copies.

**Side observation (not mine, for the coordinator's lanes):** at the time of the final sweep,
`de-pt/content7.py` already read `+ 90 + 20` and `de-zh-tw/content7.py` already read `+ 110` —
their own fix agents have landed their own remedies. en's fix1 was still in flight (its pad line
was mid-edit). None of those files were touched here.

## 7. Files changed

Per edition (6×):
- `production/2026-w47/2026-w47-de-<lang>/content7.py` — fr/it/ja/ko: line 76 only
  (pad 90 → 110 + arithmetic comment); nl/ru: lines 76–77, 84 (pad 90 → 110 + `RTOP = CTOP − 20`
  + rail lines switched to RTOP + comments).
- Rebuilt deliverables in the same edition dir: `svg/*.svg` (all 8 re-rendered; freeze_direct
  shas prove only P7 geometry differs — text identical on all 8 pages), `cards/*.png`,
  both PDFs, `<slug>.text.md` (re-exported, byte-identical sha in all 6).
- `production/2026-w47/2026-w47-de-<lang>/WEEKLY-KIT.md` — Status line + fix1 rebuild note
  (fr: §6 Rebuild 5; it: §7 Rebuild 4; nl/ru: §6 fix1 note; ja/ko: §6 fix1 bullet).
- Notes only: this scratch dir (`FIX-LOG.md`, `creambox.py`, `creambox-de-<lang>-*.log`,
  `gates.sh`, `d2scan.py`, `gates-<lang>/`).
- NOT touched: any other edition, `core-de/`, `tools/`, `issues/`, `covers/`, the shared
  fan-out sources (`gen_tr.py`, `tr_*.py`, `transform.py`), git index (no commit/push).

## 8. Handoff summary (for the coordinator)

- **6/6 repaired, 0 left unrepaired.** fr/it/ja/ko: pad 110, clearance +19.2…+19.6,
  NOCH EIN WORT ends 1508.5/1538.0 (≤ 10px margin to the 1548 rule where applicable).
  nl/ru: pad 110 + rail raised 20 (RTOP), clearance **+20.0**, toolbox bottom / LESERBRIEFE /
  NOCH EIN WORT **all unchanged** (1547.5, still 0.5px before the 1548 rule).
- All 6: driver ALL GATES PASS; occlusion 0 flags; p8 CLEAN; freeze_direct 8/8 rendered;
  text.md byte-identical (zero content change); 300 dpi zooms confirm the descender inside
  the box; print/web zooms pixel-identical.
- Pre-existing items carried forward (not regressions, out of D1 scope): ja freeze_direct
  source FAIL (JP font-switch strings, identical pre/post); ko keycheck 148/150 (extractor
  join artifacts, documented); fr/it stale `tr_*.py` copies in `scratch-fanout-de/` (use the
  rebuild-A copies for those two languages).
- Family action still open: fix `gen_tr.py` TB_NEW (pad 90 → 110) + regenerate `tr_*.py`
  so a future re-transform cannot re-inject pad 90; nl/ru/pt need a dedicated layout entry
  for the rail raise. de-pt / de-zh-tw lanes have already landed their own remedies
  (observed, not mine).
- Proof2 (independent, per edition) still to be assigned by the coordinator; this fix1
  builder does not self-certify.
