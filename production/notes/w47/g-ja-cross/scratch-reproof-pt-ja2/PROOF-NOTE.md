# PROOF-NOTE — 2026-W47 pt-ja re-proof（第 2 轮，独立复校）

- 复校员：独立 re-proof（与 fix1 修复员不同人；与上一轮 re-proof 不同人）
- 对象：`production/2026-w47/2026-w47-pt-ja/`（盘上 fix1 版），核心对照 `production/2026-w47/core-pt/`（fix2 定稿）
- 工作区：`hidden_files/w47/scratch-reproof-pt-ja2/`（全新独占；未动任何他人 scratch）
- 结论：**(a) 无缺陷** — 整期从头全量复校，一整轮零问题。D6 已修且三重验证通过；D1–D5 存活；全部机械门自跑通过。

## 0. 开工核对（三 SHA，2026-11-11 18:0x UTC 实测，与任务给定先验值逐字节一致）

| 交付物 | SHA-256 | 字节 | 先验值 |
|---|---|---|---|
| 印 PDF `A-Lucerna-VOL4.pdf` | `568eb36b19a0d285dfbb9058933659e3dd97afae0d5de535a5b47bb7906b6ea5` | 24,991,052 | 一致 |
| 网 PDF `A-Lucerna-VOL4-web.pdf` | `7079b9af534836635228e9d5982210dacbecc2257438c9d1d98afbf7761c5444` | 1,680,802 | 一致 |
| 文 `2026-w47-pt-ja.text.md` | `90dcdcca7821049a9af8735653d7059e4a111eeaae6dfebf1ea1467941ec9830` | 37,915 | 一致 |

- 开工探针：`echo test | git hash-object -w --stdin` 成功（`9daeafb9…`）+ scratch 内真实写文件成功后才动手。
- 注意：任务所指 `hidden_files/w47/briefs/brief-coordinator.md` 与上一轮目录 `scratch-reproof-pt-ja1/` 在本克隆中**不存在**（全仓搜过，无此二路径）。因此上一轮的逐缺陷量测底数无法从前人笔记复读（见 §5 末尾说明）；本轮全部数字均为自测，规则依据为任务书 + 仓根 SOP.md（§1.1、§8.4）。
- p1 SVG 现盘哈希 `fc51c47e6a0bc0d26b05892896369c50aedfe1aa05d972a25cbc01bae8e2474f`，与任务所称 fix1 后值一致。另：该版目录未入 git（`??`），无 fix1 前 commit，故任务所称「印 PDF +3 B」「仅 p1 SVG 变化」两项**无法从版本历史复核**，仅能核对修后状态（本轮已核对）；见 §5。

## 1. D6 复测（唯一缺陷，逐项独立重测）

声称：P1 顶栏标语 `ブラジルが読むポルトガル語` → `ブラジル人が読むポルトガル語`（各加一字「人」）。

- 源码行：`tables_ja.py:202`（`"读巴西人正在读的葡萄牙语": "ブラジル人が読むポルトガル語"`，SEG 表）与 `content12.py:15`（`p.text(975, 92, "TODA SEMANA EM PORTUGUÊS　毎週　ブラジル人が読むポルトガル語", 17, "sans", False, GREY, anchor="middle", spacing=1.7)`）。两处均为新串。
- 全版旧串 `ブラジルが読む`：.py/.svg/.md/.txt 全扫 **0 处**；新串 `ブラジル人が読む`：`content12.py` 1 处 + `tables_ja.py` 1 处 + `svg/p1-capa.svg` 1 处 = 源码 2 处、渲染 1 处，与声称一致。text.md 0 处（预期：标语行不在 text.md 导出中）。
- SVG 量测（`d6-measure.log`，svglib 同款 PIL 字体）：标语元 x=663.9（middle 锚，975 − advance/2），无字距 advance 右缘 **1216.4**，与声称 `1208.7→1216.4` 的修后值逐值一致。注：字距 spacing=1.7 使真实 advance 为 622.2，SVG x=663.9 已含字距；朴素 text_w（552.5）不含字距，故墨迹缘须以渲染像素为准（下一条）。
- 交付印 PDF 渲染像素量测（`render-print/p-1.png`，pdftoppm 150 dpi，3047×4219，scale 1.5626；`d6-pixel-measure.log`）：顶栏 y=92 带暗像素簇——标语墨迹 **664.3–1285.7**（SVG 单位），中心 **975.0**（恰为版心）；日期行墨迹左缘 **1460.4**；墨迹间隙 **174.7px**。声称值 1285 / 1461 / 176px，三项均在 ±1.3px 内吻合（阈值 luminance<180 的取整差异）。
- 裁图目视：`render-print/p1-topstrip.png`（交付 PDF 渲染）——标语居中、无接触、无裁切，「ブラジル人が読むポルトガル語」清晰可读；左 `VOL. 4 QUARTA EDIÇÃO`、右日期行俱全。
- D6 结论：**已修**。语言裁定不重开（任务书已裁定：日语无 che/que 强制结构，中文源文「巴西人」，加「人」正确）。

## 2. D1–D5 存活复测

- D1（17 日 7h，非 7h15）：P1 SVG、P3 SVG、text.md（L44、L167）三处均为 `Ter 17 — Singapura × Brasil, às 7h, amistoso da Seleção`；全版 `7h15` **0 处**、`Japão` 0 处（11 月 14 日日本场不在本期 16–22 日历内，KIT §2 所述 14 日 7h15 为源事实背景）。**存活**。
- D2：Q131 键 = A（`No sábado, 21, Rafael assiste... A. a Palmeiras × Flamengo`），与 P8 阅读文逐字相符（`No sábado, 21, ele assiste a Palmeiras × Flamengo na televisão.`）。**存活**。
- D3：上一轮量测底数不在盘上（见 §5），本轮以全量复校覆盖：P1–P8 目视 + occlusion 0 + 150 题手验均零问题，未见残留缺陷。
- D4（单字「数字」）：两处「数字」表头自测——P1 `A SEMANA EM NÚMEROS　数字`（y=823.18，墨迹 1006.0–1351.0，数字框 rect x=989 y=786.18 w=422.5 h=434，墨迹右缘距框右缘 **60.5px**，与声称 +60.5 逐值重合）；P6 `O FIM DE NOVEMBRO EM NÚMEROS　11月末の数字 (Edital nº 64/2026 do Inep)`（墨迹 88.0–1066.0，距页右缘 796px，框内无接触）。P2「1ページと2ページの数字で埋めよう。」指示行墨迹 989.0–1338.0，栏内干净。occlusion 0、P1/P6 渲染目视干净。**存活**。唯声称的第二个值 +63.5 未能从现盘数据复现出同一量测口径（见 §5）。
- D5（「土曜日16:30」三方一致）：SVG P2 `土曜日16:30、パルメイラス`、text.md L118 `土曜日16:30`、核心 `周六 16:30`——三方一致，且与葡文 `SÁB 21 — Palmeiras × Flamengo, às 16h30` 同义。**存活**。
- Q65：键 B（`No domingo 15, a prova tem... B. Natureza e Matemática, das 13h30 às 18h30`），与 P5 正文逐字相符（Enem 第二天为 Natureza e Matemática；redação 是第一天）。**已修存活**。

## 3. 全量复校（SOP §8.4：修后整期从头再校）

### 3.1 机械门（全部自跑，见 GATE-LOG.md）

- run.py：rc=0，TOTAL **150**（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38；范文 88 词），FLOW OVERFLOW / HEAD TOO WIDE 0 次；P8 答案流末 col 3 y=2504（底 2560）。
- SVG 重建：scratch 副本内重跑，8/8 与成品逐字节相同（`svg-rebuild-compare.log`）。
- gates.py：**16/16 PASS**，FAILURES: none（P1 头条 41 字符 ≤56；P7 末引 baseline 2351.17 < 2404 预告框顶）。
- freeze baseline：8/8 OK；freeze diff：新增 CJK 3,246（日语讲解层替换中文讲解层，预期；与 KIT 旧值 3,255 之差源于 core fix2 refanout，非缺陷）。非 CJK 差分核查：葡文目标语文本无一字改动，差异仅为包边/页脚格式（`1／8`→`1（8）`）、标点转换（，。→ 、。）、家具翻译（P1 kicker 葡文标语→日文版面说明行；`A Lucerna VOL.4` 后英文副标移除）及换行边界伪影（如 `A SEMANA DO FUTEBOL1` 实为 `A SEMANA DO FUTEBOL　サッカーの1週間` 去 CJK 后的残字，已逐项核实）。
- occlusion_audit.py：**0 flags**（自检 6 类全触发、干净对照静默）；core-pt 同跑亦 0 flags。KIT §6 所记 1 处 P1 LINEX 擦痕（0.2px）属 refanout 前旧版，现版双双为 0。
- p8 extract：150/150（版与核心皆然）；p8 compare：**CLEAN**，missing=[]、extra=0、uncertain=[]、keydiff=**[137, 138]**（仅两道翻译题，见 §3.3）。
- 印/网文字层：pdftotext 各 107,800 字节，`cmp` **逐字节相同**；8 页，1462.5×2025pt；网 PDF 1,680,802 B < 7 MB。
- P8 最小字号：**10.125pt**（605 spans，答案区），≥ SOP §1.1 底线 9.75pt；其余各页最小 11.625–12.75pt。

### 3.2 全文独立复校（交付印 PDF 重渲染 8 版逐版目视 + text.md 534 行逐行读）

- 无溢出、重叠、压页脚、压框线、豆腐块；5 图俱全且出处齐全（P1 卡波耶拉 Rugendas 1835、P3 Zumbi Parreiras 1927、P5 Gary Todd CC0、P7 《Os Lusíadas》1572、P8 Mané Garrincha Luis Dantas；P4 无图，与核心一致）。图片与核心逐字节相同（capoeira cmp 通过，余 4 图同名同在）。
- 日期/星期日历核验（`date -d`）：11 月 16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、27 日周五（Black Friday）、12 月 1 日周二、12 月 6 日周日（决赛）——与文中全部星期表述一致。11 月 7 日周六、8 日周日（半决赛次回合）亦一致。
- 图表题独立验算：P6 11 月 16–30 日共 15 天；工作日 16/17/18/19/23/24/25/26/27/30 = 10 天，休息日 20（假日）/21/22/28/29 = 5 天，10+5=15 ✓；第 10 个工作日 27–30 日窗口 ✓（假日计入则 27 日，不计则 30 日）；Enem 两天：8 日 13h30–19h、15 日 13h30–18h30、第二天 90 题 5 小时，与正文一致。
- 金句 8 条：逐字取自本期正文，页码标注 (Página 1/1/3/3/4/5/6/2) 均与原文所在版相符。
- VOL：VOL.4 ×9、VOL.5 ×3、VOL.3 ×2（两处皆在 P7 读者来信披露中引前号，合法），与核心逐项相同。徽章逐页计数与核心完全相同（P1 A2 10/B1 3/B2 1；P2 A2 14/B1 1；P3 A2 10/B1 8；P4 B1 15；P5 B1 15/B2 3；P6 B2 18；P7 各 4；P8 A2 8/B1 24/B2 3）。
- 讲解层确为日语；练习小节头冻结为日语，题型标签为日文（補おう/文を作ろう/ペアを作ろう/正しいか間違いか/訳/作文）；简繁中文专属字 **0**（`会` 1 处为「試験会場」，合法日文）；U+2019 0、U+0027 0。
- text.md 与 SVG 的一处表面差异已核实为跨版既定模式：text.md L11 保留核心葡文标语 `O JORNAL SEMANAL PARA APRENDER — …`，而 SVG P1 y=372 为日文版面说明行；pt-en/pt-fr 的 text.md 同样保留葡文标语行、SVG 同样为读者语说明行——非本版独有，不列缺陷。
- P7 披露：无来信（F-MAIL 规则：只认用户直接发来的投稿），编辑部作例 + 双语披露，承诺延至 VOL.5；作例标签以「。」结尾。期货预告 VOL.5（11 月 27 日 Black Friday + 公式解答 + 12 月 6 日决赛）与正文承诺一致。
- ABSTRACT.txt：日文单行 123 字，内容真实（11 月 20 日祝日、3 连休、Enem 公式解答等待、12 月 6 日决赛、150 问 A2–B2、解答在 8 版）。
- §1.1 抽查：纸色 `#fbfaf6`、刊头 196px、头条 42pt 均与 KIT 一致；P4 `B AS PALAVRAS` 表头栏底孤行、P3/P5 词表引言栏顶为核心排版行为，与核心相同，不列缺陷。

### 3.3 150 题逐题手验（key 与题干/原文配对实算，非仅三源一致）

- 题号连续 1–150，分版 10/18/18/18/18/18/12/38，级别 A2 48 / B1 71 / B2 31（重跑 registry 实测）。
- 动词题全验：现在形（cai/dura/descansamos/abrem/aproveita）、过去形（morreu/nasceu/defendeu/formaram/empatou/venceu/abriu/garantiu/foram）、未来形（sairá/publicarão/decidirá/chegará）、未来接续法（sair/for/tiver）及时态选择（Q93 serão、Q108 saíram、Q112 sair）皆与语境一致。
- 易混点：Q73 `espera`——词库 {gabarito, oficial, extraoficial, espera, nota, pesar} 中唯 `espera` 可接 `começa a ___`，与 Q70 `começa a espera pelo gabarito` 分工不同、无冲突（en Q73 三源同错的前车之鉴已针对性复核）；Q36 `escravizados` 复数配合；Q58 `16h30 é mais cedo`；Q148 `na internet`；Q125 回合 36 在周六 21 日。
- P8 阅读（Rafael in Salvador）：Q129–132 键 B/B/A/B 逐句对原文核实无误；Q131 = A。
- 翻译题：137「11月20日金曜日は全国の祝日です。」、138「パルメイラスはPK戦で5–4で勝ちました。」、139「O gabarito oficial sai até o fim de novembro.」、140「Anote as suas respostas e confira quando sair o gabarito oficial.」——四条译文皆正确，与核心 137/138 的键差仅为读者语转写。
- 匹配题：25–28、52–55、141–144 逐对核实，全对。范文 88 词（程序计数 88）。

### 3.4 网页版目视

- 网 PDF P1/P8 重渲染（`render-web/wp1-1.png`、`wp8-8.png`）：与印版版式一致，无豆腐块、无缺字，标语「人」清晰。

## 4. 缺陷清单

**(a) 无缺陷。** 本轮全量复校零问题。

## 5. 观察项（不计缺陷）

- O1：KIT §6 门记录仍引 refanout 前旧版量测（印 PDF 24,992,044 B / sha `04f284ed…`、网 PDF 1,644,666 B、occlusion 1 flag、VOL.3 ×1、CJK 新增 3,255），与现盘 fix1 版（24,991,052 B / `568eb36b…`、1,680,802 B、occlusion 0、VOL.3 ×2、CJK 新增 3,246）不符。属 KIT 未随 refanout+fix1 更新，版面本身无问题。
- O2：任务所称「印 PDF +3 B」「仅 p1 SVG 变化」无法从本克隆复核——该版目录未入 git，无 fix1 前 commit；p1 SVG 现盘哈希与任务所称修后值一致，修后状态已全项核实。
- O3：上一轮目录 `scratch-reproof-pt-ja1/` 与 `brief-coordinator.md` 不在本克隆中，故 D1–D3 的声称量测值（+15.4/+10.4/+8.2）及 D4 的第二个值（+63.5）无法按原口径复现。已改以自测覆盖其实质：D1 的 7h 事实三处一致、D4 的 P1 +60.5 逐值重合、P6 表头 796px 余量、occlusion 0、8 版目视、150 题手验——均零问题。建议协调员确认上一轮 scratch 的存放位置，以免后轮复核再度缺底数。

## 6. 生产零写入核对

- 收工快照 `snapshot-end.sha256` 与开工 `snapshot-start.sha256` 比对：`production/2026-w47/2026-w47-pt-ja/` + `production/2026-w47/core-pt/` 共 88 文件 SHA 全部相同，**零写入**。全部重建/渲染均在 scratch 副本内完成，未覆盖生产网 PDF（网 PDF 仅 pdftotext/pdftoppm 只读）。

## 附：证据文件（均在 scratch-reproof-pt-ja2/）

- `snapshot-start.sha256` / `snapshot-end.sha256`、`run-rebuild.log`、`svg-rebuild-compare.log`、`gates.log`、`freeze/baseline.log` + `baseline.json`、`freeze/diff.log` + `diff.json`、`freeze/non-cjk-diff.log`、`occlusion.log` + `occlusion.json`、`occlusion-core.log` + `occlusion-core.json`、`p8extract-ed.log/.json`、`p8extract-core.log/.json`、`p8compare.log/.json`、`print.txt` / `web.txt`（107,800 B，逐字节同）、`p8-fontsize.log`、`d6-measure.log`、`d6-pixel-measure.log`、`d1-d5-spot.log`、`d4-measure.log`、`misc-checks.log`、`render-print/p-1.png`～`p-8.png`、`render-print/p1-topstrip.png`、`render-web/wp1-1.png`、`render-web/wp8-8.png`、`GATE-LOG.md`。
