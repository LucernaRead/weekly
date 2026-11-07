#!/usr/bin/env python3
"""Build W45 teasers.json (same shape as W43/W46).

Ground truth decisions (verified 2026-11-05):
- headlines + excerpts: from the W45 PRINT covers (all 12 reader versions
  agree byte-identically). These are the full excerpt paragraphs.
- teasers: BASELINED FROM THE SHIPPED .html files. Fresh extraction from
  W45 edition abstracts with the W46 trim rules diverges 142/142 from the
  shipped teaser text, and W45 .html headlines are English glosses (0/144
  match the print covers) — W45 was built by a different/older pipeline
  than W43/W46 (whose .html teasers match their teasers.json 144/144).
  The shipped teaser text is what readers see; this fix must not change
  teasers, so the .html text is the correct baseline for the regression
  gate (cover_check.py assertion 2). The extraction comparison is kept
  below as a diagnostic only.
- The 2 cross-script pairs (zh-cn reader x zh-tw story, zh-tw reader x
  zh-cn story) have no edition files; their teasers come from the .html
  like all the others.
"""
import glob, html, json, re, sys
import yaml

ROOT = '/home/hatch/workspace/weekly-git'
WEEK = '2026-w45'
OUTDIR = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/cover-build'
LANGS = ['de', 'fr', 'es', 'en', 'it', 'pt', 'nl', 'ru', 'ja', 'ko', 'zh-cn', 'zh-tw']


def load_md(path):
    txt = open(path, encoding='utf-8').read()
    m = re.search(r'^---\n(.*?)\n---', txt, re.S)
    return yaml.safe_load(m.group(1))


def trim_abstract(a):
    s = a
    m = re.search(r'VOL\.\d+\s*', s)
    if m:
        rest = s[m.end():]
        for sep in (': ', '：'):
            i = rest.find(sep)
            if 0 <= i < 160:
                s = rest[i + len(sep):]
                break
        else:
            s = rest
    else:
        for sep in (': ', '：'):
            i = s.find(sep)
            if 0 < i < 80:
                s = s[i + len(sep):]
                break
    for _ in range(2):
        done = False
        for sep in ('— ', ': ', '; ', '；', '、'):
            i = s.find(sep)
            if 0 < i < 150:
                head = s[:i]
                if (('A2' in head or '150' in head)
                        or (any(w in head for w in
                                ['learn', 'apprend', 'lernen', 'impar', 'aprender',
                                 'изуча', '学习', '學習', '学ぶ', '배우'])
                            and any(w in head for w in
                                   ['news', 'Nachrichten', 'nouvelles', 'noticias',
                                    'notizie', 'notícias', 'nieuws', 'новост',
                                    'ニュース', '뉴스', '新闻', '新聞']))):
                    s = s[i + len(sep):]
                    done = True
                    break
        if not done:
            break
    i = s.rfind(' — ')
    if i > 0 and any(w in s[i:] for w in ('150', 'A2', '연습', '練習', '练习')):
        s = s[:i]
    cuts = []
    m = re.search(r'A2', s)
    if m:
        cuts.append(m.start())
    m = re.search(r'150', s)
    if m:
        cuts.append(m.start())
    m = re.search(r'正文', s)
    if m:
        cuts.append(m.start())
    m = re.search(r'一份以', s)
    if m:
        cuts.append(m.start())
    for marker in ('con note in', 'frasi della settimana', 'tutte le risposte',
                   'with notes', 'and all answers', 'mit Lösungen',
                   'con soluzioni', 'avec corrigés', 'com respostas',
                   'met antwoorden', 'с ответами', '解答つき', '解答付き',
                   '정답 수록', '附答案'):
        i = s.find(marker)
        if i > 0:
            cuts.append(i)
    if cuts:
        s = s[:min(cuts)]
    s = re.sub(r'[\s,;、，；：:—\-–]+$', '', s).strip()
    frag = ('Niveaus', 'niveaux', 'niveles', 'livelli', 'níveis', 'niveaus',
            'уровни', 'レベル', '수준', '程度', '分级', '分級', '練習問題',
            '练习题', '練習題', '연습 문제', '연습문제', 'exercices',
            'ejercicios', 'exercises', 'esercizi', 'exercícios',
            'oefeningen', 'упражнений', 'Übungen')
    changed = True
    while changed:
        changed = False
        for w in frag:
            for sep in (' ', ', ', '; ', '、', '，', '；', '：', ': '):
                if s.endswith(sep + w):
                    s = s[:-(len(sep) + len(w))]
                    s = re.sub(r'[\s,;、，；：:—\-–]+$', '', s).strip()
                    changed = True
            if s.endswith(w) and len(s) > len(w) + 2:
                s = s[:-len(w)]
                s = re.sub(r'[\s,;、，；：:—\-–]+$', '', s).strip()
                changed = True
    s = re.sub(r'[\s,;、，；：:—\-–]+$', '', s).strip()
    if s:
        if any('\u4e00' <= ch <= '\u9fff' for ch in s):
            if s[-1] not in '。！？':
                s += '。'
        elif s[-1] not in '.!?"”':
            s += '.'
    return s


def parse_block(path):
    """Return (data-story-langs list, [(headline, teaser_text)]) for one .html block."""
    s = open(path, encoding='utf-8').read()
    langs = re.search(r'<body[^>]*data-story-langs="([^"]+)"', s).group(1).split()
    arts = re.findall(r'<article[^>]*>(.*?)</article>', s, re.S)
    assert len(arts) == 12, f'{path}: {len(arts)} articles'
    out = []
    for a in arts:
        hm = re.search(r'<h[23][^>]*>(.*?)</h[23]>', a, re.S)
        assert hm, f'{path}: article without headline'
        headline = html.unescape(hm.group(1)).strip()
        a_nofig = re.sub(r'<figure>.*?</figure>', '', a, flags=re.S)
        ps = re.findall(r'<p[^>]*>(.*?)</p>', a_nofig, re.S)
        assert len(ps) == 1, f'{path}: {len(ps)} teaser <p> in article [{headline[:30]}]'
        out.append((headline, html.unescape(ps[0]).strip()))
    return langs, out


def main():
    pc = json.load(open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/cover-excerpt-fix/2026-w45-print-cover.json', encoding='utf-8'))
    headlines = pc['headlines']
    excerpts = pc['excerpts']

    # Diagnostic only: fresh extraction from edition abstracts.
    editions = {}
    for p in glob.glob(f'{ROOT}/issues/{WEEK}/*/2026-w45-*.md'):
        if p.endswith('.text.md'):
            continue
        fm = load_md(p)
        if fm.get('kind') == 'cover':
            continue
        editions[(fm['target'], fm['native'])] = {
            'abstract': fm.get('abstract', ''),
            'excerpt': fm.get('excerpt', ''),
        }
    extracted = {}
    for R in LANGS:
        extracted[R] = {}
        for S in LANGS:
            if (S, R) in editions:
                extracted[R][S] = trim_abstract(editions[(S, R)]['abstract'])
            elif S == R:
                cands = [(t, n) for (t, n) in editions if t == S]
                src = sorted(cands)[0]
                extracted[R][S] = editions[src]['excerpt'].strip()

    # Teasers baselined from shipped .html (story lang by data-story-langs position).
    teasers = {}
    n_diag = 0
    n_diverge = 0
    for R in LANGS:
        teasers[R] = {}
        langs, arts = parse_block(f'{ROOT}/covers/{WEEK}/{WEEK}-cover-{R}/{WEEK}-cover-{R}.html')
        for pos, (headline, teaser_html) in enumerate(arts):
            S = langs[pos]
            teasers[R][S] = teaser_html
            if S in extracted[R]:
                n_diag += 1
                if extracted[R][S] != teaser_html:
                    n_diverge += 1
    print(f'diagnostic: fresh extraction vs shipped .html teasers: {n_diverge}/{n_diag} diverge')
    print('(teasers.json uses the shipped .html text; see provenance note)')

    out = {
        'headlines': headlines,
        'teasers': teasers,
        'excerpts': excerpts,
        'missing_pairs_needing_override': [],
        'provenance': ('headlines+excerpts from W45 print covers (all 12 reader versions agree); '
                       'teasers BASELINED FROM THE SHIPPED .html files (fresh extraction from edition '
                       'abstracts diverges 142/142 — W45 was built by a different/older pipeline than '
                       'W43/W46, whose .html teasers match their teasers.json 144/144). '
                       'NOTE: excerpts here are the FULL print-cover paragraphs; the edition frontmatter '
                       '`excerpt` field is a shorter prefix and must NOT be used as the cover excerpt. '
                       'KNOWN DEFECT (found 2026-11-05, NOT fixed by the excerpt fix): W45 .html headlines '
                       'are English glosses, 0/144 byte-identical to the print-cover headlines (W43/W46 are '
                       '144/144). cover_check.py headline assertion therefore fails for W45 until the '
                       'headlines are separately corrected.'),
    }
    with open(f'{OUTDIR}/teasers.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f'wrote {OUTDIR}/teasers.json (teasers baselined from shipped .html)')


if __name__ == '__main__':
    main()
