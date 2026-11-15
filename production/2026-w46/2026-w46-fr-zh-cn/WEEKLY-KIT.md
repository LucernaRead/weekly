# WEEKLY-KIT — Le Lucerna · 法语周报 VOL.4 · 简体中文讲解版（分版）

- 目标语：法语（fr）；读者母语：简体中文（zh-cn）；期号 VOL.4，总第 4 期。
- 刊期：2026 年 11 月 9 日（周一）至 11 月 15 日（周日）；slug 周 `2026-w46`；frontmatter 周 `2026-W46`；weekStart `2026-11-09`，weekEnd `2026-11-15`。
- 刊名：`Le Lucerna`。版式：8 版，1950×2700，4 栏，页脚配对标识每版可见，P1 配对徽章可见。
- 练习：150 道（P1 10 · P2 15 · P3 18 · P4 18 · P5 17 · P6 18 · P7 12 · P8 42），分级 A2 52 · B1 75 · B2 23。

## 一、本版性质：与核心版文字相同

本版是核心版（`files/weekly-report-w46-fr-core/`）的文字相同分版：讲解层 `expl.py` 直接复用核心版文件（未改一字），`content*.py` 仅 OUT 路径不同，`svglib.py` 字节相同。构建目录 `hidden_files/weekly-report-w46-fr-zh-cn-build/` 由冻结的核心构建目录复制。

按任务书要求（11 个分版含 zh-cn，另有核心版目录），本版单独成目录；如协调员认定核心版即 zh-cn 版、勿重复入仓，可直接弃用本目录（见核心版 KIT §九.2）。

## 二、内容与承诺

与核心版 KIT §一、§二完全相同（P1–P8 内容、巴黎大师赛结果未出推迟至 VOL.5、预算周自我更正、读者园地编辑部示例 + 双语说明、日历节点）。事实来源与图片见核心版 KIT §三、§四。

## 三、门禁输出（实测，2026-11-02）

- `tools/freeze.py diff`（相对核心版）：**8/8 页零差异**（移除 0 条、新增 0 条，含 CJK 字符数相同）。
- `tools/p8.py compare`：**CLEAN**，keydiff `[]`（连 #150 写作题键也相同）。
- `tools/occlusion_audit.py`：**0 flags**。
- 大报版 PDF：8 页，23,643,152 字节，SHA-256 `5f5d1b0ac8610c10a15bb497f581434b1a3e6eccf82097932a24882ab8d943c4`——**与核心版大报版哈希完全相同**。
- 网页版 PDF（`tools/webpdf.py`）：8 页，2,057,412 字节（< 7 MB），SHA-256 `49f5bd0cff38415731d1e22418a8733e16aa59e28ec02d299d5fce084b6f698c`（与核心版网页版哈希不同，仅构建元数据差异）；pdftotext 46,196 字节，与核心版大报版文本逐字相同（`cmp` 校验通过）。
- 卡片：8 张 PNG（1950×2700），`cards/`。
- `.text.md`：45,517 字节（正文与核心版相同，仅 3 行头信息措辞不同，差 3 字节），由源稿导出器从 `content*.py` 源稿导出。
- `ABSTRACT.txt`：与核心版逐字相同（355 字节）。

## 四、待确认

与核心版 KIT §九相同：(1) 邮箱核实（读者园地示例/说明以前提“未收到 VOL.3 投稿”为真）；(2) 参议院正式投票日单源口径，VOL.5 以实际结果为准；(3) 本分版是否重复入仓，由协调员定夺。

## 补记：独立校对 Round 1 缺陷修复（2026-11-03，本地修复工）

独立校对 Round 1 结论见 `hidden_files/w46/fr-proofread-gates/proofreader-verdict-round1.md`（本版 FAIL，缺陷 D1）。以下修复均改构建源码后整版重渲染，未手改 SVG/PDF。构建脚本与门禁输出见 `hidden_files/w46/fr-fix/`（`apply_fixes.py`、`shorten_d2.py`、`render*.log`、`gates-final/`）。

### D1（全部 11 版 + 核心）——P3 第 37 题否定算子与事实冲突

源码：`hidden_files/weekly-report-w46-fr-build/content34.py` 及各母语版构建目录的 `content34.py`（除 OUT 路径外字节相同，12 份同步改动）+ 各版 `expl.py`。
改前题干：`(plus) La foire est à Paris. → ___`；P8 键：`La foire n'est plus à Paris.`——`ne...plus` 预设集市曾在巴黎，与本期通篇“集市在迪耶普”冲突。
改后题干：`(pas) La foire est à Paris. → ___`；P8 键：`La foire n'est pas à Paris.`（事实正确的否定为 `ne...pas`）。连带一致性改动：各版 `expl.py` 的 `bridge_neg` 删去 `/ ne...plus`（现仅列 `ne...jamais / ne...pas`），`n_neg3` 注记改为与各版 `n_neg2` 相同的 `ne...pas` 释义（原 `ne...plus` 释义已无对应题）。改后全版 SVG 文本中已无 `n'est plus` / `(plus)` / `ne...plus`。

### 重渲染与重验门禁（最终产物）

- 整版重渲染：8 SVG + 8 PNG 卡片 + 大报版 PDF（8 页，23643162 字节，SHA-256 前 12 位 `64007cac3b20`）+ 网页版 PDF（`tools/webpdf.py`，8 页，2057424 字节，SHA-256 前 12 位 `e56328087e18`，< 7 MB，带文字层）。`.text.md` 由源稿导出器从 `content*.py` 重生成（45503 字节，含新题干/新键，旧字符串已无），ABSTRACT.txt 未动（仍与本期主题相符）。
- `tools/freeze.py diff` vs 核心：裁定通过——P1–P7 移除的非 CJK 字符串仅标点碎片（`。`/`）。`）；P8 移除碎片均为答案键重排断行，由 p8 比对裁定；新增 CJK 字符 0 个；本版与核心 0 差异。
- `tools/p8.py compare`：CLEAN，核心与本版印出注记集均为 121/150，missing=[]、extra=0、uncertain=[]，keydiff=[]（仅 #150 写作题母语注记，属预期）。
- `tools/occlusion_audit.py`：0 旗标（每次运行自检 OK）；PDF 校验：8 页，文字层齐全，网页版与大报版 pdftotext 字节相等（46177 字节）。
- 改动页人工复核：P3 否定三题（题干/桥接语/ P8 键 37）逐项验过；未引入新缺陷。F-MAIL 旗标（读者来信邮箱核实）非文本缺陷，仍待协调员在入仓前核实，本次未动相关措辞。

## 补记：D5 字体重建（2026-11-15）

D5-only 重建：基线已是新样式（§1.1 已在 style-port 落仓），本次只换字体路由（拉丁/西里尔进 Newsreader、ru 进 Noto Sans、CJK 留 CJK 面）+ 只降字号修复 D5 引入的越框/重叠，零文案改动。装机与门禁见家族报告 `hidden_files/d5-redo/FAMILY-W46-FR-BUILD.md`。

### D5 交付物 pin（run2 终轮实测）

- 印 PDF（`render.py` 直出）：8 页，10,134,957 字节，SHA-256 `42fd77e0a86ea1ef5b02a913f69f391dbe7a5557576528bed190ec38315daa4d`。
- 网 PDF（`tools/webpdf.py`）：8 页，1,583,698 字节（< 7 MB），SHA-256 `9a086afce8e2c943ea1ad56e0c1f51f2b922b19e335bf6cfb7b6b6a5d254ccf5`。
- `.text.md`：45,357 字节，SHA-256 `bc53a38cc7a81f66bf889972f6063af0aee2f222944d6b7f3af60dd1361cde00`，与 `issues/2026-w46/2026-w46-fr-zh-cn/2026-w46-fr-zh-cn.text.md` 逐字节一致（取件：`2026-w46-fr-zh-cn.text.md.new` 新导出件；目录内同名 `.text.md` 为旧 fanout 产物，见家族报告 §8）。
- 基线印 PDF（修前生产版）：21,354,923 字节，SHA-256 `fbca7b272eddaa8c1337719ae2a438e7fd6be53f36d066c9ec112a9484c08979`。

### D5 重建记录

- 装机：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target fr --reader cn --week 2026-w46`（先 `--check` 干跑；core-fr 按读者 zh-cn 装 cjk）。`_D5_READER = "cjk"`（svglib.py:100）；fix2 保留（`_QUOTE_CLS`=4、`fix2`=5）；`test_d5_routing.py` **FAILURES: 0**。
- 修前普查：D5 Latin in CJK / Cyrillic in CJK = 417/0；curly_in_cjk 0/0。
- run1 15/19；修复 10 处（全为字号缩小），run2 19/19：
  - `content12.py:124` 25→24pt（探针余量 16.1px）：P1-budget head HDW
  - `content34.py:76` 23→21pt（探针余量 14.0px）：P3 mots_fetes creambox +24.8/+22.8
  - `content34.py:84` 23→22pt（探针余量 9.8px）：P3 zoom creambox +7.6
  - `content56.py:80` 23→20pt（探针余量 14.6px）：P5 cine creambox +57.3/+43.3
  - `content56.py:159` 25→23pt（探针余量 11.5px）：P6-opinion head HDW
  - `content56.py:165` 25→24pt（探针余量 12.4px）：P6-micro head HDW
  - `content7.py:38` 24→23pt（探针余量 11.5px）：P7-B2 head HDW
  - `content7.py:89` 25→23pt（探针余量 3.6px）：P7-clinic head HDW
  - `content34.py:161` 加 `tsize=21`（默认 23→21pt，探针余量 2.0px）：P4 COMMENTATEUR f.box tsize 23->21
  - `content56.py:189` 加 `tsize=21`（默认 23→21pt，探针余量 12.8px）：P6 3dates f.box tsize 23->21
