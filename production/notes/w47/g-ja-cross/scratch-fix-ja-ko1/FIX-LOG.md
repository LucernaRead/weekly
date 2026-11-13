# FIX-LOG — W47 ja-ko 第一轮返修（fix1, builder）

- 返修员：fix1；日期 2026-11-11（UTC）
- 复校对象：`production/2026-w47/fanout-ja/2026-w47-ja-ko/`
- 复校笔记：`hidden_files/w47/scratch-proof-ja-ko1/PROOF-NOTE.md`（proof1，3 条缺陷 D1/D2/D3）
- 任务红线遵守：只改本版目录、ko map 源（`scratch-fanout-ja/map-ko.json`、`gen-map-ko.py`，本版专用）与本笔记目录；未碰 core-ja、其他家庭、tools/、issues/；未跑 insert.py、lint --write；无 git 写操作；未派 subagent。

## 0. 成品身份核实（动手前盘上实测）

| 交付物 | 字节 | SHA-256（实测） |
|---|---|---|
| print `Lucerna-VOL4-JA-KO.pdf` | 28,189,461 | `fbcfe840f569ff521fb4aed509a441b8375a01b792f329fdc0a0bda2689437bc` |
| web `Lucerna-VOL4-JA-KO-web.pdf` | 4,550,459 | `d52edd4e6be8a2b3fa7c3115155e07e6cde028aa7dceaa723fea34bb365c27ac` |
| `2026-w47-ja-ko.text.md` | 47,721 | — |

任务简报所给两枚 SHA 标注互换，实测与 KIT §8、EDITION-RECORD 一致，以实测为准。
探针：PROBE1 `git hash-object -w` OK（`da0c4eb8…`）；PROBE2 笔记目录写盘 OK；`df` 45G 可用；全程无 EDQUOT。

## 1. D1 + D2 — 人名转写（map 值 5 处 + 键 1 处）

源头文件不在版目录内，在 fan-out 工作目录
`hidden_files/w47/scratch-fanout-ja/`（本版 ko 专用；重 apply 即由此生成版目录）。
`map-ko.json` 原有 4 个值含 `후지류가`（在 content 文件里出现 5 次：content34.py L190/202/224、
content7.py L57、content8.py L22——其中「金星是初登场后第11个场所」一值被 content34 与
content7 两处共用），1 个值含 `기하라 류치`（content56.py L109）。

改法（先改 `gen-map-ko.py` 的 T 表，再跑它重生成 `map-ko.json`，保证两者同步）：
- `후지류가는 3일째에 호쇼류를 이겼어요` → `후지료가는 3일째에 호쇼류를 이겼어요`
- `후지류가는 3일째에 긴보시를 땄어요` → `후지료가는 3일째에 긴보시를 땄어요`
- `후지류가의 긴보시는 데뷔 후 11번째 장소였어요` → `후지료가의 긴보시는 데뷔 후 11번째 장소였어요`
- `호쇼류는 3일째에 후지류가에게 졌어요` → `호쇼류는 3일째에 후지료가에게 졌어요`
- `ryuuryuu는 미우라 리쿠와 기하라 류치의 페어예요` → `ryuuryuu는 미우라 리쿠와 기하라 류이치의 페어예요`
- 生成器自检：missing translations 0，221 keys。

与原 map 的 diff：恰 6 处值改动（另见 §1b 键修复 1 处）。

## 1b. 附带发现（fix1 修，proof1 未列）：map 键错字致 #47 漏译

重 apply 时 `apply.py ko` 报 `1 PROBLEMS: MAP key never occurs quoted in core:
'首日战胜大之里的是一之富士'`。核查：
- map-en.json 第 221 键（含 ko 继承）把核心原文「义之富士」错写成「一之富士」，
  apply 的逐字替换永不命中；旧版 content34.py:186 靠人工手补才译成韩语
  （旧 text.md #47 为 `요시노후지는 1일째에 오노사토를 이겼어요`，proof1 复核无误），
  但凡重 apply 就会把 #47 打回中文（apply 后实测 content34.py:186 已是中文原文）。
- 其余 10 个 ja 家庭同题均已译（en/de/fr/es/it/pt/nl/ru/zh-tw 的 content34.py:186 皆为译文），
  唯 ko 的 map 键带此错字。
- 修法：`map-ko.json` 第 221 键 `首日战胜大之里的是一之富士` → `首日战胜大之里的是义之富士`
  （值不变）；`gen-map-ko.py` 加 `KEY_FIX` 映射，使重生成不再丢修；未碰 `map-en.json`
 （他家庭源文件，不属本版）。重生成后 keys 仍 221，missing 0。
- 重 apply 后 `APPLY ko: OK`（0 problems），content34.py:186 已为
  `요시노후지는 1일째에 오노사토를 이겼어요`。
- 附带后果（apply.py 设计如此，先记于此）：apply 会 `shutil.rmtree` 整个版目录再从
  core 重拷，因此版内手写文档 `WEEKLY-KIT.md`、`EDITION-RECORD.md` 及已交付的
  PDF/text.md/cards 一并被清。PDF/text.md/cards 已按 KIT §9 管线全数重建（见 §2）；
  两份手写文档按本轮开工时逐字读到的原文重建（见 §4），内容不变，只更新 §8 门禁数
  与 §11 fix 记录；重建件与原值逐项核对过，见 FIX-LOG §4。

## 2. D3 — P5「あなたは？」框句号孤悬

- 框内韩语提示 3 行，第 3 行仅 `.`（旧 SVG 基线 y=1473.57/1501.97/1530.37）。
- 修法：`map-ko.json` / `gen-map-ko.py` 同步改值——`…써서 보내 주세요.` → `…써서 보내주세요.`
  （去一空格，붙여쓰기，句意不变；`svglib.wrap()` 事先实测 20px/sans、宽 CW−44=378.5 时由 3 行变 2 行，
  句号贴回第 2 行末）。P2/P3 同类框的 `보내 주세요.` 未动（proof1 核实其句号本就贴尾）。
- 重建后实测：P5 提示 2 行（基线 y=1473.57/1501.97），末行止于 `…보내주세요.`；
  P5 col3 ends 1506.45（练习区固定起于 1580，无挤压）。

## 3. 重建（KIT §9 管线）

- `apply.py ko` → OK（0 problems，见 `apply-ko-fix1b.log`；首次 apply-ko-fix1.log 的 1 problem
  即 §1b，已修）。
- `run.py`（fix1 run1）：exit 0，0 FLOW OVERFLOW / HEAD TOO WIDE，TOTAL 150
  （A2 48 / B1 73 / B2 29；按页 10/18/18/18/18/18/12/38；类型与旧版一致）。
- `run.py`（fix1 run2，冻结重跑）：exit 0，0 溢出；两次构建 8 SVG sha256 8/8 相同
  （`ko-sha-fix1-run1.txt` vs `ko-sha-fix1-run2.txt`）。
- `render.py`：8 张 cards + print PDF 重建。
- `tools/webpdf.py svg Lucerna-VOL4-JA-KO-web.pdf`：见 §5（新 web SHA/字节）。
- `export-textmd-ko.py`：text.md 重导出，见 §5。

## 4. 手写文档重建（apply 清目录所致，见 §1b）

- `WEEKLY-KIT.md`：按本轮开工时读到的全文逐字重建，只改 §8（新 SHA/字节/门禁日志名）
  与 §11（追加 F2 fix1 记录）；其余章节（§1–§7、§9、§10、F0/F1）一字未动。
  重建后与原 KIT 逐节核对：规格/题量/图片/趋势/承诺/复现命令皆与原文一致。
- `EDITION-RECORD.md`：按开工时读到的全文重建，更新 Deliverables/Gates 两节为 fix1 新值；
  原文末行关于 P2/P4 栏中空白的一句按 proof1 §3.2 同义表述补全（原读数被截断处）。
  该文件是协调员审计记录，非构建者原文；proof2/协调员复核时请以本 FIX-LOG 为据再验。

## 5. 新成品身份（fix1 重建后实测）

| 交付物 | 字节 | SHA-256 |
|---|---|---|
| print `Lucerna-VOL4-JA-KO.pdf` | 28,189,450 | `8c6b7566e6efe7d94beae5bf10b6382970a93b3b71708688d3d27dbb7f39f177` |
| web `Lucerna-VOL4-JA-KO-web.pdf` | 4,550,444 | `133f57264a824575af7336c6e1198c4992211fa45bf8c82d96dfd89e840f3368` |
| `2026-w47-ja-ko.text.md` | 47,722 | `b20d5bc686ff94773bbd9a63980bc8672bd98d7d504328bfa4da51bca3ccb8af` |

双 PDF 均为 8 页。变化量与改动相符：print −11 B、web −15 B、text.md +1 B
（`이` +3、D3 去空格 −1、D3 并行 −1 换行）。text.md 1329 text 行 / 1356 文件行
（原 1330/1357，D3 并掉一行所致）。`ABSTRACT.txt` 296 B 未变。
SVG 变化面：仅 p5（D3）与 p8（D1/D2/#47）；与 proof1 交付 SVG 指纹逐页比对，
p1/p2/p3/p4/p6/p7 六页逐字节一致。

## 6. EDQUOT 事件（写 EDITION-RECORD 时）

- 现象：写 `EDITION-RECORD.md` 时报 Disk quota exceeded（Errno 122）；此时
  `df` 仍显示 45G 可用——属配额封顶，非磁盘满（与 AGENTS.md 2026-11-10 条目同类）。
- 处理（按任务令）：立即停手；只删本笔记目录内可复现的中间件——4 份 pdftotext
  提取文本（`print-plain.txt`/`web-plain.txt`/`print.txt`/`web.txt`，约 280KB，
  可由双 PDF 随时重提；字节数 47,998/91,550 已记入 GATE-LOG）；未动任何他处文件，
  未删日志/备份/证据 JSON。
- 重试一次即成功（`EDITION-RECORD.md` 4,217 B 落盘）。KIT（12,408 B）在 EDQUOT 前已写好。
- 提醒协调员：配额已近顶（并行 16 线同写），后续 proof2/入仓前宜先清已推旧中间件。
