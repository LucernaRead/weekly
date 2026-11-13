# PROOF-NOTE — core-nl fix5 独立 re-proof（2026-11-11）

- **结论：(a) — 零缺陷，可定稿。** fix5 的唯一改动（D11 盒高公式）经三重独立实测验证正确；fix4 的 D8/D9/D10 三处回归全部通过；全部门禁重跑通过；8 页逐页目视无新缺陷。
- **复校员**：独立复校员（非 fix5 修复者）。所有门禁均为本轮独立重跑；修复者的日志/脚本只作阅读参考，未直接采信其结论（其脚本复制后仅改 scratch 路径，逻辑未动；关键量测另用独立脚本复核）。
- **范围**：仅 core-nl；未碰任何 nl-* 读者版、其他核心；未 commit、未 push；生产目录无新增修改（最终 git status 与接手时一致；重建/重渲染/重导出均为字节一致）。

## §0 前置核对（SHA / 变化范围 / 源码 diff）

- 探针：`/dev/null` 存在；`git hash-object -w` 在仓库内 rc=0；scratch 目录可写。全部通过。
- 三件 SHA 实测（`sha256sum`，与任务书给出的 fix5 值逐字节比对）：
  - 印 `De-Lucerna-VOL4.pdf`：`b7d4a9cddbc38dd56ddd22cd2ae15a2e04ba1988670b6cf384eafbc66bd7ce47` / 25,955,578 B ✓
  - 网 `De-Lucerna-VOL4-web.pdf`：`5a47449cdff7d5847aee81c1c5b0f1af54cfeda873c5b55058a6d18f0e10404c` / 2,104,000 B ✓
  - 文 `2026-w47-nl-zh-cn.text.md`：`0b97a48dc248c9cf3dc28f21b55e06a1e0dc7dea7db5f6e46e55f2f2fed7050c` / 44,093 B ✓（与 fix4 一致，未变）
- SVG 变化范围实测：当前 8 个 SVG 哈希 = fix5b `svg-hashes-after.txt` 逐个一致；与 fix4（fix5b `svg-hashes-prebuild.txt`）比对，**仅 p4-sport.svg 变化**（`c82c9a3c…` → `6e05d5a0…`），其余 7 版字节一致 — 与修复者声称一致。
- 源码 diff（`git diff`，对照 HEAD）：`content34.py` 仅一处 hunk（:130–134，4 行注释 + `sh = 62 + …` → `sh = 89 + …`）；`content34.py:37` 的 `sh = 62 + … + 64`（SINTERKLAAS IN CIJFERS 盒）未动 — 已逐行核对，不是 D11 改动、无误判。`content7.py` 的修改为 fix4 D10 状态（与接手时一致）；`bslib4.py`、`content12.py`、`content56.py`、`content8.py` 本轮无改动。
- 核心内 FIX-LOG.md 第 5 轮 + WEEKLY-KIT.md §16 已含新 SHA（§16 第 232 行三件 SHA 与实测一致）。

## §1 D11（P4 HET PROGRAMMA 盒）—— 验证通过，三重实测

- 源：`content34.py:134`，`sh = 89 + Σ(len(wrap(t)) * 30.5 + 12) + 32 + 30`，附 4 行注释（盒顶→首基线实为 89 = 16+52+21）。
- 独立验算（SVG 解析 + 首基线实测，不抄 fix5 数字）：首段首基线 y=680.60，盒顶 y=591.6，差值恰为 **89.00**；五段 wrap 行数 3/3/3/2/3=14 行与 SVG 行数一致；末基线距盒顶 617.89；`89 + 487 + 62 = 638.0` 公式复算一致。
- 三重实测（`inkprobe-d11-reproof5.log`，裁图 `render/crop-p4-programma.png`）：

  | # | 方法 | 实测值 |
  |---|---|---|
  | 1 | SVG 几何 | 盒 `x=1439.5 y=591.6 w=422.5 h=638.0`，盒底 **1229.6**；末行 `<text x=1461.5 y=1209.49>` `18:45 uur.`；基线余量 **+20.11px** |
  | 2a | 真墨，cards 1× | 最低真墨行 y=**1209.00**，真墨余量 **+20.60px**；盒底以下 7px 带 **0** 非纸像素 |
  | 2b | 真墨，印 PDF 150dpi | 最低真墨行 y=**1209.12**，真墨余量 **+20.48px**；盒底以下 7px 带 **0** 非纸像素 |
  | 3 | 目视 150dpi 裁图 | `18:45 uur.` 在奶油盒内，下方有清晰奶油边距；盒底边线可见于行下 |

- 下游：`P4 col3 ends 1229.6`，练习区标线 y=1608，净空 378.40px — 无影响。
- P3 同形盒交叉核对（`content34.py:37`，尾 64）：盒底 1106.60，末基线 1090.40，余量 **+16.20px**，无溢出 — 与 fix5 声称一致。
- 修复值记录：盒底 1229.6，末基线 1209.49，真墨底 1209.00（cards）/ 1209.12（印 150dpi），余量 +20.11px（基线）/ +20.48–20.60px（真墨）。旧溢出 +6.89px 基线 / +6.4px 真墨已消除。

## §2 D8/D9/D10 回归（fix4 三处）—— 全部仍为已修状态

- **D8**（P6 图注，`content56.py:151 capcn_w = CW - 25` = 397.5）：SVG 两行 `练习数据：虚构数字，仅供练习，非真实调查。`（635.02）/ `问题：你在鞋里放什么？（100 名年轻人）`（659.44），与 fix4 基线一致；独立重扫 `width_scan_reproof.py`：目标两行成立带 **388.5–425.0**，397.5 在带内；行 1 末端 1850.0，距盒右缘 1862.0 内缩 12px；裁图 `render/crop-p6-d8.png`：行 1 以 。 结尾，行 2 行首为“问”。**通过。**
- **D9**（Q140，`content8.py:75`）：`p8-compare-reproof5.json` #140 MATCH — 注册表键 = text.md:416 = P8 节点 = `Ik maak een surprise met een kort gedicht.`；`een kort gedicht`（het 词，kort 不加 -e）语法正确；裁图 `render/crop-p8-q140.png` 已印出。**通过。**
- **D10**（P7 读者来信，`content7.py:99 dt_zh_w = CW - 32` = 390.5）：SVG 两行 `截稿时未收到真实来信或第 8 版最佳作文，`（1754.27）/ `刊登示例信，承诺顺延 VOL.5。`（1782.67），与 fix4 基线一致；独立重扫：目标两行成立带 **380.5–430.0**（另有窄带 338.5–360.0），390.5 在带内；行 1 末端 1841.6，距盒右缘 20px；裁图 `render/crop-p7-d10.png`：行 1 以 ， 结尾，行 2 行首为“刊”。**通过。**
- p6/p7/p8 SVG 与 fix4 字节一致 — 三处修复按构造不可能回归，上述实测亦逐一确认。

## §3 150 题键逐题手验 —— 全部通过（机械 149 MATCH + #150 例外；手验无同类键错）

- 机械三源对照（自写 `p8compare_reproof.py`，REG 由原地重跑 content 文件独立导出，非修复者的脚本输出）：**MATCH 149/149，DIFF 0，MISSING 0**；#150 为已知开放写作例外（P8 键 `✓`、text.md 范文 81 词、REG 占位键）。配对键重验：25–28 = d/c/a/b，141–144 = b/c/d/a。
- REG 键集与 fix4 一致性：本轮现导的 `reg-dump.json` 与 re-proof nl4 的 `reg-dump.json` 逐项一致（`json.tool` 规范化后 diff 为空）— fix5 未动任何键。
- 手验方法：通读 `keytable-150.txt` 全部 150 条（题干 + REG 键/注 + text.md 答案 + P8 键），逐题判断填空合理性；另核对外部事实点。
- 手验要点（均通过）：
  - Q140 见 §2；Q73（“四行写一首 ___”→gedicht）填空合理，无 en-ko 式键错。
  - 数字题复算：Q22/Q45（11 月 16 日→12 月 5 日=19 天）、Q43（11 月 14→15 日=1 天）、Q44（12:00–16:00=4 小时）、Q46（2026−2009=17 年）、Q83–87（35+30+20+15=100；35+30=65）全部正确。
  - 星期复核（`date -d`，Europe/Amsterdam）：2026-11-01 周日、11-11 周三（Sint-Maarten“上周三”）、11-14 周六、11-15 周日、11-16 周一、11-21 周六、12-05 周六 — 与题干/注/金句一致。
  - 语法：完成时 Q39–42（is aangekomen / heeft ontvangen / is gevaren / hebben gelezen）、过去时 Q57–60/Q104–107（speelde/won/verloor/speelden/scoorde；Q107 单数主语 Ajax→speelde，与 Q60 复数 speelden 一致）、omdat 从句末动词 Q111–112（wil/maakte）、将来时 Q76–79（gaat winnen/gaan kijken/gaat maken/gaan schrijven，主谓一致）全部正确。
  - 翻译 Q137–140 中荷互译准确；造句 Q97–100/Q133–136 语序正确；判断 Q61–64/Q80–82 与正文一致（含 Q63/Q126 的 PSV 26 分，由 P4 正文直接验证）。
  - 重复项一致：Q18=Q93（verlanglijstje）、Q58=Q105、Q59=Q106、Q60↔Q107（Twente–Ajax 2–2）无矛盾；Q6/Q104/Q115 的“7 球”三处一致；Q49/Q125（德国 0–1 负希腊）与积分榜一致。
  - Q150 范文：text.md:432 直接计数 **81 词**（去独立 `–` 为 80），在 80–100 范围内；P8 十片段逐一核对齐全。（gates 脚本的正则 fallback 报 110 词系取错段落，已在 re-proof/fix5 两轮确认，`q150-line432.txt` 为直接行计数，以此为准。）

## §4 孤儿标点 sweep —— (a) 0 / (b) 0（独立重扫，三种方法一致）

- 自写脚本 `orphan_sweep_reproof.py`（未复用修复者的脚本）：xml 解析 `<text>`，按基线 y 分组、x 间隙 >60px 分段；推进量用 PIL 实测字体与 svglib `text_w` 两种方法各跑一遍；另加无分段的蛮力复核。
- 结果（`orphan-sweep-reproof5.json` / `.log`）：重建行 1421 行；PIL 法 (a)=0、(b)=0；svglib 法 (a)=0、(b)=0；逐页均为 0。
- 蛮力复核：12 个以闭标点开头的 `<text>` 片段（与 re-proof 一致：P1 `：`1 个；P8 `：`4 个、`）`7 个），**最左元 0 个**，全部为行中片段，排除成立。
- D8/D10 目标行见 §2（行数 2，基线与 fix4 一致）。

## §5 溢出全扫（spill sweep，creambox 盲区）—— 0 溢出

- 方法：`spill_sweep_reproof.py`（re-proof 脚本复制，逻辑未动）：每奶油盒外 0–60px 邻近文本扫描。
- 结果（`spill-sweep-reproof5.log`）：**0 溢出**。P4 HET PROGRAMMA 盒现无 BELOW 命中。最近 BELOW 命中为 +24.00px（P1 `HET WOORD VAN DE WEEK`，下一区块标题），其余 BELOW 命中 ≥+32px，均为独立区块（P1 读头版说明 +44.00；P2 `Let op…` +32.00；P5 译注 +50.50；P7 两处区块标题各 +60.00）— 已逐一 adjudicate，非盒内容。ABOVE 命中为上区块的图注/说明/段落，SIDE 命中为相邻盒各自的标题 — 与 re-proof/fix5 的 adjudication 一致。
- creambox canonical（`hidden_files/w47/tools/creambox.py`，8 个 SVG 文件作参数）：rc=0；P4 盒 inside-only 末基线 1209.5，余量 **+20.1**，desc-clear **+13.7**；负余量仅上述三处已 adjudicate 的下方独立区块（−24/−44/−32）。
- creambox 旧脚本（`check_creambox_reproof.py`）：仍报 3 处 CREAM-BOTTOM（P2/P5/P6，各 ≤1.6px 几何带）；真墨探针（`inkprobe2_reproof.py`）三处框底 7px 带均为 **0** 非纸像素，真墨余量 +3.4/+3.5/+3.6px；P7 金句最低真墨 2378.0，页脚带顶 2439，余量 61.0px。**3 处真溢出 0。**

## §6 其余门禁（详见 GATE-LOG.md）

- `run.py` rc=0，TOTAL 150（页 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31），0 溢出警告；重跑后 SVG 8/8 字节一致（构建确定性）；`P4 col3 ends 1229.6`、`P3 col3 ends 1106.6`、`P6 chart ends 665`、`P6 col3 ends 1000.0`、`P7 col3 ends 1898.0`，除 P4 外与 fix4 一致。
- `render.py` rc=0，印 PDF SHA 与交付一致（字节可复现已证）。
- freeze baseline **8/8 MATCH**（`--build` 指真核心目录，`--core-svg` 指真核心 svg 目录；core SVG 未被该运行改动）。
- occlusion 真实审计 **0 flags**（自测先行通过，含 BOXTITLE 0）。
- p8 extract **150/150**；P8 最小字号 **10.12pt** ≥ 9.75pt（561 段）。
- 印/网文字层：pdftotext 印=网=重渲 44,197 B 且逐字节一致；token 多重集每页 diff 0；位置 diff 仅 P1 两 token（见 §7 备注）。
- 网 PDF scratch 重渲 2,104,001 B（交付 2,104,000 B，+1 B）；逐对象比对：唯一差异区为一个字体子集流（obj 20，Length 2174 vs 2173，Length1 同为 3320）— fontTools 子集化逐次不定，非缺陷。
- D3 回归：P2 真墨余量右列 a +98.2 / b +46.0 / c +72.2 / d +55.8；左列 25 +272.8 / 26 +280.2 / 27 +200.0 / 28 +259.2（边 1862）— 与 fix5b 逐值一致，均大幅通过。
- 引号：ASCII `"` 0、反引号 0；`« »` 35/35 成对；`“ ”` 1/1；md 同值。金句 8/8 逐字在正文。
- text.md 重导出（fix4 导出器复制，输出写回生产路径）：rc=0，44,093 B，SHA 与交付件一致；432 行；142+2+8=150 题；8 金句；6 gloss。
- §1.1 适配检查（`check_s11_core_nl.py`）：纸底、VOL 计数、等级芯片（8 页 10/15/18/18/18/18/12/35）17 PASS；P4 未引入新填充色。见 §7 备注 3（check_s11.py/verify_ed.py 原版为 en-fanout 专用，无 core-nl 版）。
- 8 页逐页目视（`render/p-1..p-8.png`，印 PDF 150dpi 自渲染）：除已修 D11 外无新发现；P2 “D WOORDEN”栏目标题与内容分栏、P7 VOLGENDE WEEK 深色带贴近末行（proof2 N3）均为修前既有、未越线，记为观察、不列缺陷。

## §7 备注（非缺陷，不影响判定，但须如实记录）

1. **印/网 P1 位置 diff 2 token**：0.1pt 精度测量下，P1 词首 `De Lucerna` 两 token 在网 PDF 中 x=393.8，较印 PDF 394.0 左移 0.2pt；其余 7 页 0，多重集 8 页均为 0。交付网与本轮 scratch 重渲结果**相同**（均含该 0.2pt 偏移），属 webpdf 字体子集化固有微差，且 P1 SVG 与 fix4 字节一致（修前既有）。内容一致，不列缺陷。
2. **网 PDF 字节不可复现**：scratch 副本重渲（仅副本，未覆盖交付件）得 2,104,001 B（交付 2,104,000 B，+1 B）；唯一差异区为 1 个字体子集流（obj 20，Length 2174 vs 2173，Length1 同为 3320）— fontTools 子集化输出逐次不定。文字层逐字节一致（pdftotext 44,197 B 三方相同）。交付件 SHA 有效；字节级复现不是门禁。
3. **check_s11.py / verify_ed.py 无 core-nl 版**：全仓检索，两个脚本只有 en-fanout 版（硬编码 core-en 与 en-{lang} 路径；verify_ed.py 还是 en 专属内容检查，含 Ashes 等），不存在可对 core-nl 运行的版本；re-proof nl4 亦未运行。已按相同检查实质写 `check_s11_core_nl.py` 对 core-nl 自身跑：纸底 #fbfaf6 8/8、等级芯片全在 LV 色集、VOL.4 每页 ≥1（P2 另有 1 处 VOL.5、P7 4 处 VOL.5 均为“VOL.5 刊登”前瞻，修前既有）、P4 无新增填充色、P8 最小字号 10.12pt — 17 PASS，0 FAIL。初版白名单系我自拟调色板误报 1 项（P6 图表蓝/金等为既有设计色），已改为“P4 无新增色”判定并重跑通过；误报不属缺陷。
4. **D5 字体只记录**：本轮重数纯拉丁落 CJK 字体段共 **245** 段（分版 38/23/30/29/29/26/18/52；方法与 re-proof/fix5b 同），字体段总数 Noto Sans CJK SC 619 / Newsreader 1215 / Noto Serif CJK SC 305 / UnifrakturMaguntia 1 — 与 fix5b 逐值一致。只记录，不判 (a)/(b)，不修。
5. **P2 “D WOORDEN”栏目标题**：标题落在第 3 栏底、内容（25–28 配对）在第 4 栏，属分栏排版旧貌，无溢出重叠，修前既有，不列缺陷。
6. **P7 VOLGENDE WEEK 深色带**：末行文字贴近带底（proof2 N3 旧貌）；P7 SVG 与 fix4 字节一致，本轮未变，不列缺陷。

## §8 结论与后续

- **结论 (a)。缺陷清单：无。** D11 已修且三重实测通过（§1）；D8/D9/D10 回归通过（§2）；150 键手验通过（§3）；孤儿 sweep (a)/(b) 0/0（§4）；spill sweep 0 溢出（§5）；其余门禁全部通过（§6）。
- **确认 fix5 可进入 nl delta 重建。** 建议：按协调员计划推进；spill sweep 入常驻门禁的工具债仍留待协调员处理（fix5b 已记，本轮复核其必要性依旧成立）。
- 交付：本文件 + `GATE-LOG.md`（见 `scratch-reproof-nl5/`）。生产目录未改动；全部复校产物在 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-nl5/`。
