# W47 zh-tw-fr proof2 — 独立复校笔记（重扩散新版，全量重校）

- 复校员：独立复校 proof2（与构建者、proof1 均不同轮次），2026-11-11
- 目标：`production/2026-w47/2026-w47-zh-tw-fr/`（繁中正文 × 法语讲解），重 fan-out 新版，未 commit 未 push
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-zh-tw-fr1/`（下称 `$S`）
- TMPDIR：`$S/tmp/`（未用 /tmp）；`PYTHONDONTWRITEBYTECODE=1` 全程
- 红线遵守：只读生产文件，未改任何生产文件内容、未 commit、未 push；重建（run.py / render.py）全部在 `$S/build/` 副本内完成；web PDF 未重渲染，只比文字层
- 本轮是**从头全量重校**：proof1 的旧缺陷、旧结论均未采信为结论，只作方法参考；每项均在本版上实测

## 结论：(a) 零缺陷，可定稿

缺陷清单：**空（D0）**。全部机械门通过；150 题三源逐题手验一致；8 页逐版目视干净；法语讲解层全文通读无误；日期/星期全验；STRADDLE 0；boxtitle -0.2px 经交付 PDF 渲染像素实测为盒内（见 O2）。以下 O1–O4 为观察项，均不构成缺陷。

## §1 身份核对（三 SHA，任务给值逐字核对）

| 件 | SHA-256（实测） | 字节 | 核对 |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-FR.pdf` | `acd1d85b2af073100140a8bfd5936faeecc8a050f42226a424066aefce1aaf33` | 20,191,919 | ✓ 全 SHA + 字节一致 |
| 网 PDF `Lucerna-VOL4-FR-web.pdf` | `6026be3ed418a8bd9574bfea2fd154ec7bc727d600b0eded0cff2b91a4070246` | 2,366,339 | ✓ 全 SHA + 字节一致 |
| text.md `2026-w47-zh-tw-fr.text.md` | `673943a0de31811ee43d899390a40fdde1c564ae7176f61878f77e1c687fa613` | 52,470 | ✓ 全 SHA + 字节一致 |
| 核心印 PDF `core-zh-tw/Lucerna-VOL4.pdf` | `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a` | 19,420,552 | ✓ 未变 |
| 核心网 PDF `core-zh-tw/Lucerna-VOL4-web.pdf` | `1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240` | 2,324,042 | ✓ 未变 |
| 核心 text.md `2026-w47-zh-tw-en.text.md` | `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b` | 49,798 | ✓ 未变 |

前置探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` rc=0，goals 侧真实写文件成功后才开工。
只读复核：生产成品印/网 PDF、text.md 的 mtime 仍为 builder 的 2026-11-11 11:06–11:08；生产 `svg/` 8 文件 mtime 为 20:20:18–20:20:58——字节经本轮开工实测与任务 SHA 逐一一致、与 `$S/build/` 独立重建逐字节一致，freeze 8/8 一致，故为本轮复校前一次逐字节相同的重建留下的 mtime，无内容改动；本人未向生产写盘（freeze baseline 为 copy 式，输出只在 `$S/gates/fr-proof2/freeze-base/`）。

## §2 机械门独立重跑（全部用 `tools/venv/bin/python` 正典栈，见 GATE-LOG.md）

| 门 | 独立实测结果 | 结论 |
|---|---|---|
| run.py（`$S/build/` 副本） | **RC=0**，0 FLOW OVERFLOW，0 HEAD TOO WIDE，0 警告；150 题；分级 A2 44 / B1 74 / B2 32；分页 10/18/18/18/18/18/12/38；类型 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1；P7 col3 1823.3、teaser 2577.3（页脚规则 2596，余 18.7px）；P8 keys 末行 2431、写作条 1280.2、范文 142 字 | 通过 |
| SVG 重建（副本 vs 生产） | **8/8 字节一致**（sha256 diff 空）：p1 `b11d4028…`、p2 `f8f7c994…`、p3 `7c9e4576…`、p4 `7bda50af…`、p5 `f2de5e8e…`、p6 `08e0227d…`、p7 `6b3fd466…`、p8 `f7421f50…` | 通过 |
| 印 PDF 重渲（副本 render.py） | RC=0，**逐字节相同**：20,191,919 B，SHA `acd1d85b…af33` 与交付一致 | 通过 |
| freeze baseline | **8/8** SVGs byte-identical；核心 8 个 SVG 重哈希未变 | 通过 |
| freeze diff --strict-cjk | rc=1，新增 CJK 合计 9，**全部是家具「法語講解」中的「法」**（P1 ×2 徽章行+页脚，其余每页 ×1 页脚）；正文 CJK 无新增。裁定：门禁工具对 fan-out 家具（读者语名必然更换）的结构性误报，非缺陷（与 proof1 同一裁定，实测签名完全相同） | 通过（已裁决） |
| checks.py | **CHECKS PASS**：8 phrases ×2；SIMP_ONLY_HITS []；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] | 通过 |
| occlusion 审计 | selftest 6 类 planted 全触发、clean 对照静默；全版 **0 flags** | 通过 |
| p8 extract + compare | extract noted **150/150**；compare **CLEAN**，missing=[]、extra=[]、keydiff=[]（驱动 `gates.json` 的 `extra: "?"` 为驱动取键小 bug，compare JSON 原文 extra=[] 已核） | 通过 |
| canonical creambox 全版扫描 | **36 盒**；inside-only 最小清除 P1 18.8 / P2 15.8 / P3 15.8 / P4 9.8 / P5 6.4 / P6 19.9 / P7 12.5；负清除 0；P7 工具盒 +40.5 / +12.5 / +14.0 | 通过 |
| boxtitle | 36 盒、超框 0；最小标题右余 **-0.2px**（P2「耶誕城小檔 Fiche Christmasland」）——交付 PDF 渲染像素实测墨右缘 1860.5、盒右缘 1862.0，**在盒内**，见 O2 | 通过 |
| PIL STRADDLE / CREAM-COVER | 新版 **STRADDLE 0、CREAM-COVER 0**（与重扩散报告 §7「fr 0 = 舊 0」一致；proof1 另测得旧版 STRADDLE 1，本轮未再测旧版——新版 0 已实测） | 通过 |
| spill 扫（creambox_check.py） | **NO OVERFLOW**，36 盒 inside-clearance 全正（最小 +15.8，P7 盒 +12.5 另见 canonical 扫） | 通过 |
| 孤儿扫（orphan_scan.py，自写） | 原始候选 275 个，逐项核为**中文按字换行的正常末行碎片**（单字/单标点行尾是 CJK 排版常态）；无栏顶孤词、无脱离盒子的孤行；唯一单标点独占盒末行是 P4「你呢？」盒末行 "?"，在盒内（墨底距盒底 +9.6px），见 O1 | 通过（0 孤儿） |
| 印/网文字层 | -layout 字节 110,315 / 110,315，字符多重集差 **0**；plain 差恰 1 字节（仅一个 `\n`）；本週日 11/11、下週日 0/0、BABYMONSTER 0、取捨 2/2、小雪 36/36、end point 0、next Sunday 0 | 通过 |
| PDF 度量 | 8 页、1462.5×2025 pt；P8 字号 9.75–34.5pt（最小恰 SOP §1.1 下限 9.75，印/网一致）；P1 顶部字号 [147.0, 45.0, 27.0, 24.0]；印 20,191,919 B / 网 2,366,339 B（< 7 MB） | 通过 |
| keycheck（填空键 + 1–150 连续） | 填空键 **54/54** 出自正文；答案键 1–150 连续 | 通过 |
| leak 扫描 | deny 命中 {}（含 "next Sunday"/"Next Sunday" 0 处——英文源 key 未漏入版面文字层）；唯一与核心共有的长 ASCII 串为选项行「A. 12:00 · B. 14:00 · C. 19:00」（构造共享） | 通过 |
| abutting（P6 18:30/19:00） | 墨缝 **0.6px**（頒獎典禮墨右缘 990.8 → 夜間遊行墨左缘 991.4），与核心先例完全一致；目视无重叠 | 通过（非缺陷） |
| text.md ↔ 印 PDF 文字层 | 非空白字符多重集差 153/约 25,800，**CJK 字符差 0**；残差全为 Markdown 标题记号（`#`×17、"Page N — …" 标题字母）与 PDF 独有的装饰性 "Lucerna" 页眉词标（text.md 8 处页脚 vs PDF 16 处） | 通过 |
| VOL 计数（印文字层） | VOL.4 ×10、VOL.3 ×2、VOL.5 ×1；VOL.5 ×1 为 P7 下期預告头（正确），VOL.3 ×2 为 P7 延期披露中法各 1（W46 VOL.3 下期預告原话承诺，属实） | 通过 |
| ABSTRACT.txt | 法语单行 423 B：VOL.4、A2 à B2、150 exercices，列本周真实主题（味全龍遊行、六福村最終場、金馬獎 63 屆、鋼雕閉幕、小雪、迪士尼聖誕、西九爵士）；无 ASCII 双引号 | 通过 |
| §1.1 风格杂扫 | 纸色 #fbfaf6 8 页齐全；「Gold」仅见于 "Golden Horse" 专名（×6）；`stroke-width="3"` 0 处；「·」用法与核心一致（选项分隔、时间轴图例、人名中点）；弯引号 “” 0、直引号 `"` 0；页脚 `Lucerna　繁體中文週報 VOL.4　繁體中文正文　法語講解` + `Page N sur 8` 每页齐全 | 通过 |
| 标题数实测 | 25px 章节头 **39** 个 + 奶油盒标题 **36** 个 = 75 个标题类元素；“56 titles”在本版实测中无依据 | 记录 |

## §3 目视（交付印 PDF 自行渲染 100dpi，8 页逐版；网 PDF 抽查 P1、P4）

- P1–P8 全部看过：无溢出、无重叠、无页脚碰撞；图片/署名位置确认；P7 记忆/M1 行、P6 时间线、P4 D4 盒、P8 键尾均在画面内。
- 网 P1、P4 与印版视觉一致（版式、文字、图片、条形图均在位）。
- P4「你呢？」盒：法语译文末行独占的 "?" 在米色盒内（200dpi 裁切确认，盒底留白可见），见 O1。
- P6 时间轴 18:30「頒獎典禮」与 19:00「夜間遊行」标签并排可读，无碰撞。
- P2「耶誕城小檔 Fiche Christmasland」标题：200dpi 渲染像素实测墨右缘 1860.5 < 盒右缘 1862.0，完整在盒内，见 O2。
- P4「棒球詞卡 Mots du baseball」头折为两行（"Mots du" / "baseball"）——在栏内折行，无溢出警告、无重叠，KIT 已记为已知非缺陷。

## §4 150 题逐题手验（三源交叉 + 题干复算）

方法：独立解析三源答案键——(1) 版 text.md 答案区、(2) 版 P8 SVG 答案区、(3) 核心 P8 SVG 答案区；另逐题对照题干事实核对答案正误，算术/日期类复算。结果见 `keycheck-150.json`（mismatches 仅 #150 一项，见下）。

- 三源答案值：**150/150 一致**（字母/填空词/配对词逐项比对；唯一名义差异为 #150 的注释语言：核心为英文 "Open task … (142 characters)"、版与 text.md 为法文 "Tâche ouverte … (142 caractères)"，内容相同，已标注 OK——非缺陷）。
- 逐题正误：150 题题干、选项、答案全部手验无误。已复算的算术/日期类：Q23 2000、Q24 800、Q41 17 天、Q42 1.5h、Q59 50、Q60 30、Q77 48 天（14+31+3）、Q78 6 天、Q84/Q99 5h、Q85 1.5h、Q125 48 天、Q126 6 天、Q127 100、Q128 5h。
- 判断题 Q114（六福村最終場在 11 月 15 日）答案为 **B（錯）**——SVG 原文核实，与核心一致。
- F 写作范文：实测正好 **142 字**（含标点、无空格），在 120–180 字要求内；内容与 D 篇一致（下午看遊行、晚上看金馬轉播、兩件大事、天气转冷）。
- 8 句「本週金句」页码引用（p.1/p.1/p.2/p.2/p.3/p.3/p.4/p.5）逐句核对，均出自所引页正文。
- E 节 type 标签繁体本地化：A 判斷對錯 Vrai ou faux、B 本週大測驗 Le grand quiz、C 完成句子 Compléter les phrases、D 讀一讀，答一答 Lire et répondre、E 情景說話 Dire dans le contexte、F 寫一寫 Écrire——全为繁体，无简体残留。
- 简体字扫查：checks.py SIMP_ONLY_HITS []；text.md 同集扫查 []。
- M1/M2（P7）：M1「終點 (ligne d'arrivée)」已为正确法语；M2 记忆口诀顺序正确——「apprenez d'abord 入圍, puis 星光大道 (le tapis rouge à 17:00, avant la cérémonie), puis la cérémonie （頒獎） à 18:30」，与 P3 正文「頒獎典禮前，先走星光大道」一致。

## §5 法语讲解层全文通读（text.md 法语行 554 行 + 8 页渲染对照）

- 全部 Notes 盒（P1×2、P2×2、P3×3、P4×2、P5×3、P6×1）逐句读过：性数配合、变位、标点、事实均与中文正文一致；"ce dimanche, 22 nov."（P1、P4 各一处；P1 第二篇 Notes 另用 "le dimanche 22 nov."），"dimanche prochain" 0 处。
- 易错诊所三条法语订正（22 nov. / 14:00 / 12 fois, 17:30–23:00）与正文一致；12 场计数正确（17:30、18:00、…、23:00 每半小時共 12 場）。
- 读者园地法语披露与中文「延期披露」逐句对应，无新增事实、无虚构读者。
- P8 150 条答案注释全为法语，无英文残留（除 #150 的核心对照英文，见 §4）。

## §6 日期/星期全验（`date -d`，Asia/Taipei）

11/16 週一、11/17 週二、11/22 週日、11/13 週五、12/27 週日、2027/1/3 週日、11/21 週六、11/6 週五、10/23 週五、11/24 週二、12/4 週五、12/5 週六——与版内全部星期标注一致。版内算术：耶誕城 11/13–12/27 = 45 天（18+27）；迪士尼 11/17–明年 1/3 = 48 天（14+31+3）；金馬影展 11/6–11/22 = 17 天；爵士第二週 11/17–11/22 = 6 天；小雪倒數 11/16→11/22 = 6 天——全部复算正确。

## §7 观察项（非缺陷，无需修版）

### O1 — P4「你呢？」盒法语末行独占 "?"（STRADDLE 规则实测裁定）
- 位置：P4 SVG `x=1461.5, y=1362.2`；米色盒底 1372，墨底 1362.4，**在盒内 +9.6px**；200dpi 裁切目视：French 末行 "?" 独占一行，盒底留白清晰。
- STRADDLE 三判据：(a) 字形被裁——无；(b) 墨迹重叠/压线——无（occlusion 0、CREAM-COVER 0）；(c) 回归——无（旧版同一位置曾伸出盒底 4.4px，重建已修好，本版为改进）。排版上略不雅（单问号独占一行），但不构成缺陷。

### O2 — P2 boxtitle 最小右余 -0.2px（工具估计值 vs 渲染像素）
- 标题「耶誕城小檔　Fiche Christmasland」，盒 [1439.5, 1430.0, 1862.0, 1890.0]；boxtitle.py 估计右余 -0.2px。
- **交付 PDF 渲染像素为准**：200dpi 实测标题墨右缘 1860.5、盒右缘 1862.0，**墨在盒内**（boxtitle 的 -0.2px 为 PIL 字体度量估计偏差，渲染像素不认同）。字形完整、无裁切、无碰撞。非缺陷。
- 另：与 proof1 的 -0.2px 数值相同（同一标题同一工具），裁定一致。

### O3 — P4「Mots du baseball」头折两行（KIT 已记）
- 「棒球詞卡 Mots du / baseball」在栏内折行，无溢出警告、无重叠；排版略不雅，KIT 已记为已知非缺陷。本轮实测与 KIT 一致。

### O4 — freeze diff --strict-cjk rc=1 的裁定（见 §2）
- 新增 CJK 仅「法」×9，全在家具「法語講解」中；与 proof1 同一裁定，非缺陷。门禁工具对 fan-out 家具的结构性误报，建议工具侧白名单处理（不属本版缺陷）。

## §8 重扩散报告 §7 未决项实测（只作待裁定提示的逐项核实，不预判）

1. **英文源 key「next Sunday」未改**：`tables.py:245/:267/:322` 与冻结核心 `content12.py:37/:113`、`content34.py:127` 仍为「next Sunday」；本版版面文字层实测「next Sunday」/「Next Sunday」**0 处**、「下週日」0 处、「本週日」11 处（印/网一致）。英文源 key 未漏入本版，不列缺陷。是否改核心英文，属协调员定夺（KIT K6/K7 之外的文档收尾，不属本轮）。
2. **双语小檔标题 STRADDLE**：本轮 PIL 扫描实测 **STRADDLE 0**（法语版无标题伸出盒外）；唯一接近项为 O2 的 -0.2px 估计值，渲染像素实测在盒内。无字形被裁、无墨迹重叠、无回归。按 STRADDLE 规则记观察，不列缺陷。

## 交付

- `PROOF-NOTE.md`（本文件）
- `GATE-LOG.md`（每门禁命令与结果）
- `keycheck-150.json`（150 题三源比对）
- 辅证：`gates/fr-proof2/gates.json` + 各门日志（`checks.log`、`occlusion*.log`、`p8-*.json`、`creambox.log`、`creambox-pil.log`、`boxtitle.log`、`fillin-check.log`、`freeze.log`、`freeze-diff.log`、`spill.log`、`orphan.json`、`text-layer-*.txt`）、`build-run.log`、`build-render.log`、`prod-svg-sha.txt`、`rebuilt-svg-sha.txt`、`textmd-prose.txt`、`textmd-french.txt`、`render/p1–p8.png`、`render/web-p1.png`、`render/web-p4.png`、`render/p2-christmasland-title-crop.png`、`render/p4-vous-crop.png`、`orphan_scan.py`、`gates-proof2.py`、`keycheck150.py`
