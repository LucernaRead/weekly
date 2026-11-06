import pathlib, shutil
H = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
V = H/"hidden_files/w45/ko-ru-fix-verify/work"
DEL = H/"hidden_files/weekly-report-w45-ko-ru-build"
FILES = ["bslib4.py","content12.py","content34.py","content56.py","content7.py","content8.py"]
d = V/"negB2"
if d.exists(): shutil.rmtree(d)
d.mkdir(parents=True)
for f in FILES: shutil.copy(DEL/f, d/f)
shutil.copy(DEL/"transform.py", d/"transform.py")
p = d/"content56.py"; t = p.read_text(encoding="utf-8")
old = "Во время аудирования самолёты не летают"; new = "Во время аудирования самолёты не летаюX"
assert t.count(old)==2, t.count(old)
p.write_text(t.replace(old, new), encoding="utf-8")
print("negB2 corrupted content56 x2:", old, "->", new)
# sanity: dst must NOT remain as substring anywhere in the tree
for f in FILES:
    tt = (d/f).read_text(encoding="utf-8")
    assert old not in tt, f
print("sanity: short form substring absent from all 6 files")
