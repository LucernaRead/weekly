# FIX-LOG — W47 zh-cn-es fix1 (D-1 / D-2 / D-3 / D-4, proof1 a700b623 结论 (b))

**范围**：只改 `production/2026-w47/2026-w47-zh-cn-es/` 这一版。核心
`core-zh-cn/`、`tools/`、SOP 与其他版未碰；不 commit、不 push。
工作区：`hidden_files/w47/scratch-fix-zh-cn-es1/`（新建独占；脚本、日志、
渲染件全在内）。`TMPDIR` 全程指向该目录下 `tmp/`。

**前置阅读**：repo 根 `SOP.md`（§1.1、§8）、`AGENTS.md`、
`hidden_files/w47/scratch-fix-es-fr1/FIX-LOG.md`（双方法量测做法参考）。
注：任务所指 `hidden_files/w47/briefs/brief-coordinator.md` 在盘上不存
在（`hidden_files/w47/` 下无 `briefs/` 目录）；工作依据为任务书 + SOP +
proof1 结论 + 前序 fix 的实测方法。

**探针**：`echo test | git hash-object -w --stdin` → `9daeafb…` 成功；
scratch 真实写文件成功后才动手。

## 对象与三 SHA

| 件 | 修前（开工核对，与协调员 18:18 UTC 实测一致） | 修后 |
|---|---|---|
| 印 PDF `Lucerna-VOL4-ES.pdf` | `f05d6126a7f55564787be64e370de7ce05ade6abb38b18fbecc9cb2d070a2508` / 44,799,104 B | `ba184b75daf1896bf528192e6adfad9d7f847bef57f16c43dc048461697c4182` / 44,799,095 B |
| 网 PDF `Lucerna-VOL4-ES-web.pdf` | `249ee578617c1c584f11ef2436d2438a41cf8c8b10b3e24baf3ff45b8396d437` / 2,723,559 B | 未动（同左；见“待办”） |
| 文 `2026-w47-zh-cn-es.text.md` | `edc045da1f0cc5267ec18046a193e055dfbf90e70421d79bcf0ba93f2497f482` / 51,175 B | 未动（同左） |

开工快照：`snapshot-before.sha256`（本版 46 个文件）。

## 改动（4 处；文字零改动，D-4 仅改前缀）

| # | 文件:行 | 改动 | 效果 |
|---|---|---|---|
| D-1 | `content12.py:187` | `f.box("本周生活小日历　Fechas de la semana", …)` 加 `tsize=22`（23→22） | 盒高 247.0→246.0；标题基线 237.0→236.0；盒内 3 行正文各上移 1px |
| D-2 | `content34.py:176` | `p.text(…, "看比赛的中文　Palabras de los partidos", 24, …)` → `21` | 仅该标题一行变；手动盒高不变（`sh` 公式不含标题字号） |
| D-3 | `content56.py:25` | `f.box("这一周的高频词　Palabras de la semana", …)` 加 `tsize=21`（23→21） | 盒高 168.0→166.0；标题基线 714.8→712.8；盒内 2 行正文各上移 2px |
| D-4 | `content8.py:104` | `f.para("Respuesta modelo: " + MODELO, …)` → `f.para("Modelo: " + MODELO, …)` | 前缀缩短 10 字符；MODELO 原文不动；仍 7 行，基线不变 |

- 取字号的依据：每项取满足双方法余量 ≥ +5px 的最小降幅。逐档 PIL
  实测（`title_sweep.py --size=`）：D-1 在 22 时 +8.5（21 时 +27.5，
  过度）；D-2 在 22 时仍 −10.5、21 时 +8.5；D-3 在 22 时仍 −10.5、21
  时 +9.5。D-4 候选前缀 `wrap()` 模拟：`Modelo: ` 与 `Respuesta: `
  均为 0 孤儿，`Modelo de respuesta: ` 仍 1 孤儿；取 `Modelo: `（与
  上方 glossline “Un modelo de N caracteres sigue” 与 ex 注
  “modelo arriba, sección F”一致）。
- D-1 的前情纠正：build #3 的 KIT 称该标题“距山谷照 16.8px”属实，
  但量的是照片（x=1439.5）不是盒边（1411.5）；实测墨 1422.8 已越盒
  11.2px。本次以盒边为准，KIT 该条已改写。

## 实测（PIL 真墨 + 600 dpi 印 PDF 像素，双方法；单位 svg px）

| 缺陷 | 盒右缘 | 修前 PIL 墨 / 余量 | 修前 PDF 像素墨 / 余量 | 协调员值 | 修后 PIL 墨 / 余量 | 修后 PDF 像素墨 / 余量 |
|---|---|---|---|---|---|---|
| D-1 P2 日历盒标题 | 1411.5 | 1420.0 / −8.5 | 1421.5 / −10.0 | 1422.8 / −11.2 | **1403.0 / +8.5** | **1403.4 / +8.1** |
| D-2 P4「看比赛」盒标题 | 1862.0 | 1910.5 / −48.5 | 1912.8 / −50.8 | 1911.2 / −49.2 | **1853.5 / +8.5** | **1856.3 / +5.7** |
| D-3 P5 高频词盒标题 | 961.0 | 989.5 / −28.5 | 991.9 / −30.9 | 992.0 / −31.0 | **951.5 / +9.5** | **954.2 / +6.8** |

- 核心同位对照（PIL，复核任务书数值）：D-1 核心 `"本周生活小日历　This week's dates"`
  墨 1388.0 / +23.5（任务书 +22.0）；D-2 核心 `"看比赛的中文　Match words"` 墨
  1779.5 / +82.5（+82.2）；D-3 核心 `"这一周的高频词　Words of the week"` 墨
  947.5 / +13.5（+12.5）。方法间 ≤1.5px，与 PDF 像素法 ≤2.8px，结论一致。
- D-4：修前 P8 全页孤儿扫描 1 处（y=912.4，`》，故事很有意思。星期日是小雪，天气更冷了，我`，
  `wrap()` 模拟第 5 行一致）；核心 P8 0 处。修后 P8 全页孤儿扫描 **0 处**；
  范文 7 行逐行与模拟一致（`Modelo: 这一周是小雪那一周。星期日凌晨3点，我` … `服，不着凉。`），
  基线 y=816.2…960.5 不变；pdftotext 亦见 `Modelo: …` 且无行首 `》`。
- 全版标题横扫（8 页，PIL）：除 D-1~D-3 外无任何标题余量 < +10；
  修后三项均 ≥ +5（双方法）。纵向奶油盒全扫（PIL 墨底 + PNG 实渲，
  35 盒）：真盒内溢出 0 处（修前修后同）；8 处“盒下标题”抓取是已知
  误报类（脚本 +45px 窗口抓到盒下下一节标题），修前修后同一批、值相同；
  D-1/D-3 盒纵向余量修前修后同为 43.0/41.0（盒缩 1–2px、内容同步上移）。
- 目视：`crop-d1.png` / `crop-d2.png` / `crop-d3.png` 三标题全在奶油盒
  内、右缘留白清晰；`crop-d4.png` 范文 7 行无孤儿。

## 重建（scratch 内，OUT/BASE 重定向）

- 拷贝整版到 `scratch-fix-zh-cn-es1/build/`，`content*.py` 的 `OUT` 与
  `render.py` 的 `BASE` 指向 scratch 内绝对路径，grep 验无生产路径残留
  后运行。修前重建 `build-pre.log`：rc=0，TOTAL 150，0 OVERFLOW/
  TOO WIDE；修后重建 `build-fix1b.log` 与 `render-fix1.log`：rc=0，
  TOTAL 150，8 页卡片 + 印 PDF 44,799,095 B。
- **中途事故（已恢复，如实记录）**：修后第一次同步时直接把生产源
  文件拷进 scratch 覆盖了已打补丁的 `OUT` 行，随后一次 `run.py` 未重
  定向，把生产 `svg/p2/p4/p5/p8.svg` 写成了新构建（正是任务书警告的两
  起事故同款）。发现后立即处理：先把事故版 4 个 SVG 的 SHA 存为
  `accidental-fix1-svg.sha256`；再用修前 scratch 构建件把生产 `svg/`
  恢复成字节原样（核对开工快照：仅 4 个已改源码文件不同）；重新给
  scratch 副本打 `OUT` 补丁并 grep 验净，再在 scratch 内干净重建。
  干净重建的 8 个 SVG 与事故版 SHA **逐字节相同**（构建确定性得证），
  且本次重建确认生产 `svg/` 未被再写；之后才按计划把 scratch 成品
  同步进生产。今后规则：凡从生产拷文件进 scratch，拷完必重打补丁 +
  grep 再运行。
- `freeze.py baseline`（修后同步后，`--build` 生产版目录 +
  `--core-svg` 生产 `svg/`）：**8/8 逐字节相同**（修前同为 8/8）。
  干净重建与事故版相同亦是确定性旁证。

## 逐门结果（全部重跑，详见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| build | rc=0，TOTAL 150，OVERFLOW/TOO WIDE 0；全部 flow 末值与 build #3 相同（P7 teaser 2588.78，P8 keys 2475.7） |
| render | rc=0，8 卡 + 印 PDF 44,799,095 B |
| 标题横扫 + 双方法量测 | 见上表；D-1~D-3 均 ≥ +5，其余标题 ≥ +10 |
| 纵向奶油盒全扫 | 真盒内溢出 0；误报类修前修后同一批 |
| occlusion 审计 | **0 flags**；自检六类全触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX）。但对 D-1~D-3 是空信号（纯填充奶油盒，BOXTITLE 只认描边盒）——已用真墨横扫另行验证 |
| p8 extract / compare | **150/150**；**CLEAN**，missing=[] extra=0，keydiff=[] |
| freeze baseline | **8/8**（修前、修后同步后各一次） |
| freeze diff `--strict-cjk` | rc=0，新增 CJK **0**；修前修后差分增量仅 P8 范文重排 runs（前缀 + 行切分），MODELO 字符不变 |
| 印/网文字层 | 新印 45,052 B vs 生产网 45,062 B；词集差仅 D-4 段（前缀 + 重排行），余全同 |
| P8 最小字号 | **9.98pt**（≥ 9.75 底线，不变）；其余页 10.50–12.75pt |
| §1.1 | 纸 #fbfaf6；fills 修前修后相同（非调色板色为既有图表/照片色）；VOL.4 ×9 / VOL.5 ×1（P7 下期预告，同核心）；徽章：全部徽章矩形内文字确为 A2/B1/B2（拉丁-only） |
| SVG 几何差分 | p1/p3/p6/p7 0 改动；p2 32 元全在 D-1 盒内；p4 1 元（标题字号）；p5 7 元全在 D-3 盒内；p8 16 元全为范文重排 runs |
| 目视 | P2/P4/P5 标题 + P8 范文 4 张裁图，零缺陷 |

## 存活项复测（逐项，不得回退）

- P1 数字盒标题 PIL +25.5（任务书 +24.2，方法差 1.3px）；P1 截稿行
  `content12.py:86` “Cierre: 10 nov. …” 在位，P1 0 改动。
- P4 gloss：6 行、框底 792.2，基线 595.86…744.5 与核心逐值相同（仅
  讲解语种不同）；P4 除 D-2 标题外 0 改动。
- P7 预告带底 2588.78（run 日志，修前修后同）；P8 keys 尾 2475.7
  （同）；P7/P8 除 D-4 外 0 改动。
- D4/D5 与核心全同：p8 compare CLEAN（keydiff=[]，比 es-fr fix1 时的
  [137,138,139] 更干净——本版核心无漂移），freeze CJK 新增 0。
- Badge 拉丁-only：见上表。ABSTRACT.txt 335 B、尾换行在位，未动。
- 12 处声称修复：11 处存活复测通过；未存活的 1 处即 D-1（build #3
  “距山谷照 16.8px”实为量错参照），本次按盒边真正修好。

## 生产零写入核对（收工全版 SHA vs 开工快照）

仅以下 14 个文件不同，其余 32 个（含网 PDF、text.md、ABSTRACT.txt、
p1/p3/p6/p7 的 SVG 与卡片、assets、bslib4/svglib/run.py/render.py、
`__pycache__`）与快照一致：

- 源码（意向改动）：`content12.py`、`content34.py`、`content56.py`、`content8.py`
- 重建输出：`svg/p2-shenghuo.svg`、`svg/p4-tiyu.svg`、`svg/p5-qingnian.svg`、`svg/p8-ceyan.svg`
- 渲染缓存：`cards/p2-shenghuo.png`、`cards/p4-tiyu.png`、`cards/p5-qingnian.png`、`cards/p8-ceyan.png`
- 印 PDF：`Lucerna-VOL4-ES.pdf`（新 SHA 见上）
- KIT：`WEEKLY-KIT.md`（fix1 章节 + 新 SHA + D-1 参照纠正）
- 核心、其他版、工具、SOP 均未动（freeze 基线复核核心 SVG 未变）。

未 commit、未 push。

## 待办（不属本次修复范围，需上游裁定）

1. **生产网 PDF 须在入仓前用已修源码重建**：现网 PDF 仍是 build #3，
   文字层仍含旧前缀 “Respuesta modelo: ” 与孤儿行；其 SHA 不可重现，
   本次按任务书要求未覆盖。印/网文字层差仅 D-4 段（45,052 vs 45,062 B）。
2. **独立 re-proof 另派**（本 fix 只修不校）。
3. 事故教训已记入本日志“重建”一节；工具层面未改（`freeze.py`
   已有防写穿守卫；`run.py` 的 OUT 硬编码是事故根源，是否收进工具
   由协调员定）。

## 遗留文件（本 scratch 内）

`probe.txt`、`snapshot-before.sha256`、`accidental-fix1-svg.sha256`、
`title_sweep.py`、`title-sweep-baseline.log`、`title-sweep-all-baseline.log`、
`title-sweep-after.log`、`pdf_right.py`、`pdf-right-D{1,2,3}-{pre,pre2,post}.png`、
`orphan.py`、`orphan-baseline.log`、`orphan-baseline2.log`、`orphan-after.log`、
`ink_check.py`（es-fr 版补 Noto Serif CJK SC）、`ink-baseline.log`、`ink-after.log`、
`occlusion-selftest-after.log`、`occlusion-after.log`、
`p8-extract-after.json/.log`、`p8-compare-after.json/.log`、
`freeze-baseline-pre/`、`freeze-baseline-pre.log`、`freeze-baseline-post/`、
`freeze-baseline-post.log`、`freeze-diff-pre.json/.log`、`freeze-diff-after.json/.log`、
`print.txt`、`web.txt`、`print-layout.txt`、`web-layout.txt`、
`style_check.py`、`style-after.log`、`build/`（scratch 构建副本 + SVG +
卡片 + 新印 PDF）、`build-pre.log`、`build-fix1.log`（事故版）、
`build-fix1b.log`（干净重建）、`render-fix1.log`、
`crop-d1.png`、`crop-d2.png`、`crop-d3.png`、`crop-d4.png`、`tmp/`。
Scratch 总计约 200 MB（含两份 freeze 副本与构建件，供 re-proof 复核）。
