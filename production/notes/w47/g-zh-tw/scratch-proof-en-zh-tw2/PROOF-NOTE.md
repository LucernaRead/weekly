# PROOF-NOTE — 2026-W47 en-zh-tw 独立复校 proof2（Q73 delta 后，2026-11-11）

- 版：`production/2026-w47/2026-w47-en-zh-tw/`（English target × Traditional Chinese readers），
  复校对象为 Q73 键同步 delta（content56.py Q73 键 "speak"→"up"）后的现状。
- 复校员：独立 proof2，与建版者/delta 执行者不是同一人。只复校，未改任何生产文件、
  未重建、未 commit、未 push、未动 tools/、未碰 core-en。中间件全在
  `hidden_files/w47/scratch-proof-en-zh-tw2/`（`TMPDIR=<scratch>/tmp`），未写 /tmp。
- 探针：`git hash-object -w --stdin` 成功（`e69de29b…`）；scratch 真实写文件成功。

## 结论：(a) 零缺陷，可定稿

9 门全过。proof1 的 D1–D9 在本次现状中逐项独立复核，**全部已关闭**（见下节，每项均有
实测值与渲染证据，非采信转述）；delta 范围亦逐项独立核实（仅 p8 SVG 变化、registry 与
text.md 各仅 Q73 一行差异、ABSTRACT 未动）。150 键逐项手核全部适配。

## 先验 SHA（实测，与任务书一致）

| 文件 | 字节 | SHA-256（实测） |
|---|---|---|
| `The-Lucerna-VOL4-en-zh-tw.pdf`（print） | 38,152,349 | `854d0943264c0821842da52d75585a5eeaaf537b371e0148d22bfab7a1853468` |
| `The-Lucerna-VOL4-en-zh-tw.web.pdf` | 2,965,206 | `e6e9f8596f14d431c7805b0ad630c91669317b2a99f3d4557ac08903526a41bb` |
| `2026-w47-en-zh-tw.text.md` | 51,144 | `cf12ebfe88d7804ccef05d2fb62d8e94dc68ed081a20577cb8adac2ae6386e2b` |
| `ABSTRACT.txt`（必须未动） | 498 | `47750881038ea49c33d1a562346d13a23bb0b058f6e487e3dd35a985ecc80f16` |
| `registry.json` | — | `ee44f57db25c51848ec30e1912731437b1ffb2a1046ddc87ed245e9bc5e3df3c` |

复校结束时四件 SHA 再次复核，无变化（见 GATE-LOG §0）。

## Q73 delta 四源一致（全部为 up）

1. `registry.json`：`{"n": 73, "page": 5, "level": "A2", "type": "完成句子", "key": "up", "note": "speak up = 大聲說出來"}`。
2. `text.md` L1151：`73. [A2] 完成句子 — up (speak up = 大聲說出來)`。
3. P8 SVG/PDF 印出：ANSWERS 第 5 版 `73. up · 74. d · 75. a · 76. b (right = 權利 b) · 77. c · 78. Schools …`
  （p8.py extract 键亦为 `up`；P8 渲染图目视确认）。
4. P5 SVG/PDF：题干 `Speak ___: tell a teacher.` + gloss `to speak up = 大聲說出來`
   （P5 渲染图目视确认；P5 SVG SHA 与 delta 前完全相同 `c9985432…`，符合“键只印在 P8”的预期）。
5. Delta 范围核实：p1–p7 SVG SHA 与 delta 前（`scratch-delta-en-zh-tw/pre-svg-sha.txt`）逐一相同，
   仅 p8-test.svg 变化（`a7b6345d…` → `38073581…`）；registry SHA 与 delta 后记录一致
   （`ee44f57d…`），Q73 为唯一 registry 差异（与 core 的 diff 仅剩 137/138/139/150）；
   `content56.py:49` 为 `f.ex("A2", "完成句子", "up", …`，`grep '"speak", "speak up'` 无残留。

## proof1 D1–D9 逐项复核（全部关闭，独立实测）

| 缺陷 | 本次实测 | 结论 |
|---|---|---|
| D1 Q39/Q40 键互换 | registry 39=`a`、40=`d`；P8 extract 39=`a`、40=`d`；P8 印出 `38. b · 39. a · 40. d · 41. c`；P3 印版释义顺序 a=mentor、b=tribute、c=campmate、d=arena | 关闭 |
| D2 P1 SEARCHES 盒末行漫出 | 盒底 1256.0，末行 `相對熱度示意，非精確搜尋量。` 基线 1244.0，余 +12.0；真墨底 1245，余 +11.0；P1 渲染图目视盒内 | 关闭 |
| D3 P2 DID YOU KNOW 盒末行漫出 | 盒 y=833，盒底 1185.4（已加高），末行 `November 3.` 基线 1171.1，余 +14.3；真墨底 1170，余 +15.4；P2 渲染图目视盒内 | 关闭 |
| D4 “已確認”模糊 call/certified | registry 中 `已確認` 0 处；Q7/Q82/Q83/Q84 已改 `已宣佈/尚未宣佈`；仅 Q90 `兩個參議院選區尚未確認`，指两场仍未 call 的参议院选区，表述准确 | 关闭 |
| D5 Ashes 整版错一年 | 全文已改写为 2025–26 回顾：标题 `Perth, One Year On: How Australia Kept the Ashes`；首战 2025-11-21 珀斯、两天八 wicket、系列 2025-11-21 至 2026-01-08、4–1、英格兰第四场墨尔本四 wicket 取胜、第五场悉尼澳大利亚五 wicket；P1 IN BRIEF、P2、P5、P7 金句与 NEXT WEEK 联动处均已改；`verify_ed.py` 全部 PASS（含“无 Ashes begin、无 second week in Perth”） | 关闭 |
| D6 P2 SENATE 框题漫出 | 标题已缩短为 `SENATE IN NUMBERS　參議院數字`；advance 556.5..930.5，框右缘 961，余 +30.5；真墨 558..929，余 +32.0 | 关闭 |
| D7 P2 SAY IT 第 2 盒英文行漫出 | 第 2 盒已加宽至 380（x=560..940）；英文行 advance 574.0..926.1，余左 +14.0、右 +13.9；真墨 575..930，盒内 | 关闭 |
| D8 P4 框题真墨出框 | 标题已缩短为 `SATURDAY, NOV 21　週六賽程`；advance 1457.5..1782.1，余 +79.9；真墨 1459..1784，余 +78.0 | 关闭 |
| D9 P7 NEXT WEEK 无法兑现 | 已改写：`Thanksgiving in America. The Ashes: England's rematch waits until June 2027. More certified results of the midterm election. And your letters — the first real ones.`（无 flat promise、无“第二周在珀斯”）；P6 条件式写法保留 | 关闭 |

## 150 键逐项手核（key-vs-stem 适配）

- stub 抽取的 150 对（n/level/type/key/note/body/opts）与 registry keys+types **150/150 MATCH**
  （`extract_pairs.py`，重定向到本 scratch 重跑；见 GATE-LOG §2 的附注：首次运行误用了
  delta 脚本内硬编码的写路径，复写了 delta scratch 的 `gates/exercises.json`，内容为同一
  来源的确定性抽取、事后核对 150 对且 Q73 为 up，未改生产文件；已改写路径重跑于本 scratch）。
- 逐项读 stem 核 key：填空/改写/翻译/完形/对话/纠错 78 项全部成句适配（含 Q73 `up` 补全
  `Speak ___: tell a teacher.` = speak up）；51 项 MCQ 每键均在选项内且与正文/图表/算术一致
  （254+162+19=435；254−218=36）；20 项配对逐题按印版释义顺序手验（P2 D、P3 C、P4 C、
  P5 C、P8 F 五组全对）；Q150 開放題无键可核。
- 观察（非缺陷，核心既有设计，与 delta 报告 §10 一致）：3 组重复题干为 P6 复习回访，
  键均适配：Q2/Q95（call）、Q5/Q96（changed）、Q6/Q12（January）。

## 已核对无问题（要点）

- 8 页逐页目检（print PDF 100 dpi 渲染 + web P1/P8 渲染）：版式干净，无溢出、重叠、压页脚、
  行首孤标点；图片与出处齐全；网版与印版视觉一致。
- 32 个奶油盒逐盒实测：盒内末基线余 +4.5 至 +92.4 px；+45 px 窗口内全部 BELOW-WINDOW 行
  均为 +24 至 +37 px 的下块栏头（已知假阳性带），无 +12..+18 px 整行漫出。
- 全部奶油框题 advance + 真墨实测合框（最紧 P1 NUMBERS：advance 余 +1.5 px，真墨余 +4.5 px）。
- P7 金句 8/8 逐字出自本期正文，页码标注正确；MODEL 82 词（与 KIT 一致）。
- ABSTRACT.txt：一行、498 B、繁体中文、无 ASCII 双引号、`宣布` 0×、`已宣佈` 1×，
  内容与本期事实一致（254 对 162、认证 11 月 10 日至 12 月 18 日、灰燼盃 4–1 回顾）。
- 印/网文字层逐页 token-multiset diff 0/0，逐页文本逐字节相同。

## 观察（非缺陷）

- O1 — P1 NUMBERS 框题极紧：advance 余 +1.5 px，真墨余 +4.5 px，框内，目视未碰线（与 proof1 O1 一致）。
- O2 — P2 AND YOU? 盒盒内余 +4.5 px，真墨底余 +3.9 px，末行中文、无降部，框内（与 proof1 O2 一致；
  canonical creambox desc-clear −1.5 px 为 0.30×字号降部估算，末行 `。` 无降部，真墨为准）。
- O3 — KIT §3 “P8 min font 13.5 pt”写的是 SVG 属性值而非渲染 pt；实测印版 P8 最小 10.12 pt，
  仍 ≥ §1.1 下限 9.75 pt，通过；仅 KIT 口径问题，非本版缺陷（与 proof1 O3 一致）。
- O4 — Q50 干扰项 A `10:20 a.m.`：proof1 已列为未独立核实的次要项（2025 赛程 listing 为 10:30），
  本轮未再展开；正确答案 C `12:30 p.m.` 与正文一致，不影响作答。
- O5 — D5 字体（只记录不判定）：print/web 各 43 个字体对象，全部 embedded+subset；
  `NotoSansCJKtc` 16 项、`NotoSansCJKsc` 0 项（见 GATE-LOG §8）。

## 建议下一步（报协调员定）

1. 本版可定稿入仓（按既有流程 commit/push，不在本复校职责内）。
2. 附注：首次运行 `extract_pairs.py` 时复写了 delta scratch 的 `gates/exercises.json`
   （同一来源的确定性抽取，内容已核对一致）；该文件可由 delta 方按需从源重建，无生产影响。
