import pathlib, difflib
H = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
OLD = H/"hidden_files/w45/ko-ru-proof/work/transform-repro"
DEL = H/"hidden_files/weekly-report-w45-ko-ru-build"
for fn in ["content12.py","content7.py","content56.py","content8.py","content34.py"]:
    a = (OLD/fn).read_text(encoding="utf-8").replace("ko-core","OUT").replace("ko-ru","OUT").splitlines()
    b = (DEL/fn).read_text(encoding="utf-8").replace("ko-core","OUT").replace("ko-ru","OUT").splitlines()
    print(f"===== {fn} =====")
    for line in difflib.unified_diff(a,b,lineterm="",n=1):
        print(line[:260])
