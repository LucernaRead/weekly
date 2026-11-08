#!/usr/bin/env node
/**
 * Website cover blocks: the one template, the length limits and the content check.
 *
 *     node tools/cover.mjs <week>     build covers/<week>/<week>-cover-<reader>/<…>.html (12 files) from
 *                                     production/covers/<week>/cover.json
 *
 * From 2026-w46 on, a cover block is generated, never hand-written: lint.mjs renders each block again from
 * cover.json and fails when the file differs by one byte. The layout lives on the site: one whole printed
 * front page per target-language edition —
 *   lead (wide column): headline → italic deck (teaser) → 3:2 picture + caption → excerpt in 2 justified columns;
 *   rail (narrow column): more[0..1] as briefs → word of the week → "inside this issue" (pages 2…n);
 *   below the fold: more[2..5] in 4 columns.
 * The limits below are measured from that layout. SOP.md (Appendix 5) says how to write each field.
 *
 * cover.json:
 *   { "stories": { "<target>": {
 *       "headline": "<target language>",
 *       "excerpt":  "<target language: whole sentences, verbatim from the start of the core's P1 lead>",
 *       "teaser":   { "<reader>": "<reader language>" … 12 },
 *       "caption":  { "<reader>": "…" … 12 },
 *       "alt":      { "<reader>": "…" … 12 },
 *       "more": [ { "headline": "<target language>", "summary": { "<reader>": "…" … 12 } } × 6 ],
 *       "word": { "term": "<target language>", "gloss": { "<reader>": "…" … 12 } },
 *       "pages": [ "<target language: title of page 2>", …, "<title of the last page>" ]
 *   } … 12 } }
 * For reader = target, write the reader-language fields in the target language.
 * lint.mjs also checks that pages has one title per page after P1 (the edition's page count − 1).
 */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

export const LANGS = ['en', 'de', 'fr', 'es', 'it', 'pt', 'nl', 'ru', 'ja', 'ko', 'zh-cn', 'zh-tw'];
/** The first week whose cover blocks come from cover.json. Earlier weeks keep their hand-written blocks. */
export const FIRST_GENERATED_WEEK = '2026-w46';
/**
 * Secondary stories and where the site places them (NYT front-page grid):
 *   more[0] under the lead, headline only · more[1], more[2] the narrow column of the second group, each with a
 *   square thumbnail · more[3] the feature of the second group, with a 3:2 picture · more[4] under the feature ·
 *   more[5] the rail story, with a 3:2 picture.
 */
export const MORE_COUNT = 6;
/** more index → picture aspect [w, h]. File: covers/<week>/images/<target>-<index>.webp (lint rule 10). */
export const MORE_IMAGES = { 1: [1, 1], 2: [1, 1], 3: [3, 2], 5: [3, 2] };

/** Masthead and the small line under it, per reader language (the site replaces the masthead per edition). */
const MASTHEAD = {
  en: ['The Lucerna', 'Weekly'], de: ['Die Lucerna', 'Wochenzeitung'], fr: ['Le Lucerna', 'Hebdomadaire'],
  es: ['La Lucerna', 'Semanario'], it: ['La Lucerna', 'Settimanale'], pt: ['A Lucerna', 'Semanário'],
  nl: ['De Lucerna', 'Weekblad'], ru: ['Lucerna', 'Еженедельник'], ja: ['Lucerna', '週刊'],
  ko: ['Lucerna', '위클리'], 'zh-cn': ['Lucerna', '周报'], 'zh-tw': ['Lucerna', '週報'],
};

/**
 * Length limits. Count = Unicode characters after removing all whitespace; punctuation and digits count.
 * Script group of a field = the language it is written in (target for headline / excerpt / more headline /
 * word term / page titles, reader for the rest). Measured 2026-11-07 on the site layout at the widest page
 * (cover 1200 px, NYT grid: text column 271 px, picture 485 px, rail 314 px), with real text filled to the
 * limit in each script; "other" follows Russian, the widest of the Latin/Cyrillic group:
 *   headline ≤ 3 lines · excerpt ≤ 6 · teaser ≤ 3 · caption 1 · more headline ≤ 3 · more summary ≤ 4 ·
 *   word term 1 · word gloss ≤ 4 · page title 1.
 * alt has no place in the layout; its limit keeps it a short description for screen readers.
 */
export const LIMITS = {
  headline: { cjk: 30, ko: 28, other: 56 },
  excerpt: { cjk: 100, ko: 110, other: 165 },
  teaser: { cjk: 50, ko: 50, other: 80 },
  caption: { cjk: 30, ko: 34, other: 38 },
  alt: { cjk: 60, ko: 70, other: 150 },
  moreHeadline: { cjk: 30, ko: 36, other: 60 },
  moreSummary: { cjk: 60, ko: 60, other: 115 },
  wordTerm: { cjk: 8, ko: 10, other: 14 },
  wordGloss: { cjk: 60, ko: 60, other: 120 },
  pageTitle: { cjk: 12, ko: 14, other: 16 },
};
const CJK = new Set(['ja', 'zh-cn', 'zh-tw']);
const NON_LATIN = new Set(['ru', 'ja', 'ko', 'zh-cn', 'zh-tw']);
/** An excerpt is whole sentences: it ends with a sentence-final mark (closing quotes / brackets may follow). */
const SENTENCE_END = /[.!?。！？…][»"”’」』)）]*$/u;

export const count = (s) => [...s.replace(/\s/gu, '')].length;
export const limitOf = (field, lang) => LIMITS[field][CJK.has(lang) ? 'cjk' : lang === 'ko' ? 'ko' : 'other'];

function asciiLetterFraction(s) {
  const letters = [...s].filter((c) => /\p{L}/u.test(c));
  return letters.length ? letters.filter((c) => c.charCodeAt(0) < 128).length / letters.length : 0;
}

/** Every problem in cover.json, as "where: message" strings. Empty = valid. */
export function checkCover(cover) {
  const out = [];
  const text = (where, field, lang, value) => {
    if (typeof value !== 'string' || !value.trim()) return out.push(`${where}: missing`);
    if (value !== value.trim() || /\s{2,}|\n/.test(value)) out.push(`${where}: no leading/trailing, double or line-break whitespace`);
    if (/[<>]/.test(value)) out.push(`${where}: plain text only, no markup`);
    const n = count(value);
    const max = limitOf(field, lang);
    if (n > max) out.push(`${where}: ${n} characters, limit ${max} (${field}, ${lang}; whitespace not counted)`);
    if (NON_LATIN.has(lang) && asciiLetterFraction(value) > 0.5) out.push(`${where}: mostly ASCII letters; write it in ${lang}`);
  };
  const perReader = (where, field, map) => {
    if (!map || typeof map !== 'object') return out.push(`${where}: missing (one entry per reader language)`);
    const extra = Object.keys(map).filter((r) => !LANGS.includes(r));
    if (extra.length) out.push(`${where}: unknown reader languages ${extra.join(' ')}`);
    for (const r of LANGS) text(`${where}.${r}`, field, r, map[r]);
  };
  const stories = cover?.stories;
  if (!stories || typeof stories !== 'object') return ['stories: missing'];
  const extra = Object.keys(stories).filter((t) => !LANGS.includes(t));
  if (extra.length) out.push(`stories: unknown target languages ${extra.join(' ')}`);
  for (const t of LANGS) {
    const s = stories[t];
    const at = `stories.${t}`;
    if (!s) {
      out.push(`${at}: missing`);
      continue;
    }
    text(`${at}.headline`, 'headline', t, s.headline);
    text(`${at}.excerpt`, 'excerpt', t, s.excerpt);
    if (typeof s.excerpt === 'string' && !SENTENCE_END.test(s.excerpt.trim())) {
      out.push(`${at}.excerpt: must end with a whole sentence (verbatim from the core; do not cut a sentence)`);
    }
    perReader(`${at}.teaser`, 'teaser', s.teaser);
    perReader(`${at}.caption`, 'caption', s.caption);
    perReader(`${at}.alt`, 'alt', s.alt);
    if (!Array.isArray(s.more) || s.more.length !== MORE_COUNT) {
      out.push(`${at}.more: exactly ${MORE_COUNT} secondary stories`);
      continue;
    }
    s.more.forEach((m, i) => {
      text(`${at}.more[${i}].headline`, 'moreHeadline', t, m?.headline);
      perReader(`${at}.more[${i}].summary`, 'moreSummary', m?.summary);
    });
    text(`${at}.word.term`, 'wordTerm', t, s.word?.term);
    perReader(`${at}.word.gloss`, 'wordGloss', s.word?.gloss);
    if (!Array.isArray(s.pages) || s.pages.length < 3) out.push(`${at}.pages: one title per page after P1`);
    else s.pages.forEach((p, i) => text(`${at}.pages[${i}]`, 'pageTitle', t, p));
  }
  return out;
}

const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

/** Standalone look only: the site restyles the block (lead + secondary row) and shows one story at a time. */
const CSS = `
      .lucerna-cover { --lc-bg: #fbfaf6; --lc-ink: #302c28; --lc-body: #3a3631; --lc-muted: #6f675d;
        --lc-line: #d8d2c4; --lc-olive: #46581f; --lc-plate: #efebe1;
        background: var(--lc-bg); color: var(--lc-body); padding: 8px 24px 28px;
        font: 16px/1.55 "Newsreader", Georgia, "Noto Serif SC", "Songti SC", serif; }
      @media (prefers-color-scheme: dark) {
        .lucerna-cover { --lc-bg: #16180f; --lc-ink: #ece4cd; --lc-body: #cfc9b6; --lc-muted: #9a957f;
          --lc-line: #3d3f2c; --lc-olive: #a9bf7d; --lc-plate: #26291a; }
      }
      .lucerna-cover * { box-sizing: border-box; }
      .lucerna-cover .lc-wordmark-block { text-align: center; padding: 18px 0 20px; border-bottom: 2px solid var(--lc-ink); }
      .lucerna-cover .lc-wordmark { margin: 0; color: var(--lc-ink); font-size: clamp(44px, 7vw, 80px); font-weight: 800; line-height: 1; }
      .lucerna-cover .lc-wm-small { display: block; margin-top: 10px; font-size: 14px; font-weight: 600;
        letter-spacing: .34em; text-transform: uppercase; color: var(--lc-olive); }
      .lucerna-cover .lc-hero { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 28px 32px; padding-top: 24px; }
      .lucerna-cover .lc-story { min-width: 0; }
      .lucerna-cover .lc-media { margin: 0 0 12px; }
      .lucerna-cover .lc-plate { display: flex; align-items: center; justify-content: center; aspect-ratio: 3 / 2;
        background: var(--lc-plate); border: 1px solid var(--lc-line); }
      .lucerna-cover .lc-mast { font-style: italic; font-size: 22px; color: var(--lc-ink); }
      .lucerna-cover figcaption { margin-top: 6px; font-size: 12px; color: var(--lc-muted); }
      .lucerna-cover h3 { margin: 0 0 8px; color: var(--lc-ink); font-size: 22px; line-height: 1.2; }
      .lucerna-cover p { margin: 0 0 8px; }
      .lucerna-cover .lc-teaser { color: var(--lc-muted); font-size: 14.5px; }
      .lucerna-cover .lc-more { margin: 12px 0 0; padding: 10px 0 0; list-style: none; border-top: 1px solid var(--lc-line); }
      .lucerna-cover .lc-more li + li { margin-top: 10px; }
      .lucerna-cover .lc-more h4 { margin: 0 0 2px; color: var(--lc-ink); font-size: 16px; line-height: 1.3; }
      .lucerna-cover .lc-more p { margin: 0; color: var(--lc-muted); font-size: 14px; }
      .lucerna-cover .lc-word { margin-top: 12px; padding-top: 8px; border-top: 1px solid var(--lc-line); }
      .lucerna-cover .lc-term { margin: 0; color: var(--lc-ink); font-size: 20px; font-style: italic; font-weight: 700; }
      .lucerna-cover .lc-gloss { margin: 0; color: var(--lc-muted); font-size: 14px; }
      .lucerna-cover .lc-pages { margin: 10px 0 0; padding-left: 1.6em; font-size: 14px; color: var(--lc-muted); }
`;

/** The cover block for one reader language. Story order = LANGS (rule 8 reads it from data-story-langs). */
export function renderCover(cover, reader) {
  const [masthead, small] = MASTHEAD[reader];
  const story = (t) => {
    const s = cover.stories[t];
    const more = s.more
      .map((m) => `\n          <li><h4 lang="${t}">${esc(m.headline)}</h4><p>${esc(m.summary[reader])}</p></li>`)
      .join('');
    return `
      <article class="lc-story">
        <figure class="lc-media" data-image-slot data-alt="${esc(s.alt[reader])}">
          <div class="lc-plate"><span class="lc-mast" lang="${t}">${esc(MASTHEAD[t][0])}</span></div>
          <figcaption>${esc(s.caption[reader])}</figcaption>
        </figure>
        <h3 lang="${t}">${esc(s.headline)}</h3>
        <p class="lc-excerpt" lang="${t}">${esc(s.excerpt)}</p>
        <p class="lc-teaser">${esc(s.teaser[reader])}</p>
        <ul class="lc-more">${more}
        </ul>
        <div class="lc-word"><p class="lc-term" lang="${t}">${esc(s.word.term)}</p><p class="lc-gloss">${esc(s.word.gloss[reader])}</p></div>
        <ol class="lc-pages" start="2">${s.pages.map((p) => `\n          <li lang="${t}">${esc(p)}</li>`).join('')}
        </ol>
      </article>`;
  };
  return `<!doctype html>
<html lang="${reader}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="color-scheme" content="light dark" />
    <title>${esc(masthead)} · ${esc(small)}</title>
    <link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,600;6..72,700;6..72,800&amp;display=swap" rel="stylesheet" />
    <style>${CSS}    </style>
  </head>
  <body data-story-langs="${LANGS.join(' ')}">
    <div class="lucerna-cover">
      <div class="lc-wordmark-block">
        <h1 class="lc-wordmark">${esc(masthead)}<span class="lc-wm-small">${esc(small)}</span></h1>
      </div>
      <div class="lc-hero">${LANGS.map(story).join('')}
      </div>
    </div>
  </body>
</html>
`;
}

export const coverJsonPath = (week) => join('production', 'covers', week, 'cover.json');
export const coverHtmlPath = (week, reader) => join('covers', week, `${week}-cover-${reader}`, `${week}-cover-${reader}.html`);

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const week = process.argv[2];
  if (!/^\d{4}-w\d{2}$/.test(week ?? '')) {
    console.error('usage: node tools/cover.mjs <week, e.g. 2026-w47>');
    process.exit(2);
  }
  const cover = JSON.parse(readFileSync(coverJsonPath(week), 'utf8'));
  const problems = checkCover(cover);
  if (problems.length) {
    console.error(`${coverJsonPath(week)}: ${problems.length} problems`);
    for (const p of problems) console.error(`  - ${p}`);
    process.exit(1);
  }
  for (const r of LANGS) {
    const path = coverHtmlPath(week, r);
    mkdirSync(join(path, '..'), { recursive: true });
    writeFileSync(path, renderCover(cover, r));
    console.log(`wrote ${path}`);
  }
}
