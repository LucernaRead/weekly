# it-en — edition record (build4, 2026-11-11)

## Deliverables
- `production/2026-w47/2026-w47-it-en/La-Lucerna-VOL4-EN.pdf` — 14,032,990 bytes, sha256 `d41e7255d7da8ea63cf07560911a518b2e55a4a7d8a9eb8b0f3c1ae6d3129e2f`
- `La-Lucerna-VOL4-EN-web.pdf` — 1,259,104 bytes, sha256 `32a6727966cfa130618c64356cd9db9812f04cbc96e961ff1534b143580e5903`
- `2026-w47-it-en.text.md` — 55,286 bytes, 1317 lines, 150 exercises
- `ABSTRACT.txt`, `WEEKLY-KIT.md` (both in the edition dir)
- 8 SVG + 8 cards in `svg/` / `cards/`

## Builds
- build1 (prev. runner): P1-headline FLOW OVERFLOW fixed at source (cifre items shortened); rebuild clean, P1-headline ends 1362.
- build2 (prev. runner): gates found 2 occlusion flags (P4 E TU 52% covered; P7 disclosure crossed by FRASI hline) + gates.py filename bug + U+3000 strict-cjk issue.
- build3 (this runner, 01:31 UTC): 4 fixes applied (P4 E TU line; 3 P7 error notes; gates.py filename + U+3000 exemption) — all grep-verified before the run; run/render/webpdf rc 0, 150 ex. Gates then showed 1 remaining LINEX (disclosure last line baseline 1696.32 crossing the y=1686 hline; col3 ended 1702.0) + 3 gates.py bugs (p8 extract key, p8 compare verdict key, "no VOL.5" over-strict, textmd duplicate kwarg, vacuous freeze check, notes-equality check wrong for fan-out).
- build4 (this runner, 01:38 UTC): disclosure shortened 4 → 3 wrapped lines (translations.py:986 + content7.py:100/106); P7 col3 ends 1673.0; gates ALL PASS (gates5.log).

## Gates (gates5.log, ALL PASS)
occlusion 0; p8 extract 150/150, compare CLEAN (keydiff 137–139 only); freeze fragments 0 unexplained; freeze baseline sha256 8/8; strict-cjk 13 × U+3000 only; print/web multiset identical 7,945 words; web 1,259,104 < 7MB; P8 min 13.0px = 9.75pt; §1.1 scans pass; VOL.5 = 3 legitimate nodes; textmd 0/0; keys match (except 137–139 + writing); notes match translations.py (9 frozen notes exempted).

## Self-checks
- P8 chips: Q113–120, Q145–149, Q150 all B1, = core 1:1.
- Visual 8/8 cards: zero defects.
- Full self-read of .text.md (1317 lines): only CJK is the deliberate 「翻译」 label (Q137–140); English explanation layer throughout; keys re-verified.
- ABSTRACT: EN one line, no ASCII double quotes, contains刊名/目标语/A2–B2/150题.

## Tool fixes made this shift (scratch gates.py only)
See STATUS.md top section. Shared tools (tools/p8.py, tools/freeze.py, tools/occlusion_audit.py) NOT modified.

---

## Re-fan-out (2026-11-11)
- Rebuilt from core-it fix3 (36bdec2e) by build_edition.py, RC=0 first attempt; text.md 55,221 bytes, 1317 lines, 150 exercises.
- Gates: 20/20 PASS, 0 FAIL (`scratch-refanout-it/gates-en.log`); P8-keys flow ends y=2514 (bottom 2552); freeze baseline re-taken 8/8 (this dir's baseline is the re-fan-out one; first-fan-out baseline preserved in `scratch-refanout-it/prev-fanout/en/`).
- fix3 9 lines + E labels + table values verified by `scratch-refanout-it/check_refanout.py` (ALL PASS); sim cross-check 0 unexpected changes.
- KIT updated with the new SHAs + §11 (see the edition dir). Full report: `scratch-refanout-it/FANOUT-REPORT-it.md`.
