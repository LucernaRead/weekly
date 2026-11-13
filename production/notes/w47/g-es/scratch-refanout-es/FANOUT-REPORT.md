# W47 es 全族重建报告（re-fanout，core build 10 定稿后）

- 日期：2026-11-11
- 任务：从定稿 core-es fix build 10 重建 10 版 fan-out
  `production/2026-w47/2026-w47-es-{de,en,fr,it,ja,ko,nl,pt,ru,zh-tw}/`
  （core-es 即 zh-cn 读者版，不建 es-zh-cn）
- 工作目录（goals 侧 scratch）：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-refanout-es/`
  （下称 **S**；备份 `S/backup-old/`，门禁日志 `S/<lang>-*.log`，门禁汇总 `S/<lang>-gates.json`，
  目检裁图 `S/visual/`，分类报告 `S/classify-<lang>.txt`，原始 diff `S/diffs/<lang>.diff`）
- Fan-out 机制：`hidden_files/w47/scratch-fanout-es/`（`apply_fanout.py`、`manual_table.py`、
  `harvest/<lang>.json`、`extract_text_es_<lang>.py`）
- **没有 commit，没有 push。**10 版目录在仓库里仍是未追踪状态，待协调员入仓。

## 0. Core 基线（已定稿，不动）

core-es fix build 10，独立 re-proof (a) 零问题：

| 产物 | 字节 | SHA-256 | 行数 |
|---|---|---|---|
| print `La-Lucerna-VOL4.pdf` | 17,212,955 | `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5` | — |
| web PDF | 1,410,471 | `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235` | — |
| text.md | — | `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb` | 1,822 |

已在 core 落盘的改动（本重建只继承、不重议、不重打）：
C1（P1 CINCO CLAVES 盒 700→720）、C2（`antes del jueves`→`hasta el jueves`，
11 月 19 日周四 inclusive，Correos 官方通告原文证实）、es-ja D1（consejo 句补全）+D4
（德比周六 21 日）、es-nl D1/D2（Atresmedia 23 Nov 正确、Q89 键 B 成立，协调员 11:18 UTC
再裁定）、es-pt C2（PCTE 保留，195 总数保留）。
**C3（P5 词库 `content56.py:79`：4 用 + 2 干扰词 sobre/urna）已裁定接受原样，全程未动该行。**

## 1. 方法

1. 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 通；
   goals 侧真实写文件成功后才开工。TMPDIR 全程用 `S/tmp`，从未写 `/tmp`。
2. 备份：10 个旧版目录完整拷到 `S/backup-old/`（154 MB），`diff -rq` 验证与原版一致
   （仅 `__pycache__` 噪声）。
3. 机制补丁：core build 10 改了中文邮寄投票句，旧 harvest 键失效，
   `scratch-fanout-es/manual_table.py` 新增两条 MANUAL（147b 短句、147c 长句 `→ ___`），
   10 语翻译全部给出；it/ja/ko/pt/ru 的短句旧译已是 inclusive 措辞，原样保留。
4. 重跑：10 版旧目录删除后经 `apply_fanout.py <lang>` 重建；apply 报告 leftover zh 键 NONE、
   .py 内 CJK NONE（ja 2 处 key==value 误报 `VIDA　生活` / `CULTURA　文化`；
   zh-tw 剩余全为同形 no-op，`EL PLAN DE LA SEMANA　本周计划` 经 diff revert 恢复）。
5. 分类：`S/classify.py` 逐行比对备份与新版源码——KEEP = core build 10 改动，
   REVERT = 版内手修恢复，MERGE = 德比信行（新版 sábado + 备份 ASCII 括号），
   INSERT = RTVE debate-a-ocho 时间轴行（新版独有）。每版 MERGE 1、INSERT 1、DELETE 0，
   无不等长块；且逐项核对无 REVERT 行含 core 关键词、无 MERGE/INSERT 误判。
   分类后残差 diff（vs 备份）恰好 = 2×KEEP + 1 INSERT + 2 MERGE 行。
6. 手修：备份里没有的，在 proof 报告指导下逐项新打（见 §3），逐项 PIL 真墨复测。
7. 门禁：`S/gates.py` 逐版跑 render + occlusion + p8 extract/compare + freeze baseline/diff +
   creambox（全版扫描）+ creambox_diag（真墨）+ boxtitle（真墨）+ keycheck + sweep +
   pdftotext print/web 一致 + P8 最小字号（pypdf visitor，有效字号 = font_size × |Tm[0]|，
   阈值 ≥9.75pt）。de/fr 在盒题修复后重建 run3 并重跑全门禁（含重渲染）。

## 2. 十版新产物（SHA + 字节）

| 版 | print 字节 / SHA-256 | web 字节 / SHA-256 | text.md 行 / SHA-256 | text 字节 (print=web) | P8-keys 终 y |
|---|---|---|---|---|---|
| es-de | 3,503,120 / `65ebf6b7df8b07013d809427259a8b3504ac33e318bb9e0b61f72d7c9498fbca` | 889,914 / `2e39306ddd4424e8309aed9efe9e580920c75a826e5821c5e67f401f91c7ec9b` | 1,802 / `81ff06563dd9332ab6af2b4d826f2dda6d7157d82983df01e484fa462c310a67` | 111,448 | 2506 |
| es-en | 3,500,924 / `80b4ce0a095551599adbf0e8e0c617715513a6df3c6ad004cc1428d8bb99b602` | 886,730 / `f03047b1631fba034e3e65d2804a95c4c4ea40ba6af36a46e312921a7a70b5b0` | 1,797 / `6080c94c420fd1077fedee777bba77ec789fd4c6c431ef70e7b7313923cc8906` | 107,966 | 2569* |
| es-fr | 3,500,186 / `688152c7a055a25414e9c72b33f9e6d074b8137c2a9e2c9ea365b4d541e14894` | 884,225 / `3c2d60696561278323150dafabe922bc77df682946e3266e89adfb9180a3016c` | 1,815 / `ae1c3f3ba234a0b3f5ce2128770e4e4983d509822fdd520d03da4e98a76fad43` | 109,748 | 2521 |
| es-it | 3,498,553 / `12e7e0817b13bdd21576b820bd567b821fb69c679508189b1ef9ba973b442724` | 882,077 / `17d4b8efd2b997ce84f260f8dd1def296c145a3ade005a4885d41a4fc35cf4d8` | 1,806 / `434e8df8f0d64924b89efe561adcc9406e7b1442e801eee66c16ceeca7f06abe` | 108,723 | 2521 |
| es-ja | 17,294,448 / `459d570a294a14a3b170e7bf99ca4db3bc91560603dc21c43d371977e55da12f` | 1,540,831 / `5895fce90fffd07cccf1909f8de1aa481572751e8caa9bc3a0d80be00845f71f` | 1,820 / `7479077861f46c27c4d69ae265d43bab40e14cdc2e09bec48d53772142b3e9ea` | 109,951 | 2521 |
| es-ko | 8,874,351 / `65e3a3993f2f315f9a89c316788f6f93ed79ef69212c4b32f08f52a9976cb0f7` | 1,237,415 / `54494cef95ba3a7b98dc70aba67bd8a5cd03676106f14b6c928f38f417715351` | 1,817 / `f49dd7088c16f7a40c14618019a05800b45418be8a9a137c8f83ddb8554dbc3e` | 109,956 | 2506 |
| es-nl | 3,502,134 / `d5e63a7f5ee3c974b345ebdb72ca438082718de970e2469dba7c2f96b60db68c` | 887,959 / `54fbf35e4f3a0694d1922b5ef158d7ab9212d8908d1cedbecbf23f4465f6a763` | 1,835 / `d8d8e0078a7a121cf9a68bb22ee8074c6245462ebd86ef768cf87ee88c44b91e` | 109,833 | 2506 |
| es-pt | 3,500,936 / `0c8dd28550be5ababc176503a426e430546f8357969d8f9104451b10b5c0d6c2` | 885,039 / `427e9c26d0b055f94e27e06fb659738e7250363e8a0eaf88fe5086f70e099e38` | 1,815 / `9df4d30caba991aa1f966eccc360cf801b3a6cf9764f448662be5804de06e6c8` | 109,215 | 2521 |
| es-ru | 3,593,735 / `68a761681e7d760174eed1554672b7c3664cfbbef16bc89538543202bc3414b5` | 941,922 / `e6281174237fe2bd31fb749fe7bc9bd76055933a632ec8b20d3081556171aaab` | 1,893 / `05e7d6c91fa331618985a9d9bfae6564c1d596321227d002e4ff92e26a25c6aa` | 117,979 | 2537 |
| es-zh-tw | 17,263,265 / `ef5f1cde27036e5c810c4f779fd43e743857ab763c77df9b09bf6d885d804365` | 1,725,936 / `5b7d87967332783dd0314d54ab2b8483e7d0036b4bdc8609ae3226f2c5de6500` | 1,803 / `930fc2bab9b7f99ad45c1a2d50349a750bb76b52f89bad2dc0f203b62310f36f` | 106,384 | 2506 |

*en P8-keys 终 y=2569：无 OVERFLOW 警告，末墨距页脚线 39px，沿用旧 build 5 的已接受状态。
所有 10 版 print/web 文字层字节一致；全部 web PDF < 7 MB。

分类计数（KEEP / REVERT / MERGE / INSERT）：
de 23/36/1/1，en 23/23/1/1，fr 23/40/1/1，it 18/32/1/1，ja 17/19/1/1，
ko 18/15/1/1，nl 23/31/1/1，pt 18/40/1/1，ru 17/45/1/1，zh-tw 23/6/1/1。

## 3. 手修重打清单（逐项核实）

### 3.1 经 revert 恢复的旧版手修（备份里有，classify 恢复）

- fr D1：P3/P5 ¿Y TÚ? 盒各 +9px（eh 尾部 +29 恢复）。
- ko D-02：P8 #45 补系词 → `두 번째예요`。
- zh-tw：`EL PLAN DE LA SEMANA　本週計劃`（text.md 核实 ×1）。
- 其余各版的旧手修均由 classify REVERT 行恢复（计数见 §2），无一漏、无一错打到别版。

### 3.2 新打的手修（备份里没有，逐项核实）

| # | 版 / 项 | 改动 | 核实 |
|---|---|---|---|
| 1 | fr O1 | `content12.py:198`、`content56.py:41` facts 盒公式 `+37` → `+42`（P2 ¿SABÍAS QUE…? 盒、P5 VOTAR POR PRIMERA VEZ 盒各 +5px） | PIL 真墨：两盒 clearance 各 **+10.1px**；P2 渲染裁图核实墨在盒内 |
| 2 | it E1 | `content12.py:275` `Leggi l’articolo` → `Leggi l'articolo`（直撇号） | text.md：直撇号 ×4，curly ×0 |
| 3 | ru D1 | `content34.py:45` eh `+20`→`+25`（P3 ¿Y TÚ? 盒） | PIL 真墨 clearance **+2.7px**；裁图核实 |
| 4 | ru D2 | `content56.py:50` eh `+20`→`+25`（P5 同类盒） | PIL 真墨 clearance **+2.7px**；受 y=1608 分隔线封顶（1.5px 间隙，无法再延）；裁图核实 |
| 5 | ru D3 | `content7.py:83` `ERRORES TÍPICOS　Типичные ошибки` → `…　Ошибки`（原超盒右缘 44.7px） | boxtitle 0 溢出；裁图核实标题在盒内 |
| 6 | pt D1 | `content12.py:46` `LA SEMANA EN CIFRAS　Em números` → `…　Números`（原 +10.9px） | boxtitle 0 溢出；裁图核实 |
| 7 | pt D2 | `content56.py`：#67 `seções`→`secções`、#71 `cédula`→`boletim de voto`、#74 `cadastro eleitoral`→`recenseamento eleitoral`、#96 `fato`→`facto`（巴西葡语→欧洲葡语） | text.md：欧葡形式齐全，巴西形式 ×0 |
| 8 | ko D-01 | `content12.py:116` `“토론”` → `"토론"`；`content56.py:93` `‘~할 것’` → `'~할 것'`（ASCII 引号） | text.md：curly ×0；两处渲染裁图核实为直引号、拉丁字体 |
| 9 | nl D3 | `content56.py:50` eh `+20`→`+29`（P5 ¿Y TÚ? 盒，+9px） | PIL 真墨 clearance **+6.4px**；裁图核实 |
| 10 | nl D4 | `content56.py:22` `EL PLAN DE LA SEMANA　Het weekplan` → `…　Weekplan`（原 +36.8px） | boxtitle 0 溢出；裁图核实 |
| 11 | nl D5 | `content7.py:83` `ERRORES TÍPICOS　Typische fouten` → `…　Fouten`（原 +6.5px） | boxtitle 0 溢出；裁图核实 |
| 12 | nl D6 | `content7.py:134` 横幅 `py = fy + 66 + 3*128 + 105 + 30` → `+ 1`（上移对齐 core） | 横幅 py 2464.5、底缘 2582.5 = core exactly；页脚墨顶 2611，间隙 28.5px；裁图核实 |
| 13 | fr D1 | 见 §3.1（经 revert 恢复，P3/P5 真墨 clearance 各 +6.7px，≥+5 要求；裁图核实） | — |

### 3.3 本重建中新发现并修复的问题（首轮漏检）

| # | 版 | 问题 | 修复与核实 |
|---|---|---|---|
| A | de | boxtitle 溢出 ×2（首轮未在 de 跑 boxtitle）：`EL PLAN DE LA SEMANA　Wochenplan` −21.4px；`ERRORES TÍPICOS　TYPISCHE FEHLER` −30.8px | → `…　Der Plan`、`…　Fehler`（与其他版短 gloss 惯例一致）；重建 run3 rc=0，boxtitle 0 溢出，P8-keys 仍 2506 |
| B | fr | boxtitle 溢出 ×2（首轮未在 fr 跑 boxtitle；LA SEMANA 一处 pt proof1 已指出漏检）：`LA SEMANA EN CIFRAS　EN CHIFFRES` −16.8px；`ERRORES TÍPICOS　ERREURS TYPES` −9.2px | → `…　Chiffres`、`…　Erreurs`；重建 run3 rc=0，boxtitle 0 溢出，P8-keys 仍 2521 |
| C | fr/nl | C2 新措辞使 5 条 P8 答案注在 13.5pt 下由 1 行变 2 行，P8-keys 溢出警告、终 y=2590（底 2560） | 各版 5 条注缩短为 1 行（fr 如 `Vote par correspondance: à demander le 19 au plus tard`；nl 如 `Stemmen per post: uiterlijk op de 19e aanvragen`；均经 `bslib4.wrap()` 验证 1 行）；重建后 0 OVERFLOW，P8-keys fr 2521、nl 2506（与旧版终值一致） |

### 3.4 ABSTRACT.txt / KIT

- 各版 ABSTRACT.txt + WEEKLY-KIT.md 均从备份拷回；两处措辞按 core build 10 事实修正：
  fr `avant le 19 novembre` → `le 19 novembre au plus tard`；
  zh-tw `11月19日前申請郵寄投票` → `最遲11月19日申請郵寄投票`。
  其余摘要已用 inclusive 措辞（bis/entro/までに/까지/tot/até/до/by），且未对 laSexta 辩论作虚假排他表述。
- 各版 WEEKLY-KIT.md 已追加“重建（re-fanout，2026-11-11 — core build 10）”一节
  （新 SHA、手修、门禁结果、移交注意事项）。
- text.md 内容抽查（每版）：`hasta el jueves` ×7、`antes del jueves` ×0、
  `sábado veo el derbi` ×1；拉丁版 text.md CJK 字符 0（ja/ko/zh-tw 为本语文字，预期内）；
  ja 1,601 CJK 字符为日语说明。

## 4. 门禁汇总

每版 `S/<lang>-gates.json`，除 ru keycheck 一项裁定外全部 rc=0：

| 版 | run | render | occlusion | p8 150/150 | p8 compare | freeze 8/8 | creambox 真墨 | boxtitle | keycheck | sweep | print=web 文字 | P8 最小字号 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| de | 0 | 0 | 0 | ✓ | CLEAN [137,138] | ✓ | 0 | 0 | 149/150* | 0 | ✓ 111,448 B | 10.125pt |
| en | 0 | 0 | 0 | ✓ | CLEAN [137,138] | ✓ | 0 | 0 | 149/150* | 0 | ✓ 107,966 B | 10.125pt |
| fr | 0 | 0 | 0 | ✓ | CLEAN [137,138] | ✓ | 0 | 0 | 149/150* | 0 | ✓ 109,748 B | 10.125pt |
| it | 0 | 0 | 0 | ✓ | CLEAN [137,138] | ✓ | 0 | 0 | 149/150* | 0 | ✓ 108,723 B | 10.125pt |
| ja | 0 | 0 | 0 | ✓ | CLEAN [137,138] | ✓ | 0 | 0 | 149/150* | 0 | ✓ 109,951 B | 10.125pt |
| ko | 0 | 0 | 0 | ✓ | CLEAN [137,138] | ✓ | 0 | 0 | 149/150* | 0 | ✓ 109,956 B | 10.125pt |
| nl | 0 | 0 | 0 | ✓ | CLEAN [137,138] | ✓ | 0 | 0 | 149/150* | 0 | ✓ 109,833 B | 10.125pt |
| pt | 0 | 0 | 0 | ✓ | CLEAN [137,138] | ✓ | 0 | 0 | 149/150* | 0 | ✓ 109,215 B | 10.125pt |
| ru | 0 | 0 | 0 | ✓ | CLEAN [137,138] | ✓ | 0 | 0 | 148/150† | 0 | ✓ 117,979 B | 10.125pt |
| zh-tw | 0 | 0 | 0 | ✓ | CLEAN [137,138] | ✓ | 0 | 0 | 149/150* | 0 | ✓ 106,384 B | 10.125pt |

*keycheck 149/150：唯一 mismatch 为 #150 开放写作题，抽取为 `✓`，为已知例外（各版皆然）。
†ru keycheck 148/150：第 2 个 mismatch 为 #137，**裁定非缺陷**（见 §5.1）。
freeze-diff CJK 账：de/fr/it/nl 仅新增 U+3000（分隔符）；en/pt/ru 新增 0；ja/ko/zh-tw 新增为本语文字。
creambox 全版扫描：每版原始扫描各有 6 条负 clearance，皆为盒下标题/注文（与 core 同坐标、同布局，设计如此，
fr proof1 已裁定）；creambox_diag 真墨复核：10 版自有末行墨 clearance 全部 ≥0。

## 5. 裁定记录

### 5.1 ru keycheck #137（抽取器误报，非缺陷）

- 现象：keycheck 148/150，#137 抽取 `Понедельник`，REG 为 `Понедельник — Международный день фламенко.`。
- 原因：俄语译句用 em-dash 作系动词（“星期一是……”），`p8.py` 的 dash 风格解析把第一处
  ` — ` 当作“键—注”分隔符，故键只取到 `Понедельник`。
- 核实：SVG 中 #137 键文完整在同一行（y=2088.34）；渲染裁图 `S/visual/ru-p8-key137.png` 显示
  印出全文 `137. Понедельник – Международный день фламенко – См. оригинал.`。
  与 p8-compare keydiff [137, 138] 为同一裁定项（旧版 KIT §6.1：翻译题按键以目标语译句为准，
  注 `См. оригинал.`，非缺陷）。旧版 KIT §6.4 另记 #137/#138 保留 2 行（本版亦然）。
- 结论：keycheck 实际有效 149/150 + 一项已裁定；不改版面。

### 5.2 其余已接受状态（沿用旧版裁定）

- p8 compare keydiff [137, 138]：各版皆然，翻译题按键以目标语译句为准（W45/W46 裁定）。
- en P8-keys 终 y=2569：无 OVERFLOW，末墨距页脚线 39px（见 §2 注）。
- fr P5 col3 1593.55 < 1608 分隔线；nl P7 col3 1873.51（与旧裁定注一致）。

## 6. 移交 proof2 的注意事项

- **es-fr proof2 必须重测 P1 CINCO CLAVES 盒（C1）与 P1 盒题真墨**：本重建实测 P1 盒底 1308.0、
  末行墨底 1304.2、真墨 clearance **+3.8px**（在内为正；core 原测量为 +5.8px，法语末行
  `Cinq clés, sans chiffres inventés.` 墨位略高）。另须复核本重建新修的两处盒题
  （`Chiffres`、`Erreurs`）与 O1 两盒（+10.1px）。
- **es-nl proof2 必须复测 D3–D6**：D3 真墨 +6.4px；D4/D5 盒题已缩短；D6 横幅 py 2464.5 = core、
  页脚墨顶间隙 28.5px。
- **es-de / es-en**：先前“定稿”状态已作废（重建于新 core 之上），须另派重校；本重建另在 de
  发现并修复两处首轮漏检的盒题溢出（§3.3 A），en 无新增问题。
- **es-ru**：D2 盒底距 y=1608 分隔线仅 1.5px（无法再延，设计上限）；#137 keycheck 裁定见 §5.1。
- **es-ja / es-zh-tw**：无手修，仅重建验证；ja boxtitle 的 2 处 key==value 误报非溢出。
- 各版 KIT 的重建附录含本版全部新 SHA 与门禁细节；门禁日志与裁图在 S 内可查。

## 7. 交付物与状态

- 10 版已重建、渲染、门禁全绿（ru 一项 keycheck 已裁定），KIT 已更新。
- **未 commit、未 push**；10 版目录在 `~/workspace/weekly-git` 中为未追踪状态。
- 本报告：`S/FANOUT-REPORT.md`。
- 旧版备份：`S/backup-old/`（154 MB，`diff -rq` 已验证）。
