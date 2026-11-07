# Lucerna 日本語版 · Japanese Weekly — VOL.2 · JA × ES edition (W45)

> Pairing badge (P1): «TEXTOS EN JAPONÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES»
>
> Week: Mon 2 – Sun 8 Nov 2026 (W45) · VOL.2 · 8 pages · **150 exercises**
>
> **BUILDER-COMPLETE — NOT finalized.** This KIT records the builder's own
> gates only. Finalization requires an independent proofread pass with a
> zero-problem verdict; no Discord post, no main-chat card/PDF dump, no
> repo insert was made by this build.

## 1. What this edition is

The fan-out of the finalized W45 Japanese core
(`files/weekly-report-w45-ja-core/`, Chinese explanations) for
Spanish-speaking readers. The Japanese target text is the frozen core;
only the explanation layer was rewritten natively in Spanish: every
definition, grammar note, instruction, furniture label, and all 150 P8
answer notes are in Spanish. There is no intermediary language anywhere
in the paper or the build code (the core's explanation-render method was
renamed `expl()` in this build's lineage; this build's transform works
by exact-literal replacement of the core sources, see §11).

P7 word-box rule (applied and checked): target-language definition
sentences stay Japanese verbatim; only the gloss/explanation line is
localized (e.g. the 『ゆるく整える』 frame box keeps its Japanese
breakdown sentence; only the `wcn` line became Spanish).

## 2. Baseline proof (fan-out step 1)

- Build dir: `hidden_files/weekly-report-w45-ja-es-build/` — transform
  output from the pristine core build dir
  (`hidden_files/weekly-report-w45-ja-build/`).
- Before any edit, `tools/freeze.py baseline` rebuilt the unmodified
  core and compared its 8 SVGs to the shipped core: **8/8 byte-identical
  (sha256)**, core files re-hashed untouched afterwards.

| page | sha256 (baseline = core) |
|---|---|
| p1-hyoushi | 4abe63d2a0e8076f3f681f66c259a361f02f1936cd9ced43b675b0bc5a13b17b |
| p2-kurashi | 08439072c0d680fa7da0ca4d35f9df8d595e2861e8d86a54e3805da5f9b |
| p3-bunka | 48a1fe9450c3e7988ee4154175f02a564cc893b1b4d02fc4b64421f4e796bc6b |
| p4-supotsu | 11b592b546e64fee738055bab3bf10ee9da99550be3f3ea024263ac78612c618 |
| p5-wakamono | 3035b928c6b7c71566d9917d9cd55aa319096ad23b28d9148751fc5502070d5c |
| p6-fukayomi | a8095c47341dd03d7f6e5768117994c48edd520078f467f9c6ee5bfe8ffe11f2 |
| p7-kotoba | 08060a286dd81b556726c740c02f449a87c82ed8cf08aa5bcaf76b056dd71d49 |
| p8-tesuto | 9e733a427864a61348e6e693050804540a33aa3aedcf78a5f1eacffbb4d53196 |

- Core registry re-derived in the same run: **150 exercises — A2 46 ·
  B1 75 · B2 29**; per page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
  Writing model character count: **167 characters**, identical to the
  printed claim on P8.
- Canonical svglib md5 verified before every transform run:
  `d73e23b365676c3618d7e060b835eb4d` (SEAM_SLACK=28); the canonical file
  was copied verbatim, never edited.

## 3. Totals (this edition = core)

- **150 exercises** — A2 46 · B1 75 · B2 29; per page
  10/18/18/18/18/18/12/38 (registry-compared item by item against the
  core: number, page, and level identical for all 150).
- Type counts (Spanish labels): Completar 50 · Opción múltiple 51 ·
  Texto con huecos 13 · Emparejar 12 · Formar una frase 8 ·
  Verdadero o falso 11 · Traducción 4 · Redacción 1.
- Instruction strings: Completa / Forma una frase / Verdadero/falso /
  Traduce / Redacción; matching: «Une palabra y definición» (P2, P8),
  «Une cada evento con su lugar y fecha» (P3).
- Masthead: **Lucerna with NO article** (Japanese is article-less per
  the SOP masthead rule; tables.json article null), exactly as the core.
- House style inherited from the core: です・ます throughout; weekday
  notation 土よう日・日よう日 (full forms); no ruby/furigana.

## 4. What changed vs the core (explanation layer only)

Freeze diff, final round (multiset of SVG text nodes, this edition vs
core; image payloads byte-identical on all 8 pages):

| page | nodes removed | nodes added | added CJK |
|---|---|---|---|
| P1 | 18 | 20 | 0 |
| P2 | 28 | 30 | 0 |
| P3 | 22 | 23 | 0 |
| P4 | 20 | 21 | 0 |
| P5 | 25 | 27 | 0 |
| P6 | 22 | 23 | 0 |
| P7 | 40 | 41 | 0 |
| P8 | 177 | 191 | 0 |
| **Total** | | | **0** |

Every changed node was reviewed: all are explanation-layer items
(gloss boxes with prefix «Nota — », bilingual section/box titles,
pairing badge, footers, band subtitles, quiz/phrase/answer apparatus)
plus the §5 registry items. The core's Japanese-language instruction
lines printed above exercise sections on P2–P6 belong to the target
layer and are unchanged. No foreign Han character entered the paper:
the Han charset of every added node is a subset of the core's 627-char
set (checked programmatically on the final diff), and a word-level
review of all added nodes found no Chinese word surviving (all added
Han tokens are frozen Japanese words such as 見頃, 紅葉狩り, 落葉,
読書週間, 紹介, ことば).

Furniture (W43 JA×ES precedent wins over the generic rule; three-way
measurement, record: `hidden_files/weekly-report-w45-ja-es-build/furniture-round3.log`):

| element | W43 JA×ES (shipped) | W45 core | This edition |
|---|---|---|---|
| wordmark y | 248 | 262 | **248** |
| edition line y | 316 | 330 | **316** |
| badge y / size / weight / fill | 356 / 19pt / 700 / #a4553a (BRICK) | — (no badge) | **356 / 19pt / 700 / #a4553a** |
| badge ink span | 467.1–1482.9 (1015.8 wide) | — | **467.1–1482.9 (1015.8 wide)** |
| tagline y | 390 | 372 | **390** |
| double rules y | 406 / 413 | 392 / 401 | **406 / 413** |
| dark band y | 424 | 424 | **424 (untouched core code)** |
| footer | Lucerna · SEMANARIO JAPONÉS VOL.1 · TEXTO EN JAPONÉS · EXPLICACIONES EN ESPAÑOL | Lucerna · 日语周报 VOL.2 · LUCERNA JAPANESE WEEKLY | **Lucerna · SEMANARIO JAPONÉS VOL.2 · TEXTO EN JAPONÉS · EXPLICACIONES EN ESPAÑOL** |
| page line | Página N de 8 | 第 N 版 / 共 8 版 | **Página N de 8** |
| gloss prefix | Nota — | 译注｜ | **Nota —** |
| P8 separator | — PÁGINA N — | — 第N面 — | **— PÁGINA N —** |

The pairing badge appears on the P1 masthead and the pairing footer
appears on all 8 pages («Página N de 8» likewise). The edition line
(«日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間») and the tagline
(«日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で») are
frozen core text, byte-identical, as is the wordmark ink (713.0–1237.0).

## 5. Key-diff registry (the only key changes vs the core)

All 150 answer **notes** are Spanish (apparatus). The **keys**
themselves are identical to the core except:

| # | type | core key | this edition's key | why |
|---|---|---|---|---|
| 137 | Traducción | 文化日是11月3日。 (reader-language sentence) | «El Día de la Cultura es el 3 de noviembre.» (note: Ver página 3) | The exercise asks the reader to translate the Japanese sentence **into their own language**; the model answer is therefore Spanish here. Same re-aiming as W43 JA×ES #137. |
| 138 | Traducción | 乱扔垃圾，要罚2,000日元。 (reader-language sentence) | «Tirar basura cuesta una multa de 2.000 yenes.» (note: Ver página 5) | Same re-aiming as #137; wording reuses the W43 JA×ES precedent verbatim. |
| 150 | Redacción | apparatus: reader-language open-question marker | apparatus: «(pregunta abierta — modelo a continuación)»; note: «El modelo está en la sección H de esta página (167 caracteres)» | Open writing exercise; only the apparatus line is language-dependent. Model text (167 characters) unchanged. |

Exercises **#139 / #140** (sentence cloze) keep Japanese keys
byte-identical to the core
（読書週間は10月27日から始まります。 /
神戸の紅葉のライトアップを見に行きたいです。); only their **prompt
sentences** are printed in Spanish on P8 («La Semana de la Lectura
empieza el 27 de octubre. → ＿» / «Quiero ir a Kobe a ver la
iluminación de las hojas de otoño. → ＿»), because the task is to
complete the Japanese sentence from a meaning given in the reader's
language. Same pattern as W43 JA×ES #139/#140.

Verification: printed P8 lines were parsed for core and edition and
split at " — "; key parts are identical for every item except #137,
#138 (above) and #150 (apparatus, no key). Answer-key format: the
core's house format `n. key — note` (em dash) is kept, matching all
shipped JA fan-outs.

## 6. Content checks

- **P7 phrases of the week**: each of the 8 quoted sentences occurs
  exactly twice in the issue text (once in its article, once in the P7
  section) — verified programmatically on the whitespace-stripped
  concatenation of all SVG text; Spanish translations carry page tags
  (Página 1–6) matching the source pages.
- **P7 word-box definitions**: the Japanese definition sentences in the
  A2/B1/B2 columns are byte-identical to the core (they never appear in
  the freeze diff as changed content); only their gloss lines were
  localized.
- **Readers' corner (no fabrication)**: the Japanese letter text is
  verbatim from the core (frozen); the core's Japanese disclosure line
  does NOT serve as the operative disclosure and the core's Chinese
  disclosure was replaced by ONE Spanish disclosure stating all three
  facts — editor's sample (not a real letter), no real letters had
  arrived by the deadline, no best P8 compositions had arrived, both
  carried to VOL.3 — plus an explicit invitation in the imperative
  («¡Envíanos tu carta en japonés!») with a VOL.3 publication promise
  («Las seleccionadas saldrán en el VOL.3.»). The VOL.3 preview box
  (frozen Japanese) repeats the same promise. No reader, letter, name,
  or quotation was invented; the pre-announcement line in the preview
  box is not counted as the invitation.
- **Weekdays/dates/numbers**: inherited from the core's verified
  record (core KIT): Nov 2 Mon, 3 Tue, 7 Sat, 8 Sun, 9 Mon; Oct 24 Sat,
  25 Sun, 27 Tue, 30 Fri, 31 Sat, Nov 1 Sun. Re-checked arithmetic:
  chart 38+27+21+14 = 100; chart-derived keys 21−14 = 7, 38+27 = 65;
  1.5倍 = 50% more than last year; 73% ≈ 3 in 4; G1 3–1, G2 4–3;
  attendances 33,388 / 33,432 as reported.
- **P6 practice chart**: 近場の満足 38% · 温泉 27% · 紅葉 21% ·
  グルメ 14% = 100%, labeled 練習用データ on the chart itself and in
  the «練習用データ · Datos de práctica» box title; bar widths in
  code = 30× the values (same formula as the core).
- **Topics** (from the core, unchanged): Nov 3 Culture Day + Nov 7–8
  autumn-leaf weekend (Naruko Gorge peak, Kobe Nunobiki Herb Garden
  light-up from Nov 7) + ゆる整え食 (Ajinomoto, Oct 21) + Reading Week
  in progress (to Nov 9) + 立冬 Nov 7; Japan Series G1/G2 verified,
  G3–G7 schedule-only with the gap stated on P4 and deferred to VOL.3;
  Oct 31 Halloween as a just-passed report; P4 schedule box, P6 chart,
  and P8 sections A–H all as in the core.
- **SOP-banned term scan**: 0 hits in the paper SVGs and in the build
  code (checked via unicode-escaped search so the scan itself does not
  introduce the term).
- **Simplified-residue word-level review**: beyond the char-level
  freeze gate (added CJK = 0), all added text nodes were read: no
  Chinese word survives anywhere, including shared-kanji words (the
  class of the nl-ja fix-3 lesson). One genuine residual found in
  round 1 (a P3 note left untranslated because the sibling table it
  was copied from missed it) was fixed in round 2 and verified gone
  (#37 now reads «La exposición dura hasta el 8 de noviembre»).

## 7. Geometric occlusion audit (builder-run)

Canonical tool `tools/occlusion_audit.py`, selftest first (all 6
planted classes fire exactly once; clean controls silent), builder-run
on the final SVGs: **0 flags** (exit 0). Round trail:

- Round 1: 18 flags — 16 TEXTX from the P8 keys-flow stack (see §9)
  + 2 BOXTITLE (P1 trend-box footnote line, P4 schedule-box title),
  both real Spanish-length overflows, both fixed in round 2.
- Round 2: P8 stack gone; the two BOXTITLE fixes verified; 0 flags
  except the flow was still 1 item over (see §9) — the audit itself
  read clean because the single clamped item's ink stayed above the
  footer band, but the FLOW OVERFLOW warning is a gate failure on its
  own and was fixed in round 3.
- Round 3 (final): **0 flags**, no FLOW OVERFLOW, no HEAD TOO WIDE.

Additional scans (builder-run, records in the build dir):

- Same-baseline furniture-band scan (P1 top band, PIL widths): left
  «VOL. 2 · 第2号» ends 219.9, center strapline 680.4–1269.7, right
  date ink starts 1530.0 — no collisions (same geometry family as the
  core).
- Right-edge advance scan (anchor-aware, true ink boxes): 0 hard
  violations (ink right > 1950). The only over-margin items are 7
  anchor=end furniture lines ending at 1885.1 (0.1 rounding on the
  RIGHT=1885 construction) — adjudicated non-defects.
- P6 chart-label scan (baseline-anchored true ink vs later-drawn bar
  rects): all 8 labels (4 categories + 4 values) at **0.0% coverage**
  — labels sit left of the bars, values right of the bar ends, no
  contact. The getbbox-whole-string shortcut was NOT used; coverage
  was computed from per-label true ink boxes.
- Kinsoku line-start scan (canonical NO_START set + small kana):
  **0 hits** on all 8 pages.
- Gloss count (rendered gloss() strings split on `·` itself, never on
  the spaced form): core 39 = edition 39 (P1–2: 13, P3–4: 15, P5–6: 11),
  item by item 1:1.
- 8 cards visually inspected (see §9): no overflow, overlap, footer
  intrusion, or image/credit defect. P7 teaser band ends at 2500.08
  (< 2540); P8 keys flow ends at 2533 (< 2540); lowest P8 key ink
  bottom ≈ 2534 (< 2580 footer rule).

## 8. Deliverables & pins

Directory: `files/weekly-report-w45-ja-es/`

- svg/ ×8, cards/ ×8 (1950×2700 PNG)
- **Lucerna-VOL2-ES-web.pdf — 3,108,359 bytes · sha256
  304d7e3b4107b627e1fb38e57324f98f28c644443d3bda6de89cb743d363c9cf**
  (< 10 MB, JPEG q≈85 pages; 8 pages)
- Lucerna-VOL2-ES.pdf (print) — 28,026,528 bytes · sha256
  ef7aedba043a03109afb4b5c70ebedb5d9c0922b069fd7ebbd956ce4d2259285
  (8 pages)
- WEEKLY-KIT.md (this file)
- ABSTRACT.txt (Spanish single line, no ASCII double quotes; real
  topic keywords + the learner search phrase «aprender japonés
  leyendo» + masthead, target language, A2–B2, 150 exercises)

Final SVG sha256 (round 3):

| page | sha256 |
|---|---|
| p1-hyoushi | 2da957acb8ced2d1e55c96a867c96252ced96c9e700426ee6df2fcded35b29d8 |
| p2-kurashi | 116a8632f50e226e07c894e31ceda1a91376ea662c001b61889e676747623259 |
| p3-bunka | 91b09247f099112cd2f24f10c4daa48d3d83a955a587f7f785ce7ad4d00e6b95 |
| p4-supotsu | 9762d6b410349e88725bc3eca7b42ffc7ff1b0826271955bf8aab8803c8eb8e4 |
| p5-wakamono | 97fc80da5fed83c0499179a5a9050a19bbc0cceacefd5e5cbf45335d13c10df5 |
| p6-fukayomi | 1cbeffbaff057e813b67782533830b3d0ef9352c0ba6453051278f67a09345a1 |
| p7-kotoba | 438b00ba032372a0920967fa205589adc14a5c8436d434cf534da006ec60314d |
| p8-tesuto | a47b07d7de24866e399e86765d3eadf023a9edd17f6bcff7ad9b8de81a285db7 |

Build code: `hidden_files/weekly-report-w45-ja-es-build/`
(transform.py + content files + svglib.py + run.py + render.py +
assets/ + per-round baselines + per-round gate outputs).

## 9. Build & fix-round record

All fix rounds edited `transform.py` only, then re-ran
transform → run.py (ONE process, registry order) → render.py. No fix
was applied to a content file alone; no build directory containing a
baseline was reset; the shared scratch directory was not cleaned.
Pre-fix baselines: `sha256-round1.txt` (round-1 SVG/cards/PDFs),
`sha256-round2.txt`, `sha256-round3.txt` (final).

- **Round 1** (baseline: freeze 8/8; totals 150 / 46-75-29 / 167 chars):
  defects found by the builder's gates — (a) P7 teaser band ended at
  2582.12 (> 2540): Spanish clinic notes wrapped to 2 extra lines
  (+53.04) and the frame-box breakdown to 2 lines (+29) against the
  readers'-box saving (−12); (b) P8 keys flow overflowed with the last
  6 items clamped onto one baseline (Flow `_fit` clamp; the stacked
  items were unreadable); (c) 2 BOXTITLE flags (P1 trend footnote,
  P4 schedule title); (d) 1 untranslated note (#37, inherited from a
  gap in the sibling table this transform was adapted from).
  All other gates already green in round 1 (freeze strict-CJK 0,
  P8 CLEAN 150=150, kinsoku 0, gloss 39=39, phrases 8×2, images
  identical, P6 labels 0.0%).
- **Round 2** (transform edits only): added the missing note; shortened
  8 Spanish answer notes to one line each (11 P8 lines saved: the
  Reading-Week-Monday, temperature, Ishikawa-museum, Shibuya-ban,
  2–0-title-rate, Naruko-peak, and both Kyushu-search notes);
  shortened 2 clinic notes to one line each and the readers'-corner
  disclosure from 7 to 6 lines; shortened the P1 footnote line and the
  P4 schedule title to fit their boxes. Result: P7 teaser 2500.08,
  P8 down to a single overflowing item (#150, 24 points over),
  occlusion 0 flags, P8 CLEAN 150=150. The single remaining overflow
  was still a gate failure (SOP: FLOW OVERFLOW must be handled).
- **Round 3** (final): shortened 3 more Spanish answer notes to one
  line each (Culture-Day-nationwide, Kanazawa-light-up, Japan-Series-G1
  notes). Result: **zero FLOW OVERFLOW, P8 keys flow ends at 2533**
  (< 2540), occlusion 0 flags, all other gates re-verified green, all
  8 cards re-inspected visually. Only P8 changed between round 2 and
  round 3 (P1–P7 SVGs and cards byte-identical), as expected: every
  round-3 edit touched a note that prints only on P8.

Builder's own full pass: registry re-derived and compared item by
item with the core; freeze diff reviewed node by node (P7 added/removed
lists read in full; P8 key-part comparison in §5); all Spanish read in
the rendered cards (8/8 pages visually inspected); weekday/number
checks in §6; geometric audit in §7.

## 10. Deviations from W43 JA×ES (same pairing, earlier week)

- VOL.2 (W45) vs VOL.1 (W43); week Nov 2–8 vs Oct 19–25; topics are
  the W45 core's (Culture Day / autumn leaves / Reading Week /
  Japan Series / Halloween), not W43's.
- Core totals differ: A2 46 / B2 29 here vs A2 48 / B2 27 in W43
  (B1 75 and 150 total identical).
- Furniture identical except the volume number: badge string, slot
  (y=356), size (19pt), weight (700), and fill (BRICK #a4553a) match
  the W43 shipped SVG exactly; footer and page line match with VOL.2
  substituted; gloss prefix «Nota — » and P8 separator «— PÁGINA N —»
  match.
- P8 E-zone pattern identical to W43 (137/138 re-aimed, 139/140
  prompt-only); P8 matching instruction «Une palabra y definición»
  reuses W43's overflow fix verbatim; phrase page tags «Página N»
  match W43; type/instruction labels match W43.
- Readers' corner differs structurally because the W45 core carries
  both a Japanese and a Chinese disclosure line where the W43 core
  carried one: both were replaced by a single Spanish disclosure +
  invitation (see §6), following the W45 sibling (JA×EN/JA×DE)
  precedent rather than the W43 shape.
- P8 answers header («答え · Respuestas — ordenadas por página,
  busca el número» + «Una breve explicación en español por
  respuesta · ✓ = ejercicio con modelo») matches W43.
- No other deviation: image set, credit lines, and caption wording are
  the core's (see §12), as in W43.

## 11. Reproduction

```bash
cd hidden_files/weekly-report-w45-ja-es-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python transform.py  # pristine core -> edition build (asserts every source)
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py         # content12+34+56+7+8 in ONE process (registry order = numbering)
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py      # svg -> cards PNG -> Lucerna-VOL2-ES.pdf + Lucerna-VOL2-ES-web.pdf
```

Fonts: Noto Serif/Sans CJK (JP face) + UnifrakturMaguntia (masthead).
System python3 has no cairosvg — the tools venv is mandatory. Content
modules are never imported inside the core build directory and never
run standalone (one-process driver rule); shared content modules are
re-rendered through run.py after every fix.

## 12. Images (4, all from the core's verified set; record in build `assets/CREDITS.md`; every image confirmed present in the final render, payloads byte-identical to the core)

| Page | File | Subject | Author (Commons API Artist field) | License |
|---|---|---|---|---|
| P1 | maple.jpg | autumn maple leaves | Poliphilo | CC0 |
| P3 | hiroshige.jpg | Utagawa Hiroshige III, 1876 imperial-inspection procession print (captioned as a Meiji-era art print for Culture Day arts, NOT as a W45 event photo) | Hiroshige III | Public domain |
| P4 | stadium.jpg | Yokohama Stadium "Dream Gate" — the actual Games 1–2 venue | Syced | CC0 |
| P5 | pumpkin.jpg | jack-o'-lantern pumpkins | Petr Kratochvil | Public domain |

Credit lines on the pages (frozen core text): P1 «写真：Poliphilo —
CC0（Wikimedia Commons）», P3 «版画：歌川広重（三代）—
パブリックドメイン（Wikimedia Commons）», P4 «写真：Syced —
CC0（Wikimedia Commons）», P5 «写真：Petr Kratochvil —
パブリックドメイン（Wikimedia Commons）». One chart (P6, practice
data, labeled) and the P4 two-game record table are drawn in code. No
copyrighted modern photography anywhere. No new image was downloaded.

## 13. Residual, disclosed (inherited from the core)

- Feature-column whitespace remains on P2/P4/P5/P6 (same pattern as
  the core and VOL.1).
- P2 and P6 carry no photo (same pattern as the core).
- Japan Series G3–G7 results and Halloween Oct 31 outcomes are NOT in
  this issue (core verification debt, stated on P4/P5 and deferred to
  VOL.3 — not invented here).
- Lifestyle buzz items rest on the note.com Oct 22 X-buzz roundup,
  not survey data — attributed as such on every page that uses them,
  per the core.
- The P5 Halloween block claims no event outcome; only the standing
  rules and the scheduled dates are printed (core).
- VOL.3 promises printed on P7 (frozen core text): Reading Week ends
  (Mon Nov 9) closing report; Japan Series final-result roundup;
  紅葉の見頃の続き; real readers' letters + the best P8
  『私の11月の週末』 writing (or another honest disclosure if none
  arrive).
