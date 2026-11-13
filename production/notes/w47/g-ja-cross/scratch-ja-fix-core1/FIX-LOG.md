# FIX-LOG — 2026-W47 core-ja 第一轮返修（核心笔误 key 47）

- 返修 builder：叶子（第一轮，与 core-ja builder / ja 各轮复校员不同人）
- 日期：2026-11-11（EST 02:44 任务下达，约 07:00 开工）
- 对象：`production/2026-w47/core-ja/`（`2026-w47-ja-zh-cn`，VOL.4）
- 依据：SOP.md §8、§1.1；AGENTS.md；core-ja WEEKLY-KIT.md；
  de-fr 第一轮复校 PROOF-NOTE.md（`hidden_files/w47/scratch-proof-ja-de1/`）O1；
  ja-de fix1 FIX-LOG.md（`goals/.../hidden_files/w47/scratch-ja-de-fix1/`）第 3 点 / 第 5 点
- 结论：**1 处核心笔误修完，整期重渲染，全套机械门全绿，8 版目视通过。
  待全量复校（协调员另派）。**

## 0. 开工探针（双通才动手）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` →
  `da0c4eb8d9a48d171a33574b380752e183286751`，RC=0。
- `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ja-fix-core1/.probe`
  真实写盘成功。
- 身份复核（修前）：旧印刷 PDF 26,018,003 字节 /
  `e1782168d89d06cd080dd7acf62b6dafc69ca7dc5c6c839e698e25c3de2466bd`；
  旧网页 PDF 4,652,749 字节 /
  `7c21329c89efcda759e5aeb91fffd7ac47871b36a6a03a29652f7ccf598c5a1c`；
  旧 text.md 44,432 字节 /
  `49d7c1f7ac8d01d02e5c11a5b9445641125fa1c0bfe39466e8a32997564410b3`。

## 1. 动手前独立核实（不只采信复校笔记）

### (1) 日文正文确为 義ノ富士 ✓

- `content34.py:120`（P4 正文）：
  「2場所連続優勝をねらう大の里が、小結の義ノ富士に突き落としで敗れました。」
- `content34.py:187`（key 47 题干）：
  「初日に大の里に勝ったのはだれですか。 A. 義ノ富士　B. 美ノ海　C. 藤凌駕」
- `content34.py:189`（key 48 题干选项 A 亦为 義ノ富士）、`content8.py:21`
  （P8 ex 115 题干）「大の里は初日、義ノ富士に（___）ました。」

### (2) key 47 与 key 115 指同一人 ✓

- key 47 题干：初日に大の里に勝ったのはだれですか（A. 義ノ富士）。
- key 115 题干：大の里は初日、義ノ富士に（___）ました（A. 負け　B. 勝ち）。
- 同一事实（初日大の里败给義ノ富士），同一选项人。key 115 中文简析
  （`content8.py:20`）「大之里首日输给了义之富士」已正确。

### (3) 全核心 grep（修前）✓ 一之富士只在 key 47 一处

| 串 | content*.py | text.md | svg（p8） |
|---|---|---|---|
| `一之富士` | 1（content34.py:186） | 1（:1247） | 1 |
| `义之富士` | 1（content8.py:20，key 115） | 1（:1319） | 1 |
| `義之富士` | 0 | 0 | 0 |
| `義ノ富士`（日文正文/题干） | 4 | 2 | — |

- 其他提及義ノ富士的中文简析：只有 key 47（错）与 key 115（对）两处，
  无同类一/义混淆。key 48 简析「首日败给丰升龙的是美之海」指美ノ海，
  非義ノ富士，无误。
- 「一之酉」（`content12.py:261` / text.md:1217，key 19）是一之酉
  （Ichi-no-tori），正确，未动。

## 2. 改动清单（源码 1 处 + 生成物同步）

| # | 文件:行 | 原文 | 改后 |
|---|---|---|---|
| 1 | content34.py:186 | `首日战胜大之里的是一之富士` | `首日战胜大之里的是义之富士`（key 47 注文，一字 一→义） |

- 其余一字不动。text.md 由重建的导出器从新 SVG 生成（见 §3），
  diff vs 修前：仅 1247 行一处变化。
- SVG：仅 `svg/p8-tesuto.svg` 变化（`9db7294a…` →
  `f7118644ac8b31a4be2f04c7044afd0a9043592bfd89d1b45c1b0526c08798a2`）；
  P1–P7 SVG 与修前逐字节一致（freeze 8/8 佐证）。
- KIT（§8 新 SHA/字节 + Fix 1 门禁节、§9 导出器重建 NOTE、§11 Fix 1 记录）
  与 `ja-gates.log`（Fix 1 附录）同步更新。
- 未改动：W43–W46、其他目标语家庭、tools/；未跑 insert.py、lint --write；
  未 git add/commit/push/reset/stash。

## 3. text.md 导出器重建

- KIT §9 所指 `hidden_files/w47/scratch-ja/export-textmd.py` 在本 clone 中
  已不存在（`hidden_files/w47/` 下无 `scratch-ja/` 目录）。
- 在本 scratch 重建 `export-textmd-core.py`（SVG `<text>` 逐行导出，仿照
  fanout-ja-en 已验证的导出器）。验证：对修前 SVG 运行，与修前 text.md
  **逐字节一致**（1357 行），然后才用于新 SVG。
- 新 text.md 44,432 字节（与修前同字节，因 一/义 同为 3 字节 UTF-8）。

## 4. 重建后验证

- 全核心 grep `一之富士`：py=0、md=0、svg=0。
- `义之富士`：py=2、md=2、svg=2（= 修前 `一之富士` 1 + `义之富士` 1，各处一致）。
- `一之酉` 仍在原处（content12.py:261、text.md:1217），未动。

## 5. 新双 PDF

- 印刷 `Lucerna-VOL4.pdf`：26,018,019 字节 /
  `20b9d50469fbb6ca6470c17becb2790a30f69191d9083520a9270ea7ebbe9ab4`
  （旧 26,018,003 字节 /
  `e1782168d89d06cd080dd7acf62b6dafc69ca7dc5c6c839e698e25c3de2466bd`）
- 网页 `Lucerna-VOL4-web.pdf`：4,652,763 字节（< 7 MB）/
  `8722bdfbcec0478a7a60fc86ab0ee7cc9333f957253959476d4f608eed82d5b0`
  （旧 4,652,749 字节 /
  `7c21329c89efcda759e5aeb91fffd7ac47871b36a6a03a29652f7ccf598c5a1c`）
- text.md：44,432 字节 /
  `bcfa667da57e2f477b9d825200b98db454ade3c1dde6ec92ea3d446b0bf9926a`

## 6. 门禁与复核（摘要，详见 GATE-LOG.md）

- `run.py` ×2（tools/venv）：均 exit 0，零溢出；登记 150（A2 48 / B1 73 /
  B2 29；分版 10/18/18/18/18/18/12/38；题型与 KIT 一致）。
- `render.py` exit 0；`webpdf.py` exit 0（首次 RC=120 瞬时失败，见 §8）。
- freeze 8/8（tools/venv/bin/python）；occlusion 0 flags；p8 extract 150/150，
  noted 集与修前一致、0 key diffs。
- print/web 文字层 pdftotext 各 44,818 B，逐字节一致（web -layout 85,061 B）。
- P8 最小字号 9.98pt（≥9.75pt；题干 10.35pt）。
- U+2019 全扫 0（SVG + text.md + py）。
- 150 键逐题复核：登记 vs 印刷 P8 答案行 145 条逐字一致；余 5 条为冻结版式
  （F 组 141–144 题干行 + 键行、写作题 150 的 ✓ 显示），与修前逐字节一致；
  除 key 47 注文一字外与上一轮一致。
- 8 版目视（新印刷 PDF 100 dpi）：全部干净；P8 答案区放大确认 key 47 为
  「义之富士」；网页版 P8 key 47 裁图与印刷版逐字节一致。

## 7. 未动（红线外，另案）

- 各 fan-out 版：一字未动（其 P8 注文为读者语译文，de 版已核实两处均正确译为
  Yoshinofuji）。
- core-ja KIT §3 趋势叙述中的罗马字误拼（Umi-no-umi、Fujiryūga）：另案记录问题，
  不在本修补范围内，未动。

## 8. 过程事件：瞬时配额满（已恢复，无残留影响）

- 首次 `webpdf.py` 在第一支 subset 字体后无输出地失败（RC=120），随后
  text.md 写盘报 `OSError: [Errno 122] Disk quota exceeded`——当时 `df`
  仍有 45G 空闲，属配额（EDQUOT）瞬时触顶，并行负载所致（见 AGENTS.md
  2026-11-10 同类记录）。
- 处置：未硬锤、未重试写盘循环；先探针小写盘（通过），再以全新 TMPDIR
  重跑 webpdf，RC=0 成功。旧网页 PDF 在失败期间未被覆盖（时间戳仍为修前）。
- 失败的 webpdf 临时目录在 /tmp（tmpfs，不占配额）；已清理本次产生的
  /tmp 临时文件；他人 /tmp 文件未动。

## 9. 工作文件

- 本笔记：`hidden_files/w47/scratch-ja-fix-core1/FIX-LOG.md`
- 门日志：`hidden_files/w47/scratch-ja-fix-core1/GATE-LOG.md`
- 构建日志：`run1.log`、`run2.log`、`render.log`、`webpdf.log`（首次失败）、
  `webpdf2.log`（成功）、`freeze.log`、`occlusion.log`、`p8extract.log`
- 门输出：`svg-run1.sha`、`svg-run2.sha`、`ja-core-occlusion-fix1.json`、
  `ja-core-p8-fix1.json`、`registry-fix1.json`
- 对照：修前 text.md 副本 `textmd-prefixed.md`（供 diff 用）
- 工具：`export-textmd-core.py`（重建的 text.md 导出器）
- 渲染图：`render-print/p-*.png`（印刷 8 版）、`render-web/p-8.png`、
  `p8-key47-crop.png`（+ 网页版同名裁图，逐字节一致）
