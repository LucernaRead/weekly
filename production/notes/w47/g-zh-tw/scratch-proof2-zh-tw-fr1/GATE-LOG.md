# GATE-LOG — W47 zh-tw-fr proof2 机械门独立重跑记录（重扩散新版）

- 复校对象：`production/2026-w47/2026-w47-zh-tw-fr/`（印 SHA `acd1d85b2af07310…` / 网 SHA `6026be3ed418a8bd…` / text SHA `673943a0de31811e…`，见 PROOF-NOTE.md）
- 工具：`~/workspace/weekly-git/tools/venv/bin/python`（正典栈）；TMPDIR 为 scratch 内 `tmp/`；`PYTHONDONTWRITEBYTECODE=1` 全程
- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` rc=0（`e69de29b…`），goals 侧真实写文件成功后开工
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-zh-tw-fr1/`（下称 `$S`），版目录 `$ED=~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-fr`，核心 `$CORE=~/workspace/weekly-git/production/2026-w47/core-zh-tw`
- 驱动：`$S/gates-proof2.py`（重扩散 `gates.py` 的复制本，仅改 M 路径指向本 scratch；`gtools/` 同为复制本）

## 1. 成品指纹（开工实测，sha256sum + stat）

- print `Lucerna-VOL4-FR.pdf` 20,191,919 B，SHA-256 `acd1d85b2af073100140a8bfd5936faeecc8a050f42226a424066aefce1aaf33` ✓
- web `Lucerna-VOL4-FR-web.pdf` 2,366,339 B，SHA-256 `6026be3ed418a8bd9574bfea2fd154ec7bc727d600b0eded0cff2b91a4070246` ✓
- text.md `2026-w47-zh-tw-fr.text.md` 52,470 B，SHA-256 `673943a0de31811ee43d899390a40fdde1c564ae7176f61878f77e1c687fa613` ✓
- 核心对照：印 `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a` 19,420,552 B；网 `1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240` 2,324,042 B；text `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b` 49,798 B ✓

## 2. run.py（副本重建，`$S/build/`）

命令：`rsync -a`（排除 hidden_files / *.pdf / *.text.md / cards / __pycache__ / ABSTRACT.txt）复制版目录到 `$S/build/`；`tools/venv/bin/python run.py > $S/build-run.log`（cwd=`$S/build/`）

- **RC=0**，0 FLOW OVERFLOW，0 HEAD TOO WIDE，0 警告；TOTAL 150；分级 A2 44 / B1 74 / B2 32；分页 10/18/18/18/18/18/12/38；类型 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1
- P7 col3 1823.3、teaser 2577.3（页脚规则 2596，余 18.7px）；P8 keys 末行 2431、写作条 1280.2、MODEL chars 142

## 3. SVG 重建比对 + 印 PDF 重渲（副本）

命令：`sha256sum $S/build/svg/*.svg > $S/rebuilt-svg-sha.txt`；`diff $S/prod-svg-sha.txt $S/rebuilt-svg-sha.txt`；`tools/venv/bin/python render.py > $S/build-render.log`（cwd=`$S/build/`）

- **SVG 重建 8/8 字节一致**（diff 空）
- render.py RC=0；重渲印 PDF 20,191,919 B，SHA `acd1d85b2af073100140a8bfd5936faeecc8a050f42226a424066aefce1aaf33`，**与交付逐字节相同**
- web PDF 未重渲染（字节不可复现），只比文字层（见 §10）

## 4. gates 驱动全跑

命令：`tools/venv/bin/python $S/gates-proof2.py fr proof2 > $S/gates-proof2-run.log`；结果 `$S/gates/fr-proof2/gates.json`

- checks：rc 0，PASS；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]
- occlusion：selftest rc 0，flags 0，rc 0
- p8：extract noted 150；compare CLEAN，keydiff=[]、missing=[]；`extra` 字段驱动取键 bug 显示 "?"，compare JSON 原文 extra=[]（`$S/gates/fr-proof2/p8-compare.json` 已核）
- creambox_canonical：36 盒，负 inside 清除 []；分页面最小 P1 18.8 / P2 15.8 / P3 15.8 / P4 9.8 / P5 6.4 / P6 19.9 / P7 12.5；P7 工具盒 +40.5/+12.5/+14.0
- boxtitle：36 盒，overruns 0，最小右余 -0.2px，rc 0
- creambox_pil：STRADDLE 0，CREAM-COVER 0，P7 最小清除 8.0，rc 0
- text_layer：-layout 110,315 / 110,315，多重集差 0；本週日 11/11、下週日 0/0、BABYMONSTER 0/0、取捨 2/2、end point 0/0、小雪 36/36
- pdf：印/网各 8 页、1462.5×2025 pt；P8 最小 9.75pt、最大 34.5pt；P1 顶部字号 [147.0, 45.0, 27.0, 24.0]；印 20,191,919 B / 网 2,366,339 B
- keycheck：填空键 54/54，缺失 []；答案键 1–150 连续（150/150）
- leak_scan：deny_hits {}；唯一共有长 ASCII 串「A. 12:00 · B. 14:00 · C. 19:00」
- abutting：P6 18:30/19:00 墨缝 0.6px（label1 墨右缘 990.8，label2 墨左缘 991.4）
- freeze：8/8，rc 0；核心完整性 OK（8 个核心 SVG 重哈希未变）

## 5. freeze diff --strict-cjk

命令：`tools/venv/bin/python tools/freeze.py diff --core-svg $CORE/svg --edition-svg $ED/svg --strict-cjk > $S/gates/fr-proof2/freeze-diff.log` → **rc=1**

- `STRICT-CJK FAIL`；分页：p1 +25/-25，CJK 892→879，added {'法': 2}；p2 +43/-39，1111→1106，{'法': 1}；p3 +48/-46，1198→1193，{'法': 1}；p4 +40/-37，810→805，{'法': 1}；p5 +50/-45，1220→1215，{'法': 1}；p6 +35/-33，884→879，{'法': 1}；p7 +114/-106，822→817，{'法': 1}；p8 +189/-179，1114→1109，{'法': 1}；TOTAL added CJK = 9，全部是家具「法語講解」中的「法」；正文 CJK 无新增。裁定：结构性误报，非缺陷。

## 6. spill 扫

命令：`python3 <w47/tools>/creambox_check.py $ED/svg/*.svg > $S/gates/fr-proof2/spill.log` → rc=0，**NO OVERFLOW**（36 盒 inside-clearance 全正；P2 盒最小 +15.8，P7 盒 +12.5 另见 canonical 扫）

## 7. 孤儿扫（自写，`$S/orphan_scan.py`）

命令：`tools/venv/bin/python $S/orphan_scan.py $S/gates/fr-proof2/orphan.json` → rc=0，原始候选 275 个
- 定义：同一栏内末行、长度 ≤2 字符或单个 ≤3 字母短词的文本元素（排除页脚/徽章/题号等家具）
- 裁定：全部为中文按字换行的正常末行碎片；无栏顶孤词、无脱离盒子的孤行；唯一单标点独占盒末行是 P4「你呢？」盒末行 "?"（x=1461.5, y=1362.2），在盒内（+9.6px），见 PROOF-NOTE O1。结论：**0 孤儿**。

## 8. 150 题三源逐题手验

命令：`tools/venv/bin/python $S/keycheck150.py > $S/keycheck150-run.log` → rc=0；parsed ed-svg=150 core-svg=150 textmd=150；mismatches 仅 [150]：#150 注释语言差异（版/ text.md 法文 "Tâche ouverte … (142 caractères)" vs 核心英文 "Open task … (142 characters)"），内容相同，记 OK。结果 `$S/keycheck-150.json`。
- 另逐题手验：算术/日期类复算 Q23 2000、Q24 800、Q41 17、Q42 1.5h、Q59 50、Q60 30、Q77 48、Q78 6、Q84/Q99 5h、Q85 1.5h、Q125 48、Q126 6、Q127 100、Q128 5h 全部正确；Q114 答案 B（SVG 原文核实）；F 范文 142 字。

## 9. text.md 全文通读 + text.md ↔ 印 PDF 文字层

- text.md 52,470 B：法语行 554 行全文读过（`$S/textmd-french.txt`，数字拆行已合并）；中文正文经 8 页渲染逐版读过；答案区 150 条逐条读过。
- 多重集比对（venv python）：非空白字符差 153，**CJK 字符差 0**；残差为 `#`×17、"Page N — …" 标题字母与 PDF 独有的 "Lucerna" 页眉词标（text.md 8 处页脚 vs PDF 16 处）。

## 10. 印/网文字层 + PDF 度量（见 §4 gates.json，不另跑）

- pdftotext -layout 印/网字节全等 110,315，多重集差 0；plain 差恰 1 字节（`\n`）
- VOL 计数（印文字层）：VOL.4 ×10、VOL.3 ×2、VOL.5 ×1

## 11. 日期/星期全验

命令：`TZ='Asia/Taipei' bash -c 'for d in ...; do date -d "$d" "+%A %F"; done'` → 2026-11-16 Monday、11-17 Tuesday、11-22 Sunday、11-13 Friday、12-27 Sunday、2027-01-03 Sunday、11-21 Saturday、11-06 Friday、10-23 Friday、11-24 Tuesday、12-04 Friday、12-05 Saturday——与版内标注全部一致。

## 12. §1.1 风格杂扫

- 纸色 `#fbfaf6`：8 个 SVG 各 1 处；`gold|brick` 命中仅 "Golden Horse"（`grep -o Gold` = 6）；`stroke-width="3"` 0 处；弯引号 “” 0、直引号 `"` 0
- 标题数实测：25px 章节头 39 个（P1 5 / P2 5 / P3 7 / P4 5 / P5 7 / P6 5 / P7 3 / P8 2）+ 奶油盒标题 36 个；“56 titles”无依据

## 13. 目视（交付 PDF 自行渲染，PyMuPDF 100dpi）

- 印 PDF P1–P8 → `$S/render/p1.png`–`p8.png`，逐版看过，无溢出/重叠/页脚碰撞
- 网 PDF P1、P4 → `$S/render/web-p1.png`、`web-p4.png`，与印版视觉一致
- 200dpi 裁切：P2 耶誕城标题 `$S/render/p2-christmasland-title-crop.png`（像素实测墨右缘 1860.5 < 盒右缘 1862.0，在盒内）；P4「你呢？」盒 `$S/render/p4-vous-crop.png`（"?" 在盒内，盒底留白可见）

## 14. 只读复核

- 未改任何生产文件内容、未 commit、未 push；全部写盘只在 goals 侧 `$S`（build 副本、gates、render）
- 生产成品印/网 PDF、text.md mtime 仍为 builder 的 2026-11-11 11:06–11:08；生产 `svg/` 8 文件 mtime 为 20:20:18–20:20:58，字节经开工实测与任务 SHA 一致、与副本重建逐字节一致（见 PROOF-NOTE §1）
- 核心三件 SHA 复核未变（见 §1）
