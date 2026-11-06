# -*- coding: utf-8 -*-
"""Semantic re-verification of all five matching blocks (p8.py cannot catch
key transpositions: it compares note SETS, not key correctness).
Parses match_set() calls from the build sources in registry order, prints
left -> key -> right-text + note for every item, and asserts:
 - keys are a permutation of a/b/c/d per block;
 - each note's trailing letter equals the key;
 - the same left word maps to the SAME right text in every block it appears in
   (посылка, пик appear twice with different option orders);
 - P5 block (75-78): 75->d, 76->b, 77->a, 78->c (the D1 fix).
Usage: verify_matching.py <build-dir>..."""
import ast, sys, os

def eval_list(node):
    return [e.value for e in node.elts]

def main():
    all_ok = True
    for bdir in sys.argv[1:]:
        print(f"== {bdir}")
        n = 0
        blocks = []
        for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
            tree = ast.parse(open(os.path.join(bdir, fname), encoding="utf-8").read())
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and getattr(node.func, "attr", None) == "ex":
                    n += 1
                elif isinstance(node, ast.Call) and getattr(node.func, "attr", None) == "match_set":
                    lefts = eval_list(node.args[2]); rights = eval_list(node.args[3])
                    keys = eval_list(node.args[4]); notes = eval_list(node.args[5])
                    start = n + 1
                    n += len(lefts)
                    blocks.append((start, lefts, rights, keys, notes))
        word_to_right = {}
        for start, lefts, rights, keys, notes in blocks:
            assert sorted(keys) == ["a", "b", "c", "d"], (bdir, start, keys)
            for i, (lf, ky, nt) in enumerate(zip(lefts, keys, notes)):
                rt = rights[ord(ky) - 97]
                print(f"  {start+i}. {lf} -> {ky}. {rt}  (note: {nt})")
                assert nt.rsplit(" ", 1)[-1] == ky, (bdir, start + i, nt, ky)
                if lf in word_to_right and word_to_right[lf] != rt:
                    print(f"  !! INCONSISTENT right text for {lf}: {word_to_right[lf]!r} vs {rt!r}")
                    all_ok = False
                word_to_right[lf] = rt
        p5 = [b for b in blocks if b[0] == 75]
        assert len(p5) == 1, [b[0] for b in blocks]
        assert p5[0][3] == ["d", "b", "a", "c"], (bdir, p5[0][3])
        print(f"  P5 block keys OK: {p5[0][3]}")
    print("MATCHING VERIFICATION:", "PASS" if all_ok else "FAIL")
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
