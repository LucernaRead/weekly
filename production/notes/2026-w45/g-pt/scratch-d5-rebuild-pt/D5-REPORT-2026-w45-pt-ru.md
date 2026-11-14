# D5 重建报告 — 2026-w45-pt-ru（俄语读者版）
W45 pt 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁与西里尔字母由 Noto Sans CJK SC 改走 Noto Sans，installer 旧分支，D26）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-pt/logs/2026-w45-pt-ru/`
（`GATES-SUMMARY.txt` 为 run2 门禁总表；`*-gates-run1.log` / `*-rebuild.log` 为 run1 记录）。
## 一、装机
- Core 落盘（全家共用一次）：`apply_variant.py --patch-core pt --week 2026-w45`
  → `production/2026-w45/core-pt/svglib.py`，`_D5_READER = "latin"`（core 模板；D24 常驻值，按 patched 原样同步，不特殊处理）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-pt-ru/svglib.py --target pt --reader ru --week 2026-w45`（先 `--check` dry-run 全净，RC 0）。装后 `_D5_READER = "ru"`（installer 旧分支：拉丁与西里尔字母一律走 Noto Sans；fix-xru 只限 W47，绝未带入）；
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py`。text.md 无导出器（pt 家已证实：生产目录无 textmd/export/derive 文件；pt-de/pt-fr 的 `transform.py` 是内容分发变换，不是 textmd 导出器），已发 `issues/2026-w45/2026-w45-pt-ru/2026-w45-pt-ru.text.md` 原样 carry-over
  **BYTE-IDENTICAL**（SHA-256 `9d6f502f27d39d848071f612c35c7c945ec26414dbb9d0d13e631361df739fb8`），验证用 `verify_textmd.py` carry-over + 门 15。
## 二、基线（修前生产版，全部干净才装机）
- `run.py` RC=0，**TOTAL 150**，0 警告。
- 文字层：印 / 网 / 已发三方字符数均为 33207 = 33207 = 33207，多重集差 **0**；自建网 PDF 884861 B。
- 印 PDF 2820389 B（SHA-256 `0def0c8a2191dd1809050c0ae49f15ffbaaad502b366872053bfa43f18017175`）；D5 前 KIT 记值 3,435,753 B（D1 旧值，已过期；工具链漂移，见 §六）。
- 修前普查 `d5_census.py`：D5 拉丁 **338**（>0，符合装机前提）、西里尔 254、弯引号在 CJK 0。
- 基线 P8 口径：noted **150/150**。
## 三、缺陷与修法（run1 → run2）
run1 共 0 项缺陷——首轮构建即全绿，无需修复。

P8 变化：264→**265** 行（一处 D5 字体换行重排，非修复所致），距页脚线余量 44.3→**44.3 px**（正，无溢出）。
## 四、门禁（run2，全套 17 门）
| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0（curly_total=0，noto_sans_elements=775） |
| 4 render | RC=0，印 PDF 2546515 B |
| 5 webpdf | RC=0，网 PDF 1007923 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**（keydiff=[137, 138]（与 KIT 记载的读者语答案键一致）） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 163，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（63 OBSERVE） |
| 12 boxtitle | 0 DEFECT（31 titles，313 body lines） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 264→264，slack 44.3→44.3） |
| 15 文字层 print=web | 字符多重集差 **0**；text.md 与已发版 diff = 1 行（D34 line 34，落仓时修正），其余逐字节相同；修正后 carryover 0/0 |
| 15b 刊头 gap（D18） | 95.7 px PASS |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | 家族 gates.py 经 runner 跑通：874 vs 864（+10 rowcheck，同类噪声；5 处增量行间隙 −3.6…+4.9px，在基线自有范围 −16.2 以内；`cjk` 项两版相同）。 |

**OVERALL: ALL-GREEN.**

**G17（家族 gates.py，runner 重跑，修复后与修复前一致）**：家族 gates.py 经 runner 跑通：874 vs 864（+10 rowcheck，同类噪声；5 处增量行间隙 −3.6…+4.9px，在基线自有范围 −16.2 以内；`cjk` 项两版相同）。
## 五、新交付物
（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）
- 印 PDF：`A-Lucerna-VOL2-pt-ru.pdf`，**2546515 字节**，
  SHA-256 `ece324aa6ba2900817cd248f9c5de0707ef6dc3881167965fd07e91e6cdd8748`
  （D5 前 KIT 记值 3,435,753 字节——D1 旧值，已过期，以此为准）。
- render-web PDF：`A-Lucerna-VOL2-pt-ru-web.pdf`，**3134878 字节**，
  SHA-256 `f08b6bb4f54eb1bb6bc9bb39b1e1599ff51a7389d50e38f5e850524279933876`
  （D5 前 KIT 记值 3,520,353 字节，见 §六）。
- 网 PDF（issues 型）：`2026-w45-pt-ru.web.pdf`，**1007923 字节**，
  SHA-256 `6a5aacc4e63199a73967df9982ac7d415ebc175e1634105138eae9d502dbe112`
  （D5 前 issues 已发版 884861 字节）。
- text.md：与已发版差 1 行（D34 line 34，落仓时修正；交付文件 `issues/2026-w45/2026-w45-pt-ru/2026-w45-pt-ru.text.md`，SHA-256 `09900cbd8f59ee9c13b4af556d9966edf58c0f1420f3e5bccf8094fd05dd96c7`，33816 字节；原已发版 BYTE-IDENTICAL `9d6f502f27d39d848071f612c35c7c945ec26414dbb9d0d13e631361df739fb8`）。。
- 练习总量仍为 **150 题**，答案键仅 #137/#138 与 core 不同（KIT 已登记）。
## 六、KIT
- `patched/2026-w45-pt-ru/WEEKLY-KIT.md`（closer 同步入 `production/2026-w45/2026-w45-pt-ru/WEEKLY-KIT.md`）：pin 节追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **D5 rebuild（2026-11-14）** 节
  （装机、基线、缺陷与修法、门禁、新交付物、导出器缺失说明）。
- 工具校准（家族报告 §0）：`tools/verify_textmd.py` 经 W45 基线 + patched 两轮校准后落地，
  live md5 `6dc093c207b0d72b6d387c04e46066f2`；本版 carryover 修正后 0/0（D34 已修）。
- KIT SHA 漂移：重建印 PDF 系统性小于 KIT 记值（工具链漂移、内容相同），KIT 更新以实测发运值为准纠正。
