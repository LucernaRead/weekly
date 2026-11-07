#!/usr/bin/env python3
"""Extract W46 cover content: headlines, teasers per (target, reader), excerpts."""
import json, re, sys, glob
import yaml

ROOT = '/home/hatch/workspace/weekly-git'
LANGS = ['de', 'fr', 'es', 'en', 'it', 'pt', 'nl', 'ru', 'ja', 'ko', 'zh-cn', 'zh-tw']

def load_md(path):
    txt = open(path, encoding='utf-8').read()
    m = re.search(r'^---\n(.*?)\n---', txt, re.S)
    return yaml.safe_load(m.group(1))

# shared headlines from any print cover frontmatter
d = load_md(f'{ROOT}/covers/2026-w43/2026-w43-cover-en/2026-w43-cover-en.md')
headlines = {h['lang']: h['headline'] for h in d['headlines']}
assert set(headlines) == set(LANGS), headlines.keys()

editions = {}  # (target, native) -> {abstract, excerpt}
for p in glob.glob(f'{ROOT}/issues/2026-w43/*/2026-w43-*.md'):
    if p.endswith('.text.md'):
        continue
    fm = load_md(p)
    if fm.get('kind') == 'cover':
        continue
    editions[(fm['target'], fm['native'])] = {
        'abstract': fm.get('abstract', ''),
        'excerpt': fm.get('excerpt', ''),
    }

import re

BOILER_MARKERS = ['150', 'A2', 'B2', 'pagine', 'esercizi', 'Übungen',
    'ejercicios', 'exercises', 'oefeningen', 'упражнений', '練習', '练习',
    '연습', '解答', 'solutions', 'corrigés', 'respostas', 'antwoorden',
    'testi in', 'con spiegazioni', 'Erklärungen', 'para lectores',
    'learners', 'lectores', 'lettori', 'semanario', 'Weekly', 'titula',
    'Ausgabe', 'edizione', 'número', 'numero', 'graded', 'stufen',
    'niveaux', 'levels', 'Seiten', 'pages', 'páginas', 'paginas',
    'lezioni', 'leçons', 'lessen', 'уроков', '課', '강의']

def trim_abstract_v2(a):
    s = a.strip()
    # 1. Cut through VOL.N masthead marker
    m = re.search(r'VOL\.\d+\s*', s)
    if m:
        s = s[m.end():].strip()
        # If what follows is a masthead clause ending in an em-dash, take the story after it
        dm = re.search(r' — ', s[:300])
        if dm:
            pre = s[:dm.start()]
            if (len(pre) < 200 and any(w in pre for w in
                    ['Lucerna', 'Weekly', 'semanario', 'lettori', 'lectores',
                     'readers', 'learners', 'spiegazioni', 'Erklärungen',
                     'testi', 'Ausgabe', 'edizione', 'número', 'numero',
                     'para ', 'for ', 'di ', 'en ', 'auf ', 'mit '])):
                s = s[dm.end():].strip()
    # 2. Drop leading boilerplate/masthead sentences
    parts = re.split(r'(?<=[.!?。！？])\s+', s)
    i = 0
    while i < len(parts) - 1:
        sent = parts[i]
        if any(w in sent for w in BOILER_MARKERS):
            i += 1
        else:
            break
    s = ' '.join(parts[i:]).strip()
    # 3. Cut at first boilerplate marker in the remainder
    cuts = []
    for pat in (r'A2', r'B2', r'150', r'8 pagine', r'8 pages', r'8 Seiten',
                r'8 páginas', r'8 paginas'):
        mm = re.search(pat, s)
        if mm:
            cuts.append(mm.start())
    if cuts:
        s = s[:min(cuts)]
    s = re.sub(r'[\s,;、，；：:—\-–]+$', '', s).strip()
    if s:
        if any('\u4e00' <= ch <= '\u9fff' for ch in s):
            if s[-1] not in '。！？':
                s += '。'
        elif s[-1] not in '.!?"”':
            s += '.'
    return s

teasers = {}   # teasers[reader][target] = text
missing = []
for R in LANGS:
    teasers[R] = {}
    for S in LANGS:
        if (S, R) in editions:
            teasers[R][S] = trim_abstract_v2(editions[(S, R)]['abstract'])
        elif S == R:
            # same-language: excerpt of any edition with target S (excerpt is in S)
            cands = [(t, n) for (t, n) in editions if t == S]
            src = sorted(cands)[0]
            teasers[R][S] = editions[src]['excerpt'].strip()
        else:
            missing.append((S, R))

excerpts = {}
for S in LANGS:
    cands = sorted([(t, n) for (t, n) in editions if t == S])
    excerpts[S] = editions[cands[0]]['excerpt'].strip()

out = {
    'headlines': headlines,
    'teasers': teasers,
    'excerpts': excerpts,
    'missing_pairs_needing_override': missing,
}
with open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w43/cover-build/teasers.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

print('MISSING (cross-script, need manual override):', missing)
print()
for R in LANGS:
    print(f'===== reader {R} =====')
    for S in LANGS:
        t = teasers[R].get(S, '<<MISSING>>')
        print(f'  [{S}] ({len(t)}ch) {t[:180]}')
print()
print('EXCERPTS:')
for S in LANGS:
    print(f'  [{S}] {excerpts[S][:220]}')
