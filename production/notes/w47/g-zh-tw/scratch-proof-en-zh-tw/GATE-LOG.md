# GATE-LOG — 2026-W47 en-zh-tw proof1（en re-fanout #2 重建版，独立复校，2026-11-11）

复校员：proof1（重建版，独立）。对象 `production/2026-w47/2026-w47-en-zh-tw/`。
探针：`ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；scratch 真实写文件成功。
`TMPDIR=<scratch>/tmp` 全程；未写 /tmp。未改生产文件、未重建生产件、未 commit、未 push。
工具状态注：`git status` 显示 `tools/freeze.py`、`tools/occlusion_audit.py`、`tools/p8.py` 有未提交修改，mtime 均早于本轮开工（freeze.py 2026-11-11 13:07 UTC、occlusion 05:01 UTC、p8.py 2026-11-10 21:37 UTC；本轮开工 09:02 EST = 14:02 UTC），是他人在先的合法改进（freeze.py 运行守卫、p8.py 跨 run 文本合并），非本轮所改；本轮门禁均在现场工具版本下实跑，结果如数记录。

## 0. 对象 SHA（实测，与任务书逐字节一致）

| 文件 | 字节 | SHA-256（实测） |
|---|---|---|
| `The-Lucerna-VOL4-en-zh-tw.pdf` | 38,152,350 | `7641031186c77653ac1263056a968ba7ce2ffb9383716c5a35cfad798e0fc334` |
| `The-Lucerna-VOL4-en-zh-tw.web.pdf` | 2,965,191 | `e07e5dd048dad9ab1ed42daa6d33c2e9f0dea129538b957c06afe25627e0d177` |
| `2026-w47-en-zh-tw.text.md` | 51,147 | `57cb886738e8e23d79abe531e1f03ee7372560c5020ff02d4d6997ea117651b3` |
| `ABSTRACT.txt` | 498 | 206 字符、1 行、无 ASCII 双引号、以换行结尾（见 §5.1） |

两 PDF 各 8 页，1462.5 × 2025 pt。收尾复核 SHA 与开工一致（生产文件未动）。

## 1. 机械门（实跑）

### 1.1 occlusion 审计（正式）
```
tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-en-zh-tw --json <scratch>/occlusion.json
→ selftest OK: planted classes fired {BOXTITLE: 1, COVER: 1, EDGE: 1, FOOTER: 1, LINEX: 1, TEXTX: 1}; clean controls silent
→ production/2026-w47/2026-w47-en-zh-tw/svg: 0 flags
```
盲区记录（与 proof1 同）：审计 BOXTITLE 只查有描边/填色框，不覆盖奶油框题；盒内末行漫出亦不在类目内——本次由 creambox 实测（§1.4/§1.5）+ 目视裁定补上。

### 1.2 p8 extract + compare
```
tools/p8.py extract --p8 .../svg/p8-test.svg --total 150 [--json <scratch>/p8-extract.json]
→ noted set = 60 of 150 (parse: joined)
  set: [3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82, 83, 84, 85, 86, 87, 89, 108, 109, 110, 111, 112, 113,
        114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132,
        133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
tools/p8.py compare --core-p8 core-en/svg/p8-test.svg --edition-p8 .../svg/p8-test.svg --total 150
→ core 60 noted / edition 60 noted / status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]
```
keydiff 说明：137–139 为翻译题（简繁字形不同）、150 为開放題，预期内；**140 不在 keydiff 内**——registry 键 core 与本版逐字相同（“打破沉默。”，简繁同形），故不列入。compare 对键错是盲的——Q39/40 的核对见 §1.7/§1.13（四源手验）。

### 1.3 freeze（8/8 + diff）
```
tools/freeze.py baseline --build .../2026-w47-en-zh-tw --core-svg .../2026-w47-en-zh-tw/svg --out <scratch>/freeze-final
→ baseline: 8/8 SVGs byte-identical (repointed files: none)
  p1 eadcdb16… / p2 3505d378… / p3 f516d68b… / p4 1e1a1bee… / p5 c9985432… / p6 149586d8… / p7 7aa58e08… / p8 a7b6345d…
  core integrity: shipped SVGs unchanged by the run (8 files re-hashed)
```
过程注：首次误把 `--core-svg` 指到 core-en/svg，跑出 0/8——那是参数错误（把版面重建结果拿去对核心 SVG，当然不等），不是版面缺陷；按 proof1 同款正确参数（`--core-svg` 指本版 svg，即“重跑建版能否复现交付 SVG”）重跑即 8/8。误跑日志未覆盖，见 `freeze.log` 终版。
```
tools/freeze.py diff --core-svg core-en/svg --edition-svg .../svg [--json <scratch>/freeze-diff.json]
→ p1 +23/-23（CJK 202→231，新增 98）/ p2 +32/-32（278→283，新增 109）/ p3 +17/-17（146→154，新增 52）
  / p4 +16/-16（143→151，新增 50）/ p5 +16/-15（132→140，新增 45）/ p6 +14/-14（159→161，新增 55）
  / p7 +40/-40（429→422，新增 142）/ p8 +82/-90（634→542，新增 224）
→ TOTAL added CJK characters: 775（与 KIT §5 一致）
```
`--strict-cjk` 附加跑 rc=1，预期内：core-en 的读者层是简体中文（见 diff removed_strings 中的“民主党赢下两院”“快讯”等简体句），繁体 fan-out 的 775 字新增是 s2t 层转换本身，不是违规。逐字核查：775 字共 180 个不同字，OpenCC s2t 自恒**全部**（`non-s2t-identity: {}`），即繁体合法新增，全数追踪，无一简体字混入。P5 +16/-15 不对称说明：P5 gloss 行 “silence = 沉默”在两版断行位置不同（本版断成 “沉”+“默”两行），属断行 artifact，非内容差。P8 +82/-90 为简繁字形 + 家具（“翻譯：”vs“Translate:”）差异。

### 1.4 creambox 全版扫描（32 盒；`measure.py` + `measure2.py`）
方法：每盒取盒内末基线（真 clearance）+ 盒底上 45 px 带内逐行裁定（x0≈盒内 inset 且字号为正文/gloss 号者为盒内行；x0=栏 x 且 22–25pt 者为下块栏头）。

| 页 | 盒 | 盒内末基线 clearance | 带内行裁定 |
|---|---|---|---|
| P1 | NUMBERS y=786 | +45.7 | TRY IT NOW（栏头，FP） |
| P1 | SEARCHES y=588 | **+12.0（D2 已修：旧 -18.0）** | —（末行“相對熱度示意…”框内，裁图证实） |
| P1 | IN THIS ISSUE y=1280 | +48.0 | THE WORD OF THE WEEK（栏头，FP） |
| P1 | IN BRIEF y=1874 | +44.0 | — |
| P2 | SENATE y=526 | +48.1 | Life goes on…（栏头，FP） |
| P2 | CALENDAR y=200 | +48.1 | WHAT IS ON THIS WEEK?（栏头，FP） |
| P2 | gloss y=1400 | +47.7 | — |
| P2 | DID YOU KNOW y=833 | **+14.3（D3 已修：旧 -12.7）** | —（末行“November 3.”框内，裁图证实） |
| P2 | AND YOU? y=1211 | **+4.5**（最紧，末行中文、无降部，框内，裁图证实） | — |
| P2 | SAY IT ×3 y=1636 | +30.0 ×3 | —（横向见 §1.5） |
| P3 | COMING SOON y=200 | +48.1 | A film is not only…（栏头，FP） |
| P3 | gloss y=1224 | +47.7 | A COMPREHENSION（栏头，FP） |
| P3 | HAYMITCH'S y=856 | +48.5 | FIVE SENTENCES（栏头，FP） |
| P4 | WHY PERTH? y=489 | +48.1 | How do you follow…（栏头，FP） |
| P4 | gloss y=1435 | +47.7 | A COMPREHENSION（栏头，FP） |
| P4 | SATURDAY y=856 | +48.5 | ONE SCREEN, TWO SCREENS（栏头，FP） |
| P5 | （左下）y=2034 | +48.1 | If you want to practise（栏头，FP） |
| P5 | gloss y=200 | +47.7 | A COMPREHENSION（栏头，FP） |
| P5 | SPEAK UP y=852 | +48.5 | FRIDAY'S WORDS（栏头，FP） |
| P6 | BALLOT y=200 | +48.1 | A note on numbers…（栏头，FP） |
| P6 | gloss y=779 | +47.7 | READ THE CHART（栏头，FP） |
| P6 | HOW LONG? y=666 | +48.5 | FIFTY ELECTIONS（栏头，FP） |
| P7 | WORDS win/won y=254 | +47.7 | win = to get first place…（栏头，FP） |
| P7 | WORDS more than y=923 | +47.7 | more than = a bigger…（栏头，FP） |
| P7 | GRAMMAR will y=1599 | +47.7 | The counting will continue…（栏头，FP） |
| P7 | GRAMMAR past y=2062 | +47.7 | Use the past for the past…（栏头，FP） |
| P7 | GRAMMAR headlines y=254 | +47.7 | Newspapers use the present…（栏头，FP） |
| P7 | GRAMMAR whether y=684 | +47.7 | Nobody knows whether…（栏头，FP） |
| P7 | **TOOLBOX y=651** | **+48.5（墨水最低行 961，盒底 1008.2，余 +47.2；B2 句末行降部字母干净，裁图证实）** | READERS' CORNER（栏头，FP） |
| P8 | MODEL y=1720 | +92.4 | — |

**结论：32 盒全部盒内 clearance 为正，无真墨溢出。**（measure.py 的 +45 px 窗口初筛会把栏头标 OVERFLOW，measure2.py 的逐行裁定已全部澄清为 FP，方法与 proof1 同。）

### 1.5 框题 text_w + 真墨实测（全部奶油框题）
| 框题 | advance 止点 / 框右缘 | advance 余量 | 真墨（卡片 PNG） | 真墨余量 |
|---|---|---|---|---|
| P1 THE WEEK IN NUMBERS　數字看本週 | 1410.0 / 1412 | +1.5 | 1007..1407 | **+5.0** |
| P2 SENATE IN NUMBERS　參議院數字 | 930.5 / 961 | **+30.5（D6 已修：旧 −28.1）** | 558..929 | **+32.0** |
| P2 THE CALENDAR　本週日曆 | 1294.2 / 1412 | +117.3 | — | — |
| P3 COMING SOON　即將上映 | 836.6 / 961 | +124.4 | — | — |
| P3 HAYMITCH'S GAMES　海米奇的比賽 | 1842.9 / 1862 | +19.1 | 1459..1841 | +21.0 |
| P4 WHY PERTH?　為什麼去珀斯？ | 885.9 / 961 | +75.1 | — | — |
| P4 SATURDAY, NOV 21　週六賽程 | 1782.1 / 1862 | **+79.9（D8 已修：旧 +0.7）** | 1458..1785 | **+77.0** |
| P5 ODD SOCKS, IN NUMBERS　奇襪日 | 486.9 / 510 | +23.6 | 107..482 | +28.0 |
| P5 SPEAK UP　大聲說出來 | 1707.6 / 1862 | +154.4 | — | — |
| P6 A PRACTICE BALLOT　模擬選票 | 895.4 / 961 | +65.6 | — | — |
| P6 HOW LONG?　任期多長？ | 1732.5 / 1862 | +129.5 | 1459..1726 | +136.0 |
| P7 THE TOOLBOX　句型工具箱 | 1756.1 / 1862 | +105.9 | 1458..1755 | +107.0 |
| P8 MODEL　範文 | 1161.2 / 1862 | +700.8 | — | — |

**结论：全部框题合框，无双语小标题漫出奶油框右缘；STRADDLE 裁定无适用项。**（另有 15 个“译注｜”首行按同法实测，余量 +18.3 至 +72.0，全部合框，见 measure.log PART 2。）

### 1.6 P2 SAY IT 横向实测（D7 已修）
| 盒 | 英文行 span / 盒 | 中文行 span / 盒 |
|---|---|---|
| 盒 1 x=159–439（宽 280） | The counting continues. 181.0..417.1 ✓ | 計票還在繼續。229..369 ✓ |
| 盒 2 x=560–940（**宽 380**，旧 280） | The new Congress meets in January. 574.0..926.1，左右余 **+14.0/+13.9** ✓ | 新國會在一月開會。660..840 ✓ |
| 盒 3 x=1060–1340（宽 280） | Happy Thanksgiving! 1094.9..1305.1 ✓ | 感恩節快樂！1140..1260 ✓ |

注：measure.py PART 3 只筛宽 280 的盒，故第 2 盒未出现在其输出中；已用同法单独实测（盒宽 380），裁图 `render/crop-p2-sayit-box2.png` 目视证实英文行框内。

### 1.7 keycheck（registry vs text.md vs 印版 P8 键）
- registry 150 条；text.md 答案行 150 行（1–150 连续）；逐项核对：**0 不符**。
- 印版 P8 键（`p8.py extract --json`）vs registry：**149/150 exact**，唯一差异 #150 印出“開放題”（键为开放题，后接要点说明，extract 只取首段）——预期例外，与 KIT 一致。
- 印版 P8 键含已修正的 Q39/Q40：`38. b · 39. a · 40. d · 41. c`（extract JSON 实测）。
- registry 键 vs core-en registry 键：差异仅 **[137, 138, 139, 150]**（146/150 相同）；140 不在差异内（简繁同形，逐字相同）。KIT §5 所称“145/150（diff 137–140, 150）”多算了 140，见 PROOF-NOTE O2。
- Q139：印出版键现与 registry 逐字一致（“新國會將於 2027 年 1 月開會。”），proof1 的空格断行差异已无。

### 1.8 印/网文字层逐页比对（PyMuPDF token-multiset）
| 页 | print tokens | web tokens | multiset diff | 字符数 print/web（span） |
|---|---|---|---|---|
| p1 | 788 | 788 | 0 | 3444 / 3444 |
| p2 | 976 | 976 | 0 | 4230 / 4230 |
| p3 | 899 | 899 | 0 | 3953 / 3953 |
| p4 | 979 | 979 | 0 | 4334 / 4334 |
| p5 | 779 | 779 | 0 | 3492 / 3492 |
| p6 | 956 | 956 | 0 | 4166 / 4166 |
| p7 | 870 | 870 | 0 | 4017 / 4017 |
| p8 | 1602 | 1602 | 0 | 6299 / 6299 |

另：pdftotext 全文字符数印/网各 **42,852**（与 KIT 一致；字符数口径：`len(pdftotext stdout)`，字节数则各 47,832——两者印=网）；PyMuPDF `get_text()` 各 41,784 字符，逐页相同。网 PDF 未重渲，仅从交付件本身读取。

### 1.9 P8 最小字号（印版 PDF spans，PyMuPDF）
- P8 min **10.12 pt**（答案键块，0.75 缩放组内）；P1–P7 min 均为 11.62 pt（图注）。≥ 任务书 10 pt 下限（亦 ≥ §1.1 下限 9.75 pt），通过。
- KIT “13.5 pt”是 SVG 属性值（px），非渲染 pt——口径备注，非本版缺陷。

### 1.10 §1.1 字体/配色
- 字体（SVG）：Newsreader 1025、Noto Sans CJK TC 619、Noto Serif CJK TC 48、UnifrakturMaguntia 1（刊头）、DejaVu Sans 4（符号）。合规；无无关字体。
- 用色集合与 core-en **完全一致**（fill/stroke 集合逐项比对，edition-only 与 core-only 均为空）。§1.1 外的色（#4f765d、#84a283、#4d72b4、#7898cd、#d7b257、#edd17f、#f1e8d4、#34483a、#cac8ba、#ffffff）均为图表/地图/搜索条内容色，核心共有。
- 家具分隔符：U+3000 141（核心 132，+9 为繁体家具多用全角空格）；· 282，与核心完全一致；VOL.4 ×12、VOL.5 ×8、VOL.3 ×3，与核心一致。

### 1.11 弯引号 U+201C/U+201D/U+2019 在 CJK 语境计数
- SVG：“ 82 / ” 82 成对；U+2019 **0**。按 font-family 分：全部 82 对均在 Newsreader（拉丁）节点；**CJK 字运行 0**。
- 唯一斜体对：P1 每周一词 “midterm”（Newsreader 斜体，§1.1 本周词斜体）；**P7 无斜体引号**。
- text.md：“ 81 / ” 81，U+2019 0。SVG 多一对是 P3 图注 “Surprised!”（Rousseau 画名，text.md 按惯例跳过图注）。
- text.md 中与 CJK 同行的引号（P7 工具盒三行、P8 E 节四行）渲染时按字形分 run，SVG 里中英分属不同 <text> 节点，无 CJK 节点含弯引号。

### 1.12 简繁脚本门（OpenCC s2t，repo venv Python，`OpenCC('s2t')`）
- registry.json：0 差异；2026-w47-en-zh-tw.text.md：0 差异；8 个 SVG 可见文本：全部 0 差异。
- **ABSTRACT.txt：1 差异 `(38, '布', '佈')`**——“已宣布結果”中的“布”→“佈”。即 **D1**（见 PROOF-NOTE）。
- 直接验证：`宣布 → 宣佈`、`宣佈 → 宣佈`、`布料 → 布料`（OpenCC 不乱改合法的“布”）；本版 text.md/registry 中“布”出现 0 次（除“宣佈”内），故该门对本版无假阳性。

### 1.13 配对题释义顺序（印版 SVG 节点顺序手验）
| 节 | 释义顺序（印版） | 键 | 结论 |
|---|---|---|---|
| P2 D 24–27 | a=the bird of the Thanksgiving dinner, b=a second vote, when nobody wins, c=to confirm a count officially, d=the American family holiday | 24→b, 25→c, 26→a, 27→d | ✓ 全对 |
| P3 C 38–41 | a=a person who teaches and guides you, b=a person chosen to take part in the Games, c=a person who lives with you in the jungle camp, d=the place where the Games are fought | 38→b, **39→a, 40→d**, 41→c | ✓ 全对（D1 已修，四源一致：text.md、P3 SVG、registry、P8 印出键） |
| P4 C 56–59 | a=a pause between parts of a season, b=a five-day cricket match, c=a series of games away from home, d=damage to the body that stops you playing | 56→b, 57→c, 58→d, 59→a | ✓ 全对 |
| P5 C 74–77 | a=saying what you think, loudly and clearly, b=something every child has, by law, c=saying nothing at all, d=hurting or frightening someone again and again | 74→d, 75→a, 76→b, 77→c | ✓ 全对 |
| P8 F 141–144 | a=an election in the middle of a President's term, b=a news organisation's judgement on a race, c=a second vote, when nobody wins, d=to confirm a count officially | 141→b, 142→c, 143→d, 144→a | ✓ 全对 |

注：`measure3.py` 原“Matching definition order”段有 bug（`m.group(2)`，正则只含 1 组），首次运行在该段崩溃（rc=1，前段已完成）；已在本轮 scratch 副本中改 `group(1)` 后重跑（`measure3b.log`，rc=0），repo 工具未动。配对顺序最终以本节的手工 SVG 节点抽取为准（上表逐行原文）。

### 1.14 其余核对
- P7 金句 8/8 逐字出自本期正文（页码标注正确；“A ‘call’…”含嵌套引号，regex 截断但正文逐字核对无误）。
- MODEL 82 词（字母数字 token 计，与 KIT 一致）。
- 可见文本禁词：TODO/占位/SOP/cover/bridge/lorem/FIXME/XXX/TBD/placeholder **0**（SVG 可见文本节点；原始 SVG 源码中的命中均为 base64 图片数据）。
- 旧版表述残留：`Perth is winning!` / `second week in Perth` / `Ashes begin` / `Ashes to Perth` 在 text.md 中 **0**；`Arsenal are winning!` 在 P4（ONE SCREEN, TWO SCREENS）存在 ✓。
- P2 A 组说明“根據日期與時間”偏宽（本周 5 题全是日期、无钟点题）——核心模板通用措辞，记观察 O6。
- 全部 5 组配对之外的 145 题已逐题核对题面与答案（§4）。

## 2. 日期/星期（`date -d`，America/Toronto）
Mon 2026-11-16 / Sun 2026-11-22（刊期）/ Tue 2026-11-03（投票日）/ Sun 2026-11-08（AP 数字日）/ Mon 2026-11-09（截稿日）/ Tue 2026-11-10 / Wed 2026-11-11 / Sun 2026-11-15 / Wed 2026-11-18 / Thu 2026-11-19 / Fri 2026-11-20（世界儿童日）/ Sat 2026-11-21（Ashes 首日按纸面新版为 2025 年事）/ Wed 2026-11-25 / Thu 2026-11-26（感恩节）/ Fri 2026-11-27（黑色星期五）/ Tue 2026-12-01（佐治亚决选日）/ Fri 2026-12-18（认证截止）/ Sun 2027-01-03（新国会就职）/ **Fri 2025-11-21**（2025–26 Ashes 首战）/ Sat 2025-11-22 / Thu 2026-01-08（系列终战）。**全部与纸面一致。**

## 3. 外部事实逐项核实（网上，2026-11-11；Ashes 为本轮改写内容，全新核实；其余与 proof1 已核实集一致，内容未改）

| 事实 | 纸面 | 核实结果 |
|---|---|---|
| 2025–26 Ashes 首战 2025-11-21 珀斯，澳大利亚 8 wicket、两天取胜；847 球，自 1888 年最短 | P4 主文 | ✓ Cricbuzz/TNT/Sky：Perth Stadium，AUS 132 & 205/2 vs ENG 172 & 164，won by 8 wkts，两天；847 球，第三少，仅次于 1888 年两场（788/792），“shortest Ashes Test since 1888”/“shortest in 137 years” |
| 系列 2025-11-21–2026-01-08；前三场珀斯/布里斯班/阿德莱德，澳大利亚 3–0 保住 Ashes；第四场墨尔本英格兰 4 wicket（两天，近十五年首胜）；第五场悉尼澳大利亚 5 wicket；终 4–1 | P4 主文 + Q46/Q125 | ✓ Sky Sports / cricket.com.au：1st Perth 8 wkts、2nd Brisbane 8 wkts、3rd Adelaide 82 runs、4th Melbourne England 4 wkts（“inside two days…first victory in 18 Tests on Australian soil”）、5th Sydney Australia 5 wkts（1 月 8 日终战），4–1 |
| Cummins 背伤缺首战、Hazlewood 腿筋伤缺首战、Smith 代队长、Boland 上场、Doggett 首秀 | P4 主文 | ✓ cricket.com.au（2025-11-24）：“lumbar back stress injury ruled Cummins out…Steve Smith take charge”；“Josh Hazlewood…serious hamstring injury”；“debutant Brendan Doggett…five wickets…Scott Boland…key role” |
| 2024 年 11 月珀斯：澳大利亚首败于该场地，印度 295 分胜 | P4 WHY PERTH? + Q63 | ✓ Cricbuzz：India 150 & 487/6 decl. beat Australia 104 & 238 by 295 runs，2024-11-25，Optus Stadium；终结澳大利亚在该场地自 2018 年不败 |
| 珀斯不在 2021–22 巡回赛 | P4 WHY PERTH? | ✓ Reuters/cricket.com.au：2021-12-06，第五场因 WA 边境隔离由珀斯移至霍巴特 |
| 下届 Ashes 2027 年 6 月英格兰 | P7 NEXT WEEK + P7 WORDS | ✓ ECB（2026-07-23 公布）：2027 Ashes 6 月 18 日–8 月 2 日，首战 Trent Bridge 6 月 18–22 日 |
| 英格兰上次在澳赢系列赛 2010–11；2017–18 与 2021–22 均 0–4；2023 英格兰打平 | P4 主文 + Q49/Q60/Q62 | ✓ 与系列赛程记录一致（2021–22 为 4–0 一平；2023 年 2–2 打平） |
| 中期选举众院 254/162/19（AP，11 月 8 日）、参院 20/13、2 未定 AK/MS、7 翻转、5 州长翻转、选前 218–214/53–47、第 120 届国会 2027-01-03 就职、认证窗口 11 月 10 日–12 月 18 日、佐治亚决选 12 月 1 日 | P1/P2/P6 | ✓ 与 proof1 已核实集一致（内容未改；AP 口径来源同 proof1） |
| Hunger Games 11 月 20 日上映；Zada/McKenna Grace/Fiennes；Lawrence 导演；2025 小说；50 届 2 倍 tribut；原声专辑 11 月 13 日 | P3 | ✓ 与 proof1 已核实集一致（内容未改） |
| I'm a Celebrity S26：11 月 16 日周一 21:00 ITV1，Ant & Dec，Murwillumbah，因英格兰–西班牙国家联赛晚一天，Unpacked 在 ITV2，营员截稿未公布 | P2/P3 | ✓ 与 proof1 已核实集一致（内容未改） |
| ATP 总决赛 11 月 15–22 日都灵；8 人名单；Sinner 膝伤缺席 | P4 | ✓ 与 proof1 已核实集一致（内容未改） |
| 英超第 11 轮：曼城–富勒姆 12:30、纽卡–阿森纳 17:30（11 月 21 日）、利物浦–曼联 16:30（11 月 22 日） | P4 | ✓ 与 proof1 已核实集一致（内容未改） |
| NFL 第 11 周：小马–德州人 11 月 19 日 20:15 ET、维京人–49 人墨西哥城 11 月 22 日 20:20 ET、爱国者慕尼黑赛后轮空 | P4 | ✓ 与 proof1 已核实集一致（内容未改） |
| 反欺凌周 11 月 16–20 日；主题 Break the Silence；Odd Socks Day 11 月 16 日十周年；约 800 万儿童；80%+ 学校；200+ 儿童定主题；ABA 主办；英格兰/威尔士/北爱 | P5 | ✓ 与 proof1 已核实集一致（内容未改） |
| 世界儿童日 11 月 20 日；主题 “My day. My rights. My future.”；1989 年《儿童权利公约》 | P5 | ✓ 与 proof1 已核实集一致（内容未改） |

## 4. 150 题逐题语义核对（摘要；全量答案行已通读 text.md 第 1001–1305 行）

- P1 TRY IT 1–6 ✓；LIGHTNING QUIZ 7–10 ✓（7 B 254、8 A 周二、9 C 218、10 C Jan 2027）。
- P2 A 11–15 ✓（Nov 3 周二、Jan 2027、Dec 1、Thu Nov 26、27）；B 16–19 ✓（will 句型）；C 20–23 ✓；D 24–27 ✓（见 §1.13）。
- P3 A 28–33 ✓；B 34–37 ✓（opens/mentor/twice/jungle）；C 38–41 **39→a、40→d 已修，四源一致**；D 42–45 ✓（published/won/painted/chose）。
- P4 A 46–51 ✓（A/C/B/A/C/B：首战 2025-11-21 珀斯、Cummins 背伤、Smith 代队长、2010–11、12:30、Sinner 膝伤）；B 52–55 ✓（hosted/lasts/eight/won）；C 56–59 ✓；D 60–63 ✓（lost/lost/ended/beat；295 分已核实）。
- P5 A 64–69 ✓；B 70–73 ✓（silence/socks/rights/speak）；C 74–77 ✓；D 78–81 ✓（are wearing/are speaking/are listening/is sitting）。
- P6 A 82–87 ✓（图表算术 254+162+19=435；33/35；7；5）；B 88–93 ✓（call≠official/certify/AK-MS/Nov 10/Congress not President/VOL.5）；C 94–99 ✓（certify/call/changed/takes/differs/official）。
- P7 DRILLS 100–107 ✓（won/more/lost/will/published/whether/chose/win；107 标题现在时 win）；ERROR CLINIC 108–111 ✓（won/continued/more than/whether）。
- P8 A 112–119 ✓（Tuesday/call/continues/will meet/writes/will certify/wears/will watch；星期与时态与正文一致）；B 120–128 ✓（含 125 A 4–1）；C 129–132 ✓；D 133–136 ✓；E 137–140 ✓（翻译；140 打破沉默。简繁同形）；F 141–144 ✓；G 145–149 ✓（row/film/popcorn/show/Friday）；150 開放題 ✓。
- 其余 149 题除 ABSTRACT 一字外全部正确。

## 5. 目视检查

- 印版 8 页总览（`render/print-p1-small.png` … `print-p8-small.png`，由交付印 PDF 渲染）：版式干净，无大面积溢出/重叠/压页脚；P5 D 节栏头跨栏见 PROOF-NOTE O7。
- 裁切目视（`render/crop-*.png`，2× 放大，由交付印 PDF 渲染）：
  - `crop-p1-numbers-title.png`：NUMBERS 框题框内（真墨余 +5.0）。
  - `crop-p1-searches-bottom.png`：D2 已修——“相對熱度示意…”行在盒内，下有盒底白边。
  - `crop-p2-senate-title.png`：D6 已修——“參議院數字”在框内，右有余白。
  - `crop-p2-didyouknow-bottom.png`：D3 已修——“November 3.”在盒内，下有盒底白边。
  - `crop-p2-andyou-bottom.png`：AND YOU? 盒末行框内（余 +4.5）。
  - `crop-p2-sayit-box2.png`：D7 已修——英文行左右均在加宽后的奶油框内。
  - `crop-p4-saturday-title.png`：D8 已修——“週六賽程”在框内，右有余白。
  - `crop-p7-toolbox-bottom.png`：工具盒干净，B2 句末行框内余量充足。
- 网版 P1/P8 渲染（`render/web-p1-small.png`、`web-p8-small.png`，由交付网 PDF 渲染）：与印版视觉一致。

## 6. re-fanout #2 承接项专项

- ABSTRACT 全文形式：498 B、206 字符、单行、无 ASCII 双引号；内容点（已宣布结果、认证 11 月 10 日–12 月 18 日、11 月 16 日反霸凌週/奇襪日、11 月 20 日世界儿童日+飢餓遊戲、11 月 21 日英超+都靈 ATP+灰燼盃 4–1 回顾、读者语言、A2–B2、150 道）与本期一致——**但含 D1 一字“宣布”**（见 PROOF-NOTE）。
- Q39→a / Q40→d 四源一致：text.md（1083/1085 行）、P3 SVG（释义顺序 + 印出题号）、registry（39 `key='a'`、40 `key='d'`）、P8 extract（39→a、40→d）。old 版互换已无。
- zh-tw：text.md 宣佈 ×13 / 宣布 ×0；registry 宣佈 ×9 / 宣布 ×0；SVG 宣佈 ×9 / 宣布 ×0；OpenCC s2t：registry + text.md + 8 SVG 全部 0 diffs；**残留 1 在 ABSTRACT.txt（D1）**。本轮其他 zh-tw 版对照：全周 9 个 zh-tw ABSTRACT 仅本版含“宣布”；es-zh-tw text.md 另有“宣布”×2（他版事宜，不属本版）。
- Q140 `打破沉默。`：registry 键与 core-en 逐字相同（简繁同形），keydiff 不含 140，印出键亦为“打破沉默。”——非错误。
- freeze-diff CJK：新增 775 字（KIT 一致），180 个不同字全部 OpenCC s2t 自恒，繁体合法新增全数追踪；`--strict-cjk` rc=1 属预期（核心读者层为简体，转换本身即新增），见 §1.3。

## 7. 产物清单（本 scratch）

- `PROOF-NOTE.md`、`GATE-LOG.md`
- `measure.py`、`measure2.py`、`measure3.py`（测量脚本，系 proof1 脚本的副本；measure3.py 仅本副本改 `group(2)`→`group(1)`）、`measure3b.log`、`measure.log`、`measure2.log`、`measure3.log`
- `occlusion.log`、`occlusion.json`、`p8-extract.log`、`p8-extract2.log`、`p8-extract.json`、`p8-compare.log`
- `freeze.log`、`freeze-diff.log`、`freeze-diff.json`、`freeze-diff-strict.log`、`freeze-diff-strict.json`、`freeze-final/`（8/8 重渲染 SVG）
- `render/print-p1..p8.png`、`render/web-p1..p8.png`（110 dpi，由交付 PDF 渲染）、`render/print-p*-small.png`、`render/web-p*-small.png`、`render/contact-sheet.png`、`render/crop-*.png`（8 张）
- `tmp/`（TMPDIR）、`probe.txt`
