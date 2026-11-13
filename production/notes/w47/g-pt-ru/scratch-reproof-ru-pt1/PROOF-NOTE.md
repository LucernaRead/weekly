# PROOF-NOTE — 2026-W47 ru-pt 独立复校（re-proof）

- 版：`production/2026-w47/2026-w47-ru-pt/`（仓库 `~/workspace/weekly-git`）
- 复校员：独立 re-proof（与 fix1 修复员、proof1、proof2/R2 均不同人；前人数字一律不采信，全部重跑重测）
- 日期：2026-11-11；工作区：`hidden_files/w47/scratch-reproof-ru-pt1/`（独占新目录）
- 只复校，不改任何生产文件，不 commit、不 push。
- 依据：repo 根 `SOP.md`（§1.1、§8.4）与协调员 brief（goals 树 `hidden_files/w47/briefs/brief-coordinator.md`）。
- 方法口径：光栅 = 印 PDF 经 PyMuPDF 以 1950px 宽渲染（1x）与 3900px（2x）；PIL 真墨含前导空白 advance（U+3000 在 23pt = 23px）；下行部用 `anchor="ls"`；阈值 med−60（cutoff 189）为主，med−25/100 交叉核对。run.py 重建只在 scratch 副本上跑（OUT 重定向到 scratch 内绝对路径，运行前核对）；网 PDF 绝不重渲（SHA 不可重现），只比文字层。

## §0 身份核对（三 SHA，磁盘实测，与任务先验值一致）

| 件 | SHA-256 | 字节 | 与任务 |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-pt.pdf` | `4d726d922b33b6c38ab93e7ed1c47c8913817a5fa4e3bbc59988ff232bec61ed` | 21,205,591 | 一致 |
| 网 PDF `Lucerna-VOL4-ru-pt-web.pdf` | `f21ed9285a7fcca0a3515e2daa2af2518b0e11fb83752280ea448cf80b7864df` | 3,383,546 | 一致 |
| 文 `2026-w47-ru-pt.text.md` | `54d8a766e18daf5f256e91c76765c9e71fefb48c9435e83d28e103bba603d60e` | 65,155 | 一致（修前字节不变） |

开工探针：`echo test | git hash-object -w --stdin` 通过；scratch 真实写文件通过。

## 结论：verdict (b) —— 仅一项缺陷，且仅为文档（KIT 身份号过期）

除 §6 的一项外，**全部内容门禁与全部 fix1 修复声称均经独立重测通过**。缺陷清单：

### (b)-1 — `WEEKLY-KIT.md` §5/§7 的交付件身份号过期（docs-only）

KIT 记的是 fix1 **修前** re-fanout 构建的数字，盘上 fix1 交付的 PDF 是另一组数字。fix1 自己的 GATE-LOG §8 明文列出 `WEEKLY-KIT.md` 未动（"均未动"），即 KIT 从未随 R2 修复更新。

| KIT 位置 | KIT 所写 | 盘上实测（本复校） | 说明 |
|---|---|---|---|
| §5 L53 印 PDF | SHA `59f01012f5c6…` / 21,205,597 B | SHA `4d726d92…` / 21,205,591 B | KIT 数 = re-fanout 构建（proof2 表同值） |
| §5 L54 网 PDF | SHA `485a27b6be19…` / 3,383,529 B | SHA `f21ed928…` / 3,383,546 B | 同上 |
| §5 L56 pdftotext 字节 | 58,200 | 58,327（印/网各，逐页 6230/6603/5356/6462/5730/5616/6906/15424） | proof1 旧值 |
| §5 L56 / L77 字符数 | 31,041（各） | 31,105（各，pdftotext CLI 去空白后；re-fanout 值为 31,107，2 字为抽取方法差） | proof1 旧值 |
| §1.1 L79 网 PDF | 3,344,677 B | 3,383,546 B | 3,344,677 是 proof1 的网 PDF 大小 |
| §5 L83 引用的记录路径 | `hidden_files/w47/scratch-refanout-ru/records/pt/RECORD.md` | 本 clone 内无此目录（`find` 无结果） | 引用悬空 |

影响：无内容影响、无门禁影响、无读者可见影响。KIT 是 SOP §1 所列的当期交付物之一，其身份号与交付件不符即是交付物缺陷。修复 = 只改 KIT 里的 5 个数字 + 1 条引用（无需重建、无需重校内容）。
另：KIT §5 L83 的 kicker 间隙表 `[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]`（称最小 5.9）在我 1x 与 2x 两套光栅测量下均不重现（见 §3）；但"最小 ≥ 4px"的判定本身成立，故不另列缺陷，只记于此。

**除 (b)-1 外，无其他缺陷。**D5（§5）仍为记录项，未恶化；P1 MEDIA 标题（§5）为同类 ±1px 观察项，非缺陷。

## §1 fix1 修复声称——逐项独立重测（全部通过）

右缘限值 1862（MX=88，RIGHT=1862，NOTE_RIGHT=1852）；页 1950×2700。

| 声称 | 源码行 | 我的实测 | 结论 |
|---|---|---|---|
| R2-D1 P1 标题改 `СЛОВО НЕДЕЛИ PALAVRA SEMANAL`（22pt 不变） | `content12.py:113` | 光栅 **1845**（余量 +17；med-60 与 med-25 一致），PIL 1842.5，span 1844.4 | 通过（声称 1844/+18，1px 方法差，无实质区别） |
| R2-D2 桥接行字符串不动，锚点改 NOTE_RIGHT | `content12.py:149`；`bslib4.py:20`（NOTE_RIGHT = RIGHT−10 = 1852） | 光栅 **1855**（余量 +7） | 通过（与声称完全一致） |
| R2-D3 EX_NOTE 单一源头，5 处改用 + NOTE_RIGHT | `bslib4.py:25`；`content12:237`、`content34:59/201`、`content56:51/174` | 五页光栅 **全部 1854**（余量 +8），印/网一致 | 通过 |
| map D1 四锚点落地 | P6 图题 + `УЧЕБНЫЕ ДАННЫЕ` `content56.py:158`（text.md:459）；P6 免责声明 `content56.py:159`（印/网 P6 文字层 L117）；P7 副标题 `content7.py:12`（text.md:504）；P8 副标题 `content8.py:12`（text.md:596） | 印 + 网均落地 | 通过 |
| kicker 9 个双空格 | `content12.py:18`（P1，16pt） | 字隙 1x **[9, 4, 10, 7, 7, 8, 9, 9, 10]**；2x **[8.5, 4.0, 9.5, 6.5, 7.5, 7.0, 9.5, 8.5, 9.5]**；**最小 4.0px ≥ 4** | 通过（裁图目检正常） |
| Q20 键 `желании` | text.md:173、:694 | 键一致；语法：`о` + 前置格 `своём` → -ие 中性前置格 -ии，正确 | 通过 |
| Q25 选项 `День студента` | text.md:187 | 选项一致；全称 `Международный день студента` 仍 ×2（正文 L91、Q11 题干 L159） | 通过 |
| pt1-D7 网 PDF 斜体 | — | 网 P1 内嵌 `LucernaNotoSerif-Italic` + `LucernaNewsreader-Italic`；`«чёрная пятница»` span 为 `LucernaNotoSerif-Italic` 16.12pt（印版为 `NotoSerif-MediumItalic` 16.12pt，同字号）；文字层 `чёрная пятница»` 贴合 ×4（印/网各 4），脱离 `чёрная пятница »` ×0；印/网裁图字节相同 | 通过（斜体 + 闭引号贴合均落地） |

R2-D2 关键发现独立确认：右锚定行的右缘由锚点决定，删词无用（proof1 建议的缩短修法经 fix1 实验 V1 证伪：缩短 51.4px 仅 1865→1864）；只有锚点内收能修。我的光栅测量以交付 PDF 像素为准。

## §2 机械门禁——全部自跑结果

| 门 | 命令/方法 | 结果 |
|---|---|---|
| run.py（scratch 副本） | `run.py` rc | **rc=0，TOTAL 150**（A2 50 / B1 76 / B2 24；页 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38）；零 FLOW OVERFLOW / HEAD TOO WIDE |
| SVG 重建 | 副本重建 vs 生产 SVG | **8/8 字节一致** |
| freeze baseline（核心） | `freeze.py baseline --build core-ru --core-svg core-ru/svg` | **8/8 字节一致**；Pillow 13.0.0 / FreeType 2.14.3 |
| freeze diff（核心→本版） | `freeze.py diff` rc=0 | 新增 CJK 仅 U+3000 ×1/页（共 8）；**零新增西里尔串**；带拉丁的移除仅 masthead + P8 键片段 |
| p8 extract / compare | `p8.py extract/compare --total 150` | extract 核心 150/150、本版 150/150；**compare CLEAN**，keydiff **[137, 138, 139, 140]** |
| P8 键 vs Answers | 150 行比对 | 150 行连续 1–150；唯一分歧 Q150（P8 印 `✓`，text.md 为开放题说明——与核心一致的已知例外） |
| occlusion | `occlusion_audit.py`（自检先行通过，6 类均触发） | **42 TEXTX，0 LINEX / COVER / FOOTER / EDGE / BOXTITLE**；核心同为 42；vs 核心 NEW 3 |
| occlusion 裁决（独立） | 1x + 2x 光栅逐条测共享墨列 | **42/42 假阳性**：全部零共享墨列；1x 间隙 ≥0，2x 间隙 ≥0（25 例间隙 0 = 零空格标点相邻，如 `» , . : ; ! ?` 紧贴词尾，正常排版）；NEW 3 例间隙大（1x 50/50/29px；2x 100/101/57）。机理已证：PIL `getbbox('　LÍNGUA')` 返回 left=0（前导 U+3000 贡献空 bbox），而 46pt 下真墨始于 ~50px 右——审计高估左缘。8 张裁图目检均为正常排版 |
| 印/网文字层 | `pdftotext` 逐页 | 每页字符多重集 **完全相同（8/8 页）**；字节数相等（6230/6603/5356/6462/5730/5616/6906/15424）；去空白字符 31,105（各） |
| P8 最小字号 | PyMuPDF span | **9.75pt**（386 spans）——恰达 SOP §1.1 下限 |
| check_core | `check_core.py .`（本版 + 核心对照） | 本版 rc=0：golden BAD 0，gloss fails 0；1 孤儿行首（P7 y553 `”».`）+ 1 同基线碰撞（P1 y1712 `чёрная`）；核心跑确认两处在核心中**完全相同存在**（核心有 5 孤儿，含 y553）——继承的良性项 |
| 32 盒标题（内容盒） | 基线分组 32 盒（9 绿带 + 23 奶油） | 全部间隙为正；最紧 **8.3px**（P6 `ЗА И ПРОТИВ / PRÓS E CONTRAS` 右侧） |
| 32 盒标题（规范 creambox） | 全部 `#f0eee5` 矩形 + 所含文字 | 最紧 **−1.65px PIL**（P1 `O QUE DIZEM OS MEDIA` 标题，见 §5 观察项）；次紧 O3 P2 盒底 **+0.52px PIL / 1px 光栅**（最低墨行 1158，盒底 1159.0）——在内，与 pt1（1158.98/+0.02）、pt2（1159.00/+0.00）在方法噪声内一致；裁图目检干净 |

范围说明：SVG 重建 8/8 字节一致证明**当前 SVG = 当前源码的 run.py 输出**（含 P7/P8）。"P7/P8 相对 re-fanout 字节不变"的声称，依据是 fix1 的 svg-before/after 快照（其 GATE-LOG §8）；本 clone 内无 re-fanout 版 SVG 备份可独立再验，故记为范围注记，不列缺陷。

## §3 150 题逐题手验（text.md L1–838 全读 + SVG 表核对）

Q1–150 **全部正确**，逐题核对题干、选项、键与正文配对（不只比三源一致）。要点：

- Q1–6 日期/数字：16 日周一、21 球、120/180 欧元、16:00、13/35；21 球由 P4 赛果表 8 场比分独立复算：0:1 + 1:2 + 1:0 + 4:2 + 2:0 + 3 (Spartak–Akron 2:1) + 2:2 + 0:1 = **21**（Q54 Krylia–Orenburg 2:0、Q59 Spartak–Akron 2:1、Q53 Zenit–Rostov 2:2、Q55 Baltika 1:0、Q64 Dynamo 2:1 均与表一致）。
- Q7–10、Q11–15、Q16–19 天气词、Q20（见 §1）、Q21–24、Q29–33 电影、Q34–38 动词形（`выходят`、`рассказывает`、`снял`、`посмотреть`、`ноября` 属格）、Q43–46 组句、Q47–51、Q52–56 分数/时间、Q61–64（`сыграли`、`будет`、`играет`、`победило`）、Q65–69 促销日期、Q70–74（`распродажа`、`вернуть`、`промокод`、`заказов` 属格复数、`скидка`）、Q79–82、Q83–88 图表/日历（38/26/18/18 = 100%）、Q89–96、Q97–100 连词（`поэтому`、`а`、`а`、`или`）、Q101–112 P7 双栏、纠错诊所 4 项全对（`с Днём студента`、`на "чёрной пятнице"`、`забили 21 гол`、`с 19 ноября`）、金句 8/8 与正文逐字一致（check_core BAD 0）、Q113–120、Q121–128、Q129–132 Masha 阅读、Q133–136 组句、Q137–140 葡译（p8 keydiff 四条，译文正确：139 `играет с Венесуэлой` → `joga contra a Venezuela`；140 `Поздравляю с Днём студента!` → `Feliz Dia do Estudante a todos!`）、Q145–149 店铺对话、Q150 开放题。
- 五组配对（SVG 右侧选项表核对，20/20）：P2 D（a 心理学家日 / b 学生日 / c 世界儿童日 / d 杰德·莫罗兹生日）→ 25=b, 26=d, 27=c, 28=a；P3 C（a 观影者 / b 传记片 / c 场次 / d 纪录片）→ 39=b, 40=d, 41=c, 42=a；P4 C（a 胜 CSKA 4:2 / b 负 Rubin 0:1 / c 胜 Akron 2:1 / d 平 Rostov 2:2）→ 57=b, 58=a, 59=c, 60=d；P5 C（a 促销码 / b 退货 / c 折扣 / d 大促销）→ 75=d, 76=b, 77=a, 78=c；P8 F（a 比分 / b 路面结冰 / c 融雪暖冬 / d 大促销）→ 141=c, 142=d, 143=a, 144=b。
- G 对话（P8 SVG 全文读）：145 A（`со скидкой`，工具格）、146 B（`«чёрная пятница»`）、147 B（`промокод`）、148 A（`целый`）、149 B（`Хороших покупок!`）——全部符合对话语境。
- Q150 范文：我自数 **97 词**，brief 80–100 词内。
- 日期星期（`date -d` 核）：2026-11-06 五、07 六、08 日、12 四、13 五、14 六、16 一、17 二、18 三、19 四、20 五、22 日、27 五（黑色星期五）、29 日、30 一（网络星期一）——与刊内全部日期表述一致。

## §4 遗留越界 D5（记录项，未恶化）

P8 副标题 `Cada resposta com uma breve nota em português　✓ = texto modelo`（基线 1302，SVG x=1239.7，19.5pt）：

- 我的光栅：印 + 网 **1864**（阈值 15/25/40/60 一致）；2x **1864.5**；PIL ink_box 1861.95，advance 1862.03。
- 与前人对比：任务记录 1863（+1）；proof1 测 1864；proof2 测 1864.4；fix1 测 1863。**同一行、同一量级（1863–1864.5），未恶化。**
- 1863 vs 1864 的来源已查明：1864 列像素灰度 140–192（✓ 尾的抗锯齿边缘），在 thr=100（cutoff 149）时仍计入，仅在更严的 cutoff（<140）下消失——属 1px 阈值带差异，非内容变化。**仍只记录，不修，不列为新缺陷。**

## §5 同类 ±1px 观察项（非缺陷）

P1 `O QUE DIZEM OS MEDIA` 标题：PIL 1863.65；光栅 1862（thr-60）/ 1863（thr-25）/ 1863.0（2x）。裁图目检：末尾 `A` 完整可见，未截断；边界是奶油填色边缘，无描绘的线。与 D5 同属 ±1px 方法噪声类，记为观察项，不列缺陷。

## §6 生产零写入核对

- 开工快照 `opening-snapshot.sha256`（44 个生产文件）与收工重哈希 `closing-snapshot.sha256` 对比：**44/44 哈希完全相同**。
- 本复校未改任何生产文件，未 commit，未 push。`git status` 显示 `production/2026-w47/2026-w47-ru-pt/` 为未追踪目录（整版未入仓状态如前，未动）。

## 证据索引（本 scratch 内）

`run-rebuild.log`、`svg-rebuild-compare.log`、`freeze-core.log`、`freeze-diff.log` / `.json` / `-cyrillic.txt`、`p8-compare.log` / `.json`、`p8extract-core/ed.json`、keys.json、`key-compare.log`、`occlusion.log` / `.json`、`adjudicate_textx.py` / `adjudicate_textx_2x.py` / `textx-adjudication*.log` / `.json`、`textlayers/`（印/网各 p1–p8）、`text-diff.log`、`p8-font.log`、`check-core.log` / `check-core-core.log`、`edge-measure.log`、`d3-measure.log`、`d5-raster.log`、`d5-threshold.log`、`kicker*.log`、`boxtitle-32b.log` / `.json`、`creambox-32.log` / `.json`、`scan-d5-boxtitle.log`、`scan-d5-advance.log`、`p4-table.log`、`match-groups.log` / `match-groups2.log`、`render-print/`、`render-print-2x/`、`render-web/`、`crop-*.png`（TEXTX 8 张 + kicker + P8 副标题 + P1 斜体印/网 + P1 MEDIA 标题 + P2 盒底）、`opening-snapshot.sha256`、`closing-snapshot.sha256`、`GATE-LOG.md`。


---

# ROUND 3 — Re-proof after text.md L836 fix (2026-11-11 ~22:46–22:57 UTC)

Independent re-proof (did not build this edition; did not write the round-2 note above).
Read: all 8 pages of the print PDF (rendered to PNG at 100 dpi, read visually in full)
+ full text.md (838 lines, read in full) + web PDF (text-extracted).
Read-only; no production file touched, no re-render of the edition, no lint, no commit.

## VERDICT: (a) ZERO FINDINGS

## SHA-256 (start and end — identical, no mid-read change)

| File | SHA-256 | Bytes |
|---|---|---|
| `2026-w47-ru-pt.text.md` | `ab21732233d80c5af14a2a579ef611370fb228ba29376d9e2ce9186a7c613a02` | 65,116 |
| `Lucerna-VOL4-ru-pt.pdf` (print) | `4d726d922b33b6c38ab93e7ed1c47c8913817a5fa4e3bbc59988ff232bec61ed` | 21,205,591 |
| `Lucerna-VOL4-ru-pt-web.pdf` (web) | `6f197ab96c9735caf94a98c97e716b594a120870a661b7b998238f63e264d20f` | 3,383,561 |

- text.md SHA matches the required `ab217322…` exactly (65,116 B) — gate passed
  before reading began.
- Print SHA matches KIT §5 (`4d726d92…`); print was NOT rebuilt by the fix.
- Web SHA differs from KIT §5 (`f21ed928…`, 3,383,546 B) — known drift from the
  concurrent web-PDF rebuild that rewrote all 9 ru web PDFs. Not a content defect:
  web-PDF extracted text is byte-identical to print-PDF extracted text (`cmp`
  clean, 91,462 chars each, 8 pages each), and the web SHA was stable across my
  whole read (start 22:46 = end 22:57), so the web verdict stands on the final
  file. Coordinator to reconcile the KIT web SHA in the KIT-sync wave.
- No U+FFFD / tofu in either PDF's extracted text (count 0).

## The fix under re-proof (L836) — verified

- text.md L836 reads exactly:
  `150. ✓ Ver o texto modelo na secção H desta página (97 palavras)`
- P8 printed answer-key line 150 reads identically:
  `150. ✓ Ver o texto modelo na secção H desta página (97 palavras)`
- The section-H model text ("Моя неделя 16–22 ноября …") counts **97 words**,
  matching the "(97 palavras)" note; the H brief asks for 80–100 words.

## Answer-key cross-check (text.md appendix vs printed P8) — verified

- text.md `## Answers` contains keys 1–150, none missing; P8 printed keys all
  numbers 1–150 present.
- Programmatic check (whitespace-normalised): 149/150 appendix key cores found
  verbatim in the P8 print text. The one exception, Q98
  ("В понедельник трудно начать, а в пятницу уже почти выходные."), is present
  but split by a pdftotext column interleave ("…уже почти" + intruding
  "19. гололедица…" + "выходные.") — an extraction artifact; the key is complete
  and correct in the P8 render, read visually.
- Every exercise key was spot-checked against its stem/article; all correct,
  including association mappings (P2 D 25–28, P3 C 39–42, P4 C 57–60,
  P5 C 75–78, P8 F 141–144) and translation keys E 137–140.

## Page-by-page notes (print PDF, visual read of all 8 rendered pages)

- **P1 (lead):** "14-Й ТУР СЫГРАН!" / "A jornada 14 terminou"; lead article,
  "ТУР В ЦИФРАХ", "СЕЙЧАС ВЫ" Q1–6, "О ЧЁМ ПИШУТ", "В ЭТОМ НОМЕРЕ", weekly word
  "«чёрная пятница»", "СНЕГ БУДЕТ?", "КОРОТКО", quiz Q7–10, park photo + CC0
  caption. Dates/scores consistent with P4 (6–8 Nov, 31 pts, 4:2, 0:1, 15th round
  20 Nov, Black Friday from 16 Nov). The 12 Nov Uzbekistan result is honestly
  flagged unknown at press time (10 Nov), deferred to VOL.5 — consistent P1/P4.
- **P2 (VIDA, A2):** Student Day / Ded Moroz birthday / weather, "ПРАЗДНИКИ
  НЕДЕЛИ", "А ВЫ?", Yuon "Зима. Ростов" image + PD caption, "СЛОВА НЕДЕЛИ"
  (оттепель / мокрый снег / ледяной дождь / гололедица), Q11–28. Q20 key
  "желании" (prepositional after "о своём") correct.
- **P3 (CULTURA, A2→B1):** 5 premieres 19 Nov, "А ЧТО УЖЕ В КИНО?",
  "ГЛАВНОЕ — КОРОТКО", "КАК ПРОВЕСТИ ВЕЧЕР", Q29–46. Q32 "Увидеть всё" /
  Elizabeth Holmes; Q33 Hunger Games 26 Nov — verified.
- **P4 (DESPORTO, B1):** Round-14 results table (8 matches, incl. the VOL.3
  correction "Балтика — Динамо Мх 0:1, 8 Nov 20:45"), top-5 table, national-team
  box (Tashkent 12 Nov 18:00, Krasnodar 17 Nov 19:00), 15th-round fixtures
  20–22 Nov, 1912 Olympic-team photo + PD caption, Q47–64. Q54 key 2:0 and
  Q57–60 mapping verified against the table.
- **P5 (JOVENS, B1):** Black Friday (calendar date Fri 27 Nov 2026, Cyber Monday
  30 Nov, Ozon 13 Nov–2 Dec, Wildberries 16–30 Nov, in Russia since 2013),
  "А ЧТО С 11.11?" (14.4M Ozon orders 11 Nov 2025), market/corn photo + USDA/PD
  caption, "ЧЁРНАЯ ПЯТНИЦА: ДАТЫ" box, Q65–82. All dates/keys verified.
- **P6 (EM PROFUNDIDADE, B2):** Week 16–22 Nov essay, calendar strip (16–20
  working days, 21–22 weekend, yellow), "ЗА И ПРОТИВ", practice-data chart
  (38/26/18/18%) with the "учебные данные — не настоящая статистика" disclaimer
  in Russian and Portuguese, Q83–100. Chart values match Q85–87 keys.
- **P7 (LÍNGUA, A2→B2):** Three-level focus, "ОШИБКИ / CLÍNICA DE ERROS" (4 items,
  all grammatically correct: "с Днём студента!", "на «чёрной пятнице»",
  "забили 21 гол", "с 19 ноября"), weekly word "распродажа", "ПИСЬМА ЧИТАТЕЛЕЙ"
  (editorial example honestly disclosed, RU + PT), Pushkin portrait (Kiprensky
  1827) + PD caption, "ФРАЗЫ НЕДЕЛИ" (8 verbatim quotes, all match source pages
  + PT translations), next-week box. Q101–112 verified.
- **P8 (TESTE E RESPOSTAS):** Test A–H, Q113–150, all stems present; full answer
  key 1–150 (see cross-check); Q150 ✓ line (see fix section); section-H model
  text present, 97 words. Weekday claims verified: 16 Nov 2026 Mon, 17 Tue,
  19 Thu, 27 Fri = Black Friday, 30 Mon = Cyber Monday, 12 Nov Thu.

## Layout / rendering

- No overflow, overlap, clipping, or tofu on any of the 8 rendered pages. No text
  runs into the footer; P5 exercises end clear of the footer; P8 key block complete
  to Q150. P8 "Морозко" image absent, as the KIT records (skipped by the build's
  own condition — same as W46 ru-pt, by design, not a defect).

## Investigated and cleared (not findings — evidence recorded)

1. **Apparent joined words** ("Профессиональныепраздники", "метеорологическаязима",
   "поздравитьfelicitar", "успеховêxito", "рожденияДеда", etc.): pdftotext merges
   some word pairs into single tokens, and at 100 dpi a few spaces look narrow.
   Checked against the SVG sources with Noto font metrics (fontTools): every
   sampled pair carries an implied space of 3.6–5.8 SVG units vs a full space of
   4.7–6.2 (e.g. "поздравить"→"felicitar": implied 4.6, full 5.3;
   "Профессиональные"→"праздники": 5.8 vs 6.2). The spaces ARE laid out; the tight
   appearance is letter-bearing geometry plus this builder's narrow word spacing.
   No word is actually missing its space. (Controls on the same lines:
   "повод | motivo" 6 px, "успехов | êxito" 5 px ink gap at 100 dpi.)
2. **"��" glyphs in an early tool-output dump** (P2 "��иноптики", P3 "«У��идеть всё»"):
   a display artifact of that output only — the extracted text files contain
   0 U+FFFD, the SVGs contain the full words, and the renders show "Синоптики" /
   "«Увидеть всё»" correctly.
3. **Q98 core not found verbatim** in P8 extracted text: pdftotext column
   interleave (see cross-check); visually complete and correct on P8.
4. **"13 de novembro–2 de dezembro"** (Q67/Q125 keys, P8): no spaces around the en
   dash — matches the text.md source wording exactly, so house style for that
   string, not a PDF/text.md mismatch.

## Observation for the coordinator (not a finding)

- text.md ends with "*«Морозко»: иллюстрация Ивана Билибина, 1932 год. Зимняя
  сказка — к ноябрю.*" — a caption for the Morozko image that the build skips on
  P8 by design (KIT). The caption text itself is correct; a site reader sees the
  caption line without the picture. Pre-existing, disclosed in the KIT, same as
  W46 ru-pt; recorded as an observation, not a defect.

## Relation to the round-2 note above

- Round 2 verdict (b)-1 was KIT identity numbers stale (KIT listed re-fanout SHAs).
  The KIT has since been updated: it now records the print SHA `4d726d92…`
  matching disk, and carries the Fix-1 record with the new text.md SHA
  `ab217322…`. The remaining KIT drift in this round is only the web SHA
  (`f21ed928…` in KIT vs `6f197ab9…` on disk, from the concurrent web-PDF rebuild)
  — same class, smaller scope; left for the KIT-sync wave, not counted as a
  content finding in this round.
- Round-2 §4 D5 (P8 subtitle right edge 1863–1864.5) and §5 P1 MEDIA title ±1px
  observations were not re-measured in this round (pixel-geometry audit was
  round 2's scope; this round is a content re-proof after the one-line text.md
  fix). Nothing in this round's full visual read contradicts them.
