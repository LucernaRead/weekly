# de — 2026-w47-zh-tw-de（完成，2026-11-11 ~02:10 UTC，第 7 棒）

**结论：完成，全量自查零问题。**

- 印刷 PDF `Lucerna-VOL4-DE.pdf` 21,717,574 字节，SHA-256 `28af6ac44b607d5a2e7518e45a422ae23859fe10bc0142ba6c81f0dc9edaa77c`；网页 PDF `Lucerna-VOL4-DE-web.pdf` 2,436,311 字节（< 7 MB），SHA-256 `18f1ed9d6f978b5c5e29eb080498dbc9c4b5120e2c4e899fc1e288c2894619f8`；text.md 51,842 字节，SHA-256 `6a3c4ae7df0d0f95e37c758d640c0bbf449eea6e6a563fd6f55510cd4792631e`。
- 门禁：run.py exit 0（0 FLOW OVERFLOW；1 HEAD TOO WIDE 已裁定，见下）；occlusion 0 flags；p8 extract 150/150、compare CLEAN（键与核心一致）；freeze 直接 sha256 8/8 MATCH；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt（双 PDF）；§1.1 逐项实测通过；8 版渲染图逐版目视通过；150 题逐题复核通过（键一致 + 全版英文泄漏扫描 0）；P8 徽章 38/38，Q113–150 各带徽章，F 写作标题在。
- 详见本版 `WEEKLY-KIT.md`。

## 本版修过的两处（均只改本版目录内文件）

1. **P7 第 3 栏溢出压页脚**：德语讲解比英语长 ~30%，col3 终点 1935.2（核心 1825.4），预告条终点 2689.2，超页脚线 93px，occlusion 2 flags。修 content7.py：读者园地德语披露 8→7 行、诊所第 3 条注 3→2 行、句式例 5→4 行、预告条高 118→104px；结果 col3 终点 1849.8、预告条终点 2589.8（页脚线 2596，上方 6.2px），occlusion 0。三条缩短的德语已同步回 tables.py（仅 de 列）。
2. **6 条 P8 答案注记未译出（英文残留）**：Q92、Q98/Q117/Q138、Q100、Q134。原因：tables.py ENTRIES 缺这 5 条源串，transform 没换。修 content56.py（Q92/98/100）+ content8.py（Q117/134/138），答案键不动。修后全版泄漏扫描 0。
3. 删 copytree 带入的 3 个核心旧件（Lucerna-VOL4.pdf、Lucerna-VOL4-web.pdf、2026-w47-zh-tw-en.text.md，SHA 核对与核心一致后删除）。

## 已裁定的非缺陷

- P8 D 头 `Lesen und antworten` 实测 423.08px vs 栏宽 422.5px，超 0.58px 进 28px 装订空隙，无碰撞（W46 de 已发版同一警告）；P7 B1 栏终点 1568 vs 标称底 1560（+8px，下方金句条远在 292px 外）；P5 首篇末行跨栏续排；P8 题干 10.35pt 按核心裁定；text.md 页标题英文为导出器固定格式（与核心/W46 de 一致）。

## 共享缺口（转协调员：其余 8 语都会遇到）

- **tables.py 缺 5 条源串**：`Xiaoxue is Nov 22.`、`The ceremony is at the Taipei Music Center.`、`Four big events fall on the same Sunday.`、`Collecting points is 集點.`，另 `Xiaoxue is Nov 22.` 一串对应 3 个键注。fr–ko 各版须在自家 content56.py/content8.py 里把这 5 串译成本语（不要只加 de 列就以为完事；也不要无其他 8 语译文就往 ENTRIES 里加）。
- **P7 第 3 栏德语/法语等长讲解语普遍会超**：各版须实测 col3 终点，超了按本版同法缩短本语讲解层（披露/诊所注/句式例/预告条高），不要动目标语正文。
- **stale core 文件**：每版 transform 后须删 copytree 带入的 `Lucerna-VOL4.pdf`、`Lucerna-VOL4-web.pdf`、`<core>.text.md`（本版已删；transform.py 未删）。

## 日志

- `transform-de.log`（TRANSFORM OK de，244 行）、`build-de-run.log` / `build-de-run2.log` / `build-de-run3.log`、`render-de.log` / `render-de2.log` / `render-de3.log`、`webpdf-de.log` / `webpdf-de2.log` / `webpdf-de3.log`、`checks-de.log` / `checks-de2.log` / `checks-de3.log`、`occlusion-de.log`（2 flags）/ `occlusion-de2.log` / `occlusion-de3.log`（0 flags）、`p8-extract-de.log`、`p8-compare-de.log`（CLEAN）、`p8-keys-de.json`、`p8-keys-core.json`、`measure-de.log`、`chips-de.log`、`leak-scan-de.log`（6 leaks）/ `leak-scan-de3.log`（0）、`textmd-selfread-de.log`、`freeze-de.log` / `freeze-de3.log`（8/8）、`export-de.log` / `export-de2.log`。
