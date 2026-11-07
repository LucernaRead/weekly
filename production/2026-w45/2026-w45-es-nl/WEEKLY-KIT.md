# La Lucerna · VOL.2 · ES × NL — WEEKLY KIT

**Edition**: Spanish target text (frozen VOL.2 core) × Dutch explanations —
the edition for Dutch-speaking readers («de editie voor Nederlandstalige lezers»).
**Pairing**: target `es` × native `nl`. Masthead: **La Lucerna** (as the core ships).
**Issue week**: Monday 2 — Sunday 8 November 2026 · **Cover date**: Monday 2 November 2026.
**Source core**: `files/weekly-report-w45-es-core/` (build
`hidden_files/weekly-report-w45-es-build/`), in its post-Fix1/Fix2 state
(the un-independently-verified 12 November committee-vote date was already
removed from the core by its Fix 1 and is NOT reintroduced here — zero
occurrences of «12 de noviembre» in this edition's SVGs).
**Build dir**: `hidden_files/weekly-report-w45-es-nl-build/` (copy of the core build).
**Deliverables** (this dir): `svg/` ×8, `cards/` ×8 (1950×2700),
`La-Lucerna-VOL2-NL.pdf` (print), `La-Lucerna-VOL2-NL-web.pdf` (web, < 10 MB),
`WEEKLY-KIT.md` (this file), `ABSTRACT.txt` (Dutch, one line).
**Status**: **builder-complete, NOT finalized — independent proofread still pending.**
No Discord post, no card/PDF dump into main chat, no cron, no weekly-git
touch was made by this build.

## 1. Baseline proof (tools/freeze.py)

`tools/freeze.py baseline` on the unmodified copied core build, re-run by this
builder: **8/8 SVGs byte-identical** to the shipped core SVGs
(p1 a1b30102… / p2 10e78c2e… / p3 5986ba9e… / p4 1894836e… /
p5 cd15c68b… / p6 fcfccf82… / p7 b1774024… / p8 d1c46fa4… — full hashes in §11).
Core SVG sha256 recorded before and after: all 8 identical — the frozen core
was never touched. Proof log: `hidden_files/w45/es-nl-proof/freeze-baseline.log`.
Prior residue: `hidden_files/w45/es-nl-core-hashes-before.txt` (2026-10-27 18:40 UTC)
and `…-after.txt` (18:52 UTC) from the interrupted previous build match the
same 8 hashes.

## 2. Method

Explanation layer rewritten into Dutch by a count-asserted literal transform
(`hidden_files/w45-es-nl-transform.py`, applied to the BUILD COPY ONLY;
whole-line / exact-unique-literal replacements per tools/README #17 — no AST
byte-offset splicing; value-map replacements use bare text, never repr
literals, per #18). Every replacement goes through `rep(files, old, new,
expect)`, which counts occurrences across the listed files and **aborts on
zero hits (unless explicitly allow_zero) or on any expect mismatch**; Spanish
target-language text is never a replacement target. The explanation method
`bridge()` was renamed to `expl()` (def + 20 call sites, as in the W43 ES×NL
build code); `bridge` occurs **0 times** in this edition's build code and SVGs.
Furniture strings are copied verbatim from the shipped W43 ES×NL edition
(`files/weekly-report-es-nl/`), VOL.1 → VOL.2 only, topics updated to this
week's (see §5). svglib.py is byte-identical to the core's; bslib4.py differs
only in the footer line, the page line, the `bridge` → `expl` rename and the
gloss prefix (see §5). Answer-generation code is byte-identical to the core's
— this edition prints in the core's own **dash style**
(`N. key — note`; writing items `N. ✓ note`), like the core and like W43 ES×NL
(tools/README #8, #14: bracket form verified from the family build code, not
from the core's rendered SVG — see §6).

Layout fixups after the transform, all count-asserted (wording-only throughout):
- `w45-es-nl-fixup.py`: P6 exercises 19pt/gap3 → 18.5pt/gap2 (×18, Dutch notes
  overflowed at 19pt, as English did in the W45 ES×EN KIT precedent); P8 answer
  lines 13.5pt/1.16 → 13.2pt/1.12 (×1 + ×1). Chart/article geometry untouched.
- `w45-es-nl-fix2.py`: three `match_set` type names the transform loop missed
  (line-break pattern) → «Woorden combineren» (×1 each in content12/34/8).
- `w45-es-nl-fix3.py`: four telegraphic P8-note trims, keys untouched (incl. the
  P8 #1 note and the #131 Ana/Pablo note); each trim verified 2 → 1 wrapped
  lines at serif 13.2 / width 434.
- `w45-es-nl-fix4.py`: one missed apparatus fragment «(原形 acoger)» →
  «(infinitief: acoger)» (assert = 1).
- `w45-es-nl-fix5.py`: P7 col-3 compression (W45 ES×EN KIT precedent): word note
  4 → 3 lines (×2 occurrences) and the editorial disclosure 5 → 3 lines (×1);
  col3 ends 1820.08, preview title 2484.08 — the disclosure keeps all three
  facts of §8.

Reproducibility: a scratch copy of this build dir (OUT repointed to scratch,
shipped files untouched) re-ran through the single one-process driver
(`run.py`, tools/README #7) produces **8/8 SVGs byte-identical to the shipped
ones** (log: `hidden_files/w45/es-nl-proof/scratch-rerun.log`).

## 3. Totals (registry, one-process run)

TOTAL **150** exercises · A2 **50** · B1 **72** · B2 **28** · per page
**10/18/18/18/18/18/12/38** (identical pagination to the core).
Type counts (Dutch names, counts identical to the core's):
Zinnen aanvullen 48 · Meerkeuze 47 · Cloze-meerkeuze 13 · Woorden combineren 12 ·
Zinnen omvormen 10 · Lezen: waar/onwaar 8 · Zinnen maken 7 · Vertalen 4 ·
Schrijven 1.
Build warnings: **FLOW OVERFLOW 0 · HEAD TOO WIDE 0** (final build, scratch
re-run log confirms 0 occurrences of either string).
Writing model text (P8 §H, frozen Spanish): **84 words** measured by
whitespace split, byte-identical to the core's MODELO.

## 4. Per-page contents (same as the core; only the explanation layer is Dutch)

| Page | Section | Content |
|---|---|---|
| P1 | PORTADA | Headline «La cuenta atrás del 29-N: la vivienda decide la campaña» (27 days to the vote; housing the top issue at 55,7%); week in figures; five keys (no invented figures); contents; word of the week «la precampaña»; editorial house illustration (not a photo); briefs; lightning quiz. Exercises 10 |
| P2 | VIDA | «El puente del lunes 2»: the nine holiday regions (BOE list verbatim) vs working regions; why Sunday 1 November shifts to Monday in some regions; week calendar (Tue 3 Nov Champions League + BOE formal candidate list; Sat 7 Nov Valencia–Real Madrid; Sun 8 Nov NFL + Atlético–Barça); date-format box; days-of-the-week overview. Exercises 18 |
| P3 | CULTURA | Retrospective only: Thu 29 Oct Valencia DANA memorial (no casualty/attendance figures printed); Sat 31 Oct Halloween + Catalan Castanyada + Galician Samaín; Sun 1 Nov All Saints (flowers at graves); roasted-chestnut photo (CC0). Exercises 18 |
| P4 | DEPORTE | Europe first, Sunday 21:00: 25 Oct Clásico result (Real Madrid 2–1 at Camp Nou, Mbappé twice, Barça's first league defeat, gap cut to 3 points); Champions League round 4 (3–4 Nov); Europa League 5 Nov; LaLiga round 12 full table (6–8 Nov); Sun 15:30 NFL Bernabéu sidebar. Exercises 18 |
| P5 | JUVENTUD | «Madrid, capital del fútbol americano»: Sun 8 Nov 15:30 Bernabéu NFL (Cincinnati Bengals–Atlanta Falcons, the Bernabéu's second NFL game); both anthems before kickoff; American-football rules primer; 31 Oct Halloween night retrospective; puente plan table; pumpkin-market photo (USDA public domain). Exercises 18 |
| P6 | A FONDO | «La vivienda decide la campaña»: timeline (2 Oct Congress rejects two housing decrees → 5 Oct dissolution → 6 Oct BOE call → 16 Oct coalition notices → 21–26 Oct candidacies → 28 Oct lists published → 3 Nov BOE formal lists → 13 Nov campaign starts → 29 Nov vote; **no 12 November date anywhere, per core Fix 1**); CIS October barometer bars (PSOE 34,0 / PP 22,2 / Vox 17,1 / Sumar 6,1 / Podemos 3,1; fieldwork 1–6 Oct, 5.025 sample, ±1,4, published 14 Oct); top-issue chart (housing 55,7 / immigration 20,9 / economy 20,3); only the CIS set printed, with source/date stated; «LEER UNA ENCUESTA» box; Idealista September second-hand price 2.930 €/m² (+11,8% year-on-year, source stated). Exercises 18 |
| P7 | LENGUA | Three grammar columns (A2 dates; B1 comparatives; B2 promise subjunctive); error clinic ×4; word of the week «la precampaña»; readers' letters = clearly labelled editorial example letter (Ana, see §8); 8 golden sentences verbatim from this issue's articles; VOL.3 preview (13 Nov campaign start, 29 Nov vote, readers' letters + best page-8 texts). Exercises 12 |
| P8 | EJERCICIOS Y RESPUESTAS | 38-item final test (Clásico cloze, cross-page general knowledge, two-city reading, sentence-making, two-way translation, 29-N vocabulary matching, estate-agent dialogue, writing); 84-word model text (Madrid puente vs Barcelona working, consistent with the P2 list); **all 150 answers + one short Dutch note each**, arranged by page from the registry. Exercises 38 |

## 5. Furniture as shipped (verbatim; W43 ES×NL copy, VOL.2)

- P1 masthead subtitle (46pt serif, y=330): «SPAANS WEEKBLAD · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL» (W43: «…VOL.1 · EL RELOJ · EL CLÁSICO · LA F1» — same slot, this week's topics).
- P1 pairing badge (**19.5pt sans bold brick, x=975, y=372 — geometry byte-identical
  to W43's badge element**): «TEKSTEN IN HET SPAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS» (adjective uninflected, as specified; this is the ES-family subtitle-slot case of tools/README #20 — **no discrepancy
  between the W43 shipped geometry and the README #20 description was found for
  this family, so no coordinator ruling is needed on furniture**).
- P1 top strip (21pt, y=92): «CADA SEMANA EN ESPAÑOL · ELKE WEEK · HET SPAANS DAT DE SPANJAARDEN LEZEN» (byte-identical to W43).
- Footers (all pages, 20pt, y=2624): «La Lucerna · SPAANS WEEKBLAD VOL.2 · TEKSTEN IN HET SPAANS · UITLEG IN HET NEDERLANDS» / «Pagina N van 8».
- Gloss prefix (bslib `expl()`/gloss): «Uitleg — » (×5 in the SVGs = the core's 5 gloss boxes: 4 × «译注｜» + 1 × «讲解｜»).
- P8 section separators: «— Pagina N —» (N = 1..8, unaccented Dutch form, as in W43).
- P8 answers header: «RESPUESTAS · Antwoorden — per pagina gerangschikt; zoek op nummer» / «Bij elk antwoord een korte uitleg in het Nederlands · ✓ = met voorbeeldtekst».
- Exercise heads: «EJERCICIOS · Oefeningen van pagina N»; answers pointer: «Antwoorden op pagina 8 · Niveaus door elkaar — zoek op nummer».
- Band subtitles pair Spanish + Dutch throughout (e.g. P6 «NIVEL B2 · La vivienda decide la campaña · Huisvesting beslist de campagne»; P7 band «Tres niveles, tres herramientas · Drie niveaus, drie hulpmiddelen» — Dutch wording shortened only where ink width required it; no Spanish band text altered).
- P7 phrase tags: (Pagina N) unaccented ×8 — (Pagina 1)×2, (Pagina 2)×1, (Pagina 3)×1, (Pagina 4)×1, (Pagina 5)×1, (Pagina 6)×2 — counts equal to the core's (Página N) tags in order [1,2,3,4,5,6,6,1]; zero accented «(Página» left among the P7 tags. (Coordinator KIT-only correction 2026-10-27: the builder draft listed (1)×1/(2)×2/(3)×2 and claimed edition-wide zero accented residue; P1 retains two frozen accented references byte-identical to the core — see §14. Paper unchanged.)
- Exercise type names (registry-level localisation, counts unchanged): see §3. Instruction tags: 填空→Vul in · 判断→W/NW · 造句→Zinnen maken · 改写→Herschrijf · 翻译→Vertalen · 写作→Schrijven · 把词和释义配对→Combineer. Apparatus: «(原形 …)»→«(infinitief …)» (incl. fix4's acoger).

## 6. Printed-note verification (tools/p8.py)

`p8.py compare --core-p8 …/weekly-report-w45-es-core/svg/p8-ejercicios.svg
--edition-p8 …/weekly-report-w45-es-nl/svg/p8-ejercicios.svg --total 150`:
**status: CLEAN — core 150 noted, edition 150 noted, missing=[], extra_count=0.**
Tool keydiff = [17, 18, 19, 20, 60, 61, 62, 63, 64, 72, 83, 85, 95, 96, 98, 107,
117, 137, 138, 148]. Independent dash-parse re-verification (key = printed
segment before the first « — », per tools/README #13 — suspect the tool before
the edition) clears all but two:
- **True key changes (2), both adjudicated legal under the W43 same-pair
  precedent**: the two translation items whose key IS the translated sentence:
  #137 core «周一在九个自治区是假日。» → «Maandag is een feestdag in negen autonome regio's.» (note «对照原文» → «zie het origineel»);
  #138 core «周日我们看 NFL 和马竞–巴萨。» → «Op zondag kijken we naar de NFL en Atlético–Barça.» (same note change).
- **Reverse translation items — keys byte-identical**: #139 «El Bernabéu acoge un partido de la NFL.» ✓; #140 «Cada gráfico tiene que llevar su fuente.» ✓ (notes translated only: 承办→organiseren, 必须→moeten).
- **The other 18 tool keydiffs are extractor artefacts, keys byte-identical by
  dash-parse**: #17 preguntan, #18 anochece, #19 descansamos, #20 dura, #60 «El Madrid ganó 2–1 en el Camp Nou.», #61 «Mbappé marcó dos goles.», #62 «El Barça perdió su primer partido.», #63 «Mourinho recortó la distancia.», #64 «Los aficionados fueron al estadio.», #72 acoge (tool's paren branch absorbs the Dutch parenthesised gloss appended to the note); #83 A, #85 C, #95 para que, #96 Aunque, #98 muestra, #107 mejor, #117 A, #148 A (tool's paren key absorbs the note text before the paren group — Chinese in the core, Dutch here; the dash-parsed key is the same letter/word in both).
- Writing item #150: «✓ voorbeeldtekst in deel H (84 woorden)» (core: «✓ 范文见本版 H 区（84 词）»); the 84-word Spanish model text is frozen byte-identical to the core's. Bracket form: edition build code uses half-width `(…)` in its Dutch notes (core build code uses full-width `（…）` in the corresponding Chinese notes) — the family's Dutch-note form, verified from code per README #14, not from the rendered SVG alone.
- Full dash-parse table: `hidden_files/w45/es-nl-proof/p8-keydiff-verify.txt` and `p8-el-trace.txt`.

## 7. Freeze diff classification (tools/freeze.py diff --strict-cjk)

Per page (added/removed strings): p1 +27/−25 · p2 +54/−45 · p3 +34/−30 ·
p4 +32/−27 · p5 +51/−40 · p6 +28/−27 · p7 +45/−42 · p8 +201/−177.
**Added CJK characters: 0 on every page** (edition CJK total 0 on all pages
except P7 = 2, which are the full-width parentheses of the frozen Spanish
letter attribution «（carta de ejemplo, escrita por la redacción）», present
identically in the core; **zero Han characters anywhere in the edition's SVGs**).
Spanish-token audit (multiset token diff over all SVG text, core vs edition):
every lost Spanish token is accounted for, and no Spanish body token is lost:
- P1 subtitle furniture replacement (core «EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA» → W43-style topic subtitle): periódico, semanal, aprender, vida, desde, españa, español, para, el (−1 each on P1).
- Footer English furniture replacement (core «LUCERNA SPANISH WEEKLY» → Dutch footer): lucerna −1 per page, spanish/weekly −8 total.
- P7 phrase tags (Página → Pagina, W43 precedent) and P8 separators (PÁGINA → Pagina): página 11→3 on P7 (the remaining 3 are Spanish body references, e.g. «página 6/8» in grammar text), 8→0 on P8.
- P8 explanation-note translations (keys unchanged): #1 note («las listas ya están presentadas; ahora se escriben los programas» → Dutch «lijsten ingediend; nu de programma's geschreven» — the sentence itself stays intact as P1 body text and as a P7 golden sentence) and #102 note («el 1 = el uno» → «de 1e = el uno», Spanish example kept).
- All other removed strings are Chinese explanation-layer strings or wrap fragments of lines whose Dutch explanation changed the line breaks (identical Spanish wording, new breaks). **No unlisted Spanish token loss — no stop-work condition triggered.**
Proof: `hidden_files/w45/es-nl-proof/freeze-diff.json`,
`freeze-diff-analysis.txt`, `spanish-token-diff.txt`, `spanish-token-diff-perpage.txt`.

## 8. Readers' letters (no fabrication)

P7 «CARTAS DE LOS LECTORES» reuses the core's disclosure + Ana example letter
with **only the explanation layer translated** — no reader, letter or quote invented:
- Spanish letter text byte-identical to the core's (Ana, studying Spanish in
  Shanghai, no puente on Monday 2, watching Atlético–Barça and the NFL on
  Sunday) — frozen from the core, NOT a claim about a Dutch reader; the letter
  keeps its full-width-paren attribution «（ejemplo, escrito por la redacción）».
- Spanish editorial note byte-identical («Nota de la redacción: al cierre no había cartas reales ni los mejores textos de la página 8; publicamos este ejemplo y la promesa pasa al VOL.3.»).
- Dutch disclosure carries all three facts: «Opmerking: geen echte brieven of beste pagina-8-teksten; daarom een voorbeeldbrief. Belofte: VOL.3.» (1: no real letters received; 2: no best page-8 texts received; 3: example printed, promise carried to VOL.3).
- VOL.3 preview (Spanish, frozen) still invites letters + best page-8 texts («Además: tus cartas y los mejores textos de la página 8»).

## 9. Geometric occlusion audit (tools/occlusion_audit.py, selftest OK)

- Selftest: all 6 planted classes fire exactly once; clean controls silent.
- Edition run: **0 flags**. Core run: **0 flags**. With `--core`: **NEW flags = 0**.
- Same-baseline row scan (tools/README #10 method, previous builder's
  `w45-es-nl-rowcheck.py`): 7 sub-6px gaps, all P1 contents-list pairs
  («Pág. N» <> title, gap +4.0px — a positive separation, not an overlap),
  **byte-identical in the core's own rowcheck output** — inherited frozen
  geometry, not an edition defect.
- P6 chart GRAZE check (tools/README #12 method, `w45-es-nl-chartcheck.py`):
  **later-rect overlaps: 0** in both edition and core. Element-level P6
  comparison: article + chart texts at y<1950 are 100 = 100 with only the two
  furniture band titles differing (Chinese → Dutch); **all chart bars
  byte-identical** (CIS bars 408.0 / 266.4 / 205.2 / 73.2 / 37.2; top-issue bars
  417.75 / 156.75 / 152.25; chart boxes identical).
- **Known frozen defect, coordinator-adjudicated non-blocking (task §5)**: the
  P6 «Inmigración» chart label's ~5px bar graze is frozen core geometry — the
  label element (x=1011, y=1717, 21pt serif) is identical in core and edition,
  and the chart bars above are byte-identical. Geometry kept exactly as the
  core's, per the coordinator's ruling; **this build did not touch the core chart**.
- Proof: `hidden_files/w45/es-nl-proof/occlusion.json` (edition+core),
  `occlusion-edition-only.json`, `occlusion-core-only.json`, `rowcheck.log`,
  `rowcheck-core.log`, `chartcheck.log`, `chartcheck-core.log`, `p6-compare.txt`,
  `p6-chart-compare.txt`.

## 10. Gloss, images, golden sentences

- **Gloss (tools/README #21 — split on `·` itself)**: core 19 items = edition
  19 items, per box 5/5/5/4 (content12 / content34 ×2 / content56), Spanish
  headwords item-for-item equal (festivo, el puente, la comunidad, anochecer,
  el horario de invierno; sobrio, el homenaje, el disfraz, el boniato,
  el cementerio; la jornada, recortar la distancia, recibir, visitar,
  el Metropolitano; el emparrillado, el himno, el touchdown, la calabaza).
  Proof: `hidden_files/w45/es-nl-proof/gloss-images-p7.txt`.
- **Images (payload byte-identical to the core)**: P3 roasted chestnuts
  (CC0, Wikimedia Commons) payload sha256
  `39eaac936006604ab544173c6e8b6f59cab966d847c4249bcad984c19d9f4655` (coordinator KIT-only correction 2026-10-27: builder draft listed `54adf4fa…`, which has no source in the core KIT or build tree; measured embedded payload = build asset `castanas.jpg`, core = edition byte-identical);
  P5 pumpkin market (USDA public domain) payload sha256
  `70542c15d5106c4a1a93fda258924c156660a59affa38c969c38db33deeaa57d` (coordinator KIT-only correction 2026-10-27: builder draft listed `91bd483d…`, which has no source in the core KIT or build tree; measured embedded payload = build asset `kuerbis.jpg`, core = edition byte-identical);
  P1 house illustration is vector, not a photo — its 4 path elements are
  identical in core and edition (joined sha prefix `989cf5ae…`).
  Credit lines are Spanish and frozen (see core KIT §11 / build assets
  `CREDITS-VOL2.md`); P1 caption states the illustration is editorial art,
  not a photograph.
- **P7 golden sentences**: the 8 FRASES quotes each occur **exactly 2 times**
  in the whitespace-normalised full text of both edition and core (article
  once + P7 once), with Dutch translations and (Pagina N) tags. Proof:
  `hidden_files/w45/es-nl-proof/p7-quotes-norm.txt`.

## 11. PDF pins (final render)

- Print: `La-Lucerna-VOL2-NL.pdf` — **7,163,203 bytes**, 8 pages,
  sha256 `7e0398c1412ac99e0934331f8672488347e9fc1fe7373a13e788c8b725c3fbec`.
- Web: `La-Lucerna-VOL2-NL-web.pdf` — **3,739,003 bytes (< 10 MB)**, 8 pages,
  sha256 `4130e4bef0c5d8150200307ed5fac2705929d95948edc1676408fcbc7bc7b549`.
- Cards: all 8 PNGs 1950×2700 (rendered from these SVGs by the build's
  `render.py`: CairoSVG print PDF + JPEG q85 @1400px web PDF, the core's recipe).
- Edition SVG sha256:
  p1 `c77fe533c5e6abb794f5e5548fa002ab8ad7eb350616ba7914d748a4b715ff8b` ·
  p2 `3bf43b787d063294a709a7990af530c26d484ac886de8aaa32fba4b58bfbcddf` ·
  p3 `47f1ff9ee25a801b3bb209635430a9fb1069d638a6752456a2ce90cdafa79a61` ·
  p4 `68a7e69beb87b4a492ed9bdb3640601c04881da21c709a5c46f297983c62cf9b` ·
  p5 `31d90b5f07ec372cbe5fddd74edb9c7708498f5fd02530c9651c79aa19458b94` ·
  p6 `547fd1961aa411cf0c5a101056d594e309bb109db5e88bfaebe857938767ae8c` ·
  p7 `d63e44d0e77df77392eb06702140d2ca5496a6ac4b1c660a8809809ecbaa6c88` ·
  p8 `2fa4753c072d126d9d218cffeba2bc4ddfd2fdddca33fad4213cb52d46e97635`.
- Core integrity: core SVG sha256 set identical before/after the whole build
  (§1). No repo insert and no Discord post were made (parent's steps).

## 12. ABSTRACT.txt (verbatim)

> La Lucerna Spaans weekblad VOL.2: de countdown naar de verkiezingen van 29 november, huisvesting als beslissend thema, het lange weekend van maandag 2 november in negen regio's, en zondag 8 november de NFL in het Bernabéu om 15:30 plus Atlético–Barça om 21:00; Spaanse teksten met Nederlandse uitleg, niveau A2–B2, 150 oefeningen, voor Nederlandstaligen die Spaans leren met Spaans nieuws.

Checks: one line, Dutch, no ASCII double quotes, masthead + target language
name + A2–B2 + 150 exercises present, real topic keywords (29 November
election countdown, housing, 2 November long weekend in nine regions,
8 November NFL Bernabéu 15:30 + Atlético–Barça 21:00) and a learner search
phrase («Spaans leren met Spaans nieuws»).

## 13. Build commands (reproduction)

- Build dir: `hidden_files/weekly-report-w45-es-nl-build/` (single one-process
  driver; never run content modules standalone, never import inside the core
  build dir — tools/README #7/#11).
- Transform (already applied; re-running it on an already-transformed copy
  would fail its count assertions — it is a record of how this build was made,
  not an idempotent script): `hidden_files/w45-es-nl-transform.py`, then
  `w45-es-nl-fixup.py`, `w45-es-nl-fix2.py`, `w45-es-nl-fix3.py`,
  `w45-es-nl-fix4.py`, `w45-es-nl-fix5.py` (each count-asserted; see §2).
- One-process build: `cd hidden_files/weekly-report-w45-es-nl-build &&
  ../../tools/venv/bin/python run.py`; render: `../../tools/venv/bin/python render.py`.
- Gates (all re-run by this builder, logs in `hidden_files/w45/es-nl-proof/`):
  freeze baseline · freeze diff --strict-cjk · p8 compare · occlusion_audit
  --selftest + edition + --core · rowcheck · chartcheck · gloss/headword ·
  image-payload · P7-quote · scratch re-render 8/8 byte-identical.

## 14. Prior-residue disposition + known items

- **Prior residue**: the previous es-nl builder's work survived the service
  restarts as a near-complete build (build tree + transform/fix scripts +
  8 SVGs + 8 cards + both PDFs + ABSTRACT.txt, written 2026-10-27 18:40–18:52
  UTC); only this KIT was missing. This task re-checked before writing:
  no es-nl process was running (`ps` clean for es-nl), and a 90-second
  re-check showed zero new writes to the es-nl directories before any write
  was made. The shipped SVGs/cards/PDFs were **not** rebuilt or overwritten
  by this builder — they were verified gate by gate (§1–§13) and reproduced
  byte-identically from a scratch copy instead. The only new files in the
  edition dir are this KIT; proof logs went to `hidden_files/w45/es-nl-proof/`.
  Other editions' processes seen running during the checks (es-pt render,
  ru-es freeze diff) are unrelated parallel builds and were not touched.
- **Known items for the independent proofreader** (none blocking at builder level):
  1. P6 «Inmigración» ~5px bar graze — frozen core geometry, coordinator-adjudicated non-blocking (§9); do not "fix" by altering the core chart.
  2. Ana's example letter keeps the core's Shanghai persona in frozen Spanish text (§8) — it is the core's labelled example, not a Dutch-reader letter.
  3. P6 exercise bodies render at 18.5pt (vs the core's 19pt) and P8 answer lines at 13.2pt (vs 13.5pt) — deliberate Dutch-length adaptations (§2), chart/article text untouched.
  4. This KIT is builder self-verification only and **does not replace the
     independent proofread gate** — the edition is builder-complete, NOT finalized.

## 15. Coordinator KIT-only correction (2026-10-27, paper unchanged, FINALIZED)

- Independent proof (hidden_files/w45/es-nl-proof/REPORT.md): paper ZERO defects (SVG / 8 cards / both PDFs), 3 KIT-only items. Coordinator independently re-measured all three and confirmed the proofreader exactly:
  1. P7 tags in order [1,2,3,4,5,6,6,1] in both core and edition → (1)×2, (2)×1, (3)×1, (4)×1, (5)×1, (6)×2 (§5 corrected).
  2. Edition P1 retains two frozen accented references `(Página 4)` and `(Páginas 4 y 5)`, byte-identical to core P1 — the edition-wide "zero (Página" claim was false; corrected to P7-tags-only (§5). Paper correct as frozen core text.
  3. Embedded image payloads: P3 `39eaac9360…f4655` (470,292 B, = asset `castanas.jpg`), P5 `70542c15d5…eaa57d` (346,249 B, = asset `kuerbis.jpg`); core = edition byte-identical (§10 corrected; builder-draft hashes had no source).
- Only KIT text was edited; no SVG/card/PDF touched, paper hashes unchanged. Per the JA KIT-only precedent, no new proof round is needed. FINALIZED. Proofreader's P1 Dutch-shortening observation is accepted as a variant, not a defect.
