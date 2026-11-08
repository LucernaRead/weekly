# Weekly content: agent guide

## Before you start

- Read README.md first. This repo holds content only: edition metadata and PDFs. It holds no site code.
- Add an edition only when it has passed the weekly SOP on the production side:
  one full independent proofreading round with zero findings, and a geometry-overlap audit with zero flags.
  Do not add an edition that has not passed.

## Production sources and tools

- `SOP.md` is the canonical production SOP for this weekly paper. It
  changes often; each weekly cycle pulls the latest version before
  starting. Do not work from memory or from a summary of it.
- `tools/` holds the shared production toolkit (freeze / p8 / occlusion
  audit / insert / webpdf / cover_check / tables + README; `cover.mjs` generates the website cover
  blocks from cover.json, `motion.sh` turns a video into a moving picture). Run the Python tools from
  the repo clone with the persistent venv `tools/venv/bin/python`
  (never `/tmp`). `tools/venv/` and `tools/scratch/` are gitignored and
  never committed. Every builder/proofreader MUST use these tools
  instead of hand-rolled equivalents; if a check is missing, extend
  the tool here.
- `production/` holds the per-edition sources: `production/<week>/<slug>/`
  (edition KIT + build code + ABSTRACT.txt + .text.md; rendered PDFs/
  SVGs/PNGs are NOT kept here — they are reproducible from the sources
  and the final web PDFs are already under `issues/`), `production/<week>/core-<target>/`
  (core build code), `production/production-matrix.md` (the 12×11 grid),
  `production/covers/<week>/` (teasers.json + cover build scripts), and
  `production/notes/` (audit records the SOP appendices cite).
- This repo holds content, the SOP, the toolkit and the production
  sources. It holds no site code.

## Add an edition

1. Create the directory `issues/<week, lowercase>/<week, lowercase>-<target>-<native>/`.
   Example: `issues/2026-w43/2026-w43-fr-zh-cn/`. The week is its own level.
2. Write `<slug>.md`. Give every frontmatter field in README. Do not omit a field.
   Measure `pdfBytes` and `pdfSha256` from the **final** web PDF. Write the SHA-256 in lowercase.
3. When you commit the PDF file, name it `<slug>.pdf` and put it in the same directory.
4. Body markdown: export the edition's body as `<slug>.text.md` into the same directory (lint rule 9).
   - The site renders this file as the edition page's body, for readers and for search engines.
     Without it, the site falls back to text extracted from the PDF. That text has a broken layout and starts collapsed.
   - Export it from the production source. Write titles, paragraphs and exercises in their original order.
     Do not extract it back from the PDF.
   - Do not commit an empty file. Lint writes its path, byte size and SHA-256 into the index field `text`.
5. Run `node lint.mjs --write`. Then run `node lint.mjs` and confirm it is green.
   Commit the generated index.json together with the md. **Do not edit index.json by hand.**
6. The commit hook regenerates the index. Do not skip it. Read `git diff` before you commit. Do not commit unrelated files.

## Add a cover

Each week has one website cover block per reader language.
A cover block is a snapshot of that week's 12 front pages, one per target language.
The site shows it at the top of the weekly page.
When a reader clicks a story, the site opens the edition for that target language, explained in the cover's reader language.

**The website cover is required (lint rule 11).** When a week holds all 130 editions, lint requires this week to have:
12 website cover blocks (`.html`, one per reader language) and 12 story images (one per target language).
If one is missing, lint fails. The commit hook and CI both block it.
The print cover (`.md` + PDF) is **not** a website cover block. The site reads only the `.html`.
Order: commit the cover blocks and the images first. Then commit the last batch of editions that completes the 130.

### From 2026-w46: write cover.json, generate the blocks (lint rule 14)

The site shows one target-language edition at a time as one newspaper front page (the NYT front-page grid).
You write the content in one file. A tool generates the 12 cover blocks. Lint checks the content and the blocks.

1. Write `production/covers/<week>/cover.json`. The shape is in the header of `tools/cover.mjs`.
   Write one entry per target language (12). Each entry has these fields:

   | Place on the page | Field | Language |
   |---|---|---|
   | lead headline | `headline` | target |
   | lead text (verbatim, whole sentences) | `excerpt` | target |
   | lead explanation | `teaser[reader]` | reader |
   | lead picture caption / screen-reader text | `caption[reader]` / `alt[reader]` | reader |
   | 6 secondary stories | `more[n].headline` / `more[n].summary[reader]` / `more[n].page` | target / reader / page number |
   | word of the week | `word.term` / `word.gloss[reader]` / `word.page` | target / reader / page number |
   | "inside this issue" | `pages` (titles of page 2 to the last page) | target |

   For reader = target, write the reader fields in the target language.
   Write `page` for every secondary story and for the word: the page of the edition PDF that item is on
   (an integer, 1 to the last page). The page number is required. Read it from the PDF page footer.
   The site sends a click on the item to that page of the edition. The lead is page 1, and
   "inside this issue" line i is page i + 2. Do not write a page for those two.
   SOP.md, Appendix 5, says how to write each field. Read it before you write.
2. Keep each field within its length limit. The limits are `LIMITS` in `tools/cover.mjs`.
   Count = Unicode characters after you remove all whitespace. Punctuation and digits count.
   The limits come from the site layout. Do not ask for a higher limit to fit a text. Write a shorter text.
3. Run `node tools/cover.mjs <week>`. It checks cover.json and writes the 12 `.html` files.
   It fails and writes nothing when a field is missing or too long.
4. Do not edit a generated `.html`. Lint renders each block again and fails on a difference of one byte.
   To change a block, change cover.json and run step 3 again.
5. Put the print cover in the same directory, as before (step 3 below).
6. Run `node lint.mjs --write`. Then run `node lint.mjs` and confirm it is green.

When content is not ready, put a placeholder text in the field (a short sentence in that language that says it is a placeholder).
Do not leave a field empty. Do not publish a week with placeholders.

### Before 2026-w46: hand-written blocks

Follow W45 (`covers/2026-w45/`): the lead story carries its image, and the other stories hold an image slot (`data-image-slot`).

1. Create the directory `covers/<week, lowercase>/<week, lowercase>-cover-<reader language>/`.
   Example: `covers/2026-w45/2026-w45-cover-en/`.
2. Put one `<directory name>.html` in it: a self-contained static cover block.
   - No interaction (lint rule 5): no scripts, buttons, links, forms, navigation, footer, sidebar or click handlers.
     The site adds the links. Do not write links into the cover block.
   - Write each story as one `<article>`. Write one story per target language, 12 in total.
   - Write `data-story-langs="…"` on `<body>` (lint rule 8).
     List the target language of each `<article>` in document order.
     Use the language codes from README, separated by spaces. Give each of the 12 exactly once.
     Example: `<body data-story-langs="de fr es en it pt nl ru ja ko zh-cn zh-tw">`.
     When the layout or the story order changes, change this line too.
     A wrong order sends the reader to the wrong edition.
   - For a story that gets an image, put `data-image-slot` on the placeholder element in that `<article>` (lint rule 10).
     Give the attribute no value. Lint derives the target language from the order in `data-story-langs`.
     Put at most one slot in each story. Do not put a slot outside an `<article>`.
     Example: `<div class="plate" data-image-slot aria-hidden="true"><span class="mast">La Lucerna</span></div>`.
     Write the placeholder's content as usual. The site shows it as is until the image exists.
3. Put the print cover in the same directory: `<directory name>.md` and one PDF. The site does not use it.
4. Run `node lint.mjs --write`. Then run `node lint.mjs` and confirm it is green.
   Lint writes the cover into `covers` in `index.json`: `slug`, `week`, `lang`, the `html` path,
   and the html's byte size and SHA-256 (computed from the file, never typed by hand).
   The site verifies the SHA-256. When you change one byte of a cover block, run `--write` again.
5. Commit the html and index.json. **Do not edit index.json by hand.**

## Add story images

Each week has one lead image per target language. The image goes with that week's lead story in that target language.
The 12 covers share these 12 images. The site puts each image into that story's picture place on every cover.

From 2026-w46, four secondary stories per target language also have a picture place (`MORE_IMAGES` in `tools/cover.mjs`):

| Story | Place on the page | Aspect | File |
|---|---|---|---|
| `more[1]`, `more[2]` | narrow column, small picture beside the text | 1:1, at least 400 px wide | `images/<target language>-1.webp`, `-2.webp` |
| `more[3]` | feature of the second group, above the headline | 3:2, at least 800 px wide | `images/<target language>-3.webp` |
| `more[5]` | rail story, above the headline | 3:2, at least 800 px wide | `images/<target language>-5.webp` |

A secondary picture is optional for lint. Without it, the site shows a placeholder in that place.
Make it from that secondary story's content, with the same rules as the lead image (no text in the image, WebP, ≤ 400 KB).

1. Read that target language's story (headline and summary) on any of that week's covers. Make an image from its content.
2. Image specification:
   - Landscape 3:2 (recommended 1200×800 px). The site crops the image to fill the slot.
     Each edge can lose a little. Keep the subject in the centre.
   - Put no text in the image. The 12 reader-language covers share the image, and text serves only one reader.
   - Format WebP, file ≤ 400 KB (counted in file bytes). If it is larger, compress it again at lower quality.
     Do not scale it below 800 px wide.
3. Save it as `covers/<week, lowercase>/images/<target language>.webp`. Example: `covers/2026-w45/images/it.webp`.
   Use only the language codes from README in the file name. Save one image per target language.
4. Run `node lint.mjs --write`. Then run `node lint.mjs` and confirm it is green.
   Lint writes the image into `coverImages` in `index.json`: `week`, `lang`, path, byte size, SHA-256.
5. Commit the image and index.json. Before the week has 130 editions, you can commit in batches.
   When the week has 130 editions, all 12 images must exist (lint rule 11).
6. To replace a committed image, overwrite the file with the same name. Then do step 4 again.
   The site fetches the new image by its SHA-256.

## Add a moving picture

A lead story can have a moving picture in place of its still image: a short silent loop, like a living photograph.
The site shows it with no controls. It plays in a loop. Readers who turned motion off in their system see the still image.

1. Cut the video to 2–15 seconds. Make the last frame meet the first frame, so the loop does not jump.
2. Run `sh tools/motion.sh <video file> <week> <target language>`.
   The tool writes `covers/<week>/motion/<target language>.webp`: an animated WebP, 1200×800, 12 frames per second.
   A WebP has no audio track, so the picture is always silent.
   The tool lowers the quality until the file is ≤ 4 MB.
3. Durations must be staggered: each language has a fixed prime frame count at 12 fps, so the 12 motions
   on one cover page never loop back in sync — en 89, de 97, fr 103, es 109, it 113, pt 127, nl 131,
   ru 137, ja 149, ko 157, zh-cn 167, zh-tw 179 (same language, same count, every week).
   `motion.sh` applies the count for the language automatically (a 4th argument overrides it).
   Lint rule 15 checks every pair of frame counts is coprime (SOP Appendix 5).
4. Keep the still image `covers/<week>/images/<target language>.webp`. Lint requires it (rule 15).
5. Run `node lint.mjs --write`. Then run `node lint.mjs` and confirm it is green.
   Lint checks rule 15: animated, loops forever, 3:2, at least 800 px wide, 2–15 s, ≤ 4 MB, pairwise-coprime frame counts.
6. Commit the file and index.json.

## Do not

- Do not change the frontmatter of a committed edition to "fix" history.
  When an edition has an error, use the production correction flow to make a new file.
  Then update `pdfBytes` / `pdfSha256` in the md and note the correction.
- Do not create a pair directory between Simplified and Traditional Chinese (zh-cn × zh-tw).
  Lint blocks it. Do not try to get around it.
- Do not put an edition's print PDF into `issues/`. A print cover is the exception: it goes into its cover directory under `covers/`.
