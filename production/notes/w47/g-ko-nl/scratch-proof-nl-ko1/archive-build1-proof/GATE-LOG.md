# GATE-LOG — 2026-W47 · nl → ko · proof1 机械门实跑证据

复校员独立实跑，不信 KIT，只信自己跑的结果。全部命令用 `tools/venv/bin/python`；
TMPDIR 全程指向本 scratch 下 `tmp/`（系统 /tmp 512M 常满，未用）。
工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-ko1/`。
源码见 `freeze-baseline.log`、`freeze-diff.json`、`freeze-diff.log`、`occlusion.json`、
`p8-extract.json`、`p8-compare.json`、`keycheck-150.json`、`creambox-all.log`、`boxtitle.log`、
`measure.log`、`pdfspan.log`、`pixelscan2.log`、`italic.log`、`print.txt`、`web.txt`、
`textaudit.log`、`render-p1.png`…`render-p8.png`、`zoom-p2-optc.png`、`zoom-p2-enjij.png`。

## §0 身份核对（磁盘为准）

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0；scratch 写入探针文件成功。
- 印 PDF `De-Lucerna-VOL4-nl-ko.pdf`：SHA `d72e53eb31c222fb3882b5644162a8292ec1a8ba0b3481b3b6099f98f710fed8`，17,281,555 字节——**与任务一致**。
- 网 PDF `De-Lucerna-VOL4-nl-ko-web.pdf`：SHA `a5b50f5985fa7da5dd213ece619c21004c9a4d8698a7c331e5dca64aeecac119`，1,884,427 字节——**与任务一致**。
- text.md `2026-w47-nl-ko.text.md`：开工时 SHA `bbca93462db80962c14bee566395aea8f3ba8f62d9570c99335ae718cbf92d33`，47,383 字节——**与任务一致**。**但校对中途 2026-11-11 11:53:08 UTC 该文件被并发重写**：当前磁盘 SHA `702e12429b09648655760352f966574f4483c5b63413d2d22a9ebd861f26683a`，47,525 B；标记改为 `— 정답： `（142 处）+ `(정답 x`（8 处），「答案」残留 0 处，Han 0。修复代理留下的 `scratch-fix-core-nl1/textmd-before/2026-w47-nl-ko.text.md` 的 SHA 就是 pinned 版 `bbca93462d…`；新旧两版标记归一化（정답→答案、去掉冒号后空格）后完全相同——通读结论可 1:1 平移。两 PDF 的 SHA 在收尾时复核仍与任务一致（未变）。
- 仅 text.md 被改；SVG（2026-11-11 05:08–05:09）、两 PDF（05:10/05:12）、ABSTRACT.txt、WEEKLY-KIT.md、content*.py 均未动——全部 SVG/PDF 门禁与测量仍然有效。
- 本节结论：三件 SHA 开工时与任务一致；text.md 的中途重写已记录并核对，不影响 pinned 版结论（D4 在 pinned 版成立）。

## §1 几何遮挡审计（tools/occlusion_audit.py）

- 命令：`./tools/venv/bin/python tools/occlusion_audit.py <edition>/svg --core <core-nl>/svg --json occlusion.json`
- 结果：**0 flags**（edition 与 core 均为 0，NEW vs core 0）；合成自检通过（6 类 planted flags 全触发，clean 对照静默）。RC=0。
- 局限（任务已提示）：该工具只核查带边框盒的 BOXTITLE 类；无边框奶油盒标题横向溢出不在其覆盖内——本版无此类问题（§3 已用真墨水排除）；对 P2 选项 c（D3）与 P4 积分榜缺失（D6）亦盲，不得以 occlusion 0 为放过理由。

## §2 正典 creambox.py 全版扫描（+45px 窗口 + 逐行 clearance + P7 toolbox）

- 命令：`./tools/venv/bin/python <goals>/hidden_files/w47/tools/creambox.py <edition>/svg/*.svg` → `creambox-all.log`（372 行）。
- 结果：全部**盒内行 clearance 为正**；仅 3 处「last baseline」负值，均为盒下相邻标题的已知假阳性：
  - P1 IN DEZE EDITIE 盒：+45 窗口内下一行「HET WOORD VAN DE WEEK」（+24.0）。
  - P1 y=1874 盒：+45 窗口内「BLIKSEMQUIZ」导语行（+44.0，与 BLIKSEMQUIZ 标题同基线 y=2348，x=1504，是盒下独立块；de 版同行在 x=1248.5、盒 x 范围外故未报）。
  - P2 四词盒组：+45 窗口内下一行「Let op: schrijf je gedicht…」（+32.0）。
- **P7 toolbox 实测**：3 个盒，min inside clearance **+12.5**，min desc-clear **+6.5**；PIL 逐盒余量 +12.4/+10.5/+27.1。任务必查项 (d) 未复现。
- P3/P5 右栏奶油盒末行降部：P5 EN JIJ 盒（y=632，bottom=965.5）creambox desc-clear −0.9 为**公式假象**（0.30×字号假设拉丁降部，该行是纯韩语）；PIL 真墨水 ink-bottom 962.4（余 +3.1 px），像素扫描底缘 961.9 px（余 3.6 px）。P3 SINTERKLAAS 盒末行 `november.` ink-bottom 1090.4（余 +16.2）；P4 盒 `18:45 uur.` 余 +14.2；P6 y=200 盒 `은이 100명)` 余 +3.1。任务必查项 (c) 未复现。
- 窄带 `creambox_check.py` 未用作证据（已证实漏报整行溢出）。

## §3 框标题 / 版心右缘实测（PIL 真墨水 + 印 PDF span + 200 dpi 像素扫描，三法）

- 自写脚本 `boxtitle_audit.py`（PIL getbbox 真墨水，含 letter-spacing；Noto Sans CJK SC、Newsreader Regular/SemiBold）+ `measure_ls.py`（anchor="ls" 修正版）+ PyMuPDF span 检查 + 200 dpi 像素扫描（`pixelscan2.log`，仅裁切右缘条带渲染，避开大内存并行渲染）。
- 方法教训（已验证）：PIL `font.getbbox` 默认 anchor 是 `"la"`（ascender 顶），bb[3] 为 ascender+descent（~1.3em），不是基线以下降部——借用的 `boxtitle_audit.py` 由此产生全部 BOX-BOTTOM 假阳性。修正版 `measure_ls.py` 全程用 `anchor="ls"`：20 pt 韩语行 la bbox (0,6,304,26) vs ls (0,-18,304,2)；Newsreader `november.` la (0,0,107,17) vs ls (0,-17,107,0)。横向测量不受 anchor 影响。
- **D3**：P2 选项 c「c. eten voor het paard van Sinterklaas」— PIL +8.5 px / 印 PDF span +13.1 px / 像素 +12.0 px（行：x=1473.5，基线 y=2233，23 pt Newsreader；右版心 1862.0 px = 1396.5 pt；PIL ink right 1870.5；印版 span 1406.3 pt = 1875.1 px；像素最右墨点 1874.0 px）。与核心旧版一致（归属见 PROOF-NOTE D3）。目视确认：该行明显比同列 a/b/d 行探出、直抵页边（裁图 `zoom-p2-optc.png`）。
- **任务必查项 (a) 全部合规**：P1「IN DEZE EDITIE　이번 호 내용」— PIL 1785.5 / 像素 1781.1（盒右缘 1862，余 ~81 px）；P6「VOOR OF TEGEN?　찬성? 반대?」— PIL 1764.5 / 像素 1762.9（余 ~99 px）；P2「ZO ONTHOUD JE HET　기억해요」— PIL 902.5 / 像素 901.9（盒右缘 961，余 ~59 px）。无一 R2-BOX-RIGHT 标记。
- **排除的 PIL 假阳性**（非整数字号被 PIL 取整放大所致，15.5→16 pt、19.5→20 pt、13.8→14 pt；一律以 PDF span + 像素扫描翻案）：P4 图注 PIL +11.5 → PDF span 1861.6 px（盒内 0.4 px）；P8 韩语注头 PIL +11.8 → span 最大 1851.2 px（盒内）；P8 `wat doe jij…` PIL +0.5 → span 1859.3 px（盒内）。
- 其余右缘：P1 刊首日期行像素 +0.5 px（噪声，nl-de 同类 +0.2 px 不计）；P2 `Pakjesavond에속한단어는?` span +0.1 px（噪声）。

## §4 p8 compare（显式 --core-p8/--edition-p8；--total 150）

- 命令：`p8.py compare --core-p8 <core-nl>/svg/p8-toets.svg --edition-p8 <edition>/svg/p8-toets.svg --total 150`
- 结果：**CLEAN**，core 150 noted / edition 150 noted，missing=[]，extra=0，uncertain=[]，**keydiff=[137, 138]**。RC=0。
- keydiff 裁决：137、138 为 E 节翻译题（NL→KO），键合法重定向到读者语；键本身正确（137 源句 `Het Sinterklaasjournaal is elke dag om 18:00 uur te zien.` → 韩 `신터클라스 뉴스는 매일 18:00에 방송해요.`，elke dag=매일，正确；138 `De nummers één en twee gaan naar de kwartfinales.` → `상위 두 팀이 8강전에 진출해요.`，正确）。139（암스테르담 도착은 88회째예요 → `De intocht in Amsterdam was de 88e editie.`）、140（→ `Ik maak een surprise met een gedicht.`）键与核心一致。非缺陷。
- `p8.py extract --p8 <edition>/svg/p8-toets.svg --total 150`：**noted set = 150 of 150**。RC=0。
- 另：text.md 键与印刷版 P8 键逐题比对 **0 不符**（150 题，见 §6）。

## §5 freeze / freeze_direct 8/8

- `freeze.py baseline --build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg --out <scratch>/freeze-baseline`：**8/8 SVG byte-identical**（p1 7edd158d…、p2 619c071a…、p3 086ebdbc…、p4 c82c9a3c…、p5 2a1335ec…、p6 52507c3e…、p7 7d55e70e…、p8 20280b79…；core integrity 8 文件重哈希确认未被改动）。RC=0。
- **注意**：第一次跑是 6/8（p2/p4 DIFF），因为协调员的核心重建在 2026-11-11 11:43:00–11:43:06 UTC 重写了核心 p2/p4（旧 shipped 哈希 6af13240/cfe890a0，新 619c071a/c82c9a3c）；重跑后 8/8。
- `freeze.py diff --core-svg <core-nl>/svg --edition-svg <edition>/svg`：各页 +26~+932/−26~−424 串；**新增 CJK 共 3449 字符，全为 Hangul + 每页 1 个 U+3000 分隔符**；非 Hangul 新增仅 P1「」与 P8『』（合法引号）。RC=0。
- 移除串核查：除 P4 积分榜（D6，真丢失）外，其余「未 accounted」均为假警——P8 注为韩语翻译（40/42 `perfectum`→`완료형`：`…의 완료형: heeft ontvangen`；118 로빈슨、129 단、6 네덜란드、65 로빈슨、21 오조스넬），P1 `ORANJE/SINTERKLAAS` 等以 `ORANJE · P.4` 形式存在，刊头 `LUCERNA DUTCH WEEKLY` 在韩版页脚完整保留。

## §6 keycheck 150/150（逐题手验）

- `keycheck-150.json`：text.md 键已解析 150/150；P8 SVG 答案注重建经两次修复后仍缺 23 条（40, 42, 43, 47, 50, 57, 60, 61, 70, 72, 73, 78, 79, 80, 82, 83, 84, 87, 88, 99, 117, 120, 125）另 97 号不匹配（待裁定）。已定位根因：行分组用了 |dy|<3 容差而各列基线相差 ~2.5 px（如 col A 行 y=1373.7 vs col B 行 y=1371.2），且早期 col() 边界（300/750/1250）错误地把跨栏碎片并入同一行；已改为按栏起始 x 划分（88/538.5/989/1439.5 的 [start, next start) 区间），再把分组容差由 |dy|<3 改为 <0.6（同行碎片基线完全相同）后重跑：**P8 notes 150/150 解析，mismatches: []，ok: 150**。
- 方法：text.md 全文通读 + 印 PDF 8 页目视；配对题字母对照印刷版 a–d 列表（P2 D：25-d、26-c、27-a、28-b；P8 F：141-b、142-c、143-d、144-a）；算术重算（19 天、1 天、4 小时、17 年、65、100）；范文计词 81。
- 语义核对：全部 150 键与正文/事实一致，惟 Q63/Q126 所考事实（PSV 26 分）在正文中无出处——属 D6（正文缺失），键本身外部属实（§10），不另计键错。
- Q78「Zij ___ (maken)」单复数歧义为核心同文、键自洽，不计缺陷。

## §7 印/网文字层比对

- `pdftotext -layout` 印版与网版各 38,715 字符（归一化后）；归一化（空白折叠）diff **为空**；词多重集 diff 0/0。
- **D5**：网 PDF 斜体丢失（见 §8）；其余两项（空格丢失、闭引号脱离）未复现。

## §8 斜体三联症（nl-de D5 同类）+ P8 最小字号实测

- PyMuPDF 全书 span 扫描：印版 italic span **1 处**（P1「«de groepswinst»」，Newsreader Italic 16.12 pt，bbox 1079.6–1201.8 pt）；网版 italic span **0 处**，同词改用 LucernaNewsreader-Regular。→ D5（轻微）。
- P8 最小字号实测（PyMuPDF 逐 span）：印版与网版均为 **10.12 pt**（P8 `1. 20:45 —`）。SOP §1.1 让步阶梯允许降至 9.75 pt，10.12 合规，非缺陷。
- P8 最大 span 右缘 1396.5 pt = 1861.9 px（页脚 `제8 면/ 총8 면`，盒内）。

## §9 弯引号全版扫描 + E 节 type 标签本地化 + text.md 残留中文

- text.md：U+201C/U+201D/U+2019/U+201E 均为 0；U+0027 ×12（`'s avonds` 等，与核心一致）。新版 text.md CJK：Han 0、U+3000 ×59、「1 」1 『3 』3。
- E 节 type 标签：已本地化——번역/한국어로 번역하기/네덜란드어로 번역하기、문장 완성、객관식、빈칸 채우기、단어 짝짓기、참/거짓 판단、문장 만들기、쓰기；无中文标签。标签计数：A2 문장완성 19、B1 32、B2 14；A2 객관식 21、B1 29、B2 7；A2 단어짝짓기 1、B2 1；B1 참/거짓 6、B2 1；B2 문장만들기 4、A2 1、B1 3；번역 A2 1、B1 2、B2 1；B1 쓰기 1。任务必查项 (e) 的 type 标签部分通过。
- **但 pinned 版 text.md 答案标记未本地化**：`— 答案：` 142 处 + 配对题 `(答案 x · …)` 8 处 = 150 处；除「答/案」外该文件无其他中文字符。→ D4（重大，针对 pinned 版；当前文件已修复，见 §0）。
- ABSTRACT.txt：**通过**。297 字节、0 换行（单行、无尾换行）、ASCII 双引号 0 个；韩语；含 `Lucerna VOL.4`、네덜란드어、A2–B2、150문항与真实主题（신터클라스/파크예스아본트/네이션스리그 네덜란드 대 독일/익스페디티 로빈슨）。校准：de 版摘要同样只写 `Lucerna …`（无字面 `A Lucerna`）且已通过。SOP §9（SOP.md 行 187）：摘要须读者母语、单行、无 ASCII 双引号，含刊名、目标语名、A2–B2 分级与题数。
- 韩语注时间误译类（pt-ko D5）：**未复现**。`[0-9]일:[0-9]` 在 text.md 与全部 SVG 均为 0 命中；仅有的两处 `일:` 是日期 gloss 分隔符 `(11월 16일: 독일–네덜란드)` 与 `(12월 5일: 19일 남음)`，与核心全角冒号结构平行，非缺陷。text.md 时间 inventory：20:45×17、12:00×16、20:00×13、18:00×27、16:00×3、10:15×4、11:30×1、13:00×3、16:30×2、18:45×2、14:30×1、12:15×1。

## §10 外部事实来源（2026-11-11 检索，5 组）

- **PSV 26 分**（题 63、126；D6 所缺句子的事实依据）：PitchLab「PSV Eindhoven are 1st in the 2026/27 Eredivisie with 26 points from 12 games. Their latest result was a 5–2 win at Cambuur on 8 November. The next game is away at Nijmegen on 21 November」；VAVEL「PSV lead the table with 26 points after 12 matches, 1 clear of Feyenoord. Matchweek 13 starts on 21 November with NEC Nijmegen v PSV」；Sports Mole 表格 PSV 12 战 8-2-2、40:15、26 分；TuringStats「PSV top … 1 point clear of Feyenoord」。——属实。NEC–PSV 11 月 21 日 원정 확인；16:30 개시 시간은 이번 검색 조각에 미표시（与核心文本一致）。
- **Grave 入城**（P1/P3）：vandaagingrave.nl：Landelijke intocht 2026 in Grave，14 november 2026 周六，Maaskade，市长 Marieke Moorman，NPO Zapp (NPO 3) 直播，Merel Westrik 主持；mamaliefde.nl：约 12:00 靠岸 Maaskade，节目 12:00–16:00，NPO Zapp (NPO 3) 12:00 起直播，Merel Westrik 主持；playtix：同上 + Sinterklaasjournaal 自 11 月 9 日。——全部属实。注：vandaagingrave 另称节目 11:45 开始、船 12:15 靠岸——文中只写「rond 12:00」（约 12:00），无冲突。
- **Amsterdam 入城**（P3；题 31、32、139）：desinterklaassite.nl、amsterdam.org、noordhollandnieuws.nl：2026-11-15 周日，船 De Omval 10:15，陆上队伍 Stopera 13:00 出发；amsterdaminside.com 与 holland-explorer.com：gemeente 登记为第 88 届（88ste editie）。——全部属实。注：uitamsterdam.com 一处散文写 10:30 靠岸 De Omval，但其自家节目表明细与所有其他来源均为 10:15（10:30 为 Berlagebrug 时刻），文中 10:15 为多数值。
- **下期预告欧战**（P7 VOLGENDE WEEK）：UEFA.com 2026/27 Champions League 赛程：Matchday 5，Tuesday 24 November 2026，Feyenoord vs Porto、Real Madrid vs PSV Eindhoven。——属实。
- **Feyenoord–Ajax**（P7 VOLGENDE WEEK）：FBref、FotMob、Sky Sports：Sun 29 November 2026，14:30 CET，De Kuip（Stadion Feijenoord）。——属实。
- **日期/星期**：`date -d` 核验（Europe/Amsterdam）：2026-11-01 周日、11-04 周三、11-14 周六、11-15 周日、11-16 周一、11-21 周六、11-22 周日、11-24 周二、11-29 周日、12-05 周六——与文中全部星期表述吻合。

## §11 其他核查

- 全文通读：text.md 全文（pinned 版）+ 印 PDF 8 页逐页目视（自渲染 150 dpi，`render-p1.png`…`render-p8.png`）。除 D3（P2 选项 c）、D6（P4 盒偏短留白）、D7（P2 EN JIJ 孤儿句号）外，无溢出/重叠/压页脚/图片问题；8 张图片均带目标语图说 + CC0 出处（Wim van Rossem/Anefo、Anefo、W. Punt/Anefo、Spaarnestad Photo/Wikimedia Commons、Elise lovenko/Unsplash、Cristina Gottardi/Unsplash、Aaron Burden/Unsplash）。
- P7 金句 8 条逐字出自本期正文，页码标注正确（P1×2、P2、P3、P4、P5、P6×2）。
- D6 补充核查：核心 `content34.py:127` 与核心 P4 SVG（y=1054.4/1084.9）均有 `Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten.`；本版 `content34.py` facts 列表只有 4 条，P4 SVG 与 text.md 均无此句；grep 验证 10 个 fan-out-nl 版的 `content34.py` 与 `svg/p4-sport.svg` 均无 `Stand Eredivisie na 12`（0 命中）；nl-de 的 P4 同样缺失。
- D7 补充核查：P2 EN JIJ 盒（y=1022.25，bottom=1445.8）韩语 gloss 末行孤立 `.`，基线 y=1440.2，PIL ink-bottom 1440.2，盒内余 5.6 px，不溢出；Zoom 裁图 `zoom-p2-enjij.png` 目视确认。
- **未改动源文件**：无任何源文件改动/重建/commit/push。

## 附：工具与方法备注
- 绝不用 `grep -o 'X[^<]*'` 扫 SVG：SVG 基本是单行文件，内含巨大 base64 图片数据，一次可吐 200 KB。只用 python 按 `<text>` 元素解析。heredoc `<<'EOF'` 不展开 `$变量`；python -c 里写中文/韩语字面量可能被传输层改写，码点检查用 `chr()`。
- 200 dpi 像素扫描只渲染窄条带 clip（`get_pixmap(clip=..., dpi=200)`），不要整页并行渲染（nl-de 曾因此致服务重启）。
- PIL 非整数字号取整放大假阳性（15.5→16 pt、19.5→20 pt、13.8→14 pt）：一律以 PDF span + 像素扫描翻案（见 §3）。
