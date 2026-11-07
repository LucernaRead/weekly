import pathlib, hashlib, re, difflib, sys
V = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ko-ru-fix-verify/work"
DEL = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ko-ru-build"
fresh = V/"fresh"
FILES = ["bslib4.py","content12.py","content34.py","content56.py","content7.py","content8.py"]
CORE_OUT = "weekly-report-w45-ko-core/svg"
DEL_OUT = "weekly-report-w45-ko-ru/svg"
def sha(b): return hashlib.sha256(b).hexdigest()
for fn in FILES:
    f = (fresh/fn).read_bytes(); d = (DEL/fn).read_bytes()
    print(f"== {fn}: fresh={sha(f)[:12]} delivered={sha(d)[:12]} raw-identical={f==d} len fresh={len(f)} delivered={len(d)}")
    # OUT-normalized: replace both OUT path substrings with placeholder
    fnorm = f.replace(CORE_OUT.encode(), b"OUT").replace(DEL_OUT.encode(), b"OUT")
    dnorm = d.replace(CORE_OUT.encode(), b"OUT").replace(DEL_OUT.encode(), b"OUT")
    print(f"   OUT-normalized identical={fnorm==dnorm}")
    # OUT-restored strict: fresh with delivered OUT line substituted
    frest = f.replace(CORE_OUT.encode(), DEL_OUT.encode())
    print(f"   OUT-restored strict identical={frest==d}")
    if fnorm!=dnorm:
        fl = fnorm.decode().splitlines(); dl = dnorm.decode().splitlines()
        for line in difflib.unified_diff(fl, dl, lineterm="", n=0):
            print("   DIFF:", line[:200])
    # OUT line itself
    for tag, data in (("fresh", f), ("delivered", d)):
        for line in data.decode().splitlines():
            if line.startswith("OUT ="):
                print(f"   OUT line [{tag}]: {line}")
