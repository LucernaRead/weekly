# DELTA-NOTE — 2026-W47 en-fr Q73 键同步 delta（core-en fix2）

- 版：`production/2026-w47/2026-w47-en-fr/`（只改这一版；核心、其他版、tools/ 未碰）。
- 唯一改动：`content56.py:49` Q73 键 `"speak"` → `"up"`；note（`speak up = parler franchement`）与题干（`Speak ___: tell a teacher.`）一字未动。其他源行、map/翻译文件、ABSTRACT.txt/KIT 以外文件未动。
- 核心对照（只读）：core-en `content56.py:49` 已为 `up`；本版改动与核心同形。
- 未 commit、未 push（10 版并行，git 操作由协调员统一做）。版内 WEEKLY-KIT.md 已更新（§7 新 SHA + §8 delta 条目 + §9 delta 门禁行）。
- Scratch：本目录（`scratch-delta-en-fr/`）；所有日志/证据在此，repo 侧 hidden_files 未写。

## 修前三 SHA（与 proof1 PROOF-NOTE 逐字节核对一致，动手前已验）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-fr.pdf`（印） | 29,330,979 | `76b4522c53a2fcad0a92f9b02180ff353dc73845ce57080cb7c1d2b0d263dd2f` |
| `The-Lucerna-VOL4-en-fr.web.pdf`（网） | 2,413,670 | `dd68f929b86af917626769bb52cad6ba34a0b6fe4e959a43279de4e319f83266` |
| `2026-w47-en-fr.text.md` | 53,809 | `2d832a170a229817af36c1c5378db7ef2030abd54bec54ab5cf019a6f0364855` |

修前三源同错已验（预期状态）：registry Q73 `key='speak'`；text.md:589 题干 `Speak ___: tell a teacher.`、附录 `73. [A2] Compléter — speak (speak up = parler franchement)`；P8 SVG `73. speak`；核心 en 已为 `up`。

## 修后三 SHA

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-fr.pdf`（印） | 29,330,985 | `0b4fded62123ee39ec97b8d4b7abd9c5c8e1f41184500a0aa76c25ee2678c693` |
| `The-Lucerna-VOL4-en-fr.web.pdf`（网） | 2,413,667 | `2d20b93df8f88596e1eec7915b7a2ea3d103176061cc35e7b24009c32e95a733` |
| `2026-w47-en-fr.text.md` | 53,806 | `ed8fd9ec8b706dfe961b5638fefe4e857f6493a01a312d2a7e8fdc0f0f0ff213` |

另：`registry.json` `41dc6d5ba8a803ca23217092479ea8f19c48e97e555952cf4ee37d2b56792ace`；`content56.py` `86383c4edd051a929194bd83edfd7d1d3e9c2f99000679250b486639df9f251e`。
修前 registry `58f67e95eca854e7506c9a2bd29a908e4ef81257ef658288c831fbf9ecbc51d9`（proof1 记录一致）。

## Diff 证据（各恰好 1 行；见 `diff-*.txt`）

- `content56.py`（`diff-content56.txt`）：`49c49`，仅 key `speak` → `up`。
- registry（`diff-registry.txt`）：`583c583`，仅 Q73 `"key": "speak"` → `"key": "up"`。
- text.md（`diff-textmd.txt`）：`1151c1151`，仅 `73. [A2] Compléter — speak (speak up = parler franchement)` → `… — up (…)`。
- SVG（`diff-svg.txt`）：8 页中仅 `p8-test.svg` 变化（`4978f960…` → `34acf55d…`）；其余 7 页字节一致。**p5 未变是正确且预期的**：Q73 的键只出现在 P8 答案页，从不上 P5 题干页（P5 只印 `Speak ___` 空白 + `speak up` 注记）——en-es delta 已证实此点（p8 含 `73. up`，p5 不变）。不要把 p5 未变当成异常，无需为此返工。

## Q73 四源证据（修后，全为 up）

| 源 | 实测 |
|---|---|
| registry | Q73 `{n: 73, page: 5, level: A2, type: Compléter, key: 'up', note: 'speak up = parler franchement'}` |
| text.md | :1151 `73. [A2] Compléter — up (speak up = parler franchement)`；:589 题干 `Speak ___: tell a teacher.` 不变 |
| P8 印出键 | `svg/p8-test.svg` `73. up`；印/网 PDF 文字层各含 `73. up` ×1；`73. speak` 在 registry/text.md/P8 SVG 中均为 0 命中 |
| P5 题干 + 注释 | `svg/p5-youth.svg` `Speak ___: tell a teacher.`；Note 盒 `speak up = parler franchement`；填入后 `Speak up: tell a teacher.` 语法正确 |

## 重建步骤

1. `tools/venv/bin/python run.py`（版内，TMPDIR=本 scratch/tmp）→ RC=0。
2. `tools/venv/bin/python render.py` → RC=0，印 PDF 29,330,985 B。
3. registry 重导：`dump_reg_delta.py`（`dump_reg.py` 的同款逻辑，出路改成本 scratch；随后 cp 到版内 `registry.json`）→ 150 条，页分布 10/17/18/18/18/18/12/39，级别 A2 62 / B1 66 / B2 22。
4. text.md 重导：`make_textmd_delta.py`（fanout/fr 原版复制，仅 SCRATCH 路径指向本 scratch）→ RC=0，53,806 B，stub registry 150 = real registry 150。
5. `tools/webpdf.py svg The-Lucerna-VOL4-en-fr.web.pdf` → RC=0，2,413,667 B，49,436 text bytes。

## 全部门禁表（全部独立重跑，日志在本目录）

| 门 | 结果 | 证据 |
|---|---|---|
| run.py | RC=0，0 OVERFLOW / 0 TOO WIDE，TOTAL 150，MODEL 82 | `build.log` |
| render.py | RC=0，印 PDF 8 页 1462.5×2025 pt | `render.log` |
| registry diff | 恰好 1 条（n=73 speak→up） | `diff-registry.txt` |
| text.md diff | 恰好 1 行（同上） | `diff-textmd.txt` |
| occlusion 审计 | **0 flags**，RC=0 | `occlusion.log` / `occlusion.json` |
| occlusion 自检 | OK：6 类阳性对照全触发，干净对照静默 | `occlusion-selftest.log` |
| p8 extract | **150/150**，noted set 60/150（与核心 noted 集相同） | `p8-extract.log` / `p8-extract.json` |
| p8 compare | **CLEAN**，missing=[] extra_count=0 uncertain=[]；keydiff=[137, 138, 139, 140, 150]（预期内，与 proof1 同） | `p8-compare.log` / `p8-compare.json` |
| p8 extract vs registry | 149/150 exact + #150 短标例外；mismatch=[] | `keycheck.log` |
| registry keys vs core | 145/150；diff 仅 137–140、150（读者语键，预期内）；Q38–41 = b/a/d/c；Q125=A，Q46=A，Q52=hosted，Q55=won，Q82/83/84=B/C/A | `keycheck.log` |
| freeze baseline | **8/8 SVGs byte-identical**（`--build` = 版自己的构建目录，含 run.py；core 对照另用 `--core-svg` 路径） | `freeze.log` / `freeze-baseline.json` / `freeze-final/` |
| freeze baseline（core 只读对照） | **8/8 SVGs byte-identical**：core-en 在 scratch 副本内重建、比对 core-en/svg 全等；核心文件未动（core p8 `73. up`、p5 `Speak ___`，与 fix2 一致） | `freeze-core.log` / `freeze-core.json` / `freeze-core/` / `core-svg-now.sha` |
| freeze diff vs core | p1 +34/−34、p2 +43/−54、p3 +26/−23、p4 +26/−22、p5 +25/−22、p6 +26/−21、p7 +66/−55、p8 +103/−98；**新增 CJK 共 9 个，全为 U+3000**（与 proof1 计数一致） | `freeze-diff.log` / `freeze-diff.json` |
| 印/网文字层 | pdftotext 印=网 48,073 字符；token 多重集差 0/0；逐页 byte-identical 8/8；-layout 印=网 108,899 B；网 < 7 MB | `printweb.log`、`print.txt`、`web.txt`、`print-nl.txt`、`web-nl.txt` |
| P8 最小字号 | PDF 有效最小 **10.12 pt**（P8 答案键块，0.75 缩放组内）；SVG 属性最小 13.5 pt；均 ≥ §1.1 下限 9.75 pt | `verify.log`、`scan.log` |
| keycheck | 见上（150/150 机械 + 下述人工抽查） | `keycheck.log` |
| 印/网逐页一致 | 8/8 页 identical（见 printweb.log） | `printweb.log` |
| creambox（原版） | RC=0，**0 OVERFLOW**；23 行负值全为 proof1 已裁定的假阳性集（-24.0 下块标题 ×1、-35.5 ×9、-36.0 ×2、-37.0 ×11）；SEARCHES 末基线 +12.0，DID YOU KNOW +14.3 | `creambox-all.log` |
| creambox_check（精炼版） | **NO OVERFLOW，RC=0**；P8 MODEL 盒 +92.4 | `creambox-check.log` |
| box-title | 源标题 12/12 fit（最紧 ODD SOCKS +4.8）；SVG 标题 18/18 fit，0 overflow | `boxtitle.log`、`boxtitle-svg.log` |
| §1.1 / P8 检查 | `check_s11.py fr` RC=0，**ALL §1.1/P8 CHECKS PASS** | `check_s11.log` |
| 字符/引号/禁词 | “ 82 / ” 82 成对；U+2019 0；ASCII 撇号 73；U+00B7 282；U+3000 141；可见文字真实 CJK 0；孤儿标点 0；`Note \| Note \|` 0；禁词 0；`encore changer` 0（合法 `encore` 仍 2 处：Q138 注、P7 读者来信注） | `scan.log` |
| VOL 计数 | VOL.4 12、VOL.5 8、VOL.3 3，逐页与 proof1 一致 | `scan.log` |
| ABSTRACT.txt | 775 B，一行 + 结尾换行，无 ASCII 双引号（未动） | `scan.log` |
| 150 题键与题干适配抽查 | 全部 44 个 `___` 填空/改写项逐项填入核对，键均合理（见下）；完形 Q112–119 逐项对段落核对，全对 | `fillcheck.log` |
| 8 页逐页目视 | 印版 P1–P8 全页 + 网版 P1/P8 目视：无溢出/重叠/压页脚；页脚 `Page N sur 8` 全 8 页正确；P8 答案块 `73. up` 在页内 | `render/print/p-1..8.png`、`render/web/p1-1.png`、`render/web/p8-8.png` |
| 像素范围 | vs proof1 旧渲染：P1–P7 **0 差异像素**；P8 仅 3,366 px（`73. speak`→`73. up` 一行） | `pixeldiff.log` |
| 网/印视觉 | 网版 P1/P8 目视与印版一致（像素数差为网 PDF 图片 JPEG 重压所致；文字层逐页 byte-identical） | `webdiff.log`、`render/web/` |
| D5 字体 | **只记录，不判**：P8 渲染有效最小字号 10.12 pt（属性 13.5 pt，0.75 缩放组内），≥ 9.75 pt 下限，与 proof1 同值，未变 | `verify.log` |

## 150 题填空/改写抽查（Q73 教训：三源一致不够，逐项填入）

- 方法：`fillcheck.py` 从 content 源解析全部 `f.ex`，列出所有含 `___` 的题（44 项：Compléter / Transformation / Phrases d'or / Comparatifs / Passé / Futur / Temps / Subordonnées），逐项把键填入题干核对语法与注记一致性；另对 P8 完形 Q112–119 逐项对段落原文核对（`content8.py` 段落 + 三选项）。
- 结果：44/44 合理，无问题。例：Q73 `Speak ___: tell a teacher.` + `up` → `Speak up: tell a teacher.`（注 `speak up = parler franchement` 一致）；Q70 `Break the silence: speak up about bullying.`；Q79 `Children are speaking up this week.`；Q52 `hosted`、Q55 `won`、Q112–119（Tuesday / call / continues / will meet / writes / will certify / wears / will watch）逐项对段落均唯一正确。
- 其余题型（配对 5 组、选择 Q120–128、阅读 Q129–132、句型 Q133–136、翻译 Q137–140、对话 Q145–149、写作 Q150）沿用 proof1 逐题结论，本轮未动其源，registry/P8 抽出键与 proof1 一致（keycheck 149/150 + #150 例外）。

## 结论

**Delta 完成，全部门禁绿，只此一改。** Q73 键已在 registry、text.md、P8 印出键、P5 题干注记四源同步为 `up`；SVG/PDF 变化范围仅 P8 一页；其余 7 页字节与像素均与 proof1 定稿一致。**可进 proof2。**
