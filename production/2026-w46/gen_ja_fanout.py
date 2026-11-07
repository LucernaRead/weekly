#!/usr/bin/env python3
"""Generate a W46 JA fan-out transform.py from the EN transform.py.

Applies structural edits (edition paths, PDF name, badge line,
disclosure fragments, docstring, ld_en rename) then a MAP of
English new-strings -> target-language strings, longest-first.
Each MAP key must occur >= 1 time in the EN transform text.
Usage: gen_ja_fanout.py <lang> <map_module_path> <out_transform_path>
The map module defines: LANG_NAME, PDF_SUFFIX, BADGE (str),
DISC (list of 4 fragments), MAP (dict).
"""
import importlib.util
import os
import sys

EN = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/hidden_files/"
    "weekly-report-w46-ja-en-build/transform.py")

EN_DISC = [
    "Editor\\'s sample, not a real letter. No real letters or best ",
    "Page 8 compositions had arrived by the deadline; both will appear ",
    "in VOL.4. Send us your letter in Japanese — selected letters will ",
    "be printed in VOL.4!",
]
EN_BADGE = ("TEXT IN JAPANESE · EXPLANATIONS IN ENGLISH — "
            "THE EDITION FOR ENGLISH-SPEAKING READERS")


def main():
    lang, map_path, out_path = sys.argv[1:4]
    spec = importlib.util.spec_from_file_location("fanout_map", map_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    text = open(EN, encoding="utf-8").read()
    text = text.replace("weekly-report-w46-ja-en",
                        f"weekly-report-w46-ja-{lang}")
    text = text.replace('"Lucerna-VOL3-EN.pdf"',
                        f'"Lucerna-VOL3-{mod.PDF_SUFFIX}.pdf"')
    assert EN_BADGE in text, "badge line not found"
    # The badge line is a single-quoted Python string containing
    # double quotes; escape apostrophes in the new badge text.
    text = text.replace(EN_BADGE, mod.BADGE.replace("'", "\\'"))
    for old, new in zip(EN_DISC, mod.DISC):
        assert old in text, f"disclosure fragment missing: {old!r}"
        # Disclosure fragments sit inside single-quoted literals; escape
        # apostrophes the same way as MAP values.
        text = text.replace(old, new.replace("'", "\\'"))
    text = text.replace("-> JA x EN edition transform.",
                        f"-> JA x {lang.upper()} edition transform.")
    text = text.replace("headers/instructions -> English, per the W45 JA x EN shipped precedent.",
                        f"headers/instructions -> {mod.LANG_NAME}, per the W45 JA x {lang.upper()} shipped precedent.")
    text = text.replace("ld_en", f"ld_{lang}")
    skipped = []
    for old in sorted(mod.MAP, key=len, reverse=True):
        new = mod.MAP[old]
        # MAP values land in both single- and double-quoted literals in
        # the transform file; \' renders as ' in either quoting style,
        # while a raw ' would terminate a single-quoted literal.
        new = new.replace("'", "\\'")
        n = text.count(old)
        if n == 0:
            # Consumed already by a longer twin key with the same rendering
            # (e.g. the quoted PER_FILE form of a NOTES value). Verified
            # by the post-check below: no MAP key may survive.
            skipped.append(old)
            continue
        text = text.replace(old, new)
    for old in mod.MAP:
        if mod.MAP[old] != old:
            assert old not in text, f"MAP key survived replacement: {old!r}"
    if skipped:
        print(f"skipped (consumed by twin keys): {len(skipped)}")
    # Per-language structural PER_FILE pairs, inserted at the START of
    # the named file's list (so they run before the EN-derived entries).
    extra = getattr(mod, "EXTRA", {})
    for fname, pairs in extra.items():
        anchor = '    "%s": [\n' % fname
        assert anchor in text, f"EXTRA anchor missing for {fname}"
        ins = "".join("        (%r, %r),\n" % (o, n) for o, n in pairs)
        text = text.replace(anchor, anchor + ins, 1)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {out_path} ({len(text)} bytes)")


if __name__ == "__main__":
    main()
