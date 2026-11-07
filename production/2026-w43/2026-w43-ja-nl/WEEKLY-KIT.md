# Lucerna 日本語版 · Japanese Weekly — VOL.1 · JA×NL Production Kit

Week: **Monday 19 – Sunday 25 October 2026** · Edition: **Japanese text + explanations in Dutch** — languages pair one-to-one: Japanese articles, small gray Dutch glosses/notes/answer explanations only. **Independent proofread: PASS (2026-10-21, see §10).**

Build directory: `hidden_files/weekly-report-ja-nl-build/` (copied from the PATCHED core build `hidden_files/weekly-report-ja-build/`; content12.py, content34.py, content56.py, content7.py, content8.py, bslib4.py, svglib.py, render.py, run.py, assets/ inherited from the core; transform record in `scratch/transform_nl.py`).
Deliverables here: `svg/` (8), `cards/` (8 PNG @1950×2700), `Lucerna-VOL1-NL.pdf` (print, 8 pp), `Lucerna-VOL1-NL-web.pdf` (web, 8 pp, **3.18 MB**, under the measured ~10 MB server limit).

## 1. Baseline & patch provenance

- The core build's `svglib.py` carries the 2026-10-21 P7 seam patch (`SEAM_SLACK = 28`); md5 verified before copying and again at the end: **d73e23b365676c3618d7e060b835eb4d** in both the core build and this build (byte-identical file).
- `tools/freeze.py baseline` on this build copy, before any edit: **8/8 SVGs byte-identical** to the shipped (patched) core SVGs; core integrity re-hashed after the run — unchanged. Baseline core hashes: p1 db328eb8… · p2 ef09afeb… · p3 07e44381… · p4 01ade8a4… · p5 403dd3db… · p6 8a92c611… · p7 c7f0e380… · p8 355de22c… — re-verified identical at the end of this build.
- Transform: literal, count-asserted replacements (`scratch/transform_nl.py`, 482 replacements + 2 hand fixes recorded in §7), applied to the copied build only. Answer-generation code in content8.py is byte-identical to the core's apart from the registered strings in §4; the JA core's own key style is kept: `{n}. {key} — {note}`, writing item in the ✓ form.

## 2. Dutch furniture — strings as shipped (verbatim)

- **Pairing badge (P1, 19px sans bold, brick)**: `TEKSTEN IN HET JAPANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS` — one line, fits (occlusion audit: no EDGE flag). Masthead reflow identical to the other JA fan-outs: wordmark y 262→248, subtitle 330→316, badge at y=356, tagline 372→390, rules 392/401→406/413.
- **Footer line (every page)**: `Lucerna · JAPANS WEEKBLAD VOL.1 · TEKSTEN IN HET JAPANS · UITLEG IN HET NEDERLANDS`
- **Footer page line**: `Pagina N van 8`
- **Gloss prefix**: `Uitleg — ` (the library gloss adds it; gloss strings do not carry it in-string). 10 gloss boxes (P1 ×1 · P2 ×2 · P3 ×2 · P4 ×2 · P5 ×2 · P6 ×1).
- **P8 separators**: `— Pagina N —` (N = 1..8, one per source page).
- **Masthead**: `Lucerna` (no article) on all 8 pages.
- Bilingual heads follow the family pattern (Japanese head · Dutch gloss): `トップニュース · Hoofdnieuws`, `数字で見る今週 · In cijfers`, `今すぐ練習 · Meteen oefenen`, `この号の内容 · In dit nummer`, `今週のことば · Woord van de week`, `短いニュース · Kort nieuws`, `クイズ · Bliksemquiz`, `季節のことば · Seizoenswoorden`, `日本シリーズの日程 · Schema`, `箱根駅伝・予選会の10校 · De tien scholen van de voorronde`, `グラフを読もう · Lees de grafiek`, `まちがい診療所 · Foutenkliniek`, `今週のフレーム · De zin van de week`, `読者の手紙 · Lezershoek`, `テストと答え · Toets en antwoorden`, exercise headers `練習 · Oefeningen van pagina N` with the right line `Antwoorden op pagina 8 · Niveaus gemengd: zoek je nummer op`.
- Two deliberate deviations from a literal carry-over, both documented: (a) the P7 band title's language word is translated — `ことば · Taal` — as in JA×DE/EN/ES/FR/IT (JA×PT kept the core's Chinese word; not followed); (b) the P4 band title `スポーツ · 体育` is kept as-is — 体育 is a Japanese word, as in all other JA fan-outs.
- Dutch number style in notes (keys keep the core's byte formats): thousands with a dot (2.000 yen, 1.342 punten), decimal comma (1,5 keer), times as 18.30 / 12.00 uur.

## 3. Totals (registry dump, this build vs a scratch dump of the core build)

- **Exercises: 150 = core.** By level **A2 48 · B1 75 · B2 27**; by page **10/18/18/18/18/18/12/38**; page/level metadata diffs vs the core registry: **none**.
- Type counts identical to the core (fill 51 · MC 50 · cloze MC 13 · matching 12 · true/false 11 · sentence building 8 · translation 4 · writing 1), registered under Dutch type names (zinnen aanvullen / meerkeuze / gatentekst / combineren / waar of onwaar / zinnen bouwen / vertalen / schrijven).
- P8 writing model 『私の秋の週末』 unchanged, 150 characters (frozen Japanese).
- P6 practice chart bars frozen (34/28/22/16 = 100), re-measured in the render.

## 4. Key-diff registry (the ONLY registry differences vs the core)

Verified by dumping the exercise registry from scratch copies of BOTH builds and diffing programmatically: page/level meta diffs **none**; key diffs **exactly {137, 138, 150}**; stems re-aimed **exactly {139, 140}**; **all 150 notes differ** — every one rewritten in Dutch, none left in Chinese, none left as a bare Japanese gloss.

| # | Change | Core | This edition |
|---|---|---|---|
| 137 | key → Dutch; note → NL; instr | key 游行队伍12点从京都御苑出发。/ note 对照第3版 / instr 翻译 | key **"De optocht vertrekt om 12 uur uit de Kyoto Gyoen."** / note "Zie pagina 3" / instr **"Vertaal naar het Nederlands"** (stem unchanged Japanese) |
| 138 | key → Dutch; note → NL; instr | key 乱扔垃圾，要罚2,000日元。/ note 对照第5版 | key **"Wie afval op straat gooit, krijgt een boete van 2.000 yen."** / note "Zie pagina 5" / instr **"Vertaal naar het Nederlands"** (stem unchanged Japanese) |
| 139 | stem re-aimed (was Chinese, now Dutch); note → NL; instr; **key unchanged** (Japanese 読書週間は来週の火よう日から始まります。) | stem 读书周从下周二开始。→ ___ / note 对照第7版 | stem **"De Leesweek begint volgende week dinsdag. → ___"** / note "Zie pagina 7" / instr **"Vertaal naar het Japans"** |
| 140 | stem re-aimed; note → NL; instr; **key unchanged** (Japanese 私は池袋のハロウィンのイベントに行きたいです。) | stem 我想去池袋的万圣节活动。→ ___ / note 对照第5版（池袋的活动） | stem **"Ik wil naar het Halloween-evenement in Ikebukuro. → ___"** / note "Zie pagina 5 (het evenement in Ikebukuro)" / instr **"Vertaal naar het Japans"** |
| 150 | key (apparatus) → NL; note → NL; writing expl → NL | key （开放题，范文如下）/ note 范文见本版 H 区（150 字） | key **"(open opdracht — voorbeeldtekst hieronder)"** / note **"Voorbeeldtekst in deel H van deze pagina (150 tekens)"** / expl "Schrijfopdracht (geen enig juist antwoord); de voorbeeldtekst (150 tekens) staat hieronder." |

All other **145 keys are byte-identical to the core** — verified twice: on the registry dump above, and on the RENDERED P8 (spot lines 7, 25, 140, 141 extracted from both SVGs: printed keys identical, only the notes differ). Keys keep the core's byte formats (e.g. "2,000", "1.5", "1,342" inside Japanese keys); Dutch notes use NL number style (2.000 yen, 1.342 punten, "1,5 keer").

**p8.py keydiff adjudication (for the proofreader):** `tools/p8.py compare` reports status **CLEAN** (sets EQUAL, §5) but lists extra keydiff numbers [7, 25–29, 43–46, 65, 78, 83, 95, 109, 113, 115, 120, 136, 140–144, 146, 147] beyond {137, 138}. These are extractor artefacts of note translation (same class as ES×NL's 12): the registry dump — the authoritative source — shows the keys themselves are unchanged, and the printed lines confirm it. Do not re-flag; the gate is the note SET, which is CLEAN.

## 5. Gates (all run on the final artifacts with the canonical tools)

- **Freeze diff** (`tools/freeze.py diff --strict-cjk`): **added CJK = 0 on all 8 pages.** Every removed core string is classified: Chinese explanation layer, bilingual furniture heads, gloss wrap fragments, or P8 answer lines whose key segment is byte-identical in the corresponding added line (only the note changed). No Japanese article text removed; no undocumented Japanese-text change.
- **Printed-note set** (`tools/p8.py compare`): **CLEAN — core prints {1..150}, this edition prints {1..150}, EQUAL**, each entry carrying a Dutch note (150 in the ✓ model form).
- **Geometric occlusion audit** (`tools/occlusion_audit.py`, selftest passed first): edition **0 flags**; core 0 flags; **NEW vs core = 0**. (After the §7 fixes; the pre-fix run's 4 flags are recorded there.)
- **P7 seam pixel re-check** (the two seams patched in the core on 2026-10-21): gutter bands measured on the final rendered cards, this edition vs the patched core — seam (a) B1|B2 at y≈337: longest clear run **31px** in both; seam (b) A2|B1 at y≈370: **26px** in both (the correction record's 31/25 within band-choice tolerance). The patched clearance is preserved exactly; no overprint anywhere on P7 (audit TEXTX = 0).
- **P7 phrases**: the 8 phrases + page tags — Japanese quotes byte-identical to the core, tags localized to `(Pagina N)`; occurrence counts: each phrase exactly **2×** in the whitespace-stripped full text of both the core and this edition.
- **Calendar**: every weekday/date claim re-checked against the real 2026 calendar (Oct 17 Sat · 20 Tue · 22 Thu · 23 Fri · 24 Sat · 25 Sun · 27 Tue · 31 Sat · Nov 9 Mon) — the frozen Japanese text and the Dutch notes agree (G1 = Sat Oct 24, 18:30, DeNA vs SoftBank; ticket sale Thu Oct 22, 12:00; Reading Week Tue Oct 27 – Mon Nov 9; Halloween Sat Oct 31).
- **Images**: embedded image payloads **byte-identical to the core on every page** (1/2/1/1/1/1/0/0); every printed credit line matches the core and the core KIT (Syced CC0 · Poliphilo CC0 · Fumikas Sagisavas CC0 · Hiroshige III PD · Bain News Service PD · Petr Kratochvil PD · EJ Hersom / US DoD PD, with the P6 caption's not-this-event disclaimer intact).
- **Banned intermediary-layer term**: **0** occurrences in the paper, this KIT, and the operative build code (methods renamed `.bridge(` → `.expl(`, 22 call sites + the definition). The one-off transform script under `scratch/` quotes the core's original call strings as search patterns for the renaming — scratch-only, as permitted.
- Build log: zero `!!` warnings (no HEAD TOO WIDE, no FLOW OVERFLOW); all flows end inside their bottoms (P8 keys end y=2457 vs bottom 2540). Re-renders always ran through `run.py` in ONE process (shared-registry rule).

## 6. Builder's proofread (full pass; the independent loop follows)

All 8 pages read end-to-end on the final rendered cards; all 150 keys re-derived against the Japanese text via the registry dump (§3–§4); every gloss glosses a word that appears on its own page; Dutch read for naturalness throughout (glosses, the three あなたは？ prompts, the error-clinic explanations, the slogan breakdown, the readers'-corner note, all 150 P8 notes). VOL.2 promises printed on P7 are the core's frozen Japanese teaser (Reading Week, Halloween, Japan Series results, real readers' letters + best P8 writing) — unchanged, as in every JA fan-out.

## 7. Defects found & fixed during the build (all in the explanation layer / NL furniture)

1. **P2 freeze --strict-cjk +2 chars**: the first Dutch rendering of the 『見頃』の使い方 box title quoted 『見頃』 a second time in the Dutch half, adding one 『 and one 』 to the page's CJK multiset. JA×PT avoided this with «» quotes; the title was then shortened anyway under defect 2 (final: `『見頃』の使い方 · Zo werkt het`). Final freeze: added CJK = 0.
2. **P2 BOXTITLE flag**: that box title's true ink crossed the box border (right ink 974.5 > border 961.0; advance width 429.5 vs 416 available). Shortened to `Zo werkt het` (349.9) — fits with margin.
3. **P2 EDGE flag**: the matching-set instruction `Koppel de plaatsen aan de migoro-datums` ran off the page (ink to x=2032.75) — match_set draws the instruction at a fixed offset with no width check. Shortened to `Combineer`.
4. **P8 TEXTX flags ×2**: the F-section instruction `Koppel de woorden aan de betekenissen` spilled into the neighbouring column, overlapping exercise 150's number and the writing body. Shortened to `Combineer`. (P3's matching instruction, in a wider position, fits and is kept in full.)
5. **P8 note orphan**: note 135's closing » wrapped alone onto the next line. Note shortened (`De plaats van de handeling krijgt «で»` → `De plaats van de actie krijgt «で»`); the item now prints on one line. Only P8 changed in that re-render (other 7 SVGs byte-identical).
6. **Missed gloss caught by the residual-Chinese scan**: the P2 『餅』 gloss (口コミ…) survived the first transform pass; translated (`online reviews · toenemen · bekendmaken`) before the first render. A tightened simplified-only character scan of all operative code then came back empty.
7. **Transform-script artefact (record hygiene)**: the sed patch that prepared the E-section blocks also rewrote the type token on the NEW side of items 139/140, which would have registered their type in Chinese; caught by the same scan and corrected to `vertalen` in the build code and in `scratch/transform_nl.py`, so the recorded transform reproduces the shipped code.

After fixes 1–5 the full gate suite was re-run on the final artifacts: freeze added CJK = 0, p8 CLEAN, occlusion 0 flags / NEW 0.

## 8. PDF pins (measured from the final files on disk)

- Print `Lucerna-VOL1-NL.pdf`: **42,002,941 B**, sha256 `180bbbc8092916659d3e4ded2f13a117b16928bf177959635733cf75e3dcec3b`
- Web `Lucerna-VOL1-NL-web.pdf`: **3,183,532 B** (< 10 MB), sha256 `7a9814bd79da0fec769797047c7abc3b1d9002f5e4b9cb04f019a1b0dbd8726e`

## 9. Reproduction

```bash
cd hidden_files/weekly-report-ja-nl-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py     # content12+34+56+7+8 in ONE process
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py  # svg -> cards PNG -> print + web PDF
```

Fonts: Noto Serif/Sans CJK (JP face) + UnifrakturMaguntia (masthead). Never use /opt/meta-chromium (hangs in this VM).

## 10. Independent proofread record

**Verdict: PASS — one complete independent pass, zero problems found; no fixes, no re-render.** (Proofreader scratch: `hidden_files/proof-ja-nl/scratch/`.)

- **Patch provenance**: core build `svglib.py` md5 = `d73e23b365676c3618d7e060b835eb4d` verified before and after the pass (identical in core build and this build); shipped core SVG hashes re-verified unchanged at the end.
- **freeze.py baseline** (independent run on a pristine copy of the patched core build): **8/8 byte-identical**; core integrity re-hashed after — unchanged.
- **freeze.py diff --strict-cjk** (independent run): **added CJK = 0 on all 8 pages**. Every removed string classified page by page: Chinese explanation layer, Chinese halves of bilingual furniture heads, type labels, footer lines, and P8 answer lines whose key segment is byte-identical in the corresponding added line. No undocumented Japanese-text change.
- **Registry diff** (fresh dumps from scratch copies of BOTH builds, run in one process each): 150 = 150; page/level metadata diffs **none**; key diffs **exactly {137, 138, 150}** with the exact strings registered in §4; stems {139, 140} re-aimed to Dutch with Japanese keys byte-identical; **all 150 notes rewritten in Dutch** (none unchanged, no Chinese or bare-Japanese notes left). Totals: **150 = A2 48 · B1 75 · B2 27**, pages 10/18/18/18/18/18/12/38, type counts identical to core. Bonus check: the scratch re-runs of both builds reproduce the shipped SVGs of BOTH editions byte-for-byte (one-process render reproducibility).
- **Keys re-derived**: all 150 NL notes read end-to-end for Dutch correctness and key/note consistency (arithmetic spot-verified: .650 = 91/140, 671×2 = 1,342, 34+28 = 62, 22−16 = 6, 1 min 46 s = 106 s); #137/#138 Dutch keys are faithful renderings of the Japanese stems; #150 writing model counted character-by-character: **exactly 150 characters**, byte-identical to the core's model.
- **p8.py compare** (independent run): **CLEAN — core 150 noted = edition 150 noted, sets EQUAL**; keydiff list reproduced exactly as §4 registers. Artefact adjudication: 10 numbers sampled from the artefact list (7, 25, 43, 65, 95, 120, 136, 140, 141, 146) against the printed P8 lines of both editions — in every case the key segment is byte-identical and the difference sits entirely in the note segment. Not defects.
- **Occlusion audit** (canonical tool, selftest passed first, independent run): edition **0 flags**, core 0 flags, **NEW vs core = 0** — covers the builder's four fixed flags (P2 box title «Zo werkt het», P2 + P8 «Combineer» instructions) and the P8 note-135 orphan («135. 図書館で本を借ります。 — De plaats van de actie krijgt «で»» prints on one line).
- **P7 seam special check**: pixel-measured on the rendered cards with one identical method for both editions — seam (a) y≈337 minimum clear run **29 px in both** (last ink x=963, first ink x=993 at row 334), seam (b) y≈370 **24 px in both** (503 → 528, row 356). The edition's clearance is exactly the patched core's, at identical rows and ink coordinates; TEXTX = 0. (The builder's 31/26 figures come from a widest-run band choice; the governing criterion — clearance not smaller than the core's — is met exactly.)
- **Geometry deltas vs core** (full rect census): confined to explanation-layer flow — gloss boxes (#f1ead6) one line taller (+29.7) where Dutch wraps longer, downstream chips/boxes shifted by the same flow, P7 VOL.2 teaser box ends y=2548.6 < 2580. The P6 practice-chart bars sit inside the identical rect set (frozen). No manual geometry change; audit-clean.
- **Furniture**: P1 badge verbatim as §2; footers + «Pagina N van 8» correct on all 8 pages; «Uitleg — » prefixes total **10** (= the registered gloss boxes); P8 separators «— Pagina 1..8 —» all present; P8 key style `{n}. {key} — {note}` kept; deviations confirmed non-defects: P7 «ことば · Taal», P4 «スポーツ · 体育» (Japanese word).
- **P7 phrases**: the 8 quotes byte-identical Japanese; each occurs **exactly 2×** (article + deck) in both editions; tags all «(Pagina N)», pattern (1,1,2,2,3,4,5,6); no Chinese page tags remain.
- **Calendar** (verified with `date`, Asia/Tokyo): Oct 17 Sat · 20 Tue · 22 Thu (ticket sale 12:00; Jidai Matsuri) · 23 Fri · 24 Sat (Japan Series G1, 18:30, DeNA vs SoftBank) · 25 Sun · 27 Tue (Reading Week opens) · 31 Sat (Halloween) · Nov 9 Mon (Reading Week ends) — all agree with the frozen Japanese text and the Dutch notes.
- **Images & credits**: embedded image payloads byte-identical to the core on every page (1/2/1/1/1/1/0/0); credit lines equal to the core's on every page and matching the placed images.
- **Residual-language scan**: no Chinese explanation remnants (all Chinese strings of the core are removed and replaced by Dutch, per the freeze classification); simplified-only characters appear solely inside frozen Japanese text (写真・国立・結果・点数 etc.). Banned intermediary-layer term: **0** in the paper, this KIT, and the operative code; `.expl(` = 22 call sites + definition; the scratch transform script's 3 search-pattern mentions are the disclosed scratch-only exception.
- **PDF pins (measured from disk by the proofreader)**: print `Lucerna-VOL1-NL.pdf` **42,002,941 B**, sha256 `180bbbc8092916659d3e4ded2f13a117b16928bf177959635733cf75e3dcec3b`; web `Lucerna-VOL1-NL-web.pdf` **3,183,532 B** (< 10 MB), sha256 `7a9814bd79da0fec769797047c7abc3b1d9002f5e4b9cb04f019a1b0dbd8726e` — identical to §8.

Housekeeping note (not an edition defect): a stray `home/` tree at the goal root — leftover scratch output of an earlier proof, produced by the same OUT-path mangling this proofreader initially reproduced — was removed during this pass after its contents were verified to be scratch only; both editions' shipped trees were re-hashed intact afterwards.
