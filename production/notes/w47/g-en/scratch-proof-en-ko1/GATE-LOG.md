# GATE-LOG — W47 en-ko · proof1（机械门逐门结果）

- 版：`production/2026-w47/2026-w47-en-ko/`，刊期 2026-11-16–22，VOL.4
- 工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`（除注明外）；scratch：`hidden_files/w47/scratch-proof-en-ko1/`；`TMPDIR=<scratch>/tmp`，未写 `/tmp`
- 探针（2026-11-11 09:40:13Z）：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；scratch 内真实写入 `probe.txt`。通过。

## SHA 核对（KIT §7 + 盘上 sha256sum，全符）
| 文件 | 字节 | SHA-256 | 核对 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-ko.pdf`（印刷） | 32,386,030 | `983ad19cbd400836a465b9592d9a866597d5476b39a0a36a3c8e6ea9e6834c18` | ✓ |
| `The-Lucerna-VOL4-en-ko.web.pdf`（网页） | 2,594,367 | `e2439e78fc3d551503b7222ed740f2868eba415bddaa960a1fd47d06a126907a` | ✓ |
| `2026-w47-en-ko.text.md` | 52,965 | `9020d107dc95860e4b9bb5768134241d0c2e7ee4fecf56e29cf3562d1d325a53` | ✓ |

两 PDF 各 8 页（PyMuPDF 验证：print 8 页，web 8 页）。

## 逐门结果

| 门 | 结果 | 证据/日志 |
|---|---|---|
| 全文通读 | **通过**（除 PROOF-NOTE 缺陷外） | text.md 全 1305 行逐行通读；题量 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39，合计 150 题；答案区 1–150 编号连续无缺重 |
| 答案键 × registry | **通过** | `registry.json` 150 条与 text.md 答案键逐项比对：0 处不符 |
| 答案键 × 印版释义 | **1 处缺陷 D2** | 其余配对题全部一致：P2 D（Q24–27）、P4 C（Q56–59）、P5 C（Q74–77）、P8 F（Q141–144）；P8 其余各题（完形 112–119、选择 120–128、阅读 129–132、句型 133–136、翻译 137–140、对话 145–149、写作 150 开放题）逐题核对无误。D2：P3 C Q39/Q40 互换（39 mentor→d 应为 a；40 arena→a 应为 d）；核心 registry 相同，核心级 |
| 外部事实核查 | **1 处重大缺陷 D1，其余属实** | 中期选举 / I'm a Celebrity 2026 / ATP 总决赛 2026 / 英超 / NFL 第 11 周 / 反欺凌周 / 饥饿游戏电影与原声专辑（2026-11-13）/ Mike Johnson / 密西西比无决选均与公开来源逐项吻合（来源：美联社 2026-11-08 数据、californiatoday.com、political.org、maproll.io、MCA 新闻稿、Wikipedia）。D1：Ashes 整版错一年（见 PROOF-NOTE） |
| 日期/星期 | **通过** | `date` 核验：11 月 3 日周二、8 日周日、9 日周一、10 日周二、15 日周日、16 日周一、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、26 日周四、27 日周五、12 月 1 日周二、12 月 18 日周五、2027 年 1 月 3 日周日 |
| occlusion 审计 | **0 flags（通过）** | 自检 OK：6 类 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 阳性对照全部触发、干净对照静默；正式审计 `flag_count: 0`（`occlusion.json`）。已知盲区：BOXTITLE 只覆盖有描边或填色 `#2c2822` 的矩形，奶油色 `#f0eee5` 无描边框不在候选内——D3 由此漏网，boxtitle 门捕获 |
| p8 extract + compare | **CLEAN（通过）** | 60/150 带印刷注释，与核心同一集合；compare CLEAN，无缺失、无多余；keydiff = [137, 138, 139, 140, 150]，逐项说明：137–140 为 E 翻译题键，核心为中文译文、ko 版为韩文译文（读者语改向，预期内）；150 为开放写作题键，核心中文措辞 vs ko 版韩文措辞（预期内）。`p8-extract.log/json`、`p8-compare.log/json` |
| keycheck（p8 抽取键 × registry） | **通过** | 150 条抽取键逐项比对：仅 2 处差异，均可解释——139：registry "새 의회는 2027년 1월에 개회한다." vs 抽取 "새 의회는2027년 1월에 개회한다."（PDF 文本抽取在 CJK–数字边界丢空格，SVG 节点与渲染均有空格，抽取引擎伪影）；150：抽取器截断长开放题键为 "열린 문제"（keycheck 既定预期行为） |
| freeze 渲染 | **通过** | 新增 CJK 字符总数 2324，与 KIT 声称一致；baseline：8/8 字节一致，核心 SVG 完整性未变（重跑前后哈希一致）。`freeze-diff.log/json`、`freeze-baseline.log` 及 `freeze-baseline/` |
| creambox.py（P7 工具盒清除量，必跑） | **通过** | 8 个 SVG 全跑，共 32 个奶油框；大量负清除量（-12 至 -37）均为该脚本 +45px 窗口的已知假阳性形态（所报"末行基线"皆为框下方下一区块的首行/标题，清一色 -35.5/-37.0，即一倍行距）。P7 工具盒实测干净：框 x=1439.5 y=651 w=422.5 h=357.21，底边 1008.2；盒内末行基线 y=959.68（"지 아무도 모른다。"），清除量 **+48.5px**；所报 -37.0 是下方 READERS' CORNER 标题（y=1045.2）的假阳性。目视裁切 `render/crop-p7-toolbox.png` 确认墨水全在盒内。`creambox.log` |
| boxtitle 宽度 | **1 处缺陷 D3 + 1 处观察 O1** | 10/12 在 386.5px 预算内，2 项 OVER：HAYMITCH 标题 401.9px（建版 `text_w` 实测；boxtitle-ko.py 400.7px），止于 1859.4，框右缘 1862，**入框、余约 2.6–3.8px（偏紧，仅作观察 O1）**；ODD SOCKS 标题 424.1px（boxtitle-ko.py 422.9px），止于 530.1，框右缘 510.5，**超出约 19.6px（boxtitle 口径 18.4px），缺陷 D3**。放大裁切 `render/crop-p5-oddsocks.png` 目视确认 "보기" 在框外白纸上。`boxtitle-ko.log` |
| P8 最小字号 | **通过** | PyMuPDF 实测印刷 PDF：P8 最小 10.125pt（答案行，SVG 13.5px），≥ §1.1 底线 9.75pt；其余各页最小 11.62pt；页脚 12.75pt。注：KIT §3 "P8 min font 13.5pt" 的 13.5 是 px 数而非 pt（见 PROOF-NOTE O5），非本版缺陷 |
| 印/网文字层同一 | **通过** | `pdftotext` 两版各 49,094 字节、43,304 字符、8,436 词、2,550 去重词，词多重集差分 0/0，内容同一。`print.txt`、`web.txt` |
| 弯引号/撇号 | **通过** | text.md 中 " 81 个 / " 81 个，成对；U+2019 为 0 个（英文撇号用 ASCII `'`，符合 build_map 归一化）。SVG 去标签后扫描：8 个 SVG 均无弯引号邻接韩文。text.md 中 6 处弯引号邻接韩文已逐节点核查：全部落在 Newsreader 英文字节点内（P7 工具盒两行英文句；P8 E 题干 `“The …”`，其中 "번역：" 为独立的 Noto Serif CJK SC 节点、引号属 Newsreader 节点），**0 处落入 CJK 字体节点**，渲染窄引号合格；text.md 的邻接只是导出拼接伪影。P3 框题撇号为 ASCII U+0027 |
| 残留简体中文 | **通过** | text.md 汉字（U+4E00–U+9FFF）0 个；版内 SVG 仅 3 个汉字 `三色蛾`（刊头绿线上的三色蛾装饰，§1.1 规定元素，属意）；core-en SVG 含汉字 1691 个（中文讲解层，已全部移除） |
| 禁词 | **通过** | `SOP`、`proofread`、`cover`、`lint`、`github`、`TODO`、`placeholder`、`占位`、`bridge` 在 text.md 与 SVG 可见文本中均为 0；`ko` 在 text.md 出现 2 次，仅见于文件头元数据行（非印刷内容） |
| 目视 | **通过（除 D3 外）** | 印刷 P1–P8 全页 + 网页 P1/P8 全页已目视（`render/print-p1.png`…`print-p8.png`、`web-p1.png`、`web-p8.png`，96dpi，PyMuPDF）；无溢出/重叠/压页脚；图片与出处齐全（见 PROOF-NOTE）。放大裁切：`crop-p5-oddsocks.png`（D3 实证）、`crop-p3-haymitch.png`（O1 实证：标题在框内）、`crop-p7-toolbox.png`（工具盒干净实证） |

## 结论
- **(b) 缺陷清单，不可定稿**：D1 Ashes 整版错一年（核心级·重大）、D2 P3 C Q39/Q40 答案互换（核心级·重大）、D3 P5 ODD SOCKS 框题出框约 19.6px（ko 版独有·中）。
- D1、D2 根在 core-en，须报协调员、由核心层修正并联动全部 12 个读者语版；本复校未碰核心。
- 机械门除上述三项缺陷外全部通过。
