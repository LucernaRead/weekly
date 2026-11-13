# GATE-LOG — 2026-W47 zh-cn-fr fix1（修后全部门禁逐项实测值）

- 版：`production/2026-w47/2026-w47-zh-cn-fr/`；核心：`production/2026-w47/core-zh-cn/`
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）
- 日志与中间件均在本 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-cn-fr1/`
- 修前三 SHA 与任务书一致（见 FIX-LOG §0）；修后三 SHA 见 FIX-LOG §3，收工重验全串一致。

## 1. run.py（`run-fix1.log`）

- 命令：`tools/venv/bin/python run.py`（cwd=版目录；日志重定向用 scratch 内绝对路径）
- rc=0，`TOTAL 150`，by level `{'A2': 56, 'B1': 69, 'B2': 25}`，by page `{1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`，by type `{'完成句子': 68, '单选': 50, '词汇配对': 20, '完形单选': 11, '写作': 1}`；`FLOW OVERFLOW` / `HEAD TOO WIDE` 计数 0。
- 关键行：`P7 teaser ends 2588.78`；`flow[P8-keys] ended col 3/3 y=2537 (bottom 2560)`；`P8 keys flow ends col/y: 3 2537.2`（均与修前一致）。

## 2. gates-zhcn.py 11/11（`gates-fix1.log` / `gates-fr.json`），rc=0，OVERALL: ALL PASS

| 门 | 结果 |
|---|---|
| occlusion | PASS：rc=0，flags=0，selftest OK |
| img_overlap | PASS：hits=0 |
| p8_extract | PASS：rc=0，noted=150/150 |
| p8_compare | PASS：rc=0，verdict=CLEAN，keydiffs=0 |
| freeze_sha256 | PASS：run rc=0，match=8/8（版内二次构建与交付 SVG 逐字节一致） |
| print_web_text | PASS：pages 8/8，posdiff=0，msdiff=0；逐页 P1 394/394、P2 374/374、P3 290/290、P4 364/364、P5 292/292、P6 365/365、P7 589/589、P8 1897/1897（token 数） |
| pdftotext_nonempty | PASS：print=45,540 B，web=45,540 B，web_size=2,663,732（< 7 MB） |
| p8_fontsize | PASS：answer-zone min=9.98 pt，median=9.98 pt，spans=368（≥ 9.75；与修前 9.975 同值） |
| p8_chips | PASS：core={'A2': 11, 'B1': 24, 'B2': 3}，edition 相同 |
| u2019 | PASS：files_with_U+2019=[] |
| s11_svg | PASS：off-palette={}，gold/old=False，stroked_rects=0，VOL.5=1（core 1，已知误印数一致），paper_fills=8 |

## 3. freeze（`freeze-core.log` / `freeze-diff-fr.log` / `freeze-diff-fr.json`）

- baseline：`freeze.py baseline --build production/2026-w47/core-zh-cn --core-svg production/2026-w47/core-zh-cn/svg --out <scratch>/freeze-core`，rc=0，`baseline: 8/8 SVGs byte-identical`，`core integrity: shipped core SVGs unchanged`。
- diff：`freeze.py diff --core-svg core/svg --edition-svg fr/svg --strict-cjk --json`，rc=0。逐页新增 CJK：P1–P8 全 0；`TOTAL added CJK characters: 0`。CJK 数：核心 886/1065/864/772/969/912/753/1125 → 本版 870/1060/859/767/964/907/742/1118（与 proof1 逐字一致）。

## 4. render / webpdf / export（`render-fix1.log` / `webpdf-fix1.log` / `export-fix1.log`）

- render.py：rc=0，cards 8/8，印 PDF 42,504,769 B。
- webpdf.py：rc=0，8 pages，724 distinct chars，`WROTE … 2,663,732 bytes, 45,540 text bytes`。字体子集：Newsreader 3 faces + Noto Sans/Serif CJK SC 各 2 faces + UnifrakturMaguntia。
- export_fr.py：rc=0，recorded strings 1050，registry 150，写出 51,821 B。导出器事先验证：修前源码副本重跑逐字节复现修前 text.md（SHA `fb72ed29…`，`export-origcheck.log`）。

## 5. 盒标题真墨 + 溢出横扫（`sweep-after.log` / `sweep-after.json`）

- 方法：proof1 `sweep.py` 同款（复用 `tools/occlusion_audit.py` 的解析与真墨度量；容器含全部纯填充奶油盒）。
- 法语版：8 页，texts 3285，containers 181，flags **0**（修前 3：`sweep-before.log`）。
- D-1：`数字看本周　Cette semaine en chiffres` 墨右缘 942.0 vs 盒 [538.5, 1110.3, 961.0, 1434.3]，余 **+19.0**；D-3：`本周生活小日历　Dates de la semaine` 墨右缘 1397.0 vs 盒 [989.0, 200.0, 1411.5, 446.0]，余 **+14.5**。
- D-2 不在容器标题表内（为盒内正文行），以 advance 实测：墨右缘 1848.5（盒 1862.0），余 +13.5；渲染像素墨右缘 1846，余 +16；sweep 全刊 0 flags 覆盖。

## 6. 孤儿扫描（`orphan_scan.py` / `orphan-fix1.json` / `orphan-fix1.log`）

- 方法：proof1 门 8 同法（按基线 y + 栏位分组，取每行最左 run 首字，闭集 `。，、；：？！」』）〕］》›`）。
- 结果：rc=0，**orphans: 0**。D-4 修复确认：数字盒第 3 项现为单基线 y=1337.265（`21 nov., samedi — le film 《试探》 sort` 四 run 连成整句），SVG 内无 `》` 行首元素（唯一的 `》` 起首 run 在 x=250.5 的段中续行，非行首）。

## 7. 150 键复核（`dump_reg-fix1.log` / `reg-fr-fix1.json` / `p8extract-fix1.json` / `p8compare-fix1.json`）

- `dump_reg.py fr`（proof1 同款 stub）：REG=150，ex=130，matches=5。
- REG 150 行与 proof1 `reg-fr.json` 逐行一致（n/page/level/type/key/note 全同）；LOG 649 条仅 1 处差异（第 25 条 boxpara，即 D-4 改动）；matches 一致。
- `p8.py extract`：150/150；印出键与 proof1 `p8extract.json` 逐键一致（仅 JSON 内路径串写法不同）。
- `p8.py compare`（直接读 JSON 本体）：rc=0，`status: CLEAN, total: 150, core_count: 150, edition_count: 150, missing: [], extra: [], uncertain: [], keydiff: []`。
- Q150 开放题印出 `✓` 与修前一致（REG 键 `(开放题，范文如下)`，预期内差异，与 proof1 相同）。

## 8. 渲染证据（`crop-d*.png`，自 `cards/*.png` 1950×2700 1:1 坐标裁切）

- `crop-d1-title.png`（x 520–990，y 1100–1170）：标题末 `s` 在盒内；渲染像素墨右缘 939，余 +22。
- `crop-d2-pressline.png`（x 1420–1880，y 1220–1280）：`Bouclage : 10 nov. — la finale pas encore jouée` 末 `é` 在盒内；渲染像素墨右缘 1846，余 +16。
- `crop-d3-title.png`（x 980–1430，y 195–260）：标题末 `e` 在盒内；渲染像素墨右缘 1397，余 +14.5。
- `crop-d4-item3.png`（x 530–970，y 1300–1400）：`21 nov., samedi — le film 《试探》 sort` 单行完整，无孤儿。

## 9. “绝不动”复验

- P4/P7/P8 所在 SVG 与修前字节相同（P3–P8 全同，见 FIX-LOG §4）：P4 注释框 6 行、框底 792.2 成立；P8 keys 尾 2537.2；P7 预告条底 2588.78（run 日志）。
- ABSTRACT.txt：333 B，末字节 `\n`，mtime 未变（2026-11-11 15:36），未动。
- WEEKLY-KIT.md：mtime 未变（2026-11-11 14:07），未动。
- 仅 `content12.py` 4 处改动；`content34/56/7/8.py`、`bslib4.py`、`svglib.py`、`render.py`、`run.py`、`assets/` 未动；核心 `core-zh-cn/` 未动（freeze baseline 核心完整性已验）。

## 10. 总表

| 门禁 | 实测 |
|---|---|
| run.py TOTAL / 溢出 | rc=0，150，0 溢出 |
| gates-zhcn.py | 11/11 ALL PASS |
| freeze baseline（核心） | rc=0，8/8 |
| freeze diff --strict-cjk | rc=0，新增 CJK 0 |
| occlusion 真实审计 | rc=0，0 flags |
| p8 extract / compare | 150/150；CLEAN（keydiff=[]） |
| 印/网文字层 | 8/8 页，posdiff 0，msdiff 0；pdftotext 45,540 B 双份 |
| P8 最小字号 | 9.98 pt（≥ 9.75） |
| 盒标题真墨 / 溢出横扫 | 0 flags；D-1 +19.0、D-2 +13.5、D-3 +14.5 |
| 孤儿扫描 | 0 orphans |
| 150 键复核 | REG 150/150 与 proof1 一致；印出键一致；仅 Q150 开放题预期差异 |
| SVG 变化 | 仅 P1、P2；其余 6 页字节不变 |
| ABSTRACT 尾换行 | 333 B，末字节 `\n` 在位 |
