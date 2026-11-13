# W47 Cover Report — 2026-W47 (issue 2026-11-16–22, VOL.4)

Status: complete. Generated 2026-11-13. Single source of truth:
`production/covers/2026-w47/cover.json`; blocks regenerated with
`node tools/cover.mjs 2026-w47` (exit 0, 12/12 blocks written).

## Blocks — 12/12

One block per reader language: de, en, es, fr, it, ja, ko, nl, pt, ru,
zh-cn, zh-tw. Each block: masthead + plain date + the same 12 stories
in the same order, with the reader-language headline, excerpt, teasers,
captions, alt text and weekly word.

## Images — 60/60 stills

- 60 still images (WebP, valid header, decode, dimensions): 12 lead
  pictures (3:2, ≥800 px wide) + 48 secondary pictures (more[1]/more[2]
  1:1, more[3]/more[5] 3:2).
- 9 stills were regenerated in this round (de-3, es, fr, ja-5, ko-2,
  ko, ru, zh-cn, zh-tw); all 60 match their production sources.
- No duplicates, no missing images, no placeholders. Every image
  corresponds to real content inside its weekly PDF.

## Motion — intentionally stills-only this week

`covers/2026-w47/motion/` does not exist, by decision: this week
ships with still images only. Lint passes without it (motion is
optional; it blocks neither lint nor insertion). Motions follow after
insertion, one image per commit, same pattern as the W43/W45/W46
secondary motions (motion.sh + the frame counts in
tools/motion-durations.json, pairwise-coprime per visible set).

## Captions / alt text — lead images rewritten

The 6 lead images' caption and alt text were rewritten from the old
generic captions (e.g. "A parcel locker in a hallway") to
image-specific text in all 12 reader languages — 144 strings, all
within the cover limits (caption ≤30 cjk / ≤34 ko / ≤38 other;
alt ≤60 cjk / ≤70 ko / ≤150 other). Old generic captions are gone
from cover.json and from all 12 blocks.

Secondary images (de-3, ja-5, ko-2) have no caption/alt slot in the
cover schema, so their rewritten captions were not applied; they are
kept with the caption work for a future schema change.

## Page audit — 84/84

All 12 stories × 7 guide pages anchor to the real pages of the
weekly PDFs, in the same order, in every language version.

## Weekly word

de family word is "Totensonntag" (page 6, verified in the PDF).

## Open items (KIT wave 2, not cover-blocking)

- ja-ru §8 stale values; ko-ru "Output files + sizes" stale;
  nl W-1–W-5 several §7 SHA stale / missing text SHA;
  zh-tw-ru KIT L35 typo; HEADS-NOTE acceptance records to add.
- KIT F8 advance 422.72 → 426.14 (update the number in wave 2).
