# W47 步骤 2 watcher 报告（恢复协调员 #8 派单）

- 观察窗口：2026-11-13 10:28–11:09 UTC（约 41 分钟，未满 50 分钟上限）
- 结束条件：**B 达成**（edge 新鲜 130/130 + 聚合报告已生成）。A 未按字面达成（见下）。
- 角色：只读观察；未修复、未提交、未推送、未杀进程、未重跑任何门禁。

## 结论

**步骤 2 可闭合。**三门禁 130 版全量重跑完成，缺陷总数 **0**（spill 0 / boxtitle 0 / edge 0 TOUCH），聚合报告已生成。唯一的形式缺口：driver-final.log 全程未出现 `DRIVER_RC` 行（两次 driver 调用均未写该行），若闭合条件字面要求该行，需协调员确认是否以聚合报告为准。

## 最终聚合（直接数 per-edition JSON，不转述日志）

| 门禁 | 新鲜份数 | 缺陷 | 观察/边际 |
|---|---|---|---|
| spill sweep | 130/130（mtime > 2026-11-13 07:48 UTC，本轮 07:48 跑） | **0 SPILL** | observes 17280 |
| boxtitle | 130/130（mtime > 2026-11-13 07:48 UTC，本轮 07:48 跑） | **0 DEFECT** | marginal 6，observes 0 |
| edge（PDF 边缘扫描） | 130/130（mtime > 2026-11-13 09:01 UTC，本轮 09:01 + 11:00 两段跑） | **0 TOUCH** | NEAR 0，全部 status ok |
| U+201C 普查 | census-201c.json（2026-11-13 07:59 生成） | **0 defective** | 1359 个 “  glyphs，entity_hits 0，defective_editions [] |

- boxtitle marginal 6 版（均为 ≤1.0px 容差内，verdict MARGINAL）：2026-w47-es-de（0.7px）、2026-w47-de-ja（1.0px）、2026-w47-nl-it（0.6px）、core-de（1.0px）、2026-w47-de-fr（1.0px）、2026-w47-de-zh-tw（1.0px）。
- 驱动自带聚合：`aggregate.json`（2026-11-13 11:01:25 重写）：defects 0，observes 17286（= spill observes 17280 + boxtitle marginal 6），missing []。
- 聚合报告：`hidden_files/w47/Reports-preinsert/new-gates-130.md`，生成 2026-11-13 11:01 UTC，26640 字节，首行“生成：2026-11-13 11:01 UTC”。**注意路径**：报告写在 `Reports-preinsert/`，不在 `scratch-new-gates/`（任务所说的待写位置）；scratch 目录下无 new-gates-130.md。
- 残留一件：`per-edition/spill/` 共 131 个文件，多出 `2026-w47-zh-cn-en.json` 一个陈旧文件（不在 130 版清单内——zh-cn 无 en 读者版）；其内容无 SPILL，不影响计数。

## 与 16:07 基线对照

基线文件：`Reports-preinsert/new-gates-130-2026-11-12-1607.md`（实际生成 2026-11-12 01:54 UTC）。

| 项 | 基线 | 本轮 | 变化 |
|---|---|---|---|
| 缺陷总数 | 21 | **0** | −21 |
| spill | 1（2026-w47-ko-it p2 “kimchi”） | 0 | 已清零 |
| boxtitle DEFECT | 18 | 0 | 已清零 |
| boxtitle marginal | 见注 | 6 | 见注 |
| edge TOUCH | 2（it-es、it-pt，均为 P1 右缘 11px） | 0 | 已清零（it-es/it-pt 本轮重扫干净） |
| edge NEAR | 4（it-es 2、it-pt 2） | 0 | 已清零 |
| spill observes | 11516 | 17280 | +5764（观察项计数，非缺陷） |
| 总 observes | 11546 | 17286 | +5740 |

注：任务简报称基线“boxtitle 18 DEFECT / 7 marginal”，但基线报告文件逐版表的 marg 列全为 0，aggregate.json 亦已被本轮重写，**“7 marginal”一数在基线文件中无法核实**，特此标明。本轮实测 marginal 为 6。

## 过程记录（每次检查实测）

| 时间 (UTC) | driver 2058 | edge 2084 | edge 新鲜 | TOUCH/NEAR | 备注 |
|---|---|---|---|---|---|
| 10:28–10:30 | 活（CPU 累计 00:00:06） | 活（CPU 00:04:23，5.0%） | 90→91/130 | 0 / 0 | spill/boxtitle 已 130/130 新鲜（07:48 跑） |
| 10:39:52 | 活（00:00:06） | 活（CPU 00:04:51） | 101/130 | 0 / 0 | 约 1.1 分钟/版 |
| 10:49:59 | 活（00:00:06） | 活（CPU 00:05:11） | 110/130 | 0 / 0 | 剩余 20 版，预计 ~11:12 完成 |
| ~10:55–10:59 | **已死** | **已死** | 119/130（冻结） | 0 / 0 | **VM/运行时重启**：edge.log 末写 10:55:18；/tmp 被清空（watch 脚本与 ref 文件丢失，我的 sleep 检查亦丢失）；ps 查无 2058/2084 |
| 11:01:24–26 | —（新调用，已退出） | —（新调用，已退出） | 130/130 | 0 / 0 | **新 driver 调用** 10:59:57 inventory → 11:00:14 仅 11 版 stale → GATE edge 11 版 rc=0（70s）→ 11:01:25 pass 2 全新鲜 → aggregate → 11:01:26 报告写出 |
| 11:08:46 | 无 python 进程 | 无 python 进程 | 130/130 | 0 / 0 | 最终核实；仍无 DRIVER_RC，无 scratch 内报告 |

## Driver 状态与 DRIVER_RC

- 原 driver PID 2058（09:01 UTC 启动）与 edge PID 2084 在约 10:55–10:59 的运行时重启中被杀，**非正常退出**，driver-final.log 无 DRIVER_RC 行。
- 10:59:57 有一次新的 `run_all.py` 调用（同名日志续写）：只补跑剩余 11 版 edge（zh-cn-pt、zh-cn-ru、zh-tw-de/es/fr/it/ja/ko/nl/pt/ru），rc=0，聚合与报告均完成，随后退出；**该调用同样未写 DRIVER_RC 行**。
- 至 11:08:46 核实：无任何 run_all.py / pdf_edge_scan.py 进程存活；driver-final.log 末行仍为 11:01:26 的 report written 行；DRIVER_RC 全文 grep 计数 0。

## 还差什么

- 实质工作已全部完成：三门禁 130/130 新鲜、0 缺陷、聚合报告已生成。无待跑版、无缺失门禁结果（aggregate missing []）。
- 仅存形式项：`DRIVER_RC` 行从未出现。若步骤 2 的闭合只认报告与 JSON，则已可闭合；若硬性要求 DRIVER_RC，需由协调员决定是否补写/接受现状——watcher 按只读任务未做任何写入。
- 另两点如实记录（非阻塞）：U+201C 普查文件为 07:59 生成，本轮 driver 两次调用均未重跑 census（日志无 census 行），数字以该文件为准；spill 目录多一个陈旧的 `2026-w47-zh-cn-en.json`。
