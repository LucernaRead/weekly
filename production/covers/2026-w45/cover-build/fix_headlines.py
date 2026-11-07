#!/usr/bin/env python3
"""Fix W45 website cover headlines: replace English-gloss headlines with the
verbatim target-language headlines from the W45 print-cover frontmatter.

Ground truth: cover_check.load_print_covers (cross-checked across all 12
print-cover reader versions). Only the <h2>/<h3> inner text of each
<article> is replaced, mapped by the block's own data-story-langs order.
Everything else in the file is left byte-identical.
"""
import html
import os
import re
import sys

sys.path.insert(0, os.path.expanduser(
    '~/workspace/goals/lucernaread-social-media-operations/tools'))
import cover_check

ROOT = os.path.expanduser('~/workspace/weekly-git')
WEEK = '2026-w45'
LANGS = cover_check.LANGS

headlines, excerpts, pfails = cover_check.load_print_covers(ROOT, WEEK)
if pfails:
    print('PRINT-COVER GROUND-TRUTH FAILURES:')
    for f in pfails:
        print(' ', f)
    sys.exit(1)
assert set(headlines) == set(LANGS), headlines.keys()
print('Ground-truth headlines from print covers (12/12 agree):')
for s in LANGS:
    print(f'  [{s}] {headlines[s]}')

total = [0]
for r in LANGS:
    path = os.path.join(ROOT, 'covers', WEEK, f'{WEEK}-cover-{r}', f'{WEEK}-cover-{r}.html')
    s = open(path, encoding='utf-8').read()
    bm = re.search(r'<body[^>]*data-story-langs="([^"]+)"', s)
    langs = bm.group(1).split()
    assert len(langs) == 12 and set(langs) == set(LANGS), (r, langs)

    def repl_article(m):
        open_tag, a, close_tag = m.group(1), m.group(2), m.group(3)
        idx = repl_article.i
        repl_article.i += 1
        s_lang = langs[idx]
        hm = re.search(r'(<h[23][^>]*>)(.*?)(</h[23]>)', a, re.S)
        assert hm, f'{r} art{idx}: no headline tag'
        new = headlines[s_lang]
        new_esc = html.escape(new, quote=True)
        total[0] += 1
        return open_tag + a[:hm.start(2)] + new_esc + a[hm.end(2):] + close_tag

    repl_article.i = 0
    new_s, n = re.subn(r'(<article[^>]*>)(.*?)(</article>)', repl_article, s, flags=re.S)
    assert n == 12, (r, n)
    assert repl_article.i == 12
    open(path, 'w', encoding='utf-8').write(new_s)
    print(f'{r}: 12 headlines replaced (order {langs})')

print(f'TOTAL headlines replaced: {total[0]}')
assert total[0] == 144, total[0]
