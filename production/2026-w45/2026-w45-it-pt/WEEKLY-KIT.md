# WEEKLY-KIT — La Lucerna VOL.2 · W45 IT × PT

**Edition**: Italian target text (frozen W45 IT core, VOL.2) × Brazilian Portuguese
explanations, for Portuguese-speaking readers. Week: Mon Nov 2 – Sun Nov 8, 2026
(issue dated Mon Nov 2, 2026). Masthead: **La Lucerna**.
Build: `hidden_files/weekly-report-w45-it-pt-build/` (copy of the W45 IT core
build + `transform.py` with fix rounds 1–3; every fix-round edit lives in
`transform.py`, never only in a content file).
Deliverables in this dir: `svg/` ×8, `cards/` ×8 (1950×2700), print + web PDF
(§11), `ABSTRACT.txt` (§12).
**Status: builder-complete (all mechanical gates measured green). NOT
finalized — a fresh full independent proofread is still required before
delivery. Nothing was posted to Discord, nothing was sent to the main chat,
no cron was created, weekly-git was not touched.**

## 1. Baseline proof (before any edit)

`tools/freeze.py baseline` on the unmodified copy of the core build
reproduced all 8 shipped W45 IT core SVGs **byte-identically (sha256 8/8)**,
and re-hashed the shipped core SVGs afterwards to prove them untouched:

| page | sha256 (core, also final re-verification) |
|---|---|
| p1-prima | 81051bbb0799fafe26bb187fdb71df0eed7b18a52555ffea892e431f87d681a0 |
| p2-vita | d42ce9aedc445111c7bcc62732c355ae037f567b6c49bba448a73532469bb739 |
| p3-cultura | 9e45586d3187ec8e59aba136a5829686a246273b005a2abc7615552efc15e742 |
| p4-sport | 62f75269d2878cd07d00e8a5223d0d259dfceed6a0d5122d2f154b5daf34faa1 |
| p5-giovani | c907b869e4cda01e9185325c72425c96a9c366d70609b6303d4eb43aed4ea089 |
| p6-approfondimento | 5545f8ddae0dab5a4000b295def63197f19d6193b10b740debec418c3fce88f2 |
| p7-lingua | 9fc999f45c9826e676220a9d861a5b5e40afdf986f0c0d962ea587d22f0fed07 |
| p8-valutazione | 3b87e54f30b6c0504e2b8d099aea51f9b4c1b994f1f905bc63d56f6e11c18285 |

Core SVGs re-hashed unchanged at the end of all work (same 8 hashes).
Registry from the unmodified copy: 150 exercises; A2 47 · B1 70 · B2 33;
per page 10/18/18/18/18/18/12/38; writing model 81 words — identical to the
core KIT §1 (these are the W45 IT core's own numbers, measured from the
core, never borrowed from another family).

## 2. Totals (this edition, machine-verified from an independent registry dump)

- Exercises: **150** — A2 47 · B1 70 · B2 33; per page 10/18/18/18/18/18/12/38
  (= core); numbering continuous 1–150 (dump from a scratch copy of the
  final build, OUT repointed, in `scratch/` via the EN sibling's
  `dump_reg.py` pattern).
- Writing model: 81 words (Italian, frozen; `MODELO` byte-identical to the
  core, word-counted from the source string).
- P8 sections: A cronaca 8, B generali 8, C leggi e rispondi 4, D frasi 4,
  E traduci 4, F matching 4, G dialogo 5, H scrittura 1.
- Instructions localized (printed beside exercise numbers): «Completar»,
  «Formar frases», «Verdadeiro ou falso», «Combinar», «Escrever»,
  «Traduzir para português» (E items 137–139), «Traduzir para italiano»
  (E item 140). Registry exercise-type names stay in Chinese (never
  printed anywhere, W43/W45 IT × EN precedent) so the registry stays
  byte-comparable with the core.

## 3. Key-diff registry (complete; machine diff of the two registries + printed-key audit)

Keys differ from the core at exactly **{137, 138, 139}** — the translation-type
items re-aimed at Portuguese (direction IT→PT, as in the core's own
E-section direction for these three items):

| # | core key | PT key |
|---|---|---|
| 137 | 周一第一场寒冷来了。 | Na segunda-feira chega o primeiro frio. |
| 138 | 观众可以免费品尝。 | O público pode provar de graça. |
| 139 | 周日晚上，佛罗伦萨对尤文图斯。 | No domingo à noite, joga-se Fiorentina–Juventus. |

Stems re-aimed at Portuguese (keys unchanged, still the Italian target
sentence):
- #140 stem: «Cada previsão deve ser clara. → ___»; key unchanged
  «Ogni previsione deve essere chiara.», note «dovere = dever».
- #137 note «Ver o texto original.»; #138 note «assaggiare gratis = provar
  de graça»; #139 note «si gioca = joga-se».
- #150 (writing): key not printed; printed note «O texto modelo está na
  seção H desta página, 81 palavras» (core: «范文见本版 H 区（81 词）»).

Notes: all 150 notes are in Portuguese (translated from the core's Chinese
notes); no note contains parentheses (deliberate: the P8 paren format must
parse unambiguously in `tools/p8.py`), and no note contains the banned
intermediary-layer term in either language (scan 0 in all deliverables and
in the build code).
Key format: `N. key (note)` — W43 IT × PT shipped precedent (its P8 SVG),
NOT the core's dash form; writing items print `N. ✓ note`.

## 4. Printed-note set verification

`tools/p8.py compare` (explicit `--core-p8`/`--edition-p8` paths, `--total
150`; the `--target pt` form mis-resolves the core filename to the PT
family's `p8-avaliacao.svg` and was not used):
**CLEAN — core 150 noted, edition 150 noted, missing=[] extra_count=0
uncertain=[]**. Printed-note sets are EQUAL ({1..150} = {1..150}).

### Keydiff adjudication (complete, item by item)

`p8.py compare` reported keydiff
`[6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 137, 138, 139]`.
- **137, 138, 139 — TRUE re-aims** (§3 above, legal).
- **6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77 — paren-branch artifacts,
  NOT real key changes.** Cause (verified by calling the tool's own
  `detect_note` on the segments): the CORE's notes contain full-width
  parentheses （…）, so the tool's paren branch truncates the CORE-side
  "key" at the full-width paren opening, swallowing the dash and part of
  the note into the "key" (e.g. core #6 extracted as
  «previsioni — previsioni = 预报» instead of «previsioni»). The
  edition's notes use no full-width parentheses, so its extraction is
  the true key. **Printed-key verbatim对照 (from the P8 SVGs,
  13pt answer lines, rejoined):** #6 previsioni, #13 guanti,
  #14 crisantemi, #15 termosifoni, #16 fa, #20 resta, #38 mandorle,
  #58 più bella, #71 gratuiti, #74 castagne, #77 ci sarà — byte-identical
  Italian in core and edition for all 11. #140 correctly NOT flagged
  (Italian key unchanged); #150 not a keydiff (writing item).
- P8 notes in Portuguese throughout; P8 printed-note set equality holds
  (§4 head).

## 5. Freeze check

`tools/freeze.py diff` core vs edition (final render): added CJK = 0 on
every page (edition CJK characters = 0 on every page); every differing
line was read in full (diff5.json) and classified — all are explanation
layer (Portuguese glosses, instructions, bridges, notes, E TU translations,
quote translations), pairing furniture (§6), the §3 registry items, or
re-wrap fragments whose Italian words survive unchanged (P1/P5 box
parentheticals re-wrapping because the Portuguese parenthetical changed
line widths — same class as the W43 IT × PT proofread's adjudicated
re-wrap fragments). No Italian target text changed. Specifically verified:
- P7 word-box Italian definition sentence **byte-identical** to the core:
  «« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se
  piace. Questa settimana vive a pagina 3, alla finale del Panettone.»
  Only the gloss line below it is localized («assaggio = prova, página 3.»).
  Definition-sentence localization would be a blocking failure; none occurred.
- Manovra disclosure on P2/P6: Italian body text frozen; only the Chinese
  disclosure lines were translated into Portuguese (wording verified
  against the core's Italian: expected date ~Oct 28, disputed point,
  DPB figures — NO outcome claimed or invented anywhere).
- P6 chart labels, fixture table, captions, credits: byte-identical Italian.
- Zero CJK characters in the final SVGs (Unicode-range scan, all 8 pages).
- Banned term: 0 occurrences of the banned intermediary-layer term in the SVGs, this KIT, ABSTRACT.txt,
  and the build code.

## 6. Portuguese furniture — as shipped (verbatim)

Strings verbatim from the shipped W43 IT × PT SVGs
(`files/weekly-report-it-pt/svg/`), VOL updated to VOL.2:

- P1 badge: «TEXTOS EM ITALIANO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA
  OS LEITORES DE LÍNGUA PORTUGUESA»
- P1 top strip middle: «OGNI SETTIMANA IN ITALIANO · TODA SEMANA · O ITALIANO
  QUE OS ITALIANOS LEEM»
- P1 subtitle (strap line): «SEMANÁRIO ITALIANO · VOL.2 · PRIMO FREDDO ·
  PANETTONE · SERIE A» (see §7 deviation 6 for the article-drop).
- P1 band right: «A SEMANA DO PRIMEIRO FRIO» / «A semana do primeiro frio ·
  ver página 2»
- Footers (all pages): «La Lucerna · SEMANÁRIO ITALIANO VOL.2 · TEXTOS EM
  ITALIANO · EXPLICAÇÕES EM PORTUGUÊS» / «Página N de 8»
- Gloss prefix: «Nota — » (the library adds it; gloss strings carry no prefix)
- Band titles: «VITA · VIDA COTIDIANA», «CULTURA · CULTURA»,
  «SPORT · ESPORTES», «GIOVANI · JOVENS», «APPROFONDIMENTO · APROFUNDAMENTO»,
  «LINGUA · LÍNGUA», P8: «VALUTAZIONE E RISPOSTE · AVALIAÇÃO E RESPOSTAS»
- P1 numbers-box title «LA SETTIMANA IN CIFRE · EM NÚMEROS» at tsize 20 and
  P2 phrase-box title «LA FRASE PER RICORDARE · MACETE» at tsize 20 (both
  per the shipped W43 IT × PT KIT §6 deviation 3).
- P8 keys head: «RISPOSTE · RESPOSTAS — organizadas por página: busque pelo
  número do exercício»; separators «— PÁGINA n —»; page-8 subtitle note:
  «Uma nota breve em português para cada exercício · ✓ = exercício de escrita»
- P7 quote page tags stay Italian «Pagina N» (W43 IT × PT shipped precedent:
  its P7 quotes carry «(Pagina N)»); quote translations are Portuguese.

### Badge geometry — W43 string, W45 insertion (adjudication, recorded)

W43 IT × PT puts its badge in the y=372 slot at 20pt, but the W45 core's
y=372 is FROZEN Italian strapline («IL GIORNALE SETTIMANALE PER IMPARARE —
L'ITALIA VERA, IN ITALIANO, DALL'ITALIA»), so the badge is INSERTED at
y=574, 22pt BRICK centered, following the W45 IT-family insertion precedent
(W45 IT × EN, same core) — replacing the strapline would delete frozen
Italian text. Band bottom is 542, headline label ink starts ~584: the badge
sits clear of both (visually confirmed on the P1 card).

## 7. Deviations from the core (all wording-only, recorded)

1. Badge insertion (§6) — geometry only; string verbatim W43 IT × PT.
2. P1 numbers-box title tsize 20; P2 phrase-box title tsize 20 + MACETE (§6).
3. P8 answer lines dash → paren format (§3, W43 IT × PT precedent).
4. P8 separators PAGINA → PÁGINA (§6, W43 IT × PT precedent).
5. Overflow-driven wording shortenings (build log 0 warnings; every flow ends
   inside its region, P7 col3 ends y=1648, FRASI rule at 1686, 38 px clear):
   P7 errori notes 2/3, P7 parola gloss, P7 letter note, P8 notes
   #24, #44/#134 (shared string), #56, #57, #58, #87, #135 — each verified
   1 line at its print size with the build's own `wrap()` before adoption.
6. P1 subtitle articles dropped (§9 fix round 3b): «IL PRIMO FREDDO · IL
   PANETTONE · LA SERIE A» → «PRIMO FREDDO · PANETTONE · SERIE A» — the
   full form's TRUE ink reached x=1925, crossing both page-frame rects
   (1910/1922); the shortened form's ink ends at 1826.5.
7. P1 day-box note printed with `p.para` (wrapped at box inner width) instead
   of the core's unwrapped `p.text` (§9 fix round 2b) — same first baseline,
   no geometry change elsewhere.
8. P7 parola box height +4 padding (§9 fix round 2f) — formula rounding
   grazed its own border by 1.1 px; col3 still ends 1648.
9. P7 letter box: NO new Italian disclosure sentence (coordinator ruling,
   §10). The letter box keeps the core's exact structure (Italian letter +
   one grey note); only the note language changed.

## 8. Geometric occlusion audit (mandatory gate)

`tools/occlusion_audit.py` (canonical tool, selftest OK — all 6 planted
classes fired, clean controls silent), final render:
**edition 0 flags, core 0 flags, NEW vs core 0** (`scratch/occlusion5.json`).
Intermediate rounds: round 2 = 7 NEW flags (all Portuguese text longer than
the Chinese original in fixed-width/unwrapped slots), all fixed by wording
in fix round 2; round 4 = 0/0/0 already, round 5 re-confirmed after fix
round 3.

Supplementary geometric checks (same-core-family scripts, EN sibling's
`scratch/` tools, run on the final render):
- Right-edge scan, ADVANCE method: **frame violations (>1910): 0** for the
  edition (round 4 had 1 — the P1 subtitle, fixed in round 3b). Remaining
  margin-zone (1885,1910] items are byte-identical frozen core strings,
  identical to the core's own run (P1 parola lines, P2 match option b,
  P8 writing stem).
- Same-baseline collision scan: **7 flags, byte-identical to the core's 7**
  (P1 sommario «Pag. N» <> title pairs at 4.0 ink gap — inherited layout,
  not NEW, visually clean on the P1 card).
- P6 chart-label coverage, baseline-anchored ink method (PIL `getmetrics`,
  anchor `ls`): **worst coverage 0.0%** (gate <30%), edition and core alike.
- Full 8-page frame + right-edge scan: no box rect passes 1885; no text
  advance passes 1910 (see rightedge output in `scratch/`).

## 9. Fix rounds (all edits in transform.py; each round re-ran from a fresh core copy)

- **Round 1 (render):** P7 col3 ended y=1831 (past the FRASI rule at 1686)
  and P8 keys flow overflowed (items 148–150 clamped into the footer zone).
  Fixes: P7 errori notes 2/3, parola gloss and letter note shortened by
  measured lines; P8 notes #24, #44/#134, #56, #57, #58, #87, #135 trimmed
  to 1 line each at 13pt (verified with `wrap()`). Result: P7 col3 1656,
  P8 overflow 0. Baselines: `scratch/svg-round1.txt`,
  `scratch/cards-pdf-round1.txt`.
- **Round 2 (occlusion audit):** 7 NEW flags (see §8). Fixes: P1 day-box
  subtitle, day-box note wrap, sommario title, parola translation
  (1 line), P7 parola title, parola box +4 padding. Result: audit 0/0/0,
  P7 col3 1660. Baselines: `scratch/svg-round2.txt`,
  `scratch/cards-pdf-round2.txt`. (One aborted attempt in this round:
  the day-note fix first targeted a `p.para` call, but the core call is
  `p.text` — the transform's count assertion caught it, the run was
  discarded, and the fix was corrected before any delivery render.)
- **Round 3 (coordinator ruling + subtitle frame):** (a) removed the
  Italian disclosure line added in round 1 — see §10; Portuguese note
  rewritten to carry the «exemplo» fact explicitly (3 wrapped lines);
  (b) P1 subtitle articles dropped after true-ink measurement (§7.6).
  Result: audit 0/0/0, rightedge frame violations 0, P7 col3 1648.
  Baselines: `scratch/svg-round4.txt` (pre-round-3 render),
  `scratch/cards-pdf-round4.txt`; final: `scratch/svg-round5.txt`,
  `scratch/cards-pdf-round5.txt`.

## 10. Readers' corner (no fabricated readers, letters, names, or quotes)

- P7 LETTERE prints the core's labeled editor's example verbatim in Italian
  («Ciao! Sono Li, studio italiano a Pechino… — Li (esempio della
  redazione)») — Li/Pechino are the core's own labeled example, NOT
  presented as a real reader. No reader, letter, name, or quote was invented.
- Disclosure (Portuguese note, 3 lines on the page): «Exemplo da redação:
  sem cartas reais nem o melhor texto da página 8. Escrevam, saem no
  VOL.3!» — states all three facts (it is an example; no real letters yet;
  no best page-8 essay yet) PLUS the explicit imperative invitation
  («Escrevam») with the VOL.3 publication promise («saem no VOL.3»).
  The VOL.3 preview band on the same page carries the Italian promise
  («le vostre lettere vere e i testi migliori della pagina 8») — the
  preview line is NOT counted as the invitation; the invitation is the
  imperative note above.
- **Coordinator ruling 2026-10-27 (IT family, applied here):** the core's
  Italian side has NO disclosure sentence to retain (letter verbatim +
  `(esempio della redazione)` label + preview promise are the whole of
  the Italian material; the disclosure sentence itself is in the core
  reader language). The task wording "disclosure in Italian original +
  reader-language equivalent" therefore means: retain the core's existing
  Italian elements, write the disclosure sentence itself in the reader
  language — and NO new Italian disclosure sentence may be written
  (the core has none, W43 has none, shipped IT × DE has none, and P7
  col3 has no spare room). IT × EN proofread blocking item B1 was ruled
  non-blocking on exactly this ground. The round-1 Italian line added by
  this builder was REMOVED in fix round 3 for this reason; the final
  letter box has the core's exact structure.
- P2/P3/P4/P5 E TU boxes are the core's own open invitations (Italian
  question + Portuguese translation, «Escreve duas frases… e envia-as»),
  unchanged in intent; no real letters are claimed anywhere.

## 11. Deliverables

- `svg/` ×8 (sha256, final render):
  - p1-prima: 4d1886a499144e80fa93f035fa7c0e1b647116f56ce76c651205d240777e7e26
  - p2-vita: e7321272a180de142f066372b0933f211554f4fab11abf09dbe2e60c99764777
  - p3-cultura: ae0480e599cc24799e1ca4cb64f9897ec600a936f224df43bd497505e8c5fb5a
  - p4-sport: 22e857f8f55b91d3c8285be15a0ac9ddc3b81c604792dfdc64d419b6ed0bd254
  - p5-giovani: 8fc1fe6743fca8f712b3db50de45d0096782a70742a38d1effe4a70a7ded17a0
  - p6-approfondimento: 0af73ba8404399eefcfbbaa78a39fe0735767b576f6c27f6561d584a09ec0f53
  - p7-lingua: cfa9a78b7773397a85a6c6975600dad0fa719005752cc872b783d5a99dc38941
  - p8-valutazione: ff82478f96c28c3927385bdf71131ddfb60abe8f5848f14c714889d0f5e2a81e
- `cards/` ×8 (1950×2700 PNG, all 8 visually inspected page by page:
  no overflow, overlap, footer strike, or frame touch on any page; P1
  badge/subtitle/day-box/parola, P6 chart + caption, P7 col3 vs FRASI
  rule, P8 answers bottom vs footer all confirmed by eye).
- Print PDF `La-Lucerna-VOL2-PT.pdf`: **7,137,176 bytes**,
  sha256 ed151a3987d527f88ee54409f7337417759810b929b796715cf222ec9086acd4
- Web PDF `La-Lucerna-VOL2-PT-web.pdf`: **3,622,395 bytes** (< 10 MB),
  sha256 ff156593b4646f0864edde12b762577a5393c6cdde898e772fcb9043627149ca

## 12. Build / reproduce

- Build dir: `hidden_files/weekly-report-w45-it-pt-build/` (bslib4.py,
  svglib.py, run.py, render.py, assets/ copied from the W45 IT core build;
  content12/34/56/7/8.py are the core's, transformed by `transform.py`).
- Pipeline (single process only — never run content modules standalone,
  per tools/README lessons 7/11; content modules share the bslib4
  exercise registry):
  - Transform: `cd hidden_files/weekly-report-w45-it-pt-build &&
    ../../tools/venv/bin/python transform.py` (re-runnable from a fresh
    core copy; every rep() asserts its count).
  - Build: `../../tools/venv/bin/python run.py` (ONE process).
  - Render: `../../tools/venv/bin/python render.py`.
- Interpreters (measured, both steps):
  - run.py: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0,
    cairosvg 2.9.1.
  - render.py: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0,
    cairosvg 2.9.1.
  - System `python3` is also 3.12.3 but ships PIL 10.2.0 and NO cairosvg —
    render.py must NOT be run under system python3.
- Final build: FLOW OVERFLOW 0, HEAD TOO WIDE 0; TOTAL 150; by page
  {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}; by level
  {A2: 47, B1: 70, B2: 33}; model words 81.
- P7 col3 ends y=1648 (FRASI rule 1686, 38 px clear; core: 1673, 13 px).
- P6 exercises end y=2569 (bottom 2580, core-identical); P8 keys end
  inside the answers zone with clear space above the footer rule.
- Gloss counts (rendered gloss() strings, split on ·, measured from the
  final SVGs): P2 6, P3 5, P4 4, P5 4, P6 5 — 1:1 with the core's own
  gloss() strings (P2 6, P3 5, P4 4, P5 4, P6 5, counted from the core
  source, not borrowed from any other family). Gloss boxes: 1 each on
  P2–P6, none elsewhere (distribution 0/1/1/1/1/1/0/0 by page).
- P7 golden sentences: all 8 bare phrases occur exactly 2× issue-wide
  (article + P7) in both core and edition; P7 translations in Portuguese;
  page tags identical to the core's (1, 1, 2, 2, 3, 4, 5, 6, Italian
  «Pagina N» per the W43 IT × PT precedent).
- Images: unchanged from the core (P3 tartufo PD, P5 castagne CC0, P1 frost
  drawing «Disegno della redazione», P6 practice-data chart labeled
  DATI INVENTATI PER L'ESERCIZIO); embedded payloads untouched — P3/P5
  SVGs are byte-identical to round 1 (only P1/P7 changed across fix
  rounds 2–3, P8 unchanged since round 2).
- W43 deviations list (same-pair furniture vs README #20 generalization):
  badge string, footer, band titles, gloss prefix, page line, P8 keys
  head + separators all follow the shipped W43 IT × PT SVGs, NOT the
  generic §20 rules; badge geometry follows the W45 insertion precedent
  (§6) because the W43 slot is frozen Italian strapline in the W45 core;
  P7 quote page tags stay Italian «Pagina N» per W43 IT × PT (not
  localized to «Página N»).
- NOT pushed to git, NOT posted to Discord, NO messages sent (per task).
  Delivery to the LucernaRead/weekly repo is the main line's job.

## 13. Abstract

`ABSTRACT.txt` (Portuguese, one line, no ASCII double quotes — see the file):
names the masthead (La Lucerna VOL.2), the week (2–8 November 2026), the
real topics (primeiro frio, Forum Cultura Milano, Panettone World Cup
final, Festa del Torrone Cremona, Serie A matchday 11), the learner
search phrase («aprender italiano»), the target language (italiano),
levels (A2 a B2) and the exercise count (150 com respostas). Facts taken
only from this edition.
