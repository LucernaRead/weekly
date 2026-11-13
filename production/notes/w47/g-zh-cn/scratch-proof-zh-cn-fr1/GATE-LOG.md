# GATE-LOG — 2026-W47 zh-cn-fr proof1（独立重跑，全部门禁逐项实测值）

- 版：`production/2026-w47/2026-w47-zh-cn-fr/`；核心：`production/2026-w47/core-zh-cn/`
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）
- 日志与中间件均在本 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-zh-cn-fr1/`
- 注：首轮 run.py 误写生产 SVG，见 PROOF-NOTE“事件披露”；以下数值均为改写路径后的 scratch 重跑（run-copy / run-copy2）。

## 0. 身份核对

- 探针：`echo test | git hash-object -w --stdin`（仓内）rc=0，对象 `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`。
- 印 `f00a276e9d3366f6220df0acfc7e3f7b5573209f349d8fb380dc7a42252027f4` / 42,504,783 B ✓
- 网 `b7e43796dbe39674e42910eb37c56b20e45bd223e797bb3999560ee8d516845c` / 2,663,754 B ✓
- 文 `fb72ed2964225edb7f51599047012d0501499f41cb80543ec67d01753473080b` / 51,829 B ✓
- 核心印 `c34f5a54e491a085ea3e19a986748938dda79294b90d154a8e746f54a9eb05aa` / 41,763,115 B ✓
- 核心网 `6b7a12f517749738de2028569556be326aabe00ab556ac3ec8e59cc936a263d9` / 2,632,446 B ✓
- 核心文 `23fb62bd7763c59392c05ba7e03f64ad8f521352d464d6ac293d2190c4d0bf04` / 49,435 B ✓
- 上三 SHA 于收工时重验，全串一致。`ABSTRACT.txt` 333 B，`od` 末字节 `\n`。

## 1. run.py（scratch 副本，OUT 已改写）

- 命令：复制版内 `*.py` + `assets/` 到 `run-copy/`（及 `run-copy2/`），`sed` 替换 5 个 `content*.py` 的绝对 OUT 为 scratch，跑 `run.py`。
- `run1b.log` / `run1c.log`：rc=0，`TOTAL 150`，by level `{'A2': 56, 'B1': 69, 'B2': 25}`，by page `{1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`，by type `{'完成句子': 68, '单选': 50, '词汇配对': 20, '完形单选': 11, '写作': 1}`；日志 `overflow` 计数 0。
- 字节比对：重建 A vs 重建 B 8/8 一致（确定性成立）；重建 vs 现盘 SVG 8/8 一致（`p1-touiban` … `p8-ceyan` 全 MATCH）。
- 关键行：`P7 teaser ends 2588.78`；`flow[P8-keys] ended col 3/3 y=2537 (bottom 2560)`；`P8 keys flow ends col/y: 3 2537.2`。

## 2. freeze

- baseline（`freeze-core.log`）：`freeze.py baseline --build <core-zh-cn> --core-svg <core-zh-cn>/svg --out <scratch>/freeze-core`，rc=0，`baseline: 8/8 SVGs byte-identical`，`core integrity: shipped core SVGs unchanged`。`--build` 指核心目录，非版目录。
- diff（`freeze-diff-fr.log` / `freeze-diff-fr.json`）：`freeze.py diff --core-svg core/svg --edition-svg fr/svg --strict-cjk --json`，rc=0。逐页新增 CJK：P1–P8 全 0；`TOTAL added CJK characters: 0`。页 CJK 数：核心 886/1065/864/772/969/912/753/1125 → 本版 870/1060/859/767/964/907/742/1118。减少的串逐条核对过，全部是讲解层英→法替换的标签/注释串（如 `简体中文正文　英语讲解` → `TEXTE CHINOIS　EXPLICATIONS EN FRANÇAIS`、`第1版／共8版` → `Page 1 sur 8`），无题干中文被删。

## 3. occlusion / p8 / keycheck（真实审计，非 --selftest）

- occlusion（`occl.log` / `occl.json`）：`occlusion_audit.py <版>/svg/ --json`，rc=0，`0 flags`，内含 `selftest OK`（6 类 planted 全触发，clean 对照静默）。
- p8 extract（`p8extract.log` / `p8extract.json`）：rc=0，`noted set = 150 of 150 (parse: lines)`。
- p8 compare（`p8compare.log` / `p8compare.json`，直接读 JSON 本体）：rc=0，`status: CLEAN, total: 150, core_count: 150, edition_count: 150, missing: [], extra: [], uncertain: [], keydiff: []`。gates.json 的 p8 extra "?" 未采信，以 JSON 本体为准。
- keycheck（`keycheck.log` / `keycheck-150.json`）：`keycheck.py fr <版> <scratch>`（de 家族 stub 本地补两法：`glossline` 代理 `bridge`、`Flow.ci = 0`；只改本 scratch 副本）。`REG entries: 150; p8extract keys: 150; exact match: 149/150`，唯一 mismatch `n=150 写作：key='(开放题，范文如下)' extracted='✓'`。核心同法提取 Q150 亦为 `✓`，行为相同；脚本 rc=1 是其 `startswith` 预期不适用，非版面问题。
- 另：核心 P8 同法提取 150/150，与本版印出键逐项差 0（`extracted-key diffs core vs fr: []`），Q137–140（7.77 / 14 / GEN / 冷）相同。

## 4. 印/网文字层逐页一致 + P8 字号（`textcmp.log` / `p1diff.py`）

- PyMuPDF 逐页 span 比对（位置排序 + 多重集，含字号）：P1 485/485、P2 359/359、P3 297/297、P4 507/507、P5 301/301、P6 328/328、P7 348/348、P8 836/836；msdiff 全 0；posdiff 仅 P1 = 1：147 pt 刊名 `Lucerna`（印 x0=502.2，网 x0=501.7，差 0.5 pt；y/字号/文字同一）。
- P8 最小字号：印 9.975000381469727 pt、网 9.975 pt、核心印 9.98 pt（spans 836 / 836 / 838）；源头为 SVG 13.3 px（13.3 × 0.75 = 9.975）。任务书 ≥10 pt 差 0.025 pt，三方同一，见 PROOF-NOTE 记录项 1。

## 5. 150 题逐题手验（`verify-150.txt`、`stems.json`、`reg-fr.json`、`reg-core.json`）

- 机制：stub 下重跑版内 content（`dump_reg.py`，REG + LOG 全量），法语版与核心各一份。
- 题干 CJK：150/150 与核心逐字一致（仅 `[instr]` 英→法不同）。
- REG 字段（page/level/type/key）：法语版 vs 核心 0 差异；注文 149 条译法，仅 Q80 `悬疑 = suspense, b` 与核心相同（同形法语词）。
- 键 vs 印出：149/150 精确一致；Q150 开放题 `✓`（预期）。
- 单选/完形 61 题：键均在选项内；事实键对正文核对：Q4（瑞士轮 HLE / 八强 DK / 半决赛 T1）、Q15/Q20/Q21–23、Q57–60、Q65–77、Q106/Q117、Q113–120、Q141–146、Q150 范文 138 字符（实测 138）。
- 词汇配对 20 项：5 组 `match_set` 源码数组 + 印出字母顺序逐项核对（P2 a/b/c/d；P3 b/d/a/c；P4 d/b/c/a；P5 c/b/d/a；P6 c/d/a/b），全部正确；P3 印出 `a. 天冷了… / b. 二十四节气… / c. 不小心… / d. 古人…` 与键一致。
- D4/D5：印 PDF 全文计数法语版 = 核心（`全球总决赛的BO5` 2 / 旧 0；`GEN在S16一场没输` 2 / 旧 0；`只丢了一小局` 2；`一局没输` 1，仅 P4 事实框）；Q56 题干 + 键 T1 + 法语注文 Worlds 限定在位；P1/P4 两句原文已目视确认。

## 6./7. 盒标题真墨 + 溢出横扫（`sweep.py` / `sweep.json` / `sweep-core.json`）

- 方法：复用 `tools/occlusion_audit.py` 的 `parse_svg` + `ink_box`（PIL 真墨、同字体栈）；容器为全部 `<rect>`（含纯填充奶油盒 `#f0eee5`，审计 BOXTITLE 只认有描边盒，故其 0 flags 对此类是空信号）；容器须先于文字绘制、含文字锚点或墨中心；容限 0.5 px。
- 法语版：8 页，texts 3286，containers 181，flags **3**：BOX_OVERFLOW ×3（P1 数字标题、P1 截稿行、P2 日历标题）；BASELINE_OUTSIDE 0、EDGE 0、真墨触图 IMG_OVERLAP 0。
- 标题余量：179 个容器标题，仅 2 个负余量（D-1 −17.8、D-3 −3.2）；其余最小 +6.0（P5 `这一周的高频词　Mots de la semaine`）。
- 核心同法横扫：0 flags（同位余量：P1 数字标题 +20.2、P1 截稿行 +10.2、P2 日历标题 +22.0）。
- D-1：`数字看本周　Cette semaine en chiffres` 墨 [556.5, 1127.3, 978.8, 1149.8] vs 盒 [538.5, 1110.3, 961.0, 1463.3]，右超 17.8 px；源码 `content12.py:47`；证据 `flag1-p1-numbers-title.png`。
- D-2：`Bouclage : 10 nov. — la finale pas encore jouée` 墨 [1461.5, 1235.5, 1869.5, 1256.8] vs 盒 [1439.5, 588.0, 1862.0, 1288.0]，右超 7.5 px；源码 `content12.py:88`；证据 `flag2-p1-pressline.png`。
- D-3：`本周生活小日历　Dates de la semaine` 墨 [1007.0, 217.2, 1414.8, 239.5] vs 盒 [989.0, 200.0, 1411.5, 447.0]，右超 3.2 px；源码 `content12.py:187`；证据 `flag3-p2-cal-title.png`。建造者曾量墨右缘 1414.9（与本次 1414.8 一致），只对了山谷照、未对盒边。

## 8. 引号 / 孤儿 / 禁词 / 繁体（`gate8.log`）

- 弯引号：文 `“`2/`”`2、`«`6/`»`6、`‘’`0；SVG P3 1/1、P6 1/1、P7 4/4、P8 1/1——全部成对。U+2019：文 0、SVG 0。
- 禁词/政治/占位：`乌克兰/俄乌/战争/地缘/外交/制裁/北约/普京/特朗普/贸易战/台独/…/TODO/FIXME/Lorem/TBD/占位/待填/XXX` 正文 0（`TBD`×13、`XXX`×16 只在 base64 图片数据内，`<text>` 内 0、去 base64 后 0）。
- 英文残留：`Fill in the blank / Read & choose / Answers on page / EXPLANATIONS IN ENGLISH` 等 13 标记，SVG 0。
- opencc t2s：文 + 8 SVG，改动字符全部 NONE（0 繁体残留）。
- CJK 孤儿标点（精修扫描：按基线 y + 栏位分组，闭集 `。，、；：？！」』）〕］》›` / 开集 `「『（〔［《〈‹`）：仅 1 处真孤儿——P1 y=1366.3 行首 `》 sort`（D-4；证据 `flag4-p1-shitan-orphan.png`；核心无行首孤儿）。P4 `一起打游戏的老照片（` 初报为行尾开括号，经核对为误报：同一基线接续 `2003年，法国）。今天看`，核心亦同。
- 填空/改写键合理性：见 §5；Q150 范文 138 字符实测 138。

## 9. 重建修点复验（全部存活）

- P4 注释框：以本版前缀 `Notes｜`（`bslib4.py:207` 硬编码，非英文前缀量测）实测 6 行（基线 595.9 / 625.6 / 655.3 / 685.0 / 714.8 / 744.5），盒 `x=538.5 y=557.36 w=422.5 h=234.85`，框底 **792.2**；`GEN，` 在 y=822.4，净空 30.2 px；occlusion 0 印证。源码 `content34.py:134` 已无 `, les demi-finalistes`。
- P8 keys 溢出：`flow[P8-keys] ended col 3/3 y=2537 (bottom 2560)`；末键基线 2506.392（Q150 第二行 2521.82），尾 y=2537.2，余 22.8 px。
- P2 词卡例句出框：价保卡 `x=989.0 y=1618.0 w=422.5 h=150.0`（底 1768.0）；例句 `pas automatique : demande-le toi-même` 1 行，墨底 1756.3，净空 11.7 px。
- P7 下期预告压页脚：`P7 teaser ends 2588.78` < 页脚线 2596，净空 7.22 px；目视条底在页脚线上方。
- D5 字体问题：只记录，不判——P1/P4 的 D5 句查 SVG 字体分段，拉丁 `GEN`/`S16` 走 Newsreader、中文走 Noto Sans CJK SC，与核心分段同一，渲染目视无异常；重建报告/记录/KIT 中无此项具体所指。见 PROOF-NOTE 记录项 4。

## 目视

- 印 PDF 110 dpi 全 8 版（`vis-p1.png` … `vis-p8.png`）逐页读过；P1/P2/P4/P5/P7/P8 逐页读过，P3/P6 同。另 216 dpi 裁图：`flag1/2/3/4`、`core-p1-numbers-title.png`、`core-p2-cal-title.png`（核心对照）。
- 除 D-1 ~ D-4 外未见重叠、裁切、缺图、压页脚。
