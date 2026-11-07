# -*- coding: utf-8 -*-
"""Generate one W46 EN fan-out build dir from the frozen W46 core build.

Pipeline (per native): copy W46 core build -> apply structural edits (furniture,
badge, OUT repoint, P8 keys block, bridge rename, svglib variant) -> apply
translation MAP (kept W45 pairs + authored table, longest-first, skip-if-absent
logged) -> apply W45 fragment pairs that still match -> verify post-conditions:
no string byte-identical to a W46 core CJK string remains; Latin natives: zero
CJK chars in the six source files.

Usage: python gen_fanout.py <native>   (native in de fr es it pt nl ru ja ko zh-tw)
"""
import ast, json, os, re, shutil, sys

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE_BUILD = os.path.join(BASE, "hidden_files/weekly-report-w46-en-build")
W45 = os.path.join(BASE, "hidden_files")
H46 = os.path.join(BASE, "hidden_files/w46")
FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]
CJK = re.compile(r"[\u4e00-\u9fff]")

PRINT_SET = [8, 9, 15, 23, 31, 32, 37, 39, 48, 50, 55, 57, 67, 68, 72, 82, 83, 84, 85, 86, 87,
             89, 90, 92, 103, 104, 106, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118,
             119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134,
             135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]

# footer, page line, gloss prefix, rename, masthead (y,text), badge (text,color),
# answers head, keys style, separator template
CFG = {
 "de": dict(footer="The Lucerna · ENGLISH WEEKLY VOL.3 · Englischer Text · Deutsche Erklärungen",
   pageline='f"Seite {n} von {total}"', gloss="Anmerkung | ", rename=None,
   masthead=(330, "ENGLISCHES WOCHENBLATT · VOL.3 · GEDENKEN · FUSSBALL · FILME"),
   badge=("ENGLISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", "OLIVE"),
   answers="ANSWERS · Alle Antworten mit Anmerkungen (Seiten 1–8)", keys="all",
   sep="— Seite {pg} —", svglib="core"),
 "fr": dict(footer="The Lucerna · HEBDOMADAIRE ANGLAIS VOL.3 · TEXTE EN ANGLAIS · EXPLICATIONS EN FRANÇAIS",
   pageline='f"Page {n} sur {total}"', gloss="Note | ", rename="instrline",
   masthead=(338, "HEBDOMADAIRE EN ANGLAIS · VOL.3 · COMMÉMORATION · FOOTBALL · CINÉMA"),
   badge=("TEXTE EN ANGLAIS · EXPLICATIONS EN FRANÇAIS — L’ÉDITION POUR LES LECTEURS FRANCOPHONES", "BRICK"),
   answers="ANSWERS · Toutes les réponses commentées (pages 1 à 8)", keys="all",
   sep="— Page {pg} —", svglib="core"),
 "es": dict(footer="The Lucerna · SEMANARIO INGLÉS VOL.3 · TEXTO EN INGLÉS · EXPLICACIONES EN ESPAÑOL",
   pageline='f"Página {n} de 8"', gloss="Nota — ", rename=None,
   masthead=(338, "SEMANARIO EN INGLÉS · VOL.3 · CONMEMORACIÓN · FÚTBOL · CINE"),
   badge=("TEXTOS EN INGLÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", "BRICK"),
   answers="ANSWERS · Respuestas y notas (páginas 1–8)", keys="explicit",
   sep="— Página {pg} —", svglib="core"),
 "it": dict(footer="The Lucerna · SETTIMANALE INGLESE VOL.3 · TESTI IN INGLESE · SPIEGAZIONI IN ITALIANO",
   pageline='f"Pagina {n} di {total}"', gloss="Nota — ", rename=None,
   masthead=(338, "SETTIMANALE IN INGLESE · VOL.3 · COMMEMORAZIONE · FOOTBALL · FILM"),
   badge=("TESTI IN INGLESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI", "BRICK"),
   answers="ANSWERS · Risposte e note (pagine 1–8)", keys="explicit",
   sep="— Pagina {pg} —", svglib="core"),
 "pt": dict(footer="The Lucerna · SEMANÁRIO INGLÊS VOL.3 · TEXTOS EM INGLÊS · EXPLICAÇÕES EM PORTUGUÊS",
   pageline='f"Página {n} de 8"', gloss="Nota — ", rename=None,
   masthead=(338, "SEMANÁRIO EM INGLÊS · VOL.3 · COMEMORAÇÃO · FUTEBOL · CINEMA"),
   badge=("TEXTOS EM INGLÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", "BRICK"),
   answers="ANSWERS · Respostas e notas (páginas 1–8)", keys="explicit",
   sep="— Página {pg} —", svglib="core"),
 "nl": dict(footer="The Lucerna · ENGELS WEEKBLAD VOL.3 · TEKSTEN IN HET ENGELS · UITLEG IN HET NEDERLANDS",
   pageline='f"Pagina {n} van {total}"', gloss="Uitleg — ", rename=None,
   masthead=(330, "ENGELS WEEKBLAD · VOL.3 · HERDENKING · VOETBAL · FILMS"),
   badge=("TEKSTEN IN HET ENGELS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", "OLIVE"),
   answers="ANSWERS · Alle antwoorden met toelichting (pagina 1–8)", keys="all",
   sep="— Pagina {pg} —", svglib="core"),
 "ru": dict(footer="The Lucerna · АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА АНГЛИЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ",
   pageline='f"Страница {n} из 8"', gloss="Пояснение — ", rename=None,
   masthead=(338, "АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.3 · ПАМЯТЬ · ФУТБОЛ · КИНО"),
   badge=("ТЕКСТЫ НА АНГЛИЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", "BRICK"),
   answers="ANSWERS · Все ответы с пояснениями (стр. 1–8)", keys="explicit",
   sep="— СТРАНИЦА {pg} —", svglib="core"),
 "ja": dict(footer="The Lucerna · 英語週刊 VOL.3 · 本文は英語 · 解説は日本語",
   pageline='f"{n} ページ（全 {total} ページ）"', gloss="解説 — ", rename=None,
   masthead=(330, "英 語 週 刊 · VOL.3 · 記 念 · フットボール · 映 画"),
   badge=("英語テキスト · 日本語の解説 — 日本語読者のための版", "BRICK"),
   answers="ANSWERS · 全解答と解説（1–8ページ）", keys="explicit",
   sep="— {pg} ページ —", svglib="ja"),
 "ko": dict(footer="The Lucerna · 영어 주간지 VOL.3 · 텍스트는 영어 · 해설은 한국어",
   pageline='f"제 {n} 면 / 총 {total} 면"', gloss="해설 — ", rename=None,
   masthead=(330, "영어 주간지 · VOL.3 · 기념 · 축구 · 영화"),
   badge=("영어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판", "BRICK"),
   answers="ANSWERS · 모든 정답과 간단한 설명(1–8면)", keys="explicit",
   sep="— 제 {pg} 면 —", svglib="core"),
 "zh-tw": dict(footer="The Lucerna · 英語週報 VOL.3 · 正文英語 · 講解繁體中文",
   pageline=None, gloss="譯注｜", rename="expl",
   masthead=(330, "英 語 週 報 · VOL.3 · 紀 念 · 足 球 · 電 影"),
   badge=("英語正文 · 繁體中文講解 — 給繁體中文讀者的版本", "BRICK"),
   answers="ANSWERS · 全部答案與簡析（第 1–8 版）", keys="explicit",
   sep="— 第 {pg} 版 —", svglib="zh-tw"),
}

def rep1(text, old, new, fname, what):
    n = text.count(old)
    assert n == 1, f"{fname} {what}: count {n} != 1 for {old[:60]!r}"
    return text.replace(old, new)

def main(native):
    cfg = CFG[native]
    dst = os.path.join(BASE, "hidden_files", f"weekly-report-w46-en-{native}-build")
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(CORE_BUILD, dst, ignore=shutil.ignore_patterns("__pycache__"))
    ed = f"weekly-report-w46-en-{native}"
    texts = {f: open(os.path.join(dst, f), encoding="utf-8").read() for f in FILES + ["svglib.py"]}

    # ---- structural edits (pristine copy) ----
    b = texts["bslib4.py"]
    b = rep1(b, '"The Lucerna · 英语周报 VOL.3 · LUCERNA ENGLISH WEEKLY"',
             f'"{cfg["footer"]}"', "bslib4.py", "footer")
    if cfg["pageline"]:
        b = rep1(b, 'f"第 {n} 版 / 共 {total} 版"', cfg["pageline"], "bslib4.py", "pageline")
    b = rep1(b, '"译注｜" + s', f'"{cfg["gloss"]}" + s', "bslib4.py", "gloss prefix")
    if cfg["rename"]:
        b = rep1(b, "def bridge(self, s", f"def {cfg['rename']}(self, s", "bslib4.py", "rename def")
    texts["bslib4.py"] = b

    # Latin-script fan-outs: the P1 gloss bridge lengthens to 3 lines at 20.5pt
    # and pushes the last headline exercise past the rule; 19.5pt restores 2 lines.
    if native in ("de", "fr", "es", "it", "pt", "nl", "ru"):
        c12pre = texts["content12.py"]
        old_bridge = 'f.bridge("讲解｜an armistice 停战协定 · a veteran 退伍军人 · to fall silent 沉寂。")'
        assert c12pre.count(old_bridge) == 1, "P1 bridge line not found"
        texts["content12.py"] = c12pre.replace(old_bridge, old_bridge[:-1] + ", size=19.5)")

    c12 = texts["content12.py"]
    c12 = rep1(c12, 'p.text(975, 330, "英 语 周 报 · VOL.3 · 纪 念 · 足 球 · 电 影", 46, "serif", True, INK, anchor="middle")',
               f'p.text(975, {cfg["masthead"][0]}, "{cfg["masthead"][1]}", 46, "serif", True, INK, anchor="middle")',
               "content12.py", "masthead")
    c12 = rep1(c12, 'p.text(975, 372, "THE LEARNERS\' WEEKLY — REAL LIFE, IN ENGLISH, FROM LONDON TO MUNICH", 19, "sans", False, GREY, anchor="middle")',
               f'p.text(975, 372, "{cfg["badge"][0]}", 19.5, "sans", True, {cfg["badge"][1]}, anchor="middle")',
               "content12.py", "badge")
    texts["content12.py"] = c12

    # bridge rename at call sites
    if cfg["rename"]:
        tot = 0
        for f in FILES[:5]:
            c = texts[f].count(".bridge(")
            texts[f] = texts[f].replace(".bridge(", f".{cfg['rename']}(")
            tot += c
        assert tot >= 1, "no .bridge( call sites found"

    # OUT repoint + render ED path
    for f in FILES[:5]:
        texts[f] = rep1(texts[f], "weekly-report-w46-en-core", ed, f, "OUT repoint")
    rp = os.path.join(dst, "render.py")
    rtext = open(rp, encoding="utf-8").read()
    assert rtext.count("weekly-report-w46-en-core") == 1
    open(rp, "w", encoding="utf-8").write(rtext.replace("weekly-report-w46-en-core", ed))

    # P8 keys block
    c8 = texts["content8.py"]
    c8 = rep1(c8, 'p.text(MX, ky + 26, "ANSWERS · 全部答案与简析（第 1–8 版）", 26, "sans", True, OLIVE)',
              f'p.text(MX, ky + 26, "{cfg["answers"]}", 26, "sans", True, OLIVE)', "content8.py", "answers head")
    if cfg["keys"] == "all":
        c8 = rep1(c8, 'kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")',
                  'kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2530, tag="P8-keys")', "content8.py", "kf bottom")
        c8 = rep1(c8, '    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
                  f'    kf.para(f"{cfg["sep"]}", 16, "sans", True, OLIVE, 1.26, 3)', "content8.py", "separator")
        c8 = rep1(c8, '        if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):\n            s += f"（{e[\'note\']}）"',
                  '        if e["note"]:\n            s += f" ({e[\'note\']})"', "content8.py", "note condition")
        c8 = rep1(c8, '    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)',
                  '    kf.para(" · ".join(parts), 13.5, "sans", False, INK, 1.26, 9)', "content8.py", "keys font")
    else:
        c8 = rep1(c8, '    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
                  f'    kf.para(f"{cfg["sep"]}", 17, "sans", True, OLIVE, 1.28, 3)', "content8.py", "separator")
        c8 = rep1(c8, '        if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):\n            s += f"（{e[\'note\']}）"',
                  '        if e["note"] and (pg == 8 or e["n"] in PRINT_NOTES):\n            s += f" ({e[\'note\']})"', "content8.py", "note condition")
        anchor = 'kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")'
        assert c8.count(anchor) == 1
        c8 = c8.replace(anchor, anchor + "\nPRINT_NOTES = " + repr(PRINT_SET), 1)
    texts["content8.py"] = c8

    # P8 battery packing: the W46 dialogue paragraph is 10 lines at 21.5pt and
    # the core battery ends 4px above its bottom; fan-out heads/bridges cost a
    # few px more, so fan-outs use 20.5pt for the dialogue and gap=8 on every
    # battery exercise (uniform across fan-outs; English text unchanged).
    c8b = texts["content8.py"]
    old_dlg = '— Have a good day.", 21.5)'
    assert c8b.count(old_dlg) == 1, "dialogue tail not found"
    c8b = c8b.replace(old_dlg, '— Have a good day.", 20.5)')
    n_ex = c8b.count("size=20.5)")
    assert n_ex >= 1, "no size=20.5 ex calls"
    c8b = c8b.replace("size=20.5)", "size=20.5, gap=8)")
    texts["content8.py"] = c8b

    # svglib variant
    if cfg["svglib"] != "core":
        src = os.path.join(W45, f"weekly-report-w45-en-{native}-build", "svglib.py")
        shutil.copyfile(src, os.path.join(dst, "svglib.py"))

    for f in FILES:
        open(os.path.join(dst, f), "w", encoding="utf-8").write(texts[f])

    # ---- translation MAP: kept + authored, longest-first ----
    table = {}
    kp = os.path.join(H46, f"kept-{native}.json")
    if os.path.exists(kp):
        table.update(json.load(open(kp, encoding="utf-8")))
    ap = os.path.join(H46, f"authored-{native}.json")
    if os.path.exists(ap):
        table.update(json.load(open(ap, encoding="utf-8")))
    skipped = []
    for f in FILES:
        p = os.path.join(dst, f)
        t = open(p, encoding="utf-8").read()
        for old, new in sorted(table.items(), key=lambda kv: -len(kv[0])):
            if old in t:
                t = t.replace(old, new)
            else:
                skipped.append((f, old))
        open(p, "w", encoding="utf-8").write(t)
    print(f"[{native}] MAP entries={len(table)} skips={len(skipped)}")

    # ---- W45 fragment pairs that still match (ES/PT/RU R-style; harmless elsewhere) ----
    frag_applied = apply_fragment_pairs(native, dst)
    print(f"[{native}] fragment pairs applied={frag_applied}")

    # ---- post-conditions ----
    core_strs = set(json.load(open(os.path.join(H46, "core-cjk-strings.json"), encoding="utf-8")))
    def strs_in(path):
        out = set()
        tree = ast.parse(open(path, encoding="utf-8").read())
        for node in ast.walk(tree):
            v = None
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                v = node.value
            elif isinstance(node, ast.JoinedStr):
                v = "".join(p.value if isinstance(p, ast.Constant) else "{...}" for p in node.values)
            if v and CJK.search(v):
                out.add(v)
        return out
    leftovers = []
    for f in FILES:
        rem = strs_in(os.path.join(dst, f)) & core_strs
        leftovers += [(f, s) for s in sorted(rem)]
    if leftovers:
        print(f"[{native}] LEFTOVER core strings: {len(leftovers)}")
        for f, s in leftovers[:40]:
            print("   ", f, s[:100])
        sys.exit(1)
    if native not in ("ja", "ko", "zh-tw"):
        for f in FILES:
            t = open(os.path.join(dst, f), encoding="utf-8").read()
            assert not CJK.search(t), f"{native} {f}: CJK remains"
            assert "｜" not in t, f"{native} {f}: fullwidth bar remains"
    print(f"[{native}] OK -> {dst}")

# ---- fragment-pair extraction (bootstrap2 logic, condensed) ----
def strval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        return "".join(p.value if isinstance(p, ast.Constant) else "{...}" for p in node.values)
    return None

def tuples_of(node):
    out = []
    if isinstance(node, ast.List):
        for el in node.elts:
            if isinstance(el, ast.Tuple) and len(el.elts) >= 2:
                a, b = strval(el.elts[0]), strval(el.elts[1])
                if a is not None and b is not None:
                    out.append((a, b))
    return out

def extract_pairs(tree):
    env = {}
    pairs = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if not isinstance(t, ast.Name):
                    continue
                if isinstance(node.value, ast.List):
                    env[t.id] = tuples_of(node.value)
                elif isinstance(node.value, ast.Dict):
                    d = {}
                    for k, v in zip(node.value.keys, node.value.values):
                        kk = strval(k)
                        if isinstance(v, ast.List):
                            vv = tuples_of(v)
                        elif isinstance(v, ast.Name):
                            vv = ("REF", v.id)
                        elif isinstance(v, ast.Dict):
                            vv = {strval(k2): strval(v2) for k2, v2 in zip(v.keys, v.values)
                                  if strval(k2) is not None and strval(v2) is not None}
                        else:
                            vv = strval(v)
                        if kk is not None:
                            d[kk] = vv
                    env[t.id] = d
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AugAssign)) and isinstance(node.value, ast.List):
            for el in node.value.elts:
                if isinstance(el, ast.Tuple) and len(el.elts) >= 3:
                    f, a, b = strval(el.elts[0]), strval(el.elts[1]), strval(el.elts[2])
                    if f in FILES and a is not None and b is not None:
                        pairs.append((f, a, b))
    for name, val in env.items():
        if isinstance(val, dict):
            for k, v in val.items():
                if isinstance(v, str):
                    for f in FILES:
                        pairs.append((f, k, v))
                elif isinstance(v, tuple) and len(v) == 2 and v[0] == "REF":
                    v2 = env.get(v[1], [])
                    if isinstance(v2, list) and k in FILES:
                        for a, b in v2:
                            pairs.append((k, a, b))
                elif isinstance(v, list) and k in FILES:
                    for a, b in v:
                        pairs.append((k, a, b))
    named_lists = {k: v for k, v in env.items() if isinstance(v, list)}
    def visit(node):
        if isinstance(node, ast.Call):
            fn = node.func
            nm = fn.attr if isinstance(fn, ast.Attribute) else (fn.id if isinstance(fn, ast.Name) else "")
            if nm == "rep" and len(node.args) >= 3:
                f, o, n = strval(node.args[0]), strval(node.args[1]), strval(node.args[2])
                if f and o is not None:
                    pairs.append((f, o, n))
            elif nm == "rep_all" and len(node.args) >= 2:
                f = strval(node.args[0])
                lst = node.args[1]
                items = tuples_of(lst) if isinstance(lst, ast.List) else (named_lists.get(lst.id, []) if isinstance(lst, ast.Name) else [])
                for a, b in items:
                    pairs.append((f, a, b))
        for ch in ast.iter_child_nodes(node):
            visit(ch)
    visit(tree)
    if "GLOBAL" in named_lists:
        for f in FILES[:5]:
            for a, b in named_lists["GLOBAL"]:
                pairs.append((f, a, b))
    seen, out = set(), []
    for p in pairs:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out

def apply_fragment_pairs(native, dst):
    tp = os.path.join(W45, f"weekly-report-w45-en-{native}-build", "transform.py")
    tree = ast.parse(open(tp, encoding="utf-8").read())
    pairs = extract_pairs(tree)
    n = 0
    for fname, old, new in pairs:
        if fname not in FILES or "VOL.2" in old or "VOL.2" in new or "w45-en-core" in old or "w45-en-core" in new:
            continue
        if "英语周报" in old and "LUCERNA ENGLISH WEEKLY" in old:
            continue  # footer handled structurally
        p = os.path.join(dst, fname)
        t = open(p, encoding="utf-8").read()
        if old in t:
            open(p, "w", encoding="utf-8").write(t.replace(old, new))
            n += 1
    return n

if __name__ == "__main__":
    main(sys.argv[1])
