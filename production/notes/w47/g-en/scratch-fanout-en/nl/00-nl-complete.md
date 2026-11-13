# nl — COMPLETE, self-check zero issues (2026-11-11)

- Edition: `production/2026-w47/2026-w47-en-nl/` (slug `2026-w47-en-nl`)
- Print PDF: `The-Lucerna-VOL4-en-nl.pdf`, 29,340,703 bytes,
  SHA-256 `5b2a364b60fb55372e2ceada5e19b48cbdaa6e14b3ef8872d6e75322eff18e05`
- Web PDF: `The-Lucerna-VOL4-en-nl.web.pdf`, 2,375,438 bytes,
  SHA-256 `f1d2b8f43600e39af4aa1677db61f84820bef07ee9b826828e28704c55a9d94c`
- Gates: run exit 0, 0 overflow (all flows within bottom; P8-keys 2375/2560); occlusion 0 flags;
  p8 extract 60/150, compare CLEAN (keydiff 137–140, 150, expected); freeze direct sha256 8/8;
  print/web text diff 0/0; P8 min font 13.5 pt; badges = core on all 8 pages; text.md
  52,965 bytes, 150/150 keys; 8 cards visually checked after the final render, zero issues.
- Fix in this round (→ rebuild + re-render + full re-gate): P2 SENATE box title
  "THE SENATE, IN NUMBERS　De Senaat" (text_w 413.0) overflowed its box and ended 6pt from the
  column-3 line "Second story of the week" — the occlusion audit does NOT flag title-to-neighbour
  text collisions (0 flags throughout). Shortened to "…　Senaat" (gap now 39pt, pixel-verified).
  Standing lesson: text_w under-measures U+3000 titles by ~15pt (true ink 428.5 vs text_w 413.0);
  pixel-check any title facing live text in the next column; shorten pre-emptively.
  Note: es's SENATE title (411.4pt) has the same ~6pt tightness and was left as "tight but no
  collision" — flagged here for the parent, not re-opened (es is complete).
- Full record: the edition WEEKLY-KIT.md §5/§10.
