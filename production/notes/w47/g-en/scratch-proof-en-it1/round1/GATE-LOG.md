# GATE LOG — Lucerna Weekly 2026-W47 · en-it · proof1

**Date:** 2026-11-11 · **Proofreader:** independent proof1 · **Conclusion: (b) defect list — D1 + D2 (see PROOF-NOTE.md)**
**Scratch:** `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-it1/`
**Edition:** `~/workspace/weekly-git/production/2026-w47/2026-w47-en-it/`
**Core:** `~/workspace/weekly-git/production/2026-w47/core-en/`

## 0. Probe (before work)
- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4` ✓
- `probe.txt` written in scratch ✓. `/tmp` avoided throughout (TMPDIR=<scratch>/tmp).

## 1. SHA verification — all MATCH
Print PDF `The-Lucerna-VOL4-en-it.pdf`: 29,326,709 B, SHA-256 `195e155228e63515d3133a32cebbbee71c3dccf973387d4c1c2f614670e3da26` ✓
Web PDF `The-Lucerna-VOL4-en-it.web.pdf`: 2,372,517 B, SHA-256 `995339d48612cc9344a5213e38026a9cda9a1de910efb268308fa9e877064a46` ✓
text.md `2026-w47-en-it.text.md`: 53,373 B, SHA-256 `a9cbd2f18c6ecfeebf86dfe68558ab9d1145ce7fc4476b8004b610bb7e4805ec` ✓
Both PDFs 8 pages (pdfinfo).

## 2. Full text read
`text.md` read in full (~1,306 lines). All 150 answers checked against stems: 148 correct, 2 wrong (D1, Q39/Q40). Per-page counts 10/17/18/18/18/18/12/39 = 150 (A2 62 / B1 66 / B2 22, matches KIT §1).

## 3. Occlusion audit — 0 flags ✓
`tools/venv/bin/python tools/occlusion_audit.py` on edition `svg/`: selftest OK (all 6 planted classes fired, clean controls silent), **0 flags**, RC=0.
Files: `gates/occlusion.log`, `gates/occlusion.json`.
Note: audit is blind to the D2 class (text wider than its box, drawn after the box, nothing covering it) and to wrong keys that are consistent across sources (D1).

## 4. p8 extract + compare — CLEAN ✓ (with itemised keydiff)
`tools/p8.py extract` (edition P8): **60/150 noted** (same set as core).
`tools/p8.py compare` core vs edition: **CLEAN**, missing=[] extra=0, keydiff=[137, 138, 139, 140, 150].
Keydiff itemised: 137–140 are Italian translations vs core Chinese (legitimate re-aim, same meaning); 150 is the open writing task ("Compito aperto" vs core "开放题"). No defect.
Files: `gates/p8-extract.json`, `gates/p8-extract-core.json`, `gates/p8-compare.json`, `gates/p8-compare.log`.

## 5. Registry / text.md / P8 cross-check — zero mismatches ✓
Scripted comparison of all three pairings (registry vs text.md, P8 print vs text.md, registry vs P8 print): **zero mismatches** on 150 keys.
Apparent exception only: registry key 150 is the long dash form; p8 extract splits "Compito aperto" from its note — full text is printed on P8 (SVG grep confirmed), not a defect. Matches KIT §10's known p8.py FOOTER_RE note.

## 6. freeze — 8/8 byte-identical; diff added CJK = 9× U+3000 only ✓
`tools/freeze.py baseline` (core-en rebuild): **8/8 byte-identical**, RC=0, core SVGs unchanged.
`tools/freeze.py diff` core vs edition: added CJK = only **9× U+3000** ideographic-space separators (P1: 2, P2–P8: 1 each), no added CJK text, RC=0.
Files: `gates/freeze-baseline.log`, `gates/freeze-diff.log`, `gates/freeze-diff.json`, `gates/freeze/`.
Independent CJK scan of edition SVGs: zero non-U+3000 CJK characters (P1 22, P2 18, P3 13, P4 14, P5 13, P6 13, P7 24, P8 24 — all U+3000 separators).

## 7. Print vs web text layer — identical ✓
pdftotext -layout: print 111,889 B / web 111,893 B; **token-multiset diff 0/0**. Web PDF text layer non-empty.
Files: `gates/print.txt`, `gates/web.txt`.

## 8. P8 minimum font — 10.12 pt, ≥ 9.75 floor ✓ (observation: KIT claims 13.5)
PyMuPDF via tools venv, both PDFs: **10.12 pt** on P8 (smallest spans are answer-note lines) and all-pages min. Passes SOP §1.1 floor (9.75 pt). KIT §3's "13.5 pt" is the configured answers-block font size, not the measured minimum span. Not a defect.

## 9. Creambox (P7 toolbox) — PASS, all 32 boxes positive ✓
Raw `creambox.py` on all 8 SVGs shows many negative clearances (−35 to −37) — **known false positives** (de fix log): the +45 px window below each box catches the following section heading / exercise numbers in the same column.
Corrected measurement (texts actually inside each box only): **all 32 cream boxes across 8 pages have positive inside-clearance** (min +5.0, most +44 to +48.5).
P7 TOOLBOX (x=1440, y=651, bottom=1008.2): last baseline 959.7, clearance **+48.5**; raw −37.0 was the "READERS' CORNER Lettere" heading at y=1045.2 below the box. **No vertical toolbox spill.** Visually confirmed (`render/p7-toolbox.png`).
Tightest: P2 AND YOU box (x=1440, y=1184, bottom=1517.9), last baseline 1512.8, clearance +5.0 ("redazione." — no descender letters, ink ends at baseline, ~5 px inside). Observation, not a defect.
Scan artifact: corrected scan reported P2 box x=610 y=1636 EMPTY — false; its texts start left of the box (see gate 10, D2).
Files: `gates/creambox.log`, `gates/creambox-corrected.log`.

## 10. Horizontal overflow scan — 3 real hits = D2 (MODERATE)
PIL true-ink scan of all cream boxes, membership = ink overlap ≥ 0.5 with the box:
- P2 SAY IT box2 (x=610–890): EN "The new Congress meets in January." ink 574.0–926.0, spill **+36.0 / +36.0**; IT "Il nuovo Congresso si riunirà a gennaio." ink 568.2–932.2, spill **+41.8 / +42.2**.
- P2 SAY IT box3 (x=1060–1340): IT "Buon Giorno del Ringraziamento!" ink 1045.1–1355.1, spill **+14.9 / +15.1**.
- Box1 clean (EN margins 22/22, IT ~11.5); box3 EN "Happy Thanksgiving!" margins ~35.
**TOTAL real hits: 3.** Visually confirmed (`render/p2-sayit.png`, `render/p-2.png`).
Root: box2 EN line identical in core-en (x=574.0) → core-rooted; Italian lines edition-local (core Chinese lines fit).
Files: `gates/h-overflow.log` (broad scan, loose filter — full of neighbouring-column false positives, do NOT cite as evidence).

## 11. Boxtitle width — 31/31 fit ✓
Every cream box's first (title) line ink right edge vs its box right edge: all inside. Tightest: P2 "THE SENATE, IN NUMBERS Il Senato" margin +6.5 px (visually confirmed inside). P7 "THE TOOLBOX Strumenti" margin +119.5.
File: `gates/boxtitle.log`.

## 12. keycheck (equivalent) — 149/150, only expected Q150 ✓
`registry.json` (150 entries) vs `p8-extract.json` (150 keys): **149/150 exact**. Sole mismatch n=150: key 'Compito aperto — punti chiave nel riquadro di scrittura; testo modello nel riquadro a pagina 8' vs extracted 'Compito aperto' — the expected p8.py extractor truncation of the long open-task key (key starts with extracted). Same expected exception as the de keycheck.
File: `gates/keycheck-150.json`.
(Note: the de `keycheck.py` is family-specific — imports `tr_de` / core-de `svglib`; there is no en-it `keycheck.py` in `scratch-fanout-en`. The equivalent comparison above was run directly on en-it `registry.json` + `p8-extract.json`.)

## 13. Quote / apostrophe pairing — balanced ✓
text.md: “ 81 / ” 81, ‘ 0, ’ 0, straight " 0. All 8 SVGs: “ = ” per page (P1 2/2, P2 1/1, P3 10/10, P4 3/3, P5 11/11, P6 2/2, P7 29/29, P8 24/24), 0 straight quotes. Apostrophes are ASCII ' per KIT §8 normalisation.

## 14. Forbidden terms — 0 in reader-facing text ✓
18-term scan (SOP, proofread, placeholder, lorem, TODO, XXX, TBD, W47, 2026-W47, en-it, cover, bridge, internal, draft, SOP.md, geometry audit, frontmatter, registry) on visible text only (SVG `<text>` elements + text.md body):
- All 8 SVGs: 0 real hits (raw grep hits were base64 image data; the 2 "SOP" substrings are Italian "sopra"/"soprattutto").
- text.md: hits are "sopra"/"soprattutto" (Italian), "2026-W47" in the source header line 1 only, and "registry" in the source file's own answer-list headers — none of which are printed in the PDF.

## 15. External fact checks — all confirmed, no contradictions
Weekdays/dates via `date -d` (America/Toronto): Nov 3 Tue, Nov 8 Sun, Nov 9 Mon, Nov 10 Tue, Nov 15 Sun, Nov 16 Mon, Nov 18 Wed, Nov 19 Thu, Nov 20 Fri, Nov 21 Sat, Nov 22 Sun, Nov 26 Thu (Thanksgiving, 4th Thursday), Nov 27 Fri, Dec 1 Tue, Dec 18 Fri — all consistent with the paper.
Web sources confirmed: US midterms AP calls (House 254D/162R/19 uncalled; Senate 20D/13R of 33; 7 Senate flips Iowa, Kansas, Maine, North Carolina, Ohio, South Carolina, Texas; 5 governors flipped Georgia, Iowa, Nevada, Ohio, Texas; pre-vote 218R–214D / 53R–47D; new Congress Jan 3, 2027); Mike Johnson will not run to lead House Republicans (NBC/AP, Nov 4; House GOP leadership vote Tue Nov 10); Hunger Games: Sunrise on the Reaping (theatres Fri Nov 20; Joseph Zada as 16-yr-old Haymitch, McKenna Grace as Maysilee Donner, Ralph Fiennes as young Snow, Francis Lawrence directing; novel Suzanne Collins, March 2025; 50th Games / Second Quarter Quell, twice as many tributes; soundtrack album Nov 13, 29 tracks); I'm a Celebrity s26 (Mon Nov 16, 9 p.m., ITV1/ITVX, Ant & Dec, Murwillumbah; launch one day late because England–Spain Nations League Sun Nov 15; "How to Survive the Jungle" special Sun Nov 15; Unpacked ITV2; campmates not yet confirmed); Ashes 1st Test Perth Sat Nov 21 (first ball 10:20 local = 02:20 London; Cummins out with lumbar stress injury, Steve Smith captains, Scott Boland in; Hazlewood out with hamstring strain; Brendan Doggett may debut; England last series win in Australia 2010–11, lost 4–0 in 2017–18 and 2021–22, 2023 drawn; Australia lost first Perth-Stadium Test Nov 2024 by 295 runs to India); ATP Finals Turin Nov 15–22 (field Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Tiafoe, Jódar; Sinner two-time defending champion out with right knee injury, season ended Oct 6; semis Sat Nov 21, finals Sun Nov 22); Premier League Sat Nov 21 Man City–Fulham 12:30, Newcastle–Arsenal 17:30; Sun Nov 22 Liverpool–Man Utd 16:30; international break Nov 9–17; NFL Week 11 Colts–Texans Thu Nov 19 8:15 p.m. ET, Vikings–49ers Mexico City Sun Nov 22 8:20 p.m. ET, Patriots bye after Munich Sun Nov 15; Anti-Bullying Week Nov 16–20 theme "Break the Silence", Odd Socks Day Mon Nov 16, 10th anniversary, organised by Anti-Bullying Alliance, theme shaped by 200+ children, ~8 million children / 80%+ schools (ABA's own figures); World Children's Day Fri Nov 20, CRC adopted 1989; Georgia runoff Dec 1 = 28 days after Nov 3.
Not independently verified (no contradiction): Ashes day-one sold out; ATP singles final not before 6 p.m. local; World Children's Day 2026 theme; House Democrats leadership vote Nov 18–19.
Minority figure noted: one aggregator (political.org) showed House 252/161/22 vs the paper's 254/162/19 — paper matches the majority of sources.

## 16. Visual check — print 8/8 + web P1/P8 read
`render/p-1.png`…`p-8.png` (print, 110 dpi) and `render/w-1.png`, `render/w-8.png` (web) all read. Clean except D2 (P2 SAY IT, visible at full-page scale) and the P3 def order confirming D1. P7 toolbox clean (`render/p7-toolbox.png`). P8 answers block ends above the footer; MODEL text present; "Levels: 145–149 [A2]" present; cloze options carry [A2]/[B1] tags.

## Gate summary

| Gate | Result |
|---|---|
| SHA (print/web/text.md) | MATCH |
| Full text read (150 keys vs stems) | 148 ✓ / 2 ✗ (D1) |
| Occlusion audit | 0 flags |
| p8 extract / compare | 60/150 noted; CLEAN, keydiff [137,138,139,140,150] itemised |
| Registry / text.md / P8 cross-check | 0 mismatches |
| freeze baseline / diff | 8/8 identical; added CJK 9× U+3000 only |
| Print vs web text layer | token-multiset 0/0 |
| P8 min font | 10.12 pt (≥ 9.75 floor) |
| Creambox (P7 toolbox) | +48.5; all 32 boxes positive |
| Horizontal overflow | 3 real hits (D2) |
| Boxtitle width | 31/31 fit |
| keycheck-equivalent | 149/150 (only expected Q150) |
| Quotes balanced | ✓ |
| Forbidden terms | 0 |
| External facts | confirmed, no contradictions |
| Visual (print 8/8, web P1/P8) | clean except D2 |
