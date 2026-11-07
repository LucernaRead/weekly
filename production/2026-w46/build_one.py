# -*- coding: utf-8 -*-
"""Build one W46 ES fan-out: copy core build, apply transform, run, gate.
Usage: python3 build_one.py <native> <transform-module> [--skip-render]
Gates: freeze diff vs W46 core SVGs, p8 compare vs core, occlusion audit.
Render (cards + print + web PDF) uses tools/venv python + build render.py.
"""
import os, sys, shutil, subprocess, json
GOALS = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HF = os.path.join(GOALS, "hidden_files")
TOOLS = os.path.join(GOALS, "tools")
CORE_BUILD = os.path.join(HF, "weekly-report-w46-es-build")
CORE_SVG = os.path.join(GOALS, "files/weekly-report-w46-es-core/svg")
VENV = os.path.join(TOOLS, "venv/bin/python")

def run(cmd, cwd=None, log=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    out = r.stdout + r.stderr
    if log:
        with open(log, "a", encoding="utf-8") as fh:
            fh.write("$ " + " ".join(cmd) + "\n" + out + f"[exit {r.returncode}]\n")
    print(out[-3000:])
    if r.returncode != 0:
        raise SystemExit(f"FAILED ({r.returncode}): {' '.join(cmd)}\n{out[-2000:]}")
    return out

def main():
    nat = sys.argv[1]
    modname = sys.argv[2]
    skip_render = "--skip-render" in sys.argv
    build = os.path.join(HF, f"weekly-report-w46-es-{nat}-build")
    ed = os.path.join(GOALS, f"files/weekly-report-w46-es-{nat}")
    log = os.path.join(HF, "w46", f"es-{nat}-build.log")
    if os.path.exists(build):
        shutil.rmtree(build)
    shutil.copytree(CORE_BUILD, build, ignore=shutil.ignore_patterns("__pycache__"))
    # transform
    sys.path.insert(0, os.path.join(HF, "w46"))
    import importlib
    mod = importlib.import_module(modname)
    pairs = getattr(mod, "PAIRS", []) + getattr(mod, "PAIRS2", [])
    from engine import apply_pairs, residue_scan
    with open(log, "w", encoding="utf-8") as fh:
        fh.write(f"=== build {nat} ===\n")
    # capture transform output
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        apply_pairs(build, pairs)
        residue_scan(build)
    with open(log, "a", encoding="utf-8") as fh:
        fh.write(buf.getvalue())
    print(buf.getvalue()[-1500:])
    # build
    run([sys.executable, "run.py"], cwd=build, log=log)
    if skip_render:
        return
    run([VENV, "render.py"], cwd=build, log=log)
    # gates
    diff_json = os.path.join(HF, "w46", f"es-{nat}-diff.json")
    run([sys.executable, os.path.join(TOOLS, "freeze.py"), "diff",
         "--core-svg", CORE_SVG, "--edition-svg", os.path.join(ed, "svg"),
         "--json", diff_json], log=log)
    p8json = os.path.join(HF, "w46", f"es-{nat}-p8-compare.json")
    run([sys.executable, os.path.join(TOOLS, "p8.py"), "compare",
         "--core-p8", os.path.join(CORE_SVG, "p8-ejercicios.svg"),
         "--edition-p8", os.path.join(ed, "svg/p8-ejercicios.svg"),
         "--total", "150", "--json", p8json], log=log)
    occ_json = os.path.join(HF, "w46", f"es-{nat}-occlusion.json")
    run([sys.executable, os.path.join(TOOLS, "occlusion_audit.py"),
         os.path.join(ed, "svg"), "--json", occ_json], log=log)
    print("GATES DONE", nat)

if __name__ == "__main__":
    main()
