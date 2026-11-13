# GATE-LOG — 2026-W47 en-ja · proof1 机械门（en re-fanout #2 重建版）

- **版**：2026-W47 en-ja，VOL.4
- **复校日期**：2026-11-11
- **对象目录**：`production/2026-w47/2026-w47-en-ja/`；核心对照 `production/2026-w47/core-en/`
- **工作区**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-ja1/`（全部中间件与日志在此；TMPDIR 指向其下 `tmp/`，未写 /tmp；旧 proof1 原件在 `old-proof1-pre-rebuild/` 子目录）

## SHA 核对（任务简报 + KIT §2 + 盘上 sha256sum，复核前后各测一次）

| 文件 | 大小 | SHA-256 | 结果 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-ja.pdf` | 41,509,391 B | `9f9faaea18807551394977ef536d142da65cfda78b73aa91d807063c0c4b0428` | MATCH |
| `The-Lucerna-VOL4-en-ja.web.pdf` | 2,883,877 B | `25645767641d06f1bfdc25f9437eb5c7f3ce0c319612eaabc9e912353f756f49` | MATCH |
| `2026-w47-en-ja.text.md` | 53,588 B | `219ce22d549887f0ca6895a928206ac18b255686e8f50f07296c54cd33d48aa9` | MATCH |
| core-en 印 `The-Lucerna-VOL4-en-zh-cn.pdf` | 41,407,278 B | `b484e007e6e0e29a78ea3f81c412e9c27c45a7c2b317a9a6081a2f63eb416566` | 复核前＝复核后，未变 |
| core-en 网 `The-Lucerna-VOL4-en-zh-cn.web.pdf` | 2,804,271 B | `7277e32a96f26974efd68d5e27978e0f1570dd15222f29a060ecdf7dbd89d3f8` | 复核前＝复核后，未变 |
| core-en `2026-w47-en-zh-cn.text.md` | 51,405 B | `e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b` | 复核前＝复核后，未变 |

两 PDF 各 8 页，页尺寸 1462.5 × 2025 pts（fitz）。

## 逐门结果

| 门 | 命令 / 方法 | 结果 | 证据 |
|---|---|---|---|
| 探针 | `ls /dev/null` 存在；`echo test \| git hash-object -w --stdin` 通；工作区真实写文件成功 | **PASS** | `.probe` |
| occlusion 审计 | `tools/venv/bin/python tools/occlusion_audit.py <svg dir> --json occlusion.json` | **PASS — 0 flags**，rc=0，selftest OK | `occlusion.json/.log` |
| p8 extract | `tools/p8.py` 抽取（本版 + core-en 对照） | **60/150 noted，两版抽取集完全相同** `[3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82–87, 89, 108–150]` | `p8extract.json/.log`、`p8extract-core.json/.log` |
| p8 compare | `tools/p8.py compare` | **CLEAN**，missing=[]，extra_count=0，keydiff=**[137, 138, 139, 140, 150]**（4 个读者语翻译键 + 写作键，预期内） | `p8compare.json/.log` |
| freeze baseline（真核心冻结） | `tools/freeze.py baseline --build core-en --core-svg core-en/svg --out freeze-base` | **PASS — 8/8 SVG 字节一致**（自产 build-copy 与盘上核心 SVG 逐文件 sha256 MATCH）；核心完整性未变 | `freeze-base.log`、`freeze-base/` |
| freeze diff | `tools/freeze.py diff --core-svg core-en/svg --edition-svg svg` | rc=0，新增 CJK 总计 **2,084**（与 KIT §3 一致；逐页：182/273/159/168/145/156/435/566；U+3000 各页 1–2） | `freeze.json/.log`（实为 `freeze-diff.json/.log`） |
| creambox 全版扫 | `creambox.py` 本版 + core-en 对照（+45 px 窗口版） | 真溢出 **0**；旧 D2/D3 现为 +14.3/+12.0；其余负值均为盒下节头伪影（core-en 同盒同值） | `creambox.log`、`creambox-core.log`、`creambox.py` |
| creambox inside-only | 自写 `creambox_inside.py`（仅计盒内基线）本版 + core-en | **0 真溢出**；每页最差 P1 +12.0、P2 +5.0、P3–P7 +47.7、P8 +92.4；P7 工具盒最小 +47.7 / desc-clear +41.6 | `creambox-inside.log`、`creambox-inside-core.log`、`creambox_inside.py` |
| keycheck | `keycheck.py ja <ed> <scratch>`（registry vs P8 抽取） | **149/150 exact**；唯一不匹配 Q150 = 预期内的抽取截断 + 页脚泄漏（p8.py FOOTER_RE 已知 bug）。每页累计与 KIT 一致（P1 10、P2 27、P3 45、P4 63、P5 81、P6 99、P7 111、P8 150）；级别 A2 62 / B1 66 / B2 22；Q38–41 = b/a/d/c。rc=1 仅因 Q150 | `keycheck.log`、`keycheck-150.json`、`keycheck.py` |
| text.md 答案 150 | 答案行正则抽取 vs registry.json 逐项比对（键/级别/题型） | **150/150 连续，0 差异** | `answers-150.log` |
| check_s11 | `check_s11.py ja` | **全部 §1.1 / P8 检查 PASS**：色集 core 19 = 本版 19；徽章 A2 #5c6e30 / B1 #46581f / B2 #37402f 在位；P8 最小字号 13.5；Q113–120 [A2] 选项标签；"Levels: 145–149 [A2]"；Q120 [A2] chip；"H　WRITING　作文 [B1]" | `check_s11.log` |
| boxtitle 宽度（源） | `sweep_titles.py ja`（fanout 轮硬化版） | **12/12 全过，0 超限**：最紧 THE WEEK IN NUMBERS +1.5；HAYMITCH +19.1；ODD SOCKS +23.6；A PRACTICE BALLOT +65.6 | `boxtitle.log`、`sweep_titles.py` |
| boxtitle 宽度（SVG） | `sweep_svg_titles.py ja`（advance + 紧项 PIL 真墨） | **18/18 全过，0 溢出**；THE WEEK IN NUMBERS 真墨 +1.5 | `boxtitle-svg.log`、`sweep_svg_titles.py` |
| PIL 真墨重测（两修复标题） | `ink_titles.py`（独立复用 svglib._runs/_pil） | P5 ODD SOCKS "数字で" **真墨 +23.5**；P6 A PRACTICE BALLOT "投票用紙" **真墨 +65.5**；对照 THE WEEK IN NUMBERS 真墨 +1.5 | `ink_titles.log`、`ink_titles.py` |
| P8 最小 PDF 字号 | fitz 逐 span（印 + 网） | **10.12 pt**（两版一致，≥ 9.75 下限）；全文档最小亦 10.12 pt | `p8font.log` |
| 印/网文字层 | `pdftotext -layout` 两版 + 词多重集 | print 43,475 字符 = web 43,475 字符；**词多重集差 0**；逐页字节一致 **8/8** | `printweb.log` |
| 网 PDF 重渲染（仅 scratch） | 复制 svg 到 `webrerender/`，`webpdf.py` 重渲染 | RC=0，2,883,892 B；SHA 与已发版不同（`075aed46…`，符合铁律——子集 head.modified 墙钟 + CreationDate）；文字层与已发网/印两版**均差 0**（43,475 字符）；已发网 PDF 未动 | `web-rerender.log`、`web-rerender-compare.log`、`webrerender/out.web.pdf` |
| 弯引号扫描 | text.md + 8 页 SVG 全扫 | text.md “ 81 / ” 81 成对，0 贴 CJK，0 个 ‘/’；SVG “ 82 / ” 82 成对，0 贴 CJK（+1 对为 Rousseau 图注 "Surprised!"）；孤标点行首 0 命中 | `quotes.log` |
| 禁词 / 残留简体中文 | text.md + SVGs + registry grep | 中期选举/众议院/民主党赢下/参议院/星期五/金句/范文/桥接/占位/TODO/FIXME/Lorem/已确认 **0 命中**；宣布/宣佈 0 命中（日语用 発表 8×） | （扫描输出见 PROOF-NOTE） |
| ABSTRACT | 全文核对 | **完整式**：Lucerna、VOL.4、150、A2、B2 俱在；0 ASCII 双引号；666 B | （见 PROOF-NOTE） |
| Q39/Q40 四方一致 | SVG 题干/选项、registry 键、text.md 注记、P8 提取键 | **四方一致**：a=mentor、b=tribute、c=campmate、d=arena；39=a、40=d | `q39-40.log`、`q39-stem.log`、`q39-stem2.log` |
| 改动题语义核对 | Q46/Q52/Q55/Q125/Q7/Q82–84/Q47–51 题干取自 SVG/源码 | **全部正确**（Q46 A、Q52 hosted、Q55 won、Q125 A、Q7 B、Q82 B、Q83 C、Q84 A；见 PROOF-NOTE） | `changed-stems.log`、`changed-stems2.log` |
| P5 D 节（旧 D6） | SVG 文本行位置核对 | 节头 y=2497.45，说明单行 y=2543.95（页脚线上 52 px），栏 3 顶无孤字 | `p5-dsection.log` |
| SAY IT | `text_w` 实测三格 + SVG 位置 | 三格 label/sub 全 fit（最小余量 +45.3）；panel 3 右缘 1340，glossary lx=1370，间隙 30 px | `sayit.log` |
| 残留措辞 | "Ashes begin" 等 grep | SVG + text.md + registry **0 命中**；"Arsenal are winning" 1×、"June 2027" 2× | （见 PROOF-NOTE） |
| "next Sunday" 冻结规则 | core-en / en-ja 源码+registry+SVG / tables.py / text.md | **0 命中**——无适用对象，规则不适用 | （见 PROOF-NOTE） |
| D5 字体（只记录，不判） | SVG font-family 统计 | 5 种：Newsreader 1037、Noto Sans CJK JP 633、Noto Serif CJK JP 55、DejaVu Sans 4、UnifrakturMaguntia 1 | （见 PROOF-NOTE） |
| 目视 | 印刷卡片 p1–p8 全 8 页 + 网页 PDF P1/P8（`pdftoppm -r 100` 渲染） | **全部看过，干净**；D2/D3/D5/D6 与两修复标题均经目视确认；P1 SEARCHES 注脚、P2 DID YOU KNOW/AND YOU?/SAY IT、P3 HAYMITCH 标题、P4 Ashes 全文、P5 ODD SOCKS 标题与 D 节、P6 投票用纸标题与图表、P7 工具盒/金句页码/NEXT WEEK、P8 Q125 与答案区均无异常 | `render/p-1.png` … `render/p-8.png`、`render-web/web-p1-1.png`、`render-web/web-p8-8.png` |
| 旧版逐页对比 | 备份旧版 print PDF 像素对比（100 dpi） | P1 0.98%、P2 0.82%、P3 0.02%、P4 11.48%（Ashes 重写）、P5 0.87%、P6 0.05%、P7 2.90%（NEXT WEEK 重写）、P8 0.65%——与已知修复一一对应 | `oldnew-diff.log`、`render-old/o-1.png` … `o-8.png` |
| 印/网像素差定位 | web-vs-print 分格统计 + 差异区裁切目视 | 差异集中在 P1 国会大厦照片（y2000–2400）与 P8 图书馆全景照片（y1600–1800，x 右半），双版裁切目视内容同一——网版照片下采样所致，非内容差；文字层已证字节一致 | `diff-p1-block.png`、`diff-p1w-block.png`、`diff-p8-block.png`、`diff-p8w-block.png` |
| 星期核对 | `date -d` | 2025-11-21 Friday（Q46 选项 A）、2026-11-21 Saturday、2026-11-16 Monday——与印刷一致；其余沿用旧 proof1 核对 | — |

## 诚实说明（与任务简报 / fanout 报告的出入）

1. **p8 extract 不是 150/150**：工具对本版返回 **60/150 noted**，因为本版 P8 版式下仅 60 个键带印刷注记。有意义的门是与 core-en 抽取集相同——该门通过。不得谎称 150/150。
2. **keycheck rc=1 仅因 Q150**：抽取截断 + p8.py FOOTER_RE 已知 bug（混合大小写页脚漏进第 150 键），非版面缺陷。
3. **fanout 轮 freeze.log 的 "core" 标签名不副实**：各语 freeze.log 的 p1 "core" 哈希互不相同，且 ja 的 `freeze-final/build-copy/svg/p1-front.svg` 与已发 ja 版 SVG 字节一致（`bdd374b7…`，含日语句 "人気の目安で" 与 CJK JP 字体）——其实是各版重建自身的自洽校验。本次独立重跑了真正的核心冻结（`freeze.py baseline --build core-en --core-svg core-en/svg`，8/8 字节一致，产出与盘上核心 SVG 逐文件 MATCH），且 freeze-diff 逐页数值与 fanout 轮完全一致（TOTAL 2,084），故不影响结论。此处记明，免得协调员被两组哈希差值误导。
4. **网 PDF 重渲染 SHA 必然不同**：`075aed46…` vs 已发 `25645767…`，符合铁律（fontTools 子集改写 head.modified 为墙钟 + cairo 写 CreationDate）；内容以文字层为准（差 0）。重渲染只在工作区 scratch 副本里做，已发网 PDF 的 SHA 复核后仍为 `25645767…`，未动。
5. **P2 AND YOU? 盒 desc-clear −1.0 是 heuristic 伪报**：末行 "ださい。" 为假名，无拉丁下行字母；core-en 同盒同 heuristic 为 −1.5；P2 渲染目视确认末行完整在盒内。基线余量 +5.0 为真。

## 缺陷汇总

**零缺陷。结论：(a) 定稿。** 详见 PROOF-NOTE.md。
