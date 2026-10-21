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
The directory name is the edition's identifier:

```
issues/2026-w43-fr-zh-cn/
  2026-w43-fr-zh-cn.md    ← metadata (frontmatter) + a short intro
  2026-w43-fr-zh-cn.pdf   ← the full issue, web PDF
```

Slug rule: `<week lowercase>-<target>-<native>`. Language codes:
`en` `de` `fr` `es` `it` `pt` `nl` `ru` `ja` `ko` `zh-cn` `zh-tw`.

Each `.md` opens with frontmatter — `title`, `excerpt`, `publishedAt`, `week`,
`weekStart`/`weekEnd`, `vol`, `masthead`, `target`/`targetName`/`targetLabel`,
`native`/`nativeName`/`nativeLabel`, `exercises`, `pages`, `pdf`, `pdfBytes`,
`pdfSha256`, `discordThread`, `draft` — and the lint gate enforces that every
field is present.

## Three hard rules

`node lint.mjs` blocks violations, and so does CI:

1. **One level only** — no subdirectories inside an edition directory, and
   nothing in it except `<slug>.md` and `<slug>.pdf`.
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
consumers. If you edit an `.md` and forget `--write`, the default mode
compares and fails: a drifted index would silently show stale data.

## PDFs

The web PDF is the archived artifact; the print PDF is not kept here (size).
Because each PDF's size and SHA-256 are pinned in the frontmatter and in
`index.json`, any copy of a PDF can be verified against the index, wherever
it was downloaded from.

## Branches

`main` is the only long-lived branch.
