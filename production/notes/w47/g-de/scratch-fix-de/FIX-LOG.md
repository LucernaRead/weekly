# W47 de 家庭修复日志（SOP §8 修复流程）

- 修复工人：subagent d307ec2a（de 家庭修复）
- 日期：2026-11-12
- 范围：10 版 fan-out（2026-w47-de-{en,es,fr,it,ja,ko,nl,pt,ru,zh-tw}）；core-de 零问题，不动。
- 依据：`scratch-reproof-w47-de/PROOF-NOTE.md`（9 条 F1–F9，F7 major 其余 minor；协调员已核实属实）；D5-REPORT（`scratch-d5-de/RUN-LOG.md` + 各版 WEEKLY-KIT §5–§7，渲染命令 `build_edition.py <lang>`）。
- 工具：全程 `~/workspace/weekly-git/tools/venv/bin/python`。不 commit、不 push、不跑 lint。磁盘：开工 93G 已用 / 150G。
- 构建驱动：`scratch-fanout-de/build_edition.py <lang>`（run.py → render.py → webpdf → verify → occlusion → p8 → freeze → pdftotext → chips → text export）。门禁另跑：`tools/boxtitle_check.py`、`tools/spill_sweep.py`、`tools/pdf_edge_scan.py`、`tools/head_check.py`（build.log）、D5 普查复核（`scratch-fix-de/census.py`，D5 原普查脚本未保留，按 census-patched.json 口径自写等效核查）。
- 注意：`occlusion_audit.py` 对 letter-spacing 有测量盲区（PROOF-NOTE O7），F7 不以 occlusion 0 flags 为准，以 advance 实测 + P1 渲染图目视为准。

## 改前基线（盘上实测，与 PROOF-NOTE 一致）

| 版 | text.md 字节 / SHA 前 12 | web PDF 字节 / SHA 前 12 | print PDF 字节 / SHA 前 12 |
|---|---|---|---|
| de-en | 49658 / `e0947980eb52` | 1509978 / `3be4943e11fe` | 10349936 / `ad95457cbdf7` |
| de-es | 50124 / `5f5ea69b69a5` | 1514229 / `3feadde5ae0f` | 10354187 / `93ad64f8e3ae` |
| de-fr | 50042 / `3ef1934af59e` | 1512394 / `e15171852122` | 10352360 / `fef16b0bc8b0` |
| de-it | 49712 / `1594ba080bec` | 1508579 / `348a9389865e` | 10348542 / `9316b647da34` |
| de-ja | 51913 / `a59f784705be` | 1935168 / `c460c72c8f6e` | 15963826 / `03c71417a55f` |
| de-ko | 51498 / `fd2dbd047e23` | 1789607 / `c63dbb544b9e` | 12889807 / `559a59cda507` |
| de-nl | 49403 / `e904fb3d7ee1` | 1507082 / `0c9e07550881` | 10347054 / `0ca4821bd281` |
| de-pt | 49812 / `e2ee96ebd9dc` | 1514691 / `fb4c17fa436f` | 10354673 / `b3ad2533ab0f` |
| de-ru | 56231 / `dee6697b0ec3` | 1769729 / `c0c2360180d4` | 10623285 / `97941203c39a` |
| de-zh-tw | 49092 / `fe62ddb59ac6` | 1936641 / `48edfb95456b` | 11838985 / `d51a66c6331d` |

## 修复内容（源头改动）

- **F7**（5 版）：`content12.py:15` 顶栏 kicker 读者语段缩短（居中排布，缩短量一半落到右缘；目标 advance 间隙 ≥12px，折合 ink 间隙 ≥10px，对照 de-en 14.5px ink）：
  - es：`EL ALEMÁN QUE LEEN LOS ALEMANES` → `EL ALEMÁN QUE LEEN`，advance 间隙 49.6px
  - fr：`L'ALLEMAND QUE LISENT LES ALLEMANDS` → `L'ALLEMAND D'ALLEMAGNE`，advance 间隙 18.4px（`L'ALLEMAND DES ALLEMANDS` 仅 5.8px，不够）
  - it：`IL TEDESCO CHE LEGGONO I TEDESCHI` → `IL TEDESCO DEI TEDESCHI`，advance 间隙 23.6px
  - nl：`HET DUITS DAT DUITSERS LEZEN` → `HET DUITS VAN DUITSERS`，advance 间隙 31.0px
  - pt：`O ALEMÃO QUE OS ALEMÃES LEEM` → `O ALEMÃO DOS ALEMÃES`，advance 间隙 31.9px
  - 度量方法复核：同一算法复算改前值得 es −33.1 / fr −58.0 / it −40.8 / nl −4.8 / pt −17.4（PROOF-NOTE ink 值 −34.8/−59.7/−42.5/−6.5/−19.2，差约 1.7px 为末字 bearing，方向一致）；en 对照 16.2（PROOF-NOTE 14.5）。
  - 另查：RIGHT=1862（bslib4 注释误写 1885），刊期 x=1447.4 不动。
- **F8**（de-it）：`content12.py:27` 横幅译文 `TORNA LA BUNDESLIGA` 27pt → 24pt（沿用 es/fr 的 D5 先例：只降字号，不改词）；实测译文起始 x=1518.8，ink 间隙 38.8px（改前 −0.4px）。
- **F1**（9 版）：`content56.py` P5 UND SIE 读者提示补第一问（eh 高度公式与 p.para 两处同改），两问式与 de-en/core 一致：
  - （各版新提示见下）
- **F1 跟进修复（P5 练习区横线，es/fr 首轮重建暴露）**：`content56.py:88` 的 `ey = 1756` 是 W47 D1 定值（当时 col-3 配图结束于 1732.9，横线 y=1744 可 clearance）。F1 使 UND SIE 框增高一行（+29px），配图说明下移，横线穿过说明 credit 行（occlusion LINEX 真报，非伪报）。**第一次尝试（失败）**：`ey = max(1756, cy5 + 24)` 让横线随图浮动——LINEX 消失，但 P5-ex 流柱高缩水、末块溢出（es 第二轮 FLOW OVERFLOW，P5-ex 末端 2682 > 2560）。**最终方案（横线上方回收空间，`ey` 恢复 1756，P5-ex 几何不变）**：
  - es/fr/it/ja/nl/pt（提示多 1 行）：配图间距 `iy5 = ey3 + eh + 26` → `+ 14`，图末端 1761.93 → 1749.93，credit ink 下余 ~8.6px。
  - ru（提示多 1 行 + F2 词表两词各多 1 行，共 +90px）：三处间距 26 → 10、配图高 313 → 280（caption 起点同步改 `iy5 + 280`），图末端 1822.99 → 1741.99，credit ink 下余 ~16.5px。
  - ko/zh-tw 提示换行数不变（0 行增长），图末端仍为 1732.93，无需改动。
  - 验算（单跑 content56.py）：es 图末端 1749.93、ru 图末端 1741.99，与设计值一致。
  - es：`¿Haces un calendario de Adviento? ¿Qué hay en tu lista de deseos? ¡Escribe en alemán!`
  - fr：`Fabriquez-vous un calendrier de l'Avent ? Votre liste de souhaits : qu'y a-t-il ? Écrivez en allemand !`
  - it：`Costruisci un calendario dell'Avvento? Cosa c'è nella tua lista dei desideri? Scrivi in tedesco!`
  - ja：`アドベントカレンダーを作る？願い事リストには何を書く？ドイツ語で2文書こう！`
  - ko：`어드벤트 캘린더를 만드나요? 소원 목록에는 무엇이 있나요? 독일어로 두 문장 써 보세요!`
  - nl：`Knutsel je een adventskalender? Wat staat er op jouw verlanglijst? Schrijf in het Duits!`
  - pt：`Fazes um calendário do Advento? O que há na tua lista de desejos? Escreve em alemão!`
  - ru：`Вы мастерите адвент-календарь? Что в вашем списке желаний? Напишите по-немецки!`
  - zh-tw：`你會做降臨節日曆嗎？願望清單上寫了什麼？用德文寫兩個句子！`
- **F2**（de-ru）：`content56.py:40` ADVENTSWÖRTER 词表：`der Wunschzettel — желания` → `список желаний`；`das Christkind — Младенец` → `Младенец Христос`（与同版 P5 注释、P8 答案 71/72 一致）。
- **F3**（de-fr）：`content12.py:221` P2 框标题 `La semaine` → `La semaine calme`，19pt（20pt 仍超框 0.5px advance / 0.2px ink；19pt ink 余 19.3px）；`content56.py:191` P6 框标题同改，24pt 不变（宽框）。
- **F4**（de-ru）：`content12.py:221` P2 框标题 `Тишина` → `Тихая неделя`，21pt（22pt 仍超框 6.2px；21pt ink 余 11.9px）；`content56.py:191` P6 框标题同改，24pt 不变（宽框）。
- **F5**（4 版）：`content12.py:43` P1 DIE WOCHE IN ZAHLEN 框补三句德文（抄 core）+ 各版读者语注释（拉丁版式配对；CJK 版用全角括号，与 core-de 一致）：
  - `5 — Punkte hat Deutschland nach vier Spielen in der Nations League …`
  - `20.30 — Anstoß Bayern gegen Köln am Freitagabend …`
  - `30 — Tore fielen am 9. Spieltag der Bundesliga …`
- **F6**（de-zh-tw）：`content7.py:71` 工具箱 + `content12.py:293` P2 配对题 key（P8 答案 25 由此派生）：`懺悔祈禱` → `懺悔祈禱日`。
- **F9**（7 拉丁版）：`content8.py:221` P8 答案串接 `"·".join(parts)` → `" · ".join(parts)`（与 core-de/ja/ko/zh-tw 源码一致）；en/es/fr/it/nl/pt/ru。

## 改后逐版（待填：重渲染 + 门禁复核结果）

（每版：改后印/网/text.md 尺寸+SHA 前 12；build_edition 全部门禁；boxtitle/spill/edge/head_check/census；F7/F8 实测值；P1/P5/P7/P8 目视结论；KIT 更新记录。）

### de-en — DONE（F9）

- 重建：`build_edition.py en`，**ALL GATES PASS**（run 0 FLOW OVERFLOW / 0 HEAD TOO WIDE, TOTAL 150；render；webpdf；verify TOTAL 150、编号连续、SVG byte-identical、style True、verbatim True、P8 floor True；occlusion 0 flags；p8 extract 150/150、compare CLEAN keydiff [137,138,139,150]；freeze exit 0，added CJK 7（均为 U+3000）；印/网文字层 default 50580B 完全相同、raw 49548B 完全相同；chips 141，P8 A2 22/B1 13；export 591 entries 150 exercises；P8 min span 9.94pt ≥ 9.75）。
- 改后：text.md 49942 B sha `7f6f56e355f3`；印 PDF 10350164 B sha `e861ff1d468d`；网 PDF 1510214 B sha `8638905f9014`。
- F9 核查：text.md 中 `)·` 0 处；P8 渲染图放大目视：`·` 两侧均有空隙（`back) · 2.`、`Monday) · 3.` 等）。
- P8-keys flow ends 2442（改前 2481），余 118px，无溢出。
- 三门禁（2026-11-12 15:00）：boxtitle 46 titles / 0 DEFECT / 0 OBSERVE；spill_sweep 0 SPILL（84 OBSERVE，含 P7 一处 −26.39px observe 注记，属既往）；pdf_edge_scan 8 页 0 TOUCH / 0 NEAR；D5 census PASS（D5_lat=0 D5_cyr=0 curly_cjk=0）。
- text.md 干跑核查：与修前快照比对，变更 9 行（1 行 D5 期 gloss + 8 行 P8 F9），丢行 0；盘上文件与干跑字节一致。

## 导出器陷阱核查（2026-11-12 15:00，协调员补充任务）

ru 家发现：`ru_textmd.py` 的 `do_p_text` 只收 sans 粗体 ≥24pt 的标题，D5 后缩到 22/23pt 的框题会在重导出时丢行，须干跑到 /tmp、diff、逐字回补。de 家核查结果：

- **de 导出器无此规则**：`export_text_lang.py` + `stub_svg.py`（`Page.text` 无条件记录）+ `stub_bslib.py`（`head`/`boxtitle`/`shead` 无条件记录）——无字号过滤。
- **实证**：`verify_textmd.py`（本 scratch 目录）对 10 版逐版干跑导出到 `tmp/dryrun/`、与修前快照 `pre-textmd/`（D5 baseline 副本，SHA 与 PROOF-NOTE 一致；en 的快照为 rebuild-6 版，与真修前差 1 行 P4 gloss）逐行比对：**10 版真正丢行均为 0**；变更行数与有意修复一一对应（en 9、es 10、fr 12、it 10、ja 4、ko 4、nl 10、pt 10、ru 16、zh-tw 6；en/es/fr 的盘上文件已与干跑字节一致）。
- 10 版重建后已复跑 `verify_textmd.py`：盘上文件与干跑字节一致、丢行 0（见门禁复核汇总表）。修前快照保留在 `pre-textmd/`。

### de-es — DONE（第三轮/第四轮，ALL GATES PASS）

- 首轮：`build_edition.py es` 除 occlusion 外全过（TOTAL 150；p8 CLEAN；freeze；印/网文字层一致；chips 141；export 591 entries）。occlusion 1 flag LINEX：P5 配图 credit 行被固定横线 y=1744 穿过——F1 增高所致（见上文跟进修复）。
- 第二轮（ey 浮动方案）：FLOW OVERFLOW（P5-ex 末端 2682 > 2560）+ occlusion TEXTX——ey 下移方案作废，已改回 1756、改间距回收。
- 第四轮（15:03–15:15，间距方案）：**ALL GATES PASS**。P5 col3 image ends 1749.93（设计值一致），occlusion 0 flags；p8 CLEAN；印/网文字层一致；chips 141；export 591 entries。
- 改后：text.md 50430 B sha `a10745854e27`；印 PDF 10354400 B sha `2286ca8be3f3`；网 PDF 1514438 B sha `dd6b52264ee1`。

### de-fr — DONE（除 1 空格旧 quirks 外全过）

- 首轮：同 es 的 LINEX（P5 credit 行被 y=1744 横线穿过），另 `print/web raw normalised identical` FAIL：印 50018B vs 网 50019B，唯一差异为 `früh→`（印）vs `früh →`（网）——D5 RUN-LOG 已记录的 fr poppler 分组旧 quirks（非空格字符数一致、零词丢失），与本次修复无关（该串为未动的 P8 答案注释）。
- 第二轮（15:15–15:25，间距方案）：occlusion 0 flags，P5 col3 image ends 1749.93；p8 extract 150/150、compare CLEAN keydiff [137,138,139,150]；chips 141；export 591 entries；P8 min 9.94pt；印/网 default 文字层 51088B 完全相同。**唯一未过**：`print/web raw normalised identical`（50018B vs 50019B，同一处 `früh→`/`früh →`）。
- 单独重建 webpdf 一次再验（15:32）：raw 差仍在同一位置、非空格字符仍一致——该 quirks 为稳定的 poppler 分组 artifact，非本次修复引入，按 D5 先例接受（不改源码、不动 PDF 结构）。
- 改后：text.md 50367 B sha `9c66b0945bba`；印 PDF 10352516 B sha `c0db47831b17`；网 PDF 1512555 B sha `a1b12f828e4a`（webpdf 重建后实测值）。
- **中断记录**：run_rest4 循环于 15:28 VM 重启时被杀（it 重建中途，build-it.log 0 字节），es/fr 已完成不受影响；余下 6 版以 run_rest5 重起。

### de-it — DONE（F7+F8+F1+F9，ALL GATES PASS）

- 重建 15:35–15:38：`build_edition.py it`，**ALL GATES PASS**（TOTAL 150；occlusion 0 flags；p8 CLEAN；印/网文字层一致；chips 141；export 591 entries；P8 min 9.94pt）。
- 改后：text.md 50025 B sha `2bc2080597e1`；印 PDF 10348810 B sha `c6643394c3c5`；网 PDF 1508853 B sha `352bd66ae305`。
- F7：kicker → `IL TEDESCO DEI TEDESCHI`，advance 间隙 23.6px（≥10px）；P1 顶栏渲染图目视：WOCHE VOM 前有清晰空隙。
- F8：横幅 27→24pt，ink 间隙 38.8px（≥4px）；PNG 列分析 1 空列（headline ink 止于 col 1489，译文始于 col 1491）；横幅渲染图目视 "!" 与 "TORNA LA BUNDESLIGA" 明显分离。
- F1/F9：P5 提示 3 行渲染正常；P8 `)·` 0 处、`) · ` 142 处。
- 跟进：P5 image gap 26→14（image ends 1749.93）。
- 三门禁：boxtitle 44 titles / 0 DEFECT / 0 marginal；spill 0 SPILL；edge 0/0；census-patched PASS；head_check PASS；text.md 干跑 diff 10 行、丢行 0。

### de-ja — DONE（F1+F5+P1 流量修复，ALL GATES PASS）

- 首轮重建失败：FLOW OVERFLOW [P1-headline] col 2 y=1738 need 107 bottom 1828；flow 末端 1921；occlusion 11 flags（全在 p1-front.svg）。根因见下文 P1 流量修复节。
- 修复后重建 16:32–16:37：**ALL GATES PASS**。P1-headline flow ends 1554（与 es/fr/ko/zh-tw 一致）；occlusion 0 flags；p8 CLEAN；印/网文字层一致；chips 141；export 591 entries。
- 改后：text.md 52118 B sha `15aa6bc8921b`；印 PDF 15960325 B sha `1b91ff1f9ca0`；网 PDF 1935367 B sha `dfb0c403f2f4`。
- F5：P1 数字框三句德文 + 读者语注释已在印 PDF 实测可见（×1）；P1 数字框渲染图目视：德文句 + 注释在奶油框内、无溢出。
- 三门禁：boxtitle 52 titles / 0 DEFECT / 1 marginal（P7 toolbox +1.0px，D5 已记的既往）；spill 0 SPILL；edge 0/0；census-patched PASS（P5 cjk_sans +2 = F1 提示拉长所致的 run split，见普查节）；head_check PASS；text.md 干跑 diff 4 行、丢行 0。

### de-ko — DONE（F1+F5，ALL GATES PASS）

- 重建 15:44–15:51：**ALL GATES PASS**（P1-headline flow ends 1554；occlusion 0 flags；p8 CLEAN；印/网文字层一致；chips 141；export 591 entries）。
- 改后：text.md 51701 B sha `0d17881f6154`；印 PDF 12926530 B sha `be2444232568`；网 PDF 1791578 B sha `49223ed15613`。
- F5：三句德文 + 注释在印 PDF 实测可见（×1）；P1 数字框无溢出（ko 的框 7 行、fits col 1）。
- 三门禁：boxtitle 65 titles / 0 DEFECT / 0 marginal；spill 0 SPILL；edge 0/0；census-patched PASS（P5 cjk_sans +2，同 ja，F1 run split）；head_check PASS；text.md 干跑 diff 4 行、丢行 0。

### de-nl — DONE（F7+F1+F9，ALL GATES PASS）

- 重建 15:51–15:58：**ALL GATES PASS**。
- 改后：text.md 49713 B sha `551f278a1026`；印 PDF 10347239 B sha `6a452b7accfb`；网 PDF 1507275 B sha `3c0e337e55b4`。
- F7：kicker → `HET DUITS VAN DUITSERS`，advance 间隙 31.0px；P1 顶栏目视无叠字。
- F1/F9：P5 提示 3 行；P8 `)·` 0、` ) · ` 142。
- 跟进：P5 image gap 26→14（image ends 1749.93）。
- 三门禁：boxtitle 44 / 0 DEFECT / 0 marginal；spill 0；edge 0/0；census-patched PASS；head_check PASS；干跑 diff 10 行、丢行 0。

### de-pt — DONE（F7+F1+F9，ALL GATES PASS）

- 重建 15:58–16:05：**ALL GATES PASS**。
- 改后：text.md 50121 B sha `2e2ce4689359`；印 PDF 10354705 B sha `55e95caf7bcb`；网 PDF 1514735 B sha `c62f38ea0c65`。
- F7：kicker → `O ALEMÃO DOS ALEMÃES`，advance 间隙 31.9px；P1 顶栏目视无叠字。
- 其余同 nl（P5 gap 26→14；image ends 1749.93；F9 142 处）。
- 三门禁：boxtitle 42 / 0 DEFECT / 0 marginal；spill 0；edge 0/0；census-patched PASS；head_check PASS；干跑 diff 10 行、丢行 0。

### de-ru — DONE（F1+F2+F4+F5+F9+P1 流量修复，ALL GATES PASS）

- 首轮重建失败：FLOW OVERFLOW [P1-headline]（col 2 y=1953 need 75）；flow 末端 1921；occlusion 9 flags（p1-front.svg）。根因见 P1 流量修复节。
- 修复后重建 16:37–16:41：**ALL GATES PASS**。P1-headline flow ends 1554；occlusion 0 flags；p8 CLEAN；印/网文字层一致；chips 141；export 591 entries。
- 改后：text.md 56776 B sha `28db7a67610c`；印 PDF 10624220 B sha `dda94ec32ed3`；网 PDF 1770599 B sha `b9971c845e0f`。
- F2：印 PDF 中 `список желаний` ×5、`Младенец Христос` ×4；F4：`Тихая неделя` ×4；F5：三句德文 ×1；F1：P5 提示 3 行；F9：` )· ` 0、` ) · ` 142。
- 跟进：P5 三 gaps 26→10 + image 313→280（caption 同步 iy5+280；image ends 1741.99，credit 余 ~16.5px）；P1 box 18pt + bridge 19pt。
- 三门禁：boxtitle 46 / 0 DEFECT / 0 marginal；spill 0；edge 0/0；census-patched PASS（见普查节的 D5_cyr 假警说明）；head_check PASS；干跑 diff 16 行、丢行 0。
- P5 col3 渲染图目视：F1 提示 3 行、F2 两词各 2 行、配图（280px 明显更短）+ caption + credit 与横线有可见空隙。

### de-zh-tw — DONE（F1+F5+F6，ALL GATES PASS）

- 重建 16:09–16:14：**ALL GATES PASS**。
- 改后：text.md 49291 B sha `c2d3f679b8c5`；印 PDF 11837604 B sha `6658366039a8`；网 PDF 1938383 B sha `9b83129c7472`。
- F5：三句德文 ×1；F6：`懺悔祈禱日` ×7（P7 toolbox、P2 key、P8 答案 25）；F1：P5 提示（wrap 行数不变，0 行增长）。
- 三门禁：boxtitle 48 / 0 DEFECT / 1 marginal（P7 toolbox +1.0px 既往）；spill 0；edge 0/0；census-patched PASS（P5 cjk_sans +0，与 wrap 模拟一致）；head_check PASS；干跑 diff 6 行、丢行 0。

## 跟进修复 2：P1-headline FLOW OVERFLOW（ja/ru，F5 数字框；2026-11-12 ~16:30 发现）

- 现象：ja/ru 首轮重建 FLOW OVERFLOW [P1-headline]（ja col 2 y=1738 need 107 bottom 1828；ru y=1953 need 75），flow 末端 1921；occlusion ja 11 / ru 9 flags，全在 p1-front.svg（溢出的习题撞上 P1-fussball 流）。
- 根因（trace_p1.py 追踪 Flow 方法逐块打印 (ci, y)）：F5 后的数字框 20.5pt 为 9 行、total+gap 402px。ja 中框在 col 1 y=1440 起（剩余 388 < 402）→ 整框 COLUMN BREAK 到 col 2，浪费 388px；随后 head + 6 习题溢出 col 2。es 的框 7 行（~346px）fits col 1（ends 1815）。5 段 lead paras 在各版 wrap 完全一致（39 行）；框是唯一差异。ru 的 bridge 更高（208px/6 行 vs ja 148px/4 行），框起于 y=1500（剩余 328）。
- 修复（已应用，文字不变故 text.md 不受影响）：ja + ru P1 数字框 items 20.5pt → 18pt（box total+gap 339.4px）；ru 另 bridge 20.5pt → 19pt（`f.bridge(..., size=19)`；ru bridge 6→5 行，208→166px，框起点上移 42px）。重追踪：ja 框 col 1 末端 y=1780（余 48px），ru y=1797（余 31px）；两版 P1-headline flow 均 ends 1554（与 es/fr/ko/zh-tw 相同），无溢出。
- 重建 ja + ru（run_rest6.sh）：两版 ALL GATES PASS（ja 16:32–16:37，ru 16:37–16:41）。
- 教训：跟进修复 1 的 ey 浮动方案已作废（见上文）；本修复只动字号、不动 flow 几何，P5-ex 不受影响。

## F7/F8 实测值汇总（verify_f7f8.py；对照 de-en kicker 间隙 14.5px）

| 版 | F7 新 kicker | advance 间隙 | 判定 |
| es | EL ALEMÁN QUE LEEN | 49.6px | PASS ≥10px |
| fr | L'ALLEMAND D'ALLEMAGNE | 18.4px | PASS |
| it | IL TEDESCO DEI TEDESCHI | 23.6px | PASS |
| nl | HET DUITS VAN DUITSERS | 31.0px | PASS |
| pt | O ALEMÃO DOS ALEMÃES | 31.9px | PASS |

- 测量方法：各版自带 svglib（text_w + 1.7×(len−1)，右缘 = 975+total/2）；方法以 PROOF-NOTE 校准（advance 与 proof ink 值差恒定 ~1.7px = 末字形 bearing）。SVG first-run x 与计算左缘逐版吻合。P1 顶栏渲染图 5 版均已目视：WOCHE VOM 前有清晰空隙。
- 拒选记录：fr `L'ALLEMAND DES ALLEMANDS` 仅 5.8px——未采用。
- F8（de-it）：横幅 27→24pt，ink 间隙 38.8px（≥4px）；PNG 列分析 1 空列（headline ink 止 col 1489，译文始 col 1491）；渲染图目视分离。
- 关键修正：刊期右缘 RIGHT=1862（bslib4 注释误写 1885）；刊期 x=1447.4 未动。

## D5 普查复核（census_patched.py；2026-11-12）

- **纠正**：我最初的 replication（census.py）误用了 PRODUCTION 普查 schema（D5_cyr = CJK 字体元素内的西里尔文），报 ru D5_cyr=84。权威的 D5 后 patched census（scratch-d5-de/de-ru/census-patched.json，D5 RUN-LOG 记 "census 0" 的门）已完全去掉 d5_* 键——只跟踪 elements/newsreader/cjk_sans/noto_sans（仅 ru）/curly_total/curly_in_newsreader。西里尔文跑在 "Noto Serif CJK SC"（masthead subtitle、gloss 词）是 ru 版 by-design 的路由，patched baseline 本身即如此。
- **census_patched.py 结论：10 版全部 PASS**（cjk_sans 与 patched baseline 逐页一致，除 ja/ko P5 +2，见下；curly_cjk=0 各版）。
- ja/ko P5 cjk_sans +2：F1 提示拉长所致——20pt sans、宽 378.5 下 _runs 模拟：ko 提示 sans-runs 10→12，ja 2→4，zh-tw 2→2（+0，与实测 zh-tw +0 一致）。非路由变化。
- 系统性 p5/p7 curly 元素差（6→5、21→20）：10 版全有，包括源码未动的 en——重建间 run-split 抖动（或 census 方法差异），非本次修复所致；证据：(a) en 的 P5/P7 源码从未动过，仍有同样差值；(b) curly 字符数改前/改后逐版逐页完全一致（en 70=70，其余 66=66）。
- CJK 版用 locale 字体（"Noto Sans CJK JP/KR/TC"）——census_patched.py 计入任何 "CJK"+"Sans" 族。
- 注：de-en 节所记 "D5 census PASS（D5_lat=0 D5_cyr=0…）" 为旧 replication schema 的数字，已由本节的 patched-schema 结论取代（结论同为 PASS）。

## 门禁复核汇总（2026-11-12，10 版）

| 门禁 | 结果 |
| build_edition.py 全部门禁 | 10/10 PASS（fr 除 1 空格旧 quirks 外全过；ja/ru 首轮 P1 溢出已修复后重建通过） |
| boxtitle_check | 10/10：0 DEFECT（en 46、es 48、fr 44、it 44、ja 52、ko 65、nl 44、pt 42、ru 46、zh-tw 48 titles；fr/ja/zh-tw 各 1 marginal，均为 D5 已记的 P7-toolbox +1.0px 既往） |
| spill_sweep | 10/10：0 SPILL（84–142 OBSERVE 候选） |
| pdf_edge_scan | 10/10：8 页 0 TOUCH / 0 NEAR |
| head_check.py（build.log） | 10/10：PASS 0 defects |
| D5 census（patched schema） | 10/10：PASS（见上节） |
| p8 compare | 10/10：CLEAN（keydiff [137,138,139,150]） |
| occlusion_audit | 10/10：0 flags（终版） |
| text.md 干跑核查 | 10/10：丢行 0，盘上文件与干跑字节一致；变更行数 = 有意修复（en 9、es 10、fr 12、it 10、ja 4、ko 4、nl 10、pt 10、ru 16、zh-tw 6） |
| F7/F8 advance + 目视 | 5/5 kicker PASS（18.4–49.6px）；F8 ink 38.8px PASS；P1 顶栏/横幅渲染图 6 版目视通过 |
| F1–F6 印 PDF 实测 | 全部确认（见各版节；pdftotext 须 space-insensitive 匹配——1.7 letter-spacing 会拆分 kicker 字母与撇号旁空格） |
| F9 P8 放大核对 | en P8 zoom 目视通过；7 版 `)·` 0、` ) · ` 141–142 |

## KIT 更新记录（2026-11-12）

- 脚本：本目录 `update_kits.py`（tools/venv python 运行；先备份 10 份 KIT 到 /tmp/kit-backup-\<lang\>.md）。
- 10 版 WEEKLY-KIT.md 的 §5/§2 Deliverables 块已更新为重建后盘上实测值（印/网/text.md 尺寸 + 完整 SHA-256 + 文字层字节数 + 字符数），标签改为 "reproof fix rebuild, 2026-11-12; D5 superseded"；text.md 注释由 "(**unchanged**…)" 改为 "(changed — wording fixed per the §7 reproof fix entry…)"。
- 各版新增历史条目：Format A（en/es/fr/it/nl/pt/ru）为 §7 "### Reproof fix rebuild (2026-11-12 — rebuild 8)"；ja/ko 为 §6 D5 条目后的 "- **Reproof fix rebuild (2026-11-12)**" 条目；zh-tw 为新 "## §10 Reproof fix rebuild (2026-11-12)"。
- 校验：10 版旧印 PDF SHA12 在 KIT 中出现 0 次、新 SHA12 出现 2 次（Deliverables 块 + 历史条目）；Deliverables 标签 10/10 为新标签；ru 的网 PDF 注释行（Cyrillic font subsets）原样保留；历史条目未动。
- 过程插曲：首版脚本的切片 bug 使 Format A 的标签行被旧值覆盖——发现后以独立补丁脚本逐版修正并重新校验 10/10（见上条校验）。

## 9 条状态总表

| 条 | 版 | 状态 |
| F7（major） | es/fr/it/nl/pt | 全部修好：kicker 缩短，advance 间隙 18.4–49.6px（≥10px），P1 渲染图目视无叠字 |
| F8 | it | 修好：横幅 24pt，ink 间隙 38.8px，1 空列，目视分离 |
| F1 | es/fr/it/ja/ko/nl/pt/ru/zh-tw | 全部修好：P5 提示补上降临节日历一问，印 PDF 实测可见；P5 配图跟进修复已完成（es/fr/it/nl/pt gap 26→14；ru gaps 26→10 + image 280；ko/zh-tw 无需动） |
| F2 | ru | 修好：`список желаний` ×5、`Младенец Христос` ×4 |
| F3 | fr | 修好：P2+P6 `La semaine calme`（19pt/24pt），印 PDF ×3 |
| F4 | ru | 修好：P2+P6 `Тихая неделя`（21pt/24pt），印 PDF ×4 |
| F5 | ja/ko/ru/zh-tw | 全部修好：三句德文 + 注释，印 PDF ×1 各版；ja/ru P1 流量溢出已修复（box 18pt；ru bridge 19pt），flow ends 1554 |
| F6 | zh-tw | 修好：`懺悔祈禱日` ×7（P7、P2、P8-25） |
| F9 | en/es/fr/it/nl/pt/ru | 全部修好：`·` 前后空格，` )· ` 0、` ) · ` 141–142；en P8 zoom 目视通过 |

**结论：9 条全部修好；10 版全部重建、全部复核通过（fr 仅剩 D5 已记的 1 空格 poppler quirks，接受不追）。无 commit、无 push、无 lint；只动了 de 家 10 版目录 + 本 scratch 目录。**

## 备注

- zh-tw P1-headline flow：改前直接跑 `content12.py` 得 1378，KIT 所记 1503（build 1/rebuild-B）——改前已存在的差值，与本次修复无关；重建后 run.py 实测为 1554（与 es/fr/ko/ja/ru 一致），已解决。
- F3/F4 的 P2 框标题降至 19pt/21pt，低于 boxtitle_check 22pt 检测下限（D5 先例：pt 21pt、nl 20pt 标题同样以下限外直接量度核验）；已用 PIL ink 实测（fr 19pt 余 19.3px、ru 21pt 余 11.9px），复核时另以 boxtitle（其余标题）+ 渲染图目视确认。
