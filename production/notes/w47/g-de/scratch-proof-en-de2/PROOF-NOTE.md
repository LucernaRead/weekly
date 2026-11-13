# 校对笔记 — 2026-W47 en-de 第二轮独立复校（delta 后，proof2）

- 版：`2026-w47-en-de`（英语目标语 × 德语读者版），VOL.4，8 版，150 题
- 校对员：第二轮独立复校（与 builder、delta 执行者、第一轮 proof1 复校员不同人）
- 日期：2026-11-11（UTC 约 15:56–17:30）
- 依据：仓库根 SOP.md §8 / §1.1、`~/workspace/weekly-git/AGENTS.md`、协调员 brief（`hidden_files/w47/briefs/brief-coordinator.md`）、本版 `WEEKLY-KIT.md`、proof1 笔记 `scratch-proof-en-de1/PROOF-NOTE.md`、delta 记录 `scratch-delta-en-de/DELTA-NOTE.md`——后两者只作参考，全部结论本轮独立重核、全部机械门本轮独立重跑。
- 只检查、不改任何生产文件；未碰 core-en、其他版、tools/；未跑 insert.py、lint --write，未做任何 git 写操作（无 add/commit/push/reset/stash；开工探针 `git hash-object -w` 除外）。复校前后送审文件 SHA 逐字节一致（见首尾两次核对）。
- 本笔记目录 `scratch-proof-en-de2/` 下的 `pre-delta/` 为今晨 08:22–09:05 旧一轮 proof2（修前 SHA `6f82363a…`）的原样归档，与本轮无关；本轮全部证据为 `gates/`、`render/`、`freeze-core/`、`freeze-ed/` 下的新文件。

## 开工探针（双通，通过）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，成功。
- 笔记目录真实写盘成功；`TMPDIR` 全程指向本笔记目录 `tmp/`；解释器一律 `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3，freeze 日志所印）；`/dev/null` 开工时为字符设备（`crw-rw-rw- 1, 3`）；`df -h`：`/home/hatch` 可用 61G，无配额问题；全程未遇 EDQUOT。

## 身份核对（先核身份，通过；复校结束时复核，SHA 未变）

| 文件 | 字节 | SHA-256（实测完整串） | 与任务先验 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-de.pdf` | 29,331,209 | `ae3b2e371d0dc8344853c106a697d958496dffb0170d3f6cb8599618209f1751` | 一致 |
| `The-Lucerna-VOL4-en-de.web.pdf` | 2,414,471 | `7117abe47962468fbf93068665f10da4cafaa2116ad368a907971bc9a94fa655` | 一致 |
| `2026-w47-en-de.text.md` | 52,565 | `c16f0e473f8017605fe8822a6d711134ad55b1708a0f22346ef2b4dd1f01d589` | 一致 |

两 PDF 均为 8 页、1462.5 × 2025 pt；网页版 2,414,471 B < 7 MB。身份相符后开工。

## Delta 范围独立核实（与 delta 声称逐项比对，全部相符）

- registry：修前快照（delta `pre/registry.json`）vs 现状 `diff` 恰 1 行：第 583 行 `"key": "speak"` → `"key": "up"`；其余 149 条一致。
- text.md：修前快照 vs 现状 `diff` 恰 1 行：第 1151 行 `73. [A2] Satzergänzung — speak (speak up = laut sagen)` → `… — up (…)`；52,568 → 52,565 B（少 3 B）。
- SVG：修前 SHA 清单（delta `pre/svg-sha-pre.txt`）vs 现状：仅 `p8-test.svg` 变化（`6b691560…` → `b04d052dd7d4b0eb35702e9766f681e2d6d318642d7da773aa18b14559d6f623`），p1–p7（含 P5）字节一致。**此为正确预期**：Q73 键只出现在 P8 答案区，P5 只印 `Speak ___` 空白与 `speak up` 注记，键本身从不上 P5——p5 不变不是异常。
- 旧键全域扫描：`73. speak` 在 registry、content56.py、text.md、8 个 SVG 中 0 命中（`speak up` 短语本身是正确的注记/正文用词，保留）。

## Q73 四源一致（本轮独立核实，全为 `up`）

| 源 | 证据 |
|---|---|
| 源码 | `content56.py:49`：`f.ex("A2", "Satzergänzung", "up", "speak up = laut sagen", "Speak ___: tell a teacher.", …)`；core-en `content56.py:49` 同为 `up`（注记中文 `speak up = 大声说出来`） |
| registry | `{"n": 73, "page": 5, "level": "A2", "type": "Satzergänzung", "key": "up", "note": "speak up = laut sagen"}` |
| text.md | L589 题干 `EXERCISE: Speak ___: tell a teacher.`；L1151 答案 `73. [A2] Satzergänzung — up (speak up = laut sagen)` |
| P8 印出键 | `svg/p8-test.svg` 含 `73. up`（grep 1 命中，`73. speak` 0 命中）；印刷 P8 提取文本含 `73. up`；印刷/网页 P8 渲染目视：答案区 Seite-5 行 `… 72. rights (right = Recht) · 73. up · 74. d · 75. a · 76. b …` |
| P5 题干 + 注释 | `svg/p5-youth.svg`：题干 `Speak ___: tell a teacher.`；注释框 `Mobbing · to speak up = laut sagen · a …`；印刷/网页 P5 渲染目视：B 组第 73 题 `Speak ___: tell a teacher.` 正常落版 |

语义：`Speak up: tell a teacher.`——speak up 为固定短语动词，键 `up` 填入成句，正确。

## 结论：(a) 零缺陷，可定稿

本轮全量复校**零缺陷**。以下逐项通过；按 SOP §8.4（"一整轮全量校对零问题才算定稿"），本版达到定稿条件。proof1 结论 (a) PROVISIONAL 所待的 delta 后复校至此完成。

## 全量复校结果（逐项，均已查）

1. **8 版印刷版逐版目视**（从印刷 PDF 用 pdftoppm 全新渲染 110 dpi，`render/p--1.png`～`p--8.png`，非 builder card 图）：P1–P8 均读完；无溢出、重叠、压页脚、截断、豆腐块、孤行。**8 版网页版亦逐版目视**（`render/w--1.png`～`w--8.png`）：与印刷版逐页一致，无差异；P5 Q73 题干、P8 `73. up` 在网页版亦正常落版。
2. **全文重读**（`2026-w47-en-de.text.md` 全文 1307 行，P1–P8 正文 + 练习题面 + 150 条答案附录逐行读完）：英文正文拼写/标点/语法无误；德语讲解层通顺正确；无英文/中文讲解残留；讲解层所注之词均真实出现在正文里；金句 8 条逐字见于正文（脚本核对印刷提取文本 8/8 命中），出处页码全部正确（P1×2、P2、P3、P4、P5、P6×2）。
3. **150 题逐题手核 key-vs-stem**（Q73 教训：三源一致也可能同错；每键读 stem 看 key 填入是否成句）：
   - 填空/改写 50 题：用 recording-stub 直跑 content 文件配对（`gates/pair_stems.py` 新跑，150 对全部配出、与 registry 键 0 不一致），50 题逐题手验全部成句——含 Q73 `up` / `Speak ___: tell a teacher.`、Q70 `silence` / `Break the ___`、Q79 `Children are speaking up this week.` / `Children (speak) up this week.`、Q13 `1` / `December ___`、Q14 `Thursday` / `Thanksgiving is on ___, November 26`（2026-11-26 经 `date -d` 核为周四）、Q107 `win` / `“Democrats ___ the House” is a headline`。已知重复 Q2/Q95、Q5/Q96、Q6/Q12 为跨版有意重复（同题干同键，P1→P6 难度复现），非缺陷。
   - 其余 100 题逐题对照题面/原文/图表验算：选择题字母全部正确（含 P1 闪电问答 7=B/8=A/9=C/10=C；P2 20=B/21=C/22=A/23=B；P3 28=B/29=A/30=C/31=B/32=A/33=C；P4 46=A/47=C/48=B/49=A/50=C/51=B；P5 64=B/65=A/66=C/67=B/68=A/69=C；P6 图表 82=B/83=C/84=A/85=B/86=A/87=C（254+162+19=435）、理解 88=B/89=A/90=C/91=B/92=A/93=C；P7  drills 100=won/101=more/102=lost/103=will/104=published/105=whether/106=chose/107=win（词库 8 词各用一次）、纠错 108–111 改正句均正确；P8 填空 112=Tuesday/113=call/114=continues/115=will meet/116=writes/117=will certify/118=wears/119=will watch、选择 120=B/121=A/122=C/123=B/124=A/125=A/126=B/127=A/128=C、阅读 129=B/130=A/131=C/132=B、改写 133=will meet/134=won/135=more/136=whether、对话 145=row/146=film/147=popcorn/148=show/149=Friday）；匹配题字母映射逐项核对：P2 24=b/25=c/26=a/27=d、P3 38=b/39=a/40=d/41=c、P4 56=b/57=c/58=d/59=a、P5 74=d/75=a/76=b/77=c、P8 141=b/142=c/143=d/144=a；翻译题 137–140 德译准确（`Die Demokraten haben das Repräsentantenhaus und den Senat gewonnen.` / `Die Auszählung geht weiter.` / `Der neue Kongress tagt ab Januar 2027.` / `Brich das Schweigen.`）；Q150 为开放题短标签（与 core 相同的例外）。
   - 三源机械核对（`verify3.py` 新跑）：text.md 答案 150 条 vs registry vs P8 印刷键提取——**0 不一致**（Q150 短标签例外）；registry 150 条，`n` 连续 1–150；分版 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；分级 A2 62 / B1 66 / B2 22。
4. **P7 D1 回归**：8 条出处行全部 x=538.5（第 2 栏），y=1432.76 / 1539.23 / 1679.07 / 1818.91 / 1958.75 / 2131.96 / 2305.17 / 2545.12；末条金句末行 `Senate, and for governor in 36 states.”`（y=2490.75）与其出处行（y=2545.12）紧邻；第 3 栏顶为 `THE DRILLS　Übungen`（x=989.0，y=228.0）。印刷 P7 与网页 P7 目视双重确认。**D1 已修，无回归。**
5. **fix1 两处文案**：text.md 第 747 行 `Erklärung | Win ist Gegenwart; won ist Vergangenheit (hat schon gewonnen) — …`、第 775 行 `Erklärung | past simple = einfache Vergangenheit; unregelmäßige Verben muss man lernen.`；旧串 `(gewinnt immer wieder)`、`für Geschehenes` 在 text.md、8 个 SVG、印/网提取文本中均为 0 命中。
6. **核心未变**：core-en 8 个 SVG SHA 与 proof1 登记逐个一致（p1 `a9a8deaf76e61cb2`、p2 `979747160de01d67`、p3 `efb83ce76688554b`、p4 `aa6f395e4932ef8b`、p5 `a6a515cd5f734d0d`、p6 `7692256484f26289`、p7 `da908af644651793`）；p8 为 fix2 后的 `1066c475da8afe7e`（Q73 `speak`→`up` 所致，预期内）；freeze-core 运行前后重哈希确认核心 SVG 未被运行改动。
7. **禁词扫描**：印刷提取文本扫描 `W47 / 2026-w47 / 2026-W47 / cover / SOP / proofread / TODO / Lorem / placeholder / en-de / zh-cn / XXXX / TBD`，零命中。
8. **VOL**：P1 刊头 VOL.4；全部 8 页页脚 `Seite {n} von 8` + `ENGLISH WEEKLY VOL.4`；提取文本计数 VOL.4 ×12、VOL.5 ×8、VOL.3 ×3；VOL.5 8 处均为合法下期预告，VOL.3 3 处与 core 一致（“VOL.3 promised real letters…”）；无错印 VOL 号。
9. **徽章逐页计数**：60×30 芯片与 LV 填充矩形逐页计数，与 core 逐页完全一致：P1 16、P2 15、P3 16、P4 16、P5 16、P6 19、P7 13、P8 23。
10. **P8 最小字号**：SVG font-size 最小值 13.5pt；PDF 最小字号 10.12pt（`verify_ed.py` 实测），均 ≥ 9.75pt。
11. **日期/星期**：全部日期逐个用 `date -d` 核验：11月3日周二、11月8日周日、11月9日周一、11月10日周二、11月16日周一、11月18日周三、11月19日周四、11月20日周五、11月21日周六、11月22日周日、11月26日周四、11月27日周五、12月1日周二，全部与正文一致；2025年11月21日周五（首场 Ashes 测试日）亦核对无误。佐治亚决胜轮 12月1日（投票后 4 周）正确。
12. **孤儿标点全扫**：SVG 8 文件逐元素扫描（独行 。/独行右引号/独行 ：/– 均为 **0**）；印刷提取文本按行扫描独行标点亦为 0。
13. **U+2019 / CJK**：8 个 SVG 全扫 U+2019 总数 **0**；可见文本零真实 CJK 字符（U+3000 表意空格 ×141 为家具分隔符；唯一其余 CJK 为非可见 SVG `<title>Lucerna 三色蛾</title>`，与 core 共有）。
14. **盒标题溢出（PIL 真实墨迹量）**：源扫 12/12 fit（最紧 ODD SOCKS +15.2）；SVG 扫 21/21 fit（最紧 P2 `The new Congress meets in January.` +8.8，加粗首行）；P3 HAYMITCH 标题真墨重测：最右真墨 x=1772，盒右缘 x=1862，**真墨 clearance +90.0 px**；带顶真墨 y=875，盒顶 y=856，+19.0 px。裁图 `render/crop-p3-haymitch.png` 目视确认标题居盒内、两侧留白充足。
15. **MODEL 字数**：H 写作范文 82 词（不含独立破折号），在 80–100 词任务范围内。
16. **ABSTRACT.txt**：699 字节，德文单行，零 ASCII 双引号；含刊名、目标语名、A2–B2、题数与本期真实主题词。
17. **D5 字体（只记录，不判定）**：8 个 SVG 的 `<text>` 元素按 font-family 计数：Newsreader 1022 / Noto Sans CJK SC 655 / Noto Serif CJK SC 27 / DejaVu Sans 4 / UnifrakturMaguntia 1；合计 1709。与 proof1/delta 数字完全一致（本次改动不涉及字体；拉丁读者解释层在 Noto Sans CJK SC 是已知待用户裁定的全线问题，不作本版缺陷）。

## 观察项（单独列，不计缺陷；本轮亲自核实）

1. **P2 AND YOU? 为全版最紧盒**：基线 clearance +5.0 px，desc-clear −1.0 px（0.30×20pt 启发式）。本轮 PIL 真墨重测（`gates/ink_check2.py`，卡片 PNG 1950×2700，与 SVG 坐标 1:1）：该行深色真墨（lum<120）最低行 y=1543（`Englisch` 的 `g` 降部）；米色实测底缘在 y=1544（米色占比 0.98）与 y=1545（0.00）之间。**真墨未越过盒底**：深色墨 +1 px（相对像素底缘），抗锯齿尾触及最后一行米色、未出盒。启发式按 6.0 px 估降部，实测降部约 4.2 px——**确为假警报，通过**。裁图 `render/crop-p2-andyou.png` 目视确认 `g` 降部完整在米色盒内，下方绿线分隔清晰。
2. **ABSTRACT.txt “am Samstag, 21. November, … das ATP-Finale in Turin”**：ATP 决赛在周日 11月22日，周六是半决赛；正文 P4/P6 写法正确。但该句式为核心版摘要的忠实翻译——已定稿的核心摘要原文同款压缩日程列法（W46 en-de 摘要亦同例）。属核心冻结措辞，本版无权单方面改动；不计本版缺陷。
3. **引号方向**：德文引文用 «…»（法式/瑞士式）；标准德语常用 »…« 或 „…“。全版一致，非错（瑞士德语即用 «»）。
4. **“Anmerkung | Erklärung |” 双前缀**：P2/P3/P4/P5/P6/P7 的 Erklärung 框均有双前缀——KIT 已记为已确认的 W46 惯例，本轮渲染目视核实为有意保留，非缺陷。
5. **P8 印刷答案注为节选**：150 条 registry 注中 83 条未印在 P8 答案区（只印键或短注）；core 同模式，属模板惯例，非缺失；键本身 150/150 齐全。
6. **版面留白**：P3 第 3 栏止于 1619、P4 第 3 栏止于 1713、P5 第 2 栏止于 597、P6 第 3 栏止于 1256——与 core 相同的模板 flow 行为，KIT 已记。
7. **P7 不规则动词行跨栏**：`Irregular verbs in this issue: win → won, lose → lost, beat → beat, choose` 在第 1 栏底、`→ chose, run → ran.` 在第 2 栏顶——flow 正常分栏，无断句、无溢出，非缺陷。

## 缺陷清单

无。本轮零缺陷。

## 证据文件（本笔记目录内）

- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`（机械门逐条日志）
- `gates/`：occlusion / p8-extract / p8-extract-core / p8-compare / keycheck / check_s11 / verify / verify3 (+json) / printweb / freeze-diff (+json) / freeze-baseline-core / freeze-baseline-ed / creambox-all / sweep-boxes / ink_check2 / fill-rewrite (+json) 各门日志与 JSON；各门所用脚本副本（`check_s11.py`、`verify_ed.py`、`keycheck_ed.py`、`verify3.py`、`pair_stems.py`、`printweb.py`、`sweep_boxes.py`、`ink_check2.py`、`boxtitle.py`——其中 keycheck/verify3/ink_check2/pair_stems 仅把写出路径由 delta scratch 改指本目录，未改核查逻辑）；`make_textmd_delta.py` 存于本目录根（pair_stems.py 的 stub 来源）
- `render/`：印刷 p--1..p--8、网页 w--1..w--8（pdftoppm 110 dpi 全新渲染）+ 裁图 crop-p2-andyou.png、crop-p3-haymitch.png
- `freeze-core/`、`freeze-ed/`：两口径 freeze baseline 运行产物与日志
- `pre-delta/`：今晨旧一轮 proof2 原样归档（与本轮无关）
