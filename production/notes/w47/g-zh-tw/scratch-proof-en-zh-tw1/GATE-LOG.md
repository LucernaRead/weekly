# GATE-LOG — 2026-W47 en-zh-tw proof1（独立复校，2026-11-11）

复校员：proof1（独立）。对象 `production/2026-w47/2026-w47-en-zh-tw/`。
探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；scratch 真实写文件成功。
`TMPDIR=<scratch>/tmp` 全程；未写 /tmp。未改源文件、未重建、未 commit、未 push。

## 0. 对象 SHA（实测）

| 文件 | 字节 | SHA-256（实测） | KIT §7 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-zh-tw.pdf` | 38,152,082 | `d2e919473d70463a00b3be10129bfecbd3c1a9137b0ae4ab0cf8ca2bdea78e07` | 一致 |
| `The-Lucerna-VOL4-en-zh-tw.web.pdf` | 2,927,283 | `df41f1fc1a6786b839c63fdd53ecec1fdecba57a19ddf7c274a679762f421545` | 一致 |
| `2026-w47-en-zh-tw.text.md` | 50,505 | `6ecf354e4e614c77d747604aab6ef888ac794305869e997bc4d9049b31324dbc` | 大小一致（KIT 未列 SHA） |
| `ABSTRACT.txt` | 151 | 一行、繁体中文、无 ASCII 双引号 | 一致 |

两 PDF 各 8 页，1462.5 × 2025 pt。

## 1. 机械门（实跑）

### 1.1 occlusion 审计（正式）
```
tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-en-zh-tw --json <scratch>/occlusion.json
→ selftest OK: planted classes fired {BOXTITLE: 1, COVER: 1, EDGE: 1, FOOTER: 1, LINEX: 1, TEXTX: 1}; clean controls silent
→ production/2026-w47/2026-w47-en-zh-tw/svg: 0 flags
```
盲区记录：审计 BOXTITLE 只查有描边/填色 `#2c2822` 的框，不覆盖奶油框（D6/D7/D8 均由此漏检）；盒内末行漫出（D2/D3）亦不在类目内——本次由 creambox 实测 + 目视裁定补上。

### 1.2 p8 extract + compare
```
tools/p8.py extract --p8 .../svg/p8-test.svg --total 150
→ noted set = 60 of 150 (parse: joined)
  set: [3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82, 83, 84, 85, 86, 87, 89, 108, 109, 110, 111,
        112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
        130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
tools/p8.py compare --core-p8 core-en/svg/p8-test.svg --edition-p8 .../svg/p8-test.svg --total 150
→ core 60 noted / edition 60 noted / status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]
```
keydiff 说明：137–139 为翻译题（简繁字形不同）、150 为開放題，预期内；140 因简繁同形而不列入。compare 对键错是盲的——D1（Q39/40 互换）两边同错，故判 CLEAN。

### 1.3 freeze（8/8 + diff）
```
tools/freeze.py baseline --build production/2026-w47/2026-w47-en-zh-tw --core-svg .../svg --out <scratch>/freeze-final
→ baseline: 8/8 SVGs byte-identical
  p1 0a70632e… / p2 e1054436… / p3 f516d68b… / p4 a329e1d3… / p5 eb99395a… / p6 c6d14ddd… / p7 bc029bc5… / p8 a8253bd6…
  core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
tools/freeze.py diff --core-svg core-en/svg --edition-svg .../svg
→ p1 +23/-23（CJK 202→231，新增 98）/ p2 +32/-32（278→283，新增 109）/ p3 +17/-17（146→154，新增 52）
  / p4 +16/-16（143→151，新增 50）/ p5 +16/-15（132→140，新增 45）/ p6 +14/-14（159→161，新增 56）
  / p7 +40/-40（429→422，新增 142）/ p8 +82/-90（634→541，新增 224）
→ TOTAL added CJK characters: 776（与 KIT 一致）
```
P5 +16/-15 不对称说明：P5 gloss 行 “silence = 沉默”在两版断行位置不同（本版断成 “沉”+“默”两行），属断行 artifact，非内容差。P8 +82/-90 为简繁字形 + 家具（“翻譯：”vs“Translate:”）差异。

### 1.4 creambox 全版扫描（32 盒；`measure.py` + `measure2.py`）
方法：每盒取盒内末基线（真 clearance）+ 盒底上 45 px 带内逐行裁定（x0≈盒内 inset 且字号为正文/gloss 号者为盒内行；x0=栏 x 且 22–25pt 者为下块栏头）。

| 页 | 盒 | 盒内末基线 clearance | 带内行裁定 |
|---|---|---|---|
| P1 | NUMBERS y=786 | +45.7 | TRY IT NOW（栏头，FP） |
| P1 | SEARCHES y=588 | +16.0 | **相對熱度示意…（盒内行，+18.0，D2）** |
| P1 | IN THIS ISSUE y=1280 | +48.0 | THE WORD OF THE WEEK（栏头，FP） |
| P1 | IN BRIEF y=1874 | +44.0 | — |
| P2 | SENATE y=526 | +48.1 | Life goes on…（栏头，FP） |
| P2 | CALENDAR y=200 | +48.1 | WHAT IS ON THIS WEEK?（栏头，FP） |
| P2 | gloss y=1400 | +47.7 | — |
| P2 | DID YOU KNOW y=833 | +17.9 | **November 3.（盒内行，+12.7，D3）** |
| P2 | AND YOU? y=1184 | **+4.5**（最紧，末行中文、无降部，框内） | — |
| P2 | SAY IT ×3 y=1636 | +30.0 ×3 | —（横向见 §1.5） |
| P3 | COMING SOON y=200 | +48.1 | A film is not only…（栏头，FP） |
| P3 | gloss y=1224 | +47.7 | A COMPREHENSION（栏头，FP） |
| P3 | HAYMITCH'S y=856 | +48.5 | FIVE SENTENCES（栏头，FP） |
| P4 | WHY PERTH? y=200 | +48.1 | How do you follow…（栏头，FP） |
| P4 | gloss y=1086 | +47.7 | A COMPREHENSION（栏头，FP） |
| P4 | SATURDAY y=856 | +48.5 | ONE SCREEN, TWO SCREENS（栏头，FP） |
| P5 | （左下）y=2034 | +48.1 | If you want to practise（栏头，FP） |
| P5 | gloss y=200 | +47.7 | A COMPREHENSION（栏头，FP） |
| P5 | SPEAK UP y=852 | +48.5 | FRIDAY'S WORDS（栏头，FP） |
| P6 | BALLOT y=200 | +48.1 | A note on numbers…（栏头，FP） |
| P6 | gloss y=779 | +47.7 | READ THE CHART（栏头，FP） |
| P6 | HOW LONG? y=666 | +48.5 | FIFTY ELECTIONS（栏头，FP） |
| P7 | WORDS win/won y=254 | +47.7 | win = to get first place…（栏头，FP） |
| P7 | WORDS more than y=888 | +47.7 | more than = a bigger…（栏头，FP） |
| P7 | GRAMMAR will y=1563 | +47.7 | The counting will continue…（栏头，FP） |
| P7 | GRAMMAR past y=2026 | +47.7 | Use the past for the past…（栏头，FP） |
| P7 | GRAMMAR headlines y=254 | +47.7 | Newspapers use the present…（栏头，FP） |
| P7 | GRAMMAR whether y=684 | +47.7 | Nobody knows whether…（栏头，FP） |
| P7 | **TOOLBOX y=651** | **+48.5（墨水最低行 961，盒底 1008.2，余 +47.2；B2 句末行 “count will change.” + “會不會變。”，降部字母干净）** | READERS' CORNER（栏头，FP） |
| P8 | MODEL y=1720 | +92.4 | — |

### 1.5 框题 text_w + 真墨实测（全部奶油框题）
| 框题 | advance 止点 / 框右缘 | advance 余量 | 真墨（卡片 PNG） | 真墨余量 |
|---|---|---|---|---|
| P1 THE WEEK IN NUMBERS　數字看本週 | 1410.0 / 1412 | +1.5 | 1007..1407 | **+5.0** |
| P2 THE SENATE, IN NUMBERS　參議院數字 | 989.1 / 961 | **−28.1（D6）** | 557..986 | **−25（D6）** |
| P2 THE CALENDAR　本週日曆 | 1294.2 / 1412 | +117.3 | — | — |
| P3 COMING SOON　即將上映 | 836.6 / 961 | +124.4 | — | — |
| P3 HAYMITCH'S GAMES　海米奇的比賽 | 1842.9 / 1862 | +19.1 | 1459..1841 | +21.0 |
| P4 WHY PERTH?　為什麼去珀斯？ | 885.9 / 961 | +75.1 | — | — |
| P4 SATURDAY, NOVEMBER 21　週六賽程 | 1861.3 / 1862 | +0.7 | 1458..1865 | **−3（D8）** |
| P5 ODD SOCKS, IN NUMBERS　奇襪日 | 486.9 / 510 | +23.6 | 107..482 | +28.0 |
| P5 SPEAK UP　大聲說出來 | 1707.6 / 1862 | +154.4 | — | — |
| P6 A PRACTICE BALLOT　模擬選票 | 895.4 / 961 | +65.6 | — | — |
| P6 HOW LONG?　任期多長？ | 1732.5 / 1862 | +129.5 | 1459..1726 | +136.0 |
| P7 THE TOOLBOX　句型工具箱 | 1756.1 / 1862 | +105.9 | 1458..1755 | +107.0 |
| P8 MODEL　範文 | 1161.2 / 1862 | +700.8 | — | — |
注：core-en 同法实测——SENATE 真墨亦 557..986（−25）、SATURDAY 真墨亦 1458..1865（−3），与本版同形同数，根在核心。P1 NUMBERS 的首次真墨测量曾因扫描窗截在框缘而误报 +1.0，已用加宽窗口重测为 +5.0（另核：y=791–794、x>1412 的墨为邻栏 SEARCHES 条形图，非标题墨）。

### 1.6 P2 SAY IT 横向实测
| 盒 | 英文行 span / 盒 | 中文行 span / 盒 |
|---|---|---|
| 盒 1 x=159–439 | The counting continues. 181.0..417.1 ✓ | 計票還在繼續。229..369 ✓ |
| 盒 2 x=610–890 | The new Congress meets in January. 574.0..926.1，**左超 36.0、右超 36.1（D7）** | 新國會在一月開會。660..840 ✓ |
| 盒 3 x=1060–1340 | Happy Thanksgiving! 1094.9..1305.1 ✓ | 感恩節快樂！1140..1260 ✓ |

### 1.7 keycheck（registry vs text.md vs 印版 P8 键）
- registry 150 条；text.md 答案行 150 行（1–150 连续）；逐项核对：**0 不符**。
- 印版 P8 键（`p8.py extract --json`）vs registry：仅 2 处 benign——139 印出“新國會將於2027 年 1 月開會。”vs registry“將於 2027 年”（空格断行差异）；150 印出“開放題”（键为开放题，后接要点说明，extract 只取首段）。
- 印版 P8 键含 D1 错键：`38. b · 39. d · 40. a · 41. c`（SVG 可见）。

### 1.8 印/网文字层逐页比对（PyMuPDF token-multiset）
| 页 | print tokens | web tokens | multiset diff | 字符数 print/web |
|---|---|---|---|---|
| p1 | 783 | 783 | 0 | 3420 / 3420 |
| p2 | 974 | 974 | 0 | 4225 / 4225 |
| p3 | 899 | 899 | 0 | 3953 / 3953 |
| p4 | 876 | 876 | 0 | 3909 / 3909 |
| p5 | 781 | 781 | 0 | 3502 / 3502 |
| p6 | 956 | 956 | 0 | 4166 / 4166 |
| p7 | 860 | 860 | 0 | 3968 / 3968 |
| p8 | 1611 | 1611 | 0 | 6306 / 6306 |

### 1.9 P8 最小字号（印版 PDF spans，PyMuPDF）
- P8 min **10.12 pt**（答案键块，0.75 缩放组内）；P1–P7 min 均为 11.62 pt（图注）。≥ §1.1 下限 9.75 pt，通过。
- KIT “13.5 pt”是 SVG 属性值（px），非渲染 pt——口径备注，非本版缺陷。

### 1.10 §1.1 字体/配色
- 字体（SVG）：Newsreader 1007、Noto Sans CJK TC 619、Noto Serif CJK TC 48、UnifrakturMaguntia 1（刊头）、DejaVu Sans 4（符号）。合规；无 Noto Sans（俄语读者）等无关字体。
- 用色集合与 core-en **完全一致**（fill/stroke 集合逐项比对，edition-only 与 core-only 均为空）。§1.1 外的色（#4f765d、#84a283、#4d72b4、#7898cd、#d7b257、#edd17f、#f1e8d4、#34483a、#cac8ba、#ffffff）均为图表/地图/搜索条内容色，核心共有。
- 家具分隔符：U+3000 141（核心 132，+9 为繁体家具多用全角空格）；· 282，与核心完全一致；VOL.4 ×12、VOL.5 ×8、VOL.3 ×3，与核心一致。

### 1.11 弯引号 U+201C/U+201D/U+2019 在 CJK 语境计数
- SVG：“ 82 / ” 82 成对；U+2019 **0**。按 font-family 分：全部 82 对均在 Newsreader（拉丁）节点；**CJK 字运行 0**。
- 唯一斜体对：P1 每周一词 “midterm”（Newsreader 斜体，§1.1 本周词斜体）；**P7 无斜体引号**（任务书所称“P7 Newsreader 斜体对”在本版未见——仅 P1 一对斜体引号）。
- text.md：“ 81 / ” 81，U+2019 0。SVG 多一对是 P3 图注 “Surprised!”（Rousseau 画名，text.md 按惯例跳过图注）。
- text.md 中与 CJK 同行的引号（P7 工具盒三行、P8 E 节四行）渲染时按字形分 run，SVG 里中英分属不同 <text> 节点，无 CJK 节点含弯引号。

### 1.12 简繁脚本门（OpenCC s2t）
- registry.json：0 差异；2026-w47-en-zh-tw.text.md：0 差异；ABSTRACT.txt：0 差异。交付物中零简体字。

### 1.13 配对题释义顺序（印版 SVG 节点顺序手验）
| 节 | 释义顺序（印版） | 键 | 结论 |
|---|---|---|---|
| P2 D 24–27 | a=turkey, b=runoff, c=certify, d=Thanksgiving | 24→b, 25→c, 26→a, 27→d | ✓ 全对 |
| P3 C 38–41 | a=mentor, b=tribute, c=campmate, d=arena | 38→b, **39→d ✗（应 a）, 40→a ✗（应 d）**, 41→c | **D1** |
| P4 C 56–59 | a=break, b=Test, c=tour, d=injury | 56→b, 57→c, 58→d, 59→a | ✓ 全对 |
| P5 C 74–77 | a=speak up, b=right, c=silence, d=bullying | 74→d, 75→a, 76→b, 77→c | ✓ 全对 |
| P8 F 141–144 | a=midterm, b=call, c=runoff, d=certify | 141→b, 142→c, 143→d, 144→a | ✓ 全对 |

### 1.14 其余核对
- P7 金句 8/8 逐字出自本期正文（页码标注正确；“A ‘call’…”含嵌套引号，regex 截断但正文逐字核对无误）。
- MODEL 82 词（字母数字 token 计，与 KIT 一致）。
- 可见文本禁词：TODO/占位/SOP/cover/bridge/lorem/FIXME/XXX/TBD/placeholder **0**（1680 个可见文本节点；原始 SVG 源码中的命中均为 base64 图片数据）。
- P2 A 组说明“根據日期與時間”偏宽（本周 5 题全是日期、无钟点题）——核心模板通用措辞，记观察 O5。

## 2. 日期/星期（`date -d`，America/Toronto）
Mon 2026-11-16 / Sun 2026-11-22（刊期）/ Tue 2026-11-03（投票日）/ Sun 2026-11-08（AP 数字日）/ Mon 2026-11-09（截稿日）/ Tue 2026-11-10 / Wed 2026-11-11 / Sun 2026-11-15 / Wed 2026-11-18 / Thu 2026-11-19 / Fri 2026-11-20（世界儿童日）/ Sat 2026-11-21（Ashes 首日按纸面）/ Wed 2026-11-25 / Thu 2026-11-26（感恩节）/ Fri 2026-11-27（黑色星期五）/ Tue 2026-12-01（佐治亚决选日）/ Fri 2026-12-18（认证截止）/ Sun 2027-01-03（新国会就职）。**全部与纸面一致。**

## 3. 外部事实逐项核实（网上，2026-11-11）

| 事实 | 纸面 | 核实结果 |
|---|---|---|
| 中期选举众院 254/162/19（AP，11 月 8 日 21:00 ET） | P1/P6/图表 | ✓ californiatoday（AP 口径）、en.newjinmedia、bitcoinversus 均 254–162、19 未定；AP 于 11 月 4 日 01:24 ET 宣布众院归属 |
| 参院 20/13、2 未定 AK/MS；7 翻转（IA/KS/ME/NC/OH/SC/TX） | P1/P2/P6 | ✓ 同上；AP 于 11 月 3 日 23:36 ET 宣布参院归属；新参院 54–44（2 未定，含 2 独立） |
| 5 州长翻转 GA/IA/NV/OH/TX；选前 218–214 / 53–47 | P1/P6 | ✓ 同上 |
| 认证窗口 11 月 10 日–12 月 18 日 | P1/P2/P6 | ✓ congresscountdown（Ballotpedia/NCSL）：各州 11 月 10 日–12 月 18 日认证，7 州无固定日期 |
| 佐治亚决选 12 月 1 日（仅佐治亚；密西西比常规大选无决选） | P2/P6/图表 | ✓ congresscountdown + gamatters：佐治亚无过半则 12 月 1 日决选；密西西比得票最多者当选（州务卿 12 月 3 日宣布）；Ossoff 59.0% 已过半，决选本不会发生 |
| 新国会 2027 年 1 月 3 日就职（第 120 届） | P1/P2/P6 | ✓ californiatoday：120th Congress convenes Jan 3, 2027 |
| Hunger Games 11 月 20 日上映；Zada/McKenna Grace/Fiennes；Lawrence 导演；2025 小说；50 届 2 倍 tribut；原声专辑 11 月 13 日 | P3 | ✓ drawpie/9to5marvel/shortlist/nerdsnack：2026-11-20 周五上映（IMAX），Zada 16 岁 Haymitch，Fiennes 为 Snow，Francis Lawrence 导演，小说 2025-03-18，原声专辑 11 月 13 日（MCA） |
| I'm a Celebrity S26：11 月 16 日周一 21:00 ITV1，Ant & Dec，Murwillumbah，因英格兰–西班牙国家联赛晚一天，Unpacked 在 ITV2，营员截稿未公布 | P2/P3 | ✓ Capital/energyradio/memorabletv：ITV 已确认 11 月 16 日 21:00，首播原定周日因 11 月 15 日英格兰对西班牙欧国联（马德里 20:45 开球）推迟一天；Unpacked 由 Sam Thompson 与 Kemi Rodgers 在 ITV2 主持；ITV 未确认营员名单 |
| ATP 总决赛 11 月 15–22 日都灵；8 人名单 Zverev/Alcaraz/Shelton/Medvedev/Cobolli/Fils/Tiafoe/Jodar；Sinner 膝伤缺席（2024+2025 两届冠军） | P4 | ✓ rallyhub/livetennis/tntsports：名单完全一致；Sinner 10 月 6 日宣布赛季结束（右膝治疗），Jodar 以 Race 第 9 名（3,234 分）递补；分组抽签 11 月 12 日周四 |
| 英超第 11 轮：曼城–富勒姆 12:30、纽卡–阿森纳 17:30（11 月 21 日）、利物浦–曼联 16:30（11 月 22 日） | P4 | ✓ premierleague.com / vavel / sportsmole：三场时间完全一致 |
| NFL 第 11 周：小马–德州人 11 月 19 日 20:15 ET；维京人–49 人墨西哥城 11 月 22 日 20:20 ET；爱国者慕尼黑赛后轮空 | P4 | ✓ sportradar/nflplayoffpass/paramountplus：Colts at Texans Thu Nov 19 8:15pm ET；Vikings at 49ers Mexico City Sun Nov 22 8:20pm ET NBC；Patriots–Lions Munich Sun Nov 15 9:30am ET，Week 11 轮空 |
| 反欺凌周 11 月 16–20 日；主题 Break the Silence；Odd Socks Day 11 月 16 日十周年；约 800 万儿童；80%+ 学校；200+ 儿童定主题；ABA/NCB；英格兰/威尔士/北爱 | P5 | ✓ anti-bullyingalliance.org.uk（学校包 + 社交包）：2026-11-16–20，主题 Break the Silence，Odd Socks Day 十周年，ABA 主办（NCB），英格兰/威尔士/北爱；“去年逾 800 万儿童参加”；主题由 200+ 儿童参与选定 |
| 世界儿童日 11 月 20 日；主题 “My day. My rights. My future.”；1989 年《儿童权利公约》 | P5 | ✓ unicef.org + 多家：2026 主题 “My day. My rights. My future.”，11 月 20 日，公约 1989-11-20 通过 |
| 感恩节 11 月 26 日（11 月第四个周四）；黑色星期五 11 月 27 日 | P2 | ✓ 日历（date -d） |
| **Ashes：2025–26 系列 2025-11-21–2026-01-08 已打完，澳大利亚 4–1；首场珀斯 2025-11-21–22，8 wicket 两天取胜；Perth Stadium 已办过 Ashes Test** | **P4（D5）** | **✗ 与纸面相反——纸面把 2025 年 11 月的事实写成 2026 年 11 月 21 日即将开打（Wikipedia 2025–26 Ashes series、Flashscore、Sky Sports）** |
| Mike Johnson 不竞选新一届众议院共和党领袖；两党领袖选举 11 月 10 日/18–19 日 | P2/P6 | 未独立再核实（兄弟版已核；低风险） |
| “How to Survive the Jungle”特别节目 11 月 15 日；ATP 决赛“不早于 18:00”；Lawrence 儿童照片 1912-02-19；P4“Day one is already sold out” | P3/P4/P5 | 未独立再核实（低风险） |

## 4. 150 题逐题语义核对（摘要）

- P1 TRY IT 1–6 ✓；LIGHTNING QUIZ 7–10 ✓（7 B 254、8 A 周二、9 C 218、10 C Jan 2027）。
- P2 A 11–15 ✓（Nov 3 周二、Jan 2027、Dec 1、Thu Nov 26、27）；B 16–19 ✓（will 句型）；C 20–23 ✓；D 24–27 ✓（见 §1.13）。
- P3 A 28–33 ✓；B 34–37 ✓；C 38–41 **39/40 互换（D1）**；D 42–45 ✓（published/won/painted/chose）。
- P4 A 46–51 ✓；B 52–55 ✓（hosts/lasts/eight/sold）；C 56–59 ✓；D 60–63 ✓（lost/lost/ended/beat；295 分见 D5 注）。
- P5 A 64–69 ✓；B 70–73 ✓；C 74–77 ✓；D 78–81 ✓（are wearing/are speaking/are listening/is sitting）。
- P6 A 82–87 ✓（图表算术 254+162+19=435；33/35；7；5）；B 88–93 ✓；C 94–99 ✓（certify/call/changed/takes/differs/official）。
- P7 DRILLS 100–107 ✓（won/more/lost/will/published/whether/chose/win）；ERROR CLINIC 108–111 ✓（won/continued/more than/whether）。
- P8 A 112–119 ✓（Tuesday/call/continues/will meet/writes/will certify/wears/will watch；星期与时态与正文一致）；B 120–128 ✓；C 129–132 ✓；D 133–136 ✓；E 137–140 ✓（翻译）；F 141–144 ✓；G 145–149 ✓（row/film/popcorn/show/Friday）；150 開放題 ✓。
- 其余 148 题除 D1 外全部正确。

## 5. 目视检查

- 印版 8 页总览（`render/contact-sheet.png`）：版式干净，无大面积溢出/重叠/压页脚。
- 裁切目视（`render/crop-*.png`，3× 放大）：
  - `crop-p2-senate-title.png`：D6 确认——“數字”在框外白纸上。
  - `crop-p4-saturday-title.png`：D8 确认——框边从“程”字中间切过。
  - `crop-p1-searches-bottom.png`：D2 确认——“相對熱度示意…”行在盒外白纸上。
  - `crop-p2-didyouknow-bottom.png`：D3 确认——“November 3.”在盒外白纸上。
  - `crop-p2-sayit-box2.png`：D7 确认——英文行左右均漫出奶油框。
  - `crop-p7-toolbox-bottom.png`：工具盒干净，B2 句末行框内余量充足。
  - `crop-p1-numbers-title.png`：NUMBERS 框题框内（真墨余 +5.0）。
- 网版 P1/P8 渲染（`render/web-p1-p8.png`，PyMuPDF 100dpi）：与印版视觉一致，含 D2 同形缺陷（网版亦然）。

## 6. 产物清单（本 scratch）

- `PROOF-NOTE.md`、`GATE-LOG.md`
- `measure.py`、`measure2.py`、`measure3.py`（测量脚本）、`measure.log`、`measure2.log`、`measure3.log`
- `occlusion.log`、`occlusion.json`、`p8-extract.log`、`p8-extract.json`、`p8-compare.log`、`p8-compare.json`
- `freeze.log`、`freeze.json`、`freeze-final/`（8/8 重渲染 SVG）、`freeze-diff.log`、`freeze-diff.json`
- `render/contact-sheet.png`、`render/crop-*.png`（7 张）、`render/web-p1.png`、`render/web-p8.png`、`render/web-p1-p8.png`
- `tmp/probe.txt`
