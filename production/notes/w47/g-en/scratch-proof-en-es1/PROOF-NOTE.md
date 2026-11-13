# PROOF-NOTE — Lucerna Weekly 2026-W47 en-es · proof1 (independent, re-fanout #2 rebuild)

- Edition: `production/2026-w47/2026-w47-en-es/` (VOL.4, issue week Mon 2026-11-16–Sun 2026-11-22)
- Proofreader: proof1 (independent; not the builder). No production file was modified, rebuilt, committed or pushed. All build/tool runs happened in scratch copies; production objects re-hashed identical at the end of the round.
- Build under review: en re-fanout #2 (rebuilt from fixed core-en; uncommitted new directory).

## Conclusion: (a) — 定稿，零缺陷

No defect found. All mandatory gates pass; all 150 exercises hand-verified; all 8 pages visually inspected; the three defects of the previous build's proof1 (D1 Q39/Q40 swapped keys, D2 P2 Senate title overflow, D3 P6 HOW LONG title overflow) are all fixed and verified fixed at every source (source file, registry, text.md, printed SVG, P8 ANSWERS, web PDF text layer).

## Identity / SHA (PASS — match task values exactly)

| Object | Size | SHA-256 |
|---|---|---|
| Print `The-Lucerna-VOL4-en-es.pdf` | 29,331,231 B | `6341e239942338c547cfff31d96b4d6b0ad5b4ad811164380995959ea210b4a5` |
| Web `The-Lucerna-VOL4-en-es.web.pdf` | 2,414,448 B | `73356781d8c02970f18e592ef60189891db128eb38cabb04442e1919ee725b97` |
| `2026-w47-en-es.text.md` | 54,388 B | `2539179917d985e6da78c36be288946865af6b8aa8599c3e532e44e262921e2d` |
| `registry.json` (shipped, reference) | 22,306 B | `58a61af5a5bde13b5c54e825efa2d877937313b91bef4a98165a27383d216e1b` |

Both PDFs 8 pages, 1462.5×2025 pts. Probe first: `git -C ~/workspace/weekly-git hash-object -w --stdin` OK (`bf0a0bbf…`) + probe file written in this scratch dir (`probe2.txt`). TMPDIR pointed at this scratch dir's `tmp/`; `/tmp` never written; `/dev/null` present throughout. Interpreter: `tools/venv/bin/python` (Pillow 13.0.0 / FreeType 2.14.3) for every tool run.

## 必验项逐项结果

### 1. es fix1 — D3: HOW LONG? → "Duración" (PASS, 落版已核对)
- `2026-w47-en-es.text.md:729` — `HOW LONG? · Duración`.
- Shipped SVG `p6-deep.svg`: title text `HOW LONG?　Duración`, x=1457.5, baseline y=703; advance width 262.2 px, cream box x=1439.5–1862.0 → margin **+142.3 px** (svg boxtitle sweep, 18/18 fit, 0 overflows). Old build was 410.2 px, −5.7 over.
- Visual: new crop `crop-new-p6-deep-title.png` — title sits well inside the cream box with wide margin. Old-build crop (`prev-proof1-old-sha/crop-p6-howlong.png`) showed the final "o" of "mandato" straddling the edge; the new wording removes the overflow entirely.

### 2. es fix1 — Q40 note "arena = la arena d" (PASS, 落版已核对)
- `registry.json` n=40: `"key": "d", "note": "arena = la arena d"`.
- `content34.py:62` notes list: `tribute = un tributo b`, `mentor = un mentor a`, `arena = la arena d`, `campmate = un compañero de campamento c`.
- `2026-w47-en-es.text.md:1085`: `40. [A2] Emparejar — d (arena = la arena d)`.
- Printed P3 gloss in SVG: `the arena = la arena`. Printed P8 ANSWERS: `38. b · 39. a · 40. d · 41. c` (SVG text elements + web PDF text layer).
- Visible SVG text contains **0** occurrences of `estadio` / `stadio`.

### 3. Q40 arena 注释同类错核实 (PASS)
- 本版 Q40 arena 注释正确：`arena = la arena`（沙场/斗牛场），与 stadium 完全区分；全版可见文字中无 `estadio`/`stadio`。旧错（es/it 两版曾注成 estadio/stadio）已不在本版。
- 同版另一处 arena 释义一致：P3 gloss `the arena = la arena`；Q40 题干定义 d = "the place where the Games are fought"。

### 4. Q39→a / Q40→d 与 Ashes 回顾口径逐题手验 (PASS)
- Q39/Q40 四方一致（题干、选项、键、注记），逐源核对：
  - P3 印出版式（SVG 实测字母顺序）：terms 38. a tribute / 39. a mentor / 40. the arena / 41. a campmate；definitions a. "a person who teaches and guides you" / b. "a person chosen to take part in the Games" / c. "a person who lives with you in the jungle camp" / d. "the place where the Games are fought"。
  - 键：38→b（tribute），**39→a（mentor）**，**40→d（arena）**，41→c（campmate）—— registry、text.md 答案行、P8 ANSWERS 三源一致。
  - 注记与键一致：mentor = un mentor a；arena = la arena d。
- Ashes 回顾口径（2025–26 retrospective，取代旧版 preview 写法）逐题手验：
  - Q46 A — "The 2025–26 Ashes began on Friday, November 21, 2025, in Perth"；`date` 核实 2025-11-21 确为 Friday；注记 "El primer Test de las Ashes 2025–26 fue el viernes 21 de noviembre de 2025 en Perth"。
  - Q52 hosted — "Perth Stadium hosted its first Ashes Test in November 2025"（过去时，题干为过去语境）。
  - Q55 won — "Australia won the first Test by eight wickets"。
  - Q125 A — "Australia won the 2025–26 Ashes by 4–1"；注记 "Australia ganó las Ashes 2025–26 por 4–1"。
  - 旧版残留口径全清：text.md/registry/SVG 中无 `Perth is winning!`、`second week in Perth`、`Ashes begin`；P7 NEXT WEEK 为 "England's rematch waits until June 2027"。
  - 事实复核（2026-11-11 当日多源检索）：系列 4–1（ECB 官方声明、cricketcountry、ICC）；Perth 首 Test 两日内澳大利亚 8 wickets 获胜（cricket.com.au、AP）；"shortest Ashes Test since 1888"（多源）；墨尔本第 4 Test 英格兰 4 wickets 获胜、两日结束、近 15 年首胜（ICC、AP、Cricbuzz、cricketarchive）；悉尼第 5 Test 澳大利亚 5 wickets 获胜、系列 4–1；系列赛期 Nov 21, 2025–Jan 8, 2026（2025-11-21 Fri、2026-01-08 Thu 经 `date` 核实）。

## 全量门禁逐项结果（详见 GATE-LOG.md）

| 门禁 | 结果 |
|---|---|
| run.py（scratch 拷贝内重跑） | rc=0；OVERFLOW 0；TOO WIDE 0；TOTAL 150；MODEL 82；ALL DONE |
| freeze baseline（edition rebuild） | 8/8 SVGs byte-identical |
| freeze diff vs core-en | TOTAL added CJK 9，全部 U+3000；added/removed 逐条审过：仅家具、注释、指令词、页脚、重排的答案行，英文正文零改动；core P8 移除行亦为 `38. b · 39. a · 40. d · 41. c`（core 同样已修） |
| occlusion audit | 0 flags；0 NEW vs core；selftest OK（6 类 planted 全部触发） |
| p8 extract | 150/150；noted set 60/150，与 core set 完全相同 |
| p8 compare | CLEAN；missing=[]；extra=0；keydiff=[137, 138, 139, 140, 150]（预期：西语翻译题 + 开放题） |
| keycheck（p8 extract vs registry） | 150/150；唯一差异 Q150 截短为短标签 "Pregunta abierta"（已知 extractor 模式，与 core 相同） |
| text.md 答案 vs registry | 150/150 精确一致（键 + 级别），编号 1–150 连续 |
| creambox（canonical refined scan） | NO OVERFLOW；32 cream boxes；inside clearance +5.0 至 +92.4 px；最紧 P2 box y=1211（+5.0，仍为正） |
| boxtitle（source 12 + SVG 18） | 0 超框；最紧 P1 +20.4、P4 SATURDAY +86.7；P2 SENATE +33.6、P6 HOW LONG +142.3 |
| SAY IT phrase boxes（逐盒实测） | 3 盒全部 fit；见观察 O4（Feliz 行墨迹贴左沿，0 px 余量但不出框） |
| P8 最小字号 | SVG 13.5 pt；PDF 实测 10.12 pt；均 ≥ SOP §1.1 下限 9.75 pt；其余各页最小 15.5 pt |
| 印/网文字层一致 | 各 48,258 字符；token-multiset diff 0/0；逐页 8/8 byte-identical |
| check_s11（§1.1 + P8） | ALL PASS |
| verify_ed | VERIFY ALL PASS（Q39/Q40、Q46/Q52/Q55/Q125、Ashes 旧语清零、P8 字体、SVG 零 real CJK） |
| 孤儿标点全扫 | 独行 。/”/：/–/—/. /,/’/»/« 均为 0；行首孤儿闭标点、行尾孤儿开标点均为 0（SVG 全 <text> + text.md 全行） |
| 引号/内部字符串 | curly “ ” 82/82 平衡；直引号 ' 为 frozen core 惯例（43，core 45；curly ’ = 0 双方）；SOP/proofread/TODO/PLACEHOLDER/Lorem/XXX/cover = 0；real CJK（除 U+3000 外）= 0；U+3000 ×141；estadio/stadio = 0 |
| 日期/星期 | 全部核实（`date`，America/Toronto）：Nov 3 Tue、Nov 8 Sun、Nov 9 Mon、Nov 10 Tue、Nov 15 Sun、Nov 16 Mon、Nov 18 Wed、Nov 19 Thu、Nov 20 Fri、Nov 21 Sat、Nov 22 Sun、Nov 26 Thu、Nov 27 Fri、Dec 1 Tue、Dec 18 Fri、Jan 3 2027 Sun、Nov 21 2025 Fri、Jan 8 2026 Thu |
| 模型文 | "My Monday, November 16" = 82 词（alphanumeric-token 计，与 KIT/run.py 一致） |
| ABSTRACT.txt | 一行西班牙语，807 B，无 ASCII 双引号，含真实主题 + A2–B2 + 150 ejercicios |
| IN THIS ISSUE / 交叉引用 | p.2–p.8 与各版栏目一致；"Read page 6" → P6 地图；P2 "Page 3 has the story / page 4 the sport" 正确 |
| P7 golden sentences | 8/8 逐字见于正文，页码归属正确 |

## 150 题逐题手验（PASS，150/150）

- 全文 text.md 通读（P1–P8 正文 + 全部答案行）；registry 150 题编号连续，分页 10/17/18/18/18/18/12/39，级别 A2 62 / B1 66 / B2 22，与 KIT 一致。
- 每题键对照题干语义手验；配对题另对印版 SVG 字母顺序核对：P2 D 24–27（runoff→b、certify→c、turkey→a、Thanksgiving→d）、P3 C 38–41（见上）、P4 C 56–59（Test→b、tour→c、injury→d、break→a）、P5 C 74–77（bullying→d、speak up→a、right→b、silence→c）、P8 F 141–144（call→b、runoff→c、certify→d、midterm→a）。
- 图表题算术：254+162+19=435（Q87→C）；参议院 33/35 已宣布（Q84→A）；254−218=36（P7 "36 more than the majority"）。
- 对话 145–149（row / film / popcorn / show / Friday）与翻译 137–140（西语译文准确）逐一核对。
- Q109 诊所题已审定接受：原句 "The count continue after the vote."（wrong tense）→ key "The count continued after the vote."；过去时修正与诊所 "wrong tense" 定性及本期过去时框架一致，句子本身合乎语法，不计缺陷。

## 8 页逐页目视（PASS）

- 看过：`cards/p1-front.png` … `p8-test.png`（8 张印版卡片）+ 网版 `web-p1-1.png`、`web-p8-8.png`（72 dpi pdftoppm 渲染）。
- P1：masthead、VOL.4、日期、头条、数字盒、搜索榜、目录、简讯、Capitol 图 + 图注、快问——干净。
- P2：SENATE 标题已收进奶油盒（新裁切 `crop-new-p2-life-title.png` 证实）；SAY IT 三盒、火鸡图 + 图注、练习 A–D、页脚 "Página 2 de 8"——干净。
- P3：配对块 C（38–41 题干与 a–d 定义顺序正确）、gloss "the arena = la arena"、Rousseau 虎图 + 图注、HAYMITCH'S GAMES 盒、FIVE SENTENCES——干净。
- P4：Ashes 回顾正文、WHY PERTH 盒、SATURDAY 盒（标题收进框内）、W. G. Grace 照 + 图注、"Arsenal are winning!"、练习 A–D——干净。
- P5：Lawrence 1912 儿童图 + 图注、ODD SOCKS 盒、SPEAK UP 盒、FRIDAY'S WORDS、桥接行、练习 A–D——干净。
- P6：HOW LONG? 标题收进框内（新裁切 `crop-new-p6-deep-title.png` 证实）、图表数字、投票亭图 + 图注、FIFTY ELECTIONS——干净。
- P7：8 句 golden sentences 及页码归属、drills 100–107、error clinic 108–111、toolbox、Samuel Johnson 肖像 + 图注、读者来信、示例信、NEXT WEEK——干净。
- P8：cloze A、选择 B、阅读 C、句子 D、翻译 E、配对 F、对话 G、写作 H、MODEL 82 词、Library of Congress 图 + 图注、ANSWERS 块（目视可见 "38. b · 39. a · 40. d · 41. c"）——干净。
- 网版 P1/P8 与印版卡片版式一致（文字层 diff 0 已证）。

## 与旧版逐页对比（除重建修复处外无意外变化）

- 直接对比留存的旧版渲染：旧版网版 P1（`prev-proof1-old-sha/web-p1-1.png`）与 P8（`prev-proof1-old-sha/web-p8-8.png`）vs 新版同页。P1 差异仅 4 处，均为重建修复：SEARCHES #2 ashes→thanksgiving；kicker "Resultados verificados"→"Resultados anunciados"；导读 "the Ashes to Perth"→"a look back at last year's Ashes"；IN BRIEF ASHES "Sat, Nov 21: Australia v England, first Test, Perth."→"A year ago: Australia beat England 4–1 in the 2025–26 Ashes."。P8 差异仅 Ashes 回顾相关：Q125 题干改 4–1 问法；Q52 hosts→hosted；Q46 注记加日期 "el viernes 21 de noviembre de 2025"；Q39/Q40 键 d/a→a/d；Q125 注记改 "Australia ganó las Ashes 2025–26 por 4–1"。其余版式、文字、答案一字未动。
- P2/P6 标题新旧裁切对比：旧裁切（`prev-proof1-old-sha/crop-p2-senate.png`、`crop-p6-howlong.png`）示溢出；新裁切示标题收进框内（P2 余量 +33.6 px，P6 +142.3 px）。
- P2–P7 旧版整页渲染未留存（旧 scratch 仅存 P1/P8 网版渲染与 P2/P6 裁切），故该 6 页以 freeze-diff vs core-en（英文正文零改动）+ KIT 修复清单 + 全文重读三重覆盖；未发现超出修复清单的变化。

## Core-en 复核（核心未变，重建前后 SHA）

- core-en 同为未跟踪新目录；本轮记录其 content 源文件 SHA-256（供协调方比对）：`registry.json 05d412f9d55b1919a928ef4b6a5f5d50fe3f2630096802d48a201648a7fbc6f8`；`content34.py b61e3d5b59c85e0c5206a6462d8535558871407ddec0791d33e9f2cf9c8e863d`；`content12.py 64cb26a992cae28eb4ebcc10fe48063b018ee7b11791ecc135ce1369956c70ef`；`content56.py 5331c38d4d390e7ff1ea1d29cfea74acbb2d906fcfd37bce89a7c08c587f8eed`；`content7.py 8620bc505fdecf20eee0489fafba77b215377675b011924449fbb13232ea3d2f`；`content8.py bed28110ae61936067eea5fda97043b585e6028a478d0be68e10254ed796781d`。
- core-en `content34.py:61` keys `["b", "a", "d", "c"]`，registry Q39=a / Q40=d——已修复核心；es 与 core 键差异仅 5 个读者语键（137–140、150）。
- 本轮生产文件零改动：收尾复核三件 SHA 与任务值完全一致；`git status` 显示 en-es 与 core-en 仍为未跟踪新目录、无 M 项（其余 `M` 项为其他版本并行工作，与本版无关）。

## 观察项（非缺陷，不阻塞定稿）

- O1 — P5 桥接行 "Cada niño tiene derechos | Every child has rights = Cada niño tiene derechos." 西班牙语出现两次，读感冗余；与 core 同构（freeze-diff 证实 core 同句式），属 frozen core 写法。
- O2 — P7 golden sentence "A "call" is not the official result." 内层直引号；core-en P7 SVG 同字节 renders（`“A “call” is not the official result.”`），属 frozen core 排版惯例。
- O3 — P5 "D PRESENT CONTINUOUS" 小节头在第 2 栏底、题目在第 3 栏顶；模板分流，freeze-diff 证实 P5 英文正文与 core 一致。
- O4 — P2 SAY IT 第 3 盒 Feliz 行贴边：advance 宽 285.8 px vs 盒宽 280 px（两侧各超 2.9 px advance），但像素实测墨迹 x=1060–1338，恰在盒边 1060/1340 之内（`crop-sayit-feliz.png` 目视：¡ 在奶油左沿上、! 在框内，无溢出）。advance 超出为字形 side-bearing，非墨迹溢出；沿用旧版 proof1 同款裁定（clean）。其余两盒余量 +9.5 至 +45.9 px。
- O5 — Q109 诊所修正（见 150 题节）已审定接受。
- O6 — 旧版 proof1 三项未 source-verified 微断言中两项已随 Ashes 改写消失（"Day one is already sold out"、首球 "10:20 a.m. local — 2:20 a.m. in London" 均不在新版）；仅余 ATP 决赛 "not before 6 p.m. local time" 未 source-verified（未断言为假，仅未核实）。

## D5 字体（只记录、不计入判定）

按任务要求只记录：本轮在 edition KIT、core-en KIT 及可及的 fanout 记录中未找到 "D5 字体" 的定义文本；本轮亦未发现新增字体缺陷（§1.1 字体/配色检查全过：纸色 `#fbfaf6`、badge 色与 core 一致、masthead UnifrakturMaguntia、P8 最小字号 13.5 pt、SVG 零 real CJK）。D5 作为生产级待定项留待生产方处理，不计入本次定稿判定。

## 交付

工作目录 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-es1/`：
`PROOF-NOTE.md`（本文件）、`GATE-LOG.md`、门禁日志（`gates-run1.log`、`run.log`、`occlusion*.log`、`p8-*.log/json`、`freeze*.log/json`、`check_s11.log`、`boxtitle*.log`、`creambox-check.log`、`verify.log`、`printweb.log`、`keycheck.log`、`orphan.log`、`freeze-diff-strings.txt`、`sayit-check.log`）、复现产物（`freeze-final/`、`runcopy/`）、渲染与裁切（`web-p1-1.png`、`web-p8-8.png`、`crop-new-p2-life-title.png`、`crop-new-p6-deep-title.png`、`crop-sayit-feliz.png`）、旧版对照（`prev-proof1-old-sha/`，上一 build 的 proof1 全套文件原样归档）。
