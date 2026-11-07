# FIX-1 LOG — De Lucerna VOL.2, Nederlands core, W45 (against `nl-core-independent-proof.md`)

Fix agent, 2026-10-26. Scope: ONLY the 3 problems in the independent proof report.
No new content, no new facts, no lead/image/credit/ABSTRACT changes. No git push,
no Discord, no messages sent. NOT self-certified: a fresh full independent proof
round is still required before finalization.

## Problem 1 — HARD, P4 European-week tally (fixed, all 3 spots)

Old (wrong): «Europa: vier keer feest, één keer verlies» / «Alleen NEC verloor» /
ex. 52 stem «vier keer feest». Paper's own results: 3 wins (Ajax 2–0 Atalanta,
Twente 4–1 Lincoln, AZ 4–0 Ararat) and 2 losses (NEC 2–4 Dinamo, Feyenoord 0–1 Betis).

Fixes in `hidden_files/weekly-report-w45-nl-build/content34.py`:
- Headline → «Europa: drie keer feest, twee keer verlies»
- Article ¶1 → «De Europese week is voorbij — en de balans is drie keer feest,
  twee keer verlies. … NEC verloor: 2–4 bij Dinamo Zagreb.» («Alleen» dropped;
  Feyenoord's loss is stated in the next paragraph, as before)
- Ex. 52 stem → «De ___ van de Europese week is: drie keer feest, twee keer verlies.»
- KIT §2 headline corrected to match.

Verification on the rendered P4 SVG (joined text) + P4 PNG viewed: all three spots
read the correct tally. P8 key 52 verified UNCHANGED and still matching:
«52. balans — balans = 成绩单、总结». No other key or note was affected by the
stem change (checked: no other exercise, key, or note references the tally).

## Problem 2 — PROMISE GAP, P7 readers' corner (fixed, on-page disclosure)

No letters or texts fabricated. Disclosure added INSIDE the P7 BRIEVEN VAN LEZERS
box itself, in `content7.py` (existing labeling and invitation kept verbatim):
- Dutch: «Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen —
  daarom dit voorbeeld; belofte naar VOL.3.»
- Chinese: «截稿时未收到真实来信或第 8 版最佳作文，刊登示例信，承诺顺延 VOL.3。»
- Kept verbatim: «Li (voorbeeldbrief van de redactie)» and
  «编辑部示例信，非真实来信。欢迎寄来你的真实来信和第 8 版最佳作文，VOL.3 刊登！»

Layout only, to make room (no quote or preview text changed): BRIEVEN box height
+250 in total; ZINNEN section fy 1712 → 1951; golden-sentence row pitch 158 → 90;
VOLGENDE WEEK box 2404 → 2439.

Defect caught during my own re-read of the changed page (first re-render):
the box-height formula undercounts rendered inter-paragraph spacing by ~20px
per added paragraph, so the last line of the existing note sat 21px BELOW the
box edge. Fixed with a measured +50 correction to the box height; second
re-render verified on the SVG (box bottom 1897, last baseline 1868, 28.5px
margin) and on the P7 PNG (all lines inside the box, no overlap with the
ZINNEN section, preview box, or footer).

## Problem 3 — MINOR, P8 key 99 (fixed)

Old key: «Rood komt weinig voor in Nederland.» — «in Nederland» appears in
neither the exercise prompt («rood / komt / weinig / voor») nor the P6 article
sentence («Rood komt weinig voor.»).
Fix in `content56.py` (the registry entry that generates the P8 key):
key → «Rood komt weinig voor.» Note unchanged («weinig voor = 很少出现»);
no note anywhere repeated the added words, so no other change was needed.
Verified on the rendered P8 SVG and P8 PNG: «99. Rood komt weinig voor. —
weinig voor = 很少出现».

## Re-render + gates (final render)

- Full re-render of all 8 pages: `run.py` (SVGs) + `render.py` (8 PNG cards +
  both PDFs). Final run log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings
  (grep count 0). Second, corrected P7 re-render included in the same counts.
- Exercises: 150 total, numbering continuous; `p8.py extract` on the final
  P8 SVG: noted set = 150 of 150. By page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38;
  levels A2 47 / B1 72 / B2 31; model essay 87 words (unchanged).
- Changed pages re-read: P4 PNG (headline, article, ex. 52), P7 PNG (whole page),
  P8 PNG (keys area) — all clean after the box-height correction above.
- Occlusion audit (`tools/occlusion_audit.py`, selftest first): selftest OK
  (all 6 planted classes fired, clean controls silent); final render:
  `../files/weekly-report-w45-nl-core/svg: 0 flags`.
- PDFs (final): `De-Lucerna-VOL2.pdf` 20,576,518 bytes, 8 pages;
  `De-Lucerna-VOL2-web.pdf` 3,487,176 bytes, 8 pages (under the 10 MB limit).
- Old strings absent from all 8 SVGs: «vier keer feest» 0, «Alleen NEC» 0,
  «Rood komt weinig voor in Nederland» 0. ABSTRACT.txt untouched.

## Files changed

- Build code: `hidden_files/weekly-report-w45-nl-build/content34.py`,
  `content56.py`, `content7.py`
- Edition: `files/weekly-report-w45-nl-core/` (8 SVGs, 8 cards, both PDFs
  re-rendered) + `WEEKLY-KIT.md` (§2 headline corrected; §11 fix record appended,
  earlier sections untouched)
- This log: `hidden_files/w45/nl-core-fix1.md`

## Open item for the parent

Nothing from the 3 problems is left unfixed. Next step is the parent-ordered
FRESH full independent proof round — this fix log does not certify finalization.
