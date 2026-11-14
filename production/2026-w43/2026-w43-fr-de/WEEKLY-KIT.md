# Le Lucerna — VOL.2 · FR × DE EDITION (French text · German explanations)

The German-explanations edition of VOL.2 « Spätherbst & Feste » (week of
19–25 October 2026, 8 pages). Same French core as the delivered first edition
(`files/weekly-report-vol4/`), same 145 exercises — only the explanation
apparatus is rewritten, in German, for German-speaking readers. Built after
the SOP (`files/weekly-report-SOP.md`) and its closing addendum, mirroring the
FR × EN sibling edition's method.

## HOW THIS EDITION WAS MADE

- Build sources copied from the CORE build (`hidden_files/weekly-report-vol4-build/`)
  to `hidden_files/weekly-report-fr-de-build/`; the core's dirs were never modified.
- Baseline first: the unmodified copy, rebuilt in scratch, reproduces all 8 shipped
  core SVGs **byte-identical** — the toolchain and fonts are proven before any edit.
- Every apparatus string was then rewritten in German (glosses, grammar notes,
  instructions, explainers, clinic notes, the readers'-corner comment, chart notes,
  and all P8 answer notes). French content — articles, stems, options, quoted
  examples, taught text, the French halves of dual-language titles, content
  letters — is untouched.
- One-to-one pairing: French text + explanations written directly in German.
  No intermediary language anywhere in the chain.

## SPECIFICATIONS (measured on the shipped files)

- Page: 1950 × 2700 px cards · paper ivory `#f7f2e3` · DejaVu Serif / Sans.
- Total visible characters: **46,370** (core: 40,645 · FR × EN: 45,752).
  (Was 46,415 as built; −45 after the independent-proofread P7 fix — see the
  proofread record at the end of this file.)
- PDFs: print `Le-Lucerna-VOL2-DE.pdf` 9,783,030 B · web `Le-Lucerna-VOL2-DE-web.pdf`
  **7,278,643 B < 10 MB** (Discord-safe).
- D5 重建（2026-11-13，见文末 D5 节）：印 `The-Lucerna-VOL1-fr-de.pdf` **8,684,191 字节**（SHA-256 `d35301927a619f5870ae1125c1793776c9ac2060b9963739c1579608c78c8252`）；网 `2026-w43-fr-de.web.pdf` **1,708,945 字节**（SHA-256 `9b87e27cc8d45b1ae2ecfb57523cfca344f116030f7a418537554d230a5ec63c`，< 7 MB）；text.md 与已发版 12-line gloss-leak diff（SHA-256 `d9daf60ed041666657b2e51a3ac0dfdfd75c0d4c576bfcd88c7e978575851ac0`）。D5 前值：印 9,782,922 B（KIT "Final sizes"，L241；L30 的 9,783,030 B 为校对修复前值）（KIT 未记 SHA）、网 1,749,852 字节（`86fe6bec…`，issues 已发版）。

- Images (public domain, unchanged from the core; credits unchanged): P1 Hiroshige
  maple (LACMA) · P2 Atget Paris street · P3 Blanco chrysanthemum plate.

## PAIRING BADGE (as printed)

- P1, under the countdown band, brick red, bold, centered:
  **„FRANZÖSISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER"**
- Every page footer: „Le Lucerna · FRANZÖSISCHE WOCHENZEITUNG VOL.2 · TEXT AUF
  FRANZÖSISCH · ERKLÄRUNGEN AUF DEUTSCH" (left) · „Seite N von 8" (right).
- Masthead stays **Le Lucerna**; dual-language furniture throughout, e.g.
  „HEBDOMADAIRE EN FRANÇAIS · JEDE WOCHE · FRANZÖSISCH, WIE FRANKREICH ES LIEST",
  „À VOUS ! · SIE SIND DRAN", „EXERCICES & RÉPONSES · ÜBUNGEN & ANTWORTEN",
  section gloss prefix „HINWEIS · ", P8 group headers „— SEITE n —".

## EXERCISES

- **145** — registry re-derived from this build and field-diffed against the core
  registry: identical count, identical per-page distribution
  (10 · 16 · 18 · 18 · 17 · 18 · 11 · 37), identical levels
  (A2 55 · B1 65 · B2 25); key fields differ only for the re-aimed items below
  and the three model-answer labels on #71–73 (the core keys carried a Chinese
  „（参考答案）" suffix; here „(Musterantwort)" — the French model answers are
  byte-identical).
- Instruction words in German: Ausfüllen · Umformen · Zuordnen · Korrigieren.
- Answer-key typography: a space before each note parenthesis everywhere on P8
  (the core's full-width parentheses are gone; zero full-width parens in the keys).
- Printed-note set: the P8 code carries an explicit set of the 67 exercises whose
  notes print — recomputed from the core registry, it is exactly the set the
  core's own rule produced (page 8 always, or note ≤ 10 chars, or error-clinic /
  chart-reading types). Every exercise that had a note in the core has its German
  note here; none gained, none lost.

## TRANSLATION ITEMS RE-AIMED AT THE READER'S LANGUAGE (the only key changes)

- **#132** — direction flips to French → German. Stem: „Übersetzen Sie ins
  Deutsche: « Lire un sondage, c'est déjà faire de la politique. »" Key:
  „Eine Umfrage zu lesen ist schon eine Form politischer Beteiligung."
  Note: „lire un sondage = eine Umfrage lesen".
- **#133** — stem now German: „Übersetzen Sie ins Französische: Er ist größer
  als sein Bruder." Key unchanged: „Il est plus grand que son frère."
  Note: „Komparativ: plus grand que".
- **#134** — stem: „Übersetzen Sie ins Französische: Die Schüler haben seit
  Samstag Ferien." Key unchanged: „Les élèves sont en vacances depuis samedi."
- **#135** — stem: „Übersetzen Sie ins Französische: Heute Abend stellen wir
  die Uhren um eine Stunde zurück." Key unchanged: „Ce soir, nous allons
  reculer les horloges d'une heure."
- **#145** (writing, registry key) — „Offene Aufgabe — Punkte im Schreibrahmen;
  Mustertext im MODÈLE-Kasten auf dieser Seite", note „Bewertung nach den Punkten".

## PROOFREAD RECORD (this edition, full pass)

- **Source-level string audit** (the build is deterministic; the baseline is
  byte-proven): every string literal removed from the core sources contains
  Chinese or is build plumbing (output path, the key-printing rule fragments);
  every string added is German apparatus, a bilingual head, an instruction word,
  or a re-aimed item above. No French string was removed or altered anywhere —
  **the French layer is frozen**, confirmed independently at SVG level:
  all French-bearing nodes match the core modulo apparatus-driven reflow.
- **CJK scan of the final SVGs: 0 Han characters on all 8 pages** (text nodes;
  the only CJK left anywhere is in build-source comments and the registry's
  internal type names, which never print — identical to the core, kept so the
  registry stays field-comparable).
- **Re-solved 34 exercises** against their printed German keys/notes (clocks
  #11–15 incl. „halb drei / Viertel nach / Viertel vor"; matching #22; Toussaint
  #28/#33; chart #80–85; phrases #98–104; clinic #105–108; cloze #109–116;
  reading #124–127; translations #132–135; dialogue #141/#144): all agree.
- **P7 phrases**: the 7 taught sentences are the core's frozen French strings
  with their (page N) tags; occurrence counts across the paper are identical to
  the core's (2 · 3 · 2 · 1 · 1 · 2 · 1 — the core's own distribution, inherited
  unchanged with the frozen text).
- **Facts/dates identical** to the core; spot-verified against the calendar:
  1 Nov 2026 is a Sunday (#109), 24 Oct 2026 is a Saturday (#138).
- **P8 keys flow**: lowest key baseline = **2539.2**, i.e. **40.8 px above the
  footer rule (2580)** — the same geometry as the core itself; keys' ink band
  bottom (2545) clears the rule.
- Build log: zero FLOW OVERFLOW; the only warning is the core's inherited
  P4 „REGARDER UN MATCH EN FRANÇAIS" head (see adjudications).

## GEOMETRIC OCCLUSION AUDIT RECORD (SOP addendum + thin-line supplement, mandatory gate)

Method: paint-order audit over the shipped SVG element stream, ink bands =
baseline −0.88 em … +0.30 em, widths from the production font metric; checks =
(a) later opaque shape (fill opacity ≥ 0.85, images included) covering ≥ 30 % of
a text ink band, (b) text ink intruding into the footer band (below the y = 2580
rule), (c) text ink past a page edge, (d) any later-drawn line (rect ≤ 3 px or
line element, thin lines included) crossing a text ink band. All 8 pages.

- Result: **16 flags, all one benign class** — the two footer texts themselves
  (baseline 2624, below the rule by design). The identical audit run on the core
  and on FR × EN produces the identical 16-flag profile.
- **Zero** coverage flags, **zero** line-crossing flags, **zero** edge spills,
  **zero** content intrusions into the footer band. No unresolved flags.
- All 8 card PNGs additionally viewed page by page: no covered, clipped, or
  struck-through text anywhere.

## LAYOUT DECISIONS TAKEN IN THIS EDITION (German runs long)

- P1 gloss tightened („…présidentielle Präsidentenwahl…", 4 wrapped lines) and
  the EN CHIFFRES row-2 note shortened to „(Sieg in Runde 1)" so the numbers box
  stays in column 2 exactly as in the core — the headline flow ends at
  col 2 · y = 1583, the core's own end position; no overflow.
- Three bilingual heads shortened to fit the 434 px column (the head check is
  the build's own): P6 „LIRE LE GRAPHIQUE · GRAFIK", P7 „CLINIQUE DES ERREURS ·
  KLINIK", P8 battery B „B · CHOIX MULTIPLE · ANKREUZEN". The German halves of
  the corresponding section titles remain fully present in the band/sub lines.
- P2 ET VOUS note kept to two wrapped lines („Gibt es bei Ihnen Zeitumstellung?
  Zwei Sätze Französisch an die Redaktion.") — the box geometry is the core's.

## ADJUDICATIONS KEPT FROM THE CORE (unchanged)

- P4 head „REGARDER UN MATCH EN FRANÇAIS" is set in italic serif and overflows
  its 434 px column by design of the core (the build's HEAD TOO WIDE note also
  fires on the core and on FR × EN). French head — kept.
- The registry's internal type names stay as the core's (metadata only, never
  printed) — required for the field-exact registry diff above.
- bslib's internal layout helpers are inherited untouched except the footer
  line and the gloss prefix; the note-line helper's inherited internal name is
  code-only, never printed, and identical in the core and every sibling.
- No occurrence of the banned intermediary term in the paper or this kit, in
  any language; the explanation layer is described only as what it is:
  French text + German explanations, one-to-one.

## VOL.3 PROMISES CARRIED OVER (printed in this edition, owed by VOL.3)

- Next issue covers **31 Oct Halloween, 1 Nov Toussaint, and the first week of
  winter time** (P7 teaser, in German).
- The readers' corner will comment on readers' VOL.2 compositions — topic on
  P8 („Mes vacances de la Toussaint", German instruction printed alongside);
  P7's German comment repeats the invitation.
- The sports page collects „Mein erstes Spiel mit französischem Kommentar"
  (P4, German call printed in the LE SAVIEZ-VOUS ? box).

## REPRODUCE

```bash
cd hidden_files/weekly-report-fr-de-build
/tmp/wp-venv/bin/python -c "import content12, content34, content56, content7, content8"
# -> svg/ in files/weekly-report-fr-de/svg/
# cards: cairosvg.svg2png(output_width=1950, output_height=2700)
# print PDF: cairosvg.svg2pdf per page + pypdf merge
# web PDF: card PNGs saved as one PDF, JPEG quality 85 (PIL)
```

## INDEPENDENT PROOFREAD RECORD (fresh pass, 2026-10-21) — FINAL AFTER 1 FIX

Reviewer: independent proofreader (not the builder). Method: own extraction,
own registry dump, own geometric audit (PIL metrics, SC face), own rebuilds —
nothing taken from the builder's claims without re-measurement.

**Verified clean (all re-measured independently):**
- Reproducibility: scratch rebuilds of BOTH builds regenerate all 16 shipped
  SVGs byte-identical → the source diff is a faithful proxy for the render diff.
- Core integrity: bslib4 diff = footer/badge/gloss-prefix strings only. Registry
  field-diff (145 × 6 fields): identical pages (10/16/18/18/17/18/11/37), levels
  (A2 55 · B1 65 · B2 25), types; key diffs ONLY the documented set (#71–73 label
  „z. B.:" + „(Musterantwort)", French model answers byte-identical; #132 German
  key; #145 German key). #133–135 French keys byte-identical; stems re-aimed as
  documented. No French string altered anywhere.
- Explanation language: CJK/full-width-paren scan = **0 nodes on all 8 pages**.
  All five content diffs read in full as a German speaker: glosses, grammar,
  clinic, readers' corner, chart notes and every printed P8 note grammatical,
  idiomatic, accurate. Printed-note set recomputed from the core registry with
  the CORE's own printing rule = **67**, identical to this build's PRINT_NOTES.
  23 registry notes byte-identical to the core — all French formulas (e.g.
  „28 % = vingt-huit pour cent"), correct in both editions, not a defect.
  Registry `type` fields stay Chinese internally (never print) — documented,
  accepted.
- Re-solved 60+ exercises against articles/keys/notes across all 8 pages
  (headline quiz, clocks #11–15 + table, matching #23–26/#50–53/#136–139,
  V/F #27–31, chart #80–85 arithmetic 28−24=4 · 17≠2×11 · B 27/A 26 · 52 %,
  phrases #98–104, clinic #105–108, cloze #109–116, reading #124–127,
  transformations #128–131, translations #132–135, dialogue #140–144): all agree.
- P7 phrases: sentence+tag sequence identical to the core; occurrence profile
  across the paper 2·3·2·1·1·2·1 in BOTH editions (exact match).
- Dates (verified with `date`, Europe/Paris): 1 Nov 2026 = Sunday (#109 ✓),
  24 Oct 2026 = Saturday (#140 ✓), 31 Oct = Saturday (teaser ✓), 25 Oct = Sunday,
  school resumes Mon 2 Nov ✓. P3 dates box weekdays all correct.
- Badge: P1 pairing line present in render (brick, under the band); footers on
  all 8 pages carry the pairing string + „Seite N von 8".
- Images/credits: asset md5s byte-identical to the core; credit lines identical
  (Hiroshige/LACMA, Atget, Blanco).
- Geometric audit (own script, SOP addendum + thin-line supplement): the ONLY
  flags are the 16 footer-self nodes (2 footer texts × 8 pages, baseline 2624,
  below their own 2580 rule by design) — the builder's classification CONFIRMED,
  not assumed. Zero coverage, zero line-crossings, zero edge overflows.
  P8 lowest key baseline = **2539.19** (builder claimed 2539.2 ✓); per column
  2539.19 / 2511.77 / 2527.57 / 2157.6 — all ≥ 40 px clear of the rule.
  P4 „REGARDER UN MATCH EN FRANÇAIS" head: inherited core geometry, crosses no
  text, no page edge — core adjudication stands.
- VOL.3 promises all carried in German (P7 teaser, readers'-corner follow-up,
  sports-page collection line).

**Problem found in pass 1 (1) — FIXED:**
- P7: phrase 7's page tag „(page 1)" was orphaned at the top of column 4,
  separated from « On gagne une heure de sommeil. » (bottom of column 3) by the
  column break — the core keeps them together. Cause: two German grammar notes
  (phrases 5/6) wrap to 2 lines where the core's Chinese wraps shorter.
  Fix (fr-de build only, content7.py display points; registry untouched):
  „Grammatik · attendre ohne Präposition." and
  „Grammatik · si + Imparfait → Konditional." — each now one line; the full
  explanations remain in the P8 notes (#102/#106, #103). Visible chars
  46,415 → 46,370.

**Pass 2 (complete, on the rebuilt artifacts): ZERO problems.**
Rebuild blast radius verified: SVGs/cards for pages 1–6 and 8 byte-identical to
the pre-fix shipped set; only p7-langue.svg and its card changed, and within P7
only the two notes + the resulting reflow (tag now directly under its sentence
in column 3, as in the core). Registry re-derived from the fixed build:
field-identical to the pre-fix registry (145 × 6, zero diffs). Audit re-run:
16 footer-self flags only. CJK re-scan: 0. Final sizes: print PDF 9,782,922 B ·
web PDF 7,274,783 B (< 10 MB Discord limit).

**Verdict: FINAL — passes the SOP gate (one complete independent pass with
zero problems). Not posted to Discord (per instructions).**

## D5 REBUILD RECORD (2026-11-13)

SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader（SemiBold）。
施工不 commit、不 push；入仓由独立重校后的 closer 做。工作日志：
`hidden_files/d5-redo/scratch-2026-w43-fr/logs/2026-w43-fr-de/`；
逐版报告：`production/notes/2026-w43/g-fr/scratch-d5-rebuild-fr/D5-REPORT-2026-w43-fr-de.md`。

**装机**：core 落盘 `apply_variant.py --patch-core fr --week 2026-w43`（core-fr
`svglib.py` +95/−3 行，`_D5_READER = "latin"`）；本版 `--svglib patched/…/svglib.py
--target fr --reader de --week 2026-w43`，装后 `_D5_READER = "latin"`；路由单元测试 FAILURES: 0；fix2 块保留。
D1 组装先于安装：patched svglib 取本地 fanout D1 版，组装后与生产版 svglib 的 diff 恰为 D1 hunk 一处（28 行）。

**基线**（修前生产版）：run TOTAL 145，0 警告；印 PDF 与 `d1-fix/work/2026-w43-fr-de/RESULT.txt`
的 shipped SHA/字节逐字节一致；印/网文字层差 0；自建网 vs issues 已发 web 非空字符差 0（仅空格差）；
修前普查 D5 拉丁 554、西里尔 0、弯引号在 CJK 2；基线 P8 noted 67/145。

**缺陷与修法**（run1 → run2 → run3；修法只动字号、盒高与间距，未动文字）：
head 11 项（共用 5 + outils 27→26、clinic 25→23、battery A 24→22、B 24→21、E 24→22、G 24→21）；箱标题 6 处（COMMENTATEUR 20、TROIS DATES 21、scrutin 21、fêtes 22、zoom 22、écrans 21）；spill ×2；run2 P2 LINEX → run3 消除。

P8：198→199 行，距页脚线余量 33.7→32.7 px。

**门禁 run3（全套 16 门 ALL-GREEN）**：run TOTAL 145、0 警告；head_check 0；
d5 census 0/0/0；render RC=0；webpdf RC=0（1,708,945 B < 7 MB）；occlusion 0 flags；
p8 extract noted 67/145；p8 compare **CLEAN**（keydiff=[71, 72, 73, 132, 145]）；freeze baseline 8/8；
freeze diff 新增 CJK 字符 0；spill 0；boxtitle 0 DEFECT（40 titles）；
edge 0/0；creambox PASS 0 defects；文字层 print=web 差 0（各 105,859 字符）；census_quotes
0 defective；fr 家无 gates.py。

**新交付物**：印 `The-Lucerna-VOL1-fr-de.pdf` 8,684,191 字节（`d3530192…`）；
网 `2026-w43-fr-de.web.pdf` 1,708,945 字节（`9b87e27c…`）；text.md 12-line gloss-leak diff
（`d9daf60e…`）。练习仍为 145 题。
