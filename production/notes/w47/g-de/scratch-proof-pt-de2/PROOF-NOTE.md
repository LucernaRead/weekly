# PROOF-NOTE — 2026-W47 pt-de（葡萄牙语目标 · 德语读者）proof2（重建版复校）

独立复校员：proof2（完整独立复校），2026-11-11。
Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-de2/`
（全部工作文件见该目录；生产目录未写任何文件，未 commit，未 push。）
复校对象：core-pt fix2（`d2b0e182`）重建版，见 `FANOUT-REPORT-pt.md` §1/§2/§6 与本版 `WEEKLY-KIT.md` 附录
`Re-fanout (2026-11-11, core-pt fix2)`。

## §0 版身份核对（磁盘为准）

| 文件 | 磁盘字节数 | 磁盘 SHA-256 | 与任务一致 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | 12,938,914 | `77243c72c38a14232ea443f03856ccf0a88f3d4b2c0c89e75aa87cf658e6284a` | ✓ |
| `A-Lucerna-VOL4-web.pdf`（网） | 1,147,629 | `56eb92d0251d691956e8dac6cccab0e9bf2a4bbadd9dc662c55632eb1b13b84b` | ✓ |
| `2026-w47-pt-de.text.md` | 37,907 | `519ab0dedbae110dba11eeffe3cd8517db41141020061e9a66c5dd252d784305` | ✓ |

三份 SHA 与字节数与任务完全一致（开工与收工各验一次，收工时 SHA 不变）。
核心 HEAD：`d2b0e182`（fix2）。解释器全程 `tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0）。
`git status --porcelain`：版目录仍为 untracked（`?? production/2026-w47/2026-w47-pt-de/`），无修改。

## 结论：(b) 有缺陷，不能定稿

发现 **1 项缺陷（D4）**，四法一致实测证实、交付 PDF 上肉眼可见。
其余全部机械门通过，proof1 的三项核心缺陷 D1–D3 已修复并复测通过，
D5 gloss、150 题、KEEP 盘点、印/网文字层全部通过。
按 SOP §8 proofread-until-zero，本版当前状态不能定稿。

## 缺陷清单

### D4（中低）P1 框标题横向溢出：NESTA EDIÇÃO 框标题末字漫出奶油框右缘

- **页码 / 定位**：P1 右栏奶油框 `x=1439.5, y=1238.35, w=422.5, 右缘=1862.0`；
  框标题 `NESTA EDIÇÃO　In dieser Ausgabe`（Noto Sans CJK SC 24 bold，基线 y=1278.35），
  末字 `Ausgabe` 的 `e` 伸出框右缘，落在白底上。
- **归属**：本版家具（德语副标题），**非核心**。字符串来源：
  `content12.py:89`（`p.text(gx + 22, sy + 40, "NESTA EDIÇÃO　In dieser Ausgabe", 24, "sans", True, OLIVE)`），
  德语部分译自 `tables_de.py:139`（`"本期目录": "In dieser Ausgabe"`）。
  核心 pt 的同框标题为中文读者语，不受影响。
- **是否回归**：不是重建回归。第一轮备份 SVG（`backup-old/2026-w47-pt-de/svg/p1-capa.svg`）
  中该标题元素与本版逐字相同（同 x=1461.5、同字串、同字体/字号/粗体）。
  是 proof1 遗漏的既有缺陷——proof1 的 (a) 项“未复现、余量 +16.5px”所依据的测量有误
  （见下“测量分歧”）。
- **实测证据（四法一致，均指同一标题；另见 GATE-LOG §4）**：
  1. `boxtitle_core.py`（PIL advance，4× 渲染）：`title_w=402.1, right=1863.6, clear=-1.6  <<<< OVERFLOW`
     （`boxtitle.log:4`）。
  2. 本人独立 PIL 真墨水实测（`boxtitle_ink.py`，svglib 字体、anchor 感知）：
     墨迹右缘 1863.5，clear **−1.5**（`boxtitle-ink.log`）。
  3. 交付印 PDF 像素实测（PyMuPDF 渲染，96dpi 与 200dpi 同法）：
     墨迹右缘 1864.0 / 1864.8，超出框缘 **+2.0 / +2.8**（`pixel_compare.py`、`pixel_boxtitle_pdf.py`）。
  4. 交付印 PDF 与网 PDF 的文字层 span（fitz）：`'In dieser Ausgabe'` bbox x1 = **1866.1**（单位），
     框缘 1862.0，advance 口径超出 +4.1；网 PDF 同值（`GATE-LOG §4`）。
  5. 目视：300dpi 原生裁图 `visual/crop-p1-nesta-pdf300.png`——末字 `e` 完整可见、
     横跨奶油框右缘，右端约 3 单位落在白底上；同法裁图 `visual/crop-p1-nesta-card.png`
     （Cairo 直渲卡片）则显示该标题收在框内（余量 +1），即**只有交付的 PDF 溢出，卡片不溢出**——
     渲染器间约 5 单位的宽度差（见“测量分歧”）。
- **测量分歧（为什么 proof1 称 +16.5）**：同一标题四种口径——proof1 `boxtitle2-proof1.log`
  墨迹右缘 1845.5（+16.5），比其余全部方法窄约 15–18 单位：advance −1.6、PIL 真墨 −1.5、
  卡片像素 +1、PDF 像素 −2.8。proof1 的方法（脚本未留存，仅有日志）对粗体标题系统性偏窄
  （其余粗体标题亦同：EM POUCAS +18.5 vs 实测 +0.5…+3；A SEMANA EM NÚMEROS +18.5 vs +1.5…+3；
  而非粗体 HINWEIS 行与 Newsreader 标题则与各法一致）。以交付 PDF 的像素为准，标题确实溢出。
- **严重度**：溢出量约 2–3 SVG 单位（≈0.75pt ≈ 0.26mm，一字之末笔），小但真实、
  放大可见，且正是必查项 (a) 框标题横向溢出的类别。occlusion 审计的 BOXTITLE 容差为 0.5px
  （`r > rr + 0.5`），本项超其 3–5 倍；ru O3 裁定（0.5px 零余量为非缺陷）的边际带亦未覆盖。
  该审计对无描边奶油框根本不检查 BOXTITLE（见 GATE-LOG §2），故其 0 标记不能作为反证。
- **修复建议**：缩短德语副标题（如 tables_de.py:139 改短写法，或 content12.py:89 字号 24→23、
  或标题 x 左移 ≥4 单位），重渲染本版印/网 PDF，复跑 boxtitle + PDF 像素实测复验。
  同列另一标题 EM POUCAS PALAVRAS 亦在边缘（见“边缘记录”），修时一并复测。

## 边缘记录（不计缺陷）

- **E1** P1 `EM POUCAS PALAVRAS　IN KÜRZE`：PIL 真墨 +0.5、advance +0.9、印/网 PDF 像素 1862.0–1862.4、
  fitz advance 1864.0——墨迹基本恰贴框缘（0–0.4 单位），300dpi 裁图 `visual/crop-p1-poucas-pdf300.png`
  显示末字 `E` 完整、右缘贴框边。按 ru O3 的 0.5px 边际带裁定为边缘通过，不计缺陷；修 D4 时一并复测。
- **E2** P1 `A SEMANA EM NÚMEROS　In Zahlen`：PIL 真墨 +1.5、PDF 像素 +2.9/+3——紧但在框内。

## 必查项裁决

- **run.py / gates.py**：run.py RC=0，TOTAL **150**（A2 48 / B1 71 / B2 31；
  每页 10/18/18/18/18/18/12/38）；edition `gates.py` **16/16 PASS**，`FAILURES: none`。
  重渲复现：scratch 副本 run.py 重建的 8 张 SVG 与交付 SVG 逐字节一致，
  重渲印 PDF SHA 与交付印 PDF **完全一致**（`77243c72…`）。
- **freeze**：核心 baseline **8/8**（`--build` 真核心 core-pt；核心哈希 bd87a867…a7b7a661；
  核心完整性重哈希无改动）；版 baseline **8/8**（f988db96…a4447964，与 refanout 一致）；
  freeze diff 新增 CJK 共 9 个，全部为 U+3000 家具分隔符。
- **occlusion**：真实审计命令 0 flags（`occlusion.json`）。但注意：其 BOXTITLE 检查只看有描边
  或 fill `#2c2822` 的矩形，无描边的奶油框（`fill="#f0eee5"`，无 stroke 属性）根本不在检查之列——
  D4 因此未被审计发现（GATE-LOG §2 有代码行号）。
- **p8**：extract **150/150**；compare **CLEAN**，core 150 / edition 150，
  keydiff **[137, 138]**（预期；两句德语译文答案逐题验过，正确——见下）。
- **keycheck**：**149/150**，仅 #150 例外（开放写作题，提取为 `✓`，预期内）。
- **creambox / boxtitle**：正典 creambox 全版扫描 31 框，OWN 真墨余量全部为正（最小 +2.1，
  P2 `Palmeiras–Flamengo-Duell`）；D1（P1 闪讯框末行墨底 2332.6，框底 2348.0，余量 **+15.4**）、
  D2（P3 日程框 `16h30.` 墨底 540.9，框底 551.0，余量 **+10.1**）、D3（P6 时间线框
  `Página do Participante.` 墨底 846.0，框底 854.0，余量 **+8.0**）——proof1 三项核心缺陷全部修复，
  均经 PIL 真墨复测。5 处负 clearance 为已知的下块标题假阳性（+32…+42，owner-rect=NONE）。
  boxtitle advance 报告 1 处 OVERFLOW，即 D4。
- **D5 gloss**：P4 gloss 框实测 4 行，末行右余 **+101.5**、底余 **+42.7**，无溢出；
  渲染 `o título Titel`（`gloss.log`；与 FANOUT-REPORT §3 宣称值逐字一致）。
  `tables_de.py:40` `"冠军头衔": "Titel"`；旧映射 `tables_de.py:39` `"冠军": "Meister"` 未动。
- **印/网文字层**：`pdftotext -layout` 逐字节一致（111,362 B）；fitz 逐页比对 8/8 页一致；
  check_final 词数印 8,436 = 网 8,436，多重集差 0；斜体 span 印 1 = 网 1（`« consciência »`）。
  网 PDF 只在 scratch 副本重渲比对：SHA 浮动（重渲 fb94a0e9… vs 交付 56eb92d0…，为预期现象），
  文字层逐页一致、8,436 词；交付网 PDF 未被触碰（收工 SHA 仍为 56eb92d0…）。
- **P8 最小字号**：9.75pt（n=380），低于 9.75pt 者 0——正好 SOP §1.1 底线，不低于。
- **孤儿标点**：SVG 文本行首孤儿标点扫 **0**；sweep：box-vs-hline 0、bridge widows 0、
  bridge orphans 2（见下“旧修复复验”）。
- **8 页目视**：印 PDF 8 页逐页看图（`visual/p-1.png`…`p-8.png`）。D1/D2/D3 修复处目视确认在框内；
  P4 gloss 框 `o título Titel` 在框内；其余无可见缺陷（P3/P5 `Kasten.` 孤字与 O4 同，见下）。
- **D5 字体**：只记录数量，不判 (b)：P5（印 PDF 第 5 页）共 **4** 个内嵌字体子集
  （`NGCYSB+NotoSansCJKsc-Regular`、`UIKPPO+Newsreader16pt-Regular`、
  `WRUMGD+Newsreader16pt-Regular`、`YCHKXS+NotoSansCJKsc-Bold`；即 3 个字体族）。

## 150 题逐题手验（Q73/en-ko 教训：三源一致不够，逐题看题干与键的适配）

- text.md 535 行通读；keycheck 机械比对 149/150（仅 #150）；P8 目视核对答案键。
- **Q73**（教训所指类）：题干 `Depois da prova, começa a ___.`，键 `espera`——
  P5 正文原句即 `Depois da prova, começa a espera pelo gabarito.`，题干与键逐字适配，正确。
- **Q65**：`No domingo 15, a prova tem... B. Natureza e Matemática, das 13h30 às 18h30`——与 P5 正文一致。
- **Q83–87** 工作日重算：11 月 16–30 日共 15 天；工作日 10 天（16–19、23–27、30，扣 20 日假期）；
  周末+假期 5 天（21、22、28、29 + 20 日）；10+5=15。Q83 B（15 天）、Q84 A（10）、Q85 B（5）、Q86 B（15）、Q87 B（期限）全对。
- **Q120**：13h30–18h30 = 5 小时，键 B 正确。**Q125**：36ª rodada Palmeiras × Flamengo，周六 21 日 16h30，
  Nubank Parque——proof1 已用 CBF 赛程外部核实（brasileirao.com.br、colunadofla、portaldopalestra），
  本次未重复外部核查，结论沿用 proof1（见 GATE-LOG §8 备注）。
- **Q137/138**（p8 keydiff 两题）：137 `Freitag, 20. November, ist ein nationaler Feiertag.`、
  138 `Palmeiras gewann das Elfmeterschießen mit 5:4.`——德语正确。
- **Q139/140** 德→葡翻译、`Q141–144` 配对、`Q52–55` 配对、`Q25–28` 配对、`Q56–59` 比较级
  （mais/mais/mais/menos）、`Q76–79` 将来时（sairá/publicarão/decidirá/chegará）、
  `Q101–112` 语法（含 Q108 `saíram`、Q109 `sair`、Q110 `for`、Q111 `tiver`）、
  `Q113–120`、`Q121–132`（Rafael 阅读）、`Q133–136` 造句、`Q145–149` 对话（Mané/ sexto/quinto/na/obrigado）
  逐题验过，全部正确。范文重数 **88 词**（实测 88）。
- 题号 1–150 连续；每页题量 10/18/18/18/18/18/12/38。

## proof1 旧修复逐项复验（重建版是否存活）

| proof1 项 | 本版复验 |
|---|---|
| D1 P1 闪讯框 +17.6 漫出（核心 fix1：框 436→474） | 存活：框高 474（content12.py:138 `p.rect(bx, 1874, CW, 474, …)`），末行墨底余量 +15.4，目视在框内 ✓ |
| D2 P3 日程框 +15.6 漫出（核心 fix1：+26） | 存活：content34.py:40 `+ 58`（原 +32），末行墨底余量 +10.1，目视在框内 ✓ |
| D3 P6 时间线框降部 +4.8 漫出（核心 fix1：框 640→654） | 存活：content56.py:132 `p.rect(bx, 200, CW, 654, …)`，末行墨底余量 +8.0，目视在框内 ✓ |
| (a) P1 标题横向溢出“未复现”（+16.5px） | **不成立**：见 D4。proof1 测量偏窄约 18 单位；四法一致证实溢出约 2–3 单位 |
| (b) P3/P5 降部漫出“未复现”（6 行负 desc-clear 为误报） | 存活：本版 creambox.log 同 6 行负 desc-clear（−0.3…−1.1，行文与 proof1 相同）；
  creambox-diag 真墨复测 6 行均无降部字母，墨迹底 ≈ 基线 +0.2–0.5，墨余 +4.8–5.4；全版 31 框 OWN 墨余最小 +2.1 ✓ |
| (c) P7 toolbox 通过 | 存活：P7 三框 inside（基线）余量 ERROS +29.6、词框 +5.1、CARTAS +10.9；
  真墨余量 +24.6 / +4.8 / +5.9（creambox-diag.log），最小 +4.8 ✓ |
| (d) E 节 type 标签已本地化 | 存活：P8 E 节 4 题标签均为德语 `Übersetzung`；text.md CJK 扫描 0（除 U+3000 分隔符与 P1 `<title>` 元数据外）✓ |
| O1 `«consciência»` 引号内空格不一致 | 仍在：text.md `«consciência»` ×1 / `« consciência »` ×1；SVG  spaced ×2。核心继承，观察，非缺陷 |
| O2 家具字体 Noto Sans CJK SC（SOP §1.1 规定拉丁家具用 Newsreader） | 仍在：系统约定，核心同款，非缺陷 |
| O3 两处德语 gloss 行 advance 超名义边 1862 约 3–4px | 仍在：P2 日程标题 advance 1865.8（渲染墨迹 1860）、P8 注 advance 1865.7（墨迹 1864）；距页边 ≥84px，gates 框内，非缺陷 |
| O4 P3/P5 `Kasten.` 孤字、P4 `B AS PALAVRAS` 栏目标题落栏底 | 仍在：与第一轮备份坐标逐字节相同（P3/P5：行 1 x=88 y=2564.45，`Kasten.` x=538.5 y=1696.5）；核心流式排版行为，KIT 已注明，接受。sweep 的 2 个 bridge orphans 即此二处，widows 0 |
| O5 P1 `EM POUCAS PALAVRAS IN KÜRZE` 贴框边但在框内 | 改判为边缘记录 E1：实测墨迹恰贴框缘（0–0.4 单位），按 ru O3 边际带通过，不计缺陷 |

## Hand-patch 盘点复验（KIT 附录称 de 24 KEEP、0 REVERT、0 丢失）

- `de-classify.json`：24 KEEP（bslib4 9、content12 11、content34 2、content56 1、content8 1），
  0 REVERT，0 MERGE/INSERT/DELETE，总计 24。
- 抽查 5 项（源文件行号为准，均存活）：
  - content12.py:138 `p.rect(bx, 1874, CW, 474, fill=BOX)`（备份为 436）；
  - content34.py:134 gloss `o título Titel`（备份为 `Meister`）；
  - content34.py:40 日程框 `+ 58`（备份 `+ 32`）；
  - content56.py:132 `p.rect(bx, 200, CW, 654, …)`（备份 640）；
  - content8.py:110 `f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False, max_w=395)`（备份无 max_w）。
- fix1 标记计数：本版 content12/content34/content56/content8/bslib4 各含 fix1 标记，备份中均为 0。
- `tables_de.py:39` `"冠军": "Meister"` 未动；`:40` `"冠军头衔": "Titel"`、`:41` `"墨底": "Tintenunterkante"` 在位。
- 未发现丢失的手工修复。

## 未决事项（沿用 proof1，不新立）

- O1–O5 见上表。D4 修复后，P1 两标题（NESTA、EM POUCAS）须按本 NOTE 的像素法复测，
  不可用 proof1 的 boxtitle2 口径（该口径对粗体标题偏窄约 18 单位）。
- KIT 附录称 text.md “535 lines”；实测按行迭代为 **534** 行（refanout `de-gates.json` 亦为 534）——
  计数口径差，非内容缺陷。

## 建议后续

1. 修 D4：缩短 `tables_de.py:139` 的 `In dieser Ausgabe`（或 content12.py:89 降字号/左移标题），
   重渲染本版印/网 PDF；复测以交付 PDF 像素为准（本 NOTE 的 pixel_compare 口径），
   同时复测 EM POUCAS 标题。
2. 修后复校只需按同一规程重跑（重点为 P1 两标题 + 全部门禁），其余项本次已全部通过。
3. 工具缺口：occlusion 审计的 BOXTITLE 检查不覆盖无描边奶油框（D4 因此漏网）；
   建议工具侧补上 `#f0eee5` 框的标题检查（属工具改进，不在本版定稿条件内）。
