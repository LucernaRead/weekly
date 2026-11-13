# GATE-LOG — W47 nl-en 第二轮独立校对机械门（build 8 复校，2026-11-11）

- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（tools/venv）
- 对象：build 8（SHA 见 PROOF-NOTE.md §0；与任务消息逐字一致）
- 第一轮（build 7）日志已归档至 `round1-build7/GATE-LOG.md`；本文件只记本轮自跑结果
- 全程 `TMPDIR` 指向本 scratch 下 `tmp/`（系统 /tmp 只有 512M）

## §0 身份

| 文件 | 字节 | SHA-256 |
|---|---|---|
| 印 PDF `De-Lucerna-VOL4-nl-en.pdf` | 12,665,899 | `2cc431f2572abad8790d1b99d6211d3aa87a5278a4052f3f0810dd6d764b0b58` |
| 网 PDF `De-Lucerna-VOL4-nl-en-web.pdf` | 1,574,228 | `0fc6232bbe2bd8d3794169d83b4c233df519845f07eef1f9f35e2fdada2f6d18` |
| `2026-w47-nl-en.text.md` | 45,074 | `1d69f5edc43e217bfa5d9e032d3c8c6666460a37ee163d0f0db18b1bebeba45b` |

探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，通过。creambox.py md5 `ee7a55d8b2057cf4ad42a97bb1197383`，与任务一致。

## 逐门结果（本轮自跑）

| 门 | 命令 / 方法 | 结果 |
|---|---|---|
| occlusion | `tools/occlusion_audit.py <edition>/svg/`（`occlusion.log`） | 自检 OK（6 类阳性对照全触发）；**0 flags**，rc=0 |
| creambox 全版 | 正典 `tools/creambox.py <edition>/svg/*.svg`（`creambox.log`） | 全部奶油框末行 clearance 为正；P7 toolbox 3 框，最小末行 clearance **+13.1**、最小 desc-clear **+7.1**；BRIEVEN 框底 1927.5，末行基线 1899.6（+27.9）；P2 EN JIJ 框 desc-clear −0.4 已裁决为假阳性（末行无降部字母，见 PROOF-NOTE §6）；P1 IN DEZE EDITIE 框下 +24px 与 P2 四词框下 +32px 均为框外下一标题/说明，非溢出 |
| p8 extract | `tools/p8.py extract --p8 <edition>/svg/p8-toets.svg --total 150`（`p8-extract.json`/`p8-extract.log`） | noted set **150/150**，rc=0 |
| p8 compare | `tools/p8.py compare --core-p8 <core>/svg/p8-toets.svg --edition-p8 <edition>/svg/p8-toets.svg --total 150`（`p8-compare.json`/`p8-compare.log`） | **CLEAN**，missing=[] extra=0 uncertain=[]，**keydiff=[137, 138]**，rc=0。裁决：137/138 核心键为中文译文、本版键为英文译文，139/140 两边同为荷兰语——翻译题合法重定向（核心键 137 `圣诞老人新闻每天 18:00 播出。` / 138 `前两名晋级四分之一决赛。`，见 `p8-extract-core.json`），非缺陷 |
| freeze baseline | `tools/freeze.py baseline --build <core> --core-svg <core>/svg --out <scratch>/freeze-baseline`（`freeze-baseline.log`） | **8/8** SVGs byte-identical；core 完整性：重跑前后 8 文件复哈希无变化，rc=0 |
| freeze diff | `tools/freeze.py diff --core-svg <core>/svg --edition-svg <edition>/svg`（`freeze-diff.json`/`freeze-diff.log`） | 逐页增减仅讲解层；新增 CJK 字符共 **15** 个，全部为 U+3000 全角空格（每页 1–2 个），无新增中文文本，rc=0 |
| freeze_direct | `tools/freeze.py --help` | **无此子命令**（仅 baseline/diff）——方法备注，非缺陷（见 PROOF-NOTE O10） |
| print/web 文字层 | PyMuPDF span 级比对（`textcompare.log`） | 8 页 span 数逐页相等（218/203/189/184/196/201/188/386），多重集差分 **0**、位置差分（容差 2pt）**0** |
| pdftotext | gates.py 门内 | print 45,404 B / web 45,409 B，均 > 0；网 PDF 1,574,228 B < 7 MB |
| P8 字号 | PyMuPDF 答案区 y>1040pt（`p8font.log`） | 最小 **10.12pt**（162 span；10.5pt×7、12.75pt×6），中位数 10.12pt ≥ 9.75pt 下限 |
| P8 徽章 | gates.py 门内 | core A2 8 / B1 24 / B2 3 = edition A2 8 / B1 24 / B2 3 |
| §1.1 SVG 审计 | gates.py 门内 | off-palette {}，无金色，描边矩形 0，VOL.5=5（core 5），纸色填充 8 |
| gates.py 全套 | `gates.py . en`（cwd 为版目录，`gates-build8.log`） | **OVERALL: ALL PASS**（9/9 门） |
| 弯引号全扫 | U+2018/2019/201C/201D/201A/201E/2032/2033 扫 `content*.py`、8 SVG、`.text.md`、`ABSTRACT.txt`、印/网两 PDF 文字层 | **全 0**（第一轮 D1 已修好） |
| CJK 扫查 | `.text.md` 全文 | 仅 `答案`×150 + 全角标点 `：（）`×142 + U+3000×59，无其他中文 |
| keycheck 150 | `keycheck-150.json`（text.md 逐题解析 vs 印刷 P8 键） | 150/150 解析；149 match + 第 150 题开放写作；**0 不一致** |

## 机械门不覆盖的发现（本轮新增缺陷，见 PROOF-NOTE.md）

机械门 9/9 全过，但以下两项缺陷不在机械门覆盖范围内，由 SVG 几何 + 像素实测 + 字体面检查发现：

- **D1（中）**：P1 HET WOORD 英文注文被 y=1853 通栏细线从中切断。occlusion LINEX 漏检的原因：线距行 1 墨迹带下缘约 0.5px、距行 2 墨迹带上缘约 2px，落在两带之间的缝隙里。证据：`crop-p1-woord.png`、150dpi 像素扫描（行 1 墨迹末行 svg 1850.2、线 svg 1852.8、行 2 墨迹始于 svg 1856.6）、核心对照（核心为中文单行、整段在线上）。
- **D2（轻）**：网 PDF 丢失全版唯一斜体（P1 `«de groepswinst»`：印版 `Newsreader16pt-Italic`，网版 `LucernaNewsreader-Regular`；网 PDF 字体清单无 Italic 面）。文字内容无损（印/网差分 0），仅字形斜/直差异。证据：`italic.log`、`crop-italic-print.png` vs `crop-italic-web.png`。

**机械门全过 ≠ 本轮零问题。**

## 判为非缺陷的项

- P2 D 组 c 项 `c. eten voor het paard van Sinterklaas` 超出右栏家具边约 8.6pt（印 PDF span x1=1406.3pt，200dpi 像素最右墨迹 1405.1pt）——核心版同一行同一位置逐值相同（span 1406.3pt、像素 1405.1pt），为核心继承版式，右方空白边距、无碰撞（`crop-p2-match.png`）。见 PROOF-NOTE O1。
- P1 "Page 1 of 8"、"Answers on page 8"、"Levels are mixed" 等家具 span 超出版心右缘 0.8–2.1pt——各页一致，为家具右对齐设计，非溢出（`pdf-spans.log`）。
- P2 EN JIJ 框 desc-clear −0.4——末行无降部字母，统一 0.30 余量所致假阳性（PROOF-NOTE §6）。
- P8 顶栏荷兰语副标题未翻英文、text.md 首行含 `2026-W47`——与核心同模板/同家具（PROOF-NOTE O8/O9）。

## 外部事实来源（本轮独立检索，2026-11-11）

- Eredivisie 第 12 轮（11 月 8 日）+ 积分榜：Flashscore roundup（Heerenveen–Feyenoord 5–3、Twente–Ajax 2–2、Cambuur–PSV 2–5；PSV 26 分榜首）、VAVEL standings（"Leaders: PSV, 26 points; 12 of 34 matchweeks played"）、Road2Sushi/PitchLab 积分表（PSV 12 场 26 分）、OddAlerts 第 13 轮赛程（NEC–PSV 周六 15:30 UTC = 16:30 CET、Feyenoord–Excelsior 17:45 UTC = 18:45 CET、Twente–Willem II 周日 11:15 UTC = 12:15 CET、Ajax–ADO 13:30 UTC = 14:30 CET；Feyenoord–Ajax 11 月 29 日周日 13:30 UTC）。
- Nations League A2 组：UEFA 赛程/Sportradar（MD6 11 月 16 日周一 Germany vs Netherlands，Olympiastadion Berlin，20:45 CET；Greece vs Serbia 同日）、TNT Sports 积分表（NED 8（7:5）、GRE 8（5:3）、GER 5（3:2）、SRB 0（3:8））、AppiSToS（Greece–Germany 0–0，10 月 5 日）。
- Sinterklaas：playtix（全国 intocht 11 月 14 日周六 Grave，Maaskade 约 12:00，市长 Marieke Moorman，NPO 3 直播，Merel Westrik 主持；阿姆斯特丹 11 月 15 日周日，De Omval 10:15、Scheepvaartmuseum 11:30、Stopera 13:00）、amsterdaminside（第 88 届）、holland-explorer（Grave 11 月 14 日、阿姆斯特丹 11 月 15 日第 88 届、Pakjesavond 12 月 5 日周六）、vandaagingrave.nl（节目 12:00–16:00，Merel Westrik）、Ziggo（Merel Westrik 主持）。
- 欧冠第 5 轮：UEFA 赛程/sync2cal/VAVEL（11 月 24 日周二 Real Madrid–PSV、Feyenoord–FC Porto，20:00 UTC）。
- Expeditie Robinson 2026：Ziggo/mannenstof/nl.wikipedia（11 月 1 日周日 20:00 RTL 4 首播；19 名选手 10 荷 + 9 弗拉芒；马来西亚；34 天；Nicolette Kluijver + Edson da Graça 主持；Camille Vanuxem 记者）。
- Het diner：en.wikipedia（Herman Koch，Ambo Anthos 2009 年初版）。
- "Elise Iovenko / Unsplash"：检索无确认结果亦无反证，列为未核验（PROOF-NOTE O6）。

## 方法备注

- gates.py 的 `p8_compare` 门打印 "keydiffs=0" 是其正则 `[Kk]ey diff`（要求空格）匹配不到 p8.py 输出格式 `keydiff=[137, 138]` 所致；以直接跑的 p8.py 输出 + `p8-compare.json` 为准（CLEAN，keydiff=[137,138]，已裁决）。
- 本轮 PIL 墨水实测初版对分数 pt 字号用 `round()` 取整、高估了行宽（如 P8 133/137 行"溢出"为伪报）；最终横向溢出结论以 PyMuPDF span bbox + 200dpi 像素扫描为准（`pdf-spans.log`；唯一真超限为 P2 c 项，核心同值，见上）。
