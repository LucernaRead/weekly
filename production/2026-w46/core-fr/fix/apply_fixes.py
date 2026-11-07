import re, sys
from pathlib import Path
ROOT = Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files"
BUILDS = {
    "core": ROOT/"weekly-report-w46-fr-build",
    "de": ROOT/"weekly-report-w46-fr-de-build",
    "en": ROOT/"weekly-report-w46-fr-en-build",
    "es": ROOT/"weekly-report-w46-fr-es-build",
    "it": ROOT/"weekly-report-w46-fr-it-build",
    "ja": ROOT/"weekly-report-w46-fr-ja-build",
    "ko": ROOT/"weekly-report-w46-fr-ko-build",
    "nl": ROOT/"weekly-report-w46-fr-nl-build",
    "pt": ROOT/"weekly-report-w46-fr-pt-build",
    "ru": ROOT/"weekly-report-w46-fr-ru-build",
    "zh-cn": ROOT/"weekly-report-w46-fr-zh-cn-build",
    "zh-tw": ROOT/"weekly-report-w46-fr-zh-tw-build",
}
def replace_once(path, old, new, label):
    t = path.read_text(encoding="utf-8")
    assert t.count(old) == 1, f"{label} {path}: count of {old!r} = {t.count(old)}"
    path.write_text(t.replace(old, new), encoding="utf-8")
    print(f"{label}: {old!r} -> {new!r}")

# D1: core French stem/key in every build copy (content identical modulo OUT)
for name, b in BUILDS.items():
    p = b/"content34.py"
    replace_once(p, "La foire n'est plus à Paris.", "La foire n'est pas à Paris.", f"D1-key[{name}]")
    replace_once(p, "(plus) La foire est à Paris. → ___", "(pas) La foire est à Paris. → ___", f"D1-stem[{name}]")

# D1 notes/bridge in every expl.py: n_neg3 := n_neg2 value; drop ne...plus from bridge_neg
for name, b in BUILDS.items():
    p = b/"expl.py"
    t = p.read_text(encoding="utf-8")
    m2 = re.search(r'"n_neg2": "([^"]*)"', t); m3 = re.search(r'"n_neg3": "([^"]*)"', t)
    assert m2 and m3, f"neg notes missing in {name}"
    print(f"D1-note[{name}]: n_neg2={m2.group(1)!r} n_neg3 before={m3.group(1)!r}")
    t = t.replace(f'"n_neg3": "{m3.group(1)}"', f'"n_neg3": "{m2.group(1)}"', 1)
    assert " / ne...plus" in t, f"bridge_neg pattern missing in {name}"
    t = t.replace(" / ne...plus", "", 1)
    p.write_text(t, encoding="utf-8")
    print(f"D1-note[{name}]: n_neg3 after={m2.group(1)!r}; bridge_neg ne...plus removed")

# D2: faithful stems for item 135 in 6 editions (key stays)
STEMS = {
    "it": ("Un programma spiega la Francia.", "Leggere un programma è già capire la Francia."),
    "nl": ("Een programma legt Frankrijk uit.", "Een programma lezen is al Frankrijk begrijpen."),
    "pt": ("Um programa explica a França.", "Ler um programa é já compreender a França."),
    "ru": ("Программа объясняет Францию.", "Читать программу — это уже понимать Францию."),
    "ja": ("番組がフランスを説明する。", "番組表を読むことは、すでにフランスを理解することだ。"),
    "ko": ("프로그램이 프랑스를 설명한다.", "프로그램표를 읽는 것은 이미 프랑스를 이해하는 것이다."),
}
for name, (old, new) in STEMS.items():
    p = BUILDS[name]/"expl.py"
    replace_once(p, f'"stem_e1": "{old}"', f'"stem_e1": "{new}"', f"D2[{name}]")

# D3: familier gloss -> familiar sense in 4 editions
GLOSS = {
    "ja": ("familier くだけた", "familier なじみのある"),
    "ko": ("familier 구어체", "familier 친숙한"),
    "ru": ("familier разговорное", "familier знакомый"),
    "zh-tw": ("familier 口語", "familier 熟悉的"),
}
for name, (old, new) in GLOSS.items():
    p = BUILDS[name]/"expl.py"
    replace_once(p, old, new, f"D3[{name}]")

print("ALL EDITS APPLIED")
