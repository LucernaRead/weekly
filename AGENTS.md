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
  audit / insert / webpdf / cover_check / tables + README). Run it from
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

Each week has one image per target language. The image goes with that week's story in that target language.
The 12 covers share these 12 images. The site puts each image into that story's `data-image-slot` on every cover.

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

## Do not

- Do not change the frontmatter of a committed edition to "fix" history.
  When an edition has an error, use the production correction flow to make a new file.
  Then update `pdfBytes` / `pdfSha256` in the md and note the correction.
- Do not create a pair directory between Simplified and Traditional Chinese (zh-cn × zh-tw).
  Lint blocks it. Do not try to get around it.
- Do not put an edition's print PDF into `issues/`. A print cover is the exception: it goes into its cover directory under `covers/`.
