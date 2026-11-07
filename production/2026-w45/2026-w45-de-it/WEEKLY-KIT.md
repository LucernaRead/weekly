# WEEKLY-KIT — Die Lucerna · W45 DE×IT (VOL.2)

Issue week: **Mon 2 – Sun 8 November 2026**. Issue dated **Mon 2 November 2026**.
Edition: **German text × Italian explanations** (target DE, native IT).
Status: **builder-complete, NOT finalized — awaiting independent proofread.**
No Discord post, no card/PDF dump into main chat, no cron, no weekly-git
touch, no edit to the core or W43 directories — this build only.

## 1. Spec

- 8 pages, 1950×2700, warm ivory paper, dark olive-green accents,
  blackletter masthead **Die Lucerna** (core's masthead; target is German).
- Only the explanation layer was rewritten, directly into Italian for
  Italian-native readers. All German body text is frozen, word for word.
  No invented reader letters, names, or quotations: the P7 readers' box
  keeps the core's German example letter, labelled as an editors' example.
- The explanation layer contains no “桥接” wording anywhere (SVG CJK = 0,
  see §2); the layer is called 讲解 in the brief only — in the edition it
  is Italian notes (prefix `Nota — `).
- 150 exercises, continuously numbered 1–150; levels A2 66 · B1 70 ·
  B2 14 (B2 is light, as in the core — honestly recorded, no re-labelling).
  Per page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38.
  By type (Italian names): scelta multipla 52 · completare 41 ·
  abbinamento 12 · trasformazione 11 · vero/falso 8 · costruire frasi 8 ·
  testo a buchi 8 · completare il dialogo 5 · traduzione 4 · scrittura 1.

## 2. Freeze check (tools/freeze.py)

- Baseline first, before any edit: `freeze.py baseline` on the W45 DE core
  build reproduced **8/8 SVGs byte-identical**, and the shipped core SVGs
  re-hashed unchanged afterwards.
- Core hashes before = after (sha256, first 16 hex):
  p1 6cbd48022b5f863d · p2 9362256dca74f877 · p3 3e8a8d16136a46a3 ·
  p4 b787f592599cc4d1 · p5 4dcbeb97c566f4df · p6 01b75ad49a54c803 ·
  p7 fbaf8cdd8a90f299 · p8 299524bd2ad25ec4 — all MATCH after the build.
- `freeze.py diff` core vs this edition (final render):
  p1 +23/−23 · p2 +36/−32 · p3 +41/−40 · p4 +26/−22 · p5 +44/−39 ·
  p6 +37/−33 · p7 +58/−53 · p8 +157/−141 strings;
  **added CJK characters = 0 on every page; edition SVG CJK total = 0.**
- Adjudication of the diff, page by page:
  - P1–P2, P5: every removed string contains Chinese or is a bilingual
    furniture/mixed element; every added string is its Italian
    counterpart. No German body line differs.
  - P3, P4, P6: the only removed strings without CJK are a lone `。`
    (the Chinese full stop that ended a core gloss line; the Italian
    gloss ends with `.` attached to its last word) — punctuation only.
  - P7: removed non-CJK strings are (a) the label
    `Ein Beispiel der Redaktion!` → Italian `Un esempio della redazione!`
    (explanation-layer label, same precedent as DE×EN/DE×FR);
    (b) a wrap fragment of the NOCH EIN WORT line, whose German words are
    intact across fragments — only the parenthesis form changes
    `（Seite 2）` → `(Seite 2)`, the W43 DE×IT family precedent;
    (c) a `……` wrap fragment of a core toolbox item (no Italian
    counterpart fragment). German quotes do not appear in the diff at
    all: they are byte-identical.
  - P8: removed non-CJK strings are only bracket-form fragments of key
    lines (core full-width `（）` → this family's half-width `()`,
    see §4); German key text itself is intact in the added lines.
  - P1 headline flow ends at y=1555, exactly the core's value
    (see §8, first fix).
- New explanation-language characters added, beyond Italian/Latin and
  the frozen German text: none to declare — the edition adds only
  Italian text in the Latin script (plus the frozen German `ß`, `ä/ö/ü`
  and the `ª` in `9ª giornata`, which is Latin-1). No CJK, no other script.

## 3. Furniture — three-way对照 (this edition / W43 shipped DE×IT / README §20)

W43 shipped DE×IT SVG wins verbatim wherever it speaks; the DE family
case in README §20 applies (EN/DE/ES cores have a native subtitle slot
at y≈372 → the badge replaces it in place). Measured from the shipped
W43 SVG, copied exactly:

- P1 badge element, byte-identical to W43 shipped:
  `<text x="975" y="372" font-family="Noto Sans CJK SC" font-size="20"
  font-weight="700" fill="#a4553a" text-anchor="middle">TESTI IN TEDESCO ·
  SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI</text>`
  (slot y=372, 20pt, bold, BRICK #a4553a, centred). String also matches
  `tables.py furniture it --target de --vol 2` exactly.
- Masthead: core's **Die Lucerna** (target-language article; German).
- Footer, every page: `Die Lucerna · SETTIMANALE TEDESCO VOL.2 ·
  TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO` + `Pagina N di 8`
  (verified present on all 8 SVGs; VOL.2 follows the W45 core).
- Gloss prefix: `Nota — ` (W43 shipped form).
- P8 separators: `— PAGINA N —` (W43 shipped form), 17pt bold olive.
- P8 keys: half-width parens ` (note)`, 13pt, leading 1.26 — the W43
  DE×IT build-code form (not the core's full-width 14.5pt/1.3 form;
  README §14: bracket form follows the family's shipped fan-out code).
- No furniture string was generalised to fit README §20, and no frozen
  German line was moved or deleted to accommodate a badge: the badge
  occupies the core's own subtitle slot, as in W43.

## 4. P8 verification (tools/p8.py)

- `p8.py compare` (explicit core/edition P8 paths; the `--core-dir`
  form mis-resolves the P8 filename for this pairing and was not used):
  **CLEAN 150=150**, missing=[], extra_count=0, uncertain=[].
- keydiff = **[137, 138, 139, 150]**, adjudicated item by item:
  - 137, 138, 139 — E-section DE→IT translation items: keys legitimately
    re-aim from Chinese to Italian (137 `Lo sconto sul carburante dura
    fino a dicembre.`; 138 `Guardo il calcio di martedì.`; 139 `La scuola
    è ricominciata.`). Translation items re-aim by definition.
  - 150 — writing item: the prompt/note language changes from Chinese
    to Italian (`Domanda aperta — segui i punti del riquadro di
    scrittura; il testo modello è nel riquadro di questa pagina` /
    `Si valuta secondo i punti indicati`); it is not a German key.
  - 140 — the REVERSE item — is NOT in the keydiff: its key stays
    German in both editions (`Am Sonntag schlafe ich eine Stunde
    länger.`), with only the prompt re-aimed to Italian
    (`Domenica dormo un'ora in più.`, instr `Traduci in tedesco`).
    Reverse-key verified.
  - No keydiff is a tool artifact: the bracket change is the family's
    half-width form (§3), and the dash/parenthesis extraction classes in
    README §13–§14 were checked against the registry — the four diffs
    above are all genuine, legal re-aims.

## 5. Occlusion audit (tools/occlusion_audit.py)

- Selftest first: all 6 planted classes fired exactly once; clean
  controls silent.
- Final: **edition 0 flags · core 0 flags · NEW vs core 0.**
- P6 chart (README §12 blind-spot check, done by hand regardless of
  flags): chart-label ink vs later-drawn bar rects = 0 overlaps.
  Labels at MX+360, bars at MX+470: `in famiglia` ink right 522.3
  (clear 12.7px) · `servizio` 496.8 (clear 38.2px) · `in istituto` 513.7
  (clear 21.3px). The ÜBUNGSDATEN line fits the full width (1759px
  of 1820px) after shortening its Italian parenthetical (§8).
- Same-baseline scan (README §10, furniture bands): the P1 sommaire
  row `Ferienwechsel & Herbst` vs `A2→B1` — CORRECTION (coordinator
  KIT-only edit 2026-10-27, JA precedent; paper untouched): the
  "4.6px advance-width overlap" claimed here did NOT reproduce under
  independent proof. Re-measured with the correct fonts (Serif title
  + Sans Bold label), title ink right edge 1755.0, label ink left
  edge 1799.7, ink clearance 44.7px, advance clearance 44.9px,
  identical in core, DE×EN and this edition; P1 same-baseline
  overlaps 0. The 4.6px figure came from a wrong-font measurement
  (Sans measured 58.3px clearance); actual geometry is cleaner than
  claimed, no defect in the shipped SVG. All other pages: no
  same-baseline overlaps.

## 6. Gloss count (split on `·` itself, README §21)

- `gloss()` calls, core vs this edition, counted by splitting the call
  string on `·` (not on ` · `):
  P2 5 · P3 5 · P4 5 · P5 5 · P6 5 = **25 = 25, item by item, no
  addition, deletion, or merger.**
- P1 bridge line: 4 = 4 items (Englische Woche / Spieltag / empfangen /
  Bundesliga), rendered as `Note — …` with `=` glosses.
- Gloss style follows W43 DE×IT: `German term = Italian gloss`,
  items separated by ` · `, ending with `.`.

## 7. P7 golden sentences (VERBATIM)

- All 8 German quotes occur **exactly 2×** in the rendered issue text
  in both the core and this edition (article + P7), verified by
  substring count over reconstructed SVG text:
  Vier Nächte Fußball… · Energiesteuer…14,04 Cent… · Wer 50 Liter
  tankt… · Die Schule hat nach den Herbstferien… · Die Tage sind
  kurz… · Zwei schwere Auswärtsspiele… · Die deutsche Wirtschaft
  kommt langsam… · Es geht langsam aufwärts… — each 2×.
- Page tags, identical in core and this edition, in P7 order:
  Seite 4 · B1, Seite 2 · A2, Seite 2 · A2, Seite 5 · B1, Seite 3 · A2,
  Seite 4 · B1, Seite 6 · B2, Seite 6 · B2 — each tag matches the
  article page where its quote was found (verified per quote).
- P7 col-3 rail ends at 1504.5 (toolbox + readers + word box), exactly
  the DE×EN value, clear of the phrases rule at y=1508.

## 8. Readers' corner (mandatory items) + self-fix list

P7 LESERBRIEFE box contains, in Italian, all three facts plus an
explicit public invitation — the teaser box at the foot of P7
(`IN DER NÄCHSTEN AUSGABE`) is NOT counted as the invitation, and
neither is any “your letter” line in the contents preview or any
exercise-submission prompt elsewhere:

- Label (editors' example, Italian): `Un esempio della redazione!`
- Frozen German lines (unchanged): deferral
  `Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in
  VOL.3.`, the example letter itself, and the German invitation.
- Italian note, verbatim: `Nessuna lettera vera, nessun miglior testo
  di pagina 8; tutto rinviato a VOL.3.`
  (= no real letters arrived; no best page-8 writing arrived; the
  promise is deferred to VOL.3; together with the label this states
  that the letter shown is an editors' example, not a real letter.)
- Italian invitation, verbatim (explicit, public, in Italian):
  `Scriveteci! Mandateci lettere vere e testi di pagina 8: i migliori
  in VOL.3.`
- No real letter, no real name, and no invented quotation was created
  anywhere in this edition.

Self-fixes made inside this build round (wording only, geometry kept):

1. P1 headline flow overflowed (ended 1921, bottom 1828) on the first
   render: the Italian bridge line wrapped to 4 lines and two Zahlen
   lines to 3 lines, pushing a column move. Shortened (bridge to the
   3-line form `Note — Englische Woche = settimana inglese · Spieltag
   = giornata · empfangen = ospitare · Bundesliga = Bundesliga.` and
   the Zahlen parentheticals to `(9 partite, 9ª giornata)` /
   `(14,04 cent in meno al litro)`). Flow now ends at 1555 = core.
2. First occlusion run: 9 NEW flags, all Italian over-length lines.
   Fixed by wording shortening only: P1 Fragen subtitle →
   `Le cinque domande della Germania.`; box titles →
   `FERIENWECHSEL · Vacanze`, `HERBSTWÖRTER · Autunno`,
   `SCHULWÖRTER · Scuola`, `DIE ZAHLEN · Numeri`; P6 ÜBUNGSDATEN
   parenthetical → `(Esempio della redazione, non un vero sondaggio.)`;
   P7 phrase-7 translation shortened to 2 lines
   (`…ma la ripresa non regge da sola.`, dropping the added `ancora`,
   which is not in the German quote) so its tag no longer strikes the
   error-clinic rule. Re-audit: 0 flags.
3. P7 readers box first ended at 1532.5, crossing the phrases rule:
   the Italian note was shortened by relying on the label for the
   “editors' example” fact (note now 2 lines, §8 above), bringing
   col-3 ends to 1504.5.
4. Transform-record fix: the first content7 patch wrote a literal
   backslash-n into the readers lines (syntax error); corrected to a
   real two-line assignment in the build copy and in transform.py.
5. P1 top-strip, masthead second line, badge, and band lines were
   width-measured before building (badge 826.5px, footer 886.7px,
   masthead line 1559.4px — all inside their slots).

## 9. Files, sizes, hashes

- `svg/` ×8 (1950×2700 source), `cards/` ×8 PNG @1950×2700.
- Print PDF `Die-Lucerna-VOL2-IT.pdf`: 4,137,863 bytes, 8 pages,
  1462.5×2025 pt,
  sha256 42d18ca43f7994db4245c702fc89cc319eef30d7f30b064d57f9bb087acff56a.
- Web PDF `Die-Lucerna-VOL2-IT-web.pdf`: 4,147,320 bytes, 8 pages,
  1400×1938 pt (JPEG pages q85 @1400px; under the 10 MB insert limit),
  sha256 09d9b4ae05e03fe9baf386bc70a2bb60d805cbb46bfa472a78abf5441d9b402b.
- SVG sha256:
  p1 a18e05d9088693dd7c568f76ddfabcb7d74c2f00776f1e4668e66f777b4c60e4 ·
  p2 76c721f58a8c9668d40d4d52cb77d9850d04fb2464e4053c378dce910e4c7002 ·
  p3 ccaac269146e1989e9cf19c2eba32c9657446f75880772ec8e3b758239d6a13d ·
  p4 248362a571975d92b2f5aae9b337083a23976a63eb87857449e0e58082b77903 ·
  p5 bad4d771e29d28243b24f33b4f26564ea7018fa110af471bf4460e11cc42a80b ·
  p6 0200b84f0ff11a715596c22dd27048bf0950f94a68a470ef36e0eb1ffe4dcdeb ·
  p7 08a0518b1e73b660807283ffb14a64fd1b5a6d05db83a8a06c8abdee983425e3 ·
  p8 fa94d8dfdc799e9e830ce1c094c55796e8086dd5960f36f4e4b6f2b7e6275979.
- Re-render determinism: a second single-process run produced
  byte-identical SVGs (hash diff empty).
- All 8 cards were visually reviewed end to end (this build round):
  no overflow, no text/rule collision, footers and page lines present
  on every page, chart labels clear of bars, readers box fully inside
  its border, phrases tags clear of the clinic rule.
- `ABSTRACT.txt`: one Italian line, no ASCII double quotes, naming the
  real topics (football week, fuel discount, care, back to school) and
  learner search phrases (`imparare il tedesco con le notizie`,
  `esercizi di tedesco A2 B1 B2`).

## 10. Build environment (as actually used)

- Renderer: `tools/venv/bin/python` ONLY (system python3 was not used
  for any render; it lacks cairosvg).
- `tools/venv/bin/python`: Python 3.12.3, **Pillow (PIL) 13.0.0**.
  (System python3 on this VM reports PIL 10.2.0 — recorded here only
  to distinguish it; no deliverable was produced with it.)
- Single-process render throughout (shared bslib4 registry; README §7):
  `run.py` runs content12 → 34 → 56 → 7 → 8 in one process; no content
  module was ever imported or run inside the core build directory
  (README §11); all comparisons used copies or the shipped SVGs.
- Build tree: `hidden_files/weekly-report-w45-de-it-build/` (transform.py,
  build-log.txt, render-log.txt, freeze-diff.json, occlusion.json,
  p8-compare.txt, reg-dump.json, cjk-inventory.txt).
- Core and W43 directories were read-only for this build (hashes in
  §2 prove the core untouched).
