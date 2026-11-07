#!/usr/bin/env python3
"""Website cover block gate — the check that did not exist before 2026-11-05.

Every website cover block (covers/<week>/<week>-cover-<reader>/*.html,
lint rule 11) must carry, per <article>:
  (1) a <p class="lc-excerpt" lang="<story lang>"> whose text is
      byte-identical to that week+story's PRINT-cover excerpt;
  (2) a teaser <p> whose text is byte-identical to teasers[reader][story];
  (3) a headline byte-identical to the print-cover frontmatter headline;
  (4) exactly 12 articles, with data-story-langs intact (12 codes, each
      exactly once, in document order).

Why this tool exists: the 2026-11-04 W43/W46 cover build verified its
output by comparing the .html against teasers.json — but teasers.json
`excerpts` were never inserted into the .html, so a comparison check
could not catch the missing element. The defect shipped (every article
showed only the reader-language teaser, no target-language excerpt) and
was caught by the user reading the cover. This tool reads the ground
truth INDEPENDENTLY of the build — headlines + excerpts straight from
the print-cover .md files in the repo, teasers from the per-week
teasers.json — and FAILS LOUDLY on any missing or wrong-language
excerpt. Never compare a build's output against the build's own input
and call that verification.

Ground-truth notes (verified 2026-11-05, do not "fix" by editing data):
- Excerpts come from the PRINT covers, NOT from teasers.json `excerpts`:
  W43 teasers.json excerpts are different short summaries (one contains
  mojibake), W46's are truncated prefixes of the print-cover paragraphs.
  The print cover is the shipped, proofread artifact; it wins.
- W45 .html headlines are English glosses, 0/144 byte-identical to the
  print covers (W43/W46 are 144/144). The headline assertion therefore
  FAILS for W45 until the headlines are separately corrected. That is a
  true positive, not a tool bug — do not add exceptions.
- W45 teasers.json `teasers` are baselined from the shipped .html
  (fresh extraction diverges 142/142); for W43/W46 they come from the
  extraction pipeline and the .html matches them 144/144.
- Template variance (NOT failures, preserved as shipped): only the
  es/fr/zh-cn/zh-tw blocks use class="lc-teaser" on the teaser <p>;
  old-style blocks use a plain <p>, the feature article uses class
  "teaser", pt blocks use <h2> headlines. The tool finds the teaser
  structurally (the single <p> outside <figure> that is not the
  excerpt) and checks its TEXT; it does not require the lc-teaser class.
  The ko block's non-standard data-story-langs order is also preserved.

Usage (run with the tools venv python):
  $PY cover_check.py --week 2026-w46 [--root ~/workspace/weekly-git]
  $PY cover_check.py --all [--root ...]
  --teasers-root defaults to <repo>/production/covers, i.e. the
  production/covers/<week>/teasers.json per week (full week name,
  e.g. 2026-w46). The legacy goal hidden_files/w<NN>/cover-build/
  layout is still accepted as a fallback. A future week's
  build must produce its teasers.json (headlines/teasers/excerpts from
  the print covers + edition abstracts) BEFORE running this gate.
Exit: 0 all checks pass; 1 any failure (every failure printed as FAIL).
"""
import argparse
import glob
import html
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    yaml = None

LANGS = ['de', 'fr', 'es', 'en', 'it', 'pt', 'nl', 'ru', 'ja', 'ko', 'zh-cn', 'zh-tw']


def fail(lines, msg):
    lines.append(f'FAIL {msg}')


def parse_print_cover(path):
    """Return (frontmatter headlines, body excerpts) for one print cover .md."""
    txt = open(path, encoding='utf-8').read()
    m = re.search(r'^---\n(.*?)\n---\n', txt, re.S)
    assert m, f'{path}: no frontmatter'
    fm = yaml.safe_load(m.group(1))
    headlines = {h['lang']: h['headline'] for h in fm['headlines']}
    body = txt[m.end():]
    sec = re.search(r'## Headlines\n(.*?)(?:\n## |\Z)', body, re.S)
    assert sec, f'{path}: no Headlines section'
    items = {}
    lines = sec.group(1).split('\n')
    i = 0
    while i < len(lines):
        hm = re.match(r'^(\d+)\. \[([a-z-]+)\] (.*)$', lines[i])
        if not hm:
            i += 1
            continue
        lang = hm.group(2)
        headline = hm.group(3).strip()
        j = i + 1
        para = []
        while j < len(lines):
            if re.match(r'^\d+\. \[[a-z-]+\] ', lines[j]):
                break
            if lines[j].strip() == '':
                break
            para.append(lines[j])
            j += 1
        assert len(para) == 1, f'{path} [{lang}]: excerpt spans {len(para)} lines'
        assert lang not in items, f'{path}: duplicate [{lang}]'
        items[lang] = (headline, para[0].strip())
        i = j
    assert set(items) == set(LANGS), f'{path}: items {sorted(items)} != LANGS'
    return headlines, items


def load_print_covers(root, week):
    """Cross-checked headlines + excerpts: all 12 reader versions must agree."""
    headlines = {}
    excerpts = {}
    failures = []
    for r in LANGS:
        path = os.path.join(root, 'covers', week,
                            f'{week}-cover-{r}', f'{week}-cover-{r}.md')
        if not os.path.exists(path):
            failures.append(f'{week}: missing print cover {path}')
            continue
        fm_h, items = parse_print_cover(path)
        for s in LANGS:
            h_body, e_body = items[s]
            if s in headlines:
                if headlines[s] != h_body:
                    failures.append(f'{week} [{s}]: headline differs between print-cover readers')
                if excerpts[s] != e_body:
                    failures.append(f'{week} [{s}]: excerpt differs between print-cover readers')
            else:
                headlines[s] = h_body
                excerpts[s] = e_body
            if fm_h.get(s) != h_body:
                failures.append(f'{week} reader {r} [{s}]: body headline != frontmatter headline')
    return headlines, excerpts, failures


def parse_block(path):
    """Parse one .html cover block into (langs, articles, style_text).

    articles: list of dicts with headline, excerpt (tag text or None,
    lang attr or None, count), teaser (text or None, count), slots.
    """
    s = open(path, encoding='utf-8').read()
    bm = re.search(r'<body[^>]*data-story-langs="([^"]+)"', s)
    langs = bm.group(1).split() if bm else []
    sm = re.search(r'<style>(.*?)</style>', s, re.S)
    style = sm.group(1) if sm else ''
    articles = []
    for am in re.finditer(r'<article[^>]*>(.*?)</article>', s, re.S):
        a = am.group(1)
        hm = re.search(r'<h[23][^>]*>(.*?)</h[23]>', a, re.S)
        headline = html.unescape(hm.group(1)).strip() if hm else None
        # excerpt paragraphs (must be exactly one, lang == story lang)
        exs = [(m.group(1), html.unescape(m.group(2)).strip())
               for m in re.finditer(r'<p class="lc-excerpt"(?: lang="([^"]*)")?>(.*?)</p>', a, re.S)]
        # teaser: the single <p> outside <figure> that is not the excerpt
        nofig = re.sub(r'<figure>.*?</figure>', '', a, flags=re.S)
        teasers = []
        for m in re.finditer(r'<p([^>]*)>(.*?)</p>', nofig, re.S):
            if 'lc-excerpt' in m.group(1):
                continue
            teasers.append((m.group(1), html.unescape(m.group(2)).strip()))
        slots = len(re.findall(r'data-image-slot', a))
        articles.append({
            'headline': headline,
            'excerpts': exs,
            'teasers': teasers,
            'slots': slots,
        })
    return langs, articles, style, s


def check_week(root, teasers_root, week):
    """Return (failures, n_articles_checked). Prints nothing; caller reports."""
    failures = []
    week_l = week.lower()
    headlines, excerpts, pfails = load_print_covers(root, week_l)
    failures.extend(pfails)
    tj_path = None
    # New layout first: production/covers/<week>/teasers.json (full week
    # name, e.g. 2026-w46). Legacy fallback: the goal's
    # hidden_files/w<NN>/cover-build/ (short week name, e.g. w46) or the
    # long form 2026-w46 under it.
    short_week = week_l.split('-', 1)[1] if '-' in week_l else week_l
    for cand in (os.path.join(teasers_root, week_l, 'teasers.json'),
                 os.path.join(teasers_root, short_week, 'cover-build', 'teasers.json'),
                 os.path.join(teasers_root, week_l, 'cover-build', 'teasers.json')):
        if os.path.exists(cand):
            tj_path = cand
            break
    if tj_path is None:
        failures.append(f'{week}: missing teasers.json under {teasers_root}/{{{week_l}/teasers.json, {short_week}/cover-build/, {week_l}/cover-build/}}')
        teasers = {}
    else:
        teasers = json.load(open(tj_path, encoding='utf-8'))['teasers']
    n_checked = 0
    for r in LANGS:
        path = os.path.join(root, 'covers', week_l, f'{week_l}-cover-{r}',
                            f'{week_l}-cover-{r}.html')
        if not os.path.exists(path):
            failures.append(f'{week} reader {r}: missing cover block {path}')
            continue
        langs, articles, style, _ = parse_block(path)
        if len(articles) != 12:
            failures.append(f'{week} reader {r}: {len(articles)} articles, expected 12')
            continue
        if len(langs) != 12 or set(langs) != set(LANGS):
            failures.append(f'{week} reader {r}: data-story-langs bad: {langs}')
        if '.lc-excerpt' not in style:
            failures.append(f'{week} reader {r}: no .lc-excerpt rule in <style>')
        for i, art in enumerate(articles):
            s_lang = langs[i] if i < len(langs) else '?'
            n_checked += 1
            tag = f'{week} reader {r} art{i} [{s_lang}]'
            if art['headline'] is None:
                failures.append(f'{tag}: no headline (h2/h3)')
            elif headlines.get(s_lang) is not None and art['headline'] != headlines[s_lang]:
                failures.append(f'{tag}: headline != print cover: {art["headline"][:60]!r} vs {headlines[s_lang][:60]!r}')
            if len(art['excerpts']) == 0:
                failures.append(f'{tag}: MISSING <p class="lc-excerpt">')
            elif len(art['excerpts']) > 1:
                failures.append(f'{tag}: {len(art["excerpts"])} excerpt paragraphs, expected 1')
            else:
                lang_attr, text = art['excerpts'][0]
                if lang_attr != s_lang:
                    failures.append(f'{tag}: excerpt lang="{lang_attr}", expected "{s_lang}"')
                if excerpts.get(s_lang) is not None and text != excerpts[s_lang]:
                    failures.append(f'{tag}: excerpt text != print cover ({len(text)}ch vs {len(excerpts[s_lang])}ch)')
            if len(art['teasers']) == 0:
                failures.append(f'{tag}: no teaser <p>')
            elif len(art['teasers']) > 1:
                failures.append(f'{tag}: {len(art["teasers"])} teaser <p>, expected 1')
            else:
                _, ttext = art['teasers'][0]
                want = teasers.get(r, {}).get(s_lang)
                if want is not None and ttext != want:
                    failures.append(f'{tag}: teaser text != teasers.json ({len(ttext)}ch vs {len(want)}ch)')
                # Teasers are compared against teasers.json, which is the
                # same source the .html was built from — a comparison check
                # cannot catch a bug shared by both. The W43 abstract trim
                # left a stray leading char on 22 teasers (')', '）', '，',
                # ':' from the "(VOL.1)" masthead prefix) in BOTH files, so
                # the comparison passed while every reader saw the stray.
                # A teaser never legitimately starts with closing
                # punctuation, so fail loudly on it.
                if ttext and ttext[0] in [')', '）', '，', ',', ':', '：', ';', '；', '、']:
                    failures.append(f'{tag}: teaser starts with stray punctuation {ttext[0]!r}')
            if art['slots'] > 1:
                failures.append(f'{tag}: {art["slots"]} data-image-slot, at most 1 allowed')
    return failures, n_checked


def main():
    ap = argparse.ArgumentParser(description='Website cover block gate (rule 11 companion).')
    ap.add_argument('--week', action='append', default=[],
                    help='week to check, e.g. 2026-w46 (repeatable)')
    ap.add_argument('--all', action='store_true',
                    help='check every week under covers/ with 12 cover dirs')
    ap.add_argument('--root', default=os.path.expanduser('~/workspace/weekly-git'),
                    help='repo clone root (default ~/workspace/weekly-git)')
    ap.add_argument('--teasers-root', default=None,
                    help='dir holding <week>/teasers.json '
                         '(default <repo>/production/covers)')
    args = ap.parse_args()
    if yaml is None:
        print('FAIL cover_check.py needs PyYAML (run with the tools venv python)')
        return 1
    if args.teasers_root is None:
        args.teasers_root = os.path.normpath(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'production', 'covers'))
    weeks = [w.lower() for w in args.week]
    if args.all:
        for d in sorted(glob.glob(os.path.join(args.root, 'covers', '2026-w*'))):
            w = os.path.basename(d)
            if len(glob.glob(os.path.join(d, f'{w}-cover-*'))) == 12 and w not in weeks:
                weeks.append(w)
    if not weeks:
        print('usage: cover_check.py --week 2026-w46 | --all')
        return 2
    all_failures = []
    total_articles = 0
    for w in weeks:
        failures, n = check_week(args.root, args.teasers_root, w)
        total_articles += n
        if failures:
            print(f'--- {w}: FAIL ({len(failures)} failures, {n} articles checked) ---')
            for f in failures:
                print(f'FAIL {f}')
            all_failures.extend(failures)
        else:
            print(f'--- {w}: PASS ({n} articles checked) ---')
    print(f'TOTAL: {total_articles} articles checked, {len(all_failures)} failures')
    if all_failures:
        print('COVER CHECK FAILED')
        return 1
    print('COVER CHECK PASSED')
    return 0


if __name__ == '__main__':
    sys.exit(main())
