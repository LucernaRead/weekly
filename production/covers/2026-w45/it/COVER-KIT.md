# W45 Weekly Cover — Italian readers (cover-w45-it)

- Week: November 2–8, 2026 (W45). Reader language: Italian (it).
- Masthead: "La Lucerna" (Italian article convention). The cover itself carries
  NO VOL number of its own; it is marked COVER with a visible olive COVER badge
  on P1 (per the binding task spec for this edition).
- Spec: SOP appendix five — 8 pages, 1950×2700, weekly visual system:
  warm ivory #f7f1e2, deep olive accents, serif.
- Build: `hidden_files/cover-w45-it-build/` (`build_cover.py` + copied `svglib.py`
  from cover-w45-en-build + `svg/` + rendered `png/` proofs). No content module
  from any core build dir was imported; only the svglib library code was copied.
- Final PDF built ONLY with `tools/webpdf.py` (text-layer web PDF).

## The 12 sources (fixed order, verbatim from cover-backfill/headlines-w45.json)

Headlines and excerpts are loaded programmatically from the shared JSON at build
time, never retyped. Before building, every headline + excerpt was checked
against its core's P1 SVG: 12/12 headlines and 12/12 excerpts confirmed present
in the cores, so no JSON-vs-core discrepancy was found and none was fixed.
(Note: the JSON's spacing, e.g. "America Votes : Election Day..." and
"Paris, Plailly, Port-en-Bessin : le week-end...", is reproduced verbatim.)

| # | Source | Core paper masthead / VOL (P8) | Headline (verbatim) |
|---|--------|-------------------------------|---------------------|
| 1 | en | The Lucerna · VOL.2 | America Votes : Election Day Comes on Tuesday, November 3 |
| 2 | de | Die Lucerna · VOL.2 | Englische Woche in Deutschland: Vier Nächte Fußball, dann der 9. Spieltag |
| 3 | fr | Le Lucerna · VOL.3 | Paris, Plailly, Port-en-Bessin : le week-end où tout se joue |
| 4 | es | La Lucerna · VOL.2 | La cuenta atrás del 29-N: la vivienda decide la campaña |
| 5 | it | La Lucerna · VOL.2 | Arriva il primo freddo: l'Italia si copre e si mette a tavola |
| 6 | pt | A Lucerna · VOL.2 | Do feriadão à prova: a semana do Enem |
| 7 | nl | De Lucerna · VOL.2 | Nederland in de Klimaatweek: bomen, musea en voetbal |
| 8 | ru | Lucerna · VOL.2 | Одна среда посреди недели |
| 9 | ja | Lucerna · VOL.2 | 文化の日と紅葉の週末 |
| 10 | ko | Lucerna · VOL.2 | 겨울이 오는 주간 — 단풍의 끝, 김장의 시작 |
| 11 | zh-cn | Lucerna · VOL.2 | 双11还在进行，冬天也要来了 |
| 12 | zh-tw | Lucerna · VOL.2 | 金融科技週開幕！香港迎四萬五千人 |

W45 VOLs per task: FR is VOL.3; all other 11 cores are VOL.2. These appear
only on P8 (the cover itself has no VOL; P1 text contains no "VOL").
No script conversion was applied: the zh-tw item stays Traditional and the
zh-cn item stays Simplified throughout; explanations are in Italian.
Cover-original text uses ASCII apostrophes only (no U+2019).

Language tags (Italian reader name + native label, no language codes on pages):
INGLESE · English, TEDESCO · Deutsch, FRANCESE · Français, SPAGNOLO · Español,
ITALIANO · Italiano, PORTOGHESE · Português, OLANDESE · Nederlands,
RUSSO · Русский, GIAPPONESE · 日本語， COREANO · 한국어,
CINESE SEMPLIFICATO · 简体中文， CINESE TRADIZIONALE · 繁體中文.

## Layout (binding, 8 pages)

- P1: masthead "La Lucerna" + COVER badge + week label "2-8 novembre 2026" +
  cover title "Dodici prime pagine, una settimana" + 1-sentence generic framing
  intro (no new facts) + 12 headline teasers in fixed order (language tag +
  verbatim headline, smaller type).
- P2–P7, 2 items per page in fixed order: P2 EN, DE · P3 FR, ES · P4 IT, PT ·
  P5 NL, RU · P6 JA, KO · P7 zh-cn, zh-tw. Each item: source-language tag,
  verbatim headline, verbatim excerpt (max 4 sentences each, as extracted),
  then a 1–2 sentence "SPIEGAZIONE" in Italian. Every explanation claim is
  traceable to that item's headline + excerpt only; no external facts.
- P8: "I dodici giornali di questa settimana" — the 12 core papers at a glance
  in fixed order, each with masthead + VOL + verbatim headline, nothing invented.
- Fonts: Noto Serif/Sans CJK, per-script faces (SC for Latin/Cyrillic/zh-cn,
  JP for Japanese, KR for Korean, TC for Traditional Chinese) so all 12 scripts
  render with real glyphs.

## Verification outputs

- Visual eyeball: all 8 pages rendered to PNG (CairoSVG) and inspected — no
  overflow, no cut-off text, no tofu/missing glyphs, no overlapping elements
  in any of the 12 scripts. (Pages carry generous bottom whitespace; content
  ends well above the footer.)
- Occlusion audit (`tools/occlusion_audit.py` on the edition SVGs): selftest OK
  (all 6 planted classes fired, clean controls silent); final run **0 flags**.
- Final PDF: `cover-w45-it.pdf`, 8 pages, **408,870 bytes** (< 7 MB),
  built with `tools/webpdf.py`.
- Text layer: `pdftotext` returns **9,506 bytes** (non-empty). All 12 headlines
  extract verbatim (12/12 OK); all 12 excerpts extract verbatim (12/12 OK,
  whitespace-normalized; CJK also confirmed space-stripped).
- P8 VOL check: VOL.2 × 11, VOL.3 × 1 (FR). P1 contains no "VOL".
  Page text contains no week codes (no "W45"/"W43"), no language codes,
  no repo links, no internal column names.
- Fixed order, P2–P7 pairings, P1 masthead + COVER badge, no own VOL, and
  P8 masthead + VOL all confirmed by build construction + visual inspection.

## Issues found + fixed

1. None during build. The layout was adapted from the proven cover-w45-en-build
   (same geometry, same tag-to-headline step of 74 units that cleared the
   en-cover audit), and the first build passed the occlusion audit with
   0 flags and visual inspection clean on all 8 pages, so no layout fix
   was needed.

## Flag for the parent (standing-rule conflict, NOT resolved unilaterally)

During this build, MEMORY.md gained a new user rule (2026-10-28): public-facing
pages must not carry internal production structure — week codes, language codes,
placeholder labels, repo links, internal column names, or "cover" as an internal
product name. This edition complies on every point except one: the binding task
spec for this edition explicitly required the P1 masthead + COVER badge and
"mark it COVER", so the COVER badge and the word COVER in headers/footers were
kept as specified. No week codes, language codes, repo links, or internal names
appear on any page. Whether the COVER marking itself should change under the
new rule is a parent/user decision — the task spec and the new rule point in
different directions here, and this build followed the explicit task spec.

## Fix record — grave-accent defect class + KO accuracy rewrite (2026-10-28/29)

Proofread found exactly 12 problems, all in cover-original Italian text:
grave accents systematically stripped, so "è" (is) read as "e" (and) in
four explanations. Each fix below replaced the identified sentence in
`hidden_files/cover-w45-it-build/build_cover.py` with the correct sentence
given in the fix task; verbatim headlines/excerpts, tags, masthead, and VOL
were not touched. No headline, excerpt, tag, masthead, or VOL text changed.

1. P1 intro (token only) — old: "…su che cosa dice e perche merita attenzione."
   → new: "…su che cosa dice e perché merita attenzione."
2. P2, DE explanation — old: "Una settimana piena di calcio: Champions League martedi e mercoledi, Europa League giovedi e da venerdi la nona giornata di Bundesliga."
   → new: "Una settimana piena di calcio: Champions League martedì e mercoledì, Europa League giovedì e da venerdì la nona giornata di Bundesliga."
3. P3, ES explanation — old: "Con le liste gia presentate, i partiti ora scrivono i loro programmi in vista delle elezioni generali di domenica 29 novembre, una campagna in cui la casa decide."
   → new: "Con le liste già presentate, i partiti ora scrivono i loro programmi in vista delle elezioni generali di domenica 29 novembre, una campagna in cui la casa decide."
4. P4, IT explanation — old: "Lunedi 2 novembre arriva il primo freddo vero della stagione, con piogge sul versante adriatico e la prima neve leggera in montagna; novembre potrebbe essere piu freddo della media, ma si tratta di una probabilita, non di una certezza."
   → new: "Lunedì 2 novembre arriva il primo freddo vero della stagione, con piogge sul versante adriatico e la prima neve leggera in montagna; novembre potrebbe essere più freddo della media, ma si tratta di una probabilità, non di una certezza."
5. P4, PT explanation — old: "La settimana va dalla festivita di Finados di lunedi 2 novembre al primo giorno dell'Enem domenica 8 novembre: riposo, ripasso e prova per tutto il paese."
   → new: "La settimana va dalla festività di Finados di lunedì 2 novembre al primo giorno dell'Enem domenica 8 novembre: riposo, ripasso e prova per tutto il paese."
6. P5, NL explanation — old: "Dal 2 all'8 novembre nei Paesi Bassi e la Settimana del Clima: i comuni di tutto il paese organizzano azioni come piantare alberi, risparmiare energia e andare in bicicletta invece che in auto, e tutti possono partecipare."
   → new: "Dal 2 all'8 novembre nei Paesi Bassi è la Settimana del Clima: i comuni di tutto il paese organizzano azioni come piantare alberi, risparmiare energia e andare in bicicletta invece che in auto, e tutti possono partecipare."
7. P5, RU explanation — old: "Una settimana insolita in Russia: si lavora lunedi e martedi, poi mercoledi 4 novembre e giorno libero, proprio nel mezzo della settimana lavorativa."
   → new: "Una settimana insolita in Russia: si lavora lunedì e martedì, poi mercoledì 4 novembre è giorno libero, proprio nel mezzo della settimana lavorativa."
8. P6, JA explanation — old: "Il Giorno della Cultura cade martedi 3 novembre: e una festivita nazionale, scuole e aziende chiudono e in tutto il paese si svolgono eventi culturali."
   → new: "Il Giorno della Cultura cade martedì 3 novembre: è una festività nazionale, scuole e aziende chiudono e in tutto il paese si svolgono eventi culturali."
9+10. P6, KO explanation (accent + accuracy: Ip-dong is the first WINTER term
    among the 24, not a term to which all 24 belong to winter) — old: "La settimana dal 2 all'8 novembre segna l'arrivo dell'inverno: sabato 7 novembre e Ip-dong, la prima delle 24 stagioni solari che appartengono all'inverno."
    → new: "La settimana dal 2 all'8 novembre segna l'arrivo dell'inverno: sabato 7 novembre è Ip-dong, la prima stagione solare dell'inverno tra le 24."
11. P7, zh-cn explanation — old: "Il periodo di saldi del Doppio 11 e gia iniziato, con merci in vendita da meta ottobre fino al 13 novembre, proprio mentre arriva l'inverno."
    → new: "Il periodo di saldi del Doppio 11 è già iniziato, con merci in vendita da metà ottobre fino al 13 novembre, proprio mentre arriva l'inverno."
12. P7, zh-tw explanation — old: "La Settimana FinTech di Hong Kong x StartmeupHK 2026 si apre lunedi 2 novembre e dura cinque giorni fino a venerdi 6 novembre, con conferenza ed esposizione principali, piu oltre 100 eventi di comunita e oltre 45.000 partecipanti attesi."
    → new: "La Settimana FinTech di Hong Kong x StartmeupHK 2026 si apre lunedì 2 novembre e dura cinque giorni fino a venerdì 6 novembre, con conferenza ed esposizione principali, più oltre 100 eventi di comunità e oltre 45.000 partecipanti attesi."

Same-class sweep: after applying 1–12, ALL cover-original Italian text was
scanned (P1 intro, all 12 explanations, labels, P8 headings) for any other
missing grave accent (è, già, più, metà, probabilità, festività, comunità,
perché, lunedì/martedì/mercoledì/giovedì/venerdì, plus città/realtà-type
forms). Result: NO additional instance found — sweep additions: none.
The remaining "e" forms in the untouched EN explanation ("e i governatori")
and FR explanation ("e la settimana") are the conjunction "and" and are
correct as written. Verbatim headlines/excerpts were left untouched even
where they contain unaccented forms.

Rebuild: SVGs regenerated from `build_cover.py`, copied to the edition
`svg/` dir, PDF rebuilt ONLY via
`tools/venv/bin/python tools/webpdf.py files/cover-w45-it/svg files/cover-w45-it/cover-w45-it.pdf`.

Re-verification outputs (post-fix):
- All 12 correct sentences present verbatim in edition SVGs AND in PDF text
  (whitespace-normalized check, 12/12 each); all 12 old unaccented fragments
  absent from SVGs and PDF text (12/12 each); tokens perche/martedi/
  mercoledi/giovedi/venerdi/lunedi/probabilita/festivita/comunita absent
  from SVG and PDF text.
- Occlusion audit (`tools/occlusion_audit.py` on edition SVGs): selftest OK
  (all 6 planted classes fired, clean controls silent); final run 0 flags,
  exit 0.
- PDF: 8 pages, 409,248 bytes (< 7 MB), `pdftotext` 9,518 bytes (non-empty),
  all 12 headlines extract verbatim (12/12) and all 12 excerpts extract
  verbatim (12/12, whitespace-normalized; CJK also space-stripped).
- SVGs changed vs pre-fix set: p1, p2, p3, p4, p5, p6, p7 changed; p8
  UNCHANGED (SHA-256 172281d811a7d0c92e79c184b44a805c56bb757e18b74121ebce7071b2cff929
  before and after). Build SVGs and edition SVGs are byte-identical.
- Nothing else changed: P8 VOL check still VOL.2 × 11, VOL.3 × 1 (FR);
  P1 contains no "VOL"; masthead "La Lucerna", P1 title, P8 headings, tags,
  and all headlines/excerpts confirmed present verbatim as before.
- New PDF: 409,248 bytes (was 408,870), pdftotext 9,518 bytes (was 9,506),
  SHA-256 890c993a5b83aa081dd3432484eb9e3374b3527056c09a674aaaa4bc53bbf6f1
  (was 20d39bd602157429d23676f25b75df48c2e3138d2db500d0006dff06783e4051).
