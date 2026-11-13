# D5 重建工作日志 — zh-cn 目标家庭（W47）

工人：D5 重建工人（zh-cn 家庭）。范围：core-zh-cn（= zh-cn-en 版，印 PDF 逐字节相同）
+ 9 个 fan-out：zh-cn-de / zh-cn-fr / zh-cn-es / zh-cn-it / zh-cn-pt / zh-cn-nl / zh-cn-ru /
zh-cn-ja / zh-cn-ko。不建 zh-cn-zh-tw（跨体裁定组合不存在），不另建 zh-cn-en。

裁定正本：`scratch-d5-plan/mechanism/CJK-DECISION.md`；简报：同目录 `brief-d5-rebuild.md`。
解释器全程 `tools/venv/bin/python`。不 commit、不 push、不跑 lint --write。
磁盘门限：df 已用 ≥100G 立即停手。开工时 91G 已用。

## 0. 开工核对（2026-11-12）

- core-zh-cn 印 PDF `Lucerna-VOL4.pdf` 与 `2026-w47-zh-cn-en/Lucerna-VOL4-EN.pdf`
  sha256 同为 `c34f5a54e491a085ea3e19a986748938dda79294b90d154a8e746f54a9eb05aa`（41,763,115 B）。
  网 PDF 不同（见各版记录）。
- core-zh-cn svglib 未打 D5（旧式 `_char_font`，无 `_D5_READER`）；其余 9 版 svglib
  md5 `a6fd6f1d…`（zh-cn-ja 为 JP 改写版、zh-cn-ru 为 +unkerned 块版）。
- tools 自检：`d5_creambox_audit.py --selftest` OK；`head_check.py --selftest` OK。
- 备份布局：`scratch-d5-zh-cn/scratch-fanout-zh-cn/backup/<slug>/`（去 PDF、去 __pycache__；
  供 boxtitle `--backup-root scratch-d5-zh-cn` 与 creambox 基线对照用）。

## 0b. 接替核实（2026-11-12，工人 4bd662d3 接棒 ffe1ed8e）

- df：92G 已用 / 150G（62%），低于 100G 门限。
- 已验 5 版生产 SHA 与本日志一致：core 印 `f7b13153…551041` / 网 `7088ff06…0318ac7f`；de 印 `778118ef…0e92eec` / 网 `4d937086…7dfc05`；fr 印 `b76447c9…379294` / 网 `fd1fd83b…522ef4`；es 印 `6a34c9e1…3d503` / 网 `f5cd5f46…65a0a`；it 印 `f3c6061e…5b58b1` / 网 `3b2e81e4…2e0ebd`。svglib 均已打 D5（`_D5_READER = "latin"`，md5 `35e83e68…da821`）。
- **pt：已重建、门禁中断在 render.py 之后**。生产印 `d4c27a7fc2a4` 33,516,121 B（修前 `6644cd43` 41,734,802 B，已变）；网仍修前 `68680e3b342c`（未跑 webpdf）。`GATES-SUMMARY.txt` 只到 render.py。svglib 已装（md5 与 core 同）。待：自 webpdf 起补全门禁 + KIT 同步。
- **nl：已装机、未重建**。svglib md5 与 core 同（`35e83e68`），生产印仍修前 `3a160cae374c` 44,048,879 B。待：重建 + 全套门禁 + KIT 同步。
- **ru / ja / ko：未装机**。svglib 仍修前（ru `13e7fa70…`、ja `4edca36a…`、ko `a6fd6f1d…`）；生产印/网均为修前 SHA（见各版 pdf-pre.sha256）。待：装机（ru 模式 / cjk 模式）+ 重建 + 全套门禁 + KIT 同步。
- **zh-cn-en 目录（待协调员定）**：svglib 仍修前（`a6fd6f1d`），印仍修前 `c34f5a54e491` 41,763,115 B，网仍修前 `97e3082d90e2`。core 已是 D5 版。本任务指令“核心重建一次即可，不要另建一个 zh-cn-en”，故本工人不单独重建该目录；但 `tools/insert.py` 的 `resolve_bundle_dir` 优先取已存在的版目录，插仓时会读该目录的网 PDF——此为遗留风险，见 §4 汇总报协调员。

## 1. core-zh-cn（= zh-cn-en）— ALL-GREEN，零缺陷，无内容修补

- Pre-record：印 `c34f5a54…eb05aa` 41,763,115 B；网 `6b7a12f5…263d9` 2,632,446 B；
  text.md `23fb62bd…bf04`；普查 D5 拉丁 444 / 西里尔 0 / 弯引号 CJK 0（总数 4，全 Newsreader）；
  quotes 0 缺陷。基线：freeze 8/8，原地 run.py TOTAL 150、0 警告、SVG 不变。
- 装机：`apply_variant.py --patch-core zh-cn --i-understand-this-writes-production`；
  变更：Noto Sans faces + sans_noto cmaps/_PATH + _CYR/family + _QUOTE_CLS + fix2 + D5 block +
  `_D5_READER = "latin"` + italic sans_noto_i + sans 注释。
- 门禁（首轮全绿，`logs/core-zh-cn/GATES-SUMMARY.txt`）：run TOTAL 150 / 0 OVERFLOW / 0 HEAD；
  head_check 0；occlusion 0；p8 extract 150、compare vs 修前 base CLEAN keydiff=[]；
  freeze baseline 8/8；freeze diff vs base 新增 CJK 0（新增拉丁串 276，run 拆分）；
  spill 0（35 boxes，86 candidates）；boxtitle 0 DEFECT（48 titles，589 body lines，真备份）；
  edge 0/0；creambox PASS 0（n=368，中位 1.015，粗体 1.040；P8 246→246 行，余量 55.9→55.9px）；
  census PASS（拉丁 444→0）；quotes 0；textcheck PASS（印/网/修前均为 22,523 非空白字符）；
  text.md 字节不变。
- 新交付物：印 `f7b13153…551041` 33,521,853 B；网 `7088ff06…0318ac7f` 2,434,915 B。
  印 PDF 变小 8.2MB：拉丁离开 CJK 面后嵌的字形少了。内容零改动。
- KIT 同步：`WEEKLY-KIT.md` Measured totals 文件行更新 + 文末新增 “D5 rebuild” 记录。
  freeze build-copy 已清。

## 2. fan-out（9 版）

基线（全部 9 版，修前）：freeze baseline 8/8、原地 run.py TOTAL 150、0 FLOW OVERFLOW、
0 HEAD TOO WIDE、SVG 与交付字节一致。普查（修前，`logs/<slug>/census-pre.json`）：
de 462 / fr 458 / es 461 / it 454 / pt 457 / nl 455 / ru 拉丁 243+西里尔 325 /
ja 244 / ko 240；弯引号缺陷全 0。备份齐于 `scratch-fanout-zh-cn/backup/<slug>/`。

### zh-cn-de — ALL-GREEN，零缺陷，无内容修补

- Pre-record：印 `b38ffe40…ee97279` 44,829,877 B；网 `cf42d84a…deb733a` 2,732,377 B；
  text.md `51d6dab1…06e0a1e`；普查拉丁 462；quotes 0。
- 装机：`--target zh-cn --reader de`（latin）；装后 svglib 与已打补丁的核心逐字节相同
  （md5 `35e83e68…da821`）。
- 门禁（首轮全绿）：run TOTAL 150 / 0 / 0；head_check 0；occlusion 0；p8 150、CLEAN
  keydiff=[]；freeze baseline 8/8；diff vs base 新增 CJK 0（新增拉丁串 272）；
  diff vs core 新增 CJK 0；spill 0（35 boxes，83 candidates）；boxtitle 0 DEFECT
  （48 titles，595 body lines）；edge 0/0；creambox PASS 0（n=377，中位 1.013，粗体 1.040；
  P8 222→222 行，余量 58.9→58.9px）；census PASS（462→0）；quotes 0；
  textcheck PASS（23,731 非空白字符三方一致）；text.md 字节不变。
- 新交付物：印 `778118ef…0e92eec` 33,519,497 B；网 `4d937086…7dfc05` 2,433,374 B。
- KIT 同步：Artifacts（final）印/网行更新 + 文末新增 “D5 rebuild” 记录；并注记
  11-11 KIT 数与交付文件已有约 100 B 出入（修前已存在，与 D5 无关，报协调员）。
  freeze build-copy 已清。

### zh-cn-fr — ALL-GREEN，零缺陷，无内容修补

- Pre-record：印 `097c8818…68b8e` 42,504,769 B；网 `6556d667…13695` 2,663,743 B；
  text.md `e125a9d1…12e6`；普查拉丁 458；quotes 0。
- 装机：`--target zh-cn --reader fr`（latin）；装后 svglib 与已打补丁的核心逐字节相同。
- 门禁（首轮全绿）：run TOTAL 150 / 0 / 0；head_check 0；occlusion 0；p8 150、CLEAN
  keydiff=[]；freeze baseline 8/8；diff vs base 新增 CJK 0（新增拉丁串 272）；
  diff vs core 新增 CJK 0；spill 0（35 boxes，85 candidates）；boxtitle 0 DEFECT
  （46 titles，592 body lines）；edge 0/0；creambox PASS 0（n=373，中位 1.008，粗体 1.040；
  P8 199→199 行，余量 67.2→67.2px）；census PASS（458→0）；quotes 0；
  textcheck PASS（23,968 非空白字符三方一致）；text.md 字节不变。
- 新交付物：印 `b76447c9…379294` 33,513,605 B；网 `fd1fd83b…522ef4` 2,427,580 B。
- KIT 同步：Artifacts（final）印/网行更新 + 文末新增 “D5 rebuild” 记录；11-11 KIT 数
  与交付文件约 10 B 出入（修前已存在，同 de 模式）。
  freeze build-copy 已清。

### zh-cn-es — ALL-GREEN，零缺陷，无内容修补

- Pre-record：印 `ba184b75…97c4182` 44,799,095 B；网 `399a11df…1d405b` 2,723,553 B；
  text.md `edc045da…7f482`；普查拉丁 461；quotes 0。
- 装机：`--target zh-cn --reader es`（latin）；装后 svglib 与已打补丁的核心逐字节相同。
- 门禁（首轮全绿）：run TOTAL 150 / 0 / 0；head_check 0；occlusion 0；p8 150、CLEAN
  keydiff=[]；freeze baseline 8/8；diff vs base 新增 CJK 0（新增拉丁串 272）；
  diff vs core 新增 CJK 0；spill 0（35 boxes，86 candidates）；boxtitle 0 DEFECT
  （44 titles，594 body lines）；edge 0/0；creambox PASS 0（n=372，中位 1.008，粗体 1.040；
  P8 217→216 行，余量 55.9→55.9px）；census PASS（461→0）；quotes 0；
  textcheck PASS（23,575 非空白字符三方一致）；text.md 字节不变。
- 新交付物：印 `6a34c9e1…3d503` 33,515,606 B；网 `f5cd5f46…65a0a` 2,429,057 B。
- KIT 同步：Artifacts（final）印/网行更新 + 文末新增 “D5 rebuild” 记录；注记网 PDF
  与 KIT build-#3 数差 6 B（KIT 自记网 PDF 未随 fix1 重建，修前已存在）。
  freeze build-copy 已清。

### zh-cn-it — ALL-GREEN，零缺陷，无内容修补

- Pre-record：印 `440490c4…98a69d` 41,730,133 B；网 `c216bbb1…a7a52` 2,641,786 B；
  text.md `afc9b2c0…544f`；普查拉丁 454；quotes 0。
- 装机：`--target zh-cn --reader it`（latin）；装后 svglib 与已打补丁的核心逐字节相同。
- 门禁（首轮全绿）：run TOTAL 150 / 0 / 0；head_check 0；occlusion 0；p8 150、CLEAN
  keydiff=[]；freeze baseline 8/8；diff vs base 新增 CJK 0（新增拉丁串 272）；
  diff vs core 新增 CJK 0；spill 0（35 boxes，86 candidates）；boxtitle 0 DEFECT
  （48 titles，589 body lines）；edge 0/0；creambox PASS 0（n=368，中位 1.012，粗体 1.040；
  P8 199→199 行，余量 51.8→51.8px）；census PASS（454→0）；quotes 0；
  textcheck PASS（23,696 非空白字符三方一致）；text.md 字节不变。
- 新交付物：印 `f3c6061e…5b58b1` 33,509,850 B；网 `3b2e81e4…2e0ebd` 2,423,808 B。
- KIT 同步：Artifacts（final）印/网行更新 + 文末新增 “D5 rebuild” 记录；注记网 PDF
  与 KIT 数差 18 B（KIT 自记 fix1 未重建网 PDF，修前已存在）。
  freeze build-copy 已清。

### zh-cn-pt — ALL-GREEN，零缺陷，无内容修补（接替工人 4bd662d3 补完门禁）

- Pre-record：印 `6644cd43…7dccb` 41,734,802 B；网 `68680e3b…54d` 2,647,149 B；
  text.md `ed085834…9808d94`；普查拉丁 457；quotes 0。
- 装机（前任）：`--target zh-cn --reader pt`（latin）；装后 svglib 与已打补丁的核心逐字节相同。
- 门禁（首轮全绿，接替后重跑全套 `gates.sh`，exit 0；重建确定性：印 PDF 与前任
  09:26 UTC 产物逐字节相同 `d4c27a7f…`）：run TOTAL 150 / 0 / 0；head_check 0；
  occlusion 0；p8 150、CLEAN keydiff=[]；freeze baseline 8/8；diff vs base 新增 CJK 0
  （新增拉丁串 277）；diff vs core 新增 CJK 0；spill 0（35 boxes，84 candidates）；
  boxtitle 0 DEFECT（48 titles，588 body lines）；edge 0/0；creambox PASS 0（n=373，
  中位 1.008，粗体 1.040；P8 202→202 行，余量 51.8→51.8px）；census PASS（457→0）；
  quotes 0；textcheck PASS（23,297 非空白字符三方一致）；text.md 字节不变。
- 新交付物：印 `d4c27a7f…86a72` 33,516,121 B；网 `a3a92057…5c926` 2,430,183 B。
- KIT 同步：Artifacts（final）印/网行更新 + 文末新增 “D5 rebuild” 记录；注记网 PDF
  与 KIT 数差 56 B（KIT 自记 2,647,093 B / `030f52fb…`，修前已存在）。
  freeze build-copy 已清。

### zh-cn-nl — ALL-GREEN 除 1 处有意内容修补（接替工人 4bd662d3）

- Pre-record：印 `3a160cae…4c628` 44,048,879 B；网 `dd9e804f…c60c8` 2,702,851 B；
  text.md `9bc8212f…0732b8`；普查拉丁 455；quotes 0。
- 装机（前任）：`--target zh-cn --reader nl`（latin）；装后 svglib 与已打补丁的核心逐字节相同。
- 首轮门禁：唯一缺陷 HEAD TOO WIDE ×1（P7-a2 `A2　决赛与包裹　Finale & pakketten`，
  24pt 粗体 425.2px vs 栏宽 422.5px，超 2.7px）；其余全绿。
- 内容修补：`content7.py:16` 与 text.md:1313 同改 → `A2　决赛与包裹　Finale pakketten`
  （401.5px，留 21.0px；字号 24 不变，双词保留）。二轮门禁：run TOTAL 150 / 0 / 0；
  head_check 0；occlusion 0；p8 150、CLEAN keydiff=[]；freeze baseline 8/8；diff vs base
  新增 CJK 0（新增拉丁串 280）；diff vs core 新增 CJK 0；spill 0（35 boxes，84 candidates）；
  boxtitle 0 DEFECT（48 titles，591 body lines）；edge 0/0；creambox PASS 0（n=370，
  中位 1.012，粗体 1.040；P8 220→220 行，余量 55.9→55.9px）；census PASS（455→0）；
  quotes 0；textcheck 印/网一致（23,167 字符），修前→修后仅差 `removed={'&': 1}`（即修补
  本身）；text.md 仅 1313 行一处改动（`9bc8212f…` → `1f864e74…`，50,059 → 50,057 B）。
  gates.sh 总评 HAS-FAILURES 仅因此两项基线对照（修补所致），其余全绿。
- 新交付物：印 `b317ad38…06a35` 33,512,276 B；网 `29150ee7…4074c` 2,426,135 B。
- KIT 同步：Artifacts（final）印/网/text.md 行更新 + 文末新增 “D5 rebuild” 记录（含修补
  说明）；注记网 PDF 与 KIT 数差 197 B（KIT 自记 2,703,048 B / `495594dc…`，修前已存在）。
  freeze build-copy 已清。

### zh-cn-ru — ALL-GREEN 除 2 处有意内容修补（接替工人 4bd662d3）

- Pre-record：印 `f1b2162d…189fe` 33,572,048 B；网 `dbf960ab…4ee1` 2,485,880 B；
  text.md `de12db58…08094`；普查拉丁 243 + 西里尔 325；quotes 0。
- 装机：`--target zh-cn --reader ru`（mode `ru`，`_D5_READER = "ru"`）；装后 svglib
  与已打补丁的核心仅差 `_D5_READER` 一行 + 既有 unkerned 块（md5 `71ed2bfc…25a6e`）。
- 首轮门禁：唯一缺陷 HEAD TOO WIDE ×2（P7-a2 `Финал и посылки` 422.7px 超 0.2px；
  P8-ex D `Читай и ответь` 428.5px 超 6.0px）；其余全绿（census 拉丁/西里尔均 0，
  Noto Sans 元素 790——ru 路径真实触发）。
- 内容修补：P7-a2 → `Финал посылки`（399.2px，留 23.3px）；P8-ex D → `Читай, ответь`
  （411.8px，留 10.7px；逗号式与 es/it/nl 的 D 头一致）。`content7.py:16` /
  `content8.py:74` 与 text.md:1313 / :1703 同改。二轮门禁：run TOTAL 150 / 0 / 0；
  head_check 0；occlusion 0；p8 150、CLEAN keydiff=[]；freeze baseline 8/8；diff vs base
  新增 CJK 0（新增拉丁串 121）；diff vs core 新增 CJK 0；spill 0（35 boxes，90 candidates）；
  boxtitle 0 DEFECT（48 titles，617 body lines）；edge 0/0；creambox PASS 0（n=377，
  中位 1.002，粗体 0.956——ru 符号翻转预期内；P8 224→224 行，余量 55.9→55.9px）；
  census PASS（拉丁 243→0，西里尔 325→0）；quotes 0；textcheck 印/网一致（22,681 字符），
  修前→修后仅差 `added={',': 1} removed={'и': 2}`（即两处修补）；text.md 仅两行改动
  （`de12db58…` → `eb5345d9…`，60,508 → 60,503 B）。gates.sh 总评 HAS-FAILURES 仅因此
  两项基线对照（修补所致），其余全绿。
- 新交付物：印 `1b71f5d4…e3b99` 33,721,996 B；网 `2eee3f44…af07d` 2,634,216 B。
- KIT 同步：Artifacts（final）印/网/text.md 行更新 + 文末新增 “D5 rebuild” 记录。
  freeze build-copy 已清。

### zh-cn-ja — ALL-GREEN，零缺陷，无内容修补（接替工人 4bd662d3）

- Pre-record：印 `c395a505…353b6` 36,336,862 B；网 `65347722…f07d` 2,900,720 B；
  text.md `68d850ea…5e4`；普查拉丁 244；quotes 0。
- 装机：`--target zh-cn --reader ja`（mode `cjk`，`_D5_READER = "cjk"`；SC→JP 改写，
  kinsoku 已有）；装后 svglib 与已打补丁的核心仅差 JP 面名 + `_D5_READER` 一行。
- 门禁（首轮全绿）：run TOTAL 150 / 0 / 0；head_check 0；occlusion 0；p8 150、CLEAN
  keydiff=[]；freeze baseline 8/8；diff vs base 新增 CJK 0（新增拉丁串 161）——D5 对照；
  diff vs core 新增 CJK 4648 为日语讲解层本身，非 D5 效应；spill 0（35 boxes，
  107 candidates）；boxtitle 0 DEFECT（26 titles，712 body lines）；edge 0/0；
  creambox PASS 0（n=361，中位 1.009，粗体 1.040；P8 224→224 行，余量 55.9→55.9px）；
  census PASS（244→0）；quotes 0；textcheck PASS（17,708 非空白字符三方一致）；
  text.md 字节不变。
- 新交付物：印 `d2e3ee82…1a249` 35,542,943 B；网 `fa614f26…37fb44` 2,826,687 B。
- KIT 同步：Artifacts（final）印/网行更新 + 文末新增 “D5 rebuild” 记录；注记网 PDF
  与 KIT 数差 1 B（KIT 自记 2,900,721 B / `c620b9ee…`，修前已存在）。
  freeze build-copy 已清。

### zh-cn-ko — ALL-GREEN，零缺陷，无内容修补（接替工人 4bd662d3）

- Pre-record：印 `69744432…3ff30` 36,966,247 B；网 `ec02a819…83c0` 2,817,984 B；
  text.md `eb5fdedd…63c0`；普查拉丁 240；quotes 0。
- 装机：`--target zh-cn --reader ko`（mode `cjk`，`_D5_READER = "cjk"`；SC→KR 改写）；
  装后 svglib 与已打补丁的核心仅差 KR 面名 + `_D5_READER` 一行。
- 门禁（首轮全绿）：run TOTAL 150 / 0 / 0；head_check 0；occlusion 0；p8 150、CLEAN
  keydiff=[]；freeze baseline 8/8；diff vs base 新增 CJK 0（新增拉丁串 153）——D5 对照；
  diff vs core 新增 CJK 4038 为韩语讲解层本身，非 D5 效应；spill 0（35 boxes，
  140 candidates）；boxtitle 0 DEFECT（51 titles，935 body lines）；edge 0/0；
  creambox PASS 0（n=359，中位 1.010，粗体 1.040；P8 221→221 行，余量 53.9→53.9px）；
  census PASS（240→0）；quotes 0；textcheck PASS（17,555 非空白字符三方一致）；
  text.md 字节不变。
- 新交付物：印 `a4fa88ef…87c4f5` 36,955,697 B；网 `43f7a29a…fbb8c` 2,808,430 B。
- KIT 同步：Artifacts（final）印/网行更新 + 文末新增 “D5 rebuild” 记录；注记网 PDF
  与 KIT 数差 3 B（KIT 自记 2,817,987 B / `bbf0d14d…`，修前已存在）。
  freeze build-copy 已清。

## 3. 汇总

| 版 | 印 PDF（生产 SHA 前 12 + 大小） | 网 PDF（生产 SHA 前 12 + 大小） | 门禁 | KIT |
|---|---|---|---|---|
| core-zh-cn（= zh-cn-en） | `f7b131533cda` 33,521,853 B | `7088ff061297` 2,434,915 B | ALL-GREEN，0 缺陷 | 已同步 |
| zh-cn-de | `778118ef7b60` 33,519,497 B | `4d937086bd26` 2,433,374 B | ALL-GREEN，0 缺陷 | 已同步 |
| zh-cn-fr | `b76447c9c2a5` 33,513,605 B | `fd1fd83b1ce0` 2,427,580 B | ALL-GREEN，0 缺陷 | 已同步 |
| zh-cn-es | `6a34c9e1a097` 33,515,606 B | `f5cd5f4687c8` 2,429,057 B | ALL-GREEN，0 缺陷 | 已同步 |
| zh-cn-it | `f3c6061e9a2c` 33,509,850 B | `3b2e81e4a3d2` 2,423,808 B | ALL-GREEN，0 缺陷 | 已同步 |
| zh-cn-pt | `d4c27a7fc2a4` 33,516,121 B | `a3a92057bead` 2,430,183 B | ALL-GREEN，0 缺陷 | 已同步 |
| zh-cn-nl | `b317ad38804e` 33,512,276 B | `29150ee7cb3c` 2,426,135 B | 除 1 处有意修补（P7-a2 头去 `&`）外全绿 | 已同步 |
| zh-cn-ru | `1b71f5d44d46` 33,721,996 B | `2eee3f4487d8` 2,634,216 B | 除 2 处有意修补（P7-a2、P8-ex D 头）外全绿 | 已同步 |
| zh-cn-ja | `d2e3ee82fc0e` 35,542,943 B | `fa614f26d856` 2,826,687 B | ALL-GREEN，0 缺陷 | 已同步 |
| zh-cn-ko | `a4fa88ef2420` 36,955,697 B | `43f7a29a3843` 2,808,430 B | ALL-GREEN，0 缺陷 | 已同步 |

- 10 版全部在生产目录原地重建，生产印/网 SHA 与各版 `GATES-SUMMARY.txt` /
  `pdf-post.sha256` 逐版核对一致；每版 freeze build-copy 已清。
- 独立重校（SOP §8.4）未做，由协调员另派。
- 未完成项：无。遗留待协调员定：`2026-w47-zh-cn-en/` 目录仍为修前版（印
  `c34f5a54e491` 41,763,115 B、网 `97e3082d90e2`），见 §0b——insert 优先取版目录，
  该目录的网 PDF 如不从 core 刷新，插仓时会带修前版。

## 4. zh-cn-en 版目录同步（同步工人，2026-11-12）—— §0b 遗留已清

`2026-w47-zh-cn-en/` 从 `core-zh-cn` 全量同步（纯复制，本目录未重建；
`insert.py` `resolve_bundle_dir` 优先取版目录，`find_web_pdf` 要求目录内
恰一个 `*web*.pdf`——同步后该目录的网 PDF 即 D5 版）。

- 同步前（版目录，修前）：印 `Lucerna-VOL4-EN.pdf`
  `c34f5a54e491a085ea3e19a986748938dda79294b90d154a8e746f54a9eb05aa`
  41,763,115 B；网 `Lucerna-VOL4-EN-web.pdf`
  `97e3082d90e214475637ae432712ce3393443e8e884063607ac2f857c0229aff`
  2,652,425 B；text.md `23fb62bd7763…bf04`（已与 core 一致）；
  svglib 修前 md5 `a6fd6f1d…`（无 `_D5_READER`）。
- 同步后（版目录 = core D5 版）：印 `f7b131533cda7e748f627016e0b76960de8e5e7300ea26831e3c005b8f551041`
  33,521,853 B；网 `7088ff0612976bb1eb354df995f2f647562b7508ece220bfc2c3abec0318ac7f`
  2,434,915 B；text.md `23fb62bd7763c59392c05ba7e03f64ad8f521352d464d6ac293d2190c4d0bf04`
  不变。核对：core 印/网/text SHA 与本日志 §1 一致才动手；同步后逐项核实——
  印/网/text SHA 与 core 相同，svglib 字节相同（md5 `35e83e68…da821`，
  `_D5_READER = "latin"`），`svg/` 8/8、`cards/` 8/8 字节相同，
  `ABSTRACT.txt`/`bslib4.py`/`run.py`/`assets/` 本就相同；目录内恰一个
  `*web*.pdf`；两 PDF 均为 8 页。
- 有意保留的差异（`diff -r --exclude=__pycache__` 仅剩这些）：① PDF 文件名
  ——版目录沿用 `-EN` 名（`Lucerna-VOL4-EN.pdf` / `-EN-web.pdf`，与 de/fr
  等版 `-DE`/`-FR` 惯例一致），内容 SHA 与 core 相同；② `content*.py` /
  `render.py` 仅差自指路径行（`OUT`/`BASE` 指本目录、印 PDF 用 `-EN` 名），
  内容相同，故未复制——复制 core 版会把本版构建指回 core 目录；③ KIT 为
  各版自述：`Files:` 现状行已更新为 D5 数值（与 core KIT 同行一致），文末
  追加 “D5 sync from core-zh-cn” 记录，2026-11-11 构建记录原文保留为历史；
  ④ `__pycache__/svglib` 陈旧 pyc 已删（svglib 换版后失效）。
- 抽查门禁（同步后目录，`tools/venv/bin/python`，日志 `/tmp/zhcn-en-sync-check/`）：
  spill 全量 RC=0（35 boxes，86 candidates，0 SPILL）；edge 全量 RC=0
  （8 页，0 TOUCH，0 NEAR）；`census_quotes.py` RC=0（0 缺陷）。交付物与
  core 全门禁 ALL-GREEN 的 D5 产物逐字节相同——可直接插仓。
- 未动：`core-zh-cn/` 只读；无 commit、无 push、无 lint --write；未碰其他版。
  df 同步后仍 93G（<100G 门限）。
