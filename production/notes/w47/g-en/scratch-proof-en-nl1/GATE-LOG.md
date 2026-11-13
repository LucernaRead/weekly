# GATE-LOG — W47 en-nl proof1 (re-fanout #2 rebuild)

- **Edition:** `production/2026-w47/2026-w47-en-nl/`
- **Run:** 2026-11-11 (Toronto). All gates run in `scratch-proof-en-nl1/`; `TMPDIR=<scratch>/tmp`
  (nothing written to /tmp except the tool-output spill of one oversized grep, which was my own
  command output, not proof data).
- **Core integrity:** core-en SHAs measured before AND after (print `b484e007…`, web `7277e32a…`,
  text `e368828a…`) — unchanged throughout. Freeze baseline re-rendered core into a scratch
  build-copy only (`gates/freeze-final/`); no production file was overwritten. The web PDF was never
  re-rendered over the production copy — identity was verified from the delivered PDFs by pdftotext.
- **Superseded round:** the 09:47–09:57 PROOF-NOTE/GATE-LOG in this same directory belonged to the
  old build and were moved to `archive-oldbuild/` (with `gates/` → `archive-oldbuild/gates-oldbuild/`
  and `render/` → `archive-oldbuild/render-oldbuild/`). All gate products below are fresh, from the
  new build.

## File identity (verified before proofing; KIT §7 + `sha256sum`)

| file | size (B) | sha256 (full) |
|---|---|---|
| print `The-Lucerna-VOL4-en-nl.pdf` | 29,341,272 | `a5957d64e727662c0d4763596af517f0eae324471b93a4bd9dadb304c03bc136` |
| web `The-Lucerna-VOL4-en-nl.web.pdf` | 2,411,538 | `ee3d98baba20febe72c297ccb2591055991d4ed9b341b1429b6c7748b3371193` |
| `2026-w47-en-nl.text.md` | 53,568 | `baecaf6e92ff837857e3d6d7dd7ae28f2b1fbb15b8be78bec9428a83c13be459` |

All match the task values. Both PDFs 8 pages (`pdfinfo`, 1462.5 × 2025 pts).
Probe: `git hash-object` OK (`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`); probe file written in scratch.
Backup (old build, for the per-page compare): print `5b2a364b…` (29,340,703 B), web `f1d2b8f4…`,
text `3e21e424…` — matches the archived round's recorded SHAs.

## Gates

| gate | result |
|---|---|
| **Occlusion audit** | selftest OK (all 6 classes fired, clean controls silent); **0 flags** — PASS (`gates/occlusion.json`, `occlusion.log`) |
| **p8 extract (core + edition)** | edition 150 keys; noted set 60/150; noted set **identical to core's** — PASS (`p8-extract-core.json`, `p8-extract.json`) |
| **p8 compare** | **CLEAN**; missing=[]; extra=0; keydiff=[137,138,139,140,150] (reader-language translation keys + writing key — expected) (`p8-compare.json`) |
| **keycheck.py** | RC=0; REG 150, p8extract 150, exact match **149/150**; only mismatch n=150 (key 'Open vraag — punten in het schrijfblok; voorbeeldtekst in het kader op pagina 8' vs extracted 'Open vraag' — expected extractor truncation). `keycheck-150.json` written. Note: first run failed FileNotFoundError (script expects `p8extract.json`, gate writes `p8-extract.json`); fixed by copying the extract to the expected name and re-running clean — same filename quirk as the previous round. REG vs text.md appendix (separate scripted parse): **0 mismatches / 150**. (`keycheck.log`, `crosschecks.log`) |
| **freeze baseline** | **8/8 SVGs byte-identical**; core integrity unchanged — PASS (`freeze.log`, `gates/freeze-final/`) |
| **freeze direct sha** | **8/8 MATCH** — PASS (inline in `run-gates-stdout.log`) |
| **freeze diff** | added CJK = **9× U+3000 only** — PASS (`freeze-diff.json`, `freeze-diff.log`) |
| **print/web text diff** | 48,044 vs 48,044 chars; 2,481 distinct tokens each; token multiset diff **0/0** — PASS. Additionally: per-page pdftotext **byte-identical p1–p8**, and full pdftotext **byte-identical** (`run-gates-stdout.log`) |
| **check_s11.py (nl)** | RC=0, **ALL §1.1 / P8 checks PASS**; colour set core 19 = edition 19; badges A2 #5c6e30 / B1 #46581f / B2 #37402f; Q113–120 [A2] tag, "Levels: 145–149 [A2]", Q120 chip, H WRITING head all present; P8 min font **13.5pt** (≥11.25 target, ≥9.75 floor) (`check_s11.log`) |
| **creambox.py (all 8 SVGs, raw)** | Raw output shows negative clearances (e.g. −35.5/−37.0) — proven artifacts on strict re-measurement (see next row). |
| **creambox strict re-measurement (own content only)** | **PASS.** All 32 `#f0eee5` boxes have POSITIVE own-content clearance (**+5.0 to +92.4**); every raw negative is the next heading/line 35.5–37.0 px BELOW the box bottom, caught by the tool's +45 tolerance. Tightest box P2 y=1211, +5.0 ("Engels voor de redactie."). P7 TOOLBOX box y=651, bottom=1008.2, own last baseline 959.7, clearance +48.5. Visually confirmed on the P7 render. (`creambox-all.log`, `creambox-strict.log`) |
| **boxtitle sweep (source)** | 12/12 fit; tightest HOW LONG? +20.3, ODD SOCKS +20.6 — PASS (`boxtitle-src.log`) |
| **boxtitle sweep (SVG, hardened)** | 18/18 fit; overflows 0; SENATE IN NUMBERS +66.6, SATURDAY, NOV 21 +70.5 — PASS (`boxtitle-svg.log`) |
| **quote balance** | text.md “ 85 / ” 85 ✓; « 0 / » 0 ✓; straight `'` ×44 (apostrophes, per TM rule normalizing U+2019→`'`); U+2019 ×0. Per-SVG “/” balanced all 8 pages (P1 2/2, P2 1/1, P3 10/10, P4 3/3, P5 11/11, P6 2/2, P7 29/29, P8 26/26); «/» 0 on every page. (`crosschecks.log`) |
| **orphan punctuation sweep** | 0 orphan-start lines on all 8 SVGs and in text.md — PASS (`orphan-sweep.log`) |
| **banned words** | text.md: "W47"/"2026-W47" only on line 1 (file header, house convention); "cover"/"SOP"/"proofread" 0. SVG `<text>` elements: **0 banned tokens** on all 8 pages (raw-file SOP/W47 hits are inside base64 image blobs, not text). "VOL." 13× is the issue's own volume label in reader copy, not an internal token. (`crosschecks.log`) |
| **D5 fonts (count only, not judged)** | Newsreader 1023, Noto Sans CJK SC 663, Noto Serif CJK SC 27, DejaVu Sans 4, UnifrakturMaguntia 1 |
| **"next Sunday" freeze rule** | 0 hits in core-en, en-nl, `tools/tables.py` — **no applicable object**; not applied |
| **CREDITS.md** | all 8 images PD/CC0 with sources — capitol (Noclip), turkey (Audubon), tiger (Rousseau, *Surprised!* 1891), grace (W. G. Grace, Barraud), children (Bain/Lawrence 1912), voting (Zirkel CC0), johnson (**Samuel** Johnson 1772, Reynolds), readingroom (Highsmith). football1910.jpg NOT used — PASS |
| **visual inspection** | fresh pdftoppm renders (100 DPI) of all 8 print pages + web P1/P8, viewed in `render/`: no overflow/overlap/clipping; footers "Pagina N van 8" on all pages; P3 matching block, P7 toolbox/readers' corner, P8 answers block all as expected; web P1/P8 visually identical to print P1/P8 (see PROOF-NOTE.md observations) |
| **old-vs-new per-page compare** | pixel diff vs archived old build (threshold >30): P1 0.91%, P2 0.71%, **P3 0.00% (pixel-identical)**, P4 10.53%, P5 0.16%, P6 3.66%, P7 5.83%, P8 0.62%. All changes confined to the rebuild's touched regions; no wholesale change, no layout regression. (`oldnew-diff.log`, `render-old/`) |

## Answer-key verification (manual, 150/150 vs stems)

- All 150 keys checked stem-by-stem across registry.json, text.md appendix, P8 extracted keys, and
  the rendered P3/P8 SVGs where keys print. **Zero mismatches.**
- Carry-forward four-way check Q39/40: SVG defs (a=teaches/guides y=1078.7, b=chosen y=1149.7,
  c=lives with you y=1220.7, d=place where Games are fought y=1291.7) × registry (39=a, 40=d) ×
  text.md appendix (lines 1083/1085) × P8 extracted (39='a', 40='d') — all agree.
- Q46/52/55/125: registry = text.md = P8 extracted (A / hosted / won / A); Q46 stem and Q125 stem
  verified in the P4/P8 SVGs.
- Matching sets verified: P2 D (24 b, 25 c, 26 a, 27 d), P4 C (56 b, 57 c, 58 d, 59 a), P5 C
  (74 d, 75 a, 76 b, 77 c), P8 F (141 b, 142 c, 143 d, 144 a).
- P6 chart arithmetic 254+162+19=435 ✓. P7 golden sentences 8/8 verbatim ✓. MODEL text 82 words (80–100) ✓.
- Per-page counts 10/17/18/18/18/18/12/39 = 150; A2 62 / B1 66 / B2 22; numbering continuous 1–150.
- Weekdays for all named dates verified against `date` (America/Toronto); the only sweep "mismatches"
  were the 2025 date (Friday, November 21, 2025 — correctly a Friday).

## External-fact verification (web search, 2026-11-11)

Re-verified the rewritten Ashes article's new claims (the previous round's verified facts — midterms,
I'm a Celebrity, Anti-Bullying Week, Hunger Games, ATP Finals, Premier League, NFL Week 11,
World Children's Day, certification window — stand from that round and were not re-searched; the
unchanged article text carrying them was re-read in full):
- Perth 1st Test: 847 deliveries, shortest Ashes Test by balls bowled since 1888 (1888: 788 OT, 792
  Lord's); won in two days by 8 wickets (ICC via IANS; TNT Sports table).
- Series: first three Tests Perth/Brisbane/Adelaide, Ashes retained after the third; Melbourne 4th
  Test a two-day finish (852 balls), England won by 4 wickets, first England Test win in Australia
  since Jan 2011; Sydney 5th Test Australia won by 5 wickets (target 160, Jan 8, 2026); final 4–1
  (Sky Sports; cricket.com.au).
- Next Ashes in England: 18 Jun–2 Aug 2027, Trent Bridge opener (ECB schedule; Sky/ESPN/Radio Times).
  The paper claims only "June 2027".
- Cummins (back), Hazlewood (hamstring) out, Smith captained, Boland played, Doggett debuted in Perth
  — consistent with the series record as reported at the time (cricket.com.au squad lists include
  Doggett; Smith captained the 5th Test).
