# GATE-LOG — W47 zh-cn-pt 独立 re-proof（2026-11-11）

工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-zh-cn-pt1/`
生产：`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-pt/`（只读）
解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）
结论：**(a) 零缺陷**；唯一 FAIL 的第 14 门为已知预期项（网 PDF 旧版，见末）。

| # | 门 | 实测值 | 结果 |
|---|---|---|---|
| 1 | run.py 重建 | RC=0（`run-rebuild3.rc`=0）；TOTAL 150（A2 56 / B1 69 / B2 25；分页 10/18/18/18/18/18/12/38；类型 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1）；0 FLOW OVERFLOW；0 HEAD TOO WIDE；P7 teaser 2588.78；P8 keys 2552.7。日志 `run-rebuild.log` / `run-rebuild3.log` | PASS |
| 2 | SVG 重建 8/8 字节一致 | scratch 重建 SVG 与生产 SVG sha256 8/8 MATCH（p1–p8 全同；另 gates-zhcn 内 freeze repro 亦 8/8） | PASS |
| 3 | 重渲印 PDF 与交付逐字节相同 | 重渲 `rebuild/Lucerna-VOL4-PT.pdf` 41,734,802 B，SHA `6644cd43e033e99b27eb02f8bbaca9b470002eb40c9ebac12fed75a73cb7dccb` = 交付印 PDF；`cmp` 通过。日志 `render.log` | PASS |
| 4 | freeze 核心 baseline 8/8 | `freeze.py baseline --build core-zh-cn --core-svg core-zh-cn/svg` RC=0，8/8 OK；核心 SVG 完整性：重跑前后 8 文件 hash 不变。日志 `freeze-baseline.log`，`--core-svg` 指向核心 svg 子目录 | PASS |
| 5 | freeze diff --strict-cjk | TOTAL added CJK **0**（逐页 0/0/0/0/0/0/0/0；CJK 计数仅在英→葡替换处下降）。RC=0。日志 `freeze-diff.log` | PASS |
| 6 | occlusion 0 flags（自检六类全触发） | `occlusion_audit.py` RC=0，`0 flags`；自检 `BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX` 全部触发，干净对照静默。日志 `occlusion.log`。注：纯填色 `#f0eee5` 盒不在其 BOXTITLE 候选内，盒标题证据另见第 7/8 门 | PASS |
| 7 | 奶油盒纵+横双扫（PIL 真墨） | fix1 `sweep.py` 复跑 + 自写 `scan_all.py`：cream_flags **0**；每页最紧余量 P1 21.9 / P2 20.5 / P3 19.5 / P4 15.5 / P5 30.5 / P6 25.5 / P7 21.3 / P8（无奶油盒）。P1 数字盒 8 行正文最紧 30.5。`sweep-after.json` / `scan_all.json` | PASS |
| 8 | 盒标题横向真墨 + 交付 PDF 渲染像素（D-01~D-03） | PIL：P1 925.5/+35.5，P2 1382.0/+29.5，P5 912.5/+48.5（盒缘 961.0/1411.5/961.0）。像素（150 dpi 交付 PDF）：P1 922.9/960.6/+37.8，P2 1381.1/1410.6/+29.4，P5 912.6/960.6/+48.0。均 ≥+5 px 門限，与 fix1 声称逐值一致。裁图 `evidence-p1/p2/p5-title.png`（绿=墨，红=盒缘）目视在盒内。`pixels-after.json` | PASS |
| 9 | spill 扫 | 页界溢出 **0**（墨右缘 >1950 或 y 越界 0 项；`scan_all.json: spill_flags []`） | PASS |
| 10 | 孤儿扫（与核心逐项比对） | P1–P7 徽章集与核心逐页完全相同（10/14/14/14/14/14/12）；REG 有号无徽章 20 项 = 5 组 `match_set` 子项，核心同结构；**0 新增**。`keycheck.json: orphans` | PASS |
| 11 | p8 extract 150/150 | `p8.py extract` RC=0，`noted set = 150 of 150`。日志 `p8extract.log` | PASS |
| 12 | p8 compare CLEAN + keycheck 150/150 | `p8.py compare` RC=0，`status: CLEAN missing=[] extra_count=0 keydiff=[]`。REG 150 = 源码 AST 150，对齐 0 错位；键三方核对 149/150 自动通过，Q150 人工重组核实（P8 实印键与 REG note 逐字一致，范文 138 字，键流止 2552.7，无截断）→ **150/150**。配对 5 组键均为 a/b/c/d 排列。`keycheck.json` / `p8compare.log` | PASS |
| 13 | 印/网文字层 8 页 posdiff/msdiff | 见第 14 门（本门与之同一组实测；gates-zhcn `print_web_text` 明细：P1 385/386 pos216 ms2；P2 366/366 pos1 ms1；P3 282/282 0/0；P4 358/358 0/0；P5 283/285 pos211 ms1；P6 352/352 0/0；P7 532/532 0/0；P8 1879/1879 0/0；合计 pos428 ms4） | 预期 FAIL（第 14 门） |
| 14 | print_web_text 门 | **FAIL（预期）**：网 PDF 仍为 fix1 前旧版。逐词差分证明差异恰为三处旧标题：P1 print-only `Números, da` / web-only `Esta, em, números`；P2 `da` / `desta`；P5 `Palavras-chave` / `Palavras, da, semana`；其余 5 页 0/0。待全家统一重建网 PDF 后自愈；印 PDF 为权威终稿。`gates.log` | EXPECTED FAIL，非缺陷 |
| 15 | P8 最小字号 ≥9.75 pt | 答案区最小 **9.98 pt**，中位 9.98 pt，371 spans（印 PDF 与网 PDF 同值）。`gates.log: p8_fontsize` | PASS |
| 16 | §1.1 调色板 / 禁用色 / VOL.4 | `s11_svg`：off-palette {}；gold/old=False；stroked_rects 0；VOL.5=1（=核心 1 处，P7 下期预告合法）；paper `#fbfaf6` ×8；每版 VOL.4 各 1 处；U+2019 0（SVG + text.md + ABSTRACT.txt）；P8 chips A2 11 / B1 24 / B2 3 = 核心；img_overlap 0 hits；pdftotext 印 44,808 B / 网 44,820 B。`gates.log` / `gates-pt.json` | PASS |
| 17 | 日期 `date -d` 全验 + 固定核查 | 11-16 星期一 – 11-22 星期日；11-08 星期日、11-09 星期一、11-10 星期二（截稿）、11-15 星期日（决赛凌晨3点，与范文“星期日凌晨3点”一致）、11-21 星期六（`21 nov., sábado`）、11-22 星期日（小雪，`22 nov., domingo`）。“next Sunday”在本版与核心均不存在。D4/D5：`第一次` 恰 2 处均带限定；Q56 键注在位；`今年一场没输` 0 命中。#3 点全部存活（P4 C-head 339.0 px 称谓在位、P7 三头、P4 gloss 6 行、P2 词卡各 1 行、teaser 2588.78、keys 2552.7）。text.md 仅 3 行变化（:47/:271/:915；50,846→50,834 B）。 | PASS |

## gates-zhcn.py 11 子门汇总（`gates.log`，独立复跑）

PASS：occlusion / img_overlap / p8_extract / p8_compare / freeze_sha256 /
pdftotext_nonempty / p8_fontsize / p8_chips / u2019 / s11_svg（10 项）。
FAIL：print_web_text 1 项（第 14 门预期项）。OVERALL: FAILURES PRESENT 仅因该预期项。

## 证据文件（本工作区内）

- `PROOF-NOTE.md`（本轮结论与逐项证据）、`GATE-LOG.md`（本文件）
- `run-rebuild.log`、`run-rebuild3.log`（RC=0）、`run-rebuild3.rc`
- `render.log`（重渲印 PDF SHA 逐字节相同）
- `freeze-baseline.log` / `freeze-baseline.json`、`freeze-diff.log` / `freeze-diff.json`
- `occlusion.log`、`sweep-after.json`、`scan_all.log` / `scan_all.json`、`pixels-after.json`
- `p8extract.log`、`p8compare.log`、`reg.json`、`dump-reg.log`、`keycheck.log` / `keycheck.json`
- `gates.log`、`gates-pt.json`、`gates-zhcn.py`（复跑副本）
- `evidence-p1-title.png`、`evidence-p2-title.png`、`evidence-p5-title.png`（三处标题裁图，绿=墨右缘，红=盒缘）
- `full-p1-1.png`、`full-p8-8.png`（交付印 PDF 110 dpi 整页目视）
- `px/p1-1.png`、`px/p2-2.png`、`px/p5-5.png`（交付印 PDF 150 dpi 渲染底图）
- `rebuild/`（scratch 重建：run.py + 重渲印 PDF；生产 SVG 8/8 字节一致之对照）
