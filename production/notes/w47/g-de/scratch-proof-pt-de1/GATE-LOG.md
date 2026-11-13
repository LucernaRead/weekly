# GATE-LOG — 2026-W47 pt-de proof1（独立复校机械门实跑记录）

独立复校员 proof1，2026-11-11。工具链：`~/workspace/weekly-git/tools/venv/bin/python`；
TMPDIR 全程指向 scratch 下 `tmp/`（系统 /tmp 未用）。
正典 creambox：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`
（md5 `ee7a55d8b2057cf4ad42a97bb1197383` ✓）。
所用运行命令与输出均列于下；KIT 自述数值一律不采信，只认以下本人实跑结果。
Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-de1/`

## §0 身份与探针

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` →
  `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0；随后 scratch 写 `probe.txt`（`probe-ok`）成功。
  （探针写了一个无引用孤 blob，无影响。）
- SHA/字节核对（`sha256sum` + `stat`）：印 PDF 12,938,940 B `a1b7bfc2…274c48f` ✓；
  网 PDF 1,110,425 B `26647474…79b87` ✓；text.md 37,905 B `f33307b8…57da` ✓。与任务一致。
- 版目录 git 状态：`?? production/2026-w47/2026-w47-pt-de/`（未入仓）；本次未 commit、未 push、未改源文件。
- SOP：仓库根 `SOP.md`（319 行）已读；仓库 `AGENTS.md` 已读。核心规则（proofread-until-zero、
  几何审计必过、p8 compare --total 必跑、讲解用读者母语、对外禁内部标签）均执行。

## §1 gates.py（构建自检，独立重跑）— 16/16 PASS

命令：`cd production/2026-w47/2026-w47-pt-de && tools/venv/bin/python gates.py`，RC=0，
`FAILURES: none`。逐项：P1 VOL.4+日期 / 副标题 / 页脚+页码 8/8 / 无 VOL.3 残留 /
截稿注+决赛命名 / P1 刊头行 ≤1820（{330: 262.9, 372: 767.3}）/ 同基线墨迹碰撞 0 /
页框墨迹穿越 0（最小边距 L/R/T/B = 47.0/46.5/35.0/36.0，框为 40…1910）/
P6 图表标签覆盖 0% / gloss 29 项 / gloss 词头存活 0 缺失 / P7 引言 8 条各 2× + 页签 + 德语 /
读者园地 5/5 / 图片+出处 5/5 / P7 引言避开预告框（最大基线 2393.995）/ P1 头条 ≤56 非空字符（41）。

## §2 occlusion 审计 — 0 标记

命令：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-pt-de --json <scratch>/de-occlusion-proof1.json`
输出：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；
`production/2026-w47/2026-w47-pt-de/svg: 0 flags`，RC=0。
注：审计对奶油框内溢出/框标题溢出/横向溢出/降部溢出有盲区（SOP 附则一补注），
故 §3–§7 另行实测，不以 0 标记为准——D1/D2/D3 即如此查出。

## §3 正典 creambox.py 全版扫描 — 31 框；3 处实缺陷（D1/D2/D3），余皆裁定非缺陷

命令：`tools/venv/bin/python <goals>/hidden_files/w47/tools/creambox.py svg/*.svg > <scratch>/creambox-all-proof1.log`。
P7-TOOLBOX 汇总：3 框，inside clearance 最小 +5.1，desc-clear 最小 −0.9。
全部负值裁决（见 PROOF-NOTE；完整逐框表在 `creambox-all-proof1.log`）：
- BELOW-WINDOW 真漫出 3 处：P1 闪讯框 +17.6 `em Brasília. (Página 4)`（D1）；
  P3 日程框 +15.6 `16h30.`（D2）；P6 时间线框 +0.8 `Página do Participante.`（D3）。
- BELOW-WINDOW 假阳性 5 处（下块标题/段落，+32…+42）：P1 数字框后 `AGORA VOCÊ…` +37.0；
  P2 日程框后 `Atenção:…` +32.0；P3 HINWEIS 框后 `UM DIA, DOIS SENTIDOS` +37.0；
  P6 图表框后 `EXERCÍCIOS　SEITE 6 ÜBUNGEN` +42.0 ×2。
- inside-only desc-clear 负值 6 处（−0.3…−1.1）均为误报：PIL 真墨水实测（§4）6 行均无降部字母，
  墨迹底 = 基线 −1px，距框底 6.1–6.7px。
- 其余 22 框 inside-only clearance 均为正（最小 +5.1），desc-clear 均为正。
- 同工具对 core-pt（p1/p3/p6）重跑（`creambox-core-p1p3p6.log`）：D1/D2/D3 三处几何与文字
  在核心中逐字相同（P1 框内末行同为 +9.6、框外同为 +17.6；P3 +15.6；P6 +0.8），归属核心。

## §4 PIL 真墨水实测（Newsreader，tools/fonts）

- 降部深度（20px）：`g/p/y/q` 墨迹底 = 基线 +4px，`j` +5px；font metrics ascent/descent = 15/6。
- D3：`Página do Participante.` 墨迹底 = 基线 +4px；基线 840.8、框底 840.0 → 漫出 4.8px。
- 6 行 desc-clear 负值行：`schicken Sie sie ein.` / `zwei Sätze und schicken Sie sie ein.` /
  `2027.` / `Sie sie ein.` / `Kultur.` / `em Brasília. (Página 4)`（末者为整行框外，另计）——
  前 5 行墨迹底均为基线 −1px（无 `g/j/p/q/y`），无漫出。
- 像素扫描（`cards/*.png`，1:1 SVG 单位）：
  P1 奶油止于 y=2309，漫出行墨迹 y=2314–2330；P3 奶油止于 y=524，`16h30.` 墨迹 y=526–540；
  P6 奶油止于 y=839，框底外墨迹 y=840–845。裁切图：`crop-p1-flashbox.png`、
  `crop-p3-schedbox.png`、`crop-p6-timeline.png`（各 2×放大）。
- 框标题（boxtitle）PIL 实测（`boxtitle-p1-proof1.log` 修正版 `boxtitle2-proof1.log`）：
  31 框标题墨迹右缘均在框内，余量 +16.5…+562.0px；最紧三处：P1 `NESTA EDIÇÃO　In dieser Ausgabe` +16.5、
  P1 `EM POUCAS PALAVRAS　IN KÜRZE` +18.5、P1 `A SEMANA EM NÚMEROS　In Zahlen` +18.5。
  P1 刊头行：`A Lucerna` 墨迹 561.0…1389.0；副标题段末 `A FINAL DA COPA` 止于 1800.8；
  顶栏三段止于 1800.5；tagline 止于 1358.3。
- 200dpi 像素扫描（PyMuPDF 渲染印 PDF，`pdf-checks-proof1.log`）：P1 刊头行（y300–390）
  最右墨迹 1817.8 SVG 单位；P2 日程标题行最右墨迹 1864.8（含抗锯齿阈值影响；PNG 卡片同行实测 1860，
  PDF span advance 右缘 1865.8——见 §5 末条裁定）。
- 全版横向墨迹扫描（PIL，框 40…1910）：无任何文本墨迹出框；唯一超名义内容边 1862 的是两处
  独立德语 gloss 行 advance（P2 标题 1865.8、P8 注 1865.7），渲染墨迹分别为 1860/1864，
  距页边 ≥84px，裁定非缺陷（O3）。

## §5 p8 compare / freeze / keycheck

- `tools/p8.py extract --p8 svg/p8-avaliacao.svg --total 150`：`noted set = 150 of 150`，RC=0。
- `tools/p8.py compare --core-dir production/2026-w47/core-pt --edition-dir production/2026-w47/2026-w47-pt-de --target pt --total 150`：
  `core 150 noted / edition 150 noted / status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`，RC=0。
  keydiff 两题逐题验：137 `Freitag, 20. November, ist ein nationaler Feiertag.`、
  138 `Palmeiras gewann das Elfmeterschießen mit 5:4.`——德语正确，核心 Q131=A 的 D2 修正亦在本版。
- `tools/freeze.py baseline --build . --core-svg svg --out <scratch>/de-freeze-proof1b`（日志 `freeze-baseline-proof1.log`）：
  `baseline: 8/8 SVGs byte-identical (repointed files: none)`，RC=0，core 完整性 8 文件重哈希无改动。
- `tools/freeze.py diff --core-svg production/2026-w47/core-pt/svg --edition-svg svg`：
  每页 +26…+196 / −22…−752 串；新增 CJK 共 9 个，全部为 U+3000 家具分隔符（P1: 2，其余每页 1），RC=0。
- 150 题手验：`keycheck-150.json`，150/150 correct（方法见该文件头；含 Q83–87 工作日重算、
  Q120 5 小时重算、Q125 外部赛程核实）。印 PDF P8 答案流与 text.md Respostas 机械比对：
  149/150 逐字一致，仅 Q150 为提取换行 artifact（PDF 提取 `✓Siehe` 并行与 `(88` 断行；
  目视 P8 图为 `150. ✓ Siehe den Mustertext in Abschnitt H auf dieser Seite (88 Wörter)`，一致）。
- 模型文重数 88 词；题号 1–150 连续；每页题量 10/18/18/18/18/18/12/38；
  P6 图表柱宽 300 vs 150（10 天 vs 5 天，2:1）。

## §6 印/网文字层比对、字号、引号

- PyMuPDF 提取：印 PDF 8 页 1462.5×2025pt；网 PDF 8 页；印/网文本各 47,015 字节、8,436 词，
  词多重集差 = 0（`pdf-checks-proof1.log`）。
- P8 最小字号实测（PyMuPDF span，印 PDF）：9.75pt（最小 span 如 `1. consciência — …`、`100. chute — …`；
  全版最小亦为 9.75pt，仅在 P8），正好 SOP §1.1 底线 9.75pt，不低于。KIT 数字 9.75pt 经独立实测证实。
- 弯引号全版扫描（SVG 抽取 base64 后 + text.md + 印/网 PDF 文本）：
  U+201C 2、U+201D 2（均在 P8 E 节 139/140 两句德语句，印/网 PDF 均有且渲染正常）、
  U+2019 0；« 40、» 40。无缺引号、无豆腐块。

## §7 判为非缺陷的项（证据摘要）

1. (a) P1 标题横向溢出：未复现（§4：框标题余量 ≥+16.5px；刊头副标题止于 1818.4；200dpi 刊头行 1817.8）。
2. (b) P3/P5 降部漫出：未复现（§3/§4：6 行负 desc-clear 均为无降部字母误报，PIL 墨迹底基线 −1px）。
3. (c) P7 toolbox：通过（§3：3 框，inside 最小 +5.1；ERROS +29.6、词框 +5.1、CARTAS +10.9）。
4. (d) E 节 type 标签：已本地化（P8 E 节 4×`Übersetzung`；text.md `E · Traduza`；text.md CJK 0；
   SVG CJK 仅 U+3000 + P1 `<title>Lucerna 三色蛾</title>` 元数据，非渲染文本）。
5. 内部标签扫描（仅 `<text>` 元素）：零命中；P7 的 VOL.3/VOL.5 均在读者园地披露与下期预告正文内，
   属合法读者内容（gates 同项 PASS）。
6. `«consciência»` 引号空格不一致（P1 无内空格 vs P7 有内空格）：核心同款（core-pt-zh-cn 第 52/406 行），
   记 O1 观察，非缺陷。
7. P3/P5 `Kasten.` 孤字、P4 `B AS PALAVRAS` 栏目标题落栏底：KIT 已注明的核心流式行为，接受。
8. P2 日程标题与 P8 注 advance 超名义边 1862 约 3–4px：渲染墨迹 1860/1864，距页边 ≥84px，
   gates 框内，记 O3，非缺陷。
9. 家具字体 `Noto Sans CJK SC`（SOP §1.1 规定拉丁读者语家具用 Newsreader）：核心同款系统约定，
   无可见缺陷，记 O2。
10. 外部事实复核：Q125（36ª rodada, Palmeiras × Flamengo, sábado 21/11, 16h30, Nubank Parque）
    与 P4 表 `Nubank Parque` 均经 CBF 赛程证实（§8）。

## §8 外部事实来源

- Brasileirão 36ª rodada Palmeiras × Flamengo（21/11/2026 周六 16h30, Nubank Parque）：
  brasileirao.com.br《Flamengo conhece agenda das quatro rodadas finais do Brasileirão》（2026-11-07；
  “no sábado (21), o Rubro-Negro visita o Palmeiras às 16h30, no Nubank Parque, pela 36ª rodada”）；
  colunadofla.com《CBF divulga dias e horários das 2 últimas rodadas》（2026-11-06；
  “36ª rodada: Palmeiras x Flamengo – sábado (21/11), às 16h30, no Nubank Parque”）；
  portaldopalestra.com.br《Palmeiras x Flamengo: data e horário》（2026-11-01；
  “no sábado, 21 de novembro, às 16h30, no Nubank Parque, pela 36ª rodada do Brasileirão”）；
  sportradar.com 赛程页（Matchday 36, Nov 21, 2026, Nubank Parque）。
- 其余事实（Zumbi/Leis、Enem Edital 64/2026、半决赛比分）为核心冻结内容，KIT §2 称已核（2026-11-10），
  本次未逐项重查外部来源——除 Q125 与工作日算术外，事实类结论以核心 KIT 来源为准，
  已在 PROOF-NOTE 中如实说明。

## 附：输出文件（本 scratch 目录）

- `PROOF-NOTE.md`（结论 (b) + 缺陷 D1–D3 + 未决 O1–O5）
- `GATE-LOG.md`（本文件）
- `keycheck-150.json`（150 题逐题手验，150/150 correct）
- `de-occlusion-proof1.json`、`creambox-all-proof1.log`、`creambox-core-p1p3p6.log`、
  `freeze-baseline-proof1.log`、`boxtitle-p1-proof1.log`、`boxtitle2-proof1.log`、
  `pdf-checks-proof1.log`、`crop-p1-flashbox.png`、`crop-p3-schedbox.png`、`crop-p6-timeline.png`、
  `make_keycheck.py`、`probe.txt`、`tmp/`（TMPDIR）
