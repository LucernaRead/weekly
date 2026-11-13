# GATE-LOG — 2026-W47 en-ru fix1 机械门记录

- 版：`2026-w47-en-ru`；解释器：`~/workspace/weekly-git/tools/venv/bin/python`（未用系统 python3）
- 日期：2026-11-11；命令均在版目录或仓根下执行；输出存本目录 `gates/`，运行日志存本目录
  （`run.log`、`render.log`、`gates.log`、`textmd.log`、`verify_fix.log`、`verify_3src.log`、
  `verify_fix2.log`）。
- 对照基准：proof1（`scratch-proof-en-ru1/GATE-LOG.md`）仅 D1 一条缺陷；本次全部门在重建后的
  新成品上重跑。D1 已修，观察项未动。

## 0. 开工探针（双通）

- `ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`
  → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，成功。
- 在 `hidden_files/w47/scratch-fix-en-ru2/` 真实写小文件成功（`probe.txt`）。

## 1. 身份核对（新成品）

- `sha256sum`：
  - `The-Lucerna-VOL4-en-ru.pdf`：29,241,529 字节，
    `fb849665c691cfb687f50d523a2f551ccc09cef806b942624e2f316395dab994`
  - `The-Lucerna-VOL4-en-ru.web.pdf`：2,452,560 字节，
    `5aac849d1b2d03bbf6838c4850a4c47d3df8fe5a01b726a306c8c1e3c5a28304`
  - `2026-w47-en-ru.text.md`：62,384 字节，
    `bf3a9127b62eaec3a2aa53359a28ffdd2aa8f503df53c24fcec7d77ea1ef6de7`
- `pdfinfo`：两 PDF 均为 8 页、1462.5 × 2025 pt。
- SVG 快照比对：修前 8 个 SVG 哈希存 `svg-before.sha256`；重建后仅 `p1-front.svg` 变化，
  其余 7 个 byte-identical。

## 2. run.py 重跑（真版）

- 命令：版目录内 `tools/venv/bin/python run.py`（日志 `run.log`）。
- 结果：**exit 0**；`OVERFLOW`/`TOO WIDE` 出现 0 次；`TOTAL exercises: 150`；
  `MODEL words: 82`。**PASS**

## 3. occlusion_audit.py

- 命令：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-en-ru/svg`
  （经 `gates.sh`）。
- 结果：`0 flags`，selftest OK。**PASS**

## 4. p8.py extract + compare

- 命令：`tools/venv/bin/python tools/p8.py extract --p8 <edition>/svg/p8-test.svg --total 150`
  及 `compare --core-p8 <core-en>/svg/p8-test.svg --edition-p8 <edition>/svg/p8-test.svg`
  （经 `gates.sh`）。
- 结果：extract noted 60/150（与 core 同集）；compare `status: CLEAN missing=[] extra_count=0
  keydiff=[137, 138, 139, 140, 150]`（预期：读者语翻译键 + 写作题短标签）。**PASS**

## 5. freeze

### 5a. baseline

- 命令：`tools/venv/bin/python tools/freeze.py baseline --build <core-en> --core-svg
  <core-en>/svg --out <scratch-fanout-en/ru>/freeze-final`（经 `gates.sh`）。
- 结果：**8/8 SVGs byte-identical**（repointed files: none）；core integrity：shipped core
  SVGs unchanged。direct sha256（baseline 重渲染 vs  shipped core）8/8。**PASS**

### 5b. freeze.py diff（core vs edition，只读）

- 命令：`tools/venv/bin/python tools/freeze.py diff --core-svg <core-en>/svg --edition-svg
  <edition>/svg`（经 `gates.sh`）。
- 结果：TOTAL added CJK characters: 9，全部为 U+3000；无英文正文改动。**PASS**

## 6. print/web 文字层一致

- `pdftotext` 两版各 47,649 字符（修前 47,655，−6 = 删 "цифры " 恰 6 字符）；
  token 多重集差 0/0；逐页 byte-identical 8/8
  （5556/6621/5756/6182/5175/6110/7379/11950 B）。
- web PDF 2,452,560 字节 < 7 MB。**PASS**

## 7. D1 三重实测（`verify_fix.py`）

- (a) SVG advance：339.4 px，止于 1800.9，框右缘 1862.0，余量 **+61.1 px**（修前 −8.5）。
- (b) 印 PDF 真墨：span x[1096.1, 1351.3] pt，框右 1396.5 pt，余量 **+45.2 pt**（修前 +7.0 溢出）。
- (c) 150 dpi 渲染像素：最右墨点 1349.3 pt，余量 **+47.2 pt**（修前 +5.1 溢出）；
  cream→white 交界 1396.3 pt。目视裁图 `render/p1-searches-gloss-new.png`。**全部 PASS**

## 8. 其他量化核查

- P8 最小字号：print PDF span 最小 **10.12 pt** ≥ 9.75 pt（P1 最小 11.62 pt）。
- creambox（canonical `hidden_files/w47/tools/creambox.py`）：RC=0，**0 OVERFLOW**。
- h-containment（proof 的 `gates/h-containment.py`，新印 PDF）：**H-SPILL total: 0**。
- boxtitle 源码 sweep（`sweep_titles.py ru`）：12/12 fit，0 over budget。
- boxtitle SVG sweep（`sweep_svg_titles.py ru`）：18/18，overflows 0。
- check_s11（`check_s11.py ru`）：ALL §1.1/P8 CHECKS PASS。
- verify_ed（`verify_ed.py ru`）：VERIFY ALL PASS。
- keycheck（proof 的 `keycheck.py`，重指向本目录 `gates/p8-extract.json`）：
  registry-vs-P8extract exact **149/150**，exc=[150]，mismatch=[]；Q38–41 b/a/d/c；
  Q125 A，Q46 A，Q52 hosted，Q55 won；Q82/83/84 B C A；noted set == core noted True。
  registry-keys-vs-core 144/150：除 5 个读者语键外仅 Q73 不同（`speak` vs core `up`——
  见 FIX-LOG §8，**未修**，交协调员）。
- 150 题三源逐题手验（registry / P8 extract / text.md 答案）：150/150 exact，0 差异
  （`verify_3src.log`；初版脚本因答案区间空行与注中括号切错曾误报 10 处，已修正重跑通过，
  过程见 `verify_fix.log` 与 `verify_fix2.log`）。
- 孤儿标点：视觉行定义（按 y 分组整行）全版扫 **0**，core-en 对照亦 0（`verify_fix2.log`）。
- 引号：text.md U+201C=81 / U+201D=81，SVG 82/82，U+2019=0，U+2018=0；禁词 0。
- D5 字体（只记录）：1798 个 `<text>`，26 种字号，与 proof1 记录逐项相同。

## 门总汇

| 门 | 结果 |
|---|---|
| run.py | exit 0，TOTAL 150，MODEL 82，零溢出 |
| occlusion | 0 flags |
| p8 extract | 150/150，noted 60/150 = core |
| p8 compare | CLEAN，keydiff 仅 137–140、150（预期） |
| freeze baseline | 8/8 byte-identical；direct sha 8/8 |
| freeze diff | 新增 CJK 仅 9 个 U+3000 |
| print/web 文字层 | 各 47,649 字符，token 差 0/0，逐页 byte-identical 8/8 |
| D1 三重实测 | SVG +61.1 px；PDF 真墨 +45.2 pt；渲染像素 +47.2 pt |
| P8 最小字号 | 10.12 pt ≥ 9.75 pt |
| creambox | 0 OVERFLOW |
| h-containment | H-SPILL 0 |
| boxtitle 源码 | 12/12 fit |
| boxtitle SVG | 18/18 fit |
| check_s11 | ALL PASS |
| verify_ed | ALL PASS |
| keycheck | 149/150，exc=[150] |
| 150 题三源 | 150/150 exact |
| 孤儿标点 | 0 |
| 引号/禁词 | 201C=201D，2019=0，禁词 0 |
| D5 字体 | 只记录（1798/26，与 proof1 相同） |

机械门全部通过；D1 已修；Q73 见 FIX-LOG §8（未修，待定）。
