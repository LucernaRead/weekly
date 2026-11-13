# GATE-LOG — 2026-W47 en-zh-tw proof2（独立复校，2026-11-11）

复校员：proof2（独立）。对象 `production/2026-w47/2026-w47-en-zh-tw/`（Q73 delta 后现状）。
探针：`git hash-object -w --stdin` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`；scratch 真实写文件成功。
`TMPDIR=<scratch>/tmp` 全程；未写 /tmp。未改生产文件、未重建、未 commit、未 push。
结论：(a) 零缺陷，可定稿。

## 0. 对象 SHA（实测，复校前后两次一致）

| 文件 | 字节 | SHA-256（实测） | 任务书先验 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-zh-tw.pdf` | 38,152,349 | `854d0943264c0821842da52d75585a5eeaaf537b371e0148d22bfab7a1853468` | 一致 |
| `The-Lucerna-VOL4-en-zh-tw.web.pdf` | 2,965,206 | `e6e9f8596f14d431c7805b0ad630c91669317b2a99f3d4557ac08903526a41bb` | 一致 |
| `2026-w47-en-zh-tw.text.md` | 51,144 | `cf12ebfe88d7804ccef05d2fb62d8e94dc68ed081a20577cb8adac2ae6386e2b` | 一致 |
| `ABSTRACT.txt` | 498 | `47750881038ea49c33d1a562346d13a23bb0b058f6e487e3dd35a985ecc80f16` | 一致（未动） |
| `registry.json` | — | `ee44f57db25c51848ec30e1912731437b1ffb2a1046ddc87ed245e9bc5e3df3c` | 与 delta 后记录一致 |

两 PDF 各 8 页，1462.5 × 2025 pt。复校结束时四件 SHA 再次复核，无变化。

## 1. 机械门（实跑）

### 1.1 occlusion 审计（正式，无 --selftest）
```
tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-en-zh-tw --json <scratch>/occlusion.json
→ selftest OK: planted classes fired {BOXTITLE: 1, COVER: 1, EDGE: 1, FOOTER: 1, LINEX: 1, TEXTX: 1}; clean controls silent
→ production/2026-w47/2026-w47-en-zh-tw/svg: 0 flags
```
注：首行的 selftest 输出是该工具每次正式运行自带的内部检测器自检（delta 报告亦有说明），
审计本身未加 --selftest。盲区如 proof1：BOXTITLE 只查有描边/填色框、盒内末行漫出不在类目内，
本次由 creambox 实测 + 框题真墨 + 目视补上。

### 1.2 p8 extract + compare（门 3）
```
tools/p8.py extract --p8 .../svg/p8-test.svg --total 150
→ noted set = 60 of 150 (parse: joined)
  set: [3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82, 83, 84, 85, 86, 87, 89, 108, 109, 110, 111,
        112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
        130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
tools/p8.py compare --core-p8 core-en/svg/p8-test.svg --edition-p8 .../svg/p8-test.svg --total 150
→ core 60 noted / edition 60 noted / status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]
```
keydiff 恰为预期 [137, 138, 139, 150]（翻译题 + 開放題）；Q140 `打破沉默。` 核心与本版完全相同，
故不列入。extract 的 P8 键含 `39. a · 40. d · 73. up`。

### 1.3 keycheck（门 4，自写 `keycheck.py`）
- registry 150 条；core registry 150 条；P8 extract 键 150/150，无缺号。
- registry vs P8 extract：**149/150**，唯一不符为 Q150（registry 全写
  `開放題 — 要點見寫作框，範文在第 8 版寫作框內`，P8 extract 只取首段 `開放題`，预期内截断）。
- registry vs core：**146/150**，diff 仅 {137, 138, 139, 150}（读者语键：繁/简字形与開放題措辞）；
  Q73 已与核心一致（`up`）。
- registry vs text.md 答案行：**150/150** 逐行正则核对，0 不符（`text.md` 答案行格式
  `n. [LEVEL] 类型 — key (note)`）。
- Q73：registry `up` / P8 extract `up` / core `up`，note 仅简繁字形差
  （本版 `大聲說出來` vs 核心 `大声说出来`）。

### 1.4 freeze（门 5）
```
tools/freeze.py baseline --build production/2026-w47/core-en --core-svg production/2026-w47/core-en/svg --out <scratch>/freeze-core
→ baseline: 8/8 SVGs byte-identical
  p1 a9a8deaf… / p2 97974716… / p3 efb83ce7… / p4 aa6f395e… / p5 a6a515cd… / p6 76922564… / p7 da908af6… / p8 1066c475…
  core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
```
基线确为 core-en 的 SVG：核心哈希（a9a8deaf…等）与本版 shipped SVG 哈希（eadcdb16…等）逐页不同，
且运行前后 core SVG 的 sha256sum 全部 OK。版内补充基线
（`--build` = 本版目录、`--core-svg` = 本版 svg/）亦 8/8（仅作补充证据，不冒充标准口径），
本版 shipped SVG 运行前后亦全部 OK。
```
tools/freeze.py diff --core-svg core-en/svg --edition-svg .../svg
→ p1 +23/-23（CJK 202→231，新增 98）/ p2 +32/-32（278→283，新增 109）/ p3 +17/-17（146→154，新增 52）
  / p4 +16/-16（143→151，新增 50）/ p5 +16/-15（132→140，新增 45）/ p6 +14/-14（159→161，新增 56）
  / p7 +40/-40（429→422，新增 142）/ p8 +81/-89（634→542，新增 224）
→ TOTAL added CJK characters: 775
```
与 delta 记录一致（p8 +81/-89 为 delta 后的值；其余各页与 delta 前相同）。

### 1.5 creambox 全版扫描（门 6，canonical `hidden_files/w47/tools/creambox.py`，8 个 SVG）
- 32 盒；inside-only 末基线余量最小 +4.5 px（P2 AND YOU? 盒，末行中文、无降部）；
  其余 +12.0 至 +92.4 px；P7-TOOLBOX 汇总：7 盒，min inside +47.7，min desc-clear +41.6。
- +45 px 窗口内全部 BELOW-WINDOW 行均为 +24 至 +37 px 的下块栏头（TRY IT NOW、THE WORD OF THE WEEK、
  WHAT IS ON THIS WEEK?、A COMPREHENSION、READ THE CHART、READERS' CORNER 等），无 +12..+18 px 整行漫出。
- D2/D3 复核（见 §1.6）：SEARCHES 盒末行基线 1244.0（余 +12.0）、DID YOU KNOW 盒末行基线 1171.1
  （盒底已改为 1185.4，余 +14.3），均已在盒内。
- AND YOU? 盒 desc-clear −1.5 px 为 0.30×字号降部估算，末行 `。` 无降部；真墨底余 +3.9 px（§1.6），框内。

### 1.6 框题 advance + 真墨实测（自写 `measure2.py`；真墨取 shipped `cards/*.png`，1950×2700 = SVG 单位 1:1；
###      扫描窗横向封顶于框右缘+10 px，排除邻栏墨迹——v1 未封顶曾误报 P1 NUMBERS 等 4 处邻栏假阳性，已修正重测）
| 框题 | advance 止点 / 框右缘 | advance 余量 | 真墨 | 真墨余量 |
|---|---|---|---|---|
| P1 THE WEEK IN NUMBERS　數字看本週 | 1410.0 / 1412 | +1.5 | 1008..1407 | **+4.5** |
| P1 SEARCHES | 1602.3 / 1862 | +259.7 | 1464..1600 | +262.0 |
| P1 IN THIS ISSUE　本期目錄 | 1744.5 / 1862 | +117.5 | 1464..1742 | +120.0 |
| P1 IN BRIEF　快訊 | 1634.3 / 1862 | +227.7 | 1464..1632 | +230.0 |
| P2 SENATE IN NUMBERS　參議院數字（已缩短，D6） | 930.5 / 961 | +30.5 | 558..929 | **+32.0** |
| P2 THE CALENDAR　本週日曆 | 1294.2 / 1412 | +117.3 | 1008..1291 | +120.5 |
| P2 gloss 首行 | 1375.8 / 1412 | +35.7 | 1009..1382 | +29.5 |
| P2 DID YOU KNOW? | 1651.7 / 1862 | +210.3 | 1464..1647 | +215.0 |
| P2 AND YOU?　說說你自己 | 1723.7 / 1862 | +138.3 | 1462..1720 | +142.0 |
| P3 COMING SOON　即將上映 | 836.6 / 961 | +124.4 | 558..835 | +126.0 |
| P3 gloss 首行 | 904.7 / 961 | +56.3 | 558..910 | +51.0 |
| P3 HAYMITCH'S GAMES　海米奇的比賽 | 1842.9 / 1862 | +19.1 | 1460..1840 | +22.0 |
| P4 WHY PERTH?　為什麼去珀斯？ | 885.9 / 961 | +75.1 | 557..878 | +83.0 |
| P4 gloss 首行 | 923.3 / 961 | +37.7 | 558..931 | +30.0 |
| P4 SATURDAY, NOV 21　週六賽程（已缩短，D8） | 1782.1 / 1862 | +79.9 | 1459..1784 | **+78.0** |
| P5 ODD SOCKS, IN NUMBERS　奇襪日 | 486.9 / 510 | +23.6 | 108..481 | +29.5 |
| P5 gloss 首行 | 937.8 / 961 | +23.2 | 559..943 | +18.0 |
| P5 SPEAK UP　大聲說出來 | 1707.6 / 1862 | +154.4 | 1459..1704 | +158.0 |
| P6 A PRACTICE BALLOT　模擬選票 | 895.4 / 961 | +65.6 | 557..895 | +66.0 |
| P6 gloss 首行 | 889.0 / 961 | +72.0 | 559..895 | +66.0 |
| P6 HOW LONG?　任期多長？ | 1732.5 / 1862 | +129.5 | 1460..1726 | +136.0 |
| P7 gloss（win/won、comparative、will、past simple、headline、whether） | — | +18.3 ~ +50.2 | — | +13.0 ~ +45.5 |
| P7 THE TOOLBOX　句型工具箱 | 1756.1 / 1862 | +105.9 | 1459..1754 | +108.0 |
| P8 MODEL　範文 | 1161.2 / 1862 | +700.8 | 1013..1159 | +703.0 |

全部框题 advance 与真墨均合框，无溢出。

### 1.7 P2 SAY IT 横向实测（D7 复核）
| 盒 | 英文行 span / 盒 | 中文行 span / 盒 |
|---|---|---|
| 盒 1 x=159–439 | The counting continues. 181.0..417.1，ink 182..418 ✓ | 計票還在繼續。229..369 ✓ |
| 盒 2 x=560–940（已加宽至 380） | The new Congress meets in January. 574.0..926.1，左余 +14.0、右余 +13.9，ink 575..930 ✓ | 新國會在一月開會。660..840 ✓ |
| 盒 3 x=1060–1340 | Happy Thanksgiving! 1094.9..1305.1 ✓ | 感恩節快樂！1140..1260 ✓ |

### 1.8 印/网文字层逐页比对（门 7，PyMuPDF token-multiset，只读；未重渲染 web PDF）
| 页 | print tokens | web tokens | multiset diff | 字符数 print/web | 文本逐字节相同 |
|---|---|---|---|---|---|
| p1 | 788 | 788 | 0 | 4232 / 4232 | 是 |
| p2 | 976 | 976 | 0 | 5206 / 5206 | 是 |
| p3 | 899 | 899 | 0 | 4852 / 4852 | 是 |
| p4 | 979 | 979 | 0 | 5313 / 5313 | 是 |
| p5 | 779 | 779 | 0 | 4271 / 4271 | 是 |
| p6 | 956 | 956 | 0 | 5122 / 5122 | 是 |
| p7 | 870 | 870 | 0 | 4887 / 4887 | 是 |
| p8 | 1602 | 1602 | 0 | 7898 / 7898 | 是 |

TOTAL multiset diff 0。web P1/P8 另渲染于 scratch 目视，与印版一致。

### 1.9 check_s11.py zh-tw / verify_ed.py zh-tw（门 8）
```
check_s11.py zh-tw → rc=0
  colour set: core 19 edition 19 extra: none missing: none
  badge colour A2 #5c6e30 / B1 #46581f / B2 #37402f present: True
  P8 min font-size: 13.5 (SVG 属性值)
  P8 Q113-120 options line with [A2] tag present; 'Levels: 145-149 [A2]' present
  P8 Q120 [A2] chip OK; P8 WRITING head present
  ALL §1.1/P8 CHECKS PASS
verify_ed.py zh-tw → rc=0, VERIFY ALL PASS
  Q39 key a / Q40 key d / Q39 note mentor=a / Q40 note arena=d / Q46 key A / Q46 note 2025
  Q52 hosted / Q55 won / Q125 key A / Q125 note 4-1 / registry notes: no stale Ashes phrasing
  text.md has 150 answers / text.md Q39 a / Q40 d / Q125 A / 'Arsenal are winning'
  text.md: no 'Perth is winning' / no 'second week in Perth' / Ashes retrospective present / no 'Ashes begin'
  P8 min PDF font >= 9.75pt — min 10.12pt
```
注：两个脚本不在 repo tools/ 内，取自 `scratch-fanout-en2`（md5 校验复制一致），
以副本形式存于本 scratch（`check_s11.py`、`verify_ed.py`），未动原文件。

### 1.10 P8 最小字号（独立实测，PyMuPDF，印版 PDF 全页 spans）
- P1–P7 min 均为 11.62 pt；**P8 min 10.12 pt**（269 spans）≥ §1.1 下限 9.75 pt，通过。
  与 verify_ed.py 的 10.12 pt 一致；check_s11 的 13.5 为 SVG 属性值口径，非渲染 pt。

### 1.11 简繁脚本门（门 8，OpenCC s2t，venv）
- registry.json：0 差异；2026-w47-en-zh-tw.text.md：0 差异；ABSTRACT.txt：0 差异；
  8 个 SVG：各 0 差异。**TOTAL 0**。交付物中零简体字（读者语繁体中文为正常正文）。

### 1.12 D5 字体（门 9，只记录不判定）
- print/web 各 43 个字体对象，全部 embedded+subset；两份 `pdffonts` 列表仅 subset 前缀不同。
- `NotoSansCJKtc` 16 项；`NotoSansCJKsc` 0 项（print/web 均为 0）。

## 2. 150 题逐题语义核对（门 2）

- 方法：stub 执行 content12/34/56/7/8 抽取全部 150 对（n/level/type/key/note/body/opts），
  keys+types 与 registry **150/150 MATCH**（`extract_pairs.py` + `exercises.json` + `pairs.txt`）。
- 附注：首次运行该脚本时未注意其第 244 行硬编码写路径指向 delta scratch 的
  `gates/exercises.json`，复写了该文件；随后核对：该文件内容为同一来源的确定性抽取
  （150 对、Q73 为 up），与 delta 原内容一致，未改生产文件（四件 SHA 事后复核无变化）；
  已用 sed 将写路径改到本 scratch 后重跑，`exercises.json` 现存于本 scratch。
- 手核结果：填空/改写/翻译/完形/对话/纠错 78 项逐项读 stem、key 全部成句适配（含 Q73）；
  51 项 MCQ 每键均在选项内且与正文/图表/算术一致；20 项配对按印版释义顺序逐组手验全对
  （P2 D 24–27、P3 C 38–41、P4 C 56–59、P5 C 74–77、P8 F 141–144）；
  完形 112–119 与 P8 短文逐字核对（Tuesday / call / continues / will meet / writes /
  will certify / wears / will watch）；对话 145–149 与 P8 对话逐字核对
  （row / film / popcorn / show / Friday）；翻译 137–140 繁体译文准确；Q150 開放題。
- 3 组重复题干（Q2/Q95、Q5/Q96、Q6/Q12）为 P6 复习回访，键均适配，核心既有设计，非缺陷。

## 3. 目视检查（门 1）

- 印版 8 页总览（`render/print-p1.png` … `render/print-p8.png`，PyMuPDF 100 dpi）逐页目视：
  版式干净，无溢出、重叠、压页脚、行首孤标点；图片与出处齐全。
- P1：SEARCHES 盒末行在盒内；NUMBERS 框题合框；IN BRIEF Ashes 已为 2025–26 回顾。
- P2：SENATE 标题已缩短合框；DID YOU KNOW 末行 `November 3.` 在盒内；SAY IT 三盒英文行均合框；
  AND YOU? 盒末行在盒内；火鸡图注完整。
- P3：C 组 38–41 题面与释义顺序可视；Rousseau 图注 `"Surprised!" (1891)` 完整。
- P4：Ashes 回顾全文；SATURDAY, NOV 21 框题合框；W. G. Grace 图注完整。
- P5：Q73 `Speak ___: tell a teacher.` + gloss `to speak up = 大聲說出來` 在位；
  ODD SOCKS 框题合框；THE JUNGLE, TOO 无“Ashes 周六开打”表述。
- P6：图表数字与正文一致；认证表述为条件式；投票亭图注完整。
- P7：金句 8 句；NEXT WEEK 已改写；TOOLBOX 盒干净；READERS' CORNER 与示例信完整。
- P8：ANSWERS 块 `38. b · 39. a · 40. d · 41. c` 与 `73. up · 74. d · 75. a · 76. b · 77. c` 可视；
  MODEL 82 词；H WRITING 与图片完整。
- 网版 `render/web-p1.png`、`render/web-p8.png` 与印版视觉一致。

## 4. 产物清单（本 scratch）

- `PROOF-NOTE.md`、`GATE-LOG.md`
- `keycheck.py`/`keycheck.log`、`measure.py`/`measure.log`、`measure2.py`/`measure2.log`
  （measure.py 为 v1，含邻栏墨迹误报 4 处，已废弃，见 §1.6 注；measure2.py 为修正版）
- `exercises.json`、`pairs.txt`、`extract_pairs.py`/`extract_pairs.log`
  （`extract_exercises.py` 为 delta 脚本的同批复制，未使用）
- `check_s11.py`/`check_s11.log`、`verify_ed.py`/`verify_ed.log`
- `occlusion.log`、`occlusion.json`、`p8-extract.log`、`p8-extract.json`、
  `p8-compare.log`、`p8-compare.json`
- `freeze-core.log`、`freeze-core/`、`freeze-ed.log`、`freeze-ed/`、
  `freeze-diff.log`、`freeze-diff.json`、`core-svg-before.sha`、`ed-svg-before.sha`
- `creambox.log`、`s2t.log`、`p8-minfont.log`、`pdffonts-print.txt`、`pdffonts-web.txt`
- `render/print-p1.png` … `render/print-p8.png`、`render/web-p1.png`、`render/web-p8.png`
- `tmp/probe.txt`（TMPDIR 探针）
