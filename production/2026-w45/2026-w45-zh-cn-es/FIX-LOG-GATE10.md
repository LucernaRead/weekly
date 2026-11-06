# Gate 10 fix round — W45 zh-CN × ES (fix, NOT finalization)

## Pre-fix baselines (recorded BEFORE any re-render)

Toolchain:
python 3.12.3
PIL 13.0.0

Interpreter: /home/hatch/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python

### Delivered SVGs (full SHA-256)
71d4b608add7f84e0e92bad531409da28d0cb288fee2a0396f0feb1f60e91b52  svg/p1-touiban.svg
8d78f0bb0fe50aa15041bd9012f65215d6cb40e364d691ae17c69f85c2f30c33  svg/p2-shenghuo.svg
091af691031a38e7610cbb34de8dc2da70dd67910b3aad372802e7117cefb912  svg/p3-wenhua.svg
f316e145cefc692ebd85b23c406a93a58309f9e915318d9f823e94521c44a604  svg/p4-tiyu.svg
203d8eae79a87f32d963fdc17040ee538c27f427161f0a40c2af8c0fb494aeef  svg/p5-qingnian.svg
d26244db12294e27a32454b525f7f7cdbda5d055738dade458055b58a681ed73  svg/p6-shendu.svg
1fd7c59999288c37abd0d70ffea0390142bfc5c2486e1866c352697f6ac41394  svg/p7-ciyu.svg
d6c9bb95b56f21b6786cbe64332e63de0ef617ba6b66033e5a4564ab7d887045  svg/p8-ceyan.svg

### Delivered cards (full SHA-256)
44df3074de8fba1f68325ca467a440b2a7ef1da5094f8aaece838c3c1f3b9122  cards/p1-touiban.png
5c4e8b73f90613ce8eaac3b812da0c630bbdb556b83730bd268ecea05ed6bba8  cards/p2-shenghuo.png
494c447158acd036cbe053f139c75af55bb882648d5aa94d41ab7bb3324340d4  cards/p3-wenhua.png
6326f43b5a54e869848410a05cc6cfe6117512148d03d53f1e977afa78c273a0  cards/p4-tiyu.png
094f7ad601fe03b71e0872678391019a0dcd1d4d441ab65b938828b4f76da5b6  cards/p5-qingnian.png
84a5c32bb87dcc8c3c718d51389a0f14fe799bb70c9057b9b36a5203f108061d  cards/p6-shendu.png
ec4d9604b2f1cbfa2290348314242fb50d56b3c014aa6f97d45e2839fd71cb99  cards/p7-ciyu.png
605e5da0001fb34424364b4c0d3a8204ea2ec3e0ceeb24a98ed4d953e6aa1366  cards/p8-ceyan.png

### Delivered PDFs (size + full SHA-256)
-rw-rw---- 1 root nogroup  3242033 Oct 28 07:19 Lucerna-VOL2-ES-web.pdf
-rw-rw---- 1 root nogroup 50133157 Oct 28 07:18 Lucerna-VOL2-ES.pdf
e53d52040d1990edbb3c89aa6a3e0fc29d83c9325de75e3f1f65aed911543c46  Lucerna-VOL2-ES.pdf
0ee7547e5d24a835cb349a4037fa94adf279c3350b73a26dacb414609baa573c  Lucerna-VOL2-ES-web.pdf

## The 21 folded edits (all in the build dir's transform.py — no other script)

Source of truth: proof report `hidden_files/w45/zh-cn-es-proof/REPORT.md`
(B1) + `work/manual-edits-diff.txt`. Direction verified against the
delivered build files: each transform `new` string below replaces the
pre-fix transform output with the delivered string. 20 transform
replacements cover 21 diff lines (the content12 降价 replacement is
replace-all and covers both its exercise and quiz lines). All are exact
unique literals with the runner's per-replacement count assertion
(tools README #17); no AST byte-offset splicing, no repr literals
in f-strings.

1. content56 head: `Cuentas de cestas` → `Cuentas` (P6 head shortening).
2. content12 预售: `Las preventas de Taobao y Tmall empezaron el 15 de octubre.` → `Las preventas de Taobao y Tmall: 15 de octubre.`
3. content12 一: `El Comienzo del Invierno es el primer término solar del invierno.` → `El Comienzo del Invierno es el primer término del invierno.` (the P1 glossline keeps `solar` — different replacement, untouched).
4. content12 降价 (×2 lines): `Este año muchos productos bajan de precio directamente.` → `Este año muchos productos bajan directamente.`
5. content12 spot: `Las ventas en stock de Taobao y Tmall empezaron el 20 de octubre.` → `Ventas en stock de Taobao y Tmall: 20 de octubre.`
6. content12 WeChat: `El evento de la tienda de WeChat dura hasta el 15 de noviembre.` → `El evento de la tienda WeChat termina el 15 de noviembre.`
7. content34 final: `La final empieza a las 03:00 del 15 de noviembre, hora de Pekín.` → `La final es a las 03:00 del 15 de noviembre, hora de Pekín.`
8. content34 内战: `nèizhàn — AL perdió el partido entre equipos de la LPL contra TES.` → `nèizhàn — AL perdió ante TES en el duelo de la LPL.`
9. content34 淘汰: `táotài — tres victorias llevan a un equipo a las eliminatorias.` → `táotài — tres victorias clasifican a las eliminatorias.`
10. content56 estreno: `La nueva película se estrena el 7 de noviembre, Comienzo del Invierno.` → `La nueva película se estrena en lìdōng, 7 de noviembre.` (pinyin rewording).
11. content56 数字: `shùzì — los personajes de la película son imágenes digitales.` → `shùzì — los personajes son imágenes digitales.`
12. content56 立冬: `lìdōng — la nueva película se estrena en el Comienzo del Invierno.` → `lìdōng — estreno de la nueva película.` (pinyin rewording).
13. content56 2: `El 24 y 25 de octubre, cada sesión tuvo una media de 2 espectadores.` → `El 24 y 25 de octubre: media de 2 espectadores por sesión.`
14. content7 凌晨: `凌晨 língchén — las horas pequeñas después de medianoche.` → `凌晨 língchén — las primeras horas tras medianoche.` (the `Dos palabras más` glossline keeps the old wording — different replacement, untouched).
15. content7 最低价: `「最低价」 es una afirmación publicitaria, no un dato medido.` → `「最低价」 es publicidad, no un dato medido.`
16. content7 frame (NEW replacement, was never in transform.py): old `「先看评价,再下单。」(First check the reviews, then order.) The frame 先…再… gives the order of actions. More: 「先看天气,再出门。」` → new `「先看评价,再下单。」(Primero mira las reseñas y luego pide.) El marco 先…再… da el orden de las acciones. Más: 「先看天气,再出门。」` (old string verified to occur exactly 1× in the core's content7.py line 80).
17. content8 loop final: same final-note shortening as (7), in the content8 shared-notes loop.
18. content8 loop shùzì (translation completion): old string CORRECTED to include "AI" — `shùzì — the AI film's characters are digital images.` (pre-fix old string omitted "AI" and missed) → new `shùzì — personajes digitales en la película con IA.` The content56 non-AI pair (11) is unchanged and still matches the core's content56 note.
19. content8 stock: `La mercancía en stock se envía de inmediato, sin espera de preventa.` → `La mercancía en stock se envía al momento, sin preventa.`
20. content8 rule: `La regla de la página 6: primero los datos, el anuncio al final.` → `Página 6: primero los datos, el anuncio al final.`

Script path: `hidden_files/weekly-report-w45-zh-cn-es-build/transform.py`
(edited in place; `py_compile` OK). Fix scratch (Gate 10 repro, logs,
pre-fix backup): `hidden_files/w45/zh-cn-es-fix/work/`.

## Post-fix verification (re-render + Gate 10 re-run + mechanical gates)

- **In-place re-render:** single one-process driver in the edition build
  dir (`tools/venv/bin/python run.py`, content12 → 34 → 56 → 7 → 8),
  log `build-es-fix.log`. Exit 0, zero `HEAD TOO WIDE` /
  `FLOW OVERFLOW` warnings, registry TOTAL 150 (A2 56 / B1 69 / B2 25;
  pages 10/18/18/18/18/18/12/38; types 完成句子 68 / 单选 50 / 词汇配对 20 /
  完形单选 11 / 写作 1; writing model 172 chars).
- **Post-fix byte-identity table (delivered files, pre-fix → post-fix):**
  all 18 files byte-identical (full SHA-256 in the pre-fix section above):

  | File | Pre-fix SHA-256 (12-hex) | Post-fix |
  |---|---|---|
  | svg/p1-touiban.svg | 71d4b608add7 | identical |
  | svg/p2-shenghuo.svg | 8d78f0bb0fe50 | identical |
  | svg/p3-wenhua.svg | 091af691031a | identical |
  | svg/p4-tiyu.svg | f316e145cefc | identical |
  | svg/p5-qingnian.svg | 203d8eae79a8 | identical |
  | svg/p6-shendu.svg | d26244db1229 | identical |
  | svg/p7-ciyu.svg | 1fd7c5999928 | identical |
  | svg/p8-ceyan.svg | d6c9bb95b56f | identical |
  | cards/*.png (8) | see pre-fix section | all identical |
  | Lucerna-VOL2-ES.pdf (50,133,157 B) | e53d52040d19… (full pin unchanged) | identical, size unchanged |
  | Lucerna-VOL2-ES-web.pdf (3,242,033 B) | 0ee7547e5d24… (full pin unchanged) | identical, size unchanged |

  Cards/PDFs were verified by hash, NOT regenerated: re-running
  render.py would rewrite the web PDF's wall-clock timestamps and change
  its SHA (proof Gate 9 documented variance). SVGs are byte-identical,
  so card/PDF inputs are unchanged.
- **Gate 10 re-run (transform alone, fresh core copy):** scratch
  `hidden_files/w45/zh-cn-es-fix/work/gate10/` (core build copy +
  fixed transform.py + ES run.py; OUT repointed to gate10-out; driver
  in one process). Transform: **317/320 replacements, exit 1** — the 3
  remaining misses are the proof-adjudicated benign byline misses
  (content12 B1, content56 A2, content34 A2→B1; old strings absent
  from those files, output unaffected). The fixed shùzì-AI pair hit
  x1, the new P7 frame pair hit x1, the P6 head pair hit x1.
  Driver: exit 0, **zero `HEAD TOO WIDE` / `FLOW OVERFLOW` warnings**,
  P7 teaser ends 2525.1, P7 col3 ends 1679.1, P8 keys end y=2411
  (delivered values; repro pre-fix ended 2585).
  **SVG comparison: 8/8 byte-identical to the delivered SVGs.**
  Transform-output content files are byte-identical to the delivered
  ES build content files except the repointed OUT line; bslib4.py
  identical. Gate 10 criterion (8/8 + zero warnings) is met.
- **Mechanical gates re-run on the re-render:**
  - `tools/occlusion_audit.py --selftest` → OK (all 6 planted classes
    fire exactly once); edition audit → **0 flags**; with
    `--core …/weekly-report-w45-zhcn-core/svg` → core 0 flags,
    **NEW vs core: 0**.
  - `tools/p8.py compare --target zh-cn` → **CLEAN: core 150 noted,
    edition 150 noted, missing=[] extra_count=0, uncertain=[],
    keydiff=[]**.
  - Gloss counts: source content12 [4,4,4], content34 [3,3,3],
    content56 [3,3,3,3], total 33, equal core vs edition; rendered
    `Nota — ` prefix counts per page equal core `Notes｜` counts
    (1/2/2/1/2/2/0/0).
  - Registry 150, 0 warnings (both driver runs above).
- **Unchanged by this fix round:** paper content, furniture,
  `ABSTRACT.txt` (SHA-256 unchanged vs pre-fix backup), and
  `tools/tables.json` (not edited; the all-caps separator discrepancy
  vs the shipped `— Página N —` form remains recorded for the parent
  line, per the proof). No `weekly-git`, insert.py, Discord, main-chat
  delivery, or cron activity. No subagent spawned.
- **Status:** FIX DONE, NOT finalized. A full independent reproof
  follows per SOP §8.4; this record does not declare finalization.
