# PROOF-NOTE — 2026-W47 ko-nl (proof1, independent)

- **Edition:** `2026-w47-ko-nl` (target ko, reader Dutch). Fan-out #3, run 2 shipped.
- **Prover:** independent proof1 (separate person from the fan-out #3 builder).
- **Date:** 2026-11-11. Work dir:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ko-nl/`
  (all gates re-run in a scratch copy; the production dir was only read, never
  written; `TMPDIR` pointed at the work dir throughout.)
- **Core baseline:** `core-ko` run 11 (fix1) + textmd fix2.

## Conclusion: (a) 定稿零缺陷

No defect found. All gates pass on independent re-runs; the 150 items were
hand-verified across three sources; all 8 pages were visually read at 100dpi
with zero issues. Carry-forward items from FANOUT-REPORT-ko3.md all verify.

## SHA verification (before AND after proof — unchanged)

| File | Bytes | SHA-256 | Result |
|---|---|---|---|
| Edition print `Lucerna-VOL4-KO-NL.pdf` | 45,473,131 | `2bf684453f9bb187001070bcdae607bee74f51d193fb886a3fa2d76c77790a7b` | ✓ matches task |
| Edition web `Lucerna-VOL4-KO-NL-web.pdf` | 4,020,321 | `c4ad9cc631b7d35230510f0920eac2310537bdffba5baec1793341ef4611eef5` | ✓ matches task |
| Edition `2026-w47-ko-nl.text.md` | 35,040 | `a51d9fa51f86c3ca3b10475ea9701326aef55bd1afb99f2c58d2b62a048b669d` | ✓ matches task |
| Core print `Lucerna-VOL4.pdf` | 46,232,227 | `53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27` | ✓ matches fan-out baseline |
| Core web `Lucerna-VOL4-web.pdf` | 4,232,878 | `9592945ae188dc8e50394fcab1ded155baaff63161bcf0b5f7ecbc6898c43bc7` | ✓ matches fan-out baseline |
| Core `2026-w47-ko-zh-cn.text.md` | 34,606 | `da1d3a323f7c83eb95fe989e59f56ca6a706282c443f20cc5792c3f73468181a` | ✓ matches fan-out baseline |

Core SHAs re-measured after all gates: identical — the core did not move during
this proof. Edition SHAs re-measured after all gates: identical — production
was not touched. (The edition `__pycache__`/SVG hashes in the scratch copy
match the builder's `sha-nl-run2.txt` exactly.)

## Gate summary (all independently re-run; full logs in GATE-LOG.md)

| Gate | Result |
|---|---|
| run.py (system python3) | rc=0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150 (A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38); P2-feature ends 1531, P8-keys ends 2487, P7 teaser 2512.7; re-run SVGs byte-identical to shipped |
| freeze baseline (system python3) | **8/8 byte-identical** |
| freeze diff vs core | added CJK **7, all U+3000** (1 each on p2–p8, 0 on p1 — footer separators) |
| venv freeze (control) | ABORT rc=2, as expected (ko exemption: venv Pillow 13 vs system Pillow 10.2.0) — recorded control, not a failure |
| p8.py extract | 150/150 noted |
| p8.py compare vs core | **CLEAN**, missing=[] extra_count=0, keydiff=[137, 138] (E-group re-aiming, W46 precedent) |
| occlusion audit | **0 flags**; selftest OK (6 planted classes fired, clean controls silent); NEW vs core 0 |
| check_core / check_gloss | rc=0, gloss fails 0, phrases **8/8 verbatim**, orphan issues 0, dates correct |
| textmd re-export | **byte-identical** to shipped text.md (SHA `a51d9fa5…`, 35,040 B, 449 items) |
| print/web text layers | **byte-identical** (108,414 B each, pdftotext -layout; 51,630 text bytes per webpdf log); both 8 pages, 1462.5×2025 pts |
| web PDF re-render (scratch only) | text layer byte-identical to shipped web PDF; same byte size 4,020,321; SHA differs (expected — fontTools wall-clock); shipped web PDF never overwritten |
| P8 min font | **9.975pt** (172 spans by the calibrated bbox rule, 167 at-min) ≥ 9.75pt |
| boxtitle widths | **8/8 ≤ 386.5px**, widest 350.3px (`김장 장보기 목록　Boodschappen`) |
| U+2019 / U+201C / U+201D sweep | **0 / 0 / 0** across 8 SVGs + text.md |
| Han-ideograph residual | **0** in all 8 SVGs (the 177 raw CJK-range hits are U+3000 ×124, 「」 ×25 each, 〜 ×3 — legitimate Korean punctuation/space) |
| §1.1 grep audit | OK: paper/VOL.4/middot identical to core page-by-page; hanzi 0; P7 VOL.5 3→2 by design; unknown colours identical to core |
| census (ex/match + D6 vs text.md) | 166 items, **0 missing**; D6 0 missing |
| creambox 真墨复核 | 55 cream rects (excl. page bg), **0 empty** |
| orphan-punctuation sweep | **0** (no line starts with closing punctuation, none ends with opening punctuation) |
| D5 font census (record only, not judged) | **Noto Sans CJK SC segments: 0** in print and web PDFs (both embed KR fonts only: NotoSansCJKkr / NotoSerifCJKkr + UnifrakturMaguntia masthead). Latin-only spans in print PDF: 486 (Sans Regular 157, Sans Bold 212, Serif Regular 104, Serif Bold 12, UnifrakturMaguntia 1) — all set in KR fonts. SVG font-family counts: Noto Serif CJK KR 882, Noto Sans CJK KR 620, UnifrakturMaguntia 1 |

## Carry-forward verification (FANOUT-REPORT-ko3.md)

- **P2-feature overflow fix #1 — VERIFIED LANDED.** My own run.py: P2-feature
  ends 1531 (bottom 1540), margin **9px** — the tightest flow in the issue,
  same as en. Shipped P2 SVG geometry: gloss #2 is exactly **2 lines**
  (`Uitleg — 효능 = voordeel · 등재되다 =` y=815.5 / `geregistreerd · 발효 =
  fermentatie` y=845.225, 29.7px line pitch); `geregistreerd worden` occurs
  **0** times in the SVG. All other flows fit (next-tightest: P1-headline 14px,
  P8-keys 53px, P7 teaser 67.3px; every other flow ≥196px headroom).
- **#43 / #123 / #124 adjudication — VERIFIED against core sources.** The core
  REG notes are the source of truth and the Dutch notes render them exactly:
  #43 core `内藏山=Weatheri预报11日 b` → nl `内藏山 = Weatheri-voorspelling 11 nov. b`;
  #123 core `内藏山林业厅预报峰值11月4日` → nl `Naejangsan: Bosdienst voorspelt piek op 4 nov.`;
  #124 core `内藏山Weatheri预报峰值11月11日` → nl `Naejangsan: Weatheri voorspelt piek op 11 nov.`.
  P3 items #40/#41 (Weatheri 11 / Bosdienst 4) and #44/#45 are consistent with
  P8 #123–#125. Attribution: **core inheritance** — Weatheri / Bosdienst are
  core-ko's own renderings of the private weather company and the Forestry
  Service (산림청); not typos, not introduced by this fan-out.
- **"next Sunday" freeze rule — NO APPLICABLE OBJECT.** Grep for `next Sunday`
  (and case-insensitive `sunday`) over core-ko, ko-nl and `tools/tables.py`:
  **0 hits**. The Dutch text says `zondag 22 nov.`, never "Sunday". Nothing to
  freeze; the rule is not applied to any line.

## 150-item three-source hand verification (all rows read)

Sources: (1) REG from the edition's `content*.py` (AST), (2) keys from the
edition P8 SVG (`tools/p8.py extract`), (3) REG from core-ko `content*.py`;
cross-checked against the builder's EDITION-RECORD table (4th source).
Full table: `logs/three-source.log` (150 rows + per-row core-note vs nl-note).

- Keys: **BAD 0/150**. 147 exact across all three sources; #137/#138 re-aimed
  to Dutch by design (W46 E-group precedent; SVG matches the Dutch keys;
  `p8.py compare` CLEAN); #150 renders `✓` in core and edition alike
  (verified in the core P8 extract).
- Record cross-check: **BAD 0/150** (page/type/key/note all match the record).
- Notes: I read all 150 Dutch notes against the core Chinese notes — every one
  is a faithful rendering (dates, numbers, weekdays, scores all match; Dutch
  number/date formats `54.980 won` / `26,5%` / `16 nov.` applied consistently;
  `weerdienst` for 气象厅 in #89/#110 is the same rendering in both places).
- Counts: TOTAL 150; by page 10/18/18/18/18/18/12/38; A2 51 / B1 72 / B2 27;
  types Invullen 48 / Meerkeuze 52 / Combineren 16 / Omzetten 4 /
  Zinnen bouwen 8 / Juist of onjuist 4 / Gatentekst 13 / Vertalen 4 /
  Schrijven 1; H model 169 chars.

## 8-page visual read (100dpi renders of the shipped print PDF)

P1–P8 all read, zero issues. Spot notes: P1 `Alles` visible in the contents
8면 row; P2 `Boodschappen` box fully inside the feature area, D-day strip
clean; P3 `김치의 날에 알아 둘 것　Te weten` fits; P4 postseason ladder clean;
P5/P6 no overflow, table clean; P7 frame `Kader: 「na ~」. Vraag: 「〜 후에 뭐
해요?」` with 「」, clinic notes one line each, single Dutch disclosure
carrying the promise to VOL.5, all 8 phrases verbatim with per-phrase page
citations; P8 all 150 answers printed, E 137/138 in Dutch, `150. ✓ Modeltekst
in deel H op deze pagina (169 tekens)`, H model + photo in col 4. Footer on
all pages: `Lucerna　KOREAANS WEEKBLAD VOL.4　Teksten in het Koreaans　Uitleg
in het Nederlands`; page lines `Pagina {n} van 8`.

## text.md self-read (full)

Read head + P7 + P8 sections; sweeps: no TODO/XXX/lorem/placeholder, no stray
English furniture words, no double spaces, 917 lines. Frame line at line 761
(`Kader: 「na ~」. Vraag: 「〜 후에 뭐 해요?」`), Dutch disclosure at line 767.
The P7 phrase citations show a single `1면` (line 781) — **identical to core**:
core's text.md has the same single `1면` (line 787); textmd.py dedupes the
repeated citation strings, and the rendered P7 phrases carry the full
per-phrase citations (check_core phrases 8/8 verbatim). Not a loss, not a defect.
text.md 449 items vs core 452: the three drops are the adjudicated ones
(`Alles` rejected by `is_prose` — rendered correctly on P1; `lcn2` + `lko`
removed by design). `___` blanks (75) are exported source literals, same as core.

## Old-version comparison

No prior ko-nl edition exists (new edition in fan-out #3; no `2026-w47-ko-nl`
in `issues/` or git history) — nothing to compare against. (W46 ko bundle
commits are a different week.)

## Notes / observations (not defects)

- Tightest margin in the issue is P2-feature at 9px — the same as en; it fits
  and is confirmed in the shipped SVG geometry. No action.
- The freeze guard keys off path components: my first baseline run from a
  scratch dir named `edition` aborted rc=2 because no path component matched
  the ko-family pattern; renaming the scratch copy to `2026-w47-ko-nl` (its
  true slug) made the guard recognise it and the baseline passed 8/8 under
  system python3. Worth knowing for future proofs: the scratch copy must keep
  a ko-family path component.
- My first HAN sweep used the broad range `[\u2e80-\u9fff]` and counted 177
  CJK-punctuation hits; the correct Han-ideograph range `[\u4e00-\u9fff]`
  (same as style11-ko.py) gives 0. The sweep script was corrected and re-run.

## Defects

None. **(a) 定稿零缺陷.**

No commit, no push, no insert.py, no lint --write performed.
