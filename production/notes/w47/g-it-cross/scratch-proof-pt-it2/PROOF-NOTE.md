# PROOF-NOTE — 2026-W47 pt-it（葡萄牙语目标、意大利语读者版）— proof1（re-fanout 重建版复校）

- Proofreader: independent proof1（subagent proof-pt-it2）
- Date: 2026-11-11（UTC；任务 11:23 EST 下达）
- Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-it2/`
- Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-pt-it/`（sources untouched, no commit, no push；生产目录零写入）
- 对照：首轮 proof1（scratch-proof-pt-it1，D1–D5）；重建驱动 `scratch-refanout-pt/build_edition.sh it`，core-pt fix2 `d2b0e182`。

## §0 身份核对（磁盘为准）

| 文件 | 磁盘 SHA-256 | 字节 | 与任务一致 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | `6c8a5f3db220dcdfba6e0904b12ec66e37062f0007cfaeb9aed71b208e9911ce` | 12,930,828 | ✓ |
| `A-Lucerna-VOL4-web.pdf`（网） | `5ebf28b436f60fe0b59dcff89a4f1bf62dc0aa93bf4a4e2e7da9a2e965114e89` | 1,137,080 | ✓ |
| `2026-w47-pt-it.text.md` | `37c1980caacc6cef28d9df50133b09b45a51a8d4f17296e34412b2cd88285209` | 37,419 | ✓ |

三文件 SHA 与任务消息完全一致，字节数如上。探针通过（repo 内 `git hash-object -w` 返回 `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）。复校结束时三文件 SHA 复验未变。

## 结论：(b) 有缺陷，不能定稿

**缺陷 1 项：D6。** 首轮 5 项缺陷 D1–D5 已全部修复并复测存活（见下）；但本轮按任务 gate 6 对**全部**盒标题逐一真墨量测（首轮只量了 P1/P7 子集），新发现一处同类框标题右溢——P2「PARA NÃO ERRAR」意大利语 gloss 过长，墨出奶油框右缘约 60 单位，交付印/网 PDF 肉眼可见。其余全部复校项通过（见 GATE-LOG）。

- 150 题答案键逐题手验：**149/150 PASS + Q150 开放写作 ✓**（任务预期 149/150），四源一致（P8 印刷键 = 核心键除 137/138 = text.md 行内答案 = Respostas 汇总）。
- 全文通读（印 PDF 8 页逐版看图 + text.md 534 行逐行读）：除 D6 外无文字、事实、日期、编号、级别问题；首轮未外部核实的 O2（Q125 36 轮）与 O3（夺冠次数）本轮已 live 核实无误。
- 机械门：run.py rc=0 TOTAL 150、重建 SVG 8/8 字节一致；gates 16/16；occlusion 0 flags；freeze 核心基线 8/8 + 版内自比对 8/8，新增 CJK 仅 U+3000（9 个）；p8 extract 150/150、compare CLEAN（keydiff [137, 138]）；印/网文字层逐字节相同（110,388 字节，token 差 0）；P8 最小字号 9.75pt（= SOP §1.1 下限）；check_s11 全 PASS；creambox 除 D6 外 0 真溢出；弯引号成对、CJK 仅 U+3000、禁词/简体残留 0。

## 缺陷清单

### D6 — P2「PARA NÃO ERRAR」框标题意大利语 gloss 伸出奶油框右缘约 60 单位（新发现，非回归）

- 页码/定位：P2 第二栏，奶油框 `x[538.5,961.0] y[605.02,846.02]`（窄栏盒，宽 422.5）；标题「PARA NÃO ERRAR　La regola da ricordare」基线 y=642.02，fs=23 粗体，x=556.5。
- 源码行：`content12.py:183`（`f.box("PARA NÃO ERRAR　La regola da ricordare", [`）；意大利语 gloss 来源 `tables_it.py:58`（`"口诀": "La regola da ricordare"`）。核心同框标题为「PARA NÃO ERRAR　口诀」（`core-pt/content12.py:183`，同盒、同 x/y/fs），中文 gloss 仅 2 字，框内无溢出——溢出为**本版意大利语层引入**，与首轮 D4/D5 同类（D4「La parola della settimana」、D5「In questo numero」皆为 gloss 过长）。
- 是否回归：**不是重建回归**。首轮备份 SVG（`scratch-refanout-pt/backup-old/2026-w47-pt-it/svg/p2-vida.svg`）中该标题元素与本版逐字相同（同 x=556.5、同字串、同 fs=23 粗体）。是首轮遗漏的既有缺陷——首轮 boxtitle 日志（`boxtitle.log`、`boxtitle2.log`）中全无 PARA 一行，其只量了 P1/P7 标题子集（同类前科：pt-de2 的 D4 亦为首轮遗漏的 P1 框标题溢出）。
- 实测证据（四法一致，均指同一标题；另见 GATE-LOG §1/§2/§4）：
  1. PIL 真墨（`boxtitle_ink.py`，svglib `_pil`/`_runs`，fs=23 自身字号）：墨右 **1020.5**，框右 961.0，clear **−59.5**（`boxtitle-ink.log`）。
  2. 交付**印 PDF** 300dpi 像素实测（`pixel_boxtitle.py`，PyMuPDF）：墨右 **1023.4**，clear **−62.4**（`pixel_boxtitle.log`）；fitz 文字层 span：`'La regola da ricordare'` bbox x1=768.6pt，框右 961×0.75=720.75pt，advance 口径超 +47.9pt（≈ +63.8 SVG 单位）。
  3. 交付**网 PDF**同法像素实测：墨右 **1023.4**，clear **−62.4**；span bbox 与印 PDF 同值——缺陷在两版 PDF 中皆存在。
  4. 目视：300dpi 原生裁图 `crop-p2-PARA-NAO-ERRAR.png`——「ricordare」整词落在奶油框外的白纸上，肉眼清楚可见；全页图 `view-p2.png` 中同处亦可见标题漫出盒外（框右缘横切「ricordare」中部）。
- 严重度：溢出约 60 SVG 单位（≈15pt ≈ 5.3mm，末词近乎整词出框），非边缘擦痕；正是必查项框标题横向溢出的类别，且与 D4（+29.5）同类而幅度约两倍。occlusion 审计 0 flags 不能作为反证——该审计对无描边奶油框根本不检查 BOXTITLE（pt-de2 已证实）。
- 修复建议（已实测余量）：缩短 gloss，与 D4 的修复范式一致——首选「La regola」（PIL 真墨墨右 877.5，clear **+83.5**）；或「La regola d'oro」（advance 余量 +17.8）、「Da ricordare」（真墨 +47.5）。只改本版讲解层（`tables_it.py:58` 或 `content12.py:183`），不动核心；改后重渲染本版印/网 PDF，复跑 boxtitle（PIL + PDF 像素双法）+ creambox + 目视。另建议协调员顺查同类：pt-fr「La règle à retenir」、pt-es「La regla para recordar」、pt-nl「Het ezelsbruggetje」在同盒是否同样漫出（首轮备份值，仅作提示，非本版缺陷）。

## 首轮缺陷复验（D1–D5 全部存活）

- **D1** P1「EM POUCAS PALAVRAS」框：框底 2310 → **2348.0**，末行「em Brasília. (Página 4)」基线 2327.6，clearance **+20.4**（与 core-pt 逐一一致）；全页目视：该行已在奶油底上。✓
- **D2** P3「A SEMANA, DIA A DIA」框：框底 525 → **551.0**，末条「16h30.」基线 540.6，clearance **+10.4**；全页目视：整条在框内。✓
- **D3** P6「O CAMINHO ATÉ O GABARITO」框：框底 840 → **854.0**，末行「Página do Participante.」基线 840.8，clearance **+13.2**；全页目视：整行在框内。✓
- **D4** P7「A PALAVRA」标题：现为「A PALAVRA　La parola」（fs=23）；PIL 真墨 clear **+151.5**（KIT 称 +151.6）、印 PDF 像素 **+151.0**、网 PDF 同。✓
- **D5** P1「NESTA EDIÇÃO」标题：现为「NESTA EDIÇÃO　Questo numero」（fs=24）；PIL 真墨 clear **+23.5**（KIT 称 +23.3 at fs=24）、印 PDF 像素 **+21.7**、网 PDF 同；原 +2.5px 溢出已修。✓
- 另：core fix2 的 P4 gloss「o título 冠军」→「o título 冠军头衔」（it 值 `titolo`）已在版内，P4 Nota 盒「o título titolo」目视无溢出。

## 未决事项

- **O1 — D6 修复。** 与 D4/D5 同类同修法（缩短 gloss），修后须重渲染本版双 PDF 并复跑 boxtitle 双法 + creambox + 目视；按 SOP §8 proofread-until-zero，本轮不能定稿。
- **O2 — P1 顶栏标语意译疑似。** `tables_it.py:201`「读巴西人正在读的葡萄牙语」→「Il portoghese che legge il Brasile」（`content12.py:15`）。直译回中文为「读巴西的葡萄牙语」，与原文主客颠倒；但属标语修辞、语法完整、首轮未 flag，本轮仅记观察、不计缺陷，由协调员定夺是否改「Il portoghese che i brasiliani leggono」。
- **O3 — P8 最小字号口径。** 实测 9.75pt = SOP §1.1 下限（任务写「≥10pt」，与 SOP 字面不符；以 SOP 与 check_s11 的 9.75 阈值为准判 PASS）。已如实记入 GATE-LOG §6.1，供协调员复核。
- **O4 — D5 字体问题。** 拉丁解释层在 Noto Sans CJK SC 是已知待用户裁定的事，本轮只记录不判（任务明示），不作缺陷。

## 核实摘要（本轮独立实测，非复述 KIT）

- 全文通读：印 PDF 8 页逐版看图 + text.md 534 行逐行读；葡萄牙语正文与意大利语讲解逐项核对；除 D6 外未见拼写、性数配合、变位、标点、截断、重复词问题。
- 150 题：机械四源 0 不符；逐题手验 149/150 PASS + Q150 ✓；Q137「Venerdì 20 novembre è festa nazionale.」与 Q138「Il Palmeiras ha vinto 5–4 ai rigori.」皆为正确意大利语译文；Q139/Q140 意葡互译正确（「esce prima della fine」→「sai até o fim」；「Appunta…controllale」→「Anote…confira」）。
- P7 八句本周短语逐字出自本期正文（P1 标题、P1 导语、P3「Zumbi nasceu em Palmares」「sem memória, não há futuro」、P4「o agregado ficou em 2 a 2」、P5「a espera pelo gabarito」、P6「primeiro as fáceis, depois as difíceis」、P2「Confira o transporte…」），意译 + 页码标注齐全；读者来信披露意译 3 行齐全；范文 88 词（`len(split())`=88）；P1 头条 41 非空字符 ≤56。
- 事实抽查（live 源，本轮新核实首轮 O2/O3）：Q125 rodada 36（Palmeiras × Flamengo，周六 21 日 16h30，Nubank Parque）——CBF 10-30 赛程 + 多家同；Grêmio 第十次决赛、争第六冠（五冠 1989/1994/1997/2001/2016），Palmeiras 争第五冠（四冠 1998/2012/2015/2020）——多家 11-08/11-09 同；巴西对新加坡友谊赛周二 17 日 7h（CBF 官网 10-29 征召公告）；Enem 5,051,345 人报名、Edital nº 64/2026 第 15.1 条、第 10 个工作日 = 11 月 30 日（计入 11 月 20 日假日）、「27–30 日之间视假期是否计入」与 Ulti 11-09 的算法注释逐字一致、个人成绩 2027 年 1 月。半决赛比分与 F1 赛果与首轮 live 核实一致（本轮未重复检索）。日期星期与 P6 工作日算术复核无误（15 天 = 10 工作日 + 5 周末/假日；第 10 个工作日 = 11 月 30 日）。
- 讲解层本地化：E 节标题 SVG 为「E　TRADUZA」、text.md 为「### E · Traduza」（葡萄牙语目标语标签，正确）；全版无中文「翻譯」残留；P8 CJK 字符数 0；Q150 答案注为意大利语。
- 已排除的疑似问题（详见 GATE-LOG）：4 处 creambox BELOW-WINDOW（皆盒外章节标题/正文）；6 处 desc-clear 负值（真墨迹复验余量 +4.5~+5.4，无降部字母）；P8 注行墨右 +0.4（0.5 边际带内）；贴版心家具行墨右 ±0.4 内；「o título → titolo」与「cair → cadere in un giorno」为五版 pt fan-out 共用 gloss 惯例；ASCII 省略号撇号为全 program 惯例；「L'EDIZIONE」徽标为字体渲染特性；P3 词表栏跨栏、P2/P5 留白为核心固有排版。
