# GATE-LOG — 2026-W47 ja-es 第二轮独立校对（叶子）

校对员：叶子。工作目录 `~/workspace/weekly-git`。本人笔记目录：
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ja-es2/`
（PROOF-NOTE.md、GATE-LOG.md、`view/`、`text/`、`svg-sha-original.txt`、
`svg-sha-rebuild.txt`、`rebuild-run.log`、`es2-occlusion.json`、`es2-p8.json`、
`es2-p8-core.json`、`es2-p8compare.json`）。
注：写笔记时遇磁盘配额（EDQUOT，df 仍有 45G 空闲）——已删本人 scratch
内可复现的渲染中间件（100dpi render-print/render-web、rebuild/ 副本，
证据保留在日志与 SHA 清单中，PNG 随时可由 PDF 重渲），未碰他人目录。

## 0. 开工硬门禁（双通才动手）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin`
  → `da0c4eb8d9a48d171a33574b380752e183286751`，RC=0。
- `hidden_files/w47/scratch-proof-ja-es2/probe.txt` 真实写入成功。
- 红线遵守：未碰 core-ja、W43–W46、其他目标语家庭、tools/；未跑 insert.py、
  未跑 lint --write，未 git add/commit/push/reset/stash，未改任何成品。
  构建重跑在本人 scratch 副本 `scratch-proof-ja-es2/rebuild/` 内进行；
  原构建目录 8 个 SVG 在校对开始与结束时 `sha256sum -c` 逐一 OK，未变。

## 1. 身份核对

```
print Lucerna-VOL4-JA-ES.pdf      29,102,102 bytes
  sha256 9947b70c00a378c912ad7cffd198fd19a234ca3d6a3598589f647c3eaff0fce7 (8 pages)
web   Lucerna-VOL4-JA-ES-web.pdf   4,482,721 bytes
  sha256 49665374de81dd2a2ee7dad1b91396b22b69b2e64f5a038d55f03b5246a99550 (8 pages)
```
与 KIT §8 fix-1 登记一致（字节数与完整 SHA 逐字一致）。text.md 46,684 字节，
sha256 `81993361c31fad6ea4c9bf8fbc91aed068979d6a8542a756a9fa4063519168e6`，
与 FIX-LOG §6 登记一致。

## 2. 机械门（全部自跑）

### 2.1 冻结重跑（freeze）
- 做法：完整复制构建目录（*.py、*.md、ABSTRACT.txt、assets/）至
  `scratch-proof-ja-es2/rebuild/`，排除 svg/、cards/、PDF、__pycache__；
  用 KIT §9 指定的解释器 `tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0）跑 `run.py`。
- 结果：exit 0；`FLOW OVERFLOW` / `HEAD TOO WIDE` grep 计 0；
  8/8 SVG 与原构建逐字节相同（`diff svg-sha-original.txt svg-sha-rebuild.txt` 空）：
  p1 `7dd43e66…`、p2 `0ef2001d…`、p3 `8afb24cc…`、p4 `b26e6867…`、
  p5 `7170970d…`、p6 `c4c405b4…`、p7 `d00608f9…`、p8 `25b95108…`（完整串见文件）。
  其中 p1–p7 与第一轮记录的 hash 逐一相同，仅 p8 由改前的 `cb2813a7…` 变为
  `25b95108…`，与 fix1 称的“仅 p8-tesuto.svg 变化”一致。
- 重跑 registry（`rebuild-run.log` 尾部）：TOTAL 150；by level A2 48 / B1 73 / B2 29；
  by page {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；
  by type {completa:50, opción múltiple:51, relacionar:12, construye una frase:8,
  verdadero o falso:11, cloze:13, Traduce:4, Redacción:1}；model chars: 154。
  P8-keys flow 终点 col 3 y=2397（底 2540）；P7 teaser 末行 2557.1（页脚 2580）。

### 2.2 几何遮挡审计
- `tools/venv/bin/python tools/occlusion_audit.py --selftest`
  → `selftest OK: planted classes fired {'BOXTITLE':1,'COVER':1,'EDGE':1,'FOOTER':1,
  'LINEX':1,'TEXTX':1}; clean controls silent`。
- `tools/venv/bin/python tools/occlusion_audit.py <es svg dir> --json es2-occlusion.json`
  → `0 flags`，RC=0。

### 2.3 P8 提取与比对
- `tools/p8.py extract --p8 <es p8 svg> --total 150 --json es2-p8.json`
  → `noted set = 150 of 150 (parse: lines)`，RC=0。
- `tools/p8.py compare --core-p8 <core-ja p8 svg> --edition-p8 <es p8 svg> --total 150
  --json es2-p8compare.json`
  → `core 150 noted; edition 150 noted; status: CLEAN; missing=[]; extra_count=0;
  uncertain=[]; keydiff=[137, 138, 139, 140]`，RC=0。
- 另对核心 P8 跑 extract（`es2-p8-core.json`）取键值逐一比对：150 键中仅 137–140 不同，
  其余 146 个键值逐字相同。137–140 的 es 值逐条对题面核实为正确西班牙文翻译
  （见 PROOF-NOTE §2.2）。
- 注意：p8.py 的 keys 只存键值（字母/数字），不存注文散文——D1 的罗马字错误不在其比对范围。

### 2.4 print/web 文字层一致
- `pdftotext -layout` 两版各 102,065 字节，`cmp` 通过：`PRINT_WEB_TEXT_IDENTICAL`
  （与第一轮的 102,065 B 一致）。
- plain `pdftotext` 两版各 47,036 字节，`cmp` 通过（与 EDITION-RECORD 登记的 47,036 B 一致）。
- web PDF 4,482,721 字节 < 7 MB。

### 2.5 U+2019
- 8 个 SVG 中 U+2019 计数：p1–p8 全部 0（总计 0）。
- text.md 0；content*.py 合计 0。8 版渲染图目视：无宽字形断裂。

### 2.6 P8 字号（PyMuPDF 测印刷 PDF 第 8 页）
- 尺寸分布（pt: span 数）：9.98:164、10.35:79、10.88:6、11.25:5、11.62:1、12.75:5、
  13.5:2、14.25:37、14.62:12、15.38:3、15.75:16、17.25:4、18.0:39、18.75:2、34.5:3。
- 最小 9.98pt（≥9.75pt 门槛）；次档 10.35pt = 题干（与 KIT 的 9.975pt/10.35pt 一致，
  9.98 为四舍五入）。

### 2.7 §1.1 grep 审计（8 个 SVG）
- `·` 0×；纸色 `#fbfaf6` 合计 8（每页 1×）；旧 `#f7f1e2` 0×；
  刊头 `font-size="196"`、UnifrakturMaguntia 各 1×（P1）；
  页码行 `Página N de 8` 每页 1×；页脚 `SEMANARIO JAPONÉS VOL.4　Texto en japonés　Explicaciones en español` 每页 1×。
- VOL：VOL.4 各页均有；VOL.3 仅 P4 前号注 1 处；VOL.5 仅 P4 次号预告 1 处 + P7 3 处
  （读者园地披露 2 处、预告条 1 处），均已核对上下文为冻结正文/预告。
- `Foto:` 图注 5 处（P1 Poliphilo、P3 Alainauzas、P5 lumoplank、P7 Mozzucu、P8 lumoplank），
  均为西班牙文 `Foto:` + CC0/公有领域出处。

## 3. D1 回归专项（强证据）

- 改前基准：`hidden_files/w47/scratch-proof-ja-es1/rebuild/svg/p8-tesuto.svg`
  （第一轮复校员留下的改前副本，hash cb2813a7…）。
- 新旧 P8 文本节点 diff：329 个节点中**仅 6 个不同**，恰为 keys 48/49/54/63/111/116
  的罗马字修正（`Umi-no-umi`→`Chura-no-umi` 1 处，`Fujiryūga`→`Fujiryōga` 5 处）。
- P1–P7 文本节点与改前副本**逐字相同**。
- 读音独立核实：デイリー 2026-10-27「美ノ海義久（ちゅらのうみ・よしひさ）」；
  スポーツ報知 2026-11-11「藤凌駕 雅治（ふじりょうが・まさはる）」；sumo-guide.com 同。
- 内容文件错拼排查：py + SVG 文本节点 + text.md + ABSTRACT.txt 中
  `Fujiryūga` / `Umi-no-umi` 均为 0；正确拼写 `Fujiryōga` 5×、`Chura-no-umi` 1×。
  仅 WEEKLY-KIT.md §11 F4（4 行）与 EDITION-RECORD.md Fix-1 节（1 行）含旧拼写，
  全部为修复记录引用的“改前值”（见 PROOF-NOTE O1）。
- P8 答案区高清裁图（`view/p8-answers-left.png`、`view/p8-answers-right.png`，
  100dpi 渲染裁切）：6 处修正行在印刷成品上清晰可读，无溢出、无重叠。

## 4. 逐题与分级核对（SVG 文本节点 + text.md）

- 徽章文本节点计数：P1 A2 11/B1 2/B2 1（其中 4 个为目录栏级别标注；
  练习徽章 A2 10）；P2 A2 15；P3 A2 7/B1 8；P4 B1 18；P5 B1 18；P6 B2 18；
  P7 A2 4/B1 4/B2 4；P8 A2 9/B1 22/B2 4（徽章 rect 共 141 个）。
- 按文档顺序逐题配对徽章：P1 10（A2 10）、P2 18（A2 18）、P3 18（A2 7/B1 11）、
  P4 18（B1 18）、P5 18（B1 18）、P6 18（B2 18）、P7 12（A2 4/B1 4/B2 4）、
  P8 38（A2 9/B1 22/B2 7）；合计 A2 48 / B1 73 / B2 29、总数 150。
  配对题组级别：25–28 全 A2、43–46 全 B1、141–144 全 B2。
- text.md：1377 行、非空 1359 行；KIT“1349 text lines”= 非空行减标题、Week 行与
  8 个 `## Page N` 标记行（1359−10=1349），已自洽；与第一轮的 1376 行差 1 行为重导
  多出的文末空行（见 PROOF-NOTE O9）。
- text.md 与 SVG 文本节点逐行比对：1349 个 SVG 文本节点全在 text.md 中；仅文件头
  `Week: 2026-W47 (16–22 Nov 2026)` 1 行不在 SVG 中。
- 范文实数：H 节范文去空白后 154 字，与宣称一致。

## 5. 金句与事实核对

- 金句 8 条：日语句与核心版逐字相同；逐句在正文原页真实出现，
  页码引用 1/1/2/3/4/7/1/2 全对（第 6 处在 P7 语言专栏本身）。
- 星期核验（`date -d`，America/Toronto）：2026-11-07 六、2026-11-16 一、2026-11-19 四、
  2026-11-22 日、2026-11-23 一、2026-12-01 二、2026-11-05 四；11 月第 3 木曜日 = 19 日。
- P6 图表：38+24+22+16=100；38−24=14；38+24=62；柱长比例与数值一致，标注为练习数据。
- 相扑事实与正文一致：初日 大の里●/豊昇龍○/霧島○/琴櫻●/安青錦●（大関 3 人中 2 人败）；
  3 日目 豊昇龍●/大の里○/藤凌駕金星；藤凌駕初土俵 11 场所目金星。

## 6. 翻译层差分核对（核心 ja-zh-cn vs 本版 ja-es，SVG 文本节点全量）

- 核心独有节点：P1 21、P2 28、P3 24、P4 17、P5 25、P6 22、P7 46、P8 175；
  其中非 CJK 节点仅 P3 的 1 个 `Commons）`（图注中文行尾折行残片），对应 es 版
  `Foto: Alainauzas — dominio público (Wikimedia Commons)` 已完整改写，无丢失。
  无一条纯日文核心句丢失。
- es 独有节点：P1 21、P2 30、P3 26、P4 19、P5 26、P6 23、P7 51、P8 182；
  其中含 CJK 且无假名的节点逐一核查均为日文单词头/冻结小节头配西班牙文 gloss，
  无中文解释句。
- 中文残留词扫描（es 全 SVG 文本节点）：吉伊卡哇 0、参考答案 0、酉之市 0、提名 0、
  译注 0、`｜` 0、练习/阅读/翻译/注释/说明/词汇/语法/发音/例句/问题/选择/填空/意思/中文 0；
  `理解` P2–P6 各 1×，均为冻结日语小节头 `A　理解`。
- Chiikawa：P7 词表 `ちいかわ Chiikawa`、P8 答案 67/106/128；ryuuryuu：P7 gloss、
  P8 答案 66/77/80/105；`吉伊卡哇` 全版 0×。
- `((pág.` 0×；P7 金句引用均为单括号 `(pág. N)`。

## 7. 目视记录（自渲染，非 builder 的图）

- 渲染：`pdftoppm -png -r 100` 自印刷 PDF 得 p-1.png … p-8.png；
  自网页 PDF 得 p1-1.png、p8-8.png；另有 72dpi 浏览版存于 `view/`。
  逐页目视：P1–P8 均无溢出、无重叠、无压页脚；网页 P1/P8 与印刷版视觉一致。
- P7 预告条末行 y≈2557（页脚 2580）；P2/P3/P5 中栏 Nota 框下留白与核心版同一版式。
- D1 的 6 条修正注文在 P8 渲染图上均清晰可见（48/49/54/63/111/116）。
- 注：100dpi 渲染与 rebuild/ 副本已因磁盘配额清理（可由 PDF/源码随时重渲），
  72dpi 浏览版与全部日志/JSON/SHA 清单保留在 `view/` 与本目录。
