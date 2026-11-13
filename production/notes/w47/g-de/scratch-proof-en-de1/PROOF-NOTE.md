# 校对笔记 — 2026-W47 en-de 第一轮独立复校（重建版，proof1）

- 版：`2026-w47-en-de`（英语目标语 × 德语读者版），VOL.4，8 版，150 题
- 校对员：独立复校（与 builder、re-fanout #2 builder、proof1/proof2 复校员不同人；本轮为 proof2 作废、核心改动后重建版的从头完整重校）
- 日期：2026-11-11（UTC 约 13:20–14:30）
- 依据：SOP §8 / §1.1、repo `AGENTS.md`、本版 `WEEKLY-KIT.md`、重建门禁记录 `scratch-fanout-en2/fanout/de/build-gates.log`（只作参考，全部结论本轮独立重核）
- 只检查、不改任何源码/成品；未碰 core-en、W43–W46、其他目标语家庭、tools/；未跑 insert.py、lint --write，未做任何 git 写操作（无 add/commit/push/reset/stash；开工探针 `git hash-object -w` 除外）。送审目录在本轮前后状态一致（`?? production/2026-w47/2026-w47-en-de/`，未跟踪）。

## 开工探针（双通，通过）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，成功。
- 笔记目录 `hidden_files/w47/scratch-proof-en-de1/` 真实写盘成功（探针文件已删）；`TMPDIR` 全程指向本笔记目录 `tmp/`；解释器一律 `tools/venv/bin/python`（Python 3.12.3）。
- `/dev/null` 开工时为普通文件（写成功）；中途服务重启后恢复为字符设备（`crw-rw-rw- 1, 3`），未影响核查。
- 中途一次服务重启（约 13:24–13:25 UTC）：第二批门禁日志已全部落盘、无损失；仅 `pdftoppm` 渲染中断（当时只出 p-1..p-4），重启后补跑 p-5..p-8 及全部网页版渲染。详见 GATE-LOG.md。

## 身份核对（先核身份，通过）

| 文件 | 字节 | SHA-256（实测完整串） | 与任务/KIT 登记 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-de.pdf` | 29,331,212 | `fe02ab1d9ba41e7a22651be02bda3612b66b54f2c521e12ab0ab5ca6797be5e1` | 一致 |
| `The-Lucerna-VOL4-en-de.web.pdf`（点式命名） | 2,414,462 | `19e166e03f28e813a8418189f20c1ddd31635f6621fbb182268e552c5302e6e5` | 一致 |
| `2026-w47-en-de.text.md` | 52,568 | `0aad0d2c8118bd6dab2f08170425f8ada595b5a397ba0d77511cffdd12c1e5e1` | 一致 |

两 PDF 均为 8 页、1462.5 × 2025 pt；网页版 < 7 MB。身份相符后开工。
本笔记目录下 `prev-round-old-build/` 为上一轮（旧版 SHA `6d91162f…` / `e8c67461…`）的 PROOF-NOTE/GATE-LOG/gates/render 原样归档，与本轮无关。

## 核心 en 未变（复核，通过）

- core-en 即 `core-en/`（实为 en-zh-cn 核心版）：印 PDF SHA `b484e007e6e0e29a78ea3f81c412e9c27c45a7c2b317a9a6081a2f63eb416566`，与核心 KIT 登记及核心 re-proof 记录（`scratch-reproof-core-en1`，结论 (a) 定稿）一致。
- 核心 8 个 SVG 实测 SHA 与 re-proof GATE-LOG 登记逐个一致：p1 `a9a8deaf76e61cb2`、p2 `979747160de01d67`、p3 `efb83ce76688554b`、p4 `aa6f395e4932ef8b`、p5 `a6a515cd5f734d0d`、p6 `7692256484f26289`、p7 `da908af644651793`、p8 `2f9a0334d70e07ba`。核心自定稿后未变。

## 结论：(a) 零问题，可定稿

本轮全量复校**零缺陷**。以下必验项逐项通过；其余全量项见后。按 SOP §8.4，本版达到定稿条件。

## 必验项逐项结果

### 1. de fix1：proof2 作废后重建 + 2 处 proof2 文案

- proof2（旧版 SHA `6f82363a…`，结论 (a)）因核心改动作废后，本版由 `scratch-fanout-en2` 重建（en re-fanout #2 DONE 10/10，未提交）。
- fix1 两处德语文案已带入重建并逐处核对原文与落版：
  - 第 747 行 `Erklärung | Win ist Gegenwart; won ist Vergangenheit (hat schon gewonnen) — in dieser Woche steht meist die Vergangenheit.`——text.md 有；SVG `p7-lang.svg` 内有换行分片 `Win ist` / `Gegenwart; won ist Vergangenheit (hat`（同句）；旧串 `(gewinnt immer wieder)` 在 text.md、8 个 SVG、印/网提取文本中均为 0 命中。
  - 第 775 行 `Erklärung | past simple = einfache Vergangenheit; unregelmäßige Verben muss man lernen.`——text.md 有；SVG 内有分片 `past simple =` / `einfache Vergangenheit; unregelmäßige`；旧串 `für Geschehenes` 全域 0 命中。
- D1（proof1 缺陷）回归：P7 8 条出处行全部 x=538.5（第 2 栏），y=1432.76 / 1539.23 / 1679.07 / 1818.91 / 1958.75 / 2131.96 / 2305.17 / 2545.12；第 3 栏流式首项为 `THE DRILLS　Übungen`（x=989.0，y=228.0）；末条金句末行 `Senate, and for governor in 36 states.”`（y=2490.75）与其出处行（y=2545.12，间距 54.37，与 fix1 版一致）紧邻。印刷 P7 与网页 P7 目视双重确认。

### 2. 本轮新修：P3 HAYMITCH 标题（旧 −39.1px）→ "Spiele"

- SVG 标题元素：`HAYMITCH'S GAMES　Spiele`（x=1457.5，y=893.0，23pt）；SVG advance 扫：317.5 px，余量 +87.0（18/18 标题全过，最紧为 ODD SOCKS +15.2）。
- 本轮 PIL 真墨重测（`gates/ink_check2.py`，卡片 PNG 1950×2700，与 SVG 坐标 1:1）：标题带最右真墨 x=1772，盒右缘 x=1862，**真墨 clearance +90.0 px**；带顶真墨 y=875，盒顶 y=856，+19.0 px。裁图 `render/crop-p3-haymitch.png` 目视确认标题居盒内、两侧留白充足。**通过**。

### 3. 紧处重测：P2 AND YOU? 末行基线 +5.0px（启发式 −1.0px 假警报）

- 典范 creambox 扫：AND YOU? 盒（y=1211，底 1544.9）末行 `Englisch an die Redaktion.` 基线 y=1539.85，clearance **+5.0 px**，desc-clear **−1.0 px**（0.30×20pt 启发式）。
- 本轮 PIL 真墨重测（同脚本，卡片 PNG）：该行深色真墨（lum<120）最低行 y=1543（x=1488–1493，即 `Englisch` 的 `g` 降部）；计入抗锯齿边缘（与米色差 >25）最低行 y=1544；米色实测底缘在 y=1544（米色占比 0.98）与 y=1545（0.00）之间。**真墨未越过盒底**：深色墨 +1 px（相对像素底缘），抗锯齿尾触及最后一行米色、未出盒。启发式按 6.0 px 估降部，实测降部约 4.2 px——**确为假警报，通过**。裁图 `render/crop-p2-andyou.png` 目视确认 `g` 降部完整在米色盒内，下方绿线分隔清晰。
- 附：32 个米色盒全部 inside-only clearance 为正（0 OVERFLOW）；次紧为 P1 SEARCHES +12.0（desc +6.3）、P2 DID YOU KNOW +14.3。AND YOU? 为全版最紧盒，已如上裁定。

### 4. Q39→a / Q40→d：Ashes 回顾口径逐题手验（题干、选项、键、注记四方一致）

- P3 匹配题（38–41）SVG 落版：题干 38. a tribute / 39. a mentor / 40. the arena / 41. a campmate；选项 a. "a person who teaches and guides you" / b. "a person chosen to take part in the Games" / c. "a person who lives with you in the jungle camp" / d. "the place where the Games are fought"。
- 语义：tribute→b（被选中的参赛者）、mentor→a（教导指引者）、arena→d（比赛场地）、campmate→c（同住营地者）。
- 四方一致：registry 键 38=b / 39=a / 40=d / 41=c；注记 `tribute = Teilnehmer b` / `mentor = Mentor a` / `arena = Arena d` / `campmate = Mitbewohner im Camp c`；text.md 答案行逐字一致；P8 印刷键提取 39=a、40=d。**四方一致，通过**。
- Ashes 回顾口径（重建同步项）同步手验：Q46 键 A、注 `Erster Ashes-Test 2025–26: Freitag, 21. November 2025, in Perth`（2025-11-21 经 `date -d` 核为周五）；Q52 `hosted`、Q55 `won`、Q125 `A (Australien hat die Ashes 2025–26 mit 4–1 gewonnen)`；text.md 中无 `Perth is winning!` / `second week in Perth` / `Ashes begin`，有 `Arsenal are winning!` 与 Ashes 回顾表述（`verify.log` 全 PASS，本轮重跑一致）。

## 全量复校结果（逐项，均已查）

1. **机械门全套自跑**（见 GATE-LOG.md，全部 RC=0）：
   - 瘦复制重建 `run.py`：RC=0，OVERFLOW / TOO WIDE 0 次，TOTAL 150，MODEL 82 词；再生 SVG 与送审 SVG **8/8 SHA 一致**（等效 freeze baseline，整树复制因配额风险沿用 proof1/proof2/fix1 同款做法）。
   - `occlusion_audit.py`：selftest OK，**0 flags**。
   - `p8.py extract`：core 与本版 noted set 均为 60/150，同一集合；`compare` **CLEAN**，missing=[]、extra_count=0、uncertain=[]；keydiff=[137, 138, 139, 140, 150]（预期内：德语翻译键 + 写作题短标签，与 W46 en-de 相同）。
   - `keycheck`：registry vs P8 提取 exact 149/150（唯一例外 Q150 短标签）；registry 键 vs core 145/150（仅 5 个读者语键）；Q38–41=[b,a,d,c]；Q46=A、Q52=hosted、Q55=won、Q82/83/84=B/C/A；提取键 150 条、registry 无缺失。
   - `freeze.py diff` vs core：P1 +32/−34、P2 +42/−54、P3 +25/−23、P4 +24/−22、P5 +24/−22、P6 +25/−21、P7 +64/−55、P8 +99/−99；新增 CJK 共 9 个、全部 U+3000。
   - 印/网文字层：各 47,406 字符，token 多重集差 0/0，逐页 byte-identical 8/8；网页版 2,414,462 字节 < 7 MB。
   - `check_s11.py`：**ALL PASS**；色集与 core 相同（19=19，无多无少）；徽章色 A2 #5c6e30 / B1 #46581f / B2 #37402f；P8 最小字号 13.5 pt（SVG）；P8 PDF 最小字号 10.12 pt ≥ 9.75 pt；Q113–120 选项级 [A2]、Q145–149 `Levels: 145–149 [A2]`、H WRITING `Schreiben [B1]` 均在版。
   - boxtitle 源扫 12/12、SVG 扫 18/18，0 超框。
   - creambox 典范扫：32 盒，0 OVERFLOW，全部 inside-only clearance 为正（见必验项 3）。
   - `verify_ed.py`：**VERIFY ALL PASS**。
2. **150 题逐题手验（三源一致 + 全文手读）**：registry 150 条（n 连续 1–150；分版 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；分级 A2 62 / B1 66 / B2 22）；registry 键/注记/级别/类型 vs text.md 答案附录 vs P8 印刷键提取——**0 不一致**（Q150 为与 core 相同的短标签例外）。text.md 全文 1305 行逐行读完：英文正文为冻结核心、无拼写/标点/语法误；德语讲解层通顺正确、无英文或中文讲解残留；逐题对照题面/原文/图表验算答案全部正确（含 Q84 33 of 35（20+13=33）、Q87 254+162+19=435、MODEL 82 词手数、Q100–107 drills 八词各用一次、Q141–144 b/c/d/a、Q145–149 row/film/popcorn/show/Friday、匹配题 P2 24=b/25=c/26=a/27=d、P3 38=b/39=a/40=d/41=c、P4 56=b/57=c/58=d/59=a、P5 74=d/75=a/76=b/77=c、P8 141=b/142=c/143=d/144=a）。
3. **8 版印刷版逐版目视**（从印刷 PDF 用 pdftoppm 全新渲染 110 dpi，非 builder card 图）：P1–P8 均读完；无溢出、重叠、压页脚、截断、豆腐块。**8 版网页版亦逐版目视**（`render/w-1.png`～`w-8.png`）：与印刷版逐页一致，无差异。
4. **金句 8 条逐字比对正文**：印刷提取文本 8/8 命中，出处页码全部正确（P1×2、P2、P3、P4、P5、P6×2）。P7 呈现顺序与 KIT §5 不同（proof1 已记），8 条齐全、文字逐字一致。
5. **禁词扫描**：印刷提取文本扫描 `W47 / 2026-w47 / 2026-W47 / cover / SOP / proofread / TODO / Lorem / placeholder / en-de / zh-cn / XXXX / TBD`，零命中。
6. **VOL**：P1 刊头 VOL.4；全部 8 页页脚 `ENGLISH WEEKLY VOL.4` + `Seite {n} von 8`；提取文本计数 VOL.4 ×12、VOL.5 ×8、VOL.3 ×3（与 proof1/proof2 一致；另 `VOL. 4` ×1 为 P1 刊头行本身）；VOL.5 8 处均为合法下期预告，VOL.3 3 处与 core 一致；无错印 VOL 号。
7. **徽章逐页计数**：LV 填充矩形逐页计数，与 core 逐页完全一致：P1 16、P2 15、P3 16、P4 16、P5 16、P6 19、P7 13、P8 23（= KIT 登记；60×30 芯片子集为 10/14/15/15/15/18/12/22，两版亦一致）。
8. **日期/星期**：全部日期逐个用 `date -d` 核验：11月3日周二、11月8日周日、11月9日周一、11月10日周二、11月16日周一、11月18日周三、11月19日周四、11月20日周五、11月21日周六、11月22日周日、11月26日周四、11月27日周五、12月1日周二，全部与正文一致；2025年11月21日周五（首场 Ashes 测试日）、2026年11月15日周日（ATP 总决赛开幕）亦核对无误。佐治亚决胜轮 12月1日（投票后 4 周）正确。
9. **孤儿标点全扫**：SVG 8 文件逐元素扫描（独行 。/独行右引号/独行 ：/– 均为 **0**）；印刷提取文本按行扫描独行标点亦为 0。
10. **U+2019**：8 个 SVG 全扫总数 **0**。可见文本零真实 CJK 字符（U+3000 表意空格 ×141 为家具分隔符；唯一其余 CJK 为非可见 SVG `<title>Lucerna 三色蛾</title>`，与 core 共有）。
11. **ABSTRACT.txt**：699 字节，德文单行，零 ASCII 双引号；含刊名、目标语名、A2–B2、题数与本期真实主题词。本轮相对旧版两处改动（`geprüften`→`verkündeten`；Ashes 条改为一年前回顾 4–1）均已核实；见观察项 2。
12. **与旧版逐页对比**（旧版 = fix1/proof2 版，SHA `6f82363a…`，备份于 `scratch-fanout-en2/backup/2026-w47-en-de/`）：110 dpi 像素差 P1 0.99%、P2 1.64%、P3 0.04%、P4 17.80%、P5 0.18%、P6 0.00%、P7 8.71%、P8 0.38%；SVG 可见文本差 P1 +8/−8、P2 +5/−5、P3 +1/−1、P4 +57/−41、P5 +3/−3、P6 +0/−0、P7 +9/−7、P8 +11/−11；registry 差恰 7 条（Q39/40、Q46、Q52、Q55、Q84、Q125）；text.md 差 120 行。**全部变化均可归因于重建修复处**（已宣布口径、Ashes 回顾重写、SENATE/SATURDAY 标题、SAY IT 面板、HAYMITCH 标题、Q39/40 换键、Q46/52/55/84/125），无意外变化。P6 像素与文本 0 变化（其唯一改动为 Q84 注记，落在 P8 答案区）。
13. **事实抽查**：沿用 proof1 已核实的公开来源结论（密西西比常规选举无决胜轮；Rousseau《Surprised!》1891 年；人名 Joseph Zada / Ralph Fiennes / Suzanne Collins / Henri Rousseau 等），本轮全文重读未发现矛盾的新表述；P4 回顾内数字自洽（首场 2025-11-21 周五、两日胜、八 wicket、系列 2025-11-21–2026-01-08、前三场珀斯/布里斯班/阿德莱德、第四场墨尔本、第五场悉尼、总分 4–1）。

## 观察项（单独列，不计缺陷；与 proof2 的 8 条一致，均未变；另加本轮 3 条）

1. **P2 A 组说明 “Ergänze die Sätze nach Datum und Uhrzeit.”**：本周 5 道题全部是日期、无钟点题；“und Uhrzeit”用词偏宽。但这是 core 中文说明的忠实翻译，且 W46 en-de 同款写法——属模板通用措辞，非本版新错。
2. **ABSTRACT.txt “am Samstag, 21. November, … das ATP-Finale in Turin”**：ATP 决赛在周日 11月22日，周六是半决赛；正文 P4/P6 写法正确。但该句式为核心版摘要的忠实翻译——已定稿的核心摘要原文即 “11 月 21 日周六英超回归与都灵 ATP 总决赛”（同款压缩日程列法，W46 en-de 摘要亦同例）。属核心冻结措辞，本版无权单方面改动；不计本版缺陷。
3. **引号方向**：德文引文用 «…»（法式/瑞士式）；标准德语常用 »…« 或 „…“。全版一致，非错（瑞士德语即用 «»）。
4. **“Anmerkung | Erklärung |” 双前缀**：P2/P3/P4/P5/P6/P7 的 Erklärung 框均有双前缀——KIT 已记为已确认的 W46 惯例，本轮核实为有意保留，非缺陷。
5. **P8 印刷答案注为节选**：150 条 registry 注中 83 条未印在 P8 答案区（只印键或短注）；core 同模式，属模板惯例，非缺失；键本身 150/150 齐全。
6. **版面留白**：P3 第 3 栏止于 1619、P4 第 3 栏止于 1713、P5 第 2 栏止于 597、P6 第 3 栏止于 1256——与 core 相同的模板 flow 行为，KIT 已记。
7. **P1-countries flow 余量仅 2pt**（2298/2300）：在底线内，无溢出；仅记一笔。
8. **freeze.py baseline 未能按原样跑**：整树复制涉磁盘配额风险，沿用 proof1/proof2/fix1 的等效做法（同一 tools/venv 解释器、同一构建源码的瘦复制，在笔记目录内重跑，不碰送审目录）并逐字节比对，8/8 一致。详见 GATE-LOG.md。
9. **P2 AND YOU? 为全版最紧盒**（见必验项 3）：基线 +5.0 px；真墨深色最低行距盒底 1 px，抗锯齿尾触及最后一行米色。实测在盒内、通过，但余量为全版最小。
10. **P7 不规则动词行跨栏**：`Irregular verbs in this issue: win → won, lose → lost, beat → beat, choose` 在第 1 栏底、`→ chose, run → ran.` 在第 2 栏顶——flow 正常分栏，无断句、无溢出，run.py 零警告，非缺陷（proof2 同记）。
11. **D5 字体（只记录、不计入判定）**：SVG `font-family` 统计：Newsreader 1022、Noto Sans CJK SC 655、Noto Serif CJK SC 27、DejaVu Sans 4、UnifrakturMaguntia 1；8 页双版渲染目视无豆腐块、无缺字形；U+2019 总数 0。

## 未核查项

- 无。本任务清单内各项均已核查（身份、核心未变、8 版印刷目视、8 版网页目视、全文重读、150 题三源+手验、8 金句、禁词、VOL、徽章、P8 字号、日期/星期、翻译层、U+2019、孤儿标点、全部机械门、印/网一致、run.py 瘦复制重跑、D1 回归、fix1 两处文案、HAYMITCH 标题真墨、AND YOU? 真墨、Q39/40 四方、旧版逐页对比、ABSTRACT、D5 字体记录）。

## 产物（本笔记目录）

- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`
- `gates/`：各门禁日志与 JSON、瘦复制重建（`rebuild/`，含 run.log、再生 SVG 8 个）、`ink_check2.py` + `ink_check2.log`（真墨重测）、`verify3.py` + `verify3.log` + `verify3.json`（三源键/孤儿标点/D1/fix1/金句/禁词/VOL/徽章/U+2019/Q38–41）、`oldnew-diff.log`、`svg-text-diff.log`
- `render/`：印刷版 `p-1.png`～`p-8.png`、网页版 `w-1.png`～`w-8.png`（110 dpi 全新渲染）、`crop-p2-andyou.png`、`crop-p3-haymitch.png`
- `prev-round-old-build/`：上一轮旧版校对文件原样归档
