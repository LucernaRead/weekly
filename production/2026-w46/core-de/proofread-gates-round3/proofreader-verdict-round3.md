# Round 3 Proofreader Verdict — Lucerna Weekly 2026-W46, DE edition 2026-w46-de-zh-cn (P8 scope + occlusion adjudication)

**Issue:** Mon 2026-11-09 – Sun 2026-11-15. Target language German, reader-native Simplified Chinese.
**Proofreader:** independent, Round 3. Did not build or fix this edition. Did not edit, re-render, or re-sync anything. Verdict date: 2026-11-03.
**Scope:** P8 ONLY in ONE edition — `2026-w46-de-zh-cn`, folder `files/weekly-report-w46-de-zh-cn/` — PLUS the occlusion-flag adjudication and the de-core duplicate check. The other 10 DE editions are Round 2 PASS and were verified byte-identical only (hash/PDF-text level); no fresh full proofread of them was in scope.
**Fix record adjudicated:** `hidden_files/w46/de-fix-round3/FIX-REPORT.md` + §7 fix record in the zh-cn `WEEKLY-KIT.md`.
**Gate directory (this round, fresh):** `hidden_files/w46/de-proofread-gates-round3/` (all JSONs/logs/crops below live there; Round 2 / fix dirs were not reused).
**Rules observed:** `~/workspace/weekly-git` untouched, `index.json` untouched, nothing pushed/inserted/posted, no edition content dumped into chat, no subagents spawned. All gates were re-run by the proofreader with the canonical shared tools (`tools/occlusion_audit.py`, `tools/p8.py`, `tools/freeze.py`, venv Python); no tool conclusion was trusted from the fix worker.

## Verdict summary

| Question | Ruling |
|---|---|
| D-R2-1 fix (key 140 `das` split) | **CONFIRMED** — fixed; key 140 renders intact (§1) |
| Occlusion Flag 1 (5.2px, keys 17/58 seam) | **REAL OVERPRINT (minor), NEW in Round 3** — fix worker's "measurement artifact / visually clean" adjudication REFUTED (§2.1). Blocking: D-R3-2 |
| Occlusion Flag 2 (76.2px, keys 80–81/124 seam) | **REAL OVERPRINT (severe), NEW in Round 3** — fix worker's "pre-existing" attribution REFUTED (§2.2). Blocking: D-R3-1 |
| Round 2 "0 flags" discrepancy | **NO DISCREPANCY — Round 2 reproduces.** Round 2 was correct on Round 2-state SVGs; the fix worker's "pre-fix" audit audited post-fix SVGs (§3) |
| Regression gates (freeze / p8 / counts / PDF / .text.md) | **ALL PASS** except occlusion (§4) |
| Change isolation | **CONFIRMED** — only zh-cn changed, exactly the 5 files listed (§5) |
| De-core duplicate | **Divergent, defective, must not ship** (§5) |
| Keys 16/79/140 | Text-identical to the EN fan-out (§6) |

**Final verdict line: ROUND 3 FAIL — de-zh-cn is NOT shippable. Blocking defects: D-R3-1 and D-R3-2 (two NEW TEXTX overprints on P8 introduced by the Round 3 re-wrap). D-R2-1 itself is fixed. Required fix: keys-block reflow of the zh-cn P8 (§8), then a P8-only Round 4 re-proofread.**

## 1. Fix verification — D-R2-1: CONFIRMED

The defect (Round 2 verdict §5): in `svg/p8-uebungen.svg`, key 140 rendered as `…schaue ich da` / `sNFL-Spiel.`, splitting the word `das`.

Fixed rendering, quoted verbatim from the shipped P8 SVG (282 text elements, unchanged count), with coordinates:

- `<text x="1451" y="2091.0">（wieder begonnen = 又开始） · 140. Am Sonntag schaue ich</text>`
- `<text x="1451" y="2109.85">das NFL-Spiel.（看比赛 = das Spiel schauen） · 141. b（Mantel=…</text>`

Full key-140 rendering across the two lines: `… · 140. Am Sonntag schaue ich` / `das NFL-Spiel.（看比赛 = das Spiel schauen） · 141. b …` — the sentence `Am Sonntag schaue ich das NFL-Spiel.` is intact, one whole token per line, no split. Visual: full-res crop `crops/key140-fixed-2x.png` (from the shipped card `cards/p8-uebungen.png`, region x 1400–1950, y 2030–2165) shows `das NFL-Spiel.` clean, no overflow/overlap. P8 full frame (half-scale, `crops/p8-full-fixed-half.png`) is clean overall with no footer overflow.

Corroboration:

- `sNFL` = **0** occurrences in all 8 zh-cn SVGs, in `2026-w46-de-zh-cn.text.md`, and in both PDF text layers (web + print).
- `p8.py extract` key 140 (fixed zh-cn) = `Am Sonntag schaue ich das NFL-Spiel.` — exactly equal to the EN fan-out's extracted key 140. The unfixed core duplicate extracts `Am Sonntag schaue ich da sNFL-Spiel.` (see §5).
- Key text/note/gloss unchanged: freeze diff vs core shows the +13/−13 P8 strings are re-wrap placement only (§4); the joined key stream is identical (p8.py CLEAN, §4).
- Same-class repairs verified: key 16 `begonnen` now whole on one line (`begonnen） · 17. …`, el x=65 y=2198.02) and key 79 `beginnt` now whole (`beginnt.（beginnt置尾） · 80. …`, el x=527 y=2523.12), vs the v2 splits `begonne`/`n）` and `beginn`/`t置尾` in the core duplicate. The three restored separator spaces are present: `· 16.`, `· 24.`, `· 129.`.
- `76.` intact on one line: `76. Die Kinder freuen sich, weil St. Martin kommt.（weil 句动词置…` (x=527, y=2447.72).
- Own scans over all 8 zh-cn pages (`scans/round3_scans.py`, `scans/kinsoku-token-scan.log`): line-start hits **0**, line-end hits **0**, lone-punctuation elements **0**, S1-signature lines **0**. Own positional scan: 5 lowercase-fragment line pairs, ALL adjudicated whole-word wraps at spaces (e.g. `…Karnevalssession` / `beginnt.…`; `…es` / `dunkel ist.…`; `…ich` / `das NFL-Spiel.…`) — **0 mid-word splits** in the whole edition. Combined with the p8 extract key identity, the token-split class is closed for the fixed text stream. (The two overlong lines in §2 are a column-overflow defect, not token splits.)
- No origin asserted for D-R2-1 (as in Round 2 and the fix report): whether the split pre-dated the kinsoku changes could not be established, and none is asserted here. The fix stands on its own evidence regardless.

**Adjudication: D-R2-1 CONFIRMED fixed.** The fix worker's code-path account (v2 END-pass shedding one glyph off `das`) was not independently re-derived — the shipped artifacts are the evidence, and they confirm the repair. The v3 wrap change itself is NOT endorsed beyond this: it lengthened two keys-block lines past their columns, creating D-R3-1/D-R3-2 (§2).

## 2. Occlusion flags — adjudication (own audits + own crops)

### 2.0 Own audit results (canonical tool, selftest OK, deterministic)

Run with `tools/venv/bin/python tools/occlusion_audit.py` (tool mtime 2026-10-27, unchanged since Round 2):

| Input | Result | Evidence |
|---|---|---|
| Fixed zh-cn SVG dir, run 1 | **2 flags, both TEXTX, P8 only** | `occlusion/zh-cn-run1.json/.log`, exit 1 |
| Fixed zh-cn SVG dir, run 2 | **Identical JSON** (byte-identical diff) | `occlusion/zh-cn-run2.json/.log` |
| Fixed zh-cn with `--core` = core duplicate | **core 0 flags; NEW vs core: 2** | `occlusion/zh-cn-vs-core.json/.log`, exit 1 |
| Core duplicate (true Round 2 state, §3) | **0 flags, all 8 pages** | `occlusion/core.json/.log`, exit 0 |
| EN P8 control (read-only) | **0 flags** | `occlusion/en.json/.log`, exit 0 |
| ZH-TW P8 control (read-only) | **0 flags** | `occlusion/zh-tw.json/.log`, exit 0 |
| Fix worker's `scratch/svg-v2scan` (v2 code) | **0 flags** | `occlusion/scratch-v2scan.json/.log`, exit 0 |
| Fix worker's `scratch/svg-v3scan` (v3 code) | **2 flags, identical texts/boxes to the fixed edition** | `occlusion/scratch-v3scan.json/.log`, exit 1 |

No other flag class fired anywhere (no COVER/LINEX/FOOTER/EDGE/BOXTITLE). The two flags are the ONLY occlusion findings, both on `p8-uebungen.svg`, both in the keys block. Geometry below uses the tool's true-ink boxes (PIL/FreeType). Column layout: keys columns start x = 65 / 527 / 989 / 1451, width 434 → column right edges 499 / 961 / 1423 / 1885.

### 2.1 Flag 1 — REAL OVERPRINT (minor), NEW — D-R3-2 (blocking)

Tool flag (own JSON, identical in both runs):

> `[TEXTX] 'später（15:30 晚于 11:11）） · 58. leiser（leise → leiser（空场' — ink overlaps 'begonnen） · 17. Die Kinder haben Martins' by 5.2x11.7px`, box `[527.0, 2181.5, 948.2, 2197.2]`, by `text@221`.

Geometry (own ink-box dump, `scans/ink-boxes-flag-sites.txt`):

- Col-2 line (x=527, baseline y=2193.96): `später（15:30 晚于 11:11）） · 58. leiser…` — box `[527.0, 2181.5, 948.2, 2197.2]`, identical in core and fixed.
- Col-1 line (x=65, baseline y=2198.02): core `n） · 17. Die Kinder haben Martinslieder gesungen.（singen →` — box right **490.8** (36.2px clear of col-2's x=527 start; no overlap). Fixed `begonnen） · 17. Die Kinder haben Martinslieder gesungen.（singen` — box right **532.2**, i.e. **33.2px past its column edge (499)** and 5.2px into col-2's line band. Line ink width 467.2px vs 434px column.
- The re-wrap moved the whole token `begonnen）` onto this line, extending its ink 41.4px rightward (490.8 → 532.2) into the neighbouring column.

Visual ruling — REAL, not artifact. Own full-res crop `crops/flag1-fixed-2x.png` (card region x 400–1010, y 2140–2245, 2×): at the column seam the tail `(singen` of col-1 and the head `später` of col-2 share pixels — the glyphs read as merged `singe[n/s]päter`, with the `n` of `singen` and the `s` of `später` overprinted (baselines 4.06px apart, so the strokes interleave rather than sitting on separate rows). The contrast crop `crops/flag1-core-2x.png` (same region, Round 2 state) shows a clean gutter: `…begonne` / `n. (singen →` on the left, `später` clean on the right, no contact. The fix worker's adjudication ("measurement artifact / benign proximity … visually separated") is therefore REFUTED: the 5.2px is real ink-on-ink collision, visible at full resolution. It is small, but under proofread-until-zero a visible glyph collision in the answers block is a defect, not a tolerance item. It is fixed by the same reflow as Flag 2 (enforce the column edge); it is not acceptable as-is.

**Ruling: Flag 1 = REAL OVERPRINT, NEW (introduced by the v3 re-wrap), BLOCKING defect D-R3-2.**

### 2.2 Flag 2 — REAL OVERPRINT (severe), NEW — D-R3-1 (blocking)

Tool flag (own JSON, identical in both runs):

> `[TEXTX] 'beginnt.（beginnt置尾） · 80. Richtig（11 月 9 日巴伐利亚也复课） · 81. Fal' — ink overlaps '15:30） · 124. A（纪念日 11 月 15 日） · 125. B（' by 76.2x12.2px`, box `[527.0, 2510.6, 1065.2, 2526.6]`, by `text@295`.

Geometry (own ink-box dump):

- Col-2 line (x=527, baseline y=2523.12): core `t置尾） · 80. Richtig（…） · 81. Falsch` — box right **947.8** (41.2px clear of col-3's x=989 start; no overlap). Fixed `beginnt.（beginnt置尾） · 80. Richtig（…） · 81. Falsch` — box right **1065.2**, i.e. **104.2px past its column edge (961)**. Line ink width 538.2px vs 434px column.
- Col-3 line (x=989, baseline y=2527.18): `15:30） · 124. A（纪念日 11 月 15 日） · 125. B（…` — box `[989.0, 2514.4, 1396.5, 2528.7]`, identical in core and fixed. Vertical ink overlap 12.2px; baselines only 4.06px apart.
- The re-wrap merged `beginnt.` onto this line (repairing the key-79 split), lengthening its ink 117.4px (947.8 → 1065.2) and driving its tail `…81. Falsch` through the head of the col-3 line. In the core state the same content sat on two lines (baselines 2504.27 + 2523.12), neither of which collided (upper line box right 970.0 vs col-3 line at y=2508.33 starting x=989 — 19px clear).

Visual ruling — REAL, severe. Own full-res crop `crops/flag2-fixed-2x.png` (card region x 480–1450, y 2470–2575, 2×): the seam shows plainly jumbled glyphs — `15:30)` overprinted by `Falsch`, rendering as `15:30)Falsch 124. A`, with the `F`/`a` strokes superimposed on the digits and `124. A` partly obscured. Neither the tail of item 81 nor the head of item 124 is cleanly legible at the seam. The contrast crop `crops/flag2-core-2x.png` shows the same site clean: `…81. Falsch` ends well clear of `15:30） · 124. A`. The fix worker's site description (538px line in a 434px column; baselines 2523.12/2527.18) is accurate; its "pre-existing" attribution is wrong (§3).

**Acceptability ruling: BLOCKING, no acceptable-as-is case.** The overprint garbles printed answer text (items 81 and 124) — the core deliverable of P8. There is no strong justification for shipping jumbled glyphs: the text is not decipherable by context at the seam (two unrelated items superimposed), the SOP occlusion gate requires true defects to be fixed and re-audited to zero, and proofread-until-zero admits no "small overprint" tolerance. The fix worker's "outside the fix scope, left untouched" is a scope statement, not a justification for acceptance, and scope does not transfer to the shipping verdict.

**Ruling: Flag 2 = REAL OVERPRINT, NEW (introduced by the v3 re-wrap), BLOCKING defect D-R3-1. Exact fix + scope: keys-block reflow of the zh-cn P8 only (§8).**

### 2.3 What the flags are NOT

- Not a tool false-positive class: both flags are TEXTX ink-vs-ink with measured boxes and visible collisions; the tool's selftest passed and clean controls (EN, zh-tw, core, v2scan) are silent.
- Not a footer/edge/cover issue: no other class fired; P8 full frame shows no footer intrusion.
- Not present in any other edition audited (EN/zh-tw controls 0; core 0). The defect is zh-cn-P8-specific, in the re-wrapped keys block only.

## 3. Round 2 discrepancy investigation — NO DISCREPANCY; Round 2 stands

**Question:** Round 2 reported 0 occlusion flags on all pages/all editions. The fix worker reported the canonical invocation does NOT reproduce 0 flags on Round 2-state SVGs, and asserted no explanation. **Finding: the 0-flag result DOES reproduce on the true Round 2-state SVGs. There is no discrepancy to explain; the fix worker's non-reproduction claim is refuted.**

Evidence, in order:

1. **The core duplicate IS the Round 2 state of zh-cn, hash-proved.** Current `weekly-report-w46-de-core/svg/p8-uebungen.svg` sha256 `89e34350…` equals the fix worker's own pre-fix snapshot hash for zh-cn P8 (`pre-fix-hashes.json`), and its text elements quote exactly the Round 2 verdict's D-R2-1 lines (`…schaue ich da` / `sNFL-Spiel.`; `begonne`/`n）`; `beginn`/`t置尾`). The snapshot comparison (`hash-isolation.log`) shows the core dir entirely unchanged vs the snapshot. The core is therefore a trustworthy Round 2-state witness, independent of the fix worker's later claims.
2. **My canonical audit on that witness returns 0 flags** (`occlusion/core.json`, exit 0, selftest OK) — the same result Round 2 recorded in `de-proofread-gates-round2/occlusion/zh-cn.json` and `core.json` (both `flag_count: 0`, same selftest line, same tool). Round 2's JSONs are plain canonical outputs (no `--core` keys, `flag_count` 0) — i.e. a plain run on the Round 2 SVGs, exactly the invocation the fix worker used for the fixed edition. No invocation difference is evidenced: same tool file (mtime 2026-10-27, predates both rounds), same selftest output, same venv.
3. **The fix worker's own v2/v3 scan pair confirms the split:** `scratch/svg-v2scan/p8-uebungen.svg` is hash-identical to the core/Round 2 P8 and audits to **0 flags**; `scratch/svg-v3scan/p8-uebungen.svg` is hash-identical to the fixed P8 and audits to **2 flags** (identical texts/boxes). The flags track the code version (v2→v3), not the audit invocation.
4. **Why the fix worker's "pre-fix" audit showed 2 flags:** `de-fix-round3/occlusion-pref.json` claims to audit the Round 2-state SVGs at `scratch/svg-out`, with flag texts/boxes identical to the fixed edition. But `scratch/svg-out/p8-uebungen.svg` is hash-identical to the **fixed** P8 (`df4fd583…`), NOT to the Round 2 P8 — and its mtime (05:47:02) precedes `occlusion-pref.json` (05:51:28). The flag texts themselves prove it: both flags name the v3-repaired lines (`begonnen） · 17.…`, `beginnt.（beginnt置尾） · 80.…`), which do not exist in the v2 SVGs. **Most likely explanation, on this evidence: the scratch `svg-out` directory was (re)written by the post-fix build before the "pre-fix" audit ran, so the audit measured fixed SVGs and was mislabelled as pre-fix.** Intent cannot be established from the files and none is asserted; what IS established is that the audited input was post-fix (hash + mtime + flag-text evidence), so `occlusion-pref.json` is not evidence about the Round 2 state at all. The Round 2 verdict's occlusion claim (§3(b)/§7) is therefore vindicated, not impugned.
5. **Environment explanations excluded:** a Pillow/font difference cannot explain a 76.2px overlap appearing/disappearing — and the same environment + same tool gives 0 on v2 SVGs and 2 on v3 SVGs in this round. The difference is the SVG text distribution, not measurement.

**Conclusion: do not re-raise a Round 2 occlusion discrepancy. Round 2's 0-flag finding was correct for the state it audited. The 2 flags are new Round 3 regressions, and FIX-REPORT §5.1 / KIT §7 must be corrected on this point (see §8) — the "0 new flags / byte-identical pre/post" and "Flag 1 artifact" statements are factually wrong and must not be carried into the shipping record.**

## 4. Regression gates (P8 scope) — ALL PASS except occlusion

| Gate | Result (own runs) | Evidence |
|---|---|---|
| Freeze `freeze.py diff --strict-cjk` (zh-cn vs core duplicate) | **exit 0.** P1–P7 +0/−0 strings; P8 **+13/−13** strings; TOTAL added CJK **0** | `freeze/zh-cn.json/.log` |
| Freeze +13/−13 content | **Exactly the v3 re-wrap, no content change.** All 13 added/removed pairs are the same keys-block lines re-broken (incl. `sNFL-Spiel.` → `das NFL-Spiel.`; `begonne`/`n）` → `begonnen）`; `beginn`/`t置尾` → `beginnt.…`; three restored `· N.` spaces: `·129.`→`· 129.`, `·16.`→`· 16.`, `·24.`→`· 24.`). Element count unchanged (282). | `freeze/zh-cn.json` (verified pair-by-pair) |
| P8 `p8.py compare --total 150` (zh-cn vs core) | **CLEAN 150/150**, missing=[], extra=0, uncertain=[]; **keydiff [140]** — the correction itself (fixed key vs defective rendering; returns to [] if the duplicate is re-synced) | `p8/zh-cn-vs-core.json/.log` |
| Counts | **150**: 149 numbered (1–149 continuous) + item 150; per-page **10/18/18/18/18/18/12/37** (+150 on P8 = 38); chips A2 57 / B1 70 / B2 14 / 8 untagged (113–120) — identical to Round 2, all 12 dirs | `counts.json/.log` (proofreader's `count_exercises.py`, re-run) |
| PDF text layer | **web == print byte-identical, 47,665 bytes each**; web PDF **1,670,966 bytes ≤ 7 MB**; `sNFL` 0; `das NFL-Spiel` ×3 in web text | `pdf-web.txt`, `pdf-print.txt` (cmp clean) |
| `.text.md` | **Byte-identical to Round 2**: 37,769 bytes, sha256 `7feaf88c…` — identical across fixed zh-cn, core duplicate, and the fix worker's pre-fix copy (`textmd-pre-fix.md`); 1,409 lines. (The FIX-REPORT "695 items" figure could not be re-derived from the file's visible structure — 94 `###` headings, 8 `##` — and is not relied on; hash identity is the gate, and it holds.) | hash comparison in §5 |
| Kinsoku / token splits | **0 / 0 / 0** + **0 mid-word splits** (§1) | `scans/kinsoku-token-scan.log` |
| Dates/weekdays | Independently verified (Europe/Berlin): Mon 2026-11-09 … Sun 2026-11-15; Mon 2026-11-16 outside the week | `scans/dates-berlin.log` |
| P8 visual | Full frame clean; key-140 block clean (§1); flag sites defective (§2) | `crops/` |

## 5. Change isolation + duplicate divergence

**Isolation — CONFIRMED.** Full sha256 comparison of every file in all 12 DE edition dirs against the fix worker's pre-fix snapshot (`hash-isolation.log`): exactly **5 DIFF files, all in zh-cn, no extra/missing files in any dir**:

1. `svg/p8-uebungen.svg` (89e34350… → df4fd583…, 50,404 bytes)
2. `cards/p8-uebungen.png` (1,335,671 bytes)
3. `Die-Lucerna-VOL3-ZH-CN.pdf` — print (16,578,262 bytes; −10 vs snapshot)
4. `Die-Lucerna-VOL3-ZH-CN-web.pdf` — web (1,670,966 bytes; −10 vs snapshot)
5. `WEEKLY-KIT.md` (Round 3 fix record appended as §7; earlier sections untouched per the record — the §7 occlusion sentences are factually wrong per §3 and need correction, see §8)

Unchanged in zh-cn: the other 7 SVGs, the other 7 cards, `ABSTRACT.txt`, and `.text.md` (byte-identical). The other 10 editions + the core duplicate are byte-identical to the snapshot in every file. Independent corroboration: re-measured `pdftotext` byte counts for all 11 editions match the Round 2 equality log exactly (en 48,496; es 50,100; fr 49,946; it 49,571; ja 50,640; ko 49,557; nl 49,275; pt 49,672; ru 56,649; zh-cn 47,665; zh-tw 47,235 — `scans/pdf-bytes-recheck.log`). The other 10 editions' Round 2 PASS verdicts are therefore undisturbed; no new evidence about them arose in this round beyond their unchanged state.

**Duplicate divergence — exact statement.** `weekly-report-w46-de-core/` is a duplicate directory of the zh-cn edition, not a 12th edition. It was NOT re-synced and now diverges from the canonical zh-cn edition as follows — file by file, the duplicate differs in exactly the 4 artifact files (its KIT differs in framing text, as in Round 2, and was not changed):

| File in `de-core/` | State | Defect |
|---|---|---|
| `svg/p8-uebungen.svg` | Round 2 state (sha256 `89e34350…`) | Still carries D-R2-1: `…schaue ich da` / `sNFL-Spiel.`; also the v2 `begonne`/`n）` and `beginn`/`t置尾` splits |
| `cards/p8-uebungen.png` | Round 2 state | Renders the `sNFL` split (card hash = snapshot) |
| `Die-Lucerna-VOL3.pdf` (print) | Round 2 state (16,578,272 bytes) | Text layer contains `sNFL` ×1 (verified: `pdf-core-print.txt`, 47,665 bytes) |
| `Die-Lucerna-VOL3-web.pdf` (web) | Round 2 state (1,670,976 bytes) | Same defective text layer (Round 2 web/print equality held) |
| `2026-w46-de-zh-cn.text.md` | **Byte-identical to the fixed edition** (`7feaf88c…`, 37,769 bytes) | No divergence — the export is wrap-insensitive and was always correct |
| `ABSTRACT.txt`, other 7 SVGs/cards | Byte-identical to the fixed edition | No divergence |

**The duplicate must not be shipped, and must not be shipped in place of the fixed zh-cn edition.** Insert-process check: `tools/insert.py` reads ONLY the `--edition-dir` passed to it (web PDF + `<slug>.text.md` + `ABSTRACT.txt` from that dir) and contains no reference to `de-core` — but it contains NO guard against being pointed at the duplicate either, and the duplicate would satisfy all its file checks (it holds a single `*web*.pdf`, a non-empty `2026-w46-de-zh-cn.text.md` with the correct slug name, and an `ABSTRACT.txt`). Shipping safety therefore depends entirely on the coordinator passing the canonical dir. **This could not be verified further:** no insert invocation naming the duplicate was found in the searched Round 2 / fix-round-3 records, but no workflow-wide guarantee was in scope to check — if a coordinator-side process ever passes `--edition-dir …/de-core`, the defective P8 would ship silently. The duplicate must be re-synced (coordinator decision — NOT done here, per the brief: the proofreader must not re-sync it) or clearly quarantined before any insert step runs. Note the duplicate currently also has a DIFFERENT defect profile from the fixed edition: it has D-R2-1 but NOT D-R3-1/D-R3-2 (0 occlusion flags) — neither version is shippable as-is.

## 6. Keys (regression spot-check; Round 2 verified 150/150 semantically)

Per scope, no full semantic re-verification was required; p8.py CLEAN (§4) plus spot-confirmation:

- Key 16: `Der Karneval hat in Köln begonnen.` — fixed zh-cn = EN = core extract (identical in all three; only the line breaking differed).
- Key 79: `Köln feiert, weil die Karnevalssession beginnt.` — fixed zh-cn = EN = core extract.
- Key 140: `Am Sonntag schaue ich das NFL-Spiel.` — fixed zh-cn = EN; core extract `Am Sonntag schaue ich da sNFL-Spiel.` is the rendering defect, not a different key.

Any p8 failure would have been blocking; there is none. No new key defect was found. (Full 150-key semantic verification stands as Round 2 §6; nothing in this round disturbs it — the key stream is unchanged per the freeze multiset + p8 extracts.)

## 7. New / residual defects (complete list)

| ID | Severity | Location | Defect | Evidence |
|---|---|---|---|---|
| **D-R3-1** | **BLOCKING** | zh-cn P8 keys block, col-2/col-3 seam, baselines y=2523.12/2527.18 | Real overprint: col-2 line ink to x=1065.2 (104.2px past column edge 961) overprints col-3 head `15:30） · 124. A…`; glyphs jumbled (`15:30)Falsch 124. A`) | Own audit JSON (`occlusion/zh-cn-run1.json`); ink boxes (§2.2); own crop `crops/flag2-fixed-2x.png` vs clean `crops/flag2-core-2x.png` |
| **D-R3-2** | **BLOCKING** | zh-cn P8 keys block, col-1/col-2 seam, baselines y=2198.02/2193.96 | Real (minor) overprint: col-1 line ink to x=532.2 (33.2px past column edge 499) collides 5.2×11.7px with col-2 head `später…`; glyphs merged at seam | Own audit JSON; ink boxes (§2.1); own crop `crops/flag1-fixed-2x.png` vs clean `crops/flag1-core-2x.png` |

No other new or residual defects were found in P8 scope: no token splits, no kinsoku hits, no lone punctuation, no key errors, no footer/edge/cover flags, no PDF-text or count defects. All Round 1 items and Round 2 rulings (a)–(g) stand and are NOT re-raised, except the occlusion-discrepancy item itself, which §3 resolves in Round 2's favour. The fix worker's FIX-REPORT §5.1/KIT §7 occlusion sentences are incorrect as a record matter (see §8) but are documentation, not additional shippable-artifact defects.

## 8. Required fix (for the coordinator / fix worker — proofreader does not fix)

1. **Reflow the zh-cn P8 keys block only** (no other page, no other edition, no key-text change): re-break the keys paragraphs so that EVERY keys-block line's true ink stays within its 434px column — specifically the two overlong lines (§2): the `beginnt.…81. Falsch` line (ink ≤ 961) and the `begonnen）…singen` line (ink ≤ 499). The v3 never-split-a-Latin-token rule MUST be retained (reverting to v2 reintroduces D-R2-1 and the key-16/79 splits); the reflow must achieve column discipline by earlier breaks / block reflow, not by re-splitting tokens. Key text, notes, and glosses must remain byte-identical in the joined stream (freeze +0/−0 vs the re-synced core, p8 CLEAN).
2. **Re-gate:** canonical `occlusion_audit.py` to **0 flags on all 8 pages** (the gate as written); kinsoku line-start/line-end + token-split scans to 0; freeze/p8/counts/PDF-text re-run; P8 full-frame + both seam crops re-viewed at full resolution.
3. **Correct the record:** FIX-REPORT §5.1 and KIT §7 must be amended — the 2 flags are NEW Round 3 regressions (not pre-existing), Flag 1 is a real overprint (not an artifact), and the Round 2 0-flag result reproduces on Round 2-state SVGs (no discrepancy). The `occlusion-pref.json` "pre-fix" audit must be annotated as having audited post-fix SVGs (hash evidence §3), or withdrawn.
4. **Duplicate decision (coordinator):** re-sync `de-core/` from the corrected canonical edition (after the reflow passes) or quarantine it so no insert step can be pointed at it (§5). Do NOT ship from the duplicate in the interim.
5. **Round 4:** P8-only independent re-proofread of the reflowed edition (occlusion + kinsoku + p8 + visual seams). The other 10 editions need no re-proofread if they remain byte-identical.

## 9. Gate artifacts (this round)

All under `hidden_files/w46/de-proofread-gates-round3/`:

- `occlusion/zh-cn-run1.json/.log`, `zh-cn-run2.json/.log` (identical; 2 TEXTX flags), `zh-cn-vs-core.json/.log` (NEW=2), `core.json/.log`, `en.json/.log`, `zh-tw.json/.log` (0 flags), `scratch-v2scan.json/.log` (0), `scratch-v3scan.json/.log` (2)
- `freeze/zh-cn.json/.log` (+0/−0 P1–P7, +13/−13 P8, added CJK 0)
- `p8/zh-cn-vs-core.json/.log` (CLEAN, keydiff [140]), `p8/extract-{zh-cn,en,core}.json/.log`
- `counts.json/.log` (150; 10/18/18/18/18/18/12/38)
- `pdf-web.txt`, `pdf-print.txt` (47,665 bytes, byte-identical), `pdf-core-print.txt` (sNFL ×1)
- `scans/round3_scans.py`, `scans/kinsoku-token-scan.log` (0/0/0, 0 splits), `scans/ink-boxes-flag-sites.txt`, `scans/p8-elements-evidence.txt`, `scans/dates-berlin.log`, `scans/pdf-bytes-recheck.log`
- `crops/flag1-fixed-2x.png`, `crops/flag1-core-2x.png`, `crops/flag2-fixed-2x.png`, `crops/flag2-core-2x.png`, `crops/key140-fixed-2x.png`, `crops/key140-core-2x.png` (+ 1× versions), `crops/p8-full-fixed-half.png`, `crops/p8-full-core-half.png`
- `hash-isolation.log` (5 DIFF files, all zh-cn)

## 10. Final verdict

**ROUND 3 FAIL — de-zh-cn blocked by D-R3-1 (severe TEXTX overprint, keys 80–81/124 seam) and D-R3-2 (minor TEXTX overprint, keys 17/58 seam), both NEW regressions introduced by the Round 3 v3 re-wrap. D-R2-1 is CONFIRMED fixed. The other 10 DE editions remain Round 2 PASS and byte-identical. The edition becomes shippable only after the §8 keys-block reflow, a 0-flag occlusion re-gate, record correction, and a P8-only Round 4 re-proofread.**
