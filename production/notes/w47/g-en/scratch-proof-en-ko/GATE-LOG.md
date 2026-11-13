# GATE-LOG — W47 en-ko · proof1（独立复校，en re-fanout #2 重建版）

- 版：`production/2026-w47/2026-w47-en-ko/`，刊期 2026-11-16–22，VOL.4
- 复校员：独立 proof1（与建版者/fan-out agent 非同一人）；本轮会话 `6494a7de-5444-4e09-a07c-2597f43f0d5b`
- 工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`（除注明外；本版构建栈为 venv，见“构建重跑”）；scratch：`hidden_files/w47/scratch-proof-en-ko/`；`TMPDIR=<scratch>/tmp`，未写 `/tmp`
- 只读核查生产目录：构建类门禁在 scratch 副本里重跑；网 PDF 只重渲到 scratch，未覆盖生产目录网 PDF；未改任何生产文件，未 commit、未 push、未碰 core-en、未动 `tools/`
- 探针（2026-11-11 14:03:30Z 前后）：`ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；scratch 内真实写入 `probe.txt`。通过。
- 并行说明：本目录内另有会话 `248f4608-a118-4c3b-ba55-f36af524d2d8` 的同任务产物（`rerun-build.log`、`p8-extract.json` 等无后缀文件及 `PROOF-NOTE.md` / `GATE-LOG.md` 先版）；该会话结论为 (a)，其两份文件已原样保存在 `PROOF-NOTE-concurrent-run-248f4608.md` / `GATE-LOG-concurrent-run-248f4608.md`。本日志所引全部证据均为本复校自跑（带 `2` 后缀的日志/json、或本复校自写脚本），并与先版逐项比对一致——除本日志新发现的 D4（Q73，见 PROOF-NOTE）外。
- 复校结束时三件 SHA 与任务给定值逐符一致（见下表），生产目录未动。

## SHA 核对（任务给定值 + 盘上 sha256sum，全符）

| 文件 | 字节 | SHA-256 | 核对 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-ko.pdf`（印刷） | 32,386,301 | `ecad215eb3f5ab98e6d50a7fd5ea5b383902c8f1ea0aadd3bff1fb28822072cd` | ✓ |
| `The-Lucerna-VOL4-en-ko.web.pdf`（网页） | 2,629,426 | `5115ad3f586bbb94226ad841bbfeedd31fa80eecc7ee6cf4a9296d43ccc9ca9e` | ✓ |
| `2026-w47-en-ko.text.md` | 53,590 | `e5633ac3569d216ce5e7f0578af3ab0c920fa964c77636fd2c7954a3a05484ac` | ✓ |

两 PDF 各 8 页（PyMuPDF 验证：print 8 页，web 8 页；版面 1462.5×2025pt）。

## 逐门结果

| 门 | 结果 | 证据/日志 |
|---|---|---|
| 构建重跑（scratch 副本，venv） | **通过** | 新副本 `build-copy2/`（仅 `*.py` + `assets/`）：venv 重跑 rc=0，`TOTAL exercises: 150`，`OVERFLOW`/`TOO WIDE` 命中 0（grep 计数 0），`MODEL words: 82`，重生成的 8 个 SVG 与生产 SVG SHA-256 逐个一致（`VENV MATCH` 8/8）；重跑 registry 与生产 `registry.json` 内容相等（150 条）。`rerun-venv.log`、`registry-rerun-venv.json`。注：同一副本用系统 python3（Pillow 10.2.0）重跑为 7/8 DIFF（仅 p4 MATCH），属栈 artifact：生产 SVG 由 venv（Pillow 13.0.0 / FreeType 2.14.3）构建，`freeze.log` 首行 runtime 亦为 venv；系统栈重跑 TOTAL/流末值相同（P8-keys 2205/2560、MODEL 82），仅 x 坐标微差（如 P1 “WEEKLY IN ENGLISH” x=679.5 vs 676.1）。`rerun-sys.log`、`rerun-build2.log` |
| run rc=0 / TOTAL 150 | **通过** | 同上；分版 10/17/18/18/18/18/12/39（P8 112–150 共 39 题） |
| ABSTRACT 全文形式 | **通过** | `ABSTRACT.txt` 624 字节，一行韩文，ASCII 双引号 0 个；与 fanout-en2 `abstracts/ko.txt` `cmp` 字节一致。内容：11 月 3 日中期选举发表结果（民主党两院、254–162、认证 11 月 10 日–12 月 18 日）、11 月 16 日反欺凌周/짝짝이 양말의 날、11 月 20 日世界儿童日+饥饿游戏新片、11 月 21 日英超回归+都灵 ATP 决赛+一年前珀斯 Ashes 4–1 回顾、本文英语/解说韩语、A2–B2、150 题 |
| Q39→a / Q40→d（四源一致） | **通过** | registry：39 mentor→a（`mentor = 스승 a`）、40 arena→d（`arena = 경기장 d`），38 b / 41 c；text.md 答案区：39 a、40 d；P3 SVG C 配对释义顺序 a=teaches and guides you（mentor）、b=chosen to take part（tribute）、c=lives with you in the jungle camp（campmate）、d=place where the Games are fought（arena），与键逐项对应；P8 extract：38–41 = b/a/d/c |
| Ashes 回顾措辞 | **通过** | “Perth is winning” / “Ashes begin” / “second week in Perth” 全版 0 处；P4 “Perth, One Year On: How Australia Kept the Ashes”，首场 2025-11-21 周五珀斯、澳大利亚两天 8 wicket 取胜、系列赛 2025-11-21–2026-01-08、总比分 4–1，Cummins 背伤 / Smith 代任队长 / Boland / Doggett 首秀 / Hazlewood 腿筋伤一律过去时。外部复核（实时检索）：Sky Sports 2025–26 系列赛总结——Australia win 4–1，1st Test Perth Australia won by eight wickets，2nd Test Brisbane eight wickets，4th Test Melbourne England won by four wickets，5th Test Sydney Australia won by five wickets，`Nov 21 - Jan 08`；cricket.com.au / TNT：珀斯首场 847 球，为 1888 年以来最短 Ashes Test（仅 788/792 两场更短）；“first Test win in Australia for almost fifteen years”与 2011 年 1 月悉尼后首胜吻合（另源：18 Tests 未胜）。Q46 A、Q52 hosted、Q55 won、Q125 A 均与回顾一致 |
| ATP 总决赛 2026 | **通过** | 实时检索复核：2026 ATP Finals 11 月 15–22 日都灵；八人 Zverev / Alcaraz / Shelton / Medvedev / Cobolli / Fils / Tiafoe / Rafael Jodar；Sinner 为 2024+2025 两届冠军、因膝伤缺席。与 P4 文本及 Q51（B 膝伤）逐项一致 |
| occlusion 审计 | **0 flags（通过）** | 自检 OK：6 类 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 阳性对照全部触发、干净对照静默；正式审计 `flag_count: 0`。`occlusion2.log/json`。已知盲区同 ko1（BOXTITLE 只覆盖有描边或填色 `#2c2822` 的矩形）——本版由 boxtitle 门 + PIL 真墨 + 目视覆盖 |
| p8 extract + compare | **CLEAN（通过）** | core 与 edition 各 60/150 带印刷注释，同一集合；compare CLEAN，无缺失、无多余；keydiff = [137, 138, 139, 140, 150]，逐项说明：137–140 为 E 翻译题键，核心为中文译文、ko 版为韩文译文（读者语改向，预期内）；150 为开放写作题键，核心中文措辞 vs ko 版韩文措辞（预期内）。`p8-extract2.log/json`、`p8-extract-core2.log/json`、`p8-compare2.log/json` |
| keycheck（p8 抽取键 × registry；registry × core；registry × 重跑） | **通过** | registry 150 条，重跑 registry 150 条，二者内容相等；registry-vs-p8extract exact **149/150** + exc=[150]（抽取器截断长开放题键为 “열린 문제”，既定预期行为），mismatch=[]；registry-keys-vs-core **145/150**，diffs 仅 137–140、150（读者语改向，预期内）；Q38–41 = b/a/d/c；Q125 A、Q46 A、Q52 hosted、Q55 won；Q82/83/84 = B/C/A；noted set == core noted: True；extract keys 150，无缺失。`keycheck2.log` |
| freeze 渲染 | **通过** | baseline：venv 重跑 8/8 SVG 字节一致（见“构建重跑”）；freeze diff TOTAL 新增 CJK **2323**：Hangul 音节 2309、U+3000 9、CJK 标点 5（：1、「2、」2，P8 翻译题引号）；新增汉字（U+4E00–U+9FFF）**0**，无未解释项。分版：p1 213 / p2 316 / p3 162 / p4 170 / p5 166 / p6 183 / p7 471 / p8 642。`freeze-diff2.log/json` |
| 印/网文字层同一 | **通过** | `pdftotext -layout` 两版各 **107,723 字节**，`cmp` 字节一致；PyMuPDF 逐页 span 数一致（P1 227 / P2 259 / P3 216 / P4 229 / P5 197 / P6 218 / P7 242 / P8 273，两版相同）。`print.txt`、`web.txt` |
| P8 最小字号 | **通过** | PyMuPDF 实测印版：P8 最小 **10.125pt**（答案行，SVG 13.5px），≥ 9.75pt 底线；其余各页最小 11.625pt。网版同值。`render-print.log` |
| creambox（canonical 全版扫描） | **通过** | 32 个奶油框全跑；全部 inside-only 清除量为正，最小 **+5.0px**（P2 AND YOU? 框，末行 “요.” 基线 1539.85，框底 1544.9）；所报负清除量（-35.5/-36/-37.0）皆为 +45px 窗口的已知假阳性（所报“末行”皆为框下方下一区块的首行/标题，清一色一倍行距，canonical 工具已标注 BELOW-WINDOW）。P7 工具盒：框 x=1439.5 y=651 w=422.5 h=357.21，底边 1008.2；盒内末行基线 y=959.68，清除量 **+48.5px**；7 个工具盒最小 inside 清除量 +47.7、最小 desc-clear +41.6。P2 AND YOU? desc-clear −1.0 为 0.30×size 下行启发式假阳性：PIL 真墨实测（anchor="ls"）“요.” 墨水止于基线（y1=0），真墨余量 **+5.05px**。`creambox-canon.log`、`creambox2.log`、`ink_ko.log` |
| boxtitle 宽度 | **通过（1 处观察 O1）** | 源级 `boxtitle-ko.py`（venv）：12 项中 11 项在 386.5px 通用预算内，HAYMITCH 401.9px 标 OVER，ODD SOCKS 375.4px（ko1 D3 已修复）。HAYMITCH 权威口径：SVG 实测框右缘 1862，标题起于 1457.5，advance 401.9px 余量 **+2.6px**；PIL 真墨余量 **+2.5px**（ink_end 1859.5）；放大裁切 `render/crop-p3-haymitch.png` 目视确认末字 “기” 完整在框内、无裁切、未压框边、未碰他元素；与旧版同标题 401.9px 同值（修复而非回归）。其余 11 项 advance 均 ≤375.4px，真墨无溢出。`boxtitle2.log`、`ink_ko.log` |
| 孤儿标点全版扫 | **0 真孤儿（通过）** | 8 个 SVG 逐节点扫查：行首孤儿 0；text.md 行首孤儿 0。8 处“纯标点节点”全部为同基线折分 artifact（P2 5 处 “—” 为日历分隔符、与同行韩文/数字同基线；P7 3 处 “.” 为句末句号、与所属句同基线 y=754.03/841.59/959.68），非孤儿。另：全版独立 `___` 节点 19 处，edition 与 core-en 逐页位置完全一致（P2 4 / P3 5 / P4 4 / P5 4 / P8 2；P1/P6/P7 0），属核心既有排版形态，非本轮回归，记观察 O3。`mech-checks.log`、`blank-lines3.log` |
| 150 题三源逐题手验 | **1 处缺陷 D4，其余通过** | text.md 全 1305 行逐行通读（P1–P8 + 答案区）；答案解析 150 条、编号 1–150 无缺重；text.md 答案区 vs registry **150/150** 一致；registry vs P8 抽取键 149/150 + #150 例外（见 keycheck）；5 组配对题释义顺序逐组对 SVG 核对（P2 D Q24–27、P3 C Q38–41、P4 C Q56–59、P5 C Q74–77、P8 F Q141–144）全部与键一致；其余各题（完形 112–119、选择 120–128、阅读 129–132、句型 133–136、翻译 137–140、对话 145–149、写作 150）逐题核对无误。唯一例外 **D4：P5 B Q73 题干/键不合**（见 PROOF-NOTE）：题干 “Speak ___: tell a teacher.”（text.md:589、P5 SVG、core-en content56.py:49–50）配答案键 “speak”（registry n=73、text.md 答案区、P8 印版 ANSWERS 块 “73. speak”、P8 抽取键），完成句为 “Speak speak: tell a teacher.”，不合语法；合乎题干的键应为 “up”（speak up）。三源一致地错过——跨源比对无法检出，属 ko1 D2 同类核心级键错 |
| 日期/星期 | **通过** | `date` 核验：2025-11-21 周五、2026-01-08 周四、11 月 3 日周二、8 日周日、9 日周一、10 日周二、15 日周日、16 日周一、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、26 日周四、27 日周五、12 月 1 日周二、12 月 18 日周五、2027-01-03 周日 |
| 残留简体中文 | **通过** | text.md 汉字（U+4E00–U+9FFF）0 个；SVG 汉字仅 P1 刊头三色蛾装饰 `三色蛾`（§1.1 规定元素，属意，见并行版 text-scan 结论） |
| 禁词 | **通过** | `SOP`、`proofread`、`cover`、`lint`、`github`、`TODO`、`placeholder`、`占位`、`bridge` 在 text.md 与 SVG 可见文本中均为 0；`ko` 仅见于 text.md 文件头元数据行（非印刷内容，见 ko1） |
| 弯引号/撇号 | **通过** | text.md 中 “ 81 个 / ” 81 个，成对；U+2019 为 0 个（英文撇号用 ASCII `'`，符合 build_map 归一化）；ASCII 撇号 40 个；P3 框题撇号为 ASCII U+0027；SVG 去标签后扫描 8 页均无弯引号邻接韩文（见 ko1；本轮弯引号计数与之相同） |
| 金句逐字 | **通过** | P7 金句 8 条与原文页面逐字一致（8/8）：P2 “The vote is over. The counting is not.”、P1 “A “call” is not the official result.”、P4 “The Ashes are not a sport for early nights.”、P6 “A midterm changes Congress, not the President.” / “The map is drawn. The work starts in January.”、P3 “Two jungles, one week: a painted jungle in the cinema, and a real jungle on television.”、P5 “A small act is not small to the person it helps — and a loud voice starts with one sentence.”、P1 “On Tuesday, November 3, Americans voted in the midterm election — for all 435 seats in the House of Representatives, for 35 seats in the Senate, and for governor in 36 states.” |
| MODEL 范文词数 | **通过** | P8 MODEL 82 词（构建计数；连独立 em-dash 计为词符则为 84），在 80–100 词范围内 |
| 目视 | **通过（除 D4 文字缺陷外）** | 印刷 P1–P8 全页 + 网页 P1/P8 全页已目视（`render/print-p1.png`…`print-p8.png`、`web-p1.png`、`web-p8.png`，96dpi，PyMuPDF）；无溢出/重叠/压页脚；图片与出处齐全（见 PROOF-NOTE）。放大裁切：`crop-p3-haymitch.png`（O1 实证：标题在框内）、`crop-p5-oddsocks.png`（D3 修复实证）、`crop-p7-toolbox.png`（工具盒干净实证）、`crop-p2-andyou.png`（O2 实证）、`crop-p8-answers.png`（答案块完整、未压页脚） |

## 结论

- **(b) 缺陷清单，不可定稿**：唯一缺陷 **D4（核心级·中）P5 B Q73 “Speak ___” 配错键 “speak”**（应为 “up”）。根在 core-en（content56.py:49–50），10 个已查 en-* 读者语版 registry 均同错（de/es/fr/it/ja/ko/nl/pt/ru/zh-tw），须报协调员、由核心层修正并联动全部 12 个读者语版；本版单独无法修。
- ko1（旧版）的 D1（Ashes 错一年）、D2（Q39/Q40 互换）、D3（ODD SOCKS 出框）三项缺陷在本重建版中**全部已修复**，逐项复核通过（见 PROOF-NOTE）。
- 除 D4 外全部机械门通过；D4 为三源一致地错过的新发现（proof1 与并行版均未提及 Q73），非本轮返修引入。
- 本复校未改任何生产文件、未碰 core-en、未动 `tools/`。
