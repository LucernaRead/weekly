#!/usr/bin/env python3
"""Fix W43 website-cover teaser trim artifact (2026-11-05).

Root cause: the W43 abstract trim cut the masthead prefix
("Die Lucerna ... (VOL.1" / "（VOL.1") but left the closing
punctuation behind, so 22 teasers start with a stray char:
  - reader fr x 11 stories: leading ASCII ')' (some '), ' / ') : ')
  - reader zh-cn x 10 stories: leading full-width '）' (one leading '，')
  - reader ru x 1 story (nl): leading ': '
The stray exists ONLY in the website layer (.html teaser + teasers.json):
the W43 print covers contain none of this teaser text (verified by grep),
and the edition abstracts are clean (the '）' is the closing paren of
"（VOL.1）"). So fix it in BOTH website-layer places so they stay
consistent: teasers.json AND the .html blocks. Print covers untouched.
Two German-quote teasers ([de][fr], [de][ru] starting with '„') are
legitimate opening quotes and are NOT touched.
"""
import html
import json
import os
import re
import sys

ROOT = os.path.expanduser('~/workspace/weekly-git')
WEEK = '2026-w43'
TJ_PATH = os.path.expanduser(
    '~/workspace/goals/lucernaread-social-media-operations/hidden_files/'
    'w43/cover-build/teasers.json')

STRIP = set([')', '）', ' ', ',', '，', ':', '：', ';', '；', '、'])


def strip_leading(t):
    i = 0
    while i < len(t) and t[i] in STRIP:
        i += 1
    return t[i:]


tj = json.load(open(TJ_PATH, encoding='utf-8'))
teasers = tj['teasers']

# 1. find + fix in teasers.json
fixes = {}  # (reader, story) -> (old, new)
for r, d in teasers.items():
    for s, t in d.items():
        if t and t[0] in STRIP:
            new = strip_leading(t)
            assert new, (r, s)
            assert new[0].isalnum() or new[0] in '«"“「『', (r, s, new[:20])
            assert new != t, (r, s)
            fixes[(r, s)] = (t, new)
print(f'flagged teasers: {len(fixes)}')
for (r, s), (old, new) in sorted(fixes.items()):
    print(f'  [{r}][{s}]: {old[:40]!r} -> {new[:40]!r}')
assert len(fixes) == 22, len(fixes)
for (r, s), (old, new) in fixes.items():
    teasers[r][s] = new
with open(TJ_PATH, 'w', encoding='utf-8') as f:
    json.dump(tj, f, ensure_ascii=False, indent=1)
print('teasers.json updated')

# 2. apply the same fix to the .html blocks (assert old text matches first)
for (r, s), (old, new) in sorted(fixes.items()):
    path = os.path.join(ROOT, 'covers', WEEK, f'{WEEK}-cover-{r}', f'{WEEK}-cover-{r}.html')
    txt = open(path, encoding='utf-8').read()
    bm = re.search(r'<body[^>]*data-story-langs="([^"]+)"', txt)
    langs = bm.group(1).split()
    assert s in langs, (r, s)
    idx = langs.index(s)

    state = {'i': -1}

    def repl_article(m):
        state['i'] += 1
        open_tag, a, close_tag = m.group(1), m.group(2), m.group(3)
        if state['i'] != idx:
            return m.group(0)
        nofig = re.sub(r'<figure>.*?</figure>', '', a, flags=re.S)
        cands = [(mm.group(1), mm.group(2)) for mm in
                 re.finditer(r'<p([^>]*)>(.*?)</p>', nofig, re.S)
                 if 'lc-excerpt' not in mm.group(1)]
        assert len(cands) == 1, (r, s, len(cands))
        attrs, inner = cands[0]
        cur = html.unescape(inner).strip()
        assert cur == old, (r, s, repr(cur[:50]), repr(old[:50]))
        new_inner = html.escape(new, quote=True)
        pat = re.compile(r'(<p' + re.escape(attrs) + r'>)'
                         + re.escape(inner) + r'(</p>)', re.S)
        new_a, n = pat.subn(r'\g<1>' + new_inner + r'\g<2>', a, count=1)
        assert n == 1, (r, s, n)
        return open_tag + new_a + close_tag

    new_txt, n = re.subn(r'(<article[^>]*>)(.*?)(</article>)',
                         repl_article, txt, flags=re.S)
    assert n == 12, (r, n)
    open(path, 'w', encoding='utf-8').write(new_txt)
    print(f'{r} [{s}]: teaser fixed in .html')

print(f'TOTAL teaser fixes applied (teasers.json + .html): {len(fixes)}')
