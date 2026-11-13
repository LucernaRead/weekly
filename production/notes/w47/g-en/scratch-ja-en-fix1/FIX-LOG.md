# FIX-LOG — 2026-w47-ja-en 第一轮返修（叶子）

- 版：`2026-w47-ja-en`（日文目标语 × 英文读者），VOL.4，刊期 2026-11-16〜22
- 返修员：叶子（第一轮返修 builder；与 builder、core-ja builder、各轮复校员不同人）
- 日期：2026-11-11（UTC 07:27 起）
- 返修对象：`production/2026-w47/fanout-ja/2026-w47-ja-en/`
- 依据：第一轮复校 PROOF-NOTE（`hidden_files/w47/scratch-proof-ja-en1/PROOF-NOTE.md`）缺陷 D1、D2
- 前版身份（返修前核对，与 PROOF-NOTE 一致）：
  印刷 PDF `Lucerna-VOL4-JA-EN.pdf` 27,440,477 字节，
  SHA-256 `c29f6f987ba709082145c4ca71b7a656eb0b6bcc5f5f49d89f22b35a6161bbeb`；
  网页 PDF `Lucerna-VOL4-JA-EN-web.pdf` 4,428,571 字节，
  SHA-256 `9d10efc5fdc72c1c46194eea25cb5ff7b59f52c316a13fb5564395439396beb1`。
- 开工探针（双通才动手）：`git hash-object -w --stdin` 成功（`da0c4eb8…`）；
  goals hidden_files 真实写文件成功。

## 1. 独立核实（动手前，公开来源，不只采信复校笔记）

- D1 美ノ海：读法「ちゅらのうみ」核实——sumo-guide 力士名鑑
  「美ノ海 義久（ちゅらのうみ よしひさ）」；スポーツ報知 2026-10-26
  「美ノ海義久（ちゅらのうみ・よしひさ）」；Daily Sports 2026-10-27 同。
  故 `Umi-no-umi`（汉字字面拼法）错，`Churanōmi`（任务给定形式，无连字符）对。
- D2 藤凌駕：读法「ふじりょうが」核实——ozumo.jp（引日本相扑协会官方资料）
  「藤凌駕 雅治（ふじりょうが まさはる）」；sumo-guide 力士名鑑同；
  Wikipedia「藤凌駕 雅治（ふじりょうが まさはる）」同。
  故 `Fujiryūga`（ū 错）错，`Fujiryōga`（ō）对；与版内长音体例一致
  （Ōnosato、Hōshōryū）。

## 2. 改动逐处清单（共 6 处，全部在 P8 答案简析注文；答案键未动）

| # | 缺陷 | 键 | 文件:行 | 原文 | 改后 |
|---|------|----|---------|------|------|
| 1 | D1 | 48 | content34.py:188 | `Umi-no-umi lost to Hōshōryū on day 1` | `Churanōmi lost to Hōshōryū on day 1` |
| 2 | D2 | 49 | content34.py:190 | `Fujiryūga beat Hōshōryū on day 3` | `Fujiryōga beat Hōshōryū on day 3` |
| 3 | D2 | 54 | content34.py:202 | `Fujiryūga's kinboshi: 11th tournament since debut` | `Fujiryōga's kinboshi: 11th tournament since debut` |
| 4 | D2 | 63 | content34.py:224 | `Fujiryūga won a kinboshi on day 3` | `Fujiryōga won a kinboshi on day 3` |
| 5 | D2 | 111 | content7.py:57 | `Fujiryūga's kinboshi: 11th tournament since debut` | `Fujiryōga's kinboshi: 11th tournament since debut` |
| 6 | D2 | 116 | content8.py:22 | `Hōshōryū lost to Fujiryūga on day 3` | `Hōshōryū lost to Fujiryōga on day 3` |

- 全版 grep（改后）：`Fujiryūga` / `Umi-no-umi` 在 .py 源码、8 个 SVG、
  `.text.md` 中均为 0×；唯一残留是 WEEKLY-KIT.md §11 F6 记录本身引用的
  旧拼法（有意记录）。`Fujiryōga` ×5、`Churanōmi` ×1，位置与上表一致。
- 过期 `__pycache__/content7.cpython-312.pyc` 仍含旧字节，已手工删除；
  构建经 runpy 读源码，不加载它（新渲染已证实）。
- 其余改动：无。core-ja 未碰；W43–W46、其他目标语家庭、tools/ 未碰；
  未跑 insert.py、未跑 lint --write、未 git add/commit/push/reset/stash。

## 3. 上游来源与受影响版（只报告，未改其他版）

- 两个错拼的上游是 core-ja `WEEKLY-KIT.md` §3 趋势来源记录
  （第 80–90 行）："Hōshōryū beat Umi-no-umi"、"Kotosakura lost to
  Fujiryūga"、"Ōnosato beat Fujiryūga"、"Hōshōryū lost to Fujiryūga —
  Fujiryūga's first kinboshi"。core 正文用汉字（美ノ海 / 藤凌駕），
  只有 KIT 的英文赛果记录带错拼。
- 不是一个共用罗马字表文件：本 clone 无 `map-en.json` / `apply.py`
  （复校 O3 已记）；各拉丁字母 fan-out 各自带了同样的 6 处。
- 其他版现状（.py 源码计数，2026-11-11 07:30 实测）：
  - ja-es / ja-fr / ja-it / ja-nl / ja-pt：仍各带 `Fujiryūga` ×5 +
    `Umi-no-umi` ×1（与本版改前相同），未改。
  - ja-de：.py 已是 `Fujiryōga` ×5 + `Churanoumi` ×1（无 macron、
    无连字符的另一拼法；何人所改未核查，其 svg/.text.md 仍带旧拼，
    尚未重渲染）——未碰。
  - ja-ko / ja-ru / ja-zh-tw：.py 中无拉丁拼法（注文用日文汉字），不受影响。
- core-ja 本身不动（红线）；上游 KIT 记录的错拼建议由协调员决定是否订正。

## 4. 附带发现（非缺陷，记录）

- (a) `export-textmd-en.py` 在本 clone 中缺失（与 map/apply 同属 O3
  缺失项），已按 KIT §9 描述重建并放回版目录；验证：对改前 SVG
  逐字节复现改前 `.text.md`，对改后 SVG 逐字节复现改后 `.text.md`。
- (b) KIT §7 旧句 "P8-keys flow ends col 3 y=2426 (bottom 2540,
  114px slack)" 与实测不符：改后实测 keys flow 最末基线 y=2530.5
  （col 2 key 76；col 3 key 114 y=2530.3；底边 2540，余 9.5px；
  页脚分隔线 2596，净空）。该数改前即如此（6 条注文行数未变），
  属旧记录失实，非本次引入；遮挡审计 0 旗标，目视 P8 页脚净空，
  不构成缺陷。KIT §7 已按实测订正，§11 F6 亦记。
- (c) 改后 PDF 字节均比改前 +4（印刷 27,440,481；网页 4,428,575）：
  字符串本身等长，差值来自 CairoSVG/webpdf 重渲染的容器字节；
  文字层内容逐字节一致（pdftotext 46,044 字节双版一致，layout
  导出 99,988 字节双版一致）。

## 5. 重渲染

- run11：`tools/venv/bin/python run.py` rc 0，零 FLOW OVERFLOW /
  HEAD TOO WIDE；registry 与 KIT 一致（150 题；A2 48 / B1 73 / B2 29；
  分版 10/18/18/18/18/18/12/38；题型 fill-in 50 / multiple choice 51 /
  matching 12 / sentence building 8 / true/false 11 / cloze 13 /
  translation 4 / writing 1；范文 154 字）。
- run11：`render.py` rc 0（8 张 cards + 印刷 PDF）。
- run11：`tools/webpdf.py svg Lucerna-VOL4-JA-EN-web.pdf` rc 0。
- run11：`export-textmd-en.py` 重导出 `.text.md`（45,706 字节，
  与改前逐字节 diff 恰为上述 6 行）。
- run12：`run.py` 重跑 rc 0，零溢出；SVG sha256 run11 vs run12 8/8 一致。

## 6. 新成品身份（本轮交付物）

- 印刷 PDF `Lucerna-VOL4-JA-EN.pdf`：27,440,481 字节，8 页，
  SHA-256 `38b0d3ab8db70ce62f491f9f608c05b79125ae336349d26b423ad68bec4bb965`
- 网页 PDF `Lucerna-VOL4-JA-EN-web.pdf`：4,428,575 字节（< 7 MB），8 页，
  SHA-256 `95cf9e66f51aa4d01c0f346ac8e052516136657814c9c2aab6ac1dba7d71204b`
- `.text.md`：45,706 字节，1376 行（1348 文本行），改动恰为 6 行。

## 7. KIT 更新

- `WEEKLY-KIT.md`：§7 P8-keys 末行实测订正；§8 门记录更新为
  run11/run12（新 SHA/字节、layout 导出 99,988 字节、U+2019 0、
  150 键复核）；§11 增 F6（核实来源、6 处清单、上游与他版现状、
  导出器重建、§7 订正）。

## 8. 交接

- 按 SOP §8.4，改后须从头再做一轮全量复校（第二轮，协调员另派，
  不由本轮返修员做），零问题方可定稿。本轮不作定稿决定。
