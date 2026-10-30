# 周报内容 Agent 指南

## 开始前

- 先读 README.md。本仓只维护内容(周报各版本的元数据与 PDF),不放站点代码。
- 一版能不能进仓,只看一条:它在生产端已经走完周报 SOP —— 独立校对
  完整一轮零问题、几何遮挡审计零标记。没过门的版不要往这里放。

## 加一版

1. 建目录 `issues/<week 小写>/<week 小写>-<目标语>-<母语>/`(如 `issues/2026-w43/2026-w43-fr-zh-cn/`)—— 周次本身是一层。
2. 写 `<slug>.md`:frontmatter 字段照 README,一个不能少。
   pdfBytes 与 pdfSha256 从**最终定稿**的网页版 PDF 实测(SHA-256 全小写)。
3. 有 PDF 实体要一并提交时,文件名必须是 `<slug>.pdf`,放进同一目录。
4. 正文 md:把这一版的正文导出成 `<slug>.text.md`,放进同一目录(lint 规则 9)。
   - 站点把它渲染成单期页的正文给人读、给搜索引擎读;没有它,站点只能退回 PDF 抽出的文字,版面乱、默认收起。
   - 从生产端的源稿导出,标题、段落、练习按原顺序写成 markdown;不要从 PDF 反抽。
   - 不许是空文件。lint 会把路径、字节数、SHA-256 写进 index 的 `text` 字段。
5. 跑 `node lint.mjs --write`,再跑 `node lint.mjs` 确认绿;把生成的
   index.json 和 md 一起提交。**不要手工编辑 index.json。**
6. 提交钩子会重算索引,不得跳过。提交前看 git diff,别混入无关文件。

## 加封面

每周每种读者语言一份网站封面块。封面块是那一周 12 种学习语言头版的快照,
站点把它放在周报页最上面,读者点哪一篇报道,就进那种学习语言、用封面读者语言讲解的那一版。

1. 建目录 `covers/<week 小写>/<week 小写>-cover-<读者语言>/`(如 `covers/2026-w45/2026-w45-cover-en/`)。
2. 放一份 `<目录名>.html`:自包含的静态封面块。
   - 零交互(lint 规则 5):不许有脚本、按钮、链接、表单、导航、页脚、侧栏、点击事件。
     入口由站点加,封面块里不写链接。
   - 每篇报道是一个 `<article>`,12 种学习语言各一篇。
   - `<body>` 上写 `data-story-langs="…"`(lint 规则 8):按文档顺序列出每个 `<article>`
     是哪种学习语言,用 README 里的语言代码,空格分隔,12 个各出现一次。
     例:`<body data-story-langs="de fr es en it pt nl ru ja ko zh-cn zh-tw">`。
     版式换了、报道顺序变了,这一行跟着改;顺序错了,读者会被带进错误的一版。
   - 要配图的报道,在那篇 `<article>` 的占位元素上加 `data-image-slot`(lint 规则 10)。
     不带值:是哪种学习语言,由 `data-story-langs` 的顺序推出。每篇至多一个,不许放在 `<article>` 外。
     例:`<div class="plate" data-image-slot aria-hidden="true"><span class="mast">La Lucerna</span></div>`。
     占位元素里的内容照常写:还没有图时,站点原样显示它。
3. 印刷版封面(可选)放同一目录:`<目录名>.md` 与一份 PDF。
4. 跑 `node lint.mjs --write`,再跑 `node lint.mjs` 确认绿。lint 会把这份封面写进
   `index.json` 的 `covers`:`slug`、`week`、`lang`、`html` 路径,以及 html 的字节数与 SHA-256
   (从文件实算,不手填)。站点按 SHA-256 验真,所以封面块改一个字节都要重跑 `--write`。
5. 提交 html 和 index.json。**不要手工编辑 index.json。**

## 加报道配图

每周每种学习语言一张图,配那一周这种学习语言的那篇报道。
12 份封面共用这 12 张图:站点把图填进每份封面里那篇报道的 `data-image-slot`。

1. 读那一周任意一份封面里这种学习语言的那篇报道(标题和摘要),按内容生成一张图。
2. 图的规格:
   - 横版 3:2(建议 1200×800 像素)。站点按「裁切填满」放进图片位,四边可能各裁掉一点,主体放中间。
   - 图里不放文字。12 种读者语言的封面共用这张图,文字只对一种读者有用。
   - 格式 WebP,文件 ≤ 400 KB(按文件字节数)。超了就降质量重压,不要缩到 800 像素宽以下。
3. 存为 `covers/<week 小写>/images/<学习语言>.webp`(如 `covers/2026-w45/images/it.webp`)。
   文件名只用 README 里的语言代码,一种学习语言一张。
4. 跑 `node lint.mjs --write`,再跑 `node lint.mjs` 确认绿。lint 会把图写进 `index.json` 的
   `coverImages`:`week`、`lang`、路径、字节数、SHA-256。
5. 提交图和 index.json。可以分批提交:缺图的报道,站点照常显示占位元素。
6. 换一张已提交的图:直接覆盖同名文件,重跑第 4 步。站点按 SHA-256 取新图。

## 不许做的事

- 不许改已入仓版本的 frontmatter 来「修正」历史 —— 版有错,走生产端的
  更正流程出新文件,再更新 md 的 pdfBytes/pdfSha256 并注明。
- 不许出现简繁互译的配对目录(zh-cn × zh-tw):lint 会拦,也不要试图绕过。
- 不许把各版的印刷版 PDF 放进 `issues/`(印刷版封面例外,放在 `covers/` 的封面目录里)。
