# ja — 2026-w47-zh-tw-ja（完成，2026-11-11 ~04:10 UTC，第 7 棒）

**结论：完成，全量自查零问题（checks.py 的 SIMP_ONLY 报错为已证实的日语汉字误报，见下）。**

- 印刷 PDF `Lucerna-VOL4-JA.pdf` 18,090,244 字节，SHA-256 `35fb9b00d5e9c33f4d1ef9fdcecaff5f83b3139e264b39182a420f2fb90b3d95`；网页 PDF `Lucerna-VOL4-JA-web.pdf` 2,548,035 字节（< 7 MB），SHA-256 `5c3be54673d3e1d65b14df730b48a1de908ca30d6a354ea651cd1811dc9f912f`；text.md SHA-256 `47162db4c1020a498e429df6336dbc3f7d83137a0ecfbb8d0ac0832f31b08918`。
- 门禁：run exit 0（首轮 0 溢出、0 超宽，P7 预告条 2581.28，离页脚线 14.7px）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；全版泄漏扫描 0；P8 徽章 38/38，Q113–150 各带徽章，F 写作标题在。
- 详见本版 `WEEKLY-KIT.md`。

## 本版特点

- **九版中唯一首轮零修改的版。** 日语讲解紧凑：首轮即 0 FLOW OVERFLOW、0 HEAD TOO WIDE，P7 第 3 栏终点 1827.28、预告条 2581.28，无需任何内容修正。
- **6 条 P8 答案注记预补译**：与 de/fr/es/it/pt/nl/ru 同一 tables.py 缺口，首轮构建前已在 content56.py/content8.py 译成日语（式典は台北音楽センターです。/ 小雪は11月22日です。/ 4つの大きなイベントが同じ日曜日に重なります。/ ポイントを集めることは集點です。），答案键不动。
- 删 copytree 带入的核心旧件 3 个。

## checks.py SIMP_ONLY 误报（已核实，非缺陷）

`checks.py` 报 `CHECKS FAIL`，`SIMP_ONLY_HITS ['国', '学']`。逐处核实：两字均为日语汉字（新字体），只出现在 3 处日语讲解串中——(1) P1 徽章行 "繁体字中国語の本文…" 中的「中国語」；(2) P3 注记 "高雄国際鋼雕芸術祭" 中的「国際」；(3) P7 "四つの便利な言葉が学べる" 中的「学べる」。繁体中文正文内无 国/学。SIMP_ONLY 检查无法区分日语汉字与简体字，今后每期 ja 版都会同样触发，正确做法是逐处核实上下文。短语（8 条各 2 次）与图表检查均通过。

## 已裁定的非缺陷

- P4 "野球のことば" 栏头单行（与 fr/es/it/pt/nl/ru 的折行不同）；P5 首篇末行跨栏续排；P8 题干 10.35pt 按核心裁定；text.md 页标题英文为导出器固定格式；P7 col3 终点 1827.28（名义目标 1826 仅超 1.28px，预告条离页脚线 14.7px，occlusion 0，目视确认）。

## 日志

- `transform-ja.log`（244 行）、`build-ja-run.log`（0 警告）、`render-ja.log`（rc=0）、`webpdf-ja.log`、`checks-ja.log`（SIMP_ONLY 误报）、`occlusion-ja.log`（0 flags）、`p8-extract-ja.log`、`p8-compare-ja.log`（CLEAN）、`leak-scan-ja.log`（0）、`freeze-ja.log`（8/8）、`export-ja.log`。
