# W45 English core VOL.2 — FIX ROUND 2 (builder fix log, 2026-10-26)

Fixes exactly the 2 NEW problems in the round-2 independent proof report
(`hidden_files/w45/en-core-independent-proof2.md`), which had verified all
11 round-1 fixes. No other content was changed: the 11 round-1 fixes stay
exactly as they are; no new articles, no new facts, no lead/image/credit/
ABSTRACT changes, no rewording beyond what each fix needs. ABSTRACT.txt is
untouched. No git push, no Discord, no messages sent. This log does NOT
self-certify finalization — a fresh full independent proof round (round 3)
is still required.

Dates re-verified with `date -d` before fixing: November 3, 2026 is a
Tuesday; November 7, 2026 is a Saturday; November 8, 2026 is a Sunday.

Build code edited (only these two lines):
`hidden_files/weekly-report-w45-en-build/content7.py` (fix 1),
`hidden_files/weekly-report-w45-en-build/content56.py` (fix 2).

## The 2 fixes

1. **P7 B2 column, false page-6 attribution for "whether" (proof2 problem 1).**
   Was: "« Nobody knows whether the race is called yet. » Whether
   introduces an open question inside a sentence — more elegant than if,
   and safe everywhere. It is the word of the deep read (page 6)."
   Now: "…and safe everywhere. It is the word for election-night
   uncertainty." The false attribution is deleted, not moved: "whether"
   occurs zero times on page 6 (re-verified by grep of the P6 SVG, before
   and after the fix), so no other page could truthfully take the pointer.
   Dependency check: no exercise or note depends on the attribution.
   P8 Q125/Q136 and the P7 toolbox B2 sentence use "whether" as teaching
   material with no page claim, and are untouched. The P7 B2 EXAMPLE box's
   "(page 6)" for the Patience sentence is a different, true attribution
   (that sentence is verbatim from page 6) and is untouched.

2. **P5 SATURDAY SPORT box, Saturday framed as before the Tuesday vote
   (proof2 problem 2).**
   Was: "Before Tuesday, there is Saturday : MLS fixtures on November 7,
   including Charlotte against Inter Miami and Atlanta against the New
   York Red Bulls. The weekend warms up before the vote."
   Now: "After Tuesday, the weekend keeps going : MLS fixtures on
   Saturday, November 7, including Charlotte against Inter Miami and
   Atlanta against the New York Red Bulls. The weekend warms up for
   Sunday's games." Fixtures and dates are unchanged (they were correct);
   only the temporal framing changed, and it now matches P4, which frames
   the same November 7 Saturday as the warm-up ("On Saturday, November 7,
   the warm-up is already on … The weekend starts on Saturday — and it
   does not stop."). No other page mentions the P5 box's framing, and no
   exercise depends on it.

## Re-render + gates (final render, all 8 pages)

- Full re-render: 8 SVG + 8 PNG (1950×2700) + `The-Lucerna-VOL2.pdf`
  (8 pages, 31,114,501 bytes) + `The-Lucerna-VOL2-web.pdf` (8 pages,
  3,712,305 bytes).
- Build warnings: **zero FLOW OVERFLOW / HEAD TOO WIDE** (full build
  log `/tmp/en45-build2.log` grepped). Flow ends unchanged except the two
  fixed columns: P7-B2 ends y=988 (bottom 1150); P5-col3 ends y=1213
  (bottom 2540); P8 battery still ends y=1483 (bottom 1485) and P8 keys
  still end y=2535 (bottom 2545) — the round-1 P8 fix is untouched.
- Exercises: **150** (numbering 1–150, per-page 10/17/18/18/18/18/12/39
  unchanged).
- Builder re-read of the two changed pages, from the rendered output:
  P5 PNG read in full — the SATURDAY SPORT box prints the new framing
  cleanly, with clear space below and no crowding; P7 PNG read in full —
  the B2 column prints "It is the word for election-night uncertainty."
  cleanly, with no overflow into the EXAMPLE box. Tag-stripped SVG-text
  extraction confirms both new wordings present and both old wordings
  absent from the whole issue ("word of the deep read", "Before Tuesday",
  "warms up before the vote" — zero occurrences in all 8 SVGs).
- Occlusion audit (`tools/occlusion_audit.py`, selftest first):
  selftest OK (all 6 planted classes fired, clean controls silent);
  edition run **0 flags** on the final render (output saved to
  `hidden_files/w45/en-core-fix2-occlusion.txt`).
- Nothing else changed: lead, images, credits, ABSTRACT.txt untouched;
  no git push, no Discord, no messages.

## Not done here (for the parent to order)

Fresh full independent proof round 3 over the re-rendered issue. This
fix log does not certify finalization.
