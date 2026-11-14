# D5 重建报告 — 2026-w43-zh-cn-nl（荷兰语读者版）

W43 zh-cn 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader；ru 读者版 Latin AND Cyrillic → Noto Sans，D26 旧分支）。施工 2026-11-14；
**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-zh-cn/logs/2026-w43-zh-cn-nl/`
（`GATES-SUMMARY.txt` 为门禁总表，`gates-run1.log` 为修前门禁日志）。

## 一、装机

- 本版手 port：installer 无法在 face= 引擎上运行（`cmap: pattern found 0x, expected 1`），
  改由 `scripts/d5_port_zhcn.py`（经 `scripts/install_zhcn.sh`，`logs/install.log`，
  `INSTALL DONE fail=0`）；本版 port RC=0。
- 装后 `_D5_READER = "latin"`（mode=latin variant=SC）；svglib.py 与基线差 99 行。
- 路由单元测试 `scripts/test_d5_routing_zhcn.py`：**FAILURES: 0**（66 PASS）；fix2 块保留（5 处）+ `_QUOTE_CLS` 4 处。
- 重建：`run.py` → `render.py` → `webpdf.py`（`scripts/rebuild_zhcn.sh`）→ text.md 由 textexp 导出（与 fanout `.text.md.new` BYTE-IDENTICAL）。

## 二、基线（修前生产版）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 65,334,695 字节（SHA-match）；网 PDF 3,172,345 字节。
- 文字层：印 PDF vs 网 PDF 字符多重集差 **0**（24,236 字符）；残差 {·:164, —:1}。
- 修前普查：D5 拉丁 **468**、西里尔 0、弯引号在 CJK **0**。
- 基线 P8 口径：noted **150/150**（core 重测亦为 150/150；port 期 149/150 是 `p8.py is_header()` 误判，已 adjudicated）。

## 三、缺陷与修法（run1 → run2）

run1 共 1 项缺陷。修法只动字号/内容侧几何常数，**未动任何文字内容**（diff vs 基线源仅改动字号/常数行）；每处修复后全量重渲 + 全部门禁重跑。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | G6 occlusion | P1 版行 `TEKSTEN IN HET CHINEES (VEREENVOUDIGD)　UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`（content12.py:23，16pt sans，anchor middle x=975，y=612） | Newsreader 荷兰语 run x=850.0，墨水右缘 1499.2；`本周热搜`标题墨水起于 1461.5 → 重叠 37.8×6.0px。基线（单 CJK run）总宽 926.5px，右缘 1438.3，occlusion 0 flags——D5 引起（整行 926.5→1048.5px）。PIL 实测：15pt → 右缘 1466.5（仍盖 −5.0px）；**14.5pt → 右缘 1450.2，余量 11.3px**；14pt → 1433.8（27.7px） | `content12.py:23` 16→**14.5**（15pt 不够——实测，非假设） |

P8 变化：834 节点（修前修后同值），距页脚线余量 35.85px（正，无溢出）。

## 四、门禁（run2，全套 17 门 + D18，ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 警告 |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：lat 0 / cyr 0 / curly_cjk 0 / noto 0 |
| 4 render | RC=0，印 PDF 55,558,312 B |
| 5 webpdf | RC=0，网 PDF 2,901,950 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 全过） |
| 7 p8 extract | noted 150/150（含 [108]） |
| 8 p8 compare | **CLEAN**：core 150 noted vs 本版 150 noted，missing=[] extra_count=0 keydiff=[]（[108] 两边都在，无 EXTRA_ONLY、无 SHORT；不切 canonical） |
| 9 freeze（基线 8/8 + diff vs base） | 基线 8/8；新增 CJK 字符 **0**（新增拉丁 strings 275，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 10 spill | 0 SPILL（33 boxes，92 candidates） |
| 11 boxtitle | 0 DEFECT（41 titles，457 body lines，1 marginal） |
| 12 edge | 0 TOUCH，0 NEAR（8 页） |
| 13 creambox | PASS，0 defects |
| 14 文字层 print=web | 字符多重集差 **0**（各 24,236 字符） |
| 15a text.md | 与 fanout **BYTE-IDENTICAL**（41,871 B） |
| 15b 共享 verify_textmd | CARRYOVER FAIL（SVG-only 241 / MD-only 2463），基线对照亦 FAIL（219/2445），差值 +22/+18 为 run 拆分 tokenization，无内容差。按 D27 口径验收：15a BYTE-IDENTICAL + 15c 907/907 UNEXPECTED 0 + 全文通读（复校）。残差逐条见 `g15b-verify.log` / `g15b-baseline-control.log`。 |
| 15c native verifier | PASS：907 entries vs ref 907，ADOPT 0，UNEXPECTED 0 |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | 本家无 gates.py（N/A） |
| D18 刊头 | gap 333.6px PASS |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `2026-w43-zh-cn-nl.pdf`；production 内印 PDF 沿用 KIT 登记名 `Lucerna-VOL1-NL.pdf`）

- 印 PDF：`Lucerna-VOL1-NL.pdf`，**55,558,312 字节**，
  SHA-256 `94950a0ef36ee18d9faf7b59edc6bec16c841bb2543ea5961fb73327c72926d4`
  （D5 前 KIT 值印 67,300,871 字节、网 3,222,500 字节（`075d90fe…`））。
- 网 PDF：`Lucerna-VOL1-NL-web.pdf`，**2,901,950 字节**，
  SHA-256 `15f5301d142c7f3471cd1259d2686401830e92bc57f2c4eb0ba791f6e6358dfb`
  （< 7 MB）。
- text.md：导出与 fanout **BYTE-IDENTICAL**
  （SHA-256 `a52d3cd4e3c7506d10a1bb3563aa41dc15c1f55fcd433b2611419aca68b68afe`，41,871 B）。
- 练习总量仍为 **150 题**。

## 六、KIT

- `production/2026-w43/2026-w43-zh-cn-nl/WEEKLY-KIT.md`：交付物/针脚行更新为 D5 值（新 SHA + 字节数）；
  文末追加 **D5 重建记录（2026-11-14）**（装机、基线、缺陷与修法、门禁 ALL-GREEN、新交付物）。
