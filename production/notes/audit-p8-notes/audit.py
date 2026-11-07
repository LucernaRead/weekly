# -*- coding: utf-8 -*-
"""P8 printed-note audit v2: compare each fan-out edition's PRINTED P8 note set
(from shipped SVGs) against its frozen core's printed note set.
REPORT ONLY - reads artifacts, writes only this scratch dir."""
import re, os, json, html

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
REPO = os.path.expanduser("~/workspace/weekly-git/issues/2026-w43")

P8 = {
    "de": "p8-uebungen.svg", "en": "p8-exercices.svg", "es": "p8-ejercicios.svg",
    "fr": "p8-exercices.svg", "it": "p8-valutazione.svg", "ja": "p8-tesuto.svg",
    "ko": "p8-siheom.svg", "nl": "p8-toets.svg", "pt": "p8-avaliacao.svg",
    "ru": "p8-test.svg", "zh-cn": "p8-ceyan.svg", "zh-tw": "p8-test.svg",
}
CORE_DIR = {
    "de": "weekly-report-de-vol1", "en": "weekly-report-en-vol1",
    "es": "weekly-report-es-vol1", "fr": "weekly-report-vol4",
    "it": "weekly-report-it-vol1", "ja": "weekly-report-ja-vol1",
    "ko": "weekly-report-ko-vol1", "nl": "weekly-report-nl-vol1",
    "pt": "weekly-report-pt-vol1", "ru": "weekly-report-ru-vol1",
    "zh-cn": "weekly-report-zhcn-vol1", "zh-tw": "weekly-report-zhtw-vol1",
}
EDITION_DIR = {
    "de-zh-cn": "weekly-report-de-vol1", "en-zh-cn": "weekly-report-en-vol1",
    "es-zh-cn": "weekly-report-es-vol1", "fr-zh-cn": "weekly-report-vol4",
    "it-zh-cn": "weekly-report-it-vol1", "ja-zh-cn": "weekly-report-ja-vol1",
    "ko-zh-cn": "weekly-report-ko-vol1", "nl-zh-cn": "weekly-report-nl-vol1",
    "pt-zh-cn": "weekly-report-pt-vol1", "ru-zh-cn": "weekly-report-ru-vol1",
    "zh-cn-en": "weekly-report-zhcn-vol1", "zh-tw-en": "weekly-report-zhtw-vol1",
    "zh-cn-fr": "weekly-report-zhcn-fr",   # pin-verified ad785911 (not the hyphenated pre-fix dir)
    "zh-tw-fr": "weekly-report-zh-tw-fr",  # pin-verified 137bed3e (not weekly-report-zhtw-fr)
}
def edition_dir(suffix):
    return EDITION_DIR.get(suffix, "weekly-report-" + suffix)

TEXT_RE = re.compile(r"<text([^>]*)>(.*?)</text>", re.S)
HEADER_RE = re.compile(r"^—\s*(.{0,24}?\d.{0,12}?)\s*—$")
CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")

def load_texts(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for attrs, content in TEXT_RE.findall(s):
        content = re.sub(r"<[^>]+>", "", content)
        out.append(html.unescape(content))
    return out

def is_header(t):
    t = t.strip()
    return bool(HEADER_RE.match(t)) and len(t) <= 34

def answers_elements(texts):
    start = None
    for i, t in enumerate(texts):
        if is_header(t):
            start = i
            break
    if start is None:
        return None
    return texts[start:-2]

def join2(a, b):
    if not a:
        return b
    if CJK.search(a[-1:]) or CJK.search(b[:1]):
        return a + b
    return a + " " + b

def last_paren_group(seg):
    best = None
    for op, cl in (("(", ")"), ("（", "）")):
        groups = []
        depth = 0
        st = None
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
    """Unified: returns (has_note, key_text, method)."""
    seg = seg.strip()
    if seg.startswith("✓"):
        rest = seg[1:].strip()
        return (bool(rest), "✓", "check")
    g = last_paren_group(seg)
    dash = None
    if " — " in seg:
        k, tail = seg.split(" — ", 1)
        dash = (k.strip(), tail.strip())
    if g and dash:
        # both signals: the later-starting one is the note boundary
        if seg.rfind(" — ") > g[0]:
            return (bool(dash[1]), dash[0], "dash")
        return (True, seg[:g[0]].strip(), "paren")
    if g:
        return (True, seg[:g[0]].strip(), "paren")
    if dash:
        return (bool(dash[1]), dash[0], "dash")
    return (False, seg, "none")

def split_joined(els, total):
    # build stream, headers -> '·' sentinel
    stream = ""
    for t in els:
        if is_header(t):
            stream = join2(stream, "·")
        else:
            stream = join2(stream, t)
    stream = re.sub(r"\s+", " ", stream).strip().lstrip("·").strip()
    m = re.match(r"1\.\s", stream)
    if not m:
        return None
    entries = {}
    pos = m.end()
    cur = 1
    while cur < total:
        pat = re.compile(r"·\s*" + str(cur + 1) + r"\.\s")
        mm = pat.search(stream, pos)
        if not mm:
            return None
        entries[cur] = stream[pos:mm.start()].strip().rstrip("·").strip()
        pos = mm.end()
        cur += 1
    entries[total] = stream[pos:].strip()
    return entries

def split_lines(els, total):
    lines = [t for t in els if not is_header(t)]
    entries = {}
    cur = None
    expect = 1
    for ln in lines:
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

def parse_edition(files_dir, target, total):
    path = os.path.join(BASE, files_dir, "svg", P8[target])
    texts = load_texts(path)
    els = answers_elements(texts)
    if els is None:
        return None, "no-header"
    body = [t for t in els if not is_header(t)]
    joined = any(re.search(r"\d+\.\s.*·\s*\d+\.", t) for t in body)
    if joined:
        entries = split_joined(els, total)
        how = "joined"
    else:
        entries = split_lines(els, total)
        how = "lines"
    if entries is None:
        return None, how + "-split-fail"
    res = {}
    for n, seg in entries.items():
        has, key, method = detect_note(seg)
        res[n] = {"has_note": has, "key": key, "seg": seg, "method": method}
    return res, how

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

def repo_meta(slug):
    md = open(os.path.join(REPO, slug, slug + ".md"), encoding="utf-8").read()
    total = int(re.search(r"^exercises:\s*(\d+)", md, re.M).group(1))
    target = re.search(r"^target:\s*(\S+)", md, re.M).group(1)
    native = re.search(r"^native:\s*(\S+)", md, re.M).group(1)
    return total, target, native

def main():
    slugs = sorted(s for s in os.listdir(REPO)
                   if os.path.isdir(os.path.join(REPO, s)))
    core_ref = {}
    for target, cdir in CORE_DIR.items():
        total = {"en": 149, "fr": 145}.get(target, 150)
        res, how = parse_edition(cdir, target, total)
        core_ref[target] = (res, how)
    report = {}
    for slug in slugs:
        suffix = slug.replace("2026-w43-", "")
        total, target, native = repo_meta(slug)
        fdir = edition_dir(suffix)
        res, how = parse_edition(fdir, target, total)
        ref, refhow = core_ref[target]
        row = {"dir": fdir, "target": target, "native": native, "total": total,
               "how": how, "ref_how": refhow}
        if res is None or ref is None:
            row["status"] = "PARSE_FAIL ed=%s ref=%s" % (how, refhow)
        else:
            missing, extra, uncertain, keydiff = [], [], [], []
            for n in range(1, total + 1):
                cn, en_ = ref[n]["has_note"], res[n]["has_note"]
                if cn and not en_:
                    # definite only if edition segment is bare key
                    if norm(res[n]["seg"]) == norm(ref[n]["key"]) or res[n]["method"] == "none":
                        missing.append(n)
                    else:
                        uncertain.append(n)
                elif en_ and not cn:
                    extra.append(n)
                elif cn and en_:
                    if norm(res[n]["key"]) != norm(ref[n]["key"]):
                        keydiff.append(n)
            refset = {n for n, v in ref.items() if v["has_note"]}
            edset = {n for n, v in res.items() if v["has_note"]}
            row.update(core_count=len(refset), ed_count=len(edset),
                       missing=missing, extra=extra, uncertain=uncertain,
                       keydiff_note_items=keydiff)
            row["status"] = ("SHORT" if missing else
                             "UNCERTAIN" if uncertain else
                             "EXTRA_ONLY" if extra else "CLEAN")
            row["_detail"] = {str(n): {"core": ref[n], "ed": res[n]}
                              for n in sorted(set(missing + uncertain + extra))}
        report[slug] = row
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    for slug in slugs:
        r = report[slug]
        print(slug, "|", r.get("status"), "| core:", r.get("core_count"),
              "| ed:", r.get("ed_count"), "| missing:", r.get("missing"),
              "| extra:", r.get("extra"), "| uncert:", r.get("uncertain"),
              "| keydiff:", r.get("keydiff_note_items"),
              "| how:", r.get("how"), "/", r.get("ref_how"))

if __name__ == "__main__":
    main()
