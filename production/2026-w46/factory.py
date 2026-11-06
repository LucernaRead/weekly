# -*- coding: utf-8 -*-
"""W46 KO fan-out factory: copy W45 build -> W46 build, harvest W45
transforms, apply filtered W45 REPS with VOL bump. Scratch for the W46
cycle; lives in hidden_files/w46/."""
import ast, json, os, shutil, sys

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HF = os.path.join(GOAL, "hidden_files")
LANGS = ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "zh-tw"]
CORE_BUILD = os.path.join(HF, "weekly-report-w46-ko-build")

def w45_build(lang):
    return os.path.join(HF, f"weekly-report-w45-ko-{lang}-build")

def w46_build(lang):
    return os.path.join(HF, f"weekly-report-w46-ko-{lang}-build")

def setup(lang):
    src, dst = w45_build(lang), w46_build(lang)
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    for name in ["bslib4.py", "svglib.py", "run.py", "render.py"]:
        shutil.copy2(os.path.join(src, name), os.path.join(dst, name))
    shutil.copytree(os.path.join(src, "assets"), os.path.join(dst, "assets"))
    # transform reference
    tsrc = os.path.join(src, "transform.py")
    if not os.path.exists(tsrc):
        tsrc = os.path.join(src, "scratch", "transform.py")
    shutil.copy2(tsrc, os.path.join(dst, "transform-w45.py"))
    # fresh W46 core content
    for name in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        shutil.copy2(os.path.join(CORE_BUILD, name), os.path.join(dst, name))
    print(f"setup {lang}: {dst}")

def harvest(lang):
    path = os.path.join(w46_build(lang), "transform-w45.py")
    tree = ast.parse(open(path, encoding="utf-8").read())
    out = {"REPS": {}, "ROUND2": {}, "GEOM": [], "CONSTS": {}}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            try:
                val = ast.literal_eval(node.value)
            except Exception:
                continue
            if name in ("REPS", "ROUND2"):
                out[name] = {k: [list(p) for p in v] for k, v in val.items()}
            elif name == "GEOM":
                out["GEOM"] = [list(p) for p in val]
            elif isinstance(val, str) and len(val) > 40:
                out["CONSTS"][name] = val
    # also collect top-level string constants defined via concatenation
    src = open(path, encoding="utf-8").read()
    out["_src_len"] = len(src)
    return out

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "setup":
        for lang in LANGS:
            setup(lang)
    elif cmd == "harvest":
        os.makedirs("/tmp/w46-harvest", exist_ok=True)
        for lang in LANGS:
            h = harvest(lang)
            json.dump(h, open(f"/tmp/w46-harvest/{lang}.json", "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)
            print(lang, "REPS files:", {k: len(v) for k, v in h["REPS"].items()},
                  "ROUND2:", {k: len(v) for k, v in h["ROUND2"].items()},
                  "GEOM:", len(h["GEOM"]), "CONSTS:", list(h["CONSTS"]))
