# pt — 2026-w47-zh-tw-pt（完成，2026-11-11 ~03:10 UTC，第 7 棒）

**结论：完成，全量自查零问题。**

- 印刷 PDF `Lucerna-VOL4-PT.pdf` 20,944,927 字节，SHA-256 `3673d36cb0890418be4e1699fdda2e0df0525516227a7cd0dc8b35bf414e8d47`；网页 PDF `Lucerna-VOL4-PT-web.pdf` 2,396,718 字节（< 7 MB），SHA-256 `da2dd497b7fca416acba2751f4e7c4cc6321418d71efc7fe1f4ffa16c345db14`；text.md SHA-256 `1f1738742785e806b65e63afb44fc92854e04fc79de12ba11676c42404857f37`。
- 门禁：run exit 0（最终轮 0 溢出、0 超宽）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；全版泄漏扫描 0；P8 徽章 38/38，Q113–150 各带徽章，F 写作标题在。
- 详见本版 `WEEKLY-KIT.md`。

## 本版修过的三处（均只改本版目录内文件）

1. **6 条 P8 答案注记预补译**：与 de/fr/es/it 同一 tables.py 缺口，首轮构建前已在 content56.py/content8.py 译成葡萄牙语（A cerimônia é no Taipei Music Center. / Xiaoxue é 22 de nov. / Quatro grandes eventos caem no mesmo domingo. / Acumular pontos é 集點。），答案键不动。
2. **P6 栏头超宽**：首轮 1× HEAD TOO WIDE（469.6px vs 栏宽 422.5px），content56.py 缩为 "Quiz de leitura"（303.9px）。
3. **P7 第 3 栏溢出压页脚**：首轮 col3 终点 1908.7、预告条终点 2662.7；修 content7.py（披露 8→7 行、诊所第 3 条注 3→2 行、句式例 5→4 行），终点 1823.3 / 2577.3，occlusion 0。
4. 删 copytree 带入的核心旧件 3 个。

## 已裁定的非缺陷

- P4 "Palavras do beisebol" 栏头折两行（栏内，无溢出）；P5 首篇末行跨栏续排；P8 题干 10.35pt 按核心裁定；text.md 页标题英文为导出器固定格式。

## 日志

- `transform-pt.log`（244 行）、`build-pt-run.log`（1 HEAD TOO WIDE，P7 2662.7）/ `build-pt-run2.log`（0 警告）、`render-pt.log`、`webpdf-pt.log`、`checks-pt.log`、`occlusion-pt.log`（0 flags）、`p8-extract-pt.log`、`p8-compare-pt.log`（CLEAN）、`leak-scan-pt.log`（0）、`freeze-pt.log`（8/8）、`export-pt.log`。
