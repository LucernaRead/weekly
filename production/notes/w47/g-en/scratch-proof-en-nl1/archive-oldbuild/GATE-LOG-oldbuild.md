# GATE-LOG — W47 en-nl proof1

- **Edition:** `production/2026-w47/2026-w47-en-nl/`
- **Run:** 2026-11-11 (UTC). All gates run in `scratch-proof-en-nl1/`; `TMPDIR=<scratch>/tmp` (nothing written to /tmp).
- **Core integrity:** core-en untouched throughout (freeze direct-SHA check 8/8 MATCH; see below).

## File identity (verified before proofing; KIT §7 + `sha256sum`)

| file | size (B) | sha256 (full) |
|---|---|---|
| print `The-Lucerna-VOL4-en-nl.pdf` | 29,340,703 | `5b2a364b60fb55372e2ceada5e19b48cbdaa6e14b3ef8872d6e75322eff18e05` |
| web `The-Lucerna-VOL4-en-nl.web.pdf` | 2,375,438 | `f1d2b8f43600e39af4aa1677db61f84820bef07ee9b826828e28704c55a9d94c` |
| `2026-w47-en-nl.text.md` | 52,965 | `3e21e424fbc2237a1d3d75266510ef9cbbd5fb0d96f86f5e0f28b37c1736b0de` |

All match the task values. Both PDFs 8 pages (`pdfinfo`).
Probe: `git hash-object` OK (`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`); probe file written in scratch.
Note: `/tmp` was in fact only 3% used at probe time, but scratch tmp was used throughout anyway per the task.

## Gates

| gate | result |
|---|---|
| **Occlusion audit** | selftest OK (all 6 classes fired, clean controls silent); **0 flags** — PASS |
| **p8 extract** | edition 150 keys; noted set 60/150; noted set **identical to core's** — PASS |
| **p8 compare** | **CLEAN**; missing=[]; extra=0; keydiff=[137,138,139,140,150] (reader-language translation keys + writing key — expected) |
| **keycheck.py** | RC=0; REG 150, p8extract 150, exact match **149/150**; only mismatch n=150 (key 'Open vraag — punten…' vs extracted 'Open vraag' — expected extractor truncation). `keycheck-150.json` written. Note: first run failed FileNotFoundError (expected `p8extract.json`, found `p8-extract.json`); fixed by copy, re-ran clean. REG vs `registry.json`: **0 mismatches**. Registry vs text.md appendix: 7 apparent mismatches were regex false positives (key + parenthetical note); 0 real mismatches. |
| **freeze baseline** | **8/8 SVGs byte-identical**; core integrity unchanged — PASS |
| **freeze direct sha** | **8/8 MATCH** — PASS |
| **freeze diff** | added CJK = **9× U+3000 only** — PASS |
| **print/web text diff** | 47,442 vs 47,444 chars; 2,464 distinct tokens each; token multiset diff **0/0** — PASS |
| **check_s11.py (nl)** | RC=0, **ALL §1.1 / P8 checks PASS**; colour set core 19 = edition 19; badges A2 #5c6e30 / B1 #46581f / B2 #37402f; Q113–120 [A2] tag, "Levels: 145–149 [A2]", Q120 chip, H WRITING head all present |
| **P8 min font** | **13.5pt** (≥11.25 target, ≥9.75 floor — no concession) — PASS |
| **creambox.py (all 8 SVGs)** | **PASS.** Raw output showed negative clearances (e.g. −35.5/−37.0) — proven artifacts on strict re-measurement: own-content clearance for every `#f0eee5` box is **POSITIVE (+5.0 to +92.4)**; negatives are the next heading/line below the box caught by the tool's +45 tolerance (identical values in the sibling clean `scratch-proof-en-ja1` log). **P7 TOOLBOX box y=651, bottom=1008.2, own last baseline 959.7, clearance +48.5 — no ink past the box bottom.** Tightest box P2 y=1184, +5.0 ("Engels voor de redactie.") — positive, fine. Visually confirmed in the P7 render. |
| **boxtitle / title-gap scan** | **0 tight title neighbours** — PASS (P2 "THE SENATE, IN NUMBERS　Senaat" fix holds; visually confirmed with clear gap) |
| **quote balance** | text.md “ 81 / ” 81 ✓; « 4 / » 4 ✓; straight `'` ×44 (apostrophes, per TM rule normalizing U+2019→`'`). Per-SVG “/” balanced all 8 pages (P1 2/2, P2 1/1, P3 10/10, P4 3/3, P5 11/11, P6 2/2, P7 29/29, P8 24/24). « only on P8 (literal count 2 in the SVG source; the render shows the guillemets in the H instruction and in answer notes 65 and 126 — some are entity-encoded in the SVG, hence the count gap) |
| **banned words** | text.md: only "W47"/"2026-W47" on line 1 (file header, identical to core line 1 — house convention, not a defect). SVG `<text>` elements: **0 banned tokens** — PASS |
| **CREDITS.md** | all images PD/CC0 with sources — capitol (Noclip), turkey (Audubon), tiger (Rousseau, *Surprised!* 1891), grace (W. G. Grace, Barraud), children (Bain/Lawrence 1912), voting (Zirkel CC0), johnson (**Samuel** Johnson 1772, Reynolds), readingroom (Highsmith). football1910.jpg NOT used — PASS |
| **visual inspection** | fresh CairoSVG renders (975×1350) of all 8 print pages + `pdftoppm` web P1/P8, viewed with `muse.read` in `scratch-proof-en-nl1/render/`: no overflow/overlap/clipping; footers "Pagina N van 8" on all pages; P3 matching block, P7 toolbox/readers' corner, P8 answers block all as expected (see PROOF-NOTE.md observations) |

## Answer-key verification (manual, 150/150 vs stems)
- All 150 keys checked stem-by-stem. Only defect: **#39/#40 swapped** (see PROOF-NOTE defect 1). Confirmed in text.md appendix, nl `registry.json`, core `registry.json`, core text.md def order, rendered P3 SVG (defs a y=1079, b y=1150, c y=1221, d y=1292), and the P8 render ("39. d · 40. a").
- Matching sets verified: P2 D (24 b, 25 c, 26 a, 27 d), P4 C (56 b, 57 c, 58 d, 59 a), P5 C (74 d, 75 a, 76 b, 77 c), P8 F (141 b, 142 c, 143 d, 144 a).
- P6 chart arithmetic 254+162+19=435 ✓. P7 golden sentences 8/8 verbatim ✓. MODEL text 82 words (80–100) ✓.
- Per-page counts 10/17/18/18/18/18/12/39 = 150; A2 62 / B1 66 / B2 22; numbering continuous 1–150.

## External-fact verification (web search, 2026-11-11)
Verified: midterms outcome + flips; MS no-runoff rule + uncalled race; Johnson not running for leader + Nov 18–19 Dem leadership votes; I'm a Celebrity launch + "How to Survive the Jungle" special (Sun Nov 15, 6pm, ITV1/ITVX); Anti-Bullying Week dates/theme/10th anniversary + ABA reach figures (8m children, >80% schools, NCB Feb 2026); Hunger Games film/album/dates/cast; ATP Finals dates/players/Sinner injury; Premier League fixtures (exact); NFL Week 11 (exact); World Children's Day (Nov 20, UNICEF theme, CRC 1989); certification window Nov 10–Dec 18 (Ballotpedia; Arkansas Dec 18 latest fixed date).
Not a confirmed defect: House triple 254/162/19 is a live-count snapshot (AP Nov 8 per core KIT D1's 4 sources; nearby trackers 252/161/22, 254/163, 252/162/21).
