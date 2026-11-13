# WEEKLY-KIT — 2026-W47 · nl → fr (French readers)

Dutch weekly newspaper for French readers. Target language Dutch (nl), reader
native language French (fr). VOL.4, issue 2026-11-16 – 2026-11-22. Target: 150
exercises (10/18/18/18/18/18/12/38 across pages 1–8); A2 46 / B1 73 / B2 31;
model essay 81 words.

## Source

Fan-out of the frozen Dutch core `production/2026-w47/core-nl/` (slug
`2026-w47-nl-zh-cn`). Dutch target text, facts, and answer keys are frozen; only
the explanation layer (glosses, notes, section subtitles, exercise type words)
was rewritten in French. No new trend research, no invented reader letters.

## Files delivered

- 8 SVGs (`svg/p1-voorpagina.svg` … `svg/p8-toets.svg`), 8 render cards (`cards/`)
- Print PDF: `De-Lucerna-VOL4-nl-fr.pdf` — 12,106,421 bytes,
  sha256 `08f57ec27d8698c54be0ef79024048fec737ed4aabbfa8be68c1bb04b26c5fad`
- Web PDF: `De-Lucerna-VOL4-nl-fr-web.pdf` — 1,538,511 bytes,
  sha256 `1b429a3ff61edb99348c4d29a790204565b07a173e966f340268af79b9c585bc`
  (via `tools/webpdf.py`, text layer pdftotext 46,769 B)
- Source export: `2026-w47-nl-fr.text.md` — 47,744 bytes,
  sha256 `f1d1154442c4ea26fcc71dcf605704ab76a3555a2568bff521f158d974b5bc1a`
  (142 single + 2 match headers + 8 match items = 150; 8 golden, 6 gloss)
- `ABSTRACT.txt` (French, one line, no ASCII double quotes)
- This KIT.

## Build record (final = build 4)

- `run.py` exit 0, TOTAL 150, **zero OVERFLOW / TOO WIDE warnings**.
  `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core);
  `flow[P8-keys] ended col 3/3 y=2550 (bottom 2560)` — flow cursor only; last
  ink baseline ~2533, ink bottom ~2537, 59 px above the footer rule (y=2596).
- `render.py` exit 0; `webpdf.py` exit 0 (< 7 MB).
- Gates (build 4): **ALL PASS** — occlusion 0 flags; p8 extract 150/150;
  p8 compare CLEAN, 0 key diffs; freeze direct sha256 8/8; print/web text
  posdiff 0 msdiff 0 on all 8 pages (P1 819/819 … P8 2436/2436); pdftotext
  print 46,820 B / web 46,821 B; P8 answer-zone min font 10.12 pt
  (median 10.12); P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit
  clean (off-palette {}, VOL.5 = 5 = core, paper fills 8).
- Visual: all 8 cards viewed, clean. P1 numbers box fits col 1; P6 chart head
  "DONNÉES FICTIVES" fits; P7 BRIEVEN box ends above the ZINNEN rule;
  P8 answers 1–150 complete, pen photo with caption.

## Fixes vs the generated fan-out (explanation layer only)

1. P1 subtitle → 36 pt, spacing 2 (W46 fr; 1584 px < 1818 px limit).
2. Numbers-box title → "DE WEEK IN CIJFERS　EN CHIFFRES" (400 px).
3. Numbers-box items shortened ([2,1,2,3], total 384 px): item 3
   "(8 points : égalité en tête)", item 4 "(5 déc. : dans 19 jours)".
4. P6 chart head → "DE GRAFIEK　DONNÉES FICTIVES" (390 px).
5. P2 box title → "ZO ONTHOUD JE HET　À RETENIR".
6. P7 BRIEVEN glosses shortened to telegraphic W46 style (g1 2 lines, g2 2 lines;
   VOL.5 reference kept so the §1.1 VOL.5 count stays 5 = core).
7. **P1-headline overflow (build 1, new defect class, 9th)**: the numbers box
   jumped to col 2 and the flow ended at 1942 (114 px past 1828). Cause: the
   French P1 bridge is 4 lines (20.5 pt) and the box (384 px) no longer fit in
   col 1 (bridge ends y≈1441, box needs 396, i.e. 8.7 px short). Fix:
   numbers item 4 "(5 déc. : Pakjesavond, dans 19 jours)" → "(5 déc. : dans
   19 jours)" (3→2 lines, box 357 px) — the box fits col 1 again and the flow
   ends at 1465, exactly as the core. Mechanic: each exercise's real advance
   is 15.5 px more than Flow._fit assumes (hh + size − 4), so the tail cannot
   absorb a jumped box; the box must stay in col 1.
8. **P8-keys overflow (build 1→3, 30 px past bottom; #150 was drawn clamped
   past the footer)**: shortened 4 answer notes in col 3, each measured to drop
   from 2 lines to 1 (13.5 pt serif, 422.5 px): #131 "Carotte et liste de
   souhaits dans sa chaussure", #133 note "S + V + temps", #136 note "Sujet +
   verbe + objet", #139 note "Ordinal 88e". Keys untouched. Flow ends 2550.
9. **P1 agenda gloss** (class from de): single unwrapped p.text ran off the
   page edge (514 px) → "Toutes les dates et heures : pages 2 à 5." (343 px).
10. **P1 agenda sub-head** (class 10th): "Agenda van de week　LES RENDEZ-VOUS
    DE LA SEMAINE" (503 px, off-page) → "LES RENDEZ-VOUS" (364 px). Same
    class pre-fixed in es ("CITAS SEMANALES"), it ("GLI APPUNTAMENTI"), pt
    ("OS COMPROMISSOS").
11. **P1 IN DEZE EDITIE head** (class 11th): "IN DEZE EDITIE　DANS CE NUMÉRO"
    (412.3 px, past the box edge) → "CE NUMÉRO" (341.7 px). Same class
    pre-fixed in es ("ESTE NÚMERO"), it ("L'EDIZIONE"), ru ("В ВЫПУСКЕ").
12. **Re-fanout fix2 (2026-11-11, proof1 D1/D2/D4):** P7 `HET WOORD　LE MOT DE LA
    SEMAINE` (+21.6px over) → `HET WOORD　MOT DE LA SEMAINE` (+10.5 clearance,
    chosen over the proof's `LE MOT` to preserve meaning; verified 3 ways:
    PIL + built-SVG ink + visual crop); P6 `VOOR OF TEGEN?　POUR OU CONTRE?`
    (+0.8) → `POUR OU CONTRE` (+14.5). 8× U+2019 → U+0027 (content7.py 4,
    content8.py 4) — post-build sweep: U+2018/U+2019/U+201C/U+201D = 0 in
    `content*.py`, `svg/`, `.text.md`, both PDF text layers.
13. **Re-fanout fix2 D3:** P2 D-set option c → `"eten voor Sinterklaas' paard"`
    (core fix2 short form); clearance +71.9px.
14. **Re-fanout fix2 D5:** P4 HET PROGRAMMA box gained `"Stand Eredivisie na 12
    ronden: PSV 26, Feyenoord 25, Ajax 25 punten."` (5th fact, after Speelronde
    12, before Speelronde 13); box +73px.

## Notes

- The French P1 bridge stays 4 lines ("Notes — … · het verlanglijstje liste
  de souhaits.") — the box fix (item 7) leaves 8.7 px of margin without
  dropping a bridge gloss.
- HET WOORD gloss on P1 stays 2 lines; ends above the row-B rule (y=1853),
  occlusion clean.
- The curly apostrophe U+2019 renders with a visible gap before "s" in card
  PNGs — same quirk as the core, not a defect.

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 5)

Rebuilt from the fixed core (D3 + D5 + D4 export + proof1 fixes §Fixes 12–14). Build only — no commit, no push. Logs: `hidden_files/w47/scratch-refanout-nl/` — `fr-build.log`, `fr-check.log`, `fr-creambox.log`, review `fr-review/` (p1–p8 + crops).

- D3 short form in P2, clearance +71.9px (x+adv 1790.1); D5 standings line in P4 box + text.md; D4 142 `— Réponse:` + 8 `(Réponse x)`, 答案 0; italic print=web=1.
- text.md diff vs build 4: exactly 19 changed lines (D3 2 + D5 1 + P6 title 2 + P7 title 2 + 6 curly-quote line-pairs) — no unintended changes.
- Gates (build 5): TOTAL 150, by page 10/18/18/18/18/18/12/38, zero OVERFLOW / TOO WIDE; occlusion 0; p8 extract 150/150, compare CLEAN; freeze 8/8; print/web text posdiff 0, msdiff 0, all 8 pages (tokens 819/824/722/725/799/739/944/2436); pdftotext 46,862 B both; P8 font min=median 10.12pt, spans 187; chips core=edition {A2:8, B1:24, B2:3}; §1.1 clean.
- Creambox: 3 flags, all adjudicated non-overflow: P1 CREAM-RIGHT on the numbers-box title `DE WEEK IN CIJFERS　EN CHIFFRES` (right 956.5 vs rect 961.0 — ink inside the box, 4.5px clearance; the flag is the checker's 8px warning band only, visually confirmed in-box); P2 CREAM-BOTTOM `'rédaction.'` and P5 CREAM-BOTTOM `'envoie-les.'` both pixel-probed 0 dark pixels in the 7px strip below the box bottom (2px-margin rule only). 0 true overflow.
- 8-page visual pass: P1–P8 clean (P6 `POUR OU CONTRE` and P7 `MOT DE LA SEMAINE` in their boxes; P4 box with new standings line; straight apostrophes in `l'Allemagne` / `c'est` / `qu'ils`; P7 BRIEVEN ends above the ZINNEN rule; P8 answers 1–150 complete).
- Known core item NOT in this build: core-nl re-proof (post-fix2) found D6/D7 — a Chinese full stop `。` orphaned alone on its own line on core P3 and P7. Core fix3 is being done by another agent; this edition gets a separate incremental rebuild then. This build is against core HEAD `5de7492f` only.
- Note (Q140, recorded not fixed): fr Q140 source `Je fais une surprise avec un petit poème.` carries `petit`, but the key `Ik maak een surprise met een gedicht.` (copied from core `content8.py:75`) omits `kort` — the same key-vs-source mismatch the es proof caught as D6. Per coordinator instruction (2026-11-11 12:45 EST) only es was corrected; the core key would need a core-level fix to correct all 7 affected editions at once.

## Delta (core fix3 + fix4 + fix5, 2026-11-11, build 6)

Core-nl fix3 (D6/D7) + fix4 (D8/D9/D10) + fix5 (D11) synced to this edition, in the canonical path `production/2026-w47/2026-w47-nl-fr/` (copied `cp -a` from staging `fanout-nl/2026-w47-nl-fr/`, `diff -r` identical; staging untouched). Build only — no commit, no push. Logs: `hidden_files/w47/scratch-delta-nl-fr/` (DELTA-LOG.md, width-scan, gates, crops, 8-page renders). Old SHAs (build 5, history): print `50d9182b…aca544` / 12,656,012 B; web `9e90d0ab…84e4` / 1,612,638 B; text.md `21888192…e7c9` / 47,739 B.

- Pre-fix verdicts (measured, not assumed): D6/D7/D8/D10 did **not** exist in this edition — pre-fix orphan sweep 0/0 on all 8 pages (both classes, PIL + svglib advances, 1,458 lines; brute-force 0). Their sync is **structural**: `w` mechanism + w recomputed from this edition's French text by `wrap()` width scan (core numbers never copied); rebuilt p3/p6/p7 SVGs are byte-identical to pre-fix, proving the breaks are unchanged. D9 and D11 were **true defects**.
- Width scan (0.1px steps, identical-wrap band, midpoint): D6 bridge `w=430.4` (band 410.8–450.0); D7 gloss `w=433.45` (419.2–447.7); D8 `capcn_w=382.25` (359.7–404.8); D10 `dt_zh_w=408.75` (367.5–450.0). `bslib4.py` gained the core fix3 `w` parameter on `Flow.para`/`Flow.bridge`.
- D9 (true fix): `content8.py:75` key `Ik maak een surprise met een gedicht.` → `… met een kort gedicht.`; note unchanged. Three-source consistency verified: registry key = text.md:415 answer = P8 node; text.md:72 (`kort is ook goed`) and the French stem (`avec un petit poème`) both support `kort`. text.md diff vs build 5 is exactly line 415 (+5 B).
- D11 (true fix): `content34.py:130` top reserve 62 → 89 (= 16 pad + 52 title block + 21 para y-offset; this edition's render loop has the identical shape). Facts wrap 3/3/3/2/3 = 14 lines; box 611.0 → 638.0, bottom 1202.6 → 1229.6; last line `18:45 uur.` baseline 1209.49, margin **+20.11px** (≥20px); true ink lowest row 1209, clearance +20.6px; 7px strip below the box: 0 non-paper pixels.
- SVG changes vs build 5: **only `p4-sport.svg` (D11) and `p8-toets.svg` (D9)**; the other 6 are byte-identical.
- Gates (build 6): `run.py` rc=0, TOTAL 150, by page 10/18/18/18/18/18/12/38, zero OVERFLOW / TOO WIDE; occlusion 0 flags (real audit); p8 extract 150/150; p8 compare CLEAN, keydiff [137, 138] (translation keys, by design — core Chinese vs French; pre-fix keydiff was [137, 138, 140], D9 removed 140); 3-way compare 149/149 MATCH (Q150 open-writing exception; match keys 25–28 = d/c/a/b, 141–144 = b/c/d/a); freeze core-standard 8/8; in-edition freeze 8/8; print/web text posdiff 0, msdiff 0 all 8 pages (tokens 819/824/722/725/799/739/944/2437; P8 +1 = `kort`); pdftotext print = web = 46,867 B; P8 answer-zone min font 10.12pt, spans 187; chips core=edition {A2:8, B1:24, B2:3}; §1.1 clean. Orphan sweep post-fix 0/0 (pre and post identical). Creambox: same 3 pre-existing flags as build 5 (P1 RIGHT, P2/P5 BOTTOM), all pixel-probed false positives (strip 0 non-paper pixels; true-ink clearances P1 +9.0 / P2 +6.8 / P5 +7.5px); **true overflow 0**. Spill sweep 0 spills (P4 box has no below hit). Print-text diff vs build 5 is exactly the Q140 `kort` line. 8 pages viewed clean; crops for all six points confirmed by eye.

## D5 rebuild (2026-11-12, B档 — explanation-layer Latin rendered in Noto Sans CJK instead of Newsreader; REDO in top-level production)

- **Why a redo:** the first D5 worker (2026-11-12, `scratch-d5-rebuild-nl/`) rebuilt the `fanout-nl/` COPY, not this top-level production dir, and deleted its build-copy — production still held pre-D5 PDFs (print `6aedb91f…`, web `81d4fc19…`). This redo rebuilt from the current top-level build-6 sources in place. The copy's D5 SHAs (print `06838646…` / 12,106,426 B) are superseded and do NOT describe production.
- **Pre-D5 baseline (top-level, verified on disk, `scratch-d5-redo-nl/2026-w47-nl-fr/baseline.txt`):** svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `6aedb91fdc857b2ae545795b490c10b95400925ab1f430c658ca34922fd92d47` / 12,656,006 B; web `81d4fc195b008be1ec35d7fe5ec31e4c591fd796d54730c410857843f0c1793b` / 1,612,631 B (KIT §Files delivered recorded a different web SHA `4f78d3a7…` — pre-existing drift, web rebuilt after KIT written); text `f1d1154442c4ea26fcc71dcf605704ab76a3555a2568bff521f158d974b5bc1a` / 47,744 B. Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production by the build-6 sh=89 port), boxtitle 0 DEFECT, edge 0; census FAIL 500 Latin-in-CJK-sans. `run.py` pre-run reproduced the on-disk SVGs 8/8 byte-identical.
- **Install:** mechanism `apply_variant.py --target nl --reader fr` (mode latin), svglib md5 `78fdfbb037538b1f8a738434ea90a782` → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.
- **Ported core fixes (already in production before this rebuild):** P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` (core fix5 D11). P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt applied in this rebuild (core-nl D5 defect, same line here).
- **Defects found by the gates (all D5-caused, same class: bold-caps box titles widen in Newsreader SemiBold) — conclusions reused from the first worker's copy build, re-verified on the top-level rebuild; all fixed by size only, text unchanged:**
  1. P1 `DE WEEK IN CIJFERS　EN CHIFFRES` +44.2px → `f.box` tsize 23 → 20 (`content12.py:43`). Also fixed the P1 TEXTX overlap with `'wedstrijden.'` 16.5×4.8px.
  2. P2 `ZO ONTHOUD JE HET　À RETENIR` +20.0px → `f.box` tsize 23 → 21 (`content12.py:177`).
  3. P6 `DE GRAFIEK　DONNÉES FICTIVES` +42.6px → 24 → 21pt (`content56.py:149`).
  4. P6 `VOOR OF TEGEN?　POUR OU CONTRE` +24.1px → 21 → 19pt (`content56.py:169`).
  5. P7 `PAS OP!　CLINIQUE DES ERREURS` +21.1px → 23 → 21pt (`content7.py:73`).
  6. P7 `HET WOORD　MOT DE LA SEMAINE` +44.1px → 23 → 20pt (`content7.py:84`).
- **Gates (final rebuild, after the 6 fixes, all in top-level production):** `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`head_check.py` PASS 0 defects); `render.py` / `webpdf.py` RC 0; `p8.py extract` 150/150, `compare` vs core-nl CLEAN, keydiff=[137, 138] (reader-language keys, expected); `freeze.py baseline` 8/8 byte-identical; `freeze.py diff` vs core-nl: added CJK 7 (all U+3000); vs pre-D5 baseline: added CJK 0, added Latin strings 242 (run-splitting, expected); `occlusion_audit.py` 0 flags; `spill_sweep.py` 0 SPILL (38 OBSERVE); `boxtitle_check.py` 0 DEFECT; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` PASS 0 defects (P8 lines 215 → 215, footer slack 37.6px unchanged); `d5_census.py` PASS — D5 Latin 0, Cyrillic 0, curly-in-CJK 0; `census_quotes.py` 0 defective; text layer print = web = 46,769 bytes, word multiset diff 0; orphan sweep (a) 0, (b) 0.
- **New SHAs (lowercase, verified on production files):** print `08f57ec27d8698c54be0ef79024048fec737ed4aabbfa8be68c1bb04b26c5fad` (12,106,421 B); web `7e2f0989d641c4f6daa83f9f4698747810ab7f7e9ee9a588a38d9208eb362126` (1,538,515 B). **text.md unchanged:** 47,744 B, sha256 `f1d1154442c4ea26fcc71dcf605704ab76a3555a2568bff521f158d974b5bc1a`, byte-identical to the pre-D5 baseline.
- **Repro check (2026-11-12, third worker):** re-running `render.py` + `webpdf.py` in place reproduced the print PDF byte-identically (SHA unchanged); the web PDF rebuilt with a new SHA `1b429a3ff61edb99348c4d29a790204565b07a173e966f340268af79b9c585bc` (1,538,511 B) — content-equivalent (pdftotext 46,769 B, identical; `textlayer.py` re-run RC 0, word multiset diff 0). Only embedded-font `head`-table checksums differ (stream-level diff on nl-de: 70 bytes in 18/126 streams). Web PDF SHA is not reproducible run to run (see build-7 note); "Files delivered" above is re-synced to the new production file; the SHA on the "New SHAs" line above is the rebuild's original output, kept as history (was `7e2f0989d641c4f6daa83f9f4698747810ab7f7e9ee9a588a38d9208eb362126`, 1,538,515 B).
- **Files changed (not committed, not pushed, no `lint.mjs --write`):** `svglib.py` (D5 install), `content12.py` (P2 head 25 → 23pt; 2 title sizes), `content56.py` (P6 titles 24 → 21pt, 21 → 19pt), `content7.py` (P7 titles 23 → 21pt, 23 → 20pt), `WEEKLY-KIT.md` (sizes + this section). Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-fr/` (`rebuild-1.log`, `run.log`, `render.log`, `webpdf.log`, `routing.log`, `post/` gates + `post.txt`, `pre/` pre-D5 gates, `baseline.txt`).
