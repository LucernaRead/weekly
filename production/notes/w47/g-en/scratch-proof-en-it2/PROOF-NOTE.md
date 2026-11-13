# PROOF NOTE — Lucerna Weekly 2026-W47 · en-it · proof2 (post-delta)

**Edition:** English target × Italian readers (`2026-w47-en-it`), VOL.4, issue week 2026-11-16..22
**Proofreader:** independent proof2 (SOP §8.4), not the builder / not the delta agent
**Date:** 2026-11-11
**Conclusion: (a) 定稿零缺陷 — zero defects. Ready to ship.**
**Scope:** the delta state — Q73 key sync `content56.py:49` `"speak"` → `"up"` only.
Proof1 conclusion was (a) PROVISIONAL pending this post-delta re-proof; this note closes it.

## Objects verified (SHA-256, measured before AND after all proof work — identical)

| File | Size | SHA-256 | Check |
|---|---|---|---|
| `The-Lucerna-VOL4-en-it.pdf` (print) | 29,327,187 B | `2db4dad1496e474fbd01315bf3b7f8393358a60155ce103f6a8bae476a5502a0` | MATCH task |
| `The-Lucerna-VOL4-en-it.web.pdf` (web) | 2,408,879 B | `570eef4fb1174edb33e3e46c324d96231dac086140a34e1e7376929a41525239` | MATCH task |
| `2026-w47-en-it.text.md` | 53,944 B | `a833062570765ad5fea4e1f2a4ac4396afd28f2376bb86dbeb9991eae9e2f464` | MATCH task |

Both PDFs 8 pages, 1462.5 × 2025 pts. Probes passed before work (`ls /dev/null` present;
`echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`;
write probe in goals-side scratch OK; TMPDIR pointed at scratch `tmp/`; disk 62G free).
**Core-en untouched by this round** (matches the delta note §7.3): print
`08cbc1e53f2d02d6c64266d1f64ac2422eaa2f8f71e1829f877e94a5627b3213`, 41,407,287 B;
text.md 51,402 B. No production file was written: all re-renders ran in the scratch copy
`proof-copy/`; `git status` shows the edition and core dirs only as untracked (`??`), same as before.

## Delta independently re-verified (against delta scratch `pre/`)

- **Registry:** pre vs production — exactly **1** differing entry: n=73 key `'speak'` → `'up'`,
  note identical (`speak up = parlare senza paura`); all other 149 entries identical.
- **text.md:** pre vs production — exactly **1** differing line (1151):
  `73. [A2] Completare le frasi — speak (…)` → `… — up (…)`. Line count 1305 both.
- **SVG:** p1–p7 byte-identical to pre (SHA match); only `p8-test.svg` changed
  (pre `2060db36…` → post `ba31ef73…`). **P5 unchanged is correct and expected**
  (Q73 key prints only on the P8 answers page; P5 prints only the `Speak ___` blank + the
  `speak up` gloss) — matches DELTA-NOTE §7 correction.
- **Q73 four-source consistency (all `up`):** registry n=73 key `'up'`;
  text.md line 1151 `— up (speak up = parlare senza paura)`;
  fresh P8 extract `"73": "up"` and rendered P8 ANSWERS `73. up`;
  P5 stem `73. Speak ___: tell a teacher.` + gloss `to speak up = parlare senza paura`
  (P5 SVG: `Speak ___` ×1, `to speak up` ×2); core-en registry n=73 key `'up'`.
  `content56.py:49` key `"up"`. "Speak up: tell a teacher." is a correct sentence.

## What was checked

- **Reproducibility (scratch copy only):** `run.py` RC=0, 0 OVERFLOW / TOO WIDE, TOTAL 150,
  MODEL 82 (P8-keys 2443/2560); `render.py` RC=0. Re-rendered print PDF is **byte-identical**
  to production (`2db4dad1…`, 29,327,187 B) and all 8 SVGs MATCH production byte-for-byte.
- **Registry:** re-dump (repointed `dump_reg.py`, output to this scratch) == production
  `registry.json` (150 entries; per page 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22).
- **Occlusion audit (real command, no `--selftest`):** 0 flags (selftest OK, all 6 planted
  classes fired, clean controls silent).
- **p8 extract + compare:** 60/150 noted, same set as core; **CLEAN**, missing=[] extra=0,
  keydiff=[137, 138, 139, 140, 150] (reader-language translation keys + open writing key — expected).
- **Keycheck — see §"Keycheck note" below.** Independent re-run on MY fresh extract +
  production registry: registry-vs-p8extract **149/150 exact + n=150 exception**, mismatch=[];
  registry-keys-vs-core 145/150 (diff only the 5 expected reader-language keys 137–140, 150);
  Q38–41 = [b, a, d, c]; Q125=A, Q46=A, Q52=hosted, Q55=won; Q82/83/84 = B/C/A;
  noted set == core; extract keys 150, none missing.
- **Freeze (standard invocation):** `--build` = core-en, `--core-svg` = core-en/svg:
  baseline **8/8 SVGs byte-identical**, repointed files: none; core integrity re-hash OK.
  Supplementary edition-internal baseline (`--build` = proof-copy, `--core-svg` = edition svg):
  **8/8 byte-identical** (recorded as supplement only, not as the freeze gate).
  Freeze diff: TOTAL added CJK = **9, all U+3000** (p1: 2, p2–p8: 1 each).
- **Print/web text layers:** 47,988 chars each (47,991 − 3 = the one key), token-multiset diff **0**,
  per-page byte-identical **8/8** (p8 10,243 B vs pre-delta 10,246 B — the −3). Scratch-only
  webpdf re-render (2,408,885 B) has a **byte-identical text layer** to the production web PDF
  (47,988 chars, token diff 0). Production web PDF never overwritten. Print-vs-web render
  pixel diff is font-rasterisation only (P1 0.657% / P8 0.157% of pixels differ >30 grey levels;
  web embeds Lucerna-renamed subsets); web P8 visually identical to print P8.
- **text.md:** re-export from proof-copy source + re-dumped registry is **byte-identical**
  to production text.md (SHA `a8330625…`, 53,944 B, 498 recorded blocks, stub 150 = real 150).
- **check_s11:** ALL §1.1/P8 CHECKS PASS (colour set core 19 = edition 19; badges A2/B1/B2 present;
  P8 min SVG font 13.5; Q113–120 [A2] tag line; "Levels: 145–149 [A2]"; Q120 [A2] chip;
  WRITING head "H　WRITING　Scrittura [B1]").
- **Boxtitle sweeps:** source 12/12 fit (tightest HOW LONG? 384.3px, margin +20.2); rendered SVG
  18/18 fit, 0 overflows (PIL real-ink measurement, not baseline-only).
- **Creambox (canonical `hidden_files/w47/tools/creambox.py`, all 8 SVGs):** 32 boxes; log
  **byte-identical to proof1's** (`diff` RC=0). Min inside-only clearance **+5.0px**, no inside-only
  negative. The single desc-clear flag (−1.0px, P2 AND YOU? box) is the same adjudicated false
  alarm as proof1 (last line "redazione." has no descender; baseline clearance +5.0px inside
  the cream; rendered P2 confirms).
- **Spill sweep (baselines outside boxes):** for every cream box (#f0eee5), all text lines
  horizontally overlapping the box with baseline below its bottom sit ≥24px below the bottom
  (min 24.0px, p1 WORD OF THE WEEK title; all others ≥35.5px) — all are next-section titles or
  following paragraphs, never a straddling line. No spill.
- **verify_ed.py:** ALL PASS (23/23).
- **150 questions, three-source hand verification:** full read of production `text.md`
  (1305 lines) + registry + P8 extract + SVG definitions. Every answer checked against its stem;
  **150/150 correct.** All 5 matching sets re-verified against printed definitions in source AND
  SVG (P2 Q24–27 b/c/a/d; P3 Q38–41 b/a/d/c; P4 Q56–59 b/c/d/a; P5 Q74–77 d/a/b/c;
  P8 Q141–144 b/c/d/a). Weekday checks via `date -d` (America/Toronto): Tue 2026-11-03,
  Sun 2026-11-08, Mon 2026-11-09, Tue 2026-11-10, Mon 2026-11-16, Wed 2026-11-18,
  Fri 2026-11-20, Sat 2026-11-21, Sun 2026-11-22, Thu 2026-11-26, Fri 2026-11-27,
  Tue 2026-12-01, Fri 2025-11-21 — all match the text.
- **8 pages rendered and read visually** from the production print PDF (`render/p--1.png`…
  `p--8.png`) + web P1/P8 (`render/w1--1.png`, `w8--8.png`). No overlap, no spill, no missing
  content; footers "Pagina n di 8" all present. Web P8 visually identical to print P8.
- **Orphan punctuation sweep:** 0 orphan-led lines in text.md; U+2019: 0 hits in text.md and
  all 8 SVGs (61 ASCII straight apostrophes in text.md).
- **D5 fonts (recorded only, not judged):** print PDF 41 font objects, 7 families —
  DejaVuSans ×1, Newsreader16pt-Italic ×1, Newsreader16pt-Regular ×16, NotoSansCJKsc-Bold ×8,
  NotoSansCJKsc-Regular ×8, NotoSerifCJKsc-Regular ×6, UnifrakturMaguntia ×1. Web PDF
  41 objects, 8 Lucerna-renamed families. P8 min PDF font **10.12pt ≥ 9.75pt** floor.

## Keycheck note (canonical run reads a stale archive — NOT an edition defect)

The canonical `keycheck_ed.py it` run in this round printed
`registry-vs-p8extract exact 148/150 exc=[150] mismatch=[(73, 'up', 'speak')]`.
Root cause, verified: the script (`scratch-fanout-en2/keycheck_ed.py:16`) reads its extract from
the archived `scratch-fanout-en2/fanout/it/p8-extract.json`, mtime 2026-11-11 11:57 — a
**pre-delta** extract whose Q73 is still `'speak'`. The registry it reads is the current
production one (Q73 `'up'`), so the single mismatch is the archive being older than the delta,
not the edition. Evidence: my fresh `p8.py extract` on the shipped production P8 SVG gives
Q73 `'up'`; the independent keycheck re-run against MY fresh extract + production registry
gives **149/150 exc=[150], mismatch=[]** (file `gates/keycheck-mine.log`), identical figures to
proof1 and to the delta's own independent re-run. The canonical script's other line
(registry-vs-core 145/150, same 5 diffs; Q38–41/Q125/Q46/Q52/Q55/Q82–84) agrees in both runs.
**Action for the coordinator, not a defect of this edition:** refresh the archived
`scratch-fanout-en2/fanout/it/p8-extract.json` (and any sibling archives) after a delta, or
repoint the canonical script at the current extract; otherwise every post-delta canonical
keycheck will report this same phantom 148/150.

## Tight-but-passing (genuinely tight, inside, recorded no-fix — carried from proof1)

- **HOW LONG? box title:** source 384.3px, margin **+20.2px** (tightest of the 12); SVG advance
  margin +20.2 — inside, visually confirmed on P6.
- **P2 AND YOU? box:** last baseline clearance **+5.0px**; desc-clear heuristic −1.0px is a false
  alarm (last line "redazione." has no descender; see §9 of proof1 GATE-LOG). Creambox log
  byte-identical to proof1, so the adjudication stands unchanged.
- **Q2 note vs P6 gloss:** "call a race = proclamare il risultato" (registry note) vs
  "annunciare il risultato" (P6 gloss) — two source literals, both correct.
- **Q54 note** "eight (otto = eight)" — tautological, same pattern as the core's note style.
- **Q34 note** "(open = uscire (terza persona singolare con -s))" — correct in context.
- **proof1 line-count note:** proof1's note says text.md has "1,306 lines"; the file has
  **1305** lines, pre-delta and post-delta alike (verified by `wc -l` on both). Pen slip in
  proof1, not a content difference.

## Defects

**None. Zero defects found in this round.**

No commit, no push made. All work in
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-it2/`
(gates in `gates/`, renders in `render/`, scratch re-render copy in `proof-copy/`).
