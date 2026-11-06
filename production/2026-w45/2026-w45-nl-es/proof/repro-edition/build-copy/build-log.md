# NL x ES W45 — build log summary
- Baseline: unmodified core-build copy reproduced shipped core SVGs 8/8 byte-identical
  (re-established from isolated scratch copy; core SVGs verified untouched at end of build).
- Transform: transform_es.py (exact quoted-literal replacements, per-string assertions) + 2 manual
  instr fixes in content8 (Traducir/Escribir) + P6 title shortenings (width-measured).
- Fix-0: P1/P2 flow overflow shortenings (see KIT §8). Pre-render sha: build-log-before-rerender-sha256.txt.
- Fix-1: P1 wordnote + P7 PAS OP/BRIEVEN shortenings (see KIT §8). Pre-render sha: build-log-before-fix1-sha256.txt.
- Final run: build-log-fix1.txt — zero FLOW OVERFLOW / HEAD TOO WIDE; 150 ex; A2 47/B1 72/B2 31;
  pages 10/18/18/18/18/18/12/38; model words 87.
- Render: render.py (tools venv) — cards 1950x2700 x8; print PDF 7,917,403 B; web PDF 3,680,221 B.
- Gates: occlusion 0/0/0 (occlusion-fix1.txt); freeze diff added CJK 0 (freeze-diff.txt);
  p8 CLEAN 150=150, keydiff adjudicated (p8-compare.txt); gloss 5/5 match; golden 8x2 with labels;
  rowcheck same-baseline flags = core-identical 8 (rowcheck-out.txt); chart clearance 4px x4.
- Full logs: build-log.txt, build-log-fix1.txt, gates-out.txt, p8-core.txt, p8-ed.txt.
