# W47 D5 重建 — fr 家庭 RUN-LOG

工人：第三任（接替 d1990f92，2026-11-12 02:31 EST 被运行时重启打断；e1e9eab5 在 01:59 EST 被 cron 超时打断）。
开工：2026-11-12 02:39 EST（07:39 UTC）。
家庭：core-fr（读者 zh-cn）+ 10 fan-out；本次做 core-fr + 7 个 Latin/Russian 读者版（fr-en、fr-es、fr-de、fr-it、fr-nl、fr-pt、fr-ru）。CJK 读者版（fr-ja、fr-ko、fr-zh-tw）不动。
工作目录（沿用前任）：`hidden_files/w47/scratch-d5-rebuild-fr/`（门禁脚本 `run_gates.sh`、各版基线、日志）；本日志在任务指定位置 `hidden_files/w47/scratch-d5-fr/RUN-LOG.md`。
构建解释器：全程 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）。

## 接手时已核实状态（2026-11-12 07:39 UTC）

- core-fr 已装 D5（svglib.py 含 `_D5_READER = "cjk"`，23,410 B，06:24 UTC）。
- r1 门禁（06:26–06:44 UTC，`core-fr/logs-r1/`）：census PASS（D5 拉丁 0 / 西里尔 0 / 弯引号 CJK 0）；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs core 与 vs pre 基线均 CLEAN）；spill 0；edge 0 TOUCH/NEAR；freeze baseline 8/8、diff +0 CJK / +0 Latin；print/web 文字层逐字节一致（94,800 字符）。**但 boxtitle 4 DEFECT**（P3 `LES DATES EN CHIFFRES` +7.6px、P4 `LES PHRASES DU COMMENTATEUR` +36.5px、P5 `周三电影` +43.3px、P6 `TROIS DATES POUR COMPRENDRE` +24.5px）；creambox 审计崩溃（基线目录缺 `assets/lucerna-moth.svg`，后已补，06:45）。
- 8 处修复（06:54–06:55 UTC，相对 r1 freeze build-copy 的 diff，全部只降字号、未改文字，故 `.text.md` 不 stale）：content34.py `head_zoom` 23→22、P4 框题 `tsize=21`；content56.py `head_cine` 23→20、`IL EST PRÉVU QUE + SUBJONCTIF` 25→23、`head_comp6` 25→24、P6 框题 `tsize=21`；content7.py 同语法头 24→23、`head_clinic` 25→23。
- r2（前任被打断前）：run.py 07:27 TOTAL 150、0 HEAD TOO WIDE、0 FLOW OVERFLOW；render.py 07:30 印 PDF 重建（18,475,436 B，sha256 `f36c32f0…`）；**webpdf 在 07:31 被重启打断，网 PDF 仍是 06:38 的 r1 构建（1,985,413 B，sha256 `1ac595ec…`），与当前印 PDF 不同源、STALE，须重建**。
- KIT 未同步 D5：`WEEKLY-KIT.md` 最后改动 2026-11-11 13:34；§七第 112–113 行仍记旧印 PDF（30,446,975 B，`a30af667…`）与旧网 PDF（2,241,835 B，`56f50ca8…`）；§七第 5 行“讲解层 → Noto Sans CJK SC”在 D5 后已不准确（拉丁讲解层现为 Newsreader）。
- 7 个 fan-out 均未装 D5（svglib md5 `f25bfcfc`，与 `backups/` 预备份一致，无 `_D5_READER`）；moth 7 版齐全；各版基线齐全（`baseline/` 含 svg 8 张 + svglib.py + assets/moth、`census-pre.json`、`p8-extract-pre.json`）。fr-en 预普查 D5 拉丁 566（与 D5-CENSUS-130 一致）。
- CJK-DECISION.md 已落地（机制收尾工人，2026-11-12 UTC）：§1 CJK 读者版按字符分流（mode=cjk），§2 ru 模式已证实，§3 fix2 不扩 JP/KR，§4 落盘方式待协调员发话。**按任务令，本次仍不动 fr-ja/fr-ko/fr-zh-tw，留待协调员另派。**
- 磁盘：接手时 df 已用 91G（任务称配额约 105G 上限）；每次重建后删 freeze build-copy，只留生产文件 + 基线记录。

## core-fr — r2（进行中）

### r2 结果（2026-11-12 07:44–07:46 UTC，全绿，DRIVER EXIT=0，FAILFLAG=0）

- run.py：TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE（`tools/head_check.py` PASS 0 defects）。
- render.py rc=0：印 PDF `La-Lucerna-VOL4.pdf` 18,475,436 B，SHA-256 `f36c32f020e48…`（与 07:30 重建值相同，确定性重建）。
- webpdf.py rc=0：网 PDF `La-Lucerna-VOL4-web.pdf` 1,985,431 B，SHA-256 `ff08e74903d6…`（r1 的 `1ac595ec…` 已 stale，今已更新；WROTE 1,985,431 B，46,527 text bytes）。
- 文字层：印/网 pdftotext 各 101,106 字节，逐字节一致，multiset diff 0。
- occlusion：0 flags（自检 6 类全触发）。
- p8：extract 121/150；compare CLEAN（vs core-fr 与 vs 修前基线，keydiff=[]）。
- freeze：baseline 8/8（p1 `f3e6f6d994e1`、p2 `d39cfc493b0a`、p3 `88866677d673`、p4 `3b36fccbeff9`、p5 `912f3265193a`、p6 `1061fabdde2c`、p7 `93cf42e425eb1`、p8 `870a684ba67e`）；diff vs core +0 CJK / +0 Latin。
- boxtitle：**0 DEFECT**（r1 的 4 处已由 8 处字号修复清零；40 titles、381 body lines）。
- creambox：**PASS 0 defects**（n=492，中位 1.016、粗体 1.049、常规 1.000；P8 193→193 行、余量 36.1→36.1px）。
- spill：0 SPILL（33 boxes，102 OBSERVE）；edge：0 TOUCH，0 NEAR。
- census：**PASS**（D5 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；Newsreader 元素 1,877，CJK Sans 元素 670）。
- P8 最小字号重测：仍 11.62pt（865 spans，560 处此字号）。
- KIT 同步完成：`WEEKLY-KIT.md` §七第 5 行（字体普查 P1 190/42/10/1、P8 537/350/23）、第 109 行（freeze r2 哈希）、第 111 行（P8 字号重测）、第 112–113 行（印/网新 SHA + 大小 + 文字层 101,106 字节）已更新；§八新增 D5 重建条目。`.text.md` 未变（SHA `52024e02…` 与 r2 一致，无需重出）。
- 清理：`freeze-r1/build-copy` 与 `freeze-r2/build-copy` 已删（core-fr scratch 43M→8.2M）；`freeze-r*.json`、基线与日志保留。
- core-fr 状态：**D5 完成，全部门禁通过，KIT 已同步。**

## fr-en（进行中）

### 修前基线（pre-D5，2026-11-12 07:47 UTC）
- p8 compare vs core-fr：CLEAN，keydiff=[150]（唯一读者语键，与全部 7 版一致）；freeze diff vs core-fr：added CJK 9（全 U+3000：P5 1、P7 1、P8 7）、added Latin 398。`baseline/p8-compare-core-pre.json`、`freeze-diff-pre.json`。
- census-pre：D5 拉丁 566（与 D5-CENSUS-130 一致），弯引号 0。

### D5 安装
- `apply_variant.py --target fr --reader en`（mode=latin）：10 项改动（Noto Sans faces、sans_noto cmaps、_CYR + family、_PATH rows、_QUOTE_CLS、fix2 块、D5 块、`_D5_READER='latin'`、italic 覆盖、sans 注释）。`assert_routing.py` latin：20/20 PASS（含 fix2 三引号 → news）。

### r1 门禁（07:48–07:53 UTC）：9 类缺陷，余者全绿
- run.py TOTAL 150，0 FLOW OVERFLOW，**6 HEAD TOO WIDE**：P3 `BEAUJOLAIS　BEAUJOLAIS QUIZ`、P6 `LIRE LE CALENDRIER　TIMETABLE`、P6/P7 `IL EST PRÉVU QUE + SUBJONCTIF` ×2、P6 `LE COMPARATIF EN POLITIQUE`、P7 `CLINIQUE DES ERREURS　ERRORS`。
- occlusion **3 TEXTX**：P1 头条 `ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI` vs `ALCARAZ CHAMPION` 222.2×20.8px（同基线左右锚）；P6 `TIMETABLE` vs `B1` 12.6×13.2；P7 `THE WEEK'S SENTENCES (ALL FROM THIS ISSUE)` vs `One grammar point + one mini-exercise…` 86.3×18.2（同基线左右锚）。
- boxtitle/creambox **7 DEFECT**（两工具逐项一致）：P1 `IN THIS ISSUE` +45.9、P3 `WINE WORDS` +12.9、P3 `LES DATES EN CHIFFRES` +7.6、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P5 `FILM WORDS` +15.7、P5 `FILMS` +31.3、P6 `TROIS DATES POUR COMPRENDRE` +24.5。
- 其余绿：render rc 0（印 PDF `cc3b3c47…` 17,031,628 B；网 PDF `8b013caf…` 1,622,981 B）；文字层逐字节一致（99,529 字符）；p8 121/150、CLEAN（vs core keydiff=[150] 与修前一致；vs 修前基线 keydiff=[]）；freeze baseline 8/8；spill 0；edge 0；census PASS（0/0/0）。
- freeze diff 注：added CJK 9→15（全 U+3000）；实测 SVG 内 U+3000 总数 366→372（+6，与 diff 增量一致）——系 D5 重排后折行处分隔符存留数变化，非新增内容（同 KIT 既有口径：P8 184→181 亦为折行消耗所致）；无非分隔符 CJK 新增。记 OBSERVE，不修。

### r1→r2 修复（15 处，全为内容侧）
- 与 core-fr 相同的 8 处（content 文件与 core 修前版字节相同，遂原样同步）：content34.py `head_zoom` 23→22、P4 框题 `tsize=21`；content56.py `head_cine` 23→20、语法头 25→23、`head_comp6` 25→24、P6 框题 `tsize=21`；content7.py 语法头 24→23、`head_clinic` 25→23。同步后三文件与 core-fr 当前版逐字节相同。
- 英文读者版特有 7 处（实测 `text_w` 定量后定）：
  1. expl.py `band_r1`：`ALCARAZ CHAMPION　SENATE VOTES WED` → `SENATE VOTES WED`（P1 间隙 −222.2→+122.7px；“ALCARAZ CHAMPION”与正上方主头条重复，且为读者层字符串，法语核心不动）。
  2. expl.py `head_phrases`：删 `(ALL FROM THIS ISSUE)`（P7 间隙 −86.1→+261.9px；该信息 P7 上文法语段已有“chaque phrase…vient d'un article de ce numéro”）。
  3. expl.py `head_lire`：`TIMETABLE` → `DATES`（25pt 下 480.1→406.2px < CW 422.5；本题问的即各投票日期）。
  4. content12.py:93 `sommaire_title` 24→21（446.0→390.2px advance，墨水约 371 < 378.5）。
  5. content34.py:76 `head_mots_fetes` 23→21（413.6→377.6px）。
  6. content56.py:76 `head_mots_photo` 23→21（416.4→380.1px）。
  7. content34.py:53 `head_dieppe_ex` 25→23（442.5→407.2px < CW 422.5）。
- `.text.md` 重出：`export47.py` 会把头两行写成 core-fr 简体中文头（脚本第 52/54 行 hardcode），已按修前版恢复英文头（`# Le Lucerna　FRENCH WEEKLY VOL.4` / `Week of 16–22 November 2026…`）；重出后 diff 仅 3 处预期改动，新 SHA `82f53a7a…`。**工具坑：凡 fan-out 重出 .text.md 必复核头两行。**

### r2（08:00–08:03 UTC）：余 1 处
- occlusion 0 flags、boxtitle 0 DEFECT、creambox PASS 0 defects、spill 0、edge 0、census PASS、文字层逐字节一致；p8 CLEAN；freeze 8/8。
- **余 1 处 HEAD TOO WIDE**：P7 `CLINIQUE DES ERREURS　ERRORS` 在 23pt 下仍超 6.1px（实测 428.6 vs CW 422.5）。修复：`content7.py:99` `head_clinic` 23→22（409.9，余量 12.6px）。
- 补查：`svglib.py` 与 core-fr 仅差 `_D5_READER` 一行（落盘批复要求，符合）；修前 fan-out svglib 与 core 修前 svglib 字节相同；`tools/occlusion_audit.py` 已含 §10 修复（裸 `Noto Sans` 量非 CJK 面，`resolve_font` L92–105）。

### r3（08:04–08:09 UTC）：全绿，fr-en 完成
- run.py TOTAL 150，0 FLOW OVERFLOW，**0 HEAD TOO WIDE**（`head_check.py` PASS）；render rc 0；webpdf rc 0。
- 印 PDF `La-Lucerna-VOL4-fr-en.pdf` 17,031,641 B，SHA-256 `0503cff0885d…`；网 PDF `La-Lucerna-VOL4-fr-en-web.pdf` 1,622,982 B，SHA-256 `11e5babac345…`；`.text.md` SHA-256 `82f53a7a…`（46,146 B，44,063 字符）。
- 文字层逐字节一致（各 100,705 字节）；occlusion 0 flags；p8 121/150 CLEAN（vs 核心 keydiff=[150] 与修前一致，vs 修前基线 keydiff=[]）；freeze baseline 8/8（p1 `62b4b174`、p2 `b18e2801`、p3 `0a722c78`、p4 `cf8c9d8b`、p5 `60dd199a`、p6 `43c36a0f`、p7 `9a4dffd3`、p8 `e4a16d38`）；freeze diff vs 核心 added CJK 14（全 U+3000）、vs 修前基线 5（全 U+3000）；boxtitle 0 DEFECT；creambox PASS 0 defects（n=522，中位 1.016、粗体 1.056、常规 0.998；P8 199→199 行、余量 38.1→38.1px）；spill 0；edge 0；census PASS（0/0/0）；`census_quotes.py` 弯引号缺陷 0。
- P8 最小字号重测 11.62pt（514 spans，260 处此字号）；P6 深读流终值 1258/1300（D5 重排，旧值 1288）。
- KIT 同步完成：§三（D5 差异清单）、§四（D5 r3 门禁值 + 新印/网 SHA + P8 字号）、§五 `.text.md` 新 SHA、§七新增 D5 重建条目。
- 清理：`freeze-r1/r2/r3/build-copy` 已删（fr-en scratch 9.2M）；`freeze-r*.json`、基线与日志保留。
- fr-en 状态：**D5 完成，全部门禁通过，KIT 已同步。**

## fr-es（进行中）

### 修前基线（pre-D5）
- p8 compare vs core-fr：CLEAN，keydiff=[150]；freeze diff vs core-fr：added CJK 9（全 U+3000）、added Latin 395。`baseline/p8-compare-core-pre.json`、`freeze-diff-pre.json`。
- census-pre：D5 拉丁 564（与 D5-CENSUS-130 一致），弯引号 0。基线核验：生产 svg/ 与 `baseline/svg/` SHA-256 逐一相同（BASELINE-FAITHFUL）。

### D5 安装
- `apply_variant.py --target fr --reader es`（mode=latin）：10 项改动（同 fr-en）。`assert_routing.py` latin：ROUTING PASS。`svglib.py` 与 core-fr 仅差 `_D5_READER` 一行。

### r1（08:0x–08:1x UTC）：4 HEAD TOO WIDE + 1 TEXTX + 5 框题
- run.py TOTAL 150，0 FLOW OVERFLOW，**4 HEAD TOO WIDE**：P6-ex `LIRE LE CALENDRIER　HORARIO`、P6-opinion 与 P7-B2 `IL EST PRÉVU QUE + SUBJONCTIF`、P6-micro `LE COMPARATIF EN POLITIQUE`。
- occlusion 1 TEXTX：P1 头条 vs `ALCARAZ GANA` 167.0×20.8px。
- boxtitle/creambox 5 DEFECT：P3 `LES DATES EN CHIFFRES` +7.6、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P4 `PALABRAS` +27.3、P5 `CINE` +14.3、P6 `TROIS DATES POUR COMPRENDRE` +24.5。
- 其余绿：文字层逐字节一致；p8 121/150 CLEAN（vs 核心 keydiff=[150]、vs 修前 keydiff=[]）；freeze 8/8（diff vs 核心 added CJK 8）；spill 0；edge 0；census PASS。
- 修复 11 处（r1→r2）：与核心相同的 8 处原样同步（同步后 content34/56/7.py 与核心字节相同）；es 特有 3 处：`band_r1` 删 `ALCARAZ GANA　`（间隙 −166.9→+96.6px）、`head_mots_tennis` 23→21（content34.py:171）、`head_lire` 25→23（content56.py:135，447.0→411.2）。`.text.md` 重出 + 西语头恢复，diff 仅 1 行（band_r1），新 SHA `7c340f2d…`（46,645 B，44,362 字符）。

### r2（08:24–08:35 UTC）：全绿，fr-es 完成
- run.py TOTAL 150，0 FLOW OVERFLOW，**0 HEAD TOO WIDE**（`head_check.py` PASS）；render rc 0；webpdf rc 0。
- 印 PDF `La-Lucerna-VOL4-fr-es.pdf` 17,031,451 B，SHA-256 `d732ed21b8be…`；网 PDF `La-Lucerna-VOL4-fr-es-web.pdf` 1,622,812 B，SHA-256 `aa1b3076782d…`；`.text.md` SHA-256 `7c340f2d…`。
- 文字层逐字节一致（各 100,880 字节）；occlusion 0；p8 121/150 CLEAN（vs 核心 keydiff=[150]，vs 修前 keydiff=[]）；freeze baseline 8/8（p1 `c1c81317`、p2 `cd1d01f4`、p3 `7964454d`、p4 `cb9ce4b2`、p5 `48b20dd5`、p6 `1948eab1`、p7 `4b6651dd`、p8 `030cc839`）；freeze diff vs 核心 added CJK 8（全 U+3000）、vs 修前基线 1（U+3000）；boxtitle 0 DEFECT；creambox PASS 0 defects（n=519，中位 1.01、粗体 1.056、常规 0.995；P8 207→207 行、余量 21.9→21.9px）；spill 0；edge 0；census PASS（0/0/0）；`census_quotes.py` 弯引号缺陷 0。
- P8 最小字号 11.62pt（251 spans）；流终值 P6-deep 1288/1300、P6-ex 2527/2560、P7-phrases 1806/1830、P8-keys 2167/2560（与旧 KIT 一致）。
- KIT 同步完成：§三（D5 差异清单）、§四（D5 r2 门禁值 + 新印/网 SHA + P8 字号）、§五 `.text.md` 新 SHA、§七新增 D5 重建条目。
- 清理：`freeze-r1/r2/build-copy` 已删（fr-es scratch 8.7M）；`freeze-r*.json`、基线与日志保留。
- fr-es 状态：**D5 完成，全部门禁通过，KIT 已同步。**

## fr-de（进行中）

### 修前基线（pre-D5）
- p8 compare vs core-fr：CLEAN，keydiff=[150]；freeze diff vs core-fr：added CJK 7、added Latin 403；census-pre：D5 拉丁 570。基线核验：生产 svg/ 与 `baseline/svg/` SHA-256 逐一相同（BASELINE-FAITHFUL）。

### D5 安装
- `apply_variant.py --target fr --reader de`（mode=latin）：10 项改动。`assert_routing.py` latin：ROUTING PASS。`svglib.py` 与 core-fr 仅差 `_D5_READER` 一行。

### r1（08:3x–08:4x UTC）：9 HEAD TOO WIDE + 4 遮挡 + 9 框题
- run.py TOTAL 150，0 FLOW OVERFLOW，**9 HEAD TOO WIDE**：P3-main `BEAUJOLAIS　BEAUJOLAIS-QUIZ`、P4-micro 与 P6-micro `MICRO-DRILLS　KURZÜBUNGEN`、P6-ex `LIRE LE CALENDRIER　KALENDER`、P6-opinion 与 P7-B2 `IL EST PRÉVU QUE + SUBJONCTIF`、P6-micro `LE COMPARATIF EN POLITIQUE`、P7-outils `BOÎTE À OUTILS　WERKZEUG`、P7-clinic `CLINIQUE DES ERREURS　FEHLER`。
- occlusion 4 flags：P1 头条 vs `ALCARAZ SIEGT` 127.3×20.8px；P6 `HAUSHALTSKALENDER (ABSTIMMUNG MITTWOCH)` LINEX 越框；P6 `LE COMPARATIF EN POLITIQUE` vs 该长标题 41.0×8.2px；P7 金句头 vs 副标 134.9×18.2px。
- boxtitle/creambox 9 DEFECT：P3 `WEINWÖRTER` +25.9、P3 `LES DATES EN CHIFFRES` +7.6、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P4 `WÖRTER` +5.3、P4 `FORTSETZUNG FOLGT` +19.7、P5 `FILMWÖRTER` +28.7、P5 `FILME` +33.3、P6 `HAUSHALTSKALENDER (ABSTIMMUNG MITTWOCH)` +68.7、P6 `TROIS DATES POUR COMPRENDRE` +24.5。
- 其余绿：文字层逐字节一致；p8 121/150 CLEAN（vs 核心 keydiff=[150]、vs 修前 keydiff=[]）；freeze 8/8（diff vs 核心 added CJK 12）；spill 0；edge 0；census PASS。
- 修复 19 处（r1→r2）：与核心相同的 8 处原样同步（`content7.py` 的 `head_clinic` 例外：核心 23→de 22）；de 特有 11 处：`band_r1` 删 `ALCARAZ SIEGT　`（间隙 −127.3→+137.9px）、`head_phrases` 删 ` (ALLE AUS DIESER AUSGABE)`（墨尾 895.0，副标起 1190.9，间隙 +295.9px）、`head_chart` `HAUSHALTSKALENDER (ABSTIMMUNG MITTWOCH)`→`KALENDER`（第二段墨宽 683.3→147.4，框内余量 141.8，另降 24→22pt）、`head_lire` 25→22（23pt 仍超 10.0px）、`head_dieppe_ex` 25→23、`head_micro` 24→23 与 `head_micro6` 25→23、`head_outils` 27→25、`head_clinic` →22（23pt 仍超 6.2px，与 fr-en 同）、`head_mots_fetes` 23→21、`head_mots_tennis` 23→22、`head_mots_photo` 23→21、`head_asuivre` 23→21。`.text.md` 重出 + 德语头恢复，diff 仅 3 行（band_r1、head_chart、head_phrases），新 SHA `de37011a…`（46,559 B，44,357 字符）。

### r2（08:52–08:59 UTC）：全绿，fr-de 完成
- run.py TOTAL 150，0 FLOW OVERFLOW，**0 HEAD TOO WIDE**（`head_check.py` PASS）；render rc 0；webpdf rc 0。
- 印 PDF `La-Lucerna-VOL4-fr-de.pdf` 17,035,304 B，SHA-256 `234a877ebbbb…`；网 PDF `La-Lucerna-VOL4-fr-de-web.pdf` 1,626,645 B，SHA-256 `68c62c41b596…`；`.text.md` SHA-256 `de37011a…`。
- 文字层逐字节一致（各 100,921 字节）；occlusion 0；p8 121/150 CLEAN（vs 核心 keydiff=[150]，vs 修前 keydiff=[]）；freeze baseline 8/8（p1 `37a032bd`、p2 `de95d62e`、p3 `0e3deb9a`、p4 `1e82cf09`、p5 `6aac1fce`、p6 `21238dce`、p7 `55bd0e43`、p8 `55774270`）；freeze diff vs 核心 added CJK 11（全 U+3000）、vs 修前基线 7（全 U+3000）；boxtitle 0 DEFECT（34 titles，296 body lines）；creambox PASS 0 defects；spill 0；edge 0；census PASS（0/0/0）；`census_quotes.py` 弯引号缺陷 0。
- P8 最小字号 11.62pt（248 spans）；流终值 P6-deep 1288/1300、P6-ex 2527/2560、P7-phrases 1806/1830、P8-keys 2126/2560。
- KIT 同步完成：§三（D5 差异清单）、§四（D5 r2 门禁值 + 新印/网 SHA + P8 字号）、§五 `.text.md` 新 SHA、§七新增 D5 重建条目。
- 清理：`freeze-r1/r2/build-copy` 已删（fr-de scratch 8.7M）；`freeze-r*.json`、基线与日志保留。
- fr-de 状态：**D5 完成，全部门禁通过，KIT 已同步。**

## fr-pt（进行中）

### 修前基线（pre-D5）
- p8 compare vs core-fr：CLEAN，keydiff=[150]；freeze diff vs core-fr：added CJK 11、added Latin 398；census-pre：D5 拉丁 565。基线核验：生产 svg/ 与 `baseline/svg/` SHA-256 逐一相同（BASELINE-FAITHFUL）。

### D5 安装
- `apply_variant.py --target fr --reader pt`（mode=latin）：10 项改动。`assert_routing.py` latin：ROUTING PASS。`svglib.py` 与 core-fr 仅差 `_D5_READER` 一行。

### r1（09:0x–09:1x UTC）：5 HEAD TOO WIDE + 3 遮挡 + 6 框题
- run.py TOTAL 150，0 FLOW OVERFLOW，**5 HEAD TOO WIDE**：P6-ex `LIRE LE CALENDRIER　HORÁRIO`、P6-opinion 与 P7-B2 `IL EST PRÉVU QUE + SUBJONCTIF`、P6-micro `LE COMPARATIF EN POLITIQUE`、P7-outils `BOÎTE À OUTILS　UTENSÍLIOS`。
- occlusion 3 flags：P1 头条 vs `ALCARAZ VENCE` 198.0×20.8px；P6 `CALENDÁRIO DO ORÇAMENTO (VOTO QUARTA-FEIRA)` LINEX 越框；P6 `LE COMPARATIF EN POLITIQUE` vs 该长标题 60.7×12.5px。
- boxtitle/creambox 6 DEFECT：P3 `LES DATES EN CHIFFRES` +7.6、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P4 `PALAVRAS` +27.3、P5 `CINEMA` +57.3、P6 `CALENDÁRIO DO ORÇAMENTO (VOTO QUARTA-FEIRA)` +88.7、P6 `TROIS DATES POUR COMPRENDRE` +24.5。
- 其余绿：文字层逐字节一致；p8 121/150 CLEAN（vs 核心 keydiff=[150]、vs 修前 keydiff=[]）；freeze 8/8（diff vs 核心 added CJK 12）；spill 0；edge 0；census PASS。观察项：creambox P8 slack 34.1→32.6（行数不变，D5 重排微移，非缺陷）。
- 修复 13 处（r1→r2）：与核心相同的 8 处原样同步；pt 特有 5 处：`band_r1` 删 `ALCARAZ VENCE　`（间隙约 −198→+87px）、`head_chart` `CALENDÁRIO DO ORÇAMENTO (VOTO QUARTA-FEIRA)`→`CALENDÁRIO` + 24→20pt（第二段墨宽 703.0→约 137，框内余量 141.8）、`head_lire` 25→23、`head_outils` 27→25、`head_mots_tennis` 23→21（22pt 墨宽约 380 仍擦边）。`.text.md` 重出 + 葡语头恢复，diff 仅 2 行（band_r1、head_chart），新 SHA `12a860a9…`（46,486 B，44,145 字符）。

### r2（09:15–09:23 UTC）：全绿，fr-pt 完成
- run.py TOTAL 150，0 FLOW OVERFLOW，**0 HEAD TOO WIDE**（`head_check.py` PASS）；render rc 0；webpdf rc 0。
- 印 PDF `La-Lucerna-VOL4-fr-pt.pdf` 17,031,944 B，SHA-256 `8c01de5f3691…`；网 PDF `La-Lucerna-VOL4-fr-pt-web.pdf` 1,623,290 B，SHA-256 `a62233ec10cd…`；`.text.md` SHA-256 `12a860a9…`。
- 文字层逐字节一致（各 100,788 字节）；occlusion 0；p8 121/150 CLEAN（vs 核心 keydiff=[150]，vs 修前 keydiff=[]）；freeze baseline 8/8（p1 `bb8ffdf8`、p2 `8b3d442f`、p3 `7ee87f1b`、p4 `ed6eff64`、p5 `84b27038`、p6 `23df0293`、p7 `9667cc32`、p8 `1da78777`）；freeze diff vs 核心 added CJK 12（全 U+3000）、vs 修前基线 1（U+3000）；boxtitle 0 DEFECT（36 titles，289 body lines）；creambox PASS 0 defects；spill 0；edge 0；census PASS（0/0/0）；`census_quotes.py` 弯引号缺陷 0。
- P8 最小字号 11.62pt（255 spans）；流终值 P6-deep 1288/1300、P6-ex 2527/2560、P7-phrases 1778/1830、P8-keys 2106/2560。
- KIT 同步完成：§三（D5 差异清单）、§四（D5 r2 门禁值 + 新印/网 SHA + P8 字号）、§五 `.text.md` 新 SHA、§七新增 D5 重建条目。
- 清理：`freeze-r1/r2/build-copy` 已删（fr-pt scratch 8.7M）；`freeze-r*.json`、基线与日志保留。
- fr-pt 状态：**D5 完成，全部门禁通过，KIT 已同步。**

## 自查：生产原地重建核验（2026-11-12，协调员紧急纠正通知后）

- 机制确认：`run_gates.sh` 开头即 `cd "$W/production/2026-w47/$SLUG"`，run.py/render.py/webpdf.py 均在生产目录原地执行，印/网 PDF 直接写进生产目录；`shas.txt` 即对生产文件哈希。唯一的 build-copy 是 `freeze.py baseline --build . --out $S/<slug>/freeze-<tag>` 的确定性校验副本（只验 SVG 哈希，不产 PDF），每轮后已删——与 nl 工人“在 build-copy 里建完不回同步”的模式不同。
- 三项验收逐版核对（生产印/网/text SHA vs 终轮门禁 `logs-*/shas.txt` vs KIT §四/§五；生产 `svglib.py` 含 `_D5_READER`）：core-fr、fr-en、fr-es、fr-de、fr-pt **5 版全部 PASS**——生产 SHA = 日志 SHA = KIT SHA，`_D5_READER` 各 5 处。核对值：core-fr 印 `f36c32f020e4`/网 `ff08e74903d6`/文 `52024e024d32`；fr-en 印 `0503cff0885d`/网 `11e5babac345`/文 `82f53a7aa6af`；fr-es 印 `d732ed21b8be`/网 `aa1b3076782d`/文 `7c340f2d9ede`；fr-de 印 `234a877ebbbb`/网 `68c62c41b596`/文 `de37011a23a0`；fr-pt 印 `8c01de5f3691`/网 `a62233ec10cd`/文 `12a860a9b4e1`（各前 12 位）。
- 结论：已完成 5 版均为生产原地重建，无需重做、无需补同步。此后每版报完成前仍按此三项逐版核对。

## fr-it（进行中）

### 修前基线（pre-D5）
- p8 compare vs core-fr：CLEAN，keydiff=[150]；freeze diff vs core-fr：added CJK 11、added Latin 393；census-pre：D5 拉丁 563。基线核验：生产 svg/ 与 `baseline/svg/` SHA-256 逐一相同（BASELINE-FAITHFUL）。

### D5 安装
- `apply_variant.py --target fr --reader it`（mode=latin）：10 项改动。`assert_routing.py` latin：ROUTING PASS。`svglib.py` 与 core-fr 仅差 `_D5_READER` 一行。

### r1（09:2x–09:5x UTC）：4 HEAD TOO WIDE + 1 TEXTX + 6 框题
- 说明：首跑在 render.py 阶段被运行时重启打断（render.log 0 字节，生产 PDF 仍为 11-11 旧版）；无残留进程；原样重跑 r1 完成，run.py 结果与中断前一致（同 4 处 HEAD TOO WIDE）。
- run.py TOTAL 150，0 FLOW OVERFLOW，**4 HEAD TOO WIDE**：P6-ex `LIRE LE CALENDRIER　ORARIO`、P6-opinion 与 P7-B2 `IL EST PRÉVU QUE + SUBJONCTIF`、P6-micro `LE COMPARATIF EN POLITIQUE`。
- occlusion 1 TEXTX：P1 头条 vs `ALCARAZ VINCE` 156.8×20.8px。
- boxtitle/creambox 6 DEFECT：P1 `SOMMARIO` +16.9、P3 `LES DATES EN CHIFFRES` +7.6、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P5 `CINEMA` +57.3、P6 `CALENDARIO DEL BILANCIO (VOTO MERCOLEDÌ)` +18.7、P6 `TROIS DATES POUR COMPRENDRE` +24.5。
- 其余绿：文字层逐字节一致；p8 121/150 CLEAN（vs 核心 keydiff=[150]、vs 修前 keydiff=[]）；freeze 8/8（diff vs 核心 added CJK 13）；spill 0；edge 0；census PASS。
- 修复 12 处（r1→r2）：与核心相同的 8 处原样同步；it 特有 4 处：`band_r1` 删 `ALCARAZ VINCE　`（间隙 −156.8→+112.6px）、`sommaire_title` 24→22（417.8→383.0）、`head_chart` `CALENDARIO DEL BILANCIO (VOTO MERCOLEDÌ)`→`CALENDARIO` + 24→20pt（与 pt 同类处理）、`head_lire` 25→23（391.2 < 422.5）。`.text.md` 重出 + 意大利语头恢复，diff 仅 2 行（band_r1、head_chart），新 SHA `030e3615…`（46,570 B，44,403 字符）。

### r3（09:53–10:03 UTC）：全绿，fr-it 完成
- run.py TOTAL 150，0 FLOW OVERFLOW，**0 HEAD TOO WIDE**（`head_check.py` PASS）；render rc 0；webpdf rc 0。
- 印 PDF `La-Lucerna-VOL4-fr-it.pdf` 17,027,791 B，SHA-256 `5d31cbc41f0a…`；网 PDF `La-Lucerna-VOL4-fr-it-web.pdf` 1,619,122 B，SHA-256 `20b66275d46c…`；`.text.md` SHA-256 `ac5c096d…`（46,528 B，44,361 字符）。
- 文字层逐字节一致（各 102,893 字节）；occlusion 0；p8 121/150 CLEAN（vs 核心 keydiff=[150]，vs 修前 keydiff=[]）；freeze baseline 8/8（p1 `d29ae84b`、p2 `d249091a`、p3 `ea4c9a4a`、p4 `c552e302`、p5 `09d10b95`、p6 `a3eb8c2d`、p7 `37c8c3f2`、p8 `fe0959c6`）；freeze diff vs 核心 added CJK 14（全 U+3000）、vs 修前基线 4（全 U+3000）；boxtitle 0 DEFECT（38 titles，286 body lines）；creambox PASS 0 defects；spill 0；edge 0；census PASS（0/0/0）；`census_quotes.py` 弯引号缺陷 0；PDF 8 页、内嵌图 6 枚（Hiroshige 已恢复）。
- P8 最小字号 11.62pt（254 spans）；流终值 P6-deep 1288/1300、P6-ex 2527/2560、P7-phrases 1778/1830、P8-keys 2167/2560。
- KIT 同步完成：§三（D5 差异清单）、§四（D5 r3 门禁值 + 新印/网 SHA + P8 字号）、§五 `.text.md` 新 SHA、§七新增 D5 重建条目。
- 三项验收（协调员纠正通知后复核）：生产印/网/text SHA = r3 日志 `shas.txt` = KIT；生产 `svglib.py` 含 `_D5_READER`（5 处）。PASS。
- 清理：`freeze-r1/r2/r3/build-copy` 已删（fr-it scratch 9.3M）；`freeze-r*.json`、基线与日志保留。
- fr-it 状态：**D5 完成，全部门禁通过，KIT 已同步。**

## fr-nl（进行中）

### 修前基线（pre-D5）
- p8 compare vs core-fr：CLEAN，keydiff=[150]；freeze diff vs core-fr：added CJK 8、added Latin 394；census-pre：D5 拉丁 565。基线核验：生产 svg/ 与 `baseline/svg/` SHA-256 逐一相同（BASELINE-FAITHFUL）。

### D5 安装
- `apply_variant.py --target fr --reader nl`（mode=latin）：10 项改动。`assert_routing.py` latin：ROUTING PASS。`svglib.py` 与 core-fr 仅差 `_D5_READER` 一行。

### r1（10:0x–10:1x UTC）：4 HEAD TOO WIDE + 1 TEXTX + 4 框题
- run.py TOTAL 150，0 FLOW OVERFLOW，**4 HEAD TOO WIDE**：P6-ex `LIRE LE CALENDRIER　AGENDA`、P6-opinion 与 P7-B2 `IL EST PRÉVU QUE + SUBJONCTIF`、P6-micro `LE COMPARATIF EN POLITIQUE`。
- occlusion 1 TEXTX：P1 头条 vs `ALCARAZ WINT` 131.0×20.8px。
- boxtitle/creambox 4 DEFECT：P3 `LES DATES EN CHIFFRES` +7.6、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P4 `WOORDEN` +27.3、P6 `TROIS DATES POUR COMPRENDRE` +24.5。
- 其余绿：文字层逐字节一致；p8 121/150 CLEAN（vs 核心 keydiff=[150]、vs 修前 keydiff=[]）；freeze 8/8（diff vs 核心 added CJK 9）；spill 0；edge 0；census PASS。注意：`head_chart` `LE CALENDRIER　BEGROTINGSKALENDER (STEMMING WO.)` 未被 flag（框内放得下，与 de/pt/it 不同），未动。
- 修复 11 处（r1→r2）：与核心相同的 8 处原样同步；nl 特有 3 处：`band_r1` 删 `ALCARAZ WINT　`（间隙 −131.0→+127.5px）、`head_lire` 25→23（434.7→399.9）、`head_mots_tennis` 23→21（22pt 墨宽约 381 仍擦边）。`.text.md` 重出 + 荷兰语头恢复，diff 仅 1 行（band_r1），新 SHA `4a4a9fcc…`（46,250 B，44,135 字符）。

### r2（10:18–10:26 UTC）：全绿，fr-nl 完成
- run.py TOTAL 150，0 FLOW OVERFLOW，**0 HEAD TOO WIDE**（`head_check.py` PASS）；render rc 0；webpdf rc 0。
- 印 PDF `La-Lucerna-VOL4-fr-nl.pdf` 17,029,995 B，SHA-256 `c0c12aea4176…`；网 PDF `La-Lucerna-VOL4-fr-nl-web.pdf` 1,621,369 B，SHA-256 `36493cef193a…`；`.text.md` SHA-256 `4a4a9fcc…`。
- 文字层逐字节一致（各 99,546 字节）；occlusion 0；p8 121/150 CLEAN（vs 核心 keydiff=[150]，vs 修前 keydiff=[]）；freeze baseline 8/8（p1 `221e81b8`、p2 `8584b196`、p3 `97e66d66`、p4 `7e787816`、p5 `8cb8b633`、p6 `7737c6a9`、p7 `b57c92e0`、p8 `d17281f2`）；freeze diff vs 核心 added CJK 9（全 U+3000）、vs 修前基线 2（全 U+3000）；boxtitle 0 DEFECT（38 titles，285 body lines）；creambox PASS 0 defects（n=520，中位 1.016、粗体 1.056、常规 0.997；P8 198→197 行、余量 36.6→36.6px）；spill 0；edge 0；census PASS（0/0/0）；`census_quotes.py` 弯引号缺陷 0；PDF 8 页、内嵌图 6 枚。
- P8 最小字号 11.62pt（250 spans）；流终值 P6-deep 1288/1300、P6-ex 2527/2560、P7-phrases 1718/1830、P8-keys 2106/2560。
- KIT 同步完成（本版 KIT 为英文结构）：Files（新印/网/text SHA + D5 r2 freeze 哈希 + P8 字号 + D5 源码冻结行）、新增 `## D5 rebuild (2026-11-12)` 一节。
- 三项验收：生产印/网/text SHA = r2 日志 `shas.txt` = KIT；生产 `svglib.py` 含 `_D5_READER`（5 处）。PASS。
- 清理：`freeze-r1/r2/build-copy` 已删（fr-nl scratch 8.7M）；`freeze-r*.json`、基线与日志保留。
- fr-nl 状态：**D5 完成，全部门禁通过，KIT 已同步。**

## fr-ru（进行中）

### 修前基线（pre-D5）
- p8 compare vs core-fr：CLEAN，keydiff=[150]；freeze diff vs core-fr：added CJK 15、added Latin 232；census-pre：D5 拉丁 450 + 西里尔 301。基线核验：生产 svg/ 与 `baseline/svg/` SHA-256 逐一相同（BASELINE-FAITHFUL）。

### D5 安装
- `apply_variant.py --target fr --reader ru`（mode=ru）：10 项改动。`assert_routing.py` ru：ROUTING PASS。`svglib.py` 与 core-fr 仅差 `_D5_READER` 一行（`"ru"` vs `"cjk"`）。

### r1（~10:3x–10:5x UTC）：首轮全绿（除 creambox 3 误报），fr-ru 完成
- run.py TOTAL 150，0 FLOW OVERFLOW，**0 HEAD TOO WIDE**；render rc 0；webpdf rc 0。
- 印 PDF `La-Lucerna-VOL4-fr-ru.pdf` 17,331,940 B，SHA-256 `3459a9b9d3ed…`；网 PDF `La-Lucerna-VOL4-fr-ru-web.pdf` 1,882,129 B，SHA-256 `ccfba10759e7…`；`.text.md` SHA-256 `9aa919b7c647…`（50,418 B；mtime 2026-11-11 18:34 UTC——r1 未动此文件，与重建 #2 KIT 记录 50,453 B 差 35 B 属修前既有，头已验为俄语）。
- 文字层逐字节一致（各 97,297 字符，multiset diff 0）；occlusion 0（selftest OK）；p8 121/150 CLEAN（vs 核心 keydiff=[150]，vs 修前 keydiff=[]）；freeze baseline 8/8（p1 `08fa5423`、p2 `bd65bf21`、p3 `e21de010`、p4 `37754b6c`、p5 `efc93cdc`、p6 `ee01d3e6`、p7 `44dae27c`、p8 `10644821`）；freeze diff vs 核心 added CJK 7（全 U+3000）、vs 修前基线 added CJK **0**；boxtitle 0 DEFECT（41 titles，358 body lines）；spill 0（33 boxes，106 candidates）；edge 0；census PASS（0/0/0）；`census_quotes.py` 弯引号缺陷 0；PDF 8 页、内嵌图 6 枚（P8 Hiroshige 在位）。
- P8 最小字号 11.625pt（502 spans，244 at min）；流终值 P6-deep 1288/1300、P6-ex 2527/2560、P7-phrases 1718/1830、P8-keys 2086/2560（Hiroshige 阈值 2170，余量 84）。
- 核心 8 处字号修复**未应用**：ru 版 heads 在修前字号下已放得下（head_zoom 23、head_cine 23、语法头 25、head_clinic 25、无 P4 `tsize=21`），r1 三门禁皆 0——content34/56/7.py 与 core-fr 仅差这些字号。强行同步核心字号只会无故缩小 ru heads，不做。
- creambox r1 报 FAIL 3 defects——**裁定为测量误报**（与试点 P8 `·` TEXTX 误报同类，已收回、不改内容）：3 条全是 P5 `debat5_note`（Кино или дома? …）。D5 回流使第一处重排（西里尔在 Noto Sans 下更宽：首行 `Кино или дома? Старая вещь обретёт`→`Кино или дома? Старая вещь`），修前原字符串仅在第二处（y=2326.6） verbatim 存活；审计按精确文本取 `cands[0]` 判为“spilled below box”。现版 P5 SVG 实测：第一处 3 行 y=780.6/811.0/841.5 全在 box#1 内（底 887.9），全句完整无截断；第二处与修前位置相同；独立 spill_sweep 0 SPILL。**工具缺陷类**：审计需按词覆盖匹配而非精确文本取首候选——机制方修，不改内容；中途不改共享机制工具（他家也在跑）。
- KIT 同步完成（Files 新印/网/text SHA + D5 r1 freeze 哈希 + P8 字号 + D5 源码冻结行，新增 `## D5 rebuild (2026-11-12)` 一节，含上述 creambox 裁定与 8 处修复未应用的说明）。
- 三项验收：生产印/网/text SHA = r1 日志 `shas.txt` = KIT；生产 `svglib.py` 含 `_D5_READER = "ru"`（第 100 行，共 5 处）。PASS。
- 清理：`freeze-r1` build-copy 已删；`freeze-r1.json`、基线与日志保留。磁盘 /home/hatch 93G/150G（57G 空闲，<100G 门限）。
- fr-ru 状态：**D5 完成，全部门禁通过（creambox 3 误报已裁定），KIT 已同步。**
- 附：期间收到运行时 house-rules 提示，重读 `~/workspace/weekly-git/AGENTS.md` 全文（repo 层加版流程：issues/lint/covers——本次只动 production/2026-w47/，不 commit、不跑 lint --write，无冲突）。

## CJK 读者版（进行中：fr-ja 已装，r1 跑着；fr-ko、fr-zh-tw 待装）

- 修前基线已建（09:3x UTC）：每版 `baseline/`（svg ×8 + svglib.py + assets 全量）+ `census-pre.json` + `p8-extract-pre.json` + `baseline/p8-compare-core-pre.json` + `baseline/freeze-diff-pre.json`。修前 svglib md5 均为 `f25bfcfc`（与 Latin/Russian 修前版相同），含 0 处 `_D5_READER`。
- census-pre：fr-ja 445、fr-ko 442、fr-zh-tw 439（与 D5-CENSUS-130 一致）；p8 compare vs core-fr 均为 CLEAN，keydiff=[150]；freeze diff vs core-fr：fr-ja added CJK 2329/Latin 231、fr-ko 2564/227、fr-zh-tw 971/224。
- moth 在位（3 版均有 `assets/lucerna-moth.svg`），svg 各 8 页。待：mode=cjk 安装 + 全套门禁；fr-ko 注意 freeze Pillow 10 例外（仅 freeze 一步可用系统 python3，先确认其确有 Pillow 10）。
- **fr-ja 已装（fr-ru r1 等待期间，mode=cjk）**：`apply_variant.py --target fr --reader ja`，输出含 "CJK index SC -> JP; ported kinsoku block from core-zh-tw"；`assert_routing.py` cjk PASS（`_D5_READER='cjk'`）；装前基线核验 BASELINE-FAITHFUL。注意：fr-ja svglib 与 core-fr **不止差 `_D5_READER` 一行**——按 CJK 设计另有 JP 索引（`_jp_index` vs `_sc_index`）、"Noto Serif/Sans CJK JP" 字族、以及从 core-zh-tw 移植的 kinsoku 块（244–386 行）；与修前 fr-ja svglib 的 diff 恰为安装器的改动（D5 sans 块 + fix2 块 + `_D5_READER` + JP 索引/字族 + kinsoku 移植）。“仅差 `_D5_READER` 一行”的落盘批复只适用于 Latin/Russian 版；CJK 版按 CJK-DECISION 执行，不改回 core。
- **fr-ja r1 已起**（后台，`run_gates.sh 2026-w47-fr-ja ja La-Lucerna-VOL4-fr-ja.pdf La-Lucerna-VOL4-fr-ja-web.pdf r1`，日志 `2026-w47-fr-ja/logs-r1-driver.log`）。

### fr-ja r1（~10:5x–11:0x UTC）：4 超宽头 + 1 TEXTX + 3 框题
- run.py TOTAL 150，0 FLOW OVERFLOW，**4 HEAD TOO WIDE**：P6-ex `LIRE LE CALENDRIER　カレンダー`、P6-opinion 与 P7-B2 `IL EST PRÉVU QUE + SUBJONCTIF`、P6-micro `LE COMPARATIF EN POLITIQUE`。
- occlusion 1 TEXTX：P1 头条 vs 日文 band `アルカラス優勝　上院は水曜に採決` 9.2×26.0px。
- boxtitle/creambox 3 DEFECT：P3 `LES DATES EN CHIFFRES` +7.6、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P6 `TROIS DATES POUR COMPRENDRE` +24.5。
- 其余绿：文字层逐字节一致（各 93,216 字符）；p8 121/150 CLEAN（vs 核心 keydiff=[150]、vs 修前 keydiff=[]）；freeze 8/8（diff vs 核心 added CJK 2330）；spill 0；edge 0；census PASS。
- 修复 10 处（r1→r2）：与核心相同的 8 处原样同步；ja 特有 2 处：`band_r1` 删 `アルカラス優勝　`（→`上院は水曜に採決`）、`head_lire` 25→23（实测 441.5→406.2px < CW 422.5）。修前 `.text.md` 副本补存为 `text-md-pre-fix.md`（原先缺失；SHA `aca65425…`，日文头已验）。
- **fr-ko 已装**（fr-ja r2 等待期间，mode=cjk）：`apply_variant.py --target fr --reader ko`，输出 "CJK index SC -> KR"（**无** kinsoku 移植——安装器仅为 ja 移植；ko svglib kinsoku 计数 0，ja 为 4，属安装器设计）；`assert_routing.py` cjk PASS。修前 svglib md5 `f25bfcfc`，基线核验 BASELINE-FAITHFUL，moth 在位。修前 `.text.md` 副本已存（SHA `f5474d61…`，韩文头已验）。

### fr-ja r2（~11:0x UTC）：全绿，fr-ja 完成
- run.py TOTAL 150，0 FLOW OVERFLOW，**0 HEAD TOO WIDE**；render rc 0；webpdf rc 0。
- 印 PDF `La-Lucerna-VOL4-fr-ja.pdf` 20,148,505 B，SHA-256 `a62d3c89d9a9…`；网 PDF `La-Lucerna-VOL4-fr-ja-web.pdf` 2,019,098 B，SHA-256 `bc8eb6e62d2b…`；`.text.md` SHA-256 `df028d09d5db…`（47,508 B，542 entries，150 exercises；export47.py 重出 + 日文头恢复，diff vs 修前仅 1 行 band_r1）。
- 文字层逐字节一致（各 93,208 字符——较 r1 少 8 字符，正是删掉的 `アルカラス優勝　`）；occlusion 0；p8 121/150 CLEAN（vs 核心 keydiff=[150]，vs 修前 keydiff=[]）；freeze baseline 8/8（p1 `0afa9c6a`、p2 `21be28bf`、p3 `7b93df4b`、p4 `77b198c9`、p5 `1fae947b`、p6 `0f3a0e99`、p7 `f1a9c6bc`、p8 `bdde8366`）；freeze diff vs 核心 added CJK 2323、vs 修前基线 added CJK **1**（1 个 U+3000 回流分隔符，可接受）；boxtitle 0 DEFECT（41 titles，394 body lines）；creambox PASS 0 defects（n=495，中位 1.014、粗体 1.049、常规 1.002；P8 191→191 行、余量 37.1→37.1px）；spill 0；edge 0；census PASS（0/0/0）；`census_quotes.py` 弯引号缺陷 0；PDF 8 页、内嵌图 6 枚。
- P8 最小字号 11.625pt（834 spans，551 at min）；流终值 P6-deep 1258/1300、P6-ex 2402/2560、P7-phrases 1718/1830、P8-keys 2106/2560（Hiroshige 阈值 2170，余量 64）。
- KIT 同步完成（`## Files delivered` 新印/网/text SHA + D5 r2 freeze 哈希 + P8 字号，新增 `## D5 rebuild (2026-11-12)` 一节，含 source_freeze 的 CJK 注记：ja svglib 与 core 按设计不同，不改回 core）。
- 三项验收：生产印/网 SHA = r2 日志 `shas.txt` = KIT；text SHA = 重出后的 `df028d09d5db…` = KIT（r2 `shas.txt` 记的是重出前 SHA `aca65425…`，属时序差，非不符）；生产 `svglib.py` 含 `_D5_READER = "cjk"`（第 100 行，共 5 处）。PASS。
- 清理：`freeze-r1/r2` build-copy 已删；`freeze-r*.json`、基线与日志保留。
- fr-ja 状态：**D5 完成，全部门禁通过，KIT 已同步。**

### fr-ko r1（进行中，~11:01 UTC 起）
- `run_gates.sh 2026-w47-fr-ko ko La-Lucerna-VOL4-fr-ko.pdf La-Lucerna-VOL4-fr-ko-web.pdf r1` 后台运行中。注意 ko freeze 例外：若 freeze 在 venv 下 ABORT（Pillow 10 要求），仅 freeze 一步用系统 python3 跑一次（先确认系统 python3 确有 Pillow 10；没有则上报，不绕门）。

### fr-ko r1（~11:01–11:2x UTC）：3 超宽头 + 3 框题 + p8 SHORT 缺 Q150
- run.py TOTAL 150，0 FLOW OVERFLOW，**3 HEAD TOO WIDE**：P6-opinion 与 P7-B2 `IL EST PRÉVU QUE + SUBJONCTIF`、P6-micro `LE COMPARATIF EN POLITIQUE`（head_lire 未超——韩文 gloss 短；band 无 TEXTX）。
- occlusion 0；boxtitle/creambox 3 DEFECT（同款 3 法文框题 +7.6/+36.5/+24.5）；freeze 8/8（diff vs 核心 added CJK 2560）；文字层逐字节一致（各 95,053 字符）；spill 0；edge 0；census PASS；流终值 P8-keys 2086/2560。
- **p8 compare vs 核心与 vs 修前均为 SHORT，missing=[150]**（注记 120 vs 121）：Q150 注记在现版 P8 SVG 里**实际存在且位置正确**（y=2036.7/2056.8，全句完整）——是 p8.py 解析失败，不是渲染缺失。根因：D5 把注记拆成 ~30 个按文字分流的小 `<text>`，断行恰落在 `—` 之后，行首空格被 svglib wrap() 丢掉，join 后成 `자유 작문 —채점…`（` — ` 变 ` —`）；`detect_note` 的 `" — "` 测试失手，落到 paren 分支，`last_paren_group()` 取到吞进末条的 P8 图注 `(1797-1858)`，整条 key 判错。基线与现版末条吞图注的行为完全相同（238 vs 237 字符），只差这一个空格。
- 另：PDF 文字层里该注记词间空格亦丢失（`자유작문—채점포인트는상자안`）——与 fr-ru KIT 已记的“lost spaces”同类（run 首空格被 CairoSVG 丢掉），视觉排版正确（各 run 按 x 定位，词间距正常），属已知 svglib 局限，不在 builder 范围；不改韩文内容迁就它。
- 修复（r1→r2）：内容只做与核心相同的 8 处（head_lire、band_r1 均不动——r1 未 flag）；**工具侧修了共享 `tools/p8.py`**（`detect_note` 顶部：` —` 后紧跟 CJK 字符时补回空格——源 E 值里的 dash 两侧恒有空格，无空格只可能是 D5 丢空格 artifact；正则仅覆盖 ` —`+CJK，不动拉丁/俄文分支）。回归验证：单元测试 dash/CJK→(True,'자유 작문','dash')，拉丁/俄文用例不变；全量 extract：fr-ko 现版注记 120→**121**、key150=`자유 작문`，fr-ko 基线 121 不变，fr-ja/fr-ru/core-fr 现版均为 121 且 key150 不变。**共享门禁工具已改动，须报协调员知悉**（改动窄、回归已验；他家后续跑 p8 只会在 `—`+CJK 段少误报）。
- r2 已起（后台，含 8 处核心修复 + 修复后 p8.py）。

### fr-ko r2（~11:2x–11:3x UTC）：全绿，fr-ko 完成
- run.py TOTAL 150，0 FLOW OVERFLOW，**0 HEAD TOO WIDE**；render rc 0；webpdf rc 0。
- 印 PDF `La-Lucerna-VOL4-fr-ko.pdf` 20,086,049 B，SHA-256 `9aeba6cc400e…`；网 PDF `La-Lucerna-VOL4-fr-ko-web.pdf` 1,923,039 B，SHA-256 `98170fbd21ae…`；`.text.md` SHA-256 `f5474d61eead…`（47,323 B，未变——8 处均为字号修复，无文本改动）。
- 文字层逐字节一致（各 94,860 字符）；occlusion 0；p8 121/150 CLEAN（vs 核心 keydiff=[150]，vs 修前 keydiff=[]——Q150 已找回）；freeze baseline 8/8（p1 `84b79449`、p2 `ed0efa63`、p3 `97989738`、p4 `87d7745e`、p5 `f9e6dee0`、p6 `a625b622`、p7 `82f17174`、p8 `788f7c60`）；freeze diff vs 核心 added CJK 2560、vs 修前基线 added CJK **1**（1 个 U+3000 回流分隔符，可接受）；boxtitle 0 DEFECT（47 titles，546 body lines）；creambox PASS 0 defects（n=493，中位 1.014、粗体 1.053、常规 0.999；P8 189→189 行、余量 45.7→45.7px）；spill 0；edge 0；census PASS（0/0/0）；`census_quotes.py` 弯引号缺陷 0；PDF 8 页、内嵌图 6 枚。
- P8 最小字号 11.625pt（881 spans，554 at min）；流终值 P6-deep 1258/1300、P6-ex 2402/2560、P7-phrases 1718/1830、P8-keys 2086/2560（Hiroshige 阈值 2170，余量 84）。
- ko freeze 例外**未触发**：venv 下 freeze baseline 8/8 + diff 正常，未用系统 python3。
- KIT 同步完成（`## Files delivered` 新印/网 SHA + D5 r2 freeze 哈希 + P8 字号，新增 `## D5 rebuild (2026-11-12)` 一节，含 p8.py 工具修复与 Q150 根因）。
- 三项验收：生产印/网/text SHA = r2 日志 `shas.txt` = KIT；生产 `svglib.py` 含 `_D5_READER = "cjk"`（第 100 行）。PASS。
- 清理：`freeze-r1/r2` build-copy 已删；`freeze-r*.json`、基线与日志保留。
- fr-ko 状态：**D5 完成，全部门禁通过，KIT 已同步。**

### fr-zh-tw r1（进行中，~11:3x UTC 起）
- `run_gates.sh 2026-w47-fr-zh-tw zh-tw La-Lucerna-VOL4-fr-zh-tw.pdf La-Lucerna-VOL4-fr-zh-tw-web.pdf r1` 后台运行中。

### fr-zh-tw r1（~11:3x–11:5x UTC）：3 超宽头 + 3 框题（与 ko 同型，p8 干净）
- run.py TOTAL 150，0 FLOW OVERFLOW，**3 HEAD TOO WIDE**：P6-opinion 与 P7-B2 `IL EST PRÉVU QUE + SUBJONCTIF`、P6-micro `LE COMPARATIF EN POLITIQUE`（head_lire `LIRE LE CALENDRIER　行事曆` 未超——3 字 gloss 短；band `阿爾卡拉斯奪冠　參議院週三表決` 无 TEXTX）。
- occlusion 0；boxtitle/creambox 3 DEFECT（同款 3 法文框题 +7.6/+36.5/+24.5）；p8 121/150 CLEAN（vs 核心 keydiff=[150]，vs 修前 keydiff=[]——无 Q150 问题）；freeze 8/8（diff vs 核心 added CJK 970）；文字层逐字节一致（各 93,560 字符）；spill 0；edge 0；census PASS。
- 修复（r1→r2）：仅与核心相同的 8 处（head_lire、band_r1 均不动）。r2 已起。
### fr-zh-tw r2（~11:5x–12:0x UTC，重跑后）：全绿，fr-zh-tw 完成
- run.py TOTAL 150，0 FLOW OVERFLOW，**0 HEAD TOO WIDE**；render rc 0；webpdf rc 0。
- 印 PDF `La-Lucerna-VOL4-fr-zh-tw.pdf` 18,531,943 B，SHA-256 `de24f2a08c9b…`；网 PDF `La-Lucerna-VOL4-fr-zh-tw-web.pdf` 2,074,668 B，SHA-256 `f54db205afbd…`；`.text.md` SHA-256 `e5c8c1cd50f0…`（45,992 B，未变——8 处均为字号修复；与重建 #2 KIT 记录 45,998 B 差 6 B，mtime 2026-11-11 16:39 UTC，修前既有，繁体头已验）。
- 文字层逐字节一致（各 93,337 字符）；occlusion 0；p8 121/150 CLEAN（vs 核心 keydiff=[150]，vs 修前 keydiff=[]）；freeze baseline 8/8（p1 `4b48d178`、p2 `a078ab99`、p3 `5cbffbd7`、p4 `294acd2c`、p5 `eaaca5e8`、p6 `e4266b64`、p7 `76d84860`、p8 `a234e5e7`）；freeze diff vs 核心 added CJK 970、vs 修前基线 added CJK **0**；boxtitle 0 DEFECT（40 titles，380 body lines）；creambox PASS 0 defects（n=486，中位 1.017、粗体 1.049、常规 1.000；P8 188→188 行、余量 36.1→36.1px）；spill 0；edge 0；census PASS（0/0/0）；`census_quotes.py` 弯引号缺陷 0；PDF 8 页、内嵌图 6 枚。
- P8 最小字号 11.625pt（828 spans，532 at min）；流终值 P6-deep 1258/1300、P6-ex 2402/2560、P7-phrases 1718/1830、P8-keys 2026/2560（Hiroshige 阈值 2170，余量 144——全家最宽）。
- KIT 同步完成（`## Files delivered` 新印/网/text SHA + D5 r2 freeze 哈希 + P8 字号，新增 `## D5 rebuild (2026-11-12)` 一节，含 SC 字族注记与 r2 重跑记录）。
- 三项验收：生产印/网/text SHA = r2 日志 `shas.txt` = KIT；生产 `svglib.py` 含 `_D5_READER = "cjk"`（第 100 行）。PASS。
- 清理：`freeze-r1/r2` build-copy 已删；`freeze-r*.json`、基线与日志保留。磁盘 /home/hatch 93G/150G（57G 空闲，<100G 门限）。
- fr-zh-tw 状态：**D5 完成，全部门禁通过，KIT 已同步。**

## 全家收尾（2026-11-12 ~12:0x UTC）
- fr 家庭 11 版全部 D5 完成：core-fr（r2）、fr-en（r3）、fr-es（r2）、fr-de（r2）、fr-pt（r2）、fr-it（r3）、fr-nl（r2）、fr-ru（r1）、fr-ja（r2）、fr-ko（r2）、fr-zh-tw（r2）。每版均通过三项验收（生产 SHA = 门禁日志 = KIT；svglib 含 `_D5_READER`；KIT 已同步），无未完成项。
- 工具改动（须报协调员）：① `tools/p8.py` 的 `detect_note` 补了 ` —`+CJK 丢空格归一化（fr-ko Q150 根因），回归已验 5 版提取不变；② fr-ru creambox 3 误报已裁定（重排复本误判，工具需词覆盖匹配——未改工具，仅记录）。无 commit、无 push、无 lint --write。

### fr-zh-tw 已装（fr-ko r2 等待期间，mode=cjk）
- `apply_variant.py --target fr --reader zh-tw`，`assert_routing.py` cjk PASS（`_D5_READER='cjk'`）。修前 svglib md5 `f25bfcfc`，基线核验 BASELINE-FAITHFUL，moth 在位。修前 `.text.md` 副本已存（SHA `e5c8c1cd50f0`，繁体中文头已验）。
- 注意：装后 fr-zh-tw svglib 与 core-fr **字节一致**（diff 为空）——仍用 SC 字族/`_sc_index`，安装器未切 TC。按 CJK-DECISION 是按文字分流、mode=cjk；TC 字族属于 core-zh-tw 这个 target，fr-zh-tw 读者版修前即用 SC 字族（md5 与各 fan-out 相同），D5 未改字族 variant，属机制行为，不手动切 TC。门禁会验证渲染。
