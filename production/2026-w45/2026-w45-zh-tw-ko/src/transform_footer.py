
def main():
    gate10 = "--gate10" in sys.argv
    if gate10:
        dest = os.path.join(GOAL, "hidden_files/w45-zh-tw-ko-gate10")
        svg_dir = os.path.join(dest, "svg")
        fresh_copy(dest)
        os.makedirs(svg_dir, exist_ok=True)
        apply_all(dest, "files/w45-zh-tw-ko-gate10/svg", dest)
        # repoint OUT to the temp svg dir: replace the WHOLE expanduser
        # assignment (a tail-substring replace would double the prefix).
        for fname in ["content12.py", "content34.py", "content56.py",
                      "content7.py", "content8.py"]:
            path = os.path.join(dest, fname)
            text = open(path, encoding="utf-8").read()
            text, n = re.subn(r'OUT = os\.path\.expanduser\("[^"]*"\)',
                              'OUT = "' + svg_dir + '"', text)
            assert n == 1, f"{fname}: OUT repoint failed"
            open(path, "w", encoding="utf-8").write(text)
        venv = os.path.join(GOAL, "tools/venv/bin/python")
        r = subprocess.run([venv, os.path.join(dest, "run.py")],
                           cwd=dest, capture_output=True, text=True)
        print(r.stdout)
        print(r.stderr, file=sys.stderr)
        assert r.returncode == 0, "gate10 driver failed"
        warns = [ln for ln in (r.stdout + r.stderr).splitlines()
                 if "FLOW OVERFLOW" in ln or "HEAD TOO WIDE" in ln
                 or "TOO WIDE" in ln]
        names = ["p1-front.svg", "p2-life.svg", "p3-culture.svg", "p4-sport.svg",
                 "p5-youth.svg", "p6-deep.svg", "p7-lang.svg", "p8-test.svg"]
        ok = 0
        for n in names:
            a = sha(os.path.join(svg_dir, n))
            b = sha(os.path.join(DELIVERY, "svg", n))
            match = (a == b)
            ok += match
            print(f"gate10 {n}: {'IDENTICAL' if match else 'DIFF ' + a + ' vs ' + b}")
        print(f"GATE10: {ok}/8 byte-identical, warnings={len(warns)} {warns}")
        sys.exit(0 if ok == 8 and not warns else 1)
    else:
        fresh_copy(MYBUILD)
        apply_all(MYBUILD, MY_SVG_PATH, DELIVERY)
        print("transform applied to", MYBUILD)


if __name__ == "__main__":
    main()
