# GATE-LOG — 2026-w47-fr-ru fix-ru2（5 处门禁回归 + B1 答案 141，修后复核）

- 时间：2026-11-13 01:25–01:35 UTC；修复工人：协调员 #4 派
- 对象：~/workspace/weekly-git/production/2026-w47/2026-w47-fr-ru/
- 日志与证据：本目录 scratch-fix-fr-ru2/（measure*.py、textmd.diff、check_extra.log、
  run_gates-fix-ru2.log）；门禁全套日志：
  scratch-d5-rebuild-fr/2026-w47-fr-ru/logs-fix-ru2/

## 修法（每处只删一词，不改意、不改字号）

1. Occlusion P1：content12.py:28 头条 `ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI`
   → `ALCARAZ GAGNE PARIS, LE SÉNAT VOTE`（删 MERCREDI；星期三仍在正文与日期盒）。
   头条墨止 x=1124.0，与 audit 的 gloss 起点 1302.5 间隙 +178.5px。
2. Boxtitle P3：expl.py head_zoom `ZOOM　LES DATES EN CHIFFRES` → `ZOOM　DATES EN CHIFFRES`
   （+7.6 → −44.4px）。
3. Boxtitle P4：content34.py:158 f.box `LES PHRASES DU COMMENTATEUR`
   → `PHRASES DU COMMENTATEUR`（+36.5 → −15.5px）。
4. Boxtitle P5：expl.py head_cine `LE CINÉМА DU MERCREDI　КИНО` → `CINÉМА DU MERCREDI　КИНО`
   （+21.3 → −16.2px；被 flag 的是 head_cine，不是 head_mots_photo）。
5. Boxtitle P6：expl.py head_3dates `TROIS DATES POUR COMPRENDRE` → `DATES POUR COMPRENDRE`
   （+24.5 → −57.5px）。
6. B1：expl.py m_p8b `vainqueur = чемпион　b` → `vainqueur = победитель　b`
   （与 P1 译注 `un vainqueur победитель` 统一；`чемпион` 仅留 g4 `действующий чемпион`
   = tenant du titre，词不同）。

宽度事前用版内 svglib 真墨数学逐项验算（measure3.py），修前门禁数值逐位复现
（P1 −108.5≈audit −108.2；P3 +7.6；P4 +36.5；P5 +21.3；P6 +24.5）。

## 新旧 SHA（SHA-256 全值见 KIT；以下 SHA-12）

- 印 PDF La-Lucerna-VOL4-fr-ru.pdf：1aa7c71d7f2e / 17,222,306 B → **af7d37bc0a56 / 17,222,281 B**
- 网 PDF La-Lucerna-VOL4-fr-ru-web.pdf：85c45f1cff46 / 1,773,870 B → **f6e82ee074cf / 1,773,854 B**
- text.md：028cb8c2d4b0 / 50,495 B → **ae0a0429047a / 50,475 B**

## text.md 重导出 diff（只许改动处变）

diff vs 修前恰好 6 行：L19 头条、L415 head_zoom、L505 P4 box、L655 head_cine、
L785 head_3dates、L1083 Q141 注记。542 entries / 150 exercises 不变。

## 门禁逐项（run_gates.sh fix-ru2；FAILFLAG=0）

1. run.py：TOTAL 150，0 FLOW OVERFLOW；1 HEAD TOO WIDE（P7-outils，修前已存在，不在本
   次范围）。render rc=0，webpdf rc=0。
2. p8 extract --total：150/150，noted 121/150。compare vs core-fr：CLEAN，
   missing=[] extra=0 uncertain=[]，keydiff=[150]（已知 Q150 读者语标签）。
   compare vs 修前 baseline：CLEAN，keydiff=[]（键未变；B1 改的是注记）。
3. occlusion_audit.py：rc=0，**0 flags**（修前 1 flag）。
4. boxtitle_check.py：rc=0，**0 DEFECT**（53 titles / 549 body lines；修前 4 DEFECT）。
5. spill_sweep.py：rc=0，0 SPILL（33 boxes / 151 candidates / 151 OBSERVE）。
6. pdf_edge_scan.py：rc=0，8 pages，0 TOUCH，0 NEAR（top 54.0 / bottom 53.6 /
   left 65.5–65.9 / right 45.0–66.2 pt，与修前一致）。
7. D5 census：rc=0，CENSUS PASS（D5_latin_in_cjk=0，D5_cyrillic_in_cjk=0，
   curly_in_cjk=0；fr-ru runs LAT@Newsreader 23917、CYR@NotoSans 5246 不变）。
8. 文本层 multiset：(a) 印 vs 网 PDF 文本层逐字节相同（96,699 字符，multiset diff 0）；
   (b) p8 键 150/150 与 text.md 答案键逐字一致（注记剥离后 diff 0；Q25 'd'、
   Q141 'b'、Q150 'Открытый вопрос'）；(c) SVG 全文 multiset vs 印 PDF 文本层 diff 0
   （35,395 非空字符；`&amp;` ×3 为 XML 转义假象，已计入）。
9. freeze：freeze.py baseline rc=0（core 8 文件完整性 OK）；diff vs core-fr rc=0，
   TOTAL added CJK 10（全 U+3000，与修前一致），added Latin 208（修前 203；
   core-vs-edition 差分按工具文档必然 wholesale 添拉丁，--strict-latin 不适用，
   不作 FAIL 判据）。源↔PDF 同步：两 PDF 建于最后一次源码改动（01:25:28）之后，
   其后无源码改动。
10. 成品形态：印/网 PDF 各 8 页（1462.5×2025 pts）；VOL.4 ×11 + VOL. 4 ×1；
    网 PDF 1,773,854 B < 7 MB；文本层 51,025 B 非空。新串逐项核对进印 PDF 文本层
    （头条 / DATES EN CHIFFRES / PHRASES DU COMMENTATEUR / CINÉМА DU MERCREDI КИНО /
    DATES POUR COMPRENDRE / Q141 `победитель b)`），旧串 6 处均为 0。

## 附带说明（非 FAIL）

- creambox FAIL 3 defects：与 r1/r2 完全相同的已裁定误报（P5 `debat5_note` 复文
  被按精确文本匹配到第二处；字符串与坐标与 KIT 记录逐位一致）；独立 spill 门禁
  0 SPILL。creambox 不在本次任务门禁清单内，未作内容改动。
- 协调：fr-family 工人（scratch-fix-fr-family1/）01:20 UTC 搭架但修毕时未动过 fr-ru
  文件；本次 01:27 UTC 构建为当前态，按协调员令，其后续 fr 家工作须以此修后态为
  基础，不得覆盖。

## 结论

- 6 处修复全部落地；门禁清单 8 项全绿（p8、occlusion、boxtitle、spill、edge、
  D5 census、文本层三方一致、freeze、成品形态）。
- 未 commit、未 push、未动其他版。KIT 已同步新 SHA + Fix 记录。
