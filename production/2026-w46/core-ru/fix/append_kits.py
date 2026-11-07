# -*- coding: utf-8 -*-
"""Append fix record section 10 to all 11 W46 RU WEEKLY-KIT.md files.
Sections 1-9 are left untouched; the record is appended only."""
import os

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
FILES = os.path.join(GOAL, "files")

# Per-edition data: (dir, slug, d2a before/after or None, d2b before/after or None,
#                    key note words 76/77, web pdf bytes, textmd bytes, freeze char totals)
EDITIONS = {
    "core": dict(
        d2a=None, d2b=None, note76="退货", note77="促销码",
        web=2719077, textmd=52661, chars="cyr=17049 han=1972 kana=0 hangul=0 (core self-diff control)",
        extra="Core edition; the same fix record covers the zh-cn edition, whose "
              ".text.md is byte-identical to the core file (52,661 bytes, cmp-verified).",
    ),
    "en": dict(
        d2a=("Fill in the gaps with the right verb form or the right case.",
             "Fill in the right verb form or the right case."),
        d2b=("Fill in the gaps with numbers and words from page 4.",
             "Fill in with numbers and words from page 4."),
        note76="return", note77="promo code",
        web=2310183, textmd=54203, chars="cyr=16860 han=0 kana=0 hangul=0",
        extra="",
    ),
    "de": dict(
        d2a=("Füllen Sie die Lücken mit der richtigen Verbform oder dem richtigen Kasus aus.",
             "Setzen Sie Verbform und Kasus richtig ein."),
        d2b=("Füllen Sie die Lücken mit Zahlen und Wörtern von Seite 4 aus.",
             "Zahlen und Wörter von Seite 4 einsetzen."),
        note76="Rücksendung", note77="Rabattcode",
        web=2316120, textmd=54855, chars="cyr=16860 han=0 kana=0 hangul=0",
        extra="",
    ),
    "fr": dict(
        d2a=("Complétez avec la bonne forme du verbe ou le bon cas.",
             "Complétez la bonne forme verbale ou le cas."),
        d2b=("Complétez avec les chiffres et les mots de la page 4.",
             "Complétez : chiffres et mots de la page 4."),
        note76="retour", note77="code promo",
        web=2312371, textmd=54870, chars="cyr=16860 han=0 kana=0 hangul=0",
        extra="",
    ),
    "es": dict(
        d2a=("Completa con la forma verbal correcta o el caso correcto.",
             "Completa la forma verbal o el caso correcto."),
        d2b=("Completa con números y palabras de la página 4.",
             "Completa: números y palabras (página 4)."),
        note76="devolución", note77="código promocional",
        web=2314532, textmd=55596, chars="cyr=16860 han=0 kana=0 hangul=0",
        extra="",
    ),
    "it": dict(
        d2a=("Completa con la forma verbale giusta o il caso giusto.",
             "Metti la forma verbale o il caso giusti."),
        d2b=("Completa con i numeri e le parole di pagina 4.",
             "Completa con numeri e parole di pagina 4."),
        note76="reso", note77="codice promozionale",
        web=2311010, textmd=55223, chars="cyr=16860 han=0 kana=0 hangul=0",
        extra="",
    ),
    "pt": dict(
        d2a=("Complete com a forma verbal correta ou o caso correto.",
             "Complete a forma verbal ou o caso correto."),
        d2b=("Complete com números e palavras da página 4.",
             "Complete: números e palavras da página 4."),
        note76="devolução", note77="código promocional",
        web=2316135, textmd=56445, chars="cyr=16860 han=0 kana=0 hangul=0",
        extra="",
    ),
    "nl": dict(
        d2a=("Vul in met de juiste werkwoordsvorm of de juiste naamval.",
             "Vul in: juiste werkwoordsvorm of naamval."),
        d2b=None, note76="retour", note77="kortingscode",
        web=2314264, textmd=55432, chars="cyr=16796 han=0 kana=0 hangul=0",
        extra="D2b: clean in this edition (bridge already fit one line) — untouched for D2b.",
    ),
    "ja": dict(
        d2a=None, d2b=None, note76="返品", note77="プロモコード",
        web=2736421, textmd=55116,
        chars="cyr=16804 han=2944 kana=1447 hangul=0; 2 core Han nodes survive verbatim "
              "(生活, 文化); strict-CJK exit 1 adjudicated (added chars are native Japanese script)",
        extra="D3 (ja only) — see below. D2: clean in this edition — untouched for D2.",
    ),
    "ko": dict(
        d2a=None, d2b=None, note76="반품", note77="프로모 코드",
        web=2490725, textmd=55835,
        chars="cyr=16868 han=8 (brackets 『』 only) kana=0 hangul=2791; 0 core Han nodes survive",
        extra="D2: clean in this edition — untouched for D2.",
    ),
    "zh-tw": dict(
        d2a=None, d2b=None, note76="退貨", note77="促銷碼",
        web=2760278, textmd=52585,
        chars="cyr=16868 han=2132 kana=0 hangul=0; 109 core Han nodes survive verbatim; "
              "zero Simplified-only chars among added Han (opencc check)",
        extra="D2: clean in this edition — untouched for D2.",
    ),
}

D1_CORE_BEFORE = 'content56.py match_set keys ["d", "a", "b", "c"], notes ["包裹 d", "退货 a", "促销码 b", "高峰 c"]'
D1_CORE_AFTER = 'content56.py match_set keys ["d", "b", "a", "c"], notes ["包裹 d", "退货 b", "促销码 a", "高峰 c"]'


def record(key, d):
    lines = []
    lines.append("")
    lines.append("## 10. Fix record — Round 1 proofread defects D1–D3 (2026-11-02/03, fix worker)")
    lines.append("")
    lines.append("Source of the defects: independent proofreader Round 1 verdict "
                 "(`hidden_files/w46/ru-proofread-gates/proofreader-verdict-round1.md`, ROUND 1 FAIL). "
                 "All fixes were made at the source and fully re-rendered; no rendered SVG/PDF was hand-edited. "
                 "Sections 1–9 above are untouched by this record.")
    lines.append("")
    lines.append("### D1 (BLOCKING, all 11 editions) — P5 matching block C, P8 key letters 76/77 transposed")
    lines.append("")
    lines.append("P5 block C prints words 75 посылка, 76 возврат, 77 промокод, 78 пик with options "
                 "a. код со скидкой (= promo code), b. товар возвращают в магазин (= return), "
                 "c. самое большое число заказов, d. товар, который прислали по почте. "
                 "Correct matches: 75→d, 76→b, 77→a, 78→c. The P5 block itself was correct and is unchanged.")
    lines.append("")
    lines.append(f"- Core build source `hidden_files/weekly-report-w46-ru-build/content56.py`: before {D1_CORE_BEFORE}; "
                 f"after {D1_CORE_AFTER}.")
    if key == "core":
        lines.append("- Fan-out map `hidden_files/w46/ru_maps.py` (all 10 specs): the same transposition in the P8-key "
                     "note pairs was fixed in every spec, e.g. en `('退货 a', 'return a')` → `('退货 b', 'return b')` "
                     "and `('促销码 b', 'promo code b')` → `('促销码 a', 'promo code a')`; this edition's own rendering "
                     "comes from the core source above.")
    else:
        lines.append(f"- Fan-out map `hidden_files/w46/ru_maps.py` (all 10 specs): the P8-key note pairs encoded the same "
                     f"transposition; before `('退货 a', '{d['note76']} a')` / `('促销码 b', '{d['note77']} b')`, "
                     f"after `('退货 b', '{d['note76']} b')` / `('促销码 a', '{d['note77']} a')`.")
    lines.append(f"- Rendered P8 key, before: `76. a — {d['note76']} a`, `77. b — {d['note77']} b`; "
                 f"after (verified in this edition's p8-test.svg): `76. b — {d['note76']} b`, `77. a — {d['note77']} a`.")
    lines.append(f"- Manuscript registry (`.text.md` §C + Answers, regenerated from source): before "
                 f"`76. возврат — код со скидкой (key a · {d['note76']} a)` / "
                 f"`77. промокод — товар возвращают в магазин (key b · {d['note77']} b)`; after "
                 f"`76. возврат — товар возвращают в магазин (key b · {d['note76']} b)` / "
                 f"`77. промокод — код со скидкой (key a · {d['note77']} a)`.")
    lines.append("- All five matching blocks were semantically re-verified option-by-option in the build sources "
                 "(25–28, 39–42, 57–60, 75–78, 141–144) and the rendered P8 keys were extracted per edition: "
                 "all correct; only 76/77 changed. See `hidden_files/w46/ru-fix/verify_matching.py` output and "
                 "`logs/p8-keys-printed.txt`.")
    lines.append("")
    if d["d2a"] or d["d2b"]:
        lines.append("### D2 (BLOCKING, edition-specific) — displaced wrapped instruction lines (stray fragments)")
        lines.append("")
        lines.append("Root cause: the 20.5 pt bridge wrapped to two lines; when only one line fit at the bottom of "
                     "column 1, line 2 flowed to the top of column 2 (x=527), ~900 px from its home line. "
                     "Fix: the instruction was shortened/re-worded in `hidden_files/w46/ru_maps.py` only, to fit one "
                     "434 px column line (measured with the build's own font metrics). Core source untouched for D2.")
        if d["d2a"]:
            lines.append(f"- D2a, P3 block C (bridge under head B · ГЛАГОЛЫ И ФОРМЫ): before `{d['d2a'][0]}` "
                         f"(orphan fragment at (527, 1696.5)); after `{d['d2a'][1]}` — single line at the home position.")
        if d["d2b"]:
            lines.append(f"- D2b, P4 block B (bridge under head B · КАЛЕНДАРЬ И ДАТЫ): before `{d['d2b'][0]}` "
                         f"(orphan fragment at (527, 1656.5)); after `{d['d2b'][1]}` — single line at the home position.")
        lines.append("")
    if key == "ja":
        lines.append("### D3 (MINOR, ja only) — kinsoku violation, P8 H-note")
        lines.append("")
        lines.append("Before: line 1 `作文（決まった答えはありません）；模範文（` (dangling opening bracket), "
                     "line 2 `87 語）は下にあります。`. After (re-worded in the ja spec of `hidden_files/w46/ru_maps.py`, "
                     "meaning preserved): line 1 `作文（決まった答えはありません）；模範文は`, "
                     "line 2 `下にあります（87 語）。` — the bracketed count opens and closes inside line 2. "
                     "Line count unchanged (2). Kinsoku scan of all 8 SVGs: 0 hits in ja (this was the only hit).")
        lines.append("")
    if d["extra"]:
        lines.append(d["extra"])
        lines.append("")
    lines.append("### Re-render + re-gate evidence (final artifacts, 2026-11-03)")
    lines.append("")
    lines.append(f"- Rebuild: `hidden_files/w46/ru-fix/rebuild.sh` (core + all 10 fan-outs, sequential); every run log: "
                 f"exit 0, TOTAL 150, A2 51 / B1 75 / B2 24, pages 10/18/18/18/18/18/12/38, model words 87, "
                 f"0 FLOW OVERFLOW / HEAD TOO WIDE. Logs: `hidden_files/w46/ru-fix/logs/ru-*-run.log`, `ru-*-transform.log`.")
    lines.append(f"- Web PDF via `tools/webpdf.py`: {d['web']} bytes (≤ 7 MB), 8 pages, print-vs-web text identical "
                 f"after whitespace normalisation, pdftotext bytes > 0. `.text.md` regenerated from the source "
                 f"manuscript (headers verbatim; only the D1/D2/D3 lines differ from the pre-fix file): {d['textmd']} bytes.")
    if key == "core":
        lines.append("- Occlusion audit: 0 flags, selftest OK. `check_core.py`: golden BAD 0, gloss fails 0, "
                     "orphan line-starts [], same-baseline collisions 0. `p8.py extract`: 150/150 noted. "
                     "Freeze self-diff control: 0 added/removed strings, 0 added CJK characters.")
    else:
        lines.append("- Occlusion audit: 0 flags, selftest OK. `check_core.py`: golden BAD 0, gloss fails 0, "
                     "orphan line-starts [], same-baseline collisions 0. `p8.py compare` vs core: CLEAN 150/150, "
                     "keydiff [137, 138, 139, 140] adjudicated (E-section translations by design).")
    lines.append(f"- Freeze diff vs core: zero added Cyrillic words (per-page word-level analysis, TOTAL ADD {{}}); "
                 f"char totals {d['chars']}.")
    lines.append("- Orphan-fragment scan (`ru-fix/orphan_scan.py`, all 8 pages of all 11 editions): TOTAL ORPHANS 0; "
                 "only the legitimate pre-existing P5 D-head bridge band-hits directly under their heads. "
                 "Kinsoku scan (`ru-fix/kinsoku_scan.py`, all editions): 0 hits.")
    lines.append("- P6 chart re-measured: bars at x=685 widths 600/343/286/200 for 42/24/20/14%, labels sum to 100%. "
                 "P7 phrases: per-page freeze ADD {} on p7 in every edition (Russian text verbatim).")
    lines.append("- Visual checks at full frame: P5 card (this edition), plus the D2/D3 pages where applicable "
                 "(P3/P4 in D2 editions, P8 in ja) — instructions complete at home positions, no stray fragments, "
                 "no overflow, footer clear.")
    lines.append("- Full fix report + gate JSONs/logs: `hidden_files/w46/ru-fix/FIX-REPORT.md` and "
                 "`hidden_files/w46/ru-fix/`. A Round 2 independent proofread follows; re-gating does not replace it.")
    lines.append("- Delivery: still finalized, NOT pushed, NOT posted — repo insertion remains the coordinator's "
                 "(serialized) step. No git push, no Discord post, no user message was made from this fix work.")
    return "\n".join(lines) + "\n"


def main():
    for key, d in EDITIONS.items():
        path = os.path.join(FILES, f"weekly-report-w46-ru-{key}", "WEEKLY-KIT.md")
        with open(path, encoding="utf-8") as f:
            before = f.read()
        assert before.count("\n") == 91 or before.endswith("\n"), (key, before.count("\n"))
        assert "## 10. Fix record" not in before, key
        with open(path, "a", encoding="utf-8") as f:
            f.write(record(key, d))
        print(f"appended {key}: {path}")


if __name__ == "__main__":
    main()
