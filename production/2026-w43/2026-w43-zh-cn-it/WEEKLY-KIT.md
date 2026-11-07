# Lucerna Weekly VOL.1 — Edizione zh-CN × IT (testi in cinese semplificato, spiegazioni in italiano)

Fan-out of the frozen VOL.1 Simplified Chinese core (`files/weekly-report-zhcn-vol1/`).
Target text, images and layout geometry are the core's, unchanged; the entire explanation
layer (glosses, grammar notes, instructions, exercise apparatus, all 150 P8 answer notes)
is rewritten in Italian for Italian-speaking readers. Issue week: Mon 19 – Sun 25 Oct 2026.
Build code: `hidden_files/weekly-report-zh-cn-it-build/` (copy of the core build).

## Baseline proof (before any edit)

The unmodified copy of the core build was run with its output pointed at a scratch
directory inside the build dir (`scratch/baseline-svg/`). It reproduced all 8 shipped
core SVGs **byte-identically (sha256 8/8)**. After all work was finished, the shipped
core SVGs were re-hashed and diffed against that baseline reproduction: **zero
differences — the frozen core is untouched.**

## Totals (identical to the core)

- 150 exercises: A2 56 · B1 65 · B2 29.
- Per page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- Types (Italian names, core counts): Completa la frase 68 · Scelta multipla 50 ·
  Abbinamento 20 · Scelta in contesto 11 · Scrittura 1.
- Writing model (#150): 148 characters, as in the core.
- Registry pages/levels identical to the core for all 150 items; **all 150 notes
  rewritten** (0 notes carried over unchanged).

## Key-diff registry (complete)

Keys are byte-identical to the core for 149 of 150 items. The single documented
difference is the #150 apparatus key:

- #150 key: core `(开放题，范文如下)` → IT `(domanda aperta — modello qui sotto)`
- #150 note: core `开放题——范文在本版F部分，共148字。` → IT
  `Domanda aperta — il modello è nella sezione F di questa pagina, 148 caratteri`

No other key differs. (The core has no translation-type items, so no stem changes
were needed anywhere.)

## Answer-key format and pinyin discipline

- Entries print as `N. key (note)` — space before the parenthesis, half-width
  parentheses only, page separators `— Pagina N —`, writing entry `N. ✓ (note)`.
- In the printed P8 answer block: full-width parentheses = **0**; Han characters
  inside parentheses = **0**. Chinese words cited inside Italian notes appear in
  pinyin (e.g. Chóngyáng, Shuāngjiàng, biàn chā zhūyú shǎo yì rén), mirroring the
  shipped zh-CN × ES sibling. (Full-width parentheses that remain on P8 are inside
  the frozen Chinese exercise stems, byte-identical to the core; the core's own two
  in-note full-width glosses — ##53, 147 — are gone in this edition.)

## Pairing furniture (verbatim, as printed)

- P1 badge (brick slot): `TESTI IN CINESE SEMPLIFICATO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI`
- P1 strap: `SETTIMANALE CINESE SEMPLIFICATO · VOL.1 · 双11 · 大闸蟹 · 霜降`
- Footer (all 8 pages): `Lucerna · SETTIMANALE CINESE SEMPLIFICATO VOL.1 · TESTI IN CINESE SEMPLIFICATO · SPIEGAZIONI IN ITALIANO` / `Pagina N di 8`
- Gloss prefix: `Nota — `
- Masthead: `Lucerna` (no article), exactly as the core ships.
- Measured fits: the P7 structure-box title `本周句式 · Struttura della settimana`
  measures 411.0 units against 412.0 available; rendered ink ends at x=1884 with the
  box border at x=1885 — inside, no overflow, no wording change. No furniture string
  needed shortening; geometry was never touched. Three section titles were given
  slightly shorter Italian wording during the rewrite to stay inside the build's own
  width checks (P2 calendar box, P5 high-frequency-words box, P6 crab-facts box);
  the build runs with zero HEAD TOO WIDE / overflow warnings.

## Printed-note set verification (from the rendered P8 SVG)

Sequential parse of the rendered answer blocks: core prints entries 1–150 (149 with
dash notes + the #150 writing entry); this edition prints entries 1–150, each with a
parenthesised Italian note (150/150). **Printed-note sets are equal: {1..150}.**
All 8 P7 phrases of the week occur exactly 2× in the full issue text (source page +
P7), with `Pagina N` tags, identical counts to the core.

## Freeze check (text diff vs core)

Per-page CJK accounting on the rendered SVGs: **Chinese characters added = 0 on every
page.** Removals on P1–P7 are confined to pairing-furniture characters (footer, badge,
strap). P8 removals are the Chinese words that the core's English notes cited inline;
in this edition those citations are pinyin/Italian (see the discipline above) — no
exercise stem changed. Embedded image payloads are byte-identical to the core on
every page (1/1/2/2/1/2/0/0 images).

## Geometric occlusion audit (mandatory gate)

Audit script (paint-order SVG parse, real-font PIL glyph metrics, line boxes expanded
by half stroke width; classes COVER / LINEX / LINEXB / FOOTER / EDGE / BOXTITLE) was
validated on a synthetic positive control first — all 6 classes fired, clean text
unflagged. Real runs:

- First run on this edition: **5 flags**. Pixel adjudication on the rendered cards:
  - P2 word card 定金 — **REAL DEFECT**: the definition wrapped to a second line
    («prima») whose ink crossed the card's bottom border (ink rows 1766–1777 vs
    border y=1768). Fixed by wording only: «piccola parte del prezzo, pagata prima»
    now fits on one line inside the card. Whole issue re-rendered.
  - 4 remaining flags are grazes also present in the core at identical coordinates,
    pixel-adjudicated non-defects: P2 «E tu?» box last line (ink ends row 1159,
    border 1164.95); P2 «Ricorda la frase» line (text ink ends row 1800, rule rows
    1803–1804); P3 «E tu?» box (ink 1378 vs border 1384.1); P5 «E tu?» box (ink 1208
    vs border 1213.6).
- Final run after the fix: **4 flags, all adjudicated above; 0 unresolved.**

## Terminology rule

The intermediary-layer term (Chinese or English form) occurs **0 times** in the paper,
in this KIT, and in the operative build code (grep-verified). The core build's gloss
method is named `glossline()`; no method rename was required. One-off transform
scripts live in the build dir's `scratch/` subdir.

## Content facts (from the core KIT, unchanged)

Lead: 双11 tail-payment week (Tmall tail payments Tue Oct 20, 20:00). Hairy-crab data:
Xinfadi ~3两 females ¥77.5/斤 (Mid-Autumn) → ¥57.5/斤 on Oct 6; the −25.8% figure is
labelled computed in the paper ((77.5−57.5)/77.5 = 25.8%). 重阳 = Sun Oct 18, 2026
(retrospective); 霜降 = Fri Oct 23. Gymnastics gap 251.928 − 249.193 = 2.735. Zero
politics, per the zh-edition rule.

## Image credits (from the core KIT; images byte-identical)

- P1 parcel locker — Map hobby, CC0 (Wikimedia Commons)
- P2 autumn valley — Paul Gilmore, CC0 (Wikimedia Commons)
- P3 chrysanthemum — PushpaKhan, CC0 (Wikimedia Commons)
- P3 frosted leaves — Gerda Arendt, CC0 (Wikimedia Commons)
- P4 basketball — noahsilliman, CC0 (Wikimedia Commons)
- P4 gymnastics 1896 — unknown author, 1896, public domain (Wikimedia Commons)
- P5 LAN party (2003 file photo) — Syced, CC0 (Wikimedia Commons)
- P6 crab, cut + mini crabs — Fumikas Sagisavas, CC0 (Wikimedia Commons)

## Deliverables and PDF pins

- `svg/` ×8, `cards/` ×8 (1950×2700) in this directory.
- Print PDF: `Lucerna-VOL1-IT.pdf` — 67,291,606 bytes —
  sha256 `cb99ae772c661cd136857d866d850c0a75dd0eb1e7197aea9db5159220439fe9`
- Web PDF: `Lucerna-VOL1-IT-web.pdf` — 3,246,493 bytes (< 10 MB) —
  sha256 `d61b31da346d90f9682fc7c51a15df0c95dfbfa706850eae61f00b5015433d99`
  (These pins supersede the builder's originals — 67,291,731 /
  `d62ba9f0…` and 3,246,674 / `6c8b8cec…` — after the proofreader's
  P7 title fix and full re-render; see the proofread record below.)

## Proofread status

Builder's full proofread: **done** (every page read end-to-end from the rendered
cards; all 150 keys re-derived from the Chinese text, incl. the crab arithmetic;
every weekday/date claim checked against the 2026 calendar, Europe/Rome).
Independent proofread: **PASS** (2026-10-21, independent proofreader;
one complete pass with zero problems on the final artifacts, after one
proofreader fix — full record below).

### Independent proofread record (zh-CN × IT)

**Verdict: PASS.** One defect found and fixed during the pass; the entire
pass was then re-run from the top on the final artifacts and found zero
problems.

**The one fix (explanation layer only).** P7 structure-box title: the
builder's measurement (ink ends x=1884 vs border 1885) was wrong. The
proofreader's PIL real-font measurement gives ink right edge 1886.6
against the box border at x=1885, and the rendered card confirms glyph
ink reaching columns 1885–1886 — the final letter of the Italian title
touches the box's right border (the class the geometric gate exists to
catch). Fixed by Italian wording only, Chinese part byte-identical:
「本周句式 · Struttura della settimana」→「本周句式 · La struttura
settimanale」 (IT build `content7.py`). Post-fix: PIL ink right edge
1874.9; card pixels: rightmost dark pixel in the title rows = 1874,
11 px clear of the border. Whole issue re-rendered; only the p7 SVG
changed (all other SVGs byte-identical); final PDF pins above supersede
the builder's.

**Freeze vs the frozen core.** Baseline independently reproduced: an
unmodified copy of the core build regenerates all 8 shipped core SVGs
byte-identically (8/8). The edition build reproduces the shipped edition
SVGs 8/8, before and after the fix (source = shipped artifact). Rendered
text diff, all 8 pages: Chinese characters ADDED = 0 on every page;
every removal is pairing furniture or a Chinese citation inside a core
English note (converted to pinyin); every other difference is the
Italian explanation layer or the documented registry item. Images
byte-identical to the core on every page (md5 lists equal, in order;
counts 1/1/2/2/1/2/0/0). Credits match the placed images and the core KIT.

**Keys.** Independent registry dump from the final build vs the core:
page and level identical for all 150; key diff = exactly one item,
#150 (key → «(domanda aperta — modello qui sotto)»); all 150 notes
rewritten in Italian, 0 carried over. All 150 keys re-derived from the
Chinese text, incl. crab (77.5−57.5)/77.5 = 25.8 % and gymnastics
251.928 − 249.193 = 2.735. Totals 150 (A2 56 · B1 65 · B2 29); per page
10/18/18/18/18/18/12/38; types Completa la frase 68 · Scelta multipla 50 ·
Abbinamento 20 · Scelta in contesto 11 · Scrittura 1; writing model
148 characters, byte-identical to the core's model.

**Printed-note set equality.** Extracted by number from both shipped P8
SVGs: core set {1..150} = edition set {1..150}, EQUAL; every entry in
both editions carries its note. Pinyin discipline on the rendered
edition P8: full-width parentheses in the answer block = 0 (the core's
two in-note full-width glosses, ##53 and 147, are both converted); Han
characters inside parentheses = 0; full-width parens remain only inside
frozen Chinese exercise stems. Pinyin conversions sample-verified
against the core's cited words: dìngjīn, wěikuǎn, mǎnjiǎn, Chóngyáng,
Shuāngjiàng, zhūyú, biàn chā zhūyú shǎo yì rén, yuánqí, bǔdōng bùrú bǔ
shuāngjiàng, dēnggāo, cǎomù huángluò, sānliǎng — all correct.

**P7 phrases.** Each of the 8 phrases occurs exactly 2× issue-wide (once
on its tagged source page, once on P7), verbatim-contiguous, in both
editions; the edition's tags read (Pagina 1, 1, 2, 3, 4, 4, 5, 6),
matching the core's (p. 1 … p. 6).

**Calendar + politics.** Every weekday/date claim verified against the
real 2026 calendar: 重阳 Sunday Oct 18; fashion show Monday Oct 19;
tail payments Tuesday Oct 20, 20:00; 霜降 Friday Oct 23 (four separate
claims, all «venerdì»); 立冬 Nov 7. Politics-term scan: zero hits in
both editions.

**Geometric occlusion audit (proofreader's own implementation).**
Paint-order SVG parse; per-glyph ink boxes from PIL with the real fonts
(Noto Serif/Sans CJK, SC face, Regular/Bold), line boxes expanded by
half the stroke width. Validated BEFORE the real run on six synthetic
positive controls (COVER / LINEX / FOOTER / EDGE / TITLEX / TEXTX all
fire) and on a real-world control: the PT core's known P1 numbers-box
title overshoot reproduced exactly (measured ink 968.4 vs border 961,
TITLEX fired). On the final edition, ink model: exactly 2 flags, both
the same graze — P2 «Ricorda la frase» line, two full-width commas vs
the rule at y=1804. Pixel adjudication on the 1:1 card: rendered ink
ends at row 1800, rule occupies rows 1803–1804, zero intersection —
non-defect, identical geometry in the core. The sensitive em-box
variant flags 85 (37 LINEX + 48 TEXTX), every one cleared by the ink
model (adjacent-line em overlap and descent proximity; no ink contact).
The builder's four claimed grazes all verified, incl. pixel-exact: P3
«E tu?» box ink bottom row 1378 vs border 1384.1. The builder's in-build
P2 fix is pixel-verified: the 定金 gloss «piccola parte del prezzo,
pagata prima» prints as ONE line; card ink rows 1741–1756; rows
1757–1768 (up to the card's bottom border at y=1768) contain zero dark
pixels — no straddle.

**Furniture.** Badge verbatim on P1 («TESTI IN CINESE SEMPLIFICATO ·
SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI»); pairing
footer «Lucerna · SETTIMANALE CINESE SEMPLIFICATO VOL.1 · TESTI IN
CINESE SEMPLIFICATO · SPIEGAZIONI IN ITALIANO» and «Pagina N di 8» on
all 8 pages; gloss prefix «Nota — »; masthead «Lucerna» (no article).
Italian completeness: every explanation element is Italian on all 8
pages; the only English retained is the frozen source name «(The
Beijing News)» on P4, identical in the core. The intermediary-layer
term (both language forms): 0 occurrences in the paper, this KIT, and
the operative build code.

**KIT correction (documentation only, paper unaffected).** The builder's
section above quotes the core's #150 note as a Chinese sentence; the
actual core registry note is 'Open task - the model answer is printed
in section F above (148 characters)'. The edition's Italian note is a
faithful rendering of the actual core note.

**Core integrity.** The frozen core's shipped SVG hashes were recorded
before the pass and re-verified after all work: unchanged, 8/8.

**Final pins.** Web PDF 3,246,493 B, sha256
`d61b31da346d90f9682fc7c51a15df0c95dfbfa706850eae61f00b5015433d99`
(< 10 MB); print PDF 67,291,606 B, sha256
`cb99ae772c661cd136857d866d850c0a75dd0eb1e7197aea9db5159220439fe9`.
