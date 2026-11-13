# PROOF-NOTE — core-nl fix4 独立 re-proof（2026-11-11）

- **结论：(b) — 不通过。** fix4 自身的三处修复（D8/D9/D10）全部验证正确；但独立复校在 8 页逐页目视中发现一处**真缺陷 D11**（P4 HET PROGRAMMA 盒最后一行溢出盒外，真墨 +6.4px），且该缺陷是 creambox 门禁脚本的盲区（见 §6）。按本项目既往先例（proof2 对 fix2 的 (b)：缺陷为修前旧患、非本轮引入，仍判 (b)），fix4 不能进入 nl delta 重建，须先修 D11（fix5）再复校。
- **复校员**：独立复校员（非 fix4 修复者）。所有门禁均为本轮独立重跑；修复者的日志/脚本只作阅读参考，未直接采信其结论。
- **范围**：仅 core-nl；未碰任何 nl-* 读者版、其他核心；未 commit、未 push；生产目录无新增修改（最终 git status 与接手时一致）。

## §0 前置核对（SHA / 变化范围 / 源码 diff）

- 探针：`/dev/null` 存在；`git hash-object -w` 在仓库内 rc=0；scratch 目录可写。全部通过。
- 三件 SHA 实测（`sha256sum`，与任务书给出的 fix4 值逐字节比对）：
  - 印 `De-Lucerna-VOL4.pdf`：`2c7f2c6fb3c443fa32a6055bfa4a368f11a761c75de0995b776204510a7ecd3c` / 25,955,580 B ✓
  - 网 `De-Lucerna-VOL4-web.pdf`：`434626f58b605b8ba0878b7d52de32e8255f2ad43489e133e602faef49853df5` / 2,103,990 B ✓
  - 文 `2026-w47-nl-zh-cn.text.md`：`0b97a48dc248c9cf3dc28f21b55e06a1e0dc7dea7db5f6e46e55f2f2fed7050c` / 44,093 B ✓
- SVG 变化范围实测：当前 8 个 SVG 哈希 = fix4 `svg-hashes-after-b.txt` 逐个一致；与 fix3（`svg-hashes-before.txt`）比对，**仅 p6/p7/p8 变化**，其余 5 版字节一致 — 与修复者声称一致。
- 源码 diff（对照 fix3 时代的 `scratch-fix-core-nl3/freeze/build-copy/`，已验该副本 text.md SHA=`2f2a650b…b25d92e`、SVG 与 fix3 before-hashes 一致，确为 fix3）：
  - `content56.py`：仅 D8（注释 + `capcn_w = CW - 25` + 高度计算与 `p.para` 两处调用点）。
  - `content8.py`：仅第 75 行，`…met een gedicht.` → `…met een kort gedicht.`。
  - `content7.py`：仅 D10（注释 + `dt_zh_w = CW - 32` + 两处调用点）；与 `git diff` 一致。
  - `bslib4.py`、`content12.py`、`content34.py`：与 fix3 副本逐字节一致。
- text.md 与 fix3 的 diff：**仅第 416 行**（Q140 加 `kort `，+5 字节）。

## §1 D8（P6 图注行首孤儿 。）—— 验证通过

- 源：`content56.py:143 capcn` 原文不变；`:151 capcn_w = CW - 25`（CW=422.5 → 397.5px），高度计算（`:152`）与 `p.para`（`:164`）两处同用。
- 独立重扫 `wrap()`（`width_scan_reproof.py`，`width-scan-reproof.log`）：
  - 旧宽 378.5 重现孤儿：`['练习数据：虚构数字，仅供练习，非真实调查', '。问题：…']`。
  - 目标两行成立的带为 **388.5–406.5**（与修复者声称一致）；397.5 恰为带中值。
  - 窄化不可行：370 仍为 2 行孤儿，≤360 则 3 行 — 修复者“窄化不能保 2 行”成立。
- 重建后 SVG 实测（`orphan_sweep_reproof.py`）：`练习数据：虚构数字，仅供练习，非真实调查。`（x=1461.5, y=635.02, 18.5px）/ `问题：你在鞋里放什么？（100 名年轻人）`（x=1461.5, y=659.44），行数 2，基线与修前一致。
- 行 1 末端：1461.5+388.5=**1850.0**，盒右缘 1862.0，内缩 12px；creambox 无 CREAM-RIGHT 告警。
- 下游不动：重跑 `run.py` 日志 `P6 chart ends 665`、`P6 col3 ends 1000.0`，与 fix3 一致。
- 裁图目验 `render/crop-p6-d8.png`：行 1 以 。 结尾，行 2 行首为“问”，孤儿消除。

## §2 D9（Q140 答案缺 kort）—— 验证通过

- 源：`content8.py:75` 注册表键 `Ik maak een surprise met een kort gedicht.`；注 `surprise 是固定搭配` 不动。
- 四源一致（独立重跑 `p8compare_reproof.py`）：注册表键 = text.md:416 答案 = P8 答案节点 = `Ik maak een surprise met een kort gedicht.`（`p8-compare-reproof.json` #140 MATCH）；题干“带小诗”与 text.md:73 源句 `Twee: schrijf een gedicht — kort is ook goed.` 均支撑 kort。
- 语法核对：`een kort gedicht`（不定冠词 + het 词 gedicht，kort 不加 -e）正确。
- 注不动的理由成立：`surprise 是固定搭配`在新答案下仍真；kort 已由题干与源句交代。
- P8 裁图目验 `render/crop-p8-q140.png`：`140. Ik maak een surprise met een kort gedicht. — surprise 是固定搭配` 已印出。
- 其余 149 键未动：本轮 REG 键与 proof3 手验集（`keycheck-150.json`，150/150 PASS-HAND）比对，仅 Q140 不同（另 Q150 为字段含义差异，见 §5）。

## §3 D10（P7 行首孤儿 ，）—— 验证通过；范围裁定：属本轮正当修复，不超范围

- 源：`content7.py:91 dt_zh` 原文不变；`:99 dt_zh_w = CW - 32`（390.5px），`lh` 计算（`:100`）与 `p.para`（`:108`）两处同用。
- 独立重扫：旧宽 378.5 重现孤儿（行 1 360.06px + ，20px > 378.5）；目标两行成立带为 **380.5–400.0**（与修复者声称一致）；390.5 取中（距下缘 10px、上缘 9.5px）。
- 重建后 SVG 实测：`截稿时未收到真实来信或第 8 版最佳作文，`（x=1461.5, y=1754.27, 20px）/ `刊登示例信，承诺顺延 VOL.5。`（x=1461.5, y=1782.67），行数 2，基线不变；`P7 col3 ends 1898.0` 与 fix3 一致；行 1 末端 1461.5+380.06=1841.6，距盒右缘 20px。
- 裁图目验 `render/crop-p7-d10.png`：行 1 以 ， 结尾，行 2 行首为“刊”，孤儿消除。
- **范围裁定**：D10 虽不在任务书原定的两源文件内，但它是任务书自身要求的双类 sweep (b)=0 门禁所必需的修复；与 D8 同一缺陷类（贪婪 `wrap()` 在 CW-44 下把全角标点推到下一行行首）、同一修法（加宽 wrap 宽、行数与盒高不动）、最小改动（一个宽度常量 + 两处调用点 + 注释）。**不属超范围，修得正确。** 若不修，(b) 门禁不可能为 0。
- 修复者论证的一处不精确（记为备注，非缺陷）：其称“窄化 ~350–360 会拆散‘作文’”属实（350–360 行 1 以“最佳作”结尾），但窄带 **338.5–~341** 同样 2 行清孤儿且“作文”完整（行 1 以“最佳”结尾，行 2 以“作文，”开头）。选择加宽仍正确且更优（断行落在分句边界 ， 处），但“窄化必然拆 作文”的表述不完整。

## §4 孤儿标点 sweep —— (a) 0 / (b) 0（独立重扫，三种方法一致）

- 自写脚本 `orphan_sweep_reproof.py`（未复用修复者的 `orphan_sweep.py`）：xml 解析 `<text>`，按基线 y 分组、x 间隙 >60px 分段；推进量用 PIL 实测字体（fc-match 定位）与 svglib `text_w` 两种方法各跑一遍；另加无分段的蛮力复核（所有以闭标点开头的 `<text>` 元， adjudicate 是否为基线最左元）。
- 结果（`orphan-sweep-reproof.json` / `.log`）：重建行 1421 行；PIL 法 (a)=0、(b)=0；svglib 法 (a)=0、(b)=0；逐页均为 0。
- 蛮力复核：12 个以闭标点开头的 `<text>` 片段（P1 `：柏林奥林匹克` 1 个；P8 `：` 4 个、`）` 7 个），**最左元 0 个**，全部为行中片段，排除成立。
- 备注：修复者 FIX-LOG/WEEKLY-KIT 称“11 个行中片段”，其自家 `orphan-crosscheck-fix4.log` 实际列出 12 个（1+4+7）——文字笔误，门禁结论不受影响。

## §5 150 题键逐题手验 —— 全部通过（机械 149 MATCH + #150 例外；手验无同类键错）

- 机械三源对照（自写 `p8compare_reproof.py`，REG 由原地重跑 content 文件独立导出，非修复者的 `p8compare_fix4.py`）：**MATCH 149/149，DIFF 0，MISSING 0**；#150 为已知开放写作例外（P8 键 `✓`、text.md 范文 81 词、REG 占位键）。配对键重验：25–28 = d/c/a/b，141–144 = b/c/d/a。
- 手验方法：通读 `keytable-150.txt` 全部 150 条（题干 + REG 键/注 + text.md 答案 + P8 键），逐题判断填空合理性；另核对外部事实点。
- 手验要点（均通过）：
  - Q140 见 §2；Q73（“四行写一首 ___”→gedicht）填空合理，无 en-ko 式键错。
  - 数字题复算：Q22/Q45（11 月 16 日→12 月 5 日=19 天）、Q43（11 月 14→15 日=1 天）、Q44（12:00–16:00=4 小时）、Q46（2026−2009=17 年）、Q83–87（35+30+20+15=100；35+30=65）全部正确。
  - 星期复核（`date -d`，Europe/Amsterdam）：2026-11-01 周日、11-11 周三（Sint-Maarten“上周三”）、11-14 周六、11-15 周日、11-16 周一、12-05 周六 — 与题干/注/金句一致。
  - 语法：完成时 Q39–42（is aangekomen / heeft ontvangen / is gevaren / hebben gelezen）、过去时 Q57–60/Q104–107（speelde/won/verloor/speelden/scoorde）、omdat 从句末动词 Q111–112（wil/maakte）、将来时 Q76–79（gaat winnen/gaan kijken/gaat maken/gaan schrijven，主谓一致）全部正确。
  - 翻译 Q137–140 中荷互译准确；造句 Q97–100/Q133–136 语序正确；判断 Q61–64/Q80–82 与正文一致（含 Q63/Q126 的 PSV 26 分，现可由 P4 正文直接验证，D5 修复有效）。
  - 重复项一致：Q18=Q93（verlanglijstje）、Q58=Q105、Q59=Q106、Q60↔Q107（Twente–Ajax 2–2）无矛盾。
  - Q150 范文：text.md:432 计 81 词（去独立 `–` 为 80），在 80–100 范围内；P8 十片段逐一核对齐全。
- 与 proof3 手验集比对：本轮 REG 键与 proof3 `keycheck-150.json`（150/150 PASS-HAND）仅 Q140 不同；Q150 的差异只是字段含义（proof3 该字段记 P8 键 `✓`，本轮记 REG 占位键），内容无变化。**Q140 之外无同类键错。**

## §6 缺陷 D11（判 (b) 的唯一原因）—— P4 HET PROGRAMMA 盒最后一行溢出盒外

- **位置与实测值**：P4 col3 `HET PROGRAMMA` 奶油盒，rect `(x=1439.5, y=591.6, w=422.5, h=611.0)`，盒底 **1202.6**；盒内最后一段第 3 行 `18:45 uur.`（`<text x=1461.5 y=1209.49 font-size=21.5>`），基线超出盒底 **+6.89px**；卡片 PNG 真墨探针（`inkprobe2_reproof.py`，墨点定义 r<200 或 g<200 或 b<190）：最低真墨行 y=**1209**，真墨溢出 **+6.4px**；裁图 `render/crop-p4-programma.png` 目视：`18:45 uur.` 落在盒外白地上。
- **同段完整证据**：该段三行基线 1148.43 / 1178.96 / 1209.49（x 同为 1461.5，同字号 21.5），前两行在盒内，仅末行出盒。
- **根因**（`content34.py:126–137`）：盒高公式 `sh = 62 + Σ(len(wrap(t)) * 30.5 + 12) + 32 + 30`；五段 wrap 行数 3/3/3/2/3=14 行，sh=611。但渲染侧从盒顶到第一段首基线实际为 89px（16 pad + 52 标题块 + 21 首基线偏移），公式顶部只留 62px，短 27px；尾部预留 62px，实际只需 42.53px（para 回值一整行距 30.53 + 间隔 12），多留约 19.5px；净短约 7px。逐行行距 30.5≈30.53 无问题，短缺来自固定预留，与行数无关。另：`Page.para` 返回末基线 + 一整行距（`svglib.py` 实测源码），这正是每段间隔实为 63.53px（30.53+12+21）的原因。
- **旧患，非 fix4 引入**：当前 P4 SVG 哈希与 fix3 逐字节一致；fix3 时代副本（`scratch-fix-core-nl3/freeze/build-copy/svg/p4-sport.svg`）中同一 `<text>` 同为 y=1209.4899999999996。缺陷由 fix2 的 D5 引入（第 5 条事实入盒），fix2 FIX-LOG 称“P4 card visually checked (line inside the box, clear margins)”与实测不符。
- **门禁盲区（本轮新发现，须写入工具）**：`check_creambox.py` 的收容前置条件要求文本基线落在 `rect±1` 内才检查——整行落在盒外的文本直接被跳过，P4 本轮复跑仍报 0 flags；occlusion 的 BOXTITLE 类只针对有描边的盒，本盒为纯 fill 矩形，不适用。两道门禁均看不见此类溢出。本轮另写的 `spill_sweep_reproof.py`（盒外 0–60px 邻近文本扫描）全周仅此一处近距命中（+6.89px；其余 BELOW 命中均 ≥+24px 且为独立区块标题/注脚，已 adjudicate 非盒内容）。
- **修复建议**：`content34.py` 修正盒高公式（顶部预留按实际 89px 计，或直接将 sh 增大至末行基线 + 下垫距，即盒底 ≥1216，约 +14px）；P4 col3 末端 1202.6→~1216.6，距练习区标线 1608 仍有 ~390px，无下游影响；修后用 spill sweep 复验（盒外 0 命中）并重跑 creambox/occlusion/8 页目视。
- **判定**：D11 为真缺陷，违反“creambox/box-title 真墨扫描 0 真溢出”门禁的实质要求（任务书明确“以 PIL 真墨为准”）。fix4 未动 P4，但复校判的是核心整体状态；按 proof2 对 fix2 的既往先例（修前旧患仍判 (b)），此处判 **(b)**。

## §7 其余门禁（详见 GATE-LOG.md）

- `run.py` rc=0，TOTAL 150（页 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31），0 溢出警告；重跑后 SVG 字节一致。
- `render.py` rc=0，印 PDF SHA 与交付一致（字节可复现已证）。
- freeze baseline **8/8**（`--build` 指真核心目录，`--core-svg` 指真核心 svg 目录）。
- occlusion 真实审计 **0 flags**（自测先行通过，含 BOXTITLE 0）。
- p8 extract **150/150**；P8 最小字号 **10.12pt** ≥ 10pt。
- 印/网文字层：pdftotext 印=网=44,197 B 且逐字节一致；token 多重集每页 diff 0；位置 diff 仅 P1 两 token（见 §8 备注）。
- creambox：仍报 3 处 CREAM-BOTTOM（P2/P5/P6，均 ≤1.6px 几何带）；真墨探针三处框底 7px 带均为 0 墨点，真墨余量 +3.4/+3.5/+3.6px。**但 D11 不在该脚本覆盖内（§6），三处 0 真溢出不代表全周 0 溢出。**
- D3 回归：P2 D 选项真墨余量 a +97.5、b +44.5、c +71.5、d +55.5（`font.getbbox` 1x 实测，与修复者右列值逐值一致）；左列 25–28 真值 +272.5/+279.5/+199.5/+258.5（见 §8 备注）。
- 引号：ASCII `"` 0、反引号 0；`« »` 35/35 成对；`“ ”` 仅 1 对。金句 8/8 逐字在正文；Q150 范文 81 词。
- text.md 重导出（输出重定向至 scratch，未动交付件）：rc=0，44,093 B，与交付件逐字节一致；432 行；142+2+8=150 题；8 金句；6 gloss。
- 8 页逐页目视（`render/p1–p8.png`，印 PDF 1.5x 自渲染）：除 D11 外无新发现；P2 “D WOORDEN”栏目标题与内容分栏、P7 VOLGENDE WEEK 深色带贴近末行（proof2 N3）均为修前既有、未越线，记为观察、不列缺陷。

## §8 备注（非缺陷，不影响判定，但须如实记录）

1. **印/网 P1 位置 diff 2 token**：本轮 0.1pt 精度测量下，P1 词首 `De Lucerna` 两 token 在网 PDF 中 x=393.8，较印 PDF 394.0 左移 0.2pt；其余 7 页 0，多重集 8 页均为 0。交付网 PDF 与本轮 scratch 重渲结果**相同**（均含该 0.2pt 偏移），属 webpdf 字体子集化固有微差，且 P1 SVG 与 fix3 字节一致（修前既有）；修复者“positional diff 0”应为其取整较粗所致。内容一致，不列缺陷。
2. **网 PDF 字节不可复现**：scratch 副本重渲（仅副本，未覆盖交付件）得 2,104,002 B（交付件 2,103,990 B，+12 B）；逐对象比对：8 页内容流逐字节一致，3 个图像流一致，**6 个字体子集流长度相同、字节不同**——fontTools 子集化输出逐次不定。文字层逐字节一致（pdftotext 44,197 B 三方相同）。交付件 SHA 有效；字节级复现不是门禁。
3. **D5 字体只记录**：本轮重数纯拉丁落 CJK 字体段共 **245** 段（分版 38/23/30/29/29/26/18/52；方法：`<text>` 含 `[A-Za-z]` 且无 U+3400–U+9FFF/U+F900–U+FAFF 字符，字体名含 CJK），与 proof3 的 245 一致；修复者记 206（方法未留存，不可比）。字体段总数：Noto Sans CJK SC 619 / Newsreader 1215 / Noto Serif CJK SC 305 / UnifrakturMaguntia 1。只记录，不判 (b)，不修。
4. **修复者 D3 左列数值有误（右列无误）**：其 P2 左列 25–28 余量 +278.5/+285.5/+208.5/+265.5 是按 23px 量的，而 SVG 实际为 24px；按 24px `font.getbbox` 重测为 +272.5/+279.5/+199.5/+258.5。右列四值与本轮逐值一致。门禁（≥+5px）两种量法下均大幅通过。
5. **P2 “D WOORDEN”栏目标题**：标题落在第 3 栏底、内容（25–28 配对）在第 4 栏，属分栏排版旧貌，无溢出重叠，修前既有，不列缺陷。

## §9 结论与后续

- **结论 (b)。缺陷清单仅 D11 一项**（§6，P4 `content34.py` 盒高公式，末行 `18:45 uur.` 基线 +6.89px / 真墨 +6.4px 出盒）。
- **D10 范围裁定**：正当、最小、同缺陷类，满足 (b)=0 门禁所必需，不超范围。
- **fix4 自身（D8/D9/D10）全部验证通过**；但核心整体仍含 D11，**不确认 fix4 可进入 nl delta 重建**。建议：开 fix5 修 D11（修正盒高公式并补 spill sweep 入常驻门禁），复校通过后再行 delta 重建。
- 交付：本文件 + `GATE-LOG.md`（见 `scratch-reproof-nl4/`）。生产目录未改动；全部复校产物在 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-nl4/`。
