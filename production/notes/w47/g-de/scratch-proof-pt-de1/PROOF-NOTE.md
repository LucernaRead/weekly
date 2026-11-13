# PROOF-NOTE — 2026-W47 pt-de（葡萄牙语目标 · 德语读者）proof1

独立复校员：proof1（完整独立复校），2026-11-11。
Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-de1/`
（全部工作文件见该目录；仓库侧未写任何文件，源文件未改动，未 commit，未 push。）

## §0 版身份核对（磁盘为准）

| 文件 | 磁盘字节数 | 磁盘 SHA-256 | 与任务一致 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | 12,938,940 | `a1b7bfc28e2a74b3ab9918dbc7f5e516ca7d7ef1b8fe56a6cc7921760274c48f` | ✓ |
| `A-Lucerna-VOL4-web.pdf`（网） | 1,110,425 | `26647474dbeb744211c4b67f3b6c3af9917024aaf3940d2e7a82cca917a79b87` | ✓ |
| `2026-w47-pt-de.text.md` | 37,905 | `f33307b8413e34a3fa113dd11942dc7f02213d08d15c709dfa3e192e9a0c57da` | ✓ |

三份 SHA 与字节数与任务消息完全一致。creambox 正典工具 md5 `ee7a55d8b2057cf4ad42a97bb1197383` ✓。
另记：版目录在 git 中目前为 untracked（`git status --porcelain` 显示 `?? production/2026-w47/2026-w47-pt-de/`），
本次未做任何 commit/push；探针 `git hash-object -w` 按任务要求写了一个孤 blob（`9daeafb9…`，无引用，无影响）。

## 结论：(b) 有缺陷，不能定稿

发现 **3 项缺陷，均已实测证实、均在渲染成品上肉眼可见，归属均为核心（core-pt）**——
几何与葡语正文在核心与本版完全一致，德语讲解层未引入任何一处。
按 SOP §8 proofread-until-zero，本版当前状态不能定稿；修复须在 core-pt 落地后重渲染核心、
重新 fan-out（至少本版；同几何亦存在于核心及全部 11 个 pt 讲解版，需协调员定是否同批修）。

## 缺陷清单

### D1（中）P1 框外整行：EM POUCAS PALAVRAS 框末行漫出框底

- **页码 / 定位**：P1 右栏奶油框 `x=1439.5, y=1874, bottom=2310.0`；O FUTEBOL 条目末行
  `em Brasília. (Página 4)`（Newsreader 20，基线 y=2327.6），整行落在框底之外 17.6px、
  白纸底上，紧贴 QUIZ RELÂMPAGO 栏目标题上方。
- **归属**：核心（core-pt 同框同文同几何，见 GATE-LOG §5；德语层未动此处）。
- **实测证据**（三法一致）：
  1. 正典 creambox.py 全版扫描：该框 inside-only 末行 `Brasil: a decisão é no dia 6 de dezembro,`
     clearance +9.6，BELOW-WINDOW +17.6 `em Brasília. (Página 4)`（同类整行漫出判据 +12…+18px 同流续行）。
  2. 200dpi/1:1 像素扫描（`cards/p1-capa.png`）：奶油行止于 y=2309，漫出行的墨迹行 y=2314–2330，
     框底到墨迹顶 4px、到底 20px。
  3. 目视：`crop-p1-flashbox.png`（2×放大）与整版 P1 图均可见该行坐在奶油框外的白底上。
- **修复建议**：core-pt 把该框加高 ≥28px（或重排 O FUTEBOL 使末行收进框内）；重渲染核心，
  重新 fan-out，复跑 freeze + p8 compare + occlusion + creambox 全版扫描复验。

### D2（中）P3 框外整行：A SEMANA, DIA A DIA 框末行漫出框底

- **页码 / 定位**：P3 右栏奶油框 `x=1439.5, y=200, bottom=525.0`；日程末行 `16h30.`
  （基线 y=540.6），整行落在框底之外 15.6px，夹在该框与下方 E VOCÊ 框（top 551）之间的白底间隙。
- **归属**：核心（core-pt 同框同文同几何）。
- **实测证据**：
  1. creambox：inside-only 末行 `Sáb 21 — Palmeiras × Flamengo, às` clearance +14.9，
     BELOW-WINDOW +15.6 `16h30.`（同流续行，非下块标题）。
  2. 像素扫描：奶油行止于 y=524（另 1px 抗锯齿噪点除外），`16h30.` 墨迹行 y=526–540。
  3. 目视：`crop-p3-schedbox.png` 与整版 P3 图均可见 `16h30.` 坐在两框之间的白底上。
- **修复建议**：core-pt 把该框加高 ≥20px（或改写使 `16h30.` 与上一行同行）；重渲染 + 重 fan-out + 全部门复验。

### D3（中低）P6 框底降部漫出：时间线框末行降部字母跨过框边

- **页码 / 定位**：P6 右栏时间线奶油框 `x=1439.5, y=200, bottom=840.0`；末行
  `Página do Participante.`（Newsreader 21，基线 y=840.8）基线即在框底外 0.8px，
  其中 `g`（Página）与 `p`（Participante）两处降部墨迹伸出框底约 5px。
- **归属**：核心（core-pt 同框同文同几何）。即任务必查项 (b) 的同类缺陷，
  在 P6（非 P3/P5）复现。
- **实测证据**：
  1. creambox：inside-only 末行 `A nota individual sai na` clearance +28.6，
     BELOW-WINDOW +0.8 `Página do Participante.`。
  2. PIL 真墨水实测：Newsreader 降部深 4px（20px 字，`j` 为 5px；font metrics descent 6）；
     基线 840.8 + 4px = 墨迹底 844.8，即框底外 4.8px。
  3. 像素扫描：奶油行止于 y=839，框底外墨迹行 y=840–845（降部尾）。
  4. 目视：`crop-p6-timeline.png` 中该行贴框底边，降部尾触边/出边。
- **修复建议**：core-pt 把该框加高 ≥8px（或重排 JAN. 2027 条目）；重渲染 + 重 fan-out + 全部门复验。

## 必查项 (a)–(d) 裁决

- **(a) P1 框标题/副标题横向溢出——未复现。** 全部 31 个奶油框标题 PIL 真墨水实测均在框内，
  余量最小 +16.5px（P1 `NESTA EDIÇÃO　In dieser Ausgabe`）、+18.5px（P1 `EM POUCAS PALAVRAS　IN KÜRZE`、
  `A SEMANA EM NÚMEROS　In Zahlen`）；刊头副标题 PDF span 右缘 1818.4 SVG 单位，
  200dpi 像素扫描刊头行最右墨迹 1817.8，均在内容边 1862 内。occlusion 审计 BOXTITLE 类 0 标记（自检阳性对照全过）。
- **(b) P3/P5 右栏末行降部漫出——未复现。** creambox 6 处 desc-clear 负值（−0.3…−1.1）
  均为 0.30em  allowance 的误报：PIL 真墨水实测 6 行均无降部字母（`schicken Sie sie ein.` ×2、
  `zwei Sätze und schicken Sie sie ein.`、`2027.`、`Sie sie ein.`、`Kultur.`），墨迹底 = 基线 −1px，
  距框底 6.1–6.7px。无漫出。——但同类缺陷在 P6 复现为 D3（见上）。
- **(c) P7 toolbox clearance——实测通过，无缺陷。** creambox P7-TOOLBOX 汇总：3 框，
  inside clearance 最小 +5.1，desc-clear 最小 −0.9（该行 `Kultur.` 无降部字母，PIL 墨迹底基线 −1px）；
  ERROS COMUNS 框 +29.6、CARTAS 框 +10.9。occlusion 0 标记。
- **(d) text.md 第 E 节 type 标签——未复现，已本地化。** P8 E 节 4 题标签均为德语 `Übersetzung`，
  text.md 标题为葡语 `E · Traduza`；全版 CJK 扫描 text.md 为 0，SVG 仅 U+3000 分隔符
  （+ P1 `<title>Lucerna 三色蛾</title>` 元数据，非渲染文本）。无中文「翻譯」残留。

## 全文通读核实摘要

- text.md 535 行逐行读过；印 PDF 8 页逐版看图；150 题逐题手验（`keycheck-150.json`），150/150 正确。
- 事实重算：P6 工作日计数 16–30日 = 15 天、10 个工作日、5 个周末/假日、10+5=15（Q83–87 全对）；
  Q120 13h30–18h30 = 5 小时；Q125 「36ª rodada, Palmeiras × Flamengo, sábado 21, 16h30, Nubank Parque」
  经外部来源证实（CBF 赛程：brasileirao.com.br、colunadofla、portaldopalestra，见 GATE-LOG §8）；
  P6 图表柱宽 300 vs 150（10 天 vs 5 天，正好 2:1）；范文 88 词重数 = 88；题号 1–150 连续，
  每页题量 10/18/18/18/18/18/12/38。
- 印/网文字层：各 47,015 字节、8,436 词，词多重集差 = 0。
- P8 最小字号实测 9.75pt（PyMuPDF span，全版最小亦为 9.75pt，仅在 P8），正好 SOP §1.1 底线，不低于。
- 弯引号：U+201C/U+201D 各 2（E 节 139/140 两句德语句），印/网 PDF 均有且渲染正常；
  U+2019 全版 0；«» 各 40。de-en fix2（Newsreader 闭引号渲染）在此版成立。
- 印 PDF 8 页、1462.5×2025pt；网 PDF 8 页；钥匙 p8 compare vs core CLEAN，keydiff 仅 [137, 138]
  （两句译文答案，德语正确：`Freitag, 20. November, ist ein nationaler Feiertag.` /
  `Palmeiras gewann das Elfmeterschießen mit 5:4.`）。
- 冻结：freeze baseline 8/8 字节一致；freeze diff 新增 CJK 仅 9 个 U+3000 家具分隔符。
- 其余机械门：gates.py 16/16 PASS；occlusion 审计 0 标记（自检阳性对照 6 类全触发）；
  p8 extract 150/150。

## 未决事项

- **O1**（核心排版观察，非缺陷）：`«consciência»` 引号内空格前后不一致——P1 用 `«consciência»`
  （无内空格），P7 词框用 `« consciência »`（有内空格）。核心 pt-zh-cn text.md 第 52/406 行亦然，
  为核心继承；不影响阅读，建议核心统一为一种形式。
- **O2**（系统约定观察，非缺陷）：读者语家具字串（如 `Übersetzung`、`QUIZ RELÂMPAGO　Blitzquiz`）
  在 SVG 中字体为 `Noto Sans CJK SC`，而 SOP §1.1 规定拉丁读者语家具用 Newsreader。
  核心亦同，属构建系统约定，非本版缺陷；是否改属系统决定。
- **O3**（已裁定非缺陷）：两处独立德语 gloss 行 advance 右缘超出名义内容边 1862 约 3–4px——
  P2 日程标题 `…eine Woche geplant`（PDF span 右缘 1865.8，渲染墨迹 PNG 1860 / 200dpi 1864.8）、
  P8 注 `✓kennzeichnet den Mustertext`（span 右缘 1865.7，墨迹 1864）。距页边仍 ≥84px，
  在 gates 框（40…1910）内，无可见溢出、无压线、无裁切。
- **O4**（KIT 已注明，接受）：P3/P5 `Kasten.` 孤字、P4 `B AS PALAVRAS` 栏目标题落栏底，
  均为核心流式排版行为，非缺陷。
- **O5**（KIT 已注明）：P1 `EM POUCAS PALAVRAS IN KÜRZE` 贴框边但在框内（实测余量 +18.5px）。

## 建议后续

1. 协调员定 D1–D3 的核心修复（core-pt 三框加高/重排），重渲染核心后重新 fan-out pt 全部 11 版
   （同几何在核心及各讲解版均存在），复跑全部机械门后重新 proof。
2. 本版德语讲解层本身零问题：150 键全对、讲解/导读均为德语、无内部标签、无中文残留、文字层一致。
   核心修好重 fan-out 后，本版只需按同一规程复核（重点为三框复测）。
