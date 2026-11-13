# PROOF-NOTE — 2026-W47 nl-ru（俄语读者 × 荷兰语目标）独立复校 proof1

- 校对员：独立 proof1（与 delta 员不同人，全部重跑）
- 日期：2026-11-11；工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-ru1/`
- 目标：`~/workspace/weekly-git/production/2026-w47/2026-w47-nl-ru/`（只读；未改任何生产文件，未 commit/push；所有重建均在 scratch 副本里做；`PYTHONDONTWRITEBYTECODE=1` 全程；TMPDIR = 本 scratch）
- 方法：SOP §8.4 全量独立复校；机械门禁一律用仓内共享工具（`tools/occlusion_audit.py`、`tools/p8.py`、`tools/freeze.py`）+ 本轮 delta 脚本的复用改写版（路径指向本 scratch，核心读数全部重测）

## 结论 (a) 零缺陷，可定稿

17 门全部通过（实测值见 `GATE-LOG.md`），无缺陷。缺陷清单：无。观察类事项见文末（均不构成缺陷，按 STRADDLE 裁定与任务指令不报缺陷）。

## 开工身份核对（三 SHA，实测 = 任务给定值 = KIT build-6 值）

| 文件 | 字节 | SHA-256（实测，开工与收尾两次一致） |
|---|---|---|
| `De-Lucerna-VOL4-nl-ru.pdf`（印） | 12,718,418 | `21b7adf007a15e195756d49b22c824e828f854e11e02a10c916426997c468cc8` |
| `De-Lucerna-VOL4-nl-ru-web.pdf`（网） | 1,661,392 | `1a17474368591008dcefb73661be58a17edc38c5dcc98f674fc0afe6ea6cc9bf` |
| `2026-w47-nl-ru.text.md`（文） | 57,870 | `f23da475ff54bcfe86bbe6794473eafc65b42dbd5f015766924ce3e83cefb984` |

开工探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；goals-side scratch 真实写文件 `probe.txt` OK。`/dev/null` 正常（字符设备，无需补建）。
收尾复核：三 SHA 与 8 个交付 SVG SHA 与开工记录逐字节一致；`find` 验生产目录无文件在本轮开工时间后被修改；`__pycache__` 时间戳仍为 delta 轮次（18:48 / 02:13），本轮未写入。

## 核心实测（每项源码行 + 实测值 + 渲染证据）

### 1. 重建与冻结

- `run.py`（scratch 副本 `repro-build/`）：rc=0，TOTAL 150（by page 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31），FLOW OVERFLOW / TOO WIDE 计 0；`flow[P1-headline] ended col 2/2 y=1465`、`flow[P8-keys] ended col 3/3 y=2486 (bottom 2560)`、`P4 col3 ends 1229.6`。日志 `run-rebuild.log`。
- 重建 SVG 与交付 SVG sha256 逐页比对 8/8 一致（`delivered-svg-sha.txt` vs `repro-svg-sha.txt`）。
- 印 PDF scratch 重渲（`render.py`，rc=0）：12,718,418 B，SHA `21b7adf0…468cc8`，与交付印 PDF **逐字节相同**。
- freeze 核心 baseline：`freeze.py baseline --build core-nl --core-svg core-nl/svg` rc=0，**8/8 字节一致**；核心 shipped SVG 跑前后哈希不变（`freeze-core.log`，`core-svg-sha-before/after.txt` 一致）。

### 2. 几何门禁

- occlusion：`tools/occlusion_audit.py svg/` rc=0，**0 flags**；自检六类全触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），干净对照静默（`occlusion.log`）。
- creambox：TOTAL 3 flags，与 delta 轮完全相同的三处，逐项像素裁定均为假阳性：
  - P2 CREAM-BOTTOM `'редакцию.'`（bottom 1503.0 vs rect 1503.8）：盒底下 7px 条带（交付卡片 PIL）0 非纸像素。
  - P5 CREAM-BOTTOM `'отправь их.'`（1051.6 vs 1052.5）：同法 0 非纸像素。
  - P6 CREAM-RIGHT `DE GRAFIEK　УЧЕБНЫЕ ДАННЫЕ`（advance 右 1855.6 vs 盒右沿 1862.0，内 6.4px）：盒右沿外 x1862–1875 条带 0 非纸像素；隔离真墨渲染余量 **+9.5px**。真溢出 0。
  （`creambox.log`、`probe-cream-d11.log`；`boxtitle_rc: 0` 未作证据——occlusion 对纯填色 `#f0eee5` 奶油盒全盲已在方法中说明。）
- 盒标题横向真墨扫描（隔离渲染，PIL + NotoSansCJK-Bold 真墨 bbox）：**59 标题，OVER-EDGE 0**。独立重数与之完全吻合：奶油盒标题 21（26 个奶油 rect 中 21 个含粗体标题；另 5 个为无标题的事实/图表盒，其标题在盒外上方，如 P4 `DE STAND IN GROEP 2`）+ Flow.head 标题 38 次出现（31 个不同源字符串，`content*.py` 的 `.head(...)` 逐一核对，SVG 内精确 `<text>` 匹配；初数 41 为子串误计——`B　WOORDEN` 3 次实为 `B　WOORDEN UIT DE TEKST`，已纠正）。最紧余量：P6 DE GRAFIEK **+9.5px**、P6 VOOR OF TEGEN? +18.5px、P2 DRIE DINGEN head +25.5px、P2 ZO ONTHOUD +26.5px、P1 DE WEEK IN CIJFERS +35.5px。任务所称 56 标题无一定义能复现（38 head 出现 + 21 盒标题 = 59 为本版实测）；按 59 全集扫查，0 越边（`boxtitle2.log`、`title-count.log`、`heads-source.txt`）。
- spill 横扫：P4 HET PROGRAMMA 盒（底 1229.6）**无任何 BELOW 命中**；其余 BELOW 命中均为独立版块（下一节标题、提示语、gloss），ABOVE/SIDE 均为图注/邻盒标题/刊头——与核心 fix5 同类裁决，真溢出 0（`spill.log`）。

### 3. P8 与三方比对

- p8 extract：noted set **150/150**（`gates/p8-extract.json`）。
- p8 compare（核心 vs 本版）：**CLEAN**，missing []、extra 0、uncertain []，keydiff **[137, 138]**——翻译题键即读者语（核心中文 vs 本版俄文），按设计不同，非缺陷（`p8-compare.json`）。
- 三方比对（registry vs text.md vs P8，俄语答案标记 `— Ответ：` / `(Ответ x ·`）：**149/149 MATCH**，DIFF=[]、MISSING=[]；配对键 25–28 = d/c/a/b、141–144 = b/c/d/a（`p8-compare-3way.json`）。
- Q150 重组核实：P8 节点为单个 `✓`（x=1470.1, y=2470.24）；text.md:431 Tekstmodel 实测 **81 词**（与 KIT 及 REG 注“81 слов”一致）；REG 键为开放题占位。P8 实印全键与 REG 逐字一致的结论成立（Q150 为开放写作例外，非截断）。
- P8 最小字号：答案区 min **10.12pt**（median 10.12，598 spans）≥ 9.75pt 下限；chips core=edition {A2: 8, B1: 24, B2: 3}。
- 印/网文字层：8 页 posdiff 0、msdiff 0（tokens 797/802/722/727/783/730/885/2151）；pdftotext 印 55,000 B = 网 55,000 B；网 PDF 1,661,392 B < 7 MB。

### 4. 孤儿标点

全版横扫（PIL + svglib 双 advance，1464 行）：独行标点 (a) **0**，行首标点 (b) **0**，8 页全 0。brute-force：以闭标点开头的 `<text>` 元素 5 个（均为 P8 `»` 行中片段），leftmost 0 个。核心集同法横扫亦为 0/0——**0 新增**（`orphan.log`、`orphan-core.log`）。D8/D10 目标行逐行核对见 §5。

### 5. Delta 六点逐项复核（D6–D11，只验不修）

| 点 | 复核实测 |
|---|---|
| D6 `content34.py:78` w=366.05 | width scan（0.1px，本版文字 + `svglib.wrap()`）：区间 **304.3–427.8**，中点 366.05 ✓；P3 桥接仍 3 行逐字相同（`Заполни в перфекте. Следи за` / `вспомогательными глаголами` / `hebben/zijn.`，基线 2303.5/2333.225/2362.95）；p3 SVG 字节一致 |
| D7 `content7.py:19` w=435.85 | 区间 **419.8–451.9**，中点 435.85 ✓；行 1 实测 419.78px ≤ CW 422.5 ✓；P7 桥接仍 3 行逐字相同（基线 725.66/755.385/785.11）；p7 SVG 字节一致 |
| D8 `content56.py:143–144,156` capcn_w=369.3 | 区间 **353.1–385.5**，中点 369.3 ✓；P6 图注仍 4 行，基线 635.02/659.44/683.86/708.28 全不变；行 1 实测 339.08px，末端距盒右沿 39.4px；p6 SVG 字节一致 |
| D10 `content7.py:91–92,100` dt_zh_w=384.3 | 区间 **373.2–395.4**，中点 384.3 ✓；P7 来信仍 2 行逐字相同（`Писем и лучших текстов не поступило` 1783.27 / `— образец; обещание на VOL.5.` 1811.67）；行 1 实测 373.11px，末端距盒右沿 5.39px；p7 SVG 字节一致 |
| D9 `content8.py:75–76` | 三方法一致：REG 键 = text.md:415 答案 = P8 节点 y=2173.64，均为 `Ik maak een surprise met een kort gedicht.`；题干 `Я делаю сюрприз с небольшим стихотворением.`（text.md:415 唯一出现 `небольшим стихотворением` 的行；`kort gedicht` 全文仅见于 415 行）；keydiff 表由 [137,138,140] 变为 [137,138]，140 已移出 ✓。裁图证据 `crop-p8-q140.png`（P8 印出 140. `Ik maak een surprise met een kort gedicht. — surprise (фикс.)`） |
| D11 `content34.py:130` 顶留 62→89，`sh` 611.0→638.0 | 双法重测：SVG 盒 `<rect y=591.6 h=638.0>` 底 1229.6；末行 `18:45 uur.` 基线 1209.49，**盒内余量 +20.11px**；交付卡片 PIL 真墨最低行 1209，余量 **+20.60px**，盒底下 7px 条带 0 墨像素；交付印 PDF 150dpi 渲染（`render-pdf-p4-150dpi.png`）真墨最低行 svg-y 1210，余量 **+19.6px**（1px 量化差，与卡片法一致），7px 条带 0 墨像素。模拟末行偏移 617.89 与 SVG 实测一致；旧 `sh` 611 下余量为 −6.89px（已修）。裁图证据 `crop-p4-programma.png`（末行在盒内，下有明显留白） |

D6/D7/D8/D10 在本版预先不存在（复核前孤儿扫查已为 0/0），四处 w 只复现当前干净断行——p3/p6/p7 SVG 字节一致为证，属结构同步，无重复修。
D3 回归：P2 SVG 字节一致，D3 短式断行与余量与 build-5 相同。

### 6. 语义抽查（防三方一致也查不出的键–干错配；抽查 20 题 + 配套算术/日期）

逐组核对配对题 Q25–28、Q141–144（选项表逐字核对：`content12.py:272–279` a=愿望清单/b=小诗/c=马食/d=门边；`content8.py:78–85` a=小诗/b=新闻节目/c=小组第一/d=门边；配对全部正确）；单题抽查 Q1、Q7、Q11、Q36、Q37、Q83、Q113、Q130、Q137、Q138、Q145、Q149（另有 Q22/Q43–Q45/Q46–Q51/Q57/Q124–Q128/Q133–Q136/Q139 在核对中一并验过，均正确）。要点：

- Q1/Q7 20:45 ✓（P1 正文“Maandag 16 november … 20:45 uur”）；Q11 B Grave en Amsterdam ✓；Q36 `sleutel`（“kreeg hij de sleutel van de stad”）✓；Q37 `editie`（88e editie）✓；Q57 `speelde`（“1–1 thuis tegen Duitsland”）✓；Q83 35 ✓（图表行“Een wortel en een tekening 35”）；图表自洽：35+30=65（Q85）、35+30+20+15=100（Q87）、30（Q84）、15（Q86）✓；Q113/Q130 Berlijn / Duitsland–Nederland ✓；Q137/Q138 俄译准确 ✓；Q139 `De intocht in Amsterdam was de 88e editie.` ✓；Q145–149 对话补全 ✓。
- 算术：Q22/Q45 16 Nov→5 Dec = 19 天 ✓；Q43 14→15 Nov = 1 天 ✓；Q44 12:00–16:00 = 4 小时 ✓；Q46 2026−2009 = 17 年 ✓（P8 答 #46 亦同）。
- 内部一致：积分 NL 8 / GR 8 / DE 5 / SRB 0 在正文、HET PROGRAMMA 盒、Q48/Q126（PSV 26）三处一致 ✓；Speelronde 13 = 21–22 Nov（Q50/Q128 选项顺序不同、答案一致）✓。
- 日期 `date -d` 全验：16 Nov 2026 周一、17 周二、18 周三、19 周四、20 周五、21 周六、22 周日；14 Nov 周六、15 Nov 周日、1 Nov 周日（P5“seizoen begon op zondag 1 november”✓）、24 Nov 周二（P7 预告“Dinsdag 24 november”✓）、29 Nov 周日（“Zondag 29 november”✓）、5 Dec 周六（pakjesavond ✓）。刊头 `WEEK VAN 16 TOT EN MET 22 NOVEMBER 2026` ✓。
- P7 ZINNEN VAN DE WEEK 8 句逐句核对原文逐字一致（P1/P2/P3/P4/P5/P6 各出处与页码标注均对）✓；text.md 词表 gloss 6 行 + 金句 8 行 = 14 个 `>` 行，与 KIT 计数一致 ✓；ABSTRACT.txt 俄语单行、无 ASCII 双引号，含 VOL.4、日期、150 题、A2–B2 ✓。
- “next Sunday”：本版 8 个 SVG 中 0 次出现，无可裁定项（冻结核心表述不适用）。
- text.md:228 对话内编号“1. Kijk zondag om 20:00 uur op RTL 4”是对白行内序号，非练习编号，与练习 Q1（text.md:18）无冲突。

### 7. 目检 8 页（交付卡片逐页看图）

P1–P8 全部看过，无溢出、无重叠、无压页脚、无裁切：P1 头版/议程盒/数字盒/快讯 quiz 齐全；P2 GEDICHT strip gloss 3 行在盒内、ZO ONTHOUD/EN JIJ 盒齐整；P3 桥接与词框正常；P4 HET PROGRAMMA 盒末行在盒内留白明显（见裁图）；P5 照片与图注、EN JIJ 盒齐整；P6 图表 35/30/20/15 与图注 4 行齐整，VOOR OF TEGEN 盒齐整；P7 PAS OP!/HET WOORD/BRIEVEN 盒均在 ZINNEN 线之上收束；P8 练习 113–150 与答案 1–150 齐全、pen 照片在位。
§1.1：调色板 off-palette {}、禁用色（金/红褐）无、stroked rects 0、paper fills 8；VOL.4 各页刊头/页脚共 10 处，VOL.5 共 5 处 = 核心（均为指向下期的 VOL.5 前瞻引用，非误印）；页脚用全角空格分隔，无 `·`。

### 8. 未发现的缺陷

无。未编造任何缺陷与 SHA；所有数据均为盘上实测。

## 观察类事项（不构成缺陷，不修）

- O1（核心继承）：Q130/Q36/Q37 式填空行属正常练习版式，孤儿扫查 0/0，不报缺陷。
- O2（假阳性余波）：P2/P5 奶油盒底 flag 为 2px 容差带内的测量伪报——墨迹全在盒内、盒底下 7px 条带 0 墨像素（双法同证），不构成缺陷。
- O3（最紧余量）：P6 `DE GRAFIEK　УЧЕБНЫЕ ДАННЫЕ` 真墨余量 +9.5px，为全版最紧，但仍在盒内且盒外条带 0 墨；按 STRADDLE 裁定（字形未被裁、墨迹无重叠、与旧版比无回归），记观察。
- O4（计数口径）：简报称 56 标题无一定义能复现；本版实测 59（38 head 出现 + 21 盒标题），已按 59 全集扫查 0 越边。计数差异留协调员定，不影响结论。

## 证据文件（本 scratch）

`PROOF-NOTE.md`、`GATE-LOG.md`、`gates.log`、`gates-ru.json`、`run-rebuild.log`、`render-rebuild.log`、`freeze-core.log`、`occlusion.log`、`creambox.log`、`spill.log`、`orphan.log`、`orphan-core.log`、`boxtitle2.log`、`title-count.log`、`width-scan.log`、`probe-cream-d11.log`、`probe-pdf-d11.log`、`p8-compare.json`、`p8-compare-3way.json`、`registry.json`、`spotcheck.log`、`d9-check.log`、`delivered-svg-sha.txt`、`repro-svg-sha.txt`、`render-pdf-p4-150dpi.png`、裁图 `crop-p4-programma.png` / `crop-p8-q140.png` / `crop-p6-title.png` / `crop-p2-enjij.png` / `crop-p5-enjij.png` / `crop-p2-gedicht.png`。
