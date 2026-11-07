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

def trim_abstract(a):
    s = a
    # 1. strip masthead prefix through "VOL.N" + following colon
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
    # 2. drop a leading descriptor clause (zh-story masthead lines: "for X readers
    #    learning Chinese with real news: <story>") and leading boilerplate clauses
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
    # 3. cut trailing boilerplate: drop a trailing " — " clause carrying level/
    #    exercise markers, then cut at the first level/exercise marker
    #    (every "150"/"A2" in the W46 abstracts was verified to be boilerplate)
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
    # strip trailing level/exercise word fragments left by the cuts
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

teasers = {}   # teasers[reader][target] = text
missing = []
for R in LANGS:
    teasers[R] = {}
    for S in LANGS:
        if (S, R) in editions:
            teasers[R][S] = trim_abstract(editions[(S, R)]['abstract'])
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
