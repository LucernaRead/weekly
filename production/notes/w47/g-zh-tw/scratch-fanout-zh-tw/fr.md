# fr — 2026-w47-zh-tw-fr（完成，2026-11-11 ~02:30 UTC，第 7 棒）

**结论：完成，全量自查零问题。**

- 印刷 PDF `Lucerna-VOL4-FR.pdf` 20,191,919 字节，SHA-256 `beeebce2531fcadd076f3999d8965ee425df76efe47c1e8f1584365fe74930b3`；网页 PDF `Lucerna-VOL4-FR-web.pdf` 2,350,191 字节（< 7 MB），SHA-256 `61537f8dde6b5c04b63adebdd5835275d41108588c426688a0bf1cc4c1ce04df`；text.md 52,507 字节，SHA-256 `415890f41a1523105ccd68fbfaba0d01d922dfeed78774d285efd3f51906301e`。
- 门禁：run exit 0（最终轮 0 FLOW OVERFLOW、0 HEAD TOO WIDE）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；全版泄漏扫描 0；P8 徽章 38/38，Q113–150 各带徽章，F 写作标题在。
- 详见本版 `WEEKLY-KIT.md`。

## 本版修过的三处（均只改本版目录内文件）

1. **6 条 P8 答案注记预补译**：与 de 同一 tables.py 缺口，首轮构建前已在 content56.py/content8.py 译成法语（La cérémonie a lieu au Taipei Music Center. / Xiaoxue est le 22 nov. / Quatre grands événements tombent le même dimanche. / Collectionner des points se dit 集點。），答案键不动。
2. **P6 栏头超宽**：首轮 2× HEAD TOO WIDE（446.3px / 467.1px vs 栏宽 422.5px），content56.py 缩为 "Lire la frise" / "Quiz de lecture"，次轮 0 警告。
3. **P7 第 3 栏溢出压页脚**：首轮 col3 终点 1908.7、预告条终点 2662.7；修 content7.py（披露 8→7 行、诊所第 3 条注 3→2 行、句式例 5→4 行），终点 1823.3 / 2577.3，occlusion 0。注意：首次 patch 因误用 gloss 措辞（文件实为 "spectacle de lumières … 17:30 à 23:00"，非 "spectacle lumineux … 17 h 30"）断言失败，已按文件原串重贴；content56.py 已先修好，未重复改。
4. 删 copytree 带入的核心旧件 3 个；text.md H1 按 W46 fr 前例改为 "Textes en chinois traditionnel" 后重导出。

## 已裁定的非缺陷

- P4 "Mots du baseball" 栏头折两行（栏内折行，无溢出警告、无重叠）；P5 首篇末行跨栏续排；P8 题干 10.35pt 按核心裁定；text.md 页标题英文为导出器固定格式。

## 日志

- `transform-fr.log`（244 行）、`build-fr-run.log`（2 HEAD TOO WIDE，P7 2662.7）/ `build-fr-run2.log`（0 警告）、`render-fr.log`、`webpdf-fr.log`、`checks-fr.log`、`occlusion-fr.log`（0 flags）、`p8-extract-fr.log`、`p8-compare-fr.log`（CLEAN）、`leak-scan-fr.log`（0）、`measure-fr.log`、`freeze-fr.log`（8/8）、`export-fr.log` / `export-fr2.log`。
