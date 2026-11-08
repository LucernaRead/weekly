# Lucerna Weekly — production toolkit

Shared, hard-coded tools for the weekly-paper pipeline. They exist because
every builder/proofreader used to re-derive the same checks heuristically —
the geometric occlusion audit alone was rewritten 10+ times, and two of
those rewrites carried measurement bugs that shipped false results (an
advance-width pass on zh-TW×IT P7; a zero-height line box that could never
fire, EN×PT P6). **Rule: future editions MUST use these tools instead of
hand-rolled equivalents.** If a check you need is missing, extend the tool
here — do not fork a private copy into a build directory.

All tools live in this directory and run with the persistent venv
(**never** `/tmp/wp-venv` — it is ephemeral):

```bash
cd ~/workspace/weekly-git/tools
PY=./venv/bin/python        # cairosvg + pillow + pypdf installed
```

Scratch/output goes to `tools/scratch/` — never `/tmp` (512 MB tmpfs).

---

## 1. `tables.json` + `tables.py` — hard-coded reference data

Language codes/names/labels/mastheads (article rule included), Discord
thread IDs per target, core dir / build dir / P8 filename per language,
per-native-column furniture (badge + footer
templates, page line, gloss prefix, P8 separator, full target-name tables
for de/fr/es/it/pt + provisional nl), repo frontmatter conventions from
`lint.mjs`, and the font table. Furniture strings were extracted verbatim
from shipped SVGs/KITs — never invent one; if a string is wrong, fix it
here from a shipped artifact and say so in the commit.

```bash
$PY tables.py lang fr
$PY tables.py thread fr                                  # -> 1562312611603947611
$PY tables.py vol 2026-W47 --allocate                   # start of a week: next issue number into production/volumes.json
$PY tables.py vol 2026-W46                              # -> 3 (the tracker is the only source; never type a vol)
$PY tables.py furniture pt --target ko --week 2026-W46  # rendered badge/footer/page line, VOL from the tracker
$PY tables.py slug 2026-W43 fr zh-cn                     # -> 2026-w43-fr-zh-cn
$PY tables.py edition-dir zh-cn fr                       # -> weekly-report-zhcn-fr (exception table)
$PY tables.py frontmatter                                # required fields, slug/pdf rules
$PY tables.py check-repo                                 # cross-check vs repo frontmatter
```

Python API: `import tables` — `tables.lang/thread/masthead/slug/
edition_dir/core_dir/core_build_dir/p8_file/furniture`.

**Validation (2026-10-21):** `check-repo` over all repo editions —
73 checked, **0 mismatches** (threads, target/native names + labels,
mastheads). The brief's thread IDs match the repo exactly. Furniture
renders reproduce shipped strings byte-for-byte (KO×PT badge/footer,
FR×DE footer, EN×NL provisional badge/footer all compared against the
shipped SVGs).

## 2. `occlusion_audit.py` — THE geometric audit

Paint-order SVG parse; **true ink boxes** from PIL/FreeType
(`font.getbbox` at 4× supersampling, bold faces included) — not advance
width, not the em band. Line/thin-rect boxes expanded by half the stroke
width. Classes: `COVER` ≥30%, `LINEX`, `FOOTER` (ink below y=2580,
footer baseline 2624 exempt), `EDGE`, `TEXTX`, `BOXTITLE` (ink vs the
borders of the containing bordered box). Every real run executes the
synthetic selftest first and refuses to report if it fails.

```bash
$PY occlusion_audit.py --selftest
$PY occlusion_audit.py ../production/<week>/<slug> [--json out.json]
$PY occlusion_audit.py ../production/<week>/<slug> --core ../production/<week>/core-<target>
# exit 0 clean · 1 flags (with --core: NEW flags) · 2 selftest failed
```

Flags are a gate, not a verdict: pixel-adjudicate each flag before
fixing (a line is a defect only if it intersects actual rendered ink).

**Validation (2026-10-21):**
- Selftest: all 6 planted classes fire exactly once; clean controls silent.
- `weekly-report-ko-pt`: **0 flags** — matches the independent
  proofreader's true-ink audit (0 flags); the builder's 1 flag was the
  em-band P1 masthead artifact, which true ink correctly does not raise.
- `weekly-report-ko-vol1` (core): **0 flags** — matches the 2026-10-21
  programme audit (KO core clean).
- `weekly-report-zh-tw-it`: **0 flags** — the P7 title that shipped as
  «Struttura settimanale» is clean (the builder's em-band run recorded 1
  inherited masthead flag; both true-ink audits — the proofreader's and
  this one — find 0).
- Doctored copy: zh-tw-it P7 copied to `scratch/doctored/`, its box title
  shifted +45 px → **BOXTITLE fires: “right ink 1888.0 > border 1885.0”** —
  the exact historical defect geometry. The unshifted copy: 0 flags.

## 3. `freeze.py` — baseline proof + frozen-core diff

```bash
$PY freeze.py baseline --build ../production/<week>/core-<target> \
    --core-svg ../production/<week>/core-<target>/svg --out scratch/baseline-<target>
$PY freeze.py diff --core-svg ../production/<week>/core-<target>/svg \
    --edition-svg ../production/<week>/<slug>/svg [--strict-cjk] [--json out.json]
```

`baseline` copies the build into scratch, rewrites every `production/`
output path in the copy to the scratch tree, **aborts if any copied file still
references the real edition dir**, runs the copy (run.py, else imports
content12/34/56/7/8 in order), sha256-compares all 8 SVGs, and re-hashes
the real core SVGs afterwards to prove they were untouched.

`diff` lists every added/removed text string per page (multiset) plus CJK
accounting. **`--strict-cjk` is the gate for zh-cn/zh-tw/ja targets**:
added CJK characters must be 0. For ko targets, Hangul syllables cited
inside reader-language notes legitimately add counts (see validation) —
read the per-char list instead of gating on it.

**Validation:** KO core baseline **8/8 byte-identical**, core untouched.
Diff core-vs-itself: all zeros. KO core vs KO×PT: only explanation-layer
string churn; added CJK = 8 Hangul syllables (어/요/시/험/수/생/장 — Korean
words cited in Portuguese notes, e.g. the P7 clinic note quoting
«할 수 있어요»), i.e. citations, not new target text. zh-tw core vs
zh-tw×IT, ja core vs ja×IT and ja×PT: **added CJK = 0** under
`--strict-cjk`, as the rule requires.

## 4. `p8.py` — printed-note set gate

Extracts, from a shipped P8 SVG, the set of exercise numbers carrying a
printed note + the printed key per number. Wrap-aware; handles paren
style and dash style (incl. families that re-laid answers in the other
style) and all P8 separator forms. Verdicts per
`production/notes/audit-p8-notes/DECISION.md`: `CLEAN` / `EXTRA_ONLY`
(adjudicated acceptance, exit 0, extras listed) / `SHORT` (gate failure,
exit 1) / `UNCERTAIN` (exit 1). Key diffs are listed (translation items
legitimately re-aim — informational).

```bash
$PY p8.py extract --p8 <p8.svg> --total 150
$PY p8.py compare --core-dir ../production/<week>/core-<target> \
    --edition-dir ../production/<week>/<slug> --target <code>
$PY p8.py compare --core-p8 <svg> --edition-p8 <svg> --total 149
```

**Validation — reproduces the programme audit's anchors EXACTLY:**
EN core = **62**, FR core = **67**, NL core = **150**; EN×ES post-fix
**CLEAN 62=62**, keydiff [136, 139, 149]; en-de and en-fr **EXTRA_ONLY**
(62 → 149, the identical 87-number extra list); NL×PT CLEAN 150=150.
Cross-run against the original `audit.py` on today's repo: identical
status / counts / extra lists / keydiff lists on every pair tested.

## 5. `insert.py` — repo insert

The full flow, each step verified, stopping loudly on failure: abort if
the slug exists → render the .md (donor fields + excerpt from the
target's ×EN sibling md; masthead/names/thread from tables.json;
**pdfBytes/pdfSha256 measured from the actual web PDF file**) →
`lint --write` → commit metadata → push with ls-remote verification
(retries — tunnel cuts are normal) → copy PDF → `lint --write` again →
`lint --require-pdf` must be green → commit PDF + index.json → push →
final `ls-remote == HEAD` check + edition count.

**Bundle mode (user order 2026-11-03; the normal insert path): one
bundle = one commit.** `--bundle --week 2026-W46 --target de` renders
every remaining native first (any missing piece aborts before anything
is written), writes all md + .text.md + PDFs, one `lint --write`, one
`--require-pdf` gate, ONE commit, one verified push. Never one commit
per edition, never metadata/PDF split commits, never one commit for the
whole week. Single-edition mode above is for one-off repairs only.

```bash
$PY insert.py --week 2026-W43 --target ko --native pt \
    --edition-dir ../production/2026-w43/2026-w43-ko-pt   # single-edition repair only
$PY insert.py --week 2026-W46 --target de --bundle \
    --exercises 150 --seed-excerpt "..."                  # bundle: one commit; vol comes from the tracker
$PY insert.py ... --dry-run                               # existence/PDF checks only
$PY insert.py ... --render-only                           # render + lint in a scratch repo copy (single-edition only)
```

**Validation (2026-10-21):** against the already-inserted KO×PT it
**aborts cleanly at step (a)** (“slug 2026-w43-ko-pt already exists —
nothing written”, exit 1). `--render-only` for the pending EN×NL:
rendered .md + PDF into a scratch copy of the repo → `lint --write` and
`lint` green, rendered pins verified against the copied PDF,
`lint --require-pdf` green (75 editions incl. the rendered one); the
real repo was not touched (git status clean). `--dry-run` on the same
case passes its checks and writes nothing.

---

## 6. `cover_check.py` — website cover block gate (rule 11 companion)

**Only for hand-written cover blocks (W45 and earlier).** From 2026-w46 the blocks are generated from
`production/covers/<week>/cover.json` by `node tools/cover.mjs <week>`; the gate is lint rule 14. Do not run
this tool on W46 or later (see SOP §8.6 and Appendix 5).

Per `<article>` in every website cover block it asserts: (1) a
`<p class="lc-excerpt" lang="<story lang>">` exists, its `lang` matches
the story language, and its text is byte-identical to that week+story's
print-cover excerpt; (2) the teaser `<p>` exists and its text is
byte-identical to `teasers[reader][story]`; (3) the headline is
byte-identical to the print-cover frontmatter headline; (4) exactly 12
articles with `data-story-langs` intact (12 codes, each exactly once).
It also asserts one `.lc-excerpt` rule in each block's `<style>` and at
most one `data-image-slot` per article. Exit 0 only when every check
passes; any failure is printed as `FAIL …` with week/reader/article/
language, plus a final `COVER CHECK FAILED`.

**Why it exists (2026-11-05):** the W43/W46 cover build verified its
output by comparing the `.html` against `teasers.json` — but the
excerpts were never inserted into the `.html`, so a comparison check
could not catch the missing element. Every article shipped with only
the reader-language teaser and no target-language excerpt, and the user
caught it reading the cover. This tool reads ground truth independently
of the build — headlines + excerpts straight from the print-cover `.md`
files in the repo, teasers from the per-week `teasers.json` — and fails
loudly on any missing or wrong-language excerpt. Never compare a build's
output against the build's own input and call that verification.

**Ground truth the tool trusts (do not "fix" by editing data):**
excerpts come from the print covers, NOT from `teasers.json`
`` `excerpts` `` — W43's are different short summaries (one contains
mojibake), W46's are truncated prefixes of the print-cover paragraphs.
W45 `.html` headlines are English glosses (0/144 match the print
covers; W43/W46 are 144/144), so the headline assertion FAILS for W45
until the headlines are separately corrected — a true positive, not a
tool bug; do not add exceptions. Template variance is not a failure:
only es/fr/zh-cn/zh-tw blocks use `class="lc-teaser"` on the teaser
`<p>`; the tool finds the teaser structurally and checks its text.
A future week's build must produce its `teasers.json`
(headlines/teasers/excerpts) under
`production/covers/<week>/` BEFORE running this gate.

```bash
$PY cover_check.py --week 2026-w46            # one week
$PY cover_check.py --all                      # every week with 12 cover dirs
$PY cover_check.py --week 2026-w46 --root ~/workspace/weekly-git
```

**Validation (2026-11-05):** on the excerpt fix, W43 and W46 PASS
(144 articles each: excerpts, teasers, headlines, structure all green);
W45 FAILS on headlines only (144 headline mismatches, the known
gloss defect) while its 144 excerpts, 144 teasers and structure pass.
Re-running the tool against the pre-fix tree (git stash) fails with
432 `MISSING <p class="lc-excerpt">` lines — the exact defect it exists
to catch — plus the 144 W45 headline mismatches and 36 missing
`.lc-excerpt` CSS rules (612 failures total).

---

## Data contradictions found while consolidating (read before reusing)

1. **Fonts:** the tasking brief named combined files
   `NotoSerifCJK.ttc`/`NotoSansCJK.ttc`. This VM actually ships the split
   files `NotoSerifCJK-Regular/Bold.ttc` + `NotoSansCJK-Regular/Bold.ttc`
   (face indices JP=0, KR=1, SC=2, TC=3, HK=4 in every file). tables.json
   records the real paths.
2. **FR badge singular/plural:** shipped badges split — `TEXTE EN …`
   (EN/DE/RU/JA/KO targets) vs `TEXTES EN …` (IT/NL/PT/ES/ZH). The table
   uses TEXTES as the template and records the split under `variants`.
   Footers always use singular `TEXTE EN`.
3. **EN×DE footer** is an English-form exception (“ENGLISH WEEKLY VOL.1 ·
   Englischer Text · Deutsche Erklärungen”), not the canonical DE footer
   template the other 9 ×DE editions use. Recorded under DE `variants`.
4. **FR gloss prefix:** EN×FR's KIT once records `Note | `; the column's
   shipped gloss boxes use `Note — `. Treated as an early variant.
5. **Strict-CJK scope:** the “added CJK = 0” rule holds exactly for
   zh/ja fan-outs (verified on 3 shipped editions) but NOT for ko —
   Korean words cited in reader-language notes add Hangul counts
   (8 in KO×PT, all citations). Gate zh/ja; adjudicate ko by the list.
6. **Repo state moves during the day:** the edition count went 72 → 74
   while this toolkit was being built (parallel inserts by the main
   line), and `2026-w43-zh-cn-pt` briefly existed as md-without-PDF
   mid-insert. insert.py's abort-at-(a) + ls-remote verification exist
   precisely for this; always run them instead of assuming repo state.
8. **Dash-style answer families (ES×NL + IT×NL builds, 2026-10-21):**
   the shipped ES and IT cores print `N. key — note` (writing items
   `N. ✓ note`), despite briefs describing them as paren style. Their
   fan-outs keep the core's dash style by leaving the answer-generation
   code byte-identical. Dash-style family: NL, KO, RU, ES, IT. Before
   writing any builder brief, verify the core's P8 style from the core
   SVG/code — never from memory.
9. **RU column furniture (established by FR×RU, 2026-10-21):** tables.json
   has NO RU-native column entry; FR×RU established the pattern from the
   NL/PT column structure (its KIT §3 is the registry): badge
   «ТЕКСТЫ НА <TARGET-RU> · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ
   РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ»; footer «<Masthead> · <TARGET-ADJ-RU>
   ЕЖЕНЕДЕЛЬНИК VOL.n · ТЕКСТЫ НА <TARGET-RU> · ОБЪЯСНЕНИЯ НА РУССКОМ»
   (VOL follows the target core — FR = VOL.2); page line «Страница N из 8»;
   gloss prefix «Пояснение — »; P8 separator «— СТРАНИЦА N —»; bilingual
   section heads = target original · Russian short form. All later ×RU
   editions copy this pattern. (TODO: fold into tables.json properly.)
   Target-name adjudication (2026-10-21, NL×RU): the Dutch target is
   «ГОЛЛАНДСКИЙ / НА ГОЛЛАНДСКОМ» — the everyday Russian form wins for
   a learner weekly; this OVERRIDES the «НИДЕРЛАНДСКИЙ» variant in
   EN×RU KIT §3's name table. All other names follow that table.
10. **Same-line ink collisions (FR×RU build, 2026-10-21):** the canonical
    occlusion audit's TEXTX class only compares DIFFERENT lines. A real
    defect class it cannot see: two text runs on the SAME baseline
    colliding (FR×RU P1: centred strapline overprinted the right-hand
    date). Every build/proofread must ADDITIONALLY scan same-baseline
    text-node ink spacing on furniture bands (P1 top band especially)
    — FR×RU's scratch/rowcheck.py is the reference implementation.
13. **p8.py detect_note dash-truncation fix (EN×RU build, 2026-10-21):**
    the note-detection disambiguation truncated a key at the first
    « — » INSIDE a parenthesised note (Russian notes routinely contain
    em dashes, e.g. «(Present Simple — о привычках)»), producing false
    keydiffs. Fixed: the dash branch now requires the key candidate to
    contain no parenthesis. Regression evidence: en-nl / en-es / de-nl /
    es-nl / fr-nl compare outputs byte-identical before/after; FR×RU's
    false keydiffs cleared 15 → exactly [71, 72, 73, 132, 145], matching
    FR×NL's adjudicated legal list. Standing lesson: when a compare
    reports keydiffs in a NEW reader language, suspect extraction
    artifacts in the tool before suspecting the edition — verify
    against the registry diff, and if the tool is wrong, fix the tool
    and re-run the affected comparisons.
14. **P8 bracket form follows the family's shipped fan-out CODE
    (DE×RU proofread, 2026-10-21):** the DE core renders full-width
    parens because its code path serves Chinese notes; ALL six shipped
    DE fan-outs changed the code to half-width ` ({note})` (DE×NL
    build line 154) and measure full-width = 0. A builder claim that
    "the typesetter converts parens automatically by script" is FALSE
    — disproven by the code. Rule: verify the P8 note-bracket form
    from the family's shipped fan-out build code, never from the
    core's rendered SVG alone, and never accept a conversion excuse.
15. **"The core has the same flag" is not an adjudication for
    explanation-layer text (DE×RU proofread, 2026-10-21):** inheritance
    covers only FROZEN target-language elements byte-identical to the
    core. A fan-out's own subtitle/gloss/box title that overflows must
    be shortened even when the core shows an analogous flag on its own
    (different, frozen) text — DE×RU's P1 Fragen subtitle was the
    edition's own Russian text, shortened on proofread; audit then
    read 0 flags.
11. **Never run a build module standalone — and never import one
    inside the CORE build directory (DE×RU accident 2026-10-21;
    REPEATED by ZH-CN×RU 2026-10-21):** content modules carry ABSOLUTE
    OUT paths pointing at the CORE's files/ directory, and their
    module-level code EXECUTES ON IMPORT — a bare `import content8`
    for a "quick comparison" rewrites the shipped core P8 SVG on the
    spot (zh-cn core was overwritten with a 38-item version this way).
    Rules: (a) never run python imports of content modules inside the
    core build dir at all — for comparisons, copy the build, repoint
    OUT, and import only there; (b) copies are only ever executed
    through freeze.py (which repoints OUT) or the build's single
    one-process driver AFTER its OUT paths are repointed to the copy's
    own edition dir; (c) any core-integrity scare is closed only by
    triple evidence re-run by the independent proofreader: fresh
    freeze baseline 8/8 + published-card pixel comparison + the repo
    frontmatter pin vs the core web PDF on disk.
    REPOINTING PITFALL (EN×JA proofread, 2026-10-21): hand-rolled
    repoint scripts must match EVERY OUT spelling — some builds write
    `os.path.expanduser("~/…")` instead of a plain path literal, and a
    sed that misses that form silently re-runs the export into the
    SHIPPED directory (harmless there only because the build proved
    fully deterministic: core hashes unchanged, 16/16 cards
    pixel-identical). Prefer freeze.py's own repointing; if you hand-
    roll, grep the copy for `expanduser`, `Path.home` and `~` path
    forms and verify OUT by printing it before the first run.
12. **Occlusion-audit blind spot — sub-30% chart-label coverage
    (DE×RU build, 2026-10-21):** COVER fires at ≥30% glyph coverage;
    a chart label clipped by a later-drawn bar below that threshold
    passes silently (DE×RU P6 label was truncated, caught only by
    reading the card). Until the tool gains a GRAZE class (TODO),
    every build/proofread MUST element-check text ink vs later-drawn
    rects on chart pages regardless of audit flags.
7. **One-process re-render rule (EN×NL proofread, 2026-10-21):** in builds
   whose content modules share the bslib4 exercise registry, the content
   modules MUST be run in ONE driver process. Running them separately
   restarts the exercise numbering, producing a corrupt render that
   LOOKS plausible. Any re-render after a fix must therefore go through
   the build's single driver entry point; a partial re-render is a
   defect, not a shortcut.
16. **×KO orphan scan must include parenthesised fragments (PT×KO
    proofread, 2026-10-22):** a builder's self-reported "orphan = 0"
    missed 5 real Korean orphan fragments whose final element carried
    a `)` («세요.» / «소)» / «이)» / «적인 것.» / lone «장소»). The
    ×KO orphan scan — builder AND proofreader — must cover EVERY
    final-line text element, including notes/glosses ending in a
    parenthesis, not only whitespace-tokenised prose lines. A claim of
    orphan = 0 is only valid with the scan definition stated.
    EXTENDED (JA×KO proofread, 2026-10-22): the scan must ALSO cover
    the mirror defect — a continuation line that STARTS with orphan
    punctuation (a wrapped prompt line beginning «? …» after its
    sentence-final «요» stayed on the previous line). Line-start
    orphan punctuation and mid-word splits with ≥3-syllable tails
    (RU×KO: «채|우세요») are in scope; a scan that only counts
    single-syllable final lines will miss both.
    EXTENDED (RU×KO proofread, W45 2026-10-27): the scan window must
    start at 10, not 15 — P8 answer lines sit at 14.69 spacing and a
    15–45 window structurally excludes them (it missed P8 item 99's
    «나 | 타내요» 3-syllable split; a 10–45 rescan found it as the
    only qualifying site). Builder AND proofreader scans use 10–45.
    EXTENDED (ES×KO proofread, W45 2026-10-27): the ≥3-syllable-tail
    criterion is the standard for EVERY prose column (calendar,
    plan, ¿Y TÚ?, cifras boxes, etc.) — a builder scan reporting
    S3 = 0 under a "first segment ≤ 1 syllable" criterion is NOT
    equivalent and missed 4 qualifying sites (P1 cifras
    «자치|주예요», P2 calendar «소시|에다드», P4 ¿Y TÚ?
    «메트로폴리|타노», P5 plan «메트로폴|리타노»). State the
    criterion with the scan result; "first segment ≤ 1" wording is
    retired.
17. **Transform scripts must not splice by AST byte offsets
    (NL×JA build, 2026-10-22):** replacing strings via AST node
    byte offsets corrupted a multibyte (CJK) source file; the build
    had to be re-copied and redone with line-based splicing. Rule:
    fan-out transforms splice on whole lines or exact unique literal
    matches with an assertion after each replacement, never on raw
    byte offsets into UTF-8 source.
18. **Value-map transforms on f-string fragments must use bare text,
    never repr literals (RU×JA build, 2026-10-22):** an AST value
    replacement applied a quoted repr literal to a JoinedStr part,
    leaking the quotes into the rendered text («'82' 語»). Rule:
    when a replacement target is part of an f-string, substitute the
    bare string value; after any AST transform, assert per-page
    stray-quote counts against the core before rendering.
19. **×JA svglib NO_START may be extended for ASCII-punctuated body
    languages (KO×JA proofread adjudication, 2026-10-22):** the
    canonical JA svglib (md5 d73e23b3…) NO_START set covers only
    full-width closers; a frozen body text that uses ASCII closers
    (Korean body: `.` / `)` etc.) would strand them at line starts.
    Permitted deviation: the build COPY extends NO_START with the
    body core's own svglib ASCII closer set (KO core's set:
    `)]}〉》.,!?%:;"`), everything else byte-identical (mechanism,
    JP face, SEAM_SLACK). The canonical file itself is never edited.
    The independent proofreader must diff the two svglib files and
    confirm the change is exactly that superset line plus comments.
20. **×ZH-TW pairing-badge slot/size follows the TARGET core's family
    precedent, not one fixed §3 value (FR×ZH-TW + IT×ZH-TW proofread
    adjudications, 2026-10-22):** the EN×ZH-TW KIT §3 registry records
    the EN core's own instance (subtitle slot, 19.5pt). Other target
    families carry their own shipped conventions: EN/DE/ES cores have
    a native subtitle slot at y≈372 → badge replaces it in place at
    19.5pt BRICK; FR/IT cores have NO free slot (their y=372 is frozen
    body strapline) → badge is INSERTED at y=574, 22pt BRICK centered,
    matching the family's own fan-out precedents (FR×JA/FR×KO/IT×JA).
    Builders must state which family case applies and cite the
    shipped precedent in the KIT; proofreaders adjudicate against the
    family precedent, not against the EN instance.
    KO-target case (KO×ZH-TW proofread, 2026-10-22, measured across
    the 7 shipped ko-<native> fan-outs de/fr/es/it/pt/nl/ru): the
    majority form SHIFTS the masthead block — subtitle 372→366,
    badge INSERTED at y=394, 20pt weight-700 BRICK, rules +20,
    dark band +9 (band lines at 487/531); displacement stops at the
    masthead block (frozen elements below y=606 unmoved). Variants:
    ko-en is an early variant (same geometry, 17pt, olive #3e4c2a);
    ko-ja takes the subtitle slot (y=372, 19.5pt, no shift).
    JA-target case (JA×ZH-TW proofread, 2026-10-22, measured against
    the shipped JA×KO geometry): the JA masthead is a full geometry,
    shared by ×KO and ×ZH-TW — subtitle moves to y=316, badge
    INSERTED at (975, 356) 19pt BRICK, strapline moves to y=390,
    double rules at 406/413, dark band at 424; the wordmark baseline
    stays at the CORE's position (262 — JA×KO's 248 is its own
    variant; keeping the core position is the better freeze). The
    four displaced elements are masthead furniture (text unchanged);
    body elements do not move. A badge placed without this shift
    overprints the strapline by ~2.2 ink units — sub-threshold for
    the audit, caught only by eye; always copy the whole geometry.
21. **Gloss item counting must split on `·` itself, never on ` · `
    (PT×ZH-TW proofread, 2026-10-22):** a source gloss string may
    contain a separator with no leading space («擴大（比分）· a
    arbitragem»), so counting by the spaced form undercounts (the PT
    core's P4 box read 4 by that method, true count 5; the column's
    true total was 24, not the builder's 23). Count items by splitting
    the rendered gloss() call string on `·` and verifying each item
    survives in the render; the hard rule (fan-out gloss count ==
    core gloss count, item by item) is judged on that count.
22. **Every edition ships an abstract (user instruction, 2026-10-22):**
    the builder delivers `ABSTRACT.txt` in the edition dir — one line,
    no ASCII double quotes, written natively in the reader's language,
    naming the issue's real topics (events, festivals, matches) and at
    least one phrase learners actually search, plus masthead, target
    language name, A2–B2 levels and the exercise count. `insert.py`
    aborts without it and renders it twice into the repo md: the
    frontmatter `abstract` field (lint-required, copied into
    index.json) and a body section headed by the native language's
    word from tables.json `languages.<code>.abstract_heading`. Facts
    come from the edition itself — never a template with swapped
    words. W43's 130 editions were backfilled 2026-10-22 by per-column
    writers working from a single topics file per target core.

#23（2026-10-28）：web PDF 必须带文字层。旧 web PDF 是 PIL save_all 整页 JPEG
拼合，0 字体、pdftotext 0 字节，搜索引擎抓不到内容（W43/W45 抽查全中）。
`webpdf.py <svg-dir> <out.pdf> [--page-px 1400]` 是唯一 web PDF 构建器：
源 SVG → 图片降至网页分辨率（JPEG q85，带 alpha 的 kept PNG）→
fontTools 按当期 <text> 用字裁字体（fc-match 定位 TTC 面，改名 Lucerna*
隔离，regular + bold 各一）→ 隔离 fontconfig 下 CairoSVG 出矢量文字 →
pypdf 合并。验收：exit 0 且 pdftotext 字节 > 0；有 print 版时提取文本须
与 print 版逐字节一致；单文件目标 < 7MB（推送上限）。典型结果 2-3MB、
文字与 print 版一致。禁止再用 PIL 整页拼合出 web PDF。
