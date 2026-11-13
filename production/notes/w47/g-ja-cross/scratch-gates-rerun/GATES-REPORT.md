# W47 三门禁全量重跑报告（insert 前确认）

- 生成时间：2026-11-12 UTC（spill ~12:20–12:24；普查 ~12:25–12:27；boxtitle 12:27–12:56；
  edge 13:03–15:59，分三段断点续跑）。报告定稿 2026-11-12 ~16:00 UTC。
- 范围：`production/2026-w47/` 全部 130 版（119 fan-out 目录 + 12 core 目录，减 1 重叠）。
  重叠：`2026-w47-zh-cn-en` 同时以 fan-out 目录与 `core-zh-cn` 存在；两处 print/web PDF SHA 完全一致
  （web `7088ff06…`、print `f7b13153…`），按此前全量跑法（118 direct + 12 core）计一次，跑 `core-zh-cn`、
  跳过 fan-out 副本。另 `fanout-nl/` 下 10 个 `2026-w47-nl-*` 目录为旧 fan-out 副本（inode 不同），
  不在 119 之列，不跑。
- 枚举核对：`editions130.txt` 共 130 行；每版均有 `svg/`（8 页）且恰好 1 个 print PDF（非 web）。
- 工具 HEAD（开工记录）：`tools/boxtitle_check.py`、`tools/spill_sweep.py`、`tools/pdf_edge_scan.py`
  均在 commit `45ca73fc`（`tools: add three standing pre-insert gates`）。开工时
  `git status --porcelain tools/` 显示的改动（`tools/README.md`、`cover.mjs`、`occlusion_audit.py`、
  `p8.py`、`run_build.README.md`、`run_build.py` 已改；`d5_creambox_audit.py`、`head_check.py` 未跟踪）
  为此前已存在的工作区状态，三门禁脚本本身无改动。收尾复核见末节。
- 运行环境：一律 `~/workspace/weekly-git/tools/venv/bin/python`，永不用系统 python3。
- 磁盘：开工 `df` 93G 已用 / 57G 空闲（150G），低于 100G 停手线；门禁只读，日志小。
- 对照基线：2026-11-12 02:50–02:58 UTC run-log 记录的三门禁 21 处缺陷（spill 1 / boxtitle 18 / edge 2）
  均已修复 + 同步；D5 重建又改了全部 131 个生产目录，本次为最终版文件上的全量重跑。

## 方法

- boxtitle：`tools/boxtitle_check.py <版目录> --json-dir scratch-gates-rerun/boxtitle`
  （盒标题真墨溢出；DEFECT = 墨水超盒缘 >0.5px 且非 STRADDLE/同值观察项）。
- spill：`tools/spill_sweep.py <版目录> --json-dir scratch-gates-rerun/spill`
  （奶油盒整行溢出；SPILL = 同流续行判定成立）。
- edge：`tools/pdf_edge_scan.py <版目录> --json-dir scratch-gates-rerun/edge`
  （交付 print PDF 200dpi 光栅页缘扫描；TOUCH = 墨水进外侧 3px 带）。
- U+201C 普查：`scratch-gatefix-u201c-ru/census_quotes.py <各版 svg/>`
  （只认 Noto Sans CJK SC/TC/HK 内的 U+201C/U+201D/U+2019 为缺陷字）。

## 结论：(a) 130 版三门禁全绿 + U+201C 0 缺陷

- boxtitle：130/130 PASS，0 DEFECT / 0 OBSERVE / 7 marginal（≤1.0px 容差内，无裁切重叠）。
- spill：130/130 PASS，SPILL 合计 0（16,544 候选全为 OBSERVE）。
- edge：130/130 PASS，TOUCH 合计 0，NEAR 0 页。
- U+201C 普查：GRAND TOTAL defective: 0。
- 缺陷清单：无。21 处旧缺陷（spill 1 / boxtitle 18 / edge 2）已全部清除，无新缺陷。
  本轮未修复任何生产文件（只读核验）。

## spill 全量结果

- 130/130 版 JSON 齐全，`spills` 合计 0；全部 130 版 rc=0。
- OBSERVE（近邻候选，非缺陷）每版数量见 `spill/*.json`；对照基线：ko-it P2 `kimchi` +8.76px
  溢出已清除（本轮 ko-it 0 SPILL）。
- 原始日志：`spill-all.log`；逐版 JSON：`spill/<slug>.json`。

## U+201C 普查全量结果

- 130 个 `svg/` 目录全扫，`census_quotes.py` rc=0，`GRAND TOTAL defective: 0`。
- 无任一文件 `defective>0`。Noto Sans CJK SC/TC/HK 内 U+201C/U+201D/U+2019 均为 0。
- 原始日志：`census-all.log`（130 个 `== <dir> ==` 节，每节 `TOTAL defective: 0`）。

## boxtitle 全量结果

- 130/130 版 JSON 齐全，共 5,156 titles + 61,254 body lines；**0 DEFECT，0 OBSERVE，7 marginal**；
  全部 130 版 rc=0。
- 7 处 marginal（均为右缘超盒 ≤1.0px，属工具容差内 `MARGINAL`，非 DEFECT；无裁切、无重叠）：
  - `2026-w47-de-fr` P7 TITLE `Outils` +1.0px（core 同值 +1.0，继承非回归）
  - `2026-w47-de-ja` P7 TITLE `　道具箱` +1.0px（core 同值 +1.0，继承）
  - `2026-w47-de-zh-tw` P7 TITLE `　工具箱` +1.0px（core 同值 +1.0，继承）
  - `2026-w47-es-de` P1 TITLE `KURZNACHRICHTEN` +0.7px（core −22.0）
  - `2026-w47-ja-ru` P7 TITLE `Структура недели` +0.8px（core −22.0）
  - `2026-w47-nl-it` P6 TITLE `DATI INVENTATI` +0.6px（core −22.0）
  - `core-de` P7 TITLE `　工具箱` +1.0px（core 自身）
- 对照基线：21 处旧缺陷中的 18 处 boxtitle（de/es/fr/ko/nl/pt/ru/en 各 P1、it-ru P2 `ЗАПОМНИТЕ` +63.5、
  ja 9 处）本轮全部 0 DEFECT，已清除；无新 DEFECT。
- 原始日志：`boxtitle-all.log`；逐版 JSON：`boxtitle/<slug>.json`。

## edge 全量结果

- 130/130 版 JSON 齐全（1,040 页），**0 TOUCH，0 NEAR**；全部 130 版 status=ok，rc=0。
- 最紧的 5 处页缘余量（min_dist，pt；均未触线）：
  - `2026-w47-it-en` P1：right 5.4 / left 6.1（基线已知近点 it-en 6.1/5.4，未触）
  - `2026-w47-de-en` P6：right 7.9
  - `2026-w47-it-nl` P1：right 7.9 / left 9.0（基线已知近点 it-nl 9.0/7.9，未触）
  - `2026-w47-it-es` P1：right 10.1 / left 11.5（基线为 TOUCH 0.0——已修好）
  - `2026-w47-it-pt` P1：right 10.1 / left 11.5（基线为 TOUCH 0.0——已修好）
- 对照基线：21 处旧缺陷中的 2 处 edge（it-es / it-pt P1 右缘 36pt strap 末字 `A` 被页边裁切）
  本轮均为 0 TOUCH，已清除；无新 TOUCH。
- 执行过程：edge 驱动被两次 VM/运行期重启杀掉（~13:28–13:29 与 ~15:28–15:30 UTC），每次均按 JSON 断点续跑
  （38/130 → 57 → 71 → 86 → 100 → 110 → 126 → 130/130），最终驱动 rc=0，
  `driver done 2026-11-12T15:59:17Z gate=edge`。无一版因重启漏跑或重跑覆盖——JSON 逐版齐全。
- 原始日志：`edge-all.log`；逐版 JSON：`edge/<slug>.json`（TOUCH 页才有 crops/，本轮 0 页故无）。

## 逐版结果总表

| 版 | boxtitle | spill | edge | U+201C |
|---|---|---|---|---|
| 2026-w47-de-en | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 7.9pt) | 0 |
| 2026-w47-de-es | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 47.5pt) | 0 |
| 2026-w47-de-fr | PASS (0D/0O/1M) | PASS (0) | PASS (0T/0N, min 47.5pt) | 0 |
| 2026-w47-de-it | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 47.5pt) | 0 |
| 2026-w47-de-ja | PASS (0D/0O/1M) | PASS (0) | PASS (0T/0N, min 47.5pt) | 0 |
| 2026-w47-de-ko | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 47.5pt) | 0 |
| 2026-w47-de-nl | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 47.5pt) | 0 |
| 2026-w47-de-pt | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 47.5pt) | 0 |
| 2026-w47-de-ru | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 47.5pt) | 0 |
| 2026-w47-de-zh-tw | PASS (0D/0O/1M) | PASS (0) | PASS (0T/0N, min 47.5pt) | 0 |
| 2026-w47-en-de | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.3pt) | 0 |
| 2026-w47-en-es | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-en-fr | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 49.3pt) | 0 |
| 2026-w47-en-it | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 42.5pt) | 0 |
| 2026-w47-en-ja | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-en-ko | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-en-nl | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 44.3pt) | 0 |
| 2026-w47-en-pt | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-en-ru | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 39.2pt) | 0 |
| 2026-w47-en-zh-tw | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-es-de | PASS (0D/0O/1M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-es-en | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-es-fr | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-es-it | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 48.2pt) | 0 |
| 2026-w47-es-ja | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-es-ko | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-es-nl | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-es-pt | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-es-ru | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-es-zh-tw | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-fr-de | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-fr-en | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-fr-es | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-fr-it | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-fr-ja | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-fr-ko | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-fr-nl | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-fr-pt | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-fr-ru | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-fr-zh-tw | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-it-de | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-it-en | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 5.4pt) | 0 |
| 2026-w47-it-es | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 10.1pt) | 0 |
| 2026-w47-it-fr | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 47.5pt) | 0 |
| 2026-w47-it-ja | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-it-ko | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-it-nl | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 7.9pt) | 0 |
| 2026-w47-it-pt | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 10.1pt) | 0 |
| 2026-w47-it-ru | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-it-zh-tw | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-ja-de | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ja-en | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ja-es | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ja-fr | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ja-it | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ja-ko | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-ja-nl | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ja-pt | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ja-ru | PASS (0D/0O/1M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ja-zh-tw | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-ko-de | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ko-en | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 38.5pt) | 0 |
| 2026-w47-ko-es | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 51.1pt) | 0 |
| 2026-w47-ko-fr | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 51.8pt) | 0 |
| 2026-w47-ko-it | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 50.8pt) | 0 |
| 2026-w47-ko-ja | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-ko-nl | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ko-pt | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ko-ru | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ko-zh-tw | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-nl-de | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-nl-en | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-nl-es | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-nl-fr | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-nl-it | PASS (0D/0O/1M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-nl-ja | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-nl-ko | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-nl-pt | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-nl-ru | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-nl-zh-tw | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-pt-de | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-pt-en | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-pt-es | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-pt-fr | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-pt-it | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-pt-ja | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-pt-ko | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-pt-nl | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-pt-ru | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-pt-zh-tw | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-ru-de | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-ru-en | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 45.0pt) | 0 |
| 2026-w47-ru-es | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ru-fr | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 15.1pt) | 0 |
| 2026-w47-ru-it | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-ru-ja | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-ru-ko | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-ru-nl | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 29.2pt) | 0 |
| 2026-w47-ru-pt | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 49.3pt) | 0 |
| 2026-w47-ru-zh-tw | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-zh-cn-de | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-zh-cn-es | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-zh-cn-fr | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-zh-cn-it | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-zh-cn-ja | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-zh-cn-ko | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-zh-cn-nl | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-zh-cn-pt | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-zh-cn-ru | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-zh-tw-de | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-zh-tw-es | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-zh-tw-fr | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-zh-tw-it | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-zh-tw-ja | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-zh-tw-ko | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| 2026-w47-zh-tw-nl | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-zh-tw-pt | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| 2026-w47-zh-tw-ru | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 53.6pt) | 0 |
| core-de | PASS (0D/0O/1M) | PASS (0) | PASS (0T/0N, min 47.5pt) | 0 |
| core-en | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| core-es | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| core-fr | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| core-it | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| core-ja | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| core-ko | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| core-nl | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| core-pt | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| core-ru | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| core-zh-cn | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |
| core-zh-tw | PASS (0D/0O/0M) | PASS (0) | PASS (0T/0N, min 54.0pt) | 0 |

## 收尾复核

- tools 状态：开工时三门禁脚本均在 commit `45ca73fc`；收尾复核 `git log --oneline -1 -- <三脚本>`
  仍为 `45ca73fc`，`git diff 45ca73fc b9ac29a6 -- <三脚本>` 为空——中途落盘的 commit `b9ac29a6`
  （2026-11-12 12:35:12 UTC，`tools: D5 gates + p8/occlusion/cover/run_build fixes`）只改了另外 8 个
  tools 文件（README.md、cover.mjs、d5_creambox_audit.py、head_check.py、occlusion_audit.py、p8.py、
  run_build.README.md、run_build.py），三门禁脚本字节未动，故受影响的检查为 0、无需重跑。
  收尾 `git status --porcelain tools/` 为空（上述改动已被该 commit 收走）。
- 磁盘：开工 93G 已用；收尾 94G 已用 / 56G 空闲，全程低于 100G 停手线。
  本次日志总计 12M（390 个 JSON + 4 份全量日志 + 报告 + 驱动脚本），只写在
  `hidden_files/w47/scratch-gates-rerun/` 内。
- 未做事项（按任务硬约束）：未修复/重建/改动任何生产文件；未碰其他周；未 reset/stash/add/commit/
  push；未跑 lint。`fanout-nl/` 旧副本与 `fanout-zh-tw/.probe` 未动。
- 原始证据：`editions130.txt`（130 版枚举）、`boxtitle-all.log`、`spill-all.log`、`edge-all.log`、
  `census-all.log`、`driver.log`、`run_gate.sh`、`boxtitle/*.json`、`spill/*.json`、`edge/*.json`
  （各 130 个）、`table-partial.tsv`、`table-full.md`。


