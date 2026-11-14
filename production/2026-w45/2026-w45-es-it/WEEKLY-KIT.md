# La Lucerna — SETTIMANALE SPAGNOLO VOL.2 · ES × IT (W45)

**Pairing:** Spanish target text (frozen W45 core,
`files/weekly-report-w45-es-core/`, VOL.2, settimana da lunedì 2 a
domenica 8 novembre 2026) + explanation layer written natively in
**Italian**, for Italian-speaking readers. **Status:** builder-complete.
**Independent proofread: PENDING** (parent runs it; repo insert + any
posting happen only after it passes — not done here, and no
final-edition claim is made here). No Discord post, no main-chat
card/PDF dump, no cron was created; the core build dir, the core
edition dir and the W43 edition dir were never written.

## 1. Method & baseline proof

- Build dir: `hidden_files/weekly-report-w45-es-it-build/` — a copy of
  the W45 core build (`hidden_files/weekly-report-w45-es-build/`).
- **Baseline proven before any edit:** `tools/freeze.py baseline` on
  the core build reproduced all 8 shipped core SVGs byte-identically:
  p1 `a1b30102…`, p2 `10e78c2e…`, p3 `5986ba9e…`, p4 `1894836e…`,
  p5 `cd15c68b…`, p6 `fcfccf82…`, p7 `b1774024…`, p8 `d1c46fa4…`
  (full hashes in §8); core SVGs re-hashed afterwards, unchanged.
- All OUT paths in the copy were repointed (all `os.path.expanduser`
  forms) to `files/weekly-report-w45-es-it/`; the single-process driver
  `run.py` renders all 8 pages in one process (shared bslib4 registry).
- Only the explanation layer was rewritten, via the asserted-replacement
  script `hidden_files/w45-es-it-transform.py` (every replacement
  asserting its exact hit count, abort-on-mismatch; longer strings
  before their substrings; cross-page duplicates handled by global
  counts). **Reproducibility verified:** a from-scratch copy + the
  same script + `run.py` reproduces all 8 delivered SVGs byte-for-byte
  (hashes in §8).
- Exercise type names (`完成句子`/`单选`/…) stay frozen in the registry
  (not rendered, except the P8 writing check); only `instr=` labels
  translate, per the W43 ES×IT mapping: Completa · Vero o falso ·
  Costruisci · Riscrivi · Traduci · Scrivi · Abbina le parole.
- Bridge strings follow the W43 IT bare style (no prefix word — the
  core's `讲解｜` prefix is dropped, not translated); gloss prefix is
  `Nota — ` (see §2). The one CJK line left in build code,
  `svglib.py` line 120, is a dead-code illustration comment carried
  over from the core build (never rendered); the rendered SVGs contain
  zero CJK characters (freeze diff: edition CJK = 0 on all 8 pages).
  Residual CJK lines in the build copy are only the frozen registry
  `typ` values and the `写作` type check, none of which render.

## 2. Furniture (verbatim from the shipped W43 ES×IT edition, VOL.1→VOL.2 only)

Source of every string: the shipped W43 SVGs in
`files/weekly-report-es-it/svg/` (+ that edition's KIT §4); where a
W43 string and a generic column note conflicted, the shipped SVG won.
W45-specific topics (edition line, band subtitles, band right lines)
follow the W43 patterns with W45 content.

- Masthead: **La Lucerna**
- P1 badge (brick #a4553a, 22px bold, INSERTED slot y=574,
  strapline y=372 retained — the W43 ES×IT slot, confirmed against the
  W45 ES×DE sibling which keeps the same 574 slot; the README #20
  372/19.5pt replacement describes the EN-column instance, not the IT
  column): `TESTI IN SPAGNOLO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI`
- P1 edition line (46px): `SETTIMANALE SPAGNOLO · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL`
- P1 top strip: `CADA SEMANA EN ESPAÑOL · OGNI SETTIMANA · LO SPAGNOLO DEGLI SPAGNOLI` (the W43 shortened form, kept verbatim — the fuller wording collided with the date line in W43)
- P1 band right lines: `MANCANO 27 GIORNI AL 29-N · LA CASA DECIDE LA CAMPAGNA` / `Il tema di copertina · vedi le pagine 2 e 6`
- Section heads: `VIDA · VITA QUOTIDIANA`, `CULTURA · CULTURA`,
  `DEPORTE · SPORT`, `JUVENTUD · GIOVENTÙ`, `A FONDO · APPROFONDIMENTO`,
  `LENGUA · LA LINGUA`, `EJERCICIOS Y RESPUESTAS · ESERCIZI E RISPOSTE`;
  band subtitles: Italian second half (e.g. P7 `Focus lingua · Tres niveles, tres herramientas · Tre livelli, tre strumenti`, P8 `Pagina 8 · La gran prueba de la semana + todas las respuestas` — the Spanish descriptor kept, Italian page marker only, per the W43 IT proofread ruling).
- Box/section second halves follow W43 verbatim: `LA SEMANA EN CIFRAS · IN CIFRE`, `EL CALENDARIO · IL CALENDARIO`, `EN ESTA EDICIÓN · IL NUMERO`, `BREVES · IN BREVE`, `QUIZ RELÁMPAGO · QUIZ LAMPO`, `LA NOTICIA · LA NOTIZIA`, `AHORA TÚ · TOCCA A TE`, `¿Y TÚ? · TOCCA A TE`, `ERRORES TÍPICOS · ERRORI TIPICI`, `LA PALABRA · LA PAROLA`, `FRASES DE LA SEMANA · LE FRASI DELLA SETTIMANA (testuali, da questo numero)`, `LA PRÓXIMA SEMANA · LA PROSSIMA SETTIMANA (VOL.3)`, `EJERCICIOS · ESERCIZI · PAGINA N`, `EL PLAN DEL PUENTE · IL PIANO` (shortened from `IL PIANO DEL PONTE` — see §5.3), `RESPUESTAS · LE RISPOSTE — ordinate per pagina: cerca il numero` (+ right note `Una nota in italiano per ogni risposta · ✓ = testo modello`).
- Footers, all 8 pages: `La Lucerna · SETTIMANALE SPAGNOLO VOL.2 · TESTI IN SPAGNOLO · SPIEGAZIONI IN ITALIANO` and `Pagina N di 8`.
- Gloss prefix: `Nota — ` (vocab boxes use `termine = gloss` entries).
- P8 separator stays Spanish, frozen from the core (W43 precedent):
  `— PÁGINA N —`. Exercise-page right note (W43 verbatim):
  `Risposte a pagina 8 · livelli misti: cerca per numero`.
- P8 answers keep the core's dash style `N. key — note` and the
  `N. ✓ note` writing form; answer-generation code otherwise
  byte-identical except the §5.1 size/leading change.

## 3. Registry verification & key-diff adjudication

- **150 exercises — A2 50 · B1 72 · B2 28; per page 10/18/18/18/18/18/12/38;
  page/level/type identical to core for all 150.**
- `tools/p8.py compare` (explicit `--core-p8/--edition-p8`, total 150):
  **CLEAN, 150 = 150, missing = [], extra = 0**, keydiff list of 10:
  [83, 85, 95, 96, 98, 107, 117, 137, 138, 148].
  Adjudication, item by item, against the *printed* `N. key — note`
  lines (first-dash split, byte comparison, independent of the tool):
  - **148/150 keys byte-identical to the core.** The 8 non-137/138
    keydiff entries (83, 85, 95, 96, 98, 107, 117, 148) are a **tool
    extraction artifact**: every one of those Italian notes ends in
    an ASCII paren group (`(34%)`, `(55,7%)`, `(scopo)`,
    `(fatto noto)`, `(5.025 persone)`, `(senza más)`,
    `(il Bernabéu ospita la NFL)`, `(il contratto)`), and `p8.py`'s
    paren branch then mis-extracts the key (README #13 class: suspect
    the tool before the edition). Printed keys verified byte-identical
    by an independent dash-parse over all 150 printed answers.
  - **Exactly 2 real key changes, the W43 ES×IT KIT §3 precedent
    (translation items re-aimed ES→reader language):**
    - **#137** key core `周一在九个自治区是假日。` →
      **`Il lunedì è festivo in nove comunità.`**
      (note `confronta con l'originale`)
    - **#138** key core `周日我们看 NFL 和马竞–巴萨。` →
      **`La domenica vediamo la NFL e l'Atlético–Barça.`**
      (note `confronta con l'originale`)
  - **#139/#140** (reverse direction): stems re-aimed at Italian
    (`Il Bernabéu ospita una partita di NFL. → ___`,
    `Ogni grafico deve indicare la sua fonte. → ___`); **Spanish keys
    byte-identical to the core** — same pairing as W43 §3.
  - **#150** (Scrivere, apparatus line): renders
    `150. ✓ Il modello è nella sezione H di questa pagina (84 parole)`
    (W43 wording with the W45 word count 84, not 82).
  - One language-neutral note kept identical to the core: P6 §A
    `34 + 22,2 + 17,1 = 73,3` (digits only).
- **Frozen-text diff** (`tools/freeze.py diff --strict-cjk`, core vs
  edition): **added CJK = 0 on all 8 pages** (core CJK 170/280/161/169/
  247/80/388/981 → edition 0). Every removed non-CJK string adjudicated:
  (a) the core footer English words `SPANISH WEEKLY`, replaced by the
  Italian furniture footer per §2 — the only removed tokens not
  surviving in the edition; (b) re-wrap segmentation fragments of
  frozen Spanish lines whose words survive verbatim in the Italian
  render (P1 cifras box parens, P2 calendar box, P5 plan box, P8
  answer-line wraps); (c) P8 answer segments whose keys are verified
  byte-identical above. No Spanish token was added or removed:
  source-tree diff core-build vs this build touches only `bslib4.py`,
  the five content files and `render.py` (OUT + filenames); every
  changed line is explanation text, furniture, the §5 layout
  parameters, or the apparatus items below.
- **Apparatus-only Spanish-line changes (3, both documented):**
  (1) P5 stem #72 parenthetical `原形 acoger` → `(infinito: acoger)`
  (W43 IT precedent); P5 `ir a + 原形` bridges/notes → `ir a + infinito`.
  (2) P7 letter attribution full-width parens → ASCII
  (`(ejemplo, escrito por la redacción)`) — W43 ES×IT shipped ASCII
  parens; letter body, name Ana and place Shanghái frozen.
  (3) P8 #150 registry key → `(domanda aperta — il modello è qui sotto)`
  (W43 wording); the printed form uses the note branch, unchanged in
  structure. Nothing else: no reader, letter or quote was invented;
  the P7 letter remains the labelled editors' example and the FIX1
  disclosure (Spanish frozen, Italian note translated) still states
  that no real letters or best P8 texts had arrived, promise carried
  to VOL.3.

## 4. P7 phrases

All 8 Spanish quotes verified verbatim in **both** their article page and
P7, each appearing exactly **2 times** across the 8 SVGs (programmatic
count, normalized whitespace), with correct page tags: Página 1, 2, 3,
4, 5, 6, 6, 1. Glosses are the Italian translations.

## 5. Fit defects found in-build and fixed (Italian apparatus only; core geometry and Spanish text untouched)

1. **P8 answer flow overflow** (Italian notes longer): answer lines
   13.5pt/1.16 → **13.2pt/1.12**, separators 1.16 → 1.12 (W45 ES×FR §5.1
   / ES×EN precedent). Dash style `N. key — note` and `N. ✓ note` unchanged.
2. **P6 exercise flow overflow** (+82px): §A bridge shortened to
   `Guarda i grafici e scegli.` (1 line); exercise gap 3→1 on all 18
   size-19 items (W45 ES×FR §5.2 precedent). §D bridge kept with its
   full word list.
3. **P1 word-note LINEX** (2nd line crossed the y=1844 rule): note
   shortened to one line `«La precampagna»: prima della campagna.`
   (378.7px ≤ 434px; the longer `…della campagna ufficiale.` measures
   453.4px and still wraps to 2 lines).
4. **P5 plan box-title crossing** (ink 1050.2 > border 961.0): title
   shortened to `EL PLAN DEL PUENTE · IL PIANO` (W45 ES×EN §3.5
   precedent; ink now ends ≈917px).
5. **P7 column-3 overflow** (Italian notes pushed the quotes block and
   the preview box over the footer rule; preview was at y=2582.6):
   trimmed exactly 142.5px so col-3 ends at the core's 1820.08 + 2px box
   slack (final 1822.08): palabra note 5→2 lines (campaign-start fact
   preserved in the P5 plan box, P6 timeline and P7 preview),
   disclosure note 5→4 lines (all three disclosure facts kept: no real
   letters, no best P8 texts, example printed + promise to VOL.3 +
   invitation), clinic note #3 2→1 lines (`gente è singolare: verbo al
   singolare.`). Preview now at y=2442.08, bottom 2560.08 (19.9px clear
   of the 2580 footer rule).
6. **P7 palabra box-bottom graze** (ink 1255.1 > border 1254.6 by 0.5px,
   Latin descenders where the core's CJK ink has none): box height +2px
   (W45 ES×FR §5.8 precedent, same 0.5px numbers).

Final full build: **zero FLOW OVERFLOW / zero HEAD TOO WIDE** on all
8 pages.

## 6. Geometric occlusion audit (SOP gate) + companion scans

- `tools/occlusion_audit.py` (selftest passed: all 6 planted classes
  fired, clean controls silent): first run 3 flags (all Italian
  apparatus, §5.3–§5.5), all fixed; **final run 0 flags, --core
  comparison NEW flags = 0** (core control: 0 flags).
- Same-baseline ink scan (FR×RU rowcheck method, <6px threshold): 7
  hits, **identical to the core control run** — the P1 sommaire rows,
  where `Pág. N` and its title sit at a deliberate +4.0px ink gap
  (positive gap, no overlap). No furniture-band collision; no new
  same-baseline defect.
- P6 chart element check: chart-zone rects (10) and texts (24)
  **byte-identical to the core**; the only rect differences on P6 are
  the exercise level chips, shifted by the documented §5.2 gap change
  (flow consequence, not a chart edit). No chart geometry moved.
- **Known frozen-core defect, preserved not repaired (coordinator's
  ruling):** the P6 second chart's `Inmigración` label is pressed ~5px
  by its bar (label ink ends 1144.25, bar starts 1139 → 5.2px overlap).
  This is frozen core geometry, present identically in the shipped
  core; it was deliberately NOT repaired here.
- Gloss counting (split on `·` itself, README #21): core 19 = edition
  19, per box 5/5/5/4, item by item (Spanish headwords identical).
- Images: P3 chestnuts and P5 pumpkin payloads byte-identical to the
  core (same blob lengths and SHA-256 prefixes); P1 houses illustration
  is the core's code-drawn `illus_houses()` (code untouched); credit
  lines unchanged (Spanish apparatus of the frozen core).

## 7. Deliverables (`files/weekly-report-w45-es-it/`)

- `svg/` ×8, `cards/` ×8 (1950×2700 PNG, all verified)
- Print PDF: `La-Lucerna-VOL2-IT.pdf` — **6,024,328 bytes** (D5 rebuild, 2026-11-14; old 7,156,450 bytes expired),
  sha256 `c7680fdab56565331fbf7db53c85fce560b4a7116c89ac82688b93e0a81323d7`, 8 pages
- Web PDF: `La-Lucerna-VOL2-IT-web.pdf` — **569,716 bytes** (< 10 MB; D5 rebuild, 2026-11-14; old 3,713,123 bytes expired),
  sha256 `f4650b23b515c2c3a4f19906cf4adfc4999062ce8fe59b85fb4602936b2ef774`, 8 pages
- `WEEKLY-KIT.md` (this file), `ABSTRACT.txt` (Italian, one line, no
  ASCII double quotes)

## 8. SVG hashes (delivered edition + core baseline)

Delivered edition:
- p1 `8bd10a688f89eadde80d7dc627fed647d134afb922cc0aee1a504cdf1bdcb32a`
- p2 `13a36d63a279539b24c4023b8d31360164e37db9d5dcadb78353d71087e4337c`
- p3 `8a11f133d35d943e2c6da817220ddde271e8431eddd3393f8c6617e5af383a38`
- p4 `7fa9a5bf61e489cd78fbd352eb90402721b1a18c9d0e706a5ef935da7c9b907b`
- p5 `b15850d56e8ef9c3fa4952a8664e1b1d82a84ee02abc6b298eb39a795f6b4e4a`
- p6 `f3497016b5b3922d673fcef4b46eadeb78a116e27cfcc0087352cd6066917dc3`
- p7 `a8d9a79e0b6ffb2fae7cab47067dc8f987b1193f898b1f4f24649b09e5db9cf7`
- p8 `3e94219a67299ec0c7629595bf5b4f195ad17340d74235dfa49a92359b312b92`

Core baseline (re-hashed after the final build, unchanged):
- p1 `a1b3010296ad129e45d2816637762cec4f25635ff43ea2197e08e0efd0daf34d`
- p2 `10e78c2e6cb295198cce99ed6182cf2472511da267ddeb9bf4379d464f0bb724`
- p3 `5986ba9e318c985e14d33abb6e9277f22bf7c0c6a961f94501cdfa46b655aa8b`
- p4 `1894836e06be824b1dc3a3ac46474ccced7495679f23aabc0f27808c63617a67`
- p5 `cd15c68b5f8db752b6bc62346dd22826d19513d41fab16f2a2f7c119a3893fd2`
- p6 `fcfccf8267e10cc7ddbf14d5aa9dd735cf1c73a110f4fe8ec38d8e9aef07b280`
- p7 `b1774024b6a17353d18a7b9b13f4be14ce8a6a4ca1b8f2565e06fafb0a90a8fe`
- p8 `d1c46fa439ac505db6e2708df8206f10d7046947064172dfcde22e74d7545147`

Audit records: `hidden_files/w45-es-it-diff.json` (freeze diff),
`hidden_files/w45-es-it-occlusion.json` (final 0-flag audit),
`hidden_files/w45-es-it-transform.py` (asserted transform, from-scratch
verified), `hidden_files/w45-es-it-rowcheck.py` (same-baseline scan),
`hidden_files/w45-es-it-cjk.txt` (core Chinese-string inventory).

## 9. Open gate

**Independent proofread has NOT run — marked PENDING.** No GitHub repo
insert and no Discord post were made (parent handles both after the
proofread passes). No final-edition claim is made here.

## D5 rebuild (2026-11-14)

D5 + §1.1 merged rebuild of the W45 ES × IT edition (D5 font scope B).
Builder: scratch `hidden_files/d5-redo/scratch-2026-w45-es/`, family report
`hidden_files/d5-redo/FAMILY-W45-ES-BUILD.md`. KIT custody: this KIT was updated
in the builder scratch (`patched/2026-w45-es-it/WEEKLY-KIT.md`); the closer syncs
it into production with the rebuilt sources (for zh-cn, into
`production/2026-w45/core-es/WEEKLY-KIT.md`, byte-identical).

- Install: `apply_variant.py --patch-core es --week 2026-w45` (core-es svglib
  landed in production, `_D5_READER = "latin"`); this edition `--check` dry-run
  passed, `_D5_READER = "latin"` (svglib.py L100); `test_d5_routing.py`
  FAILURES: 0; fix2 retained (U+201C 1 hit, `_QUOTE_CLS` 4 hits).
  Pre-D5 census (baseline): 493 (lat 493 / cyr 0 / curly-in-CJK 0) — all > 0, as required for a D5 rebuild.
- Step-7 fixes (font sizes only; no wording changed):
  - `content12.py:26`: P1 headline “¡LA VIVIENDA DECIDE LA CAMPAÑA!” 46 -> 38.5 (run1 TEXTX overlap 130.9px; run2 margin 17.9px)
  - `content12.py:49`: f.box title “LA SEMANA EN CIFRAS　IN CIFRE” tsize 23 -> 21.5 (run1 over +17.5px; run2 margin 10.3px)
  - `content12.py:92`: P1 contents box title “EN ESTA EDICIÓN　IL NUMERO” 24 -> 23 (run1 over +3.7px; run2 margin 13.1px)
  - `content12.py:185`: f.box title “EL CALENDARIO　IL CALENDARIO” tsize 23 -> 21 (run1 over +23.4px; run2 margin 13.8px)
  - `content34.py:127`: P4 box title “EL CLÁSICO, UNA SEMANA DESPUÉS” 23 -> 19.5 (run1 over +51.5px, was +2.5px; run2 margin 17.3px)
  - `content7.py:79`: P7 clinic box title “ERRORES TÍPICOS　ERRORI TIPICI” 23 -> 21 (run1 over +26.7px; run2 margin 10.5px)
- Gates (run2b, full re-run after fixes): G1 TOTAL 150, 0 warnings; G2 head_check 0;
  G3 d5 census Latin 0 / Cyrillic 0 / curly-in-CJK 0 (ru: Noto Sans elements 787);
  G4 render rc=0; G5 webpdf rc=0, web PDF < 7 MB; G6 occlusion 0 flags; G7 p8 extract
  150/150; G8 p8 compare CLEAN, keydiff [137, 138]; G9 freeze baseline 8/8;
  G10 freeze diff vs base: added CJK 1 (P6 U+3000 run split, located in all 11
  editions — the known es-family case, accepted per task instruction; added Latin
  strings are reflow re-splits, token multiset unchanged);
  G11 spill 2 SPILL (frozen-core, identical lines/positions in the shipped baseline —
  P1 last list item +10.4px and P7 letters line +12.0px below their box bottoms;
  not D5-caused, carried for reproof adjudication);
  G12 boxtitle 0 DEFECT; G13 edge 0 TOUCH 0 NEAR; G14 creambox PASS 0 defects;
  G15a text layer print=web=issued diff 0, native verifier ADOPT (0 UNEXPECTED);
  G16 census_quotes 0 defective; G17 N/A (no family gates.py for es);
  D18 masthead SVG gap 19.8px PASS; D37 submasthead PASS, margin 106.4px (y=614).
- P8: lines 249 -> 249 (run1 -> run2, unchanged), slack_footer 46.7px
  (footer line y=2596, page bottom 2700 — positive margin, no overflow).
- New deliverables (builder run2b originals; the closer MUST copy these files,
  never re-run webpdf — web PDF bytes are not reproducible across runs):
  - Print PDF `La-Lucerna-VOL2-es-it.pdf`: 6,024,328 B, SHA-256 `c7680fdab56565331fbf7db53c85fce560b4a7116c89ac82688b93e0a81323d7`
  - Web PDF `2026-w45-es-it.web.pdf`: 569,716 B, SHA-256 `f4650b23b515c2c3a4f19906cf4adfc4999062ce8fe59b85fb4602936b2ef774`
  - text.md `2026-w45-es-it.text.md` (exporter `textexp_es.py`, D16-fixed;
    native verifier ADOPT; exercise sequence + per-page token multiset equal to shipped)
- Old pins: the pre-D5 print/web values elsewhere in this KIT are expired (see the
  notes on the updated pin rows above). Edition SVG hash tables, cards tables and
  historical fix-round records were NOT updated (out of scope for D5; the D5 report
  notes where they went stale).
- Logs / report: `scratch-2026-w45-es/logs/2026-w45-es-it/GATES-SUMMARY-run2b.txt`;
  D5 report `production/notes/2026-w45/g-es/scratch-d5-rebuild-es/D5-REPORT-2026-w45-es-it.md`.
