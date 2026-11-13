# WEEKLY-KIT — The Lucerna VOL.1 · EN × NL edition

**Edition:** English target text (frozen VOL.1 core) · all explanations in Dutch,
for Dutch-speaking readers. Week of October 19–25, 2026. 8 pages, 1950×2700.
Build dir: `hidden_files/weekly-report-en-nl-build/` (copy of the frozen core build;
the core itself was never edited).

## 1. Baseline proof (before any edit)

The unmodified copy of the core build was run with output paths pointed at the copy
and reproduced all 8 shipped core SVGs **byte-identically (sha256, 8/8)**:

| page | core shipped sha256 |
|---|---|
| p1-front.svg | ad9904e3c910ba7e25792c74425b2b1b25dfdaab9353a4f70c1f5622cdba8467 |
| p2-life.svg | 684025c5a32287ab9c6f5628d1148a1037e1131a6c5974984c723d7b4e757720 |
| p3-culture.svg | f912664a8f65c038322788781afd6033d9c1b293185aee88b5ae5a49c10de67d |
| p4-sport.svg | 6059e3fbc1484e8f0daed69a8de61c37ed7ac5becdb015b7fffe908393a59d54 |
| p5-jeunesse.svg | 1f1b61ceae2176754ce50c16f4cd5ea4344cd89d290060ed110c4fa02efe622e |
| p6-politique.svg | 221066e3ffbd31ebc719099d7f1e2ded327f7cecc3a3f2f42a8018c6f5cea075 |
| p7-langue.svg | 74cae1c2e87a0a8f928aef0444359fd4c3d4f1d6a5638f41b517eb7ee1019d8a |
| p8-exercices.svg | 35c00e4961b91acbf739bc7faa0b148465bedab31c45bb27f6433d3242301763 |

After all work, the core's shipped SVGs were re-hashed in full: **8/8 identical to
the table above — the frozen core is untouched.**

## 2. Totals (identical to core)

149 exercises — A2 58 · B1 72 · B2 19. Per page: P1 10 · P2 17 · P3 18 · P4 18 ·
P5 18 · P6 18 · P7 12 · P8 38. Registry diff vs core: page and level metadata —
**zero differences**; type names translated (see §4); keys differ only per §3.

## 3. Key-diff registry (complete)

Answer **keys** differ from the core at exactly **3** items:

| # | core key | NL key | why |
|---|---|---|---|
| 136 | Chinese rendering of the key sentence | « Stemmen is geen dag meer; het is een seizoen. » | translation item EN→reader language |
| 139 | Chinese rendering | « Geen van beide clubs heeft ooit de World Series gewonnen. » | translation item EN→reader language |
| 149 | Chinese writing-apparatus key | « (open vraag — het voorbeeld staat in het schrijfblok op deze pagina) » | writing item apparatus |

Item **stems** re-aimed (keys unchanged, still English):

| # | NL stem | key (unchanged) |
|---|---|---|
| 137 | « Vertaal: de 76ers wonnen met 106–100. » | The 76ers won the game 106–100. |
| 138 | « Vertaal: dit jaar begon het vervroegd stemmen op maandag. » | This year, early voting opened on Monday. |

All 149 P8 answer **notes** are rewritten in Dutch. Nine notes are language-neutral
and therefore identical to the core: #18, 77, 78, 84, 95, 100, 103, 119, 120
(worked forms and arithmetic, e.g. « 34 + 27 = 61 »).
The P6 KEY SENTENCE box carries the same Dutch sentence as key #136, verbatim.

## 4. NL furniture (verbatim, as shipped — the ×NL column standard)

- P1 badge (19.5pt sans bold, brick): « TEKSTEN IN HET ENGELS · UITLEG IN HET
  NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS »
- P1 sub-masthead (46pt): « ENGELS WEEKBLAD · VOL.1 · STADIONS · STEMMEN · POMPOENEN »
- Footer left: « The Lucerna · ENGELS WEEKBLAD VOL.1 · TEKSTEN IN HET ENGELS ·
  UITLEG IN HET NEDERLANDS » · Footer right: « Pagina N van 8 »
- Gloss prefix: « Uitleg — » · P8 keys page separators: « — Pagina N — »
- Masthead « The Lucerna » exactly as the core ships. Kicker suffixes are Dutch
  (e.g. « LIFE · Leven », « IN DEPTH · Verdieping »); exercise type names:
  Zinnen aanvullen · Meerkeuze · Zinnen omvormen · Lezen: waar/onwaar · Woorden
  combineren · Grafiek lezen · Gatentekst · Leestekst · Vertalen · Dialoog
  aanvullen · Fouten verbeteren · Meedoen · Schrijven. Short instructions:
  Vul in · Herschrijf · W/NW · Combineer · Verbeter.
- Some box titles carry shortened Dutch suffixes forced by measured width
  (wording shortened, geometry never): e.g. « THE WEEK IN NUMBERS · Cijfers »,
  « THE ERROR CLINIC · Fouten », « D · TRUE OR FALSE? · W/NW »,
  « READING THE CHART · Grafiek », « ELECTION WORDS · Verkiezing ».

**Deviation (recorded):** the prescribed footer/badge form « ENGELSE WEEKBLAD »
ships as « ENGELS WEEKBLAD ». Dutch grammar: *weekblad* is a neuter noun and,
without an article, the adjective takes the uninflected form (*Engels weekblad*,
like *Duits weekblad*); « Engelse weekblad » would be ungrammatical.

**Clock-band subtitle (P1):** the Dutch sub-line ships as « AMERIKA PAS OP
1 NOVEMBER » — the trailing page pointer was dropped after the geometric audit
showed the full string's ink collided with the frozen English sub-line on the
same baseline (see §7).

**Dutch target names** (for the other ×NL columns): ENGELS · DUITS · FRANS ·
SPAANS · ITALIAANS · PORTUGEES · RUSSISCH · JAPANS · KOREAANS · CHINEES
VEREENVOUDIGD · CHINEES TRADITIONEEL.

## 5. Printed-note set verification (by number, from the rendered P8)

Method: sequential-scan extraction of the printed keys text (15.5pt nodes) in the
shipped core P8 and in this edition's P8; an item counts as noted when its entry
carries a parenthesised note.

- Core printed set (62): 11, 14, 15, 19, 35, 36, 40, 42, 49, 65, 74, 82, 83, 84,
  85, 86, 87, 89, 101, 106, 108–149.
- This edition's printed set (62): **identical, item for item** — set equality
  holds (the edition's code carries an explicit PRINT_NOTES set derived from the
  core's own print rule run against the baseline reproduction).

Note format follows the core's P8 typography: space + half-width parentheses
« key (note) ».

## 6. Defects found by the builder and fixed (wording only, geometry frozen)

1. **P2 exercise header instructions** wrapped to 2 lines each and pushed the
   exercise flow past its end — shortened to one line each (« Vul de zinnen aan,
   volgens de klok. » / « Herschrijf met be going to + werkwoord. » / « Lees
   pagina 2 en kies het juiste antwoord. »); flow now ends at y=2565, exactly
   the core's end.
2. **P2 AND YOU box** grew past the time-band rule (Dutch paragraph 4 lines vs
   the core's 2) — paragraph shortened to « Hotdogs in je koelkast? Welk geld
   komt er elke maand binnen? Schrijf in het Engels! » (2 lines); box ends at
   y=1534.6, exactly the core's value.
3. **P3 col-3** debate paragraph ink reached the footer rule zone — FESTIVAL
   WORDS items and the paragraph shortened; col-3 flow ends y=2437 (core 2469).
4. **P6 article gloss** overflowed into the chart zone (covered-glyph class) —
   gloss trimmed to « midterm, de midterms · the House, het Huis · margin, het
   verschil · turnout, de opkomst. » (*incumbent* is fully glossed in the same
   page's ELECTION WORDS box); article flow ends y=1408, exactly the core's.
5. **P8 cloze battery** — the E2 stem at 2 lines cascaded the dialogue tail into
   the MODEL box zone; stem shortened to 1 line; battery ends y=1448 (limit
   1485).
6. **P1 clock band (found by the geometric audit):** the Dutch sub-line
   « AMERIKA PAS OP 1 NOVEMBER · ZIE PAGINA 7 » overlapped the frozen English
   sub-line's ink by 50px on the same baseline (actual glyph collision, verified
   on the rendered card) — shortened per §4; re-audit clean, gutter 106px.

## 7. Geometric occlusion audit (mandatory gate)

Method: paint-order SVG parse; PIL real-font glyph metrics, ink extent (not
advance width, bold included); line boxes expanded by half stroke width; checks
for ≥30% glyph coverage, footer-band intrusion (y>2580), page-edge spill,
line-through-ink crossings, text-vs-text overlaps, box-title ink vs its own box
borders, stacked-box bottoms. The script was validated first on a synthetic
positive control (one planted defect per class — 6/6 flagged, clean text silent).

- Core (reference): 6 flags, all known/adjudicated in the core's own production.
- This edition, first pass: 8 flags = the core's 6 classes + the P1 band
  collision (§6.6, real defect, fixed) + one P6 band-model graze.
- This edition, final: **7 flags, zero unresolved new defects** — 6 are the
  core's own flags at identical geometry (wordmark band overlap, snapshot line
  under its box by design, P2 box-bottom 1px band overshoot ×2, P6 practice-data
  note line, and the word-of-week adjacency — pixel-verified on the card: the
  only ink rows in y 1818–1862 are the rule itself at 1843–1844, text ink ends
  above it, zero overlap). The 7th (P6 chart note vs « READING · Lezen » header)
  is a band-model graze only: pixel scan shows header ink rows 1476–1493 and
  note ink rows 1499–1518 — 5 clear rows, no ink contact. Adjudicated non-defect.
- Known flow overshoots identical in class to the core's own: P2-ex ends +3
  (same value as core), P3-main +3 (ink verified clear of the 2580 footer rule;
  no FOOTER flag).

## 8. Image credits (from the core build's assets/CREDITS.md; Commons API Artist field)

1. P1 — ws1912.jpg: « 1st Game - 1912 World Series (baseball) LCCN2014691959.jpg »,
   Bain News Service / Library of Congress — public domain.
2. P2 — sscard.jpg: « PD social security card.png », US Social Security
   Administration — public domain.
3. P3 — halloween1912.jpg: « A Halloween Wish 1912.jpg » — public domain.
4. P6 — capitol.jpg: « Capitol Building Full View.jpg » — public domain.

## 9. Deliverables

`files/weekly-report-en-nl/`: svg/ ×8, cards/ ×8 (1950×2700 PNG),
Lucerna-VOL1-NL.pdf (print), Lucerna-VOL1-NL-web.pdf, this KIT.

| file | bytes | sha256 |
|---|---|---|
| Lucerna-VOL1-NL.pdf | 8,617,312 | 51cd2483d483c77f1d07da9326c7f87519c39a51a169c481e8f35673b44db8ed |
| Lucerna-VOL1-NL-web.pdf | 4,539,679 (< 10 MB ✓) | 52b71880309f960e1444935013494e2ab96b37a6fc6717eeb1ff93de9c3d57ef |

**D5 rebuild (2026-11-13, see §11 below).** Print `The-Lucerna-VOL1-en-nl.pdf` **7,494,138 bytes**, sha256 `3875d10bc3aa7a5267c4e5599358254bd20475011441385a7dc78d8fec4b85ae`; web `2026-w43-en-nl.web.pdf` **1,063,554 bytes**, sha256 `5107ac33829e6f78cac8642da9e70a450dcf506ebbe2963a72f3cf35d4e87e5d` (< 7 MB); text.md byte-identical to the shipped version (sha256 `72de5219…`). Pre-D5 values: print 8,617,312 B, web 1,105,489 B (`4e244251…`, shipped in issues/).

(The two rows above are the FINAL pins, measured by the independent
proofreader on the post-fix artifacts — §10; they supersede the builder's
pre-fix pins 8,617,532 / a74d571b… and 4,360,461 / 2a985a10….)

Print PDF verified: 8 pages, same mediabox as the core's, full text layer on
every page, and its 4 embedded images are byte-identical to the core's (the
core's own shipped print PDF is larger only because of uncompressed merge
streams; the fan-out merge matches the EN×PT sibling's 8,622,488 B).

Final SVG sha256: p1 1f8d0fa529337b4e… · p2 2b90d55d95a51c84… · p3 13b025abbbdc45c3… ·
p4 35054274fd8ea665… · p5 40b5555230e037fb… · p6 1ce4885ceeeab9fa… (§10 fix; pre-fix 8f13ff74e4ffa98b…) · p7 ddbdfbfe5e173806… ·
p8 df847a5799086ae6… (full values in build scratch).

Freeze check: every difference from the core is explanation layer, pairing
furniture, or a §3 registry item. Zero CJK characters in the final SVGs; the
intermediary-layer term (either form) occurs 0 times in the paper, this KIT,
and the operative build code. (One-off transform scripts under
`hidden_files/weekly-report-en-nl-build/scratch/` quote the core's original call
strings as search patterns for the expl() rename — scratch only, as permitted.)

## 10. Proofread status

Builder's full proofread: **complete** — all 8 pages read end-to-end from the
rendered text; all 149 keys re-derived from the English text (agreement with the
core registry except §3); P7 phrases verbatim-contiguous with the core's page
tags and per-phrase occurrence counts; every weekday/date claim checked against
the real 2026 calendar (NBA opening Tue Oct 20 · World Series from Fri Oct 23 ·
F1 Austin Sun Oct 25 · Halloween Sat Oct 31 · clocks Sun Nov 1 · Election Day
Tue Nov 3).

Independent proofread: **PASS** (2026-10-22, fresh agent, full pass on the
rendered artifacts; mechanical gates run with the shared tools in `tools/`
per SOP 附则二； scratch in `hidden_files/proof-en-nl/scratch/`, re-pass files
prefixed `rp-`).

**One real defect found and fixed (explanation layer only).** P6 PRACTICE
DATA caption: the Dutch tail («…vereenvoudigd en verzonnen voor deze
oefening; geen echte enquête.», advance end x=1469.8) ran under the READING
section-head gold rule (x 988–1424, y 1506–1508) — the rule struck through
the Dutch glyph bodies (zoomed-crop proof in scratch) and the tail abutted
item 95's text; materially worse than the core's graze of the Chinese
glyphs' feet. Same struck-caption class the EN×PT proofreader caught and
fixed by shortening. Fix (content56.py, Dutch wording only, no geometry):
tail → «Oefengegevens, verzonnen.» — the full caption now keeps the frozen
English segment + short Dutch tail, matching every shipped EN sibling.
Re-rendered via the single-process driver (the content modules share the
bslib4 registry — running them as separate processes restarts numbering;
the first re-render attempt did exactly that and was caught by the
node-level diff and fully restored from the pre-fix snapshot before the
correct driver run). Post-fix verification: 7 of 8 SVGs byte-identical to
the pre-fix edition; P6 differs in exactly one text node (the caption).
Pixel check on the final P6 card: caption ink rightmost x=956, 32 px clear
of the rule start (988); no strike, no abutment. The ENTIRE pass below was
then re-run from the top on the final artifacts.

**Freeze (tools/freeze.py).** Baseline: the unmodified core build
reproduces all 8 shipped core SVGs byte-identically (8/8, run twice);
core integrity re-hashed after every run. Diff vs the frozen core: CJK in
the edition = 0 on all 8 pages, added CJK = 0; every removed core string
classified — Chinese explanation layer, pairing furniture (masthead
tagline → Dutch badge), line-join fragments of English text verified
present in the edition, or P8 answer lines re-wrapped around Dutch notes
with all keys verified present. No undocumented English-text change.

**Totals / registry (fresh dumps from scratch copies of both builds).**
149 = 149; levels A2 58 · B1 72 · B2 19 both; per page 10/17/18/18/18/18/
12/38 both; page/level meta diffs NONE. Key diffs EXACTLY {136 → «Stemmen
is geen dag meer; het is een seizoen.», 139 → «Geen van beide clubs heeft
ooit de World Series gewonnen.», 149 → «(open vraag — het voorbeeld staat
in het schrijfblok op deze pagina)»}; stems 137/138 re-aimed in Dutch with
English keys byte-identical to the core (verified in the shipped P8).
Notes: 140 rewritten in Dutch; identical to core exactly {18, 77, 78, 84,
95, 100, 103, 119, 120} — each verified genuinely language-neutral (worked
English forms, arithmetic, time notation).

**Printed-note set (tools/p8.py compare, final artifacts).** CLEAN:
core set = edition set = {11, 14, 15, 19, 35, 36, 40, 42, 49, 65, 74,
82–87, 89, 101, 106, 108–149} (62 items, item-for-item); keydiff exactly
[136, 139, 149]. All 149 keys additionally re-derived by hand from the
English text during the full reads — agreement total.

**Occlusion audit (tools/occlusion_audit.py, selftest passed, final
artifacts).** Edition 2 flags, core 2 flags; the two pre-fix P6 flags are
gone. Remaining: (1) P1 LINEX word-of-week/rule adjacency — pixel-verified
NON-defect (Dutch gloss ink ends row 1842; rule rows 1843–1844 carry zero
dark ink in the text's x-range; pattern inherited from the core); (2) P2
BOXTITLE AND YOU box — pixel-verified NON-defect (rendered ink ends row
1534, descenders clear of the bottom border at 1534.6). The builder's six
wording fixes and the P1 clock-band collision fix («AMERIKA PAS OP 1
NOVEMBER» clear of the English sub-line) were each verified in SVG
coordinates and/or flow logs and at pixel level. Zero unresolved defects.

**Content checks.** Full 8-page reads: every explanation element in Dutch
(glosses «Uitleg — …», sidebars, instructions, grammar notes, answer notes,
writing instruction + model apparatus, readers'-corner reply, VOL.2
teaser). Calendar: all 12 weekday/date claims verified against the real
2026 calendar (Oct 14 Wed · Oct 17 Sat · Oct 19 Mon · Oct 20 Tue · Oct 22
Thu · Oct 23 Fri · Oct 24 Sat · Oct 25 Sun · Oct 30 Fri · Oct 31 Sat ·
Nov 1 Sun · Nov 3 Tue) — NBA opening Tue Oct 20, World Series Game 1 Fri
Oct 23, F1 Austin Sun Oct 25 confirmed. P7: all 12 phrases + page tags
identical to the core; whole-issue occurrence counts equal per phrase.
Images: embedded payloads byte-identical to the core per page; every
printed credit matches a placed image and the core KIT. Furniture as §4,
incl. «ENGELS WEEKBLAD» (uninflected adjective before neuter *weekblad*),
matching FR×NL's shipped «FRANS WEEKBLAD» on all 8 pages. Intermediary-
layer term (either form): 0 occurrences in the final SVGs, this KIT, and
the operative build code.

**Final pins (measured on the final artifacts; supersede §9's builder
pins).** Print Lucerna-VOL1-NL.pdf 8,617,312 B / sha256
51cd2483d483c77f1d07da9326c7f87519c39a51a169c481e8f35673b44db8ed · Web
Lucerna-VOL1-NL-web.pdf 4,539,679 B (< 10 MB) / sha256
52b71880309f960e1444935013494e2ab96b37a6fc6717eeb1ff93de9c3d57ef · Final
P6 SVG sha256 1ce4885ceeeab9fa14aa4f2c84bd8f36f8bf7f92ee2a48cf9894cfa4b4028466
(other 7 SVGs unchanged from §9). Core shipped SVG hashes re-verified
unchanged at the end of the pass (p1 ad9904e3… · p2 684025c5… · p3
f912664a… · p4 6059e3fb… · p5 1f1b61ce… · p6 221066e3… · p7 74cae1c2… ·
p8 35c00e49…, full values in §1).

**Verdict: PASS — one complete independent pass over the final artifacts
with zero problems.**

## 11. D5 rebuild (2026-11-13, D5-only)

SOP §1.1 font fix: the explanation layer's Latin letters move from Noto Sans CJK to Newsreader (SemiBold). No commit, no push — insertion is done by the closer after an independent re-proof. Work log: `hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-nl/`; per-edition report: `production/notes/2026-w43/g-en/scratch-d5-rebuild-en/D5-REPORT-2026-w43-en-nl.md`.

**Install**: core landed with `apply_variant.py --patch-core en --week 2026-w43` (core-en `svglib.py` +95/−3, `_D5_READER = "latin"`); this edition installed with `--svglib patched/…/svglib.py --target en --reader nl --week 2026-w43`, `_D5_READER = "latin"` (installed svglib md5 identical across de/it/nl/pt); routing unit test FAILURES: 0 (66 PASS); fix2 block kept.

**Baseline** (pre-fix production build): run TOTAL 149, 0 warnings; print PDF byte-identical to `MANIFEST-W43-D1.md`; print/web text layers differ by 0 chars; self-built web vs shipped web differ by 0 non-space chars (spaces only); pre-fix census D5 Latin 556, Cyrillic 0, curly in CJK 1; baseline P8 noted 62/149 (core口径).

**Defects and fixes** (run1: 8 items, all D5 widening except the pre-existing P2 spill, which the baseline shares; sizes only, no wording changed):

- heads ×3: P4 `C　COMPARATIVES　Vergelijking` 25→24 (420.6 px, only 1.9 px spare — the gate is a deterministic measurement, a pass is a pass); P5 `EARNINGS, IN PLAIN ENGLISH` 26→25; P8 `B　MULTIPLE CHOICE　Meerkeuze` 24→**22** (23pt still 0.2 px over).
- occlusion ×2: P1 band headline vs subtitle `DE KLOK TERUG` overlapped 89.9×20.8 px → headline 46→**42** (44 leaves only ~1 px advance gap); P6 PRACTICE DATA line crossed by the r6 first-column title rule (LINEX, same defect class as es — the Dutch tail sentence `Oefengegevens, verzonnen.` pushed the line end past the rule at x=989) → PRACTICE DATA 18.5→**18** (stays ≥ the 18 pt exporter threshold; text.md still byte-identical).
- creambox/boxtitle ×3: P3 `SAY IT ON THE NIGHT　Zeg het zo` +2.6 px → `tsize=22`; P5 `WORDS OF THE SCREEN　Scherm` +2.9 px → `tsize=22`; P6 `HOW TO FOLLOW IT　Zo volg je ze` +2.3 px → `tsize=22`.
- spill ×1: P2 `Check your number !` below the DID YOU KNOW box by 12.71 px → box-height formula tail +14→+34 (box bottom +20 px; same pre-existing defect as core-en).

P8: 197→193 lines, footer slack 32.7→51.6 px.

**Gates run2 (all 17 ALL-GREEN)**: run TOTAL 149, 0 warnings; head_check 0; d5 census 0/0/0; render RC=0; webpdf RC=0 (1,063,554 B < 7 MB); occlusion 0 flags; p8 extract noted 62/149; p8 compare **CLEAN** (keydiff=[136, 139, 149], the registered reader-language keys); freeze baseline 8/8; freeze diff added CJK chars 0; spill 0; boxtitle 0 DEFECT (57 titles); edge 0/0; creambox PASS 0 defects; text layer print=web diff 0; census_quotes 0 defective; no family gates.py for en.

**New deliverables**: print `The-Lucerna-VOL1-en-nl.pdf` 7,494,138 B (`3875d10b…`); web `2026-w43-en-nl.web.pdf` 1,063,554 B (`5107ac33…`); text.md byte-identical (`72de5219…`). Still 149 exercises.
