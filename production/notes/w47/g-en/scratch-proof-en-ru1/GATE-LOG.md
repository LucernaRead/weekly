# GATE-LOG — Lucerna Weekly 2026-W47 en-ru, proof1 (rebuilt edition, en re-fanout #2)

- **Edition:** en-ru, VOL.4
- **Date:** 2026-11-11
- **Probe:** `ls /dev/null` present; `echo test | git -C ~/workspace/weekly-git
  hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`; probe file
  written in scratch dir (`scratch-proof-en-ru1/.probe`). All intermediates placed
  in scratch with `TMPDIR=<scratch>/tmp`; nothing written to /tmp; no other agent's
  files touched; production dir read-only except nothing written there at all.
  The pre-refanout proof1 files were moved to `old-proof1-pre-refanout/` BEFORE
  this round started (archived, not deleted).
- **Tools:** repo venv `tools/venv/bin/python`; repo `tools/` (occlusion_audit.py,
  p8.py, freeze.py, webpdf NOT re-run); fanout scripts copied/re-run from
  `scratch-fanout-en2/` (check_s11.py, sweep_titles.py, sweep_svg_titles.py,
  verify_ed.py, keycheck_ed.py repointed at this scratch's own p8-extract);
  canonical creambox `hidden_files/w47/tools/creambox.py`; own scripts
  `gates/h-containment.py`, `gates/keycheck.py` (repointed copy).

## Object SHAs (verified on disk before AND after the round)

| File | Size | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-ru.pdf` (print) | 29,241,701 B | `daf81d35cdf44e66dffaed2f2ab68da66251742a1be02cb1af95f8daeed9cdaf` |
| `The-Lucerna-VOL4-en-ru.web.pdf` (web) | 2,452,739 B | `3fb58ae2e80f16460e7da5f5973cc5eb9ffc2687579b6fd88fb2d9eef41674fe` |
| `2026-w47-en-ru.text.md` | 62,395 B | `d59c98c0676f74352ce81557598641b91d4d17a4d033dbdd22e775199f0bbcf7` |

All three match the brief exactly, before and after. Both PDFs 8 pages,
1462.5×2025 pt. Core-en SHAs before = after (print `b484e007…`, web `7277e32a…`,
text `e368828a…`, sizes 41,407,278 / 2,804,271 / 51,405 B) — core untouched.
KIT `WEEKLY-KIT.md` read in full (builder claims all gates green; 150 exercises,
per-page 10/17/18/18/18/18/12/39, A2 62 / B1 66 / B2 22, MODEL words 82) — claims
re-verified independently below, not taken on trust.

## Gate results

### 1. Full-text read — PASS (150/150 keys correct)
- text.md read completely (~1,306 lines, 62,395 B).
- 150 keys hand-verified against stems: **150/150 correct**. All matching blocks
  verified in definition order (Q24–27 b/c/a/d; Q38–41 b/a/d/c; Q56–59 b/c/d/a;
  Q74–77 d/a/b/c; Q141–144 b/c/d/a). No wrong key.
- Files: the text.md itself (read via file tool, lines 1–1306).

### 2. Occlusion audit — PASS, 0 flags
- `tools/occlusion_audit.py` on `svg/` → RC=0, selftest OK (all 6 classes fired),
  **0 flags**.
- Files: `gates/occlusion.json`, `gates/occlusion.log`.

### 3. P8 extract + compare — PASS (CLEAN, expected keydiff)
- Core 60/150 noted, edition 60/150 noted, same set; **compare CLEAN**, missing=[]
  extra=0. **keydiff [137,138,139,140,150]** — all expected per KIT (137–140 RU
  translation keys, 150 writing key).
- Extract keys 150/150 vs registry, missing none. P8-extracted keys spot-check:
  38=b, 39=a, 40=d, 41=c, 46=A, 52=hosted, 55=won, 125=A; 150 truncated to
  "Открытый вопрос" (known short-label exception).
- Files: `gates/p8-extract.json/.log`, `gates/p8-extract-core.json/.log`,
  `gates/p8-compare.json/.log`.

### 4. Keycheck (registry vs P8 extract; registry vs core) — PASS
- `keycheck.py ru` (builder script, repointed at this scratch's own extract) RC=0:
  registry-vs-p8extract **exact 149/150, exc=[150], mismatch=[]**;
  registry-keys-vs-core 145/150 match, diff only the 5 reader-language keys
  (137–140, 150); Q38–41 `['b','a','d','c']`; Q125 A, Q46 A, Q52 hosted, Q55 won;
  Q82/83/84 keys B C A; noted set == core noted True; extract keys 150, missing none.
- File: `gates/keycheck.py`, `gates/keycheck.log`.

### 5. Freeze — PASS, 8/8
- `freeze.py baseline --build <edition> --core-svg <edition>/svg --out
  <scratch>/freeze-final` RC=0: **8/8 SVGs byte-identical** (repointed files: none);
  produced hashes match the builder's exactly (p1 `b2ff8760…`, p2 `db36fc5e…`,
  p3 `2fe286bf…`, p4 `207a761c…`, p5 `4794a9e6…`, p6 `6f0278ea…`, p7 `8bc14548…`,
  p8 `9cd7c8da…`). Core integrity: shipped SVGs unchanged by the run.
  (Re-render ran only in scratch; production dir untouched.)
- `freeze.py diff` RC=0: per-page added CJK = 9× U+3000 only (2+1+1+1+1+1+1+1);
  added strings are Russian explanation-layer strings + re-segmented identical
  English strings; removed strings are the Chinese layer. No new English content.
- Files: `gates/freeze.log`, `gates/freeze-diff.json/.log`, `freeze-final/`.

### 6. check_s11.py (ru) — PASS
- ALL §1.1/P8 CHECKS PASS: colour set core 19 = edition 19; badges A2 #5c6e30 /
  B1 #46581f / B2 #37402f; P8 min SVG font 13.5; Q113–120 [A2] tags;
  "Levels: 145–149 [A2]"; Q120 [A2] chip OK; P8 WRITING head "H　WRITING　Письмо [B1]".
- File: `gates/check_s11.log`.

### 7. Print / web text identity — PASS
- pdftotext both: **47,655 chars each, token-multiset diff 0**; per-page
  byte-identical 8/8 (4873/5818/5264/5716/4687/5600/6001/9696 B).
- Web PDF text layer present (2,452,739 B). Web P1 + P8 rendered and viewed —
  visually identical to print.
- File: `gates/printweb-diff.log`.

### 8. P8 min font — PASS
- PyMuPDF on print PDF: answers render at **10.12 pt** (13.5 SVG px × 3/4);
  ≥9.75 pt SOP §1.1 floor → PASS. P1 min 11.62 pt.
- KIT's "13.5 pt" label conflates SVG px with pt — wording nit only.
- Also verified inside `verify_ed.py` output (see §13).

### 9. Quotes / apostrophes / banned words — PASS
- text.md U+201C 81 / U+201D 81 (balanced); SVGs per page 201C=201D
  (2/1/10/3/11/2/29/24 = 82 total); U+2019 = 0 everywhere (apostrophes are ASCII ',
  40 in text.md); U+2018 = 0.
- **0 Cyrillic-adjacent curly quotes in all 8 SVGs.**
- Banned-word scan (SOP/proofread/cover/TODO/FIXME/XXX/lorem/占位/桥接) = 0 hits.
- No stale Ashes phrasing anywhere (see PROOF-NOTE.md).
- (Counts computed by script; see commands in the proofer's session, not a saved log.)

### 10. Creambox (canonical scan) — PASS, 0 OVERFLOW
- Canonical `hidden_files/w47/tools/creambox.py` on `svg/*.svg` RC=0, **0 OVERFLOW**.
- Inside-only clearances all positive; min baseline clearance +5.0 px (P2 AND YOU?
  box), next +12.0 px (P1 SEARCHES gloss, vertical only), most +47.7/+48.1 px.
  P7 toolbox: 7 boxes, min inside clearance +47.7, min desc-clear +41.6.
- True-ink-bottom scan (`gates/ink-bottom2.log`, PIL anchor="ls", per-run descents):
  every box's last line ink-bottom clearance ≥ 0.0 px; tightest is P2 AND YOU?
  +0.0 px (see PROOF-NOTE.md tight-but-passing — adjudicated inside on the render).
  (An earlier run with the default PIL anchor measured the ascender, not the
  baseline — invalid; `ink-bottom.log` is superseded by `ink-bottom2.log`.)
- Files: `gates/creambox.log`, `gates/ink-bottom.log` (superseded),
  `gates/ink-bottom2.log`.

### 11. Horizontal / vertical containment (PyMuPDF on print PDF) — 1 DEFECT
- Own script `gates/h-containment.py` (rects from cream-filled drawings, spans from
  text dict; a span counts only if it overlaps the rect BOTH vertically and
  horizontally, so other columns' text cannot false-flag — the first version of
  the script lacked the horizontal-overlap condition and was corrected before use).
- **H-SPILL total: 1** — P1 SEARCHES gloss "Относительный интерес, не точные цифры."
  x[1096.1,1403.5] pt vs rect x[1079.6,1396.5] pt → **right +7.0 pt**
  (see PROOF-NOTE.md Defect 1 for the SVG-advance + rendered-pixel cross-checks).
- V-SPILLs: 28, all +6.0/+13.7 next-block headings/body text below boxes (design
  spacing), NOT defects — same pattern as proof1.
- Files: `gates/h-containment.py`, `gates/h-containment.log`.

### 12. Boxtitle sweeps — PASS
- Source sweep (`sweep_titles.py ru`) RC=0: 12 titles measured, **0 over budget**
  (tightest: ODD SOCKS 398.3, margin +6.2; A PRACTICE BALLOT +25.8;
  THE WEEK IN NUMBERS +30.1; HOW LONG? +32.1; SATURDAY, NOV 21 +75.6;
  HAYMITCH'S GAMES is not in the 12 source titles — it is covered by the SVG sweep).
- SVG sweep (`sweep_svg_titles.py ru`) RC=0: **18 titles checked, 0 overflows**
  (HAYMITCH'S GAMES 309.6, +94.9; SATURDAY, NOV 21 328.9, +75.6;
  SENATE IN NUMBERS 328.3, +76.2; ODD SOCKS 398.3, +6.2 advance / +6.5 true ink).
- Files: `gates/boxtitle.log`, `gates/boxtitle-svg.log`.

### 13. Edition verify (Q39/40, Ashes, SAY IT, P8 font, text.md) — PASS, all lines
- `verify_ed.py ru` RC=0, **VERIFY ALL PASS** (22/22 checks): Q39 key a, Q40 key d,
  notes mentor=a / arena=d (not estadio/stadio), Q46 key A + 2025 note, Q52 hosted,
  Q55 won, Q125 key A + 4–1 note, no stale Ashes phrasing in registry, text.md
  150 answers, Q39 a / Q40 d / Q125 A, "Arsenal are winning" present,
  no "Perth is winning" / "second week in Perth" / "Ashes begin", Ashes
  retrospective present, P8 min PDF font ≥ 9.75 pt (10.12 pt), SVG zero real CJK.
- File: `gates/verify.log`.

### 14. ABSTRACT — PASS (full form)
- One line, 659 chars, Russian, no ASCII double quotes. Contains Lucerna, VOL.4,
  150, A2–B2; mentions announced results, certification 10 Nov–18 Dec,
  16/20/21 Nov items, Ashes 4–1, reader language. (Checked by script.)

### 15. "next Sunday" — NO APPLICABLE OBJECT
- `grep -rc "next Sunday"` = 0 in core-en content*.py, en-ru content*.py,
  `tools/tables.py`; case-insensitive grep = 0 in both text.md files. Rule not applied.

### 16. D5 font inventory — RECORDED ONLY (not judged)
- 1,798 `<text>` elements; 26 distinct sizes (px): 13.5×75, 15.5×13, 16×1, 17×34,
  18×15, 18.5×2, 19×162, 19.5×71, 20×53, 20.5×166, 21×21, 21.5×183, 22×167,
  22.5×9, 23×147, 23.5×131, 24×465, 25×34, 26×2, 27×3, 28×11, 32×11, 36×5,
  46×15, 53×1, 196×1. No judgement made.

### 17. Visual checks — PASS except Defect 1
- Print pages P1–P8 rendered at 150 dpi (`render/print-p-*.png`) and viewed;
  web P1 + P8 rendered (`render/web-p1-1.png`, `render/web-p8-8.png`) and viewed —
  identical to print. Zoom crops viewed: `p1-searches-gloss.png` (Defect 1 visual
  proof), `p1-searches-box.png`, `p2-andyou-bottom.png`, `p2-sayit.png` (D4 fix
  verified: all three Russian subs inside their panels, glossary gutter intact),
  `p2-didyouknow.png`, `p2-senate-title.png`, `p3-haymitch-title.png`,
  `p4-saturday-title.png`, `p5-oddsocks-title.png`.
- No other overflow/overlap/truncation/footer-intrusion on any page. Footers
  "Страница N из 8" on all pages; masthead/edition line/badge correct.
- Pixel-level cross-checks on the 150 dpi renders: P1 gloss rightmost ink 1401.6 pt
  vs box right 1396.5 pt (+5.1 pt); P2 AND YOU? lowest text ink 1157.8 pt vs box
  bottom 1158.7 pt (+0.9 pt inside; the olive divider at 1168.5 pt spans the page
  and is a design rule, not a spill).

### 18. External-fact verification — PASS (new/changed items re-checked live)
- Ashes retrospective verified 2026-11-11 via web search (Sky Sports, Cricbuzz,
  ICC, Sportradar, Flashscore): 1st Test Perth Fri 21 Nov 2025, Aus by 8 wickets
  in 2 days, 847 balls = shortest Ashes Test by balls bowled since 1888 (only
  788 Old Trafford 1888, 792 Lord's 1888 shorter); series Nov 21, 2025–Jan 8,
  2026; first three Aus (Perth/Brisbane/Adelaide); 4th Melbourne England by
  4 wickets, first England Test win in Australia since Sydney 2011; 5th Sydney
  Aus by 5 wickets; final 4–1; two Tests lasted two days; India beat Australia
  by 295 runs at Perth, Nov 2024; next Ashes England June 2027.
- Unchanged facts are byte-identical to the text proof1 verified against live
  sources the same day (see PROOF-NOTE.md); freeze diff confirms no new English
  content was introduced by the rebuild.

## Standing rules honored
- SOP §8.4 proof loop: a full round with zero findings is required to call an
  edition final; 1 defect found → verdict (b).
- Core-level vs edition-level attribution done per defect (Defect 1 is
  en-ru-specific, pre-existing; core never touched).
- No source files modified, no rebuild, no commit/push; webpdf.py NOT re-run
  (would rewrite the shipped web PDF); dump_reg.py NOT run (would write into the
  edition dir); make_textmd NOT run; freeze baseline wrote only into scratch.
- Every number in PROOF-NOTE.md is reproducible from the files listed above.
