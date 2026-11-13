# GATE-LOG — 2026-W47 nl-de 独立复校（re-proof，fix1 版）

复校员独立重跑全部机械门；不信任任何前人数字。工具一律 `tools/venv/bin/python`
（Pillow 13.0.0 / FreeType 2.14.3，freeze 各次运行均打印 runtime 行核对）。
日志与 JSON 全在 `hidden_files/w47/scratch-reproof-nl-de1/`。

## 0. 开工

- 探针：`echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；
  scratch 真实写文件成功。两项皆通后动手。
- 三 SHA 核对（开工实测 = 任务书先验值，见 PROOF-NOTE §0）：
  印 `4eacaa18f98f4e8ebdba3608da8e0ec0441f70d94533fdf8efa9234daf0188bb`（12,669,892 B）；
  网 `aba38eecd9e18499438a5f32e6f6469c3aa590ef9ed5420061f5b6bd76730953`（1,617,817 B）；
  文 `c1342c3fe20d7a26df33d604285a9a1fc746ea8ae1c62ef1c66e6211dd908aeb`（46,226 B）。
- 开工快照：85 个生产文件 SHA（`opening-snapshot.sha256`）。
- 输入缺口：`hidden_files/w47/briefs/brief-coordinator.md` 不存在（全仓 find 无此文件）；
  复校按 SOP.md + 任务书执行。

## 1. run.py（直接重建，scratch 副本）— rc=0，TOTAL 150

- 副本：`run-copy/`（仅 `.py` + `assets`，OUT 经预验指向 `…/scratch-reproof-nl-de1/run-copy/svg`）。
- `run-direct.log`：`rc=0`，`TOTAL 150`；分级 A2 46 / B1 73 / B2 31；分版
  {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}（和 = 150）；
  分型 ergänzen 65 / wählen 44 / zuordnen 8 / richtig-falsch 7 / Sätze bilden 8 /
  Lückentext 13 / übersetzen 4 / schreiben 1。
- 8 个 SVG 与生产盘逐字节比对：**8/8 MATCH**（`run-copy-sha.txt`）。
  其中 p8 `83c3cc7aa0a5142ae7e04741df6bb1118221a2f8cb473ccd26e4ab49270a86c1`，
  与 fix1 声称值 `83c3cc7aa0a5…` 一致。

## 2. freeze baseline — 核心 8/8，本版 8/8

- 核心：`freeze.py baseline --build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg
  --out scratch-reproof-nl-de1/freeze-core` → **rc=0，8/8 byte-identical**
  （`freeze-core.log`；p1 `7edd158d…` … p8 `caffbab8…`；shipped core SVGs 跑后重哈希不变）。
- 本版：`freeze.py baseline --build production/2026-w47/2026-w47-nl-de --core-svg production/2026-w47/2026-w47-nl-de/svg
  --out scratch-reproof-nl-de1/freeze-edition` → **rc=0，8/8 byte-identical**
  （`freeze-edition.log`；p1 `314ace3e…`，p2 `5a0511d9…`，p3 `3a283082…`，p4 `19889014…`，
  p5 `9eaca0c0…`，p6 `a0e18bac…`，p7 `03695006…`，p8 `83c3cc7a…`；shipped SVGs 跑后重哈希不变）。

## 3. freeze diff（核心 SVG vs 本版 SVG）— rc=0

- `freeze.py diff --core-svg …/core-nl/svg --edition-svg …/2026-w47-nl-de/svg`
  （`freeze-diff.log` / `freeze-diff.json`）：各页增/减字符串均为讲解层德↔中替换；
  增 CJK 字符合计 7，全部为 **U+3000 全角空格**（p2–p8 各 1，p1 为 0）——栏目条双语标题分隔符
  （如 `LEVEN　LEBEN`），属 SOP §1.1「不用 `·` 做分隔，用全角空格」的家具，无语义 CJK 内容新增。
  判定：通过（非内容缺陷）。

## 4. p8.py — extract 150/150，compare CLEAN

- `p8.py extract --p8 …/nl-de/svg/p8-toets.svg --total 150` → noted 150/150（`p8-extract-ed.log/.json`）；
  核心同样 150/150（`p8-extract-core.log/.json`）。
- `p8.py compare --core-p8 …/core-nl/svg/p8-toets.svg --edition-p8 …/nl-de/svg/p8-toets.svg --total 150`
  → **rc=0，status CLEAN，missing=[] extra_count=0 uncertain=[]，keydiff=[137, 138]**
  （`p8-compare.log/.json`）。140 已不在 diff 中。
- keydiff 内情：137（德 `Das Sinterklaasjournaal läuft jeden Tag um 18:00 Uhr.` vs 核心中文句）、
  138（德 `Die ersten beiden ziehen ins Viertelfinale ein.` vs 核心中文句）——翻译题键按读者语重定向，
  双向翻译均正确（PROOF-NOTE §5），属工具说明中的 informational 类，不构成失败。

## 5. occlusion_audit.py — 0 标记

- `occlusion_audit.py production/2026-w47/2026-w47-nl-de --core production/2026-w47/core-nl`
  （`occlusion.log` / `occlusion.json`）：自检 OK（6 类 planted 各命中 1 次，clean 对照静默）；
  **本版 0 flags；核心 0 flags；NEW vs core 0**。rc=0。

## 6. 印/网文字层逐页比对 — 8/8 一致

- `pdftotext -f N -l N -layout` 逐页提取（`pdftext/`），空白归一化后 diff：
  p1–p8 全部 **IDENTICAL**（字节数亦逐页相等：4744 / 4813 / 4266 / 4307 / 4749 / 4299 / 5709 / 12834）。
- 两 PDF 均为 8 页，版面 1462.5 × 2025 pt。

## 7. P8 最小字号 — 10.12pt（≥ 9.75pt 底线）

- PyMuPDF 逐 span 量测印 PDF：p1–p7 最小 11.62pt（图注），**p8 最小 10.12pt**；
  网 PDF p8 最小同为 10.12pt。≥ SOP §1.1 底线 9.75pt，通过。
- 补充：P8 题干字号 13.8px（= 10.35pt）与核心 P8 同题干同坐标（989.0, 528.04）逐字节一致，
  属核心版式固有，非本版引入。

## 8. 盒标题扫描（自写，PIL 真墨盒）— 17 个，最紧处 ≈+15px 无接触

- 方法：枚举 8 页全部 26 个浅底（`#f0eee5`）盒，取盒顶行标题真墨盒（Noto Sans CJK Bold，
  4× 超采样 `getbbox`，同基线多 run 取并集）；其中带标题盒 **17 个**
  （另 5 个 Hinweis 注释盒 + 4 个 P2 词卡不在“盒标题”计数内，与声称数一致）。
- 最紧：**P6 `VOOR OF TEGEN?　DAFÜR / DAGEGEN`，右余量 PIL 真墨盒 +13.75px；交付印 PDF
  200 dpi 光栅复测 +14.96px**。声称 +15.8px 在方法容差（≤1.2px）内一致：三法同指“约 +15px、
  无接触”。裁图 `crop-p6-title.png` 目视标题完整在框内。
- 其余 16 个标题右余量 27.50–248.75px，左余量最小 18.00px；gloss 首行最紧 P3 +22.75px。
  （注：初版扫描曾报 P3 gloss +0.75px，系单 run 取法误读多 run 行；按同基线并集重测后为 +22.75px，
  与 occlusion 0 标记一致。）

## 9. 孤儿扫描 — 0 新增

- 自写扫描（`scan_orphan_spill.py`）：全版 SVG 孤立标点元素（单字 `。·、—` 等）**本版 0 个**；
  核心 13 个，全部为核心 P8 答案分隔符 `—` / `：` 的分 run  artefact（非真实孤儿）。
  新增 = 0，通过。

## 10. 溢出扫描 — 0

- 自写扫描（顶层坐标文本 + PIL 真墨盒）：右界 1862 / 页界 1950 / 底界 2596 / 左界 0，
  唯一初报为 P1 刊头 `De Lucerna`（inkR 1995.5），系扫描 artefact：该元素为
  `text-anchor=middle` 的 UnifrakturMaguntia 刊头，我方扫描误按左锚 + 回退字体量测。
  以真实字体复测：真墨宽 898.5px，居中于 x=975，墨迹 525.8–1424.2，全在页内。
  修正后溢出 **0**；与 occlusion 工具 0 标记一致。

## 11. D11 / D12 定向复测（见 PROOF-NOTE §1–2）

- D11：SVG 末基线 1209.49 / 盒底 1229.60 / 余量 **+20.11**；交付印 PDF 200 dpi 光栅：
  盒底下 7px 带真墨像素 **0**（最小灰度 241，盒底色）；P3 Sinterklaas 盒与核心全同（末基线 1090.40，
  余量 16.20）。脚本 `measure_d11.py` / `measure_d11_pdf.py`。
- D12：源码 75–76 行、text.md:415、旧句全版 0 处、Q140 单行栏内余量 ≈60px
  （PIL 1351.31 / 光栅 1351.52，栏右界 1411.5），裁图 `crop-p8-q140.png`。
- Q150 范文逐词数 **81 词**（与 P8 印称 `(81 Wörter)` 一致，在 80–100 词区间内）。

## 12. 150 题手验 — 150/150 通过

- 三源对齐表 `verify-table.tsv`（本版 text.md 键 / 核心 text.md 键 / 两版 P8 印键）；
  键一致：147/150 逐字节同，差异仅 137、138（读者语重定向）与 Q150（开放写作例外）；
  本版文键 vs 本版印键 0 不符（Q150 除外）。
- 逐题语义配对结论见 PROOF-NOTE §5；唯一观察为 Q139 时态不对称（核心固有，非缺陷，§6）。

## 13. 收工

- 收工快照 `closing-snapshot.sha256` 与开工快照逐项比对：**85/85 一致，生产零写入**。
- 三交付物 SHA 收工复测与开工相同。
- 未 commit、未 push。全部工作件在 `scratch-reproof-nl-de1/` 内。
  （工作树 `core-nl` 的 M 标记为开工前已存在状态，与本轮无关。）
