# GATE-LOG — 2026-W47 en-fr proof2（Q73 delta 重建版，2026-11-11，复校员独立重跑，盘上实测）

Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-fr2/`
（`probe.txt`、`run-copy.log`、`svg-rebuilt.sha`、`svg-shipped.sha`、`svg-now.sha`、`diff-registry.txt`、`diff-textmd.txt`、`diff-svg.txt`、`occlusion.log/.json`、`occlusion-selftest.log`、`p8-extract.log/.json`、`p8-compare.log/.json`、`keycheck.log`、`freeze.log`、`freeze-diff.log/.json`、`freeze-final/`、`freeze-core.log`、`freeze-core/`、`core-svg-now.sha`、`print.txt`、`web.txt`、`print-nl.txt`、`web-nl.txt`、`web-rerender.txt`、`webpdf.log`、`render-web/`、`minfont.log`、`minfont.py`、`scan.py`、`scan.log`、`check_s11.py`、`check_s11.log`、`creambox-all.log`、`creambox-check.log`、`creambox-core.log`、`creambox-check-core.log`、`creambox.py`、`creambox_check.py`、`fillcheck.py`、`fillcheck.log`、`pixeldiff.log`、`render/print/p-1..8.png`、`render/web/p-1..8.png`、`tmp/`）
工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`。`TMPDIR=<scratch>/tmp`。`/dev/null` 开工检查正常。未写 /tmp，未改生产文件（收工 SHA 复核与开工一致），未 commit、未 push。

## 0. 对象核对（任务书 + DELTA-NOTE §7 + 盘上 sha256sum，2026-11-11 实测）

| 文件 | 字节 | SHA-256（完整） | 结果 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-fr.pdf` | 29,330,985 | `0b4fded62123ee39ec97b8d4b7abd9c5c8e1f41184500a0aa76c25ee2678c693` | 与任务书修后值一致 ✓（8 页，1462.5×2025 pt） |
| `The-Lucerna-VOL4-en-fr.web.pdf` | 2,413,667 | `2d20b93df8f88596e1eec7915b7a2ea3d103176061cc35e7b24009c32e95a733` | 与任务书修后值一致 ✓（8 页，< 7 MB） |
| `2026-w47-en-fr.text.md` | 53,806 | `ed8fd9ec8b706dfe961b5638fefe4e857f6493a01a312d2a7e8fdc0f0f0ff213` | 与任务书修后值一致 ✓（1305 行） |

修前三件（proof1 (a)）仅作 delta diff 的对照基线，不在本轮复核：印 `76b4522c…` / 29,330,979 B、网 `dd68f929…` / 2,413,670 B、文 `2d832a17…` / 53,809 B（与 DELTA-NOTE 修前表一致）。
收工三件 SHA 与开工一致，未变。`registry.json` `41dc6d5ba8a803ca23217092479ea8f19c48e97e555952cf4ee37d2b56792ace`、`content56.py` `86383c4edd051a929194bd83edfd7d1d3e9c2f99000679250b486639df9f251e`，与 DELTA-NOTE 一致。

## 1. Q73 四源 + delta diff（实测）

| 检查 | 命令 / 位置 | 结果 |
|---|---|---|
| registry Q73 | `registry.json` n=73 | `{page: 5, level: A2, type: Compléter, key: 'up', note: 'speak up = parler franchement'}` ✓ |
| text.md Q73 | `:589` / `:1151` | 题干 `Speak ___: tell a teacher.`；附录 `73. [A2] Compléter — up (speak up = parler franchement)` ✓ |
| P8 SVG | `svg/p8-test.svg` | `73. up` ✓ |
| P5 SVG | `svg/p5-youth.svg` | `Speak ___: tell a teacher.` + `speak up = parler franchement` ✓ |
| 残留 `73. speak` | registry / text.md / P8 SVG / 印/网文字层 grep | 全部 0 命中；`"key": "speak"` 0 命中 ✓ |
| registry diff | `diff scratch-delta-en-fr/registry-pre.json registry.json` | 恰好 1 行：`583c583` `"key": "speak"` → `"key": "up"` ✓（`diff-registry.txt`） |
| text.md diff | `diff text-pre.md 2026-w47-en-fr.text.md` | 恰好 1 行：`1151c1151` 同上 ✓（`diff-textmd.txt`） |
| SVG diff | `sha256sum svg/*.svg` vs `svg-pre.sha` | 仅 `p8-test.svg` 变化（`4978f960…` → `34acf55d…`）；p1–p7 哈希一致，p5 字节一致（预期内）✓（`diff-svg.txt`、`svg-now.sha`） |
| `73. up` 印/网文字层 | `grep -c '73\. up' print.txt web.txt web-rerender.txt` | 各 ×1 ✓ |
| 印/网文字层 `73. speak` | 同上 | 0 / 0 ✓ |

## 2. 机械门（逐门重跑）

| 门 | 命令 / 位置 | 结果 |
|---|---|---|
| 探针 | `ls /dev/null` + scratch 写文件 + `git hash-object -w`（仓库内） | /dev/null 正常；`probe.txt` 写入成功；hash `9daeafb9…`，RC=0 ✓ |
| run.py（scratch 副本） | 整版拷至 `<scratch>/build-copy`（除 cards/`__pycache__`/*.pdf/*.md/*.json；首拷漏 `svglib.py` 失败后补全重拷），`tools/venv/bin/python run.py` | **RC=0**，0 OVERFLOW / 0 TOO WIDE，TOTAL 150，MODEL 82；重建 8 页 SVG 与交付 SVG 逐字节一致（`svg-rebuilt.sha` == `svg-shipped.sha`）✓；副本随后删除（哈希与日志保留） |
| occlusion 审计 | `tools/venv/bin/python tools/occlusion_audit.py <ed>/svg --json occlusion.json` | **0 flags**，RC=0 ✓ |
| occlusion 自检 | `... occlusion_audit.py <ed>/svg --selftest` | 自检 OK：6 类 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 阳性对照全触发，干净对照静默 ✓ |
| p8 extract | `tools/p8.py extract --p8 <ed>/svg/p8-test.svg --total 150 --json p8-extract.json` | **150/150**，noted set 60/150：[3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82–87, 89, 108–150]（与核心 noted 集相同）✓ |
| p8 compare | `tools/p8.py compare --core-p8 core-en/svg/p8-test.svg --edition-p8 <ed>/svg/p8-test.svg --total 150 --json p8-compare.json` | **CLEAN**，missing=[] extra_count=0 uncertain=[]；keydiff=[137, 138, 139, 140, 150]（读者语翻译键 + 写作键，预期内，与 proof1 同）✓（`p8-compare.json` 本体已读） |
| p8 extract vs registry | 抽出键逐项对 `registry.json`（`keycheck.log`） | 149/150 exact；仅 Q150 差异（registry 长式 vs 提取短标 `Tâche ouverte`，与核心同 pattern）✓ |
| registry keys vs core | registry 逐项对 core-en `registry.json`（`keycheck.log`） | 键差异仅 137–140、150（读者语键），其余 145/150 相同；Q38–41 = b/a/d/c；Q125=A，Q46=A，Q52=hosted，Q55=won，Q82/83/84=B/C/A ✓ |
| freeze 渲染 | `tools/freeze.py baseline --build <ed> --core-svg <ed>/svg --out freeze-final` | **8/8 SVGs byte-identical**：p1 `1b1a791f…`、p2 `dd332b9c…`、p3 `9d64511a…`、p4 `049cbf23…`、p5 `e944be19…`、p6 `0f6f06dd…`、p7 `715db784…`、p8 `34acf55d…`（修后值）；core integrity 8 文件未变 ✓ |
| freeze core 对照 | `tools/freeze.py baseline --build core-en --core-svg core-en/svg --out freeze-core` | **8/8 SVGs byte-identical**；核心 8 页 SVG 哈希与 delta `core-svg-now.sha` 8/8 一致，核心未动 ✓ |
| freeze diff vs core | `tools/freeze.py diff --core-svg core-en/svg --edition-svg <ed>/svg --json freeze-diff.json` | p1 +34/−34、p2 +43/−54、p3 +26/−23、p4 +26/−22、p5 +25/−22、p6 +26/−21、p7 +66/−55、p8 +103/−98；新增 CJK 共 9 个，全为 U+3000（每页 1–2 个）✓ |
| 印/网文字层 | `pdftotext [-layout] print/web` + token 多重集 + 逐页比较 | -layout：印=网=108,899 B；无 layout：印=网=49,436 B；token 多重集差 0/0；逐页 byte-identical 8/8（每页字符数 12559/13917/11370/12423/10820/11389/13969/21089）✓；网 < 7 MB ✓ |
| 网 PDF 重渲 | scratch 副本内 `tools/webpdf.py render-web/svg The-Lucerna-VOL4-en-fr.web.pdf`（**绝未覆盖交付网 PDF**） | RC=0，2,413,678 B（与交付 2,413,667 B 差 11 B，逐次浮动，预期内）；文字层与印版及交付网版逐字节一致（`web-rerender.txt` cmp 印/网均 identical）✓ |
| P8 最小字号 | PyMuPDF（`minfont.py`，tools venv fitz）读印/网版 spans + SVG 属性（`scan.py`） | PDF 有效最小 **10.12 pt**（P8 答案键块；其余页最小 11.62 pt）；SVG 属性最小 13.5 pt（全版与 P8 同）；印/网逐页 span 数与最小值完全一致；均 ≥ §1.1 下限 9.75 pt ✓。备注：KIT “13.5 pt” 为属性值，非渲染有效值（仅记录，不计入判定）。注：首版 heredoc 方式跑 fitz 无输出挂起逾 7 分钟已杀掉，改文件方式 46 秒完成（见 PROOF-NOTE 方法备注） |
| §1.1 / P8 检查 | `check_s11.py fr`（`scratch-fanout-en/check_s11.py` 复制） | **RC=0，ALL §1.1/P8 CHECKS PASS**：色集 core 19 / edition 19，无多无少；徽章色 A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f` 齐全；P8 min font 13.5；Q113–120 选项行 [A2] 标签、Levels 145–149 [A2]、Q120 [A2] chip、H WRITING `Écriture [B1]` 均在 ✓ |
| boxtitle 宽度 | occlusion BOXTITLE 类 + P7 目视 | 审计 0 flags；P7 三处旧 HEAD TOO WIDE 节头（ERROR CLINIC / READERS' CORNER / AN EXAMPLE LETTER）渲染中均在栏宽内 ✓ |
| keycheck | p8 extract vs registry（上）+ 150 题人工逐题核对（§4） | 机械 149/150 + #150 已知例外；人工 150/150，零问题 ✓ |
| 引号/字符 | 8 页 SVG 可见文本正则统计（`scan.py`） | “ 82 / ” 82 成对 ✓；U+2019 0 ✓；ASCII 撇号 73；U+00B7 282（与核心完全一致）；U+3000 141；可见文字真实 CJK 0；原始 SVG 内 CJK 仅蛾标 `<title>Lucerna 三色蛾</title>`（与核心共有）；“Note \| Note \|” 0；禁词（TODO/FIXME/Lorem/占位/SOP/proofread/cover/bridge/XXXX/TBD）0 ✓ |
| VOL 计数 | 8 页 SVG 逐页统计，与 proof1 逐页对照 | VOL.4 12、VOL.5 8、VOL.3 3（P1 3/0/0、P2 1/1/0、P3 1/1/0、P4 1/0/0、P5 1/0/0、P6 1/2/1、P7 3/3/2、P8 1/1/0）✓ |
| ABSTRACT | `ABSTRACT.txt` | 一行 + 结尾换行，775 B，法语，无 ASCII 双引号 ✓ |
| 孤儿标点 | `scan.py`：SVG `<text>` 独行标点 + text.md 独行标点行 | 均为 **0** ✓ |
| 附录计数 | text.md ANSWERS 节起 `N. [` 行 | 恰好 **150**；全文共 158 行，另 8 行为 P8 完形选项行 112–119（与 proof1 同 pattern）✓ |
| text.md 附录 vs registry | `scan.py` | 仅 137–140 四项注记括号差异（键句本身一致），其余 146/150 逐项一致 ✓ |

## 3. creambox 逐盒裁定（原版 +45 px 窗口，本版 23 行负值全裁定；精炼版 NO OVERFLOW）

原版 `creambox.py` 全版扫描逐行（与 proof1/delta 逐行一致）：

| 页 | 盒 y / 盒底 | 末基线 / 余量 | 末行 | 裁定 |
|---|---|---|---|---|
| P1 | y=786 / 1067.2 | 1104.2 / −37.0 | `TRY IT NOW　À vous de jouer` | 下块标题，假阳性 |
| P1 | **y=588 / 1256.0** | **1244.0 / +12.0** | `Intérêt relatif, pas des volumes exacts.` | **SEARCHES 盒内**（proof1 D2 已修） |
| P1 | y=1280 / 1652.0 | 1676.0 / −24.0 | `THE WORD OF THE WEEK` | 下块标题，假阳性（全版唯一 −24.0） |
| P1 | y=1874 / 2290.0 | 2246.0 / +44.0 | `in the 2025–26 Ashes. (p. 4)` | 盒内 ✓ |
| P2 | y=526 / 706.6 | 742.6 / −36.0 | `Life goes on around the politics. Next` | 盒后流文，假阳性 |
| P2 | y=200 / 497.6 | 534.6 / −37.0 | `WHAT IS ON THIS WEEK?` | 下块标题，假阳性 |
| P2 | y=1340 / 1485.5 | 1437.7 / +47.7 | `tour.` | 盒内 ✓ |
| P2 | **y=833 / 1185.4** | **1171.1 / +14.3** | `November 3.` | **DID YOU KNOW 盒内**（proof1 D3 已修；盒高 325.5→352.5） |
| P2 | y=1211 / 1544.9 | 1539.8 / +5.0 | `anglais à la rédaction.` | 盒内，紧但未出 ✓ |
| P2 | y=1636 / 1768.0 | 1738.0 / +30.0 | `Le dépouillement continue.` 等 ×3 | 盒内 ✓（三格同 rect） |
| P3 | y=200 / 644.5 | 680.0 / −35.5 | `A film is not only a story — it is also` | 盒后流文，假阳性 |
| P3 | y=1224 / 1399.0 | 1436.0 / −37.0 | `A　COMPREHENSION` | 下块标题，假阳性 |
| P3 | y=856 / 1068.6 | 1105.6 / −37.0 | `FIVE SENTENCES` | 下块标题，假阳性 |
| P4 | y=489 / 820.7 | 856.2 / −35.5 | `How do you follow three sports in one` | 盒后流文，假阳性 |
| P4 | y=1435 / 1610.9 | 1647.9 / −37.0 | `A　COMPREHENSION` | 下块标题，假阳性 |
| P4 | y=856 / 1274.3 | 1311.3 / −37.0 | `ONE SCREEN, TWO SCREENS` | 下块标题，假阳性 |
| P5 | y=2034 / 2244.8 | 2280.3 / −35.5 | `If you want to practise` | 盒后流文，假阳性 |
| P5 | y=200 / 345.7 | 382.7 / −37.0 | `A　COMPREHENSION` | 下块标题，假阳性 |
| P5 | y=852 / 1064.6 | 1101.6 / −37.0 | `FRIDAY'S WORDS` | 下块标题，假阳性 |
| P6 | y=200 / 441.0 | 477.0 / −36.0 | `A note on numbers in this issue: this` | 盒后流文，假阳性 |
| P6 | y=779 / 954.2 | 991.2 / −37.0 | `READ THE CHART　Graphique` | 下块标题，假阳性 |
| P6 | y=666 / 878.6 | 915.6 / −37.0 | `FIFTY ELECTIONS` | 下块标题，假阳性 |
| P7 | y=254 / 429.4 | 464.9 / −35.5 | `win = to get first place. won = the past` | 下块说明文，假阳性 |
| P7 | y=953 / 1098.8 | 1134.3 / −35.5 | `more than = a bigger number than. In` | 下块说明文，假阳性 |
| P7 | y=1658 / 1803.9 | 1839.4 / −35.5 | `The counting will continue. The new` | 下块说明文，假阳性 |
| P7 | y=2151 / 2296.9 | 2332.4 / −35.5 | `Use the past for the past: Collins` | 下块说明文，假阳性 |
| P7 | y=359 / 504.6 | 540.1 / −35.5 | `Newspapers use the present in` | 下块说明文，假阳性 |
| P7 | y=818 / 964.1 | 999.6 / −35.5 | `Nobody knows whether the count will` | 下块说明文，假阳性 |
| P7 | y=651 / 1038.7 | 1075.7 / −37.0 | `READERS' CORNER　Courrier` | 下块标题，假阳性 |
| P8 | y=1720 / 2000.0 | 1907.6 / +92.4 | `a busy week of votes, socks and stories — an` | MODEL 盒内 ✓ |

负值计数：−24.0 ×1、−35.5 ×9、−36.0 ×2、−37.0 ×11，合计 23 行，与 proof1 裁定集逐行一致。
精炼版 `creambox_check.py`：全部盒内余量为正（P1 +12.0/+44.0、P2 +47.7/+14.3/+5.0/+30.0、P7 工具盒 +48.5、P8 +92.4），**NO OVERFLOW，RC=0**。
对照 core-en：两脚本均跑核心 8 页 SVG——原版负值 pattern 与本版一致（同为下块标题/流文 −35.5…−37.0），核心 P1 SEARCHES 同样 +12.0、P2 DID YOU KNOW 同样 +14.3；精炼版核心同样 NO OVERFLOW。

## 4. 150 题逐题核对（text.md 全文通读 + SVG 题面核对 + registry 对照）

- 编号连续 1–150；每页 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；级别 A2 62 / B1 66 / B2 22。
- 44 项 `___` 填空/改写（`fillcheck.py`，`fillcheck.log`）：逐项填入核对，44/44 合理。Q73 `Speak ___: tell a teacher.` + `up` → `Speak up: tell a teacher.` ✓。
- 完形 Q112–119（`content8.py` 段落 + 三选项逐项核对）：Tuesday / call / continues / will meet / writes / will certify / wears / will watch 逐项唯一正确。
- 五组配对题逐组对 SVG 渲染核对：P2（24b/25c/26a/27d ✓）、P3（38b、39a、40d、41c ✓；SVG 渲染选项 a. teaches and guides / b. chosen to take part / c. lives with you in the jungle camp / d. place where the Games are fought）、P4（56b/57c/58d/59a ✓）、P5（74d/75a/76b/77c ✓）、P8（141b/142c/143d/144a ✓）。
- 逐题核对题面、原文、图表、算术：全部正确。要点：Q7 B 254、Q9 C 218、Q46 A（2025-11-21 周五珀斯）、Q47 C 背伤、Q48 B、Q49 A 2010–11、Q50 C 12:30、Q51 B 膝伤、Q52 hosted、Q53 lasts、Q54 eight、Q55 won、Q83 C 19、Q84 A 33/35、Q87 C 435（254+162+19）、Q97 takes、Q100–107 演练（won/more/lost/will/published/whether/chose/win）、Q108–111 改错（won / continued / more than / whether）、Q112–119 完形（见上）、Q120–128 选择（B/A/C/B/A/A/B/A/C）、Q129–132 阅读（B/A/C/B）、Q133–136 句型（will meet/won/more/whether）、Q137–140 翻译（法译准确）、Q141–144 配对（b/c/d/a 全对）、Q145–149 对话（row/film/popcorn/show/Friday）、Q150 开放写作；模型文 82 词（字母数字 token 计，与核心一致）。
- 金句：P7 8 句逐字出自本期正文，页码标注（P1/P2/P3/P4/P5/P6）正确。

## 5. 8 页目视（印版 P1–P8 全页 + 网版 P1/P8，72 dpi）

- 渲染：`pdftoppm -r 72` 自印版 PDF（`render/print/p-1..8.png`）与网版 PDF（`render/web/p-1..8.png`）；网版与印版视觉一致（像素差仅 JPEG 重压所致；文字层逐页 byte-identical）。
- 结果：无溢出、重叠、压页脚、图片与出处问题；页脚 `Page N sur 8` 全 8 页正确；刊头/徽章/栏目条齐全；P8 答案块在页内，未压页脚。
- P5：Q73 题干只印 `Speak ___` 空白（键不在此页，正确）；Lawrence 儿童图 + 出处齐全；D 节头栏底、题下栏为模板流行为（与核心同）。
- P7：工具盒 B2 无 `encore`；NEXT WEEK 为 June 2027 口径；Johnson 图 + 出处齐全。
- P8：答案键块 1–150 齐全，`73. up` 在页内（Page 5 答案行）；模型文 82 词在框内。
- 像素对比（vs delta 渲染 `scratch-delta-en-fr/render/print/p-*.png`，阈值 >10）：P1–P8 **0 差异像素**（同 PDF，预期内）（`pixeldiff.log`）；网/印 P1 42,461 / P8 20,945 差异像素为网 PDF 图片 JPEG 重压所致。

## 6. 必验项专项证据

### Q73 delta（本轮唯一改动）
- 四源同为 `up`（§1）；registry/text.md diff 各恰好 1 行；SVG 仅 p8 变化、p5 字节一致（预期内）；`73. speak` 全版 0 命中。

### proof1 D1–D5 修复在位
- Q39/Q40：印版文字层 `39. a` ×2、`39. d` 0、`40. a` 0、`40. d` ×1；P8 答案行 `39. a · 40. d · 41. c`。
- D2/D3：SEARCHES +12.0、DID YOU KNOW +14.3（§3）。
- D5 “encore”：`encore changer` 全版 0 命中；剩余 `encore` 2 处均合法（Q138 注 `continues = continue encore`；P7 读者来信注 `aucune vraie lettre n'est encore arrivée`）。

### 旧版对比（本轮 = delta 后版 vs proof1 (a) 版）
- 文字层 token 多重集差：唯一差异为 Q73 键 `speak` → `up`（`73. speak` 1→0、`73. up` 0→1，其余 token 全部一致）；SVG 仅 p8 变化；像素差 vs delta 渲染 0（同 PDF）。

## 7. 方法备注（非缺陷，复校员操作记录）

- `scan.py` 路径问题：从 proof1 原样复制时 `S` 仍指向 `scratch-proof-en-fr1`，首跑误读 proof1 旧版 `p8-extract.json`，报 Q73 一条假 mismatch；已改路径为本 scratch 重跑，结果仅余 #150 已知例外（`scan.log` 第二版为准）。
- `run.py` 首拷漏 `svglib.py` 致 `ModuleNotFoundError`（复校员操作失误）；整版重拷后一次通过 RC=0。
- min-font 首版 heredoc 传脚本挂起逾 7 分钟（无输出，CPU 为空），已 SIGTERM 杀掉，改写成 `minfont.py` 文件再跑，46 秒完成 RC=0。

## 8. 结论

机械门全绿；全文、150 题、8 页目视已全量复校。结论 **(a)：定稿，零缺陷**。确认 en-fr 可定稿。仅记录、不计入判定：D5 字体（P8 渲染有效最小字号 10.12 pt vs 属性 13.5 pt，仍 ≥ 9.75 pt 下限；见 PROOF-NOTE）。
