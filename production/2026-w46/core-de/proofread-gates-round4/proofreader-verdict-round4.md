# Round 4 Proofreader Verdict — Lucerna Weekly 2026-W46, DE edition 2026-w46-de-zh-cn (P8 scope)

**Issue:** Mon 2026-11-09 – Sun 2026-11-15. Target language German, reader-native Simplified Chinese.
**Proofreader:** independent, Round 4. Did not build or fix this edition. Did not edit, re-render, re-sync, push, insert, or post anything. Verdict date: 2026-11-03.
**Scope:** P8 ONLY in ONE edition — `2026-w46-de-zh-cn`, folder `files/weekly-report-w46-de-zh-cn/` — PLUS change-isolation hash checks over the whole DE family and the de-core duplicate check. The other 10 DE editions are Round 2 PASS and were verified byte-identical only (hash level); no fresh full proofread of them was in scope. P1–P7 of zh-cn were verified UNTOUCHED (freeze +0/−0 and hash isolation), not re-proofread.
**Fix record adjudicated:** `hidden_files/w46/de-fix-round4/FIX-REPORT.md` + §§7–8 fix records in the zh-cn `WEEKLY-KIT.md`. The fix worker's numbers were NOT accepted; every measurement below was re-taken by the proofreader from the final artifacts.
**Gate directory (this round, fresh):** `hidden_files/w46/de-proofread-gates-round4/` (all JSONs/logs/crops/scans below live there; the fix worker's gate dir was not reused and no gate JSON of theirs was accepted).
**Rules observed:** `~/workspace/weekly-git` untouched, `index.json` untouched, nothing pushed/inserted/posted, no edition content dumped into chat, no subagents spawned. All gates were re-run by the proofreader with the canonical shared tools (`tools/occlusion_audit.py`, `tools/p8.py`, `tools/freeze.py`, venv Python) plus the proofreader's own measurement scripts in `scans/`.

## Verdict summary

| Question | Ruling |
|---|---|
| D-R3-1 (severe col-2/col-3 overprint, items 81/124) | **FIXED** — line re-broken, ink to x=949.25 (11.75px clear), seam visually clean (§1, §2) |
| D-R3-2 (minor col-1/col-2 overprint, singen/später) | **FIXED** — line re-broken, ink to x=401.0 (98.0px clear), seam visually clean (§1, §2) |
| D-R2-1 (`das` → `da`/`sNFL-Spiel`, key 140) | **STAYS FIXED** — `das NFL-Spiel.` intact, `sNFL` 0 everywhere (§1, §4) |
| Occlusion | **0 flags**, all 8 pages; 0 NEW vs core; Round 2 0-flag control reproduces (§3) |
| Freeze / p8 / kinsoku / token / counts / PDF / .text.md | **ALL PASS** (§5, §6, §9) |
| Change isolation | **CONFIRMED** — exactly the 5 claimed zh-cn files changed (§7) |
| Record correction | **PRESENT AND CORRECT** — superseding note, history intact, hash+mtime evidence, no intent asserted (§8) |
| De-core duplicate | **Divergent, defective, must not ship** — re-sync still owed as a coordinator step (§7) |

**Final verdict line: ROUND 4 PASS — D-R3-1 and D-R3-2 are fixed, D-R2-1 stays fixed, and the DE family is shippable 11/11 from the canonical edition dirs. The de-core duplicate re-sync remains owed as a coordinator step before any insert step is pointed at it (§7); it does not block the verdict on the canonical edition.**

## 1. Ink-extent scan — 0 of 100 keys lines past any column edge (own measurement)

Method: the proofreader's own script `scans/ink_scan_r4.py`, using the canonical `tools/occlusion_audit.py::ink_box` (PIL/FreeType `getbbox` at 4× supersampling — TRUE INK, not advance width) over ALL 100 P8 keys-block lines (every `font-size="14.5"` text element in `svg/p8-uebungen.svg`; 284 text elements total on the page). Columns start x = 65 / 527 / 989 / 1451, width 434 → right edges 499 / 961 / 1423 / 1885. Full per-line table: `scans/ink-scan-r4.json` + `.log`.

| Column | Lines | Max ink width (proofreader) | Max ink right | Min clearance to column edge | Lines past edge |
|---|---|---|---|---|---|
| col-1 (x=65) | 26 | **433.00px** | 498.00 | 1.00px | 0 |
| col-2 (x=527) | 28 | **433.75px** | 960.75 | 0.25px | 0 |
| col-3 (x=989) | 25 | **433.25px** | 1422.25 | 0.75px | 0 |
| col-4 (x=1451) | 21 | **433.50px** | 1884.50 | 0.50px | 0 |
| **Total** | **100** | — | — | — | **0** |

The fix worker claimed 433.0/433.8/433.2/433.5. The proofreader's independent re-measurement agrees to within 0.05px (433.75 vs 433.8; 433.25 vs 433.2) — rounding-level differences in the same measurement, immaterial. The claim "all 100 lines inside columns" is CONFIRMED. No line was pushed into overflow elsewhere: the full 100-line scan, not spot checks, finds 0 overflows. The tightest clearance in the whole block is 0.25px (col-2 `76.` line, ink right 960.75 vs edge 961); it is inside its column, and the neighbouring column starts at x=989, leaving a 28.25px gutter — the occlusion gate (§3) confirms no ink contact. This is a measurement observation, not a defect: the gate as briefed is "ink within its column", and it holds on all 100 lines.

Defect sites, measured (ink boxes, absolute SVG x):

- **Ex-D-R3-1** (col-2, baseline y=2523.12): now `beginnt.（beginnt置尾） · 80. Richtig（11 月 9 日巴伐利亚也复` — ink `[527.0, 2510.62, 949.25, 2526.62]`, width 422.25px, **11.75px clear** of edge 961 (Round 3: right 1065.2, +104.2 past). Remainder on the next line (y=2541.97): `课）· 81. Falsch（灯笼游行在晚上） · 82. Richtig（孩子们唱圣` — ink right 948.75, inside its column. Items 81/124 are on separate, non-overlapping lines; the `15:30） · 124. A` head now sits in col-4 (x=1451, y=1921.35), far from this seam.
- **Ex-D-R3-2** (col-1, baseline y=2198.02): now `begonnen） · 17. Die Kinder haben Martinslieder` — ink `[65.0, 2185.52, 401.0, 2201.52]`, width 336.0px, **98.0px clear** of edge 499 (Round 3: right 532.2, +33.2 past). Remainder (y=2216.87): `gesungen.（singen→ gesungen） · 18. Wir haben eine Laterne` — ink right 490.5, inside its column. The neighbouring col-2 line (y=2193.96) `später（15:30 晚于 11:11）） · 58. leiser…` — ink right 948.25, inside col-2. The two lines no longer share any x-range at the seam.
- **D-R2-1 stays fixed:** col-4 line y=2166.4 `das NFL-Spiel.（看比赛 = das Spiel schauen） · 141. b（Mantel=` — `das NFL-Spiel.` whole on one line. `sNFL` = 0 occurrences in all 8 zh-cn SVGs, in `.text.md`, and in both PDF text layers (§9). Keys 16 (`begonnen` whole, y=2179.17 line `· 16. Der Karneval hat in Köln begonnen.（beginnen →`) and 79 (`beginnt` whole, y=2523.12 line above) whole; separator spaces `· 16.` / `· 24.` / `· 129.` present; `76.` intact on one line (y=2447.72, `76. Die Kinder freuen sich, weil St. Martin kommt.（weil 句动词置`).
- Last keys baseline 2550.68 (col-3), max keys ink bottom 2554.18 — clear of the footer rule (y=2580). No footer intrusion; the FOOTER class is silent in §3.
- Keys lines 98 → 100 (+2); P8 text elements 282 → 284. Both consistent with a two-line reflow, no content change (freeze multiset, §5).

## 2. Visual — full frame + both seam sites viewed at full resolution

Own crops from the shipped card `cards/p8-uebungen.png` (1950×2700), in `crops/`; viewed by the proofreader with their own eyes:

- **Full frame (half-scale, `crops/p8-full-half.png`):** clean overall layout; four-column keys block with visibly clean gutters throughout; exercises, MUSTER box, and footer all in place; no overflow, no footer intrusion, no missing glyphs at frame scale.
- **Ex-D-R3-1 site (2× crop `crops/seam-r3-1-2x.png`, x 480–1450 / y 2470–2575; plus wide 1× `crops/seam-r3-1-wide-1x.png`, x 527–1423 / y 2495–2575):** what I see — col-2 reads `beginnt.（beginnt置尾） · 80. Richtig（11 月 9 日巴伐利亚也复` on one line and `课）· 81. Falsch（灯笼游行在晚上） · 82. Richtig（孩子们唱圣` on the next, each ending well short of the gutter; col-3 reads `117. A（schaut…）`, `119. B（erzählt…）`, `120. A（beginnt…）` on their own lines. The gutter between the columns is empty cream. `81. Falsch` is fully legible; there is no jumble, no shared pixels, no trace of the Round 3 `15:30)Falsch 124. A` overprint.
- **Ex-D-R3-2 site (2× crop `crops/seam-r3-2-2x.png`, x 400–1010 / y 2140–2245; plus wide 1× `crops/seam-r3-2-wide-1x.png`, x 65–1010 / y 2170–2245):** what I see — col-1 reads `begonnen） · 17. Die Kinder haben Martinslieder` and below it `gesungen.（singen→ gesungen） · 18. Wir haben eine Laterne`, both ending well clear of the seam; col-2 reads `später（15:30 晚于 11:11）） · 58. leiser（leise → leiser（空场` with `später` crisp and fully legible. The gutter is clean cream; `singen` and `später` are fully separated — no merged `singe[n/s]päter`, no shared pixels.
- **Key-140 block (2× crop `crops/key140-2x.png`, x 1400–1950 / y 2100–2210):** what I see — `… · 140. Am Sonntag schaue ich` / `das NFL-Spiel.（看比赛 = das Spiel schauen） · 141. b（Mantel=…` — `das NFL-Spiel.` intact on one line, clean, no overflow/overlap.

## 3. Occlusion — 0 flags; Round 2 control reproduces

Canonical `tools/occlusion_audit.py` (venv Python; selftest OK in every run: all 6 planted classes fired exactly once, clean controls silent — `occlusion/selftest.log`):

| Input (own runs) | Result | Evidence |
|---|---|---|
| Final zh-cn SVG dir, run 1 | **0 flags, all 8 pages**, exit 0 | `occlusion/zh-cn-run1.json/.log` |
| Final zh-cn SVG dir, run 2 | **Identical JSON** (byte-identical diff), exit 0 | `occlusion/zh-cn-run2.json/.log` |
| Final zh-cn with `--core` = core duplicate | **core 0 flags; NEW vs core: 0**, exit 0 | `occlusion/zh-cn-vs-core.json/.log` |
| Hash-verified Round 2-state control | **0 flags**, exit 0 | `occlusion/control-round2.json/.log` |

Pre-fix control (the rule from the brief, applied strictly): the control SVGs are a fresh copy of the de-core duplicate's SVGs, copied into `occlusion/control-round2-svg/` and hash-verified BEFORE auditing — P8 sha256 `89e3435000510b47c9fc6a8585df654e76f7fd843f935b2571f9ca26ca934f84`, equal to the Round 3 pre-fix snapshot hash for both the core and zh-cn P8 in `de-fix-round3/pre-fix-hashes.json` and to the Round 4 `round3-state-hashes.txt` core entry (`occlusion/control-hash-verify.log`). No scratch dir was audited without hash verification. **The Round 2 0-flag result reproduces on the true Round 2 state: confirmed for the third consecutive round. There is no Round 2 occlusion discrepancy.** The fix worker's control claim is independently confirmed, not merely repeated.

No other flag class fired anywhere (no COVER/LINEX/FOOTER/EDGE/BOXTITLE). The six Round 3 gutter encroachments named in the FIX-REPORT are all inside their columns in the final state per §1; the occlusion gate and the stricter column-discipline brief both pass.

## 4. Keys integrity — full 150-key semantic verification (REQUIRED for this round)

Every P8 key letter/answer was verified against the issue's own content: the proofreader read all P1–P7 prompt text and the P8 prompt sections (A–H) in full from the shipped SVGs, and checked every matching-block option-by-option, every cloze/fill key against German grammar and the article facts, and recomputed every arithmetic key. `p8.py` was supplement only. Full per-group reasoning and the complete extracted key list: `scans/keys-audit-r4.md`.

- **150/150 verified, 0 wrong keys, 0 transpositions.** Matching blocks: 25–28 (c/a/b/d), 52–55 (b/a/c/d), 141–144 (b/a/d/c) — each option text matches its definition list. Cloze/agreement keys 113–120 and dialogue keys 145–149 checked person-by-person against their subjects/pronouns (e.g. 118 `sieht` for irregular *sehen*, 146 `macht` for *ihr*, 147 `essen` for *wir*). Sentence-building keys 43–46/133–136 checked for verb-second order. *weil/dass/ob* keys 76–79/107/111 checked for verb-final order. Arithmetic recomputed: 85 → 46+34=**80** ✓; 88 → 46+34+20=**100** ✓; P2 time arithmetic in the article (11.11+6h≈17h; 15.30−11.11=4h19; 9–15 Nov=7 days) consistent with keys 11–15.
- **Key 140** `Am Sonntag schaue ich das NFL-Spiel.` — intact, and **text-identical to the EN fan-out** (see §5). The Chinese→German translation is correct (time-fronted, verb second, *schaue* = 看).
- **Keys 16/79 whole:** 16 `Der Karneval hat in Köln begonnen.`; 79 `Köln feiert, weil die Karnevalssession beginnt.` — both text-identical to the EN fan-out. **`76.` intact** on one line (§1). **`sNFL` 0 everywhere** in the canonical edition (SVGs, `.text.md`, both PDF text layers).
- Cross-edition diffs (measured from the proofreader's own `p8.py extract` JSONs, `p8/extract-{zhcn,en,core}.json`): zh-cn vs EN differ ONLY in 137/138/139 (Chinese translations — legitimate native labels) and 150 (open-task label `开放题` vs `Open task`); 146/150 keys identical. Zh-cn vs core duplicate differ ONLY in 140 (the D-R2-1 rendering defect in the duplicate). A transposed key would appear in these diffs; none does, and the semantic check independently confirms each key against its own prompt.

## 5. Freeze + P8

Own runs, canonical tools:

| Gate | Result | Evidence |
|---|---|---|
| Freeze `freeze.py diff --strict-cjk` (zh-cn vs core duplicate) | **exit 0.** P1–P7 **+0/−0** strings; P8 **+30/−28** strings; TOTAL added CJK **0** | `freeze/zh-cn-vs-core.json/.log` |
| Freeze +30/−28 content | Re-break placement only: the added/removed strings are the same keys-block lines re-broken (incl. `sNFL-Spiel.` → `das NFL-Spiel.`, `begonne`/`n）` → `begonnen）`, `beginn`/`t置尾` → `beginnt.…`, restored `· 16.`/`· 24.`/`· 129.` spaces). CJK totals identical per page (P8 1389 → 1389). No key text, note, or gloss changed. | `freeze/zh-cn-vs-core.json` (verified pair-by-pair) |
| P8 `p8.py compare --total 150` (zh-cn vs core) | **CLEAN 150/150**, missing=[], extra=0, uncertain=[]; **keydiff [140]** — the D-R2-1 correction itself | `p8/zh-cn-vs-core.json/.log` |
| P8 `p8.py compare --total 150` (zh-cn vs EN fan-out) | **CLEAN 150/150**; **keydiff [137, 138, 139, 150]** — only the legitimate native-translation labels (§4). Key 140 is NOT in this diff: it equals EN exactly. | `p8/zh-cn-vs-en.json/.log` |
| P8 extracts | Noted sets 150/150 in zh-cn, EN, and core alike | `p8/extract-{zhcn,en,core}.json/.log` |

**Adjudication of keydiff [140]:** it is the D-R2-1 correction versus the unfixed duplicate only, as claimed. Proof: against the PASS EN fan-out the keydiff is [137, 138, 139, 150] with no 140 — i.e. zh-cn's key 140 is the correct, shared key, and the duplicate's rendering is the outlier. The keydiff returns to [] if/when the duplicate is re-synced; that re-sync is a coordinator step, not a condition on this verdict.

## 6. Kinsoku / token — 0 violations; v3 rule holds

Own script `scans/kinsoku_token_r4.py` (fresh code; kinsoku-token-scan log `scans/kinsoku-token-scan-r4.log`), over all 8 pages of the final zh-cn SVGs:

- Line-start hits **0**, line-end hits **0**, lone-punctuation elements **0**, S1-signature lines **0**.
- Lowercase-fragment line pairs: **7**, ALL adjudicated whole-word wraps at spaces (each following line starts with a complete word: `gesungen.`, `gebastelt.`, `beginnt.`, `dunkel`, `fraglich,`, `ganz`, `das` — none is a continuation fragment of the previous line's final word). **0 mid-word splits** in the whole edition.
- Token-split check over `wrap()` outputs: direct import of the live zh-cn build `svglib.wrap` (import only, no rebuild) — signature confirms `strict=False` default; on Latin test strings containing `das NFL-Spiel.`, `begonnen`, `beginnt.`, 0 token violations in both strict and non-strict modes; on a long keys-like paragraph, non-strict wrap produced 2 lines over 434px advance while strict wrap produced 0 over (17 lines, max advance 428.0px) with no token split — the discipline pass enforces width by whole-token shedding, as designed.
- Build-diff confirmation (see §7): the v3 helpers `_kinsoku_shed_piece` / `_kinsoku_join_piece` are byte-identical to the Round 3 state (no diff hunks in that region); the Round 4 code only ADDS the discipline helpers and a gated call. The v3 never-split-a-Latin-token rule still holds after the reflow, on shipped-artifact evidence (§1 + this scan) and on code evidence.

## 7. Change isolation — exactly 5 files; duplicate divergent

Fresh full sha256 comparison (252 files, all 12 DE edition dirs) by the proofreader against the fix worker's pre-change snapshot `de-fix-round4/round3-state-hashes.txt` (`hashes/current-hashes.txt`, `hashes/isolation-diff.log`): **exactly 5 DIFF files, all in zh-cn, no extra/missing files in any dir:**

1. `svg/p8-uebungen.svg` — `df4fd583…` → `00563008…` (50,551 bytes; 284 text elements)
2. `cards/p8-uebungen.png` — `a2722265…` (1,373,914 bytes)
3. `Die-Lucerna-VOL3-ZH-CN.pdf` (print) — `cc0de96c…` (16,578,276 bytes)
4. `Die-Lucerna-VOL3-ZH-CN-web.pdf` (web) — `090d0b98…` (1,670,980 bytes)
5. `WEEKLY-KIT.md` — `d7fdb86e…` (§7 correction note + §8 record; see §8)

Unchanged in zh-cn: the other 7 SVGs, the other 7 cards, `ABSTRACT.txt`, and `2026-w46-de-zh-cn.text.md` (byte-identical, §9). **All 10 other editions byte-identical** to the Round 3 snapshot in every file; **the de-core duplicate byte-identical** to its Round 3 state in every file. P1–P7 are therefore verified untouched, and the other editions' Round 2 PASS verdicts are undisturbed.

**Build diff** (live zh-cn build dir vs the Round 3 build-copy in `de-fix-round3/scratch/build-copy/`, whose `svglib.py` hash `2ff28e12…` equals the fix worker's own build-before snapshot — `scans/build-diff-r3-to-r4.log`): `svglib.py` gains only `_discipline_shed_piece` + `_enforce_column_width` + the gated `if strict:` call; `bslib4.py` gains only the `strict` parameter threading; `content8.py` gains only `strict=True` on the P8 keys paragraph (its other diff hunk is the OUT path, a pre-existing scratch-copy artifact, as in `content12/34/56/7.py`, which differ ONLY in that OUT line). No content string, no other build file, and no other edition's build dir was touched by this fix as far as the shipped artifacts show. (The fix worker's `scratch/build-repro/` copies already contain the Round 4 code and were therefore NOT used as the pre-fix baseline; the Round 3 `build-copy/` + build-before hashes were.)

**Duplicate divergence — exact statement.** `weekly-report-w46-de-core/` was NOT re-synced (coordinator decision, held). It still carries D-R2-1 and must not ship: P8 SVG sha256 `89e34350…` (Round 2 state), card `2c4a53cc…`, web PDF `808aca78…`, print PDF `51ece005…`; `sNFL` ×1 in its P8 SVG and ×1 in its web-PDF text layer (47,665 bytes, `pdf-core-web.txt`); its `.text.md` is byte-identical to the fixed edition's (wrap-insensitive export). Its defect profile is unchanged by this round: D-R2-1 present, D-R3-1/D-R3-2 absent (0 flags on the Round 2 state, §3). **Re-sync (or quarantine) of the duplicate remains owed as a coordinator step before any insert step runs** — the proofreader did not re-sync it, per the brief. This does not block the PASS on the canonical edition, but the coordinator must ensure no insert invocation is ever pointed at `de-core/`.

## 8. Record correction — present, correct, history intact

Read in full: zh-cn KIT §§7–8 and FIX-REPORT §1. All 17 programmatic string checks pass (see `scans/record-correction-evidence.log` for the mtime/hash re-verification):

- **Correction present as an explicit superseding note:** KIT §7 ends with a bold-headed correction note — "CORRECTION to this §7 (Round 4, 2026-11-03 — explicit superseding note; the §7 text above is left as written and is corrected here, not silently rewritten)" — followed by the verbatim wrong quotations and the correct statements. A new KIT §8 Round 4 record was appended. FIX-REPORT §1 (§§1.1–1.3) carries the same correction in the fix record.
- **Original wrong statements quoted and left as written:** the §7 occlusion bullet still reads, verbatim, "BOTH pre-existing and byte-identical … i.e. 0 new flags", "a 5.2px column-seam proximity with visually separated glyphs (crop adjudicated clean)", "a real pre-existing overprint … line identical pre/post fix", and "The Round 2 verdict's 0-flag occlusion claim does not reproduce…". The bullet precedes the correction note in file order (offsets verified). History was not rewritten.
- **Hash+mtime evidence stated, and independently re-verified by the proofreader:** the snapshot pins the Round 2 P8 at sha256 `89e34350…`; the Round 3 "pre-fix" audit input `scratch/svg-out/p8-uebungen.svg` is sha256 `df4fd583…` (the fixed P8 — re-hashed by the proofreader), mtime 2026-11-03 05:47:02, preceding `occlusion-pref.json` (05:51:28 — re-listed by the proofreader); its flags name the v3-repaired lines. The correction states all of this.
- **No intent asserted:** both the KIT note and FIX-REPORT §1.3 state "No intent is asserted about how the scratch directory came to hold post-fix SVGs." No intent is asserted anywhere in the corrected record.
- If any of this had been missing, incomplete, or history-rewriting, it would have been a defect. It is none of those: **the record correction is complete and correct.**

## 9. Counts + text layer

Own count script `scans/count_r4.py` (fresh code; `scans/counts-r4.log`, `scans/counts-r4.json`):

- **150 total:** 149 numbered prompt items, continuous 1–149, plus item 150 (the open writing task, confirmed by the p8 extract noted set 150/150). Per-page prompt counts **10/18/18/18/18/18/12/37** (+ item 150 on P8 = **38**). Identical to Rounds 2–3.
- **A2 chip-count adjudication (57 vs registry 66) — measured explanation, not a repetition:** the shipped-SVG chip scan gives per-item levels **A2 57 / B1 70 / B2 14 / 8 untagged (113–120)** — reproduced exactly by the proofreader's independent count. The registry figure 66 is ALSO correct, on a different counting basis, and the two reconcile exactly (Round 2 §3(g) reconciliation, re-verified by the proofreader from the frozen core build sources, read-only): the 8 untagged cloze items 113–120 are registry A2×6 (113, 114, 115, 116, 117, 119) + B1×2 (118, 120) per `cloze_defs` in `content8.py`; dialogue items 145–147 carry a shipped B1 group chip but are registry A2 per `ddefs`; item 150 is registry B1 with no chip. Hence A2 = 57 + 6 + 3 = **66**; B1 = 70 − 3 + 2 + 1 = **70**; B2 = 14. Both numbers are correct under their stated bases; neither is a defect. The FIX-REPORT's presentation ("chips A2 57/B1 70/B2 14/8 untagged — registry said A2 66") is accurate as far as it goes; the full reconciliation above is the adjudication. No count defect.
- **PDF text layer:** `pdftotext` on the final web PDF → **47,656 bytes > 0**, 8 pages (`pdfinfo`: Pages 8); web PDF **1,670,980 bytes ≤ 7 MB**. Web extract vs print extract: **byte-identical** (47,656 bytes each, `cmp` clean — what was compared: the default-layout `pdftotext` extracts of `Die-Lucerna-VOL3-ZH-CN-web.pdf` and `Die-Lucerna-VOL3-ZH-CN.pdf`, saved as `pdf-web.txt` / `pdf-print.txt`). `sNFL` 0 in both; `das NFL-Spiel` ×3 in the web extract. The 9-byte difference vs the Round 3 extracts (47,665) is re-break placement in extraction; web/print equality is the gate and it holds.
- **`.text.md`:** **byte-identical to Round 3** — 37,769 bytes, sha256 `7feaf88c756c8567a29c3346e87cee5d05cb78594368a934b2a6423811a87a05` (hashed by the proofreader), 1,409 lines, 94 `###` headings. (The "695 items" figure in the fix records was not re-derived from the file's visible structure — same position as Round 3 — and is not relied on; hash identity is the gate, and it holds.)

## 10. Non-blocking observations (not defects)

1. Tightest column clearance 0.25px (§1, `76.` line) — inside its column, 28.25px gutter to the next column, occlusion 0. Noted for the record; no action required.
2. The reflowed line `课）· 81. Falsch…` joins with no space before `·`, the same rendering form as the long-shipped `数））· 149.` line — a break-placement artifact, not a content change; p8.py extraction is unaffected. Noted; no action required.
3. The fix worker's `scratch/build-repro/` copies already contain Round 4 code, so they cannot serve as a Round 3 baseline (the proofreader used the Round 3 `build-copy/` + build-before hashes instead, §7). A record-keeping observation for future rounds, not a defect in this edition.

## 11. Gate artifacts (this round)

All under `hidden_files/w46/de-proofread-gates-round4/`:

- `occlusion/zh-cn-run1.json/.log`, `zh-cn-run2.json/.log` (identical; 0 flags), `zh-cn-vs-core.json/.log` (NEW=0), `control-round2.json/.log` + `control-hash-verify.log` + `control-round2-svg/` (hash-verified Round 2 state, 0 flags), `selftest.log`
- `freeze/zh-cn-vs-core.json/.log` (exit 0; +0/−0 P1–P7; +30/−28 P8; added CJK 0)
- `p8/zh-cn-vs-core.json/.log` (CLEAN, keydiff [140]), `p8/zh-cn-vs-en.json/.log` (CLEAN, keydiff [137,138,139,150]), `p8/extract-{zhcn,en,core}.json/.log`
- `scans/ink-scan-r4.json/.log` + `scans/ink_scan_r4.py` (100-line true-ink scan), `scans/kinsoku-token-scan-r4.log` + `scans/kinsoku_token_r4.py` (0/0/0, 0 splits), `scans/counts-r4.log` + `scans/count_r4.py` + `scans/counts-r4.json`, `scans/keys-audit-r4.md` (150-key semantic verification), `scans/build-diff-r3-to-r4.log` + `scans/build-hash-compare.log`, `scans/record-correction-evidence.log`
- `crops/p8-full-half.png`, `crops/seam-r3-1-2x.png`, `crops/seam-r3-1-wide-1x.png`, `crops/seam-r3-1-1x.png`, `crops/seam-r3-2-2x.png`, `crops/seam-r3-2-wide-1x.png`, `crops/seam-r3-2-1x.png`, `crops/key140-2x.png`
- `pdf-web.txt`, `pdf-print.txt` (47,656 bytes, byte-identical), `pdf-core-web.txt` (sNFL ×1, duplicate evidence)
- `hashes/current-hashes.txt` (252 files), `hashes/isolation-diff.log` (exactly 5 files), `hashes/core-divergence.log`
- This verdict: `proofreader-verdict-round4.md`

## 12. Final verdict

**ROUND 4 PASS — D-R3-1 and D-R3-2 are fixed (keys-block reflow, v3 never-split-a-token rule retained, every one of the 100 keys lines' true ink inside its 434px column), D-R2-1 stays fixed, all regression gates pass, change isolation holds to exactly the 5 claimed zh-cn files, and the Round 3 record correction is present and correct. The DE family is shippable 11/11 from the canonical edition directories. One coordinator step remains owed and does not block this verdict: re-sync or quarantine the de-core duplicate, which still carries D-R2-1 (`sNFL`) and must not be shipped or pointed at by any insert step.**
