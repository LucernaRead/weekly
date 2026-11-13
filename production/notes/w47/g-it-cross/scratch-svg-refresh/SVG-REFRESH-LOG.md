# SVG-REFRESH-LOG — W47 production svg/ refresh (13 synced editions)

Date: 2026-11-12 ~02:00–02:15 UTC. Worker: svg-refresh.
Scratch dir (this log's home):
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-svg-refresh/`
Production dir: `~/workspace/weekly-git/production/2026-w47/` (main only, no branch).

## 0. Method

Per edition, in order:
1. **A — print-PDF anchor:** re-hashed the synced production print PDF and compared it to the
   build-1 print SHA recorded in the R1/R2/R3 REBUILD-LOGs. All 13 MATCH — the synced PDFs
   are the build-1 outputs, so the build-1 SVGs are the SVGs that produced them.
2. **B — before:** hashed the 8 production `svg/` files (stale pre-`_run_w` in all 13: 0/8
   matched build-1, as expected).
3. **C — copy:** copied the 8 build-1 SVGs over the production `svg/` dir (overwrite).
4. **D — after:** re-hashed production `svg/`; must equal build-1 8/8.
5. **E — freeze:** `tools/freeze.py baseline --build <prod dir> --core-svg <prod dir>/svg`
   (runs `run.py` only, no `render.py`), against the refreshed `svg/`. Freeze build-copies
   were deleted immediately after each edition (logs kept).

Build-1 SVG sources:
- R1 (ru-de, ru-en, ru-fr, ru-es, core-ru): `scratch-ru-rerun-R1/<ed>-1/build-copy/svg/`
- R2 (ru-it, ru-pt, ru-nl, ru-ja, ru-zh-tw): `scratch-ru-rerun-R2/<ed>/build1/build-copy/svg/`
- R3 (nl-ru, pt-ru, zh-cn-ru): `scratch-runw-rerun-R3/<ed>/build-copy/svg/`
ru-ko NOT touched (its port+rebuild+sync worker owns it). No PDF, text.md, KIT,
source `.py`, or any other edition touched. No commit / push / lint.

## 1. Results (all 13 GREEN)

| Edition | Print-PDF anchor | Before (prod svg vs build1) | Copy after | Freeze baseline vs refreshed svg/ | rc |
|---|---|---|---|---|---|
| ru-de | MATCH | 0/8 | 8/8 | 8/8 | 0 |
| ru-en | MATCH | 0/8 | 8/8 | 8/8 | 0 |
| ru-fr | MATCH | 0/8 | 8/8 | 8/8 | 0 |
| ru-es | MATCH | 0/8 | 8/8 | 8/8 | 0 |
| core-ru | MATCH | 0/8 | 8/8 | 8/8 | 0 |
| ru-it | MATCH | 0/8 | 8/8 | 8/8 | 0 |
| ru-pt | MATCH | 0/8 | 8/8 | 8/8 | 0 |
| ru-nl | MATCH | 0/8 | 8/8 | 8/8 | 0 |
| ru-ja | MATCH | 0/8 | 8/8 | 8/8 | 0 |
| ru-zh-tw | MATCH | 0/8 | 8/8 | 8/8 | 0 |
| nl-ru | MATCH | 0/8 | 8/8 | 8/8 | 0 |
| pt-ru | MATCH | 0/8 | 8/8 | 8/8 | 0 |
| zh-cn-ru | MATCH | 0/8 | 8/8 | 8/8 | 0 |

## 2. Before/after SVG SHA-256 (first 12 hex chars; full hashes in `refresh-results.json`)

### ru-de

| Page | BEFORE (stale pre-_run_w) | AFTER = build-1 | changed |
|---|---|---|---|
| p1-pervaya.svg | `c496022d6ea8` | `33e29cc9d29e` | yes |
| p2-zhizn.svg | `4590b41d027c` | `f7264097a2f5` | yes |
| p3-kultura.svg | `f1e9f5e36f55` | `01dafb04be8a` | yes |
| p4-sport.svg | `db9391e4c21f` | `31673a19baf0` | yes |
| p5-molodezh.svg | `192aa2e13259` | `035989fa870c` | yes |
| p6-razbor.svg | `14ae25471eaf` | `57d7f4d9e465` | yes |
| p7-yazyk.svg | `729792f0aa71` | `ea864aead22a` | yes |
| p8-test.svg | `269905be70aa` | `fb2b9b722445` | yes |

### ru-en

| Page | BEFORE (stale pre-_run_w) | AFTER = build-1 | changed |
|---|---|---|---|
| p1-pervaya.svg | `5f531b863310` | `354e6273be89` | yes |
| p2-zhizn.svg | `d632cba2af94` | `72cb209cd9e2` | yes |
| p3-kultura.svg | `00ff048bbe7c` | `1e93d8e788e3` | yes |
| p4-sport.svg | `f9abc1a5dcf0` | `7207baaefa36` | yes |
| p5-molodezh.svg | `3dd2f2b38c9a` | `b52522108bc1` | yes |
| p6-razbor.svg | `0794684a414d` | `3b7ff924d182` | yes |
| p7-yazyk.svg | `83d715a15a78` | `cc73aa112abb` | yes |
| p8-test.svg | `8bb21fd23e69` | `1718f7c2002a` | yes |

### ru-fr

| Page | BEFORE (stale pre-_run_w) | AFTER = build-1 | changed |
|---|---|---|---|
| p1-pervaya.svg | `0fc838b4ec3a` | `72b7eeda7e7c` | yes |
| p2-zhizn.svg | `591c647fe2a8` | `a0204993ff48` | yes |
| p3-kultura.svg | `0ce42ebe1193` | `bf2b14031b00` | yes |
| p4-sport.svg | `aac7c190b12d` | `0167d4e8cb8d` | yes |
| p5-molodezh.svg | `b681cfbf578f` | `d6bd521aaafa` | yes |
| p6-razbor.svg | `d717bddb1df4` | `3c257bc9d992` | yes |
| p7-yazyk.svg | `da6994a4647f` | `ab183870f1a4` | yes |
| p8-test.svg | `ff1d226901d0` | `a3cd256448c2` | yes |

### ru-es

| Page | BEFORE (stale pre-_run_w) | AFTER = build-1 | changed |
|---|---|---|---|
| p1-pervaya.svg | `f608059f0dc0` | `833fe6d09610` | yes |
| p2-zhizn.svg | `a8375463cf76` | `0dba462cd494` | yes |
| p3-kultura.svg | `acc55165f291` | `39a522f6f836` | yes |
| p4-sport.svg | `9bfded084885` | `c0535483ac32` | yes |
| p5-molodezh.svg | `49e94080ec29` | `147573a263d0` | yes |
| p6-razbor.svg | `760bd64b29fd` | `0a62fde37163` | yes |
| p7-yazyk.svg | `64bda8c8f353` | `5952d9aace69` | yes |
| p8-test.svg | `8da06fe89432` | `7cd5622235d9` | yes |

### core-ru

| Page | BEFORE (stale pre-_run_w) | AFTER = build-1 | changed |
|---|---|---|---|
| p1-pervaya.svg | `409d5c2d5f79` | `52b6bf0938ce` | yes |
| p2-zhizn.svg | `370a2470f20d` | `bd4862d6c3fd` | yes |
| p3-kultura.svg | `9c0de9072ddf` | `4c34c6173c3f` | yes |
| p4-sport.svg | `3f330829f0f9` | `426ddcf33777` | yes |
| p5-molodezh.svg | `2441db435350` | `dc394782372a` | yes |
| p6-razbor.svg | `c6f816791724` | `4b64984b4326` | yes |
| p7-yazyk.svg | `6679e1aa8369` | `c48ac1e5a947` | yes |
| p8-test.svg | `6ad2c7f1b434` | `c48050c24583` | yes |

### ru-it

| Page | BEFORE (stale pre-_run_w) | AFTER = build-1 | changed |
|---|---|---|---|
| p1-pervaya.svg | `fdaf10db3f5d` | `26c2bdd36f2b` | yes |
| p2-zhizn.svg | `5ba325695470` | `e5dcc74a9ee7` | yes |
| p3-kultura.svg | `533ca6240a6d` | `228747f0edd1` | yes |
| p4-sport.svg | `059d90540af9` | `ec11794106d9` | yes |
| p5-molodezh.svg | `9f5c73428031` | `476daea37247` | yes |
| p6-razbor.svg | `b3d7a1d995cb` | `7671063606d4` | yes |
| p7-yazyk.svg | `c29e36046487` | `612e5a81f6b4` | yes |
| p8-test.svg | `685746183fbc` | `999124059b34` | yes |

### ru-pt

| Page | BEFORE (stale pre-_run_w) | AFTER = build-1 | changed |
|---|---|---|---|
| p1-pervaya.svg | `9c7a128b5574` | `d89044fe9eb3` | yes |
| p2-zhizn.svg | `a8757d6cdb7c` | `8e9434e66eab` | yes |
| p3-kultura.svg | `5183be0d58cc` | `b1c902152e99` | yes |
| p4-sport.svg | `de015f4c1d97` | `5b337a1d63a1` | yes |
| p5-molodezh.svg | `abeefda77383` | `3621e729bb67` | yes |
| p6-razbor.svg | `fd9e375284d0` | `8b7f8be6784f` | yes |
| p7-yazyk.svg | `dd83d6cf3909` | `e6b0861b6b29` | yes |
| p8-test.svg | `64c80d824e3c` | `efe2de3d7b57` | yes |

### ru-nl

| Page | BEFORE (stale pre-_run_w) | AFTER = build-1 | changed |
|---|---|---|---|
| p1-pervaya.svg | `c4f4f0cda6cf` | `c758dde697a8` | yes |
| p2-zhizn.svg | `870e5c5b6811` | `8ad43c45e0f1` | yes |
| p3-kultura.svg | `af3b4ae2ed02` | `20ea7db37f4c` | yes |
| p4-sport.svg | `67383c6d2292` | `b43852085c5d` | yes |
| p5-molodezh.svg | `7537c66f4307` | `c08350f36ac6` | yes |
| p6-razbor.svg | `df9c33cc3e4d` | `05c9930eaf1d` | yes |
| p7-yazyk.svg | `80faea519a35` | `5493710d68d0` | yes |
| p8-test.svg | `c07cb075072d` | `5f3801758a58` | yes |

### ru-ja

| Page | BEFORE (stale pre-_run_w) | AFTER = build-1 | changed |
|---|---|---|---|
| p1-pervaya.svg | `d36cb640dc52` | `e39f7ae6d3a3` | yes |
| p2-zhizn.svg | `a44343f604e6` | `81ddbe1385bb` | yes |
| p3-kultura.svg | `f9bfa1ad33ef` | `0c728e3f031e` | yes |
| p4-sport.svg | `a9922c229b7d` | `5ec32066ef94` | yes |
| p5-molodezh.svg | `88eca8d6dff7` | `1eeeb0065052` | yes |
| p6-razbor.svg | `d9c308195b5c` | `6c32c318ba32` | yes |
| p7-yazyk.svg | `a425edb2845c` | `e07ec1b79dc3` | yes |
| p8-test.svg | `b5a1d06e129b` | `6fd0611b3895` | yes |

### ru-zh-tw

| Page | BEFORE (stale pre-_run_w) | AFTER = build-1 | changed |
|---|---|---|---|
| p1-pervaya.svg | `828a6c0ef57f` | `498875af6221` | yes |
| p2-zhizn.svg | `fa4eb6ad7a9b` | `d5f3cc1cd1bc` | yes |
| p3-kultura.svg | `09389ff6f123` | `f1fddb06e7d5` | yes |
| p4-sport.svg | `408165ff7982` | `30c23353568c` | yes |
| p5-molodezh.svg | `02c8ca94f522` | `c15a9c88a29d` | yes |
| p6-razbor.svg | `fe6276d22c64` | `ef634eb4df2d` | yes |
| p7-yazyk.svg | `6e46558ba2d7` | `be62c01014df` | yes |
| p8-test.svg | `d1c10d0b911f` | `fdab2d297c1e` | yes |

### nl-ru

| Page | BEFORE (stale pre-_run_w) | AFTER = build-1 | changed |
|---|---|---|---|
| p1-voorpagina.svg | `1d10b5d97d75` | `0e5a82e2a123` | yes |
| p2-leven.svg | `b02f479f1210` | `16aca666b0fe` | yes |
| p3-cultuur.svg | `4498ec96884b` | `1903259fbf8e` | yes |
| p4-sport.svg | `005fe8699188` | `79e8a6996ab0` | yes |
| p5-jongeren.svg | `c417fd0cb9cb` | `fab8dff76c7e` | yes |
| p6-verdieping.svg | `f258d5e5f3b5` | `d0c6f8642646` | yes |
| p7-taal.svg | `de0d5e09df01` | `5e8b98cc0bf9` | yes |
| p8-toets.svg | `596058af544b` | `312cf451409c` | yes |

### pt-ru

| Page | BEFORE (stale pre-_run_w) | AFTER = build-1 | changed |
|---|---|---|---|
| p1-capa.svg | `02345e2b44d3` | `0bf159ec109b` | yes |
| p2-vida.svg | `7cfd88b17a2b` | `a320b79fa655` | yes |
| p3-cultura.svg | `f1c3c019391a` | `7153a3db2883` | yes |
| p4-esporte.svg | `0fa61e1c69a3` | `6ff5d89d74f7` | yes |
| p5-jovens.svg | `e60ee014b591` | `61128d1d96c1` | yes |
| p6-aprofundamento.svg | `9ec4ed9d15e8` | `a41624c15350` | yes |
| p7-lingua.svg | `42da81ba0153` | `21e8dc86a368` | yes |
| p8-avaliacao.svg | `ce6c666e5354` | `a36ef7593414` | yes |

### zh-cn-ru

| Page | BEFORE (stale pre-_run_w) | AFTER = build-1 | changed |
|---|---|---|---|
| p1-touiban.svg | `fbe71fe70b52` | `0f06f1ec3044` | yes |
| p2-shenghuo.svg | `c3bc1da37dbc` | `b9ec226d97ae` | yes |
| p3-wenhua.svg | `20401b96bc86` | `51ada6c1ac33` | yes |
| p4-tiyu.svg | `79ae512ab525` | `6446f0e24597` | yes |
| p5-qingnian.svg | `d64ae10bdc1c` | `de8b57339916` | yes |
| p6-shendu.svg | `db428e2110d7` | `536ede66a781` | yes |
| p7-ciyu.svg | `7e5aeeb2c482` | `8494ead2df6f` | yes |
| p8-ceyan.svg | `6a4af6f6ea5f` | `d91273691dcb` | yes |

## 3. Disk

- Before: used 99G (stop line 100G; checked again at dispatch: 99G).
- After: used 99G. Freeze build-copies deleted per edition; net change 0G.

## 4. Files in this scratch dir

- `SVG-REFRESH-LOG.md` (this file), `refresh.py` (driver), `refresh-run.log` (driver stdout),
  `refresh-results.json` (machine-readable: per-edition anchor/copy/freeze + full before/after SHA tables),
  `freeze-<ed>.log` (per-edition freeze tool output, 13 files; the `freeze-<ed>/` out dirs hold
  only the tool's `svg/` placeholder — their `build-copy/` dirs were deleted after each run).

## 5. Consequence

The freeze baseline now reads **8/8 (rc=0)** for all 13 editions against the refreshed
production `svg/` dirs. Future freeze runs will compare against the SVGs that actually
produced the shipped PDFs instead of the stale pre-`_run_w` artifacts.
