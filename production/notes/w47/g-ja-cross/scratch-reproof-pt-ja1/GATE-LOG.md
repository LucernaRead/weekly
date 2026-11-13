# GATE-LOG — 2026-W47 pt-ja re-proof（独立实跑记录）

复校员 re-proof，2026-11-11。全部机械门均为本次在磁盘文件上实跑，
不采信 KIT 的数字（仅作对照，差异见 §0）。工具：
`~/workspace/weekly-git/tools/venv/bin/python`；
正典 creambox `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`
（md5 `ee7a55d8b2057cf4ad42a97bb1197383` ✓）。
工作目录与源文件：只读核验，未改动、未重建、未 commit、未 push。
`run.py` 只在 scratch 内 `run-copy/` 副本跑（content 脚本会写 SVG，绝不在生产目录跑）；
web PDF 只在 scratch 内重渲染比较，从未覆盖生产网 PDF。
日志与原始输出均存本 scratch 目录。

## §0 版身份与 KIT 对照差异

| 项 | 磁盘实测 | KIT 所称 | 结论 |
|---|---|---|---|
| 印 PDF 字节/SHA | 24,991,049 / `e45f4a94…da8a08` | 同 | ✓ 一致（重建后新版） |
| 网 PDF 字节/SHA | 1,680,796 / `ff67441e…e281e8` | 同 | ✓ 一致（重建后新版） |
| text.md 字节/SHA | 37,915 / `90dcdcca…c9830` | 同 | ✓ 一致（重建后新版） |
| occlusion 标记 | **0 flags**（本版与核心各 0，自检 OK，见 §2） | 1 flag（P1 LINEX 擦线） | **不一致**：本次实跑 0 标记，且该擦线几何已不存在（分隔线由 y=2312 移至 y=2350，距墨迹顶 38.4px；P1 SVG 中已无 '2312' 字样）；KIT 的 1 flag 为旧版/旧轮次结果。判据以本次实跑 + PIL 实测 + PDF 像素为准。 |
| 印/网文字层词数 | 各 7,038 词（pdftotext token 计） | 未载 | proof1 旧版各 7,040 词；−2 词即 D4 标题缩短所致（见 §7） |
| P8 最小字号 | 10.125pt（PyMuPDF span 实测，§7） | — | ✓ 高于 SOP §1.1 底线 9.75pt |
| gates | 16/16 PASS | 16/16 PASS | ✓ 一致 |
| p8 extract/compare | 150/150，CLEAN，keydiff [137,138] | 同 | ✓ 一致 |
| freeze baseline/diff | 8/8；diff 新增 CJK 3,246 | 8/8；— | 总量由 proof1 的 3,255 变为 3,246，−9 全部分解见 §4 |
| freeze 版内自比对 | 8/8（run-copy SVG 与 shipped SVG 字节一致） | — | ✓ 本版可复现 |
| run.py | rc=0，TOTAL 150 | — | ✓（scratch 副本跑） |
| check_s11 改编 | ALL PASS（见 §6） | — | ✓（en 版同一检查项改编，本版无专用脚本） |

## §1 run.py（构建自检，scratch 副本）——rc=0，TOTAL 150

`run.log`（`run.py` 于 `run-copy/` 内，rc=0）：
`P8 saved, TOTAL exercises: 150`；by level {A2: 48, B1: 71, B2: 31}；
by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}；
`ALL DONE`。副本重建的 8 个 SVG 与生产目录 shipped SVG **字节一致**
（`diff -r --brief run-copy/svg production/.../svg` 无差异）——本版可复现。

## §2 gates.py（构建自检）——16/16 PASS

`gates.log`（`python -u gates.py`，rc=0），16 项全 PASS，FAILURES: none：
VOL.4 + 日期 ✓；副标题三话题 ✓；页脚+页码 8/8 ✓；
无 VOL.3 版标残留 ✓；截稿注 + 决赛命名 ✓；
P1 刊头行宽 ≤1820（330 行 319.2 / 372 行 453.0）✓；
同基线墨迹碰撞 0 ✓；页框墨迹穿越 0（最小余量 L/R/T/B = 47.0/47.7/35.0/33.0）✓；
P6 图表标签 GRAZE 0% ✓；gloss 29 项枚举 + 词头存活 ✓；
P7 金句 2× + 页签 + 日语 8/8 ✓；读者角逐字串 5/5 ✓；图片 + credits 5/5 ✓；
P7 金句区不入预告框（max 基线 2351.17）✓；P1 头条 ≤56 去空白字符（41）✓。

## §3 occlusion_audit.py（几何遮挡审计）——本版 0 flags，核心 0 flags

`occlusion.log` / `occlusion.json`（`tools/occlusion_audit.py svg --json`，rc=0）：
`selftest OK: planted classes fired {BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX}; clean controls silent`
`svg: 0 flags`。
`occlusion-core.json`（同工具扫 `core-pt/svg`）：自检 OK，`0 flags`。
KIT 所称 "1 P1 LINEX flag" 在本版与核心均未复现；且旧擦线的几何根因已消失
（见 §0：分隔线 y=2312→2350）。判据以本次实跑为准。

**盲区说明（本次另行实测，不因 0 标记放过）：**
奶油框内溢出/框标题横向溢出/降部溢出——工具的 BOXTITLE 只管有边框的框，
奶油框（无边框）横向不管；creambox 只核基线纵向。另行实测见 §5–§6：
D1/D2/D3 均已修净（框底在核心加高），D4 修净，全版横向 0 溢出。

## §4 p8.py + freeze.py

### §4.1 p8 extract/compare

`p8-extract.log`：`noted set = 150 of 150 (parse: lines)`，rc=0。
`p8-compare.log` / `p8-compare.json`（vs `core-pt/svg/p8-avaliacao.svg`，rc=0）：
`core 150 noted / edition 150 noted / status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`。
keydiff 逐个裁决（与 proof1 一致，本次重验）：
137：`11月20日金曜日は全国の祝日です。`——Q137 源句
`Sexta, 20 de novembro, é feriado nacional.` 的正确日语译文。接受。
138：`パルメイラスはPK戦で5–4で勝ちました。`——Q138 源句
`O Palmeiras venceu nos pênaltis por 5 a 4.` 的正确日语译文。接受。
其余 148 键与核心逐字一致。

### §4.2 freeze baseline（核心标准比对）——8/8

`freeze-baseline.log`（`freeze.py baseline --build production/2026-w47/core-pt
--core-svg production/2026-w47/core-pt/svg`，rc=0）：
`baseline: 8/8 SVGs byte-identical (repointed files: none)`，
`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。

### §4.3 freeze baseline（版内自比对）——8/8

`freeze-self.log`（`freeze.py baseline --build <pt-ja 版目录>
--core-svg <pt-ja 版目录>/svg --out freeze-self`，rc=0）：
`baseline: 8/8 SVGs byte-identical`。与 §1 的 run-copy 字节一致交叉印证。

### §4.4 freeze diff（核心→本版）——新增 CJK 3,246

`freeze-diff.log` / `freeze-diff.json`（rc=0）：
每页增/删字符串：P1 +27/−25、P2 +36/−33、P3 +29/−28、P4 +29/−26、
P5 +44/−41、P6 +21/−21、P7 +51/−46、P8 +402/−489；
**TOTAL added CJK characters: 3246**（proof1：3,255）。
U+3000（全角空格，分隔符）新旧均为 **9**（P1 2、其余各页 1）——与 en-pt KIT
所载 en 版 "added CJK = only 9× U+3000" 的 9 一致，但 ja 版新增 CJK
主体是日语讲解层（3,246），"新增 CJK 仅 U+3000" 作为字面表述不适用于
ja 版；可核实的事实是：U+3000 恰为 9、无新增简繁-only 中文字符、
无新增葡语目标语文本（增量全部为日语讲解层字符串与家具行）。
−9 分解（新旧 `freeze-diff.json` 逐字符对账，完全闭合）：
P1 −3（で/る/見：D4 标题「数字で見る」→「数字」）；
P2 −3（P2 C 节说明「数字で見るで埋めよう」→「数字で埋めよう」−3，
D5 gloss 日→、净 0）；
P4 +3（者 −1、タイトル +4：L215 `o título 優勝者`→`優勝/タイトル`）；
P6 −3（で/る/見：P6 `O FIM DE NOVEMBRO EM NÚMEROS` 副标
「11月末の数字で見る」→「11月末の数字」）；
P8 −3（日/ま/で：Q65 注 `13:30 18日まで:30`→`13:30–18:30`）；
P3/P5/P7 为 0。合计 −9 ✓。
（`--strict-cjk` 未用：ja 版新增 CJK 是讲解层替换中文层的预期量。）

### §4.5 P8 简析注差异说明（沿用 proof1 §4a，本次重验）

核心 P8 多处简析注为空（`119. A — `、`123. B — `、`52. b — agregado=`），
ja 版填入日语层简析（`119. A — Enem`、`123. B — PK`、`52. b — agregado=2`），
属 fan-out 简析本地化设计，非目标语改动；键本身与核心一致（§4.1）。

## §5 creambox.py 全版扫描 + PIL 真墨迹 + PDF 渲染像素

`creambox-all.log`（正典 creambox.py，8 页全扫）：31 个奶油框。
`creambox-core-all.log` 未重跑（proof1 已扫；本次几何比对直接读 core SVG
rect，见 §5.3）。

### §5.1 D1/D2/D3（核心框加高修复，三法一致）

| 项 | 旧框底→新框底 | 末行基线 | PIL 墨迹底−框底 | creambox clearance | PDF 像素（200dpi） |
|---|---|---|---|---|---|
| D1 P1 `em Brasília. (Página 4)` | 2310.0→**2348.0**（+38） | 2327.6 | **−15.4**（墨底 2332.6） | +20.4 / desc +14.4 | 奶油至 2347，纸色自 2348；墨行 2313–2332 |
| D2 P3 `16h30.` | 525.0→**551.0**（+26） | 540.6 | **−10.4**（墨底 540.6） | +10.4 / desc +3.9 | 奶油至 550，纸色 551–576；墨行 525–540 |
| D3 P6 `Página do Participante.` | 840.0→**854.0**（+14） | 840.8 | **−8.2**（墨底 845.8） | +13.2 / desc +6.9 | 奶油至 853，纸色 854–865；降部墨行 826–845 |

三框的新框底在 **core-pt SVG 中同值**（P1 2348.0 / P3 551.0 / P6 854.0），
修复落在核心、经 fan-out 到位。下方间距：D1 框底 2348 → QUIZ 标题基线
2386（分隔线 y=2350 在其间）；D2 框底 551 → 下一框顶 577（26px）；
D3 框底 854 → 下一框顶 866（12px）。均无相接/碰撞。
目视：`crop-p1-d1.png`、`crop-p3-d2.png`、`crop-p6-d3.png` 均为框内。
注：`ink.py` 原脚本对 D3 硬编码旧框底 840 仍打出 +5.8——以现框底 854 计
为 −8.2（`dcheck.py` 已按现框底重算，三法一致）。

### §5.2 BELOW-WINDOW 行逐个裁决（现版 5 行，D1/D2/D3 已无）

| 行 | 偏移 | 裁决 |
|---|---|---|
| P1 `AGORA VOCÊ　さあ、あなたも` | +37.0 | 下节标题，假阳性 |
| P2 `Atenção: o feriado é nacional…` | +32.0 | 正文续段（框外正文），非框内溢出 |
| P3 `UM DIA, DOIS SENTIDOS` | +37.0 | 下节标题，假阳性 |
| P6 `EXERCÍCIOS　6ページの練習` | +42.0 | 下节标题，假阳性 |
| P6 `解答は8ページ　レベルは混ざっています。番号で答えを探そう` | +42.0 | 下节标题同行，假阳性 |

### §5.3 desc-clear 负值（6 处，均为误报）

`い。`−0.9 / `ください。`−0.9 / `さい。`−0.9 / `ください。`−1.0 /
`2027.`−1.1 / `記憶。`−1.5。PIL 真墨迹实测（`ink.py` §A，沿用 proof1 方法
重跑）：墨迹底均在框底内 2.5–5.4px（日语假名/数字无降部字母，公式高估）。
**creambox 0 真溢出。** P7-TOOLBOX 汇总：3 框，min inside clearance +4.5，
min desc-clear −1.5（上条已证为误报）；ERROS COMUNS +32.6、CARTAS +9.6。

### §5.4 横向扫描（hscan.py，全版 PIL 真墨迹）——0 溢出

`hscan.log`：`JA: 31 cream boxes, 0 horizontal-overflow lines`；
`CORE: 31 cream boxes, 0 horizontal-overflow lines`。
D4 已修净（见 §6）。全 8 页墨迹右缘 >1900 或左缘 <50 的行数为 0
（`ink.py` §E/§F 重跑）。

## §6 框标题逐个实测（PIL）+ 最紧处 PDF 渲染像素交叉验证

`dcheck.py` 全版：31 框 ×（标题行 + 框内最宽行），共 58 行，
**最小余量 +18.5px，0 行 <5px**。最紧 12 行（见 `dcheck.log`）：
+18.5 P2 解説框标题 / +18.5 P5 解説框标题 / +20.5 P6 解説框标题 /
+21.9 P1（B1 最宽行）/ +22.5 P1 末块最宽行 / +22.5 P2 SÁB 框标题 /
+22.5 P3 E VOCÊ 最宽行 / +22.5 P7 两框最宽行 / +22.9 P5 最宽行 /
+23.5 P2 最宽行 / +24.5 P4 最宽行。
PDF 渲染像素交叉验证（200dpi，阈值 <110 与 <200 一致）：
- D4 P1 数字框标题 `A SEMANA EM NÚMEROS　数字`：PIL 墨迹右缘 1351.0，
  PDF 墨迹右缘 1348，框右缘 1411.5，余量 **+60.5（PIL）/+63.5（PDF）**。
- 最紧 P2 标题：PDF 墨迹右缘 934，余量 **+27**（PIL +18.5）。
- 最紧 P5 标题：PDF 墨迹右缘 941，余量 **+20**（PIL +18.5）。
PDF 余量均大于 PIL（CairoSVG 与交付 PDF 渲染差约 3px，P2 处差 8.5px
源于末字 `·` 的渲染口径；边缘裁决以交付 PDF 为准，双法结论一致：通过）。
P1 全版墨迹右缘最大 1861.8（页脚行 y=2624），距内容边 1910 余量 48.2px，无溢出。

## §7 印/网文字层比对 + P8 最小字号实测 + 旧→新文本差

- `pdftotext -layout`：印 `print.txt` / 网 `web.txt` 各 107,708 字节；
  **各 7,038 词，词多重集差 = 0**；各 8 页；版面 1462.5×2025pt。
  （proof1 旧版各 7,040 词；−2 词 = D4 标题「数字で見る」→「数字」的
  token 变化；旧→新多重集差为删 8/增 6 个 token，均为 D4/D5/Q65/L215
  与 O2 的改动，无其他文本变化——见下。）
- 旧→新印 PDF 文本层 diff（proof1 `print.txt` 对照）：除排版换行噪音外，
  实质改动仅 5 处：① D4 `数字で見る`→`数字`；② D5 `土曜日16日:30`→
  `土曜日16:30、`；③ Q65 `13:30 18日まで:30`→`13:30–18:30`；
  ④ L215 `título 優勝者`→`título 優勝/タイトル`；
  ⑤ P2 C 节 `1ページと2ページの数字で見るで埋めよう`→`数字で埋めよう`
  与 P6 副标 `11月末の数字で見る`→`11月末の数字`（D4 同类）。
- PyMuPDF span 实测（印 + 网一致）：**全版最小字号 10.125pt，仅在 P8**
  （605 个 span 在最小值，如 `1. consciência — consciência =`），
  高于 SOP §1.1 底线 9.75pt。10.125pt = SVG 13.5 单位 × 0.75。

## §8 check_s11 改编版（en 版同一检查项，pt-ja 改编）——ALL PASS

`check_s11_ptja.py`（自写进本 scratch，未动 en 原件；en 原型见
`scratch-delta-en-pt/check_s11.py`）。改编点：core-pt 对照、pt 版 8 个
SVG 文件名、P8 无 en 式 cloze `(113)` 空白/`Levels:` 行/WRITING 头——
改查 pt P8 结构（Q113/Q120/Q145 题号、Q120 [B1] 徽章、E TRADUZA 节头、
4×`訳` 标签）；registry 不在版目录，level 取自 scratch 副本重跑的
`registry-150.json`。`check_s11.log`（rc=0）：
chip rects core=ed：P1 10/10、P2 15/15、P3 18/18、P4 15/15、P5 18/18、
P6 18/18、P7 12/12、P8 35/35；colour set core 21 = edition 21，
extra none、missing none；badge 色 A2 #5c6e30 / B1 #46581f / B2 #37402f
均在版内；P8 min font 13.5 SVG 单位 = 10.125pt；
P8 number 113./120./145. 均在位；P8 Q120 [B1] chip OK；
P8 'E TRADUZA' 节头在位；`訳` 标签 4 个。
**ALL §1.1/P8 CHECKS PASS。**

## §9 keycheck 150/150 + 事实核实

`keycheck-150.json` / `keycheck-table.txt`：150 题逐题手验，
**150/150 正确**。机械三源（registry / P8 印键 / text.md Respostas）
149/150 逐字一致，仅 Q150 为自由写作（语义一致，范文按空格重数确为
88 词）。逐题依据见 JSON 内 `basis` 字段；要点：Q83–87 图表数重算
（15/10/5/15/ prazo）；Q120 5 小时；Q131=A；Q137/138 日语译文正确；
Q70/Q73 题干配对已在 P5 SVG 上核对（y=1808 `...começa a espera pelo ___.`
→ gabarito；y=2075 `...começa a ___.` → espera），三源同错类风险已排除；
Q129–132 与 C 节 Rafael 短文逐句核对一致。

**外部事实来源（本次独立检索，2026-11-11）：**
- 圣保罗 GP 2026：Norris 冠军、Verstappen 第二、Hadjar 第三，Mercedes
  锁定车队总冠军——fia.com / formula1.com / ESPN / Sky Sports
  （均为 2026-11-08/09 报道一致）；Q51/Q63/Q124 均正确。
  （proof1 未验 F1，本次补验。）
- Grêmio 争第 6 冠（已有 5 冠 1989/1994/1997/2001/2016）、Palmeiras
  争第 5 冠（已有 4 冠 1998/2012/2015/2020），与 P4 正文一致；
  Q146/Q147 正确。
- 巴西杯半决赛比分/总比分/点球 5–4/决赛 12月6日单场马内·加林查、
  Enem Edital nº 64/2026 §15.1、第二天 11月15日、官方答案窗口 27–30日、
  个人成绩 2027年1月：沿用 proof1 已验结论，本轮 Q47–50/65–69/88–92/
  122–123 与之一致，无矛盾。
- 日期星期：proof1 已验 16 个日期；本轮重验关键日期（11月20日周五、
  21日周六、22日周日、27日周五、12月6日周日）与刊内一致。

## §10 弯引号 + 字符扫描 + E 节本地化

- U+201C / U+201D：SVG 各 2（均在 `p8-avaliacao.svg`，E 节 Q139/140 两句日语句），
  text.md 各 2，印/网 PDF 文本层各 2，P8 渲染正常。
  U+2019：全版 0。« / »：SVG 与 text.md 各 40（葡语引号，按习惯使用）。
- SVG 与 text.md 中「翻譯」「翻译」「中文」均为 0；简繁-only 字符 0；
  P8 E 节标签 4×`訳`，节标题 `E · TRADUZA`（目标语节名）；`..`（非 `...` 者）0；
  ` :` 0；`?2文`/`?Write`/`( (` 0。
- P7 金句 8 条在 SVG 全文各出现恰好 2 次（`gates.py` 亦 PASS）；范文重数 88 词（§9）。
- `«consciência»` vs `« consciência »`：现两处均为带内空格式（P1 与 P7 各 1），
  proof1 O4 的不一致已随重建统一。

## §11 判为非缺陷的项

- desc-clear 6 处负值：PIL 真墨迹均在框底内 2.5–5.4px（§5.3），公式误报。
- BELOW-WINDOW 标题行 +32/+37/+42：下节标题，非溢出（§5.2）。
- P1 刊头副标语替换（`badge372` 日语版标识行）：标准 fan-out 家具，
  en/fr 版同式；刊内无溢出。
- P8 简析注：核心留空处由日语层填注（§4.5），设计如此；键一致。
- freeze diff 新增 CJK 3,246：日语层替换中文层的预期量，无新增葡语文本（§4.4）。
- keydiff [137, 138]：正确日语译文（§4.1）。
- P1 LINEX 擦线（proof1 O1）：分隔线已移至 y=2350，几何消失；工具 0 标记（§0/§3）。
- P2 C 节说明 `数字で見るで埋めよう`（proof1 O2）：已随标题缩短变为
  「数字で埋めよう」，仅存于 `p2-vida.svg`（text.md 无此行，无不一致）。
- P3/P4 栏位孤悬标题（proof1 O3）：核心流式排版行为，目视无重叠/截断。
- D6 之外的标语：en/fr 版同用国家主语换喻（英/法语惯用），不牵连本版判定；
  D6 只改 ja 版一词（见 PROOF-NOTE）。

## §12 未跑 / 未决

- 无。本任务要求的全部机械门均已实跑（run.py、gates、occlusion 本版+核心、
  p8 extract/compare、freeze baseline 核心+版内自比对、freeze diff、
  creambox 全版、hscan 横向、PIL 真墨迹、PDF 渲染像素、印/网文字层、
  P8 字号实测、弯引号扫描、check_s11 改编、keycheck 150）。
- 遗留：D6 待 `tables_ja.py:202` 一词之改 + 重渲染本版；修后须从头再做
  一轮全量复校，方可定稿。
