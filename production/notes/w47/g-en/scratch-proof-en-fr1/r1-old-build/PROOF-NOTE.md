# PROOF-NOTE — 2026-W47 en-fr 独立复校 proof1（2026-11-11）

- 版：`production/2026-w47/2026-w47-en-fr/`，印 `The-Lucerna-VOL4-en-fr.pdf`（29,330,444 B，SHA-256 `14da9810fa348a577d16927d90c7c2c05e67c537c533266ff81860486b7c11a5`）、网 `The-Lucerna-VOL4-en-fr.web.pdf`（2,376,712 B，SHA-256 `0f188504a65e13488a5e07c2591c9ea9fa6f2adb0b5c0b2c3719797b8d7e22c3`）、`2026-w47-en-fr.text.md`（53,239 B，SHA-256 `b882d0e9f348bcee2270f80434a379b652460c1f5e5542ed2992c9fd799c81c3`）。三者完整 SHA 与 KIT §7 及任务书均一致；两 PDF 各 8 页。
- 复校员：独立 proof1，与建版者不是同一人。只复校，未改任何源文件、未重建、未 commit、未 push、未动 tools/。中间件全在 `scratch-proof-en-fr1/`（`TMPDIR=<scratch>/tmp`），未写 /tmp，未删他人文件。
- 探针：`git hash-object -w --stdin` 成功（`9daeafb9…`）；scratch 写文件成功（`probe.txt`）。

## 结论：(b) 有缺陷，不可定稿

共 5 项：D1 严重（答案键错，阻断定稿）；D2、D3 中等（可见版式缺陷）；D4、D5 轻微（措辞）。其中 D1–D4 根在 core-en（core 盘上同错同形），记为**核心级候选**，报协调员，复校员未碰核心。D5 为本版法语层小措辞。

## 缺陷清单

### D1（严重，核心级候选）— P3 配对题答案键 Q39/Q40 互换
- 定位：P3 `C · THE WORDS`（38–41题）+ P8 答案页 `— Page 3 —` 行 + `registry.json` 39/40 条 + `text.md` 39/40 行。印/网两 PDF 文字层均含错键。
- 事实：题面（印版 P3 已渲染，SVG 与 PDF 文字层一致）：
  - a. a person who teaches and guides you（= mentor，39题）
  - b. a person chosen to take part in the Games（= tribute，38题）
  - c. a person who lives with you in the jungle camp（= campmate，41题）
  - d. the place where the Games are fought（= arena，40题）
  - 正确键：38→b、**39→a、40→d**、41→c。
  - 印出键：38→b ✓、**39→d ✗、40→a ✗**、41→c ✓（P8 印 `39. d · 40. a`）。
- 根在核心：`core-en/registry.json` 39条 `key='d'`、40条 `key='a'`，与本版完全一致（39 `mentor=导师 d`、40 `arena=竞技场 a`）。`p8.py compare` 判 CLEAN 是因为两边同错——该门只核对版与核心一致，不核对键与题面。150 题中其余 148 题已逐题核对题面/原文/图表，均对（另见 GATE-LOG “150 题逐题”）。
- 影响：按题面做对的学生在答案页被判错。须改核心 registry + 核心 P8 键 → 核心重渲染 → 本版重出 → 从头再复校一轮。

### D2（中等，核心级候选）— P1 SEARCHES 盒末行漫出盒底
- 定位：P1 右栏 SEARCHES 盒，rect `x=1439.5 y=588.0 w=422.5 h=668.0`，盒底 1256.0；盒内末行 `Intérêt relatif, pas des volumes exacts.` 基线 1274.0，**超出盒底 18.0 px**，整行落在盒外白纸上（200 dpi 裁图 `render/crop-p1-searches-1.png` 目视证实：盒底白边后才出现该行）。
- 根在核心：core-en 同盒同几何（y=588、盒底 1256.0），核心末行同样 -18.0（核心行 `相对热度示意，非精确搜索量。`）。盒高是核心模板几何问题，不是法语层改动所致。
- 工具盲区：occlusion 审计 0 flags（此类缺陷盲区）；精炼版 `creambox_check.py`（0–8 px 溢出带）判 NO OVERFLOW——18.0 px 超出其 8 px 带，漏检。原版 `creambox.py`（+45 px 窗口）能捕到，但混有已知假阳性（下块标题约 36 px 下方），须逐行裁定（已逐行裁定，见 GATE-LOG）。

### D3（中等，核心级候选）— P2 DID YOU KNOW 盒末行漫出盒底
- 定位：P2 右栏 DID YOU KNOW 盒，rect `x=1439.5 y=832.9 w=422.5 h=325.5`，盒底 1158.4；盒内末行 `November 3.` 基线 1171.1，**超出盒底 12.7 px**（200 dpi 裁图 `render/crop-p2-didyouknow-2.png` 目视证实：`November 3.` 在盒底白边之下）。
- 根在核心：core-en 同盒同几何（y=832.9、盒底 1158.4、-12.7），且漫出的行是英文核心正文（`November 3.`）。同属核心模板盒高问题。

### D4（轻微，核心级候选）— “confirmé” 一词模糊了 call 与 certified 的区分
- 定位：Q7 答案注 `(chiffre confirmé le 8 novembre)`；Q83 答案注 `19 sièges de la Chambre restent à confirmer`；P6 A 节题干 `Lisez le graphique des chiffres confirmés ci-dessus`。
- 事实：正文 P1/P6 反复强调 “A ‘call’ is not the official result”，11 月 8 日的数只是 AP 的 call、不是 certified 结果；答案注/题干却称其为 “confirmé”。核心 `registry.json` 同样写 `11 月 8 日已确认数` / `19 个选区尚未确认`，法语层是忠实翻译——根在核心措辞。建议核心与各版统一改 `appelé / annoncé le 8 novembre` 一类表述。

### D5（轻微，本版法语层）— P7 工具盒 B2 句多一个 “encore”
- 定位：P7 `THE TOOLBOX · Boîte à outils`，B2 行：`“Nobody knows whether the count will change.” Personne ne sait si le décompte va encore changer.`
- 事实：源句无 “still/again” 之意，`encore` 为添加；应为 `Personne ne sait si le décompte va changer.` 学习者据此背诵会学到一个原文没有的词。轻微，可随 D1 重出时一并改。

## 已核对无问题（要点）

- 150 题：编号 1–150 连续（registry 逐项核对）；每页题数 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；级别 A2 62 / B1 66 / B2 22；与 KIT 一致。除 D1 外，答案键逐题核对题面、原文、图表、算术（254+162+19=435；254−218=36；P8 模型文 82 词）全部正确。
- 外部事实逐项核实（见 GATE-LOG §事实核对）：星期/日期 14 项日历全对；选举数（众院 254/162/19、参院 20/13、2 未定 AK/MS、7 翻转州、5 州长翻转、选前 218–214/53–47、Johnson 不竞选共和党领袖、众院共和党 11 月 10 日/民主党 11 月 18–19 日选领袖）与 AP live 页及多家复核一致；Hunger Games（11 月 20 日上映、Zada/Fiennes/McKenna Grace、Lawrence 导演、2025 小说、50 届 2 倍 tribut）核对；I'm a Celebrity S26（11 月 16 日 21:00、Ant & Dec、Murwillumbah、因英格兰–西班牙国家联赛晚一天、Unpacked 在 ITV2、营员截稿未公布）核对；Ashes（11 月 21–25 日珀斯、Cummins 背伤、Hazlewood 腿筋、Smith 队长、Boland 顶替、Doggett 首秀、英格兰上次在澳赢系列 2010–11、4–0 两次、2023 平局、澳大利亚 2024 年 11 月在珀斯首败印度 295 分）核对；Anti-Bullying Week（11 月 16–20 日、主题 Break the Silence、Odd Socks Day 11 月 16 日十周年、约 800 万儿童、80%+ 学校、200+ 儿童定主题、ABA 主办、英格兰/威尔士/北爱）核对；ATP 总决赛（11 月 15–22 日都灵、8 人名单与 Sinner 膝伤缺席完全一致）核对；英超第 11 轮（曼城–富勒姆 12:30、纽卡–阿森纳 17:30、利物浦–曼联周日 16:30）核对；NFL 第 11 周（小马–德州人 11 月 19 日 20:15 ET、维京人–49 人墨西哥城 11 月 22 日 20:20 ET、爱国者慕尼黑赛后轮空）核对。
- 8 页目视：印版 P1–P8 全页 + 网版 P1/P8 均已看图（`render/print/p-*.png`、`render/web/p1-1.png`、`render/web/p8-8.png`），除 D2/D3 外无溢出、重叠、压页脚、图片与出处问题；网版与印版视觉一致。
- 引号：弯引号 “ 82 / ” 82 成对；U+2019 0；ASCII 撇号 72；禁词 0（TODO/占位/SOP/cover/bridge 等 0 命中；“Note | Note |” 0）；真实 CJK 仅蛾标非可见 `<title>Lucerna 三色蛾</title>`（与核心共有）；家具分隔符为全角空格（U+3000 141），· 计数与核心完全一致（282，同为题支/词表/答案键分隔符）。
- 金句：P7 8 句全部逐字出自本期正文，页码标注正确。
- ABSTRACT.txt：一行、法语、无 ASCII 双引号（722 B）。
- P7 工具盒：盒内间隙 +48.5 px（盒底 1038.7，末基线 990.2 左右），无墨水漫出（D2/D3 是 P1/P2 的盒，不是 P7 工具盒）。
- P8 实测最小字号：PDF 有效 10.12 pt（答案键块在 0.75 缩放组内；SVG 属性最小 13.5 pt），≥ §1.1 下限 9.75 pt，无违规；但 KIT “13.5 pt” 写的是属性值而非渲染有效值（见 GATE-LOG 备注）。
- 其余保留项与 KIT 一致：P4/P5 “B/D” 节头在栏底、题在下栏（模板流，与核心同）；P5 词表行 `Chaque enfant a des droits | Every child has rights = Chaque enfant a des droits.` 与核心模板同构（核心：`每个孩子都有权利｜Every child has rights = …`）；VOL 计数逐页与核心一致（VOL.4 12、VOL.5 8、VOL.3 3）。

## 未独立再核实（核心层、低风险、已列出）
- 世界儿童日 2026 主题措辞 `My day. My rights. My future.`（日期 11 月 20 日与 1989 年《儿童权利公约》已核实）；Hunger Games 原声专辑 11 月 13 日；ATP 决赛 “不早于 18:00”；各州认证窗口 11 月 10 日–12 月 18 日（区间表述）；Lawrence 儿童照片日期 1912 年 2 月 19 日；投票亭图片说明细节。

## 建议下一步（报协调员定）
1. 核心修 D1（registry 39/40 键互换 + 核心 P8 键）、D4措辞，核心模板修 D2/D3 盒高（或盒内末行重排）；本版随 D5 一并重出。
2. 重出后整版重渲染，本版从头再做一轮全量复校（proof2），直至一整轮零问题。
3. 工具缺口：`creambox_check.py` 的 0–8 px 溢出带漏掉了 12.7/18.0 px 的整行漫出——建议把溢出带放宽或把 “盒内末行基线超出盒底” 本身判为溢出（须先处理下块标题假阳性）。
