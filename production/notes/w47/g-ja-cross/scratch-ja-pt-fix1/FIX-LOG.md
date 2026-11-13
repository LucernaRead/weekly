# FIX-LOG — 2026-w47-ja-pt 第一轮返修（fix1 builder，叶子）

- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-pt/`（target 日本語，reader 葡萄牙文）
- 日期：2026-11-11（UTC 07:27–07:58）
- 依据：第一轮复校 `hidden_files/w47/scratch-proof-ja-pt1/PROOF-NOTE.md`（缺陷 D1）+
  任务单 grep 要求（力士罗马字）
- 开工探针：`git hash-object -w --stdin` 成功；goals hidden_files/w47/scratch-ja-pt-fix1/
  真实写盘成功（`.probe-stick`）。双通后动手。
- 范围：只改 `production/2026-w47/fanout-ja/2026-w47-ja-pt/` 内 content*.py +
  WEEKLY-KIT.md + EDITION-RECORD.md + 生成物（SVG/cards/双 PDF/text.md）；
  记录只写 goals hidden_files/w47/scratch-ja-pt-fix1/。未改 core-ja、未碰
  W43–W46、其他目标语家庭、tools/；未跑 insert.py、lint --write；
  未 git add/commit/push/reset/stash。

## 修前独立核实（D1）

- SVG 坐标：词框 rect x=88, y=1618, w=422.5, h=150（底边 1768）；
  释义行 1 基线 y=1752.06（框内），行 2 `prósperos` 基线 y=1776.76，
  超出底边 8.76px；下一行基线 y=1800，无重叠。属实。
- 宽度实测（svglib.wrap/text_w，19px Noto Sans CJK，wrap 宽 378.5px）：
  原释义 420.0px → 2 行；新释义 341.1px → 1 行。
- 修法：选 (a) 缩短释义（改动最小）。(b) 加高词框无空间：释义墨迹底
  ~1782.5，下一行墨迹顶 ~1782，任何能容下释义的框高都会顶到下一行。

## 改动逐处清单（源码 9 处，生成物随重建更新）

### F3 — D1（content12.py 1 处）
| 位置 | 改前 | 改后 |
|---|---|---|
| content12.py:222（words 表第 1 元组） | `um ancinho de bambu para negócios prósperos` | `ancinho de bambu para bons negócios` |
- 词框 rect 不变（h=150）。P8 注（#21）与配对选项中的完整释义不动
  （该处单行容得下，且为完整释义）。
- 结果：释义单行，基线 y=1752.06，框内；2× 裁图 `p2-words-fixed.png` 确认。

### F4 — 力士罗马字（content34.py 4 处、content7.py 1 处、content8.py 1 处）
公开来源核实：藤凌駕 ふじりょうが → **Fujiryōga**
（Sumowrestling Wiki / Hakkeyoi 写作 "Fujiryoga"，即 ryō 长音 ō，不是 ū）；
美ノ海 ちゅらのうみ → **Chura-no-umi**（葡文惯用连字符形；
EN Wikipedia "Churanoumi Yoshihisa"，日刊体育给出读音 ちゅらのうみ；
原 `Umi-no-umi` 漏掉 ちゅら，义为 "sea of sea"，错）。
| 位置 | 改前 | 改后 |
|---|---|---|
| content34.py:188（ex 48 注） | `Umi-no-umi perdeu contra Hōshōryū no primeiro dia` | `Chura-no-umi perdeu contra Hōshōryū no primeiro dia` |
| content34.py:190（ex 49 注） | `Fujiryūga bateu Hōshōryū no terceiro dia` | `Fujiryōga bateu Hōshōryū no terceiro dia` |
| content34.py:202（ex 54 注） | `Kinboshi de Fujiryūga: 11.º torneio desde a estreia` | `Kinboshi de Fujiryōga: 11.º torneio desde a estreia` |
| content34.py:224（ex 63 注） | `Fujiryūga ganhou um kinboshi no terceiro dia` | `Fujiryōga ganhou um kinboshi no terceiro dia` |
| content7.py:57（ex 111 注） | `Kinboshi de Fujiryūga: 11.º torneio desde a estreia` | `Kinboshi de Fujiryōga: 11.º torneio desde a estreia` |
| content8.py:22（ex 116 注） | `Hōshōryū perdeu contra Fujiryūga no terceiro dia` | `Hōshōryū perdeu contra Fujiryōga no terceiro dia` |
- 6 处全在葡文答案简析（note）内；日文正文/题干、答案键、题号均未动。
  p8 compare 仍 CLEAN，keydiff 仍恰为 [137, 138, 139, 140]。
- 修后全版 grep（SVG + .text.md + 源码）：`Fujiryūga` / `Umi-no-umi`
  均为 0 处（KIT §12 修复记录本身作为历史引用了旧拼写 3 处，不计）。

### F5 — 框题右溢出（重扫新发现，content12.py 1 处、content7.py 1 处）
- 来源：浅色框溢出重扫（`box-overflow-scan.py`，8 页全扫，1px 容差），
  除 D1 外另报 2 处真溢出，2× 裁图（修前渲染）确认标题尾落在白纸上：
  P1 数字框标题 `数字で見る今週　A semana em números` 439.2px，
  超出框右缘 34.66px；P7 框架框标题 `今週のフレーム　Estrutura da semana`
  417.6px，超出 17.14px。
- 根因：`bslib4.box()` / `p.text` 画框题不做宽度检查；冻结的日+中标题
  容得下，更长的葡文标题容不下。家族共性（de/fr/es/it 同位置同样超框），
  但每版按各自零缺陷门槛判断，本版照修。
- 修法：标题字号 23px → 21px，文字不动（23px 下无合适的葡文缩短形：
  唯一能入框的是 `Em números`，丢了 "week"；`Estrutura semanal` 虽能入框，
  但为与 P1 统一处理、保留原措辞，两处同用 21px）。
  | 位置 | 改前 | 改后 |
  |---|---|---|
  | content12.py:46 | `f.box("数字で見る今週　A semana em números", [...])` | 同上 + `tsize=21` |
  | content7.py:86 | `p.text(..., "今週のフレーム　Estrutura da semana", 23, ...)` | 字号 `21` |
- 结果：P1 标题 401.0px ≤ 404.5px，P7 标题 381.3px ≤ 400.5px，
  均入框；2× 裁图 `p1-numbox-fixed.png` / `p7-framebox-fixed.png` 确认。
  P1 box 高随 tsize 缩 2px（box() 高度公式含 tsize+10），该列后续内容
  上移 2px，版面余量充足，无连带影响（run.py 0 溢出，整版目视干净）。
- 未动项：3 处 0.29–0.92px `envia-nas.` 框底触线（P2/P3/P5）为首轮已裁定
  的量测噪声（O4），与核心版同位置中文末行一致（0.5px），不动。

## 构建（全部 rc 0）

- run.py：4 次（run1 D1+罗马字 → run2 freeze → run3 标题修 →
  run4 freeze），每次 exit 0、0 FLOW OVERFLOW / HEAD TOO WIDE，
  登记表 TOTAL 150（A2 48 / B1 73 / B2 29；分版 10/18/18/18/18/18/12/38；
  类型 completamento 50 / escolha múltipla 51 / relacionar 12 /
  construção de frases 8 / verdadeiro ou falso 11 / cloze 13 / tradução 4 /
  escrita 1）。
- render.py rc 0（cards PNG + 印刷 PDF）；webpdf.py rc 0；
  text.md 由重建的 `export-textmd-pt.py`（见下）导出。
- text.md 与修前 diff：恰为 8 处改动（D1 释义 2 行→1 行；
  注 48/49/54/63/111/116），其余逐字节相同。
- 导出脚本说明（已更正，见补记 F6）：原 `export-textmd-pt.py`
  并未丢失——它存活在 goals 侧 `scratch-fanout-ja/` 镜像里
  （丢的只是仓内副本）。fix1 重建版在用前已对修前 text.md 验过
  **逐字节相同**（46703 字节 / 1376 行）；补记时又跑原版脚本重导
  一次，与修后 text.md **逐字节相同**（46,696 字节），双重验证通过。

## 新双 PDF（终版，run3/run4 构建）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-JA-PT.pdf`（印版） | 29,103,009 | `9591f16cb82a2e2534f141febc1232632ee6cf02eefa64e84e9b74cb3601b8be` |
| `Lucerna-VOL4-JA-PT-web.pdf`（网版） | 4,485,030 | `f0cdce302756b0bf118dfaa432af9dfcaf9d66b9d17056adbeb688f26258645f` |
| `2026-w47-ja-pt.text.md` | 46,696（1375 行） | — |

作废旧版：印版 29,103,006 / `5e7542bc94e191e418fd49326676523e545aeb3eb2363d48c19c1cc6dcb33e56`；
网版 4,485,027 / `499149398ebed4848a02b2e8efcaaf9bbbbfe1c97effe651ffde8029d8a6629c`。
双 PDF 均为 8 页，1462.5 × 2025 pt。

## KIT / 记录更新

- `WEEKLY-KIT.md`：§7 补 F3/F4/F5 事实；§8 门禁全量更新为 fix1 实测；
  §11 F1 引文拼写同步更正；新增 §12（fix1 修复记录）。
- `EDITION-RECORD.md`：交付物表 + 门禁节更新为 fix1 实测；状态改为
  fix1 完成、待第二轮全量复校。

## 补记 F6 — 翻译表修正（2026-11-11 08:05 UTC，主报告发出后）

迟到的后台 `find` 结果定位到翻译表：`map-pt.json` 并不在仓内
`hidden_files/w47/scratch-fanout-ja/`（该处确实没有），而在 goals 侧
`hidden_files/w47/scratch-fanout-ja/` 镜像里（连同 `apply.py`、
原版 `export-textmd-pt.py`、全部日志）。该镜像当时未被列出，
主报告称"map 不在盘上"是错的，特此更正。

补查补修（只动 ja-pt 的表；en/ru 侧同名 `map-pt.json` 与其他家庭
的表一律未动）：
| 文件 | 改动 |
|---|---|
| `scratch-fanout-ja/map-pt.json` | `Fujiryūga`→`Fujiryōga` 4×（ex 49/54/63/111 注值）；`Umi-no-umi`→`Chura-no-umi` 1×（ex 48）；词条 `祈求生意兴隆的竹耙` 值改为 `ancinho de bambu para bons negócios`（与 F3 同款缩短，防重跑 re-apply 带回 D1）；另 3 个含该释义的值（ex 21 注、配对选项 b/c）有意保留完整释义，与成品质地一致；JSON 改后仍合法 |
| `scratch-fanout-ja/tm-pt.json` | `O novo komusubi é Umi-no-umi` → `O novo komusubi é Chura-no-umi` 1×；JSON 合法 |
| `scratch-fanout-ja/tm2-pt.json` | 同上 1×；JSON 合法 |

补验：ja-pt 现行机制文件（map/tm/apply/export）grep 两旧拼写均为 0 处。
未动：其他家庭的表与探针（`map-de/en/it.json`、`gen-map-it/ko.py`、
`build-map-nl.py`、`probe-p8short.py`、`probe-it-p8short.py`）同样带有
旧拼写，属跨家庭共性，超出本次范围，留待协调员决定是否全家扫；
历史探针 `probe-pt-p8short.py` 保留其 F1 时冻结的原注输入串
（一次性诊断，非现行门禁）。
本次补修不改任何交付物：双 PDF 与 text.md 的字节/SHA 与主报告一致
（原版导出脚本重导 text.md 逐字节相同，已验）。

## 待第二轮复校做的事（不由本 builder 做）

- 第二轮全量复校（协调员另派）：全文、150 键、8 版目视、机械门全套独立重跑。
