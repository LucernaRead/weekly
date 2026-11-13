# ko — 2026-w47-zh-tw-ko（完成，2026-11-11 ~04:25 UTC，第 7 棒）

**结论：完成，全量自查零问题。**

- 印刷 PDF `Lucerna-VOL4-KO.pdf` 16,839,317 字节，SHA-256 `e1e1b6a2056728809b5e9ccbdbb9988c0205396dac94f46eb2523d3a8ed7cd56`；网页 PDF `Lucerna-VOL4-KO-web.pdf` 2,310,716 字节（< 7 MB），SHA-256 `3150f83e128f75b6614ef3149c645e596de867dd92f4454feaeeaf888124175f`；text.md SHA-256 `f5b1943de93a838bcd5fcfdd16cce0cafbcdc89eff5e6176604ae6061e81ea99`。
- 门禁：run exit 0（首轮 0 溢出、0 超宽，P7 预告条 2575.42，离页脚线 20.6px）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；全版泄漏扫描 0；P8 徽章 38/38，Q113–150 各带徽章，F 写作标题在。
- 详见本版 `WEEKLY-KIT.md`。

## 本版特点

- **与 ja 同为首轮零修改的版。** 韩语讲解紧凑：首轮即 0 FLOW OVERFLOW、0 HEAD TOO WIDE，P7 第 3 栏终点 1821.42、预告条 2575.42，无需任何内容修正。
- **6 条 P8 答案注记预补译**：与 de/fr/es/it/pt/nl/ru/ja 同一 tables.py 缺口，首轮构建前已在 content56.py/content8.py 译成韩语（시상식은 타이베이 음악 센터입니다. / 샤오쉐는 11월 22일입니다. / 네 가지 큰 행사가 같은 일요일에 열립니다. / 포인트를 모으는 것은 集點입니다.），答案键不动。
- 删 copytree 带入的核心旧件 3 个。

## 已裁定的非缺陷

- P4 "야구 단어" 栏头单行（与 fr/es/it/pt/nl/ru 的折行不同）；P5 首篇末行跨栏续排；P8 题干 10.35pt 按核心裁定；text.md 页标题英文为导出器固定格式。

## 日志

- `transform-ko.log`（244 行）、`build-ko-run.log`（0 警告）、`render-ko.log`（rc=0）、`webpdf-ko.log`、`checks-ko.log`（PASS）、`occlusion-ko.log`（0 flags）、`p8-extract-ko.log`、`p8-compare-ko.log`（CLEAN）、`leak-scan-ko.log`（0）、`freeze-ko.log`（8/8）、`export-ko.log`。
