#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p8.py — the P8 printed-note gate, generalized from the programme audit
(hidden_files/audit-p8-notes/audit.py, whose anchors this tool reproduces).

What it does: from a shipped P8 SVG, extract the SET of exercise numbers
that carry a PRINTED note, plus the printed key per number. Extraction is
wrap-aware and handles both answer typographies — paren style
`key (note)` and dash style `key — note`, including families that re-laid
answers in the other style than their core, and the page separators
(— SEITE n — / — PÁGINA n — / — СТРАНИЦА n — / — 제N면 — …).

Commands:
  extract --p8 <svg> --total N [--json out]
  compare --core-p8 <svg> --edition-p8 <svg> --total N [--json out]
  compare --core-dir <files dir> --edition-dir <files dir> --target <code> [--json out]

Verdicts (per hidden_files/audit-p8-notes/DECISION.md):
  CLEAN       sets equal
  EXTRA_ONLY  edition prints notes the core filters out — ADJUDICATED
              ACCEPTANCE (en-de/en-fr print all 149 vs the core's 62);
              reported, listed, exit 0
  SHORT       edition is missing notes the core prints — GATE FAILURE, exit 1
  UNCERTAIN   a missing candidate whose segment is not a bare key — exit 1
Key diffs (same noted set, different printed key) are listed; translation
items legitimately re-aim at the reader's language, so key diffs are
informational, not a failure by themselves.
Run with tools/venv/bin/python (any python3 works).
"""
import argparse, html, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tables as T

TEXT_RE = re.compile(r"<text([^>]*)>(.*?)</text>", re.S)
HEADER_RE = re.compile(r"^—\s*(.{0,24}?\d.{0,12}?)\s*—$")
CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")


def load_texts(path):
    """Logical lines, not raw <text> elements: the current svglib emits one
    <text> per same-font run, so a header like '— СТРАНИЦА 1 —' arrives as
    three elements ('— ', 'СТРАНИЦА', ' 1 —') and a per-element scan never
    sees it (fixed 2026-11-10: p8.py extract failed 'no-header' on the new
    run-split SVGs while the old single-element SVGs parsed fine).
    Runs on one baseline, in document order, join with no added space
    (spaces are explicit elements); a baseline change, an x regression
    (new column), or an end-anchored element starts a new line. Old
    single-element SVGs come through unchanged."""
    s = open(path, encoding="utf-8").read()
    raw = []
    for attrs, c in TEXT_RE.findall(s):
        m_x = re.search(r'x="([-\d.]+)"', attrs)
        m_y = re.search(r'y="([-\d.]+)"', attrs)
        m_a = re.search(r'text-anchor="([^"]+)"', attrs)
        raw.append((float(m_x.group(1)) if m_x else 0.0,
                    float(m_y.group(1)) if m_y else 0.0,
                    m_a.group(1) if m_a else "start",
                    html.unescape(re.sub(r"<[^>]+>", "", c))))
    lines, cur, cur_y, last_x = [], [], None, None
    for x, y, anchor, t in raw:
        if not t:
            continue
        new_line = (cur_y is None or abs(y - cur_y) > 2 or
                    (last_x is not None and x < last_x - 1) or
                    anchor == "end")
        if new_line:
            if cur:
                lines.append("".join(cur))
            cur, cur_y = [t], y
        else:
            cur.append(t)
        last_x = x
    if cur:
        lines.append("".join(cur))
    return lines


def is_header(t):
    t = t.strip()
    return bool(HEADER_RE.match(t)) and len(t) <= 34


FOOTER_RE = re.compile(r"LUCERNA|第\s*\d+\s*版／共\s*\d+\s*版")


def _tail(texts, start):
    """Elements from texts[start:], with trailing footer lines dropped by
    content, not by count. The two footer texts share one baseline
    (y=2624) and svglib writes both with text-anchor="start" (the
    end-anchored right text is pre-positioned), so load_texts merges them
    into ONE logical line; a blind [-2] then eats the last answer (no.
    150) and split_lines fails. Fixed 2026-11-10, W47 nl core: drop every
    trailing line that carries the masthead or the page-count footer
    instead."""
    els = texts[start:]
    while els and FOOTER_RE.search(els[-1]):
        els = els[:-1]
    return els


def answers_elements(texts):
    start = None
    for i, t in enumerate(texts):
        if is_header(t):
            start = i
            break
    if start is None:
        return None
    return _tail(texts, start)


def join2(a, b):
    if not a:
        return b
    if CJK.search(a[-1:]) or CJK.search(b[:1]):
        return a + b
    return a + " " + b


def last_paren_group(seg):
    best = None
    for op, cl in (("(", ")"), ("（", "）")):
        groups, depth, st = [], 0, None
        for j, ch in enumerate(seg):
            if ch == op:
                if depth == 0:
                    st = j
                depth += 1
            elif ch == cl and depth > 0:
                depth -= 1
                if depth == 0:
                    groups.append((st, j))
        for g in groups:
            if seg[g[1] + 1:].strip() == "":
                if best is None or g[0] > best[0]:
                    best = g
    return best


def detect_note(seg):
    """(has_note, key_text, method) for one printed answer segment."""
    seg = seg.strip()
    if seg.startswith("✓"):
        rest = seg[1:].strip()
        return (bool(rest), "✓", "check")
    # 2026-11-12 (D5 CJK, W47 fr-ko): D5 splits a sans line into per-script
    # runs, and a run that starts with a space loses it (svglib wrap() drops
    # a space token at a line break; CairoSVG drops a leading space of a run).
    # When the break falls right after an em-dash separator, the joined
    # segment reads "key —<CJK>…" with the space after the dash gone, so the
    # " — " dash test below misses and the segment falls through to paren
    # style — where last_paren_group() then finds a paren in the P8 caption
    # swallowed into the last entry (e.g. Hiroshige "(1797-1858)") and the
    # whole key is lost (fr-ko Q150). The source E values always write the
    # dash with spaces on both sides, so a dash directly before a CJK char
    # can only be this lost-space artifact: restore the space before testing.
    seg = re.sub(r" —(?=[\u3040-\u30ff\u3400-\u9fff\uac00-\ud7a3])", " — ", seg)
    g = last_paren_group(seg)
    dash = None
    if " — " in seg:
        k, tail = seg.split(" — ", 1)
        dash = (k.strip(), tail.strip())
    if g and dash:
        # Dash style wins only when the last dash sits after the paren group
        # opens AND the would-be dash key contains no '(' — a dash key with
        # '(' means the first dash actually lives INSIDE the trailing paren
        # note (Russian notes habitually read "(Present Simple — …)"), so
        # the segment is paren style. (Fixed 2026-10-22, EN×RU build: the
        # old rule truncated such keys at the note's first dash.)
        # Fixed 2026-10-27, KO×EN build: a dash separator BEFORE the paren
        # group opens is a dash-style segment whose NOTE trails with a
        # parenthetical ("key — note (page 3)") — the old rule fell through
        # to paren style and swallowed the note into the key. A dash before
        # the paren group therefore wins; a dash only inside the paren
        # group still loses (Russian case above).
        if seg.find(" — ") != -1 and seg.find(" — ") < g[0]:
            return (bool(dash[1]), dash[0], "dash")
        if seg.rfind(" — ") > g[0] and "(" not in dash[0] and "（" not in dash[0]:
            return (bool(dash[1]), dash[0], "dash")
        return (True, seg[:g[0]].strip(), "paren")
    if g:
        return (True, seg[:g[0]].strip(), "paren")
    if dash:
        return (bool(dash[1]), dash[0], "dash")
    return (False, seg, "none")


def split_joined(els, total):
    stream = ""
    for t in els:
        stream = join2(stream, "·" if is_header(t) else t)
    # 2026-11-10 (W47 fr core, SOP §1.1): the printed keys separator is now
    # a full-width space U+3000, not "·". Normalize it to the internal "·"
    # marker BEFORE the whitespace collapse below (\s+ would eat U+3000).
    stream = stream.replace("　", "·")
    stream = re.sub(r"\s+", " ", stream).strip().lstrip("·").strip()
    if not re.match(r"1\.\s", stream):
        return None
    entries, pos, cur = {}, re.match(r"1\.\s", stream).end(), 1
    while cur < total:
        # 2026-10-27 (EN x ZH-TW build): the separator space after "N." may be absent
        # when the next key starts with CJK -- svglib wrap() drops a space token at a
        # line start, and join2() adds no space before a CJK-initial line. The "·" before
        # the number keeps the separator unambiguous, so the trailing space is optional.
        mm = re.compile(r"·\s*" + str(cur + 1) + r"\.\s?").search(stream, pos)
        if not mm:
            # Fallback: a "　" eaten by svglib's rstrip() at a line break
            # leaves only a space (or nothing) before the number. Accept a
            # bare boundary, but require the number NOT to be preceded by a
            # digit or "." so decimals inside a key (e.g. "21.8") cannot
            # create a false entry.
            mm = re.compile(r"(?<![\d.])\s*" + str(cur + 1) + r"\.\s?").search(stream, pos)
        if not mm:
            return None
        entries[cur] = stream[pos:mm.start()].strip().rstrip("·").strip()
        pos, cur = mm.end(), cur + 1
    entries[total] = stream[pos:].strip()
    return entries


def split_lines(els, total):
    entries, cur, expect = {}, None, 1
    for ln in [t for t in els if not is_header(t)]:
        m = re.match(r"^\s*(\d{1,3})\.\s", ln)
        if m and int(m.group(1)) == expect:
            cur = expect
            entries[cur] = ln[m.end():]
            expect += 1
        elif cur is not None:
            entries[cur] = join2(entries[cur], ln)
        else:
            return None
    if expect != total + 1:
        return None
    return {n: s.strip() for n, s in entries.items()}


def extract(p8_path, total):
    """{n: {has_note, key, seg, method}} or (None, reason)."""
    texts = load_texts(p8_path)
    starts = [i for i, t in enumerate(texts) if is_header(t)]
    if not starts:
        return None, "no-header"
    # Try each header candidate in document order. A dialogue stem in the
    # test area can wrap to a line that looks exactly like a page
    # separator (starts AND ends with "—", short, contains a digit:
    # W47 zh-cn E149 "— 这条新闻说最高一天1.4亿件，可信吗？ —"), and the
    # old code took the first such line as the keys section start, so
    # split_lines failed before it ever saw a number. A candidate is only
    # the keys section if the numbered answers 1..total follow it in full.
    # Fixed 2026-11-10, W47 zh-cn core.
    last_err = "no-header"
    for s in starts:
        els = _tail(texts, s)
        body = [t for t in els if not is_header(t)]
        joined = any(re.search(r"\d+\.\s.*[·　]\s*\d+\.", t) for t in body)
        entries = split_joined(els, total) if joined else split_lines(els, total)
        how = "joined" if joined else "lines"
        if entries is None:
            last_err = how + "-split-fail"
            continue
        res = {}
        for n, seg in entries.items():
            has, key, method = detect_note(seg)
            res[n] = {"has_note": has, "key": key, "seg": seg, "method": method}
        res["_how"] = how
        return res, how
    return None, last_err


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def compare(core_p8, edition_p8, total):
    ref, refhow = extract(core_p8, total)
    res, how = extract(edition_p8, total)
    if ref is None or res is None:
        return {"status": "PARSE_FAIL", "ref_how": refhow, "how": how}, 2
    missing, extra, uncertain, keydiff = [], [], [], []
    for n in range(1, total + 1):
        cn, en_ = ref[n]["has_note"], res[n]["has_note"]
        if cn and not en_:
            if norm(res[n]["seg"]) == norm(ref[n]["key"]) or res[n]["method"] == "none":
                missing.append(n)
            else:
                uncertain.append(n)
        elif en_ and not cn:
            extra.append(n)
        elif cn and en_ and norm(res[n]["key"]) != norm(ref[n]["key"]):
            keydiff.append(n)
    refset = sorted(n for n in range(1, total + 1) if ref[n]["has_note"])
    edset = sorted(n for n in range(1, total + 1) if res[n]["has_note"])
    status = ("SHORT" if missing else "UNCERTAIN" if uncertain else
              "EXTRA_ONLY" if extra else "CLEAN")
    out = {"status": status, "total": total, "how": how, "ref_how": refhow,
           "core_count": len(refset), "edition_count": len(edset),
           "core_set": refset, "edition_set": edset,
           "missing": missing, "extra": extra, "uncertain": uncertain,
           "keydiff": keydiff}
    return out, (1 if status in ("SHORT", "UNCERTAIN") else 0)


def p8_path(directory, target):
    d = directory if os.path.isdir(os.path.join(directory, "svg")) else directory
    svgdir = os.path.join(directory, "svg") if os.path.isdir(os.path.join(directory, "svg")) else directory
    return os.path.join(svgdir, T.p8_file(target))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("extract")
    p.add_argument("--p8", required=True); p.add_argument("--total", type=int, required=True)
    p.add_argument("--json", dest="json_out")
    p = sub.add_parser("compare")
    p.add_argument("--core-p8"); p.add_argument("--edition-p8")
    p.add_argument("--core-dir"); p.add_argument("--edition-dir"); p.add_argument("--target")
    p.add_argument("--total", type=int)
    p.add_argument("--json", dest="json_out")
    args = ap.parse_args(argv)

    if args.cmd == "extract":
        res, how = extract(args.p8, args.total)
        if res is None:
            print(f"PARSE_FAIL ({how})", file=sys.stderr)
            return 2
        noted = sorted(n for n in range(1, args.total + 1) if res[n]["has_note"])
        keys = {n: res[n]["key"] for n in range(1, args.total + 1)}
        print(f"{args.p8}: noted set = {len(noted)} of {args.total} (parse: {how})")
        print(f"  set: {noted}")
        if args.json_out:
            json.dump({"p8": args.p8, "total": args.total, "how": how,
                       "noted_set": noted, "keys": keys},
                      open(args.json_out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        return 0

    total = args.total
    if args.core_dir and args.edition_dir and args.target:
        core_p8 = p8_path(args.core_dir, args.target)
        ed_p8 = p8_path(args.edition_dir, args.target)
        if total is None:
            # The count changes every week (fr: 145 in W43, 150 in W46); never fall back to a stored constant.
            ap.error("compare needs --total (this week's exercise count from the core's registry)")
    elif args.core_p8 and args.edition_p8 and total:
        core_p8, ed_p8 = args.core_p8, args.edition_p8
    else:
        ap.error("compare needs --core-p8/--edition-p8/--total or --core-dir/--edition-dir/--target")
    out, code = compare(core_p8, ed_p8, total)
    print(f"core    {core_p8}: {out.get('core_count')} noted")
    print(f"edition {ed_p8}: {out.get('edition_count')} noted")
    print(f"status: {out['status']}  missing={out.get('missing')} extra_count={len(out.get('extra', []))} "
          f"uncertain={out.get('uncertain')} keydiff={out.get('keydiff')}")
    if out.get("extra"):
        print(f"  extra (adjudicated acceptance, DECISION.md): {out['extra']}")
    if args.json_out:
        json.dump(out, open(args.json_out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return code


if __name__ == "__main__":
    sys.exit(main())
