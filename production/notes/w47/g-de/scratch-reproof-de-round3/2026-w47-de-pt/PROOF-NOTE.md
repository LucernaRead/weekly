# W47 2026-w47-de-pt — round-3 independent reproof (PROOF-NOTE)

- Proofer: round-3 independent reproofer (fresh round; distinct from round-2 proofer 7877e6e8). This round's sole de worker: the reproofer.
- Reader language: Portuguese. Production dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-de-pt/`.
- Scope (SOP §8): full reproof of the post-fix-de-minor1 state — text.md full read, answers re-verified question by question, 8 pages viewed per edition, geometry/occlusion audit, shared tools only (`tools/venv/bin/python`).

## Conclusion

**(b) 1 finding (R3-F1 (shared)) — fixed by the reproofer, rebuilt, re-gated; post-fix state has zero issues.**

## Pre-fix verification (post-fix-de-minor1 state)

- Disk SHAs matched the coordinator table exactly: print `43afa6245ae1`, web `ce68d33381bd`.
- fix-de-minor1 items verified in text.md AND print PDF: C-1 (`zwei große Weihnachtsmärkte` ×2 leads, Q34 new stem + key `Weihnachtsmärkte`, Q80 new sentence), C-2 (1903 sentence `Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben.`).
- Text read: reader-layer diff vs core-de read in full (235 lines); all 150 answers re-verified against stems/keys.
- Visual: all 8 pages viewed (renders in `renders/`); pre-fix gates all green (verify TOTAL 150, p8 CLEAN keydiff [137, 138, 139, 150], occlusion 0 flags, boxtitle 0 DEFECT, spill 0 SPILL, edge 0 TOUCH / 0 NEAR, D5 census PASS, print/web multiset+bytes identical, scratch rebuild SHA-identical, head_check PASS 0 defects).

## Findings and fixes

### R3-F1 — `überkleben` orphan gloss, all 11 editions (SOP §8.1)

- After the C-2 fix, `überkleben` occurred ONLY in the P5 gloss line (text.md L585, `content56.py:23`), nowhere else in the text or print PDF (×1 per edition, verified in text.md and print).
- SOP §8.1: glossed words must genuinely occur in the text. The fix-de-minor1 worker left it deliberately ("the brief's fix is the sentence only; flagged to the coordinator") — the brief is not a standing decision, §8.1 is explicit.
- Fix: deleted the ` · überkleben …` segment from the P5 gloss in `content56.py:23` (gloss shortens by one entry; layout-safe). Re-exported text.md (diff vs pre-fix: exactly L585, 1 line). Rebuilt via `tools/run_build.py` + `tools/webpdf.py`; changed SVG: p5 only.

## Post-fix verification (this round, after the fix)

- Fix evidence: `überkleben` ×0 in all 11 content56.py sources, ×0 in all 11 text.md files, ×0 in all 11 print PDFs;
- Post-fix P5 re-rendered and viewed (`renders-fix/`): gloss ends cleanly after the `basteln` entry;
- Full gates re-run (logs in `fix-round3/gates/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 42 titles, 250 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal (none); spill 0 SPILL / 86 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; HEAD CHECK PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 0, added Latin strings 438; print/web text layers multiset-identical (39,876 non-space chars each), byte-identical; scratch rebuild SVG/PDF SHA-identical to production; pre/post print multiset differs ONLY by the intended swaps (RC=1 as expected).
- KIT updated: `WEEKLY-KIT.md` §5 Deliverables (new SHAs/sizes) + §7 fix-de-round3 entry (or §2/§13 per the edition's KIT layout). Not committed / not pushed (coordinator inserts).

## Post-fix deliverables (SHA-12)

- Print PDF: `23c1505097e1` (`Die-Lucerna-VOL4-de-pt.pdf`)
- Web PDF: `bda89b7b2180` (`Die-Lucerna-VOL4-de-pt-web.pdf`)
- Text export: see KIT §5 for the full sha256.

## Observations (not findings)

- O-R2-1 (carried): P1 number-box gloss drops the `20.30` time in ja/ko/ru/zh-tw; the time remains visible in the German sentence directly above — no information loss.
- O-R3-4: several P7 toolbox titles end flush at the box edge (e.g. core `　工具箱` +1.0px marginal); glyphs complete, no clipping; boxtitle gate records 0 DEFECT.

