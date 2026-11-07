# WEEKLY-KIT — 葡萄牙语周报 VOL.3 · PT × ZH-TW（繁体中文讲解层）

- 刊期：2026-W46，2026 年 11 月 9–15 日；仓库 slug：`2026-w46-pt-zh-tw`；目录：`files/weekly-report-w46-pt-zh-tw/`。
- 目标语：葡萄牙语（巴西变体正文，与核心版逐字相同）· 讲解层：繁体中文（台湾用字，由核心版简体中文讲解层经 OpenCC s2twp 转换 + 人工校读覆核，非机械转码）。
- 练习 150 道（A2 49 / B1 70 / B2 31；分版与核心版一致）；范文 88 词；金句 8 条与核心版相同（P7 繁体中文译文 + 页码标签）。
- 事实、图片、承诺处理与核心版完全一致，见核心版 KIT（`files/weekly-report-w46-pt-core/WEEKLY-KIT.md`）：Enem 第二天 + 共和国宣言日假期为主线；P4 次回合赛果未印（截稿注 + 顺延 VOL.4 的开放更新位）；读者来信为编辑部示例 + 双语披露（葡语披露原文保留，中文披露转为繁体）。
- W45 繁体版曾加的额外邀稿段落，本期未加——结构与核心版一致。

## 家具（本版）

- P1 副标题（330 行，38pt）：`葡 萄 牙 語 週 報 · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE`（1768px，合框）。
- P1 配对徽章（372 行，19.5pt，BRICK）：`葡萄牙語正文 · 繁體中文講解 — 給繁體中文讀者的版本`。
- 页脚：`A Lucerna · 葡萄牙語週報 VOL.3 · 正文葡萄牙語 · 講解繁體中文`；页码：`第 {n} 版 / 共 8 版`。
- Gloss 前缀：`譯注｜`；P8 分隔符保留葡语 `— PÁGINA {n} —`；disc 变量改名 `disc_tw`（披露文本由转换表产生）。
- svglib：由 W45 pt-zh-tw 构建目录复制（TC 字体面），与核心版差异仅字体面。
- 印刷版 PDF：`A-Lucerna-VOL3.pdf`；网页版：`A-Lucerna-VOL3-web.pdf`（tools/webpdf.py，真实文本层）。

## 变换与复现

构建目录：`hidden_files/weekly-report-w46-pt-zh-tw-build/`（由定稿核心构建目录复制）。`transform.py` 由生成器 `/tmp/gen_zh_tw_transform.py`（OpenCC s2twp 台湾配置）生成：转换表含 223 条简→繁字面（272 条 inventory 字面中 49 条本身已是繁简通用字，无需转换）；生成器内含 6 处人工校读覆核（覆習→複習、片語→詞組、分割槽→分區、檔案→文件、支援→支持、毛裡西奧→毛里西奧），覆核记录见生成器注释；另有 1 处生成器缺陷修复史（词盒垫锚点须用转换后字串，初版误用简体锚点致 transform 中途断言失败，已修生成器、重拷全新核心目录、单次重跑——transform 仅可在全新复制上运行一次）。

复现：重拷核心构建目录 + 复制 TC svglib → 运行生成器产出 transform.py → 运行 transform.py 一次 → 适配 gates → 渲染。P7 几何沿用核心值，P8 答案沿用核心 13.5pt。

## 门禁记录

- 构建自检 `gates.py`：17/17 PASS（由 `hidden_files/w46/adapt_gates.py` 生成，cjk-mode skip；注：本版 gates.py 另有一处手工修正——词表 headword 检查改为去空格比较，因繁体词表为“葡语词 + 空格 + 中文”格式且中文按字断行，去空格比较才是正确语义；原 `=` 切分假设不适用于本版，已记录，适配器未改）。
- 简体残留验证：全部转换后源文件 CJK 字串经 OpenCC 重转恒等（除 6 处有意覆核项）；`.text.md` 重转仅 1 字差异（支持之持，属有意覆核）。
- `tools/occlusion_audit.py`：0 flags。
- `tools/p8.py compare` vs 核心版：CLEAN（150/150；keydiff 仅 137/138 两道翻译题，键随读者语重定向，属正常）。
- `tools/freeze.py diff` vs 核心版：纯转换（276 删/276 增，0 条葡语正文改动）。
- Web PDF：`A-Lucerna-VOL3-web.pdf` 1,614,344 字节（<7 MB），pdftotext 43,019 字节，含真实文本层。
- 印刷版 PDF：`A-Lucerna-VOL3.pdf` 14,818,306 字节，保留于本目录（TC 字体嵌入所致）。
- `.text.md`：`2026-w46-pt-zh-tw.text.md`，由核心版 .text.md 经 transform 表 + 头行/示例句替换导出（`hidden_files/w46/derive_textmd.py`，allow_cjk=1；另有 `譯註｜`→`譯注｜` 对齐版面家具），已验无简体残留。
- ABSTRACT.txt：繁体中文单行，无 ASCII 双引号，含 masthead、目标语、A2–B2、150 题与真实话题。
- 未做 SOP §8 独立第二人校对——仅构建者自检。

## Round 1 校对后未改动验证记录（2026-11-02）

- 本版 Round 1 PASS，未重渲染、未修改。修复工 hash 复核：全部制品与修复前快照一致；核心 build 目录未动。
- 合法 CJK 标点保留已验：P8 10 条答案注 10/10 全角冒号 ：；SVG 全量 FF1A=54、U+3002=48（含 P8 42 处 ：），.text.md FF1A=9、U+3002=32。未重跑三门禁（制品未变）。
