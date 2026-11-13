# PROOF-NOTE — 2026-W47 en-fr 独立复校 proof2（Q73 delta 重建版，2026-11-11）

- 版：`production/2026-w47/2026-w47-en-fr/`（Q73 delta 重建版）。
- 复校员：独立 proof2，与建版者（delta）不是同一人。只复校这一版，未改任何生产文件、未重建交付物（除 scratch 副本内 `run.py` 复跑与网 PDF 重渲对比）、未 commit、未 push、未动核心、其他版、tools/。中间件全在 `scratch-proof-en-fr2/`（`TMPDIR=<scratch>/tmp`，解释器一律 `tools/venv/bin/python`，未写 /tmp，未删他人文件）。
- 探针：`/dev/null` 存在；`git hash-object -w` 在仓库内成功（`9daeafb9…`）；scratch 写文件成功（`probe.txt`）。
- 先读：delta 记录 `scratch-delta-en-fr/DELTA-NOTE.md` + 本版 proof1 `scratch-proof-en-fr1/PROOF-NOTE.md` / `GATE-LOG.md`。

## 对象核对（开工与收工两次 SHA 复核一致，生产文件未变）

| 文件 | 字节 | SHA-256（盘上实测） | 与任务书修后值 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-fr.pdf`（印） | 29,330,985 | `0b4fded62123ee39ec97b8d4b7abd9c5c8e1f41184500a0aa76c25ee2678c693` | 一致 ✓ |
| `The-Lucerna-VOL4-en-fr.web.pdf`（网） | 2,413,667 | `2d20b93df8f88596e1eec7915b7a2ea3d103176061cc35e7b24009c32e95a733` | 一致 ✓ |
| `2026-w47-en-fr.text.md` | 53,806 | `ed8fd9ec8b706dfe961b5638fefe4e857f6493a01a312d2a7e8fdc0f0f0ff213` | 一致 ✓ |

两 PDF 各 8 页（印 1462.5×2025 pt；网同）。另：`registry.json` `41dc6d5b…92ace`、`content56.py` `86383c4e…251e`，与 DELTA-NOTE 记录一致。

## 结论：(a) 定稿

**本轮全量复校零缺陷。** Delta 只改 Q73 一键，四源同步为 `up`；其余全部内容与 proof1 (a) 定稿一致，变化范围仅 P8 一页。缺陷清单：空。**确认 en-fr 可定稿。**

## Q73 四源一致（修后，全为 up）

| 源 | 实测 |
|---|---|
| registry | Q73 `{n: 73, page: 5, level: A2, type: Compléter, key: 'up', note: 'speak up = parler franchement'}`（`registry.json:583`） |
| text.md | :1151 `73. [A2] Compléter — up (speak up = parler franchement)`；:589 题干 `Speak ___: tell a teacher.` 不变 |
| P8 印出键 | `svg/p8-test.svg` `73. up`；印/网/重渲网 PDF 文字层各含 `73. up` ×1 |
| P5 题干 + 注释 | `svg/p5-youth.svg` `Speak ___: tell a teacher.`；Note 盒 `speak up = parler franchement`；填入后 `Speak up: tell a teacher.` 语法正确 |
| 残留 | `73. speak` 在 registry / text.md / P8 SVG / 印/网文字层均为 **0 命中**；`"key": "speak"` 全版 0 命中 |

## Delta 变化范围（与修前逐项 diff，恰好一处）

- registry diff（vs `scratch-delta-en-fr/registry-pre.json`）：恰好 1 行，`583c583` `"key": "speak"` → `"key": "up"`（`diff-registry.txt`）。
- text.md diff（vs `text-pre.md`）：恰好 1 行，`1151c1151` 同上（`diff-textmd.txt`）。
- SVG diff（vs `svg-pre.sha`）：8 页中仅 `p8-test.svg` 变化（`4978f960…` → `34acf55d…`）；p1–p7 哈希与修前逐字节一致，**p5 不变是正确且预期的**（键只出现在 P8 答案页，不出现在 P5 题干页）（`diff-svg.txt`、`svg-now.sha`）。
- `content56.py` diff：`49c49`，仅 key `speak` → `up`（与 delta 记录一致，`diff-content56.txt`）。

## 全量门禁（逐门独立重跑，详见 GATE-LOG）

| 门 | 结果 |
|---|---|
| run.py（scratch 副本复跑） | RC=0，0 OVERFLOW / 0 TOO WIDE，TOTAL 150，MODEL 82；重建 8 页 SVG 与交付 SVG 逐字节一致 |
| occlusion 审计（真实命令） | **0 flags**，RC=0；自检 OK（6 类阳性对照全触发，干净对照静默） |
| p8 extract | **150/150**，noted set 60/150（与核心 noted 集相同） |
| p8 compare | **CLEAN**，missing=[] extra_count=0 uncertain=[]；keydiff=[137, 138, 139, 140, 150]（预期内，与 proof1 同） |
| p8 extract vs registry | 149/150 exact，仅 #150 短标例外（registry 长式 vs 提取 `Tâche ouverte`，与核心同 pattern） |
| registry keys vs core | 145/150 相同；差异仅 137–140、150（读者语键，预期内）；Q38–41 = b/a/d/c；Q125=A，Q46=A，Q52=hosted，Q55=won，Q82/83/84=B/C/A |
| freeze baseline | **8/8 SVGs byte-identical**（`--build` = 版自己的构建目录；p8 `34acf55d…` 为修后值） |
| freeze baseline（core 只读对照） | **8/8 SVGs byte-identical**；核心 8 页 SVG 哈希与 delta 快照 8/8 一致，核心未动 |
| freeze diff vs core | p1 +34/−34、p2 +43/−54、p3 +26/−23、p4 +26/−22、p5 +25/−22、p6 +26/−21、p7 +66/−55、p8 +103/−98；新增 CJK 共 9 个，全为 U+3000（与 proof1/delta 一致） |
| 印/网文字层 | pdftotext -layout 印=网=108,899 B；无 layout 印=网=49,436 B；逐页 byte-identical 8/8；token 多重集差 0/0；网 < 7 MB |
| 网 PDF 重渲（仅 scratch 副本） | RC=0，2,413,678 B（与交付 2,413,667 B 相差 11 B，为逐次浮动，预期内）；文字层与印版及交付网版逐字节一致 |
| P8 最小字号 | PDF 有效最小 **10.12 pt**（P8 答案键块）；其余页最小 11.62 pt；印/网逐页 span 数与最小值完全一致；SVG 属性最小 13.5 pt；均 ≥ §1.1 下限 9.75 pt |
| §1.1 / P8 检查 | `check_s11.py fr` RC=0，**ALL §1.1/P8 CHECKS PASS** |
| creambox（原版） | RC=0；23 行负值全为 proof1 已裁定的假阳性集（-24.0 ×1、-35.5 ×9、-36.0 ×2、-37.0 ×11）；SEARCHES 末基线 **+12.0**，DID YOU KNOW **+14.3** |
| creambox_check（精炼版） | **NO OVERFLOW，RC=0**；P8 MODEL 盒 +92.4；核心对照同样 NO OVERFLOW |
| boxtitle | occlusion BOXTITLE 类 0 flags；`check_s11.py fr` RC=0 |
| 孤儿标点 | SVG `<text>` 独行标点 **0**；text.md 独行标点行 **0** |
| 字符/引号/禁词 | “ 82 / ” 82 成对；U+2019 0；ASCII 撇号 73；U+00B7 282；U+3000 141；可见文字真实 CJK 0；`Note \| Note \|` 0；禁词 0；`encore changer` 0（合法 `encore` 仍 2 处：Q138 注、P7 读者来信注） |
| VOL 计数 | VOL.4 12、VOL.5 8、VOL.3 3，逐页与 proof1 一致 |
| ABSTRACT.txt | 775 B，一行 + 结尾换行，无 ASCII 双引号（未动） |
| 像素对比（vs delta 渲染） | P1–P8 **0 差异像素**（同 PDF 正常）；网/印视觉差仅 JPEG 重压 |

## 150 题逐题手验（text.md 1305 行全文通读 + SVG 题面核对 + registry/extract 三源对照）

- 编号连续 1–150；每页 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；级别 A2 62 / B1 66 / B2 22；附录自 ANSWERS 节起恰好 150 行（全文 `N. [` 共 158 行，另 8 行为 P8 完形选项行 112–119，与 proof1 同 pattern）。
- 44 项 `___` 填空/改写逐项填入核对（`fillcheck.log`）：44/44 合理，无问题。Q73 `Speak ___: tell a teacher.` + `up` → `Speak up: tell a teacher.`（注 `speak up = parler franchement` 一致）；Q70 `Break the silence: speak up about bullying.`；Q79 `Children are speaking up this week.`；Q52 `hosted`、Q55 `won`。
- 完形 Q112–119 逐项对段落原文核对（`content8.py` 段落 + 三选项）：Tuesday / call / continues / will meet / writes / will certify / wears / will watch 逐项唯一正确（112：11 月 3 日为周二；113：call 为新闻机构的判断；114：counting continues 现在时；115：January 将来时；116：Maya writes 三单；117：by Dec 18 将来时；118：she wears 三单；119：Friday 将来时）。
- 五组配对题逐组对 SVG 渲染核对：P2（24b/25c/26a/27d ✓）、P3（38b、39a、40d、41c ✓；选项 a. teaches and guides / b. chosen to take part / c. lives with you in the jungle camp / d. place where the Games are fought）、P4（56b/57c/58d/59a ✓）、P5（74d/75a/76b/77c ✓）、P8（141b/142c/143d/144a ✓）。
- 其余：Q7 B 254、Q9 C 218、Q46 A（2025-11-21 周五珀斯）、Q47 C 背伤、Q48 B、Q49 A 2010–11、Q50 C 12:30、Q51 B 膝伤、Q53 lasts、Q54 eight、Q83 C 19、Q84 A 33/35、Q87 C 435（254+162+19）、Q97 takes、Q100–107 演练（won/more/lost/will/published/whether/chose/win）、Q108–111 改错（won / continued / more than / whether）、Q120–128 选择（B/A/C/B/A/A/B/A/C）、Q129–132 阅读（B/A/C/B）、Q133–136 句型（will meet/won/more/whether）、Q137–140 翻译（法译准确）、Q145–149 对话（row/film/popcorn/show/Friday）、Q150 开放写作；模型文 82 词。
- 金句：P7 8 句逐字出自本期正文，页码标注（P1/P2/P3/P4/P5/P6）正确。

## 8 页逐页目视（印版 P1–P8 全页 + 网版 P1/P8，72 dpi）

- 无溢出、重叠、压页脚、图片与出处问题；页脚 `Page N sur 8` 全 8 页正确；刊头/徽章/栏目条齐全；P8 答案块在页内，未压页脚；网版与印版视觉一致。
- P1：SEARCHES 盒末行在盒内；IN BRIEF Ashes 为回顾口径；LIGHTNING QUIZ Q7–10 齐全；国会大厦图 + 出处齐全。
- P2：DID YOU KNOW 盒末行 `November 3.` 在盒内；AND YOU? 盒、SAY IT 三句、火鸡图 + 出处齐全。
- P3：Rousseau 图 + 出处、COMING SOON 盒、配对题 a–d 选项齐全。
- P4：回顾版全文 + W.G. Grace 图 + 出处、`SATURDAY, NOV 21` 盒、`Arsenal are winning!` 正常；栏底留白为模板流行为（与核心同）。
- P5：SPEAK UP / FRIDAY'S WORDS / THE JUNGLE, TOO 正常；Q73 题干只印 `Speak ___` 空白（键不在此页，正确）；Lawrence 儿童图 + 出处齐全；D 节头在栏底、题在下栏为模板流行为（与核心同）。
- P6：READ THE CHART（`chiffres annoncés`）+ 练习选票 ☐ + 投票亭图 + 出处齐全。
- P7：工具盒 B2 无 `encore`（`Personne ne sait si le décompte va changer.`）；三处旧超宽节头在栏内；NEXT WEEK 为 June 2027 口径；Johnson 图 + 出处齐全；“Irregular verbs in this issue: win →” 跨栏接续为模板行为（与核心同）。
- P8：答案键块 1–150 齐全，`73. up` 在页内（答案块 Page 5 行）；模型文 82 词在框内；H WRITING `Écriture [B1]`、Main Reading Room 图 + 出处齐全。

## 仅记录、不计入判定

- **D5 字体（生产级待定项）**：P8 渲染有效最小字号 10.12 pt，对应 SVG 属性值 13.5 pt（KIT “13.5 pt” 写的是属性值而非渲染有效值，因答案键块在 0.75 缩放组内）；10.12 pt 仍 ≥ §1.1 下限 9.75 pt，与 proof1/delta 同值，未变。仅记录，不计入本轮判定。

## 已核对无问题（要点，沿用 proof1，内容未动）

- proof1 的 D1–D5 修复均在位：Q39→a / Q40→d（印版文字层 `39. a` ×2、`39. d` 0、`40. d` ×1）；P1 SEARCHES +12.0、P2 DID YOU KNOW +14.3；P7 工具盒 B2 无 `encore`；`encore changer` 全版 0 命中。
- 外部事实：选举数、正文 Ashes 回顾、Hunger Games、I'm a Celebrity、Anti-Bullying Week、ATP 总决赛、英超第 11 轮、NFL 第 11 周与 proof1/r1 核实一致，本轮未改动，Q73 delta 不涉及。
- 读者来信：P7 读者来信栏明示截稿时无来信、VOL.5 起登真实来信，与 F-MAIL 规则一致，未编造来信。
- 保留的模板行为（与核心同，非缺陷）：P4/P5/P6 栏底留白；P5 D 节头栏底、题下栏；P7 不规则动词表跨栏接续；P1 数字盒英文术语 + 法语括号注释；Q90 答案注 `Deux sièges du Sénat restent à confirmer`（指待确认的未宣布选区，与 D4 所指不同义）。

## 复校方法备注（非缺陷）

- `scan.py` 从 proof1 原样复制时其 `S` 路径仍指向 `scratch-proof-en-fr1`，首跑误读 proof1 旧版 `p8-extract.json`，报出 Q73 一条假 mismatch（旧 extract 键 `speak` vs 新 registry `up`）；已将路径改成本 scratch 重跑，结果仅余 #150 已知例外（见 GATE-LOG）。该假 mismatch 为复校员脚本路径问题，不反映版面问题。
- 首版 `run.py` 副本只拷了 content/registry 文件，漏 `svglib.py` 致 `ModuleNotFoundError`（复校员操作失误）；改拷整版（除 cards/PDF/MD/JSON）后一次通过，RC=0。生产文件未受影响。
- 首版 min-font 检查用 heredoc 传脚本给 `python -` 时进程无输出挂起逾 7 分钟，已杀掉（SIGTERM），改把脚本写成 `minfont.py` 文件再跑，46 秒完成，RC=0。两次方法差异已记录，不影响结果。
