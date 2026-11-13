# fr — COMPLETE, self-check zero issues (2026-11-11)

- Edition: `production/2026-w47/2026-w47-en-fr/` (slug `2026-w47-en-fr`)
- Print PDF: `The-Lucerna-VOL4-en-fr.pdf`, 29,330,444 bytes,
  SHA-256 `14da9810fa348a577d16927d90c7c2c05e67c537c533266ff81860486b7c11a5`
- Web PDF: `The-Lucerna-VOL4-en-fr.web.pdf`, 2,376,712 bytes,
  SHA-256 `0f188504a65e13488a5e07c2591c9ea9fa6f2adb0b5c0b2c3719797b8d7e22c3`
- Gates: run exit 0, 0 overflow; occlusion 0 flags; p8 extract 60/150, compare CLEAN
  (keydiff only 137–140, 150, expected); freeze direct sha256 8/8; print/web text diff 0/0;
  P8 min font 13.5 pt; badges = core on all 8 pages; text.md 53,239 bytes, 150/150 keys;
  8 cards visually checked after the final render, zero issues.
- Fixes in this round (each → rebuild + re-render + full re-gate): (1) P7 HEAD TOO WIDE ×3
  — ERROR CLINIC/READERS' CORNER/AN EXAMPLE LETTER French subs shortened; (2) P2 FLOW
  OVERFLOW ×2 — calendar box → full-French short form, bridges A/B shortened;
  (3) occlusion 5 flags (P1 COVER midterm para, P2 LINEX SENATE title, P4 EDGE SATURDAY,
  P5 TEXTX ODD SOCKS, P6 EDGE HOW LONG) + 3 proactive box-title shortenings;
  (4) "Note | Note |" doubling 11× in gloss boxes — stripped the prefix from the 11 gloss
  translations (kept on the P1 bridge, which uses f.bridge); (5) U+2019 full-width gap —
  SC sans face gives U+2019 a 1.0em advance, so every French elision rendered with a ~19 px
  gap; core uses ASCII apostrophe only (0× U+2019), so build_map.py now normalizes
  U+2019 → ' for all editions (fr content now 0× U+2019; P3 bridge gaps re-measured 8–10 px).
- Full record: `scratch-fanout-en/fr/00-fr-complete.md` (and the edition WEEKLY-KIT.md §8).
- Tools built this round (reusable for es–zh-tw): `build_map.py` (TM + miss-tr + fresh +
  meta → map, with poison rejection and U+2019 normalization), `fr/gates.sh`,
  `check_s11.py` (§1.1 + P8 checks, also re-validated de RC=0), `fr/make_textmd_w47.py`.
- Standing lessons for the remaining 8: TM-reuse wording errors (SAY IT, bridges) recur —
  verify every reused TM string against the W47 content; box titles are single-line (measure
  with text_w at 23pt vs 386.5 inner width; only ink collision/page overflow is a failure);
  check each language's gloss() prepend vs its W46 gloss-arg convention before translating
  gloss lines; French-length languages overflow P2 first.
