# FANOUT-REPORT — W47 zh-tw 重 fan-out（9 版）

- 任务：从已定稿 core-zh-tw 重建 9 个母语版（de / fr / es / it / pt / nl / ru / ja / ko）。**不 commit、不 push、不派 subagent。**
- 执行：2026-11-11 ~10:37–12:05 UTC（重 fan-out rod）。工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-refanout-zh-tw/`（本报告、全部日志、门结果、旧版备份均在此；只写 goals 侧，未写进 repo 的 `hidden_files/w47/`）。
- 结论：**9/9 建成，全部正门通过。** 未决项见 §7（英文源 key 未改；双语小檔标题 STRADDLE 为旧版既有属性，已如实披露，待协调员派 fix1 定夺）。
- 探针：`git hash-object -w` rc=0，scratch 真实写文件 rc=0。`TMPDIR=<scratch>/tmp`，未写 /tmp。磁盘：/home/hatch 150G，约 72–75G 空闲，无 quota 报错。

## §0 核心基线（已定稿，不动；重建前后 SHA 复核未变）

`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`：

| 件 | 字节 | SHA-256 |
|---|---|---|
| 印刷 `Lucerna-VOL4.pdf` | 19,420,552 | `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a` |
| 网页 `Lucerna-VOL4-web.pdf` | 2,324,042 | `1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240` |
| text.md `2026-w47-zh-tw-en.text.md` | 49,798 | `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b` |

核心状态：re-proof #3（`scratch-reproof-core-zh-tw3/PROOF-NOTE.md`，2026-11-11 10:24–10:40 UTC）结论 **(a) zero issues，定稿**。已入核的 fix4/fix5：`content7.py:18` M1「終點 (end point)」、`content7.py:52` 记忆口诀新句（红毯 17:00 在典礼 18:30 之前）、`content12.py:68`「本週日 11/22 遊行、金馬獎、鋼雕閉幕、夜間遊行」、`content56.py:131`「——四件事只能取捨」、fix2 BABYMONSTER 行删除 + HK box 480→418、by4 498→436、D4 box 230→244。core-zh-tw 本身就是 zh-cn 读者版，**不在 9 版内，也绝未建 zh-cn × zh-tw 对版目录**。

## §1 机制表核对（`scratch-fanout-zh-tw/tables.py`，242 ENTRIES）

先核表再动手；只改机制表，不改核心。补丁执行记录：

| # | 核对项 | 结果 | 行号与值 |
|---|---|---|---|
| ① | nl :273「Volgende zondag」→「Deze zondag」相当表述 | **本轮补** | `tables.py:273`（ENTRIES[22] nl，P2 小雪 gloss）：「Deze zondag, 22 nov., is het Xiaoxue (Kleine Sneeuw), de 20e zonneterm en de tweede van de winter…」；同批补丁共 16 处值编辑（L246–250、L268–273、L323–327，每处断言 count==1；`ast.parse` 通过；与备份 diff 恰 16 行）。备份：`scratch-refanout-zh-tw/tables.py.bak-pre-refanout`（SHA `6ced04023c18eb5e37845f05bc1042b57effa9d64a3e73c4f77b3d0a2c5fbd71`）。 |
| ② | M1「end point」8 语 sweep（源已为 `(end point)`，无「finish line」key 残留） | **已在表内，零新增** | ENTRIES[200]（L2108–2116 附近）：de Ziellinie、fr ligne d'arrivée、es meta、it traguardo、pt linha de chegada、nl finish、ru финиш、ja ゴール；ko 已做（끝나는 곳）。逐个核对 8 语值齐全。 |
| ③ | M2 记忆口诀 7 语值（顺序：入圍 → 星光大道（红毯 17:00，典礼前）→ 典礼（頒獎）18:30；不得出现 "place" 类措辞） | **已在表内，零新增** | ENTRIES[206]（L289–298）：9 语值顺序与时间齐全（17:00 + 18:30 全 9 语有；ja 时间已修；place 类词 0）。历史：rekey 轮修 de/es/it/pt/nl/ru/ja 值；ja-time 轮补 ja 时间。 |
| ④ | D1「this Sunday」6 语 sweep（de/fr/es/it/pt/ja 的「下周日」表述 →「本周日」；nl 在 ① 中；ru 已对） | **本轮补 15 值** | de「nächsten Sonntag」→「diesen Sonntag」×3（ENTRIES[20]/[22]/[27]，L246、L323 及另一处）；fr「dimanche prochain」→「ce dimanche」×3（L247、L324…）；es「el próximo domingo」→「este domingo」×3（L248、L325…）；it「domenica prossima」→「questa domenica」×3（L249、L326…）；pt「o próximo domingo」→「este domingo」×2 +「No próximo domingo」→「Neste domingo」（L250、L272、L327）。补后全表 grep：0 残留 next-Sunday 表述。ja 今週の日曜日 ×3、ko 이번 주 일요일 ×3、ru это воскресенье ×3 已对（零改）；nl parade ×2 中性表述「op zondag 22 nov.」已对。 |
| ④-英 | 英文源 key :245/:267/:322 →「this Sunday」 | **未执行（有意）— 见 §7 未决项 1** | `tables.py:245/:267/:322` 仍为「next Sunday」/「Next Sunday」，因为冻结核心 `content12.py:37/:113`、`content34.py:127` 仍为「next Sunday」，且 re-proof #3 结论 (a) 认证了该核心（含保留「next Sunday」）。只改机制表、不改核心是任务原话；不同步改核心而改 key 会导致 transform 在 9 版全部 loud fail（`expect_min=1`）。若协调员要改英文，须先做核心 fix。 |

核对方法：先在沙箱跑 transform 烟囱测试（9/9 TRANSFORM OK；D1 旧表述 0；nl「Deze zondag」落位；M1 各语值落位；M2 17:00+18:30 全 9 语有、place 词 0），再跑真实 transform。

## §2 备份与 transform

- **备份（未删）：** 9 个旧版目录完整 `cp -a` 到 `scratch-refanout-zh-tw/backup/2026-w47-zh-tw-{de,fr,es,it,pt,nl,ru,ja,ko}/`，共 290M，每版 41 文件；逐版文件清单 SHA-256 与 production 原版逐一比对一致（BACKUP-VERIFIED）。`cp -a` 的 ownership 警告仅为外观。
- **transform（one-shot）：** 删旧版目录后重建，**9/9 TRANSFORM-OK**（2026-11-11 ~10:43 UTC）。旧 `transform-*.log` 已保存到 `scratch-refanout-zh-tw/transform-logs-old/`。copytree 带来的 3 个过期核心文件（`Lucerna-VOL4.pdf`、`Lucerna-VOL4-web.pdf`、`2026-w47-zh-tw-en.text.md`）逐版 SHA 核对与核心一致后删除。
- 机制表/transform 副本放在本 scratch 内运行，日志落本 scratch。

## §3 手修重应用清单（逐版 diff 新版 vs 备份旧版：content12/34/56/7/8.py + bslib4.py + render.py；diff 文件存 `scratch-refanout-zh-tw/diff-new-vs-old-<lang>-<file>.txt`）

- bslib4.py / render.py：9 版全部 0 diff。
- 其余全部 hunk 均已由核心或机制表承载，无一丢失：
  - 核心平行：D1 中文 下週日→本週日（11 处）、fix2 HK box/BABYMONSTER/取捨、fix5 D4 box 230→244、N4 小雪→夜間遊行、ko M3「參考:→參考｜」。
  - 表驱动 fix1：M1/M2、D1 各语值、N2 P8 notes、ru N5/N6/N7、ja D-ja-2、ko M4/M5、it D3。
  - P6/P8 标题缩短已在表中（fr「Lire la frise」/「Quiz de lecture」、it「Quiz di lettura」、pt「Quiz de leitura」、ru 4 标题 + P8 标题「Ответы — по страницам…」`tables.py:2397`、de P8 D-head「Lesen und antworten」不变）。
  - ja Disney 48 天注（content56.py:20/:31）新旧一致，仅 :60 D-ja-2 不同，无丢失。
- **唯一仅存于旧版文件的手修：de P7 teaser bar 118→104px**（旧 de `content7.py:139,142`；其余 de P7 缩短均已镜像进表，col3 终值与旧版终值一致）。重建后重测 de P7 几何并重压，见 §4 de 行。

| 来源 FIX-LOG | 手修 | 重应用验证 |
|---|---|---|
| ru fix1（`scratch-fix-zh-tw-ru1/FIX-LOG.md`） | N1/N6/N7/D1-ru + N2 新增 4 ENTRIES | 表中已含；新版 ru run 首轮即 P7 1823.3/2577.3（旧首轮曾 1968.0/2722.0），零警告 |
| ja fix1（`scratch-fix-zh-tw-ja1`） | D-ja-2 + D1-ja、M2 ja 草稿 | 表中已含；新版 ja 内容 diff 仅 :60 D-ja-2 一处 |
| ko fix1（`scratch-fix-zh-tw-ko1`） | M1/M2 源重键 + ko 值、M3/M4/M5、D1-ko | 表中已含；新版 ko 首轮零警告 |
| rekey（`scratch-rekey-zh-tw-memory`） | M2 7 语值修 | 表中已含；§1③ 核对通过 |
| ja-time（`scratch-fix-zh-tw-ja-time`） | ja M2 加时间 | 表中已含；M2 ja 值含 17:00/18:30 |
| de fan-out 旧版（`content7.py:139,142`） | P7 teaser 118→104px | 重测重压，见 §4 |

## §4 逐版构建（每版：run.py → render.py → webpdf.py → export_zhtw_textmd.py；全部 rc=0）

run.py 标准总值（9 版一致）：150 题；分级 A2 44 / B1 74 / B2 32；分页 10/18/18/18/18/18/12/38；类型 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1；0 FLOW OVERFLOW。

| 版 | run.py | P7 col3 ends | P7 teaser ends | 备注 |
|---|---|---|---|---|
| de | run2 rc=0（run1 118px bar 时 teaser 2603.82，超页脚规则 2596 达 7.82px） | 1849.82 | 2589.82（余 6.18px） | **teaser 重压**：按备份旧 de `content7.py` 同两行，`p.rect(..., 118→104)` + `print("P7 teaser ends", py + 118→104)`；重跑后 col3 1849.82 不变，teaser 2589.82。唯一警告：已知 P8 D-head HEAD TOO WIDE（+0.58px，见 §7）。 |
| fr | rc=0，零警告 | 1823.3 | 2577.3（余 18.7px） | 与旧版终值完全一致 |
| es | rc=0，零警告 | 1823.3 | 2577.3 | 与旧版终值一致 |
| it | rc=0，零警告 | 1823.3 | 2577.3 | 与旧版终值一致 |
| pt | rc=0，零警告 | 1823.3 | 2577.3 | **中途恢复**：运行时 VM 重启，render 已完成（印刷 PDF 已落盘 20,944,900 B），webpdf 中断、export 未跑；核对磁盘后仅重跑 webpdf + export（幂等），三件齐。 |
| nl | rc=0，零警告 | 1823.3 | 2577.3 | 与旧版终值一致 |
| ru | rc=0，零警告 | 1823.3 | 2577.3 | 旧首轮曾 1968.0/2722.0；表内 fix1 值使重建首轮即终值 |
| ja | rc=0，零警告 | 1827.28 | 2581.28（余 14.7px） | run 日志无 SIMP_ONLY 行；checks.py 的 SIMP_ONLY 在门阶段见 §6 |
| ko | rc=0，零警告 | 1821.42 | 2575.42（余 20.6px） | 与旧版终值一致 |

P7 三栏 Flow 终值（run 日志，nominal bottom 1560）：de A2 1343 / B1 **1602** / B2 1535（B1 较旧版 1568 长 34px——核心 fix4/fix5 加长了 P7 B1 内容；下一元素 phrases strip 距 258px，occlusion 0，目视干净；已记入 de KIT 已知非缺陷）；fr 1377/1602/1535；es 1343/1568/1535；it 1343/1568/1535；pt 1377/1568/1535；nl 1343/1535/1501；ru 1410/1657/1535；ja 1310/1535/1442；ko 1343/1475/1409。P7 工具盒实测清除量（canonical creambox，3 盒）：全 9 版 +40.5 / +12.5 / +14.0（ja 第二盒 +12.4）；P7 最小内清除量 12.5px（ja 12.4px）。

## §5 九版三件 SHA（印刷 PDF / 网页 PDF / text.md；全部 8 页、1462.5×2025 pt）

| 版 | 印刷字节 | 印刷 SHA-256 | 网页字节 | 网页 SHA-256 | text.md 字节 | text.md SHA-256 |
|---|---|---|---|---|---|---|
| de | 21,717,594 | `da4af743994c0c238549d6d87bc4fe95822b3215893988f8683ab4bf2402068e` | 2,452,914 | `de3a7594c2380e9f40e98bde23f4b163d365198a13ed6752bf6c5297b3111fd9` | 51,814 | `85584db99a9e2aa8685751d2ff385749cde5d78aca1c96cbefce845af54232fb` |
| fr | 20,191,919 | `acd1d85b2af073100140a8bfd5936faeecc8a050f42226a424066aefce1aaf33` | 2,366,339 | `6026be3ed418a8bd9574bfea2fd154ec7bc727d600b0eded0cff2b91a4070246` | 52,470 | `673943a0de31811ee43d899390a40fdde1c564ae7176f61878f77e1c687fa613` |
| es | 23,256,381 | `e32c58c489ebb9a79e2d9c6029c3c0c23931c8bcbaea631144489daef3454a2c` | 2,529,735 | `fb90e8270f4bfba8a517c8f81a95dc3814b0d3fd0fa5287d12aceb76767e5b6e` | 52,246 | `59439c7db9e176b8bb6138fafde56e0ee6f720460659a0277d2ed8c42bffc778` |
| it | 19,420,437 | `5594005aae1b2ff3b69ae37edf191dc482f2c3773b29a1cdc75c72ce5b485ce9` | 2,323,037 | `a0d80c26bdc7c8eb6029af991c4d14e8af966f0e3f6d3a066f74f98bf220d0a5` | 51,685 | `48e04f1540a9b6bcf292f9163af32707ac2ba54bcd91b18a127f45903dc12ba7` |
| pt | 20,944,900 | `6302ea7c3cb5ba6d8bc7069a9bb69d0458da46f93bcad4462019c2320ff1b5d5` | 2,412,857 | `4a257e9f33a988e88735e7c396ca73dfe9d3029b51ec21052bb698ef907804d3` | 51,492 | `02387ce2dd5e9b7b0fa1d21ce35334f16a3e398d4e7dd73388645f6e174aafb2` |
| nl | 20,939,172 | `730e15c9e70631a990d021e16e11f80de018683219c3beba08c897abf90c8832` | 2,409,973 | `1c8dc05ba68db691cd54569b3161f6310959578d952cbb062e34353a25c867c3` | 50,596 | `a3662561fff3e167b98bc8b4006ead5fe2166b56bed8ebe5e7c67105bb6ac0a5` |
| ru | 12,896,218 | `1dbe1d8ec96fe91eeccb8b2a2f92080dd83c1302d85aed555e2e4e255224eeee` | 2,007,900 | `cb05eba2e641e3a200fff8d58648092788f08fca70f1d0ab8736ac76cfb50d52` | 62,492 | `2fb4b97ef37d490e834dbef5c9553fb476c209222f061f7a17c4274e882ae03b` |
| ja | 18,089,964 | `73f623f8884296f8d23aa54e16b46bc10a40c22df24908047478a975fdd58ef8` | 2,562,627 | `b5cd6ad09008846450d662aa3e1c8b0fcd1eb0ddec099d281a6f068e36042eed` | 53,753 | `e03a56ad7254ea135f4bf6c344e6e3e798acc06a9c6452209d2b0510324e5e63` |
| ko | 16,838,018 | `75610665146d9903c5144148f799386d2ed928f11264e2a8697cb24429c307f0` | 2,325,041 | `140f83acdba99fba9b67ec26f8e1418d85a2e5aa9f791d3f16238265c67bb282` | 53,922 | `2e7038cc4c1266146824db80b1a20f87f83593b69f3e8bd755596b435e6986a8` |

- text.md H1（与旧版一致）：de「VOL.4 · Chinesischer Text (traditionell) · Erklärungen auf Deutsch」；fr「VOL.4 · Textes en chinois traditionnel · Explications en français」；es「VOL.4 · Textos en chino tradicional · Explicaciones en español」；it「VOL.4 · Testi in cinese tradizionale · Spiegazioni in italiano」；pt「VOL.4 · Textos em chinês tradicional · Explicações em português」；nl「VOL.4 · Teksten in het Chinees (traditioneel) · Uitleg in het Nederlands」；ru「VOL.4 · Тексты на китайском (традиционном) · Объяснения на русском」；ja「VOL.4 · 中国語（繁体字）テキスト · 日本語の解説」；ko「VOL.4 · 중국어 번체 텍스트 · 한국어 해설」。
- 网页 PDF 均 < 7 MB。印刷 PDF 字节与旧版接近（fr 完全相同 20,191,919；ru 仍 12.9MB 级——图片嵌入差异，卡片尺寸与文字层完整，见 ru KIT）。

## §6 门结果总表（驱动：`scratch-refanout-zh-tw/gates.py <lang> final` → `gates/<lang>-final/gates.json`；每版均跑：checks.py、occlusion（selftest + audit）、p8 extract + compare（显式 --core-p8/--edition-p8）、freeze、keycheck（fillin + 1–150 连续）、boxtitle、abutting、occlusion、canonical creambox 全版扫描（`hidden_files/w47/tools/creambox.py`）、印/网 text layer 比对、PIL creambox 补充扫描）

列说明：checks｜occlusion flags｜p8 150/compare｜canonical creambox 36 盒/负清除｜boxtitle 超框/最小右余｜PIL STRADDLE（新/旧）｜CREAM-COVER｜P8 最小字号｜fillin/keys 连续｜leak deny｜P6 18:30/19:00 墨缝｜freeze｜目视。

| 版 | checks | occl | p8 | canon | boxtitle | STRADDLE | cover | P8 pt | keycheck | leak | abutting | freeze | 目视 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| de | PASS | 0 | 150/CLEAN | 36/0 | 0/23.2 | 4 (旧 4) | 0 | 9.75 | 54/150 | 0 | 0.6 | 8/8 | 目视✓ |
| fr | PASS | 0 | 150/CLEAN | 36/0 | 0/-0.2 | 0 (旧 0) | 0 | 9.75 | 54/150 | 0 | 0.6 | 8/8 | 目视✓ |
| es | PASS | 0 | 150/CLEAN | 36/0 | 0/9.8 | 4 (旧 5) | 0 | 9.75 | 54/150 | 0 | 0.6 | 8/8 | 目视✓ |
| it | PASS | 0 | 150/CLEAN | 36/0 | 0/13.8 | 2 (旧 2) | 0 | 9.75 | 54/150 | 0 | 0.6 | 8/8 | 目视✓ |
| pt | PASS | 0 | 150/CLEAN | 36/0 | 0/9.5 | 3 (旧 3) | 0 | 9.75 | 54/150 | 0 | 0.6 | 8/8 | 目视✓ |
| nl | PASS | 0 | 150/CLEAN | 36/0 | 0/1.5 | 0 (旧 0) | 0 | 9.75 | 54/150 | 0 | 0.6 | 8/8 | 目视✓ |
| ru | PASS | 0 | 150/CLEAN | 36/0 | 0/22.5 | 4 (旧 5) | 0 | 9.75 | 54/150 | 0 | 0.6 | 8/8 | 目视✓ |
| ja | FAIL* | 0 | 150/CLEAN | 36/0 | 0/1.2 | 0 (旧 0) | 0 | 9.75 | 54/150 | 0 | 0.6 | 8/8 | 目视✓ |
| ko | PASS | 0 | 150/CLEAN | 36/0 | 0/18.5 | 0 (旧 0) | 0 | 9.75 | 54/150 | 0 | 0.6 | 8/8 | 目视✓ |

补充说明（逐条均有日志/证据在 `gates/<lang>-final/`）：

- **checks PASS 8/9**：ja 唯一 FAIL 仅为 `SIMP_ONLY_HITS ['国', '学']`（见 §7 未决项 3，已逐出现核为日语汉字误报）。其余 P4 bars [90.0, 450.0, 900.0]、P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] 全 9 版与期望一致。
- **occlusion 0 flags** 全 9 版（selftest 6 类 planted 均触发，clean 对照静默）。
- **p8**：extract noted_set 150/150；compare vs core 显式 --core-p8/--edition-p8，status **CLEAN**，missing=[]、extra=[]、keydiff=[]；答案值与核心 150 项一致。注：`gates.json` 里 `"extra": "?"` 是本轮驱动脚本的取键小 bug（读了不存在的 `extra_count`），compare JSON 本身的 extra=[] 已逐版核对。
- **canonical creambox**：36 盒全 9 版，负内清除 0；分页面最小内清除：P1 18.8、P2 15.8–41.8、P3 15.8、P4 9.8–35.8、P5 6.4、P6 19.9、P7 12.4–12.5（P8 无盒）。P7 工具盒 +40.5/+12.5/+14.0（ja +40.5/+12.4/+14.0；it 第一盒日志用双引号，驱动正则漏采，实测值同样为 +40.5/+12.5/+14.0）。
- **boxtitle**：36 盒、超框 0 全 9 版；最小标题右余：de 23.2、fr **-0.2**、es 9.8、it 13.8、pt 9.5、nl 1.5、ru 22.5、ja 1.2、ko 18.5 px（fr -0.2 与旧版完全相同，见 §7）。
- **text layer**：印/网 pdftotext（-layout）字节全 9 版相等，字符多重集差 0；plain pdftotext 印/网差恰 1 字节（与旧版的 2 字节同类 run-boundary 空白 artifact，无字符缺失）。计数：本週日 11/11、下週日 0/0、BABYMONSTER 0/0、取捨 2/2、小雪 36/36（ja 54/54——日语讲解层另有小雪词条，属语种差异）、end point 0（各语值已译）。
- **PDF**：8 页、1462.5×2025 pt；P8 最小字号 9.75pt（印/网一致，恰 SOP §1.1 下限）；P8 最大 34.5pt；P1 顶部字号 [147.0, 45.0, 27.0, 24.0] 全 9 版一致。
- **keycheck**：填空键 54/54 出自正文；答案键 1–150 连续（150/150）。
- **leak scan**：deny 命中 0 全 9 版；唯一与核心共有的长 ASCII 串为选项行「A. 12:00 · B. 14:00 · C. 19:00」（构造共享，非泄漏）。
- **abutting**：P6 18:30「頒獎典禮」墨右缘 990.8 与 19:00「夜間遊行」墨左缘 991.4，缝 **0.6px**——与核心先例完全一致（发丝缝、无重叠、不算缺陷）。驱动曾误取 P6 正文首现，今已改为同行最小缝取对。
- **freeze**：baseline 重跑 8/8 字节一致，核心完整性 OK（核心 8 个 SVG 重哈希未变）。
- **目视**：9 版 8 页全部看过（de：整版联络表 + P7 teaser 裁切 + P4 D4 裁切；其余 8 版：每版 2×4 联络表）。无溢出、无重叠、无页脚碰撞、图片/署名位置确认；P7 记忆/M1 行、P6 时间线、P4 D4 盒、P8 键尾均在画面内。

## §7 未决项（待协调员；无一写成通过）

1. **英文源 key「next Sunday」未改（有意未执行，见 §1④-英）。** `tables.py:245/:267/:322` 仍为「next Sunday」/「Next Sunday」；冻结核心 `content12.py:37/:113`、`content34.py:127` 亦然，re-proof #3 结论 (a) 认证了该核心。若要改英文，须先做核心 fix，再改表、再重 fan-out 9 版。——本轮 D1 六语值已全部改成本周日，印/网文字层「下週日」0 处、「本週日」11 处全 9 版一致。
2. **双语小檔标题 STRADDLE（补充 PIL 扫描发现；正门不含此项，全部正门均通过）。** 双语小檔标题（「中文名　<读者语名>」）墨迹伸出无边框米色盒右缘 7–80px，文字本身完整可读、无任何重叠（occlusion 0、CREAM-COVER 0、canonical creambox 全正）。逐版新/旧对照（旧版用同一扫描跑备份 SVG）：
   - de 4 = 旧 4（坐标完全相同：P2「Christmasland-Steckbrief」+64.2、P3「Golden-Horse-Steckbrief」+29.8、P3「Letztes Wochenende」+28.2、P5「Disney-Steckbrief」+17.5）；
   - fr 0 = 旧 0（但 boxtitle 最小右余 -0.2px，P2「Fiche Christmasland」，与旧版完全相同，亚像素，渲染不可见）；
   - es 4 < 旧 5（旧第 5 个为 P4 D4 盒底穿「deporte?」，已被核心 fix5 修好；余 4 与旧版相同：P2「Ficha de Christmasland」+37、P3「Ficha de los Golden Horse」+40、P3「Último fin de semana」+36、P5「Fechas del jazz」+7.2）；
   - it 2 = 旧 2（P1「Parola della settimana」+0.8、P2「Scheda Christmasland」+24.5）；
   - pt 3 = 旧 3（P2「Ficha do Christmasland」+38、P3「Ficha dos Golden Horse」+12、P3「Último fim de semana」+44.2）；
   - nl 0 = 旧 0；ru 4 < 旧 5（旧第 5 个为 P4「занимаетесь спортом?」，亦被 fix5 修好；余 4 相同：P2「Крисмасленд: коротко」+41.5、P3「«Золотая лошадь»: коротко」+80.2、P3「Последние выходные」+53.5、P5「Дисней: коротко」+14.2）；
   - ja 0 = 旧 0；ko 0 = 旧 0。
   - 净效果：重建修好了 2 处旧超框，引入 0 处。证据：de P2 裁切图 `de-p2-steckbrief-crop.png` 可见「Steckbrief」伸出米色盒；旧版 proof1（de）曾以 (b) 通过德语讲解层、唯一缺陷为核心 D1，并未列出这些标题（当时未跑 PIL STRADDLE 扫描）。
   - **未在本轮修**：缩短标题是改文字/版式的设计决定（备选：缩短读者语后缀，或标题字号自适应——后者改共享绘图 helper，属核心级改动），应由协调员定 fix1；已如实记录，未写成通过。
3. **ja `checks.py` SIMP_ONLY_HITS ['国', '学']（已核为误报，非缺陷）。** 逐出现核对：仅出现在 3 处日语词——「中国語」×2、「国際」（高雄国際鋼雕芸術祭）×1、「学べる」×1，均为标准日语汉字（新字体）；繁体中文正文无国/学出现。旧 ja KIT 已有同样说明，本轮复核一致。SIMP_ONLY 检查无法区分日语汉字与简体字，今后每版 ja 都会触发此行，应按上下文核对。
4. **de P8 D-head HEAD TOO WIDE（已知非缺陷，沿用）。** 「D　讀一讀，答一答　Lesen und antworten」423.08px vs 422.5px 栏宽，伸入 28px 间隔 0.58px；W46 de 已发版亦然，无碰撞（occlusion 0、目视干净）。记入 de KIT。
5. **工具小 bug（已定位，不影响结论）：** 本轮 `gates.py` 的 p8 extra 字段读错 key 名（显示 "?"，实为 []）；it P7 工具盒第一盒因日志双引号漏采（实测 +40.5）。两处均已在报告内用实测值纠正，驱动待下轮修。

## §8 KIT 更新

- 9 版 `WEEKLY-KIT.md` 均已更新：以备份旧版 KIT 为底，替换 §「Measured totals」印刷/网页/text.md 字节 + SHA-256（新值见 §5）、text layer 新字节（印/网差 1 字节）、P7 几何新值（de B1 1568→1602、已知非缺陷同步更新），新增「Re-fan-out (2026-11-11)」一节（核心基线、方法、手修重应用、门结果、STRADDLE 披露、目视）与 Build history 条目。核对：旧 SHA 前缀 9 版 KIT 内 0 残留，新 3 件 SHA 9 版齐全；de KIT 一处模板占位已手工修为实测值并复核无残留。
- 注意：各版 KIT 的「Proofread record」旧轮次记录保留为历史；本轮门结果写在新增的 Re-fan-out 一节内。

## §9 文件索引（本 scratch 内）

- 本报告：`FANOUT-REPORT-zh-tw.md`；机制表备份：`tables.py.bak-pre-refanout`；补丁脚本：`patch-tables-d1.py`；机制表审计：`audit-tables.py`。
- 旧版备份：`backup/2026-w47-zh-tw-{de,fr,es,it,pt,nl,ru,ja,ko}/`（290M，不删）。
- 构建日志：`build-<lang>-run*.log`、`render-<lang>.log`、`webpdf-<lang>.log`、`export-<lang>.log`；门结果：`gates/<lang>-final/gates.json` + 各门日志（`checks.log`、`occlusion*.log`、`p8-*.json`、`creambox.log`、`creambox-pil.log`、`boxtitle.log`、`fillin-check.log`、`freeze.log`、`text-layer-*.txt`）；旧版对照扫描：`gates/old-<lang>-check/`。
- 新旧内容 diff：`diff-new-vs-old-<lang>-<file>.txt`；目视：`<lang>-contact.png`（9 版）、`de-p2-steckbrief-crop.png`、`de-p7-teaser-crop.png`、`de-p4-d4-crop.png`；驱动：`gates.py`、`gtools/`（boxtitle.py、creambox-pil.py、check_fillin_keys.py——keys 区标记已改为行首「答案」以适配各语标题）。
- 驱动修补记录：gates.py 修复 4 处解析 bug（p8 `noted_set`、canonical creambox 分节统计与 ± 号、keys 区标记、abutting 同行最小缝取对）+ boxtitle 负值正则；`check_fillin_keys.py` 副本的 keys 标记改为 `^答案`；pt 重启恢复见 §4。

## 交付

- 9 版已全部建成于 `~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-<lang>/`，三件 SHA 与门结果见 §5/§6，KIT 已更新。未 commit，未 push。9 版重校（proof1/proof2）由协调员另派。
