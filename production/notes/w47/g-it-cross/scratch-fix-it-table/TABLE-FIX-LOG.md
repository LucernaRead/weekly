# W47 it 重 fan-out 前置：translations.py 表值修复 LOG（TABLE-FIX-LOG.md）

- 日期：2026-11-11（UTC）
- 任务：PATCH-INVENTORY.md §8 待办——proof1 已报的盒题/副标题溢出是表值过长，重 fan-out 前先改表
- 改动对象（唯一）：`hidden_files/w47/scratch-fanout-it/translations.py`（240 条，改后仍 240 条）
- 备份：本 scratch `translations.py.orig`（改前全文，sha 见下）
- 未动：core-it、任何版文件（`content*.py` / `.text.md` / SVG / PDF）、无 commit、无 push
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 通；goals 侧写入正常；全程 `TMPDIR=<本 scratch>/tmp`

## 0. 结论

共改 **17 处表值**（15 处几何溢出 + 2 处文字），全部 PIL 真墨双法验证 fit：

| 组 | 改动 | 结果 |
|---|---|---|
| it-de D1 | 副标题前缀缩短 | margin +5.5 px（薄，见 §3） |
| it-nl D1–D3 | 3 处盒题缩短 | margin +22.5 / +30.5 / +63.5 px |
| it-nl D9 / D10 | 拼写、引号 | 纯文字修正，无盒约束 |
| it-fr D1–D4 | 4 处盒题/副标题缩短 | margin +4.5 / +5.5 / +8.5 / +111.5 px |
| it-pt D2–D5 | 4 处盒题/副标题缩短 | margin +15.5 / +36.5 / +26.5 / +140.5 px |
| it-ru D2–D4 | 3 处副标题/栏目标题缩短 | margin +30.3 / +24.9 / +107.2 px |

模拟验证（§4）：重 fan-out 模拟 10 版，sim-OLD 差分恰为改动的表值行 + 已知基线（E 标签 4 行/版、it-nl 间距 1 行），**0 意外变化，计数断言 0 失配**；未改动的 5 版（en/es/ja/ko/zh-tw）与盘点基线逐行一致。

## 1. 量测方法（先验证方法，再量新值）

- 复刻真实渲染器：`svglib.py`（自 it-ru 版原样复制到本 scratch，仅作量测库）的 `_runs` 分词 + `_pil` 取字：**sans 体——西里尔字母用 Noto Sans，其余（含拉丁、U+3000、空格）用 Noto Sans CJK SC**；逐 run 累计 `getlength` 定 x，再取各 run `getbbox` 右缘。量测脚本 `measure.py`。
- **纠正任务书一处口径**：任务书称“俄语词用 Noto Serif 度量，拉丁部分用 Newsreader”——那是 **serif** 体的规则（见 `svglib.py` 注释与 P1 masthead 实测：西里尔 Noto Serif、拉丁 Newsreader）。本次所涉 15 处全是 **sans** 体（盒题 23/24 bold、副标题 19 regular），SVG 节点与各版 proof 的 ink 日志一致写 `Noto Sans CJK SC` / `Noto Sans`。若按任务书口径量，会量错字体、得错宽度。本 LOG 一律按实际渲染字体量测。
- 方法验证（旧值复算 vs PROOF-NOTE 报告值，15 处）：
  - 13 处 |Δ| ≤ 0.7 px；其余 3 处：pt D2 −2.4、pt D4 −2.9、ru D4 +3.5 px。另以 `occlusion_audit.py` 的 4× 超采样法（`ink_box`）复核新值：两种方法对新值相差 ≤ 0.5 px（§2 末两列）。旧值 3 处偏差的来源是 proof 侧超采样/取整口径，非分词错误——run 的 x 坐标与 SVG 节点逐个核对完全一致（如 ru P7：1643.8 / 1785.4）。
  - 盒界（以 PROOF-NOTE 为准）：P1/P2 奶油盒右缘 961.0（节点 x=556.5，预算 404.5 px）；P7 盒右缘 1862.0（节点 x=1461.5，预算 400.5 px）；P1 副标题盒/版心右缘 1862.0（节点 x=1461.5，预算 400.5 px）。
- 判定标准：新值墨右 ≤ 盒右缘，且两种方法一致通过；margin < 10 px 的记“薄”，见 §3。

## 2. 逐项改动与实测（新旧值对照）

`　` = U+3000。行号 = `translations.py` 行号。margin = 盒右缘 − 新值墨右（plain / 4× 两种方法）。

### it-de D1 — P1 副标题（表 L155，19 px regular，盒 1862）

| | 值 | 墨右（plain） | margin |
|---|---|---|---|
| 旧 | `Diese Woche　Cosa succede, giorno per giorno` | 1875.5（proof 1875.7，超 13.7） | −13.5 |
| 新 | `Die Woche　Cosa succede, giorno per giorno` | 1856.5 / 4× 1856.2 | **+5.5 / +5.8** |

按 PROOF-NOTE 建议修法；proof 估算 1858.7，与实测一致。margin 薄（§3）。

### it-nl D1–D3 — BOXTITLE（23 px bold）

| 项 | 位置/盒 | 旧值（后半） | 新值（后半） | 旧墨右 | 新墨右 plain / 4× | margin |
|---|---|---|---|---|---|---|
| D1 | P1 cifre，盒 961 | `DE WEEK IN CIJFERS` | `CIJFERS` | 1074.5（超 113.5） | 938.5 / 938.0 | **+22.5 / +23.0** |
| D2 | P2 frase，盒 961 | `OM TE ONTHOUDEN` | `LEUS` | 1097.5（超 136.5） | 930.5 / 930.8 | **+30.5 / +30.2** |
| D3 | P7 errori，盒 1862 | `VEELGEMAAKTE FOUTEN` | `VEEL FOUTEN` | 1921.5（超 59.5） | 1798.5 / 1798.8 | **+63.5 / +63.2** |

- D2 关键发现（见 §3）：直译意语头再短也装不下，改走 core 短 gloss 路线。`LEUS` = 荷兰语 motto/slogan，对应 core gloss `口诀`。备选 `MOTTO`（+6.5）因 margin 过薄未取；`SPREUK`（−3.5）、`KERNZIN`（−12.5）实测仍溢出。
- D1 备选 `IN CIJFERS` 实测 968.5（仍超 7.5）未取。

### it-nl D9 / D10 — 纯文字（无盒约束，改后仅核对表值）

| 项 | 位置 | 旧 → 新 | 表行 |
|---|---|---|---|
| D9 | Q92 注（`2027 增长预测 +0,8%` 的 nl 值，落在 `content56.py`） | `Groei Prognose voor 2027: +0,8 %` → `Groeiprognose voor 2027: +0,8 %` | L1755 |
| D10 | Q32 注（`本届巧克力节主题是“Fate dolci”` 的 nl 值，落在 `content34.py`） | `Het thema van Eurochocolate dit jaar is “Fate dolci”` → `… is «Fate dolci»` | L1295 |

D10 引号形式：nl 版其余 « » 用法为准（表 L699 `«I tesori della Calabria»`，无内侧空格）；与 es/pt/ru 的 `«Fate dolci»` 一致。直引号 “ ” 仅 nl/ko/zh-tw 的 Q32 注残留，fr 为 `« Fate dolci »`（带内侧空格，法语惯例，不动）。

### it-fr D1–D4

| 项 | 位置/盒 | 旧值（后半） | 新值（后半） | 旧墨右 | 新墨右 plain / 4× | margin |
|---|---|---|---|---|---|---|
| D1 | P1 cifre，盒 961 | `LA SEMAINE EN CHIFFRES` | `CHIFFRES` | 1133.5（超 172.5） | 956.5 / 956.2 | **+4.5 / +4.8** |
| D2 | P1 副标题 19 px，盒 1862 | `Cette semaine` | `Cette sem.` | 1889.5（超 27.5） | 1856.5 / 1856.5 | **+5.5 / +5.5** |
| D3 | P2 frase，盒 961 | `À RETENIR` | `DEVISE` | 991.5（超 30.5） | 952.5 / 953.0 | **+8.5 / +8.0** |
| D4 | P7 errori，盒 1862 | `ERREURS FRÉQUENTES` | `ERREURS` | 1908.5（超 46.5） | 1750.5 / 1750.2 | **+111.5 / +111.8** |

- D1：`CHIFFRES` 已是法语最短形式（备选 `EN CHIFFRES` 实测 992.5，仍超 31.5）。margin 薄，无更短词可选（§3）。
- D2：`Cette sem.` 为法语标准缩写；备选 `Semaine`（+21.5）因丢掉 cette 未取。`La semaine` 实测 1863.5（仍超 1.5）未取。
- D3：与 nl D2 同理（§3）。`DEVISE` = 法语 motto，对应 core gloss `口诀`；最短直译 `RETENIR` 实测 971.5（仍超 10.5）。备选 `MOTTO`（+6.5）margin 更薄未取。

### it-pt D2–D5

| 项 | 位置/盒 | 旧值（后半） | 新值（后半） | 旧墨右 | 新墨右 plain / 4× | margin |
|---|---|---|---|---|---|---|
| D2 | P1 副标题 19 px，盒 1862 | `Esta semana` | `Esta sem.` | 1874.5（超 12.5） | 1846.5 / 1847.0 | **+15.5 / +15.0** |
| D3 | P1 cifre，盒 961 | `A SEMANA EM NÚMEROS` | `DADOS` | 1120.5（超 159.5） | 924.5 / 924.5 | **+36.5 / +36.5** |
| D4 | P2 frase，盒 961 | `PARA LEMBRAR` | `LEMA` | 1045.5（超 84.5） | 934.5 / 934.0 | **+26.5 / +27.0** |
| D5 | P7 errori，盒 1862 | `ERROS FREQUENTES` | `ERROS` | 1879.5（超 17.5） | 1721.5 / 1721.5 | **+140.5 / +140.5** |

- D2：备选 `Semana`（+26.5）因丢掉 esta 未取；`Esta sem.` 保留 esta 且 margin 充足。
- D3：`EM NÚMEROS` 实测 1000.5（仍超 39.5）未取；`NÚMEROS` 实测 961.5 / 4× 961.0（−0.5 / +0.0，恰压线）**拒收**，改取 `DADOS`（= 数据，裸名词 gloss，与 `CIJFERS` / `CHIFFRES` 同式）。
- D4：与 nl D2 同理（§3）。`LEMA` = 葡语 motto，对应 core gloss `口诀`；最短直译 `LEMBRAR` 实测 981.5（仍超 20.5）。

### it-ru D2–D4

| 项 | 位置/盒 | 旧值（后半） | 新值（后半） | 旧墨右 | 新墨右 plain / 4× | margin |
|---|---|---|---|---|---|---|
| D2 | P1 副标题 19 px，盒 1862 | `На этой неделе` | `Неделя` | 1904.8（超 42.8） | 1831.7 / 1831.4 | **+30.3 / +30.6** |
| D3 | P1 IN QUESTO NUMERO，24 px bold，盒 1862 | `СОДЕРЖАНИЕ` | `СОДЕРЖ.` | 1897.7（超 35.7） | 1837.1 / 1836.9 | **+24.9 / +25.1** |
| D4 | P7 errori，盒 1862 | `ТИПИЧНЫЕ ОШИБКИ` | `ОШИБКИ` | 1896.4（proof 1892.9，超 30.9–34.4） | 1754.8 / 1754.8 | **+107.2 / +107.2** |

- D2：备选 `На неделе` 实测 margin 仅 +3.2 / +3.5，落在方法口径波动带（§1：旧值复算最大偏差 3.5 px）内，**拒收**；`Неделя` 作栏目标签自然（意语部已载完整含义）。`Эта неделя` 实测 1865.7（仍超 3.7）未取。
- D3：`СОДЕРЖ.` 为俄语标准缩写（proof 建议）。

## 3. 判定时取舍与薄 margin 说明

1. **P2 frase 三处（nl D2、fr D3、pt D4）直译意语头在 23 px bold 下无解**：意语头 `LA FRASE PER RICORDARE　` 自身 advance 315.6 px，盒预算 404.5 px，留给 gloss 仅 88.9 px；最短直译 `RETENIR` 98.9 / `LEMBRAR` 108.7 / `ONTHOUDEN` 149.4 px，全部溢出。改法遵循 core 自身模式：core 第二半是短 gloss `口诀`（2 字、墨右 918），不是意语头翻译——故三处改用各语 motto 词（`LEUS` / `DEVISE` / `LEMA`）。若协调员坚持直译意语头，则须另案改 mechanism（降盒题字号或分行），表值层面无解。
2. **薄 margin（< 10 px）共 4 处，均已双法复核一致**：de D1 +5.5、fr D1 +4.5、fr D2 +5.5、fr D3 +8.5。渲染是确定性的（同一 PIL/字体/代码，run x 与 SVG 节点已逐个核对一致），且两种量测法相差 ≤ 0.5 px；但 proof 的 PDF/像素实测与 PIL 之间历史波动达 ±3.5 px，故重 fan-out 后复校时这 4 处应优先复量墨迹。fr D1 无更短替代词（`CHIFFRES` 已最短）；其余 3 处更安全的备选会丢词义（de `Woche` +38.5、fr `Semaine` +21.5），故保留现选。
3. **拒收的两处压线候选**：pt D3 `NÚMEROS`（−0.5 / +0.0）、ru D2 `На неделе`（+3.2 / +3.5）——均在波动带内，不赌。
4. **P1 cifre 同类**：fr `EN CHIFFRES`、pt `EM NÚMEROS`、nl `IN CIJFERS` 均实测仍溢出未取；最终取裸名词（`CHIFFRES` / `DADOS` / `CIJFERS`），与 core 短 gloss 模式一致。
5. **不动项复核**：it-nl D4 方向仍为 fix3（B-2/B-3）已缩短，重 fan-out 后复核（本次模拟 sim-NEW 中已含该两行）；it-fr D5、it-ko D3、E 型标签、C-1 间距均未碰（见 §4 末）。

## 4. 模拟验证（只读、内存内，不建 PDF）

复用盘点 agent 的 `simulate.py`（拷入本 scratch，输出目录改到本 scratch；源变换逐字复刻 `build_edition.py`：OUT 重定向、E 节重定向、`instr="写作"`、P8 分隔符、最长优先全量表替换）。分别从 fix3 前 core（`oldmd`）与 fix3 后 core（现 `core-it`）重跑 10 版，与现版逐行比对（`sim-summary.txt`，逐文件差分 `sim-OLD-*/sim-NEW-*`）：

- **计数断言：0 失配、0 rep1 失配**（模拟输出无任何 DIAGS 行）。表仍 240 条；17 个新值均不含任何表键作子串（无二次替换风险；`Cosa succede, giorno per giorno` 不是独立表键）。
- **sim-OLD（旧 core + 新表）vs 现版**——差分恰为本次改动 + 盘点已知基线：
  - de `content12` +2 行（D1）；其余 0。
  - nl `content12` 6 行（D1、D2、C-1 间距各 1 行 ×2）、`content34` 2 行（D10）、`content56` 2 行（D9）、`content7` 2 行（D3）、`content8` 8 行（E 标签基线）；其余 0。
  - fr `content12` 6 行（D1、D2、D3）、`content7` 2 行（D4）、`content8` 8 行（E 标签基线）；其余 0。
  - pt `content12` 6 行（D2、D3、D4）、`content7` 2 行（D5）、`content8` 8 行（E 标签基线）；其余 0。
  - ru `content12` 4 行（D2、D3）、`content7` 2 行（D4）、`content8` 8 行（E 标签基线）；其余 0。
  - en/es/ja/ko/zh-tw：除 `content8` 8 行（E 标签基线）外全部 0——与盘点基线逐行一致，**其余表项 0 意外变化**。
  - 注：D9/D10 的注文落在 `content56.py`（Q92）/ `content34.py`（Q32）的题干内，不在 `content8.py`。
- **sim-NEW（新 core + 新表）vs 现版** = sim-OLD 上述差分 + fix3 每版 9 行（`content12` 6 行：B-1/B-2/B-3；`content34` 6 行：B-4/B-5/B-6；`content8` 6 行：B-7/B-8/B-9，与 E 基线合计 14 行）+ 0 其他。`content56` / `content7` 除上述表值行外 0 差异。与盘点 §4 的 fix3 清单逐行吻合。
- **C-1（it-nl masthead 间距 11.5 → 11.0）仍在差分中原样出现**——符合预期：它不在表里，本棒不改，重 fan-out 后须重打（协调员事）。

## 5. 附带发现（不在本棒范围，报协调员）

- **P1/P2 盒题溢出是全家族问题，不只本棒 5 版**：实测现版 SVG 墨右（盒 961）——P1 cifre：en +156、de +138、es +134、ja +46、ko +70（fr/pt/nl 即本棒已修）；P2 frase：en +40、de +30、es +100、ja +48、ko +44；P7 errori：en +6（fr/pt/nl 即本棒已修）。ru 因西里尔窄体三处全 fit；zh-tw 与 core 同宽 fit。en/es/ja/ko 的同类盒题不在本次任务内，**未改**——协调员决定是否同法处理（P2 同样须走 motto 短 gloss 路线，直译无解；P1 可走裸名词路线）。
- core re-proof（`scratch-proof-core-it3/`）仍在跑：若其后落 fix4，须 fold 进 core 再重 fan-out（协调员事；本棒只改表）。

## 6. 本 scratch 文件

- `TABLE-FIX-LOG.md`（本文件）
- `translations.py.orig`（改前表备份）
- `measure.py`（PIL 真墨量测；先复算 15 处旧值对 PROOF-NOTE，再量新值，plain + 4× 双法）
- `simulate.py` + `sim-summary.txt` + `sim-OLD-*/sim-NEW-*`（重 fan-out 模拟差分）
- `svglib.py` + `assets/lucerna-moth.svg`（量测用渲染器副本，只读导入，未改）
