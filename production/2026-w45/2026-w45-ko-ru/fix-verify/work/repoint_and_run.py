import pathlib
V = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ko-ru-fix-verify/work"
fresh = V/"fresh"; svg = V/"fresh-svg"
svg.mkdir(exist_ok=True)
for fn in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
    p = fresh/fn; lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
    assert lines[5].startswith("OUT ="), (fn, lines[5])
    print(fn, "old OUT line:", lines[5].strip())
    lines[5] = f'OUT = "{svg}"\n'
    p.write_text("".join(lines), encoding="utf-8")
    print(fn, "new OUT line:", lines[5].strip())
