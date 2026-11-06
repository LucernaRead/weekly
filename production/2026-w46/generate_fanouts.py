# -*- coding: utf-8 -*-
"""Generate W46 IT fan-out builds from the frozen W46 core build dir.

Per language: copy core build dir -> w46-it-<lang>-build, write transform.py
(harvested W45 pairs + E-section re-aim + badge/subtitle/footer + fresh
translations), run it, then run.py + render.py. Never touches the core build
dir or the W45 dirs. Run: tools/venv/bin/python hidden_files/w46/generate_fanouts.py [lang ...]
"""
import json, pathlib, shutil, subprocess, sys

ROOT = pathlib.Path.home() / "workspace/goals/lucernaread-social-media-operations"
HF = ROOT / "hidden_files"
CORE_BUILD = HF / "weekly-report-w46-it-build"
W45 = HF / "weekly-report-w45-it-build"
sys.path.insert(0, str(HF / "w46"))
from translations import T

PY = str(ROOT / "tools/venv/bin/python")
FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py", "svglib.py"]
SUFFIX = {"en": "EN", "de": "DE", "fr": "FR", "es": "ES", "pt": "PT", "nl": "NL", "ru": "RU", "ja": "JA", "ko": "KO", "zh-tw": "ZHTW"}

E_INSTR = {
    "en": ("Translate into English", "Translate into Italian"),
    "de": ("Übersetzen", "Übersetzen"),
    "fr": ("Traduire en français", "Traduire en italien"),
    "es": ("Traduce", "Traduce"),
    "pt": ("Traduzir para português", "Traduzir para italiano"),
    "nl": ("Vertaal", "Vertaal"),
    "ru": ("Переведите", "Переведите"),
    "ja": ("日本語に翻訳", "イタリア語に翻訳"),
    "ko": ("번역", "번역"),
    "zh-tw": ("翻譯", "翻譯"),
}
# badge line (975,574,22pt BRICK) for insert-languages; (975,372,20pt BRICK) replacements for es/nl/ja; none for ko
BADGE_574 = {
    "en": "Text in Italian · Explanations in English — the edition for English-speaking readers",
    "de": "ITALIENISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER",
    "fr": "TEXTES EN ITALIEN · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES",
    "pt": "TEXTOS EM ITALIANO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA",
    "ru": "ТЕКСТЫ НА ИТАЛЬЯНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ",
    "zh-tw": "義大利語正文 · 繁體中文講解 — 給繁體中文讀者的版本",
}
BADGE_372 = {
    "es": "TEXTOS EN ITALIANO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES",
    "nl": "TEKSTEN IN HET ITALIAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS",
    "ja": "イタリア語テキスト · 日本語の解説 — 日本語読者のための版",
}
# subtitle (y=330) topics segment per language, from W45 sibling line-19 patterns
SUB_HEAD = {
    "en": ("THE ITALIAN WEEKLY", 44), "de": ("ITALIENISCH", 46), "fr": ("JOURNAL ITALIEN", 46),
    "es": ("SEMANARIO ITALIANO", 46), "pt": ("SEMANÁRIO ITALIANO", 46), "nl": ("ITALIAANS WEEKBLAD", 43),
    "ru": ("ИТАЛЬЯНСКИЙ", 46), "ja": ("イ タ リ ア 語 週 刊", 46), "ko": ("이탈리아어 주간지", 46),
    "zh-tw": ("意 大 利 語 週 報", 46),
}
SUB_TOPICS = {
    "en": "SAN MARTINO · IL VINO NUOVO · L'ITALIA", "de": "SAN MARTINO · IL VINO NUOVO · L'ITALIA",
    "fr": "SAN MARTINO · IL VINO NUOVO · L'ITALIA", "es": "SAN MARTINO · VINO NUOVO · ITALIA",
    "pt": "SAN MARTINO · VINO NUOVO · ITALIA", "nl": "SAN MARTINO · IL VINO NUOVO · L'ITALIA",
    "ru": "SAN MARTINO · IL VINO NUOVO · L'ITALIA", "ja": "SAN MARTINO · IL VINO NUOVO · L'ITALIA",
    "ko": "SAN MARTINO · IL VINO NUOVO · L'ITALIA", "zh-tw": "SAN MARTINO · IL VINO NUOVO · L'ITALIA",
}
BAND_RIGHT_LINE = 'p.text(RIGHT - 30, 522, "圣马丁之周 · 详见第 2 版", 21, "sans", False, "#b3a06a", anchor="end")'
TAGLINE_LINE = 'p.text(975, 372, "IL GIORNALE SETTIMANALE PER IMPARARE — L\'ITALIA VERA, IN ITALIANO, DALL\'ITALIA", 19, "sans", False, GREY, anchor="middle")'
SUBTITLE_OLD = 'p.text(975, 330, "意 大 利 语 周 报 · VOL.3 · SAN MARTINO · IL VINO NUOVO · L\'ITALIA", 46, "serif", True, INK, anchor="middle")'

E_FRAGS = [
    ('f.ex("A2", "翻译", "圣马丁节葡萄汁变成酒。", "对照原文",\n     "A San Martino ogni mosto diventa vino. → ___", instr="翻译", size=15.5, gap=1)',
     "137"),
    ('f.ex("B1", "翻译", "周四晚上意大利对法国。", "si gioca = 进行比赛",\n     "Giovedì sera si gioca Italia–Francia. → ___", instr="翻译", size=15.5, gap=1)',
     "138"),
    ('f.ex("B1", "翻译", "周日晚上，比利时对意大利。", "si gioca = 进行比赛",\n     "Domenica sera si gioca Belgio–Italia. → ___", instr="翻译", size=15.5, gap=1)',
     "139"),
    ('f.ex("B2", "翻译", "Ogni cifra deve essere chiara.", "dovere = 必须",\n     "每个数字都必须清楚。→ ___", instr="翻译", size=15.5, gap=1)',
     "140"),
]

def e_new(lang, which):
    t = T[lang]
    i1, i2 = E_INSTR[lang]
    if which == "137":
        return ('f.ex("A2", "翻译", "%s", "%s",\n     "A San Martino ogni mosto diventa vino. → ___", instr="%s", size=15.5, gap=1)'
                % (t["圣马丁节葡萄汁变成酒。"], t["对照原文"], i1))
    if which == "138":
        return ('f.ex("B1", "翻译", "%s", "%s",\n     "Giovedì sera si gioca Italia–Francia. → ___", instr="%s", size=15.5, gap=1)'
                % (t["周四晚上意大利对法国。"], t["si gioca = 进行比赛"], i1))
    if which == "139":
        return ('f.ex("B1", "翻译", "%s", "%s",\n     "Domenica sera si gioca Belgio–Italia. → ___", instr="%s", size=15.5, gap=1)'
                % (t["周日晚上，比利时对意大利。"], t["si gioca = 进行比赛"], i1))
    return ('f.ex("B2", "翻译", "Ogni cifra deve essere chiara.", "%s",\n     "%s", instr="%s", size=15.5, gap=1)'
            % (t["dovere = 必须"], t["每个数字都必须清楚。→ ___"], i2))

def load_pairs(lang):
    if lang == "zh-tw":
        raw = json.load(open(str(HF / "w46/pairs/zhtw-litmap.json"), encoding="utf-8"))
        pairs = []
        for k, vs in raw.items():
            # litmap keys/values include surrounding quotes; keep as text-level pairs
            if any("\u4e00" <= c <= "\u9fff" for c in k):
                pairs.append((k, sorted(vs)[0]))
        return pairs
    raw = json.load(open(str(HF / f"w46/pairs/w45-{lang}-pairs.json"), encoding="utf-8"))
    return [(k, sorted(vs)[0]) for k, vs in raw.items()]

def build_transform(lang):
    lines = []
    lines.append("# -*- coding: utf-8 -*-")
    lines.append(f'"""W46 IT core -> IT x {lang.upper()} fan-out transform (build copy only). Generated."""')
    lines.append("import pathlib, sys")
    lines.append(f"B = pathlib.Path(__file__).resolve().parent")
    lines.append("FILES = ['content12.py','content34.py','content56.py','content7.py','content8.py','bslib4.py','svglib.py']")
    lines.append("def rep(files, old, new, expect=None, loud=True):")
    lines.append("    total = 0")
    lines.append("    for fn in files:")
    lines.append("        p = B / fn; t = p.read_text(encoding='utf-8'); c = t.count(old); total += c")
    lines.append("        if c: p.write_text(t.replace(old, new), encoding='utf-8')")
    lines.append("    if expect is not None and total != expect:")
    lines.append("        print(f'COUNT MISMATCH: {old!r} found {total}, expected {expect}'); sys.exit(1)")
    lines.append("    if total == 0 and loud:")
    lines.append("        print(f'NOT FOUND (skip): {old!r}'); return 0")
    lines.append("    return total")
    lines.append("def repq(old, new):")
    lines.append('    """Replace a literal value in either quote form, across FILES."""')
    lines.append("    for q in ('\"', \"'\"):")
    lines.append("        o, n = q + old + q, q + new + q")
    lines.append("        if rep(FILES, o, n, loud=False): return True")
    lines.append("    print(f'NOT FOUND literal: {old!r}'); return False")
    # Phase 0: E-section re-aim (asserted)
    lines.append("# --- E-section re-aim (keys 137-139 -> reader language; 140 stem -> reader language) ---")
    for old, which in E_FRAGS:
        lines.append(f"rep(['content8.py'], {old!r}, {e_new(lang, which)!r}, expect=1)")
    # Phase A: harvested pairs (skip-if-absent)
    lines.append("# --- harvested W45 pairs (skip if absent in W46 text) ---")
    for old, new in load_pairs(lang):
        lines.append(f"rep(FILES, {old!r}, {new!r}, loud=False)")
    # Phase B: OUT repointing + render names
    lines.append("# --- repoint OUT + render names ---")
    lines.append(f"rep(['content12.py','content34.py','content56.py','content7.py','content8.py'], 'weekly-report-w46-it-core', 'weekly-report-w46-it-{lang}', expect=5)")
    lines.append(f"rep(['render.py'], 'weekly-report-w46-it-core', 'weekly-report-w46-it-{lang}', expect=1)")
    lines.append(f"rep(['render.py'], 'La-Lucerna-VOL3.pdf', 'La-Lucerna-VOL3-{SUFFIX[lang]}.pdf', expect=1)")
    # Phase C: subtitle
    head, size = SUB_HEAD[lang]
    sub_new = f'p.text(975, 330, "{head} · VOL.3 · {SUB_TOPICS[lang]}", {size}, "serif", True, INK, anchor="middle")'
    lines.append("# --- P1 subtitle ---")
    lines.append(f"rep(['content12.py'], {SUBTITLE_OLD!r}, {sub_new!r}, expect=1)")
    # Phase D: badge
    if lang in BADGE_574:
        band_new = BAND_RIGHT_LINE.replace("圣马丁之周 · 详见第 2 版", T[lang]["圣马丁之周 · 详见第 2 版"])
        badge_line = f'p.text(975, 574, "{BADGE_574[lang]}", 22, "sans", True, BRICK, anchor="middle")'
        lines.append("# --- P1 pairing badge (inserted, y=574) ---")
        lines.append(f"rep(['content12.py'], {BAND_RIGHT_LINE!r}, {(band_new + chr(10) + badge_line)!r}, expect=1)")
    elif lang in BADGE_372:
        badge_line = f'p.text(975, 372, "{BADGE_372[lang]}", 20, "sans", True, BRICK, anchor="middle")'
        lines.append("# --- P1 pairing badge (replaces tagline, y=372; pairs may already have badged it) ---")
        lines.append(f"rep(['content12.py'], {TAGLINE_LINE!r}, {badge_line!r}, expect=None)")
        lines.append(f"assert {BADGE_372[lang]!r} in open('content12.py', encoding='utf-8').read(), 'badge text missing after pairs/badge rep'")
    # Phase E: fresh translations (skip-if-absent)
    lines.append("# --- fresh W46 translations ---")
    for old, new in T[lang].items():
        if old == "圣马丁之周 · 详见第 2 版" and lang in BADGE_574:
            continue  # handled by badge rep
        lines.append(f"repq({old!r}, {new!r})")
    # Phase E2: P2 box title must fit the 434px box: bare title, no suffix (any suffix form)
    lines.append("# --- P2 box title: bare (suffix would overflow the 434px box) ---")
    lines.append("import re as _re")
    lines.append("_t = open('content12.py', encoding='utf-8').read()")
    lines.append("_t2, _n = _re.subn(r'f\\.box\\(\"[^\"]*FRASE PER RICORDARE[^\"]*\"', 'f.box(\"LA FRASE PER RICORDARE\"', _t, count=1)")
    lines.append("assert _n == 1, 'P2 box title line not found'")
    lines.append("open('content12.py', 'w', encoding='utf-8').write(_t2)")
    # Phase E3: cifre box title bare (suffix overflows the 434px box in several languages)
    lines.append("# --- cifre box title: bare ---")
    lines.append("_t = open('content12.py', encoding='utf-8').read()")
    lines.append("_t2, _n = _re.subn(r'\\.box\\(\"LA SETTIMANA IN CIFRE · [^\"]*\"', '.box(\"LA SETTIMANA IN CIFRE\"', _t, count=1)")
    lines.append("assert _n == 1, 'cifre box title line not found'")
    lines.append("open('content12.py', 'w', encoding='utf-8').write(_t2)")
    # Phase E4: DE P7 word-box title too wide by 5.5px
    if lang == "de":
        lines.append("repq('LA PAROLA · DAS WORT DER WOCHE', 'LA PAROLA · DAS WORT')")
    # Phase E5: P8 keys smaller in long-note languages (de/es/fr/pt/ru) so all 150 fit above 2552
    if lang in ("de", "es", "fr", "pt", "ru"):
        lines.append("rep(['content8.py'], 'af.para(txt, 13, lh=1.14, gap=0.5, split=False)', 'af.para(txt, 12.5, lh=1.12, gap=0.5, split=False)', expect=1)")
    # Phase G: normalize U+2019 -> ASCII apostrophe (CJK font renders U+2019 with a visible gap)
    lines.append("# --- normalize curly apostrophe (font renders U+2019 with a gap) ---")
    lines.append("import pathlib as _pl")
    lines.append("for _fn in ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py', 'bslib4.py']:")
    lines.append("    _p = _pl.Path(_fn)")
    lines.append("    _p.write_text(_p.read_text(encoding='utf-8').replace('’', \"'\"), encoding='utf-8')")
    # Phase F: svglib docstring fragment
    lines.append("rep(['svglib.py'], 'for 重阳.', 'for Double Ninth Festival.', loud=False)")
    lines.append("print('transform done')")
    return "\n".join(lines) + "\n"

def main():
    langs = sys.argv[1:] or list(SUFFIX)
    for lang in langs:
        dest = HF / f"weekly-report-w46-it-{lang}-build"
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(CORE_BUILD, dest, ignore=shutil.ignore_patterns("__pycache__"))
        if lang in ("ja", "zh-tw"):
            src_svg = HF / f"weekly-report-w45-it-{lang}-build/svglib.py"
            shutil.copy2(src_svg, dest / "svglib.py")
            print(f"{lang}: svglib.py copied from W45 {lang} build (font-face/kinsoku patch)")
        (dest / "transform.py").write_text(build_transform(lang), encoding="utf-8")
        r = subprocess.run([PY, "transform.py"], cwd=dest, capture_output=True, text=True)
        print(f"===== {lang} transform rc={r.returncode} =====")
        print(r.stdout[-1500:])
        print(r.stderr[-500:])
        if r.returncode != 0:
            print(f"{lang}: TRANSFORM FAILED — stopping"); return 1
        r = subprocess.run([PY, "run.py"], cwd=dest, capture_output=True, text=True)
        print(f"===== {lang} run.py rc={r.returncode} =====")
        tail = "\n".join(r.stdout.splitlines()[-14:])
        print(tail); print(r.stderr[-500:])
        if r.returncode != 0:
            print(f"{lang}: BUILD FAILED — stopping"); return 1
        if "FLOW OVERFLOW" in r.stdout or "HEAD TOO WIDE" in r.stdout:
            print(f"{lang}: OVERFLOW/WIDE warnings present — see build log above")
        r = subprocess.run([PY, "render.py"], cwd=dest, capture_output=True, text=True)
        print(f"===== {lang} render.py rc={r.returncode} =====")
        print("\n".join(r.stdout.splitlines()[-4:])); print(r.stderr[-500:])
        if r.returncode != 0:
            print(f"{lang}: RENDER FAILED — stopping"); return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
