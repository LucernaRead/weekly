import pathlib, shutil
H = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
V = H/"hidden_files/w45/ko-ru-fix-verify/work"
DEL = H/"hidden_files/weekly-report-w45-ko-ru-build"
FILES = ["bslib4.py","content12.py","content34.py","content56.py","content7.py","content8.py"]
def make(name, fn, old, new):
    d = V/name
    if d.exists(): shutil.rmtree(d)
    d.mkdir(parents=True)
    for f in FILES: shutil.copy(DEL/f, d/f)
    shutil.copy(DEL/"transform.py", d/"transform.py")
    p = d/fn; t = p.read_text(encoding="utf-8")
    assert old in t, (name, old[:60])
    p.write_text(t.replace(old, new), encoding="utf-8")
    print(name, "corrupted", fn, "|", old[:60], "->", new[:60], "| occurrences replaced:", t.count(old))
# Neg-A: P1 short gloss (fix3-1 dst) corrupted in content12 -> phase1 superseded check must fail
make("negA", "content12.py",
     "입동 = ипдон · 절정 = пик · 김장 = кимчжан · 상륙하다 = выйти на берег · 온대저기압 = циклон.",
     "입동 = ипдон · 절정 = пик · 김장 = кимчжан · 상륙하다 = выйти на берег · 온대저기압 = циклонXXX.")
# Neg-B: phase-2-only dst corrupted in content56 (appears x2) -> phase1 skips, phase2 must fail
make("negB", "content56.py",
     "Во время аудирования самолёты не летают",
     "Во время аудирования самолёты не летаютXXX")
# Neg-C: chained E-item final form corrupted in content8 -> phase1 final-form check must fail
make("negC", "content8.py",
     '"Особые меры действуют только 19 ноября. → ___", instr="Переведите"',
     '"Особые меры действуют только 19 ноября. → ___", instr="ПереведитеXXX"')
