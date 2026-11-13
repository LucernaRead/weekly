# GATE-LOG — 2026-W47 · nl → de · proof1 机械门实跑证据

复校员独立实跑，不信 KIT，只信自己跑的结果。全部命令用 `tools/venv/bin/python`；
TMPDIR 全程指向本 scratch 下 `tmp/`（系统 /tmp 512M 常满，未用）。
工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-de1/`。
源码见 `gates.log`、`occlusion.json`、`p8-extract.json`、`p8-compare.json`、`freeze-diff.json`、
`freeze-baseline/`、`creambox-all.log`、`boxtitle.log`、`content-edge.log`、`pdfspan.log`、`pdfedge.log`、
`pixelscan2.log`、`measure.log`、`italic.log`、`print.txt`、`web.txt`、`render-p1.png`…`render-p8.png`。

## §0 身份核对（磁盘为准）

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0；scratch 写入探针文件成功。
- creambox.py md5 `ee7a55d8b2057cf4ad42a97bb1197383`，与任务一致。
- 印 PDF `De-Lucerna-VOL4-nl-de.pdf`：SHA `0df8e6146159d4592fe1925472dd42f3aa6181f3db1fb50508c08bf0cd7fc13e`，12,669,843 字节——**与任务一致**。
- 网 PDF `De-Lucerna-VOL4-nl-de-web.pdf`：SHA `8859e18a23b46d84d20fe52015e7e5e19d9ec168142eeee13e96de3bdef8de64`，1,581,124 字节——**与任务一致**。
- text.md `2026-w47-nl-de.text.md`：SHA `1531c25ee6ec4844681a4f6581b5c7ad5b959348cdd20c2dd884b7374f7a00d2`，46,161 字节——**与任务一致**。
- 任务数字与磁盘无出入，本节无 §0 差异。

## §1 几何遮挡审计（tools/occlusion_audit.py）

- 命令：`./tools/venv/bin/python tools/occlusion_audit.py <edition>/svg --core <core-nl>/svg --json occlusion.json`
- 结果：**0 flags**（edition 与 core 均为 0，NEW vs core 0）；合成自检通过（6 类 planted flags 全触发，clean 对照静默）。RC=0。
- 局限（任务已提示）：该工具只核查带边框盒的 BOXTITLE 类；无边框奶油盒标题横向溢出不在其覆盖内——本版 D1/D2 正属此类，由 §2–§3 的独立实测检出，不得以 occlusion 0 为放过理由。

## §2 正典 creambox.py 全版扫描（+45px 窗口 + 逐行 clearance + P7 toolbox）

- 命令：`./tools/venv/bin/python <goals>/hidden_files/w47/tools/creambox.py <edition>/svg/*.svg` → `creambox-all.log`（318 行）。
- 结果：全部盒内行 clearance 为正；仅 2 处「last baseline」负值，均为盒下相邻标题的已知假阳性：
  - P1 IN DEZE EDITIE 盒（bottom 1652）：盒内末行 baseline 1636，clearance +16.0，desc-clear +9.7；+45 窗口内下一行「HET WOORD VAN DE WEEK」baseline 1676（+24.0）。
  - P2 四词盒组（bottom 1768）：盒内末行 baseline 1756.6，clearance +11.4，desc-clear +5.7；窗内下一行「Let op: schrijf je gedicht…」baseline 1800（+32.0）。
- **P7 toolbox 实测**：3 个盒，min inside clearance **+12.5**，min desc-clear **+6.5**（末行「Gruppe zieht ins Viertelfinale ein.」baseline 1328.5，盒底 1341.0）。任务必查项 (c) 未复现。
- P3/P5 右栏奶油盒末行：P3 SINTERKLAAS IN CIJFERS 盒末行「november.」baseline 1090.4，clearance +16.2，desc-clear +9.8；P2 四词盒末行 desc-clear +5.7；PDF span 底缘复核（§3）全部在盒内。任务必查项 (b) 未复现。

## §3 框标题 / 版心右缘实测（PIL 真墨水 + 印 PDF span + 200 dpi 像素扫描，三法）

- 自写脚本 `boxtitle_audit.py`（PIL getbbox 真墨水，含 letter-spacing；Noto Sans CJK SC index 2、Newsreader Regular/SemiBold）+ PyMuPDF span 检查 + 200 dpi 像素扫描（`pixelscan2.log`，仅裁切右缘条带渲染，避开大内存）。
- **D1**：P1「IN DEZE EDITIE　IN DIESER AUSGABE」— PIL +33.5 px / PDF span +33.9 px / 像素 +31.7 px。核心同标题仅 296 px（右缘 1757.5），合规。
- **D2**：P6「VOOR OF TEGEN?　DAFÜR ODER DAGEGEN?」— PIL +47.5 px / PDF span +48.3 px / 像素 +47.0 px。核心同标题仅 326 px（右缘 1787.5），合规。
- **D3**：P2 选项 c「c. eten voor het paard van Sinterklaas」— PIL +8.5 px / PDF span +13.1 px / 像素 +11.5 px。核心同文同位，核心亦然（归属核心）。
- **排除的 PIL 假阳性**（13.5/15.5/19.5 pt 非整数字号被 PIL 取整放大所致，像素扫描已翻案）：P4 图注（像素：盒内，余 1.5 px）、P8 答案行 114/132/134（像素：盒内，余 10.6/3.4/1.9 px）、P8 答案头（像素：+0.9 px，噪声）。
- 其余右缘：页脚「Seite N von 8」+0.3–0.4 px、P1 刊首日期行 +0.2 px 墨水、P2「Welche Wörter…」+0.4 px 墨水——均为噪声，不计。
- 左缘：全部 left=87.0 标记皆为首字形侧轴承 1 px（栏位 x=88 設計值），不计。
- P2「MERK ES DIR」：PIL +0.5 px / PDF span +1.0 px——见 PROOF-NOTE O2（不计缺陷）。

## §4 p8 compare（显式 --core-p8/--edition-p8；--total 150）

- 命令：`p8.py compare --core-p8 <core-nl>/svg/p8-toets.svg --edition-p8 <edition>/svg/p8-toets.svg --total 150`
- 结果：**CLEAN**，core 150 noted / edition 150 noted，missing=[]，extra=0，uncertain=[]，**keydiff=[137, 138]**。RC=0。
- keydiff 裁决：137、138 为 E 节翻译题（NL→DE），键合法重定向到读者语；键本身正确（137「Das Sinterklaasjournaal läuft jeden Tag um 18:00 Uhr.」；138「Die ersten beiden ziehen ins Viertelfinale ein.」）。139、140（DE→NL）键与核心一致。非缺陷。
- `p8.py extract --p8 <edition>/svg/p8-toets.svg --total 150`：**noted set = 150 of 150**。RC=0。
- 另：text.md 键与印刷版 P8 键逐题比对 **0 不符**（150 题，含 137–140 全句比对、150 题 ✓ 标记）。

## §5 freeze / freeze_direct 8/8

- `freeze.py baseline --build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg --out <scratch>/freeze-baseline`：**8/8 SVG byte-identical**，核心 8 文件重哈希确认未被改动。RC=0。
- `freeze.py diff --core-svg <core-nl>/svg --edition-svg <edition>/svg`：p1 +27/−48 … p8 +183/−676；**新增 CJK 仅 7 个 U+3000**（每页 1 个，p1 为 0——p1 的 U+3000 在核心已存在）。U+3000 是 SOP §1.1 规定的全角空格分隔符（「不用·做分隔，用全角空格」），非中文文本。RC=0。
- 移除串核查：全部含拉丁字母的移除串，其词元均在同页新增串中重现；惟二例外已裁定：（a）刊头「LUCERNA DUTCH WEEKLY」→ 德语刊头副标（fan-out 设计）；（b）「perfectum」→ 德语「Perfekt」（P8 答案注 40/42「ontvangen Perfekt」「lezen im Perfekt」），讲解层合法翻译，非核心丢失。
- 方法备注：`tools/freeze.py` 只有 `baseline`/`diff` 两个子命令，无 `freeze_direct` 子命令（与任务注记一致）——记为方法备注，不当缺陷。
- 附：核心 P8 的「perfectum」为中文答案注里的荷兰语语法词，共 2 处；本版德语注用「Perfekt」，正确。

## §6 keycheck 150/150（逐题手验）

- `keycheck-150.json`：150 题逐题手验，**150/150 ok，0 不符**。方法：text.md 全文通读 + 印 PDF 8 页目视；配对题字母对照印刷版 a–d 列表（P2 D：a 列表/b 诗/c 食物/d 门口；P8 F：a 诗/b 新闻节目/c 小组头名/d 门口）；算术重算；范文计词。
- 外部核实：PSV 26 分（题 63、126）见 §10；其余键均由文内事实直接支撑。

## §7 印/网文字层比对

- `pdftotext -layout` 印版 105,802 B / 网版 105,809 B；归一化（空白折叠）diff **为空**；逐页核对 P1 834/834 … P8 2255/2255 与 KIT 所述一致（未采信 KIT，以上为自跑结果）。
- **D5**：网 PDF 斜体丢失（见 §8）；其余两项（空格丢失、闭引号脱离）未复现。

## §8 斜体三联症（ru-en D3 同类）+ P8 最小字号实测

- PyMuPDF 全书 span 扫描：印版 italic span **1 处**（P1「«de groepswinst»」，Newsreader Italic 16.12 pt）；网版 italic span **0 处**，同词改用 LucernaNewsreader-Regular（宽 131.1 pt vs 印版 122.2 pt）。→ D5（轻微）。
- P8 最小字号实测（PyMuPDF 逐 span）：**10.12 pt**（174 个 span）；次小 10.35 pt。KIT 所述 10.12 属实。SOP §1.1 让步阶梯允许降至 9.75 pt，10.12 合规，非缺陷。

## §9 弯引号全版扫描 + E 节 type 标签本地化 + text.md 残留中文

- SVG 全版：U+201C=1、U+201D=0、U+2019=0、U+201E=1——唯一一对为 P1「„Gruppensieg"」，合法德语引号对（U+201E 开、U+201C 闭）。核心为 U+201C=1、U+201D=1、U+201E=0（核心的引号对在讲解层替换中消失）。无误用。
- text.md：U+201C=1、U+201E=1（同上）；U+2019=0。`'s avonds` 等用直引号 U+0027，与核心一致；KIT 所述 U+2019 间距现象在渲染中与核心相同，非缺陷。
- E 节 type 标签：已本地化——`übersetzen`、`Ins Deutsche übersetzen`、`Ins Niederländische übersetzen`；其余 type 词亦为德语（Einsetzen、Richtig oder falsch?、Bilde den Satz、Schreiben）。无「翻譯」/「翻译」残留。任务必查项 (d) 的 type 标签部分未复现。
- **但 text.md 答案标记未本地化**：CJK 字符共 300 个，全为「答/案」——「— 答案：」142 处 + 配对题「(答案 x · …)」8 处 = 150 处。→ D4（重大）。对照：nl 全家 10 版各 142 处、核心 168 处；en-fr 用「— Correct:」，de-en/fr-de/es-de 均为 0 处「答案」。
- SVG 内 CJK：仅 U+3000（118 处）+ 刊头三色蛾标记「三色蛾」（P1，核心亦有 1 处，同 SOP §1.1 刊头蛾标）。

## §10 外部事实来源（2026-11-11 检索）

- **PSV 26 分**（题 63、126）：VAVEL Eredivisie standings 2026/27（2026-11-08 更新）：「Leaders: PSV, 26 points; 12 of 34 matchweeks played」；PitchLab：「PSV Eindhoven are 1st … with 26 points from 12 games. Latest result 5–2 win at Cambuur on 8 Nov」；Sports Mole 表格 PSV 12 战 8-2-2、40:15、26 分。——属实。另证实 P4「Cambuur – PSV 2–5」与「Speelronde 13: NEC – PSV 21 Nov 16:30」（15:30 UTC = 16:30 CET）。
- **Grave 入城**（P1/P3）：vandaagingrave.nl：Landelijke intocht 2026 in Grave，14 november 2026 周六，Maaskade，市长 Marieke Moorman，NPO Zapp (NPO 3) 直播，Merel Westrik 主持；kidsproof.nl：节目 12:00–16:00，约 12:00 靠岸 Maaskade；mamaliefde.nl：同上 + Pakjesavond 2026-12-05 周六；ozosnel.nl：马名 Ozosnel。——全部属实。
- **下期预告欧战**（P7 VOLGENDE WEEK）：UEFA.com 2026/27 Champions League 赛程：Matchday 5，Tuesday 24 November 2026，Feyenoord vs Porto、Real Madrid vs PSV Eindhoven。——属实。
- **日期/星期**：`date -d` 核验（Europe/Amsterdam）：2026-11-14 周六、11-15 周日、11-16 周一、11-21 周六、11-22 周日、11-24 周二、11-29 周日、12-05 周六——与文中全部星期表述吻合。

## §11 其他核查

- 全文通读：text.md 全文 + 印 PDF 8 页逐页目视（自渲染 150 dpi，`render-p1.png`…`render-p8.png`）。无溢出/重叠/压页脚/图片问题（除 D1/D2/D3 外）；8 张图片均带目标语图说 + CC0 出处（Wim van Rossem/Anefo、Anefo、W. Punt/Anefo、Spaarnestad Photo/Wikimedia Commons、Elise lovenko/Unsplash、Cristina Gottardi/Unsplash、Aaron Burden/Unsplash）。
- P7 金句 8 条逐字出自本期正文，页码标注正确（P1×2、P2、P3、P4、P5、P6×2）。
- ABSTRACT.txt：德语单行 309 字节，无 ASCII 双引号，含刊名/目标语/150 题/A2–B2/德语讲解。
- P8：答案 1–150 齐全，末行 ink baseline 2548.5 上方、页脚线 y=2596 下方留空；范文 81 词（脚本计数，80–100 内）。
- P2 EN JIJ 盒末行距盒底仅 0.4–0.5 pt（紧但在内）；P7 HET WOORD gloss 两行、止于行 B 规则上方（KIT 已接受）；P1 HET WOORD gloss 末行贴行 B 规则但未 crossing——三者皆不计缺陷。
- **未改动源文件**：无任何源文件改动/重建/commit/push。

## 附：工具与方法备注
- `freeze.py` 无 `freeze_direct` 子命令（见 §5）。
- 自写 `boxtitle_audit.py` 的 BOX-BOTTOM 标记为锚点换算错误所致的假阳性（getbbox y1 含 ascender），已由 PDF span 底缘 + 像素扫描翻案；BOX-RIGHT 标记经三法复核属实者已列为 D1/D2/D3。
- 2026-11-11 11:23 左右一次重复并行渲染调用致服务重启；已确认 8 张 150 dpi 渲染图完整落盘，其后 200 dpi 像素扫描改为逐条带裁切渲染、单次执行，完成。
