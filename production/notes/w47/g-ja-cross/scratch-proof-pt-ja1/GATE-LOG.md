# GATE-LOG — 2026-W47 pt-ja proof1（独立实跑记录）

复校员 proof1，2026-11-11。全部机械门均为本次在磁盘文件上实跑，
不采信 KIT 的数字（仅作对照，差异见 §0）。工具：
`~/workspace/weekly-git/tools/venv/bin/python`；
正典 creambox `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`
（md5 `ee7a55d8b2057cf4ad42a97bb1197383` ✓）。
工作目录与源文件：只读核验，未改动、未重建、未 commit、未 push。
日志与原始输出均存本 scratch 目录。

## §0 版身份与 KIT 对照差异

| 项 | 磁盘实测 | KIT 所称 | 结论 |
|---|---|---|---|
| 印 PDF 字节/SHA | 24,992,044 / `04f284ed…da7fb` | 同 | ✓ 一致 |
| 网 PDF 字节/SHA | 1,644,666 / `339d2b05…06a4` | 同 | ✓ 一致 |
| text.md 字节/SHA | 37,892 / `893e8574…bb2ac` | 同（KIT 未载字节数） | ✓ 一致 |
| occlusion 标记 | **0 flags**（自检 OK，见 §2） | 1 flag（P1 LINEX 擦线） | **不一致**：本次实跑 0 标记；PIL 实测擦线几何仍在（约 1.4px 高，见 §2 与 PROOF-NOTE O1），小于工具 LINEX 阈值（重叠 ≥9px² 且高 ≥3px）故工具不报；KIT 的 1 flag 应为旧版工具/旧轮次结果。判据以本次实跑 + PIL 实测为准。 |
| 印/网文字层词数 | 各 7,040 词（pdftotext token 计） | 各 6,897 词 | 计数口径差；关键量——词多重集差 = 0——一致。 |
| P8 最小字号 | 10.125pt（PyMuPDF span 实测，§7） | 10.125pt | ✓ 一致（实测，非配置值） |
| gates | 16/16 PASS | 16/16 PASS | ✓ 一致 |
| p8 extract/compare | 150/150，CLEAN，keydiff [137,138] | 同 | ✓ 一致 |
| freeze baseline/diff | 8/8；diff 新增 CJK 3,255 | 8/8；3,255 | ✓ 一致 |
| P8 末行 y | 2504（KIT 称 flow end y=2504） | 同 | ✓（未独立重测末行 y，P8 目视无溢出） |

## §1 gates.py（构建自检）——16/16 PASS

`gates.log`（`python -u gates.py`，rc=0）：
VOL.4 + 日期 ✓；副标题三话题 ✓；页脚+页码 8/8 ✓；
无 VOL.3 版标残留（VOL.3 仅在 P7 披露中作被引承诺期）✓；
截稿注 + 决赛命名 ✓；P1 刊头行宽 ≤1820（330 行 319.2 / 372 行 453.0）✓；
同基线墨迹碰撞 0 ✓；页框墨迹穿越 0（最小余量 L/R/T/B = 47.0/47.7/35.0/33.0）✓；
P6 图表标签 GRAZE 0% ✓；gloss 29 项枚举 + 词头存活 ✓；
P7 金句 2× + 页签 + 日语 8/8 ✓；读者角逐字串 5/5 ✓；图片 + credits 5/5 ✓；
P7 金句区不入预告框（max 基线 2351.17）✓；P1 头条 ≤56 去空白字符（41）✓。
FAILURES: none。

## §2 occlusion_audit.py（几何遮挡审计）——0 flags

`occlusion.log` / `occlusion.json`（`tools/occlusion_audit.py svg --json`，rc=0）：
`selftest OK: planted classes fired {BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX}; clean controls silent`
`svg: 0 flags`。

**盲区说明（本次另行实测，不因 0 标记放过）：**
- 奶油框内溢出/框标题溢出/横向溢出/降部溢出——工具的 BOXTITLE 只管有边框的框，
  奶油框（无边框）横向不管；creambox 只核基线纵向。另行实测见 §5：检出 D1/D2/D3/D4。
- P1 LINEX 擦线（PROOF-NOTE O1）：PIL 实测规则线 y=2312（band [2311,2313]，线宽 2）
  与 `em Brasília. (Página 4)` 墨迹顶 2311.6 相交约 1.4px 高 × 约 3px 宽
  （仅重音顶部；线画在文字之后，文件偏移 962101 > 962057）；
  小于工具 LINEX 阈值（`occlusion_audit.py:466`：重叠 ≥9.0px² 且宽 ≥3.0 且高 ≥3.0），
  故工具 0 标记。200dpi 裁图 `crop-p1-linex.png` 上该线仅轻触重音顶部，常读尺寸不可见。
  记 O1，不计缺陷。
- KIT 称该擦线“1 flag”与本次 0 标记不一致：应为工具版本/轮次差；本次自检通过，
  0 标记为本次实跑结论。

## §3 p8.py——extract 150/150；compare CLEAN，keydiff [137, 138]

`p8-extract.log`：`noted set = 150 of 150 (parse: lines)`，rc=0。
`p8-compare.log` / `p8-compare.json`（vs `core-pt/svg/p8-avaliacao.svg`，rc=0）：
`core 150 noted / edition 150 noted / status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`。

**keydiff 逐个裁决：**
- 137：核心键为葡语原文句，ja 键 `11月20日金曜日は全国の祝日です。`——
  Q137 源句 `Sexta, 20 de novembro, é feriado nacional.` 的正确日语译文。接受。
- 138：ja 键 `パルメイラスはPK戦で5–4で勝ちました。`——
  Q138 源句 `O Palmeiras venceu nos pênaltis por 5 a 4.` 的正确日语译文。接受。
- 其余 148 键与核心逐字一致（`p8-compare.json`）。

## §4 freeze.py——baseline 8/8；diff 新增 CJK 3,255（预期内）

`freeze-baseline.log`（`freeze.py baseline --build production/2026-w47/core-pt
--core-svg production/2026-w47/core-pt/svg`，rc=0）：
`baseline: 8/8 SVGs byte-identical (repointed files: none)`，
8 页 sha256 逐一一致；`core integrity: shipped core SVGs unchanged by the run`。

`freeze-diff.log` / `freeze-diff.json`（`freeze.py diff --core-svg … --edition-svg …`，rc=0）：
每页增/删字符串：P1 +28/−26、P2 +36/−33、P3 +29/−28、P4 +29/−26、P5 +44/−41、
P6 +21/−21、P7 +51/−46、P8 +404/−489；**TOTAL added CJK characters: 3255**。
逐项核对增/删 Latin 残留：全部为 (i) 葡萄牙语词头 + 日语 gloss 的讲解层字符串、
(ii) 家具行（刊头/节名 + 日语副标）、(iii) P8 答案简析（核心留空处由日语层填注，
如 `119. A — Enem`、`123. B — PK`、`144. a — agregado=2`，见 §4a）、
(iv) P1 刊头副标语替换为日语版标识行 `badge372`（与 en/fr 版同为标准 fan-out 家具）。
**无新增葡语目标语文本。**（`--strict-cjk` 未用：ja 版新增 CJK 是讲解层替换中文层的预期量，
与 KIT 的 3,255 一致。）

### §4a P8 简析注差异说明

核心 P8 多处简析注为空（`119. A — `、`123. B — `、`52. b — agregado=`），
ja 版填入日语层简析（`119. A — Enem`、`123. B — PK`、`52. b — agregado=2`），
en/fr 版亦各自填入读者语完整简析句。属 fan-out 简析本地化设计，非目标语改动；
键本身与核心一致（§3）。

## §5 creambox.py 全版扫描 + PIL 真墨迹实测

`creambox-all.log`（正典 creambox.py，8 页全扫）：31 个奶油框。
`creambox-core-all.log`（同工具扫 core-pt）：31 框，对照用。

### §5.1 框内末行（纵向）

- 全部 31 框 inside-only clearance ≥ +4.5px（最小：P7 A PALAVRA 框 +4.5）。
- 6 处 desc-clear 负值（−0.9…−1.5）均为 0.30em allowance 误报，PIL 真墨迹实测
  （`ink.py`/`ink.log`，用本版 svglib 同款字体）墨迹底均在框底内：
  P2 E VOCÊ `ください。` −3.0px；P3 E VOCÊ `い。` −3.1px；P4 E VOCÊ `さい。` −3.1px；
  P5 数字框 `2027.` −5.4px；P5 E VOCÊ `ください。` −3.1px；P7 A PALAVRA `記憶。` −2.5px；
  另 P2 SÁB 21 框 `対フラメンゴ` −4.8px。——日语假名/数字无降部字母，公式高估。
  **(b) 类在 P3/P5 未复现。**
- P7-TOOLBOX 汇总：3 框，min inside clearance +4.5，min desc-clear −1.5
  （上条已证为误报，真墨迹 −2.5px）；ERROS COMUNS +32.6、CARTAS +9.6。
  **(c) 通过。**

### §5.2 BELOW-WINDOW 行逐个裁决

| 行 | 偏移 | 裁决 |
|---|---|---|
| P1 `AGORA VOCÊ　さあ、あなたも` | +37.0 | 下节标题，假阳性 |
| P1 `em Brasília. (Página 4)` | +17.6 | **D1**：同流续行整行漫出（§5.3） |
| P2 `Atenção: o feriado é nacional…` | +32.0 | 正文续段（框外正文），非框内溢出 |
| P3 `UM DIA, DOIS SENTIDOS` | +37.0 | 下节标题，假阳性 |
| P3 `16h30.` | +15.6 | **D2**：同流续行整行漫出（§5.3） |
| P6 `Página do Participante.` | +0.8 | **D3**：末行降部漫出（§5.3） |
| P6 `EXERCÍCIOS　6ページの練習` ×2 | +42.0 | 下节标题（两栏同行），假阳性 |

### §5.3 缺陷三项（D1/D2/D3，归属核心）

- **D1**：P1 框 `y=1874 bottom=2310.0`，`em Brasília. (Página 4)` 基线 2327.6，
  整行在框底外 17.6px；200dpi 裁图 `crop-p1-linex.png` 可见白底上的该行；
  core-pt 同框同文同几何。pt-de1 D1 同项复现。
- **D2**：P3 框 `y=200 bottom=525.0`，`16h30.` 基线 540.6，在框底外 15.6px；
  像素扫描：x=1700 SVG 列奶油 `#f0eee5` 止于 y=525，y=526 起纸色 `#fbfaf6`；
  裁图 `crop-p3-schedbox.png` 可见。core-pt 同。pt-de1 D2 同项复现。
- **D3**：P6 框 `y=200 bottom=840.0`，`Página do Participante.` 基线 840.8，
  PIL 墨迹底 845.8 → 框底外 **+5.8px**（core-pt 同行墨迹盒逐值相同）；
  裁图 `crop-p6-timeline.png` 可见 `g`/`p` 降部切出框边。pt-de1 D3 同项复现。

### §5.4 横向扫描（hscan.py，全版 PIL 真墨迹）——检出 D4

对 31 框 × 全部框内行核墨迹左右缘 vs 框左右缘（阈值 0.5px）：
**ja 全版仅 1 处溢出**：P1 数字框标题 `A SEMANA EM NÚMEROS　数字で見る`
墨迹右缘 1420.0 vs 框右缘 1411.5 → **RIGHT OVERFLOW +8.5px**（`hscan.log`）；
**core-pt 同扫描 0 处**。PIL 实测 + 200dpi 裁图 `crop-p1-numtitle.png`（末字 `る` 落在框外白纸上）
双重证实。**D4，归属本版。**
其余：P1 全部文本墨迹右缘 ≤1861.8（距内容边 1910 余量 ≥48.2px）；全 8 页
墨迹右缘 >1900 或左缘 <50 的行数为 0（`ink2.log` §E/§F）。

## §6 boxtitle 逐个实测

- 有边框的框标题：occlusion BOXTITLE 类 0 标记（自检阳性对照通过，§2）。
- 奶油框标题（31 框首行 + 全部框内行右缘）：`hscan.py` 全版 PIL 实测，
  仅 D4 一处溢出（§5.4）；其余框标题余量均 ≥ +21.9px（P1 各框 widest 行余量
  +21.9…+129.5px；全版最小余量见 `ink2.log` §D）。
- P1 刊头副标题 y=372（日语版标识行）墨迹右缘 1861.8，内容边内，无溢出。

## §7 印/网文字层比对 + P8 最小字号实测

- `pdftotext -layout`：印 `print.txt` 107,895 字节 / 网 `web.txt` 108,013 字节；
  **各 7,040 词，词多重集差 = 0**；各 8 页；版面 1462.5×2025pt。
  （KIT 的 6,897 词为另一计数口径；等式关系一致。）
- PyMuPDF span 实测（印 + 网一致）：**全版最小字号 10.125pt，仅在 P8**
  （828 个 P8 span，最小 10 项均为 10.125pt，如 `✓模範文はこのページの…`、
  `あてずっぽうの答え`）；高于 SOP §1.1 底线 9.75pt。
  10.125pt = SVG 13.5 单位 × 0.75，与 KIT 数字一致——**以实测为准，非配置值**。
  其余各页最小字号均 >10.125pt。

## §8 弯引号 + 字符扫描 + E 节本地化

- U+201C / U+201D：SVG 各 2（均在 `p8-avaliacao.svg`，E 节 Q139/140 两句日语句），
  text.md 各 2，印/网 PDF 文本层各 2，P8 渲染正常（`all-8.png` 可见）。
  U+2019：全版 0；U+2018：0。« / »：SVG 与 text.md 各 40（葡语引号，按习惯使用）。
- (d)：SVG 与 text.md 中「翻譯」「翻译」「中文」均为 0；简繁-only 字符 0
  （`来` 的出现全为日语：未来/来週/出来/来ます）；P8 E 节标签 4×`訳`，节标题 `E · TRADUZA`
  （目标语节名）；`?2文`/`?Write`/`( (`/`。。`/` :` 均为 0；`..`（非 `...` 者）0。
- P7 金句 8 条在 SVG 全文各出现恰好 2 次（`gates.py` 亦 PASS）；范文重数 88 词（§9）。

## §9 keycheck 150/150 + 事实核实

`keycheck-150.json`：150 题逐题手验，**150/150 正确**。
印键（`p8.py extract`）与 text.md Respostas 汇总逐项比对 150/150 一致
（初版正则在 `1 a 1.` 等处吞数，逐字复核后确认一致，见 `keycheck-compare.json`）。
逐题依据见 JSON 内 `basis` 字段；要点：Q83–87 图表数重算（15/10/5/15/ prazo）；
Q120 5 小时；Q131=A（核心 D2 修正已在位）；Q137/138 日语译文正确；
Q150=✓，范文 88 词（text.md 模型文按空格重数 = 88）；
题号 1–150 连续；每页题量 10/18/18/18/18/18/12/38。

**外部事实来源（本次独立检索，2026-11-11）：**
- 巴西杯半决赛：Atlético-MG 1–1 Grêmio（11月7日周六，Arena MRV；
  Renan Lodi 先拔头筹、Carlos Vinícius 扳平；总比分 3–1）、
  Vasco 2–1 Palmeiras（11月8日周日，São Januário；点球 5–4）、
  决赛 12月6日周日单场、马内·加林查——与刊内完全一致。
  来源：brasileirao.com.br（CBF 官网）、estacaolivremt.com.br、
  futebolinterior.com.br、sportbuzz.com.br（均为 2026-11-08/09 报道）。
- Enem：Edital nº 64/2026 §15.1「até o 10º dia útil após o 2º dia de aplicação」；
  第二天 11月15日（周日，自然科学 + 数学 90 题，13h30–18h30）；
  官方答案窗口 27–30日（20日假日计与不计之争，各来源有 27 日与 30 日两说，
  刊内印 27–30日窗口并说明分歧，正确）；个人成绩 2027年1月、Página do Participante。
  来源：cursosdoportal.com.br、blogdovestibular.com、sisu.pro.br、acheconcursos.com.br。
- 日期星期：`date -d`（America/Sao_Paulo）核对 16 个日期全部一致
  （11月1日周日、7日周六、8日周日、14日周六、15日周日、16日周一、17日周二、
  18日周三、19日周四、20日周五、21日周六、22日周日、23日周一、27日周五、
  30日周一、12月6日周日）。
- 工作日重算（16–30日）：工作日 16/17/18/19/23/24/25/26/27/30 = 10 天；
  周末 + 假日 20/21/22/28/29 = 5 天；10+5=15 天。✓

## §10 判为非缺陷的项

- desc-clear 6 处负值：PIL 真墨迹均在框底内 2.5–5.4px（§5.1），公式误报。
- BELOW-WINDOW 标题行 +32/+37/+42：下节标题，非溢出（§5.2）。
- P1 刊头副标语替换（`badge372` 日语版标识行）：标准 fan-out 家具，
  en/fr 版同式；刊内无溢出。
- P8 简析注：核心留空处由日语层填注（§4a），设计如此；键一致。
- freeze diff 新增 CJK 3,255：日语层替换中文层的预期量，无新增葡语文本。
- keydiff [137, 138]：正确日语译文（§3）。
- P1 LINEX 擦线（O1）：几何相交 ~1.4px，常读尺寸不可见，工具阈值外（§2）。
- P2 C 节说明 `数字で見るで埋めよう`（O2）：模板拼接致 `で` 重叠，语法可通，不改数字。
- P3/P4 栏位孤悬标题（O3）：核心流式排版行为，无重叠/截断。
- `«consciência»` vs `« consciência »` 空格不一致（O4）：核心带来，建议统一。
- 读者面无内部标签：可见文本 `2026-w47`/`pt-ja`/`W47`/`SOP`/`cover` 均为 0
  （`W47`/`SOP` 仅出现在 base64 图片数据内，非可见文本）；VOL 15 处均为正当引用。

## §11 未跑 / 未决

- 无。本任务要求的全部机械门均已实跑（gates、occlusion、p8 extract/compare、
  freeze baseline/diff、creambox 全版、hscan 横向、PIL 真墨迹、印/网文字层、
  P8 字号实测、弯引号扫描、keycheck 150）。
- 遗留：D1–D3 待 core-pt 修复 + 重 fan-out；D4–D5 待本版源头修复 + 重渲染；
  修复后须从头再做一轮全量复校（PROOF-NOTE O5）。
