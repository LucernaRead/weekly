import pathlib, shutil
H = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
V = H/"hidden_files/w45/ko-ru-fix-verify/work"
DEL = H/"hidden_files/weekly-report-w45-ko-ru-build"
FILES = ["bslib4.py","content12.py","content34.py","content56.py","content7.py","content8.py"]
d = V/"negD"
if d.exists(): shutil.rmtree(d)
d.mkdir(parents=True)
for f in FILES: shutil.copy(DEL/f, d/f)
shutil.copy(DEL/"transform.py", d/"transform.py")
p = d/"content7.py"; t = p.read_text(encoding="utf-8")
old = "cyq = fy + 66 + (i % 4) * 102"; new = "cyq = fy + 66 + (i % 4) * 10X"
assert t.count(old)==1, t.count(old)
p.write_text(t.replace(old, new), encoding="utf-8")
print("negD corrupted content7 pitch dst x1:", old, "->", new)
for f in FILES:
    assert old not in (d/f).read_text(encoding="utf-8"), f
print("sanity: pitch dst substring absent from all 6 files")
