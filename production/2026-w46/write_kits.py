# -*- coding: utf-8 -*-
"""Write WEEKLY-KIT.md for the 11 W46 DE fan-outs (+ the zh-cn duplicate)
from a per-edition data table. Gate results are the measured values from
hidden_files/w46/ gate logs (see de-gates.log for the consolidated record)."""
import os

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")

ED = {
"en": dict(
    native="English", badge='TEXT IN GERMAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS (20 pt, OLIVE)',
    footer="Die Lucerna · GERMAN WEEKLY VOL.3 · German text · English explanations",
    pageline="Page N of 8", gloss="Note — ", sep="— Page {pg} —", bracket="({note})",
    keys="13 pt / lh 1.26", svglib="core svglib.py unchanged",
    defects="First occlusion audit: 8 flags (7 BOXTITLE + 1 COVER — P4 invite 3 lines). Fixed by shortening box titles/glosses and the P4 invite to 2 lines; P6 gloss trimmed to 4 lines at iw=398. Second audit: 0 flags.",
    extra="Transform: 379 replacements, CJK leaks NONE. P8 keydiff [137, 138, 139, 150] is legitimate translation re-aiming (E-section).",
    occ="0 flags (2nd audit: de-en-occlusion2.txt)", p8="CLEAN 150=150, keydiff=[137, 138, 139, 150]",
    freeze="exit 0, TOTAL added CJK characters: 0", eq="48,481 bytes",
    web="1,064,521", printp="4,042,810"),
"fr": dict(
    native="French", badge='TEXTE EN ALLEMAND · EXPLICATIONS EN FRANÇAIS — L\'ÉDITION POUR LES LECTEURS FRANCOPHONES (20 pt, BRICK)',
    footer="Die Lucerna · HEBDOMADAIRE ALLEMAND VOL.3 · TEXTE EN ALLEMAND · EXPLICATIONS EN FRANÇAIS",
    pageline="Page N sur 8", gloss="Note — ", sep="— Page {pg} —", bracket="({note})",
    keys="13 pt / lh 1.26", svglib="core svglib.py unchanged",
    defects="P6 gloss shortened to 4 lines; F-head shortened to “Paires” (HEAD TOO WIDE); first occlusion audit 5 flags (4 BOXTITLE + 1 EDGE, all title widths) fixed by shortening 4 box titles. Second audit: 0 flags.",
    extra="Transform: 379 replacements, CJK leaks NONE. P8 keydiff [137, 138, 139, 150] is legitimate translation re-aiming (E-section).",
    occ="0 flags (2nd audit: de-fr-occlusion2.txt)", p8="CLEAN 150=150, keydiff=[137, 138, 139, 150]",
    freeze="exit 0, TOTAL added CJK characters: 0", eq="49,789 bytes",
    web="1,069,996", printp="4,102,998"),
"es": dict(
    native="Spanish", badge='TEXTOS EN ALEMÁN · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES (20 pt, BRICK)',
    footer="Die Lucerna · SEMANARIO ALEMÁN VOL.3 · TEXTO EN ALEMÁN · EXPLICACIONES EN ESPAÑOL",
    pageline="Página N de 8", gloss="Nota — ", sep="— Página {pg} —", bracket=" ({note})",
    keys="12 pt / lh 1.22", svglib="core svglib.py unchanged",
    defects="First build: P6-main FLOW OVERFLOW (gloss 5 lines). Fixed by shortening the P6 gloss (“ofrenda” for “ofrenda floral”, 4 lines). Rebuild clean; occlusion 0 on first audit.",
    extra="Transform: 379 replacements, CJK leaks NONE. P8 keydiff [137, 138, 139, 150] is legitimate translation re-aiming (E-section).",
    occ="0 flags (de-es-occlusion.txt)", p8="CLEAN 150=150, keydiff=[137, 138, 139, 150]",
    freeze="exit 0, TOTAL added CJK characters: 0", eq="49,937 bytes",
    web="1,071,506", printp="4,046,442"),
"it": dict(
    native="Italian", badge="TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI (20 pt, BRICK)",
    footer="Die Lucerna · SETTIMANALE TEDESCO VOL.3 · TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO",
    pageline="Pagina N di 8", gloss="Nota — ", sep="— PAGINA {pg} —", bracket=" ({note})",
    keys="13 pt / lh 1.26", svglib="core svglib.py unchanged",
    defects="First build: HEAD TOO WIDE on the P8 F-head (“Abbinamento”). Fixed to “Coppie”. Rebuild clean; occlusion 0 on first audit.",
    extra="Transform: 379 replacements, CJK leaks NONE. P8 keydiff [137, 138, 139, 150] is legitimate translation re-aiming (E-section).",
    occ="0 flags (de-it-occlusion.txt)", p8="CLEAN 150=150, keydiff=[137, 138, 139, 150]",
    freeze="exit 0, TOTAL added CJK characters: 0", eq="49,406 bytes",
    web="1,063,521", printp="4,041,417"),
"pt": dict(
    native="Portuguese", badge='TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA (20 pt, BRICK)',
    footer="Die Lucerna · SEMANÁRIO ALEMÃO VOL.3 · TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS",
    pageline="Página N de 8", gloss="Nota — ", sep="— Página {pg} —", bracket="({note})",
    keys="13 pt / lh 1.26", svglib="core svglib.py unchanged",
    defects="First build: HEAD TOO WIDE on P8 A-head (“Texto com lacunas”) and F-head (“Correspondência”) — shortened to “Lacunas” / “Pares”. First occlusion audit: 1 BOXTITLE (“DIE WOCHE IN ZAHLEN · Em números”) — shortened to “Números”. Second audit: 0 flags.",
    extra="Transform: 379 replacements, CJK leaks NONE. P8 keydiff [137, 138, 139, 150] is legitimate translation re-aiming (E-section).",
    occ="0 flags (2nd audit: de-pt-occlusion2.txt)", p8="CLEAN 150=150, keydiff=[137, 138, 139, 150]",
    freeze="exit 0, TOTAL added CJK characters: 0", eq="49,507 bytes",
    web="1,075,455", printp="4,048,882"),
"nl": dict(
    native="Dutch", badge='TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS (20 pt, BRICK)',
    footer="Die Lucerna · DUITS WEEKBLAD VOL.3 · TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS",
    pageline="Pagina N van 8", gloss="Uitleg — ", sep="— Pagina {pg} —", bracket="({note})",
    keys="13 pt / lh 1.26", svglib="core svglib.py unchanged",
    defects="First build: P6-main FLOW OVERFLOW (gloss 5 lines) — P6 gloss shortened. First occlusion audit: 2 flags (BOXTITLE “SCHULWOCHE · Terug naar school” 0.8 px over → “Naar school”; LINEX P7 word-box gloss 3 lines → shortened). Second audit: 0 flags.",
    extra="Transform: 379 replacements, CJK leaks NONE. P8 keydiff [137, 138, 139, 150] is legitimate translation re-aiming (E-section).",
    occ="0 flags (2nd audit: de-nl-occlusion2.txt)", p8="CLEAN 150=150, keydiff=[137, 138, 139, 150]",
    freeze="exit 0, TOTAL added CJK characters: 0", eq="49,058 bytes",
    web="1,066,758", printp="4,101,695"),
"ru": dict(
    native="Russian", badge='ТЕКСТЫ НА НЕМЕЦКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ (20 pt, BRICK)',
    footer="Die Lucerna · НЕМЕЦКИЙ ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА НЕМЕЦКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ",
    pageline="Страница N из 8", gloss="Пояснение — ", sep="— СТРАНИЦА {pg} —", bracket="({note})",
    keys="13.0 pt / lh 1.16", svglib="core svglib.py unchanged",
    defects="First build: HEAD TOO WIDE on P8 A-head (“Текст с пропусками”) → “Пропуски”. First occlusion audit: 3 flags (Fragen subtitle too long → shortened; “IN DIESER AUSGABE · Содержание” → bare head; P7 word-box gloss 3 lines → shortened, measured 2 lines). Final audit: 0 flags. The verify paren-check string in the edition script was mis-authored at first (“3-е лицо, ед. число”); corrected to the actual key form “(3-е лицо ед. ч.)” — the keys themselves were always half-width.",
    extra="Transform: 379 replacements, CJK leaks NONE. P8 keydiff [137, 138, 139, 150] is legitimate translation re-aiming (E-section). NOTE: the local print PDF is 40,640,945 bytes — CairoSVG embeds the full CJK fonts when Cyrillic glyphs are used; the shippable web PDF is 1,105,087 bytes (< 7 MB) and the repo ships the web PDF.",
    occ="0 flags (3rd audit: de-ru-occlusion3.txt)", p8="CLEAN 150=150, keydiff=[137, 138, 139, 150]",
    freeze="exit 0, TOTAL added CJK characters: 0", eq="56,396 bytes",
    web="1,105,087", printp="40,640,945"),
"ja": dict(
    native="Japanese", badge='ドイツ語テキスト · 日本語の解説 — 日本語読者のための版 (19.5 pt, BRICK)',
    footer="Die Lucerna · ドイツ語週刊 VOL.3 · 本文はドイツ語 · 解説は日本語",
    pageline="N ページ（全 8 ページ）", gloss="解説 — ", sep="— {pg} ページ —", bracket=" ({note})",
    keys="13.0 pt / lh 1.16", svglib="kinsoku svglib.py copied from the W45 de-ja build (NO_START + seam repair); TC/SC font handling untouched",
    defects="Transform first run flagged 3 leftover literals that are identity replacements (core strings already correct Japanese: 生活/文化/和解) — documented exemptions in tr-ja.py CFG. P8 key strings first used full-width parens; corrected to half-width per the fan-out convention (verify paren check now True). Build clean, occlusion 0.",
    extra="Freeze diff exits 1 by design (added CJK expected): ADJUDICATED — 3,276 added CJK characters, verified by string-set diff: every added string is a Japanese translation/furniture string or a mechanical P8 key join of frozen German text + Japanese; no new German text added; no Simplified-Chinese markers; non-Japanese-range chars in added strings are only German umlauts/ß/„/→ from frozen German text. Transform: 379 replacements, leftover original literals NONE after exemptions.",
    occ="0 flags (2nd audit: de-ja-occlusion2.txt)", p8="CLEAN 150=150, keydiff=[137, 138, 139, 150]",
    freeze="exit 1, ADJUDICATED — TOTAL added CJK characters: 3,276 (all Japanese script)", eq="50,614 bytes",
    web="1,744,916", printp="18,319,846"),
"ko": dict(
    native="Korean", badge='독일어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판 (20 pt, BRICK) — NEW: W45 shipped no KO badge; W46 adds one per the task',
    footer="Die Lucerna · 독일어 주간지 VOL.3 · 텍스트는 독일어 · 해설은 한국어",
    pageline="제 N 면 / 총 8 면", gloss="해설 — ", sep="— 제 {pg} 면 —", bracket=" ({note})",
    keys="13.0 pt / lh 1.26", svglib="core svglib.py unchanged; bridge() kept (not renamed to expl())",
    defects="None geometry-wise on first build (zero overflows, occlusion 0). P8 key strings corrected to half-width parens with the JA/ZH-TW fix. Visual proofread 2026-11-02 caught a lone 。 orphan on the P1 bridge gloss (3-line wrap); gloss shortened to “Länderspielpause＝A매치 휴식 · Viertelfinale＝8강전 · ausverkauft＝매진” (2 lines), rebuilt/re-rendered/re-gated (build3/render3, occlusion 0, p8 CLEAN, freeze re-adjudicated).",
    extra="Freeze diff exits 1 by design (added Hangul expected): ADJUDICATED — 3,196 added CJK characters, verified by string-set diff: every added string is a Korean translation/furniture string or a mechanical P8 key join; no new German text; no Simplified-Chinese markers; non-Korean-range chars are only German umlauts/ß/„/→ from frozen German text. Transform: 379 replacements, leftover original literals NONE.",
    occ="0 flags (3rd audit: de-ko-occlusion3.txt)", p8="CLEAN 150=150, keydiff=[137, 138, 139, 150]",
    freeze="exit 1, ADJUDICATED — TOTAL added CJK characters: 3,196 (all Hangul/kanji in Korean strings)", eq="49,442 bytes",
    web="1,401,261", printp="9,078,460"),
"zh-tw": dict(
    native="Traditional Chinese", badge='德語正文 · 繁體中文講解 — 給繁體中文讀者的版本 (19.5 pt, BRICK)',
    footer="Die Lucerna · 德語週報 VOL.3 · 正文德語 · 講解繁體中文",
    pageline="第 N 版 / 共 8 版", gloss="譯注｜", sep="— 第 {pg} 版 —", bracket=" ({note})",
    keys="14.5 pt / lh 1.3 (core values kept)", svglib="TC-index svglib.py copied from the W45 de-zh-tw build (_tc_index, Noto CJK TC families)",
    defects="None geometry-wise (first build clean, occlusion 0). Translation method: core Simplified strings converted with opencc s2t (gen_tr_zhtw.py), hand-overridden badge line + MUSTER “範本（84 Wörter）” (W45 form, not 範文); the German readers'-corner label is kept verbatim as in W45 ZH-TW (documented exemption). Identity conversions (shared SC/TC glyphs) auto-exempted from the leftover check. One post-conversion fix: 意味着 → 意味著 (Taiwan usage). Context-sensitive conversions spot-checked (後/發/裏/併為 all correct). P8 key strings corrected to half-width parens with the JA/KO fix.",
    extra="Freeze diff exits 1 by design (added TC characters expected): ADJUDICATED — 1,043 added CJK characters, every one a legitimate Traditional character present in the TC translation table (plus 義/釋 from the instrmap “把詞和釋義配對”); no kana/Hangul; no Simplified-only characters except 家 (shared glyph in both scripts). Transform: 379 replacements, leftover original literals NONE after identity exemptions.",
    occ="0 flags (de-zh-tw-occlusion.txt)", p8="CLEAN 150=150, keydiff=[137, 138, 139, 150]",
    freeze="exit 1, ADJUDICATED — TOTAL added CJK characters: 1,043 (all Traditional Chinese)", eq="47,211 bytes",
    web="2,038,435", printp="16,633,773"),
"zh-cn": dict(
    native="Simplified Chinese (duplicate of the core)",
    badge='DIE WOCHENZEITUNG FÜR LERNENDE — subtitle slot, as in the core (the core IS the zh-cn edition)',
    footer="Die Lucerna · 德语周报 VOL.3 · LUCERNA GERMAN WEEKLY",
    pageline="第 N 版 / 共 8 版", gloss="译注｜", sep="— 第 {pg} 版 —", bracket="（note） full-width, as in the core",
    keys="14.5 pt / lh 1.3 (core values)", svglib="core svglib.py unchanged",
    defects="None — this is an identical-content re-render of the frozen core (OUT paths repointed only). All 8 SVGs byte-identical to the core dir (verified with cmp).",
    extra="DUPLICATION NOTICE: insert ONE of core / zh-cn for slug 2026-w46-de-zh-cn, never both (see the core KIT). This dir exists so the zh-cn edition stands alone with its own render, gates, KIT, ABSTRACT and text.md.",
    occ="0 flags (de-zh-cn-occlusion.txt)", p8="CLEAN 150=150, keydiff=[] (identical)",
    freeze="exit 0, +0/−0 strings, TOTAL added CJK characters: 0", eq="47,647 bytes (identical to core)",
    web="1,670,903", printp="16,578,199"),
}

TEMPLATE = """# Die Lucerna — 德语周报 VOL.3 · {NATIVE}-EXPLANATIONS EDITION · WEEKLY KIT

**Edition:** German core VOL.3 × {native} explanations — **matrix cell DE × {CODE}**.
Target language German, reader native language {native}; both dimensions named in
full. The German text is the frozen W46 DE core
(`files/weekly-report-w46-de-core/`, Die Lucerna VOL.3); only the explanation
layer was rewritten, natively in {native}. No frozen German line was edited,
moved, or deleted to fit the furniture.

**Week:** Mon 2026-11-09 → Sun 2026-11-15 (P1 header:
`WOCHE VOM 9. BIS 15. NOVEMBER 2026`). Slug week `2026-w46`, frontmatter
week `2026-W46`. **Press time: 2 November 2026** — 9–15 Nov events are
previews; unknowns are stated on the page (see the core KIT §§2–3 for the
fact record, the W45-promises cross-check, and the readers'-letters
disclosure carried to VOL.4). **150 exercises** (P1 10 · P2–P6 18 each ·
P7 12 · P8 38; A2 66 / B1 70 / B2 14), numbering continuous 1–150, P8
answers registry-generated. P7 golden sentences verbatim from this issue's
articles (8, each exactly 2×). Images: the two verified PD soccer photos
reused from W45 (see the core KIT §4); the unverifiable American-football
photo was rejected and is used nowhere.

**Status: builder-complete，未定稿，待独立校对。** This KIT records the
builder's own gates only. It is NOT a finalization claim, NOT an independent
proofread verdict. Nothing was posted to Discord, nothing was sent into the
main chat, no cron was created, `~/workspace/weekly-git` was not touched,
and no W43/W45 directory was modified. No subagent was spawned.

## 1. Pairing furniture

- **Masthead (from the core, unchanged):** `Die Lucerna`, UnifrakturMaguntia
  168 pt, centred x=975, baseline y=262.
- **P1 pairing badge (subtitle slot, y=372):** `{BADGE}` — centred.
- **Top strapline (P1, y=92):** `WÖCHENTLICH AUF DEUTSCH · …` in the
  reader language (see the transform file for the exact string).
- **Footer, all 8 pages:** `{FOOTER}` — present 8/8.
- **Page lines, all 8 pages:** `{PAGELINE}` (8/8).
- **Gloss prefix:** `{GLOSS}` **P8 separator:** `{SEP}` **P8 note brackets:**
  `{BRACKET}` **P8 keys size:** {KEYS}.
- **svglib:** {SVGLIB}.

## 2. Method

Build dir: `hidden_files/weekly-report-w46-de-{code}-build/` (copy of the
frozen core build; OUT paths repointed to this edition's `svg/` dir).
Transform: `hidden_files/w46/transform-{code}.py`, generated by
`hidden_files/w46/gen_transform.py` from `en-pairs.json` + `tr-{code}.py`
(whole-line / exact-literal replacements with count assertions; German body
text never touched). The generator's leak check passed (see §4). Render:
`hidden_files/w46/de-{code}/render.py` (cards PNG @1950 + print PDF via
CairoSVG/pypdf + web PDF via `tools/webpdf.py`). Verify:
`hidden_files/w46/de-{code}/verify.py` (one-process re-run, byte-identity,
verbatim 8/8, furniture checks). `.text.md` exported from the edition's own
build sources via `hidden_files/w46/export_textmd.py` (AST, in order).

## 3. Gates

- Builder self-check (`verify.py`): 150 exercises, verbatim 8/8, SVGs
  byte-identical on re-run, footer/page lines 8/8, badge present, top band
  no overlap, MUSTER 84 words. Log: `hidden_files/w46/de-{code}/verify.log`.
- Occlusion audit (`tools/occlusion_audit.py`, incl. LINEX + same-baseline
  furniture scan + chart GRAZE check): **{OCC}**.
- P8 compare (`tools/p8.py compare`, explicit core/edition paths):
  **{P8}**. Log: `hidden_files/w46/de-{code}-p8.txt`.
- Freeze diff (`tools/freeze.py diff --strict-cjk`): **{FREEZE}**.
  Log: `hidden_files/w46/de-{code}-freeze.txt` (+ `.json`).
- Web/print text: `pdftotext` normalised text identical, {EQ}.
- Web PDF `Die-Lucerna-VOL3-{SUFFIX}-web.pdf` {WEB} bytes (< 7 MB); print
  PDF `Die-Lucerna-VOL3-{SUFFIX}.pdf` {PRINT} bytes (local print master;
  the repo ships the web PDF as `<slug>.pdf`).

## 4. Defects fixed / notes

{DEFECTS}

{EXTRA}

## 5. Honest shortfalls

Same as the core KIT §8 (no real letters known; press-time unknowns stated
on the page; P6 chart is labelled practice data; no dedicated NFL photo).
Shortened glosses/titles/invites listed in §4 are translation choices, not
content changes; the German body text is frozen and untouched.
"""

for code, d in ED.items():
    suffix = {"en": "EN", "fr": "FR", "es": "ES", "it": "IT", "pt": "PT",
              "nl": "NL", "ru": "RU", "ja": "JA", "ko": "KO",
              "zh-tw": "ZH-TW", "zh-cn": "ZH-CN"}[code]
    text = TEMPLATE.format(
        NATIVE=d["native"].upper(), CODE=code.upper(), native=d["native"],
        code=code, BADGE=d["badge"], FOOTER=d["footer"],
        PAGELINE=d["pageline"], GLOSS=d["gloss"], SEP=d["sep"],
        BRACKET=d["bracket"], KEYS=d["keys"], SVGLIB=d["svglib"],
        OCC=d["occ"], P8=d["p8"], FREEZE=d["freeze"], EQ=d["eq"],
        SUFFIX=suffix, WEB=d["web"], PRINT=d["printp"],
        DEFECTS=d["defects"], EXTRA=d["extra"])
    p = os.path.join(GOAL, "files", f"weekly-report-w46-de-{code}", "WEEKLY-KIT.md")
    open(p, "w", encoding="utf-8").write(text)
    print(code, len(text))
