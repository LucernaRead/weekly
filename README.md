# weekly

The content repository for **Lucerna Weekly**, Lucerna's multilingual weekly
newspaper for language learners. **Content only, no code** — every published
edition is archived here, and the site and community tools read `index.json`
plus each edition's metadata from this repo at runtime.

## One edition = one directory

An edition is one **target language × reader's native language** pairing:
target-language text with all explanations written in the reader's language.
With 12 target languages × 11 native languages the full grid is ~130 editions
per week (the two cross-script Chinese pairings do not exist — see rule 2).
Editions live under a **week directory** — the week itself is one level —
and the directory name is the edition's identifier:

```
issues/2026-w43/2026-w43-fr-zh-cn/
  2026-w43-fr-zh-cn.md       ← metadata (frontmatter) + a short intro
  2026-w43-fr-zh-cn.pdf      ← the full issue, web PDF
  2026-w43-fr-zh-cn.text.md  ← the full issue as markdown (optional; the site renders it)
```

Slug rule: `<week lowercase>-<target>-<native>`. Language codes:
`en` `de` `fr` `es` `it` `pt` `nl` `ru` `ja` `ko` `zh-cn` `zh-tw`.

Each `.md` opens with frontmatter — `title`, `excerpt`, `abstract`,
`publishedAt`, `week`, `weekStart`/`weekEnd`, `vol`, `masthead`,
`target`/`targetName`/`targetLabel`, `native`/`nativeName`/`nativeLabel`,
`exercises`, `pages`, `pdf`, `pdfBytes`, `pdfSha256`, `discordThread`,
`draft` — and the lint gate enforces that every field is present.

## Abstracts

Every edition carries an **abstract**: a short summary of the issue, written
in the reader's native language, naming the week's actual topics (events,
festivals, matches) and the phrases learners search for. It lives twice in
each `.md` — as the frontmatter `abstract` field (also copied into
`index.json`, so listings and page descriptions can use it verbatim) and as
a visible section in the body under the edition's own word for "abstract".
Abstracts exist so search engines can match an edition to what learners are
actually looking for that week; a generic description repeated across 130
editions cannot do that. The field has been required by the gate since
2026-10-22, and the W43 editions were backfilled with theirs the same day.
An abstract states only what the issue contains — topics come from the
edition itself, never from a template.

## Three hard rules

`node lint.mjs` blocks violations, and so does CI:

1. **Two fixed levels** — `issues/` holds only week directories
   (`2026-w43`), a week directory holds only edition directories, an edition
   directory holds nothing but `<slug>.md`, `<slug>.pdf` and the optional
   `<slug>.text.md`, and every edition sits under its own week.
2. **Legal pairings only** — target ≠ native, both from the 12-language list,
   and never Simplified ↔ Traditional Chinese as target/native of each other
   (they are two scripts of one language; nobody learns one as a foreign
   language from the other).
3. **The PDF must match its declaration byte for byte** — the frontmatter
   pins the PDF's byte size and SHA-256; if the file in the repo differs in
   size or hash, the gate fails.

## The gate and the index

`lint.mjs` is both the structural validator and the index generator
(zero-dependency Node):

```bash
node lint.mjs                 # validate + check that index.json is up to date (CI mode)
node lint.mjs --write         # validate + regenerate index.json (run after adding an edition)
node lint.mjs --require-pdf   # additionally require every edition's PDF to be present and intact
```

`index.json` is the one file consumers read to render a listing: with it, a
listing costs a single upstream request; without it, every edition's `.md`
would have to be fetched individually (and the unauthenticated GitHub API
allows only 60 requests/hour/IP). Sort order is fixed in the gate — week
descending, then target language, then native language — never left to
consumers. The index also carries a `covers` section — one static HTML
cover block per week per language — so the site can locate each week's
cover without scanning the tree. Each entry carries the block's byte size
and SHA-256 (computed from the file by the gate), so the site can verify
its copy. A cover block has no links; its `<body data-story-langs="…">`
names the target language of each `<article>` in document order, and the
site turns each story into a link to that language's edition (see
AGENTS.md, "加封面"). If you edit an `.md` and forget `--write`, the default mode
compares and fails: a drifted index would silently show stale data.

## PDFs

The web PDF is the archived artifact; the print PDF is not kept here (size).
Because each PDF's size and SHA-256 are pinned in the frontmatter and in
`index.json`, any copy of a PDF can be verified against the index, wherever
it was downloaded from.

## Branches

`main` is the only long-lived branch.
