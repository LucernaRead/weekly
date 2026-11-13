# D5-REPORT — ru-nl (2026-w47)

- Edition: `2026-w47-ru-nl` (target ru, reader nl, mode latin, `_D5_READER = "latin"`)
- Date: 2026-11-12 (UTC). Builder: W47 D5 ru-family worker.
- Mechanism: `scratch-d5-plan/mechanism/apply_variant.py --target ru --reader nl`
  (per PILOT-REPORT install method; CJK-DECISION.md §1–§3 + brief-d5-rebuild.md read).
- Build interpreter: `tools/venv/bin/python` throughout (Pillow 13.0.0). No system python3.
- Scratch: `hidden_files/w47/scratch-d5-rebuild-ru/scratch-fanout-ru/2026-w47-ru-nl/`
  (baseline/ = pre-fix svg + svglib.py + assets; backup/ = same copy for boxtitle).
- **Build location: IN PLACE in production** (`production/2026-w47/2026-w47-ru-nl/`).
  The only build-copy was the gates' `freeze/` rebuild output, deleted after
  verification. Production SHAs below were re-checked against the production
  files themselves (not a scratch copy).
- **Latin set complete:** ru-nl is the 7th and last Latin/Russian reader edition
  (de, en, fr, es, it, pt, nl). CJK readers (ja, ko, zh-tw) follow.

## Install

- Pre-fix `svglib.py` md5 `27f11789af7c828e47ca14eb00c1dded` (no fix2;
  unkerned run-measurement fix present) → post-install
  `2e87fef862607133a962c0ee981bd0a6` (fix2 added by the installer + D5).
- `assert_routing.py` (latin→news): all assertions pass, fix2 routing preserved.
- Baseline verified clean BEFORE install: pre-fix `run.py` rebuild reproduced the
  delivered 8 SVGs byte-identically (8/8 sha256 OK); pre-fix run.log 0 HEAD TOO WIDE,
  0 FLOW OVERFLOW, TOTAL 150.

## Census (pre → post)

| check | pre | post |
|---|---|---|
| D5 Latin in CJK Sans | 426 | **0** |
| D5 Cyrillic in CJK Sans | 0 | 0 (417 Noto Sans elements, unchanged) |
| curly quotes in CJK Sans | 0 | 0 (2 total, all Newsreader) |
| `census_quotes.py` defective | 0 | **0** |

## Builds

- `run.py` RC=0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE;
  `head_check.py` (run.log vs base-run.log) PASS 0 defects.
- `render.py` RC=0, first pass already normal (20,876,339 B);
  `webpdf.py` RC=0, 57,993 text bytes.
- text.md byte-identical: SHA-256
  `849015f1e920f15c8a0040157a477aab5efb75200f27ef8bcac43160e544e9b0` (64,013 B).

## New PDFs (verified in production)

- Print `Lucerna-VOL4-ru-nl.pdf`: `2bd4e0f2…` 21,289,183 B →
  **`b355efedd9fc5324832796572254cad36efa293b32d18dd612c1abf542b73efb` 20,876,339 B**
- Web `Lucerna-VOL4-ru-nl-web.pdf`: `390d4050…` 3,384,838 B →
  **`15cf757d84824dc05550c65d73170c3924ea01a5257d98dcb64c129816da2482` 3,329,813 B**
  (< 7 MB; print/web text layers byte-identical, 38,778 chars each)
- Production `svglib.py` contains `_D5_READER` (verified); KIT §5 synced to
  the SHAs above.

## Defects found by D5 (2, both fixed; text unchanged, font size only)

1. P6 `ЗА И ПРОТИВ　VOOR EN TEGEN` over right +3.4px (creambox + boxtitle agree).
   Fix: `content56.py:136` size 24→23pt (advance 403.2→386.4 vs box inner width
   400.5, ~14.1px margin).
2. P8 head/subtitle same-baseline collision (occlusion TEXTX, 12.8×19.0px;
   same class as ru-de/ru-pt P8 collisions — a REAL defect, unrelated to the
   voided PILOT-REPORT §5.4 P8 key-row false positive):
   P8 head `ОТВЕТЫ　ANTWOORDEN — PER PAGINA GERANGSCHIKT; ZOEK HET OPGAVENUMMER`
   ink overlaps the subtitle `Elk antwoord met een korte Nederlandse
   toelichting　✓ = modeltekst` (same baseline y=1302).
   Fix: `content8.py:116` size 25→24pt (advance 1159.5→1113.0; head ends
   ~33.7px before the subtitle starts; subtitle `content8.py:117` untouched).
   Full rebuild + full gates re-run after the fixes. Card crops of both fixed
   spots were read visually and confirmed clean (P8 head and subtitle with a
   clear gap).

NOT fixed (voided false positive): PILOT-REPORT §5.4 en-ru P8 key-row
"collisions" — voided by CJK-DECISION.md §2 (occlusion_audit.py measured
bare `Noto Sans` runs on the CJK SC face; U+00B7 full-width). No P8 key
row was touched. This edition's P8 key rows ran 0 flags with the fixed tool;
the flag above was the head/subtitle collision, a different element.

## Gates (post-fix rebuild, GATES_OVERALL_FAIL=0)

- D5 census PASS (0/0/0); quotes census 0; `head_check.py` PASS 0 defects.
- `run.py` TOTAL 150; `p8.py extract` 150/150; `p8.py compare` vs core-ru
  CLEAN (keydiff=[137, 138, 139, 140], expected reader-language keys).
- `freeze.py baseline` 8/8 byte-identical; freeze-diff vs pre-fix baseline:
  added CJK chars 0 (added Latin strings 150 = D5 run-splitting).
- `occlusion_audit.py` (fixed version) 0 flags; `boxtitle_check.py` 0 DEFECT
  (57 titles, 681 body lines); `d5_creambox_audit.py` PASS 0 defects
  (P8 lines 241→241, slack_footer 45.7→45.7px; ratios n=395, median 1.040,
  bold median 1.049).
- `spill_sweep.py` 0 SPILL; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR.
- Print/web text layers byte-identical (38,778 chars).
- P8 Morozko SKIPPED by the build's own condition — as before,
  by design, not a defect.

## KIT

- `WEEKLY-KIT.md` §7 appended with the D5 record; §5 PDF SHAs/sizes updated
  to the new values above. History preserved.
- Independent re-proof is the coordinator's job; this report records
  self-check gates only.

## Cleanup

- `freeze/` build-copy deleted after verification. Baseline + logs + JSONs kept.
- No commit, no push, no `lint --write`. No other family touched.
