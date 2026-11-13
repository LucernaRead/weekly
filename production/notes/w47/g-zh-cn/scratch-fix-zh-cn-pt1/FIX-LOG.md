# W47 zh-cn-pt 修复记录 fix1（修 proof1 结论 (b) D-01～D-03）

- 修复员：fix1（与 proof1 校对员、builder 不同人）
- 对象：`production/2026-w47/2026-w47-zh-cn-pt/`（只改这一版，不碰核心与其他版）
- 日期：2026-11-11（EST 18:47 开工，19:35 左右收工）
- 任务书：proof1（8ee0cffb）结论 (b) 的 3 项缺陷，同属一类（葡语后缀加长，
  盒标题真墨越奶油盒右缘）。不 commit、不 push。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-cn-pt1/`
  （唯一、专用；生产目录只在同步一步写盘）

## 开工探针与身份核对（自行算出）

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功（`e69de29b…`）。
- scratch 真实写盘成功（`probe.txt`）。
- 开工三 SHA 与任务书逐字一致：

| 文件 | 字节 | SHA-256（开工） |
|---|---|---|
| 印刷 PDF `Lucerna-VOL4-PT.pdf` | 41,734,759 | `2286485f2608d2a144d37e9451f7a1945313e54e1f6ba1b540aec1ab5484859c` |
| 网页 PDF `Lucerna-VOL4-PT-web.pdf` | 2,647,093 | `030f52fb82087f8fe13f3465b74ee61b8c02b6e7d8a4740280ff7fa66cac76fa` |
| 文本导出 `2026-w47-zh-cn-pt.text.md` | 50,846 | `9207974bed3d5d16c4312752ad22a4219f0033e33d9264c29c07adfe3d44cb71` |

## 修前复测（自己重测，不采信转述）

- 锚定确认：`bslib4.py:199` 的 `box()` 标题行
  `self.p.text(x + pad, yy + tsize - 4, title, tsize, "sans", True, OLIVE)`，
  未传 anchor；`svglib.py:387` 的 `text()` 默认 `anchor="start"`——
  三处均为左锚定，缩短葡语后缀必左移墨右缘（ru-pt 的右锚定反例不适用）。
- PIL 真墨横扫（自写 `sweep.py`，与 proof1 `sweep-boxes.py` 同法：`_runs`/`_pil`
  分 run、23pt sans bold），生产 SVG 全 8 页：**恰 3 旗**，与 proof1 逐值一致；
  核心同扫 0 旗（proof1 值）。

| 缺陷 | 位置 | 改前标题 | PIL 墨右 | 盒右缘 | 越边 | 像素墨右（旧 PDF） |
|---|---|---|---|---|---|---|
| D-01（中） | P1 `content12.py:47` | 数字看本周　Esta semana em números | 982.5 | 961.0 | **21.5** | 982.4（proof1：981.7） |
| D-02（小） | P2 `content12.py:187` | 本周生活小日历　Datas desta semana | 1416.0 | 1411.5 | **4.5** | 1415.7（proof1：1415.0） |
| D-03（小） | P5 `content56.py:25` | 这一周的高频词　Palavras da semana | 964.5 | 961.0 | **3.5** | 963.8（proof1：963.2） |

可用墨宽均为 404.5px（盒右缘 − 标题 x：P1/P5 961.0−556.5，P2 1411.5−1007.0）。
D-02 量值以盒右缘 1411.5 为准（#3 的“距山谷照 23.7px”量的是照片边，不是对盒边）。

## 候选标题测宽（PIL 真墨，23pt sans bold；标准：墨右 ≤ 盒右缘且余量 ≥ +5px）

| 候选 | 墨宽 | 墨右 | 余量 | 结论 |
|---|---|---|---|---|
| D-01 “Números da semana” | 369.0 | 925.5 | **+35.5** | ✅ 采用 |
| D-01 “Números desta semana” | 402.0 | 958.5 | +2.5 | ❌ 余量不足（< +5） |
| D-01 “Esta semana, em números” | 434.0 | 990.5 | −29.5 | ❌ 更糟 |
| D-02 “Datas da semana” | 375.0 | 1382.0 | **+29.5** | ✅ 采用 |
| D-03 “Palavras frequentes” | 409.0 | 965.5 | −4.5 | ❌ 比原题还宽（“frequentes”宽于“da semana”） |
| D-03 “Palavras-chave” | 356.0 | 912.5 | **+48.5** | ✅ 采用 |
| D-03 “Palavras em destaque” | 431.0 | 987.5 | −26.5 | ❌ |
| D-03 “Vocabulário da semana” | 447.0 | 1003.5 | −42.5 | ❌ |
| D-03 原题降 22pt | 390.0 | 946.5 | +14.5 | 备用（未用：改字号会破 23pt 统一） |

- 改法均为缩短葡语标题、字号不动（23pt，与全刊其他盒标题一致；与 #3 的
  P4 C-head、P7 A2-head 同类修法）。
- 措辞：中文半句一字未动；葡语半句只缩短不改事实——“Números da semana”
  （本周数字）、“Datas da semana”（本周日期）、“Palavras-chave”（本周关键词）
  均与中文标题同义，无事实内容；D4（全球总决赛限定、Q56 键注
  `pela primeira vez num BO5 dos Worlds`）与 D5（S16 限定）所在行未碰，
  修复后逐项复核在位（见 GATE-LOG）。
- P7 另有一句 “Palavras da semana: …”（`content7.py:17`，词语回顾句）不是
  P5 盒标题，未动；text.md 中该句保留 1 次。

## 改动（scratch 副本内重建，确认后同步）

| 文件 | 改动 |
|---|---|
| `content12.py:47` | `f.box("数字看本周　Esta semana em números", [` → `f.box("数字看本周　Números da semana", [` |
| `content12.py:187` | `f.box("本周生活小日历　Datas desta semana", [` → `f.box("本周生活小日历　Datas da semana", [` |
| `content56.py:25` | `f.box("这一周的高频词　Palavras da semana", [` → `f.box("这一周的高频词　Palavras-chave", [` |

- 重建：scratch 副本 `run.py` RC=0，TOTAL 150（A2 56 / B1 69 / B2 25；
  页 10/18/18/18/18/18/12/38），0 FLOW OVERFLOW / 0 HEAD TOO WIDE；
  P7 teaser 2588.78、P8 keys 2552.7（与 #3 一致）；SVG 变化恰好 p1/p2/p5，
  其余 5 页与生产件逐字节一致；卡片变化恰好 p1/p2/p5。
- 印 PDF 在 scratch 副本内重建（`render-scratch.py`，BASE 已改向 scratch，
  未跑生产 `render.py`）；网 PDF 按要求不覆盖。

## 修后实测（双方法，裁决以交付 PDF 渲染像素为准）

| 缺陷 | 改后标题 | PIL 墨右 | PIL 余量 | 像素墨右（新印 PDF） | 像素盒缘 | 像素余量 |
|---|---|---|---|---|---|---|
| D-01 | 数字看本周　Números da semana | 925.5 | **+35.5** | 922.9 | 960.6 | **+37.8** |
| D-02 | 本周生活小日历　Datas da semana | 1382.0 | **+29.5** | 1381.1 | 1410.6 | **+29.4** |
| D-03 | 这一周的高频词　Palavras-chave | 912.5 | **+48.5** | 912.6 | 960.6 | **+48.0** |

- 标准：像素墨右 ≤ 盒右缘且余量 ≥ +5px——三项双法全部通过。
- PIL 全版横扫（新 SVG）：**0 旗**；最紧的非标题行余量 P1 +21.9、P2 +20.5、P5 +30.5。
- 像素法先用旧印 PDF 校验：复现 proof1 值在 0.7px 内（P1 982.4/960.6、
  P2 1415.7/1410.6、P5 963.8/960.6），方法有效才用于新 PDF。
  像素法两点修正（初版踩坑，见 GATE-LOG）：盒缘取盒顶无字条带而非标题行
  （标题字墨的抗锯齿晕边呈奶油色，会污染标题行盒缘扫描）；墨搜索限在
  [标题 x, 盒右+25] 且要求绿主导暗像素（排除中性 INK 正文与 P2 山谷照）。
- D-01 像素墨右（922.9）比 PIL（925.5）小 2.6px：像素橄榄阈值漏掉末字 “a”
  最淡的抗锯齿边缘；PIL 是更严的上界，仍余 +35.5，结论不受影响。
- 裁切目视（新印 PDF 150dpi 裁图 `render-new/crop-p1-numbox.png` 等）：
  三处标题均收进盒内、右侧留空明显；P1/P2/P5 整版 110dpi 目视无其他位移。

## 同步进生产（11 个文件；快照比对逐项核对）

开工快照 `snapshot-start.txt`（39 文件）→ 收工 `snapshot-end.txt` diff：
**恰好 11 个文件变化**，其余 28 个逐字节相同：

- 源码：`content12.py`、`content56.py`（各仅 1 处标题行；OUT 行仍为生产路径）
- SVG：`svg/p1-touiban.svg`、`svg/p2-shenghuo.svg`、`svg/p5-qingnian.svg`
- 卡片：`cards/p1-touiban.png`、`cards/p2-shenghuo.png`、`cards/p5-qingnian.png`
- 印 PDF：`Lucerna-VOL4-PT.pdf`
- 文本：`2026-w47-zh-cn-pt.text.md`（仅 3 行标题，行 47/271/915）
- KIT：`WEEKLY-KIT.md`（新 SHA + fix1 章节，旧 SHA 保留；“Visual — zero
  defects”改写；P2 旧量值“距照 23.7px”订正为对盒边；occlusion 盲区明示）

未变：网 PDF（见下）、`ABSTRACT.txt`、其余源码/SVG/卡片、assets。
生产 `__pycache__/` 只有开工前已有的 2 个 .pyc（2026-11-11 14:16），
本次凡 import 生产源码一律 `PYTHONDONTWRITEBYTECODE=1`，无新 .pyc 写入。
未 commit、未 push。

## 新三 SHA（生产盘上实测）

| 文件 | 字节 | SHA-256（修复后） | 旧值 |
|---|---|---|---|
| 印刷 PDF `Lucerna-VOL4-PT.pdf` | 41,734,802 | `6644cd43e033e99b27eb02f8bbaca9b470002eb40c9ebac12fed75a73cb7dccb` | 41,734,759 / `2286485f…4859c` |
| 网页 PDF `Lucerna-VOL4-PT-web.pdf` | 2,647,093（未变） | `030f52fb82087f8fe13f3465b74ee61b8c02b6e7d8a4740280ff7fa66cac76fa`（未变） | 同左 |
| 文本导出 `2026-w47-zh-cn-pt.text.md` | 50,834 | `ed0858346f731013dd8b8f6c5d4c85c15a3b6d7eae61099d62e36e3bd9808d94` | 50,846 / `9207974b…4cb71` |

- 网 PDF 未覆盖（任务要求）：它仍带 3 处旧标题，入仓前须由全家统一重建。
  新印 PDF 与旧网 PDF 的文字层在空白归一化后、把 3 处标题映射回去即逐字
  相同，词多重集之差恰好是 3 处标题的词（见 GATE-LOG）。

## 门禁逐项（实测值见 GATE-LOG.md）

rebuild RC=0 TOTAL 150；occlusion 0 旗（自检 OK；但对奶油盒盲，**不作**
三项修好的证据）；PIL 奶油盒横扫 0 旗；150dpi 像素三项全过（+37.8 /
+29.4 / +48.0）；p8 extract 150/150；p8 compare CLEAN；freeze diff 新增
CJK 0；freeze baseline 核心 8/8；文字层仅 3 处标题不同；P8 最小字号
9.98pt；徽章 135；U+2019 0；§1.1 干净；D4/D5 在位；#3 修复点全部存活。

## 未做事项（明示）

- 未重跑 `tools/webpdf.py`（网 PDF 按要求不覆盖，留待入仓前全家统一重建）。
- 未动 `tools/occlusion_audit.py`（BOXTITLE 对无描边奶油盒的盲区须工具线修；
  本次只修版，盲区已在 KIT 与 GATE-LOG 明示）。
- 未跑 `insert.py` / `lint --write`；未 commit、未 push。
