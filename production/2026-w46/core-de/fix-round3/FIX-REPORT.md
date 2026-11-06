# FIX-REPORT — Lucerna Weekly W46 DE, Round 3 fix (D-R2-1, de-zh-cn only)

- **Issue:** VOL.3, Mon 2026-11-09 – Sun 2026-11-15. Target German (DE). Press time 2 November 2026.
- **Verdict:** `hidden_files/w46/de-proofread-gates-round2/proofreader-verdict-round2.md` (2026-11-03), ROUND 2 FAIL — de-zh-cn blocked by ONE defect, D-R2-1; the other 10 editions PASS.
- **Fix worker:** 2026-11-03. Fix applied AT THE SOURCE (this edition's build-dir `svglib.py` only) and fully re-rendered. No SVG/PDF was hand-edited. `.text.md` was regenerated from the source manuscript (never hand-edited, never extracted from PDF) and is byte-identical to the pre-fix file.
- **Scope:** ONE edition only — `2026-w46-de-zh-cn` (German target, Simplified-Chinese reader-native), folder `files/weekly-report-w46-de-zh-cn/`. The other 10 DE editions are Round 2 PASS and remain byte-identical (verified by hash, §6). `files/weekly-report-w46-de-core/` is a DUPLICATE of the zh-cn edition, not a 12th edition; it was NOT edited as a separate edition and now diverges from the canonical edition (§7) — report it, do not ship from it. Work dir: `hidden_files/w46/de-fix-round3/` (created for this round). `~/workspace/weekly-git` untouched, `index.json` untouched, SOP untouched, nothing pushed, inserted, or posted to Discord, no edition content dumped into chat, no subagents spawned.
- **Round 1 record adjudicated:** `hidden_files/w46/de-fix/FIX-REPORT.md` (kinsoku v1→v2 token-aware shedding, spacing recoveries). This fix works WITH the v2 wrap behaviour (v3 extends it); no Round 1 fix was disturbed — P1–P7 SVGs are byte-identical to the Round 2 state and the `76.` protection still holds (§4).
- **Result:** D-R2-1 fixed; the whole P8 keys block now satisfies the token-aware rule (0 token splits in all 351 distinct `wrap()` calls). A P8-only Round 3 independent proofread follows — this re-gating does not replace it.

## 1. The defect (D-R2-1, BLOCKING, zh-cn only, render/wrap-only)

Round 2 verdict §5, P8 keys block, items 139–141, `svg/p8-uebungen.svg` (and identically in the de-core duplicate):

Before (SVG elements, quoted verbatim from the shipped Round 2 file):

```xml
<text x="1451" y="2091.0">（wieder begonnen = 又开始） · 140. Am Sonntag schaue ich da</text>
<text x="1451" y="2109.85">sNFL-Spiel.（看比赛 = das Spiel schauen） · 141. b（Mantel=斗…</text>
```

The word `das` is split across lines, producing the non-word `sNFL`. Full-resolution card crop confirmed it. The correct rendering (`140. Am Sonntag schaue ich das NFL-Spiel.` intact) appears in all 10 fan-outs. The key itself is correct (`140. Am Sonntag schaue ich das NFL-Spiel.` with note/gloss `看比赛 = das Spiel schauen` unchanged); `.text.md` showed the correct source string, so the defect is render/wrap-only.

**Origin: not asserted.** Whether the split was pre-existing in renderings before the Round 1 kinsoku v1/v2 wrap changes, or introduced by them, could not be established — no pre-fix SVGs exist — and none is asserted here (per the Round 2 verdict and the fix brief). What WAS established by simulation (§2) is the code path in the shipped v2 wrap code that produces the split. No historical origin is claimed beyond that.

## 2. Root cause (established by simulation on the exact paragraph)

The P8 keys paragraph for page 8 (size 14.5 sans, `max_w` 434) was reconstructed exactly from the build registry (keys string, 1181 chars; the build reproduces the shipped SVGs byte-identically — all 8 pages IDENTICAL on a scratch re-run before any change). Tracing `wrap()` stage by stage:

1. **Greedy wrap: CORRECT.** Line 18 ends `…schaue ich das` (426.5px ≤ 434); line 19 starts `NFL-Spiel.…`. No token is split.
2. **END pass (kinsoku): the split is created here.** Greedy line 17 ends with the opening bracket `（`. The END repair pushes `（` to the head of line 18; the receiving line then exceeds `max_w`, and the shedding loop sheds trailing glyphs forward with the v2 `_kinsoku_shed_piece`, which sheds ONE glyph for a plain trailing Latin word — the `s` off `das`. Line 18 becomes `…schaue ich da` (434.2px); line 19 becomes `sNFL-Spiel.…` (the shed `s` joins with no space, correctly for a word fragment — the fragment itself is the defect).
3. START pass, seam cascade, and final polish leave lines 18/19 untouched.

So the v2 token-aware rule protected only ASCII-punctuated Latin tokens (`76.`); a plain Latin word at the end of an END-pass receiving line was still shed one glyph at a time.

## 3. The fix (v3, source only, zh-cn build only)

File changed (source only): `hidden_files/weekly-report-w46-de-zh-cn-build/svglib.py` — the two kinsoku helpers only. No content string, no other build file, no other build dir (frozen-core build verified still v2: 0 occurrences of the v3 marker). Pre-v3 copy preserved at `de-fix-round3/svglib-v2-before.py`. The diff vs v2 is confined to `_kinsoku_shed_piece` / `_kinsoku_join_piece`:

- `_kinsoku_shed_piece` (v3): NEVER split a Latin token. A trailing Latin word goes whole (`das`, `NFL-Spiel`); a Latin word carrying trailing NO_START punctuation goes whole with the punctuation (`begonnen）`, not `n）`); a trailing ASCII-punctuated Latin token goes whole (v2 `76.` rule, preserved); a trailing CJK glyph (or CJK glyph + NO_START punctuation) sheds as before, since CJK wraps per character.
- `_kinsoku_join_piece` (v3): a whole Latin token rejoining Latin text restores the space the raw wrap consumed at the break (`das` + `NFL-Spiel.` → `das NFL-Spiel.`; v2 punctuated-token case preserved). A piece ending in CJK/NO_START punctuation, or a CJK glyph, joins with no space, as before.

After (SVG elements, quoted verbatim from the rebuilt file):

```xml
<text x="1451" y="2091.0">（wieder begonnen = 又开始） · 140. Am Sonntag schaue ich</text>
<text x="1451" y="2109.85">das NFL-Spiel.（看比赛 = das Spiel schauen） · 141. b（Mantel=…</text>
```

Full key-140 rendering, from the rebuilt P8 SVG (single token, no split):

```text
（wieder begonnen = 又开始） · 140. Am Sonntag schaue ich
das NFL-Spiel.（看比赛 = das Spiel schauen） · 141. b（Mantel=斗篷 b） · …
```

`p8.py extract` on the fixed edition: key 140 = `Am Sonntag schaue ich das NFL-Spiel.` — exactly equal to the EN fan-out's extracted key 140. The unfixed core duplicate extracts `Am Sonntag schaue ich da sNFL-Spiel.`

### Same-class repairs by the same wrap change (whole keys block)

A positional token-split scan (token-stream walker over every `wrap()` call, §4) found that the shipped v2 code produced exactly THREE Latin-token splits in the whole edition, ALL in P8 keys paragraphs. The other two are repaired by the same v3 change; no key text changed in any of them:

| Token | Key | Before (v2 lines) | After (v3 lines) |
|---|---|---|---|
| `begonnen` | 16 (P2 keys block) | `…（beginnen → begonne` / `n） · 17. Die Kinder…` | `…（beginnen →` / `begonnen） · 17. Die Kinder…` |
| `beginnt` | 79 (P6 keys block) | `…Karnevalssession beginn` / `t置尾） · 80. Richtig…` | `…Karnevalssession` / `beginnt.（beginnt置尾） · 80. Richtig…` (line shown in §5 note) |
| `das` | 140 (P8 keys block, D-R2-1) | `…schaue ich da` / `sNFL-Spiel.…` | `…schaue ich` / `das NFL-Spiel.…` |

The Round 2 S1-signature scan (line starting with 1–2 lowercase letters + capital) found only D-R2-1, because the `begonnen`/`beginnt` continuations start with CJK punctuation (`n）`, `t置尾`), not a capital. The fix brief's whole-keys-block scan is what requires all three to be gone. Three `· N.` separators also regained the space the raw wrap had consumed at the break (`· 16.`, `· 24.`, `· 129.` — rendering-fidelity only, same class). Total P8 SVG change: 13 re-wrapped lines, all inside the keys block; element count unchanged (282); P1–P7 SVGs byte-identical.

## 4. Verification — token splits and kinsoku

- **Reproduction before the fix:** scratch copy of the zh-cn build (OUT repointed) rebuilt all 8 SVGs byte-identically to the shipped Round 2 files; the exact keys-paragraph simulation reproduced D-R2-1 and, after patching the scratch copy, verified the fix before the real build was touched.
- **Positional token-split scan** (`de-fix-round3/scratch/token_scan2.py`, run against the real build dir after the fix): token-stream walker aligning every token of every `wrap()` input to its output lines; a token spanning a line boundary = a split. **351 distinct `wrap()` calls, 0 violations, 0 mismatches.** Same scan on the v2 code: exactly the 3 splits in §3. This scan covers every paragraph on all 8 pages, not only P8.
- **Kinsoku re-gate (own line-start AND line-end scans over all 8 rebuilt zh-cn pages):** 0 lines starting with a NO_START glyph (`。、，．！？：；）」』】}),.:;!?`), 0 lines ending with a NO_END opening bracket (`（(［｛〈《「『`), 0 lone-punctuation elements, `sNFL` = 0 occurrences in ALL zh-cn SVGs, in `.text.md`, and in both PDF text layers (see §5). The `76.` token is intact (`76. Die Kinder freuen sich, weil St. Martin kommt.` on one line) — the v2 shedding still holds after the change. The v2 follow-up concern (seam shedding stopping on an opening bracket) is covered by the 0 line-end hits above.

## 5. Re-gate results (final artifacts, 2026-11-03)

Build: `run.py` in the zh-cn build dir — 150 exercises, 0 `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings (`zh-cn-run.log`). Render: `hidden_files/w46/de-zh-cn/render.py` — cards PNG @1950 + print PDF via CairoSVG/pypdf + web PDF via `tools/webpdf.py` (`zh-cn-render.log`, webpdf exit 0). Verify: `verify.py` — TOTAL 150, SVGs byte-identical on re-run, P7 verbatim 8/8, footers/page lines 8/8, MUSTER label present, P8 separators 8 (`zh-cn-verify.log`).

| Gate | Result |
|---|---|
| Kinsoku (own scans, all 8 pages) | 0 line-start hits, 0 line-end hits, 0 lone-punctuation elements |
| Token-split scan (351 wrap calls) | 0 violations (v2: 3) |
| Freeze (`tools/freeze.py diff --strict-cjk`, vs unfixed core duplicate) | exit 0; P1–P7 +0/−0 strings; P8 +13/−13 strings; TOTAL added CJK characters: 0 (`freeze-zh-cn.log/.json`) |
| P8 (`tools/p8.py compare --total 150`, vs unfixed core duplicate) | CLEAN 150/150, missing=[], extra=0, uncertain=[]; **keydiff [140]** — the correction itself (fixed key = EN fan-out key 140 exactly; core extracts `…da sNFL-Spiel.`). See note below. |
| Occlusion (`tools/occlusion_audit.py`, selftest OK, deterministic) | **2 TEXTX flags on P8 — both pre-existing, byte-identical pre/post fix (0 new flags). See §5.1. NOT 0 flags; see the finding.** |
| Counts (proofreader's `count_exercises.py`) | zh-cn: 149 numbered + item 150 = 150; per-page 10/18/18/18/18/18/12/37 (+150 on P8 = 38); level chips A2 57 / B1 70 / B2 14 / 8 untagged (113–120) — identical to Round 2 (`counts.json/.log`) |
| PDF text layer | web == print byte-identical, 47,665 bytes each; `sNFL` 0; `das NFL-Spiel` 3 occurrences; web PDF 1,670,966 bytes ≤ 7 MB |
| Visual | P8 full frame (half-scale) viewed: clean layout, no overflow past footer. Full-res crop of the key-140 block viewed: `das NFL-Spiel.` intact, no overflow/overlap. Full-res crops of both occlusion-flag sites viewed and adjudicated (§5.1). |

**P8 keydiff note.** The brief's expected `keydiff []` assumed comparison against an identical core. The core duplicate was deliberately NOT re-fixed (it is not a separate edition), so `p8.py compare` against it now reports keydiff [140] — that single difference IS the fix (defective rendering vs corrected rendering). Status remains CLEAN 150/150. When/if the duplicate is re-synced from this edition, keydiff returns to [].

### 5.1 Occlusion finding — 2 pre-existing TEXTX flags (NOT fixed; out of scope)

The canonical audit (`tools/occlusion_audit.py`, selftest: all 6 planted classes fired, clean controls silent; re-run twice, deterministic, identical JSON) reports 2 TEXTX flags on `p8-uebungen.svg`, with identical flag texts, boxes and details on the Round 2-state SVGs (audited from the byte-identical scratch rebuild) and on the fixed SVGs:

1. `[TEXTX] 'später（15:30 晚于 11:11）） · 58. leiser…'` — ink overlaps `'begonnen） · 17. Die Kinder haben Martins'` by 5.2×11.7px (box [527.0, 2181.5, 948.2, 2197.2]). **Adjudicated on the full-res crop: measurement artifact / benign proximity.** The two column lines are visually separated; the 5.2px is advance/ink-box encroachment into the gutter, with no glyph collision visible.
2. `[TEXTX] 'beginnt.（beginnt置尾） · 80. Richtig… · 81. Fal…'` — ink overlaps `'15:30） · 124. A…'` by 76.2×12.2px (box [527.0, 2510.6, 1065.2, 2526.6]). **Adjudicated on the full-res zoom crop: REAL pre-existing overprint.** The col-2 keys tail (`…81. Falsch`, line width 538.3px in a 434px column) is overprinted by the col-3 keys head (`15:30） · 124. A…`) at the bottom of the keys block (baselines 2523.12 / 2527.18). The overprinting line's text and position are IDENTICAL in the pre-fix and post-fix SVGs — this fix neither caused nor changed it. Read-only audits of the EN and ZH-TW editions return 0 flags, so the site is zh-cn/core-specific.

Fixing flag 2 needs a keys-block reflow (the line exceeds its column by ~104px), which is a different defect class from the assigned wrap-token fix and would change P8 layout beyond D-R2-1. It is therefore **left untouched and flagged here** for the coordinator and the Round 3 proofreader to decide. The Round 2 verdict's occlusion claim (0 flags on every edition) does **not** reproduce under the canonical invocation on the Round 2-state SVGs; no explanation for that discrepancy is asserted. The brief's "0 flags" re-gate expectation is therefore NOT met as written — honestly reported here rather than claimed.

## 6. Change isolation (hash proof vs pre-fix snapshot)

Pre-fix snapshot: `de-fix-round3/pre-fix-hashes.json` (sha256 of every file in all 12 DE edition dirs, taken before any change). Post-fix comparison (after rebuild + re-render + `.text.md` regen, before the KIT append; the KIT append is the only further change):

- **Changed, zh-cn only (4 files):** `svg/p8-uebungen.svg`, `cards/p8-uebungen.png`, `Die-Lucerna-VOL3-ZH-CN.pdf` (print), `Die-Lucerna-VOL3-ZH-CN-web.pdf` (web). Plus `WEEKLY-KIT.md` (Round 3 fix record appended; earlier sections untouched).
- **Unchanged in zh-cn:** the other 7 SVGs, the other 7 cards, `ABSTRACT.txt`, and `2026-w46-de-zh-cn.text.md` (byte-identical).
- **Byte-identical, all 10 other editions + the de-core duplicate:** `de-en, -es, -fr, -it, -ja, -ko, -nl, -pt, -ru, -zh-tw`, and `de-core` (see §7 for the consequence).
- SVG text-multiset diff (zh-cn, pre-fix vs fixed): P1–P7 identical; P8 differs only in the 13 re-wrapped keys-block lines listed in §3 (same element count, same key text — only line-break placement and three restored separator spaces).

## 7. De-core duplicate divergence (reported, not silently shipped)

`weekly-report-w46-de-core/` was not edited. Its artifacts are now DIVERGENT from the canonical zh-cn edition: the duplicate's P8 SVG, card, and both PDFs still contain the D-R2-1 split (`sNFL` present; its `.text.md` is still byte-identical to zh-cn's, as before). PDF file hashes already differed at identical byte sizes in Round 2 (metadata/filename-level only); the divergence is now substantive for P8 artifacts. The duplicate must not be counted or shipped separately, and must not be shipped in place of the fixed zh-cn edition. Re-syncing it is a coordinator decision (rebuild the frozen-core build with the same v3 helpers, or copy the fixed zh-cn artifacts) — not taken here, per the brief.

## 8. Regenerated `.text.md` — diff vs pre-fix

`.text.md` was regenerated with a zh-cn-only run of the family's `export_textmd.py` (AST extraction from this edition's build-dir sources; the shared script's other-edition entries were disabled in a scratch copy so no other edition's file was touched). Result: **byte-identical to the pre-fix file** — 695 items, 37,769 bytes, golden sentences 8/8 (`textmd-regen.log`; pre-fix copy kept at `de-fix-round3/textmd-pre-fix.md`, `cmp` clean). The export is wrap-insensitive and no content string changed, so a zero diff is the expected and correct outcome; the header is verbatim. (Stated explicitly with hash proof, per the brief — not a missing regeneration.)

## 9. Final per-edition file inventory (zh-cn only; other editions unchanged)

| File | Bytes | Note |
|---|---|---|
| `2026-w46-de-zh-cn.text.md` | 37,769 | byte-identical to pre-fix; 695 items; golden 8/8 |
| `Die-Lucerna-VOL3-ZH-CN-web.pdf` (repo-shipped web PDF) | 1,670,966 | ≤ 7 MB; via `tools/webpdf.py`; pdftotext 47,665 bytes |
| `Die-Lucerna-VOL3-ZH-CN.pdf` (print master) | 16,578,262 | pdftotext 47,665 bytes; web == print byte-identical |
| `svg/p8-uebungen.svg` | (changed) | 282 text elements; only P8 SVG changed |
| `cards/p8-uebungen.png` | 1,335,671 | re-rendered @1950 |
| `WEEKLY-KIT.md` | (appended) | §7 Round 3 fix record added; §§1–6 untouched |
| `ABSTRACT.txt` | (unchanged) | 347 bytes; not part of this fix |

Pre-fix inventory for comparison (Round 1 FIX-REPORT §7): `.text.md` 37,769 bytes; web PDF 1,670,976 bytes; web `pdftotext` 101,893 bytes (that figure was the Round 1 pdf-text check's raw count; the Round 2 equality log and this round both measure 47,665 bytes for web and print — web == print holds either way); print PDF 16,578,272 bytes.

## 10. What could NOT be applied / deviations

1. **Occlusion 0-flag re-gate: NOT met as written.** 2 pre-existing TEXTX flags (§5.1); 0 new flags. The real overprint (flag 2) is out of this fix's one-defect scope and was left untouched. This is the one brief requirement that could not be applied as specified.
2. **P8 keydiff []: not applicable while the core duplicate stays unfixed.** Keydiff is [140] vs the duplicate, for the reason in §5 — the correction itself. No action taken on the duplicate, per the brief.
3. **No other deviation.** Every other brief requirement was applied: D-R2-1 fixed at source with the token intact; key text/notes/glosses untouched; no other token split in the P8 keys block (whole-edition scan: 0); kinsoku re-gate 0 hits; `76.` intact; freeze added CJK 0; counts 150 with the specified per-page distribution; PDF text layer > 0 and web PDF ≤ 7 MB; P8 full-frame + key-140 crop viewed; change isolation proved by hash; `.text.md` diff stated explicitly; KIT record appended; no origin asserted for D-R2-1.
4. **No fix could not be applied as specified within the D-R2-1 scope itself.** The defect, including the two same-class splits the whole-block scan required, is fixed.

## 11. Records and logs

- This report: `hidden_files/w46/de-fix-round3/FIX-REPORT.md`.
- Logs/JSONs under `hidden_files/w46/de-fix-round3/`: `pre-fix-hashes.json` (snapshot of all 12 DE dirs); `zh-cn-run.log` (build, 150, 0 warnings); `zh-cn-render.log` (cards/print/webpdf); `zh-cn-verify.log` (verify.py); `run_gates.sh` + `gates-run.log`; `freeze-zh-cn.log/.json`, `p8-zh-cn.log/.json`, `occlusion-zh-cn.log/.json`, `occlusion-pref.log/.json` (pre-fix audit, identical flags), `counts.json/.log`, `count_exercises_run.py`; `textmd-regen.log`, `textmd-pre-fix.md`; `svglib-v2-before.py` (pre-v3 helpers); `token-scan-final.json` (351 calls, 0 violations); `token-viol2-v2.json` / `token-viol2-v3.json` (scratch censuses: 3 / 0); `keys-p8.txt` (exact keys-paragraph string used in simulation); `crop-key140.png`, `crop-textx1.png`, `crop-textx2.png`, `crop-textx2-zoom.png`, `p8-half.png` (visual evidence); `scratch/` (build copies, simulation and scan scripts — do not ship).
- Nothing was pushed, inserted, or posted: work is local only (`~/workspace/weekly-git` untouched, `index.json` untouched, no Discord). A P8-only Round 3 independent proofread follows.
