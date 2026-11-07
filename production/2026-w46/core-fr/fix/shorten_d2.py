from pathlib import Path
ROOT = Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files"
STEMS = {
    "it": ("Leggere un programma è già capire la Francia.", "Leggere un programma è capire la Francia."),
    "nl": ("Een programma lezen is al Frankrijk begrijpen.", "Een programma lezen is Frankrijk begrijpen."),
    "pt": ("Ler um programa é já compreender a França.", "Ler um programa é compreender a França."),
    "ru": ("Читать программу — это уже понимать Францию.", "Читая программу, понимаешь Францию."),
    "ja": ("番組表を読むことは、すでにフランスを理解することだ。", "番組表を読むとフランスが分かる。"),
    "ko": ("프로그램표를 읽는 것은 이미 프랑스를 이해하는 것이다.", "프로그램표를 읽으면 프랑스를 이해한다."),
}
for name, (old, new) in STEMS.items():
    p = ROOT/f"weekly-report-w46-fr-{name}-build/expl.py"
    t = p.read_text(encoding="utf-8")
    assert t.count(f'"stem_e1": "{old}"') == 1, name
    p.write_text(t.replace(f'"stem_e1": "{old}"', f'"stem_e1": "{new}"'), encoding="utf-8")
    print(f"D2-short[{name}]: {old!r} -> {new!r}")
print("DONE")
