# FIX-REPORT — Lucerna Weekly W46 DE, Round 4 fix (D-R3-1 + D-R3-2, de-zh-cn P8 only)

- **Issue:** VOL.3, Mon 2026-11-09 – Sun 2026-11-15. Target German (DE). Press time 2 November 2026.
- **Verdict:** `hidden_files/w46/de-proofread-gates-round3/proofreader-verdict-round3.md` (2026-11-03), ROUND 3 FAIL — de-zh-cn blocked by TWO defects, D-R3-1 + D-R3-2, both NEW overprints introduced by the Round 3 v3 re-wrap; D-R2-1 CONFIRMED fixed; the other 10 editions PASS.
- **Fix worker:** 2026-11-03. Fix applied AT THE SOURCE (this edition's build-dir sources only — see §3) and fully re-rendered. No SVG/PDF was hand-edited. `.text.md` was regenerated from the source manuscript (never hand-edited, never extracted from PDF) and is byte-identical to the Round 3 file.
- **Scope:** ONE edition only — `2026-w46-de-zh-cn` (German target, Simplified-Chinese reader-native), folder `files/weekly-report-w46-de-zh-cn/`, P8 keys block only. The other 10 DE editions are Round 2 PASS and remain byte-identical (verified by hash, §6). `files/weekly-report-w46-de-core/` is a DUPLICATE of the zh-cn edition, not a 12th edition; it was NOT edited and NOT re-synced (coordinator decision after this round — see §7) and now diverges from the canonical edition — report it, do not ship from it. Work dir: `hidden_files/w46/de-fix-round4/` (created for this round). `~/workspace/weekly-git` untouched, `index.json` untouched, SOP untouched, nothing pushed, inserted, or posted to Discord, no edition content dumped into chat, no subagents spawned.
- **Round 3 record adjudicated:** `hidden_files/w46/de-fix-round3/FIX-REPORT.md` (kinsoku v3 — the never-split-a-token rule is RETAINED; this fix works WITH it, §3) + §7 fix record in the zh-cn `WEEKLY-KIT.md`. §1 below CORRECTS the factually wrong occlusion statements in both records, by explicit superseding note — history is not silently rewritten.
- **Result:** D-R3-1 + D-R3-2 fixed; EVERY P8 keys-block line's ink now stays within its 434px column (0 overflowing lines of 100); D-R2-1 stays fixed and the v3 same-class repairs survive. A P8-only Round 4 independent proofread follows — this re-gating does not replace it.

## 1. Record correction (mandatory) — what was wrong, what is correct, evidence

### 1.1 The wrong statements

Round 3 FIX-REPORT §5.1 and KIT §7 (occlusion bullet) stated, in substance and in the quoted words below:

1. FIX-REPORT §5.1: the canonical audit "reports 2 TEXTX flags on `p8-uebungen.svg`, with identical flag texts, boxes and details on the Round 2-state SVGs (audited from the byte-identical scratch rebuild) and on the fixed SVGs" — i.e. **"both pre-existing, byte-identical pre/post fix (0 new flags)"**.
2. FIX-REPORT §5.1, Flag 1: **"Adjudicated on the full-res crop: measurement artifact / benign proximity.** The two column lines are visually separated; the 5.2px is advance/ink-box encroachment into the gutter, with no glyph collision visible." KIT §7 repeats it as "a 5.2px column-seam proximity with visually separated glyphs (crop adjudicated clean)".
3. FIX-REPORT §5.1, Flag 2: **"Adjudicated on the full-res zoom crop: REAL pre-existing overprint.** … The overprinting line's text and position are IDENTICAL in the pre-fix and post-fix SVGs — this fix neither caused nor changed it." KIT §7 repeats it as "a real pre-existing overprint … line identical pre/post fix".
4. FIX-REPORT §5.1 / KIT §7: **"The Round 2 verdict's occlusion claim (0 flags on every edition) does not reproduce under the canonical invocation on the Round 2-state SVGs; no explanation for that discrepancy is asserted."**

### 1.2 What is correct (Round 3 proofreader verdict §§2–3, confirmed by this round's own re-runs)

- **Both flags are NEW Round 3 regressions introduced by the v3 re-wrap.** Neither is pre-existing. The v3 change lengthened the two keys-block lines past their columns (D-R3-2 line ink 490.8 → 532.2; D-R3-1 line ink 947.8 → 1065.2, measured on the true Round 2-state vs Round 3 SVGs).
- **Flag 1 is a REAL overprint (minor), not a measurement artifact.** The full-res crop shows the `n` of `singen` and the `s` of `später` sharing pixels (merged `singe[n/s]päter`); the Round 2-state contrast crop shows a clean gutter.
- **The Round 2 0-flag result DOES reproduce on true Round 2-state SVGs. There is no discrepancy.** The canonical audit on a fresh, hash-verified copy of the Round 2-state SVGs returns 0 flags (this round, `occlusion/control-round2.json`, exit 0, selftest OK — §4). Round 2's 0-flag finding was correct for the state it audited.

### 1.3 Evidence (hash + mtime, re-verified by this fix worker 2026-11-03, read-only)

- The Round 3 pre-fix snapshot (`de-fix-round3/pre-fix-hashes.json`) pins the zh-cn P8 at sha256 `89e3435000510b47c9fc6a8585df654e76f7fd843f935b2571f9ca26ca934f84` — identical to the de-core duplicate P8. That is the true Round 2 state: its lines carry the v2 splits (`…schaue ich da` / `sNFL-Spiel.`; `begonne` / `n）`; `beginn` / `t置尾`), and it audits to 0 flags.
- The Round 3 fix worker's "pre-fix" audit input, `de-fix-round3/scratch/svg-out/p8-uebungen.svg`, is sha256 `df4fd5831d8d6da8ce18e1de519158550654de2030fb777abb5c2a2f2b4ee4a4` — the FIXED (Round 3) P8, not the Round 2 P8. Its mtime (2026-11-03 05:47:02 UTC) precedes `occlusion-pref.json` (05:51:28 UTC). The two flags in `occlusion-pref.json` name the v3-repaired lines (`begonnen） · 17.…`, `beginnt.（beginnt置尾） · 80.…`), which do not exist in the v2 SVGs. The "pre-fix" audit therefore measured post-fix SVGs and was mislabelled as pre-fix; `occlusion-pref.json` is not evidence about the Round 2 state at all.
- Corroboration from the fix worker's own scan pair (hashes re-verified): `scratch/svg-v2scan/p8-uebungen.svg` = `89e34350…` (Round 2 state) → 0 flags; `scratch/svg-v3scan/p8-uebungen.svg` = `df4fd583…` (fixed state) → 2 flags, identical texts/boxes to the Round 3 edition. The flags track the code version (v2→v3), not the audit invocation.
- **No intent is asserted** about how the scratch directory came to hold post-fix SVGs (the proofreader did not assert intent, and neither does this report). What is established is the hash + mtime + flag-text evidence above.
- **Correction applied in the record:** a superseding correction note quoting the wrong statements was appended to KIT §7 (earlier §7 text left as written), a new KIT §8 Round 4 record was appended, and this §1 is the correction in the fix record. The v3 wrap rule itself is NOT impugned by this correction — it is retained (§3); only the occlusion attribution/adjudication is corrected.

## 2. The defects (D-R3-1 + D-R3-2, BLOCKING, zh-cn P8 only, render/wrap-only)

Both in `svg/p8-uebungen.svg`, keys block, columns starting x = 65 / 527 / 989 / 1451, width 434 (right edges 499 / 961 / 1423 / 1885). Geometry from the shipped Round 3 SVG, true-ink boxes (canonical `occlusion_audit.py` ink measurement, PIL/FreeType `getbbox` at 4×):

**D-R3-1 (SEVERE):** col-2 line (x=527, baseline y=2523.12):

```text
beginnt.（beginnt置尾） · 80. Richtig（11 月 9 日巴伐利亚也复课） · 81. Falsch
```

Advance 538.3px in a 434px column; ink box `[527.0, 2510.6, 1065.2, 2526.6]`, i.e. **104.2px past its 961 column edge**, overlapping col-3's `15:30） · 124. A（纪念日 11 月 15 日） · 125. B（…` (baseline y=2527.18) by **76.2×12.2px**. Full-res crop shows jumbled glyphs (`15:30)Falsch 124. A`); items 81 and 124 are garbled at the seam.

**D-R3-2 (MINOR, still blocking):** col-1 line (x=65, baseline y=2198.02):

```text
begonnen） · 17. Die Kinder haben Martinslieder gesungen.（singen
```

Advance 467.2px in a 434px column; ink right x=532.2, i.e. **33.2px past its 499 column edge**, overlapping col-2's `später（15:30 晚于 11:11）） · 58. leiser…` line by **5.2×11.7px**. Full-res crop shows the `n` of `singen` and the `s` of `später` sharing pixels.

**Full-scan finding (this round, before the fix):** SIX keys lines in the Round 3 state had ink past their column edges, not just the two flagged ones — the two flagged lines above, plus four gutter encroachments of 2–19px that raised no TEXTX flag (no neighbouring ink in range): col-2 y=2485.42 inkR 963.0 (edge 961); col-3 y=2292.27 inkR 1435.0 (edge 1423); col-4 y=1977.9 inkR 1890.5 (edge 1885); col-4 y=2204.1 inkR 1904.2 (edge 1885). The Round 2 state had a similar six-line gutter profile (different lines, max 19px past an edge, 0 flags) — gutter encroachment within the 28px SEAM_SLACK pitch is tolerated by the occlusion gate, but the Round 4 brief requires EVERY keys line's ink inside its column, so the fix below brings all six inside. No key text, note, or gloss is wrong in any of these lines; the defect is wrap/reflow-only. **Origin: not asserted** for D-R3-1/D-R3-2 beyond the established v3-rewrap mechanism (the re-wrap moved whole tokens `begonnen）` / `beginnt.` onto the lines, lengthening their ink 41.4px / 117.4px vs the Round 2 state). No origin is asserted for D-R2-1 either (as in Rounds 2–3).

## 3. The fix (Round 4, source only, zh-cn build only, v3 rule RETAINED)

**Why the overflow existed:** `wrap()`'s greedy pass respects `max_w`, but the kinsoku passes grow lines afterwards — the final START-then-END polish sweep never re-measures, so a line can end past `max_w` (and, via the 28px SEAM_SLACK, past its column into the next column's ink). The v3 shed/join primitives are correct; they were simply never applied as a final width enforcement.

**Files changed (source only, this edition's build dir `hidden_files/weekly-report-w46-de-zh-cn-build/`):**

1. `svglib.py` — two new helpers + one gated call, nothing else:
   - `_discipline_shed_piece(ln, ns)`: the v3 `_kinsoku_shed_piece` result, extended leftwards so the remaining line never ends with an opening bracket (NO_END) and the piece never starts with closing punctuation (NO_START). Still a suffix of the line; still never splits a Latin token.
   - `_enforce_column_width(lines, kind, bold, size, max_w)`: after the kinsoku passes, shed trailing pieces forward (whole Latin tokens only, via the v3 primitives, rejoined with `_kinsoku_join_piece`) until EVERY line's advance width fits `max_w`, cascading forward; appends a line if the last line overflows. Converges (each shed shortens the line by ≥1 glyph; guard raises if it ever did not).
   - `wrap(text, kind, bold, size, max_w, strict=False)`: the discipline pass runs ONLY when `strict=True`. Default off — every non-strict caller is byte-identical to before.
2. `bslib4.py` — `Flow.para(..., strict=False)` threads the flag to its `wrap()` call. Default off.
3. `content8.py` — the P8 keys paragraphs ONLY pass `strict=True` (`kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9, strict=True)`). Keys headers, the battery flow, and all other pages use the default.

No content string, no other build file, no other build dir was touched. The v3 helpers `_kinsoku_shed_piece` / `_kinsoku_join_piece` are byte-identical to the Round 3 state (verified by diff against the pre-fix copies); the frozen-core build still carries v2 (untouched — the duplicate was not re-synced).

**Verification before touching the real build:** the fix was implemented in a scratch copy of the build (`de-fix-round4/scratch/build-strict/`, OUT repointed), rebuilt there first: P1–P7 SVGs byte-identical to the shipped Round 3 files, P8 only changed, 0 FLOW OVERFLOW / HEAD TOO WIDE warnings, occlusion 0 flags. The identical three edits were then applied to the real build dir (diff: real `svglib.py`/`bslib4.py` == scratch copies; real `content8.py` differs from the scratch copy ONLY in its OUT line). The real rebuild's SVGs are byte-identical to the scratch build's SVGs (all 8 pages).

**After (SVG elements, quoted verbatim from the rebuilt file):**

```text
# D-R3-2 site, col-1 (x=65):
y=2198.02  begonnen） · 17. Die Kinder haben Martinslieder
y=2216.87  gesungen.（singen→ gesungen） · 18. Wir haben eine Laterne

# D-R3-1 site, col-2 (x=527):
y=2523.12  beginnt.（beginnt置尾） · 80. Richtig（11 月 9 日巴伐利亚也复
y=2541.97  课）· 81. Falsch（灯笼游行在晚上） · 82. Richtig（孩子们唱圣
```

Re-breaks only, at word/token boundaries per the v3 rule; no token split, no key text/note/gloss change (the `课）· 81.` join has no space before `·`, the same rendering form as the shipped `数））· 149.` line — a break-placement artifact, not a content change; p8.py extraction is unaffected, §4).

## 4. Verification — geometry (measured from the final SVG)

Full ink-extent scan of ALL keys-block lines (100 lines, 14.5pt, canonical ink measurement via `occlusion_audit.ink_box` + `svglib.text_w`; script `de-fix-round4/scan_final.py`):

| Line | Before (Round 3) | After (Round 4, final) |
|---|---|---|
| D-R3-1, col-2 y=2523.12 | advance 538.3px; ink `[527.0, 2510.6, 1065.2, 2526.6]`; right edge **1065.2** (column edge 961, **+104.2**) | advance 422.2px; ink `[527.0, 2510.62, 949.25, 2526.62]`; right edge **949.25** (961, **11.75 clear**) |
| D-R3-2, col-1 y=2198.02 | advance 467.2px; ink right **532.2** (column edge 499, **+33.2**) | advance 335.8px; ink `[65.0, 2185.52, 401.0, 2201.52]`; right edge **401.0** (499, **98.0 clear**) |

- **Full scan: 0 of 100 keys lines overflow their column.** Max ink width per column: col-1 433.0px, col-2 433.8px, col-3 433.2px, col-4 433.5px (column 434px). All six Round 3 gutter/overflow lines are inside their columns; the reflow pushed overflow nowhere else.
- Keys lines 98 → 100 (+2); P8 text elements 282 → 284. Keys baseline range 1902.5 … 2550.68 (was … 2546.03); last ink bottom ≈ 2555, clear of the footer rule (y=2580) — no footer intrusion (occlusion FOOTER class silent, §5).
- D-R2-1 stays fixed: `das NFL-Spiel.` intact on one line (`y=2166.4`, col-4: `das NFL-Spiel.（看比赛 = das Spiel schauen） · 141. b（Mantel=…`), `sNFL` = 0 occurrences in all 8 SVGs, in `.text.md`, and in both PDF text layers. v3 same-class repairs survive: key 16 `begonnen` whole, key 79 `beginnt` whole, separator spaces `· 16.` / `· 24.` / `· 129.`, `76.` intact on one line (all verified by string presence over the joined P8 text + p8.py extract, §5).

## 5. Re-gate results (final artifacts, 2026-11-03)

Build: `run.py` in the zh-cn build dir — 150 exercises, 0 `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings (`zh-cn-run.log`). Render: `hidden_files/w46/de-zh-cn/render.py` — cards PNG @1950 + print PDF via CairoSVG/pypdf + web PDF via `tools/webpdf.py` (`zh-cn-render.log`, webpdf exit 0). Verify: `verify.py` — TOTAL 150, SVGs byte-identical on re-run, P7 verbatim 8/8, footers/page lines 8/8, MUSTER label present, P8 separators 8 (`zh-cn-verify.log`). `.text.md`: regenerated with the family's `export_textmd.py` (zh-cn-only scratch copy, `export_textmd_zhcn_r4.py`) — byte-identical, see §8.

Tool note: the brief named `tools/freeze_check.py`; no such file exists. The canonical tool is `tools/freeze.py` (SOP §8 / tools README §3) and that is what was run. All gates below use the venv Python `tools/venv/bin/python` with the canonical shared tools. Exact commands (run from `~/workspace/goals/lucernaread-social-media-operations/tools` unless noted):

```bash
./venv/bin/python tools/occlusion_audit.py --selftest
./venv/bin/python tools/occlusion_audit.py ../files/weekly-report-w46-de-zh-cn/svg --json <round4>/occlusion/final.json
./venv/bin/python tools/occlusion_audit.py ../files/weekly-report-w46-de-zh-cn/svg --core ../files/weekly-report-w46-de-core/svg --json <round4>/occlusion/final-vs-core.json
./venv/bin/python tools/occlusion_audit.py <round4>/control/svg-round2 --json <round4>/occlusion/control-round2.json
./venv/bin/python tools/freeze.py diff --core-svg ../files/weekly-report-w46-de-core/svg --edition-svg ../files/weekly-report-w46-de-zh-cn/svg --strict-cjk --json <round4>/freeze-final.json
./venv/bin/python tools/p8.py compare --core-p8 ../files/weekly-report-w46-de-core/svg/p8-uebungen.svg --edition-p8 ../files/weekly-report-w46-de-zh-cn/svg/p8-uebungen.svg --total 150 --json <round4>/p8-final.json
```

| Gate | Result |
|---|---|
| Occlusion, canonical (`tools/occlusion_audit.py`, selftest OK: all 6 planted classes fired, clean controls silent) | **0 flags on all 8 pages** — two runs, byte-identical JSONs (`occlusion/final.json`, `occlusion/final-run2.json`, exit 0). **0 NEW vs core** (`--core` comparison, `occlusion/final-vs-core.json`, exit 0, `new_flag_count: 0`). |
| Occlusion control (pre-fix / Round 2 state) | Fresh copy of the de-core SVGs, hash-verified before auditing (P8 sha256 `89e34350…` = the pre-fix snapshot hash): **0 flags** (`occlusion/control-round2.json`, exit 0). Confirms the flags were new-vs-Round-2 (pre-fix 0, post-fix 0 after this reflow). The overwritten Round 3 scratch dir was NOT reused for this control. |
| Freeze (`tools/freeze.py diff --strict-cjk`, vs unfixed core duplicate) | exit 0; P1–P7 **+0/−0** strings; P8 **+30/−28** strings; TOTAL added CJK **0** (`freeze-final.json/.log`). Vs the Round 3 state: P1–P7 +0/−0, P8 +23/−21, added CJK 0 (`freeze-r3-to-r4.json/.log`) — reflow only. |
| P8 (`tools/p8.py compare --total 150`, vs unfixed core duplicate) | **CLEAN 150/150**, missing=[], extra=0, uncertain=[]; **keydiff [140]** — the D-R2-1 correction itself (returns to [] if the duplicate is re-synced). Extracts: keys 16/79/140 text-identical to the EN fan-out (`p8-extract-zhcn.json` vs `p8-extract-en.json`): 16 `Der Karneval hat in Köln begonnen.`; 79 `Köln feiert, weil die Karnevalssession beginnt.`; 140 `Am Sonntag schaue ich das NFL-Spiel.` |
| Kinsoku (proofreader's `round3_scans.py`, re-run on final SVGs) | 0 line-start hits, 0 line-end hits, 0 lone-punctuation elements, S1-signature lines 0 (`kinsoku-token-scan-final.log`). The 7 lowercase-fragment line pairs are ALL whole-word wraps at spaces (e.g. `…Karnevalssession` / `beginnt.…`; `…ich` / `das NFL-Spiel.…`; `…Martinslieder` / `gesungen.…`) — 0 mid-word splits. |
| Token-split scan (token-stream walker over every `wrap()` call, adapted Round 3 `token_scan2.py`, run on a fresh copy of the FINAL build dir, whose SVGs equal the shipped finals) | **351 distinct `wrap()` calls, 0 violations, 0 mismatches** (`token-scan-final.json` = `[]`). The v3 never-split-a-token rule holds under the discipline pass. |
| Counts (proofreader's `count_exercises.py`) | zh-cn: 149 numbered + item 150 = **150**; per-page **10/18/18/18/18/18/12/37** (+150 on P8 = 38); level chips A2 57 / B1 70 / B2 14 / 8 untagged (113–120) — identical to Rounds 2–3 (`counts.json/.log`) |
| PDF text layer | web == print byte-identical, **47,656 bytes each** (Round 3: 47,665 — the 9-byte difference is re-break placement in extraction; web/print equality is the gate and it holds); `sNFL` 0; `das NFL-Spiel` 3 occurrences; web PDF **1,670,980 bytes ≤ 7 MB**; print PDF 16,578,276 bytes |
| Visual | P8 full frame (half-scale) viewed: clean layout, no footer overflow. Full-res (2×) crops of BOTH seam sites viewed: D-R3-2 site — clean gutter, `später` legible, col-1 tail ends x=401.0, no shared pixels; D-R3-1 site — clean gutter, `81. Falsch` and `124. A` fully legible, no shared pixels. Round 3-state contrast crop (same pipeline, same region) shows the `15:30)Falsch 124. A` jumble, confirming the defect and the fix in one pipeline. Full-res crop of the key-140 block viewed: `das NFL-Spiel.` intact, no overflow/overlap. Crops in `de-fix-round4/crops/`. |

## 6. Change isolation (hash proof vs Round 3 state)

Pre-change snapshot: `de-fix-round4/round3-state-hashes.txt` (sha256 of every file in all 12 DE edition dirs, taken before any change; zh-cn P8 `df4fd583…`, core P8 `89e34350…`, `.text.md` `7feaf88c…`). Post-fix comparison (after rebuild + re-render + `.text.md` regen + KIT append):

- **Changed, zh-cn only (4 artifacts + KIT):** `svg/p8-uebungen.svg`, `cards/p8-uebungen.png`, `Die-Lucerna-VOL3-ZH-CN.pdf` (print), `Die-Lucerna-VOL3-ZH-CN-web.pdf` (web), plus `WEEKLY-KIT.md` (§7 correction note + §8 record appended; §§1–6 and the §7 record text untouched — the wrong sentences remain visible in §7 and are quoted in the correction note).
- **Unchanged in zh-cn:** the other 7 SVGs, the other 7 cards, `ABSTRACT.txt`, and `2026-w46-de-zh-cn.text.md` (byte-identical).
- **Byte-identical, all 10 other editions + the de-core duplicate:** `de-en, -es, -fr, -it, -ja, -ko, -nl, -pt, -ru, -zh-tw`, and `de-core` (every file; the duplicate's P8 SVG is still `89e34350…`).
- SVG text-multiset diff (zh-cn, Round 3 → Round 4): P1–P7 identical; P8 differs only in the re-broken keys-block lines (+23/−21 strings, same element family, +2 elements for the two added lines; same key text — only line-break placement, plus break-placement spacing at two `·` joins).

## 7. De-core duplicate divergence (reported, not silently shipped)

`weekly-report-w46-de-core/` was not edited and not re-synced (coordinator decision after this round). Its artifacts are now DIVERGENT from the canonical zh-cn edition in the same 4 artifact files as in Round 3 (its KIT framing differs, as before): the duplicate's P8 SVG, card, and both PDFs still contain the D-R2-1 split (`sNFL` present; its `.text.md` is still byte-identical to zh-cn's, as before). Its defect profile is UNCHANGED by this round: it has D-R2-1 but NOT D-R3-1/D-R3-2 (0 occlusion flags on the Round 2 state). The duplicate must not be counted or shipped separately, and must not be shipped in place of the fixed zh-cn edition. Re-syncing it is a coordinator decision (rebuild the frozen-core build with the same v3 + Round 4 helpers, or copy the fixed zh-cn artifacts) — not taken here, per the brief.

## 8. Regenerated `.text.md` — diff vs Round 3 state

`.text.md` was regenerated with a zh-cn-only run of the family's `export_textmd.py` (AST extraction from this edition's build-dir sources, scratch copy `export_textmd_zhcn_r4.py`; the shared script's other-edition entries were already zh-cn-only in the Round 3 scratch copy, and no other edition's file was touched). Result: **byte-identical to the Round 3 file** — 695 items, **37,769 bytes**, sha256 `7feaf88c756c8567a29c3346e87cee5d05cb78594368a934b2a6423811a87a05`, 1,409 lines, golden sentences 8/8 (`textmd-regen.log`; pre-round copy kept at `de-fix-round4/textmd-pre-round4.md`, `cmp` clean). The export is wrap-insensitive and no content string changed, so a zero diff is the expected and correct outcome. (Stated explicitly with hash proof, per the brief — not a missing regeneration.)

## 9. Final per-edition file inventory (zh-cn only; other editions unchanged)

| File | Bytes | sha256 (prefix) | Note |
|---|---|---|---|
| `2026-w46-de-zh-cn.text.md` | 37,769 | `7feaf88c…` | byte-identical to Round 3; 695 items; golden 8/8; 1,409 lines |
| `Die-Lucerna-VOL3-ZH-CN-web.pdf` (repo-shipped web PDF) | 1,670,980 | `090d0b98…` | ≤ 7 MB; via `tools/webpdf.py`; pdftotext 47,656 bytes |
| `Die-Lucerna-VOL3-ZH-CN.pdf` (print master) | 16,578,276 | `cc0de96c…` | pdftotext 47,656 bytes; web == print byte-identical |
| `svg/p8-uebungen.svg` | 50,551 | `00563008…` | 284 text elements; only P8 SVG changed (Round 3: 50,404 bytes, 282 elements) |
| `cards/p8-uebungen.png` | 1,373,914 | `a2722265…` | re-rendered @1950 |
| `WEEKLY-KIT.md` | (appended) | `d7fdb86e…` | §7 correction note + §8 Round 4 record; §§1–6 + §7 record text untouched |
| `ABSTRACT.txt` | (unchanged) | — | not part of this fix |

Pre-fix inventory for comparison (Round 3 FIX-REPORT §9): `.text.md` 37,769 bytes; web PDF 1,670,966 bytes; pdftotext 47,665 bytes; print PDF 16,578,262 bytes; P8 card 1,335,671 bytes.

## 10. What could NOT be applied / deviations

1. **None within scope.** Every brief requirement was applied: D-R3-1 + D-R3-2 fixed at the source with the v3 rule retained; every keys line's ink inside its column (full scan, not just the two lines); no key text/note/gloss changed; D-R2-1 stays fixed; v3 same-class repairs survive; occlusion 0 flags + 0 NEW vs core + hash-verified pre-fix control 0; record correction in both KIT §7 and this report §1 (with hash/mtime evidence, no intent asserted); freeze/p8/counts/PDF-text re-gates all pass; `.text.md` byte-identical with hash proof; change isolation proved by hash; visual seams + full frame + key-140 block viewed; de-core untouched per the coordinator decision.
2. **P8 keydiff []: not applicable while the core duplicate stays unfixed.** Keydiff is [140] vs the duplicate, for the reason in §5 — the D-R2-1 correction itself. No action taken on the duplicate, per the brief.
3. **No other deviation.** No other edition, family, or file was touched; no origin is asserted for D-R2-1 or intent about the scratch-dir overwrite.

## 11. Records and logs

- This report: `hidden_files/w46/de-fix-round4/FIX-REPORT.md`.
- Logs/JSONs under `hidden_files/w46/de-fix-round4/`: `round3-state-hashes.txt` (snapshot of all 12 DE dirs, pre-change); `zh-cn-run.log` (build, 150, 0 warnings); `zh-cn-render.log` (cards/print/webpdf); `zh-cn-verify.log` (verify.py); `freeze-final.json/.log`, `freeze-r3-to-r4.json/.log`, `freeze-strict.json/.log`; `p8-final.json/.log`, `p8-strict.json/.log`, `p8-extract-zhcn/en.json/.log`; `occlusion/` (`final.json/.log`, `final-run2.json/.log`, `final-vs-core.json/.log`, `control-round2.json/.log`, `strict.json/.log`, `strict-vs-core.json/.log`, `zh-cn-round3.json/.log` (pre-fix 2 flags), `zh-cn-round3-vs-core.json/.log`, `selftest.log`); `counts.json/.log`, `count_exercises_run.py`; `textmd-regen.log`, `textmd-pre-round4.md`; `token-scan-final.json/.log`, `token-scan-strict.json/.log`, `token_scan_r4.py`; `kinsoku-token-scan-final.log`, `kinsoku-token-scan.log`, `round3_scans_final.py`, `round3_scans_r4.py`; `scan_final.log`, `scan_strict.log`, `measure_r3.log`, `measure_r3.py`, `scan_strict.py`, `scan_final.py`; `pdf-web.txt`, `pdf-print.txt`; `crops/` (P8 full frame half-scale, both seam sites fixed + Round 3-state contrast at 2×, key-140 block); `build-before-hashes.txt`; `export_textmd_zhcn_r4.py`; `scratch/` (build-repro: byte-identical Round 3 reproduction; build-strict: fix verified before the real build was touched; build-final: fresh copy of the final build, SVGs equal to shipped finals — do not ship).
- Nothing was pushed, inserted, or posted: work is local only (`~/workspace/weekly-git` untouched, `index.json` untouched, no Discord). A P8-only Round 4 independent proofread follows.
