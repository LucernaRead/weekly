# W47 zh-cn 家 §8.4 状态核对报告

- 核对员：本轮独立核对员（与建造者、第一轮/第二轮校对员、修复者、*-ru 重建者均不同）
- 核对时间：2026-11-13（UTC；磁盘 96G 已用 / 150G，未触 100G 门限）
- 范围：目标语 zh-cn × 读者母语 de/en/es/fr/it/ja/ko/nl/pt/ru，共 10 版；core-zh-cn（= zh-cn-en）只作交叉核对
- 依据：`~/workspace/weekly-git/SOP.md` §8（校对闭环）；只读核对，未改任何生产文件，未 commit/push/lint --write
- 工作目录：`hidden_files/w47/scratch-verify-zh-cn/`（本报告 + `ru/` 下重校日志与提取文本）

## 结论总览

| 版 | 最后重校记录 | 当前 SHA 对照 | 结论 |
|---|---|---|---|
| zh-cn-de | 第二轮 90628111，(a) 干净 | 印/网/文 3/3 一致 | **VERIFIED CLEAN** |
| zh-cn-en | 第二轮 90628111，(a) 干净 | 印/网/文 3/3 一致 | **VERIFIED CLEAN** |
| zh-cn-es | 第二轮 90628111，(a) 干净 | 印/网/文 3/3 一致 | **VERIFIED CLEAN** |
| zh-cn-fr | 第二轮 90628111，(a) 干净 | 印/网/文 3/3 一致 | **VERIFIED CLEAN** |
| zh-cn-it | 第二轮 90628111，(a) 干净 | 印/网/文 3/3 一致 | **VERIFIED CLEAN** |
| zh-cn-ja | 第二轮 90628111，(a) 干净 | 印/网/文 3/3 一致 | **VERIFIED CLEAN** |
| zh-cn-ko | 第二轮 90628111，(a) 干净 | 印/网/文 3/3 一致 | **VERIFIED CLEAN** |
| zh-cn-nl | 第二轮 90628111，(a) 干净 | 印/网/文 3/3 一致 | **VERIFIED CLEAN** |
| zh-cn-pt | 第二轮 90628111，(a) 干净 | 印/网/文 3/3 一致 | **VERIFIED CLEAN** |
| zh-cn-ru | 第二轮 90628111，(a) 干净，但印/网 SHA 已变 | 文一致；印 `fd6977bff8b0`→`52aa381ae7dd`、网 `e5ce689b3811`→`3e47f038c53b` | **本轮已做全新全量重校（见下），结论 (a) 干净，1 项度量更新（已接受项 F8 数值变化，目视无缺陷）** |

- 9 版 VERIFIED CLEAN：第二轮重校结论 (a) 干净（`scratch-reproof2-w47-zh-cn/PROOF-NOTE-2.md`，2026-11-12 ~18:18，工人 90628111），其后磁盘三 SHA 逐字节未变，KIT 记录值亦一致。
- 1 版（ru）重校：印/网 PDF 在第二轮之后由 *-ru 字体路由重建（工人 C，2026-11-12 23:49–23:50）重建，text.md 未变（SHA `1f11029b4e83` 不变）。本轮按 SOP §8 对 ru 版做全新全量重校，结论 (a) 干净。

## SHA-12 表（磁盘实测，2026-11-13）

| 版 | text.md（字节 / SHA-12） | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） |
|---|---|---|---|
| core-zh-cn | 49,447 / `2aaf8992bbc2` | 33,521,858 / `566554e0ebc8` | 2,434,907 / `6c258be74dac` |
| zh-cn-en | 49,447 / `2aaf8992bbc2` | 33,521,858 / `566554e0ebc8` | 2,434,914 / `2579a61027eb` |
| zh-cn-de | 50,640 / `e11d4f915226` | 33,519,503 / `b104a8b7b81b` | 2,433,265 / `31fffc7ff93c` |
| zh-cn-fr | 51,785 / `4cf31ce982f6` | 33,513,599 / `30ea0661e5c7` | 2,427,467 / `638e9293509b` |
| zh-cn-es | 51,137 / `b5bf366bad5f` | 33,515,603 / `91c8a84ce10b` | 2,428,933 / `86df4f212879` |
| zh-cn-it | 50,924 / `808250dde250` | 33,509,858 / `0649d5e84bdd` | 2,423,711 / `9aef40aa18ad` |
| zh-cn-pt | 50,798 / `0c9d9d5b97ac` | 33,516,115 / `fa6c12699c41` | 2,430,061 / `bfc1a6e4b6bd` |
| zh-cn-nl | 50,025 / `79666191a8b5` | 33,512,271 / `8ac769437ff6` | 2,426,029 / `fad4d6c11db0` |
| zh-cn-ru | 60,498 / `1f11029b4e83` | 33,644,459 / `52aa381ae7dd` | 2,557,060 / `3e47f038c53b` |
| zh-cn-ja | 52,408 / `b0fa1af51e9f` | 35,542,435 / `1e4e8510174c` | 2,826,131 / `21f0e9ba278c` |
| zh-cn-ko | 52,695 / `9f58f841635d` | 36,955,671 / `93cae6913685` | 2,807,966 / `68597c56beb0` |

- 第二轮重校指纹（`scratch-reproof2-w47-zh-cn/fingerprints.txt`）与上表逐项核对：除 ru 版印/网外，全部 30 个值（10 版 × 3 文件）字节与 SHA 均一致；core-zh-cn 三值亦与第二轮表一致。
- ru 版变化说明：重建摘要（`scratch-fix-xru-w47/summary-zh-cn.txt`）记录的印 `52aa381ae7dd…`/33,644,459 B、网 `3e47f038c53b…`/2,557,060 B 与磁盘一致；重建前后文字层多重集相同（22,680 非空字符），本轮独立复核亦相同（见 ru 重校 §2）。

## KIT SHA 核对（10 版全过，无 wave-2 缺口）

- 逐版核对 KIT 记录的印/网/text.md 完整 SHA-256 与字节数与磁盘一致：de/es/fr/it/ja/pt/ru 在 `Artifacts (final)` 节 + `Post-proof fix` 节各记一次；ko/nl 的 Artifacts 节名为 `Artifacts (final — fix round 1…)` / `Artifacts (final, after fix1…)`，值一致；en（core KIT）在 `Post-proof fix record` 节记一次，值一致。
- ru KIT：`Artifacts (final)` 节已更新为新 SHA 与字节数（印 33,644,459 B `52aa381a…`、网 2,557,060 B `3e47f038…`、文 60,498 B `1f11029b…`），另有 `## fix-xru` 节记录修复内容与新 SHA。**KIT 与磁盘一致。**
- 结论：KIT §7（一处称谓：各版 Artifacts/Post-proof fix 记录表）无 SHA 不一致，**wave-2 KIT 清单中无 SHA 更正项**。仅有的 wave-2 记项见文末（F8 数值更新、杂文件）。

## core-zh-cn 交叉核对

- core 印 PDF 与 zh-cn-en 印 PDF 逐字节相同（SHA `566554e0ebc8`，33,521,858 B）；core text.md 与 en text.md 逐字节相同（SHA `2aaf8992bbc2`，49,447 B）。
- core 网 PDF（`6c258be74dac`，2,434,907 B）与 en 网 PDF（`2579a61027eb`，2,434,914 B）差 7 字节：两者 pdftotext 提取文本逐字节相同，属非内容差异（元数据/字体子集化），且两份 KIT 各自记录了自己正确的值（core KIT 记 `6c258be74dac`，en KIT 记 `2579a61027eb`）。第二轮重校已同样记录此差异。**不作缺陷，不入 wave-2。**

## zh-cn-ru 全新全量重校（SOP §8）

重校对象：`2026-w47-zh-cn-ru/` 当前磁盘文件（印 `52aa381ae7dd`、网 `3e47f038c53b`、文 `1f11029b4e83`）。日志见本目录 `ru/logs/`，提取文本见 `ru/print.txt`、`ru/web.txt`。

### 1. text.md 全文通读（2,102 行）

- P1–P8 全文通读：目标语拼写/标点、讲解层对照正文、注释词均出自正文。无拼写、截断、重复词问题。
- 事实逐项复核（与第二轮独立结论一致，不只沿用）：S16 赛程与比分（四分之一决赛 11月4–7日、半决赛 GEN 3–0 IG、BLG 3–1 T1、决赛 11月15日 03:00 纽约巴克莱中心；GEN 瑞士轮 3–0 仅丢一小局对 LYON 2–1；BLG 连赢三支韩国队 HLE/DK/T1；IG 七年重返四强）；邮政局 2025 双 11（22 天 139.38亿件、单日最高 7.77亿件、6.34 仅作干扰项）；湖南顺丰 +约20%、高峰 11月12–15日；中通云仓三波 10月20–21日、10月31日、11月11日最高；高铁急送 196 城、最快 4 小时；深圳读书月 11月1日开幕、11月7日国际美术馆日、11月14日文化馆之夜；电影《试探》11月21日（冯绍峰/李梦/陈雨锶、钢琴家、失踪女友、山间别墅）、《白衣逆行者》原定 11月6日映前撤档、《珠穆朗玛：云中彼岸》11月6日艺联、《我们仅有一次的人生》11月7日（宋佳/文淇）；小雪 2026-11-22（周日）、农历十月十四、二十四节气第 20 个、冬天第 2 个、三候引文。全部星期经 `date -d`（Asia/Shanghai）核验：11月4日周三、5日周四、6日周五、7日周六、8日周日、9日周一、11日周三、12日周四、13日周五、14日周六、15日周日、21日周六、22日周日——与正文一致。
- 150 题答案逐题重推：编号 1–150 连续、无缺重（答案节实测 150 行唯一编号；按页 10/18/18/18/18/18/12/38）；陷阱题核对无误（P8 A Q2“今年是第20个小雪节气”为错，key 114 B；B 大测验各题与题面一致；D 小林段日期与星期全对；F 模范答案实测 138 字，120–180 要求内）。
- 配对题逐组验算全对（P2/P3/P4/P5/P6 五组）；金句 8 条均逐字取自正文、页码锚点齐全；VOL.5 预告、读者园地延期说明齐全。
- 红线：选题 S16 电竞、双 11 包裹、小雪、读书月、电影——无国际政治；目标国是中国，无中国国内政治内容。合规。

### 2. 印/网文本层逐字节一致

- `pdftotext -layout` 印/网提取均为 100,428 B，`cmp` 逐字节相同。
- 与第二轮重建前提取（`scratch-reproof2-w47-zh-cn/logs/ru-print.txt`）比较：非空字符多重集相同（22,680 = 22,680），即 *-ru 重建未改动任何内容字符（行顺序差异仅为提取 flag 不同所致）。

### 3. P8 150 题（机械门）

- `p8.py extract`：150/150，rc=0。
- `p8.py compare`（core-zh-cn P8 vs ru P8）：CLEAN，missing=[]、extra=0、keydiff=[]，rc=0。
- P8 最小字号 PyMuPDF 实测 9.98pt（≥9.75 下限），与第二轮一致。

### 4. 8 页逐页看图

- 用生产目录已有的 `cards/*.png`（重建后产物）逐页目视 P1–P8：无溢出、无重叠、无压页脚、无豆腐块、无截断句；5 张照片与出处在位；刊头 `Lucerna` 每页在位；页脚 `Lucerna 简体中文周报 VOL.4 …` + `Страница N из 8` 齐全；P6 图表两柱分别为 22 天总数与单日最高，文内明示不可直接比大小。
- P1 栏间断句为多栏接排（“每周…”接中栏“周，我们用…”），非截断。
- P7-a2 栏目标题见下文观察项：目视栏间留白清晰，无碰撞（另有放大裁图 `ru/p7-head-zoom.png`）。

### 5. 共享工具机械门禁（只读重跑，`tools/venv/bin/python`）

| 门 | 结果 |
|---|---|
| `p8.py extract` / `compare` | 150/150；CLEAN，keydiff=[] |
| `occlusion_audit.py`（自检先过） | 自检 OK（6 类 planted 全触发，clean 对照静默）；0 flags |
| `spill_sweep.py` | 35 盒，148 候选，0 SPILL，148 OBSERVE，rc=0 |
| `boxtitle_check.py` | 78 titles，928 body lines，0 DEFECT，0 OBSERVE，0 marginal，rc=0 |
| `pdf_edge_scan.py` | 8 页，0 TOUCH，0 NEAR（各边最小距离 ≥53.6pt），rc=0 |
| `d5_creambox_audit.py`（baseline=修前备份，patched=生产） | CREAMBOX PASS，0 defects；P8 keys slack_footer 55.9→54.9 |
| `head_check.py`（重建 run 日志） | 仅 1 项：P7-a2（已接受项 F8，见观察项） |
| 字体路由探针 `probe_xru.py`（仅 zh-cn-ru 只读重跑） | runs=5529，LAT@NotoSans=0，LAT@Newsreader=1811，CYR@NotoSans=4851，CYR@Newsreader=0，CJK+LAT=0，CJK+CYR=801，curly={'Newsreader': 4}——与重建探针值逐项相同，*-ru 修复在位 |
| `head` 宽度独立复测 | 见观察项 O-R1 |

- 说明两处计数变化（非缺陷）：spill 候选 90→148、boxtitle 标题 48→78，均为重建后 SVG 文本 run 按新字体路由重拆所致（元素数 577→753 等）；0 SPILL/0 DEFECT 不变。creambox P6 行数 113→111、diff 77 亦为同因重排；逐页字符多重集与修前备份比较：P1–P4/P6 相同；P5 仅 犯罪→惊悚 ×3（F4）；P7 仅多一 `и`（F8）；P8 仅 F4-key65 gloss 与 F9措辞之差——与 F4–F9 修复逐项对应，无非预期改动。

### 6. 第一轮修复 F4–F9 逐项核实（text.md + 印 PDF 文字层双重核实）

| 修复 | 核实结果 |
|---|---|
| F4《试探》体裁 | text.md `犯罪片` ×0、`惊悚片` ×3（P5 正文 + Q65 选项 A + 填空题干）；印层同；key 65 gloss `саспенс-триллер`。在版 ✓ |
| F5 ja 括号 | 非 ru 版；不适用（ja 版 SHA 未变，第二轮结论覆盖） |
| F6 ko/ja 引文数字 | 非 ru 版；不适用（同上） |
| F7 es/pt 否定晚上 | 非 ru 版；不适用（同上）；ru 版 B1 填空“（不是晚上）”对应 gloss `06:00 — это 早上, а не вечер.`，无误 |
| F8 ru 栏目标题 | text.md :1313 `Финал и посылки`；印层 ×1，`Финал посылки` ×0；P7 目视确认。在版 ✓ |
| F9 ru「结算页」 | text.md :1407/:2021（key 111）`Данные и чекаут сначала, заголовок — последним.`；印层 key 111 同，`Данные и оплата` ×0、`страница оформления заказа` ×0。在版 ✓（`чекаут` 措辞沿用第二轮裁定：可接受） |

### 7. 发现表

**本轮 ru 重校零新内容发现。**（MAJOR 0、MEDIUM 0、low 0。）仅 1 项度量更新（观察项 O-R1，见下），属已接受项 F8 的数值变化，目视无缺陷。

## 观察项（非缺陷，报协调员裁定）

### O-R1：P7-a2 栏目标题 advance 宽度由 422.72 → 426.14（栏宽 422.5px）

- 事实：`head_check.py` 对重建 run 日志仅报 1 项，即 P7-a2 `A2　决赛与包裹　Финал и посылки`——与修前已接受项 KIT F8 同一标题。用该版自身 `svglib.text_w(s, "sans", True, 24)` 独立复测：修前备份 svglib（`_D5_READER=="ru"` 分支）测得 422.72（超 0.22px，与 KIT F8 所记 422.7 一致）；当前 svglib 测得 426.14（超 3.64px）。增量主因是拉丁 `A2` 由 Noto Sans Bold（30.30）改走 Newsreader Bold（34.97），系 *-ru 字体路由修复的直接后果。
- 目视证据：P7 目视 + 栏目标题放大裁图（`ru/p7-head-zoom.png`）——标题一行排完，末词 `посылки` 与 B1 栏之间留白清晰，无碰撞、无压线；`boxtitle_check` 0 DEFECT（真墨 fits）、`occlusion_audit` 0 flags、`pdf_edge_scan` 0 TOUCH/NEAR。advance 超宽 ≠ 墨迹越栏。
- 建议（不作“应改”主张）：KIT F8 数值在 wave-2 更新为 426.1 vs 422.5（超 3.64px），或维持接受现状；是否重排标题由协调员定。本轮不把此项记为缺陷。

### 沿用观察（第二轮 O1–O6，均未变，不重报）

- O4：ru 版目录仍有 `svglib.py.orig` 杂文件（第二轮 O4 已记；插仓前待办：确认 insert 不收杂文件或先清掉）。本轮仅记录，不处理。
- 其余 O1/O2/O3/O5/O6 与第二轮记录一致，无变化。

### 不修项复核（F1/F2/F3/F10）

- F1（P8 题干字号）：P8 字号实测 13.12–14.62pt（题干），答案区最小 9.98pt ≥ 9.75pt，合格；与第二轮一致。
- F2（P1 头条无首字下沉）：P1 目视确认仍无 drop cap（引擎级已知偏差，已裁定不修）。
- F3（选择题选项内折行）：系统性引擎行为，与第二轮相同，未扩大。
- F10（右缘溢出）：`pdf_edge_scan.py` 8 页 0 TOUCH、0 NEAR（edge 门为 governing 门）；与第二轮一致。

## 待修清单 / wave-2 记项

1. **O-R1（ru，观察级）**：KIT F8 数值更新 422.7 → 426.1（超 3.64px），或协调员另行裁定。无内容修复、无重建需要。
2. **O4（ru，插仓前待办）**：目录残留 `svglib.py.orig` 杂文件——插仓时确认 insert 不收杂文件（或先清掉）。第二轮已记，本轮复核仍在。
3. 其余 9 版：无待修项、无 KIT 更正项。

## 附：核对方法与证据位置

- 最后重校记录来源：run-log 2026-11-12 ~18:55 条（二轮重校 90628111 干净）+ `scratch-reproof2-w47-zh-cn/PROOF-NOTE-2.md` 与 `fingerprints.txt`（11 版 × 3 文件全表）。
- ru 重建记录来源：run-log 2026-11-12 23:58 条 + `scratch-fix-xru-w47/summary-zh-cn.txt`（印/网 SHA、探针值、多重集相同）+ `scratch-sweep-xru-occl-2/SWEEP-LOG.md`（occlusion+boxtitle PASS）。
- ru 重校日志：本目录 `ru/logs/`（p8-extract/compare、occlusion、spill、boxtitle、edge、creambox、head、probe.json/probe.log）；提取文本 `ru/print.txt`、`ru/web.txt`；P7 栏目标题放大裁图 `ru/p7-head-zoom.png`；探针复跑脚本 `ru/probe_xru_zhcnru.py`（原 `scratch-fix-xru-w47/probe_xru.py` 仅限 zh-cn-ru 的只读副本）。
- 未动生产文件：全程只读；`occlusion_audit.py --selftest` 单独跑时只出自检行（工具行为：该 flag 仅跑自检），故另以无 flag 方式重跑并记录 0 flags；未跑 `run.py`/`render.py`/`webpdf.py`/`freeze.py baseline`（HEAD 宽度复测用的是已生成的 run 日志 + `text_w` 只读调用，未重渲染）。
