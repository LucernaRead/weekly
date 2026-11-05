#!/usr/bin/env node
/**
 * Structure gate **and index generator** for the Lucerna Weekly content repo. Zero dependencies: run `node lint.mjs`.
 *
 *     node lint.mjs                check, and check that index.json is current (CI mode, writes nothing)
 *     node lint.mjs --write        check, and write index.json (run this after you add an edition)
 *     node lint.mjs --require-pdf  also require every edition's PDF file to be in the repo (pre-release check)
 *
 * Why lint generates the index: consumers (the site, the community) fetch content from GitHub at run time.
 * Without an index, a listing must fetch every edition's md: upstream requests grow with the edition count,
 * and the unauthenticated GitHub API allows only 60 requests/hour/IP. With the index, a listing fetches 1 file.
 *
 * ⚠️ The index can **drift**: you change an md, forget --write, and the index keeps the old data with no error.
 * So the default mode compares the regenerated index with the committed index.json and fails on a difference.
 *
 * The repo has one shape, and this gate checks it:
 *
 *     issues/<week>/
 *       <slug>/
 *         <slug>.md      the edition's metadata (frontmatter) + a short introduction
 *         <slug>.pdf     the whole edition as a web PDF (file optional; see "PDFs" in README)
 *         <slug>.text.md the edition's body in markdown (optional; see rule 9)
 *
 * <week> is the week directory (lowercase, e.g. 2026-w43). It is its own level: find the week, then the edition.
 * slug = <week, lowercase>-<target>-<native>, e.g. 2026-w43-fr-zh-cn.
 *
 * The other shape is the website cover block. The site finds it through the index:
 *
 *     covers/<week>/
 *       <week>-cover-<lang>/
 *         <week>-cover-<lang>.html       static cover block (no interaction, see rule 5)
 *         <week>-cover-<lang>.md         print cover metadata (optional)
 *         cover-<week short>-<lang>.pdf  print cover PDF (optional)
 *       images/
 *         <target language>.webp         the image for that week's story in that target language (see rule 10)
 *
 * Cover blocks go into the index's covers section by week + language. Only a directory with a .html goes in.
 * The site locates covers by that section.
 *
 * Hard rules:
 *   1. **Two fixed levels** — issues/ holds only week directories; a week directory holds only edition directories;
 *      an edition directory holds no subdirectory; an edition sits in the directory of its own week.
 *   2. **Valid pairs** — target ≠ native; both languages are in the 12-language list;
 *      the two pairs between Simplified and Traditional Chinese **do not exist** (nobody learns a language that way).
 *   3. **Self-contained** — an edition directory holds only <slug>.md, <slug>.pdf and (optional) <slug>.text.md;
 *      the md frontmatter declares the PDF file name, byte size and SHA-256;
 *      when the PDF file is in the repo, it must match the declaration byte for byte
 *      (a hash mismatch means the file was replaced or damaged in transfer).
 *   4. **Text layer** — a PDF in an edition directory must carry an extractable text layer (pdftotext extracts text);
 *      an image-only PDF has no text layer, the site's SEO cannot read it, and it does not enter the repo.
 *   5. **No interaction in cover blocks** — no .html in the repo may contain interactive elements
 *      (scripts, buttons, links, forms, navigation, footer, sidebar, click handlers, etc.); keep static content only.
 *      With no .html in the repo, this rule passes and main stays green.
 *   6. **Excerpt in the target language** — for a non-Latin-script target (ru/ja/ko/zh-cn/zh-tw), an excerpt with
 *      too many ASCII letters (>50%) counts as an English excerpt in the wrong place and fails.
 *      Latin-script targets cannot be told apart by script, so they are not checked.
 *   7. **Cover blocks in the index** — each language directory under covers/ holds at most one .html,
 *      and its language is in the 12-language list. Only a directory with a .html enters the index
 *      (a directory with only the print md/pdf does not). The covers section is sorted week descending,
 *      then language in LANGS order. The site finds each week's cover per language by that section.
 *      Each entry carries a slug (the cover directory name) and the html's byte size and SHA-256
 *      (computed from the file). The site verifies its copy with them.
 *   8. **A cover block names each story's target language** — <body> carries data-story-langs="<lang> <lang> …",
 *      matching each <article> in document order: each of the 12 languages once, exactly 12 <article> elements.
 *      The site turns each story into a link to "learn this language, explained in this cover's reader language"
 *      (the cover block itself stays free of interaction).
 *   9. **Body md (optional)** — an edition directory may also hold <slug>.text.md: the edition's body in markdown.
 *      It must not be empty. When present, it enters the index field text (path, byte size, SHA-256, computed
 *      from the file); when absent, text is null. The site renders it as the edition page's body; without it,
 *      the site can use only text extracted from the PDF.
 *  10. **Story images** — a cover block reserves image places: put data-image-slot on the placeholder element
 *      inside an <article> (no value; rule 8's order gives its target language). At most one per story;
 *      none outside an <article>. The image goes in covers/<week>/images/<target language>.webp: one per target
 *      language, shared by the 12 covers; it must be WebP, non-empty, ≤ 400 KB (file bytes).
 *      It enters the index's coverImages (week, lang, path, byte size, SHA-256).
 *      The site fills each cover's slot for that story with the image; without an image the placeholder shows as is.
 *  11. **A complete week must have its website cover** — when a week's expected set (130 editions) is all present
 *      (not draft, PDF in the repo), covers/<week>/ must hold one cover block .html for each of the 12 reader
 *      languages, and images/ must hold one image for each of the 12 target languages.
 *      A print md/pdf does not count. Without them the site can show that week only as a list of cards.
 */
import { readdirSync, readFileSync, writeFileSync, existsSync, statSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join } from 'node:path';
import { createHash } from 'node:crypto';

/** The 12 languages (target and native use the same codes). This order is the sort order in the index. */
const LANGS = ['en', 'de', 'fr', 'es', 'it', 'pt', 'nl', 'ru', 'ja', 'ko', 'zh-cn', 'zh-tw'];
const ROOT_ALLOW = new Set([
  'issues', 'lint.mjs', 'index.json', 'README.md', 'AGENTS.md', 'CLAUDE.md',
  '.git', '.husky', 'package.json', 'package-lock.json', 'node_modules',
  '.github', '.gitignore', 'covers',
]);
const REQUIRED_FM = [
  'title', 'excerpt', 'abstract', 'publishedAt', 'week', 'weekStart', 'weekEnd', 'vol',
  'masthead', 'target', 'targetName', 'targetLabel', 'native', 'nativeName',
  'nativeLabel', 'exercises', 'pages', 'pdf', 'pdfBytes', 'pdfSha256',
  'discordThread', 'draft',
];
const SLUG_RE = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const WEEK_RE = /^\d{4}-w\d{2}$/;
const DATE_RE = /^\d{4}-\d{2}-\d{2}$/;
const SHA_RE = /^[0-9a-f]{64}$/;
const INDEX_FILE = 'index.json';

/** Non-Latin-script targets: their excerpt language can be judged by script. */
const NON_LATIN_TARGETS = new Set(['ru', 'ja', 'ko', 'zh-cn', 'zh-tw']);
/** Share of ASCII letters among all letters in an excerpt (digits and punctuation do not count). */
function asciiLetterFraction(s) {
  const letters = [...s].filter((c) => /\p{L}/u.test(c));
  if (!letters.length) return 0;
  const ascii = letters.filter((c) => c.charCodeAt(0) < 128).length;
  return ascii / letters.length;
}

const write = process.argv.includes('--write');
const requirePdf = process.argv.includes('--require-pdf');

const problems = [];
const fail = (where, msg) => problems.push(`${where}: ${msg}`);

/** Minimal frontmatter parser: reads only `key: value` (value may be quoted). Enough for checking and the index. */
function frontmatter(raw, where) {
  if (!raw.startsWith('---\n')) {
    fail(where, 'no frontmatter (the file must start with ---)');
    return null;
  }
  const end = raw.indexOf('\n---', 4);
  if (end === -1) {
    fail(where, 'frontmatter has no closing ---');
    return null;
  }
  const out = {};
  for (const line of raw.slice(4, end).split('\n')) {
    const m = line.match(/^([A-Za-z][A-Za-z0-9]*):\s*(.*)$/);
    if (!m) continue;
    let v = m[2].trim();
    if (v.startsWith('"') && v.endsWith('"')) v = v.slice(1, -1);
    out[m[1]] = v;
  }
  return out;
}

const root = process.cwd();

// Root allowlist
for (const name of readdirSync(root)) {
  if (!ROOT_ALLOW.has(name)) fail('repo root', `entry not allowed: ${name}`);
}

// No interaction in cover blocks: no .html in the repo may contain interactive elements; static content only.
// <a\b does not match <article>/<aside>; <link> is not <a>; <header> is allowed; cursor/:hover are not checked.
// With no .html this passes. The default mode enforces it; CI and the commit hook both run plain lint.
const INTERACTIVE_PATTERNS = [
  [/<script\b/i, '<script>'],
  [/<button\b/i, '<button>'],
  [/<a\b/i, '<a>'],
  [/<form\b/i, '<form>'],
  [/<input\b/i, '<input>'],
  [/<select\b/i, '<select>'],
  [/<textarea\b/i, '<textarea>'],
  [/<nav\b/i, '<nav>'],
  [/<footer\b/i, '<footer>'],
  [/<aside\b/i, '<aside>'],
  [/onclick\b/i, 'onclick'],
  [/addEventListener/i, 'addEventListener'],
  [/tabindex\s*=/i, 'tabindex'],
  [/role\s*=\s*["']button["']/i, 'role="button"'],
];
const SKIP_DIRS = new Set(['.git', 'node_modules']);
function scanHtml(dir, rel) {
  for (const name of readdirSync(dir).sort()) {
    const p = join(dir, name);
    const r = rel ? `${rel}/${name}` : name;
    if (statSync(p).isDirectory()) {
      if (!SKIP_DIRS.has(name)) scanHtml(p, r);
      continue;
    }
    if (!name.toLowerCase().endsWith('.html')) continue;
    let text;
    try {
      text = readFileSync(p, 'utf8');
    } catch {
      fail(r, 'cannot read the cover HTML');
      continue;
    }
    for (const [re, label] of INTERACTIVE_PATTERNS) {
      if (re.test(text)) {
        fail(r, `a cover block must not contain interactive elements (scripts, buttons, links, forms, navigation, footer, sidebar, click handlers, etc.); keep static content only (found ${label})`);
        break;
      }
    }
  }
}
scanHtml(root, '');

const issuesDir = join(root, 'issues');
if (!existsSync(issuesDir)) {
  fail('issues/', 'directory does not exist');
  report();
}

const editions = [];
const seenPairs = new Set();

for (const weekDirName of readdirSync(issuesDir).sort()) {
  const weekPath = join(issuesDir, weekDirName);
  if (!statSync(weekPath).isDirectory()) {
    fail(`issues/${weekDirName}`, 'issues/ holds only week directories');
    continue;
  }
  if (!WEEK_RE.test(weekDirName)) {
    fail(`issues/${weekDirName}`, 'a week directory name must be YYYY-wNN in lowercase (e.g. 2026-w43)');
  }

  for (const slug of readdirSync(weekPath).sort()) {
    const dir = join(weekPath, slug);
    const rel = `issues/${weekDirName}/${slug}`;
    if (!statSync(dir).isDirectory()) {
      fail(rel, 'a week directory holds only edition directories');
      continue;
    }
    if (!SLUG_RE.test(slug)) fail(rel, 'a slug uses only lowercase letters, digits and hyphens');
    if (!slug.startsWith(`${weekDirName}-`)) {
      fail(rel, `an edition must sit in the directory of its own week (the slug must start with ${weekDirName}-)`);
    }

    const files = readdirSync(dir);
    for (const f of files) {
      const p = join(dir, f);
      if (statSync(p).isDirectory()) fail(`${rel}/${f}`, 'an edition directory must not hold a subdirectory');
    }
    const mdName = `${slug}.md`;
    const pdfName = `${slug}.pdf`;
    const textName = `${slug}.text.md`;
    for (const f of files) {
      if (f !== mdName && f !== pdfName && f !== textName) {
        fail(rel, `extra file ${f} (only ${mdName}, ${pdfName} and ${textName} are allowed)`);
      }
    }
    if (!files.includes(mdName)) {
      fail(rel, `${mdName} is missing`);
      continue;
    }

    const where = `${rel}/${mdName}`;
    const fm = frontmatter(readFileSync(join(dir, mdName), 'utf8'), where);
    if (!fm) continue;

    for (const key of REQUIRED_FM) {
      if (!(key in fm) || fm[key] === '') fail(where, `frontmatter is missing ${key}`);
    }
    if (problems.length && fm.target === undefined) continue;

    // Pair rules
    const { target, native: nat } = fm;
    if (!LANGS.includes(target)) fail(where, `unknown target language ${target}`);
    if (!LANGS.includes(nat)) fail(where, `unknown native language ${nat}`);
    if (target === nat) fail(where, 'target and native language must differ');
    if ((target === 'zh-cn' && nat === 'zh-tw') || (target === 'zh-tw' && nat === 'zh-cn')) {
      fail(where, 'a Simplified/Traditional Chinese pair does not exist (they are two scripts of one language; nobody learns that way)');
    }
    const pair = `${fm.week}|${target}|${nat}`;
    if (seenPairs.has(pair)) fail(where, `duplicate pair: ${pair}`);
    seenPairs.add(pair);

    // The slug must follow from week + pair, so a directory name always parses
    const expectSlug = `${String(fm.week).toLowerCase()}-${target}-${nat}`;
    if (slug !== expectSlug) fail(where, `slug must be ${expectSlug}, found ${slug}`);

    // Field formats
    for (const d of ['publishedAt', 'weekStart', 'weekEnd']) {
      if (fm[d] && !DATE_RE.test(fm[d])) fail(where, `${d} must be YYYY-MM-DD`);
    }
    for (const n of ['vol', 'exercises', 'pages', 'pdfBytes']) {
      if (fm[n] !== undefined && !/^\d+$/.test(fm[n])) fail(where, `${n} must be an integer`);
    }
    if (fm.pdfSha256 && !SHA_RE.test(fm.pdfSha256)) fail(where, 'pdfSha256 must be 64 lowercase hex digits');
    if (fm.pdf && fm.pdf !== pdfName) fail(where, `the pdf field must be ${pdfName}`);

    // Excerpt language gate (conservative): only non-Latin-script targets, by share of ASCII letters.
    // Latin-script targets (de/fr/es/it/pt/nl/en) use Latin letters anyway and cannot be told from English, so they are not checked.
    if (NON_LATIN_TARGETS.has(target) && fm.excerpt && asciiLetterFraction(fm.excerpt) > 0.5) {
      fail(where, `the excerpt must be written in the target language ${target} (too many ASCII letters; it looks like an English excerpt)`);
    }

    // When the PDF file is in the repo, check it byte for byte (size + SHA-256)
    const pdfPath = join(dir, pdfName);
    const pdfInRepo = existsSync(pdfPath);
    if (pdfInRepo) {
      const data = readFileSync(pdfPath);
      if (data.length !== Number(fm.pdfBytes)) {
        fail(where, `PDF size mismatch: declared ${fm.pdfBytes}, actual ${data.length}`);
      }
      const sha = createHash('sha256').update(data).digest('hex');
      if (sha !== fm.pdfSha256) fail(where, 'the PDF SHA-256 does not match the frontmatter');
      // Text layer: only a PDF that pdftotext extracts text from has a text layer; an image-only PDF has none.
      // pdftotext comes with poppler (preinstalled on the ubuntu-latest runner); without it locally, fail loudly, never pass silently.
      try {
        const text = execFileSync('pdftotext', [pdfPath, '-'], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
        if (text.replace(/\s/g, '').length === 0) {
          fail(where, 'the PDF has no extractable text layer (image-only PDFs do not enter the repo; make the web PDF with webpdf.py first)');
        }
      } catch (e) {
        if (e.code === 'ENOENT') fail(where, 'the PDF text-layer check needs pdftotext (install poppler-utils, then run again)');
        else fail(where, `PDF text-layer check failed: ${e.message}`);
      }
    } else if (requirePdf) {
      fail(rel, 'the PDF file is not in the repo (--require-pdf)');
    }

    // Body md (rule 9, optional): when present it enters the index with byte size and SHA-256 (computed from the file);
    // the site renders it as the edition page's body.
    let text = null;
    if (files.includes(textName)) {
      const data = readFileSync(join(dir, textName));
      if (data.toString('utf8').trim().length === 0) fail(`${rel}/${textName}`, 'the body md is empty');
      text = {
        path: `${rel}/${textName}`,
        bytes: data.length,
        sha256: createHash('sha256').update(data).digest('hex'),
      };
    }

    editions.push({
      slug,
      title: fm.title,
      excerpt: fm.excerpt,
      abstract: fm.abstract,
      publishedAt: fm.publishedAt,
      week: fm.week,
      weekStart: fm.weekStart,
      weekEnd: fm.weekEnd,
      vol: Number(fm.vol),
      masthead: fm.masthead,
      target,
      targetName: fm.targetName,
      targetLabel: fm.targetLabel,
      native: nat,
      nativeName: fm.nativeName,
      nativeLabel: fm.nativeLabel,
      exercises: Number(fm.exercises),
      pages: Number(fm.pages),
      dir: rel,
      md: `${rel}/${mdName}`,
      pdf: `${rel}/${pdfName}`,
      pdfBytes: Number(fm.pdfBytes),
      pdfSha256: fm.pdfSha256,
      pdfInRepo,
      text,
      discordThread: fm.discordThread,
      draft: fm.draft === 'true',
    });
  }
}

// Cover blocks in the index: the site finds each week's cover per language by the covers section (rule 7).
// Shape covers/<week>/<week>-cover-<lang>/, at most one .html per language directory.
// A directory with only the print cover and no .html does not enter the index; rule 11 decides whether the week needs one.
const covers = [];
const coverImages = [];
const IMAGES_DIR = 'images';
const IMAGE_MAX_BYTES = 400 * 1024;
const IMAGE_SLOT_RE = /\sdata-image-slot\b/gi;
const coversDir = join(root, 'covers');
if (existsSync(coversDir)) {
  for (const weekDirName of readdirSync(coversDir).sort()) {
    const weekPath = join(coversDir, weekDirName);
    if (!statSync(weekPath).isDirectory()) {
      fail(`covers/${weekDirName}`, 'covers/ holds only week directories');
      continue;
    }
    if (!WEEK_RE.test(weekDirName)) {
      fail(`covers/${weekDirName}`, 'a week directory name must be YYYY-wNN in lowercase (e.g. 2026-w45)');
      continue;
    }
    for (const coverDirName of readdirSync(weekPath).sort()) {
      const dir = join(weekPath, coverDirName);
      const rel = `covers/${weekDirName}/${coverDirName}`;
      if (coverDirName === IMAGES_DIR) {
        collectCoverImages(dir, rel, weekDirName);
        continue;
      }
      if (!statSync(dir).isDirectory()) {
        fail(rel, 'a week directory holds only cover directories');
        continue;
      }
      const m = coverDirName.match(new RegExp(`^${weekDirName}-cover-(.+)$`));
      if (!m) {
        fail(rel, `a cover directory name must be ${weekDirName}-cover-<lang>`);
        continue;
      }
      const lang = m[1];
      if (!LANGS.includes(lang)) {
        fail(rel, `unknown language ${lang}`);
        continue;
      }
      const files = readdirSync(dir);
      const htmls = files.filter((f) => f.toLowerCase().endsWith('.html'));
      if (htmls.length === 0) continue; // print cover only: not in the index; rule 11 checks the week
      if (htmls.length > 1) {
        fail(rel, `a cover directory holds at most one .html, found ${htmls.length}`);
        continue;
      }
      const pdfs = files.filter((f) => f.toLowerCase().endsWith('.pdf'));
      if (pdfs.length > 1) {
        fail(rel, `a cover directory holds at most one PDF, found ${pdfs.length}`);
        continue;
      }
      const mdName = `${coverDirName}.md`;
      const htmlRel = `${rel}/${htmls[0]}`;
      const htmlData = readFileSync(join(dir, htmls[0]));
      checkStoryLangs(htmlData.toString('utf8'), htmlRel);
      checkImageSlots(htmlData.toString('utf8'), htmlRel);
      covers.push({
        slug: coverDirName,
        week: weekDirName,
        lang,
        dir: rel,
        html: htmlRel,
        htmlBytes: htmlData.length,
        htmlSha256: createHash('sha256').update(htmlData).digest('hex'),
        md: files.includes(mdName) ? `${rel}/${mdName}` : null,
        pdf: pdfs.length === 1 ? `${rel}/${pdfs[0]}` : null,
      });
    }
  }
}
/** Rule 8: <body data-story-langs> lists each of the 12 languages once, one per <article>, in document order. */
function checkStoryLangs(text, where) {
  const m = text.match(/<body\b[^>]*\sdata-story-langs\s*=\s*"([^"]*)"/i);
  if (!m) {
    fail(where, 'the cover block <body> has no data-story-langs (list the target language of each <article> in order; see AGENTS.md, "Add a cover")');
    return;
  }
  const langs = m[1].trim().split(/\s+/).filter(Boolean);
  const unknown = langs.filter((l) => !LANGS.includes(l));
  if (unknown.length) fail(where, `data-story-langs has unknown languages ${unknown.join(' ')}`);
  const missing = LANGS.filter((l) => !langs.includes(l));
  if (missing.length) fail(where, `data-story-langs is missing languages ${missing.join(' ')}`);
  if (new Set(langs).size !== langs.length) fail(where, 'data-story-langs has a duplicate language');
  const articles = (text.match(/<article\b/gi) ?? []).length;
  if (articles !== langs.length) {
    fail(where, `data-story-langs lists ${langs.length} languages but the cover block has ${articles} <article> elements; they must match one to one`);
  }
}

/** Rule 10: an image slot (data-image-slot) sits only inside an <article>, at most one per story. */
function checkImageSlots(text, where) {
  const [before, ...articles] = text.split(/<article\b/i);
  let stray = (before.match(IMAGE_SLOT_RE) ?? []).length;
  articles.forEach((chunk, i) => {
    const [inside, ...after] = chunk.split(/<\/article>/i);
    const n = (inside.match(IMAGE_SLOT_RE) ?? []).length;
    if (n > 1) fail(where, `<article> number ${i + 1} has ${n} data-image-slot attributes; at most one per story`);
    stray += (after.join('').match(IMAGE_SLOT_RE) ?? []).length;
  });
  if (stray) fail(where, `${stray} data-image-slot attributes are outside an <article>; an image slot must sit in its story`);
}

/** Rule 10: covers/<week>/images/<lang>.webp, at most one per target language (story), each ≤ IMAGE_MAX_BYTES. */
function collectCoverImages(dir, rel, week) {
  if (!statSync(dir).isDirectory()) {
    fail(rel, `${IMAGES_DIR} must be a directory`);
    return;
  }
  for (const name of readdirSync(dir).sort()) {
    const fileRel = `${rel}/${name}`;
    const m = name.match(/^(.+)\.webp$/);
    if (!m || !LANGS.includes(m[1])) {
      fail(fileRel, 'an image file name must be <target language>.webp (a language from the 12-language list, e.g. it.webp)');
      continue;
    }
    const data = readFileSync(join(dir, name));
    if (data.length === 0 || data.length > IMAGE_MAX_BYTES) {
      fail(fileRel, `image is ${data.length} bytes; it must be non-empty and ≤ ${IMAGE_MAX_BYTES} bytes`);
      continue;
    }
    if (data.subarray(0, 4).toString('latin1') !== 'RIFF' || data.subarray(8, 12).toString('latin1') !== 'WEBP') {
      fail(fileRel, 'not a WebP file (the header is not RIFF…WEBP)');
      continue;
    }
    coverImages.push({
      week,
      lang: m[1],
      path: fileRel,
      bytes: data.length,
      sha256: createHash('sha256').update(data).digest('hex'),
    });
  }
}

// Rule 11: when a week's editions are complete (all 130 of the expected set, none draft, every PDF in the repo —
// the same bar the site uses to publish a week), its website cover must be complete too:
// one cover block .html per reader language (12) and one story image per target language (12).
// It is no longer optional: without it the site shows that week as a list of cards, not a front page
// (W43 and W46 had only print covers).
const coverLangsByWeek = new Map();
for (const c of covers) coverLangsByWeek.set(c.week, (coverLangsByWeek.get(c.week) ?? new Set()).add(c.lang));
const imageLangsByWeek = new Map();
for (const i of coverImages) imageLangsByWeek.set(i.week, (imageLangsByWeek.get(i.week) ?? new Set()).add(i.lang));
const expectedPairCount = LANGS.length * (LANGS.length - 1) - 2;
const readyPairsByWeek = new Map();
for (const e of editions) {
  if (e.draft || !e.pdfInRepo) continue;
  const week = e.week.toLowerCase();
  readyPairsByWeek.set(week, (readyPairsByWeek.get(week) ?? new Set()).add(`${e.target}>${e.native}`));
}
for (const [week, pairs] of readyPairsByWeek) {
  if (pairs.size < expectedPairCount) continue;
  const noCover = LANGS.filter((l) => !coverLangsByWeek.get(week)?.has(l));
  if (noCover.length) {
    fail(`covers/${week}`, `this week has all ${expectedPairCount} editions but no website cover block .html for reader languages ${noCover.join(' ')}; see AGENTS.md, "Add a cover"`);
  }
  const noImage = LANGS.filter((l) => !imageLangsByWeek.get(week)?.has(l));
  if (noImage.length) {
    fail(`covers/${week}/${IMAGES_DIR}`, `this week has all ${expectedPairCount} editions but no story image for target languages ${noImage.join(' ')}; see AGENTS.md, "Add story images"`);
  }
}

covers.sort((a, b) =>
  b.week.localeCompare(a.week) ||
  LANGS.indexOf(a.lang) - LANGS.indexOf(b.lang));
coverImages.sort((a, b) =>
  b.week.localeCompare(a.week) ||
  LANGS.indexOf(a.lang) - LANGS.indexOf(b.lang));

// Sort: week (weekStart) descending → target in LANGS order → native in LANGS order. Never left to consumers.
editions.sort((a, b) =>
  b.weekStart.localeCompare(a.weekStart) ||
  LANGS.indexOf(a.target) - LANGS.indexOf(b.target) ||
  LANGS.indexOf(a.native) - LANGS.indexOf(b.native));

const index = {
  about: 'Lucerna Weekly edition + cover index. Generated by lint.mjs — do not edit by hand.',
  count: editions.length,
  editions,
  coverCount: covers.length,
  covers,
  coverImages,
};
const rendered = JSON.stringify(index, null, 2) + '\n';

if (problems.length) report();

if (write) {
  writeFileSync(join(root, INDEX_FILE), rendered);
  console.log(`index.json written: ${editions.length} editions`);
} else {
  const current = existsSync(join(root, INDEX_FILE))
    ? readFileSync(join(root, INDEX_FILE), 'utf8')
    : '';
  if (current !== rendered) {
    console.error('index.json does not match the content (drift). Run `node lint.mjs --write` and commit the result.');
    process.exit(1);
  }
  console.log(`OK: ${editions.length} editions, index.json is current`);
}

function report() {
  if (problems.length) {
    console.error(`Check failed, ${problems.length} problems:`);
    for (const p of problems) console.error(`  - ${p}`);
    process.exit(1);
  }
}
