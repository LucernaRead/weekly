# es — 2026-w47-zh-tw-es（完成，2026-11-11 ~02:45 UTC，第 7 棒）

**结论：完成，全量自查零问题。**

- 印刷 PDF `Lucerna-VOL4-ES.pdf` 23,256,393 字节，SHA-256 `5f77b922a5f954fbe84b59ea6a1bcce7a21f663dd27d69e4067f34d655dea9cf`；网页 PDF `Lucerna-VOL4-ES-web.pdf` 2,513,310 字节（< 7 MB），SHA-256 `c625ae1d85f220af088c6f3c95189b31442cbb970079067e5f3364310060b7b8`；text.md SHA-256 `4e7bd1ae9b864a43b65b3edb882b82de9be9535e3d930035176fce902c47aa08`。
- 门禁：run exit 0（最终轮 0 溢出、0 超宽）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；全版泄漏扫描 0；P8 徽章 38/38，Q113–150 各带徽章，F 写作标题在。
- 详见本版 `WEEKLY-KIT.md`。

## 本版修过的两处（均只改本版目录内文件）

1. **6 条 P8 答案注记预补译**：与 de/fr 同一 tables.py 缺口，首轮构建前已在 content56.py/content8.py 译成西班牙语（La ceremonia es en el Taipei Music Center. / Xiaoxue es el 22 nov. / Cuatro grandes eventos caen el mismo domingo. / Acumular puntos es 集點。），答案键不动。
2. **P7 第 3 栏溢出压页脚**：首轮 col3 终点 1908.7、预告条终点 2662.7（0 超宽警告）；修 content7.py（披露 8→7 行、诊所第 3 条注 3→2 行、句式例 5→4 行），终点 1823.3 / 2577.3，occlusion 0。本轮三条候选串先量后贴，无失败 patch。
3. 删 copytree 带入的核心旧件 3 个。

## 已裁定的非缺陷

- P4 "Palabras de béisbol" 栏头折两行（栏内，无溢出）；P5 首篇末行跨栏续排；P8 题干 10.35pt 按核心裁定；text.md 页标题英文为导出器固定格式。

## 日志

- `transform-es.log`（244 行）、`build-es-run.log`（0 警告，P7 2662.7）/ `build-es-run2.log`（0 警告）、`render-es.log`、`webpdf-es.log`、`checks-es.log`、`occlusion-es.log`（0 flags）、`p8-extract-es.log`、`p8-compare-es.log`（CLEAN）、`leak-scan-es.log`（0）、`freeze-es.log`（8/8）、`export-es.log`。
