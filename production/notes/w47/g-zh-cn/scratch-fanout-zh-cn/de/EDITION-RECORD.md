# EDITION-RECORD — 2026-w47-zh-cn-de (German explanations)

## Verdict

**COMPLETE — all gates green on the final files.** Builder handoff, NOT a
finalisation claim: independent proofreading is still owed by the parent
line. No commit, no push, no insert, no lint run by this builder.

## Final artifacts

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-DE.pdf` (print) | 44,829,975 | `e6ed50ab8eedb82c249aee9a9ce5e6ed61d0b06bc2060c79c9cdb94957ac424b` |
| `Lucerna-VOL4-DE-web.pdf` (web) | 2,732,464 | `7fb396f13ece42b771beb722811e4ab8df8bb2f9971cf2380e3f06d7e83535e5` |
| `2026-w47-zh-cn-de.text.md` | 50,637 | `8940ba88e92d70eb6d54e4759657d187b451e259b1633bb92f9d475e97075b0a` |
| `ABSTRACT.txt` | 305 | matches `tables.py` ABSTRACT['de'] |

## Audit of the #2 handoff (#3, 2026-11-11 12:32 UTC)

Coordinator's 12:30 UTC disk reading verified exactly:

| File | Handoff bytes / SHA | Match |
|---|---|---|
| print PDF | 44,831,669 / `0f93280d79730b21effc15415b7f4fa330c9d54ee2d311c5c0734680d8f65a60` | yes |
| web PDF | 2,736,660 / `a5caf2fbb6ea1fabfa18eb69a8d0c311cd902f10f839c03de897c737b97ba368` | yes |
| text.md | 50,680 / `505d817ab7a89021db97cf3fe9ef21d4b7cdad63b04e3068fcd21d754e7c5d99` | yes |

Handoff verdict: **NOT qualified as-is** —

1. Print PDF (08:51) predates the P7 teaser fix (`content7.py` 08:54,
   pitch 120 → 112): the rendered P7 band ended at 2615.3, crossing the
   footer rule (2596) and the footer text. Evidence: file mtimes +
   run-de-7.log (teaser 2583.3) vs render-de-5.log (08:51).
2. Web PDF (08:42) predates the P2/P7 fixes and was built with the
   pre-patch `webpdf.py` (italic-face fix is commit 40963281, 09:39 UTC):
   no Newsreader-Italic face subset. Text.md (08:42) still contains the
   superseded “Diese Woche im Kalender” (×1) and lacks “Kalender der
   Woche”.
3. SVG on disk was final (08:55, run-de-7 RC=0 TOTAL 150, 0 overflow).
4. **Badge strict-CJK failure:** `freeze.py diff --strict-cjk` on the
   handoff SVG: TOTAL added CJK = 1 (`德` × 1, P1 badge “德语讲解”).
   SOP requires 0 for zh-target editions with a Latin/Cyrillic
   explanation layer; W46 zh-cn-de KIT records the same failure mode and
   the Latin-only badge fix. Fixed in this round (see below).

## Fixes applied in #3

1. Badge: `fresh.py` badge entry → Latin-only for de/fr/es/it/pt/nl/ru
   (the Latin halves verbatim), W46 wordings for ja/ko (separators
   `·` → U+3000 per SOP §1.1); regenerated `tables.py`
   (`gen_tables-3.log`: 276 ENTRIES, 0 missing, 0 extra, 0 unconsumed).
   De edition `content12.py:24` badge now “CHINESISCHER TEXT　ERKLÄRUNGEN
   AUF DEUTSCH”. Only p1 SVG changed (p2–p8 byte-identical).
2. Synced the 3 de value fixes #2 made in edition files but not in the
   table (`fresh.py` + `gen_tables.py` re-run; diff = exactly those 3
   de lines): press-time short line “Finale offen”, calendar title
   “Kalender der Woche”, gloss “die letzten vier Teams” (no
   “, die Halbfinalisten”). Table now reproduces this edition exactly.
3. Full rebuild from the final sources: `run.py` → `render.py` →
   `webpdf.py` (patched) → `export_de.py`. New SHAs above.
4. `WEEKLY-KIT.md` rewritten for de (was an untranslated copy of the
   core KIT, pairing zh-cn × en).

## Gates (final files)

`gates-zhcn.py` (`gates-de-9.log`): **11/11 PASS, OVERALL ALL PASS.**

| Gate | Result |
|---|---|
| occlusion | rc=0, 0 flags (selftest OK) |
| img_overlap | 0 hits |
| p8_extract | 150/150 |
| p8_compare | CLEAN, keydiffs 0 |
| freeze_sha256 | run rc=0, match 8/8 |
| print_web_text | 8/8 pages, posdiff 0, msdiff 0 (P1 356/356 … P8 1706/1706) |
| pdftotext_nonempty | print 44,739 B, web 44,739 B |
| p8_fontsize | answer-zone min 9.98 pt, median 9.98 pt (≥ 9.75) |
| p8_chips | A2 11 / B1 24 / B2 3 = core |
| u2019 | 0 files |
| s11_svg | off-palette {}, no gold, 0 stroked rects, VOL.5 = core (1), paper #fbfaf6 × 8 |

Plus: `run.py` RC=0 TOTAL 150 (A2 56 / B1 69 / B2 25; pages
10/18/18/18/18/18/12/38), 0 overflow; `freeze.py baseline` core 8/8
byte-identical (venv Pillow 13.0.0 / FreeType 2.14.3, core integrity
confirmed); `freeze.py diff --strict-cjk` TOTAL added CJK **0**, exit 0
(`freeze-diff-de-9.log`); leak scan over all 275 translate sources vs
final SVG + text.md: **0 real leaks** (`leak-de-9.log` — “体育　Sport”
is a covered entry whose German rendering is identically “Sport”; the
welcome line is the documented EXCLUDE).

## 150-key verification

- `p8.py extract --total 150`: noted set = 150 of 150, keys 1–150 all
  present (`p8-extract-de-9.json`).
- `p8.py compare` core vs edition: **CLEAN**, missing=[], extra=[],
  uncertain=[], keydiff=[] (`p8compare-de-9.json`). Keys 137–140
  (7.77 / 14 / GEN / 冷) print identically to the core by design; E-group
  keys are the option letters with German notes.
- Registry: `run.py` TOTAL 150, same level/page/type split as the core.

## Visual

- P1: badge Latin-only on the masthead rule, moth clear; press-time
  “Finale offen” visible; welcome line flows col 1 → col 2. PASS.
- P2: “Kalender der Woche” fully visible, 21 px clear of the valley
  photo; “Übungsbeispiel　练习例子” fits. PASS.
- P4: Hinweise box 6 lines, bottom clear of “GEN，” below. PASS.
- P7: teaser band ends 2583.3, clear of footer; image ends 1889.3. PASS.
- P8: test sections A–F (113–150), keys with “— Seite N —” separators,
  photo + credit, footer clear. PASS.
- P3/P5/P6: unchanged since #2's visual pass (byte-identical SVGs).

## Logs (this dir)

`run-de-9.log`, `render-de-9.log`, `webpdf-de-9.log`, `export-de-9.log`,
`gates-de-9.log`, `gates-de-9.json`, `freeze-diff-de-9.log`,
`freeze-diff-de-9.json`, `freeze-de-8.log` (baseline), `leak-de-9.log`,
`p8-extract-de-9.json`, `p8compare-de-9.json`, `svg-sha-before-rebuild.txt`.
#2's logs retained alongside (`run-de-7.log`, `render-de-5.log`, …).
