# W46 法语目标家族 D5 重建报告

刊期 2026-11-09（周一）至 2026-11-15（周日）；VOL.3；W46 due 2026-11-16。重建 11 读者版（de/en/es/it/ja/ko/nl/pt/ru/zh-cn/zh-tw）+ core-fr。Builder 2026-11-15（UTC）。**本报告只记录 builder 工作；绝无 commit/push；production/ 由 closer 同步。**

## §0 方法

### §0.0 任务与纪律

- 本地仓库 `~/workspace/weekly-git`（LucernaRead/weekly clone）；工作目录 `hidden_files/d5-redo/scratch-2026-w46-fr/`（`baseline/`、`patched/`、`logs/`、`bin/`、`notes/`）。正典解释器 `tools/venv/bin/python`（Pillow 13.0.0）；开工前 `fc-cache -f` 已暖字体。磁盘门 ≥100G 未触（开工 73G/150G，晚间 74G/150G）。
- builder 只写 scratch 内 `patched/`；**绝不 commit、绝不 push、绝不跑 `lint --write`、不动 index.json、不写 production/**（D40）。绝不重跑 webpdf 覆盖 builder 网 PDF（网 PDF 字节非确定性；§9 以终轮实测为准；closer 拷 builder 原件）。

### §0.1 导出器结论（P3b）——原生导出器认对，ADOPT

- 任务书写的 `hidden_files/style-port-fr/textexp_fr.py` **不存在**；实测真导出器是 `hidden_files/w46/text-export/export.py`（stub-run，与 W47 export47.py 同血统；头取自 production 副本 `.text.md`、VOL 按 `production/volumes.json` 纠为 VOL.3）。
- 以已发版 text.md（`issues/` 内）为金标准：试跑 baseline fr-en / fr-zh-cn / fr-ru，RC=0，各 527 entries、150 题，与 `issues/` 已发版 **BYTE-IDENTICAL**。无 `verify_textexp_fr.py`；G15c 口径定为：export.py 重出 + `cmp` vs issues/（BYTE-IDENTICAL 即 ADOPT，0 UNEXPECTED）。`style-port-fr/textexp-fix/verify_textexp.py` 是 fanout 比对工具（含 SEP/VOL/CJK 等 intended-transform 类），不作 D5 门禁。
- 交付 text.md 取件口径：**取 `.text.md.new`（新鲜导出），绝不取同名 `.text.md`**。实测 de 版：patched 内旧 `.text.md` 45,812 B（2026-11-06，SHA `b45397cf…`）= production/ 同名旧 fanout 产物；`.text.md.new` 45,709 B（2026-11-15 run2，SHA `fe0a9922…`）= issues/ 已发版逐字节一致。core-fr 同款：production 旧件 45,506 B（SHA `91593976…`），`.new` 45,357 B（SHA `bc53a38c…`）。run2 12/12 `cmp` vs issues/ 全部 BYTE-IDENTICAL（§9）。

### §0.2 D1 必须做，任务书“D5-only”前提不成立

- 实测生产 svglib 含 D1 fix 0 处、Newsreader 7 处、`_D5_READER` 0 处；fanout svglib 含 D1 fix 1 处，与生产版 diff 恰为 D1 hunk 一处（26 行 `<>` 行）。按 PLAN §0.1，fr×3 属 pre-D1 新样式，D1 + D5 一次做（W45 fr 先例）。patched svglib = fanout D1 版（逐读者；zh-cn/core-fr 用 fanout en 版；生产 core-fr svglib 与生产 fr-zh-cn svglib 逐字节相同，patched 两者亦相同，已验）。

### §0.3 zh-tw 保持 SC 面，不改 TC

- 生产 fr-zh-tw svglib 与生产 fr-en svglib 逐字节相同（SC `_sc_index`、`Noto Sans CJK SC`）；fanout zh-tw 与 W45 fr-zh-tw 生产 svglib 同样是 SC 面。D5-METHOD §1.2 的“zh-tw 用 core-zh-tw 基底（TC 面）”与实盘不符；安装器亦未改写其下标（`install_cjk_variant` 只处理 ja/ko）。改 TC 会改变全部繁体字形/字宽、超出 D5 范围，故维持已发 SC 面；提请协调员/重校注意（§10）。ja：`CJK index SC -> JP` + kinsoku 块自当周 core-zh-tw 移植；ko：SC -> KR。

### §0.4 基线（12/12 CLEAN）

- 每版 run TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；G2 head_check 0 defects；G9 freeze 8/8；G11 0 SPILL；G12 0 DEFECT（27 titles）；G13 0 TOUCH 0 NEAR；G14 creambox PASS；G15a 印/网/已发三方字符多重集差 0 + text.md BYTE-IDENTICAL；G15c ADOPT；G16 0 defective；p8 extract **121/150** 全 12 版，compare CLEAN（keydiff `[150]` ×10 读者版，`[]` 为 zh-cn 与 core-fr 自比）。
- 修前普查 D5 lat/cyr：de 556/0、en 545/0、es 547/0、it 543/0、ja 417/0、ko 415/0、nl 555/0、pt 546/0、ru 437/319、zh-cn 417/0、zh-tw 411/0、core-fr 417/0；curly_in_cjk 0/0 全版。
- D18 基线间隙 px：de 122.6、en 144.4、es 128.4、it 112.8、ja 165.4、ko 248.6、nl 159.3、pt 136.4、ru 163.6、zh-cn 248.7、zh-tw 248.7、core 248.7。D37 基线余量 pt：de 67.0、en 120.2、es 42.5、it 111.8、ja 184.6、ko 210.0、nl 61.2、pt 38.0、ru 47.0、zh-cn 214.3、zh-tw 214.3、core 214.3。
- 基线印 PDF 字节：de 9,191,671、en 9,186,502、es 9,173,346、it 9,170,576、ja 21,442,781、ko 15,097,268、nl 9,174,011、pt 9,175,010、ru 9,232,415、zh-cn 21,354,923、zh-tw 21,420,041、core 21,354,923；issues pin（pdfBytes/pdfSha256）与 issues/ PDF 文件核对 12/12 一致。基线印 PDF SHA 见 §9 对照列。
- 残留记录（非缺陷）：de 基线 G12 1 OBSERVE（P1 BODY over +2.5px，与 backup 同值，先存）；自建网 PDF 比 issues 版大约 37KB（webpdf 字体子集化 artifact，W45 fr 同款，文字层差 0）。

### §0.5 装机

- `tools/mechanism-w47/apply_variant.py --target fr --reader <r> --week 2026-w46`（先 `--check` 干跑），日志 `logs/install.log`；`test_d5_routing.py` **FAILURES: 0**；fix2 保留（`_QUOTE_CLS`=4、`fix2`=5，全 12 文件）；fix-xru=0（D26，W47-only 未引入）；ru 用旧 `_D5_READER == "ru"` 分支。
- `_D5_READER` 实际行号是 **svglib.py:100**（任务书写的 :107 是 W47 版行号；本家文件 L100）。值：latin ×6（de/en/es/it/nl/pt）、ru ×1（ru）、cjk ×4（ja/ko/zh-cn/zh-tw；core-fr 按 zh-cn 装为 cjk）。
- 每版补 W47 版 `run.py`（`production/2026-w47/core-fr/run.py`，md5 `183d86d469b8480da4a9721f7b241036`，D14）+ fanout 版 `render.py`（`style-port-fr/fanout-w46/<reader>/render.py`，仅改印 PDF 名 1 行；zh-cn/core-fr 用 en 版改名 `The-Lucerna-VOL3-fr-zh-cn.pdf` / `The-Lucerna-VOL3-fr.pdf`）；3 张故事 JPG（atget-paris / chrysanthemum-blanco / hiroshige-maple）自 fanout assets 拷入 scratch 复印件（D20，绝不进 production；生产 assets 本无 JPG，只有 CREDITS + moth）。

### §0.6 门禁口径（19 verdict/版）

- G1–G14 + G15a/G15c + G16 + D18 + D37 = 19。**G15b 仅记录（D27 类）**：共享 `tools/verify_textmd.py` 未标定 fr 格式——基线 11 版 rc=1 CARRYOVER FAIL、pt 版 rc=2（无 pt 读者表）。验收以 G15a（印/网文字层多重集差 0）+ G15c（原生导出器 ADOPT）为准；run2 各版残留词见 §1–§6。
- D18 = 刊头标语行间隙（内容识别，绝不硬编码 y）；D37 = 徽章行余量（内容识别实际行，绝不硬编码 y=612，D39(5)）。D18 y=92、徽章 y=612、副标题 y=372（通栏设计，无门禁）。
- G6 斜体旗标先量测再定性（D41）：本家 run1/run2 全部 G6 旗标均为正体 TEXTX（预告带/ strip 标题越界），无斜体误报项。

### §0.7 几何常量（SVG 实测）

- **RIGHT=1862，不是 1885**：`bslib4.py:13` 的注释写 1885 是 stale；实算 `88 + 4×422.5 + 3×28 = 1862`，SVG 页脚线 `x2=1862.0` 与 band_r1 末端 1832.0（= RIGHT−30）证实。MX=88、CW=422.5、GUT=28、COLX=[88, 538.5, 989, 1439.5]、页脚线 y=2596、页底 2700。头预算 CW=422.5（须 ≤420.5）；p.text 盒标题预算 400.5（须 ≤398.5）；f.box 标题预算 404.5（须 ≤402.5）；D37 以 COLX[3]=1439.5 为界。
- 两个归因纠正（SVG 实测，2026-11-15）：de P1 缺陷 `9. bis 15. November` 不是 f.box 标题，而是 `content12.py:71` 的 `p.text(gx + 22, gy + 106, E["agenda_sub"], 19, "sans", False, GREY)`——19pt 常规体；19pt 探针 407.0px，修复 19→18（385.6px）。`content12.py:46` 的 f.box 标题实为 `E["dates_box_title"]` = `LES DATES　DREI TERMINE`（23pt，y=1483.08，未越框，无需修）。zh-tw 的 `head_mots_fetes` = `LES MOTS DU SOUVENIR`（无读者词）、`head_cine` = `LE CINÉMA DU MERCREDI　電影`（仅 2 字），故 P3/P5 盒标题未越框、无需修；zh-cn 对应串为 `…纪念词表` / `…周三电影`，越框须修。
- f.box 标题无字号字面：三处缺陷 f.box 调用（COMMENTATEUR、TROIS DATES，及 de 的 dates 盒——后者无需修）用默认 `tsize=23`，调用内无字面；修复是在收尾行 `])` 后加 `, tsize=21`（`bin/apply_tsize.py`，沿用 apply_fix.py 的精确旧行 + 行号双重校验 + 唯一性 + `py_compile` 纪律）。

### §0.8 事故

- **measure_fr.py D18 量测 bug（2026-11-15 已修）**：run1 的 D18 量测是错的——它只取含 `HEBDOMADAIRE` 的 run 作为标语行末；D5 后标语行被拆成多个 run（拉丁进 Newsreader、CJK 留 CJK 面），只量到第一段，致 run1 D18 间隙虚高（490–660px；基线 112–248px）。修复：以文档顺序取标语行——VOL. 末 run 与首个 `SEMAINE DU` run 之间、同 y=92 的全部 run 为标语行；日期取同 y 自首个日期 run 起的全部 run。D37 不受影响。重测日志 `logs/measure-fixed-baseline-run1.log`：基线值与旧量测完全相同（122.6–248.7px），run1 修正值 de 38.5、en 58.3、es 43.3、it 24.2、ja 109.0、ko 193.1、nl 77.0、pt 52.7、ru 140.0、zh-cn/zh-tw/core 192.4px，全 PASS。run2 门禁用修后脚本；**本报告凡引 run1 D18 一律用修正值，旧 run1 D18 行已作废**。
- **derive_margins.py 两个量测 bug（2026-11-15 已修，余量表重算）**：(1) 字面串经 `.encode().decode("unicode_escape")` 会把 UTF-8 重音字母（É 等） mangling 成双字符，致 `IL EST PRÉVU…` 23pt 探针 411.0→427.0px、预告带间隙算出负值；已去掉该往返，改直接用 JSON 解出的 Unicode 串。(2) strip 对侧串提取：无修复的副标行被当成空串，致 en 间隙 723.9px；已改为始终从文件读两行并按行解析 bold。另 f.box 标题预算由 402.5 纠为 404.5（COMMENTATEUR 402.5px 余量恰 2.0px 是对 404.5 而言）。重算后 131 行余量无一 < 2.0px，与 run1 探针日志（`logs/probes-run1.txt`）逐项对得上。
- run2 构建首批三批曾因 `build-one.sh` 无执行位全部 rc=126 Permission denied，改 `bash bin/build-one.sh` + `chmod +x bin/*` 后重跑成功（12/12 BUILD-OK，2026-11-15 约 20:20–20:25 UTC，每版约 85 秒）。

### §0.9 KIT custody

- KIT 正本在 production（W45 fr 先例）；实测 production KIT 与 patched KIT 对 de 版 `diff` rc=0（装机时同步）。builder 只在 `patched/<slug>/WEEKLY-KIT.md` 更新，closer 按 §8 同步。**绝不以 patched KIT 覆盖 production KIT 的反向操作**（W45 fr 警告过此同步陷阱）。

## §1 de / en

### 2026-w46-fr-de（读者 de，`_D5_READER = "latin"`）

- 修前普查：D5 Latin in CJK / Cyrillic in CJK = 556/0；curly_in_cjk 0/0。
- 基线：TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；G15a 多重集差 0、text.md BYTE-IDENTICAL；印 PDF 9,191,671 B。
- run1 **14/19**：G1/G2 HDW 9、G6 2、G12 6 DEFECT、G14 9 DEFECT；D18 38.5px、D37 32.0pt。G6 2 处：P1 预告带标题 vs `SENAT ÜBERNIMMT`（97.8×25.2px）；P7 strip 标题 vs 副标（134.9×18.2px）。G12 6 处：P1 BODY `9. bis 15. November` +6.7、P4 `WÖRTER` +5.3、P4 `FORTSETZUNG FOLGT` +19.7、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P6 `HAUSHALTSKALENDER (NOCH KEIN ERGEBNIS)` +7.7、P6 `TROIS DATES POUR COMPRENDRE` +24.5。
- run2 **19/19**：G1 TOTAL 150、OVF 0、HDW 0；G3 lat/cyr/curly-in-CJK 0；G5 网 PDF 1,209,895 B（< 7 MB）；G6 0 flags；G7 p8 extract 121/150；G8 CLEAN；G9 8/8；G10 新增 CJK 0、新增 Latin 345（run 拆分预期）；G11 0 SPILL、111 OBSERVE；G12 0 DEFECT；G13 0 TOUCH 0 NEAR；G14 P8 行数 197→201、余量 36.6→40.9px；G15a 多重集差 0、text.md BYTE-IDENTICAL；G15c ADOPT；G16 0 defective；D18 38.5px、D37 32.0pt。G15b 仅记录：2× `kurzübungen` / `sport`。

修复（22 处，全为字号缩小，零文案改动）：

| 位置 | 旧→新 | 缺陷 | 探针宽 / 预算 | 余量 |
|---|---|---|---|---|
| `content12.py:27` | 46→44pt | P1 band title G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 17.9px |
| `content12.py:29` | 27→24pt | P1 band_r1 G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 17.9px |
| `content12.py:71` | 19→18pt | P1 agenda_sub creambox +6.7 | 385.6px / 400.5px | 14.9px |
| `content12.py:124` | 25→24pt | P1-budget head HDW | 406.4px / 422.5px | 16.1px |
| `content34.py:76` | 23→20pt | P3 mots_fetes creambox +42.8 | 385.1px / 400.5px | 15.4px |
| `content34.py:84` | 23→22pt | P3 zoom creambox +7.6 | 390.7px / 400.5px | 9.8px |
| `content34.py:161` | 加 `tsize=21`（默认 23→21） | P4 COMMENTATEUR f.box tsize 23->21 | 402.5px / 404.5px | 2.0px |
| `content34.py:171` | 23→22pt | P4 mots_tennis creambox +5.3 | 387.8px / 400.5px | 12.8px |
| `content34.py:179` | 23→21pt | P4 asuivre creambox +19.7 | 383.2px / 400.5px | 17.3px |
| `content34.py:182` | 24→23pt | P4-micro head HDW | 408.4px / 422.5px | 14.1px |
| `content56.py:80` | 23→21pt | P5 cine creambox +33.3/+31.3 | 396.0px / 400.5px | 4.5px |
| `content56.py:110` | 24→23pt | P6 chart creambox +7.7 | 822.7px / 851.0px | 28.3px |
| `content56.py:127` | 25→22pt | P6-ex head HDW | 413.7px / 422.5px | 8.8px |
| `content56.py:159` | 25→23pt | P6-opinion head HDW | 411.0px / 422.5px | 11.5px |
| `content56.py:165` | 25→24pt | P6-micro head HDW | 410.1px / 422.5px | 12.4px |
| `content56.py:173` | 25→23pt | P6-micro MICRO head HDW | 408.4px / 422.5px | 14.1px |
| `content56.py:189` | 加 `tsize=21`（默认 23→21） | P6 3dates f.box tsize 23->21 | 391.7px / 404.5px | 12.8px |
| `content7.py:38` | 24→23pt | P7-B2 head HDW | 411.0px / 422.5px | 11.5px |
| `content7.py:48` | 27→26pt | P7-outils head HDW | 420.0px / 422.5px | 2.5px |
| `content7.py:59` | 27→24pt | P7 strip title G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 36.0px |
| `content7.py:60` | 20→19pt | P7 strip sub G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 36.0px |
| `content7.py:89` | 25→22pt | P7-clinic head HDW | 410.0px / 422.5px | 12.5px |

### 2026-w46-fr-en（读者 en，`_D5_READER = "latin"`）

- 修前普查：D5 Latin in CJK / Cyrillic in CJK = 545/0；curly_in_cjk 0/0。
- 基线：TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；G15a 多重集差 0、text.md BYTE-IDENTICAL；印 PDF 9,186,502 B。
- run1 **14/19**：G1/G2 HDW 6、G6 3、G12 3 DEFECT、G14 6 DEFECT；D18 58.3px、D37 117.9pt。G6 3 处：P1 预告带标题 vs `SENATE TAKES OVER`（103.3×20.8px）；P6 `TIMETABLE` vs `B1`（12.6×13.2px）；P7 strip 标题 vs 副标（86.3×18.2px）。G12 3 处：P1 `IN THIS ISSUE` +45.9、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P6 `TROIS DATES POUR COMPRENDRE` +24.5。
- run2 **19/19**：G1 TOTAL 150、OVF 0、HDW 0；G3 lat/cyr/curly-in-CJK 0；G5 网 PDF 1,206,200 B（< 7 MB）；G6 0 flags；G7 p8 extract 121/150；G8 CLEAN；G9 8/8；G10 新增 CJK 0、新增 Latin 354（run 拆分预期）；G11 0 SPILL、112 OBSERVE；G12 0 DEFECT；G13 0 TOUCH 0 NEAR；G14 P8 行数 197→195、余量 32.7→31.7px；G15a 多重集差 0、text.md BYTE-IDENTICAL；G15c ADOPT；G16 0 defective；D18 58.3px、D37 117.9pt。G15b 仅记录：2× `of` / `9`。

修复（15 处，全为字号缩小，零文案改动）：

| 位置 | 旧→新 | 缺陷 | 探针宽 / 预算 | 余量 |
|---|---|---|---|---|
| `content12.py:27` | 46→44pt | P1 band title G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 12.9px |
| `content12.py:29` | 27→24pt | P1 band_r1 G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 12.9px |
| `content12.py:92` | 24→21pt | P1 sommaire creambox +45.9 | 390.2px / 400.5px | 10.2px |
| `content12.py:124` | 25→24pt | P1-budget head HDW | 406.4px / 422.5px | 16.1px |
| `content34.py:76` | 23→21pt | P3 mots_fetes creambox +24.8/+22.8 | 388.5px / 400.5px | 12.0px |
| `content34.py:84` | 23→22pt | P3 zoom creambox +7.6 | 390.7px / 400.5px | 9.8px |
| `content34.py:161` | 加 `tsize=21`（默认 23→21） | P4 COMMENTATEUR f.box tsize 23->21 | 402.5px / 404.5px | 2.0px |
| `content56.py:80` | 23→21pt | P5 cine creambox +33.3/+31.3 | 394.1px / 400.5px | 6.4px |
| `content56.py:127` | 25→21pt | P6-ex head HDW + TIMETABLE/B1 TEXTX | 403.4px / 422.5px | 19.1px |
| `content56.py:159` | 25→23pt | P6-opinion head HDW | 411.0px / 422.5px | 11.5px |
| `content56.py:165` | 25→24pt | P6-micro head HDW | 410.1px / 422.5px | 12.4px |
| `content56.py:189` | 加 `tsize=21`（默认 23→21） | P6 3dates f.box tsize 23->21 | 391.7px / 404.5px | 12.8px |
| `content7.py:38` | 24→23pt | P7-B2 head HDW | 411.0px / 422.5px | 11.5px |
| `content7.py:59` | 27→24pt | P7 strip title G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 44.9px |
| `content7.py:89` | 25→22pt | P7-clinic head HDW | 409.9px / 422.5px | 12.6px |

## §2 es / it

### 2026-w46-fr-es（读者 es，`_D5_READER = "latin"`）

- 修前普查：D5 Latin in CJK / Cyrillic in CJK = 547/0；curly_in_cjk 0/0。
- 基线：TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；G15a 多重集差 0、text.md BYTE-IDENTICAL；印 PDF 9,173,346 B。
- run1 **14/19**：G1/G2 HDW 5、G6 1、G12 4 DEFECT、G14 6 DEFECT；D18 43.3px、D37 4.9pt。G6 1 处：P1 预告带标题 vs `EL SENADO TOMA EL RELEVO`（125.5×20.8px）。G12 4 处：P4 `PALABRAS` +27.3、P5 `PALABRAS` +6.7、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P6 `TROIS DATES POUR COMPRENDRE` +24.5。
- run2 **19/19**：G1 TOTAL 150、OVF 0、HDW 0；G3 lat/cyr/curly-in-CJK 0；G5 网 PDF 1,206,561 B（< 7 MB）；G6 0 flags；G7 p8 extract 121/150；G8 CLEAN；G9 8/8；G10 新增 CJK 0、新增 Latin 351（run 拆分预期）；G11 0 SPILL、112 OBSERVE；G12 0 DEFECT；G13 0 TOUCH 0 NEAR；G14 P8 行数 194→200、余量 36.6→40.9px；G15a 多重集差 0、text.md BYTE-IDENTICAL；G15c ADOPT；G16 0 defective；D18 43.3px、D37 4.9pt。G15b 仅记录：3× `los` / `fechas`。

修复（13 处，全为字号缩小，零文案改动）：

| 位置 | 旧→新 | 缺陷 | 探针宽 / 预算 | 余量 |
|---|---|---|---|---|
| `content12.py:27` | 46→44pt | P1 band title G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 14.4px |
| `content12.py:29` | 27→23pt | P1 band_r1 G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 14.4px |
| `content12.py:124` | 25→24pt | P1-budget head HDW | 406.4px / 422.5px | 16.1px |
| `content34.py:84` | 23→22pt | P3 zoom creambox +7.6 | 390.7px / 400.5px | 9.8px |
| `content34.py:161` | 加 `tsize=21`（默认 23→21） | P4 COMMENTATEUR f.box tsize 23->21 | 402.5px / 404.5px | 2.0px |
| `content34.py:171` | 23→21pt | P4 mots_tennis creambox +27.3 | 391.0px / 400.5px | 9.5px |
| `content56.py:72` | 23→22pt | P5 mots_photo creambox +6.7 | 389.9px / 400.5px | 10.6px |
| `content56.py:80` | 23→22pt | P5 cine creambox +14.3 | 396.1px / 400.5px | 4.4px |
| `content56.py:127` | 25→23pt | P6-ex head HDW | 411.2px / 422.5px | 11.3px |
| `content56.py:159` | 25→23pt | P6-opinion head HDW | 411.0px / 422.5px | 11.5px |
| `content56.py:165` | 25→24pt | P6-micro head HDW | 410.1px / 422.5px | 12.4px |
| `content56.py:189` | 加 `tsize=21`（默认 23→21） | P6 3dates f.box tsize 23->21 | 391.7px / 404.5px | 12.8px |
| `content7.py:38` | 24→23pt | P7-B2 head HDW | 411.0px / 422.5px | 11.5px |

### 2026-w46-fr-it（读者 it，`_D5_READER = "latin"`）

- 修前普查：D5 Latin in CJK / Cyrillic in CJK = 543/0；curly_in_cjk 0/0。
- 基线：TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；G15a 多重集差 0、text.md BYTE-IDENTICAL；印 PDF 9,170,576 B。
- run1 **14/19**：G1/G2 HDW 5、G6 1、G12 3 DEFECT、G14 5 DEFECT；D18 24.2px、D37 80.7pt。G6 1 处：P1 预告带标题 vs `IL SENATO PRENDE IL RELEVO`（134.8×20.8px）。G12 3 处：P1 `SOMMARIO` +16.9、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P6 `TROIS DATES POUR COMPRENDRE` +24.5。
- run2 **19/19**：G1 TOTAL 150、OVF 0、HDW 0；G3 lat/cyr/curly-in-CJK 0；G5 网 PDF 1,202,591 B（< 7 MB）；G6 0 flags；G7 p8 extract 121/150；G8 CLEAN；G9 8/8；G10 新增 CJK 0、新增 Latin 328（run 拆分预期）；G11 0 SPILL、112 OBSERVE；G12 0 DEFECT；G13 0 TOUCH 0 NEAR；G14 P8 行数 193→194、余量 39.9→32.7px；G15a 多重集差 0、text.md BYTE-IDENTICAL；G15c ADOPT；G16 0 defective；D18 24.2px、D37 80.7pt。G15b 仅记录：2× `2026` / `3`。

修复（12 处，全为字号缩小，零文案改动）：

| 位置 | 旧→新 | 缺陷 | 探针宽 / 预算 | 余量 |
|---|---|---|---|---|
| `content12.py:27` | 46→44pt | P1 band title G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 6.4px |
| `content12.py:29` | 27→23pt | P1 band_r1 G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 6.4px |
| `content12.py:92` | 24→22pt | P1 sommaire creambox +16.9 | 383.0px / 400.5px | 17.5px |
| `content12.py:124` | 25→24pt | P1-budget head HDW | 406.4px / 422.5px | 16.1px |
| `content34.py:84` | 23→22pt | P3 zoom creambox +7.6 | 390.7px / 400.5px | 9.8px |
| `content34.py:161` | 加 `tsize=21`（默认 23→21） | P4 COMMENTATEUR f.box tsize 23->21 | 402.5px / 404.5px | 2.0px |
| `content56.py:80` | 23→20pt | P5 cine creambox +57.3/+43.3 | 397.9px / 400.5px | 2.6px |
| `content56.py:127` | 25→24pt | P6-ex head HDW | 408.2px / 422.5px | 14.3px |
| `content56.py:159` | 25→23pt | P6-opinion head HDW | 411.0px / 422.5px | 11.5px |
| `content56.py:165` | 25→24pt | P6-micro head HDW | 410.1px / 422.5px | 12.4px |
| `content56.py:189` | 加 `tsize=21`（默认 23→21） | P6 3dates f.box tsize 23->21 | 391.7px / 404.5px | 12.8px |
| `content7.py:38` | 24→23pt | P7-B2 head HDW | 411.0px / 422.5px | 11.5px |

## §3 ja / ko

### 2026-w46-fr-ja（读者 ja，`_D5_READER = "cjk"`）

- 修前普查：D5 Latin in CJK / Cyrillic in CJK = 417/0；curly_in_cjk 0/0。
- 基线：TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；G15a 多重集差 0、text.md BYTE-IDENTICAL；印 PDF 21,442,781 B。
- run1 **15/19**：G1/G2 HDW 5、G6 0、G12 2 DEFECT、G14 5 DEFECT；D18 109.0px、D37 185.6pt。G6 0。G12 2 处：P4 `LES PHRASES DU COMMENTATEUR` +36.5、P6 `TROIS DATES POUR COMPRENDRE` +24.5。G14 5 处含 P5 2 条 SPILL（D41 误报，见 D41 节）。
- run2 **18/19（G14 2 处 artifact，见 D41 节）**：G1 TOTAL 150、OVF 0、HDW 0；G3 lat/cyr/curly-in-CJK 0；G5 网 PDF 1,596,068 B（< 7 MB）；G6 0 flags；G7 p8 extract 121/150；G8 CLEAN；G9 8/8；G10 新增 CJK 0、新增 Latin 364（run 拆分预期）；G11 0 SPILL、118 OBSERVE；G12 0 DEFECT；G13 0 TOUCH 0 NEAR；G14 P8 行数 184→191、余量 33.7→33.7px；G15a 多重集差 0、text.md BYTE-IDENTICAL；G15c ADOPT；G16 0 defective；D18 109.0px、D37 185.6pt。G15b 仅记录：3× `点` / `ル`。

修复（8 处，全为字号缩小，零文案改动）：

| 位置 | 旧→新 | 缺陷 | 探针宽 / 预算 | 余量 |
|---|---|---|---|---|
| `content12.py:124` | 25→24pt | P1-budget head HDW | 406.4px / 422.5px | 16.1px |
| `content34.py:84` | 23→22pt | P3 zoom creambox +7.6 | 390.7px / 400.5px | 9.8px |
| `content34.py:161` | 加 `tsize=21`（默认 23→21） | P4 COMMENTATEUR f.box tsize 23->21 | 402.5px / 404.5px | 2.0px |
| `content56.py:127` | 25→23pt | P6-ex head HDW | 406.2px / 422.5px | 16.3px |
| `content56.py:159` | 25→23pt | P6-opinion head HDW | 411.0px / 422.5px | 11.5px |
| `content56.py:165` | 25→24pt | P6-micro head HDW | 410.1px / 422.5px | 12.4px |
| `content56.py:189` | 加 `tsize=21`（默认 23→21） | P6 3dates f.box tsize 23->21 | 391.7px / 404.5px | 12.8px |
| `content7.py:38` | 24→23pt | P7-B2 head HDW | 411.0px / 422.5px | 11.5px |

### 2026-w46-fr-ko（读者 ko，`_D5_READER = "cjk"`）

- 修前普查：D5 Latin in CJK / Cyrillic in CJK = 415/0；curly_in_cjk 0/0。
- 基线：TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；G15a 多重集差 0、text.md BYTE-IDENTICAL；印 PDF 15,097,268 B。
- run1 **15/19**：G1/G2 HDW 4、G6 0、G12 2 DEFECT、G14 3 DEFECT；D18 193.1px、D37 226.0pt。G6 0。G12 2 处：P4 `LES PHRASES DU COMMENTATEUR` +36.5、P6 `TROIS DATES POUR COMPRENDRE` +24.5。
- run2 **19/19**：G1 TOTAL 150、OVF 0、HDW 0；G3 lat/cyr/curly-in-CJK 0；G5 网 PDF 1,529,620 B（< 7 MB）；G6 0 flags；G7 p8 extract 121/150；G8 CLEAN；G9 8/8；G10 新增 CJK 0、新增 Latin 348（run 拆分预期）；G11 0 SPILL、149 OBSERVE；G12 0 DEFECT；G13 0 TOUCH 0 NEAR；G14 P8 行数 184→193、余量 33.7→33.1px；G15a 多重集差 0、text.md BYTE-IDENTICAL；G15c ADOPT；G16 0 defective；D18 193.1px、D37 226.0pt。G15b 仅记录：4× `론` / `당`。

修复（7 处，全为字号缩小，零文案改动）：

| 位置 | 旧→新 | 缺陷 | 探针宽 / 预算 | 余量 |
|---|---|---|---|---|
| `content12.py:124` | 25→24pt | P1-budget head HDW | 406.4px / 422.5px | 16.1px |
| `content34.py:84` | 23→22pt | P3 zoom creambox +7.6 | 390.7px / 400.5px | 9.8px |
| `content34.py:161` | 加 `tsize=21`（默认 23→21） | P4 COMMENTATEUR f.box tsize 23->21 | 402.5px / 404.5px | 2.0px |
| `content56.py:159` | 25→23pt | P6-opinion head HDW | 411.0px / 422.5px | 11.5px |
| `content56.py:165` | 25→24pt | P6-micro head HDW | 410.1px / 422.5px | 12.4px |
| `content56.py:189` | 加 `tsize=21`（默认 23→21） | P6 3dates f.box tsize 23->21 | 391.7px / 404.5px | 12.8px |
| `content7.py:38` | 24→23pt | P7-B2 head HDW | 411.0px / 422.5px | 11.5px |

## §4 nl / pt

### 2026-w46-fr-nl（读者 nl，`_D5_READER = "latin"`）

- 修前普查：D5 Latin in CJK / Cyrillic in CJK = 555/0；curly_in_cjk 0/0。
- 基线：TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；G15a 多重集差 0、text.md BYTE-IDENTICAL；印 PDF 9,174,011 B。
- run1 **14/19**：G1/G2 HDW 5、G6 1、G12 4 DEFECT、G14 5 DEFECT；D18 77.0px、D37 23.5pt。G6 1 处：P1 预告带标题 vs `DE SENAAT NEEMT HET OVER`（130.8×20.8px）。G12 4 处：P4 `WOORDEN` +27.3、P5 `WOORDEN` +6.7、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P6 `TROIS DATES POUR COMPRENDRE` +24.5。
- run2 **19/19**：G1 TOTAL 150、OVF 0、HDW 0；G3 lat/cyr/curly-in-CJK 0；G5 网 PDF 1,205,454 B（< 7 MB）；G6 0 flags；G7 p8 extract 121/150；G8 CLEAN；G9 8/8；G10 新增 CJK 0、新增 Latin 340（run 拆分预期）；G11 0 SPILL、109 OBSERVE；G12 0 DEFECT；G13 0 TOUCH 0 NEAR；G14 P8 行数 195→202、余量 38.5→36.6px；G15a 多重集差 0、text.md BYTE-IDENTICAL；G15c ADOPT；G16 0 defective；D18 77.0px、D37 23.5pt。G15b 仅记录：2× `3` / `au`。

修复（12 处，全为字号缩小，零文案改动）：

| 位置 | 旧→新 | 缺陷 | 探针宽 / 预算 | 余量 |
|---|---|---|---|---|
| `content12.py:27` | 46→44pt | P1 band title G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 9.9px |
| `content12.py:29` | 27→23pt | P1 band_r1 G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 9.9px |
| `content12.py:124` | 25→24pt | P1-budget head HDW | 406.4px / 422.5px | 16.1px |
| `content34.py:84` | 23→22pt | P3 zoom creambox +7.6 | 390.7px / 400.5px | 9.8px |
| `content34.py:161` | 加 `tsize=21`（默认 23→21） | P4 COMMENTATEUR f.box tsize 23->21 | 402.5px / 404.5px | 2.0px |
| `content34.py:171` | 23→21pt | P4 mots_tennis creambox +27.3 | 390.6px / 400.5px | 9.9px |
| `content56.py:72` | 23→22pt | P5 mots_photo creambox +6.7 | 389.5px / 400.5px | 11.0px |
| `content56.py:127` | 25→24pt | P6-ex head HDW | 417.3px / 422.5px | 5.2px |
| `content56.py:159` | 25→23pt | P6-opinion head HDW | 411.0px / 422.5px | 11.5px |
| `content56.py:165` | 25→24pt | P6-micro head HDW | 410.1px / 422.5px | 12.4px |
| `content56.py:189` | 加 `tsize=21`（默认 23→21） | P6 3dates f.box tsize 23->21 | 391.7px / 404.5px | 12.8px |
| `content7.py:38` | 24→23pt | P7-B2 head HDW | 411.0px / 422.5px | 11.5px |

### 2026-w46-fr-pt（读者 pt，`_D5_READER = "latin"`）

- 修前普查：D5 Latin in CJK / Cyrillic in CJK = 546/0；curly_in_cjk 0/0。
- 基线：TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；G15a 多重集差 0、text.md BYTE-IDENTICAL；印 PDF 9,175,010 B。
- run1 **13/19**：G1/G2 HDW 6、G6 1、G12 4 DEFECT、G14 6 DEFECT；D18 52.7px、D37 -0.6pt（run1 FAIL）。G6 1 处：P1 预告带标题 vs `SENADO ASSUME REVEZAMENTO`（187.3×20.8px）。G12 4 处：P4 `PALAVRAS` +27.3、P5 `PALAVRAS` +6.7、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P6 `TROIS DATES POUR COMPRENDRE` +24.5。D37 唯一 FAIL：徽章余量 −0.6pt。
- run2 **19/19**：G1 TOTAL 150、OVF 0、HDW 0；G3 lat/cyr/curly-in-CJK 0；G5 网 PDF 1,207,119 B（< 7 MB）；G6 0 flags；G7 p8 extract 121/150；G8 CLEAN；G9 8/8；G10 新增 CJK 0、新增 Latin 342（run 拆分预期）；G11 0 SPILL、111 OBSERVE；G12 0 DEFECT；G13 0 TOUCH 0 NEAR；G14 P8 行数 198→201、余量 32.6→31.7px；G15a 多重集差 0、text.md BYTE-IDENTICAL；G15c ADOPT；G16 0 defective；D18 52.7px、D37 21.2pt。G15b 仅记录：rc=2（无 pt 读者表）。

修复（15 处，全为字号缩小，零文案改动）：

| 位置 | 旧→新 | 缺陷 | 探针宽 / 预算 | 余量 |
|---|---|---|---|---|
| `content12.py:27` | 46→44pt | P1 band title G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 8.8px |
| `content12.py:29` | 27→21pt | P1 band_r1 G6 TEXTX（与对侧合计间隙） | — | 与对侧合计间隙 8.8px |
| `content12.py:32` | 16→15pt | D37 badge -0.6pt（D37 徽章余量，pt） | — | D37 徽章余量 21.2pt |
| `content12.py:124` | 25→24pt | P1-budget head HDW | 406.4px / 422.5px | 16.1px |
| `content34.py:84` | 23→22pt | P3 zoom creambox +7.6 | 390.7px / 400.5px | 9.8px |
| `content34.py:161` | 加 `tsize=21`（默认 23→21） | P4 COMMENTATEUR f.box tsize 23->21 | 402.5px / 404.5px | 2.0px |
| `content34.py:171` | 23→21pt | P4 mots_tennis creambox +27.3 | 390.2px / 400.5px | 10.3px |
| `content56.py:72` | 23→22pt | P5 mots_photo creambox +6.7 | 389.1px / 400.5px | 11.4px |
| `content56.py:80` | 23→20pt | P5 cine creambox +57.3/+43.3 | 397.9px / 400.5px | 2.6px |
| `content56.py:127` | 25→23pt | P6-ex head HDW | 411.2px / 422.5px | 11.3px |
| `content56.py:159` | 25→23pt | P6-opinion head HDW | 411.0px / 422.5px | 11.5px |
| `content56.py:165` | 25→24pt | P6-micro head HDW | 410.1px / 422.5px | 12.4px |
| `content56.py:189` | 加 `tsize=21`（默认 23→21） | P6 3dates f.box tsize 23->21 | 391.7px / 404.5px | 12.8px |
| `content7.py:38` | 24→23pt | P7-B2 head HDW | 411.0px / 422.5px | 11.5px |
| `content7.py:48` | 27→25pt | P7-outils head HDW | 410.6px / 422.5px | 11.9px |

## §5 ru / zh-cn / zh-tw

### 2026-w46-fr-ru（读者 ru，`_D5_READER = "ru"`）

- 修前普查：D5 Latin in CJK / Cyrillic in CJK = 437/319；curly_in_cjk 0/0。
- 基线：TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；G15a 多重集差 0、text.md BYTE-IDENTICAL；印 PDF 9,232,415 B。
- run1 **19/19**：G1/G2 HDW 0、G6 0、G12 0 DEFECT、G14 0 DEFECT；D18 140.0px、D37 40.7pt。run1 即 19/19 全绿，零修复。G3 census 证实 ru 路由触发：Noto Sans 元素 815。
- run2 **19/19**：G1 TOTAL 150、OVF 0、HDW 0；G3 lat/cyr/curly-in-CJK 0；G5 网 PDF 1,462,831 B（< 7 MB）；G6 0 flags；G7 p8 extract 121/150；G8 CLEAN；G9 8/8；G10 新增 CJK 0、新增 Latin 209（run 拆分预期）；G11 0 SPILL、108 OBSERVE；G12 0 DEFECT；G13 0 TOUCH 0 NEAR；G14 P8 行数 195→206、余量 32.6→32.6px；G15a 多重集差 0、text.md BYTE-IDENTICAL；G15c ADOPT；G16 0 defective；D18 140.0px、D37 40.7pt。G15b 仅记录：1× `французском` / `объяснения`。

修复（0 处，全为字号缩小，零文案改动）：

_无修复。_

### 2026-w46-fr-zh-cn（读者 zh-cn，`_D5_READER = "cjk"`）

- 修前普查：D5 Latin in CJK / Cyrillic in CJK = 417/0；curly_in_cjk 0/0。
- 基线：TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；G15a 多重集差 0、text.md BYTE-IDENTICAL；印 PDF 21,354,923 B。
- run1 **15/19**：G1/G2 HDW 5、G6 0、G12 2 DEFECT、G14 5 DEFECT；D18 192.4px、D37 215.2pt。G6 0。G12 2 处 DEFECT：P4 `LES PHRASES DU COMMENTATEUR` +36.5、P6 `TROIS DATES POUR COMPRENDRE` +24.5（另 3 处同 core-fr 的共享串只判 OBSERVE：P3 `　纪念词表` +22.8、P3 `LES DATES EN CHIFFRES` +7.6、P5 `　周三电影` +43.3——修 core-fr 的共享 content 即同时修 zh-cn，故 zh-cn 修复表含此 3 处）。
- run2 **19/19**：G1 TOTAL 150、OVF 0、HDW 0；G3 lat/cyr/curly-in-CJK 0；G5 网 PDF 1,583,698 B（< 7 MB）；G6 0 flags；G7 p8 extract 121/150；G8 CLEAN；G9 8/8；G10 新增 CJK 0、新增 Latin 409（run 拆分预期）；G11 0 SPILL、116 OBSERVE；G12 0 DEFECT；G13 0 TOUCH 0 NEAR；G14 P8 行数 187→187、余量 33.7→32.7px；G15a 多重集差 0、text.md BYTE-IDENTICAL；G15c ADOPT；G16 0 defective；D18 192.4px、D37 215.2pt。G15b 仅记录：2× `15` / `练`。

修复（10 处，全为字号缩小，零文案改动）：

| 位置 | 旧→新 | 缺陷 | 探针宽 / 预算 | 余量 |
|---|---|---|---|---|
| `content12.py:124` | 25→24pt | P1-budget head HDW | 406.4px / 422.5px | 16.1px |
| `content34.py:76` | 23→21pt | P3 mots_fetes creambox +24.8/+22.8 | 386.5px / 400.5px | 14.0px |
| `content34.py:84` | 23→22pt | P3 zoom creambox +7.6 | 390.7px / 400.5px | 9.8px |
| `content34.py:161` | 加 `tsize=21`（默认 23→21） | P4 COMMENTATEUR f.box tsize 23->21 | 402.5px / 404.5px | 2.0px |
| `content56.py:80` | 23→20pt | P5 cine creambox +57.3/+43.3 | 385.9px / 400.5px | 14.6px |
| `content56.py:159` | 25→23pt | P6-opinion head HDW | 411.0px / 422.5px | 11.5px |
| `content56.py:165` | 25→24pt | P6-micro head HDW | 410.1px / 422.5px | 12.4px |
| `content56.py:189` | 加 `tsize=21`（默认 23→21） | P6 3dates f.box tsize 23->21 | 391.7px / 404.5px | 12.8px |
| `content7.py:38` | 24→23pt | P7-B2 head HDW | 411.0px / 422.5px | 11.5px |
| `content7.py:89` | 25→23pt | P7-clinic head HDW | 418.9px / 422.5px | 3.6px |

### 2026-w46-fr-zh-tw（读者 zh-tw，`_D5_READER = "cjk"`）

- 修前普查：D5 Latin in CJK / Cyrillic in CJK = 411/0；curly_in_cjk 0/0。
- 基线：TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；G15a 多重集差 0、text.md BYTE-IDENTICAL；印 PDF 21,420,041 B。
- run1 **15/19**：G1/G2 HDW 4、G6 0、G12 2 DEFECT、G14 3 DEFECT；D18 192.4px、D37 215.2pt。G6 0。G12 2 处：P4 `LES PHRASES DU COMMENTATEUR` +36.5、P6 `TROIS DATES POUR COMPRENDRE` +24.5。P3/P5 盒标题未越框、无需修：`head_mots_fetes` = `LES MOTS DU SOUVENIR`（无读者词）、`head_cine` = `LE CINÉMA DU MERCREDI　電影`（仅 2 字）。
- run2 **19/19**：G1 TOTAL 150、OVF 0、HDW 0；G3 lat/cyr/curly-in-CJK 0；G5 网 PDF 1,653,845 B（< 7 MB）；G6 0 flags；G7 p8 extract 121/150；G8 CLEAN；G9 8/8；G10 新增 CJK 0、新增 Latin 350（run 拆分预期）；G11 0 SPILL、116 OBSERVE；G12 0 DEFECT；G13 0 TOUCH 0 NEAR；G14 P8 行数 187→195、余量 33.7→32.7px；G15a 多重集差 0、text.md BYTE-IDENTICAL；G15c ADOPT；G16 0 defective；D18 192.4px、D37 215.2pt。G15b 仅记录：3× `單` / `&`。

修复（7 处，全为字号缩小，零文案改动）：

| 位置 | 旧→新 | 缺陷 | 探针宽 / 预算 | 余量 |
|---|---|---|---|---|
| `content12.py:124` | 25→24pt | P1-budget head HDW | 406.4px / 422.5px | 16.1px |
| `content34.py:84` | 23→22pt | P3 zoom creambox +7.6 | 390.7px / 400.5px | 9.8px |
| `content34.py:161` | 加 `tsize=21`（默认 23→21） | P4 COMMENTATEUR f.box tsize 23->21 | 402.5px / 404.5px | 2.0px |
| `content56.py:159` | 25→23pt | P6-opinion head HDW | 411.0px / 422.5px | 11.5px |
| `content56.py:165` | 25→24pt | P6-micro head HDW | 410.1px / 422.5px | 12.4px |
| `content56.py:189` | 加 `tsize=21`（默认 23→21） | P6 3dates f.box tsize 23->21 | 391.7px / 404.5px | 12.8px |
| `content7.py:38` | 24→23pt | P7-B2 head HDW | 411.0px / 422.5px | 11.5px |

## §6 core-fr（交叉核对）

### core-fr（读者 core (zh-cn)，`_D5_READER = "cjk"`）

- 修前普查：D5 Latin in CJK / Cyrillic in CJK = 417/0；curly_in_cjk 0/0。
- 基线：TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；G15a 多重集差 0、text.md BYTE-IDENTICAL；印 PDF 21,354,923 B。
- run1 **15/19**：G1/G2 HDW 5、G6 0、G12 5 DEFECT、G14 5 DEFECT；D18 192.4px、D37 215.2pt。G6 0。G12 5 处 DEFECT：P3 `　纪念词表` +22.8、P3 `LES DATES EN CHIFFRES` +7.6、P5 `　周三电影` +43.3、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P6 `TROIS DATES POUR COMPRENDRE` +24.5（core 自比 core=None 判 DEFECT；zh-cn 同值只判 OBSERVE）。
- run2 **19/19**：G1 TOTAL 150、OVF 0、HDW 0；G3 lat/cyr/curly-in-CJK 0；G5 网 PDF 1,583,706 B（< 7 MB）；G6 0 flags；G7 p8 extract 121/150；G8 CLEAN；G9 8/8；G10 新增 CJK 0、新增 Latin 409（run 拆分预期）；G11 0 SPILL、116 OBSERVE；G12 0 DEFECT；G13 0 TOUCH 0 NEAR；G14 P8 行数 187→187、余量 33.7→32.7px；G15a 多重集差 0、text.md BYTE-IDENTICAL；G15c ADOPT；G16 0 defective；D18 192.4px、D37 215.2pt。G15b 仅记录：2× `15` / `练`（与 zh-cn 同）。

修复（10 处，全为字号缩小，零文案改动）：

| 位置 | 旧→新 | 缺陷 | 探针宽 / 预算 | 余量 |
|---|---|---|---|---|
| `content12.py:124` | 25→24pt | P1-budget head HDW | 406.4px / 422.5px | 16.1px |
| `content34.py:76` | 23→21pt | P3 mots_fetes creambox +24.8/+22.8 | 386.5px / 400.5px | 14.0px |
| `content34.py:84` | 23→22pt | P3 zoom creambox +7.6 | 390.7px / 400.5px | 9.8px |
| `content34.py:161` | 加 `tsize=21`（默认 23→21） | P4 COMMENTATEUR f.box tsize 23->21 | 402.5px / 404.5px | 2.0px |
| `content56.py:80` | 23→20pt | P5 cine creambox +57.3/+43.3 | 385.9px / 400.5px | 14.6px |
| `content56.py:159` | 25→23pt | P6-opinion head HDW | 411.0px / 422.5px | 11.5px |
| `content56.py:165` | 25→24pt | P6-micro head HDW | 410.1px / 422.5px | 12.4px |
| `content56.py:189` | 加 `tsize=21`（默认 23→21） | P6 3dates f.box tsize 23->21 | 391.7px / 404.5px | 12.8px |
| `content7.py:38` | 24→23pt | P7-B2 head HDW | 411.0px / 422.5px | 11.5px |
| `content7.py:89` | 25→23pt | P7-clinic head HDW | 418.9px / 422.5px | 3.6px |

### §6.1 已发 (fr, zh-cn) 是 core-fr 构建，不是独立读者目录构建

- 印 PDF 逐字节相同：patched/core-fr `The-Lucerna-VOL3-fr.pdf` 与 patched/2026-w46-fr-zh-cn `The-Lucerna-VOL3-fr-zh-cn.pdf` 同为 10,134,957 B，SHA-256 同为 `42fd77e0a86ea1ef5b02a913f69f391dbe7a5557576528bed190ec38315daa4d`（仅文件名不同）；网 PDF 仅差 8 B（1,583,706 vs 1,583,698，webpdf 元数据浮动）。
- fitz 文字层：P1 前 200 字逐字相同（VOL. 3、HEBDOMADAIRE、SEMAINE DU 9 AU 15 NOVEMBRE 2026…）；页脚相同（“正文法语 / 讲解简体中文 / 第1版／共8版”）。
- 源相同：expl.py md5 同为 `47c918880512df366207e4b52d370198`；content*.py 12 版字节相同；G8 keydiff `[]`（zh-cn 与 core 均为自比）。
- production/2026-w46/core-fr/ 存在，内含 `2026-w46-fr-zh-cn.text.md`（以 zh-cn slug 命名）、ABSTRACT.txt、WEEKLY-KIT.md、content*.py、bslib4.py、build-fr.log 等。
- **结论：closer 将 patched/core-fr/ 同步进 production/2026-w46/core-fr/；与 D5 字面条款一致，无覆盖风险，无上报项。**

## D47 节（`###` 行丢失核对——本家不适用，0 丢失）

- D47 的 24pt 丢失只发生在 AST 导出器 `export_text.py`（nl 家）。fr 导出器 `export.py` **无 24pt 阈值**——stub（`stub_bslib.py`）无条件记录全部字符串，`export.py` L124 按 LOG kind（head/boxtitle/shead → `###`）无条件映射。
- 逐版核对：`###` 行数 **47/版 ×12**（`.text.md.new` 与 issues/ 已发版 `cmp` BYTE-IDENTICAL，故行数必然一致）；多重集差 0；UNEXPECTED 块数 0。**丢失行 0 行，无补行，builder 不改导出器阈值。**
- 47 个 `###` 盒头含全部修复点标题（`LE BUDGET EN TROIS PHRASES`、`IL EST PRÉVU QUE + SUBJONCTIF`、`LE COMPARATIF EN POLITIQUE`、`LES PHRASES DU COMMENTATEUR`、`TROIS DATES POUR COMPRENDRE`、`LES DATES EN CHIFFRES` 及各版读者词盒头，§7 已逐版核对在位）。

## D41 节（ja G14 2 项——审计 artifact，不修，不 run3）

- creambox 工具报 ja P5-jeunesse box1 两条 SPILL：`写真1枚は千の言葉に勝る？あなたの週を`（y_base 395.0 → y_patch 1873.0）与 `語る写真は？`（425.4 → 1901.0），box_bottom 471.9。run1 与 run2 同串同坐标。
- SVG 实测（2026-11-15）：同串 `E["debat5_note"]` 在两处合法出现——f.box `REGARDER UNE PHOTO` 内（rect 989,200,422.5,271.9，行 y=395/425.45，盒内）与右下 debat 盒内（rect 1439.5,1588,422.5,972，行 y=1873/1901，盒内）。D5 仅使 f.box 内行重排一字（`を` 自行 1 末移至行 2 首：基线行 1 `…あなたの週を` + 行 2 `語る写真は？`；patched 行 1 `…あなたの週` + 行 2 `を語る写真は？`，因数字 `1` 进 Newsreader 变宽；盒高不变，内容仍在盒内）。
- 误报机理：creambox 溢出检测按 joined 行串精确匹配；重排后盒内行串不再精确等于基线行串，唯一精确匹配落在下盒副本处，遂误判为溢出。G11 spill_sweep 对 ja 为 0 SPILL，G12 0 DEFECT。
- **决定：不修、不 run3**（无合法修复——降正文 21→20pt 只为迎合误报且改动已发版式）；按 D41 口径记录为 artifact，附 SVG 坐标证据，由重校复核，**提请协调员裁决工具行匹配逻辑**。ja 其余 18 门全绿。

## §7 内容抽查

- text.md 结构（12/12 同值，`.text.md.new`）：1,057 行、`## ` 页头 12 个、`### ` 盒头 47 个；占位串扫描 TODO/FIXME/XXX/lorem/`[untranslated]`/undefined **0 命中**。
- 修复点标题原位核对：共享标题（`LE BUDGET EN TROIS PHRASES`、`IL EST PRÉVU QUE + SUBJONCTIF`、`LE COMPARATIF EN POLITIQUE`、`LES PHRASES DU COMMENTATEUR`、`TROIS DATES POUR COMPRENDRE`、`LES DATES EN CHIFFRES`、`ZOOM`）及各版读者词标题（de `MICRO-DRILLS　KURZÜBUNGEN` / `BOÎTE À OUTILS　WERKZEUG` / `CLINIQUE DES ERREURS　FEHLER` 等 9 串、en 5 串、es 4 串、it 3 串、ja 1 串、nl 3 串、pt 5 串、zh-cn/core 3 串）**在各自 text.md 中 0 缺失**。
- 12 个 `##` 栏头齐全（含 `EXERCICES & RÉPONSES` 答案栏，各版读者语翻译一致）；卷头 `# Le Lucerna · Französische Wochenzeitung VOL.3` + 刊期行 + `VOL. 3　AUSGABE NR. 3` + 标语行 + `SEMAINE DU 9 AU 15 NOVEMBRE 2026` 逐版在位。
- 编号习题体：`^\d+\.\s` 匹配 131 项（编号按栏重启，缺号为连线题等非数字编号体；总数 150 以 G1 TOTAL 与 G15a 多重集差为准）。

## §8 同步清单（closer 用）

实测 `diff -rq patched/ vs production/2026-w46/`（排除 `__pycache__`/svg/cards/PDF/`.text.md`，日志 `logs/diff-patched-vs-production-final.txt`，KIT 更新后重跑）：

- 每读者版（de/en/es/it/ja/ko/nl/pt/zh-cn/zh-tw）同步 6 件：`WEEKLY-KIT.md`、`content12.py`、`content34.py`、`content56.py`、`content7.py`、`svglib.py`。
- ru 同步 2 件：`WEEKLY-KIT.md`、`svglib.py`（content*.py 零修复，与生产版逐字节相同）。
- core-fr 同步 6 件：`WEEKLY-KIT.md`、`content12.py`、`content34.py`、`content56.py`、`content7.py`、`svglib.py` → `production/2026-w46/core-fr/`。
- text.md：取 **`.text.md.new` 新导出件**，改名去掉 `.new` 后同步（见 §0.1 口径；目录内同名 `.text.md` 是旧 fanout 产物，**绝不取**）。
- 不同步：`assets/` 内 3 张故事 JPG（atget-paris / chrysanthemum-blanco / hiroshige-maple，D20）、`run.py` / `render.py`（scratch 构建驱动，生产目录本无此二件）、`__pycache__`、svg/、cards/、PDF（由 closer 在 production 内重建或拷 builder 原件，见 §10）、ABSTRACT.txt（排除）。
- 与修复清单一一对应：content*.py 的差异恰为 §1–§6 各版修复表（131 处）；svglib.py 的差异恰为 D1 hunk + D5 路由（`_D5_READER`、fix2、ru 分支）；其余源文件（expl.py、bslib4.py 等）**零差异**。

## §9 交付物 SHA 总表（run2 终轮实测）

| 版 | 印 PDF（字节 / SHA-256） | 网 PDF（字节 / SHA-256） | text.md `.new`（字节 / SHA-256） | 基线印 PDF（字节 / SHA-256） |
|---|---|---|---|---|
| 2026-w46-fr-de | 8,683,798 / `d7225f48a8d32e416a5ca3a27bcc8e19ecc1e56d6eb1c2642b2ae5e8cd985a71` | 1,209,895 / `d27cdc228c1ada2876225f8a87d5135492cb37480236645ae567e112e90f9ff0` | 45,709 / `fe0a9922c85606b7322c41b2a3a86e58f6a45daf452c89fb250656f7ed493e4e` | 9,191,671 / `bb29007c3ac34b0bbe2fd33ed1eaa202645499978ebc7909c5376b745e3bdda7` |
| 2026-w46-fr-en | 8,680,085 / `de154494dc6582f67f7a9b41a461c15edeb031eb86aa3278066205efd57630ac` | 1,206,200 / `12df4d2402f1d77c340f2bc3d9b202598a8af3b68d94eca80dbeda5736f3c2ae` | 45,147 / `30320a32aca75e8da681c8cf4e293899df9dd5b4863b730377449d659892cab7` | 9,186,502 / `00a53deaa7ff498d38af43a142a1004a75a3937f5459c324303544b689164858` |
| 2026-w46-fr-es | 8,680,457 / `72afe3c9f7aa0e8f3d0b9b10adedcce965a74fd5cc4a24016df20be77328411f` | 1,206,561 / `be385859a7596d1739ca6e56789b03378b973abb0f7b650e2c417f506f033fcc` | 45,660 / `ccca43880f69b832aa01b7fcc5fd17def009485770e924b66281be2e470a5962` | 9,173,346 / `00f2429ee0eb4da794481ec33cfcbc0494e6b0c095e2cdae4258b614b2672f55` |
| 2026-w46-fr-it | 8,676,523 / `0d868dd5e7fae1cfc7637ca8d1fcfe5d40166693a5faada92afd224a82c6f67c` | 1,202,591 / `f731751896a261c35b64859ad507c9db04d3598c595e9388b68ad5b5a7d07cb1` | 45,394 / `09a680f04bc18c39ff5ef6303b4de052c748abc44d571a5fe1f97769d1735384` | 9,170,576 / `8a7b70ee790d6369c70ed6bd535a176c7bd2725a674a5a96550fcd644a453fe3` |
| 2026-w46-fr-ja | 10,972,599 / `4267c698acd6f02240112bb3139467db4f0a0dfea96046ec47befb53c459d1f1` | 1,596,068 / `a6ca92e5bfb5abd444dcdca7281416af0101b918e7347f46225b6de9763abc8a` | 46,066 / `da25fecb2c3367472f1c874ac8c4b7e24adb01c889bb0e899545e1d089217ce3` | 21,442,781 / `70427aa0945acc68ad8b3d7358c077500126ac693651ea8a4f088a40b970ff86` |
| 2026-w46-fr-ko | 12,199,829 / `337fe71951d0b2382c57ae84920a19749e73fcb53ab4e401f52ffd26d6808c10` | 1,529,620 / `610c0073b2f97ede3bf0b9a8422c245a6abbaa6ec7aa62300cb8cddd6655d174` | 45,588 / `86f04d071399051007e1daf497e92d2c4783c020f73584236abe42410298143d` | 15,097,268 / `ad3b1de25fe353ee12a1a1bdec7083fa63ae341e869f6984c1f5db960bf784e4` |
| 2026-w46-fr-nl | 8,679,349 / `217b3f66f882996abada09f51a634491fb0a0ad069c28b9ac056c92f7b3c3201` | 1,205,454 / `ffba06bed6e8d26d16b163dbaa9ae0d5196a822034b02da4e39ccd795164cfec` | 45,444 / `61c21e51df12c5c6967ccbd0558ba5ce74fc3ba77ebdbe02492aae43f474e3cf` | 9,174,011 / `2917c2eda011de6b93d37f18f5072bda7058be06e5f8f94434908b788f05505f` |
| 2026-w46-fr-pt | 8,681,026 / `12b2b699e37adc55973317eeb2a36408d4e534afa57d82aa4be4096789a6f6c0` | 1,207,119 / `a3216051f0c099e8801de87937adcc7714a11724d68e5956b6ebb9cc0cbeda2c` | 45,458 / `6d4591fda5b652a8300f56d4a202279192c19d86015a711293cdaff5df7383e1` | 9,175,010 / `c011a0a909adb3ed37dd397c78d23203ffad04230e30f40573f621581724339d` |
| 2026-w46-fr-ru | 8,977,846 / `4d2c6440f259d823c9fecf36a290cb64963bf9f6d261db6bbb2a8dcac166d1c1` | 1,462,831 / `32828794342f20331b5d9118883475f2bd5ad224062cac35d29e877acb7b73b7` | 49,954 / `c34508d1ead03f247ffa9be2d6d12a1bdcb8e888a42c10bfa4c00a166ca70c51` | 9,232,415 / `9b2c17d1ba2ad0222909320b9d7bddfb5bdecee74094e5001c05d4ca68678c8b` |
| 2026-w46-fr-zh-cn | 10,134,957 / `42fd77e0a86ea1ef5b02a913f69f391dbe7a5557576528bed190ec38315daa4d` | 1,583,698 / `9a086afce8e2c943ea1ad56e0c1f51f2b922b19e335bf6cfb7b6b6a5d254ccf5` | 45,357 / `bc53a38cc7a81f66bf889972f6063af0aee2f222944d6b7f3af60dd1361cde00` | 21,354,923 / `fbca7b272eddaa8c1337719ae2a438e7fd6be53f36d066c9ec112a9484c08979` |
| 2026-w46-fr-zh-tw | 10,174,126 / `d334a600ae9081aaf7eb26dd3d2d53992248477b356e131309f1e71a80b08e28` | 1,653,845 / `1f4340bf75bec602b2b668ebc09da23764fb84a7a41d76377e6d679582d0f4d2` | 44,205 / `c388eeb4ecb538570b6e4d73745c7a817ce0e2bac191b0bb73949d3b4a955207` | 21,420,041 / `e0a7976bb8e83b1f7d6e15562a2276d173b8b51f4117397f3b2d5e44afd1b0d3` |
| core-fr | 10,134,957 / `42fd77e0a86ea1ef5b02a913f69f391dbe7a5557576528bed190ec38315daa4d` | 1,583,706 / `8814e539e796e3f7bd7bbd29a16dfcfd4f17b93cd0921e86a771cc80522f99dc` | 45,357 / `bc53a38cc7a81f66bf889972f6063af0aee2f222944d6b7f3af60dd1361cde00` | 21,354,923 / `fbca7b272eddaa8c1337719ae2a438e7fd6be53f36d066c9ec112a9484c08979` |

- text.md 12/12 与 `issues/2026-w46/<slug>/<slug>.text.md` `cmp` BYTE-IDENTICAL（SHA 与上表 text.md 列逐版相同）。
- core-fr 与 zh-cn：印 PDF 同字节同 SHA（`42fd77e0…daa4d`），text.md 同字节同 SHA（`bc53a38c…cde00`）；网 PDF 仅差 8 B（1,583,706 vs 1,583,698，webpdf 元数据浮动）。
- D47 已发版值：本家无 24pt 阈值丢失，`###` 行数 47/版（见 D47 节），无另表。

## §10 closer 交接

### KIT custody

- KIT 正本在 production；builder 已在 `patched/<slug>/WEEKLY-KIT.md` 追加 `## 补记：D5 字体重建（2026-11-15）`（D5 pin 块 + 重建节，12 份）。closer 按 §8 同步 patched KIT → production KIT（**单向**，绝不反向覆盖）。

### D19 核对结果

- KIT 内全部 `content*.py:NNN` 引用 **131/131 核对通过**（日志 `logs/d19-kit-check.txt`）：p.text/head 引用行含新字号字面；f.box 引用行 `content34.py:161`、`content56.py:189` 为收尾行 `], tsize=21)`。本报告 §1–§6 修复表引用与 KIT 同源（同一 margins 表生成），一致。

### 残留项

- ja G14 2 项 creambox SPILL 为审计 artifact（D41 节），不阻塞，待重校复核 + 协调员裁决工具行匹配逻辑。
- G15b 仅记录（11 版 rc=1、pt rc=2 无读者表）；验收以 G15a + G15c 为准。
- es D37 余量 4.9pt 偏紧（PASS，未改，留作观察）。
- zh-tw 保持 SC 面（§0.3），提请协调员/重校注意：D5-METHOD §1.2 的 TC 基底口径与实盘不符。
- de 基线 G12 1 OBSERVE（P1 BODY over +2.5px）为基线既有，先存。

### closer 待办（按序）

1. 按 §8 同步清单把 patched/ 差异文件 + `.text.md.new`（去 `.new` 后缀）同步进 `production/2026-w46/`（core-fr 进 `production/2026-w46/core-fr/`），一 bundle 一 commit（fr 家一 target 一 commit；zh-Hans 与 zh-Hant 各一 bundle）。
2. 在 production 内重建或拷 builder 原件交付 PDF（印/网），**绝不重跑 webpdf 覆盖 builder 的网 PDF**；核对 §9 SHA（印 PDF SHA 须与上表逐版一致；网 PDF 字节非确定性，以 closer 实测为准、文字层差 0 为验收）。
3. 针对性重验 G15a/G15c（text.md `cmp` vs issues/ + 多重集差 0）；D47 无补行（0 丢失）。
4. `lint.mjs` 全量门禁 + 独立重校（proofread-until-zero）；ja G14 2 项按 D41 节复核。
5. 推仓后清 scratch（按本地存储规矩：推完及时清，只留工具/脚本）。

### 交付物位置

- 本报告：`hidden_files/d5-redo/FAMILY-W46-FR-BUILD.md`。
- 门禁摘要：`scratch-2026-w46-fr/logs/<slug>/GATES-SUMMARY-run1.txt` / `-run2.txt`；基线 `GATES-SUMMARY-baseline.txt`。
- 修复 JSON：`logs/<slug>/fix-run2.json`、`fix-tsize-run2.json`；探针余量表：`logs/margins-run2.json`（`bin/derive_margins.py` 生成）；探针日志：`logs/probes-run1.txt`。
- 缺陷总表：`logs/defects-run1.txt`（405 行）、`logs/creambox-defects-run1.txt`（82 行）；D18 重测：`logs/measure-fixed-baseline-run1.log`；§8 diff：`logs/diff-patched-vs-production-final.txt`；D19：`logs/d19-kit-check.txt`；SHA 采集：`logs/collect-run2.txt`。
- D5 报告 + GATES-SUMMARY 复本：`notes/g-fr/scratch-d5-rebuild-fr/`（D29，见下）。