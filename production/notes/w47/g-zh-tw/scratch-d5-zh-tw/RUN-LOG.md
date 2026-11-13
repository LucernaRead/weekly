# D5 重建工作日志 — zh-tw 目标家庭（W47）

工人：D5 zh-tw 重建工人。开工 2026-11-12 ~03:10 EST。
范围：core-zh-tw（= zh-tw-en 版，slug 2026-w47-zh-tw-en，无独立目录）+ 9 fan-out：
zh-tw-de / -es / -fr / -it / -ja / -ko / -nl / -pt / -ru。
不建 zh-tw-en 目录，不建 zh-tw-zh-cn。
方法：裁定正本 CJK-DECISION.md（§1 字符分流、§3 KR 引号不扩展、§4 核心模板落盘）+
简报 brief-d5-rebuild.md；解释器一律 tools/venv/bin/python。
门禁：D5 census、occlusion、p8 compare --total 150、spill、boxtitle、edge、freeze
A-vs-B（对照=修前基线）、印/网文字层一致、head_check（HEAD TOO WIDE 即缺陷）、
creambox 审计、U+201C census_quotes（0 缺陷字）。
工作区：本目录；备份 `scratch-fanout-zh-tw/backup/<slug>/`；日志 `logs/<slug>/`。

## 接替记录（第二任工人，2026-11-12 ~04:31 EST）

上一任 e133a508 08:05 UTC 派出、约 1.5 小时后被运行时重启打断，resume 未能重启。接替时核实（生产 SHA vs 各版 `logs/<slug>/pdf-post.sha256` 逐版比对）：
- core-zh-tw / zh-tw-de / zh-tw-es：生产 SHA 与报告一致，stage2 ALL-GREEN，KIT 已同步——✅ 已完成，不重做。
- zh-tw-fr：stage2 已 ALL-GREEN（09:15 UTC），生产印 `384fd32e…` / 网 `64439f14…` 与 pdf-post 一致；**唯 KIT 未同步**——本任已补同步（PDFs 行 + STRADDLE FIXED 标注 + Build history D5 条目），见下。
- zh-tw-it：stage1 HAS-FAILURES，唯一缺陷 P2 boxtitle `耶誕城小檔　Scheda Christmasland` +23.5px（creambox PASS 0）；生产已是 D5 后 PDF（`99317d04…`），待修后 stage2。本任已改 content12.py:190 字号 25→22（文字不动），stage2 进行中。
- zh-tw-nl：仅 stage0 CLEAN（基线干净），生产未动（svglib 仍 pre-D5 md5 9caa4651…）。stage1 进行中。
- zh-tw-ja / -ko / -pt / -ru：未开工，无备份、无日志，生产未动。待 stage0→stage1→stage2。

## 进度总表（续）

| 版 | 基线 | 安装 | 门禁 | KIT | 状态 |
|---|---|---|---|---|---|
| core-zh-tw (=zh-tw-en) | CLEAN 8/8，TOTAL 150，D5 586 | patch-core latin | ALL-GREEN（两轮） | 已同步 | ✅ 完成 |
| 2026-w47-zh-tw-de | CLEAN 8/8，TOTAL 150，D5 618，基线 HTW×1（已修） | latin | ALL-GREEN（stage2） | 已同步 | ✅ 完成 |
| 2026-w47-zh-tw-es | CLEAN 8/8，TOTAL 150，D5 616，基线 0 HTW | latin | ALL-GREEN（stage2） | 已同步 | ✅ 完成 |
| 2026-w47-zh-tw-fr | CLEAN 8/8，TOTAL 150，D5 621，基线 0 HTW | latin | ALL-GREEN（stage2，09:15 UTC） | 已同步（本任补） | ✅ 完成 |
| 2026-w47-zh-tw-it | CLEAN 8/8，TOTAL 150，D5 605，基线 0 HTW | latin | ALL-GREEN（stage2；stage1 boxtitle 1 缺陷 P2 +23.5px，已改 25→22） | 已同步（本任） | ✅ 完成 |
| 2026-w47-zh-tw-nl | CLEAN 8/8，TOTAL 150，D5 607，基线 0 HTW | latin | ALL-GREEN（stage1 一轮，无修补） | 已同步（本任） | ✅ 完成 |
| 2026-w47-zh-tw-ja | CLEAN 8/8，TOTAL 150，D5 276，基线 0 HTW | cjk | ALL-GREEN（stage1 一轮，无修补） | 已同步（本任） | ✅ 完成 |
| 2026-w47-zh-tw-ko | CLEAN 8/8，TOTAL 150，D5 331，基线 0 HTW | cjk | ALL-GREEN（stage1 一轮，无修补） | 已同步（本任） | ✅ 完成 |
| 2026-w47-zh-tw-pt | CLEAN 8/8，TOTAL 150，D5 608，基线 0 HTW | latin | ALL-GREEN（stage2；stage1 boxtitle 3 缺陷，已改 25→21/23/21） | 已同步（本任） | ✅ 完成 |
| 2026-w47-zh-tw-ru | CLEAN 8/8，TOTAL 150，D5 拉丁 272+西里尔 480，基线 0 HTW | ru | ALL-GREEN（stage2；stage1 boxtitle 4 + occlusion 7 + edge 1 TOUCH + creambox 4，已改 4 标题 25→21/19/20/22 + content7.py 两处 sans 降字号） | 已同步（本任） | ✅ 完成 |
| 2026-w47-zh-tw-it | | | | | |
| 2026-w47-zh-tw-ja | | | | | |
| 2026-w47-zh-tw-ko | | | | | |
| 2026-w47-zh-tw-nl | | | | | |
| 2026-w47-zh-tw-pt | | | | | |
| 2026-w47-zh-tw-ru | | | | | |

## 逐版记录

### core-zh-tw
- 基线（2026-11-12 08:12 UTC）：备份 `scratch-fanout-zh-tw/backup/core-zh-tw/`；svglib pre-D5 md5 `9caa4651959673f511cd56873d93a04a`；印 PDF `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a`（19,420,552 B，与 KIT fix5 记录一致）；网 PDF `ffea9ab9dd8f2374217c5abe98323a781e222a0dbf74d1337bd127cb6f33c164`（2,324,046 B——与 KIT 登记的 1c0799ac/2,324,042 B 差 4 字节，系 webpdf 每次重跑 SHA 浮动，见 KIT 注）；text.md `09e083e1…`（49,798 B，与 KIT 一致）；重建 8/8 字节一致，TOTAL 150，0/0；普查 D5 拉丁 586、西里尔 0、弯引号 CJK 0；引号普查 0 缺陷字；印/网文字层各 23,960 字符一致。
- 安装：`apply_variant.py --patch-core zh-tw --i-understand-this-writes-production`（须显式确认旗标；不带旗标的 --check 被拒 RC=1，系脚本防护、已修脚本后不再出现）；`_D5_READER = "latin"`；fix2 块随装。
- 门禁（stage1 + stage2 两轮全绿）：run TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；head_check 0；occlusion 0（自检 6 类全触发）；p8 extract 150/150、compare vs 修前基线 CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 基线新增 CJK 0（新增拉丁 strings 243，run 拆分）；spill 0（131 OBSERVE）；boxtitle 0 DEFECT（48 titles）；edge 0/0；creambox PASS 0 defects（n=523，median 1.007，bold 1.040）；D5 普查 PASS（0/0/0）；引号普查 0 缺陷字；textcheck PASS（印/网/修前各 23,960 字符）；text.md 逐字节相同；P8 123→123 行、余量 37.3→37.3px。内容零改动。
- 交付：印 `Lucerna-VOL4.pdf` 11,194,932 B，SHA-256 `332ed38d5cd20b125f5246055c987743f1081c1b72d49b165dabf23044a6e3c8`（两轮 SHA 相同）；网 `Lucerna-VOL4-web.pdf` 1,897,929 B，SHA-256 `8fa6efdf1bdcf0c187c988b0d32c5dbdcca6438a3a977729231467d8316b30b8`。
- KIT 已同步（§Measured totals PDFs 行 + Build history D5 条目）。清理：freeze/build-copy 已删、备份 PDF 已删（留 svg/ + 源码 + 基线记录）。
- 脚本修正两则：(1) `cp -a` 保所有权失败（源文件属 root）→ 改 `cp -r`；(2) zh-tw 文件名是 `-web.pdf` 而非 en 版 `.web.pdf`——PRINTPDF 的 grep 排除与 WEBPDF 拼接均已改 `-web.pdf`；(3) head_check 门禁口径：以修后 run.log 为门（须 0），基线 log 另行扫描记档（修前已有的 HTW 记为“已修”，不计入 D5）。

### 2026-w47-zh-tw-de
- 基线（08:28 UTC）：备份已拷；svglib pre-D5 md5 `9caa4651959673f511cd56873d93a04a`（与 core 相同）；印 PDF `da4af743994c0c238549d6d87bc4fe95822b3215893988f8683ab4bf2402068e`（21,717,594 B）；网 PDF `542051ea82eee8a577d69976f93e2ca233cdd4fc7be3f028290a9ec310acbdfd`（2,452,925 B）；text.md `85584db9…`；重建 8/8 字节一致，TOTAL 150；普查 D5 拉丁 618、西里尔 0、弯引号 CJK 0；引号普查 0 缺陷字；印/网文字层各 25,858 字符一致。
- 修前缺陷（非 D5 引起）：基线 run.log 有 HEAD TOO WIDE ×1——P8-ex `D　讀一讀，答一答　Lesen und antworten`（content8.py:72，21pt）。实测：修前 423.1 vs 栏宽 422.5（超 0.6px），D5 后 424.2（超 1.7px）。已修：字号 21→20（实测 404.0，余 18.5px），文字不动。修后 run.log 0 HEAD TOO WIDE。
- 安装：`--target zh-tw --reader de`（mode latin），与 core 同批改动；stage1 进行中。
- 缺陷 5 项（stage1，boxtitle 4 + creambox 3，同一组标题；另 P8 电池头 1 项见上）：4 个 25pt 手绘奶油框标题越框右缘——**修前已溢出**，D5 各加重约 +6px：P2 `耶誕城小檔　Christmasland-Steckbrief` +64.5→+70.5px（content12.py:190，25→20，余 26.5px）；P3 `金馬小表　Golden-Horse-Steckbrief` +30.5→+35.5px（content34.py:76，25→22，余 20.1px）；P3 `鋼雕閉幕行程　Letztes Wochenende` +28.5→+26.5px（boxtitle 判；content34.py:93，25→22，余 24.5px）；P5 `迪士尼聖誕小檔　Disney-Steckbrief` +18.5→+24.5px（content56.py:81，25→22，余 29.6px）。文字一字未动。
- stage2 终轮全绿：run TOTAL 150、0/0；head_check（修后）0；occlusion 0；p8 extract 150/150、compare vs core-zh-tw CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 基线新增 CJK 0；spill 0（140 OBSERVE）；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0 defects（n=546，median 1.008，bold 1.040）；D5 普查 PASS；引号普查 0 缺陷字；textcheck PASS（印/网/修前各 25,858 字符）；text.md 逐字节相同；P8 158→160 行、余量 35.7→36.7px。
- 交付：印 `Lucerna-VOL4-DE.pdf` 11,195,908 B，SHA-256 `1b1f0f0370c1ffb945f8c329c9f29250f96d710253bd562839e53cc672ae05b0`；网 `Lucerna-VOL4-DE-web.pdf` 1,903,427 B，SHA-256 `f430e390f4958cabf98e1034e6a28c564f8b9788f70e8dc6dc50a9e4d16e47ef`。
- KIT 已同步（PDFs 行 + Known non-defects P8 D-head 标注已修 + Build history D5 条目）。清理：freeze/build-copy 已删、备份 PDF 已删。

### 2026-w47-zh-tw-es
- 基线（08:41 UTC）：备份已拷；svglib pre-D5 md5 `9caa4651959673f511cd56873d93a04a`；印 PDF `e32c58c489ebb9a79e2d9c6029c3c0c23931c8bcbaea631144489daef3454a2c`（23,256,381 B）；网 PDF `a1f8af0d1c788b51be8c0cd083e325a360387e98130b7c5e63c9f24d89f10849`（2,529,736 B）；text.md `59439c7d…`；重建 8/8 字节一致，TOTAL 150，0/0；普查 D5 拉丁 616、西里尔 0、弯引号 CJK 0；引号普查 0 缺陷字；印/网文字层各 25,773 字符一致。基线 0 HEAD TOO WIDE。
- 安装：`--target zh-tw --reader es`（mode latin）；stage1 门禁除 boxtitle 外全绿（occlusion 0、p8 150/150 CLEAN、freeze 8/8、新增 CJK 0、spill 0、edge 0/0、creambox PASS 0、普查 PASS、引号 0、textcheck PASS、text.md 相同；P8 144→144 行、余量 36.3→36.3px）。
- 缺陷 4 项（boxtitle；creambox 0——修后越框 ≤ 修前越框，无新增回归）：4 个 25pt 手绘奶油框标题越框右缘，**修前已溢出**：P2 `耶誕城小檔　Ficha de Christmasland` +36.5→+38.5px（content12.py:190，25→21，余 32.1px）；P3 `金馬小表　Ficha de los Golden Horse` +40.5→+39.5px（content34.py:76，25→21，余 30.5px）；P3 `鋼雕閉幕行程　Último fin de semana` +36.5→+33.5px（content34.py:93，25→22，余 19.0px）；P5 `爵士音樂節時間表　Fechas del jazz` +7.5→+3.5px（content56.py:110，25→23，余 29.2px）。文字一字未动。stage2 终轮全绿：run TOTAL 150、0/0；head_check 0；occlusion 0；p8 extract 150/150、compare vs core-zh-tw CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 基线新增 CJK 0；spill 0（146 OBSERVE）；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0 defects（n=541，median 1.001，bold 1.040）；D5 普查 PASS；引号普查 0 缺陷字；textcheck PASS（印/网/修前各 25,773 字符）；text.md 逐字节相同；P8 144→144 行、余量 36.3→36.3px。
- 交付：印 `Lucerna-VOL4-ES.pdf` 11,193,961 B，SHA-256 `e9d3ac05473f56d64ad5de9eda671fb39097a3cebb2ba9b8865d06b7706a6d3c`；网 `Lucerna-VOL4-ES-web.pdf` 1,902,094 B，SHA-256 `2ec0065257c1cbded0f97a7b4d2c0363057fd9665c4669f1e5f673b1c8720622`。
- KIT 已同步（PDFs 行 + Re-fan-out 节 STRADDLE 标注已修 + Build history D5 条目）。清理：freeze/build-copy 已删、备份 PDF 已删。

### 2026-w47-zh-tw-fr
- 基线（08:52 UTC）：备份已拷；svglib pre-D5 md5 `9caa4651959673f511cd56873d93a04a`；印 PDF `acd1d85b2af073100140a8bfd5936faeecc8a050f42226a424066aefce1aaf33`（20,191,919 B）；网 PDF `cac6ab5bfe82fb10bf32cabfaee5be3f297441b1f75db880e1a841b0ae2ab2f2`（2,366,341 B）；text.md `673943a0…`；重建 8/8 字节一致，TOTAL 150，0/0；普查 D5 拉丁 621、西里尔 0、弯引号 CJK 0；引号普查 0 缺陷字；印/网文字层各 25,767 字符一致。基线 0 HEAD TOO WIDE。
- 安装：`--target zh-tw --reader fr`（mode latin）；stage1 除 boxtitle/creambox 各 1 处外全绿（occlusion 0、p8 150/150 CLEAN、freeze 8/8、新增 CJK 0、spill 0、edge 0/0、普查 PASS、引号 0、textcheck PASS、text.md 相同；P8 152→152 行、余量 36.3→35.3px）。
- 缺陷 1 项（boxtitle + creambox 一致）：P2 `耶誕城小檔　Fiche Christmasland` 越框右缘 +2.5px——**纯 D5 引起**（修前基线无溢出；creambox_abs_base 无此条）。content12.py:190 字号 25→23，余 29.5px。文字一字未动。stage2 重门禁进行中。

### 2026-w47-zh-tw-it
- 基线（09:03 UTC）：备份已拷；svglib pre-D5 md5 `9caa4651959673f511cd56873d93a04a`；印 PDF `5594005aae1b2ff3b69ae37edf191dc482f2c3773b29a1cdc75c72ce5b485ce9`（19,420,437 B）；网 PDF `83a57fb094d5f961b5a3ee4899abc065e78f2968b826d94e511f3ab4077275f5`（2,323,037 B）；text.md `48e04f15…`；重建 8/8 字节一致，TOTAL 150，0/0；普查 D5 拉丁 605、西里尔 0、弯引号 CJK 0；引号普查 0 缺陷字；印/网文字层各 25,577 字符一致。基线 0 HEAD TOO WIDE。
- 安装：`--target zh-tw --reader it`（mode latin）；stage1 进行中。

## 本任完成记录（第二任工人，2026-11-12 ~04:31–05:15 EST）

### 2026-w47-zh-tw-fr（KIT 补同步）
- 上一任 stage2 已 ALL-GREEN（09:15 UTC），生产印 `384fd32e…` / 网 `64439f14…` 与 pdf-post 一致；本任只补 KIT 同步（PDFs 行 + STRADDLE FIXED 标注 + Build history D5 条目）。交付：印 11,191,465 B / 384fd32e70c8d50f38f9df384c99c352d8b38cf20a59c4ec819a10d2e8d90b99，网 1,899,091 B / 64439f145ccecabaac6ad6fe5f7f49e03ec7352d96b8df86a0452deb3e20e83d。门禁见上一任 stage2（creambox n=546，P8 152→152、余量 36.3→35.3px）。

### 2026-w47-zh-tw-it（修 1 缺陷后 stage2 全绿）
- stage1 唯一缺陷 P2 boxtitle `耶誕城小檔　Scheda Christmasland` +23.5px；content12.py:190 字号 25→22（文字不动）。stage2 全绿：run TOTAL 150、0/0；head_check 0；occlusion 0；p8 150/150 CLEAN keydiff=[]；freeze 8/8、新增 CJK 0（拉丁 strings 241）；spill 0（143 OBSERVE）；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0（n=532，median 1.005，bold 1.040）；D5 普查 PASS；引号 0；textcheck PASS（25,577 字符）；text.md 逐字节相同（48e04f15…）；P8 150→150、余量 50.3→50.3px。
- 交付：印 11,187,632 B / b4a3fdfc5868342e30bab53608eccd04138140b360e5b7d9baa8d54f46c5003b，网 1,895,530 B / 39898950b0d02ccf088ea5d4fe0dc98401322d7e5292ae8a60dd8867f845c3ef。KIT 已同步。

### 2026-w47-zh-tw-nl（stage1 一轮全绿）
- stage0 CLEAN（上一任已做）。stage1 一轮全绿，无修补：run TOTAL 150、0/0；head_check 0；occlusion 0；p8 150/150 CLEAN；freeze 8/8、新增 CJK 0（拉丁 250）；spill 0（134 OBSERVE）；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0（n=535，median 1.003，bold 1.040）；D5 普查 PASS；引号 0；textcheck PASS（24,793 字符）；text.md 逐字节相同（a3662561…）；P8 158→158、余量 36.3→36.3px。
- 交付：印 11,189,525 B / 1e24a8deb37bfcba3ef7ac6cff92f26a21a545b7533dc3de1fa9557e3d265f0b，网 1,898,551 B / 9461e8bad39b96c04dd34d57453fc2bbbc5d6f1faf46535c58489a92b44d56d5。KIT 已同步。

### 2026-w47-zh-tw-ja（stage0+stage1，cjk，一轮全绿）
- 基线 CLEAN 8/8，TOTAL 150，D5 拉丁 276，基线 0 HTW。安装 mode=cjk（`_D5_READER = "cjk"`；CJK index TC→JP，kinsoku 已在版内 skip port）。stage1 一轮全绿，无修补：run TOTAL 150、0/0；head_check 0；occlusion 0；p8 150/150 CLEAN；freeze 8/8、新增 CJK 0（拉丁 155）；spill 0（146 OBSERVE）；boxtitle 0 DEFECT（25 titles）；edge 0/0；creambox PASS 0（n=506，median 1.006，bold 1.040）；D5 普查 PASS；引号 0；textcheck PASS（18,668 字符）；text.md 逐字节相同（e03a56ad…）；P8 126→126、余量 50.3→50.3px。
- 交付：印 16,365,732 B / 1f61f431d75eb60ceb7d130f9e1f8498a812a1f0352d4cba6e50100955f81efc，网 2,447,140 B / 94b53a518bb0954494ef414b57ddbc678e173450d3c91d39ff0deeb8122d968c。KIT 已同步。

### 2026-w47-zh-tw-ko（stage0+stage1，cjk，一轮全绿）
- 基线 CLEAN 8/8，TOTAL 150，D5 拉丁 331，基线 0 HTW。安装 mode=cjk（CJK index TC→KR）。stage1 一轮全绿，无修补：run TOTAL 150、0/0；head_check 0；occlusion 0；p8 150/150 CLEAN；freeze 8/8、新增 CJK 0（拉丁 234）；spill 0（188 OBSERVE）；boxtitle 0 DEFECT（56 titles）；edge 0/0；creambox PASS 0（n=501，median 1.005，bold 1.040）；D5 普查 PASS；引号 0；textcheck PASS（19,169 字符）；text.md 逐字节相同（a44ba8cb…）；P8 119→119、余量 50.8→50.8px。
- 交付：印 12,718,866 B / 0fe4589f6fe80bc856aaa89eb536e5a4a5f67d65bb90e788048a63bf14798884，网 2,134,058 B / e298e577bf0b0ef8ff410dd7b26ce298562823ab713289a653c6a3d2fb7de443。KIT 已同步。

### 2026-w47-zh-tw-pt（修 3 缺陷后 stage2 全绿）
- 基线 CLEAN 8/8，TOTAL 150，D5 拉丁 608，基线 0 HTW。stage1 除 boxtitle 外全绿（creambox PASS 0）：3 处 25pt 奶油框标题越框——P2 `耶誕城小檔　Ficha do Christmasland` +39.5px（content12.py:190，25→21，余 30.9px）、P3 `金馬小表　Ficha dos Golden Horse` +12.5px（content34.py:76，25→23，余 20.6px）、P3 `鋼雕閉幕行程　Último fim de semana` +40.5px（content34.py:93，25→21，余 30.0px）。字号按实测 text_w 选定，文字一字未动。stage2 全绿：run TOTAL 150、0/0；head_check 0；occlusion 0；p8 150/150 CLEAN；freeze 8/8、新增 CJK 0（拉丁 266）；spill 0（144 OBSERVE）；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0（n=536，median 1.000，bold 1.040）；D5 普查 PASS；引号 0；textcheck PASS（24,949 字符）；text.md 逐字节相同（02387ce2…）；P8 126→126、余量 36.3→35.3px。
- 交付：印 11,197,823 B / b036790928ced2c1d9c1fb730c6e631ebdf69f5d9ae809bcb1c4d60eed19a33b，网 1,906,989 B / ad03afe2ccb9e1f4a72e8e92a15945665010ebe0922458df50548391231c6d8e。KIT 已同步。

### 2026-w47-zh-tw-ru（修 5 缺陷后 stage2 全绿）
- 基线 CLEAN 8/8，TOTAL 150，D5 拉丁 272 + 西里尔 480，基线 0 HTW。安装 mode=ru（`_D5_READER = "ru"`；fix2 已在版内，installer 未重复装；Noto Sans 元素 1014，ru 路由真实触发）。stage1 失败 4 门：boxtitle 4 缺陷、occlusion 7 flags、edge 1 TOUCH 1 NEAR、creambox 4 缺陷；其余全绿。
- 缺陷与修法（字号按实测 text_w 选定，文字一字未动）：P2 `耶誕城小檔　Крисмасленд: коротко` +45.5px（content12.py:190，25→21，余 25.8px）；P3 `金馬小表　«Золотая лошадь»: коротко` +90.5px、墨水越过页缘（content34.py:76，25→19，余 27.3px；occlusion EDGE 与 edge P3 TOUCH 为同一处）；P3 `鋼雕閉幕行程　Последние выходные` +60.5px（content34.py:93，25→20，余 31.7px）；P5 `迪士尼聖誕小檔　Дисней: коротко` +18.5px（content56.py:81，25→22，余 31.7px）。P7 下期预告越页脚线：D5 后俄文 sans 常规变宽（中位 +3.4%），col3 1823.3→1878.2（+54.9px = 诊所俄文 gloss 1→2 行 +26.52 + 读者园地披露俄文 7→8 行 +28.4），预告盒底 2577.3→2632.2、文字 baseline 2598.22 越过页脚线 2596（修前备份 occlusion 0 flags，确为 D5 引起）；content7.py 诊所俄文 sans 19.5→19（公式与绘制两处）、披露俄文 sans 20→19（公式与绘制两处），实测恢复基线行数，col3/teaser 精确回到 1823.3/2577.3。
- stage2 全绿：run TOTAL 150、0/0；head_check 0；occlusion 0 flags；p8 150/150 CLEAN；freeze 8/8、新增 CJK 0（拉丁 55）；spill 0（146 OBSERVE）；boxtitle 0 DEFECT；edge 0 TOUCH 0 NEAR；creambox PASS 0（n=557，median 1.029，bold 0.956——西里尔粗体反变窄）；D5 普查 PASS（0/0/0）；引号普查 0 缺陷字（弯引号 5 个全在 Newsreader）；textcheck PASS（24,960 字符）；text.md 逐字节相同（2fb4b97e…）；P8 174→172、余量 38.7→35.7px。
- 交付：印 11,366,251 B / d80b9ee5df60b982eb1ae4fffe026a0cc33703292f589765b5776baa7a6af524，网 2,070,745 B / d255e31ad059a2c4f1595d75b99aba3f140faa2b1fcc138d2b55a0fa80865610。KIT 已同步。

## 清理
- 各版 freeze build-copy（可复现的重建副本）已删；logs 202M→12M。备份 `scratch-fanout-zh-tw/backup/<slug>/`（修前基线记录）保留。磁盘 93G 已用 / 57G 可用，未触 100G 门限。
