# GATE-LOG — W47 en-ko · proof1（独立复校，en re-fanout #2 重建版）

- 版：`production/2026-w47/2026-w47-en-ko/`，刊期 2026-11-16–22，VOL.4
- 复校员：独立 proof1（与建版者/fan-out agent 非同一人）；本轮会话 `248f4608-a118-4c3b-ba55-f36af524d2d8`
- 工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`（除注明外）；scratch：`hidden_files/w47/scratch-proof-en-ko/`；`TMPDIR=<scratch>/tmp`，未写 `/tmp`
- 只读核查生产目录：构建类门禁在 scratch 副本（`build-copy/`）里重跑；网 PDF 只重渲到 scratch（`web-rerender.pdf`），绝未覆盖生产目录网 PDF；未改任何生产文件，未 commit、未 push。复校结束时三件 SHA 与任务给定值逐符一致（见下表），生产目录未动。
- 探针（2026-11-11 14:02:48Z）：`ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；scratch 内真实写入 `.probe`。通过。
- 注意：同一 scratch 目录内另有同名文件（`…2.log/json`、`tr_ko.py`、`ink_ko.py`、`stub_*.py` 等）非本复校所写，疑为并行同任务 agent 的产物；本日志只引用本复校自写/自跑、未带 `2` 后缀的文件。

## SHA 核对（任务给定值 + 盘上 sha256sum，全符；复校结束时重验一致）

| 文件 | 字节 | SHA-256 | 核对 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-ko.pdf`（印刷） | 32,386,301 | `ecad215eb3f5ab98e6d50a7fd5ea5b383902c8f1ea0aadd3bff1fb28822072cd` | ✓ |
| `The-Lucerna-VOL4-en-ko.web.pdf`（网页） | 2,629,426 | `5115ad3f586bbb94226ad841bbfeedd31fa80eecc7ee6cf4a9296d43ccc9ca9e` | ✓ |
| `2026-w47-en-ko.text.md` | 53,590 | `e5633ac3569d216ce5e7f0578af3ab0c920fa964c77636fd2c7954a3a05484ac` | ✓ |

两 PDF 各 8 页（PyMuPDF 验证：print 8 页，web 8 页；版面 1462.5×2025pt）。

## 逐门结果

| 门 | 结果 | 证据/日志 |
|---|---|---|
| 构建重跑（scratch 副本） | **通过** | 复制 `*.py` + `assets/` 至 `build-copy/`，`run.py` 等效重跑 rc=0，`TOTAL exercises: 150`，`OVERFLOW`/`TOO WIDE` 命中 0；重生成的 8 个 SVG 与生产 SVG SHA-256 逐个一致（`MATCH` 8/8）；重跑 registry 与生产 `registry.json` 内容相等（`registry == rerun registry: True`）。`rerun-build.log`、`registry-rerun.json` |
| run rc=0 / TOTAL 150 | **通过** | 同上；`by page {1: 10, 2: 17, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 39}`；levels A2 62 / B1 66 / B2 22 |
| ABSTRACT 全文形式 | **通过** | `ABSTRACT.txt` 624 字节，一行韩文，ASCII 双引号 0 个；与 fanout-en2 `abstracts/ko.txt` 字节一致（`cmp` 通过）。内容：11 月 3 日中期选举发表结果（民主党两院、254–162、认证 11 月 10 日–12 月 18 日）、11 月 16 日反欺凌周/짝짝이 양말의 날、11 月 20 日世界儿童日+饥饿游戏新片、11 月 21 日英超回归+都灵 ATP 决赛+一年前珀斯 Ashes 4–1 回顾、本文英语/解说韩语、A2–B2、150 题。旧短式已不存在 |
| Q39→a / Q40→d（四源一致） | **通过** | registry：39 mentor→a（`mentor = 스승 a`）、40 arena→d（`arena = 경기장 d`），38 b / 41 c；text.md 答案区：39 a、40 d；P3 SVG C 配对释义顺序 a=teaches and guides you（mentor）、b=chosen to take part（tribute）、c=lives with you in the jungle camp（campmate）、d=place where the Games are fought（arena），与键逐项对应；P8 extract：38–41 = b/a/d/c。`q3940.log`、`p3-match.log`、`answers3b.log` |
| Ashes 回顾措辞 | **通过** | text.md：P1 IN BRIEF “A year ago: Australia beat England 4–1 in the 2025–26 Ashes. (p. 4)”；P4 “Perth, One Year On: How Australia Kept the Ashes”，首场 2025-11-21 周五珀斯、澳大利亚两天 8 wicket 取胜、系列赛 2025-11-21–2026-01-08、4–1，Cummins 背伤/Smith 代任/Boland/Doggett 首秀等 2025 年事实一律过去时；“Perth is winning” 0 处、“Ashes begin” 0 处、“second week in Perth” 0 处；“Arsenal are winning!” 1 处；P7 NEXT WEEK “England's rematch waits until June 2027”。外部复核：Wikipedia 2025–26 Ashes 系列赛（21 Nov 2025–8 Jan 2026、Australia won 4–1、1st Test 21–22 Nov 2025 Perth、Australia won by 8 wickets、shortest by balls since 1888）逐项吻合。Q46 A、Q52 hosted、Q55 won、Q125 A 均与回顾一致；registry notes 无 stale Ashes措辞 |
| occlusion 审计 | **0 flags（通过）** | 自检 OK：6 类 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 阳性对照全部触发、干净对照静默；正式审计 `flag_count: 0`。`occlusion.json/log`。已知盲区同 ko1（BOXTITLE 只覆盖有描边或填色 `#2c2822` 的矩形）——本版由 boxtitle 门 + 目视覆盖 |
| p8 extract + compare | **CLEAN（通过）** | core 与 edition 各 60/150 带印刷注释，同一集合；compare CLEAN，无缺失、无多余；keydiff = [137, 138, 139, 140, 150]，逐项说明：137–140 为 E 翻译题键，核心为中文译文、ko 版为韩文译文（读者语改向，预期内）；150 为开放写作题键，核心中文措辞 vs ko 版韩文措辞（预期内）。`p8-extract.log/json`、`p8-extract-core.log/json`、`p8-compare.log/json` |
| keycheck（p8 抽取键 × registry；registry × core） | **通过** | registry-vs-p8extract 149/150 exact + #150 例外（抽取器截断长开放题键为 “열린 문제”，既定预期行为），mismatch=[]；registry-keys-vs-core 145/150，diffs 仅 137–140、150（读者语改向，预期内）；Q38–41 = b/a/d/c；Q125 A、Q46 A、Q52 hosted、Q55 won；Q82/83/84 = B/C/A；noted set == core noted: True；extract keys 150，无缺失。`keycheck.log` |
| freeze 渲染 | **通过** | baseline 8/8 字节一致（core SVGs 重跑前后哈希一致，核心完整性未变）；freeze diff TOTAL 新增 CJK **2323**：Hangul 音节 2309（99.4%）、U+3000 9、其余 CJK 标点 5（：1、「2、」2，P8 翻译题引号）；新增汉字（U+4E00–U+9FFF）0；移除串含 Hangul 0。分版：p1 213 / p2 316 / p3 162 / p4 170 / p5 166 / p6 183 / p7 471 / p8 642。`freeze-baseline.log`、`freeze-diff.log/json`、`freeze-analysis.log` |
| 印/网文字层同一 | **通过** | 生产印版 vs 生产网版：`pdftotext` 各 49,711 字节、43,897 字符，词多重集差分 0/0；逐页 PyMuPDF 文本字节一致 8/8；scratch 重渲网版（2,629,443 字节，网 PDF 字节不可复现，属预期）与印版亦逐字节一致、词差分 0。`print.txt`、`web.txt`、`web-rerender.pdf/txt`、`printweb.log` |
| P8 最小字号 | **通过** | PyMuPDF 实测：印版与网版均为 P8 最小 **10.12pt**（答案行，SVG 13.5px），≥ 9.75pt 底线；其余各页最小 11.62pt；页脚 12.75pt 未单独计。`p8font.log` |
| creambox（P7 工具盒清除量，必跑） | **通过** | 32 个奶油框全跑；全部负清除量（-35.5/-36/-37.0）皆为该脚本 +45px 窗口的已知假阳性形态（所报“末行基线”皆为框下方下一区块的首行/标题，清一色一倍行距）。P7 工具盒实测干净：框 x=1439.5 y=651 w=422.5 h=357.21，底边 1008.2；盒内末行基线 y=959.68，清除量 **+48.5px**；P1 SEARCHES +12.0；P2 AND YOU? +5.0（紧但在内，见 PROOF-NOTE O2 与 `crop-p2-andyou.png` 目视）。`creambox.log`、`toolbox.log` |
| boxtitle 宽度 | **通过（1 处观察 O1）** | 源级 `boxtitle-ko.py`：12 项中 11 项在 386.5px 通用预算内，HAYMITCH 400.7px 标 OVER——该数为通用预算口径 artifact：HAYMITCH 所在奶油框实为更宽框（框右缘 1862，标题起于 1457.5，内宽 404.5）。权威口径为 SVG 实测 sweep（`sweep_svg_titles.py`，硬化版）：18/18，0 溢出；HAYMITCH advance 401.9px，余量 **+2.6px**，PIL 真墨余量 **+2.5px**（见 PROOF-NOTE O1 与 `crop-p3-haymitch.png` 目视确认在框内、无裁切）；ODD SOCKS 375.4px，余量 +29.1（ko1 D3 已修复，`crop-p5-oddsocks.png` 目视确认在框内）。`boxtitle.log`、`boxtitle-svg.log` |
| 孤儿标点全版扫 | **0 真孤儿（通过）** | 8 个 SVG 逐节点扫查：8 处“纯标点节点”全部为同基线折分 artifact（P2 5 处 “—” 皆为日期分隔符、与同行韩文/数字同基线；P7 3 处 “.” 皆为句末句号、与所属英文/韩文句同基线 y=754.03/841.59/959.68），无独行标点行；text.md 独行标点行 0。`orphan-punct.log`、`orphan-punct2.log`。另见 PROOF-NOTE O3：7 处孤行填空线（非标点类）单独记录为观察项 |
| 150 题三源逐题手验 | **通过** | text.md 全 1305 行逐行通读（P1–P8 + 答案区）；答案解析 150 条、编号 1–150 无缺重；text.md vs registry：仅 Q34 为解析器 artifact（注记含嵌套括号，原文 `opens (open = 개봉하다(3인칭 단수는 s 추가))` 与 registry 键 `opens` 一致），其余 149/149 一致；text.md vs p8extract：同上（除 #150 截断外）；5 组配对题释义顺序逐组对 SVG 核对：P2 D（Q24–27）、P3 C（Q38–41）、P4 C（Q56–59）、P5 C（Q74–77）、P8 F（Q141–144）全部与键一致；P8 其余各题（完形 112–119、选择 120–128、阅读 129–132、句型 133–136、翻译 137–140、对话 145–149、写作 150 开放题）逐题核对无误。`answers3.log`、`answers3b.log`、`match-order.log` |
| 日期/星期 | **通过** | `date` 核验：11 月 3 日周二、8 日周日、9 日周一、10 日周二、15 日周日、16 日周一、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、26 日周四、27 日周五、12 月 1 日周二、12 月 18 日周五、2027 年 1 月 3 日周日 |
| 残留简体中文 | **通过** | text.md 汉字（U+4E00–U+9FFF）0 个；版内 SVG 仅 3 个汉字 `三色蛾`（P1 刊头绿线上的三色蛾装饰，§1.1 规定元素，属意）；其余 7 个 SVG 汉字 0 个。`text-scan.log` |
| 禁词 | **通过** | `SOP`、`proofread`、`cover`、`lint`、`github`、`TODO`、`placeholder`、`占位`、`bridge` 在 text.md 与 SVG 可见文本中均为 0 |
| 弯引号/撇号 | **通过** | text.md 中 “ 81 个 / ” 81 个，成对；U+2019 为 0 个（英文撇号用 ASCII `'`，符合 build_map 归一化）；ASCII 撇号 40 个。P3 框题撇号为 ASCII U+0027 |
| 金句逐字 | **通过** | P7 金句 8 条逐字核对原文页：P2 “The vote is over. The counting is not.”、P1 “A “call” is not the official result.”、P4 “The Ashes are not a sport for early nights.”、P6 “A midterm changes Congress, not the President.” / “The map is drawn. The work starts in January.”、P3 “Two jungles, one week…”、P5 “A small act is not small…”、P1 长句 “On Tuesday, November 3, Americans voted…”——8/8 逐字，页码标注正确 |
| MODEL 范文词数 | **通过** | P8 MODEL 84 词，在 80–100 词范围内 |
| 目视 | **通过** | 印刷 P1–P8 全页 + 网页 P1/P8 全页已目视（`render/print-p1.png`…`print-p8.png`、`web-p1.png`、`web-p8.png`，96dpi，PyMuPDF）；无溢出/重叠/压页脚；图片与出处齐全（见 PROOF-NOTE）。放大裁切：`crop-p3-haymitch.png`（O1 实证）、`crop-p5-oddsocks.png`（D3 修复实证）、`crop-p7-toolbox.png`（工具盒干净实证）、`crop-p2-andyou.png`（O2 实证） |

## 结论

- **(a) 定稿零缺陷**：全部机械门通过；150 题三源一致；Q39/40、Ashes 回顾、ABSTRACT、HAYMITCH/ODD SOCKS 框题等 re-fanout #2 承接项全部核实。观察项 O1–O6 见 PROOF-NOTE（非缺陷，不修）。
- ko1（旧版）的 D1（Ashes 错一年）、D2（Q39/Q40 互换）、D3（ODD SOCKS 出框）三项缺陷在本重建版中**全部已修复**，逐项复核通过。
- 本复校未改任何生产文件、未碰 core-en、未动 `tools/`。
