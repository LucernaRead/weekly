# GATE-LOG — 2026-W47 ja-es 第一轮独立校对（叶子）

校对员：叶子。工作目录 `~/workspace/weekly-git`。本人笔记目录：
`hidden_files/w47/scratch-proof-ja-es1/`（PROOF-NOTE.md、GATE-LOG.md、
`render-print/`、`render-web/`、`text/`、`svg-sha-original.txt`、
`svg-sha-rebuild.txt`、`rebuild-run.log`、`es1-occlusion.json`、`es1-p8.json`、
`es1-p8-core.json`、`es1-p8compare.json`、`rebuild/` 副本构建目录）。

## 0. 开工硬门禁（双通才动手）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin`
  → `da0c4eb8d9a48d171a33574b380752e183286751`，RC=0。
- `hidden_files/w47/scratch-proof-ja-es1/.probe` 真实写入成功
  （`probe-ok 2026-11-11T05:30:53Z`）。
- 红线遵守：未碰 core-ja、W43–W46、其他目标语家庭、tools/；未跑 insert.py、
  未跑 lint --write，未 git add/commit/push/reset/stash，未改任何成品。
  构建重跑在本人 scratch 副本 `scratch-proof-ja-es1/rebuild/` 内进行；
  原构建目录 8 个 SVG 在校对开始与结束时 `sha256sum -c` 逐一 OK，未变。

## 1. 身份核对

```
print Lucerna-VOL4-JA-ES.pdf      29,102,097 bytes
  sha256 0feb61136c4c9c267a9c84664287c6bb1a897ddb2fc496d79137073542eacb55 (8 pages)
web   Lucerna-VOL4-JA-ES-web.pdf   4,482,717 bytes
  sha256 b274eac2faa2a91cdeefc303092805253b34f3cacfef095cded332cee5e95380 (8 pages)
```
与任务单与 KIT §8 登记一致（字节数与 SHA 前 8 位及完整串均一致）。

## 2. 机械门（全部自跑）

### 2.1 冻结重跑（freeze）
- 做法：完整复制构建目录（*.py、*.md、ABSTRACT.txt、assets/）至
  `scratch-proof-ja-es1/rebuild/`，排除 svg/、cards/、PDF、__pycache__；
  用 KIT §9 指定的解释器 `tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0——
  与构建相同的解释器，ko 家庭已证实的 Pillow 版本差风险已用此方式规避）跑 `run.py`。
- 结果：exit 0；`FLOW OVERFLOW` / `HEAD TOO WIDE` grep 计 0；
  8/8 SVG 与原构建逐字节相同（`diff svg-sha-original.txt svg-sha-rebuild.txt` 空；
  原始 SHA 见 `svg-sha-original.txt`，重跑 SHA 见 `svg-sha-rebuild.txt`）：
  p1 `7dd43e66…`、p2 `0ef2001d…`、p3 `8afb24cc…`、p4 `b26e6867…`、
  p5 `7170970d…`、p6 `c4c405b4…`、p7 `d00608f9…`、p8 `cb2813a7…`（完整串见文件）。
- 重跑 registry（`rebuild-run.log` 尾部）：TOTAL 150；by level A2 48 / B1 73 / B2 29；
  by page {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；
  by type {completa:50, opción múltiple:51, relacionar:12, construye una frase:8,
  verdadero o falso:11, cloze:13, Traduce:4, Redacción:1}；model chars: 154。
  P8-keys flow 终点 col 3 y=2397（底 2540）。

### 2.2 几何遮挡审计
- `tools/venv/bin/python tools/occlusion_audit.py --selftest`
  → `selftest OK: planted classes fired {'BOXTITLE':1,'COVER':1,'EDGE':1,'FOOTER':1,
  'LINEX':1,'TEXTX':1}; clean controls silent`。
- `tools/venv/bin/python tools/occlusion_audit.py <es svg dir> --json es1-occlusion.json`
  → `0 flags`，RC=0。

### 2.3 P8 提取与比对
- `tools/p8.py extract --p8 <es p8 svg> --total 150 --json es1-p8.json`
  → `noted set = 150 of 150 (parse: lines)`，RC=0。
- `tools/p8.py compare --core-p8 <core-ja p8 svg> --edition-p8 <es p8 svg> --total 150
  --json es1-p8compare.json`
  → `core 150 noted; edition 150 noted; status: CLEAN; missing=[]; extra_count=0;
  uncertain=[]; keydiff=[137, 138, 139, 140]`，RC=0。
- 另对核心 P8 跑 extract（`es1-p8-core.json`）取键值逐一比对：150 键中仅 137–140 不同，
  其余 146 个键值逐字相同。137–140 的 es 值逐条对题面核实为正确西班牙文翻译
  （见 PROOF-NOTE §2.2；139 为 F1 认可的缩短）。
- 注意：p8.py 的 keys 只存键值（字母/数字），不存注文散文——D1 的罗马字错误不在其比对范围。

### 2.4 print/web 文字层一致
- `pdftotext -layout` 两版各 102,065 字节，`cmp` 通过：`PRINT_WEB_TEXT_IDENTICAL`。
- web PDF 4,482,717 字节 < 7 MB。

### 2.5 U+2019 缺陷类回归
- 8 个 SVG 中 U+2019 计数：p1–p8 全部 0（总计 0）。
- text.md 中 U+2019 0、直撇号 0；8 版渲染图目视：无宽字形断裂。

### 2.6 P8 字号（PyMuPDF 测印刷 PDF 第 8 页）
- 尺寸分布（pt: span 数）：9.98:164、10.35:79、10.88:6、11.25:5、11.62:1、12.75:5、
  13.5:2、14.25:37、14.62:12、15.38:3、15.75:16、17.25:4、18.0:39、18.75:2、34.5:3。
- 最小 9.98pt（≥9.75pt 门槛）；次档 10.35pt = 题干（与 KIT 的 9.975pt/10.35pt 一致，
  9.98 为四舍五入）。

### 2.7 §1.1 grep 审计（8 个 SVG）
- `·` 0×；纸色 `#fbfaf6` 合计 8（每页 1×）；旧 `#f7f1e2` 0×；
  禁色（金/红褐/近黑采样）0×；刊头 `font-size="196"`、UnifrakturMaguntia 各 1×（P1）；
  页码行 `Página N de 8` 每页 1×；页脚 `SEMANARIO JAPONÉS VOL.4　Texto en japonés　Explicaciones en español`。
- VOL：VOL.4 各页均有；VOL.3 仅 P4 前号注 1 处；VOL.5 仅 P4 次号预告 1 处 + P7 3 处
  （读者园地披露 2 处、预告条 1 处），均已核对上下文为冻结正文/预告。
- `Foto:` 图注 5 处（P1 Poliphilo、P3 Alainauzas、P5 lumoplank、P7 Mozzucu、P8 lumoplank），
  均为西班牙文 `Foto:` + CC0/公有领域出处。

## 3. 逐题与分级核对（SVG 文本节点 + text.md）

- 徽章白字标签计数：P1 A2 10；P2 A2 15；P3 A2 7/B1 8；P4 B1 18；P5 B1 18；P6 B2 18；
  P7 A2 4/B1 4/B2 4；P8 A2 9/B1 22/B2 4（徽章 rect 共 141 个）。
- 按文档顺序逐题配对最近徽章（含 P8 取首次出现以避开答案区重号）：
  P1 10（A2 10）、P2 18（A2 18）、P3 18（A2 7/B1 11）、P4 18（B1 18）、P5 18（B1 18）、
  P6 18（B2 18）、P7 12（A2 4/B1 4/B2 4）、P8 38（A2 9/B1 22/B2 7）；
  合计 A2 48 / B1 73 / B2 29、总数 150。配对题组级别：25–28 全 A2、43–46 全 B1、141–144 全 B2。
- text.md 题号：独行 `N.` 138 条 + 配对题内联 `N. 词` 12 条 = 150，无缺重。
- text.md 行数：1376 行、非空 1359 行；KIT“1349 text lines”= 非空行减文件头与 8 个
  `## Page N` 标记行（1359−10=1349），已自洽。
- 范文实数：H 节范文去空白后 154 字，与宣称一致。

## 4. 金句与事实核对

- 金句 8 条：日语句与核心版逐字相同；逐句在正文原页真实出现，
  页码引用 1/1/2/3/4/7/1/2 全对（第 7 处另命中 P7 金句节本身，不计）。
- 星期核验（`date -d`，America/Toronto）：2026-11-07 六、2026-11-16 一、2026-11-19 四、
  2026-11-22 日、2026-11-23 一、2026-12-01 二、2026-11-05 四；11 月第 3 木曜日 = 19 日。
- P6 图表：38+24+22+16=100；38−24=14；38+24=62；柱长比例与数值一致，标注为练习数据。
- 相扑事实公开来源佐证（browser.search，2026-11-11）：
  大の里 2 连冠目标/初日义ノ富士/2 日目藤凌駕/豊昇龍 3 场所休场后复出战美ノ海
  （サンスポ 2026-11-06）；藤凌駕 11 场所目金星、7 位速度、3 日目胜豊昇龍
  （日刊スポーツ 2026-11-10）；美ノ海新小結（デイリー 2026-10-27）。
- 美ノ海读音：ちゅらのうみ（sumo-guide.com；日刊スポーツ 2018-05-30；
  デイリー 2026-10-27）。藤凌駕读音：ふじりょうが（sumo-guide.com；
  日刊スポーツ 2025-10-01；ozumo.jp）。

## 5. 翻译层差分核对（核心 ja-zh-cn vs 本版 ja-es，SVG 文本节点全量）

- 每页节点数：P1 145/145、P2 145/143、P3 135/133、P4 153/151、P5 141/140、
  P6 147/146、P7 154/149、P8 329/322（es/core）。
- 核心独有节点 298 个：逐类核查，全部含中文讲解段（`译注｜…`、中文 gloss、中文答案注文），
  另有 1 个非 CJK 节点 `Commons）`——为 P3 图注中文行尾折行残片，对应 es 版
  `Foto: Alainauzas — dominio público (Wikimedia Commons)` 已完整改写，无丢失。
  无一条纯日文核心句丢失。
- es 独有节点：全部为西班牙文，或“日文词头＋西班牙文 gloss”双语节点；
  其中含 CJK 且无假名的 40 个节点，逐一核查均为日文单词头/冻结小节头（熊手、金星、解禁、
  小雪、屋台、千秋楽、見頃、収穫、一番太鼓、京都、発表、練習、来週、〜勝〜敗、〜番目、「昨日」等）
  配西班牙文 gloss，无中文解释句。
- 中文残留词扫描（es 全 SVG 文本节点）：吉伊卡哇 0、参考答案 0、酉之市 0、提名 0、
  译注 0、`｜` 0、练习/阅读/翻译/注释/说明/词汇/语法/发音/例句/问题/选择/填空/意思/中文 0；
  `理解` P2–P6 各 1×，均为冻结日语小节头 `A　理解`。
- Chiikawa：P7 词表 `ちいかわ Chiikawa`、P8 答案 67/106/128；ryuuryuu：P7 gloss、
  P8 答案 66/77/80/105；`吉伊卡哇` 全版 0×。
- `((pág.` 0×；P7 金句引用均为单括号 `(pág. N)`。

## 6. 目视记录（自渲染，非 builder 的图）

- 渲染：`pdftoppm -png -r 100` 自印刷 PDF 得 `render-print/p-1.png` … `p-8.png`；
  自网页 PDF 得 `render-web/p1-1.png`、`p8-8.png`。逐页目视：P1–P8 均无溢出、无重叠、
  无压页脚；网页 P1/P8 与印刷版视觉一致。
- P7 预告条末行 y≈2557（页脚 2580）；P2/P3/P5 中栏 Nota 框下留白与核心版同一版式。
- D1 的 6 条错误注文在 P8 渲染图上均清晰可见（48/49/54/63/111/116）。

## 7. 未能核对的项（缺失材料）

- `hidden_files/w47/scratch-fanout-ja/FANOUT-REPORT-ja.md` 不存在（任务单点名要读的顶部
  审计节与关键裁定备忘无法读到）；KIT §8 引用的 builder 门记录
  （`es-occlusion-run4.json`、`es-p8-run4.json`、`es-p8compare-run4.json`、
  `es-sha-run4.txt`、`es-sha-run5.txt`、`build-es-run5.log`）与 `map-es.json`
  全仓检索均无（检索时该目录仅有 `.probe-stick8`、`build-ko-stick8-run1.log`、
  `ko-sha-stick8-pre.txt`）。因此 221 键无法按 map 逐键核对，改用 §5 的全量文本差分核实；
  全部机械门均为本人独立重跑，不依赖缺失文件。详见 PROOF-NOTE 观察项 O1。

## 8. 待修复后重校的提醒

- D1 修复（6 条 P8 注文罗马字）后须整期重渲染并从头再做一轮全量校对（SOP §8.4）；
  本轮结论为 (b) 缺陷清单，不作定稿决定。
