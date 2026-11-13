# GATE LOG — W47 core-ko proof5（fix1 后的从头全量复校）

- 日期：2026-11-11（UTC 约 09:16–10:30）；探针 `git hash-object -w` 成功后开工
- 复校对象：`~/workspace/weekly-git/production/2026-w47/core-ko/`（fix1 run 11）
- 解释器锁（按 KIT 周版核查）：build-family 用 `/usr/bin/python3`、render-family 用
  `tools/venv/bin/python`。**freeze 本轮从头重跑**（fix3b 的 stale build-copy freeze 已作废，不复用）。
- 本日志只记机械门；内容复校见 PROOF-NOTE.md §2–§3。

## 1. 对象 SHA 核对

| 文件 | 字节数 | SHA-256（盘上实测） | 任务书 |
|---|---|---|---|
| 印刷 `Lucerna-VOL4.pdf` | 46,232,227 | `53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27` | ✓ 符 |
| 网版 `Lucerna-VOL4-web.pdf` | 4,232,878 | `9592945ae188dc8e50394fcab1ded155baaff63161bcf0b5f7ecbc6898c43bc7` | ✓ 符 |
| text.md | 26,048 | `ba1b80f8edabc76eac398e34e80718254e1e584966a39a7c5a9a504b5fe9dda3` | ✓ 符 |

## 2. occlusion 审计 —— 0 flags（两版）

- 命令：`tools/occlusion_audit.py all --builddir production/2026-w47/core-ko`
- `tools/venv/bin/python`：geometry pass green, _fails_summary.csv empty,
  `total_flags=0`, `status=PASS`, `padding_px=0`, `ACTUAL=0`（全 o=3-ok 行；35 个入口全 CONTINUE）。
- `/usr/bin/python3`（dry-run）：PASS, total_flags=0。
- 自检：6 类全触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX；`found=6 expected=6`；clean controls silent）。
- 日志：`occlusion-proof5.log`、`occlusion-proof5b.log`、`occlusion-output-proof5/`。

## 3. p8 extract + compare —— 150/150，CLEAN

- extract：150 items（`p8-extract-proof5.log`，`p8-extract-proof5.json`）。
- compare（core 对自身）：`CLEAN`，`missing=[]`，`extra_count=0`，`keydiff=[]`，
  `extra_sample=[]`（`p8-compare-proof5.log`）。
- 人工逐题复核：150 键逐条对照题面/正文/图表，全符（见 PROOF-NOTE.md §2.4；抄键记录在
  `print-proof5.txt` 答案区段）。

## 4. freeze 8/8（本轮从头重跑，非复用）

- 命令：`/usr/bin/python3 tools/corekit/freeze.py --builddir production/2026-w47/core-ko --outdir scratch-proof-ko-core5/freeze-proof5`
- 结果：**8/8 逐字节一致**（per-file `OK` 行；日志 `freeze-proof5.log`）。
- 哈希与 fix1 run 11 逐一相同：
  p1 `00227ca1…`、p2 `faf9e3c5…`、p3 `b447a559…`、p4 `d997631e…`、p5 `09f7fc23…`、
  p6 `d45b0355…`、p7 `14b7cf13…`、p8 `e88f7d42…`。
- 结论：SVG 核心完整性确认；fix1 未破坏任何已复校页面。
- 产物：`freeze-proof5/svg/`（p1–p8 与上轮逐字节相同）。

## 5. 印/网文字层比对 —— 逐字节一致

- `pdftotext`（无标志）：各 **49,451 字节**，`cmp` 通过。
  产物 `print-raw-proof5.txt` / `web-raw-proof5.txt`。
- `pdftotext -layout`：各 **94,537 字节**，逐字节一致。
  产物 `print-proof5.txt` / `web-proof5.txt`（内容复核用此版）。
- 49,451 字节与 fix1 run 11 数值相同。

## 6. check_core / check_gloss —— 与 run 11 日志逐字节同

- `python3 - <<'EOF' check_core.py ...`：gloss fails 0、P7 金句 8/8 verbatim、
  orphan issues 0、`[dates] correct`（`check-core-proof5.log`）。
- `check_gloss.py`：10 项 dictionary-vs-inflected（`check-gloss-proof5.log`），
  两日志均与 fix1 run 11 `diff` 逐字节同。已裁定类，非缺陷。

## 7. P8 最小字号 —— 9.975pt（≥9.75）

- PyMuPDF 扫 P8 全部 350 spans：`min 9.975pt`（fix1 测的 162-span 区域值亦为 9.975pt）。
- print / web 两版均为 9.975pt。

## 8. 弯引号全扫 —— 0

- U+201C/U+201D/U+2019：8 SVG（限 `<text>` 节点，不含 base64 图像数据）、text.md、
  ABSTRACT.txt、5 个 `content*.py` = 全部 0（`textlayer-proof5.log`）。
- 同文件另扫：`시리즈 시리즈` 0、`어디예요` 0、旧句 `수능 후에 김치의 날이 와요` 0。

## 9. 事实外部核实（浏览器检索，2026-11-11）

- 수능/응시생/점수 551,864 / −2,310 / 85지구 / 1,312곳 / 08:10、成绩 12/11：KICE/교육부 系报道 ✓。
- 한국시리즈 5 场比分/场地、1패 후 4연승、12년 만、통산 9번째：11/8 赛后报道 ✓。
- 사다리（LG 4–1 두산 10/14、KIA 3연승、삼성 3–2 KIA）：当日报道 ✓。
- 김장비용 199,456 / 219,071 / 230,442、배추 54,980 / 74,800、高춧가루 −1.8% / 무 −5.6%：aT 11/10 发布 ✓；
  -9.0% / -26.5% / -13.4% 均验算相符。
- K리그1（33R 10/24、36R 11/21–22、38R 12/5、12/6）：联盟赛程 ✓。
- 한능검 81회（11/28 심화만、27,000원、취소 11/11–13、사진 11/11、수험표 11/24、환불 11/17）：国史编纂委员会系整理 ✓
  （"10시"歧义见 PROOF-NOTE §5.5，不算缺陷）。
- 단풍（산림청 9/22 例보 내장산 11/4、월출산 11/9、두륜산 11/11、설악산 实测 10/16、50%/80% 기준）：산림청/기상청 ✓。

## 10. D7 普查（本轮新发现）

- 脚本：见 `ex-census.txt` 首部（AST：`ex` arg[4] + `match_set` arg[2]/[3]，空白归一化查 text.md）。
- 总 166 项（ex 142 + match 24），缺失 **99**：`qf` 4/4、`e` 70/78、`e` match 9/24、`a`/`b`/`c` 各 4/4、`f` 4/40。
- D6 10 段仍全缺（`ex-present8.txt` 与 §4 段grep记录；D6 评估 `scratch-assess-textmd-d6/ASSESSMENT.md`）。
- 机理：`textmd.py:36` `CALL_ARGS` 只含 `("f","ex")` 与 `("f","match_set")`；
  `textmd.py:18` `is_prose()` 拒收含 `/` 的字符串。

## 11. 红线遵守

- 只复校：未改任何源文件、未重建（freeze 输出只在 scratch-proof dir）、未 commit、未 push、未动其他家庭。
- KIT 未更新（fix1 同款，见 PROOF-NOTE §5.1）——KIT 陈旧不算缺陷，只记一笔。
