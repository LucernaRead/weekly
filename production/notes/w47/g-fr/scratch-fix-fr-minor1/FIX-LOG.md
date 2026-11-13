# FIX-LOG — W47 fr 家全新一轮重校 minor1 修复（发现 1/2 + fr-en 轻微）

- 日期：2026-11-13（UTC 03:47–04:00）
- 修复工人：协调员 #4 派（23bd0de5）
- 任务依据：run-log.md 2026-11-13 ~03:43 UTC 条；重校工人 27bf5531（§8.4 round 2）结论 NOT CLEAN——2 项中等 + 1 项轻微，8 版 CLEAN。
- 约束遵守：**未 commit、未 push、未跑 lint**；只动 fr-ru / core-fr / fr-en 3 版，未碰其他 8 版与其他家庭。
- 工作目录：`hidden_files/w47/scratch-fix-fr-minor1/`（本日志、pre-shas.txt、pre-textmd/、pre-svg/、diffs/、run_all.sh、ru 溢出证据 ru-p1-overflow-crop.png / ru-overflow-shas.txt、修后卡面 core-p3-after.png / en-p5-after.png）。
- 工具链：`~/workspace/weekly-git/tools/venv/bin/python`；门禁驱动 `scratch-d5-rebuild-fr/run_gates.sh`（tag minor1；ru 回退 tag minor1-revert）；fan-out 导出器 `scratch-fanout-fr/export_lang.py`；core 导出器 `scratch-fr/export47.py`。
- 修前基线（盘上实测，见 pre-shas.txt，与 run-log 核对一致）：core 印 `45745d5874df` / 网 `9b66c0f91a68` / 文 `9334d70437d3`；en 印 `b227430a9e54` / 网 `167410e0620c` / 文 `f03b13d44104`；ru 印 `ade6694fcd1a` / 网 `9de461db64ed` / 文 `69d348831b05`。

## §1 逐项修法

### 发现 1（fr-ru，中等）—— P1 kicker 法语行缺 MERCREDI → 恢复后超宽，未硬塞，已回退，待协调员裁定

- 源：`2026-w47-fr-ru/content12.py:28`。旧：`ALCARAZ GAGNE PARIS, LE SÉNAT VOTE`（29 个非空字符）；试验态：`ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI`（37 个非空字符，与其余 10 版一致）。
- 试验过程：恢复 → 重出 text.md（diff 恰 1 行 L19）→ 重渲 → 全套门禁（logs-minor1）。
- **实测数据（超宽确证，三重证据一致）：**
  1. PIL 真墨实测（ru2 `measure3.py` 同款方法，同一套字体计量，ru2 曾以此法复现 audit 至 0.3px）：头条墨宽 1293.0px，墨右缘 x=1411.0；俄语 gloss `band_r1`（`АЛЬКАРАС ПОБЕДИЛ　ГОЛОСУЕТ В СР.`）墨左缘 1302.5 → **重叠 108.5px**。无 MERCREDI 时墨右缘 1124.0，净空 +178.5px。
  2. occlusion 门禁实测：1 TEXTX flag——`p1-une.svg 'ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI' — ink overlaps 'АЛЬКАРАС' by 108.2x19.8px`，与 ru2 修前实测值（−108.5/−108.2）逐位一致。boxtitle 门 0 DEFECT（该 kicker 行不在 boxtitle 检查范围内，occlusion 为 catches 它的门）。
  3. P1 卡面目视（`ru-p1-overflow-crop.png`，印 PDF 渲染）：MERCREDI 白字直接压在金色俄语 gloss `АЛЬКАРАС ПОБЕДИЛ　ГОЛОСУЕТ В СР.` 之上，肉眼可见重叠。
  4. 为何其余 10 版能放下：其 gloss 墨左缘均 ≥1450（en 1556.4、core/zh-tw 1450.0、de 1571.6），净空 ≥+39px；唯 ru 的西里尔 gloss 最宽（墨左缘 1302.5）。栏宽/字号全家同一套，ru 的 gloss 是唯一变量。
  5. 溢出试验件 SHA（内容已回退，见下）：印 `f415b89bd708…` / 17,222,519 B、网 `cc8d46847690…` / 1,774,111 B、文 `b435423835af…` / 50,702 B（`ru-overflow-shas.txt`）。
- **处理：未硬塞，已回退。**按任务书"超宽须报实测数据由协调员裁定，不许擅自再缩短或改写"，源已恢复为 fixfam1 态（头条仍缺 MERCREDI），并以 minor1-revert 全套重建 + 全套门禁重跑（logs-minor1-revert）：text.md diff vs 修前 0 行；印 PDF SHA 与 fixfam1 逐字节一致（`ade6694fcd1a…`，17,222,512 B）；text.md SHA 与 fixfam1 一致（`69d348831b05…`，50,693 B）；门禁全绿（见 §3 ru-revert 条）。**发现 1 未闭合，待协调员裁定**，选项：(a) 接受现状并在 KIT 书面记录缩短理由（本次重校的指控点之二）；(b) 缩短俄语 gloss `band_r1`（KIT 预检曾删 `СЕНАТ` 的先例）以腾出 ≥108.5px；(c) 缩小 kicker 字号；(d) 接受重叠。
- 附带发现（已记录在 ru KIT）：网 PDF 构建非确定性——同一内容三次构建三次 SHA 不同（fixfam1 `9de461db64ed…` 1,774,107 B → 溢出试验 `cc8d46847690…` 1,774,111 B → 回退 `4acb91b39968…` 1,774,094 B），而印 PDF 同一内容可逐字节复现（`ade6694fcd1a…` 两次一致）。回退后的网 PDF 文字层与印 PDF 逐字节一致（96,948 字符），内容无差；ru KIT 网 PDF 行已更新为回退后的实测值 `4acb91b39968…`。

### 发现 2（core-fr，中等偏轻）—— P3 BEAUJOLAIS 盒子桥接行 gloss 错误 → 已修，全绿

- 源：`core-fr/expl.py:95` `bridge_dieppe`。旧：`博若莱新酒小测　博若莱新酒小题。`；新：`微练习　博若莱新酒小测。`
- 选词理由：首节取 MICRO-DRILLS gloss `微练习`（与本版 `head_micro`/`head_micro6` 一致）；次节取盒子 gloss `博若莱新酒小测`，与兄弟版 `<MICRO-DRILLS gloss>　<盒子 gloss>` 结构一致（en "Quick drills　the Beaujolais Nouveau quiz."、zh-tw "微練習　薄酒萊小測。"）；次节与盒子标题 gloss `博若莱小题`（`head_dieppe_ex`）不重复——故取 `小测` 而非 `小题`。
- 共用源核查：`bridge_dieppe` 各版独立存在于自家 `expl.py:94/95`，其余 10 版原已是正确结构（逐版 grep 核实：de/en/es/it/ja/ko/nl/pt/ru/zh-tw 均为 `<MICRO>　<盒子>` 形），**只改 core 一处，无跨版影响**。

### 轻微（fr-en）—— P5 `An old coat's new owner` 窄化 → 已修，全绿

- 源：`2026-w47-fr-en/expl.py:128` `debat5_note`。旧：`Cinema or home? An old coat's new owner — or the bin?`；新：`Cinema or home? An old garment's new owner — or the bin?`（取单数 garment，与单数 `un vieux pull` / core "一件旧衣服" 对应；未取 `Some old clothes'`）。
- 同源两处：该字符串在 text.md 出现两次（L633 P5 讨论框、L673 LE DÉBAT 栏），均已改（diff 2 行）。

## §2 每版改前 / 改后（尺寸 + SHA-256 前 12；全 SHA 见各版 WEEKLY-KIT.md）

| 版 | 印 PDF 改前 → 改后 | 网 PDF 改前 → 改后 | text.md 改前 → 改后 | text.md diff（vs 修前） |
|---|---|---|---|---|
| core-fr（zh-cn） | 18,488,281 `45745d5874df` → **18,488,886 `8809c4bae4b6`** | 1,989,187 `9b66c0f91a68` → **1,989,709 `c024e0ad6061`** | 46,565 `9334d70437d3` → **46,553 `5416a602158f`**（39,355→39,351 字符） | 恰 1 行（L383 桥接行） |
| fr-en | 17,031,841 `b227430a9e54` → **17,031,843 `8ffde4f87863`** | 1,623,184 `167410e0620c` → **1,623,186 `271926332039`** | 46,274 `f03b13d44104` → **46,280 `4029e89a87ec`**（44,220→44,226 字符） | 恰 2 行（L633/L673，同源） |
| fr-ru（回退后） | 17,222,512 `ade6694fcd1a` → **17,222,512 `ade6694fcd1a`（不变）** | 1,774,107 `9de461db64ed` → **1,774,094 `4acb91b39968`**（重建 artifact，内容一致） | 50,693 `69d348831b05` → **50,693 `69d348831b05`（不变）** | 0 行 |

## §3 门禁复核结果（逐版；日志在 `scratch-d5-rebuild-fr/<版>/logs-minor1/`，ru 回退另见 `logs-minor1-revert/`）

注：`run_gates.sh` 的 FAILFLAG 只反映 run/render/webpdf 返回码，以下结论以各工具日志为准。

- **core-fr — 全绿**：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心与 vs 修前基线，keydiff=[]）；boxtitle 0 DEFECT（40 titles）；creambox PASS 0 defects；spill 0（102 OBSERVE，均为已知 below-box 提示）；edge 0 TOUCH / 0 NEAR；census PASS（0/0/0）；freeze diff +0 CJK / +0 Latin（与 fixfam1 一致）；印/网文字层逐字节一致（各 100,857 字节，94,229 字符，multiset 0）；P8 最小字号 11.62pt（858 spans，与 fixfam1 一致）；逐页 SVG 哈希：仅 p3-culture.svg 变；「　」计数不变（text.md 392）；P3 卡面目视通过（桥接行 `微练习　博若莱新酒小测。` 在栏内干净，盒子标题 `BEAUJOLAIS　博若莱小题` 未动）。
- **fr-en — 全绿**：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心 keydiff=[150] 已知 Q150，vs 修前基线 keydiff=[]）；boxtitle 0 DEFECT（34 titles）；creambox PASS 0 defects；spill 0（102 OBSERVE）；edge 0 TOUCH / 0 NEAR；census PASS（0/0/0）；freeze diff CJK 16 / Latin 521（与 fixfam1 一致，跨版 wholesale 值，非 FAIL 判据）；印/网文字层逐字节一致（各 101,484 字节，100,262 字符，multiset 0）；P8 最小字号 11.62pt（514 spans）；逐页 SVG 哈希：仅 p5-jeunesse.svg 变；P5 卡面目视通过（两处 `An old garment's new owner — or the bin?` 均在栏内干净）；印 PDF 文字层新串 ×2、旧串 `old coat` ×0。
- **fr-ru（溢出试验，logs-minor1）— 除 occlusion 外全绿**：run.py TOTAL 150、0 FLOW OVERFLOW、1 HEAD TOO WIDE（[P7-outils]，fix-ru2 已记录的修前已存在项）；**occlusion 1 flag TEXTX（108.2×19.8px，见 §1）**；p8 extract 121/150、compare CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；boxtitle 0 DEFECT（53 titles）；spill 0（151 OBSERVE）；edge 0 TOUCH / 0 NEAR；census PASS；印/网文字层逐字节一致（96,882 字符，multiset 0）；creambox FAIL 3 defects（与 fix-ru2 裁定逐位相同的误报，坐标 y_base 780.6/811.0/841.5、y_patch 2326.6/2354.6/2382.6、box_bottom 887.9 一致）；仅 p1-une.svg 变。
- **fr-ru（回退后，logs-minor1-revert）— 全绿**：run.py TOTAL 150、0 FLOW OVERFLOW、1 HEAD TOO WIDE（[P7-outils]，修前已存在）；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；boxtitle 0 DEFECT（53 titles）；spill 0（151 OBSERVE）；edge 0 TOUCH / 0 NEAR；census PASS；印/网文字层逐字节一致（各 96,948 字符，与 KIT fixfam1 值一致，multiset 0）；freeze CJK 12 / Latin 209（与 fixfam1 一致）；creambox FAIL 3 defects（同款已裁定误报）；P8 最小字号 11.62pt（861 spans）；印/text.md SHA 与修前逐字节一致。

## §4 KIT 更新记录

- core-fr：已更新（§七印/网/text.md 字节+SHA、pdftotext 100,857 B、webpdf 文字 46,596 B；§八追加 minor1 条目）。
- fr-en：已更新（§四印/网/text.md 字节+SHA、pdftotext 101,484 B；文末追加 minor1 小节）。
- fr-ru：已更新（Files 区网 PDF 行改为回退重建实测值 `4acb91b39968…` / 1,774,094 B，并注明内容与 fixfam1 一致；印/text.md 行未动——SHA 仍与 fixfam1 一致；文末追加 minor1 小节，含溢出实测数据与待裁定选项）。
- KIT↔磁盘核对：9 件（3 版 × 印/网/text.md）全 SHA 均与 KIT 所载一致（逐项 grep 核实）。

## §5 备注

- 未做：commit / push / lint（按任务约束）。未动其他 8 版（fr-de/es/it/ja/ko/nl/pt/zh-tw）任何文件；修后 mtime 核查：03:40 UTC 后除 core-de（de 家并行工人）外，仅本任务 3 版文件有变动。
- 溢出试验的 P1 顶部裁图与全页图存于本目录（`ru-p1-overflow-crop.png` / `ru-p1-overflow-full.png`）；修后 core P3、en P5 卡面图存于本目录（`core-p3-after.png` / `en-p5-after.png`）。
- 磁盘：收尾时 /home/hatch 96G/150G（54G 可用）。
