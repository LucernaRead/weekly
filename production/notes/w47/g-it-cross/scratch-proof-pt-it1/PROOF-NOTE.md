# PROOF-NOTE — 2026-W47 pt-it (Portuguese target, Italian explanations) — proof1

- Proofreader: independent proof1 (subagent proof-pt-it1)
- Date: 2026-11-11 (UTC; 05:51 EST task start)
- Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-it1/`
- Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-pt-it/` (sources untouched, no commit, no push)

## §0 身份核对（磁盘为准）

| 文件 | 磁盘 SHA-256 | 字节 | 与任务一致 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | `ea4e4fd80e9aa3f9d9fa305a985f9e234abc4858b6f10e4d4b2ab416e34156aa` | 12,930,920 | ✓ |
| `A-Lucerna-VOL4-web.pdf`（网） | `4c0d5069ba440d21f7601bb88ba37ec14a77f30c51ab8a9202fe7bb2a31b3729` | 1,100,022 | ✓ |
| `2026-w47-pt-it.text.md` | `178b5bb2dff8452c72959b3fda5cc9982c4ea2c2a3618361708928ee77cd9495` | 37,404 | ✓ |
| 正典 creambox.py | md5 `ee7a55d8b2057cf4ad42a97bb1197383` | — | ✓ |

三文件 SHA 与任务消息完全一致，字节数如上。探针通过（`git hash-object -w` 返回 `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；scratch 可写，`probe.txt` 已留）。复校结束时三文件 SHA 复验未变。

## 结论：(b) 有缺陷，不能定稿

**缺陷 5 项：D1–D5。** 其中 D1–D3 为核心层（core-pt）原样携带的几何缺陷，本版与核心逐像素一致；D4–D5 为本版意大利语层引入的框标题右溢。其余全部复校项通过（见 GATE-LOG）。

- 150 题答案键逐题手验：150/150 PASS，三源一致（P8 印刷键 = text.md 行内答案 = text.md Respostas 汇总）。
- 全文通读（印 PDF 8 页 + text.md 534 行）：除 D1–D5 外无文字、事实、日期、编号、级别问题。
- 机械门：gates 16/16、occlusion 0 flags（KIT 称 1 flag，见 GATE-LOG §0，已裁决为非缺陷）、creambox 全版扫描（见 D1–D5）、p8 extract 150/150、p8 compare CLEAN（keydiff [137, 138] 已逐个裁决正确）、freeze baseline 8/8、freeze diff（新增 CJK 仅 9 个 U+3000）、印/网文字层词集差 0、P8 最小字号实测 9.75pt（= SOP §1.1 下限）、弯引号全版扫描通过。

## 缺陷清单

### D1 — P1「EM POUCAS PALAVRAS」框内段落第三行整行落在奶油框外
- 页码/定位：P1 右栏，奶油框 `x[1440,1862] y[1874,2310]`；行「em Brasília. (Página 4)」基线 y=2327.6，墨迹盒 `[1461.5, 2313.1, 1665.5, 2332.6]`。
- 实测证据：真墨迹（审计工具自带 `ink_box`，Pillow 13）墨顶比框底低 +3.1px、墨底 +22.6px——整行完全在框外；像素裁图 `p1-d1-crop.png`：该行落在 quiz 分隔绿线之下的白纸上，前两行在奶油底上，段落中部断底色，肉眼可见。creambox：该框 inside-only 末行 2300.4（余量 +9.6），BELOW-WINDOW +17.6。
- 归属：**核心**。core-pt 同页同框同基线逐一一致（creambox-core-p136.log：`box y=1874 bottom=2310.0`、BELOW-WINDOW +17.6 同文同值）。本版未改动核心几何。
- 修复建议：核心层改框高（P1 该框底边 2310 → 约 2340）或重排该段只留两行；改核心后核心 + 全部 11 个 fan-out 版重渲染、重跑 proof。fan-out 侧无法修（动核心布局即破 freeze）。

### D2 — P3「A SEMANA, DIA A DIA」日程末条换行碎片落在奶油框外
- 页码/定位：P3 右栏，奶油框 `y[200,525]`；碎片「16h30.」基线 y=540.6，墨迹盒 `[1461.5, 525.1, 1531.5, 540.9]`。
- 实测证据：真墨迹墨顶比框底低 +0.1px、墨底 +15.9px——整片完全在框外；像素裁图 `p3-d2-crop.png`：「Sáb 21 — Palmeiras × Flamengo, às」在奶油底上，「16h30.」孤零零落在框下白纸上，肉眼可见。creambox：inside-only 末行 510.1（余量 +14.9），BELOW-WINDOW +15.6。
- 归属：**核心**。core-pt 逐一一致（`box y=200 bottom=525.0`、BELOW-WINDOW +15.6 同文同值）。
- 修复建议：核心层改框高（该框底边 525 → 约 545）或改写该条使之不换行；改核心后全量重渲染、重跑 proof。

### D3 — P6「O CAMINHO ATÉ O GABARITO」时间线末行骑在奶油框底边上
- 页码/定位：P6 右栏，奶油框 `y[200,840]`；行「Página do Participante.」基线 y=840.8，墨迹盒 `[1603.5, 825.5, 1828.5, 846.0]`。
- 实测证据：真墨迹墨顶在框内 −14.5px、墨底出框 +6.0px——框底边横切该行中部，「Página」的降部字母 g 伸出框外约 6px；像素裁图 `p6-d3-crop.png`：该行上半在奶油底、下半（含 g 降部）在白纸上，放大可见，整页缩略不明显。creambox：inside-only 末行 811.4（余量 +28.6），BELOW-WINDOW +0.8。
- 归属：**核心**。core-pt 逐一一致（`box y=200 bottom=840.0`、BELOW-WINDOW +0.8 同文同值）。
- 修复建议：核心层改框高（该框底边 840 → 约 850）；改核心后全量重渲染、重跑 proof。

### D4 — P7「A PALAVRA」框标题意大利语 gloss 伸出奶油框右缘 29.5px
- 页码/定位：P7 右栏，奶油框 `x[1440,1862] y[1187,1461]`；标题「A PALAVRA　La parola della settimana」基线 y=1229.0，墨右 1891.5。
- 实测证据：真墨迹墨右比框右缘多 +29.5px，同时超出页右版心 1862 达 29.5px（页内，未出页边）；像素裁图 `p7-d4-crop.png`：「settimana」末尾「…na」落在白纸上，肉眼清楚可见。核心对照：core 同标题「A PALAVRA　本周生词」墨右 1697.2（框内 −164.8）——意大利语 gloss「La parola della settimana」远长于中文 gloss，是本版引入的溢出（同类前科：it-de D1、it-fr D1/D2/D3、es-pt D1）。
- 归属：**本版（意大利语层）**。
- 修复建议：缩短该标题的意大利语 gloss（如「La parola」或「Parola della settimana」，须实测墨右 ≤1862）；或降该标题字距/字号。只改本版讲解层，不动核心；改后重渲染本版、重跑 creambox + occlusion + 目视。

### D5 — P1「NESTA EDIÇÃO」框标题意大利语 gloss 伸出奶油框右缘 2.5px
- 页码/定位：P1 右栏，奶油框 `x[1440,1862] y[1238,1578]`；标题「NESTA EDIÇÃO　In questo numero」基线 y=1278.35，墨右 1864.5。
- 实测证据：真墨迹墨右比框右缘多 +2.5px；像素裁图 `p1-d5-crop.png`：「numero」末字母 o 的尾部约 2.5px 在白纸上，放大可见，整页缩略不可见。核心对照：core 同标题墨右 1752.5（框内 −109.5）——为本版 gloss 加长所致，同 D4 一类、幅度极小。
- 归属：**本版（意大利语层）**。
- 修复建议：与 D4 同批修（缩短 gloss 或微调字距，实测墨右 ≤1862）；可与 D4 同一修复轮次做。

## 未决事项

- **O1 — D1–D3 的修复口径待定。** 三项皆为核心几何缺陷，修核心即牵动核心 + 全部 fan-out 版重渲染与重跑 proof；不修则本版带核心缺陷定稿。请协调方决定：是现在修核心全量重跑，还是接受核心缺陷、仅修本版 D4/D5 后定稿本版。（按 SOP §8 proofread-until-zero，本轮不能以“核心缺陷不归本版”为由直接定稿。）
- **O2 — Q125「rodada 36」未做外部核实。** 内部一致（P4 称 35 轮止于周四 19 日，周六 21 日一场应为 36 轮），但未对照真实 2026 巴甲赛程外部核实；核心 KIT 称事实已于 2026-11-10 核查。本轮不记缺陷，仅记未外部复核。
- **O3 — P4 两处夺冠次数未做外部核实。** 「Grêmio busca o sexto título — e joga a décima final」「O Palmeiras busca o quinto título」取自核心，未在 live 源复核；半决赛比分/决赛日期/F1 结果已 live 核实无误（见 GATE-LOG）。不记缺陷，仅记未复核。
- **O4 — P8 注行墨右 1862.2（+0.2px）。** 「Una breve nota per risposta　✓ segna il testo modello」墨右超出右版心 0.2px，在 PIL 取整容差内，判为非缺陷，无须动作（见 GATE-LOG）。

## 核实摘要（本轮独立实测，非复述 KIT）

- 全文通读：印 PDF 8 页逐版看图 + text.md 534 行逐行读；葡萄牙语正文与意大利语讲解逐项核对；未见拼写、性数配合、变位、标点、截断、重复词问题。
- 事实抽查（live 源）：2026-11-07 Atlético-MG 1–1 Grêmio（Arena MRV；Renan Lodi、Carlos Vinícius 进球；首回合 2–0、总比分 3–1）、2026-11-08 Vasco 2–1 Palmeiras（São Januário；点球 5–4；首回合 1–0、总比分 2–2）、决赛 12 月 6 日单场 Mané Garrincha——与 P4 逐字相符；F1 圣保罗站 Norris 冠军、Verstappen 第 2、Hadjar 第 3、Mercedes 锁定车队冠军——与 P4 逐字相符。日期星期：2026-11-16 周一、11-15 周日、11-20 周五、11-21 周六、11-22 周日、11-27 周五均合日历。P6 工作日算术复核：11 月 16–30 日共 15 天 = 10 个工作日（16、17、18、19、23、24、25、26、27、30 日）+ 5 个周末/假日（20、21、22、28、29 日）；第 10 个工作日 = 11 月 30 日，与正文「27–30 日之间（视 20 日假期是否计入）」一致。
- 数字核对：Q83–Q86（15 天 / 10 工作日 / 5 假日 / 10+5=15）与 P6 图表一致；范文 88 词按构建程序口径 `len(MODELO.split())`=88，在 80–100 范围内；P1 头条 41 非空字符 ≤56。
- 讲解层本地化：E 节标题 SVG 为「E　TRADUZA」、text.md 为「### E · Traduza」（葡萄牙语目标语标签，正确）；全版无中文「翻譯」残留；P8 CJK 字符数 0；P7 八句本周短语均逐字出自本期正文、意译 + 页码标注齐全；读者来信披露意译 3 行、示例标签意译齐全；Q150 答案注为意大利语。
- 已排除的疑似问题（详见 GATE-LOG）：P1 LINEX 0.2px 擦痕（KIT 称 1 flag）未复现且像素裁图见清晰间隙；5 处 desc-clear 负值经真墨迹核实均无降部字母、实测余量 +4.2~+4.9px；「o título → campione」与「cair → cadere in un giorno」均为五版 pt fan-out 共用 gloss 惯例；ASCII 省略号撇号为全 program 惯例（pt-fr 52 处同）；「L’EDIZIONE」SVG 文本为 U+2019 无空格，属字体渲染特性。
