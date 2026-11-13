# GATE-LOG — 2026-w47-ja-en 第一轮返修后全套机械门（叶子）

- 版：`2026-w47-ja-en`，VOL.4；构建 run11（内容）+ run12（冻结复跑）
- 解释器：`tools/venv/bin/python`（Python 3.12.3），构建与冻结同一解释器
- 日期：2026-11-11；记录文件均在本目录（`scratch-ja-en-fix1/`）

## 门禁结果总表（全部通过）

| 门 | 工具/方法 | 结果 |
|---|---|---|
| 构建 | `tools/venv/bin/python run.py`（run11、run12） | rc 0；FLOW OVERFLOW / HEAD TOO WIDE 0×；registry 150 题与 KIT 一致 |
| 渲染 | `tools/venv/bin/python render.py`（run11） | rc 0；8 cards + 印刷 PDF |
| 网页 PDF | `tools/venv/bin/python tools/webpdf.py svg Lucerna-VOL4-JA-EN-web.pdf` | rc 0；4,428,575 字节 |
| 遮挡 | `tools/occlusion_audit.py`（+ --selftest） | 0 flags；selftest OK（6 类全触发，干净对照静默） |
| P8 提取 | `tools/p8.py extract --total 150` | noted 150/150 |
| P8 对照 | `tools/p8.py compare` vs core-ja | CLEAN；missing=[] extra_count=0 uncertain=[]；keydiff=[137, 138, 139, 140] |
| 冻结 | SVG sha256 直比 run11 vs run12 | 8/8 byte-identical |
| 文字层双版一致 | `pdftotext -layout` 双 PDF 导出 cmp | 逐字节一致（各 99,988 字节）；`pdftotext` 纯文本双版各 46,044 字节 |
| P8 最小字号 | PyMuPDF 测印刷 PDF p.8 | 9.975pt（≥9.75pt ✓）；165 span；次档 10.35pt（79 span，题干） |
| U+2019 全扫 | SVG ×8 + 双 PDF 文字层 | 0（U+2018 亦 0） |
| §1.1 grep 审计 | 终版 SVG | 纸 `#fbfaf6` 1×/页；旧 `#f7f1e2` 0；禁色 0；`·` 0；徽章色齐全；刊头 196px 仅 P1 1 处；`Page N of 8` 1×/页；页脚 8/8 |
| 150 键逐题复核 | 答案区旧 vs 新逐行 diff + p8 extract keys | 除 6 处注文外与上一轮逐字节一致；6 处键（B/A/11/○/11/A）未变 |
| 8 版目视 | cards PNG（重渲染）逐版 + P8 答案区全分辨率裁切 | 无溢出/重叠/压页脚；6 处改后拼法目视确认（macron 清晰） |

## 逐项证据

### 构建 / 渲染 / 网页 PDF
- `build-en-run11.log`：run.py rc 0，TOTAL 150，by level {'A2': 48, 'B1': 73, 'B2': 29}，
  by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}，
  by type {fill-in: 50, multiple choice: 51, matching: 12, sentence building: 8,
  true/false: 11, cloze: 13, translation: 4, writing: 1}；model chars 154；
  FLOW OVERFLOW / HEAD TOO WIDE 计数 0。
- `build-en-run12.log`：同上（冻结复跑 rc 0，零溢出）。
- `render-en-run11.log`：render.py rc 0，cards p1–p8 + print PDF 27,440,481 字节。
- `webpdf-en-run11.log`：webpdf.py rc 0，`Lucerna-VOL4-JA-EN-web.pdf` 4,428,575 字节，
  46,044 text bytes（与改前 pdftotext 字节数相同）。

### 冻结
- `en-sha-run11.txt` vs `en-sha-run12.txt`：diff 空，8/8 一致。
  run11：p1 c695313e… p2 da0faee4… p3 42f368e3… p4 53bc8f7c… p5 96bc4ac9…
  p6 9efab662… p7 9d437896… p8 c9df11b8…（全值见文件）。

### 遮挡
- `occlusion-selftest-run11.log`：selftest OK，planted classes fired
  {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}，
  clean controls silent。
- `en-occlusion-run11.json` / `occlusion-run11.log`：
  `production/2026-w47/fanout-ja/2026-w47-ja-en/svg: 0 flags`。

### P8
- `en-p8-run11.json` / `p8extract-run11.log`：noted set = 150 of 150。
- `en-p8compare-run11.json` / `p8compare-run11.log`：core 150 noted，
  edition 150 noted，status CLEAN，missing=[] extra_count=0 uncertain=[],
  keydiff=[137, 138, 139, 140]（与上一轮完全相同；137–140 为 E 组
  中译英答案，逐条与复校记录一致，未变）。

### 文字层
- `pdftotext -layout` 印刷版与网页版导出各 99,988 字节，`cmp` 逐字节一致。
- 纯 `pdftotext` 双版各 46,044 字节；PyMuPDF 双版各 25,280 字符。
- 双 PDF 均为 8 页。

### P8 字号
- PyMuPDF（venv）：P8 共 378 span，最小 9.975pt（165 span，答案），
  次档 10.35pt（79 span，题干），与 KIT 登记一致（≥9.75pt ✓）。

### U+2019 / §1.1
- U+2019：8 SVG 0，印刷 PDF 文字层 0，网页 PDF 文字层 0；U+2018 亦 0。
- §1.1：`#fbfaf6` 每版 1 次；`#f7f1e2` 0；`·` 0；禁色
  （#c9a227/#d4af37/#8b4513/#a0522d/#000000/#111111）0；
  徽章 A2 `#5c6e30` ×45 / B1 `#46581f` ×373 / B2 `#37402f` ×35；
  刊头 `Lucerna` 196px 仅 P1 1 处；`Page N of 8` 每版 1 次；
  页脚 `Lucerna　JAPANESE WEEKLY VOL.4　Japanese text　English explanations` 8/8；
  VOL.4：P1 3 次、P2–P8 各 1 次（VOL.3/VOL.5 冻结正文，未核查动——与上一轮计数相同）。

### 150 键逐题复核
- 方法：改前 `.text.md`（重渲染前备份）与改后 `.text.md` 的 P8 答案区
  （答え Answers 头起）逐行 diff；另用 `p8.py extract` keys 字典核对键值。
- 结果：答案区 169 行中仅 6 行不同，即 F6 的 6 条注文（48、49、54、63、
  111、116）；其余 144 条（含 E 组 137–140、范文 150）逐字节一致。
- 6 处键未变：48=B、49=A、54=11、63=○、111=11、116=A；
  extract JSON keys 同值。注文新拼法：48 `Churanōmi`、49/54/63/111/116 `Fujiryōga`。
- 特殊格式已逐条确认未变：139（尾随 `—` 空注）、140（折两行）、
  150（`✓ Model text … (154 characters)`，无 `—` 分隔符）。

### 8 版目视
- 审读对象：run11 重渲染的 `cards/*.png`（非旧图），`review/` 下 780px
  缩览 8 版 + P8 答案区全分辨率裁切 3 张（col2 keys 48–63、key 111、key 116）。
- 结果：8 版均无溢出、重叠、压页脚、图片与出处问题；P8 答案区 6 处
  改后拼法逐字目视确认，macron 清晰，无宽撇号/断裂。
  （P4 顶栏 "5) でお知らせします。" 为冻结核心正文续行，改前即有，非改动。）

## 新成品身份
- 印刷 PDF `Lucerna-VOL4-JA-EN.pdf`：27,440,481 字节，
  SHA-256 `38b0d3ab8db70ce62f491f9f608c05b79125ae336349d26b423ad68bec4bb965`
- 网页 PDF `Lucerna-VOL4-JA-EN-web.pdf`：4,428,575 字节，
  SHA-256 `95cf9e66f51aa4d01c0f346ac8e052516136657814c9c2aab6ac1dba7d71204b`
- `.text.md`：45,706 字节（与改前同；6 处等长替换）

## 未做事项
- 未跑 insert.py、未跑 lint --write；未 git add/commit/push/reset/stash；
  未改 core-ja、W43–W46、其他目标语家庭、tools/。
- 第二轮全量复校待协调员另派（SOP §8.4），本轮不作定稿决定。
