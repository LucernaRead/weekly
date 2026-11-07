# -*- coding: utf-8 -*-
"""Append Round-1 fix records + re-gate results to all 11 W46 IT KITs.
Only appends/updates numbers; never rewrites existing prose."""
import os, re

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
FILES = os.path.join(GOAL, "files")

COMMON = [
    "D1 (all 11, CORE): `content12.py` P1 IN BREVE FESTIVAL cross-reference `(Pagina 5)` → `(Pagina 2)` — the Festival closing coverage is on P2 (`E LA SETTIMANA SCORSA?`), not P5. MANOVRA → Pagina 6 and RICERCA → Pagina 4 in the same box were already correct.",
    "D2 (all 11, CORE): `content34.py` ex. 56/57 contradicted the issue's own facts (both matches kick off 20:45 — P1, P4 article, fixture table). Stems gained NON (`Le partite di domenica sera NON cominciano ___ …`, `Le partite di giovedì NON cominciano ___ …`); keys unchanged (`più tardi` / `più presto`); P8 notes rewritten in each reader language to state both matches at 20:45 + the negation. No other exercise or key changed.",
    "D3 (all 11, CORE): `content12.py` P2 agreement fixed: `si sono chiusi il Forum Cultura … e si sono aperti la finale del Panettone e la Festa del Torrone` → `si è chiuso il Forum Cultura … e si sono aperte la finale del Panettone e la Festa del Torrone`.",
    "Q1 (all 11, CORE, query resolved as ERROR): `content7.py` B2 column `la finale è a Perugia` has no referent anywhere in the issue — the only `finale` mentions are the Panettone finale (no location given) and `quarti di finale` (Mar 2027, no location); Perugia hosts Eurochocolate (an opening, not a finale). Replaced with the verified fact `la Festa del Torrone è a Cremona` (P1 + P3). No referent was invented.",
]
SPECIFIC = {
    "core": [
        "D5 (CORE): `content8.py` P8 §G notes 146–148 normalized to `=` like item 145: `mandorle 杏仁` → `mandorle = 杏仁`, `quanto costa? 多少钱` → `quanto costa? = 多少钱`, `pagare con carta 刷卡` → `pagare con carta = 刷卡`.",
    ],
    "de": [
        "F1: `content12.py` P8 items 16–19 notes, full-width colon U+FF1A → half-width colon (`dividere：…` → `dividere: …`, same for assaggiare/aprire/mangiare), matching items 20/60/61.",
    ],
    "en": [
        "P1 strapline: `THE ITALIAN ITALIANS ARE READING` → `THE ITALIAN THAT ITALIANS ARE READING` (core: `the Italian that Italians are reading`). Pixel-checked: centred, no collision with VOL/date.",
        "P8 item 132 note: `two cities, two sweets` → `two cities, two festivals` (`feste` = festivals, title `Due città, due feste`).",
        "P8 items 44/134 notes: `Subject + essere + place` → `Subject + essere + place + date` (as de/fr).",
        "F1: `content12.py` items 16–19 full-width colon → half-width colon.",
    ],
    "es": [
        "P8 item 132 note: `dos ciudades, dos dulces` → `dos ciudades, dos fiestas`.",
        "P8 item 117 note: `La Festa del Torrone abre en Cremona` → `La Festa del Torrone continúa en Cremona`, aligning with the stem's `continua`.",
        "P8 item 56 note rewritten under D2 with standard `más tarde que` (the old `después que` was nonstandard).",
        "F1: `content12.py` items 16–19 full-width colon → half-width colon.",
    ],
    "fr": [
        "P8 item 132 note: `deux villes, deux douceurs` → `deux villes, deux fêtes`.",
        "F1: `content12.py` items 16–19 full-width colon → half-width colon. (Items 74 `marrons grillés` and the disclosure's `reçus` agreement were judged acceptable by the proofreader and left unchanged.)",
    ],
    "ja": [],
    "ko": [
        "P8 name rendering: `Scrittorincittà` printed with Japanese katakana (`스크리토리ンチ타`) in 6 P8 notes (items 65, 66, 80, 82, 120, 129) → proper Korean `스크리토린치타` (`content56.py` ×4, `content8.py` ×2).",
        "Ideographic full stop U+3002 → `.` in two instruction lines: P3 bridge (`content34.py`) and P5 futuro-semplice bridge (`content56.py`).",
        "D5: `content8.py` item 146 `mandorle 아몬드` → `mandorle = 아몬드`.",
        "F1: `content12.py` items 16–19 full-width colon → half-width colon; plus the P6 box-header line `빈칸 채우기：manovra …` → half-width colon (`content56.py`).",
    ],
    "nl": [
        "P8 item 20: pronoun gender fixed — `dura (hij)` → `dura (zij)` for feminine `l'estate` (de `sie`, es `ella`, fr `elle`).",
        "P8 item 146: `mandorle: amandelen` → `mandorle = amandelen`.",
        "F1: `content12.py` items 16–19 full-width colon → half-width colon.",
        "REGRESSION CAUGHT + FIXED IN-ROUND: the first (longer) Dutch D2 notes pushed P8 keys 1 line past the bottom (`FLOW OVERFLOW [P8-keys]`, 9 px). Notes shortened below their original lengths (`Beide om 20.45 uur: zondag niet later dan donderdag: più tardi` / `… donderdag niet eerder dan zondag: più presto`); re-render clean, 0 overflows.",
    ],
    "pt": [
        "P8 item 132 note: `duas cidades e dois doces` → `duas cidades e duas festas`.",
        "P7 disclosure register aligned to the E TU boxes' tu forms: `escrevam à redação` → `escreve à redação` (both occurrences in `content7.py`). European Portuguese spelling untouched throughout.",
        "F1: `content12.py` items 16–19 full-width colon → half-width colon.",
    ],
    "ru": [
        "P7 disclosure qualifier added: `Писем и лучших сочинений нет; …` → `Пока писем и лучших сочинений нет; …` (temporal `Пока` = as yet/so far — the press-time bound every other edition states). NOTE: the fuller `К моменту сдачи номера …` wording was tried first and REVERTED — it added a 4th line that pushed the letters box across the FRASI gold rule (LINEX, verified on pixels); the compact `Пока` form fits 3 lines with the box bottom 14 px clear of the rule (1672 vs 1686).",
        "P8 item 38: `mandorle = миндаль (мн. ч.)` → `mandorle = миндаль` — миндаль is a mass noun; the plural marker was inaccurate. Other `(мн. ч.)` markers (true plurals) untouched.",
        "F1: `content12.py` items 16–19 full-width colon → half-width colon.",
    ],
    "zh-tw": [
        "Stranded line-start punctuation reflowed (0 hits after fix; scan of all SVG text nodes): P1 cifre item 1 `11 — 11月、聖馬丁節那天、週三（聖馬丁節，11 月 11 日週三）` → `11 — 11月11日週三，聖馬丁節` (one line); P5 plan item 3 `（週五：巧克力節開幕）` → `（週五巧克力節開幕）` (wrap now breaks before 巧, never before punctuation).",
        "Terminology unified to 將來時 (majority form, 7 source sites; no core KIT mandate for this term): `content7.py` 未來時 → 將來時 ×3 (P7 bridge + P8 items 102/104 notes). Rendered total: 將來時 ×10 (P5+P7 bridges + P8 76–79, 101–104), 未來時 ×0.",
        "D5: `content8.py` items 146/147/148 → `=` (`mandorle = 杏仁`, `quanto costa? = 多少錢`, `pagare con carta = 刷卡` — item 148 included under `normalize to = everywhere`, same defect class).",
    ],
}
PAGES = {
    "core": "P1, P2, P4, P7, P8", "de": "P1, P2, P4, P7, P8", "en": "P1, P2, P4, P7, P8",
    "es": "P1, P2, P4, P7, P8", "fr": "P1, P2, P4, P7, P8", "ja": "P1, P2, P4, P7, P8",
    "ko": "P1–P8 (all 8: P3/P5 bridges + P6 box header also changed)",
    "nl": "P1, P2, P4, P7, P8", "pt": "P1, P2, P4, P7, P8", "ru": "P1, P2, P4, P7, P8",
    "zh-tw": "P1, P2, P4, P5, P7, P8",
}
FREEZE_CJK = {"de": 0, "en": 0, "es": 0, "fr": 0, "ja": 3036, "ko": 3235, "nl": 0, "pt": 0, "ru": 0, "zh-tw": 968}
VALID = {"core": "forward-miss 1 / reverse-miss 0 (registry-only writing note, same class as zh-tw)",
         "de": "forward-miss 0 / reverse-miss 0", "en": "forward-miss 0 / reverse-miss 0",
         "es": "forward-miss 0 / reverse-miss 0",
         "fr": "forward-miss 0 / reverse-miss 8 (footer page lines, render-added furniture; as builder's)",
         "ja": "forward-miss 1 / reverse-miss 8 (writing note + footer page lines; as builder's)",
         "ko": "forward-miss 0 / reverse-miss 0",
         "nl": "forward-miss 0 / reverse-miss 8 (footer page lines; as builder's)",
         "pt": "forward-miss 0 / reverse-miss 14 (validator normalisation gaps, adjudicated; as builder's)",
         "ru": "forward-miss 0 / reverse-miss 0",
         "zh-tw": "forward-miss 1 / reverse-miss 0 (registry-only writing note; as builder's)"}
TEXTMD = {"core": 53103, "de": 55867, "en": 55674, "es": 56252, "fr": 56642, "ja": 58207,
          "ko": 57512, "nl": 55279, "pt": 55978, "ru": 67455, "zh-tw": 53103}
PRINTB = {"core": 20987102, "de": 7094506, "en": 7092138, "es": 7089743, "fr": 7090758,
          "ja": 20219136, "ko": 11601407, "nl": 7128492, "pt": 7093017, "ru": 7051930, "zh-tw": 19363047}
WEBB = {"core": (1204277, 44258), "de": (673009, 45670), "en": (667594, 45362), "es": (665241, 46013),
        "fr": (665372, 46221), "ja": (1258072, 47589), "ko": (966392, 47396), "nl": (662676, 45619),
        "pt": (669259, 45646), "ru": (701784, 53115), "zh-tw": (1463313, 44394)}
WEBNAME = {"core": "La-Lucerna-VOL3-web.pdf", "de": "La-Lucerna-VOL3-DE-web.pdf", "en": "La-Lucerna-VOL3-EN-web.pdf",
           "es": "La-Lucerna-VOL3-ES-web.pdf", "fr": "La-Lucerna-VOL3-FR-web.pdf", "ja": "La-Lucerna-VOL3-JA-web.pdf",
           "ko": "La-Lucerna-VOL3-KO-web.pdf", "nl": "La-Lucerna-VOL3-NL-web.pdf", "pt": "La-Lucerna-VOL3-PT-web.pdf",
           "ru": "La-Lucerna-VOL3-RU-web.pdf", "zh-tw": "La-Lucerna-VOL3-ZHTW-web.pdf"}
GATELOG = {"core": "zh-cn", "de": "de", "en": "en", "es": "es", "fr": "fr", "ja": "ja",
           "ko": "ko", "nl": "nl", "pt": "pt", "ru": "ru", "zh-tw": "zh-tw"}
SLUG = {"core": "2026-w46-it-zh-cn", "de": "2026-w46-it-de", "en": "2026-w46-it-en", "es": "2026-w46-it-es",
        "fr": "2026-w46-it-fr", "ja": "2026-w46-it-ja", "ko": "2026-w46-it-ko", "nl": "2026-w46-it-nl",
        "pt": "2026-w46-it-pt", "ru": "2026-w46-it-ru", "zh-tw": "2026-w46-it-zh-tw"}

def fmt(n):
    return f"{n:,}"

for code in ["core", "de", "en", "es", "fr", "ja", "ko", "nl", "pt", "ru", "zh-tw"]:
    eddir = "weekly-report-w46-it-core" if code == "core" else f"weekly-report-w46-it-{code}"
    path = os.path.join(FILES, eddir, "WEEKLY-KIT.md")
    txt = open(path, encoding="utf-8").read()
    orig = txt
    # 1. fix-record block before ## 8
    items = COMMON + SPECIFIC[code]
    block = ("\n- Fix record — Round 1 independent-proofread fixes (2026-11-03, fix worker; all fixes at source in "
             "`content*.py`, never in rendered SVGs/PDFs; full re-render + full re-gate after the round; "
             "asserted-replacement log `hidden_files/w46/it-fix/apply_fixes.log`, 137/137 applied):\n" +
             "".join(f"  {i+1}. {it}\n" for i, it in enumerate(items)) +
             f"  Changed pages vs pre-fix snapshot (SVG sha256): {PAGES[code]}; all other pages byte-identical. "
             "ABSTRACT.txt unchanged (still valid: single line, no ASCII double quotes).\n")
    assert "\n## 8. Gates" in txt
    txt = txt.replace("\n## 8. Gates", block + "\n## 8. Gates", 1)
    # 2. re-gate bullet before the next ## heading after §8
    gl = GATELOG[code]
    keydiff = "[]" if code == "core" else "[137, 138, 139]"
    p8line = (f"status CLEAN, 150 noted = 150 noted, missing=[] extra_count=0 uncertain=[], keydiff={keydiff}"
              if code != "core" else "status CLEAN (core vs itself), 150 noted, keydiff=[]")
    gate = (f"\n- Round-1 fix re-gate (2026-11-03, fix worker, logs `hidden_files/w46/it-fix/`): "
            f"`freeze.py diff` vs core (freeze-{gl}.log) — TOTAL added CJK characters "
            f"{FREEZE_CJK.get(code, 0) if code != 'core' else 0} (core self-diff 0); 0 long Italian body strings in any added/removed set (no frozen-layer drift); "
            f"`p8.py compare` (p8-{gl}.log) — {p8line}; "
            f"`occlusion_audit.py` (occlusion-{gl}.log, selftest OK) — 0 flags on all 8 shipped SVGs; "
            f"build logs 0 FLOW OVERFLOW / 0 HEAD TOO WIDE, TOTAL 150 (10/18/18/18/18/18/12/38; A2 47 / B1 70 / B2 33); "
            f"`.text.md` validation ({VALID[code]}); "
            f"web PDF {fmt(WEBB[code][0])} bytes (< 7 MB), `pdftotext` {fmt(WEBB[code][1])} bytes, byte-identical to the print PDF's text, 8 pages; "
            "changed pages proofread on pixels (core P1/P2/P4/P7, EN P1 strapline, RU+PT P7 letters boxes, ZH-TW P1 cifre + P5 plan, NL P8 foot, KO P8) + full changed-text verification against the SVGs (`hidden_files/w46/it-fix/verify_svgtext.py`, 0 failures).\n")
    # insert before the heading that follows ## 8
    idx8 = txt.index("## 8. Gates")
    m = re.search(r"\n## \d+\.", txt[idx8 + 10:])
    assert m, code
    ins = idx8 + 10 + m.start()
    txt = txt[:ins] + gate + txt[ins:]
    # 3. Web PDF line numbers in §8
    wb, tb = WEBB[code]
    txt2, n = re.subn(r"(- Web PDF: `tools/webpdf.py <svg-dir> \S+` — )[\d,]+ bytes \(< 7 MB\); `pdftotext` [\d,]+ bytes",
                      rf"\g<1>{fmt(wb)} bytes (< 7 MB); `pdftotext` {fmt(tb)} bytes", txt, count=1)
    assert n == 1, (code, "webpdf line")
    txt = txt2
    # 4. §10/§9 shipped-file sizes
    txt2, n1 = re.subn(r"(- `La-Lucerna[^`]*\.pdf` — print PDF \(vector, text layer\)), [\d,]+ bytes",
                       rf"\g<1>, {fmt(PRINTB[code])} bytes", txt)
    txt2, n2 = re.subn(r"(- `La-Lucerna[^`]*-web\.pdf` — web PDF \(text layer, < 7 MB\)), [\d,]+ bytes",
                       rf"\g<1>, {fmt(wb)} bytes", txt2)
    txt2, n3 = re.subn(r"(- `\d+-w46-it-[^`]*\.text\.md` — manuscript text export \(from the source manuscript, never from PDF\)), [\d,]+ bytes",
                       rf"\g<1>, {fmt(TEXTMD[code])} bytes", txt2)
    print(code, "print-line:", n1, "web-line:", n2, "textmd-line:", n3)
    txt = txt2
    if code == "core":
        old9 = "manuscript text export (from the shipped SVGs' text, never from PDF)"
        assert old9 in txt
        txt = txt.replace(old9, "manuscript text export (from the build sources via the AST exporter `hidden_files/w46/it-fix/export_core_textmd.py`, never from PDF/SVG)")
    assert txt != orig
    open(path, "w", encoding="utf-8").write(txt)
    print("patched", code)
print("DONE")
