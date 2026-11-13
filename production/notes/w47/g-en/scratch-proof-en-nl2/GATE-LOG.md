# GATE-LOG — W47 en-nl proof2 (post-Q73-delta build)

- **Edition:** `production/2026-w47/2026-w47-en-nl/`
- **Run:** 2026-11-11 (Toronto). All gates run in `scratch-proof-en-nl2/`; `TMPDIR=<scratch>/tmp`.
  Nothing written to /tmp. No production file was modified; no commit/push.
- **Core integrity:** core-en SHAs measured before AND after (print `08cbc1e5…`,
  web `d7927ead…`, text `23855d4b…` — the fix2 values) — unchanged throughout.
  Freeze baseline re-rendered core into a scratch build-copy only (`gates/freeze-final/`);
  no production file was overwritten. The web PDF was never re-rendered over the production
  copy — identity was verified from the delivered PDFs by pdftotext + scratch renders.
- **Probes:** `/dev/null` present; `git hash-object -w` OK
  (`da0c4eb8d9a48d171a33574b380752e183286751`); probe file written in scratch before any work.

## File identity (verified before proofing)

| file | size (B) | sha256 (full) |
|---|---|---|
| print `The-Lucerna-VOL4-en-nl.pdf` | 29,341,267 | `f1e1e511bd780243878f767c73d92f22ff6407718fbde7dbe209068938e87dca` |
| web `The-Lucerna-VOL4-en-nl.web.pdf` | 2,411,546 | `c1a0828865d9a293b7e2be1e3f6cec674f7b1f1ca8193049c2c43906e1c509a8` |
| `2026-w47-en-nl.text.md` | 53,565 | `30bfb6f93860fae5ae58707c28c4f2e3a18ebcc07e272681e67688451d12c0be` |

All match the task values. Both PDFs 8 pages, 1462.5 × 2025 pts.
Core-en fix2 SHAs (before AND after, unchanged): print `08cbc1e5…` 41,407,287 B;
web `d7927ead…` 2,804,281 B; text `23855d4b…` 51,402 B.

## Delta verification (independent re-measurement of DELTA-NOTE §4)

| check | result |
|---|---|
| registry vs `registry.pre.json` | **exactly 1 entry diff** — n=73 `key: 'speak'` → `'up'`; other 149 byte-identical (`gates/delta-verify.log`) |
| text.md vs `text.pre.md` | **exactly 1 line diff** — line 1151, Q73 `speak` → `up` |
| SVG vs `svg.pre/` | **p1–p7 byte-identical; only p8-test.svg changed** (`530c9d35…` → `ee35fc68…`); P5 byte-identical by design (key prints only on P8) |
| P8 stripped-text diff pre vs cur | same 259 `<text>` elements; only 5 lines reflowed around Q73; no word added/removed/altered |
| Q73 four-source | registry `up` / text.md line 1151 `up` / P8 SVG `73. up` present + `73. speak` absent / P5 stem `Speak ___: tell a teacher.` + gloss `to speak up = je uitspreken` present; core-en `content56.py:49` key `"up"` (read-only) |

## Gates

| gate | result |
|---|---|
| **Occlusion audit (real command, no --selftest)** | selftest OK as tool sanity (all 6 classes fired, clean controls silent, separate `occlusion-selftest.log`); audit of `svg/`: **0 flags** — PASS (`gates/occlusion.json`, `occlusion.log`) |
| **p8 extract (core + edition)** | edition 150 keys; noted set 60/150; noted set **identical to core's** — PASS (`p8-extract-core.json`, `p8-extract.json`) |
| **p8 compare** | **CLEAN**; missing=[]; extra=0; keydiff=[137, 138, 139, 140, 150] (reader-language translation keys + writing key — exactly as expected) (`p8-compare.json`) |
| **keycheck.py** | RC=0; REG 150, p8extract 150, exact match **149/150**; only mismatch n=150 (key 'Open vraag — punten in het schrijfblok; voorbeeldtekst in het kader op pagina 8' vs extracted 'Open vraag' — known extractor truncation). `keycheck-150.json` written. Note: first run failed `ModuleNotFoundError: tr_nl` (script imports the translation module from its own dir); fixed by copying `tr_nl.py` from proof1 scratch into this scratch and re-running clean. Registry vs core P8 keys: **145/150** (the same 5 keydiffs). (`keycheck.log`) |
| **freeze baseline (STANDARD: `--build` core-en, `--core-svg` core-en/svg)** | **8/8 SVGs byte-identical**; core integrity unchanged (shipped core SVGs re-hashed, unchanged) — PASS (`freeze.log`, `gates/freeze-final/`). Baseline verified to be core-en's SVG: the 8 core hashes in the log (p1 `a9a8deaf…`, p8 `1066c475…`) are the shipped core SVGs, and the direct re-hash below matches them. |
| **freeze direct sha** | build-copy vs shipped core SVGs **8/8 MATCH** — PASS (inline in `run-gates-stdout.log`) |
| **freeze baseline SUPPLEMENTARY (edition-internal)** | `--build` = edition dir, `--core-svg` = edition svg: **8/8 byte-identical**, incl. new p8 `ee35fc68…` — supplementary evidence only, not presented as the standard baseline (`freeze-edition.log`, `gates/freeze-edition/`) |
| **freeze diff** | added CJK = **9× U+3000 only** (p1 2, p2–p8 1 each) — PASS (`freeze-diff.json`, `freeze-diff.log`) |
| **print/web text diff** | 48,041 vs 48,041 chars; 2,481 distinct tokens each; token multiset diff **0/0**; full pdftotext **byte-identical**; per-page pdftotext **byte-identical p1–p8** — PASS (`printweb.log`, `pg-print-*.txt`, `pg-web-*.txt`) |
| **check_s11.py (nl)** | RC=0, **ALL §1.1 / P8 CHECKS PASS**; colour set core 19 = edition 19; badges A2 #5c6e30 / B1 #46581f / B2 #37402f present; P8 min font **13.5 pt** (≥10 required) (`check_s11.log`) |
| **verify_ed.py (nl)** | RC=0, **VERIFY ALL PASS** — Q39 a / Q40 d / Q46 A / Q52 hosted / Q55 won / Q125 A + notes; text.md 150 answers; no stale Ashes phrasing; **P8 min PDF font 10.12 pt (≥9.75 floor)**; **SVG zero real CJK (only U+3000 allowed)** (`verify_ed.log`) |
| **creambox.py canonical (all 8 SVGs, raw)** | RC=0, **0 OVERFLOW**; every raw negative clearance is the next section head 35.5–37.0 px BELOW the box bottom, caught by the tool's +45 tolerance (`creambox-all.log`) |
| **creambox strict re-measurement (own content only)** | **PASS.** All 32 `#f0eee5` boxes have POSITIVE own-content clearance (**+5.0 to +92.4**); tightest P2 y=1211 +5.0 ("Engels voor de redactie."); P7 TOOLBOX +48.5; P8 MODEL +92.4. The P2 box's desc-clear −1.0 is the 0.30×font-size heuristic only — true descender depth ≈4.2 px < 5.0 px clearance, and the P2 render shows the line inside the box. (`creambox-strict.log`) |
| **spill sweep (BELOW-WINDOW lines)** | All 22 BELOW-WINDOW lines are first lines of the next block (section heads: TRY IT NOW, WHAT IS ON THIS WEEK?, THE WORD OF THE WEEK, COMPREHENSION, FIVE SENTENCES, FRIDAY'S WORDS, READ THE CHART, FIFTY ELECTIONS, READERS' CORNER; or article openers), 35.5–37.0 px below the box bottom. **No box-content line spilled outside its box.** (grep of `creambox-all.log`) |
| **boxtitle sweep (source)** | 12/12 fit; tightest HOW LONG? +20.3, ODD SOCKS +20.6 — PASS (`boxtitle-src.log`) |
| **boxtitle sweep (SVG, advance)** | 18/18 fit; overflows 0; SENATE IN NUMBERS +66.6, SATURDAY, NOV 21 +70.5 — PASS (`boxtitle-svg.log`) |
| **boxtitle sweep (SVG, PIL true-ink, all 18)** | **18/18 OK, 0 failures**; worst horizontal true-ink margin **+20.5** (ODD SOCKS / HOW LONG?), worst vertical top ink margin **+45.0** — PASS (`boxtitle-ink.log`) |
| **registry vs appendix** | **0 mismatches / 150**; appendix continuous 1–150; per-page 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22 (`crosschecks.log`) |
| **orphan punctuation sweep** | 0 orphan-start `<text>` lines on all 8 SVGs; 0 orphan-start lines in text.md — PASS (`crosschecks.log`) |
| **quote balance** | text.md “ 85 / ” 85; « 0 / » 0. Per-SVG “/” balanced all 8 pages (P1 2/2, P2 1/1, P3 10/10, P4 3/3, P5 11/11, P6 2/2, P7 29/29, P8 26/26); «/» 0 everywhere (`crosschecks.log`) |
| **banned words** | text.md: "W47"/"2026-W47" only on line 1 (file header, house convention); "cover"/"SOP"/"proofread" 0. SVG `<text>` elements: **0 banned tokens** on all 8 pages. "VOL." 18× = the issue's own VOL.3/4/5 labels in reader copy (VOL.4 5×, VOL.5 9×, VOL.3 3×, "VOL. 4" masthead 1×) (`crosschecks.log`) |
| **D5 fonts (count only, not judged)** | Newsreader 1023, Noto Sans CJK SC 663, Noto Serif CJK SC 27, DejaVu Sans 4, UnifrakturMaguntia 1 — identical to proof1 (`crosschecks.log`) |
| **visual inspection** | fresh pdftoppm renders (100 DPI) of all 8 print pages + web P1/P8, viewed in `render/`: no overflow/overlap/clipping; footers "Pagina N van 8" on all pages; P8 answers print "73. up"; MODEL box ends well above the footer; web P1/P8 visually identical to print P1/P8 |
| **old-vs-new per-page compare** | vs delta's renders of this same build (threshold >30): **P1–P8 0.00% (pixel-identical)** — my renders reproduce the delta build exactly (`oldnew-diff.log`). Pre- vs post-delta change is established independently by the SVG byte diff (p1–p7 identical, p8 Q73 reflow only). |

## Answer-key verification (manual, 150/150 vs stems — this round)

- All 150 keys read stem-by-stem across registry.json, text.md bodies + appendix, P8
  extracted keys, and the rendered P5/P8 SVGs where keys print. **Zero mismatches.**
  Full per-key record is in PROOF-NOTE.md (Q73 `up` verified four-way; Q107 `win`
  headline present; Q108–111 error-clinic corrections; Q112 Tuesday = Nov 3, 2026;
  Q137–140 Dutch translations; Q145–149 dialogue row/film/popcorn/show/Friday).
- Carry-forward four-way check Q39/40: registry (39=a, 40=d) × text.md (lines 1083/1085)
  × P8 extracted (39='a', 40='d') × P3 SVG defs — all agree.
- Q46/52/55/125: registry = text.md = P8 extracted (A / hosted / won / A); Q46 stem and
  Q125 stem verified in the P4/P8 SVGs.
- Matching sets verified: P2 D (24 b, 25 c, 26 a, 27 d), P3 C (38 b, 39 a, 40 d, 41 c),
  P4 C (56 b, 57 c, 58 d, 59 a), P5 C (74 d, 75 a, 76 b, 77 c), P8 F (141 b, 142 c, 143 d, 144 a).
- P6 chart arithmetic 254+162+19=435 ✓. P7 golden sentences 8/8 verbatim ✓. MODEL text
  82 words (80–100) ✓.
- Per-page counts 10/17/18/18/18/18/12/39 = 150; A2 62 / B1 66 / B2 22; numbering continuous 1–150.
- Weekdays for all named dates verified while reading; the only 2025 date (Friday,
  November 21, 2025) is correctly a Friday.
- Pre-existing duplicates carried over unchanged (not flagged): Q6/Q12 same stem
  ("The new Congress meets in ___ 2027."); Q2/Q95 key `call`; Q5/Q96 key `changed`.

## Script-invocation fixes during this proof (gates re-run clean, no gate skipped)

- keycheck.py first run failed `ModuleNotFoundError: tr_nl` — copied `tr_nl.py` from
  proof1 scratch into this scratch, re-ran: RC=0, 149/150.
- creambox_inside.py / sweep_titles.py / sweep_svg_titles.py first invoked with wrong
  arguments (dir instead of glob pattern; missing `nl` arg) — re-ran with the correct
  invocations from delta's `delta-gates.sh`: all RC=0.
