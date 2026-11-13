# W47 zh-cn 家庭修复 FIX-LOG（接替工人；上一任 8701ed10 被运行时重启中断）

- 范围：`production/2026-w47/` 内 `core-zh-cn` + 10 版 fan-out（`2026-w47-zh-cn-{en,de,fr,es,it,pt,nl,ru,ja,ko}`）。不碰其他家庭、其他周；不 commit、不 push、不跑 lint；`svglib.py` 一律不动。
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`。脚本复用上一任 `scratch-fix-zh-cn/` 下 `rebuild-fix.sh` / `run-all.sh` / `backup-pre-fix/`（已核实，见下）。
- 磁盘门限：df 已用 ≥100G 立即停手。接手时 94G/150G。

## 接手核实（2026-11-12，上一任中断后第一步）

### 1. 指纹：10 版印/网 PDF + text.md 与 PROOF-NOTE 全表对照——全部一致（均为校对时状态）

| 版 | text.md 字节 / SHA-256 前 12 | 印 PDF 字节 / SHA-256 前 12 | 网 PDF 字节 / SHA-256 前 12 |
|---|---|---|---|
| zh-cn-en | 49,435 / `23fb62bd7763` | 33,521,853 / `f7b131533cda` | 2,434,915 / `7088ff061297` |
| zh-cn-de | 50,628 / `51d6dab11f8b` | 33,519,497 / `778118ef7b60` | 2,433,374 / `4d937086bd26` |
| zh-cn-fr | 51,821 / `e125a9d1b75b` | 33,513,605 / `b76447c9c2a5` | 2,427,580 / `fd1fd83b1ce0` |
| zh-cn-es | 51,175 / `edc045da1f0c` | 33,515,606 / `6a34c9e1a097` | 2,429,057 / `f5cd5f4687c8` |
| zh-cn-it | 50,916 / `afc9b2c02a31` | 33,509,850 / `f3c6061e9a2c` | 2,423,808 / `3b2e81e4a3d2` |
| zh-cn-pt | 50,834 / `ed0858346f73` | 33,516,121 / `d4c27a7fc2a4` | 2,430,183 / `a3a92057bead` |
| zh-cn-nl | 50,057 / `1f864e74ae70` | 33,512,276 / `b317ad38804e` | 2,426,135 / `29150ee7cb3c` |
| zh-cn-ru | 60,503 / `eb5345d96801` | 33,721,996 / `1b71f5d44d46` | 2,634,216 / `2eee3f4487d8` |
| zh-cn-ja | 52,444 / `68d850eac576` | 35,542,943 / `d2e3ee82fc0e` | 2,826,687 / `fa614f26d856` |
| zh-cn-ko | 52,725 / `eb5fdedda37c` | 36,955,697 / `a4fa88ef2420` | 2,808,430 / `43f7a29a3843` |

- core-zh-cn text.md 与 zh-cn-en 字节相同（49,435 / `23fb62bd7763`，`cmp` identical），与 PROOF-NOTE 一致。
- core-zh-cn 印/网 PDF 与 en **不再相同**（上一任重建过 core，见下）：印 33,522,354 / `c5dbd85164ae`，网 2,436,070 / `9a60689dd3fc`。
- 10 版 text.md 逐版实测：`犯罪片` ×3（`悬疑犯罪片` ×2：P5 正文 + Q65 选项 A；另 `是___犯罪片` 填空题干 ×1，见 F4 补充实例）、`惊悚片` ×0。

### 2. 上一任留下的东西——源头改动大部已落地，成品一律未落地

核实结论：**协调员「上一任的活基本没落地」对成品成立、对源头不成立。** 上一任已在 11 个目录的源头（`.py`）里改好了 F4（正文+Q65 选项+读者 gloss）、F5、F6（引文内）、F7、F8、F9，只漏 F4 填空题干一处（见 §3）；但只重建了 core-zh-cn 一个目录（`logs/core-zh-cn/GATES-SUMMARY.txt`，2026-11-12T13:19Z，ALL-GREEN），10 版 fan-out 的 SVG/PDF/text.md 全是校对时原样，text.md 里的 F4–F9 缺陷全在。

证据：

- `backup-pre-fix/` 的 `.py` 与生产目录 `.py` 用 `diff -rq` 逐版比对**完全相同**（只差备份时未收的 `ABSTRACT.txt` / `WEEKLY-KIT.md`，ru 另有 `svglib.py.orig` 杂文件未动）。即备份里的源头已是改后状态——**备份是成品基线（text.md/SVG 为校对态），不是源头基线**。text.md diff 以备份为准，仍能准确反映本次修复（只含意改行）；源头无真 pre-fix 对照可比，本节改以逐项实测为准。
- 上一任 core 重建的实际变化（备份 SVG vs 现盘 SVG 文本提取）：仅 p5 两处 `悬疑犯罪片`→`悬疑惊悚片`、p8 两处 `is a suspense crime film.`→`is a suspense thriller film.`；其余文本全同。core `run.log`：TOTAL 150、0 OVERFLOW、0 HEAD TOO WIDE；门禁 ALL-GREEN（occlusion 0、p8 extract 150 + compare CLEAN、freeze baseline 8/8、spill 0、boxtitle 0、edge 0、census PASS、quotes 0、print==web 文本 22,529 字）。
- 但 core 的 text.md **未重导出**（仍为校对 SHA `23fb62bd7763`，含 `犯罪片` ×3），KIT 也未更新。本次接手须补：core 重建（含 F4 填空题干）+ en text.md 重导出并拷回 core。

### 3. F4–F9 逐项接手状态（源头 .py vs 成品 text.md/SVG/PDF）

| 发现 | 源头（.py，11 目录实测） | 成品（10 版 text.md 实测，均为校对态） | 结论 |
|---|---|---|---|
| F4 体裁 | `content56.py`：`悬疑惊悚片` ×2（P5 正文 + Q65 选项 A），`悬疑犯罪片` ×0，11 目录全同；读者 gloss 已去犯罪化：en `suspense thriller film`、de `Suspense-Thriller`、fr `film à suspense`、es `película de suspense`、it `thriller di suspense`、pt `filme de suspense`、nl `suspensefilm`、ru `саспенс-триллер`、ja `サスペンス映画`、ko `서스펜스 영화` | 每版 `犯罪片` ×3、`惊悚片` ×0 | **半落地**。只剩填空题干一处源头未改（见下 F4 补充实例），成品 10 版全待重建 |
| F4 补充实例（同缺陷同修） | `content56.py` 完成句子题干 `《试探》是___犯罪片，11月21日上映。` ×1，11 目录全有；填空答案为 `悬疑`，补全后仍读作 `悬疑犯罪片`，与已改体裁矛盾。上一任全局替换漏了这一处（core p5 SVG 实测仍含 `犯罪片，` 一处） | 每版 text.md 均含该题干 | **未修**。本次一并改 `《试探》是___惊悚片，11月21日上映。`（同 F4，无新增改动类） |
| F5 ja 括号 | `content7.py` P7 A2 词表行已统一为 ASCII 括号：`(juésài、決勝)` 等 6 处全为 `(…)`；全文件 `(` 117 = `)` 117、`（` 19 = `）` 19，无 `(…）` 混用 | text.md:1315 仍为 `(juésài、決勝）` 等 6 处混用 | **源头已修，成品待重建**（只动 ja） |
| F6 ko/ja 引文数字 | `content7.py:51-52` 引文内已是原文：ko `「139.38亿件」` ×2、ja `「139.38亿件」` ×2；非引文内本地化按裁定保留：ko `content7.py:49` `139.38억 개`（B2 讲解段正文）、ko `content8.py:60` `22일 합계는 139.38억 개입니다。`（P8 填空 gloss）、ja `content7.py:49` `139.38億件`、ja `content8.py:60` `22日間の合計は139.38億件。` | ko/ja text.md 各含 `139.38억` / `139.38億件` ×9，其中引文内 2 处（:1393 练习 gloss、:2017 key 109）待改；其余 7 处为按裁定保留的正常读者语 | **源头已修，成品待重建**（只动 ko/ja） |
| F7 es/pt | es `content7.py`：`Las 06:00 son 早上 — no por la noche.`；pt：`As 06:00 são 早上 — não à noite.`；`no la tarde` / `não à tarde` ×0 | es text.md:1363、:2011（key 106）仍为 `no la tarde`；pt 同位置仍为 `não à tarde` | **源头已修，成品待重建**（只动 es/pt） |
| F8 ru | `content7.py`：`a.head("A2　决赛与包裹　Финал и посылки", 24)` | text.md:1313 仍为 `Финал посылки` | **源头已修，成品待重建**（只动 ru；重建时预计出现 rebuild-fix.sh 已预期的 1 处 HEAD TOO WIDE，422.7px vs 422.5px，任务定改、记录在案） |
| F9 ru | `content7.py`（最终措辞）：`Данные и чекаут сначала, заголовок — последним.`（见下「重建与门禁」ru 重跑记：第一版长措辞 `Данные и страница оформления заказа сначала…` 致 P8 keys 溢出、重建 RC=1，第二接替改用 `чекаут` 后重跑通过；`страница оформления заказа` 源头零残留） | text.md:1407、:2021（key 111）仍为 `Данные и оплата сначала` | **源头已修，成品待重建**（只动 ru） |

### 4. 复用脚本核实

- `rebuild-fix.sh`（逐版：run → head_check → render → webpdf → occlusion → p8 extract/compare → freeze baseline/diff → spill → boxtitle → edge → creambox → census → quotes → print==web 文本比对；ru 允许恰 1 处 HEAD TOO WIDE，其余版 0 处）：已通读，逻辑与任务一致；上一任用它跑 core 已 ALL-GREEN，可复用。
- `run-all.sh`（10 版 fan-out 串行 rebuild-fix.sh + `export_ed.py` 重导出 text.md + 与备份 text.md diff + en 文拷回 core）：已通读；`export_ed.py`、`d5_census.py`、`census_quotes.py`、`spill_sweep.py`、`boxtitle_check.py`、`pdf_edge_scan.py`、`d5_creambox_audit.py`、`head_check.py` 均在盘上。可复用。
- 注意：`rebuild-fix.sh` 的 freeze diff / creambox 以 `backup-pre-fix`（成品校对态）为基线，diff 有变化是预期的，只记录、不以零为门。

## 修复实施（源头改动）

### F4 填空题干（11 目录 content56.py，唯一仍开的源头口子）

- 改动：`《试探》是___犯罪片，11月21日上映。` → `《试探》是___惊悚片，11月21日上映。`（每目录恰 1 处）
- 核实（改后即验）：11 目录 content56.py 逐个 `OLD 1→0、NEW 0→1`；全家 `.py` 扫查 `犯罪片` 零残留；每目录 `惊悚片` ×3（正文 + Q65 选项 A + 填空题干）。磁盘 94G，未动门限。

## 重建与门禁（2026-11-12，第三工人核实补全）

- core-zh-cn 单独重建（`rebuild-fix.sh core-zh-cn`，GATES 2026-11-12T16:06Z，ALL-GREEN）；10 版 fan-out 由 `run-all.sh` 串行重建 16:06–17:08Z（`RUN-SUMMARY.txt`）；ru 另有重跑，见下。
- ru 重跑记：`run-all.sh` 内 ru 首建 16:57 RC=1——F9 第一版长措辞 `Данные и страница оформления заказа сначала…` 致 `FLOW OVERFLOW [P8-keys]`（keys 末行 2588.7 vs 底边 2560），其余门全绿。第二接替把 F9 措辞换成 `Данные и чекаут сначала, заголовок — последним.`（俄语电商借词 checkout，本期已用 `постамат` 同类借词；key 111 回到 y=2537.12，P8 底边余量 53.6pt），17:10–17:13 重跑 `rebuild-fix.sh` + 重导出 text.md → ALL-GREEN（`logs/2026-w47-zh-cn-ru/GATES-SUMMARY.txt` 17:13:51Z）。`RUN-SUMMARY.txt` 仍记首建失败（16:57），以 17:13 的 GATES-SUMMARY 为准。

### 逐版门禁（第三工人逐个重读 `logs/<版>/GATES-SUMMARY.txt` 原文核实）

全 11 版：run.py TOTAL 150、0 FLOW OVERFLOW；occlusion 0 flags（自检 6 类全触发、干净对照静默）；p8 extract 150/150、compare CLEAN；freeze baseline 8/8；spill 0 SPILL；boxtitle 0 DEFECT；edge 0 TOUCH、0 NEAR；creambox PASS；D5 census PASS；quotes 0 defective；print==web 文本逐字相等。

| 版 | run.py TOTAL / OVERFLOW / HEAD_TOO_WIDE | head_check | print==web 非空字符数 | OVERALL |
|---|---|---|---|---|
| core-zh-cn | 150 / 0 / 0 | RC=0 PASS | 22,529 = 22,529 | ALL-GREEN |
| zh-cn-en | 150 / 0 / 0 | RC=0 PASS | 22,529 = 22,529 | ALL-GREEN |
| zh-cn-de | 150 / 0 / 0 | RC=0 PASS | 23,737 = 23,737 | ALL-GREEN |
| zh-cn-fr | 150 / 0 / 0 | RC=0 PASS | 23,952 = 23,952 | ALL-GREEN |
| zh-cn-es | 150 / 0 / 0 | RC=0 PASS | 23,562 = 23,562 | ALL-GREEN |
| zh-cn-it | 150 / 0 / 0 | RC=0 PASS | 23,700 = 23,700 | ALL-GREEN |
| zh-cn-pt | 150 / 0 / 0 | RC=0 PASS | 23,281 = 23,281 | ALL-GREEN |
| zh-cn-nl | 150 / 0 / 0 | RC=0 PASS | 23,151 = 23,151 | ALL-GREEN |
| zh-cn-ru | 150 / 0 / 1（F8 预期，422.7px vs 422.5px） | RC=1（设计如此，恰 1 处） | 22,680 = 22,680 | ALL-GREEN |
| zh-cn-ja | 150 / 0 / 0 | RC=0 PASS | 17,704 = 17,704 | ALL-GREEN |
| zh-cn-ko | 150 / 0 / 0 | RC=0 PASS | 17,551 = 17,551 | ALL-GREEN |

### text.md diff 核查（第三工人逐版通读 `logs/<版>/textmd-diff.txt` 全文，逐行归类）

基线：`backup-pre-fix/`（成品校对态，见「接手核实」§2；其 text.md SHA 与「接手核实」改前表逐版一致，已用 `pre-fix-textmd.sha256` 复核）。每版改动行数（`diff` 的 `c` 行数；括号内为 `^[<>]` 计数）：

| 版 | 改动行 | 归类（行号为新 text.md 行号） |
|---|---|---|
| core-zh-cn | 7（14） | 全为 F4：P5 正文 :899、读者 gloss :953/:987、Q65 选项 A :955、填空题干 :989、key 65 :1925、Q70 词汇 gloss :1935 |
| zh-cn-en | 7（14） | 同 core（F4，en gloss `suspense thriller film`） |
| zh-cn-de | 7（14） | 同 core（F4，de gloss `Suspense-Thriller`） |
| zh-cn-fr | 7（14） | 同 core（F4，fr gloss `film à suspense`） |
| zh-cn-es | 10（20） | F4 7 行 + F7 2 行（:1363 练习、:2011 key 106）+ 同步漂移 1 行（见下） |
| zh-cn-it | 7（14） | 同 core（F4，it gloss `thriller di suspense`） |
| zh-cn-pt | 9（18） | F4 7 行 + F7 2 行（:1363 练习、:2011 key 106） |
| zh-cn-nl | 7（14） | 同 core（F4，nl gloss `suspensefilm`） |
| zh-cn-ru | 10（20） | F4 7 行 + F8 1 行（:1313 `Финал и посылки`）+ F9 2 行（:1407 练习、:2021 key 111，最终措辞 `чекаут`） |
| zh-cn-ja | 10（20） | F4 7 行 + F5 1 行（:1315，6 处括号全改 ASCII）+ F6 2 行（:1393 练习 gloss、:2017 key 109，引文内 `「139.38亿件」`） |
| zh-cn-ko | 9（18） | F4 7 行 + F6 2 行（:1393 练习 gloss、:2017 key 109，引文内 `「139.38亿件」`） |

- 结论：**除 es 1 行外，其余 10 版 diff 只含意改行，无任何其他漂移。** 各版 text.md 现盘实测：`犯罪片` ×0、`惊悚片` ×3（11 版全同）；ja/ko 引文内旧数字零残留（印 PDF 文字层 `「139.38亿件」` 各 ×2，旧式 `「139.38億件」`/`「139.38억` ×0）；ru 印 PDF 文字层 `чекаут` ×1、`Финал и посылки` ×1、`Данные и оплата` ×0。
- es 同步漂移行（合规，已记入 KIT）：P8 模范答案标签 :1777 `Respuesta modelo:` → `Modelo:`。核实：印 PDF 文字层（`logs/2026-w47-zh-cn-es/print-post.txt`）`Modelo:` ×1、`Respuesta modelo` ×0，网 PDF 文字层同；备份 SVG 与现盘 SVG 均只含 `Modelo:`——印 PDF 自 fix1（D-4，`content8.py:104` 前缀缩短）起一直是 `Modelo:`，只是校对态 text.md 未重导出而滞留旧标签。本次重导出使 text.md 与印 PDF 一致，属合规同步，非意改。

### 附带发现（重导出时同步治愈的旧漂移，非本次改动引入）

- es text.md diff 除 F4（7 行）+ F7（2 行）外，另有 1 行：`Respuesta modelo:` → `Modelo:`（P8 模范答案标签）。核实：`content8.py:104` 在 fix1（D-4，前缀缩短、使 `》` 不再成为行首）时已改为 `Modelo:`；备份 SVG 与现盘 SVG 均含 `Modelo:` ×1、`Respuesta modelo` ×0——印 PDF 一直是 `Modelo:`，只是校对态 text.md 自 fix1 后未重导出而滞留旧标签。本次重导出使 text.md 与印 PDF 一致，属于合规同步，非意改，已记于此。其他版 diff 逐版核查同类漂移。
- （第三工人补记）其余 10 版 diff 已逐行通读：只含上表意改行，**无同类漂移行**。es 漂移行已用印/网 PDF 文字层双重核实合规（见上节）。

## KIT 更新（2026-11-12，第二接替已执行 `update_kit.py`，第三工人逐项核实）

- 执行：第二接替于 17:27–17:28Z 跑 `update_kit.py`，11 份 `WEEKLY-KIT.md` 同批更新（mtime 均为 11-12 17:27/17:28）。第三工人未重跑（脚本见 marker 即跳过；重跑无新写入）。
- 核实方法：脚本逐版从盘上实测印/网 PDF 与 text.md 的尺寸+SHA-256 全值，比对 KIT 内记载——**11 版 × 3 文件 = 33 项全命中**（印/网/text.md 全值均在 KIT 内）；每份 KIT 均含 `### Post-proof fix — independent reproof F4–F9 (2026-11-12)` 一节：逐版修复 bullet（F4 全家 + 各版 F5–F9；es 含 `Incidental sync` 漂移 bullet；ru 含 F9 `чекаут` 措辞沿革 bullet）、门禁行（TOTAL 150、0 OVERFLOW、ru 1 HEAD TOO WIDE 预期、print==web 非空字符数、OVERALL: ALL-GREEN）、新交付物尺寸+SHA 全值、不修项（F1/F2/F3/F10）复述。
- 另：core 与 en 的 KIT 内 `Files:` 段已同步改为改后尺寸+SHA（截断式 `xxxxxxxx…xxxxxx`）；其余 9 版 `Artifacts` 节内印/网/text.md 三行已改为改后尺寸+SHA 全值。
- 注意：ru KIT 内门禁行与交付物 SHA 取自 17:13 重跑后的盘上值（非 16:57 首建），与现盘一致。

## 不修项裁定复述（协调员裁定，照录）

- F1（P8 题干 13.12pt < 15.4pt 底线）：KIT 已披露，15.4pt 测试溢出，12 页/答案册方案未采纳，不修。
- F2（P1 头条无首字下沉）：KIT 已披露的引擎偏差，不修（与 es F1 同类裁定）。
- F3（选择题选项内折行）：两轮已裁定非缺陷，不修。
- F10（右缘溢出最大 +4.8pt，无裁切，余量 61pt+）：KIT 已披露的同类偏差，门禁 edge 报告为准，不修。

## 改前/改后 SHA（2026-11-12，第三工人盘上实测）

改前值取自本 LOG「接手核实」§1（10 版 fan-out）及同节 core 行；改后值为现盘实测（SHA-256 前 12 位；全值见各版 KIT）。11 版改后印/网/text.md 的 SHA 与改前全不同（重建已落地）；core 印 PDF 与 en 印 PDF 改后字节相同（SHA 相同），网 PDF 因构建产物差异 SHA 不同，属实测值。

| 版 | 印 PDF：改前 字节 / SHA 前 12 → 改后 字节 / SHA 前 12 | 网 PDF：改前 → 改后 | text.md：改前 → 改后 |
|---|---|---|---|
| core-zh-cn | 33,522,354 / `c5dbd85164ae` → 33,521,858 / `566554e0ebc8` | 2,436,070 / `9a60689dd3fc` → 2,434,907 / `6c258be74dac` | 49,435 / `23fb62bd7763` → 49,447 / `2aaf8992bbc2` |
| zh-cn-en | 33,521,853 / `f7b131533cda` → 33,521,858 / `566554e0ebc8` | 2,434,915 / `7088ff061297` → 2,434,914 / `2579a61027eb` | 49,435 / `23fb62bd7763` → 49,447 / `2aaf8992bbc2` |
| zh-cn-de | 33,519,497 / `778118ef7b60` → 33,519,503 / `b104a8b7b81b` | 2,433,374 / `4d937086bd26` → 2,433,265 / `31fffc7ff93c` | 50,628 / `51d6dab11f8b` → 50,640 / `e11d4f915226` |
| zh-cn-fr | 33,513,605 / `b76447c9c2a5` → 33,513,599 / `30ea0661e5c7` | 2,427,580 / `fd1fd83b1ce0` → 2,427,467 / `638e9293509b` | 51,821 / `e125a9d1b75b` → 51,785 / `4cf31ce982f6` |
| zh-cn-es | 33,515,606 / `6a34c9e1a097` → 33,515,603 / `91c8a84ce10b` | 2,429,057 / `f5cd5f4687c8` → 2,428,933 / `86df4f212879` | 51,175 / `edc045da1f0c` → 51,137 / `b5bf366bad5f` |
| zh-cn-it | 33,509,850 / `f3c6061e9a2c` → 33,509,858 / `0649d5e84bdd` | 2,423,808 / `3b2e81e4a3d2` → 2,423,711 / `9aef40aa18ad` | 50,916 / `afc9b2c02a31` → 50,924 / `808250dde250` |
| zh-cn-pt | 33,516,121 / `d4c27a7fc2a4` → 33,516,115 / `fa6c12699c41` | 2,430,183 / `a3a92057bead` → 2,430,061 / `bfc1a6e4b6bd` | 50,834 / `ed0858346f73` → 50,798 / `0c9d9d5b97ac` |
| zh-cn-nl | 33,512,276 / `b317ad38804e` → 33,512,271 / `8ac769437ff6` | 2,426,135 / `29150ee7cb3c` → 2,426,029 / `fad4d6c11db0` | 50,057 / `1f864e74ae70` → 50,025 / `79666191a8b5` |
| zh-cn-ru | 33,721,996 / `1b71f5d44d46` → 33,722,005 / `fd6977bff8b0` | 2,634,216 / `2eee3f4487d8` → 2,634,194 / `e5ce689b3811` | 60,503 / `eb5345d96801` → 60,498 / `1f11029b4e83` |
| zh-cn-ja | 35,542,943 / `d2e3ee82fc0e` → 35,542,435 / `1e4e8510174c` | 2,826,687 / `fa614f26d856` → 2,826,131 / `21f0e9ba278c` | 52,444 / `68d850eac576` → 52,408 / `b0fa1af51e9f` |
| zh-cn-ko | 36,955,697 / `a4fa88ef2420` → 36,955,671 / `93cae6913685` | 2,808,430 / `43f7a29a3843` → 2,807,966 / `68597c56beb0` | 52,725 / `eb5fdedda37c` → 52,695 / `9f58f841635d` |
