# GATE-LOG.md — 2026-W47 it-pt (round 2 proofread, re-fan-out), mechanical gates self-run

Proofer: independent proof2, 2026-11-11. All commands run by the proofer; nothing
copied from builder logs. Working directory: ~/workspace/weekly-git.
My scratch dir: ~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-pt1/
`PYTHONDONTWRITEBYTECODE=1` throughout. TMPDIR = my scratch (never /tmp).

## 0. Hard-gate probes (pre-work, 2026-11-11 ~20:36 UTC)

| probe | result |
|---|---|
| `git -C ~/workspace/weekly-git hash-object -w /dev/null` | OK (`e69de29bb2…`, RC=0) |
| real file write into scratch `scratch-proof2-it-pt1/probe.txt` | OK |

Production pre-work hashes recorded in `prod-hashes-before.txt` (8 SVGs + print +
web PDF + text.md); re-verified at the end (§15): all OK, production untouched.

## 1. Identity (KIT §7 three SHA)

Proofer's own `sha256sum`:
- print `6f74ee92c72d4ca545fb763c268231b05b6970a5e170b943cdc2882a3ce4a477`, 14,036,628 B — MATCHES task + KIT §7
- web `f28a563544bcac8998097fc418c94b47f92a650b351518339c9be864a1ada1c4`, 1,294,408 B — MATCHES
- text.md `2ce7bfe9bb1f58d72b6249c4a2d2cd2bf5d97e028e10d2e3acfc480797627cb8`, 55,739 B / 1317 lines — MATCHES

## 2. Build interpreter

`tools/venv/bin/python -c 'import PIL'` → Pillow 13.0.0 (same as the build).
System python3 → Pillow 10.2.0, not used.

## 3. run.py re-run (in a scratch copy, OUT repointed FIRST — RC=0, TOTAL 150, 0 overflow)

The edition's `content*.py` hardcode
`OUT = ~/workspace/weekly-git/production/2026-w47/2026-w47-it-pt/svg`, so a naive
scratch-copy run would REWRITE the production SVGs (the incident it-en proof2
recorded in its GATE-LOG §3). I did not do that: I copied the whole edition dir to
`scratch/rerun/edition` (minus `cards/`, `__pycache__/`, PDFs), sed-patched the OUT
line in the five scratch copies to `…/scratch-proof2-it-pt1/rerun/svg`, grepped the
copies to confirm no production path remained except `render.py`'s BASE (which I
never executed as-is), and only then ran `tools/venv/bin/python run.py` there.
Output to `rerun/run.log`.
Result: RC=0; 0 occurrences of FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE;
TOTAL 150; levels A2 47 / B1 70 / B2 33; pages 10/18/18/18/18/18/12/38;
types Completa a frase 61 / Escolha múltipla 48 / Relaciona as palavras 12 /
Forma frases 7 / Estruturas frásicas 1 / Verdadeiro ou falso 3 / Cloze 13 /
Traduzir 4 / Escrita 1. P1 settimana ends 1250.24; P4 col3 ends 1140.45;
P7 col3 ends 1673.0; P8 exercises flow ends col 3 y=870.12;
flow[P8-keys] ended col 3/3 y=2529 (bottom 2552, 23 px spare).
Production SVGs re-hashed immediately after: unchanged.

## 4. SVG rebuild 8/8 + print PDF re-render byte-identical

- Re-run SVGs (`rerun/svg/`) vs shipped SVGs: `cmp` 8/8 byte-identical
  (p1–p8; e.g. p1 `0362f854092e…`, p8 `c7b5373e4a4d…`).
- Print PDF re-render: my own `rerender.py` (same steps as edition `render.py`:
  cairosvg svg2pdf per page + pypdf merge, reading the shipped SVGs read-only,
  writing only to scratch) → `rerender-print.pdf` 14,036,628 bytes, sha256
  `6f74ee92c72d4ca545fb763c268231b05b6970a5e170b943cdc2882a3ce4a477` —
  **BYTE-IDENTICAL to the delivered print PDF**. (Edition `render.py` was NOT
  run as-is: its BASE is hardcoded to production and it would overwrite the
  delivered PDF and `cards/`.)
- Web PDF was NOT re-rendered (task: web PDF bytes are not reproducible; only
  its text layer was compared — gate 8).

## 5. Freeze (canonical tool)

- FIRST attempt (transparent record): I passed my already-patched `rerun/edition`
  copy as `--build`. freeze.py only repoints paths that still aim at the real
  production tree, so it repointed only `render.py`; the run's SVGs landed in
  `rerun/svg/` and freeze reported `baseline: 0/8` with empty produced hashes.
  That 0/8 was a harness mistake of mine, not a build failure — the same SVGs
  were verified 8/8 identical by direct `cmp` in gate 4, and production was
  untouched (hashes re-checked). I discarded that run.
- SECOND attempt (clean): fresh UNPATCHED copy of the edition dir as `--build`
  (`freeze-src/edition`), `--core-svg` the shipped edition SVGs,
  `--out scratch/freeze-baseline` → RC=0, **8/8 "OK"** (produced sha256 == shipped
  sha256 for all 8 SVGs; repointed files: render.py, content12/34/56/7/8);
  "core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)".
  Log: `freeze-baseline.log`.
- `tools/freeze.py diff` core vs edition (JSON `freeze-diff.json`): pages 1–8
  present; added/removed strings per page P1 +30/−46, P2 +33/−29, P3 +32/−30,
  P4 +28/−26, P5 +43/−41, P6 +29/−25, P7 +42/−40, P8 +172/−637; every
  added/removed text-node fragment on P1–P7 explained by a translations.py
  value/key, a NOTE/gloss composite, a gloss + " (Pagina N)" composite, or
  generated page furniture — **0 unexplained fragments** (adjudicated by the
  gates.py copy, §10). Strict-CJK: added CJK = 8 × U+3000 only (one per page;
  furniture separators, exempt); non-space added CJK = {}.
  Note: `freeze.py diff` exit code is 1 for Latin editions in this setup (the
  strict-CJK report lists the exempt U+3000); the gate reads the JSON, not the RC.

## 6. Occlusion audit (canonical tool)

- `tools/occlusion_audit.py <edition svg>` (selftest OK — all 6 classes fire,
  clean controls silent): **0 flags** on the 8 shipped SVGs.
- Caveat recorded in PROOF-NOTE.md: BOXTITLE covers bordered boxes only;
  borderless cream boxes are blind to horizontal overflow — the cream-box scan
  (gate 7) is the supplement, and it found 0 flags here (unlike it-en, where it
  found 3).

## 7. Cream-box PIL true-ink scan + spill scan + orphan scan (my script)

Script: `cream_spill_orphan.py` (adapted from it-en proof2's copy: ED repointed to
it-pt; footer check looks for "Página"/"Pagina" instead of "Page").
Uses `occlusion_audit.ink_box` true ink; 29 cream rects `#f0eee5` across P1–P7;
P8 has 0 cream rects.
- Text nodes scanned: P1 173, P2 179, P3 177, P4 172, P5 171, P6 193, P7 161, P8 380.
- CREAM-X flags: **0**. CREAM-Y flags: 0. SPILL-PAGE flags: 0 (no ink outside
  1950×2700). SPILL-FOOTER flags: 0 (no ink below y=2580 outside furniture).
- ORPHAN flags: **3**, all adjudicated NOT defects — each node is byte-identical
  (same text, same x/y) in the core SVGs:
  P6 "18." at 1603.5/641.6; P8 "due" at 538.5/818.975; P8 Q137 "___" at
  773.3/1187.825. Frozen Italian text, inherited wraps. See PROOF-NOTE.md O-9.
  Log: `cream-spill-orphan.log`.

## 7b. Raster box-title measurement (delivered print render, 96 dpi)

Script: `raster_titles2.py` (v1 `raster_titles.py` is preserved in scratch but
superseded: its unrestricted x-window caught other columns' ink at the same
baseline — e.g. P1 cifre band read to x=1837 — and is not used for any verdict).
v2 restricts the raster x-window to the title's own column
`[title_x−10, box_right+150]` and measures all 38 bold ≥21 px titles inside
cream rects, cross-checked with PIL true ink. Log: `raster-titles2.log`.
- **37 fit, 1 apparent overflow adjudicated not-an-overflow** (P6 MINIME, see
  PROOF-NOTE.md U-2): the title's own PIL ink ends 538.2 (422.8 px spare); the
  raster 1111 reading is the neighbouring PROPOSTA box's title on the same
  baseline y=1634, starting x=1011. Node byte-identical to the core.
- En-analogue titles: P1 cifre PIL 924.5 vs box 961.0 (fits 36.5 px, raster 922);
  P2 frase PIL 934.0 vs 961.0 (fits 27.0 px, raster 933); P7 errori PIL 1721.5 vs
  1862.0 (fits 140.5 px, raster 1719). Tightest in the edition: P7 LA PAROLA
  1845.0 vs 1862.0 (fits 17.0 px, raster 1846).
- Crops (2×, from the delivered print render): `pages/crop-p1-cifre.png`,
  `pages/crop-p2-frase.png`, `pages/crop-p7-errori.png`, `pages/crop-p6-minime.png`.

## 8. Text-layer consistency (print vs web PDF)

- `pdftotext -layout` on both PDFs → word multiset identical, 7965 words each,
  char multiset equal, 0 diffs. Both extract 106,577 bytes.
  (KIT §7's "45,804 text bytes" is a different measure, presumably without
  -layout; my figure is the -layout extraction, identical for both PDFs.)
- Web PDF 1,294,408 bytes < 7 MB, real text layer. Web P1 and P8 rendered
  (`pages/web-p1-1.png`, `pages/web-p8-8.png`) and viewed: identical to print,
  no tofu.

## 9. p8.py extract + compare (canonical tool) + third-source key check

- `tools/p8.py extract --p8 svg/p8-valutazione.svg --total 150` → noted 150/150, RC=0.
- `tools/p8.py compare --core-p8 core-it/svg/p8-valutazione.svg --edition-p8 …` →
  status CLEAN, keydiff **[137, 138, 139]** (expected re-aimed reader-sentence
  keys; verified by hand: 137 "Para a Madonna della Salute, as pessoas atravessam
  a ponte votiva.", 138 "No domingo à noite, a Atalanta joga contra o Inter.",
  139 "No sábado, a Lazio joga em casa contra o Lecce."; 140 "Ogni cifra deve
  essere chiara." is the Italian sentence in both, so no diff — correct behaviour).
- Third source (my own check): SVG-printed P8 keys (from `pt/p8-extract.json`,
  150 keys) vs `.text.md` RISPOSTE answers — 149/150 exact; the single difference
  is Q150, whose printed "key" is the ✓ marker by design (the text.md answer is
  the note "Texto modelo na secção H abaixo (99 palavras)"). The exercise side and
  the answer side of P8 are therefore consistent with each other as well as with
  the core.

## 10. gates.py copy re-run (20/20 PASS)

Copied `gates.py` + `translations.py` + `validate_edition_textmd.py` from
`scratch-fanout-it/` into my scratch, repointed SCRATCH at my dir, ran with the
tools venv python against the shipped edition. Log: `gates-pt.log`.
FIRST run failed 3 gates (`p8 extract noted count`, `p8 compare vs core`,
`freeze diff report present`) because `gates.py` writes its JSON outputs to
`$SCRATCH/pt/`, which did not exist in my fresh scratch — `p8.py --json` exits 1
when the directory is missing. That was a harness artifact, not an edition
failure (my direct runs in §§5/9 had already passed with JSON written to existing
paths). After `mkdir -p $SCRATCH/pt`, the re-run is **20 PASS, 0 FAIL**:
occlusion 0 flags · p8 extract noted 150 · p8 compare CLEAN keydiffs [137,138,139] ·
freeze diff 0 unexplained · freeze diff report present (pages 1–8) · freeze
strict-cjk (only U+3000 ×8, rc=1 as in en — the tool exits 1 when reporting the
exempt U+3000) · print/web text multiset identical (7965/7965 words, chars equal) ·
web < 7 MB · print size sane · P8 min font 13.0 px · paper #fbfaf6 present ·
no gold/brick/near-black · VOL.5 only in the 3 legitimate nodes · VOL.4 count 9 ·
badge colours present · no double outer frame (0 full-page rects) · textmd validate
forward-miss 0 / reverse-miss 0 · answers 150/150 · keys 1–150 match core
(except 137–139 + writing) · notes match translations.py (except 137–140 +
writing). Final line: "GATES ALL PASS".

## 11. §1.1 scans (from gates.py + proofer's own)

- Paper `#fbfaf6` present; bad colours `#c9a227/#b8860b/#8b4513/#a0522d/#1a1a1a/#000000/#d4af37` — 0 hits.
- VOL.4 count 9 across SVGs; VOL.5 = 3 text nodes only (P2 cross-reference,
  P7 LETTERE disclosure, P7 next-week preview — same 3 as the core).
- Badge colours A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f` present.
- No double outer frame: 0 full-page rects.
- P8 min font: 13.0 SVG px = 9.75 pt (SOP §1.1 floor, exactly at floor).
- "·" total in SVGs: 148 (core pattern: options/gloss lists only).
- P8 chip check (my own): Q113–120, Q145–149 and the writing item Q150 each carry
  a B1 badge (23 B1 badge texts on P8; no missing badge among the checked set).
  Q141–144 use the range header "141–144." plus item lines, as in the core.

## 12. Character scans

- `.text.md` CJK ideographs: **0**. U+3000 ×101, U+FF1A ×14.
- U+2019: 0 in all 8 SVGs and in `.text.md`; U+2018: 0.
- SVG CJK scan: 0 text-node CJK hits on all 8 pages; the only CJK string in any
  SVG is `三色蛾` inside the P1 moth-logo `<title>` metadata (also present in the core).
- Banned terms (Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu): 0 in `.text.md`.
- ABSTRACT.txt: 1 line, 411 chars, 0 ASCII double quotes, 0 CJK.
- English function-word scan of `.text.md`: 0 hits (see PROOF-NOTE.md U-1).

## 13. Title count (measured, not assumed)

- Article headlines: 6 (P1–P6, listed in PROOF-NOTE.md).
- All-caps title/furniture lines in `.text.md` by my stated rule (line ≥3 chars,
  ≥70% of its letters uppercase): 95.
- Page sections: 8 `##` headings + 1 answer-key section (RISPOSTE).
- The string "56" occurs only twice in `.text.md` (exercise 56, stem + key).
  No element of this edition counts 56 — "56 titles" is a phantom number.

## 14. Visual read (fresh renders, proofer's own)

- `pdftoppm -r 96` the delivered print PDF → `pages/p-1.png` … `pages/p-8.png`
  (1950×2700 each), all 8 viewed. Web P1/P8 viewed (see gate 8).
- Results: P1 — clean (cifre title inside its box; masthead band flush left, glyphs
  complete); P2 — clean (frase title inside its box); P3 — clean (core-pattern
  mid-page whitespace); P4 — clean (E TU box 2 lines + gloss, flush with the
  results table; results table clean); P5 — clean (core-pattern whitespace;
  IL PIANO box fits); P6 — clean (MINIME/PROPOSTA twin boxes clean, chart bars
  inside the box and proportional; inherited "18." orphan line); P7 — clean
  (errori title inside its box with 140 px spare; LETTERE disclosure 3 lines clear
  of the FRASI hline; 8 FRASI + VOL.5 preview clean); P8 — dense but legible,
  "Traduzir para português/italiano" labels correct, model text present, keys flow
  ends 2529/2552, no footer intrusion.
- No overflow, overlap, footer intrusion, or tofu anywhere.

## 15. Fact verification (web, 2026-11-11)

- Sinner won the 2025 ATP Finals — beat Alcaraz 7–6(4), 7–5, Turin, Nov 16,
  2025, retained title — confirmed (sportradar; bworldonline; supersport; TNT
  Sports; Boston Globe; tennistourtalk). "Vincitore del 2025" correct.
- Torino Film Festival 2026 = 44ª edizione, Tue Nov 24 – Wed Dec 2, 2026, 9 days
  — confirmed by the official regulation (torinofilmfest.org) and programme
  reporting (filmbunch; cineuropa; fred.fm).
- BookCity Milano 2026 = 15ª edizione, Nov 23–29, theme «Il senno sulla Luna»
  from Ariosto's *Orlando furioso*, opening Mon Nov 23 20:00 Teatro Dal Verme
  with Colson Whitehead (2× Pulitzer), 1,360 events; Edmund de Waal among the
  international guests — confirmed (illibraio.it; milanoweekend.it;
  sudovestmilano.it; libreriamo.it).
- Eurochocolate 32ª / Torrone 29ª: it-en proof2's 2026-11-11 web verifications
  stand; not re-litigated. Manovra anchors rest on the core KIT's stated
  independent verification, as in proof1.
- Weekdays (Europe/Rome `date`): Nov 6 Fri, Nov 9 Mon, Nov 12 Thu, Nov 15 Sun,
  Nov 16 Mon, Nov 17 Tue, Nov 19 Thu, Nov 20 Fri, Nov 21 Sat, Nov 22 Sun,
  Nov 23 Mon, Nov 24 Tue, Dec 2 Wed, Dec 6 Sun, Dec 31 Thu — all match the paper.
  MD11 days Fri 6 / Sat 7 / Sun 8 Nov 2026 confirmed.
- Arithmetic re-verified by hand (MD11 goals 24; Q85 13−11=2; Q86 6+7=13;
  Torrone 16 days / 3 weekends; Torino FF 9 days; BookCity 7 days; chart bars
  34 px/degree; model text 99 words counted by script).

## 16. Production integrity (end of work)

- `sha256sum -c prod-hashes-before.txt`: all 11 files OK (8 SVGs + print PDF +
  web PDF + text.md) — byte-identical to the pre-work hashes.
- `git status --porcelain -- production/2026-w47/2026-w47-it-pt/`: the edition
  dir shows as untracked (`??`, i.e. the re-fan-out build is not committed yet);
  no file modified. No commit, no push, no production file written at any point.
  The only production-adjacent writes were reads; every build/render output went
  to my scratch dir.
