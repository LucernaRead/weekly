# PROOF-NOTE — Lucerna Weekly 2026-W47, edition en-nl (proof2, post-delta)

- **Edition:** English target, Dutch reader (`production/2026-w47/2026-w47-en-nl/`)
- **Proofreader:** independent proof2 (SOP §8.4); not the delta agent, not the builder.
- **Date:** 2026-11-11 (Toronto, America/Toronto)
- **Scope:** delta build only. Full re-proof of the delta'd build, not a copy of proof1:
  full text.md read (1,305 lines); 150/150 answer keys checked stem-by-stem against
  registry.json, text.md appendix, P8 extracted keys, and the rendered P5/P8 SVGs where
  keys print; 8 print pages + web P1/P8 visually inspected from fresh renders of the
  delivered PDFs; all mechanical gates re-run (see GATE-LOG.md).
- **Delta under proof:** content56.py Q73 key `"speak"` → `"up"` only (core-en fix2 sync).
  Every delta claim was independently re-verified (see §Delta verification).

## Conclusion: (a) — 定稿，零缺陷 (final, zero defects)

The Q73 delta is correct and complete in all four sources, and no other defect was found
in the full re-proof. Proof1's conclusion (a) carries over: its 4 fixed defects are verified
still fixed, and the delta touched exactly one key, one text line, and one SVG page.

---

## File identity (measured before proofing; all three match the task values exactly)

| file | size (B) | SHA-256 |
|---|---|---|
| print `The-Lucerna-VOL4-en-nl.pdf` | 29,341,267 | `f1e1e511bd780243878f767c73d92f22ff6407718fbde7dbe209068938e87dca` |
| web `The-Lucerna-VOL4-en-nl.web.pdf` | 2,411,546 | `c1a0828865d9a293b7e2be1e3f6cec674f7b1f1ca8193049c2c43906e1c509a8` |
| `2026-w47-en-nl.text.md` | 53,565 | `30bfb6f93860fae5ae58707c28c4f2e3a18ebcc07e272681e67688451d12c0be` |

Both PDFs are 8 pages (`pdfinfo` via render: 1462.5 × 2025 pts, as in delta-note).
Probe before any work: `/dev/null` present, `git hash-object -w` OK
(`da0c4eb8d9a48d171a33574b380752e183286751`), probe file written in this scratch dir.
No repo-side writes by this proof (all artifacts in this goals-side scratch dir only;
`git status` shows the edition dir as untracked — pre-existing state, same as proof1;
the `issues/2026-w43` diff visible during this proof is other agents' parallel work,
not mine; no commit/push made).

Core-en (measured before AND after proof; unchanged throughout):
- print `The-Lucerna-VOL4-en-zh-cn.pdf` — 41,407,287 B,
  `08cbc1e53f2d02d6c64266d1f64ac2422eaa2f8f71e1829f877e94a5627b3213`
- web `The-Lucerna-VOL4-en-zh-cn.web.pdf` — 2,804,281 B,
  `d7927eaad14531a9aee71331d4e27abbf951a296f6b6ee5fb1c770f8c7f7e444`
- text `2026-w47-en-zh-cn.text.md` — 51,402 B,
  `23855d4bd60abe4a7fb4db42050cb9343202e85789ffd434634808d299215c69`
All three equal the fix2 values in DELTA-NOTE §9. Core was not touched.

## Delta verification (independent; DELTA-NOTE's §4 claims re-measured, not trusted)

- **registry diff vs `registry.pre.json`: exactly 1 entry** — n=73 `key: 'speak'` → `'up'`;
  all other 149 entries byte-identical; total still 150
  (`gates/delta-verify.log`).
- **text.md diff vs `text.pre.md`: exactly 1 line** — line 1151:
  `73. [A2] Zinnen aanvullen — speak (speak up = je uitspreken)` →
  `73. [A2] Zinnen aanvullen — up (speak up = je uitspreken)`.
- **SVG diff vs `svg.pre/`: p1–p7 byte-identical; only p8-test.svg changed**
  (`530c9d35…` → `ee35fc68…`, matching DELTA-NOTE §4). P5 byte-identical by design:
  the Q73 key only ever prints on the P8 answers page; P5 prints only the stem and the
  `speak up` gloss — p5-unchanged is the correct expectation, not an anomaly.
- **P8 stripped-text diff pre vs cur: same 259 `<text>` elements; only 5 lines reflowed**
  (`73. speak` → `73. up` plus reflow of `76. b …`, `socks today.`, `We are …`) —
  no word added, removed, or altered.
- **Q73 four-source evidence (all `up`):**
  - registry.json Q73: `{'n': 73, 'page': 5, 'level': 'A2', 'type': 'Zinnen aanvullen',
    'key': 'up', 'note': 'speak up = je uitspreken'}`
  - text.md line 1151: `73. [A2] Zinnen aanvullen — up (speak up = je uitspreken)`
  - P8 SVG: `73. up` present, `73. speak` absent (SVG text + print-PDF render + web-PDF
    render all show "73. up · 74. d")
  - P5 SVG: stem `Speak ___: tell a teacher.` present; gloss `to speak up = je uitspreken`
    present in the Uitleg box; `up` in "Speak ___" is the correct phrasal verb
    (speak up = tell a teacher — matches the note, the article, and core-en
    `content56.py:49` key `"up"`, verified read-only).
  - core-en `content56.py:49`: key `"up"` (edition line identical except the Dutch
    note/gloss wording).

## Carry-forward verification (proof1's 4 defects + ABSTRACT → this build)

1. **Q39→a / Q40→d — still fixed, four-way consistent.** Registry 39=a, 40=d; text.md
   lines 1083/1085; P8 extracted 39='a', 40='d'; P3 SVG defs unchanged (P3 byte-identical
   to pre-delta, which is correct: no key letter prints on P3).
2. **Ashes staleness — still fixed.** P4 remains the 2025–26 retrospective (read in full,
   lines 439–451); no stale phrasing reintroduced (delta touched nothing outside Q73).
3. **P7 NEXT WEEK "certified results" — still fixed.** "More certified results of the
   midterm election" (line 883), comparative, unchanged.
4. **Dutch guillemets « » — still 0** in text.md, registry.json, all 8 SVGs, content*.py
   (re-measured: text.md “ 85 / ” 85, « 0 / » 0; per-SVG balanced).
5. **ABSTRACT — full form, unchanged.** (Not re-read in this round beyond the carried
   proof1 verification; delta touched no ABSTRACT/KIT file except the KIT SHA+delta entry,
   and the edition file set differs from proof1 only by the Q73 delta — verified by the
   registry/text/SVG diffs above.)

## Full 150-key verification (manual, stem-by-stem, this round)

- Registry vs text.md appendix keys: **0 mismatches / 150** (scripted parse; appendix
  continuous 1–150).
- Registry vs P8 extracted keys: **149/150 exact** (keycheck RC=0); the single mismatch is
  n=150, the known extractor truncation of the open-question long label ('Open vraag' vs
  the full registry note).
- Registry vs core P8 keys: **145/150** — the 5 keydiffs are exactly [137, 138, 139, 140,
  150] (reader-language translation keys + writing key — expected, p8 compare CLEAN).
- Every key read against its stem in text.md (bodies + appendix). Spot record:
  Q1–6 midterm/call/seats/majority/changed/January; Q11 November, Q13 `1`, Q15 `27`;
  Q16–19 will meet/will certify/will travel/"Will they watch…?"; Q24–27 b/c/a/d;
  Q34 opens, Q35 mentor, Q36 twice, Q37 jungle; Q38–41 b/a/d/c; Q42–45
  published/won/painted/chose; Q46 A, Q47 C, Q48 B, Q49 A, Q50 C, Q51 B; Q52 hosted,
  Q53 lasts, Q54 eight, Q55 won; Q56–59 b/c/d/a; Q60–63 lost/lost/ended/beat; Q64–69
  B/A/C/B/A/C; Q70 silence, Q71 socks, Q72 rights, **Q73 up**; Q74–77 d/a/b/c; Q78–81
  are wearing/are speaking/are listening/is sitting; Q82–87 B/C/A/B/A/C (chart 254+162+19
  = 435 ✓); Q88–93 B/A/C/B/A/C; Q94 certify, Q95 call, Q96 changed, Q97 takes,
  Q98 differs, Q99 official; Q100–107 won/more/lost/will/published/whether/chose/win
  (Q107 `win`: headline present tense, correct); Q108–111 error-clinic corrections
  won/continued/more than/whether — each correct against the wrong sentence shown;
  Q112–119 Tuesday/call/continues/will meet/writes/will certify/wears/will watch
  (112 Tuesday: Nov 3, 2026 is a Tuesday ✓); Q120–128 B/A/C/B/A/A/B/A/C; Q129–132
  B/A/C/B; Q133–136 will meet/won/more/whether; Q137–140 correct Dutch translations;
  Q141–144 b/c/d/a; Q145–149 row/film/popcorn/show/Friday (dialogue fits); Q150 open
  question (extractor truncation only).
- Matching sets re-verified against the SVG defs as printed: P2 D (24 b, 25 c, 26 a, 27 d),
  P3 C (38 b, 39 a, 40 d, 41 c), P4 C (56 b, 57 c, 58 d, 59 a), P5 C (74 d, 75 a, 76 b,
  77 c), P8 F (141 b, 142 c, 143 d, 144 a).
- Per-page counts 10/17/18/18/18/18/12/39 = 150; levels A2 62 / B1 66 / B2 22;
  numbering continuous 1–150. MODEL text 82 words (80–100 required) ✓.
- Golden sentences 8/8 verbatim against this issue's articles (checked line by line while
  reading: P2, P1, P4, P6 ×2, P3, P5, P1).
- Weekdays: every "Weekday, November N" in text.md re-checked while reading — Nov 3 Tue,
  Nov 8 Sun, Nov 9 Mon, Nov 10 Tue, Nov 16 Mon, Nov 20 Fri, Nov 21 Sat, Nov 22 Sun,
  Nov 26 Thu, Nov 27 Fri — all match 2026; the 2025 date "Friday, November 21, 2025" is
  correctly a Friday.
- Pre-existing duplicates carried over unchanged from proof1 (not flagged, same as proof1
  and delta-note §7): Q6/Q12 share the stem "The new Congress meets in ___ 2027.";
  Q2/Q95 share key `call`; Q5/Q96 share key `changed` (different pages/levels).

## Visual check (fresh renders from the delivered PDFs, `render/`)

- `render/p-1.png` … `p-8.png` (pdftoppm, 100 DPI, from the delivered print PDF) +
  `web-p1-1.png`, `web-p8-8.png` (from the delivered web PDF). All 8 pages + web P1/P8
  viewed: no overflow, overlap, clipping, or cut-off text; footers "Pagina N van 8" on
  all pages; P3 matching block, P7 toolbox / readers' corner, P8 answers block all as
  expected; P8 answers print "73. up" and end well above the footer; MODEL box clean.
  Web P1/P8 visually identical to print P1/P8.
- P5: Q73 stem + gloss clean; the widowed "D PRESENT CONTINUOUS" head at the bottom of
  column 2 is the carried-over proof1 observation (readable, untidy only).
- P1 SEARCHES bars, P2 SAY IT three panels (all inside), P4 Grace photo + "SATURDAY,
  NOV 21" box, P5 children photo + "ODD SOCKS, IN NUMBERS" box, P6 voting-booth photo +
  practice ballot, P7 Johnson portrait (Samuel Johnson, 1772) all clean.
- Old-vs-new pixel diff vs delta's renders of this same build (threshold >30):
  **P1–P8 0.00% (pixel-identical)** — my renders reproduce the delta build exactly.
  (Pre- vs post-delta diff was already established by the SVG byte diff: p1–p7 identical,
  p8 reflow confined to the Q73 region — see §Delta verification.)

## Observations (not defects — same carried-over items as proof1)

1. **Widowed section head (cosmetic):** P5 "D PRESENT CONTINUOUS" head sits at the bottom
   of column 2 with its instruction line split across the column break ("Herschrijf in de
   tegenwoordige tijd (wat er" / "nu gebeurt).") and items 78–81 at the top of column 3.
   Readable, just untidy. Same as proof1; P5 is byte-identical to the proof1 build.
2. **P5 "FRIDAY'S WORDS":** "Elk kind heeft rechten | Every child has rights = Elk kind
   heeft rechten." — the gloss repeats the Dutch. Harmless TM carryover, unchanged.
3. **"Rafael Jodar"** spelled without the accent in body text and SVG (Spanish: Jódar).
   Diacritic dropped in English body text; not a factual error.
4. **P4 "they lost 4–0 on their last two tours, in 2017–18 and 2021–22"** (text.md line 445;
   core-en line 445, verbatim core wording) — checked in proof1, not flagged: past-perfect
   anchored to the eve of the 2025–26 series, explicit years pin it to those tours, and
   the same article states 2025–26 was 4–1 with England winning in Melbourne.
5. **D5 fonts (recorded only, not judged):** SVG font-family counts — Newsreader 1023,
   Noto Sans CJK SC 663, Noto Serif CJK SC 27, DejaVu Sans 4, UnifrakturMaguntia 1 —
   identical to proof1.

## Checked and NOT flagged (with reasoning)

1. **P2 tightest cream box (y=1211, baseline clearance +5.0, desc-clear −1.0 by the
   0.30×font-size heuristic):** the heuristic is conservative — the last line "Engels voor
   de redactie." (20 pt) has true descender depth ≈4.2 px < 5.0 px clearance, and the P2
   render shows the line fully inside the AND YOU? box with no ink crossing the edge.
   Same value as proof1's PASS; P2 is byte-identical to the proof1 build. Not a defect.
2. **"VOL." 18× in text.md** (proof1 reported 13× under a narrower count): all 18 are the
   issue's own volume labels — VOL.4 (5×), VOL.5 (9×), VOL.3 (3×), "VOL. 4" masthead (1×)
   — in reader-facing copy, not internal structure.
3. **All 22 BELOW-WINDOW lines in the creambox raw scan** are first lines of the next
   block (section heads or article openers, 35.5–37.0 px below the box bottom), not
   spilled box content — verified line by line in the spill sweep.
